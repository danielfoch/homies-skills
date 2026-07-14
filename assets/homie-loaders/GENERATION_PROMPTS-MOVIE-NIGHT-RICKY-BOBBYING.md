# Generation prompts — Ricky-Bobbying

Date: 2026-07-14  
Loader: `ricky-bobbying-manager`  
Collection: Movie Night  
Image workflow: built-in image-generation tool, local chroma-key removal, then deterministic locked-plate animation.

## Reference roles

- User reference `codex-clipboard-625bacb5-35a5-4ecc-a0c7-0149690e9127.png`: trophy scale, racing wardrobe and celebratory pose only.
- `references/manager.png`: exact canonical male Manager identity, face, proportions and Homies ink/watercolour style.

## Accepted generation prompt

> Use case: stylized-concept. Asset type: locked character plate for a 128px transparent chat-interface loading GIF. Create one canonical male Manager Homie enthusiastically hoisting one oversized silver racing trophy high beside and slightly above his head. Preserve the exact Manager face and swept brown hair. Dress him in a professional cream-white stock-car racing suit with cobalt-blue sleeves, coral-red piping, small navy/coral/gold circular accents, matching racing shoes and a white-and-blue racing cap. Replace every Wonder Bread or real sponsor reference with a simple invented Homies house-shaped H crest. No real brands, sponsor names, numbers, flags, actor likeness, movie title or other readable text. Exactly one adult male Homie, two natural connected arms, two five-finger hands supporting the trophy, and one trophy. Use an energetic thigh-up victory pose with the trophy fully inside the canvas and generous padding. Match the exact hand-drawn editorial black-ink outline, restrained watercolour fill and pencil texture of the Manager reference; no clay, 3D, vector-flat, photorealistic or new mascot style. Use one perfectly flat solid `#00ff00` chroma-key field with no shadow, gradient, floor, crowd, race car, podium, confetti, scenery, watermark, extra limbs, people or floating fragments.

## Accepted locked plates

| Artifact | SHA-256 |
|---|---|
| Generated chroma plate | `112c47647f29a81192b796d3739e769f447adfe36b43b352e9180694c2f1336e` |
| Transparent canonical plate | `17046de6956f55ecd746537b041e96f3b5331801f3a7d7201509f9e1d7c2ccc9` |

The chroma plate was processed with border auto-keying, a soft matte,
thresholds `12/220`, and despill. The four animation cells are not independently
generated: the accepted Manager, suit, hands and trophy remain pixel-locked,
while a deterministic glint moves across the trophy cup. A fixed checkered rail
conceals the intentional thigh-up illustration boundary in every frame.
