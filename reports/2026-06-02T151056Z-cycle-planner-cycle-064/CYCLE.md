---
agent: cycle-planner
invoked_at: 2026-06-02T151056Z
scope: cycle-064 dispatch plan
status: pending
---

# Cycle 064 dispatch plan

## Goals selected this cycle

Open the **FE-space / mesh-construction L1 front** — the strategic steer the user just gave
(batch-19 meta-phase §5 ASK: "Open the FE-space/mesh-construction L1 front", chosen over continued
solver-test-load breadth). This is the largest un-opened in-scope denominator: `FiniteElementSpace`
has a firm `L0/fespace-file.md` chapter but ZERO L1 form, and `fe_assemble`/`weak_form_term`/
`eliminate_*` all take the space as an OPAQUE parameter — so the FE-assembly sub-spine (settled +
descent-complete as of batch-19) bottoms out on an un-lifted dependency. Cycle-064 is the
**front-opening cycle**: establish the FE-space sub-spine framing (in-scope-liftable vs out-of-scope
MFEM/`Par*`/mesh-partitioning) + land the single highest-fan-out FE-space construction operator that
`fe_assemble` most needs to stop treating the space as opaque, + its L1>L0 rotation. Focused
(4 dispatches) — opening the front cleanly matters more than breadth.

## FE-space front localization (codemap-verified; the evidence base for the picks)

**In-scope, cleanly L1-liftable (the shared substrate under every assembled-operator pipeline):**

- **`ConstructFiniteElementSpaceHierarchy`** (`palace/fem/multigrid.hpp:78-126`) — THE prime
  pick. The central space-hierarchy construction operator: seeds the coarse `FiniteElementSpace`
  (`:90-91`), runs the **h-refinement** loop over the mesh sequence (`:104-114`) and the
  **p-refinement** loop over the FE-collection sequence (`:117-124`), each `AddLevel`-ing a
  `FiniteElementSpace`, with optional **essential-true-dof** extraction per level
  (`GetEssentialTrueDofs`, `:97-100`/`:108-112`/`:119-123`). Every solver's space stack is built by
  it: `spaceoperator.cpp:47-77` calls it 4× (ND / H1 / RT / L2-curl collections). This is the
  construction that the L1 form lifts — `fe_assemble` consumes its output (`FiniteElementSpace`).
- **`ConstructFECollections`** (`palace/fem/multigrid.hpp:22-75`) — the FE-collection-sequence
  builder: the p-multigrid order schedule (`LINEAR`/`LOGARITHMIC` coarsening, `:60-67`) per
  collection type, branching on whether the collection is vector (ND/RT, 2-basis ctor `:46-49`) or
  scalar (H1/L2, 1-basis ctor `:51-53`). The input to `ConstructFiniteElementSpaceHierarchy`.
- **The `FiniteElementSpace` object as the typed L1 domain/range** (`fespace.hpp:21-194`,
  ctor `:67-75`) — the type that `fe_assemble`/`weak_form_term`/`eliminate_*` currently take
  opaque. Its identity is `(mesh, FECollection)`; the de-Rham collection family (H1 →∇ H(curl) →∇×
  H(div) →∇· L2) is named by the collection type. The MFEM-forwarding dof-count accessors
  (`GetTrueVSize`/`GetVSize`/`GetProlongationMatrix`, `fespace.hpp:93-103`) give the L1 true-dof ↔
  L-vector transfer surface.

**In-scope but SIBLING / pull-gated (NOT this cycle's front-opener — named for the framing, deferred):**

- `BuildDiscreteInterpolator` (`fespace.cpp:173-238`) — the discrete-de-Rham interpolator family
  (gradient / 3-D curl / 2-D scalar-curl / divergence dispatch); the standing
  `discrete-linear-operator-interpolation-sibling` OQ (c053 D3). Pull-gated on a multigrid /
  interpolation consumer.
- `BuildProlongationAtLevel` (`fespace.cpp:240-261`) — the input-side multigrid transfer
  (h-refinement `TransferOperator` / p-refinement `IdentityInterpolator`). Pull-gated on the
  geometric-multigrid V-cycle algebra.

**OUT OF SCOPE — flagged once, skipped (single-machine / `Par*`-single-rank scope per CLAUDE.md §Scope):**

- MPI / `Par*`: the wrapped `mfem::ParFiniteElementSpace` (`fespace.hpp:24`) is read single-rank as
  a serial `FiniteElementSpace`; `GetComm` (`fespace.hpp:186`) read single-rank. (The existing
  `L0/par-types-single-rank-reading` rule already covers this — the L1 form cites it, does not
  re-derive it.)
- MFEM-owned dof internals: dof/vdof numbering, byNODES/byVDIM ordering, element-to-dof tables,
  conformity, and the prolongation/restriction MATRICES are MFEM's (`fespace.hpp:93-103` thin
  `return Get().X()` forwarders). The L1 form treats the FE-space as an opaque index structure with
  a known true-dof ↔ L-vector transfer; the internal numbering is read as-given, NOT lifted.
