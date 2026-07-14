#!/usr/bin/env python3
"""Build the candidate-only Scooby-Dooing Manager loader.

The accepted Manager-and-dog alpha plate is fitted exactly once.  Every phase
is a whole-rig integer translation of those immutable pixels, producing a
controlled shared shake without AI redraw, scaling, anatomy drift, or crop.
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
SLUG = "scooby-dooing-manager"
RAW = ROOT / "qa/strict-repairs/raw/scooby-dooing-manager-alpha.png"
CHROMA = ROOT / f"qa/strict-repairs/{SLUG}/candidates/raw/{SLUG}-chroma.png"
OUTPUT = ROOT / f"qa/strict-repairs/{SLUG}/candidates"
RAW_SHA256 = "c29f3a2e02ca6f01405df62535cc3d41f8503d28bf10aaeb386b585c74555d55"
CHROMA_SHA256 = "f1974fd98e5240af0a8527bbf3548209885fc304a4884dbf65325115dfdfb2dc"
RAW_SIZE = (1010, 1558)
SAFE_MARGIN = 60
MAX_FITTED_HEIGHT = 480
OFFSETS = ((-9, 0), (-3, -2), (3, 2), (9, 0))


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


def translate_plate(plate: Image.Image, offset: tuple[int, int]) -> Image.Image:
    frame = Image.new("RGBA", (CELL, CELL), (0, 0, 0, 0))
    frame.alpha_composite(plate, offset)
    return frame


def assert_candidate(frames: list[Image.Image]) -> dict[str, object]:
    pixel_hashes = [hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames]
    if len(set(pixel_hashes)) != 4:
        raise ValueError("four authored shake phases are not byte-distinct")

    masks: list[np.ndarray] = []
    areas: list[int] = []
    bboxes: list[list[int]] = []
    centroids: list[list[float]] = []
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
        centroid_y, centroid_x = ndimage.center_of_mass(alpha)
        masks.append(alpha)
        areas.append(int(alpha.sum()))
        bboxes.append(bbox)
        centroids.append([float(centroid_x), float(centroid_y)])

    if len(set(areas)) != 1:
        raise ValueError(f"integer shake changed immutable foreground area: {areas}")
    widths = [bbox[2] - bbox[0] for bbox in bboxes]
    heights = [bbox[3] - bbox[1] for bbox in bboxes]
    if len(set(widths)) != 1 or len(set(heights)) != 1:
        raise ValueError("integer shake changed immutable bbox dimensions")

    for index, ((expected_x, expected_y), centroid) in enumerate(zip(OFFSETS, centroids)):
        observed_x = centroid[0] - centroids[0][0]
        observed_y = centroid[1] - centroids[0][1]
        wanted_x = expected_x - OFFSETS[0][0]
        wanted_y = expected_y - OFFSETS[0][1]
        if abs(observed_x - wanted_x) > 0.01 or abs(observed_y - wanted_y) > 0.01:
            raise ValueError(f"phase {index} is not the declared whole-rig translation")

    changed = np.zeros((CELL, CELL), dtype=bool)
    base = np.asarray(frames[0])
    for frame in frames[1:]:
        changed |= np.any(np.asarray(frame) != base, axis=2)
    subject_union = np.logical_or.reduce(masks)
    motion_ratio = float(changed.sum() / subject_union.sum())
    # A translated textured watercolour plate changes essentially every
    # occupied RGBA pixel even though the silhouette displacement is small.
    if not 0.90 <= motion_ratio <= 1.10:
        raise ValueError(f"shared shake motion ratio {motion_ratio:.5f} outside contract")
    return {
        "frame_pixel_hashes": pixel_hashes,
        "foreground_areas": areas,
        "bboxes": bboxes,
        "centroids": centroids,
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
    frames = [translate_plate(plate, offset) for offset in OFFSETS]
    metrics = assert_candidate(frames)

    source_out = source_dir / f"{SLUG}.png"
    gif_out = gif_dir / f"{SLUG}.gif"
    plate_out = frame_dir / "locked-manager-and-dog.png"
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
        "motion": {"kind": "whole-rig integer shared shake", "offsets_px": OFFSETS},
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
