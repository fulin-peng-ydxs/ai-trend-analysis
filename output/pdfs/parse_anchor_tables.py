import csv
import json
import re
from pathlib import Path


OCR_PATH = Path("tmp/pdfs/ocr_all_zh.json")
OUT_CSV = Path("tmp/pdfs/main_anchor_rows.csv")
OUT_JSON = Path("tmp/pdfs/main_anchor_rows.json")

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

NUMERIC_COLS = {
    "rev_2q26",
    "rev_2026",
    "rev_yoy_2q26",
    "rev_yoy_2026",
    "np_2q26",
    "np_2026",
    "np_yoy_2q26",
    "np_yoy_2026",
    "beat",
}


def has_cjk(text):
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def has_numberish(text):
    return bool(re.search(r"\d|%|亏|扭|减|转|NA", text, re.I))


def norm_text(text):
    text = text.replace("\n", " ").replace("|", "")
    return " ".join(text.split()).strip()


def top_center(item):
    return 1 - (item["y"] + item["height"] / 2)


def x_center(item):
    return item["x"] + item["width"] / 2


def cell_for_x(xc):
    for name, left, right in COLS:
        if left <= xc < right:
            return name
    return None


def clean_company(text):
    text = norm_text(text)
    text = text.replace("公司简称", "").strip()
    return text


def is_company_token(item):
    xc = x_center(item)
    if not (0.0878 <= xc < 0.1548):
        return False
    text = clean_company(item["text"])
    if not text:
        return False
    if text in KNOWN_PLATES:
        return False
    if any(key in text for key in ["公司简称", "收入", "预测", "子行业", "增速", "净利润"]):
        return False
    return has_cjk(text) or bool(re.search(r"[A-Za-z]{2,}", text))


def is_plate_token(item):
    return norm_text(item["text"]) in KNOWN_PLATES


def join_cell(items, name):
    if not items:
        return ""
    ordered = sorted(items, key=lambda item: (top_center(item), x_center(item)))
    texts = [norm_text(item["text"]) for item in ordered if norm_text(item["text"])]
    if name in NUMERIC_COLS:
        return "".join(texts)
    return " ".join(texts)


def main():
    data = json.loads(OCR_PATH.read_text(encoding="utf-8"))
    by_page = {}
    for item in data:
        if 1 <= item["page"] <= 15:
            by_page.setdefault(item["page"], []).append(item)

    rows = []
    current_plate = ""

    for page in range(1, 16):
        items = by_page.get(page, [])
        plate_events = sorted(
            [(top_center(item), norm_text(item["text"])) for item in items if is_plate_token(item)]
        )

        company_items = sorted([item for item in items if is_company_token(item)], key=top_center)
        anchors = []
        for item in company_items:
            text = clean_company(item["text"])
            tc = top_center(item)
            if anchors and abs(tc - anchors[-1]["y"]) < 0.005:
                anchors[-1]["items"].append(item)
                anchors[-1]["text"] = clean_company(anchors[-1]["text"] + " " + text)
                anchors[-1]["y"] = sum(top_center(x) for x in anchors[-1]["items"]) / len(anchors[-1]["items"])
            else:
                anchors.append({"y": tc, "items": [item], "text": text})

        # Remove obvious non-data anchors by requiring at least one number/status nearby.
        filtered = []
        for anchor in anchors:
            nearby = [
                item
                for item in items
                if 0.1548 <= x_center(item) < 0.6540 and abs(top_center(item) - anchor["y"]) < 0.025
            ]
            if any(has_numberish(norm_text(item["text"])) for item in nearby):
                filtered.append(anchor)
        anchors = filtered

        sub_tokens = []
        for item in items:
            text = norm_text(item["text"])
            xc = x_center(item)
            if xc < 0.0878 and has_cjk(text) and text not in KNOWN_PLATES:
                if not any(key in text for key in ["子行业", "同比", "增速", "扭亏", "转正", "减亏", "亏损"]):
                    sub_tokens.append((top_center(item), text))

        anchor_ys = [anchor["y"] for anchor in anchors]
        for index, anchor in enumerate(anchors):
            prev_y = anchor_ys[index - 1] if index > 0 else max(0, anchor["y"] - 0.035)
            next_y = anchor_ys[index + 1] if index + 1 < len(anchor_ys) else min(1, anchor["y"] + 0.035)
            top_mid = (prev_y + anchor["y"]) / 2 if index > 0 else 0
            bottom_mid = (anchor["y"] + next_y) / 2 if index + 1 < len(anchor_ys) else 1
            # OCR centers are slightly noisy. Cap row bands so header labels and adjacent rows do not bleed in.
            top = max(top_mid, anchor["y"] - 0.012)
            bottom = min(bottom_mid, anchor["y"] + 0.012)

            for event_y, plate in plate_events:
                if event_y <= anchor["y"]:
                    current_plate = plate

            row_items = [item for item in items if top <= top_center(item) < bottom]
            cells = {name: [] for name, _, _ in COLS}
            for item in row_items:
                col = cell_for_x(x_center(item))
                if col:
                    cells[col].append(item)

            record = {
                "page": page,
                "plate": current_plate,
                "subindustry": "",
                "company": anchor["text"],
                "row_y": round(anchor["y"], 5),
            }
            for name, _, _ in COLS:
                if name == "company":
                    continue
                record[name] = join_cell(cells[name], name)

            if sub_tokens:
                nearest_sub = min(sub_tokens, key=lambda token: abs(token[0] - anchor["y"]))
                if abs(nearest_sub[0] - anchor["y"]) < 0.12:
                    record["subindustry"] = nearest_sub[1]

            numeric_count = sum(1 for name in NUMERIC_COLS - {"beat"} if record.get(name))
            if numeric_count >= 3:
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
        "row_y",
    ]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    OUT_JSON.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"rows={len(rows)}")
    for row in rows[:30]:
        print(
            row["page"],
            row["plate"],
            row["subindustry"],
            row["company"],
            row["rev_2q26"],
            row["rev_2026"],
            row["rev_yoy_2q26"],
            row["np_2q26"],
            row["np_yoy_2q26"],
            row["beat"],
        )


if __name__ == "__main__":
    main()
