---
title: Review Format
doc_type: normative
version: 0.2 (Working Draft)
status: drafted, informed by two real reviews (post 7938, post 8006) and two rounds of ChatGPT critique
owner: Brian
last_updated: 2026-07-08
purpose: Defines how an editorial review is classified, structured, and written up — so two different reviewers (Claude, ChatGPT, or a human) produce comparable output.
used_by: [Claude, ChatGPT, human reviewer]
depends_on: [docs/01-Editorial-Standards.md, docs/02-Evidence-and-Sourcing.md]
referenced_by: [reviews/*.md]
---

# Document 03 — Review Format

## Purpose

`docs/01` defines *what* gets checked (the gates and scores). `docs/02` defines *what counts as evidence*. This document defines *how the findings get written up* — so a review is diagnostic, not just a verdict, and so two reviewers working from the same standards produce output that's actually comparable.

This document exists because the first real review (post 7938, 2026-07-07) produced a flat pass/fail list with impressionistic score estimates and no structure for distinguishing "the content is wrong" from "the content is probably right but unverifiable as written" from "the Operating System has no reference material to check this against." ChatGPT's critique of that review is what prompted this document; the structure below is Claude's synthesis of that critique, not a verbatim adoption — see "Where this diverges from the ChatGPT critique" at the end.

## FIND-TYPE — Classify every finding before writing it up

Every failed gate or flagged issue gets one of three types. The type determines what fixing it actually requires — which is more useful than a generic severity label.

| Type | Meaning | What fixes it |
|---|---|---|
| **Type A — Content Error** | The draft asserts something factually wrong, or violates a standard as currently written. | Change the claim itself. |
| **Type B — Evidence Gap** | The claim is plausible or even correct, but the post doesn't cite or verify it per `docs/02`. | Add a citation. The underlying claim may not need to change at all. |
| **Type C — System Gap** | The reviewer can't fully evaluate the claim because the Operating System itself has no reference material for it — no `/knowledge` file to check against, no rule covering this scenario. | Build the missing reference material (new `/knowledge` doc, new rule, new `/tests` case) — independent of whatever happens to the post. |

A single finding can be more than one type. Post 7938's rent-cap claims were Type B (no citation in the post) *and* Type C (no `knowledge/laws/rent-caps.md` existed for the reviewer to check the number against) at the same time — fixing the citation didn't fix the system gap, and vice versa. Log both.

**Why this document does not add separate "Accuracy" and "Evidence" gates.** ChatGPT's second-round proposal (2026-07-08) suggested splitting accuracy and evidence into two distinct review gates. Not adopted, for the same reason a claim can be both Type A and Type B at once: a single finding routinely needs both tags simultaneously, and a gate structure forces it into one bucket or the other. `FIND-TYPE` already carries this distinction per-finding rather than per-category — extend the type system if a new distinction is needed, rather than adding a parallel gate that can disagree with it.

## FIND-SEVERITY — Why this document does not add a separate severity scale

ChatGPT's critique proposed a Critical/Major/Minor severity scale layered on top of every finding. This document deliberately does not adopt that, for one reason: `docs/01` already establishes that gated categories are pass/fail with **no partial credit** — a legal claim is either sourced and correct, or it isn't. Bolting a three-tier severity scale onto a binary gate quietly reintroduces the partial credit that principle was written to rule out ("it only failed a Minor," etc.).

Severity-equivalent information is already carried by FIND-TYPE instead:

- **Type A always blocks.** It's a gate failure by definition — that's what "Critical" would have meant anyway.
- **Type B blocks this post until cited**, but is typically the fastest fix (the claim doesn't change, just gets sourced) — functionally closer to what "Minor" was reaching for, without pretending the gate itself has degrees.
- **Type C often does *not* block this specific post** if the claim is independently reasonable and sourced elsewhere — but it always produces a follow-up task regardless of whether this post ships.

For `SCORE-*` categories, the existing 0–100 thresholds in `docs/01` already are a severity gradient. A second severity label there would be redundant, not additive.

## FIND-STRUCTURE — Root cause format for every Type A or Type B finding

Instead of a one-line description, write each finding as:

- **Finding** — what's actually in the draft (quote it).
- **Root Cause** — why this happened. Was reference material missing (Type C)? Was the standard itself ambiguous? Did the writer skip a step the process assumes but doesn't enforce?
- **Fix** — the specific, minimal change that resolves it for *this post*.
- **Future Prevention** — what changes about the process, the standards doc, or the knowledge base so the same gap doesn't recur on the next post. This is often where a Type C system gap gets logged even when the immediate Fix is small.

## FIND-STRENGTHS — Strengths Worth Preserving

Every review includes a section naming what the post did well — specifically, anything that's a genuine differentiator (an AEBP-specific observation, a correctly-hedged estimate, good use of `EVD-CONFIDENCE-LEVELS`) rather than generic praise. The point isn't encouragement for its own sake — it's that a standards document which only ever documents failures will eventually get "fixed" in ways that accidentally regress something that was working. Naming it explicitly gives future revisions something concrete to check against, the same way `/tests` does for failures.

## FIND-SCORING — Presenting scored categories

`docs/01`'s `SCORE-*` categories stay numeric (0–100) — that decision isn't reopened here. What changes is how the number is presented: a bare estimate like "SCORE-SEO ~88" asserts false precision and gives the next reviewer nothing to act on. Instead, present each scored category as:

- The numeric estimate (still explicitly labeled as an estimate unless it was actually computed against a rubric)
- **Threshold status** — pass/fail against the `docs/01` minimum, stated plainly
- **What's working** — one or two specific strengths
- **What's holding it back** — the specific gap(s) keeping it under threshold, not a vague "could be improved"

## FIND-FIXLISTS — Separate the two kinds of fix

Every review ends with two distinct lists, not one merged one:

- **Article fixes** — changes to *this specific post*: add a citation, correct a claim, restructure a section. Scoped to what ships.
- **Operating System improvements** — anything the review surfaced that belongs in the repo instead: a missing `/knowledge` file, a rule that needs sharpening, a new `/tests` case. These persist regardless of what happens to the post under review, and shouldn't get lost inside a post-specific to-do list.

Keeping these separate is what prevents the mistake the first review nearly made: treating "fix the article" and "fix the system" as the same task with the same urgency, when they usually aren't.

## REVIEW-MODE — Which review is being requested

Added 2026-07-08, proposed by ChatGPT after reviewing a Thursday Tip post outside this framework entirely — a useful failure, since it showed that "review this post" is ambiguous about *what* gets checked. Three modes:

| Mode | Includes | Excludes | Use when |
|---|---|---|---|
| **Editorial Review** | `SCORE-READABILITY`, brand voice (once `docs/04-Brand-Voice.md` exists), prose-level flow/engagement notes | All `GATE-*`, `SCORE-SEO`, `SCORE-GEO`, `SCORE-CONVERSION`, `GATE-COMPLIANCE-RISK` | A quick gut-check on prose quality mid-draft, before the piece is otherwise finished |
| **QA Review** | All `GATE-*` and all `SCORE-*` from `docs/01`, plus the content type's manifest in `/reviews` if one exists | Freeform commentary not tied to a defined category | Confirming a finished draft meets the Operating System's defined bar |
| **Pre-Publish Audit** | QA Review + Editorial Review run together, plus a final internal-linking/schema/technical pass | Nothing — this is the full check | The last gate before Brian publishes |

**Default:** a review request that doesn't name a mode is treated as a **Pre-Publish Audit** — the highest bar — and the review's header states which mode actually ran, so the requester can see what was checked and ask for a lighter pass next time if that's what they wanted. This default exists because the reviews that have happened so far (post 7938, 7996, 8006) were all functionally pre-publish checks even when not labeled as such; defaulting to the narrower Editorial or QA mode would risk silently skipping gated categories on a request that meant "is this ready."

A review conducted outside any of the three modes — general editorial instinct with no stated scope, the kind ChatGPT flagged about its own Thursday Tip review — isn't invalid, but it isn't a Content Operating System review either, and shouldn't be logged as one in `/tests` or cited as having passed a gate it never actually checked.

## Review template

```
# Editorial Review — Post [ID]
**[Title]**
Published [date] · Reviewed [date] against docs/01 vX.X + docs/02 vX.X + docs/03 vX.X
Reviewer: [Claude/ChatGPT/human]
Review Mode: [Editorial Review / QA Review / Pre-Publish Audit]

## Gated categories (pass/fail)
### GATE-[ID] — PASS/FAIL
[If FAIL, use FIND-STRUCTURE format with FIND-TYPE tagged]

## Scored categories
[Use FIND-SCORING format per category]

## Strengths Worth Preserving
[FIND-STRENGTHS]

## Article fixes
[Scoped to this post]

## Operating System improvements
[Scoped to the repo]

## Recommendation
[Publish as-is / hold pending fixes / unpublish]
```

## Where this diverges from the ChatGPT critique

ChatGPT's review-of-the-review recommended: Type A/B/C classification (adopted, above), a Critical/Major/Minor severity scale (not adopted — see FIND-SEVERITY), root-cause analysis format (adopted, above), separated fix lists (adopted, above), structured qualitative scoring instead of bare numbers (adopted as a presentation layer, not a replacement for the numeric scale — see FIND-SCORING), and a Strengths Worth Preserving section (adopted, above). The one substantive disagreement is the severity scale; everything else is adopted close to as proposed.

## Round two, 2026-07-08 — ChatGPT's post-hoc Thursday Tip proposal

After reviewing post 8006 outside this framework entirely, ChatGPT proposed: (1) a 10-gate universal PASS/FAIL rubric replacing the `docs/01` gate/score split, (2) a `/reviews` folder of per-content-type manifests, (3) a formal Claude-drafts → self-check → ChatGPT-review → fix → verify → publish workflow, (4) machine-readable review output. Claude's pushback and ChatGPT's revised position, after seeing it: keep the gate/score split (binary categories stay binary, gradient categories stay scored — collapsing `SCORE-GEO`/`SCORE-READABILITY` into pass/fail reintroduces the same false-precision-removal problem the severity scale did); extend `FIND-TYPE` rather than adding separate Accuracy/Evidence gates (see the note under `FIND-TYPE` above); adopt a `GATE-COMPLIANCE-RISK` gate (added to `docs/01` this round — the one genuinely missing check in the original proposal); build `/reviews` as manifests that *extend* `docs/01`'s categories per content type rather than replace them (see `/reviews`); delay machine-readable output, since it would violate the "prove the manual process before automating" principle all three parties already agreed to; and add `REVIEW-MODE` (above) to make explicit what kind of review is being requested — the one item from ChatGPT's proposal that's about how reviewers engage with the framework rather than changing the framework, and the reason the original ambiguity happened at all.

## Status

v0.2 — informed by two real reviews (post 7938, post 8006) and two rounds of ChatGPT critique. Re-run `TEST-LEGAL-001` and `TEST-LEGAL-002` against this format the next time a review happens, to confirm `REVIEW-MODE` and the `FIND-TYPE` extension note hold up in practice rather than just resolving the disagreement on paper.
