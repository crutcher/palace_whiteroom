# solver_as_operator

The type-level statement that an *approximate inverse* IS-A *operator*: in Palace, `Solver<OperType>` derives from `OperType`, so any preconditioner can be passed wherever a forward operator is expected and applied via the same `Mult(x, y)` interface as the operator it inverts.

## Background

In textbook preconditioned Krylov methods (Saad 2003, ch. 9), the preconditioner `M⁻¹` is *applied* like an operator — its action on a vector is what the iteration needs, not its explicit form. Palace makes this type-explicit: `Solver<OperType>` derives from `OperType`, so a preconditioner can be:

- bound to an operator via `SetOperator(op)` (rebind affordance, distinct from forward operators which fix their action at construction),
- applied via `Mult(x, y)` (the inherited operator interface),
- composed into wrappers (`BaseProductOperator`, `SumOperator`, etc.) that expect any `OperType`.

The additional `initial_guess` flag tells the solver whether `Mult(x, y)` should treat the input `y` as a starting iterate (for stationary / Krylov-as-preconditioner cases) or as scratch.

## Signature

```
class Solver<OperType> : public OperType {
    void SetOperator(const OperType& op);
    void Mult(const VecType& x, VecType& y) const;  // y ← op⁻¹ · x (approximately)
    bool initial_guess;
};
```

Citation: [palace/linalg/solver.hpp:20-64](../../../reference/palace/linalg/solver.hpp#L20-L64).

## Why this matters

The consequence is that Krylov iteration code (`IterativeSolver`) holds a `Solver<OperType>* B` rather than a typed family of preconditioner-specific pointers. Variant absorption for the preconditioner-type axis (`AMS | BoomerAMG | sparse-direct | Jacobi | GMG`) is achieved at this type, not at every call site. See [`variant-absorption`](./variant-absorption.md) and [`apply_linop`](./apply_linop.md) — `ApplyB` in the iterative solver is `apply_linop` specialised to `Solver<OperType>` with a timer wrapper and a not-null guard.

## Used by

- [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md): the framework's central type abstraction.
- [`cg`](../spec/slices/cg.md), [`gmres`](../spec/slices/gmres.md), [`fgmres`](../spec/slices/gmres.md#fgmres): each iteration consumes the preconditioner via `Solver<OperType>::Mult`.
