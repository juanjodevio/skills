---
name: product-steering
description: Orchestrate product steering for a repository. Use this skill whenever the user asks to create, update, audit, align, or maintain PRODUCT.md, STRUCTURE.md, TECH.md, DESIGN.md, ROADMAP.md, docs/adr, or AGENTS.md; when they mention product steering, repo memory, durable project truth, ADRs, roadmap drift, agent instructions, or documentation that should guide future coding agents; or when a change affects product intent, technical direction, design direction, package manager, roadmap, or agent behavior.
---

# Product Steering

Coordinate the product-steering skill suite. The goal is to keep durable project truth accurate, discoverable, and useful for both humans and coding agents without duplicating the same facts across files.

## Steering Artifacts

The canonical artifacts are:

- `docs/PRODUCT.md`
- `docs/STRUCTURE.md`
- `docs/TECH.md`
- `docs/DESIGN.md`
- `docs/ROADMAP.md`
- `docs/adr/`
- root `AGENTS.md`

`AGENTS.md` should orient agents and point to the docs. Durable truth belongs in the focused docs or ADRs.

## First Pass

Start by inspecting the repository context that is relevant to the request:

- current steering docs, if present
- root `AGENTS.md`, if present
- file and directory structure
- package/tooling files such as `package.json`, lockfiles, `pyproject.toml`, `Cargo.toml`, `go.mod`, or CI config
- recent commits when they help explain drift or decisions
- `docs/adr/` and any ADR index

Do not infer product intent from file names alone. Treat code, config, and docs as evidence; treat user goals, user value, roadmap priority, and product scope as intent that may need confirmation.

## Route The Work

Classify the request and use the focused skill that owns the artifact:

- Product purpose, users, scope, workflows, or success criteria: use `steer-product`.
- Repo map, boundaries, ownership, or where files belong: use `steer-structure`.
- Stack, runtime, package manager, commands, dependencies, integrations, or constraints: use `steer-tech`.
- Design direction, UI context, or Google Stitch-compatible `docs/DESIGN.md`: use `steer-design`.
- Now/next/later sequencing, non-goals, risks, or dependencies: use `steer-roadmap`.
- Durable product, technical, design, or roadmap decisions that shape implementation: use `steer-adr`.
- Root agent instructions or cross-doc pointers: use `steer-agents`.

If a request spans multiple artifacts, handle them in dependency order: product intent, technical/design decisions, roadmap sequencing, repo structure, ADRs, then `AGENTS.md` pointers.

## Ask Rather Than Invent

Use `AskQuestionTool` where possible for bounded choices, approvals, and missing intent. Good structured-question moments include:

- choosing whether a change should be recorded as an ADR
- selecting between plausible product scopes
- confirming roadmap priority
- deciding whether to update docs or only report drift
- choosing whether a generated `DESIGN.md` link should be a symlink or copy

Ask in plain text when the clarification is open-ended or the tool is unavailable. If the user is not available and the work can still proceed, record uncertainty in an `Assumptions` or `Unknowns` section instead of pretending to know.

## Bootstrap Workflow

When a repo has no steering system:

1. Inspect the repo and identify facts that can be discovered safely.
2. Use `AskQuestionTool` for missing high-impact intent if the user has not provided it.
3. Draft balanced first versions of the steering docs with explicit assumptions and unknowns.
4. Initialize or propose `docs/adr/` using `steer-adr`.
5. Create or update root `AGENTS.md` using `steer-agents`.
6. Summarize what was created, what is still unknown, and what should be reviewed by a human.

## Drift Review Workflow

For drift reviews, compare docs, code, config, ADRs, roadmap, and `AGENTS.md`.

When doing a full drift review, read `references/drift-review-checklist.md`.

Report:

- contradictions
- stale commands or package-manager claims
- missing ADRs for durable decisions
- duplicated truth across files
- broken local links
- docs that lack assumptions, unknowns, or last-reviewed metadata

When fixes require intent, ask before editing. When fixes are mechanical, such as correcting a broken local link, explain the change and proceed if the user asked for updates.

## Output Style

End with a concise summary:

- artifacts created or updated
- ADRs created, proposed, or intentionally skipped
- questions asked or assumptions recorded
- follow-up checks the user should review

Keep summaries specific and grounded in file paths.
