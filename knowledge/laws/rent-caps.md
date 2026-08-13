---
title: Rent Cap Figures — AB 1482, Oakland RAP, Berkeley AGA, Richmond AGA
doc_type: informative
owner: Brian
last_verified: 2026-08-09
next_review: 2026-11-01
next_review_by_jurisdiction:
  ab_1482_statewide: 2027-08-01
  oakland_rap: 2027-08-01
  berkeley_aga: 2026-11-01
  richmond_aga: 2027-06-01
review_frequency: as-changed (see Currency note; per-jurisdiction dates above — the file-level next_review is the earliest of the four, so nothing in this file goes stale silently)
authority: Statute / Local Ordinance
confidence: Mixed — see per-figure confidence below
review_method: Manual, cross-checked against primary sources; re-verified 2026-08-09 against live Oakland, Berkeley, and Richmond city pages during Pre-Publish Audit of post 8801
source:
  - https://www.bls.gov/regions/west/news-release/consumerpriceindex_sanfrancisco.htm
  - https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1947.12.&lawCode=CIV
  - https://www.oaklandca.gov/Community/Housing-Programs-Support/For-Landlords/Allowable-Rent-Increases/Learn-More-About-Allowable-Rent-Increases
  - https://www.oaklandca.gov/Community/Housing-Programs-Support/Rent-Adjustment-Program-RAP
  - https://rentboard.berkeleyca.gov/elected-rent-board/news/2026-aga-published-and-2025-security-deposit-interest-payment-due-soon
  - https://caanet.org/where-are-the-new-cpi-figures-for-rent-increases-under-ab-1482-5/
  - https://www.ci.richmond.ca.us/3376/Rent-Increase
---

# Rent Cap Figures — AB 1482, Oakland RAP, Berkeley AGA, Richmond AGA

Existed for one reason: post 7938 published specific 2026 rate figures with no citation and no file in `/knowledge` to check them against. This is that file. Every post citing these figures should link back here rather than restating the numbers inline from memory.

**Important for anything published between now and August 1, 2026:** AB 1482 and Oakland RAP are still governed by the *current* period's rates (6.3% and 0.8% respectively) through July 31, 2026. The 8.8% / 2.3% figures below are the *confirmed, upcoming* rates effective August 1, 2026 — correct to cite, but should be framed as "effective August 1, 2026" rather than "the current rate" until that date actually arrives. This distinction is why AEBP's site-wide rate refresh (this round, 2026-07-07) touches nine posts: several correctly stated the outgoing rate as current but hadn't yet flagged the incoming one.

AEBP's service area (Alameda and Contra Costa Counties, per `knowledge/company/overview.md`) falls inside the BLS "San Francisco-Oakland-Hayward" CPI region, which also covers Marin, San Francisco, and San Mateo Counties. Numbers quoted elsewhere for "the Bay Area" or "Marin" that come from this same BLS region apply equally to AEBP's territory — they are not a coincidence or a mismatch.

## AB 1482 (statewide rent cap) — Alameda / Contra Costa

| Period | Regional CPI (Apr–Apr) | Cap (CPI + 5%) | Confidence |
|---|---|---|---|
| Aug 1, 2025 – Jul 31, 2026 | 1.3% | 6.3% | Confirmed (statute + BLS) |
| Aug 1, 2026 – Jul 31, 2027 | 3.8% | **8.8%** | Confirmed (statute + BLS) |

