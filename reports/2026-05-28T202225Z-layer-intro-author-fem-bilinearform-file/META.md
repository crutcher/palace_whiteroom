---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T20:38:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-28T20:52:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of L0 `fem-bilinearform-file` reference note

## Critique

### Checks run

**citation-validity — warning.** Spot-checked all 9 anchor ranges against the source via `palace-codemap` (`get_symbol_def` + `read_range`). Both class decls verified exactly: `BilinearForm` `bilinearform.hpp:25-91`, `DiscreteLinearOperator` `bilinearform.hpp:95-132`. All cpp method-body anchors verified accurate to the line: `AssembleQuadratureData` 15-25, `BilinearForm::PartialAssemble` 27-107 (mesh-check 31-32, op-construct 37-46, OMP loop 51-101, domain 61-79, boundary 80-99, Finalize 104 — all confirmed), `FullAssemble` 109-113, `Assemble(bool)` 141-151, hierarchy `Assemble` 153-201 (square-check 158-161, Coarsen-reuse 170-180, per-level 186-198 — confirmed), `DiscreteLinearOperator::PartialAssemble` 203-282 (interp-basis ~237, sub-op+transpose 242, dof-multiplicity 258-281 — confirmed). No line-drift defect of the cycle-013/014 kind. **One content (not range) defect**: §`Assemble` — the report attributes the `order + 1` historical quirk to `L2_FECollection` ("L2_FECollection reports order+1, so it subtracts back"), but the **source comment at `bilinearform.cpp:121-123` names `RT_FECollection`** as the collection that returns `order + 1` for historical reasons. The code's `dynamic_cast` does target `L2_FECollection` (so the runtime behavior the report describes is what the code does), but the prose mis-paraphrases the cited comment's attribution. The `115-139` range for the `UseFullAssembly` helper is slightly loose (the anonymous namespace + both overloads span ~115-137) but in-range.

**surface-or-evidence — pass.** New-file L0 reference-note authoring, not a refinement of an existing operator/theme. No rotation_claim required; this is descriptive L0 surface backed by source citations throughout. Not applicable in the refinement sense.

**rotation-quality — pass.** No L_{n+1}→L_n rotation asserted; this is L0 ground-truth. The "Notes for higher layers" section forward-flags lifts (PA/FA dual collapses to a variant axis at L1, integrator-fold → L2 `Σ_i integ_i`) as speculative upward context, correctly framed as notes not as a landed rotation. Not applicable to L0 reference-note shape.

**variant-axis-coverage — pass.** The orthogonal axes are explicitly enumerated and covered: partial-vs-full assembly (the load-bearing dual), domain-vs-boundary integrators, single-space-vs-mixed (`SymmetricOperator` vs `Operator`), `BilinearForm` vs `DiscreteLinearOperator`, single-level vs FE-space-hierarchy `Assemble`, and the `set` vs accumulate flag distinguishing the two classes' `FullAssemble`. The multigrid `Assemble` square-form restriction is noted. No hidden branch found in the read.

