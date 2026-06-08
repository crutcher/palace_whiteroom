---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/fem/fespace.hpp:200-286
      kind: cites-evidence            # class FiniteElementSpaceHierarchy: fespaces (:203), mutable lazy P (:204) + BuildProlongationAtLevel (:206), seed ctor (:210-213), AddLevel = push_back + nullptr slot (:217-221), accessors GetNumLevels/GetFESpaceAtLevel/GetFinestFESpace/GetProlongationAtLevel/GetProlongationOperators/GetDiscreteInterpolators (:215-285)
  reference:
    - L1/fe_space_hierarchy
    - L1/fe_space
    - feature/geometric-multigrid-preconditioner.L4
    - feature/geometric-multigrid-preconditioner.L1
    - concepts/mesh
    - concepts/build-time-vs-run-time-stratification
---

# FiniteElementSpaceHierarchy

> **Kind: `record`.** This page defines the *data shape* of `FiniteElementSpaceHierarchy` —
> its fields, their types and meaning, the construction-vs-run-time stratum of each, and the
> L0 source home the backing C++ class mirrors. The *behaviour* — how
> [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) constructs it (the `AddLevel`-fold) and
> how the [geometric-multigrid preconditioner](../feature/geometric-multigrid-preconditioner.L4.md)
> consumes its prolongation level-stack — lives in those chapters; this page does not restate
> that algebra.

`FiniteElementSpaceHierarchy` is the Palace **coarse-to-fine stack of typed finite-element
spaces** — the geometric/p-multigrid level hierarchy the multigrid preconditioner relaxes
over. It is **produced** by [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md)
(`fe_space_hierarchy :: [Mesh] -> [FECollection] -> Config -> FiniteElementSpaceHierarchy`,
the `AddLevel`-fold) and **consumed** by the
[geometric-multigrid preconditioner](../feature/geometric-multigrid-preconditioner.L4.md) — the
V-cycle's inter-level transfers are exactly this record's per-level prolongation operators
`P[l]` (`GetProlongationOperators()` / `GetDiscreteInterpolators()` passed to the
`GeometricMultigridSolver` constructor, `palace/linalg/ksp.cpp:221,228`). Two distinct
consumers (producer + GMG column) put it at the ≥2-consumer bar, so it has a cross-cutting
definition home here rather than only an in-chapter section in its producing chapter.

## One-line semantics

`FiniteElementSpaceHierarchy` is an immutable coarse-to-fine **list of [`fe_space`](../L1/fe_space.md)
values** (`fespaces[0]` coarsest, `fespaces.back()` finest) plus a **lazily-materialized
per-level prolongation operator stack** `P[l]` (each lifting level `l → l+1`). It carries no
algebra of its own: the [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) fold builds it, the
multigrid V-cycle reads its prolongations, and the accessors below are read-as-given.

## Record definition

`FiniteElementSpaceHierarchy` is the backing C++ `class FiniteElementSpaceHierarchy`
(`palace/fem/fespace.hpp:200`). The TS brace form (immutable level stack once built;
per-field strata below):

```text
FiniteElementSpaceHierarchy = {
  fespaces : [FiniteElementSpace],   -- coarse-to-fine level stack; [0] coarsest, back() finest
  P        : [Operator?]             -- per-level prolongation operators P[l] : level l -> l+1
                                     --   (mutable; lazily built; nullptr until first request)
}
```

| field | type | meaning | stratum | L0 source |
|---|---|---|---|---|
| `fespaces` | `[FiniteElementSpace]` | the coarse-to-fine level stack; `fespaces[0]` the coarsest, `fespaces.back()` the finest. Each element is one [`fe_space`](../L1/fe_space.md) value. | construction-time (built by the `AddLevel`-fold; thereafter read-only) | `palace/fem/fespace.hpp:203` |
| `P` | `[Operator?]` (`mutable`) | per-level **prolongation** operators (`P[l]` lifts level `l → l+1`); **lazily** materialized on first `GetProlongationAtLevel(l)` via `BuildProlongationAtLevel` — `nullptr` until then. The V-cycle's `restrict = Pᵀ`, `prolong = P` over exactly these. | run-time (lazy; populated on demand during the multigrid solve, NOT at construction) | `palace/fem/fespace.hpp:204,206` |

The single-machine **read surface** (read-as-given accessors, NOT operations): `GetNumLevels`
(`fespace.hpp:215`), `GetFESpaceAtLevel` (`:223-234`), `GetFinestFESpace` (`:236-247`),
`GetProlongationAtLevel` / `GetProlongationOperators` (`:249-267`),
`GetDiscreteInterpolatorAtLevel` / `GetDiscreteInterpolators` (`:269-285`). The
`GetProlongationOperators()` accessor returns the `GetNumLevels()-1`-length `P[l]` list (one
per inter-level transfer) and is the exact value the multigrid preconditioner consumes by name.

## Stratum — construction-time stack, run-time-lazy prolongations

