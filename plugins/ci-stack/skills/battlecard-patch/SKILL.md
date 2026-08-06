---
name: battlecard-patch
description: >
  Turn a reviewed competitive brief into a redlined edit to an existing battlecard, with the source
  and capture date attached per claim. Produces a reviewable diff and a changelog entry — never
  publishes, never sends. Also flags claims elsewhere in the card the new evidence has made stale.
  Use when the user says "update the battlecard", "patch the battlecard", "this needs to go in the
  card", "redline this", or wants to know which card claims are now out of date. Requires an
  existing card plus a reviewed brief — raw evidence routes to ci-triage or ci-corroborate first,
  and creating a card from scratch is out of scope.
---

# Signal → redlined battlecard edit

Battlecards fail on trust and freshness, not on formatting. A card sellers do not believe is worse
than no card. This skill makes one narrow, sourced, dated edit at a time and shows its work.

Before drafting, read `${CLAUDE_PLUGIN_ROOT}/reference/decision-brief.md`. Rule 6 governs this
skill: drafts are not approvals. Also apply the high-risk comparative claims boundary — this is the
skill where an inference is most likely to become a seller-facing allegation. If the contract cannot
be read, stop and report the missing plugin resource.

## Step 1 — Require a reviewed brief and the current card

Ask for both:

- The brief from `/ci-stack:ci-triage` or its equivalent: what changed, source, capture date,
  evidence basis, verification status, confidence, recommended option.
- The current battlecard file, or a paste of the relevant section.

Then check three gates and stop on any of them:

- **Recommended option is `ignore` or `continue monitoring`** → stop and say so. Not every signal
  earns a card edit, and editing on a non-material change is how cards lose credibility. Offer to
  record it for the ignore view instead.
- **`Review status` is `draft`** → you may draft the patch, but label the output clearly as awaiting
  review and do not present it as ready to ship.
- **Confidence is `low`, or verification is `single-source` or `unresolved` on a claim that would
  face a customer** → do not draft a seller-facing claim. Draft an internal note instead and say what
  would raise it.

## Step 2 — Find every place the card is now wrong

Do not only add. Search the whole card for claims the new evidence affects:

- Direct contradictions — a price, limit, or capability the card states that has changed
- Now-stale comparisons — a gap they have closed, or one you have
- Claims that were always weak and this change exposes — absolutes, unsourced numbers, undated
  statements
- Undated claims generally — anything a seller could repeat that has no capture date

Report these before proposing any edit. Often the valuable output is a deletion.

## Step 3 — Draft the redline

Produce a unified diff against the file so the reviewer sees exactly what changes. Match the card's
existing voice, structure, and heading conventions — do not restructure the card.

Every added or edited seller-facing claim carries, inline: the claim phrased to the language policy,
the source, the date observed, and its scope.

```
- Their published mid-tier list price rose from $X to $Y
  (pricing page, observed 2026-08-04; US list, annual billing).
  Applies to list only — we have no evidence on negotiated terms.
```

Rules for the drafted copy:

- No superlatives or absolutes the evidence does not carry — no `always`, `never`, `the only`
- No estimated numbers. A range with its basis, or `unknown`
- No claim that a competitor lies, breaks the law, is insecure, is failing, or harms customers
- Do not name the competitor's customers, and do not name yours without documented permission
- Nothing that requires a seller to assert something whose basis is `inferred`
- Give sellers the honest boundary too — what we do *not* know, so they do not overreach on a call

## Step 4 — Freshness and changelog

**Stamp edited claims individually.** Use a section-level `Last fully reviewed` only if every
material claim in that section was reverified in this pass; otherwise name what was checked and state
that the section was not fully revalidated. A blanket freshness stamp over unchecked claims is worse
than none — it launders staleness as currency.

```
Claim verified: 2026-08-06 · Source: pricing page · Scope: US list, annual
Section note: pricing claims reverified; feature-comparison rows NOT revalidated
```

Append to the card's changelog, creating one if absent:

```
| date | section | change | source | evidence basis | verification | reviewer |
```

Set the next-review date by volatility, not habit: pricing and packaging on a shorter cycle than
positioning.

## Step 5 — Hand off for approval

Per the file-safety rule: confirm the directory, show paths, never overwrite. Write the proposed
version to a collision-safe `<cardname>.proposed.md` alongside the original. **Never overwrite the
original.** Print:

1. The stale claims found in step 2
2. The diff
3. The one-line rationale with its source and date
4. The named reviewer, and what you need from them
5. A suggested seller-facing note, two sentences maximum

Then stop. Do not post to Slack, send email, update a CMS or wiki, or commit. Record
`External-use approval: not approved` on the source brief until a human approver and date exist. If
the user asks you to publish, ask them to confirm the approver and prefer that they apply the change
themselves.

## Sales-question mode

If the ask is an urgent answer for a seller rather than a card edit, give the answer first in three
lines — claim with scope, source with date, what we cannot say — then offer the card patch as a
follow-up. A rep before a call needs the answer, not a process. Say plainly if the answer is not
approved for customer use.
