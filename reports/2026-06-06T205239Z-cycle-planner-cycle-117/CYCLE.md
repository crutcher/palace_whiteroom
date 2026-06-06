---
agent: cycle-planner
invoked_at: 2026-06-06T205239Z
scope: cycle-117 dispatch plan
status: pending
---

# Cycle 117 dispatch plan

## Goals selected this cycle

Cycle-117 is the THIRD/FINAL primary cycle of meta-batch-37 (115/116/117; the batch-37 meta-phase
fires after this finalize). The semantic-consolidation LEAD (campaign 1, directive A) landed clean
in c116 (`00a8f78`: surface moved to `book/src/semantics/index.md`, the 27-file restatement cohort
fully swept), so the post-consolidation gate is satisfied. **This cycle executes campaign 2
(`open-all-feature-fronts`, directive B, HIGH fan-out): ONE wide multi-dispatch fan-out opening ALL
remaining in-scope deferred feature fronts SIMULTANEOUSLY** to exploit shared-exploration lifting —
the mesh→fe_space→assemble→solve→readout chain these fronts touch is lifted ONCE across the wave.

**Substrate localization (codemap-verified, on-disk-confirmed) determined that every front has
on-disk Palace substrate that composes ALREADY-FIRM book vocabulary** — so each lands as a real
firm/rough-in chapter, NONE forced to a `roadmap_goal` rank-0 placeholder. The fronts collapse to
five dispatches (front (iii) `fe_space` siblings reduces because `essential_dofs` is ALREADY FIRM on
disk — only `fe_space_hierarchy` + the de-Rham interpolator remain). Linter baseline confirmed
unchanged (`files=356, reachable=133, rank_violations=0, untyped=61, promotion_frontier=8,
detritus=126, roots=36, STRONGER=23`).

## Deliverable-presence verification

Per the MANDATORY pre-dispatch deliverable-presence discipline (paste-inline-evidence). The four
NEW-front dispatches (D1, D3, D4, D5) are **open by construction** (fresh front-authoring of files
with no prior-cycle history — the demand-gate was only fired by directive-B post-c115); D2 targets an
EXISTING `seed` column and gets the full four-step check.

**Baseline linter run (the c117 ground truth):**
```
$ python3 tools/graded-stack-lint/graded_stack_lint.py --book-src book/src --json | <extract totals>
totals: {"files": 356, "typed": 295, "untyped": 61, "roots": 36, "rank_violations": 0,
         "unresolved_depends_on_targets": 0, "promotion_frontier": 8, "reachable": 133,
         "detritus": 126, "detritus_no_typed_edges_pre_p1_artifact": 103,
         "detritus_with_typed_edges_stronger_signal": 23, "expected_unreachable_outside_dag": 45}
```
Matches the stated baseline exactly.

**D1 — `waveguide-mode` output-product column (L4/L1/L0)** — OPEN BY CONSTRUCTION (new front):
```
$ ls book/src/feature/waveguide-mode.*
ls: cannot access 'book/src/feature/waveguide-mode.*': No such file or directory
```
Absent → authoring is a no-op risk = nil. Substrate present (see Substrate-localization below):
`boundarymodesolver.cpp:300-340` (the readout/reduction) + firm `eigsolve`. NOT on the STOP-PROPOSING
negative list (that list is L3-backfill vocabulary slugs; this is a feature column). Not structurally
blocked — directive-B FIRES this demand-gate (priorities.md item-2; the prior
`waveguide-mode-output-product-column-demand-gated` gate is LIFTED).

**D2 — `boundary-mode` column promotion off `seed`** — EXISTING column, four-step check:
1. File existence:
   ```
   $ ls book/src/feature/boundary-mode.{L0,L1,L4}.md   → all three present
   ```
2. Maturity / already-discharged:
   ```
   $ grep -m1 'feature_root:' book/src/feature/boundary-mode.{L0,L1,L4}.md
   boundary-mode.L0.md: feature_root: seed
   boundary-mode.L1.md: feature_root: seed
   boundary-mode.L4.md: feature_root: seed   (rank: rough-in)
   ```
   Still `seed` → promotion to a promoted feature_root is NOT yet discharged. NOT a no-op.
