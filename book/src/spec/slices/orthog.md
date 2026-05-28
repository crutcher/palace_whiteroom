# Slice: orthog

Block Gram-Schmidt orthogonalization of a candidate vector against a stored basis,
with three variants (MGS, CGS, CGS2) selected by a runtime tag. Used by GMRES /
FGMRES Arnoldi and by the SLEPc eigenvalue path.

## L0 → L1 (reduced)

> **Reduction status (cycle-011+):** the Gram-Schmidt L1 form of this slice has been partially lifted into the firm artifact (see below). The unique L1 invariants and MPI-collective shape disclosure are retained in the L2/L3/L4 sections of this slice pending lift to a firm `L1/orthogonalize` operator entry. The plane-rotation-stream sub-slice (lines 313+ below) overlaps `book/src/spec/slices/plane_rotation_stream.md` and is deferred to batch-3 of the phase-1-corpus-reduction-audit for joint reduction.

The Gram-Schmidt L1 form has been partially lifted into the firm artifact:

- `book/src/concepts/orthogonalization.md` — the L1 contract: `orthogonalize(gs_orthog, V[0..j], w) → (w', h)` dispatching on `gs_orthog ∈ {MGS, CGS, CGS2}` exactly once. The variant axis is named here; the level-(b) variant absorption is the slice's pattern.
- `book/src/concepts/sequential-obstruction.md` §"Example: MGS as sequential-obstruction" (lines 37-48 of that file) — the structural argument for MGS's L3 non-liftability is lifted verbatim from this slice's L3 section.
- `book/src/L2/krylov-step.md` references `orthogonalization` as a level-(b)-absorbed L2-composition surface (per `L2/krylov-step.md:38` future harvester candidate); the slice's L1 invariants (read-only `V_basis` / mutated `w` / written `H` / `dot_op` is local + routine owns reduction) and the MPI-collective shape disclosure (MGS: m reductions of size 1; CGS: 1 of size m; CGS2: 2 of size m) are NOT in firm entries.
- `book/src/L1-L0/ksp-solve-mutation-rotation.md` §"Sub-pattern C — inner GMRES body" cites `OrthogonalizeIteration` at `iterative.cpp:307-325` as the dispatch site.

**Pending lift to firm `L1/orthogonalize` operator entry** (OQ `l1-orthogonalize-promotion-from-arnoldi-step-and-orthog` at `scaffolding/open-questions.md`): the unique L1 invariants and the MPI-collective shape are retained in the L2/L3/L4 sections below pending a firm L1 row.

**Citations and test linkage retained** in the L2/L3/L4 sections (the unique parametric test coverage of all three variants at `test/unit/test-orthog.cpp:70-97, :123-160` is also cited by `L2/krylov-step.md:170-171`).

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

## Context

# Orthogonalization (plane-rotation stream)



GMRES and other Krylov methods produce an upper-Hessenberg matrix $\bar{H}_m \in \mathbb{C}^{(m+1) \times m}$ one column at a time. To extract a least-squares solution incrementally and to monitor the residual norm without forming $\bar{H}_m$ explicitly, Palace applies a stream of plane (Givens) rotations to each newly-added column, reducing $\bar{H}_m$ to upper-triangular $R_m$ in place and propagating a transformed RHS vector $\bar{g}_m$ from which $\|r_m\|$ is read off as $|\bar{g}_m[m]|$.

This slice dissects the plane-rotation stream: the per-step generation, application, and accumulation of Givens rotations against the Hessenberg column and the RHS vector. It is the L0→L1 entry point for a body of machinery shared across GMRES, FGMRES, and any future least-squares-on-Krylov solver.

## Background

The technique is textbook least-squares-on-Hessenberg via Givens rotations; see Saad 2003 *Iterative Methods for Sparse Linear Systems* §6.5.3 ("Practical Implementation Issues"), and Golub & Van Loan 2013 *Matrix Computations* §5.1.8–9 (Givens rotations) and §5.2.4 (QR via Givens). A 2×2 Givens rotation

```
G(c, s) = [  c̄  s̄ ]
          [ -s   c ]
```

is chosen at column $k$ to zero the sub-diagonal entry $\bar{H}_m[k+1, k]$, then accumulated and re-applied to subsequent columns and to $\bar{g}_m$. Palace's variant uses the scaled-Givens form (Bindel/Demmel/Kahan/Marques 2002, *On Computing Givens Rotations Reliably and Efficiently*) for numerical robustness against over/underflow; for complex scalars $\bar{c}$ is real and $s$ is complex (the standard "real-cosine" convention).

