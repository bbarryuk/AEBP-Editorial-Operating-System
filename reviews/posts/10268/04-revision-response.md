# Revision Response 04 — Post 10268

Responds to: `reviews/posts/10268/03-final-review.json` (2026-10-31T04:10:44.820Z)  
Responder: Claude (Cowork) · 2026-10-31T04:20:00Z  
Repo: `6c10e32acdeee4f44681ec9e835fd92a1cb1aab7` (dirty: response files, rent-caps.md, tests/legal/TEST-LEGAL-008.md)  
WordPress: draft, https://dev.alleastbayproperties.com/?p=10268

**Summary:** F03 accepted (RAP Notice attachment restored; my round-02 deletion was the error). F09 accepted (banking-expiration window removed in favor of the reviewer's conservative wording; knowledge file marked unresolved). F07 stays open as requires_human until the video and an authenticated preview exist. New regression test TEST-LEGAL-008 records both round-02 mistakes.

**requires_human_review:** true · **recommendation_to_brian:** proceed_to_gpt_final_review

## Dispositions

### 10268-F03 — accepted

**Rationale:** Correct, and my error: round 02 deleted an independently applicable duty. Confirmed against the ordinance snapshot, OMC §8.22.070H.1, H.4 and H.6: every rent increase notice must include notice of the Chapter and the right to petition in the RAP-prescribed form, or the increase is invalid. Logged as TEST-LEGAL-008 Finding A.

**Change applied:** Separate bullet restored ahead of the business-tax bullet; registration, timing and tax-document bullets kept. Sources line now cites OMC §8.22.070.

> After: Include a copy of the City's RAP Notice with every rent increase notice.

### 10268-F09 — accepted

**Rationale:** Correct. The ten-year/five-year accrual-date rule came from a tool summary of the 5/28/26 info sheet, not a full read, and conflicts with OMC §8.22.070B.5.c in the ordinance snapshot (flat five years). Applied the reviewer's conservative wording rather than retaining any specific window. rent-caps.md now marks the rule UNRESOLVED; logged as TEST-LEGAL-008 Finding B.

**Change applied:** Key Facts row 'Oakland banked increases' removed. Body sentence replaced and linked to the City's allowable-increases page. 'and expiration' removed from the Oakland Sources line.

> Before: Banked amounts that accrue on or after January 1, 2026 expire after five years.

> After: Banked CPI increases are subject to expiration and other eligibility limits. Check Oakland's current banking rules before including older amounts.

### 10268-F07 — requires_human

**Rationale:** Not deferring this again: it stays open. The production placeholder is accurate and stays. Clearance needs (1) the recorded video, embedded and checked, with the 'Prefer video?' line restored only once its destination works, and (2) an authenticated preview of the rendered post (BlogPosting/FAQPage output, block validity, final internal destinations), which Claude can't access. Brian or Claude can do the preview once Brian provides access or screenshots; the post stays draft until both are done.

> Before: 🎥 Companion video in production; the video and transcript will be added when ready.

## Operating System follow-ups

- rent-caps.md: ten-year/five-year banking-expiration claim marked UNRESOLVED (do not cite); OMC §8.22.070H RAP Notice attachment duty recorded. Target: `knowledge/laws/rent-caps.md`.
- Regression case for dropping the RAP Notice attachment and for promoting an unreconciled agency summary over the ordinance snapshot. Target: `tests/legal/TEST-LEGAL-008.md`.
- Reconcile Oakland's banking-expiration rule (OMC §8.22.070B.5.c vs. RAP info sheet 5/28/26 vs. RAP Regulations) when Brian or a reviewer can read the full info sheet and Regulations; until then, generic wording only. Target: `knowledge/laws/rent-caps.md`.
