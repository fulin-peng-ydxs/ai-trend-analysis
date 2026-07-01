import csv
import json
import re
from pathlib import Path

import numpy as np
from PIL import Image


OCR_PATH = Path("tmp/pdfs/ocr_all_zh.json")
IMAGE_PATTERN = "tmp/pdfs/26h1-page-{page:02d}.png"
OUT_CSV = Path("tmp/pdfs/main_rows.csv")
OUT_JSON = Path("tmp/pdfs/main_rows.json")

KNOWN_PLATES = {
    "电子",
    "通信",
    "计算机",
    "传媒互联网",
    "非银",
    "医药",
    "电新",
    "机械",
    "具身智能",
    "汽车",
    "军工",
    "交运",
    "建材新材料",
    "公用事业",
    "有色金属",
    "石油石化",
    "化工",
    "商贸零售",
    "纺服美护",
    "食品饮料",
    "农林牧渔",
    "家电",
}

COLS = [
    ("subindustry", 0.000, 0.0878),
    ("company", 0.0878, 0.1548),
    ("rev_2q26", 0.1548, 0.2078),
    ("rev_2026", 0.2078, 0.2672),
    ("rev_yoy_2q26", 0.2672, 0.3110),
    ("rev_yoy_2026", 0.3110, 0.3537),
    ("np_2q26", 0.3537, 0.4194),
    ("np_2026", 0.4194, 0.4801),
    ("np_yoy_2q26", 0.4801, 0.5348),
    ("np_yoy_2026", 0.5348, 0.5895),
    ("beat", 0.5895, 0.6540),
    ("logic", 0.6540, 1.0000),
]


def has_cjk(text):
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def norm_text(text):
    text = text.replace("\n", " ").replace("|", "")
    return " ".join(text.split()).strip()


def groups_from_indices(indices, gap=2):
    groups = []
    start = None
    prev = None
    for value in indices:
        value = int(value)
        if start is None:
            start = prev = value
        elif value - prev > gap:
            groups.append((start, prev))
            start = prev = value
        else:
            prev = value
    if start is not None:
        groups.append((start, prev))
    return groups


def horizontal_lines(page):
    image = Image.open(IMAGE_PATTERN.format(page=page)).convert("RGB")
    arr = np.array(image)
    height, width = arr.shape[:2]
    dark = (arr[:, :, 0] < 100) & (arr[:, :, 1] < 100) & (arr[:, :, 2] < 140)
    row_count = dark.sum(axis=1)
    indices = np.where(row_count > width * 0.25)[0]
    groups = groups_from_indices(indices, gap=2)
    lines = sorted({round((start + end) / 2 / height, 5) for start, end in groups})
    return lines


def cell_for_x(x_center):
    for name, left, right in COLS:
        if left <= x_center < right:
            return name
    return None


def top_center(item):
    return 1 - (item["y"] + item["height"] / 2)


def x_center(item):
    return item["x"] + item["width"] / 2


def join_cell(items, name):
    if not items:
        return ""
    ordered = sorted(items, key=lambda item: (top_center(item), x_center(item)))
    texts = [norm_text(item["text"]) for item in ordered if norm_text(item["text"])]
    if name in {
        "rev_2q26",
        "rev_2026",
        "rev_yoy_2q26",
        "rev_yoy_2026",
        "np_2q26",
        "np_2026",
        "np_yoy_2q26",
        "np_yoy_2026",
        "beat",
    }:
        return "".join(texts)
    return " ".join(texts)


def is_header_company(text):
    bad = {"公司简称", "子行业", "收入预测", "收入同比增速", "归母净利润预测"}
    return not text or text in bad or "公司简称" in text or "预测" in text


def main():
    data = json.loads(OCR_PATH.read_text(encoding="utf-8"))
    by_page = {}
    for item in data:
        if 1 <= item["page"] <= 15:
            by_page.setdefault(item["page"], []).append(item)

    rows = []
    current_plate = ""
    previous_page_subindustry = ""

    for page in range(1, 16):
        items = by_page.get(page, [])
        plate_events = []
        for item in items:
            text = norm_text(item["text"])
            if text in KNOWN_PLATES:
                plate_events.append((top_center(item), text))
        plate_events.sort()

        sub_tokens = []
        for item in items:
            xc = x_center(item)
            text = norm_text(item["text"])
            if xc < 0.085 and has_cjk(text) and text not in KNOWN_PLATES and text not in {"子行业"}:
                if "同比" not in text and "增速" not in text and "扭亏" not in text:
                    sub_tokens.append((top_center(item), text))

        lines = horizontal_lines(page)
        if len(lines) < 2:
            continue

        for top, bottom in zip(lines, lines[1:]):
            if bottom - top < 0.006:
                continue

            row_items = []
            for item in items:
                tc = top_center(item)
                if top < tc < bottom:
                    row_items.append(item)

            if not row_items:
                continue

            for event_top, plate in plate_events:
                if event_top <= (top + bottom) / 2:
                    current_plate = plate

            cells = {name: [] for name, _, _ in COLS}
            for item in row_items:
                col = cell_for_x(x_center(item))
                if col:
                    cells[col].append(item)

            record = {
                "page": page,
                "plate": current_plate,
                "row_top": round(top, 5),
                "row_bottom": round(bottom, 5),
            }
            for name, _, _ in COLS:
                record[name] = join_cell(cells[name], name)

            company = record["company"]
            if is_header_company(company):
                continue
            # OCR sometimes assigns continuation text from the logic column to rows without company data.
            if not has_cjk(company) and not re.search(r"[A-Za-z]{2,}", company):
                continue

            row_mid = (top + bottom) / 2
            nearest_sub = None
            if sub_tokens:
                nearest_sub = min(sub_tokens, key=lambda token: abs(token[0] - row_mid))
            if record["subindustry"] and record["subindustry"] not in {"子行业"}:
                previous_page_subindustry = record["subindustry"]
            elif nearest_sub and abs(nearest_sub[0] - row_mid) < 0.11:
                record["subindustry"] = nearest_sub[1]
            elif previous_page_subindustry:
                record["subindustry"] = previous_page_subindustry

            rows.append(record)

    fieldnames = [
        "page",
        "plate",
        "subindustry",
        "company",
        "rev_2q26",
        "rev_2026",
        "rev_yoy_2q26",
        "rev_yoy_2026",
        "np_2q26",
        "np_2026",
        "np_yoy_2q26",
        "np_yoy_2026",
        "beat",
        "logic",
        "row_top",
        "row_bottom",
    ]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    OUT_JSON.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"rows={len(rows)}")
    for row in rows[:20]:
        print(row["page"], row["plate"], row["subindustry"], row["company"], row["rev_2q26"], row["rev_yoy_2q26"], row["np_2q26"], row["np_yoy_2q26"], row["beat"])


if __name__ == "__main__":
    main()