- Mesh PARTITIONING and the libCEED basis/restriction caches: partitioning is out of scope; the
  four lazy `CeedObjectMap` caches (`fespace.cpp:44-132`) are transparent performance machinery
  (derived data of `(space, geometry, Ceed)`), a one-line annotation, NOT L1 vocabulary.

**The L0 chapter (`book/src/L0/fespace-file.md`) already previews the L1 lifts** (§"Notes for higher
layers", lines 147-174: "At L1, the FE-space is the typed domain/range object of the FE-assembly
map; this chapter anchors that object"; the de-Rham interpolator family; the multigrid transfer
stack) — the L0 evidence base is firm and on-disk, so the front opens onto a prepared L0 surface.

## Deliverable-presence verification

All named-artifact-slug dispatches below are **OPEN BY CONSTRUCTION** (a fresh front with NO prior
L1 FE-space form — the `fe-space-l1-form-untouched` OQ (c053 D3) has been deferred since cycle-053,
trigger now fired by the user steer). The target slugs are nonetheless verified-ABSENT and the L0
evidence verified-PRESENT, with pasted evidence:

| Dispatch | Check | Pasted evidence |
|---|---|---|
| D2 `book/src/L1/fe_space.md` | `ls` → ABSENT | `NOT FOUND: book/src/L1/fe_space.md` (also verified absent: `fespace.md`, `finite_element_space.md`, `construct_fespace_hierarchy.md`, `fespace_hierarchy.md`, `fe_collection.md`, `dof_map.md`) |
| D3 `book/src/L1-L0/fe-space-construction-rotation.md` | `ls` → ABSENT | `NOT FOUND: book/src/L1-L0/fe-space-construction-rotation.md` (also `fespace-construction-rotation.md` absent) |
| L0 evidence base | codemap `read_range` → PRESENT | `palace/fem/multigrid.hpp:78-126` (`ConstructFiniteElementSpaceHierarchy` body read), `:22-75` (`ConstructFECollections` body read), `palace/fem/fespace.hpp:67-75` (ctor read); `book/src/L0/fespace-file.md` firm on disk (291-line header anchored), wired in `SUMMARY.md:190` |
| STOP-PROPOSING negative-list check | none of the picks match | The list is `lu_solve`, `back_solve`, `ls-update-column`, 4 NLEPS atoms, `apply_nonlinear_pencil` (HELD), `L3/solve_family`, `L2/fold_solve`, `L2/fe_assemble` — NO FE-space-construction slug is on it. CLEAR. |
| Anti-mirror / redirect framing | D1 is observation-first scope; D2/D3 are a genuine new representation (opaque-param → typed L1 object), NOT a rename-mirror | The L1 form re-expresses the construction as a pure `(mesh, fec) → FiniteElementSpace` function — a real vocabulary shift from the C++ `ParFiniteElementSpace`-ctor + side-effecting dof-extraction; NOT identity-in-named-terms |

The canonical L1 slug `fe_space` and the L1>L0 slug `fe-space-construction-rotation` are stated
explicitly in BOTH the D2 and D3 dispatch scopes (cross-report forward-reference convention) so
neither producer invents a divergent working slug.

## Dispatches

