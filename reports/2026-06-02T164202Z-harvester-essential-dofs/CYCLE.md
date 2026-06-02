---
agent: harvester
invoked_at: 2026-06-02T16:48:22Z
scope: L1 operator: essential_dofs
status: integrated
integrated_at: 2026-06-02T194500Z
integration_commit: 062ae9e
integration_notes: "cycle-066 D1. essential_dofs PROMOTED FIRM L1 (book/src/L1/essential_dofs.md — boundary-condition true-dof-set member of the FE-space sub-spine; DAG fe_collection > fe_space > essential_dofs). Applied: L1/index.md dep-map TABLE row + deferred-sibling bullet FLIPPED to firm cohort bullet + SUMMARY. RESOLVES c064 straddle OQ toward self-standing entry (WARRANT=YES). citecheck --scan 32 ok / 0 failing. L1 firm 33->34; FE-space sub-spine 2->3. Build clean; no build-repair."
inputs:
  - cycle-066 dispatch D1 (LEAD) prompt
  - planner on-disk inspection (multigrid.hpp:92-101 verified via Read)
  - L0 anchors (on-disk Read, NOT codemap, per confirmed ±1 drift this batch):
    - palace/fem/multigrid.hpp:92-101 (the dbc block inside ConstructFiniteElementSpaceHierarchy)
    - palace/utils/geodata.hpp:75-96 (mesh::AttrToMarker decl + template wrapper)
    - palace/models/spaceoperator.cpp:169-206 (standalone positive site: CheckBoundaryProperties)
  - sibling cross-refs: book/src/L1/fe_space.md (c064), fe_collection.md (c065),
    eliminate_essential_bc.md / eliminate_rhs.md (c055)
  - forward-ref (plain-text, same-cycle): L1-L0/essential-dofs-construction-rotation (D2, gated on this YES)
---

# CYCLE: Formalize essential_dofs at L1

## Summary

`essential_dofs` is the boundary-attribute → essential-true-dof-set operator: given a finite-element
space and a list of boundary-attribute numbers (the Dirichlet boundaries), it produces the `DofSet[N]`
of essential true degrees of freedom that `eliminate_essential_bc` / `eliminate_rhs` currently take
**opaquely** as a bare typed parameter. The target slug `book/src/L1/essential_dofs.md` is **verified
ABSENT** (it exists only as a named-not-authored `rough-in` bullet in `book/src/L1/index.md:89`).

**WARRANT = YES.** This is a genuine L1 operator, not a degenerate MFEM forwarder. The ownership
boundary splits cleanly into a **Palace-authored head** + an **MFEM-opaque tail**:

- **Palace-authored HEAD** — the `bdr_attr_max` extraction (`mesh.bdr_attributes.Max()` with empty-guard
  ⇒ 0; `multigrid.hpp:95-97`, witnessed standalone at `spaceoperator.cpp:174`) **and** the marker
  construction `mesh::AttrToMarker` (contract + decl `geodata.hpp:75-96`; body `geodata.cpp:891-916`).
  `AttrToMarker` is **Palace-authored**
  (it is in `palace/utils/`, `mesh::` namespace, not an MFEM call): attribute-list → dense boolean marker over
  `[1..bdr_attr_max]`, ones at present attributes, with the documented `-1`-singleton ⇒ all-ones
  wildcard (`geodata.hpp:76-78`). This head carries real, self-standing algebraic structure
  (membership-indicator, wildcard, dense-over-max-attr).
- **MFEM-opaque TAIL** — `GetEssentialTrueDofs(marker, out)` (`multigrid.hpp:99`), called on `.Get()`
  (the wrapped `mfem::ParFiniteElementSpace`): marker → true-dof set. Read-as-given; the dof-numbering
  internals are MFEM-owned (the same posture `fe_space` takes toward dof structure).

