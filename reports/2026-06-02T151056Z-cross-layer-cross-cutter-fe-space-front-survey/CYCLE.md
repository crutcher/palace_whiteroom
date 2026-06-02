---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-02T15:16:45Z
scope: L1↔L0 cross-cut — FE-space/mesh-construction front-scoping survey (cycle-064 D1 LEAD, wave-1 GATE)
status: integrated
integrated_at: 2026-06-02T180000Z
integration_commit: 92759ca66e33bee3cc452a82a231dc9d3665062d
integration_notes: |
  cycle-064 D1, applied clean by integrator-per-report (STAGING row 1), finalized by integrator-finalize.
  Observation-only FE-space front-scoping survey (no book change). Partitioned the Palace construction
  surface into in-scope / out-of-scope / MFEM-owned-read-as-given; granularity verdict ONE prime entry
  `fe_space` (NOT a `fe_space`+`fe_collection`+`dof_map` split) — held end-to-end across D2/D3/D4.
  Appended the FE-space sub-spine backlog pick-list OQ (`fe-space-sub-spine-backlog-pick-list`).
  The wave-1 LEAD/GATE that opened the FE-space/mesh-construction L1 front (the user's resolved
  strategic steer). retroactive-budget global = 0.
---

# CYCLE: Cross-layer observation — fe-space-front-survey

## Summary

The FE-space/mesh-construction L1 front is opening with ZERO L1 form and one firm L0 localization
(`book/src/L0/fespace-file.md`). I surveyed the Palace construction surface
(`ConstructFiniteElementSpaceHierarchy` / `ConstructFECollections` / the `FiniteElementSpace` typed
object) via `palace-codemap` to (1) partition in-scope vs out-of-scope vs MFEM-owned-read-as-given,
(2) fan-out-rank the L1 operators this front should yield, (3) deliver the **load-bearing
granularity verdict** for the wave-2 harvester, and (4) inventory the existing firm entries that
currently take the FE-space opaquely and how a firm `fe_space` entry re-anchors them. **All planner
anchors verified and refined** (one correction: the planner cited `spaceoperator.cpp:47-77` for the
4× call — the actual ND/H1/RT hierarchy-construct calls are at `spaceoperator.cpp:47,49,51` with a
4th L2-curl-only construct at `:75`; full constructor body is `:45-89`).

## Observation kind

**Coverage gap** — `FiniteElementSpace` (the L1 domain/range type) and its construction
(`ConstructFiniteElementSpaceHierarchy` / `ConstructFECollections`) have NO L1 entry, while four firm
L1 entries (`fe_assemble`, `weak_form_term`, `eliminate_essential_bc`, `eliminate_rhs`) already
reference the FE-space and its true-dof axis `N` as an **opaque parameter**. This is the shared
substrate under every assembled-operator pipeline; closing the gap is foundation work (per the
foundation-solidity ranking weight) that de-opaques the existing firm cohort.

## Specific finding

### (1) In-scope / out-of-scope / MFEM-owned-read-as-given partition

**Cleanly L1-liftable (the shared substrate under every assembled-operator pipeline):**

- The **`(mesh, FECollection) → FiniteElementSpace` construction itself.** The `FiniteElementSpace`
  variadic ctor (`palace/fem/fespace.hpp:67-75`) forwards `(&mesh.Get(), args...)` straight into
  `mfem::ParFiniteElementSpace` — i.e. the Palace-side construction is exactly the pairing of a mesh
  with an FE collection. This is the typed domain/range object `fe_assemble`/`weak_form_term`/
  `eliminate_*` already name as `space: FiniteElementSpace[N]`.
- The **FE-collection order schedule** `ConstructFECollections` (`palace/fem/multigrid.hpp:22-75`):
  the p-multigrid order sequence (finest→coarsest then reversed, `multigrid.hpp:42-71`), the de-Rham
  family selection (`H1_FECollection`/`ND_FECollection`/`RT_FECollection`/`L2_FECollection` as the
  template parameter), and the basis-type choice (GaussLobatto/GaussLegendre, `multigrid.hpp:34-39`).
  The `pmin` floor (1 for H1/ND, 0 for RT/L2, `multigrid.hpp:30-34`) and LINEAR/LOGARITHMIC
  coarsening (`multigrid.hpp:60-68`) are pure functions of `(p, dim, mg_max_levels, coarsening)`.
