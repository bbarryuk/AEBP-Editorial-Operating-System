---
title: Rent Cap Figures — AB 1482 and Oakland RAP
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
  - https://www.oaklandca.gov/Community/Housing-Programs-Support/Rent-Adjustment-Program-RAP/Rent-Adjustment-Program-Ordinance
  - https://caanet.org/where-are-the-new-cpi-figures-for-rent-increases-under-ab-1482-5/
---

# Rent Cap Figures — AB 1482 and Oakland RAP

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
| Aug 1, 2026 – Jul 31, 2027 | 60% of CPI, max 3% | **~2.3%** | **Calculated, not yet officially published** |

**Confidence: Level 2 (required by local ordinance) — calculated, pending confirmation.** Oakland's Annual General Adjustment formula (60% of the CPI change, capped at 3%) is documented at [O.M.C. 8.22 / the RAP program page](https://www.oaklandca.gov/Community/Housing-Programs-Support/Rent-Adjustment-Program-RAP/Rent-Adjustment-Program-Ordinance). Applying that formula to the same 3.8% BLS figure above yields 60% × 3.8% = 2.28% → 2.3%, well under the 3% cap. This matches the current period's math exactly (60% × 1.3% = 0.78% → rounds to the City's published 0.8%), which is why we're treating the calculation as reliable enough to publish with a "pending confirmation" label — but as of 2026-07-07, no independent search turned up an official City of Oakland notice setting the Aug 1, 2026 rate. **Do not upgrade this to "Confirmed" until an actual City of Oakland RAP notice, resolution, or updated info sheet is found.** Check `oaklandca.gov/topics/rent-adjustment-program` directly closer to Aug 1.

## Currency note (EVD-CURRENCY-CHECK)

Both figures are tied to the annual April-to-April CPI cycle and change every August 1. Re-verify before citing in any post published after **August 1, 2026**, and again after **August 1, 2027**. If Oakland's official notice is found before then, update the confidence level in this file to "Confirmed" and add the citation — don't just fix it in whichever post prompted the check.

## Other East Bay jurisdictions (not yet verified — do not cite without checking)

Berkeley (~1.0% AGA 2026) and Richmond (~1.62% AGA 2025, 2026 unconfirmed) appear in AEBP's own published guides but have not been independently re-verified for this file. Treat as unconfirmed until checked against Berkeley Rent Stabilization Board / Richmond Rent Program primary sources.
