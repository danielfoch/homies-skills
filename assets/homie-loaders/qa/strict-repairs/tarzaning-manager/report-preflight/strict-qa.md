# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `tarzaning-manager` | FAIL | 62px | 34.482px | 61.7976% | 77.3607% | pending |

## tarzaning-manager — FAIL

Concept: (not supplied)

Required action: (not supplied)

Full-size contact: `qa/strict-repairs/tarzaning-manager/report-preflight/contacts/tarzaning-manager-source-full.png`

128px contact: `qa/strict-repairs/tarzaning-manager/report-preflight/contacts/tarzaning-manager-source-128.png`

GIF contact: `qa/strict-repairs/tarzaning-manager/report-preflight/contacts/tarzaning-manager-gif-128.png`

Failures: `VISUAL_REVIEW_REQUIRED`

Warnings: `BBOX_SCALE_OR_PROP_JUMP`, `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: (none)

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 62px | 29313px | 1 (1/0) | none |
| 1 | 62px | 29280px | 1 (1/0) | none |
| 2 | 62px | 29308px | 1 (1/0) | none |
| 3 | 62px | 29323px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 61.7861% | 34.366px | 28.033px | 26.907px | 77.1929% | -0.2239 |
| 1→2 | 61.7947% | 34.438px | 28.038px | 26.907px | 77.238% | -0.2267 |
| 2→3 | 61.7976% | 34.482px | 28.09px | 27.203px | 77.3607% | 0.0036 |
