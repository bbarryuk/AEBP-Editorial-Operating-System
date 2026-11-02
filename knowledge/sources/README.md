---
title: Primary Source Texts — Statutes, Bills, Ordinances, Regulations
doc_type: informative
owner: Brian
last_verified: 2026-11-02
next_review: 2027-01-05
review_frequency: quarterly, plus every January 1 and whenever a local ordinance is amended
authority: Statute / Local Ordinance / Agency guidance (per file)
confidence: Verbatim snapshots — accurate to the version saved, not guaranteed current
review_method: Manual; re-save each file from its official URL and update manifest.json
source:
  - See the Official URL in each file header and in manifest.json
---

# Primary Source Texts

Verbatim text of the statutes, bills, ordinances and regulations that `knowledge/laws/*.md` and published posts rely on. They are here so Claude, ChatGPT and human reviewers can quote the actual section during drafting and review without leaving the repo.

## Rules for using these files

- **A snapshot is not the live law.** Draft and review from these files, but verify any claim against the Official URL before publishing. See `EVD-SOURCE-SNAPSHOTS` in `docs/02-Evidence-and-Sourcing.md`.
- **Cite the code section for current law, not the bill.** Files under `state/bills/` show what a bill changed. Cite `state/statutes/` for what the law says now.
- **This folder is canonical.** When you re-save a law, save it here, update its header and `manifest.json`, and bump `last_verified`. The original PDFs stay in the OneDrive `bill-texts` folder; the `.txt` copies there are superseded by these files.
- **Public domain only.** This repo is public. Law-firm summaries and other copyrighted material (for example the Bornstein cheat sheets) stay in OneDrive and do not go here.
- **OCR files need a second look.** Files marked OCR were read from a scanned PDF. Check numbers and section symbols against the original before quoting.

Each file starts with a header (title, jurisdiction, source type and `EVD-SOURCE-HIERARCHY` level, official URL, version, dates, notes), then `=== BEGIN VERBATIM TEXT ===`. `manifest.json` holds the same data in machine-readable form.

## Open items

- **URLs marked "to confirm"** need the exact deep link added (Oakland Municode articles, Berkeley regulations and deposit-interest pages, HUD FMR page, Alameda County ordinance and report).
- **Oakland OMC 8.22 Art. V** was saved from a version labeled 2020-07-21. Confirm it matches current Municode.
- **AB 2025** — the saved text has no bill header. Confirm the bill number and chapter before citing.
- **CCP 415.20** — the file holds both the current version and the AB 747 version that takes effect 2027-01-01.
- **Not yet saved:** sections cited in `knowledge/laws` but missing here — Civ. Code 1945 and 1962, B&P 10145, and Emeryville Ch. 3-1 (business taxes).
- **Current code text not yet saved** for sections added or amended by the 2026-11-02 bills: Civ. Code 1941.8, 1941.9 and 1942.8, and Pen. Code 396 (as amended by SB 1365, operative 2027-01-01). Until they are, quote the bill files and cite the code section.
- **SB 1365** contains two versions of Pen. Code 396 (Sec. 1 and Sec. 1.5, which adds "war" and applies only if SB 493 was also enacted and SB 1365 was enacted after it). Confirm which one is in the code before quoting.
- **2026-11-02 additions:** the OneDrive originals are CRLF; these copies are LF. AB 1414 and SB 610 match the original byte counts exactly after line-ending conversion. SB 1365 is 4 bytes short of the original (39,032 bytes) after conversion, which points to a whitespace-only difference. Re-save from the official URL if an exact copy matters.

## California — statutes (current code text)

