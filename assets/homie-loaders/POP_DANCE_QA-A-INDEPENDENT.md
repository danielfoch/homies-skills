# Pop & Dance A — Independent QA

> Historical generation/structural record. The final motion-semantic authority is `POP_DANCE_QA-SEMANTIC-REBUILD-2026-07-12.md`.


Status: **PASS — 12/12 masters, 12/12 independently assembled GIFs**

Audit mode: read-only. No source, project alignment, manifest, documentation, deployment, or Drive file was modified.

## Source contract

Every source passes:

- exact 1254×1254 RGB;
- exact flat `#00ff00` on all four outer edges and both pixels of both centre axes;
- four distinct authored-cell hashes;
- one complete full-body Homie per 627×627 cell;
- at least 60 px clearance in every direction;
- no crop, extra person, duplicate limb, detached hand/foot, wraparound fragment, or disappearing clothing/prop.

| Source | Minimum clearance | Result |
|---|---:|---|
| `sell-phoning-manager` | 60 px | PASS — superseding user-reference rebuild |
| `back-togethering-content` | 71 px | PASS |
| `shake-it-offing-research` | 66 px | PASS |
| `twenty-two-ing-crm` | 67 px | PASS |
| `single-ladying-offers` | 68 px | PASS |
| `thrillering-marketing` | 69 px | PASS |
| `moonwalking-content` | 66 px | PASS |
| `bad-romancing-reports` | 64 px | PASS |
| `poker-facing-listings` | 68 px | PASS |
| `gangnam-styling-cma` | 62 px | PASS |
| `call-me-maybeing-research` | 64 px | PASS |
| `bye-bye-bye-ing-listings` | 71 px | PASS |

Machine-readable source results: `/tmp/pop-dance-a-independent-source-qa.json`

## Full-size and 128 px continuity inspection

I inspected all 48 authored cells at 256 px and again at 128 px, with special attention to phones, glasses, hands, and feet.

- `sell-phoning-manager`: saturated orange puffer and four screenshot-derived Hotline Bling beats—low finger-flick crouch, stop palm, opposite-side point/sweep, and face-level bob—remain readable at 128px; exactly two attached hands and two legs, with no debris or generic sway.
- `back-togethering-content`: phone remains continuously connected at the same ear while the free hand performs the intentional “nope” gesture; glasses and floral jacket remain stable.
- `shake-it-offing-research`: rigid shoulder shake with consistent curls, face, silver jacket, skirt, legs, and boots; no global redraw shimmer.
- `twenty-two-ing-crm`: red heart-style glasses, hat, adjusting hand, necklace, shirt, feet, and identity remain present and aligned in every phase.
- `single-ladying-offers`: raised ring-finger hand and hip hand remain anatomically connected; bun, leotard, legs, and crossed-foot silhouette are continuous.
- `thrillering-marketing`: both zombie hands keep the correct limb count and connection; red jacket, face/beard, trousers, socks, and shoes are stable through the shoulder pop.
- `moonwalking-content`: feet progress deliberately through the glide/cross-step while the head, torso, jacket, arms, trouser silhouette, and floor baseline stay coherent; no shoe duplication or leg swap.
- `bad-romancing-reports`: monster-claw hand motion is deliberate and reversible; headpiece, hair, angular outfit, face, arms, legs, and boots remain continuous.
- `poker-facing-listings`: sunglasses and adjusting hand remain connected and readable; glasses lower/raise without changing identity, suit, feet, or limb count.
- `gangnam-styling-cma`: crossed hands and sunglasses are stable; compact rigid horse-riding bounce has no global redraw or foot crop.
- `call-me-maybeing-research`: phone stays at the same ear while only the free hand waves through the intended arc; face, curls, jacket, skirt, tights, and boots remain consistent.
- `bye-bye-bye-ing-listings`: synchronized pointing/crossing hand sequence stays anatomically coherent; glasses, hair, shirt, trousers, feet, and baseline remain registered.

No global redraw wiggle, prop/pose substitution, three-hand frame, disappearing phone/glasses, foot discontinuity, or crop blocker was found.

Authored-frame evidence:

- Full 256 px contacts: `/tmp/pop-dance-a-independent/contact/authored-full-1.jpg` through `authored-full-4.jpg`
- 128 px contact: `/tmp/pop-dance-a-independent/contact/authored-128.jpg`

## Independent GIF assembly

All twelve sources were independently assembled with `scripts/assemble_sprite.py` using `/tmp/pop-dance-a-alignment.json` and the intended production sequence `0,1,2,3,2,1`.

Every temp GIF passes:

- 256×256;
- 6 output frames and 4 unique output-frame hashes;
- exact durations `210,140,140,210,140,140 ms`;
- infinite loop metadata (`loop=0`);
- fully transparent corners and clean chroma despill;
- no crop or green fringe at 256 px or 128 px.

GIF evidence:

- Temporary GIFs: `/tmp/pop-dance-a-independent/gifs/`
- Full 256 px strips: `/tmp/pop-dance-a-independent/contact/gif-full-1.jpg` through `gif-full-6.jpg`
- 128 px strip: `/tmp/pop-dance-a-independent/contact/gif-128.jpg`
- Machine-readable results: `/tmp/pop-dance-a-independent-gif-qa.json`

## Blockers

None.
