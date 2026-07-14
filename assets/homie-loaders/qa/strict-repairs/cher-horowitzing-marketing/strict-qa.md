# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `cher-horowitzing-marketing` | PASS | 65px | 5.069px | 0.307% | 1.4326% | recorded: pass |

## cher-horowitzing-marketing — PASS

Concept: A clearly female Homie in the iconic yellow-plaid 1990s fashion look checks a blank flip phone.

Required action: The connected upper lid of one blank flip phone opens as its empty display wakes; the woman's face, hair, body, plaid outfit, hands, lower phone, legs and feet remain fixed.

Full-size contact: `/tmp/cher-horowitz-female-v3/strict-policy/contacts/cher-horowitzing-marketing-source-full.png`

128px contact: `/tmp/cher-horowitz-female-v3/strict-policy/contacts/cher-horowitzing-marketing-source-128.png`

GIF contact: `/tmp/cher-horowitz-female-v3/strict-policy/contacts/cher-horowitzing-marketing-gif-128.png`

Failures: none

Warnings: none

Manual notes: Full-size, 128px, and magnified phone contacts inspected. The character is unmistakably an adult woman with a feminine face and body, shoulder-length blonde hair, no facial hair, yellow-and-black plaid blazer and skirt, white knee socks, and black loafers. One canonical plate is reused exactly. The face, hair, torso, plaid pattern, hands, lower phone, legs and feet are pixel-identical; only the connected upper lid and its blank screen change. No seams, ghosts, debris, crop, extra anatomy, palette shimmer, or whole-body jiggle.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 41145px | 1 (1/0) | none |
| 1 | 65px | 41247px | 1 (1/0) | none |
| 2 | 65px | 41354px | 1 (1/0) | none |
| 3 | 65px | 41454px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.2957% | 5.0px | 0.461px | 0.0px | 1.0544% | 1.0 |
| 1→2 | 0.307% | 5.069px | 0.492px | 0.0px | 1.2475% | 1.0 |
| 2→3 | 0.2894% | 5.0px | 0.473px | 0.0px | 1.4326% | 1.0 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| female-face-hair-torso-plaid-hip-hand-right-side | 0.0% | 0.0% |
| fixed-body-legs-feet | 0.0% | 0.0% |
