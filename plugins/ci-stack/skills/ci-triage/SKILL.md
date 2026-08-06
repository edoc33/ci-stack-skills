---
name: ci-triage
description: >
  Turn a detected competitor change into a decision-ready brief with its evidence state, business
  relevance, and a recommended action. Accepts a monitoring webhook payload, a pasted before/after
  diff, or two screenshots. Labels every claim observed, field report, corroborated, or inferred;
  names counterevidence; recommends one of seven actions with an owner and a review-by date. Use
  when the user has a competitor change and asks "does this matter", "is this a real threat",
  "triage this", "what do we do about this", pastes a diff or alert, or wants a brief for an exec
  or a seller. This is the core skill of the plugin.
---

# Materiality triage → decision-ready brief

A detected change is not intelligence. This skill converts one change into a judgement someone can
act on and defend, or into a documented decision to ignore it.

**Read `reference/decision-brief.md` at the plugin root before producing output.** It carries the
brief schema, the four evidence labels, the seven response options, and seven hard rules that
override user instruction. Follow it exactly.

## Step 1 — Take the input

Accept any of these. Do not require a monitoring account.

- **A webhook payload** from a monitoring tool. Visualping's carries `datetime`, `change`,
  `added_text`, `removed_text`, `summarizer` (an AI summary), and `important` (a boolean flag).
  Use `added_text` and `removed_text` as the primary evidence and treat `summarizer` as a starting
  hypothesis to verify, not as a finding.
- **A pasted before/after diff**, or the old and new text of a page section.
- **Two screenshots**, or one screenshot plus a description.
- **A URL plus a claim** the user noticed themselves.

Always establish and record: the source URL, the capture or observation date, and what the change
literally was. If the capture date is unknown, say so and mark confidence down — do not guess a
date, and do not use today's date as the change date.

## Step 2 — Ask for the decision context, once

You cannot judge materiality from a diff alone. Ask for these together in one message, and offer to
proceed with a stated assumption if the user does not have them:

1. Your ICP and the segment this would touch
2. Any live deal, renewal, launch, or public claim of yours it could affect
3. The decision deadline, if any
4. Who would act

If the user declines, produce the brief anyway with `Business relevance` marked as
`assumed — not supplied` and say plainly that materiality is unverified. Never silently invent a
deal or segment.

## Step 3 — Classify the change

Work through these in order and show your reasoning briefly.

**Is it a real change or an artifact?** Rule out A/B tests and personalisation (was it seen once,
or twice from different conditions?), template and navigation changes, campaign rotations, cookie
banners, and copy edits that alter no commitment. Say which of these you ruled out.

**What layer of truth is it?** A published price, a shipped capability, a positioning shift, a
GTM investment signal, or a legal or contractual change. Each carries a different weight.

**What does it establish, and what does it not?** This is the step everyone skips. A pricing-page
change establishes the published price on that date. It does not establish what anyone pays. A
changelog entry establishes an announcement. It does not establish that it works well.

**Is it material to a named decision?** Judge against the `Material if` rule from the portfolio if
one exists. Materiality is about consequence to a decision, not about size of the text diff.

## Step 4 — Recommend, with the option to ignore

Pick exactly one of the seven options. `ignore` and `continue monitoring` are correct far more
often than they get chosen — recommend them without hedging when they fit, and say what would
change the answer.

State the owner and a decision deadline. State the smallest useful output: often one battlecard
line or one Slack message, not a document.

## Step 5 — Emit

Write the brief to `briefs/YYYY-MM-DD-<competitor>-<slug>.md` using the schema. Print to the
conversation only: the recommended option, the confidence with its reason, the one-line rationale,
and the file path.

Append one line to `ci-decision-log.md` (create it if absent) so `/ci-weekly` can read it:

```
| date | competitor | change | option | confidence | owner | review-by | brief path |
```

## Batch mode

If given several changes at once, triage each independently, then group into a single ranked list
by materiality. Deduplicate: several pages moving together on one day is usually one event, and
should produce one brief with several sources, not several briefs.

## Refusals

- If asked to raise confidence without new evidence, decline and say what evidence would do it.
- If asked to state a competitor's private price, negotiated terms, or roadmap as fact, decline and
  offer the supported range or `unknown`.
- If the only route to an answer is a paywall bypass, a fake identity, a competitor login, or
  scraping against a site's terms, say the question cannot be answered this way.

## Next steps to offer

`/ci-corroborate` when the brief rests on one layer · `/battlecard-patch` when the option is
respond, reframe, match, or diverge · `/ci-pattern-check` when it came from a single deal ·
`/ci-weekly` to roll it up.
