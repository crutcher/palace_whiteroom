---
agent: harvester
invoked_at: 2026-06-02T15:20:43Z
scope: L1 operator: fe_space
status: integrated
integrated_at: 2026-06-02T180000Z
integration_commit: PLACEHOLDER_SHA_CYCLE_064
integration_notes: |
  cycle-064 D2, applied clean by integrator-per-report (STAGING row 2), finalized by integrator-finalize.
  `fe_space` PROMOTED FIRM L1 (book/src/L1/fe_space.md — (mesh, collection) → FiniteElementSpace[N], the
  prime FE-space-construction entry, the shared substrate under all 5 solver pipelines; de-Rham family
  variant axis H1/H(curl)/H(div)/L2; firm-on-positive-structure; NO `dof_map` mirror — anti-mirror
  discipline). Applied: L1/index.md dep-map TABLE row (the separate cohort prose bullet was correctly
  dropped by the repairer — D4 owns the cohort home) + SUMMARY chapter line. Ctor cite fespace.hpp:67-75
  consistent on disk. L1 firm 31→32. retroactive-budget global = 0.
inputs:
  - reports/2026-06-02T151056Z-cross-layer-cross-cutter-fe-space-front-survey/CYCLE.md (D1 survey GATE — granularity verdict ONE prime entry)
  - palace/fem/fespace.hpp:21-194 (FiniteElementSpace typed object + variadic ctor :67-75)
  - palace/fem/multigrid.hpp:22-72 (ConstructFECollections) + :78-126 (ConstructFiniteElementSpaceHierarchy)
  - palace/models/spaceoperator.cpp:45-89 (the ND/H1/RT construct calls :47/49/51 + 2-D L2-curl :72-75)
  - book/src/L0/fespace-file.md (firm L0 localization; MFEM-as-given framing; de-Rham complex :165-169)
  - book/src/L1/{fe_assemble,weak_form_term,eliminate_essential_bc,eliminate_rhs}.md (the 4 opaque-space consumers)
---

# CYCLE: Formalize fe_space at L1

## Summary

`fe_space :: (mesh: Mesh, collection: FECollection) -> FiniteElementSpace[N]` is the construction of
a finite-element space from a mesh paired with a finite-element collection — the **shared substrate
under every assembled-operator pipeline** and the typed domain/range object that four firm L1 entries
(`fe_assemble`, `weak_form_term`, `eliminate_essential_bc`, `eliminate_rhs`) already take opaquely.
There is NO prior L1 entry; one firm L0 localization exists (`book/src/L0/fespace-file.md`). Per the
D1 survey GATE verdict, this lands as **ONE prime entry** — NOT a `fe_space`+`fe_collection`+`dof_map`
split (a `dof_map` entry would mirror opaque MFEM dof structure — the redirect's identity-in-named-terms
smell). I assign status **firm (firm-on-positive-structure)**: the construction is read off the positive
variadic ctor (`fespace.hpp:67-75`) + the ND/H1/RT call sites (`spaceoperator.cpp:47/49/51`), the
**de-Rham family variant axis** (H1/H(curl)/H(div)/L2 ↔ `H1_/ND_/RT_/L2_FECollection`) is fully
witnessed, and the laws are syntactic identities on positive source (the no-dedicated-test caveat is
non-gating, per the `fe_assemble`/`apply_linop` precedent). The dof-numbering / ordering / conformity /
prolongation-restriction internals are noted **MFEM-owned-read-as-given** (NOT cracked open). **No
concept page authored** (judged below). `fe_collection`, `essential_dofs`, `fe_space_hierarchy` named
as explicitly-deferred follow-on siblings.

## Proposed changes

