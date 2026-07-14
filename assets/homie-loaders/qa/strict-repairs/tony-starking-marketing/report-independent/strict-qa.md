# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `tony-starking-marketing` | PASS | 70px | 2.236px | 0.0984% | 2.7068% | recorded: pass |

## tony-starking-marketing — PASS

Concept: Canonical Marketing Homie in a red/gold powered suit with palm and chest energy pulse

Required action: The raised armored open palm and chest reactor pulse in four authored intensities while face, anatomy, suit, crop, anchor, and scale remain fixed.

Full-size contact: `assets/homie-loaders/qa/strict-repairs/tony-starking-marketing/report-independent/contacts/tony-starking-marketing-source-full.png`

128px contact: `assets/homie-loaders/qa/strict-repairs/tony-starking-marketing/report-independent/contacts/tony-starking-marketing-source-128.png`

GIF contact: `assets/homie-loaders/qa/strict-repairs/tony-starking-marketing/report-independent/contacts/tony-starking-marketing-gif-128.png`

Failures: none

Warnings: none

Manual notes: Independent inspection of every full-size cell, every 128px cell, and all six decoded GIF phases confirms one canonical adult male Marketing Homie in one continuous red-and-gold powered suit, with one raised five-finger armored palm and one chest reactor. Both emitter pulses remain legible at 128px while face, beard, anatomy, suit seams, boots, crop, anchor, and scale stay fixed. No redraw wiggle, extra prop, text, debris, or whole-frame scale jump is present.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 70px | 47716px | 1 (1/0) | none |
| 1 | 70px | 47716px | 1 (1/0) | none |
| 2 | 70px | 47722px | 1 (1/0) | none |
| 3 | 70px | 47769px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.0% | 0.0px | 0.0px | 0.0px | 1.6808% | 0.9939 |
| 1→2 | 0.0126% | 1.0px | 0.02px | 0.0px | 2.2107% | 0.9895 |
| 2→3 | 0.0984% | 2.236px | 0.162px | 0.0px | 2.7068% | 0.9893 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| locked lower body and boots | 0.0% | 0.0% |
