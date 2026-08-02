---
title: "TEST-LEGAL-005 — Civil Code §1946.1's periodic-tenancy notice rule applied to unexpired fixed-term lease expiration"
doc_type: informative
owner: Brian
last_verified: 2026-08-01
source_case: WordPress post 8763, "California Lease Renewals 2026: Notice Requirements, Rent Increases & What Landlords Often Get Wrong" (Week 1 Monday cornerstone, drafted 2026-08-01, Pre-Publish Audit requested same day)
---

# TEST-LEGAL-005

Fifth real entry in the `/tests/legal/` regression suite. Logged from an actual case, not invented.

## Finding — §1946.1's 30/60-day rule presented as the mechanism for ending an unexpired fixed-term lease

### Excerpt

From the original draft's excerpt, "In Short" box, Key Facts table, and body:

> "To end the tenancy instead, you must give written notice (30 or 60 days, depending on how long the tenant has lived there) before the lease expires."

The same conflation appeared in the Key Facts table (a row stating the 30/60-day rule with no scope qualifier), the fixed-term-vs-month-to-month comparison table ("30/60-day no-cause notice available" listed as a plain advantage of the month-to-month column), and the FAQ.

### Rule IDs triggered

- `GATE-LEGAL-ACCURACY` — **FAIL as originally drafted** (Type A, Content Error — the statute cited governs a different scenario than the one being described, the same failure shape as `TEST-LEGAL-004` Finding 1, but for a state statute rather than a wrong-scenario citation of a specific provision).
- `GATE-COMPLIANCE-RISK` — contributing factor. The instruction "you need to act before the lease expires... not accepting rent past the end date... or giving written notice of non-renewal" was written as a complete method for recovering possession. It isn't — a just-cause-covered tenancy can't be ended by mere non-renewal regardless of what the landlord does about accepting rent, and the original draft didn't say so.

### Why this one is instructive

Civil Code §1946.1 applies to "a hiring of residential real property for a term not specified by the parties" — a periodic (month-to-month) tenancy. It does not, on its own, create a 30/60-day non-renewal notice requirement for a fixed-term lease that is simply running out its already-agreed term. The rule only becomes relevant once a tenancy is confirmed periodic (either because it started that way, or because Civil Code §1945 converted it after the landlord accepted post-expiration rent) — and even then, only if the tenancy isn't independently protected by just cause.

This is a different failure shape from `TEST-LEGAL-001`–`003` (correct claim, missing citation) and closer to `TEST-LEGAL-004` Finding 1 (statute cited for the wrong scenario) — except here the underlying statute number was right for *a* lease-related notice rule, just applied one level too broad: to lease expiration generally, rather than specifically to ending an already-existing periodic tenancy.

A second, related gap compounded the first: even where the draft correctly discussed non-renewal, it didn't surface that AB 1482 (after the 12-/24-month occupancy threshold) and Oakland/Berkeley's just-cause ordinances (from day one of the tenancy, for covered units) make lease expiration alone insufficient grounds for recovering possession. A landlord who simply stops accepting rent and serves a non-renewal notice can still be blocked from ending a just-cause-covered tenancy — the original draft implied that sequence was sufficient.

A third, minor finding in the same review: the statewide just-cause threshold was stated as a flat "12 continuous months," omitting AB 1482's alternate 24-month trigger that applies when an additional adult tenant was added to the lease before the original tenant reached 12 months. Not a wrong-scenario citation like the main finding, but an incomplete statement of the same statute's own text.

### Expected verdict

`GATE-LEGAL-ACCURACY` should **FAIL** as originally drafted. After the fix (2026-08-01): new knowledge file `knowledge/laws/lease-expiration-and-renewal.md` documents the three-situation distinction (unexpired fixed term / expired-with-holdover / confirmed periodic tenancy) and the just-cause interaction. Post 8763 rewritten throughout — excerpt, In Short box, Key Facts table (added a row distinguishing fixed-term expiration from the periodic-tenancy notice rule, and qualified both 1946.1 rows with "only where no just-cause protection applies"), the "What Actually Happens" body section (now leads with just-cause coverage as the threshold question before any notice-period discussion), the comparison table, the FAQ, and a new "Before Your Lease Converts" checklist that puts the just-cause check first. The 24-month AB 1482 threshold added to the Key Facts table, the just-cause body section, and the relevant FAQ answer. Now **PASS**.

### Two related findings from the same review that did *not* hold up on verification

Logged here so a future pass doesn't waste time re-checking them:

1. **Claimed two H2 headings ("Ending a month-to-month tenancy," "Raising the rent") should have been H3s.** Verified against the actual post content at time of review — both were already H3 blocks nested under the "Two Different Clocks" H2. No structural error existed; the review's claim didn't match the live block markup.
2. **Claimed the post "was published on the dev site" and recommended holding it from production.** The post was in `draft` status throughout, on the dev/staging site, which is the intended safe state per `skills/monday-cornerstone.md` Step 5 ("keep the post as a draft until Brian says to publish"). Nothing was actually published to production at any point in this review cycle.

Neither of these should be treated as evidence the review as a whole was unreliable — the main legal-accuracy finding was correct and well-sourced. But both are a reminder that a review's specific factual claims about the artifact itself (block structure, publish status) need the same quick verification against ground truth as its legal claims, before being acted on.

## What this should catch in the future

1. **A notice-period statute correctly identified for "ending a tenancy" can still be applied to the wrong tenancy-status scenario.** Before citing Civil Code §1946.1 (or any periodic-tenancy statute) in content about lease renewal or non-renewal, confirm the tenancy is actually periodic at the point the rule is invoked — not still within an unexpired fixed term. Re-run this case if a future draft states or implies that ending a fixed-term lease at its own end date requires the same 30/60-day notice as ending a month-to-month tenancy.
2. **"Landlord takes action X to avoid a lease renewing" is not the same claim as "landlord can now recover possession."** Any instruction telling a landlord how to prevent an unwanted lease renewal or conversion should be checked against just-cause coverage before being presented as sufficient to end the tenancy. Re-run this case if a future draft frames non-renewal, or refusing rent after lease end, as a complete method for regaining possession without a just-cause qualifier.
3. **A review's claims about the artifact's own current state (block structure, publish status, specific media/meta IDs) are checkable facts, not opinions — verify them the same way a legal citation gets verified, rather than accepting or rejecting the whole review based on its strongest or weakest single finding.** (See the two non-holding findings above, and contrast with `knowledge/company/overview.md`'s general instruction to trust the file over a stale claim — the same discipline applies to trusting *verified current state* over an unverified review assertion.)
