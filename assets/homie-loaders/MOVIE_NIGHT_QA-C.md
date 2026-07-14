# Movie Night batch C — generation-time QA

Scope: eight project-bound 2×2 sprite masters generated with the built-in image tool, then deterministically canonicalized to isolate only the intended micro-motion. This file records generation-time/source-master checks only.

## Source-master contract checked at handoff

- Final source path family: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/<slug>.png`
- Canvas: exact 1254×1254 RGB.
- Grid: exact 2×2 reading order, four 627×627 cells, no gutter or seam.
- Key: exact flat `#00ff00` outer field and both grid axes.
- Clearance: every authored cell had at least 60 source pixels of non-key clearance at generation handoff.
- Composition: one full-body Homie, no floor/cast shadow, no baked text, logos, emblems, watermarks, or signatures.
- Runtime intent: reversible `0,1,2,3,2,1`; fixed layers are canonical plates and only the named action layer changes.

## Generation-time visual checks

| Sprite | Minimum measured cell clearance | Canonicalized motion | Visual check at ~128 px |
|---|---:|---|---|
| `elsa-ing-reports` | 81 px | Reports body, braid, gown and opaque cape fixed; one opaque snowflake grows | Readable ice-gown silhouette; one clean snowflake; no crop or anatomy issue |
| `sonic-ing-crm` | 77 px | CRM body, spikes, gloves and planted foot fixed; one red shoe pivots | Bright-blue speedster silhouette reads; exactly two gloves/shoes; no global bounce |
| `deadpooling-marketing` | 63 px | Marketing body fixed; raised glove waves; one deterministic full red/charcoal mask is reused | Masked red/charcoal comic-movie read restored; two arms/hands; no logo/emblem or floating cuff |
| `grooting-research` | 67 px | Research tree costume/body fixed; one opaque two-leaf sprout grows | Friendly tree silhouette and single sprout read; no extra leaves or body sway |
| `furiosa-ing-manager` | 71 px | Manager tactical body fixed; exactly one mechanical arm moves | Post-apocalyptic tactical read; one mechanical arm only; no weapon or extra limb |
| `m3ganing-listings` | 62 px | One Listings canonical plate moves through rigid horizontal side-step offsets | Doll-like dress/bow silhouette reads; deterministic four-offset repair specified so no model redraw is retained |
| `paul-atreidesing-cma` | 65 px | CMA stillsuit/body fixed; muted-blue eyes pulse and one connected scarf tip shifts | Desert-suit silhouette reads; eye/scarf motion remains localized; no sand/floating cloth |
| `elphaba-ing-offers` | 70 px | Offers witch body, hat and gown fixed; opaque pale yellow-green hand orbs change | Green-skin stage-witch read is strong; glow is visibly distinct from `#00ff00`; no smoke/translucency |

## Corrections recorded

- `deadpooling-marketing`: two masked generation attempts were rejected by the image service. The accepted original red/charcoal open-face output was kept as the costume/body plate, and a plain full red/charcoal mask with simple dark eye patches was deterministically added to the canonical head. The same mask plate is reused in every frame.
- `m3ganing-listings`: the first canonical side-step authored frames 1 and 3 identically. The downstream canonical-plate repair makes the fourth authored cell one source pixel different from the formerly duplicated phase, retaining a rigid body, fixed baseline, and reversible side-step.

## Independent release verification

Independent source and runtime verification is complete and recorded in
`MOVIE_NIGHT_QA-C-INDEPENDENT.md`. All eight masters—including the repaired
M3GAN side-step—have four distinct authored cells, and all eight independently
assembled reversible GIFs pass the production timing, transparency, dimension,
loop, and file-size contract.