| File | Title | Level | Version | Saved | URL |
|---|---|---|---|---|---|
| `state/statutes/civ-1940.2.txt` | Civil Code § 1940.2 — Landlord prohibited conduct (influence tenant to vacate) | 1 | (Amended by Stats. 2017, Ch. 489, Sec. 3. (AB 291) Effective January 1, 2018.) | 2026-10-06 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1940.2.) |
| `state/statutes/civ-1941.txt` | Civil Code § 1941 — Landlord duty to make premises fit | 1 | (Amended by Code Amendments 1873-74, Ch. 612.) | 2026-09-26 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1941.) |
| `state/statutes/civ-1941.1.txt` | Civil Code § 1941.1 — Untenantable dwelling standards | 1 | (Amended by Stats. 2025, Ch. 342, Sec. 1. (AB 628) Effective January 1, 2026.) | 2026-09-26 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1941.1.) |
| `state/statutes/civ-1942.txt` | Civil Code § 1942 — Tenant repair-and-deduct | 1 | (Amended by Stats. 1979, Ch. 307.) | 2026-09-26 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1942.) |
| `state/statutes/civ-1942.5.txt` | Civil Code § 1942.5 — Retaliation prohibited | 1 | (Amended (as amended by Stats. 2021, Ch. 2, Sec. 6) by Stats. 2021, Ch. 27, Sec. 5. (AB 832) Effective June… | 2026-10-06 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1942.5.) |
| `state/statutes/civ-1946.txt` | Civil Code § 1946 — Notice to terminate periodic tenancy | 1 | (Amended by Stats. 2024, Ch. 287, Sec. 1. (SB 611) Effective January 1, 2025.) | 2026-10-06 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1946.) |
| `state/statutes/civ-1946.1.txt` | Civil Code § 1946.1 — 60/30-day notice to terminate | 1 | (Amended by Stats. 2024, Ch. 1015, Sec. 3.5. (SB 1103) Effective January 1, 2025.) | 2026-10-06 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1946.1.) |
| `state/statutes/civ-1946.2.txt` | Civil Code § 1946.2 — Tenant Protection Act — just cause (AB 1482) | 1 | (Amended by Stats. 2025, Ch. 203, Sec. 1. (AB 1529) Effective January 1, 2026. Repealed as of January 1, 20… | 2026-09-26 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1946.2.) |
| `state/statutes/civ-1947.12.txt` | Civil Code § 1947.12 — Tenant Protection Act — rent cap (AB 1482) | 1 | (Repealed (in Sec. 3) and added by Stats. 2023, Ch. 290, Sec. 4. (SB 567) Effective January 1, 2024. Operat… | 2026-09-26 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1947.12.) |
| `state/statutes/civ-1950.5.txt` | Civil Code § 1950.5 — Security deposits | 1 | (Amended by Stats. 2025, Ch. 340, Sec. 1. (AB 414) Effective January 1, 2026.) | 2026-09-26 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1950.5.) |
| `state/statutes/civ-1951.3.txt` | Civil Code § 1951.3 — Abandonment of leased property | 1 | (Amended by Stats. 2018, Ch. 104, Sec. 2. (AB 2847) Effective January 1, 2019.) | 2026-09-28 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1951.3.) |
| `state/statutes/civ-1954.txt` | Civil Code § 1954 — Landlord entry | 1 | (Amended by Stats. 2018, Ch. 445, Sec. 1. (SB 721) Effective January 1, 2019.) | 2026-10-14 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1954.) |
| `state/statutes/civ-789.3.txt` | Civil Code § 789.3 — Utility shutoff / lockout prohibited | 1 | (Amended by Stats. 1979, Ch. 333.) | 2026-10-06 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=789.3.) |
| `state/statutes/civ-827.txt` | Civil Code § 827 — Notice of rent increase / change in terms | 1 | (Amended by Stats. 2024, Ch. 1015, Sec. 1. (SB 1103) Effective January 1, 2025.) | 2026-09-26 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=827.) |
| `state/statutes/ccp-1013.txt` | Code of Civil Procedure § 1013 — Service by mail — time extensions | 1 | (Amended by Stats. 2022, Ch. 686, Sec. 2. (AB 1726) Effective January 1, 2023.) | 2026-09-28 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1013.) |
| `state/statutes/ccp-1161.txt` | Code of Civil Procedure § 1161 — Unlawful detainer — grounds and notices | 1 | (Amended (as added by Stats. 2020, Ch. 37, Sec. 16) by Stats. 2024, Ch. 287, Sec. 6. (SB 611) Effective Jan… | 2026-09-26 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1161.) |
| `state/statutes/ccp-1162.txt` | Code of Civil Procedure § 1162 — Service of notices | 1 | (Amended by Stats. 2010, Ch. 144, Sec. 1. (AB 1263) Effective January 1, 2011.) | 2026-09-26 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1162.) |
| `state/statutes/ccp-1167.txt` | Code of Civil Procedure § 1167 — UD summons and response time | 1 | (Amended by Stats. 2024, Ch. 512, Sec. 1. (AB 2347) Effective January 1, 2025.) | 2026-09-28 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1167.) |
| `state/statutes/ccp-1179a.txt` | Code of Civil Procedure § 1179a — UD calendar preference | 1 | (Added by Stats. 1931, Ch. 885.) | 2026-09-26 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=1179a.) |
| `state/statutes/ccp-415.20.txt` | Code of Civil Procedure § 415.20 — Substituted service of summons | 1 | Two versions (current through 2026-12-31; AB 747 version from 2027-01-01) — see text | 2026-10-06 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=415.20.) |
| `state/statutes/gov-12927.txt` | Government Code § 12927 — FEHA housing definitions | 1 | (Amended by Stats. 2019, Ch. 601, Sec. 4.3. (SB 222) Effective January 1, 2020.) | 2026-10-06 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=12927.) |
| `state/statutes/gov-12955.txt` | Government Code § 12955 — FEHA housing discrimination prohibited | 1 | (Amended by Stats. 2023, Ch. 776, Sec. 1. (SB 267) Effective January 1, 2024.) | 2026-10-06 | [link](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=12955.) |
| `state/statutes/civ-1954.50-1954.535.txt` | Civil Code §§ 1954.50–1954.535 — Costa-Hawkins Rental Housing Act | 1 | Multiple sections — see each section's Stats. note in the text | 2026-10-06 | [link](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CIV&division=3.&title=5.&part=4.&chapter=2.7.) |

