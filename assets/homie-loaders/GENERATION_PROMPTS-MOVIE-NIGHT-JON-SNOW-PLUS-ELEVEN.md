# Generation prompts and provenance — Movie Night: Jon Snow + eleven

This release record covers the accepted candidate artifacts for twelve Movie Night loaders. Exact prompt text below is copied verbatim from the persisted prompt files. Missing prompt text is identified as missing and is not reconstructed. All digests are SHA-256 hashes of file bytes.

## Provenance rules

Canonical Homie references are the identity and illustration-style authorities. User-supplied, clipboard, and observed reference images supply only the explicitly recorded pose, wardrobe, prop, or action concept; they do not replace canonical Homie identity. When a user reference was observed but was not sent to the accepted generation, that distinction is stated explicitly.

The deterministic builders reuse an accepted alpha or locked plate. Only the named rigid rig, masked local overlay, or frame-shared deterministic recolour may change. Unless a section says otherwise, four authored phases are encoded in reversible GIF order `[0, 1, 2, 3, 2, 1]` with durations `[210, 140, 140, 210, 140, 140]` milliseconds.

Tyler and Robin were subsequently finalized, independently rebuilt, and promoted with the source-strip and GIF hashes recorded in their SHA-lock tables below.

## 1. jon-snowing-marketing

### Prompt and reference provenance

No exact accepted generation prompt, prompt file, targeted-edit prompt, or image-reference role record is persisted for Jon. Repository and candidate-record searches found the accepted generated plate, normalized alpha, locked plate, policy/QA artifacts, and deterministic builder only. The generation prompt is therefore not quoted or reconstructed.

The accepted plate depicts the male Marketing Homie in black northern fur/leather with a vertical sword. This description documents the accepted artifact and builder contract; it is not presented as recovered prompt text. No user-reference role or canonical-reference path can be established from persisted prompt/provenance evidence.

### Accepted edits and deterministic motion

No targeted image-edit prompt is persisted. `add_jon_snowing.py` hard-locks the accepted alpha by SHA before building. Face, anatomy, body, cloak, hands, sword, crop, scale, and anchor remain static in all authored phases. Only six deterministic six-arm snowflakes outside the silhouette and one glint confined to the sword blade vary.

### SHA-256 locks

| Artifact | Persisted path | SHA-256 |
|---|---|---|
| Accepted generated/chroma plate | `assets/homie-loaders/qa/strict-repairs/raw/jon-snowing-marketing-generated.png` | `55a08f44c6cc05267a4797b992683a0ade3fa126acac416552fdbb31f0d9022b` |
| Accepted alpha | `assets/homie-loaders/qa/strict-repairs/raw/jon-snowing-marketing-alpha.png` | `7c4011d89dd14c4f38d9149114387f6c26a1e4e472b15ac198949e3f9fd46b95` |
| Locked plate | `assets/homie-loaders/qa/strict-repairs/jon-snowing-marketing/candidates/frames/jon-snowing-marketing/locked-marketing-cloak-hands-and-sword.png` | `72428cf08d9b11809c922d5778ec2bac92bef6468689b9e57efb7632da66a178` |
| Builder | `assets/homie-loaders/scripts/add_jon_snowing.py` | `6a2990b7d832507ce7c1be4f92d698c0bf70cec682f41bbf464c1a41683c44b3` |
| Source strip | `assets/homie-loaders/qa/strict-repairs/jon-snowing-marketing/candidates/sources/wildcard/jon-snowing-marketing.png` | `8ae889775a0a659fb27142e8c04e45df21293ad26cf12cfc8f4b5d241f92f966` |
| Preview GIF | `assets/homie-loaders/qa/strict-repairs/jon-snowing-marketing/candidates/gifs/wildcard/jon-snowing-marketing.gif` | `081883e2ec709593c38ed98cb16cd84536173ca24e8964f39031c680cd4d95fb` |

## 2. spoking-content

### Reference roles

Canonical identity/style authority: `assets/homie-loaders/sources/content/concept-sketch.png` (current file SHA-256 `51dcf6e9e2c1767300839ff8dfcb240e92cd83d68b64b02f17802d66dadb3e09`). User reference: `/var/folders/kz/c40hnqf51b78kdv_h64qjj0h0000gn/T/codex-clipboard-e612df06-aa60-4b48-988b-59f597073a3f.png` (current file SHA-256 `58111ec9bb507f5dc09653f601a467452bb4c3b2e209118166a4b4035f294baa`), used only for wardrobe/pose guidance.

### Exact accepted generation prompt

Persisted verbatim in `imagegen-prompt.txt`:

```text
Use case: stylized-concept
Asset type: immutable 2x2 authored sprite plate for a 256px transparent loading animation
Input images: Image 1 is the ONLY identity, face, body-proportion, and ink-and-watercolour illustration-style reference; preserve its recognizable canonical Asian male Homie. Image 2 is wardrobe and pose reference ONLY; do not copy that person's face or identity.
Scene/backdrop: one perfectly uniform flat solid #00ff00 chroma-key field across the entire square sheet, including broad outer margins and clear green gutters between four cells. No panels, boxes, dividers, floor, shadows, gradients, texture, reflections, captions, or border.
Subject: the same single canonical Asian male Homie repeated exactly once per cell, waist-up, wearing a plain cobalt-blue long-sleeve science-fiction mock-neck uniform with a narrow black collar. Absolutely no chest badge, insignia, logo, emblem, text, numbers, stars, arrows, or decorative glyphs. Keep the exact same face, hair, expression, head angle, torso, shoulders, garment seams, crop, camera, scale, and anchor in all four cells.
Authored action, reading order: cell 1 right arm relaxed low; cell 2 right forearm lifting with palm beginning to face forward; cell 3 a clear palm-forward split-finger science-fiction salute with the fingers cleanly grouped 2+2; cell 4 the fully raised salute held slightly higher as the climax. Only the one right arm/hand changes. Left arm remains relaxed and identical. Each cell must be distinct and the progression must read cleanly forward then work in reverse.
Style/medium: match Image 1's polished editorial ink linework and subtle watercolour wash, realistic human anatomy, warm paper-like painted texture only inside the character.
Composition/framing: exact 2x2 regular grid, four equal square authored cells, character fully contained in every cell with at least 10% green padding on all sides, no crop or overlap into gutters.
Constraints: exactly one person in each cell; exactly two arms and two hands total; five natural fingers on every visible hand; one clean connected silhouette; no floating fragments; no extra limbs; no body scaling, camera shift, head bob, torso wiggle, redraw drift, or wardrobe drift. Preserve face identity from Image 1. Use #00ff00 nowhere in the character.
Avoid: Image 2 identity, photorealism, 3D, clay, vector-flat style, props, glass, logos, text, watermark, signature, motion lines, sparkles, icons, symbols, shadows, key-colour spill.
```

### Accepted edits and deterministic motion

The metadata records no targeted edit prompt. Donor panel `2` is the sole immutable source for the face, torso, garment, arm, and anatomically correct five-finger split salute. Registration is `[0, 0]` and scale is `0.78` in every phase. Only the locked right-arm/salute rig rotates through `[-3°, -1°, 1°, 3°]`; the recorded static face/torso hash is identical in all four phases and changed pixels outside the rig equal zero.

### SHA-256 locks

| Artifact | Persisted path | SHA-256 |
|---|---|---|
| Prompt | `assets/homie-loaders/qa/strict-repairs/spoking-content/candidates/imagegen-prompt.txt` | `36be1e1384e90fe94c674f5375575491c0b1a9df91666696348f48e6ca19f9f7` |
| Accepted chroma | `assets/homie-loaders/qa/strict-repairs/spoking-content/candidates/raw-chroma.png` | `a8d083ef3e8d9032836010231b3b9ebfd0d37757e01a16583ee33d0e4c8ea1e1` |
| Accepted raw alpha | `assets/homie-loaders/qa/strict-repairs/spoking-content/candidates/raw-alpha.png` | `0830152af4a17a2c6a6326bdb86d0bff9808d5340ac667c45cdd839e8c4f4581` |
| Locked plate | `assets/homie-loaders/qa/strict-repairs/spoking-content/candidates/locked-plate.png` | `cd48f026091fc2330151bcdccf3a030c3e516e2ec0d9d552ef4435556c5db157` |
| Builder | `assets/homie-loaders/qa/strict-repairs/spoking-content/candidates/build_spoking_content.py` | `db7ed392362b34945f9cac3235d8aee5fa423889609cff8f9eda09e4e62ef8c6` |
| Source strip | `assets/homie-loaders/qa/strict-repairs/spoking-content/candidates/spoking-content.png` | `36d0c2ab59419c30dacdb4b1705bdfce997a61f989235a7935dcae77e1157833` |
| Preview GIF | `assets/homie-loaders/qa/strict-repairs/spoking-content/candidates/spoking-content.gif` | `b9b88ac4ee647344eea4a9e811d2a6bda4fbfed3e7223df0bed74995acef3b47` |

