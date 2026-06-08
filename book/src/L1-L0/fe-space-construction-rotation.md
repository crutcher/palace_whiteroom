# fe-space-construction-rotation

**Slug:** `fe-space-construction-rotation`

How the pure L1 [`fe_space`](../L1/fe_space.md) construction lowers into the concrete Palace
`FiniteElementSpace` C++ object construction. This is a **vocabulary translation, not a rename**: the
L1 form is a value (a `(mesh, collection)` pairing naming a true-dof-indexed function space `[N]`);
the L0 form is an imperative ctor that constructs an `mfem::ParFiniteElementSpace`-wrapping object and
wires up the dof bookkeeping. The translation has a sharp boundary — the **construction lowers / the
dof-bookkeeping is MFEM-owned-read-as-given** — narrated in the split below.

The dof-numbering/ordering/conformity/prolongation boundary is **MFEM-owned-read-as-given** (the thin
forwarding accessors `fespace.hpp:93-103`) — a witnessed library-ownership boundary, NOT a constructive
reconstruction (cf. the firm `weak-form-term-rotation` identity-lowers/kernel-opaque split and the firm
`fe-operator-assemble-mutation-rotation` over a libCEED-opaque leaf). MPI/`Par*` and mesh partitioning
are flagged once and read single-rank (out of scope per CLAUDE.md §Scope).

## L1 form (LHS)

The pure construction value ([`L1/fe_space`](../L1/fe_space.md)):

    fe_space :: (mesh: Mesh, collection: FECollection) -> FiniteElementSpace[N]

`FiniteElementSpace[N]` is the typed domain/range object of the FE-assembly map, indexed by its
true-dof count `N = GetTrueVSize()`. The de-Rham family (H1 / H(curl) / H(div) / L2) is carried by
the `collection` argument's variant axis. At L1 this is a referentially-transparent pairing: given the
same `(mesh, collection)`, `fe_space` names the same indexed space; the dof structure is an opaque
property of the value (the index axis `N`), not a separate operation.

## L0 form (RHS)

The concrete C++ object construction. The Palace-side ctor is the single rewrite target; it forwards
the `(mesh, collection)` pair into MFEM:

    // palace/fem/fespace.hpp:67-75
    template <typename... T>
    FiniteElementSpace(Mesh &mesh, T &&...args)
      : fespace(&mesh.Get(), std::forward<T>(args)...), mesh(mesh), aux_fespace(nullptr)
    { ResetCeedObjects(); tx.UseDevice(true); lx.UseDevice(true); ly.UseDevice(true); }

The single-space construction is exercised at the multigrid coarse-seed
(`multigrid.hpp:90`), which is the cleanest single-`fe_space` anchor:

    // palace/fem/multigrid.hpp:90 (inside ConstructFiniteElementSpaceHierarchy)
    FiniteElementSpaceHierarchy fespaces(
        std::make_unique<FiniteElementSpace>(*mesh[coarse_mesh_l], fecs[0].get()));

i.e. `FiniteElementSpace(mesh, collection)` with `collection = fecs[0]`. The hierarchy wrapping (the
list of levels) is the deferred `fe_space_hierarchy` sibling; a single
`fe_space(mesh, collection)` is one such `make_unique<FiniteElementSpace>(mesh, coll)`.

### The construction-lowers / dof-bookkeeping-MFEM-owned split

*The translation boundary.*

The translation is sharp on one line of the ctor: `fespace(&mesh.Get(), ...args)`.

- **LOWERS HERE (Palace-readable construction).** The pairing of a mesh with a collection, the
  collection-type case selection (the de-Rham variant axis below), the `ResetCeedObjects()` cache
  initialization (a transparent-performance annotation, already classified
  `book/src/L0/fespace-file.md:159-164`), and the `tx/lx/ly` workspace `UseDevice(true)` (device
  placement, transparent). The L1 `fe_space` value's *construction* is exactly this ctor call.
