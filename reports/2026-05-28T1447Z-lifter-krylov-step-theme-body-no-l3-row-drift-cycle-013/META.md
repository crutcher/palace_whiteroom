---
verifies: ./CYCLE.md
critiqued_at: 2026-05-28T1510Z
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
repaired_at: 2026-05-28T1525Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

# META: verification of "Re-anchor krylov-step-theme-body-no-l3-row-drift-cycle-013"

## Critique

### Checks run

**citation-validity — warning.** The report's two new-text blocks cite three classes of pointer: (1) the CLAUDE.md invariant **"Identity-lowerings still require both L levels"** — verified present in CLAUDE.md (2 occurrences); (2) the cross-references `L3/krylov-step.md` and `L3-L2/krylov-step-body-identity.md` — verified present on disk at the exact byte sizes the report claims (40486 and 26828); and (3) the carried-over slice citation `cg.md:341-362` and `arnoldi_step.md:178-213` (Re-anchor 1 `[new]` block, CYCLE.md:25). The `arnoldi_step.md:178-213` range is valid — that slice was reduced (cycle-010+ banner) but the cited range still contains the MGS-obstruction / body-identity content. The `cg.md:341-362` citation is **dangling/out-of-range**: `book/src/spec/slices/cg.md` is now a 165-line reduced stub ("Slice: cg (reduced)"), so lines 341-362 do not exist, and the verbatim "step body lifts as identity" quote the theme attributes to that range (theme:210) is no longer present in the file — it was lifted into the firm entry `book/src/L3-L2/krylov-step-body-identity.md` (per `cg.md:11`). The re-anchor carries this dangling citation forward verbatim rather than re-anchoring it to its now-firm home. Warning, not fail, because (i) the dangling citation is pre-existing theme-wide (also at theme lines 98, 109, 126, 200, 204, 210, 231, 233) and is outside the report's declared scope (which was the "no L3 row" phrasing only), and (ii) the report's own structural claims are all well-cited. See Issue 1.

**surface-or-evidence — pass.** This is a refinement-shaped proposal that modifies theme surface (two prose blocks in `krylov-step-typed-wrapper-dissolution.md`) and frames itself explicitly as re-anchoring stale vocabulary to firm-now-existing entries — not a pure rotation_claim. The change is surface-bearing and the discipline-notes section frames it as bringing meta-prose into consistency with the entry's own already-correct §Audit (line 218) and §Status (line 293). Allowed.

**rotation-quality — pass / not the proposal's shape.** This dispatch does not assert a new algebraic/structural rotation; it re-anchors meta-prose about an already-firm L4>L3 wrapper-dissolution rotation. The underlying rotation (typed-wrapper dissolution into value-threaded form) is unchanged and was firmed in prior cycles. No new rotation to assess; the existing rotation's compaction claim (L4 typed wrapper -> L3 positional value-threading; monad/records/readonly dissolve) is preserved verbatim.

**variant-axis-coverage — pass.** No variant axes are introduced or modified by this re-anchor. The theme's existing six-axis variant profile (theme:93) and the MGS/CGS/CGS2 orthog-variant obstruction (theme:99) are untouched. Not applicable to a vocabulary re-anchor.

**cross-reference-integrity — pass.** Verified directly against the artifact, per the dispatch's explicit ask: (a) the two `[old]` blocks match the on-disk theme at line 20 (Context §) and line 220 (OQ-disposition §) exactly, and each `[old]` anchor is a unique substring in the file (grep count = 1 each), so both proposed-changes blocks apply unambiguously; (b) a full scan of the theme for stale "no L3 row" residuals returns exactly three matches — lines 20, 218, 220 — confirming lines 20 and 220 are the surviving live-conclusion residuals and that line 218 (the §Audit prose) already carries the correct SUPERSEDED-cycle-010 framing with the `L3/krylov-step.md` cross-reference and the identity-lowerings invariant; (c) line 293 (§Status) is already correct and untouched; (d) the two new `[link]` targets `../L3/krylov-step.md` and `../L3-L2/krylov-step-body-identity.md` resolve from the theme's directory. One borderline residual noted below (Issue 2): line 218 still contains the phrase "The L4 entry lowers transitively to the L2 entry via this theme," a relic of the transitive-skip framing — but it is embedded inside the already-SUPERSEDED §Audit block and is immediately followed by the cycle-010 backfill note, so it is not a live contradiction; flagging it as a drive-by, not as a cross-reference break.

**edge-label-fidelity — pass.** The re-anchored text correctly states the lowering chain is **L4>L3>L2>L1 with no skipped rows** and assigns each hop its edge: this theme dissolves L4 -> L3 (`L3/krylov-step`), and the body's L3 -> L2 identity hop is completed by the separate theme `L3-L2/krylov-step-body-identity`. The edge the theme carries (L4>L3) is exactly the edge the re-anchored prose discusses; the L3>L2 hop is correctly attributed to the sister theme rather than claimed by this one. The cycle-009 "Identity-lowerings still require both L levels" invariant is cited as the basis for not collapsing the L3 row. No edge mislabeling.

