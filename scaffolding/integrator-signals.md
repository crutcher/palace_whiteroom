# Integrator → planner signals

Append-only running ledger. The integrator appends a section at the **top** after each cycle's integration commit (newest first). The next cycle's `cycle-planner` reads the most recent ~3 entries as input to dispatch planning.

**User directive (2026-05-27):** the integrator should have a channel to write information used by the planner about next/unblocked/resolution/etc options implied by the integration. This file is that channel.

**Format** (per-cycle section):

```markdown
## cycle-<n> — <ISO-timestamp>

### Unblocked
- <one-line item per now-tractable priority / question> — <citation: priority slug or open-question slug>

### New dependencies
- <one-line edge that landed this cycle> — <citation: report / commit>

### Resolution implications
- <open-question slug> — <answered | partially-answered | needs-more> — <one-line how this cycle's landings bear on it>

### Suggested next dispatches
- (`<agent>`, `<scope>`) — <one-line rationale>

### Wave-conflict observations
- <one-line case where dispatches conflicted at integration; how the integrator resolved>

### Integration-tooling friction
- <one-line case where the integrator hit a gap that better tooling would close>
```

---

## cycle-028 — 2026-05-29T205500Z

**FIRST primary cycle of meta-batch-8 (cycles 028/029/030). The batch-8 meta-phase fires after the cycle-030 finalize commit — this section OPENS the batch-8 evidence window.** 7 of 7 dispatched-ready reports applied clean; zero deferrals, zero rejections. NO crash. Twenty-fourth consecutive clean split-integrator cycle. STAGING 7/7 rows == dispatched-ready-reports (the cycle-018 staging-completeness gap did NOT recur for the NINTH consecutive cycle). Build `cargo make book` exit 0, ZERO build-repairs. retroactive-budget global 0.

### Unblocked
- `back-solve-mutation-rotation` L1>L0 theme — now actionable: the `back_solve` L1 leaf is firm (c027) AND its `verified_against:` audit landed this cycle confirming firm; it has no lowering theme yet — citation: report-4 (back-solve-audit) + roadmap intermediate-tier "Sparse triangular solve" row.
- `bilinear-form-mutation-rotation` L1>L0 theme — the survey (report-6) confirmed this theme does NOT exist on disk; authoring it is the cheapest in-scope step toward bilinear-form firmness (the test-coverage gates need an out-of-scope Palace-source change) — citation: OQ `bilinear-form-mutation-rotation-l1-l0-theme-needed-c028`.
- `triangular-solve-obstruction` L1>L0 theme — the `trsv` leaf resolved-by-obstruction this cycle (report-7); the obstruction theme would give the resolved leaf a citable home, citing HYPRE relax-type sites + external direct-solver wrappers as negative anchors — citation: OQ `triangular-solve-obstruction-l1-l0-theme-needed-c028`.
- `normalize_B` F1 prose correction — the normalize audit (report-3) found a defined-but-uncalled fused `Normalize(comm,x,B,Bx)` at `palace/linalg/operator.hpp:377-384`, contradicting the theme's "no fused B-Normalize" prose; the prose rewrite ("exists but uncalled") + `normalize_B` promotion-gate tightening is a follow-up abstractor task — citation: OQ `normalize_B-note-says-no-fused-B-Normalize-but-uncalled-fused-operator-exists`.
- `ls_update_column-column-streaming-leaf-harvest` — the new L2>L1 theme (report-1) names this forthcoming Face-1 column-streaming leaf as a plain-text forward-ref; a follow-on harvester would realize it (small L1 column-streaming leaf, co-keyed with the back_solve cohort) — citation: OQ `ls_update_column-column-streaming-leaf-harvest`.

### New dependencies
- `L2-L1/incremental-least-squares-composition-lowering` (firm L2>L1 theme) → `L1/back_solve` + `concepts/givens_generate`/`givens_apply` + `L2/linear_combination` + (forthcoming, plain-text) `ls_update_column` — the running-QR fan-down edge landed; terminal back-solve targets the firm `back_solve` leaf, NOT a general `trsv` — citation: report-1 + `L2-L1/index.md` row 20.
- `L2/incremental-least-squares` → `L2-L1/incremental-least-squares-composition-lowering` — the L2 entry's deferred "forthcoming L2>L1 theme" pointer (the load-bearing rotation-stream non-associativity) now has a real lowering home — citation: report-1.

