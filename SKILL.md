---
name: trapezia-feedback-skill
description: >-
  Cross-product user feedback channel for Trapezia bots — file bugs and
  feature requests from Discord with mandatory PII scrubbing and explicit
  user confirmation before each report is posted to the public
  OrionAIDev/trapezia-feedback repo. Use when a Discord user expresses
  bug or feature-request intent ("there's a bug", "I wish it could…")
  and the bot should offer to file it. Cross-product — per-product
  config supplies the product label and additional scrubber categories.
---

# trapezia-feedback-skill

Cross-product user feedback channel for Trapezia bots. Lets any Discord user (family member, customer, pilot participant) file a structured bug report or feature request that lands as a GitHub issue on the public `OrionAIDev/trapezia-feedback` repo — with PII and product-specific sensitive content scrubbed before posting, and explicit user confirmation as the safety gate.

**Design spec:** see `2026-06-08-trapezia-feedback-skill-design.md` in `OrionAIDev/orion-cognition-labs-workspace`. This README is the operator quickstart; the spec is the contract.

## Quickstart

```bash
# Install test dependencies (first time only)
pip install -r tests/requirements.txt

# Run the self-test suite (mocks the LLM + GitHub API at the boundaries)
python -m pytest tests/ -v
```

## How it works (one-paragraph version)

When a Discord user expresses bug or feature-request intent, the consuming bot's LLM detects it and calls `feedback_draft.py` with the user's text + envelope (display name, product identifier, channel). The skill drafts a structured report, sends it through a clean-context LLM scrubber that redacts the configured categories (baseline PII + any product-specific categories), and shows the user a preview with an explicit "this will be PUBLIC on GitHub — confirm?" warning. On `file`, `feedback_file.py` posts to `OrionAIDev/trapezia-feedback` via a write-only PAT scoped to that one repo. On edit, the skill re-drafts and **re-scrubs** before showing the new preview — every preview is freshly scrubbed.

## Status

- **Repo created:** 2026-06-09
- **Initial release:** TBD (bootstrap in progress)
- **Spec:** `OrionAIDev/orion-cognition-labs-workspace/documents/Trapezia/specs/2026-06-08-trapezia-feedback-skill-design.md`
- **Companion repo:** `OrionAIDev/trapezia-feedback` (issues only — where the reports land)
