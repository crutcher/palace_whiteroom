# cycle-096 integrator staging log

Per-report integration staging. One section per applied report, appended newest LAST (append-only).
Row ORDER is the authoritative apply-order record (NOT the `applied_at` timestamps — advisory only).
integrator-finalize reads this log to reconcile the cycle (rebuild + commit + housekeeping).

---

## D1 — 2026-06-04T223500Z-layer-intro-author-cycle-096-preconditioning-framework
applied_at: 2026-06-04T232000Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/preconditioning-framework.md (create — NEW firm L4 chapter; typed graded-stack frontmatter `rank: firm`, `edges.depends-on: [L4/ksp_solve (caps-the-binding), reference/palace/.../ksp.cpp:276-293 (cites-evidence)]`, concept refs as `reference`)
- book/src/concepts/capability-typing.md (edit — repointed the two slice refs at lines 26 + 55 to ../L4/preconditioning-framework.md §"Capability typing")
- book/src/SUMMARY.md (edit — added the chapter row, alpha between ksp_solve and solve_family in the Outer-driver kind-group; D1 proposed the position, no discretionary insert)
- book/src/L4/index.md (edit — added the dep-map row in the "Outer-driver caps & coordination combinators" table, alpha between the `Outcome` row and the `restart_cycle` row; D1 SOLE owner this cycle)

Gate hits:
- rank-gate (firm-node-promotion): PASS, 0 violations. New node `rank: firm`; its sole ladder `depends-on` dep `L4/ksp_solve` reads `firmness: firm` on disk (book/src/L4/ksp_solve.md:4) → rank 3. Invariant `rank(preconditioning-framework=3) ≤ rank(ksp_solve=3)` holds (firm ≤ firm). The 2nd depends-on edge (ksp.cpp:276-293) is `cites-evidence` to L0 source, not a ladder node, so it does not constrain rank. No depends-on edge to a feature-surface root (the cap relationship is correctly `depends-on` to vocabulary, not `reference`-to-root).
- citecheck (bounds + path-hygiene): 11 ok, 0 failing. No MISS/AMBIG/OOB. Clean.
- SUMMARY.md chapter registration: not-needed (D1 proposed the SUMMARY edit explicitly).
- alpha-position insert: not-needed-as-discretionary (D1 specified both the SUMMARY and index.md alpha slots and they verified correct on disk; no position choice fell to me).
- forward-edge / edge-label / variant-axis / H1-reuse / append-on-missing-slug: none triggered.