Palace does NOT store the rotation stream as a separate $Q_m$ factor; rotations are applied in place to the columns of $\bar{H}_m$ as they are produced, and to the running $\bar{g}_m$ vector. The $(c_k, s_k)$ pairs are stored as two length-$m$ arrays so that the back-solve (against $R_m$) and the least-squares residual can both be computed from the accumulated state.

## Variant axes

The plane-rotation stream is invariant across GMRES vs FGMRES and across MGS vs CGS2 orthogonalization choices; those variants affect *how* the Hessenberg column is produced, not how it is reduced. The axes that the rotation stream itself exposes:

- **Scalar type**: real vs complex. Affects the Givens-generation formula and the conjugation pattern in application. Absorbed parametrically via the templated scalar `T`.
- **Generation formula**: naive vs scaled. Palace uses scaled-Givens unconditionally; no runtime axis.
- **Storage layout**: in-place column reduction vs explicit $Q$. Palace uses in-place; no runtime axis.

All three are absorbed at L1 — the L1 statement does not branch on any of them.

## L0 — citations

The plane-rotation stream is implemented in Palace as three primitives plus their callers in the GMRES family:

- **Generation** of $(c_k, s_k)$ from a 2-vector $(h_{kk}, h_{k+1,k})$:
  [palace/linalg/gmres.cpp:GeneratePlaneRotation](../../../reference/palace/linalg/gmres.cpp) — real and complex specializations of the function compute $(c, s)$ such that $G(c, s) \cdot (dx, dy)^T = (r, 0)^T$ with $r = \sqrt{|dx|^2 + |dy|^2}$, using a scaled formulation to avoid spurious over/underflow. The real specialization yields $c = dx/r$, $s = dy/r$. The complex specialization yields real $c$ and complex $s = \bar{dx} \cdot dy / (|dx| \cdot r)$ (the "real-cosine" convention).

- **Application** of a stored rotation $(c_k, s_k)$ to a 2-vector $(dx, dy)$ in place:
  [palace/linalg/gmres.cpp:ApplyPlaneRotation](../../../reference/palace/linalg/gmres.cpp) — computes $(dx', dy') = (c \cdot dx + s \cdot dy, -\bar{s} \cdot dx + c \cdot dy)$, overwriting the input. Used both to apply previously-stored rotations to a freshly-produced Hessenberg column entry and to apply the newly-generated rotation to the RHS pair.

- **Per-step driver** that integrates generation + application against the Hessenberg column being produced at step $k$ and the running $\bar{g}_m$ vector:
  [palace/linalg/gmres.cpp:GmresSolver::Mult](../../../reference/palace/linalg/gmres.cpp) inner loop — after the Arnoldi step produces column $H[\cdot, k]$ with sub-diagonal $H[k+1, k]$, the driver: (i) applies stored rotations $(c_0, s_0), \ldots, (c_{k-1}, s_{k-1})$ to entries $H[0..k, k]$ from top to bottom; (ii) calls `GeneratePlaneRotation` on $(H[k, k], H[k+1, k])$ to obtain $(c_k, s_k)$ and the new diagonal $r_{kk}$; (iii) applies $(c_k, s_k)$ in place to $(H[k, k], H[k+1, k])$, zeroing the sub-diagonal; (iv) applies $(c_k, s_k)$ to the RHS pair $(\bar{g}[k], \bar{g}[k+1])$, propagating the residual estimate.

- **Back-solve consumer** that reads $R_m$ (the rotated $\bar{H}_m$) and the leading $m$ entries of $\bar{g}_m$ to produce the least-squares minimizer $y_m$:
  [palace/linalg/gmres.cpp:GmresSolver::Mult](../../../reference/palace/linalg/gmres.cpp) — back-substitution loop after the inner Arnoldi loop exits. The residual norm $\|r_m\|$ is $|\bar{g}_m[k+1]|$ immediately after applying $(c_k, s_k)$ to $\bar{g}$.

The FGMRES variant ([palace/linalg/gmres.cpp:FgmresSolver::Mult](../../../reference/palace/linalg/gmres.cpp)) uses the same plane-rotation stream; only the Arnoldi step differs (it stores both $V$ and $Z = M^{-1} V$).

