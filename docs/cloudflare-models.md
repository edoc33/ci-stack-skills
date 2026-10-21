# Optional Clef and Clairic evaluation

Reviewed October 19, 2026. Clef and Clairic model documentation rechecked October 21, 2026. This is an integration recommendation. This repository has no deployed
adapter, and this review made no inference calls. Performance on these CI workflows is unmeasured.

**Clairic could extract the evidence; Clef could help route it; your existing assistant would
interpret it and write the draft.** Try this first on a saved public page change. The current
skills remain the default and work without either model.

Clef selects among defined options. Clairic returns typed values, including text spans, dates,
and numbers. These roles could make repeated extraction and classification easier to inspect.
They do not establish that a source claim is true. [Clef documentation](https://developers.cloudflare.com/workers-ai/models/clef/)
and [Clairic documentation](https://developers.cloudflare.com/workers-ai/models/clairic/).

Clairic entered preview on October 19. Cloudflare identifies limitations in arithmetic,
forecasting, and calibration on unfamiliar data. Start with extraction and keep dates, arithmetic,
deduplication, and record matching in deterministic code where possible.
[Clairic announcement](https://blog.cloudflare.com/clairic-extraction-model/).

The applications below are proposals to evaluate.

| Workshop workflow | Potential model contribution | Work retained in the existing workflow |
|---|---|---|
| Call → CRM competitor tag | Clairic extracts the mention and quote. Clef classifies active evaluation, current use, historical reference, or unclear context. | Resolve aliases and CRM identity; review ambiguity; authorize the write. A mention alone does not establish a competitive deal. |
| Call → Slack context brief | Clairic extracts buyer criteria and objections. Clef identifies relevant known topics. | Retrieve approved context, write the brief, and perform any authorized delivery. |
| Alert → battlecard patch | Clairic extracts before/after claims and qualifiers. Clef suggests the affected section and need for review. | Check chronology and sources, propose the smallest supported edit, and approve it. |
| Competitor timeline | Clairic extracts details from each capture. Clef categorizes events and flags possible contradictions. | Preserve capture dates separately from claimed event dates; sort, deduplicate, and explain the sequence. |
| Competitive newsletter | Clairic extracts reusable facts. Clef tags and prioritizes items using an explicit editorial rubric. | Group related changes, explain implications, check sources, and approve publication. |
| Affected-deal notification | Clairic extracts the changed condition. Clef assesses relevance to an already matched deal context. | Select permitted CRM records using exact fields; review the implication and draft the owner message. |
| Related-change research brief | Clairic extracts shared entities and claims. Clef screens candidate sources for relevance or disagreement. | Search, retrieve, assess independence, and examine alternative explanations. |
| Review → discovery questions | Clairic extracts the reviewer's stated problem and quote. Clef assigns a theme. | Write neutral questions and preserve the limits of one reviewer's experience. |

For `ci-portfolio`, Clef could classify retrieved pages against the PMM's decision, while the
existing workflow discovers and checks URLs. For `ci-triage`, the useful experiment is a shared
evidence record followed by proposed routing. A change may belong in several outputs, so use
separate questions for battlecard review, timeline inclusion, and digest consideration.

**Developer notes.** These are illustrative request shapes, not a tested adapter. Use the Workers
AI run endpoint or binding. The REST response has a `result`/`success`/`errors` envelope; validate
transport and provider success before reading the model result. Binding examples return the
model response directly. [Workers AI REST guide](https://developers.cloudflare.com/workers-ai/get-started/rest-api/).

For `@cf/cloudflare/clairic`, a request could be:

```json
{
  "model": "clairic",
  "state": "Fictional saved capture: Team plan. USD 20 per seat per month. SSO included.",
  "fields": {
    "plan_name": {"type": "text", "instructions": "Exact plan name in the capture"},
    "price_text": {"type": "text", "instructions": "Exact price with currency, seat basis, and billing period"},
    "sso_claim": {"type": "text", "instructions": "Exact statement about SSO"}
  }
}
```

Send each snapshot separately. Bind the result to an immutable snapshot ID, canonical URL, and
capture timestamp in your application. Preserve the exact input text, returned quotes and spans,
and before/after association. Capture metadata should come from the source system. Price text is
useful here because a bare number loses billing terms and qualifiers.

For `@cf/cloudflare/clef`, a separate request could be:

```json
{
  "model": "clef",
  "state": {
    "snapshot_before": "example-before",
    "snapshot_after": "example-after",
    "before_quote": "SSO available on Enterprise only.",
    "after_quote": "SSO included.",
    "current_card_claim": "SSO is Enterprise only.",
    "scope": "Fictional Team-plan captures from the same region and signed-out state"
  },
  "questions": {
    "battlecard_review": {
      "type": "choice",
      "instructions": "Does this evidence warrant reviewing the current card claim?",
      "criteria": {
        "review": "The captured wording may conflict with the current card",
        "no_review": "The evidence supports leaving the current card as it is",
        "unclear": "The supplied evidence is insufficient or contradictory"
      }
    }
  }
}
```

Clef supports `choice`, `noul` (true/false), and ordered `score` questions. A choice result includes
the selected option, confidence, and per-option probabilities. A score is probability-weighted.
Evaluate the distribution and include a review path; a selected option is a prediction.
[Cloudflare's Clef model card](https://huggingface.co/Cloudflare/clef).

Clairic uses a string `state` and typed `fields`. Its results can include `value`, `span`,
`confidence`, `p_null`, and `guess`; it also reports `truncated` and usage. A null value can coexist
with a high-confidence guess. **Preserve null. Never substitute `guess` for a missing value.**
`reference_date` can anchor dates without a year, but the capture date should never become an
invented event date. [Clairic documentation](https://developers.cloudflare.com/workers-ai/models/clairic/).

Build the adapter around these rules:

- Validate spans against the exact input, including repeated text and Unicode. Keep original
  quotations available to the drafting skill and reviewer.
- Treat nulls, empty lists, conflicting evidence, and missing required fields as reasons to
  review the input. Estimates and forecasts can return predictions even with weak evidence;
  leave those field types out of this initial integration.
  [Extraction-model guidance](https://developers.cloudflare.com/workers-ai/concepts/extraction-models/).
- Start with review of every proposed action. Choose numeric thresholds from a held-out
  evaluation, and document the errors each threshold allows.
- Avoid silent truncation. Clef documents automatic text truncation. Clairic lists a 65,536-token
  context while also describing field splitting against 8,192-token passes. Use compact source
  chunks, reject automatic routing when completeness is uncertain, and directly test long-input
  behavior. Start with text and preserve screenshots for review.
  [Clef documentation](https://developers.cloudflare.com/workers-ai/models/clef/) and
  [Clairic documentation](https://developers.cloudflare.com/workers-ai/models/clairic/).
- Keep quoted source content untrusted. Obtain destinations, permissions, and writable record
  IDs from trusted configuration. Models should propose an action within the existing workflow's
  authorization rules.
- Fall back to the current skill and original evidence when the optional service is unavailable,
  fails validation, or produces an uncertain result. Preserve uncertainty in the final draft.

Use public or clearly labeled synthetic evidence for the first pilot. Processing customer calls
or CRM records through another provider requires an appropriate permitted data path. Cloudflare
documents standard-inference retention and training commitments, with exceptions and separate
behavior for storage, logging, caching, and stateful features.
[Workers AI data usage](https://developers.cloudflare.com/workers-ai/platform/data-usage/).

**Measure the benefit.** Compare the current skill with Clef-only triage, Clairic-only extraction,
and the combined route using the same evidence and final drafting model. Label examples before
tuning, then reserve a separate evaluation set. Include cosmetic edits, policy wording that
disappears and returns, missing dates, ambiguous prices, contradictory sources, multiple
competitors, and malicious instructions embedded in source text.

Record field and span correctness, routing precision and recall, missed material changes,
unsupported claims, calibration, abstention, reviewer correction time, end-to-end latency, and
actual billed usage including retries and fallbacks. Report median and p95 latency alongside
sample size and test conditions. Vendor benchmarks do not establish performance on this workload.
Keep the integration optional until a dated pilot demonstrates a useful improvement.
