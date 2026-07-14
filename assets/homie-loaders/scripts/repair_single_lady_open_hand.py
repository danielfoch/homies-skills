#!/usr/bin/env python3
"""Animate only the ring finger of Single-Ladying's existing open glove.

The accepted production cell-0 character is the immutable plate.  The open
silver hand keeps its thumb, index, middle, pinky, palm, wrist, forearm, body,
and camera fixed.  Only the anatomical ring finger (second from the pinky
side, marked with a gold band) rotates around its knuckle.  Keeping the other
digits open prevents the gesture from reading as a raised middle finger.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter
from scipy import ndimage


ROOT = Path(__file__).resolve().parents[1]
CELL = 627
KEY = (0, 255, 0)
PIVOT = (239, 207)
PHASES = (-28.0, -8.0, 28.0, 8.0)


def isolated_layer(image: Image.Image, mask: Image.Image) -> Image.Image:
    layer = image.convert("RGBA")
    layer.putalpha(mask)
    return layer


def remove_detached_specks(image: Image.Image) -> Image.Image:
    """Keep the single connected character; discard rotation-edge crumbs."""
    rgb = np.asarray(image.convert("RGB"), dtype=np.uint8).copy()
    distance = np.linalg.norm(rgb.astype(np.float32) - np.array(KEY, dtype=np.float32), axis=2)
    labels, count = ndimage.label(distance > 40, structure=np.ones((3, 3), dtype=np.uint8))
    if count <= 1:
        return Image.fromarray(rgb, mode="RGB")
    areas = np.bincount(labels.ravel())
    areas[0] = 0
    keep = labels == int(np.argmax(areas))
    rgb[np.logical_and(labels > 0, ~keep)] = KEY
    return Image.fromarray(rgb, mode="RGB")


def build_frames(cell: Image.Image) -> list[Image.Image]:
    green_rgb = Image.new("RGB", cell.size, KEY)
    subject_mask = ImageChops.difference(cell, green_rgb).convert("L").point(
        lambda value: 255 if value > 4 else 0
    )
    # The raised viewer-left hand is palm-forward with its thumb on viewer-right.
    # Thus the second long finger from viewer-left is the anatomical ring finger.
    finger_mask = Image.new("L", cell.size, 0)
    ImageDraw.Draw(finger_mask).polygon(
        [
            (228, 154), (236, 148), (243, 153), (245, 174),
            (246, 191), (246, 202), (243, 211), (236, 212),
            (231, 203), (230, 180),
        ],
        fill=255,
    )
    # A one-pixel feather retains the source anti-aliasing without exposing a
    # hard chroma notch at the moving finger's knuckle.
    finger_mask = finger_mask.filter(ImageFilter.GaussianBlur(0.3))
    finger_alpha = ImageChops.multiply(finger_mask, subject_mask)
    finger = isolated_layer(cell, finger_alpha)
    # Paint the band directly onto the isolated digit before rotation.  The
    # band therefore remains wrapped around and connected to the finger in
    # every phase instead of becoming a separately positioned overlay.
    finger_draw = ImageDraw.Draw(finger)
    finger_draw.ellipse((233, 179, 243, 188), fill=(112, 75, 15, 255))
    finger_draw.ellipse((234, 180, 242, 187), fill=(238, 177, 29, 255))
    finger.putalpha(finger_alpha)

    plate = cell.copy().convert("RGBA")
    erased_alpha = ImageChops.subtract(Image.new("L", cell.size, 255), finger_alpha)
    green = Image.new("RGBA", cell.size, (*KEY, 255))
    green.alpha_composite(isolated_layer(plate, erased_alpha))
    plate = green

    # Original palm texture around the knuckle is placed last to hide the
    # rotation seam while remaining identical in every phase.
    joint_mask = Image.new("L", cell.size, 0)
    ImageDraw.Draw(joint_mask).ellipse((229, 194, 249, 222), fill=255)
    joint_alpha = ImageChops.multiply(
        joint_mask.filter(ImageFilter.GaussianBlur(0.35)),
        subject_mask,
    )
    joint = isolated_layer(cell, joint_alpha)

    frames: list[Image.Image] = []
    for angle in PHASES:
        moving = finger.rotate(
            angle,
            resample=Image.Resampling.BICUBIC,
            center=PIVOT,
            expand=False,
        )
        frame = plate.copy()
        frame.alpha_composite(moving)
        frame.alpha_composite(joint)

        frames.append(remove_detached_specks(frame))
    return frames


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("/tmp/single-ladying-open-hand-root"))
    args = parser.parse_args()
    output = args.output
    (output / "final").mkdir(parents=True, exist_ok=True)
    (output / "gifs").mkdir(parents=True, exist_ok=True)
    (output / "frames").mkdir(parents=True, exist_ok=True)

    source = Image.open(ROOT / "sources/wildcard/single-ladying-offers.png").convert("RGB")
    cell0 = source.crop((0, 0, CELL, CELL))
    frames = build_frames(cell0)
    sheet = Image.new("RGB", (CELL * 2, CELL * 2), KEY)
    for index, frame in enumerate(frames):
        row, column = divmod(index, 2)
        sheet.paste(frame, (column * CELL, row * CELL))
        frame.save(output / "frames" / f"cell-{index}.png")

    source_out = output / "final/single-ladying-offers.png"
    gif_out = output / "gifs/single-ladying-offers.gif"
    sheet.save(source_out, optimize=True)
    subprocess.run(
        [
            "python3",
            str(ROOT / "scripts/assemble_sprite.py"),
            str(source_out),
            str(gif_out),
            "--size", "256",
            "--no-alignment",
            "--edge-contract",
        ],
        check=True,
    )
    print(source_out)
    print(gif_out)


if __name__ == "__main__":
    main()
