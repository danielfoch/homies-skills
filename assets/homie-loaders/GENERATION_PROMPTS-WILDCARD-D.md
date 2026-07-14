# Wildcard D Batch A — exact built-in imagegen prompt ledger

Combined verbatim from the completed assets 1–4 and 5–8 ledgers. Loading phrases are metadata only.

# Wildcard D — Batch A assets 1–4 prompt ledger

Generation mode: built-in `imagegen`, one initial call per distinct asset. Local references were used as exact identity/style anchors. Loading phrases are metadata only and were not rendered in the artwork.

## `wildcard/context-window-shopping-listings`

- Identity/style reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/listings.png`
- Initial generated draft: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-2bd2c2a6-843e-44b4-9b20-f4ffb99088bb.png`
- Targeted edit draft: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-6e139475-701a-44a9-b51e-dbc147006b4c.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/context-window-shopping-listings.png`
- Loading phrase: `Context window shopping…`

### Initial generation prompt

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small chat-interface GIF
Input image: Image 1 is the sole exact Listings Homie identity, outfit, proportions, palette, and hand-drawn editorial illustration style anchor.

Primary request: Create one square 2x2 sprite sheet of Listings Homie “context window shopping.” He stands in one fixed position and uses both hands to carry and slide one giant empty wooden window frame horizontally past one fixed row of exactly three miniature listing cards. The four authored poses are a single monotonic left-to-right path designed to play 0,1,2,3,2,1 forever: window leftmost, left-center, right-center, rightmost. There is no terminal reveal and nothing appears or disappears. The metadata phrase is “Context window shopping…”, but absolutely no text may appear in the artwork.

Character lock: reproduce exactly the same young light-skinned man from Image 1 in every quadrant: same swept light-brown hair, black rectangular glasses, friendly face, tan corduroy overshirt with two chest pockets over a plain cream T-shirt, beige trousers, and white sneakers. Preserve his proportions, facial identity, colors, fine ink linework, and soft watercolor/colored-pencil shading. Keep his head center, torso center, hips, baseline, scale, expression, three-quarter camera, and focal length registered at the same coordinates across all four panels. Only his two forearms and hands make the small changes needed to slide the window.

Persistent object geometry: exactly one large empty warm-brown rectangular wooden window frame with four straight rails, consistent mitred corners, no glass, no inner mullions, no sill objects, and pure green visible through its opening. It remains identical in size, perspective, color, rail thickness, and front-facing orientation; only its x position moves monotonically. Listings Homie grips the left and right side rails with exactly two anatomically correct hands in every frame. Exactly three persistent small cream listing cards form one fixed evenly spaced horizontal row behind the window at lower-chest height. Each card has the same simple dark house pictogram with no letters or numbers. The three cards remain identical in count, design, scale, x/y coordinates, and order in all four frames; none is picked up, duplicated, obscured completely, or removed.

Frame 1 top-left: the window is at its leftmost position, framing the left listing card; both hands grip its side rails.
Frame 2 top-right: same character and fixed cards; the same window has moved a small equal step to left-center between the left and middle cards.
Frame 3 bottom-left: the same window has moved the next equal step to right-center between the middle and right cards.
Frame 4 bottom-right: the same window is at its rightmost position, framing the right listing card. This is merely the right endpoint of the horizontal sweep and reverses cleanly through frames 2 and 1.

Canvas and framing: exactly four equal square quadrants in standard reading order, with no drawn border, gutter, divider, panel line, or caption. The entire 1254x1254 sheet must be one perfectly flat uniform pure solid #00ff00 chroma-key field behind all artwork, including both center axes. No shadows, gradients, texture, floor plane, reflection, scenery, or green variation. Keep the complete hair, glasses, body, shoes, hands, whole window, and all three cards within each cell, with at least 10 percent clear green padding from every outer edge and center axis. Nothing crosses a cell boundary or is cropped.

Continuity and constraints: one character only; exactly two arms, two hands, two legs, and two feet in every frame; one window only; exactly three listing cards only. No extra hands, detached fingers, walking or body translation, head bounce, camera drift, window morphing, glass, curtains, house scenery, shopping bags, truck, motion blur, motion trails, sparkles, text, letters, numbers, logos, captions, watermark, shadows, seams, or crop. Do not use #00ff00 in the character, window, or cards.
```

### Targeted card/window continuity edit

```text
Use case: precise-object-edit
Asset type: production four-frame 2x2 loading-animation sprite master
Input images: Image 1 is the edit target sprite sheet. Image 2 is the sole exact Listings Homie identity/style anchor.

Primary request: Correct only the window-and-listing-card continuity in Image 1 while preserving the existing four-frame left-to-right action. In every quadrant there must be exactly three and only three identical cream miniature listing cards at exactly the same cell-relative x/y coordinates, in one evenly spaced horizontal row. Each card must retain the same dark simple house pictogram, cream square shape, brown outline, size, and orientation, with no letters or numbers. The third rightmost card must remain clearly visible in the bottom-right quadrant; it may not disappear or be completely hidden behind the window.

Window correction: retain exactly one persistent empty warm-brown rectangular wooden window frame in each panel. Make its outer width, height, four-rail construction, rail thickness, perspective, color, and scale identical in all four quadrants. Preserve the monotonic horizontal sweep leftmost → left-center → right-center → rightmost for runtime playback 0,1,2,3,2,1. Position the window vertically so its open green center spans the complete listing-card row: the bottom rail sits below the cards and the top rail sits above them, rather than cutting across or covering their centers. At every one of the four stages, at least one complete listing card is clearly visible inside the empty window opening. The window may pass in front of the row, but it may not erase, duplicate, resize, redesign, or fully conceal any of the three cards.

Character and anatomy lock: preserve the same Listings Homie from Image 1 and Image 2 in all four panels: same face, swept brown hair, black rectangular glasses, tan corduroy overshirt, cream T-shirt, beige trousers, white sneakers, proportions, full-body scale, registered head and torso, and friendly expression. Preserve exactly one character with exactly two arms, two attached visible hands, two legs, and two feet in each frame. Keep his existing natural interaction with the same window; adjust only the small arm/hand placement strictly required by the corrected window position. No walking, body translation, crop, or identity redesign.

Absolute preservation: keep the square 1254x1254 canvas, equal 2x2 reading-order layout, flat pure green background, no gutters/seams/panel lines, safe margins, camera, illustration style, palette, and all unaffected pixels as close to Image 1 as possible. Do not add glass, mullions, curtains, shopping props, fourth card, extra hand, text, letters, numbers, logo, watermark, shadow, floor, reflection, scenery, motion trail, divider, or crop. Retain a perfectly flat uniform pure solid #00ff00 background edge-to-edge and do not use #00ff00 in the character, window, or cards.
```

### Deterministic final correction

The targeted edit established the accepted window staging but still omitted the third/rightmost card in frames 2 and 4. After prescribed chroma extraction, the isolated frame-1 rightmost card was copied as an integer-only underlay at cell-relative box `(489, 316, 577, 407)` in frames 2 and 4. Existing window/character artwork was composited above it, so the card remains visibly behind the rails. No artwork was resampled or redrawn. The sheet was then recomposited over mathematical RGB `(0, 255, 0)`.

## `wildcard/prompting-a-move-manager`

- Identity/style reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/manager.png`
- Initial generated draft: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-b36db1ad-ab92-4b73-86b3-90dc1b99fbf1.png`
- Accepted framing edit: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-481fe273-7fbe-4b2d-a8c1-73984c76915b.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/prompting-a-move-manager.png`
- Loading phrase: `Prompting a move…`

### Initial generation prompt

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small chat-interface GIF
Input image: Image 1 is the sole exact Manager identity, outfit, proportions, palette, and hand-drawn editorial illustration style anchor.

Primary request: Create one square 2x2 sprite sheet of Manager “prompting a move.” He hoists one persistent oversized opaque cream prompt card cut as a clear simple house silhouette through four monotonically rising poses: hip height, waist height, chest height, overhead. The authored poses are designed to play 0,1,2,3,2,1 forever, so the same card rises and lowers smoothly without a terminal reveal. The metadata phrase is “Prompting a move…”, but no text may appear in the artwork. Do not include a moving truck or any vehicle.

Character lock: reproduce exactly the same light-skinned man from Image 1 in every quadrant: same swept brown hair, friendly face, camel double-breasted long coat, charcoal scarf, dark trousers, and brown lace-up shoes. Preserve his exact identity, proportions, palette, fine editorial ink outline, and soft watercolor/colored-pencil shading. Keep head center, torso center, hips, feet baseline, body scale, expression, straight-on three-quarter camera, and focal length fixed across all four frames. His torso does not rise, lean, or bounce; only his shoulders, two arms, and two hands articulate naturally to lift the card.

Persistent card geometry: exactly one large opaque cream card whose outer silhouette is a simple house: rectangular walls, symmetrical pitched roof, and no chimney. It is a solid flat cut-card shape, not a picture of a house and not a hollow frame. It contains no writing, symbol, door, window, line, number, or logo. Preserve its exact width, height, roof angle, cream fill, brown outline, scale, front-facing perspective, and orientation in every panel. Manager holds the same two lower side corners with exactly two anatomically correct hands throughout, with both hands visible and attached; the card never duplicates, folds, bends, rotates, or changes design.

Frame 1 top-left: the complete house-shaped card is held centered at hip height.
Frame 2 top-right: the same card is lifted one equal step to waist height.
Frame 3 bottom-left: the same card is lifted one equal step to chest height while his face remains fully visible.
Frame 4 bottom-right: arms extend upward and the same card reaches the overhead endpoint, still fully separated from his hair with green space. This is a reversible apex pose, not a final presentation.

Canvas and framing: exactly four equal square quadrants in standard reading order, no border, gutter, divider, panel line, or caption. Use one perfectly flat uniform pure solid #00ff00 chroma-key field edge-to-edge behind all artwork, including the center axes. No shadows, gradients, texture, floor plane, reflection, scenery, or lighting variation. Scale the complete scene consistently so Manager’s full hair, coat, shoes, extended hands, and overhead card remain inside every cell with at least 10 percent clear green padding from every outer edge and center axis. Nothing crosses a quadrant boundary or is cropped.

Continuity and constraints: one character only; exactly two arms, two hands, two legs, and two feet per panel; exactly one house-shaped prompt card. No extra fingers, detached arms, hidden duplicate hand, changing coat length, body jump, head bounce, camera drift, second card, paper stack, building, truck, vehicle, road, furniture, motion blur, motion marks, text, letters, numbers, logos, watermark, shadow, seam, gutter, or crop. Do not use #00ff00 in the character or card.
```

### Accepted uniform-framing correction

```text
Use case: precise-object-edit
Asset type: production four-frame 2x2 loading-animation sprite master
Input images: Image 1 is the edit target. Image 2 is the sole exact Manager identity/style anchor.

Primary request: Correct only the uniform framing and cell-boundary clearance of Image 1. The bottom-right overhead-card pose currently extends upward across the invisible horizontal center axis, causing the roof tip to leak into the bottom edge of the top-right quadrant and the top of the bottom-right artwork to be clipped at its cell edge. Reframe all four complete panel scenes with one identical uniform smaller scale factor so every entire Manager and entire house-shaped card fits comfortably inside its own 627x627 quadrant. Use the same scale factor for all four panels so the character and card remain exactly the same size frame-to-frame. Center each complete scene within its own quadrant while keeping the character head/torso/baseline registered as consistently as the action permits. Leave at least 50 pixels of perfectly flat green padding between all artwork and every outer canvas edge and both invisible center axes. Erase the stray roof fragment from the bottom of the top-right cell because it belongs only to the bottom-right overhead pose. Nothing may touch or cross a quadrant boundary.

Action and geometry lock: preserve exactly the current monotonic card hoist in reading order: hip height, waist height, chest height, overhead. Preserve exactly one persistent opaque cream house-silhouette prompt card with the same width, height, pitched-roof angle, brown outline, front-facing orientation, and relative scale in all four frames. Preserve Manager’s exact face, swept brown hair, camel double-breasted coat, charcoal scarf, dark trousers, brown shoes, proportions, friendly expression, two arms, two visible attached hands, two legs, and two feet. Keep both hands holding the same card. The runtime remains 0,1,2,3,2,1 with no reveal.

Absolute preservation: do not redesign, recolor, crop, fold, rotate, or replace the character or card. Do not add a truck, building, second card, text, letters, numbers, logo, watermark, shadow, floor, scenery, motion marks, panel border, divider, seam, or gutter. Retain the exact square 1254x1254 canvas, equal 2x2 reading-order layout, editorial ink-and-watercolor style, and perfectly flat uniform pure solid #00ff00 background edge-to-edge. Change only the uniform per-panel scale/framing required to create safe cell margins.
```

The accepted framing edit was processed with the prescribed chroma helper and recomposited over exact RGB `(0, 255, 0)` without further artwork changes.

## `wildcard/model-home-training-research`

- Identity/style reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/research.png`
- Initial generated draft: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-b916f0fc-3c8f-465a-97c5-f3e7ac5e25fd.png`
- Rejected generative hoop-registration edit: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-4197fca0-ca98-470b-8de2-7ec727e91f98.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/model-home-training-research.png`
- Loading phrase: `Model-home training…`

### Initial generation prompt

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small chat-interface GIF
Input image: Image 1 is the sole exact Research Homie identity, outfit, proportions, palette, and hand-drawn editorial illustration style anchor.

Primary request: Create one square 2x2 sprite sheet of Research Homie conducting “model-home training.” She remains one fixed trainer while exactly three persistent miniature model houses advance monotonically left-to-right as a tight train through exactly two fixed search hoops. She holds exactly one small navy trainer baton that points along their route. The four poses are designed for the seamless runtime order 0,1,2,3,2,1: houses at far-left approach, passing hoop one, traveling between hoops, passing hoop two/right endpoint. Every house, hoop, and baton persists; there is no finish-line reveal and nothing appears or disappears. The metadata phrase is “Model-home training…”, but absolutely no text may appear.

Character lock: reproduce exactly the same adult Black woman from Image 1 in every quadrant: same voluminous natural dark curls, face, warm skin tone, gold hoop earrings, pale-blue denim jacket, plain white top, black wide-leg trousers, and black loafers. Preserve her identity, proportions, palette, fine editorial ink linework, and soft watercolor/colored-pencil shading. Keep her head, curls silhouette, torso, hips, feet baseline, scale, friendly focused expression, three-quarter camera, and focal length registered at identical coordinates. She stands just behind the training lane. Her right hand holds the one baton and tracks the houses with a small left-to-right pointing sweep; her left hand stays visibly on her hip. Exactly two arms and two hands remain visible.

Persistent course geometry: exactly two identical large navy circular hoops on two simple short cream floorless stands, fixed side-by-side at lower-body height. Their ring diameter, outline, stand geometry, x/y coordinates, perspective, and spacing never change. Exactly three persistent small solid cream model houses travel as one evenly spaced train. Each has the same simple pitched roof, square body, one coral door, and no text, windows, sign, base, card, or wheels. Preserve each house’s individual silhouette, colors, scale, spacing, order, and upright orientation; the entire three-house formation translates right by equal steps. All three houses remain fully visible in every frame, including when passing through a hoop; no overlap hides a house completely. Exactly one small straight navy trainer baton remains in the same right hand, with unchanged length, thickness, and color.

Frame 1 top-left: all three houses approach from the left, with the lead house just before fixed hoop one; baton points leftward toward them.
Frame 2 top-right: the formation shifts one equal step right; the lead house passes through hoop one while the other two follow, all three still visible.
Frame 3 bottom-left: the formation shifts the next equal step right; the houses occupy the space between the two fixed hoops, with one house near each ring.
Frame 4 bottom-right: the formation shifts the final equal step right; the lead portion passes through hoop two and the three houses remain visible near the right endpoint. The loop then reverses through the same poses.

Canvas and framing: exactly four equal square quadrants in standard reading order, with no drawn border, gutter, divider, panel line, or caption. The entire 1254x1254 sheet is a perfectly flat uniform pure solid #00ff00 chroma-key field, including all center-axis pixels. No shadows, gradients, texture, floor plane, scenery, reflection, or green variation. Keep all curls, body, shoes, baton, three houses, and both complete hoops within every cell with at least 10 percent clear green padding from outer edges and center axes. Nothing crosses or is cropped.

Continuity and constraints: one character only; exactly two arms, two hands, two legs, and two feet per frame; exactly three houses; exactly two hoops; exactly one baton. No whistle, lanyard, fourth house, duplicate house, house disappearance, hoop morphing, extra ring, obstacle, finish line, platform, card, letters, numbers, logos, text, watermark, motion trail, shadow, divider, seam, gutter, or crop. Do not use #00ff00 anywhere in the character, houses, hoops, stands, or baton.
```

