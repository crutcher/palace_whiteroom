---
agent: abstractor
invoked_at: 2026-06-06T232937Z
scope: L1>L0 theme sketch — build-mesh-construction-rotation
status: integrated
integrated_at: 2026-06-07T003000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean as c118 D1 (batch-38 opener, mesh→fe_space substrate campaign). New firm L1>L0 theme build-mesh-construction-rotation.md + build_mesh reference→depends-on(lowers-to) edge. cargo make book EXIT 0; graded-stack rank_violations=0; reachable 136→139 (build_mesh grounded by D4, this theme flips reachable). 0 gate hits."
inputs:
  - book/src/L1/build_mesh.md (firm c117 — the upper endpoint; the named-not-authored Downward note at :178-186)
  - palace/main.cpp:285-302 (the mesh block of main — the build referent)
  - palace/utils/geodata.cpp:122-143 (mesh::Load body) / :262-290 (mesh::Partition) / :421-455 (mesh::RefineMesh)
  - palace/utils/geodata.hpp:25-50 (the four mesh:: stage declarations + contracts)
  - palace/fem/mesh.hpp:44-115 (class Mesh wrapper; ctor chain :76-81; EnsureNodes/Update :79-80)
  - book/src/L1-L0/{fe-space,essential-dofs}-construction-rotation.md (sibling construction-rotation precedent + typed-edge frontmatter shape)
---

# CYCLE: L1>L0 theme sketch — build-mesh-construction-rotation

## Summary

This dispatch authors the firm L1>L0 construction-rotation theme `build-mesh-construction-rotation`,
grounding the c117 firm `L1/build_mesh` operator's named-not-authored Downward note. The theme narrates
how the typed pure construction `build_mesh :: Config -> Mesh` lowers into the L0 imperative C++
free-function chain inside the mesh block of `main` (`palace/main.cpp:285-302`):
`mesh::Load` ▷ `solver->Preprocess` ▷ `mesh::Partition` (read single-rank) ▷ `mesh::RefineMesh` ▷
`make_unique<Mesh>`. This is a genuine **vocabulary translation, not a rename**: the L1 form is a
referentially-transparent `config → Mesh` value-pipeline; the L0 form is a sequence of free functions
that *consume-and-return* and *mutate-in-place* `unique_ptr` mesh handles — three distinct handle types
(`unique_ptr<mfem::Mesh>` serial → `vector<unique_ptr<mfem::ParMesh>>` parallel level-vector →
`vector<unique_ptr<Mesh>>` wrapped), with `RefineMesh` growing the parallel level-vector **in place**
and the `Mesh` adopting-ctor running `EnsureNodes()` + `Update()` as construction finalization. The
translation has a sharp boundary mirroring its sibling `fe-space-construction-rotation`: the
**pipeline-staging + handle-ownership-threading lowers HERE (Palace-authored)**, while the per-stage
geometric kernels (`UniformRefinement`, the MFEM partitioner, `EnsureNodes`) are
**MFEM-owned-read-as-given**. The partition/distribute aspect is flagged-once-and-skipped per §Scope
(single-rank = identity distribution). Status: `firm` (firm-on-positive-structure — every translation
piece is a syntactic identity on positive source).

The dispatch also bundles the COUPLED RE-ANCHOR: upgrading `L1/build_mesh`'s
`reference → L1-L0/build-mesh-construction-rotation` edge to `depends-on (kind: lowers-to)` and
replacing the "no `lowers-to` edge asserted yet" prose, since the lower endpoint now exists.

## Proposed changes

