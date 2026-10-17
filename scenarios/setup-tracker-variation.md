# Scenario: Setup records Work tracker configuration variants

## Request

Use `setup-project-steering` to configure Project steering and the Work
tracker seam for this repository.

## Fixture

Projects covering each supported tracker kind across separate fixtures or
confirmed choices:

- Linear
- GitHub
- GitLab
- Jira
- local Markdown
- a documented custom workflow described by the maintainer

Matt tracker/domain prerequisites may be missing for some fixtures and, when
missing, are delegated to `setup-matt-pocock-skills` by name.

## Evidence profiles

software

## Expected outcome

- Missing tracker or domain prerequisites are delegated to
  `setup-matt-pocock-skills` rather than reimplemented locally.
- Work tracker configuration supports Linear, GitHub, GitLab, Jira, local
  Markdown, and a documented custom workflow.
- Tracker configuration records status, role, hierarchy, blocker, and
  comment/activity mappings for the chosen kind.
- Compatible existing Matt tracker docs are preserved when already complete;
  steering-specific tracker mappings are added only after confirmation.
