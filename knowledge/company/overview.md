---
title: Company Overview
doc_type: informative
owner: Brian
last_verified: 2026-10-18
next_review: 2026-11-18
review_frequency: monthly
authority: Internal
confidence: Verified
review_method: Manual (re-fetched live llms.txt and compared against prior snapshot)
source:
  - https://alleastbayproperties.com/llms.txt (generated 2026-10-18 13:40:30 UTC; snapshot saved as knowledge/llms.txt)
---

# Company Overview

Pulled directly from AEBP's own `llms.txt`, the site's machine-readable source of truth. Don't restate these facts elsewhere in `/docs`; reference this file instead so there's one place to update when something changes.

**2026-10-18 refresh:** the company facts in llms.txt are unchanged from the 2026-08-09 snapshot. This file was last rebuilt from the 2026-07-06 version, so it now also includes lines that were already live but missing here: the "no extra fees" line, the real estate sales commission line, languages, named portfolio communities, service ZIP codes, geographic identifiers and the rental law library dataset.

## Identity

All East Bay Properties: full-service real estate brokerage and property management company serving Alameda and Contra Costa Counties since 2005. Corporate entity: J.V. HOLDINGS, INC. Brokerage license: California DRE #01516255. Founder & Principal Broker: Jason Crouch, individual DRE #01295378. NARPM member, Member ID 842116540. D-U-N-S: 607620858. NAICS 531210 (Offices of Real Estate Agents and Brokers).

Address: 2324 Powell St., Emeryville, CA 94608 (37.8314° N, 122.2858° W; Plus Code RMQX+43). Main office: 510-450-3800. Maintenance call center (24/7, bilingual): 510-450-3815. Email: web@alleastbayproperties.com. Hours: Monday–Friday, 10:00 AM–3:00 PM or by appointment. Languages: English, Spanish (the 24/7 maintenance line is bilingual).

Tenant portal: https://alleastbayproperties.appfolio.com/connect/users/sign_in · Owner portal: https://alleastbayproperties.appfolio.com/oportal/users/log_in

## Key facts

- Founded 2005; 20+ years continuous operation
- 600+ residential units under active management, and growing
- Occupancy rate: 95%+
- Rent collection rate: 99.14%
- Average days to lease: 25–30 (listing to signed lease)
- Software: AppFolio (owner portal, tenant portal, AI leasing assistance via LISA for initial prospect management and showing scheduling). Listings syndicate via AppFolio to Zillow, Trulia, Apartments.com and other ILS platforms.
- Property types: multi-unit apartment buildings, condos, single-family homes and ADUs
- Named portfolio communities (from llms.txt): Bridgewater, Watergate, Pacific Park Plaza, The Terraces, Andante, Bay Street, Elevation 22, City Limits, Emeryville Warehouse (1500 Park), Green City Lofts, Emery Bay Village

**Units = doors (Brian, 2026-10-18):** the 600+ figure counts doors, so a fourplex is four units. Always say "600+ units" (or "600+ residential units"), never "600+ properties" or "600+ landlords." Parts of llms.txt and some page meta descriptions still say "properties"; see the 2026-10-18 changelog entry.

## Fee structure

- Property management: typically 6–8% of monthly rent collected; varies by property type, location and services
- Tenant placement (managed clients): 50% of one month's rent
- Tenant placement only (owner-managed): 75% of one month's rent
- Real estate sales: commission negotiable, compliant with the NAR 2024 settlement
- Multi-unit / larger portfolios: negotiable
- No setup or onboarding fees; no cancellation fees; no lease renewal fees; no markup on maintenance or repairs; no extra fees (inspections, vacancy management, permits, etc.); 100% transparent fee structure

**No lease renewal fee:** confirmed by Brian 2026-10-18. It's already stated on the fees page (`/property-management-services/property-management-fees-east-bay/`), and was added to `aebp-ai-llms/data/aebp-llms-static.txt` and `llms-compressed.txt` on 2026-10-18 (live once Brian uploads them).