### Targeted hoop-registration edit prompt

```text
Use case: precise-object-edit
Asset type: production four-frame 2x2 loading-animation sprite master
Input images: Image 1 is the edit target sprite sheet. Image 2 is the sole exact Research Homie identity/style anchor.

Primary request: Correct only the fixed search-hoop registration in Image 1. The current three-house left-to-right progression is excellent and must remain exactly as authored. In the top-left quadrant, the two navy search hoops and their cream two-post stands show the canonical fixed course positions and geometry. Keep that top-left frame unchanged. In the top-right, bottom-left, and bottom-right quadrants, place the left hoop-and-stand and right hoop-and-stand at exactly the same cell-relative x/y coordinates as their corresponding hoops in the top-left quadrant. Both complete hoops must remain perfectly stationary across all four panels. Preserve their exact oval ring size, navy outline thickness, cream stand height, two-post construction, small base, front-facing perspective, spacing, palette, and proportions. Do not move the houses to follow the hoops.

Absolute house-motion lock: preserve exactly three and only three cream miniature houses in every panel, including each house’s current cell-relative x/y position, order, upright orientation, pitched roof, coral door, scale, spacing, and current monotonic left-to-right advancement. Frame 1 remains the far-left approach, frame 2 remains the next rightward step, frame 3 the next step, and frame 4 the rightmost step for the runtime sequence 0,1,2,3,2,1. Do not add, erase, duplicate, resize, rotate, or reposition any house. When a fixed hoop overlaps a moving house, keep the house visibly passing through the ring with the ring outline cleanly readable; do not hide the entire house.

Character and baton lock: preserve Research Homie exactly from Image 1 and Image 2 in all panels: same face, voluminous curls, skin tone, gold hoop earrings, light-blue denim jacket, white top, black wide-leg trousers, black loafers, full-body scale, registered head/torso/feet, friendly focused expression, and one small navy baton in her right hand with her left hand on her hip. Preserve exactly one character with exactly two arms, two visible attached hands, two legs, and two feet. Do not change her pose, baton, camera, framing, or identity.

Preserve the 1254x1254 square, equal 2x2 reading-order layout, illustration style, safe margins, and perfectly flat uniform pure solid #00ff00 background edge-to-edge. No panel borders, gutters, seams, floor, shadow, gradient, reflection, text, letters, numbers, logos, watermark, fourth house, third hoop, whistle, motion marks, or crop. Change only the three drifting instances of the left hoop-and-stand and any tiny surrounding green pixels strictly required to register them; keep every other visual decision as close to Image 1 as possible.
```

### Deterministic final correction

The targeted edit did not move the drifting left hoop and was rejected. The final uses the initial accepted artwork after prescribed chroma extraction. Frame 1 supplied the canonical disconnected Research character/baton component, two complete hoop/stand components, and three complete house components. In every frame, only that frame’s character/baton component was retained; both canonical hoops were placed at frame-1 integer coordinates; and the three canonical houses were integer-translated horizontally to target center positions `[213,272,326]`, `[320,396,457]`, `[343,429,512]`, and `[372,441,522]`. No component was scaled, rotated, resampled, or redrawn. The rebuilt sheet was recomposited over exact RGB `(0, 255, 0)`.

## `wildcard/depolarizing-parka-offers`

- Identity/style reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/offers.png`
- Accepted generated artwork: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-21b143af-3fcc-4dc3-9265-20f75c0c0856.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/depolarizing-parka-offers.png`
- Loading phrase: `De-polarizing…`

### Initial and accepted generation prompt

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small chat-interface GIF
Input image: Image 1 is the sole exact Offers Homie identity, underlying outfit, proportions, palette, and hand-drawn editorial illustration style anchor.

Primary request: Create one square 2x2 sprite sheet of Offers Homie “de-polarizing” by putting on one persistent oversized navy winter parka with one tan fur-trimmed hood. The four monotonically advancing dressing poses are: holding the open parka, one arm inserted, both arms inserted with hood down, hood up. They are designed to play 0,1,2,3,2,1 forever so the same coat goes on and comes off along one reversible path; no garment appears or disappears and there is no terminal reveal. The metadata phrase is “De-polarizing…”, but no text may appear.

Character lock: reproduce exactly the same young light-skinned woman from Image 1 in every quadrant: same warm face and blush, brown hair in the same high bun with the same loose face-framing strands, small earrings, beige pinstripe belted jumpsuit with two chest pockets, rolled cuffs, and white sneakers. Preserve her exact facial identity, body proportions, underlying outfit, palette, fine editorial ink linework, and soft watercolor/colored-pencil shading. The jumpsuit must remain visibly recognizable beneath the open parka throughout. Keep her head center, torso center, hips, feet baseline, scale, expression, straight-on three-quarter camera, and focal length registered across all frames. Her bun must remain present and recognizable even when the hood is raised.

Persistent parka geometry: exactly one oversized navy parka with the same long body, two sleeves, open front, two simple patch pockets, and one attached hood edged by the same tan opaque fur trim. Preserve the coat’s navy color, tan trim, pocket count, hem length, sleeve length, scale, stitching, and overall silhouette throughout; it changes pose only as it is put on. No second coat, no detached hood, no zipper pull, no scarf, no gloves.

Frame 1 top-left: she stands fixed and holds the same open parka in front of and slightly beside her with both anatomically correct hands gripping its upper edges; both empty sleeves and the tan-trimmed hood are clearly visible.
Frame 2 top-right: her right arm is fully inserted into the right sleeve and its hand is visible at the cuff; her left hand holds the open left side/sleeve ready. The same jumpsuit remains visible.
Frame 3 bottom-left: both arms are fully inserted and both hands are visible at their cuffs; the parka is worn open with the hood down behind her neck, high bun fully visible.
Frame 4 bottom-right: the same parka remains worn open and both hands remain visible; its attached tan-trimmed hood is now raised around her head while the same high bun remains clearly recognizable above or within the generous hood opening. This reversible endpoint lowers back through frames 3, 2, and 1.

Canvas and framing: exactly four equal square quadrants in standard reading order, with no drawn border, gutter, divider, panel line, or caption. Use one perfectly flat uniform pure solid #00ff00 chroma-key background edge-to-edge, including both center axes. No shadow, gradient, texture, floor plane, reflection, scenery, snow, weather, or lighting variation. Show her complete bun, body, shoes, hands, parka hem, sleeves, and hood inside each cell with at least 10 percent clear green padding from outer edges and center axes. Nothing crosses a boundary or is cropped.

Continuity and anatomy constraints: one character only; exactly two arms, two hands, two legs, and two feet in every frame. Exactly one parka with two sleeves and one attached hood. No extra arm inside a sleeve, detached hand, duplicate bun, hidden third hand, jacket under the parka, garment morphing, changing pocket count, closed zipper, mittens, hat, scarf, second coat, clothing rack, hanger, polar bear, snowflake, ice, weather, motion blur, text, letters, numbers, logos, watermark, shadow, panel border, gutter, seam, or crop. Do not use #00ff00 in the character or parka.
```

The accepted artwork was processed with the prescribed chroma helper and recomposited over exact RGB `(0, 255, 0)` without further artwork changes.

# Wildcard D Batch A — assets 5–8 prompt ledger

Generation mode: built-in `image_gen`. Loading phrases are metadata only and are not rendered in the artwork.

## `wildcard/deed-tecting-research`

- Identity/style anchor: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/research.png`
- Initial output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-e302686e-857c-476f-8dad-fbea6c68081a.png`
- Accepted framing edit: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-4121d877-898d-4e93-9839-654569bc2674.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/deed-tecting-research.png`
- Loading phrase: `Deed-tecting…`

### Original generation prompt

```text
Use case: illustration-story
Asset type: production four-frame 2x2 sprite master for a seamless chat loading loop
Input images: Image 1 is the exact Research Homie identity and visual-style anchor. Preserve her adult Black identity, warm brown skin, voluminous natural dark curls, gold hoop earrings, light-blue denim jacket, white top, black wide-leg trousers, black shoes, facial features, proportions, fine ink linework, and soft editorial watercolor/pencil shading. Do not redesign her.

Primary request: Create one coherent monotonic “deed-tecting” action designed specifically for playback 0,1,2,3,2,1. Research Homie wears the same playful tan detective deerstalker hat and short tan detective cape in every frame while dusting one fixed oversized blank cream deed sheet mounted on one fixed wooden easel. She uses exactly one small soft fingerprint-dusting brush. A compact cluster of exactly three opaque coral fingerprint icons travels with the brush monotonically from the far-left portion of the blank deed to left-center, right-center, and far-right across frames 1–4. The reverse playback sweeps the same cluster back. The deed must remain completely blank: no names, letters, lines, numbers, seals, or readable marks other than the three simple fingerprint icons.

Frame order, top-left to bottom-right:
1. Brush and the same three fingerprint icons at the far-left inspection point of the deed.
2. Brush and the same three icons at the left-center point.
3. Brush and the same three icons at the right-center point.
4. Brush and the same three icons at the far-right inspection point.
This is a cyclic scan pose, not a discovery, completion, or celebration state. Her gaze follows the brush. Only her working forearm/hand, brush, gaze, and icon cluster move as required.

Continuity lock: one Research Homie only; exactly two arms, two hands, two legs, and two feet in every frame. The non-working hand rests in the same neutral position on the easel edge. Exactly one persistent hat, one persistent cape, one brush, one easel, one blank deed, and exactly three fingerprint icons. Keep identical fixed straight-on three-quarter camera, character head coordinates, curl silhouette, torso, feet baseline, scale, easel coordinates, deed dimensions, perspective, palette, and prop design in all four cells. No camera drift, zoom, body bounce, prop morphing, duplicated hands, extra fingers, extra brush, extra easel, changing paper size, floating tools, dust clouds, or terminal reveal.

Canvas/layout: exact 1254x1254 square, four equal 627x627 quadrants in a borderless 2x2 grid, standard reading order. Keep the full scalp/hat, cape, elbows, hands, shoes, brush, easel, deed, and icons fully inside each cell with at least 8 percent clear green margin from outer edges and both invisible center axes. Nothing crosses or touches a cell boundary; no crop.

Background: perfectly flat, mathematically uniform pure #00ff00 edge-to-edge in every quadrant and across both center axes. No gutters, seams, panel lines, frames, shadows, gradients, texture, floor plane, reflections, halos, or lighting variation. Do not use #00ff00 in the character or props.

Text: none. Do not render “Deed-tecting…”, names, letters, words, numbers, logos, captions, ellipses, UI, or watermark.
Style/finish: exact charming hand-drawn editorial illustration style of Image 1, crisp coherent silhouettes and persistent prop continuity.
```

### Targeted framing correction prompt

```text
Use case: precise-object-edit
Asset type: production four-frame 2x2 sprite master
Input images: Image 1 is the accepted deed-tecting sprite sheet edit target. Image 2 is the exact Research Homie identity/style anchor.

Primary request: Change only the framing scale in Image 1. Uniformly scale the complete artwork cluster in each of the four quadrants down to approximately 88 percent of its current size, centered on the same scene center, so every frame has at least 52 pixels of clear green margin from all four edges of its own 627x627 cell.

Required result: the full detective hat, curls, cape, elbows, hands, shoes, brush, all three fingerprint icons, complete easel clamp, deed, and bottoms of every easel leg must be fully visible and uncropped in every cell. Nothing may touch or cross the outer canvas edges or invisible center axes. Use the identical scale factor in all four cells.

Absolute preservation lock: keep the four current monotonic brush/icon positions, exactly three coral fingerprint icons per frame, the completely blank deed, exactly one character with two arms and two hands, detective hat and cape, face, curls, clothes, expression, brush, easel, paper, perspective, camera, relative positions, colors, and all action content unchanged. Do not add, remove, redesign, or move any prop independently; do not change the sequence; no terminal state.

Keep the 1254x1254 equal 2x2 layout and perfectly uniform pure #00ff00 background. No text, names, letters, numbers, logos, shadows, gutters, seams, panel lines, border, floor, watermark, or extra objects.
```

## `wildcard/zoning-out-research`

- Identity/style anchor: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/research.png`
- Built-in output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-74ca5587-2104-46ec-a898-508a209d261d.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/zoning-out-research.png`
- Loading phrase: `Zoning out…`

```text
Use case: illustration-story
Asset type: production four-frame 2x2 sprite master for a seamless chat loading loop
Input images: Image 1 is the exact Research Homie identity and visual-style anchor. Preserve her adult Black identity, warm brown skin, voluminous natural dark curls, gold hoop earrings, light-blue denim jacket, white top, black wide-leg trousers, black shoes, facial features, proportions, fine ink linework, and soft editorial watercolor/pencil shading. Do not redesign her.

Primary request: Create a coherent monotonic “zoning out” loop designed for playback 0,1,2,3,2,1. Research Homie stands in one identical thoughtful pose in every frame, one hand lightly at her chin and the other arm folded across her torso, gazing into space. Exactly four persistent miniature zoning blocks orbit together in one curved arc around the outside of her curls. The four blocks are simple opaque building-lot shapes with four fixed colors—one coral, one ochre, one navy, one cream—and remain individually recognizable, same size, same order, same design, and exactly four total in every frame.

Monotonic frame arc, top-left to bottom-right:
1. The same four-block arc occupies the far-left side of her head/curls.
2. The unchanged four-block arc has advanced clockwise to the upper-left/top arc.
3. The unchanged four-block arc has advanced across the upper-right arc.
4. The unchanged four-block arc occupies the far-right side of her head/curls.
Reverse playback returns the same arc smoothly from right to left. No terminal state, conclusion, pop, disappearance, or celebration. Only the four-block cluster’s orbital position changes; her entire pose stays fixed.

Continuity lock: one Research Homie only; exactly two arms, two hands, two legs, and two feet in every frame. Exactly four zoning blocks, never three or five. Keep identical fixed straight-on camera, head/curl silhouette coordinates, face, gaze, thoughtful hand pose, torso, clothing, legs, shoes baseline, scale, lighting, and palette in all cells. Keep block colors/order/shape/orientation coherent. No camera drift, zoom, body bounce, duplicated hand, extra fingers, extra person, extra blocks, vanished block, letters, map, sign, house, orbit trail, sparkles, motion blur, or terminal state.

Canvas/layout: exact 1254x1254 square, four equal 627x627 cells in a borderless 2x2 grid, standard reading order. Keep full curls, elbows, hands, shoes, and all blocks fully inside their cells with at least 8 percent clear green margin from outer edges and both invisible center axes. Nothing crosses or touches a boundary; no crop.

Background: perfectly flat mathematically uniform pure #00ff00 edge-to-edge in every cell and across center axes. No gutters, seams, panel lines, borders, shadows, gradients, texture, floor plane, reflections, halos, or lighting variation. Do not use #00ff00 in the character or blocks.

Text: none. Do not render “Zoning out…”, words, letters, numbers, logos, captions, ellipses, UI, or watermark.
Style/finish: exact charming hand-drawn editorial illustration style of Image 1, crisp coherent silhouettes and a clearly readable back-and-forth orbit.
```

