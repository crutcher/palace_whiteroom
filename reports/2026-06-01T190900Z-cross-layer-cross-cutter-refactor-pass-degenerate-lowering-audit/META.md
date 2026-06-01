---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T201500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-06-01T203000Z
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

# META: verification of "Cross-layer observation — degenerate-identity-in-named-terms thin-theme cohort"

## Critique

### Checks run

**citation-validity — warning.** Ran `tools/citecheck/citecheck.py --scan` over the whole report: 17 ok, 0 failing (all cited ranges in-bounds, path hygiene clean). Spot-checked load-bearing pinpoints with `--anchor`: `scal-body-identity:86-89` (anchor `scal` ✓), `axpy-body-identity:91-93` (✓), `axpby-body-identity:90-92` (✓), `axpbypcz-body-identity:89-91` (✓), `dot-body-identity:74-84` (✓), `nrm2-body-identity:102-103` (anchor `inner_product` ✓), `scal-leaf-identity:63-73` (✓), `axpy-leaf-identity:96-108` (✓), `nrm2-leaf-identity:75-119` (✓), `linear-combination-fold-specialization:38-59` (anchor `arity` ✓), `inner-product-fold-specialization:30-59` (anchor `conjug` ✓). All the degenerate-cohort self-describing citations are byte-accurate. The warning is for the **Status-line pinpoints on the substantive KEEP themes**: the report cites the `## Status` heading line number (`ksp-solve-outer-driver.md:169`, `krylov-step-typed-wrapper-dissolution.md:291`, and analogously `:385`/`:423`/`:408`) but the `firm`/`substantive` prose token the citation quotes sits two lines below the heading (171, 293, …). `--anchor` reports these as `[DRIFT +2]`. The section is correctly identified and the quoted text is real; this is a consistent cite-the-heading-not-the-prose-line convention, off by the heading + blank line. Minor and uniform, not a wrong-location error.

**surface-or-evidence — pass.** Not a refinement proposal — this is an observation-only audit (no `book/` surface change proposed by D3 itself; the worklist is a classification artifact for cycle-050 enactment). The check no-ops on observation-kind reports. Each classification is backed by a self-describing-line citation, which is the appropriate evidence for a classification call.

**rotation-quality — pass.** The report's core claim is the inverse of a rotation claim: it asserts the 18 thin themes carry *no* rotation (degenerate identity-in-named-terms) and the 7 KEEP themes *do*. I verified both directions: the demoted themes self-describe as "identity-in-form on the body / no wrapper rotation / same signature" (confirmed on the 12 BLAS-1 leaves plus the 6 extension pairs), and the KEEP themes carry real shifts — `krylov-step-body-identity` has two wrapper rotations (`(op,K,s)`→`IterState` state-hiding + tail-recursion→outer-driver-by-role), the fold-specialization themes carry arity/conjugation dispatch + pinned-summation-order. The degenerate/genuine boundary is drawn correctly.

**variant-axis-coverage — pass.** The relevant axis here is the L3>L2 vs L2>L1 edge asymmetry on fold-member leaves, and the consumer-vs-member axis on `nrm2`. The report explicitly covers both (§A note on the asymmetry; the `nrm2` carve-out at both edges citing OQ `:595`). No hidden branch: the report enumerates all four sub-shapes (standalone leaf, constructed-operator gate, fused composite, operator-to-data leaf) and assigns each a verdict. The two gate pairs (divfree-projector, jacobi-smoother) are explicitly marked "verify" rather than asserted clean — an appropriate scoping-out of the un-read body interior.

**cross-reference-integrity — pass.** Confirmed all 18 theme files exist (`ls book/src/L3-L2/` + `L2-L1/`), all 7 KEEP theme files exist, the 8 non-cohort composition lowerings named in §C exist, and `L4-L3/krylov-step-typed-wrapper-dissolution.md` exists. OQ-ledger anchors `:594-595`, `:599`, `:651` resolve and say what the report claims (fork RATIFIED (b), nrm2 carved out as consumer-not-member, slug convention, normalize third sub-shape). The in-line-home targets (`book/src/L3/<op>.md` §"Downward to L2", etc.) are forward-references for cycle-050 enactment, appropriate for a worklist. No build-readiness fence guard applies (observation report, no proposed-changes fence).

