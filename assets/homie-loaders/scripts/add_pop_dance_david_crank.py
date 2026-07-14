#!/usr/bin/env python3
"""Build four locked-plate Pop & Dance loaders without redraw jitter.

Each loader starts from one SHA-locked, role-canonical ink-and-watercolour
plate.  The three Crank That variants move only complete connected limb units;
the character core, crop, scale and bottom anchor remain shared.  David
Blaining intentionally retains one detached flying card, which is isolated as
the plate's second alpha component and animated along a small controlled arc.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops
from scipy import ndimage

from assemble_sprite import extract_alpha
from repair_character_assignment_batch import clean_frame, connected_part
from repair_movie_style_canonical_six import (
    AssetSpec,
    CELL,
    DURATIONS_MS,
    RAW_DIR,
    ROOT,
    SAFE_MARGIN,
    SEQUENCE,
    SITE_MATTE,
    assert_candidate,
    assemble_shared_palette_gif,
    drop_tiny_alpha_islands,
    fit_registered_sequence,
    keep_largest_connected_subject,
    mask_layer,
    mask_union,
    moving_mask,
    nearest_inpaint,
    recompose_source,
    rotate_layer,
    sha256,
    zero_low_alpha_fringe,
)


@dataclass(frozen=True)
class LockedSpec:
    asset: AssetSpec
    prompt_description: str


SPECS = {
    "david-blaining-manager": LockedSpec(
        AssetSpec(
            "david-blaining-manager",
            "david-blaining-manager-generated.png",
            "781b10a5b781af750efc6dab8498b8600cc9f5c420bb259f0c2a79561ec4aa65",
            min_motion_ratio=0.006,
            max_motion_ratio=0.10,
        ),
        "Male canonical Manager Homie in an all-black street-magician outfit, "
        "holding a deck while one card travels through a six-card flying arc.",
    ),
    "cranking-that-marketing": LockedSpec(
        AssetSpec(
            "cranking-that-marketing",
            "cranking-that-marketing-generated.png",
            "60db85344c9d2a344032b44b3792cb72e7d19a2012b63bfee832bbfc957065c2",
            min_motion_ratio=0.055,
            max_motion_ratio=0.46,
        ),
        "Male canonical Marketing Homie in the white graffiti jacket, red long "
        "shirt, sideways cap, wraparound shades and black/yellow pants, doing "
        "the Crank That Superman wing sweep.",
    ),
    "cranking-the-step-marketing": LockedSpec(
        AssetSpec(
            "cranking-the-step-marketing",
            "cranking-the-step-marketing-generated.png",
            "a8e104a7e66a0dcd8f400356c770c05dcbf99dd9c25d3a3d78d7a7f693f1073c",
            min_motion_ratio=0.025,
            max_motion_ratio=0.30,
        ),
        "Male canonical Marketing Homie in the requested Crank That wardrobe, "
        "holding the crossed-foot small-hop pose while both fists pump.",
    ),
    "cranking-the-motorbike-marketing": LockedSpec(
        AssetSpec(
            "cranking-the-motorbike-marketing",
            "cranking-the-motorbike-marketing-generated.png",
            "683c904aa93e2c7d4defb365a5538ebaa17a6956473258df49f1f0f839056a33",
            min_motion_ratio=0.035,
            max_motion_ratio=0.32,
        ),
        "Male canonical Marketing Homie in the requested Crank That wardrobe, "
        "bouncing low while his two complete arms counter-rev imaginary "
        "motorcycle handlebars.",
    ),
}


def keep_n_components(image: Image.Image, count: int) -> Image.Image:
    """Retain exactly the largest ``count`` authored alpha components."""
    rgba = np.asarray(image.convert("RGBA"), dtype=np.uint8).copy()
    visible = rgba[:, :, 3] > 6
    labels, found = ndimage.label(
        visible, structure=np.ones((3, 3), dtype=np.uint8)
    )
    if found < count:
        raise ValueError(f"expected at least {count} alpha components, found {found}")
    areas = np.bincount(labels.ravel())
    ranked = np.argsort(areas[1:])[::-1][:count] + 1
    keep = np.isin(labels, ranked)
    rgba[~keep, 3] = 0
    return Image.fromarray(rgba, mode="RGBA")


def second_component_mask(plate: Image.Image) -> Image.Image:
    """Return the detached outer card, including its antialiased boundary."""
    alpha = np.asarray(plate.getchannel("A"), dtype=np.uint8)
    labels, found = ndimage.label(
        alpha > 12, structure=np.ones((3, 3), dtype=np.uint8)
    )
    if found != 2:
        raise ValueError(f"David plate must have body+card components, found {found}")
    areas = np.bincount(labels.ravel())
    order = np.argsort(areas[1:])[::-1] + 1
    card_label = int(order[1])
    core = labels == card_label
    if not 2500 <= int(core.sum()) <= 5000:
        raise ValueError(f"unexpected detached-card area: {int(core.sum())}")
    expanded = ndimage.binary_dilation(core, iterations=2) & (alpha > 0)
    return Image.fromarray((expanded * 255).astype(np.uint8), mode="L")


def build_david(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    card_mask = second_component_mask(plate)
    card = mask_layer(plate, card_mask)
    card_pixels = np.asarray(card_mask) > 0
    base_rgba = np.asarray(plate.convert("RGBA"), dtype=np.uint8).copy()
    base_rgba[card_pixels, 3] = 0
    base = Image.fromarray(base_rgba, mode="RGBA")

    # The other five cards remain locked to the character plate. The outer
    # sixth card follows a compact up-and-out arc with no camera movement.
    phases = (
        (-4.0, 38, -4),
        (0.0, 48, -10),
        (8.0, 60, -18),
        (3.0, 50, -12),
    )
    frames: list[Image.Image] = []
    allowed = [card_mask]
    for angle, dx, dy in phases:
        moved = rotate_layer(card, angle, (878, 386), dx, dy)
        frame = base.copy()
        frame.alpha_composite(moved)
        frame = zero_low_alpha_fringe(drop_tiny_alpha_islands(frame, 16))
        frames.append(frame)
        allowed.append(moving_mask(moved))
    return frames, mask_union(allowed)


def two_arm_rig(
    plate: Image.Image,
    left_polygon: tuple[tuple[int, int], ...],
    left_pivot: tuple[int, int],
    right_polygon: tuple[tuple[int, int], ...],
    right_pivot: tuple[int, int],
    phases: tuple[tuple[float, float], ...],
    joint_radius: int,
) -> tuple[list[Image.Image], Image.Image]:
    left, left_erase, left_joint, left_mask = connected_part(
        plate, left_polygon, left_pivot, joint_radius
    )
    right, right_erase, right_joint, right_mask = connected_part(
        plate, right_polygon, right_pivot, joint_radius
    )
    left_area = int((np.asarray(left_mask) > 12).sum())
    right_area = int((np.asarray(right_mask) > 12).sum())
    if left_area < 10000 or right_area < 10000:
        raise ValueError(f"arm masks too small: {left_area}, {right_area}")
    base = nearest_inpaint(
        nearest_inpaint(plate, left_erase, dilate=1),
        right_erase,
        dilate=1,
    )
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


def build_superman(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    return two_arm_rig(
        plate,
        (
            (420, 286), (522, 304), (528, 356), (493, 407),
            (431, 448), (363, 488), (289, 528), (218, 566),
            (151, 591), (91, 589), (70, 554), (78, 515),
            (126, 485), (197, 466), (270, 425), (348, 369),
        ),
        (470, 338),
        (
            (645, 248), (725, 225), (805, 226), (887, 218),
            (975, 196), (1064, 169), (1142, 166), (1191, 190),
            (1200, 226), (1177, 269), (1112, 297), (1032, 316),
            (946, 336), (853, 354), (762, 366), (684, 343),
        ),
        (687, 302),
        ((-2.8, 2.8), (-0.8, 0.8), (2.8, -2.8), (0.8, -0.8)),
        34,
    )


def build_step(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    return two_arm_rig(
        plate,
        (
            (376, 278), (438, 270), (469, 305), (476, 352),
            (464, 400), (438, 443), (402, 475), (358, 476),
            (329, 447), (330, 403), (346, 353),
        ),
        (421, 410),
        (
            (747, 270), (788, 246), (818, 218), (857, 217),
            (887, 247), (895, 289), (884, 330), (861, 372),
            (831, 414), (789, 430), (752, 401), (736, 350),
        ),
        (778, 377),
        ((-5.5, 4.5), (-1.5, 1.0), (5.5, -4.5), (1.5, -1.0)),
        28,
    )


def build_motorbike(plate: Image.Image) -> tuple[list[Image.Image], Image.Image]:
    return two_arm_rig(
        plate,
        (
            (425, 421), (490, 419), (515, 461), (543, 498),
            (578, 530), (588, 561), (568, 590), (536, 604),
            (502, 579), (474, 548), (444, 512), (426, 468),
        ),
        (468, 468),
        (
            (758, 379), (821, 382), (851, 411), (888, 431),
            (936, 447), (972, 466), (985, 493), (974, 520),
            (944, 537), (904, 529), (864, 511), (826, 488),
            (790, 458), (765, 423),
        ),
        (805, 425),
        ((-5.0, 5.0), (-1.5, 1.5), (5.0, -5.0), (1.5, -1.5)),
        25,
    )


BUILDERS = {
    "david-blaining-manager": build_david,
    "cranking-that-marketing": build_superman,
    "cranking-the-step-marketing": build_step,
    "cranking-the-motorbike-marketing": build_motorbike,
}


def assert_david(
    spec: AssetSpec, frames: list[Image.Image], allowed: Image.Image
) -> None:
    hashes = [hashlib.sha256(frame.tobytes()).hexdigest() for frame in frames]
    if len(set(hashes)) != 4:
        raise ValueError("David authored phases are not all unique")
    arrays = [np.asarray(frame, dtype=np.int16) for frame in frames]
    changed = np.zeros((CELL, CELL), dtype=bool)
    for candidate in arrays[1:]:
        changed |= np.any(candidate != arrays[0], axis=2)
    escaped = changed & ~(np.asarray(allowed) > 0)
    if escaped.any():
        raise ValueError(f"David: {int(escaped.sum())} pixels changed outside card arc")

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
            raise ValueError(f"David frame {index} margin {margin}px below {SAFE_MARGIN}px")
        cy, cx = ndimage.center_of_mass(alpha)
        centroids.append((float(cx), float(cy)))
        for threshold in (1, 8, 16, 32, 48, 64, 96, 128):
            labels, found = ndimage.label(
                alpha_u8 >= threshold,
                structure=np.ones((3, 3), dtype=np.uint8),
            )
            component_areas = np.bincount(labels.ravel())[1:] if found else np.array([])
            significant = component_areas[component_areas >= 32]
            if len(significant) != 2:
                raise ValueError(
                    f"David frame {index} has {len(significant)} significant "
                    f"components at alpha {threshold}; expected body+card"
                )
    ratio = float(changed.sum() / max(1, union.sum()))
    if not spec.min_motion_ratio <= ratio <= spec.max_motion_ratio:
        raise ValueError(f"David motion ratio {ratio:.6f} outside locked limits")
    if (max(areas) - min(areas)) / max(areas) > 0.025:
        raise ValueError("David foreground area span exceeds 2.5%")
    anchor = centroids[0]
    shift = max(
        ((x - anchor[0]) ** 2 + (y - anchor[1]) ** 2) ** 0.5
        for x, y in centroids
    )
    if shift > 1.5:
        raise ValueError(f"David card-driven centroid shift {shift:.3f}px exceeds 1.5px")


def assemble_shared_palette_gif_with_cards(
    frames: list[Image.Image], output: Path
) -> None:
    """Shared-palette GIF encoder that preserves the intentional loose card."""
    resized = [frame.resize((256, 256), Image.Resampling.LANCZOS) for frame in frames]
    resized = [drop_tiny_alpha_islands(frame, minimum_area=8) for frame in resized]
    resized = [zero_low_alpha_fringe(frame) for frame in resized]
    resized = [drop_tiny_alpha_islands(frame, minimum_area=8) for frame in resized]

    # Gate body+card continuity at the actual loader resolution.
    for index, frame in enumerate(resized):
        alpha = np.asarray(frame.getchannel("A"), dtype=np.uint8)
        for threshold in (16, 48, 96, 128):
            labels, found = ndimage.label(
                alpha >= threshold, structure=np.ones((3, 3), dtype=np.uint8)
            )
            areas = np.bincount(labels.ravel())[1:] if found else np.array([])
            significant = areas[areas >= 8]
            if len(significant) != 2:
                raise ValueError(
                    f"David GIF phase {index} has {len(significant)} visible "
                    f"components at alpha {threshold}; expected body+card"
                )

    composited: list[Image.Image] = []
    for frame in resized:
        matte = Image.new("RGBA", frame.size, SITE_MATTE + (255,))
        composited.append(Image.alpha_composite(matte, frame).convert("RGB"))
    contact = Image.new("RGB", (256 * len(composited), 256), SITE_MATTE)
    for index, frame in enumerate(composited):
        contact.paste(frame, (index * 256, 0))
    palette_reference = contact.quantize(
        colors=95,
        method=Image.Quantize.MEDIANCUT,
        dither=Image.Dither.NONE,
    )
    palette = palette_reference.getpalette()[: 255 * 3]
    palette.extend([0] * (255 * 3 - len(palette)))
    palette.extend([0, 0, 0])
    palette_reference.putpalette(palette)

    encoded: list[Image.Image] = []
    for index in SEQUENCE:
        frame = resized[index]
        pal = composited[index].quantize(
            palette=palette_reference, dither=Image.Dither.NONE
        )
        pal.putpalette(palette)
        transparent = frame.getchannel("A").point(lambda value: 255 if value < 96 else 0)
        pal.paste(255, mask=transparent)
        pal.info["transparency"] = 255
        pal.info["background"] = 255
        encoded.append(pal)
    output.parent.mkdir(parents=True, exist_ok=True)
    encoded[0].save(
        output,
        save_all=True,
        append_images=encoded[1:],
        duration=DURATIONS_MS,
        loop=0,
        disposal=2,
        transparency=255,
        optimize=False,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "qa/strict-repairs/new-pop-dance-additions/candidate",
    )
    parser.add_argument("--promote", action="store_true")
    parser.add_argument("slugs", nargs="*", choices=sorted(SPECS))
    args = parser.parse_args()
    slugs = args.slugs or list(SPECS)

    source_dir = args.output / "sources/wildcard"
    gif_dir = args.output / "gifs/wildcard"
    frame_root = args.output / "frames"
    source_dir.mkdir(parents=True, exist_ok=True)
    gif_dir.mkdir(parents=True, exist_ok=True)

    for slug in slugs:
        locked = SPECS[slug]
        spec = locked.asset
        raw = RAW_DIR / spec.raw_name
        actual = sha256(raw)
        if actual != spec.raw_sha256:
            raise ValueError(f"unexpected raw hash for {raw}: {actual}")

        extracted = extract_alpha(raw)
        if slug == "david-blaining-manager":
            plate = keep_n_components(extracted, 2)
        else:
            plate = clean_frame(keep_largest_connected_subject(extracted), 16)
        authored, allowed_raw = BUILDERS[slug](plate)
        fitted, allowed = fit_registered_sequence(authored, allowed_raw)
        if slug == "david-blaining-manager":
            fitted = [
                zero_low_alpha_fringe(drop_tiny_alpha_islands(frame, 16))
                for frame in fitted
            ]
            assert_david(spec, fitted, allowed)
        else:
            fitted = [clean_frame(frame, 16) for frame in fitted]
            assert_candidate(spec, fitted, allowed)

        source_out = source_dir / f"{slug}.png"
        gif_out = gif_dir / f"{slug}.gif"
        frame_dir = frame_root / slug
        frame_dir.mkdir(parents=True, exist_ok=True)
        recompose_source(fitted).save(source_out, optimize=True)
        if slug == "david-blaining-manager":
            assemble_shared_palette_gif_with_cards(fitted, gif_out)
        else:
            assemble_shared_palette_gif(fitted, gif_out)
        for index, frame in enumerate(fitted):
            frame.save(frame_dir / f"cell-{index}.png", optimize=True)
        allowed.save(frame_dir / "allowed-motion-mask.png", optimize=True)

        if args.promote:
            shutil.copy2(source_out, ROOT / f"sources/wildcard/{slug}.png")
            shutil.copy2(gif_out, ROOT / f"gifs/wildcard/{slug}.gif")
        print(
            f"{slug}: source={sha256(source_out)} gif={sha256(gif_out)} "
            f"prompt={locked.prompt_description}"
        )


if __name__ == "__main__":
    main()