## `wildcard/looking-under-asking-research`

- Identity/style anchor: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/research.png`
- Built-in output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-cd005293-42fb-4334-acd9-cb0bfab8c8fd.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/looking-under-asking-research.png`
- Loading phrase: `Looking under asking…`

```text
Use case: illustration-story
Asset type: production four-frame 2x2 sprite master for a seamless chat loading loop
Input images: Image 1 is the exact Research Homie identity and visual-style anchor. Preserve her adult Black identity, warm brown skin, voluminous natural dark curls, gold hoop earrings, light-blue denim jacket, white top, black wide-leg trousers, black shoes, facial features, proportions, fine ink linework, and soft editorial watercolor/pencil shading. Do not redesign her.

Primary request: Create one coherent monotonic “looking under asking” flashlight-scan loop designed for playback 0,1,2,3,2,1. Research Homie remains in the same stable crouched pose beneath one fixed oversized blank coral price-tag-shaped placard mounted on one fixed compact dark stand. The placard has a clear tag silhouette with one small punched hole but is otherwise completely blank. She holds exactly one small navy flashlight in one hand; her other hand rests in the same safe neutral position on her bent knee. One short opaque pale-cream flashlight beam sweeps left-to-right across the underside of the sign.

Frame order, top-left to bottom-right:
1. Same crouched pose; flashlight and beam aimed at the far-left underside of the fixed tag.
2. Same pose; beam aimed at the left-center underside.
3. Same pose; beam aimed at the right-center underside.
4. Same pose; beam aimed at the far-right underside.
Reverse playback sweeps the beam smoothly back. No discovery, completion, reveal, celebration, or terminating pose. Only the flashlight hand/forearm, gaze, and beam angle move as required.

Continuity lock: one Research Homie only; exactly two arms, two hands, two legs, and two feet in each frame. Exactly one persistent flashlight, one opaque beam, one coral tag placard, and one compact support stand. Keep identical fixed straight-on camera, head/curl coordinates, crouched torso, legs, feet baseline, facial identity, clothing, scale, tag position/size/perspective, stand coordinates, lighting, and palette in all four cells. Keep the same non-working hand on the same knee. No camera drift, zoom, body bounce, duplicated hand, extra fingers, extra flashlight, extra beam, extra sign, changing tag shape, detached limbs, floating props, magnifying glass, numbers, symbols, or terminal state.

Canvas/layout: exact 1254x1254 square, four equal 627x627 cells in a borderless 2x2 grid, standard reading order. Keep full curls, elbows, hands, crouched legs, shoes, flashlight, full beam, tag edges/hole, and full stand inside each cell with at least 8 percent clear green margin from outer edges and both invisible center axes. Nothing touches or crosses a cell boundary; no crop.

Background: perfectly flat mathematically uniform pure #00ff00 edge-to-edge in all cells and across center axes. No gutters, seams, panel lines, borders, shadows, gradients, texture, floor plane, reflections, halos, or lighting variation. The flashlight beam must be a short solid opaque cream graphic with crisp edges, not translucent, and must not touch an edge. Do not use #00ff00 in the character or props.

Text: none. Keep the price tag absolutely blank. Do not render “Looking under asking…”, price, currency symbol, number, word, letter, logo, caption, ellipsis, UI, or watermark.
Style/finish: exact charming hand-drawn editorial illustration style of Image 1, crisp coherent silhouettes and a readable reversible left-to-right scan.
```

## `wildcard/forecasting-market-reports`

- Identity/style anchor: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/reports.png`
- Initial output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-1215abfb-9261-49cd-9fd6-4c3e270240c0.png`
- Pointer correction output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-cf9a90ac-7bf3-464d-bd52-f99721b4aacf.png`
- Pointer-connection output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-45c1f74f-6d9c-497f-bb16-d3ca5747e655.png`
- Detached-line deletion output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-c8f78685-6e80-473e-8ef0-9598aa0eeaa5.png`
- Accepted replacement generation: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-c9dc3a77-777f-4558-bf11-b3cc906dadb4.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/forecasting-market-reports.png`
- Loading phrase: `Forecasting the market…`

### Initial generation prompt

```text
Use case: illustration-story
Asset type: production four-frame 2x2 sprite master for a seamless chat loading loop
Input images: Image 1 is the exact Reports Homie identity and visual-style anchor. Preserve her adult East Asian identity, warm light skin, long dark-brown wavy hair, friendly face, cream/beige tailored pantsuit, white blouse, peach patterned neck scarf, beige pointed shoes, slim proportions, fine dark linework, and soft editorial watercolor/colored-pencil shading. Do not redesign her.

Primary request: Create one coherent monotonic “forecasting the market” board scan designed for playback 0,1,2,3,2,1. Reports Homie stands beside one fixed compact cream weather-map board on one fixed small dark stand. She holds exactly one slim coral pointer in one hand; her other hand rests in the same neutral position on the board edge. The board contains exactly three persistent simple opaque graphic icons and no others: one navy house icon, one coral directional arrow icon, and one combined ochre cloud-with-sun icon. No words or map labels.

Monotonic frame arc, top-left to bottom-right:
1. Pointer tip indicates the leftmost house icon; all three icons at 94% pulse scale.
2. Pointer sweeps to the left-center/between house and arrow; all three icons at 98% scale.
3. Pointer sweeps to the right-center/between arrow and cloud-sun; all three icons at 102% scale.
4. Pointer indicates the rightmost cloud-sun icon; all three icons at 106% scale.
The reverse playback sweeps the pointer back and gently reverses the same pulse. No finishing gesture, result reveal, celebration, or terminal state. Only her pointer arm/gaze and the tiny synchronized icon pulse may change.

Continuity lock: one Reports Homie only; exactly two arms, two hands, two legs, and two feet in each frame. Exactly one persistent board, one stand, one pointer, and exactly three icons: house, arrow, cloud-with-sun. Keep identical fixed straight-on three-quarter camera, head/hair coordinates, face, torso, legs, shoes baseline, scale, suit/scarf design, board coordinates/size/perspective, stand, icon order/centers/colors, lighting, and palette in all four cells. The icon pulse is subtle and centered in place, not travel. No camera drift, zoom, body bounce, duplicated hand, extra finger, extra pointer, extra board, extra icon, changing icon identity, map text, weather words, numbers, floating props, motion trails, or terminal state.

Canvas/layout: exact 1254x1254 square, four equal 627x627 quadrants in a borderless 2x2 grid, standard reading order. Keep full hair, elbows, hands, shoes, pointer, board, icons, and full stand inside each cell with at least 8 percent clear green margin from outer edges and both invisible center axes. Nothing touches or crosses a boundary; no crop.

Background: perfectly flat mathematically uniform pure #00ff00 edge-to-edge in all cells and across center axes. No gutters, seams, panel lines, borders, shadows, gradients, texture, floor plane, reflections, halos, or lighting variation. Do not use #00ff00 in the character or props.

Text: none. Do not render “Forecasting the market…”, weather labels, map labels, words, letters, numbers, logos, captions, ellipses, UI, or watermark.
Style/finish: exact charming hand-drawn editorial illustration style of Image 1, crisp coherent silhouettes, fixed board geometry, and readable reversible pointer sweep.
```

### Pointer-geometry correction prompt

```text
Use case: precise-object-edit
Asset type: production four-frame 2x2 sprite master
Input images: Image 1 is the forecasting-board sprite sheet edit target. Image 2 is the exact Reports Homie identity/style anchor.

Primary request: Correct only the coral pointer geometry across the four frames so it forms one clear monotonic left-to-right scan. Each frame must contain exactly one single continuous slim coral pointer held in the same working hand, with no duplicate line, spare pointer, detached stroke, or V shape.

Required pointer-tip positions in reading order:
1. Top-left: keep the single pointer tip centered on the navy house icon.
2. Top-right: move only the pointer tip to the blank midpoint between the house and coral arrow icons.
3. Bottom-left: move only the pointer tip to the blank midpoint between the coral arrow and ochre cloud-sun icons.
4. Bottom-right: keep one pointer tip centered on the ochre cloud-sun icon, and completely remove the existing extra detached lower coral pointer stroke so only the hand-connected pointer remains.
The pointer arm may make only the small coherent angle changes required. Reverse playback must scan back smoothly.

Absolute preservation lock: change no other content. Preserve Reports Homie’s exact face, hair, body, pose, cream suit, scarf, anatomy, non-working hand, scale, camera, feet, one fixed board and stand, exactly three icons and their current designs/order/colors/sizes, green margins, 2x2 layout, and all pixels unrelated to the pointer correction. Do not add or remove any icon. Exactly two arms and two hands in every frame.

Keep the 1254x1254 canvas and uniform pure #00ff00 background. No text, words, numbers, labels, logos, gutters, seams, panel lines, shadows, watermark, or extra objects.
```

### Pointer-connection correction prompt

```text
Use case: precise-object-edit
Asset type: production four-frame 2x2 sprite master
Input images: Image 1 is the forecasting-board sprite sheet edit target. Image 2 is the exact Reports Homie identity/style anchor.

Primary request: Make exactly one small continuity repair in the bottom row only. In both the bottom-left and bottom-right quadrants, the existing single coral pointer line is detached from Reports Homie’s working hand. Extend only the left/base end of that same existing pointer line until it connects naturally and continuously into the pointer grip in her working hand. Preserve the existing pointer tip locations: bottom-left remains aimed between the arrow and cloud-sun; bottom-right remains aimed at the cloud-sun. Each bottom frame must show exactly one continuous straight pointer from her hand to its current tip, with no second line, no fork, no V, and no detached segment.

Absolute preservation lock: do not change the top row. In the bottom row preserve the character face, long hair, body, pose, both hands, cream suit, scarf, board, stand, exactly three icons, icon positions/design/colors, pointer tip locations, camera, scale, margins, and all content except the small missing connection between working hand and existing pointer base. Do not add a hand or pointer.

Keep the exact 1254x1254 2x2 layout and flat pure #00ff00 background. No text, numbers, labels, logos, seams, gutters, panel lines, shadows, watermark, or extra objects.
```

### Detached-line deletion prompt

```text
Use case: precise-object-edit
Asset type: production four-frame 2x2 sprite master
Input images: Image 1 is the original forecasting-board sprite sheet edit target. Image 2 is the exact Reports Homie identity/style anchor.

Primary request: Make exactly one tiny deletion in the bottom-right quadrant only. That frame currently contains the correct coral pointer continuously held by Reports Homie and aimed at the ochre cloud-sun icon, plus one erroneous second detached lower coral diagonal stroke beneath it. Remove only the detached lower coral diagonal stroke that begins on the board away from her hand. Repaint that narrow removed area with the exact surrounding blank cream board fill. Retain the one correct hand-connected pointer unchanged from her working hand to the cloud-sun icon. The final bottom-right frame must contain exactly one pointer.

Absolute preservation lock: change nothing else in any quadrant. Preserve every character pixel, face, hair, pose, two hands, cream suit, scarf, board, stand, exactly three icons, all other pointer geometry, camera, scale, margins, palette, and original 2x2 layout. Do not move any pointer tip, hand, arm, or icon. Do not add a second line or prop.

Keep the exact 1254x1254 sheet and flat pure #00ff00 background. No text, numbers, labels, logos, seams, gutters, panel lines, shadows, watermark, or extra objects.
```

### Accepted replacement generation prompt

```text
Use case: illustration-story
Asset type: production four-frame 2x2 sprite master for a seamless 0,1,2,3,2,1 chat loading loop
Input images: Image 1 is the exact Reports Homie identity/style anchor. Reproduce the same adult East Asian woman with warm light skin, long dark-brown wavy hair, friendly face, cream tailored pantsuit, white blouse, peach neck scarf, beige shoes, proportions, ink linework, and soft editorial watercolor/pencil finish.

Primary request: Reports Homie performs one simple left-to-right pointer scan across one fixed compact cream forecast board on one fixed dark stand. The board contains exactly three fixed opaque icons in a horizontal row: navy house on the left, coral arrow in the center, ochre cloud-with-sun on the right. No text. She grips exactly one single straight coral pointer in her right hand in every frame. The pointer must be one uninterrupted physical stick whose base is visibly enclosed by that same hand and whose tip visibly touches the requested target. Never draw a second line or detached stroke.

Four poses, reading order:
1. Top-left: the one hand-connected pointer tip touches the center of the left house.
2. Top-right: the same one hand-connected pointer tip touches the left edge of the center arrow.
3. Bottom-left: the same one hand-connected pointer tip touches the right edge of the center arrow.
4. Bottom-right: the same one hand-connected pointer tip touches the center of the right cloud-sun.
This is one monotonic sweep; reverse playback sweeps back. Her right forearm angle changes smoothly to carry the pointer. Her left hand stays fixed on the top-left corner of the board. Her gaze follows the tip. No terminal pose or celebration.

Critical pointer rule: exactly one pointer per quadrant. It is a single continuous straight coral shaft from inside her right-hand grip all the way to its target. No spare pointer, no double line, no V shape, no floating segment, no detached stroke, no motion trail, no pointer drawn behind the board.

Continuity: exactly one Reports Homie, two arms, two hands, two legs, two feet. Identical fixed camera, head/hair coordinates, torso, scale, feet baseline, board coordinates/dimensions/perspective, stand, and three icon designs/positions in every frame. Keep icons the same size; their “gentle pulse” is conveyed only by tiny opaque two-line emphasis ticks beside each icon that grow subtly from one short tick in frame 1 to two short ticks in frames 2–3 and one short tick in frame 4, while all icons remain fixed. No body bounce, camera shift, duplicated anatomy, extra icon, labels, map, floating prop, or endpoint celebration.

Canvas: exact square 1254x1254, four equal 627x627 cells in a borderless 2x2 reading-order grid. Fit the complete character, hair, both arms/hands, shoes, pointer, board, all icons, and full stand inside every cell with at least 10% clear green margin from outer edges and both invisible center axes. Nothing touches/crosses an edge; no crop.

Background: perfectly flat uniform pure #00ff00 edge-to-edge, including both center axes. No gutters, seams, panel lines, border, shadows, gradients, floor, texture, reflection, halo, or lighting variation. Do not use green in subject/props.
No text: do not render “Forecasting the market…”, words, letters, numbers, labels, logo, watermark, caption, or UI.
Style: exact charming hand-drawn editorial illustration of Image 1, clean production sprite consistency.
```

