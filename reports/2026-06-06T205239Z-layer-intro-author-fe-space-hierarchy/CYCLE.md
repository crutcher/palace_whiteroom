---
agent: layer-intro-author
invoked_at: 2026-06-06T210749Z
scope: L1/fe_space_hierarchy operator (cycle-117 D4, WAVE-1, open-all-feature-fronts front (iii)-a)
status: integrated
integrated_at: 2026-06-06T214845Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-117 D4 (apply-order 3/5). New firm L1 op fe_space_hierarchy (AddLevel-fold p-multigrid combinator composing firm fe_space+fe_collection, well-foundedness firm/firm) + 3 fe_space.md re-anchors + fe-space-intro 3->4 + OWNS the consolidated L1 firm count 40->43 (FE-space sub-spine 4->5). All per-report gates PASS; rank firm/firm (no violation). fe_space_hierarchy lands in STRONGER detritus pending an inbound consumer (GC-ground-don't-remove; NEW node, not a block). Finalize CONFIRMED D5 landed interpolator firm at the FE-space sub-spine -> grand total stays 43 (count-owner reconciliation OQ RESOLVED). 4 OQs promoted."
---

# CYCLE: L1 `fe_space_hierarchy` operator

## Summary

Author ONE new L1 operator: **`fe_space_hierarchy`** — the p-multigrid FE-space
hierarchy as an `AddLevel`-fold over the firm `fe_space` + firm `fe_collection`
vocabulary. The operator constructs a `FiniteElementSpaceHierarchy` (the level
stack the geometric-multigrid preconditioner consumes) from a list of meshes + a
list of FE-collections (the `fe_collection` schedule output).

This is **front (iii)-a** of the cycle-117 `open-all-feature-fronts` wide wave
(the `fe_space` deferred siblings). It promotes the standing `fe_space_hierarchy`
*(rough-in; no anchor yet)* row in the L1 index (line 111) and SUMMARY into a
firm chapter, re-anchors the two `fe_space.md` forward-refs that pointed at
`ConstructFiniteElementSpaceHierarchy` plain-text to live links, and (as
count-owner) applies the consolidated L1 firm-count bump for this cycle's
landing cohort.

**Maturity verdict: `firm` (firm-on-positive-structure).** The whole
`ConstructFiniteElementSpaceHierarchy` body is read from one positive source site
(`palace/fem/multigrid.hpp:78-126`); every law is a syntactic identity on that
structure (the fold shape, the coarse-seed base case, level-monotonicity, the
hierarchy-of-one degeneracy). There is no convergence/iteration semantics to
test-gate, so the absence of a dedicated `test-multigrid.cpp` exercising the
constructor does not gate firm — the `fe_space` (c064) / `fe_collection` (c065) /
`fe_assemble` (c054) / `apply_linop` no-dedicated-test precedent. The
`AddLevel`-fold composes the two firm constituents `fe_space` (per-level) +
`fe_collection` (the `[FECollection]` input); both are firm on disk (evidence
below), so the well-foundedness invariant `rank(u) ≤ min(deps)` holds at
firm/firm. The lazy prolongation operators `P[l]` (`BuildProlongationAtLevel`)
are a sibling-pull-gated property of the result record, read-as-given (not a law
substrate, not a materialized constructive sub-part) — so NOT partly-constructive.

**Record-definition:** `FiniteElementSpaceHierarchy` is the output record of this
ONE operator and is named in no other harvested L1 signature yet (its downstream
multigrid-solver consumers are not yet L1-harvested). Per the record-definition
obligation, a single-consumer record gets an in-chapter `## Record definition`
section (NOT a standalone `concepts/` page — that is the ≥2-consumer bar). I author
that section in the new chapter and FLAG `record-FiniteElementSpaceHierarchy-needs-
definition-home` in Open questions so the obligation is tracked if/when a 2nd
consumer (e.g. a geometric-multigrid L1 operator) surfaces.

## Proposed changes

### 1. New file `book/src/L1/fe_space_hierarchy.md`

```edit:book/src/L1/fe_space_hierarchy.md
[new file]:
---
layer: L1
operator: fe_space_hierarchy
harvested_by: layer-intro-author:2026-06-06T205239Z-layer-intro-author-fe-space-hierarchy
cycle: cycle-117
# Graded-stack scheme (edges authored from scratch). This firm L1 construction is the
# `AddLevel`-fold composition of its two firm L1 constituents — per-level `fe_space`
# (composes; each level is one `fe_space(mesh, collection)` construction) and the
# `[FECollection]` schedule `fe_collection` (composes; the per-level collection list it
# folds over). It cross-links D3's `build_mesh` (`Mesh` record home) as a reference (the
# `[Mesh]` input element type is defined there — navigational, not a constituent-use).
# It rests on its positive L0 ctor source (cites-evidence, rank-terminal ground truth).
# Well-foundedness rank(u) <= rank(v): this node firm (rank 3); both `fe_space` and
# `fe_collection` carry `rank: firm` (status: firm on disk, c064 / c065); the
# cites-evidence target is rank-terminal L0 ground truth. No `lowers-to` edge yet (the
# L1>L0 `fe-space-hierarchy-construction-rotation` theme is sibling-pull-gated, named
# below, NOT authored this cycle).
rank: firm
edges:
  depends-on:
    - target: L1/fe_space
      kind: composes              # each level is one fe_space(mesh, collection) construction (coarse seed :89-90, AddLevel :106/:117)
    - target: L1/fe_collection
      kind: composes              # the [FECollection] schedule it folds one-per-level (fecs[0] :90, fecs[l] :117)
    - target: palace/fem/multigrid.hpp:78-126
      kind: cites-evidence        # ConstructFiniteElementSpaceHierarchy whole body; close brace verified on disk at :126 (return fespaces; :125, } :126)
  reference:
    - L1/build_mesh                # the [Mesh] input element type — the `Mesh` record home (D3 this cycle); navigational, NOT a depends-on
---

# `fe_space_hierarchy` — p-multigrid FE-space hierarchy

`fe_space_hierarchy :: [Mesh] -> [FECollection] -> Config -> FiniteElementSpaceHierarchy`

Construct the **geometric p-multigrid FE-space hierarchy** — the coarse-to-fine
stack of typed finite-element spaces the multigrid preconditioner relaxes over —
by **folding `AddLevel` over repeated [`fe_space`](./fe_space.md) constructions**:
a coarse seed at the coarsest mesh/collection level, then one h-refinement level
per finer mesh and one p-refinement level per finer collection. The
`[FECollection]` input is exactly the finest-to-coarsest schedule that
[`fe_collection`](./fe_collection.md) produces; the `[Mesh]` input is the
coarse-to-fine mesh sequence (each element a [`build_mesh`](./build_mesh.md)
`Mesh`). This is the **hierarchy combinator** the deferred-sibling list of both
`fe_space` (law 4, coarse-seed identity) and `fe_collection` (law 6,
singleton-collapse) pointed at — the fold whose base case is one `fe_space` call
and whose general case stacks per-level `fe_space` constructions over a shared
boundary-condition marker.

## Context

L1 is the mutation-rotation layer: source operations re-expressed as pure
functions. `fe_space_hierarchy` is the **fold-over-construction** view of that
rotation — Palace's `ConstructFiniteElementSpaceHierarchy` imperatively
`push_back`s a vector of owned `FiniteElementSpace`s once before the multigrid
solve and thereafter consumes the stack read-only; the L1 form names the pure
`([Mesh], [FECollection], Config) → FiniteElementSpaceHierarchy` fold and treats
the produced hierarchy as an immutable level sequence.

At L0 the construction is the function `ConstructFiniteElementSpaceHierarchy`
(`palace/fem/multigrid.hpp:78-126`). Its body computes a coarse starting level
`coarse_mesh_l` (`multigrid.hpp:87-88`), seeds the hierarchy with one
`std::make_unique<FiniteElementSpace>(*mesh[coarse_mesh_l], fecs[0].get())`
(`multigrid.hpp:89-90`) — i.e. **one [`fe_space`](./fe_space.md) construction** —
then runs two sequential refinement loops that each `AddLevel` one more
`FiniteElementSpace`: an **h-refinement** loop over the remaining finer meshes,
holding the coarsest collection `fecs[0]` fixed (`multigrid.hpp:104-112`, the
`AddLevel(... *mesh[l], fecs[0].get())` at `:106`), and a **p-refinement** loop
over the remaining finer collections, holding the finest mesh `mesh.back()` fixed
(`multigrid.hpp:115-123`, the `AddLevel(... *mesh.back(), fecs[l].get())` at
`:117`). The optional Dirichlet-boundary block (`multigrid.hpp:92-101`) marks the
essential-true-dof set on the finest level after the seed and re-marks it after
each `AddLevel` — exactly the [`essential_dofs`](./essential_dofs.md) construction
applied per level (a hierarchy-consumer property of `essential_dofs`, not a
distinct operation here). The result is the `FiniteElementSpaceHierarchy` value
(`multigrid.hpp:125`, the `return fespaces`).

This chapter is defined in L1 vocabulary (the typed `AddLevel`-fold over per-level
`fe_space` constructions). The forward rewrite into the L0 imperative
`push_back`/`AddLevel` loops is the L1>L0 theme
`fe-space-hierarchy-construction-rotation` (sibling-pull-gated — named, NOT
authored this cycle; see *Downward*).

## Signature

    fe_space_hierarchy :: [Mesh] -> [FECollection] -> Config -> FiniteElementSpaceHierarchy

Shape contract (bunsen-style, named axes):

- `mesh` — `[Mesh]` — the **coarse-to-fine mesh sequence**; one
  [`build_mesh`](./build_mesh.md) `Mesh` per geometric (h-) refinement level
  (`std::vector<std::unique_ptr<Mesh>>`, `multigrid.hpp:79`). A genuine rank-1
  list of meshes (KEEP `[Mesh]`, not a named shape group — see the shape note
  below). `mesh.back()` is the finest mesh, held fixed across the p-refinement
  levels.
- `fecs` — `[FECollection]` — the **coarse-to-fine collection schedule** produced
  by [`fe_collection`](./fe_collection.md) (`multigrid.hpp:80`); a rank-1 list of
  FE-collections, one per p-refinement level. `fecs[0]` is the coarsest
  collection, held fixed across the h-refinement levels.
- `config` — `Config` — the hierarchy control: `mg_max_levels` (the p-multigrid
  level cap that, with `mesh.size() + fecs.size()`, fixes the coarse starting
  level `coarse_mesh_l`, `multigrid.hpp:87-88`) plus the optional Dirichlet-BC
  attributes `dbc_attr` / output `dbc_tdof_lists` (`multigrid.hpp:81-82`). The
  `Config` here is the multigrid-hierarchy slice; see *Config fields* below.
- result — `FiniteElementSpaceHierarchy` — the coarse-to-fine level stack; see
  *Record definition*. `GetNumLevels()` is the produced level count;
  `GetFinestFESpace()` is the finest [`fe_space`](./fe_space.md)
  (`FiniteElementSpace[N]`, `N` its true-dof count).

**Shape note (named shape groups, USE+LINK).** The list inputs `[Mesh]` /
`[FECollection]` and the per-level `FiniteElementSpace[N]` are **genuine rank-1**
structures (a list of meshes; a list of collections; a flat true-dof axis `N`), so
they correctly keep the bare `[·]` / `[N]` form rather than a named shape group
`Tensor[(S: ...)]`. The named-shape-group congruence machinery
(`book/src/semantics/index.md` §1.2.1) governs shape-generic elementwise/reduce
ops; this fold has no rank-agnostic congruence axis to bind — it is a list-fold,
not a shape-generic operator.

## Record definition: `FiniteElementSpaceHierarchy`

The output record is defined here (single-consumer: `fe_space_hierarchy` is the
sole harvested L1 producer/consumer of this type; its downstream
geometric-multigrid solver consumers are not yet L1-harvested). The backing C++
class is `palace::FiniteElementSpaceHierarchy` (`palace/fem/fespace.hpp:200-286`).

| field | type | meaning | stratum |
|---|---|---|---|
| `fespaces` | `[FiniteElementSpace]` | the coarse-to-fine level stack; `fespaces[0]` the coarsest, `fespaces.back()` the finest. Each is one [`fe_space`](./fe_space.md) value. (`fespace.hpp:203`) | construction-time (built by the fold; thereafter read-only) |
| `P` | `[Operator?]` | per-level **prolongation** operators (`P[l]` lifts level `l` → `l+1`); `mutable`, **lazily** materialized on first `GetProlongationAtLevel(l)` via `BuildProlongationAtLevel` (`fespace.hpp:204,206,249-255`) — `nullptr` until then. | run-time (lazy; populated on demand during the multigrid solve, not at construction) |

Accessors (read-as-given, NOT L1 operations): `GetNumLevels`
(`fespace.hpp:215`), `GetFESpaceAtLevel` (`:223-234`), `GetFinestFESpace`
(`:236-247`), `GetProlongationAtLevel` / `GetProlongationOperators`
(`:249-267`), `GetDiscreteInterpolatorAtLevel` / `GetDiscreteInterpolators`
(`:269-285`). The prolongation/interpolator machinery is **sibling-pull-gated**:
the `BuildProlongationAtLevel` (multigrid transfer) and discrete-interpolator
construction are read-as-given properties of the record here, not L1 operations
(the deferred `BuildDiscreteInterpolator` / `BuildProlongationAtLevel` siblings,
named in the `fe_space` deferred-sibling list).

## Config fields (the multigrid-hierarchy slice)

The `Config` argument carries the hierarchy control read by
`ConstructFiniteElementSpaceHierarchy`:

- `mg_max_levels` — `Nat` — the p-multigrid level cap (`multigrid.hpp:78`); with
  the input list sizes it fixes the coarse starting level
  `coarse_mesh_l = max(0, mesh.size() + fecs.size() − 1 − max(1, mg_max_levels))`
  (`multigrid.hpp:87-88`).
- `dbc_attr` — `[Attr]?` — the optional Dirichlet-boundary attribute list
  (`multigrid.hpp:81`); when present (with `dbc_tdof_lists`), the per-level
  essential-true-dof block runs (`multigrid.hpp:92-101`), constructing one
  [`essential_dofs`](./essential_dofs.md) set per level into `dbc_tdof_lists`.
- `dbc_tdof_lists` — `[DofSet[N]]?` — the per-level essential-dof output
  (`multigrid.hpp:82`); one `DofSet` appended per level via `emplace_back`
  (`multigrid.hpp:100,110,121`).

## Algebraic laws

The laws are syntactic identities on the positive `ConstructFiniteElementSpaceHierarchy`
body (no convergence/iteration semantics — the construction is a deterministic
finite fold):

1. **Coarse-seed base case.** The first level of the hierarchy IS one
   [`fe_space`](./fe_space.md) construction:
   `fespaces[0] = fe_space(mesh[coarse_mesh_l], fecs[0])` (`multigrid.hpp:89-90`).
   This is the realization of [`fe_space`](./fe_space.md) law 4 (coarse-seed
   identity) and [`fe_collection`](./fe_collection.md) law 6 (singleton-collapse):
   a hierarchy of one level reduces to a single `fe_space` call.
2. **AddLevel-fold structure.** The hierarchy is the left-fold of `AddLevel` over
   the refinement sequence: starting from the seed, the h-refinement loop appends
   one `fe_space(mesh[l], fecs[0])` per finer mesh (`multigrid.hpp:104-106`) and
   the p-refinement loop appends one `fe_space(mesh.back(), fecs[l])` per finer
   collection (`multigrid.hpp:115-117`). `AddLevel` is `push_back` + a `nullptr`
   prolongation slot (`fespace.hpp:217-221`) — strictly append, order-preserving.
3. **Level-monotonicity (coarse-to-fine).** The produced stack is ordered
   coarsest-first: `fespaces[0]` is the coarse seed, each subsequent `AddLevel`
   appends a strictly-finer level (more meshes refine geometrically; more
   collections refine in order), so `fespaces.back()` (`GetFinestFESpace`,
   `fespace.hpp:236-247`) is the finest level. The h-loop refines `mesh` at fixed
   coarsest collection `fecs[0]`; the p-loop refines `fecs` at fixed finest mesh
   `mesh.back()` — the two refinement axes are independent and sequential.
4. **Determinism.** Given fixed `([Mesh], [FECollection], Config)`, the produced
   hierarchy is a pure deterministic function — same inputs ⟹ same level count,
   same per-level `(mesh, collection)` pairing, same essential-dof sets. The level
   count is `min(mesh.size() + fecs.size() − coarse_mesh_l, ...)` driven by
   `mg_max_levels` (the `coarse_mesh_l` formula caps how many of the input
   meshes/collections become levels).
5. **Per-level essential-dof coherence.** When `dbc_attr` is supplied, the same
   boundary marker (`dbc_marker = mesh::AttrToMarker(bdr_attr_max, *dbc_attr)`,
   `multigrid.hpp:98`) is re-applied via `GetEssentialTrueDofs` to the finest
   level after the seed (`:99-100`) and after every `AddLevel`
   (`:109-110`, `:120-121`). This is exactly [`essential_dofs`](./essential_dofs.md)'s
   per-level-hierarchy-application variant axis — the dof-set on each level is one
   `essential_dofs` construction over the shared marker, not a distinct operation.

**Non-law (read-as-given).** `fe_space_hierarchy` does NOT define the prolongation
operators `P[l]` (lazily built by `BuildProlongationAtLevel`) or the discrete
interpolators — these are sibling-pull-gated multigrid-transfer machinery, read as
given properties of the result record (above). No L1 law constrains them this
cycle.

## Dependencies

Composes two firm L1 constituents (this is a genuine combinator, not a leaf):

- [`fe_space`](./fe_space.md) (firm, c064) — each level is one
  `fe_space(mesh, collection)` construction; the seed (`multigrid.hpp:89-90`) and
  every `AddLevel` (`:106`, `:117`).
- [`fe_collection`](./fe_collection.md) (firm, c065) — produces the
  `[FECollection]` schedule this fold consumes one-per-level (`fecs[0]` at `:90`,
  `fecs[l]` at `:117`).

The `[Mesh]` input element type is the `Mesh` record defined by
[`build_mesh`](./build_mesh.md) (D3 this cycle) — a **reference** (the element
type's definition home), NOT a `depends-on` (the fold does not invoke `build_mesh`;
it consumes already-constructed meshes). The per-level
[`essential_dofs`](./essential_dofs.md) construction is the hierarchy-consumer
application of that operator's per-level variant axis (a consumed relation, not a
dependency).

## Downward (to L0)

The L1>L0 rotation `fe-space-hierarchy-construction-rotation` (sibling-pull-gated;
named, NOT authored this cycle) would narrate how the typed `AddLevel`-fold rewrites
into the L0 imperative `ConstructFiniteElementSpaceHierarchy` body
(`multigrid.hpp:78-126`): the `coarse_mesh_l` computation (`:87-88`), the
`make_unique<FiniteElementSpace>` seed (`:89-90`), the two `AddLevel` refinement
loops (`:104-112`, `:115-123`), and the optional per-level `GetEssentialTrueDofs`
block (`:92-101`). The hierarchy-of-one degeneracy (law 1) is the in-line
annotation already carried by [`fe_space`](./fe_space.md) law 4 — this chapter is
the general fold over that base case.

## Status

**firm (firm-on-positive-structure).** The construction is read in full from one
positive source site: the entire `ConstructFiniteElementSpaceHierarchy` body
(`palace/fem/multigrid.hpp:78-126`). Both composed constituents are firm on disk
([`fe_space`](./fe_space.md) `## Status` line: firm, c064;
[`fe_collection`](./fe_collection.md) `## Status` line: firm, c065), so the
well-foundedness invariant `rank(u) ≤ min(deps)` holds at firm/firm. Every law is a
syntactic identity / fold-invariant on the positive structure (coarse-seed base
case, AddLevel-fold structure, coarse-to-fine level-monotonicity, determinism,
per-level essential-dof coherence) — there is no convergence/iteration semantics to
test-gate, so the absence of a dedicated `test-multigrid.cpp` exercising
`ConstructFiniteElementSpaceHierarchy` does not gate firm (the
[`fe_space`](./fe_space.md) c064 / [`fe_collection`](./fe_collection.md) c065 /
[`fe_assemble`](./fe_assemble.md) c054 / `apply_linop` no-dedicated-test
precedent). The lazy prolongation `P[l]` / discrete-interpolator machinery is
read-as-given (a property of the result record, sibling-pull-gated — NOT a
materialized constructive sub-part from negative anchors, so NOT
partly-constructive).