**D1 — `cross-layer-cross-cutter` (observation-first front-scoping survey).**
- **scope**: Scope the FE-space L1 denominator as a front-opening survey (observation-only, NO
  `book/` mutation). Read `book/src/L0/fespace-file.md` (the firm L0 anchor) + the codemap-localized
  `palace/fem/multigrid.hpp:22-126` (`ConstructFECollections` + `ConstructFiniteElementSpaceHierarchy`)
  + `palace/fem/fespace.hpp:21-194` (the `FiniteElementSpace` wrapper) + the 4 construction call-sites
  `palace/models/spaceoperator.cpp:47-77`. Produce: (i) the **in-scope-liftable vs out-of-scope
  partition** (confirm/refine the localization above: `ConstructFiniteElementSpaceHierarchy` +
  `ConstructFECollections` + the `FiniteElementSpace` typed object are the liftable core; `Par*` /
  MFEM-dof-internals / mesh-partitioning / libCEED-caches are the scope-out, flagged ONCE); (ii) a
  **fan-out ranking of the specific L1 picks** (is the front one `fe_space` constructor operator, or
  does it split into `fe_space` + a separate `fe_collection` schedule + a `dof_map`? does the
  `weak_form_term` differential-operator axis already name the H1/H(curl)/H(div)/L2 spaces these
  terms live on — i.e. is the de-Rham family already half-present?); (iii) the **opaque-parameter
  inventory** — every firm L1 op that currently takes the FE-space opaque (`fe_assemble`,
  `weak_form_term`, `eliminate_essential_bc`, `eliminate_rhs`) and what each would gain from a typed
  L1 FE-space (the fan-out the lift unblocks). Record the `discrete-linear-operator-interpolation-sibling`
  + the multigrid-transfer sibling as named pull-gated NEXT picks (NOT this cycle). **CLEAN-GATE
  (redirect):** what the mesh can't cleanly say in shared spine vocabulary (MFEM-opaque dof
  numbering, partitioning) is a spine-finding, NOT a forced land — record it as such.