### Resolution implications
- `l3-vocabulary-inventory-gap` (plan-owned, `priorities.md:24`) — **RESOLVED** — the `trsv` leaf (last of four: gemv/ksp_solve/eigsolve done) resolves resolved-by-obstruction (Palace has no standalone `trsv` primitive); parent plan item fully resolved (report-7). Meta-phase: close `:24` + mark the `:498` leaf resolved-by-obstruction.
- `incremental-least-squares-composition-lowering-theme-deferred-needs-back-solve-reanchor` (c027 D5 carry-forward) — **RESOLVED** — the theme landed firm fresh this cycle (report-1).
- `incremental-least-squares-composition-lowering-verifier-audit` (ledger :785) — **RESOLVED** — the standard firm follow-up audit appended this cycle, firm confirmed (report-5).
- `normalize-mutation-rotation-lowering-verifier-audit` (plan-owned, `priorities.md:24,49`) — **RESOLVED** — audit upholds firm with one routed F1 (report-3).
- `back-solve-lowering-verifier-audit` (plan-owned, `priorities.md:24`) — **RESOLVED** — fully-supported, firm upheld (report-4).
- `linalg-operator-file-category-mislabel-residual-lines-22-87` (plan-c028-active-#2, `:767`) — **RESOLVED** — the `:22`/`:87` Category-2→Category-1 relabel landed (report-2).
- `l2-incremental-least-squares-self-description-still-says-queued-after-firming` (plan-c028-active-#2, `:768`) — **RESOLVED** — the `:13` stale-queued drop landed (report-2).
- `matrix-weighted-norm-mixed-element-type-variant` (plan-c028-active-#4, `:769`) — **NARROWED, stays OPEN** — element-type axis now shape-witnessed by `test-orthog.cpp`; residual is the named-entry-point √+SPD-guard test (report-6). Meta-phase: update the `:769` prose, do NOT close.

### Suggested next dispatches
- (`abstractor`, `back-solve-mutation-rotation`) — the firm `back_solve` leaf's L1>L0 lowering theme; HIGH-ish fan-out (the GMRES/FGMRES restart-correction); now fully unblocked (leaf firm + audited).
- (`abstractor`, `bilinear-form-mutation-rotation`) — the missing L1>L0 theme; highest-fan-out + cheapest next step toward `bilinear-form` firmness per report-6.
- (`abstractor`, `triangular-solve-obstruction`) — the obstruction theme citing HYPRE relax-type + external-direct-solver negative anchors; LOW fan-out (obstruction leaf, no upstream combinator) but gives the resolved-by-obstruction `trsv` a citable home. Cheaper alternative: accept the existing `L3/index.md:7` line as already-sufficient.
- (`abstractor`, `normalize_B` F1 prose correction on `normalize-mutation-rotation` + `L1/normalize.md`) — rewrite "no fused B-Normalize" → "exists but uncalled" + tighten the `normalize_B` promotion gate; firm core unaffected.
- (`harvester`, `ls_update_column`) — the forthcoming Face-1 column-streaming leaf the new L2>L1 theme forward-references plain-text; small L1 column-streaming leaf.
- (`lifter` or `layer-intro-author`, `L2-L1/index.md` + `L2/index.md` prose refresh) — the `roadmap.md` L2>L1 lead prose was stale at "2 firm themes" (cycle-018 era); accurate count is 8 (7 firm + 1 partly-constructive). The index dep-map is authoritative; a navigational-prose refresh would re-sync the Part overview.

### Wave-conflict observations
- One intra-cycle dependency (not a conflict): report-1 (the D1 lifter creating the new L2>L1 theme file) MUST land before report-5 (the D5 lowering-verifier audit appending a `verified_against:` block to that same file). The per-report integrators dispatched serially in the correct order (report-1 at 20:12Z, report-5 at 20:27Z) — dependency satisfied, the theme file existed (499 lines) before the append. No artifact collision.
- No two reports touched the same file with conflicting edits. `scaffolding/open-questions.md` was appended by all seven (append-only, no collision).

### Integration-tooling friction
- **Leading-`"` `verified_against:` note channel-format hazard** (report-5's integrator flagged for the meta-phase): two `note:` values in the incremental-ls audit block began with a literal double-quote (`note: "Why this is NOT a general trsv" …`), which `yaml.safe_load` parses as a quoted scalar that ends at the closing `"` then chokes on the trailing text. The per-report integrator repaired it by single-quote-wrapping (`note: '"…" …'`). This is a recurring transport hazard for the `verified_against:` note channel — a candidate for a channel-format rule (always single-quote a note value, or forbid leading `"`). Meta-phase to consider (NOT enacted by finalize).
- The legacy-vs-current-era `log/cycle-NNN.md` filename collision recurred (current-era cycle-028 overwrites a frozen slice-vertical-era stub; content in git history). The current era progressively reclaims the namespace per the cycle-020→027 precedent — low-friction but the README still carries dangling legacy index entries for the clobbered files (pre-existing; out of finalize scope). A meta-phase one-time legacy-index cleanup would close it.

---

## cycle-027 — 2026-05-29T211500Z

**THIRD / FINAL primary cycle of meta-batch-7 (cycles 025/026/027). The batch-7 meta-phase fires after THIS cycle-027 finalize commit — this is the BATCH-CLOSING signal dump.** 5 of 6 dispatched reports applied clean; the 6th (D5) DEFERRED needs-revision. NO crash. Twenty-third consecutive clean split-integrator cycle. STAGING 5/5 rows == dispatched-ready-reports (D5 deferred, correctly NOT staged — not a completeness gap). Build `cargo make book` exit 0, ZERO build-repairs. retroactive-budget global 0.

### Unblocked
- `incremental-least-squares-composition-lowering` L2>L1 theme — now has a firm `back_solve` leaf to re-anchor its terminal back-solve refs to (the D5 deferral's primary blocker is partially lifted by the D4 `back_solve` landing) — `incremental-least-squares-composition-lowering-theme-deferred-needs-back-solve-reanchor`.
- `normalize-mutation-rotation` lowering-verifier audit — the L1>L0 theme landed firm this cycle, so the standard `verified_against:` audit is now dispatchable (firm→next-cycle-audit pattern) — c028 lowering-verifier.
- `back_solve` law-confidence / lowering-verifier audit — the new firm L1 leaf is audit-ready; also its own L1>L0 `back-solve-mutation-rotation` theme is now authorable (abstractor) — c028.
- `ls_update_column` column-streaming leaf harvest — the slug is now cleanly reserved (D4 took `back_solve`, leaving `ls_update_column` free for the distinct GMRES/FGMRES per-column running-QR streaming step) — c028 harvester (gating the D5 promotion if needed).

### New dependencies
- `book/src/L1/back_solve.md` (firm) → `incremental-least-squares` (L2, firm) — the terminal `back_solve` projection of the firm L2 named composition; cited via the L1 entry's §Semantics — report-4 (`harvester-ls-update-column-l1`).
- `book/src/L1-L0/normalize-mutation-rotation.md` (firm) → `book/src/L1/normalize.md` (firm) — the L1>L0 mutation-rotation lowering; the `normalize.md:104` ref UPGRADED plain-text→live-link this cycle — report-1 (`abstractor-normalize-rotation`).
- `book/src/L2/ksp_solve.md` → `book/src/L2/incremental-least-squares.md` (live link) + the `back_solve`-output cross-reference at §Semantics phase-3 — report-6 (`lifter-ksp-solve-materialise-iterate-cite-tightening`).
- `book/src/concepts/givens.md:29` → `palace/linalg/iterative.cpp:634-640` (source-cite re-anchor, was `gmres.md`) — report-2 (`lifter-cycle026-hygiene-reanchors`).

### Resolution implications
- `ls-update-column-l1-leaf` — **answered/RESOLVED** — landed firm under the renamed slug `back_solve` (NOT `ls_update_column`); the `ls_update_column` slug stays free for the column-streaming leaf; the `trsv` L3-inventory gap stays OPEN (`back_solve` is a sibling, not the realisation, of general `trsv`).
- `normalize-mutation-rotation-l1-l0-theme` — **answered/ENACTED** — the firm L1>L0 theme landed; the residual is the standard `verified_against:` lowering-verifier audit (c028).
- `matrix-weighted-norm-mutation-rotation-lowering-verifier-audit-followup` — **answered/AUDIT-CLOSED** — verdict fully-supported, theme stays firm; residual `matrix-weighted-norm-mixed-element-type-variant` L1-ENTRY promotion gate migrates to the plan (the L1 entry stays `rough-in (test-coverage-bounded)`).
- `l2-ksp-solve-materialise-iterate-incremental-least-squares-cite-tightening` — **answered/ENACTED** — applied at both `:83` and `:123`.
- the four cycle-026 carry-forward hygiene OQs (`matrix-weighted-norm-l1-entry-norml2-body-brace-boundary-drift-601-606`, `bilinear-form-workspace-category-4-mislabel`, `givens-concept-page-source-cite-staleness-gmres-md-should-be-iterative-cpp`, `bilinear-form-slug-name-coordination`) — **answered/RESOLVED** for the named sites (the `:22`/`:87` Category sites split off to a NEW residual OQ).
- `incremental-least-squares-composition-lowering-theme-deferred-needs-back-solve-reanchor` — **needs-more** — D5 DEFERRED to c028; the `back_solve` leaf now exists to re-anchor to, but the theme also needs `trsv`↔`back_solve` reconciliation + possibly the column-streaming `ls_update_column` leaf.
- `l2-incremental-least-squares-self-description-still-says-queued-after-firming` (NEW) + `linalg-operator-file-category-mislabel-residual-lines-22-87` (NEW) — **opened** for c028 follow-up sweeps.

### Suggested next dispatches
- (`lifter`, `incremental-least-squares-composition-lowering-promotion`) — the deferred D5 theme: re-anchor the terminal back-solve refs to the now-firm `back_solve` leaf + reconcile `trsv`↔`back_solve` + reconcile `ls_update_column` (column-streaming) vs `back_solve` (terminal solve). **HIGH-value c028 plan item.**
- (`harvester`, `ls_update_column-column-streaming-leaf`) — the still-un-harvested column-streaming `ls_update_column` leaf (the GMRES/FGMRES per-column running-QR streaming step), if the D5 promotion needs it.
- (`lifter`/`repairer`, `linalg-operator-file-category-mislabel-residual-sweep`) — the `:22`/`:87` Category-4→Category-1 residual sweep + the `incremental-least-squares.md:13` "queued"→"firm" self-description drop.
- (`lowering-verifier`, `normalize-mutation-rotation-audit` + `back_solve`-paired) — the standard `verified_against:` audit of the now-firm `normalize-mutation-rotation` L1>L0 theme + the `back_solve` law-confidence audit (firm→next-cycle-audit pattern).
- (`abstractor`, `back-solve-mutation-rotation`) — the L1>L0 lowering theme for the new firm `back_solve` leaf (`R·y=s` back-substitution → the in-place GMRES/FGMRES `iterative.cpp:652-660`/`:831-840` loops).

### Wave-conflict observations
- **`SUMMARY.md` serialized cleanly** across report-1 (`normalize-mutation-rotation` registration, L1>L0 Part) and report-4 (`back_solve` registration under L1) — disjoint anchors; serial per-report integrators re-read SUMMARY from disk before each edit.
- **`matrix-weighted-norm` touched by two reports without conflict** — D2 touched the L1 entry `L1/matrix-weighted-norm.md` (brace + Category relabel); D3 touched the L1>L0 theme `L1-L0/matrix-weighted-norm-mutation-rotation.md` (additive `verified_against:`) — distinct files.
- **D4/D5 slug collision = the coordinated-cross-report-rename trap.** D4 (`back_solve` harvest) + D5 (`incremental-least-squares-composition-lowering` theme) collided on `ls_update_column`; the coordinated-rename instruction's premise was INVERTED relative to the artifact (D5's theme legitimately keeps `ls_update_column` for the column-streaming step; D4's leaf is the terminal back-solve, renamed `back_solve`). D4 applied clean (its `back_solve` slug was re-confirmed collision-free at integration: grep `book/src/L1/` + `SUMMARY.md` → zero hits); D5's repairer caught the inversion → `needs-revision` → DEFERRED. **The collision was resolved by RENAMING the leaf (D4), not the theme (D5) — the theme's slug usage was correct.**

### Integration-tooling friction
- **(a) STRONG enactment candidate — codemap `read_range` +1 brace-boundary drift, CONFIRMED across batches 5/6/7.** Cycles 024/025/026/027 all hit it; this cycle the D2 lifter's `matrix-weighted-norm.md` brace re-anchor `:601-606`→`:602-606` is the same `+1` class on a brace-opening line, plus multiple producers + the audits re-confirmed across the batch. The standing OQ `codemap-read-range-plus-one-drift-on-brace-boundary` recommends strengthening role-specs to **"codemap is localization-only; citecheck/on-disk is the citation source of truth"** + possibly a standing citecheck `--anchor` per-report gate (now that `tools/citecheck` is wired). **The batch-7 meta-phase should ENACT this** — it is no longer a single-cycle noise signal, it is a persistent 4-cycle / 3-batch pattern.
- **(b) NEW process-friction signal — the coordinated-cross-report-rename trap.** When two same-cycle dispatches collide on a slug and the parent issues a coordinated-rename instruction, that instruction can encode an INVERTED premise about which dispatch "owns" the slug's meaning. This cycle the premise was inverted (D5's theme legitimately owned `ls_update_column` for the column-streaming step; the rename should have — and did — fall on D4's terminal-back-solve leaf). The D5 repairer caught it and filed skill-candidate `audit-slug-meaning-before-coordinated-cross-report-rename`. **The meta-phase should evaluate that skill-candidate + consider whether harvester/abstractor dispatches should run a pre-harvest slug-collision check against the existing artifact vocabulary BEFORE harvesting** (catch the collision at dispatch-plan time, not at repair time).
- **(c) D5 deferral mechanics.** The split-integrator deferral path worked correctly: D5 came back `needs-revision`, was NOT staged, NOT marked `integrated_at`, and was routed forward via a carry-forward OQ — the artifact stayed coherent (the un-landed theme left no dead link because its forward-refs were never applied). `rows (5) == dispatched-ready-reports (5)`; the deferral is the expected path, distinct from the cycle-018 staging-completeness GAP.
- **(d) `scaffolding/integrator-signals.md` well over the ~500-line budget** (archival backlog accumulating since ~cycle-007; ~1455 lines as of cycle-025 + cycle-026/027 additions). **The batch-7 meta-phase should do the archival** (move pre-batch-5 sections to an archive file or compact them) alongside the OQ unification pass.
- **(e) OQ-ledger retirement/unification readiness.** Many OQ lines are now retirement/unification-ready: the c025 `:327` four-slug audit-followup line + `:322` index-refresh line, plus this batch's many clause-scoped RESOLVED/ENACTED dispositions (append-only, status-lines not struck per convention). **The batch-7 meta-phase OQ unification pass should close/migrate/compact these.**

### batch-7 cohort summary (for the meta-phase aggregation)
- **L1 firm 19→21** (+`normalize` c026, +`back_solve` c027).
- **L2 firm 8→9** (+`incremental-least-squares` c026 stub→firm).
- **L1>L0 firm themes +2** (`matrix-weighted-norm-mutation-rotation` c026, `normalize-mutation-rotation` c027).
- **L1>L0 lowering-verifier audits**: the 3 cycle-025-new themes audited c026 (all stay firm) + `matrix-weighted-norm-mutation-rotation` audited c027 (stays firm).
- **Cohorts COMPLETE:** `l2-named-composition-lifts` 2/2 (orthogonalize + incremental-least-squares); `normalize-l1-primitive-harvest` (operator c026 + L1>L0 theme c027); NEP-interior atom cohort 5/5 (closed c024, audited c025/c026); eigsolve L1→L2→L3→L2>L1→concept chain FULLY COMPLETE + audited.
- **Big multi-cycle citation-hygiene sweep** across the batch (NLEPS/eigsolve drift swaps c026 + the c027 brace/Category/source-cite re-anchors) — the codemap-drift friction was the recurring source.
- **Unchanged at batch close:** L3 9 firm + 2 partial-obstruction; L4 4 firm; L0 22 chapters; Phase-1 removals 9/10.

**Discipline:**

- Integrator appends each cycle (prepended at top — newest first).
- Cycle-planner reads top ~3 entries.
- Keep file under ~500 lines; entries older than 10 cycles archive to `scaffolding/integrator-signals-archive/cycle-<n>-<n+9>.md`.
- No other agent writes here. (If meta-phase needs to annotate, append a `<!-- meta-phase: ... -->` HTML comment to the relevant section.)

---

## cycle-026 — 2026-05-29T2030Z

(Second primary cycle of meta-batch-7, cycles 025/026/027; meta-phase fires after cycle-027 finalize. 9 reports, all `applied`, 9/9 staging rows == dispatched-ready. Headlines: L1 firm 19→20 (+`normalize`), L2 firm 8→9 (+`incremental-least-squares`, `l2-named-composition-lifts` cohort COMPLETE 2/2), L1>L0 firm themes +1 (`matrix-weighted-norm-mutation-rotation`), the 3 cycle-025-new firm themes' `verified_against:` audit cohort complete, + NLEPS/eigsolve citation-hygiene + navigational sweep.)

### Unblocked
- `l2-ksp-solve-materialise-iterate-incremental-least-squares-cite-tightening` — NOW ACTIONABLE: the L2 `incremental-least-squares` entry is firm, so the `ksp_solve.md` §Semantics phase-3 `materialise_iterate` forward-reference to it can be cite-tightened (separate dispatch; gate satisfied). — citation: STAGING.md D2 row + OQ same-slug.
- forward-referenced `normalize-mutation-rotation` L1>L0 theme — NOW AUTHORABLE: the firm L1 `normalize` operator exists, so the abstractor can author its `linalg::Normalize` → `nrm2`/`scal` lowering theme (stub-on-integration acceptable if forward-referenced again). — citation: STAGING.md D4 row + OQ `normalize-mutation-rotation-l1-l0-theme`.
- paired `bilinear-form` firm-promotion + `matrix-weighted-norm-mixed-element-type-variant` lowering-verifier audit — NOW SCHEDULABLE: the `matrix-weighted-norm-mutation-rotation` theme is firm, so the standard `verified_against:` audit of it + the paired `bilinear-form-mutation-rotation` audit / firm-promotion can be dispatched. — citation: STAGING.md D3 row + OQ `matrix-weighted-norm-mixed-element-type-variant`.

### New dependencies
- L1 `normalize` → `nrm2`, `scal` (firm leaves) — NEW firm L1 operator; the fused vector-normalisation gate, returns the norm as a first-class result. — citation: `book/src/L1/normalize.md`, STAGING.md D4.
- L2 `incremental-least-squares` → `iterative.cpp` running-QR / Givens-rotation stream (GMRES/FGMRES) — NEW firm L2 named composition (second after `orthogonalize`); the running-QR least-squares stream + terminal `back_solve`. — citation: `book/src/L2/incremental-least-squares.md`, STAGING.md D2.
- L1>L0 `matrix-weighted-norm-mutation-rotation` → `operator.cpp:599-619` `linalg::Norml2(comm,x,B,Bx)` — NEW firm L1>L0 theme (the energy norm `√(xᴴBx)` lowering); a firm lowering of a rough-in L1 operator per the `eigsolve-mutation-rotation` precedent. — citation: `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md`, STAGING.md D3.
- 8 plain-text→live-link cross-ref edges across the eigsolve chain (`L1/L2/L3/eigsolve.md` + `L2/gram.md` → `concepts/eigsolve.md`, `L2-L1/eigsolve-spectral-transform-composition.md`, `L2-L1/gram-fold-specialization.md`) — the chain's navigational wiring is now live (targets landed cycle-025). — citation: STAGING.md D7.

### Resolution implications
- `normalize-as-fused-l1-primitive` + `normalize-and-normalize-b-weighted-l1-candidates` — **answered** — decided YES for `normalize` (firm); `normalize_B` as an in-chapter rough-in note with a stated future-promotion trigger. Plan item `normalize-l1-primitive-harvest` COMPLETE. — STAGING.md D4.
- `incremental-least-squares-as-future-L2-firstclass-entry` + `gmres-givens-stream-as-step-kernel-borderline` — **answered** — incremental-least-squares is a distinct named composition (NOT a krylov-step axis); the `l2-named-composition-lifts` cohort is COMPLETE (orthogonalize + incremental-least-squares both firm). — STAGING.md D2.
- `matrix-weighted-norm-mutation-rotation-l1-l0-theme` — **answered** — theme firmed this cycle (stub→firm). — STAGING.md D3.
- 3 NLEPS L1-entry re-anchor OQs (`nleps-jacobian-action-six-anchor`, `nleps-eigenvalue-correction-two-anchor`, `vector.cpp:667→:668 sibling-sweep`) — **answered** — all applied by D1's lifter; both L1 entries + the inner-product theme/entry now agree with on-disk source. — STAGING.md D1.
- the 3 cycle-025-new firm themes' lowering-verifier audit-followup OQs — **answered** — all DISCHARGED (24/19/15-entry `verified_against:` landed, all fully-supported, all stay firm). — STAGING.md D6a/D6b/D6c.
- the eigsolve-chain cross-ref / `gram.md` "(forthcoming)" / `concepts-eigsolve-chain-live-link` OQs — **answered** — all upgraded to live links by D7. — STAGING.md D7.
- the L0 naming-residue / dependency-map-stale-edge / negative-result-slice-reciprocal OQs — **answered** — 3 RESOLVED + `bilinear-form-slug-name-coordination` ADDRESSED-AT-L0 (one residual `bilinear-form.md:416` routed to a follow-up). — STAGING.md D5.

### Suggested next dispatches
- (`abstractor`, `normalize-mutation-rotation`) — author the forward-referenced L1>L0 `normalize-mutation-rotation` theme now that the firm L1 `normalize` operator exists.
- (`lifter`/`harvester`, `matrix-weighted-norm-l1-entry-reanchor` + `bilinear-form-provenance-refresh`) — apply the NEW carry-forward re-anchors: `operator.cpp:601` brace drift on the L1 `matrix-weighted-norm` entry (`:58`,`:83`); `bilinear-form.md:416` `dot_bilinear` provenance note; `concepts/givens.md:29` `gmres.md`→`iterative.cpp` staleness; the Category-4 workspace mislabel (`L1/matrix-weighted-norm.md:9` + `L0/linalg-operator-file.md:33`).
- (`lowering-verifier`, `matrix-weighted-norm-mutation-rotation-audit` + paired `bilinear-form`) — the standard `verified_against:` audit of the now-firm `matrix-weighted-norm-mutation-rotation` + the paired `bilinear-form-mutation-rotation` audit / firm-promotion.
- (`cross-layer-cross-cutter` / `combinator-miner`, frontier vocabulary) — next fan-out-ranked component per the plan (NEP cohort + eigsolve chain + l2-named-composition cohort now all complete; the frontier shifts to the remaining shared-infrastructure / intermediate-tier items — plane-rotation-stream L4, diagonal-preconditioner-apply, residual-update, restart-machinery).

### Wave-conflict observations
- **`SUMMARY.md` touched by 3 reports (D2 `:45`, D3 `:103`, D4 `:68`) at disjoint anchors** — the serial per-report integrator order re-read SUMMARY from disk before each edit; no collision. The per-layer index files (`L2/index.md` D2, `L1-L0/index.md` D3, `L1/index.md` D4) likewise disjoint.
- **`eigsolve.md` (L1/L2/L3) touched by D7 only; the D6c audit touched the DIFFERENT file `L2-L1/eigsolve-spectral-transform-composition.md` (the theme)** — no contention; D7 (last) re-read all four entry files from disk before editing.
- **Serial dependency held (no stub needed)** — D7's 8 live-link upgrades depend on the cycle-025-landed targets (`concepts/eigsolve.md`, the two L2-L1 themes), all on-disk before this cycle began; no plain-text forward-reference dangled.

### Integration-tooling friction
- **codemap `read_range` +1 brace-boundary drift CONFIRMED across a THIRD batch** — the cycle-026 D1 lifter + multiple producers re-confirmed the `+1` drift on brace-opening lines (`nleps.cpp` deflation block; `operator.cpp:601`). citecheck/`--anchor` + on-disk is the citation source-of-truth. **STRONG batch-7 meta-phase enactment candidate**: strengthen role-specs to "codemap is localization-only; citecheck/on-disk is the citation source of truth," and possibly add a standing citecheck per-report gate (now that `tools/citecheck` is wired). The standing OQ `codemap-read-range-plus-one-drift-on-brace-boundary` carries the second/third-cycle-confirmation clause.
- **Non-blocking citecheck AMBIG prose tokens** inside report CYCLE.md files (bare-basename readability shorthand with a resolving full-path canonical form in the same report) — NOT in the artifact, not chased.
- **`scaffolding/integrator-signals.md` ~1455 lines as of cycle-025** (over the ~500-line budget; entries older than 10 cycles should archive to `scaffolding/integrator-signals-archive/`) — still a pre-existing meta-phase archival backlog task; per-report/finalize integrators are append-only here and do not compact.

## cycle-025 — 2026-05-29T1715Z

**FIRST primary cycle of meta-batch-7 (cycles 025/026/027). The batch-7 meta-phase fires after the cycle-027 finalize commit** (3:1 cadence; cycle counter does NOT reset across batch boundaries) — dispatched separately. 9 reports all applied clean (9/9 staging rows; SEVENTH consecutive cycle with no staging-completeness gap). Twenty-first consecutive clean split-integrator cycle. NO crash this cycle (cycles 023/024 were crash-recovered). HEADLINE: the **NEP-interior L1>L0 cohort is COMPLETE 5/5** AND the **eigsolve L1→L2→L3→L2>L1→concept chain is FULLY COMPLETE**; the **batch-6 lowering-verifier audit cohort is 4/4 discharged**.

### Unblocked
- **NEP-interior L1>L0 cohort fully lowered** — both remaining atoms' L1>L0 themes landed firm (`nleps-jacobian-action-mutation-rotation`, `nleps-eigenvalue-correction-mutation-rotation`); the per-step quasi-Newton chain `residual→jacobian-action→eigenvalue-correction→deflated-solve→line-search` is now lowered L1>L0 end-to-end — OQs `nleps-jacobian-action-mutation-rotation-l1-l0-lowering-theme`, `nleps-eigenvalue-correction-mutation-rotation-l1-l0-lowering-theme` (both ENACTED this cycle).
- **eigsolve chain authoring-complete + navigationally homed** — the L2>L1 edge (`eigsolve-spectral-transform-composition`, firm) + the cross-cutting `concepts/eigsolve` page both landed; the migrated-to-plan item `eigsolve-l2-l1-and-concept` is FULLY discharged (`open-questions.md:37` / Closed-index `:323`) — ready for meta-phase Closed-index migration.
- **`L2/eigsolve.md:163` pending-forward-ref → live-link upgrade** now tractable (target `eigsolve-spectral-transform-composition` on disk) — OQ `eigsolve-l2-entry-lowers-from-pending-forward-reference-upgrade`; follow-up lifter/layer-intro-author using `upgrade-plain-text-ref-to-live-link-when-target-on-disk`.
- **The three chain-entry stale "concepts/eigsolve does not yet exist" prose** (L1 §Context, L2 §Dependencies, L3 §Context) now upgradable to a live link — recorded in the `concepts-eigsolve-page-still-absent` RESOLVED disposition.

### New dependencies
- `nleps-jacobian-action-mutation-rotation` (L1>L0 firm) → `nleps_jacobian_action`/`apply_nonlinear_pencil` law 1+3 / `lu_solve` kernel / `apply_linop` / `ksp_solve` / L2 `linear_combination` / L1-L0 residual+solve+apply-nonlinear-pencil+lu-solve+dot siblings + L2-L1 `linear-combination-fold-specialization` — `book/src/L1-L0/nleps-jacobian-action-mutation-rotation.md`.
- `nleps-eigenvalue-correction-mutation-rotation` (L1>L0 firm) → `nleps_eigenvalue_correction`/`dot` Sub-pattern A conjugation / `axpbypcz` γ=0 / `scal` negation; siblings nleps-jacobian-action + nleps-deflated-solve + nleps-deflated-residual + apply-nonlinear-pencil + dot + axpbypcz + scal mutation-rotations — `book/src/L1-L0/nleps-eigenvalue-correction-mutation-rotation.md`.
- `eigsolve-spectral-transform-composition` (L2>L1 firm) → L2 `eigsolve` / L1 leaves `apply_linop`+`ksp_solve`+`scal`+`apply_nonlinear_pencil`+`eigsolve`; L3 `eigsolve` partial-obstruction as a BOUNDARY (NOT re-derived); sibling L2-L1 `orthogonalize-composition-lowering`/`gram-fold-specialization`/`deflate-composition-lowering`; concepts sequential-obstruction/solver-as-operator/constructed-operators/variant-absorption — `book/src/L2-L1/eigsolve-spectral-transform-composition.md` (`apply_shift_invert = apply_linop(M) ▷ ksp_solve((K − σM)⁻¹)`).
- `concepts/eigsolve` (concept page) → the firm L1→L2→L3 chain entries + L0 `eigensolver-wrapper`; NEP-interior cohort; L1>L0 `eigsolve-mutation-rotation`/`eigsolve-convergence-reason-mapping`; introduces the `EigSolver[problem]` opaque type; frames `solve-monad` as the FUTURE L4 surface — `book/src/concepts/eigsolve.md`.
- `apply-nonlinear-pencil-mutation-rotation` gained an additive `verified_against:` (21 entries, all `supports`) — theme stays firm.
- `gram-fold-specialization` gained an additive `verified_against:` (13 entries) + an in-theme `vector.cpp:667→:668` `MFEM_ASSERT` aligned-pass anchor correction (both in-theme sites) + an enclosing-range tighten `nleps.cpp:613-619→:614-619` — theme stays firm.
- `deflate-composition-lowering` gained an additive `verified_against:` (19 entries) + a `gate_verdict: stays-gated-correctly` block — theme STAYS partly-constructive.

### Resolution implications
- `eigsolve-l2-l1-spectral-transform-composition-lowering-theme-needed` (cycle-024 carry-forward) — **answered/ENACTED** — the firm L2>L1 theme landed; the parent is already migrated-to-plan (`open-questions.md:37` / Closed-index `:323`), ready for meta-phase CLOSE.
- `concepts-eigsolve-page-still-absent` — **answered/ENACTED** — the full firm concept page landed; the migrated-to-plan `eigsolve-l2-l1-and-concept` item is now FULLY discharged (both halves landed this cycle); residual chain-entry live-link-upgrade follow-up recorded.
- `apply-nonlinear-pencil-mutation-rotation-lowering-verifier-audit-followup` (1st of 4 on `open-questions.md:327`) — **answered/RESOLVED** — audit fully-supported, theme firm, no gate; clause-scoped RESOLVED disposition appended.
- `gram-fold-specialization-l2-gram-forward-reference-closure-followup` (3rd of 4 on `:327`) — **answered/RESOLVED** — forward-reference closure CONFIRMED, audit discharged.
- `orthogonalize-composition-lowering-three-way-delegation-boundary-audit` (4th/last of 4 on `:327`) — **answered/RESOLVED** — verdict cleanly-partitioned, audit discharged; **the whole `:327` line is now retirement/unification-ready** (all four clauses have dispositions).
- `deflate-composition-lowering-mutation-rotation-lowering-verifier-audit-followup` (2nd of 4 on `:327`) — **partially-answered/RE-SCOPED** — the audit HALF is discharged (gate confirmed sound) but the promotion-watch REMAINS OPEN (the shared bare-Galerkin-core gate did not unblock; no positive bare-Gram `(XᴴX)⁻¹` solve exists in `palace/*.cpp`); re-scope to a deferred/contingent promotion-watch co-keyed with `deflate-galerkin-core-promotion` (`open-questions.md:35`), trigger = a positive bare-Gram-solve site surfaces.
- `eigsolve-firm-stale-cycle-009-narrative-bullet-routes-to-layer-intro-author` (2nd of 3 on `open-questions.md:322`) — **answered/ENACTED** — the cycle-009 historical-marker edit landed at `L1/index.md:108`.
- `lu-solve-layer-intro-count-refresh-and-fifth-motif` (1st of 3 on `:322`) — **answered/already-satisfied-on-disk** — motif-6 `lu_solve` + `Firm (19)` count already present from cycles 019/022/024; **the whole `:322` line is now retirement-ready** pending the 3rd-clause `l1-index-fifth-motif` confirm.

### Suggested next dispatches
- (`lifter`/`repairer`, `nleps-l1-entry-citation-correction`) — one pass applying both carry-forward NLEPS L1-ENTRY re-anchor OQs (`nleps_jacobian_action` 6 deflation-block anchors; `nleps_eigenvalue_correction` `:596→:590` while-loop + add `:712` `alpha *= backtrack_factor`) PLUS the `vector.cpp:667→:668` sibling sweep (`inner_product.md:360` + `inner-product-fold-specialization.md:59,260`).
- (`lifter`/`layer-intro-author`, `eigsolve-chain-cross-ref-cleanup`) — upgrade `L2/eigsolve.md:163` pending-forward-ref + the three chain-entry "concepts/eigsolve does not yet exist" prose to live links; refresh `gram.md:176,242` "(forthcoming)".
- (`cross-layer-cross-cutter`, `constructed-solver-opaque-type-watch`) — watch for a THIRD consumer of the `EigSolver[problem]`-style constructed-solver opaque type before warranting a generic `constructed-solver-opaque-type` concept page (currently only 2 consumers).
- (`harvester`/`abstractor`, frontier vocabulary) — NEP cohort + eigsolve chain now complete; the fan-out frontier shifts to the remaining shared-infrastructure / intermediate-tier items per the plan.

### Wave-conflict observations
- **Shared-file landings serialized cleanly.** `SUMMARY.md` + `L1-L0/index.md` (reports 1+2, L1>L0 block); `SUMMARY.md` + `L2-L1/index.md` (report 3, L2>L1 block); `SUMMARY.md` + `concepts/index.md` (report 4, concepts block). Each per-report integrator re-read the shared file from disk before editing; reports 1/2 did not touch the L2-L1 block, so report 3's `deflate-composition-lowering` insert-anchors were exactly as authored.
- **Serial dependency held, no stub needed.** Report 2's primary insert-anchor was report 1's just-landed `nleps-jacobian-action-mutation-rotation` row/entry; the documented serial dependency held (primary anchors used, fallbacks not needed), so no plain-text forward-reference dangled and no implied-component stub was created.
- **`gram-fold-specialization` vs `deflate-composition-lowering`** shared the `L2-L1/` directory but edited disjoint files; no contention. The `orthogonalize-composition-lowering` audit was verdict-only (no file touched).

### Integration-tooling friction
- **codemap `read_range` +1 brace-boundary drift recurred** (nleps.cpp deflation block) vs citecheck/on-disk — the SAME class as cycle-024's 5 off-by-one drifts. **citecheck/`--anchor`/on-disk is the citation source-of-truth.** Methodology signal for the batch-7 meta-phase: now that `tools/citecheck` is wired (cycle-024 enactment), evaluate whether per-report-gate citecheck `--anchor` invocation should be standing (catches anchor-level drift that `--scan` does not report).
- **Non-blocking citecheck AMBIG prose-shorthand inside report CYCLE.md files** (`dot.md:43`/`:49` bare-basename, `operator.cpp:621-638` cross-tree basename) — each has a resolving full-path canonical form in the same report; readability shorthand, NOT a missing/out-of-range citation. NOT in the artifact; not chased by finalize.
- **Four lowering-verifier audits, three with additive `verified_against:`/`gate_verdict:` YAML appends + one verdict-only** — confirms the audit-as-additive-provenance pattern (cross-cutter-consumed) is stable; the verdict-only case (`orthogonalize-composition-lowering`, where prior coverage already exists) correctly proposes NO new rows to avoid duplication. The nested-fence convention (`~~~yaml`/` ```edit `/4-space-indent stand-ins → real ```yaml fences) held across all appends with zero truncation.

## cycle-024 — 2026-05-29T1400Z

**THIRD/FINAL primary cycle of meta-batch-6 (cycles 022/023/024). The batch-6 meta-phase fires after THIS cycle-024 finalize commit** (3:1 cadence; cycle counter does NOT reset) — dispatched separately. 8 reports all applied clean (8/8 staging rows; SIXTH consecutive cycle with no staging-completeness gap). Twentieth consecutive clean split-integrator cycle. **Second consecutive crash-recovered cycle** — a mid-cycle machine crash interrupted the cycle after all eight per-report integrators had completed + staged; finalize resumed clean from the authoritative STAGING.md + working-tree cross-check.

### Unblocked
- **NEP-interior atom L1>L0 themes** (`nleps_jacobian_action`, `nleps_eigenvalue_correction`) — both L1 atoms landed firm this cycle, so their L1>L0 lowering themes are now authorable — OQs `nleps-jacobian-action-mutation-rotation-l1-l0-lowering-theme`, `nleps-eigenvalue-correction-mutation-rotation-l1-l0-lowering-theme`.
- **L2>L1 `eigsolve-spectral-transform-composition` theme** — the L2 `eigsolve` entry is firm (c023) and the L3 entry is now firm-partial-obstruction (c024), so the L2>L1 spectral-transform composition lowering is fully anchored on both ends — OQ `eigsolve-l2-l1-spectral-transform-composition-lowering-theme-needed` (`:807`).
- **Optional L3>L2 `eigsolve` body-identity audit anchor** — the L3 entry's per-step body is identity-in-form to firm L2; a lowering-verifier may anchor the audit — OQ `eigsolve-l3-l2-body-identity-audit-anchor-optional-followup`.
- **`deflate` Galerkin-core promotion (still gated, but now fully scoped)** — the L2>L1 `deflate-composition-lowering` audit follow-up may UNBLOCK the shared bare-Gram-solve promotion without ENACTING — OQ `deflate-composition-lowering-mutation-rotation-lowering-verifier-audit-followup`.

### New dependencies
- `nleps_jacobian_action` (L1 firm) → `apply_linop`/`apply_nonlinear_pencil`/divided-difference `A2'` — realizes the `T'` derivative-pencil that `apply_nonlinear_pencil` law 5 deferred — `book/src/L1/nleps_jacobian_action.md` (`nleps.cpp:649-669`).
- `nleps_eigenvalue_correction` (L1 firm) → dot/axpby/scal — the per-step `δλ` Rayleigh-functional correction over firm BLAS-1 leaves — `book/src/L1/nleps_eigenvalue_correction.md` (`nleps.cpp:672-677`).
- `nleps-deflated-solve-mutation-rotation` (L1>L0 firm) → `nleps_deflated_solve`/`ksp_solve`/`lu_solve`/`dot`/`axpy` — `book/src/L1-L0/nleps-deflated-solve-mutation-rotation.md` (`nleps.cpp:504-537`).
- `apply-nonlinear-pencil-mutation-rotation` (L1>L0 firm) → `apply_nonlinear_pencil`/`apply_linop`/`axpby`/`axpbypcz` — `book/src/L1-L0/apply-nonlinear-pencil-mutation-rotation.md` (`nleps.cpp:807-821`).
- `gram-fold-specialization` (L2>L1 firm) → `gram`/`dot`/`inner-product-fold-specialization` — `book/src/L2-L1/gram-fold-specialization.md` (`nleps.cpp:524-531`).
- `deflate-composition-lowering` (L2>L1 partly-constructive) → `deflate`/`gram`/`lu_solve`/`linear_combination`/`dot` + `gram-fold-specialization` — `book/src/L2-L1/deflate-composition-lowering.md` (`nleps.cpp:505-537`).
- `eigsolve` (L3 partial-obstruction) lifts_from L2 `eigsolve` (firm) / same-layer deps `ksp_solve`+`apply_linop` — the eigen-iteration loop is opaque-library-owned (SLEPc `EPSSolve` `slepc.cpp:694` / ARPACK `naupd` RCI `arpack.cpp:318`) — `book/src/L3/eigsolve.md`.

### Resolution implications
- `l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog` (`:624`, cycle-021 prediction) — **CONFIRMED** — the linear-EVP eigsolve landed `partial-obstruction` exactly as predicted; the eigen-iteration is opaque-library-owned, no Palace-authored eigen-step kernel. Ready for meta-phase CLOSE to the Closed index.
- `nleps-interior-atoms-remaining-jacobian-action-and-eigenvalue-correction` (`:779`) + its cycle-024 carry-forward (`:859`) — **answered (both halves landed firm)** — the NEP-interior atom cohort is complete; ready for meta-phase CLOSE of both.
- `nleps-deflated-solve-l1-l0-lowering-theme` (`:784`, opened cycle-023) — **ENACTED** — the theme is authored firm on disk (`book/src/L1-L0/nleps-deflated-solve-mutation-rotation.md`). Ready for meta-phase Closed-index migration.
- `dot-mutation-rotation-subpattern-d-citation-fix` (`:847`, cycle-023 carry-forward) — **RESOLVED** — the `orthog.hpp:34`→`:35` one-token fix landed + `verified_against:` block; theme stays firm. Ready for meta-phase CLOSE.
- eigsolve chain prerequisite OQs (`:613` step-3, `:802` stub-materialization) — **satisfiable** — step-3 (L3 backfill) DONE; the cycle-023 stub is now refined to firm partial-obstruction. Meta-phase can re-frame step-3-DONE + migrate the stub-materialization OQ to RESOLVED.
- `deflate` bare-Galerkin-core promotion (`:774`) — **needs-more (stays OPEN)** — three artifacts now share this single gate (L2 `deflate` + L1>L0 `nleps-deflated-solve` + L2>L1 `deflate-composition-lowering`); all promote together on a positive bare-Gram-solve site outside the Schur wrapping. None this cycle.
- `eigsolve-l4-surface-solve-monad-unauthored-future-dispatch` (new) — **needs-more** — the speculative L4 surface; plain-text-deferred (not clearly-implied, below the stub bar).

### Suggested next dispatches
- (`abstractor`, `nleps_jacobian_action` L1>L0 + `nleps_eigenvalue_correction` L1>L0) — the two remaining NLEPS L1>L0 lowering themes; both L1 atoms now firm.
- (`abstractor`, `eigsolve-spectral-transform-composition` L2>L1 theme) — fully anchored now that L2 + L3 eigsolve entries are firm.
- (`lowering-verifier`, `apply-nonlinear-pencil-mutation-rotation` audit) + (`lowering-verifier`, `deflate-composition-lowering` audit) — standard post-landing audits; the deflate audit may UNBLOCK the shared Galerkin-core promotion.
- (`layer-intro-author`, `concepts/eigsolve` page) — the still-absent eigsolve concept page (OQ `concepts-eigsolve-page-still-absent`).
- (`lowering-verifier` or `harvester`, L3>L2 `eigsolve` body-identity audit anchor) — optional, low-fan-out.
- Forward-frontier: a different solver pipeline's shared infrastructure (FE assembly / boundary conditions / a smoother) now that the NLEPS/eigsolve vocabulary cohorts are largely complete.

### Wave-conflict observations
- `book/src/L1/index.md` (Firm-count headline + cohort-list + dep-map) + `SUMMARY.md` shared by the two NEP-atom harvests (reports 1+2) — only the single Firm-count cell needed additive reconciliation (17→18 then 18→19, the second re-read disk); all other inserts non-overlapping by construction. Clean serial handoff.
- `book/src/L1-L0/index.md` + `SUMMARY.md` shared by the two L1>L0 abstractor themes (reports 3+4) — distinct slugs, non-overlapping; report 4 re-read disk and matched anchors verbatim. No count cell at L1>L0.
- `book/src/L2-L1/index.md` + `SUMMARY.md` shared by the two L2>L1 abstractor themes (reports 5+6) — distinct slugs; report 6 re-anchored after report 5's `gram-fold-specialization` row/entry (the sibling moved the on-disk last entry), non-clobbering. Plus the in-cycle live-link upgrade (report 6 re-linked its `gram-fold-specialization` refs once report 5 existed on disk).
- No conflict on L3 / `dot-mutation-rotation` — reports 7 + 8 were sole writers of their respective files (a surgical SUMMARY relabel at `:31` for the L3 entry; the `dot-mutation-rotation` anchor-fix).

### Integration-tooling friction
- **Second consecutive machine-crash recovery (recovery-not-normal-path, FLAGGED for batch-6 meta-phase).** A machine crash interrupted the cycle after all eight per-report integrators had completed + staged. Finalize recovered by reading the (complete, authoritative) STAGING.md + cross-checking the working tree; no per-report re-application or working-tree reconciliation was needed. With cycle-023 this is TWO clean crash/resume cycles — strong evidence the split-integrator staging-log channel survives crashes idempotently. No tooling gap surfaced; a resilience datapoint for the meta-phase.
- **Continuing inline-anchor-drift pattern (RECURRENCE, FLAGGED for batch-6 meta-phase).** Cycle-024 critics found 5 off-by-one drifts in the l3-eigsolve report (arpack.cpp :573/:579/:270; slepc.cpp :1857/:1873, repairer-corrected) + 1 each in 3 other reports. SAME pattern that escalated the batch-5 citation-checker ASK — now realized as `tools/citecheck` (enacted `88b7893`, user go). The meta-phase should evaluate whether `citecheck` is being invoked (producers/critics) and whether to make it a per-report gate. The cycle-024 `dot-mutation-rotation` carry-forward `orthog.hpp:34`→`:35` is itself the discharge of a prior drift instance.
- **Critic-off-by-one-on-an-off-by-one (`apply-nonlinear-pencil`).** The critic flagged `nleps.cpp:810-811` as a cosmetic off-by-one to shift to `:809-810`; the dispatch directive + repairer correctly determined `:810-811` is right — the critic's finding was itself off by one. A datapoint that anchor-drift findings need verification both ways (a mechanical checker would adjudicate).

<!-- meta-phase: batch-6 (cycles 022/023/024) fires after this cycle-024 finalize commit. Three FLAGGED items above: (a) machine-crash recovery resilience datapoint; (b) continuing inline-anchor-drift → citecheck invocation/gate question; (c) the OQ-closure batch ready for migration. -->

---

## cycle-023 — 2026-05-29T1046Z

(SECOND primary cycle of meta-batch-6 — cycles 022/023/024. **The batch-6 meta-phase fires after the cycle-024 finalize commit** — does NOT fire this cycle. **CRASH-RECOVERED:** a machine crash interrupted the cycle after all six `integrator-per-report` runs had completed + staged; `integrator-finalize` resumed clean from the authoritative STAGING.md + working-tree cross-check, no per-report re-application/reconciliation needed. 6 dispatches → 6 applied clean (all wave-1); staging reconcile clean (6 rows == 6 dispatched ready reports). Build: `cargo make book` exit 0, zero build-repairs, no dead-link errors.)

### Unblocked
- **The L3 `eigsolve` backfill (chain step 3)** is now UNBLOCKED — `book/src/L2/eigsolve.md` landed firm this cycle (chain step 2), and `book/src/L3/eigsolve.md` was materialized as a `stub` (its home). The strict prerequisite chain is now L1-firm (cycle-022) → L2-firm (cycle-023, DONE) → **L3 backfill (UNBLOCKED, the stub is its home)**, predicted terminal status `partial-obstruction` (the eigen-iteration loop is opaque-library-owned — SLEPc `EPSSolve` / ARPACK RCI, no Palace-authored kernel/driver pair). — OQ `eigsolve-l2-firm-landed-chain-step-2-done-l3-backfill-unblocked` / `eigsolve-l3-stub-materialized-cycle-024-backfill-refines-in-place` / `l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog`
- **The eigsolve L2>L1 spectral-transform-composition lowering theme** is now authorable (the L2 `eigsolve` firm anchor exists) — narrates the `apply_shift_invert = apply_linop(M) ▷ ksp_solve((K − σM)⁻¹)` composition lowering forward into L1. — OQ `eigsolve-l2-l1-spectral-transform-composition-lowering-theme-needed`
- **The remaining NLEPS interior atoms** (Jacobian-action + eigenvalue-correction) are the next fan-out-ranked NLEPS L1 pieces now that `nleps_deflated_solve` landed firm. — OQ `nleps-interior-atoms-remaining-jacobian-action-and-eigenvalue-correction`
- **The `nleps_deflated_solve` L1>L0 lowering theme** is now authorable (the L1 anchor is firm). The `apply_nonlinear_pencil` L1>L0 leaf is the other still-unthemed NLEPS L1>L0 forward-reference. — OQ `nleps-deflated-solve-l1-l0-lowering-theme` / `nleps-deflated-residual-l1-l0-interior-leaf-themes-still-forward-referenced`
- **A `concepts/eigsolve` page** is still absent despite the now-firm L1 + L2 `eigsolve` entries (a layer-intro-author candidate). — OQ `concepts-eigsolve-page-still-absent`

### New dependencies
- `book/src/L1/nleps_deflated_solve.md` (NEW firm) → the firm L1 leaves (`ksp_solve`, `lu_solve`, `dot`, …); the Schur-complement deflated block solve at `nleps.cpp:504-537`; the next fan-out-ranked NLEPS interior piece. L1 firm 16→17. — report 1
- `book/src/L2/eigsolve.md` (NEW firm) → `ksp_solve` (L2; the inner solve inverting the shifted operator) + `apply_linop` / `apply_nonlinear_pencil` (L1; the M/PEP-block / NEP operand applies); the named shift-invert spectral-transform composition. Chain step 2. L2 firm 7→8. — report 3
- `book/src/L3/eigsolve.md` (NEW `stub`) → claim-free placeholder; the chain step-3 home (implied-component stub, ≥2 converging refs). Refined in place cycle-024. — report 3 (discretionary stub)
- `book/src/L1-L0/lu-solve-mutation-rotation.md` (NEW firm) → L0 inline-Eigen sites (`nleps.cpp` full-pivot-LU, `romoperator.{cpp,hpp}` full-pivot-QR) + the firm L1 `lu_solve` anchor; 2 sub-patterns + load-bearing factorization-kernel axis. Discharges the `lu_solve` half of the NLEPS L1>L0 cohort. — report 4
- `book/src/L1-L0/nleps-deflated-residual-mutation-rotation.md` (NEW firm) → L0 `nleps.cpp:547-577` (`compute_residual` lambda) + `:329-347` (MatVecMult) + the firm L1 `nleps_deflated_residual` anchor; 3 sub-patterns. Discharges the `nleps_deflated_residual` half of the cohort. — report 5
- `book/src/L2-L1/orthogonalize-composition-lowering.md` (stays firm; +`verified_against:` 17-citation yaml) → orthog.hpp ×5 + iterative.cpp/romoperator.cpp dispatch/consumers ×6 + test-orthog.cpp ×4 + cross-theme delegation anchors ×3; confirming audit, no status flip. 0 count delta. — report 6
- `book/src/L1/index.md` semantic-motif taxonomy 4→6 (motif 5 operator-introspection + motif 6 coordinate-space dense direct algebra) + §Working-Notes eigsolve-firm bullet; navigational, 0 count delta. — report 2

### Resolution implications
- `eigsolve-l1-firm-landed-chain-step-1-done-l2-entry-unblocked` (cycle-022) — **answered** — the L2 entry landed firm this cycle (chain step 2 done).
- `nleps-deflated-solve-is-next-fan-out-ordered-nleps-piece-and-l2-deflate-gram-positive-site` (cycle-022) — **partially-answered** — `nleps_deflated_solve` landed firm (the NLEPS-piece half); the deflate-positive-site half is **NEGATIVE** (the bare `(XᴴX)⁻¹` Galerkin core never appears — only ever Schur-wrapped), so the `deflate` promotion gate STAYS OPEN against a positive bare-Gram-solve site outside `nleps.cpp`.
- `lu-solve-mutation-rotation-l1-l0-theme-needed` / `nleps-deflated-residual-l1-l0-lowering-theme-needed` (cycle-022) — **answered** — both L1>L0 themes landed firm this cycle.
- `orthogonalize-composition-lowering-three-way-delegation-boundary-audit` (cycle-022) — **answered** — the lowering-verifier audit confirms fully-supported, theme stays firm; also discharges the cycle-019 `orthogonalize-composition-lowering-l2-l1-theme` (was blocked on the L2 anchor) + the L2>L1 side of `orthogonalize-mutation-rotation-l1-l0-theme-should-cite-dot-subpattern-d`.
- `deflate-l2-partly-constructive-landed-promotion-gates-on-positive-galerkin-site` (cycle-022) — **needs-more** — CONFIRMED the gate stays open by this cycle's `nleps_deflated_solve` read; not closable until a positive bare-Gram-solve site surfaces.

### Suggested next dispatches
- (`harvester`/`lowering-verifier`, **L3 `eigsolve` backfill**) — chain step 3; refines the materialized stub in place; predicted `partial-obstruction` (the eigen-iteration loop does not lift).
- (`harvester`, **`nleps_deflated_solve` adjacent NLEPS interior atoms** — Jacobian-action + eigenvalue-correction) — the remaining NLEPS L1 pieces.
- (`abstractor`, **`nleps_deflated_solve` L1>L0 theme**) + optionally the `apply_nonlinear_pencil` L1>L0 leaf — closes the NLEPS L1>L0 cohort.
- (`abstractor`, **`gram-fold-specialization` + `deflate-composition-lowering` L2>L1 themes**) — carried from cycle-022, not picked this cycle.
- (`lifter`/`lowering-verifier`, **`dot-mutation-rotation` §Sub-pattern D `orthog.hpp:34`→`:35` one-token fix**) — at lines ~160, ~183; mechanical anchor correction.

### Wave-conflict observations
- **`book/src/L1/index.md` shared between report 1 (`nleps_deflated_solve` harvest — Firm-count headline 16→17 + firm-list bullet + dep-map row) and report 2 (motif refresh — §Semantics motif list + §Working-Notes), DISJOINT regions.** Report 2 re-read disk first, confirmed report 1's three landings present, then edited its non-overlapping regions. No reconciliation needed.
- **`book/src/L1-L0/index.md` + `book/src/SUMMARY.md` shared between reports 4 + 5 (the two L1>L0 abstractor themes).** Report 5 re-read disk first, confirmed report 4's firm row + SUMMARY entry, then inserted its own at distinct (upstream) positions. Clean serial handoff.
- **In-cycle implied-component stub + live-link upgrade** — report 3 materialized the `L3/eigsolve.md` stub and, in the same apply, upgraded the L2 §"Lifts to" plain-text forward-reference (the repairer's de-link fallback) back to a live link. The canonical implied-component-stub resolution, preferred over plain-text-defer per the directive; build-safe.

### Integration-tooling friction
- **Machine-crash recovery — finalize resumed from a fully-staged state (NEW; recovery-not-normal-path).** A machine crash interrupted the cycle after all six per-report integrators had completed + staged. Finalize recovered idempotently from the authoritative STAGING.md + working-tree cross-check (6 rows == 6 dispatched ready reports, all `applied`); no per-report re-application or working-tree reconciliation was needed. Validates the split-integrator design's crash-resilience (the staging log + on-disk artifact are sufficient to resume finalize). Batch-6 meta-phase: a clean crash/resume, no tooling gap surfaced — recorded as evidence of the design holding under a real interruption.
- **Carry-forward inline-anchor drift: `orthog.hpp:34`→`:35`** in `book/src/L1-L0/dot-mutation-rotation.md` §Sub-pattern D (lines ~160, ~183; line 34 is the brace `{`, the `return LocalDot(x, y);` is `:35`). Out of the orthogonalize-audit's scope (a different existing file); routed as OQ for a future dot-mutation-rotation pass. Continues the inline-anchor-drift pattern feeding the batch-5-escalated codemap-backed citation-checker ASK (user decision pending).
- **Repaired-CYCLE.md fence handling held for both paths.** Report 4 (`lu-solve-mutation-rotation`) used 4-space-indented inner samples (the cycle-019 fence-truncation guard); report 5 (`nleps-deflated-residual`) kept nested `text` fences intact (firm apparatus fully enclosed, no truncation). Both clean — the cycle-019/020/021 fence guidance continues to hold.

---

## cycle-022 — 2026-05-29T1130Z

(FIRST primary cycle of meta-batch-6 — cycles 022/023/024. **The batch-6 meta-phase fires after the cycle-024 finalize commit** — does NOT fire this cycle. 9 dispatches → 9 applied clean (7 wave-1 + 2 wave-2); staging reconcile clean (9 rows == 9 dispatched ready reports). Build: `cargo make book` exit 0, zero build-repairs, no dead-link errors.)

### Unblocked
- **The L2 `eigsolve` entry** (chain step 2) is now UNBLOCKED — `book/src/L1/eigsolve.md` flipped rough-in (test-coverage-bounded)→firm this cycle (law-confidence re-eval: the laws are positive-source syntactic identities, the cycle-009 convergence-semantics rough-in premise was over-stated). The strict prerequisite chain is now L1-firm (DONE) → **L2 entry (UNBLOCKED, HIGH priority)** → L3 backfill (STAYS BLOCKED until L2 exists; predicted `partial-obstruction`, the eigen-iteration is opaque-library-owned). — OQ `eigsolve-l1-firm-landed-chain-step-1-done-l2-entry-unblocked` / `l3-eigsolve-blocked-on-l1-firm-and-l2-entry` / `l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog`
- **`nleps_deflated_solve` L1** (`nleps.cpp:504-537`) is the next fan-out-ranked NLEPS piece AND the **positive Galerkin source site that would promote `deflate` partly-constructive→firm** (the deflate bare-Galerkin core is currently constructive-from-literature; this site is its positive anchor). Double fan-out: NLEPS interior + deflate promotion. — OQ `nleps-deflated-solve-is-next-fan-out-ordered-nleps-piece-and-l2-deflate-gram-positive-site` / `deflate-l2-partly-constructive-landed-promotion-gates-on-positive-galerkin-site`
- **The L1>L0 lowering themes for the 2 new L1 ops** are now authorable (the L1 anchors are firm): `lu-solve-mutation-rotation`, `nleps-deflated-residual-mutation-rotation`. — OQ `lu-solve-mutation-rotation-l1-l0-theme-needed` / `nleps-deflated-residual-l1-l0-lowering-theme-needed`
- **The L2>L1 lowering themes for the 2 new L2 ops** are now authorable: `gram-fold-specialization` (the double-`dot` loop fusion at `nleps.cpp:524-531`, sibling to the firm `inner-product-fold-specialization` it lifts), `deflate-composition-lowering`. — OQ `gram-l2-l1-lowering-theme-double-dot-loop-fusion` / `deflate-l2-l1-lowering-theme-needed`
- **The `orthogonalize-composition-lowering` three-way-delegation-boundary audit** is ready for a lowering-verifier (the standard `verified_against:` audit + non-duplication confirmation across stage-selection ⟂ Sub-pattern D inner-product unfusing ⟂ orthogonalize-mutation-rotation in-place `w.Add`). — OQ `orthogonalize-composition-lowering-three-way-delegation-boundary-audit`
- **The `lu_solve` §Semantics motif-framing refresh** + candidate 5th "small-dense direct solve" L1 motif is a layer-intro-author follow-up (the count bump 13→14 landed; the motif framing was deferred). The `eigsolve`-firm stale cycle-009 narrative bullet also routes to layer-intro-author for the whole-cohort prose refresh. — OQ `lu-solve-layer-intro-count-refresh-and-fifth-motif` / `eigsolve-firm-stale-cycle-009-narrative-bullet-routes-to-layer-intro-author`

### New dependencies
- `book/src/L1/lu_solve.md` (NEW firm) → leaf (small-dense `k×k` direct solve via pivoted factorization; firm-on-positive-structure); the HIGH-fan-out Gram-coordinate primitive reused by `nleps_deflated_residual` + `deflate` (both this cycle) + future eigensolver/ROM small-dense solves. L1 firm 13→14. — report 2
- `book/src/L1/eigsolve.md` (rough-in (test-coverage-bounded)→firm) → 10 new positive-source law anchors across `slepc.cpp`/`arpack.cpp`; the firm status unblocks the L2 `eigsolve` entry. L1 firm 14→15; L1 rough-in (test-coverage-bounded) cohort 3→2. — report 3
- `book/src/L1/nleps_deflated_residual.md` (NEW firm) → `apply_nonlinear_pencil` (the `k=0` degeneration) + `dot` + `nrm2` + `lu_solve` (the deflation-coords solve); the deflation extension of `apply_nonlinear_pencil`. L1 firm 15→16. — report 4
- `book/src/L1-L0/axpbypcz-mutation-rotation.md` (rough-in→firm) → L0 `vector.{hpp,cpp}` + the 3 corrected callsites (`nleps.cpp:343-344`, `romoperator.cpp:188-189`, `slepc.cpp:1986`); **CLOSES the BLAS-1 L1>L0 floor 8/8**. L1>L0 stays 16 theme files (firm-flip, not add). — report 1
- `book/src/L2/gram.md` (NEW firm) → `inner_product` (the scalar fold it lifts matrix-valued) + `dot` (the per-cell leaf) + `orthogonalize` (the consumer); the all-pairs fold `G = XᴴX → Matrix[k,k]` on the sole literal Gram-build site `nleps.cpp:524-531`. L2 firm 6→7. — report 8 (wave-2)
- `book/src/L2/deflate.md` (NEW partly-constructive) → `gram` + `lu_solve` + `linear_combination` + `dot` (the Schur-form pipeline); firm Schur-form on `nleps.cpp:505-537`, constructive bare-Galerkin core `I − X(XᴴX)⁻¹Xᴴ` from literature + negative-anchor; the promotion gate = a positive Palace Galerkin source site. L2 firm stays 7; L2 partly-constructive tier 0→1; L2 dep-map rough-in cohort 1→0 (drained). — report 9 (wave-2)
- `book/src/L2-L1/orthogonalize-composition-lowering.md` (NEW firm) → firm L2 `orthogonalize` (LHS) + firm L1 `orthogonalize`/`dot`/`axpy` (RHS) + `dot-mutation-rotation` Sub-pattern D (the inner-product realization it CITES rather than re-derives). L2>L1 firm 3→4. — report 6
- `book/src/L3/ksp_solve.md` + `book/src/L2-L1/inner-product-fold-specialization.md` citation-drift sweep (both stay firm, 0 count delta) → 5 distinct inline-anchor re-anchors (`iterative.cpp:464→:463`/`:564→:563`, `operator.cpp:623→:624`/`:632→:634`/`:615-616→:616`); enacts the inner-product theme's own embedded cycle-021 `audit_caveat`. — report 5

### Resolution implications
- `blas1-l1-l0-lowering-theme-gap` / `blas1-l1-l0-lowering-floor-7-of-8-axpbypcz-remains` — **RESOLVED / CLOSED** — `axpbypcz-mutation-rotation` firmed, closing the floor 7/8 → 8/8 (all of `dot`/`scal`/`nrm2`/`assemble-diagonal`/`axpby`/`axpbypcz` firm). The cycle-021 `axpbypcz-mutation-rotation-callsite-correction-and-firm` gated item is enacted. Meta-phase migrates both to the Closed index. — report 1
- `deflate-needs-small-dense-lu-solve-primitive` (cycle-021) — **RESOLVED** — `lu_solve` firmed this cycle, satisfying the HIGH-fan-out blocker; then `gram` firmed + `deflate` landed partly-constructive (all constituents firm except the constructive bare-Galerkin core). Meta-phase closes/migrates. — report 2 / report 8 / report 9
- `eigsolve` rough-in (test-coverage-bounded) — **promoted to firm** — the cycle-009 convergence-semantics rough-in premise was over-stated; the laws are positive-source syntactic identities. **Chain step 1 done**; the L3-prediction (partial-obstruction) is unchanged by the L1 firm. A residual source-read-confirmed-empirically-unwitnessed caveat survives but does NOT gate the firm (test likely out of write-scope). — report 3
- `l3-ksp-solve-citation-drift-463-563-correction` / `inner-product-fold-specialization-operator-cpp-inline-anchor-drift` — **RESOLVED** — both append-only-entry inline-anchor drifts swept in one citation-drift pass (the inner-product sweep enacts the theme's own embedded cycle-021 `audit_caveat`). Meta-phase migrates to Closed. — report 5
- `orthogonalize-composition-lowering-l2-l1-theme` (cycle-019 carry-forward, `:120`) — **RESOLVED** — the now-firm L2 `orthogonalize` anchor (recovered cycle-020) let the theme land firm; it cites Sub-pattern D, discharging the L2>L1-side of `orthogonalize-mutation-rotation-l1-l0-theme-should-cite-dot-subpattern-d` (`:606`; the L1>L0-side residual stays with the un-authored L1>L0 theme). Meta-phase migrates. — report 6
- `l2-index-working-note-staleness-l3-ksp-solve-on-disk` (`:533`) / `L2-layer-intro-refresh-for-named-compositions` (`:123`) / `L2-layer-intro-refresh-for-fold-cohort` (`:149`) — **RESOLVED / DISCHARGED** — the L2 Part-intro refresh dropped the stale "L3 ksp_solve not on disk" clause + discharged the two intro-refresh flags. Meta-phase folds into closed dispositions. — report 7

### Suggested next dispatches
- (`harvester`, L2 `eigsolve` entry) — chain step 2; now unblocked by the L1 firm; HIGH priority — gates the L3 `eigsolve` backfill (predicted partial-obstruction).
- (`harvester`, `nleps_deflated_solve` L1) — the next fan-out-ranked NLEPS piece AND the positive Galerkin source site that promotes `deflate` partly-constructive→firm (double fan-out).
- (`abstractor`, `gram-fold-specialization` L2>L1 + `deflate-composition-lowering` L2>L1) — the L2>L1 lowering themes for the 2 new L2 ops; `gram-fold-specialization` is the sibling of the firm `inner-product-fold-specialization` it lifts.
- (`abstractor`, `lu-solve-mutation-rotation` + `nleps-deflated-residual-mutation-rotation` L1>L0) — the L1>L0 lowering themes for the 2 new L1 ops; the L1 anchors are firm.
- (`lowering-verifier`, `orthogonalize-composition-lowering` three-way-delegation-boundary audit) — the standard `verified_against:` audit + non-duplication confirmation across the three delegation boundaries.
- (`layer-intro-author`, L1 §Semantics motif refresh) — the candidate 5th "small-dense direct solve" L1 motif (from `lu_solve`) + the `eigsolve`-firm stale cycle-009 narrative bullet (whole-cohort prose refresh).

### Wave-conflict observations
- **Intra-cycle load-bearing dependency chains satisfied by serial in-cycle live-link upgrades** — (i) `lu_solve` (wave-1 report 2) firmed before `nleps_deflated_residual` (report 4) consumed it; report 4 was authored plain-text-referencing `lu_solve` (not-yet-firm at author time) and the per-report integrator upgraded all `lu_solve` cross-refs to live links `./lu_solve.md` once it was on disk. (ii) `gram` (wave-2 report 1) firmed before `deflate` (wave-2 report 2) consumed it; the `deflate` integrator upgraded all `gram` cross-refs to live links `./gram.md` + removed every `<!--rough-in-->` marker. Each upgrade re-read the dependency on disk first — build-safe; the canonical in-cycle live-link-upgrade pattern.
- **`book/src/L1/index.md` Firm-count serial reconciliation across reports 2/3/4** — the count took `13→14→15→16`, each per-report integrator reconciling against the THEN-CURRENT on-disk value rather than a stale proposed `old_string` (report 4's proposed `old_string` said "Firm (13)→(14)", stale by two). Clean serial handoff; the per-report Notes explicitly handed the THEN-CURRENT value forward to the next integrator.
- **`book/src/L2/index.md` shared between the wave-1 L2-intro refresh + the wave-2 gram + deflate landings** — disjoint regions (refresh touched prose/working-notes; gram row-substituted its rough-in row + added the 7th firm bullet; deflate row-substituted its rough-in row + added the partly-constructive tier). Each re-read disk fresh at apply. Zero collision.
- **`scaffolding/open-questions.md` append-only multi-report concurrency** — all 9 reports appended OQ intake (RESOLUTION-RECORDs + forward-flags); serial per-report dispatch + append-only discipline serialized with zero collision; per-report integrators do NOT edit existing OQ entries in place (RESOLVED markers are append-only intake for meta-phase Closed-index migration).

### Integration-tooling friction
> **First cycle of the batch-6 (022/023/024) evidence window.** The meta-phase fires after cycle-024 — these items open the window.
- **(a) Transient API 529 mid-dispatch truncation + orchestrator recovery (NEW this cycle).** Both wave-2 harvesters (`gram`, `deflate`) hit a transient API 529 that truncated their FINAL `edit:book/src/L2/index.md` dep-map row-flip block — the producers' chapter bodies were COMPLETE, only the trailing dep-map edit was cut off. The orchestrator surgically completed both truncated blocks (the critics verified the completions FAITHFUL to the chapter content — signature/dependency/status cells all consistent), and the per-report integrators applied them as row-substitutions; the repairers refreshed a stale `lu_solve` reference in the same region. This is a **recovery, not the normal path** — the artifact is correct, but it relied on orchestrator hand-completion rather than the producer re-emitting its own block. **Prevention:** a producer retry/checkpoint on transient API errors (so the truncated turn re-runs and the producer re-emits its final block). Meta-phase: consider whether the harness should retry the truncated turn. Distinct from the cycle-019 fence-truncation defect (that was a producer authoring-OUTSIDE-the-fence error; this is a transport-layer mid-stream cut of a well-formed block).
- **(b) SUMMARY-chapter-registration auto-fix fired twice (gram, deflate) — traceable to (a).** Neither wave-2 harvester's blocks carried a SUMMARY edit (the truncation cut the tail where it would have sat), so the per-report SUMMARY-chapter-registration gate added both `- [gram](./L2/gram.md)` / `- [deflate](./L2/deflate.md)` registrations. The gate worked as designed; flagged because both auto-fixes trace to the same transient-529 truncation (item a), NOT to a producer omission — a producer retry (item a) would have carried the SUMMARY edits the producer intended.
- **(c) Same-cycle plain-text→live-link upgrade recurred (lu_solve, gram) — well-handled, recorded as evidence not friction.** Two reports authored before their in-cycle dependency landed referenced it plain-text; the per-report integrators upgraded to live links once the dependency was on disk (re-reading disk first). This is now a routine multi-wave pattern that the dispatch directive + per-report Notes both anticipate. If it recurs every multi-wave cycle, the meta-phase may codify a one-line "in-cycle live-link upgrade" convention; for now it is friction-free and self-documenting.
- **(d) Inline-anchor drift — the carried cycle-021 L3/inner-product drift was SWEPT this cycle (report 5).** The `l3-ksp-solve-citation-drift-463-563` + `inner-product-fold-specialization-operator-cpp` drifts (carried from cycles 020/021) were enacted in a dedicated citation-drift sweep, with the critic re-verifying each of the 5 corrections via `read_range` + `tools/citecheck/citecheck.py --anchor`. **Note for the batch-6 meta-phase:** `tools/citecheck/` (the batch-5-ASK-enacted mechanical checker) is now in active use by the lifter/critic on this exact class of drift — the first cycle where the dedicated tool backed a drift sweep. Watch whether it reduces the inline-anchor-drift recurrence over 022/023/024 (the batch-5 meta-phase escalated this to recurrence-4; if the tool drives it down, the friction can de-escalate).

---

## cycle-021 — 2026-05-29T0614Z

(THIRD / FINAL primary cycle of meta-batch-5 — cycles 019/020/021. **The batch-5 meta-phase fires immediately AFTER this finalize commit.** This section is the comprehensive batch-5 handoff: it aggregates the cross-batch friction picture the meta-phase aggregates over 019/020/021. 8 dispatches → 7 applied (1 `partially-applied` by design) + 1 BLOCKED-inventory (no book change); staging reconcile clean (8 rows == 8 dispatched). Build: `cargo make book` exit 0, no dead-link errors.)

### Unblocked
- **`axpbypcz-mutation-rotation` callsite-correction + firm** is the cycle-022 closer of the BLAS-1 L1>L0 floor (7/8 → 8/8). The lowering-verifier UNBLOCKED it this cycle (drafted `verified_against:` + drafted firm `## Status`) but GATED enactment per the cycle-012 gated-promotion discipline — 3 confirmed call-site classification errors to correct first (`nleps.cpp:343-344` D→A, `romoperator.cpp:188-189` D→A, `slepc.cpp:1986` γ≠0→γ=0; all critic `read_range`-confirmed). — OQ `axpbypcz-mutation-rotation-callsite-correction-and-firm` / `blas1-l1-l0-lowering-floor-7-of-8-axpbypcz-remains`
- **The `deflate`/`gram` L2 harvester** is surfaced with two rough-in dep-map rows but **firm-promotion BLOCKED on a NEW `lu_solve` L1 dense-solve primitive** (the small-dense `k×k` `fullPivLu().solve` Gram solve — distinct from iterative `ksp_solve` + triangular `trsv`; HIGH fan-out: any small-dense coordinate solve across eigensolver/ROM paths reuses it). The `lu_solve` candidate L1 leaf is the gating dependency before `deflate` can firm. — OQ `deflate-needs-small-dense-lu-solve-primitive` / `nleps-deflation-subspace-projection-combinator-deflate-gram`
- **The `eigsolve` prerequisite chain** is now explicit (this cycle's BLOCKED-inventory product): L1 `eigsolve` rough-in→firm → L2 `eigsolve` entry → THEN L3 `eigsolve` backfill, in **strict order**. The L3 backfill is BLOCKED on missing L1-firm + L2-entry anchors; the linear-EVP has no Palace-authored kernel/driver pair (predicted sequential/partial-obstruction, NOT a clean kernel+driver split like krylov-step/ksp_solve). — OQ `l3-eigsolve-blocked-on-l1-firm-and-l2-entry` / `l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog`
- **The 4 deferred NLEPS L1 pieces** are carried fan-out-ordered: `nleps_deflated_residual` → deflated-solve → Jacobian → eigenvalue-correction. `nleps_deflated_residual` is gated on the L2 `deflate`/`gram` combinator shape settling (the combinator-miner row this cycle IS that shape). — OQ `nleps-deferred-l1-primitives-carry-forward`
- **The append-only firm L3 `ksp_solve` entry's inner-citation drift** (`:464`→`:463` CG, `:564`→`:563` GMRES) is queued for a lifter/lowering-verifier pass (the L3 entry is append-only post-integration; the new L2 entry already uses the corrected lines). — OQ `l3-ksp-solve-citation-drift-463-563-correction`
- **The `orthogonalize-mutation-rotation` L1>L0 theme** (un-authored) should cite `dot-mutation-rotation` Sub-pattern D rather than re-derive the unfused `LocalDot`+`GlobalSum` surface. — OQ `orthogonalize-mutation-rotation-l1-l0-theme-should-cite-dot-subpattern-d`
- **The inner-product-fold `operator.cpp` inline-anchor drift** (`:624`/`:634`/`:616`) — carried from cycle-020; part of the recurring inline-anchor-drift pattern (see Integration-tooling friction). — see cycle-020 §New dependencies

### New dependencies
- `book/src/L1/apply_nonlinear_pencil.md` (firm) → positive site `nleps.cpp:807-821` (`GetResidualNorm`) + 4 corroborating sites + opaque-`A2`-closure type (`nleps.cpp:177-181`); the NEP-interior atom (the `apply_linop`-of-the-NEP-loop). L1 firm cohort 12→13. — report 2
- `book/src/L2/ksp_solve.md` (stub→firm) → `L2/krylov-step` (the folded kernel) + transitively the L1 primitives / L2 named-compositions through krylov-step; L0 anchors CG `iterative.cpp:361-486`, GMRES `:544-705`, base `iterative.hpp:25-115`, driver `ksp.cpp:296-309`. The **non-identity** L2↔L1 (un-collapse) + L2↔L3 (iteration-view un-erasure) relationships. L2 firm cohort 5→6. — report 4
- `book/src/L3-L2/ksp-solve-outer-driver.md` (NEW firm) → firm `L3/ksp_solve` (cycle-020) LHS + firm `L2/ksp_solve` (this cycle) RHS + krylov-step at L2/L3/L4 + the kernel-identity sibling + minres/bicgstab obstruction themes + 6 concept pages + the l4_calculus strawman. The **driver complement** of `krylov-step-body-identity`. L3>L2 firm cohort 1→2 (FIRST L3>L2 growth this batch). — report 5
- `book/src/L4-L3/fgmres-inner-loop-iterate-while-migration.md` (rough-in→firm) → firm `gmres-inner-loop-iterate-while-migration` sibling (cycle-020) + `krylov-step-typed-wrapper-dissolution` rotation shape + `L4/iterate-while`; the firm theme row ADDED to `L4/index.md:44` (was absent from the L4 index entirely). L4>L3 firm cohort 2→3, rough-in cohort 1→0. — report 1
- `book/src/L1-L0/axpby-mutation-rotation.md` (rough-in→firm) → `L1/axpy` (the axpby theme covers the axpy family) + L0 `vector.{hpp,cpp}`/`operator.cpp`/`rap.cpp`; re-audited fenced `verified_against:` (9 anchors line-exact, refreshed to 2026-05-29). L1>L0 firm themes 15→16 (BLAS-1 floor 7/8). — report 3
- `book/src/L2/index.md` dep-map → 2 rough-in rows `gram` (all-pairs `inner_product` fold → `Matrix[k,k]`) + `deflate` (oblique projector `I − X(XᴴX)⁻¹Xᴴ`; over `gram`+`lu_solve`+`linear_combination`+`dot`); both plain-text forward-refs (no live link; `gram.md`/`deflate.md` correctly absent on disk). — report 6
- `book/src/L1-L0/dot-mutation-rotation.md` Sub-pattern D (additive; theme stays firm) → the unfused hook-routed `LocalDot`+`Mpi::GlobalSum` dot surface (first unweighted-observable `dot` use outside the SLEPc-NEP deflation cohort); `book/src/L2-L1/inner-product-fold-specialization.md` gained a bypass-surface cross-link paragraph. — report 7

### Resolution implications
- `fgmres-inner-loop-iterate-while-migration-lifter-candidate` — **RESOLVED** — the 5-batch carry-forward (cycle-010→021) is closed; the FGMRES theme firmed against the firm gmres sibling. The cycle-020 trigger OQ `fgmres-inner-loop-iterate-while-migration-firm-against-gmres-sibling` is enacted. Meta-phase migrates both to the Closed index. — report 1
- `l3-l2-ksp-solve-outer-driver-theme-warranted-gated-on-l2-promotion` (`open-questions.md:356`) — **RESOLVED** — the gate (L2 ksp_solve stub→firm) was satisfied by report 4 this same cycle, then the theme landed (report 5). Answer-link `book/src/L3-L2/ksp-solve-outer-driver.md`. Meta-phase migrates to Closed index. — report 5
- `ksp-solve-l2-promotion-non-identity-substantive-gap` — **RESOLVED** — the L2 ksp_solve outer-driver promotion resolves the maturity-gradient inversion (firm cycle-020 L3 entry was sitting above an L2 stub). — report 4
- `orthog-hpp-localdot-globalsum-unfused-dot-surface` — **RESOLVED** — Sub-pattern D ENACTED this dispatch (load-bearing follow-up applied, not deferred); closes the cycle-020 dot-callers census's flagged "coverage gap of its own" (the second unweighted inner-product surface bypassing `linalg::Dot`). Answer-link `book/src/L1-L0/dot-mutation-rotation.md` Sub-pattern D. Meta-phase migrates to Closed index. — report 7
- `inner-product-conjugate-pair-reorder-caller-classification` (cycle-020) — **RESOLVED** — corroborated by Sub-pattern D + the bypass-surface note completing the dot-caller surface census. Meta-phase migrates/closes. — report 7
- `blas1-l1-l0-lowering-theme-gap` / `blas1-l1-l0-lowering-floor-7-of-8-axpbypcz-remains` — **partially-resolved, NOT closed** — axpby firmed (floor 7/8); axpbypcz remains rough-in (gated cycle-022). The floor OQ does NOT close this cycle — meta-phase keeps it open with the cycle-022 trigger. — report 3

### Suggested next dispatches
- (`lowering-verifier`/`abstractor`, `axpbypcz-mutation-rotation` callsite-correction + firm) — correct the 3 call-site classification errors then firm; **closes the BLAS-1 L1>L0 floor 8/8**. The auditor already drafted the firm body — this is an enact-the-drafted-corrections dispatch.
- (`harvester`, NEW `lu_solve` L1 dense-solve primitive) — the HIGH-fan-out blocker for `deflate`; small-dense `k×k` `fullPivLu().solve`; unblocks the `deflate`/`gram` combinator firm-promotion + reused across eigensolver/ROM small-dense solves.
- (`harvester`, `deflate`/`gram` L2 combinator firm) — gated on `lu_solve` above; decides the `project_oblique`-vs-Schur-modified-NLEPS factoring; AT firm creates `book/src/L2/gram.md`+`deflate.md` and switches the dep-map cells to live links + registers in SUMMARY.
- (`harvester`, `eigsolve` L1 rough-in→firm) — the FIRST step of the strict eigsolve prerequisite chain (then L2 entry, then L3 backfill); the L3 backfill stays BLOCKED until both anchors exist.
- (`harvester`, `nleps_deflated_residual` L1) — the next deferred NLEPS piece; now unblocked by the `deflate`/`gram` L2 shape landing this cycle (the shape it was waiting on).
- (`lifter`/`lowering-verifier`, L3-entry citation-drift sweep) — correct the append-only L3 `ksp_solve` `:464`→`:463`/`:564`→`:563` + the inner-product-fold `operator.cpp` `:624`/`:634`/`:616` drift in one citation-drift pass.
- (`abstractor`, `orthogonalize-composition-lowering` L2>L1 theme) — carry from cycle-019; the now-firm L2 orthogonalize anchor is ready (the orthogonalize-mutation-rotation L1>L0 theme should cite Sub-pattern D).

### Wave-conflict observations
- **Intra-cycle ordering dependency satisfied (the load-bearing chain this cycle)** — report 4 (L2 ksp_solve stub→firm) landed BEFORE report 5 (L3>L2 ksp-solve-outer-driver) by design; the abstractor's RHS reproduces/cites the firm L2 form, and the per-report integrator confirmed `firmness: firm` on disk before applying report 5. Clean serial handoff — the canonical "promote the lower-layer anchor, then author the lowering theme that cites it" pattern.
- **`L2/index.md` dep-map adjacent-append after an in-cycle firm-flip** — report 6 (gram/deflate rough-in rows) re-read disk FRESH and anchored "after the `ksp_solve` row (:53)" which report 4 had just flipped stub→firm; the row is still the table tail, so the append composed cleanly with the in-cycle firm landing. Zero collision.
- **`scaffolding/open-questions.md` append-only multi-report concurrency** — all 8 reports appended OQ intake entries; serial per-report dispatch + append-only discipline serialized them with zero collision. Three reports recorded `...-RESOLVED` append-only intake entries (per-report integrators do NOT edit existing OQ entries in place) for meta-phase Closed-index migration — the fgmres/ksp-solve-outer-driver/orthog-dot-surface closures.

### Integration-tooling friction
> **Comprehensive batch-5 (019/020/021) picture for the meta-phase that fires next.**
- **(a) The cycle-019 orthogonalize fence-truncation defect — RESOLVED cycle-020, guidance HELD cycle-021.** Batch-5's headline defect: the cycle-019 `orthogonalize` L2 harvest authored the firm chapter body OUTSIDE the proposed-changes `edit:` fence, so the cycle-019 integrator landed only the 14-line intro while the dep-map + SUMMARY already said firm (silent body-truncation masked by the dep-map/SUMMARY). Caught + corrected cycle-020 (full-file replacement backfill). TWO skill-candidates filed (`proposed-changes-fence-encloses-full-body-guard`, `verify-intro-firmness-survey-against-on-disk-status-lines`) + OQ `firm-chapter-body-authored-outside-proposed-changes-fenced-block`. **NOTE FOR META: cycle-021's harvesters/abstractors ALL correctly enclosed full bodies inside fences** (apply_nonlinear_pencil CYCLE.md:24-143; ksp_solve full-replace; ksp-solve-outer-driver fence :49-232 with both inner ```text blocks nested+closed; per-report fence-guard PASS on every report) — the guidance held across the batch; no recurrence. Meta-phase should decide whether to promote the skill-candidates to firm skills given the held-clean cycle.
- **(b) Recurring inline-anchor drift across 019/020/021 — now a stable 3-cycle pattern.** Pinpoint citations drift ±1-2 lines while wide enclosing ranges stay correct. Cycle-019: orthogonalize spot-line nits. Cycle-020: dot `:667`→`:668`, scal `nleps.cpp:491`→`:493`, assemble-diagonal `:172`→`:174`, ksp_solve `:100-106`→`:101-108`, inner-product-fold `operator.cpp:623`→`:624`/`:632`→`:634`/`:615-616`→`:616`. Cycle-021: apply_nonlinear_pencil `GetResidualNorm` line-pin + `eps.hpp:69-74` + `:729` role-label; deflate D3 `:663-668`→`:664/:666/:667` + reference `:356-362`→`:354-362`; the carried L3 `ksp_solve` `:464`→`:463`/`:564`→`:563`; the carried inner-product-fold `operator.cpp` drift. **The mechanical codemap-backed citation-checker tool ASK (deferred batch-3/batch-4) is increasingly justified** — the drift is a stable 3-cycle pattern now, and the codemap MCP is in routine use (it could back the checker). Meta-phase should re-evaluate the defer-confirmed status.
- **(c) Sibling-slice citation re-anchor gap.** Cycle-020: `cg.md` drifted the same way as `gmres.md` during the gmres self-rotation (the lifter swept gmres but the sibling cg precedent-ref dangled). Skill-candidate `sibling-slice-citation-reanchor-sweep` filed: when a self-rotation re-anchors one slice, sibling slices carrying the same stale precedent ref should be swept in the same pass.
- **(d) critic-vs-repairer/verifier citation disagreements resolved by independent source re-reads.** Cycle-019: critic raised 3 spot-line nits on orthogonalize-l2; repairer independently `read_range`-re-verified and found the report's ORIGINAL pointers correct (repairer won). Cycle-021: critic-vs-auditor disagreement on the axpbypcz callsite classifications resolved by independent `read_range` (the auditor's 3-error finding confirmed). The cross-check works but **costs an extra independent-re-read each time** — exactly what a shared codemap-backed line-map (item b) would amortize.
- **(e) skill-uptake-survey telemetry pervasive across the batch.** Skills are used in spirit but not named by slug — every cycle-021 report tripped the skill-uptake-survey warning (`verify-citation-range`/`verify-refinement-surface`/`classify-variant-axis` used but unnamed). This continues the batch-3/4 benign-telemetry pattern (escalating-but-no-go). Meta-phase: confirm whether the survey check should be relaxed to telemetry-only (it has never been load-bearing) or whether slug-naming should be enforced.

---

## cycle-020 — 2026-05-29T0605Z

(SECOND primary cycle of meta-batch-5 — cycles 019/020/021; the **batch-5 meta-phase fires after the cycle-021 finalize commit**. Does NOT fire this cycle.)

### Unblocked
- **`fgmres-inner-loop-iterate-while-migration` L4>L3 theme** is now firmable — the gmres sibling rotation landed firm this cycle (the `gmres.md` §L4 v0.7 self-rotation + the L4>L3 theme firm-flip), so the FGMRES sister-theme has a live firm precedent to re-anchor against. A cycle-021 lifter dispatch firms it. — OQ `fgmres-inner-loop-iterate-while-migration-firm-against-gmres-sibling`
- **`L3-L2/ksp-solve-outer-driver` theme** is WARRANTED (the L3 `ksp_solve` outer-driver fold is firm and its L3>L2 rotation is substantive/non-identity) but **gated on the L2 `ksp_solve` stub→firm promotion** — so the immediate unblock is the L2 `ksp_solve` harvest, then the abstractor theme. — OQ `l3-l2-ksp-solve-outer-driver-theme-warranted-gated-on-l2-promotion`
- **The `deflate`/`gram` combinator candidate** is now surfaced with evidence — the recurrent `X[j]ᴴ·` deflation-subspace projection pattern in `nleps.cpp` (`:522,:529,:568`) is a combinator-miner target (`deflate`/`gram` over an invariant-pair basis `X`; pins the conjugation convention once at the combinator boundary). — OQ `nleps-deflation-subspace-projection-combinator-deflate-gram`
- **L2 `ksp_solve` + `incremental-least-squares` stub→firm promotions** are unblocked — both are live-linked L2 stubs (materialized 2026-05-28); the L2 `ksp_solve` promotion is now extra-warranted because the firm L3 `ksp_solve` landed above it (maturity-gradient inversion to resolve). — OQ `ksp-solve-l2-promotion-non-identity-substantive-gap` / `incremental-least-squares-as-future-L2-firstclass-entry`
- **The next L3 inventory item is the `eigsolve` kernel+driver pair** — with the `ksp_solve` L3 constituent of `l3-vocabulary-inventory-gap` now done, `eigsolve` is the next L3 backfill (scope as kernel+driver, mirroring the krylov-step kernel / ksp_solve driver split); `trsv` stays blocked (no L1 anchor). — OQ `l3-vocabulary-inventory-gap-ksp-solve-resolved-and-remaining-inventory`
- **The `orthog.hpp:35` `LocalDot`+`GlobalSum` unweighted-inner-product surface** is a now-identified coverage gap — a SECOND unweighted inner-product surface bypassing `linalg::Dot` (routes through `LocalDot`+`GlobalSum`), out of the Dot-caller census; likely a Condition-5 coverage-gap extension (Gram-Schmidt coefficients generally observable). — OQ `orthog-hpp-localdot-globalsum-unweighted-inner-product-surface`

### New dependencies
- `book/src/L1-L0/dot-mutation-rotation.md` (firm) → `L1/dot` (firm) + L0 `vector.cpp` sites; consumed by the `nrm2 = √∘abs∘dot` sub-pattern A of `nrm2-mutation-rotation`. — report 2
- `book/src/L1-L0/scal-mutation-rotation.md` (firm) → `L1/scal` (firm) + `concepts/scalar-promotion` + sibling `axpby`/`axpbypcz` (rough-in) + `nleps.cpp:486-493` normalize site. — report 3
- `book/src/L1-L0/assemble-diagonal-mutation-rotation.md` (firm) → `L1/assemble-diagonal` (firm) + `apply-linop-mutation-rotation` + L0 rap/hypre/libceed sites; forward (plain-text) deps on `reciprocal`/`elementwise_product` L1 primitives. — report 4
- `book/src/L3/ksp_solve.md` (firm) → `L3/krylov-step` (kernel half, firm) + `L2/ksp_solve` (stub — maturity-gradient inversion) + 8 BLAS-1 L3 siblings + `L3-L2/krylov-step-body-identity` + 8 concept pages; the `L3-L2/ksp-solve-outer-driver` theme is a plain-text forward-ref (gated). — report 5
- `book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md` (firm) → `L4/iterate-while` + `L4/krylov-step` Form A + `L3/krylov-step` + `krylov-step-typed-wrapper-dissolution` + live-link sibling `fgmres-inner-loop-iterate-while-migration` (rough-in); LHS surface = `spec/slices/gmres.md` §L4 v0.7. — report 6
- `book/src/L2-L1/inner-product-fold-specialization.md` gained a `verified_against:` EOF block (15 audit rows, fully-supported) + a `conjugation_caller_inventory:` §Condition 5 block (15 caller sites: 11 invisible + 4 observable, all SLEPc-NEP `nleps.cpp`). — reports 7 + 8
- `book/src/L4/index.md` dep-map (:44 theme row + :53 iterate-while "Lowers to" cell) synced rough-in→firm for the gmres theme (consistency-repair by integrator-finalize). — finalize
- `book/src/L2/index.md` (refreshed) → 5 firm L2 ops + 2 live-linked stubs (`incremental-least-squares`, `ksp_solve`); new §"Vocabulary cohort"; 7-row dep-map. — report 9

### Resolution implications
- `blas1-l1-l0-lowering-theme-gap` — **partially-resolved** — the `dot`/`scal`/`assemble-diagonal` constituents firmed this cycle (joining `nrm2` from cycle-019); the `l1-l0-dot-lowering-asymmetry` constituent is resolved. But `axpby`/`axpbypcz` mutation-rotation themes are STILL rough-in, so the parent is NOT fully closed — meta-phase reconciles the constituent strikes against the axpby/axpbypcz remainder. — reports 2/3/4
- `l3-vocabulary-inventory-gap` — **partially-resolved** — the `ksp_solve` constituent is done (first non-identity L3 backfill); the parent stays open against `trsv` (blocked, no L1 anchor) + `eigsolve` (next, kernel+driver). `gemv` was done-via-`apply_linop`. — report 5
- `inner-product-conjugate-pair-reorder-caller-classification` (:152) — **resolved** — the cross-layer dot-callers census classifies every `linalg::Dot` site (real-projected-invisible vs full-complex-observable); meta-phase migrates/closes. — report 8
- `gmres-inner-loop-iterate-while-migration` (Closed-index :192, `answered-by-rough-in-theme cycle-008`) — **resolved cycle-020** — the migration landed firm (slice §L4 v0.7, option (a) `check_stop_into_carry`); meta-phase updates the Closed-index entry. — report 6
- `inner-product-harvester-formalization-and-conjugation-pinning` (:140) — **confirmed-firm** — the lowering-verifier audit (`fully-supported`, keep firm) ratifies the cycle-019 conjugation pinning; meta-phase enacts the close + plan Now #2 flip. — report 7
- `assemble-diagonal-mutation-rotation` (theme-authoring, :110) — **resolved** — the abstractor L1>L0 dispatch landed firm; meta-phase migrates :110 to the Closed index. — report 4

### Suggested next dispatches
- (`lifter`, `fgmres-inner-loop-iterate-while-migration`) — firm the FGMRES sister-theme against the now-firm gmres sibling (the obvious cycle-021 follow-on).
- (`harvester`, `L2/ksp_solve` stub→firm) — promote the L2 `ksp_solve` outer-driver framing (resolves the maturity-gradient inversion below the firm L3 entry), THEN (`abstractor`, `L3-L2/ksp-solve-outer-driver`) for the substantive L3>L2 rotation.
- (`same-layer-cross-cutter`/`harvester`, `orthog.hpp:35` `LocalDot`+`GlobalSum` unweighted-inner-product surface) — cover the second unweighted inner-product surface the Dot-caller census did not reach.
- (`combinator-miner`, `deflate`/`gram` deflation-subspace candidate) — the recurrent nleps `X[j]ᴴ·` projection pattern; pins the conjugation convention at the combinator boundary.
- (`abstractor`, `axpby`/`axpbypcz` L1>L0 mutation-rotation themes) — close the remaining BLAS-1 L1>L0 lowering floor.
- (`harvester`, NLEPS at L1+) — large multi-cycle carry-forward (sustained context required); (`abstractor`, `orthogonalize-composition-lowering` L2>L1 theme) — carry from cycle-019 (now-firm L2 orthogonalize anchor ready).

### Wave-conflict observations
- **L1-L0/index.md multi-row-append (dot/scal/assemble-diagonal)** — integrations #2/#3/#4 each appended a dep-map row into the BLAS-1+ cohort after the nrm2 row; serial per-report dispatch + re-read-disk-before-edit serialized the three appends cleanly (dot after nrm2, scal inserted after nrm2 / before dot, assemble-diagonal after dot / before the minres/bicgstab obstruction rows). Zero collision; the SUMMARY.md de-stubs (#2/#3 in-place) + new chapter lines (#4/#5) serialized by-slug.
- **Two appends to `inner-product-fold-specialization.md`** — #7 (lowering-verifier) appended a `verified_against:` yaml block at END OF FILE (~:488-553); #8 (cross-layer dot-callers) inserted a `conjugation_caller_inventory:` block into §Condition 5 (~:284-289), ~200 lines ABOVE #7's block. Serial, non-overlapping; the EOF block untouched. Composed cleanly — this is the canonical "two additive appends to the same firm chapter at distinct sections" pattern.
- **Intra-cycle ordering dependency satisfied** — #1 (orthogonalize-backfill) landed FIRST so #9 (L2-refresh) firm-orthogonalize assertions resolve on-disk; #5 (L3/ksp_solve) created the file so #9's L2-index L3-crossref is now upgradeable (left plain-text per dispatch).

### Integration-tooling friction
- **HEADLINE — the cycle-019 orthogonalize fence-truncation defect.** The cycle-019 `orthogonalize` L2 harvest authored the firm chapter body OUTSIDE the report's proposed-changes `edit:` fenced block, so the cycle-019 integrator landed ONLY the 14-line intro; `book/src/L2/orthogonalize.md` was a 14-line intro with NO `## Status` while `L2/index.md:27` dep-map + `SUMMARY.md:41` already said `firm` — a silent body-truncation that the dep-map/SUMMARY masked. Caught cycle-020 by the L2-refresh critic; corrected by the `harvester-orthogonalize-l2-backfill` full-file replacement (staging row #1). TWO skill-candidates filed (`proposed-changes-fence-encloses-full-body-guard` — the full chapter body must be enclosed in the proposed-changes block; `verify-intro-firmness-survey-against-on-disk-status-lines` — the per-report integrator surveys intro-firmness assertions against on-disk `## Status`) + OQ `firm-chapter-body-authored-outside-proposed-changes-fenced-block`. ALL feed the batch-5 meta-phase.
- **Recurring inline-anchor-drift** — now across cycle-019/020 in multiple reports (dot `:667`→`:668`/`:679`→`:678`; scal `nleps.cpp` `:491`→`:493`; assemble-diagonal `AbsMultTranspose` `:172`→`:174` + 3 more; ksp_solve accessor `:100-106`→`:101-108` + 3 more; inner-product-fold `operator.cpp` `:623`→`:624`/`:632`→`:634`/`:615-616`→`:616`). Wide enclosing ranges always correct; pinpoint anchors drift ±1-2 lines. The mechanical **codemap-backed citation-checker tool ASK** (deferred batch-3/4) is increasingly justified — the drift is now a stable 2-cycle pattern.
- **Sibling-slice citation re-anchor gap** — `cg.md` drifted the same way as `gmres.md` (the lifter re-anchored stale `cg.md:215-219` CG-precedent refs to firm `L4/krylov-step` Form A while doing the gmres self-rotation). Skill-candidate `sibling-slice-citation-reanchor-sweep` filed: when a self-rotation re-anchors one slice, sibling slices carrying the same stale precedent ref should be swept in the same pass (otherwise the dangling ref surfaces a cycle or two later).

---

## cycle-019 — 2026-05-29T0810Z

(FIRST primary cycle of meta-batch-5 — cycles 019/020/021; the **batch-5 meta-phase fires after the cycle-021 finalize commit**. Does NOT fire this cycle.)

### Unblocked
- The **BLAS-1 L1>L0 lowering-theme gap** is now partially closed and the rest is unblocked: `nrm2-mutation-rotation` firmed; `dot-mutation-rotation` (:82 stub) + `scal-mutation-rotation` (:84 stub) + `assemble-diagonal-mutation-rotation` are the remaining ready abstractor targets (the firm L1 leaves all exist). — OQ `blas1-l1-l0-lowering-theme-gap` / `assemble-diagonal-mutation-rotation`
- **`orthogonalize-composition-lowering` L2>L1 theme** is now unblocked — the L2 `orthogonalize` operator firmed this cycle, so the lowering theme has a live firm L2 anchor. — OQ `orthogonalize-composition-lowering-l2-l1-theme`
- **`inner-product-fold-specialization` lowering-verifier audit** is now tractable — the theme is firm with a per-line dispatch-rule + re-order-rule + summation-order-table ready for audit. — OQ `inner-product-fold-specialization-lowering-verifier-audit`
- **The L2 Part-intro refresh** is now warranted and unblocked — L2 grew to 5 firm ops this cycle (added the named-composition `orthogonalize` + the fold cohort `inner_product`), so the `L2/index.md` Working-Notes prose + overlay is stale. Two converging refresh flags (`L2-layer-intro-refresh-for-named-compositions` + `L2-layer-intro-refresh-for-fold-cohort`) can fold into one dispatch. — OQ `L2-layer-intro-refresh-for-named-compositions` / `L2-layer-intro-refresh-for-fold-cohort`
- **`assemble-diagonal` downstream** is unblocked: it is now a firm L1 leaf for Jacobi / Chebyshev / block-Jacobi / polynomial-preconditioner diagonal-extraction; the `reciprocal` + `elementwise_product` L1 primitives it forward-references are the next-ranked diagonal-preconditioner-apply backlog items. — OQ `assemble-diagonal-reciprocal-elementwise-product-l1-primitives`

### New dependencies
- `book/src/L2/inner_product.md` (firm) → L1 leaves `dot`/`tdot` (type-API-surface only — zero call sites) / `bilinear-form` (rough-in, M-weighted member) + `apply_linop` + sibling-fold `linear_combination` (do-NOT-merge) + consumer `nrm2`/`matrix-weighted-norm`. — report 7
- `book/src/L2-L1/inner-product-fold-specialization.md` (firm) → `L2/inner_product` (firm, post-#7) + `L1/dot` (firm; `dot`+`tdot`) + `L1/bilinear-form` (rough-in). — report 8
- `book/src/L2/orthogonalize.md` (firm) → L1 leaf `orthogonalize` (firm) + `dot`/`axpy` stage primitives + `krylov-step`/ROM consumers + `inner_product` sibling-fold-constituent. — report 4
- `book/src/L1/assemble-diagonal.md` (firm) → operator/rap/hypre/libceed assembly sites + the two smoother consumers; forward (not-yet-live) deps on `reciprocal` / `elementwise_product` L1 primitives + the `assemble-diagonal-mutation-rotation` L1>L0 theme. — report 2
- `book/src/L1-L0/nrm2-mutation-rotation.md` (firm) → `L1/nrm2` (firm) + L0 `vector.hpp`/`communication.hpp`/`errorindicator.hpp`; forward dep on `dot-mutation-rotation` (stub) for the collective-double recheck. — report 3
- `book/src/L0/fespace-file.md` → forward (plain-text) deps on libceed basis/restriction + quadrature + geometric-factor L0 anchors (folded into OQ `fem-libceed-basis-restriction-l0-anchor`). — report 1

### Resolution implications
- `inner-product-harvester-formalization-and-conjugation-pinning` — **answered/resolved** — the headline plan Now #1/#2 item; conjugation PINNED arg-1 `xᴴ y`, reconciliation against Palace's arg-2 `yᴴ x` documented, Palace verified self-consistent. (Per-report integrator recorded RESOLVED-by-this-entry; meta-phase enacts the close + plan flip.) — report 7
- `inner-product-fold-sibling-candidate` — **resolved** — the sibling-fold boundary (`inner_product` vs `linear_combination`) is drawn two-sided; the fold is firm. — report 7
- `inner-product-fold-specialization-l2-l1-theme` — **resolved** — the forward pointer the #7 harvester opened is closed by the #8 theme. — report 8
- `assemblediagonal-is-not-apply-linop-variant` — **resolved** — the firm `assemble-diagonal` entry is the resolution-anchor (it is a distinct operator-to-data primitive, NOT an `apply_linop` variant). — report 2
- `nrm2-std-abs-defensive-guard-classification` — **resolved** — the `std::abs` is a load-bearing defensive guard (same-sign-strip on the real-projected complex path). — report 3
- `divfree-mult-doc-irrotational-vs-divfree-stale` — **resolved/closure-ready** — the stale-`Mult`-doc tension is dispositioned with the authoritative L0 site named; meta-phase enacts the close + the `priorities.md` flip. — report 5
- `combinator-miner-arity-blind-parametric-family-detection` — **partially-answered** — the cycle-018 parametric-family mode WORKS for fold-families (first live exercise characterized `inner_product`) but has NO positive channel for NON-fold parametric families (Qualification B); the mode-gap is the batch-5 meta-phase resolution target. — report 6

### Suggested next dispatches
- (`abstractor`, `inner-product-fold-specialization lowering-verifier audit + conjugate-pair-reorder caller-classification`) — the theme is firm; audit the per-line dispatch/re-order/summation-order rules + classify every `linalg::Dot` site real-projected-invisible vs full-complex-observable.
- (`abstractor`, `dot-mutation-rotation + scal-mutation-rotation + assemble-diagonal-mutation-rotation L1>L0 themes`) — the BLAS-1 L1>L0 gap; the firm L1 leaves are all ready; the `(stub)` :82/:84 SUMMARY rows are the homes.
- (`abstractor`, `orthogonalize-composition-lowering L2>L1 theme`) — now-firm L2 `orthogonalize` anchor ready.
- (`layer-intro-author`, `L2 Part-intro refresh`) — L2 at 5 firm ops; folds the two converging refresh flags into one dispatch.
- (`harvester/lifter`, `gmres.md §L4 v0.6→v0.7 self-rotation`) — large carry-forward, recurring across batches; would firm the cycle-008 GMRES + cycle-011 FGMRES sister themes.
- (`harvester`, `NLEPS at L1+`) — large multi-cycle carry-forward.
- (`harvester`, `l3-vocabulary-inventory-gap — gemv/trsv L3 cohort growth`) — lower-layer shared-vocabulary weight per the cycle-009 directive.

### Wave-conflict observations
- **`L2/index.md` adjacent-row case** — integration #4 (orthogonalize) ADDED a dep-map row after the `inner_product` rough-in row at `:26` (orthogonalize becomes `:27`); integration #7 (inner_product) then FLIPPED the `inner_product :26` row rough-in→firm by matching its full slug-text, NOT touching the orthogonalize `:27` row. **Auto-resolved by the per-report integrators' serial re-read of disk before each Edit** — the #7 integrator explicitly disambiguated by slug-text and confirmed the `:27` orthogonalize row was untouched.
- **`SUMMARY.md` multi-de-stub case** — five reports (assemble-diagonal, nrm2, orthogonalize, inner_product, inner-product-fold-specialization) each did an IN-PLACE de-stub of their existing `(stub)` line (NOT an append — a second link would be a duplicate-link build error). Serial per-report dispatch + by-slug matching serialized them cleanly with zero collision.
- **Intra-cycle ordering dependency handled correctly** — integration #8 (L2>L1 theme) links to `book/src/L2/inner_product.md` firmed by integration #7; #7 was dispatched before #8 by design so #8's L2 anchor resolves firm at the finalize rebuild — no broken-link wave conflict.

### Integration-tooling friction
- **critic-vs-repairer citation-renumbering disagreement on `orthogonalize-l2`** — the critic raised 3 `citation-validity: warning` spot-line nits (orthogonality assertion 158→156, `m==0` guard `orthog.hpp:62-64`→61, no-normalise `:22`→21); the repairer **independently re-verified** via `read_range`/`search_text` against `reference/palace` and found the report's ORIGINAL pointers correct (the critic read against a 1–2-line-shifted offset). The repairer's re-verify WON; citations stand AS-IS. A **3-of-3-same-direction critic line-offset-drift signal** worth a batch-5 meta-phase friction-window glance IF it recurs (single-cycle, not yet a pattern). Better tooling: a mechanical codemap-backed citation-range checker (the batch-3 meta-phase ASK item, still defer-confirmed) would have given both critic + repairer the same authoritative line-map and avoided the disagreement.
- **`classify-variant-axis` SKILL.md:64-68 `gs_orthog` worked-example staleness** — the orthogonalize-l2 repairer flagged the skill's worked example as stale vs L0 (lists `gemv_basis`/`axpy_scalar`/a `refine_threshold` scalar the actual `OrthogonalizeColumnCGS` does not have) and filed it to `scaffolding/skill-candidates.md`. Meta-phase skill-correction authority.
- **skill-uptake-survey named-skill-by-slug telemetry continues** — reports #4/#7/#8 performed `verify-citation-range`/`verify-rotation-citation`/`classify-variant-axis`/`find-tests-for-region` substance inline but named few/no skill invocations by slug. Pure batch-5 meta-phase telemetry (the verification was evidently done; only the slug back-reference is absent).

---

## Archived — cycles ≤018 (batches 1–4)

Older integrator→planner signal sections (cycle-018 down to cycle-003) were **tail-trimmed 2026-05-29** as a batch-7 meta-phase follow-up (user directive: *per-batch tail-trim* — keep the last ~3 batches in-file, drop older to git history). The planner reads only the most recent ~3 entries, so the trimmed sections are not load-bearing.

Full prior content is preserved in git history — retrieve with:

```
git show 8f14978:scaffolding/integrator-signals.md
```

(`8f14978` = cycle-027 integrator-finalize commit, the last revision carrying cycles 003–018 in-file.)