## Deterministic production post-processing

All accepted built-in outputs were processed with the installed imagegen chroma helper using `--auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill`, then composited onto exact RGB `(0, 255, 0)`. Uniform cell-centered scaling preserved content while meeting margins: deed 1.00, zoning 0.88, looking-under-asking 0.90, forecasting 0.88.

## Final aggregate margin normalization

After combining both halves, strict pixel QA applied a final uniform cell-centered framing fit to the first four accepted masters so every authored cell clears the integer equivalent of the requested 8% margin: context-window-shopping 0.925, prompting-a-move 0.87, model-home-training 0.89, and depolarizing-parka 0.85. This deterministic post-processing did not change pose order, prop counts, identities, or prompt content.

# Wildcard D — Batch B assets 1–4 prompt ledger

Generation mode: built-in `imagegen`, one initial call per distinct asset. Local Homie references were exact identity/style anchors. Loading phrases are metadata only and were not rendered.

## `wildcard/surveying-situation-cma`

- Reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/cma.png`
- Accepted generation: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-8a070ec2-8868-49fb-897b-63b32cca13fb.png`
- Final: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/surveying-situation-cma.png`
- Phrase: `Surveying the situation…`

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small chat-interface GIF
Input image: Image 1 is the sole exact CMA Homie identity, outfit, proportions, palette, and hand-drawn editorial illustration style anchor.

Primary request: Create one square 2x2 sprite sheet of CMA Homie “surveying the situation” through exactly one persistent fixed tripod surveyor scope. The scope pivot, tripod, two property stakes, and boundary line stay fixed while only the scope barrel and his tracking gaze pan monotonically leftmost → left-center → right-center → rightmost. The four poses are authored for seamless runtime playback 0,1,2,3,2,1, so the final pose is merely the right endpoint of a reversible scan, not a reveal or conclusion. The loading phrase is metadata only; absolutely no text may appear.

Character lock: reproduce exactly the same adult Black man from Image 1 in every quadrant: same close-cropped dark hair, friendly face, warm skin tone, navy blazer, pale blue-white crew-neck T-shirt, charcoal trousers, and white lace-up sneakers. Preserve his exact facial identity, body proportions, palette, fine dark editorial ink linework, and soft watercolor/colored-pencil shading. Keep his head center, torso center, hips, feet baseline, scale, three-quarter camera, and focal length registered at essentially identical cell-relative coordinates. His torso and legs remain still. His near eye stays naturally aligned to the eyepiece while his gaze and head angle make only the tiny horizontal tracking change required by the pan.

Persistent apparatus: exactly one professional surveyor scope with one long cream-and-navy barrel, one small eyepiece, one focus ring, one horizontal pan handle, one central pivot housing, and exactly one rigid navy tripod with three clearly readable legs. The pivot housing, tripod hub, all three legs, their feet, scale, perspective, x/y coordinates, and colors remain mechanically identical in every frame. The barrel rotates only around the fixed pivot in the horizontal plane; it never changes length, diameter, design, height, or handedness. CMA Homie uses exactly two anatomically correct hands in every frame: one hand remains on the same pan handle and the other lightly steadies the same focus ring.

Fixed property markers: exactly two and only two short ochre property stakes stand beyond the tripod, connected by exactly one thin taut coral boundary line. Both stakes and the one line remain identical in design, length, spacing, scale, and cell-relative x/y coordinates in all four panels. No extra stake, fence post, sign, flag, label, number, house, or landscape.

Frame 1 top-left: barrel and gaze at the leftmost scan angle, about 18 degrees left of center.
Frame 2 top-right: same fixed apparatus and markers; barrel and gaze at left-center, about 6 degrees left of center.
Frame 3 bottom-left: barrel and gaze at right-center, about 6 degrees right of center.
Frame 4 bottom-right: barrel and gaze at the rightmost scan angle, about 18 degrees right of center. The runtime then reverses through frames 3, 2, and 1.

Canvas and framing: exactly four equal square quadrants in standard reading order, with no drawn border, panel line, gutter, seam, divider, or caption. Use one perfectly flat uniform pure solid #00ff00 chroma-key background edge-to-edge, including both center axes. No shadow, gradient, texture, floor plane, reflection, scenery, horizon, or lighting variation. Keep the complete scalp, full body, shoes, both hands, whole scope barrel, eyepiece, handle, all three tripod legs, both stakes, and line fully within each cell with at least 10 percent clear green padding from every outer edge and center axis.

Continuity and anatomy constraints: one character only; exactly two arms, two hands, two legs, and two feet in each frame; exactly one scope and one tripod; exactly two stakes and one line. No duplicated hand, detached finger, extra lens, second scope, changing tripod, moving stakes, motion trail, blur, arrows, text, letters, numbers, logo, watermark, cast shadow, reflection, panel border, crop, or #00ff00 inside the character or props.
```

The accepted artwork was chroma-extracted, uniformly scaled to 82% around each 627 × 627 cell center to enforce at least 51 px source margin, and recomposited over exact RGB `(0,255,0)`.

## `wildcard/sifting-listings-listings`

- Reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/listings.png`
- Accepted generation: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-fe9d34d2-4d88-4737-9d1d-f53c31c71401.png`
- Final: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/sifting-listings-listings.png`
- Phrase: `Sifting the listings…`

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small chat-interface GIF
Input image: Image 1 is the sole exact Listings Homie identity, outfit, proportions, palette, and hand-drawn editorial illustration style anchor.

Primary request: Create one square 2x2 sprite sheet of Listings Homie “sifting the listings” with exactly one persistent prospector pan containing exactly five persistent miniature listing/house cards and exactly three persistent solid gold sparkle shapes. The same pan rocks monotonically tilt-left → near-left → near-right → tilt-right while every card and sparkle follows coherently inside or just above the pan. The authored poses are designed for runtime playback 0,1,2,3,2,1; frame 4 is only the right endpoint of the rocking motion and reverses cleanly. No card is selected or revealed. The loading phrase is metadata only; no text may appear.

Character lock: reproduce exactly the same young light-skinned man from Image 1 in every quadrant: same swept light-brown hair, black rectangular glasses, friendly face, tan corduroy overshirt with two chest pockets, plain cream T-shirt, beige trousers, and white sneakers. Preserve his exact identity, proportions, palette, fine ink linework, and soft watercolor/colored-pencil shading. Keep his head center, torso center, hips, feet baseline, body scale, expression, three-quarter camera, and focal length registered across all panels. His torso and legs remain fixed; only his two forearms and hands make the small rocking movement.

Persistent pan and contents: exactly one broad shallow charcoal prospector pan with one ochre rim, two small side grips, and the same oval perspective, diameter, depth, colors, and design in all four frames. Listings Homie holds the two side grips with exactly two visible attached hands in every frame. Exactly five and only five small cream listing cards are fanned across the pan interior and remain individually visible in every frame. Each card has one simple dark house pictogram, a thin brown outline, and no letters or numbers. Preserve all five cards’ count, size, design, order, and identity; they shift and tilt coherently with the pan but never leave it, overlap completely, duplicate, or disappear. Exactly three and only three small opaque gold four-point sparkle shapes hover immediately above the pan contents; all three persist, remain separate, and rock with the pan. No dust or translucent particles.

Frame 1 top-left: pan at its clear leftmost tilt, about 14 degrees down on the left; all five cards and three sparkles visibly follow the tilt.
Frame 2 top-right: same pan and contents at a shallow near-left tilt, about 5 degrees left.
Frame 3 bottom-left: same pan and contents at a shallow near-right tilt, about 5 degrees right.
Frame 4 bottom-right: same pan and contents at its clear rightmost tilt, about 14 degrees down on the right; this reverses through frames 3, 2, and 1.

Canvas and framing: exactly four equal square quadrants in reading order, no border, panel line, gutter, seam, divider, or caption. Use one perfectly flat uniform pure solid #00ff00 chroma-key field edge-to-edge behind all artwork, including the center axes. No shadow, gradient, texture, floor plane, reflection, scenery, or lighting variation. Keep the complete hair, glasses, full body, shoes, elbows, hands, pan, all five cards, and three sparkles inside every cell with at least 10 percent clear green padding from outer edges and center axes.

Continuity and constraints: one character only; exactly two arms, two hands, two legs, and two feet per frame; exactly one pan, five listing cards, and three gold sparkles. No sixth card, missing card, extra sparkle, nugget, gravel, water, shovel, pickaxe, table, motion blur, translucent dust, text, letters, numbers, logos, watermark, shadow, panel border, crop, or #00ff00 inside the character or props.
```

The accepted artwork was chroma-extracted, uniformly scaled to 82% around each cell center, and recomposited over exact RGB `(0,255,0)`.

## `wildcard/keying-criteria-listings`

- Reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/listings.png`
- Initial draft: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-a83a1782-8b7d-45af-92d1-e7f5edffbe94.png`
- Seven-key correction draft: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-4d04876f-3c6c-43a8-b20a-299ec836e9ad.png`
- Seven/eight alternating correction draft used for final deterministic fix: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-aa509ca1-3a59-46d5-ac05-38fca3f521aa.png`
- Final: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/keying-criteria-listings.png`
- Phrase: `Keying in the criteria…`

### Initial generation prompt

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small chat-interface GIF
Input image: Image 1 is the sole exact Listings Homie identity, outfit, proportions, palette, and hand-drawn editorial illustration style anchor.

Primary request: Create one square 2x2 sprite sheet of Listings Homie “keying in the criteria” on exactly one persistent fixed oversized keyboard whose eight pressable keycaps are unmistakable brass house-door key silhouettes. His two hands and the active pair of depressed keys travel monotonically left-to-right across four poses. The sequence is authored for runtime playback 0,1,2,3,2,1, so frame 4 is simply the rightmost typing pose and reverses cleanly; there is no submission or final result. The loading phrase is metadata only and no text may appear.

Character lock: reproduce exactly the same young light-skinned man from Image 1 in every quadrant: same swept light-brown hair, black rectangular glasses, friendly focused face, tan corduroy overshirt with two chest pockets, plain cream T-shirt, beige trousers, and white sneakers. Preserve identity, proportions, palette, fine editorial ink outline, and soft watercolor/colored-pencil shading. Keep head center, torso center, hips, feet baseline, scale, expression, straight-on three-quarter camera, and focal length fixed. He stands behind the keyboard in one stable pose; only his forearms, two hands, and depressed key depth change.

Persistent keyboard geometry: exactly one wide cream-and-tan keyboard console with one rigid rectangular deck and two small integrated support feet. The complete deck, feet, perspective, x/y coordinates, size, colors, and geometry remain identical in every panel. It contains exactly eight and only eight identical brass house-door key silhouettes arranged horizontally as eight separate oversized pressable keycaps. Each keycap clearly has one round bow, one straight shaft, and one toothed end; no letters, numbers, labels, regular square computer keys, or house-shaped buildings. Preserve all eight keys’ count, design, scale, spacing, order, and x/y slots in every frame. Only the currently pressed adjacent pair sits a few pixels lower; all other keys remain raised and visible.

Hand progression: both anatomically correct hands remain visible above the deck and press exactly two adjacent keys in every panel. Frame 1 top-left: hands press keys 1 and 2 at the far left. Frame 2 top-right: hands press keys 3 and 4 at left-center. Frame 3 bottom-left: hands press keys 5 and 6 at right-center. Frame 4 bottom-right: hands press keys 7 and 8 at the far right. The hands and depressed pair move in one monotonic path; runtime reversal types back across the same keyboard. No key is removed, duplicated, launched, or replaced.

Canvas and framing: exactly four equal square quadrants in reading order, with no drawn border, panel line, gutter, seam, divider, or caption. Use one perfectly flat uniform pure solid #00ff00 chroma-key background edge-to-edge, including both center axes. No shadow, gradient, texture, floor plane, reflection, scenery, office, or lighting variation. Keep complete hair, glasses, full body, shoes, elbows, both hands, whole keyboard deck, both feet, and all eight brass keycaps inside every cell with at least 10 percent clear green padding from every outer edge and center axis.

Continuity and anatomy constraints: one character only; exactly two arms, two hands, two legs, and two feet per frame; one keyboard only; exactly eight brass key keycaps. No extra hand, floating finger, ninth key, disappearing key, typewriter, laptop, screen, mouse, table, loose key, key ring, house model, text, letters, numbers, logo, watermark, motion trail, shadow, panel border, crop, or #00ff00 inside the character or keyboard.
```

### First key-count/console correction prompt

```text
Use case: precise-object-edit
Asset type: production four-frame 2x2 loading-animation sprite master
Input images: Image 1 is the edit target sprite sheet. Image 2 is the sole exact Listings Homie identity/style anchor.

Primary request: Correct only the persistent oversized keyboard geometry, brass-key count, and hand progression in Image 1. The top-left quadrant shows the canonical wide cream keyboard console and a complete row of exactly eight brass house-door key silhouettes. Preserve that same console and rebuild every quadrant so all four panels contain exactly eight and only eight persistent brass keys at the same eight cell-relative x/y slots. No key may disappear, duplicate, merge, or move to a different slot.

Canonical console lock: copy the top-left panel’s complete rigid cream rectangular keyboard deck, ochre outline, two integrated support feet, width, height, front-facing perspective, scale, colors, and cell-relative x/y position into the top-right, bottom-left, and bottom-right panels. The deck and feet must be mechanically identical and perfectly stationary in all four frames. Remove the vertical seam or split currently visible in the top-right deck; every frame uses one uninterrupted console. Do not resize, shorten, lengthen, tilt, or redraw the table geometry differently between panels.

Eight-key lock: use exactly eight identical persistent brass house-door key silhouettes in one evenly spaced horizontal row on the deck. Each key has one round bow, one straight shaft, and one toothed end. Preserve one fixed design, size, upright orientation, gold color, outline, spacing, and slot for keys 1 through 8. All eight remain visibly readable in every frame, including beneath the hands. Do not substitute regular computer keys, buildings, key rings, letters, or numbers.

Hand/action progression: preserve exactly two anatomically correct visible hands and two arms per panel. The hands press the adjacent pair that travels monotonically left-to-right: frame 1 top-left presses keys 1 and 2; frame 2 top-right presses keys 3 and 4; frame 3 bottom-left presses keys 5 and 6; frame 4 bottom-right presses keys 7 and 8. The active pair may sit only a few pixels lower in its fixed slots while the other six keys remain raised. Keep each hand attached to its arm and positioned above its active key; do not add fingers, hands, pointers, loose keys, or motion trails. Runtime reversal 0,1,2,3,2,1 types back across the same fixed eight-key row.

Character preservation: preserve Listings Homie’s exact face, swept brown hair, black rectangular glasses, tan corduroy overshirt, cream T-shirt, beige trousers, white sneakers, full-body scale, registered head/torso/feet, focused expression, camera, and editorial ink-and-watercolor style from Image 1 and Image 2. Keep one character only, exactly two arms, two hands, two legs, and two feet. Adjust only the forearm/hand x positions required to press the correct pair.

Preserve the exact 1254x1254 square, equal 2x2 reading-order layout, safe margins, and perfectly flat uniform pure solid #00ff00 chroma background edge-to-edge. No border, gutter, seam, divider, floor, shadow, reflection, text, letters, numbers, logo, watermark, second console, laptop, mouse, typewriter, extra key, missing key, or crop. Change no unrelated visual decision.
```

