# Movie Night QA — Jon Snow Plus Eleven

Date: 2026-07-14 (America/Toronto)

Scope: consolidated root QA record for the twelve current **candidate-only** Homie loaders. This record does not promote or modify production sources, GIFs, manifests, site code, or independent QA records.

## Root gate verdict

**PASS — 12/12 current candidates.**

The gate is stated as 12/12 only because every selected current strict report below records PASS with:

- zero failures;
- zero warnings;
- a complete manual visual gate;
- a directly matching current source-PNG SHA-256 and GIF SHA-256; and
- the standard transparent GIF contract: 256×256, six frames, four unique authored phases, exact reversible phase order `0,1,2,3,2,1`, durations `210,140,140,210,140,140ms`, infinite loop, and exact loop closure.

## Final artifact ledger

| # | Candidate | Final source PNG SHA-256 | Final GIF SHA-256 | Strict min margin | Strict result | Warnings / failures |
|---:|---|---|---|---:|---|---|
| 1 | `jon-snowing-marketing` | `8ae889775a0a659fb27142e8c04e45df21293ad26cf12cfc8f4b5d241f92f966` | `081883e2ec709593c38ed98cb16cd84536173ca24e8964f39031c680cd4d95fb` | 65px | PASS | 0 / 0 |
| 2 | `buffying-offers` | `883c3f2ceb2b749c22e7215b3556a3c9df7a51e9a873788aea99ab677ef26ea8` | `6565844e06abce38749e33523c26c52d03b4f1975c4837860f16356b4560f572` | 71px | PASS | 0 / 0 |
| 3 | `scooby-dooing-manager` | `61dc3d62762f91cd870c2593e87b5d4b93aca1b54c91f46062d807edc183b4be` | `cf5003e386102c932bd60feba93bc9f82df6224ac421fffbed0abd5431187f07` | 72px | PASS | 0 / 0 |
| 4 | `walter-whiting-crm` | `3c30d08ce62138368d0ec71a261b0e573de85c0520acc0a26db47ad680939944` | `d1086c933c49a0e2e9ee1959fd3fcf768b042e97f5637318d27d5d58dd5f959d` | 74px | PASS | 0 / 0 |
| 5 | `gary-veeing-crm` | `72abdf6a37492c47cc93172e311a3ec7c37f23cc7dfaa5298c832f5d796413aa` | `916e302a614de9edd3b7327b4eccb7f085324acc09185221958ae84d8b43ea47` | 83px | PASS | 0 / 0 |
| 6 | `gatsbying-manager` | `a354e8b829adcb45bde98864eeb108f21a97cd3dc953361627a3a1b69098b30b` | `085f3f58c889dcd46acdf963307e7c5310ccc6bb4ac67fa6758ea223e9776f86` | 86px | PASS | 0 / 0 |
| 7 | `ron-burgunding-cma` | `0049af3ccaf578d2713c271b0f956cfe6d6d18b88cc29d2752f42299349f9b2f` | `9747e6408df19ae78d84804fbb7e11b4bc03d4f88a92e27b03612a68243503fd` | 84px | PASS | 0 / 0 |
| 8 | `serhanting-manager` | `1ae6833056cc64ebf1025a07ff86144373070d5c12bb23c9ebf7b5ea2b786fe3` | `ec406f690b731c8388d3a60783791948069ce85442b83f5d04cc890b9d74ee3f` | 76px | PASS | 0 / 0 |
| 9 | `spoking-content` | `36d0c2ab59419c30dacdb4b1705bdfce997a61f989235a7935dcae77e1157833` | `b9b88ac4ee647344eea4a9e811d2a6bda4fbfed3e7223df0bed74995acef3b47` | 86px | PASS | 0 / 0 |
| 10 | `tony-starking-marketing` | `0f7331eb81717dc6920d26fb4b8ec25cefec356980be5777b48cade22dd7aea9` | `5abb05d4b2a993c127f2585b91eea0f8ffdff9bbe7c5bb8ae837b9b4c1c9b17a` | 70px | PASS | 0 / 0 |
| 11 | `tyler-durdening-listings` | `3f04d49bfeca9aa98c3aae199fbb98b8752e7c92b061fba4e451835e6df945b2` | `abfba32629dab614567f5c07444e85c75770f29528e566bd67c7ee7e521a6bf1` | 70px | PASS | 0 / 0 |
| 12 | `robin-hooding-manager` | `45b28eac67576766fcf254d6affb1d2ec5180f29bc235091da73094f2d37c171` | `33d8044924f5f549a8856ad5671871f92fc4dc5932ed98549e899defae50ac13` | 70px | PASS | 0 / 0 |

