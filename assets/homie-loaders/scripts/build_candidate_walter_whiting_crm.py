#!/usr/bin/env python3
"""Build the candidate-only Walter-Whiting CRM loader.

The corrected canonical dark-skinned CRM/hazmat/respirator/briefcase plate is
fitted once and then reused byte-for-byte in all four phases.  Only a tiny
glasses glint and respirator-filter highlight change inside explicit local
masks; the body, face, hands, suit, briefcase, crop, scale, and anchor are
fully pixel-locked.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw
from scipy import ndimage

from repair_movie_style_canonical_six import (
    CELL,
    DURATIONS_MS,
    SEQUENCE,
    assemble_shared_palette_gif,
    drop_tiny_alpha_islands,
    recompose_source,
    zero_low_alpha_fringe,
)


ROOT = Path(__file__).resolve().parents[1]
SLUG = "walter-whiting-crm"
RAW = ROOT / "qa/strict-repairs/raw/walter-whiting-crm-alpha.png"
CHROMA = ROOT / f"qa/strict-repairs/{SLUG}/candidates/raw/{SLUG}-chroma.png"
OUTPUT = ROOT / f"qa/strict-repairs/{SLUG}/candidates"
RAW_SHA256 = "994483ad6390e70ac43a862a9213a5d5b24ead56aa2b3e3bf643c900003e3230"
CHROMA_SHA256 = "0acddc575a1789fba5cdc629bdcf117762676da416a440731e26c88ffddb4836"
RAW_SIZE = (1189, 1323)
SAFE_MARGIN = 60
MAX_FITTED_HEIGHT = 480
GLASSES_GLINT_X = (299, 309, 320, 331)
FILTER_RADII = (2, 3, 5, 3)
GLASSES_BOX = (292, 94, 352, 123)
RESPIRATOR_BOX = (292, 145, 354, 192)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fit_immutable_plate() -> Image.Image:
    if sha256(RAW) != RAW_SHA256:
        raise ValueError(f"unexpected immutable alpha hash: {RAW}")
    if sha256(CHROMA) != CHROMA_SHA256:
        raise ValueError(f"unexpected accepted chroma hash: {CHROMA}")
    raw = Image.open(RAW).convert("RGBA")
    if raw.size != RAW_SIZE:
        raise ValueError(f"unexpected immutable alpha size: {raw.size}")
    alpha = raw.getchannel("A").point(lambda value: 255 if value > 12 else 0)
    bbox = alpha.getbbox()
    if bbox is None:
        raise ValueError("immutable plate is empty")
    padding = 4
    crop = (
        max(0, bbox[0] - padding),
        max(0, bbox[1] - padding),
        min(raw.width, bbox[2] + padding),
        min(raw.height, bbox[3] + padding),
    )
    trimmed = raw.crop(crop)
    scale = MAX_FITTED_HEIGHT / trimmed.height
    fitted = trimmed.resize(
        (round(trimmed.width * scale), MAX_FITTED_HEIGHT),
        Image.Resampling.LANCZOS,
    )
    plate = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    plate.alpha_composite(fitted, ((CELL - fitted.width) // 2, (CELL - fitted.height) // 2))
    return zero_low_alpha_fringe(drop_tiny_alpha_islands(plate, minimum_area=24))


def local_allowed_mask(static_alpha: Image.Image) -> Image.Image:
    mask = Image.new("L", (CELL, CELL), 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle(GLASSES_BOX, fill=255)
    draw.rectangle(RESPIRATOR_BOX, fill=255)
    return ImageChops.multiply(mask, static_alpha)


def draw_local_highlights(phase: int, static_alpha: Image.Image) -> Image.Image:
    """Draw one glasses/filter phase, clipped to the fixed subject alpha."""
    scale = 4
    layer = Image.new("RGBA", (CELL * scale, CELL * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)

    x = GLASSES_GLINT_X[phase] * scale
    y = 106 * scale
    draw.line(
        (x - 4 * scale, y + 5 * scale, x + 4 * scale, y - 5 * scale),
        fill=(255, 255, 248, 235),
        width=2 * scale,
    )
    draw.line(
        (x - 1 * scale, y + 5 * scale, x + 5 * scale, y - 1 * scale),
        fill=(210, 228, 232, 180),
        width=1 * scale,
    )

    radius = FILTER_RADII[phase] * scale
    filter_color = (
        (190, 205, 210, 150),
        (220, 232, 234, 190),
        (255, 255, 246, 235),
        (218, 230, 232, 185),
    )[phase]
    for cx in (307, 341):
        cy = 166
        draw.ellipse(
            (
                cx * scale - radius,
                cy * scale - radius,
                cx * scale + radius,
                cy * scale + radius,
            ),
            outline=filter_color,
            width=2 * scale,
        )

    highlight = layer.resize((CELL, CELL), Image.Resampling.LANCZOS)
    allowed = local_allowed_mask(static_alpha)
    highlight.putalpha(
        ImageChops.multiply(highlight.getchannel("A"), allowed)
    )
    return highlight


def build_frames(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    static_alpha = plate.getchannel("A")
    frames: list[Image.Image] = []
    allowed = local_allowed_mask(static_alpha)
    for phase in range(4):
        frame = plate.copy()
        frame.alpha_composite(draw_local_highlights(phase, static_alpha))
        # Highlights alter colour only; lock the silhouette byte-for-byte.
        frame.putalpha(static_alpha)
        frames.append(frame)
    return frames, allowed


def assert_candidate(
    frames: list[Image.Image], plate: Image.Image, allowed: Image.Image
) -> dict[str, object]:
    pixel_hashes = [hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames]
    if len(set(pixel_hashes)) != 4:
        raise ValueError("four authored brooding phases are not byte-distinct")
    plate_rgba = np.asarray(plate)
    plate_alpha = np.asarray(plate.getchannel("A"))
    allowed_array = np.asarray(allowed) > 0
    masks: list[np.ndarray] = []
    areas: list[int] = []
    bboxes: list[list[int]] = []
    for index, frame in enumerate(frames):
        frame_rgba = np.asarray(frame)
        frame_alpha = np.asarray(frame.getchannel("A"))
        if not np.array_equal(frame_alpha, plate_alpha):
            raise ValueError(f"phase {index} changed the locked subject silhouette")
        if not np.array_equal(frame_rgba[~allowed_array], plate_rgba[~allowed_array]):
            raise ValueError(f"phase {index} changed pixels outside local highlight masks")
        alpha = frame_alpha > 12
        labels, count = ndimage.label(alpha, structure=np.ones((3, 3), dtype=np.uint8))
        if count != 1:
            raise ValueError(f"phase {index} has {count} foreground components")
        ys, xs = np.nonzero(alpha)
        bbox = [int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1]
        margin = min(bbox[0], bbox[1], CELL - bbox[2], CELL - bbox[3])
        if margin < SAFE_MARGIN:
            raise ValueError(f"phase {index} margin {margin}px below {SAFE_MARGIN}px")
        masks.append(alpha)
        areas.append(int(alpha.sum()))
        bboxes.append(bbox)
    area_span = (max(areas) - min(areas)) / max(areas)
    if area_span != 0.0:
        raise ValueError("local highlights changed locked foreground area")
    changed = np.zeros((CELL, CELL), dtype=bool)
    base = np.asarray(frames[0])
    for frame in frames[1:]:
        changed |= np.any(np.asarray(frame) != base, axis=2)
    if np.any(changed & ~allowed_array):
        raise ValueError("authored motion escaped glasses/respirator masks")
    subject_union = np.logical_or.reduce(masks)
    motion_ratio = float(changed.sum() / subject_union.sum())
    if not 0.0002 <= motion_ratio <= 0.03:
        raise ValueError(f"local highlight ratio {motion_ratio:.6f} outside contract")
    return {
        "frame_pixel_hashes": pixel_hashes,
        "foreground_areas": areas,
        "foreground_area_span": area_span,
        "bboxes": bboxes,
        "motion_ratio": motion_ratio,
    }


def main() -> None:
    source_dir = OUTPUT / "sources/wildcard"
    gif_dir = OUTPUT / "gifs/wildcard"
    frame_dir = OUTPUT / "frames" / SLUG
    source_dir.mkdir(parents=True, exist_ok=True)
    gif_dir.mkdir(parents=True, exist_ok=True)
    frame_dir.mkdir(parents=True, exist_ok=True)

    plate = fit_immutable_plate()
    frames, allowed = build_frames(plate)
    metrics = assert_candidate(frames, plate, allowed)

    source_out = source_dir / f"{SLUG}.png"
    gif_out = gif_dir / f"{SLUG}.gif"
    plate_out = frame_dir / "locked-crm-hazmat-respirator-and-briefcase.png"
    allowed_out = frame_dir / "allowed-glasses-and-respirator-highlight-mask.png"
    recompose_source(frames).save(source_out, optimize=True)
    assemble_shared_palette_gif(frames, gif_out)
    plate.save(plate_out, optimize=True)
    allowed.save(allowed_out, optimize=True)
    frame_paths: list[Path] = []
    for index, frame in enumerate(frames):
        path = frame_dir / f"cell-{index}.png"
        frame.save(path, optimize=True)
        frame_paths.append(path)

    evidence = {
        "slug": SLUG,
        "builder": str(Path(__file__)),
        "builder_sha256": sha256(Path(__file__)),
        "immutable_alpha": {"path": str(RAW), "sha256": sha256(RAW), "size": list(RAW_SIZE)},
        "accepted_chroma": {"path": str(CHROMA), "sha256": sha256(CHROMA)},
        "locked_plate": {"path": str(plate_out), "sha256": sha256(plate_out)},
        "allowed_local_highlight_mask": {
            "path": str(allowed_out),
            "sha256": sha256(allowed_out),
            "glasses_box": GLASSES_BOX,
            "respirator_box": RESPIRATOR_BOX,
        },
        "motion": {
            "kind": "static locked plate with local glasses glint and respirator-filter pulse",
            "glasses_glint_x_px": GLASSES_GLINT_X,
            "filter_radii_px": FILTER_RADII,
        },
        "authored_cells": [
            {"path": str(path), "sha256": sha256(path)} for path in frame_paths
        ],
        "source": {"path": str(source_out), "sha256": sha256(source_out)},
        "gif": {
            "path": str(gif_out),
            "sha256": sha256(gif_out),
            "sequence": SEQUENCE,
            "durations_ms": DURATIONS_MS,
        },
        "assertions": metrics,
    }
    evidence_out = OUTPUT / "builder-evidence.json"
    evidence_out.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(f"{SLUG}: source={sha256(source_out)} gif={sha256(gif_out)}")
    print(evidence_out)


if __name__ == "__main__":
    main()
