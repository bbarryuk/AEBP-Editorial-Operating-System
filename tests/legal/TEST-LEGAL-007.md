# TEST-LEGAL-007 — AB 1482 12/24-month interaction rule oversimplified; relocation payment timing wrong

**Date:** 2026-08-23
**Caught by:** ChatGPT pre-publish audit of WordPress posts 8883 and 8885 (Week 4 Monday cornerstone, "Ending a Month-to-Month Tenancy in California")
**Type:** Type A (Content Error) + Type C (System Gap) — the same error was already present in `knowledge/laws/lease-expiration-and-renewal.md`, so the knowledge layer supplied the mistake rather than catching it.

## Finding A — the AB 1482 "24-month rule" was stated incorrectly

Both posts said, in effect: "if an additional adult tenant was added before the 12-month mark, the threshold becomes 24 months, measured from the original tenant's move-in — so a landlord can't reset the clock by adding a roommate."

That is not what Civil Code §1946.2 says. The actual rule (confirmed independently against the statute text via two secondary sources, 2026-08-23): if an additional adult tenant is added before an existing tenant has occupied the unit for 24 months, just-cause protection applies once **either** (1) all tenants have occupied the unit for 12 months or more, **or** (2) at least one tenant has occupied it for 24 months or more — whichever happens first. In practice this usually means coverage attaches sooner than a flat "24 months from the original move-in" framing would suggest (example: Tenant A moves in January, Tenant B added six months later in July — coverage can attach when Tenant B hits 12 months, i.e. when Tenant A is only around 18 months in, not 24).

**Root cause:** `knowledge/laws/lease-expiration-and-renewal.md` already stated the same oversimplified version before either post was drafted — this was a repo problem, not just a drafting error. Fixed in that file the same day (see its own inline correction note, 2026-08-23).

## Finding B — AB 1482 relocation-payment timing was wrong

Both posts said relocation assistance is "paid at the time notice is served." Civil Code §1946.2 actually requires it **within 15 calendar days of service** of the termination notice — a deadline, not a simultaneity requirement. Confirmed directly against the statute text (two independent secondary-source fetches, 2026-08-23). The posts also implied this same "at service" timing applied uniformly to Oakland/Berkeley/Emeryville, when each local ordinance sets its own deadline (Oakland: split 15-day windows; Emeryville: by the last day of the paid tenancy; Berkeley: not yet independently confirmed).

## Finding C — "larger" local relocation amounts stated too categorically

Both posts said Oakland/Berkeley/Emeryville "each require their own, larger" relocation amount than AB 1482's one-month baseline. Emeryville's small-landlord tier (≤4 units) is the greater of one month's HUD FMR or one month's actual rent — which can land at or near AB 1482's own figure, not clearly above it. Corrected to non-categorical language ("their own local relocation rules and amounts... which can be substantially higher... though not always").

## Fix

- Posts 8883 and 8885: all instances of the 24-month shorthand, the "at time of service" timing claim, and the categorical "larger" framing corrected across In Short, Key Facts, body sections, comparison table, Common Mistakes, checklist, FAQ, and Video Script blocks in both posts.
- `knowledge/laws/lease-expiration-and-renewal.md`: corrected inline with a dated note (see file).
- `knowledge/laws/relocation-assistance-just-cause.md`: softened the "much larger" framing, added a payment-timing-by-jurisdiction subsection, and added an Oakland ground-by-ground caveat (owner move-in / Ellis Act / code-compliance displacement are separate programs, not one uniform schedule).
- Post 8883 restructured to give the AEBP-specific relocation-refusal anecdote its own distinct section ("What We See Managing East Bay Rentals"), separate from the regulatory relocation-figures section, per the Monday Cornerstone manifest's AEBP-specific-section requirement.
- Post 8883's Oakland dollar figures ($8,106.68 / $9,977.45 / $12,315.92 / $2,500) were removed from the published post entirely — `knowledge/laws/relocation-assistance-just-cause.md` already flagged these as `EVD-BLOCK-PENDING-VERIFICATION` (cycle lapsed, no confirmed Aug2026–Jul2027 figure found), and the post had cited them anyway. This was a self-inconsistency: the knowledge file's own block wasn't honored when the post was drafted. Replaced with a "confirm the current amount with Oakland's Rent Adjustment Program" instruction instead.

## Future prevention

Before citing a knowledge-file-sourced dollar figure in a post, check that file's own Currency flag / `EVD-BLOCK-PENDING-VERIFICATION` language, not just the figure itself — a knowledge file can correctly document a block and still have that block ignored at drafting time if the figure is skimmed rather than read in full.
