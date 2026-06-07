---
agent: combinator-miner
invoked_at: 2026-06-07T130000Z
scope: cycle-125 D3 — GMG/hygiene bundle (stale-path fix + V-cycle combinator audit + GMG-smoother L3-home audit)
status: integrated
integrated_at: 2026-06-07T124519Z
integration_commit: dca60b0fe398230a33421863a30b2608e41bce69
integration_notes: "cycle-125 D3 (batch-40 MIDDLE). Applied clean by integrator-per-report (staging row 3, after D1+D2); no gate hits. GMG cross-ref hygiene: multigrid-relaxation-smoother.md:113 re-pointed last stale design/l4_calculus.md §1.2.2 → live semantics/index.md §1.2.1 (double-correction path AND section); STALE-PATH SWEEP COMPLETE (grep design/l4_calculus book/src = 0, was 1; OQ batch-37-era-stale-design-l4-calculus-path-drift-sweep flagged for meta CLOSE). Two NEGATIVE-finding records (V-cycle do-not-mine; GMG-smoother-L3-home already-covered). rank_violations 0. Build EXIT 0, no finalize build-repair."
---

# CYCLE: GMG/hygiene bundle — last stale path + V-cycle combinator verdict + GMG-smoother L3-home verdict

## Summary

Three disjoint genuinely-open picks from the cycle-125 plan D3 entry. **(a)** The last
batch-37-era stale `book/src/design/l4_calculus.md` path reference (at
`book/src/L1/multigrid-relaxation-smoother.md:113`) is re-pointed to the live semantic
surface — and the section number is corrected: the "reserve `Tensor[N]` for genuinely-flat
rank-1 dof-vectors" rule lives at `semantics/index.md` **§1.2.1** (Named shape groups,
line 85), NOT §1.2.2 (which is "Operator shapes"). **(b)** The GMG V-cycle level-recursive
structure is a **NEGATIVE finding** — it has exactly ONE source instance in Palace
(`gmg.cpp:172` `VCycle`), failing both the ≥3-same-shape bar and the ≥2-sibling-family bar;
the OQ's speculated AMG / auxiliary-space recurrences do not bear out (AMG is opaque HYPRE;
the Hiptmair aux-space smoother is a flat single-level `pc_it` sweep). Mining it would be
mine-and-strand. The existing in-line GMG-column presentation is the correct disposition.
**(c)** The GMG outer `pc_it` smoother sweep is **ALREADY COVERED** — it is dispositioned as
the consumer's `iterate_while` fold around the `correction_step` body
(`L2/correction_step.md:47-53`), and its L3 iteration-view partial-obstruction home already
exists as `L3/chebyshev.md` (which explicitly names "the outer `pc_it` Richardson sweep" as
its partial-obstruction marker). No new L3 home is warranted. D3 reduces to picks (a)+(b)
on the artifact (one path edit + one negative finding recorded); (c) is a confirmed
no-author audit result.

## Pick (a) — last stale-path fix

### Evidence

- The stale reference: `book/src/L1/multigrid-relaxation-smoother.md:112-114`:
  > `Tensor[N]` is the genuinely-flat rank-1 dof-vector at L1, per
  > `book/src/design/l4_calculus.md` §1.2.2 "reserve `Tensor[N]` for genuinely-flat rank-1
  > dof-vectors at L1/L0"
- `grep -rn 'design/l4_calculus' book/src/` → **1 hit**, this line (c124 D3/D4 fixed the four
  libCEED-substrate-op instances; this batch-37-era file was the residual).
- The live surface: `book/src/semantics/index.md` exists. The reserved-`Tensor[N]` rule is at
  **§1.2.1** (`semantics/index.md:73` header "Named shape groups"; the rule text at
  `semantics/index.md:85`: *"reserve `Tensor[N]` for genuinely rank-1 vectors (e.g. a flat
  dof-vector of length `N`)"*). The original `§1.2.2` citation was ALSO wrong: `§1.2.2`
  (`semantics/index.md:87`) is "Operator shapes — domain and range groups", not the
  rank-1-reservation rule. **The re-point fixes BOTH path and section.**
- Convention match: the c124 sibling fixes use the inline-code form
  `` `book/src/semantics/index.md` §1.2.1 `` (`L1/element_restrict.md:55`,
  `L1/geom_factor_build.md:52`). The fix matches that form exactly.

### Proposed change

```edit:book/src/L1/multigrid-relaxation-smoother.md
- rank-1 dof-vector at L1, per `book/src/design/l4_calculus.md` §1.2.2 "reserve
+ rank-1 dof-vector at L1, per `book/src/semantics/index.md` §1.2.1 "reserve
```

