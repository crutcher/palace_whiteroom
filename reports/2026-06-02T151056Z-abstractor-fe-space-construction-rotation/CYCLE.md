---
agent: abstractor
invoked_at: 2026-06-02T15:55:00Z
scope: L1>L0 theme sketch — fe-space-construction-rotation
status: integrated
integrated_at: 2026-06-02T180000Z
integration_commit: PLACEHOLDER_SHA_CYCLE_064
integration_notes: |
  cycle-064 D3, applied clean by integrator-per-report (STAGING row 3), finalized by integrator-finalize.
  `fe-space-construction-rotation` LANDED FIRM L1>L0 (book/src/L1-L0/fe-space-construction-rotation.md —
  LHS L1 `fe_space` → RHS L0 FiniteElementSpace ctor; construction-lowers / dof-bookkeeping-MFEM-owned
  split; 4 de-Rham rewrite cases H1/ND/RT/L2). Applied: L1-L0/index.md theme row + SUMMARY chapter line.
  The forward-ref live link ../L1/fe_space.md RESOLVES (D2 landed it the prior per-report invocation);
  applied as a live link, NOT down-converted. Ctor cite fespace.hpp:67-75 consistent on disk.
  L1>L0 firm themes +1. retroactive-budget global = 0.
inputs:
  - book/src/L1/fe_space.md (D2 this-cycle harvester — fe_space prime entry; forward-ref live-link)
  - reports/2026-06-02T151056Z-cross-layer-cross-cutter-fe-space-front-survey/CYCLE.md (D1 survey — scope partition + opaque-parameter inventory)
  - palace/fem/fespace.hpp:67-75 (FiniteElementSpace variadic ctor)
  - palace/fem/multigrid.hpp:90 (ConstructFiniteElementSpaceHierarchy coarse-seed)
  - palace/models/spaceoperator.cpp:47,49,51,75 (ND/H1/RT + L2-curl de-Rham instantiation sites)
  - book/src/L0/fespace-file.md (firm L0 localization — MFEM-as-given framing + de-Rham complex)
---

# CYCLE: L1>L0 theme sketch — fe-space-construction-rotation

## Summary

The L1 `fe_space (mesh, collection) -> FiniteElementSpace[N]` construction lowers FORWARD into the
concrete Palace `FiniteElementSpace` object construction: the variadic ctor at
`palace/fem/fespace.hpp:67-75` (which forwards `(&mesh.Get(), collection)` straight into
`mfem::ParFiniteElementSpace`), instantiated at the solver build sites where the de-Rham collection
type is the template parameter — `ND_FECollection`/`H1_FECollection`/`RT_FECollection` at
`spaceoperator.cpp:47/49/51` and the 2-D L2-curl `L2_FECollection` at `:75`. This is a genuine
**vocabulary translation, not a rename**: the L1 side is a pure value (a `(mesh, collection)` pairing
that *names* an indexed function space `[N]`); the L0 side is an imperative C++ object construction
that wires up the dof numbering, element-to-dof tables, conformity, and prolongation/restriction
matrices. The KEY translation boundary — made explicit in the theme as the **construction-lowers /
dof-bookkeeping-MFEM-owned split** — is that the *construction* lowers cleanly (the ctor + the
collection-type case selection are Palace-readable), but the *dof internals* are MFEM-owned-read-as-
given (the thin `return Get().X()` accessors at `fespace.hpp:93-103` forward to
`mfem::ParFiniteElementSpace` verbatim). This is the same shape as `fe_assemble`'s libCEED-leaf
boundary (`fe-assemble-libceed-boundary-obstruction`) and `weak_form_term`'s identity-lowers/kernel-
opaque split, but here the opaque owner is MFEM dof-management rather than libCEED quadrature.
**Status: firm** — the construction is positively anchored (ctor + 4 collection sites + coarse-seed)
and the MFEM-owned boundary is documented (not a constructive reconstruction). The four de-Rham
collection cases are the variant axis.

## Proposed changes

