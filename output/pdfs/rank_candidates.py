import csv
import re
from collections import defaultdict


def pct(value):
    value = value or ""
    match = re.search(r"-?\d+(?:\.\d+)?%", value)
    if not match:
        return None
    return float(match.group(0).rstrip("%"))


def status_score(value):
    value = value or ""
    if "扭亏" in value or "转正" in value or "同比扭亏" in value:
        return 80
    if "减亏" in value:
        return 30
    if "亏损扩大" in value or "转亏" in value or "由盈转亏" in value:
        return -80
    return 0


def row_score(row):
    npy = pct(row["np_yoy_2q26"])
    revy = pct(row["rev_yoy_2q26"])
    score = 0
    if npy is not None:
        score += min(npy, 500) * 0.70
    else:
        score += status_score(row["np_yoy_2q26"])
    if revy is not None:
        score += min(revy, 250) * 0.20
    if "V" in row["beat"] or "√" in row["beat"]:
        score += 60
    return score


rows = list(csv.DictReader(open("tmp/pdfs/main_anchor_rows.csv", encoding="utf-8")))
for row in rows:
    row["score"] = row_score(row)
    row["np_pct"] = pct(row["np_yoy_2q26"])
    row["rev_pct"] = pct(row["rev_yoy_2q26"])

good = sorted(rows, key=lambda row: row["score"], reverse=True)
bad = sorted(rows, key=lambda row: (row["np_pct"] if row["np_pct"] is not None else status_score(row["np_yoy_2q26"]), row["rev_pct"] if row["rev_pct"] is not None else -999))

print("TOP GOOD")
for row in good[:80]:
    print(row["score"], row["plate"], row["subindustry"], row["company"], row["rev_2q26"], row["rev_yoy_2q26"], row["np_2q26"], row["np_yoy_2q26"], row["beat"], row["logic"][:50])

print("\nTOP BAD")
for row in bad[:80]:
    print(row["score"], row["plate"], row["subindustry"], row["company"], row["rev_2q26"], row["rev_yoy_2q26"], row["np_2q26"], row["np_yoy_2q26"], row["beat"], row["logic"][:50])

by_plate = defaultdict(list)
for row in rows:
    by_plate[row["plate"]].append(row)

print("\nPLATE SUMMARY")
for plate, plate_rows in sorted(by_plate.items(), key=lambda kv: sum(r["score"] for r in kv[1]) / max(len(kv[1]), 1), reverse=True):
    nums = [r["np_pct"] for r in plate_rows if r["np_pct"] is not None]
    revs = [r["rev_pct"] for r in plate_rows if r["rev_pct"] is not None]
    beat_count = sum(1 for r in plate_rows if "V" in r["beat"] or "√" in r["beat"])
    avg_score = sum(r["score"] for r in plate_rows) / len(plate_rows)
    median_np = sorted(nums)[len(nums) // 2] if nums else None
    print(plate, "n", len(plate_rows), "avg", round(avg_score, 1), "median_np", median_np, "beat", beat_count)