This is the **hierarchy combinator** of the FE-space sub-spine — the fold whose
base case is one [`fe_space`](./fe_space.md) construction and whose general case
stacks per-level constructions; it closes the `fe_space_hierarchy` deferred-sibling
slot named by both [`fe_space`](./fe_space.md) and [`fe_collection`](./fe_collection.md).

**MPI / `Par*` out of scope (flagged once):** `ConstructFiniteElementSpaceHierarchy`
wraps each level into an `mfem::ParFiniteElementSpace` (read single-rank, per the
existing `par-types-single-rank-reading` rule); mesh partitioning is out of scope.

**Deferred siblings (named, NOT authored this cycle):** the L1>L0
`fe-space-hierarchy-construction-rotation` theme (sibling-pull-gated); the
multigrid-transfer `BuildProlongationAtLevel` (`fespace.hpp:206,249-255`) and the
de-Rham `BuildDiscreteInterpolator` / discrete-interpolator machinery
(`fespace.hpp:269-285`) — both already named sibling-pull-gated in the
[`fe_space`](./fe_space.md) deferred-sibling list. (D5 this cycle lands the de-Rham
interpolator front; this chapter only reads its output as a given property of the
record.)

## Evidence

- `palace/fem/multigrid.hpp:78-126` — `ConstructFiniteElementSpaceHierarchy(int
  mg_max_levels, const std::vector<std::unique_ptr<Mesh>> &mesh, const
  std::vector<std::unique_ptr<FECollection>> &fecs, const mfem::Array<int>
  *dbc_attr, std::vector<mfem::Array<int>> *dbc_tdof_lists)`: the whole fold. The
  signature (`:78-82`); the non-empty `MFEM_VERIFY` (`:84-86`); the `coarse_mesh_l`
  computation (`:87-88`); the coarse-seed single `FiniteElementSpace` construction
  (`:89-90`); the optional Dirichlet block — `bdr_attr_max` (`:95-97`),
  `mesh::AttrToMarker` (`:98`), `GetEssentialTrueDofs` (`:99-100`); the
  h-refinement loop `AddLevel(... *mesh[l], fecs[0].get())` (`:104-112`, the
  `AddLevel` at `:106`); the p-refinement loop `AddLevel(... *mesh.back(),
  fecs[l].get())` (`:115-123`, the `AddLevel` at `:117`); the `return fespaces`
  (`:125`).
