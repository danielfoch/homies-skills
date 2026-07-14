# Movie Night QA plan — Hormozing

Date: 2026-07-14  
Asset: `hormozing-manager`  
Status: **PASS**. Root and independent production gates are complete.

## Candidate under review

- Prompt/provenance record:
  `GENERATION_PROMPTS-MOVIE-NIGHT-HORMOZING.md`
- Candidate workspace:
  `qa/strict-repairs/hormozing-manager/candidates/`
- Intended source: `sources/wildcard/hormozing-manager.png`
- Intended GIF: `gifs/wildcard/hormozing-manager.gif`
- Manifest collection: Movie Night, immediately after `serhanting-manager`

## Required root QA gates

- Inspect all four authored cells at full size and at the intended `128x128`
  display size.
- Confirm the canonical male Manager Homie remains recognizable and the
  backward blue cap, clear glasses, beard, white nasal strip, sleeveless shirt,
  silver watch, pointing hand, book, and `$100M` title are coherent.
- Confirm exactly one person, two connected arms, two coherent hands, and one
  stable book; reject extra fingers, detached fragments, overlaps, trash, crop,
  or changing book perspective.
- Require a byte-locked alpha silhouette and no pixel changes outside the
  permitted book-effect mask. The `$100M` title itself must remain fixed.
- Confirm only the three value bars and final gold glint advance, and that the
  action remains readable at `128x128` without whole-character wiggle.
- Confirm four unique authored phases, reversible sequence
  `[0, 1, 2, 3, 2, 1]`, durations
  `[210, 140, 140, 210, 140, 140]`, transparent corners, and infinite looping.
- Perform an isolated deterministic rebuild and require byte-for-byte equality
  for the rebuilt candidate artifacts and evidence before promotion.
- Run `scripts/strict_qa.py` and `scripts/verify.py`; record actual reports,
  hashes, warnings, and reviewer notes here only after those commands finish.

## Required independent QA gates

A reviewer who did not author the candidate must inspect the full-size source,
the animated GIF, and the `128x128` presentation independently. The reviewer
must verify character/style continuity, anatomy, book/title continuity,
effect-only motion, action readability, clean transparency, framing, and loop
stability. A production promotion must not be inferred from this checklist;
record the independent result and evidence paths only after review is complete.

## Release record

- Root visual review: **PASS**. The full 1254×1254 source, all four 627×627
  cells, the 128px source contact, and the decoded six-frame 128px GIF contact
  were inspected. The four recorded cell gates are in
  `qa/strict-repairs/hormozing-manager/candidates/visual-review.json`.
- Candidate strict QA: **PASS**, 1/1, zero failures and zero warnings. Report:
  `qa/strict-repairs/hormozing-manager/candidates/report-final/`.
- Independent visual review: **PASS**. Reported in
  `qa/strict-repairs/hormozing-manager/visual-review-independent.json` and
  `MOVIE_NIGHT_QA-HORMOZING-INDEPENDENT.md`.
- Independent production strict QA: **PASS**, 1/1, zero failures and zero
  warnings. Report: `qa/strict-repairs/hormozing-manager/report-independent/`.
- Structural verification: `scripts/verify.py` checked all 371 production GIFs
  and all satisfy the production contract.
- Isolated rebuild comparison: **byte-exact** for source, GIF, build evidence,
  locked plates, alpha contact, book mask, effect mask, and title glyph mask.
- Production source SHA-256:
  `0732f5c23f4c24e8f9423fc85733f89d33d09d00d3f2b0725c4e78a1e4d8da17`.
- Production GIF SHA-256:
  `373a6ff9a0d1479af6090b9f9417800ca15a5f11252e7ec2515fe7c24db33a3a`.
- Measured drift, centroid shift, mask XOR, silhouette motion, foreground-area
  span, bounding-box span, and stationary-region change are all `0.0`; upper
  anchor NCC is `1.0`; minimum source-cell margin is 84px.
- Promotion decision: **approved** for the 371-loader production release.
