# cycle-138 integrator staging log

Per-report integrator landings for cycle-138 (batch-44 CLOSER). Newest LAST, append-only.
Row ORDER is the authoritative apply-order record (NOT the `applied_at` timestamps).

---

## 2026-06-07T233148Z-harvester-l4-krylov-step-cg-solve-worked-example-refresh
applied_at: 2026-06-07T23:40:27Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/krylov-step.md (edit — single [old]→[new] block at lines 192-197, refreshing the stale `cg_solve` Form-B worked-example `iterate_while_with_prev` call to the canonical boot/init/steady/cont arg order + record returns)

Gate hits:
- citecheck bounds + path-hygiene lint: 11 ok, 1 failing — the single failing is [AMBIG] on a bare-basename PROSE ref `krylov-step.md:192-197` (matches L2/L3/L4), a path-hygiene lint NOT a MISS/OOB/bounds defect; all load-bearing pinpoints (proposed-changes block + frontmatter `inputs:`) use the full `book/src/L4/...` path and the edit resolves unambiguously. Cosmetic-only (critic concurred, META §Issues item 1). Non-blocking, unrepairable-at-this-scope (it is the report's own prose, append-only after integration).
- KaTeX $-sigil-fence: satisfied — the edit lands entirely inside the pre-existing ` ```text ` fence (opens at :178, closes at :199); no new $-sigil pseudocode introduced (the `$S` in the untouched `cg_solve` type-signature line at :180 is already fenced).
- edit-applies-cleanly: pass — OLD block matched on-disk verbatim (incl. trailing ` in`), critic-pre-verified.
- no other gates fired (no status promotion, no dep-map/SUMMARY edit, no new slug, no deleted slug, no rank-flip, no forward-edge/variant-axis concerns) — within-body firm→firm fidelity fix.

Open questions promoted:
- iterate-while-with-prev-evidence-prose-stale-cg-call-shape (the secondary stale occurrence at iterate-while-with-prev.md:233, routed for a follow-up single-operator dispatch)

Build-relevant: yes

Notes: Mechanical fidelity fix; `krylov-step` stays `firm`, no dep-map (book/src/L4/index.md) or SUMMARY.md edit (chapter already registered) — confirmed not needed by the report and verified on-disk. This report DISCHARGES OQ `synthesis-l4-krylov-step-worked-example-cg-solve-stale-vs-iterate-while-with-prev-signature` (already present in open-questions.md at :2149) — flagged here for finalize/meta-phase to close/migrate at the ledger-unify step; per-report integrator does not edit/close existing OQs. Deferred `integrated_at` (and `integration_commit`) to finalize per role-spec. First (and per dispatch, only) per-report integrator in cycle-138 — created STAGING.md.

---

## 2026-06-07T233350Z-lowering-verifier-synthesis-rendered-def-vs-l4-correspondence-audit-coordination-drivers-types
applied_at: 2026-06-07T23:52:10Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- (none — audit-class, no book mutation)
- scaffolding/open-questions.md (append — 2 new OQ sections)

Gate hits:
- (none fired) — audit-class report with NO `## Proposed changes` edit blocks (the §Proposed-changes section explicitly states "No mutation to any L4 / feature / concept chapter is proposed"; the two residuals route as gated OQ follow-ups). No book/src edit, no dep-map/SUMMARY edit, no new/deleted slug, no rank-flip, no forward-edge/variant-axis/edge-label surface to gate.
- citecheck bounds + path-hygiene lint: N/A — the report's anchors are book-internal (rendered-def ↔ authoritative-chapter line correspondences), NOT L0 citations; the report itself notes the L0 citecheck adjudicator is N/A here (synthesis defs carry no L0 citations by the link-don't-re-cite convention). No MISS/AMBIG/OOB surface to scan.

Open questions promoted:
- l4-eigsolve-initial-state-vs-initial-eig-state-seed-inconsistency (NEW → abstractor; the upstream L4/eigsolve.md :44+:97 `initial_state` vs `StateT EigState` self-inconsistency)
- synthesis-types-iodata-omits-units-field (NEW → layer-intro-author shell pass; the `IoData` 5-of-6-field `units:Units` completeness add)
- (NOT promoted — already present, INHERITED) the per-library `kind: navigational-container` vs `seed`/`stub` status-token reconciliation: this report's third OQ item is explicitly INHERITED from c137 and is already covered by `synthesis-index-per-library-status-cell-rendered-completeness-convention` (open-questions.md :2137) + the c136 sweep note (:2129); not re-appended to avoid duplication.

Build-relevant: no

Notes: Audit completing the Synthesis correspondence coverage (c137 covered iteration + data-algebra; this covers coordination + drivers + types — whole `# Synthesis` Part now correspondence-audited, modulo the 2 gated non-blocking residuals). This report DISCHARGES OQ `synthesis-correspondence-audit-coverage-coordination-drivers-types-next-pull` (present in open-questions.md as the c137 next-pull candidate) — flagged here for finalize/meta-phase to close/migrate at the ledger-unify step; per-report integrator does not edit/close existing OQs. Deferred `integrated_at` (and `integration_commit`) to finalize per role-spec.

---

## 2026-06-07T233317Z-cross-layer-cross-cutter-maintenance-floor-batch-44-full-hygiene-sweep
applied_at: 2026-06-07T23:53:40Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- (none — audit-class CLEAN-BILL, no book mutation, no scaffolding mutation)

Gate hits:
- (none fired) — audit-class clean-bill with NO `## Proposed changes` section at all. No book/src edit, no dep-map/SUMMARY edit, no new/deleted slug, no rank-flip. The sweep itself verified (independently re-runnable) rank_violations==0, unresolved_depends_on_targets==0, all 6 synthesis chapters `reference`-class-only with 0 blocking edges + correct GC classification (expected_unreachable, not detritus), 3 `realizes-kernel-api` reference-class edges, 3 `#extern` boundaries, 0 `$`-sigil-fence leaks, DIRECTIVE-1 MPI boundary clean (0 frontmatter depends-on onto MPI nodes).
- citecheck bounds + path-hygiene lint: N/A — audit-residue clean-bill; the report's evidence pointers are lint re-runs + on-disk frontmatter line ranges, not L0 citations to scan.

Open questions promoted:
- (none) — clean-bill; the report explicitly states "no OQ append needed" and no baseline-exception ledger edit needed.

Build-relevant: no

Notes: The once-per-batch full-hygiene sweep (batch-44; the per-cycle floor is the integrator-finalize step-5b two-invariant tripwire). This report DISCHARGES OQ `synthesis-edges-next-batch-maintenance-floor-audit` (present in open-questions.md :2129, the c136 deferred Synthesis edge-audit note) — the full Part's edge-typing is now verified `reference`-class with 0 blocking edges + correct GC classification; flagged here for finalize/meta-phase to close/migrate at the ledger-unify step; per-report integrator does not edit/close existing OQs. The report correctly routes the residual per-library status-token-convention reconciliation sub-item to meta-phase/shell-author (out of audit-only scope; already tracked under the OQs noted in the prior row). Deferred `integrated_at` (and `integration_commit`) to finalize per role-spec.

---
