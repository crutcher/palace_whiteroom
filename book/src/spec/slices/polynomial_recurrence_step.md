# Polynomial recurrence step

## Context

This slice was opened by a scope question asking whether Palace has a named, shared `polynomial_recurrence_step` kernel across (i) Chebyshev smoothers, (ii) GMRES restart cycles, and (iii) LOBPCG / eigenvalue tracking. The empirical answer is **no**. This slice exists as a **negative-result catalog**: a structured record of three independent per-step scalar-update sequences and one out-of-scope (Palace-boundary obstruction) site, with explicit non-unification noted.

The slice's value is in cataloging what the source DOES carry — a file-local pair of fused-update helpers in `chebyshev.cpp` shared between 4th-kind and 1st-kind Chebyshev — and what it does NOT carry: a shared scalar-coefficient generator, a shared outer driver across Chebyshev/GMRES, and any Palace-level eigenvalue-tracking kernel at all.

## Background

The textbook view (e.g., Saad 2003 ch. 12 for polynomial smoothing; Phillips & Fischer 2022 §3 for the 4th-kind Chebyshev recurrence; Saad 2003 ch. 6.5 for restarted GMRES) suggests a family of polynomial / Krylov iterations that share a *shape*: maintain a small running scalar state, generate per-step coefficients from a recurrence over that state, and apply those coefficients to a fused vector update. The shape suggests unification.

Palace does **not** realize that shape as a shared kernel. Each concrete solver inlines its own scalar-coefficient generator inside its `Mult` / `Mult2` body. The polynomial families involved (1st-kind Chebyshev, 4th-kind Chebyshev) and the Krylov family (GMRES with Givens) have genuinely different scalar-state shapes — the only thing they share is the meta-shape "a scalar recurrence drives a fused vector update."

## L0

### Chebyshev fused-update helpers (file-local, shared between 1st-kind and 4th-kind)

Two anonymous-namespace inlines in `chebyshev.cpp` factor the vector-update half of the per-step kernel:

