# Wildcard E Batch A — exact built-in imagegen prompt ledger

Generation mode: built-in `imagegen`, one call per distinct asset or targeted correction.

## Accepted finals

- `tying-loose-ends-manager`: accepted base `exec-1a37cc93-49da-4b74-94ee-e8933859826f.png`; final source `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/tying-loose-ends-manager.png`; deterministic centered per-cell scale 0.88.
- `operating-on-file-reports`: accepted base `exec-b5f6fb8c-bd0d-40d5-a981-2c80ea6d065d.png`; final source `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/operating-on-file-reports.png`; deterministic centered per-cell scale 0.86.
- `locking-in-offers`: accepted base `exec-ba024f60-0704-4ef6-8edb-cc973de5c208.png`; final source `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/locking-in-offers.png`; deterministic centered per-cell scale 0.88.
- `lockboxing-offers`: accepted base `exec-d789ba7d-d5a1-4f56-80ba-edaac9aafbf4.png`; final source `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/lockboxing-offers.png`; deterministic centered per-cell scale 0.84.
- `running-comps-cma`: accepted base `exec-1a7edbf3-c0ba-42cd-ba9b-d32064be9fbe.png plus deterministic frame-4 card-group +4px patch`; final source `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/running-comps-cma.png`; deterministic centered per-cell scale 0.83.
- `combing-mls-crm`: accepted base `exec-76f397c9-cd1d-488e-be07-a42c3ff8adc6.png`; final source `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/combing-mls-crm.png`; deterministic centered per-cell scale 0.86.
- `counter-offering-offers`: accepted base `exec-91293e07-39ee-4057-9a39-09f350397ee6.png`; final source `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/counter-offering-offers.png`; deterministic centered per-cell scale 0.87.
- `farming-sphere-crm`: accepted base `exec-97e32f7f-93c9-4ab3-8c05-c7ac710e5a11.png`; final source `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/farming-sphere-crm.png`; deterministic centered per-cell scale 0.87.

## Exact generation and correction prompts

### 1. `tying-loose-ends-manager` — generation

- Reference/edit target: `assets/homie-loaders/references/manager.png`
- Built-in output: `exec-1a37cc93-49da-4b74-94ee-e8933859826f.png`

```text
Use case: illustration-story.
Asset type: production four-frame AI loading-animation sprite master.
Input image: Image 1 is the exact Manager Homie identity, outfit, proportions, palette, and hand-drawn editorial style anchor.

Primary request: Create a 1254x1254 square 2x2 sprite sheet of Manager Homie tying one giant rope knot. Runtime order is 1→2→3→4→3→2, so the four poses must be one reversible progression from loose to tighter, with no terminal finished pose. “Tying up loose ends…” is metadata only and must not appear.

Character lock: same adult man from Image 1, same swept brown hair, face, camel double-breasted long coat, charcoal scarf, dark trousers, and brown shoes. One full-body character centered and registered at the same head, torso, hips, feet, scale, and three-quarter camera coordinates in all frames. Exactly two sleeve-connected arms and two anatomically correct hands.

Persistent rope: exactly one thick tan rope with exactly two visible free ends and one large central overhand knot at waist height. Same rope thickness, color, total length, ends, and knot construction in all frames. Manager holds one free end in each hand continuously; no floating end or extra coil.

Frames: top-left knot is very loose with a wide open central loop; top-right hands move slightly apart and the same loop crosses into a loose knot; bottom-left the same knot becomes moderately snug; bottom-right it is the tightest pose but still visibly adjustable, with both free ends in his hands and no presentation or completion. Knot opening shrinks monotonically frame1→2→3→4; reverse playback loosens it cleanly. Only forearms/hands, rope ends, and knot loop change.

Layout/background: exactly four equal 627px cells in a borderless 2x2 reading-order grid. Flat uniform pure #00ff00 across the entire canvas and center axes; no seams, gutters, shadows, gradients, floor, texture, reflections, or variation. Generous padding; full hair, coat, elbows, shoes, rope, knot, and both ends fully visible with nothing crossing a cell edge.

Constraints: one character, exactly two arms/hands/legs/feet, one rope, two rope ends, one knot per frame. No second rope, duplicate loop, extra hand, detached fingers, scissors, bow, package, text, letters, numbers, logos, caption, watermark, crop, or #00ff00 in subjects.
```

### 2. `operating-on-file-reports` — generation

- Reference/edit target: `assets/homie-loaders/references/reports.png`
- Built-in output: `exec-b5f6fb8c-bd0d-40d5-a981-2c80ea6d065d.png`

```text
Use case: illustration-story.
Asset type: production four-frame AI loading-animation sprite master.
Input image: Image 1 is the exact Reports Homie identity, outfit, proportions, palette, and editorial illustration style anchor.

Primary request: Create a 1254x1254 square 2x2 sprite sheet of Reports Homie playfully “operating” on one file folder. Runtime order 1→2→3→4→3→2 must read as a reversible left-to-right repair pass, never a terminal finished operation. “Operating…” is metadata only and must not appear.

Character: same woman from Image 1—same long dark-brown wavy hair, face, cream tailored pantsuit, blouse, peach scarf, trousers, and beige shoes. Add one persistent plain coral surgical cap and cream waist apron, no logo or text; keep her face visible. One full-body character behind the table, same registered head/torso/feet/camera/scale each frame. Exactly two sleeve-connected arms and two hands.

Fixed scene: exactly one compact navy operating table on two cream legs, identical in every frame. Exactly one oversized closed coral file folder lies flat at its center, same shape/position/perspective, with one cream tab and no writing. On the folder is one small dashed cream repair seam that remains visible in all frames and never becomes fully completed.

Tools/action: exactly one slim navy probe in her right hand and one small cream clamp in her left, same designs and grips throughout. Both tools remain visibly hand-held. Frame1 probe/clamp at far-left end of seam; frame2 left-center; frame3 right-center; frame4 far-right, still actively probing/clamping with seam persistent. Tool tips progress strictly left→left-center→right-center→right; reverse playback is the return repair pass. No folder opens/closes, no result display, no blood, no patient, no disappearance.

Layout: four equal 627px cells in borderless 2x2 reading order. Entire canvas/center axes flat uniform pure #00ff00; no seams, gutters, panels, shadows, gradients, floor, texture, reflections, or variation. Full hair/cap, elbows, shoes, table legs, folder, probe, clamp fully visible and isolated in each cell.

Constraints: one character, exactly two arms/hands, one table, one folder, one probe, one clamp, one persistent seam per frame. No extra tool, hand, file, table, syringe, readable text, letters, numbers, medical logo/cross, caption, watermark, crop, or #00ff00 inside subjects.
```

### 3. `locking-in-offers` — generation

- Reference/edit target: `assets/homie-loaders/references/offers.png`
- Built-in output: `exec-ba024f60-0704-4ef6-8edb-cc973de5c208.png`

