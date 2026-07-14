# Independent QA — Pop & Dance follow-on batch F

> Historical generation/structural record. The final motion-semantic authority is `POP_DANCE_QA-SEMANTIC-REBUILD-2026-07-12.md`.


Date: 2026-07-12

Scope: read-only independent audit of the six final source masters under `sources/wildcard/` and independently assembled temporary GIFs under `/tmp/pop-dance-f-independent/gifs/`.

## Result

**PASS — 6/6. No release blocker found.**

Every source is exactly 1254×1254 RGB, uses an exact `#00ff00` key on all four outer edges and both two-pixel centre axes, has four distinct authored cells, and clears the required 60px content margin. Every independent GIF is 256×256, has six output frames and four unique phases, uses the exact reversible `0,1,2,3,2,1` sequence with `210,140,140,210,140,140ms` timing, loops forever, retains transparency with fully transparent corners, and is well below 750KB.

## Source structure

| Source | SHA-256 | Minimum margin | Four cells | Structural result |
|---|---|---:|---:|---|
| `wrecking-ball-riding-research.png` | `4c60c9ee93230aa0af48c6653d6caddff82639698d154369365f44bd4d4d5ad0` | 68px | 4 unique | PASS |
| `popping-my-collar-manager.png` | `14f19641e1f86a184f9e6468008970b20a418a5c4d447b08508d8edb96066a35` | 67px | 4 unique | PASS |
| `dirt-off-your-shoulders-marketing.png` | `879526f6d4f9f923f7bacf454d2eb7d351c0f289f06957f88ae45654ce6a81fd` | 67px | 4 unique | PASS |
| `reformering-offers.png` | `bcde1ab9b469730d0c52a264e7337b2a7b00166a58473d4ef3d4101dc4d3dff4` | 64px | 4 unique | PASS |
| `jazzing-content.png` | `ee03cce69aae75700b961c8f098844aa8f1e1f101d76fd8b2f82fe6509990341` | 61px | 4 unique | PASS |
| `jazzercising-reports.png` | `72b43a0c75f43b29533b130912a7e60cadd5b2c511063e9f82275238d020e554` | 63px | 4 unique | PASS |

## Frame-by-frame visual inspection

- **Wrecking-Balling:** All four full-size frames and the 128px render are uncropped. The chain, rider, boots, hands, saddle point, and ball remain one coherent connected unit throughout the small swing. Chain-link count and attachment do not change, the ball keeps the same form and shading, and the Homie has exactly two arms and two legs. No redraw shimmer was found.
- **Popping my collar:** Both hands remain attached and correctly placed on the same collar/lapel edges. Face, hair, jacket, shirt, belt, trousers, and shoes retain continuity. The small rigid adjustment reads as a collar pop without any duplicated fingers, detached cuff, changing jacket length, crop, or redraw wobble.
- **Getting that dirt off your shoulders:** The brushing hand remains connected at the same shoulder while the other arm stays at the side. The Homie is anatomically continuous, and the only extra activity is a small controlled dust-fleck progression beside the brushed shoulder. No stray flecks appear near edges and no body part changes form.
- **Reformering:** The reformer base, legs, rails, shoulder blocks, footbar, and screen perspective remain fixed. The Homie and carriage advance together in a small controlled leg-press movement; handles and straps stay connected and change length coherently. The machine does not bend, jump, or redraw, and the female Homie retains exactly two arms and two legs.
- **Jazzing:** The final replacement was re-audited after generation. The entire Homie, including connected arms, wrists, hands, and all fingers, is pixel-identical in all four cells. Only the tiny ink motion ticks beside the palms vary; pairwise source differences are confined to 462–488 tick pixels. This fully removes wrist, shoulder, and global redraw risk.
- **Jazzercising:** One continuous female full-body plate rocks and side-steps as a unit around a stable foot line. Both arms, both legs, face, hair, headband, leotard, tights, leg warmers, and shoes remain continuous. The motion is intentionally energetic but does not introduce anatomical redraw wiggle or cropping.

## Independently assembled GIFs

Assembly used `inset_ratio: 0`, identity post-split frame transforms, sequence `[0,1,2,3,2,1]`, and durations `[210,140,140,210,140,140]`.

| GIF | SHA-256 | Bytes | Contract |
|---|---|---:|---|
| `wrecking-ball-riding-research.gif` | `674b104ace03030934b4cb394fb91da8c30d0eb5954a21ba21a1730c7d2e0505` | 52,086 | PASS |
| `popping-my-collar-manager.gif` | `b717a6877ef1befc71218a12fdd8ca88138c28c65cde58a401394443e044b7c6` | 46,152 | PASS |
| `dirt-off-your-shoulders-marketing.gif` | `52d294a6ca653a155d0141d7b5ba58141e5a4cb86c0ff21e1b40de5388ae8d76` | 46,291 | PASS |
| `reformering-offers.gif` | `4ad7943e3841999fc4c56a94e4f4c707804cc5338d3ad6eb665fa9bf6fd92cf3` | 42,442 | PASS |
| `jazzing-content.gif` | `7e0771c2181ea031d89ae15f41b8cb64b7d42c8345540040b22c8eaeafb8e502` | 45,097 | PASS |
| `jazzercising-reports.gif` | `1ccf5a2caf6c3bfdc133c9a240c34160a6af9ee05e3684371172c4015ff818bd` | 34,553 | PASS |

The production verifier returned no errors for any independent GIF. Contact sheets:

- `/tmp/pop-dance-f-independent/contact/all-source-128.png`
- `/tmp/pop-dance-f-independent/contact/all-gif-128.png`
- Per-asset full-size, 128px, and six-frame GIF contacts are in `/tmp/pop-dance-f-independent/contact/`.
