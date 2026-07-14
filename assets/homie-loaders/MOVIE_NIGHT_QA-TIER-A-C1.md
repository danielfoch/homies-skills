# Homies strict QA report

> Structural metrics and continuity proxies are evidence, not a substitute for the mandatory cell-by-cell visual gate.

| Asset | Result | Min margin | Silhouette p95 | Mask XOR | Registered residual | Visual gate |
|---|---|---:|---:|---:|---:|---|
| `austin-powersing-content` | PASS | 60px | 117.532px | 57.0088% | 83.0646% | recorded: pass |
| `barbie-ing-listings` | PASS | 60px | 55.154px | 55.7593% | 72.4067% | recorded: pass |
| `dirty-dancing-listings` | PASS | 60px | 88.955px | 62.8835% | 82.3991% | recorded: pass |
| `elf-ing-cma` | PASS | 60px | 101.045px | 67.5309% | 93.2417% | recorded: pass |
| `et-ing-research` | PASS | 60px | 6.0px | 2.0638% | 37.8692% | recorded: pass |
| `groundhog-daying-content` | PASS | 60px | 32.0px | 54.136% | 72.4822% | recorded: pass |
| `home-alone-ing-crm` | PASS | 60px | 26.077px | 17.4168% | 43.1373% | recorded: pass |
| `karate-kidding-offers` | PASS | 60px | 98.478px | 64.8484% | 87.4485% | recorded: pass |
| `ken-ing-marketing` | PASS | 60px | 43.966px | 28.6071% | 55.738% | recorded: pass |
| `mission-impossible-ing-manager` | PASS | 60px | 168.0px | 85.3607% | 91.2427% | recorded: pass |
| `mr-beaning-research` | PASS | 60px | 32.388px | 44.8193% | 67.941% | recorded: pass |
| `willy-wonka-ing-offers` | PASS | 60px | 100.896px | 43.6971% | 75.9403% | recorded: pass |
| `zoolandering-reports` | PASS | 60px | 41.0px | 59.7381% | 76.4733% | recorded: pass |

## austin-powersing-content — PASS

Concept: Blue-suited 1960s spy-comedy homage performing a connected finger-gun flourish

Required action: The attached hand must travel from open reset to a full lateral finger-gun extension and return; the gesture must read at 128px.

Full-size contact: `/tmp/movie-tier-a-c1/strict/contacts/austin-powersing-content-source-full.png`

128px contact: `/tmp/movie-tier-a-c1/strict/contacts/austin-powersing-content-source-128.png`

GIF contact: `/tmp/movie-tier-a-c1/strict/contacts/austin-powersing-content-gif-128.png`

Failures: none

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Full-size and 128px review passed. The blue suit, head, glasses and legs remain coherent while one attached arm opens into a strong side finger-gun and returns; no loose fragments or crop.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 60px | 55355px | 1 (1/0) | none |
| 1 | 60px | 55985px | 1 (1/0) | none |
| 2 | 60px | 58091px | 1 (1/0) | none |
| 3 | 60px | 51905px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 35.1617% | 117.532px | 22.496px | 8.062px | 80.1921% | 0.4111 |
| 1→2 | 49.6488% | 26.926px | 23.691px | 29.017px | 71.9732% | 0.7203 |
| 2→3 | 57.0088% | 85.329px | 18.842px | 29.428px | 83.0646% | 0.1791 |

## barbie-ing-listings — PASS

Concept: Bright-pink fashion-doll homage alternating polished sunglasses poses

Required action: The same pink-suited character must move through a sunglasses touch, hair/pose flourish, lateral point, and composed reset.

Full-size contact: `/tmp/movie-tier-a-c1/strict/contacts/barbie-ing-listings-source-full.png`

128px contact: `/tmp/movie-tier-a-c1/strict/contacts/barbie-ing-listings-source-128.png`

GIF contact: `/tmp/movie-tier-a-c1/strict/contacts/barbie-ing-listings-gif-128.png`

Failures: none

