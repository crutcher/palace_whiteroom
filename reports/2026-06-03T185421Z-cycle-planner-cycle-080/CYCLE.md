---
agent: cycle-planner
invoked_at: 2026-06-03T185421Z
scope: cycle-080 dispatch plan
status: pending
integrated_at: 2026-06-03T192132Z
integration_commit: 7edbd3d
integration_notes: "Planner report consumed per convention. Planned 3 dispatches (D2 harvester eigenvalue-untransform; D1 lowering-verifier matrix-weighted-norm 2nd-gate; D3 lifter c079-deferred prose cleanup); 3 dispatched-ready, 3 applied clean."
---

# Cycle 080 dispatch plan

## Goals selected this cycle

Cycle-080 is position 2/3 of meta-batch-25 (cycles 079/080/081; the batch-25 meta-phase
fires AFTER cycle-081's finalize). The batch-25 frontier is **FIRMING the seed surface**
(the FEATURE-SURFACE SPINE column build-out is COMPLETE at 13 `seed` columns). Cycle-079
landed both c075 reduce verbs' 2nd (test-coverage) gate via existing-test citation and
authored the new `domain_energy_reduce` L4 verb at rough-in. This cycle takes the two
**STRUCTURE-side firming routes** the c079 finalize surfaced as the highest-fan-out
continuations — the `matrix-weighted-norm` 2nd-gate audit (which is on `domain_energy_reduce`'s
critical path) and the eigenvalue-un-transform L1 primitive (the residual structure gate to
firming `eigenfreq_qfactor_reduce`) — plus a LOW prose-cleanup micro-pass batching the two
c079-deferred items. Three dispatches, single parallel wave.

## Dispatches

### D1 — `lowering-verifier` (THE LEAD, HIGH)
- **scope:** `matrix-weighted-norm-second-gate-via-domainpostoperator-test` — audit
  `book/src/L1/matrix-weighted-norm.md` (currently `rough-in (test-coverage-bounded)`, 0
  `verified_against:` blocks) against the EXISTING positive test
  `reference/palace/test/unit/test-domainpostoperator.cpp:75-93` — the `GetElectricFieldEnergy`
  call (`domainpostoperator.cpp:219-235`, body `½⟨E, M_elec E⟩` = SPD-weighted inner-product
  radicand summed over real+imag) followed by
  `CHECK_THAT(energy_SI, WithinRel(expected_energy_SI, 0.01))` against the closed-form
  `0.5·ε₀·E₀²·sx·sy·sz`. The test positively exercises the SPD-weighted radicand `⟨E, M E⟩`
  + the `½` scaling (the energy form `domain_energy_reduce` folds) — but NOT the outer `√`
  of `matrix-weighted-norm = √(xᴴ B x)` directly. **Audit-judgment** (firm-on-positive-structure
  escape vs. √-not-directly-tested caveat): emit the `verified_against:` block citing the test;
  promote to `firm` OR sharpen the `rough-in (test-coverage-bounded)` warrant per the verdict.
  COUPLED re-anchor (floor-landing-implies-same-cycle-adjacent-entry-reanchor): re-anchor the
  DIRECT critical-path consumer `book/src/L4/domain_energy_reduce.md:7,278` (the "rough-in
  maturity inherited from it" note + the "as firm as its least-firm folded primitive" note) to
  the audited maturity. IF the verdict is a FULL firm promotion (which would cascade the ~30-file
  `matrix-weighted-norm` reference graph), DO NOT touch all 30 files in this dispatch — flag a
  broad re-anchor sweep as a follow-up OQ (one-operator-per-dispatch / bounded-context
  discipline; the most likely clean outcome is the qualifier-sharpening + the gate-(a) discharge).
- **deps:** none
- **rationale:** Active-head LEAD; the c079 finalize's STRONG next-cycle candidate
  (integrator-signals cycle-079 §Unblocked + §Suggested-next-dispatches). Highest fan-out:
  firms/sharpens a widely-used L1 primitive AND discharges `domain_energy_reduce`'s energy-form
  constituent gate-(a) — the verb's critical path (`domain_energy_reduce.md:43` "a reduction is
  as firm as its least-firm folded primitive — so firming `matrix-weighted-norm` is on the
  critical path to `domain_energy_reduce` promotion"). OQs
  `matrix-weighted-norm-and-bilinear-form-stay-rough-in-with-sharpened-per-operator-gates-c028`,
  `domain_energy_reduce-promotion-double-gated`.

### D2 — `harvester` (MEDIUM-HIGH)
- **scope:** `eigenvalue-untransform-l1-primitive` — author the per-mode eigenvalue→ω
  un-transform L1 primitive (linear-EVP `ω = √μ` | quadratic-EVP `ω = λ/i`, keyed on
  `ProblemType`), the SECOND scalar map `eigenfreq_qfactor_reduce` folds. The κ-participation
  half is ALREADY firm L1 `participation_ratio` (c077) — do NOT re-open it. L0 (codemap-confirmed
  this cycle): `reference/palace/drivers/eigensolver.cpp:424-441` — the readout loop's
  `if (!C && !has_A2) { omega = std::sqrt(omega); } else { omega /= 1i; }` branch. Firm L1 home
  (+ L2 only if it meaningfully reshapes — no forced rectangular floor; this is a small per-mode
  scalar branch, likely L1-leaf-only per the redirect's anti-rectangular-floor stance). COUPLED
  re-anchor (same guard): re-anchor `book/src/L4/eigenfreq_qfactor_reduce.md` §"Lowers to" +
  dep-map + Status gate-(a) (the verb Status enumerates gate-(a) = "the eigenvalue un-transform
  is not yet a firm L1 entry") to point at the new firm L1 entry + mark gate-(a) discharged. The
  verb STAYS `rough-in (test-coverage-bounded)` — gate-(b) (the eigenpair→`(f,Q)` assembly test)
  is still open and out of write-scope.
- **deps:** none
- **rationale:** c079 finalize §Suggested-next-dispatches ("the eigenvalue-un-transform L1
  primitive ... would promote `eigenfreq_qfactor_reduce` past `rough-in (test-coverage-bounded)`
  toward `firm`"). Discharges the residual STRUCTURE-side gate; the last folded primitive of the
  eigenmode output product's reduction verb gets a firm L1 home. OQs
  `eigenvalue-untransform-l1-primitive`,
  `eigenfreq-qfactor-reduce-firm-needs-l1-eigenvalue-untransform-primitive`.

### D3 — `lifter` (LOW / hygiene)
- **scope:** `c079-deferred-prose-cleanup-micro-pass` — the two c079-deferred prose items
  (integrator-signals cycle-079 §Suggested-next-dispatches):
  (a) repoint the STALE `bilinear-form`→`port_projection` PROSE down-links in
  `book/src/feature/sparameters.L1.md` (the 6 `bilinear-form` refs at ~lines 36, 39, 49, 59, 64 —
  `port_projection` is FIRM as of c077 and the dep-map line 8 already points at it; the prose +
  the dep-map row at :59 still call the port-mode projection a rough-in `bilinear-form`); this is
  a stale-ref REPOINT to the now-firm verb, NOT a plain-text→live-link upgrade.
  (b) Fix the INTERNALLY-CONTRADICTORY stale opening Status paragraph at
  `book/src/feature/eigenfrequency-qfactor.L4.md:68` — it asserts `eigenfreq_qfactor_reduce` is
  `rough-in` + "κ participation ratio ... not yet firm L1 entries", contradicted by the dep-map
  (lines 65/67: `rough-in (test-coverage-bounded)`) + the corrected appended paragraph (70-78)
  + the firm L1 `participation_ratio`. Reconcile the opening paragraph to the appended-paragraph
  narration (CURRENT on-disk maturity).
- **deps:** none
- **rationale:** Drift-guard hygiene; closes the two c079-deferred prose items. Rides the cycle
  as a light disjoint pass.

## Overlap analysis

Pairwise file-region check (the genuine-overlap test = same operator entry modified OR same
theme body rewritten; distinct dep-map rows / disjoint files are parallel-safe):

- **D1 ∩ D2:** No overlap. D1 writes `book/src/L1/matrix-weighted-norm.md` + re-anchors
  `book/src/L4/domain_energy_reduce.md`. D2 writes a NEW `book/src/L1/<eigenvalue-untransform>.md`
  + re-anchors `book/src/L4/eigenfreq_qfactor_reduce.md`. Disjoint L1 entries, disjoint L4 verb
  files. Both touch `book/src/L1/index.md` and `book/src/SUMMARY.md` — but: D1's audit is a
  status-cell maturity refresh on an EXISTING `matrix-weighted-norm` row; D2 ADDS a new L1
  dep-map row + a new SUMMARY entry. These are anchor-distinct (different rows). PARALLEL-safe
  per the "distinct rows / non-aggregate" rule. **No consolidated-tally co-write risk:** D1 does
  not change the L1 firm-count unless its verdict is a full firm promotion; D2 adds a new
  rough-in (or firm) L1 entry. To stay clean per the parallel-blind-shared-index guard, the
  L1/index firm-count + SUMMARY count-tally write is assigned to **D2 as sole count-owner**
  (D2 is the new-entry author and the last in dependency order); **D1 emits ONLY its
  `matrix-weighted-norm` status-cell maturity refresh + its own `verified_against:` block and
  DEFERS any L1/index aggregate count delta to D2.** (D1's audit most likely sharpens a qualifier
  with NO firm-count change; if it DOES promote to firm, it states the +1 in its report Notes for
  D2/the per-report integrator to fold into the single tally.) Each adds its OWN non-aggregate
  row; the consolidated count is D2's.
- **D1 ∩ D3:** No overlap. D1 touches `matrix-weighted-norm.md` + `domain_energy_reduce.md`;
  D3 touches `feature/sparameters.L1.md` + `feature/eigenfrequency-qfactor.L4.md`. Disjoint files.
- **D2 ∩ D3:** **Topical coupling, NOT file overlap.** D2 re-anchors the L4 verb file
  `book/src/L4/eigenfreq_qfactor_reduce.md`; D3 cleans the feature column chapter
  `book/src/feature/eigenfrequency-qfactor.L4.md`. DISTINCT files. The coupling: if D2 firms the
  eigenvalue-un-transform primitive, the eigenfreq-qfactor column's seed-reasoning shifts again.
  D3's scope explicitly narrates the CURRENT-on-disk maturity (reconcile the internal
  contradiction) and DEFERS any un-transform-firmness restatement to D2's verb re-anchor — so the
  two do not both rewrite the same maturity claim. PARALLEL-safe (distinct files; D3's job is the
  internal-contradiction fix, which is true regardless of D2's verb-side outcome — the κ-half is
  firm and the verb is `rough-in (test-coverage-bounded)` either way this cycle).

No two dispatches modify the same operator entry or rewrite the same theme body. Shared-index
consolidated-count ownership assigned to D2 (sole count-owner); D1 defers any aggregate count
delta to D2 and emits only its own status-cell refresh + audit block.

## Sequencing schedule

**Single wave (all parallel):** D1, D2, D3.

No forward-reference dependencies (no dispatch references another's not-yet-landed slug — D2
authors a NEW L1 file but no co-dispatched report links to it this cycle; D1's
`domain_energy_reduce` re-anchor and D2's `eigenfreq_qfactor_reduce` re-anchor target EXISTING
on-disk files). Per the conflict-tolerance philosophy (when in doubt, PARALLEL), the only shared
surfaces (`L1/index.md`, `SUMMARY.md`) carry anchor-distinct rows with the consolidated-count
owner assigned to D2 — false sequentialization here would cost throughput for no real conflict.

## Deliverable-presence verification

Per the MANDATORY four-step pre-dispatch check (paste-inline evidence):

### D1 — `matrix-weighted-norm.md` 2nd-gate audit
1. **File existence:** `ls book/src/L1/matrix-weighted-norm.md` →
   `-rw-rw-r-- 1 crutcher crutcher 25308 May 29 11:28 book/src/L1/matrix-weighted-norm.md` (EXISTS).
2. **Maturity / already-discharged:** `## Status` line read on disk (`:110`):
   `rough-in (test-coverage-bounded)` — "no dedicated Palace test exercises the SPD-weighted
   overload at this exact entry point". `grep -c '^verified_against:' book/src/L1/matrix-weighted-norm.md`
   → `0` (NO audit block present — the proposed audit deliverable is genuinely absent).
3. **OQ-ledger RESOLVED-grep:** `grep '...RESOLVED\|...CLOSED' scaffolding/open-questions.md` →
   `matrix-weighted-norm-and-bilinear-form-stay-rough-in-with-sharpened-per-operator-gates-c028` is
   `RESOLVED-as-adjudication c028 D6 (STAYS OPEN as plan Backlog item with sharpened gates) — both
   L1 operators STAY rough-in; matrix-weighted-norm gate narrowed to named-entry-point √+SPD-guard
   test`. The gate (a named-entry-point √+SPD-guard test) is the structural block; the c079 signal
   identifies `test-domainpostoperator.cpp` as the addressing route.
4. **Structural-block check:** the c028-sharpened gate ("named-entry-point √+SPD-guard test") was
   blocking because no upstream Palace test exercised the entry point. The block is NOW addressable:
   `test-domainpostoperator.cpp:75-93` is a positive SI-energy assertion on the SPD-weighted
   radicand (verified below) — a NEW test-citation route the c028 adjudication did not have. The
   audit is OPEN. (Note: the test exercises the radicand `⟨E,M E⟩`+`½`, not the outer `√` directly
   — hence this is an audit-judgment dispatch, not a presumed firm promotion.)
   - Test anchor codemap-confirmed: `test-domainpostoperator.cpp:83`
     `double energy_nondim = dom_post_op.GetElectricFieldEnergy(*E_field);`; `:90-91`
     `expected_energy_SI = 0.5 * electromagnetics::epsilon0_ * E0_SI * E0_SI * sx_SI * sy_SI * sz_SI;`;
     `:93` `CHECK_THAT(energy_SI, WithinRel(expected_energy_SI, 0.01));`.
   - Energy-form body codemap-confirmed: `domainpostoperator.cpp:219-231`
     `GetElectricFieldEnergy` → `M_elec->Mult(E.Real(), D); double dot = linalg::LocalDot(E.Real(), D); ... return 0.5 * dot;`.
   - **NOT on the STOP-PROPOSING negative list** (the list is `lu_solve`/`back_solve`/
     `ls-update-column`/`nleps_*` L3 backfills; `matrix-weighted-norm` is not on it).
   - **Framing = audit-first** (`lowering-verifier`), correct for a test-coverage-gate discharge
     (the c079 signal + the active head both name `lowering-verifier`/`find-tests-for-region`).
   - **ALL FOUR PASS → recruit.**

### D2 — eigenvalue-un-transform L1 primitive (open by construction)
1. **File existence:** `ls book/src/L1/eigenvalue-untransform.md book/src/L1/eigenpair-omega-map.md`
   → both `No such file or directory` (the new L1 primitive does not exist under either likely slug;
   the harvester picks the canonical slug at authoring).
2. **Maturity:** N/A (file absent — a fresh harvest of a new operator).
3. **OQ-ledger grep:** `grep 'eigenvalue-untransform\|eigenvalue-un-transform' scaffolding/open-questions.md`
   → `eigenvalue-untransform-l1-primitive (c077 D4) — the per-mode eigenvalue→ω un-transform ... no
   firm L1 home. Trigger: the coupled eigenfreq_qfactor_reduce re-check or an eigenmode-column
   firming pass.` + `eigenfreq-qfactor-reduce-firm-needs-l1-eigenvalue-untransform-primitive (opened
   c079 ...)`. Both OPEN (NOT RESOLVED/CLOSED) — and this cycle IS the coupled-re-check trigger.
4. **Structural-block check:** no block — the source is fully-specified positive Palace source
   (`eigensolver.cpp:424-441`, codemap-confirmed: `omega = std::sqrt(omega)` linear branch /
   `omega /= 1i` quadratic branch). The `eigenfreq_qfactor_reduce.md` Status explicitly names this
   as gate-(a) ("the eigenvalue un-transform is not yet a firm L1 entry"), confirming the target is
   the open structure-side gate. **Skip-justification for steps 1-2 maturity:** open by construction
   (fresh harvest of a new operator with no prior-cycle file). **Recruit.**

### D3 — c079-deferred prose cleanup (open by construction — c079 finalize-routed follow-up)
- (a) `sparameters.L1.md` stale `bilinear-form` refs: `grep -c "bilinear-form" book/src/feature/sparameters.L1.md`
  → `6`; `grep -c "port_projection" ...` → `1` (the dep-map line 8 only). Confirmed STALE: the prose
  + dep-map row :59 still call the projection a rough-in `bilinear-form` though `port_projection` is
  firm (c077). On-disk loci verified: `:36,39,49,59,64`. The deferral is named in
  integrator-signals cycle-079 §Suggested-next-dispatches (`sparameters.L1.md` PROSE down-link
  repoint `:39,60,64`). OPEN.
- (b) `eigenfrequency-qfactor.L4.md:68` internal contradiction: read on disk — opening paragraph
  `:68` says verb is `rough-in` + "κ participation ratio ... not yet firm L1 entries"; dep-map
  `:65,67` says `rough-in (test-coverage-bounded)`; appended paragraph `:70-78` says
  `rough-in (test-coverage-bounded)` + "the κ-participation half is already firm L1
  `participation_ratio`". Confirmed internally contradictory + named in the c079 signal. OPEN.
- **Skip-justification:** open by construction (meta-/finalize-routed follow-up explicitly named
  in the immediately-prior cycle's integrator-signals). **Recruit.**

## Open questions / caveats

- **D1 verdict uncertainty is intentional and bounded.** `GetElectricFieldEnergy` tests the SPD
  radicand `⟨E,M E⟩` + `½` (the energy form), NOT the outer `√` of `matrix-weighted-norm`. The
  cleanest outcome is the **energy-form (squared) constituent becomes positively test-covered**
  → `domain_energy_reduce`'s gate-(a) discharges + `matrix-weighted-norm`'s warrant sharpens
  (possibly still `rough-in (test-coverage-bounded)` since the √-overload's named entry point
  `linalg::Norml2(comm,x,B,Bx)` is not the tested entry point). A full firm promotion would
  cascade ~30 files — D1 is instructed to flag that broad sweep as a follow-up OQ rather than
  touch all 30 in-dispatch. The lowering-verifier owns this judgment; I am not pre-deciding it.
- **D2's `eigenfreq_qfactor_reduce` verb-side re-anchor does NOT promote the verb to `firm`.**
  D2 discharges gate-(a) (the structure-side primitive-maturity gate); gate-(b) (the eigenpair→
  `(f,Q)` assembly test) is out of write-scope and stays open. The verb stays
  `rough-in (test-coverage-bounded)`, and the `eigenfrequency-qfactor` column stays `seed` — this
  cycle does NOT trigger the column seed→promotion. Surfaced for the batch-25 meta-phase
  (whether an assembly-confidence lowering-verifier pass could discharge gate-(b) in-scope, per
  the OQ's "OR an assembly-confidence lowering-verifier pass" note).
- **Budget:** 3 of ≤12 slots used. The remaining FIRM-the-seed-surface work this cycle is either
  out-of-write-scope (the `sparameter_reduce` / `eigenfreq_qfactor_reduce` assembly tests) or
  trigger-gated (the column seed→promotions, the record-definition ≥2-consumer promote watches);
  forcing more dispatches would either redo c079 or hit a structural block. Three well-scoped,
  genuinely-open, high-warrant dispatches is the right load for this position.
- **For the batch-25 meta-phase (fires after c081):** the `domain-field-energy-participation-guard-inconsistency`
  source-observation (c079 D3/D-eigenfreq intake — the electric numerator-guard vs magnetic
  denominator-guard asymmetry in `MeasureDomainFieldEnergy`) is flagged as a possible `problems/`
  filing, NOT a plan item — note it for the aggregated 079/080/081 view if it recurs.
