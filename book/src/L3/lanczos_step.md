---
layer: L3
operator: lanczos_step
kind: kernel-impl-constituent
status: roadmap_goal
rank: roadmap_goal
edges:
  depends-on:
    - target: L3/krylov-step
      kind: specializes                 # lanczos_step IS krylov-step with the orthogonalization-variant axis collapsed to the symmetric band-3 (three-term) recurrence; same per-step shape, narrowed auxiliary stage (firm)
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
      kind: pulled-by                   # the sole consumer this cycle: the Hermitian basis-extension step of the constructive eigensolve fold
    - target: L1-L0/minres-iteration
      kind: cites-evidence              # the L1 rough-in row's home (MINRES obstruction theme, enum-only-stub); the symmetric-Lanczos kernel referenced there
    - target: semantics/index
variant_axes:
  - reorthogonalization (none = pure three-term recurrence / full = re-orthogonalize against all prior basis cols to combat loss-of-orthogonality / selective = Paige's criterion — informational; the band-3 recurrence is the unstable-but-cheap default)
  - matrix-pencil (standard = A only / generalized = (A, B)-inner-product Lanczos for EPS_GHEP — selects the inner product the orthogonality is measured in)
---

# lanczos_step

> **⟢ kernel-impl-constituent (DIRECTIVE-3).** The symmetric/Hermitian specialization of the per-step Krylov basis-extension body, constructed for the Hermitian arm of [`eigsolve-impl`](./eigsolve-impl.md) (`EPS_HEP` / `EPS_GHEP` pencils). Not a Palace-authored callable — the symmetric Lanczos recurrence is inside SLEPc/ARPACK; this is the from-our-primitives realization.

> **⟢ roadmap_goal (rank 0) — claim-free intent.** This chapter carries no positive Palace-source claim. It is the intent node for the symmetric three-term-recurrence basis-extension step the `L1/index.md:179` rough-in row names (from the MINRES `obstruction (enum-only-stub)` theme). Pulled by [`eigsolve-impl`](./eigsolve-impl.md) (the Hermitian basis-extension consumer). Promotes `roadmap_goal → stub → rough-in → firm` as it materializes against the symmetric-Lanczos L0 (MINRES) and a blocking consumer firms. Speculative reconstruction; not asserted as Palace source.

## Intent

What this becomes: a `firm` L3 operator `lanczos_step` — `krylov-step` with the `op.orthog` orthogonalization-variant axis **collapsed to the symmetric band-3 (three-term) recurrence**. Where Arnoldi (`krylov-step`'s non-Hermitian form) orthogonalizes the new basis column against ALL prior columns (full upper-Hessenberg `H`), the Hermitian case needs only the previous TWO columns — the projection onto the rest is zero by symmetry. This produces a **tridiagonal** `H` (the symmetric Lanczos `T` matrix), the structural saving the Hermitian eigensolve exploits.

## kernel-impl form (the constructive realization)

> **SPECULATIVE** — a reconstruction in our L3 vocabulary, composing only firm constituents.

Shape contract (the operator-domain shape group `S` per [`l4_calculus`](../semantics/index.md) §1.2.1–§1.2.2; `v_prev`, `v_curr`, `v_next` each `Tensor[(S: ...), complex]`; the recurrence coefficients `α_j, β_j` scalar):

    lanczos_step :: (A, v_prev, v_curr, β_prev) -> (v_next, α_j, β_j)
    -- A : the (shift-inverted) symmetric/Hermitian operator op.operand ▷ op.inv action (from eigsolve-impl's op)
    -- v_prev, v_curr : the previous two orthonormal basis columns BV[j-1], BV[j]
    -- β_prev : the prior off-diagonal coefficient (β_{j-1}); β_{-1} = 0 at the first step (first-iteration-unrolled)

    lanczos_step A v_prev v_curr β_prev =
      let w0  = apply_linop A v_curr                  -- symmetric operator-apply A·v_j
      let α_j = real (dot w0 v_curr)                  -- diagonal coeff α_j = ⟨A v_j, v_j⟩ (real for Hermitian A)
      let w1  = axpy (negate α_j) v_curr w0           -- w ← A v_j − α_j v_j
      let w   = axpy (negate β_prev) v_prev w1        -- w ← w − β_{j-1} v_{j-1}   (the THIRD term — band-3)
      let β_j = nrm2 w                                -- off-diagonal coeff β_j = ‖w‖
      let v_next = scal (1 / β_j) w                   -- normalize: v_{j+1} = w / β_j   (β_j = 0 ⇒ invariant subspace / breakdown)
      in (v_next, α_j, β_j)

This is **exactly [`krylov-step`](./krylov-step.md) with `op.orthog` = the band-3 form**: the kernel-api / `eigsolve-impl` per-step body `apply_shift_invert` produces `w0` (here `A` is the already-shift-inverted action `op.operand ▷ op.inv ▷ scale_untransform`), and the orthogonalize stage — which for full Arnoldi is MGS/CGS/CGS2 against all of `BV[0..j]` — collapses to the two `axpy` subtractions against `v_curr` and `v_prev` only. The `(α_j, β_j)` are the tridiagonal `T`-matrix entries `eigsolve-impl`'s Rayleigh-Ritz solves.

## Relationship to `krylov-step`

`lanczos_step` `specializes` [`krylov-step`](./krylov-step.md): same `(op, K, s) -> (K', ...)` per-step iteration-rotation shape, with two narrowings — (1) the orthogonalization-variant axis (`{MGS, CGS, CGS2}`) collapses to the symmetric band-3 recurrence (orthogonality against only the prior two columns, exact in infinite precision by Hermitian symmetry); (2) the recurrence coefficients `(α_j, β_j)` are the tridiagonal entries vs Arnoldi's full Hessenberg column. The L2 [`krylov-step`](../L2/krylov-step.md) note (`book/src/L2/krylov-step.md:187`) already records this: *"MINRES is the symmetric specialisation of `arnoldiStep`; its `lanczos_step` would specialise `krylov-step`'s orthogonalization-variant axis to a band-3 form."* This chapter is that specialization, constructed.

## Justification kind

`structural` — a shape-driven narrowing of the firm `krylov-step` per-step body. `reduction-chain` (secondary) — the three-term recurrence small-step is the content.

## Status

`roadmap_goal` (rank 0) — `kernel-impl-constituent` role. Claim-free intent node for the symmetric Lanczos basis-extension step. Rests on firm `L3/krylov-step` (specializes) + `L3/apply_linop` + `L1/dot` + `L1/nrm2` + `L1/axpy` + `L1/scal`. Pulled by [`eigsolve-impl`](./eigsolve-impl.md). Promotion: materialize against the symmetric-Lanczos L0 (the MINRES obstruction theme's literature-anchored form, `L1-L0/minres-iteration.md`) + a blocking consumer firms. The known-loss-of-orthogonality of the pure band-3 recurrence (the `reorthogonalization` variant axis) is the numerical caveat to resolve at firming.

## Evidence

> All Palace citations are to the symmetric-eigensolve sites the recurrence realizes (the library-owned Lanczos is inside SLEPc/ARPACK); NOT positive source for the reconstruction.

- `book/src/L3/krylov-step.md` (firm, cycle-010) — the operator this specializes; §Variant-axes axis 2 (orthogonalization-variant, the axis that collapses to band-3), §Semantics (the `op.orthog` auxiliary stage).
- `book/src/L2/krylov-step.md:187` — the standing note that `lanczos_step` specializes `krylov-step`'s orthogonalization axis to band-3 (the MINRES symmetric-specialization).
- `book/src/L1/index.md:179` — the `lanczos_step` rough-in dep-map row `(A, B?, V_prev, V_curr) → (V_next, alpha, beta)` (the signature this chapter realizes) + its constituent list `apply_linop, dot, axpy, nrm2`.
- `book/src/L1-L0/minres-iteration.md` — the MINRES `obstruction (enum-only-stub)` theme; the symmetric-Lanczos kernel home (the literature-anchored form the firming would draw on).
- `palace/linalg/slepc.cpp:607,613` — `EPS_HEP` / `EPS_GHEP`: the Hermitian / generalized-Hermitian problem types that select the symmetric Lanczos recurrence (the `matrix-pencil` variant axis).
- `book/src/L1/dot.md`, `book/src/L1/nrm2.md`, `book/src/L1/axpy.md`, `book/src/L1/scal.md` — the firm BLAS-1 constituents of the three-term update (`scal` is the normalize step `v_{j+1} = scal (1/β_j) w`).
- `book/src/semantics/index.md` §1.2.1–§1.2.2 — the named-shape-group convention; USED + linked.
