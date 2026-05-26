# two_operator_split

The convention by which a preconditioned Krylov solver in Palace iterates against one operator `op` (typically a matrix-free, exact, possibly complex operator) while constructing its preconditioner against a *different* operator `pc_op` (typically a real-valued, coarsened, or assembled approximation).

## Background

Standard preconditioned Krylov theory (Saad 2003 §10.2) admits any operator `M` whose action `M⁻¹` is cheap to apply and which approximates `A⁻¹` well enough to cluster the spectrum of `M⁻¹ A`. There is no requirement that `M` be derived *from* `A`. In matrix-free settings — where `A` is too expensive or structurally awkward to assemble — it is standard practice to construct `M` from a separate, simpler operator `A_pc` (real-valued approximation of a complex `A`, coarse-grid approximation, or a piece of `A` such as its symmetric part).

Palace's `BaseKspSolver::SetOperators(op, pc_op)` makes this split a type-level convention: the two operators are passed separately, the Krylov iteration binds to `op`, and the preconditioner binds to `pc_op`.

## Concrete uses in Palace

- **Complex K with real preconditioner.** In `SpaceOperator`, `op` is the matrix-free complex `K = a₀M + a₁C + a₂Σ_PEC`; `pc_op` is the real assembled approximation `Br + Bi`. The preconditioner runs entirely in real arithmetic via [`complex_from_real_lift`](./complex_from_real_lift.md).
- **Eigensolver shift.** `ModeEigensolver` ships an `op = K − σM` (shifted) for the Krylov iteration and `pc_op = K − σ_pc M` (different shift for the preconditioner build).

## Correctness contract

The iteration's stopping test depends only on `r = b − op · x`. Convergence *rate* depends on the spectral relationship between `op` and `pc · pc_op`; convergence *correctness* (the returned `x` actually satisfies `op x ≈ b`) is independent of whether `pc_op = op`.

## Structural adapter

`SetOperators` contains one piece of intelligence: if `pc_op` is a `BaseMultigridOperator` but the configured `pc` is not a `GeometricMultigridSolver`, `pc_op` is unwrapped to its finest level before being passed to `pc->SetOperator`. This handles the case where the model layer ships a multigrid-shaped `pc_op` to a single-level preconditioner.

## Used by

- [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) (introducing slice).
- Future slices on `SpaceOperator` assembly and on the eigensolver.

## See also

- [`constructed-operators`](./constructed-operators.md) — the methodology pattern for absorbing variants behind a uniform operator interface.
- [`solver_as_operator`](./solver_as_operator.md) — the type-level statement that makes the split syntactically uniform (both `op` and `pc_op` have type `OperType`, both `pc` and `op` have `Mult`).
