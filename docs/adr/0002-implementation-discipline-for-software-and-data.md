---
status: accepted
date: 2026-10-17
---

# Implementation discipline for software and data

Ship **Implementation discipline** as suite guidance for software and data
implementation, not as a new Steering artifact kind and not as marketing-first
doctrine. Adapted from
[andrej-karpathy-skills CLAUDE.md](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md)
(attribution + rewrite; not a vendor copy).

## Decision Outcome

- Seed: `skills/steer-agent-guidance/references/implementation-discipline.md`
- Project path: `docs/agents/implementation-discipline.md`
- Create file and agent-guidance pointer when `evidenceAdapters` includes
  `software` and/or `data`; skip both on marketing-only Projects
- `deliver-work` requires reading that file before `implement-spec` when those
  adapters are active (no per-Ticket domain labels)
- Update only the configured `agent-guidance` path; do not sync sibling root
  files
- When adapters later lose software/data: remove the pointer; leave the file

## Considered Options

- Inline the essay into agent-guidance — rejected (bloats the always-loaded map)
- Suite default for every Project including marketing-only — rejected
- Patch upstream `implement-spec` — rejected (non-vendoring Intent)
- Project-local only — rejected in favor of suite consistency for software/data

## Consequences

- Conditional materialization is gated on existing `evidenceAdapters`, not a
  new domain-specific skill family
- Agents may still skip the spirit of the rules; the suite enforces the read
  hook, not runtime compliance
