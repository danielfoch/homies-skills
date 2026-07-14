# Wildcard F — exact generation and de-wiggle ledger

Generation mode: built-in image generation, one call per distinct loader. The accepted artwork was chroma-extracted with the installed imagegen helper, then deterministically registered and canonicalized before transparent GIF assembly.

# CRM Gold Pair — Exact Built-in Image Generation Prompt Ledger

Identity/style reference for both generations:
`/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/crm.png`

Built-in outputs:

- `panning-for-gold-crm`: `/Users/danielfoch/.codex/generated_images/019f5718-1758-7fd2-b64e-b1a40ed249a8/exec-dcdf7671-fc8c-4b4a-a27c-eecbabffbddd.png`
- `diamonding-in-rough-crm`: `/Users/danielfoch/.codex/generated_images/019f5718-1758-7fd2-b64e-b1a40ed249a8/exec-ed3bdcb1-6d88-48b0-9b8c-918960537d49.png`

Both outputs were chroma-extracted with the installed imagegen helper. Final sources were deterministically registered, persistent props were canonicalized, each cell was uniformly scaled around its fixed 627×627 center, and the sprite sheets were recomposited over exact RGB `(0,255,0)`.

## `panning-for-gold-crm`

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small AI chat-interface GIF
Input image: Image 1 is the sole exact CRM Homie identity, outfit, proportions, palette, and hand-drawn editorial illustration style anchor.

Primary request: Create one square 2x2 sprite sheet of CRM Homie literally panning for gold with exactly one persistent traditional gold-panning pan. The four authored poses show one small smooth reversible sifting cycle, designed for runtime playback frame 1→2→3→4→3→2. Frame 4 is only the opposite endpoint of the circular tilt and must reverse cleanly; there is no final discovery, victory, empty pan, or terminal reveal. The loading phrase is metadata only. No text appears.

Exact character identity lock: reproduce the same adult Black man from Image 1 in every quadrant—same shaved/bald head, same friendly face and skin tone, olive-gray bomber jacket with its sleeve pocket, plain white T-shirt, light blue jeans, and white slip-on shoes. Preserve his exact identity, proportions, palette, fine editorial ink linework, and soft watercolor/colored-pencil shading. He stands in one stable three-quarter pose holding the pan at waist height. Keep his scalp center, face, torso, hips, legs, feet baseline, body scale, expression, camera, and focal length registered at essentially identical coordinates across all four frames. Only his forearms, two attached hands, the pan, and its contents make a very small coherent sifting motion.

Persistent pan lock: exactly one broad shallow dark charcoal prospector pan with one warm-ochre rim and two small side grips, held by exactly two visible sleeve-connected hands. Preserve the same pan diameter, depth, oval perspective, rim design, colors, and center position in every panel. The pan only rocks/tilts a few degrees around its fixed center; it does not zoom, change shape, duplicate, disappear, translate across the cell, or swap sides.

Persistent contents: inside the pan in every frame are exactly one opaque muted-blue water patch, exactly six small gray gravel ovals, and exactly three small solid gold nugget/fleck shapes. Preserve all counts, individual designs, sizes, and colors in every frame. The water, six gravel pieces, and three gold flecks remain fully inside the pan and shift together by only a few pixels around a small reversible clockwise arc; none appears, disappears, duplicates, spills, flies, or becomes a final prize.

Four authored frames in reading order:
1. Top-left: pan at a shallow left/down tilt, contents resting slightly left.
2. Top-right: pan nearly level with its front rim subtly angled forward, contents slightly lower/front.
3. Bottom-left: pan at a shallow right/down tilt, contents slightly right.
4. Bottom-right: pan nearly level with its back rim subtly angled forward, contents slightly upper/back. This is merely the opposite endpoint and reverses through frames 3, 2, 1.
The motion must be small and continuous, like gently swirling a gold pan, never a large gesture.

Sprite layout and backdrop: exactly four equal square quadrants in standard reading order, borderless with no drawn border, panel line, gutter, divider, seam, caption, or frame labels. One perfectly flat, uniform, exact solid pure #00ff00 chroma-key background fills the entire canvas edge-to-edge and both center axes. No shadow, gradient, texture, floor plane, reflection, scenery, horizon, or lighting variation. Keep the full scalp, elbows, both hands, pan, all contents, full body, and shoes completely inside every 627-by-627 cell with at least 10 percent clear green padding from every outer edge and center axis.

