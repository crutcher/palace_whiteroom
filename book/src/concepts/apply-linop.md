# concept: apply_linop

`apply_linop(L, x, y) → y` evaluates the action of a linear operator `L` on a vector `x`, writing the result into `y`. It is the single primitive through which all operator actions enter an iterative solver's primitive sequence — including the system operator `A`, the preconditioner `M`, and any composite operator (e.g., `B·A` in left-preconditioned GMRES).

## Role in the L2 vocabulary

At L2, operator actions are not unfolded into per-element loops; they are treated as opaque primitives because (a) the operator may be matrix-free, (b) the operator may be a sparse matvec, a multigrid V-cycle, an FFT-based solve, or any composition thereof, and (c) the iterative solver's correctness argument depends only on `apply_linop`'s linearity, not its internal structure.

This is the natural primitive at which to count operator applications — the "matvec count" / "preconditioner-apply count" used to characterise iterative-solver convergence. Each `apply_linop` call is one such application.

## Constructed operators

When variant axes are absorbed via constructed operators (see [concept: constructed-operators](./constructed-operators.md)), the constructed operator presents the same `apply_linop` interface as a primitive operator. The fact that `apply_linop(BA, v, w)` may internally invoke two operator applications (`apply_linop(M, v, z); apply_linop(A, z, w)`) is an unfolding choice, not a change of primitive.

## Relation to matvec

The special case where `L` is a concrete sparse matrix and `apply_linop(L, x, y)` is a `y ← L·x` SpMV is one realisation. The L2 vocabulary uses `apply_linop` rather than `matvec` because matrix-free operators (FE-assembly-free, Jacobian-action, multigrid cycles) are first-class and should not be linguistically demoted.

## Citations

- Palace `Operator::Mult(x, y)` and `ComplexOperator::Mult(x, y)` are the in-tree realisations of this primitive.
- The `OperType` template parameter on `GmresSolver` and `IterativeSolver` (`palace/linalg/iterative.hpp:152–217`) parametrises which `apply_linop` variant is instantiated.
