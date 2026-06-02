---
agent: abstractor
invoked_at: 2026-06-02T161500Z
scope: L1>L0 theme sketch — fe-collection-construction-rotation
status: integrated
integrated_at: 2026-06-02T190000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied cycle-065 (D3). NEW firm book/src/L1-L0/fe-collection-construction-rotation.md (LHS L1 fe_collection schedule -> RHS L0 ConstructFECollections template body multigrid.hpp:22-73; 5-piece forward rewrite; 3 variant-axis rewrite cases; std::reverse load-bearing) + L1-L0/index.md theme row + SUMMARY chapter line. Build-relevant; the live link ../L1/fe_collection.md resolves (D2 landed earlier this cycle). L1>L0 firm themes +1. No gate hits; 0 new OQs."
inputs:
  - reference/palace/palace/fem/multigrid.hpp:22-73 (ConstructFECollections — the order schedule; on-disk verified, body return :72, closing brace :73)
  - reference/palace/palace/utils/labels.hpp:114-119 (MultigridCoarsening enum LINEAR/LOGARITHMIC)
  - reference/palace/palace/utils/configfile.hpp:918 (mg_coarsening default = LOGARITHMIC)
  - book/src/L1/fe_collection.md (D2 this-cycle prime entry — the operator this theme lowers; warrant=YES, firm-on-positive-structure)
  - reports/2026-06-02T160332Z-harvester-fe-collection/CYCLE.md (D2 report — read to match the lowering)
  - book/src/L1-L0/fe-space-construction-rotation.md (sibling FE-space-construction theme — structure template + construction-lowers/MFEM-owned split precedent)
---

# CYCLE: L1>L0 theme sketch — fe-collection-construction-rotation

## Summary

D2's warrant came back YES, so this L1>L0 theme is authored. It lowers the pure L1
[`fe_collection`](../L1/fe_collection.md) operator
(`fe_collection :: (p, dim, mg_max_levels, coarsening, family) → [FECollection]`, D2 this-cycle) into
the concrete Palace `ConstructFECollections` function-template body
(`palace/fem/multigrid.hpp:22-73`). This is a genuine **vocabulary translation, not a rename** (per the
2026-06-01 redirect): the L1 LHS is a pure declarative *schedule value* — a finest-to-coarsest order
sequence naming a list `[FECollection]`; the L0 RHS is an imperative `for`-loop that `push_back`es one
`make_unique<FECollection>` per level into a `std::vector`, decrements/halves the order via a switch,
breaks at a family floor, and finally **`std::reverse`s the accumulated vector** so the returned list
runs coarsest-to-finest. The declarative `(params) → [collections]` schedule and the
build-then-reverse imperative loop are different semantic organizations of the same enumeration — that
gap is the translation.

