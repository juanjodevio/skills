# Decision Record Template

Use the Project's established ADR conventions when they already provide numbered
files, explicit status, a status-bearing index, and supersession. Prefer
`domain-modeling` ADR shape for body length. This suite requires explicit status
and a status-bearing index even when the body stays short.

## Short Record

```markdown
---
status: accepted
date: YYYY-MM-DD
---

# {Short title of the decision}

{1-3 sentences: context, decision, and why.}
```

## Optional Sections

Include only when useful to preserve the trade-off:

- **Considered Options**: rejected alternatives worth remembering
- **Consequences**: non-obvious downstream effects

## Status-Bearing Index

Keep an index such as `index.md` or `README.md` beside the records:

| ADR | Status | Decision |
| --- | --- | --- |
| [ADR-0001](./0001-example.md) | Accepted | Example decision |

Update the index in the same change as the ADR it describes. Status in the index
must match the status declared in the ADR file. If status is missing, record
`Unknown` and flag follow-up rather than inventing a value.

## Supersession

When direction changes, leave the accepted record intact. Create a new numbered
ADR that supersedes it, set the new status (usually `accepted`), and update the
prior record's status to `superseded by ADR-NNNN`. Refresh both index rows in
the same change.

## Numbering

Scan the configured decisions directory for the highest existing number and
increment by one. Use zero-padded filenames such as `0002-slug.md`.