**plan-kind-consistency — pass.** Declared as a `firm`-status theme re-anchor (status unchanged; theme remains `firm`), content shape matches: two surgical prose edits, no LHS/RHS change, no new claims, no rough-in placeholders introduced. The "structural rewrite only" framing in Discipline notes is consistent with the content.

**skill-uptake-survey — warning.** This dispatch re-asserts an inherited slice citation (`cg.md:341-362`) without a range re-verification, which is precisely the case the `verify-citation-range` skill's "Audit-report / inherited-citation sub-case" (extended cycle-012 meta-phase) was written to catch — an inherited citation carried verbatim from a prior cycle into a since-reduced slice. The report does not reference invocation of `verify-citation-range` on the carried-forward citation. Pure telemetry; non-blocking. Had the skill been run on the `cg.md` pointer, Issue 1 would have surfaced inside the dispatch.

### Issues found

**Issue 1 (citation-validity, medium) — `cg.md:341-362` is dangling; re-anchor carries it forward instead of re-pointing to the firm L3-L2 entry.** Location: CYCLE.md:25 (Re-anchor 1 `[new]` block), which re-asserts `(`cg.md:341-362`, `arnoldi_step.md:178-213`)`. `book/src/spec/slices/cg.md` is now a 165-line reduced stub; lines 341-362 do not exist, and the cycle-002 "step body lifts as identity" content the theme attributes to that range has been lifted into the firm `book/src/L3-L2/krylov-step-body-identity.md` (per `cg.md:11`). The faithful current pointer for the body-identity claim is the firm L3-L2 theme, not the reduced slice. The report had a natural opening to re-anchor this stale citation in the very same edit (exactly parallel to its "no L3 row" -> firm-L3-entry re-anchor) but did not. Note this is a **pre-existing theme-wide problem**: the same dangling `cg.md` ranges appear at theme lines 98, 109, 126, 200, 204, 210, 231, 233 (`cg.md:341-362` / `:351-362` / `:347-350` / `:341-349`), all into reduced material. Candidate repair: in the Re-anchor 1 `[new]` block (and optionally a broader sweep), re-anchor `cg.md:341-362` to `book/src/L3-L2/krylov-step-body-identity.md` (keeping `arnoldi_step.md:178-213`, which remains valid). The broader theme-wide sweep is arguably out of this report's scope and could be deferred to a dedicated citation-re-anchor dispatch; minimally the re-asserted pointer in the new text should be fixed so the report does not introduce/re-bless a dangling citation.

**Issue 2 (cross-reference-integrity, low / drive-by) — residual "lowers transitively to the L2 entry" phrasing at theme:218.** Location: `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:218` (inside §Audit, the prose the report classifies as already-correct). The sentence "The L4 entry lowers transitively to the L2 entry via this theme (L4>L3 wrapper dissolution) plus a one-line L3>L2 theme..." retains the transitive-skip framing that the re-anchor is otherwise eliminating. It is not a live contradiction — it sits inside the SUPERSEDED block and is immediately followed by the "Cycle-010 backfill" note affirming the firm L3 row — so the report's claim that line 218 "already carries the correct framing" is defensible. Flagging only because, if a repairer is sharpening for full internal consistency, this clause reads as a transitive-lowering relic that could be brought into line with the "no skipped rows" vocabulary the re-anchor establishes. Optional; not required for correctness.

**Issue 3 (citation-validity / OQ-disposition, low / drive-by) — re-anchored OQ may already be closed.** Location: CYCLE.md:32 (Re-anchor 2 `[new]`) and theme:220. The re-anchored text proposes closing OQ `krylov-step-l3-identity-in-form-audit` as confirmed-with-refinement; the open-questions ledger (`scaffolding/open-questions.md:1134-1139`) shows this slug already has `answered_in: reports/2026-05-27T081913Z-abstractor-...` (cycle-006). The re-anchor preserves the OQ-disposition prose (correctly — it is firming the "no L3 row needed" tail of it), so this is not a defect introduced by the report, but the integrator should be aware the OQ is already answered and the disposition prose is historical, not a fresh closure action. No edit required.

### Notes for downstream

- All three dispatch-asked verifications confirmed: (a) lines 20 and 220 are the only stale "no L3 row" live-conclusion residuals; lines 218 and 293 are already correct and were correctly left untouched; (b) the re-anchored text correctly states the L4>L3>L2>L1 no-skipped-rows chain and cites the cycle-009 identity-lowerings invariant (CLAUDE.md, verified present); (c) both `[old]`->`[new]` blocks have unique anchors and apply unambiguously.
- The one substantive finding (Issue 1) is the carried-forward dangling `cg.md` citation — a real citation-validity gap, but pre-existing and at the edge of this report's narrow scope.

