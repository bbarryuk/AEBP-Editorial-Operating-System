# TEST-LEGAL-009 — PDF text extraction hid strikethrough; a deleted ballot provision was published as law

**Date:** 2026-11-05
**Caught by:** Brian (ChatGPT-assisted document check), the day after post 10268 was updated with the Measure X result.
**Type:** Type A (Content Error) + Type C (System Gap)

## Finding

On 2026-11-04 Claude updated live post 10268, Law Library entry 9403 and `knowledge/laws/rent-caps.md` to say Berkeley's Measure X "requires a written Golden Duplex exemption notice for tenancies that start on or after December 1, 2027." The source was the July 7, 2026 council packet, read through `pdftotext`. That packet contained the proposal with strikethrough formatting (removed by the Lunaparra revision, Supplemental Packet 2), but plain-text extraction drops strikethrough, so the deleted paragraph read as operative. The official Measure X full text has no such requirement. The same extraction also carried a draft "lower state limit" clause into the 10% cap description; the final §13.76.110(F) doesn't include it.

## Rule this tests

1. For a ballot measure, cite the City's **official full text as submitted to voters**, never council agenda packets or staff summaries, which contain superseded and struck drafts.
2. Plain-text PDF extraction is not a reliable read of legislative redlines. Struck text and inserted text merge (visible symptoms: doubled words like "A Rrental", "July 1 the due date"). Where a document uses strikethrough or underline to show changes, inspect the rendered PDF pages, or use a clean final version.
3. When more than one version of a measure exists, name which one is final before drafting (the Nov 4 plan update flagged the June 30 / July 7 ambiguity but the live post was edited before resolving it).

## Fix

- Post 10268, Law Library 9403, rent-caps.md and the November plan corrected 2026-11-05 to the official full text: 10% AGA-based cap (§13.76.110(F)), exemption-after-tenancy rule (§13.76.050(D)), September 30 registration deadline from 2027 (§13.76.080(G)); Golden Duplex notice claim removed.

## Pass criteria

A future ballot-measure post cites the official full text, with section numbers, and contains no provision that appears only in a superseded or struck draft.