```text
Use case: illustration-story.
Asset type: production four-frame AI loading-animation sprite master.
Input image: Image 1 is the exact Offers Homie identity, outfit, proportions, palette, and editorial illustration style anchor.

Primary request: Create a 1254x1254 square 2x2 sprite sheet of Offers Homie “locking in” by guiding one giant padlock shackle through a reversible closing arc. Runtime 1→2→3→4→3→2 must never show a terminal click. “Locking in…” is metadata only and must not appear.

Character: same woman from Image 1, same top bun/loose strands, face, beige pinstriped jumpsuit, belt, rolled cuffs, and white sneakers. One full-body character centered beside/behind the lock, same registered head/torso/feet/camera/scale in all frames. Exactly two sleeve-connected arms and two hands.

Persistent lock: exactly one oversized navy-and-ochre padlock with one fixed rectangular body on one short cream pedestal, and one thick silver U-shaped shackle hinged at the body’s left socket. Lock body, keyhole, pedestal, dimensions, perspective, colors, and coordinates never change. No keys or numbers.

Interaction: one hand grips the shackle top continuously; her other hand steadies the lock body. Frame1 shackle is fully raised/open and angled left; frame2 swings partway down; frame3 swings lower toward the right socket; frame4 is almost seated but a small visible gap remains, so it is not locked. Shackle angle/gap decreases monotonically 1→2→3→4; reverse playback reopens cleanly. Only working forearm/hand and shackle rotate; no click, sparkle, closed result, or presentation.

Layout: exact four 627px cells in borderless 2x2 reading order, flat uniform pure #00ff00 over canvas/center axes. No seams, gutters, panels, shadows, gradients, floor, texture, reflection, or variation. Full bun, elbows, shoes, pedestal, body, and complete shackle fully visible and isolated.

Constraints: one character, exactly two arms/hands, one padlock body, one shackle, one pedestal. No extra lock, key, chain, extra hand, floating shackle, digits, readable text, logos, caption, watermark, crop, or #00ff00 inside subjects.
```

### 4. `lockboxing-offers` — generation

- Reference/edit target: `assets/homie-loaders/references/offers.png`
- Built-in output: `exec-d789ba7d-d5a1-4f56-80ba-edaac9aafbf4.png`

```text
Use case: illustration-story.
Asset type: production four-frame AI loading-animation sprite master.
Input image: Image 1 is the exact Offers Homie identity, outfit, proportions, palette, and editorial illustration style anchor.

Primary request: Create a 1254x1254 square 2x2 sprite sheet of Offers Homie “lockboxing” by lightly tapping four giant numberless lockbox buttons left-to-right with boxing gloves. Runtime 1→2→3→4→3→2 is a reversible tapping pass, no completed code. “Lockboxing…” is metadata only and must not appear.

Character: same Offers Homie from Image 1, same bun/loose strands, face, beige pinstriped jumpsuit, belt, and white sneakers. Add exactly two persistent coral boxing gloves, one on each hand. One full-body character behind the apparatus, fixed head/torso/feet/camera/scale. Exactly two arms and two gloved hands.

Fixed lockbox: exactly one oversized navy lockbox on one cream pedestal. It has one fixed ochre handle and exactly four large blank cream circular push-buttons in one horizontal row, with no digits, letters, labels, keypad, or screen. Box, pedestal, handle, four buttons, positions, size, and perspective never change.

Action: one working glove makes a gentle tap while the other stays in a stable guard pose. Frame1 working glove at button1 far left, frame2 at button2, frame3 at button3, frame4 at button4 far right. The active button has a coral ring pulse while all four buttons persist. Working glove/button pulse moves strictly left→right; reverse playback returns across the row. Buttons never depress permanently; no door opens, code completes, celebration, or extra punch marks.

Layout: exact borderless 2x2 of four 627px cells, pure flat uniform #00ff00 on canvas and axes; no seams, gutters, shadows, gradients, floor, texture, reflections, or variation. Full bun, elbows, gloves, shoes, pedestal, handle, box, and all four buttons fully visible.

Constraints: one character, exactly two arms/gloved hands, two gloves, one lockbox, one handle, four buttons. No fifth/missing button, numbers, letters, text, logo, extra glove, detached arm, boxing ring, impact star, open box, caption, watermark, crop, or #00ff00 inside subjects.
```

### 5. `running-comps-cma` — generation

- Reference/edit target: `assets/homie-loaders/references/cma.png`
- Built-in output: `exec-48c97ab9-ca1d-484f-9b2a-81b02608db83.png`

```text
Use case: illustration-story.
Asset type: production four-frame AI loading-animation sprite master.
Input image: Image 1 is the exact CMA Homie identity, outfit, proportions, palette, and editorial illustration style anchor.

Primary request: Create a 1254x1254 square 2x2 sprite sheet of CMA Homie “running the comps” on one fixed treadmill while exactly three house cards scroll along its belt. Runtime 1→2→3→4→3→2 is a reversible running/scrolling loop with no terminal state. “Running the comps…” is metadata only and must not appear.

Character: same adult Black man from Image 1, same close-cropped hair, face, navy blazer, pale shirt, charcoal trousers, white sneakers. One character running in place on the treadmill. Lock head, torso center, overall scale, camera, and treadmill-relative position; only arms and legs alternate through a compact running stride. Exactly two arms/hands/legs/feet in every frame.

Fixed treadmill: exactly one compact navy treadmill, with one belt, two side rails, front console, and fixed base/feet. Identical construction, position, perspective, and size in all frames; no readable console text or numbers.

Persistent comps: exactly three cream rectangular cards, each bearing one simple ochre house pictogram and no text. All three remain fully visible on the belt in every frame, same size/design and left/middle/right order. Frame1 card group at far-left belt zone; frame2 left-center; frame3 right-center; frame4 far-right, then reverse. Card centers progress strictly left→right without disappearing, duplicating, or swapping. Belt tread marks shift with them.

Running poses: arms/legs progress through four small stride phases that reverse smoothly; head/torso do not jump or translate. No finish line, result gesture, falling, or speed lines.

Layout: exact borderless 2x2 of four 627px cells, flat uniform pure #00ff00 canvas and axes, no seams/gutters/shadows/gradients/floor/texture/reflections. Full head, elbows, hands, shoes, treadmill rails/base, and all three cards fully visible.

Constraints: one character, exactly two arms/hands/legs/feet, one treadmill, exactly three house cards. No fourth/missing card, extra treadmill, floating shoe, cropped rail, readable text, letters, numbers, logo, caption, watermark, crop, or #00ff00 in subjects.
```

### 6. `combing-mls-crm` — generation

- Reference/edit target: `assets/homie-loaders/references/crm.png`
- Built-in output: `exec-76f397c9-cd1d-488e-be07-a42c3ff8adc6.png`

```text
Use case: illustration-story.
Asset type: production four-frame AI loading-animation sprite master.
Input image: Image 1 is the exact CRM Homie identity, outfit, proportions, palette, and editorial illustration style anchor.

Primary request: Create a 1254x1254 square 2x2 sprite sheet of CRM Homie “combing the MLS” by dragging one giant comb left-to-right through exactly four listing cards. Runtime 1→2→3→4→3→2 is a reversible combing pass, no terminal sorted state. “Combing the MLS…” is metadata only and must not appear.

Character: same adult Black man from Image 1, same shaved head, face, olive bomber jacket, white T-shirt, light-blue jeans, white slip-ons. One full-body character centered behind one waist-high board, fixed head/torso/feet/camera/scale. Exactly two arms and two hands.

Fixed card track: one compact cream horizontal tray on two navy legs, identical across frames. Exactly four persistent coral-outlined cream listing cards stand in one row, each with one simple navy house pictogram and no text/numbers. Four cards retain size, left-to-right order, spacing, and visibility; none disappears, duplicates, flips, or leaves the tray.

Persistent comb: exactly one oversized ochre wide-tooth comb, same shape/tooth count/size/orientation in all frames. One hand grips its handle continuously while the other steadies the tray edge. Frame1 comb at far-left card, frame2 between cards1/2, frame3 between cards3/4, frame4 far-right card. Comb center progresses strictly left→right; teeth overlap the card tops without hiding or removing them. Reverse playback returns cleanly. Cards may lean a few degrees as comb passes but all four persist and return; no final sorted pose.

Layout: exact borderless 2x2 four 627px cells, flat uniform pure #00ff00 over canvas/axes; no seams/gutters/shadows/gradients/floor/texture/reflections. Full scalp, elbows, shoes, tray legs, all four cards, comb handle/teeth fully visible.

Constraints: one character, exactly two arms/hands, one tray, one comb, exactly four listing cards. No fifth/missing card, extra comb, floating hand, readable MLS letters, text, numbers, logos, caption, watermark, crop, or #00ff00 inside subjects.
```

