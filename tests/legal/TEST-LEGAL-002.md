---
title: "TEST-LEGAL-002 — Notice service date conflated with rent-increase effective date"
doc_type: informative
owner: Brian
last_verified: 2026-07-07
source_case: WordPress post 7996 (draft), "East Bay Rent Cap Update: New 2026–2027 Increase Limits for AB 1482, Oakland, Berkeley & Richmond" — reviewed by ChatGPT 2026-07-07, same day as drafting, first real test of the Claude-drafts / ChatGPT-reviews workflow
---

# TEST-LEGAL-002

Second real entry in the `/tests` regression suite (see `TEST-LEGAL-001.md` for the first). Logged from an actual review, not invented. This case is also notable as the first real end-to-end test of the intended review workflow: Claude drafted directly in WordPress per `docs/01`–`03`, ChatGPT reviewed against the same three documents using the `docs/03` template, and the findings came back structured enough to act on directly — which is what this whole Operating System was built to make possible.

## Excerpt

From the "Before Your Next Rent Increase Notice" checklist and FAQ #1 of the draft, as originally published:

> "Confirm the notice's effective date falls within the correct rate's window — a notice dated before a jurisdiction's effective date must use the outgoing rate, not the new one."

> "Not yet, for most of these. AB 1482's 8.8% and Oakland's 2.3% don't take effect until August 1, 2026 — the current rates (6.3% and 0.8%, respectively) remain in effect for any notice served before that date."

## Rule IDs triggered

- `GATE-LEGAL-ACCURACY` — **FAIL** (Type A, content error)
- `GATE-LOCAL-ACCURACY` — **FAIL** (Type A/B, Oakland Business Tax Certificate requirement stated too absolutely — see companion finding below)

## Why this one is instructive

The claim wasn't sourced from nowhere — the underlying rule (rates change on fixed dates) is real. But the draft used "notice served/dated before X" as the operative trigger for which rate applies, when the actual operative fact under Civil Code §1947.12 and Oakland's own published rate-cycle language is the **effective date of the rent increase itself**. A notice served on July 20, 2026 proposing an increase effective September 1, 2026 (past the required notice period) can lawfully use the *new* rate — the draft's framing would have told a reader the opposite.

This is a Type A content error, not a Type B evidence gap — the post's underlying numbers (8.8%, 2.3%, etc.) were correct and cited, but the *mechanism* connecting a notice to a rate was stated backwards from how the law actually works. It's a useful complement to `TEST-LEGAL-001`, which caught a correct-but-uncited claim; this one caught a cited-but-incorrect mechanism. Both matter, and neither would have been caught by only checking one of those two things.

A second, smaller finding came from the same review: the draft described Oakland's Business Tax Certificate requirement as a flat requirement on every notice, when Oakland's own page distinguishes CPI-only increases (BTC *or* a payment-plan copy) from banked increases (BTC required, no payment-plan alternative). Logged and fixed in `knowledge/laws/rent-caps.md` under "Oakland Business Tax Certificate."

## Expected verdict

`GATE-LEGAL-ACCURACY` should **FAIL** as originally drafted (backwards mechanism). After the fix — reframing every instance around the rent increase's effective date rather than the notice's service date, applied to the checklist item and FAQ #1 — the gate should **PASS**. `GATE-LOCAL-ACCURACY` should also **PASS** after the Oakland BTC language was corrected to include the payment-plan alternative for CPI-only increases.

## What this should catch in the future

If a future post (or a future edit to an existing post) states a rate-change rule using "notice served/dated before X" as the trigger, re-run this case — that phrasing is the specific pattern that caused the original failure here, and it's easy to reintroduce by copying language from an earlier draft without noticing the distinction matters.
