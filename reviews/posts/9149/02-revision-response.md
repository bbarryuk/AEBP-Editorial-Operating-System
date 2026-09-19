# Revision Response — Post 9149 (Richmond Rent Control 2026)

**Responds to:** `reviews/posts/9149/01-review.json` (timestamp 2026-09-08T05:38:01Z, reviewer chatgpt / GPT-6 Codex, recommendation `hold_pending_fixes`)
**Reviewer (this response):** claude / claude-sonnet-5
**Timestamp:** 2026-09-08T06:04:36Z
**Repo state:** commit `3f947319d5734072553348a513650c79c0d7b928`, dirty (untracked `reviews/posts/`)
**WordPress:** post 9149, status draft, https://dev.alleastbayproperties.com/?p=9149
**requires_human_review:** true
**recommendation_to_brian:** hold_for_brian_decision

Before dispositioning, two contested findings were independently checked against primary sources rather than accepted or rejected on the review's word alone:

- **9149-01** (historical rate comparison): Fetched Oakland's own Allowable Rent Increases page (confirms Aug 2024 RAP rate = 2.3%) and found contemporaneous local reporting (RichmondSide, July 2024) confirming Richmond's 2024 AGA was 1.4%. So Richmond was already below Oakland in that cycle — the draft's "first time in years the two have swapped places" claim was wrong. **Review confirmed correct.**
- **9149-06** (RRIP fee frequency): Our own `knowledge/laws/richmond-rent-program.md` contains two conflicting statements — an older fee-summary line says a flat "$106/owner, annual," while the file's own January 2025 amendment section says annual for 3+ units, every 3 years for 1–2 units. This is a real inconsistency in our knowledge base, not an unresolvable dispute, so the amendment language (the more authoritative, dated source) was used. Filed as a follow-up to fix the knowledge file itself.

## Dispositions

| Finding | Disposition | What changed |
|---|---|---|
| 9149-01 | accepted | Historical comparisons scoped to the actual 2025–26 vs 2026–27 numbers; "first time in years" claim removed. |
| 9149-02 | accepted_with_modification | Single-family/condo coverage now says "not subject to Richmond's *local*" cap, with an AB 1482 statewide-cap note added in 3 places. |
| 9149-03 | accepted_with_modification | "Base Rent + AGA = MAR" formula replaced with an explanation (Base Rent + all lawful AGAs since + any banked AGA) and a pointer to the city's MAR calculator. |
| 9149-04 | accepted_with_modification | 30/90-day notice statement now reflects the cumulative 12-month test and mailed-notice timing. |
| 9149-05 | accepted_with_modification | Pre-notice checklist gained brochure-service and Rental Housing Fee items; registration section notes enrollment must be amended on ownership/contact/agent/status changes. |
| 9149-06 | accepted_with_modification | RRIP registration fee now correctly stated as annual (3+ units) / every 3 years (1–2 units), per the repo's own 2025 amendment. |
| 9149-07 | accepted_with_modification | Unverified "checking every notice" and "safe assumption" claims replaced with the documented Richmond business-license-letter anecdote (`anecdote-log.md`, 2026-08-26). |
| 9149-08 | **requires_human** | Ordered-list attribute fixed directly. Share-link icons and rendered schema/JSON-LD can't be verified via the API — needs Brian to check the live block editor. |
| 9149-09 | accepted_with_modification | Oakland-inspection comparison narrowed; couldn't confirm or rule out a comparable program in the time available. |
| 9149-10 | accepted_with_modification | Same rewrite as 9149-07 — restores a provenanced first-person AEBP observation instead of an unverified one. |

## Claim provenance updates

| Claim | Old | New | Action |
|---|---|---|---|
| C2 (multi-city mistake we watched for) | unverified | unverified | removed |
| C3 ("Richmond runs a bit hotter" as safe assumption) | unverified | unverified | removed |
| C4 (checking every Richmond notice) | unverified | documented | replaced with the business-license-letter anecdote |
| C5 ("nothing gets applied on the wrong city's clock") | unverified | documented | absolute claim dropped, 600+ units figure (documented) kept |

## New operating-system follow-ups

1. **`knowledge/laws/richmond-rent-program.md`** — reconcile the two conflicting RRIP registration-fee-frequency statements (flat "annual" vs. the 2025 amendment's 3+/1–2 unit split) so the file doesn't contradict itself.
2. **Share-link template** — the "Share this post" block (used across posts, including 9050) has 7 empty, unconfigured `wp:social-link` blocks. Site-wide decision needed: configure real profile links, or remove the block from the template.

## What still needs you directly

1. **Read the rewritten "What We See at AEBP" section** — it now leads with the rate-reversal observation and ties it to the documented business-license-letter anecdote instead of the unverified "we check every notice" claim. Worth a read to confirm it sounds like AEBP and not like a patch job.
2. **Open post 9149 in the WordPress block editor** and check: the numbered just-cause list renders correctly now; whether the share icons should be configured or removed; and whether the Article/FAQ schema is actually emitting valid JSON-LD (not verifiable from here).

Once you're comfortable with both, this is ready to go back to ChatGPT for the `03-final-review` pass per the AUTO-WORKFLOW loop.
