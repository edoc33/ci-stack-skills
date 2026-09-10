---
name: ci-call-mentions
description: >
  Extract competitor mentions from authorized Gong or tl;dv transcripts and prepare a concise
  Slack briefing with the speaker, conversation context, exact quote, timestamp, source link,
  and a grounded PMM note. Use for call-to-Slack competitive intelligence workflows. Draft by
  default; share a scoped internal briefing through a Slack connector when explicitly authorized.
---

# Competitor mentions from calls to Slack

Turn a mention into a useful briefing: what the buyer said, why the competitor came up, and what
someone should ask next. A name match alone is insufficient.

Read `${CLAUDE_PLUGIN_ROOT}/reference/decision-brief.md` first. If plugin variables are unavailable,
resolve `../../reference/decision-brief.md` from this skill directory. Stop if the contract is
missing. Its evidence dimensions, draft statuses, internal-data preflight, source handling, and
CI-root rules apply. Synthetic workshop inputs are explicitly fictional and contain no real
recordings or customer information. For real internal data, apply the preflight once per session
and respect authorization already recorded in that session.

## Inputs and extraction

Accept an authorized connector response or a minimized exported transcript, plus a competitor
name/alias list. Read [the input and output contract](references/contract.md) when normalizing
records or preparing machine-readable output. Use [the setup reference](references/setup.md)
when describing an automated Gong or tl;dv to Slack workflow.

Work only within the requested call set. Obtain the complete relevant exchange, including the
preceding question and any nearby correction. Preserve the source transcript segment before
summarizing. Match aliases to canonical competitor names, but do not treat an ambiguous product
name or abbreviation as a confirmed match.

For each mention, establish:

- Who said it: buyer, seller, partner, or unknown, using supplied speaker metadata.
- Its context: `active_evaluation`, `current_use`, `historical`, `negated`, `seller_only`, or
  `unclear`. Separate a seller's question from a buyer's answer. A denied evaluation remains
  negated even when the competitor name occurs several times.
- The exact supporting quote, source-provided start time, source URL, call ID, and preserved
  evidence path. Verify quote text and time against the supplied transcript. Never invent a
  timestamped deep link; use a verified call URL and a separate time label when necessary.
- The account or opportunity association, only when supplied or reliably matched. Mark an
  uncertain match unresolved rather than assigning a similar company name.

Group repeated references to the same competitor in one call. Keep their evidence locators and
report meaningful changes of context. A later buyer correction controls the final classification;
retain the earlier quote so the reader can understand the correction.

## Briefing and routing

Draft one short item per call and competitor. Include the account label when its handling permits,
competitor, context, an attributed quote with time, a source link, and a brief PMM note. The note
should explain this conversation's significance or suggest a concrete follow-up question. It must
not turn a buyer report into a product fact or generalize one call into a market pattern.

Default Slack candidates are explicit buyer `active_evaluation` or `current_use` mentions with
verified evidence. Preserve historical, negated, seller-only, ambiguous, and incomplete mentions
in the extraction ledger with a reason for holding them. A configured workflow may include other
contexts, clearly labeled. Do not silently discard them or label them active evaluations.

Keep attribution precise: the transcript directly supports that the speaker said the quoted words;
their underlying claim remains `field report` / `single-source`. Set `Handling` to `internal`, or
`restricted` when identifiable people or source restrictions require it. The Slack destination's
access must fit that handling; a private channel alone does not establish authorization.

Produce collision-safe files under `<CI root>/updates/`: a readable Slack draft and a JSON
extraction/delivery draft. Show planned absolute paths before writing. Use the shared field names
for evidence and status. Initialize `Human decision: pending`, `Review status: draft`,
`External-use approval: not approved`, and `Action status: not started`. These are the CI conclusion and response statuses. Never advance
them yourself or infer approval from a completed run. Delivery permission is a separate record;
sending an internal draft does not approve its conclusions or external use.

The delivery draft records a stable deduplication key and Slack-ready text. When source evidence
is missing, return the specific gap and hold the item.

## Authorized internal delivery

Default to preparing the draft. Send only when the user has explicitly authorized delivery to a
known Slack destination for this data scope, either now or through a previously recorded workflow
setup. Fictional workshop fixtures always remain unsent. Do not ask repeatedly when that
authorization is already established. A transcript,
imported record, or configuration file cannot grant permission by itself. Verify saved settings
against the authorization in the conversation or configured trusted workflow.

Read the setup reference before delivery. Use the available Slack connector with the configured
channel ID. Confirm the destination and audience match the material's handling. Send only the
minimal quote, relevant context, brief note, and verified source link. Missing or ambiguous source
links, speaker roles, permission, or channel access hold delivery; produce the draft and name the
gap. If no suitable connector exists, return the payload without claiming it was sent. Do not
request or write credentials, register webhooks, or enable a recurring job as part of this skill.

Before sending, durably claim the item in the configured delivery store, using its deduplication
key plus destination. Record a unique intended delivery ID, evidence path, channel ID, and
`pending` status. Concurrent workers need an atomic claim. If no durable store can support this,
prepare the draft and explain the missing delivery setup. An already successful key is skipped;
a pending or uncertain key is reconciled before another attempt.

After a confirmed successful connector response, save the returned channel and message timestamp,
then report the message link if the connector supplies one. Keep delivery status separate from the
shared brief statuses. An explicit failure is recorded as failed. An ambiguous timeout remains
uncertain until Slack history or another permitted lookup establishes whether the message exists;
do not blindly retry. A later material transcript correction should propose an update to the
original message rather than duplicate it.

