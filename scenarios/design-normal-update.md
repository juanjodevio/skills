# Scenario: Design normal update

## Request

Use `steer-project` to capture that this Project's experience should feel calm
and operational, with a restrained palette and WCAG AA contrast for dense
dashboards.

## Fixture

A mixed Project with:

- `.steering.json` mapping `design` to `docs/VISUAL.md`
- an empty or sparse Design Steering artifact at that mapped path
- software UI components and screenshots showing a muted dashboard
- data report layouts using the same spacing rhythm
- a marketing brand brief describing calm, trustworthy operations visuals

## Evidence profiles

software, data, marketing

## Expected outcome

- Ownership is classified as Design and routed through `steer-design`.
- The configured artifact path is used; the physical filename is not assumed.
- User, repository, visual, and brand evidence are inspected and treated as
  evidence only.
- Material unknowns are resolved or recorded; no invented atmosphere or
  accessibility bar.
- Only the Design Steering artifact is updated.
- Assumptions, unknowns, and last-reviewed metadata appear when relevant.
- Related intent, technology, roadmap, structure, decision, or agent-guidance
  work is reported rather than performed in this invocation.
- Stitch is not installed, invoked, or required.
