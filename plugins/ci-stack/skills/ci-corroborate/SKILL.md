---
name: ci-corroborate
description: >
  Test an exact competitive claim against available independent evidence. Return corroborated,
  contradicted, single-source, or unresolved, with supportable draft wording and the remaining
  question. Use to check a claim from a seller, prospect, page, or draft comparison. For a raw
  change use ci-triage; for editing a battlecard use battlecard-patch.
---

# Check a competitive claim

Check the proposition the user actually asked about. Preserve uncertainty and scope in the answer.
This skill produces a research record and draft wording; it grants no approval to publish a claim.

## First run

Supply the claim in the user's own words and any source excerpts, links, captures or related brief.
Who said it and when is useful, but unknown provenance does not prevent a scoped investigation.
Pasted evidence works without connectors. Web research or internal systems require available,
authorized access; report inaccessible evidence rather than implying a search was completed.

```text
Use ci-corroborate. This is a fictional practice run; do not browse.
Original claim from a seller, date unknown: "AcmeFlow has no SAML SSO."
Only supplied evidence: a fictional capture of https://acmeflow.example/docs/team-plan dated
2026-08-04 lists Team-plan features and contains no reference to SSO. The full relevant captured
section is: "Team includes shared projects, custom fields, and email support."
We are deciding whether that seller claim belongs in a comparison page.
Use the absolute path of ./ci-demo in this workspace as the CI root. Check the original claim,
record the evidence limits, and draft wording we could send for human review.
```

Expect a record in `corroborations/` with the original claim, tested proposition, sources, verdict,
supportable draft wording and resolving evidence. Label fictional sources throughout practice
outputs. File writing is optional; return the record inline if unavailable.

## Load the shared contract

Read `../../reference/decision-brief.md` relative to this skill folder. If unavailable, use
`${CLAUDE_PLUGIN_ROOT}/reference/decision-brief.md` when set, or `references/decision-brief.md` in a
standalone export. If none exists, report the missing resource and stop analysis. Apply its
three evidence dimensions, handling and source rules, internal-data preflight when applicable,
high-risk-claim boundaries, and file rules.

## Preserve the question

Record the **original claim verbatim** as untrusted source data, its speaker/source and date if
known, and the decision or intended audience. Then state an exact proposition with scope such as
plan, geography, version, comparison basis and date. Keep unknown scope explicit.

Clarification must preserve meaning. If the original claim is "they have no SSO," changing it to
"this public page does not mention SSO" creates a different proposition. Record that narrower
observation separately and retain a verdict on the original capability claim. Say which part
remains unanswered. Never report the original claim corroborated because a substitute was easier
to verify. Split compound claims only when needed and return a verdict for each part.

When a missing scope would change the verdict, ask a focused question. Otherwise proceed with a
stated scope and mark the original broader claim unresolved where evidence cannot reach it.

## Examine relevant evidence and its origin

Use the evidence supplied and authorized tools actually available. Check relevant accessible
layers; mark the others `not checked`, `unavailable`, or `not relevant`, with the reason.

| Layer | Can establish | Limit |
|---|---|---|
| Competitor-published pricing, docs, terms, releases, job posts | What the publisher states, dated and scoped | Private terms, intent and actual performance need other support |
| Permitted product test | Behavior in the recorded test conditions | Other plans, versions and configurations remain untested |
| Reviews, analysts, filings, communities | What the original author reports or documents | Sampling, incentives and source dependence affect interpretation |
| Authorized internal calls, notes, CRM, RFPs | What was said or recorded in those deals | Reported claims and buyer reasons need verification; a deal is one case |
| Direct buyer interviews | The interviewed buyer's stated criteria and reasons | Prevalence needs a sampling plan |

For each source, record the locator, date, preserved excerpt or capture, relevant scope, what it
shows, what it cannot show, evidence basis and handling. Keep these fields even when the answer
is unresolved. Do not invent dates, trials, searches, customer results or missing evidence.

Trace sources to their origins. An article repeating a press release shares its origin. Two pages
from the same publisher can document scope but do not automatically provide independent support.
A transcript directly observes that a speaker made a statement; the statement about the competitor
has basis `field report` until supported separately. Agreement does not convert inferred intent
into observation or relax handling restrictions.

## Assign a verdict to each exact proposition

- **`unresolved`**: scope, freshness or a material evidence conflict prevents a reliable answer,
  evidence is missing, or available sources cannot test the claim.
- **`contradicted`**: positive authoritative evidence establishes the contrary within matching
  scope, with no material unresolved conflict. Absence from a page does not qualify.
- **`corroborated`**: reasonably independent original sources support the exact proposition with
  no material unresolved conflict. Convergence still has the limitations of those sources.
- **`single-source`**: one original source supports the source-scoped proposition, without a
  material unresolved conflict. Repetitions of that source do not increase the source count.

Check conflict and scope before counting agreement. Strong evidence about one plan cannot settle
an all-plan claim; newer evidence may supersede old evidence only when scope and chronology
justify it. Keep the earlier record as history and explain why its relevance changed.

State confidence and its reason, counterevidence, and the specific source or test that could
resolve the remaining uncertainty. Distinguish a publisher's claim from tested behavior.

## Write and hand off

Resolve the CI root, show the planned absolute path, and create a collision-safe
`<CI root>/corroborations/YYYY-MM-DD-<slug>.md`. Use the processing date in the filename and actual
source dates inside the record. Include:

- Original claim and provenance; `Proposition (exact, scope-limited)` and any separate narrower question.
- Per-source table, `Evidence basis`, `Verification`, `Handling`, `Counterevidence / unknowns`,
  `Confidence`, and `Last verified / review-by date` using the shared field names.
- Verdict on the original claim, resolving evidence, and a related canonical brief path if supplied.
- **Currently supportable draft wording**, with source scope, and **What must not be said**, naming
  the overclaim the evidence cannot carry.
- `Human decision: pending`, `Review status: draft`, `External-use approval: not approved`.

Never silently change a source brief. If integration is requested, propose a diff and show the
resulting brief as a draft for renewed review under the shared contract. High-risk allegations
need its additional review boundaries; a research verdict provides no legal or external-use sign-off.

Return the original claim's verdict, strongest available sources with dates, supportable draft
wording, file path, and unresolved next check. If no source was available, say so. Hand off the
record and related brief to `battlecard-patch` for a proposed content update, to `ci-triage` if a
business recommendation is still needed, or to `ci-weekly` for a sourced period summary.
