#!/usr/bin/env python3
"""Build clean runtime and complete-release archives.

Both archives are rebuilt from current workspace files and deliberately exclude
credentials, Vercel link state, caches, Finder metadata, and stale/nested ZIPs.
"""

from __future__ import annotations

import fnmatch
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
COMPLETE = ROOT.parent / "Homies-AI-Loading-Gallery-Complete-2026-07-12.zip"
RUNTIME = ROOT / "homie-loaders-runtime.zip"

BLOCKED_PARTS = {".git", ".vercel", "__pycache__"}
BLOCKED_NAMES = {".DS_Store", ".env", ".env.local"}
BLOCKED_SUFFIXES = {".pyc", ".pyo", ".zip"}

RUNTIME_ROOT_PATTERNS = (
    "README.md",
    "SHARE.md",
    "PROMPT_TEMPLATE.md",
    "GENERATION_PROMPTS-*.md",
    "*_QA*.md",
    "*_DEDUPE.md",
    "manifest.json",
    "preview.html",
    "contact-sheet.jpg",
)
# Include the deployable site as well as the reusable runtime assets.  The
# shared ``allowed`` gate strips Vercel link state, local environment files,
# caches, Finder metadata, and nested archives from this tree.
RUNTIME_DIRS = ("gifs", "references", "scripts", "vercel-site")


def allowed(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    if any(part in BLOCKED_PARTS for part in relative.parts):
        return False
    if path.name in BLOCKED_NAMES or path.name.startswith(".env"):
        return False
    if path.suffix.lower() in BLOCKED_SUFFIXES:
        return False
    return path.is_file()


def runtime_files() -> list[Path]:
    files: set[Path] = set()
    for path in ROOT.iterdir():
        if path.is_file() and any(
            fnmatch.fnmatch(path.name, pattern) for pattern in RUNTIME_ROOT_PATTERNS
        ):
            files.add(path)
    for directory in RUNTIME_DIRS:
        files.update(path for path in (ROOT / directory).rglob("*") if allowed(path))
    return sorted(path for path in files if allowed(path))


def complete_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*") if allowed(path))


def write(path: Path, files: list[Path]) -> None:
    with ZipFile(path, "w", ZIP_DEFLATED, compresslevel=9) as archive:
        for file in files:
            archive.write(file, file.relative_to(ROOT).as_posix())
    print(f"{path}: {len(files)} files")


def assert_clean(path: Path) -> None:
    with ZipFile(path) as archive:
        names = archive.namelist()
    bad = [
        name
        for name in names
        if any(part in BLOCKED_PARTS for part in Path(name).parts)
        or Path(name).name in BLOCKED_NAMES
        or Path(name).name.startswith(".env")
        or Path(name).suffix.lower() in BLOCKED_SUFFIXES
    ]
    if bad:
        raise ValueError(f"unsafe/stale archive entries in {path}: {bad[:10]}")


def main() -> None:
    write(RUNTIME, runtime_files())
    write(COMPLETE, complete_files())
    assert_clean(RUNTIME)
    assert_clean(COMPLETE)


if __name__ == "__main__":
    main()
