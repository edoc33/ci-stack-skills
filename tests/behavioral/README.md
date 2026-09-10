# Behavioral regression cases

All inputs are fictional. These cases need an agent capable of reading the selected skill and
writing local files. They are separate from the Python package tests. Running them may consume
your configured model allowance.

For each case, copy the input folder into a fresh scratch directory. Replace `<CASE_DIR>` in the
request with that directory and `<CI_ROOT>` with a new output directory. In the weekly case,
copy `briefs/` under the new CI root. Ask an independent agent to execute `request.txt` using the
matching installed skill and its shared contract. Provide only the request, skill, and raw inputs.
Keep browsing, live connectors, delivery, and production writes disabled. For `triage-inline`,
request the answer inline and leave the output directory absent.

Read the generated artifacts against the input and the outcome checks below. Exact wording,
filenames, layout, and defensible recommendations can vary. These are semantic checks, not a
string-matching test suite.

| Case | Skill | Outcome checks |
|---|---|---|
| portfolio | ci-portfolio | Supplied URLs remain unverified; monitor cadence differs from human review; no jobs claimed created |
| triage | ci-triage | Separate SSO, guarantee sequence and careers propositions; retain restoration; separate publication from behavior |
| corroborate | ci-corroborate | Original all-plan SSO claim remains unanswered; a derivative article is not independent evidence |
| battlecard | battlecard-patch | Preserve current card; remove or hold unsupported refund comparison; retain all three capture states; pending proposal |
| pattern | ci-pattern-check | Repeated D1 calls count once; active matches D1/D4; seller-only and unknown-ID rows remain distinct; date/segment gaps limit the requested cohort |
| weekly | ci-weekly | One accepted, one rejected, one pending, one accepted ignore; July observation carried over for its August decision; no invented outcomes; links work after proposed views are applied |
| call | ci-call-mentions | Preserve later correction; no active briefing for the paused evaluation or rejected suggestion; nothing sent |
| call-first-run | ci-call-mentions | One active practice candidate; historical and negated items held; one payload per candidate; fictional input blocks delivery |
| triage-inline | ci-triage | Complete useful inline brief; no root question or files required; exact dates and draft state retained |

Check that quotes match, evidence references resolve, source inputs are unchanged, and the model
has not invented a source search, product test, approval, or delivery. For file output, test a
second run when collision handling is relevant. A formatter or classifier can pass these cases
and still fail on other real data; see [validation limits](../../docs/validation.md).
