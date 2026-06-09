---
name: skill-template
description: >-
  Skeleton for a new Trapezia skill. Use when starting a new first-party
  skill that must conform to the Trapezia disciplines conformance standard.
  Provides the required directory layout, stub artifacts, self-tests, and
  cross-platform hooks out of the box.
---

# skill-template

This is a **clone-source skeleton**. You should not load it as a Claude Code skill
directly. Instantiate it with:

```bash
gh repo create my-new-skill --template OrionAIDev/skill-template --clone
cd my-new-skill
```

Or, without the GitHub CLI:

```bash
cp -r /path/to/skill-template my-new-skill
cd my-new-skill
git init && git add . && git commit -m "chore: instantiate from skill-template"
```

## After instantiation — required renames

1. **Rename the directory** to your skill's name (e.g., `mv skill-template my-new-skill`).
2. **Update `SKILL.md` frontmatter:**
   - `name:` must equal the directory name exactly (the `frontmatter.name` check enforces this).
   - `description:` must be 40–500 characters and contain a "Use when …" trigger phrase
     describing when Claude should invoke your skill.
3. **Update `README.md`** with your skill's quickstart, design notes, and known limitations.
4. **Update `CHANGELOG.md`** — add a `## [Unreleased]` entry describing what this skill does.
5. **Update `.trapezia-skill.toml`** — set `sensitive = true` if your skill handles personal,
   medical, financial, or credential data.
6. **Delete `scripts/.keep`** and replace with real scripts (T1/T2 skills) or delete the
   `scripts/` directory entirely if this is a T0 (prompt-only) skill.
7. **Update `hooks/session-start`** and `hooks/session-start.cmd` with any setup your skill
   needs on session start (source a venv, export env vars, etc.).
8. **Update `NOTICE.md`** if you fork or vendor any third-party content. Delete it if you
   do not.

## Self-test

After renaming, verify the template audits green:

```bash
pip install -r tests/requirements.txt
python -m pytest tests/ -v
```

All tests must pass. The `test_structure.py` test imports `trapezia-skill-validator`
and calls `run_audit()` against this directory — zero FAILs is the gate.

## Conventions

See `conventions/` for the baseline git, Python, and testing conventions that all
Trapezia skills follow.
