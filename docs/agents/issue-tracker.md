# Issue tracker: Linear

Issues and specs for this repo live in Linear. Agents read and write them through the Linear MCP only (`plugin-linear-linear`).

## Defaults

- **Team**: P&P (`PAN`)
- **Do not** use GitHub Issues or local `.scratch/` files as the tracker for this repo

## Conventions

- **Create / update an issue**: `save_issue` (set `team` to `P&P` or `PAN` when creating)
- **Read an issue**: `get_issue` with the identifier (e.g. `PAN-123`)
- **List issues**: `list_issues` scoped to team `P&P` / `PAN`
- **Comment**: `save_comment` on the issue identifier
- **Labels**: `save_issue_label` / `list_issue_labels`; apply labels when creating or updating via `save_issue`
- Prefer issue identifiers (e.g. `PAN-123`) in chat and commits

## When a skill says "publish to the issue tracker"

Create a Linear issue on team **P&P** via `save_issue`.

## When a skill says "fetch the relevant ticket"

Read it with `get_issue`.