- `ApplyOrder0(sr, dinv, r, d)` — pure overwrite `d := sr · (dinv ⊙ r)`. Two overloads: real `Vector` and `ComplexVector`. Citation: [palace/linalg/chebyshev.cpp:63-92](../../../../reference/palace/linalg/chebyshev.cpp#L63-L92).
- `ApplyOrderK<Transpose=false>(sd, sr, dinv, r, d)` — accumulator update `d := sd·d + sr·(dinv ⊙ r)`. Two overloads (real, complex); the `Transpose` template flag affects the complex conjugation pattern only. Citation: [palace/linalg/chebyshev.cpp:113-155](../../../../reference/palace/linalg/chebyshev.cpp#L113-L155).

Both helpers are `static` in an anonymous namespace, not exported. They are the named per-step **vector-update** kernel of the polynomial recurrence; they do NOT encapsulate scalar-coefficient generation.

### Chebyshev scalar-coefficient sequences (inlined per variant; not unified)

The per-step scalar pair `(sd_k, sr_k)` is generated INLINE inside each `Mult2` body:

- **4th-kind** (`ChebyshevSmoother::Mult2`, [palace/linalg/chebyshev.cpp:191-220](../../../../reference/palace/linalg/chebyshev.cpp#L191-L220)): `sd = (2k-1)/(2k+3)`, `sr = (8k+4)/((2k+3) · lambda_max)`. State: `lambda_max` (persisted on smoother) plus loop index `k`.
- **1st-kind** (`ChebyshevSmoother1stKind::Mult2`, [palace/linalg/chebyshev.cpp:261-293](../../../../reference/palace/linalg/chebyshev.cpp#L261-L293)): genuine three-term-style recurrence over a running scalar `rhop`: `rho = 1/(2·theta/delta - rhop); sd = rho·rhop; sr = 2·rho/delta; rhop := rho`. State: `(theta, delta)` persisted on smoother, `rhop` threaded across loop iterations.

No shared scalar generator is factored out. The setup paths persist different derived state: 4th-kind stores `lambda_max`, 1st-kind stores `(theta, delta)`.

### Chebyshev outer driver (duplicated per variant; no shared base)

Each `Mult2` contains the `for it` (preconditioning passes) × `for k` (polynomial degree) double loop with the residual-recompute branch `(initial_guess || it > 0) ? r := x - A·y : r := x, y := 0`. The two driver bodies are textually ~95% identical, differing only in (a) the `ApplyOrder0` argument expression (`4/(3·lambda_max)` for 4th-kind vs `1/theta` for 1st-kind) and (b) the in-loop scalar-update lines. Citation: [palace/linalg/chebyshev.cpp:230-258](../../../../reference/palace/linalg/chebyshev.cpp#L230-L258).

No `PolynomialSmoother` intermediate base class hosts the driver. Both `ChebyshevSmoother` and `ChebyshevSmoother1stKind` derive directly from `Solver<OperType>`.

### GMRES Givens scalar recurrence (independent; not a polynomial recurrence)

GMRES's restart cycle in `GmresSolver::Mult` ([palace/linalg/iterative.cpp:555-651](../../../../reference/palace/linalg/iterative.cpp#L555-L651)) carries a DIFFERENT scalar-update sequence: a stream of plane (Givens) rotations applied to a growing Hessenberg column. Per inner-loop column `j`:

1. Replay stored `(cs[i], sn[i])` for `i = 0..j-1` over the new column `H_j` (via `ApplyPlaneRotation`).
2. Generate new `(cs[j], sn[j])` from `(H_j[j], H_j[j+1])` via `GeneratePlaneRotation`.
3. Apply the new rotation to `(H_j[j], H_j[j+1])` and to `(s[j], s[j+1])`.

`GeneratePlaneRotation` has real and complex specializations at [palace/linalg/iterative.cpp:73-120](../../../../reference/palace/linalg/iterative.cpp#L73-L120); `ApplyPlaneRotation` similarly at [palace/linalg/iterative.cpp:227-250](../../../../reference/palace/linalg/iterative.cpp#L227-L250). Scalar state: `cs[]`, `sn[]`, `s[]`, column index `j`, Hessenberg column buffer.

This is a stream of unitary 2×2 rotations parameterized by the column index — NOT a degree-k three-term scalar recurrence over a smoothing polynomial. The state shape is fundamentally different from Chebyshev's `(theta, delta, rhop, lambda_max)`.

### LOBPCG / eigenvalue tracking (Palace-boundary obstruction)

LOBPCG does not exist in the Palace source tree (zero hits on `LOBPCG`). Eigenvalue tracking is delegated to:

- SLEPc via `SlepcEPSSolverBase::Solve` calling `EPSSolve` ([palace/linalg/slepc.cpp:687-720](../../../../reference/palace/linalg/slepc.cpp#L687-L720)).
- ARPACK via the restarted-Arnoldi `dnaupd` driver wrapper ([palace/linalg/arpack.cpp:35-115](../../../../reference/palace/linalg/arpack.cpp#L35-L115)).

Whatever scalar-update sequence runs inside SLEPc (Krylov-Schur / Lanczos / LOBPCG / Jacobi-Davidson, configured by `Customize()`) or ARPACK is **below the Palace boundary** and not visible to this spec. Per the 2026-05-26 lesson on out-of-scope obstructions: this branch is OBSTRUCTED, not falsified — there is no Palace-internal eigenvalue scalar-update sequence to compare to Chebyshev or GMRES.

## L1 — distinction catalog

**There is no `polynomial_recurrence_step` kernel in Palace.** The L1 form for this slice is a **distinction catalog**: three independent scalar-update-sequence sites are named, with their state schemas, and explicitly NOT unified.

### Falsification criterion

This slice is a negative result. The L1 catalog is **falsified** (and should be rewritten as a positive unification) if any of the following become true in the Palace source:

1. A function or class named `PolynomialRecurrenceStep`, `PolynomialSmoother`, or any common base class hosting the Chebyshev outer-driver double-loop appears anywhere in `palace/linalg/`.
2. A scalar-coefficient generator factored OUT of `ChebyshevSmoother::Mult2` and `ChebyshevSmoother1stKind::Mult2` (e.g., a functor or callable producing `(sd_k, sr_k)` from per-variant state) becomes visible at file or namespace scope in `chebyshev.cpp` or a sibling header.
3. `ApplyOrder0` / `ApplyOrderK` are promoted out of the anonymous namespace and reused outside `chebyshev.cpp` — particularly if reused from `iterative.cpp` (GMRES) or any eigensolver site.
4. A GMRES variant or rewrite re-expresses the Givens-stream inner loop in terms of a polynomial-recurrence parameterization, or shares scalar-state machinery with Chebyshev.

If none of (1)-(4) hold on re-examination, the catalog stands. Any cycle proposing to convert this slice from negative-result to positive-unification MUST cite one of (1)-(4) with a specific line range; absence-of-shared-kernel is not falsified by spec-side desire for symmetry.

### Distinguishing features (why the three sites do not unify)

The four sites differ on FIVE orthogonal axes; sharing any single axis would not be sufficient to unify them. The textbook meta-shape collapses these axes; the source does not.

| Axis | Chebyshev-4th | Chebyshev-1st | GMRES-Givens | Eigentracking |
|---|---|---|---|---|
| Scalar-state cardinality (per step) | 1 (loop index k) | 2 (k, rhop) | O(j) (cs/sn/s arrays of growing length) | unknown (below boundary) |
| Scalar recurrence kind | closed-form in k | three-term over rhop | unitary 2×2 stream | unknown |
| Persisted derived state | lambda_max | (theta, delta) | none (rebuilt per restart) | unknown |
| Vector-update shape | fused elementwise-product accumulator | fused elementwise-product accumulator | Hessenberg-column rotation + RHS-vector rotation | unknown |
| Termination shape | fixed degree (order-1) | fixed degree (order-1) | dynamic on \|s[j+1]\| (convergence test) | unknown |

The Chebyshev variants agree on the vector-update shape (column 4) — this is what `ApplyOrder0` / `ApplyOrderK` factor — but disagree on the scalar-recurrence kind (column 2) and persisted state (column 3). That is precisely why the source factors the vector half but not the scalar half: the shared substrate ends at the vector update.

GMRES disagrees on every axis. Eigentracking is unknown by construction (Palace-boundary obstruction).

### Catalog

| Site | Class / function | Scalar state | Per-step scalar update | Vector update |
|---|---|---|---|---|
| Chebyshev-4th-kind | `ChebyshevSmoother::Mult2` | `lambda_max` (persisted) + loop index `k` | `sd_k = (2k-1)/(2k+3)`, `sr_k = (8k+4)/((2k+3)·lambda_max)` | `ApplyOrder0` (k=0) then `ApplyOrderK` (k≥1) |
| Chebyshev-1st-kind | `ChebyshevSmoother1stKind::Mult2` | `(theta, delta)` persisted; `rhop` threaded | `rho = 1/(2θ/δ - rhop); sd = rho·rhop; sr = 2ρ/δ; rhop ← rho` | `ApplyOrder0` (k=0) then `ApplyOrderK` (k≥1) |
| GMRES Givens stream | `GmresSolver::Mult` inner loop | `cs[0..j]`, `sn[0..j]`, `s[0..m]`, column index `j` | replay `(cs[i],sn[i])` for `i<j`; `GeneratePlaneRotation(H_j[j], H_j[j+1])` → `(cs[j], sn[j])`; apply to `(H_j[j], H_j[j+1])` and `(s[j], s[j+1])` | (not applicable — scalar state IS the update) |
| Eigenvalue tracking | SLEPc / ARPACK | — | — (Palace-boundary obstruction) | — |

### Shared surface (what IS factored)

- **`ApplyOrder0` / `ApplyOrderK`** is the ONLY shared per-step surface — file-local to `chebyshev.cpp`, shared between the two Chebyshev variants only. It factors the **vector update**, not the scalar-coefficient generator. Translation-unit-private (anonymous namespace); not visible to GMRES or anything else.

### Non-shared surface (what is NOT factored)

1. **Scalar-coefficient generators**: re-derived inline per Chebyshev variant; not extracted into a `(α₀, sd_k, sr_k)` generator functor. The textbook-uniform `(α₀, sd_k, sr_k)` parameterization is a spec-level idealization that the source does not realize.
2. **Outer driver** (preconditioning-pass × polynomial-degree double loop with residual recompute): duplicated between `ChebyshevSmoother::Mult2` and `ChebyshevSmoother1stKind::Mult2`; no shared base class hosts it.
3. **Cross-solver unification** (Chebyshev ↔ GMRES): zero. Different state shapes (polynomial-degree scalars vs. Givens-rotation stream), different vector-update kernels (elementwise-product accumulator vs. Hessenberg-column rotation), different files (`chebyshev.cpp` vs. `iterative.cpp`).
4. **Eigenvalue tracking**: obstructed (below Palace boundary).

### Procedure (abstract; the slice's L1 statement)

```
# This is a catalog, not a unifying procedure.
# Each site below is its own L1 statement.

site_chebyshev_4th_kind:
  state := { lambda_max }
  for it in 1..pc_it:
    r := residual(x, A, y, it, initial_guess)
    for k in 0..order-1:
      if k == 0:
        d := (4 / (3·lambda_max)) · (dinv ⊙ r)        # ApplyOrder0
      else:
        (sd, sr) := ((2k-1)/(2k+3),  (8k+4)/((2k+3)·lambda_max))
        d := sd·d + sr·(dinv ⊙ r)                      # ApplyOrderK
      # ... y update via d (see L2 of the Chebyshev slice)

site_chebyshev_1st_kind:
  state := { theta, delta, rhop }
  for it in 1..pc_it:
    r := residual(x, A, y, it, initial_guess)
    rhop := 1.0
    for k in 0..order-1:
      if k == 0:
        d := (1 / theta) · (dinv ⊙ r)                  # ApplyOrder0
      else:
        rho := 1 / (2·theta/delta - rhop)
        (sd, sr) := (rho·rhop,  2·rho/delta)
        rhop := rho
        d := sd·d + sr·(dinv ⊙ r)                      # ApplyOrderK
      # ... y update via d

site_gmres_givens_stream:
  state := { cs[0..m], sn[0..m], s[0..m] }
  for j in 0..m-1:
    # ... Arnoldi step produces Hessenberg column H_j
    for i in 0..j-1:
      apply_plane_rotation(cs[i], sn[i], H_j[i], H_j[i+1])
    (cs[j], sn[j]) := generate_plane_rotation(H_j[j], H_j[j+1])
    apply_plane_rotation(cs[j], sn[j], H_j[j], H_j[j+1])
    apply_plane_rotation(cs[j], sn[j], s[j], s[j+1])
    # residual norm proxy is |s[j+1]|

site_eigenvalue_tracking:
  # OBSTRUCTED: scalar-update sequence lives inside SLEPc / ARPACK,
  # below the Palace boundary. Not in this spec's scope.
```

## Open questions

1. **Spec-side unification.** Should the spec introduce a methodology-level concept `polynomial_recurrence_step` that the Chebyshev slice cites, parameterized by `(α₀, sd_k, sr_k)` generators, even though no Palace kernel realizes it? Recording the absorption potential is legitimate per the variant-absorption methodology, but the resulting concept would have NO source citation — only the 2026-05-25 lesson as justification. **Resolution proposed in this cycle: NO** — emit this slice as a negative-result catalog instead, with `polynomial_recurrence_step` as a methodology-tracking term but not a source-anchored primitive. (See lesson appended this cycle.)
2. **Refactor potential within Chebyshev.** The two Chebyshev `Mult2` bodies are 95% textually identical. A single parameterized `Mult2(scalar_generator)` would absorb both. Out of scope for this slice; flagged for the Chebyshev slice if/when it is opened in earnest.
3. **`ApplyOrderK<Transpose=true>` liveness.** The `Transpose` template flag (default `false`) on `ApplyOrderK` is used only in the complex specialization to switch the conjugation pattern. No call site in `chebyshev.cpp` passes `Transpose=true`. Dead-code candidate or future-use stub; out of scope.

## See also

- [`negative-result-slice`](../../concepts/negative-result-slice.md) — the methodology pattern this slice instantiates.
- [`sequential-obstruction`](../../concepts/sequential-obstruction.md) — sister pattern for genuinely sequential algorithms; this slice is an OBSTRUCTION at the Palace boundary (eigenvalue branch) plus a NEGATIVE RESULT at the unification question.
- [`variant-absorption`](../../concepts/variant-absorption.md) — the absorption framework against which this slice's non-unification is measured.
- [`constructed-operators`](../../concepts/constructed-operators.md) — the canonical absorption route that Palace does NOT take here.
