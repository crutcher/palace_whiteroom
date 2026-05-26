# Concepts — Shared Library

A look-aside library of **shared primitives and abstract concepts** referenced across multiple slices. Examples of what lives here:

- Primitive tensor operators: `axpy`, `dot`, `matvec`, `outer`, `reduce`, `conv`, `unfold`, etc.
- Abstract mathematical concepts: Krylov subspace, condition number, iteration matrix, convergence rate, residual, preconditioner.
- Composite building blocks reused across solvers: Krylov-basis extension, Gram–Schmidt, Lanczos tridiagonalization.

## Why this exists

This is **both a DRY mechanism and the unification artifact** of the layered methodology:

- DRY: defining `axpy` once and referencing it from every slice that uses it means corrections propagate.
- Unification signal: when two slices' L2/L3 forms reach for the same primitive, *putting it here is what "they unify" means* concretely. Growth of this library tracks the unification depth of the spec.

## Lifecycle

Concepts are extracted **on demand**, not enumerated up front:

1. While drafting a slice's L1/L2/L3, when a primitive or concept is reached for that "feels canonical," check this index.
2. If present, link to the existing entry from the slice.
3. If not present, create a new `concepts/<name>.md` and add it to the index.
4. If a concept already here turns out to have multiple inconsistent uses across slices, that's a **push-back signal** — the concept's definition needs revision, or the slices need to converge.

## Concept file format

```markdown
# `<name>`

## Context
(optional — short orientation: what this is, where it shows up, when to reach for it)

**Signature.** `<haskell-style type or pseudo-signature>`

**Shape contract.** `<bunsen-DimExpr-style shape annotation>`

**Definition.** Prose + equations defining the operation or concept.

**Algebraic laws.** Commutativity, associativity, distributivity, etc., where applicable.

**Used by.**
- [slice X](../spec/slices/X.md)
- [slice Y](../spec/slices/Y.md)

## Working Notes
(optional — todos, ambiguities, open questions tied to this concept)
```

The `Context` and `Working Notes` sections are general agent-facing affordances available on any spec content; see `CLAUDE.md` *Pinned conventions* for the convention.

## Index

Auto-maintained by the orchestrator: every `concept_writes mode=create` adds a row here (analogous to the `SUMMARY.md` auto-register added in meta-7). `Used by` was removed in meta-15 as too expensive to keep accurate — `dependency-map.md` gives the layered cross-reference view, and `grep -l "concepts/<name>.md" book/src/spec/slices/*.md` answers the "where is this used" question reliably.

**Kind values**:
- `methodology` — concepts about the dissection process itself (rotation, variant-absorption, …).
- `algorithm` — top-level algorithmic patterns (gmres, chebyshev-iteration, orthogonalization, …).
- `primitive` — base tensor/linear-algebra operations (axpy, dot, apply_linop, …).
- `layer-pattern` — concepts naming how L1/L2/L3/L4 work (state-stratification, solve-monad, tensor-field-lift, …).
- `auxiliary` — supporting concepts that don't fit the other categories.

| Concept | Kind |
|---------|------|
| [apply_linop](./apply_linop.md) | primitive |
| [axpy](./axpy.md) | primitive |
| [chebyshev-iteration](./chebyshev-iteration.md) | algorithm |
| [complex_from_real_lift](./complex_from_real_lift.md) | primitive |
| [constructed-operators](./constructed-operators.md) | methodology |
| [convergence-test](./convergence-test.md) | auxiliary |
| [derived-view-hoisting](./derived-view-hoisting.md) | layer-pattern |
| [dot](./dot.md) | primitive |
| [elementwise-product](./elementwise-product.md) | primitive |
| [gemv_basis](./gemv_basis.md) | primitive |
| [givens](./givens.md) | primitive |
| [gmres](./gmres.md) | algorithm |
| [incremental-least-squares](./incremental-least-squares.md) | algorithm |
| [ksp_solve](./ksp_solve.md) | layer-pattern |
| [negative-result-slice](./negative-result-slice.md) | methodology |
| [nrm2](./nrm2.md) | primitive |
| [orthogonalization](./orthogonalization.md) | algorithm |
| [rotation](./rotation.md) | methodology |
| [scal](./scal.md) | primitive |
| [sequential-obstruction](./sequential-obstruction.md) | layer-pattern |
| [set_subvector_zero](./set_subvector_zero.md) | primitive |
| [solve-monad](./solve-monad.md) | layer-pattern |
| [solver_as_operator](./solver_as_operator.md) | primitive |
| [state-stratification](./state-stratification.md) | layer-pattern |
| [tensor-field-lift](./tensor-field-lift.md) | layer-pattern |
| [trsv](./trsv.md) | primitive |
| [two_operator_split](./two_operator_split.md) | methodology |
| [variant-absorption](./variant-absorption.md) | methodology |
