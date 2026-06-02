---
agent: layer-intro-author
invoked_at: 2026-06-02T061737Z
scope: L4 index prose refresh (fold_solve firmness-split + active-frontier re-state)
status: pending
integrated_at: 2026-06-02T061737Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-059 D2. Applied clean (3 surgical prose edits, prose-only). book/src/L4/index.md cohort refresh firm: Vocabulary-cohort header count 6->7 firm + batch-17 MAP/FOLD framing; fold_solve firm bullet inserted before solve_family; Active-frontier fold_solve thread-opener re-stated firm with a live ../L3/fold_solve.md link (kept LIVE — D1 co-landed it this cycle). The 6->7 corrects the lingering '6' to match the authoritative Firm-at-L4=7 tally (firm-flip landed c058). Resolves OQ fold-solve-l4-index-vocabulary-cohort-firmness-split-refresh. citecheck --scan 9 ok / 4 AMBIG (ALL NON-BLOCKING, NOT landed — report-narrative bare-basename status-reads + intra-document self-refs; landed prose carries ZERO AMBIG citations). Build cargo make book exit 0; no build-repair needed."
---

# CYCLE: L4 index cohort refresh

## Summary

PROSE-ONLY surgical refresh of `book/src/L4/index.md`, resolving OQ
`fold-solve-l4-index-vocabulary-cohort-firmness-split-refresh`. Three stale prose
loci are brought current with the cycle-058 D1 landing of firm
`book/src/L4/fold_solve.md` (state-threaded FOLD outer-driver) and the cycle-059 D1
landing of its L3 image:

1. **§Vocabulary cohort header (line ~32)** — re-stated to register `fold_solve` as
   the SECOND solver-driven firm L4 combinator (the state-threaded FOLD sibling of
   `solve_family`'s independent MAP; both are §3.7 `iterate_while`-family children per
   the batch-17 two-combinator MAP/FOLD ratification, NO third parent abstraction).
   Firm-cohort count updated **6 → 7** firm operators.
2. **§Vocabulary cohort firm-list (line ~40 block)** — added a `fold_solve` firm bullet
   alongside `solve_family` (the rough-in bullet at ~line 50 is unchanged; `solve_family`
   remains `rough-in (test-coverage-bounded)`).
3. **§Active frontier (line ~62)** — the `fold_solve` / `time_step_fold` rough-in
   thread-opener bullet re-stated as firm (cycle-058 D1), noting its L3 image landed
   this cycle (cycle-059 D1, `partial-obstruction`) with a live-link to
   `../L3/fold_solve.md`.

**Count discipline (c057-meta count-owner guard):** firm count registered from each
linked chapter's on-disk `## Status` line, NOT from index cells. Verified:
`fold_solve.md:157` = `firm` (firm-on-positive-structure escape, 2 fold witnesses);
`solve_family.md:144` = `rough-in (test-coverage-bounded)`. Firm L4 operator cohort =
**7** (krylov-step, iterate-while, iterate-while-with-prev, chebyshev, ksp_solve,
eigsolve, fold_solve) + 4 outer-driver vocabulary anchors (solve_loop, restart_cycle,
Outcome, EigOutcome); rough-in = 1 (solve_family).

The dep-map TABLE row for `fold_solve` (line ~82) is ALREADY firm and is NOT re-touched.

## Proposed changes

```edit:book/src/L4/index.md
[old]: **Firm at L4 (6 + 4 outer-driver)** — UNCHANGED this cycle (cycle-055 added one *rough-in* combinator, `solve_family`, not a firm entry): the typed-wrapper Krylov step kernel, the two value-threading loop combinators that drive it, the fixed-degree polynomial smoother, and (cycle-048) the two iterative-solve outer-driver **caps** (`ksp_solve`, `eigsolve`); plus the four `solve-monad` outer-driver vocabulary anchors:
[new]: **Firm at L4 (7 + 4 outer-driver)** — `fold_solve` joined the firm cohort cycle-058 (the SECOND solver-driven firm L4 combinator after `solve_family`'s rough-in): the typed-wrapper Krylov step kernel, the two value-threading loop combinators that drive it, the fixed-degree polynomial smoother, the two iterative-solve outer-driver **caps** (`ksp_solve`, `eigsolve`; cycle-048), and the state-threaded **fold** outer-driver `fold_solve` (cycle-058); plus the four `solve-monad` outer-driver vocabulary anchors. The two solver-driven combinators `solve_family` (independent **MAP** over an RHS family) and `fold_solve` (state-threaded **FOLD** over a time/sweep schedule) are the two children of the strawman §3.7 [`iterate-while`](./iterate-while.md) family — a map is the degenerate fold whose step ignores the accumulator — per the batch-17 two-combinator MAP/FOLD ratification; there is **no third parent abstraction** above them (the §3.7 `iterate_while` family IS the shared parent):
```

