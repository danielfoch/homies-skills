#!/usr/bin/env python3
"""Verify that a deployed gallery serves the exact local manifest and GIF bytes."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": "Homies-release-verifier/1.0"})
    with urlopen(request, timeout=30) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status}")
        return response.read()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("base_url")
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument("--workers", type=int, default=12)
    args = parser.parse_args()
    base_url = args.base_url.rstrip("/") + "/"
    manifest_path = args.root / "manifest.json"
    manifest_bytes = manifest_path.read_bytes()
    manifest = json.loads(manifest_bytes)
    failures: list[str] = []

    remote_manifest = fetch(urljoin(base_url, "manifest.json") + "?release=verify")
    if sha256(remote_manifest) != sha256(manifest_bytes):
        failures.append("manifest.json byte hash differs")

    assets = [
        animation["asset"]
        for homie in manifest["homies"]
        for animation in homie["animations"]
    ]

    def check(relative: str) -> tuple[str, str | None]:
        local = (args.root / relative).read_bytes()
        digest = sha256(local)
        remote_url = urljoin(base_url, relative) + f"?v={digest[:12]}"
        try:
            remote = fetch(remote_url)
        except Exception as exc:
            return relative, f"fetch failed: {exc}"
        if sha256(remote) != digest:
            return relative, "byte hash differs"
        return relative, None

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(check, relative) for relative in assets]
        for future in as_completed(futures):
            relative, error = future.result()
            if error:
                failures.append(f"{relative}: {error}")

    print(f"checked remote manifest and {len(assets)} GIFs")
    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1
    print("live deployment exactly matches local release bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
