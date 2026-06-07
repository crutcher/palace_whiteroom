---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T17:05:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-07T17:30:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of D2 high-order-signature closure-grouping compliance audit

## Critique

### Checks run

**citation-validity — pass.** I independently Read every load-bearing cited line. All match exactly: the 4 NON-COMPLIANT signature sites (`assemble_frequency_operator.md:98-99`, the `:106` `A2` field, the `:293` restatement; `fe_assemble.md:60`, `:35`, `:71`); the borderline `eliminate_bc.md:83-84`; the trigger `mk_matrix_free_operator.md:60` + its mirror `feature/matrix-free-operator.L4.md:54`; the COMPLIANT spot-checks `krylov-step.md:63,69-70`, `chebyshev.md:70,74,75`, `apply_linop` (L3) `:37`, `inner_product_M` (L4 `:85` / L3 `:95`); and the convention-source lines `semantics/index.md:46,91-95,383-408,494`. The convention citations are accurate and load-bearing: `semantics/index.md:95` explicitly sanctions `LinOp[(S: ...), $S]` as the calculus rendering of a square operator, and `:91-95` states the rank-1 `LinearOperator[M,N]` spelling is faithful *at L1/L0* but the calculus rendering belongs at L4/L3/L2 — which is exactly why the 4 L4 ops using `LinearOperator[N,N]` are correctly non-compliant. No off-by-one, no out-of-range, no dead refs.

**surface-or-evidence — pass (no-op for read-only audit kind).** This is a read-only cross-cutting findings catalogue: it mutates no chapter, proposes no surface change, makes no new algebraic/rotation claim. It is not a refinement-shaped proposal, so the surface/rotation-evidence obligation does not attach. No record is newly named in a signature here (the records referenced — `FrequencyOperatorFamily`, `ChebOp` — are defined in their home chapters and only quoted). Not applicable.

**rotation-quality — pass (not applicable to read-only audit).** No rotation is asserted; the report classifies an existing notation convention's satisfaction. No-op.

**variant-axis-coverage — pass (not applicable).** No operator with variant axes is being authored. The audit's own coverage (COMPLIANT/NON-COMPLIANT/N-A partition) is assessed under completeness below, not this check. No-op.

**cross-reference-integrity — pass.** All file:line refs resolve to real, in-range locations in real chapters; the constituent chapters (`assemble_frequency_operator.md`, `fe_assemble.md`, `eliminate_bc.md`, `mk_matrix_free_operator.md`, `krylov-step.md`, `chebyshev.md`, `apply_linop.md`, `inner_product.md`, `semantics/index.md`, `feature/matrix-free-operator.L4.md`) all exist. The sync flag (`feature/matrix-free-operator.L4.md:54` carrying the identical trigger signature) is correct — I verified the mirror line reads `matrix_free_operator :: ... -> LinearOperator (Tensor[(N: ...)])`.

**edge-label-fidelity — pass.** The report frames itself as an L4↔L3 cross-cut and an "edge-label/surface-fidelity drift" observation; the prose discusses exactly the signature-convention surface it claims to. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared as a read-only findings catalogue / cross-cutting observation making no new claims and creating no chapters; content matches (a classification table + a c129 lifter-sweep recommendation, no proposed-changes block). Correctly shaped as an observation, not a firm/rough-in entry.

**skill-uptake-survey — warning (telemetry only, non-blocking).** A signature-spelling compliance sweep across a known op population is a procedure that plausibly maps to a skill (a "high-order-signature closure-grouping compliance audit" sweep procedure), and `classify-variant-axis`-style mechanical-classification skills exist in the family; the report invokes none and references none. This is a surfacing-only signal, not a defect in the findings.

### Issues found

