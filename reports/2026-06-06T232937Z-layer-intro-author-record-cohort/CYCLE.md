---
agent: layer-intro-author
invoked_at: 2026-06-06T232937Z
scope: cycle-118 D6 (batch-38) — record-definition cohort (Mesh / FiniteElementSpaceHierarchy / WaveguideModeTable) + Mesh-&-FE-space kind-grouping fold-vs-standalone decision
status: integrated
integrated_at: 2026-06-07T003000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean as c118 D6 (batch-38 opener, LAST apply). New firm concepts/mesh.md + concepts/WaveguideModeTable.md record-definition pages (kind: record, data-shape only) + 4 back-link re-points + mesh-construction kind-grouping KEEP-STANDALONE. build_mesh.md#record-definition anchor PRESERVED (all cross-file refs re-pointed to concepts/mesh.md). cargo make book EXIT 0; 0 dead links; rank_violations=0. OPEN: record-FiniteElementSpaceHierarchy-promote-watch (<2 firm consumers, KEPT in-chapter). 0 gate hits."
---

# CYCLE: record-definition cohort + mesh-construction kind-grouping decision

## Summary

Two bundled sub-tasks for the c117/c118 mesh→fe_space wave.

**Sub-task (a) — three per-record ≥2-consumer judgments:**

| record | current home | distinct signature/typed consumers | judgment |
|---|---|---|---|
| `Mesh` | in-chapter `L1/build_mesh.md#record-definition` | `build_mesh` (producer), `fe_space` (`mesh: Mesh` input :33/:72), `fe_space_hierarchy` (`[Mesh]` element type), `lifecycle.L1` stage-(1) (D4 grounded `lifecycle → build_mesh`) | **PROMOTE → `concepts/mesh.md`** (≥2 distinct consumers — in fact 4) |
| `FiniteElementSpaceHierarchy` | in-chapter `L1/fe_space_hierarchy.md` §Record-definition | only `fe_space_hierarchy` (sole harvested L1 producer/consumer); the geometric-multigrid preconditioner consumer is future/RE9, NOT yet firm-harvested | **KEEP in-chapter** + promote-watch (`< 2` FIRM consumers) |
| `WaveguideModeTable` | in-chapter `feature/waveguide-mode.L4.md` §Inputs/outputs | `waveguide-mode.L4` (signature `-> WaveguideModeTable`), `waveguide-mode.L1` (signature `waveguide_mode :: BoundaryModeConfig -> WaveguideModeTable` :26), `L4/waveguide_mode_reduce` (D5; signature `-> WaveguideModeTable`) | **PROMOTE → `concepts/WaveguideModeTable.md`** (3 distinct signature-naming chapters — the verb is a standalone L4 op chapter, not just a feature column; matches the `DofSet` 3-consumer precedent) |

**Sub-task (b) — kind-grouping decision (OQ `build-mesh-fe-space-kind-grouping-fold-residual-c117`): KEEP `Mesh & FE-space construction` as a standalone L1 kind grouping** (do NOT fold into the FE-space sub-spine). The grouping is coherent on its own — mesh construction (the geometric substrate) is a genuinely distinct kind from FE-space construction (the function space on a given mesh). The `mesh-construction-intro.md` body already draws that boundary explicitly ("Where the FE-space sub-spine constructs the function space … on a given mesh, this surface constructs the mesh itself"). The c118 wave adds L1>L0 *themes* (build-mesh / fe-space-hierarchy / interpolator construction-rotation), NOT new L1 *ops*, so `build_mesh` stays the sole L1 op in this grouping; the would-be siblings (MFEM-opaque adaptive AMR, `Par*` partitioning) are obstruction/out-of-scope and will not land as L1 ops. Closes the OQ. The grouping-intro is refreshed (re-point the `Mesh` record reference to the new `concepts/mesh.md`, record the closed fold-decision, note the now-grounded downward rotation). SUMMARY navigation is unchanged and link-safe (the grouping link already points at the live `mesh-construction-intro.md`).

This report is the SOLE owner this cycle of the `concepts/index.md` rows + `SUMMARY.md` concepts-Part rows it creates and the kind-grouping decision.

## Coordination notes (back-link re-pointing for the integrator)

Wave-1 reports referenced the records by their CURRENT in-chapter homes. With `Mesh` and `WaveguideModeTable` promoted, these back-links want re-pointing (the integrator or a follow-on lifter wires them — D6 decides page existence only):

