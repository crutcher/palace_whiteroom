---
kind: feature-surface
feature: inductance
level: L0
status: seed
l0_ground_truth:
  - palace/drivers/magnetostaticsolver.cpp:110-152 (MagnetostaticSolver::PostprocessTerminals — the inductance reduction)
  - palace/drivers/magnetostaticsolver.cpp:105 (the PostprocessTerminals call)
lifts_to:
  - book/src/feature/inductance.L1.md (the L1 pure-function composition root)
---

# inductance — L0 ground-truth surface (output product)

The **Maxwell inductance matrix** output product at L0: the cited Palace source that realizes the reduction, with the per-stage source ranges that the L1 / L4 inductance feature chapters lift. This is the ground-truth surface — every claim is a `(file:start-end)` citation into `palace/drivers/magnetostaticsolver.cpp`. The output product is the **post-processing** half of the magnetostatic driver; the solve that produces its input solution family is the [`magnetostatic.L0`](./magnetostatic.L0.md) driver surface.

The reduction is `MagnetostaticSolver::PostprocessTerminals(PostOperator<ProblemType::MAGNETOSTATIC> &post_op, const SurfaceCurrentOperator &surf_j_op, const std::vector<Vector> &A, const std::vector<double> &I_inc) const` (`palace/drivers/magnetostaticsolver.cpp:110-113`), called from the `Solve` body after the source sweep at `:105` (`PostprocessTerminals(post_op, curlcurl_op.GetSurfaceCurrentOp(), A, I_inc)`). It consumes the solution family `A` (the per-source vector potentials `[Aᵢ]`) and the excitation currents `I_inc` (the per-source `Iᵢ`), and writes the Maxwell inductance matrix.

## The reduction, in source

The body computes the symmetric inductance matrix `M` via the COMSOL magnetic-energy formulation, normalized by the excitation currents. The source stages, in order:

1. **The COMSOL energy formulation.** The leading comment (`:115-121`) cites p. 97 of the COMSOL AC/DC Module manual: `Mᵢᵢ = 2Uₘ(Aᵢ)/Iᵢ²` is the magnetic field energy per excitation current; the energy formulation is chosen over the direct flux integral `Φᵢ = ∫ B·nⱼ dS, Mᵢⱼ = Φᵢ/Iⱼ` because it avoids locally integrating `B = ∇×A`. This is the source-level statement that the reduction is an **operator-weighted energy form**, not a flux integral.

2. **Allocate the matrices.** `mfem::DenseMatrix M(A.size()), Mm(A.size())` (`:122`) allocates the `n_source × n_source` inductance matrix `M` (and the mutual-inductance variant `Mm`, sized from the solution-family count `A.size()`). This is the L0 home of the output product.

3. **Diagonal — the current-normalized self-energy.** Inside the `i`-loop (`:123`): `auto &A_gf = post_op.GetAGridFunction().Real()` + `auto &H_gf = post_op.GetDomainPostOp().H` (`:126-127`) grab the workspace grid functions; `A_gf.SetFromTrueDofs(A[i])` (`:128`) loads `Aᵢ`; `post_op.GetDomainPostOp().M_mag->Mult(A_gf, H_gf)` (`:129`) applies the magnetic-energy operator `K = M_mag` (`H_gf = K·Aᵢ`); `M(i, i) = Mm(i, i) = linalg::Dot<Vector>(post_op.GetComm(), A_gf, H_gf) / (I_inc[i] * I_inc[i])` (`:130-131`) forms the diagonal `Mᵢᵢ = (Aᵢᵀ K Aᵢ)/Iᵢ²`. This is the L0 site the diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (squared, current-normalized) lifts.

4. **Off-diagonal — the current-normalized cross-energy.** The inner `j`-loop (`:135`, `for (int j = i + 1; ...)`): `A_gf.SetFromTrueDofs(A[j])` (`:137`) loads `Aⱼ` (`H_gf` still holds `K·Aᵢ` from the diagonal apply); `M(i, j) = linalg::Dot<Vector>(post_op.GetComm(), A_gf, H_gf) / (I_inc[i] * I_inc[j])` (`:138`) forms the off-diagonal `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` — the operator-weighted cross-pairing normalized by the current product; the mutual-inductance bookkeeping `Mm(i, j) = -M(i, j); Mm(i, i) -= Mm(i, j)` (`:139-140`) builds the `Mm` variant. This is the L0 site the off-diagonal [`bilinear-form`](../L1/bilinear-form.md) lifts. The whole diagonal+off-diagonal energy-form computation spans `:129-138`.

5. **Symmetric mirror.** The lower-triangle copy loop `for (int j = 0; j < i; j++) { M(i, j) = M(j, i); Mm(i, j) = Mm(j, i); ... }` (`:143-149`) mirrors the already-computed upper triangle — `M` is symmetric by construction (the L4 `symmetric_from_upper`).

6. **The inverse tail → the alternate Maxwell form.** `mfem::DenseMatrix Minv(M); Minv.Invert()` (`:151-152`) computes `Minv = M⁻¹` in-place via LAPACK (the comment notes it is cheap). This is a downstream consumer of the produced `M`, not part of the reduction.

## Inputs / outputs (the feature surface, in source)

- **Input.** The solution family `const std::vector<Vector> &A` (the per-source vector potentials `[Aᵢ]`) and the excitation currents `const std::vector<double> &I_inc` (`magnetostaticsolver.cpp:112-113`), both arguments to `PostprocessTerminals`, produced by the `Solve` sweep and passed at the call site (`:105`). The energy operator `K = M_mag` is reached via `post_op.GetDomainPostOp().M_mag` (`:129`). The excitation currents `I_inc` are the inductance-specific normalization.
- **Output — the physical product.** The Maxwell inductance matrix `mfem::DenseMatrix M` (`:122`) and its inverse `Minv` (`:151-152`) — what the user ran the magnetostatic solver to compute. Only the root rank writes them to disk (`:155-158`, the `if (!root) return` guard, every process holding the full matrices).

## Lifts to

This L0 surface lifts to the L1 pure-function output-product composition root [`inductance.L1`](./inductance.L1.md) (each in-place energy-form write → a value-returning bilinear evaluation) and the L4 combinator composition root [`inductance.L4`](./inductance.L4.md) (the upper-triangle double loop → the [`gram_reduce`](../L4/gram_reduce.md) symmetric-Gram reduction with the current-normalized weight `w = 1/(IᵢIⱼ)`). The per-operator L1>L0 mutation-rotation themes of [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) / [`bilinear-form`](../L1/bilinear-form.md) carry the per-write lifts; this feature surface records the output-product *site map* (which source range realizes which reduction stage).

## Status

`seed` — the L0 ground-truth surface for the inductance output product, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), the sibling of the [capacitance.L0](./capacitance.L0.md) output-product surface. Every stage is a cited range into `palace/drivers/magnetostaticsolver.cpp`, confirmed on-disk via palace-codemap `search_text` + `read_range` this dispatch (call `:105`, def `:110`, `M(A.size())` `:122`, diagonal apply `:129` / Dot `:131`, off-diagonal Dot `:138`, inverse `:151-152`). The chapter's evidence IS the driver-source range + the per-stage site map to the constituent ops (the adapted surface-or-evidence form for the feature-surface kind).
