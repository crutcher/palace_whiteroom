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

| Concept | Kind | Used by |
|---------|------|---------|
| _(none yet)_ | — | — |
