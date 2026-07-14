# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `barbie-ing-listings` | PASS | 65px | 7.28px | 3.3789% | 10.0182% | recorded: pass |
| `pulp-fictioning-manager` | PASS | 65px | 9.487px | 3.4065% | 6.7499% | recorded: pass |
| `michael-burrying-manager` | PASS | 60px | 9.849px | 2.3206% | 8.4285% | recorded: pass |
| `harvey-spectering-manager` | PASS | 64px | 4.243px | 0.3596% | 5.262% | recorded: pass |

## barbie-ing-listings — PASS

Concept: A clearly female canonical Homie poses in a bright pink tailored Barbie-inspired outfit.

Required action: The connected pointing forearm pivots around one fixed elbow while the connected ponytail tail counter-swishes; face, sunglasses, hair cap, torso, planted hand, skirt, legs and heels remain fixed.

Full-size contact: `qa/strict-repairs/character-assignment-batch/report-production/contacts/barbie-ing-listings-source-full.png`

128px contact: `qa/strict-repairs/character-assignment-batch/report-production/contacts/barbie-ing-listings-source-128.png`

GIF contact: `qa/strict-repairs/character-assignment-batch/report-production/contacts/barbie-ing-listings-gif-128.png`

Failures: none

Warnings: none

Manual notes: Single canonical female plate. Face, sunglasses, hair cap, torso, planted hand, skirt, legs and heels remain exact; only the pointing forearm and connected ponytail tail move. No redraw, extra anatomy, debris, crop or palette shimmer.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 43728px | 1 (1/0) | none |
| 1 | 65px | 43392px | 1 (1/0) | none |
| 2 | 65px | 42905px | 1 (1/0) | none |
| 3 | 65px | 43088px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 2.2203% | 5.0px | 1.061px | 0.0px | 8.1319% | 0.9871 |
| 1→2 | 3.3789% | 7.28px | 1.578px | 0.0px | 10.0182% | 0.9814 |
| 2→3 | 2.3286% | 5.0px | 0.535px | 0.0px | 8.4868% | 0.9865 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-skirt-legs-heels | 0.0% | 0.0% |

## pulp-fictioning-manager — PASS

Concept: A clearly male canonical Manager Homie performs the iconic black-suit bent-knee twist.

Required action: Both connected distal forearms counter-rotate around fixed elbows while the male face, swept shoulder-length hair, bolo tie, torso, hips, legs and shoes remain fixed.

Full-size contact: `qa/strict-repairs/character-assignment-batch/report-production/contacts/pulp-fictioning-manager-source-full.png`

128px contact: `qa/strict-repairs/character-assignment-batch/report-production/contacts/pulp-fictioning-manager-source-128.png`

GIF contact: `qa/strict-repairs/character-assignment-batch/report-production/contacts/pulp-fictioning-manager-gif-128.png`

Failures: none

Warnings: none

Manual notes: Male face, shoulder-length swept hair, bolo tie, torso, pelvis, legs and shoes stay fixed. Fixed elbow disks prevent holes or duplicate limbs. No female identity, morph, camera motion, debris, crop or shimmer.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 59785px | 1 (1/0) | none |
| 1 | 65px | 59448px | 1 (1/0) | none |
| 2 | 65px | 59092px | 1 (1/0) | none |
| 3 | 65px | 59182px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 2.4374% | 7.071px | 0.817px | 0.0px | 5.1862% | 1.0 |
| 1→2 | 3.4065% | 9.487px | 1.439px | 0.0px | 6.7499% | 1.0 |
| 2→3 | 2.0883% | 5.385px | 0.43px | 0.0px | 5.3446% | 1.0 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-male-head-tie-torso | 0.0% | 0.0% |
| fixed-bent-knee-lower-body | 0.0% | 0.0% |

## michael-burrying-manager — PASS

Concept: A clearly male canonical Manager Homie in a faded blue pocket tee desk-drums with wired earbuds.

Required action: Exactly two connected forearm-hand-drumstick units alternate tabletop-directed strokes around fixed elbows while the male head, earbud wires, shirt core, chair, paper stack and desk remain fixed.

Full-size contact: `qa/strict-repairs/character-assignment-batch/report-production/contacts/michael-burrying-manager-source-full.png`

128px contact: `qa/strict-repairs/character-assignment-batch/report-production/contacts/michael-burrying-manager-source-128.png`

GIF contact: `qa/strict-repairs/character-assignment-batch/report-production/contacts/michael-burrying-manager-gif-128.png`

Failures: none

Warnings: none

Manual notes: Manager face, hair, shirt core, earbuds, chair, papers and desk are one immutable plate. Exactly two hands and two sticks remain continuous. No duplicated props, desk drift, floating notes, debris, crop or shimmer.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 60px | 76612px | 1 (1/0) | none |
| 1 | 60px | 76702px | 1 (1/0) | none |
| 2 | 60px | 76802px | 1 (1/0) | none |
| 3 | 60px | 76792px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 1.9404% | 9.849px | 0.286px | 0.0px | 7.746% | 0.9389 |
| 1→2 | 2.3206% | 8.246px | 0.505px | 0.0px | 8.4285% | 0.9497 |
| 2→3 | 1.3297% | 6.325px | 0.217px | 0.0px | 6.5812% | 0.9605 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-manager-head | 0.0% | 0.0% |
| fixed-desk-fascia | 0.0% | 0.0% |

## harvey-spectering-manager — PASS

Concept: A clearly male canonical Manager Homie adopts a sharp closer-lawyer pose in a charcoal suit.

Required action: One connected cuff-and-lapel forearm makes a compact confident adjustment around a fixed elbow while the male face, hair, tie, suit core, folder, other arm, legs and shoes remain fixed.

Full-size contact: `qa/strict-repairs/character-assignment-batch/report-production/contacts/harvey-spectering-manager-source-full.png`

128px contact: `qa/strict-repairs/character-assignment-batch/report-production/contacts/harvey-spectering-manager-source-128.png`

GIF contact: `qa/strict-repairs/character-assignment-batch/report-production/contacts/harvey-spectering-manager-gif-128.png`

Failures: none

Warnings: none

Manual notes: Single male Manager plate in a charcoal suit. Face, hair, tie, suit core, folder, other arm, legs and shoes remain exact. No redraw, extra fingers, folder motion, debris, crop or shimmer.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 64px | 41543px | 1 (1/0) | none |
| 1 | 64px | 41593px | 1 (1/0) | none |
| 2 | 64px | 41685px | 1 (1/0) | none |
| 3 | 64px | 41630px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 0.2547% | 2.68px | 0.104px | 0.0px | 4.1806% | 0.9442 |
| 1→2 | 0.3596% | 4.243px | 0.198px | 0.0px | 5.262% | 0.8808 |
| 2→3 | 0.1943% | 2.828px | 0.117px | 0.0px | 4.0913% | 0.9178 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| fixed-manager-head | 0.0% | 0.0% |
| fixed-folder-and-lower-body | 0.0% | 0.0% |
