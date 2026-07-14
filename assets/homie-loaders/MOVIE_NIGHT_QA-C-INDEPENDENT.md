# Movie Night Homies — independent QA C

Result: **PASS — no blockers found**.

Audited source masters:

- `elsa-ing-reports`
- `sonic-ing-crm`
- `deadpooling-marketing`
- `grooting-research`
- `furiosa-ing-manager`
- `m3ganing-listings` (post-repair)
- `paul-atreidesing-cma`
- `elphaba-ing-offers`

## Source-sheet contract

All eight sources are exact `1254x1254` RGB PNGs with four `627x627` authored cells. Every outer edge and both full cell axes are exact `#00ff00`. All four cell hashes are distinct for every asset. Minimum non-key clearance remains above the required 60px in every frame.

| Slug | Source SHA-256 | Minimum L/T/R/B clearance across cells |
|---|---|---|
| elsa-ing-reports | `c299149b1d25f47fda563e00e6268141e8307b617fb1d4d90d2c57de239dc094` | 120 / 81 / 150 / 85 |
| sonic-ing-crm | `ae999ab2bcb4e71e7ad8454fb90a673ee01e11e55abdac78b552948e1fb8f69f` | 235 / 77 / 224 / 86 |
| deadpooling-marketing | `a327e5305f657d628dd66d5e137a14746ab4e6f776a03a26e1a0e70cf145bc84` | 202 / 63 / 204 / 75 |
| grooting-research | `12a24f081019d278f6c909a85f82bb805036f640941bda509c205f8fa0dbe2a3` | 219 / 67 / 232 / 75 |
| furiosa-ing-manager | `ab06810710bcd0290b3722cd51f36ccc131fc42a800c1077663415998dad7e89` | 228 / 71 / 214 / 77 |
| m3ganing-listings | `8deb790e9ac870749e6c843a5c0a7233874319b949dfe39b309accc3a11a20eb` | 249 / 61 / 225 / 87 |
| paul-atreidesing-cma | `8678df7287aadf56acc910b07d1b4a640b8bf29d781ed067c3c49150a92dad10` | 230 / 65 / 198 / 89 |
| elphaba-ing-offers | `29afa2a78f93b6b90135e1935cb9f46d40678ac020289c24123e10bf2591f308` | 261 / 72 / 214 / 70 |

Each cell contains one dominant connected character component. Elsa’s generated snowflake and Elphaba’s generated light orbs are intentionally separate effect components; they remain well inside the cell and do not resemble panel bleed or detached anatomy.

## Continuity and anti-wiggle inspection

Every final sheet and all four authored frames were visually inspected at full source resolution and again in the 128px runtime contact at `/tmp/movie-new-c-independent/contact/final-128.jpg`.

- `elsa-ing-reports`: literal fixed character/gown plate; changes are confined to the snowflake effect at source bbox `x=368..402, y=155..187`.
- `sonic-ing-crm`: fixed head, torso, hands, legs and camera; changes are confined to the tapping shoe/foot at `x=334..403, y=473..540`.
- `deadpooling-marketing`: fixed mask, torso, lower body and feet; changes are confined to the connected waving hand/forearm at `x=202..257, y=104..181`.
- `grooting-research`: fixed tree costume/body; changes are confined to the connected sprout at `x=300..328, y=67..95`.
- `furiosa-ing-manager`: fixed head, torso, organic arm, legs and camera; changes are confined to the connected mechanical forearm/hand at `x=364..413, y=225..360`.
- `m3ganing-listings`: no redraw occurs. Frame 1 is the exact frame-0 plate shifted 3 source pixels left, frame 2 is the exact plate shifted 1 pixel up, and frame 3 is the exact plate shifted 3 pixels right. Inverse translation produces zero differing pixels in every frame. This is a controlled rigid dance step, not global jitter.
- `paul-atreidesing-cma`: fixed body/stillsuit/boots; changes are confined to eyes and connected scarf edge at `x=302..429, y=99..211`.
- `elphaba-ing-offers`: fixed body, face, hat, gown and hand; changes are confined to the orbiting glow at `x=371..403, y=180..203`.

No frame contains a crop, duplicate or missing limb, floating hand/foot, costume replacement, prop switch, changed perspective, or unintentional camera-scale change. All effects and active limbs retain continuity through the reversible sequence.

## Temporary runtime GIF verification

GIFs were assembled independently with `scripts/assemble_sprite.py --no-alignment` into `/tmp/movie-new-c-independent/gifs/`. Every GIF passes the project verifier: transparent `256x256`, six frames, infinite loop, sequence `0,1,2,3,2,1`, durations `210,140,140,210,140,140` ms, four visually distinct authored frames, transparent corners, non-empty subjects, and size below 750 KiB.

| Slug | Bytes | GIF SHA-256 |
|---|---:|---|
| deadpooling-marketing | 57,161 | `0770a82f570242f4afc6099cd7af80950d20a8a80e62f87225d29b610084e87b` |
| elphaba-ing-offers | 46,348 | `70680bcf44367d18eae6a658c8ffd7e7159720b1481703066ab6a96e88913edf` |
| elsa-ing-reports | 75,413 | `2e15835fd771f735c93ee1e65eca78db525c95d0ac5470adbdf753db3a8233bb` |
| furiosa-ing-manager | 53,615 | `5fa3cc0ed9a75f041f57104ef1ba08dd17a98467908cc326aa0645a79ffa9119` |
| grooting-research | 57,848 | `32eda2948d39139b26133cd9182de3c4eee80a4e144603933dbbad6c4625a4a4` |
| m3ganing-listings | 43,327 | `07a17e05ae49533a6f9a5d6352709afac8499b6dd182cac5cb6f8ed57348ffc8` |
| paul-atreidesing-cma | 55,053 | `f592038f8ec4768a37f194ef528876a6588b7b146f022892f4024c944231a812` |
| sonic-ing-crm | 49,101 | `69d1f5b6a1e90f129e5952bbc8eb16f0499565f85ee6323c8a09d873b8370c6a` |

Animated contact: `/tmp/movie-new-c-independent/contact/animated-2x4.gif`.
