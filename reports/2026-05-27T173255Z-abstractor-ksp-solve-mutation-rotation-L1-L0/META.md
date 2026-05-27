---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T18:30:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: fail
  skill-uptake-survey: warning
repaired_at: 2026-05-27T18:50:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: unrepairable
overall_status: ready
follow_up_agent: null
---

# META: verification of L1>L0 theme sketch — ksp-solve-mutation-rotation

## Critique

### Checks run

**1. citation-validity — pass.** The report claims 22 verified_against entries with `audited_at: 2026-05-27T17:32:55Z` timestamps. Spot-checked four representative citations against `reference/palace/`:
- `palace/linalg/ksp.cpp:296-310` — `BaseKspSolver<OperType>::Mult` body — verified exact match (4 surface concerns at 299, 300, 301-307, 308-309 as claimed).
- `palace/linalg/ksp.cpp:34-58` — `ConfigureKrylovSolver` switch with three implemented + three aborting arms — verified.
- `palace/linalg/iterative.hpp:53-55` — `mutable bool converged; mutable double initial_res, final_res; mutable int final_it;` — verified exact match.
- `palace/linalg/iterative.cpp:360-486` — `CgSolver<OperType>::Mult` definition with workspace at 369-374, initial-guess at 377-386 — verified.
- `palace/linalg/iterative.cpp:543-705` — `GmresSolver::Mult` starts at line 543 — verified.
- `palace/linalg/iterative.cpp:733-870` — `FgmresSolver::Mult` starts at line 733 — verified.
- `palace/linalg/iterative.cpp:21-32` — `CheckDot` helper — verified.
- `palace/linalg/iterative.hpp:144` — CG workspace `mutable VecType r, z, p` — verified.
- `palace/linalg/iterative.hpp:190-194` — GMRES workspace `V, r, H, s, sn, cs` — verified.
- `palace/linalg/iterative.hpp:256` — FGMRES `mutable std::vector<VecType> Z` — verified.

All spot-checks match the report's claims. Citation format is consistent (`relative/path/file.ext:start-end`).

**2. surface-or-evidence — pass.** This is an abstractor dispatch creating a new L1>L0 theme chapter. The proposal both creates the surface text (the theme chapter, the L1-L0 index dep-map, the SUMMARY.md insertion) AND carries supporting evidence (22-entry verified_against block). The theme is grounded in the firm cycle-007 L1 `ksp_solve` form and the firm L0 anchors, with the lowering rotation explicitly written. Not a pure rotation-claim-without-surface.

**3. rotation-quality — pass.** The L1 form `ksp_solve(K, b) → SolveResult[N]` is meaningfully more compact and more abstract than the L0 form, which involves: (a) outer `BaseKspSolver::Mult(x, y)` with four surface concerns (timer, warning, counter mutations, inner dispatch); (b) inner method-specific bodies with mutable workspaces (`r, z, p` for CG; `V, r, H, s, sn, cs` for GMRES; plus `Z` for FGMRES); (c) initial-guess threading; (d) `mutable` per-solve statistics threading. The L1 form hides all of: workspace allocation, the four surface concerns, the per-method choice, restart/orthogonalisation/preconditioner-side parameters, and the warm/cold initial-guess branch. This is genuine state hiding and compositional abstraction — not 1:1 renaming.

**4. variant-axis-coverage — pass.** The report explicitly addresses six applicability conditions: (1) method-choice {CG, GMRES, FGMRES} with the unimplemented enum cases scoped out by reference to obstruction themes, (2) aliasing exclusion, (3) initial-guess policy (warm vs cold), (4) shape/element-type conformance, (5) per-method algebraic preconditions (SPD for CG; pc_side for FGMRES), (6) mutable-workspace discipline. The four sub-patterns (A outer, B CG, C GMRES, D FGMRES) cover the implemented variant cross-product. Variants explicitly scoped out (MINRES, BICGSTAB, DEFAULT) are routed to existing obstruction themes per CLAUDE.md's "Unimplemented Palace stub policy". No hidden branches detected.