- `palace/fem/fespace.hpp:200-286` — the `FiniteElementSpaceHierarchy` class: the
  level vector `fespaces` (`:203`), the mutable lazy prolongation vector `P`
  (`:204`) + `BuildProlongationAtLevel` (`:206`), the seed ctor (`:210-213`),
  `AddLevel` = `push_back` + `nullptr` slot (`:217-221`), `GetNumLevels` (`:215`),
  `GetFESpaceAtLevel` (`:223-234`), `GetFinestFESpace` (`:236-247`),
  `GetProlongationAtLevel`/`GetProlongationOperators` (`:249-267`), the discrete
  interpolators (`:269-285`).
- `palace/fem/multigrid.hpp:22-73` — `ConstructFECollections` (the
  [`fe_collection`](./fe_collection.md) schedule that produces the `[FECollection]`
  input; the p-MG order schedule `:41-69`, the terminal `std::reverse` `:70`).
- `book/src/L1/fe_space.md:149-154` — `fe_space` law 4 (coarse-seed identity) — the
  in-line annotation that the hierarchy folds `AddLevel` over repeated `fe_space`
  constructions; the base case this chapter generalizes.
- `book/src/L1/fe_collection.md:173-177` — `fe_collection` law 6
  (singleton-collapse to one `fe_space` input) — the boundary at which a length-1
  schedule yields a one-level hierarchy = one `fe_space` call.
