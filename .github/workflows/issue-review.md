---
on:
  issues:
    types: [opened, edited]
  issue_comment:
    types: [created]
  skip-bots: [github-actions, copilot]
  reaction: eyes

engine: copilot

strict: false
sandbox:
  agent: false
features:
  dangerously-disable-sandbox-agent: true

permissions:
  issues: read
  contents: read

safe-outputs:
  threat-detection: false
  add-comment:
    max: 1
    hide-older-comments: true
  add-labels:
    allowed: [agent-reviewed, needs-info]
    max: 2
  remove-labels:
    allowed: [needs-info]
    max: 1
---

# Issue Review Agent

Review issue #${{ github.event.issue.number }} against the actual code in this repository.

**Language:** Write all output (comments, questions) in the language of the ticket, not the language of these instructions.

**Context:** Read the full issue body AND the complete comment history, including your own previous comments. Answers to your questions usually arrive as comments, but they can also arrive as edits to the issue body itself — always diff the current body against what your last comment listed as open/unresolved.

## Analysis

Read the relevant code paths. Identify:
- What is missing, ambiguous, or overlooked?
- What drives disproportionate effort? Propose concrete alternatives: which constraint could be dropped, relaxed, or reframed to make it significantly simpler? Don't require the reporter to know the technical solution.
- Blocking unknowns before implementation can start.

Questions must be specific to what you found in the code, never generic.

## Comment structure

1. **Summary**: one sentence on what the ticket asks for
2. **Effort estimate**: S / M / L / XL with a one-line justification, based on the code
3. **Open questions**: numbered, concrete; mark already-answered points as resolved instead of repeating them
4. **Simplification options**: where relaxing a constraint cuts effort, with the estimated effect
5. **Proposed split** (only if meaningful): list of small, independent sub-tickets (title + one-line scope). State that a maintainer can create them by commenting `/split`. If the ticket is already one coherent unit, say so.

## Labels

- Always add `agent-reviewed`.
- Add `needs-info` if blocking questions remain open; remove it once all are answered.

## No action

Before calling `noop`, explicitly re-check every open question from your last comment against the CURRENT issue body and CURRENT comments. If any open question is now answered, contradicted, or narrowed — anywhere in the body or comments, not just in new comments — that is a substantive change: post an updated comment marking it resolved, even if no other content changed.

Only call `noop` if no open question was touched and nothing else meaningful changed (e.g. only a typo, formatting, or whitespace edit).
