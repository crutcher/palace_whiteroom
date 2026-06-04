---
kind: feature-surface
feature: electrostatic
level: L0
feature_root: seed
rank: firm
edges:
  depends-on:
    - target: palace/drivers/electrostaticsolver.cpp:21-98
      kind: cites-evidence
    - target: palace/drivers/electrostaticsolver.cpp:100-160
      kind: cites-evidence
    - target: palace/drivers/electrostaticsolver.hpp:34-44
      kind: cites-evidence
  reference:
    - feature/electrostatic.L1
---

# electrostatic — L0 ground-truth surface

The **electrostatic simulation feature** at L0: the cited Palace driver source that realizes the composition root, with the per-stage source ranges that the L1 / L4 feature chapters lift. This is the ground-truth surface — every claim is a `(file:start-end)` citation into `palace/drivers/electrostaticsolver.cpp`.

The driver is `ElectrostaticSolver::Solve(const std::vector<std::unique_ptr<Mesh>> &mesh) const`, returning `std::pair<ErrorIndicator, long long int>` (`palace/drivers/electrostaticsolver.cpp:20-21`; declared `palace/drivers/electrostaticsolver.hpp:39-41`). The class is `ElectrostaticSolver : public BaseSolver` with a private `PostprocessTerminals(...)` and the private `Solve(...) const override` (`electrostaticsolver.hpp:34-44`).

## The composition, in source

The driver is a fixed-operator solve: assemble `K` once, sweep the terminal-source family with the operator captured once, reduce to the capacitance matrix. The source stages, in order:

1. **Assemble `K` once.** `LaplaceOperator laplace_op(iodata, mesh)` (`:28`) constructs the operator builder from config (`iodata`) + mesh; `auto K = laplace_op.GetStiffnessMatrix()` (`:30`) assembles the stiffness operator `K` ONCE; `const auto &Grad = laplace_op.GetGradMatrix()` (`:31`) grabs the gradient operator for the field post-process. This is the L0 site the L1/L4 [`fe_assemble`](../L1/fe_assemble.md) lift.

2. **Build the solver, capture the operator once — OUTSIDE the loop.** `KspSolver ksp(iodata, laplace_op.GetH1Spaces())` (`:34`) builds the Krylov solver from config + the H1 space; `ksp.SetOperators(*K, *K)` (`:36`) captures `K` as both system and preconditioner operator. Both are *before* the terminal loop — this placement is the fixed-operator-capture that the L4 [`solve_family`](../L4/solve_family.md) operator-capture-once hoist makes structural.

3. **Set up the terminal-source family.** `PostOperator<ProblemType::ELECTROSTATIC> post_op(iodata, laplace_op)` (`:38`); `int n_step = static_cast<int>(laplace_op.GetSources().size())` (`:39`) — the terminal-boundary count; `MFEM_VERIFY(n_step > 0, "No terminal boundaries specified for electrostatic simulation!")` (`:40`) — the empty-family exclusion; `std::vector<Vector> V(n_step)` (`:45`) — the solution family storage, pre-sized.

4. **Per-terminal-source map (the fixed-operator sweep).** `for (const auto &[idx, data] : laplace_op.GetSources())` (`:59`) iterates the terminal-boundary index family. Per index: `laplace_op.GetExcitationVector(idx, *K, V[step], RHS)` (`:68`) forms the per-terminal RHS (prescribed nonzero voltage on terminal `idx`); `ksp.Mult(RHS, V[step])` (`:69`) solves the fixed system into the family slot `V[step]`; the field post-process `E = 0.0; Grad.AddMult(V[step], E, -1.0)` (`:75-76`) computes `E = -∇V`; `step++` (`:89`) advances the family index. This loop is the L0 site the L4 [`solve_family`](../L4/solve_family.md) map (and per-element L1/L4 [`ksp_solve`](../L1/ksp_solve.md)) lift.

5. **Capacitance-matrix reduction → the physical product.** After the loop, `PostprocessTerminals(post_op, laplace_op.GetSources(), V)` (`:95`, def `:100`) computes the Maxwell capacitance matrix from the solution family. Inside (`:100-138`): `mfem::DenseMatrix C(V.size()), Cm(V.size())` (`:111`); the diagonal `Cᵢᵢ = Vᵢᵀ K Vᵢ` via `post_op.GetDomainPostOp().M_elec->Mult(V_gf, D_gf)` then `linalg::Dot<Vector>(post_op.GetComm(), V_gf, D_gf)` (`:118-119`); the off-diagonal `Cᵢⱼ = Vⱼᵀ K Vᵢ` via the same energy-form `Mult`/`Dot` pairing (`:122-127`); the LAPACK inverse `mfem::DenseMatrix Cinv(C); Cinv.Invert()` (`:139-140`) for the alternate Maxwell form. The energy formulation (`Cᵢᵢ = 2Uₑ(Vᵢ)/Vᵢ²`) follows the COMSOL AC/DC Module manual p. 97 (cited inline in the source comment, `:105-110`). This is the L0 site the diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + off-diagonal [`bilinear-form`](../L1/bilinear-form.md) lift.

The driver returns `{indicator, laplace_op.GlobalTrueVSize()}` (`:97`) — the error indicator + the global true-dof count.

## Inputs / outputs (the feature surface, in source)

- **Input — config.** `iodata` (the `IoData` config surface) + `mesh`, consumed by `LaplaceOperator laplace_op(iodata, mesh)` (`:28`) and `KspSolver ksp(iodata, ...)` (`:34`). The terminal-source set is `laplace_op.GetSources()` (`:39`, `:59`, `:95`).
- **Output — the physical product.** The Maxwell capacitance matrix `mfem::DenseMatrix C` (and inverse `Cinv`) written by `PostprocessTerminals` (`:111`, `:139-140`), plus the per-terminal fields `V[step]` / `E` measured by `post_op.MeasureAndPrintAll(step, V[step], E, idx)` (`:82`).

## Lifts to

This L0 surface lifts to the L1 pure-function composition root [`electrostatic.L1`](./electrostatic.L1.md) (each in-place driver write → a value-returning pure operator) and the L4 combinator composition root [`electrostatic.L4`](./electrostatic.L4.md) (the per-terminal loop → the [`solve_family`](../L4/solve_family.md) map; the assemble → the [`fe_assemble`](../L4/fe_assemble.md) fold). The per-operator L1>L0 mutation-rotation themes of the constituent ops carry the per-write lifts; this feature surface records the composition-root *site map* (which driver range realizes which composed stage).

## Status

`firm` (promoted `seed`→`firm` at cycle-095 alongside its L1/L4 levels, the `bilinear-form-firm-flip-and-cascade-wave`) — the L0 ground-truth surface for the electrostatic feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02). Every stage is a cited range into `palace/drivers/electrostaticsolver.cpp`, confirmed on-disk via palace-codemap `read_range` this dispatch. The chapter's evidence IS the driver-source range + the per-stage site map to the constituent ops (the adapted surface-or-evidence form for the feature-surface kind); as a cited ground-truth surface its rank is firm.