(Single-line substring replacement on the line currently reading
`rank-1 dof-vector at L1, per `` `book/src/design/l4_calculus.md` `` §1.2.2 "reserve` — the
trailing `` `Tensor[N]` for genuinely-flat rank-1`` text on line 114 is unchanged and
accurate.) Closes the residual of OQ
`batch-37-era-stale-design-l4-calculus-path-drift-sweep` (the `design/l4_calculus` count
drops 1→0 across all of `book/src/`).

## Pick (b) — V-cycle level-recursive combinator: NEGATIVE finding (do NOT mine)

### Verdict

The GMG V-cycle's level-recursive `restrict → recurse → prolong-add` structure is a
genuinely interesting recursion shape (a balanced two-pass recursive descent over the
level-stack — distinct in *shape* from the flat tail-recursive folds `iterate-while` /
`fold_solve`), BUT it **fails the instance bar** and is **already correctly dispositioned
in-line**. Recommendation: **do NOT mine a new combinator; close the OQ as a negative
finding.**

### Pattern-instance count (the dispositive evidence)

The level-recursive cycle pattern occurs in **exactly ONE place** in Palace:

- Instance 1 (the only one): `palace/linalg/gmg.cpp:172-205` — `GeometricMultigridSolver::VCycle(int l, bool initial_guess)`:
  ```
  if (l == 0) { B[0]->Mult(X[0], Y[0]); return; }     // base case: coarse solve
  B[l]->Mult2(X[l], Y[l], R[l]);                        // pre-smooth
  A[l]->Mult(Y[l], R[l]); linalg::AXPBY(1, X[l], -1, R[l]);   // residual r = x − A y
  RealMultTranspose(*P[l-1], R[l], X[l-1]);             // restrict  Pᵀ r
  VCycle(l - 1, false);                                 // RECURSE to coarser level
  RealMult(*P[l-1], Y[l-1], R[l]); Y[l] += R[l];        // prolong-add  y += P e
  B[l]->MultTranspose2(X[l], Y[l], R[l]);               // post-smooth
  ```
  driven by the outer fixed-count wrapper `gmg.cpp:137-140`
  `for (it < pc_it) VCycle(n_levels-1, it>0)`.

`mcp__palace-codemap__search_text 'VCycle|recursi|Cycle\('` over `palace/linalg/*.cpp`
returns only the three `gmg.cpp` hits (139 / 172 / 196) plus two `iterative.cpp` hits that
are **log-message strings** ("from the recursion formula …" — Chebyshev recursion-formula
diagnostic text at `iterative.cpp:599` / `:778`), NOT structural recursion.

### Why the OQ's speculated recurrences do not bear out

The OQ `vcycle-level-recursive-combinator-mining-candidate` speculated the pattern "recurs
in AMG / auxiliary-space transfers." Checked against Palace source — it does not:
- **AMG**: Palace has no Palace-authored algebraic-multigrid level recursion; BoomerAMG is
  HYPRE (opaque-library boundary) and is never a Palace-owned level-recursive cycle.
- **Auxiliary-space (Hiptmair) transfer**: `palace/linalg/distrelaxation.cpp:97-118`
  (`DistRelaxationSmoother::Mult2`) is a **flat single-level** `for (it < pc_it)` sweep —
  primary-space `correction_step` then a gradient-space `G B_G Gᵀ` correction. NO level
  recursion; it is one smoother that the GMG V-cycle *calls* at a level, not a second
  level-recursive cycle.

So the recurrence is genuinely 1×. The combinator-miner same-shape bar is ≥3 (2 borderline);
the parametric-family bar is ≥2 siblings sharing a stateable law. One instance meets neither.

### Why mining would be mine-and-strand (redirect re-mandate)

Even setting aside the instance count, the project has **already dispositioned** this
recursion correctly, twice, as the consumer's iteration rather than a new vocabulary op:
- `book/src/L2/correction_step.md:47-53` states verbatim: *"The outer `pc_it` smoothing
  sweep / the V-cycle recursion are the **consumer's** `iterate_while` fold
  (`distrelaxation.cpp:102`; `gmg.cpp:172` `VCycle`), NOT folded into this kernel —
  `correction_step` is the per-sweep body, the fold is the driver above it (the same
  kernel-plus-driver split `krylov-step` (kernel) / L4 `iterate_while` (driver)
  establishes)."*
- `book/src/feature/geometric-multigrid-preconditioner.L4.md:66-82` presents `vcycle ps bs
  b0 l` in-line and explicitly annotates it: *"the V-cycle itself is a level-recursive
  combinator (NOT a new vocabulary op; the recursion structure read off
  gmg.cpp:172-205)."* The per-level smooth + coarse-grid leg already names the firm
  `L2/correction_step` combinator (`B = B[l]` for the smooth, `B = P·(recursive V-cycle
  solve)·Pᵀ` for the coarse-grid leg, via `correction_step` law 6 with `T = P`).

