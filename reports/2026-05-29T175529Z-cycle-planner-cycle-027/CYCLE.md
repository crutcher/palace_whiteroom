---
agent: cycle-planner
invoked_at: 2026-05-29T17:55:29Z
scope: cycle-027 dispatch plan
status: pending
---

# Cycle 027 dispatch plan

**Meta-batch-7 context:** This is the THIRD / FINAL primary cycle of meta-batch-7 (cycles 025/026/027). The meta-phase fires after THIS cycle's integrator-finalize and will handle role-spec strengthening (codemap drift correction), OQ-ledger unification, and integrator-signals.md archival. No dispatch work is assigned to meta-phase prep; all 12 planning slots go to forward-frontier work.

## Goals selected this cycle

Cycle-026 completed all seven active-head picks (NLEPS/eigsolve citation-hygiene + normalize + incremental-least-squares + matrix-weighted-norm L1>L0 theme + firm-theme audit cohort). **Cycle-027 shifts to two threads: (A) immediate carry-forward hygiene from cycle-026 (4 re-anchors + lowering-verifier audits + L1>L0 theme authorship), and (B) high-fan-out forward-frontier completion** (the L2>L1 `incremental-least-squares-composition-lowering` theme + L1 `ls_update_column` leaf that unblock krylov-step further lowering; the `l2-ksp-solve-materialise-iterate` cite-tightening that unblocks downstream krylov/GMRES work). Both threads are HIGH fan-out: the incremental-least-squares L2>L1 theme unblocks reusable `ls_update_column` and cascades into GMRES/FGMRES restart machinery (roadmap intermediate-tier impact score top-3). The re-anchors close cycle-026's carry-forward signal and clear the citation-hygiene friction pattern (3 OQs resolved, 1 addressed-at-L0 with residual follow-up). Together, they firm up the krylov-step / GMRES core ahead of higher-tier restart/restart-machinery work.

## Dispatches

