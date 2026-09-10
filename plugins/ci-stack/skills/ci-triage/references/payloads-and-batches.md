# Monitoring inputs and batch triage

Read this for webhook payloads, exported alert lists, or related change histories.

## Normalize without assuming a provider schema

Use the supplied payload's actual fields. If field meaning is unclear, inspect the connector's
schema or the provider's current documentation. Do not request credentials to analyze a pasted
payload. A monitor account, webhook server and scheduler are separate setup requirements.

Normalize each record into these concepts, keeping unavailable fields `unknown`:

| Concept | Handling |
|---|---|
| Alert/event ID and monitor ID | Preserve stable nonsecret IDs when present; use them to detect retries |
| Competitor and plain page URL | Resolve source identity without retaining credentials or sensitive query strings |
| Before and after capture time | Keep timezone if supplied; distinguish an effective date from capture time |
| Capture context | Locale, plan, account state, region and selected page area when available |
| Added/removed text or paired images | Read the actual diff and relevant surrounding section |
| Tool summary and importance flag | Record as the tool's interpretation; verify against the source |
| Preserved evidence | Retain permitted text or local captures that contain the cited change |

For Visualping-shaped payloads, fields may include `url`, `datetime`, `added_text`, `removed_text`,
`summarizer`, `important`, `original`, `current`, or HTML capture links. Treat this as recognition
help, not a fixed API schema. Optional fields and string-valued flags need explicit parsing: a
string `"false"` is false, not truthy importance. A percent-change value measures the diff size.

Authenticated change-view links and signed screenshot/HTML URLs are not safe source locators to
save. Use an already authorized connector to preserve relevant evidence if available; otherwise
record that preservation was unavailable. Never save the original secret-bearing payload as a
convenient archive. Sanitize all copied text as well as URL fields. A plain page URL by itself
cannot preserve what the page used to say.

If only the tool summary is available, attribute it and mark the literal change unverified. If
raw text contradicts the summary, quote the relevant raw text and explain the mismatch.

## Process related history without erasing events

1. Track every input alert before grouping. Repeated delivery of the same stable event ID can be
   deduplicated. Without an ID, compare source, capture pair, context and content; mark uncertain
   duplicate candidates instead of discarding them.
2. Group different pages only when evidence links them to the same event, such as a shared release
   identifier or an explicitly cross-referenced plan announcement. A shared company or date is
   insufficient. Keep separate events separate even if a single executive takeaway connects them.
3. Within a grouped brief, retain every source, date and subchange. Evaluate each proposition's
   evidence and limitations. Several pages from one publisher are not independent corroboration.
4. Read supplied chronological history before recommending action. A removal followed by a
   restoration is a sequence, not two votes for the removal. Preserve both observations and state
   the latest supported state and any unknown effective period.
5. Rank briefs by consequence and urgency for the named decision, not percent change. Account for
   duplicates, missing evidence, unresolved items and ignored changes in the batch summary.

If a new alert revises an existing brief, create a linked follow-up or proposed diff under the
shared file rules. Do not overwrite the prior record or manufacture a human review. If an archive
was requested, retain the permitted capture history separately from the curated briefs; only the
latter are assessed intelligence. Actual retrieval and recurring archive storage need an external
connector or runner configured by the user.
