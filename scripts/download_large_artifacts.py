"""Download ignored benchmark archives with checksum verification."""

from __future__ import annotations

import argparse
import hashlib
from dataclasses import dataclass, replace
from pathlib import Path
from typing import BinaryIO, Callable, Iterable
from urllib.request import urlopen


@dataclass(frozen=True)
class ArtifactSpec:
    name: str
    relative_path: Path
    url: str
    sha256: str

    def with_expected_sha256(self, sha256: str) -> "ArtifactSpec":
        return replace(self, sha256=sha256)


ARTIFACTS = {
    "longpibench": ArtifactSpec(
        name="longpibench",
        relative_path=Path(
            ".hermes/lit_review/ranking/benchmark_verification/"
            "core_shard_a/artifacts/LongPiBench_data.zip"
        ),
        url="https://github.com/Rachum-thu/LongPiBench/releases/download/test/data.zip",
        sha256="7a9226fa2e7b6584dca6f0b43c8bd590f34b042a9fe55ae8d44bd4a2be4bc335",
    ),
    "alce": ArtifactSpec(
        name="alce",
        relative_path=Path(
            ".hermes/lit_review/ranking/benchmark_verification/"
            "core_shard_b/raw/ALCE-data.tar"
        ),
        url="https://huggingface.co/datasets/princeton-nlp/ALCE-data/resolve/main/ALCE-data.tar",
        sha256="eda837bf659a91b3648dc6e7ab6b17197664d93593857e8fdf3800b6aa6a98f0",
    ),
}


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download_artifact(
    spec: ArtifactSpec,
    root: Path,
    opener: Callable[[str], BinaryIO],
    chunk_size: int = 1024 * 1024,
) -> Path:
    """Download one artifact atomically and verify its SHA-256 digest."""
    destination = root / spec.relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    partial = destination.with_suffix(destination.suffix + ".part")
    partial.unlink(missing_ok=True)

    try:
        with opener(spec.url) as response, partial.open("wb") as stream:
            for chunk in iter(lambda: response.read(chunk_size), b""):
                stream.write(chunk)

        actual_sha256 = sha256_file(partial, chunk_size)
        if actual_sha256 != spec.sha256:
            raise ValueError(
                f"SHA-256 mismatch for {spec.name}: "
                f"expected {spec.sha256}, got {actual_sha256}"
            )
        partial.replace(destination)
    except Exception:
        partial.unlink(missing_ok=True)
        raise

    return destination


def _is_valid(path: Path, spec: ArtifactSpec) -> bool:
    return path.is_file() and sha256_file(path) == spec.sha256


def _selected(names: Iterable[str]) -> list[ArtifactSpec]:
    return [ARTIFACTS[name] for name in names]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "artifacts",
        nargs="*",
        choices=["all", *ARTIFACTS],
        default=["all"],
        help="artifacts to download (default: all)",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (default: inferred from this script)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="redownload even when an existing file has the expected checksum",
    )
    parser.add_argument("--timeout", type=float, default=120.0)
    args = parser.parse_args()

    names = list(ARTIFACTS) if "all" in args.artifacts else args.artifacts
    for spec in _selected(names):
        destination = args.root / spec.relative_path
        if not args.force and _is_valid(destination, spec):
            print(f"already present: {destination}")
            continue
        print(f"downloading {spec.name} -> {destination}")
        download_artifact(
            spec,
            args.root,
            opener=lambda url: urlopen(url, timeout=args.timeout),
        )
        print(f"verified {spec.name}: {spec.sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