## 3. gatsbying-manager

### Reference roles

Canonical identity/style authority: `assets/homie-loaders/sources/manager/decode-goal.png` (current file SHA-256 `889dad569156d8f1376931db7a540d1f24c9c33dc158e18edea68744c4cd6878`). User reference: `/var/folders/kz/c40hnqf51b78kdv_h64qjj0h0000gn/T/codex-clipboard-b64f7135-4e22-43ae-b302-7290f0b10d4b.png` (current file SHA-256 `0054699018e08f9e0028c748040c27a53043bc50e13347fa7476c8f028c43d33`), used only for wardrobe/toast guidance.

### Exact accepted generation prompt

Persisted verbatim in `imagegen-prompt.txt`:

```text
Use case: stylized-concept
Asset type: immutable 2x2 authored sprite plate for a 256px transparent loading animation
Input images: Image 1 is the ONLY identity, face, body-proportion, and ink-and-watercolour illustration-style reference; preserve its recognizable canonical brown-haired white male Manager Homie. Image 2 is wardrobe and toast-pose reference ONLY; do not copy that person's face, identity, poster design, lettering, frame, or branding.
Scene/backdrop: one perfectly uniform flat solid #00ff00 chroma-key field across the entire square sheet, including broad outer margins and clear green gutters between four cells. No panels, boxes, art-deco frame, dividers, floor, shadows, gradients, texture, reflections, captions, or border.
Subject: the same single canonical Manager Homie repeated exactly once per cell, waist-up and front-facing, wearing a classic plain black tuxedo jacket, crisp white shirt, and simple black bow tie. He holds one simple stylized champagne coupe with a clearly opaque pale-gold drink; render the glass as clean dark ink outlines and pale wash, not translucent or reflective. Keep the exact same face, hair, gentle confident smile, head angle, torso, shoulders, lapels, bow tie, crop, camera, scale, and anchor in all four cells.
Authored action, reading order: cell 1 glass held low beside the waist; cell 2 glass lifted to lower chest; cell 3 glass at shoulder height in a clear toast; cell 4 glass raised beside the cheek as the celebratory climax. Only the glass-holding forearm and hand move. Other arm and body stay identical. Each cell is distinct and the motion must read forward and in reverse.
Style/medium: match Image 1's polished editorial ink linework and subtle watercolour wash, realistic human anatomy, warm painted texture only inside the character.
Composition/framing: exact 2x2 regular grid, four equal square authored cells, character and coupe fully contained in every cell with at least 10% green padding, no crop or overlap into gutters.
Constraints: exactly one person and exactly one coupe in each cell; exactly two arms and two hands total; five natural fingers per visible hand; hand must grip the stem coherently; one connected subject silhouette where possible; no floating fragments; no extra limbs; no body scaling, camera shift, head bob, torso wiggle, face redraw drift, prop multiplication, prop morphing, or wardrobe drift. Preserve face identity from Image 1. Use #00ff00 nowhere in subject or prop.
Avoid: Image 2 identity, photorealism, 3D, clay, vector-flat style, logos, words, initials, title text, numbers, glyphs, watermark, signature, poster frame, confetti, sparkles, motion lines, transparent glass, cast shadows, key-colour spill.
```

### Accepted edits and deterministic motion

The metadata records no targeted edit prompt. Donor panel `3` is the sole immutable source for the face, torso, tuxedo, arm, hand, and glass. Registration is `[0, 0]` and scale is `0.78` in every phase. Only the locked arm-and-glass toast rig rotates through `[-3°, -1°, 1°, 3°]`; the recorded static face/torso hash is identical in all phases and changed pixels outside the rig equal zero.

### SHA-256 locks

| Artifact | Persisted path | SHA-256 |
|---|---|---|
| Prompt | `assets/homie-loaders/qa/strict-repairs/gatsbying-manager/candidates/imagegen-prompt.txt` | `6a2681fa2dbabcd63903324509de2e95f8bd2c9a6fb13bcd45c7a5e829d72e72` |
| Accepted chroma | `assets/homie-loaders/qa/strict-repairs/gatsbying-manager/candidates/raw-chroma.png` | `df1d0cc14aa84b2fae2e9946ecbdd7b750e3751fed24da445540a87fbb879ea9` |
| Accepted raw alpha | `assets/homie-loaders/qa/strict-repairs/gatsbying-manager/candidates/raw-alpha.png` | `c33d55265d59e037361e836f46e5af1cc6bad81423f644d330053e3bbe06cdbf` |
| Locked plate | `assets/homie-loaders/qa/strict-repairs/gatsbying-manager/candidates/locked-plate.png` | `3666617a7d7b9d774cd41cb12abaadaa370150640e141d028ce1ed47afff21a9` |
| Builder | `assets/homie-loaders/qa/strict-repairs/gatsbying-manager/candidates/build_gatsbying_manager.py` | `c8c86e88921ca298d4aa83dd57a289f27d06c0e265c726dc17887bc3ea21c375` |
| Source strip | `assets/homie-loaders/qa/strict-repairs/gatsbying-manager/candidates/gatsbying-manager.png` | `a354e8b829adcb45bde98864eeb108f21a97cd3dc953361627a3a1b69098b30b` |
| Preview GIF | `assets/homie-loaders/qa/strict-repairs/gatsbying-manager/candidates/gatsbying-manager.gif` | `085f3f58c889dcd46acdf963307e7c5310ccc6bb4ac67fa6758ea223e9776f86` |

## 4. scooby-dooing-manager

### Reference roles

Canonical identity/style authority: `assets/homie-loaders/references/manager.png` (SHA-256 `9bdcf4363fb403917761987da581f4cbfe746f1fe564ad64480c582877d8fc55`). User reference: `/var/folders/kz/c40hnqf51b78kdv_h64qjj0h0000gn/T/codex-clipboard-8af1590d-40ae-413a-ba62-b9dfb922bc75.png` (SHA-256 `56d62c84084e4a2aed291d8e9b5ee9edc778b18d6ba5c28fa31fbde955793149`), used only for the frightened carrying-pose concept. The canonical Manager file controls human identity and Homies style; the dog is an original generic design.

### Exact accepted base-generation prompt

```text
Use case: stylized-concept
Asset type: original immutable character plate for a small animated web loader
Primary request: Draw an original comic scene with exactly two subjects: one adult male Manager character carrying one oversized goofy brown spotted dog. Both are startled and trembling together in a tight, funny huddle. The dog must be a new generic design, not a reproduction of any named or existing media character.
Input images: Image 1 supplies only the broad physical idea of a frightened man carrying a frightened large dog; change the dog design, colors, markings, face, and accessories into an original generic animal. Image 2 supplies the canonical Homies Manager identity and ink-and-watercolour illustration language. Preserve Image 2's adult male Manager face language, proportions, hand-drawn dark contour, restrained watercolor wash, warm paper-like coloring, and editorial character finish.
Scene/backdrop: one perfectly uniform flat solid #00ff00 chroma-key field. No floor plane.
Subject: exactly one adult male and exactly one large dog. The man supports the dog safely using exactly two clear human arms and two hands. The dog has one head, one body, exactly four legs/paws, and one tail; floppy ears, medium-brown coat, several irregular dark spots, no collar and no tag. Both face generally forward with wide comic alarmed eyes and tense posture. Entire connected pair visible.
Style/medium: canonical Homies hand-drawn ink-and-watercolour 2D illustration; natural slightly imperfect line, soft restrained wash; not 3D, not clay, not photorealistic, not anime, not flat vector art.
Composition/framing: centered full-body combined pair, generous even empty padding on every side, no crop, no detached elements, one cohesive silhouette.
Constraints: exactly two subjects total; no extra people or animals; no extra heads, faces, arms, hands, fingers, legs, paws, or tails; crisp clean outline; no use of #00ff00 in the subjects; no cast shadow, contact shadow, reflection, gradient, texture, background lighting variation, or green spill.
Avoid: any existing franchise-specific dog likeness, logos, brand marks, text, letters, numbers, glyphs, watermarks, emblems, signs, debris, particles, motion marks, duplicate props, furniture, scenery, borders, halos.
```

