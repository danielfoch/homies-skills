#!/usr/bin/env python3
"""Render raw/aligned GIF pairs as frame strips for visual motion QA."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


BG = (251, 249, 246, 255)
PAPER = (255, 255, 255, 255)
INK = (30, 29, 28, 255)
MUTED = (105, 99, 94, 255)
BORDER = (230, 224, 216, 255)


def font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        Path(
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
            if bold
            else "/System/Library/Fonts/Supplemental/Arial.ttf"
        ),
        Path(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
            if bold
            else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        ),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def frames(path: Path, size: int) -> list[Image.Image]:
    image = Image.open(path)
    output: list[Image.Image] = []
    for index in range(min(4, image.n_frames)):
        image.seek(index)
        rgba = image.convert("RGBA")
        canvas = Image.new("RGBA", (size, size), PAPER)
        rgba.thumbnail((size, size), Image.Resampling.LANCZOS)
        canvas.alpha_composite(
            rgba, ((size - rgba.width) // 2, (size - rgba.height) // 2)
        )
        output.append(canvas)
    return output


def build_group(
    names: list[str],
    raw_dir: Path,
    aligned_dir: Path,
    output: Path,
    size: int,
) -> None:
    margin = 24
    label_w = 210
    row_gap = 8
    card_gap = 18
    card_h = 46 + size * 2 + row_gap
    width = margin * 2 + label_w + size * 4
    height = margin * 2 + card_h * len(names) + card_gap * (len(names) - 1)
    sheet = Image.new("RGBA", (width, height), BG)
    draw = ImageDraw.Draw(sheet)
    title_font = font(18, bold=True)
    small_font = font(12, bold=True)
    y = margin
    for name in names:
        draw.rounded_rectangle(
            (margin, y, width - margin, y + card_h),
            radius=16,
            fill=PAPER,
            outline=BORDER,
            width=1,
        )
        draw.text((margin + 14, y + 13), name, fill=INK, font=title_font)
        raw_y = y + 46
        aligned_y = raw_y + size + row_gap
        draw.text((margin + 14, raw_y + 4), "RAW", fill=MUTED, font=small_font)
        draw.text(
            (margin + 14, aligned_y + 4), "REGISTERED", fill=MUTED, font=small_font
        )
        x0 = margin + label_w
        for index, frame in enumerate(frames(raw_dir / f"{name}.gif", size)):
            sheet.alpha_composite(frame, (x0 + index * size, raw_y))
        for index, frame in enumerate(frames(aligned_dir / f"{name}.gif", size)):
            sheet.alpha_composite(frame, (x0 + index * size, aligned_y))
        y += card_h + card_gap
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.convert("RGB").save(output, quality=94)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("raw_dir", type=Path)
    parser.add_argument("aligned_dir", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--per-sheet", type=int, default=6)
    parser.add_argument("--size", type=int, default=128)
    args = parser.parse_args()
    names = sorted(path.stem for path in args.raw_dir.glob("*.gif"))
    for start in range(0, len(names), args.per_sheet):
        group = names[start : start + args.per_sheet]
        index = start // args.per_sheet + 1
        build_group(
            group,
            args.raw_dir,
            args.aligned_dir,
            args.output_dir / f"motion-qa-{index}.jpg",
            args.size,
        )
    print(f"rendered {len(names)} comparisons across {(len(names) - 1) // args.per_sheet + 1} sheets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
