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
Palace [`Mesh`](../concepts/mesh.md) wrapper whose adopting ctor runs the
`EnsureNodes()` + `Update()` geometry/attribute finalization. The translation has a sharp boundary — the
**pipeline staging + handle-ownership threading lowers HERE (Palace-authored), while each stage's
geometric kernel is MFEM-owned-read-as-given** — narrated in the split below. This is the
domain-construction analogue of the FE-space sub-spine's `fe-space-construction-rotation` /
`essential-dofs-construction-rotation` siblings (construction-lowers / library-owned-kernel-as-given).

The per-stage geometric kernels (`UniformRefinement`, the MFEM `MeshPartitioner`, `EnsureNodes`)
are **MFEM-owned-read-as-given** — a witnessed library-ownership boundary, not a constructive
reconstruction (the same posture the FE-space siblings take toward dof bookkeeping / element
quadrature). MPI/`Par*` and mesh partitioning/distribution are read single-rank (out of scope per
CLAUDE.md §Scope).

## L1 form (LHS)

The pure construction value (the prime entry [`build_mesh`](../L1/build_mesh.md)):

    build_mesh :: Config -> Mesh

`Mesh` is the discretised computational domain — a single-rank `mfem::ParMesh` augmented with the libCEED
local-attribute mapping (see [`Mesh` record definition](../concepts/mesh.md)). At L1 this
is the ordered composition of four pure stages — **load ▷ preprocess ▷ partition ▷ a-priori-refine** —
each a pure function of the prior stage's mesh value:

    build_mesh config =
      let smesh = load config            -- read serial mesh + all serial-stage prep
          smesh' = preprocess config smesh   -- problem-type-specific serial preprocessing
          pmesh  = partition config smesh'   -- single-rank: the identity distribution (see Scope)
          levels = refine config pmesh       -- a-priori uniform refinement -> level-mesh sequence
      in  wrap levels                     -- the Palace Mesh wrapper (finalized geometry + attr maps)

At L1 the staging is referentially transparent: given the same `config`, `build_mesh` names the same
`Mesh` (same geometry, same `Dimension`/`SpaceDimension`/`GetNE`/`GetNBE`, same attribute maps — the
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
- **Zero-refinement identity** (build_mesh law 3): with `uniform_ref_levels == 0` the loop `:448`
  does not execute and the vector keeps its single partitioned entry — the refine stage is the identity on
  the partitioned mesh. **Level-monotonicity** (build_mesh law 4): with `uniform_ref_levels = k`, the vector is
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
[`Mesh` record definition](../concepts/mesh.md)). At L1 these are an *opaque property of
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
  the `lifecycle` root's outer fold (MFEM-opaque AMR), NOT part of this construction (build_mesh
  Non-laws; out of scope here, obstruction-documented at the lifecycle root).

## Scope

**Kind:** single-machine (flag-once-skip)

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
algebraic law beyond the build_mesh staging/identity/monotonicity laws is asserted.

## Evidence

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
- `book/src/L1/build_mesh.md` — the L1 upper endpoint: the typed `config → Mesh` pipeline, the
  `Mesh` record definition (`#record-definition`), the staging/identity/monotonicity laws this theme's
  pieces realize, and the Downward note (`:178-186`) this theme grounds.
- `book/src/feature/lifecycle.L1.md:44` — the `lifecycle.L1` composition root's stage-(1)
  build_mesh constituent (the sole mesh-build site).
