from pathlib import Path

def test_repository_bootstrap_declares_canonical_authority():
    root = Path(__file__).parents[1]
    readme = (root / "README.md").read_text()
    assert "Canonical schema authority:" in readme
    assert "Supported execution command:" in readme
    assert "Source-of-truth:" in readme
