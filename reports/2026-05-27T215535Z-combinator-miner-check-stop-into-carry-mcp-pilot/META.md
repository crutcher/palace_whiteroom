---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T22:10:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-27T22:25:00Z
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
overall_status: pass-after-repair
follow_up_agent: null
---

# META: verification of combinator-miner `check_stop_into_carry` reuse audit (MCP pilot retry)

## Critique

### Checks run

**citation-validity (warning):** The two load-bearing source citations are verified at the precise lines claimed.

- `palace/linalg/iterative.cpp:644-649` — verified: contains the 3-condition stop test on lines 644-649 (`converged = (beta < eps); if (converged || j + 1 == max_dim || it + 1 == max_it) { it++; break; }`) inside `GmresSolver<OperType>::Mult` (the function definition is at line 544 as cited).
- `palace/linalg/iterative.cpp:823-828` — verified: textually-identical disjunct (`converged = (beta < eps); if (converged || j + 1 == max_dim || it + 1 == max_it) { it++; break; }`) inside `FgmresSolver<OperType>::Mult` (function at line 734 as cited).
- `palace/linalg/iterative.cpp:418-465` CG non-instance — verified: loop guard is `for (; it < max_it && !converged; it++)` at line 427; convergence is `converged = (res < eps)` at line 463; `CheckDot` throw-on-divergence at lines 446, 462. The 2-condition characterization is accurate.
- `palace/linalg/operator.cpp:662-684` power iteration — verified: `while (it < max_it)` loop with `if (res < tol) break` inner test; the 2-condition characterization is accurate.
- `palace/linalg/nleps.cpp:589-650` Quasi-Newton — verified: `while (it < nleps_it)` outer guard at line 590; convergence-and-record-update at line 601 (`if (res < rtol)`); streak-counter divergence `if (diverged_it > 10)` at line 636. The 4-exit characterization is accurate.
- `palace/linalg/slepc.cpp:559-562, 1047-1050, 1398-1401` — verified approximate: actual `SlepcEPSSolverBase::SetMaxIter` is at lines 558-563 (cited 559-562 falls inside, slightly imprecise). The `EPSSetTolerances` call is at line 562; similar pattern at 1042/1050 (PEP) and 1394/1401 (NEP). All cited ranges are in-range but the start lines could be tightened by 1 line.
- `palace/linalg/arpack.cpp:231-233, 272` — verified: `SetMaxIter` is at lines 231-234 (cited 231-233 is within); `iparam[3] = 1; // Block size` is at line 271 (cited line 272 is `iparam[4] = 0; // Number of converged Ritz values`). The line 272 citation is in-range for the `iparam` block but the human-readable intent ("Block size" claim implicit) is one line off — minor slippage.
- The non-instance evidence sweep for chebyshev.cpp / distrelaxation.cpp returned zero hits (confirmed via independent search), consistent with the "fixed-degree polynomial smoother with no convergence test" claim.

`warning` only because of the minor slepc/arpack line-offset imprecisions; the load-bearing GMRES/FGMRES citations are exact.

**surface-or-evidence (pass):** This is an inspection-only dispatch with no surface mutation proposed. The "structural fingerprint" claims are anchored in directly-read source ranges (verified above), not inferred — every `Instance`/`Non-instance` carries a verified file:line range with quoted disjunct text or shape description. The defer-with-routing recommendation explicitly does NOT promote the helper; it routes the formalization to a future lifter dispatch. No retroactive-evidence-backfill problem.

**rotation-quality (pass — n/a):** Not applicable to this inspection-only dispatch. The report does not assert a new rotation; it audits the reuse-evidence for an already-proposed (cycle-008) speculative helper. The "identity-in-form caveat on the L3 side" paragraph correctly notes that GMRES/FGMRES twin reuse does not stress the helper's signature in any new dimension — this is a methodologically-sound observation, not a rotation claim.

