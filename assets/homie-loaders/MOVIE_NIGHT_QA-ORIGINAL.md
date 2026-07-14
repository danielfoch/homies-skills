# Original Movie Night 12 — independent QA

Result: **PASS — all 12 corrected source masters and all 12 assembled transparent GIFs pass.**

This was an independent cross-audit of the current source files using `/tmp/movie12-alignment.json`. Each source was inspected as a four-frame strip at both 128 px chat scale and the original 627 px cell scale. GIFs were assembled at 256 px with the production `scripts/assemble_sprite.py` path and then checked numerically and visually.

## One blocker found and corrected

The first audit found a concrete blocker in `mavericking-manager`: frames 1 and 3 had a hard rectangular transparent notch beneath the raised viewer-left sleeve, with a smaller hard edge in frame 2. The defect was visible in both the 128 px strip and original-scale alpha frames.

The final repair is deterministic and contains no generative redraw:

- frame 0's complete full-character plate is now copied pixel-identically into all four cells;
- the raised sleeve, hand, head, hair, jacket, torso, legs, shoes, baseline, scale, and camera therefore remain literal canonical pixels;
- only the single sunglasses assembly moves through four tiny distinct diagonal offsets: `(0,0)`, `(-1,+1)`, `(-2,+2)`, `(-3,+3)` source pixels;
- the original glasses area is nearest-filled beneath the moving assembly, so no doubled glasses or ghost frame remains;
- the hand stays touching the temple and the action still reads as adjusting the aviators.

The repaired source is `assets/homie-loaders/sources/wildcard/mavericking-manager.png`. The pre-fix source is retained only as the temporary audit artifact `/tmp/movie12-independent/mavericking-manager-before-fix.png`. The rebuilt source and GIF now pass at both inspection scales; the underarm edge is continuous and the rectangular notch is gone.

No other source required modification.

## Visual continuity audit

- `lloyd-doblering-manager`: one stable body/coat/lower-body plate; rigid boombox/raised-arm micro-motion; no crop or camera wobble.
- `ferris-buellering-marketing`: chair, pelvis, legs, shoes, hands, and face remain registered; contained shoulder/upper-body bounce only.
- `harry-pottering-research`: corrected cuff area passes. The wand-side arm is connected in every frame with no detached sleeve/cuff shard, extra hand, floating fragment, or crop.
- `bilbo-bagginsing-crm`: body, cape, feet, hand, and one ring remain fixed; only the small ring glint changes.
- `neo-ing-offers`: feet and baseline stay fixed; controlled lean has no global translation, coat discontinuity, or camera change.
- `indy-jonesing-reports`: body, satchel, legs, and feet are registered; one hat/hand tip reads cleanly with no duplicate hat.
- `jack-sparrowing-marketing`: one continuous character and costume with no weapon or extra anatomy; restrained sway does not move the camera.
- `rocky-balboa-ing-cma`: exactly two attached hands and two persistent red gloves in every frame; canonical lower body; alternating fist motion remains continuous.
- `mavericking-manager`: after the deterministic repair, one canonical full-character plate is fixed and only one sunglasses assembly moves. No underarm notch, doubled sleeve, floating pixels, or body wobble remains.
- `bond-ing-offers`: canonical head, torso, tuxedo, legs, and feet; cuff/forearm motion stays attached; exactly two hands and no weapon.
- `sherlocking-research`: one persistent magnifier and connected hand; lower body, coat, hat, and camera remain fixed; no pipe or extra prop.
- `gandalfing-reports`: one persistent staff with fixed floor contact; robe, hat, beard, feet, and camera remain registered; no crop or floating hem fragment.

The 128 px scan sheet is `/tmp/movie12-independent/movie12-all-128.png`. Per-loader 128 px strips are under `/tmp/movie12-independent/strips128/`; original-scale strips are under `/tmp/movie12-independent/strips-original/`; extracted RGBA cells are under `/tmp/movie12-independent/frames/`.

## Source contract

All 12 sources pass:

- exact `1254 × 1254` RGB geometry;
- four exact `627 × 627` authored cells;
- exact RGB `(0,255,0)` along the full outer border and both two-pixel center axes (`x=626/627`, `y=626/627`);
- four distinct authored source cells;
- minimum non-key clearance of at least 52 px across the batch;
- no crop, panel border, readable text, logo, watermark, extra character, or floating anatomy.