3. OQ-ledger RESOLVED-grep: the gating OQ
   (`boundary-mode-waveguide-output-product-column-needs-home`) is the OWN-readout gate; directive-B
   + the D1 waveguide-mode landing FIRE it. Under the OWN-COMPOSITION rule, the waveguide-mode column
   is a cross-linked SIBLING reference, NOT a blocking constituent — boundary-mode promotes on its
   OWN firm constituents (`fe_assemble`×2, `eigsolve`, the per-mode readout), all firm on disk.
4. Structural-block check: the prior block was "own stage-(3) readout reduces into a waveguide-mode
   product with no firm home" (`feature/index.md:80`). D1 lands that home THIS cycle → block clears.
   Per CLAUDE.md §Extraction-goal OWN-COMPOSITION rule + `feature/index.md:67-69`, the sibling column
   is a reference not a blocker, so promotion is licensed once D1 provides the live cross-link target.

**D3 — `Mesh` / `build_mesh` mesh-wrapper L1 op** — OPEN BY CONSTRUCTION (new front):
```
$ ls book/src/L1/mesh.md book/src/L1/build_mesh.md book/src/concepts/mesh.md
(all three: No such file or directory)
```
Absent. Referent already forward-referenced as `build_mesh :: Config -> Mesh` in `lifecycle.L1`
(`mesh::Load`/`Partition`/`RefineMesh`, `main.cpp:287-302`) and `lifecycle.L4`/`L1/index.md`. Substrate
`palace/fem/mesh.hpp:44-77`. Single-machine scope (§Scope: `ParMesh`-distributed methods read as
single-rank; `Par*`/partitioning OUT). NOT structurally blocked — directive-B fires the mesh-wrapper
demand-gate.