### Exact targeted edit 1 — remove stray motion marks

```text
Use case: precise-object-edit
Asset type: corrected immutable chroma character plate for an animated web loader
Primary request: Remove only every small black tremble squiggle or motion mark floating around the man and dog. Replace those removed marks with the exact same perfectly flat solid #00ff00 chroma color as the surrounding background.
Input image: Image 1 is the edit target and accepted subject design.
Invariants: Keep the adult male Manager and the single large brown spotted dog unchanged in identity, facial expressions, pose, anatomy, hands, paws, tail, clothing, colors, textures, outlines, scale, crop, anchor, and composition. Keep exactly one man and one dog. Keep the entire connected pair visible with the same padding. Do not redraw or restyle the subjects. Do not add anything.
Background: perfectly uniform flat #00ff00 with no shadows, gradients, floor plane, texture, halos, spill, or lighting variation.
Constraints: exactly two subjects; no motion marks, squiggles, debris, particles, text, letters, numbers, glyphs, logos, brand marks, watermark, border, shadow, or reflection.
```

### Exact targeted edit 2 — add recognizable blank collar/tag cue

```text
Use case: precise-object-edit
Asset type: final immutable chroma character plate for an animated web loader
Primary request: Add only one simple bright teal-blue collar around the large brown spotted dog's neck and one small plain green diamond-shaped tag hanging at the center of that collar. The tag must be blank: no letter, number, logo, mark, engraving, or glyph.
Input image: Image 1 is the edit target and accepted composition.
Invariants: Keep every other visible element unchanged: exactly one adult male Manager and exactly one large brown spotted dog; their identities, faces, frightened expressions, eye directions, pose, anatomy, human hands, dog paws, tail, embrace, clothing, colors, textures, outlines, scale, crop, anchor, and composition. Keep the flat chroma background unchanged. Do not alter or add any other accessory. Do not redraw or restyle the subjects.
Background: perfectly uniform flat solid #00ff00 with no shadows, gradients, floor plane, texture, halos, spill, or lighting variation.
Constraints: exactly two subjects total; exactly one collar and exactly one small blank diamond tag; no motion marks, squiggles, debris, particles, text, letters, numbers, glyphs, logos, brand marks, watermark, border, shadow, or reflection.
```

### Accepted edits and deterministic motion

Both targeted edits were applied sequentially to the accepted composition: first removing all stray tremble marks, then adding exactly one teal-blue collar and one blank green diamond tag. The final Manager-and-dog plate is immutable. The builder applies only a shared integer translation to the entire connected rig with offsets `[[-9, 0], [-3, -2], [3, 2], [9, 0]]`; no subject part is independently redrawn or moved.

### SHA-256 locks

| Artifact | Persisted path | SHA-256 |
|---|---|---|
| Prompt/edit record | `assets/homie-loaders/qa/strict-repairs/scooby-dooing-manager/candidates/accepted-imagegen-prompts.md` | `3ca7ff7b5b4ec2c3d4f1db3d15b8ef2ae2254257c1950a65cf2147bf81844289` |
| Accepted chroma | `assets/homie-loaders/qa/strict-repairs/scooby-dooing-manager/candidates/raw/scooby-dooing-manager-chroma.png` | `f1974fd98e5240af0a8527bbf3548209885fc304a4884dbf65325115dfdfb2dc` |
| Accepted alpha | `assets/homie-loaders/qa/strict-repairs/raw/scooby-dooing-manager-alpha.png` | `c29f3a2e02ca6f01405df62535cc3d41f8503d28bf10aaeb386b585c74555d55` |
| Locked plate | `assets/homie-loaders/qa/strict-repairs/scooby-dooing-manager/candidates/frames/scooby-dooing-manager/locked-manager-and-dog.png` | `a2a910d43bfafa361405273d59c7f6fc5bc95946c97a72b355aaeb8fe0f7fe02` |
| Builder | `assets/homie-loaders/scripts/build_candidate_scooby_dooing_manager.py` | `9f95b098682896e044889bfe4cb6967361f460606584435f7445d3fb4075fd5a` |
| Source strip | `assets/homie-loaders/qa/strict-repairs/scooby-dooing-manager/candidates/sources/wildcard/scooby-dooing-manager.png` | `61dc3d62762f91cd870c2593e87b5d4b93aca1b54c91f46062d807edc183b4be` |
| Preview GIF | `assets/homie-loaders/qa/strict-repairs/scooby-dooing-manager/candidates/gifs/wildcard/scooby-dooing-manager.gif` | `cf5003e386102c932bd60feba93bc9f82df6224ac421fffbed0abd5431187f07` |

## 5. walter-whiting-crm

### Reference roles

The accepted fresh generation used only `assets/homie-loaders/references/crm.png` (SHA-256 `033872e6e3ed7f9fefa317090c204a243ccfbe541e766ef8786e3e92ed46a59d`) as the canonical CRM identity/style authority. The user reference `/var/folders/kz/c40hnqf51b78kdv_h64qjj0h0000gn/T/codex-clipboard-7ec6cb98-2f09-4c75-9994-13ac1cd2f11f.png` (SHA-256 `cded49c6204aad4ebb3162311c4f8d5c270396a36a88db4420155a956b32eca4`) supplied concept guidance only and was not an input to the accepted final generation.

### Exact accepted fresh-generation prompt

```text
Use case: stylized-concept
Asset type: final immutable character plate for a small animated web loader
Primary request: Draw exactly one adult male CRM Homie as an original brooding laboratory-deal specialist. He is unmistakably the same canonical dark-skinned bald male CRM identity shown in Image 1, now wearing a bright yellow protective hazmat coverall, clear eyeglasses, and a compact gray respirator hanging at his neck, while carrying exactly one plain dark hard-sided briefcase in one hand. His expression is serious and brooding. This must remain an original Homies character, not a likeness of any real person.
Input image: Image 1 is the mandatory canonical identity and style source. Preserve its deep warm-brown skin tone, bald head, recognizable CRM facial proportions, broad friendly facial structure, nose, eyes, brows, natural adult anatomy, hand-drawn dark contour, restrained watercolor wash, and editorial Homies finish. A very small restrained dark goatee may be added as a costume cue only if the canonical CRM face remains unmistakable.
Scene/backdrop: perfectly flat uniform solid #00ff00 chroma-key field; no floor plane.
Subject: exactly one full-body adult dark-skinned bald man with one head and face, exactly two arms, two hands, and two legs. Bright yellow hood-down protective coverall with a simple zipper and elastic cuffs; one pair of clear eyeglasses; one compact gray respirator resting at the front of his neck with simple straps; exactly one plain dark rectangular briefcase held naturally at his side; simple white shoes. No other object.
Style/medium: canonical Homies hand-drawn 2D ink-and-watercolour illustration matching Image 1, with a natural slightly imperfect outline, soft restrained wash, and clean readable silhouette; not photorealistic, not 3D, not clay, not anime, not flat vector art.
Composition/framing: centered full-body standing figure, entire head, shoes, respirator, both hands, and briefcase visible, generous even padding on all sides, no crop, no contact shadow.
Lighting/mood: neutral clean illustration light; serious, controlled, intelligent, understated.
Constraints: canonical dark-skinned CRM identity must remain obvious at thumbnail size; one subject only; exactly one briefcase, one eyeglasses pair, and one neck respirator; no extra people, heads, faces, arms, hands, fingers, legs, bags, masks, respirators, filters, tubes, cases, boxes, containers, props, money, drugs, weapons, chairs, or scenery; connected anatomy; no #00ff00 inside the subject; no shadow, reflection, gradient, texture, background lighting variation, or green spill.
Avoid: any real-person likeness, light skin, logos, brand marks, text, letters, numbers, glyphs, hazard symbols, watermarks, badges, emblems, signs, labels, debris, particles, motion marks, smoke, duplicate accessories, borders, halos.
```

### Accepted edits and deterministic motion

An earlier light-skinned plate was rejected. A targeted edit attempted against that rejected plate was blocked by input moderation and produced no accepted output; it did not influence the final. The accepted fresh plate is the canonical dark-skinned bald male CRM with a yellow suit, one glasses pair, one neck respirator assembly, and exactly one briefcase.