```new:book/src/L1/fe_space.md
---
status: firm
harvested_by: harvester:2026-06-02T151056Z-harvester-fe-space
cycle: cycle-064
---

# `fe_space` — finite-element space construction

`fe_space :: (mesh: Mesh, collection: FECollection) -> FiniteElementSpace[N]`

Construct the typed finite-element space `FiniteElementSpace[N]` — the **domain/range object of every
assembled-operator pipeline** — from a `Mesh` paired with a finite-element `FECollection`. `N` is the
true-dof count `space.GetTrueVSize()`. The de-Rham family (H1 / H(curl) / H(div) / L2) the space
belongs to is selected by the collection type. This is the shared substrate that `fe_assemble`,
`weak_form_term`, `eliminate_essential_bc`, and `eliminate_rhs` consume; before this entry those four
took the FE-space (and its true-dof axis `N`, and the essential-dof set `DofSet[N]`) as bare opaque
typed parameters.

## Context

L1 is the mutation-rotation layer: source operations re-expressed as pure functions. `fe_space` is the
**typed-object-construction** view of that rotation — Palace's `FiniteElementSpace` is constructed once
and thereafter consumed read-only by the assembly fold; the L1 form names the pure
`(mesh, collection) → space` pairing and treats the constructed space as an immutable typed value.

At L0 the construction is the variadic constructor
`FiniteElementSpace(Mesh &mesh, T &&...args)` (`palace/fem/fespace.hpp:67-75`), which forwards
`(&mesh.Get(), std::forward<T>(args)...)` straight into the wrapped `mfem::ParFiniteElementSpace`
(`fespace.hpp:68`). The Palace-side construction is therefore *exactly* the pairing of a mesh with an
FE collection: the second forwarded argument is the `FECollection` (a
`std::unique_ptr<FECollection>::get()` at every call site). Every solver model operator builds its
spaces this way through `ConstructFiniteElementSpaceHierarchy` (`palace/fem/multigrid.hpp:78-126`),
whose coarse seed is a single `std::make_unique<FiniteElementSpace>(*mesh[coarse_mesh_l], fecs[0].get())`
(`multigrid.hpp:90`) — i.e. one `fe_space` construction — and whose h/p levels each `AddLevel` one more
`FiniteElementSpace` built the same way (`multigrid.hpp:106,117`).

This chapter is defined in L1 vocabulary (the typed `(mesh, collection) → space` construction). The
forward rewrite into the L0 ctor + the `ConstructFiniteElementSpaceHierarchy` coarse-seed is the L1>L0
theme `fe-space-construction-rotation` (authored cycle-064 D3; forward-reference until on disk).

## Signature

    fe_space :: (mesh: Mesh, collection: FECollection) -> FiniteElementSpace[N]

Shape contract (bunsen-style, named axes):

- `mesh` — `Mesh` — the discretised domain; the Palace `Mesh` wrapper owning a single-rank
  `mfem::ParMesh` (`palace/fem/fespace.hpp:28` holds the non-owned `Mesh &mesh`). Read-only; the
  partitioning attribute-remap (`loc_attr`/`loc_bdr_attr`) is out of scope (single-rank reading).
- `collection` — `FECollection` — the finite-element collection selecting the basis family + order;
  one of the de-Rham family types (see *Variant axis*). At L0 it is the second forwarded ctor argument
  (`fespace.hpp:68`).
- result — `FiniteElementSpace[N]` — the typed space; `N = result.GetTrueVSize()`
  (`palace/fem/fespace.hpp:96`) is the **global true-dof count** (the square dimension of every
  operator assembled over this space). The space additionally carries an L-vector ↔ true-dof transfer
  via the prolongation/restriction matrices (`fespace.hpp:102-103`), MFEM-owned (see below).

The true-dof axis `N` is the load-bearing output: it is the very `N` that
[`fe_assemble`](./fe_assemble.md)'s `LinearOperator[N, N]`,
[`eliminate_essential_bc`](./eliminate_essential_bc.md)'s `DofSet[N]`, and all the BLAS-1 `Tensor[N]`
operands are indexed by. `fe_space` is the operator that *defines* `N`.

## Variant axis: the de-Rham family

The single load-bearing variant axis is **which de-Rham space the collection picks**, selected purely
by the `FECollection` type passed as `collection`:

| Family | Collection type | de-Rham slot | Map type |
|---|---|---|---|
| H1 (nodal scalar) | `H1_FECollection` | `H1` →∇ | VALUE |
| H(curl) (Nédélec) | `ND_FECollection` | →∇ `H(curl)` →∇× | (vector) |
| H(div) (Raviart–Thomas) | `RT_FECollection` | →∇× `H(div)` →∇· | (vector) |
| L2 (discontinuous) | `L2_FECollection` | →∇· `L2` | INTEGRAL |

The construction is **identical across the family modulo the collection type** — `fe_space` is
variant-uniform in its body; the family is an attribute of the `collection` argument. All four types
are witnessed positively at the construction call sites:
`ConstructFiniteElementSpaceHierarchy<mfem::ND_FECollection>` (`palace/models/spaceoperator.cpp:47`),
`<mfem::H1_FECollection>` (`:49`), `<mfem::RT_FECollection>` (`:51`), and the 2-D-only
`<mfem::L2_FECollection>` for `B = curl E` (`:72-75`, the `INTEGRAL` map-type collection constructed at
`:72-73`). The de-Rham complex H1 →∇ H(curl) →∇× H(div) →∇· L2 is the L0 framing at
`book/src/L0/fespace-file.md:165-169`.

The **collection order schedule** itself (`ConstructFECollections`, `palace/fem/multigrid.hpp:22-72`)
— the p-multigrid order sequence, the `pmin` floor (1 for H1/ND, 0 for RT/L2,
`multigrid.hpp:30-33`), the GaussLobatto/GaussLegendre/IntegratedGLL basis-type choice
(`multigrid.hpp:34-38`), the LINEAR/LOGARITHMIC coarsening — is a *separate* construction that produces
the `collection` input(s). At this assembly-front altitude a single `FECollection` is just an input to
`fe_space`; the list-producing order-schedule is deferred to the `fe_collection` / `fe_space_hierarchy`
follow-on (see *Status*).

## MFEM-owned, read-as-given (NOT lifted)

The `FiniteElementSpace` exposes a body of dof bookkeeping that is **MFEM's structure**, surfaced
through thin forwarding accessors that all `return Get().X()` (`palace/fem/fespace.hpp:93-103`). The L1
`fe_space` treats these as given properties of the constructed value, NOT as L1 operations:

- **dof / vdof numbering, byNODES/byVDIM ordering, element-to-dof tables, conformity** — forwarded to
  `mfem::ParFiniteElementSpace` verbatim; the L0 chapter frames them as MFEM's, read as-is
  (`book/src/L0/fespace-file.md:18-25,150-158`). The space is an **opaque index structure with a known
  true-dof count `N`**, not a re-defined numbering.
- **prolongation / restriction matrices** (`GetProlongationMatrix` / `GetRestrictionMatrix`,
  `fespace.hpp:102-103`) — MFEM-owned, forwarded verbatim; the L-vector ↔ true-dof transfer.

Authoring a separate `dof_map` L1 entry for this structure would mint a thin mirror of opaque MFEM
internals — the redirect's degenerate identity-in-named-terms smell (D1 survey §3). The dof structure
is a *property* of the `FiniteElementSpace` value (the opaque axis `N`), not a distinct L1 operation.

## Algebraic laws

The laws are syntactic identities on the positive construction (no convergence/iteration semantics):

1. **True-dof axis determinism.** The output axis `N = GetTrueVSize()` (`fespace.hpp:96`) is a pure
   function of `(mesh, collection)` — same mesh + same collection ⟹ same `N`. This is the axis every
   downstream `[N]`-indexed operand shares.
2. **Family selection by collection type.** The de-Rham family of the result is determined entirely by
   the `FECollection` subtype (`H1_/ND_/RT_/L2_FECollection`); the construction body does not branch on
   family (`spaceoperator.cpp:47/49/51` are the same `ConstructFiniteElementSpaceHierarchy` call
   modulo template parameter). Family is an attribute of the argument, not a variant of the operation.
3. **Mesh/collection separability.** `fe_space` is jointly a function of `(mesh, collection)` with the
   two arguments independent: the same `collection` over a refined mesh, or the same mesh under a
   higher-order `collection`, are both well-formed constructions (the h- and p-refinement loops of
   `ConstructFiniteElementSpaceHierarchy` — `multigrid.hpp:106` varying the mesh, `:117` varying the
   collection — exercise exactly these two independent axes).
4. **Coarse-seed identity (hierarchy base case).** The coarsest level of a space hierarchy *is* one
   `fe_space` construction: `ConstructFiniteElementSpaceHierarchy(...)`'s seed is
   `make_unique<FiniteElementSpace>(*mesh[coarse_mesh_l], fecs[0].get())` (`multigrid.hpp:90`). A
   hierarchy of one level reduces to a single `fe_space` call. (This is the in-line annotation of how
   `fe_space` relates to the deferred `fe_space_hierarchy` — the hierarchy folds `AddLevel` over
   repeated `fe_space` constructions.)

**Non-law (MFEM-owned).** `fe_space` does NOT define the dof numbering, ordering, or conformity of its
result — these are MFEM's and are read as given (above). No L1 law constrains them.

## Dependencies

(leaf at L1 — the construction takes a `Mesh` and an `FECollection` and produces a typed value; no
other L1 operator is invoked). The result is consumed by [`fe_assemble`](./fe_assemble.md),
[`weak_form_term`](./weak_form_term.md), [`eliminate_essential_bc`](./eliminate_essential_bc.md), and
[`eliminate_rhs`](./eliminate_rhs.md) (the opaque-space consumers — see *Downward*); those are
consumed-by relations, not dependencies.

## Downward (to L0)

The L1>L0 rotation `fe-space-construction-rotation` (cycle-064 D3) narrates how the typed
`(mesh, collection) → FiniteElementSpace[N]` construction rewrites into the L0 variadic ctor
(`fespace.hpp:67-75`) forwarding into `mfem::ParFiniteElementSpace`, and into the
`ConstructFiniteElementSpaceHierarchy` coarse-seed (`multigrid.hpp:89-90`) + `GetEssentialTrueDofs`
extraction (`multigrid.hpp:98-99`, via `mesh::AttrToMarker` `:97-98`). (Forward-reference until that
theme is on disk.)

**Opaque-parameter fan-out (replace-and-propagate forward-look — re-anchors NOT enacted this cycle).**
Four firm L1 entries currently take the FE-space, its true-dof axis `N`, or its essential-dof set
opaquely; a firm `fe_space` gives each a real L1 home. A later replace-and-propagate dispatch (D4 +
follow-on) upgrades their bare typed parameters to live `[fe_space](./fe_space.md)` cross-refs:

- `fe_assemble` — `space: FiniteElementSpace[N]` (the bare typed input; `N = space.GetTrueVSize()`
  named but undefined-at-L1) becomes the output of `fe_space(mesh, collection)`; `N` gets its L1
  definition here. (The per-term `A(space, ·)` map stays libCEED-owned — a separate obstruction.)
- `weak_form_term` — `A(space, ·)` over an opaque `space` cross-refs `fe_space`.
- `eliminate_essential_bc` — `dofs: DofSet[N]`, `N = space.GetTrueVSize()`, re-anchors `N` + the
  essential-dof extraction (the deferred `essential_dofs` sibling) to `fe_space`.
- `eliminate_rhs` — the `dbc_tdof_list` masking projections over the same opaque dof set re-anchor to
  `fe_space`'s `N`.

## Status

**firm (firm-on-positive-structure).** The construction is read directly from positive source: the
variadic ctor (`palace/fem/fespace.hpp:67-75`) and the ND/H1/RT construction calls
(`palace/models/spaceoperator.cpp:47/49/51`) plus the 2-D L2-curl construction (`:72-75`). The de-Rham
family variant axis is fully witnessed (all four collection types appear at construction sites). Every
law is a syntactic identity on this positive structure — there is no convergence/iteration semantics to
test-gate, so the absence of a dedicated `test-fespace.cpp` exercising the constructor does not gate
firm (the `fe_assemble` cycle-054 / `apply_linop` no-dedicated-test precedent). The dof-numbering /
ordering / conformity / prolongation-restriction internals are explicitly MFEM-owned-read-as-given, not
L1 law substrate.

This is the highest-fan-out entry of the FE-space-construction front: the **shared substrate under all
five solver pipelines** and the de-opaquing home for four firm L1 entries (the fan-out above).

**Deferred follow-on siblings (named, NOT authored this cycle):** `fe_collection` (the
`ConstructFECollections` order schedule — `multigrid.hpp:22-72`), `essential_dofs` (the
boundary-attribute-marker → essential-true-dof-set extraction, `multigrid.hpp:97-99` — straddles the
MFEM-owned boundary, likely a noted-property of `fe_space` unless `eliminate_*`'s `DofSet[N]` demands a
self-standing home), and `fe_space_hierarchy` (the h/p-refinement multigrid stack,
`multigrid.hpp:78-126`). The `BuildDiscreteInterpolator` (de-Rham interpolator) and
`BuildProlongationAtLevel` (multigrid transfer) machinery is sibling-pull-gated — named, not authored.

## Evidence

- `palace/fem/fespace.hpp:67-75` — the variadic `FiniteElementSpace(Mesh &mesh, T &&...args)`
  constructor forwarding `(&mesh.Get(), std::forward<T>(args)...)` into `mfem::ParFiniteElementSpace`
  (`:68`). The construction IS the `(mesh, collection)` pairing.
- `palace/fem/fespace.hpp:21-194` — the `FiniteElementSpace` typed object; wrapped
  `mfem::ParFiniteElementSpace fespace` (`:25`) + non-owned `Mesh &mesh` (`:28`); `GetTrueVSize`
  (`:96`); prolongation/restriction matrices (`:102-103`); the MFEM-forwarding dof accessors (`:93-103`).
- `palace/models/spaceoperator.cpp:47/49/51` — the ND / H1 / RT `ConstructFiniteElementSpaceHierarchy`
  construction calls (every solver builds its spaces here); the 2-D L2-curl construction at `:72-75`
  (`L2_FECollection` with `INTEGRAL` map type at `:72-73`).
- `palace/fem/multigrid.hpp:78-126` — `ConstructFiniteElementSpaceHierarchy`: the coarse-seed single
  `FiniteElementSpace` construction (`:89-90`), `mesh::AttrToMarker` (`:97-98`) + `GetEssentialTrueDofs`
  (`:98-99`), the h-refinement `AddLevel` (`:106`) and p-refinement `AddLevel` (`:117`).
- `palace/fem/multigrid.hpp:22-72` — `ConstructFECollections` (the deferred order-schedule context):
  `pmin` floor (`:30-33`), basis-type choice (`:34-38`).
- `book/src/L0/fespace-file.md` — the firm L0 localization: MFEM-as-given framing (`:18-25,150-158`),
  the de-Rham complex H1 →∇ H(curl) →∇× H(div) →∇· L2 (`:165-169`), the transparent libCEED-cache
  classification.
- `book/src/L1/fe_assemble.md:60` — `space: FiniteElementSpace[N]` opaque input;
  `book/src/L1/weak_form_term.md:79` — `A(space, ·)` over opaque `space`;
  `book/src/L1/eliminate_essential_bc.md:63` — `dofs: DofSet[N]`, `N = space.GetTrueVSize()`;
  `book/src/L1/eliminate_rhs.md:67` — `dbc_tdof_list` masking over the opaque dof set.
```