```

### 2. `book/src/L1/fe_space.md` — re-anchor the two `ConstructFiniteElementSpaceHierarchy` plain-text forward-refs to live links

The `fe_space` chapter currently mentions `ConstructFiniteElementSpaceHierarchy`
in plain text at two spots (the §Context paragraph and the §Downward paragraph).
Re-anchor both to a live link to the new chapter (coupled re-anchor — I own this as
layer-intro-author). Both edits add the live-link parenthetical without altering
the cited L0 line numbers.

```edit:book/src/L1/fe_space.md
[old]: Every solver model operator builds its
spaces this way through `ConstructFiniteElementSpaceHierarchy` (`palace/fem/multigrid.hpp:78-126`),
whose coarse seed is a single `std::make_unique<FiniteElementSpace>(*mesh[coarse_mesh_l], fecs[0].get())`
(`multigrid.hpp:90`) — i.e. one `fe_space` construction — and whose h/p levels each `AddLevel` one more
`FiniteElementSpace` built the same way (`multigrid.hpp:106,117`).
[new]: Every solver model operator builds its
spaces this way through [`fe_space_hierarchy`](./fe_space_hierarchy.md)'s L0 site
`ConstructFiniteElementSpaceHierarchy` (`palace/fem/multigrid.hpp:78-126`),
whose coarse seed is a single `std::make_unique<FiniteElementSpace>(*mesh[coarse_mesh_l], fecs[0].get())`
(`multigrid.hpp:90`) — i.e. one `fe_space` construction — and whose h/p levels each `AddLevel` one more
`FiniteElementSpace` built the same way (`multigrid.hpp:106,117`).
```

```edit:book/src/L1/fe_space.md
[old]: 4. **Coarse-seed identity (hierarchy base case).** The coarsest level of a space hierarchy *is* one
   `fe_space` construction: `ConstructFiniteElementSpaceHierarchy(...)`'s seed is
   `make_unique<FiniteElementSpace>(*mesh[coarse_mesh_l], fecs[0].get())` (`multigrid.hpp:90`). A
   hierarchy of one level reduces to a single `fe_space` call. (This is the in-line annotation of how
   `fe_space` relates to the deferred `fe_space_hierarchy` — the hierarchy folds `AddLevel` over
   repeated `fe_space` constructions.)