The entire accepted character plate is static. Only a deterministic glasses glint and respirator-filter highlight vary inside the saved local mask. The glint x positions are `[299, 309, 320, 331]` pixels and the filter radii are `[2, 3, 5, 3]` pixels. Body, hands, suit, respirator geometry, briefcase, silhouette, crop, scale, and anchor remain locked.

### SHA-256 locks

| Artifact | Persisted path | SHA-256 |
|---|---|---|
| Prompt record | `assets/homie-loaders/qa/strict-repairs/walter-whiting-crm/candidates/accepted-imagegen-prompts.md` | `d6f79fe8fabea77c669b61c597e98526e0c95531825f0daeda174df61411bd69` |
| Accepted chroma | `assets/homie-loaders/qa/strict-repairs/walter-whiting-crm/candidates/raw/walter-whiting-crm-chroma.png` | `0acddc575a1789fba5cdc629bdcf117762676da416a440731e26c88ffddb4836` |
| Accepted alpha | `assets/homie-loaders/qa/strict-repairs/raw/walter-whiting-crm-alpha.png` | `994483ad6390e70ac43a862a9213a5d5b24ead56aa2b3e3bf643c900003e3230` |
| Locked plate | `assets/homie-loaders/qa/strict-repairs/walter-whiting-crm/candidates/frames/walter-whiting-crm/locked-crm-hazmat-respirator-and-briefcase.png` | `07165a8f1cc02b6b3a30adc167060984bb2ad6bf5233f68932b9e9c3a431f1cb` |
| Allowed local-highlight mask | `assets/homie-loaders/qa/strict-repairs/walter-whiting-crm/candidates/frames/walter-whiting-crm/allowed-glasses-and-respirator-highlight-mask.png` | `77e58273770baec6116cb4e843b7a2a9b70830fd2d3d03cd7c1d824695ad0173` |
| Builder | `assets/homie-loaders/scripts/build_candidate_walter_whiting_crm.py` | `27f79d0537ce9476012216a36ad980a49980ebd814dc2593ddbd16e0206d2268` |
| Source strip | `assets/homie-loaders/qa/strict-repairs/walter-whiting-crm/candidates/sources/wildcard/walter-whiting-crm.png` | `3c30d08ce62138368d0ec71a261b0e573de85c0520acc0a26db47ad680939944` |
| Preview GIF | `assets/homie-loaders/qa/strict-repairs/walter-whiting-crm/candidates/gifs/wildcard/walter-whiting-crm.gif` | `d1086c933c49a0e2e9ee1959fd3fcf768b042e97f5637318d27d5d58dd5f959d` |

## 6. buffying-offers

### Reference roles

Canonical identity/style authority: `assets/homie-loaders/references/offers.png` (SHA-256 `970e5dac19b45638e725c3aab25d24cc0b908612606441881cd38ebd5600e744`). User reference: `/var/folders/kz/c40hnqf51b78kdv_h64qjj0h0000gn/T/codex-clipboard-46d01a39-bd3f-4752-a906-6df4cea2d6b5.png` (SHA-256 `f851ea446c16fcdbb045bb98ed7a4d802a67d739af24554982aa8a6a09b7fb3c`), used only for the female-hunter, black-outfit, and one-stake concept.

### Exact accepted generation prompt

```text
Use case: stylized-concept
Asset type: original immutable character plate for a small animated web loader
Primary request: Draw exactly one adult female Offers Homie as a confident supernatural-offer hunter in a simple all-black outfit, holding exactly one plain wooden stake. She stands in a compact alert ready pose with focused determination and clear readable anatomy.
Input images: Image 1 is concept reference only for a young adult female hunter, black outfit, and one wooden stake; do not copy its poster layout, typography, splatter, background, photographic likeness, or franchise graphics. Image 2 is the canonical female Offers Homie identity and ink-and-watercolour style reference. Preserve Image 2's recognizable adult female Offers face language, warm off-white skin rendering, brown hair identity, natural proportions, hand-drawn dark contour, restrained watercolour shading, and editorial Homies finish while changing clothing and pose as requested.
Scene/backdrop: perfectly flat uniform solid #00ff00 chroma-key field for local background removal; no floor plane.
Subject: exactly one full-body adult woman with one head and face, exactly two arms, two hands, and two legs. Simple fitted black short-sleeve top, plain black trousers, and black ankle boots. Brown hair tied back in a practical loose ponytail. She grips exactly one short tapered wooden stake in one anatomically clear hand, angled diagonally upward and fully visible; her other hand is empty and open. No other object or weapon.
Style/medium: canonical Homies hand-drawn 2D ink-and-watercolour illustration, natural slightly imperfect outline and soft restrained wash; not 3D, not clay, not photorealistic, not anime, not flat vector art.
Composition/framing: centered complete full-body figure, head, hair, both hands, boots, and entire stake visible, generous even padding on all sides, no crop, no shadow.
Lighting/mood: neutral clean illustration light; focused, capable, understated, not horror.
Constraints: exactly one subject and exactly one wooden stake; no extra people, heads, faces, arms, hands, fingers, legs, stakes, weapons, props, jewelry, scenery, or furniture; connected natural anatomy and clear empty second hand; do not use #00ff00 within the subject; no cast shadow, contact shadow, reflection, gradient, texture, background lighting variation, or green spill.
Avoid: logos, brand marks, text, letters, numbers, glyphs, watermarks, badges, emblems, signage, blood, splatter, debris, particles, motion marks, duplicate accessories, borders, halos.
```

### Accepted edits and deterministic motion

No targeted edit prompt is recorded. The accepted female Offers identity, anatomy, empty second hand, black outfit, and exactly one stake form one immutable rig. The builder applies only a rigid boot-anchored lean around pivot `[313, 550]` through `[2.8°, 0.9°, -0.9°, -2.8°]`; it does not animate or redraw individual body parts or the stake.

### SHA-256 locks

| Artifact | Persisted path | SHA-256 |
|---|---|---|
| Prompt record | `assets/homie-loaders/qa/strict-repairs/buffying-offers/candidates/accepted-imagegen-prompts.md` | `f3a4ed4f005e2262f420a30dc1943770415eff93259bd23b32964c5ef39d5e8e` |
| Accepted chroma | `assets/homie-loaders/qa/strict-repairs/buffying-offers/candidates/raw/buffying-offers-chroma.png` | `694169c8e047fef7b8f9aacd3018bd5026317d865d93e580882eef3f40ca51e5` |
| Accepted alpha | `assets/homie-loaders/qa/strict-repairs/raw/buffying-offers-alpha.png` | `e16759f730bced67498091968b19d339409f0ca1a50dab254bc9548057e81f29` |
| Locked plate | `assets/homie-loaders/qa/strict-repairs/buffying-offers/candidates/frames/buffying-offers/locked-female-offers-and-single-stake.png` | `9b9929b6a83842b93ec1eefe84414b453d7c5b320374d3302733c4ab2c7a6ee9` |
| Builder | `assets/homie-loaders/scripts/build_candidate_buffying_offers.py` | `d52c8b6dec8adc741286a9da6a4ff1207a4e97b7b6848bff20bff7506e0c18f1` |
| Source strip | `assets/homie-loaders/qa/strict-repairs/buffying-offers/candidates/sources/wildcard/buffying-offers.png` | `883c3f2ceb2b749c22e7215b3556a3c9df7a51e9a873788aea99ab677ef26ea8` |
| Preview GIF | `assets/homie-loaders/qa/strict-repairs/buffying-offers/candidates/gifs/wildcard/buffying-offers.gif` | `6565844e06abce38749e33523c26c52d03b4f1975c4837860f16356b4560f572` |

## 7. ron-burgunding-cma

### Reference roles

Canonical identity/style authority: `assets/homie-loaders/sources/cma/cma-deck-reveal.png` (current file SHA-256 `5cf07ac060c962cd113b9c77d5311071e18ebaafbdcbc4f7500c42d01edc8b58`). User reference: `/var/folders/kz/c40hnqf51b78kdv_h64qjj0h0000gn/T/codex-clipboard-06edf20e-270d-48a4-9f14-74dc66465892.png` (current file SHA-256 `0c7d035b5fd1ff86684dcfb1b40996a72aafc1096280743ca34fcc0674f27c68`), used only for wardrobe/toast guidance.

### Exact accepted generation prompt

Persisted verbatim in `imagegen-prompt.txt`:

