# Cycle-125 integrator staging log (batch-40 MIDDLE)

Per-report integration staging for cycle-125. Rows appended newest-LAST (append-only).
Row ORDER is the authoritative apply-order record (NOT `applied_at` timestamps — advisory only).
integrator-finalize reconciles the cycle from this log.

**Apply ordering this cycle:** D1 (this report — the libCEED substrate firm-flips) MUST land before
D2 (the matrix-free / L2 contraction-chain combinator report), which depends on these firm flips;
D3 lands after. Parent dispatches serially per the plan.

---

## 2026-06-07T124519Z-harvester-substrate-firm-flip (D1)
applied_at: 2026-06-07T13:18:43Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/element_restrict.md (full-file replace: rank rough-in → firm + §Status/laws re-anchored to firm)
- book/src/L1/geom_factor_build.md (full-file replace: rank rough-in → firm + §Status/laws re-anchored to firm)
- book/src/L1/libceed-quadrature-kernel-impl.md (full-file replace: rank rough-in → firm; kernel-IMPL node, well-foundedness lift; realizes-kernel-api stays reference-class)
- book/src/L1/index.md (5 anchor edits: 4a §Firm header tally drain 45→47; 4b kernel-impl bullet rough-in→firm; 4c substrate sub-spine header + element_restrict/geom_factor_build bullets → firm; 4d AMR cross-ref 43→47-member; 4e 3 dep-map rows → firm)
- scaffolding/open-questions.md (append-only: closure note for libceed-substrate-rough-in-to-firm-flip-and-45-to-47-tally-followup)

Gate hits:
- retroactive-budget (per-slice / global): 0
- concept_writes-on-existing-slug: 0
- forward-edge-without-surface: 0
- edge-label / prose mismatch: 0
- H1-reuses-page-heading: 0
- append-on-missing-slug: 0
- variant-axis-missing: 0
- SUMMARY.md chapter-registration auto-fix: 0 (no new chapters; all three flipped files pre-exist + already in SUMMARY.md — refinement-shaped status flips only)
- alphabetical-position-insert: 0 (no new SUMMARY/index-table rows; in-place row + bullet + header replacements only)
- index-placeholder-displacement: 0
- implied-component-stub-materialization: 0
- group-intro-stub-created: 0
- rank-gate (graded-stack well-foundedness): PASS — each firm flip rests on firm deps. kernel-impl: all four `depends-on (composes)` deps firm on disk (basis_apply firm, quad_point_contract firm, element_restrict firm c125 D1, geom_factor_build firm c125 D1) ⇒ rank(impl) ≤ min(deps) = firm. element_restrict + geom_factor_build: sole blocking dep `concepts/element-local-tensor` is `rank: firm` on disk (c124 D5) ⇒ firm-flip warranted. No rank-invariant violation.
- citecheck --scan: 34 ok, 0 failing (no MISS/AMBIG/OOB; DRIFT is anchor-level, not blocked here)

Open questions promoted:
- (none newly opened by the report)
- CLOSED: libceed-substrate-rough-in-to-firm-flip-and-45-to-47-tally-followup (the prescribed c125 Action executed exactly — flip + tally reconcile; closure note appended append-only; original open section left for meta-phase migration/compaction)