## L1 — per-element procedure

### State

During one GMRES cycle of up to $m_{\max}$ steps, the plane-rotation stream contributes:

- $H \in \mathbb{C}^{(m_{\max}+1) \times m_{\max}}$ — upper-Hessenberg matrix, rotated in place as columns arrive (post-rotation, the upper-triangular part is $R_m$).
- $c \in \mathbb{R}^{m_{\max}}$ — real cosines $c_k$, one per step.
- $s \in \mathbb{C}^{m_{\max}}$ — complex sines $s_k$, one per step (real in the real-scalar specialization).
- $\bar{g} \in \mathbb{C}^{m_{\max}+1}$ — transformed RHS, initialized to $(\beta, 0, \ldots, 0)$ where $\beta = \|r_0\|$, rotated in place as steps complete.

The rotation stream's own state is $(c, s)$; $H$ and $\bar{g}$ are shared with the Arnoldi step and the back-solve consumer.

### Procedure: `plane_rotation_step(k, H_column, c, s, g_bar)`

Given step index $k$, the freshly-produced Hessenberg column $H[0..k+1, k]$ (with non-zero sub-diagonal $H[k+1, k]$ from the Arnoldi orthogonalization), the accumulator arrays $(c, s)$ holding rotations $0..k-1$, and the running $\bar{g}$:

1. **Apply prior rotations to the new column.** For $j = 0, 1, \ldots, k-1$:
   $$(H[j, k], H[j+1, k]) \leftarrow \text{ApplyPlaneRotation}(c_j, s_j, H[j, k], H[j+1, k])$$
   This brings the leading $k$ entries of column $k$ into agreement with the upper-triangular structure being accumulated in $H[0..k-1, 0..k-1]$.

2. **Generate the new rotation.** Compute $(c_k, s_k) \leftarrow \text{GeneratePlaneRotation}(H[k, k], H[k+1, k])$ using the scaled-Givens formula. The returned pair satisfies $G(c_k, s_k) \cdot (H[k, k], H[k+1, k])^T = (r_{kk}, 0)^T$ for some $r_{kk} \geq 0$.

3. **Apply the new rotation to the column.** $(H[k, k], H[k+1, k]) \leftarrow \text{ApplyPlaneRotation}(c_k, s_k, H[k, k], H[k+1, k])$. After this, $H[k+1, k] = 0$ (numerically; up to the scaled-Givens accuracy).

4. **Propagate the rotation to $\bar{g}$.** $(\bar{g}[k], \bar{g}[k+1]) \leftarrow \text{ApplyPlaneRotation}(c_k, s_k, \bar{g}[k], \bar{g}[k+1])$. Since $\bar{g}[k+1]$ was zero before, this sets $\bar{g}[k+1] = -\bar{s}_k \cdot \bar{g}[k]_{\text{old}}$ and updates $\bar{g}[k]$ in place.

5. **Read the residual estimate.** The current least-squares residual norm is $\|r_{k+1}\| = |\bar{g}[k+1]|$.

The convergence test consumes $|\bar{g}[k+1]|$ and decides whether to continue to step $k+1$, restart, or hand off to the back-solve.

### Procedure: `back_solve(R, g_bar, k_final) -> y`

After the inner loop exits at step $k_{\text{final}}$ (either converged or hit $m_{\max}$), solve the triangular system $R[0..k_{\text{final}}, 0..k_{\text{final}}] \cdot y = \bar{g}[0..k_{\text{final}}]$ by back-substitution. The result $y$ is the GMRES least-squares minimizer; the correction to $x$ is $V_{k_{\text{final}}} \cdot y$.

## Open questions

- **L2 entry: primitive composition.** The `plane_rotation_step` procedure composes `apply_linop`-style primitives over a column slice plus a 2-vector pair; it is naturally expressed as a sequence of `givens` applications + one `givens_generate`. The L2 form should pin the canonical primitives.
- **L3 viability.** The application of stored rotations to a new column (step 1) is a sequential dependency chain — each rotation reads/writes adjacent entries top-to-bottom. This is a candidate L3 obstruction (the chain is genuinely sequential at length $k$). The generation step (step 2) is pointwise. The rotation application to $\bar{g}$ (step 4) is pointwise on a 2-vector pair. The composite step is therefore not globally tensor-liftable as one operation; the obstruction analysis belongs in the L2→L3 cycle.
- **Cross-slice consolidation.** Some downstream Krylov variants (e.g., MINRES, LSQR) also produce a stream of plane rotations against a Hessenberg/Bidiagonal column. Once the L1 form is stable, a SIDEWAYS comparison can extract the rotation-stream pattern as a shared concept.

