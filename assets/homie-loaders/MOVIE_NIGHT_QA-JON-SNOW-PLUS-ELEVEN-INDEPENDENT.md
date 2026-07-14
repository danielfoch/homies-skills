# Movie Night QA — Jon Snow Plus Eleven (independent clean-room)

Date: 2026-07-14 (America/Toronto)

Scope: the exact twelve-loader Jon Snow Plus Eleven release set. Evidence comes from each slug's fresh `qa/strict-repairs/<slug>/report-independent/strict-qa.json` and `visual-review-independent.json`. This record does not promote or alter an image, GIF, manifest, or site file.

## Verdict

**PASS — 12/12 finalized candidates. Zero warnings and zero failures.**

- Every independent strict report records `passed: true`, an empty `warnings` array, an empty `failures` array, and a complete cell-by-cell manual visual gate covering full-size cells, 128px cells, and the decoded GIF.
- Clean isolated rebuilds reproduced all twelve final source PNGs and GIFs byte-for-byte from their accepted locked inputs. Generated frame/plate/mask evidence also matched where persisted.
- Each candidate source and GIF is byte-identical to its current production counterpart at `sources/wildcard/<slug>.png` and `gifs/wildcard/<slug>.gif`; the hashes below therefore freeze the production-equivalent bytes.
- All GIFs satisfy the shared runtime contract: 256×256, transparent, six frames, four unique phases, reversible order `0,1,2,3,2,1`, durations `210,140,140,210,140,140ms`, infinite loop, and exact loop closure.

## Final artifact and finding ledger

| Candidate | Source PNG SHA-256 | GIF SHA-256 | Independent QA | Key clean-room finding |
|---|---|---|---:|---|
| `jon-snowing-marketing` | `8ae889775a0a659fb27142e8c04e45df21293ad26cf12cfc8f4b5d241f92f966` | `081883e2ec709593c38ed98cb16cd84536173ca24e8964f39031c680cd4d95fb` | PASS · 65px | One male Marketing Homie, two connected hands, one uninterrupted sword, six intentional snowflakes, and one blade-confined glint; face, cloak, armor, hands, sword, crop, and scale stay locked. |
| `buffying-offers` | `883c3f2ceb2b749c22e7215b3556a3c9df7a51e9a873788aea99ab677ef26ea8` | `6565844e06abce38749e33523c26c52d03b4f1975c4837860f16356b4560f572` | PASS · 71px | Unmistakably adult female Offers identity, exactly one wooden stake and one empty second hand; the connected body/stake rig makes one clean boot-anchored guarded lean. |
| `scooby-dooing-manager` | `61dc3d62762f91cd870c2593e87b5d4b93aca1b54c91f46062d807edc183b4be` | `cf5003e386102c932bd60feba93bc9f82df6224ac421fffbed0abd5431187f07` | PASS · 72px | Exactly one male Manager and one large brown spotted dog with four paws, tail, blue collar, and blank green diamond tag; their relative geometry is locked during the shared shake. |
| `walter-whiting-crm` | `3c30d08ce62138368d0ec71a261b0e573de85c0520acc0a26db47ad680939944` | `d1086c933c49a0e2e9ee1959fd3fcf768b042e97f5637318d27d5d58dd5f959d` | PASS · 74px | Corrected dark-skinned bald male CRM in one yellow hazmat suit with one glasses pair, one neck respirator, and one vertical briefcase; only the local glasses/filter highlights change, with zero pixels outside their mask. |
| `gary-veeing-crm` | `72abdf6a37492c47cc93172e311a3ec7c37f23cc7dfaa5298c832f5d796413aa` | `916e302a614de9edd3b7327b4eccb7f085324acc09185221958ae84d8b43ea47` | PASS · 83px | Unambiguously male CRM with grey beanie, stubble, navy shirt, and two attached open five-finger hands at shoulder/head height; face/torso stay fixed and no motion escapes the two arm rigs. |
| `gatsbying-manager` | `a354e8b829adcb45bde98864eeb108f21a97cd3dc953361627a3a1b69098b30b` | `085f3f58c889dcd46acdf963307e7c5310ccc6bb4ac67fa6758ea223e9776f86` | PASS · 86px | One male Manager and one continuous champagne coupe remain coherently attached through the restrained toast; face and tuxedo core stay locked with zero out-of-rig motion. |
| `ron-burgunding-cma` | `0049af3ccaf578d2713c271b0f956cfe6d6d18b88cc29d2752f42299349f9b2f` | `9747e6408df19ae78d84804fbb7e11b4bc03d4f88a92e27b03612a68243503fd` | PASS · 84px | Black male CMA identity, moustache, burgundy suit, and exactly one coherently gripped amber tumbler persist through the toast; no duplicate prop or out-of-rig motion. |
| `serhanting-manager` | `1ae6833056cc64ebf1025a07ff86144373070d5c12bb23c9ebf7b5ea2b786fe3` | `ec406f690b731c8388d3a60783791948069ce85442b83f5d04cc890b9d74ee3f` | PASS · 76px | Male Manager's hands visibly separate, approach, fasten the same centre button, and reset at 128px; blue pinstripes remain readable and face/tie/lapels stay locked. |
| `spoking-content` | `36d0c2ab59419c30dacdb4b1705bdfce997a61f989235a7935dcae77e1157833` | `b9b88ac4ee647344eea4a9e811d2a6bda4fbfed3e7223df0bed74995acef3b47` | PASS · 86px | Asian male Content identity holds an anatomically correct salute with four upright fingers grouped 2+2 plus a separate thumb; only the attached right-arm rig moves. |
| `tony-starking-marketing` | `0f7331eb81717dc6920d26fb4b8ec25cefec356980be5777b48cade22dd7aea9` | `5abb05d4b2a993c127f2585b91eea0f8ffdff9bbe7c5bb8ae837b9b4c1c9b17a` | PASS · 70px | One male Marketing Homie in one continuous red/gold powered suit has one raised five-finger palm emitter and one chest reactor; both pulses read at 128px while the character plate remains fixed. |
| `tyler-durdening-listings` | `3f04d49bfeca9aa98c3aae199fbb98b8752e7c92b061fba4e451835e6df945b2` | `abfba32629dab614567f5c07444e85c75770f29528e566bd67c7ee7e521a6bf1` | PASS · 70px | Exactly two fists appear in every phase through attached alternating jabs; both original guard-fist erase regions retain zero skin, body regions are locked, and every phase has zero changes outside the forearm mask. |
| `robin-hooding-manager` | `45b28eac67576766fcf254d6affb1d2ec5180f29bc235091da73094f2d37c171` | `33d8044924f5f549a8856ad5671871f92fc4dc5932ed98549e899defae50ac13` | PASS · 70px | Frame-shared burgundy/olive/tan Manager has no old-string trace and exactly one string, nock, shaft/fletching assembly, and arrowhead; fixed bow-tip anchors support a visible 15px draw with no geometry drift. |

