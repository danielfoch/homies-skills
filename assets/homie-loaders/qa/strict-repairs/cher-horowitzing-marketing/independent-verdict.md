# Independent QA — `cher-horowitzing-marketing`

**Verdict: PASS**

Candidate audited read-only: `/tmp/cher-horowitz-female-v3`

## Visual gate

- The character reads unambiguously as an adult woman: feminine face and body presentation, long blonde hair, no facial hair, skirt, and the intended Cher Horowitz-inspired styling.
- The yellow-and-black plaid blazer/skirt, white blouse, white knee socks, and black loafers are recognizable and remain identical across all four source phases.
- Anatomy is coherent: one stable face/head, two arms, two hands, two legs and two feet; no duplicated or malformed anatomy is visible at full size or 128 px.
- Exactly one flip phone remains in the same grasp. The holding hand and lower handset are fixed. Only the connected upper lid/display changes as it opens and wakes; the display stays blank and the prop does not change identity.
- No crop, edge collision, ghosting, seams, detached fragments, palette flicker, background trash, or unexpected redraw was found. The action remains legible at 128 px.

## Independent pixel checks

- Source motion is confined to `x=220..250, y=94..137` in the 627 px cell—the phone lid/display only. There are **0 changed pixels** outside a broad phone ROI, **0** in the right-side face/hair/torso/outfit region, and **0** below `y=188` covering the body, legs and feet.
- Structural QA reports one significant connected foreground component and zero tiny components in every phase, with a 65 px minimum keyed margin and no edge/gutter contamination.
- Registration shift is 0 px for every source transition. The small 0.461–0.492 px foreground-centroid changes are explained entirely by the opening phone lid, not character drift.
- The decoded GIF has six frames with exact phase pattern `[0,1,2,3,2,1]`, durations `[210,140,140,210,140,140]` ms, infinite loop, and exact loop closure.
- Every GIF frame has the identical alpha bbox `(91,27)-(165,229)`. Across all GIF phases there are **0 changed RGBA pixels** in the fixed body/right-side regions (`x>=116` and `y>=77` at 256 px); only the phone area changes.
- Decoded GIF per-step centroid movement is only 0.187–0.220 px and follows the phone lid's intended opening/closing motion. No whole-character jiggle or palette shimmer is present.

## Evidence consistency

- The supplied strict report records PASS with no failures or warnings and its metrics agree with the independent decode checks.
- Source SHA-256: `37a5dec275eeb52b8ff154332ac6745a14f9da681f7998dbf36692222c34add7`
- GIF SHA-256: `36bc53cca6ecb6bc20fda32cd427bc6b45bf6ccf495f9c0ebc7514051eb2344f`

**Release recommendation: approve this candidate.**
