# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `tyler-durdening-listings` | PASS | 70px | 24.252px | 2.7695% | 6.4518% | recorded: pass |

## tyler-durdening-listings — PASS

Concept: Canonical Listings Homie in red leather performs controlled shadow boxing

Required action: Exactly two fists remain visible in every phase while the left jab retracts to guard and the right jab extends with only attached tapered motion marks; face, torso, pelvis, legs, crop, anchor, and scale remain fixed.

Full-size contact: `assets/homie-loaders/qa/strict-repairs/tyler-durdening-listings/report-independent/contacts/tyler-durdening-listings-source-full.png`

128px contact: `assets/homie-loaders/qa/strict-repairs/tyler-durdening-listings/report-independent/contacts/tyler-durdening-listings-source-128.png`

GIF contact: `assets/homie-loaders/qa/strict-repairs/tyler-durdening-listings/report-independent/contacts/tyler-durdening-listings-gif-128.png`

Failures: none

Warnings: none

Manual notes: PASS after an independent re-audit of the corrected candidate. I inspected the full 1254px source contact, all four original 627px cells, every 128px cell, and all six decoded GIF phases. Every phase contains exactly two fists: left jab plus right guard, partial left retraction plus right guard, two-fist guard, then left guard plus right jab. Both extended fists remain continuously attached to their authored forearms and sleeves. The original guard-fist regions retain zero skin pixels after the one-time erase, so no third fist, residual arm, or rod remains. The restrained tapered motion marks sit behind the moving fist and do not read as detached anatomy or a rod at full size or 128px. Direct frame-to-immutable-plate comparison finds zero changed pixels outside the saved two-forearm mask. Face, torso core, pelvis, legs, shoes, crop, anchor, and scale remain byte-locked. No visible crop fault, green debris, redraw drift, or disconnected anatomy is present.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 70px | 43633px | 2 (1/1) | none |
| 1 | 70px | 44351px | 1 (1/0) | none |
| 2 | 70px | 44484px | 1 (1/0) | none |
| 3 | 70px | 43252px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 1.7485% | 12.042px | 2.387px | 0.0px | 5.3064% | 0.9116 |
| 1→2 | 2.6196% | 11.0px | 0.667px | 0.0px | 4.2971% | 0.9946 |
| 2→3 | 2.7695% | 24.252px | 4.194px | 0.0px | 6.4518% | 0.9088 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| locked face | 0.0% | 0.0% |
| locked torso core | 0.0% | 0.0% |
| locked pelvis legs and shoes | 0.0% | 0.0% |
