---
name: ci-portfolio
description: >
  Design or prune a competitor monitoring source set, tied to the decisions the user owns. Returns
  the pages worth watching, the question each answers, a materiality threshold, an explicit
  safe-to-ignore rule, and a per-page alert prompt, plus a generic export. Use when the user asks
  what to monitor, says "which pages should I watch", "monitoring plan", "competitor portfolio",
  "set up alerts", or when an existing setup is producing noise and needs cutting back. NOT for
  judging an alert that already arrived (use ci-triage).
---

# Decision-linked signal portfolio

Most competitor monitoring starts from a competitor list and ends in noise. A page earns a slot here
only when it answers a question tied to a decision someone owns.

Before producing a portfolio, read `${CLAUDE_PLUGIN_ROOT}/reference/decision-brief.md` for the
evidence dimensions, the authorized-sources rule, and the file-safety rule. If it cannot be read,
stop and report the missing plugin resource.

## Step 1 — Anchor on one decision, then move

Use any decision context the user already gave. If there is none, ask **one** combined question:

> Which live deal, launch, pricing or positioning review, roadmap choice, or executive question
> should this watchlist support in the next 90 days?

If they cannot name one, offer two or three plausible working hypotheses, label the portfolio
**provisional**, and start with three to five pages. Do not block useful work on a full intake.

Ask about the owner, the change-of-mind threshold, and team capacity **only when the answer would
change the recommendation** — usually when the user is a one-or-two-person team, where fewer
higher-yield sources beat broad coverage nobody reviews.

If a competitor has no decision attached, say so and put it in a low-frequency awareness tier rather
than dropping it silently.

## Step 2 — Map decisions to evidence layers

Work out which layer can actually answer the question. Do not default to homepages.

| Layer | Typical pages | Answers | Cannot answer |
|---|---|---|---|
| Commercial terms | pricing, plan comparison, terms, SLA, DPA | packaging, published price, limits, contractual posture | negotiated or private pricing |
| Product truth | docs, API reference, changelog, release notes, status | what shipped, when, how it behaves | adoption or quality |
| Positioning | homepage, category and solution pages, customer stories | the story they tell now, and to whom | whether buyers believe it |
| Go-to-market | careers, partners, integrations, events, newsroom | where they are investing | timing or success |
| Third-party | review sites, analyst pages, filings, communities | outside validation and sentiment | intent |

Say this in the output: docs, changelogs, and pricing pages usually carry more decision-relevant
signal per change than a homepage, because homepages change for campaign reasons that rarely alter a
deal.

## Step 3 — Write the portfolio

One row per page.

| Column | Content |
|---|---|
| URL | The specific page, not the domain |
| Competitor | |
| Layer | From the table above |
| Decision served | The decision from step 1, named |
| Question it answers | One sentence, answerable |
| Material if | The change that would actually alter a decision |
| Safe to ignore if | The change that would not — be specific |
| Check interval | Match to how fast the decision moves, not to how fast the tool allows |
| Reviewer | A named person |

`Decision served`, `Question it answers`, `Material if`, and `Safe to ignore if` must be filled
before a row is activated — the ignore rule is what makes the portfolio survivable. Mark anything
else `unassigned` or `unknown`. Never invent a named reviewer, and never block a provisional draft
because one field is missing.

### Sizing
Propose **8–15 pages** for a one-or-two-person team, or 3–5 for a provisional start. If the user
wants more, add tiers rather than rows: a review tier read weekly, an awareness tier read monthly.
State the check volume the portfolio implies so nobody is surprised by a plan limit.

## Step 4 — Alert prompts, one per page

Semantic prompts beat keyword filters — a keyword misses a rephrased claim and fires on a navigation
change. Write each as a plain instruction naming the decision:

> Alert me when the published price, plan limits, or packaging for the mid-tier plan changes.
> Ignore testimonial rotations, blog links, and layout changes.

> Alert me when the changelog announces a capability related to SSO, audit logging, or data
> residency. Ignore bug-fix entries and copy edits.

Bad prompt: `price` · `enterprise` · `SSO`. Explain why when the user asks for keywords.

## Step 5 — Emit

Per the file-safety rule: confirm the directory, show paths, never overwrite.

1. `ci-portfolio.md` — the table plus the decisions it serves and whether it is provisional.
2. `ci-portfolio-export.csv` — a generic UTF-8 `url,title` export, where the title encodes
   competitor and layer, e.g. `Acme — pricing (commercial terms)`. Quote cells properly and
   neutralise leading `=`, `+`, `-`, and `@` so no cell is treated as a spreadsheet formula.
3. `ci-alert-prompts.md` — the per-page prompts, ready to paste.

**Do not call this import-ready for any specific tool.** Check the target tool's current import
format and plan entitlement first, and tell the user what you found. For Visualping specifically:
dashboard bulk import is a **Business-plan feature**, and it accepts URLs and titles **pasted** as
two columns separated by a tab or a single space — not an uploaded comma-delimited CSV. Users on
other plans add pages individually.

This release produces reviewed artifacts only. It does not request API credentials or create
monitoring jobs. Direct job creation belongs in a later version, once secret handling,
least-privilege scope, dry-run, duplicate detection, idempotency, and partial-failure recovery are
bundled and tested — improvising those from three lines of prose is how people end up with 40
duplicate jobs and a key in a shell history.

## Step 6 — Name the blind spots

Close by stating what this portfolio cannot see: negotiated pricing, unannounced roadmap, private
beta capability, sales behaviour, buyer perception, anything behind a login. Point at
`/ci-stack:ci-pattern-check` for the field-evidence layer.

Also name the competitor you might be missing. This skill works from the alternatives the user
already knows about; it does not discover the emerging or indirect one they omitted. Ask what buyers
mention that is not on the list, and treat "we built it in-house" and "we do nothing" as
alternatives worth a row.