**Confidence: Level 1 (required by law) — confirmed.** The formula is mechanical (Civil Code §1947.12: 5% + regional CPI, 10% hard cap) and the input is a published federal statistic, not subject to agency discretion. Source: [BLS News Release 26-739-SAN, "Consumer Price Index, San Francisco Area — April 2026,"](https://www.bls.gov/regions/west/news-release/consumerpriceindex_sanfrancisco.htm) published May 12, 2026 — reports the San Francisco-Oakland-Hayward CPI-U rose 3.8% for the 12 months ending April 2026. 3.8% + 5% = 8.8%, under the 10% hard cap. This is the figure post 7938 cited; it checks out.

## Oakland RAP (local ordinance overrides AB 1482 for covered units)

| Period | Formula | Rate | Confidence |
|---|---|---|---|
| Aug 1, 2025 – Jul 31, 2026 | 60% of CPI, max 3% | 0.8% | Confirmed (City-published) |
| Aug 1, 2026 – Jul 31, 2027 | 60% of CPI, max 3% | **2.3%** | **Confirmed (City-published, 2026-07-07)** |

**Confidence: Level 1 (required by local ordinance, City-published) — confirmed.** Upgraded 2026-07-07. The [City of Oakland's own "Learn More About Allowable Rent Increases" page](https://www.oaklandca.gov/Community/Housing-Programs-Support/For-Landlords/Allowable-Rent-Increases/Learn-More-About-Allowable-Rent-Increases) states directly: *"CPI Announcement Update: In June 2022, the City Council has adopted an amendment to change the formula used to calculate the annual allowable rent increase to 60% of the change in CPI, or 3%, whichever is lower. Effective August 1, 2026, the new annual CPI rent increase is 2.3%."* The page's own historical rate table also lists "August 1, 2026: 2.3%" and separately confirms "The 2026 state cap, effective August 1, 2026, is 8.8%" — independently corroborating the AB 1482 figure above from the same source. This closes the gap flagged in `tests/legal/TEST-LEGAL-001.md` and in post 7938/7958's original citation notes — those posts should be checked and their "pending Oakland's official notice" language updated to reflect this confirmation.

## Berkeley AGA (Rent Stabilization Board — calendar-year cycle, not Aug–Jul)

| Period | Formula | Rate | Confidence |
|---|---|---|---|
| Jan 1, 2026 – Dec 31, 2026 | 65% of CPI (SF-Oakland-San Jose, Jul 2024–Jun 2025), max not specified in this source | **1.0%** | Confirmed (City-published) |

**Confidence: Level 1 (required by local ordinance, City-published).** Source: [Berkeley Rent Board, "2026 AGA Published,"](https://rentboard.berkeleyca.gov/elected-rent-board/news/2026-aga-published-and-2025-security-deposit-interest-payment-due-soon) published November 3, 2025. Note the different mechanics from Oakland/AB 1482: Berkeley's AGA runs on a **calendar year** (effective Jan 1, applies to tenancies starting before Jan 1 of the prior year), uses a **different CPI region** (San Francisco-Oakland-San Jose, not San Francisco-Oakland-Hayward) and a **different lookback window** (July–June, not April–April), and is **not eligible** for units with certain registration or habitability violations. Don't reuse the Oakland/AB 1482 Aug 1 "re-verify" date for Berkeley — this rate is stable through Dec 31, 2026 and the next check is whenever a "2027 AGA" announcement would be expected (roughly Q4 2026).

### Berkeley's new-tenancy AGA delay — no increase in the year the tenancy starts, or the year after

Not previously spelled out in this file with the actual rule text — only implied above by the vague "applies to tenancies starting before Jan 1 of the prior year" phrasing, which undersells how unusual this rule actually is. Flagged by Brian 2026-08-13, verified against the Berkeley Rent Board's own AGA page the same day (`rentboard.berkeleyca.gov/rights-responsibilities/rent-levels/annual-general-adjustment`), direct quote:

> "Landlords cannot raise the rent for the rest of the year in which the tenancy started, and for one additional calendar year. For example, if a tenancy starts on March 1, 2026, the landlord cannot raise the rent for the rest of 2026, or in 2027. The landlord may take the first AGA rent increase in 2028 with proper notice to the tenant."

**Confidence: Level 1 (required by local ordinance, City-published) — confirmed 2026-08-13.** This is a restriction on *when a unit first becomes AGA-eligible at all*, separate from and in addition to the 1.0% rate itself — a brand-new Berkeley tenancy is AGA-increase-ineligible for close to two full calendar years regardless of the rate. Worth flagging as genuinely unusual: neither AB 1482 nor Oakland's RAP nor Richmond's Rent Program has an equivalent new-tenancy delay in the source material verified in this file — Berkeley is the outlier among AEBP's four covered jurisdictions on this specific rule, not just on rate. The rule is keyed to the tenancy's start date (when the tenant took occupancy), not the lease type or any conversion date — relevant for a tenancy that starts as a fixed term and later converts to month-to-month under Civil Code §1945, since the clock still runs from the original move-in date, not the conversion date.

## Richmond AGA (Rent Program — Sept–Aug cycle)

| Period | Formula | Rate | Confidence |
|---|---|---|---|
| Sept 1, 2026 – Aug 31, 2027 | 60% of CPI, max 3% (post-Measure P) | **1.5%** | Confirmed, 2026-07-07 |

**Confidence: Level 2 (required by local ordinance) — confirmed by owner + corroborating secondary source.** Richmond Rent Board Regulation 615 sets the 2026 AGA at 1.5%, for tenancies commencing before September 1, 2025, effective September 1, 2026 – August 31, 2027. Banked (deferred) increases allow up to 6.5% in a single year, per Regulation 602's banking limit. This is a downward adjustment from the prior 1.62% AGA. Confirmed by Brian directly, citing the City of Richmond's own Rent Increase page (`ci.richmond.ca.us/3376/Rent-Increase`) as the source, and independently corroborated by a secondary source (RentCheckMe) citing the same regulation number and figures.

**Known tooling gap, not evidence against the rate:** A direct fetch of `ci.richmond.ca.us/3376/Rent-Increase` on both 2026-07-07 attempts (morning and this session) returned only stale 2019 AGA content (Regulation 607, 3.5%) — the page is almost certainly JavaScript-rendered or serving a cached shell to non-browser fetches, since Brian's own browser and a secondary source both reflect the current 2026 regulation. If this figure needs re-confirming later, use a rendered browser fetch (not a static one) against that same URL, or request the Regulation 615 PDF directly from the Rent Program office.

## Oakland RAP banking rule (verified 2026-08-12, added for Thursday Tip Week 2 "banking" post)

Not previously captured in this file. Per the City of Oakland's own official info sheet ("Info Sheet – Allowable Annual Rent Increase," EN, rev. 6.10.25, O.M.C. §8.22.070 et seq.): banking is one of the "justifications" landlords can use to raise rent above the flat annual CPI figure. Direct quote: *"'Banking' refers to deferred annual CPI rent increases that an owner can carry forward, subject to limitations... An increase based on banking cannot be higher than three times the current year's CPI and must include the current CPI."* Two mechanical points worth keeping straight: (1) the multiplier applies to the *current* year's rate, not each historical year's own rate — e.g. three years banked this cycle multiply out to 3 × 2.3% = 6.9%, not the sum of the actual historical rates for those three years; (2) a banked-increase notice must include the current year's own increase, it can't be composed of only prior years'. Oakland's ordinance separately caps any single rent increase at 10% regardless of banking math, and increases over 10% require 90 days' written notice instead of 30 (Civil Code §827(b)). A banked-increase notice also requires a current Business Tax Certificate specifically — see the existing Business Tax Certificate section above, which already flagged this distinction from CPI-only notices.

**Not verified to primary-source confidence, flagged for follow-up:** several secondary sources (not Oakland's own page) describe a change from a 10-year to a 5-year banking-accrual expiration window effective January 1, 2026. Oakland's own 6.10.25 info sheet (pre-dating that effective date) doesn't state an accrual window directly, only referencing "Regulations, Appendix A, p. 10-15" for banking limitations. Don't cite a specific accrual-window figure in published content until confirmed against that Appendix or a post-1/1/26 City source — the 3x-current-CPI cap and current-year-inclusion rule above are confirmed and safe to cite; the accrual window is not, yet.

**Richmond's banking rule is separately confirmed, and it is NOT the same formula as Oakland's** (caught by Brian 2026-08-12 reviewing the Thursday Tip Week 2 graphic spec, which had drafted a line implying both cities cap banking at "three times the current year's cap" — that's Oakland-specific and wrong for Richmond). Per `knowledge/laws/richmond-rent-program.md` (Level 1/2, cross-checked against Richmond Rent Board Regulation 602 text via a 2026-08-12 web search): Richmond caps a banked increase at the **current year's AGA plus up to 5 percentage points** of previously deferred AGAs — an additive/compounding formula, not a multiplier. If the current AGA itself already exceeds 5%, banking isn't available that year at all. The 2026–27 cycle's 6.5% figure (1.5% AGA + 5%) is *coincidentally* close to Oakland's 3×2.3%=6.9%, which is exactly why it's easy to accidentally conflate the two rules in copy — they land in a similar range this cycle by coincidence, not because the underlying formulas match. **Never describe Richmond's banking limit as "three times the current AGA"** — always describe Oakland and Richmond's banking rules separately, never with a single shared sentence that implies one formula. **Correction (2026-08-12): Berkeley DOES have a banking provision, and it's the most permissive of the three cities — the "no banking provision" line above was wrong.** Caught by Brian, then confirmed Level 1 directly against the Berkeley Rent Board's own "Annual General Adjustment" page (`rentboard.berkeleyca.gov/rights-responsibilities/rent-levels/annual-general-adjustment`), verbatim: *"If a landlord chooses not to take an AGA rent increase in a given year, they do not lose it. Landlords can 'bank' unused AGAs and then raise the rent to the rent ceiling at any time if they provide the tenant with proper notice, even if the total rent increase exceeds 5%. The 5% AGA cap limits only the AGA percentage set by the elected Rent Board."* Mechanically this is a third, distinct formula from Oakland's and Richmond's: Berkeley has no multiplier and no flat additive cap on the banked amount itself — a landlord can accumulate unused AGAs indefinitely and apply them in one notice, limited only by the unit's own legal rent ceiling (Berkeley's rent-control concept for the maximum lawful rent on a covered unit), not by any percentage-based banking cap. Standard 30/90-day notice rules still apply based on the size of the resulting increase (Civil Code §827).

**All three cities now confirmed to allow banking, via three different mechanics — never describe them with one shared sentence:**
- **Oakland:** multiplicative, capped at 3× the current year's CPI, must include the current year (see above).
- **Richmond:** additive/compounding, current AGA + up to 5 percentage points of deferred AGAs, unavailable if the current AGA alone exceeds 5% (see above).
- **Berkeley:** uncapped by any banking-specific percentage — limited only by the unit's legal rent ceiling.

## Notice service date vs. rent increase effective date — do not conflate these

A recurring drafting error (caught in ChatGPT's review of the 2026-07-07 rent-cap announcement post, see `tests/legal/TEST-LEGAL-002.md`): the CPI period and rate that governs a rent increase is determined by the **effective date of the increase**, not the date the notice is served. A notice served before a jurisdiction's rate-change date (e.g., before August 1, 2026 for AB 1482/Oakland) can still use the new, higher rate, as long as the increase itself is effective on or after that date and the required notice period (30 days for increases of 10% or less, 90 days for larger increases, per Civil Code §827(b)) is met. Conversely, an increase effective *before* the change date must use the outgoing rate regardless of how early or late the notice was served. Source: Civil Code §1947.12's own effective-date framing, corroborated by Oakland's published rate-cycle language ("takes effect on each August 1 and remains in effect through July 31"). **When drafting any content about rate-change timing, always frame the rule around the increase's effective date — never phrase it as "notice served/dated before X."**

## Oakland Business Tax Certificate — CPI-only vs. banked increases require different documentation

Not previously captured in this file, surfaced by the same 2026-07-07 review. Per the City of Oakland's own "Learn More About Allowable Rent Increases" page: as of April 15, 2025, a rent increase notice based on **CPI only** requires either a current Business Tax Certificate **or** a copy of a payment plan with the City for delinquent business taxes. A rent increase notice that includes any **banked** CPI requires a current Business Tax Certificate specifically — the payment-plan alternative is not available for banked increases. Prior AEBP content (including posts 5634 and 6021) described this requirement as a flat "current Business Tax Certificate required" without this distinction; that's not wrong for banked increases but is incomplete for CPI-only ones. Worth a pass to add the payment-plan alternative wherever this requirement is described going forward — not urgent enough to warrant an emergency fix to already-published posts, but should be corrected the next time any of them are touched.

## Currency note (EVD-CURRENCY-CHECK)

AB 1482 and Oakland RAP are both tied to the annual April-to-April CPI cycle and change every August 1 — re-verify before citing in any post published after **August 1, 2026**, and again after **August 1, 2027**. Berkeley runs on a separate calendar-year cycle (see above) — re-check around **Q4 2026** for the 2027 AGA. Richmond runs on a September-to-August cycle — re-check around **Q2 2027** for the next AGA announcement.

**2026-08-09 re-verification:** this file's frontmatter `next_review` (2026-08-01) had lapsed by the time post 8801 (Week 2 Monday cornerstone) was drafted and reviewed, which technically put that draft under `EVD-BLOCK-PENDING-VERIFICATION` until re-checked. Live-verified during that post's Pre-Publish Audit: Oakland's official RAP page confirms 2.3% effective August 1, 2026; Berkeley Rent Board confirms 1.0% for calendar 2026; Richmond's Rent Increase page now renders correctly (the JavaScript-rendering tooling gap noted below, from 2026-07-07, appears resolved as of this check) and directly confirms 1.5%. All four figures in the tables above are unchanged and confirmed current as of this date. Frontmatter updated to per-jurisdiction `next_review` dates (see above) so a single lapsed date doesn't block unrelated content in the future — e.g. a Berkeley-only post shouldn't be blocked by an Oakland/AB 1482 date that hasn't actually lapsed, and vice versa.
