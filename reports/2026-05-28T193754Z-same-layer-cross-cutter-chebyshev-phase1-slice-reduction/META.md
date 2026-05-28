---
verifies: ../REPORT.md
critiqued_at: 2026-05-28T201500Z
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
repaired_at: 2026-05-28T202100Z
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

# META: verification of chebyshev Phase-1 slice-reduction audit (partial)

## Critique

### Checks run

**citation-validity — pass.** Every citation in the report resolves in-range. Slice anchors verified: `wc -l` = 439, single H1 at line 1, seven H2 at 34/102/106/118/122/229/287 — exactly matching the report's section-anchor table (lines 57-66) and Open-questions evidence (line 224). Firm-entry provenance cites confirmed: `L1/chebyshev-smoother.md:341` cites `slices/chebyshev.md:34-116`; `L2/chebyshev-iteration.md:266` cites `:122-228`; `L3/chebyshev.md:520` cites `:229-285`; `L4/chebyshev.md:468` cites `:287-439`. The five krylov-step → slice §L4 line ranges all resolve (see cross-reference-integrity). Minor: the report's anchor table labels the L1 provenance cite as `:341-345` in supporting evidence (line 225) but it begins at line 341 — a harmless span vs. point discrepancy, not a defect.

**surface-or-evidence — pass.** Not a refinement-shaped proposal. This is a Phase-1 corpus reduction-eligibility audit that proposes NO surface change to operators/themes and explicitly does not mutate `book/` (line 274); the proposed-changes block is a deferred sketch gated on an OQ. Out of scope for the surface-vs-evidence gate.

**rotation-quality — pass (not applicable).** The report asserts no new algebraic/structural rotation; it audits whether existing firm rotations (L1/L2 cycle-012, L3 cycle-013, the two lowering themes) already absorb the slice content. No rotation claim to grade.

**variant-axis-coverage — pass.** The report frames itself as a variant-axis / reduction-eligibility gap (Observation kind, line 47) and covers each section's supersession status exhaustively (one row per H2 in the supersession map, lines 73-82), with the single `partial` row (§L4) decomposed into its two sub-blockers (citation-redirect + downstream rough-in). No hidden branch: the §L4 retention is explicitly scoped, not silently dropped.

**cross-reference-integrity — pass (load-bearing claim CONFIRMED).** The central §L4-retention rationale holds. `L2/krylov-step.md` REALLY cites the slice §L4 ranges: `:354-362` at lines 7/79/85/140, `:355-362` at line 58, `:308-323` at line 118, `:330-353` at line 148, `:421-436` at line 77 — all five ranges the report names. The additional sites also resolve: `L2/index.md:35`, `L3/krylov-step.md:198,:206`, `L3/apply_linop.md:188`, `L3-L2/krylov-step-body-identity.md:127` each cite `:354-362`/`:330-353`. The §L1/§L2/§L3 absorption is real: the firm L1/L2/L3 entries re-cite the C++ ranges independently and cite the slice only as promotion provenance (redirectable to git history). All firm-entry slugs and the `cg_preconditioning_framework` §L4-retention precedent resolve.

**edge-label-fidelity — pass (not applicable).** No L_{n+1}→L_n edge label carried; this is a same-layer corpus-cross-cut, not a lowering proposal.

**plan-kind-consistency — pass.** Declared kind is an observation/audit (`status: pending`, same-layer-cross-cutter); content shape matches — a reduction-eligibility verdict (`partially-absorbed`) with a deferred, explicitly-not-applied proposed-changes sketch. No firm/rough-in operator mis-classification.

**skill-uptake-survey — pass.** `phase-1-slice-reduction-audit` (`skill_invoked` frontmatter, line 19) is genuinely applied: the four-part template is present (anchor table / supersession map / residual gaps / proposed changes), BOTH section ends are verified (step-1 discipline, lines 55/222-224), and the unique-text START anchor `## L4 — calculus form` is `grep -c`-confirmed unique (line 156). The cycle-012 HIGH-severity START-boundary trap is explicitly checked and ruled out (single-H1 slice, lines 68-69). The mandatory step-5 reconciliation and the sequencing hazard are both surfaced (lines 213-218, 259-264).

### Issues found

No blocking issues. Three low-severity notes for the repairer/integrator:

1. **(cosmetic) provenance-cite span label.** Supporting evidence line 225 writes `L1/chebyshev-smoother.md:341-345` while the actual provenance bullet is a single line at 341. Harmless; tighten to `:341` if touched. Severity: trivial.

