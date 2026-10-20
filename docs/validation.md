# Validation for 0.4.0

Reviewed October 19, 2026. The seven skills retain their existing evidence and draft controls.
This release adds optional timeline, CRM-proposal, affected-deal, and review-insight modes,
first-run prompts, and a workflow mapping. The Cloudflare guide is a documentation assessment;
no Clef or Clairic inference or production adapter was exercised.

The ten package and installation checks passed against this release, including self-contained
copies of all new references, matching version metadata, and resolving local documentation links.
All seven skills passed the skill-creator structural validator. The exporter checks used temporary
directories and preserved the user's installed skills.

An independent Codex agent ran the four new fictional regression requests before reading their
expected outcomes. Each case used a separate scratch directory, with one shared agent context.
All four met their stated outcome checks:

| Mode | Observed result |
|---|---|
| Timeline | Retained the US 14→7→14 sequence, deduplicated R2, separated UK and logged-in observations, and left the undated record undated |
| CRM proposal | Preserved CedarQueue in O1's additive proposal, held O2's corrected history and ambiguous O3/O4 match, and returned no change for already-tagged O5 |
| Affected-deal brief | Worked without a card, matched O1's buyer criterion, held paused O2 and tag-only O3, preserved G1's approval scope, and held stale G2 |
| Review insights | Counted five distinct review records after deduplication, retained positive and improved experiences and the add-on distinction, and avoided customer-prevalence claims |

Eight additional fictional worked examples covered the workshop outputs. The agent that authored
those fixtures also produced those example outputs; they are demonstrations, not blinded tests.
The independent regression cases above provide separate evidence for the four new modes.

These were single runs with no live connectors. Outputs were checked for resolving local links,
exact source quotes, preserved inputs and draft approval state. They remain human-readable prose:
some field values include explanatory text, so an execution adapter needs schema validation.
Output verbosity and repeatability are not established. A description-only discovery edit to
`ci-pattern-check` followed the regression run; its operative instructions were unchanged, and
its structural validation passed afterward.


The limitations below still apply. The September results are retained as dated evidence for the
unchanged workflows, rather than represented as new runs of this release.

## Validation for 0.3.0

Reviewed September 10, 2026. All seven skill entrypoints, their references, the shared contract,
onboarding, and workflow handoffs were reviewed. The checks support using supplied evidence to
produce reviewable drafts. They do not establish production integration readiness.

### Package and installation checks

Run from the repository root:

```sh
python3 -m unittest discover -s tests -v
```

Ten checks cover portable installation, required references, existing-file preservation, dry-run
behavior, cleanup after a failed copy, symlink collisions, repeat installation, matching package
versions, local document links, and the bundled transcript's metadata. All passed. All seven
SKILL.md files also passed the skill-creator structural validator. The Codex exporter was tested
in temporary directories, including paths with spaces, without modifying a user's installed skills.

### Independent model runs

Independent Codex agents executed nine fictional scenarios using the revised skills and only the
minimum raw inputs. They received no expected answer or implementation findings. The resulting
artifacts were reviewed for evidence scope, dates, deduplication, draft state, and preserved inputs.
The [regression cases](../tests/behavioral/README.md) contain the portable inputs and outcome checks.

| Skill | Observed result |
|---|---|
| ci-portfolio | Produced two provisional, unverified source rows, distinct check/review cadences, prompts and a generic CSV |
| ci-triage | Kept unrelated changes separate, retained a guarantee restoration, and recommended validation for the SSO claim; a separate inline run needed no files |
| ci-corroborate | Retained the original all-plan claim as unresolved and identified the news article's shared origin |
| battlecard-patch | Proposed removing an unsupported refund comparison, retained the restoration history, and preserved the original card |
| ci-pattern-check | Counted two confirmed evaluation cases among four known-ID observed cases; reported missing date/segment evidence for the requested cohort |
| ci-weekly | Reported one accepted decision, one rejected decision, one pending recommendation and one accepted ignore; labeled the July observation as carried over |
| ci-call-mentions | Held a paused evaluation after a correction; the first-run fixture produced one practice candidate and held the historical and rejected mentions |

The initial weekly run exposed a link-location issue: proposed views were saved in `updates/`,
while the final views belong at the CI root. The skill now places proposals beside their final
targets so relative source links retain their meaning when applied. The corrected follow-up run
passed: both proposal diffs target the fixed-name views, reconstruct the proposed content exactly,
and retain resolving source links from the final destination.
The final release review also aligned the bundled first-run example with those output paths and
checked the updated references in a fresh portable installation.

The model-generated research records were sometimes verbose. Shared guidance now asks for a
concise leading verdict, each limitation stated once, and linked detail instead of a repeated brief.
No claim is made that output length is deterministic.

## What remains untested

- Marketplace installation and automatic skill selection in a fresh Claude Code or Codex account.
- Live Gong, tl;dv, Visualping, CRM, wiki, Slack, or Teams connections.
- Live delivery, concurrent delivery claims, retries, or uncertain-send reconciliation.
- Real provider exports, retention configuration, scheduling, and model/API costs.
- Every possible missing-data, empty-period, date-boundary, source-injection, or provider variant.

The repo includes no live connectors, credentials, deployed schedulers, or production mutation
adapters. The documented delivery contract still requires its own implementation and end-to-end
tests. Earlier workshop model runs and authored worked examples remain dated historical evidence.

## Documentation sources

Install and workflow descriptions were checked against current official documentation:
[Claude plugin installation](https://code.claude.com/docs/en/discover-plugins),
[Codex skill locations](https://learn.chatgpt.com/docs/build-skills),
[n8n workflows](https://docs.n8n.io/build/understand-workflows/create-and-run-workflows),
[n8n AI Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent),
[GitHub Actions workflows](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows),
and [Visualping Reports](https://help.visualping.io/en/articles/10899969).