**variant-axis-coverage (pass — n/a):** Not applicable to inspection-only audit. The variant-axis paragraph (Proposed combinator §) restates the cycle-008 abstractor's variant-axis declaration (predicate-disjunction members; carry codomain shape) verbatim; no new axes added or hidden.

**cross-reference-integrity (warning):** All named lowering-theme references resolve.

- `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md` exists and the cited §"Speculative L4 operators" section exists at line 156.
- `book/src/L4-L3/index.md` contains the rough-in row for `check_stop_into_carry` at line 162.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` exists and the §"Audit of cycle-002 identity-in-form claim" section exists.
- The cycle-008 abstractor report referenced (`abstractor:2026-05-27T180000Z-abstractor-gmres-inner-loop-iterate-while-migration`) exists in `reports/`.
- **However**: the report cites "the upstream gmres.md §L4 v0.6→v0.7 self-rotation" repeatedly (§Routing recommendation, §Substantive caveats) without path-qualifying which `gmres.md`. There are three `gmres*.md` files in `book/src/`: `concepts/gmres.md`, `spec/slices/gmres.md`, `L4-L3/gmres-inner-loop-iterate-while-migration.md`. Only `spec/slices/gmres.md` contains a §L4 v0.6 section (line 1012 — "L4 v0.6 — stop-witness extraction") and references a v0.7 (line 1106 — "a cleaner v0.7 would split the classifier signature"). The intended referent is unambiguously the slice file in context but the path is not stated. Minor reader-cost issue; not a broken link.

`warning` for the unqualified gmres.md references.

**edge-label-fidelity (pass):** No new edge label proposed in this report. The dispatch correctly identifies the routing edge as **lifter** (re-anchoring the existing cycle-008 theme against a firmed-up gmres.md §L4 v0.7 form), not **harvester** (which would author a new firm L4 entry at `book/src/L4/check-stop-into-carry.md`). The harvester-vs-lifter distinction is correctly applied: the helper itself is already a rough-in row in `L4-L3/index.md`; the cycle-011 work is re-anchoring the theme's LHS once the upstream slice settles, which is lifter authority per agent role spec. The cycle-planner directive ("do NOT schedule a harvester on `book/src/L4/check-stop-into-carry.md` until …") explicitly closes the loop on this.

**plan-kind-consistency (pass):** The report's declared shape is `combinator-miner` reuse-audit (inspection-only, one pattern per invocation per role spec). The work product matches: no `book/src/` mutation proposed, no new dep-map rows, no rotation claim — just a reuse-evidence ledger plus routing recommendation. The §Proposed changes section explicitly states "This report does NOT propose a new dep-map entry … This dispatch instead provides the reuse-evidence ledger." The out-of-scope-but-observed §CG `CheckDot` divergence-throw pattern is correctly surfaced as a drive-by under the relaxed problems/ bar, not co-mingled into the primary recommendation. Plan-kind shape is internally consistent.

**skill-uptake-survey (pass):** This is the **MCP codemap pilot retry** dispatch and the report's §"MCP codemap pilot evaluation" section is detailed: 14 MCP tool calls inventoried by tool type (`list_files` × 2, `search_text` × 7, `get_file_subtree` × 1, `read_range` × 4), zero permission-denied errors, qualitative comparison against vanilla `Grep`+`Read` workflow (call-count parity but qualitative advantages enumerated in 4 points), one ergonomic note on snippet-line-limit, and a forward-looking recommendation for cycle-010+ planner on which dispatch shapes benefit. This is exactly the meta-phase-decision-informing telemetry the pilot is supposed to produce. Pilot-evaluation completeness is unambiguously high.

### Issues found

1. **(citation-validity, low severity)** Minor line-offset imprecision in non-instance citations: `palace/linalg/slepc.cpp:559-562` should be `:558-563` (the `SetMaxIter` function); `palace/linalg/arpack.cpp:272` references `iparam[4]` (converged Ritz values count) rather than `iparam[3]` (Block size) — the intent appears to be "the iparam block at lines 268-273" but the precise line cited is one off from a natural anchor. Load-bearing GMRES/FGMRES citations at `:644-649` and `:823-828` are exact.

2. **(cross-reference-integrity, low severity)** The "gmres.md §L4 v0.6→v0.7 self-rotation" reference (used in §Routing recommendation and §Substantive caveats) does not path-qualify which `gmres.md`. Three candidates exist in `book/src/`; only `spec/slices/gmres.md` has a §L4 v0.6 section (line 1012) and v0.7 anticipation (line 1106). Context makes the referent unambiguous but the path should be explicit (e.g., `book/src/spec/slices/gmres.md §L4 v0.6`).

3. **(methodology-signal, observation only — no check failure)** The report identified that the dispatch brief cited `palace/linalg/eps.cpp` and `palace/linalg/feast.cpp` (both non-existent) when the actual eigensolver files are `arpack.cpp` / `slepc.cpp` / `nleps.cpp`. This is correctly flagged in §MCP codemap pilot evaluation (point 2) as a friction-signal — the MCP `list_files` call corrected the brief early. **However**: the report does NOT also surface this as a planner-dispatch-brief-drift friction signal for the meta-phase ledger, nor file it to `problems/` under the relaxed bar. Given the pilot-evaluation framing is meta-phase-decision-informing, the dispatch-brief drift is a separate friction signal (planner reads stale file inventory; MCP localization fixes it) worth flagging in scaffolding/friction-ledger.md by the next meta-phase. This is a candidate for repair (append a sentence to §"Friction-signal observations for meta-phase" or a drive-by problems/ filing) or surface to the cycle-010+ planner.

4. **(judgment-quality, observation only — no check failure)** The "GMRES/FGMRES sister-algorithm twinning" characterization is methodologically sound. The report explicitly notes (§Substantive caveats first bullet) that GMRES and FGMRES share a literature ancestor — "FGMRES is GMRES with right-preconditioning allowed to vary per iteration" — and explicitly downgrades the reuse-strength to "the lower edge" of the second-reuse criterion. The defer-with-routing verdict is correctly calibrated against this: not rejecting the reuse, not promoting the helper, routing to cycle-011 lifter dispatch with explicit conditions (a) FGMRES theme firms at the same callsite shape, OR (b) a non-`GmresSolverBase` Krylov consumer surfaces. This is the key judgment the task asks me to evaluate; my assessment is that the characterization is correctly calibrated and not over-claimed.

5. **(skill-uptake-survey, observation only — no check failure)** The MCP pilot evaluation is thorough but does not surface a candidate for the `scaffolding/skill-candidates.md` channel — e.g., a "localize-then-read discipline" skill that formalizes the list_files → search_text → get_file_subtree → read_range sequence the dispatch demonstrated. Given the §Recommendation-to-cycle-010+-planner paragraph already implicitly defines the procedure ("default localization path for combinator-miner / cross-cutter / lowering-verifier dispatches whose scope is 'audit pattern X across directory Y'"), a candidate row would make the heuristic concrete. Not a finding — surfaced for repairer consideration.

## Repair

### Fixes attempted

- **Finding 1 (citation-validity, low severity — slepc/arpack non-instance line-offset imprecision)**
  - **Decision**: repaired
  - **Action**: edited CYCLE.md §Supporting evidence "Non-instance evidence (eigensolver delegation)" bullet. Verified actual line ranges via Read:
    - `slepc.cpp:559-563` (`SlepcEPSSolverBase::SetMaxIter` body) — was cited `:559-562` (off by 1 on end-line); updated to `:559-563`.
    - `slepc.cpp:1047-1051` (`SlepcPEPSolverBase::SetMaxIter`) — was cited `:1047-1050`; updated to `:1047-1051`.
    - `slepc.cpp:1398-1402` (`SlepcNEPSolverBase::SetMaxIter`) — was cited `:1398-1401`; updated to `:1398-1402`.
    - `arpack.cpp:231-234` (`ArpackEigenvalueSolver::SetMaxIter`) — was cited `:231-233`; updated to `:231-234`.
    - `arpack.cpp:272` — verified that line 271 is `iparam[3] = 1; // Block size` and line 272 is `iparam[4] = 0; // Number of converged Ritz values`. The intent was the iparam block at 268-273 (including `iparam[2] = arpack_it` at line 270 — the actual maxiter slot for ARPACK). Updated bullet to `:271` with prose-clarification that the surrounding `iparam` block spans 268-273 and the maxiter slot is at line 270.
  - Repairer authority: small mechanical line-offset fix (within repair scope per role spec); no content authoring.