| # | Agent | Scope | Deps | Rationale |
|---|-------|-------|------|-----------|
| 1 | `abstractor` | `normalize-mutation-rotation` L1>L0 theme | none | **HIGH fan-out — simplifies every Krylov-solver lowering that currently factors `normalize` into `nrm2∘scal`.** Firm L1 `normalize` operator landed cycle-026 (decision-YES on fused primitive). The `linalg::Normalize(x) = (norm(x), x/norm(x))` lowering is authorable. Carry-forward from cycle-026 integrator-signals suggested-next #1. |
| 2 | `lifter` | `matrix-weighted-norm-l1-entry-reanchor` + carry-forward hygiene re-anchors | none | **MEDIUM fan-out — citation-hygiene completion + closes 3-cycle drift pattern.** Four mechanical re-anchors from cycle-026 integrator-signals carry-forward: (a) `L1/matrix-weighted-norm.md:58,83` (operator.cpp:601 brace-boundary +1 drifts); (b) `L0/linalg-operator-file.md:33` Category-4 workspace mislabel (co-keyed with D3); (c) `concepts/givens.md:29` source-cite staleness (gmres.md→iterative.cpp); (d) `L1/bilinear-form.md:416` dot_bilinear provenance-note refresh (post-cycle-026-repoint residual). Friction-ledger `citation-drift-verify-not-self-invoked` + carry-forward OQ dispositions. |
| 3 | `lowering-verifier` | `matrix-weighted-norm-mutation-rotation` `verified_against:` audit + paired `bilinear-form-mutation-rotation` audit / firm-promotion | 1 | **MEDIUM fan-out — audit the now-firm matrix-weighted-norm L1>L0 theme + close the bilinear-form firm-promotion gate.** Standard `verified_against:` audit on D1 (cycle-026) stub→firm promotion. The paired `bilinear-form-mutation-rotation` L1>L0 theme (forward-referenced plain-text in D1, needs auditing when authored) + the `bilinear-form` L1 rough-in firm-promotion gate (test-coverage + variant-axis). Both routes carried by plan `matrix-weighted-norm + bilinear-form firm-promotion` (Medium). |
| 4 | `abstractor` | `incremental-least-squares-composition-lowering` L2>L1 theme | none | **HIGH fan-out — unblocks L1 `ls_update_column` leaf (D5) AND closes `l2-named-composition-lifts` cohort (orthogonalize + incremental-least-squares both now harvestable).** The L2 `incremental-least-squares` operator (firm c026) describes the running-QR / Givens-rotation stream; its L2>L1 lowering decomposes into base L1 leaves (`dot`, `axpy`, `scal`, `normalize`+identity, etc.) + the terminal `back_solve`. The theme follows the precedent `orthogonalize-composition-lowering` (firm c019). Unblocks forward-frontier krylov-step/GMRES work. Carry-forward from cycle-026 integrator-signals + roadmap intermediate-tier impact. **Gate:** firm L2 operator + firm L1 leaves. |
| 5 | `harvester` | `ls_update_column` L1 leaf | 4 | **MEDIUM fan-out — harvests the atomic `back_solve` step used in incremental-least-squares + GMRES least-squares update.** A small, reusable L1 primitive: `ls_update_column :: (LsqState) -> { x_new: Tensor[n], iter: int }`, solving the triangular system from the Hessenberg matrix. Dependencies: `trsv` (or its L1 wrapper if not yet firmed), small-dense kernel. Pairs with D4 theme; carries both `ls_update_column` + potentially `givens_apply` leaf refinement. |
| 5b | `lifter` | `l2-ksp-solve-materialise-iterate-cite-tightening` | 4 | **MEDIUM fan-out — cite-tightens the ksp_solve §Semantics phase-3 `materialise_iterate` to the now-firm L2 `incremental-least-squares` operator.** Gate satisfied (L2 operator firm c026). Mechanical cite upgrade on `book/src/L2/ksp_solve.md` (forward-reference prose now resolves to live link). Unblocks downstream GMRES/FGMRES theme / krylov-step re-closure work. Routed from cycle-026 integrator-signals + plan `l2-ksp-solve-materialise-iterate-incremental-least-squares-cite-tightening` (Medium). |
| 6 | `lowering-verifier` | `incremental-least-squares-composition-lowering` `verified_against:` audit | 4 | **LOW-MEDIUM fan-out — audit the L2>L1 theme (D4) for surface-form exhaustiveness + carry-forward evidence.** Standard `verified_against:` block on a firm L2>L1 named-composition theme (sibling to orthogonalize-composition-lowering c019). Covers the running-QR / Givens-rotation stream + terminal back_solve + variant-axis (pc_side + flexible). Unblocks cross-layer census of the restart machinery vocabulary. |
| 7 | `same-layer-cross-cutter` | `bilinear-form-variant-axis-audit` + mutual-consistency with `matrix-weighted-norm` | 3 | **LOW-MEDIUM fan-out — variant-axis exhaustiveness + test-coverage gate closure for the rough-in `bilinear-form` L1 operator.** Audit the element-type + weight-operator-representation axes (real vs complex; diagonal, sparse, matrix-free) against the now-firm `matrix-weighted-norm` L1>L0 theme's Sub-pattern A/B/C coverage. Gate: test coverage for at least (real `B`, complex `x`), (complex `B`, complex `x`), and identity-`B` collapse. Closes the High-priority plan item `matrix-weighted-norm + bilinear-form firm-promotion`. |
| 8 | `cross-layer-cross-cutter` | `ksp-solve-outer-driver-l3-boundary-semantics-check` | 5b | **LOW fan-out — audit the L3>L2 boundary for ksp_solve outer-driver semantics (one-pass vs iterate-all-residuals).** Scope: verify the L3 entry's loop/dispatch vs the L2 `materialise_iterate` phases align; spot-check the L3 `outer_driver` obstruction-theme narrative against current Palace `ksp.cpp` line-sweep. Non-status-reducing (L2 firm, L3 rough-in); a consistency audit. Preparatory for future L3 ksp_solve firm-promotion / GMRES/CG driver lift work. Low fan-out per scope (single cross-check vs N-dispatch impact), but unblocks higher-tier driver work. |
| 9 | `layer-intro-author` | `L1/index.md` firm-count + vocabulary-cohort refresh | 2, 3, 7 | **LOW fan-out — narrative refresh of the L1 index after normalize (D2) + matrix-weighted-norm (D2 + D3) landings.** Updates: (i) `Firm (19)→(20)` motif at §Overview; (ii) the normalize / matrix-weighted-norm bullets in §Vocabulary cohort; (iii) the normalize / matrix-weighted-norm/bilinear-form dep-map rows. These edits should have landed with D2/D3 dispatches; they were correctly deferred to layer-intro-author scope. No wait-path; the changes are read-only refreshes on already-firm entries. Bundles with any L1-index housekeeping. |