Warnings: `BBOX_SCALE_OR_PROP_JUMP`, `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Full-size and 128px review passed after removing the tiny panel-edge debris. The bright-pink outfit and heart shades remain continuous through a hair/pose flourish, point and reset; exactly two attached arms.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 60px | 47993px | 1 (1/0) | none |
| 1 | 60px | 45155px | 1 (1/0) | none |
| 2 | 60px | 53519px | 1 (1/0) | none |
| 3 | 60px | 45834px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 22.0635% | 13.0px | 1.315px | 3.162px | 67.5033% | 0.2736 |
| 1→2 | 52.4391% | 51.144px | 17.535px | 25.495px | 71.2778% | 0.5105 |
| 2→3 | 55.7593% | 55.154px | 24.96px | 25.318px | 72.4067% | 0.1768 |

## dirty-dancing-listings — PASS

Concept: Soft 1980s dancewear homage moving through a romantic sway

Required action: The connected body must shift through open-arm, side-sway, upward reach, and returning poses with clear dance motion at 128px.

Full-size contact: `/tmp/movie-tier-a-c1/strict/contacts/dirty-dancing-listings-source-full.png`

128px contact: `/tmp/movie-tier-a-c1/strict/contacts/dirty-dancing-listings-source-128.png`

GIF contact: `/tmp/movie-tier-a-c1/strict/contacts/dirty-dancing-listings-gif-128.png`

Failures: none

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Full-size and 128px review passed. The character moves through four readable dance beats with coherent anatomy and clean feet; the reversible playback makes a natural sway without background movement.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 60px | 51216px | 1 (1/0) | none |
| 1 | 60px | 45734px | 1 (1/0) | none |
| 2 | 60px | 44623px | 1 (1/0) | none |
| 3 | 60px | 42786px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 61.3772% | 88.955px | 25.237px | 11.402px | 79.2079% | 0.2169 |
| 1→2 | 57.1295% | 88.411px | 19.36px | 47.074px | 82.3991% | 0.0874 |
| 2→3 | 62.8835% | 72.998px | 9.688px | 28.018px | 81.4477% | 0.1606 |

## elf-ing-cma — PASS

Concept: Green-and-yellow holiday elf homage doing an excited bounce and wave

Required action: The character must visibly crouch, spring airborne, and land while one attached hand waves; vertical motion must read at 128px.

Full-size contact: `/tmp/movie-tier-a-c1/strict/contacts/elf-ing-cma-source-full.png`

128px contact: `/tmp/movie-tier-a-c1/strict/contacts/elf-ing-cma-source-128.png`

GIF contact: `/tmp/movie-tier-a-c1/strict/contacts/elf-ing-cma-gif-128.png`

Failures: none

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Full-size and 128px review passed. Crouch, airborne peak and landing are unmistakable, with the same green/yellow costume and one attached waving hand; no clipped hat or shoes.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 60px | 52312px | 1 (1/0) | none |
| 1 | 60px | 42986px | 1 (1/0) | none |
| 2 | 60px | 42389px | 1 (1/0) | none |
| 3 | 81px | 41270px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 60.6836% | 100.0px | 87.676px | 116.52px | 93.2417% | 0.0994 |
| 1→2 | 67.5309% | 101.045px | 118.53px | 102.02px | 88.3855% | -0.0308 |
| 2→3 | 57.8799% | 55.036px | 65.139px | 57.974px | 80.7615% | 0.0619 |

## et-ing-research — PASS

Concept: Wrinkled brown gentle alien homage extending one glowing fingertip

Required action: A single attached index fingertip must progress from off to faint to bright to strongest golden glow while the rounded low-eyed alien hood and body stay registered.

Full-size contact: `/tmp/movie-tier-a-c1/strict/contacts/et-ing-research-source-full.png`

128px contact: `/tmp/movie-tier-a-c1/strict/contacts/et-ing-research-source-128.png`

GIF contact: `/tmp/movie-tier-a-c1/strict/contacts/et-ing-research-gif-128.png`

Failures: none

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Replacement reviewed at full size and 128px. Rounded wrinkled hood, huge low side-set eyes and long neck folds read as the intended gentle alien; there are no antennae, stalks, ears or horns. One attached fingertip glow progresses off/faint/bright/strongest with fixed body registration.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 60px | 67439px | 1 (1/0) | none |
| 1 | 60px | 67404px | 1 (1/0) | none |
| 2 | 60px | 67513px | 1 (1/0) | none |
| 3 | 60px | 68006px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 1.1722% | 1.0px | 0.487px | 0.0px | 36.1963% | 0.9136 |
| 1→2 | 1.4992% | 2.0px | 0.317px | 1.0px | 37.8692% | 0.8742 |
| 2→3 | 2.0638% | 6.0px | 1.879px | 1.0px | 36.9631% | 0.9167 |

## groundhog-daying-content — PASS

Concept: Winter-coated time-loop homage checking a watch and sighing

Required action: The attached arm must rise for a clear watch check, the body must slump into an unmistakable sigh, then begin resetting.

Full-size contact: `/tmp/movie-tier-a-c1/strict/contacts/groundhog-daying-content-source-full.png`

128px contact: `/tmp/movie-tier-a-c1/strict/contacts/groundhog-daying-content-source-128.png`

GIF contact: `/tmp/movie-tier-a-c1/strict/contacts/groundhog-daying-content-gif-128.png`

Failures: none

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Full-size and 128px review passed. The winter coat and scarf stay coherent while the wrist rises for a clear watch check and the body slumps into a visible sigh; no prop morph or crop.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 60px | 52289px | 1 (1/0) | none |
| 1 | 60px | 51316px | 1 (1/0) | none |
| 2 | 60px | 50647px | 1 (1/0) | none |
| 3 | 60px | 50905px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 42.1113% | 24.0px | 16.758px | 23.022px | 61.8294% | 0.2084 |
| 1→2 | 48.3844% | 29.017px | 23.347px | 29.682px | 72.4822% | -0.0843 |
| 2→3 | 54.136% | 32.0px | 25.764px | 30.806px | 68.5158% | -0.0522 |

## home-alone-ing-crm — PASS

Concept: Red-sweater holiday-comedy homage making the hands-to-cheeks gasp

Required action: Exactly two attached hands must travel from the sides to both cheeks, then separate toward reset; the gasp must read at 128px.

Full-size contact: `/tmp/movie-tier-a-c1/strict/contacts/home-alone-ing-crm-source-full.png`

128px contact: `/tmp/movie-tier-a-c1/strict/contacts/home-alone-ing-crm-source-128.png`

GIF contact: `/tmp/movie-tier-a-c1/strict/contacts/home-alone-ing-crm-gif-128.png`

Failures: none

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Full-size and 128px review passed. Exactly two connected hands move from the sides to both cheeks for the gasp and then separate; sweater, head and legs remain stable and uncropped.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 60px | 53269px | 1 (1/0) | none |
| 1 | 60px | 46604px | 1 (1/0) | none |
| 2 | 60px | 48667px | 1 (1/0) | none |
| 3 | 60px | 50618px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 17.4168% | 26.077px | 2.623px | 1.414px | 43.1373% | 0.691 |
| 1→2 | 15.1872% | 21.213px | 5.999px | 3.0px | 36.8326% | 0.6382 |
| 2→3 | 15.6336% | 20.0px | 3.619px | 3.0px | 32.4397% | 0.7368 |

## karate-kidding-offers — PASS

Concept: White-gi martial-arts homage moving into a crane-kick balance

Required action: The connected body must progress from ready stance through one raised knee to a fully extended crane kick and controlled return.

Full-size contact: `/tmp/movie-tier-a-c1/strict/contacts/karate-kidding-offers-source-full.png`

128px contact: `/tmp/movie-tier-a-c1/strict/contacts/karate-kidding-offers-source-128.png`

GIF contact: `/tmp/movie-tier-a-c1/strict/contacts/karate-kidding-offers-gif-128.png`

Failures: none

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Full-size and 128px review passed. The white gi and belt remain coherent as one knee rises into a clear extended crane kick and returns; limbs remain attached and all feet/hands are fully framed.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 60px | 55316px | 1 (1/0) | none |
| 1 | 61px | 46814px | 1 (1/0) | none |
| 2 | 60px | 53827px | 2 (1/1) | none |
| 3 | 60px | 48264px | 2 (1/1) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 64.8484% | 98.478px | 46.299px | 53.141px | 87.4485% | 0.286 |
| 1→2 | 54.403% | 66.287px | 18.612px | 34.015px | 79.18% | 0.2957 |
| 2→3 | 43.7518% | 83.527px | 10.948px | 2.0px | 73.8586% | 0.3016 |

## ken-ing-marketing — PASS

Concept: Pastel beach-fashion homage pointing both thumbs toward himself

Required action: Both attached hands must rise into a clear double-thumbs-to-self pose, peak confidently, and reset.

Full-size contact: `/tmp/movie-tier-a-c1/strict/contacts/ken-ing-marketing-source-full.png`

128px contact: `/tmp/movie-tier-a-c1/strict/contacts/ken-ing-marketing-source-128.png`

GIF contact: `/tmp/movie-tier-a-c1/strict/contacts/ken-ing-marketing-gif-128.png`

Failures: none

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Full-size and 128px review passed. Both connected hands rise into a strong double-thumbs-to-self peak and return; pastel shirt, shorts, face and feet stay registered.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 60px | 54772px | 1 (1/0) | none |
| 1 | 60px | 53634px | 1 (1/0) | none |
| 2 | 60px | 57304px | 1 (1/0) | none |
| 3 | 60px | 54064px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 28.6071% | 43.966px | 11.067px | 4.0px | 55.738% | 0.9222 |
| 1→2 | 16.8131% | 30.799px | 9.386px | 4.123px | 51.1418% | 0.8176 |
| 2→3 | 27.5477% | 41.725px | 12.671px | 5.099px | 55.4412% | 0.8739 |

## mission-impossible-ing-manager — PASS

Concept: Black tactical spy homage swinging while suspended on one rope

Required action: One continuous rope must stay attached while the full body swings through diagonal, horizontal, opposite diagonal, and returning poses.

Full-size contact: `/tmp/movie-tier-a-c1/strict/contacts/mission-impossible-ing-manager-source-full.png`

128px contact: `/tmp/movie-tier-a-c1/strict/contacts/mission-impossible-ing-manager-source-128.png`

GIF contact: `/tmp/movie-tier-a-c1/strict/contacts/mission-impossible-ing-manager-gif-128.png`

Failures: none

Warnings: `BBOX_SCALE_OR_PROP_JUMP`, `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Full-size and 128px review passed. One uninterrupted rope and harness carry the same black-clad character through four large suspended swing angles; no duplicated rope, hands, feet or crop, and the loop reverses naturally.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 60px | 40554px | 1 (1/0) | none |
| 1 | 60px | 35886px | 1 (1/0) | none |
| 2 | 60px | 38923px | 1 (1/0) | none |
| 3 | 60px | 39935px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 80.4523% | 168.0px | 4.339px | 70.342px | 89.8262% | 0.3361 |
| 1→2 | 85.3607% | 116.417px | 6.152px | 95.859px | 91.2427% | -0.0192 |
| 2→3 | 80.0091% | 155.563px | 8.681px | 95.525px | 89.883% | 0.1968 |