- **`Mesh` → `concepts/mesh.md`** re-points needed:
  - `book/src/L1-L0/build-mesh-construction-rotation.md` (D1, landing this cycle): the two `[\`Mesh\` record definition\`](../L1/build_mesh.md#record-definition)` anchors (D1's report §L1-form + §Piece-3) → `[\`Mesh\`](../concepts/mesh.md)`. D1's own report (`reports/...abstractor-build-mesh-rotation/CYCLE.md:75,107,234`) flagged this exact follow-on.
  - `book/src/L1/build_mesh.md` §Record-definition stays as a **back-link stub** (re-pointed below in proposed-changes block (5)); `fe_space.md` / `fe_space_hierarchy.md` `Mesh` mentions are prose links to `build_mesh.md`, which still hosts the producer chapter — those resolve fine (they point at the producing chapter, not the `#record-definition` anchor), no re-point required, though a follow-on lifter MAY upgrade the bare `Mesh` mentions to the `concepts/mesh.md` link.
- **`WaveguideModeTable` → `concepts/WaveguideModeTable.md`** re-points needed:
  - `book/src/L4/waveguide_mode_reduce.md` (D5, landing this cycle): the in-chapter mention "The `WaveguideModeTable` record is defined in its current in-chapter home ([`waveguide-mode.L4`](../feature/waveguide-mode.L4.md), §Inputs/outputs)" → re-point to `[\`WaveguideModeTable\`](../concepts/WaveguideModeTable.md)`. D5's report (`reports/...combinator-miner-waveguide-mode-reduce/CYCLE.md:528-532`) explicitly deferred this judgment to D6.
  - `book/src/feature/waveguide-mode.L4.md` §Inputs/outputs (the current home) → re-pointed below in proposed-changes block (8) to a back-link stub.
  - `book/src/feature/waveguide-mode.L1.md:52` output-product bullet → MAY upgrade the `WaveguideModeTable` mention to the `concepts/WaveguideModeTable.md` link (follow-on; not required for build-safety).

All these are read-only-to-D6 (D6 does not edit D1's/D5's reports or the constituent op chapters beyond the record-home back-link stubs in the producing chapters, which is the record-definition-obligation's own re-point allowance).

## Proposed changes

### (1) Create `concepts/mesh.md` — the `Mesh` record-definition page

```new:book/src/concepts/mesh.md
---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/fem/mesh.hpp:44-115
      kind: cites-evidence
  reference:
    - L1/build_mesh
    - L1/fe_space
    - L1/fe_space_hierarchy
    - feature/lifecycle.L1
    - concepts/config-record
    - concepts/build-time-vs-run-time-stratification
---

# Mesh

> **Kind: `record`.** This page defines the *data shape* of `Mesh` — its fields, their
> types and meaning, the construction-vs-run-time stratum of each, and the L0 source home
> the backing C++ struct mirrors. The *behaviour* — how [`build_mesh`](../L1/build_mesh.md)
> constructs it and how [`fe_space`](../L1/fe_space.md) / [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md)
> consume it — lives in those operator chapters; this page does not restate that algebra.

`Mesh` is the Palace **wrapper for the discretised computational domain** — the geometric
substrate every assembled-operator pipeline stands on. It owns a single-rank `mfem::ParMesh`
(read single-rank per the standing `par-types-single-rank-reading` rule; MPI/`Par*`/partitioning
out of scope) augmented with the libCEED local-attribute mapping needed to assemble libCEED
operators over the mesh. It is **produced** by [`build_mesh`](../L1/build_mesh.md)
(`build_mesh :: Config -> Mesh`) and **consumed** by [`fe_space`](../L1/fe_space.md)
(`mesh: Mesh` input), [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) (`[Mesh]` element
type), and the [`lifecycle`](../feature/lifecycle.L1.md) composition root's stage-(1). Four
distinct consumers put it above the ≥2-consumer bar, so it has a cross-cutting definition home
here rather than only an in-chapter section in its producing chapter.

## One-line semantics

`Mesh` is an immutable typed geometric value — a single-rank `mfem::ParMesh` plus the libCEED
attribute maps — over which the FE-space construction reads the geometric axes (`Dimension`,
`SpaceDimension`, element count `GetNE`, boundary-element count `GetNBE`). It carries no algebra
of its own; the constructor and the FE-space ops supply all behaviour.

## Record definition

`Mesh` is the backing C++ `class Mesh` (`palace/fem/mesh.hpp:44`). The TS brace form (the value
is immutable once constructed; per-field strata below):

```text
Mesh = {
  mesh          : unique_ptr<mfem::ParMesh>,   -- the underlying MFEM mesh (single-rank)
  loc_attr      : Map<int, int>,               -- global domain attr -> local libCEED attr
  loc_bdr_attr  : Map<int, Map<int, int>>,     -- global bdr attr -> (neighbour domain attr -> local bdr attr)
  ceed_from_self: bool,                         -- true after RebuildCeedAttributes()
  geom_data     : CeedObjectMap<CeedGeomFactorData>  -- cached libCEED geometry factors (transparent)
}
```

| field | type | meaning | stratum | L0 source |
|---|---|---|---|---|
| `mesh` | `unique_ptr<mfem::ParMesh>` (single-rank) | the underlying MFEM mesh object; can also point to a derived `mfem::ParSubMesh` (boundary-mode submesh extraction) | construction-time (owns the loaded/partitioned/refined mesh) | `palace/fem/mesh.hpp:47-49` |
| `loc_attr` | `unordered_map<int,int>` | global (MFEM, 1-based) **domain** attribute → process-local contiguous (1-based) libCEED attribute | construction-time (built by `Update()`; single-rank = identity-flavoured remap) | `palace/fem/mesh.hpp:51-58` |
| `loc_bdr_attr` | `unordered_map<int, unordered_map<int,int>>` | global **boundary** attribute → (neighbouring domain attr → local boundary attr) — discriminates boundary elements bordering more than one domain | construction-time | `palace/fem/mesh.hpp:51-59` |
| `ceed_from_self` | `bool` | true after `RebuildCeedAttributes()` | run-time flag | `palace/fem/mesh.hpp:60` |
| `geom_data` | `mutable ceed::CeedObjectMap<ceed::CeedGeomFactorData>` | cached libCEED geometry-factor quadrature data (`w·|J|`, `adj(J)^T/|J|`) per element-geometry/thread | run-time (transparent cache, re-derivable on demand — a performance store, NOT lifted structure) | `palace/fem/mesh.hpp:62-69` |

The single-machine **read surface** (read-as-given accessors, NOT operations): `Get()` /
`Dimension()` / `SpaceDimension()` / `GetNE()` / `GetNBE()` (`palace/fem/mesh.hpp:84-96`); the
libCEED attribute-map accessors `GetCeedAttributes` / `GetCeedBdrAttributes`
(`palace/fem/mesh.hpp:96-115`). These expose the geometric axes the FE-space construction reads
(`fe_space`'s `mesh: Mesh` input pairs `Dimension`/`SpaceDimension`/`GetNE`/`GetNBE` with an
`FECollection` to define the true-dof axis `N`).

## Stratum — construction-time, immutable-once-built

`Mesh` is **construction-stratum**: it is built once at the start of every solver pipeline (the
lifecycle stage-(1) mesh block) and consumed read-only thereafter — there is no per-iteration
solve-time mutation of the geometric value (the adaptive estimate-mark-refine loop produces a
*new* `Mesh` per AMR iterate at the lifecycle root, it does not mutate an existing one). The
construction-vs-run-time split per field (above) is the
[`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md) pattern:
`mesh` / `loc_attr` / `loc_bdr_attr` are built-at-construction scaffolding; `geom_data` is a
run-time transparent cache (a performance store, re-derivable, NOT lifted structure — the
`fe_space` libCEED-cache precedent).

Concretely in Palace: the `unique_ptr`-adopting ctor `Mesh(std::unique_ptr<T> &&mesh)`
(`palace/fem/mesh.hpp:76-81`) runs `EnsureNodes()` (`:79`, geometry finalization) + `Update()`
(`:80`, builds the `loc_attr` / `loc_bdr_attr` libCEED maps) at construction; the variadic ctor
(`:72-75`) builds the `mfem::ParMesh` from forwarded args then delegates to the adopting ctor.
The construction finalization (`EnsureNodes()` + `Update()`) is the L1>L0
[`build-mesh-construction-rotation`](../L1-L0/build-mesh-construction-rotation.md) theme's Piece-3.

## L0 source home — the `class Mesh` wrapper

The backing C++ struct is `class Mesh` (`palace/fem/mesh.hpp:44`). Its construction lifecycle
across the L0 surface (the mesh block of `main`, `palace/main.cpp:286-301`): `mesh::Load` →
`solver->Preprocess` → `mesh::Partition` (read single-rank) → `mesh::RefineMesh` →
`make_unique<Mesh>(std::move(m))` (the adopting ctor). The config-relevant `IoData` surface this
record mirrors is `model.mesh` (the mesh file) + `model.refinement` (the a-priori refinement
config), part of `config::ModelData` — cross-ref [`config-record`](./config-record.md)
(`model : config::ModelData`, `iodata.hpp:32`, struct `configfile.hpp:156`).

**Single-machine carve-outs (flagged once).** The `mfem::ParMesh` is read single-rank; the
global→process-local libCEED attribute remap (`loc_attr` / `loc_bdr_attr`) collapses to a
single-process contiguous relabeling on one rank. The `mesh::Partition` distribution stage is
the identity distribution; the multi-rank partition policy is out of scope. This record carries
the maps but does not define the multi-rank remap semantics (per CLAUDE.md §Scope).

## Signatures that name this record

The ≥2-consumer evidence for the standalone page (four consumers):

- [`build_mesh`](../L1/build_mesh.md) — the **producer**: `build_mesh :: Config -> Mesh`
  (`book/src/L1/build_mesh.md:27,62`).
- [`fe_space`](../L1/fe_space.md) — the primary consumer; its `mesh: Mesh` parameter
  (`fe_space :: (mesh: Mesh, collection: FECollection) -> FiniteElementSpace[N]`,
  `book/src/L1/fe_space.md:33,68,72`).
- [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) — the `[Mesh]` coarse-to-fine input list
  element type (`fe_space_hierarchy :: [Mesh] -> [FECollection] -> Config ->
  FiniteElementSpaceHierarchy`, `book/src/L1/fe_space_hierarchy.md:33,89-93`).
- [`lifecycle.L1`](../feature/lifecycle.L1.md) — the composition root's stage-(1) build_mesh
  output threaded through the whole pipeline + the AMR fold (`book/src/feature/lifecycle.L1.md:39,44`).

## See also

- [`build_mesh`](../L1/build_mesh.md) — the producer; defines HOW the mesh is constructed
  (load → preprocess → partition → a-priori-refine). This page defines only the *shape* of its
  output.
- [`build-mesh-construction-rotation`](../L1-L0/build-mesh-construction-rotation.md) — the L1>L0
  theme; the construction finalization (`EnsureNodes()` + `Update()` building this record's
  attribute maps) is its Piece-3.
- [`fe_space`](../L1/fe_space.md) / [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) — the
  consumers; define the *behaviour over* the mesh (pairing it with an `FECollection` to build the
  space). This page does NOT restate that algebra.
- [`config-record`](./config-record.md) — the `IoData` surface (`model.mesh` + `model.refinement`)
  this record's construction reads from.
- [`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md) — the
  per-field construction-vs-run-time split (`mesh`/`loc_attr`/`loc_bdr_attr` build-time;
  `geom_data` run-time cache).

**If this page and a consumer chapter / the L0 source disagree on any factual claim about the
record, the L0 source (`palace/fem/mesh.hpp`) wins and this page is corrected.**

## Status

`firm` — the data shape is read directly from the positive `class Mesh` wrapper
(`palace/fem/mesh.hpp:44-115`): the underlying `mfem::ParMesh` (`:47-49`), the libCEED attribute
maps (`:51-59`), the `ceed_from_self` flag (`:60`) + `geom_data` cache (`:62-69`), the ctor chain
(`:72-81`) with `EnsureNodes()`+`Update()` finalization (`:79-80`), and the single-machine read
surface (`:84-115`). The construction-vs-run-time stratum per field is read off the ctor + the
member comments. The record-definition obligation is met: this is the cross-cutting home for
`Mesh`, referenced by ≥2 consumers (`L1/build_mesh`, `L1/fe_space`, `L1/fe_space_hierarchy`,
`feature/lifecycle.L1`). All L0 citations self-verified against on-disk source this dispatch via
codemap `read_range`.

Well-foundedness (rank): the page is a `record` DAG node at `rank: firm`; its only blocking edge
is `cites-evidence depends-on` to the L0 `class Mesh` range (rank-terminal ground truth), so the
`rank(u) ≤ rank(v)` invariant holds vacuously. The edges to the producer/consumer chapters and
the config surface are `reference` (navigational — a record page is named-by-use, it does not
block on its consumers).
```

### (2) Add `concepts/mesh.md` to the `concepts/index.md` index table (alpha position: after `matrix-weighted-norm`? no — `mesh` sorts after `ksp_solve` and before `negative-result-slice`; insert after `krylov`/`ksp_solve`, before `negative-result-slice`)

Insert the index-table row in alpha position — `mesh` sorts after `ksp_solve` and before `negative-result-slice`:

```edit:book/src/concepts/index.md
| [krylov](./krylov.md) | record |
| [ksp_solve](./ksp_solve.md) | layer-pattern |
| [Mesh](./mesh.md) | record |
| [negative-result-slice](./negative-result-slice.md) | methodology |
```

(Integrator: this REPLACES the existing `krylov` / `ksp_solve` / `negative-result-slice` three-row block at `book/src/concepts/index.md:179-181` by inserting the `Mesh` row between `ksp_solve` and `negative-result-slice`, preserving alpha order. `M` < `n` case-insensitively; the `WaveguideModeTable` row from block (6) sorts to the end.)

### (3) Add `concepts/mesh.md` to the `concepts/index.md` frontmatter `reference:` edge list (alpha position, after `concepts/ksp_solve`)

```edit:book/src/concepts/index.md
    - concepts/ksp_solve
    - concepts/mesh
    - concepts/negative-result-slice
```

(Integrator: insert `    - concepts/mesh` between `    - concepts/ksp_solve` (`:42`) and `    - concepts/negative-result-slice` (`:43`) in the index frontmatter `reference:` list.)

### (4) Add `concepts/mesh.md` to `SUMMARY.md` (alpha within the concepts Part, after `ksp_solve`, before `negative-result-slice`)

```edit:book/src/SUMMARY.md
  - [ksp_solve](./concepts/ksp_solve.md)
  - [Mesh — record definition](./concepts/mesh.md)
  - [negative-result-slice](./concepts/negative-result-slice.md)
```

(Integrator: insert `  - [Mesh — record definition](./concepts/mesh.md)` between `  - [ksp_solve](./concepts/ksp_solve.md)` (`:335`) and `  - [negative-result-slice](./concepts/negative-result-slice.md)` (`:336`).)

### (5) Re-point the `L1/build_mesh.md` in-chapter `## Record definition` to a back-link stub

The producing chapter keeps a short back-link to the cross-cutting home (the `DofSet` /
`eliminate_bc` precedent: the producing chapter points at the concepts page, does not duplicate
the full table). Replace the §Record-definition body (the single-consumer-judgment prose + the
full field table + the backing-struct paragraph, `book/src/L1/build_mesh.md:82-107`) with:

```edit:book/src/L1/build_mesh.md
## Record definition

`Mesh` is defined in its cross-cutting home [`concepts/mesh.md`](../concepts/mesh.md) (the
record-definition page: fields, types, per-field construction-vs-run-time stratum, and the L0
`class Mesh` backing home `palace/fem/mesh.hpp:44-115`). It has ≥2 consumers — this chapter
(`build_mesh`, the **producer**), [`fe_space`](./fe_space.md) (`mesh: Mesh` input),
[`fe_space_hierarchy`](./fe_space_hierarchy.md) (`[Mesh]` element type), and the
[`lifecycle`](../feature/lifecycle.L1.md) root's stage-(1) — so per the record-definition
obligation it has a shared `concepts/` home (promoted c118 D6) rather than an in-chapter table.
In brief: `Mesh` wraps a single-rank `mfem::ParMesh` augmented with the libCEED domain/boundary
local-attribute maps (`loc_attr` / `loc_bdr_attr`), finalized at construction by the adopting
ctor's `EnsureNodes()` + `Update()` (`palace/fem/mesh.hpp:76-81`); see the
[`Mesh` record page](../concepts/mesh.md) for the full schema.
```

(Integrator: also update the §Status `**Mesh record home:**` note `book/src/L1/build_mesh.md:208-210` — the "flagged (`record-Mesh-needs-definition-home`)" claim is now stale; the page landed. Exact edit:)

```edit:book/src/L1/build_mesh.md
**`Mesh` record home:** the cross-cutting [`concepts/mesh.md`](../concepts/mesh.md) record page
is the definition home (promoted c118 D6, since `Mesh` has ≥2 consumers); this chapter's
§Record-definition is a back-link to it (the OQ `record-Mesh-needs-definition-home` is resolved).
```

### (6) Create `concepts/WaveguideModeTable.md` — the `WaveguideModeTable` record-definition page

```new:book/src/concepts/WaveguideModeTable.md
---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/drivers/boundarymodesolver.cpp:272-340
      kind: cites-evidence
    - target: palace/models/modeeigensolver.cpp:516-519
      kind: cites-evidence
  reference:
    - L4/waveguide_mode_reduce
    - feature/waveguide-mode.L4
    - feature/waveguide-mode.L1
    - feature/boundary-mode.L4
    - concepts/config-record
---

# WaveguideModeTable

> **Kind: `record`.** This page defines the *data shape* of `WaveguideModeTable` — its row
> schema, the per-field types and meaning, the construction-vs-run-time stratum, and the L0
> readout source it mirrors. The *behaviour* — how [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md)
> constructs it from the boundary-mode eigenpair family — lives in that operator chapter; this
> page does not restate that reduction algebra.

`WaveguideModeTable` is the **boundary-mode (2D waveguide-mode analysis) output product**: a
per-mode table characterizing each converged propagation mode. One row per converged mode, each
`{kn, n_eff, (Et, En, Bz)}` — the propagation constant `kn`, the effective index `n_eff = kn/ω`,
and the mode-field triple `(Et, En, Bz)` (the transverse H(curl) field `Et`, the longitudinal H1
field `En`, and, for propagating modes only, the longitudinal magnetic field
`Bz = curl(Et)/(iω)`). It is the physical product the user runs the boundary-mode solver to
obtain. It is **produced** by [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md)
(`waveguide_mode_reduce :: EigResult -> Scalar -> WaveguideModeTable`) and named in the signatures
of the [`waveguide-mode.L4`](../feature/waveguide-mode.L4.md) and
[`waveguide-mode.L1`](../feature/waveguide-mode.L1.md) feature columns. Three distinct
signature-naming chapters (the standalone reduce-verb chapter + the two column levels) put it
above the ≥2-consumer bar, so it has a cross-cutting definition home here.

## One-line semantics

`WaveguideModeTable` is an immutable per-mode list — one row per converged waveguide mode, each
mixing complex propagation scalars (`kn`, `n_eff`) with rank-1 mode-field dof-vectors
(`Et`, `En`, `Bz`). It carries no algebra of its own; the reduce verb supplies all behaviour.

## Record definition

`WaveguideModeTable` is a list of per-mode rows. The TS brace form (each row immutable,
constructed by the per-mode reduce):

```text
WaveguideModeTable = [ WaveguideModeRow ]

WaveguideModeRow = {
  kn   : Complex,                          -- propagation constant
  n_eff: Complex,                          -- effective index = kn / ω
  Et   : Tensor[N_nd,   complex],          -- transverse H(curl) mode field (flat ND dof-vector)
  En   : Tensor[N_h1,   complex],          -- longitudinal H1 mode field    (flat H1 dof-vector)
  Bz   : Maybe (Tensor[N_curl, complex])   -- longitudinal B (propagating modes only)
}
```

| field | type | meaning | stratum | L0 source |
|---|---|---|---|---|
| `kn` | `Complex` | propagation constant — the shift-invert un-transform of the eigenvalue (`eig.GetPropagationConstant(i)`) | construction (readout) | `palace/drivers/boundarymodesolver.cpp:299` (un-transform), `:274` (reported) |
| `n_eff` | `Complex` | effective index `= kn / ω` | construction (readout) | `palace/drivers/boundarymodesolver.cpp:276` |
| `Et` | `Tensor[N_nd, complex]` | transverse H(curl) mode field — the VD-back-transform of the eigenvector, power-normalized so `|P| = 1` (genuine flat rank-1 dof-vector on the 2D-submesh ND space) | construction (readout) | `palace/drivers/boundarymodesolver.cpp:300` (`ApplyVDBackTransform`), `:304-307` (normalize) |
| `En` | `Tensor[N_h1, complex]` | longitudinal H1 mode field — the H1 component of the same VD-back-transform (flat rank-1 dof-vector on the 2D-submesh H1 space) | construction (readout) | `palace/drivers/boundarymodesolver.cpp:300` |
| `Bz` | `Maybe (Tensor[N_curl, complex])` | longitudinal magnetic field `Bz = curl(Et)/(iω)` — present (`Just`) only for propagating modes (`IsPropagating(kn)`), `Nothing` for evanescent | construction (readout) | `palace/drivers/boundarymodesolver.cpp:316-333` (formation), `palace/models/modeeigensolver.cpp:516-519` (`IsPropagating` predicate) |

The mode fields `Et` / `En` / `Bz` are **genuine flat rank-1 dof-vectors** on the 2D-submesh ND /
H1 / curl spaces — `Tensor[N]` is correct here per the semantic surface
[`semantics`](../semantics/index.md) §1.2.1 (NOT a named shape group); `kn` / `n_eff` are complex
scalars; `Bz` is `Maybe` (propagating modes only). The element-type is **pinned complex** —
waveguide modes are intrinsically complex (`kn` / `n_eff` / `(Et,En,Bz)` all complex).

## Stratum — construction-time (readout), immutable

`WaveguideModeTable` is **construction-stratum**: each row is materialized once by the per-mode
readout of the converged boundary-mode eigenpair family (after the single `eigsolve`), then read
as the final product. There is no per-iteration solve-time mutation — the reduction is a pure
`map`-then-collect over the eigenpair family with no inter-mode state (the readout loop carries no
accumulator). The whole table is the output of one reduction at a single operating frequency ω
(ω rides as a fixed scalar parameter, not a per-mode datum — the `n_eff` divisor + the `Bz` `1/ω`
scale). This is the [`build-time-vs-run-time-stratification`](./build-time-vs-run-time-stratification.md)
output-product side: the table is the constructed result, not run-time iteration scaffolding.

## L0 source home — the boundary-mode readout loops

The backing L0 surface is the boundary-mode driver's two per-mode readout loops
(`palace/drivers/boundarymodesolver.cpp:272-340`): the `kn` / `n_eff` print loop (`:272-278`) and
the field-readout + `Bz`-formation loop (`:292-335`). Palace materializes the rows imperatively
into per-mode `kn` / `(et, en)` / `Bz` values reported through `post_op.MeasureAndPrintAll(...)`
(`:314`); it does not name a single C++ struct for the whole table — `WaveguideModeTable` is the
lifted record of that scattered per-mode readout. The `IsPropagating` predicate that keys the
`Bz` `Maybe` is `ModeEigenSolver::IsPropagating(kn)` (`palace/models/modeeigensolver.cpp:516-519`:
`|kn.imag()| < 0.1·|kn.real()| ∧ |kn.real()| > 0`). The config-relevant `IoData` surface is
`iodata.solver.boundary_mode` (the operating frequency → ω, the boundary attributes → the
2D-submesh, the mode counts → the table rows) — cross-ref [`config-record`](./config-record.md).

## Signatures that name this record

The ≥2-consumer evidence for the standalone page (three signature consumers):

- [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) — the **producer** (L4 reduce verb):
  `waveguide_mode_reduce :: EigResult -> Scalar -> WaveguideModeTable` (D5 this cycle).
- [`waveguide-mode.L4`](../feature/waveguide-mode.L4.md) — the output-product composition root:
  `waveguide_mode :: BoundaryModeConfig -> WaveguideModeTable`
  (`book/src/feature/waveguide-mode.L4.md:30`).
- [`waveguide-mode.L1`](../feature/waveguide-mode.L1.md) — the L1 column:
  `waveguide_mode :: BoundaryModeConfig -> WaveguideModeTable`
  (`book/src/feature/waveguide-mode.L1.md:26`).

## See also

- [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) — the producer; defines HOW each row
  is constructed (eigenvalue un-transform → `kn`, `n_eff = kn/ω`, VD back-transform → `(Et, En)`,
  Poynting power-normalization, conditional curl `Bz`). This page defines only the *shape* of its
  output.
- [`waveguide-mode.L4`](../feature/waveguide-mode.L4.md) /
  [`waveguide-mode.L1`](../feature/waveguide-mode.L1.md) — the feature columns; define the
  *composition* that produces the table (reduce ∘ boundary-mode driver). This page does NOT
  restate that composition.
- [`boundary-mode.L4`](../feature/boundary-mode.L4.md) — the producing driver column (the 2D-submesh
  eigenpair family the reduction consumes).
- [`config-record`](./config-record.md) — the `iodata.solver.boundary_mode` surface (ω + boundary
  attributes + mode counts) the table's construction reads from.

**If this page and a consumer chapter / the L0 source disagree on any factual claim about the
record, the L0 source (`palace/drivers/boundarymodesolver.cpp` / `palace/models/modeeigensolver.cpp`)
wins and this page is corrected.**

## Status

`firm` — the row schema is read directly from the positive boundary-mode readout loops
(`palace/drivers/boundarymodesolver.cpp:272-340`): the `kn` un-transform (`:299`), `n_eff` divide
(`:276`), the VD back-transform `(Et, En)` (`:300`) + power-normalization (`:304-307`), and the
conditional `Bz = curl(Et)/(iω)` (`:316-333`) keyed on `IsPropagating(kn)`
(`palace/models/modeeigensolver.cpp:516-519`). The per-field construction stratum is the readout
of the converged eigenpair family. The record-definition obligation is met: this is the
cross-cutting home for `WaveguideModeTable`, referenced by ≥2 signature consumers
(`L4/waveguide_mode_reduce`, `feature/waveguide-mode.L4`, `feature/waveguide-mode.L1`). All L0
citations self-verified against on-disk source this dispatch via codemap `read_range`.

Well-foundedness (rank): the page is a `record` DAG node at `rank: firm`; its blocking edges are
`cites-evidence depends-on` to L0 source ranges (rank-terminal ground truth), so the
`rank(u) ≤ rank(v)` invariant holds vacuously. The edges to the producer verb chapter, the feature
columns, and the config surface are `reference` (navigational — a record page is named-by-use, it
does not block on its consumers).
```

### (7) Add `concepts/WaveguideModeTable.md` to `concepts/index.md` (index table — end of alpha order; `W` sorts after `variant-absorption`)

```edit:book/src/concepts/index.md
| [variant-absorption](./variant-absorption.md) | methodology |
| [WaveguideModeTable](./WaveguideModeTable.md) | record |
```

(Integrator: append the `WaveguideModeTable` row after the last index-table row `variant-absorption` at `book/src/concepts/index.md:203` — `W` sorts last, case-insensitive after `v`.)

### (8) Add `concepts/WaveguideModeTable.md` to `concepts/index.md` frontmatter `reference:` edge list (end — after `concepts/variant-absorption`)

```edit:book/src/concepts/index.md
    - concepts/variant-absorption
    - concepts/WaveguideModeTable
---
```

(Integrator: insert `    - concepts/WaveguideModeTable` after `    - concepts/variant-absorption` (`:65`), as the last entry before the closing `---`.)

### (9) Add `concepts/WaveguideModeTable.md` to `SUMMARY.md` (end of concepts Part, after `variant absorption`)

```edit:book/src/SUMMARY.md
  - [variant absorption — methodology concept](./concepts/variant-absorption.md)
  - [WaveguideModeTable — record definition](./concepts/WaveguideModeTable.md)
```

(Integrator: insert `  - [WaveguideModeTable — record definition](./concepts/WaveguideModeTable.md)` after `  - [variant absorption — methodology concept](./concepts/variant-absorption.md)` (`:358`), as the last concepts-Part entry.)

### (10) Re-point the `feature/waveguide-mode.L4.md` §Inputs/outputs `WaveguideModeTable` definition to a back-link

The output-product column's §Inputs/outputs currently hosts the in-chapter record definition. Add a
back-link line so the cross-cutting home is the authority (the column keeps its compositional output
description, but the *schema* authority is the concepts page). Replace the §Inputs/outputs Output
bullet (`book/src/feature/waveguide-mode.L4.md:54`) with a version pointing at the page:

```edit:book/src/feature/waveguide-mode.L4.md
- **Output — the physical product.** `WaveguideModeTable` — one row per converged mode, each `{kn, n_eff, (Et, En, Bz)}` (`Bz` present only for propagating modes). The record's data shape (row schema, per-field types/strata, the L0 readout home) is defined in its cross-cutting home [`concepts/WaveguideModeTable.md`](../concepts/WaveguideModeTable.md) (promoted c118 D6 — ≥2 signature consumers: the [`waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md) verb + this L4 column + the L1 column). This is what the user runs the boundary-mode solver to compute (waveguide / wave-port mode characterization). L0 home: the per-mode `kn`/`(et, en)`/`Bz` measured by `post_op.MeasureAndPrintAll(...)` (`boundarymodesolver.cpp:314`) + the `Bz` formation (`:316-333`).
```

(Integrator: this REPLACES the single Output bullet at `book/src/feature/waveguide-mode.L4.md:54`, adding the concepts-page back-link; the rest of §Inputs/outputs + the shape-contract code block stay as-is — the shape contract is the compositional view, the page is the authoritative schema. NOTE the cross-link wiring is allowed here per the record-definition-obligation re-point allowance.)

### (11) Refresh the `L1/mesh-construction-intro.md` group intro — record the closed fold-decision + re-point the `Mesh` reference

The kind-grouping stays standalone (sub-task b decision). Re-point the `Mesh` record reference to the
new concepts page, record the closed fold-decision, and note the now-grounded downward rotation.

```edit:book/src/L1/mesh-construction-intro.md
# L1 — Mesh & FE-space construction

