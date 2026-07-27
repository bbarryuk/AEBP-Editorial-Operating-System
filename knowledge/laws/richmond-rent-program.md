---
title: Richmond Rent Program — Coverage, Fees, Just Cause, Relocation
doc_type: informative
owner: Brian
last_verified: 2026-07-25
next_review: 2026-09-01
review_frequency: as-changed (see Currency note)
authority: Local Ordinance / City Program
confidence: Mixed — see per-fact confidence below
review_method: Manual, cross-checked against primary sources and independently corroborated (ChatGPT Pre-Publish Audit + Grok) during page 4480 review
source:
  - https://www.ci.richmond.ca.us/3373/Landlords
  - https://www.ci.richmond.ca.us/3376/Rent-Increase
  - https://www.ci.richmond.ca.us/3387/Termination-of-Tenancy
  - https://www.ci.richmond.ca.us/4824/Richmond-Relocation-Ordinance
  - https://www.ci.richmond.ca.us/3657/Enrollment-and-Registration
  - https://www.ci.richmond.ca.us/2101/Rental-Inspection-Program
  - https://www.ci.richmond.ca.us/4832/Billing
  - https://library.municode.com/ca/richmond/codes/code_of_ordinances?nodeId=ARTXIPUSAWE_CH11.100FAREJUCAEVHOPR
  - knowledge/laws/rent-caps.md (AGA rate — this file defers to that one rather than restating)
---

# Richmond Rent Program — Coverage, Fees, Just Cause, Relocation

Existed for one reason: page 4480 ("Property Management in Richmond") contained dozens of Richmond-specific legal/procedural claims with only the AGA rate captured anywhere in `/knowledge` (in `rent-caps.md`). ChatGPT's Pre-Publish Audit of that page flagged this as a `GATE-LOCAL-ACCURACY` gap — the reviewer had to reconstruct the page from live city sources because there was nothing in the repo to check it against. This file closes that gap. Every future Richmond post should cite this file rather than restating these facts from memory or re-deriving them from a fresh web search.

**For the current AGA rate, always defer to `knowledge/laws/rent-caps.md`** — that file is the single source of truth for the number itself and its currency window. This file covers everything else about the Rent Program.

## Legal framework

The **Richmond Fair Rent, Just Cause for Eviction, and Homeowner Protection Ordinance** (Richmond Municipal Code 11.100) was passed by voters in November 2016, effective December 30, 2016. It establishes rent control, just-cause eviction protections, a rent-adjustment petition process, and notice-filing requirements. **Confidence: Level 1 (statute), confirmed.**

### Coverage categories

- **Fully covered** (rent control + just cause): multi-unit properties (more than one dwelling unit on one parcel) built with permits before February 1, 1995.
- **Partially covered** (just cause only, no rent control): government-subsidized/Section 8 units; single-family homes and condominiums (one dwelling unit on one parcel); "new construction" permitted after February 1, 1995.
- **Fully exempt** (neither): landlord/tenant share kitchen or bathroom; a permitted ADU added to an owner-occupied single-family home; non-profit home for the aged.

**Confidence: Level 1, confirmed** against the city's own educational materials.

## Enrollment vs. tenancy registration — these are two different requirements

- **Property Enrollment** (required for every rental unit in the city, regardless of coverage category): filed once per property via the Rent Program's iMS system.
- **Tenancy Registration** (required only for fully-covered/rent-controlled units): filed for each tenancy, and must be re-filed on any complete change in tenancy.

Both are prerequisites for a valid rent increase — a rent increase issued while either is out of date is null and void.

## Fees — FY 2025-2026 figures confirmed directly from the City's own fee summary PDF

Brian supplied "Summary of FY 2025-2026 Fees Applicable to Residential Rental Properties" (City of Richmond, fees approved effective July 1, 2025, document updated July 3, 2025) on 2026-07-25. This single document is the primary source for every dollar figure below — **Confidence: Level 1, confirmed** for all of it, replacing the earlier Level 2 (search + Grok corroboration only) status for the Fire Prevention fee. This PDF has an explicit expiration risk of its own: it's fees "as of July 1, 2025... subject to change without notice," so it should be re-pulled for FY 2026-2027 once that cycle's summary is published (typically around July each year).

