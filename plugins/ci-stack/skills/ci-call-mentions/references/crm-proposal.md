# Draft competitor-tag changes for CRM review

Use this mode when the user wants to turn call evidence into a CRM-tag proposal. It extends the
normal extraction ledger with a reviewable change plan. It never writes CRM records or treats a
draft as an executed update. The user can try it with pasted transcript text and a small supplied
record table; a CRM connector is optional for drafting.

## Establish the target and meaning

Reuse the call classifications and exact quotes from the main skill. Use the user's supplied CRM
field name, allowed values, and tagging rule. If these are missing, draft a conceptual proposal and
list the missing schema rather than inventing a provider field or a value.

Resolve an opportunity only from an explicit call-to-opportunity ID mapping or a permitted lookup
that returns a unique association. Account name, email domain, company name, and fuzzy similarity
alone are insufficient, especially when an account has multiple open opportunities. Keep ambiguous
rows held. Record the mapping source and date; do not invent a timestamp for a supplied mapping.

Keep `active_evaluation`, `current_use`, `historical`, `negated`, `seller_only`, and `unclear` separate.
An incumbent tag and an active-evaluation tag have different meanings. The requested field's rule
determines eligibility; a Slack candidate is not a universal CRM-tag rule. Preserve corrections.

## Produce a proposed change plan

For each call/competitor/target combination, record:

`Call ID | Opportunity ID | Mapping basis | Field | Current value and read time | Proposed operation/value | Context | Quote/time/receipt | Disposition and reason`

Use `propose`, `no change`, or `hold` for disposition. Read or accept the current value when supplied.
For a multi-value field, propose the smallest additive operation and preserve existing unrelated
values. If the value is already present, use `no change`. Missing current state holds an exact
replacement plan; an additive concept can be shown as pending a fresh read. Never infer that
absence of a mention authorizes removing an existing tag. Explicit withdrawal can support a
removal proposal only when the supplied field policy and scope allow it; retain the prior evidence.

Give each proposal a stable source/target identity from available provider, workspace, call,
canonical competitor, opportunity ID and field. Keep missing identity components explicit and
hold execution readiness. Group repeated mentions into the same proposal while preserving their
receipts. A changed transcript proposes a revision to the same target, not a new independent tag.

Initialize shared draft statuses and carry source handling restrictions into the output. Mark
`CRM execution: not performed`. This record is separate from any Slack delivery record. Missing
Slack destination, delivery authorization, or Slack timestamps do not block a local CRM proposal.

Save a collision-safe `updates/YYYY-MM-DD-crm-tag-proposal.md` under the shown CI root if requested;
inline mode needs no directory. Any future executor needs separate scoped write authorization, a
fresh target-state check, and a confirmed result before claiming the CRM changed. A stale supplied
snapshot is insufficient for a blind replacement.

## First run

```text
Use ci-call-mentions to propose CRM tags inline. All data is fictional; no browsing or writes.
Provider/workspace/call: fixture / workshop / C1. Competitor: AcmeFlow.
Buyer at 02:10: "We are evaluating AcmeFlow for the support workflow this month."
This is the complete relevant exchange. Receipt: fixture:C1@02:10, captured August 6, 2026.
Call C1 is explicitly mapped to opportunity O1 by the supplied fixture mapping, date unknown.
Field: evaluated_competitors, multi-value. Allowed values: AcmeFlow, CedarQueue.
Policy: include explicit current buyer evaluations only. Current O1 value: [CedarQueue], read Aug 6.
Draft the proposal and any checks required before a separate executor could apply it.
```