The geometric-substrate surface upstream of the FE-space sub-spine: the single-machine **mesh construction** that produces the [`Mesh`](../concepts/mesh.md) typed value every solver pipeline stands on. Where the FE-space sub-spine constructs the function space (and its hierarchy + boundary-dof sets) on a given mesh, this surface constructs the mesh itself — load → preprocess → partition (read single-rank) → a-priori refine — from the `Config`/`IoData` surface. This is a **standalone kind grouping** (NOT folded into the FE-space sub-spine — OQ `build-mesh-fe-space-kind-grouping-fold-residual-c117` resolved c118 D6): mesh construction (the geometric substrate) is a genuinely distinct kind from FE-space construction (the function space on a given mesh), and the boundary is drawn explicitly above.

Currently one member: [`build_mesh`](./build_mesh.md) (`(config: Config) → Mesh`), the a-priori half of the lifecycle-root stage-(1) mesh build; its L1>L0 forward rewrite is the [`build-mesh-construction-rotation`](../L1-L0/build-mesh-construction-rotation.md) theme (c118), and its produced [`Mesh`](../concepts/mesh.md) value has a cross-cutting record-definition home (c118 D6). The MFEM-opaque adaptive-AMR refinement leaf stays obstruction-documented at the lifecycle root (not forced); the `Par*` / distributed mesh-partitioning stage is read single-rank (flag-once-skip, out of scope). The grouping stays single-member because the would-be siblings are out-of-scope / MFEM-opaque — it is not a transitional under-population (a future single-machine mesh-accessor / derived-submesh op would land here).

