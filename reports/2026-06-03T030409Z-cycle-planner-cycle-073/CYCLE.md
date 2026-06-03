---
agent: cycle-planner
invoked_at: 2026-06-03T030409Z
scope: cycle-073 dispatch plan
status: pending
---

# Cycle 073 dispatch plan

**FIRST primary cycle of meta-batch-23** (cycles 073/074/075; the batch-23 meta-phase fires AFTER cycle-075's finalize). Session was restarted post-batch-22 (the FEATURE-SURFACE SPINE role-spec codification + CLAUDE.md edits are loaded; commit `387fa56`).

## Goals selected this cycle

Push the batch-23 frontier on its two co-equal tracks per the cycle-073 active head: **(1) the LEAD — mine the shared L4 `gram_reduce`/`energy_reduce` combinator** (the ≥2-witness gate is MET; the electrostatic capacitance `Vⱼᵀ K Vᵢ` and magnetostatic inductance `(Aⱼᵀ K Aᵢ)/(IᵢIⱼ)` reductions are the SAME operator-weighted Gram map-then-reduce, differing only in the normalization weight), authored as a combinator-as-entry and **replace-and-propagated** into both feature L4 chapters' down-links per the redirect; **(2) the PARALLEL standing goal — scale the FEATURE-SURFACE SPINE** with the next-highest-fan-out driver columns (eigenmode + driven + transient), each composing only firm L4 vocabulary (clean-gated). Plus two LOW hygiene riders: the `solve_family` §Specializations anchor re-anchor + `L4-L3/index` bare-basename lint (item-3), and the AMR-loop 2nd-witness fold-in for `fold_solve` (item-4, rides alongside the spine work since the lifecycle ROOT references the AMR loop). The shared `energy_reduce` mine (item-1) gates the OUTPUT-PRODUCT feature columns (capacitance/inductance ride the mined combinator), so those are NOT recruited this cycle — they sequence to c074 once item-1 lands; this cycle's spine scaling is the 3 DRIVER columns, which compose firm solve/assemble vocabulary independently of the mine.

## Deliverable-presence verification

Per the MANDATORY paste-inline-evidence pre-dispatch check (CLAUDE.md §Discipline; skill `verify-dispatch-scope-not-already-discharged`). All `ls`/`grep`/codemap outputs below are literal pasted command results from this planning session.

### D1 — `gram_reduce`/`energy_reduce` L4 combinator (item-1 lead) — VERIFIED ABSENT
1. **File existence** (`ls book/src/L4/{energy_reduce,gram_reduce}.md`):
   ```
   ls: cannot access 'book/src/L4/energy_reduce.md': No such file or directory
   ls: cannot access 'book/src/L4/gram_reduce.md': No such file or directory
   ```
   Both candidate slugs ABSENT.
2. **L4/index dep-map** (`grep -ni 'energy_reduce|gram_reduce|capacitance_reduce|inductance_reduce' book/src/L4/index.md`): no matches — no rough-in row yet (open by construction).
3. **2-witness gate MET (on-disk evidence)** — both feature L4 chapters carry the reduction as a `map`-then-`reduce` over the SAME primitives:
   - `book/src/feature/electrostatic.L4.md:40` — "`Cᵢⱼ = Vⱼᵀ K Vᵢ` ... a `map`-then-`reduce` over the solution-family pairs using the operator-weighted-bilinear primitives (the rough-in L1 `matrix-weighted-norm` `Vᵢᵀ K Vᵢ` on the diagonal, the rough-in L1 `bilinear-form` `Vⱼᵀ K Vᵢ` off-diagonal) ... its dedicated L4 reduction-combinator ... is a forward mine, not authored here (see Open questions)."
   - `book/src/feature/magnetostatic.L4.md:40` — "`Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` ... a `map`-then-`reduce` over the solution-family pairs using the operator-weighted-bilinear primitives — the rough-in L1 `matrix-weighted-norm` `Aᵢᵀ K Aᵢ` on the diagonal, the rough-in L1 `bilinear-form` `Aⱼᵀ K Aᵢ` off-diagonal — each divided by the current normalization `Iᵢ Iⱼ` ... if the cross-pipeline post-processing proves to share a shape with the electrostatic capacitance reduction (**it does, modulo the diagonal current-vs-voltage normalization weight**) — is a forward mine, not authored here."
   The two reductions are the same operator-weighted Gram fold parameterized by the normalization weight — gate MET.
4. **OQ provenance** — `shared-l4-energy-form-reduction-combinator-gram-reduce-two-witness-mine` (c072 D1, promoted in the cycle-072 finalize). OQ is OPEN (the mine candidate), not RESOLVED.
5. **Structural-block check** — none. The combinator rises regardless of its constituent primitives' maturity (directive `project_blackbox_vs_accelerated_kernels`: `linear_combination`/`inner_product`-class combinators must reach L4 regardless). NOTE: the folded primitives (`matrix-weighted-norm`, `bilinear-form`) are themselves `rough-in (test-coverage-bounded)` / `rough-in (lower-layer-shared-vocabulary)` (pasted below) — this does NOT block the combinator entry; the entry's own status is the combinator-fold structure (the harvester picks `rough-in`/`firm` per its warrant). Pasted maturity:
   ```
   matrix-weighted-norm: `rough-in (test-coverage-bounded)` — signature and algebraic laws well-anchored ... no dedicated Palace test ...
   bilinear-form: `rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)` — the structural ...
   ```

