# CI Stack

Seven skills for product marketers who need to turn competitor evidence into useful decisions.
Start with a page change, a sales-call excerpt, or a question about a competitor. Get a sourced
brief, a proposed battlecard edit, a pattern check, or an internal update.

Each skill works from supplied evidence. You can try the examples without a monitoring account,
CRM, or Slack connection. The skills run in Claude Code or Codex; connectors and scheduling are
optional additions.

## Install

In Claude Code:

```text
/plugin marketplace add edoc33/ci-stack-skills
/plugin install ci-stack@ci-stack
```

Follow the install summary. Run `/reload-plugins` if it asks you to.
The commands follow [Claude Code's plugin installation](https://code.claude.com/docs/en/discover-plugins).

For Codex, download or clone this repository, then run from its root:

```sh
python3 scripts/install_codex.py --dest "$HOME/.agents/skills" --dry-run
python3 scripts/install_codex.py --dest "$HOME/.agents/skills"
```

The local installer copies all seven skills and their required reference files. It refuses to
replace an existing skill. Restart Codex if the new skills do not appear. Codex supports this
[user skill location](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).
Python 3.10 or later is required only for the installer and repository checks.

Already installed? Follow [the upgrade instructions](docs/getting-started.md#update-an-existing-installation)
to get version 0.3.0 and preserve any local customizations.

## Run your first skill

In Claude Code, use `/ci-stack:ci-triage`. In Codex, use `$ci-triage`. Then paste:

```text
This is a fictional example. Return the brief here; no files or live tools needed.
We sell to IT teams that require SSO. Our current comparison says AcmeFlow only
includes SSO on Enterprise. We need to review that claim before a sales call.
Source: https://acmeflow.example/pricing, US page, signed out.
Before, captured 2026-08-04: "Team: SSO available on Enterprise only."
After, captured 2026-08-06: "Team: SSO included."
These pasted extracts are the preserved evidence. We have no product test.
Does this change our seller guidance? Leave unknown owners and deadlines unknown.
```

You should get a draft that distinguishes the published change from proof that SSO works.
It should name the evidence, uncertainty, and recommended next action. It should leave approval
pending. A usable result may recommend checking the claim before editing the battlecard.

## Choose a skill

| Your question | Skill | What you get |
|---|---|---|
| What should we monitor? | `ci-portfolio` | A decision-linked watchlist, ignore rules, alert prompts, and a generic URL export |
| Does this change matter? | `ci-triage` | A decision brief with evidence, uncertainty, and a recommended response |
| Can we support this claim? | `ci-corroborate` | A source comparison, verification verdict, and supportable draft wording |
| Which battlecard lines need changing? | `battlecard-patch` | A proposed diff against the current card, including stale claims and reversals |
| Is this one deal or a recurring issue? | `ci-pattern-check` | A count over a defined cohort, coverage limits, and a scoped conclusion |
| What should the team know this period? | `ci-weekly` | A weekly, twice-monthly, monthly, or custom-period update and decision views |
| What did the buyer say about a competitor? | `ci-call-mentions` | A contextual call excerpt and Slack draft, with held items explained |

Start with the skill that fits the input you already have. There is no required sequence through
all seven. For a new CI program, the usual loop is portfolio → triage → period update.

- [First runs for all seven skills](docs/getting-started.md)
- [How the workshop workflows fit together](docs/workflows.md)
- [Evidence and file contract](plugins/ci-stack/reference/decision-brief.md)
- [Validation and known limits](docs/validation.md)
- [PMA workshop materials](https://github.com/edoc33/ci-stack-skills/tree/pma-workshop-2026/workshops/pma-2026)

The workshop branch retains dated exercises and reference outputs. Install from this repository's
`main` branch for the current skills and use the first-run guide above for current setup.

## Add your own context

Tell the agent your decision, customer segment, known competitors, and where to save CI work.
It can reuse these details in `ci-context.md` under that directory. Start with the
[fictional context example](plugins/ci-stack/examples/ci-context.example.md). Include owners and deadlines
when known. Missing metadata stays unknown; it should not prevent an initial draft.

Use permitted, minimized exports for internal calls and CRM data. Your agent provider processes
what you supply under your account and organization settings. This repository adds no telemetry,
background service, or credentials. Keep private outputs out of public repositories.

## Connect and automate when the draft works

An AI skill provides analysis instructions. A connector retrieves or writes data. A runner such as
n8n or GitHub Actions starts and coordinates the job. Your CRM and second brain supply deal context,
battlecards, brand rules, and history. Slack or Teams carry the reviewed output.

The repository includes skill instructions, examples, and a local Codex installer. It does not
include deployed n8n workflows, GitHub Actions jobs, CRM field adapters, a timeline database, or a
newsletter delivery service. `ci-call-mentions` documents optional authorized Slack delivery; it
requires a connector and a durable delivery record. The other skills produce drafts and proposals.
See the [workflow guide](docs/workflows.md) for the pieces each example needs.

## Contributing and licence

Created by Eric Do Couto, Head of Marketing at [Visualping](https://visualping.io), for the PMA
competitive intelligence workshop. Visualping is one optional source of page-change evidence.
This is a personal, MIT-licensed repository. Issues and pull requests are welcome.

Run `python3 -m unittest discover -s tests -v` before proposing installer changes. For skill changes,
include a realistic input and the observed output behavior. See [LICENSE](LICENSE).
