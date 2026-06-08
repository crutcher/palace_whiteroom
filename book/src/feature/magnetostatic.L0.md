---
kind: feature-surface
feature: magnetostatic
level: L0
feature_root: seed
rank: firm
edges:
  depends-on:
    - target: palace/drivers/magnetostaticsolver.cpp:22-108
      kind: cites-evidence
    - target: palace/drivers/magnetostaticsolver.cpp:110-204
      kind: cites-evidence
    - target: palace/drivers/magnetostaticsolver.hpp:24-39
      kind: cites-evidence
  reference:
    - feature/magnetostatic.L1
---

# magnetostatic — L0 ground-truth surface

The **magnetostatic simulation feature** at L0: the cited Palace driver source that realizes the composition root, with the per-stage source ranges that the L1 / L4 feature chapters lift. This is the ground-truth surface — every claim is a `(file:start-end)` citation into `palace/drivers/magnetostaticsolver.cpp`.

The driver is `MagnetostaticSolver::Solve(const std::vector<std::unique_ptr<Mesh>> &mesh) const`, returning `std::pair<ErrorIndicator, long long int>` (`palace/drivers/magnetostaticsolver.cpp:21-22`; declared `palace/drivers/magnetostaticsolver.hpp:33-34`). The class is `MagnetostaticSolver : public BaseSolver` with a private `PostprocessTerminals(...)` and the private `Solve(...) const override` (`magnetostaticsolver.hpp:24-39`).

## The composition, in source

The driver is a fixed-operator solve: assemble the curl-curl stiffness `K` once, sweep the surface-current-source family with the operator captured once, reduce to the inductance matrix. The source stages, in order:

1. **Assemble `K` once.** `CurlCurlOperator curlcurl_op(iodata, mesh)` (`:28`) constructs the operator builder from config (`iodata`) + mesh; `auto K = curlcurl_op.GetStiffnessMatrix()` (`:29`) assembles the curl-curl stiffness operator `K` ONCE; `const auto &Curl = curlcurl_op.GetCurlMatrix()` (`:30`) grabs the curl operator for the field post-process (`B = ∇×A`). This is the L0 site the L1/L4 [`fe_assemble`](../L1/fe_assemble.md) lift.

2. **Build the solver, capture the operator once — OUTSIDE the loop.** `KspSolver ksp(iodata, curlcurl_op.GetNDSpaces(), &curlcurl_op.GetH1Spaces())` (`:34`) builds the Krylov solver from config + the Nédélec H(curl) spaces (with the H1 spaces for the auxiliary-space preconditioner); `ksp.SetOperators(*K, *K)` (`:35`) captures `K` as both system and preconditioner operator. Both are *before* the source loop — this placement is the fixed-operator-capture that the L4 [`solve_family`](../L4/solve_family.md) operator-capture-once hoist makes structural.

3. **Set up the surface-current-source family.** `PostOperator<ProblemType::MAGNETOSTATIC> post_op(iodata, curlcurl_op)` (`:39`); `int n_step = static_cast<int>(curlcurl_op.GetSurfaceCurrentOp().Size())` (`:40`) — the surface-current-boundary count; `MFEM_VERIFY(n_step > 0, "No surface current boundaries specified for magnetostatic simulation!")` (`:41-42`) — the empty-family exclusion; `Vector RHS(Curl.Width()), B(Curl.Height())` (`:46`) — the RHS + B-field scratch; `std::vector<Vector> A(n_step)` (`:47`) — the solution family storage, pre-sized; `std::vector<double> I_inc(n_step)` (`:48`) — the per-source excitation-current storage (the inductance-matrix normalization).

4. **Per-source map (the fixed-operator sweep).** `for (const auto &[idx, data] : curlcurl_op.GetSurfaceCurrentOp())` (`:66`) iterates the surface-current-boundary index family. Per index: `A[step].SetSize(...)`/`A[step] = 0.0` (`:73-75`) zeros the family slot; `curlcurl_op.GetExcitationVector(idx, RHS)` (`:76`) forms the per-source RHS (prescribed current on surface `idx`); `ksp.Mult(RHS, A[step])` (`:77`) solves the fixed system into the family slot `A[step]`; the field post-process `Curl.Mult(A[step], B)` (`:85`) computes `B = ∇×A`; `I_inc[step] = data.GetExcitationCurrent()` (`:88`) records the excitation current; `step++` (`:99`) advances the family index. This loop is the L0 site the L4 [`solve_family`](../L4/solve_family.md) map (and per-element L1/L4 [`ksp_solve`](../L1/ksp_solve.md)) lift.

5. **Inductance-matrix reduction → the physical product.** After the loop, `PostprocessTerminals(post_op, curlcurl_op.GetSurfaceCurrentOp(), A, I_inc)` (`:108`, def `:110`) computes the Maxwell inductance matrix from the solution family. Inside (`:110-204`): `mfem::DenseMatrix M(A.size()), Mm(A.size())` (`:122`); the diagonal `Mᵢᵢ = (Aᵢᵀ K Aᵢ)/Iᵢ²` via `post_op.GetDomainPostOp().M_mag->Mult(A_gf, H_gf)` then `linalg::Dot<Vector>(post_op.GetComm(), A_gf, H_gf) / (I_inc[i]*I_inc[i])` (`:129-131`); the off-diagonal `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` via the same energy-form `Mult`/`Dot` pairing with the `j` grid function, then `/ (I_inc[i]*I_inc[j])` (`:135-138`); the LAPACK inverse `mfem::DenseMatrix Minv(M); Minv.Invert()` (`:151-152`) for the alternate Maxwell form. The energy formulation (`Mᵢᵢ = 2Uₘ(Aᵢ)/Iᵢ²`) follows the COMSOL AC/DC Module manual p. 97 (cited inline in the source comment, `:115-121`). This is the L0 site the diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + off-diagonal [`bilinear-form`](../L1/bilinear-form.md) lift.

The driver returns `{indicator, curlcurl_op.GlobalTrueVSize()}` (`:108`) — the error indicator + the global true-dof count.

## Inputs / outputs (the feature surface, in source)

- **Input — config.** `iodata` (the `IoData` config surface) + `mesh`, consumed by `CurlCurlOperator curlcurl_op(iodata, mesh)` (`:28`) and `KspSolver ksp(iodata, ...)` (`:34`). The surface-current-source set is `curlcurl_op.GetSurfaceCurrentOp()` (`:40`, `:66`, `:108`); the excitation currents are `data.GetExcitationCurrent()` (`:88`).
- **Output — the physical product.** The Maxwell inductance matrix `mfem::DenseMatrix M` (and inverse `Minv`) written by `PostprocessTerminals` (`:122`, `:151-152`), plus the per-source fields `A[step]` / `B` measured by `post_op.MeasureAndPrintAll(step, A[step], B, idx)` (`:91`).

## Lifts to

This L0 surface lifts to the L1 pure-function composition root [`magnetostatic.L1`](./magnetostatic.L1.md) (each in-place driver write → a value-returning pure operator) and the L4 combinator composition root [`magnetostatic.L4`](./magnetostatic.L4.md) (the per-source loop → the [`solve_family`](../L4/solve_family.md) map; the assemble → the [`fe_assemble`](../L4/fe_assemble.md) fold). The per-operator L1>L0 mutation-rotation themes of the constituent ops carry the per-write lifts; this feature surface records the composition-root *site map* (which driver range realizes which composed stage).