Open questions promoted:
- l4-preconditioning-framework-promotion (CLOSED-by-this-chapter; appended a close-note for the meta-phase ledger unify — the line-104 live entry's promotion half is resolved, slice deletion stays deferred to batch-31)
- record-OpBinding-may-need-concept-page (new 2nd-consumer watch item, not actionable now)

Build-relevant: yes (edits touch book/src/*.md — new L4 chapter + 3 existing book pages)

Notes:
- overall_status was canonical `ready` (all 8 critic checks pass); no normalization needed.
- The slice `book/src/spec/slices/cg_preconditioning_framework.md` is NOT deleted this cycle (deferred batch-31 tranche, per planner scope). D1 also deliberately did NOT touch `derived-view-hoisting.md` (disk-confirmed it does not cite the slice) nor `spec/index.md`/SUMMARY slice rows — correct, out of this cycle's scope.
- The critic's non-blocking observation: dep chapter `L4/ksp_solve.md` carries `firmness: firm` but no explicit `rank:` token; rank-gate satisfied via the `firmness: firm → rank 3` mapping (sound mid-campaign during incremental typed-frontmatter rollout). The `ksp_solve` rank-token backfill is graded-stack-campaign work, out of this report's write-scope — flagging for finalize/campaign awareness, not a defect here.
- All four `[old]` anchors matched on-disk text exactly at apply time (re-read disk before each edit). New file did not pre-exist (verified). I was the first per-report integrator in cycle-096 — created STAGING.md.
- Deferred `integrated_at` / `integration_commit` to integrator-finalize per role-spec (not touched).

---

## D2 — 2026-06-04T223500Z-layer-intro-author-cycle-096-resolution-ladder-example-repair
applied_at: 2026-06-04T233500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/methodology/resolution-ladder.md (edit ×3 — worked-example repair: §heading now "cycles 088–095 cascade, completed"; DAG diagram surfaces gram_reduce's second off-diagonal `bilinear-form` leaf; closing paragraphs re-told as the completed two-wave c091/c095 discharge replacing the c094 falsified forward-prediction)

Gate hits:
- rank-gate / forward-edge / edge-label / variant-axis / H1-reuse / append-on-missing-slug / concept_writes / index-placeholder: none triggered. This is a reader-facing NON-AUTHORITATIVE methodology page (banner at :3-18, explicitly outside the subject DAG per :216-220); it carries no `rank:`/`edges:` frontmatter, so all graded-stack typed-edge + subject-DAG gates no-op. Prose-only repair, no status flip authored here (the columns/verbs already flipped at c095).
- citecheck (bounds + path-hygiene): 7 ok, 0 failing. No MISS/AMBIG/OOB. Clean.
- SUMMARY.md chapter registration: not-needed (no new chapter — surgical edits to an existing page).
- bookkeeping: complete.

Open questions promoted:
- bilinear-form-firm-flip-stale-narration-in-meta-owned-methodology-pages — appended a PARTIALLY-RESOLVED progress note (append-only; did NOT edit the line-1333 original, per my append-only OQ authority). resolution-ladder.md half CLOSED by this report; goal-flow.md:260-266 half stays OPEN (meta-phase write-authority, batch-30 refresh). Do NOT close the whole OQ at ledger unify.

Build-relevant: yes (edits touch book/src/methodology/resolution-ladder.md).

Notes:
- overall_status was canonical `ready` (all 8 critic checks pass, clean all-pass report — critic set ready directly, no repairer); no normalization needed.
- All three `[old]` anchors matched on-disk text exactly at apply time (re-read disk this invocation before editing). The §rank-ladder (:32-59) + §well-foundedness-invariant (:61-89) prose and the non-authoritative banner (:3-18) sit outside the edit anchors and are untouched.
- Position 2/5. D1's staging row is present and its edits are byte-disjoint from D2 (D1 touched preconditioning-framework.md / capability-typing.md / SUMMARY.md / L4/index.md — no overlap with methodology/resolution-ladder.md). I did NOT re-narrate any sibling state I did not directly observe; the resolution-ladder.md file as read this invocation carried the c094 falsified worked example at the anchors (no prior in-cycle touch).
- Deferred `integrated_at` / `integration_commit` to integrator-finalize per role-spec (not touched).

---

## D3 — 2026-06-04T223500Z-lifter-cycle-096-o1-lazy-tail-typing
applied_at: 2026-06-04T234500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4-L3/solve-family-map-dissolution.md (edit — prepended typed graded-stack frontmatter to a file that had NO frontmatter: `layer: L4-L3`, `theme:`, `rank: firm`, `edges.depends-on: [L4/solve_family, L4/ksp_solve, L4-L3/ksp-solve-driver-dissolution, L3/ksp_solve]`, `edges.reference: [L4/iterate-while, L4-L3/iterate-while-dissolution, L4-L3/krylov-step-typed-wrapper-dissolution, concepts/state-stratification, concepts/variant-absorption, concepts/sequential-obstruction]`. Pure edge-typing — no §Status prose change, no LHS/RHS body change, no maturity re-judgment. The `---`-delimited block was inserted before the `# solve-family-map-dissolution` heading; heading + following paragraph follow correctly.)

Gate hits:
- rank-gate (firm-node edge-typing): PASS, 0 violations. New typed node `rank: firm`; all 4 `depends-on` endpoints re-read firm on disk THIS invocation: L4/solve_family.md:144 `firm` (c086 firm-on-positive-structure escape), L4/ksp_solve.md:160 `firm` (c048), L4-L3/ksp-solve-driver-dissolution.md:193 `firm` (c048), L3/ksp_solve.md:167 `firm` (c020). Invariant `rank(theme=3) ≤ min(deps=3)` holds (firm ≤ firm). The 6 `reference` edges (3 sibling themes + 3 concept pages) are navigational, constrain no rank.
- citecheck (bounds + path-hygiene): 9 ok, 0 failing. No MISS/AMBIG/OOB. Clean.
- graded-stack-lint --json on landed state: rank_violations: 0 (confirmed; O1 cleared). unreachable: 0.
- SUMMARY.md chapter registration: not-needed (no new chapter — frontmatter prepend to an existing, already-registered theme page).
- forward-edge / edge-label / variant-axis / H1-reuse / append-on-missing-slug / concept_writes / index-placeholder / alpha-position: none triggered (metadata-only edit).
- bookkeeping: complete.

Open questions promoted:
- (none) — the report's §"Open questions / caveats" carries only benign caveats, not new actionable ledger questions: (a) the D4-interaction data-point (parallel-safe, finalize-linter awareness) and (b) the no-broader-L4-L3-sweep scope note (the broader L4-L3 theme-typing is already a planner-recorded deferred batch-31 tranche). Neither warrants an OQ append.

Build-relevant: yes (edits touch book/src/L4-L3/solve-family-map-dissolution.md).

Notes:
- overall_status was canonical `ready` (all 8 critic checks pass, clean all-pass report — critic set ready directly, no repairer); no normalization needed.
- BASELINE-EXCEPTIONS DISCHARGE FOR FINALIZE/META-PHASE: `scaffolding/graded-stack-baseline-exceptions.md` TRACKED-OPEN-1 (O1, `L4/solve_family → L4-L3/solve-family-map-dissolution`) is now **discharged-by-c096-D3**: its promotion condition (type the theme with `rank: firm` + a typed `edges:` block declaring `depends-on: L4/solve_family, L4/ksp_solve, L4-L3/ksp-solve-driver-dissolution`) is satisfied on disk, and the landed-state linter reports rank_violations: 0. Per append-only ledger discipline I did NOT edit the ledger entry; flagging for finalize/meta-phase to move the burn-down "1 tracked" row to "0 tracked".
- D4 interaction (benign, parallel-safe; observed, not assumed): the critic's META non-blocking observation notes D4's `read_status_line` token-priority tool fix may already be on the working-tree linter. Either ordering drives this edge to 0 — confirmed: the linter on the landed state reads rank_violations: 0 regardless. The typed `rank: firm` token clears O1 by construction independent of D4 (it bypasses the prose fallback). No file overlap (D4 is tools/-only).
- Position 3/5. D1 + D2 staging rows are present and their edits are byte-disjoint from D3 (D1: preconditioning-framework.md / capability-typing.md / SUMMARY.md / L4/index.md; D2: methodology/resolution-ladder.md). The solve-family-map-dissolution.md file as read THIS invocation had NO frontmatter (line 1 = the `# solve-family-map-dissolution` heading), confirming no prior in-cycle touch; I re-read it before editing. I narrate only the on-disk state I directly observed.
- Deferred `integrated_at` / `integration_commit` to integrator-finalize per role-spec (not touched).

---

## D4 — 2026-06-04T223500Z-layer-intro-author-cycle-096-read-status-line-fix
applied_at: 2026-06-04T235500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- (none by this integrator — `tools/`-ONLY deliverable; D4 wrote directly to `tools/graded-stack-lint/`, this report RECORDS the writes, it does not propose them through the `book/` channel. Artifact-mutation step is a CONFIRMATION no-op.)

Confirmed-present on disk (D4's direct writes, verified this invocation):
- tools/graded-stack-lint/graded_stack_lint.py — `read_status_line` rewritten to the leading-inline-code-token rule (blob-scan removed); module-level `_STATUS_TOKENS` ordered longest-/most-qualified-first (verified at the file's lines ~315-372: `rough-in (test-coverage-bounded)` ahead of bare `rough-in`, `firm`, `seed`). `derive_rank` precedence (explicit `rank:`/`firmness:`/`status:` frontmatter wins over prose fallback) preserved.
- tools/graded-stack-lint/fixture/book/src/L1/prose_firm_provenance.md — NEW regression fixture node present (862 bytes).
- tools/graded-stack-lint/fixture/book/src/feature/widget.L4.md — present (631 bytes; wires the new node in as a firm→firm `depends-on`).
- tools/graded-stack-lint/README.md — present (8887 bytes; parse-rule paragraph).
- tools/graded-stack-lint/fixture/README.md — present (per dir listing).
- `python3 -m py_compile tools/graded-stack-lint/graded_stack_lint.py` → clean.

Proposed-changes check:
- NO `book/` proposed-changes blocks in CYCLE.md (grep for the edit fence returns none — confirmed tools-only). No `book/src/*.md` touched by D4 or by me. This matches the dispatch's "artifact-mutation step is a no-op/confirmation".

Linter run on landed real-tree state (`python3 tools/graded-stack-lint/graded_stack_lint.py --json`, this invocation):
- rank_violations: **0**
- rank_histogram: **{firm: 192, rough-in: 7, partly-constructive: 3, obstruction: 2, partial-obstruction: 4}**
- promotion_frontier: **10**
- NOTE on firm=192 vs the dispatch-stated 191: I report the value I OBSERVED on disk this invocation. firm is 192, one above the dispatch's 191, because the in-cycle SIBLING landings already on disk at this position (4/5) contribute: D1 created the firm L4 chapter `book/src/L4/preconditioning-framework.md` (`rank: firm`, a brand-new firm node = +1) and D3 typed `book/src/L4-L3/solve-family-map-dissolution.md` with `rank: firm` frontmatter (bin-neutral — it already read firm via the now-fixed prose fallback). The dispatch's 191 was the pre-D1/pre-D3 baseline used to validate D4 in isolation. The CORRECTED-vs-pre-fix shape holds exactly as the report claims: the prose-fallback was masking ~20 untyped-node maturity mis-reads (rough-in/partly-constructive/obstruction false-positives now correctly read firm) — the linter becoming ACCURATE, not a maturity change. I narrate only the on-disk state I directly observed.

Gate hits:
- citecheck (bounds + path-hygiene): 0 ok, 1 failing — `[MISS] graded_stack_lint.py:319-324`. NOT a real artifact-citation defect: this is a bug-LOCATION reference to the project's OWN tool (`tools/graded-stack-lint/graded_stack_lint.py`, the now-removed blob-scan), and citecheck only scans `reference/*` + `book/src` roots, so a `tools/`-self-reference is structurally invisible to it. Benign tool-self-reference, not a Palace/reference citation. Non-blocking; nothing to repair (the line pointer is documentary, the tool file is on disk and the fix is verified in place).
- rank-gate / forward-edge / edge-label / variant-axis / H1-reuse / append-on-missing-slug / concept_writes / index-placeholder / alpha-position / SUMMARY registration: none triggered (tools-only deliverable; no `book/` node authored, no graded-stack typed-node landed by D4, no SUMMARY chapter, no dep-map row).
- bookkeeping: complete.

Open questions promoted:
- graded-stack-lint-read-status-line-token-priority-bug — appended a CLOSED-by-c096-D4 close-note (append-only; did NOT edit the line-1374 original opened cycle-095 D6, per append-only OQ authority). The recommended fix is implemented + fixture-guarded; rank_violations=0 on the real tree. Fully closeable at the meta-phase ledger unify.

Build-relevant: **no** (tools/ + scaffolding/open-questions.md only — no `book/src/*.md` edits by this report; no book rebuild needed for D4).

Notes:
- overall_status was canonical `ready` (all 8 critic checks pass — clean all-pass report, critic set ready directly, no repairer). No normalization needed.
- Position 4/5. D1 + D2 + D3 staging rows are present. D4 is `tools/`-only and is byte-disjoint from all three (D1: preconditioning-framework.md / capability-typing.md / SUMMARY.md / L4/index.md; D2: methodology/resolution-ladder.md; D3: L4-L3/solve-family-map-dissolution.md — all `book/`, zero overlap with `tools/`). The firm=192 histogram value reflects D1+D3 already being on disk (observed directly, not assumed).
- BASELINE-EXCEPTIONS cross-reference (for finalize/meta-phase): D3's row already flagged TRACKED-OPEN-1 (O1) discharged via its `rank: firm` typing. D4 independently clears the SAME O1 from the prose-fallback side (the dep `solve-family-map-dissolution` now reads firm without needing frontmatter) AND clears the other ~12 untyped-tail mis-classifications the typed-frontmatter route would NOT have reached. Either ordering drives rank_violations→0; with both landed, 0 confirmed on disk. D4 is the broader resolution.
- Deferred `integrated_at` / `integration_commit` to integrator-finalize per role-spec (not touched).

---

## D5 — 2026-06-04T223500Z-lifter-cycle-096-mwn-theme-stale-residue
applied_at: 2026-06-05T000500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md (edit ×2 — within-theme stale-residue re-anchor of the OPERATOR's maturity to the post-c091 firm reality: line 5 opening prose `rough-in` → `firm`; line 317 §Speculative-L1-operators clause `(rough-in, test-coverage-bounded)` → `(firm, promoted cycle-091)`. Prose maturity-word swap only — no decomposition / signature / structural change, no new `path:lo-hi` citations. The theme's OWN `## Status` (firm, line ~434, a theme-maturity NOT an operator-maturity claim) deliberately NOT touched.)

Gate hits:
- rank-gate: not-triggered. D5 authors no `rank:`/`edges:` frontmatter and flips NO node status — it only narrates the operator's already-landed c091 firm-flip in consumer prose. No promotion edge to validate. The operator `book/src/L1/matrix-weighted-norm.md` reads firm on disk (`:4 rank: firm`, critic-confirmed via `--anchor`); the theme's own `## Status` (firm) is unchanged. No invariant in scope.
- citecheck (bounds + path-hygiene): 9 ok, 0 failing. No MISS/AMBIG/OOB. Clean (matches the critic's `--scan` run). The two edits introduce no new pinpoints.
- SUMMARY.md chapter registration: not-needed (no new chapter — surgical prose edits to an existing, already-registered theme page).
- forward-edge / edge-label / variant-axis / H1-reuse / append-on-missing-slug / concept_writes / index-placeholder / alpha-position: none triggered (prose maturity-word swap; no new link, dep-map row, signature, or chapter).
- bookkeeping: complete.

Open questions promoted:
- matrix-weighted-norm-mutation-rotation-within-theme-stale-rough-in-residue — appended a RESOLVED-by-c096-D5 close-note (append-only; did NOT edit the original cycle-095 entry at line ~1347, per append-only OQ authority). Both stale sites (:5, :317) re-anchored; fully closeable at the meta-phase ledger unify.
- domain_energy_reduce-377-mwn-stale-rough-in-residue — NEW OQ appended. D5's cross-file whole-book-grep guard surfaced one CLEAN cross-file genuinely-stale operator-maturity assertion at `book/src/L4/domain_energy_reduce.md:377` (`(rough-in (test-coverage-bounded) — ...)`, falsified by the c091 firm-flip), correctly FLAGGED-not-fixed (out of D5's one-theme scope). Routed to a batch-31 land-clean lifter. The two further out-of-scope residues D5 noted (`goal-flow.md:218` → batch-30 meta-phase per planner partition; `L2/index.md:112,121` normalize_B-gate framing → separate normalize-cohort follow-up, judged non-stale-in-claim) are NOT logged as separate OQs (already routed elsewhere).

Build-relevant: yes (edits touch book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md).

Notes:
- overall_status was canonical `ready` (all 8 critic checks pass — clean all-pass report, critic set ready directly, no repairer). No normalization needed.
- ALL 5 REPORTS OF CYCLE-096 ARE NOW STAGED (D1–D5 rows all present, all status `applied`). D5 is the LAST (position 5/5). integrator-finalize can reconcile the full cycle: rebuild (D1/D2/D3/D5 are book-relevant; D4 is tools-only) + commit + housekeeping.
- Position 5/5. D1–D4 staging rows are present and their edits are byte-disjoint from D5: D1 (preconditioning-framework.md / capability-typing.md / SUMMARY.md / L4/index.md); D2 (methodology/resolution-ladder.md); D3 (L4-L3/solve-family-map-dissolution.md); D4 (tools/-only). D5's sole file `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md` was touched by none of them. I re-read both edit sites off disk THIS invocation before editing; both `[old]` anchors matched exactly (no prior in-cycle touch — line 1 was the `# matrix-weighted-norm-mutation-rotation` heading, the two anchors at lines 5 + 317 carried the pre-fix `rough-in` tokens). I narrate only the on-disk state I directly observed.
- FINALIZE/META-PHASE carry-forward: D1, D2, D4 staging rows each flagged baseline-exceptions/ledger-unify items (D1: l4-preconditioning-framework-promotion close + ksp_solve rank-token backfill; D2: bilinear-form-firm-flip OQ partially-resolved, goal-flow.md half stays open; D3: TRACKED-OPEN-1/O1 discharged; D4: read-status-line bug CLOSED + the firm=192 histogram). D5 adds: within-theme mwn OQ closeable; new batch-31 `domain_energy_reduce-377` land-clean OQ.
- Deferred `integrated_at` / `integration_commit` to integrator-finalize per role-spec (not touched).

---
