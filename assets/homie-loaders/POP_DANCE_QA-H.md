# Pop & Dance batch H — Checking the Backstreets QA

Date: 2026-07-13  
Scope: `checking-the-backstreets-marketing`

## Result

**PASS — 1/1.** The opposing open-hand arm hits read clearly at 128px, both
connected arms retain natural hands, and the reversible six-frame loop has no
crop, debris, independent redraw wiggle, palette shimmer, or loop snap.

## Accepted artifacts

| Artifact | SHA-256 |
|---|---|
| Generated plate | `614455b15d080aa0b224d3af3226910a5c24e52ac5454df71372a59593b61e40` |
| 1254×1254 source master | `8201f41877784d754c90b64d2f1fd21aca04ceab720e97ac16884ea0bf9e9fe1` |
| 256×256 transparent GIF | `f9fea6ce09854f4723c515d6b15a4fab89de6f4b4ca1f7bf9624bfd05aa24387` |

## Release checks

- Four unique 2×2 source cells; runtime sequence `0,1,2,3,2,1` with durations
  `210,140,140,210,140,140ms`.
- One SHA-locked character plate and one deterministic two-arm rig; no
  independently redrawn frames.
- Wide-brim hat, aviators, face, beard, bomber core, long white shirt, hips,
  ripped jeans, legs, and planted boots remain pixel-identical.
- Both complete connected sleeve-forearm-hand units counter-sweep around fixed
  shoulders with exactly one natural hand per arm and no visible seam.
- Exactly one significant connected component at alpha thresholds
  `1/8/16/32/48/64/96/128`; no visible satellite fragments.
- All four 627px cells, the 128px source contact, and the decoded GIF loop were
  visually inspected and accepted.

Machine-readable policy and visual-review evidence live in
`qa/strict-repairs/checking-the-backstreets-marketing/`.
