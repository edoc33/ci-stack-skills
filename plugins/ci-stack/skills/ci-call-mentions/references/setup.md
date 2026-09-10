# Connect a call briefing to Slack

Start with [the draft-only practice run](first-run.md). This reference describes how to connect
that draft to a configured workflow. It is an implementation plan, not an installed integration.
Check available tools, transcript access, and account entitlements in your environment.

```text
Gong or tl;dv transcript
          |
          v
Runner: receive event or fetch the chosen call window
          |
          v
Agent: run ci-call-mentions with competitor aliases and source evidence
          |
          v
Routing check + durable delivery claim
          |
          v
Slack: contextual briefing for the authorized audience
```

The runner can be an existing automation service or a script. A manual draft needs no runner.
n8n can be part of a configured workflow; a scheduled GitHub Actions job can run a configured
script. Either needs an adapter that actually invokes an agent with this skill and passes back
its output. A generic AI node does not acquire the skill merely because this repository exists.
The user's second brain can supply competitor aliases and permitted messaging rules. CRM context
is optional; matching and updating opportunities are separate configured actions.

## Inputs the implementation owner supplies

| Component | Required setup |
|---|---|
| Transcript provider | Authorized calls, event or polling scope, fetch operation, roles, source time units, call IDs, and safe source links. |
| Agent runtime | This installed skill, shared contract, competitor aliases, permitted input/output locations, and access to the required sources. |
| Routing | Included contexts, permitted account labels, handling rules, destination channel ID, and recorded user authorization for the audience and data scope. |
| Delivery store | Persistent records, atomic claims, and a way to inspect pending, sent, failed, and uncertain attempts. A plain JSON file alone is insufficient for concurrent writers. |
| Slack connector | An authorized app or tool that can post to the intended channel and expose a confirmed result. A permitted lookup path is needed to reconcile uncertain results. |

Keep secrets in the user's configured credential store. The skill does not request credentials,
register webhooks, change provider settings, or enable a recurring job. Extra provider, runner,
hosting, and model costs depend on the chosen implementation.

## Fetch and normalize the actual provider response

For tl;dv, a configured `TranscriptReady` event can trigger a transcript fetch. For Gong, a configured
Automation rule can fire a webhook and an adapter can request transcripts. Check the current
provider documentation and permissions when building the adapter. Preserve the supplied speaker
mapping and time units, then convert source times explicitly to seconds. For Gong, sentence start
and end fields are milliseconds; verify the tl;dv response or connector's units before converting.

Fetch the requested call set and preserve the relevant exchange, including questions and
corrections. Run `ci-call-mentions` and validate its per-item output before any delivery. Call
access does not prove that a Slack audience may see the same material.

## Route and claim before delivery

Send only when the user has explicitly authorized a known destination, audience, and content
scope, either in the current request or an already configured trusted workflow. Reuse that
permission while its scope still applies. A private channel alone does not establish permission;
its actual audience, including external guests where relevant, must fit the material's handling.
Fictional fixtures always remain unsent.

For each item, require `slack_candidate: true`, complete evidence, stable identity, no unresolved
delivery blockers, and the allowed context. Consume that item's `delivery_draft`. Missing or
ambiguous permission, source evidence, connector access, or durable state yields a draft with a
specific setup gap. Do not silently promote `ready_for_delivery` based on completed extraction.

The store key combines the stable item key with the channel. Atomically claim it and persist a
unique intended delivery ID and `pending` state before calling Slack. Concurrent workers must
observe the same claim. Skip already sent keys. Reconcile pending or uncertain keys before another
attempt; an expired worker lease does not establish that a message was never sent.

A correction to an already sent item proposes an update to the original message using its stored
channel and timestamp. Posting a second message is a separate decision and must not be the default
response to a changed transcript hash.

## Send and reconcile

Use the configured Slack connector or `chat.postMessage` with the configured channel ID and the
per-item sanitized payload. Slack's posting method requires `chat:write` and appropriate access
to that destination. Request only the scopes and membership needed for the chosen workflow.
See [chat.postMessage](https://docs.slack.dev/reference/methods/chat.postMessage/).

A confirmed successful response includes `ok: true`, channel, and message timestamp (`ts`). Save
them before reporting delivery. A confirmed failure is `failed`. A timeout, lost response, or
server error that may have followed a successful write remains `uncertain`, even if it is retryable
at the network layer. Use Slack history or another permitted lookup to establish whether the
intended message exists. If it cannot be established, keep the item held and report the uncertainty.
Do not treat absence from an incomplete history lookup as proof of non-delivery.

Honor a confirmed rate-limit response's `Retry-After` and use bounded retries only after establishing
that the prior attempt did not send. Apply the workflow's configured attempt limit. If none is set,
leave a failed or uncertain record for the operator instead of looping. See
[Slack rate limits](https://docs.slack.dev/apis/web-api/rate-limits/).

Delivery status is separate from the brief's human decision, review, external-use approval, and
recommended-action status. A successful post can still contain a draft conclusion. Report a
message link only if the connector returns it or a permitted lookup resolves it.

## Verify the adapter before enabling a schedule

Use a controlled test destination and data scope explicitly authorized by the user. Check a first
send, the same input twice, two workers claiming the same item, a lost send response, and a later
transcript correction. Confirm that source text cannot generate Slack mentions or change the
configured destination. These are implementation checks to run after the adapter exists; the
bundled fictional fixture remains a draft-only exercise.

## Provider references

Consult current official documentation when implementing adapters:

- [Gong webhook rules](https://help.gong.io/docs/create-a-webhook-rule)
- [Gong transcript endpoint](https://help.gong.io/apidocs/retrieve-transcripts-of-calls-by-date-or-callids-v2callstranscript-2)
- [tl;dv API and TranscriptReady webhook](https://doc.tldv.io/index.html)
- [Slack text formatting and escaping](https://docs.slack.dev/messaging/formatting-message-text/)

A successful fixture run demonstrates interpretation and draft generation. Provider access,
subscription entitlement, the installed Slack app, and delivery reliability require separate
checks in the configured environment.