```new:book/src/L1-L0/build-mesh-construction-rotation.md
---
# Lowering theme. Per graded-stack scheme §5: rank = min(endpoint ranks). The L1
# endpoint (build_mesh) is firm (rank 3); the L0 endpoint is rank-terminal ground
# truth. So the theme is firm and rank(theme) <= min(endpoints) holds for free.
rank: firm
edges:
  depends-on:
    - target: L1/build_mesh
      kind: lowers-to             # the L1 source construction this theme lowers
    - target: palace/main.cpp:285-302
      kind: cites-evidence        # the mesh block of main: Load -> Preprocess -> Partition -> RefineMesh -> wrap
    - target: palace/utils/geodata.cpp:421-455
      kind: cites-evidence        # mesh::RefineMesh body: in-place growth of the parallel level-vector
    - target: palace/fem/mesh.hpp:76-81
      kind: cites-evidence        # the unique_ptr-adopting Mesh ctor: EnsureNodes()+Update() finalization
    - target: palace/utils/geodata.hpp:25-50
      kind: cites-evidence        # the four mesh:: stage declarations + contracts
  reference:
    - L1-L0/fe-space-construction-rotation        # sibling construction-lowers/kernel-MFEM-owned split (FE-space sub-spine)
    - L1-L0/essential-dofs-construction-rotation  # sibling construction-head-lowers/tail-MFEM-owned split
---

# build-mesh-construction-rotation

**Slug:** `build-mesh-construction-rotation`

How the pure L1 [`build_mesh`](../L1/build_mesh.md) construction lowers into the concrete Palace mesh
block of `main` (`palace/main.cpp:285-302`). This is a **vocabulary translation, not a rename**: the L1
form is a *value* — a referentially-transparent `config → Mesh` pipeline naming the discretised
computational domain — while the L0 form is an *imperative chain of free functions* that consume-and-return
and mutate-in-place `unique_ptr` mesh handles of three successive types, finishing by *constructing* a
Palace [`Mesh`](../L1/build_mesh.md#record-definition) wrapper whose adopting ctor runs the
`EnsureNodes()` + `Update()` geometry/attribute finalization. The translation has a sharp boundary — the
**pipeline staging + handle-ownership threading lowers HERE (Palace-authored), while each stage's
geometric kernel is MFEM-owned-read-as-given** — narrated in the split below. This is the
domain-construction analogue of the FE-space sub-spine's `fe-space-construction-rotation` /
`essential-dofs-construction-rotation` siblings (construction-lowers / library-owned-kernel-as-given).

## Status

`firm` — structural (firm-on-positive-structure). The construction rewrite is positively anchored at L0:
the mesh block of `main` (`palace/main.cpp:285-302`) gives the four-stage chain + the wrap loop; the four
`mesh::` stage declarations + contracts are at `palace/utils/geodata.hpp:25-50`; the in-place level-vector
growth is the `mesh::RefineMesh` body (`palace/utils/geodata.cpp:421-455`); the construction finalization
is the `unique_ptr`-adopting `Mesh` ctor (`palace/fem/mesh.hpp:76-81`, the `EnsureNodes()`+`Update()` at
`:79-80`). Every translation piece is a **syntactic identity on positive source** (handle-threading
ownership transfer, in-place level-vector growth, ctor-finalization) — there is no convergence/iteration
semantics to test-gate (the a-priori refinement *depth* is a fixed config field, not an adaptively-driven
loop), so the absence of a dedicated mesh-construction unit test does not gate firm (the
`fe-space-construction-rotation` c064 / `fe-collection-construction-rotation` c065 /
`essential-dofs-construction-rotation` c066 no-dedicated-test precedent). The per-stage geometric kernels
(`UniformRefinement`, the MFEM `MeshPartitioner`, `EnsureNodes`) are **MFEM-owned-read-as-given** — a
witnessed library-ownership boundary, NOT a constructive reconstruction, so it does not gate firmness (the
same posture the FE-space siblings take toward dof bookkeeping / element quadrature). MPI/`Par*` and mesh
partitioning/distribution are flagged once and read single-rank (out of scope per CLAUDE.md §Scope).

## L1 form (LHS)

The pure construction value (the c117 firm prime entry [`build_mesh`](../L1/build_mesh.md)):

    build_mesh :: Config -> Mesh

`Mesh` is the discretised computational domain — a single-rank `mfem::ParMesh` augmented with the libCEED
local-attribute mapping (see [`Mesh` record definition](../L1/build_mesh.md#record-definition)). At L1 this
is the ordered composition of four pure stages — **load ▷ preprocess ▷ partition ▷ a-priori-refine** —
each a pure function of the prior stage's mesh value:

    build_mesh config =
      let smesh = load config            -- read serial mesh + all serial-stage prep
          smesh' = preprocess config smesh   -- problem-type-specific serial preprocessing
          pmesh  = partition config smesh'   -- single-rank: the identity distribution (see Scope)
          levels = refine config pmesh       -- a-priori uniform refinement -> level-mesh sequence
      in  wrap levels                     -- the Palace Mesh wrapper (finalized geometry + attr maps)

At L1 the staging is referentially transparent: given the same `config`, `build_mesh` names the same
`Mesh` (same geometry, same `Dimension`/`SpaceDimension`/`GetNE`/`GetNBE`, same attribute maps — the c117
construction-determinism + pipeline-staging laws). There are **no mutable handles** at this layer — each
stage takes a value and returns a value; the constructed `Mesh` is an immutable typed object.

## L0 form (RHS)

The concrete C++ chain — the mesh block of `main` (`palace/main.cpp:285-302`). The four pure stages become
four free-function calls threading three successive `unique_ptr` handle types, ending in a wrap loop:

    // palace/main.cpp:285-301
    std::vector<std::unique_ptr<Mesh>> mesh;
    {
      auto smesh = mesh::Load(iodata, world_comm);                 // :287  unique_ptr<mfem::Mesh>
      solver->Preprocess(iodata, smesh, world_comm);               // :288  mutates *smesh in place
      std::vector<std::unique_ptr<mfem::ParMesh>> mfem_mesh;       // :289  the parallel level-vector
      mfem_mesh.push_back(mesh::Partition(iodata, std::move(smesh), world_comm));  // :290  consume smesh -> pmesh
      mesh::RefineMesh(iodata, mfem_mesh);                         // :291  grow mfem_mesh IN PLACE
      // ... memory reporting ...
      for (auto &m : mfem_mesh)                                    // :297  wrap each level
      {
        mesh.push_back(std::make_unique<Mesh>(std::move(m)));      // :299  adopt -> EnsureNodes()+Update()
      }
    }

Each line maps to one L1 stage (or the wrap), but the *vocabulary* is entirely different — value-pipeline →
imperative handle-threading. The four translation pieces below are where the shift actually lives.

### Piece 1 — value-pipeline → handle-ownership threading (three successive `unique_ptr` types)

The L1 `let`-chain of values becomes a chain of `unique_ptr` handles whose **ownership is transferred by
`std::move`** between stages:

- `mesh::Load(iodata, world_comm)` returns `std::unique_ptr<mfem::Mesh>` (the serial handle `smesh`,
  `palace/main.cpp:287`; signature `palace/utils/geodata.hpp:31`). The L1 `load` *plus* its serial-stage
  prep (AMR-compat checks, cleanup, simplex/hex conversion, element reordering, serial uniform refinement,
  the box/sphere **region** refinement, boundary cracking, finalization) is all inside `Load`'s contract
  (`palace/utils/geodata.hpp:25-31`).
- `solver->Preprocess(iodata, smesh, world_comm)` (`palace/main.cpp:288`) is the L1 `preprocess` — it
  takes `smesh` **by reference** and *mutates `*smesh` in place* (e.g. boundary-mode submesh extraction);
  this is the value→reference-mutation shift for the preprocess stage (the handle is not reassigned, the
  pointee is mutated).
- `mesh::Partition(iodata, std::move(smesh), ...)` (`palace/main.cpp:290`; signature
  `palace/utils/geodata.hpp:33-36`) **consumes** `smesh` (sink by value: `std::unique_ptr<mfem::Mesh>
  smesh` parameter) and **returns** a fresh `std::unique_ptr<mfem::ParMesh>` — the value→value stage with
  an ownership *transfer* (after the `std::move`, `smesh` is null). The returned parallel handle is
  `push_back`ed as the single seed of the parallel level-vector `mfem_mesh`.
- `mesh::RefineMesh(iodata, mfem_mesh)` (`palace/main.cpp:291`; signature `palace/utils/geodata.hpp:45-50`)
  takes the level-vector **by mutable reference** and grows it in place (Piece 2).

The L1 form has no handle nulling, no `std::move`, no by-reference mutation — those are the L0
realization of value-threading on a non-GC'd single-machine target. They carry **no algebraic content**
(the ownership discipline is a C++ memory-management artifact), so they lower as a documented mechanical
shift, not as L1 laws.

### Piece 2 — in-place growth of the parallel level-vector (`mesh::RefineMesh`)

The L1 `refine config pmesh -> levels` (a value producing the ordered level-mesh sequence) lowers into
`mesh::RefineMesh` **mutating its `std::vector<std::unique_ptr<mfem::ParMesh>> &mesh` argument in place**
(`palace/utils/geodata.cpp:421-455`):

    // palace/utils/geodata.cpp:421-455 (mesh::RefineMesh)
    MFEM_VERIFY(mesh.size() == 1, "...");                  // :424-425  single-mesh-in precondition
    int uniform_ref_levels = iodata.model.refinement.uniform_ref_levels;  // :426
    if (iodata.solver.linear.mg_use_mesh && ...mg_max_levels > 1)
    {
      mesh.reserve(1 + uniform_ref_levels);               // :429  pre-grow capacity (mg level-stack)
    }
    // ...
    for (int l = 0; l < uniform_ref_levels; l++)          // :448  a-priori refinement loop
    {
      if (mesh.capacity() > 1)
      {
        mesh.emplace_back(std::make_unique<mfem::ParMesh>(*mesh.back()));  // :452  push a copy of the finest
      }
      mesh.back()->UniformRefinement();                   // :454  refine in place (MFEM-owned kernel)
    }

The translation pieces:

- The L1 *return-a-sequence* becomes an **in-place mutable-reference grow** — `mesh.reserve` (`:429`),
  `mesh.emplace_back` (`:452`), `mesh.back()->UniformRefinement()` (`:454`) all mutate the caller's
  `mfem_mesh` vector. This is the load-bearing in-place `unique_ptr`-handle mutation the theme exists to
  document: the level-vector that the L1 form treats as a returned value is grown in place at L0.
- **Zero-refinement identity** (c117 build_mesh law 3): with `uniform_ref_levels == 0` the loop `:448`
  does not execute and the vector keeps its single partitioned entry — the refine stage is the identity on
  the partitioned mesh. **Level-monotonicity** (c117 law 4): with `uniform_ref_levels = k`, the vector is
  the ordered coarse→fine level stack (the geometric-multigrid stack, head = coarse), per the contract
  `palace/utils/geodata.hpp:47-49`.
- `UniformRefinement()` (`:454`) is the **MFEM-owned geometric kernel** — read-as-given (the same boundary
  posture the FE-space siblings take). What lowers HERE is the *loop structure + in-place vector growth*;
  the element-subdivision kernel is library-owned. Note `RefineMesh` performs **parallel uniform
  refinement only** — the box/sphere **region** refinement happens earlier inside `Load` on the serial
  mesh (in-body comment `palace/utils/geodata.cpp:423`), so this stage is region-config-independent.

### Piece 3 — construction finalization: `make_unique<Mesh>` ▷ `EnsureNodes()` + `Update()`

The L1 `wrap levels -> Mesh` lowers into the wrap loop (`palace/main.cpp:297-300`) that adopts each
refined `mfem::ParMesh` into a Palace `Mesh` via the `unique_ptr`-adopting ctor
(`palace/fem/mesh.hpp:76-81`):

    // palace/main.cpp:299
    mesh.push_back(std::make_unique<Mesh>(std::move(m)));

    // palace/fem/mesh.hpp:76-81 (the adopting Mesh ctor)
    template <typename T>
    Mesh(std::unique_ptr<T> &&mesh) : mesh(std::move(mesh))
    {
      this->mesh->EnsureNodes();   // :79  finalize geometry (ensure a Nodes GridFunction)
      Update();                    // :80  build the libCEED loc_attr / loc_bdr_attr maps
    }

The translation piece: the L1 *typed value construction* (`wrap`) lowers into a C++ ctor that **adopts the
moved-in `unique_ptr` and runs two finalization side-effects** — `EnsureNodes()` (`:79`, the
MFEM-owned-read-as-given geometry finalization) and `Update()` (`:80`, the Palace-authored construction of
the `loc_attr` / `loc_bdr_attr` libCEED attribute maps — the record fields documented at the
[`Mesh` record definition](../L1/build_mesh.md#record-definition)). At L1 these are an *opaque property of
the constructed value*; at L0 they are explicit construction-time side-effects in the ctor body. The wrap
is a `for` loop over the level-vector (`palace/main.cpp:297-300`) precisely because L0 carries the full
geometric-multigrid level stack as distinct `Mesh` objects (one per refinement level); the L1 form names
the constructed domain singularly and treats the level stack as the `fe_space_hierarchy` consumer's
concern.

## Applicability conditions

- The rewrite applies to the **serial-stage mesh-construction pipeline** — the mesh block of `main`
  (`palace/main.cpp:285-302`). It is the **sole** mesh-construction site driving every solver pipeline
  (the driver-agnostic scaffold the `lifecycle.L1` root cites, `book/src/feature/lifecycle.L1.md:44`).
- **Single-rank only** (see Scope below): the partition/distribute stage is read as the identity
  distribution.
- The **a-priori** refinement only — the adaptive (error-estimator-driven) estimate-mark-refine loop is
  the `lifecycle` root's outer fold (MFEM-opaque AMR), NOT part of this construction (c117 build_mesh
  Non-laws; out of scope here, obstruction-documented at the lifecycle root).

## Scope (single-machine — flag-once-skip)

Per CLAUDE.md §Scope (single-machine target; MPI / `Par*` out of scope):

- **`mesh::Partition` / distribution → single-rank = identity distribution.** On one rank the prepared
  serial mesh becomes the (single-rank) parallel mesh with no inter-process partitioning. The
  distribution-path decision (`use_mesh_partitioner`, `palace/utils/geodata.cpp:271-276`, including the
  `Mpi::Broadcast` at `:276`) and the `MeshPartitioner`-vs-byte-string-broadcast policy are multi-rank
  machinery — **flagged once and skipped**. The L1>L0 rewrite reads `Partition` as the
  value-consuming-and-returning stage (serial handle → parallel handle) with the *distribution placement*
  elided.
- **`mfem::ParMesh` / `loc_attr` / `loc_bdr_attr` per-process remap → single-rank.** The wrapped
  `mfem::ParMesh` is read single-rank (the standing `par-types-single-rank-reading` rule); the
  global→process-local libCEED attribute remap built by `Update()` (`:80`) collapses to a single-process
  contiguous relabeling. The translation documents that `Update()` builds these maps but does not define
  the multi-rank remap semantics.

These are the **only** single-machine carve-outs; the load / serial-prep / a-priori-refine / wrap stages
are in scope and lowered here.

## Justification kind

**Structural** — the rewrite is shape-driven. Each L1 pipeline stage maps to one positively-anchored L0
free-function call (or the wrap loop); the vocabulary shift (value-pipeline → in-place handle-threading +
ctor-finalization) is a syntactic identity on positive source, with the per-stage geometric kernels a
witnessed MFEM-owned-read-as-given boundary. No reduction-chain or empirical-match argument is needed; no
algebraic law beyond the c117 build_mesh staging/identity/monotonicity laws is asserted.

## Evidence (verified-against)

- `palace/main.cpp:285-302` — the mesh block of `main` (the build referent + the whole L0 RHS): the
  level-vector decl (`:285`), the scope (`:286`/`:301`), `mesh::Load` (`:287`), `solver->Preprocess`
  (`:288`), the parallel level-vector decl (`:289`), `mesh::Partition` consume (`:290`), `mesh::RefineMesh`
  in-place grow (`:291`), the wrap loop (`:297-300`) with `make_unique<Mesh>(std::move(m))` (`:299`).
- `palace/utils/geodata.hpp:25-50` — the four `mesh::` stage declarations + contracts: `Load`
  (load + serial-stage prep, `:25-31`), `Partition` (partition/distribute, `:33-36`), `RefineMesh`
  (parallel uniform a-priori refinement, ordered level meshes, `:45-50`).
- `palace/utils/geodata.cpp:421-455` — `mesh::RefineMesh` body: single-mesh-in precondition (`:424-425`),
  `uniform_ref_levels` read (`:426`), level-reserve (`:429`), the a-priori refinement loop `for (l = 0;
  l < uniform_ref_levels; l++)` (`:448`) with `emplace_back` copy (`:452`) and the MFEM-owned
  `UniformRefinement()` kernel (`:454`) — the in-place level-vector growth.
- `palace/utils/geodata.cpp:262-290` — `mesh::Partition` body: the distribution-path branch
  (`use_mesh_partitioner` `:271-276`, `Mpi::Broadcast` `:276`) — multi-rank, out of scope (read
  single-rank).
- `palace/fem/mesh.hpp:76-81` — the `unique_ptr`-adopting `Mesh` ctor: adopt the moved-in handle (`:77`),
  `EnsureNodes()` geometry finalization (`:79`, MFEM-owned), `Update()` libCEED attribute-map construction
  (`:80`, Palace-authored).
- `palace/fem/mesh.hpp:44-115` — the `class Mesh` wrapper (the produced output's record): `class Mesh`
  (`:44`), `unique_ptr<mfem::ParMesh> mesh` (`:49`), `loc_attr`/`loc_bdr_attr` maps (`:51-59`), the
  single-machine read surface `Get`/`Dimension`/`SpaceDimension`/`GetNE`/`GetNBE` (`:84-96`).
- `book/src/L1/build_mesh.md` — the L1 upper endpoint (firm c117): the typed `config → Mesh` pipeline, the
  `Mesh` record definition (`#record-definition`), the staging/identity/monotonicity laws this theme's
  pieces realize, and the Downward note (`:178-186`) this theme grounds.
