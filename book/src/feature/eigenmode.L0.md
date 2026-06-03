---
kind: feature-surface
feature: eigenmode
level: L0
status: seed
l0_ground_truth:
  - palace/drivers/eigensolver.cpp:32-477 (EigenSolver::Solve)
  - palace/drivers/eigensolver.hpp:20-28 (class declaration)
lifts_to:
  - book/src/feature/eigenmode.L1.md (the L1 pure-function composition root)
---

# eigenmode — L0 ground-truth surface

The **eigenmode simulation feature** at L0: the cited Palace driver source that realizes the composition root, with the per-stage source ranges that the L1 / L4 feature chapters lift. This is the ground-truth surface — every claim is a `(file:start-end)` citation into `palace/drivers/eigensolver.cpp`.

The driver is `EigenSolver::Solve(const std::vector<std::unique_ptr<Mesh>> &mesh) const`, returning `std::pair<ErrorIndicator, long long int>` (`palace/drivers/eigensolver.cpp:32-33`; the function body runs to the closing brace at `:477`). The class is `EigenSolver : public BaseSolver` with the private `Solve(...) const override` (`palace/drivers/eigensolver.hpp:20-28`, decl `:23-24`). The opaque eigensolver wrapper surface is catalogued in [`L0/eigensolver-wrapper`](../L0/eigensolver-wrapper.md) (the 22 virtuals on the `EigenvalueSolver` abstract base, the three `SetOperators` overloads, the per-pair result extractors).

## The composition, in source

The driver assembles the generalized-eigenproblem operator pencil `(K, C, M)` once, hands it to the opaque eigensolver once, and reads out the converged eigenpair set. Crucially — unlike the fixed-operator [magnetostatic](./magnetostatic.L0.md) / [electrostatic](./electrostatic.L0.md) drivers — there is **no per-source RHS family loop** and **no value-threaded outer solve loop**: the only outer loop is the post-processing readout over the already-converged modes. The source stages, in order:

1. **Assemble the operator pencil once.** `SpaceOperator space_op(iodata, mesh)` (`:39`) constructs the operator builder from config (`iodata`) + mesh; then the three pencil operators are assembled ONCE each: `auto K = space_op.GetStiffnessMatrix<ComplexOperator>(Operator::DIAG_ONE)` (`:40`) — the curl-curl stiffness, with `DIAG_ONE` shifting the PEC-dof Dirichlet eigenvalues out of range; `auto C = space_op.GetDampingMatrix<ComplexOperator>(Operator::DIAG_ZERO)` (`:41`) — the damping matrix, **which may be `nullptr`** (the source comment at `:35-37` notes this; a null `C` selects the linear EVP); `auto M = space_op.GetMassMatrix<ComplexOperator>(Operator::DIAG_ZERO)` (`:42`) — the mass matrix. The nonlinear `A2(ω)` branch is set up via the `funcA2` lambda (`:45-46`). This is the L0 site the L1/L4 [`fe_assemble`](../L1/fe_assemble.md) lift (three folds).

2. **Configure the eigensolver, capture the pencil once.** After the backend-selection block (ARPACK / SLEPc / quasi-Newton, `:50-171`), the pencil is captured into the opaque solver via the `SetOperators` dispatch (`:172-196`): the linear-EVP path `eigen->SetOperators(*K, *M, scale)` (`:193`), the quadratic-EVP path `eigen->SetOperators(*K, *C, *M, scale)` (`:189`), or the nonlinear SLP path (`:177-178`). Per-solve control is set: `eigen->SetNumModes(iodata.solver.eigenmode.n, ...)` (`:196`), `SetTol` (`:200`), `SetMaxIter` (`:201`). The optional M-inner-product orthogonalization (`:209-218`) and the divergence-free projector (`:220-235`, so the solve runs orthogonal to the stiffness-matrix null space) are configured. This is the L0 site the [`eigsolve`](../L1/eigsolve.md) operator-setup the L4 [`eigsolve`](../L4/eigsolve.md) cap names.

3. **One opaque eigen-solve.** `int num_conv = eigen->Solve()` (`:367`) runs the entire eigen-iteration **inside the opaque library** (SLEPc `EPSSolve` / ARPACK `naupd` RCI) and returns the converged-pair count; the converged-count + first-eigenvalue are printed (`:368-375`). There is an optional quasi-Newton refinement re-run `num_conv = eigen->Solve()` (`:405`) for the nonlinear hybrid case. This single call is the entire solve — the L0 site the L1/L4 [`eigsolve`](../L4/eigsolve.md) black-box-kernel constituent lifts. **No Palace-authored loop surrounds it** (the load-bearing fact for the `eigsolve` partial-obstruction / black-box-kernel status; the eigen-iteration is opaque-library-owned).

