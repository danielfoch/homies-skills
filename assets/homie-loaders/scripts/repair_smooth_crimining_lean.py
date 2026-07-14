#!/usr/bin/env python3
"""Build the Smooth-Crimining loader from one immutable Marketing Homie plate.

The generated artwork already contains the signature impossible lean.  The
animation deepens that lean with one deterministic, ankle-anchored shear.  The
entire shoe/contact region is copied byte-for-byte from the locked source plate
in every phase, while one shared crop, scale, bottom anchor and GIF palette
prevent the frame-to-frame registration wiggle seen in independent redraws.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops
from scipy import ndimage

from assemble_sprite import extract_alpha
from repair_movie_style_canonical_six import (
    CELL,
    RAW_DIR,
    ROOT,
    SAFE_MARGIN,
    assemble_shared_palette_gif,
    drop_tiny_alpha_islands,
    fit_registered_sequence,
    keep_largest_connected_subject,
    mask_union,
    moving_mask,
    recompose_source,
    remove_visible_satellite_components,
    zero_low_alpha_fringe,
)


SLUG = "smooth-crimining-marketing"
RAW_NAME = "smooth-crimining-marketing-generated.png"
RAW_SHA256 = "07decf70b68b2329be55962c20143e6a49d6e72694d33f6ec40c2fdd2b65ca03"
PHASE_SHEARS = (0.0, 0.040, 0.080, 0.120)
# The generated plate's shoes and ankle cuffs are entirely below this line.
# Pixels at and below the anchor are copied exactly from the source in every
# phase; the shear displacement converges continuously to zero at the line.
ANKLE_ANCHOR_Y = 1080


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clean_frame(frame: Image.Image) -> Image.Image:
    frame = drop_tiny_alpha_islands(frame, minimum_area=16)
    for threshold in (48, 64, 96, 128):
        frame = remove_visible_satellite_components(
            frame,
            visibility_threshold=threshold,
            maximum_expected_area=320,
        )
    frame = zero_low_alpha_fringe(frame)
    return drop_tiny_alpha_islands(frame, minimum_area=16)


def ankle_anchored_lean(plate: Image.Image, shear: float) -> Image.Image:
    """Shear only rows above the ankles, converging to zero at the shoes."""
    transformed = plate.transform(
        plate.size,
        Image.Transform.AFFINE,
        (1.0, shear, -shear * ANKLE_ANCHOR_Y, 0.0, 1.0, 0.0),
        resample=Image.Resampling.BICUBIC,
    )
    frame = Image.new("RGBA", plate.size, (0, 0, 0, 0))
    frame.alpha_composite(transformed.crop((0, 0, plate.width, ANKLE_ANCHOR_Y)), (0, 0))
    # Immutable contact patch: cuffs, socks, both complete shoes, and soles.
    frame.alpha_composite(
        plate.crop((0, ANKLE_ANCHOR_Y, plate.width, plate.height)),
        (0, ANKLE_ANCHOR_Y),
    )
    return frame


def raw_frames(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    frames = [clean_frame(ankle_anchored_lean(plate, shear)) for shear in PHASE_SHEARS]
    allowed = mask_union([moving_mask(frame) for frame in frames])
    return frames, allowed


def assert_raw_contract(plate: Image.Image, frames: list[Image.Image]) -> None:
    hashes = [hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames]
    if len(set(hashes)) != 4:
        raise ValueError("all four authored lean phases must be unique")

    # Cleanup may normalize a few identical low-alpha edge pixels, so compare
    # every phase to phase zero rather than to the pre-clean plate bytes.
    locked_contact = np.asarray(frames[0].convert("RGBA"), dtype=np.uint8)[
        ANKLE_ANCHOR_Y:, :, :
    ]
    for index, frame in enumerate(frames):
        frame_rgba = np.asarray(frame.convert("RGBA"), dtype=np.uint8)
        if not np.array_equal(frame_rgba[ANKLE_ANCHOR_Y:, :, :], locked_contact):
            raise ValueError(f"phase {index} changed the locked shoe/contact patch")

    areas: list[int] = []
    for index, frame in enumerate(frames):
        alpha = np.asarray(frame.getchannel("A"), dtype=np.uint8)
        areas.append(int((alpha > 12).sum()))
        for threshold in (1, 8, 16, 32, 48, 64, 96, 128):
            labels, count = ndimage.label(
                alpha >= threshold,
                structure=np.ones((3, 3), dtype=np.uint8),
            )
            component_areas = np.bincount(labels.ravel())[1:] if count else np.array([])
            significant = component_areas[component_areas >= 32]
            if len(significant) != 1:
                raise ValueError(
                    f"phase {index} has {len(significant)} significant components "
                    f"at alpha {threshold}"
                )
    area_span = (max(areas) - min(areas)) / max(areas)
    if area_span > 0.02:
        raise ValueError(f"foreground area span {area_span:.4f} exceeds 2%")


def assert_fitted_contract(frames: list[Image.Image], allowed: Image.Image) -> None:
    hashes = [hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames]
    if len(set(hashes)) != 4:
        raise ValueError("fitted phases are not all unique")

    arrays = [np.asarray(frame.convert("RGBA"), dtype=np.int16) for frame in frames]
    changed = np.zeros((CELL, CELL), dtype=bool)
    for candidate in arrays[1:]:
        changed |= np.any(candidate != arrays[0], axis=2)
    escaped = changed & ~(np.asarray(allowed) > 0)
    if escaped.any():
        raise ValueError(f"{int(escaped.sum())} fitted pixels changed outside the rig sweep")

    union = np.zeros((CELL, CELL), dtype=bool)
    areas: list[int] = []
    widths: list[int] = []
    heights: list[int] = []
    for index, frame in enumerate(frames):
        alpha_u8 = np.asarray(frame.getchannel("A"), dtype=np.uint8)
        alpha = alpha_u8 > 12
        union |= alpha
        areas.append(int(alpha.sum()))
        ys, xs = np.nonzero(alpha)
        bbox = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)
        margin = min(bbox[0], bbox[1], CELL - bbox[2], CELL - bbox[3])
        if margin < SAFE_MARGIN:
            raise ValueError(f"phase {index} margin {margin}px below {SAFE_MARGIN}px")
        widths.append(bbox[2] - bbox[0])
        heights.append(bbox[3] - bbox[1])
        for threshold in (1, 8, 16, 32, 48, 64, 96, 128):
            labels, count = ndimage.label(
                alpha_u8 >= threshold,
                structure=np.ones((3, 3), dtype=np.uint8),
            )
            component_areas = np.bincount(labels.ravel())[1:] if count else np.array([])
            significant = component_areas[component_areas >= 32]
            if len(significant) != 1:
                raise ValueError(
                    f"fitted phase {index} has {len(significant)} significant components "
                    f"at alpha {threshold}"
                )

    motion_ratio = float(changed.sum() / max(1, union.sum()))
    # A lean is a deliberately global silhouette action: nearly every row above
    # the locked ankles shifts by a different amount.  A high changed-pixel
    # ratio is therefore expected and is not the redraw jitter this gate targets.
    if not 0.50 <= motion_ratio <= 1.0:
        raise ValueError(f"changed-pixel ratio {motion_ratio:.4f} outside [0.50, 1.0]")
    if (max(areas) - min(areas)) / max(areas) > 0.02:
        raise ValueError("fitted foreground area span exceeds 2%")
    if (max(widths) - min(widths)) / np.median(widths) > 0.20:
        raise ValueError("fitted bbox-width span exceeds the authored lean allowance")
    if (max(heights) - min(heights)) / np.median(heights) > 0.02:
        raise ValueError("fitted bbox-height span exceeds 2%")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("/tmp/smooth-crimining"))
    parser.add_argument("--promote", action="store_true")
    args = parser.parse_args()

    raw = RAW_DIR / RAW_NAME
    actual = sha256(raw)
    if actual != RAW_SHA256:
        raise ValueError(f"unexpected raw hash for {raw}: {actual}")

    plate = clean_frame(keep_largest_connected_subject(extract_alpha(raw)))
    authored, allowed_raw = raw_frames(plate)
    assert_raw_contract(plate, authored)
    fitted, allowed = fit_registered_sequence(authored, allowed_raw)
    fitted = [clean_frame(frame) for frame in fitted]
    assert_fitted_contract(fitted, allowed)

    source_dir = args.output / "sources/wildcard"
    gif_dir = args.output / "gifs/wildcard"
    frame_dir = args.output / f"frames/{SLUG}"
    source_dir.mkdir(parents=True, exist_ok=True)
    gif_dir.mkdir(parents=True, exist_ok=True)
    frame_dir.mkdir(parents=True, exist_ok=True)

    source_out = source_dir / f"{SLUG}.png"
    gif_out = gif_dir / f"{SLUG}.gif"
    recompose_source(fitted).save(source_out, optimize=True)
    assemble_shared_palette_gif(fitted, gif_out)
    for index, frame in enumerate(fitted):
        frame.save(frame_dir / f"cell-{index}.png", optimize=True)
    allowed.save(frame_dir / "allowed-motion-mask.png", optimize=True)

    if args.promote:
        shutil.copy2(source_out, ROOT / f"sources/wildcard/{SLUG}.png")
        shutil.copy2(gif_out, ROOT / f"gifs/wildcard/{SLUG}.gif")

    print(f"{SLUG}: source={sha256(source_out)} gif={sha256(gif_out)}")


if __name__ == "__main__":
    main()
