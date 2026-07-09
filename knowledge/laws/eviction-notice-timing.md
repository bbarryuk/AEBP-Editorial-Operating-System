---
title: 3-Day Notice to Pay or Quit — Timing, Day-Count, and Waiver-by-Acceptance Rules
doc_type: informative
owner: Brian
last_verified: 2026-07-08
next_review: 2026-07-08
review_frequency: as-changed (no cyclical figure here — re-check only if CCP 1161/1162 or relevant case law is amended)
authority: Statute / Case Law
confidence: Mixed — see per-claim confidence below
review_method: Manual, cross-checked against primary sources
source:
  - https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1161.
  - https://selfhelp.courts.ca.gov/eviction-tenant/notice-types
  - https://www.dre.ca.gov/publications/ResourceGuidebook/gb08_living.html
  - "Woodman Partners v. Sofa U Love (2001) 94 Cal.App.4th 766" (case law, residential nonwaiver notice requirement)
---

# 3-Day Notice to Pay or Quit — Timing, Day-Count, and Waiver-by-Acceptance Rules

Existed for one reason: the Week 2 WWYD scenario (tenant unpaid rent, day 13, 5-day lease grace period ending day 6, landlord ready to serve a 3-Day Notice) required three legal claims that had no `/knowledge` file to check them against — flagged as a known gap in `skills/wwyd-social.md` ("Still no `knowledge/laws/`... several past scenarios hinge on statutory details"). This file closes that gap for eviction-notice-timing specifically; `knowledge/laws/rent-caps.md` remains the file for rent-cap percentages.

## Grace periods are a lease term, not a state requirement

**Confidence: Level 1 (required by law) for the negative claim — there is no statewide mandated grace period.** California does not require landlords to give any grace period before rent is considered late. If a lease grants one (e.g., "5 days"), that grace period is a contractual term the landlord must honor once given — but its existence, length, and whether it exists at all is entirely a lease-drafting choice, not a Civil Code requirement. When a WWYD scenario references a grace period, frame it explicitly as "per this lease" rather than implying state law requires it.

## No statutory deadline to serve after the grace period ends

**Confidence: Professional opinion / strongly recommended practice interpretation — not a specifically cited statute or case.** Civil Code of Civil Procedure §1161(2) authorizes a 3-Day Notice to Pay or Quit once rent is "due and unpaid" — it does not specify a window after which the landlord's right to serve expires. Practically, this means a notice served on day 13 (7 days after a day-6 grace expiration) is neither "too early" nor "too late" as a matter of the statute's text.

**Caveat worth stating in content, not hedging into vagueness:** waiting does carry a *practical* risk distinct from a legal deadline — a landlord who repeatedly and knowingly accepts late rent without enforcing the lease's stated due date can build a "course of dealing" that a tenant's attorney may later argue functions as an informal, broader grace period than the lease states. This is a real defense theory in CA landlord-tenant litigation, but it turns on a pattern of conduct across multiple months, not on a single 7-day delay — don't overstate it as "waiting past day X waives your rights" in a single-incident scenario like this one. This distinction should be reviewed and tightened with a specific case citation before this file is considered fully sourced (currently Type C — see note below).

## Day-count rules for the 3-day period itself

**Confidence: Level 1 (required by law), sourced from CCP §§1161–1162 and the existing published post below.** Already verified and published on [California Eviction Notice Requirements (2026)](https://dev.alleastbayproperties.com/california-eviction-notice-requirements-2026/) (WordPress post ID 6614):

- The three-day period excludes weekends and court holidays — only business days count.
- Day one is the day *after* service, not the day of service itself.
- If the last day of the period falls on a weekend or court holiday, it extends to the next court day.
- Post-and-mail service adds five additional calendar days before the three-day period even begins — a "3-Day Notice" served this way is effectively an 8-day notice.
- The notice must state the exact amount owed — not an estimate, not a rounded figure.

## Accepting any payment after serving can waive the notice (residential only)

**Confidence: Level 4 (case law), now properly sourced — upgraded from the uncited version reused from post 6614.** For **residential** tenancies, accepting any rent payment — including a partial payment — after serving a 3-Day Notice to Pay or Quit can constitute waiver and void the notice, requiring the landlord to start the process over. *Woodman Partners v. Sofa U Love* (2001) 94 Cal.App.4th 766 establishes that a landlord must give a proper nonwaiver notice **before** accepting any partial payment for the acceptance not to waive the underlying notice — a nonwaiver notice given only *after* accepting the payment does not cure the waiver. Because getting a nonwaiver notice right is a specific legal instrument most self-managing landlords don't have on hand, the safe, practical guidance for residential owners is simpler and stricter than the doctrine itself: **do not accept any payment, including partial, once a 3-Day Notice has been served, without consulting a property manager or attorney first.**

**Important scope limit:** this waiver rule is specific to residential tenancies. Civil Code §1161.1(c) creates a different rule for **commercial** tenancies, where a landlord can accept partial rent and still proceed with eviction. Don't generalize a residential answer to a commercial scenario, or vice versa.

This claim's citation gap (correct but unsourced when first drafted for the Week 2 WWYD social package) is logged as `tests/legal/TEST-LEGAL-003.md` — the first regression case caught in social/video content rather than a blog post.

## Type C flag — what's still not fully closed

The "no statutory deadline to serve" claim above is Type C (System Gap): it's a reasonable reading of CCP §1161(2)'s silence on timing, corroborated by the absence of any deadline in the California Courts Self-Help Guide's notice-types page, but it isn't backed by a specific case or agency statement saying so affirmatively. If this exact question (how long can a landlord wait before serving becomes risky) comes up again in future content, it's worth a deeper pass — ideally finding a case that addresses delay-based waiver directly — before treating it as more than "professional opinion" confidence.

## Currency note

No cyclical figure lives in this file (unlike `knowledge/laws/rent-caps.md`), so there's no fixed re-review date. Re-verify only if CCP §§1161–1162 are amended, or if a case is found that either confirms or narrows the "no statutory serving deadline" claim above.
