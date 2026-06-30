import sys
from pathlib import Path

import numpy as np
from PIL import Image


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


def main():
    image_path = Path(sys.argv[1] if len(sys.argv) > 1 else "tmp/pdfs/26h1-page-01.png")
    im = Image.open(image_path).convert("RGB")
    arr = np.array(im)
    h, w = arr.shape[:2]
    dark = (arr[:, :, 0] < 80) & (arr[:, :, 1] < 80) & (arr[:, :, 2] < 130)

    col = dark.sum(axis=0)
    xs = np.where(col > h * 0.20)[0]
    xgroups = groups_from_indices(xs)
    print("size", w, h)
    print("vertical")
    for start, end in xgroups:
        print(round((start + end) / 2 / w, 5), start, end, int(col[start : end + 1].max()))

    row = dark.sum(axis=1)
    ys = np.where(row > w * 0.45)[0]
    ygroups = groups_from_indices(ys)
    print("horizontal", len(ygroups))
    for start, end in ygroups[:120]:
        print(round((start + end) / 2 / h, 5), start, end, int(row[start : end + 1].max()), end - start + 1)


if __name__ == "__main__":
    main()
