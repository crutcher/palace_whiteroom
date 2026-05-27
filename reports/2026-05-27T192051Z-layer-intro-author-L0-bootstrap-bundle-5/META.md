---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T19:55:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-27T20:15:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of CYCLE.md — L0 bootstrap bundle 5

## Critique

### Checks run

**citation-validity** — heightened scrutiny per dispatch guidance. Spot-checked ~30 citations across both chapters against `reference/palace/` directly. Verified file ranges: `communication.hpp:181-425` (Mpi class), `:244-249` (GlobalOp), `:251-256` (GlobalMin), `:265-270` (GlobalSum), `:347-360` (Print), `:391-392` (World), `:401-411` (Instance) — all exact. Verified vector.hpp call sites at lines 204, 214, 251, 281, 292 — all exact. Verified orthog.hpp lines 50, 70, 82 — all exact. Verified spaceoperator.cpp:374,416,450,490,689,723,750,810,1063,1101 — all 10 lines exact. Verified gmg.cpp:126-142, 147-167, 172-205 — all ranges exact. Verified preconditioner-class hpp ranges (amg.hpp:16-27, ams.hpp:20-79, jacobi.hpp:18-44, chebyshev.hpp:22-77 + 85-142, distrelaxation.hpp:29-88, gmg.hpp:30-82, blockprecond.hpp:31-61) — all exact. Verified test-rap.cpp:24-37 — exact. Verified ksp.cpp:303-306 convergence warning — exact. Mid-write self-correction (32 → 42 `Mpi::GlobalSum` count) is genuine: actual count is 42 ✓, and `GlobalMin+GlobalMax` = 36 ✓. **Two numerical-claim issues found** (one stale 32-count not propagated, one 28→20 Mpi::Print overcount); see Issues. Warning (not fail) because citation *ranges* are uniformly precise — the failures are interpretive numbers in prose, not the structural citation discipline that cycle-007/008 violated.

**surface-or-evidence** — not applicable in the refinement sense; this is a new-chapter creation (L0 reference notes), not a modification to existing operators or themes. Both chapters are wholly new L0 surface (source ranges, file structure, interpretation paragraphs) — no rotation-claim involved. Pass.

**rotation-quality** — not applicable; L0 reference chapters do not assert algebraic rotations between layers. The chapters explicitly position higher-layer rotations as forward-targets (`(forward-target)` annotations). Pass.

