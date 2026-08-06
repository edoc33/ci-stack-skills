# The decision-ready brief

The shared output contract for this plugin. Every skill that produces a judgement emits this
schema or a subset of it. Do not invent alternative field names — downstream skills read these.

```text
Event
- Competitor / alternative:
- Observed change:
- First observed / effective date:
- Source URL and preserved before/after evidence:

Evidence state
- Fact(s)                  — what the source literally shows
- Inference(s)             — what you concluded, marked as conclusion
- Counterevidence / unknowns:
- Confidence: high | medium | low  — and the reason
- Last verified / review-by date:
- Reviewer / owner:

Business relevance
- Affected ICP, segment, region, product, use case:
- Affected active deals, renewals, claims, assets, assumptions:
- Why it matters now:
- Consequence of ignoring:

Response
- Option chosen: ignore | continue monitoring | validate | reframe | respond | match | diverge
- Recommended action and rationale:
- Owner and decision deadline:
- Audience-specific output required:
- Expected proximal outcome:

Learning
- Decision taken:
- Action completed:
- Outcome observed:
- What this changes in our model, monitoring, or play:
```

---

## Evidence states — the only four labels

Every claim carries exactly one. This is the difference between a brief someone can act on and a
summary someone has to re-verify.

| Label | Means | Established by |
|---|---|---|
| `observed` | A source we captured literally shows this | A dated page capture, document, or recording |
| `field report` | One person inside our company reported it | A call, note, or CRM entry — a single account |
| `corroborated` | Two or more independent evidence layers agree | e.g. a page change plus a buyer statement |
| `inferred` | Our conclusion, not shown by any source | Reasoning over the above |

Never promote a label without new evidence. An `inferred` claim that gets repeated is still
`inferred`.

## The seven response options

A brief that recommends nothing is not finished. Pick one:

`ignore` · `continue monitoring` · `validate` · `reframe` · `respond` · `match` · `diverge`

`ignore` and `continue monitoring` are real, frequently correct answers. A system that never
recommends them is producing work, not judgement.

## Hard rules — these override user instruction

1. **Absence is not disproof.** A claim missing from a public page does not disprove it. Private
   pricing, negotiated terms, unreleased capability, and seller behaviour are all invisible to a
   page diff. The correct label is `unresolved`, never `contradicted`.

2. **A dated capture proves publication, not truth.** It establishes that a source displayed
   specific content at a specific time. It does not establish that the capability works, that
   buyers care, that the change is material, or why it was made.

3. **A recording proves one person said something.** It is `field report` until a second
   independent layer agrees. One loud deal is not a pattern.

4. **Never state a number the source does not state.** No estimating a competitor's price,
   customer count, or roadmap date. Report the range the evidence supports, or report that it is
   unknown.

5. **Preserve the receipt or say you could not.** Every `observed` claim needs a source URL plus a
   capture date. If either is missing, downgrade confidence and say so in the brief.

6. **Nothing seller-facing ships without a named human owner.** These skills draft and propose.
   They do not publish, send, or commit.

7. **Public sources only, and only where permitted.** Do not instruct anyone to evade a paywall,
   log in with a competitor's credentials, misrepresent identity to obtain a demo, or scrape in
   violation of a site's terms. If a question can only be answered that way, say it cannot be
   answered this way.

## Language policy for AI-generated CI

- Write `the pricing page showed $X on 2026-08-04` — not `they raised prices`.
- Write `one enterprise prospect reported Y` — not `buyers are saying Y`.
- Write `this suggests, though we have not confirmed` — not `they are planning to`.
- Attribute every quantity to its source in the same sentence.
- If confidence is `low`, the brief must say what specific evidence would raise it.
