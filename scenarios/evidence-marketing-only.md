# Evidence: marketing-only Project

## Request

Update Intent for a marketing program using only marketing evidence (briefs,
channels, attribution definitions, budgets, performance metrics).

## Fixture

- `.steering.json` maps `intent` to `docs/INTENT.md`
- evidence adapters: `marketing` only
- repository contains campaign briefs and performance snapshots
- no application source tree or data warehouse schemas

## Evidence profiles

- marketing

## Expected outcome

- Inspects marketing evidence only
- Treats metrics and prior copy as evidence, not Intent
- Asks for material Intent when strategy cannot be established from briefs alone
- Does not invent software or data platform direction
