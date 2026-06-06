---
agent: harvester
invoked_at: 2026-06-06T205239Z
scope: L1 operator: build_mesh
status: integrated
integrated_at: 2026-06-06T214845Z
integration_commit: ad3a65db89bec3cb0af734d5fab52bfee9db7455
integration_notes: "cycle-117 D3 (apply-order 2/5). New firm L1 op build_mesh :: Config -> Mesh (firm-on-positive-structure; in-chapter Mesh record definition) + new 'Mesh & FE-space construction' kind-grouping in L1/index.md + SUMMARY.md. All per-report gates PASS; rank firm rests on rank-terminal L0 (no violation). build_mesh lands as detritus pending an inbound feature/higher depends-on consumer (GC-ground-don't-remove; NEW node, not a block). NOTE: D3's deferred group-intro authoring caused a duplicate-file build error at finalize, repaired by creating book/src/L1/mesh-construction-intro.md group-intro stub + repointing the SUMMARY link. 4 OQs promoted."
inputs:
  - cycle-117 D3 (WAVE-1) dispatch, open-all-feature-fronts directive B front (iv) — mesh-wrapper vocabulary
  - lifecycle.L1 forward-ref `build_mesh :: Config -> Mesh` (book/src/feature/lifecycle.L1.md:37,44)
  - substrate: palace/fem/mesh.hpp:44-115 (class Mesh), palace/main.cpp:286-301 (build referent), palace/utils/geodata.{hpp,cpp} (Load/Partition/RefineMesh)
  - sibling fe_space.md template (the FE-space construction firm chapter)
  - record-definition obligation (user directive 2026-06-03); §Scope single-machine
---

# CYCLE: Formalize build_mesh at L1

## Summary
Formalizes the single-machine **mesh construction** operator `build_mesh :: Config -> Mesh` at L1 — the
driver-agnostic pure function (load → preprocess → partition[single-rank] → a-priori-refine) that the
`lifecycle.L1` composition root already forward-references and that every per-driver column's mesh stage
and the FE-space sub-spine (`fe_space` already takes `mesh: Mesh`) consume. This is a fresh firm chapter
(`book/src/L1/build_mesh.md`): no prior rough-in row existed; the operator was named only as an L0 scaffold
cell in `lifecycle.L1`'s constituent table. The produced **`Mesh` record** (the `mfem::ParMesh` wrapper read
single-rank + the libCEED local-attribute mapping) is given an in-chapter `## Record definition` section AND
flagged for a `concepts/mesh.md` page (≥2 consumers: every driver mesh stage + `fe_space` + the deferred
`fe_space_hierarchy`). Single-machine scope: the partition/distribute stage and the `ParMesh`/`loc_attr`
per-process attribute remap are read as single-rank equivalents (flag-once-skip); MFEM-opaque adaptive
mesh-refinement is left obstruction-documented, NOT forced to a firm claim.

The operator is **firm on positive structure**: the construction is read directly from positive source (the
`Mesh` ctor chain `palace/fem/mesh.hpp:72-81` + the build referent `palace/main.cpp:286-301` →
`geodata.{hpp,cpp}` `Load`/`Partition`/`RefineMesh`); every law is a syntactic identity on that structure
(construction/composition facts, not convergence/iteration semantics), so the absence of a dedicated
mesh-construction unit test does not gate firm (the `fe_space` c064 / `fe_assemble` c054 / `apply_linop`
no-dedicated-test precedent).

## Proposed changes