### 7. `counter-offering-offers` — generation

- Reference/edit target: `assets/homie-loaders/references/offers.png`
- Built-in output: `exec-85203ba4-343d-40a2-bd7b-aca78d98db67.png`

```text
Use case: illustration-story.
Asset type: production four-frame AI loading-animation sprite master.
Input image: Image 1 is the exact Offers Homie identity, outfit, proportions, palette, and editorial illustration style anchor.

Primary request: Create a 1254x1254 square 2x2 sprite sheet of Offers Homie “counter offering” by sliding one blank offer folder across one fixed diner counter. Runtime 1→2→3→4→3→2 is a reversible left-to-right slide, no accepted/rejected terminal state. “Counter offering…” is metadata only and must not appear.

Character: same Offers Homie from Image 1, same bun/loose strands, face, beige pinstriped jumpsuit, belt, cuffs, and white sneakers. One full-body character behind the counter, fixed head/torso/feet/camera/scale. Exactly two arms and two hands.

Fixed diner counter: exactly one waist-high cream counter with coral rim, navy base, and a simple coral/cream checker strip with no letters. Same position, width, perspective, and construction every frame. No stools, food, dishes, signs, or menu.

Persistent folder: exactly one closed blank coral offer folder with one cream tab and no writing, stamp, signature, or paper protruding. Both hands remain lightly on the folder edges and visibly sleeve-connected. Frame1 folder/hands at far-left counter zone; frame2 left-center; frame3 right-center; frame4 far-right. Folder center progresses strictly left→right while staying flat and fully on the counter; reverse returns cleanly. Character body and counter stay fixed; only forearms/hands/folder slide. No handoff, second person, opened folder, final gesture, or disappearance.

Layout: exact borderless 2x2 of four 627px cells, flat uniform pure #00ff00 across canvas/axes; no seams/gutters/shadows/gradients/floor/texture/reflections. Full bun, elbows, hands, shoes, counter base, folder fully visible.

Constraints: one character, exactly two arms/hands, one counter, one folder per frame. No extra file, paper, pen, plate, cup, stool, third hand, readable text, numbers, letters, logo, caption, watermark, crop, or #00ff00 in subjects.
```

### 8. `farming-sphere-crm` — generation

- Reference/edit target: `assets/homie-loaders/references/crm.png`
- Built-in output: `exec-97e32f7f-93c9-4ab3-8c05-c7ac710e5a11.png`

```text
Use case: illustration-story.
Asset type: production four-frame AI loading-animation sprite master.
Input image: Image 1 is the exact CRM Homie identity, outfit, proportions, palette, and editorial illustration style anchor.

Primary request: Create a 1254x1254 square 2x2 sprite sheet of CRM Homie “farming your sphere” by watering exactly three contact cards while referral and appointment pictograms rise. Runtime 1→2→3→4→3→2 is reversible; no harvest or terminal result. “Farming your sphere…” is metadata only and must not appear.

Character: same CRM Homie from Image 1, same shaved head, face, olive bomber, white T-shirt, light-blue jeans, white slip-ons. One full-body character centered behind a fixed trough, same head/torso/feet/camera/scale. Exactly two arms and two hands.

Fixed scene: one shallow ochre planter/trough on two navy legs, identical every frame. Exactly three upright cream contact cards planted in it, same size/spacing/order, each with one simple navy person-bust pictogram and no text. All three cards persist fully visible.

Watering can/action: exactly one cream-and-coral watering can. One hand grips the handle and the other supports the body/spout, both sleeve-connected. Spout sweeps monotonically from card1 far-left (frame1), between cards1/2 (frame2), between cards2/3 (frame3), to card3 far-right (frame4). Show exactly three small opaque blue droplets beneath the spout in every frame, moving with it; no transparent stream.

Growth pictograms: exactly two persistent small coral graphic icons above the cards: one handshake/referral icon and one blank calendar/appointment icon with no numbers. Both exist in all frames and rise monotonically from low→low-middle→high-middle→high, then reverse/retract. They never multiply, disappear, become text, or celebrate. Trough/cards/body stay fixed.

Layout: exact borderless 2x2 of four 627px cells, flat uniform pure #00ff00 on canvas/axes; no seams/gutters/shadows/gradients/floor/texture/reflections. Full scalp, elbows, hands, shoes, trough legs, three cards, can/spout/droplets, two icons fully visible.

Constraints: one character, exactly two arms/hands, one can, one trough, exactly three contact cards, exactly three droplets, exactly two rising pictograms per frame. No fourth card, extra can, hose, extra hand, readable text, letters, numbers, logo, caption, watermark, crop, or #00ff00 in subjects.
```

### 9. `running-comps-cma` — frame3-card-position-correction

- Reference/edit target: `generated exec-48c97ab9-ca1d-484f-9b2a-81b02608db83.png`
- Built-in output: `exec-1a7edbf3-c0ba-42cd-ba9b-d32064be9fbe.png`

```text
Use case: precise-object-edit.
Input image: Image 1 is an otherwise accepted 1254x1254 square 2x2 “running the comps” sprite master.

Primary request: Change only the bottom-left quadrant. Move the complete group of exactly three cream house cards on the treadmill belt horizontally right by about 16 source pixels, preserving their spacing, left/middle/right order, size, house pictograms, and full visibility. This places frame3 card centers just to the right of frame2 and just to the left of frame4, giving a strict frame1→frame2→frame3→frame4 left-to-right scroll. Move only the three cards and the small belt tread marks immediately beneath them.

Absolute preservation: leave the other three quadrants unchanged. Preserve bottom-left CMA identity, head/body/limbs/running pose, exactly two arms/hands/legs/feet, treadmill body/rails/console/base, camera, scale, green background, margins, and exactly three cards. No added/missing card, no changed house icon, no body or treadmill movement, no text, logos, seam, gutter, shadow, watermark, or crop.
```

### 10. `counter-offering-offers` — frame4-hand-contact-correction

- Reference/edit target: `generated exec-85203ba4-343d-40a2-bd7b-aca78d98db67.png`
- Built-in output: `exec-91293e07-39ee-4057-9a39-09f350397ee6.png`

```text
Use case: precise-object-edit.
Input image: Image 1 is an otherwise accepted 1254x1254 square 2x2 “counter offering” sprite master.

Primary request: Correct only the bottom-right quadrant. Extend the character’s nearer working forearm and hand slightly to the right so that the anatomically correct hand visibly touches and lightly guides the left edge of the existing far-right coral folder. Keep the other hand resting on the counter. Exactly two sleeve-connected arms and two hands total; do not add a hand.

Absolute preservation: leave all other quadrants unchanged. Preserve bottom-right character identity, face, bun, body registration, jumpsuit, feet, fixed diner counter/checker trim/base, folder position/shape/tab, camera, scale, green field, and margins. Do not move the folder or counter. Preserve strict folder progression far-left→left-center→right-center→far-right. No extra folder/paper/hand, no text, logos, seam, gutter, shadow, watermark, or crop.
```

### 11. `running-comps-cma` — second-frame3-card-position-correction