### D2/D3/D4 — eigenmode / driven / transient driver feature columns (item-2) — VERIFIED ABSENT, constituents FIRM
1. **File existence** (`ls book/src/feature/{eigenmode,driven,transient}.L4.md`):
   ```
   ls: cannot access 'book/src/feature/eigenmode.L4.md': No such file or directory
   ls: cannot access 'book/src/feature/driven.L4.md': No such file or directory
   ls: cannot access 'book/src/feature/transient.L4.md': No such file or directory
   ```
   All 3 driver columns ABSENT at L4 (and by extension L1/L0). Existing feature dir: `electrostatic.{L4,L1,L0}`, `lifecycle.{L4,L1,L0}`, `magnetostatic.{L4,L1,L0}`, `index.md`.
2. **Constituents FIRM on disk** (the clean-gate — verify-present per the feature-column landing discipline):
   ```
   book/src/L4/frequency_sweep.md            : ## Status   (firm, c070)   — driven solve-half
   book/src/L4/assemble_frequency_operator.md: ## Status   (firm, c069)   — driven per-ω operand
   book/src/L4/fold_solve.md                 : ## Status   (firm, c058)   — transient state-fold
   book/src/L4/eigsolve.md                   : ## Status   (firm)         — eigenmode opaque solve
   book/src/L1/fe_assemble.md                : present (firm)             — shared assemble half
   ```
   Driven composes firm `frequency_sweep` + `assemble_frequency_operator`; transient composes firm `fold_solve`; eigenmode composes firm `eigsolve`. All clean-gated.
3. **Source driver entry points** (codemap `search_text '::Solve('` + `SetOperators|eigen->Solve|time_op.Step`):
   ```
   drivensolver.cpp:37   DrivenSolver::Solve       ; ksp.SetOperators(*A,*P) INSIDE loop @ :180 (frequency_sweep witness)
   transientsolver.cpp:26 TransientSolver::Solve   ; time_op.Step(t,delta_t) @ :93 (fold_solve witness)
   eigensolver.cpp:33    EigenSolver::Solve        ; eigen->Solve() opaque @ :367 (eigsolve cap)
   ```
   All entry points + composed-op witness sites codemap-confirmed (on-disk-confirm at dispatch per the close-brace discipline).
5. **Structural-block check** — none. Open by construction (no prior-cycle history; the spine is at 3 columns, these are the next 3). Feature-surface kind is now codified into `layer-intro-author` (batch-22) — the per-dispatch prompt no longer carries the convention; the role-spec does.