```new:book/src/L1/build_mesh.md
---
layer: L1
operator: build_mesh
harvested_by: harvester:2026-06-06T205239Z-harvester-build-mesh
cycle: cycle-117
# Graded-stack scheme. This firm L1 construction is a leaf at L1 (it consumes a `Config`/`IoData`
# surface and produces the `Mesh` typed value; no other L1 operator is invoked). It rests on its
# positive L0 ctor + build-referent source (cites-evidence, rank-terminal ground truth). The `Mesh`
# record is its produced output; `fe_space` (firm) consumes it (a consumed-by relation, NOT a dep of
# build_mesh). Well-foundedness rank(u) <= rank(v): this node firm (rank 3); the only edges are
# cites-evidence to rank-terminal L0 source. The L1>L0 mutation-rotation theme is named-not-authored
# (forthcoming), so no `lowers-to` edge is asserted yet (would point at a not-yet-firm node).
rank: firm
edges:
  depends-on:
    - target: palace/fem/mesh.hpp:44-115
      kind: cites-evidence        # the `class Mesh` wrapper (ctor chain :72-81, single-machine surface :84-96, libCEED attr map :96-115)
    - target: palace/main.cpp:286-301
      kind: cites-evidence        # the build referent: Load -> Preprocess -> Partition -> RefineMesh -> wrap
  reference:
    - L1/fe_space                  # the primary consumer of the constructed Mesh (fe_space takes `mesh: Mesh`)
    - feature/lifecycle.L1         # the composition root that forward-references `build_mesh :: Config -> Mesh`
---

# `build_mesh` — single-machine mesh construction

`build_mesh :: Config -> Mesh`

Construct the **discretised computational domain** `Mesh` — the geometric substrate every assembled-operator
pipeline stands on — from the input `Config`. The construction is the serial-stage pipeline
**load → preprocess → partition → a-priori-refine**: read the serial mesh from disk and perform all
serial-stage preparation (including the box/sphere **region refinement** of the serial mesh), apply
problem-type-specific preprocessing, partition (single-rank: the identity distribution, see *Scope*), then
apply the a-priori parallel **uniform** refinement requested by the config.
The result is the Palace `Mesh` wrapper — an `mfem::ParMesh` read single-rank, augmented with the libCEED
local-attribute mapping — consumed read-only thereafter by [`fe_space`](./fe_space.md) (which takes
`mesh: Mesh`) and, through it, by the whole assembled-operator front. `build_mesh` is the
[`lifecycle`](../feature/lifecycle.L1.md) composition root's stage (1).

## Context

L1 is the mutation-rotation layer: source operations re-expressed as pure functions. `build_mesh` is the
**domain-construction** view of that rotation — at L0 the mesh is loaded, preprocessed, partitioned, and
refined by a sequence of free functions that mutate (or consume-and-return) `unique_ptr` mesh handles
in place; the L1 form names the pure `config → mesh` pipeline and treats the constructed `Mesh` as an
immutable typed value.

At L0 the build referent is the mesh block of `main` (`palace/main.cpp:286-301`): a serial mesh is loaded
and serial-stage-prepared by `mesh::Load` (`palace/main.cpp:287`), the solver applies problem-type-specific
serial preprocessing via `solver->Preprocess` (`:288`), `mesh::Partition` partitions/distributes the prepared
serial mesh into a parallel mesh (`:290`), `mesh::RefineMesh` applies a-priori uniform refinement producing
the level-mesh sequence (`:291`), and each resulting `mfem::ParMesh` is wrapped into a Palace `Mesh`
(`:299`). The four `mesh::` stages are declared in `palace/utils/geodata.hpp:25-50`; their bodies live in
`palace/utils/geodata.cpp` (`Load` `:122`, `RefineMesh` `:421`).

This chapter is defined in L1 vocabulary (the typed `config → Mesh` construction pipeline). The forward
rewrite into the L0 free-function chain + the in-place `unique_ptr` mesh-handle mutation is the L1>L0
`build-mesh-construction-rotation` theme (named, NOT authored this cycle — see *Status*).

## Signature

    build_mesh :: Config -> Mesh

Shape contract (bunsen-style, named axes):

- `config` — `Config` — the `IoData` configuration surface (the same read-only record the
  [`lifecycle`](../feature/lifecycle.L1.md) root and every per-driver column consume; cross-referenced to
  [`config-record`](../concepts/config-record.md)). The mesh-relevant fields are `model.mesh` (the mesh
  file), `model.remove_curvature`, the region/box/sphere refinement config, and
  `model.refinement.uniform_ref_levels` (the a-priori refinement depth). Read-only.
- result — `Mesh` — the Palace mesh wrapper (see *Record definition*): a single-rank `mfem::ParMesh`
  augmented with the libCEED local-attribute mapping. The result carries the geometric axes the FE-space
  construction reads — `Dimension`, `SpaceDimension`, element count `GetNE`, boundary-element count
  `GetNBE` (`palace/fem/mesh.hpp:93-96`).

The `Mesh` is the load-bearing output: it is the very `mesh: Mesh` that [`fe_space`](./fe_space.md)
pairs with an `FECollection` to define the true-dof axis `N` that the whole vocabulary is indexed by.
(No `Tensor[...]` shape group appears in this signature — `build_mesh` consumes config and produces a
typed geometric object, not a tensor; the named-shape-group notation governs tensor-valued signatures, see
[semantics §1.2.1](../semantics/index.md).)

## Record definition

`Mesh` is the Palace wrapper for MFEM's `ParMesh` class, with extensions for Palace
(`palace/fem/mesh.hpp:44`). It is the produced output of `build_mesh` and the consumed input of
[`fe_space`](./fe_space.md). Single-consumer-judgment: `Mesh` is consumed by ≥2 chapters (every driver
column's mesh stage + `fe_space` + the deferred `fe_space_hierarchy`), so per the record-definition
obligation it warrants a shared `concepts/mesh.md` page — **flagged in Open questions**
(`record-Mesh-needs-definition-home`). This in-chapter section is the interim definition home until that
page lands (it is the chapter that *produces* the record).

| field | type | meaning | stratum |
|---|---|---|---|
| `mesh` | `unique_ptr<mfem::ParMesh>` (single-rank) | the underlying MFEM mesh object; can also point to a derived `mfem::ParSubMesh` (`palace/fem/mesh.hpp:47-49`) | construction-time (owns the loaded/partitioned/refined mesh) |
| `loc_attr` | `unordered_map<int,int>` | global (MFEM, 1-based) **domain** attribute → process-local contiguous (1-based) libCEED attribute (`palace/fem/mesh.hpp:51-58`) | construction-time (built by `Update`); single-rank = identity-flavoured remap (see *Scope*) |
| `loc_bdr_attr` | `unordered_map<int, unordered_map<int,int>>` | global **boundary** attribute → (neighbouring domain attr → local boundary attr) — discriminates boundary elements bordering more than one domain (`palace/fem/mesh.hpp:51-59`) | construction-time |
| `ceed_from_self` | `bool` | true after `RebuildCeedAttributes()` (`palace/fem/mesh.hpp:60`) | run-time flag |
| `geom_data` | `mutable ceed::CeedObjectMap<ceed::CeedGeomFactorData>` | cached libCEED geometry-factor quadrature data (`w·|J|`, `adj(J)^T/|J|`) per element-geometry/thread (`palace/fem/mesh.hpp:62-69`) | run-time (transparent cache, re-derivable on demand — a performance store, NOT lifted structure) |

The backing C++ struct is `class Mesh` (`palace/fem/mesh.hpp:44`). It is constructed by either the variadic
ctor that builds the `mfem::ParMesh` from forwarded args (`palace/fem/mesh.hpp:72-75`) or, the form `main`
uses, the `unique_ptr`-adopting ctor `Mesh(std::unique_ptr<T> &&mesh)` (`:76-81`) which runs
`EnsureNodes()` + `Update()` (`:79-80`) to finalize the geometry and build the attribute maps. The
single-machine read surface is `Get()` / `Dimension()` / `SpaceDimension()` / `GetNE()` / `GetNBE()`
(`palace/fem/mesh.hpp:84-96`); the libCEED attribute-map accessors are `GetCeedAttributes` /
`GetCeedBdrAttributes` (`:96-115`). The config-relevant `IoData` surface this record mirrors is
`model.mesh` + `model.refinement` (cross-ref [`config-record`](../concepts/config-record.md)).

## Algebraic laws

The laws are syntactic identities on the positive construction pipeline (no convergence / iteration
semantics — refinement *depth* is a fixed config field, not an adaptively-driven loop; the adaptive
estimate-mark-refine loop is the [`lifecycle`](../feature/lifecycle.L1.md) root's outer fold, NOT
`build_mesh`):

1. **Config determinism.** `build_mesh` is a pure function of `config` — the same config (same mesh file,
   same `remove_curvature`, same refinement settings) produces the same `Mesh` (the same geometry, the same
   `Dimension`/`SpaceDimension`/`GetNE`/`GetNBE`, the same attribute maps). The serial load + serial-stage
   prep is deterministic given the file (`palace/utils/geodata.cpp:122-143`).
2. **Pipeline staging (load ▷ preprocess ▷ partition ▷ refine).** The construction is the ordered
   composition of the four `mesh::` stages — `Load` then `Preprocess` then `Partition` then `RefineMesh`
   (`palace/main.cpp:287-291`) — each consuming the prior stage's mesh handle. The order is load-bearing
   (partition consumes a *prepared serial* mesh; refine consumes a *partitioned* mesh) and is NOT a
   commuting family.
3. **Zero-refinement identity.** With `uniform_ref_levels == 0`, `RefineMesh` produces the single
   partitioned mesh unchanged (`palace/utils/geodata.cpp:421-430`: the level-vector keeps its single entry;
   the refinement loop `for (l = 0; l < uniform_ref_levels; l++)` does not execute, `:448`). `RefineMesh`
   performs **parallel uniform refinement only** — box/sphere **region** refinement happens earlier, in the
   `Load`/serial-prep stage on the serial mesh (`palace/utils/geodata.hpp:25-31,45-46`; the in-body comment
   `palace/utils/geodata.cpp:423`), so the parallel refinement stage is the identity on the partitioned mesh
   independently of the region-refinement config.
4. **Refinement-level monotonicity (a-priori only).** With `uniform_ref_levels = k`, `RefineMesh` produces
   the ordered level-mesh sequence of increasing refinement (`palace/utils/geodata.hpp:47-49`: "stored in
   order of increased refinement"); the coarse mesh is the head, the finest the tail. This is *a-priori*
   refinement read from config — it is the geometric-multigrid level stack, NOT the adaptive AMR loop (the
   `lifecycle` root's fold owns that; see *Non-laws*).

**Non-laws (read-as-given / out-of-scope, do NOT constrain `build_mesh`):**

- **Partition / distribution semantics.** Single-rank (see *Scope*): `mesh::Partition` is read as the
  identity distribution; the multi-rank partition policy (`mfem::MeshPartitioner` vs byte-string broadcast,
  `palace/utils/geodata.cpp:131-143`) is out of scope. No L1 law constrains partition placement.
- **MFEM-opaque adaptive mesh refinement.** The adaptive (error-estimator-driven) refinement is NOT part of
  `build_mesh` — it is the `lifecycle` root's outer estimate-mark-refine fold (the per-element non-conformal
  AMR machinery, `mfem::Mesh::GeneralRefinement`, is MFEM-opaque). `build_mesh` performs only the
  **a-priori** (config-fixed uniform/region) refinement; the adaptive loop stays obstruction-documented at
  the lifecycle root, not forced into a firm claim here.
- **libCEED geometry-factor cache.** `geom_data` is a transparent performance store (re-derivable on
  demand); no L1 law constrains it (the `fe_space` libCEED-cache precedent,
  `book/src/L0/fespace-file.md:159-164`).

## Dependencies

(leaf at L1 — the construction takes a `Config`/`IoData` surface and produces a typed `Mesh` value; no
other L1 operator is invoked.) The result is consumed by [`fe_space`](./fe_space.md) (which pairs the
`Mesh` with an `FECollection`) and is stage (1) of the [`lifecycle`](../feature/lifecycle.L1.md)
composition root — those are consumed-by relations, NOT dependencies.

## Scope (single-machine — flag-once-skip)

Per CLAUDE.md §Scope (single-machine target; MPI / `Par*` out of scope):

- **`mesh::Partition` / distribution → single-rank.** The partition/distribute stage (`palace/main.cpp:290`,
  `palace/utils/geodata.hpp:33-36`) is read as the **identity distribution**: on a single rank the prepared
  serial mesh becomes the (single-rank) parallel mesh with no inter-process partitioning. The
  conformality-driven distribution-path branch (`use_mesh_partitioner`,
  `palace/utils/geodata.cpp:134,140-143`) and the `MeshPartitioner`-vs-byte-string-broadcast policy are
  multi-rank machinery — **flagged once and skipped**.
- **`mfem::ParMesh` / `loc_attr` / `loc_bdr_attr` per-process attribute remap → single-rank.** The wrapped
  `mfem::ParMesh` is read single-rank (the standing `par-types-single-rank-reading` rule); the
  global→process-local libCEED attribute remap (`palace/fem/mesh.hpp:51-59`) collapses to a single-process
  contiguous relabeling on one rank. The `Mesh` record carries these maps (above) but the L1 form does not
  define the multi-rank remap semantics.

These two are the **only** single-machine carve-outs; the load / serial-prep / a-priori-refine stages are
in scope and lifted here.

## Downward (to L0)

The L1>L0 rotation `build-mesh-construction-rotation` (named, NOT authored this cycle) will narrate how the
typed `config → Mesh` construction rewrites into the L0 free-function chain `mesh::Load` ▷
`solver->Preprocess` ▷ `mesh::Partition` ▷ `mesh::RefineMesh` ▷ `make_unique<Mesh>` (`palace/main.cpp:287-299`),
including the in-place `unique_ptr` mesh-handle mutation (the level-vector grown in place by `RefineMesh`,
`palace/utils/geodata.cpp:421-450`) and the construction-time `EnsureNodes()` + `Update()` finalization
(`palace/fem/mesh.hpp:79-80`). No `lowers-to` edge is asserted in this chapter's front-matter yet (it would
point at a not-yet-authored node); the theme is flagged in Open questions.

## Status

**firm (firm-on-positive-structure).** The construction is read directly from positive source: the `Mesh`
ctor chain (`palace/fem/mesh.hpp:72-81`), the single-machine read surface (`:84-96`), and the build referent
(`palace/main.cpp:286-301`) → the four `mesh::` stage declarations (`palace/utils/geodata.hpp:25-50`) +
bodies (`palace/utils/geodata.cpp:122`, `:421`). Every law is a syntactic identity on this positive
structure (construction determinism, pipeline staging, zero-refinement identity, a-priori
level-monotonicity) — there is no convergence/iteration semantics to test-gate (the a-priori refinement
*depth* is a fixed config field, not an adaptively-driven loop), so the absence of a dedicated
mesh-construction unit test does not gate firm (the `fe_space` cycle-064 / `fe_assemble` cycle-054 /
`apply_linop` no-dedicated-test precedent).

This is the **geometric substrate under all five solver pipelines** — the highest-fan-out entry of the
mesh-wrapper front (every driver column's mesh stage and the FE-space sub-spine, via `fe_space`'s
`mesh: Mesh` input, stand on it).

**Single-machine scope (flagged):** the partition/distribute stage and the `ParMesh`/`loc_attr` per-process
attribute remap are read as single-rank equivalents (see *Scope*); MFEM-opaque adaptive mesh refinement is
left to the `lifecycle` root's outer fold (obstruction-documented there), NOT forced to a firm claim here.

**`Mesh` record home:** an in-chapter `## Record definition` section is authored above (interim home); a
shared `concepts/mesh.md` page is flagged (`record-Mesh-needs-definition-home`) since `Mesh` has ≥2
consumers.