The composition has its own laws (on the marker head) and its codomain `DofSet[N]` is exactly the
opaque parameter shared across the firm assembled-operator front — so it earns a self-standing home,
NOT an in-line note. It is witnessed at **multiple positive standalone sites** (not only the multigrid
hierarchy): `spaceoperator.cpp:202-205` builds it standalone (and even OR-composes several markers
before the dof extraction, `:187-205`).

**Status = `firm`** (with the MFEM tail noted MFEM-owned-read-as-given), parallel to the c064 `fe_space`
/ c065 `fe_collection` firm-on-positive-structure precedent: the stated laws are syntactic/structural
identities on the Palace-authored marker head; `GetEssentialTrueDofs` is opaque-read, not a *constructed*
sub-part materialized from negative anchors, so `partly-constructive` is the wrong tier. The
no-dedicated-`test-multigrid.cpp` caveat is non-gating per the `fe_space`/`fe_assemble`/`fe_collection`
precedent.

**Signature:**
`essential_dofs :: (space: FiniteElementSpace[N], bdr_attrs: [Attr], bdr_attr_max: Nat) -> DofSet[N]`

MPI/Par*/partitioning out-of-scope (flagged once): `GetEssentialTrueDofs` and `bdr_attributes` are read
as their single-rank equivalents; the `dbc_tdof_lists` per-level accumulation in the hierarchy loop is a
list-of-spaces concern handled by `fe_space_hierarchy`, not this per-space operator.

## Proposed changes

```new:book/src/L1/essential_dofs.md
---
status: firm
harvested_by: harvester:2026-06-02T164202Z-harvester-essential-dofs
cycle: cycle-066
layer: L1
operator: essential_dofs
firmness: firm
lowers_to:
  - L1-L0/essential-dofs-construction-rotation
lifts_from: []
depends_on: []
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
  dof numbering (doing so would be the identity-in-named-terms smell the 2026-06-01 vocabulary-shift
  redirect warns against — the dof set is a *value over* the space, not a separate L1 operation that
  re-mirrors MFEM dof internals).

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

## Status

`firm` — FE-space sub-spine essential-dof-set constructor.

Firm-on-positive-structure: the whole Palace-authored head (`bdr_attr_max` extraction + `AttrToMarker`)
is read directly from source; the stated laws are syntactic/structural identities on that head, and the
MFEM tail (`GetEssentialTrueDofs`) is read-as-given (the same opaque-MFEM-tail posture as
[`fe_space`](./fe_space.md) toward dof structure). The MFEM tail does NOT gate a *constructed* sub-part
materialized from negative anchors, so this is `firm`, not `partly-constructive`. The
no-dedicated-`test-multigrid.cpp` caveat is non-gating per the `fe_space` / `fe_assemble` /
`fe_collection` precedent.

MPI/Par*/partitioning out-of-scope (flagged once): `GetEssentialTrueDofs` and `bdr_attributes.Max()`
are read as their single-rank equivalents.

## Evidence

- **Composition (head + tail), hierarchy site:** `palace/fem/multigrid.hpp:92-101` — the dbc block:
  `bdr_attr_max` extraction (`:95-97`), `dbc_marker = mesh::AttrToMarker(bdr_attr_max, *dbc_attr)`
  (`:98`), `GetEssentialTrueDofs(dbc_marker, dbc_tdof_lists->emplace_back())` (`:99-100`). Per-level
  reapplication of the same marker: `:106-111` (h-refinement), `:117-122` (p-refinement).
- **Palace-authored marker construction:** `palace/utils/geodata.hpp:75-96` — `AttrToMarker` decl
  (`:79-80`), the size-`max_attr` zero/one membership-indicator contract + `-1`-wildcard documentation
  (`:76-78`), the template wrapper returning the `mfem::Array<int>` marker (`:90-96`).
- **Standalone positive site (non-hierarchy):** `palace/models/spaceoperator.cpp:169-206` —
  `CheckBoundaryProperties`: `bdr_attr_max` (`:174`), `mesh::AttrToMarker(bdr_attr_max, dbc_attr)`
  (`:175`), the pointwise-OR marker union over eight conditions (`:187-198`), and the per-level
  `GetEssentialTrueDofs(aux_bdr_marker, aux_bdr_tdof_lists.emplace_back())` (`:202-205`).
- **Consumer of the produced `DofSet[N]`:** [`eliminate_essential_bc`](./eliminate_essential_bc.md)
  (`dofs: DofSet[N]`), [`eliminate_rhs`](./eliminate_rhs.md).

## Downward to L0

The L1>L0 rotation `essential-dofs-construction-rotation` (cycle-066 D2; forthcoming) narrates how this
L1 composition rewrites into the open-coded two-call L0 idiom (`bdr_attr_max` extraction →
`mesh::AttrToMarker` → `GetEssentialTrueDofs`), recording the Palace-authored-head / MFEM-opaque-tail
boundary explicitly.
```

