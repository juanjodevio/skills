# Scenario: Multi-artifact ownership routing

## Request

Use `steer-project` to update "the PRODUCT.md vibes, the TECH layout notes, and
the AGENTS roadmap blurbs" after a maintainer describes purpose, repository
placement rules, and agent navigation needs in plain language.

## Fixture

A Project with:

- `.steering.json` mapping `intent` to `docs/STRATEGY.md`, `structure` to
  `docs/REPO_MAP.md`, and `agent-guidance` to `docs/AGENT_ORIENTATION.md`
- stale files named `PRODUCT.md`, `TECH.md`, and `AGENTS.md` that are not the
  configured Steering artifacts
- confirmed maintainer intent for purpose, placement policy, and agent pointers
- no technology or Roadmap change requested

## Evidence profiles

software

## Expected outcome

- Ownership is classified by durable truth (Intent, Structure, agent guidance),
  not by the filenames spoken in the request.
- Work routes to `steer-intent`, `steer-structure`, and `steer-agent-guidance`
  respectively; technology and Roadmap adapters are not invoked as owners.
- Configured artifact paths are used; unmapped familiar basenames are ignored
  as ownership signals.
- Unrelated artifacts (technology, design, roadmap, decisions) may remain
  untouched and are not forced into the run.
- Focused modules remain sole owners of their truth types; the orchestrator
  does not write Intent, Structure, or guidance content itself.