**Deferred follow-on (named, NOT authored this cycle):** the L1>L0
`build-mesh-construction-rotation` theme; the `concepts/mesh.md` record page; and (downstream) the
mesh-refinement / `fe_space_hierarchy` h-refinement coupling (the a-priori level sequence is the
geometric-multigrid stack `fe_space_hierarchy` consumes).

## Evidence

- `palace/fem/mesh.hpp:44-115` — the `class Mesh` wrapper: `class Mesh` (`:44`), the underlying
  `unique_ptr<mfem::ParMesh> mesh` (`:49`), the `loc_attr`/`loc_bdr_attr` libCEED attribute maps
  (`:51-59`), the variadic ctor (`:72-75`) and the `unique_ptr`-adopting ctor with `EnsureNodes()`+`Update()`
  (`:76-81`), the single-machine read surface `Get`/`Dimension`/`SpaceDimension`/`GetNE`/`GetNBE`
  (`:84-96`), and the libCEED attribute-map accessors (`:96-115`).
- `palace/main.cpp:286-301` — the build referent (the mesh block of `main`): `mesh::Load` (`:287`),
  `solver->Preprocess` (`:288`), `mesh::Partition` (`:290`), `mesh::RefineMesh` (`:291`), and the
  `make_unique<Mesh>(std::move(m))` wrap (`:299`). The driver-agnostic mesh-build scaffold the
  `lifecycle.L1` root cites (`book/src/feature/lifecycle.L1.md:44`).
