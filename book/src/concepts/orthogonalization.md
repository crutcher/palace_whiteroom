---
edges:
  reference:
    - L1/orthogonalize
    - L1-L0/orthogonalize-mutation-rotation
    - L1/dot
    - L1/axpy
    - L2/orthogonalize
    - L3/orthogonalize
    - L2/krylov_step
    - concepts/sequential-obstruction
    - concepts/variant-absorption
---

# concept: orthogonalization

The Arnoldi orthogonalisation step in Krylov-subspace (and ROM basis-extension) methods:
given an orthonormal basis `V[0..m-1]` and a new candidate vector `w`, produce the residual
`w'` (the component of `w` orthogonal to `span(V)`) together with the projection
coefficients `H[0..m-1]` (the leading entries of the Arnoldi/Hessenberg column).

> **Authoritative definition:** the firm operator
> [`L1/orthogonalize`](../L1/orthogonalize.md) is the load-bearing contract; this page is the
> narrative cross-cut. The forward lowering is
> [`L1-L0/orthogonalize-mutation-rotation`](../L1-L0/orthogonalize-mutation-rotation.md).
> Where this page and the L1 entry disagree, the L1 entry wins.

## Contract (coefficients and normalisation)

The operator returns the pair `(w', H)`:

- `w'` — the orthogonal residual, **not normalised**. Palace's header is explicit:
  "Assumes that the input vectors are normalized, but does not normalize the output vectors!"
  (`palace/linalg/orthog.hpp:18-23`). Normalisation is the *caller's* job — `arnoldi_step`
  follows `orthogonalize` with `nrm2(w')` and `scal(1/‖w'‖, w')`.
- `H` — the **length-`m`** projection coefficients, `H[j] = ⟨w_eff(j), V[j]⟩`, with
  `w' = w − Σ_j H[j]·V[j]`. These are the leading `m` entries of the Hessenberg column.

The Hessenberg sub-diagonal `H[m] = ‖w'‖` is **not** produced by this operator — it is the
caller's `nrm2(w')` step. Do not fold it into `H`; that conflates the operator's coefficient
output with the caller's normalisation (the historical drift this page used to carry).

`w_eff(j)` is the candidate as seen by column `j`: for CGS/CGS2 it is the original `w` for
every `j`; for MGS it is the progressively-updated `w` after subtracting columns `0..j-1`.
The inner product follows the [`dot`](../L1/dot.md) conjugate-linear-first-argument
convention.

## Variants

Three implementations occupy the same L1 primitive role; they agree in exact arithmetic and
differ only in finite-precision stability and in collective shape (the load-bearing axis).
At L0 they are three distinct loop-structures — see
[`L1-L0/orthogonalize-mutation-rotation`](../L1-L0/orthogonalize-mutation-rotation.md) for
the per-variant loop forms and citations.

- **MGS (Modified Gram–Schmidt)**: single interleaved loop — for `k = 0..m-1`:
  `H[k] = dot(w, V[k]); w ← w − H[k]·V[k]`. More stable than CGS; `m` synchronisations of
  size 1 per step. Carries a [sequential-obstruction](./sequential-obstruction.md) at L3.
- **CGS (Classical Gram–Schmidt)**: split two-phase loop — all `m` `dot`s against the
  *original* `w` (one reduction of size `m`), then all `m` updates. One synchronisation per
  step; loses orthogonality faster than MGS for ill-conditioned bases.
- **CGS2 (CGS with re-orthogonalisation)**: CGS applied twice; the second batched pass
  corrects the first (coefficients accumulate, `H ← H + dH`). Two synchronisations of size
  `m`; recovers MGS-level orthogonality up to roundoff ("twice is enough" — Kahan/Parlett).
  This is Palace's default for parallel scalability with near-MGS stability.

The variant tag is a runtime enum (`Orthogonalization ∈ {MGS, CGS, CGS2}`) bound at solver
setup and **inspected exactly once** at dispatch (`OrthogonalizeIteration`,
`palace/linalg/iterative.cpp:308-325`); downstream code never re-inspects it. Per
[`variant-absorption`](./variant-absorption.md) the three absorb at all three levels under
residual-axis disclosure (the residual being the per-variant collective shape:
m×1 / 1×m / 2×m reductions). Householder is out of scope (no Palace L0 path).

A second variant axis is the **inner-product hook** (`dot_op`): the canonical inner product
vs a `B`-weighted dot used by the SLEPc/ROM paths (`palace/models/romoperator.cpp:51-66`).
This is a substitution of the [`dot`](../L1/dot.md) dependency; the operator's shape and laws
are unchanged (the orthogonality contract becomes `⟨w', V[i]⟩_B = 0`).

## L1 / L2 / L3 placement

- **L1**: the single pure primitive `orthogonalize(w, V, variant) → (w', H)` (firm —
  [`L1/orthogonalize`](../L1/orthogonalize.md)). No destination buffers, no `comm`, no
  in-place mutation; the variant is a parameter.
- **L1>L0**: the mutation rotation
  [`orthogonalize-mutation-rotation`](../L1-L0/orthogonalize-mutation-rotation.md) — in-place
  `w` overwrite + raw-pointer `H` write + the three per-variant L0 loop-structures.
- **L2 / L3**: the primitive *set* — [`dot`](../L1/dot.md), [`axpy`](../L1/axpy.md), plus the
  caller's `nrm2`/`scal` — is shared across variants; the variant axis affects only the
  *sequence and batching*. The MGS branch carries a sequential-obstruction that surfaces at
  L3 (CGS/CGS2 lift to a clean batched/global form; MGS does not). See
  [`L2/orthogonalize`](../L2/orthogonalize.md) and [`L3/orthogonalize`](../L3/orthogonalize.md)
  for the firm L2/L3 unfolding.

## Citations

- `palace/linalg/orthog.hpp:18-90` — the `OrthogonalizeColumnMGS / CGS` family (CGS2 is
  `OrthogonalizeColumnCGS(refine=true)`); header scope contract at `:18-23`.
- `palace/linalg/iterative.cpp:308-325` — `OrthogonalizeIteration` runtime variant dispatch.
- `palace/linalg/iterative.cpp:629-632, 808-811` — GMRES / FGMRES Arnoldi call sites, each
  followed by the caller's `nrm2` sub-diagonal + `scal` normalisation.
- `palace/models/romoperator.cpp:51-66` — ROM basis-extension reuse (the second consumer;
  the B-weighted `dot_op` hook).
- `test/unit/test-orthog.cpp:99-160` — empty-basis identity + the `⟨w', V[i]⟩ ≈ 0`
  substitutability witness across MGS/CGS/CGS2.

## Consumers

- [`krylov_step` (GMRES instance)](../L2/krylov_step.md) — orthogonalising the new Arnoldi vector against the
  existing basis; the variant axis is absorbed at this primitive's contract.
- The ROM basis-extension path (`romoperator.cpp`).
- The L2 [`krylov_step`](../L2/krylov_step.md) composition references `orthogonalization` as
  an all-three-level-absorbed (residual-axis-disclosed) component.