Continuity and anatomy constraints: one character only per frame; exactly two arms, two attached hands, two legs, and two feet; exactly one pan, one water patch, six gravel pieces, and three gold flecks. No hat, shovel, pickaxe, mine, second pan, bucket, dust, translucent particles, motion blur, extra limb, third hand, missing hand, detached fingers, changing clothes, readable text, letters, numbers, logos, caption, watermark, cast shadow, crop, seam, or #00ff00 inside the character or props.
```

Accepted deterministic correction: frame 2 supplies one canonical CRM identity, body, two hands, pan rim, pan body, and handles for all four frames. One persistent extracted contents group (one water patch, four gray gravel pieces, and two gold flecks as actually authored by the accepted generation) moves through four small offsets `(-5,0)`, `(0,4)`, `(5,0)`, `(0,-4)` before reversible playback. This locks every non-content pixel exactly while maintaining visible sifting motion. Final per-cell centered scale: `0.85`.

## `diamonding-in-rough-crm`

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small AI chat-interface GIF
Input image: Image 1 is the sole exact CRM Homie identity, outfit, proportions, palette, and hand-drawn editorial illustration style anchor.

Primary request: Create one square 2x2 sprite sheet of CRM Homie “diamonding in the rough”: he kneels behind exactly one fixed low rubble pile and slowly raises exactly one persistent gleaming diamond from low among the rubble to chest height. The four authored poses form one monotonic reversible lift designed for runtime playback frame 1→2→3→4→3→2. Frame 4 is only the high endpoint of the inspection and must reverse cleanly; there is no terminal reveal, transformation, disappearance, or celebration. The diamond is already visible in his hand in frame 1 and remains the same single object in every frame. The loading phrase is metadata only. No text appears.

Exact character identity lock: reproduce the same adult Black man from Image 1 in every quadrant—same shaved/bald head, same friendly face and skin tone, olive-gray bomber jacket with its sleeve pocket, plain white T-shirt, light blue jeans, and white slip-on shoes. Preserve his exact identity, proportions, palette, fine editorial ink linework, and soft watercolor/colored-pencil shading. He kneels in one stable three-quarter pose behind the rubble, with his left hand resting visibly on his bent left knee and his right hand holding the one diamond. Keep scalp center, face, torso, hips, kneeling leg positions, shoes, body scale, expression, camera, and focal length registered at essentially identical coordinates in all four panels. Only his right forearm, right attached hand, diamond height, and its two tiny opaque sparkle accents change.

Fixed rubble pile lock: exactly one low mound of exactly nine persistent opaque rubble pieces centered on the same baseline in every frame. Preserve the same nine stones’ individual shapes, sizes, brown/charcoal/gray colors, left-to-right order, overlap pattern, outline, perspective, x/y coordinates, width, and height across all four panels. The pile never shifts, reorders, changes count, collapses, grows, zooms, duplicates, or disappears. No dust, floor, cave, mine, shovel, or pickaxe.

Persistent diamond lock: exactly one and only one medium pale blue faceted diamond with a dark navy outline is pinched securely in the character’s same right hand in all four frames. Preserve its exact design, size, orientation, facets, colors, and hand grip. It never leaves the hand, never changes size, never becomes a rock, and is never replaced. Frame 1 must already show the diamond fully enough to count, low and partly nestled against the top of the rubble pile, not hidden. As the same right hand rises, the same diamond moves along one small clean diagonal path and stays visible. Exactly two small solid opaque gold four-point sparkle accents remain next to that diamond in every frame; both move with it and never change count.

Four authored frames in reading order:
1. Top-left: right hand low at the top of the rubble, the one diamond visibly partly nestled among the upper stones; left hand remains on knee.
2. Top-right: same diamond and hand rise to lower-abdomen height.
3. Bottom-left: same diamond and hand rise to upper-abdomen height.
4. Bottom-right: same diamond and hand reach chest height for inspection, with the same two sparkles; this is only the high motion endpoint and reverses through frames 3, 2, 1.
The diamond center must progress strictly upward by a similar amount each step. No new object appears at frame 4.

Sprite layout and backdrop: exactly four equal square quadrants in standard reading order, borderless with no drawn border, panel line, gutter, divider, seam, caption, or frame labels. One perfectly flat, uniform, exact solid pure #00ff00 chroma-key background fills the entire canvas edge-to-edge and both center axes. No shadow, gradient, texture, floor plane, reflection, scenery, horizon, or lighting variation. Keep the full scalp, elbows, both attached hands, diamond and sparkles, entire rubble pile, knees, legs, and shoes completely inside every 627-by-627 cell with at least 10 percent clear green padding from every outer edge and center axis.

Continuity and anatomy constraints: one character only per frame; exactly two arms, two attached hands, two legs, and two feet; exactly one fixed nine-stone rubble pile, one diamond, and two sparkles. No second diamond, extra gem, loose gem in the pile, missing diamond, changing rubble, dust, translucent glow, rays, motion blur, extra limb, third hand, detached fingers, readable text, letters, numbers, logos, caption, watermark, cast shadow, crop, seam, or #00ff00 inside the character or props.
```

