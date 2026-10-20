# Draft a competitor change timeline

Use this mode when the requested output is a chronology, a history view, or the evidence behind a
current interpretation. Work from supplied captures, alerts, or canonical briefs. Retrieving an
archive requires an available, authorized source; this mode does not create a monitoring archive.

## Build the chronology

State the competitor, question, requested interval and timezone, evidence cutoff, and coverage.
Record missing capture dates separately; do not place them using file dates or today's date.
Apply the batch reference's event deduplication and source protections before building rows.

Use one row for each distinct observed state or event with these fields:

`Observed at | Source and scope | Exact observed state/change | Receipt | Interpretation and limit | Related brief`

Preserve distinct plan, locale, billing term, access state, and page area. Do not connect differently
scoped captures into one reversal. Keep repeated observations of an unchanged state as coverage
evidence when useful; a retry of the same event adds no observation. Sort by capture time and show
announced effective dates separately. Same-time events with unknown ordering remain unordered.

If a claim disappears and returns in comparable captures, show all observed states. State when it
was last seen, first absent, and first seen again. Those observation times bound what was captured;
they do not establish the exact removal time, uninterrupted absence, a product-policy change, or
an effective period. A new pricing plan or website layout is a different proposition from why the
competitor changed it.

## Make the view useful

Lead with the latest supported state as of the cutoff, then the chronology and gaps. Separate
observed publication from interpretations. Attach evidence basis, verification and confidence to
the interpretation that drives a recommendation; a sequence alone does not prove intent.

Link existing canonical briefs without changing their approval status. If the user asks what to do,
apply ci-triage's decision assessment and shared response options. A chronology-only request does
not require a separate full brief for every capture. Include shared draft/review/handling status
on the timeline. Keep any strategic conclusion pending review.

For local output, show a collision-safe absolute path under
`<CI root>/updates/YYYY-MM-DD-<competitor>-timeline.md`. The filename uses the processing date;
the rows retain observation dates. A visual timeline must display the same dates and receipt links
and have a readable table equivalent. State that the supplied history may omit intervening changes.

## First run

```text
Use ci-triage to build an inline timeline. Fictional practice data only; do not browse or send.
Question: what does the supplied history establish about AcmeFlow's public trial wording?
Source for every receipt: https://acmeflow.example/trial, US English, public logged-out page.
The full relevant section in each capture is the quoted text below. Effective dates are unknown.
R1, 2026-08-03 10:00 UTC: "Start your 14-day trial."
R2, 2026-08-06 10:00 UTC: "Start your 7-day trial."
R2, redelivery of the same event and capture: "Start your 7-day trial."
R3, 2026-08-09 10:00 UTC: "Start your 14-day trial."
Cutoff: August 9, 2026. These are all supplied observations, with no intervening coverage.
```
