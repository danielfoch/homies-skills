# Pop & Dance batch B — independent read-only QA

> Historical generation/structural record. The final motion-semantic authority is `POP_DANCE_QA-SEMANTIC-REBUILD-2026-07-12.md`.


Auditor: `/root/pop_dance_c`  
Status: **PASS — 13/13; no production blocker found**  
Mutation policy: all batch-B masters, GIFs, alignment data, and contacts were inspected read-only. No batch-B file was changed.

## Independent checks performed

- Re-opened each project master directly from `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/`.
- Re-opened each temp GIF directly from `/tmp/pop-dance-b/gifs/`.
- Independently recomputed master dimensions/mode, exact-key outer edges and two-pixel center axes, cell hashes, subject margins, file hashes, GIF frame hashes, timing, loop metadata, transparency index, transparent corners, and canvas size.
- Visually inspected all 52 authored cells in `/tmp/pop-dance-b/contact/contact-source-256.jpg`.
- Visually inspected all six playback phases at 128 px in `/tmp/pop-dance-b/contact/contact-128.jpg` and at 256 px in `/tmp/pop-dance-b/contact/gif-full-batch-1.jpg` through `gif-full-batch-5.jpg`.

## Results

Every master independently passed: 1254×1254 RGB, exact #00ff00 on all outer edges and both center-axis pixels, four byte-distinct authored cells, and at least 60 px clearance. Every GIF independently passed: 256×256, six frames, four distinct visual phases, infinite loop, exact 210/140/140/210/140/140 ms timing, valid transparency index, and fully transparent corners.

| Asset | Source SHA-256 | GIF SHA-256 | Min margin | Visual result |
|---|---|---|---:|---|
| oops-i-did-it-again-ing-offers | `e92a64a53608c3812bd6659e6fbf1d47b86c3ae6686be649b56bd7e8cb50cc6d` | `426fb464cdc9336b04bb3eddbb02deff578640915fa0f3d57caef6668c7cb085` | 68px | PASS |
| hit-me-baby-one-more-timing-research | `d364cbbe133594c74b3c22a6935b9b30624792768b910f0c00b3f8941727794c` | `ff8d25b0123a980cae421647bd15d3a2e1ef59a281023b9b14f0bc94df4e4dd9` | 66px | PASS |
| voguing-reports | `0f475e0f6ed681721f92f902413c39ec13ba6375907995a78f15f80b18759bcb` | `7544da39382c5e672ec6e59c71c5091ffe6ee300b399a4ab54e42af41c588515` | 68px | PASS |
| material-girling-reports | `9cc16463090d8d24d97f17a9123fc11665a73e70a30fc75b155093a76d2d0a39` | `7e3c5350546246af8eae365956b6534c7f7196f8a51ac2984335516a784d3e1a` | 68px | PASS |
| fireworking-offers | `7cabccc73f4f991a2691899d0c67c497a71ec55717ffa4d9f1403195b5444e85` | `b756b19a22a3749546b6ce61950b5667dfe7cbd41cf5492d85b99d08bff7c3d9` | 68px | PASS |
| roaring-research | `ab5607ad304225ca4e6a31b71a419cbca3468312a0d0ac5d124eefaee71b87cc` | `63ab1246f1a6c9aaa24cfadd352307eba094b1ccd0da76d2ebd43a08531899e7` | 67px | PASS |
| flowers-ing-manager | `8dfdb4505dbbe79f6374eaa1c2982f4dc3837003eb3e863840e0098557943844` | `7a2123682b261403b1754a463f315286a366280ab878c56e46588a6de7c4a111` | 67px | PASS |
| espresso-ing-content | `2df28d4fe4882de6e03c376c4fb63ae64718b8cc60819344f177d3d1b396ed94` | `3950e7ac8eeca3d497b0412c4855b975d278c386fb1474c3b8ecd1a52d280a40` | 67px | PASS |
| good-as-hell-ing-marketing | `77aaec0ed6643072e7a72d72b5bfbb243b290818283e5a1fd4901921d1f06a8f` | `0b5c6ef971c9c3f09859ad52ca5bdd3dfab4bdefe6ddb7063dce3213fcf5e94a` | 66px | PASS |
| levitating-cma | `09a01c2199335836a30fcd0355aa5861ca3ff78cb01a5f7e9429f83f45568c5d` | `5b3bfc0753d2d44fdc2e793c15cf75c961512393f8fcb6e54aa700a83b340a75` | 63px | PASS |
| dont-start-now-ing-listings | `46575860cdae83cc8cc018d599d6ea180cd3d919927abe37c725ce09a0f1ce66` | `abd1af16e1bc94fb2913b763d0c53312c875070a1ed223d0ce1eacc87b94af0e` | 67px | PASS |
| umbrella-ing-manager | `29074c032de073f1e896d86cfc09d7e44e93305545f60ea3a25a48ddeefd8bf1` | `c63ec125a466b886e1ec848754bd8670f3315698f68ab1488a85f19b53e2b0a6` | 67px | PASS |
| pon-de-replaying-crm | `f5addac9a0e33f93235f0fc2cc4b4b8d75acccf2fea35d766f7d92446c1993aa` | `9209de402327d0c617ba14a88cb730edd1035bd221915b5270f5b90cb3b0e9ff` | 68px | PASS |

## Visual continuity findings

The frame strips show one stable Homie identity, fixed costume continuity, and no model-redraw wiggle. The movement is intentionally compact at loader size. I found no crop, extra limb, detached hand, character substitution, disappearing item, top/bottom wrap, center-axis intrusion, green fringe, readable logo, or text artifact.

The localized glint/star phases in `material-girling-reports` and `fireworking-offers` remain inside the safe margins and do not read as stray anatomy. The smallest clearance is 63 px on `levitating-cma`, still above the 60 px requirement.

## Blockers

None. The 13 batch-B assets are safe to merge into the production alignment/manifest/GIF build as delivered.