Accepted deterministic correction: authored scenes were registered before final compositing with source-cell transforms frame 1 `{}`, frame 2 `{dx:26}`, frame 3 `{dy:2}`, frame 4 `{dx:26,dy:10}`. Frame 2 supplies one canonical fixed nine-rock pile/lower-body plate across all four frames; the intentionally low frame-1 diamond hand is restored above that plate. The one diamond is visible in every authored pose and progresses low→lower abdomen→upper abdomen→chest. Final per-cell centered scale: `0.89`.
# Generation ledger — `needling-in-haystack-research`

## Inputs and method

- Built-in `image_gen` mode.
- Identity/style reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/research.png`.
- Accepted raw generation: `/Users/danielfoch/.codex/generated_images/019f5718-4e4a-7d30-a30e-64b774dcb986/exec-9caf9d3d-c769-4894-885f-200c4dbfad04.png`.
- An earlier draft was rejected because its final pose switched the needle to the opposite hand and its pile redrew materially.

## Accepted generation prompt

```text
Use case: stylized-concept
Asset type: exact four-frame 2x2 sprite master for a reversible loading GIF
Create one exact 1254 x 1254 square image containing four equal 627 x 627 animation cells in reading order: top-left 0, top-right 1, bottom-left 2, bottom-right 3. There must be no visible panel borders, gutters, dividers, grid lines, captions, labels, letters, numbers, words, logos, or watermark.

Character identity: faithfully reproduce the supplied Research Homie in all four cells: the same warm medium-brown-skinned woman, same dense round black curly afro, same friendly face, same gold hoop earrings, same light blue denim jacket, plain white crew-neck shirt, loose black trousers hidden by the hay, and same hand-drawn editorial ink-and-light-texture illustration style. No hat or costume change.

STRICT STATIC-PLATE RULE: draw ONE canonical golden-brown haystack once, then duplicate that exact same haystack plate into all four cells at identical cell-relative x/y coordinates and identical scale. The pile must have a clean simple persistent dome/trapezoid silhouette, the exact same width, height, outline, straw texture, individual outer straw tips, highlights and shadows in all four cells. It may not shift, bounce, resize, morph, redraw, change perspective, lose straw, gain straw, or alter texture. Research Homie's head, face, hair, shoulders and torso must also be registered to identical coordinates, size and angle in all four cells. Fixed camera, no zoom.

HAND-SIDE LOCK: ONLY her arm and hand on the VIEWER'S RIGHT side of the image (her left arm, emerging from her left shoulder) may move and hold the needle in every cell. That SAME viewer-right hand holds the same needle in all four cells. Her other arm/hand remains completely hidden behind the hay in all four cells. Never switch the needle to the viewer-left hand. Never show two hands at once.

Exactly one oversized plain straight silver-gray knitting needle exists in every cell, identical in length, thickness, pointed tip and simple round end cap. No yarn or thread. The needle is continuously visible in every cell, safely points outward away from her face and torso, and never duplicates, transforms, disappears, changes hands, or becomes a sewing needle.

Authored motion, built to ping-pong 0,1,2,3,2,1:
- 0 top-left: viewer-right hand searches low along the front-right portion of the hay; the same needle lies low and near-horizontal, pointing safely outward to the right.
- 1 top-right: same viewer-right hand lifts a small amount; same needle rises to a shallow upward diagonal, still low.
- 2 bottom-left: same viewer-right hand raises the same needle to shoulder height at a clearer upward diagonal.
- 3 bottom-right: same viewer-right hand raises the same needle slightly higher in a playful victorious apex, but remains active and reversible, not a terminal frozen celebration.
The hand/needle path must be smooth and monotonic from low to high. No sudden side switch. No extra arm, hand, finger, needle, yarn, thread, hay tool, or other prop.

Composition: one centered medium shot per cell, head and shoulders emerging from hay. Keep every hair curl, hay straw, sleeve, hand and full needle at least 80 source pixels from every outer cell edge and both invisible center seams. Full props visible and uncropped. Character, haystack and camera remain same size and position. No seam crossing.

