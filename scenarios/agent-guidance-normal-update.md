# Scenario: Agent guidance normal update

## Request

Use `steer-project` to refresh agent guidance after Intent and technology paths
were remapped, so agents find the configured Steering artifacts first.

## Fixture

A mixed Project with:

- `.steering.json` mapping `agent-guidance` to `docs/AGENT_ORIENTATION.md` and
  `intent` to `docs/STRATEGY.md`
- a sparse or stale agent-guidance artifact at the mapped path that still points
  at obsolete `PRODUCT.md` and `TECH.md` basenames
- software docs and package manifests with stable commands owned by technology
- data contracts that do not change agent navigation
- a marketing brief that does not change agent navigation

## Evidence profiles

software, data, marketing

## Expected outcome

- Ownership is classified as agent guidance and routed through
  `steer-agent-guidance`.
- The configured artifact path is used; `AGENTS.md` is not assumed.
- `writing-for-agents` is invoked for writing discipline rather than reproduced.
- Guidance pointers identify canonical Steering artifacts and `.steering.json`
  without copying their content.
- Only the agent-guidance Steering artifact is updated.
- Commands and Intent remain owned by their focused artifacts; related work may
  note them without editing them in this invocation.
- Update proceeds because navigation materially changed.
