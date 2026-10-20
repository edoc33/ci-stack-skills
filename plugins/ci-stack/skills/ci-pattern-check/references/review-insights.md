# Discover useful questions in public reviews

Use this mode for a supplied review export or accessible public reviews when collection is in
scope. Reuse authorized access and respect site terms. Do not imply that installation supplies a
review-platform API, bypass access restrictions, or invent reviews when collection is unavailable.

## Define the sample

Record the product, review platform, requested dates, actual review dates, capture dates, and
filters such as rating, keyword, segment, plan and incentive disclosures. Separate the date of a
review from the export or capture date. State whether the user supplied a selected sample or an
entire defined result set. Unknown collection coverage remains unknown.

Use a distinct review as the observable unit. Normalize repeated exports by stable review ID or a
supported duplicate mapping. A syndicated copy or updated version of the same review adds no
independent reviewer. Without identifiers, preserve uncertain duplicates and limit the count to
records; do not infer a customer denominator. One review may contain several themes, so theme
counts need not sum to the number of reviews. Do not infer buyer status or segment from a name.

## Extract reported experiences, then questions

Preserve a short exact excerpt and safe source locator for each coded theme, with product/version,
plan, role and date when supplied. Check context, negation, later edits, mixed sentiment and
counterexamples before calling something a pain point. A positive review mentioning a keyword
does not support the complaint associated with that keyword. Identify product context so a review
about an unrelated integration is not silently attributed to the core product.

Use `Evidence basis: field report` for the reviewer's experience or assertion. A capture directly
observes publication, while product behavior and prevalence remain untested. Several independent
reviewers can report the same experience, but agreement alone does not prove a universal defect,
comparative claim, or sales objection. Keep source dependence and verification explicit.

Produce a concise table:

`Theme | Supplied supporting review IDs/excerpts | Counterexamples or uncertainty | Discovery question | Evidence to validate next`

Report counts only after inspecting and deduplicating the relevant supplied records. State the
exact denominator and filters for every fraction. Never label a handpicked negative sample as
"X% of customers" or rank a market's biggest pain points from it. A small or selected sample can
still support a useful question to ask buyers. Use `repeated signal`, `single case`, or
`insufficient data` as warranted; retain the main skill's scoped-pattern rule for stronger claims.

## Keep the handoff within its evidence

Lead with the question worth testing and its source-specific basis. A proposed discovery question
must not presuppose that the competitor has the alleged weakness. Include positive or conflicting
examples that change the interpretation. Link any relevant canonical brief; otherwise leave that
association absent. Send an exact product claim to `ci-corroborate` when needed, or pass the scoped
finding to `ci-weekly` as a draft insight.

Public excerpts may remain `Handling: public` where permitted. Internal annotations, account links
or restricted source data can require `internal` or `restricted` handling. Use review IDs or roles
in portable output, omit unnecessary personal details, and preserve any supplied audience limits.
Public availability does not grant external-use approval for a new comparative claim.

Use the main skill's collision-safe `patterns/` path and shared draft fields. This mode creates no
CRM tags, outreach, monitoring jobs or published comparison.

## First run

```text
Use ci-pattern-check for review insights, inline. Fictional practice only; no browsing or sends.
Question: what discovery question about AcmeFlow setup should our PMM test?
This is a handpicked sample, not all reviews or all customers. All captures are August 6, 2026.
R1, review Aug 3, Team: "Setup took longer than I expected. Support helped us finish."
R1, duplicate export of the same review: same text.
R2, review Aug 4, Team: "Setup was quick. We connected our existing templates."
R3, review Aug 5, plan unknown: "Our custom routing rules required engineering help."
These are the full relevant fictional excerpts. Locators: fixture:R1, fixture:R2, fixture:R3.
State the sample limits and preserve the different experiences.
```
