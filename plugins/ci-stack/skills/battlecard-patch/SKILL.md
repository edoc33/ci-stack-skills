---
name: battlecard-patch
description: >
  Turn an approved competitive brief into a redlined edit to an existing battlecard, with the dated
  source receipt inline and a freshness stamp. Produces a reviewable diff and a changelog entry —
  never publishes, never sends. Also flags claims elsewhere in the card that the new evidence has
  made stale or unsupportable. Use when the user says "update the battlecard", "patch the
  battlecard", "this needs to go in the card", "redline this", has an approved brief and wants it
  reflected in enablement content, or wants to know which existing battlecard claims are now out of
  date. For creating a battlecard from scratch, this is the wrong skill.
---

# Signal → redlined battlecard edit

Battlecards fail on trust and freshness, not on formatting. A card sellers do not believe is worse
than no card. This skill makes one narrow, sourced, dated edit at a time, and shows its work.

**Read `reference/decision-brief.md` at the plugin root first** for the evidence labels and the
language policy. Rule 6 governs this skill: nothing seller-facing ships without a named human
owner. You draft; a person approves.

## Step 1 — Require an approved brief and the current card

Ask for both:
- The brief from `/ci-triage`, or its equivalent: what changed, source, date, evidence state,
  confidence, recommended option.
- The current battlecard file, or a paste of the relevant section.

If the recommended option is `ignore` or `continue monitoring`, **stop and say so.** Not every
signal earns a card edit, and editing on a non-material change is how cards lose credibility. Offer
to log it to the ignore log for `/ci-weekly` instead.

If the brief's confidence is `low`, do not draft a seller-facing claim. Draft an internal note
instead, and say what would raise confidence.

## Step 2 — Find every place the card is now wrong

Do not only add. Search the whole card for claims the new evidence affects:

- Direct contradictions — a price, limit, or capability the card states that has changed
- Now-stale comparisons — a feature gap they have closed, or one you have
- Claims that were always weak and this change exposes — absolutes, unsourced numbers, undated
  statements
- Undated claims generally — anything a seller could repeat that has no capture date

Report these as a list before proposing any edit. Often the valuable output is a deletion.

## Step 3 — Draft the redline

Produce a unified diff against the file so the reviewer sees exactly what changes. Match the card's
existing voice, structure, and heading conventions — do not restructure the card.

Every added or edited seller-facing claim carries, inline:
- the **claim**, phrased to the language policy — what the source shows, not what you concluded
- the **source URL**
- the **date observed**
- an **evidence label** where the card has room for it

Example of the target shape:

```
- Their published mid-tier list price rose from $X to $Y
  (pricing page, observed 2026-08-04). Applies to list only —
  we have no evidence on negotiated terms.
```

Rules for the drafted copy:
- No superlatives or absolutes the evidence does not carry — no `always`, `never`, `the only`
- No estimated numbers. A range with its basis, or `unknown`
- Do not name the competitor's customers, and do not name yours without permission
- Nothing that requires a seller to assert something you labelled `inferred`
- Give sellers the honest boundary too: what we do *not* know, so they do not overreach on a call

## Step 4 — Freshness and changelog

Update or add a freshness stamp at the top of the affected section:

```
Last verified: 2026-08-06 · Reviewer: <name> · Next review: 2026-09-06
```

Append to the card's changelog, creating one if absent:

```
| date | section | change | source | evidence | reviewer |
```

Set the next-review date by volatility, not by habit: pricing and packaging on a shorter cycle than
positioning.

## Step 5 — Hand off for approval

Write the proposed version to `<cardname>.proposed.md` alongside the original. **Do not overwrite
the original.** Print:

1. The list of now-stale claims found in step 2
2. The diff
3. The one-line rationale with its source and date
4. The named reviewer and what you need from them
5. A suggested seller-facing note of two sentences maximum, for whatever channel they use

Then stop. Do not post to Slack, send email, update a CMS or wiki, or commit the change. If the
user asks you to publish, ask them to confirm the reviewer has approved it, and prefer that they
apply the change themselves.

## Sales-question mode

If the ask is an urgent answer for a seller rather than a card edit, give the answer first in three
lines — claim, source with date, what we cannot say — then offer the card patch as a follow-up. A
rep before a call needs the answer, not a process.