The **three variant axes** of the L1 operator are exactly the rewrite cases: (1) **de-Rham family** —
the L0 template parameter `FECollection`, which couples the `pmin` `constexpr` floor (`:30-33`), the
3-arg vs 4-arg ctor branch (`:46-55`), and the produced subclass; (2) **coarsening policy** — the
`MultigridCoarsening` `switch` (`:60-68`), `LINEAR` (`p--`) vs `LOGARITHMIC` (`p=(p+pmin)/2`); (3) **LOR
basis selection** — the `b2 = GaussLegendre`/`IntegratedGLL` choice (`:35-39`), inert for the 3-arg
(H1/L2) families. **Status assigned: `firm`** (structural; the schedule is read in full off a single
positive source body, matching D2's firm-on-positive-structure verdict). MPI/`Par*` flagged once:
out-of-scope — `ConstructFECollections` is rank-agnostic (it builds `FECollection` template objects,
not partitioned spaces; partitioning enters only downstream).

## Proposed changes

```new:book/src/L1-L0/fe-collection-construction-rotation.md
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

## Status

`firm` — structural. The schedule rewrite is positively anchored at L0: the entire
`ConstructFECollections` template body is read in full (`palace/fem/multigrid.hpp:22-73`), and every
piece of the forward rewrite has a positive source site — the family `pmin` `constexpr`
(`multigrid.hpp:30-33`) + its `MFEM_VERIFY` precondition (`:34`), the basis-type selection
(`:35-39`), the bounded `push_back` loop (`:44-69`) with the ND/RT-4-arg vs H1/L2-3-arg ctor branch
(`:46-55`), the early floor `break` (`:56-59`), the `LINEAR`/`LOGARITHMIC` coarsening `switch`
(`:60-68`), and the terminal `std::reverse` (`:70`). Every rewrite step is a syntactic identity /
loop-invariant on this positive structure — there is no convergence/iteration semantics to test-gate,
so the absence of a dedicated `test-multigrid.cpp` exercising `ConstructFECollections` does not gate
firm (matching D2's firm-on-positive-structure verdict + the `fe_space`/`fe_assemble`/`apply_linop`
no-dedicated-test precedent). The internal basis/dof structure of the produced `FECollection`s is
**MFEM-owned-read-as-given** (the `H1_/ND_/RT_/L2_FECollection` classes are MFEM's; this theme lowers
only the *order schedule + subclass + basis-type selection*) — a witnessed library-ownership boundary,
not a constructive reconstruction, so it does not gate firmness (cf. the firm
[`fe-space-construction-rotation`](./fe-space-construction-rotation.md) construction-lowers /
dof-bookkeeping-MFEM-owned split). MPI/`Par*` and mesh partitioning are out of scope (flagged once):
`ConstructFECollections` is rank-agnostic — it builds `FECollection` template objects, not partitioned
spaces; the per-rank distribution enters only downstream at the
`ConstructFiniteElementSpaceHierarchy` `mfem::ParFiniteElementSpace` wrapping (read single-rank).

## L1 form (LHS)

The pure schedule value (D2's prime entry [`L1/fe_collection`](../L1/fe_collection.md)):

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

## Verified-against

- `palace/fem/multigrid.hpp:23-26` — `ConstructFECollections<FECollection>(int p, int dim, int
  mg_max_levels, MultigridCoarsening mg_coarsening, bool mat_lor)` signature (template param + return
  `std::vector<std::unique_ptr<FECollection>>`). On-disk verified.
- `palace/fem/multigrid.hpp:30-34` — family `pmin` `constexpr` (`is_base_of<H1...> || is_base_of<ND...>
  ? 1 : 0`, `:30-33`) + `MFEM_VERIFY(p >= pmin, ...)` precondition (`:34`).
- `palace/fem/multigrid.hpp:35-39` — `b1 = GaussLobatto`, `b2 = GaussLegendre`, `if (mat_lor) b2 =
  IntegratedGLL` (the LOR basis variant axis C).
- `palace/fem/multigrid.hpp:44-69` — the bounded build loop (`max(1, mg_max_levels)` cap `:44`), the
  ND/RT-4-arg vs H1/L2-3-arg ctor branch (`:46-55`, `MFEM_CONTRACT_VAR(b2)` at `:54`), the floor
  `break` (`:56-59`), the `LINEAR`/`LOGARITHMIC` coarsening `switch` (`:60-68`).
- `palace/fem/multigrid.hpp:70` — `std::reverse(fecs.begin(), fecs.end())` (the coarsest-first
  reorientation). `:72` — `return fecs;` (body end; closing `}` at on-disk `:73`).
- `palace/utils/labels.hpp:114-119` — `enum class MultigridCoarsening : char { LINEAR, LOGARITHMIC }`
  (coarsening-policy variant axis B). On-disk verified.
- `palace/utils/configfile.hpp:918` — `MultigridCoarsening mg_coarsening = MultigridCoarsening::LOGARITHMIC`
  (the default policy). On-disk verified.
- `palace/models/spaceoperator.cpp:47/49/51` — the ND/H1/RT
  `ConstructFiniteElementSpaceHierarchy<FECollection>` de-Rham family selection sites (shared with the
  sibling FE-space theme).
- `palace/fem/multigrid.hpp:90` / `:117` — `ConstructFiniteElementSpaceHierarchy` consumer: coarse-seed
  uses `fecs[0]` (`:90`), p-refinement loop `AddLevel`s a `fe_space` per `fecs[l]` (`:117`) — the
  producer→consumer boundary to the FE-space theme.
- [`L1/fe_collection`](../L1/fe_collection.md) — the prime L1 entry this theme lowers (D2 this-cycle,
  firm-on-positive-structure).

## Open questions / caveats

- **Lifting note (reverse direction, working-note only).** The L0 `ConstructFECollections` body lifts
  to L1 `fe_collection` cleanly precisely because the produced collections' internal basis/dof
  structure is MFEM-owned-read-as-given — the lift discards the imperative build-then-reverse machinery
  and the `std::vector`/`unique_ptr` ownership plumbing, retaining only the `(p, dim, mg_max_levels,
  coarsening, family) → [FECollection]` schedule shape. The additional structure a *complete* (rather
  than opaque) lift would need is the `FECollection` subclass internals (node placement, dof tables),
  which are MFEM's and out of scope. (High→low formal content stays in the chapter above; this is a
  working note.)
- **`fe_space_hierarchy` consumer pull.** The producer→consumer relation to the FE-space theme makes
  the deferred `fe_space_hierarchy` sibling (`ConstructFiniteElementSpaceHierarchy`,
  `multigrid.hpp:78-126`) the natural next pull — it is the operator that *pairs* this schedule's
  `[FECollection]` with the mesh sequence. Named, not authored (per D2's deferred-sibling list).
- **Stale `:22-75` close in a prior reference.** The pre-D2 `fe_space.md:124-126`
  applicability-condition note (and the old `fe_collection` deferred-sibling row) cited
  `multigrid.hpp:22-75`; the body actually ends `return` at `:72`, closing `}` at on-disk `:73`. D2's
  cohort-bullet edit corrects the row; the `fe_space.md` in-prose references are out of this dispatch's
  write-scope — flagged for a later citation-hygiene pass (a change to propose, not to apply here).
```

