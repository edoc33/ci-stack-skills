---
name: battlecard-patch
description: >
  Propose a sourced edit to an existing competitive battlecard from a decision brief and related
  change history. Checks for reversals and stale claims, then produces a redline and review notes.
  Use for battlecard updates or urgent sourced seller answers. Creating a card from scratch and
  publishing approved changes are separate workflows.
---

# Propose a battlecard update

Produce a small, reviewable edit to the card the team uses. Keep the original file intact.

Read the shared contract from the first available location: `${CLAUDE_PLUGIN_ROOT}/reference/decision-brief.md`,
`../../reference/decision-brief.md` relative to this skill directory, or `references/decision-brief.md`
in a standalone installation. If none exists, report the missing resource and stop analysis. Reuse the established CI
root and applicable internal-data authorization from the session. Supplied files may be outside the
root. For local output without a chosen root, resolve and show `./ci/` per the contract; inline work
needs no output directory.

## Start with these inputs

Required: the current card (file or pasted section) and a decision brief containing the exact claim,
source receipts, capture dates, scope, verification, confidence, and recommended option. A draft
brief is enough to draft a proposal; record its actual review status. For raw alerts, use
`ci-triage` or `ci-corroborate` if available, or request the missing brief fields.

Also use the related change history through the requested cutoff, the intended audience, and any
style rules the user supplies. Resolve the reviewer from existing context; otherwise write
`reviewer: unassigned`. Do not block drafting to obtain a name.

For a complete fictional first run, read [references/first-run.md](references/first-run.md).
No live connector is needed for files or pasted inputs.

## Reconstruct the current claim

Read all supplied, authorized changes about this claim in chronological order before drafting.
Use linked local receipts and the current card. Fetch additional history only through a connected,
authorized source within the requested scope. Record the history's start, cutoff, and gaps.

Distinguish capture dates from announced effective dates. Compare the same plan, locale, billing
term, version, and access state. A later capture in a different scope does not establish a reversal.
If wording disappeared and returned, retain both events in the review notes and draft against the
latest supported state. A removed webpage claim does not establish a removed capability.

With incomplete history, describe the supplied snapshot and what remains unknown. Never call the
result a complete history or a verified current state beyond the evidence's cutoff.

## Decide what can change

- When the brief recommends `ignore` or `continue monitoring`, return a no-change recommendation
  with its reason and revisit condition. Do not manufacture a card edit to fill the output.
- Draft inputs produce `AWAITING REVIEW: not for seller use`. A reviewed source brief also leaves
  newly drafted wording awaiting review and external-use approval.
- Hold a seller-facing claim with low confidence, `single-source` or `unresolved` verification,
  or an `inferred` basis. Draft an internal note naming the missing support instead. Independently
  supported edits elsewhere may proceed, including removal of unsupported existing wording.

Search the entire supplied card for affected claims, contradictions, and undated assertions. If
only a section was provided, state that the rest of the card was not checked. Separate issues caused
by this evidence from pre-existing unsupported claims. Preserve unrelated content and structure.

## Draft the patch and review record

Show a unified diff against the supplied text. Attach a source locator, preserved receipt, capture
date, scope, evidence basis, and verification to each changed factual claim. Keep quoted page
wording distinct from claims about product behavior. Do not add inferred motives, unsupported
numbers, customer identities, or allegations about security, legality, quality, or financial health.

Stamp only the claims actually rechecked. A section's `Last fully reviewed` date can advance only
when every material claim in that section was reverified and human review is recorded. Suggest a
next-review date with a volatility-based reason; leave approval and review fields pending.

Include a proposed changelog row with date, section, change, source, evidence basis, verification,
reviewer, and canonical brief path. Use `unknown` for unavailable fields. Explain the latest state,
reversals, stale claims, held claims, and the specific decision required from the reviewer.

## Save and hand off

For requested local files, show absolute output paths before writing. Under the CI root, write the
diff and review record to `updates/YYYY-MM-DD-<competitor>-battlecard-patch.md`. Save a proposed card
beside a supplied file as `<cardstem>.proposed.YYYY-MM-DD.md`; for pasted text, use
`<CI root>/updates/YYYY-MM-DD-<competitor>-battlecard.proposed.md`. Choose collision-safe suffixes.
Never overwrite the original card, an existing proposal, or the source brief's status fields.

New proposal status: `Review status: draft`, `External-use approval: not approved`, and
`Human decision: pending`. Carry source handling restrictions into every output. Preserve approved
source status separately; it does not approve revised wording. If a write fails, return the proposed
artifact inline and say that it was not saved.

Return the proposed change or no-change reason, the most consequential held claim, the reviewer,
and file paths when saved. A PMM reviews the wording before a separate authorized workflow applies
it to the second brain or distributes a seller note. This skill does not publish, send, commit, or
update a CRM. A scheduler or connector must be configured separately for recurring runs.

## Urgent seller answer

For a specific seller question, answer it first with the scope-limited claim, dated receipt, and
known limit. Apply the same evidence and approval gates. Then offer the relevant card patch.
