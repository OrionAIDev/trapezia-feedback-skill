"""Conformance self-test for skill-template.

Imports trapezia_skill_validator and asserts this skill directory audits
green (zero FAILs) at its detected tier.  This is the §6 shared-validator
guarantee: a skill instantiated from this template passes the same checks
the trapezia-skill-audit auditor uses.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from trapezia_skill_validator import run_audit


def test_skill_template_audits_green(skill_root: Path) -> None:
    """run_audit() on a git-initialized copy of this repo must have no FAILs."""
    report = run_audit(skill_root)
    failures = report.failures
    assert failures == [], (
        f"skill-template failed {len(failures)} check(s):\n"
        + "\n".join(f"  [{r.severity.value}] {r.id}: {r.message}" for r in failures)
    )


def test_skill_template_classifies_t2(skill_root: Path) -> None:
    """The template must classify as at least T2 (deployed skill)."""
    report = run_audit(skill_root)
    assert report.level == 2, f"expected T2, got T{report.level}"


def test_skill_template_not_sensitive(skill_root: Path) -> None:
    """The template must not be flagged sensitive (name 'skill-template' has no sensitive keywords)."""
    report = run_audit(skill_root)
    assert report.sensitive is False
