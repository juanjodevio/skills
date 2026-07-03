---
name: steer-roadmap
description: Maintain docs/ROADMAP.md as the product and delivery sequencing guide. Use this skill whenever the user asks about now/next/later priorities, planned work, non-goals, risks, dependencies, release sequencing, roadmap drift, or how future agents should understand what to build next.
---

# Steer Roadmap

Maintain `docs/ROADMAP.md`. This file captures intended sequencing and makes non-goals visible so agents do not build the wrong thing early.

## Ownership

Own roadmap truth:

- now, next, and later priorities
- explicit non-goals
- risks and dependencies
- decision points
- sequencing rationale
- assumptions and unknowns
- last-reviewed metadata

Do not duplicate product scope from `docs/PRODUCT.md` or technical command details from `docs/TECH.md`.

## Workflow

1. Read `docs/ROADMAP.md` if it exists.
2. Inspect issues, project docs, commits, TODO comments, and product docs when relevant.
3. Treat existing plans as intent only when they are current or confirmed.
4. Use `AskQuestionTool` where possible for bounded priority, sequencing, or scope decisions.
5. Ask in plain text when strategic rationale is missing.
6. Update only `docs/ROADMAP.md`.
7. If the roadmap change locks in a durable direction that affects implementation, propose or create an ADR through `steer-adr`.
8. Return cross-doc follow-ups for product, design, tech, ADR, or `AGENTS.md`.

## Suggested Structure

When creating `docs/ROADMAP.md` from scratch or normalizing a sparse file, read `references/roadmap-template.md`.

Use this structure unless the repo already has a strong convention:

- Roadmap Summary
- Now
- Next
- Later
- Non-Goals
- Risks And Dependencies
- Decision Points
- Assumptions
- Unknowns
- Last Reviewed

Keep roadmap items outcome-oriented. Implementation tasks belong in plans or issues unless they define sequencing.

## Self-Check

Before finishing, check that:

- priorities are explicit and not silently inferred
- non-goals are visible
- roadmap items do not contradict accepted ADRs
- durable roadmap decisions were routed to ADR consideration
- stale items are marked for review instead of quietly removed when intent is unclear
- `Last Reviewed` is present or intentionally preserved
