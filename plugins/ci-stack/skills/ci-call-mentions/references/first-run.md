# Try a call briefing with fictional data

The [included transcript](example-transcript.json) describes a fictional buyer discussing three
fictional competitors. It contains a current evaluation, a correction about former use, and a
seller suggestion that the buyer rejects. The source URL uses `example.invalid` and is an
illustrative locator. Keep all practice output visibly fictional and unsent.

After installing the skill, paste this request into your agent:

```text
Use ci-call-mentions in draft mode with its bundled references/example-transcript.json.
The companies, speakers, quotes, dates, and source link are fictional. Use only that file.
Use a new ci-call-practice folder under the current working directory as my CI root;
resolve it to an absolute path and show the output paths before writing.
Draft the Slack items and extraction ledger. Explain any held mentions. Do not send anything.
```

The fixture travels with the skill. The agent should resolve it relative to `SKILL.md`, regardless
of where the skill was installed. This practice run needs only an agent that can read the installed
files and write to the chosen folder. If file access is unavailable, paste the fixture contents
into the conversation and request inline drafts.

Review these parts of the result:

- The AcmeFlow item should retain the buyer's evaluation context and a follow-up about what the
  pilot must establish.
- CedarQueue should remain in the ledger as past use at another employer, with the correction
  preserved. It should not become an incumbent at this account.
- MorrowDesk should remain in the ledger as a rejected suggestion. The seller's question should
  not become evidence of a buyer evaluation.
- Every item should link back to preserved fixture text. Delivery readiness should remain false.

A readable candidate could look like this. It is illustrative wording, not a required template:

```text
FICTIONAL PRACTICE DRAFT
Northstar mentioned AcmeFlow | Active evaluation
Buyer, 12:41: "We're evaluating AcmeFlow's Team plan. The pilot needs to show whether our support team can route requests without engineering help."
PMM note: Request routing is part of this evaluation. Ask which routing task the pilot must prove.
Source: https://example.invalid/calls/practice-001 | 12:41
```

The ledger carries the remaining classifications, evidence limitations, and draft statuses. The
Slack draft stays short enough for a teammate to decide whether to open the source.

# Use your own call next

Provide one permitted export or connector response, the relevant competitor list, and the same
CI root. Include the speaker role mapping if the export has only names or numeric IDs. A pasted
excerpt is enough for an initial draft when it contains the complete relevant exchange. Missing
roles, times, source links, or stable IDs will be named as gaps and will hold delivery.

The next implementation step is to configure the provider, agent runner, Slack destination, and
persistent delivery state described in [setup.md](setup.md). A successful practice draft proves
that the skill can interpret the fixture; it does not prove provider access or live delivery.
