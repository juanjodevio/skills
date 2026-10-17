# Work Tracker Configuration

Record Work tracker semantics in `.steering.json` under `workTracker` after Matt
prerequisites exist. Setup supports these kinds: Linear, GitHub, GitLab, Jira,
local Markdown, and a documented custom workflow.

## Required mappings

Every configured kind must record:

- **status**: how Specification and Ticket progress states map to tracker
  fields or labels
- **role**: how agent-ready versus human-ready Tickets are represented (often
  triage-role labels)
- **hierarchy**: how a Specification relates to child Tickets and optional
  project/epic grouping (native parent/child, epic links, or explicit metadata)
- **blocker**: how blocking relationships are stored (native blocked-by links
  or explicit references when native support is absent)
- **comment/activity**: how progress notes and Specification-level run
  summaries are published

## Kind notes

- **Linear**: prefer native parent/child, relations, workflow states, and
  comments via the Linear MCP or API the Project already uses.
- **GitHub**: prefer Issues, labels, and issue comments via `gh`; record whether
  blockers use native dependencies or checklist/metadata references.
- **GitLab**: prefer Issues via `glab`; record label and relation conventions the
  Project already uses.
- **Jira**: record project key, issue types for Specification versus Ticket,
  link types for blockers, and comment vs work-log conventions.
- **local Markdown**: Issues live under a configured directory (often
  `.scratch/`); record filename conventions for status, role, hierarchy, and
  blockers in frontmatter or adjacent index files.
- **custom workflow**: write a short prose description of read/write steps for
  each semantic operation, then fill the same five mapping fields so execution
  stays adapter-shaped.

Do not reimplement Matt's tracker scaffolding here. If
`docs/agents/issue-tracker.md` (and related Matt setup output) is missing,
invoke `setup-matt-pocock-skills` by name first.
