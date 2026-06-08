---
layer: L3
operator: lanczos_step
kind: kernel-impl-constituent
status: roadmap_goal
rank: roadmap_goal
edges:
  depends-on:
    - target: L3/krylov_step
      kind: specializes                 # lanczos_step IS krylov_step with the orthogonalization-variant axis collapsed to the symmetric band-3 (three-term) recurrence; same per-step shape, narrowed auxiliary stage (firm)
    - target: L3/apply_linop
      kind: composes                    # the symmetric operator-apply A·v_curr (firm)
    - target: L1/dot
      kind: composes                    # the diagonal recurrence coefficient α_j = ⟨A v_j, v_j⟩ (firm)
    - target: L1/nrm2
      kind: composes                    # the off-diagonal coefficient β_j = ‖w‖ (firm)
    - target: L1/axpy
      kind: composes                    # the three-term update w = A v_j − α_j v_j − β_{j-1} v_{j-1} (firm)
    - target: L1/scal
      kind: composes                    # the normalize step v_{j+1} = w / β_j = scal (1/β_j) w (firm)
  reference:
    - target: L3/eigsolve-impl
      kind: pulled-by                   # the sole consumer: the Hermitian basis-extension step of the constructive eigensolve fold
    - target: L1-L0/minres-iteration
      kind: cites-evidence              # the L1 rough-in row's home (MINRES obstruction theme, enum-only-stub); the symmetric-Lanczos kernel referenced there
    - target: semantics/index
