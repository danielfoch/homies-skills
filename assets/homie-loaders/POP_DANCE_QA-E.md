# Pop & Dance E — QA ledger

> Historical generation/structural record. The final motion-semantic authority is `POP_DANCE_QA-SEMANTIC-REBUILD-2026-07-12.md`.


Generated with the built-in image-generation tool, one call per asset, then deterministically rebuilt from one canonical plate per animation before assembly.

## Contract checks

| slug | source | min cell margin | distinct authored cells | temp GIF | bytes | result |
|---|---:|---:|---:|---:|---:|---|
| `reformering-offers` | 1254×1254 RGB | 64 px | 4 | 256×256, 6 frames | 42,442 | PASS |
| `jazzing-content` | 1254×1254 RGB | 61 px | 4 | 256×256, 6 frames | 44,736 | PASS |
| `jazzercising-reports` | 1254×1254 RGB | 63 px | 4 | 256×256, 6 frames | 34,553 | PASS |

For every source, all four corners, all outer boundaries, and both 2×2 split axes are exact `#00ff00`. Every source has four byte-distinct cells. For every GIF, the sequence is `[0,1,2,3,2,1]`, the durations are `[210,140,140,210,140,140]`, looping is infinite, transparency is present, all corners are transparent, and four visually distinct frames survive quantization.

Machine-readable evidence:

- `/tmp/pop-dance-e/source-audit.json`
- `/tmp/pop-dance-e/fixed-layer-audit.json`
- `/tmp/pop-dance-e-alignment.json`

## Anti-wiggle construction

### `reformering-offers`

- One raw cell supplied the canonical Offers Homie, reformer and side-view perspective.
- The fixed base layer contains the reformer base, rails, footbar and tower. These pixels are identical in all four cells; after masking the intentionally moving carriage/body/strap region, all four fixed-region SHA-256 hashes are `7e859ae71313e76111e819bf72a2f04e47d8dde8037caa3f219b9c75cdcee318`.
- A single connected Homie + carriage plate moves horizontally by exactly `0/5/10/15` raw-cell pixels. The straps are deterministically redrawn between the moving handle origin and one fixed machine anchor.
- The Homie’s face, anatomy, clothing, carriage, machine design, scale and perspective never redraw or morph.

### `jazzing-content`

- One complete Content Homie is the canonical plate.
- Head, hair, face, torso, shirt, trousers, legs and shoes are pixel-identical across all authored phases.
- Both connected arms, hands and all ten fingers remain pixel-identical. Three tiny ink motion ticks beside each palm move by deterministic `0/-3/+3/-1` raw-cell pixels, giving the hands a visible jazz shimmer without any wrist seam.
- After masking only those motion-tick areas, the fixed full-body region has one identical hash across all four cells: `0c3a9513ae367d793bdd8f1f71e3dca98949988d821a9858b9d1bdc1f6eefc91`.

### `jazzercising-reports`

- The accepted raised-arm side-step cell supplied one canonical full-body Reports Homie plate (`e2db5b10131489bd65765311c405b41927745df512afd14b0efa7d2dcd311f15`).
- Exactly that plate is reused in every phase. Tiny deterministic horizontal steps and sub-two-degree rocks occur around the fixed foot baseline; there is no model redraw between frames.
- Identity, hair, face, outfit, limb count, proportions and costume colors therefore remain continuous.

## Visual inspection

Inspected the reversible six-frame contact strips at full 256 px and scaled to 128 px on the site’s off-white matte:

- no cropped heads, hands, feet, reformer ends or raised arms;
- no extra/detached limbs or duplicate props;
- no text, logos, emblems, panel dividers, shadows or background objects;
- reformer machine stays screen-fixed while the carriage/body advances smoothly;
- jazz hands read as a contained motion-tick shimmer with the entire connected body locked;
- jazzercise reads as an energetic raised-arm side-step without identity or costume changes.

Contact sheets:

- `/tmp/pop-dance-e/contact/reformering-offers-full.jpg`
- `/tmp/pop-dance-e/contact/reformering-offers-128.jpg`
- `/tmp/pop-dance-e/contact/jazzing-content-full.jpg`
- `/tmp/pop-dance-e/contact/jazzing-content-128.jpg`
- `/tmp/pop-dance-e/contact/jazzercising-reports-full.jpg`
- `/tmp/pop-dance-e/contact/jazzercising-reports-128.jpg`

Temp GIFs:

- `/tmp/pop-dance-e/gifs/reformering-offers.gif`
- `/tmp/pop-dance-e/gifs/jazzing-content.gif`
- `/tmp/pop-dance-e/gifs/jazzercising-reports.gif`
- 128 px inspection builds are in `/tmp/pop-dance-e/gifs-128/`.
