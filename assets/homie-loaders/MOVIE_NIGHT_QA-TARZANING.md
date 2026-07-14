# Movie Night QA — Tarzaning

Date: 2026-07-14  
Asset: `tarzaning-manager`

## Root QA result

PASS. One accepted male Manager plate supplies every face, hand, torso, wrap,
leg and foot pixel. One continuous deterministic vine is fused behind that
plate, and the intact rig rotates around one fixed overhead knot. There is no
independent frame generation, per-frame crop, rescale or character redraw.

| Check | Result |
|---|---|
| Source master | 1254×1254 RGB with exact `#00ff00` outer edges and gutters |
| Authored cells | 4 distinct phases, one connected foreground component, 62px minimum margin |
| Motion | `-9° → -3° → 3° → 9°`, 81.41px horizontal centroid span |
| Foreground continuity | 0.1467% area span; zero tiny components |
| Fixed pivot | 0.0% change in the annotated overhead knot core |
| Production GIF | 256×256, 6 frames, 4 unique phases, transparent corners |
| Playback | `0 → 1 → 2 → 3 → 2 → 1`, 210/140/140/210/140/140ms, loop forever |
| Source SHA-256 | `d6e7ed933ce01da07e22c4849557af9278dde2a26a1ba0e8db497c5de6edadb2` |
| GIF SHA-256 | `c2cc058d3577f27a64feca83bad642798b895e059962f38c6b1836c4c80b3f3f` |

Full-size, 128px and decoded GIF review confirms one canonical adult male
Manager, exactly two connected hands and arms, two legs and feet, one securely
covered brown jungle wrap, one uninterrupted vine and a readable pendulum arc.
No crop, debris, duplicate anatomy, palette shimmer or redraw wiggle is present.