variant_axes:
  - reorthogonalization (none = pure three-term recurrence / full = re-orthogonalize against all prior basis cols to combat loss-of-orthogonality / selective = Paige's criterion — informational; the band-3 recurrence is the unstable-but-cheap default)
  - matrix-pencil (standard = A only / generalized = (A, B)-inner-product Lanczos for EPS_GHEP — selects the inner product the orthogonality is measured in)
---

# lanczos_step

> **⟢ kernel-impl-constituent (DIRECTIVE-3).** The symmetric/Hermitian specialization of the per-step Krylov basis-extension body, constructed for the Hermitian arm of [`eigsolve-impl`](./eigsolve-impl.md) (`EPS_HEP` / `EPS_GHEP` pencils). Not a Palace-authored callable — the symmetric Lanczos recurrence is inside SLEPc/ARPACK; this is the from-our-primitives realization.

> **⟢ roadmap_goal (rank 0) — claim-free intent.** This chapter carries no positive Palace-source claim. It is the intent node for the symmetric three-term-recurrence basis-extension step the `L1/index.md:202` rough-in row names (from the MINRES `obstruction (enum-only-stub)` theme). Pulled by [`eigsolve-impl`](./eigsolve-impl.md) (the Hermitian basis-extension consumer). Promotes `roadmap_goal → stub → rough-in → firm` as it materializes against the symmetric-Lanczos L0 (MINRES) and a blocking consumer firms. Speculative reconstruction; not asserted as Palace source.

## Intent

What this becomes: a `firm` L3 operator `lanczos_step` — `krylov_step` with the `op.orthog` orthogonalization-variant axis **collapsed to the symmetric band-3 (three-term) recurrence**. Where Arnoldi (`krylov_step`'s non-Hermitian form) orthogonalizes the new basis column against ALL prior columns (full upper-Hessenberg `H`), the Hermitian case needs only the previous TWO columns — the projection onto the rest is zero by symmetry. This produces a **tridiagonal** `H` (the symmetric Lanczos `T` matrix), the structural saving the Hermitian eigensolve exploits.

## kernel-impl form (the constructive realization)

> **SPECULATIVE** — a reconstruction in our L3 vocabulary, composing only firm constituents.

Shape contract (the operator-domain shape group `S` per [`l4_calculus`](../semantics/index.md) §1.2.1–§1.2.2; the operator `A` carries the square operator-VALUE spelling `LinOp[(S: ...), $S]` of §1.2.2 / §1.2.2-R — a Hermitian operator on the basis-column domain `S`, the closed-over shift-invert action, NOT a bare type-application; `v_prev`, `v_curr`, `v_next` each `Tensor[(S: ...), complex]` congruent to that domain; the recurrence coefficients `α_j` real, `β_j` real-nonnegative; USED + linked, the convention is not restated here):

```text
lanczos_step :: LinOp[(S: ...), $S] -> Tensor[$S, complex] -> Tensor[$S, complex] -> RealScalar
             -> (Tensor[$S, complex], RealScalar, RealScalar)
-- positional: A v_prev v_curr β_prev -> (v_next, α_j, β_j)
-- A      : the (shift-inverted) symmetric/Hermitian operator — op.operand ▷ op.inv action from eigsolve-impl's op;
--          read-only across the step (closed-over !-tagged operator value per semantics §2 / §1.3.1).
-- v_prev, v_curr : the previous two orthonormal basis columns BV[j-1], BV[j].
-- β_prev : the prior off-diagonal coefficient β_{j-1} (real-nonnegative); β_{-1} = 0 at the first step (first-iteration-unrolled).

lanczos_step A v_prev v_curr β_prev =
  let w0  = apply_linop A v_curr                  -- symmetric operator-apply A·v_j
  let α_j = real (dot w0 v_curr)                  -- diagonal coeff α_j = ⟨A v_j, v_j⟩ (real for Hermitian A)
  let w1  = axpy (negate α_j) v_curr w0           -- w ← A v_j − α_j v_j
  let w   = axpy (negate β_prev) v_prev w1        -- w ← w − β_{j-1} v_{j-1}   (the THIRD term — band-3)
  let β_j = nrm2 w                                -- off-diagonal coeff β_j = ‖w‖
  let v_next = scal (1 / β_j) w                   -- normalize: v_{j+1} = w / β_j   (β_j = 0 ⇒ invariant subspace / breakdown)
  in (v_next, α_j, β_j)
```

This is **exactly [`krylov_step`](./krylov_step.md) with `op.orthog` = the band-3 form**: the kernel-api / `eigsolve-impl` per-step body `apply_shift_invert` produces `w0` (here `A` is the already-shift-inverted action `op.operand ▷ op.inv ▷ scale_untransform`), and the orthogonalize stage — which for full Arnoldi is MGS/CGS/CGS2 against all of `BV[0..j]` — collapses to the two `axpy` subtractions against `v_curr` and `v_prev` only. The `(α_j, β_j)` are the tridiagonal `T`-matrix entries `eigsolve-impl`'s Rayleigh-Ritz solves.

## Relationship to `krylov_step`

`lanczos_step` `specializes` [`krylov_step`](./krylov_step.md): same `(op, K, s) -> (K', ...)` per-step iteration-rotation shape, with two narrowings — (1) the orthogonalization-variant axis (`{MGS, CGS, CGS2}`) collapses to the symmetric band-3 recurrence (orthogonality against only the prior two columns, exact in infinite precision by Hermitian symmetry); (2) the recurrence coefficients `(α_j, β_j)` are the tridiagonal entries vs Arnoldi's full Hessenberg column. The L2 [`krylov_step`](../L2/krylov_step.md) note (`book/src/L2/krylov_step.md:187`) already records this: *"MINRES is the symmetric specialisation of `arnoldiStep`; its `lanczos_step` would specialise `krylov_step`'s orthogonalization-variant axis to a band-3 form."* The `L1/index.md:202` rough-in dep-map row carries the matching signature `(A, B?, V_prev, V_curr) → (V_next, alpha, beta)` (constituents `apply_linop, dot, axpy, nrm2`). This chapter is that specialization, constructed (band-3, with the normalize `scal` made explicit).

## Justification kind

`structural` — a shape-driven narrowing of the firm `krylov_step` per-step body. `reduction-chain` (secondary) — the three-term recurrence small-step is the content.

## Status

`roadmap_goal` (rank 0) — `kernel-impl-constituent` role. Claim-free intent node for the symmetric Lanczos basis-extension step. Rests on firm `L3/krylov_step` (specializes) + `L3/apply_linop` + `L1/dot` + `L1/nrm2` + `L1/axpy` + `L1/scal`. Pulled by [`eigsolve-impl`](./eigsolve-impl.md) (advancing this node fires that consumer's `roadmap_goal → stub` promotion condition).

**Why this STAYS `roadmap_goal` (the redirect-correct floor — a finding, not a failure).** There is **no positive Palace site** to ground it to `stub`/`rough-in`. The symmetric three-term recurrence is **literature-anchored** (Paige–Saunders 1975), NOT read from a Palace L0 implementation: its L0 home [`minres-iteration`](../L1-L0/minres-iteration.md) is an `obstruction (enum-only-stub)` with an **empty L0 RHS** — `KrylovSolver::MINRES` routes to `MFEM_ABORT` (`palace/linalg/ksp.cpp:53-57`), there is no `MinresSolver<OperType>` class under `palace/linalg/`, and no test linkage (`minres-iteration.md:41-59,128-140`). Per DIRECTIVE-3 (no constructive impl is manufactured into a positive claim absent a positive site) + the no-forced-rectangular-pull-up redirect, the node holds at `roadmap_goal`. The constructive band-3 form below is a **speculative reconstruction in our firm vocabulary**, not a Palace-source claim.

**Promotion gate (a conjunction; arm-1 currently UNSATISFIABLE in `palace/`).**
- **Arm A — positive structure** (`roadmap_goal → stub/rough-in`): EITHER (i) Palace gains an in-tree `MinresSolver`-shaped Lanczos kernel under `palace/linalg/iterative.cpp` (`minres-iteration.md:61-67`, route 1) — currently absent, so this arm cannot fire from the present `palace/` corpus; OR (ii) an integrator decision widens L0 to admit vendored MFEM `mfem::MINRESSolver` as L0 substrate (`minres-iteration.md:68-72`, route 2; MFEM not currently checked into `reference/`). Until one fires, arm A is **open by design** — this is the enum-only-stub obstruction floor, not a gap to force.
- **Arm B — blocking consumer** (`→ firm`): a blocking `depends-on` consumer firms `lanczos_step` by use — the Hermitian arm of [`eigsolve-impl`](./eigsolve-impl.md), itself reachable from the `feature/eigenmode.L4` root. Currently `eigsolve-impl` is co-`roadmap_goal`; arm B fires when that fold materializes (RE3 deflate / RE8 krylov-iteration consumers, `eigsolve-impl.md:122-125`).
- **Numerical caveat the firming must resolve.** The pure band-3 recurrence is the **unstable-but-cheap** default: it suffers known loss-of-orthogonality in finite precision (the `reorthogonalization` variant axis — `none` = pure three-term / `full` = re-orthogonalize against all prior BV columns / `selective` = Paige's criterion). The `matrix-pencil` axis (`standard` A-only vs `generalized` (A,B)-inner-product for `EPS_GHEP`) selects the inner product the orthogonality is measured in. Both axes are informational at `roadmap_goal`; a firm Lanczos kernel MUST pin a `reorthogonalization` policy (the band-3 alone is not numerically self-sufficient for a converged eigensolve).

## Evidence

> All Palace citations are to the symmetric-eigensolve sites the recurrence realizes (the library-owned Lanczos is inside SLEPc/ARPACK); NOT positive source for the reconstruction.

- `book/src/L3/krylov_step.md` (firm) — the operator this specializes; §Variant-axes axis 2 (orthogonalization-variant, the axis that collapses to band-3), §Semantics (the `op.orthog` auxiliary stage).
- `book/src/L2/krylov_step.md:187` — the standing note that `lanczos_step` specializes `krylov_step`'s orthogonalization axis to band-3 (the MINRES symmetric-specialization).
- `book/src/L1/index.md:202` — the `lanczos_step` rough-in dep-map row `(A, B?, V_prev, V_curr) → (V_next, alpha, beta)` (`rough-in (obstruction, …)`; the signature this chapter realizes) + its constituent list `apply_linop, dot, axpy, nrm2`.
- `book/src/L1-L0/minres-iteration.md` — the MINRES `obstruction (enum-only-stub)` theme; the symmetric-Lanczos kernel home (the literature-anchored form the firming would draw on).
- `palace/linalg/slepc.cpp:607,613` — `EPS_HEP` / `EPS_GHEP`: the Hermitian / generalized-Hermitian problem types that select the symmetric Lanczos recurrence (the `matrix-pencil` variant axis).
- `book/src/L1/dot.md`, `book/src/L1/nrm2.md`, `book/src/L1/axpy.md`, `book/src/L1/scal.md` — the firm BLAS-1 constituents of the three-term update (`scal` is the normalize step `v_{j+1} = scal (1/β_j) w`).
- `book/src/semantics/index.md` §1.2.1–§1.2.2 — the named-shape-group convention; USED + linked.
