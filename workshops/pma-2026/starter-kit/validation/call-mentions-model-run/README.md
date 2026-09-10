# Call-mentions draft test

An independent Codex agent ran `ci-call-mentions` on the three fictional transcripts without reading the worked answers. It produced one Slack candidate and held the negated and seller-only mentions. Quotes, timestamps, speaker roles, preserved evidence, default statuses and stable keys were checked against the inputs.

The run found an ambiguous location for the delivery payload in the schema. The contract now specifies one payload per eligible item and null for held items. `original-extraction-draft.json` preserves the original; `extraction-draft-schema-repaired.json` removes only the duplicate top-level payload. All eight schema-repair checks passed.

The model's full Markdown output includes an audit record after the concise Slack item. `result.json` describes test limits. Absolute local paths were replaced with `<CI_ROOT>`; no source URL was opened and no message was sent.