### Second narrow seven-to-eight correction prompt

```text
Use case: precise-object-edit
Asset type: production four-frame 2x2 loading-animation sprite master
Input images: Image 1 is the edit target. Image 2 is the exact Listings Homie identity/style anchor.

Primary request: Make exactly one narrow correction to Image 1: each keyboard currently has seven brass house-door key silhouettes. Change the key row in every quadrant to contain exactly eight and only eight separate brass keys. Add exactly one eighth key and redistribute the eight identical keys evenly across the existing cream deck so all eight fit comfortably between the left and right deck edges. Use the same eight fixed cell-relative x/y slots in all four panels. Every key must remain individually visible and countable.

Key design lock: preserve the existing brass key design exactly—one round bow, straight vertical shaft, toothed end, ochre-gold fill, dark outline, same size, same upright orientation. All eight keys are identical in design and spacing. No key overlaps another, hides behind another, disappears, merges, changes shape, or extends beyond the deck. Do not add a ninth key. Do not turn them into square keyboard keys, houses, letters, or numbers.

Absolute preservation: preserve the current uninterrupted cream console/deck, two support feet, width, height, perspective, x/y position, colors, and outline exactly in all four panels. Preserve Listings Homie’s face, hair, glasses, tan overshirt, white shirt, beige trousers, shoes, body, camera, and all four current arm/hand poses exactly. Preserve exactly two attached visible hands per frame and the existing left-to-right hand progression. Do not move, redraw, resize, or recolor the character, hands, console, feet, canvas, or any unrelated pixel except where the seven-key row must become eight evenly spaced keys.

Keep the exact 1254x1254 equal 2x2 layout and perfectly flat uniform pure solid #00ff00 background. No text, letters, numbers, logo, watermark, extra hand, loose key, key ring, shadow, floor, seam, gutter, divider, border, or crop. The only intended visual change is seven persistent keys becoming exactly eight persistent keys in each of the four panels.
```

### Deterministic final correction

The second edit produced eight keys in frames 2 and 4 but seven in frames 1 and 3. After prescribed chroma extraction, one unobstructed canonical brass key was isolated from frame 2 by a saturation/color mask and integer-translated into the same unused far-left deck slot `(48, canonical-y)` in frames 1 and 3. No existing key, hand, console, or character pixel was moved or resampled during that correction. All four complete cells were then uniformly scaled to 82% around their centers and recomposited over exact RGB `(0,255,0)`.

## `wildcard/room-inating-listings`

- Reference: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/listings.png`
- Accepted generation: `/Users/danielfoch/.codex/generated_images/019f554b-a553-7e53-8c4d-d7afd35001fc/exec-63e2a258-afa3-4e3d-adf1-9853a81d9306.png`
- Final: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/room-inating-listings.png`
- Phrase: `Room-inating…`

```text
Use case: illustration-story
Asset type: production four-frame loading-animation sprite master for a small chat-interface GIF
Input image: Image 1 is the sole exact Listings Homie identity, outfit, proportions, palette, and hand-drawn editorial illustration style anchor.

Primary request: Create one square 2x2 sprite sheet of Listings Homie “room-inating” in one perfectly fixed thinker pose while exactly four persistent miniature room icons travel monotonically as one ordered group along an invisible arc from the left side of his head, over his head, to the right side. The four icons are exactly one bed, one sofa, one bathtub, and one stove. The authored positions are designed for runtime playback 0,1,2,3,2,1, so the group glides back along the same arc with no final decision, reveal, or disappearing icon. The loading phrase is metadata only; no text may appear.

Character lock and thinker pose: reproduce exactly the same young light-skinned man from Image 1 in every quadrant: same swept light-brown hair, black rectangular glasses, thoughtful friendly face, tan corduroy overshirt with two chest pockets, plain cream T-shirt, beige trousers, and white sneakers. Preserve his exact identity, body proportions, palette, fine editorial ink linework, and soft watercolor/colored-pencil shading. His full-body thinker pose is identical in every frame: right elbow supported by his crossed left forearm, right hand resting at his chin, left hand visible near the opposite elbow, exactly two arms and two hands. Lock head center, hair, glasses, torso, hips, feet baseline, scale, expression, three-quarter camera, and focal length to the same coordinates. The character does not move at all.

Persistent icon set: exactly four and only four small opaque editorial miniatures, always in the same clockwise order: (1) one cream bed with ochre pillow, (2) one coral sofa, (3) one pale-blue claw-foot bathtub, and (4) one navy-and-cream stove with four simple top circles and no labels. Each icon remains individually recognizable, separate, upright, and identical in design, scale, orientation, color, and order in every frame. All four icons stay visible; none overlaps another completely, morphs, duplicates, disappears, or changes category. There is no thought bubble, orbit line, connector, room outline, floor, or extra furniture.

Arc progression: Frame 1 top-left: all four icons occupy four evenly spaced positions along the left/lower-left arc beside the head. Frame 2 top-right: the entire ordered group has shifted one equal clockwise step and spans upper-left to top-center. Frame 3 bottom-left: the group shifts the next equal step and spans top-center to upper-right. Frame 4 bottom-right: the group reaches the right/upper-right arc beside the head. This is the right endpoint only; runtime reversal retraces frames 3, 2, and 1. The group’s motion is monotonic and the character remains perfectly fixed.

Canvas and framing: exactly four equal square quadrants in reading order, no drawn border, panel line, gutter, seam, divider, or caption. Use one perfectly flat uniform pure solid #00ff00 chroma-key background edge-to-edge, including both center axes. No shadow, gradient, texture, floor plane, reflection, scenery, room, or lighting variation. Scale and position the complete scene so full hair, full body, shoes, both hands, and all four icons remain inside every cell with at least 10 percent clear green padding from all outer edges and center axes.

Continuity and constraints: one character only; exactly two arms, two hands, two legs, and two feet in every frame; exactly four icons total: one bed, one sofa, one tub, one stove. No fifth icon, duplicate furniture, missing icon, thought cloud, light bulb, question mark, sparkle, motion trail, arrows, text, letters, numbers, logo, watermark, shadow, panel border, crop, or #00ff00 inside the character or icons.
```

The accepted artwork was chroma-extracted, uniformly scaled to 82% around each cell center, and recomposited over exact RGB `(0,255,0)`.

# Wildcard D Batch B — assets 5–8 exact prompt ledger

Generation mode: built-in `image_gen`. Loading phrases are metadata only and are not rendered.

## `wildcard/raising-roof-cma`

- Anchor: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/cma.png`
- Built-in output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-dc97faa3-1856-4b21-b51f-cfc15ad60861.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/raising-roof-cma.png`
- Loading phrase: `Raising the roof…`

```text
Use case: illustration-story
Asset type: production four-frame 2x2 sprite master for a seamless 0,1,2,3,2,1 loading loop
Input images: Image 1 is the exact CMA Homie identity/style anchor. Preserve the same adult Black man, warm brown skin, close-cropped dark hair, friendly face, navy blazer, pale blue-white T-shirt, charcoal trousers, white sneakers, proportions, editorial ink linework, and soft watercolor/pencil shading.

Primary request: Create a reversible “raising the roof” loop. One fixed compact cream miniature house body sits on one fixed small dark pedestal beside CMA Homie. Exactly one separate navy roof piece belongs to that house. CMA Homie grips the same roof piece with both hands and raises it monotonically above the fixed house, designed for playback 0,1,2,3,2,1.

Frames in reading order:
1. Roof held just above the miniature house body, nearly seated.
2. Same roof lifted to his hip/waist height.
3. Same roof lifted to his chest/shoulder height while he inspects it.
4. Same roof lifted overhead, still centered above the unchanged house body.
Reverse playback lowers the roof along the same path. No installed/finished reveal, celebration, new roof, or terminal state.

Continuity lock: one CMA Homie only, exactly two arms/hands/legs/feet; both hands remain on the one roof. Exactly one house body, one roof, one pedestal. Fixed camera, head/torso coordinates, character scale, feet baseline, pedestal and house coordinates, roof design/size/color/perspective. Only arms and roof height change. No camera drift, body bounce, duplicated hands, extra roof, changing house, hammer, ladder, crane, debris, motion trail, or floating prop.

Canvas: exact 1254x1254, four equal 627x627 cells in a borderless 2x2 grid. Fit full head, elbows, hands, shoes, roof at every height, full miniature house and pedestal with at least 10% clear green margin from every cell edge and both center axes. No crop or crossing.

Background: perfectly flat uniform pure #00ff00 edge-to-edge including center axes. No gutters, seams, panel lines, border, shadows, gradients, floor, texture, reflection, or lighting variation. No green in subject/props.
Text: none. Do not render “Raising the roof…”, words, letters, numbers, logos, captions, watermark, or UI.
Style: exact charming hand-drawn editorial illustration of Image 1, crisp persistent props and a clear monotonic reversible lift.
```

## `wildcard/cooking-price-cma`

- Anchor: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/cma.png`
- Built-in output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-42a12990-e7bd-4422-a47d-ed431da98a7b.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/cooking-price-cma.png`
- Loading phrase: `Cooking up a price…`

```text
Use case: illustration-story
Asset type: production four-frame 2x2 sprite master for a seamless 0,1,2,3,2,1 loading loop
Input images: Image 1 is the exact CMA Homie identity/style anchor. Preserve the same adult Black man, close-cropped dark hair, friendly face, navy blazer, pale blue-white T-shirt, charcoal trousers, white sneakers, proportions, ink linework, and soft editorial watercolor/pencil finish.

Primary request: Create a reversible “cooking up a price” loop. CMA Homie stands behind one fixed large navy cooking pot on one fixed compact cream work surface. He holds exactly one wooden spoon in his right hand and continuously stirs the same three opaque pricing/property icons inside the pot: exactly one miniature cream house, one blank coral price-tag shape, and one ochre coin circle with no symbol. His left hand stays on the same pot handle.

Four monotonic stirring poses:
1. Spoon tip at far-left inside the pot; three icons cluster left in fixed order.
2. Spoon and same icons move to left-center.
3. Spoon and same icons move to right-center.
4. Spoon and same icons move to far-right.
Playback reverses the identical stir path. No finished dish, tasting, steam finale, serving, celebration, or terminal pose. The icons stay visible above the pot rim, same count/design/order, moving with the stir.

Continuity: one CMA Homie, exactly two arms/hands/legs/feet; one spoon, one pot, one work surface, exactly three icons. Fixed camera, head/torso coordinates, scale, feet baseline, table/pot coordinates, pot shape/handles, icon designs/colors. Only right forearm/spoon, gaze, and icon cluster travel left-to-right. No extra utensil, hand, ingredient, pot, fire, stove, food, liquid splash, translucent steam, motion trail, text, or terminal state.

Canvas: exact 1254x1254 with four equal 627x627 cells in borderless reading-order 2x2. Full hair, elbows, hands, shoes, spoon, icons, pot and complete work surface fit with at least 10% green margin from all cell edges/center axes. No crop/crossing.
Background: flat mathematically uniform pure #00ff00 edge-to-edge including axes. No seams, gutters, panel lines, shadows, gradients, floor, texture, reflection, or green in props.
Text: none. Do not render “Cooking up a price…”, symbols, currency, words, letters, numbers, labels, logos, watermark, or UI.
Style: exact editorial illustration style of Image 1, clean persistent geometry and monotonic reversible stirring.
```

## `wildcard/price-ceiling-offers`

- Anchor: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/offers.png`
- Built-in output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-554ac1b3-e8ea-4c47-806c-f1a0637ad727.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/price-ceiling-offers.png`
- Loading phrase: `Finding the price ceiling…`

```text
Use case: illustration-story
Asset type: production four-frame 2x2 sprite master for seamless 0,1,2,3,2,1 loading loop
Input images: Image 1 is the exact Offers Homie identity/style anchor. Preserve the same woman’s warm light skin, brown high bun and loose tendrils, friendly face, beige pinstriped utility jumpsuit, white sneakers, proportions, ink linework, and soft editorial watercolor/pencil shading.

Primary request: Create a reversible “finding the price ceiling” pulley loop. One fixed short dark overhead ceiling beam spans above Offers Homie with exactly one fixed navy pulley wheel. One continuous cream rope passes over it. A single large blank coral price-tag shape hangs from one side; Offers Homie grips the free rope end with both hands on the other side and pulls it monotonically so the tag rises.

Frames:
1. Tag hangs near shin/knee height; her hands hold rope high.
2. Tag rises to waist height; hands pull down slightly.
3. Tag rises to chest height; hands pull down farther.
4. Tag reaches just below the fixed beam/ceiling; hands are lowest.
Reverse playback lowers it. No final attachment, price reveal, celebration, cut rope, or terminal state.

Continuity: one Offers Homie; exactly two arms/hands/legs/feet; both hands on one rope. Exactly one beam, pulley, rope, and blank tag. Fixed camera, head/high-bun coordinates, torso, scale, feet baseline, beam/pulley coordinates, rope path, tag design. Only hands/forearms, free rope end, gaze, and tag height change. No extra rope, pulley, tag, hook, ladder, number, currency, text, duplicated anatomy, or motion trail.

Canvas: exact 1254x1254, four equal 627x627 cells borderless. Full bun, elbows, hands, shoes, beam, pulley, rope and tag fit with at least 10% green margin from every cell edge and center axes. No crop/crossing.
Background: perfectly flat pure #00ff00 edge-to-edge including axes. No seams, gutters, panel lines, borders, shadows, gradients, floor, texture, reflections, or green in props.
Text: none; tag completely blank. Do not render “Finding the price ceiling…”, symbols, words, numbers, logos, watermark, or UI.
Style: exact charming hand-drawn editorial illustration of Image 1, fixed rig and clear reversible vertical motion.
```

## `wildcard/testing-market-cma`

- Anchor: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/references/cma.png`
- Built-in output: `/Users/danielfoch/.codex/generated_images/019f552d-57b2-7901-9fce-619b71f6b28d/exec-9b5a2179-13d0-4c5d-8d27-30a8e0cf3d50.png`
- Final source: `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/testing-market-cma.png`
- Loading phrase: `Testing the market…`

```text
Use case: illustration-story
Asset type: production four-frame 2x2 sprite master for seamless 0,1,2,3,2,1 loading loop
Input images: Image 1 is the exact CMA Homie identity/style anchor. Preserve the same adult Black man, close-cropped dark hair, friendly face, navy blazer, pale blue-white T-shirt, charcoal trousers, white sneakers, proportions, ink linework, and soft editorial watercolor/pencil finish.

Primary request: Create a reversible “testing the market” loop. CMA Homie holds one persistent oversized outlined laboratory test tube with both hands in front of his torso. The tube contains one fixed solid pale-blue fill area, exactly one small navy house icon, and exactly three opaque coral bubbles. He gently rocks the same tube and its contents left-to-right.

Frames:
1. Tube tilted 12 degrees left; house and three bubbles settle slightly left.
2. Tube tilted 4 degrees left; contents left-center.
3. Tube tilted 4 degrees right; contents right-center.
4. Tube tilted 12 degrees right; contents slightly right.
Reverse playback rocks back. No reaction, color change, explosion, result reveal, celebration, or terminal state.

