# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `buffying-offers` | PASS | 71px | 10.44px | 31.5631% | 41.8768% | recorded: pass |

## buffying-offers — PASS

Concept: Exactly one female Offers Homie in a simple black outfit holds exactly one wooden stake in a ready hunter stance.

Required action: The immutable female Offers identity, anatomy, empty second hand, black outfit, and single wooden stake remain one rigid rig through a boot-anchored guarded lean.

Full-size contact: `assets/homie-loaders/qa/strict-repairs/buffying-offers/candidates/strict-qa/contacts/buffying-offers-source-full.png`

128px contact: `assets/homie-loaders/qa/strict-repairs/buffying-offers/candidates/strict-qa/contacts/buffying-offers-source-128.png`

GIF contact: `assets/homie-loaders/qa/strict-repairs/buffying-offers/candidates/strict-qa/contacts/buffying-offers-gif-128.png`

Failures: none

Warnings: none

Manual notes: Inspected the full-size four-cell contact, 128px four-cell contact, and six-phase GIF contact. Exactly one female Offers subject, exactly one wooden stake, one empty open second hand, two arms, and two legs remain continuous and readable. The intentional rigid lean reverses cleanly with no redraw, prop duplication, scale pulse, crop, text, glyphs, or debris.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 74px | 36703px | 1 (1/0) | none |
| 1 | 74px | 36747px | 1 (1/0) | none |
| 2 | 74px | 36734px | 1 (1/0) | none |
| 3 | 71px | 36723px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 31.5096% | 10.44px | 8.511px | 7.616px | 41.8405% | 0.6835 |
| 1→2 | 30.388% | 10.0px | 8.036px | 7.28px | 40.8303% | 0.7196 |
| 2→3 | 31.5631% | 10.44px | 8.578px | 7.616px | 41.8768% | 0.6938 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| empty-transparent-canvas-corner | 0.0% | 0.0% |