**D4 — `fe_space_hierarchy` L1 op** — OPEN BY CONSTRUCTION (new front):
```
$ ls book/src/L1/fe_space_hierarchy.md book/src/concepts/fe_space_hierarchy.md
(both: No such file or directory)
```
Absent. Already forward-referenced in `fe_space.md` ("spaces this way through
`ConstructFiniteElementSpaceHierarchy` (`palace/fem/multigrid.hpp:78-126`)") + `fe_collection.md`
(firm; names the hierarchy as the FECollection-list consumer). Composes firm `fe_space` + firm
`fe_collection`. NOT blocked — directive-B fires the `fe_space`-siblings demand-gate.

**D5 — de-Rham discrete interpolator L1 op** — OPEN BY CONSTRUCTION (new front):
```
$ ls book/src/L1/*interpol* book/src/L1/*de_rham* book/src/L1/*derham*
(none: No such file or directory)
```
Absent. Substrate `palace/fem/interpolator.hpp:50-56` (`InterpolateFunction`, GSLIB) +
`GetDiscreteInterpolator` (ND→RT discrete interpolator, `boundarymodesolver.cpp:322`), referenced by
divfree-projector. NOT blocked — directive-B fires the `fe_space`-siblings demand-gate. NOTE: the
GSLIB point-interpolation path is library-owned → likely `rough-in` (the discrete-interpolator
structure is firm; the GSLIB leaf is the obstruction-documented opaque piece, NOT forced).

**`essential_dofs` (front (iii), third sibling) — ALREADY DISCHARGED, NOT dispatched:**
```
$ grep -m2 'status:\|rank:' book/src/L1/essential_dofs.md
status: firm
rank: firm
```
Already FIRM on disk (harvested c066). Front (iii) therefore reduces to D4 + D5 only. No dispatch.

## Substrate localization (codemap-verified, on-disk-confirmed)

All paths verified via `palace-codemap` MCP (`search_text` / `read_range` / `list_files`), then the
exact ranges read on-disk. Pre-supplied here so the producers proceed to authoring, not a localization
loop (dispatch-resilience discipline).

- **waveguide-mode product (D1):** `palace/drivers/boundarymodesolver.cpp` — the per-mode readout/
  reduction: `ApplyVDBackTransform(e0, kn, et, en)` (`:300`), `ComputePoyntingPower` (`:304`),
  power-normalization (`:300-314`), `IsPropagating(kn)` (`:316`), `Bz = curl(Et)/(iω)` (`:316`),
  `MeasureAndPrintAll` (`:314`), the report loops (`:273`, `:292`). The product = the converged
  propagation-mode set `{kn, n_eff = kn/ω, (Et, En, Bz)}`, power-normalized to `|P|=1`. The
  `boundary-mode.L1` body ALREADY decomposes this readout and explicitly flags "the reduction into
  the reported waveguide-mode product is a forward-ref (no dedicated output-product column yet)" —
  D1 homes exactly that.
- **mesh wrapper (D3):** `palace/fem/mesh.hpp:44` `class Mesh`; variadic ctor `:69-72` +
  unique_ptr ctor `:73-77` (`EnsureNodes()` + `Update()`); single-machine surface `Get()`/
  `Dimension()`/`SpaceDimension()`/`GetNE()`/`GetNBE()` (`:84-94`) + the libCEED attribute map
  (`:96-115`). `build_mesh` referent: `mesh::Load`/`Preprocess`/`Partition`/`RefineMesh`
  (`palace/main.cpp:287-302`, per `lifecycle.L1`). [Codemap-hint ranges — D3 must on-disk-confirm
  the close-brace END lines; `mesh.hpp:77` ctor-END is the off-by-one-prone bound.]
- **fe_space_hierarchy (D4):** `palace/fem/multigrid.hpp:78-126` `ConstructFiniteElementSpaceHierarchy`
  (coarse-seed `:89-90`, `AddLevel` per-level `:106,117`); the p-MG order schedule `:41-69` (the
  `fe_collection` consumer). Composes firm `fe_space` (`L1/fe_space.md`) + firm `fe_collection`
  (`L1/fe_collection.md`). [Codemap-hint range — D4 on-disk-confirms the `:126` END.]
- **de-Rham interpolator (D5):** `palace/fem/interpolator.hpp:50-56` (`InterpolateFunction` GSLIB
  point-interp) + the discrete de-Rham interpolator `GetDiscreteInterpolator(...)`
  (`boundarymodesolver.cpp:322`, ND→RT `DiscreteLinearOperator`-based grid transfer).

## Dispatches

- **D1 — `layer-intro-author`** — scope: **`waveguide-mode` 6th output-product feature column**, new
  files `book/src/feature/waveguide-mode.{L4,L1,L0}.md` (high→low within-column ordering, the
  deliberate directive-3 exception). The output-product composition root: input = the
  `boundary-mode` driver's converged eigenpair family; body = the per-mode reduce verb
  (`kn`/`n_eff`/`(Et,En,Bz)` extraction + power-normalization); output = the waveguide-mode physical
  product. Compose the firm `eigsolve` readout vocabulary; the product reduce verb is the
  analog of `sparameter_reduce`/`domain_energy_reduce`. Substrate `boundarymodesolver.cpp:300-340`
  (pre-supplied above). **D1 OWNS the shared feature index this cycle:** the
  `feature/index.md` matrix row (insert ALPHA in the output-product group — `waveguide-mode` sorts
  AFTER `sparameters`, i.e. last output-product row), the `feature/output-product.md` group-intro
  prose, AND the `feature/SUMMARY.md` `# Feature surfaces` block (3 new entries). Clean-gate: paste
  the on-disk firm-status evidence for `eigsolve` it composes.
  *Rationale:* directive-B front (i); the highest-fan-out front (it unblocks D2's promotion + closes
  the last output-product-cohort hole). priorities.md item-2.

- **D2 — `layer-intro-author`** — scope: **`boundary-mode` driver-leaf column promotion off `seed`**,
  editing `book/src/feature/boundary-mode.{L4,L1,L0}.md` `feature_root: seed` → promoted, under the
  OWN-COMPOSITION rule (own `fe_assemble`×2 + `eigsolve` + readout all firm; the waveguide-mode column
  is a cross-linked SIBLING reference, NOT a blocker). **D2 forward-references the live D1 column
  `book/src/feature/waveguide-mode.L4.md` (+ `.L1`/`.L0`) — canonical slug `waveguide-mode`, authored
  by D1 THIS cycle** (cross-report forward-reference slug coordination: both D1 and D2 use the exact
  slug `waveguide-mode`). Update the boundary-mode `## Promotion` prose + the `feature/index.md:80`
  `seed`-explanation line (D1 owns the index file → D2 hands its index-row delta to D1, see Overlap).
  *Rationale:* directive-B front (ii); promotes the last `seed` driver column, closing the
  driver-leaf cohort.

- **D3 — `harvester`** — scope: **`Mesh` / `build_mesh` mesh-wrapper L1 operator**, new file
  `book/src/L1/mesh.md` (or `book/src/L1/build_mesh.md` — harvester's call on the operator name; the
  `lifecycle.L1` forward-ref uses `build_mesh :: Config -> Mesh`, so prefer `build_mesh` as the op
  with `Mesh` as the produced record). Formalize the single-machine mesh construction:
  `build_mesh :: Config -> Mesh` (load → preprocess → partition[single-rank] → a-priori-refine), the
  `Mesh` record (the `mfem::ParMesh` wrapper read single-rank + the libCEED local-attribute mapping).
  **Single-machine scope ONLY** — `Par*`/distributed mesh-partitioning OUT (flag-once-skip per
  §Scope); MFEM-opaque adaptive mesh-refinement leaves stay obstruction-documented, NOT forced.
  Substrate `fem/mesh.hpp:44-77` + `main.cpp:287-302` (pre-supplied). If the `Mesh` record needs a
  definition home with ≥2 consumers, flag `record-Mesh-needs-definition-home`.
  *Rationale:* directive-B front (iv); homes the `lifecycle` spine-ROOT's forward-referenced
  `build_mesh`/`Mesh` — high reuse (every driver column's mesh stage).

- **D4 — `layer-intro-author`** — scope: **`fe_space_hierarchy` L1 operator**, new file
  `book/src/L1/fe_space_hierarchy.md`. The p-multigrid FE-space hierarchy as an `AddLevel`-fold over
  firm `fe_space` + firm `fe_collection`: `fe_space_hierarchy :: [Mesh] -> [FECollection] -> Config ->
  FiniteElementSpaceHierarchy` (coarse-seed + one `fe_space` per MG level). Compose firm `fe_space`
  + firm `fe_collection` (paste their on-disk firm-status as the clean-gate evidence). Substrate
  `fem/multigrid.hpp:78-126` (+ the `:41-69` schedule, pre-supplied). Re-anchor the `fe_space.md`
  forward-ref to a live link if it currently plain-text-refers (coupled re-anchor — see Overlap).
  *Rationale:* directive-B front (iii)-a; homes the FE-space hierarchy the solve preconditioners +
  boundary-mode `GetNDSpaceHierarchy` rest on.

- **D5 — `harvester`** — scope: **de-Rham discrete interpolator L1 operator**, new file
  `book/src/L1/interpolator.md` (harvester's call on the slug). The de-Rham-family grid-transfer
  interpolator: the discrete `DiscreteLinearOperator`-based ND→RT (and de-Rham-family) interpolator
  `GetDiscreteInterpolator`, plus the GSLIB point-interpolation `InterpolateFunction`. Likely
  `rough-in` — the discrete-interpolator structure is firm but the GSLIB point-interp leaf is
  library-owned (obstruction-document the GSLIB leaf, do NOT force a firm claim on it). Substrate
  `fem/interpolator.hpp:50-56` + `boundarymodesolver.cpp:322` (pre-supplied).
  *Rationale:* directive-B front (iii)-b; the third `fe_space` sibling. Lowest-fan-out of the five
  (thin, partly-opaque) — co-scheduled to exploit the shared FE-space substrate D4 also touches.

## Overlap analysis

Pairwise (5 dispatches → 10 pairs):

- **D1 × D2** — OVERLAPPING (shared feature index + forward-reference). Both touch the
  `feature/` index surface (D1 owns it; D2 has an index-row delta for the boundary-mode `seed`-line
  at `feature/index.md:80`) AND D2 forward-references D1's not-yet-existing `waveguide-mode.*` files.
  Resolution: **D2 in a later wave than D1** (so the per-report integrator wires D2's cross-link to a
  live D1 file); **D1 SOLE-OWNS the `feature/index.md` matrix + `feature/output-product.md` +
  `feature/SUMMARY.md`** (the parallel-blind-shared-index guard — D1 authors the waveguide-mode rows
  AND applies the boundary-mode `seed`→promoted index-line edit on D2's behalf; D2 edits ONLY its own
  three `boundary-mode.*` chapter bodies + frontmatter, defers all `feature/index.md` +
  `feature/SUMMARY.md` edits to D1). Canonical slug `waveguide-mode` stated in BOTH scopes.
- **D1 × D3 / D1 × D4 / D1 × D5** — NON-overlapping. D1 writes `feature/waveguide-mode.*` +
  `feature/{index,output-product}.md` + `feature/SUMMARY.md`; D3/D4/D5 write `L1/*.md`. Disjoint
  files. D1 composes `eigsolve` (reads, does not modify). No shared region.
- **D2 × D3 / D2 × D4 / D2 × D5** — NON-overlapping. D2 edits `feature/boundary-mode.*` bodies;
  D3/D4/D5 write distinct `L1/*.md`. boundary-mode.L1 *cites* `fe_assemble`/`eigsolve` (reads), not
  the new mesh/hierarchy/interpolator ops. Disjoint.
- **D3 × D4** — NON-overlapping at the operational level, SHARED-SUBSTRATE adjacency. D3 writes
  `L1/build_mesh.md` (or `L1/mesh.md`); D4 writes `L1/fe_space_hierarchy.md`. Distinct files. D4's
  `fe_space_hierarchy` takes `[Mesh]` as input → it REFERENCES D3's `Mesh` record. This is a
  forward-reference, not a same-region edit: **D4 references `L1/build_mesh`/`Mesh` (canonical:
  whichever slug D3 lands — D4 cross-links the `Mesh` record D3 defines)**. Sequence D4 after D3 so
  the per-report integrator wires a live link, OR D4 plain-text-refers + a later lifter re-anchors
  (prefer the former — same-cycle coupling). State the slug coordination: D3 lands `Mesh` (record) in
  `L1/build_mesh.md`; D4 references `L1/build_mesh` for the `Mesh` input type.
- **D3 × D5** — NON-overlapping. Distinct `L1/*.md` files; no shared region (interpolator does not
  consume the mesh wrapper directly in the L1 surface).
- **D4 × D5** — NON-overlapping, shared FE-space substrate (both touch `fem/multigrid.hpp` /
  `fespace.hpp` REGION of Palace, but write DISTINCT book files `L1/fe_space_hierarchy.md` vs
  `L1/interpolator.md`). The shared-exploration-lifting is the POINT (directive-B): they lift the
  FE-space substrate together. No book-file conflict. Mark PARALLEL.
- **L1/index.md shared aggregate:** D3/D4/D5 each ADD a distinct API-list row to `L1/index.md`
  (alpha-within-kind). Per the discipline, distinct dep-map ROWS are parallel-safe; but `L1/index.md`
  carries NO consolidated Working-Notes firm/obstruction running-count tally that these three would
  each rewrite blind (the L1 index aggregate is the firm-count, and the integrator-finalize applies
  count bumps — NOT the producers). To be safe: **D4 (the layer-intro-author, owns layer-index
  narrative) owns any `L1/index.md` consolidated count/tally touch this cycle; D3 + D5 (harvesters)
  add ONLY their own alpha-position API-list row + SUMMARY registration, defer any tally to D4.** Each
  of D3/D4/D5 adds its OWN `L1/index.md` row + its OWN `SUMMARY.md` entry (anchor-distinct,
  parallel-safe — NOT deferred); only a consolidated count, if any, defers to D4.

## Sequencing schedule

Two waves (forward-reference ordering only; the book is NOT rebuilt between waves and there is exactly
ONE `integrator-finalize` at cycle end).

- **Wave 1 (parallel — the substrate-lifting frontier):**
  - **D1** `waveguide-mode` output-product column (+ owns `feature/` index/SUMMARY).
  - **D3** `build_mesh`/`Mesh` mesh-wrapper L1 op.
  - **D4** `fe_space_hierarchy` L1 op.
  - **D5** de-Rham interpolator L1 op.
  These four are mutually non-overlapping (disjoint files; D4-references-D3 and is sequenced within
  the wave by the per-report integrator's serial apply-order D3-before-D4, but they do not edit the
  same region — marked parallel-dispatch, the integrator applies D3's report before D4's so the
  cross-link resolves). The shared FE-space + mesh substrate is lifted once across D3/D4/D5.

- **Wave 2 (after D1's report lands):**
  - **D2** `boundary-mode` promotion off `seed` — forward-references D1's live `waveguide-mode.*`
    column + defers its `feature/index.md` index-line edit to D1. Sequenced after D1 so the per-report
    integrator wires the boundary-mode↔waveguide-mode cross-link to a live target.

Per-report integrator apply-order (serial, all reports): D1 → D3 → D4 → D5 → D2 (D1 first so the
feature index exists for D2's deferred row; D3 before D4 so `Mesh` exists for D4's reference; D2 last
so waveguide-mode exists for its cross-link). Then ONE `integrator-finalize`.

## Open questions / caveats

- **`promotion_frontier` may shift after the all-fronts wave.** The standing-gate note (priorities.md
  item-2, line 32) flags that opening the feature fronts may FIRE some RE6-RE8 baseline-exception
  promotion conditions (a waveguide-mode/boundary-mode column genuinely CONSUMING an absorbed L3
  iteration-view or an axpy-family combinator could rescue a STRONGER-GARBAGE-SIGNAL node from
  detritus). I did NOT re-derive the post-wave reachability delta (the producers' actual `edges:`
  determine it). **Flag for the batch-37 meta-phase (fires after this finalize): re-check the RE1-RE8
  set against the new edges the all-fronts wave lands** — some baseline-exceptions may auto-discharge.
- **D5 de-Rham interpolator maturity is a producer judgment call.** I scoped it as likely `rough-in`
  (firm discrete-interpolator structure + obstruction-documented GSLIB point-interp leaf). If the
  harvester finds the discrete ND→RT interpolator fully positive-anchored and the GSLIB path is not
  load-bearing for the de-Rham relation, it may land `firm` on the discrete piece with the GSLIB leaf
  noted. Either is in-discipline; not forcing a firm claim.
- **D3 operator-slug choice (`build_mesh` vs `mesh`).** I recommended `L1/build_mesh.md` with `Mesh`
  as the produced record (matching the `lifecycle.L1` forward-ref `build_mesh :: Config -> Mesh`), but
  left the final slug to the harvester. D4 references the `Mesh` record regardless of the file slug —
  the coordination is "D4 cross-links the `Mesh` record D3 defines," slug-independent.
- **5 dispatches, well within the ≤12 cap.** This is one WIDE fan-out (the directive-B intent) but
  bounded — `essential_dofs` already-firm collapsed front (iii) to two ops, and the five fronts map
  cleanly to five dispatches. No filler; no rectangular vocabulary pull-up (the redirect still governs
  vocabulary — these are user-fired FEATURE demand-gates).
- **No mutation of `book/` in this phase** (planning only). priorities.md item-2 marked DISPATCHED.