```text
Use case: stylized-concept
Asset type: immutable 2x2 authored sprite plate for a 256px transparent loading animation
Input images: Image 1 is the ONLY identity, face, body-proportion, and ink-and-watercolour illustration-style reference; preserve its recognizable canonical Black male CMA Homie. Image 2 is wardrobe and raised-tumbler pose reference ONLY; do not copy that person's face, identity, news backdrop, desk, logos, lettering, or branding.
Scene/backdrop: one perfectly uniform flat solid #00ff00 chroma-key field across the entire square sheet, including broad outer margins and clear green gutters between four cells. No panels, boxes, dividers, desk, floor, shadows, gradients, texture, reflections, captions, or border.
Subject: the same single canonical CMA Homie repeated exactly once per cell, waist-up and front-facing, wearing a rich burgundy-red 1970s-style suit jacket, crisp white shirt, and plain diagonally striped dark tie with no symbols. Add a neat dark moustache while preserving Image 1's face and identity. He holds one simple straight-sided low tumbler containing an opaque amber drink; render it as dark ink contours and pale wash, not translucent or reflective. Keep the exact same face, haircut, moustache, composed expression, head angle, torso, shoulders, lapels, tie, crop, camera, scale, and anchor in every cell.
Authored action, reading order: cell 1 tumbler held low beside waist; cell 2 tumbler lifted to lower chest; cell 3 tumbler held at shoulder in a direct confident toast; cell 4 tumbler raised beside cheek as the climax. Only the glass-holding forearm and hand move. Other hand and body remain identical. Each cell distinct; sequence reads clearly forward and in reverse.
Style/medium: match Image 1's polished editorial ink linework and subtle watercolour wash, realistic human anatomy, painted texture only inside character and prop.
Composition/framing: exact 2x2 regular grid, four equal square cells, character and glass fully contained with at least 10% green padding, no crop or overlap into gutters.
Constraints: exactly one person and one tumbler per cell; exactly two arms and two hands total; five natural fingers per visible hand; coherent grip; no floating fragments; no extra limbs; no body scaling, camera shift, head bob, torso wiggle, face redraw drift, moustache drift, glass multiplication, glass morphing, or wardrobe drift. Preserve Image 1 identity. Use #00ff00 nowhere in subject or prop.
Avoid: Image 2 identity, photorealism, 3D, clay, vector-flat style, desk, logos, words, channel marks, title text, numbers, glyphs, watermark, signature, transparent glass, ice cubes, reflections, confetti, motion lines, cast shadows, key-colour spill.
```

### Accepted edits and deterministic motion

The metadata records no targeted edit prompt. Donor panel `3` is the sole immutable source for the face, torso, suit, arm, hand, and tumbler. Registration is `[0, 0]` and scale is `0.78` in every phase. Only the locked arm-and-tumbler toast rig rotates through `[-3°, -1°, 1°, 3°]`; the recorded static face/torso hash is identical in all phases and changed pixels outside the rig equal zero.

### SHA-256 locks

| Artifact | Persisted path | SHA-256 |
|---|---|---|
| Prompt | `assets/homie-loaders/qa/strict-repairs/ron-burgunding-cma/candidates/imagegen-prompt.txt` | `b69d4c31863191863c874bb057fa355ba3ea5bae399e8db04aaaf331aea55a2e` |
| Accepted chroma | `assets/homie-loaders/qa/strict-repairs/ron-burgunding-cma/candidates/raw-chroma.png` | `3036d68b63f0b936467ce514f031a2fe1f92c25afd3229b2b252b7b395688f0f` |
| Accepted raw alpha | `assets/homie-loaders/qa/strict-repairs/ron-burgunding-cma/candidates/raw-alpha.png` | `c29710882a6ea32d80d120290fd072db31081c3b2d1a68095ac5aa91d371a793` |
| Locked plate | `assets/homie-loaders/qa/strict-repairs/ron-burgunding-cma/candidates/locked-plate.png` | `d17ef3d673d2337f7d28ccd0cf1496e02e53ceed5e44a6fe35cbefa3eecb9e72` |
| Builder | `assets/homie-loaders/qa/strict-repairs/ron-burgunding-cma/candidates/build_ron_burgunding_cma.py` | `b36ff12d8e0b6e22a440bbda1a7add56f26698de5e462600f2a151ed28d3c00d` |
| Source strip | `assets/homie-loaders/qa/strict-repairs/ron-burgunding-cma/candidates/ron-burgunding-cma.png` | `0049af3ccaf578d2713c271b0f956cfe6d6d18b88cc29d2752f42299349f9b2f` |
| Preview GIF | `assets/homie-loaders/qa/strict-repairs/ron-burgunding-cma/candidates/ron-burgunding-cma.gif` | `9747e6408df19ae78d84804fbb7e11b4bc03d4f88a92e27b03612a68243503fd` |

## 8. tony-starking-marketing

### Reference roles

The accepted generation used `assets/homie-loaders/references/marketing.png` (SHA-256 `ebc684e0e97a4dba458a1287e1796a11d4f0937701827ba17b621f2562c85841`) as the canonical Marketing identity/style input. The observed user reference `/var/folders/kz/c40hnqf51b78kdv_h64qjj0h0000gn/T/codex-clipboard-b3c150bd-6e34-4abf-be0a-8ea402c62838.png` (SHA-256 `1d21b57d9a1dc7c966be21b9beffc24420a9b5f64358e83481a0dbe8ad429522`) supplied wardrobe/open-palm action guidance only and was not sent in the accepted generation.

### Exact accepted generation prompt

```text
Use case: precise-object-edit
Asset type: isolated illustrated character plate
Primary request: Re-illustrate the same fictional adult male Homies character from Image 1 in exactly the same friendly editorial line-and-watercolor style. Preserve his face, short dark hair, full beard, body proportions, and warm confident expression. Replace the hoodie and cargo pants with an original red-and-ochre padded technology-demo suit made of simple cloth-and-plastic panels, with no recognizable franchise design. Repose him so his complete body faces three-quarter forward, one ordinary bare hand is held open in a friendly wave toward the viewer, and the other arm hangs naturally. The open hand is simply a hand with no device and no light.
Scene/backdrop: perfectly flat solid #00ff00 chroma-key field, uniform edge to edge.
Composition/framing: one complete head-to-toe figure centered on a square canvas, ample padding around hair, hands, elbows, and shoes; face unobstructed.
Style/medium: keep the canonical Homies fine ink outline and gentle watercolor shading; flat editorial character art, not photorealistic and not 3D.
Constraints: one fictional character, ordinary anatomy, two arms, two hands, two legs; face visible; original generic suit with no symbols; no text, letters, numbers, logos, marks, watermarks, props, effects, particles, scenery, shadow, reflection, or floor plane. No #00ff00 in the subject.
Avoid: any real person or celebrity resemblance, any recognizable superhero or movie costume, combat, weapons, glowing devices, circular chest elements, extra fingers or limbs, fused anatomy, debris, crop.
```

### Exact accepted targeted-edit prompt

```text
Use case: precise-object-edit
Asset type: corrected immutable illustrated character plate for an animated loader
Input image: Image 1 is the edit target.
Primary request: Make exactly two localized costume corrections to Image 1. First, replace only the raised bare forearm and raised bare open hand with a coherent red-and-muted-gold armored gauntlet that matches the existing suit, while preserving the exact raised-hand silhouette, open-palm pose, correct five-finger anatomy, wrist position, arm position, and scale. Inset one clear simple circular white-blue indicator light in the center of that open palm. Second, inset one clear simple circular white-blue indicator light at the center of the red chest panel.
Invariants: preserve the character's face, beard, hair, expression, identity, head, neck, body proportions, stance, all limb positions, other hand, legs, boots, existing red-and-gold suit panels, exact framing, exact subject scale, and the perfectly uniform solid #00ff00 background. Keep the canonical Homies dark-ink and watercolor illustration style unchanged. Change only the raised forearm/hand surface and the two circular indicator-light insets.
Constraints: helmet absent and face unobstructed; one character; normal anatomy; exactly two arms and two hands; raised hand retains exactly five readable fingers; only two contained circular lights, one palm and one chest; no external glow rings, rays, sparks, particles, smoke, text, letters, numbers, logos, symbols, glyphs, brand marks, watermarks, extra objects, scenery, floor, shadows, reflections, or crop. Do not alter or grade the #00ff00 background.
Avoid: face drift, body redraw, pose drift, scale change, camera change, duplicate hands, extra fingers, fused anatomy, bare raised forearm, recognizable franchise logos, chest emblems, debris.
```

