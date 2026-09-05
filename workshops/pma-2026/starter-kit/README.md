# AcmeFlow workshop starter kit

ILLUSTRATIVE WORKSHOP FIXTURE. Every company, buyer, deal, quote and test result here is fictional. Dates describe a staged exercise. This is a public-safe practice case, separate from the presentation's historical competitor captures.

Practice one decision: should TaskBridge change its seller guidance about AcmeFlow's Team-plan SAML SSO?

## Start

1. Extract this folder and open a terminal in it.
2. Run `python3 prepare_session.py`. It creates a fresh local session and prints the path to exact, copy-paste prompts.
3. Open Claude Code in this folder. Install the public plugin using both commands:

```text
/plugin marketplace add edoc33/ci-stack-skills
/plugin install ci-stack@ci-stack
```

Run `/reload-plugins` if prompted. The commands and namespace match the repository reviewed at commit `cd2fc5e097a7a7f3e87a6cfa11acb0fc0e722653`.

4. Open the generated `session/session-start.md` and paste its setup message. Then paste `session/prompts/01-triage.md`.
5. Compare your output with `worked/01-triage/`. Continue with the generated corroboration and patch prompts. Use the separate weekly fixture when you want to practice recorded human decisions.

Installation needs an internet connection and a configured Claude Code account. The exercise requires no web browsing or live monitoring account. Claude Code still sends prompts and selected content to its model provider. For an entirely offline exercise, use `participant-worksheet.md` and compare answers with `worked/` by hand.

## What to open

| File or folder | Purpose |
|---|---|
| `business-context.md` | The buyer, decision, deadline and fictional owner |
| `evidence/` | Complete preserved text fixtures and a hash manifest |
| `inputs/` | Existing battlecard, candidate pages, deal cohort and staged weekly records |
| `participant-worksheet.md` | A printable exercise that works without Claude Code |
| `prompts/` | Portable prompt templates; the setup script supplies absolute paths |
| `worked/` | Authored reference answers, labeled illustrative; these are not model execution logs |
| `output-excerpts.json` | Short editable artifact excerpts for presentation design |
| `VALIDATION.md` | What was checked, what ran, and what remains untested |
| `validation/runtime-output/` | Actual model drafts from the completed triage test |

## The exercise

The supplied price-page change has three claims: price, automation usage, and SAML SSO. Judge them separately. The SSO claim affects the stated seller-guidance decision. A published claim alone leaves working product behavior untested.

Use the simulated independent test records to check the narrow Team-plan/Okta scenario. Preserve the original broader question about all paid plans. A test of one plan and one identity provider leaves the broader question unresolved.

The original battlecard contains obsolete claims. Produce a proposed patch with sources, capture dates and review status. The worksheet participant acts as reviewer; generated files stay drafts until a person records a decision about the exact version.

The optional pattern exercise counts independent deals rather than repeated calls. The weekly exercise has its own supplied, fictional brief corpus so accepted, rejected and pending decisions are available to practice. Its historical statuses are story data, not permission to approve or distribute your current outputs.

## Scope

The included skills produce local drafts. This kit contains no live monitors, scheduler, CRM connection, chat integration, wiki sync or publishing workflow. The routing artifacts in `output-excerpts.json` are proposed examples for review.

No real customer information belongs in this folder. All URLs use reserved example domains and serve as fictional locators. Read the matching local files instead of opening those URLs.

## Source and licence

The base AcmeFlow price/usage/SSO text comes from the MIT-licensed `edoc33/ci-stack-skills` sample at the reviewed commit. Its original unmodified payload is in `reference/`. `reference/UPSTREAM-LICENSE` preserves its licence. Context, synthetic captures, independent test fixtures, exercises and worked outputs were authored for this kit. The kit's authored materials use the same MIT licence.

Run `python3 validate.py` to repeat deterministic fixture and contract checks. Read `VALIDATION.md` before describing the kit as tested.
