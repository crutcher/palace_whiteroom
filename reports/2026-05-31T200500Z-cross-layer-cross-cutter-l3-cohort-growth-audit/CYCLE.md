---
agent: cross-layer-cross-cutter
invoked_at: 2026-05-31T200500Z
scope: L1↔L3 cross-cut — L3 cohort-growth verdict (settle the deferred audit at book/src/L3/index.md:38)
status: integrated
integrated_at: 2026-05-31T230000Z
integration_commit: 7efd86d2c8c032ec693419d161b03281ecd448cc
integration_notes: |
  Applied cycle-036 D2; observation-only audit that SETTLED the long-standing deferred-audit at book/src/L3/index.md:38. Single book edit at L3/index.md:38 (replaced the cohort-growth-candidates deferred bullet with the c036 verdict: 6 firm (A) identity-in-form L3-backfill candidates [assemble-diagonal, jacobi-smoother, reciprocal, elementwise_product, normalize, divfree-projector] + 2 L1-promotion-gated (A) [matrix-weighted-norm, bilinear-form] + 3 substantive (B) [orthogonalize, chebyshev-smoother, apply_nonlinear_pencil] + 7-operator (C) NEGATIVE LIST [lu_solve, back_solve, ls-update-column, 4 NLEPS atoms — disqualified by small-dense coordinate-space axis]). New OQ l3-cohort-growth-audit-c036-verdict filed (supersedes 2 predecessor OQs l3-vocabulary-inventory-gap + l3-backfill-apply-linop-and-blas1-cohort). The (C) negative-list is the new anti-recurrence data feed for the cycle-033-promoted verify-dispatch-scope-not-already-discharged skill. Migrated (A)+(B) candidates to priorities.md Backlog as cycle-037 active-head opener (the natural high-confidence batch-11 batch opener); recorded (C) negative-list prominently in priorities.md + integrator-signals.md. Build clean (~90s).
---

# CYCLE: Cross-layer observation — L3 cohort-growth verdict (settle the deferred audit at `book/src/L3/index.md:38`)

## Summary

The cohort-growth deferred-audit note at `book/src/L3/index.md:38` ("other operators in the krylov-step chain ... may also have identity-in-form rotations ... Audit deferred to a `cross-layer-cross-cutter`-scoped dispatch") has been carried since cycle-010 and is the root of repeated planner churn (c034 `krylov-step` was already firm; c035 `apply_linop` was already firm; c036 proposed `assemble-diagonal` without resolving whether it is genuinely identity-in-form, partial-obstruction, or non-L3-relevant). This audit settles it: classifying the 18 L1 operators (16 firm + 2 `rough-in`, the 2 rough-ins L1-promotion-gated at L3 per cycle-009 precedent) that lack an L3 entry against the L3 cohort definition (`book/src/L3/index.md:10-16` — whole-tensor field operations, field transitions, convolution-like patterns, with sequential obstructions as first-class outputs), producing **6 (A) firm + 2 (A) L1-promotion-gated** identity-in-form L3 backlog candidates, **3 (B)** substantive partial-obstruction/non-identity-rotation candidates, and **7 (C)** NOT-L3-relevant operators that should never be re-proposed. Crucially, `assemble-diagonal` is **(A)** — it is structurally identical to the firm-cycle-011 `apply_linop` precedent (opaque `LinearOperator[N,N]` in, fresh `Tensor[N]` out, no element loop exposed at L3 vocabulary); the exact-vs-approximate caveat is a representation-dependent **non-law** at L0, not a barrier to the L1↔L3 identity rotation. The four NLEPS atoms and the small-dense solves are (C) because they operate on `Vec[k]`/`Matrix[k,k]` small-coordinate-space dimensions and dense materialized values — no field axis, no global tensor-field semantics.

## Observation kind

**Coverage gap** — 6 firm L1 operators have a clear identity-in-form L3 entry waiting to be backfilled (the BLAS-1 precedent extends cleanly; 2 additional `rough-in` L1 operators are gated on L1 promotion to firm), 3 firm L1 operators have a substantive non-identity L3 entry waiting (with sequential-obstruction loops or representation-dependent body shapes), and the question of which of the 18 L1-without-L3 candidates are (A)/(B)/(C) has stayed open across 26+ cycles (`l3-vocabulary-inventory-gap` OQ never closed), driving stale-priorities recurrence in the cycle-planner. This audit closes the verdict so subsequent cycles dispatch only against genuinely-warranted L3 work.

## Specific finding

### Method (the cohort criterion)

