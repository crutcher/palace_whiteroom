# scope-out-obstruction

The **L0→L1 negative-result pattern**: when a scope question targets
primitives or state that live *below the codebase boundary* — inside
a third-party library the codebase forwards to opaquely — the
correct L1 form is a disclosed obstruction, not a manufactured
abstraction.

## Pattern shape

A scope-out obstruction slice has the following structure:

1. **L0 evidence of opaque forwarding.** The codebase exposes the
   target functionality through thin wrapper classes whose method
   bodies are literal forwards into a third-party library. No
   in-codebase data structure represents the named machinery (factor
   storage, internal traffic, residual computation, etc.).
2. **Named wrapper-level carry-through.** The rotation that *does*
   apply at the wrapper boundary is identified — typically a
   black-box operator absorption (e.g.,
   [apply_linop](./apply_linop.md) / [ksp_solve](./ksp_solve.md)) that
   is **not specific** to the scope question's framing. The slice
   forward-points at the slice where that rotation lands.
3. **L1 obstruction statement.** The L1 section explicitly states
   "no L1 form exists at this codebase's level" and names the
   boundary that owns the missing content.
4. **Variant-absorption disclosure.** The negative result is
   classified against [variant-absorption](./variant-absorption.md)'s
   *scope-out* path: the orthogonal axis (which third-party backend,
   plus internal traffic patterns) is disclosed as out of scope,
   not silently absorbed.

## Relation to sequential-obstruction

This is the **L0→L1 analogue** of
[sequential-obstruction](./sequential-obstruction.md), which is the
L2→L3 negative result ("genuinely sequential, no global tensor-field
form"). Both are first-class outputs of the rotation process:

| Layer transition | Obstruction concept    | Reason no rotation exists                    |
|------------------|------------------------|----------------------------------------------|
| L0 → L1         | scope-out-obstruction  | implementation lives below codebase boundary |
| L2 → L3         | sequential-obstruction | algorithm is genuinely sequential            |

Neither failure is a defect of the methodology; both are accurate
claims about the material. Recording them as slices prevents future
cycles from re-exploring the same ground and gives downstream slices
a cited reference point.

## Distinguishing from silent partial absorption

A **silent scope-out** would emit an L1 form that pretends the
variant axis doesn't exist — e.g., picking one backend's behavior
as the canonical L1 statement and never mentioning the others. That
fails [variant-absorption](./variant-absorption.md)'s level-(b) and
level-(c) requirements (procedural and primitive-sequence absorption)
and is a methodology defect.

A **disclosed scope-out obstruction** — this pattern — instead
names the obstruction, cites the opaque-forwarding evidence at L0,
and points at the wrapper-level rotation that does land in a
different slice. The variant axis is acknowledged and explicitly
scoped out, satisfying variant-absorption's *scope-out* resolution
path.

## Canonical instance

[sparse_triangular_solve](../spec/slices/sparse_triangular_solve.md):
the scope question targeted sparse triangular solves with
factor-Allgatherv and residual checks. Palace forwards sparse-direct
solves through `mfem::superlu::SuperLUSolver` /
`mfem::STRUMPACKSolver` / `mfem::MUMPSSolver` wrappers and does not
see the factor interior; the named machinery lives inside
SuperLU_DIST / STRUMPACK / MUMPS. The wrapper-level rotation that
does apply is the absorption into
[apply_linop](./apply_linop.md) / [ksp_solve](./ksp_solve.md) — a
black-box linear-operator inverse, indifferent to triangular
structure.

## When to use this pattern

Reach for scope-out-obstruction when:

- L0 dissection finds only opaque forwarding bodies for the
  scope-question's target.
- The named machinery (state, traffic, residual computation)
  demonstrably lives inside a third-party library.
- The rotation that *does* apply at the wrapper boundary is
  available but **not specific** to the scope question's framing
  — it would apply identically to any black-box operator inverse.

Do NOT reach for it when:

- The implementation exists in-codebase but is structured
  awkwardly. That's a normal L0→L1 with possible push-back to L0.
- A variant axis exists and the codebase observes it. That's a
  [variant-absorption](./variant-absorption.md) problem requiring
  parametric or [constructed-operator](./constructed-operators.md)
  absorption, not scope-out.
- Only some backends are forwarded opaquely. Mixed cases are
  partial scope-out and require careful disclosure of which
  surface is in-codebase vs. external.
