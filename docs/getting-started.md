# First runs

Install using the [repository README](../README.md). These examples are fictional and work without
live tools. Paste the prompt after invoking the named skill. Ask for inline output on your first
run. When you want files, give an absolute CI directory or let the agent show its proposed `./ci/`.

Claude Code names skills `/ci-stack:ci-portfolio`; Codex names them `$ci-portfolio`. The same pattern
applies to every name below. A skill's own first-run example is included in its installed folder.

## Update an existing installation

For a Claude Code user-scope installation, run these commands in your terminal:

```sh
claude plugin marketplace update ci-stack
claude plugin update ci-stack@ci-stack
claude plugin list
```

Check that the listed version is `0.3.0`, then start a new session or run `/reload-plugins` in an
existing session when prompted. If you installed in project or local scope, add `--scope project`
or `--scope local` to the update command and run it from that project. See the
[official update reference](https://code.claude.com/docs/en/plugins-reference#plugin-update).

For Codex, download the latest `main` checkout before running the installer. If you already have
CI Stack skill folders in your destination, compare and back up those seven folders outside every
skill-discovery directory, then move the old copies out of the destination. Keep unrelated skills
and your CI output directory in place. Rerun the two installer commands in the README. The script
copies a fresh set and refuses collisions; it does not merge local edits or fetch future updates.
Review your customizations before applying them to the new version. Restart Codex if needed.

## Build a watchlist with ci-portfolio

```text
Fictional exercise, inline output. We sell workflow software to midmarket IT teams.
We need to review our SSO comparison before next month's campaign. Our known
alternative is AcmeFlow. Candidate URLs supplied for this exercise:
https://acmeflow.example/pricing and https://acmeflow.example/docs/sso.
We have not checked whether these illustrative pages exist. Propose the minimum
useful watchlist, materiality and ignore rules, and alert prompts. Do not browse
or create monitors. Reviewer and exact campaign date are unassigned.
```

Look for a connection between each page and the SSO decision. URLs supplied as fictional or
unverified should retain that label. A generic export still needs mapping to your monitoring tool.

## Judge a change with ci-triage

Use the [README's pasted change](../README.md#run-your-first-skill). Save the brief when you want
to pass it into another skill. Keep the source URL, capture date, and preserved excerpt with it.
The model's summary alone is insufficient evidence for downstream claims.

## Check a claim with ci-corroborate

```text
Fictional exercise, inline output, no browsing. Test this claim: "AcmeFlow Team
supports SAML SSO in production." Our evidence, captured 2026-08-06:
- Pricing page says "Team: SSO included."
- A syndicated article repeats that pricing announcement and links to it.
- No trial test, protocol documentation, or buyer confirmation is available.
Identify what these sources establish about the original claim and what further
evidence would resolve it. Keep publication and product behavior separate.
```

The syndicated article should count as the same origin. The skill should retain the original
product claim even when it can support narrower wording about the pricing page.

## Draft a battlecard edit with battlecard-patch

```text
Fictional exercise, inline proposal only. The current card says:
"AcmeFlow Team lacks SSO. Use SSO as our main differentiator."
A draft brief records the 2026-08-06 pricing-page excerpt "Team: SSO included"
at https://acmeflow.example/pricing. Preserved evidence is that excerpt.
Evidence basis: observed publication. Verification: single-source.
Confidence: high for publication, unresolved for product behavior.
Recommended option: validate. Human decision: pending. Review status: draft.
External-use approval: not approved. We have no newer captures or trial test.
Find stale claims and propose the appropriate internal edit. Preserve the original.
```

Expect a diff or internal warning with its limits, rather than a newly approved feature claim.
When using real data, supply the current card and related later changes, including any reversal.

## Check recurrence with ci-pattern-check

```text
Fictional exercise, inline output. We want to know whether active AcmeFlow evaluation
recurs in our August midmarket opportunities. Define the counting rule first.
Each line is one call, not necessarily one opportunity:
D1, Aug 04, buyer, "We are evaluating AcmeFlow alongside you."
D1, Aug 06, buyer, "Our AcmeFlow test is still running."
D2, Aug 07, seller, "Have you heard of AcmeFlow?"
D3, Aug 09, buyer, "We used AcmeFlow last year; it is not on this shortlist."
D4, Aug 10, buyer, "We are comparing your Team plan with AcmeFlow Team."
The complete opportunity universe and recording coverage are unknown. Do not infer
loss reasons, CRM updates, or a market-wide percentage from these notes.
```

Repeated calls from D1 should count as one opportunity. The output should distinguish active
buyer evaluation from historical use and a seller-introduced name.

## Write a period update with ci-weekly

```text
Fictional exercise, inline output. Write an internal update for August 1 through
August 15, 2026, inclusive, America/Los_Angeles. Here are two canonical brief excerpts:
A: Aug 06, AcmeFlow pricing page published "Team: SSO included". Source and preserved
excerpt: https://acmeflow.example/pricing, captured Aug 06. Observed publication,
single-source, public, product behavior untested. Recommend validate. Human decision
pending; review draft; external-use not approved; owner unassigned; action not started.
B: Aug 07, pricing page footer changed "2025" to "2026". Same URL, preserved before/after
excerpts here. Observed, single-source, public. Recommend ignore. Human decision accepted
by fictional PMM Sam on Aug 08, review reviewed by Sam Aug 08, external-use not approved.
Revisit if a product or commercial claim changes. Action done: no follow-up required.
There is no portfolio or recorded business outcome. Identify those gaps.
```

The SSO check belongs among pending recommendations. The footer belongs in the accepted ignore
view. Neither should become a claim that CI improved win rate. Supply the report period and timezone
when you schedule this workflow. Twice-monthly means named calendar periods, not every two weeks.

## Draft a call briefing with ci-call-mentions

Use the bundled [call example](../plugins/ci-stack/skills/ci-call-mentions/references/first-run.md)
for a complete normalized transcript and prompt. It requires no Gong, tl;dv, or Slack account.
Ask for a draft, then check the exact quote, speaker role, timestamp, context, and PMM note.
The result should explain why seller-only, historical, or rejected mentions were held.

## Move from examples to your own work

Supply one permitted input and the decision it should inform. Use a minimized transcript export,
a preserved before/after page excerpt, or a current card. Keep credentials out of prompts and files.
If a source cannot be accessed, provide a permitted export or leave the claim unresolved.

A file-writing run should show its output location. A rerun should preserve existing records.
Read the draft and record your decision before it reaches sellers or customers. For scheduled jobs,
use the [workflow guide](workflows.md) to define inputs, retries, destinations, and review.

## Troubleshooting

| Symptom | What to check |
|---|---|
| Skill not listed in Claude Code | Check `/plugin`, the install summary, and whether reload is requested |
| Skill not listed in Codex | Check the destination contains `<skill>/SKILL.md`; restart if needed |
| Shared contract missing | Install the complete plugin or rerun the Codex installer into a fresh destination; copying only SKILL.md loses required files |
| Codex installer reports a collision | Inspect the existing skill and back it up outside the discovery directory before installing; the installer will not overwrite it |
| Repeated context questions | Supply decision, CI root and permitted data scope once; the skills should reuse them |
| No connector available | Use a pasted excerpt or export and draft mode |
| No usable capture or timestamp | Keep the gap explicit and request evidence; do not substitute today's date |
| Existing output file | Expect a numbered new record or a proposed diff |
| Slack send result is uncertain | Reconcile the stored attempt and provider history before retrying |
