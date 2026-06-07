---
# Lowering theme. Per graded-stack scheme §5: rank = min(endpoint ranks). The L1
# endpoint (fe_space_hierarchy) is firm (rank 3, c117); the L0 endpoint is rank-terminal
# ground truth. So the theme is firm and rank(theme) <= min(endpoints) holds for free.
rank: firm
edges:
  depends-on:
    - target: L1/fe_space_hierarchy
      kind: lowers-to             # the L1 source construction this theme lowers
    - target: palace/fem/multigrid.hpp:78-126
      kind: cites-evidence        # ConstructFiniteElementSpaceHierarchy whole body (close brace } at :126, verified on-disk)
    - target: palace/fem/fespace.hpp:200-286
      kind: cites-evidence        # FiniteElementSpaceHierarchy class: seed ctor :210-213, AddLevel = push_back + nullptr slot :217-221
  reference:
    - L1-L0/fe-space-construction-rotation         # the per-level fe_space construction this fold iterates (base case + AddLevel body)
    - L1-L0/fe-collection-construction-rotation     # the upstream [FECollection] schedule the p-loop folds over
    - L1-L0/essential-dofs-construction-rotation    # the per-level dbc block this fold interleaves (single-space rewrite this iterates)
---

# fe-space-hierarchy-construction-rotation

**Slug:** `fe-space-hierarchy-construction-rotation`

How the pure L1 [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) **`AddLevel`-fold** lowers into the
concrete imperative Palace function `ConstructFiniteElementSpaceHierarchy`
(`palace/fem/multigrid.hpp:78-126`). This is a **vocabulary translation, not a rename**: the L1 form is a
single declarative left-fold — `foldl AddLevel seed refinements`, where `seed` is one
[`fe_space`](../L1/fe_space.md) construction and each fold step appends one finer level — while the L0 form
is an *imperative level-vector builder* that (1) computes a `coarse_mesh_l` start index, (2) constructs a
seed `FiniteElementSpace`, (3) runs **two separate `for` loops** that `AddLevel`-`push_back` one
`FiniteElementSpace` per refinement step over **two independent refinement axes** (h: finer meshes at
fixed coarsest collection; p: finer collections at fixed finest mesh), and (4) interleaves an optional
per-level Dirichlet-boundary block. The one declarative fold reorganizes into index arithmetic + a seed +
two axis-specialized loops — that reorganization (not a term-by-term name match) is the content of this
theme.

## Status

`firm` — structural (firm-on-positive-structure). The construction is read in full from one positive
source site: the entire `ConstructFiniteElementSpaceHierarchy` body
(`palace/fem/multigrid.hpp:78-126`; close brace `}` verified on-disk at `:126`, `return fespaces;` at
`:125`). The L1 endpoint [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md) is firm (c117) and its two
composed constituents [`fe_space`](../L1/fe_space.md) (c064) / [`fe_collection`](../L1/fe_collection.md)
(c065) are firm on disk, so the well-foundedness invariant `rank(theme) ≤ min(endpoints)` holds at
firm/firm. Every step of the rewrite is a syntactic identity / fold-invariant on the positive structure
(start-index arithmetic, seed-as-base-case, `AddLevel = push_back` append, two-axis loop decomposition,
per-level dbc interleave) — there is no convergence/iteration semantics to test-gate, so the absence of a
dedicated `test-multigrid.cpp` exercising `ConstructFiniteElementSpaceHierarchy` does **not** gate firm
(the `fe_space` c064 / `fe_collection` c065 / `fe_assemble` c054 / `essential_dofs` c066 no-dedicated-test
precedent). The per-level dof-resolution tail (`GetEssentialTrueDofs`, `multigrid.hpp:99`/`:109`/`:120`)
is **MFEM-owned-read-as-given** and is the subject of the sibling theme
[`essential-dofs-construction-rotation`](./essential-dofs-construction-rotation.md) — this fold only
*sequences* that single-space construction per level; it does not crack open the dof numbering (doing so
would be the identity-in-named-terms smell the 2026-06-01 vocabulary-shift redirect warns against). The
lazy prolongation `P[l]` / discrete-interpolator machinery is read-as-given (a property of the result
record, sibling-pull-gated), NOT a constructed sub-part — so `firm`, not `partly-constructive`. MPI /
`Par*` and mesh partitioning are flagged once and read single-rank (out of scope per CLAUDE.md §Scope).

