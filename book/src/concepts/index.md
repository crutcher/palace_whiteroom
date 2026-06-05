---
kind: navigational-container (concepts library index)
# Navigational container, not a DAG node: no `rank:` (makes no resolution
# claim, not in the total order), only `reference` edges to the concept pages
# it indexes (carry no liveness, constrain no rank — scheme §4/§5; SAME
# convention WAVE-1 D5 fixed for the layer/lowering indexes). The record-
# definition concept pages it lists (config-record / dofset / krylov / op-params
# / sim-state / step-outputs / prev-carry / solve-result) ARE DAG nodes — but a
# member being a node does not make the index a node (an index references its
# members; it does not depend-on them).
edges:
  reference:
    - concepts/dependency-map
    - concepts/apply_BA
    - concepts/apply_linop
    - concepts/axpy
    - concepts/black-box-vs-accelerated-kernels
    - concepts/build-time-vs-run-time-stratification
    - concepts/capability-typing
    - concepts/chebyshev-iteration
    - concepts/complex-from-real-lift
    - concepts/config-record
    - concepts/constructed-operator-factory
    - concepts/constructed-operators
    - concepts/convergence-test
    - concepts/counter-update
    - concepts/derived-view-hoisting
    - concepts/dofset
    - concepts/dot
    - concepts/eigsolve
    - concepts/elementwise-product
    - concepts/erasure-scope
    - concepts/finest-level-unwrap
    - concepts/first-iteration-unrolling
    - concepts/gemv_basis
    - concepts/givens
    - concepts/givens_apply
    - concepts/givens_generate
    - concepts/gmres
    - concepts/incremental-least-squares
    - concepts/krylov
    - concepts/ksp_solve
    - concepts/negative-result-slice
    - concepts/nested-constructed-operator-gate
    - concepts/nrm2
    - concepts/op-params
    - concepts/orthogonalization
    - concepts/plane-rotation-stream
    - concepts/prev-carry
    - concepts/rotation
    - concepts/scal
    - concepts/scalar-promotion
    - concepts/scope-out-obstruction
    - concepts/sequential-obstruction
    - concepts/set_subvector_zero
    - concepts/sim-state
    - concepts/solve-monad
    - concepts/solve-result
    - concepts/solver-as-operator
    - concepts/state-stratification
    - concepts/step-outputs
    - concepts/tensor-field-lift
    - concepts/trsv
    - concepts/two_operator_split
    - concepts/variant-absorption
---

# Concepts — Shared Library

A look-aside library of **cross-cutting concept pages**: shared primitives, abstract concepts, layer patterns, and
record-definition pages referenced across **multiple chapters** of the layered specification (the L4→L0 Parts, the four
`L_{n+1}>L_n` lowering Parts, and the feature-surface spine under `book/src/feature/`). Examples of what lives here:

- Primitive tensor/linear-algebra operators referenced across layers: `axpy`, `dot`, `nrm2`, `scal`, `apply_linop`, `trsv`, …
- Abstract mathematical concepts: Krylov subspace, orthogonalization, convergence test, Givens rotation.
- Layer patterns naming how the rotations work: `state-stratification`, `solve-monad`, `tensor-field-lift`, `constructed-operators`, …
- Methodology concepts accumulated from cross-cycle friction: `rotation`, `variant-absorption`, `sequential-obstruction`, …
- **Record-definition pages** (the record-definition obligation, directive-2): the fields / types / meaning /
  construction-vs-run-time stratum / L0 backing home of a record named across ≥2 chapters (`krylov`, `op-params`,
  `sim-state`, `step-outputs`, `prev-carry`, `solve-result`, `config-record`).

A concept page defines the **data shape / shared vocabulary** in itself; the per-operator chapters (in the L_n Parts)
define the *behavior over it*. A concept page does NOT restate the operators' algebra — the authoritative algebra lives
in the L_n operator entry, and the concept page forwards to it.

## Why this exists

This is **both a DRY mechanism and the unification artifact** of the layered methodology:

- DRY: defining `axpy` once and referencing it from every chapter that uses it means corrections propagate.
- Unification signal: when two layered chapters' forms reach for the same primitive, *putting it here is what "they
  unify" means* concretely. Growth of this library tracks the unification depth of the spec.

## Lifecycle

Concepts are extracted **on demand** by the specialized dispatch agents (primarily `layer-intro-author` for
cross-cutting concept + record-definition pages; the `harvester` flags a signature-named record needing a home), not
enumerated up front:

1. While authoring an L_n operator entry, a lowering theme, or a feature-surface column, a primitive / pattern / record
   is reached for that "feels canonical" and is referenced across ≥2 chapters — check this index.
2. If present, link to the existing concept page from the chapter.
3. If not present, a `layer-intro-author` dispatch authors a new `concepts/<name>.md` (one page per invocation) and the
   integrator adds it to the index in alpha position. A record used by only ONE chapter stays layer-local (an in-chapter
   `## Record definition` section), below the ≥2-consumer bar.
4. If a concept already here turns out to have multiple inconsistent uses across chapters, that's a **push-back signal**
   surfaced by the `same-layer-cross-cutter` / `cross-layer-cross-cutter` agents — the concept's definition needs
   revision, or the chapters need to converge.

## Concept file format

