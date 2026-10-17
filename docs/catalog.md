# Project Steering Catalog

Discoverable modules in this suite. Install the full suite; focused standalone
installation is unsupported. See [installation](installation.md).

## Entrypoint and setup

| Skill | Role |
| --- | --- |
| `steer-project` | Default Project steering entrypoint. Runs the shared Steering workflow, routes ownership to focused adapters, orders multi-artifact updates, and reports related work. |
| `setup-project-steering` | Suite setup entrypoint. Confirms Matt prerequisites, artifact mappings, evidence adapters, and Work tracker configuration, then bootstraps active Steering artifacts through `steer-project`. |

## Focused truth adapters

Each adapter owns one Steering artifact kind and delegates the shared process to
`steer-project`.

| Skill | Owns |
| --- | --- |
| `steer-intent` | Project Intent (purpose, audience, scope, success). |
| `steer-technology` | Technical direction (stack, commands, platforms, constraints). |
| `steer-design` | Design direction (atmosphere, visual system, interaction, accessibility). Credits the `design-md` pattern; Stitch is not required. See [design-md](design-md.md). |
| `steer-roadmap` | Delivery sequence (now/next/later, non-goals, risks). |
| `steer-structure` | Repository structure (layout, boundaries, ownership). |
| `steer-decisions` | Decision records / ADRs (eligible durable decisions and supersession). |
| `steer-agent-guidance` | Compact agent guidance (`AGENTS.md` / vendor equivalents) with pointers into Steering artifacts. |

## Default Work lifecycle

| Skill | Role |
| --- | --- |
| `deliver-work` | Default Work lifecycle coordinator: unresolved intent → grill → Specification → Tickets → Frontier execution → retrospective. Reuses Matt skills by name. |

`deliver-work` is the default path for carrying settled intent into planned work.
It is not a Steering artifact adapter.

## Situational skills

Situational skills are invoked when a specific need arises. They are **not**
required stages of the Work lifecycle.

Examples used by this suite (by name only; not vendored here):

- `grill-with-docs`, `domain-modeling` — sharpen intent and settle Domain language
- `to-spec`, `to-tickets` — Specification and Ticket shaping
- `implement-spec`, `retro` — execution and retrospective learning
- `writing-for-agents` — agent-facing prose quality for guidance artifacts
- `setup-matt-pocock-skills` — tracker, triage, Domain docs, and ADR prerequisites

Steering adapters (`steer-intent`, `steer-design`, and the other focused truth
adapters) are also Situational relative to the Work lifecycle: invoke them when
durable Project truth needs updating, not as mandatory lifecycle stages.

## Related docs

- [Installation and discoverability](installation.md)
- [Work tracker guidance](work-tracker.md)
- [Migration from the legacy suite](migration.md)
- [Domain language](../GLOSSARY.md)
- [Architecture ADR](adr/0001-rebuild-as-cross-domain-project-steering-suite.md)
