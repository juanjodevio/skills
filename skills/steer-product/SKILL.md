---
name: steer-product
description: Maintain docs/PRODUCT.md as the repository's product truth. Use this skill whenever the user asks about product purpose, target users, customer problems, scope, workflows, success criteria, product assumptions, or product documentation; when bootstrapping product steering docs; or when implementation work reveals product intent that future agents need to preserve.
---

# Steer Product

Maintain `docs/PRODUCT.md`. This file explains what the product is, who it serves, what problems it solves, what is in scope, and what good outcomes look like.

## Ownership

Own only product truth:

- target users and stakeholders
- problem and purpose
- in-scope and out-of-scope behavior
- core workflows and user journeys
- success criteria
- product assumptions and unknowns
- last-reviewed metadata

Do not put stack choices, install commands, or repo layout here. Route those to `steer-tech` or `steer-structure`.

## Workflow

1. Read `docs/PRODUCT.md` if it exists.
2. Inspect README, visible app surfaces, product-facing docs, tests, and recent commits only as evidence.
3. Separate observed facts from inferred intent.
4. Use `AskQuestionTool` where possible for bounded missing intent, such as target audience, scope boundary, success metric, or whether a workflow is in scope.
5. Ask in plain text for open-ended product context.
6. Update `docs/PRODUCT.md` using a balanced, scan-friendly structure.
7. Record uncertainty in `Assumptions` or `Unknowns` instead of inventing product truth.
8. Return cross-doc follow-ups if the change also implies roadmap, design, ADR, or agent-instruction updates.

## Suggested Structure

When creating `docs/PRODUCT.md` from scratch or normalizing a sparse file, read `references/product-template.md`.

Use this structure unless the repo already has a strong convention:

- Product Summary
- Target Users
- Problem And Purpose
- Core Workflows
- Scope
- Success Criteria
- Assumptions
- Unknowns
- Last Reviewed

Keep the writing concise enough for an agent to scan, but include enough human context to preserve product intent.

## Self-Check

Before finishing, check that:

- product claims are grounded in user input or explicit repo evidence
- unknown product intent is not presented as fact
- technical details are not duplicated from `docs/TECH.md`
- roadmap sequencing is not duplicated from `docs/ROADMAP.md`
- links are local and valid where practical
- `Last Reviewed` is present or intentionally preserved
