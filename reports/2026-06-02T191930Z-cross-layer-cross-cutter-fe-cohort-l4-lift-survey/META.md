---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T201500Z
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
repaired_at: 2026-06-02T203000Z
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

# META: verification of cross-layer survey — fe-cohort-l4-lift-survey

## Critique

### Checks run

**citation-validity — warning.** Sampled the load-bearing citations on-disk. **Palace source (codemap `read_range`, recurrence-6 direct on-disk reads, not `--anchor`):** `bilinearform.cpp:75-76` is the domain `integ->Assemble(...)` call+continuation; `:77` is `op->AddSubOperator(sub_op)`; `:95-96`/`:97` are the boundary-branch twins; `:104` is `op->Finalize()` — all confirmed exact. `libceed/operator.cpp:455` is the `CeedOperatorFullAssemble` function-open line — confirmed. **The one drift:** the report (Summary, finding (ii), Supporting-evidence) gives the `CeedOperatorFullAssemble` span as `455-523` and states "close brace at `:523`". On-disk the function body's `return mat;` is at `:521` and the closing `}` is at `:522`; line `:523` is blank and `:524` begins the next function (`CeedOperatorCoarsen`). The true END is `:522`, so the cited END is **off-by-one (+1, span over-runs into the trailing blank line)**. This is the only mechanical citation error and it is non-load-bearing (the span still correctly brackets the function; the meaning-read holds). **Artifact-side citations (on-disk `Read`):** `book/src/L1/fe_assemble.md:60-62` shows the `foldr` (line 61) + Σ (line 62) + signature (line 60) — the Summary's `:60-61` and finding-(ii)'s `:60-62` both land inside the foldr block, OK. `L4/index.md:24` = `OpParams`/`readonly` variant-absorption, `:39` = `eigsolve` `eigen_iterate` opaque marker, `:40` = `fold_solve` `time_step_op`, `:66` = the 13-of-18 no-L4-by-design line — all confirmed exact (see the dedicated sub-claim check below). `assemble_frequency_operator.md:43-49` = the `linear_combination` operand-category form; `eliminate_rhs.md:54-57` = the `axpy`+`apply_linop`+pin composition (the report writes `set_subvector`; the actual primitive is `set_essential`, a benign naming paraphrase of the same pin-set, not a citation error); `weak_form_term.md:25-31` = the inert "specification of WHICH contribution" element-type framing. All sampled artifact citations are accurate. The L1 cohort citations not individually re-opened (`fe_space.md:92-107`, `fe_collection.md:28-33`, `essential_dofs.md:39-58`, `eliminate_essential_bc.md:80-84`) are consistent in shape with the entries and were not flagged.

**surface-or-evidence — pass.** This is an observation-only survey; it modifies no operator/theme surface, so the refinement-surface gate does not bite. The classification claims (the three-way disposition table, finding (i)) are each tied to a positive artifact or source anchor: `fe_assemble` as foldr → `fe_assemble.md:61`; the libCEED leaf as opaque → `bilinearform.cpp:75-76`/`libceed/operator.cpp:455-523` + the existing `L1-L0/fe-assemble-libceed-boundary-obstruction` filing (confirmed on disk); `assemble_frequency_operator` through `linear_combination` → `:43-49`; `weak_form_term` inert → `:25-31`. Evidence-grounded throughout.

**rotation-quality — pass.** Not applicable to a coverage-gap survey in the strict sense (it asserts no L_{n+1}→L_n rotation as its own product), but the survey's structural claim — that `fe_assemble` rises as an L4 `assemble`-fold combinator with the libCEED leaf lifted to a `readonly` opaque input and the term list to the calculus list type — is a genuine abstraction step (state-hiding + leaf-opacification), not a 1:1 rename, and the survey is explicit (finding (ii), Anti-mirror guard) that this is NOT a degenerate L1→L2 mirror. The mining-gate step-3 over-unification guard (map-not-fold; concatenation-homomorphism HOLDS, distinguishing it from `fold_solve`) is correctly honored. No renaming-only rotation asserted.

**variant-axis-coverage — pass.** The PA/FA performance dual is explicitly scoped as absorbed inside `fe_assemble`'s assembly-representation variant axis (`fe_assemble.md:107-110`, the `pa_order_threshold` selector), so it does not surface as a separate stoppable entry — a correct variant-absorption call, not a hidden branch. The domain/boundary two-list split is addressed (single concatenated term list, not a structural break). The map-vs-fold axis is flagged in Open-questions. No orthogonal variant axis is left silently uncovered.

**cross-reference-integrity — pass.** All referenced slugs resolve on disk: the L4 inventory (`ls book/src/L4/`) matches the report's claimed inventory exactly (chebyshev, eigsolve, fold_solve, index, iterate-while, iterate-while-with-prev, krylov-step, ksp_solve, solve_family — no FE entry); `skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md` exists; `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md` exists; the eight L1 cohort entries are all named with real filenames. No dead references. (Build-readiness firm-body-inside-fence guard: no `book/` proposed-changes blocks at all — observation-only — so the guard no-ops.)

**edge-label-fidelity — pass.** The survey's edges (L1↔L4 climb; the `assemble`-fold as L4 combinator; the L4>L3 dissolution it recommends for c068) are each discussed in matching prose. The "L1→L2 rung is identity-skip / L4 rung still owed" framing correctly distinguishes the adjacent edges it names. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared an observation (coverage-gap survey); content shape matches — it proposes NO `book/` changes, authors nothing, and routes all landings to c068+ dispatches. Confirmed observation-only: §"Open questions / caveats" closes with "Survey authored nothing to `book/`," the Recommendation section is a dispatch-ranking not a landing, and there is no proposed-changes block. Correct kind classification.

