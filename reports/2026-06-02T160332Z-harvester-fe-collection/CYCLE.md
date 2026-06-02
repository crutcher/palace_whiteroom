---
agent: harvester
invoked_at: 2026-06-02T160332Z
scope: L1 operator: fe_collection
status: integrated
integrated_at: 2026-06-02T190000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-065 (D2). NEW firm book/src/L1/fe_collection.md (p-multigrid FE-collection order schedule; mat_lor: Bool param per repair) + L1/index.md dep-map row + FE-space sub-spine cohort bullet + SUMMARY chapter line. Build-relevant; cargo make book exit 0. L1 firm 32->33; FE-space sub-spine 1->2. 1 OQ promoted (multigrid-hpp-template-close-line-citation-hygiene). No gate hits."
inputs:
  - reference/palace/palace/fem/multigrid.hpp:22-73 (ConstructFECollections — the order schedule)
  - reference/palace/palace/utils/labels.hpp:114-119 (MultigridCoarsening enum)
  - reference/palace/palace/utils/configfile.hpp:918 (mg_coarsening default = LOGARITHMIC)
  - book/src/L1/fe_space.md (the sibling FE-space-construction entry; defers fe_collection as a separate construction)
  - book/src/L1/index.md §"Firm (FE-space sub-spine — 1; opened cycle-064)" §"Deferred follow-on siblings" (the c064 D1 borderline-second-entry flag)
  - c065 planner dispatch (structure finding: family-pmin floor, basis selection, arity-3/4 ctor, LINEAR/LOGARITHMIC coarsening, finest↔coarsest reverse)
  - D3 (sibling): book/src/L1-L0/fe-collection-construction-rotation.md (gated on this warrant=YES; forward-referenced)
---

# CYCLE: Formalize fe_collection at L1

## Summary

WARRANT VERDICT: **YES — genuine self-standing L1 entry.** `ConstructFECollections`
(`palace/fem/multigrid.hpp:22-73`) is a **list-producing p-multigrid order schedule**
`(p, dim, mg_max_levels, coarsening, family) → [FECollection]`, NOT a thin `fe_space` rename. It
carries laws `fe_space` does not have — a deterministic finest-to-coarsest order sequence under a
named coarsening policy, a family-dependent `pmin` floor that bounds the sequence, and a
`mg_max_levels`-bounded length — and its codomain is a *list* of `FECollection`s, exactly the
collection inputs that `ConstructFiniteElementSpaceHierarchy` (`:78-126`) feeds one-per-level into
`fe_space` constructions (`AddLevel`, `:106`/`:117`). The schedule and the per-level space
construction are two distinct operations on opposite sides of the `[FECollection]` boundary; the
collection schedule is upstream of `fe_space`, not a variant axis of it. This is consistent with the
`fe_space` author's own framing (`book/src/L1/fe_space.md:84-90`), which treats `ConstructFECollections`
as a *separate construction that produces the `collection` input(s)* and explicitly defers it.

Authored `book/src/L1/fe_collection.md` as **firm (firm-on-positive-structure)** — every law is a
syntactic identity / loop-invariant on fully-specified positive source (the `ConstructFECollections`
body is read in full, `:22-73`), so the absence of a dedicated `test-multigrid.cpp` does not gate firm
(the `fe_space`/`fe_assemble`/`apply_linop` no-dedicated-test precedent). Signature, three variant axes
(de-Rham family, coarsening policy, LOR basis), the relationship to `fe_space`, the L1>L0 forward-ref to
D3's `fe-collection-construction-rotation`, and the index dual-registration row + FE-space-sub-spine
cohort bullet are all proposed below. The consolidated tally is DEFERRED to D4 (count-owner this cycle).

MPI/`Par*`/partitioning flagged once: out of scope — `ConstructFECollections` is rank-agnostic (it
builds `FECollection` template objects, not partitioned spaces); the per-rank distribution enters only
downstream at `ConstructFiniteElementSpaceHierarchy`'s `mfem::ParFiniteElementSpace` wrapping, read
single-rank.

## Proposed changes