### D5 — `solve_family` §Specializations re-anchor + `L4-L3/index` lint (item-3 hygiene) — VERIFIED PRESENT (re-anchor target), DRIFT-STATE AMBIGUOUS
1. **File existence** — `book/src/L4/solve_family.md` PRESENT (firm-spine entry); `book/src/L4-L3/index.md` PRESENT.
2. **On-disk §Specializations note** (`book/src/L4/solve_family.md:107`/`:109`) cites electrostatic `:30`/`:35`/`:36` and magnetostatic `:35`/`:36`/`:66`.
3. **Codemap drift check — the priorities item-3 ASSERTION may itself be drifted.** Priorities item-3 says the note cites `:30/:35/:36` for "sites on-disk at `:29/:34/:35`" (a claimed +1 drift). But codemap `read_range electrostaticsolver.cpp:28-37` shows:
   ```
   28 BlockTimer bt0(...)
   29 LaplaceOperator laplace_op(...)
   30 auto K = laplace_op.GetStiffnessMatrix();     <- ":30" CORRECT
   ...
   35 KspSolver ksp(...);                           <- ":35" CORRECT
   36 ksp.SetOperators(*K, *K);                     <- ":36" CORRECT
   ```
   The on-disk `:30/:35/:36` cites are CORRECT, not +1-drifted — the priorities item-3 assertion is itself the codemap-drift class (`codemap-read-range-plus-one-drift-on-brace-boundary`, recurrence 6). **D5 must on-disk-Read-confirm each anchor before changing anything** (hand-Read, NOT `citecheck --anchor`, which is blind to this class). The lint half (`L4-L3/index.md:15` `integrator.hpp:58-61` bare-basename) is confirmed present and is a genuine no-source-line lint. D5's scope is "confirm-then-fix-only-if-actually-drifted" — likely a no-op on the electrostatic anchors + the magnetostatic check + the lint qualification.

### D6 — AMR-loop 2nd `fold_solve` witness fold-in (item-4) — VERIFIED PRESENT (targets), OPEN (fold-in)
1. **Source** (codemap) — `basesolver.cpp:153 BaseSolver::SolveEstimateMarkRefine` (the AMR `while` loop) confirmed. The lifecycle ROOT feature column (`feature/lifecycle.{L4,L1,L0}.md`) is on disk (c072) and references the AMR loop — D6 rides alongside the spine work.
2. **Target** — `book/src/L4/fold_solve.md` `schedule-source` variant axis (currently 1 state-generated witness: SweepAdaptive). Fold-in raises it to 2 (AMR + SweepAdaptive).
3. **OQ provenance** — `fold-solve-state-generated-schedule-source-second-witness-amr-loop` (c072 D2, OPEN). Not RESOLVED.
5. **Structural-block check** — none; observation-routed lifter fold-in (in-place variant-axis row + witness count). LOW.

### NOT recruited this cycle (sequenced / gated; paste-evidence rationale)
- **OUTPUT-PRODUCT feature columns (capacitance / inductance / S-params / eigenfreq+Q / energy-fields)** — SEQUENCED to c074. Capacitance/inductance ride the item-1 mined `gram_reduce`; authoring them this cycle would forward-reference a combinator that lands the same cycle (a cross-report forward-reference). Cleaner to land the combinator (D1) first, then the output-product columns down-link to a firm L4 reduction. S-params/eigenfreq+Q have their own additional constituents (driven/eigenmode postprocess) not all firm. Recruit c074.
- **wave-port / boundary-mode column** — DEFERRED. `boundarymodesolver.cpp:201 BoundaryModeSolver::Solve` confirmed present; it is a co-equal leaf column, but lower fan-out than the 3 main driver columns and carries the unresolved "6th ProblemType branch vs 5-drivers framing" OQ (`boundarymode-is-sixth-problemtype-branch-reconcile-five-drivers-framing`, c072 D2) that the batch-23 meta-phase should settle first. Recruit post-meta or c074/c075.
- **STOP-PROPOSING negative list** (batch-23, carried): `lu_solve`, `back_solve`, `ls-update-column`, 4 NLEPS atoms, `apply_nonlinear_pencil` (HELD), `polynomial_smoother` gap (CLOSED-RETIRED), the combinator-complete BLAS/projector/smoother surface (do NOT re-scan), NO `L3/solve_family` backfill, NO `L2/fold_solve` floor, NO `L2/fe_assemble` floor, NO `weak_form_term` L2 floor, NO shared generalized `map_solve` from the single driven witness. No dispatch below matches any disqualified slug (verified).

## Dispatches

