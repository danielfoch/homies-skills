#!/usr/bin/env python3
"""Deterministic cleanup for the remaining Pop & Dance C2 source.

The authored Rickrolling motion already reads correctly, but cell 2 contains a
second generated face/hair fragment behind the real head.  Reuse the clean head
from cell 3 at the identical coordinates and leave the dancing body/pointing arm
untouched.  Output stays in /tmp until independent full/128/GIF QA approves it.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
OUT = Path("/tmp/pop-dance-redo-c/final/rickrolling-manager.png")
CELL = 627
GREEN = (0, 255, 0)


def foreground_mask(image: Image.Image) -> Image.Image:
    rgb = np.asarray(image.convert("RGB"), dtype=np.int16)
    green = (
        (rgb[..., 1] > 120)
        & (rgb[..., 1] > rgb[..., 0] * 1.30)
        & (rgb[..., 1] > rgb[..., 2] * 1.30)
        & ((rgb[..., 1] - np.maximum(rgb[..., 0], rgb[..., 2])) > 35)
    )
    return Image.fromarray(np.where(green, 0, 255).astype(np.uint8), "L")


def main() -> None:
    source = Image.open(
        ROOT / "sources/wildcard/rickrolling-manager.png"
    ).convert("RGB")
    if source.size != (CELL * 2, CELL * 2):
        raise ValueError(f"unexpected source size: {source.size}")

    cell2 = source.crop((0, CELL, CELL, CELL * 2))
    cell3 = source.crop((CELL, CELL, CELL * 2, CELL * 2))

    # This tight shape covers the duplicate fragment, canonical head, ears, and
    # neck but stops above the coat lapels and moving pointing shoulder.
    points = [(258, 82), (342, 82), (342, 166), (328, 190), (282, 190), (258, 168)]
    region = Image.new("L", (CELL, CELL), 0)
    ImageDraw.Draw(region).polygon(points, fill=255)

    repaired = cell2.copy()
    repaired.paste(GREEN, (0, 0, CELL, CELL), region)
    donor_mask = Image.fromarray(
        np.minimum(
            np.asarray(region, dtype=np.uint8),
            np.asarray(foreground_mask(cell3), dtype=np.uint8),
        ),
        "L",
    )
    repaired.paste(cell3, (0, 0), donor_mask)

    result = source.copy()
    result.paste(repaired, (0, CELL))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    result.save(OUT, optimize=True)
    print(OUT)


if __name__ == "__main__":
    main()
