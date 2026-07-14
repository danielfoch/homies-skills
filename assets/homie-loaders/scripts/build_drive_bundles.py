#!/usr/bin/env python3
"""Build deterministic Google Drive source bundles for the wildcard release.

The source-master bundles are a partition, not snapshots layered on top of one
another: every current ``sources/wildcard`` manifest asset appears in exactly
one of E, F, or G.  The explicit repaired cohort keeps the high-churn release
easy to replace in Drive without leaving stale generated masters behind.
"""

from __future__ import annotations

import fnmatch
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "drive-bundles"

F_FOLLOW_ON = {
    "wrecking-ball-riding-research",
    "popping-my-collar-manager",
    "dirt-off-your-shoulders-marketing",
    "reformering-offers",
    "jazzing-content",
    "jazzercising-reports",
}

G_REPAIRED = set(
    """
sell-phoning-manager
neo-ing-offers
mavericking-manager
frodo-bagginsing-crm
peter-panning-listings
tinkerbelling-content
marioing-offers
mario-riding-yoshi-offers
jack-sparrowing-marketing
panning-for-gold-crm
diamonding-in-rough-crm
down-payment-hike-offers
escrow-lating-offers
operating-on-file-reports
lockboxing-offers
running-comps-cma
deslop-reports
moptimizing-crm
james-bonding-manager
sky-walkering-manager
hyah-ing-listings
master-chiefing-reports
dumbledoring-research
inspector-gadgeting-crm
cutting-red-tape-research
glengarrying-offers
buzz-lightyearing-manager
yoda-ing-cma
darth-vadering-offers
terminatoring-reports
batmaning-manager
supermanning-marketing
spider-manning-crm
wolverine-ing-research
joker-ing-content
beetlejuicing-listings
forrest-gumping-crm
mary-poppinsing-reports
ace-ventura-ing-marketing
shreking-manager
barbie-ing-listings
ken-ing-marketing
willy-wonka-ing-offers
mr-beaning-research
austin-powersing-content
zoolandering-reports
elf-ing-cma
home-alone-ing-crm
et-ing-research
mission-impossible-ing-manager
groundhog-daying-content
karate-kidding-offers
dirty-dancing-listings
pulp-fictioning-manager
michael-burrying-manager
harvey-spectering-manager
waynes-worlding-content
bill-and-ted-ing-crm
robocopping-offers
rambo-ing-manager
godfathering-reports
shake-it-offing-research
single-ladying-offers
moonwalking-content
poker-facing-listings
oops-i-did-it-again-ing-offers
hit-me-baby-one-more-timing-research
voguing-reports
espresso-ing-content
umbrella-ing-manager
cha-cha-sliding-marketing
dougie-ing-content
rickrolling-manager
harlem-shaking-listings
napoleon-dynamiting-content
elle-woodsing-reports
smooth-crimining-marketing
checking-the-backstreets-marketing
ymca-ing-cma
wednesday-ing-offers
disco-inferno-ing-reports
david-blaining-manager
cranking-that-marketing
cranking-the-step-marketing
cranking-the-motorbike-marketing
step-brothering-manager-crm
ricky-bobbying-manager
tarzaning-manager
jon-snowing-marketing
spoking-content
gatsbying-manager
scooby-dooing-manager
walter-whiting-crm
buffying-offers
ron-burgunding-cma
tony-starking-marketing
tyler-durdening-listings
robin-hooding-manager
gary-veeing-crm
serhanting-manager
hormozing-manager
""".split()
)


def wildcard_sources() -> dict[str, Path]:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    result: dict[str, Path] = {}
    for homie in manifest["homies"]:
        for animation in homie["animations"]:
            source = animation["source"]
            if not source.startswith("sources/wildcard/"):
                continue
            slug = animation["slug"]
            if slug in result:
                raise ValueError(f"duplicate wildcard slug in manifest: {slug}")
            result[slug] = ROOT / source
    return result