The pieces of the V-cycle that ARE recurrent — the per-level smooth body and the coarse-grid
correction — are **already first-class** (`L2/correction_step`, firm c122). What remains
(the level-stack descent wiring) is a one-off composition expressed cleanly in terms of that
firm combinator plus the prolongation operators (`fe_space_hierarchy`'s `P[l]`). Naming a
`vcycle`/`level_recurse` combinator from a single site would create a stranded operator with
exactly one consumer and no propagation target — precisely the mine-and-strand the
2026-06-01 redirect re-mandate forbids.

### Over-unification guard (recorded for completeness)

Were a second genuine level-recursive cycle ever to surface (a Palace-authored AMG V-cycle,
or a W-cycle / full-multigrid variant with ≥2 recursive calls per level), the unifying
combinator would be a **hylomorphism over the level-stack** (`unfold`-restrict ∘
recurse ∘ `fold`-prolong), and it must NOT be subsumed into `fold_solve`/`iterate-while`:
those are flat *linear* folds (single carry, one tail call), whereas the V-cycle does work on
BOTH the down-leg (restrict, pre-smooth) and the up-leg (prolong-add, post-smooth) of the
recursion — a balanced tree recursion, not a tail recursion. The flat-fold family is the
WRONG home for it. (This is the recorded re-open condition; no such second instance exists
today.)

### Proposed change

No artifact mutation for pick (b). Record the negative finding in the OQ ledger (the
integrator promotes Open questions):

- **Close** `vcycle-level-recursive-combinator-mining-candidate` as **negative finding —
  do-not-mine**: single source instance (`gmg.cpp:172`), speculated AMG/aux-space
  recurrences do not bear out, already correctly dispositioned in-line as the consumer's
  iteration over the firm `L2/correction_step` body. Re-open condition: a second
  Palace-authored level-recursive cycle (W-cycle / FMG / Palace-owned AMG) surfaces.

## Pick (c) — GMG-smoother L3 partial-obstruction home: ALREADY COVERED (do NOT author)

### Verdict

The GMG outer `pc_it` smoother-sweep does **NOT** need a new L3 partial-obstruction home.
Its iteration-view is already covered by the existing L3 cohort. Recommendation: **do NOT
author a redundant L3 chapter; record the coverage.**

### Coverage evidence (audit-first)

The `pc_it` sweep decomposes into a body + a loop, each with an existing home:

1. **The per-sweep body** (`y ← y + B(x − A y)`) is the firm L2 combinator
   `book/src/L2/correction_step.md` (firm c122). Its L3 iteration-views are the existing
   `book/src/L3/chebyshev.md` (polynomial `B`) and `book/src/L3/jacobi-smoother.md`
   (diagonal `B`).

2. **The outer `pc_it` loop** is ALREADY homed as a partial-obstruction at L3:
   `book/src/L3/chebyshev.md` is `firmness: partial-obstruction` and its scope text states
   verbatim: *"The per-inner-step surrounding loop structure (the inner `k`-recurrence of
   degree `order` and **the outer `pc_it` Richardson sweep**) is a witnessed sequential
   obstruction that at L3 is the canonical **partial-obstruction** case: the body lifts, the
   loop [does not]."* This is exactly the loop-doesn't-lift / body-does pattern the plan
   asked about — and it is the SAME `pc_it` outer loop (`gmg.cpp:137` and `chebyshev.cpp` /
   `distrelaxation.cpp:102` are the same fixed-count smoother-sweep idiom; `correction_step`
   cross-cites all three sites as one family).

3. The distributive (Hiptmair) variant adds only the gradient-space `G B_G Gᵀ` correction
   term (`distrelaxation.cpp:108-117`) — itself a second `correction_step` in the auxiliary
   space — inside the SAME flat `pc_it` loop. It introduces no new loop structure; it is two
   `correction_step` bodies under one already-homed sweep. The L1 home for the composite body
   already exists (`book/src/L1/multigrid-relaxation-smoother.md`, the file pick (a) fixes).

### Why no new L3 home is warranted (non-duplication)