Per `book/src/L3/index.md:10-16`, an operator belongs at L3 if its signature is one of:
- **Whole-tensor field operation** — primitive acting on whole tensors with no element loop exposed at the layer's vocabulary, L3-native by signature shape.
- **Field transition** — single-step state evolution `state' = f(state, params)`.
- **Convolution-like pattern** — stencil sweep, restriction/prolongation.
- **Sequential obstruction** — first-class output, body lifts but loop does not.

The discriminator across the firm L3 cohort:
- `apply_linop` (firm L3, `book/src/L3/apply_linop.md`) takes opaque `LinearOperator[M, N]` + `Tensor[N]`, returns `Tensor[M]` — an **opaque-operator gate** with whole-tensor argument is L3-native (`book/src/L3/index.md:22`).
- `krylov-step` (firm L3, `book/src/L3/krylov-step.md`) is the **field-transition** archetype (`book/src/L3/index.md:13`).
- `chebyshev` / `eigsolve` (firm L3 `partial-obstruction`, `book/src/L3/index.md:29, :31`) — body lifts to global tensor-field, loop is sequential-obstruction.
- `ksp_solve` (firm L3, `book/src/L3/index.md:30`) — outer-driver fold with sequential-obstruction explicitly rendered.

**Disqualifiers** (operands that break the L3 cohort):
- Operands of axis `k` where `k` is a **small dense coordinate space** (deflation rank / ROM basis size, single to low tens), not a field axis — these never belong at L3 (the L3 layer is the iteration rotation **of field-axis** operations; small-dense linear algebra in coordinate space is a different cost-model regime). Example: `Matrix[k, k]` dense materialized values.
- Operands that are **opaque structured solver values** parameterised over `k`-axis coordinates (e.g., `DeflationState[N, k]`, `ExtendedVec[N, k]`) — these are NEP-orchestration interior atoms whose L3 lift would be a category error (the NEP iteration is itself opaque at L3 via `eigsolve` `partial-obstruction`; its interior coordinate-space atoms are NOT separately L3-relevant — they were always interior to the `direct_newton` orchestration variant of `eigsolve`).

### Classification table

