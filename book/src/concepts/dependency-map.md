# Concept dependency map

Per-layer map of concepts in `book/src/concepts/`. Maintained by the Synthesizer when emitting new concept entries (per `prompts/synthesizer.md` *Build vocabulary bottom-up*).

The map serves two purposes:
- **Bottom-up vocabulary.** Support-operator concepts at L1 give the vocabulary to describe complex L1 slices concisely; L2 algebraic decompositions give the vocabulary for L2 slices, etc. Reading the map answers "what primitives does this layer have available?"
- **Cross-cutting framework discovery.** Methodology concepts (rotation, variant-absorption, constructed-operators) accumulate from cross-cycle friction integration. Reading the map answers "what methodology tools does the loop have available for handling cross-cutting concerns?"

The scaffolding WIP version at `scaffolding/concept-dependency-map.md` tracks pending extractions and hypothetical concepts that aren't yet stable enough for the book.

## Methodology concepts (cross-layer)

Methodology primitives applicable across all layers. Extracted from cross-cycle friction during meta-reviews.

```mermaid
graph BT
  variant-absorption --> rotation
  constructed-operators --> rotation
  constructed-operators --> variant-absorption
  sequential-obstruction --> rotation
  sequential-obstruction --> tensor-field-lift
  state-stratification --> variant-absorption
  state-stratification --> constructed-operators
  state-stratification --> sequential-obstruction
  solve-monad --> state-stratification
  solve-monad --> sequential-obstruction
  solve-monad --> constructed-operators
  solve-monad --> variant-absorption
  derived-view-hoisting --> rotation
```

- [`rotation`](./rotation.md) — root methodology concept. Defines what counts as a genuine rotation (state hiding / coarser substitution / threaded-state compression) vs. a renaming. Codified meta-review #1; expanded with carry-through clause meta-review #2.
- [`variant-absorption`](./variant-absorption.md) → depends on `rotation`. Parametric vs. appended absorption of orthogonal variants; levels-of-absorption refinement meta-review #3 (invariant / procedural / primitive-sequence).
- [`constructed-operators`](./constructed-operators.md) → depends on `rotation`, `variant-absorption`. Standard graph-evaluation pattern: construct an operator with internal immutable state once, apply pure-function many times. Canonical route to full variant absorption (all three levels) when configs/tables would otherwise be deep-plumbed.

## L1 — mutation-lifted primitives

Pure-functional re-expressions of in-place mutations from source. Each concept names: signature, input/output sets, mutation pattern observed in source.

(Empty as of 2026-05-23. Will populate as the agent loop's Synthesizer extracts support-operator concepts from slice work. Expected initial candidates from CG/GMRES, per BOOTSTRAP verification rubric: `axpy`, `dot`, `matvec`, `apply_linop`, `norml2`. From GMRES specifically: `arnoldi_step`, `givens_rotation`, `hessenberg_extend`.)

```mermaid
graph BT
  %% Empty — populate as concepts are extracted.
  placeholder[(no concepts yet)]
  orthogonalize_column --> variant-absorption
  gmres --> constructed-operators
  gmres --> variant-absorption
  gmres --> orthogonalization
  gmres --> incremental-least-squares
  incremental-least-squares --> orthogonalization
  gmres --> apply_linop
  orthogonalization --> variant-absorption
  chebyshev-iteration --> apply_linop
  chebyshev-iteration --> axpy
```

## L2 — algebraic decompositions

```mermaid
graph BT
  orthog --> dot
  orthog --> axpy
  orthog --> gemv_basis
  orthog --> allreduce_sum
  gemv_basis --> axpy
  nrm2 --> dot
  orthogonalization --> dot
  orthogonalization --> axpy
  orthogonalization --> nrm2
  gmres --> axpy
  gmres --> dot
  gmres --> nrm2
  gmres --> apply_linop
  gmres --> orthogonalization
  gmres --> constructed-operators
  gmres --> variant-absorption
  ksp_solve --> apply_linop
  divfree --> apply_linop
  divfree --> set_subvector_zero
  divfree --> ksp_solve
  divfree --> axpy
  divfree --> copy
  chebyshev --> copy
  chebyshev --> zero
  chebyshev --> axpy
  chebyshev --> scal
  chebyshev --> elementwise-product
  chebyshev --> apply_linop
  chebyshev --> extract-diagonal
  chebyshev --> reciprocal
  chebyshev --> spectrum-estimate
  chebyshev --> constructed-operators
  chebyshev --> variant-absorption
  ksp_solve --> constructed-operators
```

Composition of base algebraic primitives, with HPC/SIMD tricks unfolded.

(Empty as of 2026-05-23. Will populate as L1→L2 rotations land.)
s L1→L2 rotations land.)