- **deps**: none.
- **rationale**: Front-opener survey. The steer says open the front; D1 establishes the sub-spine
  framing (the "shell") and validates/refines the fan-out ranking BEFORE the harvester commits to a
  specific operator decomposition — exactly the batch-19 active-head item-1 recommended shape
  ("A pre-survey dispatch should scope the FE-space L1 denominator … then per-component harvester/
  abstractor dispatches follow"). Observation-first per the redirect; resolves the framing half of
  the `fe-space-l1-form-untouched` OQ. **fan-out: HIGH** (the FE-space is the shared substrate under
  EVERY assembled-operator pipeline).

**D2 — `harvester` (the lead L1 FE-space construction operator).**
- **scope**: Harvest the **`book/src/L1/fe_space.md`** operator (canonical slug `fe_space` — D3
  forward-references it; the L1 form of FE-space construction). Re-express
  `ConstructFiniteElementSpaceHierarchy` (`palace/fem/multigrid.hpp:78-126`) +
  `ConstructFECollections` (`:22-75`) as a pure construction function: roughly
  `fe_space :: (Mesh, FECollection, BoundaryAttrs?) -> FiniteElementSpace` (single-level) lifted to
  the **hierarchy** form `(Mesh-seq, FECollection-seq) -> [FiniteElementSpace]` (the h- and
  p-refinement levels as a constructed list, the per-level essential-true-dof extraction as a pure
  derived `dbc_tdof_lists` output rather than the L0 out-param mutation). Name the typed
  `FiniteElementSpace` L1 object (identity = `(mesh, FECollection)`; the de-Rham collection family
  H1/H(curl)/H(div)/L2 as the FECollection variant axis). State laws on the construction (e.g.
  level-count = mesh-h-levels + fec-p-levels; coarse-to-fine ordering; the single-level degenerate).
  **Read `Par*` single-rank** per `L0/par-types-single-rank-reading` (cite it, don't re-derive);
  treat MFEM dof numbering as an opaque index structure with a known true-dof ↔ L-vector transfer
  (`GetProlongationMatrix`) — do NOT lift the internal numbering. The libCEED caches + `ResetCeedObjects`
  are a one-line transparent-performance annotation. **CLEAN-GATE:** if the construction does NOT
  lift cleanly in shared spine vocabulary (e.g. the h-vs-p refinement split forces an MFEM-mesh
  dependency that is itself opaque) → record the un-liftable part as a spine-finding, land the
  cleanly-liftable core, do NOT force. Pre-survey D1's fan-out ranking MAY refine whether this is
  one `fe_space` op or splits — defer to D1's recommendation on the decomposition (sequenced
  wave-2). Author the dep-map row + the §Vocabulary-cohort registration for the new FE-space cohort
  in `book/src/L1/index.md` (D2 owns its OWN row + bullet; if a consolidated count-tally bump is
  needed, D2 owns it as the sole FE-space-cohort landing this cycle).
- **deps**: D1 (wave-2 — consume D1's in-scope/out-of-scope partition + fan-out-ranked decomposition
  recommendation before committing the operator shape).
- **rationale**: The single highest-fan-out FE-space operator — the construction that produces the
  typed object every assembled-operator pipeline consumes opaquely. Landing it is what lets
  `fe_assemble`/`weak_form_term`/`eliminate_*` stop treating the space as an opaque parameter.
  **fan-out: HIGH** (unblocks the assembly half's foundation + the de-Rham collection family + the
  pull-gated interpolation/prolongation siblings).

**D3 — `abstractor` (the L1>L0 construction rotation theme).**
- **scope**: Author **`book/src/L1-L0/fe-space-construction-rotation.md`** (canonical slug
  `fe-space-construction-rotation`; the L1>L0 rotation for the new `fe_space` operator — D2 authors
  `book/src/L1/fe_space.md` this cycle, canonical slug `fe_space`, so the LHS is a live link).
  Narrate FORWARD (L1 → L0) how the pure `fe_space` construction form lowers into the L0 source:
  the `ConstructFiniteElementSpaceHierarchy` body (`palace/fem/multigrid.hpp:78-126`) — the
  coarse-seed + h-refinement-loop + p-refinement-loop structure, the per-level `AddLevel` mutation
  of the `FiniteElementSpaceHierarchy`, and the **essential-true-dof extraction as L0 out-param
  mutation** (`GetEssentialTrueDofs(dbc_marker, dbc_tdof_lists->emplace_back())`) lowering from the
  pure derived-output L1 form (this is the genuine vocabulary shift — pure construction-returning
  L1 vs side-effecting accumulate-into-out-param L0). Treat the `ConstructFECollections` order
  schedule (`:22-75`) as the L0 realization of the FECollection-sequence input. Cite the
  `mfem::ParFiniteElementSpace` ctor (`fespace.hpp:67-75`) read single-rank. **Redirect:
  lowering-is-a-translation, NOT a rename** — if the L1→L0 rewrite is a degenerate identity-in-named
  -terms, that is a SMELL (record it as such; the construction is NOT a candidate for a thin
  identity theme — the out-param-mutation absorption is the substantive rewrite). Author the dep-map
  row + cohort registration in `book/src/L1-L0/index.md` (D3 owns its OWN row + bullet).
- **deps**: D1 (wave-2 — consume the framing), D2 (wave-2 — the LHS `fe_space` operator must exist;
  serial-per-report ordering makes D2's `book/src/L1/fe_space.md` live before D3's link resolves at
  finalize).
- **rationale**: An L_n operator landing without its adjacent-edge lowering leaves the front
  half-open. Co-scheduling the L1>L0 rotation in the SAME cycle (the
  `floor-landing-implies-same-cycle-adjacent-entry-reanchor` discipline, applied to a fresh front:
  land the op + its lowering together) opens the front with a complete L1↔L0 edge. **fan-out:
  MEDIUM** (completes the L1>L0 edge for the FE-space front; documents the construction rewrite the
  downstream burn effort needs).

**D4 — `layer-intro-author` (FE-space sub-spine framing in the L1 + L1-L0 indices).**
- **scope**: Establish the **FE-space sub-spine framing** in `book/src/L1/index.md` (and a matching
  note in `book/src/L1-L0/index.md`): add a §Vocabulary-cohort subsection / motif entry naming the
  FE-space construction sub-spine as a NEW cohort distinct from the FE-assembly sub-spine (the
  FE-assembly ops CONSUME the FE-space; the FE-space construction sub-spine PRODUCES it — the
  substrate-vs-assembler distinction). State the in-scope-liftable vs out-of-scope boundary at the
  index level (single-rank `Par*`, MFEM-dof-internals-as-given, mesh-partitioning-out) as the
  reader-facing framing, sourced from D1's survey verdict. Register the count delta from D2's landing
  (FE-space cohort: 1 firm `fe_space`). **Count discipline (c057-meta count-owner guard):** compute
  any firm count by reading the linked chapter's `## Status` line, NOT the drift-prone index cells;
  D4 owns the consolidated §Vocabulary-cohort header-prose count, D2 owns its own dep-map TABLE row +
  bullet (dual-registration partition — D4 does NOT author D2's row; D2 does NOT author the cohort-
  header prose count). The grand-total prose currently reads "31 firm" (27 main + 4 FE-assembly);
  D4 adds the FE-space cohort line and the new grand total.
- **deps**: D1 (wave-2 — the in-scope/out-of-scope framing is D1's survey output), D2 (wave-2 — count
  the `fe_space` firmness from D2's landed `## Status` line, not a guess).
- **rationale**: Front-opening cycles need the "shell" — the index-level framing that tells a reader
  the FE-space sub-spine exists, what's in it, and where the in-scope boundary sits. This is the
  layer-intro-author's front-establishing role. Owns the consolidated count so the parallel-blind
  shared-index-count divergence does not occur. **fan-out: MEDIUM** (establishes the cohort home that
  every future FE-space pick registers into).

## Overlap analysis

- **D1 ↔ D2/D3/D4**: D1 is observation-only (NO `book/` mutation) — it produces a survey verdict, not
  artifact edits. It cannot collide with any artifact writer. D2/D3/D4 CONSUME D1's verdict (deps),
  but that is a forward-reference ordering, not a region overlap. NON-overlapping.
- **D2 ↔ D3**: D2 writes `book/src/L1/fe_space.md` + a row in `book/src/L1/index.md`; D3 writes
  `book/src/L1-L0/fe-space-construction-rotation.md` + a row in `book/src/L1-L0/index.md`. Distinct
  files. D3 forward-references D2's `fe_space.md` (live link) — a cross-Part link dependency resolved
  by serial-per-report ordering (D2 applied first), NOT a same-region write. NON-overlapping at the
  artifact-write level (the link is a dependency, sequenced).
- **D2 ↔ D4**: BOTH touch `book/src/L1/index.md` — but on **anchor-distinct regions by the
  dual-registration partition** (per the cycle-045 meta-phase convention + the c062 D3/D2 working
  precedent): **D2 owns its OWN dep-map TABLE row + its OWN §Vocabulary-cohort BULLET** (anchor-
  distinct, parallel-safe, NOT deferred); **D4 (count-owner) owns ONLY the consolidated
  §Vocabulary-cohort HEADER-PROSE count + the new FE-space cohort framing subsection**. This is the
  standard harvester(row+bullet) / layer-intro-author(cohort-header-prose-count) seam — it landed
  clean at c062 on this exact file. Stated explicitly: D2 appends its `fe_space` table row + cohort
  bullet; D4 authors the FE-space-cohort framing subsection + the grand-total prose count; D2 does
  NOT touch the grand-total prose, D4 does NOT author D2's row/bullet. NON-overlapping by partition.
- **D3 ↔ D4**: D3 writes `book/src/L1-L0/index.md` (its own dep-map row + bullet); D4 may add a
  matching FE-space-framing NOTE in `book/src/L1-L0/index.md`. Mild potential co-write on the
  L1-L0 index. Per the conflict-tolerance philosophy (when in doubt, PARALLEL — but these are
  deps-sequenced to the same wave-2 anyway), the partition is: **D3 owns its own
  `fe-space-construction-rotation` dep-map row + bullet; D4 owns ONLY the FE-space-cohort framing
  note** (if any) in the L1-L0 index. Anchor-distinct. The serial-per-report integrator handles any
  residual seam; this is exactly the minor-conflict-as-signal case the philosophy says to mark
  parallel. NON-overlapping by partition (D3 row+bullet vs D4 framing-note).

No two dispatches modify the same operator entry or rewrite the same theme body. The only shared
files (`L1/index.md`, `L1-L0/index.md`) are partitioned by the dual-registration convention.

## Sequencing schedule

- **Wave 1 (the front-scoping survey)**: **D1** alone. Observation-only; its verdict (in-scope/
  out-of-scope partition + fan-out-ranked decomposition recommendation) is the input the other three
  consume. Front-opening cycles benefit from scoping BEFORE committing the operator shape — this is
  the one place a serial gate buys correctness (it prevents D2 from guessing a decomposition D1's
  survey would refine).
- **Wave 2 (parallel, after D1's report lands)**: **D2**, **D3**, **D4** in parallel. D2 lands the
  `fe_space` operator; D3 lands the L1>L0 rotation (forward-references D2's slug, resolved by
  serial-per-report ordering at integration); D4 lands the index framing + count (counts from D2's
  landed `## Status`). The three are partitioned (D2 file + own row/bullet; D3 file + own row/bullet;
  D4 cohort-header prose count + framing subsection) — parallel-safe.

Rationale for the wave split (not all-parallel): D1's survey genuinely de-risks the operator
decomposition (one `fe_space` vs a split into `fe_space` + `fe_collection` + `dof_map`). This is a
fresh front with no prior L1 precedent, so the cheap observation-first scoping pass is worth one
serial gate — consistent with the batch-19 active-head item-1 "pre-survey dispatch … then
per-component harvester/abstractor dispatches follow" shape. (If the orchestrator judges the
decomposition obvious enough to skip the gate, D1+D2+D3+D4 could collapse to one wave with D2/D3/D4
proceeding on the localization in THIS plan — but the conservative wave-2 sequencing is the
recommended front-opening shape.)

## Open questions / caveats

- **Decomposition granularity is D1's call.** I localized `ConstructFiniteElementSpaceHierarchy` +
  `ConstructFECollections` + the `FiniteElementSpace` typed object as the liftable core, and scoped
  D2 as a single `fe_space` operator (with the hierarchy + FECollection-schedule folded in). D1's
  survey may recommend a split (e.g. `fe_space` for the single-level typed object + a separate
  `fe_collection` for the p-multigrid order schedule + a `dof_map`/`true_dof_restriction` for the
  T-dof ↔ L-dof transfer). I deliberately deferred the final decomposition to D1 rather than
  over-committing the harvester scope. If D1 recommends a 2-or-3-operator split, the orchestrator
  should re-scope D2 (and possibly add a wave-2 sibling harvester) accordingly — within the
  ≤12-dispatch cap there is room.
- **The `dof_map` / true-dof-restriction is a candidate I did NOT promote to a dispatch.** The
  true-dof ↔ L-vector transfer (`GetProlongationMatrix`/`GetRestrictionMatrix`,
  `fespace.hpp:102-103`) is MFEM-owned (thin forwarders), so it reads as an opaque transfer the L1
  FE-space object carries, NOT a separately-liftable operator. If D1's survey finds the transfer is
  load-bearing enough to name as its own L1 vocabulary (e.g. because `eliminate_essential_bc`'s
  essential-true-dof handling needs it explicitly), that is a wave-2-or-next-cycle addition. Flagged
  for D1.
- **Sibling pull-gated picks are named, not dispatched.** `discrete-linear-operator-interpolation-sibling`
  (c053 D3 OQ; `BuildDiscreteInterpolator`, the de-Rham interpolator family) and the multigrid-
  transfer prolongation (`BuildProlongationAtLevel`) are in-scope but pull-gated (a multigrid /
  interpolation consumer pull). They are the natural NEXT FE-space picks (cycle-065/066) once the
  `fe_space` substrate is firm. Recorded in the priorities append below as the FE-space sub-spine
  Backlog.
- **No escalating-friction work is owed this cycle.** The two `escalating`-status ledger patterns
  (`skill-uptake-survey` benign-telemetry; the citecheck citation-drift, mechanized via
  `tools/citecheck/`) are both already addressed — no FE-space-front dispatch is needed to serve
  them. The c062 D3 citecheck-misattribution is a report-only one-off (batch-19 decision 4, NOT
  ledgered) — watch only.
- **Cadence note**: cycle-064 is the FIRST primary cycle of meta-batch-20 (064/065/066; meta fires
  after 066's finalize). The FE-space front will run across the batch (064 opens it; 065/066 descend
  it + pick up the pull-gated siblings as consumers materialize). If the front surfaces a
  methodology pattern before the batch-20 meta-phase entry lands, I will note it here for the next
  meta-phase.
