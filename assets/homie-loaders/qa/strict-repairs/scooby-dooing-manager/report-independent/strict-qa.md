# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `scooby-dooing-manager` | PASS | 72px | 6.083px | 14.9889% | 0.0% | recorded: pass |

## scooby-dooing-manager — PASS

Concept: Exactly one frightened male Manager Homie holds exactly one frightened large brown spotted dog with a blue collar and blank green diamond tag.

Required action: The immutable connected Manager-and-dog rig performs a controlled shared side-to-side shake; both identities, all anatomy, the collar/tag, crop, scale, and relative pose remain locked.

Full-size contact: `assets/homie-loaders/qa/strict-repairs/scooby-dooing-manager/report-independent/contacts/scooby-dooing-manager-source-full.png`

128px contact: `assets/homie-loaders/qa/strict-repairs/scooby-dooing-manager/report-independent/contacts/scooby-dooing-manager-source-128.png`

GIF contact: `assets/homie-loaders/qa/strict-repairs/scooby-dooing-manager/report-independent/contacts/scooby-dooing-manager-gif-128.png`

Failures: none

Warnings: none

Manual notes: Independent inspection of every full-size cell, every 128px cell, and all six decoded GIF phases confirms exactly one frightened adult male Manager and one frightened large brown spotted dog. The Manager has two connected arms and hands; the dog has one head, one body, one tail, four readable paws, one blue collar, and one blank green diamond tag. The shared shake reads at 128px and preserves the connected pair byte-identically apart from whole-rig translation, with no redraw, crop, scale jump, text, debris, or extra subject.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 74px | 57285px | 1 (1/0) | none |
| 1 | 72px | 57285px | 1 (1/0) | none |
| 2 | 73px | 57285px | 1 (1/0) | none |
| 3 | 74px | 57285px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 13.9554% | 6.0px | 6.325px | 6.325px | 0.0% | 1.0 |
| 1→2 | 14.9889% | 6.083px | 7.211px | 7.211px | 0.0% | 1.0 |
| 2→3 | 13.9554% | 6.0px | 6.325px | 6.325px | 0.0% | 1.0 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| empty-transparent-canvas-corner | 0.0% | 0.0% |
