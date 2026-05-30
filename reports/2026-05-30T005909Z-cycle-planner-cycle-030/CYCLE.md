---
agent: cycle-planner
invoked_at: 2026-05-30T005909Z
scope: cycle-030 dispatch plan
status: pending
---

# Cycle-030 dispatch plan

**Cycle-030 is the THIRD/FINAL primary cycle of meta-batch-8 (cycles 028/029/030).** The batch-8 meta-phase fires after this cycle's integrator-finalize commit. Sizing: dispatches are moderate (recommend ~6 max) to leave headroom for batch-8 meta-phase enactments (methodology codification, obstruction sub-kind refinement, OQ unification, cycle-planner repropose-staleness bullets, etc.).

## Goals selected this cycle

Cycle-029 landed **6 clean reports** (zero deferrals, zero rejections): back-solve-mutation-rotation + bilinear-form-mutation-rotation (two firm L1>L0 themes), triangular-solve-obstruction (first opaque-library-ownership obstruction), ls_update_column (firm L1 leaf for the GMRES per-column running-QR), normalize-B prose correction (F1 evidence tightening), and L2-L1/L2 index prose refresh. All now eligible for follow-up audits and live-link upgrades. **Cycle-030 goals:** (1) dispatch the standard firm→next-cycle `verified_against:` audits for the three new firm c029 themes/leaf (closing the sibling-theme audit pattern with HIGH quality-assurance); (2) author the forthcoming `ls-update-column-mutation-rotation` L1>L0 theme to **COMPLETE the GMRES inner-loop L1>L0 cohort** (back_solve + ls_update_column + orthogonalize all firm, all lowerings from L1 to L0 complete); (3) clean up c029-routed residuals (plain-text-ref upgrade, verified_against F1 row refresh); (4) optional low-fan-out same-layer-cross-cutter candidate (sparse_triangular_solve slice reduction). The cohort closure is HIGH fan-out; the audits are HIGH quality-signal; the residuals are LOW but necessary hygiene.

## Dispatches

1. **(`lowering-verifier`, `back-solve-mutation-rotation` — cycle-030 `verified_against:` audit)**
   - scope: audit the firm L1>L0 theme `book/src/L1-L0/back-solve-mutation-rotation.md` landed cycle-029; standard per-line `verified_against:` YAML block enumerating Palace source sites + L1 vs L0 form citations
   - deps: none (the theme is on disk, landing report-1 c029)
   - rationale: firm theme → next-cycle audit (precedent: `normalize-mutation-rotation` c028, `back_solve` leaf c028, `eigsolve-mutation-rotation` c025, etc.). The theme is the GMRES/FGMRES restart-correction back-solve-to-Hessenberg descending-column-oriented back-substitution lowering — high-confidence evidence target. Routes per `integrator-signals.md` cycle-029 §Suggested next dispatches item-1.

2. **(`lowering-verifier`, `bilinear-form-mutation-rotation` — cycle-030 `verified_against:` audit)**
   - scope: audit the firm L1>L0 theme `book/src/L1-L0/bilinear-form-mutation-rotation.md` landed cycle-029; standard `verified_against:` YAML block enumerating Palace source sites (the workspace-mediated `M.Mult(y, Mx); dot(comm, x, Mx)` composition) + L1 vs L0 form citations
   - deps: none (the theme is on disk, landing report-2 c029)
   - rationale: firm theme → next-cycle audit (same precedent). The theme is the energy-norm inner product `⟨x, Bx⟩` lowering (off-diagonal sibling to `matrix-weighted-norm-mutation-rotation`). Routes per integrator-signals cycle-029 §Suggested item-2.

3. **(`lowering-verifier`, `ls_update_column` — cycle-030 `verified_against:` audit)**
   - scope: audit the firm L1 leaf `book/src/L1/ls-update-column.md` landed cycle-029; standard `verified_against:` YAML block enumerating Palace source sites (the GMRES/FGMRES per-column running-QR `iterative.cpp:634-640` / `:813-819` streaming kernels) + L1 law confidence + variant axes (real/complex, static/dynamic array shapes)
   - deps: none (the leaf is on disk, landing report-4 c029)
   - rationale: firm L1 leaf → next-cycle audit (precedent: `back_solve` c028 audit). The leaf is the terminal Face-1 opaque-leaf projection of the firm L2 `incremental-least-squares` named composition — high-confidence surface. Routes per integrator-signals cycle-029 §Suggested item-3.

