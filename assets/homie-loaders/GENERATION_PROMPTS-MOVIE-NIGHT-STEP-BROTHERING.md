# Generation prompts — Step-Brothering

Date: 2026-07-14  
Loader: `step-brothering-manager-crm`  
Collection: Movie Night  
Image workflow: built-in image-generation tool, followed by local chroma-key removal and deterministic frame assembly.

## Reference roles

- User reference: `codex-clipboard-94fec5a1-a71b-44a2-a002-b0f9ac9804c7.png` — pose and wardrobe only.
- `references/manager.png` — canonical taller rear male Manager Homie identity and ink/watercolour style.
- `references/crm.png` — canonical shorter front male CRM Homie identity and ink/watercolour style.
- The first generated plate was used only as an edit target for the accepted correction.

## Initial generation prompt

> Create exactly two adult male Homies dressed and posed like the supplied awkward Step Brothers studio portrait. Use the canonical Manager Homie as the taller rear-left figure and the canonical CRM Homie as the shorter front-right figure. Both face the camera in pale blue button-down shirts and complementary dark-green/brown and burgundy/grey argyle sweater vests. Match the Homies references exactly: clean black ink outlines, light warm watercolour fills, restrained texture, and polished editorial character illustration. Manager reaches forward to rest a natural hand on CRM's left shoulder. Keep both distinct canonical faces. Center the pair as one compact silhouette with generous padding. Use a perfectly flat solid `#00ff00` chroma-key field with no gradient, texture, floor, shadow, reflection, text, logo, watermark, extra people, extra limbs, actor likenesses, green clothing, or cropped heads.

The first plate established the correct identities, wardrobe, and composition, but its pose had only one shoulder hand and its bodies ended at the canvas edge. It was retained for audit only and not shipped.

## Accepted correction prompt

> Refine only the first generated plate. Preserve the two canonical Homie identities, faces, expressions, skin tones, hair, argyle patterns, blue shirts, watercolour-and-ink style, relative sizes, and rear-left/front-right arrangement. Match the supplied portrait's key pose detail: the taller rear Manager places BOTH of his natural hands together in a slightly awkward overlapping stack on the shorter front CRM Homie's left shoulder. Both complete connected forearms must lead naturally from Manager's two sleeves to two distinct five-finger hands. Zoom the whole pair out about 15 percent and extend the artwork downward so both full figures end naturally with green padding on every side. Keep exactly two adult male Homies and exactly two stacked Manager hands; no other visible hands, extra arms, fused anatomy, detached fingers, changed faces, actor likenesses, props, text, logo, watermark, shadows, or background scenery. The field must remain perfectly flat solid `#00ff00` and the subjects must contain no green clothing or accessories.

## Accepted locked plates

| Artifact | SHA-256 |
|---|---|
| Corrected generated chroma plate | `46eaf66ec9f8f96f6b01defea451ecd8d748e35b9783106b8c29e1287e723340` |
| Corrected transparent canonical plate | `ad76fae1104bb1fcdf107762a6a09dc86dd55b9b950e5145b7e1b00de44f60e4` |

The chroma plate was converted with the installed image-generation helper using border auto-keying, soft matte, thresholds `12/220`, and despill. The four authored animation cells are not independently generated: the accepted transparent plate remains pixel-locked while a deterministic camera-flash effect changes behind it.
