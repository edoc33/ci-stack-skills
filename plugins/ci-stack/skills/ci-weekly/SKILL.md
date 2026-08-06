---
name: ci-weekly
description: >
  Roll a period's competitive briefs into one exec-ready page — what changed, what a human actually
  decided, what was deliberately ignored and why, what is still unresolved, what is next — and render
  a decision and outcome record so the program can show it influenced decisions rather than only
  produced content. Use when the user says "weekly CI update", "what changed this week", "exec
  brief", "competitive update", "ignore log", "monthly roundup", or asks a specific executive
  question about a competitor. Needs a period and an existing corpus of briefs — NOT for triaging a
  single new change (use ci-triage).
---

# Weekly decision brief and ignore log

Two outputs, and the second is the unusual one. The brief says what happened. The **ignore log** says
what you chose not to chase, and why — the honest measure of a working program.

Before writing, read `${CLAUDE_PLUGIN_ROOT}/reference/decision-brief.md` for the evidence dimensions
and language policy. Nothing is upgraded on its way to an exec. If the contract cannot be read, stop
and report the missing plugin resource.

## Step 1 — Gather the period's material

Resolve the CI root per the shared contract, then read only what lives under it: `briefs/`,
`corroborations/`, `patterns/`, `ci-portfolio.md`, and any battlecard changelog the user points at.
Do not scan unrelated working-directory files. If no briefs exist, ask the user to paste the period's
changes and run `/ci-stack:ci-triage` on anything untriaged — do not write a brief on raw alerts.

Confirm the period and hold to it. If a prior-period item is included because it resolved this week,
mark it carried over rather than presenting it as new.

**The briefs are the source of truth.** Render every section below as a view over them. Do not create
or maintain a parallel record that can drift out of sync.

## Step 2 — Assemble the brief

Target **one page**. An exec brief that runs long does not get read, and length is not rigour.

```
Competitive update — <period>
Prepared by <name> · <date>

Headline
  Two sentences. If nothing material happened, say that. A quiet week
  reported as quiet builds more trust than a padded one.

What changed
  3-5 items maximum, ranked by consequence to a named decision — not by
  recency, not by size of change. Each one line: what changed · source
  with capture date · evidence basis and verification · who it affects.

Recommendations awaiting decision
  In-period briefs still marked `Human decision: pending`.
  Never describe these as decisions.

Decisions taken
  Only briefs with a recorded human decision. Each: the decision, who
  decided, the date, the owner, the deadline, the brief path.

Deliberately not pursued
  What we saw and chose to ignore, with the reason.

Still unresolved
  Claims we could not corroborate, and the specific evidence that would
  resolve each. Naming these is a strength, not a gap.

Watching next
  Portfolio changes, with a reason for each addition or removal. Read
  `ci-portfolio.md` before claiming this section.
```

The separation between *awaiting decision* and *decisions taken* is the point. A recommendation
reported as a decision is how a program starts believing its own output.

## Step 3 — The ignore view

Render `ci-ignore-log.md` from briefs whose recommended option was `ignore` or `continue monitoring`
and whose human decision accepted that:

```
| date | competitor | what we saw | why we ignored it | who decided | revisit if |
```

`revisit if` is what separates a decision from neglect. Fill it every time.

Include it in the brief, summarised. It does three things: it shows the program is filtering rather
than forwarding, it protects the user when something ignored later matters — the reasoning was
recorded, not absent — and it makes it safe to ignore things at all.

If nothing was ignored this period, surface that as a finding: either the portfolio is too narrow, or
everything is being escalated.

## Step 4 — The decision and outcome view

Render `ci-outcomes.md` from the briefs' status fields:

```
| date | brief | decision | action status | owner | outcome observed | attribution |
```

**Never infer a status.** Action status and outcomes come from the named owner. Ask them, and
preserve `unknown` rather than guessing from chronology or the existence of a file. An unexecuted
decision is the most useful row in this file — record it.

Rules on `attribution`, and hold them:

- **`contributed`** is usually the honest word. `caused` requires a controlled comparison you almost
  certainly do not have.
- Do not attribute a won deal to a battlecard edit because the timing lines up.
- Leave `outcome observed` blank until something is observed. Blank is data; a guess is not.

When an exec asks about the program's impact, report the decision count, the action-completion rate,
and observed outcomes with honest attribution — not an influenced-revenue figure the record cannot
support.

## Step 5 — Emit

Write `<CI root>/updates/YYYY-MM-DD-competitive-update.md` as a new collision-safe record.

Then **regenerate** `ci-ignore-log.md` and `ci-outcomes.md` from the briefs. Both carry fixed names,
so emit a proposed diff against the existing file rather than replacing it — the user may have added
notes you would destroy. Apply only what they accept.

Print only the headline, the decision count, the pending count, the ignore count, and the file paths.

Offer, but never perform, distribution. Ask before writing to Slack, email, a wiki, or a CRM. If the
user wants a channel-ready version, produce the text for them to send.

## Exec and board question mode

If the trigger is a specific question — "what is Acme doing", "should we be worried about X" — answer
that question directly: what changed with dates, what it means, what we are doing, our confidence and
why, and what would change our view. Attach the receipts. Do not deliver a general roundup when a
specific question was asked.
