---
agent: layer-intro-author
invoked_at: 2026-06-07T154422Z
scope: L2 index — firm-count prose ↔ dep-map row-count reconcile (D5, WAVE-2, dep D4)
status: integrated
integrated_at: 2026-06-07T180000Z
integration_commit: acf65f6
integration_notes: "Applied clean (D5, WAVE-2 dep D4). L2/index prose firm-count reconciled to the post-D4 self-summing dep-map row count: 17 firm + 1 partly-constructive = 18 rows (per-report integrator's independent landed-tree firm-row count = 17, matches D5's post-D4 arithmetic). The 2 stale growth-log standing-count claims annotated as-of-cycle + forwarded; the frozen cycle-042 snapshot left untouched. The D4->D5 serial sequencing HELD. cargo make book EXIT 0; no rank/edge change. No OQ."
---

# CYCLE: L2 index firm-count reconcile

## Summary

`book/src/L2/index.md` carries three prose firm-count statements that have drifted from the
actual self-summing dep-map row count. As the single **count-owner** for this reconcile
(anti-drift mechanism `index-table-status-cell-drifts-when-theme-file-promoted`), I recompute
the count from the authoritative on-disk dep-map rows (surveyed by their trailing `## Status`
cell, NOT the prose), account for the landed RE6 / matrix-free changes AND D4's two pending
deletions (this cycle), and reconcile the stale prose. **I touch PROSE COUNTS ONLY** — D4 owns
the row strikes for `dot`/`nrm2`; I do not touch those rows.

## Arithmetic (explicit, so the integrator can verify after D4 lands)

**On-disk dep-map rows NOW (the authoritative self-summing enumeration, surveyed by each row's
trailing status cell):**

| # | slug | status |
|---|---|---|
| 1 | chebyshev-iteration | firm |
| 2 | correction_step | firm |
| 3 | krylov-step | firm |
| 4 | gram | firm |
| 5 | inner_product | firm |
| 6 | linear_combination | firm |
| 7 | **dot** | firm | ← **D4 strikes** |
| 8 | **nrm2** | firm | ← **D4 strikes** |
| 9 | deflate | **partly-constructive** |
| 10 | eigsolve | firm |
| 11 | incremental-least-squares | firm |
| 12 | ksp_solve | firm |
| 13 | orthogonalize | firm |
| 14 | assemble-diagonal | firm |
| 15 | divfree-projector | firm |
| 16 | elementwise_product | firm |
| 17 | jacobi-smoother | firm |
| 18 | normalize | firm |
| 19 | reciprocal | firm |
| 20 | matrix-free-operator-apply | firm |

- **Firm rows on-disk now: 19.** Partly-constructive: **1** (`deflate`). Total: **20 rows.**
- **D4 strikes 2 firm rows** (`dot` :117, `nrm2` :118 — confirmed in D4's report §7 / inbound
  inventory: "STRIKE the row").
- **Final firm rows = 19 − 2 = 17.** Partly-constructive unchanged = **1**. **Total = 18 rows.**

**Count-evolution trace (reconciles the historical growth-log claims):** cycle-043 end was
`21 firm + 1 pc = 22 rows`; then RE6 (cycle-124) deleted the 4 `linear_combination` arity
leaves (`scal`/`axpy`/`axpby`/`axpbypcz`) → 17 firm; `correction_step` landed firm (cycle-122)
→ 18 firm; `matrix-free-operator-apply` landed firm (cycle-125) → 19 firm; cycle-127 D4 deletes
the 2 `inner_product` reduce-family stubs (`dot`/`nrm2`) → **17 firm + 1 pc = 18 rows**.
(`21 − 4 + 1 + 1 − 2 = 17` firm; matches the on-disk-minus-D4 enumeration above.)

## Proposed changes

### 1. Line ~95 — the authoritative current-state count line

```edit:book/src/L2/index.md
[old]: line: 23 firm + 1 `partly-constructive` (`deflate`).
[new]: line: 17 firm + 1 `partly-constructive` (`deflate`) = 18 dep-map rows (self-summing — count the rows below).
```

### 2. Line ~168 — the cycle-043 growth-log "dep-map now 22 rows" standing claim

The cycle-043 delta narration (`firm 17 → 21`) is a frozen historical record and stays; only
the trailing **standing-count** claim "dep-map now 22 rows = 21 firm + 1 partly-constructive"
is stale (pre-RE6 / pre-matrix-free / pre-cycle-127). Annotate it as the as-of-cycle-043
snapshot and forward to the current total.