- **Finding 2 (cross-reference-integrity, low severity — unqualified `gmres.md` references)**
  - **Decision**: repaired
  - **Action**: two references path-qualified to `book/src/spec/slices/gmres.md` (the file with §L4 v0.6 at line 1012 and v0.7 anticipation at line 1106, per the critic's localization):
    - CYCLE.md §Summary (line 12): `"upstream gmres.md §L4 v0.6→v0.7 self-rotation"` → `"upstream `book/src/spec/slices/gmres.md` §L4 v0.6→v0.7 self-rotation"`.
    - CYCLE.md §Routing recommendation (line 72): `"upstream firm `gmres.md §L4 v0.7` form"` → `"upstream firm `book/src/spec/slices/gmres.md §L4 v0.7` form (currently still v0.6 inline; located at lines 1012 and 1106 of that slice)"`.
  - Repairer authority: mechanical path-qualification fix (broken-reference cleanup is in repair scope).

- **Observation (methodology-signal — dispatch-brief drift: eps.cpp/feast.cpp → arpack.cpp/slepc.cpp/nleps.cpp)**
  - **Decision**: repaired (lightweight surface)
  - **Action**: appended a bullet to CYCLE.md §"Friction-signal observations for meta-phase" flagging the dispatch-brief drift as a friction-ledger candidate at recurrence-1 (below promotion threshold but ledger-trackable). The bullet credits the MCP `list_files` call for catching the drift on first invocation, distinguishes it from the broader MCP-pilot payload, and explicitly routes the signal to the next meta-phase rather than enacting any ledger update from repair authority (meta-phase is the sole writer of friction-ledger.md per partition).

- **Observation (skill-uptake-survey — `localize-then-read` skill candidate)**
  - **Decision**: not-needed
  - **Rationale**: critic surfaced this as optional ("Not a finding — surfaced for repairer consideration") and the original task brief explicitly marked the skill-candidate filing as "appropriate but optional; the critic noted recurrence-1 is below threshold." The Recommendation-to-cycle-010+-planner paragraph in CYCLE.md already implicitly defines the procedure; deferring to either (a) a meta-phase batch-1 promotion decision or (b) a separate any-agent appendable filing in cycle-011 if the pattern recurs.

### Unrepairable findings

None. Both warning findings repaired mechanically; both observations addressed (one via lightweight CYCLE.md append, one deferred-as-optional per task brief).

## Suggested resolution

`pass-after-repair` — integrator may apply this report's routing recommendation (defer-with-routing to cycle-011 lifter dispatch; no `book/src/` mutation proposed). The slepc/arpack line offsets are now exact; the gmres.md references are now path-qualified to `book/src/spec/slices/gmres.md`; the dispatch-brief drift signal is now surfaced in CYCLE.md for the next meta-phase to assess.

Integrator notes:
- This is an inspection-only report (no proposed-changes block); `integrator-per-report` action is to set `integrated_at` frontmatter, append a row to STAGING.md noting the routing recommendation + the friction-signal flag, and (optionally) append an open-question to `scaffolding/open-questions.md` tracking the cycle-011 lifter dispatch condition ("lifter on `gmres-inner-loop-iterate-while-migration` after `book/src/spec/slices/gmres.md` §L4 v0.7 firms").
- The friction-ledger update for "cycle-planner stale-file-inventory drift" is meta-phase work, not integrator-per-report work (meta-phase is sole writer of friction-ledger.md).
- The `localize-then-read` skill candidate filing remains optional and is not blocked by this repair.
