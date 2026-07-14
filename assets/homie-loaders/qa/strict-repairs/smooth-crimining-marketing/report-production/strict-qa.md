# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `smooth-crimining-marketing` | PASS | 65px | 11.402px | 17.1507% | 53.4158% | recorded: pass |

## smooth-crimining-marketing — PASS

Concept: Marketing Homie in an ivory-white pinstripe suit and fedora performs a gravity-defying Smooth Criminal-inspired lean.

Required action: One SHA-locked canonical Marketing Homie plate deepens through four ankle-anchored lean phases; both shoes, socks, ankle cuffs and sole contact pixels remain exactly fixed while the connected body above the ankles moves as one continuous figure.

Full-size contact: `qa/strict-repairs/smooth-crimining-marketing/report-production/contacts/smooth-crimining-marketing-source-full.png`

128px contact: `qa/strict-repairs/smooth-crimining-marketing/report-production/contacts/smooth-crimining-marketing-source-128.png`

GIF contact: `qa/strict-repairs/smooth-crimining-marketing/report-production/contacts/smooth-crimining-marketing-gif-128.png`

Failures: none

Warnings: none

Manual notes: Inspected all four 627px cells, the 128px contact sheet and the exact reversible decoded GIF sequence. The iconic lean reads immediately; the same Marketing Homie face, hat, armband, suit pinstripes, arms and anatomy persist throughout. The connected body deepens into the lean without independent redraws, both shoes and sole-contact pixels remain exact, margins stay clear, and no debris, crop, palette shimmer or loop snap is visible.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 49971px | 1 (1/0) | none |
| 1 | 65px | 49979px | 1 (1/0) | none |
| 2 | 65px | 49992px | 1 (1/0) | none |
| 3 | 65px | 49983px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 17.1356% | 11.402px | 8.458px | 8.0px | 53.0344% | 0.6947 |
| 1→2 | 17.1507% | 11.402px | 8.45px | 8.0px | 53.383% | 0.6943 |
| 2→3 | 17.1468% | 11.402px | 8.423px | 8.0px | 53.4158% | 0.6958 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| pixel-locked-shoes-soles-and-contact | 0.0% | 0.0% |
