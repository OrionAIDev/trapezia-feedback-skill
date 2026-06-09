# <skill-name>

> **Instantiated from `skill-template`.** Replace this heading and all placeholder
> text below with content specific to your skill.

## Quickstart

```bash
# 1. Install test dependencies (first time only)
pip install -r tests/requirements.txt

# 2. Run the self-test suite
python -m pytest tests/ -v

# 3. Invoke the skill from Claude Code
# (skills are loaded automatically from ~/.claude/skills/<skill-name>/)
```

## Design

<!-- Explain the core design of this skill:
     - What problem it solves
     - How it works (components, data flow)
     - Key design decisions and why you made them
     - What is done in code vs. left to LLM inference (see CLAUDE.md dev principles)
-->

TODO: describe design here.

## Known limitations

<!-- List things this skill does NOT handle, known edge cases, platform restrictions,
     and any security / privacy caveats. Be honest — this section exists so users
     don't hit surprises in production.
-->

TODO: list known limitations here.

## Conventions

This skill follows the Trapezia baseline conventions in `conventions/`. See:

- `conventions/git.md` — commit message format, remote-sync flow
- `conventions/python.md` — docstrings, CLI style, anti-patterns
- `conventions/testing.md` — TDD discipline, coverage targets

## Conformance

This skill targets the [Trapezia Disciplines Conformance Standard](
https://github.com/OrionAIDev/trapezia-lab/blob/main/docs/superpowers/specs/2026-05-31-trapezia-disciplines-conformance-standard-design.md).
The `tests/test_structure.py` self-test calls `trapezia-skill-validator` and asserts
the skill is green at its tier. Run `python -m pytest tests/ -v` to verify.
