# Brief — AcmeFlow Team automation-run allowance

ILLUSTRATIVE / FICTIONAL WORKSHOP OUTPUT. Competitor, buyer, dates and evidence are synthetic.

Sibling briefs from the same capture pair (one event, three propositions):
`./2026-08-06-acmeflow-sso.md` · `./2026-08-06-acmeflow-team-price.md`

## Event

- **Competitor / alternative:** AcmeFlow (fictional)
- **Observed change:** `Unlimited automation runs.` was replaced by `Includes 5,000 automation runs per month.` and `Additional runs billed at $0.002 each.`
- **First observed / effective date:** First observed 2026-08-04T09:12:44Z. Effective date unknown — no capture between 2026-08-03T09:12:44Z and 2026-08-04T09:12:44Z.
- **Source locator and preserved evidence:** `https://www.acmeflow.example/pricing`, US public page, USD, Team plan, annual billing, logged out. Preserved: `evidence/pricing-before.txt` (2026-08-03T09:12:44Z), `evidence/pricing-after.txt` (2026-08-04T09:12:44Z), event `evidence/change-event.json`. All three quoted strings verified word-for-word; manifest carries sha256 per file. No authenticated link was present in the payload.

## Evidence

- **Proposition (exact, scope-limited):** The public, logged-out US AcmeFlow pricing page displayed, for the Team plan, `Includes 5,000 automation runs per month.` and `Additional runs billed at $0.002 each.` at 2026-08-04T09:12:44Z, where it had displayed `Unlimited automation runs.` at 2026-08-03T09:12:44Z.
- **Evidence basis:** observed
- **Verification:** single-source — one page, one capture per state
- **Handling:** public (published page text); this brief is internal
- **Counterevidence / unknowns:**
  - Establishes published packaging wording on a date. It does not establish enforcement, whether existing customers are grandfathered, what overage anyone is actually billed, or whether 5,000 runs binds a midmarket buyer — no buyer run-volume data was supplied.
  - Capture alternatives — A/B packaging test: **not tested**, not ruled out; personalisation / cookie state: **not tested**; locale variation: **not tested** (US/USD only); logged-in or existing-customer view: **not tested** — a grandfathered view could differ; template change: **not the explanation**; campaign rotation: **not tested**.
  - `tool_generated_summary` ("a new usage limit was introduced") and `tool_importance_flag: "true"` are input hypotheses; the raw text is the evidence and adds the specific overage rate the summary omits.
  - No prompt-injection content found in the supplied sources.
- **Confidence:** medium — wording is supported by preserved dated captures; single capture per state and unknown enforcement/grandfathering are the open limitations.
- **Last verified / review-by date:** Last verified 2026-08-04. Review by 2026-08-07.

## Business relevance

- **Affected ICP, segment, region, product, use case:** US midmarket IT administrators evaluating a Team-plan deployment; automation-run packaging.
- **Affected active deals, renewals, claims, assets, assumptions:** `session/existing-battlecard.md`, "Price and usage" — `Automation runs: unlimited.` That line is stale against the 2026-08-04 capture and is an affirmative claim about a competitor, so repeating it is worse than saying nothing. No specific live deal was supplied; no portfolio row exists at the CI root to match.
- **Why it matters now:** The same seller review on 7 August covers this card section; the metered wording also affects any total-cost comparison built on "unlimited".
- **Consequence of ignoring:** Sellers assert unlimited runs for a plan whose published page now states a 5,000-run allowance with per-run overage.

## Response

- **Recommended option:** reframe
- **Rationale:** Same corrective shape as the price line but a distinct proposition: replace the absolute "unlimited" assertion with the dated, scope-limited published packaging, and explicitly hold enforcement and grandfathering as unknown. No competitive counter-move is justified from one page capture.
- **Owner and decision deadline:** Alex Morgan (fictional PMM lead), by 2026-08-07 seller review.
- **Audience-specific output required:** One battlecard line, e.g. "AcmeFlow's public US pricing page listed Team as including 5,000 automation runs per month with additional runs at $0.002 each on 2026-08-04 (previously 'Unlimited automation runs' on 2026-08-03); enforcement and treatment of existing customers unknown." Route via the card-patch step. Not approved for external use.
- **Expected proximal outcome:** No seller repeats "unlimited"; run volume becomes a discovery question rather than an assumption.
- **Revisit if:** a later capture of the same US logged-out page shows different allowance wording (A/B or rollout variant), or a prospect reports Team-plan behaviour inconsistent with the published allowance.
- **Forecast:** omitted — no basis for one.

## Status

- **Human decision:** pending · decided by / date: —
- **Review status:** draft · reviewed by / date: —
- **External-use approval:** not approved · approver / date: —
- **Action status:** not started
- **Outcome observed:** —
- **Attribution:** unknown
