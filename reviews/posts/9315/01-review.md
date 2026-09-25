# Editorial Review — Post 9315

**What Overpricing a Rental Really Costs: The Vacancy Math**

Recommendation: **HOLD PENDING FIXES**

Review mode: Pre-Publish Audit. Reviewed September 24, 2026 (America/Los_Angeles).
Reviewer: ChatGPT (GPT-6).
Standards: docs/01 v0.5; docs/02 v0.2; docs/03 v0.2; docs/07 v0.1; applicable manifest v0.1.
Repository: `da1aaaf951cc97442e53fa631d34aff8298b5f64`; clean before artifact creation, matches GitHub main.
WordPress: [draft 9315](https://dev.alleastbayproperties.com/?post_type=video&p=9315).

## Context and limits

Companion to 9313, independently reviewed as part of the cornerstone package. Full snapshot draft post_modified 2026-09-24 22:25:53; timezone not supplied, revision ID/GMT not returned. Same standards/commit and pre-write repository state as parent. Legal/local/compliance gates pass for the reviewed educational script: it contains no city-specific statutory figures or individualized legal instruction. Those passes do not clear the unsupported market-wide repair comparison, handled under VIDEO-CONSISTENCY and evidence rules. VIDEO-TRANSCRIPT-LITERAL passes only for correct pre-recording labeling; there was no recording to compare. Technical FAIL records uncompleted production/access checks, not proven missing generated schema. See 9313 review for shared sources and complete package context. Scores are estimates; schema_version 1.0.0 follows existing artifact convention because schema lacks a declared constant. Claude should respond separately to every numbered finding. No WordPress edits. Local artifacts only; not committed or pushed.

## Gated categories

### GATE-LEGAL-ACCURACY — PASS

### GATE-LOCAL-ACCURACY — PASS

### GATE-TECHNICAL-SEO — FAIL

**9315-F03 — Type B**

- **Finding:** “Video in production. It will be embedded here once it's live.”
- **Root Cause:** The independent companion source review found 31 balanced block markers, metadata, image alt and conversion link, but no finished video. Public preview fetch failed; final template and applicable video schema cannot be inspected. The full-guide production URL is not yet accessible.
- **Fix:** Keep this page draft until recording/embed and final rendered checks are completed. Verify guide link at release and compare spoken recording with transcript before relabeling Video Script. Lack of raw JSON-LD is not proof that generated schema is absent.
- **Future Prevention:** Provide an authenticated preview and final video metadata in the companion handoff.

### GATE-COMPLIANCE-RISK — PASS

### GATE-ANECDOTE-INTEGRITY — FAIL

**9315-F01 — Type B**

- **Finding:** “Nothing was wrong with the unit.”
- **Root Cause:** Core case is documented, but this condition detail is not. The case note records make-ready work without establishing marketed condition. The package notes reserve reuse approval for Brian; see parent 9313-F04.
- **Fix:** Remove or document the condition assertion in both script copies. Resolve the reserved reuse decision, or replace the story with documented portfolio facts.
- **Future Prevention:** Store approved wording and reuse constraints in the anecdote log.

### VIDEO-TRANSCRIPT-LITERAL — PASS

### VIDEO-CONSISTENCY — FAIL

**9315-F02 — Type A/B**

- **Finding:** “Here's a pricing mistake that costs East Bay landlords more than almost any repair: listing high to see what happens.”
- **Root Cause:** Neither the hypothetical rent-loss calculation nor the case record supports a comparative claim about almost all repair costs. Both scripts repeat it. The companion also generalizes a loss exceeding a year's premium outside the example.
- **Fix:** Use 'Here's how testing a high rental price can cost thousands in lost rent.' Explicitly tie $3,450 and the year's-premium comparison to an assumed six extra vacant weeks in the hypothetical; label the Oct–Jan pricing instruction as professional opinion. Apply changes to both scripts and the companion summary.
- **Future Prevention:** Do not convert a worked example into a market-wide quantitative claim; check script, takeaways and article together.

## Scored categories

All scores are editorial estimates, not measured rubric outputs.

### SCORE-SEO: 90/100 — PASS (minimum 90)

- **What's working:** Descriptive title, metadata, image alt and useful links.
- **What's holding it back:** Final render/video output unverified.

### SCORE-GEO: 89/100 — FAIL (minimum 95)

- **What's working:** Short summary, takeaways and resources.
- **What's holding it back:** Example-to-general-claim drift and unsupported repair comparison.

### SCORE-EEAT: 88/100 — FAIL (minimum 95)

- **What's working:** Underlying real event has internal documentation.
- **What's holding it back:** Added condition assertion lacks evidence and reuse remains pending.

### SCORE-READABILITY: 94/100 — PASS (minimum 90)

- **What's working:** Brief, clear script and simple numbers.
- **What's holding it back:** Specify assumed six extra weeks and soften the opening.

### SCORE-CONVERSION: 90/100 — PASS (minimum 85)

- **What's working:** Direct consultation CTA and guide link.
- **What's holding it back:** Guide destination must resolve at release.

### SCORE-OVERALL: 89/100 — FAIL (minimum 95)

- **What's working:** Accessible explanation matching the parent concept.
- **What's holding it back:** Claim fixes, reuse disposition, video production and technical verification remain.

## Claim provenance

- **9315-C01 — documented:** “We've watched this happen. In one turnover we handled, the unit went through several price cuts over a period of months and leased close to where comparable units had been renting all along.” Also supports the excerpt and 'What we've seen' takeaway. Core event documented; does not clear reuse or condition embellishment. Source: C:/Users/brian/OneDrive - ALL EAST BAY PROPERTIES/Website-Assets/2026-Content-Strategy/10-October/pricing-case-study-HOLD-for-sept-oct.md; C:/Users/brian/OneDrive - ALL EAST BAY PROPERTIES/Website-Assets/2026-Content-Strategy/10-October/2026-09-28-week-package-notes.md
- **9315-C02 — unverified:** “Nothing was wrong with the unit.” See 9315-F01.
- **9315-C03 — hypothetical_example:** “Say a unit is worth $2,500 a month.” The page calls it illustrative; make six extra weeks explicit in the spoken calculation.

## Strengths Worth Preserving

- Script is correctly labeled before recording.
- The two script copies match at review time.
- Core $575 weekly and $3,450 six-week arithmetic agrees with the article.
- Resources and consultation CTA offer useful next steps.

## Article fixes

- 9315-F01: Remove or document the condition assertion in both script copies. Resolve the reserved reuse decision, or replace the story with documented portfolio facts.
- 9315-F02: Use 'Here's how testing a high rental price can cost thousands in lost rent.' Explicitly tie $3,450 and the year's-premium comparison to an assumed six extra vacant weeks in the hypothetical; label the Oct–Jan pricing instruction as professional opinion. Apply changes to both scripts and the companion summary.
- 9315-F03: Keep this page draft until recording/embed and final rendered checks are completed. Verify guide link at release and compare spoken recording with transcript before relabeling Video Script. Lack of raw JSON-LD is not proof that generated schema is absent.

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

