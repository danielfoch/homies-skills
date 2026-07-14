# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `gatsbying-manager` | PASS | 86px | 3.162px | 1.0845% | 5.2292% | recorded: pass |

## gatsbying-manager — PASS

Concept: Canonical Manager Homie holds one continuous champagne toast while a single locked arm-and-glass rig makes a restrained reversible lift.

Required action: At full size and 128px, read one coherent coupe toast with one stable glass, hand, face, tuxedo, crop, and scale.

Full-size contact: `assets/homie-loaders/qa/strict-repairs/gatsbying-manager/report-independent/contacts/gatsbying-manager-source-full.png`

128px contact: `assets/homie-loaders/qa/strict-repairs/gatsbying-manager/report-independent/contacts/gatsbying-manager-source-128.png`

GIF contact: `assets/homie-loaders/qa/strict-repairs/gatsbying-manager/report-independent/contacts/gatsbying-manager-gif-128.png`

Failures: none

Warnings: none

Manual notes: Independent review of the 1254px source contact, all four full-size cells, all four 128px cells, and the decoded six-frame 128px GIF contact. One champagne coupe remains continuously attached to the same anatomically coherent hand while the single arm/glass rig makes a restrained reversible toast. The male Manager face, tuxedo, bow tie, torso, crop, and scale are locked. No duplicate prop, grip break, detached fragment, redraw drift, crop fault, or green debris is visible.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 86px | 84611px | 1 (1/0) | none |
| 1 | 86px | 84676px | 1 (1/0) | none |
| 2 | 86px | 84805px | 1 (1/0) | none |
| 3 | 86px | 84951px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 1.0845% | 3.162px | 0.056px | 0.0px | 5.0831% | 0.966 |
| 1→2 | 1.0646% | 3.162px | 0.193px | 0.0px | 5.2292% | 0.9657 |
| 2→3 | 1.0268% | 3.162px | 0.168px | 0.0px | 5.2276% | 0.9649 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| locked-face | 0.0% | 0.1% |
| locked-tuxedo-core | 0.0% | 0.1% |
