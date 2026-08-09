---
title: "TEST-LEGAL-006 — Local annual rent adjustment presented as a universal citywide cap, plus an uncaught arithmetic error in a per-jurisdiction dollar example"
doc_type: informative
owner: Brian
last_verified: 2026-08-09
source_case: WordPress post 8801, "Should You Raise Rent at Renewal or Keep This Tenant? The East Bay Landlord's Break-Even Math" (Week 2 Monday cornerstone, drafted 2026-08-09; Findings 1–2 from first Pre-Publish Audit pass, Finding 3 from second pass same day)
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

## Finding 3 — Exemption from a local program was treated as automatic coverage under AB 1482 (found on second-pass review, 2026-08-09)

### Excerpt

After Finding 1 was fixed, the corrected language still read, in three places:

> "A unit that isn't covered by the local program falls back to the statewide AB 1482 cap instead…"
> "an exempt unit falls under the statewide AB 1482 cap instead"
> "A unit not covered by the local program falls under the statewide AB 1482 cap of 8.8%… instead"

### Rule IDs triggered

- `GATE-LEGAL-ACCURACY` — **FAIL**, second instance in the same post. Civil Code §1947.12 (AB 1482) has its own separate statutory exemptions — certain newer construction, and certain single-family homes/condos when statutory ownership and notice requirements are met, among others. A unit exempt from Oakland RAP or Berkeley's AGA is not automatically AB 1482-covered; the two determinations are independent. Oakland's own published list of RAP-exempt properties notes some carry no Oakland rent-increase limitation at all, which only makes sense if AB 1482 coverage isn't assumed to fill the gap automatically. Berkeley similarly recognizes fully covered, partially covered, and exempt units, and partially covered units aren't subject to Berkeley's rent ceiling.

### Why this one is instructive

This is the same root-cause pattern as Finding 1 — coverage-scope conflation — but one level deeper. Finding 1 caught "local percentage presented as a citywide maximum." This finding is the mirror image: "exemption from the local program presented as automatic entry into the statewide program." Both are the same underlying error (assuming a rent-control figure applies to a unit without checking that unit's actual coverage status against *that specific* law), just applied to opposite ends of the same sentence. A single review pass fixed the first without automatically catching the second — worth remembering that fixing one direction of a coverage-conflation error doesn't guarantee the inverse direction is also fixed.

### Expected verdict

`GATE-LEGAL-ACCURACY` should **FAIL** as drafted after the Finding 1 fix. Corrected 2026-08-09 (second pass): all three instances rewritten so that non-coverage by a local program triggers a *separate, independent* AB 1482 coverage check rather than an assumed fallback — e.g. "the next question is whether AB 1482 applies — some locally exempt units are still covered by the state cap, while others may also qualify for their own AB 1482 exemption." The Key Facts table's AB 1482 source cell was also changed from "applies where no lower local limit covers the unit" to "applies to units covered by the statute; statutory exemptions apply" — removing the implication that AB 1482 coverage is the automatic default whenever a local program doesn't apply. Now **PASS**.

**The bad-sentence pattern to test against, going forward:** "This unit is exempt from [local program], so the maximum rent increase is automatically [AB 1482 rate] under AB 1482." Expected result: **FAIL** — coverage under AB 1482 has to be established on its own terms, not inferred from exemption elsewhere.

## What this should catch in the future

1. **A locally-sourced percentage is not automatically a citywide maximum.** Before describing any Oakland RAP, Berkeley AGA, or Richmond AGA figure as "the cap" or "the maximum" without qualification, confirm and state whether the figure applies to all units in that city or only to units covered by that city's specific rent-adjustment program, and note that non-covered units fall under the statewide AB 1482 cap instead. Re-run this case if a future draft says a local jurisdiction "isn't governed by" the statewide cap rather than explaining the coverage-dependent relationship between the two.
2. **"Legally permitted" and "legally required" are not interchangeable when describing a rent increase.** A landlord choosing not to take an allowed increase is never violating the law. Re-run this case if a future draft implies an increase up to a cap is mandatory rather than optional.
3. **Every worked dollar figure derived from a percentage and a stated base number should be independently recomputed before publishing**, not just the figure(s) that were originally calculated programmatically. Re-run this case if a future draft contains a percentage-of-rent calculation that wasn't verified against the stated base rent using the same method as the post's primary worked example.
4. **Local rent-control exemption does not imply AB 1482 coverage, and the reverse fix isn't automatic just because the forward fix was made.** After correcting "local percentage = citywide cap," specifically re-check every sentence that describes what happens when a unit is *exempt* from the local program — confirm it directs the reader to check AB 1482 coverage independently rather than asserting AB 1482 applies by default. Re-run this case if a future draft says a unit "falls under," "falls back to," or "defaults to" the statewide cap solely because it's exempt from a local ordinance.