- `book/src/feature/lifecycle.L1.md:44` — the `lifecycle.L1` composition root's stage-(1)
  build_mesh constituent (the sole mesh-build site).
```

The `build_mesh.md` frontmatter currently has NO `lowers-to` edge; the upgrade INSERTS one into
`depends-on:` (the lower endpoint now exists) and updates the schema-comment. The complete, unambiguous
frontmatter edit is the single block below (the earlier presentation-redundant no-op-shaped fragment was
removed by the repairer — repairer META.md issue 2; finding 2026-06-06 repair phase).

```edit:book/src/L1/build_mesh.md
rank: firm
edges:
  depends-on:
    - target: palace/fem/mesh.hpp:44-115
      kind: cites-evidence        # the `class Mesh` wrapper (ctor chain :72-81, single-machine surface :84-96, libCEED attr map :96-115)
    - target: palace/main.cpp:286-301
      kind: cites-evidence        # the build referent: Load -> Preprocess -> Partition -> RefineMesh -> wrap
    - target: L1-L0/build-mesh-construction-rotation
      kind: lowers-to             # the L1>L0 home: how this typed construction rewrites into the L0 free-function chain (c118)
  reference:
    - L1/fe_space                  # the primary consumer of the constructed Mesh (fe_space takes `mesh: Mesh`)
    - feature/lifecycle.L1         # the composition root that forward-references `build_mesh :: Config -> Mesh`
