---
edges:
  reference:
    - L4/preconditioning-framework      # firm L4 home (structural adapter in pcBoundOp)
    - concepts/constructed-operator-factory  # the factory creating the unwrap condition
---

# finest-level-unwrap

A small structural-adapter primitive that extracts the finest-level operator from a multigrid-wrapped operator, used to reconcile a multigrid-typed `pc_op` (provided by the model layer) with a non-multigrid-typed `pc` (selected by the linear-solver config) at solver-bind time.

## L2 form

```
finest_level_unwrap(pc_op: BaseMultigridOperator) → OperType:
    return pc_op.GetFinestOperator()
```

The primitive is a no-op when `pc_op` is already a non-multigrid operator; the caller dispatches on `is_multigrid(pc_op) and not is_multigrid_solver(pc)` before invoking it.

## Why it is a named primitive

The alternative — silently letting `pc.SetOperator(pc_op)` apply the multigrid operator's top-level `Mult` (which forwards to the finest level anyway) — would work for `Mult` but breaks for any preconditioner-construction step that re-inspects the operator's structure (e.g. AMS extracting nodal/edge sub-operators, BoomerAMG building hierarchy). Palace's L0 evidence (`BaseKspSolver::SetOperators` at `palace/linalg/ksp.cpp:274-296`) makes the unwrap explicit: the wrapper detects the asymmetry at `SetOperators` time and unwraps once.

Naming it as a primitive lets downstream slices that compose preconditioners refer to the unwrap as a structural-adapter step rather than re-deriving the type-asymmetry from scratch.

## Used by

- [`preconditioning-framework`](../L4/preconditioning-framework.md) — `finestLevelUnwrap` is the structural adapter inside the `pcBoundOp` derived view, fired when a multigrid `pc_op` meets a non-multigrid `pc` (§Derived-view hoisting).

## See also

- [`constructed-operator-factory`](./constructed-operator-factory.md) — the factory whose multigrid-vs-single-level dispatch creates the conditions under which this unwrap is needed.
