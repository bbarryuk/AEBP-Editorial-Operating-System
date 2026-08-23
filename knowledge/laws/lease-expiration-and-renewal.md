---
title: Fixed-Term Lease Expiration, Holdover Conversion, and Just-Cause Interaction
doc_type: informative
owner: Brian
last_verified: 2026-08-23
next_review: n/a (no cyclical figure here — re-check only if Civil Code §1945, §1946.1, or §1946.2 are amended)
review_frequency: as-changed
authority: Statute / Local Ordinance
confidence: Mixed — see per-claim confidence below
review_method: Manual, cross-checked against primary statute text and Oakland/Berkeley agency pages
source:
  - https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1945.&lawCode=CIV
  - https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1946.1.&lawCode=CIV
  - https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1946.2&lawCode=CIV
  - https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=827.&lawCode=CIV
  - https://www.oaklandca.gov/Community/Housing-Programs-Support/Evictions-and-Tenant-Rights/Managing-Evictions-For-Landlords/Read-the-Just-Cause-for-Eviction-Ordinance
  - https://rentboard.berkeleyca.gov/laws-regulations/state-law/ab-1482-california-tenant-protection-act-2019
  - https://rentboard.berkeleyca.gov/rights-responsibilities/rent-control-101/renting-berkeley
---

# Fixed-Term Lease Expiration, Holdover Conversion, and Just-Cause Interaction

Existed for one reason: WordPress post 8763 ("California Lease Renewals 2026") originally applied Civil Code §1946.1's 30/60-day periodic-tenancy notice rule to the expiration of an unexpired fixed-term lease — a real `GATE-LEGAL-ACCURACY` failure caught by ChatGPT's Pre-Publish Audit on 2026-08-01. This file exists so that distinction doesn't have to be re-derived from scratch next time a post touches lease renewals, non-renewal, or holdover tenancies. See `tests/legal/TEST-LEGAL-005.md` for the full incident.

## The core distinction: three different situations, three different rules

Content describing "what happens when a lease ends" has to keep these separate. Collapsing them into one notice rule is the specific failure this file exists to prevent.

### 1. A fixed-term lease that has not yet expired

Nothing in Civil Code §1946.1 applies. The lease's own end date is the operative term the parties already agreed to. No additional 30/60-day statutory notice is owed by the landlord simply to let the term run out — that statute governs terminating a *periodic* tenancy, not the natural expiration of a fixed term.

**Confidence: Level 1 (required by law) for the negative claim** — §1946.1's text applies to "a hiring of residential real property for a term not specified by the parties," i.e., a periodic (typically month-to-month) tenancy. A fixed term is, by definition, a term specified by the parties.

### 2. A fixed-term lease that has expired, tenant remains

Two sub-cases:

- **Landlord accepts rent after the end date.** Civil Code §1945 presumes the parties renewed the hiring on the same terms — as a month-to-month tenancy when rent is paid monthly, not a new fixed term. This happens by operation of law, with no new lease document required.
- **Landlord does not accept rent after the end date.** No §1945 conversion occurs. But not accepting rent only prevents the conversion — it does not, by itself, establish that the landlord may lawfully recover possession. That depends on just-cause coverage (see below) and, if the tenant won't leave voluntarily, the unlawful detainer process. Treating "we didn't take the rent" as equivalent to "we can now evict" is the trap `GATE-COMPLIANCE-RISK` exists to catch — this is a possession question, not just a lease-status question.

**Confidence: Level 1 (required by law)** for the §1945 conversion mechanic itself, sourced directly from the statute's text.

### 3. A tenancy that has already converted to periodic/month-to-month (whether under §1945 or because it started that way)

Only *here* does Civil Code §1946.1's 30/60-day no-cause notice rule become relevant — and only if the tenancy isn't independently protected by just cause (see below). 30 days if the tenant has occupied the unit less than a year; 60 days if a year or longer.

**Confidence: Level 1 (required by law).**