**variant-axis-coverage** — preconditioner-classes-overview correctly handles the `OperType ∈ {Operator, ComplexOperator}` variant axis (called out at the Group-2 heading and individually per class). The `Operator` vs `ComplexOperator` axis is explicitly named for each of the seven classes. The Hypre-wrapped classes (`BoomerAmgSolver`, `HypreAmsSolver`) are noted as real-only (they don't template on OperType — they inherit from `mfem::HypreSolver`). The `BlockDiagonalPreconditioner` real/complex aliases are cited at blockprecond.hpp:63-64. mpi-globalsum-and-collectives covers all `Mpi::Global*` variants (Sum/Min/Max/MinLoc/MaxLoc/Or/And) plus non-reduction collectives (Broadcast/Allgather/Allgatherv). No hidden branches. Pass.

**cross-reference-integrity** — all `[link]` references resolve. Verified all 9 cross-references to existing L0 chapters (`par-types-single-rank-reading`, `linalg-vector-file`, `linalg-free-functions`, `mfem-wrapper-solver`, `ksp-factory-file`, `kspsolver-base-class`, `linalg-operator-file`, `mutable-workspace-pattern`, `eigensolver-wrapper`) — all files exist under `book/src/L0/`. Verified forward refs: `L1/dot.md`, `L1/ksp_solve.md`, `L1-L0/minres-iteration.md`, `concepts/chebyshev-iteration.md`, `spec/slices/orthog.md`, `spec/slices/chebyshev.md` — all resolve. `../design/l4_calculus.md` resolves (referenced from the index.md edit). Pass.

**edge-label-fidelity** — not applicable; new L0 chapters are layer-internal reference notes, not lowering-theme entries with directional edge labels (no `L_{n+1}→L_n` markers). The "forward-target" annotations are not edge labels. Pass.

**plan-kind-consistency** — write-authority discipline honored exactly. New chapters are co-located in the report dir (lines 25, 29 of CYCLE.md), not pre-emptively written into `book/src/`. SUMMARY.md and index.md mutations are proposed-changes blocks with `[old]`/`[new]` (repairer-/integrator-friendly diff format). No artifact mutation in this report. Declared kind (`layer-intro-author` writing L0 reference chapters under priority #10 continuation) matches the deliverables. Pass.

**skill-uptake-survey** — `verify-citation-range` skill is the relevant skill for a citation-dense bundle, and the mid-write self-correction (32→42 GlobalSum count) is exactly the kind of friction the skill addresses. The report does not name the skill in its supporting-evidence section but the *behaviour* (recompute-and-correct) is consistent with the skill's intent. Surfaces telemetry only — pass.

### Issues found

**1. Stale `GlobalSum` count in chapter prose (mpi-globalsum-and-collectives.md:35).** The chapter line 35 says "**The most-used collective in Palace** (32 call sites across the tree; see "Call-site distribution" below)". The "Call-site distribution" section at line 59 then correctly says "42 `Mpi::GlobalSum` call sites". The mid-write correction (mentioned in CYCLE.md frontmatter) reached the lower section but not line 35. Severity: low (internal-consistency; the lower number is correct so an integrator-finalize-quality reader can resolve). Repair candidate: change line 35 "32 call sites" → "42 call sites".

**2. Overcounted `Mpi::Print` calls in iterative.cpp (mpi-globalsum-and-collectives.md, "Iterative-solver `Mpi::Print` calls" caveat block at CYCLE.md:127).** The CYCLE.md "Open questions" section says "`iterative.cpp` has 28 `Mpi::Print` call sites". Actual `grep -c "Mpi::Print" palace/linalg/iterative.cpp` = **20**. The cited example line `iterative.cpp:424` does contain `Mpi::Print(comm, "{}Residual norms for PCG solve\n",` (verified), so the *cited site* is correct, but the *count* is off by 8. Severity: low (the count is in a caveat block, not in the chapter body). Repair candidate: change "28 `Mpi::Print` call sites" → "20 `Mpi::Print` call sites".

**3. "32-line wrapper" potentially misleading (preconditioner-classes-overview.md:32).** The chapter says "`BoomerAmgSolver` (`palace/linalg/amg.hpp:16-27`) is a 32-line wrapper around `mfem::HypreBoomerAMG`". The cited range `16-27` is the class definition itself, which is **12 lines** (16, 17, ..., 27). The "32 lines" likely refers to the whole `amg.hpp` file length (32 lines verified). The phrasing "32-line wrapper" reads as "the wrapper class is 32 lines" — interpretively false (the class is 12 lines; the file is 32 lines). Severity: low (precision issue, not a citation failure). Repair candidate: change "32-line wrapper" → "12-line class definition in a 32-line file" or simply "thin wrapper".

**4. Workspace-vector count mislabeled (preconditioner-classes-overview.md:77).** The chapter says "four workspace vectors `mutable VecType x0, y0, x1, y1, t1`". This lists **five** vectors (`x0, y0, x1, y1, t1`), not four. Verified against blockprecond.hpp:40 which has all five. Severity: low (off-by-one in a prose count; the vector list is correct). Repair candidate: change "four workspace vectors" → "five workspace vectors".

**5. `jacobi.cpp:99-104` Mult body off-by-one start (preconditioner-classes-overview.md, Evidence section line 145).** The cited range starts at line 99, which is the closing `}` of the prior function (`Apply`). The actual `Mult` template/signature/body spans lines 100-104 (template line 100, signature 101, body 102-104). Severity: very low (one-line overrun on the start; the cited content is present in the range). Repair candidate: change `jacobi.cpp:99-104` → `jacobi.cpp:100-104` (or leave — within tolerance).

**6. `ksp.cpp:125-204` vs `ksp.cpp:125-240` inconsistency.** Frontmatter of CYCLE.md (supporting-evidence section, line 89) cites `palace/linalg/ksp.cpp:125-204` for the switch. Chapter prose at preconditioner-classes-overview.md line 24 cites `palace/linalg/ksp.cpp:125-240`. Verified: the switch ends at line 204, the surrounding `ConfigurePreconditionerSolver` function ends at line 240 (the closing `}` is line 240). Both ranges are defensible (one is the switch body, one is the function body). Severity: very low (minor consistency between report frontmatter and chapter prose). Repair candidate: align the two citations to one of `125-204` (switch only) or `125-240` (function), or annotate the distinction.

**7. Categorization mismatch between index.md and SUMMARY.md edits.** The index.md edit places `mpi-globalsum-and-collectives` under the "File overviews" group (correct — it is a file-level chapter); the SUMMARY.md edit places the same chapter *after* the "Class" entries (`eigensolver-wrapper`, plus the new `preconditioner-classes-overview`). The current SUMMARY.md order interleaves "Convention", "File", "Overload set", and "Class" entries already (lines 53-66), so the placement is not strictly wrong, but the new MPI file entry appears in the "Class" cluster rather than alongside the other "File —" entries (lines 59-62). Severity: very low (cosmetic ordering; mdBook navigation still works). Repair candidate: reorder SUMMARY.md insertion so the MPI "File —" entry sits with the other "File —" entries (after line 62 `linalg-iterative-file`), and the "Class — preconditioner" entry stays after `eigensolver-wrapper`.

**8. `ksp.cpp:213-232` cited as the DistRelaxation-vs-Chebyshev dispatch site (preconditioner-classes-overview.md:52).** The chapter says "the dispatch from `GeometricMultigridSolver` to `DistRelaxationSmoother` versus plain `ChebyshevSmoother` is keyed by the presence of the auxiliary-space interpolators `G` (`ksp.cpp:213-232`)". The cited range is the IIFE that selects whether to pass `&G` or `nullptr` to the `GeometricMultigridSolver` constructor. The actual decision DistRelaxation-vs-Chebyshev happens *inside* the constructor body (which receives `G` and dispatches accordingly), not at `ksp.cpp:213-232`. The cited range is the *input* to the dispatch, not the dispatch itself. Severity: low (interpretive imprecision; the cited range is on the dispatch chain). Repair candidate: rephrase as "the auxiliary-space interpolators `G` are conditionally constructed at `ksp.cpp:213-232` and passed to `GeometricMultigridSolver`, which dispatches to DistRelaxation when `G` is non-null." Or cite the `GeometricMultigridSolver` constructor body that does the dispatch.

**Summary**: 8 issues found, all low-severity and mechanically repairable. No structural citation failures (the cycle-007 scrambled-ranges and cycle-008 ellipsis-format patterns are absent — citation ranges are uniformly precise). The findings are interpretive-prose precision issues and one categorization quibble. Citation-validity is `warning` (not `fail`) because the *structural* citation discipline is clean; the issues are in numerical/interpretive prose.

## Repair

### Fixes attempted

All 8 findings were mechanical / surgical and within repair authority. All 8 repaired.

- **Finding 1**: Stale "32 call sites" in `mpi-globalsum-and-collectives.md` line 35 (lower section correctly says 42).
  - **Decision**: repaired
  - **Action**: `mpi-globalsum-and-collectives.md:35` — changed "32 call sites across the tree" → "42 call sites across the tree". Also propagated the corrected counts to `CYCLE.md` summary line (was "32 `GlobalSum` sites + 12 `GlobalMin` sites" → "42 `GlobalSum` sites + 36 `GlobalMin`/`GlobalMax` sites combined"), aligning with the chapter's lower section and the supporting-evidence section.

- **Finding 2**: Overcounted `Mpi::Print` calls in iterative.cpp (chapter open-questions claimed 28; actual `grep -c "Mpi::Print" palace/linalg/iterative.cpp` = 20).
  - **Decision**: repaired
  - **Action**: `CYCLE.md:127` (Open-questions / Iterative-solver `Mpi::Print` calls section) — changed "28 `Mpi::Print` call sites" → "20 `Mpi::Print` call sites" after direct recount via `grep`.

- **Finding 3**: "32-line wrapper" misleading (file is 31 lines per `wc -l`; class body 16-27 is 12 lines).
  - **Decision**: repaired
  - **Action**: `preconditioner-classes-overview.md:32` — changed "is a 32-line wrapper around `mfem::HypreBoomerAMG`" → "is a thin 12-line class definition (inside a 31-line header file) wrapping `mfem::HypreBoomerAMG`". Also corrected the Evidence-section line at `preconditioner-classes-overview.md:129` from "(32 lines total, including license / include)" → "(31 lines total, including license / include)" (verified `wc -l amg.hpp` = 31). The chapter's `palace/linalg/amg.hpp:1-31` citation range was already correct.

- **Finding 4**: Workspace-vector count mislabeled ("four workspace vectors" lists five: `x0, y0, x1, y1, t1`).
  - **Decision**: repaired
  - **Action**: `preconditioner-classes-overview.md:77` — changed "four workspace vectors `mutable VecType x0, y0, x1, y1, t1`" → "five workspace vectors `mutable VecType x0, y0, x1, y1, t1`".

- **Finding 5**: `jacobi.cpp:99-104` off-by-one start (line 99 is closing `}` of prior `Apply` function; `Mult` is at lines 100-104).
  - **Decision**: repaired
  - **Action**: `preconditioner-classes-overview.md` (Group-2 Jacobi paragraph + Evidence section) — `jacobi.cpp:99-104` → `jacobi.cpp:100-104` everywhere (both occurrences via `replace_all`). Verified `Mult` body spans lines 100-104 by direct source read.

- **Finding 6**: Internal inconsistency: `CYCLE.md:89` frontmatter cited `ksp.cpp:125-204` (switch only); chapter prose at `preconditioner-classes-overview.md:24` cited `ksp.cpp:125-240` (function body).
  - **Decision**: repaired
  - **Action**: Aligned both to `125-240` (the function body) with explicit annotation of the switch sub-range `136-204`. Updated `CYCLE.md:89` ("supporting evidence" line) to read "`palace/linalg/ksp.cpp:125-240` — `ConfigurePreconditionerSolver` function body; switch over `LinearSolver` enum spans lines 136-204 (verified each enum case)." Updated the Evidence section of `preconditioner-classes-overview.md` similarly. The chapter prose at line 24 already cited `125-240` with `136-204` for the switch — left as-is.

- **Finding 7**: SUMMARY.md insert miscategorization — MPI "File —" entry placed with "Class —" cluster instead of with other "File —" entries.
  - **Decision**: repaired
  - **Action**: `CYCLE.md` SUMMARY.md edit block — split the single combined edit into two separate edit blocks: (a) `[old]: - [File — palace/linalg/iterative.{hpp,cpp}](./L0/linalg-iterative-file.md)` `[new]: ...` + new MPI File entry directly after, sitting with the other "File —" entries; (b) `[old]: - [Class — EigenvalueSolver and wrappers](./L0/eigensolver-wrapper.md)` `[new]: ...` + new "Class — preconditioner classes overview" entry, sitting in the "Class —" cluster as critic recommended.

- **Finding 8**: `ksp.cpp:213-232` mis-labeled as DistRelaxation-vs-Chebyshev *dispatch* site (actually it's the IIFE that constructs `G` and forwards it to `GeometricMultigridSolver`'s constructor; the dispatch happens *inside* the constructor).
  - **Decision**: repaired
  - **Action**: `preconditioner-classes-overview.md:52` (Group-2 DistRelaxationSmoother paragraph) — rephrased to: "the IIFE at `ksp.cpp:213-232` constructs `G` from the FE-space hierarchy (or passes `nullptr`) and forwards it to the `GeometricMultigridSolver` constructor, which then dispatches to DistRelaxation when `G` is non-null and to plain Chebyshev otherwise (selection logic inside the constructor body, `gmg.cpp`)." Also tightened the parallel passage at `preconditioner-classes-overview.md:26` (the `ChebyshevSmoother` non-enum-selectable paragraph) for consistency: "selection of distributive-relaxation vs Chebyshev happens inside that constructor based on whether the discrete-gradient hierarchy `G` is non-null, with `G` constructed conditionally on `linear.mg_smooth_aux` at the IIFE in `ksp.cpp:213-232` before being forwarded to the constructor".

### Unrepairable findings

None. All 8 findings were mechanical numerical-prose / categorization fixes within repair authority — no substantive authoring required and no contradictions with existing artifact content surfaced.

## Suggested resolution

`ready` — all 8 low-severity findings repaired in-place in `CYCLE.md` and the two co-located chapter files. Integrator-per-report can apply the proposed-changes blocks as-is. Notes for the integrator:

- The two co-located chapter files (`mpi-globalsum-and-collectives.md`, `preconditioner-classes-overview.md`) carry the repaired prose; copy them to `book/src/L0/` per the existing dispatch convention.
- The SUMMARY.md edit is now two separate edit blocks (one in the "File —" cluster after `linalg-iterative-file`, one in the "Class —" cluster after `eigensolver-wrapper`); apply both.
- No edge cases or follow-up agent routing needed.