## California — chaptered bills (session law)

| File | Title | Level | Version | Saved | URL |
|---|---|---|---|---|---|
| `state/bills/ab-1414-2025-ch506.txt` | AB 1414 (2025) — Tenant opt-out of third-party internet subscriptions (Civ. 1942.8) | 1 | Chaptered, Stats. 2025 ch. 506 | 2026-11-02 | [link](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB1414) |
| `state/bills/ab-1815-2024-ch619.txt` | AB 1815 (2024) — Discrimination: hairstyles (CROWN Act expansion) | 1 | Chaptered, Stats. 2024 ch. 619 | 2026-10-06 | [link](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB1815) |
| `state/bills/ab-2025-2026.txt` | AB 2025 (2026) — B&P § 10140.8, digitally altered images in real estate ads | 1 | Dated 2026-09-27 in original filename; chapter number not in saved text | 2026-09-29 | [link](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB2025) |
| `state/bills/ab-2042-2026-ch379.txt` | AB 2042 (2026) — Setting aside default / default judgment | 1 | Chaptered, Stats. 2026 ch. 379 | 2026-09-29 | [link](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB2042) |
| `state/bills/ab-2347-2024-ch512.txt` | AB 2347 (2024) — UD procedural requirements (CCP 1167, 1170) | 1 | Chaptered, Stats. 2024 ch. 512 | 2026-10-06 | [link](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2347) |
| `state/bills/ab-246-2025-ch337.txt` | AB 246 (2025) — Social Security Tenant Protection Act (Civ. 1946.3) | 1 | Chaptered, Stats. 2025 ch. 337 | 2026-10-14 | [link](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB246) |
| `state/bills/ab-747-2025-ch563.txt` | AB 747 (2025) — Service of process (CCP 415.20 et al.) | 1 | Chaptered, Stats. 2025 ch. 563 | 2026-09-26 | [link](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB747) |
| `state/bills/sb-1137-2024-ch779.txt` | SB 1137 (2024) — Discrimination: intersectionality | 1 | Chaptered, Stats. 2024 ch. 779 | 2026-10-06 | [link](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB1137) |
| `state/bills/sb-1296-2026-ch1025.txt` | SB 1296 (2026) — Rentals: pet policy (Civ. 1942.7.5) | 1 | Chaptered, Stats. 2026 ch. 1025 | 2026-10-06 | [link](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB1296) |
| `state/bills/sb-1365-2026-ch1028.txt` | SB 1365 (2026) — Price gouging: rental housing of any lease length (Pen. Code 396) | 1 | Chaptered, Stats. 2026 ch. 1028 | 2026-11-02 | [link](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB1365) |
| `state/bills/sb-329-2019-ch600.txt` | SB 329 (2019) — Source-of-income discrimination | 1 | Chaptered, Stats. 2019 ch. 600 | 2026-10-06 | [link](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=201920200SB329) |
| `state/bills/sb-567-2023-ch290.txt` | SB 567 (2023) — No-fault just cause / rent cap amendments | 1 | Chaptered, Stats. 2023 ch. 290 | 2026-10-06 | [link](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB567) |
| `state/bills/sb-610-2025-ch547.txt` | SB 610 (2025) — Disaster assistance: tenants, mobilehome parks, mortgages (Civ. 1941.8, 1941.9, 798.64) | 1 | Chaptered, Stats. 2025 ch. 547 | 2026-11-02 | [link](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB610) |