## Just cause can make "lease expiration" irrelevant to possession, regardless of tenancy type

This is the piece most likely to get flattened in drafting, and the one that actually caused the TEST-LEGAL-005 failure.

- **Statewide (AB 1482 / Civil Code §1946.2):** once the occupancy threshold is met, just cause is required to terminate the tenancy — lease expiration by itself is not one of the recognized at-fault or no-fault grounds. The threshold is **12 continuous months** for all tenants under the same household. **Correction (2026-08-23, per ChatGPT pre-publish audit of posts 8883/8885 — see `tests/legal/TEST-LEGAL-007.md`):** the added-tenant wrinkle is NOT "the threshold becomes 24 months, measured from the original tenant's move-in." The statute (Civil Code §1946.2(a)(1)) actually sets up an either/or test: if an additional adult tenant is added to the lease *before an existing tenant has occupied the unit for 24 months*, just cause applies once **either** (1) all tenants have continuously and lawfully occupied the unit for 12 months or more, **or** (2) at least one tenant has continuously and lawfully occupied it for 24 months or more — whichever happens first. In practice this usually means coverage attaches at whichever tenant hits the 12-month mark first (counting from when *they* moved in), not at a flat 24 months from the original tenant's move-in date. Do not describe this as the threshold "becoming" or "shifting to" 24 months, and do not state that the rule exists "so a landlord can't reset the clock by adding a roommate" — the statute's text doesn't say that, and the phrase invites exactly the oversimplified reading this correction fixes. Before either condition is met, a no-cause termination with proper notice is still permitted for AB 1482 purposes.
- **Oakland (Just Cause for Eviction Ordinance, OMC 8.22.360):** applies to covered units **from day one** of the tenancy — no 12-month wait, unlike the state law. Lease expiration is not among the ordinance's permitted grounds for covered units.
- **Berkeley (Rent Stabilization Ordinance, BMC Ch. 13.76):** same day-one-coverage pattern as Oakland for covered units. Expiration of a lease term is not, by itself, good cause to end the tenancy.

**Confidence: Level 1 (required by law) for AB 1482's 12-/24-month rule; Level 1 (required by local ordinance) for Oakland and Berkeley's day-one coverage** — all three sourced from the statute/ordinance text and the cities' own published guidance, not secondary summaries.

**Practical implication for renewal content:** the question "can this tenancy end when the fixed term expires" is answered by just-cause coverage first, not by which notice-period table applies. Any content walking through "what to do at lease end" should ask *"is this unit just-cause covered, and if so, from when?"* before reaching for a notice-period rule at all.

## A decision path for drafting (not exhaustive, but catches the recurring failure)

1. Is the lease fixed-term and still within its stated term? → No §1946.1 notice applies. The lease's own terms and any applicable just-cause law govern.
2. Has the fixed term expired? → Check whether rent was accepted afterward. Accepted → §1945 conversion to month-to-month. Not accepted → conversion avoided, but possession isn't automatically resolved.
3. Is the unit just-cause covered (AB 1482 threshold met, or Oakland/Berkeley from day one)? → If yes, expiration alone is not valid grounds for possession regardless of lease type or acceptance of rent — a qualifying cause is still required.
4. Only once the tenancy is confirmed periodic **and** not just-cause protected does §1946.1's 30/60-day no-cause notice rule actually apply.

## What this file does not cover

Rent-increase notice timing (Civil Code §827(b), the 30/90-day rule) is a separate mechanism from tenancy termination and isn't restated here — see the worked effective-date-vs-notice-date logic already documented in `knowledge/laws/rent-caps.md`'s "Notice service date vs. rent increase effective date" section, which remains accurate and unaffected by this file.

## Currency note

No cyclical figure lives in this file. Re-verify only if Civil Code §1945, §1946.1, or §1946.2 are amended, or if Oakland's or Berkeley's just-cause ordinances are updated to change their coverage-start rules.
