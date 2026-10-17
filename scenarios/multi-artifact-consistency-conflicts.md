# Scenario: Multi-artifact consistency conflicts

## Request

Use `steer-project` to align Intent, technology, and Roadmap after recent
repository churn.

## Fixture

A mixed Project with `.steering.json` mappings for `intent`, `technology`, and
`roadmap`, and:

- Intent claiming mid-market operations leaders as the audience
- technology docs locking an enterprise-only warehouse SKU that contradicts that
  audience constraint
- Roadmap Now items sequencing campaign automation ahead of the attribution
  export that Intent treats as the core outcome
- software, data, and marketing evidence that each partially supports a
  different resolution
- no maintainer confirmation of which artifact is wrong

## Evidence profiles

software, data, marketing

## Expected outcome

- Cross-artifact conflicts are reported explicitly and never resolved silently.
- No second artifact is quietly rewritten to erase a conflict discovered while
  updating another.
- Conflicting claims remain visible as questions, Assumptions, or Unknowns when
  a safe provisional update proceeds.
- Related work for the conflicting owners returns through the orchestrator;
  focused adapters do not side-call each other to force consistency.
- ADR eligibility and focused templates are not duplicated inside the
  orchestrator; decision follow-ups are routed to `steer-decisions` when
  appropriate.
