---
title: Change of Property Manager — Tenant Notice, Security Deposit Handoff, and Trust Fund Duties
doc_type: informative
owner: Brian
last_verified: 2026-07-18
next_review: n/a (no cyclical figure here — re-check only if Civil Code §1962, §1950.5, or Bus. & Prof. Code §10145 are amended)
review_frequency: as-changed
authority: Statute
confidence: Mixed — see per-claim confidence below
review_method: Manual, cross-checked against primary source (FindLaw mirror of Civil Code, since leginfo.legislature.ca.gov is JS-rendered and returns empty content on a static fetch — same known tooling gap logged for the Richmond rent page in knowledge/laws/rent-caps.md)
source:
  - https://codes.findlaw.com/ca/civil-code/civ-sect-1962/
  - https://codes.findlaw.com/ca/civil-code/civ-sect-1950-5/
  - https://codes.findlaw.com/ca/business-and-professions-code/bpc-sect-10145/
  - https://dre.ca.gov/files/pdf/re13.pdf
---

# Change of Property Manager — Tenant Notice, Security Deposit Handoff, and Trust Fund Duties

Existed for one reason: WordPress post 8342 ("How to Switch Property Managers in California Without Losing a Tenant or Violating Your Lease") cited Civil Code §1962 and §1950.5 from secondary-source summaries (WebSearch results) rather than primary statute text, and — more seriously — mis-cited §1950.5 as the authority for a security deposit transferring between property *managers* when the statute's transfer provisions actually govern a change of *ownership*. Caught during a Pre-Publish Audit review requested 2026-07-18. See `tests/legal/TEST-LEGAL-004.md` for the full incident.

## Civil Code §1962 — tenant notice of a change in manager

**Confidence: Level 1 (required by law) — confirmed against primary text.** Full text retrieved via FindLaw's mirror of the statute (leginfo.legislature.ca.gov itself returned empty content on a static fetch — treat this as a known tooling gap, not evidence against the citation, consistent with the Richmond rent-page precedent in `rent-caps.md`).

- **§1962(a)** requires an owner (or the owner's agent) to disclose, in the lease/rental agreement: (1) the name, phone, and street address of whoever is authorized to manage the premises, and of whoever is authorized to accept service of process and receive/receipt notices and demands on the owner's behalf; (2) the name, phone, and address of who rent is paid to, including the usual days/hours available **if rent may be paid in person** (this conditional matters — see "Scope limit" below); (3) the accepted form(s) of rent payment; (4) a copy of the lease within 15 days of execution.
- **§1962(c)** is the specific change-of-manager provision: "The information required by this section shall be kept current and this section shall extend to and be enforceable against any successor owner or manager, who shall comply with this section within 15 days of succeeding the previous owner or manager." It then states the consequence directly: **"A successor owner or manager shall not serve a notice pursuant to paragraph (2) of Section 1161 of the Code of Civil Procedure or otherwise evict a tenant for nonpayment of rent that accrued during the period of noncompliance by a successor owner or manager with this subdivision."** This confirms, verbatim from the statute (not a secondary paraphrase), the claim in post 8342 that a landlord who misses the 15-day window can lose the ability to serve a pay-or-quit notice for rent that came due during the gap. No case citation is needed for this — it's the statute's own text, not a judicial interpretation of ambiguous language.
- **Scope limit worth stating in content:** the "usual days and hours" disclosure in §1962(a)(2)(A) is only triggered **if rent payments may be made personally** (in-person). A management company that only accepts rent by check/ACH/online portal (not in-person cash) doesn't need to disclose specific hours under this subsection — worth knowing before flagging a welcome-letter template as incomplete for omitting exact hours.

## Civil Code §1950.5 — what it actually governs, and what it doesn't

**Confidence: Level 1 (required by law) for what's below — confirmed against primary text.** This is the security deposit statute, but its "successor in interest" transfer provisions (subdivisions (i)–(k)) are **narrower than they're often assumed to be**:

- §1950.5(i) triggers "Upon termination of the **landlord's interest** in the premises, whether by sale, assignment, death, appointment of receiver, or otherwise" — this is about a change of **ownership**, not a change of managing agent. When it applies, the landlord (or their agent) must either transfer the remaining deposit to the landlord's successor in interest (with tenant notice of the transfer, any deductions, the amount, and the successor's contact info) or return it directly to the tenant with an accounting.
- §1950.5(j)–(k) extend obligations to that same "successor in interest" (a new owner) — not to a newly-hired property manager acting for the same, unchanged owner.
- **What this means for a same-owner PM switch:** if an owner simply hires a new management company while keeping title to the property, §1950.5's transfer provisions do not directly govern the outgoing manager's handoff of deposit funds to the owner or the new manager. The owner's *interest* in the property never terminated — only the management agreement did.

**Do not cite §1950.5 as the authority for "the outgoing property manager must transfer the deposit with an itemized statement" in a same-owner PM-switch scenario.** That claim needs a different citation (below). §1950.5 remains the correct citation for deposit-limit, permitted-use, and itemized-statement-to-tenant rules generally — just not for the manager-to-manager handoff specifically.

## Business & Professions Code §10145 — the actual authority for the PM-to-PM/PM-to-owner handoff

**Confidence: Level 1 (required by law) — confirmed against primary text.** A real estate broker (which a licensed property manager must be, or work under, per Bus. & Prof. Code §10131) who accepts funds belonging to others — including a tenant's security deposit — must deposit those funds into a broker trust fund account within three business days of receipt, and "all funds deposited by the broker in a trust fund account shall be maintained there until disbursed by the broker in accordance with instructions from the person entitled to the funds." The broker must also maintain a separate record of receipt and disposition of trust funds. This is the correct statutory basis for: when a management agreement ends, the outgoing broker/property manager has a legal obligation to account for and disburse (to the owner, or per the owner's instruction directly to a new manager's trust account) any trust funds — including a tenant's security deposit — they were holding. It is a trust-fund-handling duty under the broker's own license, not a §1950.5 "successor in interest" event.

## Currency note

No cyclical figure lives in this file. Re-verify only if Civil Code §1962, §1950.5, or Business & Professions Code §10145 are amended, or if a specific published case addressing §1962(c) compliance as a prerequisite to an unlawful detainer action is later identified and should be added (currently Type C — see "Not yet closed" below).

## Not yet closed

The general practitioner claim that "§1962 compliance is a jurisdictional prerequisite to an unlawful detainer action" (found via secondary legal-commentary sources during drafting) is well-supported by the statute's own text in §1962(c) — no case citation is actually needed since the consequence is spelled out directly in the statute — but if a specific case interpreting this provision is ever needed for a stronger claim, it hasn't been identified yet. Low priority: the statutory text alone is Level 1 and sufficient.