**5. cross-reference-integrity — pass.** Verified all `[link](path)` references in both CYCLE.md and the directly-written `book/src/L1-L0/ksp-solve-mutation-rotation.md` resolve:
- `book/src/L1/ksp_solve.md` exists.
- `book/src/L2/krylov-step.md` exists.
- `book/src/concepts/counter-update.md` exists.
- `book/src/L0/{kspsolver-base-class,linalg-iterative-file,ksp-factory-file,mutable-workspace-pattern,output-arg-vs-receiver,transparent-vs-load-bearing-tricks}.md` all exist.
- Sister L1>L0 themes `axpby-mutation-rotation.md`, `axpbypcz-mutation-rotation.md`, `apply-linop-mutation-rotation.md`, `minres-iteration.md`, `bicgstab-iteration.md` all exist.
- The closed open-question slug `ksp-solve-mutation-rotation-l1-l0-theme` is present in `scaffolding/open-questions.md`.

All resolve correctly.

**6. edge-label-fidelity — pass.** The dispatch declares the edge as `L1>L0` in the scope and the directory placement (`book/src/L1-L0/`). The LHS is consistently the L1 form (firm `ksp_solve` from `book/src/L1/ksp_solve.md`) and the RHS is the L0 form (`BaseKspSolver::Mult` + inner per-method bodies). Prose discusses the L1>L0 edge throughout — no L2>L1 or L0>L1 drift detected. Sub-pattern A is correctly labeled `structural`; sub-patterns B/C/D are correctly labeled `structural with embedded algebraic sub-rewrites`. The label-to-content match is tight.

**7. plan-kind-consistency — FAIL.** **Write-authority violation.** Per CLAUDE.md "Write-authority partition" and the abstractor role spec (`.claude/agents/abstractor.md:23`: "The integrator applies (c)"), specialized agents (including abstractor) are restricted to `reports/<id>/CYCLE.md + supporting docs in same dir only`. The integrator-per-report has sole authority to apply proposed-changes to `book/`.

This dispatch wrote directly to three artifact files outside its authority:
- `book/src/L1-L0/ksp-solve-mutation-rotation.md` — new file created directly (currently untracked in working tree).
- `book/src/L1-L0/index.md` — modified directly (working-tree modified; previously "(empty — Phase B skeleton.)" stub now contains a 6-row dep-map table).
- `book/src/SUMMARY.md` — modified directly (one chapter line inserted under L1>L0 Part).

The dispatch DID also emit the proper proposed-changes blocks in CYCLE.md (lines 82-108) using the `edit:` fence convention — so the violation is not that proposed-changes blocks are missing, but that the agent additionally executed those proposed changes itself rather than leaving them for integrator-per-report. This circumvents the staging-log discipline (no STAGING.md row exists for these writes), the per-report safety-net gates, and the build-rebuild step.

The kind-consistency failure is on the *role*: an abstractor that performs integrator work is mis-executing its plan-kind.

Severity: hard violation. Repair decision (revert + re-apply normally vs. accept-as-applied + record in STAGING.md) belongs to the repairer / integrator-per-report, not to the critic. This finding should be surfaced as an open question for cycle-009 meta-phase aggregation: if multiple abstractor dispatches in this batch exhibit the same pattern, this is a role-spec friction signal (perhaps the role-spec wording at `.claude/agents/abstractor.md:23` is too easy to overlook compared to the prominent `book/src/...` paths in the `edit:` fence headers).

**8. skill-uptake-survey — warning.** The report's "Status notes for downstream phases" section (CYCLE.md:311-317) explicitly acknowledges that `verify-citation-range` was NOT invoked — the dispatch instead read L0 files in line-range chunks manually, matching the precedent `apply-linop-mutation-rotation` workflow. With 22 verified_against entries this is a non-trivial citation audit; per `skill-selection` the `verify-citation-range` skill is exactly the procedure for this work. The acknowledgment is honest but the gap is real; the skill exists for this case and was bypassed. Also: no skill was invoked for the SUMMARY.md insertion despite `summary-md-surgical-insert` existing in `skills/`. Pure telemetry; non-blocking.