- `palace/utils/geodata.hpp:25-50` — the four `mesh::` stage declarations + contracts: `Load`
  (load + serial-stage prep, `:25-31`), `Partition` (partition/distribute, `:33-36`), `RefineMesh`
  (parallel uniform a-priori refinement, ordered level meshes, `:45-50`).
- `palace/utils/geodata.cpp:122-143` — `Load` body: serial load + the conformality-driven
  distribution-path branch (`use_mesh_partitioner`, `:134,140-143` — multi-rank, out of scope).
- `palace/utils/geodata.cpp:421-450` — `RefineMesh` body: the single-mesh-in precondition (`:424-425`),
  `uniform_ref_levels` read (`:426`), the level-reserve (`:427-430`), and the a-priori refinement loop
  `for (l = 0; l < uniform_ref_levels; l++)` (`:448`) — the zero-refinement-identity + level-monotonicity
  law substrate.
- `book/src/feature/lifecycle.L1.md:37,44` — the composition root's forward-reference
  `build_mesh :: Config -> Mesh` (`:37`) + stage-(1) constituent narration (`:44`).
- `book/src/L1/fe_space.md:33,71-73` — `fe_space`'s `mesh: Mesh` input (the primary consumer of the
  constructed `Mesh`).
```

```edit:book/src/L1/index.md
| **Mesh & FE-space construction** | | | |
| [`build_mesh`](./build_mesh.md) | `(config: Config) → Mesh` (i.e. load → preprocess → partition[single-rank] → a-priori-refine) | (leaf; consumes the `Config`/`IoData` surface, produces the `Mesh` typed value; produces-the-`Mesh`-consumed-by [`fe_space`](./fe_space.md) and stage (1) of the [`lifecycle`](../feature/lifecycle.L1.md) root — consumed-by relations, NOT dependencies; the partition/distribute stage + `ParMesh`/`loc_attr` per-process attr remap read single-rank) | `firm` (single-machine mesh construction; the geometric substrate under all 5 solver pipelines; the `Mesh` record = the `mfem::ParMesh` wrapper read single-rank + libCEED local-attribute map, in-chapter `## Record definition` + flagged `concepts/mesh.md`; L0: `class Mesh` `palace/fem/mesh.hpp:44-115` (ctor chain `:72-81`, single-machine surface `:84-96`, libCEED attr map `:96-115`) + build referent `palace/main.cpp:286-301` (`mesh::Load`/`Preprocess`/`Partition`/`RefineMesh` `:287-291`, wrap `:299`) + `palace/utils/geodata.{hpp:25-50,cpp:122,421}`; harvested cycle-117; firm-on-positive-structure, no-dedicated-test caveat non-gating per `fe_space`/`fe_assemble` precedent; laws: config-determinism, pipeline-staging (load▷preprocess▷partition▷refine, non-commuting), zero-refinement identity, a-priori level-monotonicity; non-laws: partition/distribution single-rank, MFEM-opaque adaptive AMR (lifecycle root's fold), libCEED geom-factor cache; **single-machine scope** flag-once-skip; L1>L0: `build-mesh-construction-rotation` named-not-authored) |
```

NOTE TO INTEGRATOR: the dep-map row above is a NEW kind-grouping row (`**Mesh & FE-space construction**`).
If D4 (layer-intro-author) introduces the kind grouping this cycle, fold the `build_mesh` row under it;
otherwise insert the `**Mesh & FE-space construction**` grouping header immediately BEFORE the existing
`**FE-space sub-spine**` grouping (alpha-within-kind: `build_mesh` is the sole row in the new grouping).
I do NOT touch the consolidated firm-count / running tally in `L1/index.md` §Vocabulary-cohort — that
defers to D4 (the layer-intro-author owns the layer-index narrative this cycle, per the parallel-blind
shared-index guard).

```edit:book/src/SUMMARY.md
- [Mesh & FE-space construction](./L1/index.md)
  - [build_mesh](./L1/build_mesh.md)
```

NOTE TO INTEGRATOR (SUMMARY): insert the `build_mesh` chapter entry under the L1 Part. Placement: a new
`Mesh & FE-space construction` sub-chapter grouping immediately BEFORE the existing `FE-space sub-spine`
grouping (`SUMMARY.md:221`), OR — if D4 authors a `mesh-construction-intro.md` group page this cycle —
fold `build_mesh` under that group page link instead of the `./L1/index.md` placeholder above. The anchor
(`./L1/build_mesh.md`) is distinct and parallel-safe regardless of grouping.

## Operator content
The full firm chapter body is authored inside the `new:book/src/L1/build_mesh.md` fenced block above
(`## Status` + Signature + Record definition + Algebraic laws + Scope + Downward + Evidence — the complete
firm apparatus is INSIDE the fence). Slug LOCKED to `build_mesh` per the dispatch (matches the
`lifecycle.L1` forward-ref `build_mesh :: Config -> Mesh`; D4 references `L1/build_mesh` for its `Mesh`
input type).

## Supporting evidence
- All L0 citations self-verified with `tools/citecheck/citecheck.py --anchor` against on-disk source
  (close-brace END lines confirmed by direct `Read` per the FE-source drift guard): `class Mesh`
  `palace/fem/mesh.hpp:44`; underlying `mesh` member `:49`; `loc_attr` `:58`; variadic ctor `:72-75`;
  `unique_ptr` ctor `EnsureNodes`/`Update` `:79-80` (ctor span `:76-81`); single-machine surface
  `GetNBE` `:96` (surface span `:84-96`); `mesh::Load` `palace/main.cpp:287`; `mesh::Partition` `:290`;
  `mesh::RefineMesh` `:291`; `Load` body `palace/utils/geodata.cpp:122`; `RefineMesh` body `:421`.
  (The prompt's pre-localized hints `:69-72`/`:73-77`/`:84-94` were off-by-one on the close-brace END
  lines — corrected here to the on-disk `:72-75`/`:76-81`/`:84-96` after direct `Read` confirmation, the
  FE-source close-brace drift the prompt explicitly warned about.)
- Sibling template: `book/src/L1/fe_space.md` (the FE-space construction firm chapter — the
  closest-shaped precedent: typed-object construction, MFEM-owned-read-as-given internals, firm-on-positive-
  structure no-dedicated-test, single-rank scope carve-outs).
- `book/src/feature/lifecycle.L1.md:37,44` — the consuming composition root.

## Open questions / caveats
- **`record-Mesh-needs-definition-home`** — `Mesh` has ≥2 consumers (every driver column's mesh stage +
  [`fe_space`](./fe_space.md)'s `mesh: Mesh` input + the deferred `fe_space_hierarchy`), so per the
  record-definition obligation it warrants a shared `book/src/concepts/mesh.md` page (layer-intro-author's
  domain). The in-chapter `## Record definition` section is the interim home; FLAG for a concept page.
  Likely co-locatable with D4's FE-space-construction work this cycle.
- **L1>L0 `build-mesh-construction-rotation` theme** — named, NOT authored. The forward rewrite of the
  `config → Mesh` pipeline into the L0 free-function chain + in-place `unique_ptr` mesh-handle mutation is a
  follow-on abstractor/harvester dispatch. No `lowers-to` edge asserted in front-matter until it lands.
- **Adaptive (AMR) mesh refinement obstruction** — `build_mesh` covers only **a-priori** (config-fixed)
  refinement; the adaptive error-estimator-driven refinement is the `lifecycle` root's outer
  estimate-mark-refine fold and bottoms out in MFEM-opaque `GeneralRefinement`. It stays
  obstruction-documented at the lifecycle root, NOT forced to a firm claim here. (Consistent with the
  directive's "MFEM-opaque mesh-refinement leaves stay obstruction-documented, not forced".)
- **Kind-grouping placement** — `build_mesh` opens a candidate new L1 kind grouping
  (`Mesh & FE-space construction`, or it may be folded into the existing `FE-space sub-spine` grouping).
  Deferred to D4 / integrator judgment (noted in the integrator NOTEs above); the index intro / grouping
  narrative is D4's (layer-intro-author) domain this cycle — flagged for intro refresh.
- **`config-record` cross-ref** — the `Config`/`IoData` surface is cross-referenced to
  [`config-record`](../concepts/config-record.md); confirmed that page exists (referenced by
  `eigenvalue-untransform` and others). The mesh-relevant fields (`model.mesh`, `model.refinement`) are a
  sub-surface of it — if `config-record.md` does not yet enumerate them, a thin addition there is a
  layer-intro follow-on (not blocking `build_mesh`).