**edge-label-fidelity — pass.** Every theme is labeled with its correct edge (`L3-L2/*-body-identity` = L3>L2, `L2-L1/*-leaf-identity` = L2>L1, `L4-L3/krylov-step-typed-wrapper-dissolution` = L4>L3) and the prose discusses that exact edge. The L3>L2-demotes-to-inline / L2>L1-fold-member-absorbs asymmetry is reasoned per-edge correctly.

**plan-kind-consistency — pass.** Declared as an observation (`status: pending`, observation-kind "Consistency drift (cohort-boundary classification)"); content matches — no authored surface, a classification worklist + a scope finding. Consistent with the dispatch brief (observation-only, no book mutation).

**skill-uptake-survey — warning.** The audit is exactly the shape `verify-citation-range` / `tools/citecheck/` was built for (18-theme self-describing-line byte-verification) and a phase-1-style cohort-reduction audit, yet the report does not state which skill/tool it invoked for the byte-accuracy of its self-describing citations. The citations are in fact accurate (I confirmed via citecheck), so this is telemetry only, not a correctness issue — pure presence-check miss.

### Issues found

1. **(citation-validity, minor) Status-line pinpoints on KEEP themes drift +2 from the quoted token.** `CYCLE.md` §(2) table and §Supporting-evidence cite `ksp-solve-outer-driver.md:169`, `krylov-step-typed-wrapper-dissolution.md:291`, `orthogonalize-variant-split.md:385`, `chebyshev-nested-recurrence.md:423`, `eigsolve-opaque-eigen-iteration.md:408` — these are the `## Status` *heading* lines; the `firm`/`substantive` prose the report quotes is at heading+2 (171, 293, …). `--scan` passes (in-bounds); `--anchor` flags `[DRIFT +2]`. Repair (optional): retarget to the prose line or widen to `:169-171`. Does not affect any verdict.

2. **(no-book-mutation cross-check — NOT a D3 defect, integrator must note) `book/src/L2/inner_product.md` carries an uncommitted modification, authored by the parallel D2 sibling, not D3.** `git status --short book/` shows `M book/src/L2/inner_product.md`; the diff is the combinator-as-entry inversion (cycle-019→redirect rewrite, self-referencing "combinator-miner refactor-pass report"), mtime 12:15:57 — *before* D3's report (12:17:32). This is D2's (combinator-miner) in-flight write, which legitimately owns `inner_product`. **D3's "no `book/` mutation performed" claim is accurate for D3's own actions** — D3 authored nothing. Flagged so the integrator does not mis-attribute the dangling working-tree edit to this observation report; it belongs to the D2 dispatch and should be applied/reconciled through D2's report, not D3's.

3. **(reconciliation gap — real, integrator must close) The D1/D2 fold-specialization KEEP verdicts are cross-confirmed from theme content + OQ ledger, NOT from the sibling reports.** §Supporting-evidence and §Open-questions state the D1 combinator-miner `CYCLE.md` was empty at audit time (sibling parallel-in-flight). I confirm the D1 report is **now non-empty** (412 lines, written 12:16) — i.e., it landed after D3 read it. D3's caveat is honest and the predicted agreement is plausible (both fold-specialization themes are genuine arity/conjugation-dispatch translations, which I independently confirmed via the theme content), but the cross-check D3 flags as "required, not settled" is real: the integrator/meta-phase must reconcile this worklist against the now-landed D1 (and D2) maps before cycle-050 enactment, specifically the `nrm2`-consumer-not-member treatment (D3 follows the ledger `:595` carve-out; if D2's landed map treats `nrm2` as a member, that is a divergence to catch).

4. **(load-bearing finding — VERIFIED SOUND) the 12→18 scope expansion is correct.** I independently confirmed two of the six newly-flagged pairs carry the identical smell: `assemble-diagonal-body-identity.md:3-7` self-describes "identity-in-form on the body … same signature … value-thread-isomorphic on the primitive"; `reciprocal-body-identity.md:3-8` self-describes "identity-in-form on the body with no wrapper rotation … The body IS the identity." Also spot-confirmed the two gate themes D3 marked "verify" genuinely open "identity-in-form on the body" (jacobi-smoother: "one elementwise product `op.dinv ⊙ x`"; divfree-projector: "four-step composition … explicit at both layers"). D3's "verify the gate body before demoting" caveat is the right hedge — the gate interiors were read at heads only. Not an issue; recorded because the brief flagged this as load-bearing (demoting 12 and stranding 6 would re-create the mirrored floor — D3 correctly avoids that).

