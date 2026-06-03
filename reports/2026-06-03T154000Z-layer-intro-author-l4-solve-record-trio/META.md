---
verifies: ../CYCLE.md
critiqued_at: 2026-06-03T161500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
overall_status: ready
---

# META: verification of record-definition cohort #2(a) — `OpParams` / `SimState` / `Krylov`

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` clears all four files mechanically (op-params 10/10, sim-state 8/8, krylov 9/9, CYCLE.md 2/2 ok). I then spot-verified the load-bearing L0 backing-home anchors against on-disk `reference/palace/palace/linalg/iterative.hpp` by direct Read, since the report claims it caught and corrected codemap +1/+2 drift in the CG/GMRES/FGMRES region. Every cited anchor matches on-disk exactly: base-class `IterativeSolver` opens at 26 / closes at 115; `rel_tol, abs_tol :42`, `max_it :45`, `A :49`, `B :50`, `mutable bool converged :53`, `mutable double initial_res, final_res :54`, `mutable int final_it :55`, accessors `GetConverged/GetInitialRes/GetFinalRes/GetNumIterations :97-108`. Subclass anchors verify: `CgSolver` 119-150 with `mutable VecType r, z, p; :144` and `Mult :149`; `GmresSolver` 155-217 with `max_dim :180`, `gs_orthog :184`, `pc_side :187`, workspace `V :190 / r :191 / H :192 / s,sn :193 / cs :194`, `Initialize/Update :197-198`, `Mult :216`; `FgmresSolver` 222-275 with `Z :256`. The report's stated corrections (CG close-brace 150 not codemap-141; GMRES 217 not 219; FGMRES `Z` 256 not 255) are exactly what on-disk shows — the END-line guard was applied correctly. No drift, no off-by-one.

**surface-or-evidence (incl. record-definition sub-check) — pass.** These three pages ARE the supply side of the record-definition obligation, so the sub-check is the central check here. Each page defines its record IN ITSELF: a `## Record definition` section with a `{ field: type }` schema block, a fielded `field : type — stratum/lifetime — meaning` table, the construction-vs-run-time stratum stated per field, and an `## L0 source home` section mapping each field to a cited Palace instance-field declaration. op-params correctly marks the whole record construction-time/readonly; sim-state correctly marks all five fields run-time-evolved and uniform-across-slices; krylov correctly gives two slice-specific schemas (CG / GMRES-FGMRES) and marks the whole record run-time/restart-local with the mixed iterate/scalar internal split. Critically, none restates the `krylov-step` operator algebra — each down-links the behaviour to `../L4/krylov-step.md` and explicitly says "this page does not restate that algebra." The conceptual three-stratum typing is cross-linked to `state-stratification.md` ("do not duplicate; this page is the field schema, that page is the conceptual typing"), not restated. This is exactly the data-shape vs. behaviour-over-data partition directive-2 requires.

**rotation-quality — pass (not applicable to record-definition-page kind).** These are data-shape concept pages, not lowering themes; they assert no algebraic/structural/reduction rotation. The check no-ops, analogous to the stub/feature-surface no-op convention.

**variant-axis-coverage — pass.** The relevant variant axes (CG vs GMRES vs FGMRES; preconditioner present/absent; flexible/Z present/absent; Chebyshev poly-kind) are all explicitly handled in the schemas rather than hidden: krylov gives separate CG and GMRES/FGMRES schemas; the optional fields are flagged `?` with their presence predicate (`z?` iff a preconditioner; `Z?` iff `OpParams.flexible`); op-params marks the GMRES/Chebyshev-only selectors. No hidden branches.

**cross-reference-integrity — pass.** All down-links resolve on disk: `state-stratification`, `solve-monad`, `convergence-test`, `variant-absorption`, `constructed-operators`, `constructed-operator-factory`, `first-iteration-unrolling` all exist under `concepts/`; `krylov-step` is correctly linked as `../L4/krylov-step.md` (it lives in L4, not concepts) and exists. The three sibling cross-links (op-params↔sim-state↔krylov) will resolve once the cohort lands. The `index.md` `## Index` insertions all match on-disk `[old]` anchors exactly and land in correct alpha position (krylov between incremental-least-squares/ksp_solve @88-89; op-params between nrm2/orthogonalization @92-93; sim-state between set_subvector_zero/solve-monad @100-101). The `SUMMARY.md` insertions match on-disk anchors and alpha positions (lines 315/316, 319/320, 327/328). The Kind-legend `[old]` anchor (`- \`auxiliary\` — ...`) matches index.md line 60 exactly. The cited `state-stratification.md` sections — §"Worked example — GMRES" (line 37), §"Common stratification mistakes" (line 20), the fourth scalar-recurrence stratum (line 47+) — all exist and back the claims. The L4/krylov-step.md citations (`:37` OpParams, `:38` Krylov, `:39` SimState, `:50` slice-specific schemas) back the field schemas; the CG `{ r, p, z?, α, β }` and GMRES `{ V, Z?, H, s, cs, sn, β, j }` shapes match krylov-step.md:50 verbatim.

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label is carried; these are concept-library record pages, not lowering-edge themes.

**plan-kind-consistency — pass.** The content is uniformly a NEW `record` Kind (data-shape definition home), consistent with directive-2 (the record-definition obligation). The `## Status: firm` token on each page is justified in-prose by the record-definition firmness criterion ("every field backed by a cited L0 declaration + stratum stated") rather than an operator-algebra apparatus, which the report explicitly flags as a meta-phase Kind-convention question (`concepts-record-kind-needs-meta-ratification`). The new `record` Kind value is properly flagged for batch-24 meta-phase ratification — in-use-now-pending-ratification is the correct posture (directive-2 is a live user directive; ratification is bookkeeping). No mis-classification.

**skill-uptake-survey — pass.** The shape implies the citation-verification skill family; the report references `citecheck --anchor`/`--scan` (the `verify-citation-range` mechanical realization) and the END-line guard explicitly. Telemetry present, no blocking concern.

### Issues found

No issues rising to warning/fail. Two non-blocking observations recorded for the integrator (neither is a defect):

1. **Kind-legend insertion position is logical-order, not alpha (cosmetic, not a defect).** The new `record` bullet is appended after `auxiliary` in the index.md Kind-legend prose list (lines 56-60). That list is ordered logically (methodology / algorithm / primitive / layer-pattern / auxiliary — catch-all last), NOT alphabetically; the directive-3 alpha convention governs the `## Index` *table rows*, not the legend prose. Appending `record` after the `auxiliary` catch-all is acceptable under the existing list convention. Flagged only so the integrator does not mistake it for an alpha-position miss.

2. **Cross-cohort index/SUMMARY re-anchor dependency (already disclosed by the report).** The report's own integrator caveat correctly notes that parallel dispatches D2/D3 insert their own `## Index` rows + SUMMARY entries against distinct anchors, and that if D2/D3 land first the integrator must re-anchor this report's `[old]` neighbor pairs against the post-D2/D3 alpha-neighbors. The on-disk anchors verified here are the current pre-D2/D3 state. This is a serialization note for the integrator, not a content defect; the `record` Kind-legend line is D1-exclusive and conflict-free as stated.

All eight checks pass; `overall_status: ready` set (clean all-pass report, no repairer will run).
