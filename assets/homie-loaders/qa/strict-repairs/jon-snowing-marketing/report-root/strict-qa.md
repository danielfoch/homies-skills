# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `jon-snowing-marketing` | PASS | 65px | 8.062px | 2.1157% | 3.0347% | recorded: pass |

## jon-snowing-marketing — PASS

Concept: A male Marketing Homie in black northern fur and leather holds one vertical sword with both hands while snow drifts and the blade glints.

Required action: One immutable Marketing-Homie, cloak, hands, and sword plate remains pixel-locked while six deliberate snowflakes cross the surrounding negative space and one small glint travels along the blade.

Full-size contact: `qa/strict-repairs/jon-snowing-marketing/report-root/contacts/jon-snowing-marketing-source-full.png`

128px contact: `qa/strict-repairs/jon-snowing-marketing/report-root/contacts/jon-snowing-marketing-source-128.png`

GIF contact: `qa/strict-repairs/jon-snowing-marketing/report-root/contacts/jon-snowing-marketing-gif-128.png`

Failures: none

Warnings: none

Manual notes: Root inspection of all four source cells, 128px cells, and the six displayed GIF phases confirms one canonical male Homie, exactly two connected arms and hands, one uninterrupted sword, stable cloak/armor/face anatomy, six intentional snowflake components in every phase, a readable reversible snow-and-glint loop, and no redraw wiggle, crop, scale jump, stray debris, duplicate anatomy, or palette shimmer.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 86237px | 7 (7/0) | none |
| 1 | 71px | 86237px | 7 (7/0) | none |
| 2 | 71px | 86237px | 7 (7/0) | none |
| 3 | 69px | 86237px | 7 (7/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 2.1157% | 8.062px | 0.155px | 0.0px | 3.0324% | 1.0 |
| 1→2 | 2.1157% | 8.062px | 0.155px | 0.0px | 3.0347% | 1.0 |
| 2→3 | 2.1157% | 8.062px | 0.155px | 0.0px | 3.0209% | 1.0 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| locked-face-fur-torso-and-hands | 0.0% | 0.0% |
