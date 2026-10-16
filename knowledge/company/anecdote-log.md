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

### 2026-09-25 — Overpriced-listing turnover (posts 9313, 9315)

**Claim as published:** "In one turnover we handled, the owner wanted to list well above what comparable units nearby were renting for. That's an understandable instinct for a well-kept property. The unit went through several price reductions over a period of months. It finally leased at about the level the comparables had suggested from the start. Nothing was unreasonable about wanting top dollar for it." The video script version says: "We've watched this happen. In one turnover we handled, the unit went through several price cuts over a period of months and leased close to where comparable units had been renting all along. The asking price was simply above what renters were paying."

**Confirmed by:** Brian, directly, in the Cowork session of 2026-09-24/25.
- On 2026-09-24 he approved reusing the held pricing case, on the condition that it be "vague or different enough that if that owner reads it, he won't feel humiliated."
- On 2026-09-25 he approved the final wording above, after ChatGPT's review 01 (findings 9313-F04 and 9315-F01).
- The underlying record is `10-October/pricing-case-study-HOLD-for-sept-oct.md` in Brian's OneDrive content folder.

**Reuse limits (all mandatory):**
- Never publish any of the case's distinctive details: the price ladder, the vacancy length in days, the turnover cost, the carpet line item, dates, city, unit type or owner details.
- Don't claim the unit's condition was fine. That isn't documented, and the case note records make-ready work.
- Keep any dollar math in a separate, clearly labeled hypothetical. In 9313 that is $2,500 market vs. a $2,750 list price.
- Keep the tone non-judgmental toward the owner.

**Used in:** Post 9313 ("What Overpricing a Rental Really Costs," "What We See at AEBP" section and embedded Video Script) and companion video page 9315 (Video Script).

**Underlying point the anecdote supports:** pricing above comparables tends to extend vacancy through repeated price cuts, and the unit often ends up leasing near the market price anyway. This is AEBP practitioner experience from a single documented case. Do not present it as a portfolio-wide rate.

### 2026-09-30 — Broken entry/lobby lock triage + "liability features = retention features" view (posts 9849, 9850)

**Claims as published:**
1. *Company policy:* "When a tenant reports a broken entry door lock or a lobby door that won't lock, we treat it as an emergency on our 24/7 maintenance line, not a routine work order, and send a vendor the same day." Video Script: "At AEBP, we treat a broken entry or lobby lock as an emergency, with a vendor sent the same day."
2. *Professional opinion (not an anecdote):* "The security features that do the most to reduce an owner's risk are the same ones that help keep good tenants. Working locks, good lighting and secure mail..." Video Script: "In our view, working locks, good lighting and secure mail can help reduce risk and support tenant retention." (Both reworded 2026-09-30 per GPT review 9849-F02 / 9850-F03, which flagged "liability" / "protect you from liability" as overstating the legal effect.)

**Confirmed by:** Brian, directly, in the Cowork session of 2026-09-30 (October Week 1 cornerstone build). Asked to classify a broken exterior/entry or lobby lock report, he answered "Emergency, same day." Asked about the May-draft liability/vacancy observation, he answered that it is his real view but there is no specific building example behind it, so it is framed as professional opinion from managing 600+ units.

**Reuse limits:**
- Claim 1 is a process statement. Don't add response-time statistics, percentages or specific incidents unless Brian supplies them.
- Claim 2 must stay labeled as professional opinion. Never rewrite it as "we've seen at building X" or attach a vacancy figure to it.

**Used in:** Post 9849 ("Landlord Security Duties in California," "What We See at AEBP" + Video Script) and video page 9850 (Video Script). Reused (claim 1 only) in Oct 8 Thursday Tip, post 9900 ("A Broken Lock Report Isn't Just a Complaint. It's Notice."), its email and video script. No stats or incidents added.

**Underlying point:** under Civil Code §1941.3(b), liability for a broken lock turns on failing to fix it within a reasonable time after notice, so AEBP's same-day emergency classification is the operational answer to the statute.

### 2026-10-09 — Package theft complaint frequency + post office "get a PO box" conversation (posts 10023, 10025, 2804)

**Claims as published:**
1. *AEBP experience:* "Package theft is a common complaint we hear from tenants across the 600+ East Bay units we manage." Video Script: "At AEBP, package theft is a common complaint we hear from tenants." (Softened by Brian on 2026-10-09 from "one of the most common complaints".)
2. *AEBP experience (a conversation, reported):* "When we asked our local post office what building owners can do about it, the answer was blunt: the best advice they had was to get a PO box. They didn't have a better solution to offer for package theft. They also told us mail carriers are being robbed for their master keys." Video Script: "When we asked our local post office what owners can do, the best advice they had was a PO box. Mail carriers here have been robbed for the keys that open apartment mailboxes and building key boxes."
3. *Company fact:* "None of the buildings we currently manage use smart package lockers."

**Confirmed by:** Brian, directly, in the Cowork session of 2026-10-09 (October Week 2 cornerstone build). Asked whether package theft is the #1 complaint, he chose "one of the most common." Asked about lockers, he answered "No lockers." He volunteered the post office conversation: "our post office told us that the best advice is to get a PO box at the post office. They don't have any better solutions to package theft. Mail carriers are being robbed for their master keys." Asked whether a keypad package room has beaten cameras at a real AEBP building, he said leave it out.

**Reuse limits:**
- Claim 1: use "a common complaint"; never upgrade to "one of the most common" or "#1", or attach a percentage or count.
- Claim 2: don't name the branch or a postal employee unless Brian supplies it. The carrier-robbery part is corroborated by NBC Bay Area (May 2024 Oakland; Oct 2022 Berkeley), USPS (May 2023) and USPS OIG 25-137-R26 (May 2026). Cite those for any specifics, not the conversation.
- There is NO confirmed AEBP example of a keypad room or other fix reducing package theft. Don't imply one (relevant for the Oct 15 Thursday Tip).

**Used in:** Post 10023 ("How to Stop Package Theft in an Apartment Building": What We See at AEBP, FAQ 4, Video Script); video page 10025 (Video Script, What This Video Covers); refreshed post 2804 (What We See at AEBP). Claim 1 softened to "a common complaint" in all three on 2026-10-09. Reused (claims 1 and 2 only) in the Oct 15 Thursday Tip, post 10094, its email and video script; no stats, incidents or keypad-room outcome added.

### 2026-10-16 — No routine after-dark walk-throughs; tenants report lighting and door problems

**Source:** Brian, in session (Week 3 Monday cornerstone build), answering "Does AEBP do after-dark walk-throughs?": **No night walks.** Chose to use the tenant-reporting practice instead.

**Confirmed claims:**
1. AEBP does not run routine after-dark walk-throughs or night inspections of managed buildings.
2. AEBP asks tenants to report exterior lights that are out, flickering or on a wrong timer, and doors/gates that don't latch ("we can only fix what we know about"). Wording comes from the October 2026 tenant newsletter "Longer Nights" section; Brian confirmed 2026-10-16 the newsletter went to all residents.
3. Reused, not new: broken entry/lobby locks are emergencies with a same-day vendor (company policy, 2026-09-30 entry).

**Published wording (Brian, 2026-10-16):** use "Our tenants see the property after dark every night; we mostly see it in daylight." Don't state "we don't do night walk-throughs" outright in public copy.

**Do not:** imply AEBP inspects at night, or that any specific lighting fix reduced incidents at an AEBP building. No such example exists.

**Used in:** Post 10112 (What We See at AEBP, Video Script) and video page 10113 (Video Script). Oct 22 Thursday Tip must frame the after-dark walk as owner advice, not AEBP practice.
