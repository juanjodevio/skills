# Migration from the legacy product-steering suite

The legacy product-oriented interface has been removed. There are
**no compatibility aliases** for obsolete public names. Install the full Project
steering suite and update prompts, hooks, and docs that still reference old
skill names.

## Removed public names → replacements

| Removed name | Replacement | Notes |
| --- | --- | --- |
| `product-steering` | `steer-project` (steering) or `setup-project-steering` (bootstrap) | Default entrypoint is now `steer-project`. First-time configuration uses `setup-project-steering`. Work delivery uses `deliver-work`, not the old router. |
| `steer-product` | `steer-intent` | Intent replaces product-purpose docs. Artifact path is configured (often Intent / `PRODUCT.md` legacy locations via mapping). |
| `steer-tech` | `steer-technology` | Broader technology adapter; not package-manager-only. |
| `steer-adr` | `steer-decisions` | Decision eligibility and supersession live in `steer-decisions`. |
| `steer-agents` | `steer-agent-guidance` | Compact agent guidance with pointers; not a Work lifecycle stage. |

Names that already match the approved suite keep their public identity:

- `steer-design` — same name; semantics now credit `design-md` and do not require Stitch
- `steer-roadmap` — same name; focused Roadmap adapter on the shared workflow
- `steer-structure` — same name; focused Structure adapter on the shared workflow

## What was removed without a 1:1 skill rename

- The legacy orchestrator’s product-only framing → cross-domain Project steering
  via evidence profiles (software, data, marketing).
- Focused standalone install recommendations → full-suite install only.
- Any alias that would keep `product-steering`, `steer-product`, `steer-tech`,
  `steer-adr`, or `steer-agents` discoverable after install.

## Suggested cutover

1. Remove old skill installs for obsolete names.
2. Install the full suite per [installation](installation.md).
3. Run `setup-project-steering` to confirm artifact mappings and Work tracker
   configuration (preserve compatible existing paths).
4. Replace prompt text:
   - “use product-steering” → “use steer-project” or “use deliver-work”
   - “use steer-product” → “use steer-intent”
   - “use steer-tech” → “use steer-technology”
   - “use steer-adr” → “use steer-decisions”
   - “use steer-agents” → “use steer-agent-guidance”
5. Point humans and agents at [catalog](catalog.md) and [GLOSSARY](../GLOSSARY.md).

## Architecture

See [ADR-0001](adr/0001-rebuild-as-cross-domain-project-steering-suite.md) for
the accepted rebuild decision and consequences.
