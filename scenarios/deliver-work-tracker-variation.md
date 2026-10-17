# Scenario: Equivalent lifecycle outcomes across Work trackers

## Request

Use `deliver-work` to shape intent into an approved Specification and Tickets
under different configured Work tracker kinds.

## Fixture

Projects covering each supported tracker kind across separate fixtures or
confirmed `.steering.json` workTracker configurations:

- Linear
- GitHub
- GitLab
- Jira
- local Markdown
- a documented custom workflow

Each fixture has the same shaping request and available Matt skills by name.

## Evidence profiles

software

## Expected outcome

- Lifecycle outcomes are equivalent across tracker kinds: one canonical
  Specification record, hierarchy applied (with confirmation when ambiguous),
  and approved Tickets with roles and blockers.
- Publication uses `.steering.json` workTracker mappings (status, role,
  hierarchy, blocker, comment/activity) rather than hardcoded vendor logic.
- Native parent/child and blocker relationships are preferred; explicit
  metadata fallback is used only when native support is absent.
- Resume rules (new → grill; approved Specification → to-tickets; approved
  Tickets → skip) behave the same regardless of tracker kind.
