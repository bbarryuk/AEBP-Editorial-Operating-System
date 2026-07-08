---
title: Evidence and Sourcing
doc_type: normative
version: 0.1 (Working Draft)
status: drafted, not yet validated against real posts
owner: Brian
last_updated: 2026-07-07
purpose: Defines what counts as sufficient evidence for a legal or procedural claim, in what priority, and when a claim must be blocked pending verification rather than published with a caveat.
used_by: [Claude, ChatGPT, human reviewer]
depends_on: []
referenced_by: [docs/01-Editorial-Standards.md, docs/03-Review-Format.md, skills/monday-cornerstone.md, skills/thursday-tip.md, skills/wwyd-social.md]
---

# Document 02 — Evidence and Sourcing

This document was split out of `docs/01-Editorial-Standards.md` (previously §5–6) once it became clear that almost everything AEBP publishes is fundamentally about California law and local compliance — evidence and sourcing rules deserve their own home rather than being one subsection of a broader standards document. If a rule here and a rule in `01` ever seem to disagree, this document wins on anything evidence/sourcing-related; `01` should be updated to match, not treated as a second authority.

## EVD-CITATION-REQUIREMENT — Every significant claim needs a source or a label

The strongest AEBP articles don't just make claims — they show why the claim is true. Instead of "professional carpet cleaning is often deductible," support it with the relevant California statute (if applicable), agency guidance, case law where appropriate, or AEBP's own lease language and practical experience.

**Rule:** every significant legal or procedural claim must be backed by an identifiable source, or clearly labeled as a best practice, company policy, or opinion — never presented as settled law when it isn't.

## EVD-SOURCE-HIERARCHY — Evidence priority

Not all sources carry equal weight. When multiple sources touch the same claim, prefer the higher one and disclose if they conflict:

1. California statute (e.g., Civil Code, Government Code)
2. Local ordinance (Oakland RAP/Measure V, Berkeley Rent Board, Richmond Fair Rent Act)
3. Government agency guidance (HUD, DRE, city rent board publications)
4. Court decisions / case law
5. Official agency FAQ or published interpretation
6. AEBP documented experience (a real, verifiable pattern across managed properties)
7. Industry best practice (NARPM guidance, common industry standard)
8. Professional opinion (a judgment call, explicitly labeled as such)

A claim sourced at level 6–8 must carry its Confidence Level label (below) so the reader and any downstream AI system can tell it apart from settled law.

## EVD-CONFIDENCE-LEVELS — Label every claim's certainty

- **Required by law** — a statute or state-level requirement
- **Required by local ordinance** — Oakland/Berkeley/Emeryville/Richmond-specific
- **Strongly recommended best practice** — not legally required, but advisable
- **Company policy** — how AEBP specifically operates, not a legal requirement
- **Professional opinion** — a judgment call, explicitly framed as such

This prevents a recommendation from reading as a legal mandate when it's actually a best practice, and is what makes `GATE-LEGAL-ACCURACY` and `GATE-LOCAL-ACCURACY` in `docs/01` checkable at all — a reviewer (human or AI) can verify each claim carries an accurate label rather than needing to independently re-derive the law each time.

## EVD-CURRENCY-CHECK — When a figure needs re-verification, not just citation

Some facts are not evergreen even when correctly sourced at the time of writing: rent cap percentages, HUD Fair Market Rents, security deposit limits, and similar figures change on fixed or semi-fixed cycles. A citation is not sufficient if the underlying figure has since changed.

**Rule:** before publishing any claim involving a number that updates on a cycle (annual rent cap adjustments, HUD FMR, statutory dollar limits), check `knowledge/company/overview.md` and `knowledge/llms.txt` for the `last_verified`/`next_review` dates. If the content depends on a figure past its review date, re-verify against the live source before publishing — don't rely on the cached knowledge file alone.

## EVD-UNCERTAINTY-HANDLING — When the law is genuinely unsettled

Some questions don't have a clean answer — a statute is ambiguous, a local ordinance and AB 1482 appear to conflict, or case law is mixed. In that situation:

- Say so explicitly rather than picking a side and presenting it as settled.
- Cite the competing authorities and explain the practical tension.
- Recommend professional consultation for the reader's specific situation — this is one of the required Quality Standard questions in `docs/01` (STD-QUALITY-QUESTIONS: "when should professional advice be sought").

## EVD-BLOCK-PENDING-VERIFICATION — When a draft should not proceed to publish

An article should be held, not published with a caveat, when:

- A load-bearing legal claim has no source above level 8 (opinion) and can't be labeled any more favorably.
- A cyclical figure (rent cap, FMR, deposit limit) is past its `next_review` date in `knowledge/` and hasn't been re-verified this session.
- Two authoritative sources appear to conflict and the piece hasn't resolved or disclosed the conflict (see `EVD-UNCERTAINTY-HANDLING`).

This is what makes `GATE-LEGAL-ACCURACY` in `docs/01` §10 an actual gate rather than a formality — if any of the above is true, say so to Brian and do not treat the draft as ready, regardless of how strong the rest of the article is.

## Status

v0.1 — drafted, not yet tested against a real post. The source hierarchy and block-pending-verification rule in particular should be checked against how a real ambiguous case (e.g., the Oakland/Berkeley rent-cap figures currently flagged as unreconciled in `knowledge/llms.txt`) actually gets handled, before this is considered stable.
