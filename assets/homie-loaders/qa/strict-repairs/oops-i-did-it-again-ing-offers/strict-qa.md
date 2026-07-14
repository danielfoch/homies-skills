# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `oops-i-did-it-again-ing-offers` | PASS | 65px | 6.325px | 2.7939% | 5.3009% | recorded: pass |

## oops-i-did-it-again-ing-offers — PASS

Concept: Perform the supplied chest-palm and horizontal-arm Oops dance pose in a pure glossy red spandex catsuit.

Required action: The chest palm and crossed stance remain fixed while the opposite connected forearm progressively straightens into a shoulder-height horizontal reach.

Full-size contact: `/tmp/oops-chest-reach-v4/strict-policy/contacts/oops-i-did-it-again-ing-offers-source-full.png`

128px contact: `/tmp/oops-chest-reach-v4/strict-policy/contacts/oops-i-did-it-again-ing-offers-source-128.png`

GIF contact: `/tmp/oops-chest-reach-v4/strict-policy/contacts/oops-i-did-it-again-ing-offers-gif-128.png`

Failures: none

Warnings: none

Manual notes: Full-size and 128px contacts inspected. One canonical body plate is reused exactly. Bun, face, torso, chest hand, pelvis, crossed legs and both feet have zero changed decoded-GIF pixels outside the reaching arm. One shared GIF palette removes colour flicker. Only the connected reaching forearm changes through an elbow-anchored continuous shear. Four cells have one connected foreground component, no crop, seams, ghosts, debris or extra anatomy.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 65px | 35751px | 1 (1/0) | none |
| 1 | 65px | 35752px | 1 (1/0) | none |
| 2 | 65px | 35746px | 1 (1/0) | none |
| 3 | 65px | 35750px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 2.7939% | 6.325px | 0.244px | 0.0px | 5.3009% | 0.9853 |
| 1→2 | 2.5953% | 6.0px | 0.204px | 0.0px | 5.1189% | 0.9861 |
| 2→3 | 2.6281% | 6.0px | 0.241px | 0.0px | 5.1402% | 0.9862 |

| Stationary region | Max change | Allowed |
|---|---:|---:|
| canonical-head-torso-chest-hand-hips-crossed-legs-feet | 0.0% | 0.0% |
