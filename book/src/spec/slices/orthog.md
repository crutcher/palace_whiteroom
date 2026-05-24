# Slice: orthog

Block Gram-Schmidt orthogonalization of a candidate vector against a stored basis,
with three variants (MGS, CGS, CGS2) selected by a runtime tag. Used by GMRES /
FGMRES Arnoldi and by the SLEPc eigenvalue path.

## L0 → L1

### L1 form

**Primitive.** `orthogonalize_column(variant, V[0..m-1], w; dot_op) → (H[0..m-1], w')`
where:

- `V[0..m-1]` is a stored basis (read-only; assumed already orthonormal under `dot_op`).
- `w` is the candidate vector being orthogonalized.
- `dot_op : (x, y) → ScalarType` returns the **local** (per-rank) inner product; the
  orthogonalization routine owns the global reduction.
- `H[0..m-1]` is the coefficient vector (Hessenberg column entries, in the GMRES caller).
- `w' = w − Σⱼ H[j] · V[j]` is the orthogonalized output, **not normalized** (caller normalizes).
- `variant ∈ {MGS, CGS, CGS2}` selects the algorithm. The per-step procedure mentions
  `variant` exactly once, at the dispatch site; the rest of the L1 statement is uniform.

**Invariant.** On exit, ⟨w', V[j]⟩ ≈ 0 for j ∈ [0,m) up to the numerical floor of the
chosen variant. All three variants are substitutable on this contract; they differ only
in the floor (CGS < MGS < CGS2 in increasing stability) and in MPI-collective shape.

**Procedure (variant-parametric).** For variant V:

```
orthogonalize_column(V, V_basis, w, dot_op):
    (H, w') := one_pass(V_basis, w, dot_op)                 # MGS or CGS body
    if V == CGS2:
        (dH, w') := one_pass(V_basis, w', dot_op)           # one refinement pass
        H += dH
    return (H, w')

one_pass = mgs_pass     if V == MGS
         = cgs_pass     if V ∈ {CGS, CGS2}
```

where `mgs_pass` and `cgs_pass` are the two coefficient-update kernels (their detailed
sequencing — when the local dot is taken, when the global reduction fires, when the rank-1
update is applied — is L2 mechanism, not L1 content).

**Variant axes absorbed (per `concepts/variant-absorption.md`).**

- **Algorithm choice {MGS, CGS, CGS2}.** Absorbed parametrically: one entry point,
  one statement of invariant, one return shape. The variant tag is inspected at the
  top-level dispatch only.
- **Scalar type / vector type (real vs. complex, Vector vs. ComplexVector).** Absorbed
  by template parameters; out of L1 scope.
- **Inner-product weighting (`InnerProductW` template hook).** Absorbed as the `dot_op`
  argument. Default is the unweighted local dot; callers (e.g. weighted GMRES) pass a
  custom local inner product. The contract — `dot_op` is *local*, routine owns reduction —
  is uniform across variants.

**Residual axes (disclosed, not absorbed at L1).**

- MPI collective shape differs by variant (MGS: m reductions of size 1; CGS: 1 reduction
  of size m; CGS2: 2 reductions of size m). This is a performance axis surfaced at L2,
  not an L1 semantic difference. MPI structure is out of scope for this project per
  CLAUDE.md; recorded here as a cost annotation only.
- Normalization of `w'` is **not** part of this primitive; callers normalize. Header TODO
  notes this asymmetry; we preserve current convention.

**State / mutation pattern.** `H` is written (CGS2 accumulates across two passes; MGS/CGS
write once). `w` is updated in place (MGS: m sequential rank-1 updates; CGS: one batched
update from saved `H`; CGS2: two batched updates). `V_basis` is read-only throughout.

**Caller interface.** GMRES/FGMRES use a single dispatch helper
`OrthogonalizeIteration(type, comm, V, w, Hj, j)` that forwards to this primitive with
`m = j+1`. The Arnoldi step calls it uniformly regardless of variant; the variant lives
as a runtime field on the solver.

### Citations

- `palace/linalg/orthog.hpp:18-23` — header contract (input V normalized, output w not
  normalized, `dot_op` is local + routine owns reduction).
- `palace/linalg/orthog.hpp:25-36` — MGS variant.
- `palace/linalg/orthog.hpp:38-53` — CGS / CGS2 variant (toggled by `refine` flag).
- `palace/linalg/orthog.hpp:55-89` — block / SLEPc-facing wrappers (same shape).
- `palace/utils/labels.hpp:163-170` — `enum Orthogonalization { MGS, CGS, CGS2 }`.
- `palace/linalg/iterative.cpp:307-326` — `OrthogonalizeIteration` dispatch helper.
- `test/unit/test-orthog.cpp:70-97`, `:123-160` — parametric tests over all three variants
  + custom inner product, asserting the substitutable contract.

### Test linkage

`test/unit/test-orthog.cpp` ↔ `palace/linalg/orthog.hpp` (new linkage; record in
`scaffolding/test-linkages` when promoted). Tests confirm:

- m == 0 early-exit leaves `w` unchanged across all variants.
- All three variants achieve ⟨w', Vᵢ⟩ < 1e-12 on a well-separated random basis.
- The `dot_op` template hook is exercised with a non-identity (real-weighted) functor.

CGS-instability stress cases (near-rank-deficient bases that distinguish CGS from CGS2
numerically) are **not** covered by the unit tests; the variants are tested as
substitutable, not as numerically distinguishable.

### Open questions

- Lift normalization into the primitive's contract, or preserve the caller-normalizes
  convention? Header has a TODO; deferred.
- Surface MPI collective shape as a formal cost annotation at L2 when that slice lands.

## L1 → L2

(Deferred to next cycle on this slice.)
