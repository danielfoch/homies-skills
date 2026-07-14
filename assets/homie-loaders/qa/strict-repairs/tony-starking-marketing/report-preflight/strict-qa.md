# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `tony-starking-marketing` | FAIL | 70px | 2.236px | 0.0879% | 3.3593% | pending |

## tony-starking-marketing — FAIL

Concept: (not supplied)

Required action: (not supplied)

Full-size contact: `qa/strict-repairs/tony-starking-marketing/report-preflight/contacts/tony-starking-marketing-source-full.png`

128px contact: `qa/strict-repairs/tony-starking-marketing/report-preflight/contacts/tony-starking-marketing-source-128.png`

GIF contact: `qa/strict-repairs/tony-starking-marketing/report-preflight/contacts/tony-starking-marketing-gif-128.png`

Failures: `VISUAL_REVIEW_REQUIRED`

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: (none)

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 70px | 47719px | 1 (1/0) | none |
| 1 | 70px | 47744px | 1 (1/0) | none |
| 2 | 70px | 47766px | 1 (1/0) | none |
| 3 | 70px | 47808px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.0524% | 2.189px | 0.085px | 0.0px | 2.2788% | 0.9932 |
| 1→2 | 0.0461% | 2.236px | 0.077px | 0.0px | 2.8975% | 0.9879 |
| 2→3 | 0.0879% | 2.236px | 0.149px | 0.0px | 3.3593% | 0.9883 |