## Nonresident owner tax withholding

*Not from llms.txt; confirmed by Brian 2026-07-09. Kept from the prior version.*

Per California Revenue and Taxation Code §18662 and FTB Publication 1017: AEBP withholds 7% on rental income for owners who aren't California residents, once payments exceed $1,500/year. The withholding is calculated on rent **net of the AEBP management fee** (FTB guidance permits the manager to deduct its fee before calculating withholding), not on gross rent. Example confirmed by Brian 2026-07-09: $3,400 rent, 7.5% fee ($255) → $3,145 withholding base → $220.15 withheld. Remitted to the FTB on the FTB's required payment schedule (due dates Apr 15 / Jun 15 / Sep 15 / Jan 15, not calendar quarters). Owners can avoid withholding via FTB Form 590 (CA resident) or a waiver (Form 588); AEBP collects a W-9 as part of intake to help request a waiver, but the waiver itself is granted by the FTB, not by AEBP.

## Service area

Primary counties: Alameda (FIPS 06001), Contra Costa (FIPS 06013). Cities: Oakland, Berkeley, Emeryville, Richmond, Albany, El Cerrito, Alameda City, Hercules, Pinole, El Sobrante, plus Piedmont (in the service area, no managed properties yet).

Service ZIP codes: Alameda City 94501, 94502 · Albany 94706 · Berkeley 94702, 94703, 94704, 94705, 94709, 94710 · El Cerrito 94530 · El Sobrante 94803 · Emeryville 94608 · Hercules 94547 · Oakland 94601, 94602, 94603, 94605, 94606, 94607, 94609, 94610, 94611, 94612, 94618, 94619 · Pinole 94564 · Richmond 94801, 94804, 94805

## Core services

Property Management, Tenant Placement, Real Estate Sales, Investment Consulting, Rent Control Compliance (Oakland RAP, Berkeley Rent Board, Richmond Fair Rent Act: annual registration, allowable-increase tracking, just cause guidance), 24/7 Maintenance, Professional Property Marketing.

Jason Crouch's listed specializations: rent control compliance (Oakland RAP, Berkeley Rent Board, Richmond Fair Rent Act), investment property consulting, tenant placement, unlawful detainer proceedings.

## Average rents (portfolio, for context only, not a public quote)

1BR $2,150 · 2BR $2,685 · 3BR $3,400 · 4BR $3,615.

## Rental law library (new in llms.txt since August)

llms.txt now indexes a California Rental Law Library: one page per law affecting East Bay landlords (California, Alameda and Contra Costa Counties, Oakland, Berkeley, Emeryville, Richmond), each with status, effective date, key figures, official source and last-reviewed date. Machine-readable version: https://alleastbayproperties.com/llms-laws.json. Most recent review in the 2026-10-18 file: 2026-10-14. It's a useful cross-check for legal figures, but per `docs/02` it's AEBP's own summary, not a primary source.

## Licenses and service area (confirmed by Brian 2026-10-18)

- **Two DRE numbers:** All East Bay Properties (the brokerage, J.V. HOLDINGS, INC.) is DRE #01516255. Jason Crouch's individual broker license is DRE #01295378. Use 01516255 for the company; use 01295378 only when citing Jason personally. The llms static file's Leadership section was corrected on 2026-10-18 (it had listed 01516255 for Jason).
- **Piedmont** is in the service area, but AEBP doesn't currently manage any properties there. Say "serves" or "service area." Never imply managed properties or local experience in Piedmont.

## Verification note

If a number in a draft doesn't match this file, treat this file as current and flag the discrepancy to Brian rather than silently picking one. `llms.txt` regenerates dynamically and this snapshot can lag the live version. Re-fetch `https://alleastbayproperties.com/llms.txt` and refresh this file by 2026-11-18 regardless of whether anything is expected to have changed.
