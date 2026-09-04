---
title: Confirmed AEBP-Specific Anecdotes and Observations Log
doc_type: informative
owner: Brian
last_verified: 2026-09-04
next_review: as-needed (append on each new confirmed anecdote; no cyclical figure to re-check)
review_frequency: as-changed
authority: Internal
confidence: AEBP documented experience (source-hierarchy level 6 — see docs/02-Evidence-and-Sourcing.md, EVD-SOURCE-HIERARCHY)
review_method: Each entry confirmed directly by Brian at the time it was supplied for a specific post; logged here per EVD-ANECDOTE-INTEGRITY so a reviewer (human or ChatGPT) can verify a claim is real without re-asking Brian each time.
source:
  - Brian, directly, in the Cowork session that drafted each referenced post
---

# Confirmed AEBP-Specific Anecdotes and Observations Log

Existed for one reason: `GATE-ANECDOTE-INTEGRITY` requires that any AEBP-specific, first-person "we've seen..." claim in published content be either a real confirmed detail, a sourced general fact, or explicitly marked hypothetical — never invented. When Brian supplies a real anecdote directly in a drafting session, Claude has first-hand confirmation, but a reviewer reading the *published post* later (a human, or ChatGPT auditing via the repo) has no way to know that without a durable record. This file is that record, mirroring the pattern already established in `knowledge/company/portfolio-performance-2026-07.md` for AEBP's quantitative portfolio data.

**Process note:** an anecdote logged here was confirmed by Brian in conversation at draft time — this file itself is not independent secondary verification. If a future review (ChatGPT or otherwise) flags a specific entry as unconfirmed without knowing this context, check this log first before treating it as a `GATE-ANECDOTE-INTEGRITY` failure; the review tooling doesn't have visibility into the live drafting conversation where the confirmation actually happened.

## Entries

### 2026-08-23 — Oakland relocation-assistance refusal (posts 8883, 8885)

**Claim as published:** AEBP fielded a call from an owner who needed to sell an Oakland property with a family member living in it; the owner offered $30,000 in relocation assistance — well above what Oakland's ordinance required — and the tenant refused both the money and the move-out date, resulting in a referral to a local housing/unlawful-detainer attorney.

**Confirmed by:** Brian, directly, in the Cowork session that revised post 8883 after his initial review pass (2026-08-23). Brian supplied this as a real, recent example when asked to fill the post's AEBP-specific-observation placeholder, framed to be used in generalized/anonymized form (no address, owner name, or tenant identity included in the published version).

**Used in:** Post 8883 ("Ending a Month-to-Month Tenancy in California," blog, "What We See Managing East Bay Rentals" section) and its companion video page, post 8885 (Video Script block). Also referenced in `knowledge/laws/relocation-assistance-just-cause.md`'s practical-implication framing.

**Underlying legal point the anecdote supports:** paying (or offering) relocation assistance satisfies a notice requirement but does not, by itself, guarantee voluntary possession — a tenant can refuse the assistance and stay, pushing the matter toward a full unlawful detainer action. This point is independently sound regardless of the specific anecdote (it follows from relocation assistance being a payment obligation, not a buyout contract), but the anecdote itself is what makes it a first-person AEBP observation rather than generic advice.

### 2026-08-26 — Berkeley new-client Rent Board registration penalty deal (Berkeley PM page refresh)

**Claim as published:** AEBP onboarded a new client who owned multi-unit Berkeley properties that had never been registered with the Rent Board. The city offered to reduce the penalties owed, but the deal had a firm deadline and required an in-person visit to pay the reduced fees before it expired. The Rent Board was not sympathetic to the owner's situation.

**Confirmed by:** Brian, directly, in the Cowork session drafting the September 2026 content plan and the Berkeley PM page refresh (2026-08-26). Supplied when asked for a real Berkeley-specific practitioner observation, to be used in generalized/anonymized form (no owner name, address, or unit count that would identify the property).

**Used in:** Berkeley PM page refresh (post 2346), "mistake we see most often" / practitioner-observation section.

**Underlying point the anecdote supports:** unregistered Berkeley rental units are a real, discoverable compliance gap AEBP catches at onboarding, and the city's own remediation process (a reduced-penalty deal) can carry a hard, unsympathetic deadline — supporting the broader point that Berkeley's Rent Board enforces registration strictly and doesn't extend grace to landlords who are new to the requirement.