```edit:book/src/SUMMARY.md
- [fe-space-construction-rotation](./L1-L0/fe-space-construction-rotation.md)
- [fe-collection-construction-rotation](./L1-L0/fe-collection-construction-rotation.md)
```

## Speculative operators proposed

None. This theme lowers the already-firm D2 L1 operator [`fe_collection`](../L1/fe_collection.md) into
the positively-anchored L0 `ConstructFECollections` body; no new L1 (or higher) operator is needed —
the schedule, the family floor, the coarsening policy, and the LOR basis are all read off positive
source, and the produced `FECollection` subclass internals are MFEM-owned-read-as-given (not an
operator to harvest). The deferred `fe_space_hierarchy` sibling (the consumer that pairs this
schedule's `[FECollection]` with meshes) is named in D2's deferred-sibling list, not proposed here.

## Supporting evidence

- The translation is genuine (not a `-body-identity` rename): the L1 LHS is a single declarative tuple
  → list value; the L0 RHS is a `std::vector<std::unique_ptr<FECollection>>` built by a bounded
  `for`-loop (`multigrid.hpp:43-69`) and then `std::reverse`d (`:70`). The build-finest-first /
  name-coarsest-first reorientation (the `std::reverse`) is the load-bearing reorganization the
  vocabulary shift exposes — the declarative schedule names the coarsest-first orientation directly,
  while the imperative loop must accumulate finest-first and reverse.
- All `multigrid.hpp` line numbers self-verified against the on-disk file
  `reference/palace/palace/fem/multigrid.hpp` via the Read tool (the planner's caution: codemap drifted
  ±1 on the neighbor `fespace.hpp` this batch). Confirmed on-disk: signature `:23-26`, `pmin` constexpr
  `:30-33` + `MFEM_VERIFY` `:34`, basis selection `:35-39`, build loop `:44-69`, ctor branch `:46-55`
  (`MFEM_CONTRACT_VAR(b2)` `:54`), floor break `:56-59`, coarsening switch `:60-68`, `std::reverse`
  `:70`, `return fecs` `:72`, closing `}` `:73`. Enum `labels.hpp:114-119` and default
  `configfile.hpp:918` confirmed on-disk.
- The theme matches D2's report (`reports/2026-06-02T160332Z-harvester-fe-collection/CYCLE.md`): same
  signature, same three variant axes, same firm-on-positive-structure rationale, same producer→consumer
  framing across the `[FECollection]` boundary to the FE-space construction.

## Open questions / caveats

- **Index dual-registration partition.** The `book/src/L1-L0/index.md` is a flat theme-list table +
  Working Notes; it carries NO §Vocabulary-cohort bullet sub-section (unlike the L1 layer index). So my
  per-theme registration is the theme-list TABLE ROW (registered above — anchor-distinct, parallel-safe)
  + the SUMMARY.md line (registered above). There is no separate cohort bullet to author in this index.
  Any **consolidated tally** (a cross-cohort firm-theme count, growth-log, or coverage-gap line) is
  DEFERRED to D4 (the count-owner this cycle) per the planner's dispatch. If D4 is not in fact the
  count-owner, integrator-finalize should reconcile any running total.
- **Live-link to D2's `L1/fe_collection.md`.** The theme forward-references
  [`L1/fe_collection`](../L1/fe_collection.md) as a live link per the planner's instruction (canonical
  slug `book/src/L1/fe_collection.md`, authored by D2 this same cycle). The link resolves once D2's
  entry lands; if integration order puts this theme before D2's entry, the linkcheck would transiently
  fail — integrator should apply D2 before (or in the same finalize as) this theme. (Both are
  this-cycle; the planner gated this theme on D2's warrant=YES, so D2 lands.)
- **Sibling `fe-space-construction-rotation` cross-reference.** This theme cross-links the firm sibling
  [`fe-space-construction-rotation`](./fe-space-construction-rotation.md) (on disk, c064) as the
  consumer rewrite across the `[FECollection]` boundary — a live link to an existing file, safe.

```edit:book/src/L1-L0/index.md
| [bilinear-form-mutation-rotation](./bilinear-form-mutation-rotation.md) | `L1/bilinear-form` (rough-in test-coverage-bounded) | `palace/linalg/operator.{hpp,cpp}`, `palace/models/boundarymodeoperator.cpp` | firm *(structural; 2 element-type sub-patterns A real-`A`/B complex-`A` + callsite cohort C; reuses apply_linop A `A.Mult(x,Ax)` (×2 lane-split for real-`A`; ×1 direct for complex-`A`) + dot A `Dot(comm,Ax,y)`; internally-allocated workspace `Ax` (Category-4 — distinct from `matrix-weighted-norm`'s caller-supplied `Bx`); L1/L0 conjugation-asymmetry reconciliation via argument-position swap; no SPD/Hermitian precondition; both M-symmetry witnesses Hermitian `Bttr`(:85) + non-Hermitian `Atn`(:90))* |
| [fe-collection-construction-rotation](./fe-collection-construction-rotation.md) | [`L1/fe_collection`](../L1/fe_collection.md) (firm c065) | `palace/fem/multigrid.hpp:22-73` (`ConstructFECollections` body), `palace/utils/labels.hpp:114-119` (`MultigridCoarsening` enum), `palace/utils/configfile.hpp:918` (default LOGARITHMIC), `palace/models/spaceoperator.cpp:47/49/51` (de-Rham sites) | firm *(structural; vocabulary-translation — pure declarative finest-to-coarsest p-multigrid schedule `(p, dim, mg_max_levels, coarsening, family) → [FECollection]` value → imperative build-then-`std::reverse` loop that `push_back`es one `make_unique<FECollection>` per level; **5-piece forward rewrite**: family `pmin` constexpr + `MFEM_VERIFY` `:30-34`, basis-type selection `:35-39`, bounded `push_back` loop + arity-3/4 ctor branch `:44-55`, coarsening `switch` `:60-68`, terminal `std::reverse` `:70`; **3 variant axes = the rewrite cases**: A de-Rham family (`H1_/ND_/RT_/L2_FECollection` ↔ `pmin` 1/1/0/0 + ctor arity 3/4), B coarsening policy (`LINEAR` `p--` / `LOGARITHMIC` `p=(p+pmin)/2`, default LOGARITHMIC), C LOR basis (`b2` GaussLegendre/IntegratedGLL, inert for 3-arg H1/L2); the `std::reverse` is the load-bearing build-finest-first-vs-name-coarsest-first reorganization; produced collections' internal basis/dof structure MFEM-owned-read-as-given (witnessed boundary, non-gating, cf. `fe-space-construction-rotation` split); **upstream-producer** rewrite of the FE-space sub-spine — produces the `[FECollection]` the sibling `fe-space-construction-rotation` consumes per-level at `multigrid.hpp:90/:117`; MPI/`Par*` rank-agnostic out-of-scope; firm-on-positive-structure, no-dedicated-`test-multigrid.cpp` caveat non-gating per D2 `fe_collection`/`fe_space`/`fe_assemble` precedent)* |
