# Scenario: Technology conflicting evidence

## Request

Use `steer-technology` to align Project technology with current repository
evidence.

## Fixture

A Project with `.steering.json` mapping `technology` to `docs/TECH.md` and:

- software manifests and CI claiming npm as the package manager
- data pipeline docs and run constraints requiring a container image built with
  pnpm
- marketing attribution tooling docs that assume yarn workspaces for shared
  campaign packages
- no maintainer confirmation of which package manager is intended

## Evidence profiles

software, data, marketing

## Expected outcome

- Conflicting package-manager evidence is not silently reconciled.
- The invocation asks a material question or records an explicit unknown.
- No settled technology claim is written that chooses one package manager
  without confirmation.
- If a safe provisional update is made, conflicting interpretations remain
  visible under Assumptions or Unknowns.
- Related work may note that software, data, and marketing evidence disagree,
  and may route durable package-manager policy to decision steering, but those
  other artifacts are not edited in this invocation.