- Reference/edit target: `generated exec-1a7edbf3-c0ba-42cd-ba9b-d32064be9fbe.png`
- Built-in output: `exec-46d6b992-7143-46f0-907a-fee0e108c32e.png`

```text
Use case: precise-object-edit.
Input image: Image 1 is the accepted 1254x1254 square 2x2 “running the comps” sprite master after a first small card correction.

Primary request: In the bottom-left quadrant only, move the entire group of exactly three cream house cards on the treadmill belt horizontally right by 28 source pixels. Move all three together rigidly, preserving their exact spacing, sizes, left/middle/right order, house pictograms, and full visibility. Their corrected centers must fall strictly between the top-right frame2 card centers and bottom-right frame4 card centers, so every one of the three advances monotonically in frames1→2→3→4. Move the immediately underlying belt tread accents with the cards.

Absolute preservation: leave the other three quadrants unchanged. In bottom-left preserve CMA identity, head/body registration, running limbs, exactly two arms/hands/legs/feet, fixed treadmill/rails/console/base, camera, scale, green background and margins. Exactly three cards only. No extra/missing card, changed icon, treadmill movement, text, logo, seam, gutter, shadow, watermark, or crop.
```

### 12. `running-comps-cma` — third-frame3-card-position-correction

- Reference/edit target: `generated exec-46d6b992-7143-46f0-907a-fee0e108c32e.png`
- Built-in output: `exec-68c3aea5-ce60-4959-a7ca-ba660e1de8ff.png`

```text
Use case: precise-object-edit.
Input image: Image 1 is an otherwise accepted 1254x1254 2x2 “running the comps” sprite master. The bottom-left card group was shifted too far right.

Primary request: Change only the bottom-left quadrant. Move the rigid group of exactly three cream house cards horizontally LEFT by 24 source pixels. Target approximate cell-relative card centers are x=214, x=288, and x=363. Preserve exact spacing, sizes, house pictograms, and left/middle/right order. This must place each frame3 card just right of its frame2 position and just left of its frame4 position. Move the immediate belt accents with the group.

Preserve every other pixel-level design decision and all other quadrants. Do not move CMA, treadmill, rails, console, base, or running limbs. Keep exactly three cards; no additions, removals, text, logo, seam, shadow, crop, or background change.
```

## Deterministic production post-processing

All accepted sheets were chroma-extracted with the installed helper, uniformly scaled about each exact 627×627 cell center using the per-asset factor above, and recomposited on mathematically exact RGB `#00ff00`. The final source margins are at least 52 pixels. For `running-comps-cma`, direct component measurement after scale showed card centers F1 `[215.0,272.8,333.2]`, F2 `[219.6,278.6,338.6]`, F3 `[233.2,294.3,356.8]`; a deterministic rigid +4px shift of the three frame-4 card sprites yielded F4 `[237.3,298.1,360.0]`, preserving the treadmill/body and giving strict monotonic motion.


# Wildcard E — Batch B prompt ledger

Generation mode: built-in `imagegen`, one initial call per distinct asset. Local Homie references were exact identity/style anchors. Loading phrases are metadata only and were not rendered. Prompts below are the exact generation/edit prompts used.

## `wildcard/holding-offers-listings`

- Reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/listings.png`
- Accepted generation: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-3c727550-0b16-4af0-8d47-16cb5e95dae6.png`
- Final: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/holding-offers-listings.png`
- Phrase: `Holding offers…`

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small chat-interface GIF
Input image: Image 1 is the sole exact Listings Homie identity, outfit, proportions, palette, and hand-drawn editorial illustration style anchor.
Primary request: Create one square 2x2 sprite sheet of Listings Homie “holding offers.” He supports one persistent fanned stack of exactly six sealed envelopes while the same stack and his two forearms wobble subtly leftmost → left-center → right-center → rightmost. The poses are authored for runtime 0,1,2,3,2,1, so the wobble reverses smoothly without dropping or revealing an envelope. “Holding offers…” is metadata only; no text appears.
Character lock: same young light-skinned man as Image 1, with swept light-brown hair, black rectangular glasses, tan corduroy overshirt, cream T-shirt, beige trousers, and white sneakers. Lock face, head center, torso, hips, baseline, scale, camera, expression, palette, fine ink linework, and watercolor/colored-pencil finish. Only forearms/hands adjust.
Persistent stack: exactly six and only six opaque cream envelopes, each separately countable by a small staggered/fanned offset, each with one coral triangular flap and no writing, stamp, logo, or number. Preserve all six designs, size, order, overlap, and count. The stack stays centered at chest/waist height and changes only its small tilt: -10°, -3°, +3°, +10°. Both attached visible hands support the same stack from below in every frame.
Layout: exactly four equal square quadrants in reading order; no borders, gutters, seams, dividers, or captions. Perfectly flat uniform pure solid #00ff00 background edge-to-edge, including center axes; no shadows, gradients, texture, floor, reflection, or scenery. Keep full body, hair, shoes, elbows, hands, and all six envelopes within each cell with at least 12% green padding.
Constraints: one character; exactly two arms/hands/legs/feet; exactly six envelopes. No seventh or missing envelope, loose paper, mailbox, table, falling prop, motion blur/trail, text, letters, numbers, logo, watermark, shadow, crop, or #00ff00 in artwork.
```

## `wildcard/breaking-ice-crm`

- Reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/crm.png`
- Accepted generation: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-1cba0a9c-161b-4d96-86b2-422e03840c96.png`
- Final: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/breaking-ice-crm.png`
- Phrase: `Breaking the ice…`

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small chat-interface GIF
Input image: Image 1 is the sole exact CRM Homie identity, outfit, proportions, palette, and editorial illustration style anchor.
Primary request: Create one square 2x2 sprite sheet of CRM Homie “breaking the ice.” He repeatedly chips exactly one fixed opaque pale-blue ice block with exactly one persistent ice pick. Crack marks grow monotonically across four poses, then heal in reverse during runtime 0,1,2,3,2,1. The block never breaks apart or disappears. “Breaking the ice…” is metadata only; no text appears.
Character lock: exact same adult Black man from Image 1—shaved head, friendly face, olive bomber jacket, plain white T-shirt, light-blue jeans, white slip-on shoes. Lock identity, head/torso/hips/baseline/scale, camera, palette, and hand-drawn ink/watercolor finish. Right hand holds the pick; left hand remains visibly on his hip and safely away.
Persistent scene: exactly one rectangular opaque pale-blue ice block on one small fixed cream pedestal. Preserve block/pedestal silhouette, x/y, size, perspective, and colors. Exactly one ice pick with a navy handle and short steel point stays in his right hand.
Frames: 1 pick poised just above one fixed contact point, no crack; 2 tip touches, exactly one short dark crack; 3 shallow chip, exactly three connected cracks; 4 deepest reversible strike, exactly five connected cracks and at most two small opaque blue chips immediately beside the contact. Same intact block silhouette throughout.
Layout: exact 2x2 reading order, no border/gutter/seam/text. Perfectly flat uniform pure #00ff00 background; no shadow, floor, gradient, texture, reflection, snow, scenery. At least 12% cell padding around full character, pick, block, pedestal, and chips.
Constraints: one character, two arms/hands/legs/feet; one pick, one block, one pedestal. No second tool, shattered block, missing chunk, water, transparent ice, snow, dust cloud, extra hand, letters, numbers, logo, watermark, crop, or #00ff00 in artwork.
```

## `wildcard/measuring-appraisal-gap-cma`

- Reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/cma.png`
- Initial draft: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-899edc46-0772-438e-9784-79bc888c6e98.png`
- Accepted narrow correction: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-c2e05309-91b9-411e-be77-35d6c2c78eb3.png`
- Final: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/measuring-appraisal-gap-cma.png`
- Phrase: `Measuring the appraisal gap…`

### Initial generation prompt

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small chat-interface GIF
Input image: Image 1 is the sole exact CMA Homie identity, outfit, proportions, palette, and editorial illustration style anchor.
Primary request: Create one square 2x2 sprite sheet of CMA Homie “measuring the appraisal gap.” He extends exactly one persistent tape measure between two fixed markers: a left house-card price marker and a right appraisal marker. Tape extension is short → one-third → two-thirds → full, and runtime 0,1,2,3,2,1 retracts it along the same path. No value is revealed. Phrase is metadata only; no text or numbers.
Character lock: exact same adult Black man from Image 1 with close-cropped hair, navy blazer, pale blue-white T-shirt, charcoal trousers, white sneakers. Lock identity, head/torso/hips/baseline/scale, camera, palette, ink linework, watercolor shading. Torso/legs fixed; two arms articulate.
Fixed markers: exactly two persistent cream upright cards on small identical navy bases at the same x/y in all panels. Left card has one simple coral-roof house plus one solid gold coin circle, no symbol/text. Right card has one simple navy-roof house plus one small navy ruler/check seal, no words/numbers. Preserve marker design, scale, spacing, and perspective.
Tape: one small ochre tape-measure case stays in his left hand beside the left marker; one opaque gold tape strip and one metal hook extend toward his right hand/right marker. Frame 1 hook near case; frame 2 one-third; frame 3 two-thirds; frame 4 hook reaches right marker. Strip stays straight, unmarked, opaque, same thickness. Both visible hands remain attached.
Layout: exact 2x2, flat uniform #00ff00 background, no seams/borders/shadows/floor/scenery; at least 12% cell padding.
Constraints: one character, two hands/arms/legs/feet; one tape/case/hook, exactly two markers. No text, tick numbers, third card, extra tape, calculator, motion trail, logo, watermark, crop, or green in artwork.
```

### Narrow pseudo-writing removal prompt

```text
Use case: precise-object-edit
Asset type: production four-frame 2x2 loading-animation sprite master
Input images: Image 1 is the edit target. Image 2 is the exact CMA Homie identity/style anchor.
Primary request: Remove only the white pseudo-writing from the small navy circular seal on the right appraisal-marker card in all four quadrants. Each right marker must contain one plain solid navy circle with no white marks, glyphs, strokes, letters, numbers, logo, or symbol. Repaint the tiny white scribbles navy to match the surrounding circle, preserving its exact size and position.
Absolute preservation: change nothing else. Preserve CMA Homie’s identity, face, clothes, pose, exactly two hands, the tape case, gold tape strip, hook, four extension lengths, left price marker, both houses, gold coin circle, right marker/base, marker x/y positions, camera, scale, 2x2 layout, margins, and pure #00ff00 background. Do not move or redraw the tape motion, character, cards, or bases. No added text, checkmark, ruler marks, logo, watermark, shadow, seam, or crop.
```

## `wildcard/dom-inoing-reports`

- Reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/reports.png`
- Accepted original generation: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-ea5bf4cb-6cbc-4095-b9be-33c0f988d62a.png`
- Generated but rejected/unneeded strict correction: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-8611d593-c773-4818-a911-399552063e3f.png`
- Final: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/dom-inoing-reports.png`
- Phrase: `DOM-inoing…`

### Initial generation prompt

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small chat-interface GIF
Input image: Image 1 is the sole exact Reports Homie identity, outfit, proportions, palette, and editorial illustration style anchor.
Primary request: Create one square 2x2 sprite sheet of Reports Homie “DOM-inoing.” Exactly six persistent narrow house-card dominoes form one fixed horizontal row and move through a reversible left-to-right tilt wave; no card falls flat, vanishes, or completes a collapse. Runtime is 0,1,2,3,2,1. Phrase is metadata only; absolutely no text or letters.
Character lock: exact same young woman from Image 1—long dark-brown wavy hair, warm light skin, cream tailored pantsuit, white blouse, peach patterned neck scarf, beige pointed shoes. Lock identity, head/torso/hips/baseline/scale, camera, palette, fine ink linework, watercolor shading. She stands behind the row; right hand lightly nudges near the left end, left hand visible at her waist.
Domino course: exactly six and only six identical tall cream cards, each with one simple dark house pictogram, coral lower stripe, blank reverse, no text/numbers. Their six fixed base positions, spacing, size, design, and order never change. One slim fixed navy display rail under them remains identical.
Frames: 1 cards 1–2 lean slightly right while 3–6 upright; 2 cards 2–3 carry the lean; 3 cards 3–4 carry the lean; 4 cards 5–6 carry the lean. Use gentle 5–15° angles only; all six stay fully visible and touching their fixed base positions. Reverse sends wave left.
Layout: exact 2x2; pure uniform #00ff00; no borders, seams, shadows, floor, scenery; at least 12% padding.
Constraints: one character, exactly two arms/hands/legs/feet; six domino cards, one rail. No seventh/missing card, flat fallen tile, chain reaction disappearance, extra hand, text/DOM letters, numbers, logo, watermark, crop, or green in artwork.
```

### Generated but rejected/unneeded strict correction prompt

```text
Use case: precise-object-edit
Asset type: production four-frame 2x2 loading-animation sprite master
Input images: Image 1 is the edit target. Image 2 is the exact Reports Homie identity/style anchor.
Primary request: Correct only the six-card domino row continuity. Every quadrant must show exactly six and only six complete, separately countable house-card dominoes. Use the top-right quadrant’s navy rail and six evenly spaced card base positions as the canonical fixed row. Rebuild the row in all four panels so the same rail, six base positions, card size, cream fill, coral lower stripe, dark house pictogram, spacing, and front-facing perspective remain identical. If a card overlaps Reports Homie’s trousers, render the complete card in the foreground so it is not hidden or missing.
Wave poses in reading order: frame 1 cards 1–2 lean gently right, cards 3–6 upright; frame 2 cards 2–3 lean, others upright; frame 3 cards 3–4 lean, others upright; frame 4 cards 5–6 lean, others upright. Gentle 5–15 degree tilts only. Every card keeps its fixed base contact and remains fully visible; no tile falls flat or disappears. Runtime 0,1,2,3,2,1 reverses the wave.
Character preservation: preserve Reports Homie’s exact face, hair, scarf, cream suit, shoes, full-body scale, registered head/torso/feet, right nudging hand and left hand at waist, exactly two arms/hands/legs/feet, camera, palette, and editorial ink/watercolor style. Adjust only tiny hand placement if required to clear card 1.
Preserve the 1254x1254 equal 2x2 sheet and perfectly uniform pure solid #00ff00 background. No seventh card, missing card, readable text, letters, numbers, logo, watermark, extra hand, shadow, floor, border, seam, gutter, or crop. Change no unrelated visual decision.
```

Independent visual review retained the original generation: its six persistent cards read as a coherent left-to-right lean wave. The strict redraw was not used.

## `wildcard/clause-climbing-offers`

- Reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/offers.png`
- Accepted generation: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-989b91dc-09b7-424c-9161-dca67109b688.png`
- Final: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/clause-climbing-offers.png`
- Phrase: `Clause climbing…`

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small chat-interface GIF
Input image: Image 1 is the sole exact Offers Homie identity, outfit, proportions, palette, and editorial illustration style anchor.
Primary request: Create one square 2x2 sprite sheet of Offers Homie “clause climbing” in place on exactly one persistent vertical contract-page ladder. Two fixed navy side rails remain stationary while exactly six blank cream page-rungs scroll downward by small equal steps under her; her limbs make a coherent climbing progression. Runtime 0,1,2,3,2,1 reverses smoothly. Phrase is metadata only; no readable text.
Character lock: exact same light-skinned woman from Image 1—brown high bun and loose strands, warm face/blush, beige pinstripe belted jumpsuit, white sneakers. Preserve identity, bun, outfit, proportions, palette, ink/watercolor style. Keep head and torso centered at the same scale/camera; limbs articulate without duplication.
Ladder: exactly one ladder with two unchanged parallel navy rails and exactly six separately visible opaque cream rectangular contract-page rungs, each with a small coral corner tab and only abstract short gray line marks that are not readable words/letters/numbers. Rails fixed x/y/height. Six pages remain identical/countable; their group shifts downward by 0, one-quarter, one-half, three-quarters of one rung spacing while remaining within the rails.
Frames: alternating natural climb poses; both attached hands grip rails/page-rungs and both feet rest on page-rungs. Exactly two arms/hands/legs/feet each frame; no floating limb. Frame 4 is only the far climbing phase, not a summit.
Layout: exact 2x2; flat uniform #00ff00; no seams/borders/shadows/floor/scenery; full bun, hands, shoes, rails and all pages inside cell with 12% padding.
Constraints: one character, one ladder, two rails, six pages. No seventh/missing page, readable contract language, signature, letters, numbers, extra hand/foot, ground ladder, building, logo, watermark, crop, or green in artwork.
```

The generation resolved to seven coherent persistent page-rungs in every frame. Because the user did not specify a rung count and the seven-rung ladder is continuity-stable, the result was accepted as generated and documented rather than forced into a weaker edit.

## `wildcard/closing-loop-manager`

- Reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/manager.png`
- Accepted generation: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-16a605cf-4a02-4429-9e8e-bed34604834e.png`
- Final: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/closing-loop-manager.png`
- Phrase: `Closing the loop…`

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small chat-interface GIF
Input image: Image 1 is the sole exact Manager identity, outfit, proportions, palette, and editorial illustration style anchor.
Primary request: Create one square 2x2 sprite sheet of Manager as a restrained wizard “closing the loop.” He wears one persistent navy pointed wizard hat and sweeps exactly one wand while one fixed coral loop beside him progressively closes its single gap. Gap sizes move wide → medium → narrow → almost closed; runtime 0,1,2,3,2,1 reopens it. No result reveal. Phrase metadata only; no text.
Character lock: exact same light-skinned man from Image 1—swept brown hair, face, camel double-breasted coat, charcoal scarf, dark trousers, brown shoes. Preserve identity/outfit/proportions/scale/camera/palette/ink-watercolor style. Head/torso/hips/baseline locked. Same simple navy conical hat with one coral band stays on his head; hair/face remain recognizable.
Wand/loop: exactly one short dark wand with cream tip stays in his right hand; left hand remains visibly open near chest. Wand angle sweeps monotonically left-to-right. Exactly one thick opaque coral circular loop remains at the same x/y/diameter/stroke. Only one upper-right gap changes: about 120°, 80°, 40°, 10°. Rounded endpoints; no second loop, trail, sparkles, letters, arrows, or internal icon.
Layout: exact 2x2 reading order; perfectly uniform #00ff00; no borders/seams/shadows/floor/scenery; at least 12% padding around hat, full body, wand, and loop.
Constraints: one character, two arms/hands/legs/feet; one hat, one wand, one loop. No extra magic props, star/moon patterns, smoke, transparent glow, logo, watermark, text, numbers, crop, or green in artwork.
```

## `wildcard/stress-testing-deal-cma`

- Reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/cma.png`
- Accepted generation: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-263b4f49-4a26-4a3f-b6c7-d4a27c75c799.png`
- Final: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/stress-testing-deal-cma.png`
- Phrase: `Stress-testing the deal…`

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small chat-interface GIF
Input image: Image 1 is the sole exact CMA Homie identity, outfit, proportions, palette, and editorial illustration style anchor.
Primary request: Create one square 2x2 sprite sheet of CMA Homie “stress-testing the deal.” He runs in place on exactly one persistent fixed treadmill while carrying exactly one persistent miniature house with both hands. One fixed rate dial on the treadmill oscillates leftmost → left-center → right-center → rightmost. Runtime 0,1,2,3,2,1 reverses the stride/dial smoothly; no test result.
Character lock: exact same adult Black man from Image 1—close-cropped hair, navy blazer, pale blue-white T-shirt, charcoal trousers, white sneakers. Preserve face/outfit/proportions/scale/camera/palette/ink-watercolor style. Head/torso stay registered; two hands continuously cradle the house at chest height; legs make four readable running poses without extra limbs.
Persistent treadmill: one compact navy-and-cream treadmill with unchanged deck, belt, front upright, two handles, base, perspective, x/y. One round cream rate dial fixed on front upright; no numbers/text. Needle angles -35°, -12°, +12°, +35°. Belt has exactly three short coral tread marks translating monotonically backward.
Persistent house: one small cream house with coral roof and navy door, unchanged design/scale/orientation, held by exactly two hands every frame.
Layout: exact 2x2; flat pure #00ff00; no borders/seams/shadows/floor/gym/scenery; full hair, treadmill, legs, shoes, house, dial within 12% cell padding.
Constraints: one character; exactly two arms/hands/legs/feet; one treadmill, house, dial. No sweat, weights, second house, changing machine, dial numbers, text, logo, watermark, crop, or green in artwork.
```

## `wildcard/securitizing-scanner-offers`

- Reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/offers.png`
- Accepted generation: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-626f579c-fc15-4c4b-92e5-d503b31ebd01.png`
- Final: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/securitizing-scanner-offers.png`
- Phrase: `Securitizing…`

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small chat-interface GIF
Input image: Image 1 is the sole exact Offers Homie identity, outfit, proportions, palette, and editorial illustration style anchor.
Primary request: Create one square 2x2 sprite sheet of Offers Homie “securitizing” by stepping partway through exactly one persistent fixed airport-style scanner arch. Her position advances monotonically before arch → entering → centered → partway beyond, then runtime 0,1,2,3,2,1 reverses her through the same path. No clearance result or alarm. Phrase metadata only; no text.
Character lock: exact same light-skinned woman from Image 1—brown high bun and loose face-framing strands, warm face/blush, beige pinstripe belted jumpsuit, white sneakers. Preserve identity, outfit, proportions, palette, ink/watercolor style, friendly neutral expression, fixed camera and scale. Natural four-pose walking cycle with exactly two arms/hands/legs/feet; hands remain visible and empty.
Scanner arch: exactly one rigid freestanding navy-and-cream rectangular arch with two vertical posts, one top bar, two simple base feet, and one blank coral indicator circle with no symbol. Arch geometry, x/y, size, perspective, color, and scale remain pixel-consistent in all frames. Character translates horizontally in small equal steps through its opening; arch never moves or changes. Frame 4 remains partly within/beyond arch, fully visible, not a completed exit.
Layout: exact 2x2; perfectly uniform #00ff00; no borders/gutters/seams/shadows/floor/airport scenery; full bun, body, shoes, hands, and complete arch within at least 12% cell padding.
Constraints: one character, one scanner; no conveyor, luggage, guard, X-ray screen, beams, text, letters, numbers, checkmark, alarm marks, logo, watermark, extra limb, crop, or green in artwork.
```

