# Fictional call fixtures

All companies, calls, people, timestamps, capture dates, quotes, and URLs in this folder are
invented. The provider label illustrates the normalization shape; no provider was contacted.

- `active-evaluation.json`: buyer explicitly reports an active AcmeFlow evaluation and an Okta test.
- `negated.json`: seller asks about AcmeFlow; buyer explicitly denies a current evaluation.
- `seller-only.json`: seller introduces AcmeFlow; buyer provides no evidence of evaluation.

Run `ci-call-mentions` with these inputs and a supplied absolute CI root. Ask for a Slack draft and
JSON ledger. Do not enable delivery. The worked result is in `../../worked/07-call-mentions/`.

The first transcript uses the same fictional Northstar/AcmeFlow example shown in the presentation.