---
```

(and update the schema-comment line that currently reads "so no `lowers-to` edge is asserted yet (would
point at a not-yet-firm node)." — the node is now firm. Exact edit below.)

```edit:book/src/L1/build_mesh.md
# build_mesh. Well-foundedness rank(u) <= rank(v): this node firm (rank 3); the only edges are
# cites-evidence to rank-terminal L0 source. The L1>L0 mutation-rotation theme is named-not-authored
# (forthcoming), so no `lowers-to` edge is asserted yet (would point at a not-yet-firm node).
```
becomes
```text
# build_mesh. Well-foundedness rank(u) <= rank(v): this node firm (rank 3); the cites-evidence edges
# point at rank-terminal L0 source, and the `lowers-to` edge points at the firm L1>L0
# `build-mesh-construction-rotation` theme (c118; rank firm = min(endpoints)).
```

(and the Downward-to-L0 prose at `build_mesh.md:178-186` — the "named, NOT authored this cycle" /
"No `lowers-to` edge is asserted in this chapter's front-matter yet" claims are now stale. Exact edit
below.)

```edit:book/src/L1/build_mesh.md
## Downward (to L0)

The L1>L0 rotation [`build-mesh-construction-rotation`](../L1-L0/build-mesh-construction-rotation.md)
narrates how the typed `config → Mesh` construction rewrites into the L0 free-function chain `mesh::Load` ▷
`solver->Preprocess` ▷ `mesh::Partition` ▷ `mesh::RefineMesh` ▷ `make_unique<Mesh>` (`palace/main.cpp:287-299`),
including the in-place `unique_ptr` mesh-handle mutation (the level-vector grown in place by `RefineMesh`,
`palace/utils/geodata.cpp:421-455`) and the construction-time `EnsureNodes()` + `Update()` finalization
(`palace/fem/mesh.hpp:79-80`). The `lowers-to` edge to that theme is asserted in this chapter's front-matter
(c118).
```

```edit:book/src/L1-L0/index.md
| **Construction-rotation** | | | |
| [build-mesh-construction-rotation](./build-mesh-construction-rotation.md) | [`L1/build_mesh`](../L1/build_mesh.md) (firm c117) | `palace/main.cpp:285-302` (mesh block of main), `palace/utils/geodata.{hpp,cpp}` (`Load`/`Partition`/`RefineMesh` :25-50 decls, :421-455 RefineMesh body), `palace/fem/mesh.hpp:76-81` (adopting Mesh ctor) | firm *(structural; vocabulary-translation — pure `config → Mesh` value-pipeline → imperative free-function chain `Load` ▷ `Preprocess` ▷ `Partition` ▷ `RefineMesh` ▷ `make_unique<Mesh>` threading three successive `unique_ptr` handle types; **3 translation pieces**: P1 value-pipeline → handle-ownership `std::move` threading (no algebraic content — C++ memory discipline), P2 in-place growth of the parallel level-vector by `RefineMesh` (`emplace_back`/`UniformRefinement` mutating the caller's `mfem_mesh` :452-454; zero-refinement-identity + level-monotonicity = c117 build_mesh laws 3/4), P3 construction finalization `make_unique<Mesh>` ▷ adopting-ctor `EnsureNodes()`+`Update()` :79-80; **pipeline-staging-lowers / per-stage-geometric-kernel-MFEM-owned split** (`UniformRefinement`/MFEM-partitioner/`EnsureNodes` read-as-given, analogue of the `fe-space-construction-rotation` construction-lowers/dof-bookkeeping-MFEM-owned boundary); region-vs-uniform refinement split (region in `Load`, uniform in `RefineMesh`); MPI/`Par*` partition/distribute single-rank = identity distribution out-of-scope; firm-on-positive-structure, no-dedicated-mesh-construction-test caveat non-gating per `fe_space`/`fe_collection`/`essential_dofs` precedent)* |
| [essential-dofs-construction-rotation](./essential-dofs-construction-rotation.md) | [`L1/essential_dofs`](../L1/essential_dofs.md) (firm c066) | `palace/fem/multigrid.hpp:92-101` (dbc block: `bdr_attr_max` `:95-97`, `AttrToMarker` `:98`, `GetEssentialTrueDofs` `:99-100`; per-level `:106-111`/`:117-122`), `palace/utils/geodata.hpp:75-96` (`mesh::AttrToMarker` doc+decl+wrappers), `palace/models/spaceoperator.cpp:169-206` (standalone `CheckBoundaryProperties`: `bdr_attr_max` `:174`, marker-OR union `:187-198`, `GetEssentialTrueDofs` `:204-205`) | firm *(structural; vocabulary-translation — pure `(space, bdr_attrs, bdr_attr_max) → DofSet[N]` essential-true-dof-set value → imperative attribute→marker→`GetEssentialTrueDofs` block with out-parameter write (`emplace_back()` receiver read as return); **construction-head-lowers / dof-resolution-tail-MFEM-owned split** — `bdr_attr_max` extraction (`multigrid.hpp:95-97`, empty-guard ⇒ `∅`) + fully-Palace-authored `mesh::AttrToMarker` (`geodata.hpp:75-96`; dense `{0,1}` membership-indicator over `[1..bdr_attr_max]`, `-1`-singleton wildcard ⇒ all-ones `:77-78`) lower HERE; the marker→true-dof-set `space.Get().GetEssentialTrueDofs` (`multigrid.hpp:99`) is MFEM-owned-read-as-given (same posture as `fe-space-construction-rotation` toward dof structure), NOT a constructed sub-part — so firm, not partly-constructive; attribute-wildcard variant axis (explicit-list vs `[-1]` all-ones, 2 head cases); marker union-additivity (join-semilattice homomorphism) witnessed at `spaceoperator.cpp:187-198`; per-level-hierarchy fan-out is the `fe_space_hierarchy` consumer's property (out of scope); analogue of the c064 `fe-space-construction-rotation` construction-lowers/dof-bookkeeping-MFEM-owned split; MPI/`Par*` + partitioning out-of-scope single-rank; firm-on-positive-structure, no-dedicated-`test-multigrid.cpp` caveat non-gating per `fe_space`/`fe_collection`/`fe_assemble`)* |
```

(the edit REPLACES the `| **Construction-rotation** | | | |` header row + the immediately-following
`essential-dofs` row with: the header row, the NEW `build-mesh-construction-rotation` row alpha-first
(b < e), then the unchanged `essential-dofs` row.)

```edit:book/src/SUMMARY.md
- [Construction-rotation themes](./L1-L0/construction-rotation-intro.md)
  - [essential-dofs-construction-rotation](./L1-L0/essential-dofs-construction-rotation.md)
```
becomes
```text
- [Construction-rotation themes](./L1-L0/construction-rotation-intro.md)
  - [build-mesh-construction-rotation](./L1-L0/build-mesh-construction-rotation.md)
  - [essential-dofs-construction-rotation](./L1-L0/essential-dofs-construction-rotation.md)
```

(INSERT-only: the live SUMMARY construction-rotation group has FIVE children —
`essential-dofs` / `fe-collection` / `fe-operator-assemble` / `fe-space` / `weak-form-term`
(`book/src/SUMMARY.md:265-270`). `build-mesh` sorts alpha-FIRST (b < e), so it is inserted as a
new child line immediately AFTER the `Construction-rotation themes` group header and BEFORE the
`essential-dofs` line. The other four sibling lines are UNTOUCHED. The anchor above is the group
header + the first existing child (`essential-dofs`, `:265-266`) so the alpha-first insert is
unambiguous against the actual neighbors.)

## Speculative operators proposed

None. This is a firm L1>L0 lowering of an already-firm L1 operator (`build_mesh`, c117); no new L1
vocabulary is introduced. The three handle types and the per-stage kernels are existing L0 / MFEM
constructs, not new operators.

## Supporting evidence

(All citations self-verified via `tools/citecheck/citecheck.py` + on-disk `read_range` before emit; the
codemap `read_range` index for `palace/fem/geodata.cpp` is wrong — the file is `palace/utils/geodata.cpp`,
corrected below.)

- `palace/main.cpp:285-302` — the mesh block of `main`, on-disk-confirmed: line 285 `std::vector<...>
  mesh;`, line 286 `{`, lines 287-291 the four-stage chain, line 299 `make_unique<Mesh>(std::move(m))`,
  line 301 the closing `}` (line 302 blank). The prompt-stated `:287-302` overshoots by one (302 is blank);
  the block-scope is `:286-301`, the four-stage chain `:287-291`, the wrap loop `:297-300`. Cited
  accordingly.
- `palace/utils/geodata.cpp` (NOT `palace/fem/geodata.cpp` — the prompt's path is wrong; corrected):
  `Load` body `:122-143`, `Partition` `:262-290`, `RefineMesh` `:421-455`. The in-place level-vector
  growth: `for` loop `:448`, `emplace_back` `:452`, `UniformRefinement` `:454` (the prompt's `:421-450`
  stops just before the loop body; extended to `:455` to capture the full mutation).
- `palace/fem/mesh.hpp:76-81` — the adopting ctor; `EnsureNodes()` `:79`, `Update()` `:80` (prompt-stated
  `:79-80` confirmed on disk).
- `palace/utils/geodata.hpp:25-50` — the four stage declarations + contracts (on-disk-confirmed; `Load`
  doc `:25-31`, `Partition` `:33-36`, `RefineMesh` `:45-50`).

## Open questions / caveats

- **Prompt path error (recorded, not blocking):** the scope cited `palace/fem/geodata.cpp:421-450`; the
  actual file is `palace/utils/geodata.cpp` (codemap `search_text RefineMesh` confirms; `palace/fem/` has
  no `geodata.cpp`). The L1 `build_mesh` chapter already cites the correct `palace/utils/geodata.cpp`, so
  this is a prompt-side typo, not an artifact drift. Flagged to OQ for the integrator's awareness.
- **Prompt range overshoot (recorded):** `main.cpp:287-302` — line 302 is blank; the block closes at
  `:301`. Used `:285-302` for the cites-evidence frontmatter edge (covers decl through blank line,
  citecheck-bounds-ok) but `:286-301` / `:287-291` for the in-prose pinpoints. The `RefineMesh`
  in-place-mutation range `:421-450` was extended to `:421-455` to include `UniformRefinement()` at `:454`.
- **`EnsureNodes` ownership boundary:** `EnsureNodes()` (`mesh.hpp:79`) is read as MFEM-owned (it ensures a
  Nodes `GridFunction` on the underlying `mfem::ParMesh`). `Update()` (`:80`) is Palace-authored (builds
  `loc_attr`/`loc_bdr_attr`). The theme treats the split as part of the pipeline-staging-lowers /
  kernel-MFEM-owned boundary; a future lowering-verifier pass could pin `Update()`'s body to its own
  evidence range if a finer-grained sub-theme is wanted (not needed for firm).
- **`concepts/mesh.md` record page:** D6 owns the `record-Mesh-needs-definition-home` judgment this cycle;
  this theme references the `Mesh` record by its current in-chapter home
  (`../L1/build_mesh.md#record-definition`) per the dispatch instruction. If D6 lands `concepts/mesh.md`,
  the `#record-definition` anchors here will want a follow-on re-anchor (flag for the integrator /
  lifter).