## L1 form (LHS)

The pure construction value (D2's prime entry [`L1/fe_space_hierarchy`](../L1/fe_space_hierarchy.md)):

    fe_space_hierarchy :: [Mesh] -> [FECollection] -> Config -> FiniteElementSpaceHierarchy

At L1 this is a referentially-transparent **left-fold of `AddLevel`** over the refinement sequence:

- **base case** — the coarse seed is one [`fe_space`](../L1/fe_space.md) construction:
  `fespaces[0] = fe_space(mesh[coarse_mesh_l], fecs[0])` (`fe_space_hierarchy` law 1).
- **general case** — each fold step appends a strictly-finer level:
  the h-refinement steps append `fe_space(mesh[l], fecs[0])` for the finer meshes, and the p-refinement
  steps append `fe_space(mesh.back(), fecs[l])` for the finer collections (`fe_space_hierarchy` law 2,
  AddLevel-fold structure; law 3, coarse-to-fine level-monotonicity).

The result is the immutable `FiniteElementSpaceHierarchy` level sequence. `AddLevel` at L1 is the
order-preserving, strictly-appending fold combinator; the fold consumes the `[FECollection]` schedule
that [`fe_collection`](../L1/fe_collection.md) produces and the `[Mesh]` coarse-to-fine sequence.
`Config` carries `mg_max_levels` (fixing the fold's start index) plus the optional Dirichlet attributes.

## L0 form (RHS)

The concrete imperative builder — `ConstructFiniteElementSpaceHierarchy`
(`palace/fem/multigrid.hpp:78-126`):

    // palace/fem/multigrid.hpp:78-126 (ConstructFiniteElementSpaceHierarchy, abbreviated)
    inline FiniteElementSpaceHierarchy ConstructFiniteElementSpaceHierarchy(
        int mg_max_levels, const std::vector<std::unique_ptr<Mesh>> &mesh,
        const std::vector<std::unique_ptr<FECollection>> &fecs,
        const mfem::Array<int> *dbc_attr, std::vector<mfem::Array<int>> *dbc_tdof_lists)
    {
      MFEM_VERIFY(!mesh.empty() && !fecs.empty() && ...);              // :84-86
      int coarse_mesh_l = std::max(0, (int)(mesh.size() + fecs.size()) // :87-88
                                          - 1 - std::max(1, mg_max_levels));
      FiniteElementSpaceHierarchy fespaces(                            // :89-90  SEED
          std::make_unique<FiniteElementSpace>(*mesh[coarse_mesh_l], fecs[0].get()));

      mfem::Array<int> dbc_marker;                                     // :92-101 optional dbc block
      if (dbc_attr && dbc_tdof_lists) { /* AttrToMarker; GetEssentialTrueDofs into emplace_back() */ }

      for (std::size_t l = coarse_mesh_l + 1; l < mesh.size(); l++)    // :104-112 h-refinement loop
      {
        fespaces.AddLevel(std::make_unique<FiniteElementSpace>(*mesh[l], fecs[0].get()));  // :106
        if (dbc_attr && dbc_tdof_lists) { /* per-level GetEssentialTrueDofs */ }
      }

      for (std::size_t l = 1; l < fecs.size(); l++)                    // :115-123 p-refinement loop
      {
        fespaces.AddLevel(std::make_unique<FiniteElementSpace>(*mesh.back(), fecs[l].get()));  // :117
        if (dbc_attr && dbc_tdof_lists) { /* per-level GetEssentialTrueDofs */ }
      }

      return fespaces;                                                 // :125
    }

The L1 fold maps onto this body as:

- `seed` ⟶ the `FiniteElementSpaceHierarchy fespaces(make_unique<FiniteElementSpace>(...))` constructor
  call (`multigrid.hpp:89-90`); the seed ctor itself is `AddLevel(std::move(fespace))`
  (`fespace.hpp:210-213`), so even the base case is one append.
- `AddLevel` ⟶ `FiniteElementSpaceHierarchy::AddLevel` = `fespaces.push_back(...)` + `P.push_back(nullptr)`
  (`fespace.hpp:217-221`) — strictly-appending, order-preserving, plus the lazy `nullptr` prolongation
  slot. The L1 fold's order is the loop's `++l` order.
- the refinement sequence ⟶ split across **two** imperative loops by axis (see the next section).
- the produced level sequence ⟶ the returned `fespaces` value (`multigrid.hpp:125`).

### The fold-into-two-axis-loops reorganization (the translation core)

A single declarative `foldl AddLevel seed refinements` reorganizes into **start-index arithmetic + a seed
+ two sequential axis-specialized loops** — this is where the vocabulary genuinely shifts (and why this is
not a rename):

1. **`coarse_mesh_l` start index** (`multigrid.hpp:87-88`).
   `coarse_mesh_l = max(0, mesh.size() + fecs.size() − 1 − max(1, mg_max_levels))`. At L1 this is the
   fold's *start offset* — `mg_max_levels` (a `Config` field) caps how many of the input meshes become
   levels, so the fold begins at `mesh[coarse_mesh_l]` rather than `mesh[0]`. The imperative loop encodes
   this as the h-loop's lower bound `l = coarse_mesh_l + 1`. There is no L1 "skip-meshes" operation; the
   declarative fold simply ranges over the selected sub-sequence.

2. **Seed = base case** (`multigrid.hpp:89-90`). The fold's base `fespaces[0] = fe_space(mesh[coarse_mesh_l],
   fecs[0])` is the one-argument `FiniteElementSpaceHierarchy` ctor that immediately `AddLevel`s the seed
   space (`fespace.hpp:210-213`). The L1 base-case-as-one-`fe_space`-call (law 1) IS this seed ctor.

3. **Two independent refinement axes ⟶ two loops** — the single fold over `refinements` splits into:
   - **h-refinement** (`multigrid.hpp:104-112`): `for (l = coarse_mesh_l+1; l < mesh.size(); l++)`,
     appending `fe_space(mesh[l], fecs[0])` — finer **meshes** at the **fixed coarsest collection**
     `fecs[0]` (`AddLevel` at `:106`).
   - **p-refinement** (`multigrid.hpp:115-123`): `for (l = 1; l < fecs.size(); l++)`, appending
     `fe_space(mesh.back(), fecs[l])` — finer **collections** at the **fixed finest mesh** `mesh.back()`
     (`AddLevel` at `:117`).
   The two axes are **independent and sequential** (geometric h-refinement first, then order p-refinement);
   the L1 fold treats `refinements` as the concatenation `h-steps ++ p-steps`, and the imperative form
   realizes that concatenation as two back-to-back loops. The *axis selection* (which of `mesh`/`fecs` is
   held fixed, which is indexed) is the load-bearing structural content of each loop body — it is what the
   fold's per-step `fe_space(·, ·)` argument-pairing encodes.

4. **Per-level Dirichlet interleave** (`multigrid.hpp:92-101`, `:107-111`, `:118-122`). When
   `dbc_attr && dbc_tdof_lists`, the same boundary marker (built once at the seed, `:92-101`) is
   re-applied via `GetEssentialTrueDofs` to the finest level **after the seed** (`:99-100`) and **after
   each `AddLevel`** (`:109-110` h-loop, `:120-121` p-loop), each call `emplace_back`ing one
   `DofSet[N]` into `dbc_tdof_lists`. At L1 this is the per-level fan-out of one
   [`essential_dofs`](../L1/essential_dofs.md) construction over the shared marker — the fold carries an
   accumulating per-level dof-set output alongside the level stack (`fe_space_hierarchy` law 5). The
   single-space rewrite (attribute → marker → `GetEssentialTrueDofs`) is the sibling theme
   [`essential-dofs-construction-rotation`](./essential-dofs-construction-rotation.md); **this** theme
   contributes only the *per-level sequencing* of that construction — i.e. the hierarchy fan-out that
   theme explicitly deferred to the `fe_space_hierarchy` consumer.

### What lowers HERE vs. what is delegated / read-as-given

The translation has a sharp boundary, matching the sibling construction-rotation themes:

- **LOWERS HERE (the fold structure, Palace-authored).** The start-index arithmetic
  (`multigrid.hpp:87-88`), the seed-as-base-case (`:89-90` + the seed ctor `fespace.hpp:210-213`), the
  `AddLevel = push_back + nullptr slot` append (`fespace.hpp:217-221`), and the two-axis loop
  decomposition (`:104-112` / `:115-123`) are all Palace-owned and rewrite directly. This is the
  hierarchy-combinator content of the theme.
- **DELEGATED to siblings (not re-narrated here).** The per-level `fe_space(·, ·)` construction at each
  `AddLevel` is the [`fe-space-construction-rotation`](./fe-space-construction-rotation.md) rewrite
  (c064); the `[FECollection]` schedule the p-loop ranges over is produced by
  [`fe-collection-construction-rotation`](./fe-collection-construction-rotation.md) (c065); the per-level
  dbc single-space block is [`essential-dofs-construction-rotation`](./essential-dofs-construction-rotation.md)
  (c066). This theme **composes** those three — it is the fold whose body is a `fe_space` call and whose
  optional side-effect is an `essential_dofs` call, ranging over a `fe_collection` schedule.
- **MFEM-OWNED-READ-AS-GIVEN (does NOT lower here).** The `GetEssentialTrueDofs` dof-resolution tail
  (`multigrid.hpp:99`/`:109`/`:120`) is MFEM-owned (documented in the `essential-dofs` sibling); the lazy
  prolongation `P[l]` (`BuildProlongationAtLevel`, `fespace.hpp:206,249-255`) and discrete interpolators
  (`fespace.hpp:269-285`) are read-as-given properties of the result record (sibling-pull-gated), NOT
  constructed by this fold.

## Variant axis — refinement-axis (2 loop cases) × Dirichlet-presence (optional block)

The construction is identical modulo (a) which refinement axis a loop body indexes and (b) whether the
optional dbc block runs:

| fold-step case | held fixed | indexed | L0 `AddLevel` body | anchor |
|---|---|---|---|---|
| seed (base case) | — | `mesh[coarse_mesh_l]`, `fecs[0]` | seed ctor (`AddLevel(seed)`) | `multigrid.hpp:89-90` |
| h-refinement step | `fecs[0]` (coarsest collection) | `mesh[l]` (finer meshes) | `AddLevel(fe_space(mesh[l], fecs[0]))` | `multigrid.hpp:104-112` (`AddLevel` `:106`) |
| p-refinement step | `mesh.back()` (finest mesh) | `fecs[l]` (finer collections) | `AddLevel(fe_space(mesh.back(), fecs[l]))` | `multigrid.hpp:115-123` (`AddLevel` `:117`) |

Orthogonally, the **Dirichlet-presence** axis (whether `dbc_attr && dbc_tdof_lists`) toggles the per-level
`GetEssentialTrueDofs` `emplace_back` after the seed and each `AddLevel`. When absent, the fold produces
only the level stack; when present, it additionally accumulates one `DofSet[N]` per level (the
`essential_dofs` per-level fan-out, `multigrid.hpp:99-100`/`:109-110`/`:120-121`).

## Applicability conditions

- The rewrite applies to the whole-hierarchy construction
  `fe_space_hierarchy(mesh, fecs, config) → FiniteElementSpaceHierarchy`. The single positive anchor is
  `ConstructFiniteElementSpaceHierarchy` (`multigrid.hpp:78-126`); there is no second site (this is the
  sole hierarchy builder).
- `mesh` is a non-empty coarse-to-fine `[Mesh]`; `fecs` is a non-empty coarse-to-fine `[FECollection]`
  (the `MFEM_VERIFY`, `multigrid.hpp:84-86`). `mesh.back()` is the finest mesh; `fecs[0]` is the coarsest
  collection. The level count is bounded by `mg_max_levels` through `coarse_mesh_l`.
- **Per-level dof fan-out is in-scope for THIS theme** (it is the hierarchy property the
  `essential-dofs-construction-rotation` sibling explicitly deferred to `fe_space_hierarchy`). The
  single-space dbc rewrite itself is delegated to that sibling; this theme only sequences it per level.
- Single-rank reading: each level is wrapped into an `mfem::ParFiniteElementSpace`
  (`par-types-single-rank-reading` rule); mesh partitioning is out of scope (CLAUDE.md §Scope; flagged
  once).

## Justification kind

**Structural** — the rewrite is shape-driven: the L1 `foldl AddLevel seed refinements` maps onto the
concrete seed-ctor + two `push_back`-loops, with the refinement-axis as the positively-anchored case axis
and the Dirichlet-presence as the optional orthogonal axis. No reduction chain or algebraic re-derivation
is needed; the fold-step body (`AddLevel(fe_space(·, ·))`) and the append semantics (`push_back` +
`nullptr` slot, `fespace.hpp:217-221`) are read directly from the positive source. The delegated
sub-constructions (`fe_space` / `fe_collection` / `essential_dofs`) carry their own firm structural
rewrites; this theme is their composition.

## Verified-against

- `palace/fem/multigrid.hpp:78-126` — `ConstructFiniteElementSpaceHierarchy`: the signature (`:78-82`),
  the non-empty `MFEM_VERIFY` (`:84-86`), the `coarse_mesh_l` start index (`:87-88`), the coarse-seed
  `FiniteElementSpaceHierarchy fespaces(make_unique<FiniteElementSpace>(...))` (`:89-90`), the optional
  dbc block (`:92-101`), the h-refinement loop with `AddLevel(... *mesh[l], fecs[0].get())` (`:104-112`,
  `AddLevel` at `:106`), the p-refinement loop with `AddLevel(... *mesh.back(), fecs[l].get())`
  (`:115-123`, `AddLevel` at `:117`), and the `return fespaces` (`:125`). Close brace `}` at `:126`.
  (Verified on-disk via Read + `citecheck --anchor`; close-brace END confirmed by direct on-disk Read of
  `:124-126`.)
- `palace/fem/fespace.hpp:200-286` — the `FiniteElementSpaceHierarchy` class: the level vector `fespaces`
  (`:203`), the mutable lazy prolongation vector `P` (`:204`) + `BuildProlongationAtLevel` (`:206`), the
  one-argument seed ctor that `AddLevel`s the seed (`:210-213`), `AddLevel = push_back + nullptr slot`
  (`:217-221`), `GetNumLevels` (`:215`), `GetFinestFESpace` (`:236-247`). (Verified on-disk;
  `citecheck --anchor AddLevel` ✓ at `:217`, `--anchor FiniteElementSpaceHierarchy` ✓.)
- [`L1/fe_space_hierarchy`](../L1/fe_space_hierarchy.md) (firm c117) — the prime L1 entry this theme
  lowers; its laws 1 (coarse-seed base case), 2 (AddLevel-fold structure), 3 (level-monotonicity), 4
  (determinism), 5 (per-level essential-dof coherence) are the LHS this RHS realizes.
- Sibling delegated rewrites: [`fe-space-construction-rotation`](./fe-space-construction-rotation.md)
  (c064; per-level `fe_space` construction), [`fe-collection-construction-rotation`](./fe-collection-construction-rotation.md)
  (c065; the `[FECollection]` schedule), [`essential-dofs-construction-rotation`](./essential-dofs-construction-rotation.md)
  (c066; the single-space dbc block whose per-level fan-out this fold sequences).

## Open questions / caveats

- **Lifting note (reverse direction, working-note only).** The L0 imperative builder lifts to the L1
  `AddLevel`-fold cleanly precisely because each loop body is one `fe_space` construction and the append is
  order-preserving (`push_back` + a lazy `nullptr` slot, no mutation of prior levels). The lift retains
  the fold structure + the two-axis refinement schedule + the per-level dof fan-out, discarding the index
  arithmetic (absorbed into the fold's start offset) and the lazy prolongation slot (read-as-given). The
  structure the lift would need to be *complete* (rather than treating prolongation as opaque) is the
  multigrid-transfer `BuildProlongationAtLevel` algebra, which is sibling-pull-gated. (High→low formal
  content stays in the chapter above; this is a working note.)
- **Forward-reference resolution.** The live links to the three delegated sibling themes
  (`fe-space-construction-rotation` / `fe-collection-construction-rotation` /
  `essential-dofs-construction-rotation`) all already exist on disk (c064/c065/c066), and the
  `L1/fe_space_hierarchy` link resolves to the c117-landed chapter; no same-cycle forward-ref hazard.
- **RE9 note (NOT this theme's concern).** Per the dispatch scope, the OP `fe_space_hierarchy` stays RE9
  baseline-excepted — it has no faithful inbound consumer yet. This theme grounds the *home* (the theme
  file), not the op's reachability; no inbound consumer edge is forced.