- The **de-Rham family variant axis** — H1 (VALUE) / H(curl) (ND) / H(div) (RT) / L2 (INTEGRAL) is
  the FE-collection type axis; the construction is identical across the family modulo the collection
  type. This is the natural L1 variant axis (cf. the existing L0 framing
  `book/src/L0/fespace-file.md:165-169` already names the de-Rham complex H1 →∇ H(curl) →∇× H(div)
  →∇· L2).
- The **essential-true-dof extraction** as a *derived* projection: `GetEssentialTrueDofs(dbc_marker,
  …)` (`multigrid.hpp:99,109,120`) maps a boundary-attribute marker to a true-dof index set. The
  Palace-side input (`dbc_marker = mesh::AttrToMarker(bdr_attr_max, *dbc_attr)`,
  `multigrid.hpp:98`) is liftable as "boundary-attribute → essential-dof-set"; the dof-numbering
  internals are MFEM's (see below). This is the `DofSet[N]` that `eliminate_essential_bc` /
  `eliminate_rhs` already take opaquely.

**Out-of-scope (flag once + skip — per CLAUDE.md §Scope):**

- **MPI / `Par*`** — the wrapped `mfem::ParFiniteElementSpace` (`fespace.hpp:24`), `mfem::ParMesh`
  (`mesh.hpp:48`), and `GetComm` (`fespace.hpp:186`) are read single-rank per the existing
  `par-types-single-rank-reading` rule (`book/src/L0/fespace-file.md:13-16`). Flag once: the L1
  `fe_space` entry reads `FiniteElementSpace` as a serial `(mesh, collection)` pairing.
- **Mesh PARTITIONING** — the `Mesh` wrapper's `loc_attr`/`loc_bdr_attr` per-process
  attribute-remapping (`mesh.hpp:53-60`) is the partitioning bookkeeping; skip.
- **libCEED basis/restriction caches** — the four `CeedObjectMap` caches (`fespace.hpp:30-32`) +
  `ResetCeedObjects` lifecycle are **transparent performance machinery** (already classified at
  `book/src/L0/fespace-file.md:97-104,159-164`): derived data of (space, geometry, Ceed),
  re-derivable on demand. NOT part of the `fe_space` construction algebra; a one-line note at most.

**MFEM-owned, read-as-given (NOT re-anchored at L1):**

- **dof / vdof numbering, byNODES/byVDIM ordering, element-to-dof tables, conformity** — forward to
  `mfem::ParFiniteElementSpace` via thin `return Get().X()` accessors (`fespace.hpp:93-103`); the L0
  chapter already frames these as MFEM's, read as-is (`book/src/L0/fespace-file.md:18-25,154-158`).
  The L1 `fe_space` treats the FE-space as an **opaque index structure with a known true-dof count
  `N = GetTrueVSize()`** and a true-dof ↔ L-vector transfer (`GetProlongationMatrix`).
- **The prolongation/restriction matrices** (`GetProlongationMatrix`/`GetRestrictionMatrix`,
  `fespace.hpp:102-103`) — MFEM-owned, forwarded verbatim; the L-vector↔true-dof transfer.

### (2) Fan-out-ranked L1-pick decomposition

Ranked by what each unblocks downstream (esp. de-opaquing the existing firm cohort):

1. **`fe_space`** — `(mesh, FECollection) → FiniteElementSpace[N]`. **HIGHEST fan-out.** This is the
   typed domain/range object that `fe_assemble`, `weak_form_term`, `eliminate_essential_bc`,
   `eliminate_rhs` ALL take opaquely today (4 firm entries de-opaqued; see inventory §4). It is the
   shared substrate under all 5 solver pipelines (call-site map: `spaceoperator.cpp:47/49/51/75`,
   `curlcurloperator.cpp:36/38`, `laplaceoperator.cpp:36/39`, `boundarymodeoperator.cpp:137/139/141/143`).
