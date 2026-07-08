---
title: Rent Cap Figures — AB 1482, Oakland RAP, Berkeley AGA, Richmond AGA
doc_type: informative
owner: Brian
last_verified: 2026-07-07
next_review: 2026-08-01
review_frequency: as-changed (see Currency note)
authority: Statute / Local Ordinance
confidence: Mixed — see per-figure confidence below
review_method: Manual, cross-checked against primary sources
source:
  - https://www.bls.gov/regions/west/news-release/consumerpriceindex_sanfrancisco.htm
  - https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1947.12.&lawCode=CIV
  - https://www.oaklandca.gov/Community/Housing-Programs-Support/For-Landlords/Allowable-Rent-Increases/Learn-More-About-Allowable-Rent-Increases
  - https://rentboard.berkeleyca.gov/elected-rent-board/news/2026-aga-published-and-2025-security-deposit-interest-payment-due-soon
  - https://caanet.org/where-are-the-new-cpi-figures-for-rent-increases-under-ab-1482-5/
---

# Rent Cap Figures — AB 1482, Oakland RAP, Berkeley AGA, Richmond AGA

Existed for one reason: post 7938 published specific 2026 rate figures with no citation and no file in `/knowledge` to check them against. This is that file. Every post citing these figures should link back here rather than restating the numbers inline from memory.

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

## Richmond AGA — still not independently confirmed

Secondary sources (not the City's own page) suggest a 2026 AGA of **1.5%**, for tenancies before Sept 1, 2025, effective **Sept 1, 2026 – Aug 31, 2027**, with banked increases allowing up to 6.5%. A direct fetch of `ci.richmond.ca.us/3376/Rent-Increase` on 2026-07-07 returned only stale 2019 AGA content (3.5%) — the page is likely JavaScript-rendered and the static fetch didn't pick up current-year content, not evidence the 1.5% figure is wrong. **Do not cite a Richmond 2026 figure in published content until confirmed against a primary City of Richmond document** (a PDF notice, Rent Board resolution, or a rendered view of the live page). Try `richmondca.gov/3375/Rent-Board` or a direct-rendered fetch next time this is checked.

## Currency note (EVD-CURRENCY-CHECK)

AB 1482 and Oakland RAP are both tied to the annual April-to-April CPI cycle and change every August 1 — re-verify before citing in any post published after **August 1, 2026**, and again after **August 1, 2027**. Berkeley runs on a separate calendar-year cycle (see above) — re-check around **Q4 2026** for the 2027 AGA. Richmond needs a first real confirmation before it has a currency cycle worth tracking here at all.
