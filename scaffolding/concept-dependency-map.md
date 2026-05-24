# Concept dependency map — scaffolding / WIP

Working version of the concept dependency map. The book version at `book/src/concepts/dependency-map.md` is the canonical rendered artifact; this scaffolding version is the workshop.

## What lives here vs. in the book

**Book** (`book/src/concepts/dependency-map.md`):
- Stable concepts that have entries in `book/src/concepts/`.
- Dependencies between those concepts.
- Mermaid diagrams for each layer.

**Scaffolding** (this file):
- **Pending concept extractions.** A cycle's Synthesizer noticed a primitive that should become a concept entry but hasn't yet written it. Tracked here so the next cycle's Planner can schedule the extraction.
- **Cross-cutting dependencies the Meta-Critic notices** but hasn't yet incorporated into individual concept entries. E.g., "rotation and variant-absorption both have a 'levels of...' structure; refactor to share?"
- **Hypothetical / not-yet-needed concepts.** "We'll need something like 'effect-tracking' when we reach L4 for a slice with logging."
- **Cross-layer observations.** When a single concept obviously spans layers (e.g., `matvec` exists at L1 as an explicit primitive and at L2 as a composed primitive; the relationship between the two forms is structural and worth tracking).

## Mirror of current book state

(Updated 2026-05-23.)

### Methodology concepts (cross-layer)

- `rotation` — root concept (book: `concepts/rotation.md`)
- `variant-absorption` → `rotation` (book: `concepts/variant-absorption.md`)
- `constructed-operators` → `rotation`, `variant-absorption` (book: `concepts/constructed-operators.md`)

### L1 / L2 / L3 / L4 support concepts

Empty. Will populate as the agent loop's Synthesizer extracts concept entries from slice work, now that apply-on-revise (per CLAUDE.md *Process* #5) means slice diffs actually land.

## Pending concept extractions

(Tracked from current cycle observations. Removed when the concept entry is written to `book/src/concepts/`.)

- **axpy** (L1) — referenced by every Krylov-family slice; needs entry. Signature roughly `axpy :: α → x → y → y'` (returns `α·x + y`). Mutation pattern in source: `y.Add(α, x)`.
- **dot** (L1) — inner product, used in CG and GMRES. Mutation pattern: pure (returns scalar).
- **norml2** (L1) — L2 norm, MPI-collective in distributed mode (out of scope per CLAUDE.md). Returns scalar.
- **matvec** (L1) — matrix-vector product `y = A·x`. Mutation pattern in source: `A.Mult(x, y)` (overwrites y).
- **apply_linop** (L1) — generic linear operator application (matvec for non-matrix operators like preconditioners). `y = op.apply(x)`.
- **arnoldi_step** (L1) — one step of Arnoldi orthogonalization. Hides V/H/Givens indexing per `rotation.md` criterion (1). Will need a primitive choice between MGS/CGS/CGS2 variants — natural fit for `constructed-operators.md` pattern.
- **givens_rotation** (L1) — incremental QR via Givens rotations on a Hessenberg column. Stateless per-application; the *sequence* is what matters at L1 (carries `(cs, sn)` accumulator).
- **hessenberg_extend** (L1) — extend a Hessenberg matrix by one column.

These are candidates the GMRES Phase 6 cycles 2-9 referenced repeatedly but never extracted (because no diffs landed). Once apply-on-revise lands a GMRES slice diff (cycle 10+), the Synthesizer should extract these concept entries proactively per `prompts/synthesizer.md` *Build vocabulary bottom-up*.

## Cross-cutting observations (not yet integrated)

- **`rotation` and `variant-absorption` share a "levels of..." structure.** Both have a primary criterion that holds at multiple levels (rotation: 1/2/3 criteria; variant-absorption: invariant / procedural / primitive-sequence). Both have a "partial holding is acceptable if explicitly disclosed" clause. May be worth a meta-concept "graded methodology criteria" that both inherit from. **Status:** observed during meta-review #3 enactment; not yet acted on. Wait for a third "graded criteria" concept before considering meta-extraction.

- **Carry-through (rotation.md) and partial absorption (variant-absorption.md) are structurally similar.** Both say "the rule allows for partial application provided you disclose what isn't fully applied." Same shape: meta-rule about how strict-rules-with-exceptions should be authored. May want a "disclosed exceptions" meta-concept later.

## Hypothetical / not-yet-needed

- **effect-tracking** (L4) — when L4 is built for a slice with logging / monitoring / I/O effects, the calculus will need a way to thread effect types. Probably a monad-transformer-like structure but the L4 calculus doc may have a different approach.
- **basis-handle** (L1/L2) — for slices like GMRES with explicit Krylov basis management, a `BasisHandle` constructed-operator that hides storage layout (V allocation, growth, indexing). Mentioned in `constructed-operators.md` examples.

## Maintenance protocol (workshop side)

This file is **mutable** (unlike the book version which follows append-only-with-stub-markers discipline). When a pending extraction is completed, move it from "Pending" to "Mirror of current book state." When a cross-cutting observation is acted on (concept created, meta-review item, etc.), strike it through with a note pointing at the resolution rather than deleting.

The Synthesizer / Meta-Critic update this file when:
- Identifying a primitive that should become a concept but isn't yet written.
- Noticing a cross-cutting pattern that doesn't yet have a methodology concept.
- Anticipating a future concept need.
