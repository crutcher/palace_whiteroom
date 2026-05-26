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

## L3 — global tensor-field form (with sequential obstruction)

### L3 form (CGS and CGS2)

The L2 unfoldings for CGS and CGS2 already speak in batched, basis-wide primitives — the per-j loop of local dots collapses into one inner-products-with-a-basis operation, and the m sequential rank-1 `axpy`s fuse into one basis-combination operation. Promoting these to a tensor-field statement is a notational rotation only; no new structure appears.

**Notation.** Let `V ∈ Sⁿˣᵐ` be the basis matrix whose columns are the stored basis vectors (S the scalar type; the columns are distributed in the per-rank layout the dot uses). Let `w ∈ Sⁿ` be the candidate. Write `⟨·, ·⟩` for the (globally reduced) inner product induced by `dot_op`, and let `Vᴴ w ∈ Sᵐ` denote the column-stacked vector of inner products `H[j] = ⟨V[j], w⟩`. All operations below are read as global (post-reduction) tensor operations.

**CGS as a global statement.**
```
cgs_pass(V, w):
    H := Vᴴ w                       # m-fold inner product, one global reduction
    w := w − V H                     # basis combination, single matvec by V
    return (H, w)
```
The two lines are the L3 form: `Vᴴ w` is one `gemv` of `Vᴴ` against `w` (its realization at L2 is the m local dots followed by an `allreduce_sum` of size m); `V H` is one `gemv` of `V` against `H`. This is the textbook *projector form* of one Gram-Schmidt sweep: `w ← (I − V Vᴴ) w` with `H = Vᴴ w` retained as the coefficient output. The L2-to-L3 step is a notational compression: `[dot × m, allreduce_sum, gemv_basis] ≡ [Vᴴ w, V H]`.

**CGS2 as a global statement.**
```
cgs2(V, w):
    H  := Vᴴ w
    w  := w − V H
    dH := Vᴴ w                       # second projector pass
    w  := w − V dH
    H  := H + dH
    return (H, w)
```
Equivalently, `w ← (I − V Vᴴ)² w` with `H` accumulating both passes' coefficients. The non-fusion claim from L2 is preserved at L3: the second `Vᴴ w` reads the once-projected `w`, not a fused expression — `(I − V Vᴴ)²` is **not** `I − 2 V Vᴴ + V Vᴴ V Vᴴ` algebraically simplified, because `V` is only approximately orthonormal (the entire point of CGS2 is to handle the deviation), so the two projector applications do not collapse.

**Variant absorption at L3.** CGS and CGS2 share a primitive shape at L3 (both are projector applications using `Vᴴ w` and `V H`); they differ only in the number of passes and in coefficient accumulation. This is a tighter unification than L2 achieved — at L2, CGS's chain and CGS2's chain were different lengths over different primitive sets; at L3, both are sequences of `(Vᴴ w, V H)` projector applications. The variant tag is inspected once at the top to choose 1-pass vs. 2-pass.

### L3 obstruction (MGS)

MGS does **not** lift to a global tensor-field form. The defining feature of MGS is that the j-th `axpy` (`w ← w − H[j] V[j]`) must complete before the (j+1)-th inner product (`H[j+1] = ⟨V[j+1], w⟩`) is computed, because each subsequent inner product is taken against the *progressively-updated* `w`, not against the original. Equivalently:

- MGS computes `H[j] = ⟨V[j], (I − V[j−1] V[j−1]ᴴ)(I − V[j−2] V[j−2]ᴴ) ⋯ (I − V[0] V[0]ᴴ) w⟩` — a left-to-right composition of m rank-1 projectors, each applied serially.
- CGS computes `H[j] = ⟨V[j], w⟩` — all m inner products taken against the same original `w`, in parallel.

These are algebraically distinct (they produce different `H` vectors and different `w'`, identical only when `V` is exactly orthonormal — which it is not, by hypothesis: the orthogonalization exists because the input is not yet orthogonal to `V`). MGS therefore has no global form: it is a sequential rank-1 projector cascade, and any rewrite that touches all columns of `V` simultaneously is no longer MGS.

This is a [sequential-obstruction](../../concepts/sequential-obstruction.md) of the canonical kind — sequential dependency on a progressively-updated state, structurally analogous to Gauss-Seidel relaxation (where the j-th unknown is updated using already-updated neighbors) and to triangular solves (where the j-th solution component depends on already-solved earlier components). The obstruction is **not** removable by reordering or refactoring; it is the algorithm.