2. **`fe_collection`** — the FE-collection order schedule `(p, dim, mg_max_levels, coarsening,
   family) → [FECollection]` (`ConstructFECollections`, `multigrid.hpp:22-75`). Medium fan-out:
   feeds `fe_space` (the collection is the second ctor argument) and the multigrid hierarchy. Whether
   this is a *separate* entry or absorbed into `fe_space` is the granularity question (§3).
3. **`essential_dofs`** — boundary-attribute-marker → essential-true-dof-set
   (`GetEssentialTrueDofs` ∘ `AttrToMarker`, `multigrid.hpp:98-99`). Medium fan-out: this is the
   `DofSet[N]` that `eliminate_essential_bc`/`eliminate_rhs` take opaquely. Strong candidate but
   partly MFEM-owned (the dof-numbering is read-as-given; only the attribute→marker→dof-set *shape*
   lifts).
4. **`fe_space_hierarchy`** — the h/p-refinement multigrid stack
   (`ConstructFiniteElementSpaceHierarchy`, `multigrid.hpp:78-126`: coarse-seed + h-loop + p-loop).
   Lower fan-out for the assembly front (the geometric-multigrid preconditioner consumes it, not the
   assembled-operator pipeline). The `AddLevel`/`GetProlongationAtLevel` transfer machinery
   (`BuildProlongationAtLevel`) is **sibling pull-gated** — name, don't dispatch this cycle.
5. **`fe_collection` order/basis sub-axes** (LINEAR/LOG coarsening, GaussLobatto/Legendre, LOR
   IntegratedGLL) — these are *variant axes ON* `fe_collection`, not separate operators.

`BuildDiscreteInterpolator` (de-Rham interpolator) and `BuildProlongationAtLevel` (multigrid
transfer) are correctly sibling-pull-gated by the planner — named here, NOT dispatched.

### (3) THE LOAD-BEARING GRANULARITY VERDICT

**Recommendation: ONE prime L1 entry `fe_space`, with `fe_collection` as a thin SECOND entry only
if the order-schedule earns its own vocabulary; `dof_map` does NOT become an entry.**

Concretely, the wave-2 harvester should author **`book/src/L1/fe_space.md`** as the prime entry:

```text
fe_space :: (mesh: Mesh, collection: FECollection) -> FiniteElementSpace[N]
```

with `N = GetTrueVSize()`, the de-Rham family (H1/H(curl)/H(div)/L2) as the **collection variant
axis**, and the dof-numbering/ordering/conformity/prolongation-matrix internals noted as
MFEM-owned-read-as-given (NOT cracked open). Rationale, per the vocabulary-shift redirect
(`project_vocabulary_shift_redirect`, combinator-as-entry; avoid thin mirrors AND lumping
genuinely-distinct vocabulary):

- **Do NOT split into `fe_space` + `dof_map` (+ separate ordering/conformity entries).** The
  dof-map/ordering/conformity is MFEM-owned and read-as-given — splitting it into its own L1 entry
  would author a thin mirror of an opaque MFEM structure that L1 explicitly does NOT redefine
  (`book/src/L0/fespace-file.md:18-25,154-158`). That is the "degenerate identity-in-named-terms
  lowering = smell" the redirect warns against. The dof structure is a *property* of the
  `FiniteElementSpace` value (the opaque index axis `N`), not a distinct L1 operation.

