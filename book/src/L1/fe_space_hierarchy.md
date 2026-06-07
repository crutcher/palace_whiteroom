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
    - target: L1-L0/fe-space-hierarchy-construction-rotation
      kind: lowers-to             # the L1>L0 forward-rewrite theme for this AddLevel-fold (D2 this cycle)
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
