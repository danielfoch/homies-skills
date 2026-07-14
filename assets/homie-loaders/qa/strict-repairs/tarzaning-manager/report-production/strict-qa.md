# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `tarzaning-manager` | PASS | 62px | 34.482px | 61.7976% | 77.3607% | recorded: pass |

## tarzaning-manager — PASS

Concept: A male Manager Homie in a classic brown jungle wrap swings through the air on one continuous vine.

Required action: One immutable Manager-and-vine rig travels through a clear pendulum arc around one pixel-fixed overhead knot; the face, body, hands, wrap, feet, and vine geometry never redraw between phases.

Full-size contact: `qa/strict-repairs/tarzaning-manager/report-production/contacts/tarzaning-manager-source-full.png`

128px contact: `qa/strict-repairs/tarzaning-manager/report-production/contacts/tarzaning-manager-source-128.png`

GIF contact: `qa/strict-repairs/tarzaning-manager/report-production/contacts/tarzaning-manager-gif-128.png`

Failures: none

Warnings: none

Manual notes: Independent full-size, 128px, six-frame GIF, and individual-frame inspection confirms exactly one canonical adult male Manager Homie; a clear bare-chested, brown jungle-wrap, barefoot look; exactly two connected arms/hands and two legs/feet; one uninterrupted vine; a fixed top pivot; generous crop safety; and a readable reversible pendulum loop. No debris, duplicate anatomy, redraw wiggle, scale jump, palette shimmer, or continuity break was observed. A clean rebuild to /tmp/tarzaning-independent produced byte-identical source and GIF SHA-256 hashes (d6e7ed933ce01da07e22c4849557af9278dde2a26a1ba0e8db497c5de6edadb2 and c2cc058d3577f27a64feca83bad642798b895e059962f38c6b1836c4c80b3f3f).

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
