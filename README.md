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

## The six

| Skill | Use it when | Gives you |
|---|---|---|
| `ci-portfolio` | You don't know what to watch, or your alerts are noise | A portfolio where every page is tied to a decision, with a safe-to-ignore rule and an alert prompt. Plus a bulk-import CSV |
| `ci-triage` | A change came in and you need to know if it matters | A decision-ready brief: evidence state, counterevidence, confidence, affected deals, one of seven actions, an owner, a review date |
| `ci-corroborate` | A claim is about to go in front of a customer or an exec | `corroborated` / `contradicted` / `unresolved`, the phrasing you may use, and the phrasing you may not |
| `battlecard-patch` | An approved brief needs to reach sellers | A redlined diff with the dated receipt inline, a freshness stamp, and a list of claims elsewhere in the card that just went stale |
| `ci-pattern-check` | Someone wants to change positioning because of one deal | `anecdote` / `emerging signal` / `pattern`, with the denominator stated and competing explanations |
| `ci-weekly` | The exec asks what changed | A one-page update, an ignore log, and a decision-and-outcome record |

They chain: `ci-portfolio` → `ci-triage` → `ci-corroborate` → `battlecard-patch` → `ci-weekly`,
with `ci-pattern-check` feeding the field-evidence layer. Each also works standalone.

## What holds it together

Every skill reads one shared contract, [`reference/decision-brief.md`](plugins/ci-stack/reference/decision-brief.md).
It defines the brief schema and four rules the skills apply even when asked not to:

1. **Four evidence labels, never upgraded without new evidence** — `observed`, `field report`,
   `corroborated`, `inferred`.
2. **Absence is not disproof.** A claim missing from a public page is `unresolved`, not
   `contradicted`. Private pricing, negotiated terms, unreleased capability and seller behaviour are
   invisible to a page diff.
3. **A dated capture proves publication, not truth.** It shows what a page displayed and when. Not
   that the capability works, that buyers care, or why it changed.
4. **`ignore` is a real answer.** Two of the seven recommended actions are to do nothing. A system
   that never picks them is producing work, not judgement.

The skills draft and propose. They do not publish, send, or commit — every seller-facing output goes
to a named human first.

## Requirements

Claude Code. That is the hard requirement.

**No monitoring account is needed.** Every skill accepts a pasted before/after diff, so you can run
the whole method by hand before you automate any of it.

Optional, and all bring-your-own:

- A change-monitoring tool for detection. `ci-triage` reads
  [Visualping](https://visualping.io)'s webhook payload natively (`added_text`, `removed_text`,
  `summarizer`, `important`, `datetime`) and `ci-portfolio` can create jobs via its API, but any tool
  that reports a before/after works, and the portfolio CSV is generic.
- A meeting recorder export for `ci-pattern-check` — tl;dv, Gong, Fireflies, Zoom, or plain notes.
- A CRM export for the pattern and outcome layers.

Nothing here calls a hosted service of ours, and nothing phones home.

## Try it in two minutes

```
/ci-stack:ci-triage
```

Then paste [`examples/sample-webhook-payload.json`](plugins/ci-stack/examples/sample-webhook-payload.json)
when asked for input. You'll get a brief, a recommended action, and a log line.

## Scope, and what this is not

This is a method with guardrails, not a CI platform. It has no database, no scheduler, and no
dashboard. It will not tell you a competitor's private pricing, their roadmap, or what their
customers think — and it is built to say so rather than guess.

It also will not help you obtain information by bypassing a paywall, using a competitor's
credentials, or misrepresenting who you are. Those questions get answered `unresolved`.

## Contributing

Issues and PRs welcome. Unsupported — use at your own risk, and read a diff before you ship it to
sellers.

## Credit and licence

Built by [Eric Do Couto](https://github.com/edoc33). The evidence discipline draws on published
research into how product marketers actually work: Forrester's 2026 finding that intelligence teams
are moving from information to implications, Clozd's win/loss work on evidence convergence, and the
Product Marketing Alliance's finding that 44.3% of product marketing teams are one or two people —
which is the real design constraint here.

MIT. See [LICENSE](LICENSE).