4. **Per-mode readout map → the physical product.** `for (int i = 0; i < num_conv; i++)` (`:424`) iterates the already-converged eigenpair set — the driver's **only** outer loop, and a pure post-processing readout (NOT a solve-iteration; explicitly contrasted at `book/src/L4/solve_family.md:146`). Per mode: `std::complex<double> omega = eigen->GetEigenvalue(i)` (`:427`) reads the eigenvalue; the error norms are read (`:428-429`); `omega` is un-transformed to the eigenfrequency by problem type — `omega = std::sqrt(omega)` for the linear EVP (`μ = -λ² = ω²`, `:430-434`) or `omega /= 1i` for the quadratic EVP (`λ = iω`, `:435-439`); `eigen->GetEigenvector(i, E)` (`:443`) writes the electric mode field into `E` (the in-place destination write the L1 form lifts); `linalg::NormalizePhase(...)` (`:445`); the magnetic field `B = -1/(iω)∇×E` is formed via `Curl.Mult(E.Real(), B.Real())` / `Curl.Mult(E.Imag(), B.Imag())` then `B *= -1.0/(1i*omega)` (`:447-449`), with an optional Floquet-BC correction (`:450-455`); `post_op.MeasureAndPrintAll(i, E, B, omega, error_abs, error_bkwd, num_conv)` (`:458`) measures + records the per-mode observables. The loop closes at `:471`; `MFEM_VERIFY(num_conv >= iodata.solver.eigenmode.n, ...)` (`:472-475`) checks enough modes converged. This is the L0 site the L1/L4 per-mode readout map lifts — feeding the eigenfrequency / Q-factor **output product** (whose reduction is owned by the `eigenfrequency-qfactor` output-product column; forward-ref, not authored here).

The driver returns `{indicator, space_op.GlobalTrueVSize()}` (`:476`) — the error indicator + the global true-dof count.

## Inputs / outputs (the feature surface, in source)

- **Input — config.** `iodata` (the `IoData` config surface) + `mesh`, consumed by `SpaceOperator space_op(iodata, mesh)` (`:39`). The requested mode count + tolerances are `iodata.solver.eigenmode.{n, tol, max_it, target, ...}` (`:197-202`); the spectral-transform and orthogonalization config drive `:209-235`.
- **Output — the physical product.** The per-mode eigenfrequency `omega`, electric field `E`, and magnetic field `B` measured by `post_op.MeasureAndPrintAll(i, E, B, omega, error_abs, error_bkwd, num_conv)` (`:458`). The eigenfrequency / Q-factor reduction into the reported product is owned by the `eigenfrequency-qfactor` output-product column (forward-ref).

## Lifts to

This L0 surface lifts to the L1 pure-function composition root [`eigenmode.L1`](./eigenmode.L1.md) (the `GetEigenvector(i, E)` destination write → a value-returning `EigResult` field; the in-place `B *= ...` accumulations → pure field-readout values) and the L4 combinator composition root [`eigenmode.L4`](./eigenmode.L4.md) (the three `Get*Matrix` assembles → the [`fe_assemble`](../L4/fe_assemble.md) fold ×3; the single `eigen->Solve()` → the [`eigsolve`](../L4/eigsolve.md) black-box-kernel cap; the readout `for` → a pure `map`). The per-operator L1>L0 mutation-rotation themes of the constituent ops carry the per-write lifts; this feature surface records the composition-root *site map* (which driver range realizes which composed stage).

## Status

`seed` — the L0 ground-truth surface for the eigenmode feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [magnetostatic.L0](./magnetostatic.L0.md) / [electrostatic.L0](./electrostatic.L0.md) exemplars. Every stage is a cited range into `palace/drivers/eigensolver.cpp`, confirmed on-disk via palace-codemap `read_range` this dispatch (the `EigenSolver::Solve` decl `:32-33`, K/C/M assembly `:40-42`, `SetOperators` pencil setup `:172-196`, the single `eigen->Solve()` `:367`, the readout loop `:424-471`). The load-bearing structural fact at L0: a single opaque `eigen->Solve()` with NO surrounding Palace-authored loop and NO per-source RHS family — the driver's only loop is the post-processing eigenpair readout (the `solve_family`/`fold_solve` non-membership recorded at `book/src/L4/solve_family.md:146`). The chapter's evidence IS the driver-source range + the per-stage site map to the constituent ops (the adapted surface-or-evidence form for the feature-surface kind).
