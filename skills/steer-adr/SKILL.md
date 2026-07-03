---
name: steer-adr
description: Manage docs/adr as the repository's decision record system. Use this skill whenever the user mentions ADRs, architecture decisions, MADR, adr-tools, superseding decisions, decision logs, durable product/technical/design/roadmap choices, package-manager or framework changes, or wants future agents to understand why an implementation-shaping decision was made.
---

# Steer ADR

Manage `docs/adr` as a lightweight decision record system. ADRs should explain durable decisions that shape implementation direction. They are not a changelog for every task.

## Ownership

Own decision records:

- ADR initialization under `docs/adr`
- ADR naming and numbering
- compact MADR content
- ADR index or generated table of contents
- supersession and links between decisions
- guidance on whether a change deserves an ADR

## When To Create An ADR

Create or propose an ADR when a decision materially affects future implementation, such as:

- package manager, runtime, framework, database, or hosting choice
- durable product scope decision that constrains implementation
- design-system or canonical design-context decision
- roadmap sequencing decision that changes technical direction
- security, privacy, compliance, or data-retention posture
- public API, integration, or contract decision
- repository-wide agent behavior or workflow policy

Do not create an ADR for routine implementation tasks, small refactors, or temporary experiments unless the user explicitly asks.

## Workflow

1. Read existing `docs/adr` content and any ADR index.
2. Check whether `adr-tools` is available if creating files.
3. Use `AskQuestionTool` where possible to confirm status, decision scope, considered options, supersession, and whether an ambiguous change is ADR-worthy.
4. Initialize with `adr init docs/adr` when appropriate and available.
5. Create numbered dashed filenames, preferably through `adr new`.
6. Use compact MADR sections.
7. Treat accepted ADRs as immutable in practice. If direction changes, create a new ADR that supersedes the old one.
8. Maintain or regenerate the ADR index or table of contents.
9. Report any fallback if `adr-tools` is unavailable.

## Compact MADR Sections

When creating an ADR manually or checking adr-tools output against the suite convention, read `references/compact-madr-template.md`.

Use this shape unless the repo already has a compatible template:

- Status
- Date
- Context And Problem Statement
- Decision Drivers
- Considered Options
- Decision Outcome
- Consequences
- Confirmation
- More Information

Keep the selected option clear and name the trade-offs. Prefer a short but complete record over a large template nobody will maintain.

## Fallback Without adr-tools

If `adr-tools` is unavailable:

1. Tell the user that the tool is unavailable.
2. Create or update Markdown manually only if the user asked for implementation.
3. Preserve adr-tools-compatible naming where possible.
4. Maintain `docs/adr/index.md` manually.
5. Record that manual maintenance was used.

## Self-Check

Before finishing, check that:

- each ADR captures one decision
- status is clear
- supersession is explicit when replacing a prior decision
- the ADR does not rewrite accepted history
- options are comparable at the same level of abstraction
- consequences include meaningful trade-offs
- the index or table of contents can lead a reader to the decision
