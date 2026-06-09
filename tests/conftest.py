"""Shared test fixtures for skill-template tests.

Provides the ``skill_root`` fixture: a git-initialized tmp_path copy of
the real skill directory, so T2 checks (git.repo, git.remote) pass cleanly
during the conformance self-test.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

# The real skill root is the parent of this tests/ directory.
_SKILL_ROOT = Path(__file__).parent.parent


@pytest.fixture
def skill_root(tmp_path: Path) -> Path:
    """Return a git-initialized copy of the skill directory in tmp_path.

    Steps:
    1. Copy the entire skill directory (excluding .git and __pycache__) to
       tmp_path/skill-template/.
    2. Run git init + an empty commit inside the copy.
    3. Return the copy's root path.

    The copy is T2 (has CHANGELOG.md and VERSION) and has a real .git directory,
    so all T2 checks including git.repo run and pass.

    Note: git.remote will WARN (no remote configured) but will not FAIL —
    report.passed is True when there are only WARNs.
    """
    dest = tmp_path / _SKILL_ROOT.name

    def _ignore(src: str, names: list[str]) -> list[str]:
        return [n for n in names if n in {".git", "__pycache__", ".pytest_cache", ".venv"}]

    shutil.copytree(str(_SKILL_ROOT), str(dest), ignore=_ignore)

    # Initialize a real git repo so git.repo (min_level=2) passes.
    subprocess.run(["git", "init"], cwd=str(dest), check=True, capture_output=True)
    subprocess.run(
        [
            "git",
            "-c", "user.email=test@trapezia.ai",
            "-c", "user.name=Test",
            "commit",
            "--allow-empty",
            "-m", "chore: test fixture init",
        ],
        cwd=str(dest),
        check=True,
        capture_output=True,
    )
    # Note: git add is skipped intentionally — we only need .git to exist
    # for git.repo to PASS. The test runs run_audit() which only checks
    # (root / ".git").exists(), not the contents of the index.
    return dest