Background: perfectly flat uniform solid chroma field across the entire square, nominal #00ff00, with no floor, cast shadow, contact shadow, gradient, texture, halo, reflection, background object or lighting variation. Keep green out of all subject artwork.

Anatomy/quality: one character per cell; exactly one visible moving arm and one visible hand per cell, five natural fingers; no detached or extra limbs, no hand fusion, no crop, no dangerous impalement. Clean production-polished editorial illustration matching the reference.
```

## Deterministic finishing

The accepted built-in output was processed with the installed imagegen chroma helper using border auto-keying, soft matte, thresholds `12/220`, despill, and force. Each `627 × 627` cell was uniformly scaled to `82%` around its exact centre. A single canonical frame-0 hay/body plate was then made by replacing the low arm/needle area with an unobstructed same-location hay patch from authored pose 3, removing disconnected residue, and copying that one plate byte-for-byte into all four cells. Tight masks restore only each pose's moving arm/hand and one needle. The final sheet was recomposited over mathematical RGB `(0,255,0)` and saved as a `1254 × 1254` RGB PNG. No generative redraw occurred after the accepted output.
# `podcasting-marketing` — exact built-in imagegen prompt ledger

Generation mode: built-in `imagegen`. Image 1 in the generation call was the exact project identity/style anchor at `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/marketing.png`.

## Accepted generation

- Built-in output: `/Users/danielfoch/.codex/generated_images/019f5718-82ee-7a12-b85e-39d4fa03a647/exec-99868915-367c-4ce0-95b2-9b5d72c1ac9f.png`
- Final project source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/podcasting-marketing.png`
- The accepted base was chroma-extracted, uniformly center-scaled to `552×552` within each `627×627` cell (`0.8803828…` effective scale), registered deterministically, and recomposited over exact `#00ff00`.

```text
Use case: illustration-story.
Asset type: production four-frame AI loading-animation sprite master.
Input image: Image 1 is the exact Marketing Homie identity, face, hair, beard, outfit, proportions, palette, and hand-drawn editorial illustration style anchor.

Primary request: Create one exact 1254x1254 square 2x2 sprite sheet of Marketing Homie podcasting at one fixed broadcast microphone. The authored frames are four reversible talking phases in reading order, used at runtime as 1→2→3→4→3→2; therefore frame 4 must still be mid-conversation, never a terminal or celebratory result. “Podcasting…” is metadata only and must not appear in the image.

Character lock: same adult man from Image 1, same swept short dark-brown hair, neatly trimmed full beard, warm face, cream hoodie, olive cargo trousers, and white shoes. Add exactly one persistent pair of large over-ear studio headphones: same dark navy padded headband, same two ochre-and-navy earcups, same scale, placement, and geometry in all four frames. One character only. Use a consistent seated three-quarter waist-up composition behind the desk, with head, shoulders, torso, chair, and desk registered at exactly the same pixel coordinates, scale, and camera in all frames. Exactly two sleeve-connected arms and exactly two anatomically correct hands in every frame.

Fixed podcast setup: exactly one large side-address pod/broadcast microphone, dark navy with a cream grille, mounted vertically on exactly one compact fixed dark navy desk stand with one circular base. The microphone, grille, stem, base, compact cream desk, chair, headphones, and any visible short cable segment must remain identical in shape, perspective, size, and pixel position across all four quadrants. Keep the mic centered slightly to the character’s right and close to his mouth, but never covering his face. If a cable is shown, use one short fixed cable only; it must not bend, lengthen, disappear, or change sockets. No boom arm.

Reversible subtle action: keep the mouth close to the same fixed microphone. Frame 1: mouth slightly open in a small rounded speaking shape, both hands resting naturally near the desk. Frame 2: mouth a little wider, one forearm lifts slightly and the corresponding hand begins a small palm-up gesture. Frame 3: mouth returns to a narrower open shape, the same hand reaches the highest point of the small gesture. Frame 4: mouth opens moderately, the same hand eases halfway back down while still mid-sentence. The other hand remains stably resting on the desk throughout. Head may make only a tiny 1–2 degree nod; do not translate, resize, rotate, or redraw the head, headphones, torso, chair, desk, microphone, or stand. Only mouth line and one sleeve-connected forearm/hand change in small smooth increments. Reverse playback must feel like natural conversational emphasis, not dancing or bouncing.

Layout/background: exactly four equal 627px cells in a borderless 2x2 reading-order grid. Entire 1254x1254 canvas, including the center vertical and horizontal axes, must be one perfectly flat uniform pure RGB #00ff00. No seams, gutters, dividing lines, panels, shadows, floor plane, gradients, texture, reflections, green variation, or lighting spill. Generous padding: every non-green subject pixel must remain at least 55 source pixels inside every edge of its own 627x627 cell. Full hair/headphones, beard, shoulders, both elbows/hands, desk edges, chair, complete microphone, complete stand/base, and cable if any fully visible and separated from cell borders.

Visual style: preserve the reference’s clean hand-drawn editorial ink contours, warm cream/olive/navy/ochre palette, restrained watercolor-like shading within subjects only, and friendly professional expression. Keep line weight and rendering density identical across all quadrants.

Constraints: one Marketing Homie, one pair of headphones, one microphone, one stand/base, one desk, at most one chair, exactly two arms/hands. No second microphone, no duplicated earcup, no extra arm/hand/fingers, no floating limb, no detached hand, no headset mic, no boom arm, no phone, laptop, mixer, cup, notes, pop filter, cable morph, text, letters, numbers, podcast logo, sound-wave symbols, speech bubble, caption, border, watermark, crop, seam, or #00ff00 anywhere inside the subject.
```