### Accepted edits and deterministic motion

Three generation attempts were blocked before acceptance. The persisted targeted edit corrected the accepted generation target recorded in `provenance.json`. After alpha extraction, the character, anatomy, red/gold suit, raised open palm, and chest reactor were saved as one locked plate. No plate pixel moves; only masked palm and chest energy overlays pulse through four deterministic intensities.

### SHA-256 locks

| Artifact | Persisted path | SHA-256 |
|---|---|---|
| Generation prompt | `assets/homie-loaders/qa/strict-repairs/tony-starking-marketing/candidates/generation-prompt.txt` | `9af6af6cd2d4fd14c1f35b3a47679feea923d6cb5b24f93b379c36e488577c11` |
| Targeted-edit prompt | `assets/homie-loaders/qa/strict-repairs/tony-starking-marketing/candidates/edit-prompt.txt` | `c322c91482e61bff2c086ac40021ac77ef3e44ea3297c018ac6d998d13537d2d` |
| Accepted chroma | `assets/homie-loaders/qa/strict-repairs/tony-starking-marketing/candidates/raw/tony-starking-marketing-chroma.png` | `6851f2e0ced2df66c39e05b04c022104a5ce9f87bcfa784963c527432504f0c3` |
| Accepted alpha | `assets/homie-loaders/qa/strict-repairs/raw/tony-starking-marketing-alpha.png` | `4d5c485655b1ce4d963fcf6ab7e5e6c7fe5247fd743d66e2c2ff3b68f5fa5725` |
| Locked plate | `assets/homie-loaders/qa/strict-repairs/tony-starking-marketing/candidates/frames/tony-starking-marketing/locked-character-suit-and-emitters.png` | `1cfea4a8feec6e9b58425bed3e94e504f07612b4c59f6383106677941ca69c65` |
| Builder | `assets/homie-loaders/scripts/build_tony_starking_marketing_candidate.py` | `010a41532075a55ad6d1eb22c45bbaab2bd29b1f2b3465de5c60e4a607ac028f` |
| Source strip | `assets/homie-loaders/qa/strict-repairs/tony-starking-marketing/candidates/sources/wildcard/tony-starking-marketing.png` | `0f7331eb81717dc6920d26fb4b8ec25cefec356980be5777b48cade22dd7aea9` |
| Preview GIF | `assets/homie-loaders/qa/strict-repairs/tony-starking-marketing/candidates/gifs/wildcard/tony-starking-marketing.gif` | `5abb05d4b2a993c127f2585b91eea0f8ffdff9bbe7c5bb8ae837b9b4c1c9b17a` |

## 9. tyler-durdening-listings

### Reference roles

The accepted generation used `assets/homie-loaders/references/listings.png` (SHA-256 `15ffada285d822e22f3a8dd448b30bd94b79b2337a82a3a6a161a1833eafac0b`) as the canonical Listings identity/style input. The observed user reference `/var/folders/kz/c40hnqf51b78kdv_h64qjj0h0000gn/T/codex-clipboard-7496cc57-60bf-4a0b-98f4-bc7aebd865ed.png` (SHA-256 `e4b16b5bffc5e512b0d23f5511b141b02a56d5d9587b4950f9821ae71a479342`) supplied wardrobe/action guidance only and was not sent in the accepted generation.

### Exact accepted generation prompt

```text
Use case: identity-preserve
Asset type: immutable isolated source plate for a 2x2 animated character loader
Primary request: Keep the same canonical illustrated male Listings Homie identity and Homies drawing style from Image 1: young adult man, swept brown hair, clear friendly face, slim natural proportions, fine dark ink contours, softly shaded editorial watercolor fill. Change only his clothing, eyewear, and pose. Dress him in an original red leather jacket over a maroon-and-cream abstract patterned open-collar shirt, dark charcoal trousers, and simple dark shoes. Change his glasses to translucent red rectangular sunglasses while keeping the canonical face recognizable. Pose him head-to-toe in a controlled non-contact shadow-boxing guard: feet staggered but both planted, knees relaxed, torso upright and still, elbows held wide, both forearms raised mostly beside rather than across the torso, exactly two closed fists clearly visible near shoulder height, with clean green gaps around the forearms wherever anatomically natural.
Scene/backdrop: perfectly flat solid #00ff00 chroma-key background, uniform edge to edge.
Style/medium: canonical Homies hand-drawn editorial character illustration; crisp dark outline and restrained watercolor shading; not photorealistic, not cinematic, not 3D.
Composition/framing: centered square, complete hair, elbows, fists, trousers, and both shoes visible with generous padding; no crop.
Constraints: exactly one fictional person; ordinary anatomy with one head, two arms, two clenched hands, two legs; stationary balanced body posture; no text, letters, numbers, logos, brand marks, symbols, watermarks, props, contact with anyone, scenery, floor, shadow, reflection, or particles. Background is exactly uniform #00ff00 without gradient or lighting variation. No #00ff00 in subject.
Avoid: resemblance to a real actor or celebrity, recognizable film-specific face, violence against a person, weapons, extra or fused anatomy, duplicate fists, hands obscuring face, crossed arms, arms merged into torso, body twist, extreme foreshortening, debris, crop.
```

### Accepted edits and deterministic motion

No image-generation edit prompt is recorded. The builder reuses one immutable generated Listings plate. It removes the original two guard fists once, then uses exactly two attached fist/forearm rigs for left jab, half-retraction, two-fist guard, and right jab. No pixel outside the saved two-forearm motion mask may differ from the immutable plate. The settled evidence records zero outside-mask mismatches in all four phases and two consecutive identical rebuilds.

### SHA-256 locks

| Artifact | Persisted path | SHA-256 |
|---|---|---|
| Generation prompt | `assets/homie-loaders/qa/strict-repairs/tyler-durdening-listings/candidates/generation-prompt.txt` | `fba92546c7e82c13f08b7e2c68ab07920b0b0dd892476d10fd0dbff3d5468066` |
| Accepted chroma | `assets/homie-loaders/qa/strict-repairs/tyler-durdening-listings/candidates/raw/tyler-durdening-listings-chroma.png` | `04381eba353057933e42a79a94564ae6d2e16656df23c921a20fdd5c71e56a61` |
| Accepted alpha | `assets/homie-loaders/qa/strict-repairs/raw/tyler-durdening-listings-alpha.png` | `ba9e1e5fa3b1d65c9cbc7c9ecb404b493a95779a09cc7f5e49dd699233c360a5` |
| Immutable plate | `assets/homie-loaders/qa/strict-repairs/tyler-durdening-listings/candidates/frames/tyler-durdening-listings/immutable-generated-listings-plate.png` | `225982b64e9cd75596da90afc44c1ff63d8943d499d1010707af4ae4b6d67553` |
| Allowed forearm mask | `assets/homie-loaders/qa/strict-repairs/tyler-durdening-listings/candidates/frames/tyler-durdening-listings/allowed-left-and-right-forearm-mask.png` | `5926423a903f1db3d410487a9ebf53415670d47001d1283be2902130ab9995d7` |
| Builder | `assets/homie-loaders/scripts/build_tyler_durdening_listings_candidate.py` | `7a25bcd688442a36195c5f543600a0537832b1282a90778dc64c8cf0c35a75f1` |
| Source strip | `assets/homie-loaders/qa/strict-repairs/tyler-durdening-listings/candidates/sources/wildcard/tyler-durdening-listings.png` | `3f04d49bfeca9aa98c3aae199fbb98b8752e7c92b061fba4e451835e6df945b2` |
| Preview GIF | `assets/homie-loaders/qa/strict-repairs/tyler-durdening-listings/candidates/gifs/wildcard/tyler-durdening-listings.gif` | `abfba32629dab614567f5c07444e85c75770f29528e566bd67c7ee7e521a6bf1` |

## 10. robin-hooding-manager

### Reference roles

The accepted generation used `assets/homie-loaders/references/manager.png` (SHA-256 `9bdcf4363fb403917761987da581f4cbfe746f1fe564ad64480c582877d8fc55`) as the canonical Manager identity/style input. The observed user reference `/var/folders/kz/c40hnqf51b78kdv_h64qjj0h0000gn/T/codex-clipboard-6fa03572-3817-44c6-a267-0ad94e82aa04.png` (SHA-256 `59ea975463351fb6379d93ffd05cc0f761bacc85e66e0de11e2b10f28ea988d1`) supplied wardrobe/action guidance only and was not sent in the accepted generation.

