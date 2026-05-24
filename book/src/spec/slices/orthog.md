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

## L2 — primitive composition

### L2 form

At L2 we unfold each variant's per-pass body into a sequence of named base primitives drawn from `concepts/`: `dot` (local inner product followed by a global reduction whose owner is the orthogonalization routine), `axpy` (rank-1 vector update `w ← w − α V[j]`), `gemv_basis` (batched coefficient–basis combination `w ← w − V H`), and `allreduce_sum` (the explicit global reduction; promoted from being implicit inside `dot` to a primitive in its own right because each variant fires it a different number of times and with a different message size, which is the dominant cost structure at L2).

**MGS pass (m sequential rank-1 updates, m reductions of size 1).**
```
mgs_pass(V[0..m-1], w, dot_op):
    H : array of m scalars
    for j in 0..m-1:
        h_local := dot_op(V[j], w)               # local dot
        H[j]    := allreduce_sum(h_local, 1)     # global reduction, size 1
        w       := axpy(w, -H[j], V[j])          # w ← w − H[j] V[j]
    return (H, w)
```
The j-th `axpy` *must* complete before the (j+1)-th `dot_op` (else the algorithm is no longer MGS). The reduction inside the loop is the per-step synchronization point.

**CGS pass (one batched reduction of size m, one batched update).**
```
cgs_pass(V[0..m-1], w, dot_op):
    h_local[0..m-1] := [ dot_op(V[j], w) for j in 0..m-1 ]   # m local dots, no comm
    H[0..m-1]       := allreduce_sum(h_local, m)             # one reduction, size m
    w               := gemv_basis(w, -1.0, V, H)             # w ← w − V H, batched
    return (H, w)
```
The local dots over j are independent (no inter-j ordering); the reduction is hoisted out of the loop and batched; the rank-1 updates fuse into one `gemv_basis`.

**CGS2 (CGS twice; sum the coefficients).**
```
cgs2(V[0..m-1], w, dot_op):
    (H,  w) := cgs_pass(V, w, dot_op)
    (dH, w) := cgs_pass(V, w, dot_op)
    H := axpy_scalar(H, 1.0, dH)                 # H ← H + dH (length-m vector add)
    return (H, w)
```
The second pass operates on the once-orthogonalized `w` and accumulates the correction `dH`; the returned coefficients are `H + dH` so callers recover the original Hessenberg column.

The top-level dispatch is unchanged from L1 — it picks `mgs_pass` or `cgs_pass`/`cgs2` and returns `(H, w')`.

### Variant absorption at L2

The L1 procedure inspected `variant` exactly once (dispatch). The L2 primitive-sequence does **not** unify across variants: MGS's chain is `[dot, allreduce_sum, axpy] × m`, CGS's is `[dot × m, allreduce_sum, gemv_basis]`, CGS2's is `[CGS chain] × 2 + [axpy_scalar]`. This is a genuine primitive-sequence divergence (variant-absorption level (c) is *not* achieved at L2), and that is correct: the three variants exist precisely because their L2 primitive sequences differ in collective shape and dependency structure. L1's substitutability survives because the L2 sequences all realize the same L1 contract `⟨w', V[j]⟩ ≈ 0`; only the floor and the collective cost differ.

The variant tag is therefore inspected once at L2 too (the dispatch picks which primitive sequence to run); no primitive inside a chosen sequence re-inspects it.

### What's transparent vs. load-bearing

- **Transparent at L2** (silently unfolded into the primitives above): fusing the m rank-1 `axpy`s of CGS into one `gemv_basis`; whether `gemv_basis` is implemented as a packed BLAS-2 call or as a loop of `axpy`s; whether `h_local` in CGS is materialized as an array or streamed through a fused dot-loop kernel.
- **Load-bearing at L2** (preserved as explicit claims): the *ordering* dependency in MGS (j-th update before (j+1)-th dot); the *number and size* of `allreduce_sum` calls per variant (m×1 vs. 1×m vs. 2×m), since this is the cost-shape that motivates the variants' existence; the *non-fusion* of the two CGS2 passes (the second pass must read the once-orthogonalized `w`, not a fused expression). Floating-point reduction order inside `allreduce_sum` is delegated to the reduction primitive and is not respecified here.

### Citations

- `palace/linalg/orthog.hpp:25-36` — MGS body: per-j local dot, `Mpi::GlobalSum(1, &H[j], comm)`, then `w.AXPY(-H[j], V[j])`. Matches the MGS chain above one-for-one.
- `palace/linalg/orthog.hpp:38-53` — CGS/CGS2 body: m local dots into `H[0..m-1]`, single `Mpi::GlobalSum(m, H.data(), comm)`, then m sequential `AXPY`s (which we fuse into `gemv_basis` at L2; the source loop is the transparent unfolding). The `refine` flag re-enters the same body to produce CGS2.
- `palace/linalg/orthog.hpp:55-89` — block / SLEPc wrappers use the same primitive chain shape; the only change is the dot kernel (BV-aware), which is a `dot_op` substitution at L1.
- `test/unit/test-orthog.cpp:70-97` — all three variants pass the same substitutability assertion on a well-separated basis; this is the empirical witness that the L2 chains all realize the L1 contract.

### Test linkage

Unchanged from L1; the L2 unfolding does not require new tests — the existing substitutability tests cover the contract, and the per-variant chain divergence is a cost-shape claim, not a correctness claim. CGS-instability stress remains uncovered; flagged at L1 already.

### Open questions

- Whether `gemv_basis` deserves a dedicated concept entry (it appears here as the batched coefficient–basis combination; the same shape will appear in GMRES's `apply_basis_combination` step and in projection slices). Provisionally extracted in this cycle.
- The cost annotation for `allreduce_sum` (m×1 vs. 1×m vs. 2×m) is named at L2 but not formalized; will become a proper cost claim if/when an L3 lift is attempted (likely an obstruction, since the sequential MGS chain has no global tensor-field form).
