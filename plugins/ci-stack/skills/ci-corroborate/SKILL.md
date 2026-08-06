---
name: ci-corroborate
description: >
  Test a competitive claim against multiple independent evidence layers and return corroborated,
  contradicted, or unresolved — never a forced verdict. Reconciles competitor-published pages,
  documentation and changelogs, call transcripts and field notes, third-party sources, and your own
  product testing. Enforces that absence of evidence is not disproof. Use when the user asks "is
  this true", "can we say this publicly", "verify this claim", "a rep told me X", "corroborate",
  "can we put this in a battlecard", or when a claim is about to go in front of a customer,
  prospect, analyst, or exec and needs to survive challenge.
---

# Claim vs. evidence triangulation

One source is a lead, not a finding. This skill takes a claim and reports what the available
evidence actually supports — including, often, that it is unresolved.

**Read `reference/decision-brief.md` at the plugin root first** for the four evidence labels and
the hard rules. Rule 1 governs this skill: absence is not disproof.

## Step 1 — State the claim precisely

Restate it as one falsifiable sentence before testing anything. Vague claims cannot be
corroborated, and the restatement is often where the work happens.

- Not `Acme is cheaper` → `Acme's published mid-tier list price is below ours for a 10-seat team`
- Not `they do not have SSO` → `Acme's documentation does not describe SAML SSO as of 2026-08-06`
- Not `they are moving upmarket` → `Acme's positioning pages and job postings emphasise enterprise
  buyers more than they did 12 months ago`

Note who made the claim and how it reached the user — a seller, a prospect, a competitor's own
marketing, a rumour. Provenance changes the starting label.

## Step 2 — Test each layer independently

Check every layer that can speak to the claim. Record what each one shows and, explicitly, what it
cannot establish. Do not let a strong signal in one layer suppress a check in another.

| Layer | Where | Establishes | Blind to |
|---|---|---|---|
| Competitor-published | pricing, docs, changelog, terms, press | what they claim and publish, dated | reality behind the claim, private terms |
| Product experience | your own trial or test, where permitted | what it actually does | other segments, other configurations |
| Third-party | reviews, analysts, filings, communities, job posts | outside validation, direction, sentiment | intent, causation |
| Internal field | call recordings, seller and CS notes, CRM, RFPs | what appears in deals and how they sell | unbiased buyer view; one deal is one deal |
| Direct buyer | win/loss, churn and renewal interviews | decision criteria and why an outcome happened | prevalence without a sampling plan |

For each layer, write one line: source, date, what it shows, label from the four
(`observed` / `field report` / `corroborated` / `inferred`).

## Step 3 — Return one of three verdicts

**`corroborated`** — two or more independent layers agree. Name both, with dates. One layer twice
is not two layers: a competitor's pricing page and their pricing FAQ are the same layer.

**`contradicted`** — a layer directly shows the opposite. Requires positive contrary evidence, not
missing evidence.

**`unresolved`** — everything else, and this is a legitimate, common, useful answer. Use it when
layers disagree, when only one layer speaks, when evidence is stale, or when the claim concerns
something no public source can see.

Then state, in one line each:
- **What would resolve it** — the specific evidence needed, and which layer would carry it
- **What may be said now** — the strongest defensible phrasing, ready to use
- **What must not be said** — the overclaim someone will reach for

## The absence rule, stated for the user

If the claim is about something a public page cannot show, say this explicitly rather than reporting
`contradicted`:

> Their pricing page does not list a discount for annual commitments. That is not evidence they
> do not offer one — negotiated terms are not published. This is unresolved, and the layer that
> would resolve it is field evidence from a deal where it was offered.

The same applies to unreleased capability, private beta features, and anything behind a login.

## Step 4 — Emit

Append the verdict to the source brief if one exists, and write a standalone record to
`corroborations/YYYY-MM-DD-<slug>.md` containing the claim, the per-layer table, the verdict, the
resolving evidence, and the approved phrasing.

Print only: the verdict, the two strongest sources with dates, the approved phrasing, and the file
path.

## Refusals

Do not corroborate by asking anyone to bypass a paywall, use a competitor's login, misrepresent
identity to obtain a demo or quote, contact a competitor's employees under false pretences, or
scrape against a site's terms. If that is the only route, report `unresolved` and say the claim
cannot be verified through legitimate means.

Do not manufacture corroboration from two restatements of the same original source. Trace each
layer to its origin — a news article quoting a press release is the press release.
