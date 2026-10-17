# Migration: obsolete public names absent

## Request

After installing the full Project steering suite, confirm the legacy
product-oriented public skill names are gone and documentation names replacements.

## Fixture

- installed suite inventory from `steering-suite.json`
- published `docs/migration.md` and `docs/catalog.md`
- no compatibility aliases configured

## Evidence profiles

- software
- data
- marketing

## Expected outcome

- Obsolete names absent from discoverable modules: `product-steering`,
  `steer-product`, `steer-tech`, `steer-adr`, `steer-agents`
- Migration guide maps each removed name to its replacement
- Catalog lists only the approved Project steering suite
- No alias keeps an obsolete public name installable
