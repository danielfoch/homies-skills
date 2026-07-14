# Tier-A Movie Night S1 — generation prompt ledger

Built-in image generation was used one successful call per accepted raw asset. All accepted raws were generated as 1254×1254 RGB 2×2 sheets, copied to `raw/`, chroma-extracted to `alpha/`, then deterministically registered, recoloured, canonicalized, and placed on exact `#00ff00` cells by `build_s1.py`.

Reference research used image searches for: `Yoda Force hand lift robe pose`; `Darth Vader Force choke hand pose cape`; `Terminator black leather sunglasses red eye pose`; and `Batman cape spread scalloped silhouette`. Research was used only to isolate recognizable silhouette/action cues: low-to-high open hand and rising pebble; connected gripping-hand rise against a fixed cape; leather/shades plus one pulsing red lens and head turn; and a narrow-to-wide scalloped cape silhouette.

## yoda-ing-cma

Accepted built-in raw: `/Users/danielfoch/.codex/generated_images/019f5927-f7c1-7153-81df-ee875bc58556/exec-bb575498-6822-4981-9ef9-68df65e4588a.png`

Exact accepted prompt:

```text
Create a square 2x2 animation sprite sheet with four equal cells, in a polished hand-inked watercolor editorial illustration style. Show one original short purple woodland elf with broad pointed ears, a friendly elderly face, a navy wrap robe and cream tunic. Same exact character identity, proportions and scale in all four cells.

Animate a clear hand-and-stone lift: cell 1 open hand at waist with one small stone near knee; cell 2 hand at chest with stone at chest; cell 3 hand beside cheek with stone above shoulder; cell 4 hand at eye level with stone one full head above it. The moving arm and stone travel a large obvious distance. Head, ears, face, robe, other arm, torso and feet stay fixed. Exactly one character, two arms, two hands and one stone per cell.

Perfectly flat solid #00ff00 background across all edges and both centre axes. No borders, floor, shadow, gradient, texture, glow, scenery, text, logo, symbol, watermark, blur, extra parts or crop. At least 12% green padding in every cell. No #00ff00 inside the subject.
```

Deterministic finishing: the purple skin was recoloured moss green, white hair was neutralized, navy robe was recoloured brown/tan, the canonical cell-0 fixed body was retained outside the moving-arm windows, and the one generated stone was preserved at each authored height.

## darth-vadering-offers

Accepted built-in raw: `/Users/danielfoch/.codex/generated_images/019f5927-f7c1-7153-81df-ee875bc58556/exec-6cc927ce-b54f-4535-8437-ab16acbda2c8.png`

Exact accepted prompt:

```text
Create a square 2x2 animation sprite sheet in a polished hand-inked watercolor editorial illustration style. Show one original ceremonial robot guard wearing ivory angular helmet and armour, a long teal cape, ivory gloves and boots, plus a small abstract chest panel of plain coloured squares with no writing.

Use four equal reading-order cells with no visible divider. Reuse the same exact guard, helmet, armour, cape, torso and stance. Show one large connected hand-raising gesture: cell 1 one gloved hand open beside the hip; cell 2 forearm at the waist; cell 3 forearm at shoulder height with fingers curling; cell 4 that arm clearly extended forward at chest height in a dramatic gripping pose. The working hand moves a large distance readable at 128px. Keep the other arm, helmet, torso, legs, boots and cape fixed. Exactly two arms and two attached hands. No weapon, beam, other character, text, symbol, logo, watermark, extra fingers or extra limb.

Perfectly flat solid #00ff00 backdrop on every outer edge and both centre axes. No floor, shadow, gradient, glow, texture, scenery, border, separator or reflection. No #00ff00 inside the guard. At least 12% green padding around the subject in every cell; no crop or bleed. Treat the fixed body as one canonical drawing rather than four redraws.
```

