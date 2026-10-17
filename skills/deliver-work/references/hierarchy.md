# Specification Hierarchy

Recommend Work tracker hierarchy from **execution cohesion**, not raw size or
ticket count.

## Options

1. **Ordinary Specification item** — one coherent outcome, one integration
   branch, one final acceptance decision. Default when the work shares a single
   acceptance boundary.
2. **Large cohesive project/epic grouping** — still one Specification outcome
   and one acceptance decision, but child Tickets benefit from a native
   project/epic container for navigation. Use when cohesion is high and the
   tracker’s project/epic construct clarifies ownership without splitting
   acceptance.
3. **Multi-Specification initiative** — multiple coherent outcomes, each with
   its own integration branch and acceptance decision, grouped only at the
   initiative level. Use when acceptance or integration boundaries truly
   diverge.

## Rules

- Every Specification retains **one** canonical issue-like record, regardless
  of grouping.
- Prefer native parent/child (and project/epic) relationships from the
  configured tracker mappings.
- When native hierarchy is weak, record explicit hierarchy metadata using the
  `workTracker.hierarchy` mapping from `.steering.json`.
- If cohesion is ambiguous (plausible ordinary item vs project/epic vs
  multi-Specification split), **confirm with the maintainer before publishing**.
  Do not guess a multi-Specification split.