```new:book/src/L1/fe_collection.md
---
status: firm
harvested_by: harvester:2026-06-02T160332Z-harvester-fe-collection
cycle: cycle-065
---

# `fe_collection` — FE-collection p-multigrid order schedule

`fe_collection :: (p: Order, dim: Dim, mg_max_levels: Nat, coarsening: CoarseningPolicy, mat_lor: Bool, family: DeRhamFamily) -> [FECollection]`

Produce the **finest-to-coarsest list of finite-element collections** that seeds a geometric
p-multigrid hierarchy: starting from the finest order `p`, emit one `FECollection` per multigrid level,
coarsening the order by the `coarsening` policy down to the family-dependent floor `pmin`, then reverse
to coarsest-first. This is the **collection-schedule** operator — the upstream producer of the
`[FECollection]` whose entries `ConstructFiniteElementSpaceHierarchy` feeds one-per-level into
[`fe_space`](./fe_space.md) constructions. The de-Rham family selects the `FECollection` subclass and
sets `pmin`; the coarsening policy (`LINEAR`/`LOGARITHMIC`) sets the order step; the LOR flag selects the
order-coarsened basis type.

## Context

L1 is the mutation-rotation layer: source operations re-expressed as pure functions. `fe_collection` is
the **list-producing-schedule** view of that rotation — Palace's `ConstructFECollections` builds a
`std::vector<std::unique_ptr<FECollection>>` once before the multigrid solve and thereafter consumes it
read-only; the L1 form names the pure `(p, dim, mg_max_levels, coarsening, family) → [FECollection]`
schedule and treats the produced list as an immutable value sequence.

At L0 the schedule is the function template `ConstructFECollections<FECollection>(int p, int dim, int
mg_max_levels, MultigridCoarsening mg_coarsening, bool mat_lor)`
(`palace/fem/multigrid.hpp:23-26`). Its body is a single bounded loop (`:44-69`) that `push_back`es one
`std::make_unique<FECollection>(...)` per level (`:49`/`:53`), decrements/halves the order per the
coarsening switch (`:60-68`), breaks at the floor `p == pmin` (`:56-59`), and finally
`std::reverse`s the accumulated list (`:70`) so the returned vector runs coarsest-to-finest. The result
is **a list of collections**, not a single collection — that list cardinality (one per multigrid level)
is exactly what distinguishes this operator from [`fe_space`](./fe_space.md) (which consumes ONE
`FECollection` to build ONE space). `ConstructFiniteElementSpaceHierarchy` (`:78-126`) is the consumer
that pairs the list entries with meshes: its coarse seed uses `fecs[0]` (`:90`) and its p-refinement
loop `AddLevel`s a [`fe_space`](./fe_space.md) per `fecs[l]` (`:117`).

This chapter is defined in L1 vocabulary (the typed `(p, dim, mg_max_levels, coarsening, family) →
[FECollection]` schedule). The forward rewrite into the L0 `ConstructFECollections` loop + the
`std::reverse` is the L1>L0 theme `fe-collection-construction-rotation` (authored cycle-065 D3;
forward-reference `fe-collection-construction-rotation` until on disk).

## Signature

    fe_collection :: (p: Order, dim: Dim, mg_max_levels: Nat, coarsening: CoarseningPolicy, mat_lor: Bool, family: DeRhamFamily) -> [FECollection]

Shape contract (bunsen-style, named axes):

- `p` — `Order` — the **finest** polynomial order; the head of the produced order sequence. Must
  satisfy `p >= pmin` (the L0 `MFEM_VERIFY(p >= pmin, ...)`, `multigrid.hpp:34`); `pmin` is set by
  `family` (see *Variant axis: de-Rham family*).
- `dim` — `Dim` — the spatial dimension, forwarded verbatim into every `FECollection` constructor
  (`multigrid.hpp:49`/`:53`). It is constant across the list (only the order varies).
- `mg_max_levels` — `Nat` — the p-multigrid level cap; the produced list has length
  `min(L_floor, max(1, mg_max_levels))`, where `L_floor` is the number of distinct orders the
  coarsening policy visits from `p` down to `pmin` inclusive (the loop runs at most `max(1,
  mg_max_levels)` iterations, `multigrid.hpp:44`, breaking early at `p == pmin`, `:56-59`).
- `coarsening` — `CoarseningPolicy` — `LINEAR | LOGARITHMIC`; the order-step rule (see *Variant axis:
  coarsening policy*). The L0 `MultigridCoarsening` enum (`palace/utils/labels.hpp:114-119`); default
  `LOGARITHMIC` (`palace/utils/configfile.hpp:918`).
- `mat_lor` — `Bool` — the LOR-preconditioner basis flag (the L0 runtime 5th argument,
  `multigrid.hpp:26`); selects the second basis type `b2` (`GaussLegendre` normally,
  `IntegratedGLL` when set, `:35-39`) for the vector (ND/RT) faces (see *Variant axis: LOR basis
  selection*). Inert for the H1/L2 (3-arg ctor) faces.
- `family` — `DeRhamFamily` — selects the `FECollection` subclass produced (the template parameter
  `FECollection`) AND the floor `pmin` AND the constructor arity (see *Variant axis: de-Rham family*).
- result — `[FECollection]` — the **coarsest-to-finest** list of collections; `result[last]` is the
  order-`p` finest collection, `result[0]` the order-`pmin` (or shallowest-coarsened) coarsest. Length
  is the bounded level count above. Each entry is an immutable `FECollection` value of the same
  `family` subclass and `dim`, differing only in order.

The **list cardinality** (one collection per multigrid level) is the load-bearing output that
separates this operator from [`fe_space`](./fe_space.md): `fe_collection` produces the *sequence* of
collection inputs; `fe_space` consumes *one* of them.

## Variant axis: de-Rham family

The `family` argument is the L0 template parameter `FECollection` of `ConstructFECollections`; it
selects three coupled things:

| Family | Collection type | `pmin` | ctor arity |
|---|---|---|---|
| H1 (nodal scalar) | `H1_FECollection` | 1 | 3-arg `(p, dim, b1)` |
| H(curl) (Nédélec) | `ND_FECollection` | 1 | 4-arg `(p, dim, b1, b2)` |
| H(div) (Raviart–Thomas) | `RT_FECollection` | 0 | 4-arg `(p, dim, b1, b2)` |
| L2 (discontinuous) | `L2_FECollection` | 0 | 3-arg `(p, dim, b1)` |

- **`pmin` floor** — `pmin = 1` for `H1_FECollection`/`ND_FECollection`, else `0`
  (`multigrid.hpp:30-34`, the `std::is_base_of<...>::value ? 1 : 0` `constexpr`). H1/ND require a
  minimum order ≥ 1 (a constant nodal scalar / lowest Nédélec edge); RT/L2 admit order 0. The floor
  bounds the coarsening sequence's tail.
- **Constructor arity** — `ND_FECollection`/`RT_FECollection` (the vector de-Rham faces) take the
  4-argument `(p, dim, b1, b2)` ctor (`multigrid.hpp:46-50`); `H1_FECollection`/`L2_FECollection` take
  the 3-argument `(p, dim, b1)` ctor (`:51-55`, with `MFEM_CONTRACT_VAR(b2)` marking `b2` unused).
  This is the `if constexpr (std::is_base_of<ND...> || std::is_base_of<RT...>)` branch (`:46-47`).

The family is selected at the construction call sites the same way [`fe_space`](./fe_space.md)'s family
is — the ND/H1/RT (and 2-D L2-curl) collection lists are built per de-Rham face upstream of the
`ConstructFiniteElementSpaceHierarchy<...>` calls (`palace/models/spaceoperator.cpp:47/49/51`).

## Variant axis: coarsening policy

The `coarsening` argument is the L0 `MultigridCoarsening` enum (`palace/utils/labels.hpp:114-119`),
switched at `multigrid.hpp:60-68`:

- **`LINEAR`** — `p--` per level (`multigrid.hpp:62-64`): the order sequence is `p, p-1, p-2, ..., pmin`
  (arithmetic descent). Produces up to `p - pmin + 1` distinct levels.
- **`LOGARITHMIC`** — `p = (p + pmin) / 2` per level (`multigrid.hpp:65-67`, integer division): the
  order sequence halves the gap to the floor each level, `p, ⌊(p+pmin)/2⌋, ...` — far fewer levels for
  large `p`. The Palace default (`palace/utils/configfile.hpp:918`).

The policy changes ONLY the order sequence (hence the list length); it does not change the per-entry
collection construction. This is the load-bearing schedule axis that `fe_space` has no analog for.

## Variant axis: LOR basis selection

The `mat_lor` flag (the LOR-preconditioner indicator) selects the **second basis type** `b2` for the
vector (ND/RT) faces: `b1 = GaussLobatto` always; `b2 = GaussLegendre` normally, but
`b2 = IntegratedGLL` when `mat_lor` (`multigrid.hpp:35-39`). For H1/L2 (3-arg ctor) `b2` is unused
(`MFEM_CONTRACT_VAR(b2)`, `:54`), so the LOR axis is inert for the scalar/discontinuous faces. This is
a *basis-type* refinement of the produced collections, not a schedule-length change — it is the
construction-time basis the downstream LOR preconditioner needs.

## Algebraic laws

The laws are syntactic identities / loop-invariants on the positive `ConstructFECollections` body
(no convergence/iteration semantics — the schedule is a deterministic finite enumeration):

1. **Finest-head, coarsest-first determinism.** Given fixed `(p, dim, mg_max_levels, coarsening,
   family)`, the produced list is a pure deterministic function — same inputs ⟹ same list (same length,
   same per-entry orders). After the terminal `std::reverse` (`multigrid.hpp:70`) the list runs
   coarsest-to-finest: `result[last]` carries order `p`, `result[0]` carries the coarsest visited
   order. (The loop builds finest-to-coarsest, `:41-42` comment + `:44-69`, then reverses.)
2. **Family-determined floor.** The coarsening sequence terminates at `p == pmin`
   (`multigrid.hpp:56-59`), and `pmin` is a pure function of `family` (1 for H1/ND, 0 for RT/L2,
   `:30-33`). The order sequence never descends below the family floor; `p >= pmin` is a precondition
   (`MFEM_VERIFY`, `:34`) — supplying `p < pmin` is a contract violation, not a law branch.
3. **Length-bounded by `mg_max_levels`.** The list length is `min(L_policy, max(1, mg_max_levels))`,
   where `L_policy` is the number of distinct orders `coarsening` visits from `p` to `pmin` inclusive.
   `max(1, mg_max_levels)` is the loop cap (`:44`); the early `break` at the floor (`:56-59`) caps it
   below `L_policy` when the policy reaches `pmin` first. Length is always `>= 1` (the `max(1, ·)`
   guarantees at least the finest collection even when `mg_max_levels <= 0`).
4. **Coarsening determines order step only.** Switching `coarsening` between `LINEAR` and
   `LOGARITHMIC` (`:60-68`) changes ONLY the interior order sequence (hence list length); it does NOT
   change the per-entry `FECollection` subclass, `dim`, or basis types. The two policies share the same
   head (order `p`) and the same floor (`pmin`).
5. **Per-entry family/basis uniformity.** Every entry of the produced list is the same `family`
   subclass with the same `dim` and the same basis types `(b1, b2)` (`:49`/`:53`) — only the order
   differs entry-to-entry. The basis selection (law-inert LOR axis, `:35-39`) is constant across the
   list.
6. **Singleton degeneracy is one `fe_space` input.** When the schedule produces a length-1 list
   (`p == pmin` at entry, or `mg_max_levels <= 1`), the result is a single `FECollection` — exactly one
   [`fe_space`](./fe_space.md) collection input. This is the boundary at which `fe_collection` ∘
   per-level `fe_space` collapses to a single `fe_space` construction (the `fe_space` coarse-seed
   identity, `book/src/L1/fe_space.md` law 4).

**Non-law (MFEM-owned).** `fe_collection` does NOT define the internal basis/dof structure of the
`FECollection` objects it produces — the `H1_/ND_/RT_/L2_FECollection` classes are MFEM's; this operator
only *schedules the orders* and *selects the subclass + basis types*. No L1 law constrains the
collections' internal node placement.

## Dependencies

(leaf at L1 — the schedule is a pure enumeration producing a list of `FECollection` values; no other L1
operator is invoked). The produced list is **consumed by** [`fe_space`](./fe_space.md): each entry is a
`collection` argument to a per-level `fe_space(mesh, collection)` construction inside
`ConstructFiniteElementSpaceHierarchy` (`multigrid.hpp:90`/`:117`). That is a consumed-by relation
(producer→consumer across the `[FECollection]` boundary), not a dependency. `fe_collection` is upstream
of `fe_space`, which is in turn upstream of the FE-assembly sub-spine.

## Downward (to L0)

The L1>L0 rotation `fe-collection-construction-rotation` (cycle-065 D3) narrates how the typed
`(p, dim, mg_max_levels, coarsening, family) → [FECollection]` schedule rewrites into the L0
`ConstructFECollections` template (`multigrid.hpp:22-73`): the `pmin` `constexpr`
(`:30-33`), the basis-type selection (`:35-39`), the bounded `push_back` loop with the
arity-3/4 ctor branch (`:44-55`), the coarsening switch (`:60-68`), and the terminal `std::reverse`
(`:70`). (Forward-reference `fe-collection-construction-rotation` until that theme is on disk.)

## Status

**firm (firm-on-positive-structure).** The schedule is read in full from a single positive source site:
the entire `ConstructFECollections` template body (`palace/fem/multigrid.hpp:22-73`). All three variant
axes are positively witnessed — the de-Rham family + `pmin` + ctor-arity coupling
(`:30-34,46-55`), the `LINEAR`/`LOGARITHMIC` coarsening switch (`:60-68`, enum at
`palace/utils/labels.hpp:114-119`, default at `palace/utils/configfile.hpp:918`), and the LOR basis
selection (`:35-39`). Every law is a syntactic identity / loop-invariant on this positive structure —
there is no convergence/iteration semantics to test-gate, so the absence of a dedicated
`test-multigrid.cpp` exercising `ConstructFECollections` does not gate firm (the
[`fe_space`](./fe_space.md) cycle-064 / [`fe_assemble`](./fe_assemble.md) cycle-054 / `apply_linop`
no-dedicated-test precedent). The internal basis/dof structure of the produced `FECollection`s is
explicitly MFEM-owned-read-as-given, not L1 law substrate.

This is the **upstream producer** of the FE-space-construction sub-spine: it schedules the
`[FECollection]` list that the geometric-multigrid hierarchy feeds one-per-level into
[`fe_space`](./fe_space.md) constructions. Warrant: it earns its own entry (not a `fe_space`
variant-axis note) on the strength of its list-producing schedule laws (1, 3, 4, 6) — the p-multigrid
order sequence, the level-count bound, the policy-determines-order-step fact, and the singleton-collapse
boundary — none of which `fe_space` (a single-collection→single-space construction) carries.

**MPI / `Par*` out of scope (flagged once):** `ConstructFECollections` is rank-agnostic — it builds
`FECollection` template objects, not partitioned spaces. The per-rank distribution enters only
downstream when `ConstructFiniteElementSpaceHierarchy` wraps each collection into an
`mfem::ParFiniteElementSpace` (read single-rank, per the existing `par-types-single-rank-reading` rule).

**Deferred follow-on siblings (named, NOT authored this cycle):** `fe_space_hierarchy` (the h/p
multigrid stack `ConstructFiniteElementSpaceHierarchy`, `multigrid.hpp:78-126` — the consumer that
pairs this schedule's `[FECollection]` with meshes), and `essential_dofs` (the
boundary-attribute-marker → essential-true-dof extraction `multigrid.hpp:97-99`). Both are named in the
[`fe_space`](./fe_space.md) deferred-sibling list.

## Evidence

- `palace/fem/multigrid.hpp:22-73` — `ConstructFECollections<FECollection>(int p, int dim, int
  mg_max_levels, MultigridCoarsening mg_coarsening, bool mat_lor)`: the whole schedule. The signature
  (`:23-26`); the family `pmin` `constexpr` + `MFEM_VERIFY(p >= pmin, ...)` (`:30-34`); the
  GaussLobatto/GaussLegendre/IntegratedGLL basis selection (`:35-39`); the bounded `push_back` loop
  (`:44-69`) with the ND/RT 4-arg vs H1/L2 3-arg ctor branch (`:46-55`); the early floor `break`
  (`:56-59`); the `LINEAR` (`p--`) / `LOGARITHMIC` (`p = (p+pmin)/2`) coarsening switch (`:60-68`);
  the terminal `std::reverse(fecs.begin(), fecs.end())` (`:70`); the returned vector (`:72`).
- `palace/utils/labels.hpp:114-119` — `enum class MultigridCoarsening : char { LINEAR, LOGARITHMIC }`,
  the coarsening-policy variant axis.
- `palace/utils/configfile.hpp:918` — `MultigridCoarsening mg_coarsening = MultigridCoarsening::LOGARITHMIC`,
  the default coarsening policy (logarithmic).
- `palace/fem/multigrid.hpp:78-126` — `ConstructFiniteElementSpaceHierarchy`: the consumer that pairs
  the schedule's list entries with meshes; coarse seed uses `fecs[0]` (`:90`), p-refinement loop
  `AddLevel`s a space per `fecs[l]` (`:115-117`) — the producer→consumer relation across the
  `[FECollection]` boundary.
- `palace/models/spaceoperator.cpp:47/49/51` — the ND/H1/RT `ConstructFiniteElementSpaceHierarchy<...>`
  call sites (the de-Rham family selection point, shared with [`fe_space`](./fe_space.md)).
- `book/src/L1/fe_space.md:84-90` — the sibling FE-space entry's own framing of `ConstructFECollections`
  as a *separate construction that produces the `collection` input(s)*, deferring it (the warrant
  rationale: the `fe_space` author treated the order-schedule as a distinct operation, not a `fe_space`
  variant).
```