**(Cohort bullet REMOVED at repair — cohort-placement reconciliation, cycle-064 D2 repairer.)** D2 originally proposed a prose cohort bullet for `fe_space` anchored after the `weak_form_term` bullet, which would have placed `fe_space` UNDER the existing "FE-assembly sub-spine" subsection (and carried the framing "FE-assembly sub-spine grows 4→5"). That framing is WRONG under wave-mate D4's authoritative cohort structure: `fe_space` CONSTRUCTS the space (its own NEW "FE-space sub-spine — 1" subsection), distinct from FE-assembly which FOLDS over it; FE-assembly stays at 4. D4 (`layer-intro-author-fe-space-subspine`) is the framing/count owner this cycle and creates the FE-space sub-spine subsection, which already describes `fe_space`. To avoid a fragile cross-block re-anchor (D4's subsection text is not yet on disk — it is in D4's proposed-changes), the repairer DROPPED D2's separate cohort bullet entirely.

**INTEGRATOR-NOTE (cohort-placement reconciliation):** D4's NEW "FE-space sub-spine" subsection in `book/src/L1/index.md` is the AUTHORITATIVE home for the `fe_space` cohort description — D2 contributes NO prose cohort bullet to `index.md`. D2's dep-map TABLE row and SUMMARY.md line (below) are UNAFFECTED and DO land (the dep-map is a flat per-operator table with no sub-spine subsectioning; SUMMARY is a flat list). The "FE-assembly sub-spine grows 4→5 / firm grand total 31→32" framing originally in D2's prose is RETRACTED — D4 owns the consolidated tally and the new-sub-spine accounting (FE-assembly stays 4; FE-space is a new sub-spine of 1).

