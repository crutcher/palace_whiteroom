# arnoldi_step

## Context

The single-step Arnoldi inner body is the innermost kernel of GMRES (and, externally, of SLEPc's Krylov-Schur eigensolver path). One step accepts the prior orthonormal Krylov basis `V[0..j]` and produces (a) a new orthonormal basis column `V[j+1]` and (b) the j-th column of the upper-Hessenberg matrix `H̄`. It is the dataflow boundary between **field-side** primitives (operator apply, dot, axpy, norm — MPI-collective) and **small-dense-side** primitives (Hessenberg-column update, Givens rotations — pointwise scalar). The slice isolates this boundary so that the [gmres](./gmres.md) slice can state its outer loop at L1 in terms of `arnoldi_step` alone, without re-deriving the orthogonalisation choice each cycle.

## Background

Standard formulation: Saad 2003 *Iterative Methods for Sparse Linear Systems* §6.3 (the Arnoldi process) and §6.5 (use inside GMRES). The classical loop is

    w ← A·V[j]
    for i = 0..j:  H[i,j] ← ⟨w, V[i]⟩;  w ← w − H[i,j]·V[i]   (MGS form)
    H[j+1,j] ← ‖w‖₂
    V[j+1] ← w / H[j+1,j]

Variants in the field: MGS (the form above), classical Gram-Schmidt (CGS, a single batched projection — less stable but a single MPI allreduce), and CGS with one reorthogonalisation pass (CGS2, two batched allreduces — recovers MGS-level stability with batched comms). Palace exposes all three under the runtime tag `gs_orthog ∈ {MGS, CGS, CGS2}`; the choice is preserved as a residual variant axis through L1.

Palace deviates from the textbook in three ways: (1) the operator applied is the constructed operator `BA` (or `AB`, or `A`) rather than `A` directly, absorbing the preconditioner-side variant — see [apply_BA](./gmres.md#apply_BA); (2) FGMRES additionally retains the per-step preconditioned basis `Z[j]` as threaded state for the flexible solution reconstruction; (3) basis storage is allocated lazily in chunks rather than as a single `(max_dim+1)`-column block, which is invisible to the algorithmic contract.

This slice scopes only the in-repo Arnoldi step. The SLEPc/ARPACK eigensolver paths configure their own Arnoldi implementations behind a [constructed-operator surface](../../concepts/constructed-operators.md); they emit no Arnoldi-step primitives in Palace's own dataflow and are tracked separately (eigensolver slice not yet extracted), not here.

## Sources

- [palace/linalg/iterative.cpp:614-642](../../../reference/palace/linalg/iterative.cpp#L614-L642) — `GmresSolver::Mult` Arnoldi inner-loop body; the four-line kernel proper is lines 621-628 (`ApplyBA` → `OrthogonalizeIteration` → `Norml2` → in-place `scal`).
- [palace/linalg/iterative.cpp:734-740](../../../reference/palace/linalg/iterative.cpp#L734-L740), [794-822](../../../reference/palace/linalg/iterative.cpp#L794-L822) — `FgmresSolver::Mult` Arnoldi inner body; structurally identical to GMRES, with `ApplyBA(PreconditionerSide::RIGHT, …)` hard-wired and `Z[j]` promoted to threaded state.
- [palace/linalg/iterative.cpp:288-305](../../../reference/palace/linalg/iterative.cpp#L288-L305) — `ApplyBA` constructed-operator dispatch (LEFT: `A->Mult` then `ApplyB`; RIGHT: `ApplyB` then `A->Mult`; NONE: `A->Mult` direct).
- [palace/linalg/iterative.cpp:308-325](../../../reference/palace/linalg/iterative.cpp#L308-L325) — `OrthogonalizeIteration` wrapper: variant dispatch over MGS / CGS / CGS2 (CGS with `refine=true`).
- [palace/linalg/orthog.hpp:38-89](../../../reference/palace/linalg/orthog.hpp#L38-L89) — `OrthogonalizeColumnMGS` and `OrthogonalizeColumnCGS` implementations: MGS does m sequential `dot+allreduce+axpy` triples; CGS does one batched allreduce of m dots followed by m axpys (+ optional refinement pass for CGS2).
- [palace/linalg/iterative.cpp:519-541](../../../reference/palace/linalg/iterative.cpp#L519-L541) — `GmresSolver::Update`: lazy basis-and-Hessenberg resize by `add_size` columns when triggered from inner loop at `V[j+1].Size()==0`.
- [palace/linalg/iterative.cpp:544-550](../../../reference/palace/linalg/iterative.cpp#L544-L550) — `FgmresSolver::Update`: same as GMRES `Update` plus parallel growth of the preconditioned basis array `Z`.
- [palace/linalg/iterative.cpp:73-109](../../../reference/palace/linalg/iterative.cpp#L73-L109) — `GeneratePlaneRotation` (real specialisation).
- [palace/linalg/iterative.cpp:111-224](../../../reference/palace/linalg/iterative.cpp#L111-L224) — `GeneratePlaneRotation` (complex specialisation).
- [palace/linalg/iterative.cpp:227-241](../../../reference/palace/linalg/iterative.cpp#L227-L241) — `ApplyPlaneRotation`.
- [test/unit/test-orthog.cpp:80-170](../../../reference/palace/test/unit/test-orthog.cpp#L80-L170), [234-280](../../../reference/palace/test/unit/test-orthog.cpp#L234-L280) — parametric tests for `OrthogonalizeColumnMGS`/`CGS` across real / complex / B-weighted variants; verifies post-orthog `⟨w, V[i]⟩ ≈ 0`.

## L0 — palace source

The in-repo Arnoldi step is the four-line kernel inside the restart loop of `GmresSolver::Mult` (and FGMRES's near-identical sibling). Letting `j` be the current inner index, `V` the basis array, `H` the (max_dim+1)×max_dim Hessenberg buffer, and `Hj := &H[j*(max_dim+1)]` the j-th Hessenberg column:

    // [palace/linalg/iterative.cpp:621-628]
    VecType &w = V[j + 1];                                // alias, NOT copy: w *is* the destination slot
    if (w.Size() == 0) { Update(j); }                     // lazy resize by add_size columns; hidden at L1
    ApplyBA(pc_side, A, B, V[j], w, r, …);                // w ← (BA or AB or A) · V[j]
    Hj = H.data() + j * (max_dim + 1);                    // pointer to j-th Hessenberg column
    OrthogonalizeIteration(gs_orthog, comm, V, w, Hj, j); // Hj[0..j] ← ⟨w_pre, V[i]⟩;  w ← w − Σ Hj[i]·V[i]
    Hj[j+1] = linalg::Norml2(comm, w);                    // subdiagonal entry (post-orthog norm); MPI allreduce inside
    w *= 1.0 / Hj[j+1];                                   // in-place scal; w==V[j+1] is now unit-norm

The four lines correspond to four [rotations](../../concepts/rotation.md):

1. **operator apply** via the constructed operator `BA` (or `AB`, or `A`) — [apply_BA](./gmres.md#apply_BA);
2. **orthogonalisation** against the prior basis — [orthog](./orthog.md), variant-dispatched on `gs_orthog`;
3. **subdiagonal-norm** computation — [nrm2](../../concepts/nrm2.md) with MPI allreduce;
4. **in-place scaling** of the new basis column — [scal](../../concepts/scal.md).

The FGMRES variant ([palace/linalg/iterative.cpp:794-822](../../../reference/palace/linalg/iterative.cpp#L794-L822)) replaces the scratch `r` with the per-step preconditioned basis column `Z[j]` and hard-wires `pc_side = PreconditionerSide::RIGHT` at the `ApplyBA` call site. `Z[j]` is itself promoted to threaded state and consumed during solution reconstruction; otherwise the Arnoldi-step contract is unchanged.

Three distinct in-place writes occur concurrently in the kernel: (1) `w` (a reference, not a copy, to the basis slot `V[j+1]` — see line 622 `VecType &w = V[j+1]`) is written by `ApplyBA`, mutated by `OrthogonalizeIteration` (project-and-subtract), and finally scaled in place — the final `scal` is therefore *also* the act of installing the new basis column, with no separate copy; (2) `Hj` is an accumulator-style write into the j-th Hessenberg column (indices `[0..j]` from `OrthogonalizeIteration`, index `j+1` from `Norml2`); (3) `r` is a scratch buffer used only when a preconditioner is present (the `pc_side == NONE` branch of `ApplyBA` at [iterative.cpp:303](../../../reference/palace/linalg/iterative.cpp#L303) calls `A->Mult(x,y)` directly and never touches `r`).

Breakdown (`Hj[j+1] == 0`) is not explicitly guarded at line 627; it would manifest downstream as a division-by-zero in the rotation-generate step at [iterative.cpp:638-640](../../../reference/palace/linalg/iterative.cpp#L638-L640) and surface via `CheckDot` on line 643.

### Variant axes

The step admits three orthogonal axes of variation at L0:

- **Operator-apply variant** (`pc_side ∈ {LEFT, RIGHT, NONE}`): absorbed by the constructed operator `BA` per [constructed-operators](../../concepts/constructed-operators.md). The kernel calls `ApplyBA(...)` uniformly; `pc_side` does not appear in the per-step procedure.
- **Orthogonalisation variant** (`gs_orthog ∈ {MGS, CGS, CGS2}`): preserved as a residual axis; the variant changes the MPI-collective shape (1·j allreduces for MGS; one batched allreduce for CGS; two batched allreduces for CGS2) but not the L1 functional contract.
- **Krylov flavour** (GMRES vs FGMRES): adds `Z[j]` to threaded state. The Arnoldi step proper is identical; the difference shows up in the outer GMRES slice, not here.

Basis storage is allocated lazily (init_size=5 columns, add_size=10 columns per resize, triggered when `V[j+1].Size()==0`); the slice hides this entirely.

## L1 — invariants and procedure

### State

    inputs:
      A         : LinOp                         -- system operator
      B         : LinOp (optional)              -- preconditioner; constructs BA at solve setup
      gs_orthog : {MGS, CGS, CGS2}              -- orthogonalisation variant (residual axis)
      V[0..j]   : OrthonormalBasis              -- prior Krylov basis (V[i] unit-norm, mutually orthogonal)
      j         : InnerIndex

    outputs:
      V[j+1]    : BasisVector                   -- new unit-norm basis column
      H[:,j]    : HessenbergColumn (length j+2) -- H[0..j] = projection coeffs;  H[j+1] = ‖w_post-orthog‖₂

### Invariants

- **Input precondition.** `V[0..j]` is orthonormal: `⟨V[i], V[k]⟩ = δ_{ik}` for `0 ≤ i,k ≤ j`.
- **Arnoldi relation.** Letting `T` denote the constructed operator (`BA`, `AB`, or `A` per [apply_BA](./gmres.md#apply_BA)),

      T · V[j]  =  Σ_{i=0}^{j+1} H[i,j] · V[i]

  with `H[i,j] = ⟨T·V[j], V[i]⟩` for `i ≤ j` (under exact arithmetic) and `H[j+1,j] = ‖(I − P_{V[0..j]}) T·V[j]‖₂`.
- **Output postcondition.** `V[j+1]` is unit-norm and orthogonal to `V[0..j]` (under exact arithmetic; under finite precision, to the level afforded by the chosen `gs_orthog` variant — see [orthog](./orthog.md)).
- **Breakdown.** `H[j+1,j] = 0` signals lucky breakdown: `V[j] ∈ span{V[0..j-1], T·v_0}` is `T`-invariant; the caller terminates the restart with the exact-arithmetic Krylov subspace.

### Procedure

    arnoldi_step(V, j, T, gs_orthog) -> (V[j+1], H[:,j]):
      w        ← T(V[j])                                  -- operator apply
      H[0..j]  ← project(w, V[0..j]; gs_orthog)            -- orthogonalisation; w ← w − Σ H[i,j]·V[i] in place
      H[j+1,j] ← ‖w‖₂                                      -- subdiagonal norm
      V[j+1]   ← w / H[j+1,j]                              -- normalise

The procedure mentions the variant tag `gs_orthog` exactly once, at the orthogonalisation call site (level (b) of [variant-absorption](../../concepts/variant-absorption.md)). The operator-apply variant is fully absorbed by the constructed-operator surface and does not appear here. The post-Arnoldi Hessenberg-column triangularisation (replay-and-generate Givens rotations on `H[:,j]`) is **not** part of the Arnoldi step; it is the small-dense incremental-least-squares update consumed by [gmres](./gmres.md) at L2, tracked under [incremental-least-squares](../../concepts/incremental-least-squares.md).

### Residual variant axis

`gs_orthog` is preserved as a first-class residual axis (see [variant-absorption](../../concepts/variant-absorption.md)). All three variants share the L1 contract above; they differ in MPI-collective shape and in stability under finite arithmetic. The variant is bound at solve setup and is not re-inspected per step.

## Open questions

- The post-Arnoldi small-dense Givens-QR triangularisation has been recorded across prior cycles as a distinct sequential obstruction. Currently this slice excludes it (it belongs to the GMRES outer loop's incremental-least-squares concept). Should it instead be folded in here as a logical third phase? Current call: keep separate — the Arnoldi step is the field-side / boundary kernel; the small-dense update is consumed elsewhere.
- The eigensolver path (SLEPc Krylov-Schur, ARPACK) provides an external Arnoldi implementation reached via a constructed-operator binding at configure time. Scoped out of this slice; tracked separately (eigensolver slice not yet extracted).
- The orthogonalisation sub-primitive *is* directly tested: [test/unit/test-orthog.cpp:80-170](../../../reference/palace/test/unit/test-orthog.cpp#L80-L170) parametrises over `{MGS, CGS, CGS2}` (with real, complex, and B-weighted variants at lines 234-280), verifying the post-orthog orthogonality condition `⟨w, V[i]⟩ ≈ 0`. The four-line Arnoldi-step kernel as a unit, however, has no direct unit test — coverage is via end-to-end GMRES integration only. Flagged as a tooling gap (low priority).
- The scratch buffer `r` in GMRES is unused when no preconditioner is present (the `pc_side == NONE` branch of `ApplyBA` calls `A->Mult(x, y)` directly). An L0-storage refinement, not visible at L1.

## L2 — primitive composition

The L1 procedure unfolds into four named primitive invocations. Three are field-side (MPI-collective vectors over the global DoF space); one is dispatch over the [orthog](./orthog.md) variant, itself a small composition of field-side primitives plus a residual choice.

```
arnoldi_step_L2(V, j, T, gs_orthog) -> (V[j+1], H[:,j]):
  apply_BA       :  w        ← apply_linop(T, V[j])
  orthogonalize  :  H[0..j]  ← orthogonalize(gs_orthog, comm, V[0..j], w)   -- mutates w in place
  subdiag_norm   :  H[j+1,j] ← nrm2(comm, w)
  normalize      :  scal(1 / H[j+1,j], w)                                    -- w aliases V[j+1]
```

The four building blocks correspond to four L0 lines and four distinct concept entries:

### apply_BA

The operator apply `w ← T(V[j])` is the constructed-operator surface [apply_BA](./gmres.md#apply_BA). At L2 it reads as a single uniform call `apply_linop(T, V[j])` regardless of preconditioner side (`LEFT`, `RIGHT`, `NONE`) — the `pc_side` variant is internalised at solve setup per [constructed-operators](../../concepts/constructed-operators.md) and does not appear in the per-step composition. The output `w` is a fresh DoF-space vector aliased to the buffer that will become `V[j+1]` after the remaining three primitives. See [apply_linop](../../concepts/apply_linop.md).

FGMRES additionally retains the per-step preconditioned column `Z[j]` from this apply as threaded state; the Arnoldi-step composition at L2 is unchanged, but the GMRES outer loop tees off `Z[j]` here. The teeing-off is a write to a separate buffer, not a transformation of `w`, so it does not alter the four-primitive shape.

### orthogonalize

The projection `H[0..j] ← project(w, V[0..j]; gs_orthog)` with in-place subtraction `w ← w − Σ H[i,j]·V[i]` unfolds into the [orthog](./orthog.md) slice, which is itself a composition of [dot](../../concepts/dot.md) and [axpy](../../concepts/axpy.md) (plus a batched [gemv_basis](../../concepts/gemv_basis.md) call for CGS/CGS2 to amortise the MPI allreduce). The residual variant axis `gs_orthog ∈ {MGS, CGS, CGS2}` is bound at solve setup and dispatched here exactly once; the L2 composition for the Arnoldi step itself is variant-independent — only the unfolding of `orthogonalize` into its inner primitive chain differs. See [orthog](./orthog.md) §L2 for the inner unfolding and [variant-absorption](../../concepts/variant-absorption.md) level (b) for the dispatch-once discipline.

The procedure both reads `V[0..j]` and writes the j-th column of `H` (an accumulator-style write into the small-dense Hessenberg buffer) and mutates `w` in place. The Hessenberg write `H[0..j]` is a small-dense scalar accumulation; the global-vector mutation `w` is the load-bearing field-side work.

### subdiag_norm

The subdiagonal entry `H[j+1,j] = ‖w‖₂` is the [nrm2](../../concepts/nrm2.md) primitive over the post-orthogonalisation residual, with one MPI allreduce. It is a pure read on `w` — no mutation — producing a single scalar written into the Hessenberg column. Breakdown detection at L1 reads off this scalar (`H[j+1,j] = 0` ⇒ `T`-invariant subspace).

### normalize

The final `w ← w / H[j+1,j]` is in-place [scal](../../concepts/scal.md) with reciprocal scalar. Because `w` and `V[j+1]` alias the same buffer (the basis array entry was the destination of `apply_BA`), this primitive is also the act of installing the new basis column. No `copy` is needed.

### Composition shape

The four primitives have no internal data dependency cycle:

- `apply_BA` produces `w` from `V[j]` and the constructed operator.
- `orthogonalize` reads `V[0..j]` and `w`, writes `H[0..j]`, mutates `w`.
- `subdiag_norm` reads `w`, writes `H[j+1,j]`.
- `normalize` reads `H[j+1,j]`, mutates `w`.

The sequential chain `apply_BA → orthogonalize → subdiag_norm → normalize` is forced by these dataflow edges: `orthogonalize` needs `w` after apply; `subdiag_norm` needs `w` after orthogonalisation; `normalize` needs the scalar from `subdiag_norm`. No reordering is possible without changing semantics. The chain shape is invariant across `gs_orthog` and `pc_side` — both variants are absorbed at the primitive boundary (`orthogonalize` and `apply_linop` respectively).

The small-dense Hessenberg-column triangularisation (replay Givens 1..j, generate new rotation, apply to `H[:,j]` and the residual-norm vector) is **not** part of this composition — it is consumed by the GMRES outer loop's [incremental-least-squares](../../concepts/incremental-least-squares.md) update, deliberately scoped out per the slice's L1 statement.

### Mutation legibility

Per mutation-pseudocode discipline, the in-place writes are visible in the primitive names:

- `orthogonalize(..., w)` — `w` is the accumulator-mutation argument (signature of [orthog](./orthog.md) makes this explicit).
- `scal(α, w)` — in-place by definition of [scal](../../concepts/scal.md).
- `apply_linop(T, V[j])` — pure functional form returning a fresh `w` (the buffer pre-allocation is an L0 storage detail, invisible at L2).

No silently-aliasing assignment appears; the four-line composition is unambiguous about which buffers are mutated and which are read.

## L3 — tensor-field lift

The L2 composition is a sequence of four primitives operating on global DoF-space vectors with one small-dense accumulator-write into the j-th Hessenberg column. Lifting to L3 means asking whether the per-step procedure can be re-expressed as a single global tensor-field operation, in the sense of [tensor-field-lift](../../concepts/tensor-field-lift.md).

The answer is **partial lift with a sequential obstruction**. Three of the four primitives lift cleanly; the fourth (`orthogonalize` in its MGS form) carries a [sequential-obstruction](../../concepts/sequential-obstruction.md) that is irreducible at L3 under the MGS variant, and is only partially lifted under CGS / CGS2.

### Field-side lift of the three uncontested primitives

- **`apply_BA`** is the global operator apply `w ← T · V[j]`. The operator `T` is a constructed linear operator over the DoF tensor field; one application is a single global field-side operation by construction. See [apply_linop](../../concepts/apply_linop.md) — already a tensor-field operation; nothing to lift.
- **`subdiag_norm`** is `H[j+1,j] ← ‖w‖₂`, a single global reduction over the DoF-tensor field. The MPI allreduce is the lift's realisation. See [nrm2](../../concepts/nrm2.md).
- **`normalize`** is `w ← (1/α) · w`, an element-wise scaling over the DoF tensor field with a broadcast scalar. Pointwise, embarrassingly parallel. See [scal](../../concepts/scal.md).

All three are already in tensor-field form at L2; the L3 lift is identity-shaped (no new structure to surface). They are listed here for completeness — the L2→L3 edge is a no-op rotation for each.

### Orthogonalisation: variant-dependent lift

The orthogonalisation primitive `H[0..j] ← project(w, V[0..j]; gs_orthog)` is the only step whose lift depends on the residual variant axis. Under each `gs_orthog` value the global form differs:

- **CGS (classical Gram-Schmidt)**: the entire projection is a single batched operation

      H[0..j]  ←  V[0..j]ᵀ · w      -- one batched dot, one MPI allreduce
      w         ←  w − V[0..j] · H[0..j]      -- one batched axpy / gemv

  This is a clean tensor-field lift: `V[0..j]` is a `(n_dof, j+1)` global tensor; `H[0..j]` is a `(j+1)`-vector; the two operations are global [gemv_basis](../../concepts/gemv_basis.md) calls. One allreduce, no per-`i` sequencing. CGS achieves full L3 lift.

- **CGS2 (CGS with one reorthogonalisation pass)**: CGS twice. Two batched gemv pairs, two allreduces. Same shape as CGS, so the L3 lift is the CGS form applied twice in sequence. The two passes are themselves sequentially dependent (the second pass projects against the residual of the first), but each pass is a global tensor-field operation. L3-lifted modulo the outer two-pass sequencing, which is finite and shape-invariant — not a true sequential obstruction.

- **MGS (modified Gram-Schmidt)**: the loop

      for i = 0..j:
          H[i,j] ← ⟨w, V[i]⟩       -- one allreduce per i
          w       ← w − H[i,j] · V[i]   -- one axpy per i, depends on H[i,j]

  carries a [sequential-obstruction](../../concepts/sequential-obstruction.md): the `i+1`-th dot product reads `w` after the `i`-th axpy has updated it, so the projection coefficients `H[0..j]` cannot be computed as a single batched `V[0..j]ᵀ · w`. The data dependency `H[i+1,j]` ← f(w_after_axpy_i) ← f(H[i,j])` is genuinely sequential under MGS semantics. The lift is **obstructed at L3** for the MGS variant; the obstruction is the algorithmic distinction that motivates MGS over CGS (better backward stability per iteration through the sequential refresh of `w`).

This is a textbook variant-dependent obstruction: changing `gs_orthog` from CGS to MGS removes the L3 lift. The obstruction is not eliminable by reformulation — it is the defining feature of the MGS algorithm.

### Hessenberg-column write

The small-dense write `H[0..j] ← ⟨w, V[0..j]⟩` is into a `(j+1)`-vector indexed by the small Hessenberg-column space, not the DoF tensor field. It is L3-trivial: small-dense scalar accumulation, no parallelism question. The interesting structural property is that this small-dense vector becomes input to the [incremental-least-squares](../../concepts/incremental-least-squares.md) machinery in the outer GMRES slice — a separate small-dense tensor-field over the Krylov-subspace index space.

### Combined L3 form

Under CGS / CGS2 the entire step lifts to a sequence of global tensor-field operations:

```
arnoldi_step_L3_cgs(V, j, T) -> (V[j+1], H[:,j]):
  w        ← apply_linop(T, V[j])                 -- field-side, global
  H[0..j]  ← V[0..j]ᵀ · w                          -- global gemv_basis (batched dot), 1 allreduce
  w        ← w − V[0..j] · H[0..j]                 -- global gemv (batched axpy), no comm
  -- CGS2 only: repeat the above two lines, accumulating into H[0..j]
  H[j+1,j] ← nrm2(w)                                -- 1 allreduce
  scal(1 / H[j+1,j], w)                             -- pointwise
```

Under MGS the orthogonalisation block is irreducibly the per-`i` loop; the surrounding three primitives lift cleanly, but the step as a whole carries the MGS sequential obstruction at L3.

The L2→L3 edge is therefore a **conditional lift**: clean under CGS / CGS2, obstructed under MGS. The variant axis `gs_orthog` is the structural switch that determines whether L3 reveals a global form or preserves the sequential one. This is recorded as a first-class negative result per the L2→L3 obstruction-as-output discipline.

### MPI-collective shape (L3 observable)

The L3 view makes the MPI-collective shape per step explicit:

- MGS: `j+1` allreduces in the orthogonalisation block, `+1` for `nrm2`, total `j+2`.
- CGS: 1 allreduce (batched orthogonalisation), `+1` for `nrm2`, total 2.
- CGS2: 2 allreduces (two CGS passes), `+1` for `nrm2`, total 3.

This is the load-bearing distinction that motivates the variant axis in distributed-memory practice: MGS pays an allreduce per inner iteration; CGS / CGS2 pay a constant number. The L3 form is where this shape becomes a first-class property of the algorithm rather than an implementation incident.

## L4 — calculus form

The L3 form splits the step into a clean field-side composition plus an in-place small-dense Hessenberg-column write, with the orthogonalisation block carrying a [sequential-obstruction](../../concepts/sequential-obstruction.md) under the MGS variant. The L4 lift expresses the step against the calculus of `book/src/design/l4_calculus.md`: explicit state stratification (sim / operator-internal / ephemeral), monadic coordination of the in-place writes, and a typed variant-axis surface that makes the residual `gs_orthog` choice a parameter of the operator-internal table rather than per-step runtime data.

See [solve-monad](../../concepts/solve-monad.md), [state-stratification](../../concepts/state-stratification.md), and [derived-view-hoisting](../../concepts/derived-view-hoisting.md) for the calculus-level patterns invoked below.

### State stratification

The per-step procedure touches three distinct state strata:

```ts
// Simulation state — evolves across solver steps; persisted across restarts.
type ArnoldiSimState = {
  V: BasisChunk[];                 // lazy-allocated orthonormal basis; V[0..j] is the prior subspace
  H: HessenbergBuffer;             // (max_dim+1) x max_dim small-dense; H[:,0..j-1] populated
  j: InnerIndex;                   // current inner iteration
};

// Operator-internal params — bound at solve setup; immutable across the step.
type ArnoldiOpParams = {
  T: ConstructedLinOp;             // BA / AB / A — pc_side absorbed; see apply_BA
  comm: MpiComm;
  gs_orthog: "MGS" | "CGS" | "CGS2";  // residual variant axis; dispatched once at setup
};

// Ephemeral intermediates — created and consumed within one step.
type ArnoldiStepScratch = {
  w: DofVector;                    // aliases the buffer that becomes V[j+1] on success
  // FGMRES extension: Z[j] is teed off here; promoted to ArnoldiSimState in the FGMRES specialisation.
};
```

The sim/op/ephemeral split makes three properties first-class. (1) `V` and `H` are the only writes that persist past the step return; the calculus monad sequences them. (2) `T` and `gs_orthog` are operator-internal and never appear as per-step arguments — the variant-absorption discipline at level (b) is expressed in the type: the step procedure does not take `gs_orthog` as a parameter, the orthogonalisation operator does, once, at construction. (3) `w` is ephemeral; its in-place mutation across the four primitives is contained to a single `do`-block and not observable outside it.

### Monadic procedure

```haskell
arnoldiStep :: ArnoldiOp -> SolveM ArnoldiSimState ()
arnoldiStep op = do
  s <- get
  let j     = s.j
      V_j   = basisAt s.V j
      V_pre = basisPrefix s.V j       -- derived view: V[0..j], hoisted per derived-view-hoisting
      H_col = hessColumn s.H j         -- derived view: H[:,j]
  withScratch DofVector $ \w -> do
    applyLinop op.T V_j w                         -- field-side; produces w
    orthogonalize op.orthog V_pre w (H_col[0..j]) -- field-side, allreduces per gs_orthog; mutates w, writes H[:,j] head
    h_jp1 <- nrm2 op.comm w                       -- field-side reduction
    writeAt H_col (j+1) h_jp1                     -- small-dense scalar write
    scal (recip h_jp1) w                          -- pointwise; w aliases new basis slot
    installBasisColumn s.V (j+1) w                -- transfers ephemeral w into sim state
  modify (\s -> s { j = s.j + 1 })
```

The `SolveM ArnoldiSimState` monad is the [solve-monad](../../concepts/solve-monad.md) specialised to this slice's sim state. `withScratch` brackets the ephemeral `w` so the in-place mutations are syntactically contained — the calculus expresses what the L2 mutation-pseudocode discipline expresses informally. `installBasisColumn` is the moment the ephemeral becomes sim state; it is the only write that escapes the `withScratch` bracket.

### Derived views

Two derived views are hoisted out of the sim state per [derived-view-hoisting](../../concepts/derived-view-hoisting.md):

- `basisPrefix s.V j` — the `(n_dof, j+1)` prior-basis view consumed by `orthogonalize`. Hoisted because the L3 CGS form treats it as a tensor-field operand (`V[0..j]ᵀ · w`); the calculus form makes the view a first-class operand rather than an index range.
- `hessColumn s.H j` — the `(max_dim+1)`-vector view of the j-th Hessenberg column, written by `orthogonalize` (head) and `nrm2` (subdiagonal). Hoisting it surfaces the small-dense write target as a single named operand and lets the L4 form sequence the two writes monadically.

No other state is hoisted; `T`, `gs_orthog`, and `comm` stay in `op` (operator-internal) and `w` stays ephemeral.

### Variant axis at L4

The `gs_orthog` axis is operator-internal: it parameterises the construction of `op.orthog` at solve setup but does not appear in `arnoldiStep`'s body. This is level-(b) [variant-absorption](../../concepts/variant-absorption.md) realised in the type system: the step procedure has the same syntactic shape across MGS, CGS, and CGS2; only the operator-internal `orthog` field differs. The MGS sequential obstruction recorded at L3 is, at L4, a property of the `orthogonalize` primitive's implementation, not of the step's calculus form — the step is variant-independent at L4 even though its allreduce count is not.

### Interaction with FGMRES

The FGMRES specialisation extends `ArnoldiSimState` with `Z : BasisChunk[]` and promotes the apply's output buffer to sim state at the `installBasisColumn` step. The monadic form makes the extension localised: the four-line scratch block is unchanged; only the `withScratch` exit transfers an additional buffer. The L4 contract for the Arnoldi step itself is unchanged; the change is at the level of the sim-state type.

### Obstruction recording

The L2→L3 negative result (MGS orthogonalisation does not lift) is preserved at L4 as a property of the `orthogonalize` primitive's implementation, not erased by the calculus form. The calculus expresses *what* the step does monadically; it does not pretend the MGS sequential dependency between successive `H[i,j]` reads of `w` has disappeared. The obstruction is internal to `orthogonalize`'s `SolveM` implementation under the MGS variant, and the [sequential-obstruction](../../concepts/sequential-obstruction.md) concept entry remains the load-bearing record.

### Composition shape, restated

Reading the L4 form top-to-bottom, the step is: bind sim state; derive two views; bracket an ephemeral DoF vector; perform four primitive operations on it (one field-side apply, one orthogonalisation, one reduction, one scaling); install the result; bump the inner index. The four-primitive composition shape from L2 is preserved; what's added at L4 is the typed account of which writes are sim-state versus ephemeral and the monadic sequencing of the in-place mutations.
