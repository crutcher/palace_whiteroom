---
edges:
  reference:
    - concepts/sequential-obstruction
    - L1-L0/triangular-solve-obstruction
    - L4/chebyshev
---

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

- `polynomial_recurrence_step` (the scope question; its catalog is absorbed into this page's §Partial-positive sub-pattern and §Falsification criterion below — the Phase-1 slice was deleted cycle-098 as reachability-GC detritus, its Chebyshev-pair firm home is `book/src/L4/chebyshev.md` §Semantics `innerStep`) — three independent scalar-update sequences (Chebyshev-4th-kind, Chebyshev-1st-kind, GMRES Givens stream) plus one out-of-scope branch (eigenvalue tracking via SLEPc/ARPACK). No Palace-level unification.
- [`triangular-solve-obstruction`](../L1-L0/triangular-solve-obstruction.md) (the firm L1>L0 home; the
  Phase-1 `sparse_triangular_solve` slice was absorbed here cycle-097) — the scope question (sparse
  `Ly=b`/`Uy=b`, factor Allgatherv, residual check) returns a negative result: Palace carries no
  Palace-level triangular-solve form. SuperLU/STRUMPACK/MUMPS are thin opaque `mfem::Solver`
  forwarders (the factor interior lives below the project boundary). This is the canonical L0→L1
  **scope-out obstruction** (`trsv` obstruction-shadow) — the L0→L1 analogue of
  [`sequential-obstruction`](./sequential-obstruction.md)'s L2→L3 negative result.

## Partial-positive sub-pattern

A negative result at one scope can coexist with a *positive* unification at a narrower scope. A negative-result slice is not required to be uniformly negative — it should record **where unification fails AND where it would succeed**, scoped explicitly so the two claims do not contradict. This is the **partial-positive sub-pattern**.

The shape:

- The **outer (cross-family) scope** is the negative result: N≥2 independent sites that the scope question presupposed sharing a kernel, but the source does not unify. The distinction catalog and the five-axis difference table are the evidence.
- A **nested (within-family) scope** is a partial positive: a *subset* of those sites agrees on most axes and differs on a single residual axis, so a clean parametric unification *would* land there. This is documented as a distinct claim, with its **own falsification criterion**, alongside the cross-family negative result.

The two claims are kept honest by scope: "the sites do not unify" is true *cross-family*; "two of them differ on a single axis and could be parametrically unified" is true *within-family*. Conflating the scopes is the failure mode — either overstating the negative (eliding the within-family opportunity) or overstating the positive (claiming a unification the cross-family evidence refutes).

The canonical worked example is the `polynomial_recurrence_step` scope question's within-Chebyshev "L1 ↔ L1 self-tightening" finding (the Phase-1 slice was absorbed into this page and deleted cycle-098; its Chebyshev-pair firm home is `book/src/L4/chebyshev.md` §Semantics `innerStep`). Cross-family (Chebyshev ↔ GMRES ↔ eigentracking) the result is negative — different scalar-state cardinalities, recurrence kinds, vector-update kernels, and termination shapes (the five-axis table). Within the Chebyshev family, however, 4th-kind and 1st-kind agree on **four of five axes** (vector-update shape, persisted-state shape, termination shape, outer-driver shape) and differ only on the **scalar-recurrence kind** — so a `ChebyshevSmootherBase<ScalarGenerator>` parameterized on the single residual axis would absorb both variants cleanly. That refactor is structurally documented as a within-family partial positive *without* weakening the cross-family negative result; the within-family claim carries its own falsification surface (the vector-update / outer-driver / termination shapes diverging between the two Chebyshev variants).

When recording a partial positive, the discipline is:

1. State the cross-family negative result first; it is the slice's primary output.
2. Scope the within-family positive explicitly (which subset of sites, on which axes they agree, on which single axis they differ).
3. Give the partial positive its **own** falsification criterion — what source-side divergence would downgrade it to "no within-family unification either." A partial positive without its own falsification surface is indistinguishable from spec-side wishful symmetry (the same bar the cross-family absence claim must meet).
4. Do not promote the within-family unification to a Palace-level primitive on the strength of one within-family case — that is still spec invention. Record it as a documented refactor opportunity; promote to a concept only when a *second* within-family case appears.

## Falsification criterion (required structural element)

A negative-result slice asserts the **absence** of a unification, kernel, or shared abstraction. Absence claims are only auditable if they specify what evidence would overturn them. Therefore every negative-result slice MUST include a `### Falsification criterion` subsection within its L1 (or wherever the negative claim is stated) enumerating:

1. **Specific source-side events** that would falsify the absence claim. Each should name (a) a symbol, file, or namespace location and (b) the property that would have to hold there.
2. **Evidence bar**: what concrete citation (file:line range, symbol name, call graph) a future cycle would have to produce to convert the negative result to a positive unification.

Absence-of-X is not falsified by spec-side desire for symmetry, by methodology arguments that X *could* exist, or by textbook treatments that *suggest* X. Only by an actual source-side citation matching the falsification criterion.

This is symmetric to how a [`sequential-obstruction`](./sequential-obstruction.md) names what would have to hold for the obstruction to lift (a global form for the genuinely-sequential algorithm), and to how an OBSTRUCTION claim in a `rotation_claim` names the specific reason the rotation does not proceed. A negative-result slice without a falsification criterion is structurally indistinguishable from a slice that just hasn't found the unification yet.

The falsification criterion also serves as **forward-anchor** for future cycles: a Planner doing a refinement push on a negative-result slice consults the criterion to decide whether new source evidence has accumulated. The polynomial_recurrence_step slice (2026-05-26) is the canonical worked example.
