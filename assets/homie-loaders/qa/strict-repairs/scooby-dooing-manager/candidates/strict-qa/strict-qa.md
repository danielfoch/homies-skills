# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `scooby-dooing-manager` | PASS | 72px | 6.083px | 14.9889% | 0.0% | recorded: pass |

## scooby-dooing-manager — PASS

Concept: Exactly one frightened male Manager Homie holds exactly one frightened large brown spotted dog with a blue collar and blank green diamond tag.

Required action: The immutable connected Manager-and-dog rig performs a controlled shared side-to-side shake; both identities, all anatomy, the collar/tag, crop, scale, and relative pose remain locked.

Full-size contact: `assets/homie-loaders/qa/strict-repairs/scooby-dooing-manager/candidates/strict-qa/contacts/scooby-dooing-manager-source-full.png`

128px contact: `assets/homie-loaders/qa/strict-repairs/scooby-dooing-manager/candidates/strict-qa/contacts/scooby-dooing-manager-source-128.png`

GIF contact: `assets/homie-loaders/qa/strict-repairs/scooby-dooing-manager/candidates/strict-qa/contacts/scooby-dooing-manager-gif-128.png`

Failures: none

Warnings: none

Manual notes: Inspected the full-size four-cell contact, 128px four-cell contact, and six-phase GIF contact. Exactly two subjects remain present; the male Manager has two connected hands, the dog has one head/body/tail and four readable paws, and the blue collar with blank green diamond tag remains fixed. The whole pair translates together with no redraw, scale pulse, crop, detached pixels, text, glyphs, or debris.

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
