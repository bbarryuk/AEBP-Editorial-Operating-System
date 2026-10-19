# Follow-up Review — Post 10196

**How to Talk With Tenants About Safety Without Overpromising (Video)**

**Recommendation: HOLD PENDING FIXES.** Body and script corrections verified; one missed excerpt correction remains, plus production/technical readiness.

Pre-Publish Audit · October 18, 2026 (America/Los_Angeles) · WordPress modified 2026-10-18 21:17:39, draft (timezone unspecified; no revision ID/GMT supplied).

Repository `325556c529d5a521f985e46c2bacaa5eeef7fc55`, clean before artifacts. Standards: docs/01 v0.5; docs/02 v0.2; docs/03 v0.3; docs/07 v0.1; manifest v0.1.

## Prior findings

- 10196-F01 — CLOSED in body/script: scoped protection is present in script, key takeaway and chapter list. Excerpt carryover is recorded separately as 10196-F04.
- 10196-F02 — CLOSED in body/script: best-practice response and covered-lock notice are separated; chapter item updated. Excerpt carryover is recorded separately as 10196-F04.
- 10196-F03 — OPEN / requires_human: production placeholder remains. The human-required disposition is preserved, not silently cleared.
- 10196-F04 — NEW: excerpt was missed by the otherwise successful legal-text synchronization.

## Gated categories

- **GATE-LEGAL-ACCURACY: FAIL** — 10196-F04
- **GATE-LOCAL-ACCURACY: PASS**
- **GATE-TECHNICAL-SEO: FAIL** — 10196-F03
- **GATE-COMPLIANCE-RISK: PASS**
- **GATE-ANECDOTE-INTEGRITY: PASS**
- **VIDEO-TRANSCRIPT-LITERAL: PASS**
- **VIDEO-CONSISTENCY: PASS**

Companion review PASS means inspected separately, not approved for publishing. Script-label PASS does not certify a recording. The technical gate remains a production/verification hold.

## Open findings

### 10196-F04 — Type A

**Finding:** Watch: why "secure building" and "safe neighborhood" are promises a landlord can't keep, what to put in writing for every tenant, why a lease can't discourage calls to the police, and how to treat a security report as notice.

**Root cause:** The excerpt still carries the two unqualified claims corrected in the body and script under 10196-F01/F02. Excerpts are separate WordPress fields and can surface on archive cards, search or feeds. This is a missed synchronization, not a new objection to the accepted script.

**Fix:** Replace post_excerpt with: “Watch: how East Bay landlords can describe security features without overpromising, explain protected calls for help, and respond to reports about locks, lighting and doors.”

**Future prevention:** Include post_excerpt alongside body, takeaways, script, SEO metadata and distribution copy in paired-post revision checks.

### 10196-F03 — Type A/B

**Finding:** 🎥 Video in production. It will appear here once it's live.

**Root cause:** 10196-F03 remains requires_human in response 02. The video is still unrecorded/unembedded, so playback, recording-checked transcript, duration, thumbnail, chapters and rendered schema are not verified.

**Fix:** Retain draft status until the final video is available. Replace the production placeholder with the actual playable embed, add recording-derived chapters and a recording-checked transcript, and verify authenticated preview, generated schema and final destination links. Use “Video Transcript” only after checking it against the audio. Do not invent video IDs, duration or timestamps.

**Future prevention:** Require a production-completion check after the script review; maintain VIDEO-TRANSCRIPT-LITERAL.

## Scored categories

Estimates, not a measured rubric.

| Category | Score / minimum | Status | What's working | What's holding it back |
|---|---:|---|---|---|
| SCORE-SEO | 89/90 | FAIL | Focused query, populated Yoast fields and relevant internal links. | Video is not yet playable; stale excerpt needs replacement. |
| SCORE-GEO | 93/95 | FAIL | Answer-first structure and extractable facts/takeaways. | Body and script corrected, but excerpt still contains old broad claims. |
| SCORE-EEAT | 94/95 | FAIL | Documented practitioner process and identifiable primary legal texts. | Excerpt conflicts with corrected legal scope. |
| SCORE-READABILITY | 96/90 | PASS | Plain language with scannable sections and short script. | No blocking script readability issue found. |
| SCORE-CONVERSION | 91/85 | PASS | Relevant property-management CTA with live consultation destination. | Watch-page delivery remains incomplete. |
| SCORE-OVERALL | 93/95 | FAIL | Clear educational purpose and documented AEBP examples. | Excerpt fix and production/technical checks remain open. |

## Strengths Worth Preserving

- The features-versus-outcomes framing gives readers usable replacement language.
- AEBP welcome-sheet, lock-triage and lease practices are documented; no invented incident is needed.
- O’Hara is presented as claims allowed to proceed, not a final damages verdict.
- The script is correctly labeled as a script while recording is pending.

## Claim provenance

