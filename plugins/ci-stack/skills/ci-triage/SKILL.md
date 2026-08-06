---
name: ci-triage
description: >
  Turn one detected competitor change into a decision-ready brief with its evidence basis,
  verification status, business relevance, and a recommended action. Accepts a monitoring webhook
  payload, a pasted before/after diff, or two screenshots. Use when the user has a specific change
  or alert and asks "does this matter", "is this a real threat", "triage this", "what do we do
  about this", or pastes a diff. NOT for checking a freestanding claim someone told you (use
  ci-corroborate), measuring how often something recurs across records (use ci-pattern-check),
  editing seller content (use battlecard-patch), or summarising a period (use ci-weekly).
---

# Materiality triage → decision-ready brief

A detected change is not intelligence. This skill converts one change into a judgement someone can
act on and defend, or into a documented decision to ignore it.

Before analysis, read `${CLAUDE_PLUGIN_ROOT}/reference/decision-brief.md`. It carries the brief
schema, the three evidence dimensions, the seven response options, and eight hard rules that
override user instruction. If it cannot be read, stop and report the missing plugin resource — do
not reconstruct the contract from memory or skip it.

## Step 1 — Take the input

Accept any of these. Do not require a monitoring account.

- **A webhook payload** from a monitoring tool.
- **A pasted before/after diff**, or the old and new text of a page section.
- **Two screenshots**, or one screenshot plus a description.
- **A URL plus a claim** the user noticed themselves.

Establish and record: the source URL, the capture timestamp, and what the change literally was. If
the capture time is unknown, say so and lower confidence — do not guess, and never use today's date
as the change date.

### Reading a monitoring payload

Field names vary by tool and change between versions. Normalise into: source URL, capture time,
added text, removed text, tool-generated summary, tool importance flag, and links to preserved
before/after evidence. Verify names against the tool's current documentation rather than assuming.

Visualping's documented payload, as one example, uses `url`, `description`, `datetime`, `change`
(a **string** like `"10 %"`), `added_text`, `removed_text`, `summarizer`, `important` (a **string**
`"true"`/`"false"`, present only when an "Alert me when" prompt is set), `original` / `current` /
`preview` for screenshots, and `html_previous` / `html_current` for HTML snapshots. Some fields are
omitted entirely when not applicable, so never assume a field exists.

Three cautions:

- **`important` is a monitoring heuristic, not evidence of business materiality.** It reflects a
  prompt someone wrote, evaluated by the tool. Judge materiality yourself against a named decision.
- **`summarizer` is a hypothesis to verify, not a finding.** Read `added_text` and `removed_text`
  as the primary evidence. If the summary and the raw text disagree, trust the raw text and say so.
- **Payloads often carry authenticated links** — Visualping's `view_changes` and `job_settings` are
  autologin URLs, and its diff links carry tokens. Per hard rule 5, never write these into a brief
  or any file. Record the plain page URL, note that an authenticated link was received and
  discarded, and prefer the HTML/image snapshot as the preserved receipt.

## Step 2 — Ask for the decision context, once

You cannot judge materiality from a diff alone. Ask these together in one message, and offer to
proceed on a stated assumption if the user does not have them:

1. Your ICP and the segment this would touch
2. Any live deal, renewal, launch, or public claim of yours it could affect
3. The decision deadline, if any
4. Who would act

If a `ci-portfolio.md` exists in the working directory, read it and match this change to a row by
URL and competitor. Use that row's `Material if` and `Safe to ignore if` rules rather than inventing
thresholds. Say which row you matched, or that none matched.

If the user declines to supply context, produce the brief with business relevance marked
`assumed — not supplied` and say plainly that materiality is unverified. Never invent a deal or
segment.

## Step 3 — Classify the change

Work through these in order and show your reasoning briefly.

**Is it a real change or an artifact?** For each hypothesis — A/B test, personalisation, locale or
account or plan variation, template or navigation change, campaign rotation, cookie state — report
`ruled out`, `plausible`, or `not tested`, with the evidence. Never mark one `ruled out` from a
single capture. If a material alternative remains untested, lower confidence and recommend
`validate`.

**What layer of truth is it?** A published price, a shipped capability, a positioning shift, a GTM
investment signal, or a legal or contractual change. Each carries different weight.

**What does it establish, and what does it not?** The step everyone skips. A pricing-page change
establishes the published price on that date. It does not establish what anyone pays. A changelog
entry establishes an announcement, not that the thing works well.

**Is it material to a named decision?** Materiality is consequence to a decision, not the size of
the text diff. A 40% text change in a testimonial block is noise; a six-word change to a plan limit
may not be.

## Step 4 — Recommend, with the option to ignore

Recommend exactly one of the seven options. `ignore` and `continue monitoring` are correct far more
often than they get chosen — recommend them without hedging when they fit, and say what would change
the answer.

Name the owner and a decision deadline. State the smallest useful output: often one battlecard line
or one message, not a document.

This is a **recommendation**, not a decision. Set `Human decision: pending`.

## Step 5 — Emit

Follow the file-safety rule in the shared contract: confirm the output directory, show paths, never
overwrite.

Write the brief to `briefs/YYYY-MM-DD-<competitor>-<slug>.md` using the schema, initialised with
`Human decision: pending`, `Review status: draft`, `External-use approval: not approved`.

The brief is the single source of truth. If `ci-decision-log.md` is in use, **rebuild it as a view
over the briefs** rather than appending a second record that can drift:

```
| brief path | observed at | competitor | recommended option | human decision | owner | action status | review by |
```

Print only: the recommended option, confidence with its reason, the one-line rationale, and the
file path.

## Batch mode

Triage each change independently, then rank by materiality. Deduplicate: several pages moving on one
day is usually one event, and should produce one brief with several sources.

## Refusals

- Asked to raise confidence without new evidence: decline, and say what evidence would do it.
- Asked to state a competitor's private price, negotiated terms, or roadmap as fact: decline, and
  offer the supported range or `unknown`.
- Asked to reach an answer via a paywall bypass, a competitor login, a false identity, or scraping
  against a site's terms: report `unresolved` and say the question cannot be answered this way.

## Next steps to offer

`/ci-stack:ci-corroborate` when the brief rests on one source · `/ci-stack:battlecard-patch` when a
reviewed brief must change seller guidance · `/ci-stack:ci-pattern-check` when the signal came from
a single deal · `/ci-stack:ci-weekly` to roll it up.