**What MGS does have at L3.** A *parallel-by-blocks* form exists at finer granularity: if the basis is partitioned into blocks `V = [V₁, V₂, …, V_b]`, one can run CGS-within-block and MGS-across-blocks (this is the block-MGS variant; some implementations use it as a numerical compromise). Palace does not currently expose block-MGS, and it is out of scope here; recording the option as a pointer for future slices.

### Variant absorption at L3 (summary)

Three-way variant absorption status at L3:

- **CGS / CGS2.** Achieve all three absorption levels (invariant, procedure, primitive-sequence) at L3: both are projector-form statements over `Vᴴ w` and `V H`, differing only in pass count.
- **MGS.** Achieves invariant-level absorption only — it satisfies the same L1 contract `⟨w', V[j]⟩ ≈ 0`. Procedural and primitive-sequence absorption are **structurally impossible** at L3 because MGS has no global form. This is disclosed at L3 as an obstruction, not silently dropped.

The slice's overall variant-absorption posture at L3 is therefore: CGS and CGS2 unify at L3; MGS is a sequential-obstruction sibling that remains at L2.

### Citations

- [palace/linalg/orthog.hpp:25-36](../../../../reference/palace/linalg/orthog.hpp#L25-L36) — MGS body: per-j local dot of `V[j]` against the *current* (progressively-updated) `w`, immediately followed by `w.AXPY(-H[j], V[j])`. The interleaving of dot and axpy in the same j-loop body is the source-level witness of the sequential obstruction.
- [palace/linalg/orthog.hpp:38-53](../../../../reference/palace/linalg/orthog.hpp#L38-L53) — CGS/CGS2 body: all m local dots of `V[j]` against the *same* original `w` (no in-loop mutation of `w`), single `Mpi::GlobalSum(m, H.data(), comm)`, then a loop of `AXPY`s that the L2 form fuses into `gemv_basis` and that the L3 form writes as `w ← w − V H`. The `refine` flag re-enters this body to produce CGS2; the second entry reads the once-orthogonalized `w`.
- [test/unit/test-orthog.cpp:70-97](../../../../reference/test/unit/test-orthog.cpp#L70-L97) — substitutability test: all three variants achieve `⟨w', V[j]⟩ < 1e-12` on a well-separated basis, confirming the L1 contract holds across the L3-unifiable pair (CGS, CGS2) and the L3-obstructed sibling (MGS) alike.

### Test linkage

Unchanged. The L3 lift introduces no new correctness obligations: the CGS/CGS2 projector form is a notational compression of the L2 batched form (substitutability tests cover it), and the MGS obstruction is a structural claim (no algorithm change to test).

### Open questions

- Block-MGS as a hybrid (CGS within block, MGS across blocks) is a known numerical/parallel compromise; recording for future consideration. Not in Palace today.
- The `Vᴴ w` operation, on a *distributed* basis where each rank holds full-length columns of `V`, has a specific MPI collective shape (one allreduce of size m) that matches the L2 cost annotation. Formalizing this as a cost claim is deferred to whenever a cost-annotation slice lands; the L3 form itself does not depend on it.

## L4 — calculus form

### State stratification

The L4 form distinguishes three categories of state per [state-stratification](../../concepts/state-stratification.md):

- **Sim state** (the algorithm's externally-visible payload): the candidate vector `w` (mutated to `w'`) and the produced coefficient vector `H`. The stored basis `V[0..m-1]` is sim state owned by the caller (GMRES's Arnoldi loop, SLEPc's BV) and threaded through read-only.
- **Operator internal params** (constructed at solve-start, immutable for the call): the variant tag `variant ∈ {MGS, CGS, CGS2}`, the inner-product hook `dot_op`, and the basis-size `m`.
- **Ephemeral intermediates**: the per-pass local-dot buffer `h_local` (CGS/CGS2), the reduction temporaries inside `allreduce_sum`, and the correction coefficients `dH` (CGS2). None of these survive the call.

### L4 form

```
type OrthogParams = {
  variant   : Variant,             // MGS | CGS | CGS2 — constructed at solve start
  dotOp     : (Vec, Vec) -> Scalar // local inner-product hook
}

type OrthogState = {
  V : Basis,    // read-only basis of m columns (caller-owned)
  w : Vec,      // candidate; mutated to w'
  H : Vec_m     // coefficients; written
}

// The orthogonalization step is a Solve-monad action threading OrthogState.
// Variant is dispatched once at the top of `orthogonalize`; the per-step body
// is uniform up to the choice of pass-kernel.

orthogonalize : OrthogParams -> Solve OrthogState ()
orthogonalize params = do
  case params.variant of
    MGS  -> mgsPass  params.dotOp
    CGS  -> cgsPass  params.dotOp
    CGS2 -> do { cgsPass params.dotOp
               ; (dH, _) <- cgsPassAccum params.dotOp
               ; modify (\s -> s { H = axpy 1.0 dH s.H }) }

// cgsPass / cgsPassAccum write H and w to the state; mgsPass threads the
// per-j update through the same state (the sequential dependency is on the
// w field of OrthogState, which subsequent dotOp calls re-read).
```

The Solve-monadic structure ([solve-monad](../../concepts/solve-monad.md)) makes the read-only-ness of `V` and the write-discipline on `w` and `H` explicit. `mgsPass` is a sequence of `get s.w; modify (\s -> s { H[j] = ..., w = axpy(-H[j], V[j], s.w) })` actions whose order is load-bearing — equivalently, a left-fold over `[0..m-1]` whose accumulator is the `w` field of the state. `cgsPass` is a single `modify` that writes both fields atomically from values computed against a snapshot of `s.w`; there is no fold over j inside the monadic structure, only inside the pure `Vᴴ w` and `V H` operations that produce the new state in one step.

### Variant as constructed-operator parameter

The variant tag is an [operator internal param](../../concepts/constructed-operators.md) (per [variant-absorption](../../concepts/variant-absorption.md)): once `params.variant` is fixed at solve-start, the per-call body does not re-inspect it (the `case` above dispatches into one of three closures and stays there). This matches the L1/L2/L3 absorption story — the variant is bound once and threaded as a constructed-operator parameter, not as a per-step branch. The L4 form makes the binding/dispatch site the only place `variant` appears: the closures `mgsPass`, `cgsPass`, `cgsPassAccum` are `dotOp`-parametric but variant-free internally.

### Sequential obstruction at L4

The MGS branch's body is `for j in 0..m-1: ⟨get s.w, V[j]⟩ ; modify (..axpy..)`. The `get s.w` in iteration `j+1` reads the `s.w` written by iteration `j`'s `modify` — this is the same sequential dependency the L3 form named as obstruction ([sequential-obstruction](../../concepts/sequential-obstruction.md)), and the Solve monad expresses it as a sequence of `get`-then-`modify` actions that does not commute. Within the calculus the obstruction is no longer something the slice must apologize for — it is the *typical* shape of a Solve-monad action on a single state field, the j-indexed monadic left-fold familiar from Gauss-Seidel relaxation and forward triangular solves. CGS and CGS2 are the *atypical* shape (one snapshot read, one atomic write); at L4 this is just the difference between `do { x <- get ; modify (f x) ; modify (g x) }` (sequential) and `do { x <- get ; modify (\s -> g (f x) s) }` (atomic). The Solve monad does not eliminate the obstruction — it makes the obstruction's *shape* (sequential get/modify chain vs. single atomic modify) the literal type-level distinction between the variants.

### Citations

- [palace/linalg/orthog.hpp:18-23](../../../../reference/palace/linalg/orthog.hpp#L18-L23) — header contract: `V` read-only, `w` mutated, `H` written; this is the OrthogState write-discipline.
- [palace/linalg/orthog.hpp:25-36](../../../../reference/palace/linalg/orthog.hpp#L25-L36) — MGS body: per-j `get s.w` followed by `modify (axpy)`, the Solve-monad shape of the sequential obstruction.
- [palace/linalg/orthog.hpp:38-53](../../../../reference/palace/linalg/orthog.hpp#L38-L53) — CGS/CGS2 body: single snapshot read of `w` (across the m local dots), single batched modify; the atomic-modify shape.
- [palace/linalg/iterative.cpp:307-326](../../../../reference/palace/linalg/iterative.cpp#L307-L326) — `OrthogonalizeIteration` dispatch helper: confirms the variant is bound at solver-construction and not re-inspected per step.

### Test linkage

Unchanged. The L4 form is a notational compression of L3 plus state-stratification; no new correctness obligations are introduced.

### Open questions

- Whether the caller-normalizes asymmetry (`w'` not normalized) belongs as a separate Solve-monad action `normalize` chained after `orthogonalize`, or fused. Header has a TODO; deferred consistently with L1.
- The Solve-monad treatment of `V` as caller-owned read-only state suggests a `Reader`-flavored sub-effect; folding this into a richer monad stack is a calculus-level question, not slice-level, and is left to the L4 calculus design doc.
