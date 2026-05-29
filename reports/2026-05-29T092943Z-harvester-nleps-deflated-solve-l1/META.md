---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T10:42:00Z
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
repaired_at: 2026-05-29T11:05:00Z
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

# META: verification of "Formalize nleps_deflated_solve at L1"

## Critique

### Checks run

**citation-validity — pass.** Ran `tools/citecheck/citecheck.py --scan` over the whole CYCLE.md: **39 citations, 0 failing, all in-bounds** (nleps.cpp has 952 lines; all artifact-file ranges in-bounds). I then re-verified every load-bearing pinpoint anchor line-exact via codemap `read_range` on `palace/linalg/nleps.cpp`: `:514` `opInv->Mult(b1, x1)` ✓; `:515-518` `if (k == 0) { return; }` ✓; `:522` `x2(j) = b2(j) - linalg::Dot(GetComm(), x1, X[j])` ✓ (the producer's `:521→:522` drift correction is **confirmed correct** — :521 is the loop's opening brace, :522 is the statement); `:529` `SS(i, j) = linalg::Dot(GetComm(), X[i], X[j])` ✓; `:532` `S = eig_opInv * Identity(k,k) - H` ✓; `:533` `SS = -S.fullPivLu().solve(SS)` ✓; `:534` `x2 = SS.fullPivLu().solve(x2)` ✓; `:535` `MatVecMult(X, S.fullPivLu().solve(x2))` ✓; `:536` `linalg::AXPY(-1.0, XSx2, x1)` ✓. Call sites `:542`/`:682`/`:735` (`deflated_solve(...)`) and SetRelTol `:541`/`:681` all exact. Secondary anchors verified: `:329-347` MatVecMult def + `:334` `k = X.size()`; `:397` `H`; `:401` `X`; `:474` `eig_opInv = eig` (lagged); `:495-502` operator setup (`SetAbsTol(1.0e-12)` at :502); `:606-619` basis growth (normalize :610-611, `X[k]=v` :615, `k++` :619 — confirms NO inter-column orthogonalization); `:354-362` literature (Jarlebring–Koskela–Mele 2018, Effenberger 2013, SLEPc-NEP minimality-1). Artifact citations verified on-line: `dot.md:43` (arg-1-conjugated convention), `lu_solve.md:11` (cites :533-535) + `:58-59` (multi-RHS law 4 / nested-solve law 5), `L2/index.md:42,:59-60` (deflate/gram rows), `nleps_deflated_residual.md:86,:109,:117`. Every claim carries a pointer; every pointer resolves in-range.

**surface-or-evidence — pass.** This is a NEW firm L1 operator entry (a `new:` file), not a refinement of an existing operator/theme, so the refinement-shape gate is satisfied by construction: the report proposes surface (the full `book/src/L1/nleps_deflated_solve.md` chapter) backed by exhaustive positive source citation. The one *refinement-adjacent* assertion — the deflate-promotion verdict — is correctly framed as retroactive-evidence assessment ("confirms, does not change, the cycle-022 verdict") and is explicitly NOT a surface change to the `deflate` entry (the report states "I did NOT touch the `deflate` entry — out of scope"). No bare rotation_claim against existing surface.

