import json
from pathlib import Path

import pdfplumber


PDF_PATH = Path(
    "/Users/pengshuaifeng/Library/Containers/com.tencent.xinWeChat/Data/Library/Caches/"
    "com.tencent.xinWeChat/2.0b4.0.9/47177405b304c7d4f2337aad30b222d8/SaveTemp/"
    "9e7ed7afe087c394b03a0efc4add33ee/26中报业绩预测汇总0630.pdf"
)
OUT_DIR = Path("tmp/pdfs")


def norm_cell(value):
    if value is None:
        return ""
    return " ".join(str(value).replace("\n", " ").split())


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    settings = {
        "vertical_strategy": "lines",
        "horizontal_strategy": "lines",
        "snap_tolerance": 3,
        "join_tolerance": 3,
        "edge_min_length": 3,
        "intersection_tolerance": 4,
        "text_x_tolerance": 2,
        "text_y_tolerance": 3,
    }
    pages = []
    with pdfplumber.open(PDF_PATH) as pdf:
        for page_index, page in enumerate(pdf.pages, start=1):
            tables = page.extract_tables(table_settings=settings)
            page_tables = []
            for table in tables:
                rows = [[norm_cell(cell) for cell in row] for row in table]
                page_tables.append(rows)
            pages.append(
                {
                    "page": page_index,
                    "text": page.extract_text(x_tolerance=2, y_tolerance=3) or "",
                    "tables": page_tables,
                }
            )

    (OUT_DIR / "26h1_tables.json").write_text(
        json.dumps(pages, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    summary = []
    for page in pages:
        summary.append(f"PAGE {page['page']} tables={len(page['tables'])}")
        for i, table in enumerate(page["tables"], start=1):
            cols = max((len(r) for r in table), default=0)
            summary.append(f"  table {i}: rows={len(table)} cols={cols}")
            for row in table[:5]:
                summary.append("    " + " | ".join(row))
    print("\n".join(summary))


if __name__ == "__main__":
    main()
