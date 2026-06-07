---
verifies: ../REPORT.md
critiqued_at: 2026-06-07T171500Z
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

# META: verification of the 5-driver L4-completeness audit (ASK-2 "B" capstone)

## Critique

### Checks run

**citation-validity** — pass. The report's load-bearing claims are firm-status assertions on named constituents and L0 driver-range pointers. `citecheck --scan` on the report returned `4 ok, 0 failing` for the Palace-source citations it bounds. I independently confirmed the structural claims by reading every cited book chapter (the 6 feature surfaces + `fe_assemble.md` + `eigsolve.md` + the baseline-exceptions ledger). The constituent-firmness table (`CYCLE.md:48-55`) matches disk on every entry. The `fe_assemble.md:15-16, 164` pinpoints for the matrix-free edge are exact (frontmatter `constructs-via` at :15-16, leaf prose at :164). The RE4/RE11 ledger citations resolve to the live disposition rows. No uncited claim.

**surface-or-evidence** — pass (adapted for the read-only audit shape). This is a coverage-audit observation, not a refinement-shaped surface proposal: it proposes NO surface change and recommends NO edge authoring (explicitly "Defer — no follow-up dispatch warranted"). Its evidence is the per-driver L0 driver-range citations + the constituent down-link resolution, which is the correct evidence shape for a feature-spine composition-coverage claim. No record is named-by-use-only (each constituent has its own definition home in the linked chapter). Pass.

**rotation-quality** — pass (not applicable). The report asserts no algebraic/structural/reduction rotation of its own; it audits whether already-firm rotations compose. No-op, as for the feature-surface / read-only kind.

**variant-axis-coverage** — pass. The audit enumerates the disposition axis it is checking (PASS / opaque-boundary / absorbed-below-column / GAP) and the result for each of the 6 columns. The two opaque-boundary sub-cases (eigenmode `eigsolve`, transient ODE step) are explicitly scoped and dispositioned, not hidden. The boundary-mode 6th branch is explicitly scoped OUT with a re-check flag. No hidden branch.

**cross-reference-integrity** — pass, load-bearing for this kind and independently re-verified. Every named constituent slug resolves and is `firm` on disk: `fe_assemble`, `solve_family`, `ksp_solve`, `gram_reduce`, `eigsolve`, `frequency_sweep`, `assemble_frequency_operator`, `fold_solve`, `sparameter_reduce`, `eigenfreq_qfactor_reduce`, `mk_matrix_free_operator` (all `firmness:`/`status:`/`rank: firm`), `L1/build_mesh` (`rank: firm`). All 6 feature surfaces are `rank: firm`. All four output-product sibling columns (`capacitance`, `inductance`, `sparameters`, `eigenfrequency-qfactor`) exist on disk; the down-links resolve. The matrix-free claim — that `fe_assemble` already carries `mk_matrix_free_operator` as a navigational `constructs-via` `reference` (NOT `depends-on`) at the `assemble_term` leaf — is exactly confirmed at `fe_assemble.md:15-16` (frontmatter) and `:164` (leaf prose). No maturity overclaim: every claimed-firm constituent IS firm.

**edge-label-fidelity** — pass. The report carries no L_{n+1}→L_n edge label of its own. Its central edge claim ("do NOT author `driver-assemble → mk_matrix_free_operator`") is discussed at the exact altitude it names — the matrix-free interior below the `assemble_term` leaf vs a driver-stage constituent — and the prose matches the on-disk `constructs-via` reference relationship. Sound.

**plan-kind-consistency** — pass. Declared as a "Coverage gap audit (the inverse result: NO coverage gap)" — read-only findings. The content shape matches: a per-driver disposition table + firm-status verification + an edge recommendation + tracked-disposition citations + a Defer recommendation. No surface authoring, consistent with the read-only observation kind.

**skill-uptake-survey** — pass. The report invokes palace-codemap `read_range` for L0 anchor verification (noted in several Status lines of the chapters it audits and in its own self-verification). No dedicated "L4-completeness audit" skill exists; the per-stage composition-coverage procedure is ad-hoc but appropriate. Pure telemetry; non-blocking.

