import hashlib
import importlib.util
import sys
from pathlib import Path

import pytest


_MODULE_PATH = Path(__file__).parents[1] / "scripts" / "download_large_artifacts.py"
_SPEC = importlib.util.spec_from_file_location("download_large_artifacts", _MODULE_PATH)
assert _SPEC and _SPEC.loader
_MODULE = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _MODULE
_SPEC.loader.exec_module(_MODULE)
ARTIFACTS = _MODULE.ARTIFACTS
download_artifact = _MODULE.download_artifact


class FakeResponse:
    def __init__(self, payload: bytes):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self, chunk_size: int) -> bytes:
        if not self.payload:
            return b""
        chunk, self.payload = self.payload[:chunk_size], self.payload[chunk_size:]
        return chunk


def test_catalog_contains_the_two_large_benchmark_archives():
    assert set(ARTIFACTS) == {"longpibench", "alce"}
    assert str(ARTIFACTS["longpibench"].relative_path).endswith(
        "core_shard_a/artifacts/LongPiBench_data.zip"
    )
    assert str(ARTIFACTS["alce"].relative_path).endswith(
        "core_shard_b/raw/ALCE-data.tar"
    )


def test_download_artifact_streams_and_verifies_sha256(tmp_path: Path):
    payload = b"benchmark payload"
    spec = ARTIFACTS["longpibench"].with_expected_sha256(hashlib.sha256(payload).hexdigest())

    output = download_artifact(
        spec,
        tmp_path,
        opener=lambda _url: FakeResponse(payload),
    )

    assert output == tmp_path / spec.relative_path
    assert output.read_bytes() == payload
    assert not output.with_suffix(output.suffix + ".part").exists()


def test_download_artifact_rejects_checksum_mismatch(tmp_path: Path):
    spec = ARTIFACTS["alce"].with_expected_sha256("0" * 64)

    with pytest.raises(ValueError, match="SHA-256 mismatch"):
        download_artifact(
            spec,
            tmp_path,
            opener=lambda _url: FakeResponse(b"not the archive"),
        )

    assert not (tmp_path / spec.relative_path).exists()
