# Cycle-023 integrator staging log

Per-report integration landings, newest LAST (append-only). Read by integrator-finalize to reconcile the cycle.

---

## 2026-05-29T092943Z-harvester-nleps-deflated-solve-l1
applied_at: 2026-05-29T10:06:49Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/nleps_deflated_solve.md (new — firm L1 operator chapter; full body inside the `new:` fence, fence parity balanced 8/8)
- book/src/L1/index.md (edit — Firm count 16→17 headline; firm-list bullet after `lu_solve`; dep-map row after `lu_solve` row / before `lanczos_step`)
- book/src/SUMMARY.md (edit — `[nleps_deflated_solve]` entry after `[lu_solve]`, line 76)
- scaffolding/open-questions.md (append — 3 OQ sections)

Gate hits:
- (none non-zero) — all 4 anchored old→new pairs matched on-disk verbatim; no retroactive-budget hit; no forward-edge / edge-label / H1-reuse / append-on-missing-slug / variant-axis-missing issues; no SUMMARY auto-fix needed (report proposed the SUMMARY edit explicitly); no index-placeholder displacement; no implied-component stub creation.

Count delta:
- L1 firm: 16 → 17 (on-disk headline now reads `**Firm (17)**`). New firm operator: `nleps_deflated_solve`.

Open questions promoted:
- nleps-deflated-solve-firm-landed-deflate-promotion-gate-stays-open
- nleps-interior-atoms-remaining-jacobian-action-and-eigenvalue-correction
- nleps-deflated-solve-l1-l0-lowering-theme

Build-relevant: yes

