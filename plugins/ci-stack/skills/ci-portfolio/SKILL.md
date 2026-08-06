---
name: ci-portfolio
description: >
  Build a decision-linked competitor monitoring portfolio. Starts from the decisions you own —
  live deals, a launch, a pricing review, a board question — and returns the specific pages worth
  watching, the question each one answers, a materiality threshold, and an explicit safe-to-ignore
  rule. Emits a bulk-import CSV and per-page alert prompts. Use when the user asks what to monitor,
  wants to set up competitor tracking, says "which pages should I watch", "monitoring plan",
  "competitor portfolio", "set up alerts for competitors", or has a competitor list and no idea
  where to start. Also use when an existing monitoring setup is producing noise and needs pruning.
---

# Decision-linked signal portfolio

Most competitor monitoring starts from a competitor list and ends in noise. This skill refuses to
start there. A page earns a slot only when it answers a question tied to a decision someone owns.

## Step 1 — Get the decisions first. Do not skip this.

Ask for these before discussing any URL. If the user leads with a competitor list, thank them and
ask these anyway:

1. **What decisions do you own in the next 90 days?** Live competitive deals, a launch, a pricing
   review, a positioning refresh, a roadmap input, a board or exec question.
2. **Which competitors or alternatives actually appear in those decisions?** Include the
   status-quo and in-house-build alternatives if buyers weigh them.
3. **Who acts on the answer?** A seller, a PM, an exec, you.
4. **What would you have to see to change your mind or your plan?**
5. **How big is the team?** One or two people changes the answer — favour fewer, higher-yield
   sources and a longer check interval over broad coverage nobody reviews.

If the user cannot name a decision for a competitor, say so plainly and put that competitor in a
low-frequency "awareness" tier rather than dropping it silently.

## Step 2 — Map decisions to evidence layers

For each decision, work out which layer can actually answer it. Do not default to homepages.

| Layer | Typical pages | Answers | Cannot answer |
|---|---|---|---|
| Commercial terms | pricing, plan comparison, terms, SLA, DPA | packaging, published price, limits, contractual posture | negotiated or private pricing |
| Product truth | docs, API reference, changelog, release notes, status page | what shipped, when, how it behaves | adoption or quality |
| Positioning | homepage, category and solution pages, customer stories | the story they are telling now, and to whom | whether buyers believe it |
| Go-to-market | careers, partners, integrations, events, newsroom | where they are investing, direction | timing or success |
| Third-party | review sites, analyst pages, filings, communities | outside validation and sentiment | intent |

**Say this out loud in the output:** docs, changelogs, and pricing pages usually carry more
decision-relevant signal per change than a homepage, because a homepage changes for campaign
reasons that rarely alter a deal.

## Step 3 — Write the portfolio

One row per page. Every column is mandatory. A row missing a `Safe to ignore if` rule is not
finished — that rule is what makes the portfolio survivable.

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

### Sizing
Propose a **starting portfolio of 8–15 pages** for a one-or-two-person team. If the user wants
more, add tiers rather than rows: a review tier they read weekly and an awareness tier they read
monthly. State the check volume the portfolio implies so nobody is surprised by a plan limit.

## Step 4 — Alert prompts, one per page

Semantic prompts beat keyword filters — a keyword misses a rephrased claim and fires on a
navigation change. Write each as a plain instruction naming the decision:

> Alert me when the published price, plan limits, or packaging for the mid-tier plan changes.
> Ignore testimonial rotations, blog links, and layout changes.

> Alert me when the changelog announces a capability related to SSO, audit logging, or data
> residency. Ignore bug-fix entries and copy edits.

Bad prompt: `price` · `enterprise` · `SSO`. Say why when the user asks for keywords.

## Step 5 — Emit the artifacts

Write to files in the working directory. Never print long tables inline.

1. `ci-portfolio.md` — the full table plus the decisions it serves.
2. `ci-portfolio-import.csv` — two columns, `url,title`, where the title encodes competitor and
   layer, e.g. `Acme — pricing (commercial terms)`. This is the shape most monitoring tools accept
   for bulk import, including Visualping.
3. `ci-alert-prompts.md` — the per-page prompts, ready to paste.

## Step 6 — Name the blind spots

Close by stating what this portfolio cannot see, in the user's own context: negotiated pricing,
unannounced roadmap, private beta capability, sales behaviour, buyer perception, and anything
behind a login. Point them at `/ci-pattern-check` for the field-evidence layer. A portfolio that
does not declare its blind spots invites someone to trust it too much.

## Tooling

Tool-agnostic by design. The CSV imports into any monitoring product; the prompts work anywhere
that accepts a natural-language alert rule.

If the user has a **Visualping** API key and wants the jobs created directly, you can call the
API — ask for the key, resolve the workspace via `GET /describe-user`, then `POST /v2/jobs` per
row with `interval` as a string of minutes and the alert prompt as the importance definition.
Show the full request body and require an explicit `confirm` before creating anything. Never
create jobs the user has not seen listed.

If they have no account, the portfolio and CSV are still the deliverable — they can watch the
highest-tier pages manually and still run every other skill in this plugin.