## mr-beaning-research — PASS

Concept: Tweed-jacket physical-comedy homage cycling through suspicious awkward reactions

Required action: The character must visibly shift from hands-on-hips suspicion through a droop and raised-shoulder awkward reaction before resetting.

Full-size contact: `/tmp/movie-tier-a-c1/strict/contacts/mr-beaning-research-source-full.png`

128px contact: `/tmp/movie-tier-a-c1/strict/contacts/mr-beaning-research-source-128.png`

GIF contact: `/tmp/movie-tier-a-c1/strict/contacts/mr-beaning-research-gif-128.png`

Failures: none

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Full-size and 128px review passed. Tweed jacket, red tie and face remain recognizable through suspicious stance, droop and raised-shoulder awkward reaction; anatomy and shoes are clean.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 60px | 46386px | 1 (1/0) | none |
| 1 | 60px | 46132px | 1 (1/0) | none |
| 2 | 60px | 49990px | 1 (1/0) | none |
| 3 | 60px | 46441px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 30.0551% | 25.0px | 8.024px | 8.0px | 67.941% | -0.0077 |
| 1→2 | 44.8193% | 32.388px | 30.657px | 29.682px | 63.0335% | 0.1263 |
| 2→3 | 39.3887% | 27.295px | 24.94px | 38.639px | 63.5909% | 0.3404 |

