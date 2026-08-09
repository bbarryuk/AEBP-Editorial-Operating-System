---
title: Portfolio Performance Data — Vacancy, Turnover, and Oakland Rent (Trailing 12 Months, Aug 2025–Jul 2026)
doc_type: informative
owner: Brian
last_verified: 2026-08-09
next_review: 2026-11-09
review_frequency: quarterly, or whenever a fresh AppFolio export is pulled for a new content piece
authority: Internal
confidence: AEBP documented experience (source-hierarchy level 6 — see docs/02-Evidence-and-Sourcing.md, EVD-SOURCE-HIERARCHY)
review_method: Computed directly from raw AppFolio export data; formulas and sample sizes documented below so any figure can be independently reproduced
source:
  - AppFolio Vacancy Tracker export (Detail, Rent Roll, Tickler, Turns tabs), exported 2026-08-05
---

# Portfolio Performance Data — Vacancy, Turnover, and Oakland Rent

Existed for one reason: post 8801 ("Should You Raise Rent at Renewal or Keep This Tenant?") cited AEBP-specific portfolio figures — 79 completed turnovers, a 37.8-day average turnover cycle, 149 occupied Oakland units, and a $2,263 average Oakland rent — that satisfy `EVD-ANECDOTE-INTEGRITY`'s requirement for a confirmed-real, source-hierarchy-level-6 claim, but had no canonical file in `/knowledge` to check them against. Per that same rule ("use a real, confirmed example... ask Brian if one exists before inventing one"), this file is the durable record so the numbers can be reused in future content (video, social, AI answers, ROI posts) without re-deriving them from the raw export each time, and so a reviewer can verify the claim rather than taking it on faith.

## Reporting window and scope

- **Period:** trailing 12 months, August 1, 2025 – July 31, 2026.
- **Data source:** AEBP's AppFolio system, exported as a "Vacancy Tracker" workbook with four raw-data tabs (Detail, Rent Roll, Tickler, Turns) plus a formula-driven Dashboard tab. The Dashboard's formulas were not cached at the time of analysis (the workbook had not been reopened in Excel to recalculate), so all figures below were computed directly from the raw Tickler (tenant move-in/move-out event log) and Rent Roll tabs, replicating the same turn-pairing logic the workbook's own Turns-tab formulas use.
- **Extraction date:** workbook exported 2026-08-05 (11:13–11:15 PM per the export's own timestamp); figures computed and verified 2026-08-09.

## Methodology

**Turnover pairing:** for each Unit ID with a "Move-out" event in the Tickler log, the next "Move-in" event for that same Unit ID with a later date is matched as the corresponding move-in. Days Vacant = (next move-in date − move-out date). A turn with no subsequent move-in in the data window is excluded from "completed turns" (it would be an open/"Still Vacant" turn, not a completed cycle) — this matches the AppFolio workbook's own Turns-tab formula logic (`Turns` tab, columns G–I).

**Portfolio-wide turnover cycle:** all completed turns (Move-out matched to a later Move-in for the same unit) across the full portfolio, regardless of city, within the trailing-12-month window.

- Completed turns: **79**
- Average Days Vacant (move-out to move-in): **37.8 days**

This is a different measurement than the "25–30 days average to lease" figure in `knowledge/company/overview.md` — that figure measures how long a unit sits actively listed once a listing is live (days-on-market). The 37.8-day figure measures the full cycle: move-out, make-ready (cleaning, repairs, photography), listing, showings, screening, and move-in. Both are correct; they answer different questions and should not be treated as conflicting or interchangeable in future content. Post 8801 includes a reader-facing note making this same distinction.

**Oakland-specific turnover cycle (for reference; not the figure used in post 8801's headline math, which used the portfolio-wide number to avoid overstating precision on a smaller sample):**

- Completed Oakland turns: **17**
- Average Days Vacant, Oakland units: **45.4 days**

Flagged here because it's a real, computed figure, but 17 completed turns in one city in one year is a modest sample — future content citing an Oakland-specific turnover-duration figure should note the sample size, the same way this file does, rather than presenting it with the same confidence as the 79-turn portfolio-wide figure.

**Average Oakland rent:** mean of the current `Rent` field (Rent Roll tab) across all occupied Oakland units (property address contains "Oakland"), as of the export date (2026-08-05, "as of" date on the Rent Roll tab).

- Occupied Oakland units: **149**
- Average current rent: **$2,262.56/mo** (rounded to $2,263 in reader-facing content)
- Average market rent (for reference, not used in post 8801): $2,354.55/mo

**Portfolio-wide average rent (for reference):** 605 occupied units across the full portfolio, average current rent $2,436.39/mo.

## Derived figures used in post 8801

All derived from the base figures above; reproducible by anyone with this file.

| Figure | Calculation | Result |
|---|---|---|
| Daily rent value, avg. Oakland unit | $2,263 ÷ 30 | $75.42/day |
| Cost of one average turnover, Oakland unit | 37.8 days × $75.42/day | ~$2,851 |
| Monthly gain, Oakland 2.3% RAP increase | $2,263 × 2.3% | $52.05/mo |
| Annual gain, Oakland 2.3% RAP increase | $52.05 × 12 | ~$624/yr |
| Years to recoup one turnover at Oakland's 2.3% increase | $2,851 ÷ $624 | ~4.6 years |
| Monthly gain, Berkeley 1.0% AGA increase | $2,263 × 1.0% | $22.63/mo |
| Annual gain, Berkeley 1.0% AGA increase | $22.63 × 12 | ~$272/yr |
| Years to recoup one turnover at Berkeley's 1.0% increase | $2,851 ÷ $272 | ~10.5 years |
| Expected-value break-even (Oakland) — turnover-probability increase required | $624 ÷ $2,851 | ~21.9%, i.e. ~22 percentage points |

Rent-cap percentages (2.3% Oakland RAP, 1.0% Berkeley AGA) are sourced from `knowledge/laws/rent-caps.md`, not this file — this file supplies only the portfolio-derived inputs (rent, vacancy days, turnover cost).

## Known limitations

1. **Oakland sample size (n=17 completed turns)** is real but modest — treat any Oakland-specific turnover-duration claim (as opposed to the portfolio-wide 79-turn figure) as directionally useful, not statistically precise, and say so in reader-facing content.
2. **The Dashboard tab's own formulas were not cached** at analysis time — if the workbook is reopened in Excel and recalculated, its Dashboard figures should match the numbers in this file; if they don't, re-derive from the raw tabs using the methodology above rather than trusting either source blindly, and update this file.
3. **This is a snapshot, not a live figure.** Re-pull and recompute before reusing these numbers in content published after `next_review` above, the same currency discipline `EVD-CURRENCY-CHECK` requires for cyclical legal figures.

## Reuse note

Any future post, video script, social copy, or AI-search answer that cites AEBP's own turnover timing, vacancy cost, or Oakland rent average should link back to this file (or the reader-facing post that already cites it) rather than restating the numbers from memory — same discipline `knowledge/laws/rent-caps.md` established for rate figures.
