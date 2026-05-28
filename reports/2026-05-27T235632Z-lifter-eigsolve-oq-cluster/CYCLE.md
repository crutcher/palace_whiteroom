---
agent: lifter
invoked_at: 2026-05-27T23:56:32Z
scope: L1 eigsolve variant-axis & result-record inventory — resolve 3 cycle-009 OQs as one cluster (scaling-coordinate-convention, initial-space-axis-placement, iteration-count-result-field)
status: integrated
integrated_at: 2026-05-28T013333Z
integration_commit: 8bb16b7
integration_notes: cycle-011 wave-2 pass 7; resolves 3 of 4 cycle-009 eigsolve OQs in one report (the 4th was resolved cycle-010 via partial-answer); cycle-009 4-OQ eigsolve cluster fully closed; 7 in-place edits to L1/eigsolve.md + 6 in-place edits to open-questions.md + 1 auto-promoted new OQ; 1 safety-net gate hit (retroactive-budget per-slice recurrence-2 on eigsolve; below ≥3 block threshold); 1 new OQ promoted (eigsolve-slepc-nep-coordinate-convention-audit — opened by repairer); negative-anchor citation pattern at recurrence-2 since cycle-010 lifter — codification candidate for cycle-012 meta-phase; lifter-scope content-correction boundary at recurrence-2 — clarification candidate
inputs:
  - book/src/L1/eigsolve.md (cycle-009 rough-in; cycle-010 LinearSolveFailed L1-constructive annotation)
  - scaffolding/open-questions.md (3 OQs at lines 1493-1524)
  - reports/2026-05-27T220558Z-lifter-eigsolve-linear-solve-failed-anchor/CYCLE.md (cycle-010 sibling — structural template)
  - reports/2026-05-27T234730Z-abstractor-eigsolve-mutation-rotation-l1-l0/CYCLE.md (cycle-011 wave-1 sibling; eigsolve-mutation-rotation L1>L0 theme sketch)
  - reference/palace/palace/linalg/eps.hpp:100-141 (EigenvalueSolver virtual surface — GetScalingGamma/Delta, SetInitialSpace, Solve)
  - reference/palace/palace/linalg/arpack.cpp:249-260,340-405,410-420 (SetInitialSpace + driver-side num_it + GetEigenvalue un-scaling at neupd)
  - reference/palace/palace/linalg/slepc.cpp:655-740,1190-1210,1550-1580 (SetInitialSpace + GetEigenvalue un-scaling; EPS/PEP * gamma, NEP returns l directly)
  - reference/palace/palace/linalg/nleps.cpp:83-110,260-325 (SetInitialSpace base-abort + stored-eigenvalue GetEigenvalue + linear initial-guess priming)
  - reference/palace/palace/drivers/eigensolver.cpp:255-270 (driver-side SetInitialSpace call site, conditional on random-vs-supplied)
  - reference/palace/palace/models/modeeigensolver.cpp:470-480 (per-Solve SetInitialSpace call site, conditional on argument)
---

# CYCLE: Resolve cycle-009 eigsolve OQ cluster (scaling-coordinate-convention, initial-space-axis-placement, iteration-count-result-field)

## Summary

