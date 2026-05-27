---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T16:17:42Z
critic_version: 1
checks:
  citation-validity: fail
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-27T16:35:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: critique of L0 bootstrap bundle 3

## Critique

### Checks run

**citation-validity** — Spot-checked 4 files from the verification cohort (`solver.hpp`, `solver.cpp`, `iterative.hpp`, `iterative.cpp`) plus `operator.hpp` and `floquetcorrection.hpp`. Most citations resolve correctly: file line counts match (`iterative.hpp` 279, `iterative.cpp` 882, `operator.hpp` 407, `operator.cpp` 698, `solver.hpp` 138, `solver.cpp` 209), all `solver.cpp` `MfemWrapperSolver` method ranges (12-30, 33-136, 138-142, 144-177, 179-207) check out exactly, all `iterative.hpp` class-declaration ranges (25-115, 117-150, 152-217, 219-275) and field-line numbers (53-55, 144, 190-194, 256, 263-272) check out, all `operator.hpp` workspace anchors (73-113, 81, 116-136, 120, 178-226, 192, 199, 202-206) check out, and `solver.hpp:21-65, 70-134, 77, 80, 84-94, 103-110, 125-129, 131-133` all check out. `iterative.cpp:443` for `A->Mult(p, z)` checks out. `GmresSolver::Initialize` 488-516 and `Update` 518-541 and `Mult` 543-705 all check out. **However**, the four "Free-function helpers" citations in `linalg-iterative-file.md` are systematically wrong — the line ranges are scrambled across helpers AND one helper name is wrong. Verdict: **fail** (concrete errors below in Issues).

**surface-or-evidence** — These are pure-new L0 reference notes (kind: theme/observation, in plan-kind language). They are *reference-note overlay* over L0 source; they don't propose surface modifications to existing operators/themes. They consist of citations + interpretive prose, exactly the L0 reference-note discipline established by `book/src/L0/index.md`. No rotation_claim is asserted; no surface change to existing operators is proposed. This check is essentially "are these L0-shaped" rather than "is there surface + evidence" — and they are L0-shaped: every chapter contains 20+ citations and stays within the 2-4 paragraph + citation discipline. Verdict: **pass**.

**rotation-quality** — The chapters intentionally make *no* rotation claims; they are L0 reference notes. The closest things to algebraic claims are the equivalent-real block formulation `A = [Ar, Ai; Ai, -Ar]` and the PCG-step recurrence sketch in `linalg-iterative-file.md`. Both are descriptions of what the L0 code does, not L_{n+1}→L_n rewrites. The chapters defer all rotation language to "Notes for higher layers" sections which explicitly forward-declare future L1 work (`pc_apply`, `ksp_solve`) without claiming to perform the rotation here. Verdict: **pass** (not applicable to L0-reference-note shape, correctly).

**variant-axis-coverage** — `mfem-wrapper-solver.md` correctly enumerates the `complex_matrix = true|false` variant axis (equivalent-real block vs real-part approximation) and the `ArrayMult` fast-path vs augmented-block-vector branch in complex `Mult`. `linalg-iterative-file.md` explicitly calls out orthogonalisation as a variant axis (`MGS / CGS / CGS2`) and the `pc_side = LEFT/RIGHT` axis for GMRES vs FGMRES's RIGHT-only constraint. `mutable-workspace-pattern.md` correctly categorises four sub-patterns (operator-composition / iterative-solver / solver-workspace / retained-assembled-matrix) and Caveat #4 in CYCLE.md explicitly acknowledges Category-4's awkward fit. Verdict: **pass**.