Continuity: one CMA Homie; exactly two arms/hands/legs/feet, both hands on one tube. Exactly one tube, one house icon, three bubbles, one fill area. Fixed camera, head/torso coordinates, character scale, feet baseline, tube size/design/fill level, icon/bubble count/colors. Only forearms, tube tilt, gaze, and contents’ small settling position change. No extra tube, beaker, bubbles, hand, liquid splash, translucent vapor, smoke, lab table, text, checkmark, formula, or motion trail. Keep fill and bubbles opaque graphic shapes.

Canvas: exact 1254x1254, four equal 627x627 cells borderless. Full head, elbows, hands, shoes, and complete tube fit with at least 10% green margin from every cell edge and center axes. No crop/crossing.
Background: perfectly flat uniform pure #00ff00 edge-to-edge including axes. No seams, gutters, panel lines, borders, shadows, gradients, floor, texture, reflections, or green in props.
Text: none. Do not render “Testing the market…”, words, letters, numbers, formulas, logos, watermark, or UI.
Style: exact charming hand-drawn editorial illustration of Image 1, persistent tube/contents and clear reversible rocking motion.
```

## Deterministic production post-processing

Each accepted built-in output was processed with the installed imagegen chroma helper using border auto-key, soft matte, thresholds 12/220, and despill, then recomposited over exact RGB `(0,255,0)`. Uniform cell-centered final scale factors meeting the ≥51 px margin gate were: raising-roof 0.84, cooking-price 0.90, price-ceiling 0.91, testing-market 0.87.

# Wildcard D batch C — exact built-in imagegen prompt ledger

Generation mode: built-in `imagegen`, one call per distinct asset or targeted correction.

## Accepted finals

- `market-temperature-cma`: accepted built-in output `exec-1bedd7ca-4a02-4f87-a92a-a031d586264c.png`; final source `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/market-temperature-cma.png`; deterministic centered per-cell scale 0.86.
- `ironing-terms-offers`: accepted built-in output `exec-dec9a702-c41e-4e44-a4bf-c2d89a27a52d.png`; final source `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/ironing-terms-offers.png`; deterministic centered per-cell scale 0.85.
- `fine-tuning-fine-print-offers`: accepted built-in output `exec-50d696db-3782-4813-8a03-32766c0a972e.png`; final source `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/fine-tuning-fine-print-offers.png`; deterministic centered per-cell scale 0.84.
- `signature-chase-offers`: accepted built-in output `exec-9db17775-9a8c-4cbe-b3d5-6a7f04b4a27e.png`; final source `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/signature-chase-offers.png`; deterministic centered per-cell scale 0.92.
- `red-flag-scan-reports`: accepted built-in output `exec-a56d0681-bc6c-427e-89c7-c358d6bff920.png`; final source `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/red-flag-scan-reports.png`; deterministic centered per-cell scale 0.87.
- `rate-wrangling-cma`: accepted built-in output `exec-e0b375e5-229c-4a64-b94e-2921caf3ca91.png`; final source `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/rate-wrangling-cma.png`; deterministic centered per-cell scale 0.90.
- `making-connections-crm`: accepted built-in output `exec-928fc270-7a27-4ea2-915e-8cd1e8e2dc31.png`; final source `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/making-connections-crm.png`; deterministic centered per-cell scale 0.88.
- `cleaning-pipeline-crm`: accepted built-in output `exec-20544505-1d36-451a-a212-6d7a3a25818f.png`; final source `/Users/danielfoch/Documents/Homies/assets/homie-loaders/sources/wildcard/cleaning-pipeline-crm.png`; deterministic centered per-cell scale 0.87.

## Exact generation and correction prompts

### 1. `market-temperature-cma` — generation

- Reference/edit target: `assets/homie-loaders/references/cma.png`
- Built-in output: `exec-1bedd7ca-4a02-4f87-a92a-a031d586264c.png`

```text
Use case: illustration-story.
Asset type: production four-frame loading-animation sprite master for a small AI chat loader.
Input image: Image 1 is the exact CMA Homie identity, outfit, proportions, palette, and hand-drawn editorial ink-and-watercolor style anchor.

Primary request: Create one 1254x1254 square 2x2 sprite sheet of CMA Homie taking the market’s temperature. The runtime plays authored poses 1→2→3→4→3→2, so the four frames must be one reversible monotonic motion path with no terminal success pose. The phrase “Taking the market’s temperature…” is metadata only and must not appear in the artwork.

Character lock: reproduce the same adult Black man from Image 1 in every quadrant—same close-cropped dark hair, face, skin tone, navy blazer, pale blue-white T-shirt, charcoal trousers, and white sneakers. One character only. His head, torso, hips, feet, scale, camera angle, and expression remain registered at the same coordinates in all four frames. Exactly two arms, two hands, two legs, and two feet per frame.

Persistent scene: exactly one oversized upright analog thermometer and exactly one fixed miniature house. The thermometer is an opaque cream instrument with a navy outline, one round bulb at the bottom, one straight tube, simple short tick marks with no numerals, and one coral-red indicator column. It leans lightly against the same miniature ochre-and-cream house at the same position and angle in every frame. The house has one roof, one door, and two windows and never changes. CMA Homie stands behind them and holds the thermometer with both hands in the exact same stable grip and arm position in all four frames. Thermometer, bulb, tube, tick marks, house, hands, and body do not move, morph, resize, rotate, or disappear; only the height of the coral indicator changes.

Four frames in reading order:
1. Top-left: coral indicator is at the lowest cold position, just above the bulb.
2. Top-right: same instrument and pose; indicator rises to a low-middle cool position.
3. Bottom-left: indicator rises to a high-middle warm position.
4. Bottom-right: indicator rises to the highest hot position while remaining visibly inside the tube.
These four heights must be clearly distinct and strictly monotonic low→low-middle→high-middle→high; reverse playback reads high→high-middle→low-middle→low. No steam, flame, ice, weather icons, celebration, or final-result gesture.

Sprite layout and backdrop: exactly four equal 627x627 quadrants in a borderless 2x2 reading-order grid. Entire canvas and center axes are a perfectly flat uniform pure #00ff00 chroma-key field. No seams, gutters, divider lines, panels, shadows, gradients, texture, floor plane, reflections, or lighting variation. Each quadrant is self-contained and nothing crosses an invisible center axis. Keep at least 8% clear green padding from every cell edge; full scalp, elbows, shoes, house, thermometer top, bulb, and all tick marks must be fully visible and uncropped.

Continuity constraints: identical straight-on three-quarter camera, focal length, character registration, thermometer construction, house geometry, scale, palette, and lighting in every frame. Exactly one character, one thermometer, one indicator, and one house per frame. No extra hands, duplicated fingers, detached limb, extra thermometer, second house, changing roof/window count, labels, readable text, letters, numbers, degree symbols, logos, captions, loading phrase, watermark, panel border, crop, or #00ff00 inside the character or props.
```

### 2. `ironing-terms-offers` — generation

- Reference/edit target: `assets/homie-loaders/references/offers.png`
- Built-in output: `exec-dec9a702-c41e-4e44-a4bf-c2d89a27a52d.png`

```text
Use case: illustration-story.
Asset type: production four-frame loading-animation sprite master for a small AI chat loader.
Input image: Image 1 is the exact Offers Homie identity, outfit, proportions, palette, and hand-drawn editorial line-and-watercolor style anchor.

Primary request: Create one 1254x1254 square 2x2 sprite sheet of Offers Homie “ironing out the terms.” The runtime plays frames 1→2→3→4→3→2, so the four authored poses must be one smooth reversible left-to-right ironing stroke, with no terminal clean result. The phrase “Ironing out the terms…” is metadata only and must not appear in the image.

Character lock: reproduce the same adult woman from Image 1 in every quadrant—same brown hair in a top bun with loose face-framing strands, face, warm light skin, beige pinstriped utility jumpsuit, rolled cuffs, belt, and white sneakers. One character only. Keep her head, torso, hips, feet, scale, expression, and straight-on three-quarter camera registered at essentially the same coordinates. Exactly two arms, two hands, two legs, and two feet per frame.

Persistent props: exactly one fixed full ironing board, exactly one blank cream contract sheet lying flat on the board, and exactly one small opaque navy-and-cream cordless clothes iron. The board has the same ochre padded top, crossed navy legs, perspective, position, dimensions, and height in every frame. The paper has the same rectangle, size, position, perspective, and outline in all frames and never folds, tears, disappears, or changes size. It contains no writing, letters, numbers, signature, logo, or stamp. Show exactly five subtle gray wrinkle/crease marks on the paper in every frame; they may shift slightly around the moving iron but must never all vanish, so frame 4 is not a finished clean state. The same iron retains identical soleplate, handle, size, handedness, orientation, and design. No cord, steam, spray, table, second paper, or extra tool.

Action in reading order:
1. Top-left: her working hand holds the iron at the leftmost end of the contract. Her other hand rests stably on the far board edge, safely away from the iron.
2. Top-right: the same iron slides to left-center along the same horizontal track; wrist and working forearm follow slightly.
3. Bottom-left: the iron continues to right-center along the same track.
4. Bottom-right: the iron reaches the rightmost point of that same stroke. Five visible wrinkle marks still remain elsewhere on the paper; no presentation gesture or finished result.
The iron’s center must progress strictly leftmost→left-center→right-center→rightmost. Reverse playback is the same uninterrupted return stroke. Keep the paper and board perfectly fixed while only the working forearm, hand, iron, and small crease positions change.

Sprite layout/backdrop: exactly four equal 627x627 quadrants in a borderless 2x2 reading-order grid. Entire canvas, including center axes, is a perfectly flat uniform pure #00ff00 chroma-key field. No seams, gutters, divider lines, panels, shadows, gradients, texture, floor plane, reflections, or lighting variation. Each quadrant is self-contained; nothing crosses an invisible center axis. Keep at least 8% clear green padding from every cell edge; full bun, elbows, shoes, iron, paper, board top, and all board feet must remain fully visible and uncropped.

Continuity and anatomy: one character, exactly two arms and two hands, one board, one blank contract, one iron, and exactly five crease marks per frame. Preserve character identity, clothes, face, camera, scale, board/paper geometry, iron construction, and palette frame to frame. No extra hand, duplicated fingers, fused wrist, second iron, missing board leg, changing paper count, steam, liquid, heat glow, celebration, readable text, letters, numbers, signature, logos, caption, loading phrase, watermark, panel border, crop, or #00ff00 inside the subject or props.
```

### 3. `fine-tuning-fine-print-offers` — generation

- Reference/edit target: `assets/homie-loaders/references/offers.png`
- Built-in output: `exec-61441e82-477f-4258-b741-4a4aca4c3fe7.png`

```text
Use case: illustration-story.
Asset type: production four-frame loading-animation sprite master for a small AI chat loader.
Input image: Image 1 is the exact Offers Homie identity, outfit, proportions, palette, and hand-drawn editorial line-and-watercolor style anchor.

Primary request: Create one 1254x1254 square 2x2 sprite sheet of Offers Homie “fine-tuning the fine print.” The runtime plays frames 1→2→3→4→3→2, so the authored poses must form one reversible monotonic left-to-right tuning pass with no terminal state. The phrase “Fine-tuning the fine print…” is metadata only and must not appear in the artwork.

Character lock: reproduce the same adult woman from Image 1 in all four quadrants—same brown top bun with loose strands, face, warm light skin, beige pinstriped utility jumpsuit, rolled cuffs, belt, and white sneakers. One character only. Keep her head, torso, hips, feet, scale, expression, and three-quarter camera registered at essentially identical coordinates in every frame. Exactly two arms, two hands, two legs, and two feet.

Persistent apparatus: exactly one fixed oversized blank cream contract page on one simple navy floor easel, with exactly one fixed large circular magnifying lens mounted in front of its center. The paper, easel, lens, page outline, perspective, position, and size are identical across all frames. On the page show exactly four short horizontal charcoal-gray graphic line marks, no more and no fewer; these are abstract placeholder marks, not readable writing. The marks gently change from nearly straight to subtly wavy as the tuning pass moves, but all four persist in every frame. Exactly one oversized navy-and-silver metal tuning fork with one handle and two tines. The same fork stays upright in her same working hand and retains identical size, color, construction, handedness, and orientation. Her free hand rests stably on the easel side. No hammer, second fork, loose page, extra lens, table, text, or letters.

Four frames in reading order:
1. Top-left: the vibrating fork is at the far-left edge beside the magnified page; four page marks are nearly straight.
2. Top-right: the same fork moves to left-center across the front of the page; the left portions of all four line marks wobble slightly.
3. Bottom-left: the fork continues to right-center; the wobble travels toward the right portions of the same four marks.
4. Bottom-right: the fork reaches the far-right edge; all four marks remain present with a small right-side wobble. No success pose or changed page.
The tuning fork’s center must progress strictly left→left-center→right-center→right. Show only two tiny opaque navy vibration ticks close to the tines in every frame; they move with the fork and are not extra forks. Reverse playback is the exact return tuning pass. Only the working forearm/hand, fork, its two ticks, and slight waviness of the four marks may change.

Sprite layout/backdrop: exactly four equal 627x627 quadrants in a borderless 2x2 reading-order grid. Entire canvas and center axes are a perfectly flat, uniform pure #00ff00 chroma-key field. No seams, gutters, divider lines, panels, shadows, gradients, texture, floor plane, reflections, or lighting variation. Each cell is self-contained and nothing crosses an invisible center axis. Keep at least 8% clear green padding from every cell edge; full bun, elbows, shoes, page, easel feet, lens, tuning fork, and vibration ticks are fully visible and uncropped.

Continuity/anatomy: one character, exactly two arms and two hands, one fixed page, one fixed easel, one fixed magnifier, one tuning fork, two vibration ticks, and exactly four horizontal line marks per frame. Preserve identity, outfit, face, camera, scale, page/easel/lens geometry, fork construction, and palette frame to frame. No extra hand, duplicated fingers, detached arm, extra fork, fork afterimage, fifth line, missing line, musical notes, sound waves, readable text, letters, numbers, signatures, logos, captions, loading phrase, watermark, panel border, crop, or #00ff00 inside the subject or props.
```

### 4. `fine-tuning-fine-print-offers` — correction

- Reference/edit target: `generated exec-61441e82-477f-4258-b741-4a4aca4c3fe7.png`
- Built-in output: `exec-50d696db-3782-4813-8a03-32766c0a972e.png`

```text
Use case: precise-object-edit.
Input image: Image 1 is an otherwise accepted 1254x1254 square 2x2 loading-animation sprite master.

Primary request: Correct only the working-arm interaction in the two bottom quadrants. In bottom-left and bottom-right, the tuning fork currently appears unsupported. Repose only the character’s working forearm and working hand in each bottom quadrant so that the same anatomically correct hand clearly grips the navy handle at the bottom of the one existing tuning fork. Her arm should extend naturally across the front edge of the fixed easel toward the fork. The grip must be visibly connected to the fork handle and to her sleeve. Keep her other hand resting on the easel side. Each corrected bottom frame must still contain exactly two arms and exactly two hands total.