```new:book/src/L1-L0/fe-space-construction-rotation.md
# fe-space-construction-rotation

**Slug:** `fe-space-construction-rotation`

How the pure L1 [`fe_space`](../L1/fe_space.md) construction lowers into the concrete Palace
`FiniteElementSpace` C++ object construction. This is a **vocabulary translation, not a rename**: the
L1 form is a value (a `(mesh, collection)` pairing naming a true-dof-indexed function space `[N]`);
the L0 form is an imperative ctor that constructs an `mfem::ParFiniteElementSpace`-wrapping object and
wires up the dof bookkeeping. The translation has a sharp boundary — the **construction lowers / the
dof-bookkeeping is MFEM-owned-read-as-given** — narrated in the split below.

## Status

`firm` — structural. The construction rewrite is positively anchored at L0: the variadic ctor
(`fespace.hpp:67-75`), the single-space coarse-seed construction site
(`multigrid.hpp:90`), and the four de-Rham collection-type instantiation sites
(`spaceoperator.cpp:47/49/51/75`). The dof-numbering/ordering/conformity/prolongation boundary is
**documented as MFEM-owned-read-as-given** (the thin forwarding accessors `fespace.hpp:93-103`) — it
is a witnessed library-ownership boundary, NOT a constructive reconstruction, so it does not gate
firmness (cf. the firm `weak-form-term-rotation` identity-lowers/kernel-opaque split and the firm
`fe-operator-assemble-mutation-rotation` over a libCEED-opaque leaf). MPI/`Par*` and mesh
partitioning are flagged once and read single-rank (out of scope per CLAUDE.md §Scope).

## L1 form (LHS)

The pure construction value (D2's prime entry [`L1/fe_space`](../L1/fe_space.md)):

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
list of levels) is the deferred `fe_space_hierarchy` sibling (D1 survey pick #4); a single
`fe_space(mesh, collection)` is one such `make_unique<FiniteElementSpace>(mesh, coll)`.

### The construction-lowers / dof-bookkeeping-MFEM-owned split (the translation boundary)

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
  it earns its own `fe_collection` entry is the deferred D1 granularity question.
- Single-rank reading: `mfem::ParFiniteElementSpace`/`ParMesh` are read as their serial equivalents
  (out of scope per CLAUDE.md §Scope; `book/src/L0/fespace-file.md:13-16`). Mesh PARTITIONING (the
  `Mesh` wrapper `loc_attr`/`loc_bdr_attr` remap) is out of scope — flagged once.

## Justification kind

**Structural** — the rewrite is shape-driven: the L1 value `fe_space(mesh, collection)` maps onto the
concrete `FiniteElementSpace(mesh, collection)` ctor call, with the de-Rham collection type as the
positively-anchored case axis. No algebraic law or reduction chain is needed; the boundary (what
lowers vs. what is MFEM-owned-read-as-given) is established by the thin forwarding accessors.

## Verified-against

- `palace/fem/fespace.hpp:67-75` — `FiniteElementSpace(Mesh &mesh, T &&...args)` variadic ctor
  forwarding `(&mesh.Get(), args...)` into `mfem::ParFiniteElementSpace` (verified via codemap
  read_range).
- `palace/fem/fespace.hpp:93-103` — thin MFEM-forwarding dof accessors (`GetTrueVSize` `:96`,
  `GetProlongationMatrix`/`GetRestrictionMatrix` `:102-103`) — the MFEM-owned boundary.
- `palace/fem/multigrid.hpp:90` — `make_unique<FiniteElementSpace>(*mesh[coarse_mesh_l], fecs[0].get())`
  single-space coarse-seed (the cleanest single-`fe_space` construction anchor).
- `palace/models/spaceoperator.cpp:47/49/51` — `ConstructFiniteElementSpaceHierarchy<ND/H1/RT_FECollection>`
  de-Rham instantiation sites (ctor member init); `:75` — 2-D L2-curl `L2_FECollection` site (ctor
  body `:73-79`). Full ctor body `:45-89`.
- `book/src/L0/fespace-file.md:13-16` (single-rank/MFEM-as-given reading), `:154-158`
  (dof-structure-is-MFEM's boundary), `:159-164` (transparent libCEED-cache classification),
  `:165-169` (de-Rham complex H1->H(curl)->H(div)->L2) — the firm L0 localization.
- [`L1/fe_space`](../L1/fe_space.md) — the prime L1 entry this theme lowers (D2 this-cycle).

## Open questions / caveats

- **Lifting note (reverse direction, working-note only).** The L0 ctor lifts to L1 `fe_space`
  cleanly precisely because the dof internals are read-as-given — the lift discards the MFEM index
  bookkeeping and retains only the `(mesh, collection) -> [N]` shape. The additional structure the
  lift would need to be *complete* (rather than opaque) is the dof-numbering algebra, which is MFEM's
  and out of scope. (High->low formal content stays in the chapter above; this is a working note.)
- **`fe_collection` / order-schedule upstream.** `ConstructFECollections` (`multigrid.hpp:22-75`)
  produces the `collection` input via the pmin floor + basis-type + coarsening schedule. Whether it
  earns a separate `fe_collection` L1 entry (+ its own L1>L0 theme) is the deferred D1 granularity
  question — for this theme, `collection` is a given input.
- **`essential_dofs` straddle.** The boundary-attribute -> essential-true-dof-set extraction
  (`GetEssentialTrueDofs` ∘ `AttrToMarker`, `multigrid.hpp:97-99`) is a derived projection off the
  constructed space; the attribute->marker shape is Palace-side but `GetEssentialTrueDofs` is
  MFEM-owned dof-numbering. Per D1, lean is noted-property of `fe_space`, not a separate theme — it is
  the `DofSet[N]` the `eliminate_*` cohort takes opaquely. Out of scope for this construction theme.
- **Forward-reference resolution.** `L1/fe_space.md` (D2) and the `fe_space_hierarchy` /
  `fe_collection` siblings are this-cycle / deferred; the live-link to `fe_space` resolves once D2's
  entry lands this cycle.
```

