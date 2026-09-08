---
title: Editorial Automation Protocol — Phase 1 (Manual, Structured Artifacts)
doc_type: normative
version: 0.1 (Working Draft)
status: drafted, not yet run against a real post
owner: Brian
last_updated: 2026-09-08
purpose: Defines the machine-readable handshake between Claude and ChatGPT during editorial review, executed manually by Brian, so the JSON contract is proven before any API/GitHub Action orchestration is built.
used_by: [Claude, ChatGPT, human reviewer, Brian]
depends_on: [docs/01-Editorial-Standards.md, docs/02-Evidence-and-Sourcing.md, docs/03-Review-Format.md]
referenced_by: [automation/schemas/review.schema.json, automation/schemas/revision-response.schema.json, reviews/monday-cornerstone-review.md, reviews/thursday-tip-review.md]
---

# Document 07 — Editorial Automation Protocol

## Purpose

`docs/03-Review-Format.md` defines how a review gets written up for a human to read. This document defines how the same review gets written down for a *machine* to read — a JSON contract between Claude, ChatGPT, and Brian — so that if AEBP ever builds the API/GitHub Action pipeline described in `README.md`'s v2.0 roadmap, it automates a protocol that has already been used and refined by hand, rather than inventing the protocol at the same time as the automation.

This document was prompted by a proposal to build that full pipeline now (WordPress REST API + GitHub Actions + OpenAI API + Anthropic API, looping automatically to a PASS/BLOCK state). The repo's own standing principle — stated in `README.md`'s versioning section and reaffirmed in `docs/03`'s "Round two" notes — is that automation should only ever execute a process that has already been proven by hand. `GATE-ANECDOTE-INTEGRITY` and `EVD-ANECDOTE-INTEGRITY` exist because that manual process has already surfaced one real, serious failure mode (a GPT review that not only missed a fabricated AEBP anecdote but actively encouraged making it more convincing). That's evidence the manual process has been used enough to find an important gap — not evidence it's been proven enough to run unsupervised. This document is the middle step: formalize the JSON contract now, keep running it by hand, and only build Phase 2 once the contract itself has held up across real posts.

## AUTO-PHASING — Phase 1 is manual; Phase 2 does not exist yet

**Phase 1 (this document, active now):** Brian remains the courier between Claude and ChatGPT, exactly as today — pasting a draft into ChatGPT, pasting ChatGPT's findings back to Claude. The only change is that both sides produce and consume the JSON artifacts defined by `automation/schemas/review.schema.json` and `automation/schemas/revision-response.schema.json` instead of, or alongside, prose. No API calls, no GitHub Actions, no automatic WordPress writes, no automatic looping.

**Phase 2 (not started, not scoped beyond the sketch below):** an orchestrator — most likely a GitHub Action — reads and writes these same JSON artifacts via the OpenAI and Anthropic APIs and the WordPress REST API, without Brian manually copying anything between chat windows.

**Rule:** Phase 2 is not authorized by this document. Moving from Phase 1 to Phase 2 requires a deliberate decision, informed by Phase 1 actually being run on real posts and this document's schemas surviving contact with them without needing structural changes. Bumping this document from v0.1 to v1.0, per this repo's normal versioning discipline, is what marks that the contract is stable enough to consider automating — it does not by itself authorize building Phase 2.

## AUTO-SCOPE — what this protocol covers, and what it doesn't