**Business License Tax** (RMC 7.04) — previous calendar year gross receipts × **1.081%** (if 1–4 units owned) or **2.880%** (5+ units), plus a flat **$4.00** fee per SB 1186. Due **March 1**. Contact Business Tax Division, (510) 620-5555, Business_License_Revenue@ci.richmond.ca.us, for possible exemptions/credits. (The page previously described this as "Measure U" — that framing isn't contradicted by this PDF, which cites RMC 7.04 directly rather than the ballot measure name; keep "Measure U" only if that's confirmed elsewhere as how RMC 7.04 is publicly branded.)

**Residential Rental Inspection Program (RRIP) fees** (RMC 6.40, Community Development/Building Division, (510) 690-8260):
- Registration/Processing Fee: **$106 per owner, annual**
- Initial Inspection Fee: **$211 per unit, every 3 years**
- Re-inspection Fee: **$90 per unit**
- Exemptions (per this fee summary specifically, narrower framing than the full RMC 6.40.050 program-exemption list above): units occupied by Housing Choice Voucher (Section 8) tenants, **provided these units receive housing quality inspections by the administering agency**; and newly constructed residential rental units, **for a period of 5 years from the date of construction**. (These two caveats were in Grok's original review and were trimmed from this file's first version as unconfirmed against the RRIP webpage Brian sent — this fee-summary PDF now confirms them independently, for the fee-exemption context specifically. The RRIP *program* exemption list in RMC 6.40.050 is broader — see above — and applies to program participation, not just this specific fee line.)

**Fire Prevention Services Fee** (Fire Department, (510) 307-8037) — annual, tiered by building size, due **within 30 days of billing**:

| Units | Annual Fee |
|---|---|
| 1–5 | $170 |
| 6–15 | $276 |
| 16–99 | $400 |
| 100–249 | $809 |
| 250–499 | $1,284 |
| 500+ | $3,671 |
| Transient (hotel/motel/shelter) | $463 |

Exempt: **single-family homes and duplexes** (confirmed verbatim). See the Fire Prevention Master Fee Schedule for the source table.

**Residential Rental Housing Fee** (Rent Program, (510) 234-RENT / 7368) — funds Rent Program administration/enforcement, due within 30 days of billing, escalating late fees:
- Fully Covered Rental Units: **$267 per unit**
- Partially Covered & Governmentally Subsidized Rental Units: **$151 per unit** (rate through 06/30/2026)
- Late fees: 10% if 1–30 days late, 25% if 31–60 days late, 50% if more than 60 days late
- Exempt: permitted small second dwelling unit where the owner lives in the primary home; landlord who lives with tenants and shares a kitchen/bathroom; non-profit senior housing (additional exemptions may apply — see RMC 11.100.030(d))

## RRIP — materially amended January 7, 2025 (Ordinance No. 02-25 N.S.)

The Richmond City Council unanimously passed Ordinance No. 02-25 N.S. on January 7, 2025, amending RMC Chapter 6.40. This is a real, dated change — not a stable long-standing rule — and any pre-2025 description of RRIP exemptions should be treated as stale. Confirmed changes:

- Eliminated the self-certification process that previously let some owners avoid direct inspection.
- Expanded coverage to bring certain previously-exempt affordable/subsidized housing units into the program.
- Mandates inspection of every covered unit at least once every 3 years.
- Registration/processing fee charged annually for owners of 3+ units, every 3 years for owners of 1-2 units; separate per-unit inspection fee charged at the start of each 3-year cycle.

