# Changelog

All notable changes documented here. Format per
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning per semver.

## [Unreleased]

### In progress

- Initial bootstrap of the trapezia-feedback-skill repo from `OrionAIDev/skill-template`. Frontmatter, README, and SKILL.md customized to the spec. Stub script `scripts/feedback_draft.py` to anchor the T2 audit classification. Lib + tests + product configs to follow in subsequent commits.

## [0.0.1] - 2026-06-09

### Added

- Repository instantiated from `OrionAIDev/skill-template` (template v0.0.2).
- `SKILL.md`: skill-specific frontmatter and description per spec §3.
- `README.md`: rewritten as operator quickstart pointing at the design spec.
- `VERSION` → `0.0.1` (this release).
- `.trapezia-skill.toml`: `sensitive = true` (handles user-supplied text in transit; scrubber output goes to a public GitHub repo).
- `scripts/feedback_draft.py`: stub anchor for T2 audit; real implementation in subsequent commits per design spec.

## [0.0.2] - 2026-06-01

### Added
- `.gitattributes` (LF normalization) — instantiated skills inherit cross-platform-safe line endings.

## [0.0.1] - 2026-05-31

### Added
- Full skeleton: SKILL.md, README.md, CHANGELOG.md, VERSION, LICENSE, NOTICE.md,
  .gitignore, .trapezia-skill.toml, conventions/, scripts/.keep, hooks/ pair,
  tests/ with conformance self-test.
- `tests/test_structure.py` imports `trapezia-skill-validator` and asserts
  `run_audit()` returns zero FAILs at T2.
- `.trapezia-skill.toml` opt-out schema (machine-readable in plan-3, recorded now).
- Cross-platform `hooks/session-start` + `hooks/session-start.cmd` stubs.
- Baseline conventions adapted from `superhuman` (git, python, testing).
