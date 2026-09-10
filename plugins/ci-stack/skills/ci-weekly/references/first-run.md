# Try a period update with fictional briefs

Paste this prompt into a session where the skill is available. These are fictional records and
decisions for the exercise. The `.example` URL is a fixture locator; do not fetch it.

```text
Use ci-weekly to draft an internal PMM newsletter for August 1 through August 15, 2026, UTC.
Work inline using only these fictional records. We have two briefs and no portfolio or outcome
data beyond what follows. Do not send anything. Mark the update as a draft.

Brief ID: fixture-export-docs
Competitor / alternative: AcmeFlow (fictional)
Observed change: A docs page now describes a CSV export.
First observed / effective date: August 4, 2026; effective date unknown
Proposition: The public docs page displayed "Export your records as CSV."
Source locator and preserved evidence: https://acmeflow.example/docs/export,
captured 2026-08-04T12:00:00Z, US public English docs; preserved text in this fixture:
"Export your records as CSV."
Evidence basis: observed
Verification: single-source
Handling: public (synthetic fixture)
Confidence: high that the docs displayed this text; actual export behavior untested
Counterevidence / unknowns: Plan entitlement, prior availability, and buyer demand unknown
Recommended option: validate
Rationale: A PMM should check whether the existing battlecard's export comparison is still accurate.
Owner and decision deadline: unassigned; unknown
Human decision: pending
Review status: draft
External-use approval: not approved
Action status: not started
Outcome observed: unknown
Attribution: unknown

Brief ID: fixture-wording
Competitor / alternative: AcmeFlow (fictional)
Observed change: Homepage headline changed from "Coordinate work" to "Organize work."
First observed / effective date: July 30, 2026; effective date unknown
Source locator and preserved evidence: https://acmeflow.example,
captures 2026-07-29T12:00:00Z and 2026-07-30T12:00:00Z, same US public English page.
Preserved before text: "Coordinate work." Preserved after text: "Organize work."
Evidence basis: observed
Verification: single-source
Handling: internal (synthetic exercise decision)
Confidence: high for the captured text; strategic significance unknown
Counterevidence / unknowns: No supporting change in the supplied pricing or product evidence
Recommended option: continue monitoring
Rationale: Supplied wording alone does not justify a positioning change.
Revisit if: Product or packaging evidence shows a change affecting our target segment.
Human decision: accepted; decided by Fictional PMM Reviewer on August 2, 2026
Review status: reviewed; reviewed by Fictional PMM Reviewer on August 2, 2026
External-use approval: not approved
Action status: not started
Owner and decision deadline: Fictional PMM Reviewer; unknown
Outcome observed: unknown
Attribution: unknown
```

The update should separate the pending validation recommendation from the accepted monitoring
decision. The headline change is a carried-over observation with an in-period decision. Missing
outcomes stay unknown, and two supplied briefs do not establish complete monitoring coverage.

To save files, supply an absolute CI root and request local output. Save the newsletter under
`<CI root>/updates/`. Save proposed view snapshots and diffs beside the final views at the CI root
so relative links still work when the proposals are applied. Follow the [skill's file-output rules](../SKILL.md)
for filenames and collision handling. A later run can use a monthly or custom date interval without
changing skills. Scheduling collection and delivery requires a separate configured workflow.