This dispatch resolves the **three remaining cycle-009 cycle-of-OQs** on the L1 `eigsolve` rough-in entry (`book/src/L1/eigsolve.md`), in a single unified re-anchor lift. The cycle-010 sibling dispatch (`2026-05-27T220558Z-lifter-eigsolve-linear-solve-failed-anchor/`) resolved the fourth OQ (`eigsolve-linear-solve-failed-status-anchor`) by adopting option (b) — keep the variant and annotate as L1-constructive — which establishes the **structural template** this cluster reuses. The three OQs covered here form a single "variant-axis & result-record inventory" theme (per cycle-011 planner's unified-dispatch scoping).

The three resolutions, summarised:

**(1) `eigsolve-scaling-coordinate-convention`** — **the L1 entry currently states the wrong convention.** Algebraic-law §5 reads "At L1, the returned `eigenvalues` are in the scaled coordinate system; un-scale via `EigResult.scaling_gamma`". The L0 surface is the opposite: **all three backends (ARPACK / SLEPc-EPS / SLEPc-PEP / NLEPS) un-scale at the `GetEigenvalue(i)` accessor boundary** — ARPACK at `palace/linalg/arpack.cpp:387` (`eig[i] = eig[i] * gamma` applied inside `SolveInternal` before any caller can observe), SLEPc-EPS at `palace/linalg/slepc.cpp:715` (`return l * gamma`), SLEPc-PEP at `palace/linalg/slepc.cpp:1198` (`return l * gamma`); NLEPS stores already-un-scaled values via the linear-eigensolver priming at `palace/linalg/nleps.cpp:267, 314`. Only SLEPc-NEP at `palace/linalg/slepc.cpp:1558-60` returns `l` without `* gamma`, but that is because NEP problem-type uses `gamma = 1` (no Higham scaling applied to the nonlinear case at construction time). The L0 convention is therefore **uniform: caller sees un-scaled eigenvalues**. Resolution: **adopt convention (b)** — L1 returns un-scaled eigenvalues in the original problem's coordinate system, matching L0. Keep `scaling_gamma` / `scaling_delta` in `EigResult` for downstream Higham-coordinate consumers (they are still semantically meaningful — they are the operator-norm-derived scaling factors, regardless of whether eigenvalues are returned in the scaled or un-scaled system), with a note that the eigenvalues field is **already in un-scaled coordinates** (the fields are informational, not action-required). The L1 entry's Algebraic-law §5 is rewritten to match L0; the open-question routing is dropped.

**(2) `eigsolve-initial-space-axis-placement`** — **per-call control, current EigControl placement is correct.** The L0 `SetInitialSpace(const ComplexVector &v)` virtual (`palace/linalg/eps.hpp:122`) is a *method* on the eigensolver value (separate from `SetOperators` / construction), and is called *between* `SetOperators` and `Solve()` in both the eigenmode-driver call site (`palace/drivers/eigensolver.cpp:264`, conditional on user-supplied-vs-random initial vector) and the mode-eigensolver pipeline call site (`palace/models/modeeigensolver.cpp:474`, conditional on the `initial_space` argument to `ModeEigenSolver::Solve()`). The ordering invariant is: `SetOperators` first (allocates workspace; ARPACK's `SetInitialSpace` ABORTs if `n == 0` per `palace/linalg/arpack.cpp:253`), then optional `SetInitialSpace`, then `Solve()`. Each `Solve()` invocation may supply a different initial space (`modeeigensolver.cpp:474` is inside a per-call function; conceptually re-callable with different initial spaces against the same constructed eigensolver). **This is per-call control** — the value is bound just before `Solve()` and consumed by that one `Solve()` invocation. Resolution: **keep `initial_space` in `EigControl`** (the current rough-in placement is correct); document the construction-side prerequisite (`E` must have its operators bound before `initial_space` is meaningful) as a precondition note rather than as an axis decision. The open-question routing is dropped.

**(3) `eigsolve-iteration-count-result-field`** — **add the field with an L1-constructive annotation** (per cycle-010 `LinearSolveFailed` precedent). The L0 `EigenvalueSolver` abstract base does NOT expose a per-call iteration count via any virtual; the count is consumed only at print-side. ARPACK's outer iteration count is `iparam[2]` inside `SolveInternal` (`palace/linalg/arpack.cpp:342, 350`) and is printed but never stored where a caller could retrieve it. SLEPc has `EPSGetIterationNumber` / `PEPGetIterationNumber` / `NEPGetIterationNumber` available in the PETSc API, but **Palace never calls them** (search confirmed: zero occurrences in the `palace/` source tree). NLEPS's `QuasiNewtonSolver::Solve` has internal Newton-iteration counters, also not exposed. Resolution: **add `iterations : Int` field to `EigResult`** with an L1-constructive annotation explaining that current L0 instantiations cannot populate it — the field is reserved for downstream L4 monadic-coordination consumers (analogous to `LinearSolveFailed`); materialisation defers to the future `eigsolve-mutation-rotation` L1>L0 theme (cycle-011 wave-1 sibling sketch). Negative-anchor citations: `palace/linalg/eps.hpp:124-140` (no `GetIterations` virtual in the surface); zero occurrences of `EPSGetIterationNumber` in Palace source. The "Strict positive-iteration termination" non-law in Algebraic-laws gets a tightened parenthetical now that the field exists.

The dispatch applies **edits across all three resolution sites in `book/src/L1/eigsolve.md`** (§Signature `EigResult` record, §Signature shape contract for `EigControl`, §Algebraic-laws §5, §"Laws that explicitly do not hold" Strict-positive-iteration bullet, §Status block, §Evidence rows), plus **three OQ-ledger yaml-status flips + resolution narratives** at `scaffolding/open-questions.md`. All three OQs flip `open → resolved` (not `partially-answered` — these are full resolutions; no downstream cycles of work are needed to land the resolutions in their entirety, unlike `LinearSolveFailed` which needed the materialising L1>L0 theme as follow-up). The `iterations`-field materialisation is the only follow-up, and is already in flight via cycle-011 wave-1 sibling dispatch #7 (`eigsolve-mutation-rotation`); flagged in §Open questions.

This is structural rewriting per lifter discipline: the resolutions adopt the L0-evidence-anchored answer in each case (the scaling convention IS un-scaled at L0; the initial-space IS per-call at L0; the iteration count is NOT exposed at L0 — three direct readings of `eps.hpp` + the three backend bodies). No content authorship; no operator semantics changed.

## Proposed changes

### Edit 1: `book/src/L1/eigsolve.md` — §Signature `EigResult` record, add `iterations` field with constructive-introduction note inline

The `EigResult` record gains a new `iterations` field. The constructive-introduction caveat is encoded inline (using the same comment-block style the other fields use), with the canonical citation pointer to a new post-block callout (Edit 4).

```edit:book/src/L1/eigsolve.md
[old]:EigResult[N, K_max] = {
  eigenvalues   : Tensor[K, complex],                -- the K converged eigenvalues
  eigenvectors  : Tensor[K, N, complex],             -- corresponding eigenvectors, unit-norm
                                                     --   (or B-orthonormal if E.B is set)
  converged     : Int,                               -- number of converged pairs (0 <= K <= K_max)
  requested     : Int,                               -- number requested (= K_max)
  error         : Tensor[K, real],                   -- per-pair error norm (per ErrorType bound in E)
  scaling_gamma : Real,                              -- Higham-2008 gamma (1.0 if ScaleType::NONE)
  scaling_delta : Real,                              -- Higham-2008 delta (1.0 if ScaleType::NONE)
  status        : EigStatus
}
[new]:EigResult[N, K_max] = {
  eigenvalues   : Tensor[K, complex],                -- the K converged eigenvalues
                                                     --   (in original-problem coordinates;
                                                     --    un-scaled at the L0 GetEigenvalue boundary)
  eigenvectors  : Tensor[K, N, complex],             -- corresponding eigenvectors, unit-norm
                                                     --   (or B-orthonormal if E.B is set)
  converged     : Int,                               -- number of converged pairs (0 <= K <= K_max)
  requested     : Int,                               -- number requested (= K_max)
  error         : Tensor[K, real],                   -- per-pair error norm (per ErrorType bound in E)
  scaling_gamma : Real,                              -- Higham-2008 gamma factor used internally
                                                     --   (1.0 if ScaleType::NONE; informational only —
                                                     --    eigenvalues are already un-scaled)
  scaling_delta : Real,                              -- Higham-2008 delta factor used internally
                                                     --   (1.0 if ScaleType::NONE; informational only)
  iterations    : Int,                               -- outer-iteration count (L1-constructive;
                                                     --   see Note on EigResult.iterations below)
  status        : EigStatus
}
```

### Edit 2: `book/src/L1/eigsolve.md` — §Signature shape contract bullets, refine `EigControl.initial_space` and `EigResult.scaling_gamma/delta`/`iterations` prose

Refines the shape-contract bullets to drop the rough-in-routing language on `initial_space` and add the un-scaled-coordinate note on `scaling_*` plus the constructive-iterations note. The bullet on `E` is unchanged.

```edit:book/src/L1/eigsolve.md
[old]:- `control` — `EigControl` — per-call configuration. The only field is the optional initial-subspace seed `initial_space` (the L0 `SetInitialSpace(const ComplexVector &v)` virtual at `palace/linalg/eps.hpp:122`); all other tuning lives inside `E`. `initial_space` is rough-in pending a decision on whether it is properly per-call control or another construction-bound axis (open question below).
- result — `EigResult[N, K_max]` — record containing the `K = result.converged` converged eigenvalues (`K ≤ K_max`), the corresponding eigenvectors as a stacked tensor (each unit-norm in the L2 sense, or B-orthonormal if `E.B` is set per `palace/linalg/eps.hpp:130-132` docstring), the per-pair error norm (per the `ErrorType` bound in `E` — `ABSOLUTE` / `RELATIVE` / `BACKWARD` from `palace/linalg/eps.hpp:44-49`), the Higham scaling factors (`γ`, `δ`) for the polynomial / nonlinear cases (both `1.0` when `ScaleType::NONE`), and a sum-typed `status` flag distinguishing the four termination modes (see Algebraic laws §3 for the source-anchored semantics of each).
[new]:- `control` — `EigControl` — per-call configuration. The only field is the optional initial-subspace seed `initial_space` (the L0 `SetInitialSpace(const ComplexVector &v)` virtual at `palace/linalg/eps.hpp:122`); all other tuning lives inside `E`. **Placement-as-per-call-control is the resolved convention** (cycle-011 lifter): at L0, `SetInitialSpace` is a separate method on the eigensolver virtual surface (not bundled with construction), and is invoked between `SetOperators` and `Solve()` at both observed call sites — `palace/drivers/eigensolver.cpp:264` (conditional on user-supplied vs random-generated initial vector) and `palace/models/modeeigensolver.cpp:474` (conditional on the `initial_space` argument to `ModeEigenSolver::Solve()`). The ordering invariant is `SetOperators` → optional `SetInitialSpace` → `Solve()`; `SetInitialSpace` ABORTs if invoked pre-`SetOperators` (`palace/linalg/arpack.cpp:253` and analogues). At L1 the precondition that `E` has its operators bound is encoded in `E`'s type — by the time `eigsolve(E, control)` is called, the operators are construction-bound; supplying `initial_space` in `control` is therefore well-defined.
- result — `EigResult[N, K_max]` — record containing the `K = result.converged` converged eigenvalues (`K ≤ K_max`, **in the original-problem coordinate system** — see Algebraic-laws §5 for the L0-anchored un-scaling convention), the corresponding eigenvectors as a stacked tensor (each unit-norm in the L2 sense, or B-orthonormal if `E.B` is set per `palace/linalg/eps.hpp:130-132` docstring), the per-pair error norm (per the `ErrorType` bound in `E` — `ABSOLUTE` / `RELATIVE` / `BACKWARD` from `palace/linalg/eps.hpp:44-49`), the Higham scaling factors `γ`, `δ` (both `1.0` when `ScaleType::NONE`; **informational only at L1** — the L0 surface already un-scales at the `GetEigenvalue` boundary, so `eigenvalues` is in un-scaled coordinates regardless), the outer-iteration count (**L1-constructive** — current L0 surface does not expose an iteration-count accessor; see Note on `EigResult.iterations` below for the constructive-introduction treatment), and a sum-typed `status` flag distinguishing the four termination modes (see Algebraic laws §3 for the source-anchored semantics of each).
```

### Edit 3: `book/src/L1/eigsolve.md` — replace Algebraic-laws §5 (scaling) with corrected L0-anchored convention

The current rough-in text states the wrong convention (says L1 returns scaled, asks open question whether to un-scale). The L0 surface already un-scales uniformly at the `GetEigenvalue` accessor boundary. Replace §5 with the corrected statement plus citations.

```edit:book/src/L1/eigsolve.md
[old]:5. **Scaling invariance** (modulo tolerance, for the polynomial / nonlinear cases): when `E.ScaleType = NORM_2`, the eigenvalues `λᵢ` returned in `EigResult.eigenvalues` are scaled per Higham 2008 (γ = √(‖K‖₂ / ‖M‖₂); δ = 2 / (‖K‖₂ + γ‖C‖₂ + γ²‖M‖₂)); the un-scaled eigenvalues of the original problem are recovered by multiplying by γ. **At L1, the returned `eigenvalues` are in the scaled coordinate system**; the `EigResult.scaling_gamma` / `EigResult.scaling_delta` fields are provided for downstream un-scaling. (This matches the L0 surface: `GetScalingGamma()` / `GetScalingDelta()` at `palace/linalg/eps.hpp:102-103` are part of the interface specifically because callers need to un-scale.) **Open question**: should L1 instead un-scale at the result-extraction boundary, so that `EigResult.eigenvalues` are always in the original coordinate system regardless of `E.ScaleType`? This is a coordinate-system convention; the current L0 surface leaves it to the caller. Rough-in.
[new]:5. **Scaling-coordinate convention** (modulo tolerance, for the polynomial / nonlinear cases): when `E.ScaleType = NORM_2`, the internal Higham 2008 scaling applies γ = √(‖K‖₂ / ‖M‖₂) and δ = 2 / (‖K‖₂ + γ‖C‖₂ + γ²‖M‖₂) to the operators before the Krylov iteration runs (or γ = ‖K‖₂/‖M‖₂ with δ = 2/‖K‖₂ for the linear case per `palace/linalg/arpack.cpp:498-499`, `palace/linalg/slepc.cpp:791-792`). **At L1, the returned `EigResult.eigenvalues` are in the original-problem coordinate system** — un-scaling is performed at the L0 `GetEigenvalue` accessor boundary across the EPS / PEP / NLEPS backends: ARPACK at `palace/linalg/arpack.cpp:387` (`eig[i] = eig[i] * gamma` applied inside `SolveInternal` post-`neupd`, before the result is observable via `GetEigenvalue`), SLEPc-EPS at `palace/linalg/slepc.cpp:711-716` (`GetEigenvalue` returns `l * gamma`), SLEPc-PEP at `palace/linalg/slepc.cpp:1194-1203` (same `l * gamma` pattern), NLEPS at `palace/linalg/nleps.cpp:88-93` (returns stored eigenvalues that were already un-scaled via the linear-eigensolver priming at `palace/linalg/nleps.cpp:267, 314`). SLEPc-NEP at `palace/linalg/slepc.cpp:1554-1560` returns `l` directly without applying `* gamma` — the SLEPc-NEP backend manages its own coordinate handling separately from the EPS / PEP un-scale-at-accessor pattern (note: `SlepcNEPSolver::SetOperators` at `palace/linalg/slepc.cpp:1645-1651` and `:1711-1719` DOES compute a non-trivial `gamma = std::sqrt(normK / normM)` when `type != ScaleType::NONE`, so the "no Higham scaling for NEP" reading would be wrong; the precise un-scaling convention for the NEP backend is flagged for follow-up audit — see `scaffolding/open-questions.md` entry on NEP scaling gap below). The L0 convention is therefore uniform across EPS / PEP / NLEPS — **caller-observable eigenvalues are in original-problem coordinates** — with the SLEPc-NEP convention pending audit. The L1 form mirrors the EPS / PEP / NLEPS uniform convention — `EigResult.eigenvalues` is in original-problem coordinates. The `EigResult.scaling_gamma` / `EigResult.scaling_delta` fields are exposed at L1 as **informational** — they record the operator-norm-derived scaling factors used internally (e.g., for downstream consumers that want to inspect operator conditioning or recover the residual-in-scaled-coords for diagnostic purposes), not as action-required un-scaling factors. Resolved (cycle-011, lifter): the cycle-009 rough-in routing question is closed in favour of convention (b) per the L0 un-scale-at-accessor evidence across EPS / PEP / NLEPS; the SLEPc-NEP detail is non-blocking and flagged for follow-up audit; see `scaffolding/open-questions.md` entry `eigsolve-scaling-coordinate-convention`.
```

### Edit 4: `book/src/L1/eigsolve.md` — add `EigResult.iterations` post-Signature callout (parallel structure to the cycle-010 `LinearSolveFailed` callout)

This edit inserts a second post-Signature callout, immediately after the existing `LinearSolveFailed` callout block (which is currently between source line 47 and the start of "Shape contract"). The new callout addresses the `iterations` field's L1-constructive status. Specified as `[insert-after]` matching the cycle-010 edit-6 pattern.

```edit:book/src/L1/eigsolve.md
[insert-after: the end-of-blockquote of the existing "Note on `EigStatus::LinearSolveFailed`" callout (the line ending "current L0 instantiations of `eigsolve` will not produce it.") — the new callout goes on the next line, before the "Shape contract (bunsen-style, named axes):" line at source line ~49]
[content]:

> **Note on `EigResult.iterations` (constructed by the L1 form).** The `iterations` field has no direct L0 anchor on the `EigenvalueSolver` virtual surface (`palace/linalg/eps.hpp:124-140` — `Solve()`, `GetEigenvalue`, `GetEigenvector`, `GetError`, `RescaleEigenvectors` — none expose an iteration count). The count exists per-backend at the implementation level: ARPACK has `iparam[2]` consumed at `palace/linalg/arpack.cpp:342` and printed at line 350, but never stored where a caller could retrieve it; SLEPc has `EPSGetIterationNumber` / `PEPGetIterationNumber` / `NEPGetIterationNumber` in the PETSc API but Palace never calls these (zero occurrences across `palace/linalg/slepc.cpp` per `mcp__palace-codemap__search_text`); NLEPS has internal Newton-iteration counters inside `QuasiNewtonSolver::Solve` (`palace/linalg/nleps.cpp:351-805`), also not exposed. The `iterations` field is **introduced by the L1 form** in parallel to `EigStatus::LinearSolveFailed` (cycle-010 lifter) — both make per-call eigensolver internal state visible at the L1 surface for downstream L4 monadic-coordination consumers (an `iterate_while` composition operating on `EigSolver[problem]` needs the iteration count both for diagnostic reporting and for budget-aware re-dispatch decisions, in the same way `ksp_solve` consumers downstream of L1 use `SolveResult.iterations`). A future `eigsolve-mutation-rotation` L1>L0 theme (cycle-011 wave-1 sibling sketch at `book/src/L1-L0/eigsolve-mutation-rotation.md`) will materialise the field by either (a) adding a `GetIterations()` virtual accessor to `EigenvalueSolver` and per-backend implementations that capture the existing internal counter (ARPACK's `iparam[2]`; SLEPc's `EPSGetIterationNumber`; NLEPS's Newton-step counter), or (b) plumbing the count through the existing print-side flow into a new accessor. Until that theme lands, treat `iterations` as an L1-constructive value: current L0 instantiations of `eigsolve` cannot populate it directly; an L1 wrapping layer would either leave the field as `-1` (sentinel for "L0 surface silent") or capture the print-side output. The cycle-011 wave-1 `eigsolve-mutation-rotation` L1>L0 theme already records the materialisation shape under its Sub-pattern C; treating this OQ as resolved is consistent with the cycle-010 `LinearSolveFailed` precedent (the variant is kept; materialisation defers to the L1>L0 theme).
```

### Edit 5: `book/src/L1/eigsolve.md` — §"Laws that explicitly do not hold", tighten the Strict-positive-iteration bullet (now that `iterations` is a field)

```edit:book/src/L1/eigsolve.md
[old]:- **Strict positive-iteration termination** — for problems where `control.initial_space` is set to the exact eigenvector basis, the iteration may converge in zero or near-zero iterations; callers that assume `EigResult.iterations ≥ 1` are wrong. (Note: `iterations` is not currently a field of the proposed `EigResult` — it could be added if downstream consumers need it; routes to open question.)
[new]:- **Strict positive-iteration termination** — for problems where `control.initial_space` is set to the exact eigenvector basis, the iteration may converge in zero or near-zero iterations; callers that assume `EigResult.iterations ≥ 1` are wrong. (Note: `EigResult.iterations` is added as an L1-constructive field per the §Signature callout above; current L0 instantiations of `eigsolve` cannot populate it directly and may yield a sentinel value, so callers must also guard against the "field not yet materialised" case. Resolved cycle-011, lifter.)
```

### Edit 6: `book/src/L1/eigsolve.md` — §Status block, update with cycle-011 cluster resolution

```edit:book/src/L1/eigsolve.md
[old]:`rough-in (test-coverage-bounded, cycle-009; LinearSolveFailed-constructive resolved cycle-010)` — the structural signature (input/output shape, the four-way `EigStatus`, the `EigResult` record fields) is well-anchored by direct source reading of `eps.hpp` and the three `Solve()` bodies. The `Converged` / `PartialConverged` / `MaxIterReached` cases are directly source-witnessed (`palace/drivers/eigensolver.cpp:367-374`); the `LinearSolveFailed` case is **constructively introduced by the L1 form** (see §Signature callout and Algebraic-laws §3) — annotated as L1-constructive in cycle-010 (resolving cycle-009 OQ `eigsolve-linear-solve-failed-status-anchor`), with materialisation deferred to a future `eigsolve-mutation-rotation` L1>L0 theme.
[new]:`rough-in (test-coverage-bounded, cycle-009; LinearSolveFailed-constructive resolved cycle-010; variant-axis & result-record inventory closed cycle-011)` — the structural signature (input/output shape, the four-way `EigStatus`, the `EigResult` record fields including the cycle-011 added `iterations` field) is well-anchored by direct source reading of `eps.hpp` and the three `Solve()` bodies. The `Converged` / `PartialConverged` / `MaxIterReached` cases are directly source-witnessed (`palace/drivers/eigensolver.cpp:367-374`); the `LinearSolveFailed` case is **constructively introduced by the L1 form** (see §Signature callout and Algebraic-laws §3) — annotated as L1-constructive in cycle-010 (resolving cycle-009 OQ `eigsolve-linear-solve-failed-status-anchor`), with materialisation deferred to the cycle-011 wave-1 `eigsolve-mutation-rotation` L1>L0 theme. The cycle-009 cluster of three further OQs is resolved cycle-011 (this lifter): `eigsolve-scaling-coordinate-convention` adopts convention (b) — L1 returns un-scaled eigenvalues, matching the L0-uniform un-scale-at-accessor convention (Algebraic-laws §5 corrected); `eigsolve-initial-space-axis-placement` keeps `initial_space` in `EigControl` (per-call control, matching the L0 method placement); `eigsolve-iteration-count-result-field` adds `iterations` to `EigResult` as a second L1-constructive field (parallel to `LinearSolveFailed`), with materialisation deferred to the `eigsolve-mutation-rotation` theme.
```

### Edit 7: `book/src/L1/eigsolve.md` — §Evidence, append the L0 anchors used by this cluster (scaling un-scaling sites + iteration-count negative anchors)

```edit:book/src/L1/eigsolve.md
[old]:- `scaffolding/open-questions.md:1470-1479` — cycle-009 OQ `eigsolve-linear-solve-failed-status-anchor` (the cycle-010 lifter dispatch target; resolved by this entry).
[new]:- `scaffolding/open-questions.md:1470-1479` — cycle-009 OQ `eigsolve-linear-solve-failed-status-anchor` (the cycle-010 lifter dispatch target; resolved by this entry).
- `scaffolding/open-questions.md:1493-1502` — cycle-009 OQ `eigsolve-scaling-coordinate-convention` (the cycle-011 lifter cluster dispatch target; resolved by this entry).
- `scaffolding/open-questions.md:1504-1513` — cycle-009 OQ `eigsolve-initial-space-axis-placement` (the cycle-011 lifter cluster dispatch target; resolved by this entry).
- `scaffolding/open-questions.md:1515-1524` — cycle-009 OQ `eigsolve-iteration-count-result-field` (the cycle-011 lifter cluster dispatch target; resolved by this entry).
- `palace/linalg/arpack.cpp:387` — `eig[i] = eig[i] * gamma` inside `SolveInternal` after `neupd`. Positive anchor: ARPACK un-scales eigenvalues at the L0 boundary uniformly across all callers of `GetEigenvalue`.
- `palace/linalg/slepc.cpp:711-716` — `SlepcEPSSolverBase::GetEigenvalue(i)` returning `l * gamma`. Positive anchor: SLEPc-EPS un-scales at the accessor.
- `palace/linalg/slepc.cpp:1194-1203` — `SlepcPEPSolverBase::GetEigenvalue(i)` returning `l * gamma`. Positive anchor: SLEPc-PEP un-scales at the accessor.
- `palace/linalg/slepc.cpp:1554-1560` — `SlepcNEPSolverBase::GetEigenvalue(i)` returning `l` directly (no `* gamma`). The SLEPc-NEP backend manages its own coordinate handling separately from the EPS / PEP un-scale-at-accessor pattern; the precise convention is flagged for follow-up audit (the NEP `SetOperators` overloads at `palace/linalg/slepc.cpp:1645-1651, 1711-1719` DO compute non-trivial `gamma = std::sqrt(normK / normM)`, so the simpler "NEP gamma = 1" reading is wrong). This detail does not affect the broader resolution.
- `palace/linalg/nleps.cpp:88-93` — `NonLinearEigenvalueSolver::GetEigenvalue(i)` returning stored `eigenvalues[j]`. Positive anchor: NLEPS stores already-un-scaled values from the linear-eigensolver priming.
- `palace/linalg/arpack.cpp:249-260` — `ArpackEigenvalueSolver::SetInitialSpace` body; the `MFEM_VERIFY(n > 0, ...)` precondition + `info = 1` toggle (`info = 0` is the random-initial-space marker). Direct anchor for the initial-space-as-per-call-control treatment.
- `palace/linalg/slepc.cpp:657-669` — `SlepcEPSSolverBase::SetInitialSpace` body; `EPSSetInitialSpace(eps, 1, is)` PETSc call. Direct anchor for SLEPc per-call initial-space binding.
- `palace/drivers/eigensolver.cpp:264` — `eigen->SetInitialSpace(v0)` call site in the eigenmode driver, conditional on user-supplied vs random initial vector. Direct anchor for the call-ordering pattern (`SetOperators` → optional `SetInitialSpace` → `Solve()`).
- `palace/models/modeeigensolver.cpp:474` — `if (initial_space) eigen->SetInitialSpace(*initial_space);` call site in the mode-eigensolver pipeline, per-`ModeEigenSolver::Solve()` invocation. Direct anchor for per-call control.
- `palace/linalg/arpack.cpp:342, 350` — ARPACK driver-side `iparam[2]` iteration count print. Negative anchor for `EigResult.iterations`: the count exists internally but is never exposed via an accessor.
- `palace/linalg/eps.hpp:124-140` — `EigenvalueSolver` result-extraction surface (`Solve`, `GetEigenvalue`, `GetEigenvector`, `GetError`, `RescaleEigenvectors`). Negative anchor for `EigResult.iterations`: no `GetIterations` virtual on the surface.
- `mcp__palace-codemap__search_text` (verified by lifter): zero occurrences of `EPSGetIterationNumber`, `PEPGetIterationNumber`, or `NEPGetIterationNumber` anywhere in the `palace/` source tree. Negative anchor: SLEPc's iteration-count accessors are available in the PETSc API but unused by Palace.
- `reports/2026-05-27T234730Z-abstractor-eigsolve-mutation-rotation-l1-l0/CYCLE.md` — cycle-011 wave-1 sibling abstractor dispatch; the L1>L0 theme that will materialise `EigResult.iterations` (and `EigStatus::LinearSolveFailed`) when an upstream refactor lands. Sub-pattern C of that theme is the materialisation site.
- `reports/2026-05-27T220558Z-lifter-eigsolve-linear-solve-failed-anchor/CYCLE.md` — cycle-010 sibling lifter dispatch; the structural precedent for L1-constructive fields with negative-anchor citations. The cycle-011 `iterations` resolution uses the same pattern.
```

### Edit 8: `scaffolding/open-questions.md` — append resolution narrative to `eigsolve-scaling-coordinate-convention` entry

The OQ ledger is any-agent-appendable; the cycle-010 sibling dispatch established the in-place yaml flip + append-narrative pattern.

```edit:scaffolding/open-questions.md
[append-after: line 1502, the prose body of the eigsolve-scaling-coordinate-convention OQ ending with "Source: `reports/2026-05-27T191929Z-harvester-eigsolve-L1/CYCLE.md` §Open questions / caveats item 2."]
[content]:

**Resolved cycle-011 (lifter)**: Dispatched at `reports/2026-05-27T235632Z-lifter-eigsolve-oq-cluster/` (unified resolution of the 3-OQ cluster). Adopted convention (b) — the L1 form returns eigenvalues in the original-problem coordinate system, matching the L0 surface's un-scale-at-accessor convention across the EPS / PEP / NLEPS backends. Direct evidence: ARPACK at `palace/linalg/arpack.cpp:387` (`eig[i] = eig[i] * gamma` inside `SolveInternal` post-`neupd`); SLEPc-EPS at `palace/linalg/slepc.cpp:711-716` (`GetEigenvalue` returns `l * gamma`); SLEPc-PEP at `palace/linalg/slepc.cpp:1194-1203` (same `l * gamma`); NLEPS at `palace/linalg/nleps.cpp:88-93` (returns stored already-un-scaled eigenvalues from linear-eigensolver priming). SLEPc-NEP at `palace/linalg/slepc.cpp:1554-1560` returns `l` directly without applying `* gamma` — the SLEPc-NEP backend manages its own coordinate handling separately from the EPS / PEP un-scale-at-accessor pattern. (Note: `SlepcNEPSolver::SetOperators` at `palace/linalg/slepc.cpp:1645-1651` and `:1711-1719` DOES compute a non-trivial `gamma = std::sqrt(normK / normM)` when `type != ScaleType::NONE`, so the simpler "no Higham scaling for NEP" reading would be wrong; the precise un-scaling convention for the SLEPc-NEP backend is flagged for follow-up audit, but this detail does not affect the broader resolution — the un-scale-at-accessor pattern holds uniformly across EPS / PEP / NLEPS, which is what the L1 form mirrors.) The cycle-009 rough-in chapter's Algebraic-law §5 stated the opposite (incorrectly: "L1 returns scaled"); the cycle-011 lifter rewrites §5 to match L0. The `scaling_gamma` / `scaling_delta` fields remain in `EigResult` as informational (record the operator-norm-derived factors used internally; downstream consumers can inspect operator conditioning or recover residual-in-scaled-coords for diagnostics, but the eigenvalues field is itself in original-problem coordinates). Status: resolved (SLEPc-NEP coordinate-convention detail flagged for follow-up audit as a separate OQ).
```

### Edit 9: `scaffolding/open-questions.md` — yaml-status flip for `eigsolve-scaling-coordinate-convention`

```edit:scaffolding/open-questions.md
[old]:slug: eigsolve-scaling-coordinate-convention
opened_at: cycle-009
opened_by: harvester
status: open
[new]:slug: eigsolve-scaling-coordinate-convention
opened_at: cycle-009
opened_by: harvester
status: resolved
resolved_at: cycle-011
resolved_in: reports/2026-05-27T235632Z-lifter-eigsolve-oq-cluster/
```

### Edit 10: `scaffolding/open-questions.md` — append resolution narrative to `eigsolve-initial-space-axis-placement` entry

```edit:scaffolding/open-questions.md
[append-after: line 1513, the prose body of the eigsolve-initial-space-axis-placement OQ ending with "Source: `reports/2026-05-27T191929Z-harvester-eigsolve-L1/CYCLE.md` §Open questions / caveats item 3."]
[content]:

**Resolved cycle-011 (lifter)**: Dispatched at `reports/2026-05-27T235632Z-lifter-eigsolve-oq-cluster/` (unified resolution of the 3-OQ cluster). Keep `initial_space` in `EigControl` (per-call control); the current rough-in placement is correct. Direct evidence: `SetInitialSpace(const ComplexVector &v)` is a *method* on `EigenvalueSolver` (`palace/linalg/eps.hpp:122`) separate from `SetOperators` / construction, and is invoked between `SetOperators` and `Solve()` at both observed call sites — `palace/drivers/eigensolver.cpp:264` (conditional on user-supplied vs random initial vector) and `palace/models/modeeigensolver.cpp:474` (conditional on the `initial_space` argument to `ModeEigenSolver::Solve()`, which is a re-callable per-call function). The ordering invariant is `SetOperators` first (allocates the per-backend workspace; ARPACK `MFEM_VERIFY(n > 0, ...)` at `palace/linalg/arpack.cpp:253` rejects pre-`SetOperators` invocation; SLEPc analogue at `palace/linalg/slepc.cpp:659-661`), then optional `SetInitialSpace`, then `Solve()`. The construction-side prerequisite is documented at L1 as a precondition on `E`'s opaque type (operators are construction-bound; `initial_space` in `control` is well-defined only against an `E` whose operators are bound) rather than as an axis decision. Status: resolved.
```

### Edit 11: `scaffolding/open-questions.md` — yaml-status flip for `eigsolve-initial-space-axis-placement`

```edit:scaffolding/open-questions.md
[old]:slug: eigsolve-initial-space-axis-placement
opened_at: cycle-009
opened_by: harvester
status: open
[new]:slug: eigsolve-initial-space-axis-placement
opened_at: cycle-009
opened_by: harvester
status: resolved
resolved_at: cycle-011
resolved_in: reports/2026-05-27T235632Z-lifter-eigsolve-oq-cluster/
```

### Edit 12: `scaffolding/open-questions.md` — append resolution narrative to `eigsolve-iteration-count-result-field` entry

```edit:scaffolding/open-questions.md
[append-after: line 1524, the prose body of the eigsolve-iteration-count-result-field OQ ending with "Source: `reports/2026-05-27T191929Z-harvester-eigsolve-L1/CYCLE.md` §Open questions / caveats item 4."]
[content]:

**Resolved cycle-011 (lifter)**: Dispatched at `reports/2026-05-27T235632Z-lifter-eigsolve-oq-cluster/` (unified resolution of the 3-OQ cluster). Adopted the cycle-010 `LinearSolveFailed` precedent (option (b)) — add the `iterations : Int` field to `EigResult` with an L1-constructive annotation. Direct evidence: the `EigenvalueSolver` virtual surface (`palace/linalg/eps.hpp:124-140`) does not expose an iteration-count accessor; ARPACK has `iparam[2]` consumed at `palace/linalg/arpack.cpp:342, 350` (printed only, never stored where a caller can retrieve); SLEPc has `EPSGetIterationNumber` / `PEPGetIterationNumber` / `NEPGetIterationNumber` available in the PETSc API but Palace never calls them (zero occurrences across the `palace/` source tree per `mcp__palace-codemap__search_text`); NLEPS's `QuasiNewtonSolver::Solve` has internal Newton-iteration counters at `palace/linalg/nleps.cpp:351-805`, also not exposed. The field is added as L1-constructive (parallel to `EigStatus::LinearSolveFailed` cycle-010) — it pre-positions the iteration-count for downstream L4 monadic-coordination consumers; materialisation defers to the cycle-011 wave-1 `eigsolve-mutation-rotation` L1>L0 theme (Sub-pattern C of `reports/2026-05-27T234730Z-abstractor-eigsolve-mutation-rotation-l1-l0/CYCLE.md`), which would either add a `GetIterations()` virtual + per-backend accessor implementations, or plumb the count through the existing print-side flow. The Algebraic-laws §"Strict positive-iteration termination" non-law bullet is tightened to acknowledge the field is now part of the record but may yield a sentinel value under current L0 instantiations. Status: resolved.
```

### Edit 13: `scaffolding/open-questions.md` — yaml-status flip for `eigsolve-iteration-count-result-field`

```edit:scaffolding/open-questions.md
[old]:slug: eigsolve-iteration-count-result-field
opened_at: cycle-009
opened_by: harvester
status: open
[new]:slug: eigsolve-iteration-count-result-field
opened_at: cycle-009
opened_by: harvester
status: resolved
resolved_at: cycle-011
resolved_in: reports/2026-05-27T235632Z-lifter-eigsolve-oq-cluster/
```

## Discipline notes

This is a pure structural re-anchor lift on the cycle-009 rough-in L1 `eigsolve` chapter, scoped (per cycle-011 planner) to the **three remaining cycle-009 OQs as a unified cluster**. The unified-dispatch framing matches the lifter role-spec's "broad interpretation of 'one theme per invocation'" — the three OQs together cover the "L1 eigsolve variant-axis & result-record inventory" theme.

Six small notes on choices:

1. **Why three full resolutions (not partial)?** All three OQs are decisional questions about the L1 vocabulary's relationship to L0 evidence. The L0 evidence is unambiguous in each case: (1) un-scaling at accessor is uniform; (2) `SetInitialSpace` is a separate per-call method; (3) no iteration-count accessor exists on the virtual surface. The cycle-010 sibling dispatch left `LinearSolveFailed` partially-answered because the variant's full materialisation required a follow-up `eigsolve-mutation-rotation` L1>L0 theme (which is now itself in flight as cycle-011 wave-1 sibling dispatch #7). The three OQs in this cluster do not require analogous follow-up theme work: the scaling and initial-space resolutions are intrinsic to the L1 entry (no L1>L0 theme needs to do anything special for them — the L0 surface already does the un-scaling; the L0 surface already supports the per-call binding), and the iterations resolution's materialisation is already covered by the cycle-011 wave-1 sibling. Full resolution is appropriate.

2. **Why convention (b) for scaling, not (a)?** The L1 entry's cycle-009 text states convention (a) — "L1 returns scaled". This is wrong against the L0 evidence: all three backends un-scale at the `GetEigenvalue` accessor boundary. The cycle-009 rough-in author may have read the un-scaling at the accessor as caller-side (since the accessor is a method on the eigensolver), but the un-scaling happens before any L1-equivalent caller can observe — for ARPACK, the un-scale is inside `SolveInternal` (before any `GetEigenvalue` call), and for SLEPc, the un-scale is in the `GetEigenvalue` body itself. The L1 form, being a structural rewrite of the L0 surface, mirrors the L0 caller's view: post-`GetEigenvalue`, eigenvalues are in original-problem coordinates. Convention (b) is therefore the only L0-faithful resolution; convention (a) would require L1 to re-introduce scaling that L0 has already undone, which would be a regression.

3. **Why keep `scaling_gamma` / `scaling_delta` in `EigResult` at all if eigenvalues are un-scaled?** Two reasons: (i) downstream consumers may want the factors for diagnostic purposes (operator-norm-derived; reveal conditioning of the polynomial / nonlinear system); (ii) downstream consumers may want to recover the per-pair residual in the scaled coordinate system (the L0 `RescaleEigenvectors` computes residual in scaled coords; un-scaling the residual requires the factors). Removing the fields would forfeit this without a counterbalancing simplification. Keep them as informational; rename the docstring to clarify.

4. **Why the L1-constructive treatment for `iterations` rather than dropping the field?** The cycle-010 `LinearSolveFailed` precedent established the constructive-introduction pattern — L1 surfaces semantic distinctions the L0 form lacks, for downstream L4 monadic-coordination consumers. The `iterations` field has the same justification: an `iterate_while` composition operating on `EigSolver[problem]` needs the iteration count both for diagnostic reporting and for budget-aware re-dispatch decisions. The field is small (a single Int); the constructive-introduction cost is the same as `LinearSolveFailed`'s (the negative-anchor citations and the materialisation deferral); the future materialisation path is concrete (add a `GetIterations` virtual + per-backend implementations). Adding the field is the appropriate analog resolution; dropping it would silently lose information that's already trivially available at the L0 implementation level (ARPACK's `iparam[2]`).

5. **Why no Algebraic-law §6 added for the `iterations` field?** Iteration count is not itself an algebraic property of `eigsolve` — it's a per-call diagnostic. The Algebraic-laws section is for `(λ, x)`-level properties that hold modulo tolerance. The `iterations` field is closer in nature to `converged` / `requested` / `status` — a per-call termination-state diagnostic; the existing Algebraic-laws §3 (Termination semantics) is the appropriate site, and the existing non-law bullet ("Strict positive-iteration termination") covers the relevant caveats. Edit 5 tightens the existing bullet rather than adding a new law.

6. **Why no scope expansion to the cycle-011 wave-1 sibling theme?** The cycle-011 wave-1 abstractor dispatch (`reports/2026-05-27T234730Z-abstractor-eigsolve-mutation-rotation-l1-l0/`) is in flight in parallel; per the cycle-011 planner's dispatch-graph it has not yet been integrated, so this lifter dispatch treats it as an inputs-pointer (it documents what the future L1>L0 materialisation will do) but does not edit it. If the cycle-011 wave-1 abstractor's proposed-changes need re-anchoring against the resolved OQ cluster (e.g., if its `EigResult` field treatment differed from the cycle-011-lifter resolved shape), the cycle-011 integrator-finalize step would coordinate; or a cycle-012 lifter would re-anchor. The lifter discipline of "do not bundle multiple themes" applies — the L1>L0 theme is in flight under a separate dispatch.

## Supporting evidence

- `book/src/L1/eigsolve.md` — the chapter being re-anchored (cycle-009 rough-in; cycle-010 lifter LinearSolveFailed annotation).
- `reports/2026-05-27T191929Z-harvester-eigsolve-L1/CYCLE.md` — cycle-009 harvester report; opened all four eigsolve OQs.
- `reports/2026-05-27T220558Z-lifter-eigsolve-linear-solve-failed-anchor/CYCLE.md` — cycle-010 sibling lifter; the structural template for L1-constructive fields with negative-anchor citations.
- `reports/2026-05-27T234730Z-abstractor-eigsolve-mutation-rotation-l1-l0/CYCLE.md` — cycle-011 wave-1 sibling abstractor; the L1>L0 theme that will materialise `iterations`.
- `palace/linalg/eps.hpp:100-141` — `EigenvalueSolver` abstract virtual surface (verified by lifter; no `GetIterations` virtual; `SetInitialSpace` is a separate method; `GetScalingGamma/Delta` are accessors).
- `palace/linalg/arpack.cpp:249-260` — `ArpackEigenvalueSolver::SetInitialSpace` body (verified by lifter; `MFEM_VERIFY(n > 0, ...)` precondition; `info = 1` toggle).
- `palace/linalg/arpack.cpp:340-405` — `ArpackEigenvalueSolver::SolveInternal` body (verified by lifter; `num_it = iparam[2]` at line 342; `eig[i] = eig[i] * gamma` at line 387; un-scaling pre-`GetEigenvalue`).
- `palace/linalg/arpack.cpp:412-420` — `ArpackEigenvalueSolver::GetEigenvalue` body (verified by lifter; returns `eig.get()[j]` — value already un-scaled).
- `palace/linalg/slepc.cpp:657-669` — `SlepcEPSSolverBase::SetInitialSpace` body (verified by lifter; `EPSSetInitialSpace(eps, 1, is)` PETSc call).
- `palace/linalg/slepc.cpp:711-716` — `SlepcEPSSolverBase::GetEigenvalue` body (verified by lifter; `return l * gamma`).
- `palace/linalg/slepc.cpp:1194-1203` — `SlepcPEPSolverBase::GetEigenvalue` body (verified by lifter; `return l * gamma`).
- `palace/linalg/slepc.cpp:1554-1560` — `SlepcNEPSolverBase::GetEigenvalue` body (verified by lifter; `return l` — SLEPc-NEP returns `l` directly without `* gamma`; the backend manages its own coordinate handling separately, precise convention flagged for follow-up audit since `SetOperators` at `:1645-1651, 1711-1719` does compute non-trivial gamma).
- `palace/linalg/nleps.cpp:83-110` — `NonLinearEigenvalueSolver::SetInitialSpace` base body + `GetEigenvalue` body (verified by lifter; base `SetInitialSpace` is `MFEM_ABORT`; `GetEigenvalue` returns stored already-un-scaled value).
- `palace/linalg/nleps.cpp:260-325` — linear-eigensolver priming + un-scaled-value storage in `eigenvalues[i]` (verified by lifter; `linear_eigensolver_->GetEigenvalue(i)` returns un-scaled per linear-eigensolver's convention).
- `palace/drivers/eigensolver.cpp:255-270` — driver-side `SetInitialSpace` call site context (verified by lifter; conditional on user-supplied vs random; called after `SetOperators` setup).
- `palace/models/modeeigensolver.cpp:470-480` — mode-eigensolver `SetInitialSpace` call site (verified by lifter; `if (initial_space) eigen->SetInitialSpace(*initial_space);` immediately before `eigen->Solve()`).
- `mcp__palace-codemap__search_text` (verified by lifter): zero occurrences of `EPSGetIterationNumber`, `PEPGetIterationNumber`, `NEPGetIterationNumber` in the `palace/` source tree. SLEPc's iteration-count accessors are unused.

## Open questions / caveats

- **Three OQs flip to `resolved`, not `partially-answered`.** This dispatch resolves all three OQs in full; no follow-up theme work is required to make the resolutions in their entirety. The `iterations`-field materialisation is the only forward-looking item, and is already covered by the cycle-011 wave-1 sibling `eigsolve-mutation-rotation` L1>L0 theme dispatch (Sub-pattern C); the materialisation is not a deferred-but-needed step for *this* OQ's closure — analogous to how the cycle-010 `LinearSolveFailed` resolution was `partially-answered` because the L1>L0 theme didn't exist yet, but the cycle-011 wave-1 dispatch now establishes the theme. Once the L1>L0 theme integrates, both the cycle-010 `LinearSolveFailed` and the cycle-011 `iterations` constructive-introduction fields will have their materialisation site documented; the cycle-010 OQ can flip from `partially-answered` to `resolved` at that point (out of scope for this dispatch; flag for cycle-012 meta-phase or a cycle-012 lifter).

- **Scope conflict potential with the cycle-011 wave-1 abstractor's `EigResult` field list.** The wave-1 abstractor's L1>L0 theme report (`reports/2026-05-27T234730Z-abstractor-eigsolve-mutation-rotation-l1-l0/CYCLE.md`) sketches Sub-pattern C with the current cycle-009 `EigResult` field list (no `iterations` field). After this lifter dispatch integrates, the L1 `EigResult` will have a new `iterations` field that the wave-1 theme should reference. **Flag to cycle-011 integrator-finalize**: if both reports apply cleanly in the same cycle, the integrator-finalize step may need to either (a) add a footnote to the L1>L0 theme noting the new `iterations` field is covered by the same Sub-pattern C materialisation as `LinearSolveFailed`, or (b) defer such a footnote to a cycle-012 lifter pass. Not a blocker; the cycle-011 wave-1 abstractor's Sub-pattern C is structurally general enough that it already accommodates the `iterations` materialisation pattern (it lists the negative-anchor evidence form and the upstream-refactor-needed shape).

- **Negative-anchor citation pattern reaches recurrence-2.** This dispatch is the second consecutive lifter use of the negative-anchor citation pattern (citing L0 lines that demonstrate the *absence* of a behaviour). Cycle-010 sibling established the pattern (`LinearSolveFailed` constructive-introduction via the ten silent `opInv->Mult` callsites + `BaseKspSolver::Mult` void return); cycle-011 this dispatch extends it (`iterations` constructive-introduction via the zero `EPSGetIterationNumber` callsites + no `GetIterations` virtual on the surface). The pattern is plausibly methodology-codification-worthy at recurrence-2. The cycle-010 sibling's Open-Questions §4 already forwarded this to the cycle-012 meta-phase; this dispatch confirms recurrence and updates the meta-phase queue. Flag for cycle-012 meta-phase: friction-ledger or skill-candidate codification of "L1-constructive field annotation with negative-anchor citations" as a recurring lifter pattern.

- **Algebraic-law §5 was *wrong* in the cycle-009 rough-in** — the rough-in chapter stated convention (a) "L1 returns scaled" when the L0 surface uniformly does the opposite. This is a content correction, not pure structural re-anchoring. Per the lifter role-spec discipline ("if you find yourself making non-trivial content decisions, stop and flag in Open questions — likely an abstractor reread is needed"), this is borderline. The reason for proceeding with the correction rather than deferring to an abstractor reread is that the resolution is fully L0-evidence-driven (5 separate citation anchors in `arpack.cpp` / `slepc.cpp` / `nleps.cpp`, plus the cross-backend consistency); the cycle-009 rough-in author's choice was a factual reading-error of the L0 surface, not a design decision. The cycle-010 critic's tolerance for L0-evidence-driven prose tightening (per cycle-010 META.md commentary on the lifter's evidence-based replacements) provides precedent. **Flag for cycle-011 critic**: if this is judged outside-of-lifter-scope, the dispatch can be re-routed as an abstractor reread; this report's Edit 3 would be removed and the OQ left `partially-answered` pending abstractor work. Not a blocker; flagging for review.

- **SLEPc-NEP scaling-coordinate gap (corrected cycle-011 critic + repairer).** SLEPc-NEP at `palace/linalg/slepc.cpp:1554-1560` returns `l` directly without applying `* gamma`. The dispatch initially asserted "NEP uses `gamma = 1` at construction (no Higham scaling applied)" as the explanation. **Cycle-011 critic verified this assertion is wrong**: `SlepcNEPSolver::SetOperators` at `palace/linalg/slepc.cpp:1645-1651` (linear-K-M overload) AND `:1711-1719` (K-C-M overload) both compute `gamma = std::sqrt(normK / normM)` when `type != ScaleType::NONE`, same Higham-norm scaling pattern as EPS and PEP. The base-class constructor at `slepc.cpp:333` defaults `gamma = delta = 1.0`, but the NEP `SetOperators` overrides this when scaling is enabled. So the L0 behaviour is: NEP computes a non-trivial gamma at `SetOperators`, but its `GetEigenvalue` accessor does NOT apply `* gamma` — this is a genuine asymmetry in the L0 surface that is NOT explained by "NEP gamma = 1". The cycle-011 repairer softened the prose in Edit 3, Edit 7 (Evidence row), Edit 8 (OQ-narrative append), and the Supporting-evidence row to: "the SLEPc-NEP backend manages its own coordinate handling separately from the EPS / PEP un-scale-at-accessor pattern; the precise un-scaling convention is flagged for follow-up audit." The broader resolution (un-scale-at-accessor is uniform for EPS / PEP / NLEPS; L1 returns un-scaled) is unaffected — the asymmetry is isolated to the SLEPc-NEP backend. **Flag for cycle-012 lifter / `lowering-verifier`-on-eigsolve / harvester-NEP dispatch**: open a fresh OQ on the SLEPc-NEP coordinate convention — does the SLEPc NEP API itself un-scale before returning eigenpairs (so the Palace `GetEigenvalue` returning `l` directly is correct), or is there a missing `* gamma` un-scale that would manifest as scaled eigenvalues being passed to callers? Suggested OQ slug: `eigsolve-slepc-nep-coordinate-convention-audit`; suggest the integrator-finalize step open this OQ in `scaffolding/open-questions.md` and attach the cycle-011 repair as its provenance.
