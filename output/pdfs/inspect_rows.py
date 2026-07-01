import collections
import csv


rows = list(csv.DictReader(open("tmp/pdfs/main_anchor_rows.csv", encoding="utf-8")))
print("total", len(rows))
print("by page", collections.Counter(row["page"] for row in rows))
print("by plate", collections.Counter(row["plate"] for row in rows))
for page in range(1, 16):
    page_rows = [row for row in rows if row["page"] == str(page)]
    print("PAGE", page, len(page_rows))
    print("  first:", " | ".join(row["company"] for row in page_rows[:10]))
    print("  last :", " | ".join(row["company"] for row in page_rows[-8:]))