### 2026-08-26 — Berkeley security deposit interest paid as rent-ledger credit, not by check (Berkeley PM page refresh)

**Claim as published:** AEBP rarely holds tenant security deposits directly (owners typically hold them), but where required, AEBP calculates Berkeley's annual deposit interest using the rate the city sets roughly two months before the January 31 payment deadline (around November), and issues it to tenants as a credit on their rent ledger rather than a physical check — because small-value checks tenants forgot to deposit used to end up requiring escheatment to the state after several years.

**Confirmed by:** Brian, directly, in the Cowork session drafting the September 2026 content plan and the Berkeley PM page refresh (2026-08-26). Supplied when asked for a real Berkeley-specific practitioner observation.

**Used in:** Berkeley PM page refresh (post 2346), security-deposit-interest Key Facts line / supporting detail.

**Underlying point the anecdote supports:** Berkeley's security deposit interest requirement (Rent Board-set rate, annual payment) has a real operational wrinkle beyond just calculating the rate — how the payment is delivered matters, and AEBP's ledger-credit approach reflects lived process experience (avoiding uncashed-check escheatment), not just knowledge of the underlying rule.

**Verified 2026-09-04, directly against `rentboard.berkeleyca.gov` (Security Deposit Interest & Calculator page, and the "2026 AGA Published and 2025 Security Deposit Interest Payment Due Soon" news page):** the interest year runs **November 1 – October 31**. Landlords make the annual payment **each December** (as a cash payment or rent credit/rebate). **January 31 is the legal backstop deadline**, not the primary due date — if payment isn't made by January 31, the tenant may deduct 10% of their security deposit from rent during that calendar year. This corrects an earlier version of this entry (and the post drafted from it) that implied January 31 was the primary payment date rather than the late-payment backstop; Brian flagged the discrepancy after an independent Grok lookup surfaced the December date, which is what prompted this verification. AEBP's own operational practice — calculating and applying the credit each November, ahead of the December norm — is Brian's stated description of AEBP's process and is accurate as such.

### 2026-08-26 — Richmond post-purchase business license reminder letter (Richmond PM page refresh)

**Claim as published:** A client who had just purchased a Richmond rental property received a letter directly from the City of Richmond reminding him that a business license is required to operate a rental property there — evidence the city tracks ownership changes on registered units against the public record (deed/title transfer) and follows up proactively, paying closer attention than new owners typically expect.

**Confirmed by:** Brian, directly, in the Cowork session drafting the September 2026 content plan and the Richmond PM page refresh (2026-08-26). Supplied when asked for a real Richmond-specific practitioner observation, to be used in generalized/anonymized form (no owner name, address, or purchase date that would identify the property).

**Used in:** Richmond PM page refresh (post 4480), "mistake we see most often" / practitioner-observation section.

**Underlying point the anecdote supports:** Richmond's Business License Tax (RMC 7.04, due March 1 annually — see `knowledge/laws/richmond-rent-program.md`) is a real, actively-enforced requirement independent of whether a unit is rent-controlled, and a new owner inherits that obligation from day one of ownership, not from their first rent increase or tenant turnover. Brian's broader characterization — Richmond's rent-control information is comparatively well-organized and easy to navigate, and the city actively monitors ownership changes and follows up — is Brian's own comparative assessment, not independently sourced; treat it as AEBP's practitioner view.

**Correction (2026-08-29):** the entry originally also characterized Richmond's day-to-day enforcement as "less aggressive" than Oakland's or Berkeley's. Brian asked that this comparative-aggressiveness framing be removed wherever it appears — both on the published Richmond PM page (post 4480, corrected the same day) and here — because it risked reading as an implication that Richmond landlords can get away with non-compliance. The anecdote itself (the business-license letter) and the "paying attention" framing stay; published content should say nothing about how Richmond's enforcement intensity compares to other cities.

## Reuse note

Any future post, video script, or social copy reusing this same observation (rather than drafting a new one) should cite this entry rather than restating the anecdote from memory, consistent with the discipline `knowledge/company/portfolio-performance-2026-07.md` established for AEBP's quantitative data.
