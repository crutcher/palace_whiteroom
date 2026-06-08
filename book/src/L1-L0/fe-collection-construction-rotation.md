# fe-collection-construction-rotation

**Slug:** `fe-collection-construction-rotation`

How the pure L1 [`fe_collection`](../L1/fe_collection.md) p-multigrid order schedule lowers into the
concrete Palace `ConstructFECollections` function-template body. This is a **vocabulary translation,
not a rename**: the L1 form is a pure declarative *schedule value* — a `(p, dim, mg_max_levels,
coarsening, family)` tuple naming a finest-to-coarsest list `[FECollection]`; the L0 form is an
imperative loop that `push_back`es one collection per level into a `std::vector`, steps the order via a
`switch`, breaks at a family floor, and then **reverses the accumulated vector** to coarsest-first. The
declarative-enumeration-vs-imperative-build-then-reverse gap is the translation; it is narrated forward
(L1 → L0) in the split below.

The internal basis/dof structure of the produced `FECollection`s is
**MFEM-owned-read-as-given** (the `H1_/ND_/RT_/L2_FECollection` classes are MFEM's; this theme lowers
only the *order schedule + subclass + basis-type selection*) — a witnessed library-ownership boundary,
not a constructive reconstruction (cf. the firm
[`fe-space-construction-rotation`](./fe-space-construction-rotation.md) construction-lowers /
dof-bookkeeping-MFEM-owned split). MPI/`Par*` and mesh partitioning are out of scope (flagged once):
`ConstructFECollections` is rank-agnostic — it builds `FECollection` template objects, not partitioned
spaces; the per-rank distribution enters only downstream at the
`ConstructFiniteElementSpaceHierarchy` `mfem::ParFiniteElementSpace` wrapping (read single-rank).

## L1 form (LHS)

The pure schedule value ([`L1/fe_collection`](../L1/fe_collection.md)):

    fe_collection :: (p: Order, dim: Dim, mg_max_levels: Nat, coarsening: CoarseningPolicy, family: DeRhamFamily) -> [FECollection]

`[FECollection]` is the **coarsest-to-finest list** of finite-element collections seeding a geometric
p-multigrid hierarchy. At L1 this is a referentially-transparent enumeration: given fixed
`(p, dim, mg_max_levels, coarsening, family)`, `fe_collection` names the same list (same length, same
per-entry orders). The list is a value sequence — `result[last]` carries the finest order `p`,
`result[0]` the coarsest visited order — and the order schedule, the family floor `pmin`, and the
`mg_max_levels` length bound are all properties *of the value*, not separate operations. The three
variant axes (de-Rham family, coarsening policy, LOR basis) are carried by the operator's arguments;
they are the rewrite cases below.

## L0 form (RHS)

The concrete C++ function-template body. The Palace-side template is the single rewrite target; it
builds the list imperatively then reverses it:

    // palace/fem/multigrid.hpp:23-26 (signature)
    template <typename FECollection>
    inline std::vector<std::unique_ptr<FECollection>>
    ConstructFECollections(int p, int dim, int mg_max_levels, MultigridCoarsening mg_coarsening,
                           bool mat_lor)

The forward rewrite (L1 schedule → L0 body) decomposes into five pieces, narrated in build order:

1. **Family floor `pmin` (`multigrid.hpp:30-33`) + precondition (`:34`).** The L1 `family` argument's
   floor materializes as a compile-time `constexpr int pmin` keyed on the template parameter:

       constexpr int pmin = (std::is_base_of<mfem::H1_FECollection, FECollection>::value ||
                             std::is_base_of<mfem::ND_FECollection, FECollection>::value)
                                ? 1
                                : 0;
       MFEM_VERIFY(p >= pmin, "FE space order must not be less than " << pmin << "!");

   `pmin = 1` for H1/ND, `0` for RT/L2. The L1 precondition `p >= pmin` is the `MFEM_VERIFY` (`:34`)
   — supplying `p < pmin` is a contract violation, not a schedule branch.

2. **Basis-type selection (`multigrid.hpp:35-39`) — the LOR variant axis.** The L1 `family` + LOR flag
   selects `(b1, b2)`:

       int b1 = mfem::BasisType::GaussLobatto, b2 = mfem::BasisType::GaussLegendre;
       if (mat_lor)
       {
         b2 = mfem::BasisType::IntegratedGLL;
       }

   `b1 = GaussLobatto` always; `b2 = GaussLegendre` normally, `IntegratedGLL` under the LOR
   (`mat_lor`) flag. For 3-arg (H1/L2) families `b2` is unused (`MFEM_CONTRACT_VAR(b2)`, `:54`).