**rotation-quality — pass.** The L1 form is strictly more compact/abstract than L0: state-hiding (no `x1`/`x2` destination buffers, no per-use `SetRelTol`, no `eig_opInv` lag in the signature) and substitution of opaque named constituents (`ksp_solve`, `lu_solve`×3, `dot`-folds, `linear_combination`, `axpy`) for the literal `opInv->Mult`/`fullPivLu().solve`/`linalg::Dot`/`MatVecMult`/`linalg::AXPY` C++. This is a genuine mutation rotation (L1's defining rotation), not a renaming or 1:1 mapping — the in-place destination-buffer mutation collapses to a pure `{x1, x2}` return. The apply/inverse duality with `nleps_deflated_residual` is correctly framed: the residual *applies* the extended operator (couples through `(λI−H)⁻¹`), the solve *inverts* it (couples through the Schur complement `SS = −S⁻¹XᴴX`); law 5 records this as a **structural relationship, not a literal `solve ∘ residual = id` identity**, with the appropriate caveat that the residual uses `T(λ)` while the solve uses the lagged `T(σ)` and the big-space block is tolerance-bounded. This restraint is correct — asserting a tight inverse identity would be wrong given the lag + iterative-tolerance.

**variant-axis-coverage — pass.** Three variant axes covered: deflation-present (`k=0` | `k>0`, the `if (k==0)` guard, parameterized-not-family); purpose (projection-direction `w0` vs Newton-step `du`, scoped out as L1>L0 tolerance concern); inner-solver method (CG/GMRES/FGMRES, absorbed into the opaque `K` per ksp_solve precedent). Two axes explicitly collapsed-with-rationale: inexact-Newton tolerance + `eig_opInv` lag (L1>L0), and the `Mult`/`AddMult`/`MatVecMult`/`AXPY` L0 build-forms. The over-unification axis (vs L2 `deflate`) is handled as a dedicated guard. No hidden branches: I read the whole lambda (`:504-537`) and the three call-site contexts; every branch is the single `k==0` early-return, which is covered.

**cross-reference-integrity — pass (build-readiness guard PASSES).** All `[link]` targets exist on disk: `ksp_solve.md`, `lu_solve.md`, `dot.md`, `axpy.md`, `nleps_deflated_residual.md`, `eigsolve.md` (L1); `linear_combination.md`, `gram.md` (L2); `eigensolver-wrapper.md` (L0). **Firm-body-inside-fence guard:** fence-enumeration (`grep -n '```'`) gives 22 fences (even parity). The `new:book/src/L1/nleps_deflated_solve.md` block opens at line 25 and closes at line 211; it contains 4 balanced nested ` ```text ` pairs (36/42, 48/68, 87/91, 95/104) — 10 fences inside the block, balanced. The **full firm apparatus sits INSIDE the fence**: `## Signature` (46), `## Semantics` (83), `## Algebraic laws` (120), `## Dependencies` (141), `## Variant axes` (151), `## Status` (164), `## L1 vs L0 distinction` (172), `## Evidence` (177) — all between 25 and 211. The report's OWN top-level sections (`## Operator content` 244, `## Supporting evidence` 256, `## Open questions / caveats` 264) are correctly OUTSIDE the fence (after 211). This is the inverse of the cycle-019 fence-truncation defect — `## Status` is enclosed, not authored as a report top-level section. The four `edit:book/src/L1/index.md` blocks and two `edit:book/src/SUMMARY.md` blocks are balanced pairs. Edit anchors verified exact: "Firm (16)" headline at index.md:29 (matches old_string verbatim), lu_solve firm-bullet at :46, lu_solve dep-map row at :83, SUMMARY lu_solve line at :75 (matches).

**edge-label-fidelity — pass (not applicable to L_n operator entry).** This is an L1 operator entry, not a lowering theme; it carries no `L_{n+1}→L_n` edge label. The closest analog — the apply/inverse duality framing with `nleps_deflated_residual` — is same-layer (both L1) and the prose discusses exactly that L1↔L1 relationship. The forward-reference to a future `nleps-deflated-solve-mutation-rotation` L1>L0 theme is correctly scoped to the abstractor and left as plain-text (no live link to a missing file).

**plan-kind-consistency — pass.** Declared kind is firm L1 operator; content shape matches. Every constituent is read from a positive source site (not constructed from negative anchors), every law is a syntactic identity (k=0 reduction is the `if` branch; linearity laws are fixed-`(λ,K,P)` compositions of firm linear maps; the duality is the structural sibling relationship), and the one non-syntactic statement (law 3's tolerance-bounded inversion) is recorded as a non-law rather than asserted as a tight identity. No rough-in placeholders, no constructive sub-part, so no `partly-constructive` caveat is warranted — the `firm` classification is sound under the firm-on-positive-structure escape (the `apply_nonlinear_pencil` / `nleps_deflated_residual` precedent, correctly cited). The no-dedicated-test caveat is correctly carried as inherited-and-non-gating, matching the sibling precedent at `nleps_deflated_residual.md:117`.

**skill-uptake-survey — warning (non-blocking, telemetry only).** The report's §"Supporting evidence" states all citations were machine-verified with `tools/citecheck/citecheck.py` (25 ranges; 14 pinpoint anchors) — good tool uptake. However, several skills whose shape directly matches this report's work are not referenced by name: `verify-citation-range` (the citation-anchor verification this report performs heavily), `classify-variant-axis` (the report does a substantive variant-axis enumeration + collapse-rationale), and the `proposed-changes-fence-encloses-full-body-guard` skill (the firm-body-inside-fence concern the report navigates correctly). This is a pure presence-check surfacing telemetry — the *work* was done correctly; only the skill-invocation breadcrumbs are thin. Not blocking.

### Issues found

No blocking issues. The report is well-anchored, the firm classification is sound, the build-readiness guard passes cleanly, and the load-bearing deflate-promotion finding is independently confirmed (see below). The items below are minor / informational.

1. **KEY FINDING independently verified — deflate-promotion verdict is CORRECT (informational, strengthens the report).** I read `palace/linalg/nleps.cpp:514-536` directly via codemap. The Gram `XᴴX` is built positively at the double-loop `:524-531` (statement `:529`), then at `:533` is overwritten via `SS = -S.fullPivLu().solve(SS)` = `−S⁻¹·(XᴴX)`. The **only** `.solve()` invocations are `S.fullPivLu().solve(...)` (S⁻¹, lines :533 and :535) and `SS.fullPivLu().solve(x2)` (SS⁻¹, line :534). **There is no bare `(XᴴX)⁻¹` solve** — the Gram is never the operator-being-inverted, only the operand pre-multiplied by `−S⁻¹`. The report's verdict ("`deflate` stays `partly-constructive`; this lambda supplies only the Schur-form, not the bare-Galerkin source site") is therefore **correct**. It is also consistent with the existing `L2/index.md:42,:60` framing, which already records the Schur-form pipeline as firm-on-this-site and gates the bare-Galerkin-core promotion on "a positive Palace Galerkin-deflation source site" — which this lambda does not provide. No change to deflate is warranted; the report correctly does not enact one.

2. **Two of the four `index.md` insertions are described as prose instructions rather than anchored `edit:` old→new pairs (minor structural note for the integrator).** CYCLE.md lines 221-233: the firm-list-bullet insertion ("Add this firm-list bullet immediately after the `lu_solve` bullet ... index line 46") and the dep-map-row insertion ("Add this dep-map table row ... index line 83") are framed as single-block `edit:` snippets with surrounding prose telling the integrator WHERE to insert, rather than as literal old_string→new_string replacement pairs. The two *literal* `edit:` pairs that ARE fully anchored (the "Firm (16)→(17)" headline at :29 and the SUMMARY.md line at :75) verified exact. The insertion anchors (:46, :83) are verified correct in the live file. This is well within normal integrator-handled insert-after-anchor practice (the `summary-md-surgical-insert` pattern), not a defect — flagged only so the integrator parses the two insert-after instructions correctly rather than expecting old→new pairs.

3. **Section-order nit inside the new: chapter (informational).** The chapter places `## Dependencies` (141) and `## Variant axes` (151) before `## Status` (164), with `## Evidence` (177) last. This matches the `nleps_deflated_residual` sibling layout and is internally coherent; the firm apparatus (Signature/Status/Algebraic-laws/Evidence) is all present and all inside the fence. No action needed — noted only for completeness of the build-readiness scan.

4. **skill-invocation breadcrumbs thin (see skill-uptake-survey).** Non-blocking; the underlying work (citation verification, variant-axis classification, fence-guard navigation) was performed correctly.

## Repair

### Fixes attempted

The critic returned 7 `pass` + 1 `warning` (skill-uptake-survey, telemetry-only). The firm judgment is sound and the load-bearing deflate-promotion finding (deflate stays `partly-constructive` — the Gram `XᴴX` is built positively at `:529` but only ever solved Schur-wrapped as `SS = −S⁻¹(XᴴX)` at `:533`; no bare `(XᴴX)⁻¹` solve exists) was independently re-verified by the critic against `palace/linalg/nleps.cpp:514-536`. The four informational items are addressed below; only finding 2 warranted a (mechanical, in-scope) edit.

- **Finding (issues §1) — KEY FINDING independently verified; deflate-promotion verdict CORRECT.**
  - **Decision**: not-needed (record-only).
  - **Rationale**: The critic confirmed the report's verdict against source, not a finding against the report — it strengthens the report. No edit; the report already correctly does NOT touch the `deflate` entry (out of scope per the report's own §"Deflate-promotion assessment"). Maps to no checklist defect.

- **Finding (issues §2) — two of the four `index.md` insertions framed as prose-instructions rather than anchored old→new pairs.**
  - **Decision**: repaired.
  - **Action**: `reports/2026-05-29T092943Z-harvester-nleps-deflated-solve-l1/CYCLE.md` §"Proposed changes". Converted the two insert-after-prose snippets into explicit anchored `edit:book/src/L1/index.md` old→new replacement pairs, matching the two already-anchored pairs (the `Firm (16)→(17)` headline and the SUMMARY.md line):
    - **Firm-list bullet** — anchored on the `lu_solve` bullet's unique trailing fragment (`…ROM's QR-for-stability over rejected LDLT, …, not a transparent trick.`) + the following blank line + the `**Rough-in (test-coverage-bounded)**` header; the new `nleps_deflated_solve` bullet is inserted on its own line between the `lu_solve` bullet and the blank line. (The `lu_solve` bullet is a single physical line in `book/src/L1/index.md:46`; the original "insert at index line 46" prose would have under-specified the literal anchor — the fragment-based old→new pair is now byte-exact.)
    - **Dep-map row** — anchored on the `lu_solve` dep-map row + the `lanczos_step` row that follows it; the new `nleps_deflated_solve` row is inserted between them.
    - All four `index.md` edit anchors verified unique in the live `book/src/L1/index.md` (each `grep -c` returns 1). Fence parity of CYCLE.md preserved (26 fence lines, even). **Note for the integrator**: the Firm-count `(16)→(17)` is correct as authored, but the count will be reconciled by the integrator against same-cycle landings if any other report also lands a firm L1 operator this cycle (the headline edit is a single-token replacement the finalizer can adjust).
  - **Authority**: in-scope — this is the H1→H2-style mechanical normalization / append-by-anchor class (prose-instruction → byte-exact anchored edit). No substantive content authored; the inserted bullet/row text is the report's own, lifted verbatim into a literal old→new pair.

- **Finding (issues §3) — section-order nit inside the new: chapter (Dependencies/Variant-axes before Status; Evidence last).**
  - **Decision**: not-needed (record-only).
  - **Rationale**: The order matches the `nleps_deflated_residual` sibling layout, is internally coherent, and the full firm apparatus (Signature / Semantics / Algebraic-laws / Status / Evidence) is present and entirely inside the `new:` fence. The critic explicitly says "no action needed." Re-ordering would be a stylistic content decision, not a mechanical fix.

- **Finding (issues §4 / skill-uptake-survey warning) — skill-invocation breadcrumbs thin.**
  - **Decision**: not-needed (record-only).
  - **Rationale**: Pure telemetry; the underlying work (citation verification via `tools/citecheck/citecheck.py`, variant-axis classification, fence-guard navigation) was performed correctly. The skill `checks:` value stays `warning` (repairer does not override critic checks). Recorded for the meta-phase skill-uptake survey window; not a content or build defect.

### Unrepairable findings

None. No finding required substantive authoring, contradicted existing artifact content, or exceeded repair authority.

## Suggested resolution

`ready`. Notes for the integrator:

- The proposed-changes block now contains four byte-exact anchored `edit:book/src/L1/index.md` old→new pairs (Firm headline, firm-list bullet, dep-map row) plus the SUMMARY.md insertion — all four anchors verified unique in the live file at repair time. Apply as literal replacements; no insert-after-prose parsing needed.
- The `new:book/src/L1/nleps_deflated_solve.md` chapter is firm and self-contained; full apparatus enclosed inside the fence (the inverse of the cycle-019 fence-truncation defect — confirmed by the critic's fence-enumeration).
- **Firm-count reconcile**: the `Firm (16)→(17)` headline is correct as authored against the current `book/src/L1/index.md`. If another same-cycle report also lands a firm L1 operator, the finalizer should reconcile the headline count and the firm-bullet roster accordingly (this is the only same-cycle-coupled token in the proposed changes).
- The load-bearing deflate-promotion verdict (`deflate` stays `partly-constructive`) is confirmed and explicitly NOT enacted by this landing — the report correctly leaves the L2 `deflate` entry untouched. The future-search note (a bare `(XᴴX)⁻¹` Galerkin/oblique-deflation site outside `nleps.cpp`) is captured in the report's §"Open questions / caveats" for the OQ ledger / meta-phase, not an integrator action.