## willy-wonka-ing-offers — PASS

Concept: Purple-coated confectioner homage tipping a top hat and bowing theatrically

Required action: The same top hat must move from the head to an attached hand as the character bows and opens the free arm, then resets.

Full-size contact: `/tmp/movie-tier-a-c1/strict/contacts/willy-wonka-ing-offers-source-full.png`

128px contact: `/tmp/movie-tier-a-c1/strict/contacts/willy-wonka-ing-offers-source-128.png`

GIF contact: `/tmp/movie-tier-a-c1/strict/contacts/willy-wonka-ing-offers-gif-128.png`

Failures: none

Warnings: `BBOX_SCALE_OR_PROP_JUMP`, `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Full-size and 128px review passed. The same purple hat moves coherently from head to connected hand during the bow, with one free arm opening theatrically; no duplicate hat or clipped coat.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 60px | 47979px | 1 (1/0) | none |
| 1 | 60px | 45933px | 1 (1/0) | none |
| 2 | 61px | 47423px | 1 (1/0) | none |
| 3 | 60px | 45857px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 38.7805% | 77.964px | 29.563px | 2.0px | 66.1708% | -0.0676 |
| 1→2 | 30.2433% | 100.896px | 5.302px | 1.0px | 61.4956% | 0.162 |
| 2→3 | 43.6971% | 99.202px | 15.319px | 33.061px | 75.9403% | 0.1903 |

## zoolandering-reports — PASS

Concept: Black-runway-fashion homage alternating dramatic model poses

Required action: The same black-suited character must alternate four visibly different runway face/body poses while remaining fully framed.

Full-size contact: `/tmp/movie-tier-a-c1/strict/contacts/zoolandering-reports-source-full.png`

128px contact: `/tmp/movie-tier-a-c1/strict/contacts/zoolandering-reports-source-128.png`

GIF contact: `/tmp/movie-tier-a-c1/strict/contacts/zoolandering-reports-gif-128.png`

Failures: none

Warnings: `STATIONARY_REGIONS_NOT_ANNOTATED`

Manual notes: Full-size and 128px review passed. Four distinct runway poses read clearly while the black suit and character remain consistent; all limbs and hair stay clean inside frame.

| Cell | Margin | Foreground | Components (significant/tiny) | Artifact flags |
|---:|---:|---:|---:|---|
| 0 | 60px | 50467px | 1 (1/0) | none |
| 1 | 60px | 48614px | 1 (1/0) | none |
| 2 | 60px | 48739px | 1 (1/0) | none |
| 3 | 60px | 51501px | 1 (1/0) | none |

| Transition | Mask XOR | Silhouette p95 | Centroid | Registration shift | Residual | Upper NCC |
|---:|---:|---:|---:|---:|---:|---:|
| 0→1 | 59.7381% | 41.0px | 22.855px | 49.82px | 76.4733% | 0.1363 |
| 1→2 | 37.0252% | 30.364px | 10.341px | 5.099px | 66.6718% | 0.0467 |
| 2→3 | 28.8251% | 17.088px | 11.295px | 8.0px | 65.8975% | 0.1764 |

