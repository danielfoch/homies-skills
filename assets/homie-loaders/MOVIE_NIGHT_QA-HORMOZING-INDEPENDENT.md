# Hormozing — independent production QA

Asset: `hormozing-manager`  
Verdict: **PASS**

## Independent visual inspection

The production 1254×1254 source sheet, all four 627×627 cells, the four-cell
128px contact, all six decoded 256×256 GIF frames, and the six-frame 128px GIF
contact were inspected independently.

Every phase has exactly one male character, one head, one backward royal-blue
cap, one pair of clear glasses, one white nasal strip, one beard, one white
sleeveless shirt, two connected arms, two attached hands, and one stable navy
book. The exact `$100M` title is unchanged and readable at 128px. Three value
bars stack only inside the same locked book, and the phase-three gold glint is
clipped to the book.

No wiggle, scale pulse, crop fault, green debris, extra limb, duplicate
character, changing text, prop morph, palette spill, redraw, registration drift,
or continuity issue was found.

## Reproducibility and hashes

- Production source SHA-256:
  `0732f5c23f4c24e8f9423fc85733f89d33d09d00d3f2b0725c4e78a1e4d8da17`
- Production GIF SHA-256:
  `373a6ff9a0d1479af6090b9f9417800ca15a5f11252e7ec2515fe7c24db33a3a`
- Candidate and isolated-rebuild build-evidence SHA-256:
  `9f9db056199f3ad8002a7d404ff11ee97c8145be54609f9dbd273fb745a64145`
- The production source and GIF are byte-exact against both the candidate build
  and `/private/tmp/hormozing-rebuild.Hy0U0Y`.
- `build-evidence.json`, `allowed-book-effect-mask.png`, `book-mask.png`,
  `title-glyph-mask.png`, `alpha-normalized.png`, `locked-plate.png`, and
  `locked-titled-plate.png` are byte-exact between candidate and isolated build.
- The four source phases have zero changed pixels outside the allowed book
  effect mask and zero changed pixels in the `$100M` title glyph mask.
- Foreground silhouette, bounding box, crop, and scale are identical in all four
  source phases; the decoded GIF alpha silhouette is identical in all six
  frames.
- GIF sequence: `0, 1, 2, 3, 2, 1`; durations: `210, 140, 140, 210, 140, 140`
  ms; infinite loop; transparent corners; exact reverse continuity.

## Automated gate

The production asset was checked with `scripts/strict_qa.py` using the copied
candidate policy, independent visual review, and production alignment entry.
The result is **PASS** with zero failures and zero warnings. Measured maximum
registration shift, centroid shift, mask XOR, and silhouette motion are all
`0.0`; stationary-region change is `0.0%`; upper-anchor NCC is `1.0`. The
report is stored at:

`qa/strict-repairs/hormozing-manager/report-independent/`