No experience claim changed. All remain documented, not AI owner-verified.

- **10196-C01 (documented):** “At AEBP, every new tenant gets a welcome sheet with our 24/7 maintenance line, and a broken entry lock is an emergency, with a vendor sent the same day.” Source: knowledge/company/anecdote-log.md (2026-09-30, 2026-10-16 and 2026-10-18 entries; committed at reviewed HEAD). Documented internal record; not AI owner verification.

- **10196-C02 (documented):** “Our lease asks tenants to research the neighborhood themselves. We describe the building, and how to reach us.” Source: knowledge/company/anecdote-log.md (2026-09-30, 2026-10-16 and 2026-10-18 entries; committed at reviewed HEAD). Documented lease practice; final sentence is professional framing, not an independently verified universal listing-language policy.

- **10196-C03 (documented):** “We manage 600+ rental units across Oakland, Berkeley, Emeryville and the wider East Bay.” Source: knowledge/company/overview.md; https://alleastbayproperties.com/llms.txt. Documented internal record; not AI owner verification.

## Article fixes

- 10196-F04: replace stale post_excerpt with the supplied wording.
- 10196-F03 (open; requires_human): finish video and authenticated technical checks.

## Operating System improvements

- Add a maintained security-duty reference separating lock-statute notice, guard foreseeability, general reasonable-care duties, protected police calls and incident warnings. Sources are available, so this system gap does not independently block these posts. Target: `knowledge/laws/landlord-security-duties.md`. Type C follow-up: yes.

- Add an explicit blocked/not-verified representation for rendered-page checks; the current PASS/FAIL schema forces incomplete checks into FAIL with explanatory evidence-gap text. Target: `automation/schemas/review.schema.json`. Type C follow-up: yes.

- Include WordPress excerpts in companion-revision synchronization checks; the body/script fixes did not update the video excerpt. Target: `reviews/video-review.md`. Type C follow-up: no.

Company-overview refresh follow-up is closed; the current source was refreshed on October 18.

## Scope and evidence

Follow-up Pre-Publish Audit against response 02 and full current AEBP-Dev snapshots. WordPress post_modified 2026-10-18 21:17:39 (as returned; timezone unspecified); no revision ID or GMT supplied. Repository clean before artifacts, HEAD 325556c529d5a521f985e46c2bacaa5eeef7fc55, zero commits ahead of locally recorded origin/main; no fetch. Standards and schemas unchanged from review 01 (git diff checked): docs/01 0.5, docs/02 0.2, docs/03 0.3, docs/07 0.1, applicable manifest 0.1. Schema version 1.0.0 follows established artifacts. 10196-F01 — CLOSED in body/script: scoped protection is present in script, key takeaway and chapter list. Excerpt carryover is recorded separately as 10196-F04. 10196-F02 — CLOSED in body/script: best-practice response and covered-lock notice are separated; chapter item updated. Excerpt carryover is recorded separately as 10196-F04. 10196-F03 — OPEN / requires_human: production placeholder remains. The human-required disposition is preserved, not silently cleared. 10196-F04 — NEW: excerpt was missed by the otherwise successful legal-text synchronization. Every prior finding has a response disposition. Both scripts match exactly; both full post block-comment stacks balance, which is not editor validation. Full body, excerpt, metadata, terms, author and thumbnail reviewed. No new first-person claims; documented provenance from review 01 retained. The welcome-sheet entry is now committed, and company overview was refreshed October 18 (600+ units and bilingual maintenance line corroborated). Earlier stale-overview follow-up is closed. Statutory 1941.3 and 1946.8 text re-read through Justia mirrors this turn; other unchanged source findings carry forward from review 01 in this same session. Official-source access and case-treatment limitations from review 01 remain. No fresh authenticated preview was available or attempted this round; prior 404 result and response's explicit production deferral remain unresolved. No claim that missing raw JSON-LD proves schema absent. No video/audio exists for transcript verification. GBP precision verified in current week4 package notes; other social claims not comprehensively audited. Companion gate PASS means independent review occurred, not publication approval. VIDEO-CONSISTENCY PASS refers to matched scripts and corrected body claims; stale excerpt independently fails the legal gate on 10196. No WordPress changes. All scores are estimates.

- [Civil Code §1941.3](https://law.justia.com/codes/california/code-civ/division-3/part-4/title-5/chapter-2/section-1941-3/)
- [Civil Code §1946.8](https://law.justia.com/codes/california/code-civ/division-3/part-4/title-5/chapter-2/section-1946-8/)

See review 01 for unchanged case-law, municipal-number and company-source checks. Responses 02 were checked against the actual drafts, not accepted as proof on their own.

## Handoff

Claude should apply 10196-F04 and record its disposition in 04-revision-response.*. Preserve the requires_human state for 10196-F03 until video production and final checks are complete. Brian's final read is still required. No post was edited or published.

