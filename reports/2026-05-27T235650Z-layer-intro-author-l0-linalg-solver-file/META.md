---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T23:59:30Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-28T00:05:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: unrepairable
overall_status: pass-after-repair
follow_up_agent: null
---

# META: verification of L0 / linalg-solver-file

## Critique

### Checks run

**citation-validity (warning).** Every claim in the proposed chapter and evidence list carries a citation pointer. Spot-checks against `reference/palace/palace/linalg/solver.hpp` and `solver.cpp` confirm the cited regions exist, the content matches what the chapter claims, and the structural claims (Solver<OperType>: public OperType inheritance, static_assert constraint, MFEM_ABORT-defaulted Mult2/MultTranspose2, the eight concrete-subclass family) are accurate. However, a systematic off-by-one drift runs through most line citations — the chapter and evidence list cite line numbers that are consistently 1 below the actual source line. Examples (chapter form vs actual):
- `Solver<OperType>` class body cited as `lines 20-64` (actual `class Solver` at line 22, closing `};` at line 65); claim "lines 20-64" is acceptable only if interpreted to include the preceding 2-line comment block at lines 15-18 and the blank line.
- `bool initial_guess (line 32)` — actual line 33; line 32 is the blank line before `protected:`.
- Constructor + virtual destructor `(lines 35-36)` — actual lines 36-37.
- `SetInitialGuess (line 39)` — actual line 40.
- `SetOperator(const OperType &op) (line 42)` — actual line 43.
- `MultTranspose (lines 45-48)` — actual lines 46-49.
- `Mult2(x, y, r) (lines 51-56)` — actual lines 52-56 (start off by 1).
- `MultTranspose2(x, y, r) (lines 60-63)` — actual lines 60-64 (end off by 1).
- `comment block introducing MfemWrapperSolver (lines 66-68)` — actual lines 67-69.
- `unique_ptr<mfem::Solver> pc (line 76)` — actual line 77.
- `unique_ptr<mfem::HypreParMatrix> A (line 79)` — actual line 80.
- `solver.cpp:12-29` for `MfemWrapperSolver<Operator>::SetOperator` — closing brace at line 30 (off-by-1 at end).
- `solver.cpp:31-135` — actual lines 32-136 (off by 1 both ends).
- `solver.cpp:144-178` for `MfemWrapperSolver<ComplexOperator>::Mult` — closing brace at line 177 (off by 1 end).
- `solver.cpp:180-208` for `DropSmallEntries` — actual lines 179-207 (off by 1 both ends).
- `imaginary-part sign-flip at line 172` — actual line 173 (`yi *= -1.0;`).
- `threshold ε² at line 184` — actual line 183 (the `std::pow(...epsilon(), 2)` call).
- `MUMPS reorder_reuse interaction at lines 187-203` — actual lines 186-202.
- `palace/linalg/iterative.hpp:25-115` for `IterativeSolver` — class declared line 26 (start off by 1; closing brace line 115 matches).
- `palace/linalg/ksp.hpp:42` for `unique_ptr<Solver<OperType>> pc` — actual line 41 (off by 1 in opposite direction).

The drift is uniform enough to suggest a `cat -n`-like one-indexed offset against zero-indexed reading, or the agent counted from `#ifndef` line as 1 vs 0. Content of the cited regions is correct on inspection; the drift is mechanical, not semantic. Warning rather than fail because every cited region exists and the cited content matches the prose; readers using the cited ranges will land within a line of the intended anchor.

**surface-or-evidence (pass).** This is a layer-intro-author dispatch producing a new L0 file-overview chapter — surface authoring, not refinement. The chapter is the surface. No rotation_claim is asserted (L0 reference notes do not lower into anything; they are anchors). The check applies trivially: surface present, citations attached.

**rotation-quality (pass).** Not applicable — this is an L0 reference-note chapter, not an L_{n+1}>L_n lowering theme. The chapter forward-references the L4 `solver-as-operator` concept (at `concepts/solver-as-operator.md`) and notes the `OperType`-template-axis collapse to L1 (eight L1 solver families), but it does not author the rotation — it only points at where the rotation will be authored. Marked pass: not applicable to L0-file-overview shape.

**variant-axis-coverage (pass).** The chapter explicitly enumerates the variant axes affecting `Solver<OperType>`: (a) `OperType` template parameter (`Operator` / `ComplexOperator`) — covered via `static_assert` and the `VecType` `std::conditional` pattern; (b) `initial_guess` bool flag — covered as state-not-input concern with L1 lifting note; (c) `Mult` vs `Mult2` preallocated-temporary entry points — covered as L0-specific opt-in optimisation; (d) `MultTranspose` vs `MultTranspose2` — covered (both default to `MFEM_ABORT`); (e) the eight concrete-subclass families — enumerated with declaring files. The chapter also explicitly notes axes deferred to higher-layer entries (direct-vs-iterative classification at consumer side; Hermitian-transpose entry point inherited but not surfaced at `Solver<OperType>` API). No hidden branches detected.

