---
status: firm
harvested_by: harvester:2026-06-02T160332Z-harvester-fe-collection
cycle: cycle-065
# Graded-stack scheme (cycle-115 D2 hygiene; chapter previously carried only `status: firm`,
# NO typed edges — the rank was prose-inferred from `## Status`). This firm L1 schedule operator
# is a leaf in L1 vocabulary (a pure enumeration producing a `[FECollection]` list; no L1 op is
# invoked — §Dependencies), so it carries no `composes` edge. It rests on its positive L0 source
# (the whole `ConstructFECollections` template body, cites-evidence, rank-terminal ground truth)
# and lowers through its L1>L0 construction-rotation theme. The producer->consumer relation to
# `fe_space` (which consumes one of the produced collections) is navigational, NOT a dependency
# (§Dependencies: "a consumed-by relation ... not a dependency") -> `reference`.
# Well-foundedness rank(u) <= rank(v): this node firm (rank 3); the cites-evidence target is
# rank-terminal L0 ground truth; the lowering theme `fe-collection-construction-rotation` is
# typed `rank: firm` (this cycle, D2) so 3 <= 3 holds.
rank: firm
edges:
  depends-on:
    - target: palace/fem/multigrid.hpp:22-73
      kind: cites-evidence        # ConstructFECollections<FECollection> whole template body; close brace verified on disk at :73 (return fecs; at :72, } at :73)
    - target: L1-L0/fe-collection-construction-rotation
      kind: lowers-to             # the L1>L0 construction-rotation theme (cycle-065 D3; §Downward :175-180)
  reference:
    - L1/fe_space                  # producer->consumer: each produced FECollection is a per-level fe_space input (§Dependencies; NOT a depends-on)
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