```edit:book/src/L1/index.md
- `fe_collection` *(rough-in; no anchor yet)* — the FE-collection order schedule `(p, dim, mg_max_levels, coarsening, family) → [FECollection]` (`ConstructFECollections`, `palace/fem/multigrid.hpp:22-75`). The order-*schedule* (pmin floor, GaussLobatto/Legendre + LOR basis selection, LINEAR/LOGARITHMIC coarsening) is borderline-second-entry: fold-first as `fe_space`'s collection-input variant axis, split only if its self-standing laws justify a chapter (D1 §3).
- [`fe_collection`](./fe_collection.md) **is now FIRM** *(cycle-065 D2)* — the FE-collection p-multigrid order schedule `(p, dim, mg_max_levels, coarsening, mat_lor, family) → [FECollection]` (`ConstructFECollections`, `palace/fem/multigrid.hpp:22-73`). **WARRANT=YES (genuine self-standing entry, NOT a `fe_space` variant-axis note):** it is a **list-producing schedule** whose codomain is a *list* of collections (one per multigrid level), carrying schedule laws `fe_space` lacks — the finest-to-coarsest order sequence, the family-dependent `pmin` floor, the `mg_max_levels` length bound, the LINEAR/LOGARITHMIC policy-determines-order-step fact, and the singleton-collapse-to-one-`fe_space`-input boundary. Three variant axes: de-Rham family (selects `FECollection` subclass + `pmin` + ctor arity), coarsening policy (`LINEAR` `p--` / `LOGARITHMIC` `p=(p+pmin)/2`), LOR basis (`mat_lor` flag selects `b2` = `GaussLegendre`/`IntegratedGLL`, inert for H1/L2). The **upstream producer** of the FE-space sub-spine: schedules the `[FECollection]` that `ConstructFiniteElementSpaceHierarchy` (`:78-126`) feeds one-per-level into [`fe_space`](./fe_space.md) constructions. Firm-on-positive-structure (whole `ConstructFECollections` body read; no-dedicated-`test-multigrid.cpp` caveat non-gating per `fe_space`/`fe_assemble` precedent). L1>L0: `fe-collection-construction-rotation` (cycle-065 D3).
```

