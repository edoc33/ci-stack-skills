# PMA workshop: the $274 competitive intelligence stack

[Download the complete workshop pack](https://raw.githubusercontent.com/edoc33/ci-stack-skills/pma-workshop-2026/workshops/pma-2026/pma-workshop-kit.zip)

The pack contains a fictional practice case, all seven skill exercises, worked outputs and a visual guide to 27 source types.

- [Start the AcmeFlow exercise](starter-kit/README.md)
- [Try the Gong/tl;dv mention-to-Slack example](starter-kit/inputs/call-mentions/README.md)
- [Read the 27-source visual guide (PDF)](source-reference/27-source-reference.pdf)
- [Use the participant worksheet](starter-kit/participant-worksheet.md)
- [See exactly what was tested](starter-kit/VALIDATION.md)

Extract the pack and open `starter-kit/README.md`. The first exercise creates a dated brief and a chosen next action. You can use Claude Code or complete the worksheet manually.

The synthetic AcmeFlow case is separate from the presentation’s historical competitor evidence. All people, deals, quotes and product behavior in that practice case are fictional. The source guide labels historical captures and current page examples individually.

The workshop prompts produce local drafts. The new `ci-call-mentions` skill can also deliver a contextual internal briefing through an explicitly authorized Slack connector after the participant configures it. Monitor creation, schedules and CRM writes need separate setup. The validation report records the checks run and the model tests completed, including the earlier triage attempt that did not finish.

## Install the skills

In an authenticated Claude Code session:

```text
/plugin marketplace add edoc33/ci-stack-skills
/plugin install ci-stack@ci-stack
```

Run `/reload-plugins` if prompted. Follow the starter kit’s setup script for exact prompts and file paths.

## Source credits

The guide links each public-page screenshot to its source and labels its capture date. Original source images remain unchanged. The MIT licence covers the authored code and practice materials; third-party source screenshots retain their respective rights.
