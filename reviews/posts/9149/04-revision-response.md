# Revision Response — Post 9149 (Richmond Rent Control 2026), Round 2

**Responds to:** `reviews/posts/9149/03-final-review.json` (timestamp 2026-09-08T07:01:41Z, reviewer chatgpt / GPT-6 Codex, recommendation `hold_pending_fixes`)
**Reviewer (this response):** claude / claude-sonnet-5
**Timestamp:** 2026-09-08T07:35:00Z
**Repo state:** commit `3f947319d5734072553348a513650c79c0d7b928`, dirty
**WordPress:** post 9149, status draft, https://dev.alleastbayproperties.com/?p=9149
**requires_human_review:** true
**recommendation_to_brian:** hold_for_brian_decision

Good news first: the review's own strengths list confirms all 10 findings from round 1 are closed (9149-01, 02, 05, 07, 10 explicitly; 08's ordered-list attribute and share links corroborated as present). This round caught 4 partial/incomplete fixes plus one new finding.

One finding (9149-06, the RRIP fee amounts) involved a factual claim I could not independently verify — noted below rather than silently accepted.

## Dispositions

| Finding | Disposition | What changed |
|---|---|---|
| 9149-03 | accepted_with_modification | Removed the "MAR = Base Rent + AGA" equation framing entirely (it was still misleading even after round 1's fix); replaced with prose and a real link to the city's MAR calculator page. |
| 9149-04 | accepted_with_modification | Deleted "More notice than the minimum is always safe; less is not" — that overstates what §827 establishes. Replaced with the correct point: more notice doesn't cure an otherwise unlawful increase or defective service. Civil Code §827 now links out. |
| 9149-11 (new) | accepted_with_modification | Qualified the "Oakland's rate = automatic overcharge" claim to account for the article's own banking exception (an owner with banked AGAs can lawfully exceed 1.5%). |
| 9149-06 | accepted_with_modification, **flagged for your check** | Updated RRIP fees to the FY2026–27 figures the review cited ($110/$220/$94, replacing $106/$211/$90). **I could not verify this myself** — WebFetch on both ci.richmond.ca.us and richmondca.gov is blocked by robots.txt, and I found no independent secondary source quoting the new numbers. I used the review's cited figures as the best available information since they're specifically newer and dated, but this is a dollar amount worth a direct look if you get a chance. Also removed the specific "annual for 3+ units / every 3 years for 1–2" frequency claim — the review pointed out this still isn't actually resolved against a clear primary source, so the post now just tells readers to confirm the current cycle with the Rent Program instead of asserting either version. |
| 9149-09 | accepted | Removed the "no comparable Oakland inspection program" row from the comparison table. I checked myself (Richmonder, Pulitzer Center, KTVU reporting all describe Oakland's code enforcement as complaint-driven, not a recurring citywide cycle) but didn't find anything I could cite the way this article cites its other sources, so I dropped the row rather than assert it. |
| 9149-08 | **requires_human** (unchanged) | Ordered-list attribute and share-link URLs reconfirmed present. Rendered schema/JSON-LD and editor validity are still not checkable via the API — both my session and the review's hit a 404 on an unauthenticated preview. One thing NOT to worry about: the share links point at `dev.alleastbayproperties.com` — per what I have on file about your deploy process, that's expected and gets stripped automatically on push-to-live, not a bug in the draft. |

Also applied two non-blocking suggestions from the review: hyperlinked the Civil Code §827 and §1947.12 (AB 1482) citations, and scoped FAQ Q3 to fully-covered units (it previously implied Tenancy Registration applies to every unit, when only Property Enrollment does).

## New/updated operating-system follow-ups

1. **`knowledge/laws/richmond-rent-program.md`** — still needs the frequency conflict resolved, and now also needs the RRIP dollar figures refreshed to FY2026–27 if the review's cited numbers check out against the primary PDF (which I couldn't reach).
2. **Share-link follow-up from round 1 — closing it out.** The earlier note recommending a site-wide decision on the empty share blocks is superseded: you already configured real URLs directly in this post, and the review confirms they're there. No site-wide rebuild needed on that basis. (Post 9050 and any other post using the same pattern would still need the fix applied separately if you want it everywhere — these aren't synced reusable blocks.)

## What still needs you directly

1. **The RRIP fee figures (9149-06)** — $110/$220/$94 is now in the post, sourced from the review's citation of the city's FY2026–27 fee schedule PDF, but I couldn't pull that PDF myself to confirm it. Worth a quick look if you have a moment before this goes live.
2. **Open post 9149 in the WordPress block editor** — same ask as last round: confirm the just-cause numbered list renders, and check whether the Article/FAQ schema is emitting valid JSON-LD. Still not verifiable from here.
3. Companion video/GBP post for this cornerstone remain unaudited per the review — outside what I can check from the blog post alone.

Once you're comfortable with the fee figures and the block-editor check, this is ready to go back to ChatGPT for another pass — or, if those two items check out clean, you may be at a publish decision rather than another review round.
