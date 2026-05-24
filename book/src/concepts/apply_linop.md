# apply_linop

Base primitive: `y ← L · x` for an abstract linear operator `L` and vectors `x`, `y`. The interface is operator-shaped, not matrix-shaped: `L` may be a sparse matrix, a matrix-free operator (e.g., FE assembly closure), a composition of operators (`L = A · B`), or a preconditioner. The caller never inspects `L`'s representation.

## Contract

- Pure with respect to its operands: `apply_linop(L, x)` produces `y` without mutating `L` or `x` (in-place output is acceptable as a workspace convention).
- Shape: `L : V_in → V_out`; `x ∈ V_in`, `y ∈ V_out`. The two spaces may differ (rectangular operators).
- Linearity is implicit in the name. Nonlinear actions go through a different primitive.

## Role in the L2 vocabulary

At L2, operator actions are not unfolded into per-element loops; they are treated as opaque primitives because:

- The operator may be matrix-free (FE-assembly-free, Jacobian-action).
- The operator may be a sparse matvec, a multigrid V-cycle, an FFT-based solve, or any composition thereof.
- The iterative solver's correctness argument depends only on `apply_linop`'s linearity, not its internal structure.

This is the natural primitive at which to count operator applications — the "matvec count" / "preconditioner-apply count" used to characterise iterative-solver convergence. Each `apply_linop` call is one such application.

## Role in higher-layer rotations

`apply_linop` is the unit of operator-cost accounting: at L2 and above, an algorithm's per-step cost is typically dominated by the number of `apply_linop` calls. GMRES's inner step uses 1–2 `apply_linop` calls (one for `A`, optionally one for `M`). CG uses one `A` and one `M` per step.

## Constructed operators

When a slice's L1 names a *constructed operator* (e.g., `apply_BA` in GMRES, see [concept: constructed-operators](./constructed-operators.md)), that operator's L2 unfolding is typically a small chain of `apply_linop` calls — the constructed operator hides the chain at L1 while preserving it as the L2 primitive sequence. The fact that `apply_linop(BA, v, w)` may internally invoke two operator applications (`apply_linop(M, v, z); apply_linop(A, z, w)`) is an unfolding choice, not a change of primitive.

## Relation to matvec

The special case where `L` is a concrete sparse matrix and `apply_linop(L, x, y)` is a `y ← L·x` SpMV is one realisation. The L2 vocabulary uses `apply_linop` rather than `matvec` because matrix-free operators (FE-assembly-free, Jacobian-action, multigrid cycles) are first-class and should not be linguistically demoted.

## Palace mapping

- `mfem::Operator::Mult` and its complex analogue.
- `palace::ComplexOperator::Mult`.
- Palace `Operator::Mult(x, y)` and `ComplexOperator::Mult(x, y)` are the in-tree realisations of this primitive.
- The `OperType` template parameter on `GmresSolver` and `IterativeSolver` (`palace/linalg/iterative.hpp:152–217`) parametrises which `apply_linop` variant is instantiated.
- Any class implementing the operator-action interface (preconditioners, FE assembly closures, sum/product operators).