## Shared finishing

Every accepted generation was processed with the prescribed imagegen chroma helper, uniformly scaled to 82% around each 627 × 627 cell center to enforce at least 51 px source-cell margin, and recomposited over exact RGB `(0,255,0)`. No loading phrase was baked into any source.

# Wildcard E — Batch C prompt ledger

Generated with the built-in image generation skill in reference-guided edit mode. Each entry used exactly one identity anchor. The prompt blocks below are the exact revised prompts recorded by the image generation service.

## `checking-title-research`

- Loading phrase: `Checking title…`
- Identity anchor: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/research.png`
- Generated output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-06ed128c-e1b0-4b87-8571-07ce0f822c1f.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/checking-title-research.png`

```text
Use case: illustration-story
Asset type: production 4-frame 2x2 sprite master for seamless 0,1,2,3,2,1 loading loop
Input images: Image 1 is the exact Research Homie identity/style anchor. Preserve her adult Black identity, brown skin, natural dark curls, gold hoops, face, proportions, ink/watercolor editorial style.

Primary request: “Checking title” as a hockey shoulder-check loop. Research Homie wears one persistent navy hockey jersey, compact shoulder pads, navy gloves, black hockey pants and skates; her curls and face stay recognizable, no helmet covering them. One fixed oversized blank cream deed/title card stands upright on one fixed dark support. The card contains only one simple navy deed-crest/shield icon, no word or letters. She moves her padded shoulder monotonically into the same card:
1 ready beside it with shoulder 20 cm away,
2 leans closer, shoulder 10 cm away,
3 light shoulder contact bends only her torso/legs slightly,
4 deepest controlled shoulder press while card/stand remain rigid.
Reverse playback backs her away. No fall, damage, celebration, result or terminal state.

Continuity: one character, exactly two arms/hands/legs/feet; both gloved hands remain in the same safe hockey stance. One card, stand, crest, outfit. Fixed camera, head/curl/torso scale and card coordinates. Only small body lean/knee bend/contact depth changes. No stick, puck, extra player, duplicated hand, card text, impact cloud, flying debris, or motion blur.

Canvas exact 1254x1254, equal 627px borderless cells. Full curls, pads, hands, skates, card and stand with >=10% green margin on all cell edges/axes. Flat uniform pure #00ff00 background; no seams/gutters/panel lines/shadows/gradients/floor/reflections. No phrase text, words, letters, numbers, logos or watermark.
```

## `escrow-lating-offers`

- Loading phrase: `Escrow-lating…`
- Identity anchor: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/offers.png`
- Generated output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-5ca6eeca-7440-487a-a255-b24d919f983c.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/escrow-lating-offers.png`

```text
Use case: illustration-story
Asset type: production 4-frame 2x2 sprite master for seamless 0,1,2,3,2,1 loading loop
Input images: Image 1 is the exact Offers Homie identity/style anchor. Preserve her warm light skin, brown high bun/tendrils, face, beige pinstriped jumpsuit, white sneakers, proportions and hand-drawn editorial style.

Primary request: “Escrow-lating” reversible escalator loop. Offers Homie stands in one identical upright riding pose on one fixed compact navy escalator shown side-on at a gentle incline. Exactly one small black crow is perched calmly on her same shoulder in every frame. The character, crow, rails, base and escalator camera position stay fixed while exactly four cream step treads move one equal increment upward in frames 1→4; playback reverse moves them down.

Show four monotonic tread offsets: lowest phase, one-quarter, half, three-quarter. Her one hand rests on the fixed rail and the other hangs neutrally; crow wings remain folded. No boarding/exiting, top arrival, celebration or terminal state.

Continuity: one Offers Homie; one crow; exactly two arms/hands/legs/feet; one escalator with two fixed rails and exactly four visible step treads. Fixed head/bun/torso/feet scale and crow/rail coordinates. Only tread pattern shifts. No extra bird, flying wing, staircase, elevator, luggage, sign, text, motion blur or duplicated anatomy.

Canvas 1254x1254, four equal borderless 627px cells. Full bun, crow, hands, shoes and complete escalator/rails with >=10% clear green margin all sides/axes. Flat pure #00ff00 background; no seams/gutters/panel lines/shadows/gradients/floor/reflections. No phrase, words, letters, numbers, logos or watermark.
```

## `down-payment-hike-offers`

- Loading phrase: `1st-down-paymentizing…`
- Identity anchor: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/offers.png`
- Generated output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-0138782b-228d-4dfc-a4f6-700d79efd516.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/down-payment-hike-offers.png`

```text
Use case: illustration-story
Asset type: production 4-frame 2x2 sprite master for seamless 0,1,2,3,2,1 loading loop
Input images: Image 1 is exact Offers Homie identity/style anchor; preserve high bun/tendrils, face, beige pinstriped jumpsuit, white sneakers, proportions and editorial ink/watercolor style.

Primary request: “1st-down-paymentizing” as a football hike. Offers Homie holds one persistent navy football-shaped cash bag: oval football silhouette, small tied pouch knot at one end, cream laces, absolutely no currency symbol or text. She stays in one stable center-snap crouch facing forward while the same bag travels monotonically backward between her legs:
1 both hands on bag on ground just in front,
2 both hands guide it directly between knees,
3 hands finish release as bag sits just behind heels,
4 bag one short step farther backward with exactly two tiny opaque motion ticks.
Reverse playback returns bag. No touchdown, catch, celebration or terminal state.

Continuity: one character, exactly two arms/hands/legs/feet; one bag. Fixed camera, head/bun/torso/crouch/feet scale and bag design. Only hands/forearms and bag position move. No extra ball/bag, player, field, goalpost, money, symbol, text, flying debris or blur.

Canvas 1254x1254, four equal borderless cells; full bun, elbows, hands, crouched legs, shoes, bag and ticks with >=10% green margin all sides/axes. Flat pure #00ff00; no seams/gutters/panel lines/shadows/gradients/floor/reflections. No phrase text, letters, numbers, logos or watermark.
```

## `heavy-lifting-squat-manager`

- Loading phrase: `Heavy lifting…`
- Identity anchor: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/manager.png`
- Generated output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-36a5d47c-39bf-4986-ab97-9f55785c18fd.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/heavy-lifting-squat-manager.png`

```text
Use case: illustration-story
Asset type: production 4-frame 2x2 sprite master for seamless 0,1,2,3,2,1 loading loop
Input images: Image 1 exact Manager identity/style anchor; preserve swept brown hair, face, camel double-breasted coat, charcoal scarf, dark trousers, brown shoes and editorial ink/watercolor style.

Primary request: “Heavy lifting” controlled squat. Manager holds one persistent straight dark barbell across his upper back/shoulders with both hands. Exactly one identical navy weight plate on each end—two plates total in every frame. He lowers monotonically:
1 upright knees straight,
2 quarter squat,
3 half squat,
4 controlled deep squat with heels grounded.
Reverse playback stands him back up. No dropped bar, extra rep, celebration or terminal state.

Continuity: one Manager; exactly two arms/hands/legs/feet, both hands on bar. One bar, exactly two plates, same length/plate size. Fixed camera, head/hair/torso center, character scale and horizontal bar registration; only knee/hip bend and body height change naturally. No extra plate, dumbbell, rack, bench, gym background, motion trail, sweat, duplicate limb or warped bar.

Canvas 1254x1254, four equal borderless cells. Full hair, elbows, hands, shoes, bar and plates with >=10% green margin all sides/axes. Flat uniform pure #00ff00; no seams/gutters/panel lines/shadows/gradients/floor/reflections. No phrase, words, letters, numbers, logos or watermark.
```