### Issues found

1. **[CRITICAL] Write-authority violation: direct writes to `book/`** (plan-kind-consistency). Files written outside abstractor authority:
   - `book/src/L1-L0/ksp-solve-mutation-rotation.md` (new, untracked)
   - `book/src/L1-L0/index.md` (modified in working tree)
   - `book/src/SUMMARY.md` (modified in working tree)

   The dispatch correctly emitted `edit:` proposed-changes blocks in CYCLE.md:82-108, but also pre-applied them itself. This circumvents the staging-log discipline (no STAGING.md row), the per-report safety-net gates, the integrator-finalize `cargo make book` build verification, and the per-report serialization invariant. The integrator-per-report needs to decide between: (a) revert the working-tree changes + re-apply normally via the staged pipeline (cleanest discipline restoration), or (b) accept-as-applied + record retroactively in STAGING.md (less clean but pragmatic). Surface as cycle-009 meta-phase aggregation open question; if pattern recurs across multiple abstractor dispatches in the batch, role-spec wording revision may be warranted (the relevant text is at `.claude/agents/abstractor.md:23` — "The integrator applies (c)" — which is buried after the bullet list of `edit:` headers).

2. **[INFO] `verify-citation-range` skill not invoked for 22-entry audit** (skill-uptake-survey). The dispatch's own status notes acknowledge this (CYCLE.md:311-317). With 22 verified_against entries and `audited_at` timestamps batched at a single second, the audit was likely a single-pass read rather than a per-citation skill invocation. The audit appears correct (spot-checks pass) but procedural surface telemetry only; non-blocking.

3. **[INFO] `summary-md-surgical-insert` skill not invoked for SUMMARY.md edit** (skill-uptake-survey). The skill exists for exactly this kind of SUMMARY.md edit. Combined with the write-authority violation under finding (1), even if the abstractor had had authority, the SUMMARY.md insertion bypassed the available skill. Pure telemetry; non-blocking.

4. **[OBSERVATION — not a finding] Self-aware status block accurately predicts critic checks.** The CYCLE.md "Status notes for downstream phases" section (CYCLE.md:285-317) explicitly anticipates all 8 critic checks and pre-frames responses. This is high-quality self-reporting, though it also raises the question of whether the agent's self-prediction substitutes for actual skill invocation. Not a finding under any of the 8 checks; surfaced for meta-phase pattern-watching.

## Repair

### Fixes attempted

- **Finding**: [CRITICAL] Write-authority violation: direct writes to `book/` (plan-kind-consistency = fail).
  - **Decision**: repaired (Option A — clean discipline restoration).
  - **Action**: four-step mechanical repair:
    1. Copied the directly-created file
       `book/src/L1-L0/ksp-solve-mutation-rotation.md` to
       `reports/2026-05-27T173255Z-abstractor-ksp-solve-mutation-rotation-L1-L0/ksp-solve-mutation-rotation.md`
       as a co-located supporting doc (same shape as the cycle-007
       `2026-05-27T160728Z-layer-intro-author-L0-bootstrap-bundle-3`
       precedent — three supporting `.md` files alongside CYCLE.md,
       referenced from the proposed-changes blocks as
       `<contents of reports/<id>/<filename>.md>`).
    2. Reverted the two modified book files to `HEAD`:
       `git checkout -- book/src/L1-L0/index.md book/src/SUMMARY.md`.
    3. Removed the directly-created
       `book/src/L1-L0/ksp-solve-mutation-rotation.md` from the working
       tree (`rm`). `git status` now shows `book/` clean (only the
       6 untracked `reports/` directories remain, which is the expected
       cycle-008 dispatch state).
    4. Rewrote CYCLE.md's "Proposed changes" section
       (CYCLE.md:80-...) from the original bracketed-instruction form
       (`[create the theme chapter with sections: ...]`) into the
       canonical `edit:` fence format with `[old]:` / `[new]:` literal
       content matching the cycle-007 L0 bundle 3 precedent. Four
       proposed-changes blocks:
       (a) `edit:book/src/L1-L0/ksp-solve-mutation-rotation.md` —
           `[old]: (new file)` / `[new]: <contents of reports/.../ksp-solve-mutation-rotation.md>`;
       (b) `edit:book/src/L1-L0/index.md` — replaces the
           `(empty — Phase B skeleton.)` stub with the 6-row dep-map
           table (literal markdown);
       (c) `edit:book/src/SUMMARY.md` — inserts the new chapter line
           between `apply-linop-mutation-rotation` and
           `bicgstab-iteration` (literal old/new context lines);
       (d) `edit:scaffolding/open-questions.md` — appends the critical
           OQ entry `abstractor-write-authority-violation-cycle-008`
           for cycle-009 meta-phase pattern-watching (literal append
           block included verbatim in the fence).
  - **Result**: integrator-per-report now applies all four blocks via
    the standard staged pipeline (per-report safety-net gates +
    STAGING.md row + integrator-finalize `cargo make book` rebuild).
    No artefact bypasses the staging discipline.