**(1) Completeness gap — the `L4/index.md` dep-map mirror rows were not swept (warning).** The report's stated scope was "every high-order signature across `book/src/L4/**` …", and the classification is correct for the chapter *signature blocks*. But my completeness grep (`grep -rn 'LinearOperator\[' L4/` and `'LinearOperator ('`) surfaces that the **`L4/index.md` dep-map rows mirror the same ops in the applied-spelling**, and at least one diverges from its chapter in a way that matters to the audit's own discriminator:
   - `L4/index.md:61` writes `eliminate_essential_bc :: LinearOperator[N,N] -> LinearOperator[N,N]` — the **applied-spelling NON-COMPLIANT trigger shape** — whereas the chapter (`eliminate_bc.md:83-84`) uses the bracketed `LinOp[(S: ...), $S] -> ... -> LinOp[$S, $S]` form the report adjudicates borderline-COMPLIANT. So the same op is spelled compliantly in its chapter and non-compliantly in its index row; the index row was not flagged.
   - `L4/index.md:62` similarly mirrors `assemble_term :: ... -> LinearOperator[N,N]` (the chapter's finding #3), and `L4/index.md:119` mirrors the `mk_matrix_free_operator` trigger.
   These are **dep-map mirrors of already-flagged ops, not missed ops** — so the verdict population (the 17-op partition) is not wrong. But a c129 lifter sweep that rewrites only the chapter signature lines would leave the `index.md` rows drifted (and would leave `eliminate_bc` internally inconsistent between chapter and index). Severity: warning. Where: report Inventory tables omit the `index.md` mirror surface; the sweep recommendation (CYCLE.md:89-95) scopes "2 chapters" and should additionally name the `L4/index.md` rows for the same cohort. This is the same class of sync risk the report itself correctly raised for the feature mirror — it just did not apply the lens to the dep-map.

**(2) Minor — prose restatement of the `A2` closure field not enumerated (informational, sub-warning).** Beyond the `:106` record-field finding and the `:293` signature restatement (both noted), `assemble_frequency_operator.md:127` carries `fam.A2 — Scalar -> LinearOperator[N, N]` in the shape-contract prose — a third in-chapter instance of the same closure field. Not a separate op and arguably out of scope for a *signature* audit (it is prose), but a lifter rewriting the cohort should sweep it for consistency too. Low stakes; folds into finding #1's "rewrite all instances in the chapter" guidance.

### Assessment of the items the dispatch asked me to scrutinize

- **Classification correctness (NON-COMPLIANT cohort):** verified. All 4 ops genuinely write an operator-returning codomain as the bare `LinearOperator[N,N]` applied-spelling with a trailing arrow (`assemble_frequency_operator.md:99`, the `A2` field `:106`, `fe_assemble.md:60`, `assemble_term` `:71`/`:35`) — the identical shape as the `mk_matrix_free_operator.md:60` `LinearOperator (Tensor[(N: ...)])` trigger. None is mis-flagged.
- **Classification correctness (COMPLIANT spot-checks):** verified. `krylov-step.md:63,69-70` genuinely use the paren-grouped trailing closure `(SimState -> Solve {…})`; `apply_linop`/`inner_product_M` use the bracketed `LinOp[...]` operator-value spelling; `chebyshev` uses explicit `Solve`-monadic wraps + a paren-tupled closure field. Correct.
- **Borderline adjudication (`eliminate_essential_bc`):** D2's call is well-grounded and, if anything, the chapter form is *clearly* compliant rather than merely borderline — `semantics/index.md:95` explicitly names `LinOp[(S: ...), $S]` as the sanctioned square-operator calculus spelling. D2's conservative "defer to convention author" is acceptable because the open sub-question (should operator-TRANSFORMER codomains *additionally* be paren-grouped for symmetry with the constructor trigger) is genuinely a convention-author call, not a mechanical one. The one wrinkle the borderline framing should have surfaced is finding #1: the *index row* for this very op is in the non-compliant applied-spelling, so "compliant" is true only of the chapter.
- **Completeness:** the op-level enumeration is plausibly complete — my `grep` over `L4/**` for `LinearOperator[` / `LinearOperator (` / `Op[` surfaced no high-order op the partition missed; every applied-spelling hit maps to a flagged op (or its index/prose mirror per finding #1) or to a clearly-N/A value/record context. No missed operator.

## Repair

### Fixes attempted

- **Finding (1) — completeness — index-mirror rows + internal-inconsistency not in the recommended sweep scope (warning).**
  - **Decision**: repaired.
  - **Action**: Extended D2's **Recommendation** section in `reports/2026-06-07T164113Z-cross-layer-cross-cutter-highorder-signature-audit/CYCLE.md` (§Recommendation, the new "Sweep-scope EXTENSION" paragraph after the original cohort-sweep dispatch text). Verified all four cited sites exist on disk before editing: `L4/index.md:61` (`eliminate_essential_bc :: LinearOperator[N,N] -> LinearOperator[N,N]`), `L4/index.md:62` (`assemble_term :: ... -> LinearOperator[N,N]`), `L4/index.md:119` (the `mk_matrix_free_operator` trigger mirror row), and `assemble_frequency_operator.md:127` (the `fam.A2 — Scalar -> LinearOperator[N, N]` prose instance). The extension names each surface, marks `L4/index.md:61` as the `eliminate_bc` chapter↔index internal-consistency reconcile (tied to #4's adjudication), routes `L4/index.md:119` to D1/integrator in lockstep with the trigger fix (NOT the c129 cohort sweep), and folds `:127` into fix #1's "rewrite all instances in the chapter" guidance. This is a mechanical/surgical edit to D2's recommendation surface only — it does NOT touch the audited signatures themselves (that remains the c129 lifter sweep's job) and does NOT change the 17-op partition (the critic confirmed that population is correct).

- **Finding (2) — skill-uptake-survey (warning, telemetry only).**
  - **Decision**: not-needed (no content fix).
  - **Rationale**: the critic explicitly flagged this as a surfacing-only telemetry signal, not a defect in the findings. No repairable artifact.

### Unrepairable findings

None. The single actionable warning (finding #1) was mechanically repairable — it was a scope-completeness gap in a recommendation, fixed by extending the recommendation text to name the already-verified-on-disk mirror/prose surfaces. No substantive authoring was required (the signatures themselves are left for the c129 sweep, by design of a read-only audit).

## Suggested resolution

`ready`. D2 is a read-only findings catalogue with no proposed-changes block; the integrator applies nothing to the artifact from it. The single content edit was to D2's own recommendation, ensuring the future c129 lifter sweep is scoped to also rewrite the `L4/index.md` dep-map mirror rows (`:61`/`:62`) + reconcile the `eliminate_bc` chapter↔index inconsistency, with `:119` routed to D1/integrator alongside the `mk_matrix_free_operator` trigger fix and `:127` folded into fix #1. Note for the integrator: this report's value is the c129 sweep recommendation — promote `oq-highorder-operator-transformer-codomain-convention` to the convention author (D1) so #4's operator-transformer-codomain call is pinned before the c129 sweep runs.
