# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `tyler-durdening-listings` | FAIL | 70px | 26.173px | 5.6323% | 7.0442% | pending |

## tyler-durdening-listings — FAIL

Concept: (not supplied)

Required action: (not supplied)

Full-size contact: `qa/strict-repairs/tyler-durdening-listings/report-preflight/contacts/tyler-durdening-listings-source-full.png`

128px contact: `qa/strict-repairs/tyler-durdening-listings/report-preflight/contacts/tyler-durdening-listings-source-128.png`

GIF contact: `qa/strict-repairs/tyler-durdening-listings/report-preflight/contacts/tyler-durdening-listings-gif-128.png`

Failures: `VISUAL_REVIEW_REQUIRED`

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: (none)

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 70px | 44589px | 1 (1/0) | none |
| 1 | 70px | 44540px | 1 (1/0) | none |
| 2 | 70px | 44487px | 1 (1/0) | none |
| 3 | 70px | 44582px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 3.9138% | 12.665px | 0.567px | 0.0px | 6.0413% | 1.0 |
| 1→2 | 3.8621% | 12.042px | 0.575px | 0.0px | 5.9352% | 1.0 |
| 2→3 | 5.6323% | 26.173px | 1.176px | 0.0px | 7.0442% | 1.0 |