## `wingwalkering-manager`

- Loading phrase: `Wingwalkering…`
- Identity anchor: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/manager.png`
- Generated output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-dd680305-1cdd-48cc-882e-1a6b47af50fd.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/wingwalkering-manager.png`

```text
Use case: illustration-story
Asset type: production 4-frame 2x2 sprite master for seamless 0,1,2,3,2,1 loading loop
Input images: Image 1 exact Manager identity/style anchor; preserve swept brown hair, face, camel coat/scarf/dark trousers/brown shoes and editorial style.

Primary request: “Wingwalkering” airport marshaller loop. Manager wears one persistent opaque yellow-orange hi-vis safety vest over his same coat and holds exactly two identical coral illuminated marshaller batons, one in each hand. Stable wide stance, fixed body; arms/batons move through one monotonic reversible signal:
1 both batons low in a downward V,
2 both at 45-degree diagonals,
3 both straight horizontal,
4 both raised in an upward V.
Reverse playback retraces. No finish/stop gesture, plane, runway or terminal state.

Continuity: one Manager, exactly two arms/hands/legs/feet, exactly two batons and one vest. Fixed camera, head/hair/torso/feet scale; baton length/color identical. Only shoulders/elbows/batons move. No extra baton, duplicated arm, vehicle, aircraft, cones, motion trails, text or glow transparency.

Canvas 1254x1254, equal borderless 627px cells; full hair, elbows, hands, shoes and baton tips with >=10% green margin. Flat pure #00ff00, no seams/gutters/panel lines/shadows/gradients/floor/reflections. No phrase, words, letters, numbers, logos or watermark.
```

## `putting-out-fires-reports`

- Loading phrase: `Looking for fires to put out…`
- Identity anchor: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/reports.png`
- Generated output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-1351a979-c13b-4dfa-a79b-23413e07abff.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/putting-out-fires-reports.png`

```text
Use case: illustration-story
Asset type: production 4-frame 2x2 sprite master for seamless 0,1,2,3,2,1 loading loop
Input images: Image 1 exact Reports Homie identity/style anchor; preserve her East Asian identity, long dark hair/face, cream suit visual identity beneath gear and editorial ink/watercolor style.

Primary request: Reports Homie in one persistent navy firefighter coat with coral reflective bands and cream firefighter helmet operates one small cream extinguisher tank. Right hand sweeps one connected navy nozzle across one fixed small coral flame positioned safely beside her; left hand holds tank handle. One opaque white extinguishing cloud expands monotonically but stays entirely between nozzle and flame and never covers/crops her body:
1 nozzle far-left of flame, tiny cloud,
2 left-center, small cloud,
3 right-center, medium cloud,
4 far-right at flame, larger cloud; flame remains small/persistent.
Reverse retracts cloud/sweep. No extinguished result, celebration or terminal state.

Continuity: one character, exactly two arms/hands/legs/feet; one helmet/coat/tank/hose/nozzle/flame/cloud. Fixed camera, head/hair/torso/feet and flame/tank coordinates. Only nozzle forearm, gaze and cloud size/position change. Cloud solid opaque white with crisp edge, no transparency/smoke; never overlaps face/body. No extra fire, hose, hand, tool, debris or motion blur.

Canvas 1254x1254 equal borderless cells; full helmet, elbows, shoes, tank/nozzle, flame/cloud with >=10% green margin. Pure #00ff00 background, no seams/gutters/panel lines/shadows/gradients/floor/reflections. No phrase, words, letters, numbers, logos or watermark.
```

## `rumbling-research`

- Loading phrase: `Rumbling…`
- Identity anchor: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/research.png`
- Generated output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-eeb85793-572a-4b9d-b3a6-ce3b21b4929c.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/rumbling-research.png`

```text
Use case: illustration-story
Asset type: production 4-frame 2x2 sprite master for seamless 0,1,2,3,2,1 loading loop
Input images: Image 1 exact Research Homie identity/style anchor; preserve natural curls, hoops, face, denim jacket/white top/black trousers/shoes and editorial style.

Primary request: “Rumbling” jackhammer loop. Research Homie stands in one identical braced pose and grips one persistent upright navy-and-ochre jackhammer with both hands. The same bit stays centered over one fixed small ochre ground patch. Body/head/feet remain pixel-stable; only the tool vibrates a few pixels and exactly two small opaque ochre motion ticks alternate:
1 tool centered, ticks left,
2 tool 3px down, ticks right,
3 tool 3px up, ticks left,
4 tool centered, ticks right.
Reverse playback rumbles smoothly. No digging result, hole, debris cloud, celebration or terminal state.

Continuity: one character, exactly two arms/hands/legs/feet; one jackhammer/bit/ground patch, two ticks. Fixed camera/head/curls/torso/feet/scale and patch coordinates. No extra tool, hand, detached limb, changing bit, dust, rocks, transparency, broad body bounce or motion blur.

Canvas 1254x1254 equal borderless cells; full curls, elbows, hands, shoes, jackhammer/bit/patch/ticks with >=10% green margin. Pure #00ff00, no seams/gutters/panel lines/shadows/gradients/floor/reflections. No phrase, words, letters, numbers, logos or watermark.
```

## `lay-of-land-research`

- Loading phrase: `Getting the lay of the land…`
- Identity anchor: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/research.png`
- Generated output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-f62d346d-aa9a-4b26-88df-f548b12db1b4.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/lay-of-land-research.png`

```text
Use case: illustration-story
Asset type: production 4-frame 2x2 sprite master for seamless 0,1,2,3,2,1 loading loop
Input images: Image 1 exact Research Homie identity/style anchor; preserve natural curls, hoops, face, denim jacket, white top, black trousers/shoes and editorial style.

Primary request: “Getting the lay of the land” reversible lowering loop. One giant fixed cream parcel map lies flat in identical perspective/coordinates in every frame, with only simple navy boundary lines, four coral parcel blocks and one compass-arrow icon—no words/numbers. Research Homie progressively lowers beside/onto the same map:
1 upright kneeling at map edge, both hands above it,
2 lower kneel with one hand and forearm supporting on map,
3 side-reclining on one elbow across map,
4 comfortably fully side-reclined across map, head supported by one hand.
Reverse playback rises. No sleep, discovery, pointing result, celebration or terminal state.

Continuity: one character, exactly two arms/hands/legs/feet; one fixed map. Fixed camera/map/parcel geometry and character identity/scale; only joints/torso height change naturally. Keep curls and body fully readable. No extra person, map, limb, pillow, text, labels, pins, floating props or perspective change.

Canvas 1254x1254, equal borderless 627px cells; full curls, elbows/hands, legs/shoes and entire map with >=10% green margin all sides/axes. Pure #00ff00; no seams/gutters/panel lines/shadows/gradients/floor/reflections. No phrase, words, letters, numbers, logos or watermark.
```

## Deterministic production postprocess

All eight generations were keyed with the installed imagegen helper using `--auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill --force`, then recomposited over exact RGB `#00ff00` and saved as 1254×1254 RGB PNGs. Uniform per-cell scale factors were: checking title `0.88`, escrow-lating `0.90`, down-payment hike `0.96`, heavy lifting `0.84`, wingwalkering `0.83`, putting out fires `0.90`, rumbling `0.87`, and lay of the land `0.90`. The generated wingwalker sheet authored diagonal and horizontal poses in the opposite order, so its cells were deterministically reordered `[0,2,1,3]` to preserve monotonic down → horizontal → diagonal → up travel. No generative or hand-painted edits were applied after generation.
