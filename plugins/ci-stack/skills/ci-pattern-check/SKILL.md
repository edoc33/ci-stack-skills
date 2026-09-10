---
name: ci-pattern-check
description: >
  Assess whether a competitive objection, loss reason, or competitor mention recurs across an
  exported cohort of calls, CRM records, or buyer notes. Deduplicates cases and reports denominators,
  coverage, and competing explanations. Use for pattern checks and scoped win/loss analysis;
  verifying one claim or tagging live CRM opportunities requires a different workflow.
---

# Check a competitive pattern

Answer a specific question about a defined set of deals or interviews, with the count and its limits
visible. This skill reads supplied records and writes a draft analysis.

Read the shared contract from the first available location: `${CLAUDE_PLUGIN_ROOT}/reference/decision-brief.md`,
`../../reference/decision-brief.md` relative to this skill directory, or `references/decision-brief.md`
in a standalone installation. If none exists, report the missing resource and stop analysis. Apply its internal-data
preflight before reading real transcripts, CRM exports, or buyer notes. Reuse applicable session
authorization and the established CI root. Synthetic and already aggregated examples can be used
when real data is unavailable. Supplied files may be outside the root. For local output without a
chosen root, resolve and show `./ci/` per the contract; inline work needs no output directory.

## Start with a question and a cohort

Minimum inputs: the question to test and permitted CSV, transcript text, or notes. Use the requested
time window, or state the dates covered by the supplied export. With undated records, limit the
answer to the undated supplied cohort and avoid time-based conclusions.
A stable deal, account-episode, or interview ID is needed to count independent cases. Useful fields
include date, competitor, speaker, quote or note, source locator, outcome, segment, rep, and stage.
Accept equivalent field names and report the mapping. Do not require fields the question does not use.

For a small fictional CSV and a runnable prompt, read
[references/first-run.md](references/first-run.md). No live provider connection is needed.

## Define the rule before tallying

Inspect headers and context first. Before counting occurrences, state the independent unit, eligible
dates and records, inclusion and exclusion rules, deduplication key, expected coverage, and the
decision at stake. State what evidence would justify a scoped-pattern conclusion for this decision.
Choose a conservative rule when the user has no existing one; do not require them to design a test.
If counts were already supplied, disclose that the rule was declared after seeing them.

For competitor mentions, distinguish active buyer evaluation, incumbent use, historical evaluation,
explicit rejection, hypothetical references, and seller-only mentions. Count only categories that
answer the question. A transcript proves that someone said something; their product assertion
remains a field report.

Normalize duplicate exports and repeated calls to one case. Keep a traceable case-to-record mapping.
With missing IDs, deduplicate only where a supplied mapping supports it. Otherwise report record
counts and an unknown independent-case denominator; do not report deal prevalence.

## Count with coverage intact

Report eligible independent cases, observed matches, excluded cases, unknown or uncoded cases, and
duplicate rows removed. A blank competitor or outcome field is unknown unless the input convention
explicitly says it means none. Explain the denominator used for every fraction.

Separate `matches / observed eligible cases` from `observed eligible cases / relevant universe`.
Use `coverage: unknown` when the universe is unavailable. A competitor-filtered export can describe
its selected cases but cannot establish that competitor's share of all deals. A loss-only export
cannot estimate win rate or explain what distinguishes wins from losses.

Use the verdict supported by the data:

| Verdict | When to use it |
|---|---|
| `insufficient data` | No eligible cases, unknown independence, or missing fields prevent the requested comparison |
| `not observed in supplied cohort` | Zero observed occurrences in an analyzable cohort; state missingness and avoid a broader absence claim |
| `single case` | One independent occurrence |
| `repeated signal` | Multiple independent occurrences with coverage, concentration, or sampling limits |
| `scoped pattern in <cohort>` | The declared evidence rule is met in a named, deduplicated cohort with sufficient coverage for the decision |

No fixed count earns a pattern label. Lead with the raw fraction where a valid denominator exists.
Separate pattern strength from urgency: a single severe case can justify validation or a reversible
action while broader positioning changes need broader evidence.

## Check alternative explanations

Use available cuts such as segment, rep, outcome, region, stage, and period. Name unsupported cuts
instead of inventing them. Check whether repeated calls, one rep's assignments, recent logging
changes, or missing outcomes explain the concentration. One rep's concentration alone does not
establish a coaching problem. An objection occurring in both wins and losses does not establish
loss causation. Prefer the buyer's words when CRM shorthand conflicts with a transcript and retain
the conflict in the record.

Population estimates require a suitable sampling design and uncertainty assessment. Label supplied
export fractions as descriptive. Avoid percentages whose denominator is unknown or reconstructed
from the outcome being tested.

## Save the analysis

For requested local files, show the absolute path and write a new collision-safe record at
`<CI root>/patterns/YYYY-MM-DD-<question-slug>.md`. Include the rule and field mapping, verdict,
fractions and coverage, available breakdowns, case-to-source receipts, unknowns, competing
explanations, and one of the shared contract's seven recommended options. Link the canonical brief
path when one exists. Keep direct quotes exact and cited; if only CRM codes exist, label them as
codes and do not invent quotes. Include as many examples as the evidence warrants.

Record the exact proposition with its evidence basis, verification, confidence, and reason.
Use the shared status fields with `Human decision: pending`, `Review status: draft`, and
`External-use approval: not approved`. Handling is at least `internal`, or `restricted` when
identifiable people are present. Use role and segment in portable summaries; preserve any authorized
identity mapping only in the restricted source. Do not try to re-identify anonymized records.

Return the verdict, fraction or denominator limitation, recommended next action, and path when saved.
If writing fails, return the draft inline. `ci-weekly` can summarize the saved analysis;
`ci-call-mentions` can draft context for individual mentions. Live listening, CRM tagging, delivery,
and scheduling require separately configured connectors and authorization.
