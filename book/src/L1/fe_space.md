---
layer: L1
operator: fe_space
harvested_by: harvester:2026-06-02T151056Z-harvester-fe-space
cycle: cycle-064
# Graded-stack scheme (edges authored from scratch, batch-36 c114; chapter previously carried only
# `status: firm`, NO edges). This firm L1 construction composes its one firm L1 input — the
# `collection: FECollection`, produced by `fe_collection` — and rests on its positive L0 ctor source
# (cites-evidence, rank-terminal ground truth) + lowers through its L1>L0 construction-rotation theme.
# The `composes` edge to `fe_collection` flips it reachable (firm-but-currently-garbage); `fe_space`
# itself flips reachable transitively via `fe_assemble`'s c114 `composes` edge (sibling D1 migration).
# Well-foundedness rank(u) <= rank(v): this node firm (rank 3); `fe_collection` carries `rank: firm`
# (status: firm, cycle-065); the cites-evidence target is rank-terminal L0 ground truth; the lowering
# theme `fe-space-construction-rotation` is `status: firm` (rank 3 <= 3).
rank: firm
edges:
  depends-on:
    - target: L1/fe_collection
      kind: composes              # the `collection: FECollection` input, produced by fe_collection (sig :9/:43; §Variant-axis :89)
    - target: palace/fem/fespace.hpp:67-75
      kind: cites-evidence        # the variadic `FiniteElementSpace(Mesh&, T&&...)` ctor — the (mesh,collection) pairing (Evidence :191-193)
    - target: L1-L0/fe-space-construction-rotation
      kind: lowers-to             # the L1>L0 construction-rotation theme (cycle-064 D3; §Downward :145)
  reference:
    - L1/fe_assemble               # the primary consumer of the constructed space
    - L1/weak_form_term
    - L1/eliminate_essential_bc
    - L1/eliminate_rhs
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
theme [`fe-space-construction-rotation`](../L1-L0/fe-space-construction-rotation.md) (authored cycle-064 D3).

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

The **collection order schedule** itself (`ConstructFECollections`, `palace/fem/multigrid.hpp:22-73`)
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

The L1>L0 rotation [`fe-space-construction-rotation`](../L1-L0/fe-space-construction-rotation.md)
(cycle-064 D3) narrates how the typed
`(mesh, collection) → FiniteElementSpace[N]` construction rewrites into the L0 variadic ctor
(`fespace.hpp:67-75`) forwarding into `mfem::ParFiniteElementSpace`, and into the
`ConstructFiniteElementSpaceHierarchy` coarse-seed (`multigrid.hpp:89-90`) + `GetEssentialTrueDofs`
extraction (`multigrid.hpp:98-99`, via `mesh::AttrToMarker` `:97-98`).

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
`ConstructFECollections` order schedule — `multigrid.hpp:22-73`), `essential_dofs` (the
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
- `palace/fem/multigrid.hpp:22-73` — `ConstructFECollections` (the deferred order-schedule context):
  `pmin` floor (`:30-33`), basis-type choice (`:34-38`).
- `book/src/L0/fespace-file.md` — the firm L0 localization: MFEM-as-given framing (`:18-25,150-158`),
  the de-Rham complex H1 →∇ H(curl) →∇× H(div) →∇· L2 (`:165-169`), the transparent libCEED-cache
  classification.
- `book/src/L1/fe_assemble.md:60` — `space: FiniteElementSpace[N]` opaque input;
  `book/src/L1/weak_form_term.md:79` — `A(space, ·)` over opaque `space`;
  `book/src/L1/eliminate_essential_bc.md:63` — `dofs: DofSet[N]`, `N = space.GetTrueVSize()`;
  `book/src/L1/eliminate_rhs.md:67` — `dbc_tdof_list` masking over the opaque dof set.
