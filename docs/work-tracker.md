# Work Tracker Guidance

Specifications and Tickets are canonical in the configured **Work tracker**.
This suite does not hard-code a single vendor. Setup records kind and mappings
in `.steering.json`; `deliver-work` and Matt skills read those mappings.

For this repository’s own tracker conventions, see
[agents/issue-tracker.md](agents/issue-tracker.md). For setup field details, see
`skills/setup-project-steering/references/tracker-configuration.md`.

## Supported kinds

| Kind | Typical tooling | Notes |
| --- | --- | --- |
| Linear | Linear MCP / API | Prefer native parent/child, relations, workflow states, and comments. |
| GitHub | `gh` Issues | Prefer Issues, labels, and comments; record blocker representation. |
| GitLab | `glab` Issues | Prefer Issues with the Project’s label and relation conventions. |
| Jira | Jira Cloud/Server API or CLI | Record project key, Specification vs Ticket issue types, blocker link types. |
| local Markdown | files under a configured directory (often `.scratch/`) | Record filename and frontmatter conventions for status, role, hierarchy, blockers. |
| Configured alternatives | documented custom workflow | Write short prose for each semantic operation, then fill the same mapping fields. |

## Required mappings

Every kind must define:

- **status** — Specification and Ticket progress
- **role** — agent-ready versus human-ready Tickets
- **hierarchy** — Specification to Tickets (and optional project/epic grouping)
- **blocker** — blocking relationships
- **comment / activity** — progress notes and Specification-level run summaries

## Operating rules

- Keep Specifications and Tickets canonical in the tracker, not duplicated into
  Steering artifacts.
- Refresh Ticket state and blockers from the tracker as work progresses.
- Update each reviewed Ticket before downstream work relies on it.
- Custom workflows stay adapter-shaped: same five mappings, different transport.

## Matt prerequisites

If tracker scaffolding docs are missing (`docs/agents/issue-tracker.md` and
related Matt setup output), invoke `setup-matt-pocock-skills` by name before
recording Work tracker configuration. Do not reimplement Matt’s tracker setup
inside this suite.
