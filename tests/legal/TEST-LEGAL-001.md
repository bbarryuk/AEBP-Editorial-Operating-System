---
title: "TEST-LEGAL-001 — Uncited rate figures pass the writer's own confidence check but still need a source"
doc_type: informative
owner: Brian
last_verified: 2026-07-07
source_case: WordPress post 7938, "What Does a Property Manager Actually Do? An East Bay Landlord's Guide" (published 2026-07-06, reviewed 2026-07-07)
---

# TEST-LEGAL-001

First real entry in the `/tests` regression suite (see `README.md` → "Planned, not yet built" → `/tests`). Logged from an actual review, not invented, per the rule that this folder should grow from real cases.

## Excerpt

From the Key Facts table and video transcript of post 7938:

> "AB 1482 rises to 8.8% and Oakland's RAP rate rises to 2.3%, both effective August 1, 2026 — compliance tracking has to catch this before the next rent notice goes out."

And, separately, in "The License Question Landlords Skip":

> "California requires anyone who manages property for someone else, for compensation, to hold a real estate broker license — or to work under a broker who does."

## Rule IDs triggered

- `GATE-LOCAL-ACCURACY` — **FAIL** (rent-cap claim)
- `GATE-LEGAL-ACCURACY` — **FAIL, minor** (licensing claim)
- `EVD-CITATION-REQUIREMENT` — both claims: no ordinance number, statute section, CPI figure, or link given anywhere in the post.
- `EVD-SOURCE-HIERARCHY` — the licensing claim is genuinely settled law (should cite Business & Professions Code §10131, source-hierarchy level "statute") but was written with no citation at all — not wrong, just unsupported as written.

## Why this one is instructive

Both numbers turned out to be **correct** on independent verification — 8.8% checks out exactly against BLS's April 2026 CPI release for San Francisco-Oakland-Hayward (3.8% + 5%), and 2.3% is what Oakland's own published formula (60% of CPI, max 3%) produces from that same input. This is the useful case, not the trivial one: a confident, correctly-calculated claim still fails the gate if it isn't cited *in the post itself*. `EVD-CITATION-REQUIREMENT` doesn't ask "is this true," it asks "can a reader or an AI crawler verify this without trusting us." A writer's internal confidence — even correct confidence — isn't a substitute for a source line.

The secondary lesson: not all uncited claims deserve equal treatment once you go looking for the source. AB 1482's 8.8% is Confidence Level 1 (mechanical statutory formula + published federal data — nothing left to confirm). Oakland's 2.3% is Confidence Level 2 (correctly *derived* from the City's own published formula, but no City notice had been issued yet as of verification) — it should be published as "on track, pending confirmation," not asserted as flatly settled. A gate fix that flattens both into "now cited, resolved" would be sloppy in the opposite direction.

## Expected verdict

Both gates should **FAIL** as originally published (no citations present). After the fix (see `knowledge/laws/rent-caps.md` and the citations added to post 7938 on 2026-07-07), both gates should **PASS** — with the Oakland figure specifically labeled as calculated/pending rather than confirmed, which itself should not trigger a fail once the distinction is stated honestly per `EVD-UNCERTAINTY-HANDLING`.

## What this should catch in the future

If a future revision of `docs/02-Evidence-and-Sourcing.md` loosens `EVD-CITATION-REQUIREMENT` to only apply when a reviewer "isn't sure" a number is right, re-run this case: both figures here were *right*, and the gate should still have failed the original draft. That's the regression this test guards against.
