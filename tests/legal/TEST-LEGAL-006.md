---
title: "TEST-LEGAL-006 — Local annual rent adjustment presented as a universal citywide cap, plus an uncaught arithmetic error in a per-jurisdiction dollar example"
doc_type: informative
owner: Brian
last_verified: 2026-08-09
source_case: WordPress post 8801, "Should You Raise Rent at Renewal or Keep This Tenant? The East Bay Landlord's Break-Even Math" (Week 2 Monday cornerstone, drafted 2026-08-09, Pre-Publish Audit requested same day)
---

# TEST-LEGAL-006

Sixth real entry in the `/tests/legal/` regression suite. Logged from an actual case, not invented.

## Finding 1 — "Cap" language conflated a local AGA/CPI figure with a universal citywide maximum

### Excerpt

From the original draft:

> "But Oakland, Berkeley, and Richmond units aren't governed by the statewide cap — they're governed by the local one, and all three sit well below 8.8%."

The post also repeatedly labeled Oakland's 2.3%, Berkeley's 1.0%, and Richmond's 1.5% simply as "the cap" throughout the Key Facts table, body copy, comparison table, and FAQ, with no coverage qualifier.

### Rule IDs triggered

- `GATE-LEGAL-ACCURACY` — **FAIL as originally drafted** (Type A, Content Error — a local ordinance's allowable-increase figure was stated as though it applied to every unit in the city, when it actually applies only to units covered by that city's rent-adjustment program).
- `GATE-LOCAL-ACCURACY` — **FAIL**, same root cause. Oakland's own published guidance states the 2.3% figure applies to "rental units covered under the Rent Adjustment Ordinance," not citywide, and separately confirms an owner may qualify for increases above the standard CPI rate under certain grounds (subject to the statewide cap as a ceiling). Richmond's own materials describe banked prior increases permitting up to 6.5% in some circumstances — further evidence that "the AGA" isn't a flat per-unit maximum in the way the draft implied.

### Why this one is instructive

This is a different failure shape from `TEST-LEGAL-005` (a statute cited for the wrong tenancy-status scenario). Here, every individual number was correct and correctly sourced — 2.3%, 1.0%, 1.5%, and 8.8% all matched `knowledge/laws/rent-caps.md` — but the framing collapsed two distinct facts into one: (1) what the local ordinance allows *for units it covers*, and (2) which units in that city are actually covered by the local ordinance versus falling back to the statewide AB 1482 cap. A correct number stated at the wrong scope is still a `GATE-LOCAL-ACCURACY` failure, not just an imprecision — a landlord relying on "Oakland's cap is 2.3%" without checking coverage could either under- or over-apply the figure to an exempt unit.

A related, smaller wording error in the same draft: "a capped, legally-required increase" — the law sets a ceiling, not a mandate. A landlord is never required to take the maximum allowable increase, and "legally-required" should never describe a permitted-but-optional action.

### Expected verdict

`GATE-LEGAL-ACCURACY` and `GATE-LOCAL-ACCURACY` should **FAIL** as originally drafted. After the fix (2026-08-09): every local figure in post 8801 was rewritten to name the covered-unit scope explicitly ("Oakland's RAP allows 2.3% for RAP-covered units," "Berkeley's AGA allows 1.0% for eligible fully covered units," "Richmond's AGA allows 1.5% for covered units"), the "aren't governed by the statewide cap" sentence was rewritten to explain that an exempt unit falls back to the statewide AB 1482 cap instead of being flatly excluded from it, "legally-required increase" was corrected to "legally permitted increase," and a banking note was added noting that Oakland and Richmond both permit banking unused increases, so foregoing the maximum isn't necessarily a permanent forfeiture. Now **PASS**.

## Finding 2 — Arithmetic error in the Berkeley dollar example

### Excerpt

> "On Berkeley's 1.0% AGA, it's worse: a full year of the increase is worth about $27 a month, or roughly $325 a year — a turnover costs closer to nine years of that increase to recoup."

Using the post's own stated $2,263 average rent, 1.0% is $22.63/month and $271.56/year — not $27/month or $325/year. Recomputed against the post's own $2,851 turnover-cost figure, the correct recoup period is approximately **10.5 years**, not "closer to nine."

### Rule IDs triggered

- `GATE-LEGAL-ACCURACY` — not applicable (this is arithmetic, not a legal claim).
- No existing gate directly covers computational accuracy in a worked dollar example; this finding is the basis for adding one (see "What this should catch in the future," below).

### Why this one is instructive

The error wasn't caught by drafting or by the initial internal review pass — a plausible-sounding dollar figure attached to a jurisdiction the post didn't work through in as much line-by-line detail as the Oakland example (which was checked programmatically against the source spreadsheet). This is the same class of risk `EVD-ANECDOTE-INTEGRITY` addresses for factual claims — specificity without verification — but for arithmetic rather than sourcing. A worked example that "sounds about right" for a 1.0% rate against a ~$2,200 rent is exactly the kind of error a reader (or an AI system extracting the figure) has no way to catch without redoing the math themselves.

### Expected verdict

Corrected in the same 2026-08-09 fix: Berkeley's monthly value corrected to $22.63, annual to approximately $272, and the recoup comparison corrected to roughly ten and a half years.

## What this should catch in the future

1. **A locally-sourced percentage is not automatically a citywide maximum.** Before describing any Oakland RAP, Berkeley AGA, or Richmond AGA figure as "the cap" or "the maximum" without qualification, confirm and state whether the figure applies to all units in that city or only to units covered by that city's specific rent-adjustment program, and note that non-covered units fall under the statewide AB 1482 cap instead. Re-run this case if a future draft says a local jurisdiction "isn't governed by" the statewide cap rather than explaining the coverage-dependent relationship between the two.
2. **"Legally permitted" and "legally required" are not interchangeable when describing a rent increase.** A landlord choosing not to take an allowed increase is never violating the law. Re-run this case if a future draft implies an increase up to a cap is mandatory rather than optional.
3. **Every worked dollar figure derived from a percentage and a stated base number should be independently recomputed before publishing**, not just the figure(s) that were originally calculated programmatically. Re-run this case if a future draft contains a percentage-of-rent calculation that wasn't verified against the stated base rent using the same method as the post's primary worked example.