## Inspected fixed-prop correction attempt

- Built-in edit output: `/Users/danielfoch/.codex/generated_images/019f5718-82ee-7a12-b85e-39d4fa03a647/exec-e2875333-24de-4969-85c2-ffbed5cceaef.png`
- This output was visually inspected, but the final uses deterministic canonicalization from the accepted generation above because it gives literal pixel-registered props instead of model-redrawn approximations.

```text
Use case: precise-object-edit.
Asset type: corrected four-frame production sprite master.
Input image: Image 1 is an otherwise accepted 1254x1254 2x2 Marketing Homie podcasting sprite sheet.

Primary request: Keep the artwork, identity, speaking sequence, green background, and layout, but canonicalize the fixed scene across all four quadrants. Use the top-left quadrant as the exact canonical source for the podcast microphone capsule/grille/body, vertical desk-stand stem, circular stand base, short cable path, tabletop outer silhouette/edge, and chair silhouette. In the top-right, bottom-left, and bottom-right quadrants, redraw those fixed props to match the top-left versions exactly in shape, dimensions, perspective, color, linework, and the same cell-relative pixel coordinates. One identical persistent chair must remain behind the character in all four cells. Register Marketing Homie’s headphones, head, shoulders, and torso to the top-left cell-relative coordinates and scale in all four cells.

Motion preservation: preserve the existing four mouth shapes and the existing one-hand gesture progression. Only the mouth and that single sleeve-connected gesturing forearm/hand may vary. Preserve the other resting arm/hand, but register it naturally to the unchanged fixed desk. The four poses remain reversible 1→2→3→4→3→2 and mid-conversation. Exactly two arms and two hands in every frame.

Absolute invariants: same one Marketing Homie identity, face/beard/hair, cream hoodie, olive trousers where visible, one persistent pair of large navy/ochre over-ear headphones; exactly one side-address navy/cream microphone, exactly one vertical compact stand and one round base, exactly one fixed short cable, one compact cream tabletop, one persistent dark chair. Preserve the uniform pure #00ff00 field, borderless 2x2 structure, generous clear margins, style, lighting, palette, and four distinct speaking phases.

Do not change the top-left quadrant. Do not add or remove any object. No second mic, boom arm, pop filter, headset mic, duplicated earcup, extra cable, extra chair, extra limb/hand, floating hand, table morph, cable morph, text, letters, numbers, podcast logo, wave marks, caption, watermark, crop, gutter, seam, panel, shadow, or background variation.
```

## Deterministic de-wiggle operations retained in the final

- Chroma-key extraction with the installed helper using border auto-key, soft matte, thresholds `12/220`, and despill.
- Centered per-cell scale to `552×552`, yielding at least `57 px` source-cell clearance.
- Measured source-space whole-frame registration: frame 1 `(0,0)`, frame 2 `(+24,0)`, frame 3 `(+8,+7)`, frame 4 `(+24,+7)`.
- The frame-1 microphone/grille/body, stand/stem/base, cable path, stable resting-arm region, lower tabletop silhouette, visible outer chair silhouette, headphones, head, and upper hood were copied as canonical fixed pixels into frames 2–4.
- Each target frame’s original mouth patch was restored after the fixed head copy, so the four authored speaking phases remain distinct.
- Final runtime alignment is deliberately identity transforms because registration is baked into the source master.