## Federal

| File | Title | Level | Version | Saved | URL |
|---|---|---|---|---|---|
| `federal/hud-fmr-fy2027-oakland-fremont.txt` | HUD Fair Market Rents FY 2027 — Oakland-Fremont HUD Metro FMR Area | 3 | FY 2027 final | 2026-09-26 | [link](https://www.huduser.gov/portal/datasets/fmr.html) (to confirm) |

## Oakland

| File | Title | Level | Version | Saved | URL |
|---|---|---|---|---|---|
| `local/oakland/omc-5.04-business-tax.txt` | OMC Ch. 5.04 — Business taxes (incl. residential rental tax) | 2 | Saved 2026-10-06; Municode version date not recorded | 2026-10-06 | [link](https://library.municode.com/ca/oakland/codes/code_of_ordinances) (to confirm) |
| `local/oakland/omc-8.22-art1-rent-adjustment.txt` | OMC 8.22 Art. I — Residential Rent Adjustment Program | 2 | Municode version dated 2026-07-13 (per original filename) | 2026-09-26 | [link](https://library.municode.com/ca/oakland/codes/code_of_ordinances) (to confirm) |
| `local/oakland/omc-8.22-art2-just-cause.txt` | OMC 8.22 Art. II — Just Cause for Eviction (Measure EE) | 2 | Municode version dated 2026-07-13 (per original filename) | 2026-09-26 | [link](https://library.municode.com/ca/oakland/codes/code_of_ordinances) (to confirm) |
| `local/oakland/omc-8.22-art4-rent-program-fee.txt` | OMC 8.22 Art. IV — Rent Program Service Fee | 2 | Municode version dated 2026-07-13 (per original filename) | 2026-09-26 | [link](https://library.municode.com/ca/oakland/codes/code_of_ordinances) (to confirm) |
| `local/oakland/omc-8.22-art5-tenant-protection.txt` | OMC 8.22 Art. V — Tenant Protection Ordinance | 2 | Original filename date 2020-07-21 matches Ord. 13608 adoption; confirm against current Municode before citing | 2026-10-06 | [link](https://library.municode.com/ca/oakland/codes/code_of_ordinances) (to confirm) |
| `local/oakland/omc-8.22-art7-uniform-relocation.txt` | OMC 8.22 Art. VII — Uniform Residential Tenant Relocation | 2 | Municode version dated 2026-07-13 (per original filename) | 2026-09-28 | [link](https://library.municode.com/ca/oakland/codes/code_of_ordinances) (to confirm) |
| `local/oakland/omc-8.22-art8-omi-relocation.txt` | OMC 8.22 Art. VIII — Relocation payments for owner/relative move-ins | 2 | Municode version dated 2026-07-13 (per original filename) | 2026-09-28 | [link](https://library.municode.com/ca/oakland/codes/code_of_ordinances) (to confirm) |
| `local/oakland/omc-8.25-fair-chance-housing.txt` | OMC Ch. 8.25 — Fair Chance Access to Housing | 2 | Saved 2026-10-06; Municode version date not recorded | 2026-10-06 | [link](https://library.municode.com/ca/oakland/codes/code_of_ordinances) (to confirm) |

## Berkeley

| File | Title | Level | Version | Saved | URL |
|---|---|---|---|---|---|
| `local/berkeley/bmc-13.76-rent-stabilization-just-cause.txt` | BMC Ch. 13.76 — Rent Stabilization and Eviction for Just Cause | 2 | Includes Ord. 7950-NS (2024) amendments | 2026-09-26 | [link](https://berkeley.municipal.codes/BMC/13.76) |
| `local/berkeley/bmc-13.77-ellis-act-withdrawal.txt` | BMC Ch. 13.77 — Withdrawal of rental units (Ellis Act) | 2 |  | 2026-10-06 | [link](https://berkeley.municipal.codes/BMC/13.77) |
| `local/berkeley/regs-ch05-applicability.txt` | Berkeley Rent Board Regulations Ch. 5 — Applicability | 2 |  | 2026-10-06 | [link](https://rentboard.berkeleyca.gov/) (to confirm) |
| `local/berkeley/regs-ch12-individual-rent-adjustments.txt` | Berkeley Rent Board Regulations Ch. 12 — Individual Adjustments of Rent Ceilings | 2 |  | 2026-10-06 | [link](https://rentboard.berkeleyca.gov/) (to confirm) |
| `local/berkeley/guidance/2026-relocation-adjustment-staff-report.txt` | Berkeley Rent Board — 2026 inflationary adjustment of relocation payments (staff memo, Res. 25-28) | 3 | Memo dated 2025-10-16 | 2026-10-06 | [link](https://rentboard.berkeleyca.gov/elected-rent-board/news/2026-adjustments-relocation-assistance-payments) |
| `local/berkeley/guidance/security-deposit-interest.txt` | Berkeley Rent Board — Security deposit interest and calculator page | 3 |  | 2026-09-26 | [link](https://rentboard.berkeleyca.gov/) (to confirm) |

## Emeryville

| File | Title | Level | Version | Saved | URL |
|---|---|---|---|---|---|
| `local/emeryville/emc-5-40-landlord-tenant-relations.txt` | EMC Ch. 5-40 — Residential Landlord and Tenant Relations | 2 | eCode360, current through 2026-06-02 per knowledge/laws/emeryville-landlord-tenant.md | 2026-09-26 | [link](https://ecode360.com/46994531) |

## Richmond

| File | Title | Level | Version | Saved | URL |
|---|---|---|---|---|---|
| `local/richmond/rmc-11.100-fair-rent-just-cause.txt` | RMC Ch. 11.100 — Fair Rent, Just Cause for Eviction and Homeowner Protection | 2 | Municode version dated 2026-06-04 (per original filename) | 2026-09-26 | [link](https://library.municode.com/ca/richmond/codes/code_of_ordinances?nodeId=ARTXIPUSAWE_CH11.100FAREJUCAEVHOPR) |
| `local/richmond/guidance/rent-increase-aga-2026.txt` | Richmond Rent Program — Rent control and 2026 AGA page | 3 | 2026 AGA 1.5%, approved 2026-06-17 | 2026-09-26 | [link](https://www.ci.richmond.ca.us/3376/Rent-Increase) |

## Alameda County (unincorporated)

| File | Title | Level | Version | Saved | URL |
|---|---|---|---|---|---|
| `local/alameda-county/ord-o-2025-9-just-cause.txt` (OCR) | Alameda County Ord. O-2025-9 — Just cause for evictions, unincorporated areas (Ord. Code Ch. 3.70) | 2 |  | 2026-10-06 | [link](https://www.acgov.org/) (to confirm) |
| `local/alameda-county/guidance/2026-02-tenant-protections-staff-report.txt` | Alameda County CDA — Tenant protections staff report to Unincorporated Services Committee | 3 | Report dated 2026-02-25 | 2026-10-06 | [link](https://www.acgov.org/) (to confirm) |
