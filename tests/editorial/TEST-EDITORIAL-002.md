---
title: "TEST-EDITORIAL-002 — A break-even comparison implicitly treated tenant turnover as certain rather than probabilistic"
doc_type: informative
owner: Brian
last_verified: 2026-08-09
source_case: WordPress post 8801, "Should You Raise Rent at Renewal or Keep This Tenant? The East Bay Landlord's Break-Even Math" (Week 2 Monday cornerstone, drafted 2026-08-09, Pre-Publish Audit requested same day)
---

# TEST-EDITORIAL-002

Second entry in `tests/editorial/` — like `TEST-EDITORIAL-001`, this isn't a wrong-fact failure; the underlying numbers were all correct and correctly sourced. The failure is in the shape of the analysis the numbers were used to build.

## Finding — "Years to recoup a turnover" answered a different question than the one the headline promised

### Excerpt

The original draft's central comparison:

> "A single turnover wipes out more than four years of that gain before you're ahead."

This answers "how many years of the increase equal one complete turnover" — a cost-equivalence illustration. It does not answer the actual decision question implied by the post's own title, "The East Bay Landlord's Break-Even Math": at what likelihood of losing the tenant does taking the increase stop being worth it? The original framing implicitly treated a turnover as something that either definitely happens or definitely doesn't, rather than as a probability the increase itself shifts.

### Rule IDs triggered

- No existing gate in `docs/01-Editorial-Standards.md` directly covers analytical/methodological completeness the way `GATE-LEGAL-ACCURACY` covers factual correctness. This case is the basis for flagging that gap (see below).
- Indirectly touches `STD-QUALITY-QUESTIONS` (docs/01) in spirit — the "what should the reader actually decide" question wasn't fully answered by the cost-equivalence framing alone.

### Why this one is instructive

Both the draft and the standard cost-equivalence framing ("X years to recoup") are common in landlord content and aren't wrong — they're just incomplete on their own. They answer "how big is the number" without answering "how likely does the bad outcome need to be before this number matters." For a post explicitly framed around break-even math, that's the more useful answer, and it's a stronger AI-citation target: an AI system answering "should I raise my Oakland tenant's rent" can extract an actual decision formula (increase value ÷ turnover cost = required probability shift) rather than just a comparison ratio.

The fix pattern is general: keep the cost-equivalence illustration (it's intuitive and still useful as a way to communicate scale), but pair it with the expected-value version wherever a "break-even" or "worth it" claim is the article's actual thesis.

### Expected verdict

Fixed 2026-08-09: post 8801 now keeps the original "4.6 years to recoup" framing explicitly labeled as a cost-equivalence illustration, and adds a new section presenting the expected-value break-even calculation — one year of the increase's dollar value, divided by the turnover cost, expressed as the turnover-probability increase required to break even (~22 percentage points for the Oakland example) — with worked illustrative examples at both ends (a small probability shift vs. a large one) to make the threshold concrete without asserting a specific real probability as fact.

## What this should catch in the future

1. **A "break-even" or "worth it" claim built on a single deterministic comparison (X costs more than Y) should be checked for whether the underlying event (a turnover, a vacancy, a default) is actually being treated as certain rather than probabilistic.** Re-run this case if a future draft's central financial argument compares two fixed dollar amounts without addressing the likelihood of the risk event the comparison depends on.
2. **When a post's own title promises "break-even math," verify the math in the body actually identifies a threshold or decision rule — not just a magnitude comparison.** A reader (or AI system) extracting "the break-even point" from the post should get an actual decision rule, not just "this number is bigger than that number."
3. **Consider whether `docs/01-Editorial-Standards.md` needs a gate for analytical completeness** (working name: `GATE-DECISION-FRAMEWORK` or similar) alongside the existing fact-accuracy gates — this case and any future one like it are evidence the standards document currently has no checkable category for "the math is correct but answers an easier question than the one posed."