```edit:book/src/L4/index.md
[old]: - [`solve_family`](./solve_family.md) — the fixed-operator **map-over-RHS-family outer-driver combinator**: capture the system operator once (`SetOperators(*K,*K)` hoisted outside the loop), build the solver once, map the [`ksp_solve`](./ksp_solve.md) cap over a family of right-hand sides `[rhs_i]`, collect the solution family `[x_i]`. The **pure-`map` degenerate** of the strawman §3.7 [`iterate-while`](./iterate-while.md) family (each element independent, no carry; the trajectory IS the collected family — reusing the firm iterate-while vocabulary, the [`chebyshev`](./chebyshev.md) route). Sits one shell *above* the [`ksp_solve`](./ksp_solve.md) cap (`solve_loop` iterate-whiles over inner cycles; `solve_family` maps over an independent RHS family). Load-bearing law: the **concatenation-homomorphism** `solve_family op (a ++ b) = solve_family op a ++ solve_family op b`, licensed by the **operator-capture-once / `SetOperators`-hoist** identity. Status `rough-in (test-coverage-bounded)` (structure firm; laws stated against strawman §3.7 but test-unconfirmed). **Scope: fixed-operator ONLY (2-of-5 pipelines** — electrostatic + magnetostatic; the driven pipeline breaks shared-operator-capture, `drivensolver.cpp:176-180`, and is the `per-element` superset `map_solve_over_(operator,rhs)_family`, batch-17-gated). Harvested cycle-055 D1 from the c054 combinator-miner mine.
[new]: - [`fold_solve`](./fold_solve.md) — the state-threaded **fold-over-schedule outer-driver combinator**: capture the system operator once (the L4 typing of `TimeOperator` built outside the loop), seed the carry `s0` once, thread the persistent field-state through a schedule by `foldl`, advancing one opaque per-step operator (`time_step_op`) at a time where **each step's input is the prior step's output** (sequential — the carry-threading cannot reorder). The **non-degenerate carry-threading member** of the strawman §3.7 [`iterate-while`](./iterate-while.md) family — the fold-sibling of `solve_family`'s independent map. Load-bearing **non**-law: no commutativity/distribution across the schedule (prior-output-is-next-input); load-bearing law: the schedule-split `fold_solve op s0 (a ++ b) = fold_solve op (fold_solve op s0 a) b`, read off `foldl (a++b) = foldl b . foldl a`. Status `firm` (firm-on-positive-structure escape: every fold-spine law is a read-off syntactic identity on **two** positive driver loops — transient `transientsolver.cpp:33-99` + `timeoperator.cpp:312,410`, and driven-PROM SweepAdaptive `drivensolver.cpp:231-398`). **Scope: the 2 state-threaded pipelines** (transient + driven-PROM SweepAdaptive); electrostatic + magnetostatic are the independent-map `solve_family` (no carry), eigenmode opaque.
- [`solve_family`](./solve_family.md) — the fixed-operator **map-over-RHS-family outer-driver combinator**: capture the system operator once (`SetOperators(*K,*K)` hoisted outside the loop), build the solver once, map the [`ksp_solve`](./ksp_solve.md) cap over a family of right-hand sides `[rhs_i]`, collect the solution family `[x_i]`. The **pure-`map` degenerate** of the strawman §3.7 [`iterate-while`](./iterate-while.md) family (each element independent, no carry; the trajectory IS the collected family — reusing the firm iterate-while vocabulary, the [`chebyshev`](./chebyshev.md) route). Sits one shell *above* the [`ksp_solve`](./ksp_solve.md) cap (`solve_loop` iterate-whiles over inner cycles; `solve_family` maps over an independent RHS family). Load-bearing law: the **concatenation-homomorphism** `solve_family op (a ++ b) = solve_family op a ++ solve_family op b`, licensed by the **operator-capture-once / `SetOperators`-hoist** identity. Status `rough-in (test-coverage-bounded)` (structure firm; laws stated against strawman §3.7 but test-unconfirmed). **Scope: fixed-operator ONLY (2-of-5 pipelines** — electrostatic + magnetostatic; the driven pipeline breaks shared-operator-capture, `drivensolver.cpp:176-180`, and is the `per-element` superset `map_solve_over_(operator,rhs)_family`, batch-17-gated). Harvested cycle-055 D1 from the c054 combinator-miner mine.
```