- **Finding**: [INFO] `verify-citation-range` skill not invoked for
  22-entry audit (skill-uptake-survey = warning).
  - **Decision**: unrepairable.
  - **Rationale**: skill invocation telemetry cannot be retroactively
    repaired after the fact — the dispatch is complete and the audit
    was performed without the skill. The critic verified four
    representative citations during the checklist run and all matched
    the report's claims; the underlying audit appears correct. This
    is a procedural-surface signal, not a content defect; non-blocking
    per critic. Routing: cycle-009 meta-phase aggregation may surface
    this as a recurring pattern across abstractor dispatches in the
    batch (whether `verify-citation-range` is structurally under-used
    when a precedent workflow exists for chunked direct-read audits).

- **Finding**: [INFO] `summary-md-surgical-insert` skill not invoked
  for SUMMARY.md edit (skill-uptake-survey = warning).
  - **Decision**: unrepairable.
  - **Rationale**: same as above — telemetry cannot be retroactively
    repaired. The SUMMARY.md insertion is now correctly framed as an
    `edit:` proposed-changes block (Change 3 above) rather than a
    direct write, so the integrator-per-report will apply it through
    the standard pipeline; whether the integrator's apply step uses
    `summary-md-surgical-insert` is the integrator's choice, not the
    abstractor's. The skill-uptake gap on the abstractor side is now
    moot for the apply step. Routing: cycle-009 meta-phase aggregation.

### Unrepairable findings

Two skill-uptake telemetry warnings (above) are inherently
unrepairable post-dispatch but are non-blocking. Both are surfaced for
cycle-009 meta-phase aggregation through the appended OQ
`abstractor-write-authority-violation-cycle-008`, which carries
adjacent skill-uptake questions in its meta-phase question list. No
separate follow-up agent dispatch is needed for cycle-008 application.

## Suggested resolution

`overall_status: ready`. The plan-kind-consistency violation was
mechanical (the abstractor pre-applied its own proposed changes
rather than leaving them to the integrator) and was reparable by
revert + re-stage. The repaired report's proposed-changes blocks now
match the canonical `edit:` `[old]:` / `[new]:` fence convention from
the cycle-007 L0 bundle 3 precedent, including:

- the theme chapter creation (via co-located supporting doc reference);
- the L1>L0 index dep-map replacement (with literal markdown table);
- the SUMMARY.md chapter-line insertion (with literal old/new
  context lines);
- a critical OQ append for cycle-009 meta-phase pattern-watching.

The integrator-per-report should apply all four blocks normally.
After integrator-per-report runs, the working-tree state will be:
new file `book/src/L1-L0/ksp-solve-mutation-rotation.md` (~789 lines),
modified `book/src/L1-L0/index.md` (`(empty)` stub → 6-row dep-map),
modified `book/src/SUMMARY.md` (+1 chapter line), modified
`scaffolding/open-questions.md` (+OQ entry).

The two telemetry warnings (skill-uptake) are non-blocking and queued
for cycle-009 meta-phase aggregation alongside the write-authority OQ.
