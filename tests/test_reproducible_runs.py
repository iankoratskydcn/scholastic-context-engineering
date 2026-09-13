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
    assert all(result == "176 passed" for _, result in full_suite_results)
    current_results = []
    for path in checkpoints:
        document = json.loads(path.read_text(encoding="utf-8"))
        current_results.append(document["current_full_suite"]["result"])
    assert current_results == ["176 passed"] * len(checkpoints)
    for stale_count in ("118 passed", "124 passed", "145 passed", "150 passed", "151 passed"):
        assert stale_count not in [result for _, result in full_suite_results]
        assert stale_count not in current_results


def test_source_expected_fixture_contains_canonical_record_ids():
    import json
    from scholastic_pipeline.ingestion import ingest_text, structure_document

    fixture = ROOT / "fixtures/canary"
    expected = json.loads((fixture / "source-01.expected.json").read_text(encoding="utf-8"))
    source = (fixture / "source-01.txt").read_bytes()
    actual = structure_document(ingest_text("source-01", source, run_id="source-01-run"))

    assert expected["record_id"] == actual.record_id
    assert expected["document_id"] == actual.document_id
    assert expected["revision"] == actual.revision
    assert expected["bytes_hash"] == actual.bytes_hash
    assert [span["record_id"] for span in expected["spans"]] == [
        span.record_id for span in actual.spans
    ]
    assert [span["text"] for span in expected["spans"]] == [
        span.text for span in actual.spans
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