Append ONE table row to the §Theme list, immediately AFTER the existing
`weak-form-term-rotation` row (currently the last theme row). Anchor on the trailing portion of that
row so the insert is parallel-safe; the consolidated firm-count tally is DEFERRED to D4
(layer-intro-author, the L1-L0 count-owner this cycle). The L1-L0 index has no §Vocabulary-cohort
bulleted sub-grouping section (it is a flat theme list), so there is no own-cohort bullet to add —
the row + the SUMMARY line are this theme's full self-owned registration.

```edit:book/src/L1-L0/index.md
| [weak-form-term-rotation](./weak-form-term-rotation.md) | [`L1/weak_form_term`](../L1/weak_form_term.md) (firm c061) | `palace/fem/bilinearform.hpp:53-57` (`AddDomainIntegrator<T>(Q)` instantiation), `palace/fem/integrator.hpp:39-130` (wrapper layer), `palace/models/laplaceoperator.cpp:188-194` (Gradient/diffusion witness), `palace/models/curlcurloperator.cpp:170-181` (Curl/curl-curl witness) | firm *(structural; vocabulary-translation — pure `(coefficient, differential-operator)` pair → C++ template-type `T` (diff-op, compile-time) + runtime-arg `Q` (coefficient) dispatch into mutable owned `domain_integs` container; **identity-lowers / kernel-opaque split** — term IDENTITY (which `Q`, which `𝒟`) Palace-readable at the `AddDomainIntegrator<T>(Q)` site and lowers HERE, term KERNEL (`Assemble` quadrature) is the libCEED `opaque-library-ownership` boundary `fe-assemble-libceed-boundary-obstruction` c055, lowers ELSEWHERE; 2 grounded rewrite cases Gradient/`DiffusionIntegrator(epsilon_func)` `laplaceoperator.cpp:191-194` + Curl/`CurlCurlIntegrator(muinv_func)` `curlcurloperator.cpp:179-181` (same `BilinearForm`-fold, integrator-slot-only difference); mass/`Identity` + div-div/`Divergence` named pending-pull axis points NOT authored; container build-up is the sibling `fe-operator-assemble-mutation-rotation` c057; firm-on-positive-structure)* |
| [fe-space-construction-rotation](./fe-space-construction-rotation.md) | [`L1/fe_space`](../L1/fe_space.md) (firm c064) | `palace/fem/fespace.hpp:67-75` (variadic ctor) + `:93-103` (MFEM-forwarding dof accessors), `palace/fem/multigrid.hpp:90` (single-space coarse-seed), `palace/models/spaceoperator.cpp:47/49/51/75` (de-Rham instantiation sites) | firm *(structural; vocabulary-translation — pure `(mesh, collection) → FiniteElementSpace[N]` value → imperative `mfem::ParFiniteElementSpace`-wrapping ctor; **construction-lowers / dof-bookkeeping-MFEM-owned split** — the `(mesh, collection)` pairing + de-Rham case selection + `ResetCeedObjects` cache-init lower HERE at the ctor `fespace.hpp:67-75`, the dof/vdof numbering + ordering + conformity + prolongation/restriction matrices are MFEM-owned-read-as-given via thin forwarding accessors `fespace.hpp:93-103` (analogue of the libCEED-leaf boundary but MFEM-dof-management-owned, not libCEED-quadrature); 4 de-Rham rewrite cases H1/`H1_FECollection` `:49` + H(curl)/`ND_FECollection` `:47` + H(div)/`RT_FECollection` `:51` + L2/`L2_FECollection` `:75` (2-D-curl INTEGRAL-map load-bearing variant); single-space coarse-seed `multigrid.hpp:90`; hierarchy/`fe_collection` deferred siblings; MPI/`Par*` + mesh-partitioning out-of-scope single-rank; firm-on-positive-structure)* |
```

