---
layer: L1
operator: essential_dofs
firmness: firm
rank: firm
edges:
  depends-on:
    - target: L1-L0/essential-dofs-construction-rotation
      kind: lowers-to             # the L1>L0 construction-rotation home
  reference:
    - L1/fe_space                 # the FiniteElementSpace[N] the DofSet is built over
    - L1/eliminate_essential_bc   # consumer of the DofSet[N]
    - L1/eliminate_rhs            # consumer of the DofSet[N]
variant_axes:
  - attribute-wildcard
  - per-level-hierarchy-application
---

# `essential_dofs` — boundary-attribute → essential-true-dof set

`essential_dofs :: (space: FiniteElementSpace[N], bdr_attrs: [Attr], bdr_attr_max: Nat) -> DofSet[N]`

Construct the **essential (Dirichlet) true-dof set** `DofSet[N]` on a finite-element `space` from a list
of boundary-attribute numbers `bdr_attrs`. This is the `DofSet[N]` that `eliminate_essential_bc` and
`eliminate_rhs` consume opaquely — before this entry, those two took the essential-dof set as a bare
typed parameter with no constructor home.

The construction is a two-stage composition: `bdr_attrs` are first converted (via the Palace-authored
`mesh::AttrToMarker`) into a **dense boolean marker** over the boundary-attribute range
`[1 .. bdr_attr_max]`, then that marker is resolved (via MFEM's `GetEssentialTrueDofs`, read-as-given)
into the true-dof set on `space`.

## Context

L1 is the mutation-rotation layer: source operations re-expressed as pure functions. `essential_dofs`
is the **typed-set-construction** view of the Dirichlet-boundary marking that every solver pipeline does
before eliminating essential BCs. At L0 the construction is open-coded inline at each consumer (it is a
short two-call idiom, not a named Palace function); the L1 form names the pure composition and treats
its output as an immutable typed value.

The ownership boundary splits cleanly:

- **Palace-authored head.** `bdr_attr_max` is extracted from the mesh as
  `mesh.bdr_attributes.Size() ? mesh.bdr_attributes.Max() : 0` (`palace/fem/multigrid.hpp:95-97`;
  witnessed standalone at `palace/models/spaceoperator.cpp:174`). The marker is then built by
  `mesh::AttrToMarker(bdr_attr_max, bdr_attrs)` (`palace/fem/multigrid.hpp:98`), which is
  **Palace-authored** (contract + decl `palace/utils/geodata.hpp:75-96`; body
  `palace/utils/geodata.cpp:891-916`): it returns an `mfem::Array<int>` of
  size `bdr_attr_max` containing only zeros and ones, with ones at the listed attributes
  (`geodata.hpp:76-78`; body loop `geodata.cpp:905-915`). The special case of a single `-1` entry marks
  **all** boundaries (the wildcard; `geodata.hpp:77-78`; body `geodata.cpp:899-902`).
- **MFEM-opaque tail.** The marker → true-dof set step is
  `space.Get().GetEssentialTrueDofs(marker, out)` (`palace/fem/multigrid.hpp:99-100`), called on
  `.Get()` — the wrapped `mfem::ParFiniteElementSpace`. The true-dof numbering, the marker→dof
  resolution, and the essential-dof semantics are **MFEM-owned, read-as-given** (the same posture
  `fe_space` takes toward dof structure, `book/src/L1/fe_space.md`). This entry treats the dof-set as an
  opaque index structure tagged by the space's true-dof axis `N`; it does NOT crack open the
  dof numbering (doing so would be the identity-in-named-terms smell — the dof set is a
  *value over* the space, not a separate L1 operation that re-mirrors MFEM dof internals).

## Signature

    essential_dofs :: (space: FiniteElementSpace[N], bdr_attrs: [Attr], bdr_attr_max: Nat) -> DofSet[N]

    space        : FiniteElementSpace[N]   -- the FE space; N = space.GetTrueVSize() true-dof axis
    bdr_attrs    : [Attr]                  -- Dirichlet boundary-attribute numbers (1-based);
                                              the single-element list [-1] is the all-boundaries wildcard
    bdr_attr_max : Nat                     -- mesh.bdr_attributes.Max() (0 if no boundary attributes)
    returns      : DofSet[N]               -- the essential true-dof set, a subset of [0 .. N)

Shape contract: the intermediate marker is `Array<int>[bdr_attr_max]` valued in `{0,1}`; the returned
`DofSet[N]` indexes into the `N`-axis true-dof space of `space`. The `N` axis is the same `N` carried by
`fe_space`, `eliminate_essential_bc`, and `eliminate_rhs` — `essential_dofs` is the producer of the
`DofSet[N]` those last two consume.

## Semantics

`essential_dofs(space, bdr_attrs, bdr_attr_max)` selects every true dof of `space` that lies on a
boundary facet whose attribute is in `bdr_attrs`. The Palace-authored head reifies `bdr_attrs` as a
dense boolean indicator over the attribute range; the MFEM tail walks `space`'s essential-dof structure
restricted to the marked boundary and emits the resulting true-dof indices.

The function is **pure in its inputs**: it reads `space` (and the mesh it carries) read-only and returns
a fresh set. In Palace the result is materialized into a caller-provided `mfem::Array<int>` (e.g.
`dbc_tdof_lists->emplace_back()`, `palace/fem/multigrid.hpp:99-100`; `aux_bdr_tdof_lists.emplace_back()`,
`palace/models/spaceoperator.cpp:204-205`) — the mutation-rotation reads that out-parameter write as a
returned value.

## Algebraic laws

Stated on the **Palace-authored head** (the marker construction), where they are syntactic identities;
the MFEM tail is a fixed read-as-given resolver so the head's structure propagates through it.

- **Wildcard saturation.** `bdr_attrs = [-1]` ⇒ the marker is all-ones (`geodata.hpp:77-78`), so
  `essential_dofs(space, [-1], k)` is the **full** essential-true-dof set of every boundary of `space`.
  This is the maximal element of the operator's range under set inclusion.
- **Empty-boundary identity.** `bdr_attr_max = 0` (mesh has no boundary attributes) ⇒ the marker is
  empty ⇒ `essential_dofs(space, _, 0) = ∅` (`multigrid.hpp:95-97` empty-guard).
- **Marker monotonicity (subset-monotone in the attribute list).** Because the marker is a membership
  indicator (`geodata.hpp:76-78`), `bdr_attrs ⊆ bdr_attrs'` (modulo the `-1` wildcard) ⇒
  `marker ≤ marker'` pointwise ⇒ `essential_dofs(space, bdr_attrs, k) ⊆ essential_dofs(space, bdr_attrs', k)`.
  (The dof-set inclusion follows because `GetEssentialTrueDofs` is monotone in its marker — a larger
  marked boundary can only add essential dofs; this monotonicity is the read-as-given MFEM contract.)
- **Marker union-additivity (head-level).** Multiple attribute lists combine by OR on their markers
  before the tail (witnessed: `palace/models/spaceoperator.cpp:187-198` builds `aux_bdr_marker` as the
  pointwise OR of eight per-condition markers, then a single `GetEssentialTrueDofs` on the union,
  `:204-205`). So at the marker stage the construction is a join-semilattice homomorphism from
  attribute-sets (under union) to markers (under pointwise OR).
- **Space-determinism.** For fixed `(space, bdr_attrs, bdr_attr_max)` the output is deterministic — it is
  a pure function of the space's (read-only) dof structure and the marker.

Non-laws: `essential_dofs` is **not** linear/additive *as a dof-set* in `bdr_attrs` (union of attribute
lists does not give union of dof-sets in general — a true dof shared between a marked and an unmarked
facet may flip; the join-homomorphism holds at the **marker** stage, not unconditionally at the dof-set
stage). It is **not** defined independently of `space` (the same attribute list yields different dof-sets
on H1 vs H(curl) spaces — the de-Rham family changes which dofs sit on a boundary).

## Variant axes

- **attribute-wildcard** — the `bdr_attrs = [-1]` single-element-list case marks all boundaries
  (`geodata.hpp:77-78`); the general case marks the listed attributes. (Two points: explicit-list /
  all-boundaries-wildcard.)
- **per-level-hierarchy-application** — in the multigrid path the *same* `bdr_attrs`/marker is applied
  per FE-space level: the marker is built once (`multigrid.hpp:98`) and `GetEssentialTrueDofs` is called
  once per level on each level's finest space (`multigrid.hpp:99-100`, `:106-111`, `:117-122`),
  accumulating into `dbc_tdof_lists`. This per-level fan-out is a property of the *hierarchy* consumer
  (`fe_space_hierarchy`), not of the single-space `essential_dofs`; noted here as the axis along which
  the operator is reused. (Single-space / per-level-replicated.)

## Dependencies

Leaf at L1 — `essential_dofs` is a constructor whose Palace-authored head (`AttrToMarker`,
`bdr_attr_max` extraction) is open-coded and whose tail is MFEM-opaque; it depends on no other L1
operator.

**Cross-refs (consumed-by / operates-on, NOT dependencies):**

- operates on [`fe_space`](./fe_space.md) — the `space: FiniteElementSpace[N]` argument and the `N`
  true-dof axis come from `fe_space`.
- produces the `DofSet[N]` consumed opaquely by [`eliminate_essential_bc`](./eliminate_essential_bc.md)
  (its `dofs: DofSet[N]` parameter) and [`eliminate_rhs`](./eliminate_rhs.md) (its essential-row pin).
- the per-level fan-out belongs to `fe_space_hierarchy` (named-not-authored rough-in).

## Firmness basis

Firm-on-positive-structure: the whole Palace-authored head (`bdr_attr_max` extraction + `AttrToMarker`)
is read directly from source; the stated laws are syntactic/structural identities on that head, and the
MFEM tail (`GetEssentialTrueDofs`) is read-as-given (the same opaque-MFEM-tail posture as
[`fe_space`](./fe_space.md) toward dof structure). The MFEM tail does NOT gate a *constructed* sub-part
materialized from negative anchors, so this is `firm`, not `partly-constructive`. The
no-dedicated-`test-multigrid.cpp` caveat is non-gating.

MPI/Par*/partitioning out-of-scope: `GetEssentialTrueDofs` and `bdr_attributes.Max()`
are read as their single-rank equivalents.

## Evidence

- **Composition (head + tail), hierarchy site:** `palace/fem/multigrid.hpp:92-101` — the dbc block:
  `bdr_attr_max` extraction (`:95-97`), `dbc_marker = mesh::AttrToMarker(bdr_attr_max, *dbc_attr)`
  (`:98`), `GetEssentialTrueDofs(dbc_marker, dbc_tdof_lists->emplace_back())` (`:99-100`). Per-level
  reapplication of the same marker: `:106-111` (h-refinement), `:117-122` (p-refinement).
- **Palace-authored marker construction:** `palace/utils/geodata.hpp:75-96` — `AttrToMarker` decl
  (`:79-80`), the size-`max_attr` zero/one membership-indicator contract + `-1`-wildcard documentation
  (`:76-78`), the template wrapper returning the `mfem::Array<int>` marker (`:90-96`); body
  `palace/utils/geodata.cpp:891-916` (`-1`-singleton all-ones branch `:899-902`, membership-indicator
  loop `:905-915`).
- **Standalone positive site (non-hierarchy):** `palace/models/spaceoperator.cpp:169-206` —
  `CheckBoundaryProperties`: `bdr_attr_max` (`:174`), `mesh::AttrToMarker(bdr_attr_max, dbc_attr)`
  (`:175`), the pointwise-OR marker union over eight conditions (`:187-198`), and the per-level
  `GetEssentialTrueDofs(aux_bdr_marker, aux_bdr_tdof_lists.emplace_back())` (`:202-205`).
- **Consumer of the produced `DofSet[N]`:** [`eliminate_essential_bc`](./eliminate_essential_bc.md)
  (`dofs: DofSet[N]`), [`eliminate_rhs`](./eliminate_rhs.md).

## Downward to L0

The L1>L0 rotation [`essential-dofs-construction-rotation`](../L1-L0/essential-dofs-construction-rotation.md)
narrates how this L1 composition rewrites into the open-coded two-call L0 idiom (`bdr_attr_max`
extraction → `mesh::AttrToMarker` → `GetEssentialTrueDofs`), recording the Palace-authored-head /
MFEM-opaque-tail boundary explicitly.
