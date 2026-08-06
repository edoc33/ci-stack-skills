---
name: ci-pattern-check
description: >
  Decide whether a competitive objection, loss reason, or competitor mention is a real pattern or
  one loud deal. Reads exported call transcripts, CRM competitor tags, notes, and win/loss records;
  segments by stage, segment, region, and outcome; refuses to call a pattern below a stated sample
  floor. Use when the user says "is this a pattern", "are we losing to X", "one rep said", "how
  often does this come up", "pattern check", "win loss analysis", or when someone wants to change
  positioning, roadmap, or a battlecard on the strength of a single deal.
---

# Anecdote or pattern?

The fastest way to damage positioning is to rebuild it around the loudest recent deal. This skill
exists to make that harder.

**Read `reference/decision-brief.md` at the plugin root first.** Rule 3 governs this skill: one
recording is one person, and stays `field report` until an independent layer agrees.

## Step 1 — Take the evidence and describe the denominator

Ask for whatever the user can export. Anything works — CSV, transcript text, notes:

- Call transcripts or recording exports (tl;dv, Gong, Fireflies, Zoom, plain notes)
- CRM export with competitor field, stage, segment, region, amount, outcome, close date
- Win/loss records or interview notes
- Support or CS tickets where a competitor is mentioned

Then, before any analysis, establish the denominator out loud:

- How many deals or calls are in the export, over what date range?
- What fraction of the relevant universe is that? Coverage matters more than count — 12 of 15
  competitive deals is strong; 12 of 400 is a convenience sample.
- What is systematically missing? Deals with no recording, no-decision outcomes that were never
  logged, segments the export excludes, reps who do not take notes.

**Never analyse without stating the denominator.** A percentage on an unknown base is the failure
this skill prevents.

## Step 2 — Set the sample floor before looking

Commit to a threshold first, so the result cannot bend it:

- **Fewer than 5 instances** → report as `anecdote`. Name it, do not generalise it.
- **5 to 11** → report as `emerging signal`, with the segments it appeared in and the ones it did
  not. Not a positioning input yet.
- **12 or more, across at least 2 segments or 2 reps** → report as `pattern`, and still show the
  breakdown.

Never report a percentage on a base below 12. Say `4 of 7 recorded competitive deals` instead — the
raw fraction is honest where a percentage implies precision the base cannot support.

If the user pushes for a stronger label than the count supports, hold the line and say what
additional evidence would earn it.

## Step 3 — Segment before concluding

An objection that is universal and one that lives in a single segment need opposite responses. Break
the count down by:

stage · segment or company size · region · rep · deal outcome · time period · deal amount band

Look specifically for these traps and report any you find:

- **One rep, many deals.** Often a coaching or talk-track issue, not a market shift.
- **One segment only.** A qualification or packaging issue, not a positioning problem.
- **Recency skew.** All instances in the last three weeks may be a real shift or may be a reporting
  artifact — check whether recording coverage changed.
- **Outcome skew.** An objection that appears in wins as often as losses is not what lost the deals.
- **Post-hoc CRM shorthand.** A `lost to competitor` field is often a rep's shortcut. Prefer what
  the buyer said over what the field says, and say which you used.

## Step 4 — Report

Write to `patterns/YYYY-MM-DD-<slug>.md`:

1. **Verdict** — `anecdote` / `emerging signal` / `pattern`, with the raw fraction and denominator
2. **Breakdown** by the dimensions above
3. **Representative evidence** — 2 to 4 direct quotes with date, segment, and outcome. Quote, do
   not paraphrase; paraphrase is where objections drift into whatever the reader expected
4. **Competing explanations** — at least two alternatives to the obvious reading, and what would
   distinguish them
5. **Coverage limits** — what the export could not see
6. **Recommended action** — one of the seven options. `continue monitoring` is the right answer for
   most emerging signals

Print only the verdict with its fraction, the top two segments, the strongest competing explanation,
and the file path.

## Privacy and consent

- Recordings and CRM data are internal and often contain personal data. Keep analysis local, keep
  outputs internal, and say so.
- Quote customers anonymously in anything that could travel — role and segment, not name and
  company. Do not name a customer in outbound, marketing, or seller-facing material without
  documented permission.
- If the user asks for a named customer quote for external use, ask whether written permission
  exists before producing it.
- Do not analyse recordings the user does not have the right to use, and do not help identify
  individuals from anonymised data.