## Repair

### Fixes attempted

- **Finding (Issue 1, citation-validity, medium)**: Re-anchor 1 `[new]` block (CYCLE.md:25) re-asserts a dangling `cg.md:341-362` pointer. `book/src/spec/slices/cg.md` is now a 165-line reduced stub (verified: `wc -l` = 165; head shows "# Slice: cg (reduced)"), so lines 341-362 no longer exist; the body-identity content originally at that range was lifted into the firm `book/src/L3-L2/krylov-step-body-identity.md`.
  - **Decision**: repaired.
  - **Action**: Edited the Re-anchor 1 `[new]` block in CYCLE.md (the new text the integrator will apply to `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` line 20). Replaced the bare dangling pointer `(`cg.md:341-362`, `arnoldi_step.md:178-213`)` with a reference to the firm theme `[`L3-L2/krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md)`, noting the `cg.md:341-362` slice evidence has been lifted into that firm entry per the cycle-009 corpus reduction and that `arnoldi_step.md:178-213` remains the valid live anchor (kept verbatim — the critic confirmed it is in-range). Verified the firm entry carries the lifted content: `L3-L2/krylov-step-body-identity.md:125` reproduces the verbatim "The L2→L3 rotation on the step body is therefore the **identity in form**..." quote and attributes it to the now-reduced `cg.md:341-362`.
  - **Rationale (scope)**: only the one re-asserted pointer in *this report's* new text was re-anchored. The critic's pre-existing theme-wide dangling-`cg.md` instances (theme lines 98, 109, 126, 200, 204, 210, 231, 233) are NOT in this report's proposed-changes (which touch only theme lines 20 and 220) and are deferred — see Drive-by observations / OQ below. Repairing them would expand the report's scope beyond its declared mandate.

- **Finding (skill-uptake-survey, warning)**: dispatch re-asserted the inherited `cg.md:341-362` citation without running `verify-citation-range`'s "Audit-report / inherited-citation sub-case".
  - **Decision**: not-needed (telemetry-only check; the underlying defect it points at is Issue 1, which is now repaired). The repair itself is the `verify-citation-range` outcome applied post-hoc; no further edit required.

### Unrepairable findings

None. The two findings the critic flagged as warnings both resolve to Issue 1's dangling citation, which was mechanically re-anchorable (the faithful home — the firm L3-L2 entry — already exists and carries the lifted content).

### Drive-by observations / deferred to OQ

- **Issue 2 (cross-reference-integrity, low)** — residual "lowers transitively to the L2 entry" relic at `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:218`. OUT of this report's edit window: the report's proposed-changes touch only theme lines 20 and 220; line 218 lives in the §Audit block the report explicitly leaves untouched. Not repairable in-place via this report's CYCLE.md. Deferred to OQ / a future dedicated citation-and-vocabulary cleanup dispatch on this theme.
- **Pre-existing theme-wide dangling `cg.md` citations** (theme lines 98, 109, 126, 200, 204, 210, 231, 233) — same class as Issue 1 but outside this report's proposed-changes. Deferred to a dedicated citation-re-anchor dispatch that sweeps the whole theme and re-points each `cg.md:341-362` / `:351-362` / `:347-350` / `:341-349` range to `L3-L2/krylov-step-body-identity.md` (the firm home for the lifted body-identity material). Candidate OQ for the integrator to file.
- **Issue 3 (OQ already closed)** — the re-anchored OQ `krylov-step-l3-identity-in-form-audit` already shows `answered_in` (cycle-006) in `scaffolding/open-questions.md:1134-1139`. The Re-anchor 2 disposition prose is firming a historical "no L3 row needed" tail, not enacting a fresh closure. Integrator OQ-promotion handling should treat this as already-answered (no double-close); no CYCLE.md edit required.

## Suggested resolution

`ready`. The one substantive finding (Issue 1's dangling `cg.md:341-362` pointer in the report's new text) is repaired by re-anchoring to the firm `L3-L2/krylov-step-body-identity.md` entry, verified to carry the lifted content. The report no longer re-blesses a dangling citation. Notes for the integrator: (1) treat OQ `krylov-step-l3-identity-in-form-audit` as already-answered (cycle-006) — do not double-close (Issue 3); (2) consider filing an OQ for a dedicated theme-wide `cg.md` citation-re-anchor sweep covering the pre-existing dangling pointers at theme lines 98/109/126/200/204/210/218/231/233 plus the Issue-2 "transitive" relic at line 218.