**D1 — `combinator-miner` — item-1, THE LEAD, HIGH.**
- **scope**: Mine the shared L4 reduction combinator (canonical slug `gram_reduce`; the harvester/miner picks `gram_reduce` vs `energy_reduce` warrant-first — `gram_reduce` is the more general operator-weighted-Gram name, `energy_reduce` the physics framing). Author `book/src/L4/gram_reduce.md` as a **combinator-as-entry**: the operator-weighted Gram `map`-then-`reduce` over a solution family-pair grid, parameterized by the per-entry **normalization weight** `w(i,j)` (electrostatic `w=1` voltage-formulated; magnetostatic `w = 1/(Iᵢ Iⱼ)` current-normalized) — folding the L1 `matrix-weighted-norm` (diagonal `Vᵢᵀ K Vᵢ`) + `bilinear-form` (off-diagonal `Vⱼᵀ K Vᵢ`) over the grid. State the structural payoff: the symmetric-Gram reduction is ONE combinator across the two output products; the weight is the only difference. Cite the 2 witnesses (`feature/electrostatic.L4.md:40` capacitance, `feature/magnetostatic.L4.md:40` inductance) + the L0 postprocess sites (`electrostaticsolver.cpp:95/:100/:118-127/:139-140`; `magnetostaticsolver.cpp:108/:110/:129-138/:151-152` — on-disk-confirm at dispatch). Add the rough-in→firm dep-map row to `book/src/L4/index.md` in alpha position (D1 owns this row + its cohort bullet). **Cite `disciplined-cross-pipeline-combinator-mining-gate`** (2-of-N witness discharge; note the eigenmode Q-factor / S-param postprocess as potential 3rd+ witnesses — a stronger future mine, NOT authored now). Status: the harvester picks per warrant (likely `rough-in (test-coverage-bounded)` since the constituent bilinear primitives are rough-in + no dedicated test; firm-on-structure is defensible — record the choice). Pre-localize the postprocess sites are NOT on the known-heavy watch-list (driver postprocess, not iterative.cpp); standard localization fine.
- **deps**: none.
- **rationale**: active head #1; OQ `shared-l4-energy-form-reduction-combinator-gram-reduce-two-witness-mine`; redirect combinator-primary + replace-and-propagate. HIGH fan-out (both feature L4 chapters + the forthcoming output-product columns link DOWN to a firm reduction instead of two rough-in L1 primitives).

**D2 — `layer-intro-author` — item-2, the driven feature column, MEDIUM-HIGH.**
- **scope**: Author `book/src/feature/driven.{L4,L1,L0}.md` — the driven simulation feature composition-root (config → S-parameters / frequency response). L4 body = the composition of firm L4 vocabulary: `frequency_sweep` (the operator-VARYING per-ω solve, firm c070) ∘ `assemble_frequency_operator` (the per-ω affine operand `A(ω)=K+iωC−ω²M`, firm c069) ∘ `fe_assemble` (assemble the K/C/M bases once). Links DOWN to each. L0 ground truth = `drivensolver.cpp:37 DrivenSolver::Solve` (the per-ω loop `:170-198`, `ksp.SetOperators(*A,*P)` INSIDE the loop `:180` — the operator-varying witness; on-disk-confirm). Status `seed`. NOTE the postprocess (S-params) is the output-product surface — name it plain-text / forward-ref (its own output-product column lands c074); do NOT author the S-param reduction here. Composition-root kind per the codified `layer-intro-author` spec (inputs=config, output=physical product, body=composition, links DOWN; the adapted critic checks). **D2 owns its own `feature/index.md` matrix row + its `# Feature surfaces` SUMMARY rows** UNLESS ≥2 columns land — see overlap analysis (D2 is the SOLE index/SUMMARY owner for the 3 driver columns this cycle).
- **deps**: none (composes already-firm vocabulary). D2 is the index/SUMMARY count-owner for the driver-column cohort — D3/D4 defer their index/SUMMARY rows to D2.
- **rationale**: active head #2 (feature-spine scaling); highest-fan-out remaining driver column (driven is the richest pipeline, composes 2 firm solver-driven L4 forms). Clean-gated (constituents firm).