```markdown
# `<name>`

## Context
(optional — short orientation: what this is, where it shows up, when to reach for it)

**Signature.** `<Haskell `::` type or pseudo-signature>`  (records use the TS brace form `{ field: type }`)

**Shape contract.** `<bunsen-DimExpr-style named-axis shape annotation>`

**Definition.** Prose + equations defining the operation, concept, or record data-shape. (A concept page does NOT
restate the operators' algebraic laws — those live in the authoritative L_n operator entry, forwarded to from here.)

**Referenced by.**
- [`<chapter>`](../L<n>/<chapter>.md)
- [`<feature column>`](../feature/<name>.L<n>.md)

## Working Notes
(optional — todos, ambiguities, open questions tied to this concept)
```

The `Context` and `Working Notes` sections are general agent-facing affordances available on any chapter content.

## Index

Maintained by the integrator: a new `concepts/<name>.md` page lands as an alpha-positioned row here. The per-page
"referenced by" enumeration is not kept in this table (too expensive to keep accurate) —
`dependency-map.md` gives the layered cross-reference view, and `grep -rl "concepts/<name>.md" book/src/` answers the
"where is this used" question reliably across the L_n Parts, lowering Parts, and the feature spine.

**Kind values**:
- `methodology` — concepts about the dissection process itself (rotation, variant-absorption, …).
- `algorithm` — algorithmic patterns above the leaf primitives (chebyshev-iteration, orthogonalization, incremental-least-squares, …).
- `primitive` — base tensor/linear-algebra operations (axpy, dot, apply_linop, …).
- `layer-pattern` — concepts naming how L1/L2/L3/L4 work (state-stratification, solve-monad, tensor-field-lift, …).
- `auxiliary` — supporting concepts that don't fit the other categories.
- `record` — data-shape definition pages: the fields / types / meaning / construction-vs-run-time stratum / L0 backing home of a record named across ≥2 chapters (the record-definition obligation, directive-2). Counterpart to the behavior-side Kinds; defines the *data shape*, not the operator algebra over it.

| Concept | Kind |
|---------|------|
| [apply_BA](./apply_BA.md) | primitive |
| [apply_linop](./apply_linop.md) | primitive |
| [axpy](./axpy.md) | primitive |
| [black-box-vs-accelerated-kernels](./black-box-vs-accelerated-kernels.md) | methodology |
| [build-time-vs-run-time-stratification](./build-time-vs-run-time-stratification.md) | layer-pattern |
| [capability-typing](./capability-typing.md) | methodology |
| [chebyshev-iteration](./chebyshev-iteration.md) | algorithm |
| [complex-from-real-lift](./complex-from-real-lift.md) | primitive |
| [config-record](./config-record.md) | record |
| [constructed-operator-factory](./constructed-operator-factory.md) | layer-pattern |
| [constructed-operators](./constructed-operators.md) | methodology |
| [convergence-test](./convergence-test.md) | auxiliary |
| [counter-update](./counter-update.md) | primitive |
| [derived-view-hoisting](./derived-view-hoisting.md) | layer-pattern |
| [dofset](./dofset.md) | record |
| [dot](./dot.md) | primitive |
| [eigsolve](./eigsolve.md) | layer-pattern |
| [elementwise-product](./elementwise-product.md) | primitive |
| [erasure-scope](./erasure-scope.md) | layer-pattern |
| [finest-level-unwrap](./finest-level-unwrap.md) | primitive |
| [first-iteration-unrolling](./first-iteration-unrolling.md) | layer-pattern |
| [gemv_basis](./gemv_basis.md) | primitive |
| [givens](./givens.md) | primitive |
| [givens_apply](./givens_apply.md) | primitive |
| [givens_generate](./givens_generate.md) | primitive |
| [gmres](./gmres.md) | algorithm |
| [incremental-least-squares](./incremental-least-squares.md) | algorithm |
| [krylov](./krylov.md) | record |
| [ksp_solve](./ksp_solve.md) | layer-pattern |
| [negative-result-slice](./negative-result-slice.md) | methodology |
| [nested-constructed-operator-gate](./nested-constructed-operator-gate.md) | layer-pattern |
| [nrm2](./nrm2.md) | primitive |
| [op-params](./op-params.md) | record |
| [orthogonalization](./orthogonalization.md) | algorithm |
| [plane-rotation-stream](./plane-rotation-stream.md) | layer-pattern |
| [prev-carry](./prev-carry.md) | record |
| [rotation](./rotation.md) | methodology |
| [scal](./scal.md) | primitive |
| [scalar-promotion](./scalar-promotion.md) | methodology |
| [scope-out-obstruction](./scope-out-obstruction.md) | methodology |
| [sequential-obstruction](./sequential-obstruction.md) | layer-pattern |
| [set_subvector_zero](./set_subvector_zero.md) | primitive |
| [sim-state](./sim-state.md) | record |
| [solve-monad](./solve-monad.md) | layer-pattern |
| [solve-result](./solve-result.md) | record |
| [solver-as-operator](./solver-as-operator.md) | layer-pattern |
| [state-stratification](./state-stratification.md) | layer-pattern |
| [step-outputs](./step-outputs.md) | record |
| [tensor-field-lift](./tensor-field-lift.md) | layer-pattern |
| [trsv](./trsv.md) | primitive |
| [two_operator_split](./two_operator_split.md) | methodology |
| [variant-absorption](./variant-absorption.md) | methodology |
