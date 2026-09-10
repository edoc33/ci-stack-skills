# Try a pattern check with fictional records

Paste this prompt into a session where the skill is available. These are synthetic excerpts and
IDs. There is no real customer information or provider connection to configure.

```text
Use ci-pattern-check to answer: How often were buyers actively evaluating AcmeFlow in these
supplied opportunities during August 3 through August 9, 2026, UTC? Is this enough to change our
company-wide positioning? Work inline from this fictional fixture and make no external changes.

Each row is a call excerpt. opportunity_id is the independent case ID. We do not know how many
opportunities exist outside this export. A blank excerpt means that the call has not been coded.
The source field is a stable fixture locator and timestamp, not a web address to fetch.

opportunity_id,call_id,date,segment,rep,outcome,speaker,excerpt,source
D1,C1,2026-08-03,midmarket,R1,open,buyer,"We are comparing your product with AcmeFlow this month.",C1@05:10
D1,C2,2026-08-07,midmarket,R1,open,buyer,"Our AcmeFlow evaluation is still running.",C2@02:20
D2,C3,2026-08-04,enterprise,R2,won,seller,"Some teams also look at AcmeFlow.",C3@04:40
D3,C4,2026-08-05,midmarket,R1,lost,buyer,"We evaluated AcmeFlow last year. It is not on this shortlist.",C4@08:15
D4,C5,2026-08-06,midmarket,R2,open,buyer,"AcmeFlow and your product are the two options we are testing.",C5@03:05
D5,C6,2026-08-07,enterprise,R2,open,,,C6@unknown
D6,C7,2026-08-08,midmarket,R1,won,buyer,"We ruled out AcmeFlow before starting this evaluation.",C7@06:30
```

A useful result counts D1 once, separates active evaluations from seller, historical, and rejected
mentions, and keeps D5 unknown. The raw supplied cohort is six opportunities; two show active
evaluation and one is uncoded. Coverage of all opportunities is unknown. The two positive cases
occur in midmarket, which is useful context for further validation. These records alone do not
establish an all-market prevalence estimate or that a competitor caused a loss.

For real data, provide only the authorized fields needed for the question. Stable anonymous deal
IDs are usually enough. If the input is filtered to competitor mentions or closed-lost deals, say
so in the prompt. That selection changes what can be concluded.

For a saved result, add an absolute CI root and request local output. The analysis goes to
`patterns/YYYY-MM-DD-<question-slug>.md`. `ci-weekly` can link to it. An automation that tags live
opportunities needs a separate transcript-to-CRM mapping, write connector, and authorization.
