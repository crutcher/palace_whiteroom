---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T071500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
---

# META: verification of cycle-042 D11 L2 / L2-L1 / L3-L2 index refresh (sole count-owner)

## Critique

### Checks run

**citation-validity — pass.** This is a narrative/structural count-refresh; the report emits no NEW L0 citations (it states so explicitly, §Open-questions last bullet — `citecheck` not applicable). The few source anchors quoted (`rap.cpp:163-164`, `vector.cpp:248-261`, `test-libceed.cpp:367-376`) are transcribed verbatim from the producers' already-verified rows, not independently re-cited, and are used only as supporting color. No `verified_against:` block is present, so the YAML round-trip sub-check no-ops. The load-bearing claims here are *counts*, which I verified against on-disk tables directly (see below) rather than against file:line citations. Pass.

**surface-or-evidence — pass.** Not a refinement of an existing operator/theme's algebraic surface — it is a consolidated-tally + orientation-prose refresh of three Part-overview indices (the count-owner's narrative sections). The "surface" being modified is index prose; there is no rotation_claim to evidence. Not applicable to an index-refresh report in the refinement sense; pass.

**rotation-quality — pass.** No algebraic/structural rotation is asserted by this report. It records (does not author) the cohort's identity-in-form / one-`AddMult`-de-fusion character, all sourced to the D2–D10 producers. Not applicable to an index refresh; pass.

**variant-axis-coverage — pass.** No operator variant-axis decomposition is authored here. The report correctly relays the producers' axis notes (e.g. `reciprocal` single element-type axis; `elementwise_product` element-type / conjugation axes) without making coverage claims of its own. Not applicable; pass.

**cross-reference-integrity — warning.** I verified all ten `[old]` anchors against on-disk verbatim text. **Nine of ten match exactly and are complete-paragraph anchors** (edits 1,2,3,5 in `L2/index.md`; 6,7,8 in `L2-L1/index.md`; 9,10 in `L3-L2/index.md`). **Edit 4's `[old]` anchor is TRUNCATED** — see Issues. All `[link]` references inside the `[new]` text resolve: the new `[`reciprocal`](./reciprocal.md)` / `[`elementwise_product`](./elementwise_product.md)` / `[`assemble-diagonal`](./assemble-diagonal.md)` / `[`jacobi-smoother`](./jacobi-smoother.md)` / `[`divfree-projector`](./divfree-projector.md)` links point at chapters D2–D6 create in the same cycle (live links resolve post-integration given the serial D2–D6-before-D11 ordering the report flags); `[`ksp_solve`](./ksp_solve.md)` exists on disk. The cross-cutter audit dir `reports/2026-06-01T063231Z-cycle-042-cross-cutter-leaf-vs-fold-audit/` referenced in edits 4/8/10 EXISTS. Warning is driven solely by the edit-4 truncation.

**edge-label-fidelity — pass.** The three indices' edges are correctly oriented throughout: L2 (operator floors), L2>L1 `-leaf-identity` edges, L3>L2 `-body-identity` edges. The report consistently keeps L2>L1 vs L3>L2 separated (edit 6 = L2>L1 leaf-identity edges; edits 9/10 = L3>L2 body-identity edges), and the `divfree-projector` one-`AddMult` de-fusion is correctly attributed to the L2>L1 edge (edit 6) and explicitly disclaimed from the L3>L2 edge ("the step-4 `AddMult` de-fusion is the L2>L1 edge's content, NOT this edge's", edit 9 `divfree-projector-body-identity`). No edge-label/prose mismatch. Pass.

**plan-kind-consistency — pass.** Declared shape is a count-owner index refresh; content matches (narrative-only, no row re-emission, no chapter bodies). All five floors are relayed as `firm`, all ten themes as `firm`, `deflate`/`deflate-composition-lowering` held `partly-constructive` and excluded from firm counts — consistent with the cohort the report describes. The status-tier vocabulary is used correctly. Pass.

**skill-uptake-survey — pass (telemetry).** A count-refresh has no strongly-implied skill to invoke (`citecheck` correctly declared N/A; no `verified_against` round-trip; no fence-truncation guard needed for an `edit:`-block-only report). No skill-uptake gap. Pass.

### Count / count-ownership verification (the focus checks)

I verified the consolidated tallies directly against on-disk tables (D2–D10 row-edits are NOT yet on disk at critique time, as expected — they integrate per-report before D11):