**skill-uptake-survey — pass.** The survey's shape (a cross-pipeline combinator-rise claim) implies the `disciplined-cross-pipeline-combinator-mining-gate` skill, and the report explicitly walks all four gate steps (finding (ii)) and cites the skill by name in the recommendation + supporting-evidence. The skill exists on disk. Uptake surfaced; telemetry positive.

### Issues found

1. **`CeedOperatorFullAssemble` END line off-by-one (+1).** Where: Summary (`libceed/operator.cpp:455-523`), finding (ii) (`:455-523`, the COO→CSR materialization), and Supporting-evidence ("the hint `:455` is the function-open line, confirmed; close brace at `:523`"). On-disk the function's closing `}` is at `:522` (`return mat;` at `:521`; `:523` is blank, `:524` opens `CeedOperatorCoarsen`). The cited END over-runs by one into the trailing blank line; correct span is `455-522`. Severity: **low** (non-load-bearing — the span still brackets the function, the function-open `:455` is exact, and the meaning-read is unaffected). Candidate for a mechanical END-line correction `523 → 522` in the three occurrences.

2. **`eliminate_rhs` primitive name paraphrase (`set_subvector` vs on-disk `set_essential`).** Where: row 6 of the finding-(i) table, finding (iii), and Supporting-evidence describe the composition as `apply_linop` + `axpy` + `set_subvector` pin. The on-disk `eliminate_rhs.md:54-57` shows the third primitive as `set_essential(b', pin)` (with `restrict_essential` on the input side). Severity: **very low / informational** (the pin-set semantics are faithfully described; this is a primitive-name paraphrase, not a wrong citation — the cited line range is correct). Noted for fidelity, not a required fix.

No other issues. The sub-claim that `book/src/L4/index.md:66` asserts "13-of-18 BLAS-1 / elementwise / smoother L3 operators remain no-L4-by-design" is **confirmed verbatim on-disk** (line 66 reads: "The 13-of-18 BLAS-1 / elementwise / smoother L3 operators remain no-L4-by-design (their L4 form would add no calculus beyond their firm L3 rendering)…"). The survey's reading that this line over-claims by lumping combinators (`linear_combination`/`inner_product`) with the pure-accelerated leaves is a substantive directive-2 interpretation, not a citation error — the line genuinely makes the blanket claim the sub-observation re-examines, so the citation is accurate and the sub-finding is well-grounded against it.

## Repair

### Fixes attempted

- **Finding (Issue 1): `CeedOperatorFullAssemble` END line off-by-one (+1).** The critic flagged the report's `palace/fem/libceed/operator.cpp:455-523` span (Summary, finding (ii), Supporting-evidence) as over-running by one, claiming the close brace is on-disk at `:522` (`return mat;` at `:521`, `:523` blank, `:524` opens the next function).
  - **Decision**: not-needed (report span confirmed correct; critic premise does not hold against the canonical on-disk file).
  - **Action**: per recurrence-6, re-verified the END line by **direct on-disk `Read`** of `reference/palace/palace/fem/libceed/operator.cpp` (NOT `citecheck --anchor`). On-disk reality: `:522` = `return mat;`, **`:523` = the closing `}`**, `:524` = blank, `:525` = `std::unique_ptr<Operator> CeedOperatorCoarsen(...)`. The function spans `455-523`, which is **exactly what the report cites**. The critic's "close brace at `:522`" was itself off-by-one (likely a stale/codemap-drifted line read). No edit to the report — its three `:455-523` citations are accurate.
  - **Rationale for no edit**: applying the critic's `523 → 522` "correction" would have *introduced* an off-by-one (the report would then under-cite, ending on `return mat;` and dropping the close brace). The repairer override is grounded in the mandated direct-on-disk Read, which the critic's own check claimed to use but evidently diverged from.

- **Finding (Issue 2): `eliminate_rhs` primitive name paraphrase (`set_subvector` vs on-disk `set_essential`).** The report (finding-(i) table row 6, finding (iii), Open-questions caveat) names the third pin-set primitive `set_subvector`; the on-disk `eliminate_rhs.md:54-57` uses `set_essential(b', pin)`.
  - **Decision**: repaired.
  - **Action**: surgical name alignment `set_subvector` → `set_essential` in all three occurrences of `reports/<id>/CYCLE.md` (finding-(i) table row 6 [Decomposes? + disposition cells], finding-(iii) "Rise as L4 post-composition operators" bullet, Open-questions "`eliminate_rhs` L4 thinness gate" caveat). Verified zero `set_subvector` occurrences remain via grep. The cited line range `54-57` was already correct — this is a name paraphrase, not a citation-range error; mechanical and within repair authority.

### Unrepairable findings

None. Issue 1 resolved as not-needed (report already correct; critic premise corrected via direct on-disk Read). Issue 2 repaired mechanically.

## Suggested resolution

`ready`. Notes for the integrator: this is an **observation-only survey** — it proposes NO `book/` changes (the repairer touched only the report's own CYCLE.md text). The two flagged citation matters are settled: the `:455-523` span is on-disk-accurate (no change), and the `set_subvector`→`set_essential` name was aligned. The survey's c068+ dispatch ranking (rank-1 `fe_assemble` L4 `assemble`-fold combinator; rank-2 `assemble_frequency_operator` via `linear_combination` L4-rise; ranks 3-4 the Dirichlet-BC post-compositions; deferred construction-inputs) and the `linear_combination` no-L4-by-design sub-observation are the actionable outputs for the planner to migrate into `priorities.md`, not artifact landings for this cycle.