[new]: 4. **Coarse-seed identity (hierarchy base case).** The coarsest level of a space hierarchy *is* one
   `fe_space` construction: [`fe_space_hierarchy`](./fe_space_hierarchy.md)'s seed is
   `make_unique<FiniteElementSpace>(*mesh[coarse_mesh_l], fecs[0].get())` (`multigrid.hpp:90`). A
   hierarchy of one level reduces to a single `fe_space` call. (This is the in-line annotation of how
   `fe_space` relates to [`fe_space_hierarchy`](./fe_space_hierarchy.md) — the hierarchy folds `AddLevel`
   over repeated `fe_space` constructions.)
```

Also re-anchor the `fe_space.md` deferred-sibling-list mention (now firm):

```edit:book/src/L1/fe_space.md
[old]: and `fe_space_hierarchy` (the h/p-refinement multigrid stack,
`multigrid.hpp:78-126`). The `BuildDiscreteInterpolator` (de-Rham interpolator) and
`BuildProlongationAtLevel` (multigrid transfer) machinery is sibling-pull-gated — named, not authored.
[new]: and [`fe_space_hierarchy`](./fe_space_hierarchy.md) (the h/p-refinement multigrid stack,
`multigrid.hpp:78-126` — **now firm**, cycle-117 D4). The `BuildDiscreteInterpolator` (de-Rham
interpolator) and `BuildProlongationAtLevel` (multigrid transfer) machinery is sibling-pull-gated —
named, not authored.
```

### 3. `book/src/L1/SUMMARY.md` — add the chapter in alpha position

```edit:book/src/SUMMARY.md
[old]: - [FE-space sub-spine](./L1/fe-space-intro.md)
  - [essential_dofs](./L1/essential_dofs.md)
  - [fe_collection](./L1/fe_collection.md)
  - [fe_space](./L1/fe_space.md)
[new]: - [FE-space sub-spine](./L1/fe-space-intro.md)
  - [essential_dofs](./L1/essential_dofs.md)
  - [fe_collection](./L1/fe_collection.md)
  - [fe_space](./L1/fe_space.md)
  - [fe_space_hierarchy](./L1/fe_space_hierarchy.md)
```

(Alpha order within the FE-space sub-spine grouping: `essential_dofs` <
`fe_collection` < `fe_space` < `fe_space_hierarchy`.)

### 4. `book/src/L1/fe-space-intro.md` — extend the group intro to 4 members

```edit:book/src/L1/fe-space-intro.md
[old]:edges:
  reference:
    - L1/essential_dofs
    - L1/fe_collection
    - L1/fe_space