The two fields split across the stratum boundary (the
[`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md) pattern):

- **`fespaces` is construction-stratum.** The level stack is built once by the
  [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) `AddLevel`-fold (the coarse seed
  `make_unique<FiniteElementSpace>` + the h-/p-refinement `AddLevel` loops) at the start of the
  solve and consumed read-only thereafter; `AddLevel` is strict `push_back` + a `nullptr`
  prolongation slot (`fespace.hpp:217-221`).
- **`P` is run-time-lazy.** Each prolongation slot is `nullptr` after the fold; the operator is
  materialized **on demand** the first time `GetProlongationAtLevel(l)` is called
  (`P[l] ? *P[l] : BuildProlongationAtLevel(l)`, `fespace.hpp:249-255`) — i.e. during the
  multigrid solve, not at construction. The `mutable` keyword on `P` (`fespace.hpp:204`) marks
  it as written-during-`const`-access, the run-time-lazy-cache stratum (the `Mesh.geom_data`
  precedent on [`concepts/mesh`](./mesh.md)). This is read-as-given here, NOT a lifted L1
  operation: the prolongation-build machinery (`BuildProlongationAtLevel`) is sibling-pull-gated
  per the [`fe_space`](../L1/fe_space.md) / [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md)
  deferred-sibling lists.

## L0 source home — the `class FiniteElementSpaceHierarchy`

The backing C++ class is `class FiniteElementSpaceHierarchy` (`palace/fem/fespace.hpp:200-286`):
the protected level vector `fespaces` (`:203`); the `mutable` lazy prolongation vector `P`
(`:204`) + the protected `BuildProlongationAtLevel` (`:206`); the single-arg seed ctor
(`:210-213`, delegating to `AddLevel`); `AddLevel` = `push_back` + `nullptr` slot (`:217-221`);
and the read surface (`:215-285`). The hierarchy value flows from the
[`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) fold
(`ConstructFiniteElementSpaceHierarchy`, `palace/fem/multigrid.hpp:78-126`, `return fespaces`
`:125`) into the Krylov-solver setup, where `GetProlongationOperators()` (and, when an
auxiliary space is present, `GetDiscreteInterpolators()`) are passed to the
`GeometricMultigridSolver` constructor (`palace/linalg/ksp.cpp:221,228`).

**Single-machine carve-outs (flagged once).** Each `FiniteElementSpace` in the stack wraps an
`mfem::ParFiniteElementSpace` (read single-rank per the standing `par-types-single-rank-reading`
rule); the prolongation operators `P[l]` are the single-rank inter-level transfer operators.
Mesh partitioning / multi-rank distribution is out of scope (per CLAUDE.md §Scope). This record
carries the level stack but does not define the multi-rank transfer semantics.

## Signatures that name this record

The ≥2-consumer evidence for the standalone page (producer + GMG column):

- [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) — the **producer**:
  `fe_space_hierarchy :: [Mesh] -> [FECollection] -> Config -> FiniteElementSpaceHierarchy`
  (`book/src/L1/fe_space_hierarchy.md:35,87`).
- [geometric-multigrid preconditioner](../feature/geometric-multigrid-preconditioner.L4.md) —
  the **consumer**: the V-cycle composes the record's `GetProlongationOperators()` level-stack
  by name (the `depends-on (composes)` edge `GMG.L4 → L1/fe_space_hierarchy`;
  `book/src/feature/geometric-multigrid-preconditioner.L4.md`); the L1 surface
  ([`geometric-multigrid-preconditioner.L1`](../feature/geometric-multigrid-preconditioner.L1.md))
  renders the same `restrict = apply_transpose (P[l])` / `prolong = apply (P[l])` transfers.

**Further (non-blocking) fan-out** — the same `GeometricMultigridSolver` (hence the same
hierarchy-prolongation consumption) is also constructed by the firm
[`divfree_projector`](../L1/divfree_projector.md) (`palace/linalg/divfree.cpp:128`), the
H(curl) mass-matrix solver (`palace/linalg/hcurl.cpp:101`), and the AMR flux-recovery error
estimator (`palace/linalg/errorestimator.cpp:86`). These are additional driver-agnostic
consumers of the hierarchy via the GMG infrastructure column; they corroborate the record's
cross-cutting status but are mediated through the GMG column (the consumer named above), so the
≥2 bar is met by producer + GMG column alone.

## See also

- [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) — the producer; defines HOW the hierarchy
  is constructed (the `AddLevel`-fold over per-level [`fe_space`](../L1/fe_space.md)
  constructions). This page defines only the *shape* of its output.
- [geometric-multigrid preconditioner](../feature/geometric-multigrid-preconditioner.L4.md) —
  the consumer; defines the *behaviour over* the prolongation stack (the V-cycle
  restrict/recurse/prolong). This page does NOT restate that algebra.
- [`fe_space`](../L1/fe_space.md) — the element type of `fespaces` (each level is one
  `FiniteElementSpace`).
- [`mesh`](./mesh.md) — the analogous FE-construction record (the `[Mesh]` element of the
  hierarchy's input), same record-definition-page pattern.
- [`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md) — the
  per-field split (`fespaces` construction-time; `P` run-time-lazy).

**If this page and a consumer chapter / the L0 source disagree on any factual claim about the
record, the L0 source (`palace/fem/fespace.hpp`) wins and this page is corrected.**
