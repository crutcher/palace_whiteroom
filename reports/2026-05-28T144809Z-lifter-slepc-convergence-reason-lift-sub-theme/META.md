---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T150500Z
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
repaired_at: 2026-05-28T151500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of slepc-convergence-reason-lift-sub-theme (eigsolve-convergence-reason-mapping)

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing source claim was re-verified against the Palace tree via `palace-codemap`. All positive citations are exact and in-range: `EPSGetConverged` at `slepc.cpp:695` (the `Solve()` body; a second hit at line 276 is a different method, correctly not cited), `EPSConvergedReasonView` at 699, `return (int)num_conv` at 708; `PEPGetConverged` at 1178, `PEPConvergedReasonView` at 1182, `return (int)num_conv` at 1191; `NEPGetConverged` at 1525, `NEPConvergedReasonView` at 1529. The NEP path correctly carries no plain `return (int)num_conv` citation (its body does `const int nev = (int)num_conv;` then a sort — the report hedges with "and the NEP analogue", which is accurate). The L1 anchor `EigStatus = Converged | PartialConverged | MaxIterReached | LinearSolveFailed` is verbatim at `book/src/L1/eigsolve.md:51` (within §Signature, line 21), and the §Signature callout the report leans on (line 54) does explicitly forward the SLEPc `EPS_DIVERGED_BREAKDOWN` / `EPS_DIVERGED_SYMMETRY_LOST` family — so the reconstruction is consistent with the established L1 narrative. **The negative anchor — the partly-constructive status's load-bearing claim — is fully confirmed:** `search_text EPS_DIVERGED` → 0 hits; `EPS_CONVERGED` → 0 hits; `ConvergedReason` → exactly the three print-only `*ConvergedReasonView` sites (699/1182/1529); `GetConvergedReason` → 0 hits (no variable-binding accessor anywhere). The report's "zero references" claim and its three-print-site enumeration are exact. The only soft spot (already self-flagged, OQ #1) is that the SLEPc enumerator *names* (`EPS_DIVERGED_BREAKDOWN`, `NEP_DIVERGED_LINEAR_SOLVE`, etc.) are documented-not-source-anchored — they come from SLEPc headers, not Palace — which is correct per CLAUDE.md "Many symbols resolve into upstream libraries" and is honestly surfaced rather than asserted as Palace-cited.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (it refines the status-derivation of an existing firm theme) but it is framed as retroactive/forward-looking evidence elaboration of a forward-pointer the parent explicitly left open (parent line 301). It modifies surface (a new sibling chapter + one parent cross-ref edit) AND it is grounded in the whole-tree negative anchor as its evidence. It is not a pure rotation_claim with no surface — it discharges a named promise and lands a concrete mapping table. The partly-constructive framing (negative anchors as evidence FOR a faithful reconstruction, explicitly NOT a positive claim) is exactly the cycle-012 idiom.

**rotation-quality — pass (not the primary shape).** This is a lifter status-derivation refinement, not an assertion of a new algebraic/reduction rotation; it introduces no new LHS/RHS vocabulary and no L1 operator (correctly declared "Speculative L1 operators: None"). To the extent it carries a lowering shape, the L1 `EigStatus` discrimination (sum-typed, abstract) is strictly more compact than the L0 print-only reason-view + count-return — state hiding of the SLEPc reason enum into a four-way status. No renaming-only / 1:1 concern.

**variant-axis-coverage — pass.** The variant axis here is the SLEPc solver family (EPS / PEP / NEP) plus the backend axis (SLEPc vs ARPACK vs QuasiNewton). All three SLEPc families are covered with per-family print-site citations; the ARPACK and QuasiNewton backends are explicitly scoped out (no `EPSConvergedReason` analogue — they fall back to parent Sub-pattern B per-callsite capture). The PEP family is asserted isomorphic-to-EPS rather than tabled explicitly; this is scoped honestly (OQ #4 offers a lowering-verifier the explicit-tabling expansion) and the print-only negative anchor is identical across families, so no hidden branch. Good coverage with explicit scope-outs.

**cross-reference-integrity — pass (with two staging-order notes, both low-severity).** All `[link]` targets resolve: `eigsolve-mutation-rotation.md`, `ksp-solve-mutation-rotation.md`, `../L1/eigsolve.md` all exist; the `EigStatus` slug and §Signature section both resolve. The Change-3 index-row OLD-string matches `book/src/L1-L0/index.md:22` verbatim. **The collision-avoidance analysis is correct:** the lifter's Change-2 OLD-string is the parent SLEPc paragraph at parent lines 293-301 (verified verbatim against the current parent), while the concurrent wave-1 abstractor dispatch (`2026-05-28T143232Z-abstractor-...`) edits only the materialisation snippet + the paragraph *ending at* parent line 291 (its Change-1 OLD-string ends at "...silent-on-this-case."). The two regions are disjoint (parent line 292 is blank between them), so Change-2's old-string still matches whether or not wave-1 lands first — the report's claim is accurate. Confirmed the wave-1 dispatch does NOT edit `index.md`, so Change-3 does not double-edit. The new file does not yet exist (consistent with NEW FILE). Two notes only: (i) `SUMMARY.md` has no nav entry for the new chapter (it only carries the parent at line 63) — this WILL break `cargo make book`; the report self-flags it (OQ #2 + NOTE after Change 3) and defers to integrator, which is honest but leaves a known build break for finalize to repair; (ii) latent staging-order coupling — wave-1's Change-5 promotes the parent to `firm` (drops partly-constructive) but does NOT update the parent index row at `index.md:22`, which the lifter's Change-3 uses as its anchor OLD-string. As of now both reports leave that row intact so there is no collision, but if any later dispatch rewrites that index row, Change-3's anchor would go stale. Not blocking for this cycle.

**edge-label-fidelity — pass.** The edge is L1>L0 (eigsolve family) throughout: the frontmatter scope, the index row, and the prose all consistently narrate L1 `EigStatus` (high) lowering into the SLEPc reason/count L0 form (low). No edge-label/prose mismatch. The high→low direction is preserved (the report's Discipline note confirms no reverse-lift prose entered the chapter; the upstream-refactor discussion is framed as a forward-looking materialisation note, the established partly-constructive idiom).

**plan-kind-consistency — pass.** Declared kind is a lifter sub-theme with status `partly-constructive (structural decomposition firm; per-row status assignment reconstructed)`. The content shape matches: firm exhaustively-cited structural decomposition (converged/diverged partition, per-family isomorphism, print-only negative anchor) + a named, negative-anchor-backed caveat on the per-row status assignment + an explicit promotion condition (upstream `EPSGetConvergedReason` consumption, gated strictly downstream of parent Sub-pattern B). This is the cycle-012 `partly-constructive` template applied correctly: it states (i) which sub-part is constructive, (ii) the negative anchors, (iii) the promotion condition. The index row (`partly-constructive ...`) and the Status section agree.

**skill-uptake-survey — pass (telemetry).** The dispatch's shape implies several skills: `verify-rotation-citation` / `verify-citation-range` (citation backfill against L0), `verify-refinement-surface` (refinement-shaped proposal), and the MCP-first localization path. The report demonstrates MCP-first localization (cites `mcp__palace-codemap__read_range` / `search_text` explicitly in Verified-against and Supporting evidence) which is the codified cycle-012 practice. It does not name-invoke the citation/refinement skills by slug, but the procedures are visibly applied (whole-tree negative-anchor search, exact-range positive citations, refinement-surface framing). Surfacing as telemetry only; not blocking.

### Issues found

1. **Partly-constructive row-count arithmetic is internally inconsistent (`9` vs breakdown summing to `8`).** [CYCLE.md §Summary line 40 and §Status lines 349-353] The headline asserts "All **9 diverged-reason rows are partly-constructive**" and "the **9 diverged-reason rows are partly-constructive**", but the parenthetical breakdown is "3 EPS diverged enumerators + the `*_CONVERGED_ITERATING` sentinel + 4 NEP-family diverged enumerators; the PEP family is isomorphic to EPS and shares its 3 rows" = 3 + 1 + 4 = **8**, not 9 (PEP shares, non-additive; the ITERATING sentinel is counted once). This is a real numeric self-contradiction in the load-bearing partly-constructive count that the dispatch was specifically asked to scrutinize. Either the headline should read 8, or one row is uncounted in the breakdown (e.g., if the ITERATING sentinel is intended per-family the breakdown text must say so and the EPS/NEP split re-stated). Severity: medium (it is the count the partly-constructive status hangs its claim on; the table and per-row notes themselves are internally consistent at 8 distinct conceptual rows — only the "9" headline is wrong).

2. **Promotion condition is stated once globally, not per-row.** [CYCLE.md §Status lines 353-361] The cycle-012 invariant requires a partly-constructive entry to carry an explicit promotion condition; this report supplies a single shared gate (the same upstream `EPSGetConvergedReason`-consumption change as parent Sub-pattern B, strictly downstream of it) covering all diverged rows collectively. This is defensible (the rows genuinely share one gate) and arguably cleaner than nine near-identical per-row conditions, but it is worth noting that the per-row reconstruction notes (lines 191-234) do not each restate the gate — a reader scanning a single row in isolation sees its status but not its promotion path without scrolling to §Status. Severity: low (the gate is explicit and present; only its locality is global rather than per-row).

3. **`SUMMARY.md` nav entry is deferred to the integrator, leaving a known `cargo make book` break.** [CYCLE.md §Change 3 NOTE + OQ #2] The new chapter `eigsolve-convergence-reason-mapping.md` has no `SUMMARY.md` line (SUMMARY.md carries only the parent at line 63). Without it the chapter does not render and `cargo make book` will warn/break. The report honestly flags this and asks integrator-per-report / integrator-finalize to add it during the build-repair pass, but it does not supply the edit (justified by old-string-safety risk). Severity: low (anticipated and surfaced; finalize routinely repairs build breakage — but it is an incomplete proposed-changes set that a reader should not mistake for a clean apply).

4. **Latent staging-order coupling between this report's index anchor and the wave-1 parent promotion.** [CYCLE.md §Change 3 vs the concurrent `2026-05-28T143232Z-abstractor-...` Change 5] The wave-1 dispatch promotes the parent theme to `firm` (drops the partly-constructive status from the theme body) but does not update the parent's index row at `book/src/L1-L0/index.md:22`. The lifter's Change-3 uses that exact unmodified row as its anchor OLD-string (adding the sibling row below it). As of now there is no collision (both reports leave the row intact), but the parent index row will then describe the promoted parent as "firm *(... partly-constructive on LinearSolveFailed)*" — and any future dispatch that corrects that row would invalidate Change-3's anchor. Worth the integrator confirming row-22 state at apply time. Severity: low (no current collision; a consistency watch-item for staging order).

5. **Parent line-count off-by-one (cosmetic).** [CYCLE.md §Append-vs-new-file decision item 4, line 78] States the parent is "911 lines"; the parent is 910 lines. Immaterial to any edit (no line-numbered edit depends on it; all edits are exact-string). Severity: trivial.

---

## Repair

All 8 critic checks already `pass`; the 5 issues are content-consistency items. Four are mechanical/surgical (repaired); one is a routing flag for the integrator (no CYCLE.md content change). The settled load-bearing partly-constructive count is **8 diverged-reason rows**.

### Fixes attempted

- **Finding 1 — partly-constructive row-count self-contradiction (`9` headline vs breakdown summing to `8`).**
  - **Decision**: repaired.
  - **Action**: Recounted from the actual mapping table + per-row notes in the CYCLE.md proposed-changes. The conceptual rows are: 2 converged (`*_CONVERGED_TOL`, `*_CONVERGED_USER`, count-anchored, NOT diverged), then the diverged/partly-constructive set = 3 EPS diverged (`*_DIVERGED_ITS`, `*_DIVERGED_BREAKDOWN`, `*_DIVERGED_SYMMETRY_LOST`) + 1 `*_CONVERGED_ITERATING` sentinel + 4 NEP-family diverged (`NEP_DIVERGED_LINEAR_SOLVE`, `NEP_DIVERGED_FUNCTION_COUNT`, `NEP_DIVERGED_SUBSPACE_EXHAUSTED`, `NEP_DIVERGED_ITS`) = 3 + 1 + 4 = **8** (PEP shares EPS's 3 rows non-additively; the sentinel counted once). Changed both "9" occurrences to "8" and appended ", non-additively" to the PEP-shares clause for clarity. (CYCLE.md §Summary line ~40 + §Status lines ~350-351.) The table and per-row notes were already internally consistent at 8; only the two "9" headlines were wrong.
  - **Rationale**: pure mechanical recount from the report's own enumerated rows; no content authored.

- **Finding 2 — promotion condition stated globally, not per-row.**
  - **Decision**: repaired.
  - **Action**: Surgical clarification in §Status making the single global gate's coverage explicit — added a sentence stating one global promotion condition covers all 8 partly-constructive rows uniformly (they share a single gate; no row carries a distinct promotion path, so it is stated once rather than restated per row). This satisfies the cycle-012 invariant's "explicit promotion condition" requirement via the "one global condition clearly covers all rows" path. (CYCLE.md §Status.)
  - **Rationale**: in-scope surgical clarification; the gate text already existed, only its global-coverage scope was made explicit. No new content.

- **Finding 3 — deferred SUMMARY.md nav entry (known `cargo make book` break).**
  - **Decision**: repaired.
  - **Action**: Confirmed the exact surrounding lines `book/src/SUMMARY.md:62-64` (parent `eigsolve-mutation-rotation` at line 63, `bicgstab-iteration` at line 64) and authored a new **Change 4** proposed-changes block (per `summary-md-surgical-insert`) inserting the `eigsolve-convergence-reason-mapping` nav line directly under the parent in the `# L1 > L0 — Lowering` Part. The old-string matches verbatim, so the apply is safe regardless of staging order. Updated OQ #2 to RESOLVED. (CYCLE.md §Change 4 + §Open-questions item 2.)
  - **Rationale**: the lifter deferred only because it could not confirm safe surrounding lines; verifying them and supplying the exact-string edit is mechanical. This removes the anticipated finalize build break.

- **Finding 4 — index-row staging coupling with wave-1 parent-promotion report.**
  - **Decision**: not-needed (FLAG for integrator; no CYCLE.md content change).
  - **Action**: None to CYCLE.md. Recorded the disjoint-region confirmation for integrator apply-ordering awareness — see "Note for integrator" below. The critic already verified Change-2's old-string (parent SLEPc paragraph, parent lines 293-301) and the wave-1 abstractor's Change-1 (materialisation snippet ending at parent line 291) are disjoint (blank line 292 between), and that wave-1 does NOT edit `index.md`, so Change-3's index-row anchor (`index.md:22`) does not collide today.
  - **Rationale**: this is a cross-report apply-ordering concern, not a defect in this report; repair authority does not extend to other reports. Routed to the integrator as an awareness note, not deferred to a follow-up agent.

- **Finding 5 — parent line-count off-by-one (911 vs 910).**
  - **Decision**: repaired.
  - **Action**: Changed "911 lines" to "910 lines" (confirmed via `wc -l` = 910). (CYCLE.md §Append-vs-new-file decision item 4.)
  - **Rationale**: trivial cosmetic fix; no line-numbered edit depends on it.

### Unrepairable findings

None. All five findings were either repaired (1, 2, 3, 5) or are integrator-routing awareness notes that require no content authoring (4).

### Note for integrator (apply-ordering awareness)

This report and the concurrent wave-1 dispatch `reports/2026-05-28T143232Z-abstractor-eigsolve-getconverged-forwarder-fix-and-gated-promotion/` both touch the parent `book/src/L1-L0/eigsolve-mutation-rotation.md`, but in **disjoint regions** (confirmed by the critic):
- This report's **Change 2** edits the parent SLEPc forward-pointer paragraph (parent lines ~293-301).
- Wave-1's Change 1 edits the parent materialisation snippet ending at parent line 291.
- Parent line 292 is blank between them; the two old-strings match verbatim regardless of which applies first.
- This report's **Change 3** anchors on `book/src/L1-L0/index.md:22` (the parent index row); wave-1 does NOT edit `index.md`, so no double-edit. Watch-item: wave-1 promotes the parent body to `firm` but leaves index row 22 unchanged, so the row will still read "firm *(... partly-constructive on LinearSolveFailed)*" after both apply — accurate to neither-yet-corrected state; harmless this cycle, but a future row-22 rewrite would stale Change-3's anchor.
- New file **Change 1** (`eigsolve-convergence-reason-mapping.md`) and SUMMARY nav **Change 4** are fully independent of wave-1.

## Suggested resolution

`overall_status: ready`. All checks pass; all consistency findings repaired (load-bearing count settled at **8** diverged-reason partly-constructive rows; SUMMARY.md nav supplied as Change 4; cosmetics fixed). Integrator may apply this report's four changes in any order relative to the wave-1 parent-promotion report — the touched parent regions and the index row are disjoint per the note above. No follow-up agent required.
