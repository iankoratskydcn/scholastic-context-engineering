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


def test_checkpoint_documents_use_the_declared_schema_and_current_suite_count():
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
    checkpoints = sorted((ROOT / ".hermes" / "checkpoints").glob("*.json"))
    assert checkpoints

    for path in checkpoints:
        document = json.loads(path.read_text(encoding="utf-8"))
        assert required <= document.keys(), path.name
        assert document["checkpoint_schema_version"] == "0.1"
        assert document["checkpoint_id"] == path.stem
        assert isinstance(document["tests"], list)

    current_counts = "\n".join(
        json.dumps(json.loads(path.read_text(encoding="utf-8"))["tests"])
        for path in checkpoints
    )
    assert "124 passed" in current_counts
    assert "118 passed" not in current_counts


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
