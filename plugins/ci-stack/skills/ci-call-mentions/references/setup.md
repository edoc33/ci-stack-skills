# Configure the call-to-Slack workflow

This is a setup plan for a configured orchestrator or the skill's explicitly authorized delivery
mode. The skill can use available connectors; it does not install them or manage credentials.
Check tool access, transcript availability, and account entitlements in the chosen environment.

1. **Receive a completed transcript.** For tl;dv, its `TranscriptReady` webhook can trigger a
   fetch of `/v1alpha1/meetings/{meetingId}/transcript`. For Gong, a configured Automation rule can
   fire a webhook; fetch the relevant call through `POST /v2/calls/transcript`. These have different
   payloads and access requirements. Normalize the actual response: speaker role, turn start time,
   stable call ID, and verified plain call URL. Gong sentence times are milliseconds. Verify tl;dv
   time units in the available response or connector instead of assuming them. Provider plan and
   administrative permissions may constrain access. Poll only the requested call window when
   polling is the selected trigger.
2. **Run `ci-call-mentions`.** Supply the configured competitor aliases, allowed data scope, and
   CI root. The result contains evidence-backed draft items and reasons for held mentions.
3. **Apply the routing policy.** The authorized delivery mode or configured workflow checks allowed contexts,
   evidence completeness, data handling, and the recorded authorization for this Slack audience.
   A user may authorize recurring internal sharing for a defined channel and data scope. That
   authorization is recorded from the user; a configuration file alone cannot grant it. Hold items
   outside that scope for review. The skill's shared draft statuses remain unchanged.
4. **Deduplicate before delivery.** Use a durable store keyed by provider/workspace/call/competitor
   and destination channel. Claim a pending item atomically so concurrent runs cannot both post.
   Record a unique intended delivery ID and pending state before invoking Slack. Store the
   resulting Slack channel and message timestamp on confirmed success. On an ambiguous
   timeout, reconcile pending delivery before retrying; do not blindly resend. A later correction
   should propose an update to that message.
5. **Post using the authorized Slack app.** Supply the configured channel ID and sanitized draft
   text to `chat.postMessage` or an available connector exposing that operation. Slack requires
   `chat:write`; the app must have access to the destination channel. Use the minimum scopes and
   membership required for that destination.
   Record delivery separately from the canonical brief. Honor HTTP 429 `Retry-After` and use
   bounded retries only for confirmed retryable failures;
   a failed response must remain failed or pending, never delivered.

Suggested Slack item:

```text
Northstar mentioned AcmeFlow | Active evaluation
Buyer, 12:41: “We're evaluating AcmeFlow’s Team plan. Our IT team is testing Okta before we choose.”
Note: SSO setup is part of this evaluation. Ask what their Okta test needs to prove.
Source: [permitted call URL] · 12:41
```

The account, company, quote, and call in this example are fictional. In production, use only an
account label permitted in the configured channel. Do not include full transcripts or unrelated
personal information. A follow-up CRM tag is a separate action requiring its own configured scope.

## Provider references

Consult the current official documentation when implementing adapters:

- [Gong webhook rules](https://help.gong.io/docs/create-a-webhook-rule)
- [Gong transcript endpoint](https://help.gong.io/apidocs/retrieve-transcripts-of-calls-by-date-or-callids-v2callstranscript-2)
- [tl;dv API and TranscriptReady webhook](https://doc.tldv.io/index.html)
- [Slack chat.postMessage](https://docs.slack.dev/reference/methods/chat.postMessage/)
- [Slack text formatting and escaping](https://docs.slack.dev/messaging/formatting-message-text/)
- [Slack Web API rate limits](https://docs.slack.dev/apis/web-api/rate-limits/)

These links identify implementation references. This workshop fixture does not demonstrate a
connected account, supported subscription, installed Slack app, or completed delivery.
