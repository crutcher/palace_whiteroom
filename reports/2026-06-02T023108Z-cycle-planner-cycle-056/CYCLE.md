---
agent: cycle-planner
invoked_at: 2026-06-02T023108Z
scope: cycle-056 dispatch plan
status: pending
---

# Cycle 056 dispatch plan

## Goals selected this cycle

Cycle-056 is the SECOND primary cycle of meta-batch-17 (cycles 055/056/057; the batch-17 meta-phase fires after cycle-057's finalize). It is a **light, observation-first / hygiene cycle** under the 2026-06-01 VOCABULARY-SHIFT REDIRECT. The batch-17 lead landed cleanly cycle-055 (`solve_family` full L4 entry + firm L4>L3 dissolution + all 3 FE-assembly ops firm); the c056 candidates are the **deferred / held** items from the cycle-055 hand-off — and on inspection they are nearly all **probes (findings) and audits (confirm-clean), not landings**. Three dispatches:

1. The **`map_solve` superset probe** (HIGH-but-GUARDED) — observation-first, fold-vs-map guarded. The pre-dispatch codemap evidence (pasted below) makes the shape-classification finding near-determined: **driven is an operator-varying `map`** (`SetOperators` inside the per-ω loop), **transient is a stateful `fold`/`solve_loop`** (state threaded step→step via `time_op.Step`). The probe's value is confirming this classification and recording that the general `map_solve` superset is **NOT authorable this cycle** (only 1 operator-varying witness — driven; transient does NOT join the family). This is a spine finding, not a forced land.
2. The **L3-L2 / L2-L1 index-table-staleness sweep** (hygiene) — observation-first audit per D8's cycle-055 root-cause OQ. My pre-dispatch check (pasted below) shows the L3-L2 and L2-L1 index-table status cells are **already consistent** with their theme-file `## Status` lines — so this dispatch most likely returns a **confirm-clean negative finding** (the L4-L3 drift did NOT propagate to the mass-edited c050/c051 tables). Worth doing for count-integrity assurance; if a divergence IS found, it routes to a c057 lifter (do NOT fix mid-audit).
3. The **`fe_assemble.md:147` citation residual** (lifter) — a clean small mechanical fix (`:215-217`→`:216-217`), codemap-confirmed. The hand-off said "1 place"; there are actually **2 occurrences** (`:147` + `:257`) — both fixed.

The `gram-consuming-solver-postprocess-reduction` (active head #4) stays **DEFERRED** — re-assessed below against the clean-describability bar; it still reads as too solver-specific to lift as shared spine vocabulary. The `L3/solve_family` image + L3>L2 hop and the `solve_family` specialization-chapter split both stay **sequenced to c057** (the LAST cycle before the batch-17 meta-phase) — the specialization split is gated on the c055 §Specializations-as-notes proving insufficient (it has not), and the L3 image is a small forward-frontier landing that does not compete with this cycle's findings/hygiene.

## Dispatches

### D1 — `cross-layer-cross-cutter` — `map-solve-superset-probe` (observation-only; fold-vs-map GUARDED)
- **scope:** Probe the general `map_solve_over_(operator,rhs)_family` superset against the **driven** and **transient** pipelines to classify each pipeline's solve-sweep shape as `map` (operator-varying, per-element independent) vs `fold`/`solve_loop` (state-threaded). **Cite the promoted `skills/disciplined-cross-pipeline-combinator-mining-gate` skill** (single-witness → 2nd-pipeline-probe → discharge → mine, with the fold-vs-map over-unification check). **OBSERVATION-ONLY — no `book/` mutation.** Deliverable = the shape-classification finding + an OQ disposition: confirm/refute that (a) **driven** is the operator-varying `map` superset witness (`drivensolver.cpp:170-198`: `A = space_op.GetSystemMatrix(...)` + `P = space_op.GetPreconditionerMatrix(...)` rebuilt per-ω INSIDE the `for (omega_i ...)` loop at `:170`, then `ksp.SetOperators(*A, *P)` at `:180`, then `ksp.Mult(RHS, E)` at `:196` — the operator-capture hoist that licenses `solve_family` is ABSENT; each ω-solve is independent of the prior, so the per-element structure IS a map, but the operator varies); and (b) **transient** is a **stateful `fold`/`solve_loop`, NOT a `map`** (`transientsolver.cpp:77-93`: `for (int step = 0; step < n_step; step++)` with `time_op.Step(t, delta_t)` at `:93` advancing `t` and the E/B field state INTERNALLY — comment `:83` "Single time step t -> t + dt"; `:85-89` `step == 0 → time_op.Init()` initial-conditions then subsequent steps advance from prior state — state is threaded step→step, so folding it into the `map` family over-unifies). **The load-bearing conclusion (state it explicitly):** the general superset has **at most ONE operator-varying `map` witness (driven)**; transient is a fold and does NOT join the `map_solve` family. Per the redirect + the mining-gate skill, the superset combinator is **NOT authorable from a single witness** — do NOT author `book/src/L4/map_solve.md`. Record (i) the driven map-superset shape + its single-witness status; (ii) the transient fold shape as a DISTINCT future combinator (`fold_solve`/`solve_loop`-family, NOT this family); (iii) whether eigenmode is worth a future probe. Pre-localized anchors are embedded above so the producer reads the cited lines and proceeds to classification (no localization loop needed).
- **deps:** none.
- **rationale:** Active-head #3 (was HELD-c055 → SEQUENCED to c056). Serves OQ `solve-family-general-operator-rhs-superset-probe` + `solve-family-transient-fold-vs-map-over-unification-guard` (both from c054/c055). The redirect's item-3 (solvers as test-load): the un-`map`-able transient surface is a FINDING about the spine, not forced into the map family. fan-out HIGH (the superset would serve driven/transient/eigenmode) — **gated** by the fold-vs-map check, which the pre-evidence shows blocks authoring this cycle.

### D2 — `cross-layer-cross-cutter` — `l3-l2-l2-l1-index-table-staleness-sweep` (observation-only audit)
- **scope:** Audit the **L3-L2** and **L2-L1** index tables (`book/src/L3-L2/index.md`, `book/src/L2-L1/index.md`) for the status-cell-drift class D8 found in the L4-L3 table cycle-055 (`index-table-status-cell-drifts-when-theme-file-promoted`). For each theme row in each index table, compare the table's status cell against the linked theme-file's authoritative `## Status` line. **OBSERVATION-ONLY — no `book/` mutation.** Deliverable = a divergence table (theme slug | table cell | theme-file `## Status` | divergent?) + a verdict. **Expected outcome (pre-checked, see Deliverable-presence evidence below): CONFIRM-CLEAN** — the planner's pre-dispatch comparison found all 5 L3-L2 cells (`firm`) and all 11 L2-L1 cells (`firm` ×10 + `partly-constructive` ×1) already consistent with their theme files. The valuable finding is the **negative result**: the L4-L3 drift did NOT propagate to the c050/c051 mass-edited L3-L2/L2-L1 tables (count-integrity is sound). If — contrary to the pre-check — a divergence IS found, record it as a c057 lifter follow-up OQ; do **NOT** fix it mid-audit (a producer must not edit another artifact in-place). The root-cause tooling fix (finalize-time / promotion-time index-consistency check) is already routed to the batch-17 meta-phase (D8's OQ) — this dispatch is the one-time residue sweep, not the systemic fix.
- **deps:** none.
- **rationale:** Cycle-055 hand-off + integrator-signals "Suggested next dispatches" (the L3-L2/L2-L1 staleness sweep). Count-integrity depends on table↔theme-file agreement, and cycle-055 showed it can drift undetected for batches. fan-out LOW (hygiene/assurance; one audit).

### D3 — `lifter` — `fe-assemble-147-citation-residual` (clean small mechanical fix)
- **scope:** Fix the `palace/models/laplaceoperator.cpp:215-217` → `:216-217` citation drift in `book/src/L1/fe_assemble.md`. Codemap-confirmed on-disk: `SetEssentialTrueDofs` is at `laplaceoperator.cpp:217`; the `K_l = std::make_unique<ParOperator>(...)` construction it operates on is at `:216`; `:215` is a stray `Mpi::Print("\n")` (NOT part of the essential-BC elimination), so the current `:215-217` over-spans by one line. **Two occurrences** (the hand-off said "1 place" — re-grep confirms 2): `book/src/L1/fe_assemble.md:147` (`... laplaceoperator.cpp:215-217`) and `:257` (`wrap with SetEssentialTrueDofs (:215-217, the separable eliminate_essential_bc post-comp)`). Both refer to the same essential-BC elimination construct-then-SetEssentialTrueDofs pair → both → `:216-217`. **Belt-and-suspenders re-grep at fix time** (confirm exactly 2 occurrences before editing; if a third surfaced since this plan, fix it too). No body/semantics edits — pure citation-range correction. Leave the unrelated `:253` `laplaceoperator.cpp:184-223` (`GetStiffnessMatrix` full-method span) and `:129` `:191-192` UNTOUCHED — those are correct.
- **deps:** none (touches only `book/src/L1/fe_assemble.md`; no other dispatch touches this file).
- **rationale:** Cycle-055 hand-off + integrator-signals (`fe-assemble-laplaceoperator-citation-drift-215-vs-216`, integrator-confirmed needs-more — "a future lifter fixes :215-217→:216-217"). A clean small lifter fix; the smallest piece of FE-assembly-thread hygiene debt. fan-out LOW (citation hygiene on the freshly-firm FE-assembly cohort).

## Overlap analysis

Three dispatches, pairwise:

- **D1 × D2:** Both are `cross-layer-cross-cutter` observation-only dispatches, but they touch **disjoint subject matter** (D1 = L4/driven/transient solve-sweep shape classification, reads L0 source + `L4/solve_family.md` for context; D2 = L3-L2/L2-L1 index-table vs theme-file status comparison). Neither mutates `book/`. **NOT overlapping → PARALLEL.**
- **D1 × D3:** D1 is observation-only (no `book/` write); D3 edits only `book/src/L1/fe_assemble.md` (a file D1 does not touch — D1's reads are L4 + L0). **NOT overlapping → PARALLEL.**
- **D2 × D3:** D2 is observation-only (no `book/` write; reads `L3-L2/index.md` + `L2-L1/index.md` + theme files); D3 edits only `book/src/L1/fe_assemble.md`. Disjoint file sets. **NOT overlapping → PARALLEL.**

No two dispatches modify the same operator entry, rewrite the same theme body, or name operators the other proposes. No shared running-count / consolidated-tally index is written by ≥2 dispatches (D2 is observation-only; D3 touches no index; D1 touches no `book/`) — so the count-ownership / dual-registration partition does NOT apply this cycle. No cross-report forward-reference (no dispatch references another's not-yet-landed slug — D1 explicitly does NOT author `map_solve.md`; D2/D3 author nothing new). **All three are fully PARALLEL — one wave.**

## Sequencing schedule

**Wave 1 (parallel — all three):** D1, D2, D3.

Single wave. No forward-reference ordering needed (no dispatch produces a slug another references; D1 produces no new file by design). The standard pipeline follows: 3 critics (parallel) → repairers as needed → `integrator-per-report` ×3 (serial) → ONE `integrator-finalize`.

**Sequenced to cycle-057** (the LAST primary cycle before the batch-17 meta-phase — NOT dispatched this cycle):
- `L3/solve_family` image + L3>L2 hop — the firm L3 image named as the dissolution target by the c055 D1/D2 landings (the explicit `std::vector<Vector>`-accumulating outer sweep). `harvester` (L3 image) + `abstractor` (L3>L2 hop). A small forward-frontier landing; does not compete with this cycle's findings/hygiene. Open-by-construction next cycle (verify-absent at c057 dispatch).
- `solve_family` specialization-chapter split — ONLY IF the c055 §Specializations-as-notes-in-entry proves insufficient (size-judgment; default is notes-in-entry per combinator-as-entry; no trigger has fired).
- Any divergence found by D2 → a c057 lifter fix (contingent on D2's verdict; the pre-check predicts none).
- `fe-operator-assemble-mutation-rotation` theme firm-flip + `eliminate_*` elimination-leg theme-side re-anchors — gated on the legs + the (now-themed) libCEED boundary; a c057+ lifter (carries from c055 D6's OQs).

## Deliverable-presence verification

Per the MANDATORY paste-inline-evidence requirement. D1 and D2 are observation-only dispatches (no named-artifact-slug deliverable to author — open by construction as observation/audit); D3 is a citation-fix on an existing firm file. None recruits a stale already-landed deliverable. Evidence pasted below.

**D1 — `map-solve-superset-probe` (observation-only; the GUARD against authoring `map_solve.md`):**
- Step 1 (existence — confirm the superset is NOT already authored): `ls book/src/L4/map_solve.md book/src/L4/fold_solve.md book/src/L4/solve_loop.md` →
  ```
  ls: cannot access 'book/src/L4/map_solve.md': No such file or directory
  ls: cannot access 'book/src/L4/fold_solve.md': No such file or directory
  ls: cannot access 'book/src/L4/solve_loop.md': No such file or directory
  ```
  All ABSENT — correct (D1 is observation-only and does NOT author them; the probe's verdict is that they are NOT authorable this cycle). **OPEN by construction (observation-first probe; the redirect + mining-gate skill GATE authoring).**
- Step 2 (the existing `solve_family` entry already documents the scope boundary — confirms the probe is the right framing, not a re-derivation): `book/src/L4/solve_family.md:146` reads (pasted): *"`solve_family` (fixed-operator) is witnessed by electrostatic + magnetostatic ONLY (2-of-5 pipelines) ... The general superset is batch-17 future work (OQ `solve-family-general-operator-rhs-superset-probe`), gated on a 3rd probe (... check whether transient is a `map` or a stateful `fold`/`solve_loop` shape — a fold does NOT join this family)."* The c055 entry explicitly names this probe as the next step — D1 is the gated 3rd-probe, NOT a re-author.
- Codemap evidence (driven = operator-varying map; pre-localized for the dispatch scope): `drivensolver.cpp:170` `for (std::size_t omega_i ...)`, `:174-180` `A = space_op.GetSystemMatrix(...)` / `P = space_op.GetPreconditionerMatrix(...)` / `ksp.SetOperators(*A, *P)` INSIDE the loop, `:196` `ksp.Mult(RHS, E)`. (Read via `mcp__palace-codemap__read_range palace/drivers/drivensolver.cpp:168-200`.)
- Codemap evidence (transient = stateful fold; pre-localized): `transientsolver.cpp:77` `for (int step = 0; step < n_step; step++)`, `:83` comment "Single time step t -> t + dt", `:85-89` `step == 0 → time_op.Init()`, `:93` `time_op.Step(t, delta_t)` (advances t + field state internally). (Read via `mcp__palace-codemap__search_text` on `transientsolver.cpp`.)
- Step 4 (structural-block check): NONE — the probe is gated-but-tractable (the gate is on AUTHORING the combinator, not on running the probe; the probe is the gate-discharge attempt). Not on the STOP-PROPOSING NEGATIVE LIST.

**D2 — `l3-l2-l2-l1-index-table-staleness-sweep` (observation-only audit):**
- Step 1 (existence — both index tables present): `ls book/src/L3-L2/index.md book/src/L2-L1/index.md` → both present (the two tables to audit).
- Step 2 (the planner's pre-comparison — the audit's expected CONFIRM-CLEAN verdict): L3-L2 theme-file `## Status` lines vs index-table cells (lines 13-17 of `L3-L2/index.md`):
  ```
  krylov-step-body-identity        theme: firm   | table cell (:13): firm   -> AGREE
  ksp-solve-outer-driver           theme: firm   | table cell (:14): firm   -> AGREE
  orthogonalize-variant-split      theme: firm   | table cell (:15): firm   -> AGREE
  eigsolve-opaque-eigen-iteration  theme: firm   | table cell (:16): firm   -> AGREE
  chebyshev-nested-recurrence      theme: firm   | table cell (:17): firm   -> AGREE
  ```
  L2-L1 theme-file `## Status` lines vs index-table cells (lines 13-23 of `L2-L1/index.md`):
  ```
  chebyshev-iteration-fusion                      theme: firm                | table (:13): firm                -> AGREE
  linear-combination-fold-specialization          theme: firm                | table (:14): firm                -> AGREE
  inner-product-fold-specialization               theme: firm                | table (:15): firm                -> AGREE
  orthogonalize-composition-lowering              theme: firm                | table (:16): firm                -> AGREE
  gram-fold-specialization                        theme: firm                | table (:17): firm                -> AGREE
  deflate-composition-lowering                    theme: partly-constructive | table (:18): partly-constructive -> AGREE
  eigsolve-spectral-transform-composition         theme: firm                | table (:19): firm                -> AGREE
  divfree-projector-leaf-identity                 theme: firm                | table (:20): firm                -> AGREE
  incremental-least-squares-composition-lowering  theme: firm                | table (:21): firm                -> AGREE
  ksp-solve-outer-driver-unfold                   theme: firm                | table (:22): firm                -> AGREE
  krylov-step-kernel-defusion                     theme: firm                | table (:23): firm                -> AGREE
  ```
  All 16 rows AGREE → the dispatch's expected verdict is **CONFIRM-CLEAN** (a negative finding: no drift). **OPEN by construction (audit; no deliverable already discharged — the audit-block evidence is fresh).** The dispatch is still worth running so the verdict is produced by an independent role (the planner's pre-check is the deliverable-presence gate, not the audit itself).
- Step 4 (structural-block check): NONE. Not on the STOP-PROPOSING list.

**D3 — `fe-assemble-147-citation-residual` (citation-fix on an existing firm file):**
- Step 1 (existence): `ls book/src/L1/fe_assemble.md` → present (firm, c054).
- Step 2 (the drift is present + not already fixed): `grep -n '215-217' book/src/L1/fe_assemble.md` →
  ```
  147:  `palace/models/laplaceoperator.cpp:215-217`) and lifting inhomogeneous Dirichlet data into the RHS
  257:  wrap with `SetEssentialTrueDofs` (`:215-217`, the separable `eliminate_essential_bc` post-comp).
  ```
  2 occurrences still carry the `:215-217` drift (NOT yet fixed). The hand-off said "1 place"; the re-grep shows **2** — D3 fixes both.
- Codemap evidence (the correct range): `mcp__palace-codemap__search_text SetEssentialTrueDofs palace/models/laplaceoperator.cpp` → `{"line":217,"snippet":"K_l->SetEssentialTrueDofs(dbc_tdof_lists[l], ...)"}`; `read_range :213-219` shows `:216` = `auto K_l = std::make_unique<ParOperator>(...)` (the construct), `:217` = `SetEssentialTrueDofs`, `:215` = `Mpi::Print("\n")` (stray, NOT part of the elimination). So `:216-217` is correct; `:215-217` over-spans by one. **OPEN (the drift is on-disk, un-fixed).**
- Step 4 (structural-block check): NONE — pure mechanical citation correction, no maturity gate. Not on the STOP-PROPOSING list.

**`gram-consuming-solver-postprocess-reduction` (active head #4) — re-assessed, stays DEFERRED (NOT recruited):**
- `ls book/src/L2/*capacitance* book/src/L2/*terminal*` → no such files (only `book/src/L2/gram.md` present). The candidate would be a NEW `terminal-reduction`/`capacitance-matrix` L2 consumer entry. **Clean-describability re-assessment:** the surface is the `/Vᵢ²`+`/(IᵢIⱼ)` scaling (`electrostaticsolver.cpp:114` / `magnetostaticsolver.cpp:126,138`), the `Cm`/`Mm` sign-remix (`:127-129`/`:139-141`), and the in-place `Invert()` (`:138-139`/`:151-152`). This is pipeline-specific post-processing arithmetic on a built `gram` — it does NOT generalize as shared spine vocabulary across the 5 pipelines (it is the capacitance/inductance-matrix extraction, present only in electrostatic/magnetostatic, and even there is bespoke sign/scaling bookkeeping). Per the redirect ("solvers advance the spine only when cleanly describable; what a solver can't cleanly say is a spine finding"), this stays DEFERRED — the finding is that the terminal-reduction post-processing is genuinely solver-specific arithmetic, not a shared combinator. Re-assess at the batch-17 meta-phase only if a 3rd pipeline exhibits a structurally-matching reduction (none does). **NOT recruited this cycle.**

## Producer notes (carry into the dispatch briefs)

- **Tool-tag-leak guard (NOTE for any file-authoring producer):** cycle-055 D4 (`eliminate_essential_bc.md`) shipped with 2 leaked tool-invocation closing tags (`</content></invoke>`) at its tail — a Write artifact the per-report critic/repairer missed, caught only at finalize as a markdown WARN. **This cycle authors NO new chapter files** (D1 = observation-only; D2 = observation-only; D3 = in-place citation edit on an existing file) — so the leak risk is low — but if D3's lifter touches body text, it must NOT leak any tool-call closing tags into the file body. The general reminder stands for c057's `L3/solve_family` harvester: do NOT leak tool-invocation XML into new-file bodies.
- **D1 + D2 are observation-only — propose NO `book/` changes.** D1's deliverable is a shape-classification finding + OQ disposition (and the explicit "do NOT author `map_solve.md` from a single witness" verdict). D2's deliverable is a divergence table + CONFIRM-CLEAN (or, if surprising, a c057-routed lifter OQ). Neither edits another artifact in-place.
- **D3 is the only `book/`-mutating dispatch** — bounded to 2 citation-range string replacements in one file.

## Open questions / caveats

- **The map_solve probe verdict is near-determined by the pre-evidence — confirm I have not pre-empted the dispatch's judgment.** The codemap reads make driven=map / transient=fold strongly evident, but D1 should still independently verify (the producer may find, e.g., that transient's `time_op.Step` is internally a per-step independent solve despite the threaded `t` — unlikely given the field-state advance, but the producer decides). The plan does NOT pre-author the verdict into the artifact; D1 owns the finding. If D1 finds transient is unexpectedly map-able, the superset is at 2 witnesses (driven + transient) and authoring becomes a c057 candidate — flag for the c057 planner.
- **Light cycle (3 dispatches, 2 observation-only).** This is correct for the batch-17 state: the lead landed c055, and the remaining batch-17 items are findings/hygiene + the small c057-sequenced `L3/solve_family` image. Cycle-057 (the LAST before the batch-17 meta-phase) carries the `L3/solve_family` image + L3>L2 hop as its forward-frontier landing, plus any D2-found divergence and the `fe-operator-assemble-mutation-rotation` theme firm-flip. The batch-17 meta-phase (after c057) should: (a) ratify the driven-map-superset single-witness status + the transient-fold-distinct-family finding (D1); (b) enact the root-cause index-table-consistency tooling fix (D8's c055 OQ — finalize-time or promotion-time check) regardless of D2's confirm-clean (the residue sweep being clean does not remove the systemic drift risk); (c) close the `gram-consuming-solver-postprocess-reduction` candidate as genuinely-solver-specific (or re-open if a 3rd pipeline match surfaces).
- **For the next meta-phase (pattern note, not yet in the friction-ledger):** the cycle-055 hand-off undercounted the `fe_assemble` citation residual ("1 place" vs the actual 2 occurrences `:147`+`:257`). Minor, repaired by the belt-and-suspenders re-grep convention — but it is a small instance of an integrator-confirmed-count being stale by the next cycle. If this recurs (hand-off occurrence-counts drifting), the batch-17 meta-phase may want a convention that hand-off citation-residual notes state the grep pattern rather than a hardcoded count, so the next planner re-greps rather than trusts the number. Noting here per the cadence guidance (the friction-ledger entry is not there yet).