def docs_matching(patterns: tuple[str, ...]) -> list[Path]:
    return sorted(
        path
        for path in ROOT.iterdir()
        if path.is_file() and any(fnmatch.fnmatch(path.name, pattern) for pattern in patterns)
    )


def write_bundle(filename: str, slugs: set[str], sources: dict[str, Path], docs: list[Path]) -> None:
    path = OUT / filename
    with ZipFile(path, "w", ZIP_DEFLATED, compresslevel=9) as archive:
        for slug in sorted(slugs):
            source = sources[slug]
            if not source.is_file():
                raise FileNotFoundError(source)
            archive.write(source, source.relative_to(ROOT).as_posix())
        for doc in docs:
            archive.write(doc, doc.relative_to(ROOT).as_posix())
    print(f"{path}: {len(slugs)} source masters")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    sources = wildcard_sources()
    all_slugs = set(sources)

    if len(all_slugs) != 218:
        raise ValueError(f"expected 218 wildcard source masters, got {len(all_slugs)}")
    if F_FOLLOW_ON & G_REPAIRED:
        raise ValueError("F and G source cohorts overlap")
    unknown = (F_FOLLOW_ON | G_REPAIRED) - all_slugs
    if unknown:
        raise ValueError(f"bundle cohorts contain non-manifest slugs: {sorted(unknown)}")

    e_baseline = all_slugs - F_FOLLOW_ON - G_REPAIRED
    if (len(e_baseline), len(F_FOLLOW_ON), len(G_REPAIRED)) != (111, 6, 101):
        raise ValueError(
            "unexpected E/F/G partition: "
            f"{len(e_baseline)}/{len(F_FOLLOW_ON)}/{len(G_REPAIRED)}"
        )
    if e_baseline | F_FOLLOW_ON | G_REPAIRED != all_slugs:
        raise ValueError("E/F/G partition does not cover every wildcard source")

    shared = [ROOT / "manifest.json", ROOT / "PROMPT_TEMPLATE.md"]
    e_docs = shared + docs_matching(("GENERATION_PROMPTS-WILDCARD-*.md",))
    f_docs = shared + docs_matching(
        (
            "GENERATION_PROMPTS-POP-DANCE-D.md",
            "GENERATION_PROMPTS-POP-DANCE-E.md",
            "POP_DANCE_QA-D.md",
            "POP_DANCE_QA-E.md",
            "POP_DANCE_QA-F-INDEPENDENT.md",
            "POP_DANCE_DEDUPE.md",
        )
    )
    g_docs = shared + docs_matching(
        (
            "GENERATION_PROMPTS-MOVIE-NIGHT-*.md",
            "GENERATION_PROMPTS-POP-DANCE-A.md",
            "GENERATION_PROMPTS-POP-DANCE-B.md",
            "GENERATION_PROMPTS-POP-DANCE-C.md",
            "GENERATION_PROMPTS-POP-DANCE-G.md",
            "GENERATION_PROMPTS-POP-DANCE-H.md",
            "GENERATION_PROMPTS-POP-DANCE-I.md",
            "MOVIE_NIGHT_*.md",
            "POP_DANCE_QA-A*.md",
            "POP_DANCE_QA-B*.md",
            "POP_DANCE_QA-C*.md",
            "POP_DANCE_QA-G.md",
            "POP_DANCE_QA-H.md",
            "POP_DANCE_QA-I*.md",
            "POP_DANCE_QA-SEMANTIC-REBUILD-*.md",
            "POP_DANCE_DEDUPE.md",
        )
    )

    write_bundle(
        "Homies-AI-Loading-Gallery-Source-Masters-E-Wildcard.zip",
        e_baseline,
        sources,
        e_docs,
    )
    write_bundle(
        "Homies-AI-Loading-Gallery-Source-Masters-F-Pop-Dance-Follow-on.zip",
        F_FOLLOW_ON,
        sources,
        f_docs,
    )
    write_bundle(
        "Homies-AI-Loading-Gallery-Source-Masters-G-Strict-Repair-Release.zip",
        G_REPAIRED,
        sources,
        g_docs,
    )


if __name__ == "__main__":
    main()