| # | L1 operator | L1 status | L1 signature shape | Classification | Rationale |
|---|---|---|---|---|---|
| 1 | `assemble-diagonal` | `firm` (`book/src/L1/assemble-diagonal.md:14-19`) | `(A: LinearOperator[N, N]) -> Tensor[N]` | **(A) identity-in-form** | Structurally identical to the firm-cycle-011 `apply_linop` precedent: opaque `LinearOperator` in, whole `Tensor` out, no element loop exposed at L3 vocabulary. The exact-vs-approximate caveat (`book/src/L1/assemble-diagonal.md:37` — matrix-free high-order Nedelec yields an approximate diagonal) is recorded as a **non-law** at L0 and lives in the L1>L0 representation-aware lowering, NOT in the L1 signature; identical-in-spirit to `apply_linop`'s representation-aware reduction-tree non-associativity recorded as an explicit non-law (`book/src/L3/apply_linop.md` — same opaque-operator-gate + representation-aware non-law pattern). L3 form is identity-in-form to L1 form. **The c036 planner proposal was correct in spirit but missed that this is the trivial BLAS-1-style extension.** |
| 2 | `reciprocal` | `firm` (`book/src/L1/reciprocal.md`) | `(x: Tensor[N]) -> Tensor[N]` | **(A) identity-in-form** | Pure elementwise self-map: `result[i] = 1/x[i]`. Same signature shape as the BLAS-1 cohort (whole-tensor in, whole-tensor out, no element loop at L3 vocabulary, no cross-element dependence). Reduction-free, rank-local. Identity-in-form at L3 is trivial. |
| 3 | `elementwise_product` | `firm` (`book/src/L1/elementwise_product.md`) | `(a: Tensor[N], b: Tensor[N]) -> Tensor[N]` | **(A) identity-in-form** | Pure elementwise binary map: `result[i] = a[i] · b[i]`. Same signature shape as the BLAS-1 cohort (whole-tensor in, whole-tensor out, no element loop, element-local). Reduction-free, rank-local. Identity-in-form at L3 is trivial — the L3 form is exactly the Hadamard `a ⊙ b`. |
| 4 | `normalize` | `firm` (`book/src/L1/normalize.md:17`) | `(x: Tensor[N]) -> (Scalar, Tensor[N])` | **(A) identity-in-form** | Fused `nrm2 + scal(1/nrm2, ·)`, both constituents already firm at L3. Whole-tensor in, paired output (`Scalar` + `Tensor[N]`); no element loop exposed. Identity-in-form: the L3 form is identical to the L1 form modulo the partiality precondition at `x = 0` (the partiality is a property of the algebraic form, not a rotation barrier). |
| 5 | `divfree-projector` | `firm` (`book/src/L1/divfree-projector.md`) | `(P: DivFreeProjector[N_nd, N_h1], y: Field[N_nd]) -> Field[N_nd]` | **(A) identity-in-form** | **Constructed-operator gate**, same family as the firm-cycle-020 `ksp_solve` at L3. Whole-tensor in, whole-tensor out; the inner H1-side `ksp_solve` is a recursive L3 vocabulary call (firm at L3), not an exposed element loop. The L3 form is identity-in-form to the L1 form — the projector is a fixed linear map on the field argument; **the inner ksp_solve's own loop obstruction is already captured at L3** (`book/src/L3/ksp_solve.md`), so this projector itself does not introduce a new L3 obstruction. The H1 scratch buffers `psi`, `rhs` are L0 concerns. |
| 6 | `chebyshev-smoother` | `firm` (`book/src/L1/chebyshev-smoother.md`) | `(op: ChebSmoother[N], x, y, initial_guess) -> y'` | **(B) partial-obstruction** | The L3 `chebyshev` already exists at `book/src/L3/chebyshev.md` (cycle-013, `partial-obstruction`) — this is the **same operator** at a slightly different L1 surface (smoother wrapper vs. inner polynomial). The `chebyshev-smoother` body uses the inner polynomial that is the firm L3 `chebyshev` operator. The L3 entry for the smoother (if landed) is the wrapper around the existing L3 `chebyshev` — possibly identity-in-form modulo the smoother wrapper. **AUDIT FINDING**: this candidate may **already be subsumed** by the firm L3 `chebyshev` row, which lists `chebyshev-iteration` (L2) / `chebyshev-smoother` (L1) as its lift sources at `book/src/L3/chebyshev.md` (via the in-line L3-L1 identity annotation). If subsumed, classification collapses to (C); if not subsumed (because the smoother's `pc_it` Richardson outer sweep is a separate level of obstruction), it lands as a second `partial-obstruction` row. **Recommendation**: defer to a single harvester invocation that checks the L3 `chebyshev` row's coverage of `chebyshev-smoother`; backfill only if there is a genuine gap. |
| 7 | `jacobi-smoother` | `firm` (`book/src/L1/jacobi-smoother.md`) | `(op: JacobiSmoother[N], x: Tensor[N]) -> Tensor[N]` | **(A) identity-in-form** | The thinnest constructed-operator gate at L1: **one elementwise product**, no sweep, no workspace (`book/src/L1/jacobi-smoother.md:8,32-34,312-313`). Per-call action is `y = (ω · D⁻¹) ⊙ x` — a single `elementwise_product` of the construction-bound `dinv` against `x`. Whole-tensor in, whole-tensor out; no element loop, no inner solve, no sequential obstruction. Identity-in-form at L3 is trivial — the constructed-operator gate pattern is the precedent set by `apply_linop` / `ksp_solve` / `eigsolve` at L3. |
| 8 | `orthogonalize` | `firm` (`book/src/L1/orthogonalize.md`) | `(w: Tensor[N], V: Basis[N, m], variant) -> (Tensor[N], Tensor[m])` | **(B) partial-obstruction** | **EXPLICITLY MARKED** by the L1 entry as carrying a sequential-obstruction at L3 on the MGS variant (`book/src/L1/orthogonalize.md` Dependencies §: "MGS has no global tensor-field form; CGS/CGS2 lift cleanly"). The CGS/CGS2 variants lift identity-in-form to whole-tensor at L3 (a `gemv`-style basis projection plus an `axpy` reduction); the MGS variant is a witnessed sequential-obstruction. This is exactly the body-lifts-loop-doesn't `partial-obstruction` shape — like `chebyshev` (numerical-stability obstruction) but variant-axis-conditional (an MGS-only obstruction; CGS/CGS2 are clean lifts). Substantive harvester work is needed to land it with the MGS-variant obstruction made explicit. |
| 9 | `matrix-weighted-norm` | `rough-in (test-coverage-bounded)` (`book/src/L1/matrix-weighted-norm.md`) | `(x: Tensor[N], B: LinearOperator[N, N]) -> Scalar` | **(A) identity-in-form** (but **gated by L1 promotion to firm**) | Reduction primitive of shape `Tensor[N] × LinearOperator[N, N] -> Scalar`, structurally a generalisation of the firm `nrm2` (`Tensor[N] -> Scalar`) and `dot` (`Tensor[N] × Tensor[N] -> Scalar`) — both at L3 as identity-in-form. No element loop, no sequential dependence, no representation-dependent body — the inner `apply_linop` is itself firm at L3. Identity-in-form at L3 is trivial. **BUT** the L1 entry is `rough-in (test-coverage-bounded)` — per the cycle-009 meta-phase precedent it should not be backfilled at L3 until L1 promotes to firm (the same gate that holds `bilinear-form` below). **Recommendation**: track but DO NOT dispatch the L3 backfill until the L1 entry promotes; the L3 dispatch should ride the same promotion cycle. |
| 10 | `bilinear-form` | `rough-in (lower-layer-shared-vocabulary)` (`book/src/L1/bilinear-form.md`) | (matrix-weighted dot) | **(A) identity-in-form** (but **gated by L1 promotion to firm**) | Same shape as `matrix-weighted-norm` — structurally a generalisation of the firm `dot`. Identity-in-form at L3 is trivial when L1 promotes. **Recommendation**: same as `matrix-weighted-norm` — track, do not dispatch until L1 promotes. |
| 11 | `lu_solve` | `firm` (`book/src/L1/lu_solve.md:71-78`) | `(A: Matrix[k, k], b: Tensor[k]) -> Tensor[k]` **OR** `(A: Matrix[k, k], B: Matrix[k, m]) -> Matrix[k, m]` | **(C) NOT L3-relevant** | Small-dense direct solve on `Matrix[k, k]` materialized dense matrix where `k` is the **deflation rank or ROM basis size** (single to low tens — `book/src/L1/lu_solve.md:29` "The axis `k` is the small coordinate dimension ... **not** the large field dimension `N` of `apply_linop` / `ksp_solve`"). The L3 cohort is the iteration rotation of **field-axis whole-tensor** operations; small-dense coordinate-space linear algebra is a categorically different cost-model regime (`ksp_solve` is iterative-to-tolerance and opaque about its inner method; `lu_solve` is a finite direct solve on a materialized dense matrix). Putting `lu_solve` at L3 would require admitting `Matrix[k, k]` as an L3 type, which contradicts the L3 cohort definition ("global tensor-field operations" `book/src/L3/index.md:3`). **DO NOT RE-PROPOSE.** |
| 12 | `back_solve` | `firm` (`book/src/L1/back_solve.md`) | `(R: UpperTriangular[k+1, k+1], s: Tensor[k+1]) -> Tensor[k+1]` | **(C) NOT L3-relevant** | Same disqualifier as `lu_solve`: small-dense triangular back-solve where the axis is the GMRES restart-cycle dimension (single to low hundreds at most), NOT the field axis. The GMRES restart-cycle close at `book/src/L1/back_solve.md` Context: "the terminal step of the running-QR least-squares update". It is the per-cycle terminal of an iteration that the firm L3 `ksp_solve` outer-driver fold already captures opaquely — exposing `back_solve` at L3 would re-expose interior coordinate-space algebra that L3 collapses into the outer-driver. **DO NOT RE-PROPOSE.** |
| 13 | `ls-update-column` | `firm` (`book/src/L1/ls-update-column.md`) | `(K, j, h_new) -> K'` | **(C) NOT L3-relevant** | Same disqualifier: per-column running-QR update on the GMRES restart-cycle small-coordinate axis. It is the per-column producer of the running R-factor and rotated RHS — interior to the firm L3 `ksp_solve` outer-driver fold. Re-exposing it at L3 would be a category error (the iteration rotation of GMRES is **already** captured by the firm `ksp_solve` `sequential-obstruction`-with-explicit-rendering pattern). **DO NOT RE-PROPOSE.** |
| 14 | `apply_nonlinear_pencil` | `firm` (`book/src/L1/apply_nonlinear_pencil.md:22-23`) | `(T: NonlinearPencil[N], λ: Complex, v: Tensor[N]) -> Tensor[N]` | **(B) partial-obstruction** *OR* **(C) NOT L3-relevant** (defer to NEP-orchestration question) | Whole-tensor in, whole-tensor out signature — superficially a (A) candidate. BUT it is **the interior atom of the NEP Newton orchestration** (`book/src/L1/apply_nonlinear_pencil.md:17` "This operator is the **interior** of the `eigsolve` gate, not a competitor to it"); the NEP iteration is already opaque at L3 via the firm `eigsolve` `partial-obstruction` (`book/src/L3/eigsolve.md`, c024 — opaque-library-ownership for SLEPc/ARPACK, but `direct_newton` Palace-authored variant exists). The L3 question is whether the **NEP per-Newton-step body** lifts to a global tensor-field form when `direct_newton` is the orchestration variant — that would be a `partial-obstruction` whose body is `apply_nonlinear_pencil` and whose loop is the Newton-Armijo iteration. **Recommendation**: this is NOT a quick identity-in-form backfill. It belongs to a future substantive harvester pass on the L3 `eigsolve` `direct_newton` variant detail (which the current `book/src/L3/eigsolve.md` collapses opaquely). Until then, track as (B) candidate but do not dispatch as a separate L3 row — fold into the eigsolve-variant deepening when planned. |
| 15 | `nleps_deflated_residual` | `firm` (`book/src/L1/nleps_deflated_residual.md`) | `(T, λ, P: DeflationState[N, k], vv: Tensor[N], vv₂: Vec[k]) -> DeflatedResidual[N, k]` | **(C) NOT L3-relevant** | The signature mixes a field-axis tensor (`vv : Tensor[N]`) with a small-dense coordinate-axis tensor (`vv₂ : Vec[k]`, `k` = deflation rank). The output `DeflatedResidual[N, k]` has a `Vec[k]` coordinate-space component. Per the disqualifier above, mixed `(N, k)` operands carrying a small-dense coordinate-space axis are NEP-orchestration interior atoms (`book/src/L1/nleps_deflated_residual.md:11` Context: "interior of the `eigsolve` gate's `direct_newton` orchestration variant"); they are interior to the eigsolve `partial-obstruction` and DO NOT separately belong at L3. **DO NOT RE-PROPOSE.** |
| 16 | `nleps_deflated_solve` | `firm` (`book/src/L1/nleps_deflated_solve.md`) | `(K, P: DeflationState[N, k], λ, b1, b2: Vec[k]) -> DeflatedSolution[N, k]` | **(C) NOT L3-relevant** | Same disqualifier: mixed `(N, k)` operands with small-dense coordinate-space axis. NEP-orchestration interior atom. **DO NOT RE-PROPOSE.** |
| 17 | `nleps_jacobian_action` | `firm` (`book/src/L1/nleps_jacobian_action.md`) | `(T, λ, P: DeflationState[N, k], v: Tensor[N], v₂: Vec[k]) -> Tensor[N]` | **(C) NOT L3-relevant** | Same disqualifier. **DO NOT RE-PROPOSE.** |
| 18 | `nleps_eigenvalue_correction` | `firm` (`book/src/L1/nleps_eigenvalue_correction.md`) | `(resid: ExtendedVec[N, k], jac_action, proj_dir: ExtendedVec[N, k]) -> NewtonStep[N, k]` | **(C) NOT L3-relevant** | Same disqualifier — even more so: the output `NewtonStep[N, k]` carries `δλ : Complex` (scalar!) and `z2 : Vec[k]` (coordinate-space). The big-space `z : Tensor[N]` is a single `axpby` — but the whole operator is a small-coordinate-space algebraic atom interior to the NEP Newton step. **DO NOT RE-PROPOSE.** |

### Summary

- **(A) Identity-in-form L3 backfill candidates — 6 firm** (excluding 2 L1-promotion-gated):
  - `assemble-diagonal` (the c036 question — verdict: YES, it's the trivial extension; **closes the c036 question**)
  - `reciprocal` (elementwise self-map)
  - `elementwise_product` (elementwise binary map)
  - `normalize` (fused `nrm2 + scal`)
  - `divfree-projector` (constructed-operator gate, like `ksp_solve`)
  - `jacobi-smoother` (thinnest constructed-operator gate)

- **(A) gated by L1 promotion to firm — 2** (do NOT dispatch until L1 promotes):
  - `matrix-weighted-norm` (`rough-in (test-coverage-bounded)` at L1)
  - `bilinear-form` (`rough-in (lower-layer-shared-vocabulary)` at L1)

- **(B) Substantive partial-obstruction / non-identity-rotation candidates — 3** (need substantive harvester pass, NOT a quick backfill):
  - `orthogonalize` (MGS variant has sequential-obstruction; CGS/CGS2 lift cleanly)
  - `chebyshev-smoother` (POSSIBLY subsumed by existing L3 `chebyshev`; needs subsumption check first)
  - `apply_nonlinear_pencil` (interior to `eigsolve` `direct_newton` variant; fold into eigsolve-variant deepening, not a separate L3 row)

- **(C) NOT L3-relevant — 7** (DO NOT re-propose):
  - `lu_solve` (small-dense `Matrix[k, k]`)
  - `back_solve` (small-dense GMRES restart-cycle)
  - `ls-update-column` (per-column running-QR, GMRES restart-cycle interior)
  - `nleps_deflated_residual` (mixed `(N, k)`, NEP-orchestration interior)
  - `nleps_deflated_solve` (mixed `(N, k)`, NEP-orchestration interior)
  - `nleps_jacobian_action` (mixed `(N, k)`, NEP-orchestration interior)
  - `nleps_eigenvalue_correction` (mixed `(N, k)` + `Complex` scalar, NEP-orchestration interior)

The disqualifier criterion (small-dense coordinate-space axis OR mixed `(N, k)` interior-to-already-firm-`partial-obstruction`) is the load-bearing distinction. Any future cycle that proposes an L3 backfill for one of these 7 operators is **stale**.

## Recommendation

1. **Dispatch harvester on `book/src/L3/assemble-diagonal.md`** as the **next high-priority** L3 backfill (closes the c036 question this audit was originally chartered against; trivial identity-in-form rotation per the firm-cycle-011 `apply_linop` precedent). Estimated ~200-300 line entry; signature transcription + identity-in-form annotation + dep-map row addition.

2. **Subsequent harvester backfills** (medium-priority, in fan-out-utility order — each ~150-300 lines):
   - `book/src/L3/jacobi-smoother.md` (single `elementwise_product`; trivially identity-in-form)
   - `book/src/L3/reciprocal.md` (elementwise self-map)
   - `book/src/L3/elementwise_product.md` (Hadamard binary)
   - `book/src/L3/normalize.md` (fused `nrm2 + scal`)
   - `book/src/L3/divfree-projector.md` (constructed-operator gate; calls firm-L3 `ksp_solve` internally)

3. **Substantive (B) harvester passes** (NOT quick backfills — deferred until plan can budget the work):
   - `book/src/L3/orthogonalize.md` with MGS sequential-obstruction made explicit (third `partial-obstruction` row at L3 after `chebyshev` / `eigsolve`).
   - `book/src/L3/chebyshev-smoother.md` only after a subsumption check against the existing `book/src/L3/chebyshev.md` confirms a genuine gap.
   - `apply_nonlinear_pencil` deferred to a future eigsolve-variant deepening (not a standalone L3 row).

4. **L1-promotion-gated** (track but DO NOT dispatch L3 work until L1 promotes):
   - `matrix-weighted-norm`, `bilinear-form` — ride the same L1 promotion cycle.

5. **Update the deferred-audit note** at `book/src/L3/index.md:38` to record this audit's verdict (see proposed-changes block below) — so the cohort-growth question stops generating planner churn.

## Supporting evidence

- L3 cohort definition: `book/src/L3/index.md:10-16`
- Deferred-audit note: `book/src/L3/index.md:38`
- Firm L3 cohort precedent (BLAS-1 identity rotations): `book/src/L3/index.md:22-28` (apply_linop, axpy, axpby, axpbypcz, dot, nrm2, scal)
- Firm L3 `partial-obstruction` precedent: `book/src/L3/index.md:29` (chebyshev — numerical-stability obstruction) and `:31` (eigsolve — opaque-library-ownership obstruction)
- `assemble-diagonal` L1 entry (signature + exact-vs-approximate caveat): `book/src/L1/assemble-diagonal.md:14-19, :37`
- `apply_linop` L3 entry (opaque-operator precedent for `assemble-diagonal`): `book/src/L3/apply_linop.md`
- `reciprocal`, `elementwise_product`, `normalize` L1 status: `book/src/L1/reciprocal.md` Status §; `book/src/L1/elementwise_product.md` Status §; `book/src/L1/normalize.md` Status §
- `divfree-projector` L1 (constructed-operator gate + inner ksp_solve): `book/src/L1/divfree-projector.md` (signature + dependency on `ksp_solve`)
- `jacobi-smoother` L1 (thinnest constructed-operator gate, one `elementwise_product`): `book/src/L1/jacobi-smoother.md:8,32-34,312-313`
- `orthogonalize` L1 (MGS sequential-obstruction at L3 explicitly noted): `book/src/L1/orthogonalize.md` Variant axes § / Dependencies § ("MGS has no global tensor-field form; CGS/CGS2 lift cleanly")
- `matrix-weighted-norm` L1 status `rough-in (test-coverage-bounded)`: `book/src/L1/matrix-weighted-norm.md` Status §
- `bilinear-form` L1 status `rough-in (lower-layer-shared-vocabulary)`: `book/src/L1/bilinear-form.md` Status §
- `lu_solve` L1 (small-dense `k`-axis, distinct from large field `N`): `book/src/L1/lu_solve.md:29`
- `back_solve` L1 (GMRES restart-cycle small-coordinate): `book/src/L1/back_solve.md` Context §
- `ls-update-column` L1 (per-column GMRES interior): `book/src/L1/ls-update-column.md` Context §
- NLEPS atoms as eigsolve-orchestration interior: `book/src/L1/apply_nonlinear_pencil.md:17` (signature at `:22-23`), `book/src/L1/nleps_deflated_residual.md:11`, `book/src/L1/nleps_deflated_solve.md`, `book/src/L1/nleps_jacobian_action.md`, `book/src/L1/nleps_eigenvalue_correction.md`
- Cycle-021 OQ predicting L3-eigsolve no-krylov-step-kernel-analog: `book/src/L3/index.md:31` (enacted cycle-024)

## Proposed changes

The following edit to `book/src/L3/index.md:38` records this audit's verdict so the deferred-audit note stops being a recurrent planner-churn source. Apply ONLY this edit (no other file mutations).

```proposed-changes
file: book/src/L3/index.md
operation: replace
context: the "Cohort growth candidates" working-note bullet at line 38

old:
- **Cohort growth candidates** (per priority #20 cross-layer-cross-cutter audit, cycle-010+): other operators in the krylov-step chain (`apply_linop`, `dot`, `axpy`, `nrm2`, etc.) may also have identity-in-form rotations between adjacent layers that warrant L3 backfill. Audit deferred to a `cross-layer-cross-cutter`-scoped dispatch surveying the L4/L3/L2/L1 cohorts.

new:
- **Cohort growth candidates audit (cycle-036, SETTLED)**: the cycle-010 deferred audit ran as cycle-036 dispatch D2 cross-layer-cross-cutter on the L3-cohort-growth frontier (`reports/2026-05-31T200500Z-cross-layer-cross-cutter-l3-cohort-growth-audit/CYCLE.md`). Verdict against the 18 L1 operators (16 firm + 2 `rough-in`, the 2 rough-ins L1-promotion-gated at L3 per cycle-009 precedent) that lack an L3 entry, classified by the L3 cohort criterion (whole-tensor field operations / field transitions / convolution-like patterns / sequential obstructions as first-class outputs, per `book/src/L3/index.md:10-16`):
  - **(A) Identity-in-form L3 backfill candidates — 6 firm**: `assemble-diagonal` (the c036 question; verdict YES — structurally identical to the firm `apply_linop` opaque-operator-gate precedent, with the exact-vs-approximate caveat absorbed as a representation-aware L1>L0 non-law), `reciprocal` (elementwise self-map), `elementwise_product` (Hadamard binary), `normalize` (fused `nrm2 + scal`), `divfree-projector` (constructed-operator gate, like firm-L3 `ksp_solve`), `jacobi-smoother` (thinnest constructed-operator gate, one `elementwise_product`).
  - **(A) L1-promotion-gated — 2**: `matrix-weighted-norm` and `bilinear-form` — both `rough-in` at L1; do NOT dispatch L3 work until L1 promotes (ride the same promotion cycle, cycle-009 meta-phase precedent).
  - **(B) Substantive partial-obstruction / non-identity-rotation — 3** (NOT quick backfills): `orthogonalize` (MGS variant has sequential-obstruction at L3 explicitly noted at L1; CGS/CGS2 variants lift cleanly — would be a third `partial-obstruction` row after `chebyshev` and `eigsolve`); `chebyshev-smoother` (possibly subsumed by the existing firm L3 `chebyshev` row — requires a subsumption check first); `apply_nonlinear_pencil` (interior to the `eigsolve` `direct_newton` variant; fold into a future eigsolve-variant deepening pass, NOT a separate L3 row).
  - **(C) NOT L3-relevant — 7** (DO NOT re-propose): `lu_solve` (small-dense `Matrix[k, k]` coordinate-space — `book/src/L1/lu_solve.md:29`), `back_solve` (GMRES restart-cycle small-coordinate), `ls-update-column` (per-column running-QR, GMRES restart-cycle interior to firm-L3 `ksp_solve`), the four NLEPS atoms (`nleps_deflated_residual`, `nleps_deflated_solve`, `nleps_jacobian_action`, `nleps_eigenvalue_correction` — all mixed `(N, k)` operands carrying small-dense coordinate-space axes, interior to the firm-L3 `eigsolve` `partial-obstruction`). The disqualifier criterion is: **small-dense coordinate-space axis** (deflation rank / ROM basis size / GMRES restart-cycle, single to low hundreds at most), NOT the field axis `N`. The L3 cohort is the iteration rotation of field-axis operations; small-dense coordinate-space linear algebra is a categorically different cost-model regime that L3 absorbs opaquely into already-firm outer-driver folds (`ksp_solve`) or `partial-obstruction` markers (`eigsolve`).
  Six (A) firm backfills are routed to cycles 036-038+ planner under OQ `l3-cohort-growth-audit-c036-verdict` (which the integrator-per-report appends to `scaffolding/open-questions.md`, retiring the older `l3-vocabulary-inventory-gap` and `l3-backfill-apply-linop-and-blas1-cohort` OQs as superseded by this verdict). The seven (C) operators are recorded here as a NEGATIVE LIST — any future planner proposal for these is STALE and should be rejected.
```

## Open questions / caveats

- **`chebyshev-smoother` subsumption check** — the verdict places it in (B) pending a subsumption check against the existing firm L3 `chebyshev` row. The c013 L3 `chebyshev` entry lists `chebyshev-smoother` as a lift source (`book/src/L3/index.md:29`); whether that subsumes the smoother's `pc_it` Richardson outer sweep is unclear from this audit alone. If the firm L3 `chebyshev` row already captures the smoother (no separate gap), `chebyshev-smoother` collapses to (C) for "subsumed by existing L3 entry". A harvester half-day on `book/src/L3/chebyshev.md` checking the smoother coverage would settle this; recommended as low-priority follow-up.

- **`apply_nonlinear_pencil` routing through eigsolve-variant deepening** — the verdict treats it as (B) folded into a future eigsolve-variant deepening pass rather than a standalone L3 row. This is consistent with the cycle-024 eigsolve `partial-obstruction` framing (opaque-library-ownership for SLEPc/ARPACK), but the `direct_newton` Palace-authored variant is NOT fully exposed at L3 (the c024 entry collapses all three variants opaquely). A future eigsolve-variant deepening cycle should decide whether the `direct_newton` body deserves its own L3 row (in which case `apply_nonlinear_pencil` is the interior atom and may or may not need a separate L3 entry).

- **`divfree-projector` inner-ksp_solve interaction at L3** — the (A) classification assumes the inner `ksp_solve` is referenced as a firm-L3-vocabulary call rather than inlined. This is the same pattern as `eigsolve`'s body composing `ksp_solve(op.inv)` (firm L3 cycle-024). Confirmed correct by precedent; no follow-up needed.

- **Matrix-weighted-norm / bilinear-form promotion dependency** — both L1-promotion-gated entries are blocked by the `test-coverage-bounded` qualifier. Their L1 promotion is itself blocked because no `test-eigen*.cpp` or `test-operator*.cpp` exercises the SPD-weighted overload (per `book/src/L1/matrix-weighted-norm.md` Status §). This is a longer-horizon promotion that requires expanded literature anchoring (per cycle-021 codification of `rough-in (test-coverage-bounded)`); the L3 dispatch should ride that promotion when it lands.

- **Cycle-planner stale-priorities mitigation** — this audit's intended downstream effect is to give the c037+ planner a definitive negative list (the 7 (C) operators) so it stops re-proposing them. The friction-ledger `cycle-planner-stale-priorities-line-recruitment` recurrence-3 enacted cycle-033 meta-phase is the matching mitigation; this audit's (C) negative-verdict list is the data the new `verify-dispatch-scope-not-already-discharged` skill needs to consult.

- **OQ-ledger migration (FOR INTEGRATOR-PER-REPORT)** — the proposed-changes payload asserts retirement of two existing OQ IDs and creation of a new one. The actual `scaffolding/open-questions.md` surgical edits are downstream of this dispatch's write authority and should be enacted by `integrator-per-report` (which holds open-questions.md append authority per the role-spec partition). Mechanical edits required at integration:
  1. **Append (new OQ)**: `l3-cohort-growth-audit-c036-verdict` — "Six (A) firm L3 backfills identified by cycle-036 D2 cross-layer audit (`reports/2026-05-31T200500Z-cross-layer-cross-cutter-l3-cohort-growth-audit/`): `assemble-diagonal`, `reciprocal`, `elementwise_product`, `normalize`, `divfree-projector`, `jacobi-smoother`. Two additional (A) L1-promotion-gated: `matrix-weighted-norm`, `bilinear-form`. Three (B) substantive: `orthogonalize`, `chebyshev-smoother`, `apply_nonlinear_pencil`. Seven (C) negative-list (DO NOT re-propose): `lu_solve`, `back_solve`, `ls-update-column`, `nleps_deflated_residual`, `nleps_deflated_solve`, `nleps_jacobian_action`, `nleps_eigenvalue_correction`."
  2. **Mark as superseded / closed**: `l3-vocabulary-inventory-gap` (superseded by `l3-cohort-growth-audit-c036-verdict`).
  3. **Mark as superseded / closed**: `l3-backfill-apply-linop-and-blas1-cohort` (superseded by `l3-cohort-growth-audit-c036-verdict`).

- **CYCLE.md filename** — written directly as `CYCLE.md` per the cycle-004 rename (CLAUDE.md "REPORT.md → CYCLE.md to bypass the Claude Code subagent Write filter on `report|summary|findings|analysis` filenames"); no Write filter encountered during this dispatch.
