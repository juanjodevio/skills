# Evidence: data-only Project

## Request

Update Intent for a data platform Project using only data evidence (pipelines,
schemas, catalogs, quality checks). Do not treat observed runs as desired Intent.

## Fixture

- `.steering.json` maps `intent` to `docs/INTENT.md`
- evidence adapters: `data` only
- repository contains pipeline defs, schema docs, and recent run history
- no software product code or marketing campaign assets

## Evidence profiles

- data

## Expected outcome

- Inspects data evidence only; does not invent software or marketing Intent
- Labels pipeline/run history as evidence, not Intent
- Updates or questions Intent without silently promoting observed state to strategy
- Reports related technology/structure work when ownership is not Intent