```edit:book/src/L1/index.md
| [`fe_space`](./fe_space.md) | `(mesh: Mesh, collection: FECollection) → FiniteElementSpace[N]` (i.e. the typed FE space; `N = GetTrueVSize()` the global true-dof count) | (leaf; the construction pairs a `Mesh` with an `FECollection` and produces an immutable typed value; consumed-by [`fe_assemble`](./fe_assemble.md)/[`weak_form_term`](./weak_form_term.md)/[`eliminate_essential_bc`](./eliminate_essential_bc.md)/[`eliminate_rhs`](./eliminate_rhs.md) — those are consumed-by relations, NOT dependencies; the dof-numbering/ordering/conformity/prolongation-restriction internals are MFEM-owned-read-as-given) | `firm` (FE-space-construction front prime entry; the shared substrate under all 5 solver pipelines; **de-Rham family variant axis** H1/H(curl)/H(div)/L2 ↔ `H1_/ND_/RT_/L2_FECollection`, all 4 witnessed at construction sites `palace/models/spaceoperator.cpp:47/49/51` (ND/H1/RT) + `:72-75` (2-D L2-curl); L0: variadic ctor `palace/fem/fespace.hpp:67-75` forwarding into `mfem::ParFiniteElementSpace`, `GetTrueVSize` `:96`, MFEM-forwarders `:93-103`; coarse-seed `palace/fem/multigrid.hpp:89-90` inside `ConstructFiniteElementSpaceHierarchy` `:78-126`; harvested cycle-064; clean-gate PROMOTE; firm-on-positive-structure, no-dedicated-test caveat non-gating per `fe_assemble`/`apply_linop` precedent; laws: true-dof-axis determinism, family-selection-by-collection-type, mesh/collection separability, coarse-seed identity; NO `dof_map` mirror (MFEM-owned-read-as-given dof structure = identity-in-named-terms smell); opaque-parameter fan-out re-anchors `fe_assemble`/`weak_form_term`/`eliminate_essential_bc`/`eliminate_rhs` in a later replace-and-propagate pass; deferred siblings `fe_collection`/`essential_dofs`/`fe_space_hierarchy` named-not-authored; L1>L0: `fe-space-construction-rotation` cycle-064 D3) |
| [`fe_collection`](./fe_collection.md) | `(p: Order, dim: Dim, mg_max_levels: Nat, coarsening: CoarseningPolicy, mat_lor: Bool, family: DeRhamFamily) → [FECollection]` (i.e. the finest-to-coarsest p-multigrid collection-order schedule; coarsest-first after reverse) | (leaf; pure list-producing enumeration; **produces** the `[FECollection]` whose entries are per-level `collection` inputs to [`fe_space`](./fe_space.md) inside `ConstructFiniteElementSpaceHierarchy` `palace/fem/multigrid.hpp:90,117` — a producer→consumer relation across the `[FECollection]` boundary, NOT a dependency; the produced collections' internal basis/dof structure is MFEM-owned-read-as-given) | `firm` (FE-space sub-spine upstream collection-schedule producer; **WARRANT=YES self-standing entry** — list-producing schedule, not a `fe_space` variant-axis note; **three variant axes**: de-Rham family (`H1_/ND_/RT_/L2_FECollection` ↔ `pmin` 1/1/0/0 + ctor arity 3/4), coarsening policy (`LINEAR` `p--` / `LOGARITHMIC` `p=(p+pmin)/2`, default LOGARITHMIC `palace/utils/configfile.hpp:918`), LOR basis (`b2` GaussLegendre/IntegratedGLL, inert for H1/L2); L0: whole `ConstructFECollections` body `palace/fem/multigrid.hpp:22-73` — `pmin` constexpr `:30-34`, basis selection `:35-39`, arity-3/4 ctor branch `:46-55`, coarsening switch `:60-68`, terminal `std::reverse` `:70`; enum `palace/utils/labels.hpp:114-119`; harvested cycle-065; firm-on-positive-structure, no-dedicated-`test-multigrid.cpp` caveat non-gating per `fe_space`/`fe_assemble` precedent; laws: finest-head/coarsest-first determinism, family-determined floor, length-bounded-by-`mg_max_levels`, coarsening-determines-order-step-only, per-entry family/basis uniformity, singleton-collapse-to-one-`fe_space`-input; upstream producer of the FE-space sub-spine; L1>L0: `fe-collection-construction-rotation` cycle-065 D3) |
```