**Current exemptions (RMC 6.40.050 — category names confirmed verbatim against the city's own RRIP page, 2026-07-25):** (a) Mobile Home Parks; (b) Vacant Properties; (c) Transient Lodging; (d) Newly Constructed Buildings or Accessory Dwelling Units (ADUs); (e) Units Occupied by Housing Choice Voucher (Section 8) Tenants. The city's page refers to the full RMC 6.40.050 text for complete conditions/details on each category — we have the category list confirmed, not the full text of every condition attached to each one. This exemption list is **narrower** than older program descriptions that broadly exempted "government-subsidized units" — that broader language predates the 2025 amendment and should not be reused.

Scope note (RMC 6.40.040(a)): the program applies to "all existing residential rental dwelling units located within the City limits including parking lots, driveways, landscaping, accessory structures, and fences" — broader than just the dwelling unit itself.

Enforcement: a failed inspection results in an inspection fail notice with a compliance deadline; missing that deadline triggers code enforcement (administrative citations, re-inspection fees, and abatement — costs can become a lien on the property if unpaid). Contact for inspection reports or to report an issue: (510) 690-8260 / RichmondRRIP@ci.richmond.ca.us.

**Confidence: Level 1 — confirmed directly against the City of Richmond's own RRIP program page text**, supplied by Brian 2026-07-25 (quoting "Program updates," "Exemptions summary," and "Violations, Enforcement and Penalties" verbatim). This matches Grok's earlier independent review (which first surfaced the ordinance number and 2025 date) and resolves the confidence gap flagged in this file's first version, where Claude's own attempts to fetch `ci.richmond.ca.us/2101/Rental-Inspection-Program` and `/4832/Billing` both returned empty content (a JS-rendering/tooling gap, not evidence against the facts — same pattern already logged in `rent-caps.md`). The specific program **fee amounts** are still not confirmed here — the city's own page just points to "the Current Fee Schedule... under Building Regulations, Miscellaneous Fees" rather than stating figures inline; don't cite specific RRIP dollar amounts without pulling that fee schedule directly.

## Rent increases (Maximum Allowable Rent)

**Base Rent + AGA = Maximum Allowable Rent (MAR).** Base Rent is the rent in effect July 21, 2015, or the first rent charged to a tenant who moved in after that date. See `rent-caps.md` for the current AGA rate and its confidence level.

- AGA is announced by the Rent Board by June 30 each year, applies on or after September 1.
- **Banked (deferred) increases:** a landlord may apply the current AGA plus up to 5% of previously deferred AGAs in a single year — Regulation 602's banking limit. This combined cap moves with the AGA every year (6.5% for the Sept 2026–Aug 2027 cycle at the current 1.5% AGA; was 6.62% the prior cycle at 1.62%). Never hardcode "6.5%" as a standing constant — always state which cycle it applies to.
- **Notice:** 30 days for increases ≤10%; 90 days for increases >10% (Civil Code §827). Notice + Proof of Service must be filed with the Rent Program within **10 business days** of service on the tenant. Properties with more than 5 units must file via the online portal (Excel upload); 5 or fewer units may mail a hard copy to 440 Civic Center Plaza, Suite 200.

## Just cause for eviction (RMC 11.100.050)

Eight causes, in the city's own order (confirmed against the Termination of Tenancy page text directly, 2026-07-25):

1. Failure to Pay Rent
2. Breach of Lease* (written warning required first)
3. Nuisance* (written warning required first)
4. Failure to Give Access* (written warning required first)
5. Temporarily Vacate due to Substantial Repairs** (temporary relocation payment)
6. Owner/Relative Move-In** (permanent relocation payment)
7. Withdrawal from the Rental Market / Ellis Act** (permanent relocation payment)
8. Temporary Tenancy (single-family/condo only, max 12 months, must be agreed at lease start, Declaration of Temporary Tenancy filed with Rent Program before tenancy begins)

*Written warning notice required first. **Relocation payment required — see below.

**Filing:** a copy of any termination notice + Proof of Service must be filed with the Rent Program within **2 business days** of service on the tenant (RMC 11.100.050(g)). Failure to file is an affirmative defense to an unlawful detainer action.

## Relocation Ordinance (RMC 11.102, established December 20, 2016)

Two categories: **Permanent** (Owner Move-In, Ellis Act, and Government Agency Order to Permanently Vacate — this last category is real, confirmed directly against the Relocation Ordinance page text, RMC 11.102.030(c)) and **Temporary** (Substantial Repairs).

**2025 Permanent Relocation Payment Amounts** (RMC 11.102.050) — Base Amount / Qualified Tenant Household Amount, per unit, pro-rated across multiple tenants:

| Unit Type | Owner Move-In — Base | Owner Move-In — Qualified | Ellis Act / Gov't Order — Base | Ellis Act / Gov't Order — Qualified |
|---|---|---|---|---|
| Studio | $4,355.81 | $4,923.76 | $8,775.23 | $10,056.28 |
| 1 Bedroom | $6,725.81 | $7,749.89 | $13,451.61 | $15,501.04 |
| 2+ Bedroom | $9,159.42 | $10,504.08 | $18,255.22 | $21,009.41 |

"Qualified Tenant Household" = senior citizen, disabled, household with a child under 18, lower-income household (Health & Safety Code §50079.5), or — Owner Move-In only — a tenant with a terminal disease (Health & Safety Code §443.1(q)).

**2025 Temporary Relocation Per Diem** (substantial repairs): Hotel/motel $185.86/day/household; meals $37.42/day/person; laundry $1.25/day/household; pets — cat $36.17, dog $64.86/day/animal. Paid weekly, calculated daily at minimum, or landlord may provide comparable Richmond housing instead.

**2026 amounts not yet published.** These normally adjust every January 1 based on Bay Area CPI. The October–November 2025 federal government shutdown delayed the Bureau of Labor Statistics' October 2025 CPI release, which the city needs to calculate the update — so the 2025 figures above remain in effect until the city publishes new ones. **This is a genuinely dated, checkable fact (not an evergreen one) — re-verify before citing after any indication the city has published 2026 figures.**

**Confidence: Level 1 (city-published figures), confirmed** directly against the Relocation Ordinance page text, 2026-07-25.

## Petitions

Landlords may petition for: Fair Return Standard (Attachment A), increased occupants (B), change in space/services (C), restoration of denied AGAs (D), security deposit increase for pets (E) — capped at a 15% increase in one year if granted, larger increases spread over multiple years. Tenants may petition for: excess rent/overcharges (A), property condition/reduction in services (B), reduction in tenants allowed (C), or failure to pay relocation/rent withholding for failure to register (Other).

## Known tooling gap

Several official Richmond pages (`ci.richmond.ca.us/3376/Rent-Increase`, `/2101/Rental-Inspection-Program`, `/4832/Billing`, and PDF fee schedules under `/DocumentCenter/View/`) return empty or stale content on a static fetch from this tooling — they're almost certainly JavaScript-rendered or serving a cached shell to non-browser requests. This is the same gap already logged in `rent-caps.md`. **Resolved for RRIP specifically:** Brian supplied the actual RRIP page text directly 2026-07-25, which is now the Level 1 source for that section above — the tooling gap only blocked Claude's own fetch attempt, not the underlying facts. **Resolved for Fire Prevention/RRIP fee amounts too:** Brian supplied the FY 2025-2026 rental property fee summary PDF directly 2026-07-25, same session — all dollar figures in the Fees section above (Business License, RRIP, Fire Prevention, Residential Rental Housing Fee) are now Level 1, confirmed. The pattern holds across every fact in this file so far: this tooling's static fetch failing is not evidence the underlying fact is wrong — it just means the fact needs to come from a rendered fetch or a directly-supplied document instead. If any fact here needs re-confirming later, use a rendered fetch or contact the relevant Richmond department directly.

## Currency note (EVD-CURRENCY-CHECK)

- AGA rate: tracked in `rent-caps.md`, re-check ~Q2 2027 for the next announcement.
- RRIP: amended January 2025 — no known pending change, but re-check if a post is drafted more than ~12 months after this file's `last_verified` date.
- All FY 2025-2026 dollar figures (Business License %, RRIP fees, Fire Prevention tiers, Residential Rental Housing Fee): sourced from a document that is explicitly fees "as of July 1, 2025... subject to change without notice." Re-verify against the FY 2026-2027 summary once the city publishes it (that cycle typically follows the same July 1 pattern) — don't assume these dollar amounts hold past June 30, 2026.
- Relocation amounts: **re-check before every use** until the city publishes 2026 figures (delayed by the BLS CPI shutdown gap above) — this is the one fact in this file on a genuinely unpredictable timeline right now.
