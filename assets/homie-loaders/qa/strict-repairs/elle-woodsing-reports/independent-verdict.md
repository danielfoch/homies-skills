# Independent release QA — `elle-woodsing-reports`

**Verdict: PASS**

Candidate reviewed read-only from `/tmp/elle-woodsing-paw-v1`. I inspected the full-size four-phase source contact, the 128 px source contact, the magnified paw contact, and all six independently decoded GIF frames.

## Visual gate

- The character reads unmistakably as an adult female Homie: feminine face and proportions, blonde high ponytail, hot-pink sunglasses, fitted hot-pink blazer and pencil skirt, pink heels, and a coordinated handbag.
- There is exactly one coherent tan chihuahua, wearing one purple-and-pink sweater. Its head, ears, torso, fixed legs, and supporting contact with the woman's arm remain continuous.
- The dog's outer forepaw stays connected at the sleeve/wrist and makes a compact, readable wave. There is no duplicate paw, extra hand, doubled limb, broken wrist, ghost trail, seam, or anatomy swap.
- The woman, handbag, holding hand/arm, dog head/body, skirt, legs, and feet do not redraw or drift.
- Full-size and loader-size views are clean: no visible debris, background residue, crop, edge collision, or stray duplicated object.

## Independent pixel checks

- Source phases are four distinct 627×627 RGBA frames. Across all phases, every changed pixel is confined to the paw box `x=372..404, y=175..211`; the union is only 761 pixels. Every pixel outside that box is byte-identical to phase 0.
- Source foreground alpha bounds are approximately `x=221..404, y=61..565`, leaving ample canvas margin with no crop.
- The decoded production GIF is 256×256, transparent, infinite-looping, and has six frames with four unique phases in the exact ping-pong order `[0, 1, 2, 3, 2, 1]`.
- Frame durations are `[210, 140, 140, 210, 140, 140]` ms.
- In decoded GIF pixels, all motion is confined to `x=153..163, y=72..86` (98-pixel union). Every decoded RGBA pixel outside that small paw region is identical across all six frames, which rules out whole-body shift and palette shimmer.
- Decoded alpha bounds remain `x=91..163, y=26..229`; all four corners are transparent. The production GIF has one connected foreground component in every frame, so the raised paw is not detached and there are no visible floating fragments.
- Alpha-centroid variation is only the intended paw motion (about 0.10 px at 256 px); registration of the fixed figure is 0 px.
- The closing sequence is continuous: frame 6 is byte-identical to phase 1, then returns naturally to phase 0 without a jump.

## Release decision

PASS. The concept, female character requirement, Elle-inspired pink styling, single-dog continuity, paw-wave action, stability, transparency, and six-frame loop all meet the strict release gate.