## Motion rigs, locked regions, and deterministic evidence

### 1. Jon Snowing Marketing

- Intended motion: six authored snowflakes translate through negative space at offsets `(-12,-6)`, `(-4,-2)`, `(4,2)`, `(12,6)` while one small blade-confined glint travels through y positions `330,390,450,510`.
- Locked evidence: the single Marketing Homie, face, fur, cloak, armor, both hands, and uninterrupted sword plate remain immutable outside the snow/glint mask. Strict stationary region `locked-face-fur-torso-and-hands` changed `0.0%` against `0.0%` allowed.
- Determinism: a fresh isolated build under `/private/tmp` reproduced both final hashes byte-for-byte. Builder SHA-256: `6a2990b7d832507ce7c1be4f92d698c0bf70cec682f41bbf464c1a41683c44b3`.

### 2. Buffying Offers

- Intended motion: one complete female Offers-and-stake rig makes a guarded boot-anchored lean around pivot `(313,550)` at angles `2.8°,0.9°,-0.9°,-2.8°`.
- Locked evidence: female identity, anatomy, empty second hand, black outfit, exactly one wooden stake, scale, and internal relative geometry remain one rigid rig; the strict stationary empty-corner proxy changed `0.0%`.
- Determinism: the final builder was rerun from its accepted locked plate and reproduced the source and GIF byte-for-byte; a second fresh isolated root check did the same. Builder SHA-256: `d52c8b6dec8adc741286a9da6a4ff1207a4e97b7b6848bff20bff7506e0c18f1`.

### 3. Scooby-Dooing Manager

- Intended motion: the one connected Manager-and-dog rig receives shared integer translations `(-9,0)`, `(-3,-2)`, `(3,2)`, `(9,0)` for a controlled side-to-side shake.
- Locked evidence: both identities, Manager anatomy, dog anatomy, four paws, tail, blue collar, blank green diamond tag, crop, scale, and relative pose remain locked as one rigid pair; the strict stationary empty-corner proxy changed `0.0%`.
- Determinism: the final builder was rerun from its accepted locked plate and reproduced the source and GIF byte-for-byte; a second fresh isolated root check did the same. Builder SHA-256: `9f95b098682896e044889bfe4cb6967361f460606584435f7445d3fb4075fd5a`.

### 4. Walter Whiting CRM

- Intended motion: no body movement. Only a glasses glint travels through x positions `299,309,320,331`, and the two respirator-filter highlights pulse with radii `2,3,5,3px`.
- Locked evidence: canonical CRM identity, face, body, hands, yellow hazmat suit, respirator geometry, crop, scale, and exactly one briefcase are pixel-locked. Strict regions `empty-transparent-canvas-corner` and `locked-body-hands-suit-and-briefcase` both changed `0.0%` against `0.0%` allowed.
- Determinism: the repaired builder reproduced the final source and GIF byte-for-byte from the accepted locked plate, including a fresh isolated root check. Locked-plate SHA-256: `07165a8f1cc02b6b3a30adc167060984bb2ad6bf5233f68932b9e9c3a431f1cb`; builder SHA-256: `27f79d0537ce9476012216a36ad980a49980ebd814dc2593ddbd16e0206d2268`.

### 5. Gary Veeing CRM

