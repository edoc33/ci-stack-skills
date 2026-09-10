# Start from a Visualping Reports export

Use an authorized, user-supplied export as intake. Visualping Reports supports CSV, Excel, HTML,
and PDF exports. Read the available format with the host's file tools. If parsing is unavailable,
request the relevant rows or a supported export; do not claim the unread content was processed.
Generating a report in Visualping requires a Business plan. See the
[Visualping Reports guide](https://help.visualping.io/en/articles/10899969).

This skill does not assume a live Reports API, fetch reports on its own, or install integrations.
A recurring workflow must provide the export or use a separately verified, authorized collection
adapter. Record how this run obtained its inputs.

## Map the actual fields

Inspect the supplied headers or document labels. Export formats can differ. Map available fields
to competitor or page, plain monitored URL, observed timestamp and timezone, change summary,
importance indicator, and preserved before/after evidence. Record the report's period and filters.
The export creation date alone does not establish when a change was observed.

Keep the vendor's importance label distinct from the PMM's decision about what deserves attention.
A generated change summary is an input to check against receipts. It does not independently
corroborate those receipts. A live page URL without preserved content is not a historical capture.
Discard signed-token links and credentials before persisting any locator.

Deduplicate the same event across overlapping reports using an event ID when available, otherwise
the normalized monitored URL, capture time, and preserved change content. Group related captures
chronologically so a removed and restored statement is not reported as a current removal.

## Turn rows into usable briefs

For each potentially material change, preserve the exact proposition, relevant scope, dated receipt,
evidence basis, verification, handling, confidence, business consequence, and proposed response.
Use `ci-triage` if installed. Missing receipt content, capture dates, or context stay explicit;
hold unsupported claims out of the newsletter's factual changes and list them as unresolved.

Keep all generated briefs at `Human decision: pending`, `Review status: draft`, and
`External-use approval: not approved`. An `Important` label or a report containing a change does
not constitute a human decision. A routine change can receive an `ignore` recommendation, but it
enters the accepted ignore log only after a recorded human decision.

If `ci-triage` is unavailable, return a pending-intake table with row locator, observed timestamp,
available receipt, missing fields, and suggested triage question. Produce a partial newsletter from
existing usable briefs if possible. State how many rows were read, duplicates removed, usable
briefs included, and items held. Avoid filling the report with unsupported claims to appear complete.

## Connect a recurring workflow

An optional runner can collect a permitted export on a weekly, twice-monthly, monthly, or custom
schedule, invoke the configured agent with this skill and brand rules, and place the draft in the
team's review location. Delivery to Slack, Teams, or email is a separate authorized step. The runner
also needs durable state to avoid processing the same export or sending the same issue twice.
The presence of this skill file does not supply that adapter, scheduler, or delivery state.
