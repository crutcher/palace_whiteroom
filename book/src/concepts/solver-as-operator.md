---
edges:
  reference:
    - concepts/apply_linop
    - concepts/constructed-operators
    - concepts/constructed-operator-factory
    - concepts/variant-absorption
    - concepts/rotation
    - L4/preconditioning-framework
---
# solver-as-operator

A layer-pattern concept naming the type-level rotation in which an approximate inverse (a *solver*) is declared to inherit from the operator type it inverts. In Palace, `Solver<OperType>` derives from `OperType`, so any `pc : Solver<OperType>` can be substituted wherever an `OperType` is expected.

## Background

This pattern is standard in operator-algebra preconditioning frameworks (PETSc's `PCApply` is callable as a `Mat` via a `MATSHELL` adapter; deal.II's `PreconditionBase` derives from `Subscriptor` but exposes `vmult` as `Operator::vmult`; mfem's `mfem::Solver : public mfem::Operator`). Saad 2003 §9.2 motivates it: a Krylov method needs only `M⁻¹·v` as a black-box operator, so any approximation that respects the same interface composes uniformly.

The pattern is a **rotation at the type layer**: at L0 the `Solver` type is a distinct class hierarchy; at L1 it IS-A operator, so any L1 statement about operator-application primitives (matrix-vector products, V-cycles, factorisations) applies uniformly to both the true operator and its preconditioner.

## L1 statement

Given `pc : Solver<OperType>` and `op : OperType`, both expose `Mult(x, y)` and both are instances of the [`apply_linop`](./apply_linop.md) primitive at L2:

```
apply_linop(op, x)  : y ≈ op · x         // the true operator action
apply_linop(pc, r)  : z ≈ pc_op⁻¹ · r    // the approximate-inverse action
```

The two are called through the same primitive shape. The Krylov iteration body does not need to know that `pc` is an approximate inverse — it only needs that `apply_linop(pc, r)` returns a vector whose application of `pc_op` approximates `r`.

## Why this is a rotation, not a renaming

The rotation hides the algorithmic identity of the preconditioner from the iteration. A reader substituting a different preconditioner (BoomerAMG → AMS → MUMPS → JacobiSmoother → GeometricMultigridSolver-wrapping-anything) does not change the L1 procedure or the L2 primitive chain of the iteration; the substitution is absorbed by [`constructed-operator-factory`](./constructed-operator-factory.md) at solve-construction time. See [`variant-absorption`](./variant-absorption.md) and [`constructed-operators`](./constructed-operators.md).

Contrast with renaming: if `Solver<OperType>` were merely a typedef for `OperType`, the L1 statement would say nothing — it would not have hidden any state. The rotation is genuine because the L0 `Solver<OperType>` carries a distinct interface (`SetOperator`, `initial_guess`) that the L1 layer compresses away.

## Used by

- [`preconditioning-framework`](../L4/preconditioning-framework.md) — the framework that binds a constructed `Pc<E>` (itself an `Op<E>`) into `BaseKspSolver`; establishes Palace's KSP composition pattern.
- The per-method Krylov slices (`cg`, `gmres`, `fgmres`) at L2 — treat `apply_preconditioner(solver, r, z)` as `apply_linop(solver.pc, r)`.

## See also

- [`apply_linop`](./apply_linop.md) — the L2 primitive that consumes the rotation.
- [`constructed-operators`](./constructed-operators.md) — the absorption route the rotation enables.
- [`rotation`](./rotation.md) — the quality criterion this concept satisfies (state hiding: the `Solver` interface's `SetOperator`/`initial_guess` are hidden from the iteration body).