**cross-reference-integrity (pass).** All eight intra-L0 link targets resolve: `mfem-wrapper-solver.md`, `kspsolver-base-class.md`, `linalg-iterative-file.md`, `preconditioner-classes-overview.md`, `ksp-factory-file.md`, `apply-linop-overload-set.md`, `mutable-workspace-pattern.md`, `mfem-vector-types.md`. The `concepts/solver-as-operator.md` reference resolves. The proposed `L0/index.md` row anchor (between `linalg-iterative-file` and `mpi-globalsum-and-collectives`) matches the actual file layout (verified `index.md:27` for the `linalg-iterative-file` row; `index.md:28` is `mpi-globalsum-and-collectives`). The proposed `SUMMARY.md` edit anchor (after `iterative.{hpp,cpp}` row line 66) matches the actual SUMMARY.md layout. The `[old]` line text in the L0/index.md edit matches the actual file content verbatim.

**edge-label-fidelity (pass).** The proposal carries no edge label — this is an L0 chapter, not a lowering theme. Forward-references to "L1 `ksp_solve`" and "L1 `apply_preconditioner`" are clearly tagged as forward-pointing notes, not as edges this chapter authors. Marked pass: not applicable to L0-reference-note shape.

**plan-kind-consistency (pass).** The dispatch was layer-intro-author producing a firm L0 file-overview chapter; the content shape matches — fully-cited at-a-glance section, region-by-region structural breakdown of header + cpp, notes-for-higher-layers, dependencies, evidence list. Matches the precedent shape of `linalg-iterative-file`, `linalg-operator-file`, `linalg-vector-file`, `ksp-factory-file`, `mpi-globalsum-and-collectives`. Plan kind: firm L0 reference-note authoring. Content matches.

**skill-uptake-survey (warning).** The dispatch was a citation-heavy L0 file overview that would have benefited from invoking the `verify-citation-range` skill on the dense block of ~40 line-range citations in the evidence list before submission. The systematic off-by-one drift documented in citation-validity above is exactly the failure mode that skill exists to catch. No mention of `verify-citation-range` invocation in the report; no notes indicating the citations were spot-checked against the source. Telemetry-level signal (not blocking) — the report's content is correct on inspection, but the off-by-one pattern would have been caught by a single skill invocation on any one of the evidence rows.

### Issues found

1. **Systematic off-by-one line citation drift** (severity: warning; CYCLE.md §"At a glance" + §"`Solver<OperType>` — the abstract base" + §"Evidence (representative)").
   - Most line citations in the chapter body and evidence list are off by 1 (start, end, or both) against `reference/palace/palace/linalg/solver.hpp` and `solver.cpp`. The drift is uniform direction (cited line is below actual source line) and content matches. Examples enumerated under citation-validity above.
   - Mechanical to repair: each off-by-one cited line/range can be incremented by 1 to land on the actual source content. Repair surface is the chapter body + the ~40-row evidence list block.

2. **Friction signal: dispatch-prompt framing was inaccurate** (severity: observation; CYCLE.md §"Open questions / caveats" §1).
   - The dispatch brief described `Solver<OperType>` as "the abstract base class for direct solvers like LU/Cholesky, exterior to the `BaseKspSolver<>` Krylov hierarchy". Source inspection corrected this to "type-axis root of ALL Palace solvers (preconditioners + iterative + MFEM-wrapped)". The report adopted the corrected framing — this is correct behavior on the dispatched agent's part. The friction lies upstream: the cycle-planner brief drift. Per the user-message brief, this is recurrence-2 since cycle-010; not currently captured in `scaffolding/friction-ledger.md` under any named slug. Surface-level signal for meta-phase consideration; no in-report repair action.

3. **No `verify-citation-range` skill invocation noted** (severity: warning; CYCLE.md as a whole).
   - Given the ~40-row evidence list and the dense citation surface in chapter body, the report would have benefited from invoking `verify-citation-range` (skill exists in `skills/` per CLAUDE.md §Skills) on at least a sample of the cited ranges before submission. The systematic off-by-one drift in finding (1) is exactly the failure mode the skill exists to catch. Telemetry signal; not blocking.