[new]:edges:
  reference:
    - L1/essential_dofs
    - L1/fe_collection
    - L1/fe_space
    - L1/fe_space_hierarchy
```

```edit:book/src/L1/fe-space-intro.md
[old]: The three members form a small producer→consumer DAG: `fe_collection` schedules the finest-to-coarsest `[FECollection]` p-multigrid order list (`(p, dim, mg_max_levels, coarsening, family) → [FECollection]`); `fe_space` constructs each typed `(mesh, FECollection) → FiniteElementSpace[N]` (de-Rham family variant axis H1/H(curl)/H(div)/L2); `essential_dofs` marks the essential-true-dof set `(space, bdr_attrs, bdr_attr_max) → DofSet[N]` on a constructed space.
[new]: The four members form a small producer→consumer DAG: `fe_collection` schedules the finest-to-coarsest `[FECollection]` p-multigrid order list (`(p, dim, mg_max_levels, coarsening, family) → [FECollection]`); `fe_space` constructs each typed `(mesh, FECollection) → FiniteElementSpace[N]` (de-Rham family variant axis H1/H(curl)/H(div)/L2); `essential_dofs` marks the essential-true-dof set `(space, bdr_attrs, bdr_attr_max) → DofSet[N]` on a constructed space; and `fe_space_hierarchy` folds `AddLevel` over per-level `fe_space` constructions to build the p-multigrid `FiniteElementSpaceHierarchy` (`[Mesh] → [FECollection] → Config → FiniteElementSpaceHierarchy`) — the combinator whose base case is one `fe_space` call.
```

### 5. `book/src/L1/index.md` — promote the `fe_space_hierarchy` Vocabulary-cohort bullet (rough-in → firm), add the dep-map row, and apply the consolidated firm-count bump (count-owner)

#### 5a. Promote the deferred-sibling bullet (line 111) to the FE-space sub-spine firm narrative

```edit:book/src/L1/index.md
[old]: - `fe_space_hierarchy` *(rough-in; no anchor yet)* — the h/p-refinement multigrid stack (`ConstructFiniteElementSpaceHierarchy`, `palace/fem/multigrid.hpp:78-126`); lower fan-out for the assembly front (the geometric-multigrid preconditioner consumes it, not the assembled-operator pipeline).
[new]: - [`fe_space_hierarchy`](./fe_space_hierarchy.md) **is now FIRM** *(cycle-117 D4)* — the p-multigrid FE-space hierarchy `([Mesh], [FECollection], Config) → FiniteElementSpaceHierarchy` (`ConstructFiniteElementSpaceHierarchy`, `palace/fem/multigrid.hpp:78-126`): the **hierarchy combinator** that folds `AddLevel` over per-level [`fe_space`](./fe_space.md) constructions — a coarse seed (`:89-90`) + one h-refinement level per finer mesh (`:106`) + one p-refinement level per finer collection (`:117`). **A genuine combinator (composes firm `fe_space` + firm `fe_collection`)**, NOT a leaf: its base case is one `fe_space` call (the realization of `fe_space` law 4 / `fe_collection` law 6). The `[Mesh]` input element type cross-links D3's [`build_mesh`](./build_mesh.md) `Mesh` record (reference). Output record `FiniteElementSpaceHierarchy` defined in-chapter (single-consumer → `## Record definition`, NOT a concepts page; `record-FiniteElementSpaceHierarchy-needs-definition-home` flagged for the ≥2-consumer trigger). Five laws (coarse-seed base case, AddLevel-fold structure, coarse-to-fine level-monotonicity, determinism, per-level essential-dof coherence). Firm-on-positive-structure (whole `ConstructFiniteElementSpaceHierarchy` body read; both constituents firm on disk; no-dedicated-`test-multigrid.cpp` caveat non-gating per `fe_space`/`fe_collection`/`fe_assemble` precedent). Lazy prolongation `P[l]` / discrete-interpolator machinery read-as-given (sibling-pull-gated `BuildProlongationAtLevel`/`BuildDiscreteInterpolator` — NOT partly-constructive). L1>L0 `fe-space-hierarchy-construction-rotation` sibling-pull-gated (named, not authored).
```

#### 5b. Update the FE-space sub-spine firm-count narrative header (3 → 4) (line 99)

```edit:book/src/L1/index.md
[old]: **Firm (FE-space sub-spine — 3; opened cycle-064)** — the finite-element **space-construction** surface (the MFEM-equivalent FE-space substrate under every assembled-operator pipeline, in scope per CLAUDE.md mesh/FE), opened cycle-064 by the firm [`fe_space`](./fe_space.md) (cycle-064 D2) + its L1>L0 rotation [`fe-space-construction-rotation`](../L1-L0/fe-space-construction-rotation.md) (cycle-064 D3), extended cycle-065 by its **upstream collection-order-schedule producer** [`fe_collection`](./fe_collection.md) (cycle-065 D2) + its L1>L0 rotation [`fe-collection-construction-rotation`](../L1-L0/fe-collection-construction-rotation.md) (cycle-065 D3), and extended cycle-066 by its **boundary-condition dof-set member** [`essential_dofs`](./essential_dofs.md) (cycle-066 D1) + its L1>L0 rotation [`essential-dofs-construction-rotation`](../L1-L0/essential-dofs-construction-rotation.md) (cycle-066 D2).
[new]: **Firm (FE-space sub-spine — 4; opened cycle-064)** — the finite-element **space-construction** surface (the MFEM-equivalent FE-space substrate under every assembled-operator pipeline, in scope per CLAUDE.md mesh/FE), opened cycle-064 by the firm [`fe_space`](./fe_space.md) (cycle-064 D2) + its L1>L0 rotation [`fe-space-construction-rotation`](../L1-L0/fe-space-construction-rotation.md) (cycle-064 D3), extended cycle-065 by its **upstream collection-order-schedule producer** [`fe_collection`](./fe_collection.md) (cycle-065 D2) + its L1>L0 rotation [`fe-collection-construction-rotation`](../L1-L0/fe-collection-construction-rotation.md) (cycle-065 D3), extended cycle-066 by its **boundary-condition dof-set member** [`essential_dofs`](./essential_dofs.md) (cycle-066 D1) + its L1>L0 rotation [`essential-dofs-construction-rotation`](../L1-L0/essential-dofs-construction-rotation.md) (cycle-066 D2), and extended cycle-117 D4 by the **hierarchy combinator** [`fe_space_hierarchy`](./fe_space_hierarchy.md) — the `AddLevel`-fold over per-level `fe_space` constructions that builds the p-multigrid `FiniteElementSpaceHierarchy` (the first FE-space sub-spine member that is a genuine combinator composing two firm constituents rather than a construction/schedule/marker leaf).
```

#### 5c. Add the dep-map table row (alpha position: after `fe_collection`, before `fe_space`)

```edit:book/src/L1/index.md
[old]: | [`fe_space`](./fe_space.md) | `(mesh: Mesh, collection: FECollection) → FiniteElementSpace[N]` (i.e. the typed FE space; `N = GetTrueVSize()` the global true-dof count) |
[new]: | [`fe_space_hierarchy`](./fe_space_hierarchy.md) | `([Mesh], [FECollection], Config) → FiniteElementSpaceHierarchy` (i.e. the p-multigrid level stack; coarse seed + one level per finer mesh (h) / finer collection (p)) | composes [`fe_space`](./fe_space.md) (firm; per-level construction, seed `multigrid.hpp:89-90`, `AddLevel` `:106`/`:117`) + [`fe_collection`](./fe_collection.md) (firm; the `[FECollection]` schedule folded one-per-level, `fecs[0]` `:90`, `fecs[l]` `:117`); references [`build_mesh`](./build_mesh.md) for the `[Mesh]` element-type `Mesh` record (NOT a dependency); the per-level [`essential_dofs`](./essential_dofs.md) is a consumed hierarchy-application, NOT a dependency | `firm` (FE-space sub-spine **hierarchy combinator**; the `AddLevel`-fold whose base case is one `fe_space` construction — `fe_space` law 4 / `fe_collection` law 6 realization; output record `FiniteElementSpaceHierarchy` defined in-chapter `## Record definition` (single-consumer); L0: whole `ConstructFiniteElementSpaceHierarchy` body `palace/fem/multigrid.hpp:78-126` — `coarse_mesh_l` `:87-88`, seed `:89-90`, optional dbc block `:92-101`, h-loop `:104-112` (`AddLevel` `:106`), p-loop `:115-123` (`AddLevel` `:117`), `return` `:125`; record class `palace/fem/fespace.hpp:200-286` (`fespaces` `:203`, lazy `P` `:204`, `AddLevel` `:217-221`); harvested cycle-117 D4; firm-on-positive-structure, no-dedicated-`test-multigrid.cpp` caveat non-gating per `fe_space`/`fe_collection`/`fe_assemble` precedent; both constituents firm on disk (well-foundedness firm/firm); laws: coarse-seed base case, AddLevel-fold structure, coarse-to-fine level-monotonicity, determinism, per-level essential-dof coherence; lazy prolongation `P[l]`/discrete-interpolator machinery read-as-given sibling-pull-gated `BuildProlongationAtLevel`/`BuildDiscreteInterpolator` — NOT partly-constructive; MPI/Par* out-of-scope single-rank; L1>L0 `fe-space-hierarchy-construction-rotation` sibling-pull-gated named-not-authored) |
| [`fe_space`](./fe_space.md) | `(mesh: Mesh, collection: FECollection) → FiniteElementSpace[N]` (i.e. the typed FE space; `N = GetTrueVSize()` the global true-dof count) |
```

#### 5d. CONSOLIDATED FIRM-COUNT BUMP (count-owner duty)

I am the count-owner for cycle-117's L1 landing cohort. The cohort landing into the
L1 index this cycle (per the dispatch plan): **D3 `build_mesh`** (the `Mesh` record +
mesh-wrapper op — front (iv); lands in a NEW mesh sub-spine grouping, owns its own
row+bullet), **my `fe_space_hierarchy`** (FE-space sub-spine), **D5 de-Rham
interpolator** (FE-space sub-spine; owns its own row+bullet).

**Coordination note (count-owner discipline):** the consolidated grand-total bump
depends on what D3 and D5 actually land (their `## Status` verdicts + whether their
homes are NEW sub-spine groupings vs the FE-space sub-spine). I author the
`fe_space_hierarchy` +1 to the FE-space sub-spine (3 → 4) and the grand total here;
**the integrator must reconcile the final grand total against D3's + D5's
on-disk `## Status` lines** (per the count-discipline: count firm by reading each
linked chapter's `## Status`, NOT the index cells). My local edit below bumps **only
for the firm landings I can confirm this cycle**; D3/D5 firm verdicts fold in at
integrate-time. If D3/D5 land firm, the grand total goes 40 → 43 (build_mesh +
fe_space_hierarchy + interpolator); if either is non-firm, the integrator adjusts.

```edit:book/src/L1/index.md
[old]: **Firm (33 main cohort; 40 firm grand total incl. the FE-assembly + FE-space sub-spines).** The 33 main-cohort firm operators are listed below; the FE-assembly sub-spine adds **4** more firm (`fe_assemble` c054 + `weak_form_term` c061 + `eliminate_essential_bc` + `eliminate_rhs` both c055 — see the §"Firm (FE-assembly sub-spine)" subsection), and the FE-space sub-spine adds **3** more firm (`fe_space` c064 + `fe_collection` c065 + `essential_dofs` c066 — see the §"Firm (FE-space sub-spine)" subsection), bringing the L1 firm grand total to **40**
[new]: **Firm (33 main cohort; 41 firm grand total incl. the FE-assembly + FE-space sub-spines — pending the cycle-117 D3 `build_mesh` + D5 de-Rham-interpolator landings, which the integrator reconciles against their on-disk `## Status`).** The 33 main-cohort firm operators are listed below; the FE-assembly sub-spine adds **4** more firm (`fe_assemble` c054 + `weak_form_term` c061 + `eliminate_essential_bc` + `eliminate_rhs` both c055 — see the §"Firm (FE-assembly sub-spine)" subsection), and the FE-space sub-spine adds **4** more firm (`fe_space` c064 + `fe_collection` c065 + `essential_dofs` c066 + `fe_space_hierarchy` c117 — see the §"Firm (FE-space sub-spine)" subsection), bringing the L1 firm grand total to **41** (cycle-117 D4 added the FE-space sub-spine's 4th firm member `fe_space_hierarchy`, the `AddLevel`-fold hierarchy combinator composing firm `fe_space` + firm `fe_collection`; **count-owner reconciliation note:** the cycle-117 wide wave also lands D3 `build_mesh` (the mesh-wrapper `Mesh` record home — a NEW mesh sub-spine, +1 if firm) and D5 the de-Rham interpolator (FE-space sub-spine, +1 if firm); the integrator folds those into the grand total by reading their on-disk `## Status` lines — if both land firm the grand total is 43)
```

## Supporting evidence

### Operators currently harvested at this layer (relevant slugs)
- `fe_space` (L1, firm c064) — `book/src/L1/fe_space.md` `## Status` line (read this
  cycle): "**firm (firm-on-positive-structure).**" + frontmatter `rank: firm`. The
  per-level construction this fold composes.
