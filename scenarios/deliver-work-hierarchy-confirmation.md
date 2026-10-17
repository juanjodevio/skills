# Scenario: Hierarchy recommendation confirms when ambiguous

## Request

Use `deliver-work` to shape intent where hierarchy could reasonably be an
ordinary Specification, a project/epic grouping, or a multi-Specification
initiative.

## Fixture

A mixed software and data Project with:

- `.steering.json` workTracker hierarchy mapping present
- work whose execution cohesion is ambiguous across ordinary Specification
  item, large cohesive project/epic grouping, and multi-Specification initiative
- maintainer available to answer confirmation questions

## Evidence profiles

software, data

## Expected outcome

- Hierarchy is recommended from execution cohesion rather than raw size.
- The three options considered are ordinary Specification item, large cohesive
  project/epic grouping, and multi-Specification initiative.
- Because the recommendation is ambiguous, the coordinator confirms with the
  maintainer before publishing.
- Every Specification still retains one canonical Specification record after the
  chosen hierarchy is applied.
