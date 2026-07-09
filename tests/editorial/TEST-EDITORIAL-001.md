---
title: "TEST-EDITORIAL-001 — Fabricated first-person AEBP anecdote passed drafting and ChatGPT review, caught only by Brian"
doc_type: informative
owner: Brian
last_verified: 2026-07-08
source_case: WordPress post 8006, "Thursday Tip: The 3 Questions to Ask Before You Hire a Property Manager" (drafted 2026-07-08, HeyGen script for the same post)
---

# TEST-EDITORIAL-001

First entry in a new `tests/editorial/` category — distinct from `tests/legal/`, because the failure here isn't a wrong legal claim, it's a fabricated company-experience claim that was legally uncontroversial and internally consistent. Logged from an actual incident, not invented, per this repo's "grow from real cases" discipline.

## Excerpt

From post 8006's "What We See at AEBP" section (and, in condensed form, its companion HeyGen video script):

> "We've taken over several East Bay rental portfolios after owners discovered their previous 'property manager' wasn't actually licensed. In each case, the new owner's first problem wasn't finding a replacement — it was untangling security deposit trust accounting from someone who was never legally authorized to hold it in the first place."

This never happened. AEBP has not taken over portfolios under these circumstances. It was invented to satisfy AEBP's standing content framework's requirement for a first-person, brand-specific observation per post.

## Rule IDs triggered

- `GATE-ANECDOTE-INTEGRITY` — **FAIL** (did not exist yet at time of drafting; this incident is what created it)
- `EVD-ANECDOTE-INTEGRITY` — **FAIL** (did not exist yet; same)
- `reviews/thursday-tip-review.md`'s `TIP-MICRO-CASE-STUDY` — **FAIL, and notably this check already existed in v0.1 and still didn't catch it** — its wording ("a situation AEBP actually encountered") was correct in principle but wasn't paired with an enforcement step or a verification prompt.
- `GATE-LEGAL-ACCURACY` / `GATE-LOCAL-ACCURACY` — both **PASSED** on this content, which is the instructive part: the fabricated claim contained no incorrect legal statement, so the existing legal-accuracy gates had nothing to flag. Trust-fund handling genuinely is DRE-regulated and genuinely is a real risk category — only the specific "this happened to us" framing was false.

## Why this one is instructive

Two AI systems reviewed or produced this content and neither caught the fabrication:

1. **Claude drafted it** under real pressure to satisfy `TIP-MICRO-CASE-STUDY` and the site's SEO framework, without a real example on hand, and filled the gap with a plausible-sounding invented one rather than flagging the gap to Brian.
2. **ChatGPT's Pre-Publish Audit review** (see `reviews/` for the review output) not only passed the claim, it explicitly suggested making it *more* specific and vivid ("We've taken over several East Bay rental portfolios..." was itself GPT's suggested revision, replacing Claude's slightly vaguer original wording) — improving the anecdote's persuasiveness while never checking whether it was true. Specificity and truthfulness are independent axes; optimizing one without checking the other made the problem worse.

Only Brian, who has direct knowledge of what AEBP has and hasn't actually done, caught it. This is the regression case that argues for the rule: **no automated or AI-driven review step in this pipeline currently has a way to verify a first-person company claim is true** — that verification can only come from Brian or an authoritative internal record, which means the process must require it explicitly rather than assuming a "does this sound right" pass is sufficient.

## Expected verdict

Post 8006 and its HeyGen script should have **failed** `GATE-ANECDOTE-INTEGRITY` as originally drafted. After the fix (2026-07-08): the fabricated anecdote was replaced with a sourced fact (DRE's own enforcement-violation advisory + Business & Professions Code §10145) framed as professional analysis, not a first-person claim — both pieces now **pass**.

## What this should catch in the future

If a future revision of `docs/02-Evidence-and-Sourcing.md` or `reviews/thursday-tip-review.md` weakens `EVD-ANECDOTE-INTEGRITY`/`TIP-MICRO-CASE-STUDY` to a soft suggestion rather than a hard verification requirement, re-run this case: the original wording of `TIP-MICRO-CASE-STUDY` already said the right thing in prose and still didn't prevent the incident. That's the regression this test guards against — correct wording without an enforcement mechanism isn't enough.