## Overlap analysis

**Wave structure:** Dispatches are organized into overlapping groups. Most are **parallel-when-indepedent**; three have dependencies (listed in Deps column).

**Parallelism:**
- **D1 (normalize theme)** and **D2 (hygiene re-anchors)** are **PARALLEL**: D1 writes `L1-L0/normalize-mutation-rotation.md` (NEW); D2 writes edits to `L1/matrix-weighted-norm.md` (entry append-only), `L0/linalg-operator-file.md`, `L1/bilinear-form.md`, `concepts/givens.md` (disjoint from D1's new file).
- **D3 (matrix-weighted-norm audit)** depends on **D1** being complete (the audit may reference the just-landed normalize theme as a sibling sub-pattern or cross-layer cite). However, the audit is on the **matrix-weighted-norm-mutation-rotation** THEME (not entry), which landed firm cycle-026; D1 adds the **normalize-mutation-rotation** THEME. These are in **different files** (`L1-L0/matrix-weighted-norm-mutation-rotation.md` vs `L1-L0/normalize-mutation-rotation.md`) and the audit does NOT block on D1. **D3 is PARALLEL with D1/D2 UNLESS the normalize theme carries a cross-cite to matrix-weighted-norm** (it doesn't — they are independent lowerings of distinct L1 operators). Mark **D3 PARALLEL with D1**.
- **D4 (incremental-least-squares L2>L1 theme)** is **PARALLEL** with D1/D2/D3 — it writes a NEW `L2-L1/incremental-least-squares-composition-lowering.md` file.
- **D5 (ls_update_column harvest) DEPENDS on D4** — the theme narrates how the L2 composition lowers, and the L1 leaves (including `ls_update_column`) are discovered as part of that decomposition. D5 must see D4's proposed-changes to know what L1 leaves to harvest.
- **D5b (ksp_solve cite-tightening) DEPENDS on D4** — the forward-reference target is the new L2>L1 theme, so the cite upgrade must see it on-disk (or at minimum, see D4's finalization). Mark **D5b as a SEQUENTIAL follow-up to D4 (after D4 integrates and finalize runs)**, OR **run it in the same integration wave as D4 (let integrator-per-report for D4 apply D5b after landing D4)**. For simplicity, mark **D5b DEPENDS on D4** (integrator-per-report order).
- **D6 (incremental-least-squares-composition L2>L1 audit) DEPENDS on D4** — audits the theme D4 authors.
- **D7 (bilinear-form variant-axis audit) DEPENDS on D3** — audits the theorem-coverage of matrix-weighted-norm-mutation-rotation (D3) against bilinear-form; logical dependency on D3's completion, though D7 reads from the existing artifact. For safety (to ensure D3's audit lands before D7 surveys it), mark **D7 DEPENDS on D3**.
- **D8 (ksp-solve boundary audit) DEPENDS on D5b** — the cite-tightening in D5b may reveal whether the L3 boundary narrative aligns with the L2 phases. Logical dependency to ensure D5b's materials are visible. Mark **D8 DEPENDS on D5b** (sequential, but low-criticality cross-check).
- **D9 (L1 index refresh) DEPENDS on D2 (matrix-weighted-norm entry touched), D3 (matrix-weighted-norm theme firm), D7 (bilinear-form audit complete)** — reads off the results of these three, so depends on all three.

**Sequencing:**
- **Wave 1 (parallel):** D1, D2, D4 (independent new/edit artifacts, no conflicts).
- **Wave 2 (sequential after Wave 1):** D3, D5, D5b, D6 (D3/D5/D6 all depend on upstream [D1/D4] or each other; D5b depends on D4).
- **Wave 3 (sequential after Wave 2):** D7, D8 (D7 depends on D3; D8 depends on D5b).
- **Wave 4 (final, sequential after Wave 3):** D9 (depends on D2, D3, D7).

**Artifact contention check:**
- `L1-L0/index.md`: D3 inserts a row (matrix-weighted-norm row was inserted as part of D3 logic). **D1 does NOT touch this file** (new theme file only). **No contention between D1 and D3 at this level.**
- `L1/index.md`: D2 may touch if the hygiene includes a re-anchor of `L1/matrix-weighted-norm.md`. **D9 also writes** `L1/index.md` (count + motif refresh). **D2 and D9 touch the same file but different regions** (D2 edits the specific matrix-weighted-norm entry lines `:58,83`; D9 edits the overview motif §count + the depmap rows for normalize/matrix-weighted-norm/bilinear-form). **Potential overlap if D2 and D9 modify adjacent lines**, but they are on different logical anchors → **mark D2 and D9 as sequential** (D2 first, then D9 after D3/D7 land; implement as `D9 DEPENDS on D2`).
- `L0/linalg-operator-file.md`: D2 edits (Category-4 mislabel). **No other dispatch touches this file** → **safe parallel**.
- `L2/ksp_solve.md`: D5b edits (cite upgrade). **No other dispatch touches this file** → **safe parallel**.
- `L2-L1/incremental-least-squares-composition-lowering.md`: D4 (new file), D6 (audit on the same file). **D4 and D6 contend on the same file** → **D6 DEPENDS on D4** (already marked).
- `concepts/givens.md`: D2 edits (:29). **D5/D5b may reference givens as a concept in the ls_update_column leaf / incremental-least-squares-composition theme.** If D5 (or D4) forward-references givens, they must leave it as plain-text (givens is still a rough-in concept and may not be live-linked). **D2's edit to :29 is a staleness fix (gmres.md→iterative.cpp source-cite), not a status change**, so no conflict with new forward-refs from D4/D5.

**Verdict:** The above dependencies are load-bearing for semantic closure (themes depend on leaves, audits depend on themes, index refresh depends on multiple landings). **Recommend strict sequential ordering on the dependency chain: Wave 1 → Wave 2 → Wave 3 → Wave 4.** However, **D1/D2 CAN be parallel with D4 (independent trees), and D3/D6 can run in parallel (both audit-only, no new claims) IF desired for throughput.** The integrator-per-report series execution is the binding constraint (per role-spec, they run one-at-a-time), so actual parallelism is at critic/repairer/integration-gate levels.

**Simplified Wave plan for integrator:**
- **Wave 1 parallel:** D1, D2, D4 (then integrator-per-report applies them serially in order 1→2→4; order among them does not matter since they do not touch overlapping files)
- **Wave 2 sequential after W1:** D3, D5, D5b, D6 (in order 3→5→5b→6; integrator-per-report applies them serially)
- **Wave 3 sequential after W2:** D7, D8 (in order 7→8; integrator-per-report applies them serially)
- **Wave 4 final:** D9 (applies after W3)

## Sequencing schedule

```
Wave 1 (parallel, integrator-per-report applies serially 1→2→4):
  - D1: abstractor, normalize-mutation-rotation
  - D2: lifter, matrix-weighted-norm-l1-entry-reanchor + hygiene
  - D4: abstractor, incremental-least-squares-composition-lowering

  [integrator-per-report completes; integrator-finalize rebuilds]

Wave 2 (sequential after W1):
  - D3: lowering-verifier, matrix-weighted-norm-mutation-rotation audit
  - D5: harvester, ls_update_column leaf
  - D5b: lifter, l2-ksp-solve-materialise-iterate cite-tightening
  - D6: lowering-verifier, incremental-least-squares-composition audit

  [integrator-per-report completes; integrator-finalize rebuilds]

Wave 3 (sequential after W2):
  - D7: same-layer-cross-cutter, bilinear-form variant-axis audit
  - D8: cross-layer-cross-cutter, ksp-solve boundary semantics check

  [integrator-per-report completes; integrator-finalize rebuilds]

Wave 4 (final):
  - D9: layer-intro-author, L1/index.md refresh

  [integrator-per-report completes; integrator-finalize final commit/push]
```

**Rationale:** Waves 1/2/3 are chunked to allow build+safety-net verification between logical groups (W1 creates the two new theme files + hygiene edits; W2 audits those + harvests leaves; W3 does cross-layer/layer checks). Wave 4 is final because the index refresh may depend on reading artifact state from W3. This sequencing is **conservative but safe** — it ensures forward-references resolve and cross-file consistency is verified before the next wave runs.

## Open questions / caveats

1. **D5b integration timing:** The `l2-ksp-solve-materialise-iterate-cite-tightening` is marked as depending on D4 (the incremental-least-squares-composition-lowering theme must land before the cite can be upgraded to a live link). However, **if finalize does a book rebuild after D4 lands, the cite-tightening could also run in the same integrator wave as D4** (integrator-per-report would apply D4, finalize rebuilds, then integrator-per-report applies D5b, finalize rebuilds again). Marking it as "Wave 2" assumes the planner intends the cite-upgrade to run after finalize verification of D4. **If the planner prefers to run D5b in the same per-report batch as D4, recommend scheduling D5b immediately after D4 in the integrator's queue** (e.g., D4 then D5b in sequence). The sequencing plan above keeps them separate for logical clarity.

2. **D7 + D3 contention risk:** D7 (bilinear-form variant-axis audit) reads from the now-firm `matrix-weighted-norm-mutation-rotation` theme (D3, a lowering-verifier audit that appends a `verified_against:` block). The audit is read-only; no contention. However, **if D7 discovers a gap in variant-axis coverage that D3's audit should have caught, the feedback loop back to D3 is closed (D3 is already applied by Wave 2)**. This is acceptable per methodology (audits are meant to catch gaps; if one surfaces, it's logged as a follow-up OQ, not a re-dispatch). **No action required; flagged for meta-phase oversight.**

3. **D8 (boundary semantics) scope caveat:** The `ksp-solve-outer-driver-l3-boundary-semantics-check` is scoped as a "non-status-reducing, consistency audit" — it does NOT land any new claims or status changes, just verifies narrative alignment. **If the audit discovers a material semantic gap (e.g., the L3 outer-driver semantics contradicts the L2 materialise_iterate phase structure), escalate to the planner or mark as a follow-up OQ for a subsequent harvester/abstractor/lowering-verifier dispatch.** For this cycle, assume the audit is **benign spot-check**, not a blocker.

4. **L1 index count refresh (D9) cadence:** The `Firm (19)→(20)` motif bump should have landed with D2 (normalize operator firm c026) or D3 (matrix-weighted-norm L1>L0 theme firm c026). The plan deferred it to layer-intro-author scope (per the dispatch's own note that the count-bump is layer-intro-author territory, not producer). **D9 is a cleanup pass; if the index was not auto-counted by the integrator, the motif will still read "19" after W1/W2/W3.** No blocker — D9 is meant to refresh it. **Confirm with integrator that the count refresh is in-scope for layer-intro-author vs integrator-finalize (normally layer-intro-author owns narrative refresh, but counts are a gray zone).**

5. **Carry-forward re-anchor residuals:** D2 routes four re-anchors from cycle-026 integrator-signals. One of them — the `bilinear-form-dot-bilinear-provenance-note-refresh` — is a residual from cycle-026 D5 (the layer-intro-author naming sweep that re-pointed stale `dot_bilinear` references but left the `bilinear-form.md:416` provenance note as stale because it's in the harvester-owned L1 entry, append-only-after-integration). **This residual is correctly delegated to D2 (lifter can edit L1 entries if it's a cite/name refresh, not semantic change); confirm scope with the lifter agent.**

---

**Note for meta-phase (informational only; do not action):** Codemap `read_range` +1 brace-boundary drift has been confirmed THREE times across cycles 024/025/026. Batch-7 meta-phase should strongly consider the integrator-signals.md carry-forward recommendation to strengthen role-specs: "codemap is localization-only; citecheck/on-disk is the citation source of truth." The `tools/citecheck` tool is now wired (batch-6 meta-phase enactment), and standing citecheck gates are feasible. Friction-ledger `codemap-read-range-plus-one-drift-on-brace-boundary` + OQ `codemap-read-range-plus-one-drift-on-brace-boundary` (open, awaiting meta-phase action) carry the full context.

