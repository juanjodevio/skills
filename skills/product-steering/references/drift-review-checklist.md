# Drift Review Checklist

Use this checklist when reviewing steering drift across docs, code, config, ADRs, and agent instructions.

## Commands And Tooling

- Do `docs/TECH.md`, manifests, lockfiles, CI, and `AGENTS.md` agree on package manager?
- Are install, lint, test, typecheck, build, and validation commands current?
- Are unverified commands marked as unverified?

## Product And Roadmap

- Does `docs/PRODUCT.md` describe scope that conflicts with `docs/ROADMAP.md`?
- Are roadmap priorities explicit enough to guide future agents?
- Are non-goals visible?

## Structure

- Does `docs/STRUCTURE.md` match the current repo tree?
- Are generated files identified?
- Are placement rules contradicted by recent changes?

## Design

- Is `docs/DESIGN.md` canonical?
- Are any copied or symlinked `DESIGN.md` files explained?
- Does design direction conflict with product or roadmap docs?

## ADRs

- Are durable implementation-shaping decisions recorded?
- Are accepted ADRs being rewritten instead of superseded?
- Is package manager, runtime, framework, database, or deployment direction ADR-worthy?
- Is the ADR index or table of contents current?
- Does the ADR index include `ADR`, `Status`, and `Decision` columns, with status values matching each ADR file?
- Are ADRs with missing status recorded as `Unknown` in the index and flagged as follow-ups?

## AGENTS.md

- Is root `AGENTS.md` compact and pointer-based?
- Does it duplicate durable truth that belongs in docs?
- Does it point to every steering artifact that exists?

## Unknowns

- Are missing product, roadmap, technical, or design decisions recorded as unknowns instead of fabricated facts?
- Should `AskQuestionTool` be used to resolve any bounded choices?
