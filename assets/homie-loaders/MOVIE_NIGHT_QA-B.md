# Movie Night Homies — QA B

Result: **PASS — 9/9 selected masters and 9/9 runtime GIFs**.

Visual inspection artifacts:

- Four authored frames at 128px: `/tmp/movie-new-b/contact/final-128.jpg`
- Animated 2x4 runtime contact: `/tmp/movie-new-b/contact/animated-2x4.gif`
- Per-frame off-white inspection renders: `/tmp/movie-new-b/qa/<slug>-frame-{0..3}.jpg`

## Source-master contract

Every final source is an RGB `1254x1254` PNG, split into four exact `627x627` cells in reading order. Every outer-edge pixel and both full cell axes are exact `#00ff00`. No gutter, white separator, cast/contact shadow, floor, gradient, readable text, logo, emblem, watermark, or crop was found. The minimum non-key clearance is at least 65px in every authored cell (required: 60px).

| Slug | Final source SHA-256 | Minimum L/T/R/B clearance over four cells |
|---|---|---|
| ghostbustering-reports | `f0b0b86b4dfa2a42b3e4b7f1a8044f485fa9cd82c5c5a885c3c3f6a699638d46` | 221 / 72 / 242 / 90 |
| gizmo-ing-crm | `c097af6eb555945f9f3e7859d314600c6c5bddc9dcade84799ce5d9ceea87ac9` | 159 / 68 / 139 / 67 |
| mrs-doubtfiring-content | `4aa56b8ff43de86e7e80a58f1c4b3a6b56b19b2ec0d59e9486daba881cd2178f` | 202 / 68 / 239 / 84 |
| mask-ing-marketing | `f2ca0035676631f89c7dd57415a929f8279cb5fa43b021b9cab650cf4b5f3f33` | 220 / 69 / 223 / 85 |
| cher-horowitzing-marketing | `37a5dec275eeb52b8ff154332ac6745a14f9da681f7998dbf36692222c34add7` | 222 / 65 / 222 / 65 |
| elle-woodsing-reports | `f92d7d99e097d674824257f9ac694068ac58656b6b2598e5aa0906e2fb7b8622` | 224 / 64 / 225 / 64 |
| edward-scissorhanding-offers | `fae3ee89edf6d9fa88f508fd03fa06f1bdc953a536b00b1892a44f33e853c9f3` | 149 / 70 / 155 / 78 |
| golluming-crm | `9f44be979de9570c5e6d8a19edc64baec33a2b16b8f8c965951413238ae5bf9e` | 259 / 89 / 197 / 91 |
| iron-manning-reports | `2adf2346059383d9adae09d26379857816a8a42a9363a7d4f4bf483612279b48` | 236 / 65 / 241 / 102 |

The apparent extra connected-component specks from antialiased chroma extraction are all under 56 source pixels; each cell has exactly one component of at least 100 pixels, and the dominant component contains more than 99.7% of all non-key pixels. No detached prop, hair fragment, limb, or cropped panel bleed remains.

## Anti-wiggle / canonical-layer audit