- **L2/index.md** — 13 dep-map rows on disk: `krylov-step`, `chebyshev-iteration`, `linear_combination`, `scal`, `inner_product`, `dot`, `nrm2`, `orthogonalize`, `incremental-least-squares`, `ksp_solve`, `gram`, `deflate` (partly-constructive), `eigsolve`. = **12 firm + 1 pc**. Report "before = 12 firm" → CORRECT. +5 → 17 firm / 18 rows → CORRECT.
- **L2-L1/index.md** — 11 theme-list data rows on disk (10 firm + `deflate-composition-lowering` pc). Report "before = 10 firm" → CORRECT. +5 → 15 firm / 16 rows → CORRECT. Cohort-growth-log on disk reads "firm 7 → 10" for the c041 cohort, so 10 is the correct firm pre-c042 baseline.
- **L3-L2/index.md** — exactly 5 theme rows on disk, all firm: `krylov-step-body-identity`, `dot-body-identity`, `nrm2-body-identity`, `ksp-solve-outer-driver`, `scal-body-identity`. Report "before = 5 firm, 0 pc" → CORRECT. +5 → 10 firm → CORRECT.
- **coverage gap** — 5-of-18 → 10-of-18, remaining 8 ("8 still relying on inline") = 18−10 → CORRECT.
- **partly-constructive exclusion** — `deflate` / `deflate-composition-lowering` confirmed unchanged on disk and never folded into a firm count anywhere in the report (grep-verified). CORRECT.

**Count-ownership (D11 = SOLE tally writer) — clean.** D11's report contains NO dep-map / theme-list table rows (grep for `| [`reciprocal`]` etc. returns nothing); every `edit:` block targets only orientation prose, the Semantics-overlay motif list, and the Working-Notes consolidated tallies/cohort prose. No double-write of any D2–D10 row. The §Summary correctly disclaims row re-emission and the §Open-questions flags the D11-after-producers serial-ordering dependency for the integrator. The two meta-phase signals (leaf-vs-fold fork scoped to the c041 cohort + the c042 keep-leaf-floor-(b) audit recommendation; slug-naming `-leaf-identity`/`-body-identity` de-facto convention + the `elementwise_product` underscore-vs-hyphen split) are surfaced prominently and correctly scoped — the c042 standalone-floor cohort is consistently framed fork-INDEPENDENT / design-final. The underscore/hyphen claim is corroborated on disk: `concepts/elementwise-product.md` (hyphenated) exists while the L2 chapter is `elementwise_product.md` (underscored).

