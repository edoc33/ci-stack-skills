# CI Stack

Six Claude Code skills for product marketers who own competitive intelligence.

They take a competitor change from signal to a decision you can defend, with the evidence attached.
The premise is that detection was never the hard part — deciding what matters, saying only what the
evidence supports, and being able to show your work is the hard part.

## Install

```
/plugin marketplace add edoc33/ci-stack-skills
/plugin install ci-stack@ci-stack
```

Then `/reload-plugins` if prompted. Skills are namespaced: `/ci-stack:ci-triage`.

## Start here

**`ci-portfolio` → `ci-triage` → `ci-weekly`** is the whole loop. Learn those three.

The other three are branches you reach for when a specific thing happens:

| Branch | Reach for it when |
|---|---|
| `ci-corroborate` | One claim needs deeper verification before it faces a customer or an exec |
| `ci-pattern-check` | You need to know whether something recurs across records, or is one loud deal |
| `battlecard-patch` | A reviewed finding has to change seller guidance |

## The six

| Skill | Use it when | Gives you |
|---|---|---|
| `ci-portfolio` | You don't know what to watch, or your alerts are noise | A watchlist where every page is tied to a decision, with a safe-to-ignore rule and an alert prompt, plus a generic export |
| `ci-triage` | A change came in and you need to know if it matters | A decision-ready brief: evidence basis, verification status, counterevidence, confidence, affected deals, one of seven recommended actions, an owner, a review date |
| `ci-corroborate` | A claim is about to go in front of a customer or an exec | `corroborated` / `contradicted` / `single-source` / `unresolved`, the phrasing you may use, and the phrasing you may not |
| `battlecard-patch` | A reviewed brief needs to reach sellers | A redlined diff with source and capture date per claim, and a list of claims elsewhere in the card that just went stale |
| `ci-pattern-check` | Someone wants to change positioning because of a few deals | `single case` / `repeated signal` / `scoped pattern in <cohort>`, with the denominator stated and competing explanations |
| `ci-weekly` | The exec asks what changed | A one-page update that separates recommendations from decisions, an ignore log, and an outcome record |

## What holds it together

Every skill reads one shared contract,
[`reference/decision-brief.md`](plugins/ci-stack/reference/decision-brief.md). It defines the brief
schema and the rules the skills apply even when asked not to:

1. **Three independent dimensions, not one score** — evidence basis (`observed` / `field report` /
   `inferred`), verification status (`not tested` / `single-source` / `corroborated` /
   `contradicted` / `unresolved`), and handling (`public` / `internal` / `restricted`). Corroboration
   adds support; it never turns an inference into an observed fact. Repeating a claim upgrades
   nothing.
2. **Absence is not disproof.** A claim missing from a public page is `unresolved`, not
   `contradicted`. Private pricing, negotiated terms, unreleased capability and seller behaviour are
   invisible to a page diff.
3. **A dated capture proves publication, not truth** — and a live URL plus a date is not a receipt,
   because the page can change again. Preserved before/after content is.
4. **`ignore` is a real answer.** Two of the seven recommended actions are to do nothing. A system
   that never picks them is producing work, not judgement.
5. **Drafts are not approvals.** The skills draft and propose. They never publish, send, or commit,
   and they cannot mark their own output approved.

## Requirements

Claude Code. That is the hard requirement.

**No monitoring account is needed for the core loop.** `ci-triage` accepts a pasted before/after
diff, so you can run the method by hand before automating any of it. The other skills work from its
brief, or from a portfolio, evidence set, battlecard, or export you supply.

Optional, all bring-your-own:

