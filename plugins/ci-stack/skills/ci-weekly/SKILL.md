---
name: ci-weekly
description: >
  Roll the week's competitive briefs into one exec-ready page — what changed, what we decided, what
  we deliberately ignored and why, what is still unresolved, and what we are watching next — and
  maintain a running decision and outcome record so the program can show it influenced decisions
  rather than only produced content. Use when the user says "weekly CI update", "what changed this
  week", "exec brief", "competitive update", "board question about competitors", "ignore log",
  "monthly roundup", or needs to report on the competitive program itself.
---

# Weekly decision brief and ignore log

Two outputs, and the second one is the unusual one. The brief says what happened. The **ignore log**
says what you chose not to chase, and why — which is the honest measure of a working program.

**Read `reference/decision-brief.md` at the plugin root first** for the evidence labels and language
policy. Everything in the brief carries its label; nothing is upgraded on the way to an exec.

## Step 1 — Gather the period's material

Read whatever exists in the working directory: `ci-decision-log.md`, `briefs/`, `corroborations/`,
`patterns/`. If none exist, ask the user to paste the period's changes and run `/ci-triage` on any
that have not been triaged — do not write a brief on untriaged raw alerts.

Confirm the period and stick to it. If a prior period's item is included because it resolved this
week, mark it as carried over rather than presenting it as new.

## Step 2 — Assemble the brief

Target **one page**. An exec brief that runs long does not get read, and length is not rigour.

```
Competitive update — <period>
Prepared by <name> · <date>

Headline
  Two sentences. If nothing material happened, say that. A quiet week
  reported as quiet builds more trust than a padded one.

What changed
  3-5 items maximum, ranked by consequence, not by recency. Each one line:
  what changed · source with date · evidence label · who it affects.

Decisions taken
  Each: the decision, the owner, the deadline, and the brief it came from.
  This section is the point of the document.

Deliberately not pursued
  What we saw and chose to ignore, with the reason. See below.

Still unresolved
  Claims we could not corroborate, and the specific evidence that would
  resolve each one. Naming these is a strength, not a gap.

Watching next
  Changes to the portfolio, with the reason for each addition or removal.
```

Ranking rule: consequence to a named decision beats size of change, and beats how recent it was.

## Step 3 — The ignore log

Maintain `ci-ignore-log.md` across periods. Every entry:

```
| date | competitor | what we saw | why we ignored it | who decided | revisit if |
```

The `revisit if` column is what separates a decision from neglect. Fill it in every time.

Include the ignore log in the brief, in summary. It does three things: it shows the program is
filtering rather than forwarding, it protects the user when something ignored later matters — the
reasoning was recorded, not absent — and it makes it safe to ignore things at all.

If nothing was ignored this period, that is a finding worth surfacing: either the portfolio is too
narrow, or everything is being escalated.

## Step 4 — The decision and outcome record

Maintain `ci-outcomes.md`. This is how the program answers "did any of this matter."

```
| date | brief | decision | action taken | owner | outcome observed | attribution |
```

Rules on the `attribution` column, and hold them:

- **`contributed`** is usually the honest word. `caused` requires a controlled comparison you almost
  certainly do not have.
- Record what actually happened, including when the action was never taken. Unexecuted decisions are
  the most useful thing in this file.
- Do not attribute a won deal to a battlecard edit because the timing lines up.
- Leave `outcome observed` blank until something is observed. Blank is data; a guess is not.

When an exec asks for the program's impact, report the decision count, the action-completion rate,
and the observed outcomes with honest attribution — not an influenced-revenue figure the record
cannot support.

## Step 5 — Emit

Write `updates/YYYY-MM-DD-competitive-update.md`, update `ci-ignore-log.md` and `ci-outcomes.md`,
and print only the headline, the decision count, the ignore count, and the file paths.

Offer, but do not perform, distribution. Ask before writing to Slack, email, a wiki, or a CRM — and
if the user asks for a channel-ready version, produce the text for them to send.

## Exec and board question mode

If the trigger is a specific question — "what is Acme doing", "should we be worried about X" —
answer that question directly in a short assessment: what changed with dates, what it means, what we
are doing, our confidence and why, and what would change our view. Attach the receipts. Do not
deliver a general roundup when a specific question was asked.