```edit:book/src/SUMMARY.md
Append ONE chapter entry under the `# L1 > L0 — Lowering` Part, after the existing
`weak-form-term-rotation` line (line 149):

- [weak-form-term-rotation](./L1-L0/weak-form-term-rotation.md)
- [fe-space-construction-rotation](./L1-L0/fe-space-construction-rotation.md)
```

## Speculative operators proposed

None. This theme lowers the existing this-cycle L1 entry [`L1/fe_space`](../../book/src/L1/fe_space.md)
(D2 harvester); it does not introduce new speculative L1 operators. The construction's collection
input is produced by the upstream `fe_collection` order-schedule (`ConstructFECollections`) and the
hierarchy by `fe_space_hierarchy` (`ConstructFiniteElementSpaceHierarchy`), both **deferred** to
follow-on dispatch per the D1 survey granularity verdict (NOT proposed here, not as rough-in rows
either — they are named pending-pull siblings, not forward-referenced operators this theme depends
on).

## Supporting evidence

- `palace/fem/fespace.hpp:67-75` — `FiniteElementSpace(Mesh &mesh, T &&...args)` variadic ctor;
  `: fespace(&mesh.Get(), std::forward<T>(args)...)` forwards the `(mesh, collection)` pair into
  `mfem::ParFiniteElementSpace` (verified via codemap read_range — the construction RHS).
- `palace/fem/fespace.hpp:93-103` — thin MFEM-forwarding dof accessors: `GetTrueVSize` `:96`,
  `GetProlongationMatrix`/`GetRestrictionMatrix` `:102-103`, all `return Get().X()` — the
  MFEM-owned-read-as-given boundary (the dof-bookkeeping half of the split).
- `palace/fem/multigrid.hpp:90` — `make_unique<FiniteElementSpace>(*mesh[coarse_mesh_l], fecs[0].get())`
  single-space coarse-seed — the cleanest single-`fe_space(mesh, collection)` construction anchor
  (inside `ConstructFiniteElementSpaceHierarchy`, ctor decl `:78-82`).
- `palace/models/spaceoperator.cpp:45-89` — `SpaceOperator` ctor; the de-Rham instantiation sites:
  `ND_FECollection` `:47`, `H1_FECollection` `:49`, `RT_FECollection` `:51` (member init), and the
  2-D L2-curl `L2_FECollection` `:75` (ctor body `:73-79`, INTEGRAL map type) — the 4 variant rewrite
  cases (all verified via codemap read_range).
- `book/src/L0/fespace-file.md` — firm L0 localization: single-rank/MFEM-as-given `:13-16`,
  dof-structure-is-MFEM's `:154-158`, transparent libCEED-cache `:159-164`, de-Rham complex
  `:165-169`.
- `reports/2026-06-02T151056Z-cross-layer-cross-cutter-fe-space-front-survey/CYCLE.md` — D1 survey:
  scope partition (§1), granularity verdict (§3), opaque-parameter inventory (§4).
- [`L1/fe_space`](../../book/src/L1/fe_space.md) — D2 this-cycle prime L1 entry (the LHS this theme
  lowers; live-link resolves once D2 lands this cycle).

## Open questions / caveats

- **D2's `fe_space.md` lands same-cycle.** I authored against the D1 survey's recommended signature
  `fe_space :: (mesh: Mesh, collection: FECollection) -> FiniteElementSpace[N]` and the canonical slug
  `fe_space` the planner stated for D2. If D2's landed entry diverges in signature or variant-axis
  framing, the integrator should reconcile the LHS reference (the live-link `[`L1/fe_space`]` is to the
  planner-stated canonical slug, per the cross-report forward-reference convention).
- **Count-ownership.** The consolidated L1-L0 firm-count tally / growth-log is DEFERRED to D4
  (layer-intro-author, the count-owner this cycle). I registered only my own table row + SUMMARY line
  (the L1-L0 index has no §Vocabulary-cohort bulleted section, so there is no own-cohort bullet to
  add).
- **`essential_dofs` / `fe_collection` / `fe_space_hierarchy`** are deferred siblings (D1 picks #2/#3/#4),
  not part of this construction theme. `essential_dofs` straddles the MFEM-owned boundary
  (`GetEssentialTrueDofs` is MFEM dof-numbering); D1's lean is noted-property of `fe_space`.
- **Slug-collision check:** `fe-space-construction-rotation` is distinct from the existing
  `fe-operator-assemble-mutation-rotation` (assembly of the operator OVER the space) and
  `weak-form-term-rotation` (the per-term integrator). This theme is the construction of the space
  itself — the shared substrate those two operate on. No collision.