2. **(confirmation, not a defect) stale-header observation is CORRECT.** The slice's own reduction-status header (lines 3-19 of `book/src/spec/slices/chebyshev.md`) is the cycle-011 version and lists the two concept-extension bullets (`state-stratification` four-stratum; `derived-view-hoisting` control-flow-boundary) as pending. Both are landed: `concepts/state-stratification.md:47-61` carries the four-stratum Chebyshev example and `concepts/derived-view-hoisting.md:21-43` carries the initial-guess-branch example. The report's "header is stale" claim (lines 117-121) is accurate; recommendation 4 (drop the stale bullets) is well-founded.

3. **(forward-pointer, already flagged by the report) sequencing hazard is real and load-bearing.** The krylov-step citations into §L4 are line-number-anchored relative to the pre-reduction file; collapsing §L1–§L3 (lines 1–286) shifts §L4 upward, so the report's insistence (lines 213-218, 259-264) that the citation re-point MUST land in the same batch as the partial reduction is correct and should be preserved through any repair. Not a report defect — a correctly-surfaced integrator constraint.

## Repair

### Fixes attempted

- **Finding**: (cosmetic) provenance-cite span label — supporting-evidence bullet writes `L1/chebyshev-smoother.md:341-345` where the provenance cite is a single line at 341.
  - **Decision**: repaired
  - **Action**: CYCLE.md §Supporting evidence — tightened `book/src/L1/chebyshev-smoother.md:341-345` → `:341` (point cite, matches the actual provenance bullet location). Mechanical citation-offset fix, in-scope.

- **Finding**: (confirmation, not a defect) stale-header observation is CORRECT — the slice's cycle-011 reduction-status header lists the two concept-extension bullets as pending, but both are landed (`concepts/state-stratification.md:47-61`, `concepts/derived-view-hoisting.md:21-43`).
  - **Decision**: not-needed
  - **Rationale**: The critic explicitly confirmed the report's "header is stale" claim is accurate and recommendation 4 (drop the stale bullets) is well-founded. The fix is to the *artifact slice header*, not the report — and is correctly deferred into the report's own partial-reduction proposed-changes block (recommendation 4 + the stub front-matter). Repairer does not mutate `book/`; the integrator applies the slice-header edit when the partial reduction lands. No report-side edit required.

- **Finding**: (forward-pointer) sequencing hazard — the krylov-step §L4 citations are line-number-anchored to the pre-reduction file; the §L1–§L3 collapse shifts §L4 upward, so the citation re-point must land in the same batch.
  - **Decision**: not-needed
  - **Rationale**: Correctly surfaced by the report (lines 213-218, 259-264) as a load-bearing integrator constraint; the critic confirmed it must be preserved. It is preserved verbatim — no edit. This is a sequencing instruction for the eventual reducing dispatch, not a report defect.

### Unrepairable findings

None. All three critic notes were either a trivial mechanical fix (repaired) or confirmations to preserve (not-needed). No substantive authoring was required and no contradiction with artifact content was found.

## Suggested resolution

`ready`. Notes for the integrator:

- This is a `partially-absorbed` reduction-eligibility audit; the proposed-changes block is an **explicitly-deferred sketch** (the report did not mutate `book/`, and the partial reduction is gated on the OQ). Do not apply the §L1–§L3 collapse as artifact changes this report; only the OQ promotion is in-scope for integrator-per-report.
- **Promote OQ `chebyshev-slice-l4-full-removal`** (report lines 251-258) to the ledger. It carries both promoted threads: (a) re-point the firm `L2/krylov-step` (+ `L3/krylov-step`, `L3/apply_linop`, `L3-L2/krylov-step-body-identity`, `L2/index`) citations from `slices/chebyshev.md:354-362 / :330-353 / :355-362 / :308-323 / :421-436` onto the `L4/chebyshev.md` anchors via a lifter dispatch; (b) re-run this slice removal-audit post-cycle-015 (after the `L4/chebyshev` `iterate-while` re-anchor firms). The §L4 removal is routed to that re-run.
- **Sequencing constraint is load-bearing**: when the partial reduction is eventually applied, the krylov-step citation re-point MUST land in the same batch (the §L4 line ranges shift upward when §L1–§L3 collapse). Do not apply the §L1–§L3 collapse in isolation.
