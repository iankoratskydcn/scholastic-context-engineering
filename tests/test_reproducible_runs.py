import hashlib
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def _wheel_digest(output_dir: Path) -> str:
    wheels = sorted(output_dir.glob("*.whl"))
    assert len(wheels) == 1
    return hashlib.sha256(wheels[0].read_bytes()).hexdigest()


def test_checkpoint_documents_reconcile_every_full_suite_count_and_checkpoint_05_contract():
    import json

    required = {
        "checkpoint_schema_version",
        "checkpoint_id",
        "phase",
        "status",
        "tests",
        "reviewer_status",
        "next_allowed_task",
    }
    checkpoint_05_fields = {
        "scope",
        "tdd",
        "artifacts",
        "reviewer_status",
        "issues",
        "tests",
        "next_allowed_task",
    }
    checkpoints = sorted((ROOT / ".hermes" / "checkpoints").glob("*.json"))
    assert checkpoints
    full_suite_command = "env -u PYTHONPATH python -m pytest -q"
    full_suite_results = []

    for path in checkpoints:
        document = json.loads(path.read_text(encoding="utf-8"))
        assert required <= document.keys(), path.name
        assert document["checkpoint_schema_version"] == "0.1"
        assert document["checkpoint_id"] == path.stem
        assert isinstance(document["tests"], list)
        if path.stem == "05-ingestion":
            assert checkpoint_05_fields <= document.keys()
        for test_record in document["tests"]:
            if isinstance(test_record, dict) and test_record.get("command") == full_suite_command:
                full_suite_results.append((path.name, test_record.get("result")))

    assert len(full_suite_results) == len(checkpoints), full_suite_results
    assert all(result == "151 passed" for _, result in full_suite_results), full_suite_results
    serialized = "\n".join(path.read_text(encoding="utf-8") for path in checkpoints)
    assert "151 passed" in serialized
    for stale_count in ("118 passed", "124 passed", "145 passed", "150 passed"):
        assert stale_count not in serialized, stale_count


def test_source_expected_fixture_contains_canonical_record_ids():
    import json

    expected = json.loads((ROOT / "fixtures/canary/source-01.expected.json").read_text(encoding="utf-8"))
    assert expected["record_id"] == "structured_document-dbad3faf4345c1b2f9a1eb14"
    assert all(span["record_id"] for span in expected["spans"])
    assert [span["record_id"] for span in expected["spans"]] == [
        "span-f754b6cfd4f2c411e502dd90",
        "span-76431287858dbaab7f9eaadc",
    ]


def test_repeated_wheel_builds_are_byte_identical_without_runtime_dependencies(tmp_path):
    build_system = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert 'requires = ["setuptools>=61", "wheel"]' in build_system
    assert "dependencies" not in build_system.split("[tool.pytest", 1)[0]

    first = tmp_path / "first"
    second = tmp_path / "second"
    first.mkdir()
    second.mkdir()
    env = {**os.environ, "SOURCE_DATE_EPOCH": "0"}

    for output_dir in (first, second):
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "wheel",
                ".",
                "--no-deps",
                "--no-build-isolation",
                "--wheel-dir",
                str(output_dir),
            ],
            cwd=ROOT,
            env=env,
            check=True,
            capture_output=True,
            text=True,
        )

    assert _wheel_digest(first) == _wheel_digest(second)