- **`fe_collection` is a borderline-second entry.** `ConstructFECollections` produces a *list* of
  collections for the p-multigrid schedule (`multigrid.hpp:42-71`) — that schedule (order sequence,
  coarsening policy, basis type) IS genuinely-distinct vocabulary from the single-space construction,
  AND it has downstream reuse (the hierarchy). **Verdict: author `fe_space` FIRST and primary; treat
  the single-collection-input case as `fe_space`'s domain.** The order-*schedule* (the list-producing
  multigrid machinery) is better deferred to the `fe_space_hierarchy` work (pick #4) than split out
  prematurely — at the assembly-front altitude, a single `FECollection` is just an input to
  `fe_space`. If the wave-2 harvester finds the collection-construction has self-standing laws worth
  their own chapter (the pmin floor, the GaussLobatto/Legendre + LOR basis selection), a thin
  `fe_collection` entry is justified; otherwise fold it as `fe_space`'s collection-input variant axis.

- **Net: ONE entry `fe_space` now; `fe_collection`/`fe_space_hierarchy` as the explicitly-deferred
  follow-on, NOT a same-cycle split.** This keeps L1 concise-in-itself (one combinator for "build the
  typed assembly domain") and avoids minting three thin mirrors of MFEM internals.

### (4) Opaque-parameter inventory (replace-and-propagate forward-look)

Four firm L1 entries currently take the FE-space (or its derived true-dof axis / dof-set) opaquely.
A firm `fe_space` entry re-anchors them by giving the opaque `space`/`N`/`DofSet` parameters a real
L1 home:

| Firm entry | How it takes the space opaquely today | Re-anchor by firm `fe_space` |
|---|---|---|
| `fe_assemble` (`book/src/L1/fe_assemble.md:60,67`) | `space: FiniteElementSpace[N]` is a bare typed input; `N = space.GetTrueVSize()` named but undefined-at-L1 | `space` becomes the output of `fe_space(mesh, collection)`; `N` gets its L1 definition; the `A(space, ·)` opaque-map stays libCEED-owned (separate obstruction theme) |
| `weak_form_term` (`book/src/L1/weak_form_term.md:79,166`) | references `A(space, ·)` over an opaque `space` | `space` cross-refs `fe_space`; the term's domain/range typed |
| `eliminate_essential_bc` (`book/src/L1/eliminate_essential_bc.md:56,63,67`) | `dofs: DofSet[N]` where `N = space.GetTrueVSize()`; the `dbc_tdof_list` recorded by `SetEssentialTrueDofs` is opaque | `DofSet[N]` cross-refs `fe_space`'s `N` and the essential-dof extraction (pick #3) |
| `eliminate_rhs` (`book/src/L1/eliminate_rhs.md`) | `dbc_tdof_list` masking projections over the same opaque dof set | same — `DofSet[N]` re-anchored to `fe_space` |

**Forward-look cross-refs that would later firm up:** once `book/src/L1/fe_space.md` is firm, the
four entries above gain `[`fe_space`](./fe_space.md)` live links for their `space`/`N`/`DofSet`
parameters (currently bare typed names), and a new `book/src/L1-L0/fe-space-construction-rotation.md`
L1>L0 theme (the `(mesh, collection) → FiniteElementSpace` ctor + `GetEssentialTrueDofs` extraction
rewriting into the `ConstructFiniteElementSpaceHierarchy` coarse-seed) becomes authorable. This is
replace-and-propagate, not mine-and-strand.

## Recommendation

- **Dispatch wave-2 harvester on `book/src/L1/fe_space.md`** as the prime entry, signature
  `fe_space :: (mesh: Mesh, collection: FECollection) -> FiniteElementSpace[N]`, de-Rham family as
  the collection variant axis, dof-numbering/ordering/conformity/prolongation-matrices noted
  MFEM-owned-read-as-given (NOT cracked open). **ONE entry, not a `fe_space`+`fe_collection`+`dof_map`
  split** (granularity verdict §3).
- **Defer** `fe_collection` (order-schedule) and `fe_space_hierarchy` (multigrid stack) to a
  follow-on dispatch; sibling-pull-gate `BuildDiscreteInterpolator` / `BuildProlongationAtLevel`
  (name, don't author).
- **Forward-look** (post-`fe_space`-firm): re-anchor the four opaque-parameter entries (§4) with live
  cross-refs and author the `fe-space-construction-rotation` L1>L0 theme — a later replace-and-propagate
  dispatch, NOT this cycle.

## Proposed-changes block

None. This is an observation-only survey (DISPATCH-phase read-only audit). No `book/` mutation
proposed; the recommendation is a wave-2 dispatch scope, not an edit.

## Supporting evidence

- `palace/fem/multigrid.hpp:22-75` — `ConstructFECollections` (p-multigrid order schedule; pmin floor
  `:30-34`, basis-type `:34-39`, finest→coarsest+reverse `:42-71`, LINEAR/LOG coarsening `:60-68`).
- `palace/fem/multigrid.hpp:78-126` — `ConstructFiniteElementSpaceHierarchy` (coarse-seed `:90-92`,
  `dbc_marker = AttrToMarker` `:98`, `GetEssentialTrueDofs` `:99/109/120`, h-loop `:104-114`, p-loop
  `:116-124`).
- `palace/fem/fespace.hpp:21-194` — `FiniteElementSpace` typed object; variadic ctor forwarding into
  `mfem::ParFiniteElementSpace` `:67-75`; wrapped `ParFiniteElementSpace fespace` + `Mesh &mesh`
  `:24,27`; MFEM-forwarding dof accessors `:93-103`; `GetTrueVSize` `:96`; prolongation/restriction
  matrices `:102-103`; libCEED caches `:30-32`; `GetComm` `:186`.
- `palace/fem/mesh.hpp:43-60` — `Mesh` wrapper (`mfem::ParMesh`-owning `:48`; partitioning
  attribute-remap `loc_attr`/`loc_bdr_attr` `:53-60`, OUT of scope).
- `palace/models/spaceoperator.cpp:45-89` — the constructor calling
  `ConstructFiniteElementSpaceHierarchy<ND/H1/RT>` at `:47/49/51` + L2-curl `:75` (planner's
  `:47-77` refined).
- Call-site map (`get_call_sites ConstructFiniteElementSpaceHierarchy`): 4 solver model operators —
  `spaceoperator.cpp:47/49/51/75`, `curlcurloperator.cpp:36/38`, `laplaceoperator.cpp:36/39`,
  `boundarymodeoperator.cpp:137/139/141/143`.
- `book/src/L0/fespace-file.md` — existing firm L0 localization (FE-space wrapper + hierarchy;
  MFEM-as-given framing `:18-25,154-158`; de-Rham family `:165-169`; transparent-cache classification
  `:97-104,159-164`).
- `book/src/L1/fe_assemble.md:60,67-79` — `space: FiniteElementSpace[N]` opaque input; `A(space, ·)`
  opaque per-term map.
- `book/src/L1/weak_form_term.md:79,166` — `A(space, ·)` over opaque `space`.
- `book/src/L1/eliminate_essential_bc.md:56,63,67` — `dofs: DofSet[N]`, `N = space.GetTrueVSize()`.
- `book/src/L1/eliminate_rhs.md:67,78,246-250` — `dbc_tdof_list` masking projections over the opaque
  dof set.

## Open questions / caveats

- **`essential_dofs` (pick #3) straddles the MFEM-owned boundary.** The attribute→marker→dof-set
  *shape* lifts (`AttrToMarker` is Palace-side, `multigrid.hpp:97`), but `GetEssentialTrueDofs`
  itself is MFEM-owned dof-numbering (read-as-given). The wave-2 harvester should decide whether this
  is a thin L1 entry or a noted-property of `fe_space`; my lean is noted-property unless
  `eliminate_*`'s `DofSet[N]` demands a self-standing home. (Logged to OQ ledger.)
- **`fe_collection` self-standing-laws check is deferred to the harvester.** Whether the
  pmin-floor + basis-selection laws (`multigrid.hpp:30-39`) earn a separate chapter vs. fold as
  `fe_space`'s collection variant axis is a judgment the harvester makes once authoring; I recommend
  fold-first, split-only-if-laws-justify.
- The 2-D L2-curl special case (`spaceoperator.cpp:73-79`; `INTEGRAL` map type for `B = curl E`) is a
  load-bearing variant of the collection family — flag for the harvester but it does not change the
  granularity verdict.
