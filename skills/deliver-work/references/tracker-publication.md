# Tracker Publication

Publish Specifications and Tickets through the Work tracker configuration
written by `setup-project-steering` in `.steering.json` under `workTracker`.

## Required mappings

Use the configured fields; do not hardcode a vendor:

- **status** — Specification and Ticket progress, including what counts as
  approved
- **role** — agent-ready versus human-ready Tickets
- **hierarchy** — Specification to child Tickets; optional project/epic or
  initiative grouping
- **blocker** — blocking relationships between Tickets
- **comment/activity** — shaping notes and gate outcomes

## Preference order

1. Native tracker parent/child and blocker relationships for the configured
   kind (Linear, GitHub, GitLab, Jira, local Markdown, or custom workflow).
2. Explicit metadata fallback described by the mapping fields when native
   support is absent or incomplete.

## Tracker-agnostic outcomes

Across Linear, GitHub, GitLab, Jira, local Markdown, and custom workflows, the
lifecycle outcomes are equivalent:

- one canonical Specification record
- approved Tickets with roles and blockers
- hierarchy recommendation applied (after confirmation when ambiguous)
- resume state detectable from status/role mappings

Only the storage shape changes with `workTracker.kind`.
