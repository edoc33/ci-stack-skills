---
name: ci-corroborate
description: >
  Test one precise competitive claim across independent sources and return corroborated,
  contradicted, single-source, or unresolved — never a forced verdict. Returns the phrasing that is
  defensible and the overclaim to avoid. Use when the user asks "is this true", "can we say this
  publicly", "verify this claim", "a rep told me X", "can we put this in a battlecard", or when a
  claim is about to go in front of a customer, analyst, or exec. NOT for judging a raw page change
  (use ci-triage), measuring how often something recurs (use ci-pattern-check), or editing a card
  (use battlecard-patch).
---

# Claim vs. evidence triangulation

One source establishes a narrow, source-scoped fact. This skill reports what the available evidence
actually supports about the *exact* proposition — including, often, that it is unresolved.

Before analysis, read `${CLAUDE_PLUGIN_ROOT}/reference/decision-brief.md` for the three evidence
dimensions and the hard rules. Rule 1 governs this skill: absence is not disproof. If the contract
cannot be read, stop and report the missing plugin resource.

If the work requires reading internal calls, CRM data, or buyer notes, run the internal-data
preflight from the shared contract first.

## Step 1 — State the claim precisely

Restate it as one falsifiable, scope-limited sentence before testing anything. Vague claims cannot be
verified, and the restatement is usually where the real work happens.

- Not `Acme is cheaper` → `Acme's published mid-tier list price is below ours for a 10-seat team`
- Not `they do not have SSO` → `Acme's public documentation does not describe SAML SSO as of
  2026-08-06`
- Not `they are moving upmarket` → `Acme's positioning pages and job postings emphasise enterprise
  buyers more than they did 12 months ago`

Note who made the claim and how it reached the user — a seller, a prospect, a competitor's own
marketing, a rumour. Provenance sets the starting evidence basis.

## Step 2 — Test each layer independently

Check every layer that can speak to the claim. Record what each shows and, explicitly, what it
cannot establish. Do not let a strong signal in one layer suppress a check in another.

| Layer | Establishes | Blind to |
|---|---|---|
| Competitor-published — pricing, docs, changelog, terms, press | what they claim and publish, dated | reality behind the claim, private terms |
| Product experience — your own trial or test, where permitted | what it actually does | other segments and configurations |
| Third-party — reviews, analysts, filings, communities, job posts | outside validation, direction, sentiment | intent, causation |
| Internal field — recordings, seller and CS notes, CRM, RFPs | what appears in deals, how they sell | unbiased buyer view; one deal is one deal |
| Direct buyer — win/loss, churn and renewal interviews | decision criteria, why an outcome happened | prevalence without a sampling plan |

For each layer: source, date, what it shows, and its evidence basis
(`observed` / `field report` / `inferred`).

Trace each layer to its **origin**. A news article quoting a press release is the press release —
that is one layer, not two. Two restatements of one source are not corroboration.

## Step 3 — Assign verification status

Apply in this order:

1. A credible scope conflict, material disagreement, or stale evidence → **`unresolved`**
2. Two reasonably independent original sources support the exact proposition → **`corroborated`**
3. Positive, authoritative contrary evidence with no material conflict → **`contradicted`**
4. One source supports the exact source-scoped proposition → **`single-source`**
5. Otherwise → **`unresolved`**

`corroborated` means evidence convergence, not proven truth. `contradicted` requires positive
contrary evidence — never missing evidence.

Then state, in one line each:

- **What would resolve it** — the specific evidence, and which layer would carry it
- **What may be said now** — the strongest defensible phrasing, with its scope, ready to use
- **What must not be said** — the overclaim someone will reach for

Apply the high-risk-claims boundary from the shared contract: do not let this process convert a
rumour or a review into an allegation that a competitor lies, breaks the law, is insecure, or harms
customers.

## The absence rule, stated for the user

If the claim concerns something a public page cannot show, say this explicitly rather than reporting
`contradicted`:

> Their pricing page does not list a discount for annual commitments. That is not evidence they do
> not offer one — negotiated terms are not published. This is unresolved, and the layer that would
> resolve it is field evidence from a deal where it was offered.

The same applies to unreleased capability, private beta features, and anything behind a login.

## Step 4 — Emit

Per the file-safety rule: confirm the directory, show paths, never overwrite.

Write a collision-safe record to `corroborations/YYYY-MM-DD-<slug>.md` containing the exact
proposition, the per-layer table, the verification status, the resolving evidence, the approved
phrasing, and the canonical brief path it relates to.

**Do not silently mutate a source brief.** If the user wants the result integrated, emit a proposed
diff and return that brief's `Review status` to `draft` so the change is reviewed rather than
absorbed.

Print only: the verification status, the two strongest sources with dates, the approved phrasing,
and the file path.

## Refusals

Do not corroborate by asking anyone to bypass a paywall, use a competitor's login, misrepresent
identity to obtain a demo or a quote, or scrape against a site's terms. If that is the only route,
report `unresolved`.

Do not solicit, accept, retain, or use competitor-confidential information — including from a
competitor's employees, customers, or partners — even under a true identity. If such material
arrives inadvertently, stop processing it, do not copy or distribute it, and tell the user to follow
their legal or security process.