### Exact accepted generation prompt

```text
Use case: identity-preserve
Asset type: immutable isolated source plate for a 2x2 animated character loader
Primary request: Keep the same canonical illustrated male Manager Homie identity and Homies drawing style from Image 1: adult man, swept brown hair, clean-shaven friendly face, natural human proportions, fine dark ink contours, softly shaded editorial watercolor fill. Change only his wardrobe and pose. Dress him in a classic storybook forest-archer outfit: muted forest-green tunic and leggings, warm brown belt and boots, short green cap with exactly one red feather, and simple brown leather wrist guards. Pose him head-to-toe in a controlled traditional archery demonstration at full draw: torso in stable three-quarter profile, one anatomically correct hand holding exactly one simple curved wooden bow, the other anatomically correct hand drawing the string to a clear nock beside his cheek, exactly one arrow resting on the bow and pointing safely toward empty off-canvas space. His face remains clearly visible.
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background, uniform edge to edge.
Style/medium: canonical Homies hand-drawn editorial character illustration; crisp dark outline and restrained watercolor shading; storybook costume rendered within the established Homies style; not photorealistic, not cinematic, not 3D.
Composition/framing: centered square, complete cap feather, bow arc, arrow tip, elbows, legs, and both boots visible with generous padding on every side; no crop. Keep bow and arrow fully within the frame and clearly separate from limbs.
Constraints: exactly one fictional person; one head, two arms, two hands, two legs; exactly one bow, one bowstring, one arrow, one nock, one red hat feather; stable anatomy; clear hand grips; no quiver and no spare arrows; no target, animal, opponent, text, letters, numbers, logos, symbols, glyphs, brand marks, watermarks, scenery, floor, shadow, reflection, particles, or debris. Background is exactly uniform #ff00ff with no gradient or lighting variation. No #ff00ff in subject.
Avoid: resemblance to any real actor or celebrity, injury, impact, violence, extra limbs or fingers, duplicate bow, duplicate string, multiple arrows, merged bow and arm, arrow passing through fingers or face, malformed hands, cropped bow or feather.
```

### Accepted edits and deterministic motion

No image-generation edit prompt is recorded. A deterministic frame-shared HSV transform changes only green upper-garment pixels inside fixed hat/tunic/sleeve/hem polygons to deep muted burgundy; alpha geometry is unchanged, and olive leggings, tan leather, skin, bow, feather, and metal pixels remain unchanged. The recoloured immutable Manager character/bow plate is then reused in every phase. Only the masked string, nock, shaft overlay, fletching, and arrowhead rig varies; the character, bow base, bow hand, body, crop, scale, and anchor remain locked. The nock travels 15 pixels while both string endpoints remain fixed at the bow tips.

### SHA-256 locks

| Artifact | Persisted path | SHA-256 |
|---|---|---|
| Generation prompt | `assets/homie-loaders/qa/strict-repairs/robin-hooding-manager/candidates/generation-prompt.txt` | `eddc4a618c949afe2b8352cf8ccb308682a26c2f5958343739cebbfc9300dff7` |
| Accepted chroma | `assets/homie-loaders/qa/strict-repairs/robin-hooding-manager/candidates/raw/robin-hooding-manager-chroma.png` | `8cad9542c35a82d428e66693389cd38c26026513a4eab1aaab3fb3846863eb04` |
| Accepted alpha | `assets/homie-loaders/qa/strict-repairs/raw/robin-hooding-manager-alpha.png` | `a879e15c39c031afa2d6168f07f291c5b7033a8d2c7a576177c94bc4f8c584a7` |
| Frame-shared recolour mask | `assets/homie-loaders/qa/strict-repairs/robin-hooding-manager/candidates/frames/robin-hooding-manager/frame-shared-outlaw-recolour-mask.png` | `8c1f75dbaf0787ee824bb47044269ddf79c7a162210a0650ec8bd2d2a431cd9e` |
| Recoloured immutable plate | `assets/homie-loaders/qa/strict-repairs/robin-hooding-manager/candidates/frames/robin-hooding-manager/immutable-manager-archer-plate.png` | `0392a11539a8a4a325c8df6c2b23e5c61da1a634f25efc1c97f1c4a18b36fc1b` |
| Locked character/bow base | `assets/homie-loaders/qa/strict-repairs/robin-hooding-manager/candidates/frames/robin-hooding-manager/locked-character-and-bow-base.png` | `5afa18dcdbf1228c3858ad4e7b084e1329d18587d1c9e93debb29fef23f85006` |
| Allowed string/arrow mask | `assets/homie-loaders/qa/strict-repairs/robin-hooding-manager/candidates/frames/robin-hooding-manager/allowed-single-string-arrow-nock-rig-mask.png` | `7937824f6dbcf3302d2f4f9bb9727e52d73e5dcf40ffdde958558c8e6c3ae31d` |
| Builder | `assets/homie-loaders/scripts/build_robin_hooding_manager_candidate.py` | `4d5e27a940d949762df67e089c997dceeae5f4a8dbb41ceccf0f9d4f2c99e1ea` |
| Source strip | `assets/homie-loaders/qa/strict-repairs/robin-hooding-manager/candidates/sources/wildcard/robin-hooding-manager.png` | `45b28eac67576766fcf254d6affb1d2ec5180f29bc235091da73094f2d37c171` |
| Preview GIF | `assets/homie-loaders/qa/strict-repairs/robin-hooding-manager/candidates/gifs/wildcard/robin-hooding-manager.gif` | `33d8044924f5f549a8856ad5671871f92fc4dc5932ed98549e899defae50ac13` |

## 11. gary-veeing-crm

### Reference roles

Canonical identity/style authority: `assets/homie-loaders/sources/crm/lead-score.png` (current file SHA-256 `4aa80f3e66a6d63f723fa1861bdeddcea3e57264fd76e192fcea9b7a94a69e26`). User reference: `/var/folders/kz/c40hnqf51b78kdv_h64qjj0h0000gn/T/codex-clipboard-799e4e39-af73-463c-99b7-ce5c00410375.png` (current file SHA-256 `7bd23bbcabc6b53b617d45d6f5f21fb7d765b374dca9dcaea9b67a1030ba185a`), used only for wardrobe/open-hand speaker-pose guidance. The accepted identity remains the canonical male CRM Homie.

### Exact accepted generation prompt

Persisted verbatim in `imagegen-prompt.txt`:

```text
Use case: stylized-concept
Asset type: donor-only 2x2 authored pose plate for a deterministic 256px transparent loading animation
Input images: Image 1 is the ONLY identity, face, gender, body-proportion, and ink-and-watercolour illustration-style reference; preserve its recognizable canonical male CRM Homie. Image 2 is casual wardrobe and energetic raised-hands pose reference ONLY; do not copy that person's face, identity, stage, lettering, or branding.
Scene/backdrop: one perfectly uniform flat solid #00ff00 chroma-key field across the entire square sheet, including broad outer margins and clear green gutters between four cells. No panels, boxes, dividers, stage, floor, shadows, gradients, texture, reflections, captions, or border.
Subject: the same single canonical male CRM Homie repeated exactly once per cell, waist-up and front-facing, wearing a plain fitted navy crew-neck T-shirt and a soft light-grey knit beanie. No jacket, logos, or marks. Keep the exact same male face, beanie, friendly energetic smile, head angle, torso, shoulders, shirt neckline, crop, camera, scale, and anchor in all four cells.
Authored action donors, reading order: cell 1 both open hands low near the hips; cell 2 both arms lifting with open palms at chest/shoulder level; cell 3 both open palms beside the head; cell 4 both arms fully and joyfully raised overhead. Only both arms and hands move. Every hand remains fully visible. Each cell distinct; the rise reads clearly forward and works naturally in reverse.
Style/medium: match Image 1's polished editorial ink linework and subtle watercolour wash, realistic anatomy, warm painted texture only inside the character.
Composition/framing: exact 2x2 regular grid, four equal square cells, character and raised hands fully contained in each cell with at least 10% green padding on every side, no crop or overlap into gutters.
Constraints: exactly one male person in each cell; exactly two arms and two hands total; five natural fingers on every hand; coherent shoulder-to-elbow-to-wrist anatomy; no floating fragments; no extra limbs; no body scaling, camera shift, head bob, torso wiggle, face redraw drift, beanie drift, shirt drift, or wardrobe drift. Preserve the male CRM identity from Image 1. Use #00ff00 nowhere in the character.
Avoid: female person, Image 2 identity, photorealism, 3D, clay, vector-flat style, logos, words, initials, title text, numbers, glyphs, watermark, signature, stage, spotlight, motion lines, sparkles, props, cast shadows, key-colour spill.
```