**cross-reference-integrity** — All link targets resolve. Concepts pages `complex-from-real-lift.md`, `solver-as-operator.md`, `solve-monad.md`, `incremental-least-squares.md` all exist under `book/src/concepts/`. L2 `krylov-step.md` exists. L1-L0 `apply-linop-mutation-rotation.md` exists. All L0 sibling references (`apply-linop-overload-set`, `kspsolver-base-class`, `ksp-factory-file`, `transparent-vs-load-bearing-tricks`, `output-arg-vs-receiver`, `linalg-iterative-file`, `mutable-workspace-pattern`, `mfem-wrapper-solver`) resolve (existing files for the cycle-006 cohort, new files in this report's proposed-changes for the three new chapters). The L0 `index.md` and `SUMMARY.md` edits insert the new entries in alphabetical order within each grouping (confirmed against existing `index.md` content). Verdict: **pass**.

**edge-label-fidelity** — Report does not carry an L_{n+1}→L_n edge label (these are L0 entries with forward-pointers to L1 / L1>L0 / L4 anticipations). The "Referenced from" sections are explicitly forward-declared and the prose discusses L0 content. No edge mismatch. Verdict: **pass** (not applicable).

**plan-kind-consistency** — Declared scope is "L0 bootstrap bundle 3 (priority #10 continuation)". The chapters are observation-shaped reference notes (matching the cycle-005/cycle-006 L0 reference-note cohort precedent). Status `pending` is appropriate for a fresh dispatch. The CYCLE.md `Summary` clearly frames this as adding 3 reference-note chapters; the proposed-changes blocks are pure file additions plus index/SUMMARY updates; no L1 rotation work creep. Verdict: **pass**.

**skill-uptake-survey** — Relevant skills include `verify-citation-range` (which would have caught the helper-citation errors — see Issue #1) and `classify-variant-axis` (which would document the `complex_matrix` and `pc_side` axes). Caveat #5 in CYCLE.md explicitly notes that codemap MCP tools were not invoked because the source files were well-localised. Neither `verify-citation-range` nor `classify-variant-axis` is referenced in CYCLE.md. The chapters are well-structured and the variant axes are documented organically; the missing `verify-citation-range` invocation is the more material gap (had it run, Issue #1 would have been caught pre-dispatch). Verdict: **warning** — survey-telemetry only per check-spec, not blocking.

### Issues found

**Issue #1: Helper-function citations in `linalg-iterative-file.md` are scrambled / mis-named** *(severity: high; location: `linalg-iterative-file.md` §"Free-function helpers")*.

The chapter claims four helpers in `iterative.cpp`:
- `CheckDot` at `iterative.cpp:307-325` — **wrong**. Actual location: lines 21-32 (real and complex specialisations).
- `ApplyB` at `iterative.cpp:287-305` — **wrong**. Actual location: lines 243-250.
- `ApplyBA` at `iterative.cpp:243-285` — **wrong**. Actual location: lines 287-305 (lines 243-285 contain `ApplyB` + `InitialResidual`).
- `OrthogonalizeColumn` at `iterative.cpp:329-358` — **wrong both as line range and as name**. The actual helper at lines 307-325 is named `OrthogonalizeIteration` (it dispatches via `switch` to `linalg::OrthogonalizeColumnMGS` / `OrthogonalizeColumnCGS`). Lines 329-358 start the `IterativeSolver<OperType>` constructor, not the orthogonalisation helper.

The pattern looks like the line ranges were rotated/swapped during authoring. The Evidence-section bullets repeat the same wrong ranges:
- `iterative.cpp:243-285 — ApplyBA` (wrong)
- `iterative.cpp:287-305 — ApplyB` (wrong)
- `iterative.cpp:307-325 — CheckDot` (wrong)
- `iterative.cpp:329-358 — OrthogonalizeColumn` (wrong both range and name)

This is a citation-validity failure at the algebraic-claim level: the chapter's prose describes what each helper *does* (`CheckDot` guards `(Br,r) ≤ 0`; `ApplyB` wraps `B->Mult` in a `BlockTimer`; `ApplyBA` selects `B·A·x` vs `A·B·x` by `pc_side`; the orthogonalisation helper dispatches on `gs_orthog`) — all four descriptions are correct in content, but they cite the wrong file ranges. Additionally, the helper-section also references a fourth missing helper (`InitialResidual` at 252-285) which is not enumerated, even though it's part of the same anonymous-namespace cluster the section claims to cover.

**Issue #2: Helper name `OrthogonalizeColumn` does not exist in `iterative.cpp`** *(severity: medium; location: `linalg-iterative-file.md` §"Free-function helpers" bullet 4)*.

The actual name is `OrthogonalizeIteration`. The chapter conflates `OrthogonalizeIteration` (anonymous-namespace dispatch helper) with `linalg::OrthogonalizeColumnMGS` / `linalg::OrthogonalizeColumnCGS` (the actual orthogonalisation routines in `linalg/orthog.hpp`, called *by* `OrthogonalizeIteration`). The L1/L2 vocabulary may reasonably call the operation "orthogonalize-column" but the L0 reference note should use the C++ symbol name.

**Issue #3: `floquetcorrection.hpp` line-range citation is mildly off** *(severity: low; location: CYCLE.md §"Source-range verification" and `mutable-workspace-pattern.md` Evidence)*.

The verification section claims `palace/linalg/floquetcorrection.hpp lines 35-65 — mutable VecType rhs at line 49 confirmed; class context confirmed.` The file is 64 lines (not 65); the cited class `FloquetCorrSolver` spans 32-60, with `mutable VecType rhs` at line 49. Line 49 cite is correct ✓; the 35-65 range frame is slightly over-broad (includes the `}` namespace closer and `#endif`) but not load-bearing.

**Issue #4: `iterative.hpp:53-55` cited twice with `mutable int final_it` semantics, but `final_it` is at line 55** *(severity: low / nit; location: `mutable-workspace-pattern.md` Evidence and `linalg-iterative-file.md` §`IterativeSolver`)*.

The chapters say `IterativeSolver::final_it` is part of the `mutable` triplet at lines 53-55. Actually the declarations are: `mutable bool converged;` (53), `mutable double initial_res, final_res;` (54), `mutable int final_it;` (55). So 53-55 covers all four mutable statistics. Correct as a range, but the chapter prose says "All declared `mutable` so they can be written by the `const`-method `Mult` body" — accurate. Not an error, noting for completeness.

**Issue #5: `Solver<OperType>` `Mult` inheritance claim is slightly imprecise** *(severity: low; location: `mfem-wrapper-solver.md` §"At a glance")*.

The chapter says `Declares the abstract SetOperator(const OperType &op) and inherits a pure-virtual Mult from OperType.` Looking at `solver.hpp:21-65`, `Solver<OperType>` indeed inherits `Mult` from `OperType` (which is `Operator` or `ComplexOperator`); the pure-virtual nature comes from the base `mfem::Operator::Mult` declaration. The `Solver` base class additionally declares `MultTranspose` as `MFEM_ABORT`-stubbed (lines 46-49) and `Mult2`/`MultTranspose2` virtuals at 52-64 also `MFEM_ABORT`-stubbed. The "inherits a pure-virtual Mult" framing is technically correct but elides the `MFEM_ABORT`-stubbed siblings — a forward audit by a critic on transparent-vs-load-bearing classification might want this distinction. Not blocking.

**Issue #6: `mfem-wrapper-solver.md` "eight call sites" count is inconsistent with the enumeration** *(severity: low; location: `mfem-wrapper-solver.md` §"Where MfemWrapperSolver is used" intro vs CYCLE.md §"Source-range verification" grep enumeration)*.

The chapter says "A full grep of `reference/palace/` finds eight call sites that construct an `MfemWrapperSolver`" and then lists:
- ksp.cpp:120 (1)
- divfree.cpp:120 (1)
- hcurl.cpp:92 (1)
- errorestimator.cpp:88, 94 (2)
- modeeigensolver.cpp:666, 733, 742, 749, 761, 774 (6)

Total: 1+1+1+2+6 = 11 distinct call-site line numbers. The CYCLE.md verification section lists `modeeigensolver.cpp:666, 727, 733, 742, 749, 761, 774` (7 line numbers in `modeeigensolver.cpp`; chapter listing drops `727` and lists 6). The "eight" count doesn't match either enumeration; the chapter and verification section disagree on whether `modeeigensolver.cpp:727` is a call site. This is grep-verified-only data per the chapter's discipline, so the exact count is not load-bearing for an algebraic claim — but the inconsistency between the chapter's "eight" and its own bullet enumeration (11) plus the CYCLE.md's 12 should be reconciled.

**Issue #7: `solver.hpp:84-94` configuration-flags claim covers 4 flags + 1 counter** *(severity: low / nit; location: `mfem-wrapper-solver.md` Evidence bullet)*.

The chapter says `solver.hpp:84-94 — configuration flags: save_assembled, complex_matrix, drop_small_entries, reorder_reuse`. Lines 84-94 actually contain:
- `save_assembled` (84)
- `complex_matrix` (88)
- `drop_small_entries` (91)
- `reorder_reuse` (94)
- plus `num_dropped_entries` (97 — outside the range)

The four-flag claim is correct as named, but the range 84-94 includes blank lines and intervening comment blocks; line 97 (`num_dropped_entries`) is a related-but-distinct stateful counter that the chapter discusses in §"DropSmallEntries optimisation" (referring to it as state tracked for pattern-change detection) but does not enumerate in the Evidence-section configuration-flag bullet. Inconsistency between Evidence-section and prose; not load-bearing.

**Issue #8: `skill-uptake-survey` finding — `verify-citation-range` was not invoked** *(severity: warning-only; location: CYCLE.md Caveat #5)*.

The dispatch explicitly notes "Codemap MCP tools were not used during this dispatch" but does not mention `verify-citation-range` (a skill, not an MCP tool). The four scrambled helper citations in Issue #1 are exactly the failure mode `verify-citation-range` is designed to catch. With 60+ citations across three chapters, programmatic verification would have been efficient. Telemetry only — repairer may want to invoke `verify-citation-range` on the full citation set during repair, both to catch any analogous errors in the unverified set and as a precedent for future L0 bundles.

## Repair

### Source-verification ground truth (re-derived from `reference/palace/palace/linalg/iterative.cpp`)

Read lines 1-360 of `iterative.cpp` directly to re-derive the correct anonymous-namespace helper boundaries from first principles. The anonymous namespace spans lines 18-327; constructor at line 329 onward. Verified helper ranges (each verified by reading the exact line where the function signature begins and where its closing brace closes):

| Helper | Lines | Notes |
|---|---|---|
| `CheckDot` (real + complex specialisations) | 21-32 | Two `inline void CheckDot` template overloads |
| `SafeMin` | 34-51 | Numeric-limits helper |
| `SafeMax` | 53-70 | Numeric-limits helper |
| `GeneratePlaneRotation` (real) | 72-109 | Givens rotation |
| `GeneratePlaneRotation` (complex) | 111-224 | Givens rotation, complex spec |
| `ApplyPlaneRotation` (real) | 226-232 | Givens application |
| `ApplyPlaneRotation` (complex) | 234-241 | Givens application, complex spec |
| `ApplyB` | 243-250 | Preconditioner apply with `BlockTimer(Timer::KSP_PRECONDITIONER, ...)` |
| `InitialResidual` | 252-285 | Initial residual with PreconditionerSide-branching |
| `ApplyBA` | 287-305 | Combined precond+op apply, `pc_side`-branching |
| `OrthogonalizeIteration` | 307-325 | MGS/CGS/CGS2 dispatch over `linalg::OrthogonalizeColumn{MGS,CGS}` |

The helper-section's original ranges were **systematically wrong**: `CheckDot`/`ApplyB`/`ApplyBA` had ranges rotated across each other; `OrthogonalizeColumn` was named for the delegated routine, not the dispatch helper, and pointed at the IterativeSolver constructor's opening lines.

Additionally verified:
- `floquetcorrection.hpp` is 64 lines (not 65); `FloquetCorrSolver` class spans 32-60 (not 35-65).
- `MfemWrapperSolver` construction sites total **11**, not 8: 1 (`ksp.cpp:120`) + 1 (`divfree.cpp:120`) + 1 (`hcurl.cpp:92`) + 2 (`errorestimator.cpp:88, 94`) + 6 (`modeeigensolver.cpp:666, 733, 742, 749, 761, 774`). Verified via `grep -rn "make_unique<MfemWrapperSolver" reference/palace/palace/`. The spurious `modeeigensolver.cpp:727` is a type-signature reference inside a lambda return type, not a construction call.

### Fixes attempted

- **Issue #1 (high) — Free-function helper citations scrambled**: **repaired**.
  - Edited `linalg-iterative-file.md` §"Free-function helpers" — corrected all 4 scrambled citations (`CheckDot` 307-325→21-32, `ApplyB` 287-305→243-250, `ApplyBA` 243-285→287-305, helper-set range 21-358→21-325), added `InitialResidual` (252-285) as a 5th bullet, replaced "Sundry small-dense" range `21-241` → `34-241` to exclude `CheckDot`, enumerated the sundries explicitly (`SafeMin`/`SafeMax`, `GeneratePlaneRotation` real+complex, `ApplyPlaneRotation` real+complex).
  - Edited Evidence section — reordered the 4 helper-citation bullets to ascending-line order, corrected each range, added `InitialResidual` (252-285), added the small-dense kernel range (34-241).
  - Edited `linalg-iterative-file.md` §"CgSolver" — corrected the inline reference to `CheckDot` (307-325 → 21-32).
- **Issue #2 (medium) — Wrong helper name `OrthogonalizeColumn`**: **repaired**.
  - Replaced with the actual C++ symbol name `OrthogonalizeIteration` in the helper-section bullet and the Evidence-section bullet. Added clarifying prose that this dispatch helper delegates via `switch` to `linalg::OrthogonalizeColumnMGS` / `linalg::OrthogonalizeColumnCGS` (the routines in `linalg/orthog.hpp`).
  - Also updated CYCLE.md Caveat #2 to use the corrected helper list (`CheckDot`, `ApplyB`, `InitialResidual`, `ApplyBA`, `OrthogonalizeIteration`).
- **Issue #3 (low) — `floquetcorrection.hpp:35-65` range off by 1 + over-broad**: **repaired**.
  - Edited CYCLE.md §"Source-range verification" — replaced `lines 35-65` with `(64 lines total) — FloquetCorrSolver class at lines 32-60`. Chapter `mutable-workspace-pattern.md` did not actually contain a `35-65` range citation (only line `49`); only CYCLE.md verification claim needed correction.
- **Issue #4 (low/nit) — `iterative.hpp:53-55` `final_it` is at line 55, not 53**: **not-needed**.
  - Critic explicitly says "Correct as a range, but the chapter prose says ... — accurate. Not an error, noting for completeness." No edit required.
- **Issue #5 (low) — `Mult` inheritance claim elides `MFEM_ABORT`-stubbed siblings**: **unrepairable** (substantive content authoring).
  - Adding a discussion of the `MultTranspose` / `Mult2` / `MultTranspose2` `MFEM_ABORT` stubs to the "At a glance" section would be authorial content expansion, not a mechanical fix. The Evidence section already cites lines 46-49 and 52-64 for these stubs, so the underlying citation is intact. Critic flagged as "Not blocking"; a future lifter or cross-cutter could expand the framing.
- **Issue #6 (low) — `mfem-wrapper-solver.md` "eight" call-site count contradicts enumeration**: **repaired**.
  - Edited chapter intro: `eight call sites` → `eleven construction sites` and clarified the grep pattern (`std::make_unique<MfemWrapperSolver<...>>`).
  - Edited CYCLE.md §"Source-range verification" — removed spurious `modeeigensolver.cpp:727` from the construction call-site list, added clarifying note that `727` is a type-signature reference (lambda return type), not a call site, and called out total = 11.
- **Issue #7 (low/nit) — Configuration-flags Evidence bullet doesn't enumerate `num_dropped_entries`**: **repaired**.
  - Edited `mfem-wrapper-solver.md` Evidence-section bullet for `solver.hpp:84-94` — added per-line labels for each flag (84/88/91/94) and a parenthetical noting `num_dropped_entries` at line 97 with cross-reference to §"DropSmallEntries optimisation".
- **Issue #8 (warning-only) — `verify-citation-range` not invoked**: **not-needed** (telemetry only).
  - Per repairer-spec the warning is not blocking. During repair I manually re-verified the high-severity range (`iterative.cpp:1-360`) by directly reading source and cross-checked the `floquetcorrection.hpp` and `MfemWrapperSolver` grep claims; no further analogous errors surfaced in the spot-checked region. Skill invocation by the producer remains a methodology-level concern for a future cycle.

### Unrepairable findings

- **Issue #5** — substantive authoring required (expand "At a glance" framing to discuss the `MFEM_ABORT`-stubbed sibling virtuals). Defer to a future cross-cutter or lifter pass. No follow-up agent invocation needed for this cycle; the Evidence-section citations are intact.

## Suggested resolution

`overall_status: ready`. All high-severity and low-severity-fixable issues have been mechanically repaired. The single unrepairable finding (Issue #5) is non-blocking and explicitly flagged by the critic as "not blocking". The corrected citations have been verified by direct source reading.

Integrator notes:
- The repaired `linalg-iterative-file.md` is the version to apply via the `book/src/L0/linalg-iterative-file.md` proposed-change block. (The proposed-change uses a placeholder `<contents of ...>` reference so the integrator-per-report will read the live chapter file at apply time — repairs land automatically.)
- The repaired `mfem-wrapper-solver.md` (eleven-call-sites fix + Evidence-bullet clarification) similarly lands via its proposed-change placeholder.
- CYCLE.md text edits (verification-section corrections, caveat reword) are integrator-informational only; they don't propagate to `book/`.

The Issue #1 failure pattern is exactly what `verify-citation-range` is designed to catch (Issue #8 telemetry). Future L0 bootstrap dispatches with 60+ citations should be advised to invoke that skill — captured as a procedural follow-up but no repair action filed against this report.