5. **(KEEP-set — VERIFIED SOUND, no mis-classification) no substantive theme is mis-classified as DEMOTE.** Confirmed the 6 substantive KEEP rows (krylov-step pair + ksp-solve-outer-driver + chebyshev-nested-recurrence + eigsolve-opaque + orthogonalize-variant-split) and the 2 fold-specialization KEEPs all carry a real vocabulary/organization shift (wrapper rotation / iteration-view erasure / arity-conjugation dispatch) and are off the worklist. No genuine translation was swept into the demotion set.

## Repair

### Fixes attempted

- **Finding 1**: Status-line pinpoints on the 5 substantive KEEP themes drift +2 from the quoted `firm`/`substantive` prose token (cite the `## Status` heading line, prose sits at heading+2).
  - **Decision**: repaired
  - **Action**: Verified each `## Status` heading line and the `firm`/`substantive` prose location by reading the cited files (`grep -n "^## Status"` + `sed` heading+0..+3). Confirmed the uniform `[DRIFT +2]`: heading at the cited line, blank line at +1, prose token at +2. Retargeted all five pinpoints to the prose line (heading+2) in `CYCLE.md` — both the §(2) table rows and the §Supporting-evidence block:
    - `ksp-solve-outer-driver.md` `:169` → `:171` (heading 169, `firm`/substantive prose 171)
    - `krylov-step-typed-wrapper-dissolution.md` `:291` → `:293` (heading 291, `firm` prose 293)
    - `orthogonalize-variant-split.md` `:385` → `:387` (heading 385, `firm` prose 387)
    - `chebyshev-nested-recurrence.md` `:423` → `:425` (heading 423, `firm` prose 425)
    - `eigsolve-opaque-eigen-iteration.md` `:408` → `:410` (heading 408, `firm` prose 410)
    Confirmed no stale pinpoints remain (`grep` clean). This is a mechanical off-by-2 pinpoint correction within repair authority (citation line range off by a small offset); does not affect any verdict.

- **Finding (skill-uptake-survey warning)**: report does not state which skill/tool (`verify-citation-range` / `tools/citecheck/`) it invoked for the byte-accuracy of its self-describing citations.
  - **Decision**: not-needed
  - **Rationale**: telemetry-only presence-check miss per the critic; the citations are in fact byte-accurate (critic confirmed via citecheck). No correctness defect, no content change implied. Left as-is.

- **Findings 2, 3 (integrator-facing notes D3 surfaced)**: the D2 dangling working-tree edit on `book/src/L2/inner_product.md` must not be mis-attributed to D3; the D1/D2 reconciliation gap on the fold-specialization KEEPs (esp. `nrm2` consumer-vs-member) must be closed before cycle-050.
  - **Decision**: not-needed (not D3 defects)
  - **Rationale**: These are correct observations D3 surfaced, not D3 defects. D3 is observation-only and the critic confirmed D3 authored nothing in `book/` — the `M book/src/L2/inner_product.md` working-tree edit is D2's (combinator-miner) in-flight write, mtime-before D3's report. The reconciliation gap is a real cross-check the integrator must close, but it is not a repairable CYCLE.md defect. Left in the report to carry forward to the integrator.

- **Findings 4, 5 (load-bearing findings VERIFIED SOUND by critic)**: the 12→18 scope expansion is correct; no substantive theme mis-classified as DEMOTE.
  - **Decision**: not-needed
  - **Rationale**: Critic independently verified both sound. No defect.

### Unrepairable findings

None. The sole repairable finding (the +2 pinpoint drift) was repaired; the remaining findings are telemetry-only or non-defect integrator-forward observations.

## Suggested resolution

`ready`. Notes for the integrator:

- D3 is observation-only — apply nothing from D3 to `book/`. The worklist is a cycle-050-consumable classification artifact, not a proposed-changes block.
- Do NOT mis-attribute the uncommitted `M book/src/L2/inner_product.md` working-tree edit to D3 — it belongs to the parallel D2 (combinator-miner) dispatch and must be applied/reconciled through D2's report.
- Before cycle-050 enactment, reconcile this worklist against the now-landed D1/D2 maps — specifically the `nrm2` consumer-not-member treatment (D3 follows OQ-ledger `:595`; catch any divergence if D2's landed map treats `nrm2` as a fold member).
- The 18-vs-12 scope-boundary finding is surfaced for the cycle-050 dispatch-scope decision (treat all 18, or sequence the extra 6 to cycle-051 as a deliberate choice).