4. **(`abstractor`, `ls-update-column-mutation-rotation` — L1>L0 lowering theme)**
   - scope: author the L1>L0 mutation-rotation theme for the firm `ls_update_column` leaf (palace/linalg/iterative.cpp:634-640 GMRES + :813-819 FGMRES); sibling to the c029-landed `back-solve-mutation-rotation` theme and the firm `orthogonalize-mutation-rotation` (c024); the theme lowers the per-column running-QR streaming step into its L0 Givens-generation/application loop forms
   - deps: none (the L1 leaf is firm on-disk; no forward-ref hazard; the `back-solve-mutation-rotation` target exists on-disk; orthogonalize theme is firm)
   - rationale: HIGH fan-out — this is the FINAL piece of the **GMRES inner-loop L1>L0 cohort completion** (`ls_update_column × (j+1) ▷ back_solve` = the full restart-cycle least-squares-solve stream, all three pieces now have L1>L0 lowerings). The cohort closes the c028-routed `incremental-least-squares-composition-lowering` theme's Face-1/Face-2 decomposition. Routes per integrator-signals cycle-029 §Suggested item-4 ("completes the GMRES inner-loop L1>L0 cohort").

5. **(`lifter` or `same-layer-cross-cutter`, `L2-L1/incremental-least-squares-composition-lowering` — plain-text-ref → live-link upgrade)**
   - scope: re-link the now-on-disk `ls_update_column` at three locations in `book/src/L2-L1/incremental-least-squares-composition-lowering.md`: (a) line :69 — mechanical slug-relink (plain-text `ls_update_column` → live `[`ls_update_column`](../L1/ls-update-column.md)`); (b) lines :87-88 — substantive prose rewrite (the sentence "forthcoming / not yet on disk / plain text per the rough-in-forward-reference convention" is now factually obsolete — must be replaced, not just relinked, to reflect the landed status); (c) lines :307-310 — speculative-L1-operators §framing update to mark the column-streaming leaf as a closed-target record (not speculative)
   - deps: dispatch-4 must apply first (if dispatch-4 is ls-update-column-mutation-rotation theme authoring, the theme is also new-on-disk, so the :69 ref's live-link target is firm when this dispatch reads; the prose rewrites at :87-88/:307-310 are independent — they're framing updates on c029-landed content)
   - rationale: LOW fan-out but HIGH priority for coherence. The theme is firm (`rough-in` → `firm` c028); its prose still carries obsolete "forthcoming" framing from when the L1 leaf didn't exist. The :87-88 rewrite is substantive (beyond mechanical-relink integrator-skill scope), appropriate for a lifter. Routes per integrator-signals cycle-029 §Suggested item-5. NOTE: sequence dispatch-4 before dispatch-5 so the dispatcher can read dispatch-4's landed slug for live-link anchoring if needed.

6. **(`lowering-verifier`, `normalize-mutation-rotation` — `verified_against:` row :466-469 refresh)**
   - scope: the verified_against block in `book/src/L1-L0/normalize-mutation-rotation.md` carries an audit row at :466-469 with verdict `does-not-support` + an F1 diagnostic note. The c029 prose correction (report-5) rewrote the "no fused B-Normalize" note to "exists but uncalled" + tightened the promotion gate. The row F1 cited the OLD prose; the verdict is now STALE. Audit the row against the corrected "exists but uncalled" prose + the tightened gate; refresh the verdict + note to reflect the new framing.
   - deps: none (the normalize files are both on-disk with c029 edits; the verified_against block exists)
   - rationale: LOW fan-out, audit-row staleness only (not a defect of the firm unweighted core per c029 integrator notes). The c029 integrator explicitly flagged this as a future lowering-verifier refresh task. Clean up before batch-8 meta-phase unification pass. Non-gating, non-blocking hygiene. Routes per integrator-signals cycle-029 §Suggested item-6.

## Overlap analysis

**Dispatch 1 (back-solve-mutation-rotation audit) vs others:**
- vs 2: disjoint files (back-solve-mutation-rotation.md vs bilinear-form-mutation-rotation.md); both audit `verified_against:` blocks in different themes; parallel.
- vs 3: disjoint files (back-solve theme vs ls_update_column leaf); both audit `verified_against` blocks; parallel.
- vs 4: disjoint files (back-solve audit in theme file vs ls-update-column-mutation-rotation in new L1>L0 theme file); parallel.
- vs 5: disjoint files (back-solve audit vs L2-L1 theme relink); parallel.
- vs 6: disjoint files (back-solve audit vs normalize prose refresh); parallel.