4. **`Solver<OperType>` class body line range claim "lines 20-64" understates content position** (severity: minor; CYCLE.md §"At a glance").
   - The claim "`Solver<OperType>` (lines 20-64)" is interpretable only if "20" anchors to the preceding comment block (line 20 is `// Abstract base class for real-valued or complex-valued solvers.`). The `class Solver` template declaration is at lines 21-22 and the closing `};` is at line 65. The convention in adjacent L0 chapters (`linalg-iterative-file`, etc.) cites the class-declaration line (e.g., `iterative.hpp:26-115` for `IterativeSolver`), not the comment-block line. Either accept the broader range as a convention here, or repair to `lines 22-65` for consistency.

5. **`MfemWrapperSolver<OperType>::DropSmallEntries` characterized as "non-templated-specialisation method definition"** (severity: minor; CYCLE.md §"At a glance" + §"`MfemWrapperSolver<OperType>` — the in-file concrete subclass").
   - The cpp definition at lines 179-207 uses `template <typename OperType>` (single template-generic definition, not per-`OperType` specialization). The chapter's phrasing "non-templated-specialisation method definition" is awkward and could be misread as "non-templated method definition" (which would be wrong). Clearer phrasing: "the only `template <typename OperType>` (non-specialized) method definition in `solver.cpp`" or "the single generic template definition (vs the per-`OperType` specializations of `SetOperator` and `Mult`)".

6. **Evidence list line "palace/linalg/ksp.hpp:42" for the preconditioner field cited as line 42, actual line 41** (severity: warning; CYCLE.md §Evidence).
   - The `std::unique_ptr<Solver<OperType>> pc;` field is at `ksp.hpp:41` (verified). The report cites line 42. Off-by-one in the opposite direction from the solver.hpp/.cpp drift — suggests the drift is not a uniform offset bug but a per-citation accuracy issue.

## Repair

### Fixes attempted

