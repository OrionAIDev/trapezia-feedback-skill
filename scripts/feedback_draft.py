#!/usr/bin/env python3
"""Draft, scrub, preview, and (on confirmation) file a Trapezia feedback report.

STUB — full implementation in progress per
docs/superpowers/specs/2026-06-08-trapezia-feedback-skill-design.md.

Contract (final shape; not yet wired):

    feedback_draft.py
        --action {new,edit,file,cancel}
        --envelope-json '<json with display_name, sender_id, product, channel_id>'
        --state-key '<channel_id+sender_id hash>'
        [--text '<user supplied content>']
        [--report-type {bug,feature}]

Exit codes (per tool_runner convention):
    0  ok                    — printed JSON: preview / filed URL / cancelled
    2  validation_failed     — bad inputs
    3  forbidden             — (reserved; v1 has no per-user gating)
    4  not_found             — state-key has no draft (e.g. on `edit` before `new`)
    6  scrubber_failed       — both primary + fallback scrubber unreachable
    7  github_unreachable    — github API errored; draft preserved
    8  scrubber_rejected     — scrubber said the input was too sensitive to safely strip

The skill's invariants (per spec §4):
    1. Every preview shown to the user has been freshly scrubbed.
    2. The `file` verb operates on the last-shown scrubbed version.
    3. No unscrubbed text leaves the skill's memory.
"""
from __future__ import annotations

import sys


def main() -> int:
    print("trapezia-feedback-skill stub — implementation in progress", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
