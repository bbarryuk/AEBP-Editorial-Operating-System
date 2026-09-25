# Editorial Review — Post 9313

**What Overpricing a Rental Really Costs: The Vacancy Math East Bay Landlords Miss**

Recommendation: **HOLD PENDING FIXES**

Review mode: Pre-Publish Audit. Reviewed September 24, 2026 (America/Los_Angeles).
Reviewer: ChatGPT (GPT-6).
Standards: docs/01 v0.5; docs/02 v0.2; docs/03 v0.2; docs/07 v0.1; applicable manifest v0.1.
Repository: `da1aaaf951cc97442e53fa631d34aff8298b5f64`; clean before artifact creation, matches GitHub main.
WordPress: [draft 9313](https://dev.alleastbayproperties.com/?p=9313).

## Context and limits

Reviewed 2026-09-24 America/Los_Angeles. Full WordPress snapshot: draft, post_modified 2026-09-24 22:26:25 (timezone not supplied); no revision ID or GMT timestamp returned. Local HEAD matched GitHub main da1aaaf951cc97442e53fa631d34aff8298b5f64; no changes listed before writing artifacts (git warned that global ignore was unreadable). Repo state records pre-artifact state. No prior review paths found locally or in GitHub tree. Scope: full article source, embedded script, companion 9315 independently, and GBP draft in September 28 package notes; no recording or live GBP post reviewed. GBP draft math agrees with the article. Public article preview is a 404; technical FAIL means clearance is blocked, not that schema is proven absent. Existing internal links to vacancy tip, renewal guide, rent-control comparison, fees, move-out checklist and conversion page resolved via web reads; production destination for the new article was inaccessible, expected for a draft and must be checked at release. Article math: 30000/365 = 82.19/day; 7 days = 575.34; 28 days = 2301.37; 70 days = 5753.42; difference = 3452.05; /250 = 13.81 months. Gross-rent opportunity cost, not a net-profit model. Additional editorial corrections: label market-pricing diagnostics as possibilities (good photos do not rule out access, exposure, timing or listing errors); say 'achieved rent' rather than 'asking rent' when describing placement fees; revise Key Facts claim that rent growth peaks in summer because the cited study reports recent national rent-growth peaks moving to March while move-ins remain summer-concentrated. Keep local implications labeled professional judgment. Costa-Hawkins is already hedged 'generally'; a short eligibility/exception reminder is useful, not a demand to reproduce the statute. Scores are editorial estimates, not a calibrated or weighted computation. Sources were checked 2026-09-24 local time. No WordPress edits or publication performed. Claude should provide 02-revision-response.* with one disposition per finding and explicitly preserve the human reuse decision. Artifact files saved locally, not committed or pushed.

## Gated categories

### GATE-LEGAL-ACCURACY — FAIL

**9313-F01 — Type A**

- **Finding:** “annual increases on covered units are capped by the city: 2.3% in Oakland for August 2026 through July 2027, and 1.0% in Berkeley for 2026.”
- **Root Cause:** The current annual adjustments are correctly quoted but described as universal ceilings on actual increases. Berkeley permits banked AGAs up to the lawful rent ceiling; new tenancies also have a separate eligibility delay. The repository already distinguishes these concepts. Verified against https://rentboard.berkeleyca.gov/rights-responsibilities/rent-levels/annual-general-adjustment and https://www.oaklandca.gov/Community/Housing-Programs-Support/For-Landlords/Allowable-Rent-Increases/Learn-More-About-Allowable-Rent-Increases.
- **Fix:** Call these the current standard annual adjustments, subject to eligibility, banking and other applicable rules. Link directly to the Berkeley AGA page rather than its homepage. Keep the existing deep-dive link; a brief qualifier is sufficient, not a full legal detour.
- **Future Prevention:** Check rate, effective period, eligibility and exceptions separately; never equate the published adjustment with every tenant's maximum increase.

### GATE-LOCAL-ACCURACY — FAIL

**9313-F02 — Type A/B/C**

- **Finding:** “National average vacancy between tenants”
- **Root Cause:** Key Facts and Sources label 5.1 weeks as average between-tenant vacancy and date it Q1 2026. The report co-author's first-hand account identifies 2025 median days on market in ShowMojo's platform dataset: https://www.peterlohmann.com/blog/pm-trends-report-2026. This differs in statistic, measurement and period. The older internal content reference repeats the misleading shorthand.
- **Fix:** Replace with 'ShowMojo median days on market, 2025: 5.1 weeks' and link the report/co-author's explanation, or remove this nonessential row. If retaining the 70% comparison, explain that survey-reported vacancy and platform days on market are different measures and populations, not a like-for-like error estimate.
- **Future Prevention:** Add an industry-data reference recording statistic, population, start/end events and measurement period; audit older vacancy-gap copy separately.

**9313-F03 — Type A**

- **Finding:** “About 28 (in line with AEBP's 25–30 day average)”
- **Root Cause:** The example labels 28 days as total days vacant while the quoted AEBP benchmark ends at signed lease, not rent commencement. The portfolio record explicitly separates this from the 37.8-day move-out-to-move-in cycle. Arithmetic is sound, but the benchmark annotation conflates the clocks.
- **Fix:** Keep 28 and 70 as hypothetical rent-free periods, remove the benchmark equivalence, and state the assumed start/end points and identical make-ready/move-in lag. Preserve the 42-day difference and approximately $3,450 result.
- **Future Prevention:** Require the same start/end events whenever comparing time-to-lease, vacancy and turnover.

### GATE-TECHNICAL-SEO — FAIL

**9313-F06 — Type B**

- **Finding:** “Quick Answer”
- **Root Cause:** The source has 73 balanced Gutenberg block markers, five FAQs with the required hooks, SEO metadata and a featured image/alt. However, the draft permalink returned a 404 in the browser; web retrieval also failed. Rendered article/FAQ schema, responsive layout and editor block validity cannot be verified from stored markup alone. This is an access limitation, not evidence that schema is absent.
- **Fix:** Provide an accessible authenticated preview or recorded rendered-page/editor checks and verify the final article/FAQ output, headings, tables, mobile layout and links. Keep technical clearance pending until those checks pass.
- **Future Prevention:** Include an accessible preview in the review handoff and distinguish source checks from rendered validation.

### GATE-COMPLIANCE-RISK — PASS

### GATE-ANECDOTE-INTEGRITY — FAIL

**9313-F04 — Type B**

- **Finding:** “Nothing was wrong with the unit.”
- **Root Cause:** The internal held case note documents a real pricing ladder and eventual lease, but does not establish this categorical condition claim; it records material make-ready work. That does not prove condition caused the marketing delay. The September 28 package notes explicitly reserve approval of this reuse for Brian. Core event is documented; this added detail is unverified.
- **Fix:** Remove the condition assertion from the article and both script copies, or obtain a documented confirmation limited to the marketed condition. Record Brian's decision on reuse before publication, or replace the anecdote with the already documented portfolio observation. Do not reproduce the private case's distinctive numbers.
- **Future Prevention:** Log approved reusable wording and limits in knowledge/company/anecdote-log.md; keep historical truth, added detail and permission to reuse distinct.

### CORNERSTONE-STRUCTURE — FAIL

**9313-F05 — Type A**

- **Finding:** “Bottom Line”
- **Root Cause:** The body goes from the side-by-side comparison to Bottom Line and FAQ without the required 'Before You [Act]' checklist. A link to a move-out checklist is not the on-topic checklist required by CORNERSTONE-STRUCTURE.
- **Fix:** Add 'Before You List' before FAQ with a short checklist: compare current listings and recent leases, verify any rent restrictions, confirm market-ready condition/photos/access, calculate weekly lost rent, and set a 7–14-day review date.
- **Future Prevention:** Run the cornerstone structure check before submitting the draft.

### CORNERSTONE-AEBP-VOICE — PASS

### CORNERSTONE-COMPANION-VIDEO — FAIL

**9313-F07 — Type B**

- **Finding:** “Video in production. This week's Landlord Briefing video will appear here.”
- **Root Cause:** Companion 9315 was independently reviewed and remains held; see its separate review pair. The two scripts match, but share an unsupported repair-cost superlative and the unverified condition detail. The video is not yet produced, and its rendered output is inaccessible.
- **Fix:** Resolve findings 9315-F01 through F03 before clearing the companion. Keep the pre-recording label 'Video Script'; verify the actual recording and final embed separately. Do not infer companion readiness from the article's review.
- **Future Prevention:** Review paired assets independently and propagate accepted changes across both script copies.

### CORNERSTONE-GBP-CONSISTENCY — PASS

## Scored categories

All scores are editorial estimates, not measured rubric outputs.

### SCORE-SEO: 92/100 — PASS (minimum 90)

- **What's working:** Clear intent, focus keyword, descriptive metadata and useful internal links.
- **What's holding it back:** Rendered output not cleared; repetitive comparison section could be tighter.

### SCORE-GEO: 89/100 — FAIL (minimum 95)

- **What's working:** Answer-first block, Key Facts, five extractable FAQs and explicit hypothetical.
- **What's holding it back:** Benchmark labels and annual-adjustment wording can propagate incorrect standalone answers.

### SCORE-EEAT: 88/100 — FAIL (minimum 95)

- **What's working:** Documented portfolio data, identified author and transparent fees.
- **What's holding it back:** Condition detail unverified; ShowMojo measurement and period mislabeled; reuse decision pending.

### SCORE-READABILITY: 93/100 — PASS (minimum 90)

- **What's working:** Plain language, readable tables and clear dollar example.
- **What's holding it back:** Repeated pricing lesson; occasional absolute diagnosis and superlative; missing compact checklist.

### SCORE-CONVERSION: 91/100 — PASS (minimum 85)

- **What's working:** Timely CTA and working conversion destination; fee incentives explained.
- **What's holding it back:** Change asking rent to achieved rent and avoid treating leasing time as a promise.

### SCORE-OVERALL: 89/100 — FAIL (minimum 95)

- **What's working:** Strong practical concept and correct core arithmetic.
- **What's holding it back:** Evidence, legal qualification, structure and final technical clearance remain unresolved.

## Claim provenance

- **9313-C01 — documented:** “AEBP average days to lease (listing live to signed lease)” 25–30-day figure reconfirmed on company source; historical portfolio record defines active-listing measure. Do not treat it as move-out-to-move-in vacancy. Source: knowledge/company/overview.md; knowledge/company/portfolio-performance-2026-07.md; https://alleastbayproperties.com/llms.txt
- **9313-C02 — documented:** “37.8 days across 79 completed turnovers” Aug 2025–Jul 2026 window, methodology and n=79 match; still within November review date. Source: knowledge/company/portfolio-performance-2026-07.md
- **9313-C03 — documented:** “In one turnover we handled, the owner wanted to list well above what comparable units nearby were renting for.” Core pricing/lease event documented, including the script's 'We've watched this happen' version. This does not establish every embellished detail or clear the reserved reuse decision. Source: C:/Users/brian/OneDrive - ALL EAST BAY PROPERTIES/Website-Assets/2026-Content-Strategy/10-October/pricing-case-study-HOLD-for-sept-oct.md; C:/Users/brian/OneDrive - ALL EAST BAY PROPERTIES/Website-Assets/2026-Content-Strategy/10-October/2026-09-28-week-package-notes.md
- **9313-C04 — unverified:** “Nothing was wrong with the unit.” Appears in body and embedded script; see F04. No inference that the story itself was invented.
- **9313-C05 — documented:** “Our management fee is a percentage of rent collected” Live fee source supports collected-rent basis and placement fee as percentage of one month's rent. Clarify 'higher asking rent' to 'higher achieved rent' for precision; an unaccepted asking price produces no fee. Source: https://alleastbayproperties.com/llms.txt
- **9313-C06 — documented:** “We still push for market pricing.” The record supports market-pricing advice in this case; avoid turning one case into a quantified portfolio-wide outcome. Source: C:/Users/brian/OneDrive - ALL EAST BAY PROPERTIES/Website-Assets/2026-Content-Strategy/10-October/pricing-case-study-HOLD-for-sept-oct.md
- **9313-C07 — documented:** “Our listings lease in 25–30 days on average across 600+ managed East Bay units.” Company source supports portfolio size and leasing-time claims, not a promise for any particular property. Source: https://alleastbayproperties.com/llms.txt; knowledge/company/overview.md
- **9313-C08 — hypothetical_example:** “This is a hypothetical example with round numbers, built to show how the math works. It is not a specific client's property.” Preserve separation of $2,500/$2,750 example from the real anonymized event.

## Strengths Worth Preserving

- The $575 weekly and $3,450 six-week figures are correctly rounded.
- The numerical example is expressly hypothetical and uses different numbers from the real case.
- 79 completed turnovers and 37.8 days are documented with period and method.
- AEBP fees are explained transparently; professional-opinion labels separate recommendations from law.
- Five FAQ blocks, useful internal links and a specific CTA are present.
- The pre-recording material is correctly labeled Video Script; GBP draft matches the core numbers.

## Article fixes

- 9313-F01: Call these the current standard annual adjustments, subject to eligibility, banking and other applicable rules. Link directly to the Berkeley AGA page rather than its homepage. Keep the existing deep-dive link; a brief qualifier is sufficient, not a full legal detour.
- 9313-F02: Replace with 'ShowMojo median days on market, 2025: 5.1 weeks' and link the report/co-author's explanation, or remove this nonessential row. If retaining the 70% comparison, explain that survey-reported vacancy and platform days on market are different measures and populations, not a like-for-like error estimate.
- 9313-F03: Keep 28 and 70 as hypothetical rent-free periods, remove the benchmark equivalence, and state the assumed start/end points and identical make-ready/move-in lag. Preserve the 42-day difference and approximately $3,450 result.
- 9313-F04: Remove the condition assertion from the article and both script copies, or obtain a documented confirmation limited to the marketed condition. Record Brian's decision on reuse before publication, or replace the anecdote with the already documented portfolio observation. Do not reproduce the private case's distinctive numbers.
- 9313-F05: Add 'Before You List' before FAQ with a short checklist: compare current listings and recent leases, verify any rent restrictions, confirm market-ready condition/photos/access, calculate weekly lost rent, and set a 7–14-day review date.
- 9313-F06: Provide an accessible authenticated preview or recorded rendered-page/editor checks and verify the final article/FAQ output, headings, tables, mobile layout and links. Keep technical clearance pending until those checks pass.
- 9313-F07: Resolve findings 9315-F01 through F03 before clearing the companion. Keep the pre-recording label 'Video Script'; verify the actual recording and final embed separately. Do not infer companion readiness from the article's review.
- Editorial polish: qualify categorical showing diagnoses; use achieved rent for fees; distinguish summer move-ins from the recent earlier rent-growth peak.

## Operating System improvements

- Type C: Record the ShowMojo metric accurately and review earlier AEBP vacancy content that repeats average/median and vacancy/days-on-market conflations. Target: `knowledge/company/industry-vacancy-benchmarks.md`.
- Type C: Record approved anonymized anecdote wording and any reuse constraints after Brian's decision. Target: `knowledge/company/anecdote-log.md`.
- Type C: The schema does not declare its own version constant. This review uses 1.0.0 consistently with existing review artifacts; add a canonical version declaration. Target: `automation/schemas/review.schema.json`.
- Type C: Add a documented way to record blocked/not-applicable checks and general nonlegal evidence findings; binary gates currently require explanatory notes. No standards were modified in this review. Target: `docs/07-Editorial-Automation.md`.

## Evidence links

- [berkeley](https://rentboard.berkeleyca.gov/rights-responsibilities/rent-levels/annual-general-adjustment)
- [oakland](https://www.oaklandca.gov/Community/Housing-Programs-Support/For-Landlords/Allowable-Rent-Increases/Learn-More-About-Allowable-Rent-Increases)
- [show](https://www.peterlohmann.com/blog/pm-trends-report-2026)
- [season](https://www.apartmentlist.com/research/the-rental-markets-peak-season-is-becoming-less-pronounced)
- [company](https://alleastbayproperties.com/llms.txt)

## Handoff

Claude should create `02-revision-response.md` and `.json`, addressing every numbered finding. Brian's reserved anecdote-reuse decision remains distinct from factual verification. Re-review the updated WordPress drafts before publication; a later PASS still requires Brian's final read.