(Dual-registration note: the consolidated running-count tally — the firm grand-total prose + growth-log in §"Vocabulary cohort" lead paragraph — is DEFERRED to D4, the count-owner this cycle. D2 registers only its dep-map row + SUMMARY line below; D4 authors the FE-space sub-spine subsection + the absolute total.)

The dep-map table row (a separate anchor — append after the `weak_form_term` row, the last FE-assembly row before the obstruction rough-in rows):

```edit:book/src/L1/index.md
| [`weak_form_term`](./weak_form_term.md) | `({ coefficient: MaterialCoefficient, diff_op: DifferentialOperator }) → WeakFormTerm` (i.e. one weak-form contribution `a(u, v) = (Q · 𝒟u, 𝒟v)`, `𝒟 ∈ {Gradient, Identity, Curl, Divergence}`) | (leaf; inert `(coefficient, differential-operator)` pair; the element type [`fe_assemble`](./fe_assemble.md) folds over opaquely — consumed-by, NOT a dependency; the per-term realization `A(space, ·)` is the libCEED-owned opaque map below the fold) | `firm` (FE-assembly sub-spine term abstraction; **differential-operator variant axis** — `Gradient`/`Curl` grounded by two in-scope solver-K witnesses `palace/models/laplaceoperator.cpp:191-192` + `palace/models/curlcurloperator.cpp:179-181` (same `BilinearForm`-fold, integrator-slot-only difference); `Identity`/mass + `Divergence`/div-div named pending-pull siblings; L0 integrator wrappers `palace/fem/integrator.hpp:39-130` + instantiation `palace/fem/bilinearform.hpp:53-57`; harvested cycle-061; clean-gate PROMOTE pulled-not-speculative; firm-on-positive-structure, no-dedicated-test caveat non-gating per `fe_assemble` precedent; laws: coefficient-linearity + coefficient-additivity + diff-op-discreteness + symmetry-for-symmetric-`Q`; term KERNEL libCEED-opaque, term IDENTITY Palace-readable) |
| [`fe_space`](./fe_space.md) | `(mesh: Mesh, collection: FECollection) → FiniteElementSpace[N]` (i.e. the typed FE space; `N = GetTrueVSize()` the global true-dof count) | (leaf; the construction pairs a `Mesh` with an `FECollection` and produces an immutable typed value; consumed-by [`fe_assemble`](./fe_assemble.md)/[`weak_form_term`](./weak_form_term.md)/[`eliminate_essential_bc`](./eliminate_essential_bc.md)/[`eliminate_rhs`](./eliminate_rhs.md) — those are consumed-by relations, NOT dependencies; the dof-numbering/ordering/conformity/prolongation-restriction internals are MFEM-owned-read-as-given) | `firm` (FE-space-construction front prime entry; the shared substrate under all 5 solver pipelines; **de-Rham family variant axis** H1/H(curl)/H(div)/L2 ↔ `H1_/ND_/RT_/L2_FECollection`, all 4 witnessed at construction sites `palace/models/spaceoperator.cpp:47/49/51` (ND/H1/RT) + `:72-75` (2-D L2-curl); L0: variadic ctor `palace/fem/fespace.hpp:67-75` forwarding into `mfem::ParFiniteElementSpace`, `GetTrueVSize` `:96`, MFEM-forwarders `:93-103`; coarse-seed `palace/fem/multigrid.hpp:89-90` inside `ConstructFiniteElementSpaceHierarchy` `:78-126`; harvested cycle-064; clean-gate PROMOTE; firm-on-positive-structure, no-dedicated-test caveat non-gating per `fe_assemble`/`apply_linop` precedent; laws: true-dof-axis determinism, family-selection-by-collection-type, mesh/collection separability, coarse-seed identity; NO `dof_map` mirror (MFEM-owned-read-as-given dof structure = identity-in-named-terms smell); opaque-parameter fan-out re-anchors `fe_assemble`/`weak_form_term`/`eliminate_essential_bc`/`eliminate_rhs` in a later replace-and-propagate pass; deferred siblings `fe_collection`/`essential_dofs`/`fe_space_hierarchy` named-not-authored; L1>L0: `fe-space-construction-rotation` cycle-064 D3) |
```