3. **The bounded build loop (`multigrid.hpp:44-69`) + the arity-3/4 ctor branch (`:46-55`).** The L1
   declarative "one collection per level" enumeration lowers to an imperative `for` capped at
   `max(1, mg_max_levels)` levels that `push_back`es one `make_unique<FECollection>` per iteration,
   branching on the de-Rham family for the constructor arity:

       std::vector<std::unique_ptr<FECollection>> fecs;
       for (int l = 0; l < std::max(1, mg_max_levels); l++)
       {
         if constexpr (std::is_base_of<mfem::ND_FECollection, FECollection>::value ||
                       std::is_base_of<mfem::RT_FECollection, FECollection>::value)
         {
           fecs.push_back(std::make_unique<FECollection>(p, dim, b1, b2));   // 4-arg (ND/RT)
         }
         else
         {
           fecs.push_back(std::make_unique<FECollection>(p, dim, b1));       // 3-arg (H1/L2)
           MFEM_CONTRACT_VAR(b2);
         }
         if (p == pmin) { break; }                                          // floor break (:56-59)
         switch (mg_coarsening) { ... }                                      // order step (:60-68)
       }

   The `max(1, mg_max_levels)` cap (`:44`) is the L1 length bound (always `>= 1` — at least the finest
   collection even when `mg_max_levels <= 0`). The `if constexpr` family branch (`:46-47`) is the
   de-Rham variant axis's L0 site.

4. **The coarsening `switch` (`multigrid.hpp:60-68`) — the coarsening-policy variant axis.** The L1
   `coarsening` argument lowers to the order-step `switch`:

       switch (mg_coarsening)
       {
         case MultigridCoarsening::LINEAR:
           p--;                                                              // arithmetic descent
           break;
         case MultigridCoarsening::LOGARITHMIC:
           p = (p + pmin) / 2;                                               // gap-halving (int div)
           break;
       }

   `LINEAR` ⟹ `p, p-1, ..., pmin`; `LOGARITHMIC` ⟹ `p, ⌊(p+pmin)/2⌋, ...` (the Palace default,
   `palace/utils/configfile.hpp:918`). The policy changes ONLY the interior order sequence (hence list
   length), not the per-entry construction.

5. **The terminal `std::reverse` (`multigrid.hpp:70`) + return (`:72`).** The loop builds
   finest-to-coarsest (comment `:41-42`); the L1 *coarsest-first* result orientation is the explicit
   reverse:

       std::reverse(fecs.begin(), fecs.end());
       return fecs;

   This is the load-bearing reorganization: the L1 schedule names a coarsest-to-finest list directly,
   while L0 builds finest-first and reverses at the end. The reverse is the single line that reconciles
   the declarative orientation with the imperative accumulation order.

### Variant axis A — de-Rham family (4 collection-type rewrite cases)

The L1 `family` argument is the L0 template parameter `FECollection`. It couples three things — the
`pmin` floor (piece 1), the constructor arity (piece 3 branch), and the produced subclass:

| L1 `family` (de-Rham space) | L0 `FECollection` subclass | `pmin` | ctor arity | site |
|---|---|---|---|---|
| H1 (nodal scalar) | `mfem::H1_FECollection` | 1 | 3-arg `(p, dim, b1)` | `multigrid.hpp:30-34,51-54` |
| H(curl) (Nedelec) | `mfem::ND_FECollection` | 1 | 4-arg `(p, dim, b1, b2)` | `multigrid.hpp:30-34,46-49` |
| H(div) (Raviart-Thomas) | `mfem::RT_FECollection` | 0 | 4-arg `(p, dim, b1, b2)` | `multigrid.hpp:30-34,46-49` |
| L2 (discontinuous) | `mfem::L2_FECollection` | 0 | 3-arg `(p, dim, b1)` | `multigrid.hpp:30-34,51-54` |

