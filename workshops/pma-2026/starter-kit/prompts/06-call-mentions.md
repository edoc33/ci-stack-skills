# Call mentions to Slack

/ci-stack:ci-call-mentions

Run in draft mode using only these fictional local fixtures:

- {{KIT_ROOT}}/inputs/call-mentions/active-evaluation.json
- {{KIT_ROOT}}/inputs/call-mentions/negated.json
- {{KIT_ROOT}}/inputs/call-mentions/seller-only.json

Canonical CI root: {{CI_ROOT}}

Extract mentions with surrounding context, speaker, exact excerpt, supplied timestamp and source locator. Draft the eligible internal Slack briefing with a short PMM note. Save every extraction decision, including held mentions and reasons, and initialize review/decision states as pending. Keep the fictional label. Source URLs are fictional locators, so read the local fixtures rather than browsing. Do not send messages, call live connectors, read worked answers or change the source files.