Absolute preservation lock: leave the entire top-left and top-right quadrants unchanged. In both bottom quadrants preserve the character’s identity, face, bun, torso, legs, jumpsuit, shoes, registered head and body coordinates, expression, camera, scale, the fixed page, easel, circular magnifier, exactly four horizontal line marks, fork position, fork construction, two vibration ticks, palette, and all margins. Do not move the fork: bottom-left remains at right-center and bottom-right remains at far right, retaining the monotonic left-to-right sequence. Do not add an extra arm, hand, fork, pointer, or prop. Do not change the four line marks or background. Retain the perfectly flat uniform pure #00ff00 chroma field, exact 2x2 layout, no seams, gutters, text, logos, shadows, watermark, or crop.
```

### 5. `signature-chase-offers` — generation

- Reference/edit target: `assets/homie-loaders/references/offers.png`
- Built-in output: `exec-9db17775-9a8c-4cbe-b3d5-6a7f04b4a27e.png`

```text
Use case: illustration-story.
Asset type: production four-frame loading-animation sprite master for a small AI chat loader.
Input image: Image 1 is the exact Offers Homie identity, outfit, proportions, palette, and hand-drawn editorial line-and-watercolor style anchor.

Primary request: Create one 1254x1254 square 2x2 sprite sheet of Offers Homie playfully chasing abstract signatures with a butterfly net. The runtime plays frames 1→2→3→4→3→2, so the sequence must be one reversible monotonic left-to-right chase arc with no capture, disappearance, or terminal state. The phrase “Chasing signatures…” is metadata only and must not appear in the artwork.

Character lock: reproduce the same adult woman from Image 1 in every quadrant—same brown top bun with loose strands, face, warm light skin, beige pinstriped utility jumpsuit, rolled cuffs, belt, and white sneakers. One character only. Keep her head, torso, hips, feet, scale, expression, and three-quarter camera registered at essentially the same coordinates across frames. Exactly two arms, two hands, two legs, and two feet in each frame.

Persistent moving objects: exactly one butterfly net with one long navy handle, one cream oval hoop, and one simple opaque pale mesh interior. The same net retains identical size, handle length, hoop shape, perspective, colors, and handedness in every frame. She holds the handle continuously with both anatomically correct hands, one above the other, visibly sleeve-connected; no hand releases it. Exactly four and only four persistent abstract coral-and-navy signature-squiggle icons float ahead of the hoop. Each icon is a short nonalphabetic looping stroke with no readable name, letter, word, or number. The same four icons retain their four distinct silhouettes and relative order in every frame. They never enter the net, overlap the hoop, get captured, disappear, multiply, or turn into text.

Four frames in reading order:
1. Top-left: net hoop and the group of four squiggles occupy the far-left portion of one shallow upward chase arc.
2. Top-right: net and all four squiggles move together to left-center along the same arc, with the four icons still just ahead of the hoop.
3. Bottom-left: net and all four squiggles continue to right-center.
4. Bottom-right: net and all four squiggles reach the far-right portion of the same arc, still separated and uncaptured.
The net hoop’s center and each of the four icons must progress strictly left→left-center→right-center→right. Reverse playback reads as the same ongoing chase back along the arc. Only her forearms/hands, the one net, and the four icons may move; no running or torso bounce, no final catch, celebration, or empty end frame.

Sprite layout/backdrop: exactly four equal 627x627 quadrants in a borderless 2x2 reading-order grid. Entire canvas and center axes are a perfectly flat, uniform pure #00ff00 chroma-key field. No seams, gutters, dividers, panel lines, shadows, gradients, textures, floor plane, reflections, or lighting variation. Each quadrant is self-contained and nothing crosses an invisible center axis. Keep at least 8% clear green padding from every cell edge; full bun, elbows, hands, shoes, net pole, hoop, mesh, and every squiggle remain fully visible and uncropped.

Continuity/anatomy: one character, exactly two arms and two hands, one net, one hoop, one handle, and exactly four abstract squiggle icons per frame. Preserve identity, outfit, face, camera, scale, net construction, icon designs/order, and palette frame to frame. No extra limb, third hand, duplicated grip, extra net, second hoop, fifth squiggle, missing squiggle, caught squiggle, butterfly, animal, paper, pen, readable cursive, letters, words, numbers, logos, captions, loading phrase, watermark, panel border, crop, or #00ff00 inside the subject or props.
```

### 6. `red-flag-scan-reports` — generation

- Reference/edit target: `assets/homie-loaders/references/reports.png`
- Built-in output: `exec-a56d0681-bc6c-427e-89c7-c358d6bff920.png`

```text
Use case: illustration-story.
Asset type: production four-frame loading-animation sprite master for a small AI chat loader.
Input image: Image 1 is the exact Reports Homie identity, outfit, proportions, palette, and hand-drawn editorial ink-and-watercolor style anchor.

Primary request: Create one 1254x1254 square 2x2 sprite sheet of Reports Homie playfully scanning for red flags like a lifeguard. The runtime plays frames 1→2→3→4→3→2, so binocular direction and flag motion must form one reversible monotonic left-to-right sweep with no terminal discovery pose. The phrase “Spotting the red flags…” is metadata only and must not appear in the image.

Character lock: reproduce the same adult woman from Image 1 in every quadrant—same long dark-brown wavy hair, face, warm light skin, cream/beige tailored pantsuit, white blouse, peach patterned neck scarf, beige pointed shoes, slim proportions, and editorial style. Add one persistent playful coral lifeguard sun visor with a plain cream band, identical in all four frames; no lettering, cross, badge, or logo. One character only. Keep head, torso, hips, feet, scale, and straight-on three-quarter camera registered at essentially the same coordinates. Exactly two arms, two hands, two legs, and two feet in every frame.

Persistent scene: exactly one fixed compact ochre tabletop on two navy legs sits in front of her, identical in position, size, perspective, and construction in every frame. On it lies a tidy “sea” of exactly six overlapping blank cream document sheets, all six persistent and fixed; no sheet disappears, changes size, or contains text. Exactly three and only three plain coral-red triangular flags on short navy poles stand among three fixed sheets. The same three flags remain visible in every frame in the same left/middle/right order, with identical flag and pole designs. Reports Homie holds exactly one pair of navy binoculars continuously to her eyes with both anatomically correct hands; binocular construction and grip remain identical while her forearms and binocular direction pivot slightly.

Four frames in reading order:
1. Top-left: binoculars/gaze aim to the far left. All three flag poles are at their lowest visible height and lean subtly left.
2. Top-right: binoculars sweep to left-center. All three flags rise a small equal step and lean less left.
3. Bottom-left: binoculars sweep to right-center. All three flags rise another equal step and are nearly upright.
4. Bottom-right: binoculars aim far right. All three flags rise one final small step and lean subtly right, remaining attached to their sheets.
Binocular direction and the three flag tops progress strictly left→left-center→right-center→right. Reverse playback returns smoothly. No flag is newly found, circled, removed, captured, celebrated, or spotlighted. Only her forearms/binocular angle and the gentle flag height/lean may change; the character body, table, six sheets, and three fixed pole bases remain registered.

Sprite layout/backdrop: exactly four equal 627x627 quadrants in a borderless 2x2 reading-order grid. Entire canvas and center axes are a perfectly flat uniform pure #00ff00 chroma-key field. No seams, gutters, dividers, panel lines, shadows, gradients, textures, floor plane, reflections, or lighting variation. Each quadrant is self-contained; nothing crosses an invisible center axis. Keep at least 8% clear green padding from every cell edge; full hair, visor, elbows, shoes, binoculars, table legs, sheets, poles, and flags remain fully visible and uncropped.

Continuity/anatomy: one character, exactly two arms and two hands, one visor, one pair of binoculars, one table, six blank sheets, and exactly three red flags per frame. Preserve identity, clothing, face, camera, scale, table/sheet geometry, binocular construction, flag order/design, and palette frame to frame. No extra limb, third hand, detached binocular, extra flag, fourth flag, missing flag, extra sheet, readable text, letters, numbers, cross symbol, logo, caption, loading phrase, watermark, panel border, crop, or #00ff00 inside the subject or props.
```

### 7. `rate-wrangling-cma` — generation

- Reference/edit target: `assets/homie-loaders/references/cma.png`
- Built-in output: `exec-92482264-c07b-4d5a-90f3-0a8e4cbbfed7.png`

```text
Use case: illustration-story.
Asset type: production four-frame loading-animation sprite master for a small AI chat loader.
Input image: Image 1 is the exact CMA Homie identity, outfit, proportions, palette, and hand-drawn editorial ink-and-watercolor style anchor.

Primary request: Create one 1254x1254 square 2x2 sprite sheet of CMA Homie playfully “rate wrangling” with a cowboy lasso. The runtime plays frames 1→2→3→4→3→2, so the four authored poses must form one reversible monotonic left-to-right wrangling arc with no capture or terminal state. The phrase “Rate wrangling…” is metadata only and must not appear in the artwork.

Character lock: reproduce the same adult Black man from Image 1 in every quadrant—same close-cropped hair, face, skin tone, navy blazer, pale blue-white T-shirt, charcoal trousers, and white sneakers. Add one persistent plain ochre cowboy hat with a navy band, identical in all frames, with no badge or lettering. One character only. Keep his head under the hat, torso, hips, feet, scale, expression, and three-quarter camera registered at essentially the same coordinates. Exactly two arms, two hands, two legs, and two feet per frame.

Persistent lasso: exactly one tan rope lasso with one closed oval loop, one continuous trailing rope, and no loose duplicate coil. The same rope retains identical thickness, color, total length, loop size, knot, and construction in all frames. CMA Homie holds the trailing rope continuously with exactly two anatomically correct sleeve-connected hands, one gripping near the knot and the other controlling the tail. The loop swings in front of him but never tightens, catches, breaks, or leaves the frame.

Persistent rate tokens: exactly three and only three identical-size coral circular medallions, each containing one simple cream percent-sign graphic. The percent symbol is explicitly required, but no other text is allowed. The same three tokens retain their left/middle/right order, size, colors, and designs in all four frames. They bounce gently together along one shallow left-to-right arc just ahead of and partly surrounded by the open lasso loop, but never overlap each other, enter a pocket, get captured, disappear, multiply, or change symbols.

Frames in reading order:
1. Top-left: open lasso loop and the three rate tokens occupy the far-left portion of the shallow arc; tokens sit at a low bounce position.
2. Top-right: loop and all three tokens move to left-center; tokens rise slightly.
3. Bottom-left: loop and all three tokens continue to right-center; tokens settle slightly lower.
4. Bottom-right: loop and all three tokens reach the far-right portion; tokens rise slightly again, still free and persistent.
The loop center and each token progress strictly left→left-center→right-center→right. Reverse playback is a smooth continued wrangling motion. Only forearms/hands, rope, and tokens move; no torso bounce, capture, tied knot around tokens, empty frame, presentation, or celebration.

Sprite layout/backdrop: exactly four equal 627x627 quadrants in a borderless 2x2 reading-order grid. Entire canvas and center axes are a perfectly flat, uniform pure #00ff00 chroma-key field. No seams, gutters, divider lines, panel borders, shadows, gradients, textures, floor plane, reflections, or lighting variation. Each cell is self-contained and nothing crosses an invisible center axis. Keep at least 8% clear green padding from every cell edge; full hat, elbows, hands, shoes, rope loop/tail, and all three tokens remain fully visible and uncropped.

Continuity/anatomy: one character, exactly two arms and two hands, one hat, one lasso loop, one continuous rope, and exactly three percent-sign tokens per frame. Preserve identity, clothing, face, camera, scale, rope geometry, token designs/order, and palette frame to frame. No extra limb, third hand, duplicate rope, second loop, fourth token, missing token, changed percent symbol, dollar sign, readable words, letters, numbers, logos, caption, loading phrase, watermark, panel border, crop, or #00ff00 inside the subject or props.
```

### 8. `rate-wrangling-cma` — correction-regeneration

- Reference/edit target: `assets/homie-loaders/references/cma.png`
- Built-in output: `exec-fa0d5900-3eba-4f52-9b9e-e8ab6d460b92.png`

```text
Use case: illustration-story.
Asset type: corrected production four-frame loading-animation sprite master.
Input image: Image 1 is the exact CMA Homie identity and illustration-style anchor.

Primary request: Regenerate the four-frame “rate wrangling” loop with one essential staging correction: CMA Homie must remain centered and registered at the same exact head, torso, hips, and feet coordinates in all four quadrants while one compact lasso loop and exactly three percent tokens travel left-to-right around him. Runtime order is 1→2→3→4→3→2, so there is no capture or final state. The phrase “Rate wrangling…” is metadata only and must not appear.

Character: same adult Black man from Image 1, same close-cropped hair, face, skin tone, navy blazer, pale blue-white T-shirt, charcoal trousers, white sneakers, and one identical plain ochre cowboy hat with navy band. Place him at the horizontal center of each 627x627 cell, full-body, same straight-on three-quarter view, same scale and stance. His head center, shoulder center, belt center, and shoe baseline must match frame-to-frame within a few pixels. Exactly two sleeve-connected arms and two anatomically correct hands. Both hands continuously control the same tan rope near his waist/chest; only the forearms adjust slightly.

Moving system: one and only one compact tan lasso, with one closed oval loop roughly shoulder-width rather than huge, one continuous tail, same rope thickness/length/knot/loop size in all frames. Exactly three coral circular tokens, each with one cream percent-sign graphic, identical size, persistent left/middle/right order. The three tokens remain just inside the open loop and never disappear, multiply, overlap, change symbol, or get captured. Keep loop and tokens compact enough to travel around the fixed centered character without touching cell edges.

Frames: top-left loop/token group at far left beside his left shoulder; top-right at left-center partly in front of his torso; bottom-left at right-center partly in front of his torso; bottom-right at far right beside his right shoulder. Loop center and every token progress strictly left→left-center→right-center→right; subtle low→high→low→high bounce is allowed. Reverse playback returns smoothly. Character body does not translate, zoom, flip, or swap sides.

Layout/background: exact 1254x1254 square, four equal 627x627 quadrants, borderless 2x2 reading order. Perfectly flat uniform pure #00ff00 across canvas and center axes; no seams, gutters, panels, shadows, gradients, texture, floor, reflections, or background variation. At least 8% green padding around full hat, body, shoes, rope loop/tail, and tokens; nothing crosses axes or crops.

Constraints: one character, two arms, two hands, two legs, two feet, one hat, one rope, one loop, exactly three percent tokens per frame. No extra rope or loop, fourth/missing token, capture, celebration, readable words, letters, numbers other than the explicitly required percent graphic, dollar signs, logos, captions, watermark, crop, or #00ff00 inside subjects.
```

### 9. `making-connections-crm` — generation

- Reference/edit target: `assets/homie-loaders/references/crm.png`
- Built-in output: `exec-51b2ccee-c393-4fd5-8c9d-45d3fe94ba29.png`

```text
Use case: illustration-story.
Asset type: production four-frame loading-animation sprite master for a small AI chat loader.
Input image: Image 1 is the exact CRM Homie identity, outfit, proportions, palette, and hand-drawn editorial illustration style anchor.

Primary request: Create one 1254x1254 square 2x2 sprite sheet of CRM Homie “making connections” on one fixed plugboard network. Runtime plays frames 1→2→3→4→3→2, so the hand-held cable ends must follow one reversible monotonic left-to-right path with no final completed network state. The phrase “Making connections…” is metadata only and must not appear in the artwork.

