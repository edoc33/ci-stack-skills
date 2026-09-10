# Try a battlecard patch with fictional data

Paste the prompt below into a session where this skill is available. Every company, quote, and
receipt in this example is fictional. The `.example` URLs identify the fixture; do not browse them.
The preserved text is the evidence for this exercise.

```text
Use battlecard-patch to propose a change to the card below. Work inline and make no external
changes. Use only this fictional fixture. Review the supplied history through August 9, 2026.
Our audience is an internal PMM reviewing seller guidance. The reviewer is unassigned.

Current card, supplied in full:
# AcmeFlow battlecard
## Trial
AcmeFlow only offers a seven-day trial.
## Discovery
Ask which workflow the prospect plans to test.

Brief ID: fixture-trial-reversal
Competitor / alternative: AcmeFlow (fictional)
Observed change: The published trial wording returned to 14 days after showing 7 days.
First observed / effective date: August 9, 2026; effective date unknown
Proposition: The US public trial page displayed "Start your 14-day trial" on August 9.
Source locator and preserved evidence: receipt-3 below
Evidence basis: observed
Verification: single-source
Handling: public (synthetic fixture)
Confidence: high for the captured page wording; product entitlement untested
Counterevidence / unknowns: The seven-day wording appears in receipt-2. We have no contract or
product test confirming the actual entitlement, and no observations after August 9.
Recommended option: respond
Rationale: Remove stale seller wording and have the PMM check the current trial entitlement.
Owner and decision deadline: unassigned; unknown
Human decision: pending
Review status: draft
External-use approval: not approved
Action status: not started

Related receipts, all supplied in this fixture:
receipt-1: https://acmeflow.example/trial, 2026-08-03T10:00:00Z,
US, English, public logged-out page. Preserved text: "Start your 14-day trial."
receipt-2: Same URL and context, 2026-08-06T10:00:00Z.
Preserved text: "Start your 7-day trial."
receipt-3: Same URL and context, 2026-08-09T10:00:00Z.
Preserved text: "Start your 14-day trial."
```

The proposal should show the wording change in order, identify the stale seven-day assertion, and
preserve the discovery section. The current product entitlement remains untested. A useful result
can delete the unsupported claim and put the observed page wording in an internal review note.
The skill should not replace one unsupported seller assertion with another.

For local files, replace the pasted card and receipts with their paths and supply an absolute CI
root. The review record goes under `updates/`; a proposed copy can sit beside the supplied card.
The original stays intact. After PMM review, pass the accepted wording to the workflow that updates
your second brain. Installing this skill alone does not connect to Notion, Google Drive, or Slack.