Notes:
- KEY FINDING for finalize/meta-phase: this report's deflate-promotion verdict CONFIRMS (does not change) the cycle-022 L2 `deflate` `partly-constructive` status. The Gram `XᴴX` is built positively (`palace/linalg/nleps.cpp:529`) but only ever solved Schur-wrapped (`SS = −S.fullPivLu().solve(SS) = −S⁻¹·(XᴴX)`, `:533`); the bare `(XᴴX)⁻¹` Galerkin core never appears. `deflate` is NOT promoted this cycle, and this landing does NOT touch the L2 `deflate` entry (out of scope, correctly left untouched). The bare-Galerkin-core promotion still gates on a positive bare-Gram-solve site outside `nleps.cpp` (ROM / eigensolver-locking) — captured as OQ `nleps-deflated-solve-firm-promotion-gate-stays-open`.
- SHARED-FILE COORDINATION: `book/src/L1/index.md` is also touched by report #8 (L1-index refresh — §Semantics motif list + §Working Notes, DISTINCT regions). I took the Firm-count 16→17 headline (line 29), the firm-list bullet, and the dep-map row only. Report #8 (integrated later) should re-read disk to see these landings before editing the non-overlapping §Semantics/§Working-Notes regions. If report #8 also lands a firm L1 operator, finalize should reconcile the headline count beyond 17.
- All 9 live links in the new chapter (ksp_solve, lu_solve, dot, axpy, nleps_deflated_residual, eigsolve at L1; linear_combination, gram at L2; eigensolver-wrapper at L0) verified to resolve to existing files on disk.
- deferred integrated_at to finalize per role-spec (did NOT touch the consumed report's frontmatter).

---

## 2026-05-29T092943Z-layer-intro-author-l1-index-refresh
applied_at: 2026-05-29T10:34:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/index.md (edit ×2 — §Semantics motif list "Four"→"Six" + tightened motif-4 to "absorption-to-result" with full member set + appended motif 5 "Operator introspection" + motif 6 "Coordinate-space dense direct algebra"; §Working-Notes appended cycle-022 eigsolve-firm promotion bullet, the repaired tight back-reference form)
- scaffolding/open-questions.md (append — 1 OQ section)

Gate hits:
- (none non-zero) — both `[old]` anchors (§Semantics motif lead-in, §Working-Notes cycle-009 bullet) matched on-disk verbatim AFTER report #1's edits (distinct regions, as predicted); all 5 L0 citations in the new motif prose verified verbatim via codemap `read_range` + on-disk read (romoperator.cpp:762-764/:765/:756-758, nleps.cpp:533-535, operator.cpp:27, test-libceed.cpp:371); no retroactive-budget hit; no forward-edge / edge-label / H1-reuse / append-on-missing-slug / variant-axis-missing issues; no SUMMARY auto-fix needed (no new slug — pure refresh of existing index.md, already SUMMARY-registered); no index-placeholder displacement; no implied-component stub created; zero code fences in index.md (none added, balanced); all motif-prose links (./apply_linop.md, ./ksp_solve.md, ./assemble-diagonal.md, ./lu_solve.md) + unchanged L1-L0 theme links resolve on disk.

Count delta:
- NONE — navigational/prose refresh only. Did NOT touch the Firm-count header (line 29, `**Firm (17)**` — owned by report #1's nleps_deflated_solve +1) or the dep-map. The motif list (§Semantics) and Working-Notes bullet are count-agnostic and applied cleanly over report #1's landed state.

Open questions promoted:
- l1-semantic-motif-taxonomy-expanded-to-six-apply-linop-motif-7-watch

Build-relevant: yes

Notes:
- SHARED-FILE COORDINATION (the other side of report #1's note): this report edited book/src/L1/index.md in regions DISTINCT from report #1 (which took the Firm-count headline 16→17, the firm-list bullet after lu_solve, and the dep-map nleps_deflated_solve row). I re-read disk FIRST and confirmed report #1's three landings present (line 29 `**Firm (17)**`, firm bullet line 47, dep-map row line 85) before editing; my two anchors (§Semantics motif lead-in ~line 18, §Working-Notes cycle-009 bullet ~line 102) were untouched by report #1 and matched verbatim. No reconciliation needed.
- Applied the REPAIRED CYCLE.md content (META overall_status: ready): repair #1 trimmed the §Working-Notes cycle-022 bullet from a full per-law re-statement to a tight back-reference (defers full anchoring to §Vocabulary-cohort + dep-map row + eigsolve.md:165-171) — avoids triple-redundancy of the route-(b) basis in one file. Repair #2 re-anchored motif-6's citation from the wider `:757-764` to the pinpoint `:762-764` (QR comment) + `:765` (the fullPivHouseholderQr solve) + `:756-758` (rejected LDLT), matching the lu_solve entry-of-record; I verified all three ranges verbatim before applying.
- The `apply_linop` motif-7 question is NOT filed as a standalone OQ (producer + critic both judged it speculative / no-anchor; methodology invariant says don't park speculation). I folded it as the OPEN future-watch trigger inside the single taxonomy-expansion OQ, with the reassessment trigger (a firm opaque-operator-action L1 operator landing). Eigsolve-firm narrative: DISCHARGED (now landed in the §Working-Notes bullet; the operator is already firm on disk).
- deferred integrated_at to finalize per role-spec (did NOT touch the consumed report's frontmatter).

---

## 2026-05-29T092943Z-harvester-eigsolve-l2-entry
applied_at: 2026-05-29T11:18:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/eigsolve.md (new — firm L2 operator chapter; the named shift-invert spectral-transform composition `apply_shift_invert = apply_linop(M) ▷ ksp_solve((K − σM)⁻¹)`; full body inside the `new:` fence, fence parity balanced 6/6 — three `text` blocks; §"Lifts to" reference restored to LIVE link `[eigsolve](../L3/eigsolve.md)` since the L3 stub was materialized; `lowers_to:` frontmatter wording updated from "BLOCKED on this entry" → "predicted partial-obstruction" since no longer blocked)
- book/src/L3/eigsolve.md (new — `status: stub` claim-free placeholder; implied-component stub materialized per the "Integration may materialize implied components as stubs" directive; "Implied by" provenance + "Refinement pending (cycle-024 L3 backfill)" note; NO citations/claims — critic no-ops on it)
- book/src/L2/index.md (edit — dep-map firm `eigsolve` row appended after the `deflate` row / line 60; L2 firm dep-map count now 8)
- book/src/SUMMARY.md (edit ×2 — `[eigsolve](./L2/eigsolve.md)` after `[deflate]` under L2 Part; `[eigsolve (stub)](./L3/eigsolve.md)` after `[ksp_solve]` under L3 Part)
- scaffolding/open-questions.md (append — 4 OQ sections)

Gate hits:
- (none non-zero) — no retroactive-budget hit; no forward-edge / edge-label / H1-reuse / append-on-missing-slug / variant-axis-missing issues; no index-placeholder displacement.
- implied-component-stub-created (1): materialized `book/src/L3/eigsolve.md` as a `stub` per directive — clearly-implied (≥2 converging refs: L2 §"Lifts to" + `lowers_to:` frontmatter + chain step-3 + OQ `l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog`). Recorded as `applied-discretionarily`, rationale `implied-component-stub-created`. Opened OQ `eigsolve-l3-stub-materialized-cycle-024-backfill-refines-in-place` + the `eigsolve-l3-backfill` plan hook for the next harvester/lowering-verifier. The repairer's plain-text fallback (§"Lifts to") was UPGRADED back to a live link `[eigsolve](../L3/eigsolve.md)` now that the target exists.
- SUMMARY auto-fix: report proposed the L2 SUMMARY edit explicitly (applied verbatim). The L3-stub SUMMARY registration is part of the stub-materialization (the report did NOT propose it since the stub didn't exist at harvest) — registered under the L3 Part per the auto-fix convention.

Count delta:
- L2 firm: 7 → 8 (on-disk dep-map Status column shows 8 firm rows: krylov-step, chebyshev-iteration, linear_combination, inner_product, orthogonalize, ksp_solve, gram, eigsolve). New firm operator: `eigsolve`. (`deflate` stays partly-constructive, `incremental-least-squares` stays stub — correctly NOT counted.)
- L3: firm count UNCHANGED at 9 (krylov-step, apply_linop, axpy, axpby, axpbypcz, dot, nrm2, scal, ksp_solve are firm; chebyshev is partial-obstruction); +1 STUB (`eigsolve`). **Eigsolve prerequisite chain step 2 DONE → the L3 backfill (step 3) now has a home (the stub) and is unblocked.**

Open questions promoted:
- eigsolve-l2-firm-landed-chain-step-2-done-l3-backfill-unblocked
- eigsolve-l3-stub-materialized-cycle-024-backfill-refines-in-place
- eigsolve-l2-l1-spectral-transform-composition-lowering-theme-needed
- concepts-eigsolve-page-still-absent

Build-relevant: yes

Notes:
- VERIFICATION: all 19 relative live-links in book/src/L2/eigsolve.md resolve on disk (incl. the now-live `../L3/eigsolve.md` stub); fence parity 6 (even); firm apparatus (Signature, Algebraic laws, Status, Evidence) fully inside the entry. L3/eigsolve.md is claim-free (zero `file:line` citations), carries the `Status: stub` line + "Implied by" provenance + "Refinement pending" note, and both its links resolve (`./ksp_solve.md`, `../L2/eigsolve.md`).
- CHAIN STATUS for finalize/meta-phase: this is the cycle-022→023 eigsolve prerequisite chain — step 1 (L1 firm) landed cycle-022; step 2 (L2 firm entry) landed THIS report; step 3 (L3 backfill) is now unblocked with the stub as its home, predicted `partial-obstruction` (the cycle-021 `l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog` prediction). The upstream chain OQs (`open-questions.md:613`/`:624`/`:668`/`:676`) are left UNEDITED per role-spec — meta-phase owns the re-framing (mark step 2 done, promote step 3 actionable).
- SHARED-FILE COORDINATION: book/src/SUMMARY.md and book/src/L2/index.md may be touched by other reports in this cycle. I appended the L2 `eigsolve` dep-map row after the `deflate` row (verbatim anchor matched on-disk) and the two SUMMARY entries (after `[deflate]` for L2, after `[ksp_solve]` for L3); later reports should re-read disk to see these landings.
- deferred integrated_at to finalize per role-spec (did NOT touch the consumed report's frontmatter).

---

## 2026-05-29T092943Z-abstractor-lu-solve-mutation-rotation
applied_at: 2026-05-29T11:42:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/lu-solve-mutation-rotation.md (new — firm L1>L0 theme chapter; the small-dense direct-solve mutation rotation `x = lu_solve(A, b)` → inline Eigen `A.<kernel>().solve(b)` in place; two sub-patterns A NLEPS full-pivot-LU / B ROM full-pivot-QR; load-bearing factorization-kernel axis incl. rejected LDLT; applied the REPAIRED CYCLE.md content — the four inner code blocks are 4-space-indented, NOT nested ` ```text ` fences, so the full firm body Context→Status→Verified-against→Variant-axes lands intact; zero code fences in the written .md)
- book/src/L1-L0/index.md (edit — dep-map firm `lu-solve-mutation-rotation` row appended after the `assemble-diagonal-mutation-rotation` row / before the `minres-iteration` obstruction row)
- book/src/SUMMARY.md (edit — `[lu-solve-mutation-rotation](./L1-L0/lu-solve-mutation-rotation.md)` appended under the `# L1 > L0 — Lowering` Part after `matrix-weighted-norm-mutation-rotation (stub)`, before the `# L0` section)
- scaffolding/open-questions.md (append — 3 OQ sections)

Gate hits:
- (none non-zero) — no retroactive-budget hit (new firm theme creation, not a retroactive-evidence revision); no concept_writes-on-existing-slug (the target .md did not exist — clean `new:` create); no forward-edge-without-surface (L0 source surface + the firm L1 `lu_solve.md` anchor both exist); no edge-label/prose mismatch (edge L1>L0, prose narrates forward L1→L0; critic passed edge-label-fidelity); no H1-page-heading reuse (H1 = `# lu-solve-mutation-rotation`, the slug); no append-on-missing-slug (both `edit:` targets exist, anchors matched verbatim); no variant-axis-missing (§Variant axes enumerates 4 axes, factorization-kernel load-bearing axis exhaustively covered; critic passed variant-axis-coverage); no index-placeholder displacement (index.md has no `(empty — Phase B skeleton.)` placeholder); no implied-component stub created (no dangling plain-text forward-references); no SUMMARY auto-fix needed (report proposed the SUMMARY edit explicitly, applied verbatim); bookkeeping complete (report proposed BOTH the index.md dep-map row AND the SUMMARY entry).

Count delta:
- L1>L0 firm themes: +1 (`lu-solve-mutation-rotation` lands firm). On-disk `book/src/L1-L0/index.md` Theme-list table now carries the new firm row between `assemble-diagonal-mutation-rotation` (firm) and `minres-iteration` (obstruction). The L1>L0 Part has no headline firm-count integer to bump (the index uses a status-per-row table, not an aggregate count); finalize need only confirm the table row + SUMMARY entry render.

Open questions promoted:
- lu-solve-mutation-rotation-l1-l0-landed-firm-cycle-023
- lu-solve-mutation-rotation-lowering-verifier-audit-and-lu-solve-citation-tightening
- lu-solve-real-element-type-variant-permitted-but-unwitnessed

Build-relevant: yes

Notes:
- APPLIED THE REPAIRED CYCLE.md (META overall_status: ready). The critic's sole FAIL (cross-reference-integrity / build-readiness fence guard — the cycle-019 fence-truncation signature: nested ` ```text ` fences inside the `new:` block would truncate the firm body at the first inner fence) was repaired pre-integration: the repairer converted the four inner ` ```text … ``` ` blocks (§L1-form signature, §L0-form common skeleton, §Sub-pattern-A NLEPS, §Sub-pattern-B ROM) to 4-space-indented code blocks (the landed `dot-mutation-rotation.md` sibling convention). I wrote the .md with those four samples as 4-space-indented code blocks → the rendered chapter carries the FULL firm apparatus (Context, L1/L0 forms, both sub-patterns + all citations, §factorization-kernel axis, §in-place-RHS-overwrite, §Applicability, §Justification, §Speculative-operators=None, §Verified-against, §Variant-axes, AND `## Status`=firm). Zero triple-backtick fences in the final .md.
- VERIFICATION: all 9 relative live-links in the new chapter resolve on disk — `../L1/lu_solve.md`, `../L1/apply_linop.md`, `../L1/ksp_solve.md`, `./dot-mutation-rotation.md`, `./nrm2-mutation-rotation.md`, `./ksp-solve-mutation-rotation.md`, `./apply-linop-mutation-rotation.md`, `../L2/deflate.md`, `../L2/gram.md`.
- SHARED-FILE COORDINATION: `book/src/SUMMARY.md` was touched earlier this cycle by reports #1 (L1 `nleps_deflated_solve` entry, line ~78), #3 (L2 `eigsolve` + L3 `eigsolve (stub)` entries) — all in DISTINCT Parts. My edit is in the `# L1 > L0 — Lowering` Part (after `matrix-weighted-norm-mutation-rotation (stub)`), untouched by the prior three reports; I re-read SUMMARY.md FIRST and confirmed the anchor verbatim before editing. `book/src/L1-L0/index.md` was NOT touched by any prior cycle-023 report (reports #1/#2 touched L1/index.md; #3 touched L2/index.md) — my dep-map row insert is the first L1-L0/index.md edit this cycle; anchor (`assemble-diagonal-mutation-rotation` row + `minres-iteration` row) matched verbatim on disk. No reconciliation needed. Remaining reports #5/#6 (if any touch SUMMARY/L1-L0) should re-read disk to see this firm row + SUMMARY entry.
- NLEPS-COHORT PROGRESS for finalize/meta-phase: this firm L1>L0 theme discharges item (c) of the cycle-022 `nleps-deflation-lowering-chain-substantially-anchored-post-cycle-022` OQ for the `lu_solve` half — the `lu-solve-mutation-rotation-l1-l0` plain-text forward-reference (cited `:656` in the cycle-022 `gram`/`deflate`/NLEPS-cohort OQs) is now a firm chapter. The `nleps_deflated_residual` (`:698`) and `nleps_deflated_solve` L1>L0 lowering themes remain plain-text forward-references (NLEPS-cohort items still open).
- OQ #4 of the report (reverse-direction L0→L1 lifting prerequisites) was NOT promoted as a standalone OQ — it is a working-notes-only quarantined note per the CLAUDE.md high→low layer-definition discipline (not a deliverable question; the critic confirmed it is correctly OUTSIDE the chapter body). Captured implicitly in the landing-record OQ's high→low framing.
- deferred integrated_at to finalize per role-spec (did NOT touch the consumed report's frontmatter).

---

## 2026-05-29T092943Z-abstractor-nleps-deflated-residual-mutation-rotation
applied_at: 2026-05-29T12:04:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/nleps-deflated-residual-mutation-rotation.md (new — firm L1>L0 theme chapter; the deflated-residual mutation rotation: how firm L1 `nleps_deflated_residual` lowers into the `compute_residual` lambda `palace/linalg/nleps.cpp:547-577`; three sub-patterns A Mult+AddMult→single-pencil-apply collapse / B `MatVecMult ∘ fullPivLu().solve` deflation back-projection / C extended-space two-component norm + fused-`linalg::Dot` coordinate residual; written VERBATIM with nested ` ```text ` fences — fence parity balanced 8/8 = 16 fence lines, even; this report did NOT have the cycle-019 fence-truncation defect, unlike report #4 which the repairer converted to 4-space-indented blocks)
- book/src/L1-L0/index.md (edit — dep-map firm `nleps-deflated-residual-mutation-rotation` row appended after the `dot-mutation-rotation` row / before the `assemble-diagonal-mutation-rotation` row)
- book/src/SUMMARY.md (edit — `[nleps-deflated-residual-mutation-rotation](./L1-L0/nleps-deflated-residual-mutation-rotation.md)` inserted under the `# L1 > L0 — Lowering` Part between `dot-mutation-rotation` and `nrm2-mutation-rotation`)
- scaffolding/open-questions.md (append — 2 OQ sections)

Gate hits:
- (none non-zero) — no retroactive-budget hit (new firm theme creation, not a retroactive-evidence revision); no concept_writes-on-existing-slug (the target .md did not exist — clean `new:` create); no forward-edge-without-surface (L0 source `nleps.cpp:547-577` + the firm L1 `nleps_deflated_residual.md` anchor both exist on disk); no edge-label/prose mismatch (edge L1>L0, prose narrates forward L1→L0; critic passed edge-label-fidelity); no H1-page-heading reuse (H1 = `# nleps-deflated-residual-mutation-rotation`, the slug); no append-on-missing-slug (both `edit:` targets exist, anchors matched verbatim on-disk AFTER report #4's landings); no variant-axis-missing (§Applicability conditions enumerates k-cardinality / complex-only element-type / with-C-without-C damping / single-rank axes; critic passed variant-axis-coverage); no index-placeholder displacement (index.md has no `(empty — Phase B skeleton.)` placeholder); no implied-component stub created (the two plain-text leaf references are forward-references to not-yet-existing L1>L0 *themes* — `apply_nonlinear_pencil`/`lu_solve` lowering themes — NOT implied-component operator slugs; the operators themselves exist as firm L1 entries with live links, so plain-text-defer is the correct handling, not stub creation); no SUMMARY auto-fix needed (report proposed the SUMMARY edit explicitly, applied verbatim); bookkeeping complete (report proposed BOTH the index.md dep-map row AND the SUMMARY entry).

Count delta:
- L1>L0 firm themes: +1 (`nleps-deflated-residual-mutation-rotation` lands firm). On-disk `book/src/L1-L0/index.md` Theme-list table now carries the new firm row between `dot-mutation-rotation` (firm) and `assemble-diagonal-mutation-rotation` (firm). The L1>L0 Part has no headline firm-count integer to bump (status-per-row table, not an aggregate count); finalize need only confirm the table row + SUMMARY entry render. This is the 2nd firm L1>L0 theme landed this cycle (report #4 = `lu-solve-mutation-rotation`).

Open questions promoted:
- nleps-deflated-residual-mutation-rotation-l1-l0-landed-firm-cycle-023
- nleps-deflated-residual-l1-l0-interior-leaf-themes-still-forward-referenced

Build-relevant: yes

Notes:
- APPLIED THE REPAIRED CYCLE.md (META overall_status: ready). The critic's sole flagged finding was a cross-reference-integrity WARNING (not fail): four dead `../../../book/src/...` links in the report-scaffolding `## Speculative operators proposed` section (CYCLE.md :410-413) — these are OUTSIDE the publishable `new:` fence (never built into the artifact) and the same target slugs are linked correctly inside the fence; the repairer corrected the depth `../../../` → `../../` pre-integration. The mdBook build was never affected. The `new:` block itself is clean (the critic explicitly distinguished this from the cycle-019 fence-truncation signature: the firm apparatus — Status, L1/L0 forms, all three Sub-patterns A/B/C, citations — is fully ENCLOSED inside the `new:` fence with 8 balanced nested ` ```text ` pairs). I wrote the chapter VERBATIM with the nested fences intact (NOT converted to 4-space indentation, unlike report #4) — confirmed 16 fence lines on disk (even parity).
- VERIFICATION: all 8 chapter-body relative live-links resolve on disk — `../L1/nleps_deflated_residual.md`, `../L1/lu_solve.md`, `../L2/linear_combination.md`, `../L2-L1/linear-combination-fold-specialization.md`, `../L1/nrm2.md`, `./dot-mutation-rotation.md`, `../L1/apply_nonlinear_pencil.md`, `../L1/dot.md`. The two interior-leaf references that are PLAIN-TEXT (not live links) — the `apply_nonlinear_pencil` and `lu_solve` *L1>L0 lowering themes* (distinct from the operator entries, which ARE live-linked) — are correct plain-text forward-references per the rough-in-forward-reference convention (those *theme* files don't all exist yet).
- SHARED-FILE COORDINATION: re-read `book/src/L1-L0/index.md` and `book/src/SUMMARY.md` from disk FIRST and confirmed report #4's (`lu-solve-mutation-rotation`) landings present before editing — index.md `lu-solve-mutation-rotation` firm row (between `assemble-diagonal-mutation-rotation` and `minres-iteration`, on-disk line 31) and SUMMARY `[lu-solve-mutation-rotation]` (on-disk line 98, under the L1>L0 Part). My index anchor (`dot-mutation-rotation` row, on-disk line 29) and SUMMARY anchor (`dot-mutation-rotation` line 93 → `nrm2-mutation-rotation` line 94) were UPSTREAM of report #4's insert points and matched verbatim — no reconciliation needed (my new row/entry sits earlier in both files than report #4's, distinct positions). The remaining cycle-023 report (#6 = lowering-verifier-orthogonalize-composition-audit) is expected to be audit-only / no-mutation; if it DOES touch SUMMARY/L1-L0/index.md it should re-read disk to see this firm row + SUMMARY entry plus report #4's.
- NLEPS-COHORT PROGRESS for finalize/meta-phase: this firm L1>L0 theme discharges the `nleps_deflated_residual` half (cited `:698`) of the cycle-022 `nleps-deflation-lowering-chain-substantially-anchored-post-cycle-022` OQ. Combined with report #4 (`lu_solve` L1>L0 half, `:656`) landing firm THIS cycle, the NLEPS L1>L0 lowering cohort's remaining open item is the `nleps_deflated_solve` L1>L0 lowering theme (still a plain-text forward-reference — captured in report #1's landing-record OQ `nleps-deflated-solve-l1-l0-lowering-theme`) and the genuinely-un-themed `apply_nonlinear_pencil` L1>L0 leaf.
- The report's OQ #2 (reverse-direction L0→L1 lifting note) was NOT promoted as a standalone OQ — it is explicitly marked "working-note only, NOT in the theme body" per the CLAUDE.md high→low layer-definition discipline (the critic confirmed it is correctly OUTSIDE the chapter body). The report's OQ #3 (Sub-pattern A bit-non-determinism) and OQ #4 (no over-unification with L2 `deflate`) are already-recorded informational notes (the bit-difference is the recorded non-law at `nleps_deflated_residual.md:85`; the over-unification guard is carried in the operator entry per the cycle-021 guard) — folded into the landing-record OQ framing rather than promoted as standalone questions (same handling precedent as report #4's OQ #4).
- deferred integrated_at to finalize per role-spec (did NOT touch the consumed report's frontmatter).

---

## 2026-05-29T092943Z-lowering-verifier-orthogonalize-composition-audit
applied_at: 2026-05-29T12:26:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2-L1/orthogonalize-composition-lowering.md (edit — appended the `verified_against:` yaml block at end-of-file; 17 citations: orthog.hpp ×5 [:18-23, :29-36, :41-53, :57-74, :75-88], iterative.cpp+romoperator.cpp dispatch/consumers ×6 [:308-325, romoperator :51-66, :631-646, iterative :630-632, :809-811, romoperator :224-226], test-orthog.cpp ×4 [:99-120, :123-160, :276, :333], cross-theme delegation anchors ×3 [dot-mutation-rotation §Sub-pattern D :146-187, orthogonalize-mutation-rotation, L2/orthogonalize.md :166-220]; the theme STAYS `firm` — confirming audit, no `## Status` flip)
- scaffolding/open-questions.md (append — 3 OQ sections)

Gate hits:
- (none non-zero) — retroactive-budget per-slice = 1 (this is the ONLY retroactive-evidence revision this cycle; the other 5 reports are new-firm-theme/operator creations + a stub, not retroactive revisions — so global retroactive count = 1, well under the per-slice ≥3 / global ≥4 block thresholds; no block); no concept_writes-on-existing-slug (yaml-block append, not a concept_write); no forward-edge-without-surface (append-only evidence, no new edges; both L0 source surface + the firm L2/L1 anchors exist); no edge-label/prose mismatch (critic passed edge-label-fidelity); no H1-page-heading reuse (no new H1); no append-on-missing-slug (the target theme file exists on disk; anchor matched verbatim); no variant-axis-missing (critic passed variant-axis-coverage — 3 GS variants + 2 hook positions all in the verified block); no index-placeholder displacement; no implied-component stub created (the carry-forward is a citation-fix to a different EXISTING file, not an implied component); no SUMMARY auto-fix needed (no new chapter — the theme is already wired into SUMMARY.md:54, confirmed by critic); bookkeeping complete-by-no-op (firm-already theme, no count change, no dep-map/SUMMARY edit warranted).

Count delta:
- NONE — confirming `verified_against:` evidence backfill to an already-firm L2>L1 theme. The theme's `## Status` was firm before (cycle-022) and stays firm. No L1/L2/L1-L0 firm-count headline or dep-map row changes. (No append on SUMMARY.md / any index.md this report — distinct from reports #1-#5.)

Open questions promoted:
- orthogonalize-composition-lowering-audited-fully-supported-firm-stays-cycle-023
- dot-mutation-rotation-subpattern-d-stale-orthog-hpp-34-anchor-should-be-35
- orthogonalize-audit-dispatch-scope-named-nonexistent-orthog-cpp

Build-relevant: yes

Notes:
- APPLIED THE REPAIRED CYCLE.md (META overall_status: ready, all-8 critic checks pass). This was a confirming `lowering-verifier` audit — verdict fully-supported, theme stays `firm`, single artifact mutation = the append-only `verified_against:` yaml block at end-of-file. Verified on disk FIRST that the theme has NO pre-existing `verified_against:` yaml KEY (the prose `## Verified-against` markdown section at the theme's lines 291-357 is a distinct markdown heading, NOT a yaml block) — so the append is genuinely additive, no key conflict. The yaml block is fenced ` ```yaml … ``` ` and placed after the file's final "No dedicated L1↔L2 equivalence test" caveat (was the last content line).
- CARRY-FORWARD FOR FINALIZE/META-PHASE (NOT applied this report — out of this audit's edit scope): confirmed stale `palace/linalg/orthog.hpp:34` anchor for `return LocalDot(x, y);` in the cross-referenced delegation target `book/src/L1-L0/dot-mutation-rotation.md` §Sub-pattern D at lines 160 and 183 — should be `:35` (line 34 is the brace `{`; codemap + citecheck `[DRIFT → :35]`). The audited theme correctly uses `:35`. Routed as OQ `dot-mutation-rotation-subpattern-d-stale-orthog-hpp-34-anchor-should-be-35` for a future lifter/lowering-verifier pass owning `dot-mutation-rotation` (one-token fix at :160 + :183). I did NOT edit `dot-mutation-rotation.md` (out of this report's proposed-changes scope; not a defect of the audited theme).
- DISCHARGED OQs noted (left UNEDITED per role-spec — meta-phase owns ledger migration to the Closed index): the audit confirms the theme discharges `orthogonalize-composition-lowering-l2-l1-theme` (cycle-019 carry-forward, was blocked on the L2 anchor — now firm) and `orthogonalize-mutation-rotation-l1-l0-theme-should-cite-dot-subpattern-d` on the L2>L1 side. Both confirmed accurate against the cited evidence; meta-phase can migrate them with the answer-link.
- SHARED-FILE COORDINATION: this report touched book/src/L2-L1/orthogonalize-composition-lowering.md — a file NOT touched by any prior cycle-023 report (reports #1/#2 = L1/index.md; #3 = L2/index.md + L2/L3 eigsolve; #4/#5 = L1-L0/index.md + L1-L0 themes; SUMMARY.md touched by #1/#3/#4/#5 in distinct Parts). My edit is the FIRST and ONLY touch of this L2-L1 theme file this cycle; no shared-file reconciliation needed. I did NOT touch SUMMARY.md or any index.md (confirming audit needed no registration/count change).
- The report's OQ-area #3 (no dedicated L1↔L2 equivalence test) was NOT promoted as a standalone OQ — it is an inherited caveat the theme already records (its lines 398-405), explicitly NOT a status reduction, carried through from the sibling `linear-combination-fold-specialization`; folded into the landing-record OQ framing rather than re-filed. The report's OQ-area #4 (OQ discharges) is record-only confirmation, not a new question — captured in the landing-record OQ's meta-phase-action note.
- deferred integrated_at to finalize per role-spec (did NOT touch the consumed report's frontmatter).

---