- Intended motion: two attached arm/open-hand rigs make restrained opposing emphasis rotations: left `2.0°,0.7°,-0.7°,-2.0°`; right `-2.0°,-0.7°,0.7°,2.0°`.
- Locked evidence: male face, grey beanie, stubble, navy shirt core, crop, and scale remain fixed. Strict regions `locked-male-face` and `locked-shirt-core` measured `0.0%` change; direct changed pixels outside both allowed rigs were `[0,0,0,0]`.
- Determinism: independent isolated rebuild matched raw alpha, locked plate, normalized sheet, all frame hashes, source, GIF, and build evidence byte-for-byte. Builder SHA-256: `4a2f1b6c270acfe5b1f5c2a7e08a1f628ad18b5d675fb9d4646bc90e63d0c9d7`.

### 6. Gatsbying Manager

- Intended motion: one attached arm, hand, and champagne-coupe rig makes a restrained toast at angles `-3°,-1°,1°,3°`.
- Locked evidence: face and tuxedo core remain fixed; both strict regions measured `0.0%` change, and direct changed pixels outside the allowed toast rig were `[0,0,0,0]`.
- Determinism: independent isolated rebuild matched raw alpha, locked plate, normalized sheet, all frame hashes, source, GIF, and build evidence byte-for-byte. Builder SHA-256: `c8c86e88921ca298d4aa83dd57a289f27d06c0e265c726dc17887bc3ea21c375`.

### 7. Ron Burgunding CMA

- Intended motion: one attached arm, hand, and amber-tumbler rig makes a restrained toast at angles `-3°,-1°,1°,3°`.
- Locked evidence: Black male CMA identity, moustached face, and burgundy suit core remain fixed; both strict regions measured `0.0%` change, and direct changed pixels outside the allowed toast rig were `[0,0,0,0]`.
- Determinism: independent isolated rebuild matched raw alpha, locked plate, normalized sheet, all frame hashes, source, GIF, and build evidence byte-for-byte. Builder SHA-256: `b36ff12d8e0b6e22a440bbda1a7add56f26698de5e462600f2a151ed28d3c00d`.

### 8. Serhanting Manager

- Intended motion: two attached hand rigs move toward and away from the same centre button. Left-hand x offsets are `-16,-8,0,3px`; right-hand x offsets are `16,8,0,-3px`.
- Locked evidence: face and tie/lapels measured `0.0%` strict-region change; pinstripe torso, crop, and scale stay fixed, and direct changed pixels outside the allowed hand rigs were `[0,0,0,0]`.
- Determinism: independent isolated rebuild matched raw alpha, locked plate, normalized sheet, all frame hashes, source, GIF, and build evidence byte-for-byte. Builder SHA-256: `68339dadb7a170ef2ad135723b6661d836ba7614e5936db92baa6716087ec002`.

### 9. Spoking Content

- Intended motion: one attached right-arm/five-finger-salute rig makes a restrained reversible rotation at angles `-3°,-1°,1°,3°`.
- Locked evidence: the Asian male Content face and uniform torso measured `0.0%` strict-region change; crop and scale remain fixed, and direct changed pixels outside the allowed arm rig were `[0,0,0,0]`.
- Determinism: independent isolated rebuild matched raw alpha, locked plate, normalized sheet, all frame hashes, source, GIF, and build evidence byte-for-byte. Builder SHA-256: `db7ed392362b34945f9cac3235d8aee5fa423889609cff8f9eda09e4e62ef8c6`.

### 10. Tony Starking Marketing

- Intended motion: palm emitter and chest reactor overlays pulse through intensity levels `0.34,0.55,0.78,1.0`; no character rig moves.
- Locked evidence: the immutable Marketing face, beard, anatomy, powered-suit geometry, crop, anchor, and scale stay fixed outside the saved emitter mask. Strict region `locked lower body and boots` changed `0.0%` against `0.0%` allowed; the builder additionally asserts immutable face/body/suit pixels against the locked plate.
- Determinism: a fresh isolated root build reproduced both final hashes byte-for-byte. Builder SHA-256: `010a41532075a55ad6d1eb22c45bbaab2bd29b1f2b3465de5c60e4a607ac028f`.

### 11. Tyler Durdening Listings