```edit:book/src/L1/index.md
- `essential_dofs` *(rough-in; no anchor yet)* — boundary-attribute-marker → essential-true-dof-set (`GetEssentialTrueDofs` ∘ `AttrToMarker`, `palace/fem/multigrid.hpp:97-99`); the `DofSet[N]` that `eliminate_essential_bc`/`eliminate_rhs` take opaquely. Straddles the MFEM-owned boundary (the attribute→marker *shape* lifts; the dof-numbering is read-as-given) — lean noted-property-of-`fe_space` unless `eliminate_*`'s `DofSet[N]` demands a self-standing home (OQ).
- [`essential_dofs`](./essential_dofs.md) **is now FIRM** *(cycle-066 D1)* — the boundary-attribute → essential-true-dof-set constructor `(space: FiniteElementSpace[N], bdr_attrs: [Attr], bdr_attr_max: Nat) → DofSet[N]`: `bdr_attrs` → (Palace-authored `mesh::AttrToMarker`, `palace/utils/geodata.hpp:75-96`) a dense boolean marker over `[1..bdr_attr_max]` → (MFEM-opaque `GetEssentialTrueDofs`, read-as-given) the true-dof set. **WARRANT=YES (genuine self-standing entry, NOT an in-line `fe_space` note):** the OQ "lean noted-property-of-`fe_space`" is RESOLVED toward a self-standing home — the codomain `DofSet[N]` is exactly the opaque parameter `eliminate_essential_bc`/`eliminate_rhs` consume, and the Palace-authored marker head carries real laws (wildcard saturation, empty-boundary identity, marker subset-monotonicity, marker union-additivity as a join-semilattice homomorphism witnessed at `spaceoperator.cpp:187-205`). **Two variant axes:** attribute-wildcard (`[-1]` all-boundaries vs explicit list, `geodata.hpp:77-78`), per-level-hierarchy-application (same marker reapplied per level, `multigrid.hpp:106-111,117-122` — a hierarchy-consumer property). Palace-authored-head (`bdr_attr_max` extraction `multigrid.hpp:95-97` + `AttrToMarker`) / MFEM-opaque-tail (`GetEssentialTrueDofs` on `.Get()`, `multigrid.hpp:99`) split; firm-on-positive-structure (whole head read; tail read-as-given like `fe_space`'s dof internals — NOT partly-constructive since no sub-part is materialized from negative anchors), no-dedicated-`test-multigrid.cpp` caveat non-gating per `fe_space`/`fe_collection` precedent. Standalone positive site `palace/models/spaceoperator.cpp:169-206`. L1>L0: `essential-dofs-construction-rotation` (cycle-066 D2). MPI/Par* out-of-scope (single-rank read).
```

```edit:book/src/SUMMARY.md
- [eliminate_essential_bc](./L1/eliminate_essential_bc.md)
- [essential_dofs](./L1/essential_dofs.md)
```

## Operator content

(Authored in full inside the `new:book/src/L1/essential_dofs.md` block above — signature, semantics,
five marker-head algebraic laws + two non-laws, two variant axes, dependencies/cross-refs, `firm`
status with the firm-on-positive-structure rationale, evidence, and the downward-to-L0 forward-ref.)

