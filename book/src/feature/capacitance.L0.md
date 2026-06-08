---
kind: feature-surface
feature: capacitance
level: L0
feature_root: seed
rank: firm
edges:
  depends-on:
    - target: palace/drivers/electrostaticsolver.cpp:100-140
      kind: cites-evidence
    - target: palace/drivers/electrostaticsolver.cpp:95
      kind: cites-evidence
    - target: palace/drivers/electrostaticsolver.hpp:34-44
      kind: cites-evidence
  reference:
    - feature/capacitance.L1
---

# capacitance — L0 ground-truth surface

The **Maxwell capacitance matrix** output product at L0: the cited Palace driver source that realizes the reduction composition root, with the per-stage source ranges that the L1 / L4 capacitance feature chapters lift. This is the ground-truth surface — every claim is a `(file:start-end)` citation into `palace/drivers/electrostaticsolver.cpp`.

The capacitance reduction is `ElectrostaticSolver::PostprocessTerminals(...)` (`palace/drivers/electrostaticsolver.cpp:100`; declared private in `electrostaticsolver.hpp:34-44`), called once after the terminal-source loop at `:95` with the collected solution family `V`. It is the **output-product** tail of the electrostatic driver: the driver's `Solve` (`:21-22`, body `:21-98`) assembles `K`, sweeps the terminal family, and collects `V`; `PostprocessTerminals` reduces `V` to the capacitance matrix.

## The composition, in source

The capacitance reduction is a symmetric-Gram fold over the solution family, mirrored to a symmetric matrix, then inverted. The source stages, in order:

1. **The reduction call site.** `PostprocessTerminals(post_op, laplace_op.GetSources(), V)` (`:95`) is called after the terminal-source loop with the collected solution family `V` and the terminal-source map. This is the boundary between the producing driver column (`Solve`, `:21-98`) and the output-product reduction. The driver returns `{indicator, laplace_op.GlobalTrueVSize()}` (`:97`).

2. **The capacitance matrix allocation.** Inside `PostprocessTerminals` (def `:100`), `mfem::DenseMatrix C(V.size()), Cm(V.size())` (`:111`) allocates the `n_terminal × n_terminal` capacitance matrix `C` (and the Maxwell mutual-capacitance matrix `Cm`). The energy formulation `Cᵢᵢ = 2Uₑ(Vᵢ)/Vᵢ²` follows the COMSOL AC/DC Module manual p. 97 (cited in the source comment, `:105-110`).

3. **Diagonal — the operator-weighted self-energy.** For each `i` (`:112`), the diagonal entry is `Cᵢᵢ = Vᵢᵀ K Vᵢ` via `post_op.GetDomainPostOp().M_elec->Mult(V_gf, D_gf)` (`:118`, the `K·Vᵢ` apply on the energy operator `M_elec`) then `C(i,i) = Cm(i,i) = linalg::Dot<Vector>(post_op.GetComm(), V_gf, D_gf)` (`:119`, the `Vᵢ·(K Vᵢ)` reduction). With unit-voltage excitation (`∀i, Vᵢ = 1`) the `/Vᵢ²` normalization is the identity — the `w = 1` weight. This is the L0 site the diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (and the L4 [`gram_reduce`](../L4/gram_reduce.md) diagonal entry) lift.

4. **Off-diagonal — the operator-weighted cross-pairing.** The inner loop `for (int j = i + 1; j < C.Width(); j++)` (`:123`) computes the upper-triangle off-diagonals `Cᵢⱼ = Vⱼᵀ K Vᵢ` via `V_gf.SetFromTrueDofs(V[j])` (`:125`) then `C(i,j) = linalg::Dot<Vector>(post_op.GetComm(), V_gf, D_gf)` (`:126`, the same energy-form pairing with the `j` grid function reusing the `D_gf = K·Vᵢ` apply). This is the L0 site the off-diagonal [`bilinear-form`](../L1/bilinear-form.md) (and the L4 [`gram_reduce`](../L4/gram_reduce.md) off-diagonal entry) lift.

5. **Symmetric mirror + inverse → the physical product.** The lower-triangle copy `for (int j = 0; j < i; j++) C(i,j) = C(j,i)` (`:132-134`) mirrors the upper triangle (the L4 `symmetric_from_upper`). After the loops, `mfem::DenseMatrix Cinv(C); Cinv.Invert()` (`:139-140`, in-place LAPACK) produces the alternate Maxwell form. These are the L0 sites the symmetric-Gram mirror + the `gram_inverse` consumer lift.

## Inputs / outputs (the feature surface, in source)

- **Input — config (terminal excitations).** The terminal-source map `laplace_op.GetSources()` (`:95`, passed as `terminal_sources`) + the collected solution family `V` (`:95`, passed `const`), supplied by the producing driver column. The energy operator is `post_op.GetDomainPostOp().M_elec` (`:118`).
- **Output — the physical product.** The Maxwell capacitance matrix `mfem::DenseMatrix C` (`:111`) and its inverse `Cinv` (`:139-140`), written by `PostprocessTerminals` (root-only disk write, `:143` onward).

## Lifts to

This L0 surface lifts to the L1 pure-function composition root [`capacitance.L1`](./capacitance.L1.md) (each in-place `Mult`/`Dot`/`Invert` write → a value-returning bilinear-form pure function) and the L4 combinator composition root [`capacitance.L4`](./capacitance.L4.md) (the symmetric-Gram double loop → the [`gram_reduce`](../L4/gram_reduce.md) combinator at the voltage `w = 1` specialization). The per-operator L1>L0 mutation-rotation themes of the constituent bilinear ops carry the per-write lifts; this feature surface records the output-product *site map* (which driver range realizes which reduction stage). This is the L0 ground-truth surface for the capacitance output product (the output-product **leaf feature column**).
