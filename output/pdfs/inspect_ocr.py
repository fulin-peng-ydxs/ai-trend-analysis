import json
import re
from pathlib import Path


def has_cjk(text):
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def main():
    data = json.loads(Path("tmp/pdfs/ocr_all_zh.json").read_text(encoding="utf-8"))
    for page in range(1, 23):
        items = [item for item in data if item["page"] == page and has_cjk(item["text"])]
        heads = [
            item
            for item in items
            if item["y"] > 0.88 or (0.43 < item["x"] < 0.57 and len(item["text"]) <= 10)
        ]
        print("PAGE", page)
        for item in sorted(heads, key=lambda row: (-row["y"], row["x"]))[:30]:
            print(" ", round(item["x"], 3), round(item["y"], 3), item["text"])


if __name__ == "__main__":
    main()
