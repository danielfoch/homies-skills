# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `elle-woodsing-reports` | PASS | 64px | 4.789px | 0.3955% | 0.8631% | recorded: pass |

## elle-woodsing-reports — PASS

Concept: A clearly female Homie in a hot-pink suit and sunglasses holds a coordinated handbag and a small sweater-wearing chihuahua.

Required action: The chihuahua's connected outer forepaw makes a compact friendly wave while the woman, sunglasses, ponytail, hot-pink suit, handbag, holding arm, dog body, legs and feet remain fixed.

Full-size contact: `/tmp/elle-woodsing-paw-v1/strict-policy/contacts/elle-woodsing-reports-source-full.png`

128px contact: `/tmp/elle-woodsing-paw-v1/strict-policy/contacts/elle-woodsing-reports-source-128.png`

GIF contact: `/tmp/elle-woodsing-paw-v1/strict-policy/contacts/elle-woodsing-reports-gif-128.png`

Failures: none

Warnings: none

Manual notes: Full-size, 128px, and magnified paw contacts inspected. The character unmistakably reads as an adult woman with a feminine face/body, blonde high ponytail, hot-pink sunglasses, tailored pink blazer and pencil skirt, pink heels, coordinated handbag, and exactly one tan chihuahua in a purple-and-pink sweater. One canonical plate is reused exactly. Only the dog's connected outer forepaw rotates around its wrist; the woman, bag, holding hand, dog head/body, suit, legs, and feet are pixel-identical. No seams, ghosts, debris, crop, extra anatomy, palette shimmer, or whole-body jiggle.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 64px | 42894px | 1 (1/0) | none |
| 1 | 64px | 42904px | 1 (1/0) | none |
| 2 | 64px | 42869px | 1 (1/0) | none |
| 3 | 64px | 42802px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.3955% | 4.189px | 0.031px | 0.0px | 0.8631% | 1.0 |
| 1→2 | 0.3096% | 4.472px | 0.103px | 0.0px | 0.8381% | 1.0 |
| 2→3 | 0.2541% | 4.789px | 0.194px | 0.0px | 0.8417% | 1.0 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| female-homie-face-ponytail-suit-handbag-left-core | 0.0% | 0.0% |
| fixed-lower-body-handbag-dog-body-legs-feet | 0.0% | 0.0% |
