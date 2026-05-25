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

Palace deviates from the textbook in three ways: (1) the operator applied is the constructed operator `BA` (or `AB`, or `A`) rather than `A` directly, absorbing the preconditioner-side variant — see [apply_BA](./gmres/apply_BA.md); (2) FGMRES additionally retains the per-step preconditioned basis `Z[j]` as threaded state for the flexible solution reconstruction; (3) basis storage is allocated lazily in chunks rather than as a single `(max_dim+1)`-column block, which is invisible to the algorithmic contract.

This slice scopes only the in-repo Arnoldi step. The SLEPc/ARPACK eigensolver paths configure their own Arnoldi implementations behind a [constructed-operator surface](../concepts/constructed-operators.md); they emit no Arnoldi-step primitives in Palace's own dataflow and are tracked under [eigensolver](./eigensolver.md), not here.

## Sources

- [palace/linalg/iterative.cpp:615-640](../../../reference/palace/linalg/iterative.cpp#L615-L640) — `GmresSolver::Mult` Arnoldi inner-body kernel (the four-line ApplyBA / OrthogonalizeIteration / Norml2 / scal sequence).
- [palace/linalg/iterative.cpp:735-825](../../../reference/palace/linalg/iterative.cpp#L735-L825) — `FgmresSolver::Mult` Arnoldi inner body; identical contract, with `Z[j]` promoted to threaded state.
- [palace/linalg/iterative.cpp:287-325](../../../reference/palace/linalg/iterative.cpp#L287-L325) — `ApplyBA` constructed-operator dispatch (left/right/no preconditioner).
- [palace/linalg/orthog.hpp:38-89](../../../reference/palace/linalg/orthog.hpp#L38-L89) — `OrthogonalizeIteration` variant dispatch over MGS/CGS/CGS2.
- [palace/linalg/iterative.cpp:73-109](../../../reference/palace/linalg/iterative.cpp#L73-L109) — `GeneratePlaneRotation` (real specialisation).
- [palace/linalg/iterative.cpp:111-224](../../../reference/palace/linalg/iterative.cpp#L111-L224) — `GeneratePlaneRotation` (complex specialisation).
- [palace/linalg/iterative.cpp:227-241](../../../reference/palace/linalg/iterative.cpp#L227-L241) — `ApplyPlaneRotation`.
- [palace/linalg/iterative.cpp:489-541](../../../reference/palace/linalg/iterative.cpp#L489-L541) — `OrthogonalizeIteration` wrapper and basis `Update`/lazy-resize.

## L0 — palace source

The in-repo Arnoldi step is the four-line kernel inside the restart loop of `GmresSolver::Mult` (and FGMRES's near-identical sibling). Letting `j` be the current inner index, `V` the basis array, `H` the (max_dim+1)×max_dim Hessenberg buffer, and `Hj := &H[j*(max_dim+1)]` the j-th Hessenberg column:

    // [palace/linalg/iterative.cpp:621-628]
    ApplyBA(opA, opB, pc_side, V[j], w, r);              // w ← (BA or AB or A) · V[j]
    OrthogonalizeIteration(gs_orthog, comm, V, w, Hj, j);// w ← w − Σ Hj[i]·V[i];  Hj[0..j] ← ⟨w_orig, V[i]⟩
    Hj[j+1] = linalg::Norml2(comm, w);                   // subdiagonal entry (post-orthog norm); MPI allreduce inside
    w *= 1.0 / Hj[j+1];                                  // normalise; w aliases V[j+1]

The four lines correspond to four [rotations](../concepts/rotation.md):

1. **operator apply** via the constructed operator `BA` (or `AB`, or `A`) — [apply_BA](./gmres/apply_BA.md);
2. **orthogonalisation** against the prior basis — [orthog](./orthog.md), variant-dispatched on `gs_orthog`;
3. **subdiagonal-norm** computation — [nrm2](../concepts/nrm2.md) with MPI allreduce;
4. **in-place scaling** of the new basis column — [scal](../concepts/scal.md).

The FGMRES variant ([palace/linalg/iterative.cpp:735-825](../../../reference/palace/linalg/iterative.cpp#L735-L825)) replaces the scratch `r` with the per-step preconditioned basis column `Z[j]`, which is itself promoted to threaded state and consumed during solution reconstruction; otherwise the Arnoldi-step contract is unchanged.

Three distinct in-place writes occur concurrently in the kernel: (1) `w` (aliased to `V[j+1]`) is written by `ApplyBA`, mutated by `OrthogonalizeIteration` (project-and-subtract), and finally scaled in place; (2) `Hj` is an accumulator-style write into the j-th Hessenberg column; (3) `r` is a scratch buffer used only when a preconditioner is present.

### Variant axes

The step admits three orthogonal axes of variation at L0:

- **Operator-apply variant** (`pc_side ∈ {LEFT, RIGHT, NONE}`): absorbed by the constructed operator `BA` per [constructed-operators](../concepts/constructed-operators.md). The kernel calls `ApplyBA(...)` uniformly; `pc_side` does not appear in the per-step procedure.
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
- **Arnoldi relation.** Letting `T` denote the constructed operator (`BA`, `AB`, or `A` per [apply_BA](./gmres/apply_BA.md)),

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

The procedure mentions the variant tag `gs_orthog` exactly once, at the orthogonalisation call site (level (b) of [variant-absorption](../concepts/variant-absorption.md)). The operator-apply variant is fully absorbed by the constructed-operator surface and does not appear here. The post-Arnoldi Hessenberg-column triangularisation (replay-and-generate Givens rotations on `H[:,j]`) is **not** part of the Arnoldi step; it is the small-dense incremental-least-squares update consumed by [gmres](./gmres.md) at L2, tracked under [incremental-least-squares](../concepts/incremental-least-squares.md).

### Residual variant axis

`gs_orthog` is preserved as a first-class residual axis (see [variant-absorption](../concepts/variant-absorption.md)). All three variants share the L1 contract above; they differ in MPI-collective shape and in stability under finite arithmetic. The variant is bound at solve setup and is not re-inspected per step.

## Open questions

- The post-Arnoldi small-dense Givens-QR triangularisation has been recorded across prior cycles as a distinct sequential obstruction. Currently this slice excludes it (it belongs to the GMRES outer loop's incremental-least-squares concept). Should it instead be folded in here as a logical third phase? Current call: keep separate — the Arnoldi step is the field-side / boundary kernel; the small-dense update is consumed elsewhere.
- The eigensolver path (SLEPc Krylov-Schur, ARPACK) provides an external Arnoldi implementation reached via a constructed-operator binding at configure time. Scoped out of this slice; tracked under [eigensolver](./eigensolver.md).
- No unit test exercises `OrthogonalizeIteration` or the Arnoldi step in isolation; integration is via end-to-end examples only. Flagged as a tooling gap (low priority).
