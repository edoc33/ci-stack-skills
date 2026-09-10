# Slack briefing draft

**Fictional workshop example. No message was sent.**

**Northstar mentioned AcmeFlow | Active evaluation**

Buyer, 12:41:

> We're evaluating AcmeFlow’s Team plan. Our IT team is testing Okta before we choose.

**Note:** SSO setup is part of this evaluation. Ask what their Okta test needs to prove.

Source: [Fictional Northstar call](https://example.invalid/calls/northstar-001), 12:41.
The exact quote and timestamp are preserved in
[`active-evaluation.json`](../../inputs/call-mentions/active-evaluation.json).

This is one buyer report. It does not establish whether AcmeFlow's Okta integration works.

| Other fixture | Classification | Routing |
|---|---|---|
| Buyer explicitly denies evaluating AcmeFlow | Negated | Hold; do not tag active evaluation |
| Seller introduces AcmeFlow without buyer confirmation | Seller only | Hold; buyer status remains unresolved |

Handling: internal. Human decision: pending. Review status: draft.
External-use approval: not approved. Action status: not started.

`records.json` includes all three extraction records and a Slack-ready text draft. The destination
and authorization are configured outside the skill. The fixture contains no Slack channel ID,
credentials, live customer data, or active automation.