A new `L3/gmg-vcycle-smoother` partial-obstruction chapter would duplicate
`L3/chebyshev.md`'s already-stated `pc_it`-sweep partial-obstruction with no distinct
un-liftable loop of its own: the body is `correction_step` (homed at L2; L3 views exist),
the loop is the `pc_it` sweep (homed as `L3/chebyshev`'s partial-obstruction), and the
level-recursion is pick (b)'s consumer-iteration (not a smoother sweep at all). There is no
residual un-homed loop. Authoring one would manufacture the redundant home the plan
explicitly told me to avoid.

### Proposed change

No artifact mutation for pick (c). (Optional, deferred to the integrator/meta as a
navigational nicety, NOT proposed as a D3 edit: the GMG column already cross-links
`L3/chebyshev` + `L2/jacobi-smoother` as the smoother iteration-views at
`feature/geometric-multigrid-preconditioner.L4.md:26-27`, so the coverage is already
navigable.)

## Proposed changes (consolidated)

Only pick (a) mutates the artifact:

```edit:book/src/L1/multigrid-relaxation-smoother.md
- rank-1 dof-vector at L1, per `book/src/design/l4_calculus.md` §1.2.2 "reserve
+ rank-1 dof-vector at L1, per `book/src/semantics/index.md` §1.2.1 "reserve
```

Picks (b) and (c) are recorded as Open-questions resolutions (no `book/` mutation):

- Close `vcycle-level-recursive-combinator-mining-candidate` — negative finding, do-not-mine
  (single instance; mine-and-strand; re-open on a second level-recursive cycle).
- Record `gmg-smoother-l3-partial-obstruction-home` audit result: already covered by
  `L3/chebyshev` (the `pc_it` sweep partial-obstruction) + `L2/correction_step` (the body) +
  `L3/jacobi-smoother` / `L3/chebyshev` (the L3 body-views); no new L3 home authored.

## Supporting evidence

- `book/src/L1/multigrid-relaxation-smoother.md:112-114` — the stale `design/l4_calculus.md`
  §1.2.2 reference (pick (a) target).
- `book/src/semantics/index.md:73` (header §1.2.1 "Named shape groups"), `:85` (the
  reserve-`Tensor[N]`-for-rank-1 rule), `:87` (header §1.2.2 "Operator shapes" — the wrong
  section the old citation named). Live target verified on disk.
- `book/src/L1/element_restrict.md:55`, `book/src/L1/geom_factor_build.md:52` — the c124
  sibling-fix convention (`` `book/src/semantics/index.md` §1.2.1 ``) matched by pick (a).
- `palace/linalg/gmg.cpp:124-141` (`Mult` outer `pc_it` loop), `:172-205` (`VCycle`
  level-recursion) — the sole V-cycle instance (pick (b)).
- `palace/linalg/distrelaxation.cpp:97-118` (`Mult2`) — flat single-level `pc_it` sweep, NOT
  a level recursion (pick (b) counter-evidence; pick (c) Hiptmair variant).
- `palace-codemap search_text 'VCycle|recursi|Cycle\(' palace/linalg/*.cpp` → only gmg.cpp
  structural hits + two iterative.cpp log-string false positives (pick (b) instance count).
- `book/src/L2/correction_step.md:47-53` — the existing disposition of the V-cycle recursion
  + `pc_it` sweep as the consumer's `iterate_while` fold, body = `correction_step` (picks
  (b)+(c)).
- `book/src/feature/geometric-multigrid-preconditioner.L4.md:56-82` — the in-line `vcycle`
  presentation already annotated "NOT a new vocabulary op" + naming `correction_step`
  (pick (b)).
- `book/src/L3/chebyshev.md` (frontmatter `firmness: partly-obstruction` [partial-obstruction];
  scope text naming "the outer `pc_it` Richardson sweep" as the partial-obstruction marker)
  — the existing L3 home for the `pc_it` sweep (pick (c)).
- `book/src/L3/jacobi-smoother.md` — the thinnest constructed-operator-gate L3 view of the
  diagonal-`B` smoother body, no sweep loop (pick (c) body-view).
- `book/src/L4/fold_solve.md` (frontmatter + signature `fold_solve op s0 schedule = foldl …`)
  + `book/src/L4/iterate-while.md` — the flat-tail-fold family the V-cycle is structurally
  distinct from (pick (b) over-unification guard).

## Open questions / caveats

- **Pick (a) double-correction**: the original citation was wrong on BOTH path (`design/`)
  and section (§1.2.2 vs the correct §1.2.1). I corrected both. If a reviewer prefers to
  preserve §1.2.2 verbatim (e.g. if the rule is expected to migrate back to a "Operator
  shapes" section later), flag — but §1.2.1 is where the reserve-`Tensor[N]` rule
  demonstrably is on disk today.
- **Pick (b) re-open condition is recorded, not enforced**: if a future cycle lifts a
  Palace-authored AMG / W-cycle / full-multigrid variant (none exists in the current tree),
  the level-stack hylomorphism becomes a genuine ≥2-instance candidate and the over-union
  guard above applies (do NOT fold into `fold_solve`/`iterate-while`). Surfaced so the
  negative close is not read as "never."
- **Pick (c) is a clean no-author**: the audit found full coverage. If the GMG column's
  smoother-leg story is ever felt to need its OWN L3 navigational stub (distinct from
  `L3/chebyshev`), that is a layer-intro-author navigational call, not a partial-obstruction
  home — flagged as deferred, not proposed.
- No `book/` mutation was performed by this dispatch (write-authority partition respected);
  the single edit is in the proposed-changes channel for `integrator-per-report`.
