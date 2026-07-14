#!/usr/bin/env python3
"""Build three anti-wiggle Pop & Dance repairs from one intact character plate.

These concepts are full-body groove/bounce actions.  Reusing a single accepted
plate and applying deliberate foot-pivot transforms makes the motion readable at
128px without allowing the face, clothing, limbs or shoes to redraw each frame.
Outputs are staged under /tmp until the independent visual gate approves them.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
OUT = Path("/tmp/pop-dance-redo-rigid/final")
CELL = 627
GREEN = (0, 255, 0)


PHASES: dict[str, list[tuple[float, int, int]]] = {
    # angle, dx, dy; all rotations pivot at the same planted-foot baseline.
    # Oops is intentionally excluded: whole-character pivots were rejected and
    # replaced by the fixed-body elbow rig in repair_oops_chest_reach.py.
    "good-as-hell-ing-marketing": [
        (-2.8, -6, 0), (-0.8, -2, -7), (2.8, 6, 0), (0.8, 2, -4),
    ],
    "dont-start-now-ing-listings": [
        (-4.0, -9, 0), (-1.3, -3, -5), (4.0, 9, 0), (1.3, 3, -3),
    ],
    "pon-de-replaying-crm": [
        (-3.8, -8, 0), (-1.0, -2, -6), (3.8, 8, 0), (1.0, 2, -3),
    ],
}


def first_cell(slug: str) -> Image.Image:
    source = Image.open(ROOT / "sources/wildcard" / f"{slug}.png").convert("RGB")
    return source.crop((0, 0, CELL, CELL))


def keyed_rgba(source: Image.Image) -> Image.Image:
    rgb = np.asarray(source.convert("RGB"), dtype=np.uint8)
    # Generated masters use literal chroma green. A small tolerance removes the
    # antialiased key fringe while retaining all four selected costumes.
    key = (rgb[..., 1] > 180) & (rgb[..., 1] > rgb[..., 0] * 1.45) & (rgb[..., 1] > rgb[..., 2] * 1.45)
    alpha = np.where(key, 0, 255).astype(np.uint8)
    return Image.fromarray(np.dstack([rgb, alpha]), "RGBA")


def transformed(plate: Image.Image, angle: float, dx: int, dy: int) -> Image.Image:
    bbox = plate.getchannel("A").getbbox()
    if not bbox:
        raise ValueError("empty subject plate")
    pivot = ((bbox[0] + bbox[2]) // 2, bbox[3] - 2)
    moved = plate.rotate(
        angle,
        resample=Image.Resampling.BICUBIC,
        center=pivot,
        expand=False,
    )
    out = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    out.alpha_composite(moved, (dx, dy))
    return out


def build(slug: str) -> Image.Image:
    plate = keyed_rgba(first_cell(slug))
    sheet = Image.new("RGB", (CELL * 2, CELL * 2), GREEN)
    for index, (angle, dx, dy) in enumerate(PHASES[slug]):
        frame = transformed(plate, angle, dx, dy)
        panel = Image.new("RGBA", (CELL, CELL), (*GREEN, 255))
        panel.alpha_composite(frame)
        sheet.paste(panel.convert("RGB"), ((index % 2) * CELL, (index // 2) * CELL))
    return sheet


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for slug in PHASES:
        path = OUT / f"{slug}.png"
        build(slug).save(path, optimize=True)
        print(path)


if __name__ == "__main__":
    main()