This protocol covers exactly one loop: **WordPress draft → review → revision → review**, ending in a recommendation Brian acts on. It produces and consumes JSON artifacts about a single WordPress post (or a post plus its video-companion post, reviewed as the separate gate-checkable artifacts `reviews/monday-cornerstone-review.md`'s `CORNERSTONE-COMPANION-VIDEO` already requires).

**Explicitly out of scope**, now and for any future Phase 2 built on this document without a separate decision: Mailchimp campaign creation, GBP posting, Meta/Instagram/X/LinkedIn/Nextdoor social publishing, HeyGen video rendering, SMS. `docs/04-Social-Publishing.md` already governs the approval rule for live social posting ("Brian's explicit go-ahead on the specific post content before calling a live-posting tool, every time") and this document does not change or supersede that. If AEBP ever wants automated review artifacts for those channels, that's a new scope decision and probably a new document — not an extension read into this one.

## AUTO-WORKFLOW — the Phase 1 loop

```
Claude drafts WP post (status: draft)
        │
        ▼
Brian pastes draft + relevant docs/knowledge into ChatGPT, asks for review
        │
        ▼
ChatGPT produces reviews/posts/<post-id>/01-review.json
   (conforms to automation/schemas/review.schema.json)
        │
        ▼
Brian pastes 01-review.json to Claude
        │
        ▼
Claude produces reviews/posts/<post-id>/02-revision-response.json
   (conforms to automation/schemas/revision-response.schema.json)
   and updates the WordPress draft accordingly
        │
        ▼
Brian pastes the updated draft + 02-revision-response.json back to ChatGPT
        │
        ▼
ChatGPT produces reviews/posts/<post-id>/03-final-review.json
        │
        ▼
Brian reads the actual final draft (not just the JSON) and approves, or loops again
```

If a second round is needed, the same file-numbering pattern continues (`04-revision-response.json`, `05-review.json`, ...) rather than overwriting a prior round — the point of versioned artifacts is a full history of what each reviewer actually said and how it was disposed of, not just the latest state.

## AUTO-FILE-LAYOUT — where artifacts live

Per-post review artifacts live under `reviews/posts/<post-id>/`, as a new subfolder — **not** directly inside `reviews/`, which already holds the per-content-type manifests (`monday-cornerstone-review.md`, `thursday-tip-review.md`, etc.). Those manifests define *what gets checked for a content type*; `reviews/posts/<post-id>/*.json` records *what a specific reviewer found on a specific post*. Keeping the two apart avoids a numeric post ID ever being mistaken for, or colliding with, a manifest filename, and keeps "the standing rules for this content type" separate from "the history of one post's reviews" the same way `docs/` (behavior) stays separate from `knowledge/` (facts) elsewhere in this repo.

A review's `content_type` field (see schema) is what selects which manifest in `reviews/` applies in addition to the base `docs/01` gates — the manifest is not duplicated into the JSON artifact, only referenced.

## AUTO-VOCABULARY-REUSE — no parallel review system

The schemas defined by this document use `docs/01`'s `GATE-*` and `SCORE-*` IDs and `docs/03`'s `FIND-TYPE` (A/B/C) directly. They do not introduce a severity scale, a numeric confidence score on findings, or any classification scheme not already defined in `docs/01`–`03`. This was already litigated twice — a Critical/Major/Minor severity scale and a universal 10-gate rubric were both proposed and both rejected, for the same reason: a gated (pass/fail) category quietly regains partial credit the moment something scores it. `automation/schemas/review.schema.json`'s `gate_id` field is deliberately typed as a pattern-matched string, not a fixed enum — it must reference an ID that already exists in `docs/01` or in the relevant `reviews/*.md` manifest, but the schema itself does not hardcode the list, so a new gate added to `docs/01` doesn't require a schema change to be usable.

## AUTO-CLAIM-PROVENANCE — the anecdote-integrity contract, made checkable

`EVD-ANECDOTE-INTEGRITY` already states the rule in prose: a first-person "AEBP has done/seen/experienced X" claim must be confirmed real by Brian, replaced with a sourced general fact, or explicitly flagged as hypothetical — never invented. `GATE-ANECDOTE-INTEGRITY` in `docs/01` is the pass/fail check that rule feeds. Both existed before this document and are not changed by it.

What this document adds is a machine-readable field for that rule: every first-person AEBP-experience claim in a reviewed draft gets an entry in `claim_provenance`, tagged as one of:

- **`documented`** — backed by an identifiable internal record or citation (source-hierarchy level 6 done right, per `docs/02`).
- **`owner_verified`** — Brian has personally confirmed this happened, with no internal record cited (the common case: Brian remembers it, no paperwork trail needed).
- **`hypothetical_example`** — explicitly framed in the text as illustrative, never asserted as something that happened at AEBP.
- **`unverified`** — anything not yet confirmed. This is the required default whenever a reviewer cannot establish which of the other three applies.

**Rule, enforced structurally in `automation/schemas/review.schema.json`, not just stated here:** neither Claude nor ChatGPT may mark a claim `owner_verified`. Only a human reviewer can. This is the direct, checkable answer to the post-8006 incident: an AI reviewer inferring that a plausible-sounding claim is probably true is exactly the failure `GATE-ANECDOTE-INTEGRITY` exists to catch, and "the reviewer found it convincing" was never a valid basis for that gate even when the rule lived only in prose. A claim left `unverified` blocks `GATE-ANECDOTE-INTEGRITY` the same way an uncited legal claim blocks `GATE-LEGAL-ACCURACY` — it is not a lesser finding.

## AUTO-DISPOSITION — every finding gets an answer, on the record

Every finding in a `review.schema.json` artifact must receive a corresponding entry in the next `revision-response.schema.json` artifact's `dispositions` array: `accepted`, `accepted_with_modification`, `rejected`, or `requires_human`, each with a required `rationale`. A finding with no disposition is treated as unresolved and blocks moving to the next review round.

This exists so a disagreement between Claude and ChatGPT is a recorded decision, not a silent one — "GPT flagged X, Claude rejected it because Y" is now something Brian (or a future reviewer) can read back six months later, instead of only being visible if Brian happened to be watching both conversations at the time. `requires_human` is not a failure state — it's the correct disposition whenever the finding turns on something only Brian can settle (most commonly, a `claim_provenance` question), and `requires_human_review: true` at the top of the artifact is what actually gates whether Brian needs to step in before the loop continues.

## AUTO-VERSIONING — what every artifact records, and why

An audit trail that says "GPT flagged three things, Claude fixed two" is much less useful six months from now than one that also says which version of the standards, which git commit of the repo, and which revision of the WordPress draft were actually in view when that happened — otherwise there's no way to tell whether a later re-review is checking the same rules or a since-changed one. Every artifact records:

- `schema_version` — of the JSON schema itself, not of `docs/01`–`03`.
- `docs_versions` — the specific version string of each `docs/*` file (and the `reviews/*` manifest, if applicable) the review was actually run against.
- `repo.commit` and `repo.state` — the local git HEAD SHA at review time, plus whether the working tree was clean, had uncommitted changes, or was ahead of `origin/main` at that moment. This repo's own history has already shown why `state` matters: a prior review was run against a local copy whose latest commits hadn't been pushed yet, and the reviewer's comments about "missing" files that already existed were a direct symptom of that (see `CHANGELOG.md`, 2026-07-07 night entry, "Discrepancy worth flagging"). Recording `state` doesn't prevent that from happening again, but it makes it diagnosable after the fact instead of a mystery.
- `wordpress` — the post ID, revision ID or `modified_gmt`, status, and permalink, so a reviewer or an auditor can find exactly what was reviewed. See `AUTO-NO-DUPLICATION` for why this is a reference, not a copy.
- `reviewer` and `timestamp` — who (or which model) produced the artifact, and when.

## AUTO-NO-DUPLICATION — reference the post, don't copy it

`reviews/posts/<post-id>/*.json` files record findings, dispositions, and the WordPress post's identifying reference (ID, revision, permalink) — they do not embed the full post body. WordPress's own revision history is the system of record for post content; duplicating it into the repo risks the two silently diverging and bloats the repo with content that has nothing to do with editorial standards. The one exception is `quote` / `quote_before` / `quote_after` fields on individual findings and dispositions, which are meant to carry the specific flagged passage — consistent with `docs/03` `FIND-STRUCTURE`'s existing instruction to quote the finding, not summarize it. A full-post snapshot belongs in the artifact only if there's a concrete reason (for example, the post is deleted or heavily rewritten later and the exact reviewed text needs to be recoverable) — not by default.

## AUTO-HUMAN-GATE — automation never replaces Brian reading the draft

Nothing in this document, or in any Phase 2 built on it later, changes the fact that Brian reads the actual final draft before it publishes — not a JSON summary, not a "PASS" status line. `revision-response.schema.json`'s `summary` field exists to give Brian a fast orientation to what happened in a round (which findings, which dispositions), the same way the original automation proposal's "Post 9050 review complete... Ready for Brian" message would — but it is documented here explicitly as a convenience for triage, never as a substitute for the full-content review this repo's content already requires given how much of it is legal/compliance-adjacent. If a future Phase 2 is ever built, this gate does not shrink to "human reviews only what got flagged."

## AUTO-AGENT-FILES — if agent prompt files are ever built, they stay thin

If `/agents/*.md` files (a Claude drafter prompt, a GPT reviewer prompt, etc.) are built for a future Phase 2, they must not restate any rule defined in `docs/01`–`03` or this document — they should load those documents at run time and defer to them entirely. This repo has already hit the cost of the alternative once: the packaged Cowork skill for the Monday cornerstone post silently drifted out of sync with this repo's own `skills/monday-cornerstone.md` because an edit only touched a temporary copy (see `CHANGELOG.md`, 2026-07-14). An `/agents/` folder is a second and third place the same drift could recur — once between `/agents/*.md` and `docs/`, and again between `/agents/*.md` and whatever Cowork skill or ChatGPT custom-instruction happens to also encode review behavior. This document does not create `/agents/*.md` files; it only binds them in advance, before they exist, so they aren't drafted as freestanding prompts later.

## Status

v0.1 — drafted 2026-09-08, not yet run against a real post. Validate against the next real Monday cornerstone or Thursday Tip review cycle — specifically, confirm the `claim_provenance` field actually catches an anecdote the way `GATE-ANECDOTE-INTEGRITY` was designed to, and confirm `dispositions` holds up when ChatGPT and Claude genuinely disagree about a finding — before calling this v1.0. Phase 2 (API/GitHub Action orchestration) is not scoped by this document beyond the sketch in `AUTO-PHASING` and is not authorized to be built from this version.
