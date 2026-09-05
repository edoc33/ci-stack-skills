# Brief — AcmeFlow SSO plan availability

ILLUSTRATIVE / FICTIONAL WORKSHOP OUTPUT. Competitor, buyer, dates and evidence are synthetic.

Sibling briefs from the same capture pair (one event, three propositions):
`./2026-08-06-acmeflow-team-price.md` · `./2026-08-06-acmeflow-team-usage.md`

## Event

- **Competitor / alternative:** AcmeFlow (fictional)
- **Observed change:** On the Team plan block, `SAML SSO available on Enterprise only.` was replaced by `SAML SSO available on all paid plans.`
- **First observed / effective date:** First observed in the after-capture of 2026-08-04T09:12:44Z. Effective date unknown — the page was not captured between 2026-08-03T09:12:44Z and 2026-08-04T09:12:44Z.
- **Source locator and preserved evidence:** `https://www.acmeflow.example/pricing`, US public page, USD, Team plan, annual billing, logged out. Preserved: `evidence/pricing-before.txt` (2026-08-03T09:12:44Z), `evidence/pricing-after.txt` (2026-08-04T09:12:44Z), normalized event `evidence/change-event.json`. Both quoted strings verified word-for-word against the preserved captures. Manifest lists sha256 per file. No authenticated or token-bearing link was present in the supplied payload; none is recorded.

## Evidence

- **Proposition (exact, scope-limited):** The public, logged-out US AcmeFlow pricing page displayed the sentence `SAML SSO available on all paid plans.` in the Team block at 2026-08-04T09:12:44Z, replacing `SAML SSO available on Enterprise only.` present at 2026-08-03T09:12:44Z.
- **Evidence basis:** observed (page publication only)
- **Verification:** single-source — one page, one capture per state
- **Handling:** public (public page text); this brief is internal
- **Counterevidence / unknowns:**
  - The published sentence is broad ("all paid plans"). It is *not* the same proposition as "SAML browser sign-in with Okta works on the Team plan in a US workspace." Nothing supplied tests working behaviour: no docs page, admin console, or hands-on test has been read for this brief.
  - Capture alternatives — A/B variant: **not tested** (one capture of each state cannot rule this out); personalisation / cookie state: **not tested**; locale or currency variation: **not tested** (US/USD only); plan or account variation: **not tested** (logged out only); template or navigation change: **plausible but not the explanation** — the surrounding lines changed substantively in the same block, so this is not a chrome-only edit; campaign rotation: **not tested**. None is ruled out.
  - The supplied `tool_generated_summary` ("An enterprise-only SSO note was removed from the plan comparison") and `tool_importance_flag: "true"` are input hypotheses, not findings. The raw text goes further than the summary: a note was not merely removed, an affirmative broader claim was added. Raw text governs.
  - Removal of the Enterprise-only wording does not disprove any plan restriction that may still exist in product; absence is not disproof.
  - No prompt-injection or instruction-like content was found in the supplied sources.
- **Confidence:** medium — the exact quoted wording is supported by a preserved dated capture, but one capture per state leaves A/B and personalisation untested, and the page-level claim does not reach the Team/Okta behaviour the decision needs.
- **Last verified / review-by date:** Last verified 2026-08-04. Review by 2026-08-07.

## Business relevance

- **Affected ICP, segment, region, product, use case:** IT administrators at US midmarket organizations evaluating a TaskBridge Team-plan deployment with Okta; SAML browser sign-in. SCIM, other identity providers, other paid plans, negotiated terms and reliability are out of scope.
- **Affected active deals, renewals, claims, assets, assumptions:** `session/existing-battlecard.md`, "SSO qualification" section — the claim `AcmeFlow restricts SAML SSO to Enterprise.` and the follow-on question about upgrading for SSO. No specific live deal was supplied.
- **Why it matters now:** This is the named decision for the fictional 7 August seller review — retain or replace that line.
- **Consequence of ignoring:** Sellers repeat a plan restriction that the current published page contradicts, in front of exactly the buyer the card targets.

## Response

- **Recommended option:** validate
- **Rationale:** The change-of-mind threshold in business-context.md requires a current source *plus* scope-matched independent product evidence. One page capture meets the first half only. Validate the Team/Okta behaviour before rewriting seller guidance; meanwhile the existing line should not be repeated as stated.
- **Owner and decision deadline:** Alex Morgan (fictional PMM lead), by 2026-08-07 seller review. Technical check: Workshop tester A.
- **Audience-specific output required:** One interim seller line for the 7 August review — that AcmeFlow's published pricing page stated on 2026-08-04 that SAML SSO is available on all paid plans, that Team/Okta behaviour is unverified, and that the Enterprise-only claim should be dropped from live conversations pending verification. Not approved for external use.
- **Expected proximal outcome:** A scope-matched verdict on Team + Okta SAML sign-in in time for the review.
- **Revisit if:** a second independent capture shows different Team SSO wording (indicating an A/B variant), or product-level evidence contradicts the published sentence.

## Status

- **Human decision:** pending · decided by / date: —
- **Review status:** draft · reviewed by / date: —
- **External-use approval:** not approved · approver / date: —
- **Action status:** not started
- **Outcome observed:** —
- **Attribution:** unknown
