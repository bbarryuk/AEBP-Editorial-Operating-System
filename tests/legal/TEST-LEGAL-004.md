---
title: "TEST-LEGAL-004 — Wrong-scenario statute citation (Civil Code §1950.5 applied to an agent change, not an ownership change) plus a near-miss on anecdote specificity"
doc_type: informative
owner: Brian
last_verified: 2026-07-18
source_case: WordPress post 8342 / video 8344, "How to Switch Property Managers in California Without Losing a Tenant or Violating Your Lease" (drafted 2026-07-18, Pre-Publish Audit requested same day before Brian's own pass to ChatGPT)
---

# TEST-LEGAL-004

Fourth real entry in the `/tests/legal/` regression suite. Logged from an actual case, not invented. Two distinct findings from the same review, kept together because they were caught in the same pass and both concern claim specificity outrunning verification.

## Finding 1 — Civil Code §1950.5 cited for the wrong scenario

### Excerpt

From the original draft's Step 3 and Key Facts table:

> "If your outgoing manager was holding the deposit, California law requires it to transfer to a successor in interest along with a written itemized statement of any lawful deductions (Civil Code §1950.5)."

### Rule IDs triggered

- `GATE-LEGAL-ACCURACY` — **FAIL as originally drafted** (Type A, Content Error — not just missing a citation, the citation given supports a different scenario than the one being described).
- `EVD-CITATION-REQUIREMENT` / `EVD-SOURCE-HIERARCHY` — the citation was sourced from a WebSearch AI-generated summary of secondary results, not from the statute's own text. A direct primary-source fetch (via FindLaw's mirror, since leginfo.legislature.ca.gov returned empty content on a static fetch — a known tooling gap, see `knowledge/laws/rent-caps.md`'s Richmond note) surfaced the actual scope of the provision.

### Why this one is instructive

§1950.5(i)–(k)'s "successor in interest" transfer provisions trigger "upon termination of the **landlord's interest** in the premises, whether by sale, assignment, death, appointment of receiver, or otherwise" — a change of **ownership**. The post's actual scenario is an owner switching **property managers** while keeping title. Those are different events. The statute simply doesn't speak to a same-owner agent switch the way the draft implied.

The correct authority for "an outgoing property manager holding a tenant's deposit must account for it and hand it over" is Business & Professions Code §10145 (broker trust fund handling: funds "shall be maintained there until disbursed by the broker in accordance with instructions from the person entitled to the funds") — a trust-fund duty tied to the broker's license, not a landlord-successor event under §1950.5.

This is a subtler failure mode than `TEST-LEGAL-001`/`002`/`003` (all "correct claim, no citation" cases): here the underlying *idea* was reasonable (some law requires an accounting), but the specific statute named doesn't actually establish it for this scenario. A secondary-source WebSearch summary is good enough to identify that *a* rule probably exists; it is not good enough to confirm *which* rule, or its exact scope — that took a primary-source fetch of the actual statutory text.

### Expected verdict

`GATE-LEGAL-ACCURACY` should **FAIL** as originally drafted. After the fix (2026-07-18): §1950.5 citations in post 8342 now only appear where the statute actually applies (deposit limits, permitted uses, itemized-statement-to-tenant rules generally); the manager-to-manager/manager-to-owner trust fund handoff claim is now cited to Business & Professions Code §10145 instead. New knowledge file `knowledge/laws/change-of-manager-notice.md` documents both statutes' actual scope, plus the confirmed full text of Civil Code §1962 (previously cited only from secondary-source summaries, now verified against primary text via FindLaw's mirror).

## Finding 2 — AEBP-specific claim drifted past what Brian confirmed

### Excerpt

Brian confirmed two real, specific facts in chat: (1) "In nearly all cases, our owners hold the security deposits with a few rare exceptions," and (2) AEBP sends a specific welcome letter / §1962(c) addendum to every tenant before collecting rent (a real document was attached and reviewed). Both were used correctly. But in the same drafting pass, the post's Step 3 "From our files" paragraph escalated to:

> "We've onboarded from managers who couldn't produce a clean itemized statement, and separately we've onboarded owners who weren't entirely sure themselves how much they were holding or for which unit."

— and the video page's body copy added: "...a tenant nobody has a working phone number for, or a lease that can't be located," and "the single most common gap we find."

Neither of these more specific claims was confirmed by Brian. They were invented, in the same style as the confirmed claims, during the same drafting pass that correctly used the real ones — which is exactly the failure mode `EVD-ANECDOTE-INTEGRITY` describes: a confirmed real observation and a plausible invented elaboration sitting next to each other, both written in the same confident first-person voice, with nothing in the text distinguishing which is which.

### Rule IDs triggered

- `GATE-ANECDOTE-INTEGRITY` — **FAIL as originally drafted**, self-caught during the same Pre-Publish Audit review that found Finding 1, before Brian read the draft.
- `EVD-ANECDOTE-INTEGRITY` — the specific violation: adding invented specificity ("couldn't produce a clean itemized statement," "weren't entirely sure themselves how much they were holding," "the single most common gap we find") to a claim that had a real, confirmed, but more general version already available and sufficient.

### Why this one is instructive

This is the same failure mode as `TEST-EDITORIAL-001` (post 8006), but with an important difference worth preserving: in 8006, the anecdote was invented from nothing, with no real fact behind it at all. Here, a real, Brian-confirmed fact existed (owners hold their own deposits; AEBP sends a §1962(c) letter) and was used correctly — the drift happened in a *second*, unconfirmed layer added on top of it, in the course of trying to make the observation feel more concrete. `EVD-ANECDOTE-INTEGRITY`'s existing process note (treat a request to make a claim "more specific" as a prompt to re-verify) already anticipated this, but this case shows it applies even when *no one asked* for more specificity — the drafter can generate that pressure internally, mid-draft, without any external prompt at all.

Caught this time by the same AI that drafted it, on a structured re-read against `docs/02`, rather than only by Brian on a cold read — a useful data point that a deliberate post-hoc pass against `EVD-ANECDOTE-INTEGRITY` line-by-line can catch what happened during drafting, even without a second reviewer.

### Expected verdict

`GATE-ANECDOTE-INTEGRITY` should **FAIL** as originally drafted. After the fix (2026-07-18): both passages reverted to only the Brian-confirmed claims (deposit-holding norm, the §1962(c) welcome letter practice), with the invented specifics removed rather than softened-but-kept. Now **PASS**. No new knowledge file needed here — the fix is behavioral (a stricter self-check pass), not a missing reference document.

## What this should catch in the future

Two distinct lessons, worth re-running separately:

1. **A citation found via WebSearch summary should be treated as "a rule like this probably exists," not "this is the rule."** Before a statute number goes into gate-checkable content, fetch the primary text (or a direct mirror, given the leginfo.legislature.ca.gov tooling gap) and confirm it actually covers the scenario being described — not just the general topic area. Re-run this case if a future draft cites a specific Civil Code or Business & Professions Code section sourced only from a search-engine summary.
2. **A drafting pass that correctly uses a real, confirmed AEBP fact is not thereby safe from also inventing an adjacent, unconfirmed elaboration in the same paragraph.** `GATE-ANECDOTE-INTEGRITY` has to be checked claim-by-claim within a section, not once per section on the assumption that a confirmed anchor fact vouches for everything drafted near it. Re-run this case if a future review treats "the post has a real AEBP observation" as sufficient without checking whether every specific detail attached to it was actually confirmed.