```edit:book/src/SUMMARY.md
- [weak_form_term](./L1/weak_form_term.md)
- [fe_space](./L1/fe_space.md)
```

## Operator content

The full firm chapter body is authored inside the `new:book/src/L1/fe_space.md` proposed-changes
block above. In brief:

- **Slug + one-line**: `fe_space` — construct the typed FE space from a mesh + an FE collection.
- **Signature**: `fe_space :: (mesh: Mesh, collection: FECollection) -> FiniteElementSpace[N]`,
  `N = space.GetTrueVSize()` the global true-dof count (the square dimension every downstream
  `[N]`-indexed operator/operand shares).
- **Semantics**: the typed-object-construction view of the mutation rotation — Palace's
  `FiniteElementSpace` is constructed once (the variadic ctor forwarding `(&mesh.Get(), collection)`
  into `mfem::ParFiniteElementSpace`, `fespace.hpp:67-75`) and thereafter consumed read-only; the L1
  form names the pure `(mesh, collection) → space` pairing.
- **Variant axis**: the **de-Rham family** — H1 / H(curl) / H(div) / L2 selected purely by the
  `FECollection` type, all four witnessed at construction sites.
- **Algebraic laws** (only those that hold): true-dof-axis determinism, family-selection-by-collection-
  type, mesh/collection separability, coarse-seed identity. One MFEM-owned non-law (dof numbering not
  L1-defined).
