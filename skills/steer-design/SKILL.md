---
name: steer-design
description: Maintain docs/DESIGN.md as the canonical design context, especially for Google Stitch-compatible DESIGN.md workflows. Use this skill whenever the user asks about design direction, UI principles, visual system, Stitch design context, accessibility, interaction patterns, or whether DESIGN.md should be symlinked into another directory.
---

# Steer Design

Maintain canonical `docs/DESIGN.md`. This file captures durable design context for UI and product experience work.

## Ownership

Own design truth:

- design context and status
- UI principles
- visual system guidance
- interaction patterns
- accessibility expectations
- content style notes when they affect UI
- Google Stitch-compatible `DESIGN.md` structure
- assumptions and unknowns
- last-reviewed metadata

Do not duplicate roadmap sequencing, technical commands, or product scope beyond short links to the canonical docs.

## Google Stitch Compatibility

Keep `docs/DESIGN.md` canonical. If another tool or subproject needs a `DESIGN.md` at a different path, prefer a symlink to `docs/DESIGN.md`. Use a copy only when symlinks are not practical in that environment, and record why.

When creating `docs/DESIGN.md` from scratch or normalizing a sparse file, read `references/design-template.md`.

When no stronger project template exists, use a Stitch-compatible shape:

- Title
- Status
- Context
- Proposed Solution
- Consequences
- Assumptions
- Unknowns
- Last Reviewed

Preserve any additional Stitch-required sections already present in the repository.

## Workflow

1. Read `docs/DESIGN.md` if it exists.
2. Inspect UI code, screenshots, design docs, style tokens, component libraries, and product docs when relevant.
3. Separate visible implementation facts from design intent.
4. Use `AskQuestionTool` where possible for bounded design choices, such as status, visual direction, symlink vs copy, or accessibility priority.
5. Ask in plain text for open-ended design rationale.
6. Update only `docs/DESIGN.md` unless the user explicitly asks for symlink/copy updates.
7. If the change establishes a durable design direction that affects implementation, propose or create an ADR through `steer-adr`.
8. Return cross-doc follow-ups for product, roadmap, tech, ADR, or `AGENTS.md`.

## Self-Check

Before finishing, check that:

- `docs/DESIGN.md` remains the canonical path
- symlink or copy guidance is explicit when other locations need `DESIGN.md`
- design intent is not invented from UI code alone
- accessibility expectations are stated or listed as unknown
- durable design decisions were routed to ADR consideration
- `Last Reviewed` is present or intentionally preserved