- Intended motion: two attached fist/forearm rigs author left-jab peak, left half-retraction, two-fist guard, and right-jab peak. Only the active forearm receives attached tapered motion marks.
- Locked evidence: strict regions `locked face`, `locked torso core`, and `locked pelvis legs and shoes` each changed `0.0%` against `0.0%` allowed. Every phase is also compared directly with the immutable plate outside `allowed-left-and-right-forearm-mask.png`; mismatches were `[0,0,0,0]`.
- Determinism: two consecutive builds produced identical source and GIF hashes. Immutable-plate SHA-256: `225982b64e9cd75596da90afc44c1ff63d8943d499d1010707af4ae4b6d67553`; builder SHA-256: `7a25bcd688442a36195c5f543600a0537832b1282a90778dc64c8cf0c35a75f1`.

### 12. Robin Hooding Manager

- Intended motion: one continuous bowstring-and-arrow rig keeps fixed bow-tip anchors `(356,78)` and `(349,350)` while the nock/complete arrow moves through `(266,194)`, `(261,194)`, `(256,194)`, `(251,194)`. Total draw is a visible `15px`; arrow length remains `196px` and the arrowhead travels with the shaft.
- Locked evidence: strict regions `locked face core`, `locked bow hand and upper forearm`, and `locked lower body and boots` each changed `0.0%` against `0.0%` allowed. Every phase is compared directly with the immutable plate outside `allowed-single-string-arrow-nock-rig-mask.png`; mismatches were `[0,0,0,0]`.
- Determinism: two consecutive builds produced identical source and GIF hashes. Recoloured immutable-plate SHA-256: `0392a11539a8a4a325c8df6c2b23e5c61da1a634f25efc1c97f1c4a18b36fc1b`; builder SHA-256: `4d5e27a940d949762df67e089c997dceeae5f4a8dbb41ceccf0f9d4f2c99e1ea`.

## Required repair and delivery-size findings

### Walter identity repair

The earlier light-skinned Walter-like donor was discarded. A moderation-blocked targeted edit did not influence the final. The accepted current plate is a fresh canonical **dark-skinned bald male CRM Homie**, generated from `references/crm.png`, in one yellow hazmat suit with glasses, a respirator at the neck, and exactly one briefcase. The entire repaired identity/body plate is static; only the local glasses and filter highlights pulse. The current final hashes and strict report above supersede the retired candidate described by the older independent-failure note.

### Tyler two-fist and mask-escape repair

The residual original right guard fist was removed before the moving right-fist rig was composited. All four current authored phases show **exactly two fists**. The right jab extends cleanly, and the short motion marks are attached and tapered rather than reading as a detached rod. The corrected builder compares every phase directly with the immutable plate, not merely with cell 0, and records zero escaped pixels in every phase: `[0,0,0,0]`. The current final hashes and strict report supersede the older independent-failure note.

### Robin residual-string, wardrobe, and nock-draw repair

The old generated bowstring and fixed arrow tip were removed inside explicit masks so no residual second string or trailing fixed arrowhead remains. One continuous replacement string/arrow system is visible in every phase. A single frame-shared deterministic recolour changes exactly `16,782` green upper-garment/hat pixels to deep muted burgundy while preserving alpha geometry; olive leggings and tan leather remain. The complete arrow and nock travel `15px` toward the cheek and remain readable at 128px. The current final hashes and strict report supersede the older independent-failure note.

### Gary male CRM assignment

Gary is unambiguously the **male CRM identity**: tan male face, grey beanie, stubble, and navy shirt. Both attached open five-finger hands remain around shoulder/head height throughout. Full-size, 128px, direct mask, and byte-exact isolated-rebuild checks found no sex/role swap, detached hand, redraw, or out-of-rig motion.

### Serhant 128px buttoning

The jacket action is readable at delivery size: at 128px the hands visibly separate, approach, contact the same centre button, and reset; the blue pinstripes remain legible. The generic silhouette/XOR proxy is zero because this is internal motion, but direct delivery-resolution comparison changes `583`, `595`, and `654` pixels in phases 1–3 versus phase 0. The manual visual gate and direct rig audit therefore establish the buttoning action without relying on silhouette motion.

