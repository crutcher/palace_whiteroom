---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T060000Z
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

# META: verification of cycle-091 D4 — feature-column re-evaluation + feature/index reconciliation

## Critique

### Checks run

**citation-validity — pass.** Every `[old]` block in the proposed-changes was confirmed against on-disk text by fixed-string grep, and the cited line anchors are accurate. Spot-verified: the `energy-fields.L4.md` `composes:` block (`:6-10`) matches A1b's `old_string` verbatim; the `## Constituent down-links` rows at `:159-160` match A1f (`per-domain energy-table reduction | … *(rough-in)* | rough-in` and `per-domain energy form (folded) | …matrix-weighted-norm…-squared | rough-in (test-coverage-bounded)`); the `index.md` seed-block energy-fields bullet at `:70` matches G3. The cross-report verdicts D4 relies on are real and back the claims: the D3 report (`…lowering-verifier-cycle-091-reduce-verb-rejudgment/CYCLE.md` §"PROMINENT VERDICT FOR D4") explicitly returns `domain_energy_reduce → FLIPS to firm` + `→ D4 SHOULD FLIP energy-fields seed→firm`, and `gram_reduce → STAYS rough-in` + `→ D4 KEEPS electrostatic/magnetostatic/capacitance/inductance at seed`. No `verified_against:` block is emitted by this report (it is a feature-column re-eval, not a lowering audit), so that sub-check no-ops. No citation drift found.

**surface-or-evidence — pass (FEATURE-SURFACE-adapted).** Under the adapted check for the composition-root kind, a column's evidence is its L0 driver range + constituent down-links, not a per-op source site. The `energy-fields` flip is evidenced by the on-disk `composes:`/down-link constituents plus the L0 `MeasureDomainFieldEnergy` range (`postoperator.cpp:1021-1077`) — all present and resolving. The flip is a maturity-token + label re-anchor (surface change) justified by the cascade verdicts (D1+D3 evidence), not a bare rotation claim. The four stay-seed columns are pure re-narration of an existing gate (allowed). No record is newly named in a signature here, so the record-definition sub-check no-ops.

**rotation-quality — pass (not applicable to feature-surface kind).** A composition-root chapter rotates nothing — it recomposes already-firm vocabulary outward. No new algebraic/structural rotation is asserted; formally no-op per the adapted checklist.

**variant-axis-coverage — pass (not applicable to feature-surface kind).** Feature columns carry no variant axes of their own (the axes live in the constituent ops they compose). Formally no-op per the adapted checklist.

**cross-reference-integrity — pass (load-bearing for this kind).** This is the central check for a composition-root, and the index-cell-drift guard is the central sub-check. (1) The four stay-seed columns' re-narration correctly identifies the CURRENT gate: after the cascade discharges `matrix-weighted-norm` (the diagonal folded primitive), the residual gate is `gram_reduce`'s off-diagonal `bilinear-form` primitive — confirmed on disk `bilinear-form.md:4 firmness: rough-in` (so the residual-gate narration is honest) while `gram_reduce.md:4` stays `rough-in (test-coverage-bounded)` (so holding the four columns at seed is correct). (2) Every stale `matrix-weighted-norm` rough-in label is re-anchored to firm and every `bilinear-form` rough-in label is preserved — the label split (firm diagonal / rough-in off-diagonal) is consistent across all 9 touched files. (3) Index-cell-drift guard: after the flip, energy-fields' frontmatter `status:` → firm (A1a/A2a/A3a) AND its index cell moves to the firm cohort (G3) — consistent; the four stay-seed columns keep `status: seed` AND stay in the seed cohort — consistent. No cell drifts from its post-flip on-disk `status:`. The sibling-status grep (report §43) correctly notes the driver-agnostic exception (no per-driver up-link to energy-fields is drift). All `[link]` targets resolve to real chapters.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried; this is a maturity re-evaluation within `book/src/feature/`, not a lowering theme. Not applicable.

**plan-kind-consistency — pass.** The content shape (per-column maturity verdicts + index reconciliation) matches the D4 dispatch kind (feature-column re-eval, sole owner of `feature/index.md`). Arithmetic verified on disk: `index.md` currently reads `firm (6 columns)` (`:63`) / `seed (6 columns)` (`:67`); the +1/−1 delta to firm 7 / seed 5 is correct (energy-fields moves; the four gram_reduce-gated columns + boundary-mode = 5 remain seed). Scope discipline confirmed: every proposed-changes block targets `book/src/feature/` only; the report did NOT touch `L1/index.md`, `L4/index.md`, the reduce-verb own-entries, `L1/matrix-weighted-norm.md`, or vocabulary-spine consumers (those are D1/D2/D3's partitions).

**skill-uptake-survey — pass (telemetry).** The flip is coupled to a firm-promotion across multiple feature files; the report explicitly ran the firm-promotion-coupled whole-book-feature grep (§"Sibling-status grep", `grep -rn 'energy-fields' book/src/feature`), the expected procedure for this shape. Skill uptake surfaced.

### Issues found

No blocking issues. One load-bearing observation recorded for the integrator (not a defect in this report — the coordination is correct by design):

- **Intra-cycle dependency coupling (informational, file:all proposed-changes).** D4's correctness is contingent on BOTH sibling dispatches landing in the same cycle: D1 (`harvester-cycle-091-matrix-weighted-norm-firm-flip`) must flip `matrix-weighted-norm` to firm, and D3 (`lowering-verifier-…-reduce-verb-rejudgment`) must flip `domain_energy_reduce` to firm. On disk at critique time BOTH constituents are still `rough-in` (`domain_energy_reduce.md:4 firmness: rough-in`; `matrix-weighted-norm.md:110 ## Status … rough-in (test-coverage-bounded)`). This is the expected state of a downstream cascade consumer pre-integration, NOT drift — I verified D1's report enacts the matrix-weighted-norm firm flip and D3's report enacts the domain_energy_reduce firm flip + the honest gram_reduce hold, and D4's verdicts exactly mirror D3's explicit D4 directives. The integrator should sequence D1 → D3 → D4 (or apply all three in the same finalize batch) so that the energy-fields `firm` claim does not land while its constituents read `rough-in` on disk. If D1 or D3 is rejected/deferred, D4's energy-fields flip must defer with them.
- **Note on matrix-weighted-norm's storage (informational).** `book/src/L1/matrix-weighted-norm.md` has NO YAML frontmatter — its maturity lives only in the `## Status` prose line (`:110`). D4 correctly treats its own `composes:` references to it as prose-label re-anchors (there is no `status:`/`firmness:` field on that file for D4 or anyone to flip — D1 owns the `## Status` prose flip). No action needed; recorded so the integrator does not expect a frontmatter field there.
