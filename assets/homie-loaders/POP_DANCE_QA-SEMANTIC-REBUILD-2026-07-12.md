# Pop & Dance authoritative semantic rebuild report

Completed 2026-07-13 after the 2026-07-12 generation/rebuild run.

> Historical evidence for the original 41-loader Pop & Dance release. The
> current gallery intentionally retires `back-togethering-content` and
> `twenty-two-ing-crm`; the remaining 39 active loaders retain this audit
> evidence.

## Final release verdict

**41/41 PASS, 0 blockers.**

The final evidence pack was rebuilt from the exact current-production files after the accepted Single-Ladying v9 promotion. Review covered:

- 41 manifest mappings and exact production source/GIF hashes.
- 164 authored source cells at the native 627 px cell size.
- 41 full-resolution source contacts and 41 source contacts at 128 px.
- 41 contacts decoded from the canonical GIFs at 128 px, comprising 246 GIF frames.
- Semantic action, source/GIF agreement, loop continuity, crop, anatomy, props, stationary elements, chroma seams, fragments, and redraw wiggle.

Costume recognition alone did not qualify. Generic whole-cutout sway, effect-only motion, absent or imperceptible action, approximate choreography, and dirty frames were rejected.

Final evidence index: `/tmp/pop-dance-final-41-evidence/index.md`  
Final machine-readable evidence: `/tmp/pop-dance-final-41-evidence/evidence.json`  
Final production verdict: `/tmp/release-strict-qa/final-current-production-41-verdict.md`

## Audit history

| Milestone | Result |
|---|---|
| Initial strict semantic audit | **12/41 PASS**. Twenty-nine assets relied on costume recognition, micro-wiggle, generic translation, effect-only movement, wrong choreography, or dirty/mismatched source frames. |
| First rebuild wave | **29 assets rebuilt** around action-specific mechanics and loader-scale silhouettes. |
| Fresh unsoftened production audit | **33/41 PASS, 8 FAIL**. The eight failures below were reopened instead of being waived. |
| Final repair wave | All eight source/GIF pairs were rebuilt, independently reviewed, and promoted by exact hash. |
| Post-promotion production audit | **41/41 PASS, 0 blockers** across all full/source128/decoded-GIF128 evidence. |

## Final repaired eight

| Asset | Accepted mechanic | Production source SHA-256 | Production GIF SHA-256 |
|---|---|---|---|
| `back-togethering-content` | Receiver travels low/away → ear → away while the free hand progresses palm-up → stop → dismissive sweep. Former hip/third-hand debris is removed. | `dd22339afe60b09bc03d156e0028ca85fa1d00b79c3f2d04fad7991c923239d9` | `a5405ef795495b0a5c50a9a8cae26f37395758d1c91ac958f72b623fa7667b2b` |
| `shake-it-offing-research` | Alternating shoulder hikes and connected arm follow-through remain visible at 128 px while head, pelvis, and feet stay anchored. | `3ce7c0eec296ae5a83b17d98eeddd6d058ced05c3c27b39e19138fd8b05af9ea` | `0225d3c7b451864fde89e5ffc096c7fa2dee6f8e0b63e63cd8784c264ff0890e` |
| `single-ladying-offers` | The original open palm and four neighbouring digits remain visible and fixed. Only the gold-marked anatomical ring finger rotates left → upright → right → ease-back, eliminating whole-hand-wave and thumb/middle-finger ambiguity. | `79989bebd5a91a963476f62bc54e5be3c57496234279370669a91b24a82c90cd` | `e3e3a19fb8949352b17d74cf8b2fd4b27ffb89737b2d73630c6601e02bc0ade6` |
| `thrillering-marketing` | Superseded 2026-07-13: the entire silhouette now performs the supplied low Thriller claw-step—deep wide crouch, dropped hips, lateral weight transfer, pitched torso, lifted elbows and limp wrists—instead of an upright shoulder pop. One shoe baseline is integer-locked and every frame contains one debris-free connected character. | `68d6b6a7e2e7c9e4529957692bff5c6b7bc17ae4a95b3a2aa6b4d854ed1536ec` | `cef86e9c98145bec9060b8664509f0c480053ad059f1e34a3f9e6405a4904ada` |
| `moonwalking-content` | A fixed side-view upper plate performs two mirrored 100 px flat-shoe backward glides around a same-contact heel/weight switch. Both shoes stay grounded; no walk stride or toe tap. | `382d1a26979a42fdb21c27fbaf07d2bc9b3041823f1e59bb0b13d8c52459264e` | `1cc265754c39895b2b1ecdbc29ba437361837acff5c05469a897d8edbe150c79` |
| `gangnam-styling-cma` | Crossed reins remain connected while hips, knees, ankles, and heels form a real horse-riding compression/weight-transfer loop. | `5b2a68aa99dfc2fee0298aac53d2a1efbdd37793d9e1e8db8e368f63a17bbad9` | `e65d0078a8ca4b2d5523d88a277379d96e05e68dba5bd1a9c29075d5b4931496` |
| `oops-i-did-it-again-ing-offers` | Superseded 2026-07-13: one canonical Offers Homie in a seamless glossy pure-red spandex catsuit holds the supplied chest-palm/crossed-leg pose while only the opposite connected forearm straightens into the exact horizontal reach. The former whole-character hip rotation was rejected. The decoded GIF has zero changed pixels across the fixed bun, face, torso, chest hand, hips, legs and feet, and one shared palette removes colour shimmer. | `bf7f632f6f869210f99e33dedf9805182a44765fd1b201af57bd8da4a29b799b` | `268893b78d9de5affae5392311f915433e14333400c725cde6d6eaef15350e6d` |
| `wrecking-ball-riding-research` | The top chain pivot stays fixed while chain, rider, and ball sweep through a real pendulum arc. | `48b86e61dd75a35a71c07f9fca975b5b8ccbc8c7b35b385d26610a37acab746c` | `c5f19d522537e2958c4a3e6bc684d2180ad0a7bd36668d0bdc9697e12cf33adc` |

All 16 current-production files above are byte-for-byte identical to their independently approved replacement files.

The 2026-07-13 Thrillering correction has persistent full-size, 128px, decoded-GIF and independent-review evidence under `qa/strict-repairs/thrillering-marketing/`. Its structural and recorded visual gate is `1/1 PASS`; the minimum source margin is 60px and every authored cell contains one connected foreground component with zero tiny components.

The 2026-07-13 Oops correction has persistent full-size, 128px, decoded-GIF, policy and independent-review evidence under `qa/strict-repairs/oops-i-did-it-again-ing-offers/`. Its strict policy gate is `1/1 PASS` with zero warnings: 65px minimum margin, one connected component per cell, 0px registration shift, 0.0% stationary-region change, identical decoded-GIF bounding boxes, and zero changed fixed-body pixels outside the reaching arm.

## Sell-Phoning anchor repair

Sell-Phoning uses the supplied Hotline Bling references: bright saturated orange puffer, deep bent-forward crouch, low finger beat, stop palm, opposite point/sweep, and half-rise/heel-lift pose. It no longer relies on a generic sway.

- Source SHA-256: `a7904b843e559e0a13d746d46b6dbfd2fbe85f91ffa879610ccc053e7b57a45d`
- GIF SHA-256: `c70112813d19ae6fe7311001bad7a62d57611cfad0d346999241688b388e8234`

## Production contract

The canonical production validator completed successfully after the final promotion:

```text
checked 358 GIFs
all GIFs satisfy the production contract
```

This confirms **358/358 structural contract compliance**. The separate human semantic/artifact gate above confirms **41/41 Pop & Dance compliance**.