```edit:book/src/SUMMARY.md
- [fe_space](./L1/fe_space.md)
- [fe_collection](./L1/fe_collection.md)
```

## Operator content

(The full firm chapter body is authored inside the `new:book/src/L1/fe_collection.md` block above —
slug `fe_collection`, signature `(p, dim, mg_max_levels, coarsening, family) → [FECollection]`, three
variant axes, six algebraic laws, leaf-with-producer-consumer-to-`fe_space`, status firm, evidence.)

## Supporting evidence

- The warrant rationale rests on the codomain distinction: `ConstructFECollections` returns
  `std::vector<std::unique_ptr<FECollection>>` (`multigrid.hpp:24,43,72`) — a *list* — whereas
  `fe_space` consumes one `FECollection`. The list cardinality (one per multigrid level), the order
  sequence, and the policy/floor that determine it are the self-standing schedule structure.
- All citations self-verified against the on-disk file
  `reference/palace/palace/fem/multigrid.hpp` via `tools/citecheck/citecheck.py --anchor`
  (ConstructFECollections@25, pmin@30/34, BasisType@35/38, make_unique-ctor-branch@49/53,
  mg_coarsening-switch@60, LOGARITHMIC@65, reverse@70, ConstructFiniteElementSpaceHierarchy@78) and
  `palace/utils/labels.hpp` (MultigridCoarsening@115) + `palace/utils/configfile.hpp` (LOGARITHMIC@918).
  The planner's on-disk verification that the template closes at `:73` (not codemap's `:75`) is
  confirmed — the closing `}` is at on-disk line 73; the old deferred-sibling row's `:22-75` is
  corrected to `:22-73` in the cohort-bullet edit.

