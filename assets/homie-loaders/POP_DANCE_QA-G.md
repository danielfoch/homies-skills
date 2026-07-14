# Pop & Dance batch G — Smooth-Crimining QA

Date: 2026-07-13  
Scope: `smooth-crimining-marketing`

## Result

**PASS — 1/1.** The gravity-defying lean is readable at 128px, all four authored
phases retain one connected Marketing Homie, and the reversible six-frame loop
has no crop, debris, independent redraw wiggle, palette shimmer, or loop snap.

## Accepted artifacts

| Artifact | SHA-256 |
|---|---|
| Generated plate | `07decf70b68b2329be55962c20143e6a49d6e72694d33f6ec40c2fdd2b65ca03` |
| 1254×1254 source master | `6691c4b5889cd14c6ad1bbfcf7d3074387f55d4ac3dd9a24b088ad244b4fac32` |
| 256×256 transparent GIF | `e32192594d7722e18151d1c8e7e91c05e8196a82b7f55de45be25d82b9ef2c38` |

## Release checks

- Four unique 2×2 source cells; runtime sequence `0,1,2,3,2,1` with durations
  `210,140,140,210,140,140ms`.
- One SHA-locked character plate and one deterministic transform path; no
  independently redrawn frames.
- Shoes, socks, ankle cuffs, soles, and contact pixels are identical in every
  phase while the connected body deepens through the lean.
- Exactly one significant connected component at alpha thresholds
  `1/8/16/32/48/64/96/128`; no visible satellite fragments.
- Same face, fedora, armband, suit pinstripes, anatomy, scale, camera, shared
  crop, bottom anchor, and palette throughout.
- All four 627px cells, the 128px contact sheet, and the decoded GIF loop were
  visually inspected and accepted.

Machine-readable policy and visual-review evidence live in
`qa/strict-repairs/smooth-crimining-marketing/`.
