---
name: ci-weekly
description: >
  Draft a competitive intelligence newsletter or executive update for a weekly, twice-monthly,
  monthly, or specified period. Joins sourced briefs, recorded decisions, and outcomes without
  upgrading draft recommendations. Accepts a Reports export as intake for triage. Scheduling,
  connector setup, and message delivery are separate workflows.
---

# Draft a competitive update

Create a concise update for a named audience, plus traceable views of ignored items and outcomes.
The skill name stays `ci-weekly`; the reporting period can be any explicit date interval.

Read the shared contract from the first available location: `${CLAUDE_PLUGIN_ROOT}/reference/decision-brief.md`,
`../../reference/decision-brief.md` relative to this skill directory, or `references/decision-brief.md`
in a standalone installation. If none exists, report the missing resource. Reuse the established
CI root and applicable internal-data authorization. Source briefs remain the source of truth.
For local output without a chosen root, resolve and show `./ci/` per the contract. Supplied files
may be outside the root; inline work needs no output directory.

## Establish the period and audience

Use the user's start date, end date, and timezone. Otherwise use the most recent complete calendar
week (Monday through Sunday) for a weekly request, the most recent complete calendar month for a
monthly request, or the
last completed half-month (days 1–15 or 16 through month-end) for a twice-monthly request. Use the
configured timezone, or state UTC if none is available. Show the exact inclusive dates before work.
Every two weeks and twice monthly are different cadences; preserve the user's chosen cadence.

Use the named audience and supplied writing rules. If none is given, draft for the internal PMM and
sales team. Read [references/first-run.md](references/first-run.md) for a fictional first run and
[references/reports-intake.md](references/reports-intake.md) when starting from an export.
Neither a provider connection nor a scheduler is required for supplied files.

## Gather only relevant material

Read `briefs/`, linked `corroborations/` and `patterns/`, `ci-portfolio.md`, and explicitly supplied
battlecard changelogs under the agreed scope. Follow canonical brief paths to join work; if a link
is absent, label the item unmatched instead of guessing. Preserve handling restrictions in the
newsletter, including any more restrictive audience limit than the source's topic suggests.

Include observations within the period and older briefs with a dated decision, resolution, or
outcome update within it. Label older observations as carried over. A file modification date is not
an event or decision date. Hold undated items out of dated claims and list the missing date.
Deduplicate repeated exports and references to the same event. Related changes that reverse an
earlier change belong in one chronological account with receipts for each state.

Raw alerts or Reports rows need triage before they become decision briefs. If `ci-triage` is
available, use it on the supplied scope and preserve its draft states. Otherwise produce an intake
list identifying the missing evidence and triage fields. Continue the update from usable briefs,
state coverage, and avoid inventing a complete period when records are missing.

## Write the update

Aim for one readable page, with detail linked to source briefs. Lead with the consequence for the
audience. A period with no supported material change can have a short update.

Include the sections supported by the corpus:

- What changed, ranked by consequence. Each item names the scope, affected team or decision, dated
  receipt, evidence basis, verification, and important uncertainty.
- Recommendations awaiting decision. Keep draft recommendations distinct from recorded decisions.
- Decisions taken. Include only a recorded `accepted` or `rejected` human decision with decision
  maker and date, plus known owner and deadline. Flag incomplete decision records.
- Deliberately not pursued. Include accepted `ignore` or `continue monitoring` decisions, their
  reasons, and revisit conditions. Recommendations to ignore remain pending until accepted.
- Still unresolved. Name what evidence would resolve the question.
- Watching next. Use the recorded portfolio or label proposed monitoring changes as proposals.

Preserve missing values and conflicting records. A blank decision field is missing, not accepted.
Zero recorded ignore decisions may reflect a quiet period, incomplete records, or the supplied
selection; it does not establish a faulty program. Do not pad the update to reach an item quota.

## Build the supporting views

Render `ci-ignore-log.md` and `ci-outcomes.md` as proposed views over the canonical briefs. Use all
available briefs for these cumulative views, while the newsletter stays within its stated period.
If only a subset is available, label the view partial and preserve the existing full view.

The ignore view records date, competitor, observation, reason, decision maker, revisit condition,
and brief path. The outcome view records date, brief path, decision, action status, owner, observed
outcome, and attribution. Existing view annotations should appear in the proposed diff for review.

Statuses and outcomes need an explicit record from the responsible person. File existence, a
battlecard proposal, or elapsed time does not prove an action happened. Report known outcomes with
`contributed`, `unclear`, or `unknown` attribution as supported. Do not infer revenue influence or
causation from a deal closing after an update. If reporting a completion rate, show completed actions
over accepted actionable decisions with known status, and report unknown-status cases separately.

## Save and hand off

For requested local files, show absolute paths first. Write a collision-safe
`<CI root>/updates/YYYY-MM-DD-competitive-update.md` with the exact period, source coverage, draft
status, handling, and linked receipts. Place full proposed view snapshots and diffs beside it as
`YYYY-MM-DD-ci-ignore-log.proposed.md` and `YYYY-MM-DD-ci-outcomes.proposed.md`. Never silently replace
fixed-name views or alter source-brief statuses. Use collision-safe names for every snapshot and
diff. If a write fails, return the draft inline.

Return the headline, distinct briefs with recorded decisions in the period (accepted and rejected
separately), pending count, accepted-ignore count, coverage limits, and file paths when saved.
For Slack, Teams, or email requests, supply a channel-ready draft within the same handling scope.
This skill does not send or schedule it. A separate authorized workflow can collect inputs on a
schedule and deliver the reviewed output.

For a specific executive question, answer that question directly with dated changes, current
interpretation, recorded response, confidence, and what would change the assessment. Keep the
same period, evidence, and approval rules.
