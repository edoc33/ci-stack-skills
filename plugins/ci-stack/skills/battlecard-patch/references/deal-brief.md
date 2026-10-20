# Draft a brief for affected deals

Use this mode to connect a reviewed competitive development to supplied active opportunity
evidence and existing approved guidance. A card is optional. The deliverable is an internal draft
for the account team to review. An authorized read-only CRM lookup may supply evidence when it is
part of the request. This mode never updates CRM or sends the brief.

## Match the development to the deal

Use the supplied decision brief or corroboration, its receipts and cutoff, plus the relevant
opportunity ID, call or note date, buyer's stated evaluation criteria, and competitor context.
Reuse internal-data authorization from the session. Request only missing evidence that changes
the match; an owner, amount, stage or deadline may remain unknown.

An account name or competitor tag alone does not establish a currently affected deal. Require a
supplied exact opportunity association and dated buyer evidence of active evaluation or a
relevant current-use concern. Check later supplied corrections, evaluation pauses, closed status,
and the scope of the competitor change. Keep merely plausible matches in a held list with the
reason. Do not claim that every tagged opportunity is affected or infer revenue at risk.

## Use approved guidance without approving new claims

For buyer-facing guidance, require the actual wording and a recorded human review and external-use
approval covering this audience and scope. Retain the approver, date, and source. The word
"approved" in a filename or an owner assignment is insufficient. Check whether the new evidence
conflicts with that guidance; hold stale approved wording for renewed review.

Sellers may read permitted internal reference notes. Identify an approval limited to internal
reference as such; it does not permit the seller to repeat or send the wording to a buyer.
Quote or reference applicable approved guidance accurately. A new tailored recommendation,
question, comparison, or paraphrase remains a draft. A supplied draft or single-source public
claim may justify an internal validation note, but it cannot silently become an approved seller
assertion. If approved guidance is missing, produce the useful internal assessment, identify the
missing guidance, and hold buyer-facing assertions. Apply the parent skill's narrow publication
exception only to a dated, attributed proposed line awaiting review. Do not block drafting to
request an existing card.

## Keep the output short and traceable

For each supported match, include:

- Opportunity ID and permitted label, with mapping evidence and as-of date.
- Why it may matter: the buyer's exact criterion, dated call receipt, and matching competitive
  observation, clearly separated from inferred deal impact.
- Applicable approved guidance, preserving its original scope and approval attribution.
- One proposed next conversation or check, owner/deadline if supplied, and unresolved evidence.
- Source paths and the new artifact's shared draft, handling, and approval fields.

State the input scope: how many supplied opportunities were assessed, supported matches, and held
or unmatched records. Those counts describe the supplied set. A competitor mention alone cannot
establish deal influence, loss causation, or pipeline exposure.

For requested files, show a collision-safe path
`<CI root>/updates/YYYY-MM-DD-<competitor>-deal-brief.md`. Preserve all original cards and briefs.
No patch is needed unless the user also asks to update a supplied card.

## First run

```text
Use battlecard-patch for an internal affected-deal brief, inline. All records are fictional.
No browsing, CRM writes or messages. No existing battlecard is available.
Opportunity O1 is open. Call C1 is explicitly mapped to O1, dated August 6, 2026.
Buyer at 02:10: "We are comparing AcmeFlow Team. SAML SSO is required for the pilot."
Receipt: fixture:C1@02:10. This is the complete relevant exchange.
Brief B1: AcmeFlow's public pricing page displayed "Team: SSO included" on August 6.
Receipt: https://acmeflow.example/pricing; the quoted text is the full relevant captured section.
Evidence basis observed; verification single-source; public; behavior and protocol untested.
Recommendation validate; human decision pending; review draft; external-use not approved.
Approved guidance G1: "Ask which identity provider and protocol the pilot must support."
Reviewed and approved for buyer-facing use by fictional PMM Sam on August 5, 2026.
Prepare the internal briefing and keep any new wording pending review.
```