- A change-monitoring tool for detection. `ci-triage` reads a generic normalized event and
  understands the currently documented [Visualping](https://visualping.io) webhook fields; any tool
  that reports a before/after works, and the portfolio export is generic.
- A meeting-recorder export for `ci-pattern-check` — tl;dv, Gong, Fireflies, Zoom, or plain notes.
- A CRM export for the pattern and outcome layers.

### On data

This plugin adds no telemetry and no background service. But Claude Code itself sends prompts and
selected content to your configured model provider, stores local session transcripts in plaintext for
30 days by default, and follows your provider and account retention policies. Web research and any
API calls you authorize make explicit network requests. See
[Claude Code data usage](https://code.claude.com/docs/en/data-usage).

Before any skill reads call recordings, CRM exports, or buyer notes, it runs a preflight: confirm
recording consent under your applicable law — several jurisdictions require all-party consent —
confirm your organization permits AI processing of that data, and minimise the export before you
upload it. If either is uncertain, the skills offer a count-only workflow instead. **None of this
makes your processing compliant.** Route uncertainty to privacy or legal.

## Try it in two minutes

```
/ci-stack:ci-triage
```

Paste [`examples/sample-webhook-payload.json`](plugins/ci-stack/examples/sample-webhook-payload.json)
when asked for input. A fictional competitor raised a plan price, added a usage cap, and removed an
enterprise-only SSO restriction — the third one is the interesting signal.

## Scope, and what this is not

A method with guardrails, not a CI platform. No database, no scheduler, no dashboard. It will not
tell you a competitor's private pricing, their roadmap, or what their customers think — and it is
built to say so rather than guess.

Known gaps, stated plainly:

- **It does not capture buyer truth.** Nothing here interviews a buyer about why they chose, rejected,
  or delayed. `ci-pattern-check` consumes win/loss material; it does not produce it.
- **It does not discover competitors you omitted.** `ci-portfolio` works from the alternatives you
  already know about.
- **It does not deliver answers into a seller's workflow.** No retrieval by account, persona, or
  stage.
- **It does not observe whether guidance was used.** `ci-weekly` records what a human declares.
- **It is not roadmap prioritization.** Mention frequency is not frequency × severity × buyer
  importance × strategic fit.
- **There is no enterprise governance here** — no source allowlists, retention enforcement,
  revocation, or kill switch. It is markdown.

It also will not help you obtain information by bypassing a paywall, using a competitor's
credentials, misrepresenting who you are, or soliciting confidential information from a competitor's
people. Those questions come back `unresolved`.

## Contributing

Issues and PRs welcome. Unsupported — use at your own risk, and read a diff before you ship anything
to sellers.

## Credit and licence

Created by Eric Do Couto, Head of Marketing at [Visualping](https://visualping.io), as the ungated
take-home for a workshop at Product Marketing Summit SF 2026. Visualping hosted that workshop and is
one optional monitoring integration here — the skills are built to run without it. This is a personal
repository, MIT-licensed and unsupported.

The design is a research-backed hypothesis pending primary validation, not a description of observed
product-marketing behaviour. Three sources shaped it, each with its limits stated:

- [Forrester on market and competitive intelligence programs](https://www.forrester.com/blogs/five-findings-about-todays-market-and-competitive-intelligence-programs/)
  — intelligence teams are shifting from information to implications. A published summary of an
  analyst study; the underlying sample and method are not detailed in the post.
- [Clozd, State of Win-Loss](https://www.clozd.com/state-of-win-loss) — teams combining call
  recordings with win/loss report better feedback quality. Vendor-sponsored research into the
  category that vendor sells; treat as an association, not a causal finding.
- [Product Marketing Alliance, State of Product Marketing 2025](https://www.productmarketingalliance.com/state-of-product-marketing-report-2025/)
  — **44.3% of *responding* product marketing teams are one or two people.** That figure is the real
  design constraint here. It describes a self-selected survey population of PMA-affiliated
  practitioners, not the global profession.

None of the three is a random probability sample of product marketers. Two are published by
organizations with a commercial interest in the finding. The evidence discipline in this plugin is an
opinion about good practice, not a validated result.

MIT. See [LICENSE](LICENSE).