- **Finding 1**: Systematic off-by-one line citation drift across chapter body + evidence list (critic's enumerated drift list).
  - **Decision**: repaired
  - **Action**: Re-read `reference/palace/palace/linalg/solver.hpp` (138 lines) and `solver.cpp` (209 lines) line-by-line; reconciled every cited line/range against actual source content; applied corrected line numbers to CYCLE.md §"At a glance", §"`Solver<OperType>` — the abstract base", §"`MfemWrapperSolver<OperType>` — the in-file concrete subclass", §"The eight `Solver<OperType>` subclass families" (ASCII tree), §"Notes for higher layers", §"Evidence (representative)", §"Open questions / caveats" #3, §"Supporting evidence". Specific corrections (chapter-form → repaired-form): `Solver<OperType>` body `20-64` → `21-65` (template-line start + closing-brace end, matching sibling `linalg-iterative-file` convention of citing the `template <typename OperType>` line); `static_assert` `23-25` → `24-26`; `using VecType` `28-29` → `29-30`; `initial_guess` `32` → `33`; ctor+dtor `35-36` → `36-37`; `SetInitialGuess` `39` → `40`; `SetOperator` `42` → `43`; `MultTranspose` `45-48` → `46-49`; `Mult2` `51-56` → `52-56`; `MultTranspose2` `60-63` → `60-64`; `MfemWrapperSolver` comment-block `66-68` → `67-69`; `MfemWrapperSolver` body `67-134` → `70-134`; `pc` field `76` → `77`; `A` field `79` → `80`; flags block `83-94` (with sub-anchors `83/87/90/93`) → `84-94` (with sub-anchors `84/88/91/94`); `num_dropped_entries` `96` → `97`; `DropSmallEntries` decl `99` → `100`; ctor `102-109` → `103-110`; `GetSolver` `112` → `113`; setter block `115-122` → `116-123`; `SetInitialGuess` override `124-128` → `125-129`; `solver.cpp` `SetOperator<Operator>` `12-29` → `12-30`; `SetOperator<ComplexOperator>` `31-135` → `32-136`; `Mult<ComplexOperator>` `144-178` → `144-177`; `DropSmallEntries` def `180-208` → `179-207`; sign-flip line `172` → `173`; `ε²` threshold line `184` → `183`; MUMPS reorder-reuse block `187-203` → `186-202`. The remaining citations (`solver.hpp:21-22` for template+class declaration line pair, `solver.hpp:70-71`, `solver.hpp:73`, `solver.hpp:131`, `solver.hpp:133`, `solver.cpp:56-72`, `solver.cpp:138-142`, `iterative.hpp:25-115` (template-line-start convention), and the `jacobi.hpp:19` / `chebyshev.hpp:23` / `chebyshev.hpp:86` / `distrelaxation.hpp:30` / `gmg.hpp:31` / `blockprecond.hpp:32` / `ksp.hpp:42` siblings) were re-verified and left unchanged — they were already correct against source.

- **Finding 2**: Friction signal — dispatch-prompt framing was inaccurate (recurrence-2 since cycle-010 eps.cpp/feast.cpp drift; not currently in friction-ledger).
  - **Decision**: unrepairable (out of repair authority — not a CYCLE.md content issue; the report already adopted the corrected framing in §"Summary" and Open questions #1)
  - **Rationale**: This is a STAGING-log friction signal for the integrator-finalize phase to surface to meta-phase. The repairer cannot write to `scaffolding/friction-ledger.md` (only meta-phase has that authority), and cannot write to the cycle's STAGING.md (only integrator-per-report appends rows). The integrator-per-report should propagate this into its STAGING.md row's "friction-signals" column when this report is applied; meta-phase batch-2 review should consider naming the friction pattern.

- **Finding 3**: `verify-citation-range` skill not invoked (telemetry-level).
  - **Decision**: unrepairable (telemetry signal only; repair would require re-running the producing agent, which is not the repairer's authority)
  - **Rationale**: The skill-uptake observation is about producer-side behavior (what the layer-intro-author agent did vs should have done). The repairer cannot retroactively invoke the skill on behalf of the producer; the citation re-verification performed in Finding 1 is functionally equivalent (the repairer did manually what the skill would have done). Telemetry should flow to meta-phase via the critic's `skill-uptake-survey: warning` check in the frontmatter.

- **Finding 4**: `Solver<OperType>` class body range "20-64" understates the class-declaration line per sibling-chapter convention.
  - **Decision**: repaired
  - **Action**: Repaired to `21-65` (template line through closing-brace line). This matches the sibling-chapter convention used by `linalg-iterative-file.md` which cites `iterative.hpp:25-115` for `IterativeSolver` (line 25 is the `template <typename OperType>` line; line 115 is the closing `};`). Note: the critic suggested `22-65` (citing the `class Solver` declaration line rather than the template line); chose `21-65` instead because the sibling convention uses template-line-start.

- **Finding 5**: `DropSmallEntries` characterized as "non-templated-specialisation method definition" (awkward, could be misread).
  - **Decision**: repaired
  - **Action**: Replaced "non-templated-specialisation method definition" with "the single generic template definition (vs the per-`OperType` specialisations of `SetOperator` and `Mult` above)" in §"At a glance" (the bullet for `DropSmallEntries`) and with "single generic template method definition (vs the per-`OperType` template specialisations of `SetOperator` and `Mult`)" in §"`MfemWrapperSolver<OperType>` — the in-file concrete subclass". Both edits preserve the load-bearing observation (DropSmallEntries is the only generic template definition in `solver.cpp` while the other four cpp-side definitions are per-`OperType` explicit specialisations).

- **Finding 6**: `ksp.hpp:42` citation for preconditioner unique_ptr — critic claimed actual line 41.
  - **Decision**: not-needed
  - **Action**: Source re-verification confirms `ksp.hpp:41` is `std::unique_ptr<IterativeSolver<OperType>> ksp;` and `ksp.hpp:42` is `std::unique_ptr<Solver<OperType>> pc;`. The chapter's `ksp.hpp:42` for the preconditioner `pc` field is CORRECT. The critic's finding appears to have confused `ksp` (line 41) with `pc` (line 42); no repair action needed. Chapter unchanged. (This bears mentioning to the critic as a false positive — but repairer authority does not permit overriding the critic's checks; flagged here for integrator-per-report's awareness.)

### Unrepairable findings

- **Finding 2** (friction signal): out-of-repair-authority; routes to integrator-per-report's STAGING.md row (friction-signals column) and to meta-phase batch-2 review (potential new friction-ledger entry for "dispatch-prompt framing drift on linalg-file layer-intro-author dispatches" — recurrence-2 since cycle-010).
- **Finding 3** (skill-uptake telemetry): out-of-repair-authority; telemetry-only signal already captured in critic's `skill-uptake-survey: warning` frontmatter check, will flow to meta-phase batch-2.

## Suggested resolution

`overall_status: pass-after-repair`. The chapter's citation surface is now reconciled against source; the awkward "non-templated-specialisation" phrasing is replaced with clearer wording; the false-positive `ksp.hpp:42` finding is documented. The two unrepairable findings (friction signal and skill telemetry) are out-of-band; the integrator-per-report should:
1. Apply the proposed changes (new file `book/src/L0/linalg-solver-file.md`, `book/src/L0/index.md` row, `book/src/SUMMARY.md` row) — content is now citation-accurate.
2. Note the recurrence-2 dispatch-prompt framing drift signal in STAGING.md (friction-signals column) for meta-phase batch-2 review.

No follow-up agent required; this is ready for integration.
