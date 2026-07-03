---
name: steer-structure
description: Maintain docs/STRUCTURE.md as the repository map and ownership guide. Use this skill whenever the user asks where files should live, how a repo is organized, how modules or packages relate, what boundaries agents should respect, or when bootstrapping or refreshing repo structure documentation for future coding agents.
---

# Steer Structure

Maintain `docs/STRUCTURE.md`. This file helps humans and agents place work in the right part of the repository and understand the boundaries between areas.

## Ownership

Own repository structure truth:

- directory map
- package, module, or app boundaries
- ownership and responsibility boundaries
- where new code, tests, docs, assets, scripts, and generated files belong
- naming and placement conventions
- assumptions and unknowns about structure
- last-reviewed metadata

Do not duplicate detailed stack commands from `docs/TECH.md` or product scope from `docs/PRODUCT.md`.

## Workflow

1. Read `docs/STRUCTURE.md` if it exists.
2. Inspect the repository tree, package/workspace files, tests, docs, and generated-file patterns.
3. Identify real structure before proposing new structure.
4. Use `AskQuestionTool` where possible for bounded choices, such as where a new domain should live or whether a boundary is intentional.
5. Ask in plain text when ownership or architecture intent is unclear.
6. Update only `docs/STRUCTURE.md`.
7. Record unknown ownership or boundary questions explicitly.
8. Return cross-doc follow-ups if structure implies tech, product, roadmap, ADR, or `AGENTS.md` updates.

## Suggested Structure

When creating `docs/STRUCTURE.md` from scratch or normalizing a sparse file, read `references/structure-template.md`.

Use this structure unless the repo already has a strong convention:

- Repository Overview
- Directory Map
- Ownership Boundaries
- Placement Rules
- Tests And Fixtures
- Generated Files And Artifacts
- Assumptions
- Unknowns
- Last Reviewed

For the directory map, prefer short explanations over exhaustive listings. Mention files and directories that affect where agents should work.

## Self-Check

Before finishing, check that:

- documented directories exist or are marked as planned
- ownership and placement rules are not contradicted by the current repo
- generated files are not confused with source files
- technical command details remain in `docs/TECH.md`
- local links are valid where practical
- `Last Reviewed` is present or intentionally preserved