**cross-reference-integrity — warning.** All four "Referenced from" slugs and inline `[link]`s point to plausible L0 chapter files (`linalg-rap-file`, `par-types-single-rank-reading`, `transparent-vs-load-bearing-tricks`, `preconditioner-classes-overview`). **Inconsistency**: the body text at the `FullAssemble` paragraph links `[libceed/operator.cpp](./linalg-operator-file.md)` — a slug (`linalg-operator-file`) that does NOT yet exist (the bundle-6 #5 candidate this report proposes for cycle-016) AND is mislabeled (`libceed/operator.cpp` lives under `fem/`, not `linalg/`). This is a forward-reference to an unwritten chapter under an inconsistent slug; it will render as a dead link until #5 lands. The `rap.cpp:100` callee relationship is correct (verified `BilinearForm::FullAssemble` is the `rap.cpp:100` callee per the report's own `search_text`).

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label carried; pure L0 file note. Not applicable.

**plan-kind-consistency — pass.** Declared shape is an L0 reference-note bundle chapter; content matches. The FOCUSED-not-split decision is sound: 420 total lines (hpp 136 + cpp 284, both verified by the read extents) is well below the rap.cpp ~979 split threshold, and the 9 anchors fit one coherent chapter without transcription. Single-rank reading of `Par*`/libCEED-parallel/`HypreCSRMatrix` is applied and MPI/OMP is flagged once (not re-flagged per method) per directive. Load-bearing assembly path (`UseFullAssembly` order-threshold dispatch, dof-multiplicity averaging, multigrid coarsening) is correctly distinguished from boilerplate forwarders and the `AssembleQuadratureData` setup hook (explicitly deferred to a future `fem/integrator` chapter).

**skill-uptake-survey — warning.** The report shape — bundle L0 chapter with 9 cited ranges + a co-located `index.md`/`SUMMARY.md` registration via `[old]`/`[new]` edit blocks — is exactly the cycle-013/014 L0-bundle pattern that has now recurred ≥3 times. No skill is referenced as invoked (e.g. `verify-citation-range` for self-checking the 9 anchors, `summary-md-surgical-insert` for the SUMMARY/index edits). Surfacing telemetry only: this recurring L0-bundle-chapter procedure (size-gate → focused-vs-split decision → N-anchor harvest → index+SUMMARY surgical insert → bundle-#next ranking) is a skill-candidate worth crystallizing. Non-blocking.

### Issues found

1. **`L2_FECollection` vs `RT_FECollection` attribution (content defect)** — `book/src/L0/fem-bilinearform-file.md`, §"`Assemble` — the PA/FA policy dispatch", clause "`L2_FECollection` reports `order + 1`, so it subtracts back". The source comment at `bilinearform.cpp:121-123` attributes the historical `order + 1` quirk to `RT_FECollection`, not `L2_FECollection`. The `dynamic_cast` in the code targets `L2_FECollection`, so the runtime claim is consistent with the code, but the prose mis-cites the comment's named collection. Severity: low (factual paraphrase of a cited comment is off; does not invalidate the PA/FA logic claim).

2. **Dead + mislabeled forward link** — `book/src/L0/fem-bilinearform-file.md`, §"The two assembly modes", the `FullAssemble` bullet: `[libceed/operator.cpp](./linalg-operator-file.md)`. The target slug `linalg-operator-file` does not exist yet (it is the proposed bundle-6 #5 candidate) and the path prefix is wrong — `operator.cpp` is at `palace/fem/libceed/operator.cpp`, so a future slug should read `fem-libceed-operator-file` / `libceed-operator-file`, not `linalg-operator-file`. Severity: low-medium (renders as a broken link on build until #5 lands; the slug naming pre-commits a wrong prefix the integrator should not propagate). Candidate: drop the link target (leave bare text) or align the slug to the eventual `fem/libceed/` location.

3. **Loose helper anchor range** — `book/src/L0/fem-bilinearform-file.md`, Evidence list, `bilinearform.cpp:115-139` for `UseFullAssembly`. The anonymous namespace + both overloads span ~115-137; 139 overshoots by ~2 lines into the following `BilinearForm::Assemble`. Severity: trivial (in-range, no false claim).

4. **No skill-invocation reference** — whole report. Recurring L0-bundle-chapter shape (≥3rd occurrence) with no cited skill use (`verify-citation-range`, `summary-md-surgical-insert`). Severity: telemetry-only, non-blocking.

(Write-authority confirmed: `git status book/` clean — no dispatch-phase `book/` mutation; index/SUMMARY changes are correctly proposed-changes `[old]`/`[new]` blocks in CYCLE.md, not applied.)

## Repair

### Fixes attempted

- **Finding**: citation-validity — §"`Assemble`" prose (and the matching Evidence-list line) attribute the `order + 1` historical quirk to `L2_FECollection`, but the cited source comment names `RT_FECollection`.
  - **Decision**: repaired
  - **Action**: `CYCLE.md` §"`Assemble` — the PA/FA policy dispatch" + Evidence list. Verified the source via `palace-codemap read_range palace/fem/bilinearform.cpp:115-139`: the comment at `bilinearform.cpp:121-123` reads *"MFEM's RT_FECollection actually already returns order + 1 for GetOrder() for historical reasons."* Corrected both the prose paraphrase and the Evidence line to attribute the `order + 1` quirk to `RT_FECollection`, citing the comment range (121-123). The `dynamic_cast`-guarded `+ 1` normalization (126-131) is retained as the helper's correction. Mechanical paraphrase-fix; the PA/FA dispatch logic claim was unaffected.

- **Finding**: cross-reference-integrity — §"The two assembly modes", `FullAssemble` bullet: the forward link `[libceed/operator.cpp](./linalg-operator-file.md)` is dead (slug not yet authored) and mislabeled (`linalg-` prefix; the file is under `fem/libceed/`). A dead markdown link breaks `cargo make book`.
  - **Decision**: repaired
  - **Action**: `CYCLE.md` §"The two assembly modes" → `FullAssemble` bullet. Converted to a **plain-text reference** to `palace/fem/libceed/operator.cpp` (the not-yet-authored bundle-6 #5 candidate), removing the markdown link target entirely. Chose plain-text over a corrected slug because the target chapter does not yet exist — any link target would render dead and break the build; the Open-questions bundle ranking already records the #5 candidate, so the reference is preserved in prose. Also removed the wrong `linalg-` prefix implication.

### Unrepairable findings

None. The two `warning` content/cross-ref defects were both mechanical (a cited-comment paraphrase fix and a dead-link conversion). The `skill-uptake-survey` warning is telemetry-only (non-blocking) — acknowledged, not repaired; the loose `115-139` helper anchor range was flagged trivial/in-range by the critic and needs no edit. Write-authority confirmed clean (proposed-changes blocks only). The bundle-6 #5 ranking OQ (`palace/fem/libceed/operator.cpp`, with `fespace` alternative) is recorded in CYCLE.md §"Open questions / caveats" and survives the link-fix as a plain-text reference.

## Suggested resolution

`ready` — both warnings repaired surgically; no substantive authoring required. Note for the integrator: the `FullAssemble` reference to `palace/fem/libceed/operator.cpp` is intentionally plain text (no link) until the bundle-6 #5 chapter lands; when cycle-016 authors that chapter, re-link it then. The bundle-6 #5 ranking OQ should be promoted to the ledger.