```edit:book/src/L2/index.md
[old]: dep-map now 22 rows = 21 firm + 1 partly-constructive
[new]: dep-map 22 rows = 21 firm + 1 partly-constructive **as of cycle-043** (since revised: RE6 cycle-124 deleted the 4 `linear_combination` arity leaves, `correction_step` firm cycle-122 + `matrix-free-operator-apply` firm cycle-125 added 2, and cycle-127 D4 deleted the 2 `inner_product` reduce-family stubs `dot`/`nrm2` → **current 17 firm + 1 partly-constructive = 18 rows**; see :95)
```

### 3. Line ~171 — the cycle-052 "count is UNCHANGED (… = 22 rows)" standing claim

The cycle-052 point was that reduce-to-stub kept the files on disk so the count was unchanged
**at that time**. RE6 (cycle-124) and cycle-127 D4 have since DELETED those very stubs, so the
"unchanged = 22 rows" standing claim is now stale. Correct the standing total and note the
later eliminations.

```edit:book/src/L2/index.md
[old]: **The count is UNCHANGED** — reduce-to-stub keeps every file on disk (no delete), so all inbound links stay live and the dep-map row count is unchanged (21 firm + 1 partly-constructive = 22 rows).
[new]: **The count was UNCHANGED at cycle-052** — reduce-to-stub kept every file on disk (no delete), so all inbound links stayed live and the dep-map row count held at 21 firm + 1 partly-constructive = 22 rows **at that time**. (Since SUPERSEDED by deletion: the 4 `linear_combination` arity stubs `scal`/`axpy`/`axpby`/`axpbypcz` were eliminated cycle-124 (RE6) and the 2 `inner_product` reduce-family stubs `dot`/`nrm2` cycle-127 (D4), each folded into its combinator's §Specializations / §Consumer; with `correction_step` (c122) + `matrix-free-operator-apply` (c125) added, the **current count is 17 firm + 1 partly-constructive = 18 rows** — see :95.)
```

### NOT reconciled (deliberately left as frozen historical snapshots)

- **Line ~167** ("Cycle-042 … firm 12 → 17 … dep-map now 18 rows = 17 firm + 1
  partly-constructive") — a past-tense cycle-042 growth-log snapshot, clearly cycle-prefixed.
  Its numbers (18 rows / 17 firm / 1) are a frozen record of the cycle-042 state; they
  coincidentally equal today's total but the line is unambiguously historical (it reads
  "firm 12 → 17"), so I leave it intact rather than rewrite a frozen delta. (Reconciling :95
  + :168 + :171 covers the standing-count surfaces; :167 is not a standing-count claim.)

## Supporting evidence

- On-disk dep-map enumeration (the authoritative self-summing rows, surveyed by trailing
  `## Status` cell, NOT by prose): `book/src/L2/index.md:101-103` (Step kernels),
  `:109-111` (Fold combinators), `:117-118` (`dot`/`nrm2` stubs — **D4 strikes**),
  `:124-128` (Named compositions), `:134-139` (Elementwise & gate floors),
  `:145` (Constructive-kernel compositions). 19 firm + 1 partly-constructive = 20 rows now.
- D4 report (`reports/2026-06-07T153840Z-combinator-miner-inner-product-refactor/CYCLE.md`)
  §7 + §"Inbound-link inventory": "STRIKE" of `L2/index.md:117` (`dot` row) and `:118`
  (`nrm2` row); confirms exactly the 2 L2 rows it deletes. D4 §"Open questions / caveats"
  explicitly hands the count reconcile to D5 ("D5 owns the count prose, D4 owns the row
  strikes").
- RE6 (cycle-124) deleted the 4 `linear_combination` arity leaves; `matrix-free-operator-apply`
  added cycle-125 D2; `correction_step` firm cycle-122 — all reflected in the on-disk rows.

## Open questions / caveats

- **D5↔D4 ordering dependency.** My three prose edits are computed AS-IF D4's 2 row deletions
  have applied. The integrator must apply D4 (the row strikes) and D5 (these prose counts) in
  the same cycle for the prose to match the table; the planner sequenced D5 WAVE-2 after D4 for
  exactly this. If D4 does NOT land this cycle, these counts will read 2-high vs the table
  (defer D5 with D4 in that case). The arithmetic above states both the pre-D4 (19 firm) and
  post-D4 (17 firm) totals so the integrator can verify either way.
- I touched **prose counts only** — no dep-map rows, no status cells, no `dot`/`nrm2` row text
  (D4 owns those). No new SUMMARY/edge changes.
