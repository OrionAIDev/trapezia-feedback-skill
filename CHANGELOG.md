# Changelog

All notable changes documented here. Format per
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning per semver.

## [Unreleased]

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security

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