The `pmin` coupling is the `std::is_base_of<H1...> || is_base_of<ND...> ? 1 : 0` `constexpr`
(`:30-33`); the arity coupling is the `if constexpr (is_base_of<ND...> || is_base_of<RT...>)` branch
(`:46-47`). The family is selected upstream at the `ConstructFiniteElementSpaceHierarchy<FECollection>`
call sites (`palace/models/spaceoperator.cpp:47/49/51`, the ND/H1/RT instantiations), the same de-Rham
selection point as the sibling [`fe-space-construction-rotation`](./fe-space-construction-rotation.md).

### Variant axis B — coarsening policy (2 order-step rewrite cases)

The L1 `coarsening` argument is the L0 `MultigridCoarsening` enum
(`palace/utils/labels.hpp:114-119`), switched at `multigrid.hpp:60-68` (piece 4): `LINEAR` ⟹ `p--`
(`:62-64`), `LOGARITHMIC` ⟹ `p = (p+pmin)/2` integer division (`:65-67`, the default
`palace/utils/configfile.hpp:918`). Changes the order sequence (hence list length) only.

### Variant axis C — LOR basis selection (2 basis-type rewrite cases, inert for H1/L2)

The L1 LOR flag is the L0 `mat_lor` bool selecting `b2` (piece 2, `multigrid.hpp:35-39`):
`b2 = GaussLegendre` normally, `IntegratedGLL` when `mat_lor`. Live only for the 4-arg ND/RT families
(`:49`); for the 3-arg H1/L2 families `b2` is `MFEM_CONTRACT_VAR`-marked unused (`:54`), so the axis is
inert. A basis-type refinement of the produced collections, not a schedule-length change.

## Applicability conditions

- The rewrite applies to the whole-schedule construction `fe_collection(p, dim, mg_max_levels,
  coarsening, family)` — the entire `ConstructFECollections<FECollection>` template body
  (`multigrid.hpp:22-73`). It is a one-shot enumeration: Palace builds the `std::vector` once before
  the multigrid solve and thereafter consumes it read-only (the immutability the L1 value asserts).
- `family` must be one of the four de-Rham `FECollection` subclasses (variant axis A); `coarsening`
  one of `LINEAR`/`LOGARITHMIC` (variant axis B). `p >= pmin` is a precondition (`MFEM_VERIFY`, `:34`),
  not a branch — `p < pmin` is a contract violation.
- The produced `[FECollection]` is the per-level `collection` input to the sibling
  [`fe-space-construction-rotation`](./fe-space-construction-rotation.md): each entry rewrites to one
  `FiniteElementSpace(mesh_l, fecs[l].get())` construction inside
  `ConstructFiniteElementSpaceHierarchy` (`multigrid.hpp:90` coarse-seed, `:117` per-level
  `AddLevel`). This theme is the *upstream producer* rewrite; the FE-space theme is the *consumer*
  rewrite across the `[FECollection]` boundary.
- Single-rank reading: `ConstructFECollections` is rank-agnostic (it builds template `FECollection`
  objects, not partitioned spaces). Mesh PARTITIONING / `Par*` distribution is out of scope — flagged
  once (per CLAUDE.md §Scope).

## Justification kind

**Structural** — the rewrite is shape-driven: the L1 declarative schedule value maps onto the concrete
imperative build-then-reverse loop, with the three variant axes (de-Rham family, coarsening policy, LOR
basis) as the positively-anchored case axes. No algebraic law or reduction chain is needed; every
rewrite piece is a syntactic identity / loop-invariant on the read-in-full positive body
(`multigrid.hpp:22-73`). The MFEM-owned-read-as-given boundary (the produced collections' internal
basis/dof structure) is a witnessed library-ownership boundary, not a reconstruction.

## Relationship to the FE-space hierarchy

This theme is the **upstream producer** of the `[FECollection]` schedule. Its consumer is
`ConstructFiniteElementSpaceHierarchy` (`multigrid.hpp:78-126`), which *pairs* this schedule's
`[FECollection]` with the mesh sequence: the coarse-seed uses `fecs[0]` (`multigrid.hpp:90`) and the
p-refinement loop `AddLevel`s a `fe_space` per `fecs[l]` (`multigrid.hpp:117`). The per-level
`FiniteElementSpace(mesh_l, fecs[l].get())` construction is the sibling
[`fe-space-construction-rotation`](./fe-space-construction-rotation.md) (the *consumer* rewrite across
the `[FECollection]` boundary); this theme produces the input it consumes.

## Status

`firm` — structural; the schedule rewrite is positively anchored at L0.