## Open questions / caveats

- **Index consolidated tally DEFERRED to D4 (count-owner this cycle).** This report registers only its
  OWN dep-map row (the `fe_collection` table row) + its OWN FE-space-sub-spine cohort bullet. The
  consolidated FE-space-sub-spine running count ("Firm (FE-space sub-spine — 1; opened cycle-064)" →
  should become 2 after this lands) and the L1 firm grand total (32 → 33) are NOT touched here — D4
  owns the cohort-summing tally + the sub-spine header count update + the §"Vocabulary cohort"
  grand-total prose. If D4 is not in fact the count-owner this cycle, integrator-finalize should
  reconcile the header count (`Firm (FE-space sub-spine — 1` → `2`) and the grand total.
- **Stale `:22-75` in the existing deferred-sibling bullet** — the cohort-bullet edit replaces the old
  plain-text `fe_collection` deferred-sibling bullet (which cited `multigrid.hpp:22-75`) with the firm
  bullet citing the verified `:22-73`. The `fe_space.md:84,203` in-prose references to `multigrid.hpp:22-72`
  are likewise off-by-one/two on the close (the body ends at `:72` `return`, `}` at `:73`); those are in
  the already-firm `fe_space.md` and are NOT in this dispatch's write-scope — flagged for a later
  citation-hygiene pass (a change to propose, not to apply here).
- **`fe_space_hierarchy` consumer pull** — this entry's producer→consumer relation makes the
  `fe_space_hierarchy` sibling (`ConstructFiniteElementSpaceHierarchy`, `multigrid.hpp:78-126`) the
  natural next pull: it is the operator that *pairs* this schedule's `[FECollection]` with the mesh
  sequence. Named, not authored (per the `fe_space` deferred-sibling list); lower fan-out for the
  assembly front (the geometric-multigrid preconditioner consumes it, not the assembled-operator
  pipeline).
