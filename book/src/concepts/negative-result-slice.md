# Negative-result slice

A slice whose primary output is a structured **non-existence** finding: a scope question is asked, the source is examined, and the answer is "the abstraction the question presupposes does not exist as a shared kernel." The slice's value is in the *catalog* of what the source DOES carry instead, with explicit non-unification recorded.

## Why it is first-class

Negative results are load-bearing for the dissection methodology:

1. They prevent future cycles from re-asking the same question (the slice is the record of the prior investigation).
2. They prevent the spec from silently inventing structure the source does not have — the temptation, when a question like "is there a `polynomial_recurrence_step`?" comes back with three independent sites, is to introduce a spec-level unifying concept anyway. The negative-result slice resists that by *naming the non-unification* as the result.
3. They are the right output shape when the source has either obstructions (out-of-scope sites below the project boundary) or genuine independence (textually unrelated sites that the methodology *suggests* might be unified but the source does not unify).

## Distinction from sister patterns

- [`sequential-obstruction`](./sequential-obstruction.md) — applies when the L2→L3 lift fails because the algorithm is genuinely sequential (Gauss-Seidel, triangular solve). The slice still has an L1/L2 form; only L3 is the obstruction. A negative-result slice is more radical: the *scope question itself* is answered with non-existence at the top level.
- [`obstruction-claim`](./sequential-obstruction.md) — a per-edge obstruction within an otherwise-rotated slice. The negative-result slice is a *whole-slice* version: every layer above L0 is structured around the non-existence.

## L1 form: distinction catalog

When the scope question's presupposed abstraction does not exist, the L1 form is a **distinction catalog**:

- Enumerate each independent site the question would have unified.
- Name the state schema, the per-step operation, and the file location of each.
- Explicitly record what IS shared (often: nothing, or a narrow file-local helper) and what is NOT.
- Reserve the methodology-level term (e.g., `polynomial_recurrence_step`) as a *tracking term* for the scope question, not as a Palace-level primitive.

The catalog is the L1 statement; L2 / L3 / L4 may or may not be filled in depending on whether the individual sites have their own dedicated slices.

## When to use

Use a negative-result slice when:

- The scope question presupposes a shared abstraction across N≥2 sites.
- Empirical reading of the source reveals the sites are independently implemented with no shared kernel beyond (possibly) narrow file-local helpers.
- Some of the N sites are below the project boundary (e.g., delegated to a third-party library) and the question cannot be answered there from inside the project.
- The methodology *suggests* (via accumulated lessons) that unification is possible, but the source has not realized it.

## Relation to spec invention

A negative-result slice is the methodology's check against **spec invention** — the tempting move of writing a spec-level unifying concept that has no source citation and is justified only by accumulated lessons. The negative-result slice preserves the lessons (in `lessons.md`) and the scope question (in the slice's Context section) without crystallizing a fictional kernel.

If a later cycle finds that the source HAS unified the sites (e.g., a refactor lands), the negative-result slice can be replaced by a positive slice — the catalog becomes a record of the pre-unification state.

## Examples in this spec

- [`polynomial_recurrence_step`](../spec/slices/polynomial_recurrence_step.md) — three independent scalar-update sequences (Chebyshev-4th-kind, Chebyshev-1st-kind, GMRES Givens stream) plus one out-of-scope branch (eigenvalue tracking via SLEPc/ARPACK). No Palace-level unification.

## Falsification criterion (required structural element)

A negative-result slice asserts the **absence** of a unification, kernel, or shared abstraction. Absence claims are only auditable if they specify what evidence would overturn them. Therefore every negative-result slice MUST include a `### Falsification criterion` subsection within its L1 (or wherever the negative claim is stated) enumerating:

1. **Specific source-side events** that would falsify the absence claim. Each should name (a) a symbol, file, or namespace location and (b) the property that would have to hold there.
2. **Evidence bar**: what concrete citation (file:line range, symbol name, call graph) a future cycle would have to produce to convert the negative result to a positive unification.

Absence-of-X is not falsified by spec-side desire for symmetry, by methodology arguments that X *could* exist, or by textbook treatments that *suggest* X. Only by an actual source-side citation matching the falsification criterion.

This is symmetric to how a [`sequential-obstruction`](./sequential-obstruction.md) names what would have to hold for the obstruction to lift (a global form for the genuinely-sequential algorithm), and to how an OBSTRUCTION claim in a `rotation_claim` names the specific reason the rotation does not proceed. A negative-result slice without a falsification criterion is structurally indistinguishable from a slice that just hasn't found the unification yet.

The falsification criterion also serves as **forward-anchor** for future cycles: a Planner doing a refinement push on a negative-result slice consults the criterion to decide whether new source evidence has accumulated. The polynomial_recurrence_step slice (2026-05-26) is the canonical worked example.