Build-relevant: yes (edits touch book/src/L1/*.md)

Notes:
- D1 of cycle-125 (batch-40 MIDDLE). First report of the cycle — created reports/cycle-125-integrator-staging/STAGING.md (this file).
- Tally arithmetic verified on disk: 33 main + 4 FE-assembly + 5 FE-space + 1 Mesh-construction + 4 libCEED-substrate = 47. The §Firm header reads "47 firm grand total" / "= 47" throughout; the multi-era 45/43 count-history prose is drained to a single clean current count of 47.
- The `realizes-kernel-api` edge stayed `reference`-class (NOT depends-on) in the kernel-impl frontmatter; the kept kernel-api obstruction surface `book/src/L1-L0/fe-assemble-libceed-boundary-obstruction.md` is UNTOUCHED and on disk still reads `status: obstruction` / `sub_kind: opaque-library-ownership` (verified on-disk this apply, not assumed). The firm-flip is on the kernel-IMPL node ONLY.
- Three operator files applied as FULL-FILE replacements (the report's edit blocks carry complete file content). Fence parity verified even on all three (kernel-impl: 2 yaml fences after restoring the yaml-block closing fence the full-file write had to carry; element_restrict / geom_factor_build use indented code blocks, 0 fences). The kernel-impl §Status carries no lingering "CANNOT be firm" / stale-rough-in claims (only historical growth-log mentions of the transition remain, correct).
- META overall_status: ready (repairer-set after a cosmetic citation-validity repair: a working-note pointer +2 line-offset 155→153, on concepts/element-local-tensor.md `## Status`, which IS at :153 on disk — verified). Canonical token, no normalization needed.
- Deferred integrated_at to finalize per role-spec (per-report integrator does NOT touch the consumed report's `integrated_at:` / `integration_commit:`).
- SEQUENCING for finalize: D2 (matrix-free / L2 contraction-chain combinator) depends on these firm flips — it must have been applied AFTER this row. D3 after that.

---

## 2026-06-07T124519Z-abstractor-matrix-free-operator-apply (D2)
applied_at: 2026-06-07T13:23:55Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/matrix-free-operator-apply.md (new firm chapter — the L2 constructive-kernel combinator; full-file Write)
- book/src/L2/constructive-kernel-compositions-intro.md (new navigational-container group-intro — new L2 cohort kind; full-file Write)
- book/src/L2/index.md (4 anchor edits: [1] frontmatter `reference` edge → constructive-kernel-compositions-intro; [2] firm-cohort bullet block under **Firm at L2**, before **Partly-constructive**; [3] new `### Constructive-kernel compositions` dep-map sub-section before `## Working Notes`; [4] count line 22→23 firm)
- book/src/SUMMARY.md (new sub-chapter group `Constructive-kernel compositions` + `matrix-free-operator-apply` child, inserted after `Elementwise & gate floors` group / `reciprocal`, before `# L2 > L1` Part)
- scaffolding/open-questions.md (append-only: 4 OQ sections promoted from the report — l2-l1-no-theme-deliberate, role-vs-vocabulary-distinction, mk_matrix_free_operator-l4-placeholder (the c126/batch-41 L4 deferral), amr-rebuild-consumer-forward-note)

Gate hits:
- retroactive-budget (per-slice / global): 0
- concept_writes-on-existing-slug: 0
- forward-edge-without-surface: 0 (all `depends-on`/`reference` targets exist on disk)
- edge-label / prose mismatch: 0
- H1-reuses-page-heading: 0
- append-on-missing-slug: 0
- variant-axis-missing: 0
- SUMMARY.md chapter-registration auto-fix: 0 (report proposed the SUMMARY wiring itself — both new files registered by the report; no auto-fix needed)
- alphabetical-position-insert: 0 (report specified the exact SUMMARY position — new `Constructive-kernel compositions` group placed after the last existing L2 by-kind group `Elementwise & gate floors` per the report's explicit anchor, before `# L2 > L1`; this is a new kind-grouping appended after the existing kind-groups in the transitional flat L2 ordering, NOT a discretionary alpha choice — the position was author-specified, so no `applied-discretionarily`)
- group-intro-stub-created: 0 (report AUTHORED the group-intro `constructive-kernel-compositions-intro.md` — new-SUMMARY-kind-grouping group-intro landed in the SAME apply, as required; no duplicate-file build-break risk, the new group link points at a fresh dedicated file used exactly once)
- index-placeholder-displacement: 0
- implied-component-stub-materialization: 0
- rank-gate (graded-stack well-foundedness): PASS — verified on disk this apply: all four `depends-on (composes)` substrate deps are `rank: firm` (element_restrict firm, geom_factor_build firm — D1 landed first per row above; basis_apply firm, quad_point_contract firm — c124 D3). So `rank(matrix-free-operator-apply = firm = 3) ≤ min(deps) = firm` holds. Issue-1's sequencing precondition (apply D2 after D1) is SATISFIED — D1's row precedes this one and its firm flips are on disk. The `lifts-kernel-impl` edge to L1/libceed-quadrature-kernel-impl is `reference`-class (free/navigational, constrains no rank, carries no liveness) — correct per the kernel-api/impl + identity-in-named-terms discipline.
- citecheck --scan: 18 ok, 0 failing (no MISS/AMBIG/OOB; DRIFT is anchor-level, not blocked here)

Open questions promoted:
- matrix-free-operator-apply-l2-l1-no-theme-deliberate
- matrix-free-operator-apply-role-vs-vocabulary-distinction
- mk_matrix_free_operator-l4-backend-lowering-placeholder (the speculative L4 op deferred to c126/batch-41 — land as roadmap_goal once the L4 backend-lowering feature surface provides the pull)
- matrix-free-operator-apply-amr-rebuild-consumer-forward-note

Build-relevant: yes (edits touch book/src/L2/*.md + SUMMARY.md)

Notes:
- D2 of cycle-125 (batch-40 MIDDLE). Applied AFTER D1 (the substrate firm-flip) per the cycle's apply-ordering — confirmed by reading the four substrate ranks off disk this invocation (all `rank: firm`), so the firm-on-firm well-foundedness cap holds (Issue-1 / rank-invariant warning is RESOLVED by the satisfied serial ordering, NOT downgraded).
- NO L2-L1 theme authored (deliberate): the L2↔L1 rotation is identity-in-named-terms (a degenerate-lowering smell) — resolved as the chapter's in-line §"Downward to L1" note + the `reference`-class `lifts-kernel-impl` frontmatter edge, per the report and the vocabulary-shift redirect. Flagged for lowering-verifier/cross-cutter via the promoted OQ.
- The speculative L4 `mk_matrix_free_operator` is NOT a chapter (no roadmap_goal landed) — held as the promoted OQ for c126/batch-41, exactly as the report scoped.
- Fence parity verified on the new chapter: frontmatter `---` pair (L1/L37) + a single balanced ```yaml block (L253 open / L279 close); the entire firm apparatus is outside any fence (no cycle-019 firm-body-inside-fence truncation). Group-intro is frontmatter-only (0 code fences).
- COUNT NOTE for finalize (pre-existing, not introduced by this apply): the L2/index count line reads a prose-narrative firm count (22→23 this apply, as the report specified) while the dep-map TABLE now has 20 operator rows = 19 firm + 1 partly-constructive (`deflate`). The prose-vs-dep-map-row count gap is PRE-EXISTING (the prose said "22 firm" against 19 firm dep-map rows before this apply); I applied the report's specified 22→23 prose increment + added exactly one firm dep-map row (19→20 rows). Not reconciled here (out of per-report scope — the report specified the prose edit); surfaced for the batch-40 meta-phase / finalize if the prose-count basis wants codifying.
- Deferred integrated_at to finalize per role-spec (per-report integrator does NOT touch the consumed report's `integrated_at:` / `integration_commit:`).
- META overall_status: ready (canonical; repairer-set after the plan-kind-consistency/rank-invariant warning was repaired-via-ordering-instruction). No normalization needed.

---

## 2026-06-07T124519Z-combinator-miner-gmg-hygiene-bundle (D3)
applied_at: 2026-06-07T13:31:00Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/multigrid-relaxation-smoother.md (1 substring edit at :113 — re-point stale `design/l4_calculus.md` §1.2.2 → live `semantics/index.md` §1.2.1; double-correction: path AND section)
- scaffolding/open-questions.md (append-only: 3 resolution notes — vcycle-mining NEGATIVE-close, gmg-smoother-L3-home coverage-record, batch-37-stale-path-sweep RESIDUAL-CLEARED count 1→0 flag-for-meta-close)

Gate hits:
- retroactive-budget (per-slice / global): 0
- concept_writes-on-existing-slug: 0
- forward-edge-without-surface: 0
- edge-label / prose mismatch: 0
- H1-reuses-page-heading: 0
- append-on-missing-slug: 0
- variant-axis-missing: 0
- SUMMARY.md chapter-registration auto-fix: 0 (no new chapters; the edited file pre-exists + is already in SUMMARY.md — a one-line cross-ref hygiene fix only)
- alphabetical-position-insert: 0 (no new SUMMARY/index-table rows)
- index-placeholder-displacement: 0
- implied-component-stub-materialization: 0 (no dangling forward-ref; pick (a) re-points an existing ref to an existing live target; picks (b)/(c) are no-author negative findings)
- group-intro-stub-created: 0
- rank-gate (graded-stack well-foundedness): N/A — no rank flip, no new depends-on edge (pure cross-ref path/section hygiene fix + two negative-finding OQ records)
- citecheck --scan: 25 ok, 0 failing (no MISS/AMBIG/OOB; DRIFT is anchor-level, not blocked here). Independently confirmed the live target on disk: `book/src/semantics/index.md` §1.2.1 (header :73 "Named shape groups", reserve-`Tensor[N]` rule :85); §1.2.2 (:87) is "Operator shapes" — confirming the OLD section number was also wrong, so the double-correction is on-disk-correct.

Open questions promoted (resolution notes, append-only):
- vcycle-level-recursive-combinator-mining-candidate — RESOLVED negative-finding/do-not-mine (single instance gmg.cpp:172; AMG/aux-space speculation refuted; already in-line dispositioned as consumer iteration over firm L2/correction_step; re-open on a 2nd Palace-authored level-recursive cycle, which must NOT fold into the flat-tail fold family)
- gmg-smoother-l3-partial-obstruction-home — RESOLVED already-covered/do-not-author (body = firm L2/correction_step with L3 views L3/chebyshev + L3/jacobi-smoother; outer pc_it loop already homed as L3/chebyshev's partial-obstruction; Hiptmair variant adds no new loop)
- batch-37-era-stale-design-l4-calculus-path-drift-sweep — RESIDUAL CLEARED: `grep -rn 'design/l4_calculus' book/src/` now 0 hits (was 1, this line). Sweep COMPLETE. FLAGGED for batch-40 meta-phase to CLOSE (close/migrate is meta's unify authority per write-partition; per-report integrator records the residual-cleared flag append-only, does not itself close).

Build-relevant: yes (edit touches book/src/L1/multigrid-relaxation-smoother.md)

Notes:
- D3 of cycle-125 (batch-40 MIDDLE), 3rd and final ready report. Applied AFTER D1 + D2 per the cycle's serial apply-ordering (both rows precede this one in the log).
- Only pick (a) mutates `book/`. Picks (b) V-cycle-combinator-do-not-mine and (c) GMG-smoother-L3-home-already-covered are NEGATIVE findings with NO content — recorded as OQ resolution notes only (write-authority partition respected; the report itself authored no `book/` mutation for b/c).
- On-disk verification this invocation (not assumed): pre-apply the line :113 read exactly `... per \`book/src/design/l4_calculus.md\` §1.2.2 "reserve ...`; post-apply it reads `... per \`book/src/semantics/index.md\` §1.2.1 "reserve ...`. The trailing line :114 (`\`Tensor[N]\` for genuinely-flat rank-1 dof-vectors at L1/L0`) is unchanged and accurate.
- Stale-path-drift-sweep COMPLETED across the cycle: c124 D3/D4 fixed the 4 libceed-substrate ops; this c125 D3 fixed the last batch-37-era file. `design/l4_calculus` count in `book/src/` is now 1→0.
- Deferred integrated_at to finalize per role-spec (per-report integrator does NOT touch the consumed report's `integrated_at:` / `integration_commit:`).
- META overall_status: ready (critic-set directly per the all-pass clean-report rule — all 8 checks pass, NO repairer ran). Canonical token, no normalization needed.

---
