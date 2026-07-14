#!/usr/bin/env python3
"""Build Checking the Backstreets from one immutable Marketing Homie plate.

Only the two complete connected arm-hand units rotate around fixed shoulders.
The hat, aviators, face, beard, torso, long shirt, hips, ripped jeans, planted
legs and boots share one exact plate, crop, anchor and palette in every phase.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

from assemble_sprite import extract_alpha
from repair_character_assignment_batch import clean_frame, connected_part
from repair_movie_style_canonical_six import (
    AssetSpec,
    CELL,
    RAW_DIR,
    ROOT,
    SAFE_MARGIN,
    assemble_shared_palette_gif,
    fit_registered_sequence,
    keep_largest_connected_subject,
    mask_union,
    moving_mask,
    nearest_inpaint,
    recompose_source,
    rotate_layer,
    sha256,
)


SLUG = "checking-the-backstreets-marketing"
SPEC = AssetSpec(
    SLUG,
    "checking-the-backstreets-marketing-generated.png",
    "614455b15d080aa0b224d3af3226910a5c24e52ac5454df71372a59593b61e40",
    min_motion_ratio=0.035,
    max_motion_ratio=0.55,
)


def build(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    left_pivot = (439, 327)
    left, left_erase, left_joint, left_mask = connected_part(
        plate,
        (
            (352, 222), (447, 232), (490, 291), (482, 375),
            (422, 424), (342, 414), (278, 374), (209, 337),
            (149, 287), (98, 236), (78, 166), (86, 83),
            (232, 81), (273, 172), (305, 212),
        ),
        left_pivot,
        42,
    )
    right_pivot = (746, 347)
    right, right_erase, right_joint, right_mask = connected_part(
        plate,
        (
            (704, 275), (770, 282), (820, 326), (842, 389),
            (858, 452), (898, 508), (943, 555), (992, 600),
            (1034, 630), (1048, 675), (1031, 718), (1002, 747),
            (967, 728), (946, 682), (913, 632), (876, 592),
            (829, 548), (791, 494), (752, 437), (711, 390),
        ),
        right_pivot,
        42,
    )

    base = nearest_inpaint(
        nearest_inpaint(plate, left_erase, dilate=1),
        right_erase,
        dilate=1,
    )
    phases = ((-8.0, 8.0), (-2.5, 2.5), (2.5, -2.5), (8.0, -8.0))
    frames: list[Image.Image] = []
    allowed = [left_mask, right_mask, left_erase, right_erase]
    for left_angle, right_angle in phases:
        moved_left = rotate_layer(left, left_angle, left_pivot)
        moved_right = rotate_layer(right, right_angle, right_pivot)
        frame = base.copy()
        frame.alpha_composite(moved_left)
        frame.alpha_composite(moved_right)
        frame.alpha_composite(left_joint)
        frame.alpha_composite(right_joint)
        frames.append(clean_frame(frame, 16))
        allowed.extend([moving_mask(moved_left), moving_mask(moved_right)])
    return frames, mask_union(allowed)


def assert_arm_candidate(
    spec: AssetSpec,
    frames: list[Image.Image],
    allowed: Image.Image,
) -> None:
    """Strictly gate the two-arm rig without misreading arm mass as camera drift."""
    hashes = [hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames]
    if len(set(hashes)) != 4:
        raise ValueError(f"{spec.slug}: authored phases are not all unique")
    arrays = [np.asarray(frame, dtype=np.int16) for frame in frames]
    changed = np.zeros((CELL, CELL), dtype=bool)
    for candidate in arrays[1:]:
        changed |= np.any(candidate != arrays[0], axis=2)
    allowed_array = np.asarray(allowed) > 0
    escaped = changed & ~allowed_array
    if escaped.any():
        raise ValueError(f"{spec.slug}: {int(escaped.sum())} pixels changed outside the arm rig")

    union = np.zeros((CELL, CELL), dtype=bool)
    areas: list[int] = []
    centroids: list[tuple[float, float]] = []
    for index, frame in enumerate(frames):
        alpha_u8 = np.asarray(frame.getchannel("A"), dtype=np.uint8)
        alpha = alpha_u8 > 12
        union |= alpha
        areas.append(int(alpha.sum()))
        ys, xs = np.nonzero(alpha)
        bbox = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)
        margin = min(bbox[0], bbox[1], CELL - bbox[2], CELL - bbox[3])
        if margin < SAFE_MARGIN:
            raise ValueError(f"{spec.slug}: frame {index} margin {margin}px below {SAFE_MARGIN}px")
        centroid_y, centroid_x = ndimage.center_of_mass(alpha)
        centroids.append((float(centroid_x), float(centroid_y)))
        for threshold in (1, 8, 16, 32, 48, 64, 96, 128):
            labels, count = ndimage.label(
                alpha_u8 >= threshold,
                structure=np.ones((3, 3), dtype=np.uint8),
            )
            component_areas = np.bincount(labels.ravel())[1:] if count else np.array([])
            significant = component_areas[component_areas >= 32]
            if len(significant) != 1:
                raise ValueError(
                    f"{spec.slug}: frame {index} has {len(significant)} significant "
                    f"components at alpha {threshold}"
                )

    ratio = float(changed.sum() / max(1, union.sum()))
    if not spec.min_motion_ratio <= ratio <= spec.max_motion_ratio:
        raise ValueError(
            f"{spec.slug}: changed-pixel ratio {ratio:.6f} outside "
            f"[{spec.min_motion_ratio}, {spec.max_motion_ratio}]"
        )
    area_span = (max(areas) - min(areas)) / max(areas)
    if area_span > 0.05:
        raise ValueError(f"{spec.slug}: foreground area span {area_span:.4f} exceeds 5%")
    anchor = centroids[0]
    max_shift = max(
        ((x - anchor[0]) ** 2 + (y - anchor[1]) ** 2) ** 0.5
        for x, y in centroids
    )
    # The camera and fixed plate never move; this silhouette-centroid change is
    # caused solely by the deliberately long counter-sweeping arms.
    if max_shift > 6.0:
        raise ValueError(f"{spec.slug}: arm-driven centroid shift {max_shift:.3f}px exceeds 6px")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("/tmp/checking-the-backstreets"))
    parser.add_argument("--promote", action="store_true")
    args = parser.parse_args()

    raw = RAW_DIR / SPEC.raw_name
    actual = sha256(raw)
    if actual != SPEC.raw_sha256:
        raise ValueError(f"unexpected raw hash for {raw}: {actual}")
    plate = clean_frame(keep_largest_connected_subject(extract_alpha(raw)), 16)
    raw_frames, allowed_raw = build(plate)
    frames, allowed = fit_registered_sequence(raw_frames, allowed_raw)
    frames = [clean_frame(frame, 32) for frame in frames]
    assert_arm_candidate(SPEC, frames, allowed)

    source_dir = args.output / "sources/wildcard"
    gif_dir = args.output / "gifs/wildcard"
    frame_dir = args.output / f"frames/{SLUG}"
    source_dir.mkdir(parents=True, exist_ok=True)
    gif_dir.mkdir(parents=True, exist_ok=True)
    frame_dir.mkdir(parents=True, exist_ok=True)

    source_out = source_dir / f"{SLUG}.png"
    gif_out = gif_dir / f"{SLUG}.gif"
    recompose_source(frames).save(source_out, optimize=True)
    assemble_shared_palette_gif(frames, gif_out)
    for index, frame in enumerate(frames):
        frame.save(frame_dir / f"cell-{index}.png", optimize=True)
    allowed.save(frame_dir / "allowed-motion-mask.png", optimize=True)

    if args.promote:
        shutil.copy2(source_out, ROOT / f"sources/wildcard/{SLUG}.png")
        shutil.copy2(gif_out, ROOT / f"gifs/wildcard/{SLUG}.gif")
    print(f"{SLUG}: source={sha256(source_out)} gif={sha256(gif_out)}")


if __name__ == "__main__":
    main()