- **Dependencies**: leaf at L1 (consumed by the four FE-assembly entries; consumed-by, not deps).
- **Status**: `firm` (firm-on-positive-structure).
- **Evidence**: as in the chapter §Evidence (all citations self-verified via `palace-codemap` +
  `tools/citecheck/citecheck.py --anchor`; two drifts caught and corrected pre-emit — see below).

## Supporting evidence

All load-bearing L0 citations were self-verified against on-disk source via
`python3 tools/citecheck/citecheck.py <path:lo-hi> --anchor <token>` before emit. Two anchors **drifted**
versus the D1 survey's line numbers and were corrected:

- `ConstructFECollections` — survey implied `multigrid.hpp:22-75`; the function NAME is at `:25` and the
  body spans `:22-72` (the `std::reverse` close is `:71`, not `:75`). Corrected to `multigrid.hpp:22-72`.
- `mesh::AttrToMarker` — survey cited `multigrid.hpp:97`; the call is at `:98` (`citecheck` `[DRIFT +1]`).
  The `GetEssentialTrueDofs` it feeds is `:98-99`. Corrected.
- The `FiniteElementSpace` ctor — the authoritative on-disk range is `:67-75`
  (`template <typename... T>` at `:67`, the signature `FiniteElementSpace(Mesh &mesh, T &&...args)` at
  `:68`, the forwarding init-list at `:69`, the closing brace at `:75`; the destructor is at `:76`). A
  transient codemap read under-numbered by one (suggesting `:67-75`); retained the survey's correct
  `:67-75` after direct on-disk verification (matches D3's `fe-space-construction-rotation` ctor cite).
- Confirmed exact: ctor at `fespace.hpp:67-75` (`[ok]` anchor `FiniteElementSpace` at `:68`);
  ND/H1/RT construct calls at `spaceoperator.cpp:47/49/51` (`[ok]` anchor on all three lines); 2-D
  L2-curl construction at `spaceoperator.cpp:72-75` (`[ok]` anchor `L2_FECollection` at `:72`);
  `GetTrueVSize` `fespace.hpp:96`; prolongation/restriction `:102-103`; `pmin` `multigrid.hpp:30-33`;
  coarse-seed `multigrid.hpp:89-90`; de-Rham complex `book/src/L0/fespace-file.md:165-169`.

D1 survey GATE consumed: `reports/2026-06-02T151056Z-cross-layer-cross-cutter-fe-space-front-survey/CYCLE.md`
(granularity verdict §3: ONE prime entry; opaque-parameter inventory §4).

## Open questions / caveats

- **Concept page — NOT authored this cycle (judged).** The FE-space-as-assembly-domain is a genuine
  cross-cutting type with 4 downstream consumers, but a concept page would be a thin mirror of the
  `fe_space` operator entry until the four re-anchors actually land — there is no cross-cutting
  *abstraction* distinct from the operator entry yet (the de-Rham-domain concept would earn one only if
  a later L2 "discrete exterior-derivative interpolator parameterized by the (domain, range) space
  pair" — flagged at `book/src/L0/fespace-file.md:165-169` — materializes and reuses it). Deferred
  candidate; logged here, not in the OQ ledger as a blocker.
- **`essential_dofs` straddles the MFEM-owned boundary** (D1 survey OQ, carried forward). The
  boundary-attribute → marker → dof-set *shape* lifts (`mesh::AttrToMarker` is Palace-side,
  `multigrid.hpp:98`), but `GetEssentialTrueDofs` is MFEM-owned dof-numbering (read-as-given). My lean
  (matching the survey's): noted-property of `fe_space` unless `eliminate_*`'s `DofSet[N]` demands a
  self-standing home. Defer to the follow-on dispatch.
- **`fe_collection` self-standing-laws check** (D1 survey OQ, carried forward). Whether the
  pmin-floor + GaussLobatto/Legendre/IntegratedGLL basis-selection laws (`multigrid.hpp:30-38`) earn a
  separate chapter vs. fold as `fe_space`'s collection-input axis — I keep the survey's fold-first,
  split-only-if-laws-justify lean; at the assembly-front altitude a single `FECollection` is just an
  input to `fe_space`. Defer.
- **Layer intro refresh** — the L1 §"Vocabulary cohort" lead-paragraph consolidated tally (firm grand
  total) is DEFERRED to D4 (count-owner this cycle). **CORRECTED at repair (cohort reconciliation):**
  `fe_space` is NOT a 5th FE-assembly member — D4 creates a SEPARATE "FE-space sub-spine — 1" subsection
  (`fe_space` CONSTRUCTS the space; FE-assembly FOLDS over it). FE-assembly STAYS 4; FE-space is a new
  sub-spine of 1; the L1 firm grand total goes 31→32 once `fe_space` lands. The `layer-intro-author` (D-?) / D4 should also note
  `fe_space` as the opened FE-space-construction front in the L1 §Context if a refresh is warranted —
  flagged, not enacted (not my authority).
- **2-D L2-curl special case** (`spaceoperator.cpp:72-75`; `INTEGRAL` map type for `B = curl E`) is a
  load-bearing variant of the de-Rham family axis — captured in the variant-axis table as the L2 row;
  does not change the granularity verdict.