## L1 — per-element procedure (plane-rotation stream)

**Scope note.** This section dissects the **plane-rotation stream** used by GMRES/FGMRES to reduce the upper-Hessenberg matrix $\bar{H}_m$ to upper-triangular $R_m$ incrementally. It is structurally distinct from the **block Gram-Schmidt orthogonalization** dissected in the earlier sections of this slice (which produces the Hessenberg column in the first place). The two streams meet inside `GmresSolver::Mult`'s inner loop: Gram-Schmidt emits column $H[\cdot, k]$; the plane-rotation stream then reduces it. Treating both under one slice is a structural choice — both are "orthogonalization machinery in the Krylov inner loop" — but the L1 forms are independent. (Open question: split this slice into `orthog/gram_schmidt.md` and `orthog/plane_rotation.md` once both reach L4. Recorded in Open questions.)

### State (plane-rotation stream)

During one GMRES cycle of up to $m_{\max}$ steps, the plane-rotation stream maintains:

- $c \in \mathbb{R}^{m_{\max}}$ — real cosines $c_k$, one per step (the rotation stream's own state).
- $s \in \mathbb{C}^{m_{\max}}$ — complex sines $s_k$ (real in the real-scalar specialization; the rotation stream's own state).
- $H \in \mathbb{C}^{(m_{\max}+1) \times m_{\max}}$ — upper-Hessenberg matrix, shared with the Arnoldi step; rotated in place column-by-column (post-rotation upper-triangular part is $R_m$).
- $\bar{g} \in \mathbb{C}^{m_{\max}+1}$ — transformed RHS, shared with the back-solve consumer; initialized to $(\beta, 0, \ldots, 0)$ with $\beta = \|r_0\|$, rotated in place as steps complete.

The pair $(c, s)$ persists across steps within one GMRES cycle; on restart it is reset.

### Primitive: `plane_rotation_step(k, H[\cdot, k], c, s, \bar{g})`

Given step index $k$, the freshly-produced Hessenberg column $H[0..k+1, k]$ (sub-diagonal $H[k+1, k]$ non-zero from Arnoldi), the accumulator arrays $(c, s)$ holding rotations $0..k-1$, and the running $\bar{g}$:

1. **Apply prior rotations to the new column.** For $j = 0, 1, \ldots, k-1$:
   $$(H[j, k], H[j+1, k]) \leftarrow \mathrm{ApplyPlaneRotation}(c_j, s_j, H[j, k], H[j+1, k])$$
   This brings the leading $k$ entries of column $k$ into agreement with the upper-triangular structure accumulated in $H[0..k-1, 0..k-1]$. The loop is **strictly sequential in $j$**: the output of iteration $j$ writes $H[j+1, k]$, which is the input of iteration $j+1$.

2. **Generate the new rotation.** $(c_k, s_k) \leftarrow \mathrm{GeneratePlaneRotation}(H[k, k], H[k+1, k])$ using the scaled-Givens formula. The returned pair satisfies $G(c_k, s_k) \cdot (H[k, k], H[k+1, k])^T = (r_{kk}, 0)^T$ with $r_{kk} \geq 0$.

3. **Apply the new rotation to the column.** $(H[k, k], H[k+1, k]) \leftarrow \mathrm{ApplyPlaneRotation}(c_k, s_k, H[k, k], H[k+1, k])$. After this, $H[k+1, k] = 0$ up to scaled-Givens accuracy.

4. **Propagate the rotation to $\bar{g}$.** $(\bar{g}[k], \bar{g}[k+1]) \leftarrow \mathrm{ApplyPlaneRotation}(c_k, s_k, \bar{g}[k], \bar{g}[k+1])$. Since $\bar{g}[k+1]$ was zero before, this sets $\bar{g}[k+1] = -\bar{s}_k \cdot \bar{g}[k]_{\text{old}}$ and updates $\bar{g}[k]$ in place.

5. **Read the residual estimate.** $\|r_{k+1}\| = |\bar{g}[k+1]|$ is the current least-squares residual norm, consumed by the convergence test.

### Invariant

After `plane_rotation_step(k, ...)` returns: the matrix $G(c_k, s_k) \cdots G(c_0, s_0)$ applied to the original $\bar{H}_m[0..k+1, 0..k]$ equals $R[0..k+1, 0..k]$, where $R[k+1, 0..k] = 0$ (upper-triangular through column $k$), and the same product applied to the original $\bar{g}_0 = (\beta, 0, \ldots, 0)^T$ equals the current $\bar{g}[0..k+1]$. Equivalently: $\|R[0..k, 0..k] \cdot y - \bar{g}[0..k]\|^2 + |\bar{g}[k+1]|^2 = \|\bar{H}_m[0..k+1, 0..k] \cdot y - \beta e_1\|^2$ for any $y \in \mathbb{C}^{k+1}$, so minimizing the left side's first term yields the GMRES iterate and the second term gives the residual norm.

### Primitive: `back_solve_R(R, \bar{g}, k_\text{final}) \to y$

After the inner loop exits at step $k_{\text{final}}$, solve $R[0..k_\text{final}, 0..k_\text{final}] \cdot y = \bar{g}[0..k_\text{final}]$ by back-substitution. The result $y$ is the GMRES least-squares minimizer; the correction to $x$ is $V_{k_\text{final}} \cdot y$. This primitive is a [`trsv`](../../concepts/trsv.md) against the in-place-rotated $R$.

### Variant axes (plane-rotation stream)

Per `## Variant axes` above, the rotation stream has no runtime variant axis. All three axes (scalar type, generation formula, storage layout) are absorbed at L1: the L1 procedure does not branch on any of them. The scalar-type axis is parametric — real and complex specializations of `GeneratePlaneRotation` exist at L0 but share the L1 statement (the conjugation $\bar{s}$ in step 4 collapses to $s$ when the scalar is real).

### Open questions

- **Slice split.** Once both streams reach L4, split this slice into `orthog/gram_schmidt.md` (block-GS variants) and `orthog/plane_rotation.md` (the Givens stream + back-solve). The two streams share only the GMRES inner loop as a caller; they do not share primitives.
- **L2 entry.** The L1 form composes [`givens`](../../concepts/givens.md) applications + one `givens_generate`; step 1's loop is naturally `givens` applied to a column slice. The L2 form should pin the canonical primitives (likely: `givens_generate`, `givens` applied to a 2-vector pair, plus a length-$k$ sequential loop of `givens` applications to the column).
- **L3 viability.** Step 1's loop is genuinely sequential at length $k$ ([sequential-obstruction](../../concepts/sequential-obstruction.md) candidate); steps 2-4 are pointwise on a 2-vector pair. The L3 lift will likely be a partial obstruction analogous to MGS in the Gram-Schmidt stream.

### Citations

- [palace/linalg/gmres.cpp:GeneratePlaneRotation](../../../../reference/palace/linalg/gmres.cpp) — generation of $(c_k, s_k)$ via the scaled-Givens formula. Real and complex specializations.
- [palace/linalg/gmres.cpp:ApplyPlaneRotation](../../../../reference/palace/linalg/gmres.cpp) — in-place application of a stored rotation to a 2-vector pair.
- [palace/linalg/gmres.cpp:GmresSolver::Mult](../../../../reference/palace/linalg/gmres.cpp) inner loop — the integrating driver: apply prior rotations to the new column, generate, apply, propagate to $\bar{g}$.
- [palace/linalg/gmres.cpp:GmresSolver::Mult](../../../../reference/palace/linalg/gmres.cpp) back-substitution — consumes $R_m$ and $\bar{g}_m$ to produce the least-squares minimizer $y_m$.
- [palace/linalg/gmres.cpp:FgmresSolver::Mult](../../../../reference/palace/linalg/gmres.cpp) — same plane-rotation stream; the variation is in the Arnoldi step (storing $Z = M^{-1} V$ in addition to $V$).

### Test linkage

No direct unit tests for the plane-rotation stream in isolation; correctness is covered indirectly through GMRES/FGMRES convergence tests on the wider system. The scaled-Givens formula's robustness (no spurious over/underflow) is implicit in the standard GMRES tests passing on ill-conditioned matrices in the integration test suite. Recording the absence: a dedicated unit test for `GeneratePlaneRotation` / `ApplyPlaneRotation` would tighten verification but is not present in the current Palace test suite.
