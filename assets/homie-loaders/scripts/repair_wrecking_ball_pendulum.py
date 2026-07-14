#!/usr/bin/env python3
"""Turn the Wrecking-Ball loader into a true fixed-pivot pendulum.

The accepted illustration already has clean rider/ball/chain continuity, but
the generated cells slide the lower mass beneath a nearly vertical chain.  Use
one intact authored plate and rotate it around the centre of the top chain link
so the ceiling anchor is pixel-fixed and the chain, rider, and ball describe one
coherent swing arc.  The output remains in /tmp until independent QA approves.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage


ROOT = Path(__file__).resolve().parents[1]
OUT = Path("/tmp/pop-dance-redo-c/final/wrecking-ball-riding-research.png")
CELL = 627
GREEN = (0, 255, 0)
PIVOT = (304, 75)
ANGLES = (-12.0, -4.0, 4.0, 12.0)


def keyed_rgba(image: Image.Image) -> Image.Image:
    rgb = np.asarray(image.convert("RGB"), dtype=np.int16)
    green = (
        (rgb[..., 1] > 120)
        & (rgb[..., 1] > rgb[..., 0] * 1.30)
        & (rgb[..., 1] > rgb[..., 2] * 1.30)
        & ((rgb[..., 1] - np.maximum(rgb[..., 0], rgb[..., 2])) > 35)
    )
    rgba = np.dstack([rgb.astype(np.uint8), np.where(green, 0, 255).astype(np.uint8)])
    return Image.fromarray(rgba, "RGBA")


def keep_main_component(image: Image.Image) -> Image.Image:
    """Discard sub-pixel rotation islands while retaining the connected rig."""
    alpha = np.asarray(image.getchannel("A"), dtype=np.uint8)
    labels, count = ndimage.label(alpha > 0)
    sizes = np.bincount(labels.ravel())
    if count < 1 or len(sizes) < 2:
        raise ValueError("rotated pendulum is empty")
    sizes[0] = 0
    keep = labels == int(np.argmax(sizes))
    cleaned = image.copy()
    cleaned.putalpha(Image.fromarray(np.where(keep, alpha, 0).astype(np.uint8), "L"))
    return cleaned


def clean_rgb_panel(image: Image.Image) -> Image.Image:
    """Guarantee one foreground component in the authored chroma master."""
    rgb = np.asarray(image.convert("RGB"), dtype=np.uint8).copy()
    mask = np.any(rgb != np.array(GREEN, dtype=np.uint8), axis=2)
    labels, count = ndimage.label(mask)
    sizes = np.bincount(labels.ravel())
    if count < 1 or len(sizes) < 2:
        raise ValueError("composited pendulum is empty")
    sizes[0] = 0
    keep = labels == int(np.argmax(sizes))
    rgb[~keep] = np.array(GREEN, dtype=np.uint8)
    return Image.fromarray(rgb, "RGB")


def main() -> None:
    source = Image.open(
        ROOT / "sources/wildcard/wrecking-ball-riding-research.png"
    ).convert("RGB")
    if source.size != (CELL * 2, CELL * 2):
        raise ValueError(f"unexpected source size: {source.size}")
    plate = keyed_rgba(source.crop((0, 0, CELL, CELL)))

    sheet = Image.new("RGB", (CELL * 2, CELL * 2), GREEN)
    for index, angle in enumerate(ANGLES):
        frame = keep_main_component(plate.rotate(
            angle,
            resample=Image.Resampling.BICUBIC,
            center=PIVOT,
            expand=False,
            fillcolor=(0, 0, 0, 0),
        ))
        panel = Image.new("RGBA", (CELL, CELL), (*GREEN, 255))
        panel.alpha_composite(frame)
        left = (index % 2) * CELL
        top = (index // 2) * CELL
        sheet.paste(clean_rgb_panel(panel), (left, top))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(OUT, optimize=True)
    print(OUT)


if __name__ == "__main__":
    main()
