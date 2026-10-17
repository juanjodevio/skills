# Project Roadmap

## Roadmap Summary

Post-rebuild horizon: keep the cross-domain Project steering suite coherent,
installable, and usable. Sequencing below is provisional where noted; Ticket
detail stays in Linear.

## Now

- Finish Project steering bootstrap for this repository (configuration + active
  Steering artifacts)
- Keep inventory validation green and obsolete public names absent from the
  installable surface

## Next

- _(Assumption)_ Exercise the suite on real consumer Projects; fold editorial
  lessons back into skills and docs without adding a scenario catalog

## Later

- _(Assumption)_ Optional CI host for inventory checks once a Python/runtime
  pin is chosen
- _(Assumption)_ Revisit whether Design becomes an active truth kind if this
  Project gains a UI or visual surface

## Non-Goals

- Superpowers dependency
- Vendored upstream lifecycle skills
- Focused/partial suite install
- Committed skill-behavior scenario catalog
- `docs/DESIGN.md` for this pack (Design inactive in `.steering.json`)

## Risks And Dependencies

- Consumer agents must resolve required upstream skill names; missing names
  block setup and `deliver-work` (see `docs/installation.md`)
- Linear MCP availability affects Work tracker operations for this repo

## Decision Points

- Pin Python / CI matrix before treating maintainer automation as settled
  technology (related: `docs/TECH.md` Unknowns)
- Activate Design only if a visual product surface appears

## Assumptions

- Now/Next/Later after bootstrap are inferred from ADR-0001 consequences and
  Intent success signals, not a separate maintainer priority ranking

## Unknowns

- Explicit priority ranking beyond post-rebuild stabilization
- Whether packaging CI is desired in this horizon

## Last Reviewed

2026-10-17 by setup-project-steering bootstrap
