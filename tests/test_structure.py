"""Conformance self-test for trapezia-feedback-skill.

Imports trapezia_skill_validator and asserts this skill directory audits
green (zero FAILs) at T2. This is the shared-validator guarantee: every
Trapezia skill passes the same checks the trapezia-skill-audit auditor uses.
"""

from __future__ import annotations

from pathlib import Path

from trapezia_skill_validator import run_audit


def test_skill_audits_green(skill_root: Path) -> None:
    """run_audit() on a git-initialized copy of this repo must have no FAILs."""
    report = run_audit(skill_root)
    failures = report.failures
    assert failures == [], (
        f"trapezia-feedback-skill failed {len(failures)} check(s):\n"
        + "\n".join(f"  [{r.severity.value}] {r.id}: {r.message}" for r in failures)
    )


def test_skill_classifies_t2(skill_root: Path) -> None:
    """The skill must classify as T2 (deployed skill)."""
    report = run_audit(skill_root)
    assert report.level == 2, f"expected T2, got T{report.level}"


def test_skill_is_sensitive(skill_root: Path) -> None:
    """trapezia-feedback-skill is sensitive=true in .trapezia-skill.toml because it
    handles user-supplied text in transit and posts cleaned versions to a public
    repo. The data.separation check accordingly runs against committed files."""
    report = run_audit(skill_root)
    assert report.sensitive is True