**Fence parity — pass.** Report has 20 ` ``` ` fence-lines (even), 10 `edit:book/...` blocks each opened+closed; balanced. The three target indices contain no code fences (0 each), so no nested-fence interaction. No fence-truncation defect.

### Issues found

1. **(cross-reference-integrity — MEDIUM) Edit 4's `[old]` anchor is truncated mid-paragraph and does not span the full on-disk bullet** — `CYCLE.md` §"Proposed changes" block 4 (`reports/2026-06-01T063231Z-cycle-042-layer-intro-author-index-refresh/CYCLE.md:90-93`), target `book/src/L2/index.md:91`. The `[old]` text ends at *"...The batch-12 meta-phase must **ratify or adjust** this design before the cohort is treated as stable."* But the on-disk bullet (line 91) continues for several more sentences after that point: *"*If it adopts the (a) fold-only reading,* the leaf floors (`dot` certainly; `scal` as the arity-1 member; `nrm2` is unaffected...) and their adjacent themes **re-anchor to the fold-parents**: the L2>L1 leaf-identity edges fold into `inner-product-fold-specialization` / `linear-combination-fold-specialization`, and the L3>L2 body-identity edges re-point their L2 RHS from a same-named leaf to the fold-parent. This is upstream of the whole cohort; surfaced here in the L2 Part overview so a reader navigating the floor cohort sees the design is provisional. (Recorded by D1/D2/D4/D5/D6 in their §Open-questions; consolidated as the batch-12 meta-phase OQ.)"* The replacement `[new]` text does NOT carry this continuation forward. Consequence: if the integrator requires exact full-paragraph anchor match, the edit will FAIL to apply; if it applies `[old]` as a substring match, the orphaned continuation (the "*If it adopts the (a) fold-only reading,* ... re-anchor to the fold-parents..." sentences) is left dangling immediately after the new text, producing a self-contradictory bullet (the new text says "the c042 cross-cutter audit recommends KEEPING leaf-floor (b)" immediately followed by the old conditional "*If it adopts the (a) fold-only reading,* ... re-anchor to the fold-parents"). The fix is to extend edit-4's `[old]` anchor to include the full on-disk bullet through *"...consolidated as the batch-12 meta-phase OQ.)"* (and decide whether the (a)-reading consequence prose should be retained, folded into the new audit-recommendation framing, or dropped — the `[new]` currently drops it). This is the only blocking-candidate issue in the report.

2. **(informational — LOW, not a defect of this report) D5 directive-name variant** — the report itself flags (§Open-questions, caveat 4) that D5's dep-map row cites the cohort directive as `l2-floor-under-l3-jacobi-smoother` rather than the canonical `l2-floor-under-l3-blas1-cohort` (extended). D11 correctly uses the canonical framing and correctly declines to edit D5's row (out of write-scope). Surfaced here only so the integrator/repairer can decide whether D5's row wants a one-word normalization at integration; it is NOT an issue with this report's content.

No other issues. Counts, count-ownership partition, partly-constructive exclusions, edge orientation, fence parity, and 9-of-10 anchors are all correct.

---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T071500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-01T073000Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

## Repair

### Fixes attempted

- **Finding** (Issue 1, cross-reference-integrity — MEDIUM): Edit 4's `[old]` anchor (`CYCLE.md` block 4, target `book/src/L2/index.md:91`) is truncated mid-paragraph — it ends at "...before the cohort is treated as stable." but the on-disk bullet continues with the "*If it adopts the (a) fold-only reading,*..." consequence prose through "...consolidated as the batch-12 meta-phase OQ.)". The `[new]` text dropped that continuation, so the edit would either fail full-paragraph match or leave an orphaned, self-contradictory continuation (the new keep-(b) recommendation immediately followed by the old (a)-fold-only re-anchor conditional).
  - **Decision**: repaired.
  - **Action**: Extended edit-4's `[old]` anchor in `CYCLE.md` (§"Proposed changes" block 4) to cover the complete on-disk bullet at `book/src/L2/index.md:91` — through "...consolidated as the batch-12 meta-phase OQ.)" — verified verbatim against the on-disk line. Extended the `[new]` text so the whole bullet reads coherently under the D1 keep-leaf-floor-(b) recommendation: the old (a)-fold-only consequence prose is **subsumed, not dropped** — reframed as a conditional counterfactual ("*Were the meta-phase to instead adopt the (a) fold-only reading* (against the audit's recommendation)...the leaf floors...would re-anchor to the fold-parents...") so the provisional-design note and the D1/D2/D4/D5/D6 §Open-questions provenance line are preserved. Added one bridging sentence keeping the meta-phase framing intact ("The decision remains the **batch-12 meta-phase's to make** — this is a recommendation, not an enactment."). The fork-INDEPENDENT cycle-042-cohort note is retained at the bullet tail. Surgical anchor extension only; no new substantive content authored — the continuation text is the producer's own (a)-branch prose re-cast from indicative to counterfactual mood.

### Unrepairable findings

None. The sole warning-driving finding (Issue 1) was mechanically repairable (anchor-extension + mood-recast of the producer's own prose, no new claims).

### Follow-up notes (non-blocking, recorded for the integrator / meta-phase)

- **Issue 2 (informational — LOW, not a defect of this report)**: D5's dep-map row (in the separate D5 report, out of D11's write-scope) cites the cohort directive as `l2-floor-under-l3-jacobi-smoother` rather than the canonical `l2-floor-under-l3-blas1-cohort` (extended). D11 (this report) correctly uses the canonical framing and correctly declines to edit D5's row. **No fix applied here** — D5's row lives in a different report and is out of this repairer's one-report scope. Recorded for the integrator to decide whether D5's row wants a one-word normalization at integration, or for the batch-12 meta-phase to fold into the slug-naming normalization pass already surfaced in edit-5.

## Suggested resolution

`ready`. The only blocking-candidate finding (edit-4 anchor truncation) is repaired: the `[old]` anchor now spans the full on-disk bullet verbatim and the `[new]` text reads coherently under the keep-leaf-floor-(b) recommendation with the (a)-branch consequence preserved as a counterfactual and the meta-phase-decides framing intact. Integrator note: edit-4 now relies on a longer full-paragraph anchor match — apply against `book/src/L2/index.md:91` as it stands at integration time (D2–D10 row-edits do not touch line 91, so the anchor is stable through the serial per-report ordering). The D5 directive-name variant (Issue 2) is a separate-report item left to integrator/meta-phase discretion.