- `fe_collection` (L1, firm c065) — `book/src/L1/fe_collection.md` `## Status` line
  (read this cycle): "**firm (firm-on-positive-structure).**" + frontmatter `rank:
  firm`. The `[FECollection]` schedule producer this fold folds over.
- `essential_dofs` (L1, firm c066) — the per-level dof-set marker (consumed
  hierarchy-application, not a dependency).
- `build_mesh` (L1, D3 this cycle) — the `Mesh` record home the `[Mesh]` element
  type cross-links (reference). Per the prompt, D3 lands it CANONICAL `L1/build_mesh`;
  the per-report integrator applies D3 before D4 so the live link resolves.

### Citations self-verified against source (on-disk reads this cycle)
All `palace/fem/multigrid.hpp:78-126` line numbers confirmed by direct on-disk
`grep -n` read (NOT codemap line indexing — the codemap +1 brace-boundary drift
rule): seed `:89-90`, dbc block `:92-101` (`AttrToMarker` `:98`,
`GetEssentialTrueDofs` `:99-100`), h-loop `AddLevel` `:106`, p-loop `AddLevel`
`:117`, `return fespaces` `:125`, close brace `}` `:126`. The record class
`palace/fem/fespace.hpp:200-286` confirmed on-disk: `class
FiniteElementSpaceHierarchy` `:200`, `fespaces` `:203`, `P` `:204`, `AddLevel`
`:217-221`, close brace `:286`.

