---
edges:
  reference:
    - concepts/apply_linop
    - concepts/constructed-operators
    - concepts/variant-absorption
    - concepts/solver-as-operator
    - concepts/rotation
    - L4/preconditioning-framework
---
# constructed-operator-factory

The L2 primitive that consumes a config record (plus contextual data like FE-space hierarchies) and returns a typed operator that internalises one or more variant axes. The factory call is the **single point** at which the variant is consumed; downstream code sees a uniformly-typed operator and invokes it through [`apply_linop`](./apply_linop.md).

## Background

The pattern crystallises the *constructed-operator* route to variant absorption (see [`constructed-operators`](./constructed-operators.md) and [`variant-absorption`](./variant-absorption.md) — particularly variant-absorption level (b): the L1 procedure mentions the variant parameter at most once). In Palace it appears in two structurally identical forms:

- `ConfigureKrylovSolver(linear, verbose, comm) → unique_ptr<IterativeSolver<OperType>>` consuming the krylov-method × side × orthog × restart-dim axes.
- `ConfigurePreconditionerSolver(linear, verbose, comm, fespaces, aux_fespaces) → unique_ptr<Solver<OperType>>` consuming the preconditioner-type × multigrid-composition × scalar-field axes.

Both are factory functions that consume an enum (or set of enums) and an FE-space context, dispatch internally, and return a [`solver-as-operator`](./solver-as-operator.md)-typed handle.

## L2 signature

```
constructed_operator_factory(role: enum,
                             config: ConfigRecord,
                             variants: {axis_1: enum, axis_2: enum, ...},
                             context: {fespaces?, aux_fespaces?, ...})
  → unique_ptr<OperType-or-derived>
```

The factory is **pure with respect to the variant axes**: given the same `(role, config, variants, context)` it produces an operator with the same operational semantics. (It is impure with respect to memory allocation and MPI handles, which is L4 monadic structure, not L2 variant absorption.)

## The rotation it enables

The factory is the syntactic site where the L1 form's variant-bearing parameters disappear from downstream prose. Before the factory call, the L1 procedure mentions `linear_config.krylov_solver`, `linear_config.type`, `fespaces.num_levels`. After the factory call returns, downstream L1/L2 prose mentions only `ksp` and `pc` — the variant has been consumed.

This is the *single point* property required by variant-absorption level (b). If a slice's L1 form re-inspects the variant after the factory call, the rotation is incomplete and the absorption is structural-only (level (a)), not procedural (level (b)). See [`variant-absorption`](./variant-absorption.md).

## Used by

- [`preconditioning-framework`](../L4/preconditioning-framework.md) — `buildKspSolver`'s two `constructedOperatorFactory` calls (`KrylovRole`, `PrecondRole`) are factory instances; the variant axes absorb inside the factories (§Signature).
- Future per-method slices' L2 forms that need to refer to the krylov-builder by name.

## See also

- [`constructed-operators`](./constructed-operators.md) — the absorption pattern this primitive realises.
- [`solver-as-operator`](./solver-as-operator.md) — the type-level rotation the factory's return type relies on.
- [`rotation`](./rotation.md) — the rotation criteria satisfied: coarser substitution (the variant enum is hidden behind a uniform operator interface).