- `ghostbustering-reports`: literal canonical lower body and legs in all four cells; frames 1–3 share one raised-goggles/connected-hand plate; only that intended pose transition and the shoulder-light fill vary. Fixed lower-core hash in all four cells: `ff2acb0921a694590a4400bc9a9603027fa6f44c5a66678fff9370c31eb0df07`.
- `gizmo-ing-crm`: one literal canonical body/hood/costume plate; only the same two ears translate upward and the two eyelids change. Fixed-core hash: `0aaa8c6a8047312d612f42fbb80c029d2b89d60a9d2e18738a86a4b3226555b8`.
- `mrs-doubtfiring-content`: one literal canonical head, glasses, cardigan, floral blouse, pearls, skirt, legs, and shoes; one connected arm/hand plate rotates around a fixed shoulder pivot. Fixed-core hash: `cca400f0c323fea71377e071b07979deda71b877ea0a016d4ca049da1e5a6027`.
- `mask-ing-marketing`: the entire character is a literal canonical plate; only two small additive eyebrow arcs vary. Fixed-core hash: `3a231d0d12e198a3fd0a47b0df7d062ee612eb094a3fb3baa5e7c8f5d5a9de66`.
- `cher-horowitzing-marketing`: corrected from the rejected bearded male source to one unmistakably adult female canonical plate with a feminine face/body, shoulder-length blonde hair, yellow-and-black plaid blazer/skirt, white knee socks, and black loafers. Only the connected upper lid of one blank flip phone opens and its blank display wakes; her face, hair, torso, plaid pattern, hands, lower phone, legs, and feet remain pixel-identical. One shared GIF palette eliminates fixed-character colour shimmer. Strict evidence: `qa/strict-repairs/cher-horowitzing-marketing/`.
- `elle-woodsing-reports`: one unmistakably adult female Reports Homie plate with a blonde high ponytail, hot-pink sunglasses, tailored pink blazer/skirt, pink heels, coordinated handbag, and exactly one tan chihuahua in a purple-and-pink sweater. Only the dog's connected outer forepaw rotates around one wrist; the woman, bag, holding hand, dog head/body, suit, legs and feet remain pixel-identical. One shared GIF palette eliminates fixed-subject colour shimmer. Strict evidence: `qa/strict-repairs/elle-woodsing-reports/`.
- `edward-scissorhanding-offers`: one literal canonical centre/lower plate; only the connected arms and two fixed blunt scissor-glove silhouettes come from the registered motion cells. No blade touches the body. Fixed lower-core hash: `0bef93b6aed6b2dfd87a8eeadcf88c87ede7f4dd4fc1b2fc766947fab696887e`.
- `golluming-crm`: every frame derives from one canonical character plate; deterministic rigid transforms only: rotations `-1.10°, -0.35°, +0.45°, +1.15°` around the same foot pivot with x translations `-3, -1, +2, +5` source pixels. There is no redraw or anatomy change.
- `iron-manning-reports`: the entire original exosuit/face/body plate is literal canonical pixels; only one circular chest light and three tiny collar lights change opaque fill. Fixed-core hash: `7123594b5eff21debb2f48475564d3ece4737689391a1b44ee67aefbdc4974de`.

Visual inspection confirmed exactly one Homie per cell, no extra/missing hands or feet, no floating hand/phone/scissor fragments, no costume/prop switching, and no camera-scale drift. The improved broad-ear creature, clearly female yellow-plaid/flip-phone silhouette, pink-suited woman/chihuahua silhouette, compact goggles/backpack/light silhouette, and wiry huge-eyed cave-creature silhouette all remain legible in the 128px contact.

## Temporary GIF contract

All GIFs are transparent `256x256`, 6 frames, infinite loop, reversible sequence `0,1,2,3,2,1`, durations `210,140,140,210,140,140` ms, four distinct authored frames, transparent corners, and under 750 KiB.

| Slug | Bytes | GIF SHA-256 |
|---|---:|---|
| cher-horowitzing-marketing | 41,492 | `36bc53cca6ecb6bc20fda32cd427bc6b45bf6ccf495f9c0ebc7514051eb2344f` |
| elle-woodsing-reports | 45,589 | `8d8be2ccb4967f22afe71b475127572101ff52cdc6f31025471f34ba73c179a8` |
| edward-scissorhanding-offers | 51,856 | `1eb8766f5483efdba86144ee8ef8f3d03ae3a2e35d47fb26e355744a628d7338` |
| ghostbustering-reports | 47,988 | `c384e59e865c3037d5f3e67334f77d5090ee9e6ac83507c0e446aa357a055d6f` |
| gizmo-ing-crm | 63,347 | `725dbaf33ddb5add41ce42b6e5cc7656b0fe73d51bf90cf9fdbd7c87da2f944b` |
| golluming-crm | 45,713 | `66f3b3584bedb7c4ee2c661fd2f9a8dcd55c5c12c2ac02a14fed47d251a6c2dc` |
| iron-manning-reports | 41,641 | `f6c813bf56486a852f9b1f72b39c4ecfae06f71d470010862ead0e942a5189e1` |
| mask-ing-marketing | 60,015 | `47bf794a0b286c4d384f9afca1b71389346a2ca0d998df43717b16841d043c5c` |
| mrs-doubtfiring-content | 48,247 | `3e982e4bcfd201c739de272ddc82e001543a2e597e353c4cdfd0eac0637229b4` |

Alignment handoff: `/tmp/movie-new-b-alignment.json` contains four empty production transforms per asset because the canonicalized masters already carry the final registration.
