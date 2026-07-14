#!/usr/bin/env python3
"""Build the candidate-only Buffying Offers loader.

The accepted female Offers-and-single-stake alpha plate is fitted once.  The
four phases are deterministic rotations of that rigid plate around the boot
anchor, creating a guarded hunter lean with no redraw, scaling, or prop drift.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image
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
SLUG = "buffying-offers"
RAW = ROOT / "qa/strict-repairs/raw/buffying-offers-alpha.png"
CHROMA = ROOT / f"qa/strict-repairs/{SLUG}/candidates/raw/{SLUG}-chroma.png"
OUTPUT = ROOT / f"qa/strict-repairs/{SLUG}/candidates"
RAW_SHA256 = "e16759f730bced67498091968b19d339409f0ca1a50dab254bc9548057e81f29"
CHROMA_SHA256 = "694169c8e047fef7b8f9aacd3018bd5026317d865d93e580882eef3f40ca51e5"
RAW_SIZE = (1024, 1536)
SAFE_MARGIN = 60
MAX_FITTED_HEIGHT = 480
ANGLES_DEG = (2.8, 0.9, -0.9, -2.8)


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


def rotate_plate(plate: Image.Image, angle: float, pivot: tuple[int, int]) -> Image.Image:
    frame = plate.rotate(
        angle,
        resample=Image.Resampling.BICUBIC,
        center=pivot,
        expand=False,
        fillcolor=(0, 0, 0, 0),
    )
    return zero_low_alpha_fringe(drop_tiny_alpha_islands(frame, minimum_area=24))


def assert_candidate(frames: list[Image.Image]) -> dict[str, object]:
    pixel_hashes = [hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames]
    if len(set(pixel_hashes)) != 4:
        raise ValueError("four authored guarded-lean phases are not byte-distinct")
    masks: list[np.ndarray] = []
    areas: list[int] = []
    bboxes: list[list[int]] = []
    for index, frame in enumerate(frames):
        alpha = np.asarray(frame.getchannel("A")) > 12
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
    if area_span > 0.01:
        raise ValueError(f"rigid rotation area span {area_span:.5f} exceeds 1%")
    changed = np.zeros((CELL, CELL), dtype=bool)
    base = np.asarray(frames[0])
    for frame in frames[1:]:
        changed |= np.any(np.asarray(frame) != base, axis=2)
    subject_union = np.logical_or.reduce(masks)
    motion_ratio = float(changed.sum() / subject_union.sum())
    # A rotated textured watercolour plate changes essentially every occupied
    # RGBA pixel while remaining one immutable rigid subject.
    if not 0.90 <= motion_ratio <= 1.10:
        raise ValueError(f"guarded hunter-lean ratio {motion_ratio:.5f} outside contract")
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
    plate_bbox = plate.getchannel("A").point(lambda value: 255 if value > 12 else 0).getbbox()
    if plate_bbox is None:
        raise ValueError("fitted plate is empty")
    pivot = (CELL // 2, plate_bbox[3] - 2)
    frames = [rotate_plate(plate, angle, pivot) for angle in ANGLES_DEG]
    metrics = assert_candidate(frames)

    source_out = source_dir / f"{SLUG}.png"
    gif_out = gif_dir / f"{SLUG}.gif"
    plate_out = frame_dir / "locked-female-offers-and-single-stake.png"
    recompose_source(frames).save(source_out, optimize=True)
    assemble_shared_palette_gif(frames, gif_out)
    plate.save(plate_out, optimize=True)
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
        "motion": {
            "kind": "rigid boot-anchored guarded hunter lean",
            "angles_deg": ANGLES_DEG,
            "pivot_px": pivot,
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
