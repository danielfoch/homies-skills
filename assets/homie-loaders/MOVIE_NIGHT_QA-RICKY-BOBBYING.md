# Movie Night QA — Ricky-Bobbying

Date: 2026-07-14  
Asset: `ricky-bobbying-manager`

## Root QA result

PASS. One accepted Manager plate supplies the face, cap, racing suit, two
connected hands and silver trophy in every authored cell. The subject alpha,
crop, scale, anchor and checkered finish rail remain locked while only a small
highlight travels across the trophy cup.

| Check | Result |
|---|---|
| Source master | 1254×1254 RGB with exact `#00ff00` outer edges and gutters |
| Authored cells | 4 distinct phases, one connected foreground component, 60px minimum margin |
| Registration | 0.0px maximum global shift |
| Stationary regions | 0.0% change across Manager, hands, suit, trophy base and finish rail |
| Production GIF | 256×256, 6 frames, 4 unique phases, transparent corners |
| Playback | `0 → 1 → 2 → 3 → 2 → 1`, 210/140/140/210/140/140ms, loop forever |
| Source SHA-256 | `b1bb23d5bffba5cfe01a2dfbc3270c693aab2a17481c88baad20ab4fc667fc9d` |
| GIF SHA-256 | `b53b43d1ef074de525ed74644a93c7ab760b740b2ae3593e3d3e63f7039b51d9` |

Full-size and 128px review confirms the cream/blue/coral Homies racing livery
contains only simple house-H crests and circular accents—no Wonder Bread marks,
real sponsor branding, random text or logos. The fixed checkered rail conceals
the source illustration's thigh-up boundary consistently in all phases.
