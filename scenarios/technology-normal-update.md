# Scenario: Technology normal update

## Request

Use `steer-project` to capture that this Project standardizes on pnpm, a shared
warehouse pipeline runner, and a single attribution integration for paid
campaigns.

## Fixture

A mixed Project with:

- `.steering.json` mapping `technology` to `docs/STACK.md`
- an empty or sparse Technology Steering artifact at that mapped path
- software manifests, automation, configuration, tests, and commits showing
  pnpm lockfiles and CI scripts
- data platforms, pipelines, schemas, catalogs, quality checks, and run
  constraints for the warehouse
- marketing platforms, channels, integrations, attribution tooling, and
  operational constraints for campaign measurement

## Evidence profiles

software, data, marketing

## Expected outcome

- Ownership is classified as technology and routed through `steer-technology`.
- The configured artifact path is used; the physical filename is not assumed.
- Evidence is inspected from all three profiles and treated as evidence only.
- Material unknowns are resolved or recorded; no invented stack or command
  policy.
- Only the Technology Steering artifact is updated.
- Assumptions, unknowns, and last-reviewed metadata appear when relevant.
- Related Intent, design, roadmap, structure, decision steering, or
  agent-guidance work is reported rather than performed in this invocation.
