# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `tarzaning-manager` | PASS | 62px | 34.482px | 61.7976% | 77.3607% | recorded: pass |

## tarzaning-manager — PASS

Concept: A male Manager Homie in a classic brown jungle wrap swings through the air on one continuous vine.

Required action: One immutable Manager-and-vine rig travels through a clear pendulum arc around one pixel-fixed overhead knot; the face, body, hands, wrap, feet, and vine geometry never redraw between phases.

Full-size contact: `qa/strict-repairs/tarzaning-manager/report-root/contacts/tarzaning-manager-source-full.png`

128px contact: `qa/strict-repairs/tarzaning-manager/report-root/contacts/tarzaning-manager-source-128.png`

GIF contact: `qa/strict-repairs/tarzaning-manager/report-root/contacts/tarzaning-manager-gif-128.png`

Failures: none

Warnings: none

Manual notes: Root full-size, 128px, and six-frame GIF inspection confirms one canonical male Manager, exactly two connected arms and hands, two legs and feet, one securely covered brown waist wrap, one uninterrupted vine, a fixed top pivot, a smooth reversible pendulum loop, and no redraw wiggle, debris, duplicate anatomy, crop, scale jump, or palette shimmer.

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

| Stationary region | Max change | Allowed |
|---|---:|---:|
| pixel-fixed-vine-pivot-core | 0.0% | 0.0% |