Chapters are listed alphabetically.
```

## Supporting evidence

- **`Mesh` consumers** (the ≥2-consumer judgment): `book/src/L1/build_mesh.md:27,62` (producer);
  `book/src/L1/fe_space.md:33,68,72` (`mesh: Mesh` input); `book/src/L1/fe_space_hierarchy.md:33,89-93`
  (`[Mesh]` element type); `book/src/feature/lifecycle.L1.md:39,44` (stage-(1)). L0 backing:
  `palace/fem/mesh.hpp:44-115` (`class Mesh`), self-verified on-disk this dispatch via codemap
  `read_range` (`:44-115` read — `class Mesh` `:44`, `unique_ptr<mfem::ParMesh> mesh` `:49`, attr maps
  `:51-59`, `geom_data` `:62-69`, ctor chain `:72-81` with `EnsureNodes()`+`Update()` `:79-80`, read
  surface `:84-115`).
- **`FiniteElementSpaceHierarchy` consumers** (the KEEP judgment): sole harvested L1 producer/consumer is
  `fe_space_hierarchy` itself (`book/src/L1/fe_space_hierarchy.md:118-138` §Record-definition, already
  states "single-consumer: `fe_space_hierarchy` is the sole harvested L1 producer/consumer of this type;
  its downstream geometric-multigrid solver consumers are not yet L1-harvested"). L0 backing:
  `palace/fem/fespace.hpp:200-286` (`class FiniteElementSpaceHierarchy`; verified on-disk `:200-225`
  ctor/`AddLevel` + `:225-286` accessors incl. close brace `}` `:286`).
- **`WaveguideModeTable` consumers** (the PROMOTE judgment): `book/src/L4/waveguide_mode_reduce.md`
  (D5; signature `-> WaveguideModeTable`); `book/src/feature/waveguide-mode.L4.md:30` (signature);
  `book/src/feature/waveguide-mode.L1.md:26` (signature). L0 backing: `palace/drivers/boundarymodesolver.cpp:272-340`
  (the two readout loops) + `palace/models/modeeigensolver.cpp:516-519` (`IsPropagating`) — cited from D5's
  self-verified anchors (D5 re-verified all on-disk this cycle; D6 reuses them for the record-shape page,
  which restates only the row schema, not the reduction algebra).
- **Record-page template:** `book/src/concepts/dofset.md` (the `record` kind format — frontmatter
  `rank: firm` / `kind: record` / `cites-evidence depends-on` + `reference`; the body schema-table +
  stratum + L0-source-home + signature-consumers + L0-source-wins note). `book/src/concepts/index.md`
  (the `record` Kind row + the index format).
- **Kind-grouping decision evidence:** `book/src/SUMMARY.md:50-56` (the two adjacent L1 groupings:
  `Mesh & FE-space construction` [1 member] + `FE-space sub-spine` [5 members]);
  `book/src/L1/mesh-construction-intro.md:13` (the explicit boundary "this surface constructs the mesh
  itself" vs the FE-space sub-spine constructing the function space); `book/src/L1/fe-space-intro.md:14-18`
  (the FE-space sub-spine's distinct scope).

## Open questions / caveats

Append to `scaffolding/open-questions.md`:

- `build-mesh-fe-space-kind-grouping-fold-residual-c117` (RESOLVED c118 D6, KEEP-STANDALONE) — the
  `Mesh & FE-space construction` L1 kind grouping stays standalone (NOT folded into the FE-space
  sub-spine). Rationale: mesh construction (geometric substrate) is a distinct kind from FE-space
  construction (function space on a mesh); the c118 wave added L1>L0 *themes* not new L1 *ops*, so
  `build_mesh` stays the sole member; the would-be siblings (MFEM-opaque adaptive AMR, `Par*`
  partitioning) are obstruction/out-of-scope and won't land as L1 ops. The grouping-intro records the
  closed decision. A future single-machine mesh-accessor / derived-submesh op would land in this grouping.
- `record-Mesh-needs-definition-home` (RESOLVED c118 D6) — `concepts/mesh.md` landed (≥2 consumers:
  `build_mesh` producer + `fe_space` + `fe_space_hierarchy` + `lifecycle.L1`). The `L1/build_mesh.md`
  in-chapter §Record-definition is re-pointed to a back-link stub.
- `record-WaveguideModeTable-needs-definition-home` (RESOLVED c118 D6) — `concepts/WaveguideModeTable.md`
  landed (3 signature consumers: the `waveguide_mode_reduce` verb + the L4 + L1 columns). The
  `feature/waveguide-mode.L4.md` §Inputs/outputs is re-pointed to the page (the D5 caveat that deferred
  this judgment to D6 is closed).
- `record-FiniteElementSpaceHierarchy-promote-watch` (OPEN, promote-watch) — `FiniteElementSpaceHierarchy`
  KEPT in-chapter at `L1/fe_space_hierarchy.md` §Record-definition (< 2 FIRM consumers: only
  `fe_space_hierarchy` itself; the geometric-multigrid preconditioner consumer is future/RE9, not yet
  firm-harvested). PROMOTE to `concepts/FiniteElementSpaceHierarchy.md` once a SECOND firm consumer lands
  (the geometric-multigrid preconditioner op that consumes the hierarchy + its prolongation/interpolator
  operators — the deferred RE9 consumer). The in-chapter section's own
  "single-consumer" note (`fe_space_hierarchy.md:120-123`) is the watch anchor.
- Caveat (back-link re-pointing, for the integrator): D1's `build-mesh-construction-rotation.md` and D5's
  `waveguide_mode_reduce.md` (both landing this cycle) reference the records by their OLD in-chapter homes
  (`../L1/build_mesh.md#record-definition` and the `waveguide-mode.L4` §Inputs/outputs). With both records
  promoted, those back-links want re-pointing to `../concepts/mesh.md` / `../concepts/WaveguideModeTable.md`
  — enumerated in §Coordination-notes above. D6 owns page existence; the integrator (or a follow-on lifter)
  wires the wave-1 back-links. Build-safety: the OLD `#record-definition` anchor in `build_mesh.md` is
  re-pointed to a back-link STUB (block 5) that still carries an in-chapter §Record-definition heading, so
  `../L1/build_mesh.md#record-definition` still resolves to a live heading (no `linkcheck2` break) even if
  the re-point of D1's links lags to a follow-on.
