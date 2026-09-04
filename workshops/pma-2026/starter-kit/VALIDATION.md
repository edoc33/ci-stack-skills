# Validation report

Validation date: 4 September 2026. This report describes the authored synthetic workshop kit.

## Result

**125 offline checks passed.** Run `python3 validate.py` to reproduce them. Structured results are in `validation/results.json`.

The checks cover JSON parsing, preserved evidence hashes, exact alignment with the upstream fictional added/removed text, local source availability, separate claim records, shared-contract enums, generated approval defaults, revisit rules, independent source-origin labels, narrow versus original corroboration questions, exact unified-patch applicability, preservation of unrelated card text, independent-deal counts and coverage, weekly human-decision counts, CSV formula safety, all 13 slide excerpts and their source/context labels.

The setup script was executed in a temporary copy contained inside this kit. It generated six absolute-path invocation files, copied the original card unchanged, kept all paths inside the copied kit, and refused a second run rather than overwriting a session.

Negative probes confirmed that the validator rejects an auto-approved draft and a missing revisit condition, that adding a duplicate call leaves the independent-deal fraction unchanged, and that altered source bytes fail the preservation hash check.

## Contract review

Reviewed source: `edoc33/ci-stack-skills`, commit `cd2fc5e097a7a7f3e87a6cfa11acb0fc0e722653`. The README, all six skills and shared decision-brief contract were read, together with the presentation's skills audit.

- Triage creates separate SSO, price and usage propositions. It preserves the affirmative new SSO statement and treats the summarizer/IMPORTANT output as input to check.
- Corroboration retains the original all-paid-plans question as unresolved while the narrow Team/Okta test proposition is corroborated inside the fiction. Pricing and docs share one source origin. The two simulated tests represent independent original observations within the scenario; they are not real empirical tests.
- The current patch skill blocks customer-facing single-source claims. The worked patch therefore holds the price and usage replacements as internal review notes. A corroborated but still-draft Team/Okta handoff produces an awaiting-review proposed patch. The original card remains unchanged.
- The pattern result is 3 of 6 recorded eligible deals, covering 6 of 8 eligible deals. Nine eligible notes collapse to six cases. The incomplete short-window dataset earns repeated signal, with no causal win/loss conclusion.
- The weekly corpus is a separate supplied-fictional-history branch. It records 2 accepted decisions, 1 rejected recommendation and 1 pending recommendation. Its accepted ignore decision has a revisit rule. Approval and outcomes are never inferred from artifact presence.
- The synthetic workflow avoids actual personal/customer data. All source locators use reserved example domains. No live API payload compatibility or vendor import entitlement is claimed.

## Runtime smoke-test attempt

Installed Claude Code version `2.1.259` was inspected using `--version`, `--help` and `auth status`. Model-provider use of this fully synthetic fixture was explicitly authorized for one restricted first-triage test.

**Blocked by authentication before model execution.** `claude auth status` exited 1 and reported `loggedIn: false`, `authMethod: none`, and `apiProvider: firstParty`. No Anthropic API key/auth token, Claude OAuth token, or alternate-provider mode was set in the process. The relevant diagnostic is saved in `validation/claude-smoke-status.json`.

No credentials were printed, searched for or copied. No model invocation, plugin invocation or end-to-end skill execution occurred. Callable-tool restriction and isolated output paths therefore remain untested at runtime.

Worked outputs are authored reference answers. Deterministic tests establish fixture consistency and exercise mechanics; they do not prove that a model will follow every instruction.

## Remaining checks before presenting

Run the complete triage/corroboration/patch sequence in a fresh Claude Code session with an authorized model-provider connection. Confirm that the current plugin loads, can read its shared reference, respects the synthetic scenario and root, preserves uncertainty, returns separate claim records, and writes the expected artifact types. Review generated language against the rubric; accept equivalent defensible answers rather than demanding exact prose.

The kit's generated session files contain local absolute paths and stay outside the portable ZIP. No live monitor, product test, CRM route, Slack message, wiki entry, scheduled task or publication was executed.
