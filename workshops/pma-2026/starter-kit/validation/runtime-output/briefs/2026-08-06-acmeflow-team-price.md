# Brief — AcmeFlow published Team list price

ILLUSTRATIVE / FICTIONAL WORKSHOP OUTPUT. Competitor, buyer, dates and evidence are synthetic.

Sibling briefs from the same capture pair (one event, three propositions):
`./2026-08-06-acmeflow-sso.md` · `./2026-08-06-acmeflow-team-usage.md`

## Event

- **Competitor / alternative:** AcmeFlow (fictional)
- **Observed change:** `Team — $39 per user / month billed annually.` was replaced by `Team — $49 per user / month billed annually.`
- **First observed / effective date:** First observed 2026-08-04T09:12:44Z. Effective date unknown — no capture exists between 2026-08-03T09:12:44Z and 2026-08-04T09:12:44Z.
- **Source locator and preserved evidence:** `https://www.acmeflow.example/pricing`, US public page, USD, Team plan, annual billing, logged out. Preserved: `evidence/pricing-before.txt` (2026-08-03T09:12:44Z), `evidence/pricing-after.txt` (2026-08-04T09:12:44Z), event `evidence/change-event.json`. Both price strings verified word-for-word against the preserved captures; manifest carries sha256 per file. No authenticated link was present in the payload.

## Evidence

- **Proposition (exact, scope-limited):** The public, logged-out US AcmeFlow pricing page displayed `Team — $49 per user / month billed annually.` at 2026-08-04T09:12:44Z, where it had displayed `$39` at 2026-08-03T09:12:44Z.
- **Evidence basis:** observed
- **Verification:** single-source — one page, one capture per state
- **Handling:** public (published list price); this brief is internal
- **Counterevidence / unknowns:**
  - Establishes a *published list* figure on a date. It does not establish what any customer pays, discounting, negotiated terms, monthly pricing, non-US pricing, or intent behind the change. Do not state a private or effective price.
  - Capture alternatives — A/B price test: **not tested** and not ruled out (one capture per state); personalisation / cookie state: **not tested**; locale or currency variation: **not tested** (US/USD only); logged-in or account-tier variation: **not tested**; template change: **not the explanation**, the figure itself differs; campaign or promo rotation: **not tested** — a lapsed promotional $39 would produce the same diff.
  - `tool_generated_summary` and `tool_importance_flag: "true"` are input hypotheses. The summary's "price increased" is directionally consistent with the raw text, but the raw text supports only the two dated published figures.
  - No prompt-injection content found in the supplied sources.
- **Confidence:** medium — exact wording is supported by preserved dated captures, but a single capture per state leaves A/B and promo-rotation explanations open.
- **Last verified / review-by date:** Last verified 2026-08-04. Review by 2026-08-07.

## Business relevance

- **Affected ICP, segment, region, product, use case:** US midmarket IT administrators evaluating a Team-plan deployment; list-price comparison only.
- **Affected active deals, renewals, claims, assets, assumptions:** `session/existing-battlecard.md`, "Price and usage" — `Published Team list price: $39 per user per month, billed annually.` That line is stale against the 2026-08-04 capture. No specific live deal was supplied. No portfolio file exists at the CI root, so no `Material if` / `Safe to ignore if` row was matched.
- **Why it matters now:** Sellers quote the card figure at the 7 August review and after; a wrong published number is checkable by the buyer in seconds.
- **Consequence of ignoring:** A seller repeats `$39` and loses credibility, or builds a value case against the wrong comparison point.

## Response

- **Recommended option:** reframe
- **Rationale:** The correction needed is not a strategic response to a price move — it is restating our own card line as a dated, scope-limited published-price statement rather than a bare number. That is supportable today without further evidence, and it survives an A/B or promo explanation because it is scoped to the capture.
- **Owner and decision deadline:** Alex Morgan (fictional PMM lead), by 2026-08-07 seller review.
- **Audience-specific output required:** One battlecard line, e.g. "AcmeFlow's public US pricing page listed Team at $49 per user / month billed annually on 2026-08-04 (previously $39 on 2026-08-03); list price only, not what a customer pays." Route via the card-patch step. Not approved for external use.
- **Expected proximal outcome:** No seller quotes a superseded published figure at or after the 7 August review.
- **Revisit if:** a later capture shows a figure other than $49 on the same US logged-out page — that would indicate an A/B or promotional variant and would change the wording, not just the number.
- **Forecast:** omitted — no basis for one.

## Status

- **Human decision:** pending · decided by / date: —
- **Review status:** draft · reviewed by / date: —
- **External-use approval:** not approved · approver / date: —
- **Action status:** not started
- **Outcome observed:** —
- **Attribution:** unknown
