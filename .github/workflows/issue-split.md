---
on:
  slash_command:
    name: split
    events: [issue_comment]

engine: copilot

permissions:
  issues: read
  contents: read

safe-outputs:
  threat-detection: false
  create-issue:
    max: 5
    deduplicate-by-title: true
  link-sub-issue:
    max: 5
---

# Issue Split Agent

Create sub-issues for issue #${{ github.event.issue.number }} based on the most recent "Proposed split" in the review agent's comment, adjusted for any later discussion in the thread.

- Write titles and bodies in the ticket's language.
- Each sub-issue: clear scope, acceptance criteria, reference to the parent.
- Link every created issue to the parent as a sub-issue.
- If no split proposal exists or the discussion rejected splitting, call `noop` with the reason.