### Independent verification of the PASS verdicts

I independently Read all six L4 feature surfaces and confirmed each names the claimed firm constituents BY NAME at each composition stage:

- **electrostatic** — `fe_assemble` → `solve_family` (+`ksp_solve`) → `gram_reduce` (w=1). Confirmed (`electrostatic.L4.md:40-43`, down-link table :70-75).
- **magnetostatic** — `fe_assemble` → `solve_family` (+`ksp_solve`) → `gram_reduce` (w=1/(IᵢIⱼ)). Confirmed (`magnetostatic.L4.md:40-43`, :70-75).
- **eigenmode** — `fe_assemble`×3 (K/C/M) → `eigsolve` (once) → readout map. Confirmed (`eigenmode.L4.md:37-42`, :76-80); the `eigsolve` opaque-boundary is genuine — `eigsolve.md:176-182` carries `firm` as a cap under explicit opaque-library constraint (SLEPc `EPSSolve`/ARPACK `naupd`), the L4 echo of the L3 `partial-obstruction`, tracked by RE11. NOT an unacknowledged gap.
- **driven** — `fe_assemble`×3 → `frequency_sweep` (+`assemble_frequency_operator` + `ksp_solve`) → `sparameter_reduce`. Confirmed (`driven.L4.md:60-66`, :165-171).
- **transient** — `fe_assemble`×3 → `fold_solve`. Confirmed (`transient.L4.md:39-45`, :71-75); the per-step ODE body is genuinely `obstruction (opaque-library-ownership)` quantified-over by the firm `fold_solve` (`transient.L4.md:53, 75`). NOT an unacknowledged gap.
- **lifecycle ROOT** — `build_mesh` → driver dispatch → `fold_solve` (state-generated AMR form). Confirmed (`lifecycle.L4.md:41-44`, :67-73).

All 12 named constituents verified `firm` on disk (frontmatter grep). The matrix-free recommendation is sound: the `constructs-via` reference already exists at the correct leaf altitude, so a driver-stage `depends-on` edge would indeed misclassify (and would violate well-foundedness if the leaf interior were treated as a driver-stage constituent). No in-scope driver stage is silently omitted — the postprocess/output stage of each driver IS audited, routed to the existing output-product sibling columns (capacitance/inductance/sparameters/eigenfrequency-qfactor, all on disk) or materialized in-column (transient trajectory).

**The L4-complete conclusion holds up.** All 6 columns PASS on independent re-verification; the two non-PASS constituents are genuinely-tracked opaque-library kernels, not gaps. The capstone verdict is well-founded.

### Issues found

No blocking or warning issues. Two minor observations, neither a defect in the report:

1. **(Observation, not a report defect) Stale `rough-in` token inside the lifecycle chapter, not the audited report.** `lifecycle.L4.md:72` marks the `boundary-mode.L4` dispatch down-link as `rough-in`, but `boundary-mode.L4.md:6` is `rank: firm` on disk. The audited report reads boundary-mode correctly as `rank: firm` (`CYCLE.md:44, 129`), so the report is right and the lifecycle chapter cell is stale. This is a pre-existing artifact discrepancy in a chapter that is OUT of the 5-driver audit scope, and the report flagged boundary-mode's out-of-scope status appropriately. Surfaced here for the integrator/meta only; it does not affect the audit's verdict.

2. **(Observation, not a report defect) Pre-existing stale snapshot inside `fe_assemble.md`, correctly flagged by the report.** `fe_assemble.md:16` and `:164` still describe `mk_matrix_free_operator` as a `roadmap_goal` (its c126 state), but on disk it is `status/rank: firm` (firmed c127). The report's caveat #2 (`CYCLE.md:135-138`) flags exactly this disk-vs-snapshot drift and reads the current firm state. The stale token lives in `fe_assemble.md`, not in the report; the navigational `reference`-class relationship the report relies on is correct regardless of the leaf's maturity. No action needed from this report.