**Dispatch 2 (bilinear-form-mutation-rotation audit) vs others:**
- vs 1,3,4,5,6: all disjoint files; parallel to all.

**Dispatch 3 (ls_update_column audit) vs others:**
- vs 1,2,4,5,6: all disjoint files (L1 leaf audit vs others); parallel to all.

**Dispatch 4 (ls-update-column-mutation-rotation theme) vs others:**
- vs 1,2,3: new file creation (book/src/L1-L0/ls-update-column-mutation-rotation.md); will also update L1-L0/index.md + SUMMARY.md but disjoint from themes 1/2's audits; parallel.
- vs 5: FORWARD-REFERENCE DEPENDENCY — dispatch-5 needs to re-link the now-on-disk `ls_update_column` at :69. If dispatch-4 creates the new L1>L0 theme file, the :69 live-link target is firm when dispatch-5's integrator runs. However, dispatch-5's main task (substantive prose rewrite at :87-88) is independent. SEQUENCE dispatch-4 before dispatch-5 for hygiene, but could be parallel if integrator reads dispatch-4's report to extract the new slug (practice: serial for safety).
- vs 6: disjoint files (new L1>L0 theme vs normalize audit); parallel.

**Dispatch 5 (incremental-least-squares-composition-lowering relink) vs others:**
- vs 1,2,3,6: disjoint files; parallel.
- vs 4: FORWARD-REFERENCE DEPENDENCY (see above); SEQUENCE: dispatch-4 first.

**Dispatch 6 (normalize-mutation-rotation F1 row refresh) vs others:**
- vs 1,2,3,4,5: all disjoint; parallel.

