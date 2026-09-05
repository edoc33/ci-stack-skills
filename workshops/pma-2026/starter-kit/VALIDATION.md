# Validation report

Validation date: 5 September 2026. This report describes the authored synthetic workshop kit.

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

## Runtime test

One `ci-stack:ci-triage` run completed on 5 September 2026 using Claude Code 2.1.259, `claude-opus-5[1m]`, and medium reasoning effort. It took 164.25 seconds and saved all three claim briefs plus the decision-log view.

The test loaded the public plugin’s files locally with `--plugin-dir`. It invoked the skill, read its shared reference, and used a fresh copy of the fictional kit. The revised first prompt asks for concise briefs and exact capture dates. Marketplace installation was not exercised.

The tool inventory was limited to Read, Write, Edit, Glob, Grep and Skill. The trace contains no tool errors or permission denials. All generated writes stayed under the stated CI root. The 42 hashed evidence, input and plugin files were unchanged. Authored worked answers were not read.

File checks confirmed separate SSO, price and automation-usage briefs and the defaults `Human decision: pending`, `Review status: draft`, and `External-use approval: not approved`. Manual source review confirmed the primary quotations and capture dates. Published-page evidence remained distinct from working Team/Okta behavior. The decision-log view matched the saved briefs. See `validation/claude-smoke-status.json` for the checks and `validation/runtime-output/` for the actual files, with only local root paths normalized.

The first attempt timed out after 300.02 seconds with two briefs saved. Its SSO draft also described captures one day apart as “two days later.” That attempt is incomplete. The second attempt followed the revised prompt and passed the execution checks, with content findings that still need review. This result supports testing each generated answer against its evidence; it does not establish that future runs will be error-free.

Review found three issues in the saved drafts: the SSO brief attributes the Team-plan evaluation to TaskBridge instead of AcmeFlow; template-change language is more conclusive than the captures support; and price/usage briefs retain a `Forecast: omitted` field that the contract says to leave out. The drafts also exceed the 650-word target. The model output is preserved unchanged so readers can inspect these findings. Correct them in a reviewed working copy before using the language.

The earlier report that Claude Code was signed out came from a sandbox authentication check. The host was authenticated, and the actual model runs used that host session.

Worked outputs remain authored reference answers. The 125 offline checks test fixture consistency and exercise mechanics; they make no model calls.

## Remaining checks before presenting

Only triage was model-executed. Corroboration, battlecard patching, portfolio, pattern checking and weekly reporting have static contract and fixture checks. Run the full sequence in a fresh Claude Code session before using it as a live demonstration, and review the generated language against the evidence and rubric.

No live monitor, product test, CRM route, Slack message, wiki entry or scheduled task was executed. The kit’s generated session files contain local absolute paths and stay outside the portable ZIP.