## Mask, identity, and delivery-size conclusions

- Fixed-region checks found no unintended face, torso, costume, prop, crop, anchor, or scale drift. Local-rig candidates recorded zero changed pixels outside their saved allowed masks; shared whole-rig candidates preserved internal geometry exactly.
- Full-size and 128px review found no identity/role swaps, extra anatomy, duplicate props, disconnected grips, crop faults, green debris, pseudo-text, or redraw wiggle.
- The three repaired blockers are closed: Walter now uses the intended CRM identity and local-only highlight motion; Tyler has exactly two fists and no residual fist/arm/rod; Robin has one replacement string/arrow system and a readable 15px nock draw.
- Gary's male CRM assignment, Spock's five-finger 2+2 salute, and Serhant's 128px jacket-buttoning action were explicitly rechecked rather than inferred from structural metrics.

## Tyler report-input correction

Tyler's corrected asset and independent review were internally PASS, but an initial `report-independent` run consumed stale cell-3 anatomy/prop-continuity booleans and therefore emitted a contradictory FAIL. The independent review input was corrected to the actually inspected cell state, strict QA was rerun explicitly with `qa/strict-repairs/tyler-durdening-listings/visual-review-independent.json`, and the current final report is **PASS** with a complete manual gate, zero warnings, and zero failures. The asset bytes were not changed during that correction.

## Scope boundary

- Evidence paths are `qa/strict-repairs/<slug>/report-independent/` and `qa/strict-repairs/<slug>/visual-review-independent.json` for each row.
- This Markdown file is a read-only consolidation of finalized evidence. No source PNG, GIF, builder, locked plate, policy, manifest, or site artifact was modified.
- Any later byte change to a listed source, GIF, independent review, or independent strict report invalidates this record and requires a new clean-room gate.