**D3 — `layer-intro-author` — item-2, the transient feature column, MEDIUM-HIGH.**
- **scope**: Author `book/src/feature/transient.{L4,L1,L0}.md` — the transient simulation feature composition-root (config → time-domain field evolution). L4 body = the composition: `fold_solve` (the state-threaded time-march FOLD, firm c058) ∘ `fe_assemble`. Links DOWN. L0 = `transientsolver.cpp:26 TransientSolver::Solve` (`time_op.Step(t,delta_t)` @ `:93`, the fold witness; persistent-state advance `timeoperator.cpp` `ode->Step` — on-disk-confirm). Status `seed`. Composition-root kind per the codified spec. **D3 DEFERS its `feature/index.md` matrix row + `# Feature surfaces` SUMMARY rows to D2** (the cohort index/SUMMARY owner) — D3 authors ONLY its 3 chapter files (`transient.{L4,L1,L0}.md`). Forward-references D2's driven column + the existing electrostatic/magnetostatic/lifecycle columns by canonical slug for any cross-driver "sibling driver" navigation (plain-text for the un-authored eigenmode if referenced).
- **deps**: D2 (for the index/SUMMARY owner partition — D3's deferred rows land via D2's owned block; the per-report integrator applies D2 before D3 so D2's block exists). Content authoring is independent.
- **rationale**: active head #2; transient is the FOLD pipeline column (the fold-sibling of the map drivers). Clean-gated.

**D4 — `layer-intro-author` — item-2, the eigenmode feature column, MEDIUM-HIGH.**
- **scope**: Author `book/src/feature/eigenmode.{L4,L1,L0}.md` — the eigenmode simulation feature composition-root (config → eigenfrequencies + Q-factors + mode fields). L4 body = the composition: `eigsolve` (the opaque black-box eigen-solve primitive, firm) ∘ `fe_assemble` (assemble K/C/M). Links DOWN. The eigenmode driver has NO operator/RHS family to map and NO state-fold (per `solve_family.md:146` it is NOT a `solve_family`/`fold_solve` witness — its only outer loop is a post-processing readout map over the converged eigenpair set). L0 = `eigensolver.cpp:33 EigenSolver::Solve` (`eigen->Solve()` opaque @ `:367`; the eigenpair readout `:425-471`; the per-mode `SetOperators` setup `:177-193` — on-disk-confirm). Status `seed`. The Q-factor / eigenfreq output product = forward-ref plain-text (its output-product column lands later). Composition-root kind per spec. **D4 DEFERS its `feature/index.md` matrix row + `# Feature surfaces` SUMMARY rows to D2.** Authors ONLY its 3 chapter files.
- **deps**: D2 (index/SUMMARY owner partition; same as D3).
- **rationale**: active head #2; eigenmode is the first column that composes ONLY a single opaque black-box solve + assemble (the cleanest test of the composition-root pattern over a black-box-kernel constituent, per directive `project_blackbox_vs_accelerated_kernels`). Clean-gated.

**D5 — `lifter` — item-3 hygiene, LOW.**
- **scope**: (a) **`solve_family` §Specializations re-anchor — CONFIRM-FIRST.** On-disk-Read each anchor in `book/src/L4/solve_family.md:107`/`:109` (electrostatic `:30/:35/:36`, magnetostatic) against the source via direct hand-`Read` (NOT `citecheck --anchor` — blind to this drift class). Per the planner's codemap check (pasted above), the electrostatic `:30/:35/:36` are CORRECT on disk — the priorities item-3 +1-drift assertion is itself the codemap-drift class. So D5's likely outcome is a NO-OP confirmation on the electrostatic anchors; fix ONLY anchors that on-disk-Read shows actually drifted. (b) **`L4-L3/index.md:15` lint** — qualify the bare-basename `integrator.hpp:58-61` to its full path (`palace/fem/libceed/integrator.hpp:58-61` — on-disk-confirm the path + line range; this is a path-hygiene lint, the source line is the libCEED-leaf boundary already recorded). Apply the close-brace on-disk-Read discipline to any END line touched.
- **deps**: none (D5 touches `solve_family.md` + `L4-L3/index.md`; D1 touches `L4/index.md` — different files, no overlap; see overlap analysis).
- **rationale**: active head #3; closes OQs `solve-family-md-specialization-note-plus-one-anchor-drift` + the bare-basename lint. LOW; rides alongside the frontier.

**D6 — `lifter` — item-4, AMR 2nd `fold_solve` witness fold-in, LOW.**
- **scope**: Fold the AMR `BaseSolver::SolveEstimateMarkRefine` `while` loop (`basesolver.cpp:153-276`, the `while` driving Solve→Estimate→Mark→Refine until convergence) into `book/src/L4/fold_solve.md` as the **2nd state-generated `fold_solve` witness** on the `schedule-source` variant axis (currently 1: SweepAdaptive's greedy/error-terminated phase). Add the witness to the variant-axis row + the witness inventory; the AMR loop is a state-generated-schedule fold (loop bound derived from the error-indicator state, NOT a fixed schedule) — confirming the `schedule-source` axis is multi-witness (strengthens, does not change, the `fold_solve` entry; NO new combinator). On-disk-confirm the `:153-276` range (close-brace discipline). NOTE the lifecycle ROOT feature column (`feature/lifecycle.{L4,L1,L0}.md`) references this AMR loop — D6 rides alongside the spine work as the active head #4 directs.
- **deps**: none (D6 touches `L4/fold_solve.md`; no other dispatch touches it).
- **rationale**: active head #4; OQ `fold-solve-state-generated-schedule-source-second-witness-amr-loop`; strengthens the `fold_solve` state-generated axis 1→2 witnesses + feeds the standing `fold-solve-greedy-schedule-source-generalization` dedicated-combinator question (batch-23 meta input). LOW; observation-routed.

## Overlap analysis

Pairwise artifact-region / shared-operator-name check (CLAUDE.md: same operator-entry-edit OR same theme-body-rewrite = overlapping → sequential; distinct rows / distinct files = parallel-safe).

- **D1 ↔ D2/D3/D4**: D1 authors `L4/gram_reduce.md` + a row in `L4/index.md`. D2/D3/D4 author NEW `feature/*.{L4,L1,L0}.md` files + (D2 only) `feature/index.md` + `SUMMARY.md` `# Feature surfaces` block. Disjoint files. The driver feature columns compose `frequency_sweep`/`fold_solve`/`eigsolve` (NOT the new `gram_reduce`) — they do NOT down-link the mined combinator (the output-product columns would; those are sequenced to c074). **NON-OVERLAPPING — parallel.** (If a driver column wishes to mention the reduction it cites the existing rough-in L1 primitives or forward-refs the output-product column, never the c073-landing `gram_reduce` — confirmed by the not-recruited rationale.)
- **D2 ↔ D3 ↔ D4**: each authors its OWN 3 chapter files (disjoint slugs). The ONLY shared surfaces are `feature/index.md` (the matrix) + `SUMMARY.md` (`# Feature surfaces` block) — **D2 is the SOLE owner** of both for the driver-column cohort; D3/D4 DEFER their matrix/SUMMARY rows to D2 (the parallel-blind-shared-index guard + the FEATURE-SURFACE single-index-owner rule, codified into `layer-intro-author`). Each authors its own chapter-file content (its own L4/L1/L0 bodies — anchor-distinct, parallel-safe). With the index/SUMMARY ownership partition stated, **NON-OVERLAPPING at the operational level — parallel** (per-report integrator applies D2 first so its owned block exists before D3/D4's deferred rows land into it; this is dispatch-ordering, one finalize). DUAL-REGISTRATION partition explicit: D2 adds its OWN matrix row + SUMMARY rows AND (as cohort owner) D3's + D4's deferred rows; D3/D4 author ONLY their chapter files + DEFER index/SUMMARY to D2.
- **D1/D2/D3/D4 ↔ D5**: D5 touches `L4/solve_family.md` + `L4-L3/index.md`. D1 touches `L4/index.md` (different file). D2 touches `feature/index.md` + `SUMMARY.md`. No shared file. `solve_family` is mentioned BY the existing magnetostatic feature column but D5 only re-anchors `solve_family.md`'s OWN §Specializations (not the feature chapters). **NON-OVERLAPPING — parallel.**
- **D5 ↔ D6**: D5 → `solve_family.md` + `L4-L3/index.md`; D6 → `fold_solve.md`. Disjoint. **NON-OVERLAPPING — parallel.**
- **D6 ↔ all**: `fold_solve.md` is touched by no other dispatch. D6 references the lifecycle feature column's AMR loop only as context (no edit to `feature/lifecycle.*`). **NON-OVERLAPPING — parallel.**

No two dispatches modify the same operator entry or rewrite the same theme body. The only shared mutable surfaces (`feature/index.md`, `SUMMARY.md` `# Feature surfaces`) are partitioned to a single owner (D2). All dispatches are parallel-safe.

## Sequencing schedule

**Single wave (all 6 parallel)** — all dispatches are non-overlapping per the analysis. The per-report integrator applies in a forward-reference-safe order at integration time (D2 before D3/D4 so the cohort index/SUMMARY block D2 owns exists before D3/D4's deferred rows merge in; D1 before any future output-product column, but those are not this cycle). There is exactly ONE `integrator-finalize` at cycle end (rebuild + commit + push); the wave is dispatch ordering, not multiple finalizes.

- **Wave 1 (parallel):** D1, D2, D3, D4, D5, D6.

Per-report integrator apply order (forward-reference ordering, NOT separate waves): D2 → D3 → D4 (driver-column cohort, owner-first) → D1 (combinator + L4/index row) → D5 → D6 (independent hygiene/fold-in, any order).

## Open questions / caveats

- **The `gram_reduce` constituents are rough-in.** D1 folds `matrix-weighted-norm` + `bilinear-form`, both `rough-in`. This is correct per the redirect (combinators rise regardless of constituent maturity) and the black-box/named-abstraction directive (`linear_combination`/`inner_product`-class combinators must reach L4). The combinator entry's OWN status is the fold-structure warrant (likely `rough-in (test-coverage-bounded)`); the harvester records its choice. The output-product feature columns (c074) will down-link to this combinator — replace-and-propagate then upgrades the two existing feature chapters' "two rough-in L1 primitives" prose to "a firm/rough-in L4 reduction" once D1 lands. I did NOT recruit the propagation re-anchor into the feature chapters THIS cycle (it would be a 2nd cross-report edit racing D1's landing); it sequences to c074 as the natural replace-and-propagate follow-on, OR D1 may include the propagation in its own proposed-changes if it judges the re-anchor mechanical (the floor-landing-implies-same-cycle-adjacent-entry-reanchor coupling pattern). Flagging for the orchestrator: if D1's scope is extended to bundle the two feature-chapter §Output-product-reduction re-anchors, that is the preferred coupled-pair form (form (i)); otherwise sequence to c074.
- **Item-3 priorities-assertion drift.** The priorities item-3 asserts a +1 anchor drift on `solve_family` §Specializations that the codemap read_range does NOT confirm (the `:30/:35/:36` cites are correct on disk). D5 is scoped "confirm-then-fix-only-if-actually-drifted." This is itself a datapoint for the batch-23 meta-phase: the `codemap-read-range-plus-one-drift-on-brace-boundary` class can drift the ASSERTION in a priorities note, not just a producer citation — the meta-phase may want to note that priorities-note anchor assertions are themselves drift-prone hints (the localization-hint sub-bullet already covers dispatch-scope ranges; this extends it to plan-text assertions).
- **Output-product + boundary-mode columns deferred, not dropped.** Capacitance/inductance gate on D1 (c074); S-params/eigenfreq+Q gate on additional postprocess constituents; boundary-mode gates on the 6th-ProblemType-vs-5-drivers OQ the batch-23 meta-phase should settle. After c073 the driver-column half of the spine is at 5-of-5 (electrostatic + magnetostatic + the 3 added) — a clean milestone the c074 planner + batch-23 meta-phase will read. No methodology-adjustment-warranting friction observed this cycle that the friction-ledger lacks (the priorities-assertion-drift note above is the one candidate; routed to batch-23 meta via this section per the cadence-staleness guidance).
- **`priorities.md` update**: I will mark cycle-073 active-head items #1/#2/#3/#4 as DISPATCHED with the D1–D6 mapping + paste-evidence pointer, and append a cycle-074 hand-off note (output-product columns sequenced; driver-column half at 5-of-5 after c073). I do NOT do batch-level migration (meta-phase's job).
