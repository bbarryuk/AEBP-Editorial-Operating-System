# TEST-LEGAL-008 — Oakland RAP Notice attachment dropped; unreconciled banking-expiration rule promoted to verified

**Date:** 2026-10-30
**Caught by:** ChatGPT final review 03 of post 10268 (Nov 2, 2026 Monday cornerstone, "Oakland and Berkeley Rent Increases for 2027"), findings 10268-F03 (regression) and 10268-F09.
**Type:** Type A (Content Error) + Type C (System Gap)

## Finding A — a required notice duty was deleted while adding a different notice prerequisite

Responding to 01-review finding 10268-F03, Claude added Oakland's six-month RAP Notice prerequisite and registration-at-service check, and in the same edit removed the existing bullet "Include the City's Rent Adjustment Program notice with the increase notice," reasoning it was unverified and that the six-month rule "covers notice." Both were wrong. OMC §8.22.070H.1 and H.4 require every rent increase notice to include notice of the Chapter and the tenant's right to petition, in the RAP-prescribed form, and H.6 invalidates an increase without it. The six-month prerequisite is a separate, additional condition.

**Rule this tests:** when adding a new prerequisite to an eligibility checklist, never delete an existing, independently applicable duty unless a source shows it no longer applies. "Not re-verified this round" is a reason to verify, not to delete; the ordinance snapshot in `knowledge/sources/` was available.

## Finding B — an agency summary was promoted over the ordinance without reconciliation

In the same round, Claude promoted a "ten years for pre-2026 accruals, five years after" banking-expiration rule to Level 1 in `knowledge/laws/rent-caps.md` and published it in post 10268's Key Facts table, based on a WebFetch summary of Oakland's 5/28/26 info sheet. The ordinance snapshot (§8.22.070B.5.c) says five years with no grandfather. The conflict was not checked.

**Rule this tests:** a new agency summary must be reconciled against the saved ordinance text (EVD-SOURCE-SNAPSHOTS) before a claim is promoted to verified. A tool-generated summary of a PDF is not a full read of the PDF. When the two conflict, publish the conservative general statement and log the conflict as unresolved.

## Fix

- Post 10268: RAP Notice bullet restored as a separate item ("Include a copy of the City's RAP Notice with every rent increase notice."); banking-expiration Key Facts row removed; body sentence replaced with "Banked CPI increases are subject to expiration and other eligibility limits. Check Oakland's current banking rules before including older amounts," linked to the City's allowable-increases page. Sources line cites OMC §8.22.070.
- `knowledge/laws/rent-caps.md`: the 10-year/5-year claim marked UNRESOLVED with a do-not-cite instruction; §8.22.070H attachment duty recorded.

## Pass criteria for a future draft

1. Any Oakland rent-increase checklist includes the RAP Notice attachment duty alongside (not replaced by) the six-month prerequisite and registration check.
2. No published Oakland content states a specific banking-expiration window until `rent-caps.md` marks the conflict resolved with a controlling citation.