Character lock: reproduce the same adult Black man from Image 1 in every quadrant—same shaved head, face, skin tone, olive bomber jacket, plain white T-shirt, light blue jeans, and white slip-on shoes. One character only. Keep his head, torso, hips, feet, scale, expression, and straight-on three-quarter camera registered at essentially identical coordinates. Exactly two arms, two hands, two legs, and two feet per frame.

Fixed network: exactly one compact upright navy plugboard on one fixed cream pedestal/base beside him. Board position, rectangular shape, support, perspective, size, and all geometry stay identical. It contains exactly four and only four large graphic nodes in a 2x2 grid, each with one simple distinct opaque pictogram: top-left house, top-right person bust, bottom-left phone handset, bottom-right envelope. No words or labels. Each node has one small circular jack directly beneath it and one coral indicator ring. The four node pictograms, order, jack positions, and designs never change.

Exactly two persistent cables: one coral cable and one cream cable, each with one fixed end permanently plugged into two small source sockets at the board’s far-left edge and one free plug end. The cable colors, lengths, thicknesses, curves, connector designs, and source connections remain coherent in all frames. CRM Homie holds exactly one free cable end in each anatomically correct hand; both hands remain visibly sleeve-connected and no plug floats. The two hands and two free ends travel together horizontally across the board, never letting go and never adding/removing a cable.

Frames in reading order:
1. Top-left: both held free ends hover near the two leftmost jacks; left-side node rings glow coral.
2. Top-right: both hands/free ends move to left-center between the left and right jack columns; glow pulse shifts toward center.
3. Bottom-left: both hands/free ends continue to right-center; right-side node rings brighten while left rings dim.
4. Bottom-right: both held ends reach the two rightmost jacks but remain visibly just in front of them, not plugged as a terminal result; right node rings glow.
The hand centers and both free plugs progress strictly left→left-center→right-center→right. Reverse playback is a clean return pass. Exactly four nodes and two cables persist; only forearms/hands, free cable arcs/ends, and node-ring brightness change. No completed connection, spark, celebration, extra line, or disappearing cable.

Sprite layout/backdrop: exactly four equal 627x627 quadrants in a borderless 2x2 reading-order grid. Entire canvas and center axes are a perfectly flat uniform pure #00ff00 chroma-key field. No seams, gutters, dividers, panel lines, shadows, gradients, textures, floor plane, reflections, or lighting variation. Each cell is self-contained; nothing crosses an invisible center axis. Keep at least 8% clear green padding from every cell edge; full scalp, elbows, hands, shoes, board, pedestal, nodes, jacks, and both cable curves/end plugs remain fully visible and uncropped.

Continuity/anatomy: one character, exactly two arms and two hands, one fixed board/base, exactly four pictogram nodes in the specified order, four jacks, and exactly two cables per frame. Preserve identity, clothing, face, camera, scale, board/node geometry, cable colors/construction, and palette. No extra limb, third hand, floating plug, third cable, missing cable, fifth/missing node, swapped pictogram, extra house/person/phone/envelope, readable text, letters, numbers, logos, caption, loading phrase, watermark, panel border, crop, or #00ff00 inside subjects.
```

### 10. `making-connections-crm` — correction-regeneration

- Reference/edit target: `assets/homie-loaders/references/crm.png`
- Built-in output: `exec-50f968f9-690d-4f2e-b1df-4fdfe701603b.png`

```text
Use case: illustration-story.
Asset type: corrected production four-frame loading-animation sprite master.
Input image: Image 1 is the exact CRM Homie identity and hand-drawn editorial style anchor.

Primary request: Regenerate “Making connections…” as a mechanically clear monotonic left-to-right cable pass. Runtime order is 1→2→3→4→3→2, with no terminal connection. The loading phrase is metadata only; no text in image.

Character: same adult Black man from Image 1, shaved head, face, olive bomber, white T-shirt, light-blue jeans, white slip-ons. One full-body character centered behind the apparatus in all four cells. Lock head, torso, hips, feet, scale, camera, and expression to identical coordinates. Exactly two sleeve-connected arms and exactly two hands.

Fixed apparatus: one waist-high horizontal navy plugboard on two short cream pedestal legs in front of him, same coordinates/size/perspective every frame. Across the board is one straight horizontal row of exactly four large graphic nodes, left-to-right: house, person bust, phone handset, envelope. Each has one small jack directly below and one coral indicator ring. No labels. Nodes, pictograms, order, jacks, board, and legs never move or morph.

Exactly two persistent flexible cables, one coral and one cream. Each cable has its lower end permanently attached to one source socket at the bottom center of the board and one free plug end. CRM holds one free plug in each hand continuously; both visible hands stay connected to sleeves. The two held plugs hover together just in front of the row and never become fully inserted. Cable count, colors, connector shape, lengths, and source ends remain coherent.

Four frames: top-left both hands/free plugs at far-left house jack; top-right at left-center between house/person; bottom-left at right-center between phone/envelope; bottom-right at far-right envelope jack. Both hand centers and both free plug ends progress strictly left→left-center→right-center→right. Cable curves follow smoothly. Node-ring glow pulse moves left-to-right with the hands. Reverse playback returns cleanly; no completed connection, spark, celebration, or disappearing cable.

Canvas: exact 1254x1254 2x2 reading-order sheet, four equal 627px cells, no borders/gutters/seams. Perfectly flat uniform pure #00ff00 including center axes; no shadows, gradients, texture, floor, reflections, or variation. At least 8% green padding around scalp, elbows, shoes, board legs, cables, and plugs; no crop or center-axis crossing.

Constraints: one character, two arms/hands, one board, exactly four nodes with the specified pictograms/order, four jacks, exactly two cables. No third cable, extra/missing node, extra hand, floating plug, readable text, letters, numbers, logos, caption, watermark, crop, or #00ff00 inside subjects.
```

### 11. `cleaning-pipeline-crm` — generation

- Reference/edit target: `assets/homie-loaders/references/crm.png`
- Built-in output: `exec-8f8a53fc-e978-43de-9ae9-27a47ef308e3.png`

```text
Use case: illustration-story.
Asset type: production four-frame loading-animation sprite master for a small AI chat loader.
Input image: Image 1 is the exact CRM Homie identity, outfit, proportions, palette, and hand-drawn editorial illustration style anchor.

Primary request: Create one 1254x1254 square 2x2 sprite sheet of CRM Homie “cleaning the pipeline” by pushing one persistent plumbing snake brush through one fixed blue pipe. Runtime plays frames 1→2→3→4→3→2, so brush and clogs must follow one reversible monotonic left-to-right scrub with no terminal clean state. The phrase “Cleaning the pipeline…” is metadata only and must not appear.

Character lock: reproduce the same adult Black man from Image 1 in every quadrant—same shaved head, face, skin tone, olive bomber jacket, white T-shirt, light blue jeans, white slip-on shoes. One full-body character centered behind the apparatus. Keep head, torso, hips, feet, scale, expression, and straight-on camera registered at essentially identical coordinates. Exactly two arms, two hands, two legs, and two feet.

Fixed pipeline: exactly one continuous waist-high horizontal opaque navy-blue pipeline on two short cream supports. It has one left inlet elbow, one long straight body, and one right outlet elbow, identical coordinates, size, perspective, thickness, joints, supports, and construction in every frame. To make the interior action readable without glass or transparency, the straight front face has one long cream cutaway inspection channel bordered by the opaque navy shell. The pipe remains a solid graphic object—no translucent material, flowing liquid, or disappearing wall.

Persistent snake/brush: exactly one coral flexible plumbing snake entering through the left elbow, with one navy handgrip outside the inlet and one compact round ochre bristle brush head visible within the cream channel. Same cable thickness/length, handle, brush shape, and colors across frames. CRM holds the one handgrip with one anatomically correct hand while his other hand guides the cable near the inlet; both hands are sleeve-connected. Only small forearm/cable changes.

Persistent clogs: exactly three and only three small gray card-shaped rectangular clogs visible inside the inspection channel, each with a blank face and no text. The same three retain left/middle/right order, size, shape, gray color, and full visibility in every frame. The brush nudges them along but none exits, disappears, tears, duplicates, or becomes clean.

Four frames in reading order:
1. Top-left: brush head and the three gray cards occupy the far-left portion of the channel.
2. Top-right: brush and all three cards move to left-center; cable feeds in slightly.
3. Bottom-left: brush and all three cards continue to right-center.
4. Bottom-right: brush and all three cards reach the far-right portion but remain fully inside the channel; no empty/clean result.
Brush center and each card center progress strictly left→left-center→right-center→right. Keep small gaps so all three cards remain countable. Reverse playback is the same return scrub. Only forearms, cable curve/feed, brush, and three cards move; character body, pipeline, elbows, channel, supports remain fixed.

Sprite layout/backdrop: exactly four equal 627x627 quadrants in a borderless 2x2 reading-order grid. Entire canvas and center axes are a perfectly flat uniform pure #00ff00 chroma-key field. No seams, gutters, dividers, panel lines, shadows, gradients, textures, floor plane, reflections, or lighting variation. Each cell is self-contained; nothing crosses an invisible center axis. Keep at least 8% clear green padding from every cell edge; full scalp, elbows, hands, shoes, pipe elbows/supports, snake tail, brush, and all three cards remain fully visible and uncropped.

Continuity/anatomy: one character, exactly two arms and two hands, one fixed continuous pipeline, one inspection channel, one snake cable, one handle, one brush head, and exactly three gray card clogs per frame. Preserve identity, clothing, face, camera, scale, pipe geometry, brush construction, card order/design, and palette. No extra limb, third hand, second pipe, second brush, fourth/missing clog, terminal empty pipe, water, bubbles, transparency, readable text, letters, numbers, logos, caption, loading phrase, watermark, panel border, crop, or #00ff00 inside subjects.
```

### 12. `cleaning-pipeline-crm` — correction

- Reference/edit target: `generated exec-8f8a53fc-e978-43de-9ae9-27a47ef308e3.png`
- Built-in output: `exec-20544505-1d36-451a-a212-6d7a3a25818f.png`

```text
Use case: precise-object-edit.
Input image: Image 1 is an otherwise accepted 1254x1254 square 2x2 loading-animation sprite master.

Primary request: Correct only the count of gray rectangular card-shaped clogs in the top-right and bottom-right quadrants so every frame contains exactly three gray cards.
- Top-right currently shows four gray card clogs to the right of the ochre brush. Remove only the extra far-right gray card and close the spacing so exactly three persistent gray cards remain, still ordered left-to-right and still inside the cream pipe channel.
- Bottom-right currently shows only two gray card clogs immediately to the left of the ochre brush. Add exactly one matching gray blank rectangular card beside those two, producing exactly three evenly separated gray cards immediately left of the brush.
All card faces remain blank with no text. Keep the intended monotonic group positions: frame 2 remains left-center and frame 4 remains far right. No card exits the pipe and no clean state.

Absolute preservation lock: preserve the entire top-left and bottom-left quadrants. In the edited quadrants preserve CRM Homie’s identity, head/body registration, exactly two arms/hands and their grips, clothes, face, cable curve, one brush, pipeline shell, left/right elbows, cream inspection channel, supports, camera, scale, palette, and margins. Do not move the brush, character, pipe, or supports. Do not add another brush, cable, hand, pipe, or fourth card. Retain exactly one character, one snake/brush, and exactly three gray cards in each quadrant. Keep the perfectly flat uniform pure #00ff00 background, exact 2x2 layout, no seams, gutters, text, logos, shadows, watermark, or crop.
```

### 13. `rate-wrangling-cma` — margin-correction

- Reference/edit target: `generated exec-fa0d5900-3eba-4f52-9b9e-e8ab6d460b92.png`
- Built-in output: `exec-e0b375e5-229c-4a64-b94e-2921caf3ca91.png`

```text
Use case: precise-object-edit.
Input image: Image 1 is an otherwise accepted 1254x1254 square 2x2 “rate wrangling” sprite master.

Primary request: Make only an outer-edge safe-margin correction in the top-left and bottom-right quadrants.
- Top-left: move the complete lasso oval and its three coral percent tokens horizontally inward to the right by about 35 source pixels so the leftmost rope sits at least 55 pixels from the cell’s left edge. Preserve their spacing/order and keep this clearly the far-left pose.
- Bottom-right: move the complete lasso oval and its three coral percent tokens horizontally inward to the left by about 35 source pixels so the rightmost rope sits at least 55 pixels from the cell’s right edge. Preserve spacing/order and keep this clearly the far-right pose.
Smoothly adjust only the short connecting rope segment between each moved loop and the character’s fixed gripping hands. Keep one continuous rope, one loop, and exactly three tokens. Do not move the character or his hands.

Absolute preservation lock: leave the top-right and bottom-left quadrants unchanged. Preserve all four characters’ exact head/torso/feet registration, identity, cowboy hat, face, navy blazer, clothing, anatomy, exactly two arms/hands, poses, camera, scale, rope thickness/color/knot, percent symbols, token design, and green background. Maintain strict monotonic loop/token centers left→left-center→right-center→right and no capture. No second rope, extra loop, fourth token, missing token, extra hand, text beyond the required percent graphics, logos, seams, gutters, shadows, watermark, crop, or background variation. Exact 1254x1254 canvas, equal 2x2 layout, flat uniform pure #00ff00.
```

### 14. `making-connections-crm` — frame4-registration-correction

- Reference/edit target: `generated exec-50f968f9-690d-4f2e-b1df-4fdfe701603b.png`
- Built-in output: `exec-928fc270-7a27-4ea2-915e-8cd1e8e2dc31.png`

```text
Use case: precise-object-edit.
Input image: Image 1 is an otherwise accepted 1254x1254 square 2x2 “making connections” sprite master.

Primary request: Correct only the CRM Homie body registration in the bottom-right quadrant. His body is shifted too far right there. Reposition his head, torso, hips, legs, and shoes horizontally left so they match the exact cell-relative coordinates and scale of the CRM Homie in the bottom-left quadrant. Match his head center, shoulder center, belt center, and shoe baseline to bottom-left. Keep his two existing hands at the bottom-right frame’s rightmost envelope-jack position, each still visibly gripping one cable plug, and redraw only the two sleeve-connected forearms as natural extensions from the newly registered shoulders to those fixed hands. Bottom-right must contain exactly two arms and two hands.

Absolute preservation lock: leave the other three quadrants unchanged. In bottom-right do not move or alter the fixed horizontal board, its two cream legs, the four nodes in house/person/phone/envelope order, four jacks, indicator rings, exactly two cables, bottom source sockets, rightmost held plug positions, cable colors/curves, clothes, identity, face, scale, camera, or green background. Preserve monotonic held-plug path left→left-center→right-center→right and the envelope ring glow. No extra hand, floating plug, third cable, extra/missing node, text, logos, seam, gutter, shadow, watermark, crop, or background variation. Exact 1254x1254 2x2 canvas, flat uniform pure #00ff00.
```

## Deterministic production post-processing

All accepted artwork was processed without generative redraw after selection: the installed imagegen chroma helper extracted the removable background with soft matte and despill; artwork in each 627×627 cell was uniformly scaled about the exact cell center using the per-asset factor listed above; each cell was recomposited over mathematically exact RGB `#00ff00`. The resulting sources remain 1254×1254 RGB 2×2 sheets and every non-green authored pixel clears every cell edge by at least 52 pixels.

