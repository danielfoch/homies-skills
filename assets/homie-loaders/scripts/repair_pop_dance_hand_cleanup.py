#!/usr/bin/env python3
"""Rebuild four Pop & Dance loaders from one SHA-locked plate each.

The previous masters mixed independently redrawn characters, duplicate hands,
and per-frame rescaling.  Each repair below extracts exactly one generated
canonical Homie, freezes the face/torso/legs, and moves only a connected arm
rig.  All four authored phases share one crop, scale, bottom anchor, and GIF
palette.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops
from scipy import ndimage

from assemble_sprite import extract_alpha
from repair_character_assignment_batch import connected_part
from repair_movie_style_canonical_six import (
    AssetSpec,
    RAW_DIR,
    ROOT,
    assemble_shared_palette_gif,
    assert_candidate,
    drop_tiny_alpha_islands,
    fit_registered_sequence,
    keep_largest_connected_subject,
    mask_layer,
    mask_union,
    moving_mask,
    nearest_inpaint,
    polygon_mask,
    recompose_source,
    remove_visible_satellite_components,
    rotate_layer,
    sha256,
    zero_low_alpha_fringe,
)


SPECS = {
    "disco-inferno-ing-reports": AssetSpec(
        "disco-inferno-ing-reports",
        "disco-inferno-ing-reports-locked-v2.png",
        "8353893af86c673950d7efec54a03138daf542eb7a6e2f00d8732d9b6ea4623f",
        min_motion_ratio=0.018,
        max_motion_ratio=0.28,
    ),
    "rickrolling-manager": AssetSpec(
        "rickrolling-manager",
        "rickrolling-manager-locked-v2.png",
        "da5217b904cc04c82a966f4de11f8dfe1c7101edcc828e1cbb9f6fe6e44b8c82",
        min_motion_ratio=0.010,
        max_motion_ratio=0.24,
    ),
    "ymca-ing-cma": AssetSpec(
        "ymca-ing-cma",
        "ymca-ing-cma-locked-v2.png",
        "685e5c0e4b410cfafdf2bd69438bb95f955ab62e73c4ab7739f2f887ab3af186",
        min_motion_ratio=0.08,
        max_motion_ratio=0.58,
    ),
    "wednesday-ing-offers": AssetSpec(
        "wednesday-ing-offers",
        "wednesday-ing-offers-locked-v2.png",
        "d0a27e14f2b56c073c3f615ff10f5f5e45997c361434ed1f96cc3c75952973df",
        min_motion_ratio=0.010,
        max_motion_ratio=0.22,
    ),
}


def build_disco(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    pivot = (474, 397)
    arm, erase, joint, authored = connected_part(
        plate,
        (
            (260, 34), (382, 34), (387, 185), (412, 258),
            (452, 331), (516, 377), (522, 423), (483, 455),
            (435, 429), (392, 380), (352, 328), (315, 258),
            (274, 181),
        ),
        pivot,
        27,
    )
    base = nearest_inpaint(plate, erase, dilate=1)
    phases = (0.0, 4.5, 9.0, 13.5)
    frames: list[Image.Image] = []
    allowed = [erase, authored]
    for angle in phases:
        moved = rotate_layer(arm, angle, pivot)
        frame = base.copy()
        frame.alpha_composite(moved)
        frame.alpha_composite(joint)
        frames.append(frame)
        allowed.append(moving_mask(moved))
    return frames, mask_union(allowed)


def build_rickroll(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    pivot = (718, 275)
    arm, erase, joint, authored = connected_part(
        plate,
        (
            (686, 211), (735, 225), (773, 247), (816, 227),
            (866, 194), (925, 169), (979, 146), (1002, 169),
            (979, 210), (925, 231), (872, 267), (821, 306),
            (775, 344), (731, 332), (700, 294),
        ),
        pivot,
        29,
    )
    base = nearest_inpaint(plate, erase, dilate=1)
    phases = (3.5, 1.0, -1.5, -4.5)
    frames: list[Image.Image] = []
    allowed = [erase, authored]
    for angle in phases:
        moved = rotate_layer(arm, angle, pivot)
        frame = base.copy()
        frame.alpha_composite(moved)
        frame.alpha_composite(joint)
        frames.append(frame)
        allowed.append(moving_mask(moved))
    return frames, mask_union(allowed)


def build_wednesday(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    elbow = (757, 388)
    forearm, erase, joint, authored = connected_part(
        plate,
        (
            (716, 351), (746, 356), (766, 308), (766, 251),
            (766, 185), (777, 132), (802, 130), (812, 178),
            (801, 247), (804, 309), (815, 363), (802, 410),
            (765, 425), (728, 404),
        ),
        elbow,
        25,
    )
    base = nearest_inpaint(plate, erase, dilate=1)
    phases = (-8.0, -2.5, 3.5, 9.0)
    frames: list[Image.Image] = []
    allowed = [erase, authored]
    for angle in phases:
        moved = rotate_layer(forearm, angle, elbow)
        frame = base.copy()
        frame.alpha_composite(moved)
        frame.alpha_composite(joint)
        frames.append(frame)
        allowed.append(moving_mask(moved))
    return frames, mask_union(allowed)


def articulated_arm(
    upper: Image.Image,
    forearm: Image.Image,
    shoulder: tuple[int, int],
    elbow: tuple[int, int],
    upper_angle: float,
    forearm_relative_angle: float,
) -> tuple[Image.Image, Image.Image]:
    """Move a two-segment arm while carrying its elbow with the upper arm."""
    moved_upper = rotate_layer(upper, upper_angle, shoulder)
    locally_bent = rotate_layer(forearm, forearm_relative_angle, elbow)
    moved_forearm = rotate_layer(locally_bent, upper_angle, shoulder)
    return moved_upper, moved_forearm


def clear_alpha_mask(image: Image.Image, erase_mask: Image.Image) -> Image.Image:
    """Remove an authored part without smearing its colour into green space."""
    rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8).copy()
    rgba[np.asarray(erase_mask) > 12, 3] = 0
    return Image.fromarray(rgba, mode="RGBA")


def ymca_arm_parts(plate: Image.Image) -> tuple[dict[str, Image.Image], Image.Image]:
    alpha = plate.getchannel("A")
    shapes = {
        "left_upper": polygon_mask(
            plate.size,
            ((340, 244), (378, 241), (422, 260), (481, 252),
             (525, 245), (575, 250), (594, 285), (570, 330),
             (520, 355), (480, 342), (412, 343), (361, 330),
             (333, 301)),
        ),
        "left_forearm": polygon_mask(
            plate.size,
            ((326, 49), (386, 47), (406, 114), (398, 181),
             (405, 248), (395, 302), (365, 337), (331, 309),
             (335, 246), (327, 172)),
        ),
        "right_upper": polygon_mask(
            plate.size,
            ((660, 285), (679, 250), (729, 245), (773, 252),
             (832, 260), (876, 241), (914, 244), (923, 303),
             (893, 332), (841, 343), (774, 342), (728, 355),
             (684, 330)),
        ),
        "right_forearm": polygon_mask(
            plate.size,
            ((868, 48), (927, 50), (928, 172), (920, 246),
             (925, 309), (891, 337), (860, 301), (849, 248),
             (857, 181), (849, 114)),
        ),
    }
    masks = {name: ImageChops.multiply(shape, alpha) for name, shape in shapes.items()}
    areas = {name: int((np.asarray(mask) > 12).sum()) for name, mask in masks.items()}
    for name, area in areas.items():
        if not 12000 <= area <= 95000:
            raise ValueError(f"YMCA {name} mask area unexpected: {area}")
    layers = {name: mask_layer(plate, shape) for name, shape in shapes.items()}
    # The source goalpost sleeves contain wide watercolour/ink fringes outside
    # the tight articulation polygons.  Erase the complete authored-arm zones
    # so no original hand or sleeve survives behind a moved pose.
    erase_shapes = (
        polygon_mask(
            plate.size,
            ((295, 24), (425, 24), (432, 221), (565, 221),
             (579, 366), (312, 366)),
        ),
        polygon_mask(
            plate.size,
            ((829, 24), (958, 24), (942, 366), (675, 366),
             (691, 221), (822, 221)),
        ),
    )
    erase = mask_union([ImageChops.multiply(shape, alpha) for shape in erase_shapes])

    # Keep a small authored shoulder socket in the fixed jacket; it hides any
    # subpixel filtering seam while every visible moving arm remains connected.
    yy, xx = np.indices((plate.height, plate.width))
    sockets = (
        ((xx - 535) ** 2 + (yy - 277) ** 2 <= 27 ** 2)
        | ((xx - 719) ** 2 + (yy - 277) ** 2 <= 27 ** 2)
    )
    erase_array = np.asarray(erase, dtype=np.uint8).copy()
    erase_array[sockets] = 0
    erase = Image.fromarray(erase_array, mode="L")
    return layers | {"erase": erase}, mask_union(list(masks.values()) + [erase])


def build_ymca(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    parts, authored = ymca_arm_parts(plate)
    base = clear_alpha_mask(plate, parts["erase"])
    # Restore only the immutable central jacket/shoulder core.  The broad erase
    # above removes every old arm pixel; this tight patch closes the two shoulder
    # sockets without reintroducing either original forearm or hand.
    torso_core = mask_layer(
        plate,
        polygon_mask(
            plate.size,
            ((480, 228), (552, 222), (590, 247), (665, 247),
             (702, 222), (774, 228), (782, 401), (759, 545),
             (495, 545), (472, 401)),
        ),
    )
    base.alpha_composite(torso_core)
    left_shoulder, left_elbow = (535, 277), (367, 286)
    right_shoulder, right_elbow = (719, 277), (891, 286)

    # Y, M, C, A.  The core never moves; only these four connected arm
    # articulations change.  C deliberately curves over and under the left side.
    poses = (
        (-45.0, 90.0, 45.0, -90.0),
        (-9.0, -43.0, 9.0, 43.0),
        (-48.0, 0.0, -45.0, 135.0),
        (-24.0, -22.0, 24.0, 22.0),
    )
    frames: list[Image.Image] = []
    allowed_masks = [authored, parts["erase"]]
    for left_upper_angle, left_forearm_angle, right_upper_angle, right_forearm_angle in poses:
        lu, lf = articulated_arm(
            parts["left_upper"], parts["left_forearm"],
            left_shoulder, left_elbow, left_upper_angle, left_forearm_angle,
        )
        ru, rf = articulated_arm(
            parts["right_upper"], parts["right_forearm"],
            right_shoulder, right_elbow, right_upper_angle, right_forearm_angle,
        )
        frame = base.copy()
        frame.alpha_composite(lu)
        frame.alpha_composite(lf)
        frame.alpha_composite(ru)
        frame.alpha_composite(rf)
        frames.append(frame)
        allowed_masks.extend([moving_mask(lu), moving_mask(lf), moving_mask(ru), moving_mask(rf)])
    return frames, mask_union(allowed_masks)


BUILDERS = {
    "disco-inferno-ing-reports": build_disco,
    "rickrolling-manager": build_rickroll,
    "ymca-ing-cma": build_ymca,
    "wednesday-ing-offers": build_wednesday,
}


def assert_ymca_candidate(
    spec: AssetSpec,
    frames: list[Image.Image],
    allowed: Image.Image,
) -> None:
    """Gate the four large intentional letter silhouettes with a fixed core.

    The shared assertion's 2.75px whole-silhouette centroid limit is designed
    for tiny loops.  YMCA deliberately moves both full arms between Y/M/C/A,
    so its silhouette centroid changes while the face, torso, pelvis and legs
    remain bit-identical.  This variant keeps every other structural guardrail
    and permits only that explained arm-induced centroid excursion.
    """
    import hashlib

    hashes = [hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames]
    if len(set(hashes)) != 4:
        raise ValueError(f"{spec.slug}: authored phases are not all unique")
    arrays = [np.asarray(frame, dtype=np.int16) for frame in frames]
    changed = np.zeros((627, 627), dtype=bool)
    for frame in arrays[1:]:
        changed |= np.any(frame != arrays[0], axis=2)
    escaped = changed & ~(np.asarray(allowed) > 0)
    if escaped.any():
        raise ValueError(f"{spec.slug}: {int(escaped.sum())} pixels changed outside the arm rig")

    subject_union = np.zeros((627, 627), dtype=bool)
    areas: list[int] = []
    centroids: list[tuple[float, float]] = []
    for index, frame in enumerate(frames):
        alpha = np.asarray(frame.getchannel("A")) > 12
        subject_union |= alpha
        ys, xs = np.nonzero(alpha)
        bbox = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)
        margin = min(bbox[0], bbox[1], 627 - bbox[2], 627 - bbox[3])
        if margin < 60:
            raise ValueError(f"{spec.slug}: frame {index} margin {margin}px below 60px")
        labels, count = ndimage.label(alpha, structure=np.ones((3, 3), dtype=np.uint8))
        component_areas = np.bincount(labels.ravel())[1:]
        significant = component_areas[component_areas >= max(32, round(alpha.sum() * 0.001))]
        if len(significant) != 1:
            raise ValueError(f"{spec.slug}: frame {index} has {len(significant)} significant components")
        areas.append(int(alpha.sum()))
        cy, cx = ndimage.center_of_mass(alpha)
        centroids.append((float(cx), float(cy)))

    ratio = float(changed.sum() / max(1, subject_union.sum()))
    if not spec.min_motion_ratio <= ratio <= spec.max_motion_ratio:
        raise ValueError(f"{spec.slug}: changed-pixel ratio {ratio:.6f} outside policy")
    area_span = (max(areas) - min(areas)) / max(areas)
    if area_span > 0.05:
        raise ValueError(f"{spec.slug}: foreground area span {area_span:.4f} exceeds 5%")
    anchor = centroids[0]
    max_shift = max(((x - anchor[0]) ** 2 + (y - anchor[1]) ** 2) ** 0.5 for x, y in centroids)
    if max_shift > 16.0:
        raise ValueError(f"{spec.slug}: intentional arm centroid shift {max_shift:.3f}px exceeds 16px")


def clean_frame(frame: Image.Image) -> Image.Image:
    frame = drop_tiny_alpha_islands(frame, minimum_area=24)
    for threshold in (48, 64, 96, 128):
        frame = remove_visible_satellite_components(
            frame,
            visibility_threshold=threshold,
            maximum_expected_area=360,
        )
    frame = zero_low_alpha_fringe(frame)
    return drop_tiny_alpha_islands(frame, minimum_area=24)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "qa/strict-repairs/pop-dance-hand-cleanup/candidates",
    )
    parser.add_argument("--promote", action="store_true")
    args = parser.parse_args()

    source_dir = args.output / "sources/wildcard"
    gif_dir = args.output / "gifs/wildcard"
    frame_root = args.output / "frames"
    source_dir.mkdir(parents=True, exist_ok=True)
    gif_dir.mkdir(parents=True, exist_ok=True)
    frame_root.mkdir(parents=True, exist_ok=True)

    for slug, spec in SPECS.items():
        raw = RAW_DIR / spec.raw_name
        actual = sha256(raw)
        if actual != spec.raw_sha256:
            raise ValueError(f"unexpected raw hash for {raw}: {actual}")
        plate = keep_largest_connected_subject(extract_alpha(raw))
        raw_frames, allowed_raw = BUILDERS[slug](plate)
        raw_frames = [clean_frame(frame) for frame in raw_frames]
        frames, allowed = fit_registered_sequence(raw_frames, allowed_raw)
        frames = [clean_frame(frame) for frame in frames]
        if slug == "ymca-ing-cma":
            assert_ymca_candidate(spec, frames, allowed)
        else:
            assert_candidate(spec, frames, allowed)

        source_out = source_dir / f"{slug}.png"
        gif_out = gif_dir / f"{slug}.gif"
        recompose_source(frames).save(source_out, optimize=True)
        assemble_shared_palette_gif(frames, gif_out)
        frame_dir = frame_root / slug
        frame_dir.mkdir(parents=True, exist_ok=True)
        for index, frame in enumerate(frames):
            frame.save(frame_dir / f"cell-{index}.png", optimize=True)
        allowed.save(frame_dir / "allowed-motion-mask.png", optimize=True)

        if args.promote:
            shutil.copy2(source_out, ROOT / f"sources/wildcard/{slug}.png")
            shutil.copy2(gif_out, ROOT / f"gifs/wildcard/{slug}.gif")
        print(f"{slug}: source={sha256(source_out)} gif={sha256(gif_out)}")


if __name__ == "__main__":
    main()
