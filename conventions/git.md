# Git conventions

## Commit message format

```
<type>: <short description>
```

Where `<type>` is one of: `feat`, `fix`, `chore`, `docs`, `test`, `refactor`, `release`.

Examples:
- `feat: add session-start hook`
- `fix: handle missing SKILL.md gracefully`
- `docs: clarify limitations in README`
- `release: v0.2.0`

## When git is required

All Trapezia skills that ship executable code (T1/T2) must be in a git repository
with a configured remote under `OrionAIDev/*` (or the Trapezia org once migration
is complete). Prompt-only (T0) skills may omit git if they are single-file and
not intended for long-term maintenance — but git is strongly recommended.

## Remote-sync policy

Push after every meaningful completed unit of work. Branch strategy:
- **Trunk-based** (commit to main): preferred for small skills and solo development.
- **Feature branches**: preferred when multiple people or subagents are contributing.

## Pre-commit hooks (optional forward defense)

The `tools/git-hooks/` directory (from `trapezia-salus`) contains a pre-commit hook
that scans staged files for sensitive-data patterns before every commit. To install:

```bash
git config core.hooksPath tools/git-hooks
```

This step is optional but strongly recommended for `+S` skills. The
`trapezia-skill-audit` auditor will check whether it is installed.
See §10.2 of the conformance standard spec for details.