**Summary:** Dispatches 1–3 are pure audits (read-only on verify_against blocks); dispatch-4 creates a new file + updates index/SUMMARY; dispatch-5 has a forward-ref dependency on dispatch-4's slug and updates L2-L1 prose; dispatch-6 refreshes a normalize audit row. **Genuine conflict only between 4 and 5** (forward-ref to dispatch-4's new slug). **Recommended sequencing:** Wave-1 (dispatches 1, 2, 3, 6 — parallel, all audits + normalize refresh, no conflicts); Wave-2 (dispatches 4 and 5 — 4 first, then 5 reads dispatch-4's report for the new slug).

## Sequencing schedule

**Wave-1 (parallel, no inter-wave dependencies):**
- dispatch-1: lowering-verifier, back-solve-mutation-rotation audit
- dispatch-2: lowering-verifier, bilinear-form-mutation-rotation audit
- dispatch-3: lowering-verifier, ls_update_column audit
- dispatch-6: lowering-verifier, normalize-mutation-rotation F1 row refresh

**Wave-2 (after Wave-1 reports land; internally sequential: dispatch-4 before dispatch-5):**
- dispatch-4: abstractor, ls-update-column-mutation-rotation L1>L0 theme
- dispatch-5: lifter, incremental-least-squares-composition-lowering plain-text-ref upgrade (reads dispatch-4's report for the new ls-update-column-mutation-rotation slug + applied-at timestamp for live-link verification)

**Rationale:** Wave-1 parallelizes the four independent audit/refresh tasks (1/2/3/6); no ordering constraint. Wave-2 sequences the theme authoring (4) before the relink (5) so the integrator can apply dispatch-4's chapter-writes to disk before dispatch-5's integrator reads the L2-L1 theme file to verify the :69 link target will exist. The per-report integrators serialize across dispatches anyway, but explicit sequencing avoids any forward-reference hazard for the :69 live-link upgrade.

## Open questions / caveats

1. **Dispatch-5 prose-rewrite scope at :87-88** — The integrator signals flagged that the "forthcoming / not yet on disk" sentence at :87-88 is factually obsolete and must be **replaced, not relinked**. This is beyond the mechanical-token-relink integrator skill scope and appropriate for a lifter. However, the substantive content of the replacement prose should express the same structural point (that the theme forward-referenced the L1 leaf before it landed, and now it does). Recommend the lifter read the c029 STAGING.md report-4 notes + the ls_update_column.md landing to understand the forward-ref resolution, then compose a replacement sentence that notes the leaf's landed status without changing the theme's structural narrative. **Delegation note to the lifter:** the replacement prose should NOT introduce new citations or structural claims — it's a factual update on the resolve status, not a substantive rewrite.

2. **Dispatch-4 architectural decision** — The ls-update-column-mutation-rotation theme will describe the per-column running-QR lowering from L1 (the pure `ls_update_column` streaming operator) to L0 (the iterative.cpp:634-640 / :813-819 Givens-generation/application loops). The theme may surface sub-patterns for the `GeneratePlaneRotation` / `ApplyPlaneRotation` helper boundaries. Recommend the abstractor survey whether those helpers have dedicated L1 entries (or should be treated as L0-only) before commit. This is a navigational question, not a blocking one — the theme can note them as forthcoming if needed.

3. **Dispatch-5 integrator live-link verification** — After dispatch-4's integrator lands the new `book/src/L1-L0/ls-update-column-mutation-rotation.md` file, dispatch-5's integrator must verify the :69 live-link target `[`ls_update_column`](../L1/ls-update-column.md)` points to an on-disk file before upgrading the plain-text reference. The per-report integrator's "re-read disk before each Edit" discipline covers this, but the dispatcher should note that the dispatch order matters for the file existence precondition. **Already covered by Wave-2 sequencing above.**

4. **Optional dispatch-7 candidate** — The cycle-029 signals routed a LOW-fan-out `same-layer-cross-cutter` candidate: `spec/slices/sparse_triangular_solve.md` phase-1 slice-reduction audit. Now that the L1>L0 obstruction theme `triangular-solve-obstruction` is on-disk (c029 report-3), the slice may be reduced to a stub or removed, using the skill `phase-1-slice-reduction-audit`. The integrator-signals note explicitly flagged this as **OPTIONAL** — cycle-030 may defer to keep budget light for the batch-closing role. **Recommendation:** DEFER this to c031 to leave more headroom for batch-8 meta-phase. The slice reduction is hygiene, not blocking. Cycle-030 dispatch count is 6; batch-closing should be moderate.

## Discipline checks

✓ **Verify each candidate is genuinely OPEN** (Discipline bullet, cycle-027 meta-phase):
- Dispatch-1 (back-solve audit): c029 STAGING.md row-1 shows theme landed firm, ready for audit. Not already in counts_after as "audited" — audit is a c030 addition. **OPEN.**
- Dispatch-2 (bilinear-form audit): c029 STAGING.md row-2, theme landed firm. Not in counts_after as audited. **OPEN.**
- Dispatch-3 (ls_update_column audit): c029 STAGING.md row-4, leaf landed firm. Not in counts_after as audited. **OPEN.**
- Dispatch-4 (ls-update-column-mutation-rotation theme): c029 signals routed as a "forthcoming" abstractor target (cycle-029 §Suggested item-4). The L1 leaf landed c029. The theme does NOT exist on disk (not in book/src/L1-L0/ or in SUMMARY.md). **OPEN.**
- Dispatch-5 (incremental-least-squares plain-text-ref upgrade): c029 signals routed as "not-yet-upgraded" (integrator Notes flagged the `:69`/`:87-88`/`:307-310` plain-text refs as "NOT upgraded inline this integration" — deferred to OQ). **OPEN.**
- Dispatch-6 (normalize F1 row refresh): c029 integrator-signals flagged as a "low-priority, non-gating, audit-row staleness only" refresh. c029 STAGING.md report-5 promoted OQ `normalize-mutation-rotation-verified-against-row-466-469-stale-after-c029-prose-correction`. **OPEN.**

✓ **Exactly ONE integrator-finalize per primary cycle** (Discipline bullet, cycle-027 meta-phase):
- Wave-1 + Wave-2 are dispatch / forward-ref ordering ONLY. The cycle-030 finalize runs ONCE at cycle end (after all 6 per-report integrators complete), not per-wave. The book is NOT rebuilt between waves. All count bumps + housekeeping happen at integrator-finalize, not during dispatch phases. **CONFIRMED.**

---

**Dispatch summary:**
- 6 total dispatches (moderate, batch-closing sizing — leaving headroom for meta-phase).
- 4 lowering-verifier (audits 1/2/3/6).
- 1 abstractor (theme-authoring 4).
- 1 lifter (prose-relink 5).
- Wave-1: 4 parallel audits (no inter-deps).
- Wave-2: 2 sequential (4→5 forward-ref dependency).
- **Cohort closure:** GMRES inner-loop L1>L0 cohort complete (all three pieces firm + lowering themes).
- **Quality signal:** firm→next-cycle audit pattern applied to 3 new firm c029 deliverables.
- **Batch-8 closing:** cycle-030 leaves artifact + plan coherent for batch-8 meta-phase enactments.
