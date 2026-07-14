#!/usr/bin/env python3
"""Build the accepted full-body Thriller claw-step from its generated raw.

The raw sheet already contains the four authored dance poses.  This script
performs only deterministic release work: chroma extraction, debris removal,
integer registration to one foot baseline / jacket centre, exact-green source
recomposition, and canonical six-frame GIF assembly.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

from assemble_sprite import extract_alpha


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "qa/strict-repairs/raw/thrillering-marketing-full-body-generated.png"
EXPECTED_RAW_SHA256 = "12b552c52bf0f708db21a9b9db5e6bfe5a17d5dc208e31ff7f1450d05da70978"
CELL = 627
KEY = (0, 255, 0)

# The generated keyframes contain the intended articulated movement, but their
# whole plates were not registered.  These integer translations put every shoe
# on y=560 and keep the red jacket centroid near x=315.  The remaining motion is
# the authored crouch, weight transfer, arm sweep, and limp-wrist claw action.
TRANSLATIONS = ((-45, 2), (16, -1), (48, 44), (59, 44))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def keep_connected_character(cell: Image.Image) -> Image.Image:
    """Remove disconnected image-generation crumbs while retaining soft edges."""
    rgba = np.asarray(cell.convert("RGBA"), dtype=np.uint8).copy()
    visible = rgba[:, :, 3] > 12
    labels, count = ndimage.label(visible, structure=np.ones((3, 3), dtype=np.uint8))
    if count == 0:
        raise ValueError("chroma extraction removed the character")
    areas = np.bincount(labels.ravel())
    areas[0] = 0
    keep = labels == int(np.argmax(areas))
    rgba[~keep, 3] = 0
    return Image.fromarray(rgba, mode="RGBA")


def translate(cell: Image.Image, dx: int, dy: int) -> Image.Image:
    canvas = Image.new("RGBA", cell.size, (0, 0, 0, 0))
    canvas.alpha_composite(cell, (dx, dy))
    return canvas


def recompose_source(raw: Path) -> tuple[Image.Image, list[Image.Image]]:
    if sha256(raw) != EXPECTED_RAW_SHA256:
        raise ValueError(f"unexpected raw hash for {raw}")
    alpha = extract_alpha(raw)
    if alpha.size != (CELL * 2, CELL * 2):
        raise ValueError(f"expected 1254x1254 raw, found {alpha.size}")

    frames: list[Image.Image] = []
    for index, (dx, dy) in enumerate(TRANSLATIONS):
        row, column = divmod(index, 2)
        cell = alpha.crop(
            (column * CELL, row * CELL, (column + 1) * CELL, (row + 1) * CELL)
        )
        cell = translate(keep_connected_character(cell), dx, dy)
        bbox = cell.getchannel("A").getbbox()
        if bbox is None:
            raise ValueError(f"frame {index} is empty")
        left, top, right, bottom = bbox
        margin = min(left, top, CELL - right, CELL - bottom)
        if margin < 60:
            raise ValueError(f"frame {index} margin {margin}px is below 60px: {bbox}")
        frames.append(cell)

    source = Image.new("RGB", (CELL * 2, CELL * 2), KEY)
    for index, frame in enumerate(frames):
        row, column = divmod(index, 2)
        green = Image.new("RGB", (CELL, CELL), KEY)
        green.paste(frame.convert("RGB"), (0, 0), frame.getchannel("A"))
        source.paste(green, (column * CELL, row * CELL))
    return source, frames


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("/tmp/thrillering-marketing-claw"),
        help="candidate/evidence directory",
    )
    parser.add_argument(
        "--promote",
        action="store_true",
        help="replace the production source and GIF after candidate QA",
    )
    args = parser.parse_args()

    source, frames = recompose_source(RAW)
    final_dir = args.output / "sources/wildcard"
    gif_dir = args.output / "gifs/wildcard"
    frame_dir = args.output / "frames"
    final_dir.mkdir(parents=True, exist_ok=True)
    gif_dir.mkdir(parents=True, exist_ok=True)
    frame_dir.mkdir(parents=True, exist_ok=True)

    source_out = final_dir / "thrillering-marketing.png"
    gif_out = gif_dir / "thrillering-marketing.gif"
    source.save(source_out, optimize=True)
    for index, frame in enumerate(frames):
        frame.save(frame_dir / f"cell-{index}.png", optimize=True)

    subprocess.run(
        [
            "python3",
            str(ROOT / "scripts/assemble_sprite.py"),
            str(source_out),
            str(gif_out),
            "--size",
            "256",
            "--colors",
            "96",
            "--no-alignment",
        ],
        check=True,
    )

    if args.promote:
        shutil.copy2(source_out, ROOT / "sources/wildcard/thrillering-marketing.png")
        shutil.copy2(gif_out, ROOT / "gifs/wildcard/thrillering-marketing.gif")

    print(f"source={source_out} sha256={sha256(source_out)}")
    print(f"gif={gif_out} sha256={sha256(gif_out)}")


if __name__ == "__main__":
    main()
