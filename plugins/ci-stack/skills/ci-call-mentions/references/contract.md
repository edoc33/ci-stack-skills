# Input and output contract

## Normalized input

Accept this shape from either provider. Source IDs and speaker metadata must come from the
connector/export, not from model guesses. Preserve provider fields needed to verify the mapping.

```json
{
  "fictional": false,
  "provider": "gong",
  "workspace_id": "configured-workspace",
  "call_id": "source-call-id",
  "call_url": "https://provider.example/call/source-call-id",
  "captured_at": "source capture timestamp",
  "account": {"label": "permitted account label", "association": "supplied"},
  "competitors": [{"name": "AcmeFlow", "aliases": ["AcmeFlow"]}],
  "turns": [{"speaker_id": "buyer-1", "speaker_role": "buyer", "start_seconds": 761,
             "text": "Exact words from the transcript."}]
}
```

`captured_at` records evidence preservation, not an invented meeting date. Allow missing source
fields and report the resulting limits. No source-provided start time means no verified timestamp.
Preserve a plain source URL without signed tokens or authentication parameters. If a link cannot
be safely preserved, hold the item and state the source-locator gap. A URL in a fictional example
must remain visibly fictional.

## Extraction ledger and delivery draft

Use an `items` array. Each item has `call_id`, `competitor`, `context`, `speaker_role`,
`quote`, `start_seconds`, `timestamp_verified`, `source_url`, `evidence_path`, `pmm_note`,
`slack_candidate`, `hold_reason`, and `deduplication_key`. Additional evidence quotes may be
included when needed to preserve a correction or distinguish speakers.

Use these shared contract fields inside each item's `brief`:

- `Proposition (exact, scope-limited)`
- `Evidence basis`, `Verification`, `Handling`
- `Counterevidence / unknowns`, `Confidence`
- `Recommended option`, `Rationale`
- `Human decision`, `Review status`, `External-use approval`, `Action status`

An exact quote verifies what the transcript contains. Keep a buyer's reported evaluation or product
experience as `Evidence basis: field report`, `Verification: single-source`. State the reason
alongside confidence. A recommendation to ask what a buyer's test must establish is `validate`.

Use a deterministic key derived from `provider`, `workspace_id`, `call_id`, and canonical
competitor. Scope any posted-message ledger by destination channel as well. Transcript retries
and reprocessing should not generate another message. Preserve all relevant excerpts in the item;
a later material correction should be a proposed update to the original message. Do not treat a
changed transcript hash as permission to duplicate it.

Each eligible item owns one `delivery_draft` containing `text`, `unfurl_links: false`, and `unfurl_media: false`. Held items use `delivery_draft: null`. Do not create a second top-level delivery payload; delivery consumes the per-item payload keyed to that item. Keep the
channel outside model-generated source content; the orchestrator supplies it from configuration.
Mark default draft output `ready_for_delivery: false`. `slack_candidate: true` means it meets the
content filter; it never means permission to send. In explicit delivery mode, record authorization
provenance and the intended delivery ID separately before invoking the connector. Avoid unfurling
restricted call links into a channel.

Slack quotes and notes should be readable in plain text. Escape Slack control characters `&`,
`<`, and `>` in source-derived text. Do not let transcript text create user/channel mentions,
commands, or links; use configured source links separately. The worked example includes a plain
Markdown rendering and the corresponding Slack text draft.

## Separate delivery record

The configured durable store needs: `intended_delivery_id`, `deduplication_key`, `channel_id`,
`authorization_reference`, `evidence_path`, `draft_path`, and `delivery_status`. Record `pending`
before the API call. On confirmed success, store the response `channel`, `ts`, and `sent` status.
Use `failed` for a confirmed failure and `uncertain` for an ambiguous response. Check both pending
and successful keys before sending. A store can live under the supplied CI root or in the
user-configured automation service; it must support an atomic claim for concurrent workers.

This record establishes delivery provenance. It does not advance the brief's human decision,
review, external-use approval, or recommended-action status. Keep credentials and signed source
URLs out of both records. Use provider-returned or user-verified HTTPS call links; an invented
`example.invalid` source is suitable only for an explicitly fictional, unsent workshop output.