## GIF contract

All 12 temporary GIFs under `/tmp/movie12-independent/gifs/` pass:

- exact `256 × 256` size;
- exactly six frames in sequence `0,1,2,3,2,1`;
- all first four authored GIF frames remain distinct after 96-color quantization;
- exact durations `210,140,140,210,140,140` ms;
- infinite loop (`loop=0`);
- disposal method 2 on every frame;
- fully transparent four corners on every frame;
- frame 4 hash equals authored frame 2 and frame 5 hash equals authored frame 1, proving the reverse half is exact.

## Final hashes and margins

| Loader | Min. margin | Source SHA-256 | Temporary GIF SHA-256 |
|---|---:|---|---|
| `lloyd-doblering-manager` | 52 px | `7632a5a9deae7d5df365f57a99cd7936732f1c60219ee4cea4875f0302ac0484` | `bd4e3cd78e36e0a75fe63ee9c019ee2caed020361db8f00b7639da5c1cc78c39` |
| `ferris-buellering-marketing` | 63 px | `87841d9be6540633cc518198706986c03d86fa181069faa5b6a45939d55b31d6` | `c665e70948a8f792780d5541507a5713294a7e6b938e7ca83b1e2efb8c70bf6d` |
| `harry-pottering-research` | 54 px | `a193ab93611a3e8f5ed7fe5d4c4d81bd43e45d19f60796265283507e49bd5f6c` | `dc215ebdf024ff43f0c88168249120ee655fb2b54fb751aab8c7ad01a9727f9f` |
| `bilbo-bagginsing-crm` | 52 px | `c5f8b8d54890b7fd6f583fe7be72a7895f7d20191ef2c9640fba7c58d8f8120c` | `ed79c3c5d69a269d6812ace30347bb7d753e810b641763271bae6a7ef371fd78` |
| `neo-ing-offers` | 58 px | `9fdf618148e68e9d22e94aa58d0372f10c6aa895f0cde60363f3742e139d9626` | `412af8fd8aca18008fbc54c179975d83ccb27fac5e96974c018b419735fce112` |
| `indy-jonesing-reports` | 52 px | `3de66172bd711a2e39c7044e5901106ce7acf4b9edb1d8392b8dcbada044a615` | `6fe2532dcd90c072db3ad6e8f91eb22737a4bfc470b2ab31c15e88af19faff49` |
| `jack-sparrowing-marketing` | 60 px | `7074a3b166ea031509331ac3ecae9514aa788e4934e01229f08169a60ac3b620` | `8a112170824942ba1e68edf0e20ac9b64873b948b15b1c97cd2c454f493d6be6` |
| `rocky-balboa-ing-cma` | 53 px | `c12bb7902826b21b1e8cae862005283732fae79c86ceec970476a25b932a9692` | `a2def4aea181b0c57c5cc83f3e36aa5c37a23a4f37bd50f628422866acb892cd` |
| `mavericking-manager` | 70 px | `f9cb455b2a98521d9ba52168407e11be3c309c17b3a9fde59fefd8ce22c97f2d` | `28ca984523987208b5c6b1739a787378da0318d2035c457e5f5415645d5d10b3` |
| `bond-ing-offers` | 54 px | `9e6547727c28ba838fa22f17330727e57727fe25bea8db46ee50df820d1672ec` | `5be14f4fb274885ee466921a44ceefc4078f56f6f3175b4ab24d6c86c8a037f1` |
| `sherlocking-research` | 56 px | `a0744aaddb105245297ea531e917b3df72dbcf87137c7ee96b8a00b072878e4d` | `8e44c1962f9ac15c7e02f81707f0913bf92e0ad40083082435f8e7bde418db6d` |
| `gandalfing-reports` | 66 px | `510cab476de76723539e6698624f7507d63d3eaa147e204957928d4ed59b3ac9` | `2bfa6af0f82b89be8bd288d78732dd150ef9e22345d8de4143c100474679768f` |

Machine-readable audit details are saved at `/tmp/movie12-independent/audit.json`.