### Mesh cross-link
`[Mesh]` input element type → [`build_mesh`](./build_mesh.md) `Mesh` record
(D3 this cycle). Wired as a `reference` edge (navigational element-type-home
pointer), NOT a `depends-on` — the fold consumes already-constructed meshes; it does
not invoke `build_mesh`. Per the prompt, the live link resolves because the
per-report integrator applies D3 before D4.

## Open questions / caveats

- **`record-FiniteElementSpaceHierarchy-needs-definition-home`** — `FiniteElementSpaceHierarchy`
  is currently single-consumer (only `fe_space_hierarchy` names it), so it gets an
  in-chapter `## Record definition` section (authored here), NOT a standalone
  `concepts/` page. **TRIGGER for promotion to a `concepts/<record>.md` page:** when a
  2nd consumer surfaces — most likely a geometric-multigrid L1 operator (the
  preconditioner that relaxes over the hierarchy levels via `GetProlongationOperators`
  / `GetFESpaceAtLevel`) — the record crosses the ≥2-consumer bar and the in-chapter
  section should be lifted to `book/src/concepts/finite-element-space-hierarchy.md`.
- **`fe-space-hierarchy-construction-rotation` L1>L0 theme deferred** — the lowering
  theme is sibling-pull-gated (named in §Downward, not authored). It is a clean
  fold→imperative-loop rotation when an L1>L0 dispatch pulls it; no obstruction
  expected (the body is a deterministic `push_back`/`AddLevel` fold).
- **Count-owner reconciliation** — the L1 grand-total edit (5d) bumps to **41** for my
  confirmed `fe_space_hierarchy` landing and annotates the pending D3 `build_mesh` +
  D5 interpolator landings (→ 43 if both firm). The integrator must reconcile the
  final grand total against D3's + D5's on-disk `## Status` lines per the
  count-discipline (read each chapter's `## Status`, not the index cells). D3 lands a
  NEW mesh sub-spine grouping (its own SUMMARY block + group intro — owned by D3, not
  me); if a NEW mesh sub-spine grouping appears, the grand-total narrative should name
  it alongside the FE-assembly + FE-space sub-spines.
- **`BuildProlongationAtLevel` / `BuildDiscreteInterpolator` still sibling-pull-gated**
  — the multigrid-transfer + de-Rham-interpolator machinery is read-as-given here as a
  property of the result record. D5 this cycle lands the de-Rham interpolator front;
  if D5's interpolator op wants `fe_space_hierarchy` as a constituent (it consumes
  `GetDiscreteInterpolators`), that is a D5-side `depends-on` edge to add at D5's
  authoring, NOT an edit to this chapter (down-links are read-only; routed as this OQ).
