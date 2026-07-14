#!/usr/bin/env python3
"""Deterministic continuity repairs for the five rejected release sprites.

The input art remains image-generated. This script only freezes stationary
plates, removes two known generation artifacts, and applies rigid transforms to
already accepted connected limbs/characters. It is intentionally deterministic
so the repaired loops cannot re-introduce frame-to-frame redraw wiggle.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage


ROOT = Path(__file__).resolve().parents[1]
TMP = Path("/tmp/rejected-three-repair")
CELL = 627
SHEET = CELL * 2
GREEN = (0, 255, 0)


def cell(sheet: Image.Image, index: int) -> Image.Image:
    x = (index % 2) * CELL
    y = (index // 2) * CELL
    return sheet.crop((x, y, x + CELL, y + CELL)).convert("RGBA")


def sheet_from_cells(frames: list[Image.Image]) -> Image.Image:
    out = Image.new("RGBA", (SHEET, SHEET), (*GREEN, 255))
    for index, frame in enumerate(frames):
        x = (index % 2) * CELL
        y = (index // 2) * CELL
        out.alpha_composite(frame, (x, y))
    return out.convert("RGB")


def polygon_layer(source: Image.Image, points: list[tuple[int, int]]) -> tuple[Image.Image, Image.Image]:
    polygon = Image.new("L", source.size, 0)
    ImageDraw.Draw(polygon).polygon(points, fill=255)
    alpha = source.getchannel("A")
    mask = Image.fromarray(np.minimum(np.asarray(polygon), np.asarray(alpha)).astype(np.uint8), "L")
    layer = Image.new("RGBA", source.size, (0, 0, 0, 0))
    layer.paste(source, (0, 0), mask)
    base = source.copy()
    base.putalpha(Image.fromarray(np.where(np.asarray(mask) > 0, 0, np.asarray(alpha)).astype(np.uint8), "L"))
    return base, layer


def chroma_rgba(source: Image.Image) -> Image.Image:
    rgb = np.asarray(source.convert("RGB"))
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    keyed = (g > 185) & (g > r * 1.35) & (g > b * 1.35)
    rgba = np.dstack([rgb, np.where(keyed, 0, 255).astype(np.uint8)])
    return Image.fromarray(rgba, "RGBA")


def largest_component_layer(source: Image.Image) -> tuple[Image.Image, Image.Image]:
    alpha = np.asarray(source.getchannel("A")) > 0
    labels, count = ndimage.label(alpha)
    if count < 1:
        raise ValueError("no foreground component")
    sizes = ndimage.sum(alpha, labels, range(1, count + 1))
    largest = int(np.argmax(sizes)) + 1
    body_mask = labels == largest
    body = Image.new("RGBA", source.size, (0, 0, 0, 0))
    body.putalpha(Image.fromarray((body_mask * 255).astype(np.uint8), "L"))
    body.paste(source, (0, 0), body.getchannel("A"))
    accents = Image.new("RGBA", source.size, (0, 0, 0, 0))
    accent_mask = alpha & ~body_mask
    accents.putalpha(Image.fromarray((accent_mask * 255).astype(np.uint8), "L"))
    accents.paste(source, (0, 0), accents.getchannel("A"))
    return body, accents


def component_layers(source: Image.Image) -> list[tuple[int, Image.Image]]:
    """Return connected foreground components, largest first.

    The rejected Diamond sheet already contains intact, proportionally correct
    bodies and arms.  Splitting the transparent source into components lets us
    retain those exact figures while replacing only the generated rubble.
    """
    alpha = np.asarray(source.getchannel("A")) > 0
    labels, count = ndimage.label(alpha)
    layers: list[tuple[int, Image.Image]] = []
    for label in range(1, count + 1):
        mask = labels == label
        size = int(mask.sum())
        if not size:
            continue
        layer = Image.new("RGBA", source.size, (0, 0, 0, 0))
        layer_mask = Image.fromarray((mask * 255).astype(np.uint8), "L")
        layer.paste(source, (0, 0), layer_mask)
        layers.append((size, layer))
    return sorted(layers, key=lambda item: item[0], reverse=True)


def shifted(source: Image.Image, dx: int, dy: int) -> Image.Image:
    out = Image.new("RGBA", source.size, (0, 0, 0, 0))
    out.alpha_composite(source, (dx, dy))
    return out


def scale_canvas(source: Image.Image, scale: float) -> Image.Image:
    """Scale one complete authored plate without changing its internal layout."""
    size = round(CELL * scale)
    resized = source.resize((size, size), Image.Resampling.LANCZOS)
    out = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    offset = ((CELL - size) // 2, (CELL - size) // 2)
    out.alpha_composite(resized, offset)
    return out


def repair_diamond() -> Image.Image:
    raw = Image.open(TMP / "alpha/diamonding-in-rough-crm.png").convert("RGBA")
    # Use the three intact "diamond out" poses, then reverse through the middle
    # pose for a clean loop.  The generated bodies/arms are kept whole; only the
    # independently redrawn rubble is discarded.  Frame 1 supplies one frozen
    # rubble plate (including all of its tiny loose stones) for every frame.
    source_indices = (1, 2, 3, 3)
    frozen_components = component_layers(cell(raw, 1))
    frozen_rubble = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    for _, layer in frozen_components[1:]:
        frozen_rubble.alpha_composite(layer)

    # Align the head/torso anchor while the intact right arm raises the diamond.
    shifts = {1: (0, 0), 2: (-5, 29), 3: (5, 29)}
    frames: list[Image.Image] = []
    for phase, index in enumerate(source_indices):
        body = component_layers(cell(raw, index))[0][1]
        dx, dy = shifts[index]
        frame = frozen_rubble.copy()
        frame.alpha_composite(shifted(body, dx, dy))
        if phase == 3:
            # A final, unmistakable diamond glint creates the fourth unique
            # high pose before the reversible loop descends through phases 2/1.
            pixels = np.asarray(frame)
            blue = (
                (pixels[..., 2] > 145)
                & (pixels[..., 2] > pixels[..., 0] * 1.12)
                & (pixels[..., 2] > pixels[..., 1] * 1.02)
                & (np.indices(pixels.shape[:2])[1] > 300)
                & (np.indices(pixels.shape[:2])[0] < 300)
            )
            ys, xs = np.where(blue)
            sparkle_x = int(xs.max()) + 8
            sparkle_y = int(ys.min()) - 6
            draw = ImageDraw.Draw(frame)
            white = (255, 255, 255, 255)
            draw.line((sparkle_x - 10, sparkle_y, sparkle_x + 10, sparkle_y), fill=white, width=4)
            draw.line((sparkle_x, sparkle_y - 10, sparkle_x, sparkle_y + 10), fill=white, width=4)
        frames.append(scale_canvas(frame, 0.86))
    return sheet_from_cells(frames)


def spider_masked_plate() -> Image.Image:
    raw = Image.open(TMP / "alpha/spider-manning-crm.png").convert("RGBA")
    plate = cell(raw, 0)
    draw = ImageDraw.Draw(plate)
    red = (202, 42, 45, 255)
    dark = (45, 28, 35, 255)
    # Full mask: no exposed skin, hair, nose, or mouth.
    draw.ellipse((318, 20, 384, 106), fill=red, outline=dark, width=3)
    draw.ellipse((329, 45, 349, 76), fill=(245, 248, 244, 255), outline=dark, width=3)
    draw.ellipse((355, 45, 375, 76), fill=(245, 248, 244, 255), outline=dark, width=3)
    # Simple web cues that remain legible after 128px reduction.
    draw.line((351, 25, 351, 101), fill=dark, width=2)
    draw.arc((325, 34, 378, 83), 20, 160, fill=dark, width=2)
    draw.arc((325, 55, 378, 101), 20, 160, fill=dark, width=2)
    draw.line((351, 106, 351, 250), fill=dark, width=2)
    for y in (135, 170, 205):
        draw.arc((298, y - 20, 404, y + 25), 20, 160, fill=dark, width=2)
    return plate


def repair_spider() -> Image.Image:
    plate = spider_masked_plate()
    inverted = plate.rotate(180, resample=Image.Resampling.BICUBIC,
                            center=(CELL // 2, CELL // 2), expand=False)
    pivot = (CELL // 2, 53)
    frames: list[Image.Image] = []
    for angle in (-7, -2, 3, 7):
        frame = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
        pendulum = inverted.rotate(angle, resample=Image.Resampling.BICUBIC,
                                   center=pivot, expand=False)
        alpha = np.asarray(pendulum.getchannel("A"))
        ys, xs = np.where(alpha > 32)
        top = int(ys.min())
        ankle_band = xs[ys <= top + 16]
        ankle_x = int(np.median(ankle_band))
        # One clean web, drawn behind and eight pixels into the boot silhouette
        # so it always connects after the pendulum rotation. No loose fork.
        ImageDraw.Draw(frame).line(
            (CELL // 2, 0, ankle_x, top + 8),
            # Medium blue-grey remains visible on both the chroma master and
            # Homies' warm off-white chat background after 128px reduction.
            fill=(92, 107, 122, 255), width=5,
        )
        frame.alpha_composite(pendulum)
        frames.append(scale_canvas(frame, 0.80))
    return sheet_from_cells(frames)


def repair_shrek() -> Image.Image:
    raw = Image.open(TMP / "alpha/shreking-manager.png").convert("RGBA")
    # All four generated poses have two natural, connected ears. Keep every
    # character intact and align alternating frames instead of cutting ears out
    # of the head—a previous mask accidentally removed face pixels.
    frames: list[Image.Image] = []
    for index in range(4):
        intact = cell(raw, index)
        aligned = shifted(intact, 26 if index in (1, 3) else 0, 0)
        frames.append(scale_canvas(aligned, 0.84))
    return sheet_from_cells(frames)


def repair_neo() -> Image.Image:
    source = Image.open(ROOT / "sources/wildcard/neo-ing-offers.png").convert("RGB")
    originals = [cell(source, i) for i in range(4)]
    intact = chroma_rgba(originals[2])
    body, bullets = largest_component_layer(intact)
    deeper = body.rotate(9, resample=Image.Resampling.BICUBIC,
                         center=(326, 340), expand=False)
    deeper = shifted(deeper, 24, 0)
    repaired = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    repaired.alpha_composite(bullets)
    repaired.alpha_composite(deeper)
    return sheet_from_cells([chroma_rgba(frame.convert("RGB")) for frame in originals[:3]] + [repaired])


def repair_yoda() -> Image.Image:
    source = Image.open(ROOT / "sources/wildcard/yoda-ing-cma.png").convert("RGB")
    frames = [cell(source, i).convert("RGB") for i in range(4)]
    # Cell 1 contains one detached green/black crescent at this measured bbox.
    ImageDraw.Draw(frames[1]).rectangle((194, 410, 226, 442), fill=GREEN)
    # Preserve the RGB frames verbatim. Chroma keying is forbidden here because
    # Yoda's face and hands are intentionally the same hue family as the key.
    out = Image.new("RGB", (SHEET, SHEET), GREEN)
    for index, frame in enumerate(frames):
        out.paste(frame, ((index % 2) * CELL, (index // 2) * CELL))
    return out


def main() -> None:
    out = TMP / "final"
    out.mkdir(parents=True, exist_ok=True)
    repairs = {
        "diamonding-in-rough-crm": repair_diamond(),
        "spider-manning-crm": repair_spider(),
        "shreking-manager": repair_shrek(),
        "neo-ing-offers": repair_neo(),
        "yoda-ing-cma": repair_yoda(),
    }
    for slug, image in repairs.items():
        path = out / f"{slug}.png"
        image.save(path, optimize=True)
        print(path)


if __name__ == "__main__":
    main()