### Accepted edits and deterministic motion

The metadata records no targeted edit prompt. Donor panel `1` is the sole immutable source for the male CRM face, torso, beanie, shirt, arms, and hands. Registration is `[0, 0]` and scale is `0.78` in every phase. Only the two locked arm rigs rotate symmetrically: left `[2°, 0.7°, -0.7°, -2°]`, right `[-2°, -0.7°, 0.7°, 2°]`. The recorded static face/torso hash is identical in all phases and changed pixels outside the rigs equal zero.

### SHA-256 locks

| Artifact | Persisted path | SHA-256 |
|---|---|---|
| Prompt | `assets/homie-loaders/qa/strict-repairs/gary-veeing-crm/candidates/imagegen-prompt.txt` | `7e952fb399091c15dd54fdb3f8c6221d344459c10dfe23ca48c996945b892373` |
| Accepted chroma | `assets/homie-loaders/qa/strict-repairs/gary-veeing-crm/candidates/raw-chroma.png` | `14a1f3e3897946029de271ec038e06a55fe0755abb594326df7ec926dedf8b4e` |
| Accepted raw alpha | `assets/homie-loaders/qa/strict-repairs/gary-veeing-crm/candidates/raw-alpha.png` | `c9649111456532d9443e1e1899d790d4c9779b83004dfd0a782b824977db4050` |
| Locked plate | `assets/homie-loaders/qa/strict-repairs/gary-veeing-crm/candidates/locked-plate.png` | `c9657edca34bc3182a025caed7402d28e93882712f4596d66dff78b23c233dea` |
| Builder | `assets/homie-loaders/qa/strict-repairs/gary-veeing-crm/candidates/build_gary_veeing_crm.py` | `4a2f1b6c270acfe5b1f5c2a7e08a1f628ad18b5d675fb9d4646bc90e63d0c9d7` |
| Source strip | `assets/homie-loaders/qa/strict-repairs/gary-veeing-crm/candidates/gary-veeing-crm.png` | `72abdf6a37492c47cc93172e311a3ec7c37f23cc7dfaa5298c832f5d796413aa` |
| Preview GIF | `assets/homie-loaders/qa/strict-repairs/gary-veeing-crm/candidates/gary-veeing-crm.gif` | `916e302a614de9edd3b7327b4eccb7f085324acc09185221958ae84d8b43ea47` |

## 12. serhanting-manager

### Reference roles

Canonical identity/style authority: `assets/homie-loaders/sources/manager/decode-goal.png` (current file SHA-256 `889dad569156d8f1376931db7a540d1f24c9c33dc158e18edea68744c4cd6878`). User reference: `/var/folders/kz/c40hnqf51b78kdv_h64qjj0h0000gn/T/codex-clipboard-b45ae1a8-331b-4130-af20-5f513478418a.png` (current file SHA-256 `fa13a79f99d0a7e940669fafcae51726a934c4d7c5382eeb99643152bfb990ea`), used only for wardrobe and jacket-buttoning pose guidance.

### Exact accepted generation prompt

Persisted verbatim in `imagegen-prompt.txt`:

```text
Use case: stylized-concept
Asset type: immutable 2x2 authored sprite plate for a 256px transparent loading animation
Input images: Image 1 is the ONLY identity, face, body-proportion, and ink-and-watercolour illustration-style reference; preserve its recognizable canonical brown-haired white male Manager Homie. Image 2 is wardrobe and jacket-buttoning pose reference ONLY; do not copy that person's face, identity, skyline, photography, or branding.
Scene/backdrop: one perfectly uniform flat solid #00ff00 chroma-key field across the entire square sheet, including broad outer margins and clear green gutters between four cells. No panels, boxes, dividers, skyline, window, floor, shadows, gradients, texture, reflections, captions, or border.
Subject: the same single canonical Manager Homie repeated exactly once per cell, waist-up, straight-on, wearing a tailored medium-blue pinstripe business suit, crisp white shirt, and pale muted-pink small-pattern tie. The pinstripes are simple continuous garment seams, never letters or glyphs. Keep the head, face, hair, neutral confident expression, neck, shoulders, torso silhouette, lapels, tie, jacket seams, pinstripe layout, crop, camera, scale, and anchor visually identical in all four cells.
Authored action, reading order: cell 1 both forearms relaxed low with hands just clear of jacket front; cell 2 both hands moving inward toward the single centre jacket button; cell 3 both hands meet coherently and pinch/fasten that one centre button; cell 4 button is set and both hands release slightly outward/down as a clean reset-ready climax. Reverse playback must clearly unfasten/reset. Only forearms, hands, and the tiny centre-button state may change. Torso, lapels, tie and pinstripe pattern do not change.
Style/medium: match Image 1's polished editorial ink linework and subtle watercolour wash, realistic anatomy, warm painted texture only inside the character.
Composition/framing: exact 2x2 regular grid, four equal square cells, character and hands fully contained in every cell with at least 10% green padding, no crop or overlap into gutters.
Constraints: exactly one person in each cell; exactly two arms and two hands total; five natural fingers per visible hand; hands must connect naturally to wrists and perform one coherent buttoning cycle; no hand crossing confusion; no floating fragments; no extra limbs. Absolutely no body scaling, camera shift, head bob, face redraw, torso wiggle, shoulder drift, lapel drift, tie drift, seam drift, pinstripe drift, button migration, or wardrobe drift. Preserve identity from Image 1. Use #00ff00 nowhere in the character.
Avoid: Image 2 identity, photorealism, 3D, clay, vector-flat style, logos, words, initials, title text, numbers, glyphs, watermark, signature, skyline, jewellery, wristbands, motion lines, sparkles, props, cast shadows, key-colour spill.
```

### Accepted edits and deterministic motion

The metadata records no targeted edit prompt. Donor panel `2` is the sole immutable source for the face, torso, pinstripe suit, lapels, tie, hands, and arms. Registration is `[0, 0]` and scale is `0.78` in every phase. Only the two locked hand rigs move horizontally around the same centre button: left `[-16, -8, 0, 3]` pixels and right `[16, 8, 0, -3]` pixels. The recorded static face/torso hash is identical in all phases and changed pixels outside the rigs equal zero.

### SHA-256 locks

| Artifact | Persisted path | SHA-256 |
|---|---|---|
| Prompt | `assets/homie-loaders/qa/strict-repairs/serhanting-manager/candidates/imagegen-prompt.txt` | `594df38f68a4c6017577ca311092aca866ec1fc97039247e522690a7dd11d447` |
| Accepted chroma | `assets/homie-loaders/qa/strict-repairs/serhanting-manager/candidates/raw-chroma.png` | `664f0f5c836b4495aed3b9cd101f72cce7e44808ad2f3206814db4ee9b153cf4` |
| Accepted raw alpha | `assets/homie-loaders/qa/strict-repairs/serhanting-manager/candidates/raw-alpha.png` | `d6fbf5c872da8d24af9bce8cec1d970e6f4039b37e14548e9a0c91ea7c377a65` |
| Locked plate | `assets/homie-loaders/qa/strict-repairs/serhanting-manager/candidates/locked-plate.png` | `c2187c1d718726da27eb24f44efb09cbb475bff098a73f4de0deee88128e8745` |
| Builder | `assets/homie-loaders/qa/strict-repairs/serhanting-manager/candidates/build_serhanting_manager.py` | `68339dadb7a170ef2ad135723b6661d836ba7614e5936db92baa6716087ec002` |
| Source strip | `assets/homie-loaders/qa/strict-repairs/serhanting-manager/candidates/serhanting-manager.png` | `1ae6833056cc64ebf1025a07ff86144373070d5c12bb23c9ebf7b5ea2b786fe3` |
| Preview GIF | `assets/homie-loaders/qa/strict-repairs/serhanting-manager/candidates/serhanting-manager.gif` | `ec406f690b731c8388d3a60783791948069ce85442b83f5d04cc890b9d74ee3f` |