## Strict-report freeze

These are the exact current strict JSON reports used for this root gate:

| Candidate | Current strict-report path | Report SHA-256 |
|---|---|---|
| `jon-snowing-marketing` | `assets/homie-loaders/qa/strict-repairs/jon-snowing-marketing/report-root/strict-qa.json` | `7b81ffeba133b7bcb579dfb92f86ec38dd32a145bd08d63e0893181a9d966579` |
| `buffying-offers` | `assets/homie-loaders/qa/strict-repairs/buffying-offers/candidates/strict-qa/strict-qa.json` | `083ddd77afb70b5d3a54122cf711fba217cf6597d104199437556c147928b5f9` |
| `scooby-dooing-manager` | `assets/homie-loaders/qa/strict-repairs/scooby-dooing-manager/candidates/strict-qa/strict-qa.json` | `0ee86af9dfc28cebe9c65ae458e3adaa18ca50eb2888e3f70e872bf818edfa3a` |
| `walter-whiting-crm` | `assets/homie-loaders/qa/strict-repairs/walter-whiting-crm/candidates/strict-qa/strict-qa.json` | `b2c12df6aaa5c1e9ce8fd1004a7e477ae26022dc9022b38cc7b3ab732b21e0dc` |
| `gary-veeing-crm` | `assets/homie-loaders/qa/strict-repairs/gary-veeing-crm/candidates/qa-final/strict-qa.json` | `a4de6b417fe854b21876df1b2baf214d2ed6b427b4154322aba0d119194b37ef` |
| `gatsbying-manager` | `assets/homie-loaders/qa/strict-repairs/gatsbying-manager/candidates/qa-final/strict-qa.json` | `1cf43df2312e944c83b9357eb88c2ad95d33b5d648f90b53400923ace427d591` |
| `ron-burgunding-cma` | `assets/homie-loaders/qa/strict-repairs/ron-burgunding-cma/candidates/qa-final/strict-qa.json` | `fa4885067a4e0c0cd6d869e97e32256c8330d25a3028b70d805cdbe82521d6e2` |
| `serhanting-manager` | `assets/homie-loaders/qa/strict-repairs/serhanting-manager/candidates/qa-final/strict-qa.json` | `7a4c8221219dcd356e7f6b479bbe3d172d155bddeba9941939e6b0a001d6b649` |
| `spoking-content` | `assets/homie-loaders/qa/strict-repairs/spoking-content/candidates/qa-final/strict-qa.json` | `24097a2a9b87ef57972eb83eecb33ac0cf8136d5585066842ebe49f621a5bfaf` |
| `tony-starking-marketing` | `assets/homie-loaders/qa/strict-repairs/tony-starking-marketing/candidates/qa/strict-qa.json` | `6134536fa4621243786fe1d0680a516a102dd6bc0cc19b7871bc938bc8d761f7` |
| `tyler-durdening-listings` | `assets/homie-loaders/qa/strict-repairs/tyler-durdening-listings/candidates/qa/strict-qa.json` | `48e4d6032d5076e69fd2753d3ea13849153c4de1d8805f3bfb5542309622060b` |
| `robin-hooding-manager` | `assets/homie-loaders/qa/strict-repairs/robin-hooding-manager/candidates/qa/strict-qa.json` | `77817a161f5104bf01dd923a49878ed1ebcb10d49b67dc58403c5efd1b1ea568` |

## Scope boundary

- This is a candidate QA gate, not a production-promotion record.
- No production source, production GIF, manifest, site file, or independent QA document was edited for this record.
- The root gate did not rely on the earlier failed Walter, Tyler, or Robin reviews. Fresh independent reports for all three corrected candidates were generated afterward and are summarized in `MOVIE_NIGHT_QA-JON-SNOW-PLUS-ELEVEN-INDEPENDENT.md`.
- Any later change to a listed source, GIF, builder, locked plate, policy, visual review, or strict report invalidates this freeze and requires a new root gate.