- **MFEM-OWNED-READ-AS-GIVEN (does NOT lower here).** dof/vdof numbering, byNODES/byVDIM ordering,
  element-to-dof tables, conformity, and the prolongation/restriction matrices are produced inside
  `mfem::ParFiniteElementSpace` and exposed by the thin forwarding accessors `fespace.hpp:93-103`
  (`GetTrueVSize`/`GetVDim`/`GetProlongationMatrix`/`GetRestrictionMatrix` all `return Get().X()`).
  These are read as given — the L1 `fe_space` treats the space as an **opaque index structure with a
  known true-dof count `N` and a true-dof <-> L-vector transfer** (`GetProlongationMatrix`). The L0
  chapter already frames this boundary: `book/src/L0/fespace-file.md:154-158` ("The dof structure is
  MFEM's; the lift reads it as given.").

This split is the analogue, at the FE-space-construction altitude, of the libCEED-leaf boundary in
[`fe-assemble-libceed-boundary-obstruction`](./fe-assemble-libceed-boundary-obstruction.md) and the
kernel-opaque half of [`weak-form-term-rotation`](./weak-form-term-rotation.md): the *shell*
(construction / case selection) is Palace-owned and lowers; the *numerical/index internals* are
library-owned and read-as-given. Unlike those two, the opaque owner here is **MFEM dof-management**,
not libCEED quadrature. The boundary does not downgrade the theme — the construction is positively
anchored and firm (cf. firm-on-positive-structure precedent).

### Variant axis — the de-Rham family (4 collection-type rewrite cases)

The construction is identical across the de-Rham family modulo the `FECollection` subclass passed as
the `collection` argument. Each L1 `collection` variant rewrites to a concrete MFEM FECollection
subclass at its solver instantiation site (`spaceoperator.cpp`, the `SpaceOperator` ctor body
`:45-89`):

| L1 `collection` (de-Rham space) | L0 FECollection subclass | instantiation site | map type |
|---|---|---|---|
| H1 (nodal scalar, VALUE) | `mfem::H1_FECollection` | `spaceoperator.cpp:49` | VALUE |
| H(curl) (edge / Nedelec) | `mfem::ND_FECollection` | `spaceoperator.cpp:47` | H_CURL |
| H(div) (face / Raviart-Thomas) | `mfem::RT_FECollection` | `spaceoperator.cpp:51` | H_DIV |
| L2 (discontinuous, INTEGRAL) | `mfem::L2_FECollection` | `spaceoperator.cpp:75` | INTEGRAL |

The four sites are the template parameter to `ConstructFiniteElementSpaceHierarchy<FECollection>`
(which coarse-seeds via the `FiniteElementSpace(mesh, collection)` ctor at `multigrid.hpp:90`):

    // palace/models/spaceoperator.cpp:47,49,51 (SpaceOperator ctor member init)
    nd_fespaces(fem::ConstructFiniteElementSpaceHierarchy<mfem::ND_FECollection>(...)),  // :47
    h1_fespaces(fem::ConstructFiniteElementSpaceHierarchy<mfem::H1_FECollection>(...)),  // :49
    rt_fespaces(fem::ConstructFiniteElementSpaceHierarchy<mfem::RT_FECollection>(...)),  // :51

    // palace/models/spaceoperator.cpp:75 (2-D L2-curl special case, in ctor body)
    fem::ConstructFiniteElementSpaceHierarchy<mfem::L2_FECollection>(1, mesh, l2_curl_fecs)

The **2-D L2-curl case** (`spaceoperator.cpp:73-79`) is a load-bearing variant of the L2 rewrite: in
2-D, `curl: H(curl) -> L2` (scalar), so the curl target needs an `L2_FECollection` built with
`INTEGRAL` map type (`spaceoperator.cpp:75`) so the discrete interpolator recognizes it as the curl
target. The L1 framing: this is the L2-collection variant instantiated with the INTEGRAL map type;
the construction rewrite is identical, only the collection argument differs. The de-Rham complex
itself (H1 -grad-> H(curl) -curl-> H(div) -div-> L2) is already named at
`book/src/L0/fespace-file.md:165-169`.

## Applicability conditions

- The rewrite applies to the single-space construction `fe_space(mesh, collection)`. The
  *hierarchy*-producing form (`ConstructFiniteElementSpaceHierarchy` building a list of levels for
  p/h-multigrid) is the deferred `fe_space_hierarchy` sibling — each level IS a `fe_space(mesh_l,
  coll_l)` construction, so this theme is the per-level rewrite the hierarchy iterates.
- `collection` must be one of the four de-Rham FECollection subclasses (the variant axis). The
  collection *order schedule* (`ConstructFECollections`, `multigrid.hpp:22-75`: pmin floor, basis
  type, LINEAR/LOG coarsening) is upstream of this theme — it produces the `collection` input; whether
  it earns its own `fe_collection` entry is a deferred granularity question.
- Single-rank reading: `mfem::ParFiniteElementSpace`/`ParMesh` are read as their serial equivalents
  (out of scope per CLAUDE.md §Scope; `book/src/L0/fespace-file.md:13-16`). Mesh PARTITIONING (the
  `Mesh` wrapper `loc_attr`/`loc_bdr_attr` remap) is out of scope — flagged once.

## Justification kind

**Structural** — the rewrite is shape-driven: the L1 value `fe_space(mesh, collection)` maps onto the
concrete `FiniteElementSpace(mesh, collection)` ctor call, with the de-Rham collection type as the
positively-anchored case axis. No algebraic law or reduction chain is needed; the boundary (what
lowers vs. what is MFEM-owned-read-as-given) is established by the thin forwarding accessors.

## Adjacent constructions (out of this theme's scope)

- **`fe_collection` / order-schedule upstream.** `ConstructFECollections` (`multigrid.hpp:22-75`)
  produces the `collection` input via the pmin floor + basis-type + coarsening schedule. For this
  theme, `collection` is a given input; the schedule's own rewrite is
  [`fe-collection-construction-rotation`](./fe-collection-construction-rotation.md).
- **`essential_dofs` straddle.** The boundary-attribute → essential-true-dof-set extraction
  (`GetEssentialTrueDofs` ∘ `AttrToMarker`, `multigrid.hpp:97-99`) is a derived projection off the
  constructed space; the attribute→marker shape is Palace-side but `GetEssentialTrueDofs` is
  MFEM-owned dof-numbering. It is a noted-property of `fe_space`, not a separate theme — the
  `DofSet[N]` the `eliminate_*` cohort takes opaquely. Out of scope for this construction theme.

## Status

`firm` — structural; the construction rewrite is positively anchored at L0.
