---
name: ci-pattern-check
description: >
  Decide whether a competitive objection, loss reason, or competitor mention recurs across records
  or is a single case. Reads exported call transcripts, CRM competitor tags, notes, and win/loss
  records; states the denominator and coverage before concluding; separates pattern strength from
  action urgency. Use when the user says "is this a pattern", "are we losing to X", "how often does
  this come up", "pattern check", "win loss analysis", or wants to change positioning or roadmap on
  the strength of a few deals. NOT for verifying whether a single claim is true (use
  ci-corroborate).
---

# Single case, repeated signal, or scoped pattern?

The fastest way to damage positioning is to rebuild it around the loudest recent deal. This skill
exists to make that harder — without pretending small samples are worthless.

Before reading any data, read `${CLAUDE_PLUGIN_ROOT}/reference/decision-brief.md`. Two parts govern
this skill: the **internal-data preflight**, which you must run before ingesting anything, and hard
rule 3 — one report is one person. If the contract cannot be read, stop and report the missing
plugin resource.

## Step 0 — Run the internal-data preflight

Call recordings, CRM exports, and buyer notes are internal and usually contain personal data. Run
the preflight from the shared contract **before** the user uploads anything: consent for recording,
organizational authorization for AI processing, and minimisation before upload. If either
confirmation is uncertain, offer a count-only or synthetic workflow instead.

Request only the minimum fields and the narrowest date range that can answer the question.

## Step 1 — Show the mapping before analysing

"Just send whatever you have" hides most of the work. Accept CSV, transcript text, or notes — then
show the user, before any counting:

- The **record and field mapping** you inferred, and which fields you could not map
- The **cuts the data can support**, and the ones it cannot
- **Missing fields**, unmatched records, and uncoded rows
- **Duplicates** — three calls about one opportunity is one case, not three

Do not report prevalence across deals unless records can be deduplicated to one independent case:
normally one deal, one account episode, or one buyer interview.

Then state the denominator out loud:

- How many eligible records, over what date range?
- What fraction of the relevant universe is that? Coverage matters more than count — 12 of 15
  competitive deals is strong; 12 of 400 is a convenience sample.
- What is systematically missing? Deals with no recording, no-decision outcomes never logged,
  segments the export excludes, reps who do not take notes.

**Never analyse without stating the denominator.** A percentage on an unknown base is the specific
failure this skill exists to prevent.

## Step 2 — Define the analysis rule before counting

Commit before you look, so the result cannot bend the rule. Define one independent case, the
eligible records and date range, the inclusion, exclusion and deduplication rules, the coverage, and
the decision this evidence may affect. Then report one of:

- **`single case`** — one independent occurrence. Name it; do not generalise from it.
- **`repeated signal`** — more than one independent occurrence, but coverage, sampling, missingness,
  independence, or concentration does not support a scoped pattern claim.
- **`scoped pattern in <defined cohort>`** — the predeclared rule is met in a deduplicated cohort
  with a known denominator and adequate coverage, and the result is not an artifact of one rep,
  repeated calls about one deal, or a short window. **No universal count earns this label** — a
  cohort must be named.

Always lead with the raw fraction and base — `4 of 7 eligible recorded competitive deals`. Coverage
and limits come next. A percentage may follow when genuinely useful, but never without `k/n`.

**Pattern strength and action urgency are separate judgements.** A small but severe signal can
justify `validate` or a reversible segment-specific action. A large convenience sample may not
justify company-wide repositioning. Say which you are recommending and why.

A population-prevalence claim needs a sampling plan and an uncertainty interval — not a bigger
number. If the user wants one, say what it would take.

## Step 3 — Segment before concluding

An objection that is universal and one confined to a single segment need opposite responses. Break
down by: stage · segment or company size · region · rep · outcome · time period · deal amount band.

Report any of these traps you find:

- **One rep, many deals.** Usually a coaching or talk-track issue, not a market shift.
- **One segment only.** A qualification or packaging issue — and a legitimate scoped pattern, not a
  disqualified one. Name the cohort.
- **Recency skew.** All instances in three weeks may be a real shift or a reporting artifact — check
  whether recording coverage changed.
- **Outcome skew.** An objection appearing in wins as often as losses is not what lost the deals.
- **Post-hoc CRM shorthand.** A `lost to competitor` field is often a rep's shortcut. Prefer what the
  buyer said over what the field says, and state which you used.

## Step 4 — Report

Per the file-safety rule: confirm the directory, show paths, never overwrite. Write to
`patterns/YYYY-MM-DD-<slug>.md`:

1. **Verdict** — with the raw fraction, the denominator, and the named cohort if scoped
2. **Breakdown** by the dimensions above
3. **Representative evidence** — 2 to 4 direct quotes with date, segment, and outcome. Quote, do not
   paraphrase; paraphrase is where objections drift into whatever the reader expected
4. **Competing explanations** — at least two alternatives to the obvious reading, and what would
   distinguish them
5. **Coverage limits** — what the export could not see
6. **Recommended action** — one of the seven options, with pattern strength and urgency stated
   separately

Print only the verdict with its fraction, the top two segments, the strongest competing explanation,
and the file path.

## Handling and privacy

- Outputs from this skill are `internal` handling by default, and `restricted` if they contain
  identifiable individuals. Mark them.
- Quote customers anonymously in anything that could travel — role and segment, not name and
  company. Do not name a customer in outbound, marketing, or seller-facing material without
  documented permission; ask whether it exists before producing such a quote.
- Do not help re-identify individuals from anonymised data.
- Do not analyse recordings the user does not have the right to use.