```edit:book/src/L4/index.md
[old]: - `fold_solve` / `time_step_fold` *(rough-in thread-opener; cycle-057 D4)* — the transient pipeline's **state-threaded fold** outer-driver, the fold-counterpart of [`solve_family`](./solve_family.md)'s independent map. Distilled from the transient driver's persistent-`sol`-threading time sweep (`transientsolver.cpp:93` → `timeoperator.cpp:410` `ode->Step(sol, t, dt)` advances `sol` in place, each step's input = the prior step's output → a genuine `foldl`, NOT a `map`). This **answers the `index.md:61` fold-vs-map question for transient: fold** — so transient does NOT join the `solve_family` map family (it is the §3.7 carry-threading sibling). Held at rough-in (1 witness; per-step body is an opaque MFEM `ODESolver` step — the `eigsolve` opaque-library shape). The shared parent of `solve_family` (map) + `fold_solve` (fold) is the strawman §3.7 `iterate_while` family itself; no third parent abstraction is warranted (OQ for the batch-17 meta-phase). Thread continues across batch-18; promotion gated on a 2nd fold-witness (the cycle-056 D1 `SweepAdaptive` PROM candidate) or a downstream transient pull.
[new]: - [`fold_solve`](./fold_solve.md) *(firm; cycle-058 D1)* — the **state-threaded fold** outer-driver, the fold-counterpart of [`solve_family`](./solve_family.md)'s independent map. Distilled from the transient driver's persistent-`sol`-threading time sweep (`transientsolver.cpp:93` → `timeoperator.cpp:410` `ode->Step(sol, t, dt)` advances `sol` in place, each step's input = the prior step's output → a genuine `foldl`, NOT a `map`) **plus** the driven-PROM SweepAdaptive greedy sweep (`drivensolver.cpp:231-398`) — the 2nd fold-witness that closed the cycle-057-D4 promotion gate. This **answers the fold-vs-map question for the state-threaded pipelines: fold** — so transient does NOT join the `solve_family` map family (it is the §3.7 carry-threading sibling). Promoted firm cycle-058 D1 on the firm-on-positive-structure escape (every fold-spine law is a read-off syntactic identity on the two positive driver loops; the per-step body's opacity is recorded at the lowering layer, not as an unconfirmed law). Its **L3 image landed this cycle** ([`L3/fold_solve`](../L3/fold_solve.md), cycle-059 D1, status `partial-obstruction` — the carry-threading + opaque per-step body resist the iteration rotation while the per-step body lifts, the `chebyshev`/`eigsolve` shape), via the substantive L4>L3 theme [`fold-solve-time-step-dissolution`](../L4-L3/fold-solve-time-step-dissolution.md). The shared parent of `solve_family` (map) + `fold_solve` (fold) is the strawman §3.7 `iterate_while` family itself; **no third parent abstraction is warranted** (batch-17 two-combinator MAP/FOLD ratification). Open generalization: the `schedule-source` variant axis (fixed-list ⊂ state-generated greedy) — OQ `fold-solve-greedy-schedule-source-generalization`.
```

## Supporting evidence

- L4 firm operator chapters (each `## Status` read on-disk):
  - `book/src/L4/krylov-step.md` — `firm`
  - `book/src/L4/iterate-while.md` — `firm`
  - `book/src/L4/iterate-while-with-prev.md` — `firm`
  - `book/src/L4/chebyshev.md` — `firm`
  - `book/src/L4/ksp_solve.md` — `firm`
  - `book/src/L4/eigsolve.md` — `firm`
  - `book/src/L4/fold_solve.md:157` — `firm` (firm-on-positive-structure escape; 2 fold witnesses: transient `transientsolver.cpp:33-99` + `timeoperator.cpp:312,410`, driven-PROM SweepAdaptive `drivensolver.cpp:231-398`)
- Rough-in: `book/src/L4/solve_family.md:144` — `rough-in (test-coverage-bounded)` (unchanged this cycle)
- Firm L4 operator count = **7**; outer-driver vocabulary anchors = 4 (solve_loop / restart_cycle / Outcome / EigOutcome, unchanged); rough-in = 1 (solve_family, unchanged).
- L3 image of `fold_solve` lands this cycle (cycle-059 D1, `book/src/L3/fold_solve.md`, status `partial-obstruction`) — live-link valid post finalize-rebuild (D1 applies before rebuild this cycle).
- The dep-map TABLE row at `index.md:82` for `fold_solve` is already firm (authored cycle-058); not re-touched per dispatch instruction.

## Open questions / caveats

- The L3 `fold_solve` live-link (`../L3/fold_solve.md`) is valid only because D1 lands the file this same cycle before finalize-rebuild. If D1's per-report apply is reordered to AFTER finalize, `linkcheck2` would fail this link — the integrator should apply D1 before D2 (or before finalize-rebuild), per the dispatch dependency this CYCLE.md declares. (Standard same-cycle co-landing; flagging for ordering only.)
- `fold_solve.md:144` solve_family status text was confirmed `rough-in (test-coverage-bounded)`; left unchanged — the rough-in bullet at index.md ~line 50 and the §Active frontier solve_family bullet at ~line 61 are NOT part of this refresh (out of scope; they remain accurate).
- The `schedule-source` generalization (fixed-list vs state-generated greedy) and a possible dedicated greedy-schedule chapter remain open (OQ `fold-solve-greedy-schedule-source-generalization`) — carried forward in the refreshed §Active frontier bullet; not resolved here.