## L3 — global tensor-field operations

```mermaid
graph BT
  tensor-field-lift --> axpy
  tensor-field-lift --> dot
  tensor-field-lift --> nrm2
  tensor-field-lift --> apply_linop
  gmres-L3 --> tensor-field-lift
  gmres-L3 --> sequential-obstruction
  divfree --> apply_linop
  divfree --> set_subvector_zero
  divfree --> ksp_solve
  divfree --> axpy
  divfree --> tensor-field-lift
  divfree --> sequential-obstruction
  orthog --> sequential-obstruction
  orthog --> tensor-field-lift
  orthog --> gemv_basis
  orthog --> apply_linop
  chebyshev --> tensor-field-lift
  chebyshev --> sequential-obstruction
  chebyshev --> apply_linop
  chebyshev --> axpy
  chebyshev --> elementwise-product
  cg --> apply_linop
  cg --> axpy
  cg --> axpby
  cg --> dot
  cg --> sequential-obstruction
```

Whole-tensor operations replacing per-element iteration; or `obstruction` results documenting genuine sequentiality.

(Empty as of 2026-05-23. Will populate as L2→L3 rotations land. Expect Krylov outer loops and Arnoldi orthogonalization to be obstructions, not lifts.)
bstructions, not lifts.)

## L4 — formal calculus terms

```mermaid
graph BT
  solve-monad --> state-stratification
  solve-monad --> constructed-operators
  solve-monad --> sequential-obstruction
  gmres-L4 --> state-stratification
  gmres-L4 --> solve-monad
  gmres-L4 --> constructed-operators
  gmres-L4 --> variant-absorption
  gmres-L4 --> sequential-obstruction
  gmres --> state-stratification
  gmres --> solve-monad
  gmres --> constructed-operators
  gmres --> variant-absorption
  gmres --> sequential-obstruction
  state-stratification --> constructed-operators
  state-stratification --> variant-absorption
  state-stratification --> sequential-obstruction
  convergence-test --> constructed-operators
  convergence-test --> variant-absorption
  convergence-test --> solve-monad
  gmres --> convergence-test
```

The L4 calculus has its own design artifact at [`book/src/design/l4_calculus.md`](../design/l4_calculus.md). L4 concepts (grammar productions, reduction rules, ownership categories) are not currently tracked here — the calculus is a single document with its own internal structure. If L4 grows to need cross-cycle concept tracking, add a section here at that time.

## Maintenance protocol

When the Synthesizer emits a slice diff that introduces a new concept entry, the **same diff** must update this dependency map. Specifically:

1. **Add the new concept** under its appropriate layer subsection above.
2. **List its dependencies** — the other concepts (at the same layer or below) it references in its body.
3. **Update the mermaid graph** for that layer to reflect the new node and edges.

A concept entry that exists in `book/src/concepts/` but is not represented in this map fails the slice-acceptance criteria — it's structurally orphaned. The Critic's check #N (to be added when friction warrants enforcement) verifies that every concept page has a corresponding map entry and that declared dependencies match body references.

The scaffolding version at `scaffolding/concept-dependency-map.md` is the workshop where:
- Pending concept extractions are sketched before they stabilize.
- Cross-cutting dependencies the Meta-Critic notices but hasn't yet incorporated are tracked.
- Hypothetical concepts ("we'll need something like X eventually") are listed for future cycles to act on.

## Origin

Introduced 2026-05-23 by user direction during the same conversation as the apply-on-revise methodology fix and the constructed-operators concept. The map is the artifact that operationalizes the "build vocabulary bottom-up" principle from `prompts/synthesizer.md` and CLAUDE.md *Process* #5.
