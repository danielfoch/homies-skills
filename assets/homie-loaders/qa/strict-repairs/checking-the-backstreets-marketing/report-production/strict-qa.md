# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `checking-the-backstreets-marketing` | PASS | 65px | 10.77px | 7.0743% | 12.3083% | recorded: pass |

## checking-the-backstreets-marketing — PASS

Concept: A male canonical Marketing Homie in the supplied black hat-and-bomber outfit performs a sharp 1990s boy-band arm groove.

Required action: Two complete connected sleeve-forearm-hand units counter-sweep around fixed shoulders while the wide-brim hat, aviators, face, beard, jacket core, long white shirt, hips, ripped jeans, legs and planted boots remain pixel-identical.

Full-size contact: `qa/strict-repairs/checking-the-backstreets-marketing/report-production/contacts/checking-the-backstreets-marketing-source-full.png`

128px contact: `qa/strict-repairs/checking-the-backstreets-marketing/report-production/contacts/checking-the-backstreets-marketing-source-128.png`

GIF contact: `qa/strict-repairs/checking-the-backstreets-marketing/report-production/contacts/checking-the-backstreets-marketing-gif-128.png`

Failures: none

Warnings: none

Manual notes: Inspected all four 627px cells, the 128px source contact and decoded GIF contact. The wide bent-knee stance and opposing open-hand arm hits read as 1990s synchronized boy-band choreography. The same male Marketing face, wide-brim hat, aviators, bomber, long white shirt, knee rips, legs and boots remain fixed. Both connected arms retain exactly one natural hand, margins are clear, and no shoulder seam, duplicate anatomy, debris, palette shimmer, crop or loop snap is visible.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 65187px | 1 (1/0) | none |
| 1 | 65px | 64488px | 1 (1/0) | none |
| 2 | 65px | 63045px | 1 (1/0) | none |
| 3 | 65px | 62715px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 7.0743% | 10.77px | 1.658px | 0.0px | 12.3083% | 0.9943 |
| 1→2 | 5.4506% | 10.63px | 2.89px | 0.0px | 11.3938% | 0.9944 |
| 2→3 | 5.4546% | 10.63px | 1.163px | 0.0px | 12.1885% | 0.9924 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-hat-aviators-face-shirt-core | 0.0% | 0.0% |
| fixed-ripped-jeans-legs-and-boots | 0.0% | 0.0% |