## Supporting evidence

All citations verified on-disk via `tools/citecheck/citecheck.py --anchor` against
`reference/palace/palace/...` (codemap NOT used — confirmed ±1 drift on FE headers this batch):

- `palace/fem/multigrid.hpp:95` anchor `bdr_attr_max` ✓; `:98` anchor `AttrToMarker` ✓;
  `:99` anchor `GetEssentialTrueDofs` ✓ (the dbc block `:92-101`, per-level `:106-111,117-122`).
- `palace/utils/geodata.hpp:91` anchor `AttrToMarker` ✓; the `:75-80` decl + zero/one + `-1`-wildcard
  contract ✓ (marker anchor lands `:75`, within the `:75-80` range).
- `palace/models/spaceoperator.cpp:174` anchor `bdr_attr_max` ✓; `:175` anchor `AttrToMarker` ✓;
  `:204` anchor `GetEssentialTrueDofs` ✓ (standalone site `:169-206`, marker-OR union `:187-198`).

Citation root is `palace/...` (strips the on-disk `reference/palace/` prefix), per the existing
`fe_space.md` / `fe_collection.md` index rows.

## Dual-registration note (per partition)

This report registers (1) its OWN dep-map row (the `essential_dofs` table-area bullet conversion in the
`book/src/L1/index.md` edit above) and (2) its OWN §"Firm (FE-space sub-spine)" cohort bullet. The
**consolidated running-count tally** (the FE-space-sub-spine member count 2→3, the grand-total 33→34,
the growth-log/fork-flip prose at `book/src/L1/index.md:31`,`:78`) is **DEFERRED to D4** (the named
count-owner this cycle), per the index-dual-registration partition.

Note for D4: with `essential_dofs` firm, the FE-space sub-spine goes **2 → 3** members
(`fe_space`, `fe_collection`, `essential_dofs`) and the L1 firm grand total goes **33 → 34**
(27 main + 4 FE-assembly + 3 FE-space).

## Open questions / caveats

- **Layer-intro refresh (D4 / layer-intro-author):** the §"Firm (FE-space sub-spine)" prose at
  `book/src/L1/index.md:78` describes the sub-spine as a two-member producer→consumer chain
  (`fe_collection` ▷ `fe_space`). With `essential_dofs` firm, the sub-spine reads as a small DAG:
  `fe_collection` ▷ `fe_space`, and `fe_space` ▷ `essential_dofs` (the dof-set is built *on* a
  constructed space and feeds the assembly BC-treatment post-compositions). Suggest the intro author add
  `essential_dofs` to the sub-spine narrative as the **dof-set producer that de-opaques the
  `DofSet[N]`** parameter of `eliminate_essential_bc`/`eliminate_rhs`.
- **Replace-and-propagate (later cycle, NOT this one):** `eliminate_essential_bc`'s
  `dofs: DofSet[N]` and `eliminate_rhs`'s essential-row pin can now gain a live cross-ref to
  `essential_dofs` for their `DofSet[N]` provenance (currently a bare typed name). Same class of
  follow-up as the `fe_space` opaque-parameter fan-out (`book/src/L1/index.md:94`).
- **`fe_space_hierarchy` (named-not-authored rough-in):** the per-level fan-out of `essential_dofs`
  (the `dbc_tdof_lists` accumulation, `multigrid.hpp:99-100,106-111,117-122`) is a property of the
  hierarchy constructor, not of this single-space operator. It belongs in the eventual
  `fe_space_hierarchy` entry; flagged here so that entry picks up the per-level dof-set fan-out.
- **D2 gate satisfied:** warrant=YES, so D2 may proceed to author
  `book/src/L1-L0/essential-dofs-construction-rotation.md` (the L1>L0 rotation forward-referenced from
  this chapter's "Downward to L0" section + the `lowers_to` frontmatter).
