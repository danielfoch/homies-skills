# Pop & Dance batch I — reference corrections QA

Date: 2026-07-14  
Scope: 8 corrected loaders, 4 new loaders, and 10 rejected loaders retired.

## Result

**PASS — 12/12 accepted, zero warnings or failures.** Every accepted loader uses one SHA-locked canonical plate plus deterministic connected-part motion. The body anchor, crop, scale, palette, stationary regions, and transparent background remain fixed through the reversible six-frame runtime loop.

## Accepted production artifacts

| Loader | Source SHA-256 | GIF SHA-256 |
|---|---|---|
| `cha-cha-sliding-marketing` | `9f82209e57274ed435260e345be60659369ea4530eaeb5d54bf2f6442ccc8e1e` | `7ded39ff1072437354d1b684b288a75a50b9e180a4a57faa35bfbace52e7bf51` |
| `harlem-shaking-listings` | `dcae5b74e1fde76716840c0637148f0859c48e01d20529ba92a50e23bbb1ac67` | `0ed728cdf6f997429f280cf2c0bd371f58af2e56d44675e77e96d5183913c67f` |
| `umbrella-ing-manager` | `1cb06b7cc5b767c8f185e5ba6b2eeede18810b6b48a66781b6682e6e4fa04976` | `27008816e0cab2e190ccb898c64c3a1173f580bb4a1e8a4eda73578a1948187c` |
| `dougie-ing-content` | `2fd19cfb84a7bcfc8b06a675c1d808d159ba6cc69197f054e00e3bdac37f4b36` | `e697752fe1fe588a938e7e32d1a0aef6a7ba8f9e177288b33e7ed5529fb00667` |
| `disco-inferno-ing-reports` | `53c65c90e6f78fd7d1fbe5e3c58f2165b7a8178a513085602db9f89467ece220` | `34efda5ee99d3f0d35897c1f5f9b3dfb11abe929ef9370cc45ff836ea929d2cf` |
| `rickrolling-manager` | `779049d259e522c9274fc99ef206d0f66e4b2e854f86c2b01fd36192ae58f2b6` | `657d1fcd63fb0118e88e099933c9adb61e4133af7df5a086148d7067697a8465` |
| `ymca-ing-cma` | `490287f88e12bf486dc03b0471e6f7d44f88e08fa46cfde419eb8e6c7da9921f` | `db3a3112990025c4bb3acd002c83e4becf1628d9f5b310e62b004485db24e2dc` |
| `wednesday-ing-offers` | `cd9a11da14ad86e684dd5949421182c218692a736f0764fe58c570b0e8014417` | `649e207e1d565c9b1d83907571750de7aedc13a045fc900696679bcca7bbf3ce` |
| `david-blaining-manager` | `2b910c9ca4c8b91c45a3a0667d534284d42dab7bf295f57efaf1cd62e745446e` | `aeaaba28b2da3c570592ca828375e68b7e1acbf961c4fa96e7eb185a95523dd2` |
| `cranking-that-marketing` | `4d33e26e76d4e34e6317f9d5af735ef21c1534fc0959e9145482ffd88152ec9c` | `b7f1bfcdda93c2990548c7aba3c44995e29a1c248b889a1a7086bb7edfea78b5` |
| `cranking-the-step-marketing` | `66ae82445f37ef02edbdd6a36c1cd33ef33c8d2846ed9157273c185f81276d40` | `79a64b5207cb4f922ad8b1f2d9c663d019db1998bae3ee4c6a1306078efa21ae` |
| `cranking-the-motorbike-marketing` | `de8c01b16070f67ccd247b0ea3919fd151c3e07e6f67e25bbaa57e10e3c59145` | `53da1b2b94980c464e23fbb7a72516abc80e014db792fe3cc1611b29ce0c038f` |

## Retired from the release

`call-me-maybeing-research`, `material-girling-reports`, `fireworking-offers`, `roaring-research`, `flowers-ing-manager`, `levitating-cma`, `dont-start-now-ing-listings`, `good-as-hell-ing-marketing`, `pon-de-replaying-crm`, and `cupid-shuffling-crm` were removed from the manifest, sources, runtime GIFs, and gallery payload.

## Release checks

- Correct 1254×1254 2×2 masters and 256×256 transparent runtime GIFs.
- Four unique cells; runtime sequence `0,1,2,3,2,1` and durations `210,140,140,210,140,140ms`.
- Full-size cells, 128px source contacts, and decoded 128px GIF loops visually inspected.
- No character overlap, scale pumping, ghost hands, crop, redraw debris, palette shimmer, or loop snap.
- Deterministic repeat builds were byte-identical.

Machine-readable policies, reviews, contacts, and reports live under `qa/strict-repairs/pop-dance-reference-rebuilds/`, `qa/strict-repairs/pop-dance-hand-cleanup/`, and `qa/strict-repairs/new-pop-dance-additions/`.