Deterministic finishing: right-column body anchors were corrected by 26–27 raw pixels to remove global drift; ivory armour and teal cape were recoloured dark charcoal/black while retaining line detail; and an identical logo-free 2×2 coloured-square chest panel was drawn on every cell.

## terminatoring-reports

Accepted built-in raw: `/Users/danielfoch/.codex/generated_images/019f5927-f7c1-7153-81df-ee875bc58556/exec-86078348-6c2b-4a35-b2f5-1299818b14e8.png`

Exact accepted prompt:

```text
Create a square 2x2 animation sprite sheet in a polished hand-inked watercolor editorial illustration style. Show one original female retro-future android biker in a strong mechanical full-body stance, wearing a black leather motorcycle jacket, black trousers, heavy boots and opaque dark wraparound sunglasses. One lens contains a small circular red mechanical glow. No weapon.

Four equal reading-order cells, no visible divider. Reuse the same exact body, jacket, legs, hands and stance. Animate an unmistakable head turn with the neck connected: cell 1 head turned clearly toward viewer-left and red lens dim; cell 2 head centred and red lens medium; cell 3 head turned clearly toward viewer-right and red lens bright; cell 4 head centred again with red lens at its brightest pulse. The head turn must be visually obvious at 128px, not a tiny twitch. Hair, sunglasses and red lens follow the head as one connected rigid head layer. Keep torso, shoulders, arms, hands, jacket, legs and boots fixed. Exactly one head, two arms and two legs in every cell. No exposed gore, weapon, text, lettering, logo, watermark, extra eye, duplicate head or floating glasses.

Perfectly flat uniform solid #00ff00 chroma-key background on every background pixel, including all outer edges and both centre axes. No floor, cast shadow, gradient, glow except the contained red lens, scenery, texture, border, separator or reflection. No #00ff00 inside the subject. At least 12% green padding on all sides of every cell; no crop or bleed. Treat the fixed body as one canonical drawing reused across cells; only rotate the connected head and pulse the one red lens.
```

Deterministic finishing: all four cells use the same cell-1 canonical body below the neck; only the connected head/hair/glasses patch changes. The canonical shoulder/collar layer is restored over each neck seam.

## batmaning-manager

Accepted built-in raw: `/Users/danielfoch/.codex/generated_images/019f5927-f7c1-7153-81df-ee875bc58556/exec-20d2bb81-c725-4753-a2d4-c9cbb419c85e.png`

Exact accepted prompt:

```text
Create a square 2x2 animation sprite sheet in a polished hand-inked watercolor editorial illustration style. Show one original male theatrical illusionist in a simple fitted light-grey stage costume, plain belt, boots, a close fabric hood with the face visible, and one deep red fabric cape. No emblem, lettering, animal mark, text or logo.

Four equal reading-order cells, no visible divider. Reuse the same exact body, face, hood, costume, belt, legs, stance, scale and lighting. Animate a large symmetrical curtain-cape opening:
cell 1 the cape is wrapped around the body as a narrow closed silhouette;
cell 2 the cape is half-open with both elbows spreading;
cell 3 the cape is broadly open on both sides;
cell 4 the cape is fully spread into a very wide symmetrical fan with five large rounded scallops on each lower edge.
Cape width changes dramatically and reads at 128px. Exactly two connected arms and two hands under the cape. Head, torso, belt, legs and boots stay registered. No weapon, text, logo, watermark, extra limb, duplicate cape, detached hand or crop.

Perfectly flat solid #00ff00 background on every background pixel, all outer edges and both centre axes. No floor, shadow, gradient, glow, scenery, texture, border, separator or reflection. No #00ff00 in the subject. At least 10% green padding around even the fully spread cape in every cell; no bleed. Treat the fixed body as one canonical drawing; only articulate the two arms and cape.
```

Deterministic finishing: body anchors were normalized for the wide-cape frames; red cape and grey suit were recoloured to dark navy/charcoal; two connected pointed cowl ears were added consistently; the widest cape was scaled to preserve 66px of clearance.


