# cycle-107 integrator staging log

Per-report integrators append one row each (newest LAST, append-only). The row ORDER is the
authoritative apply-order record; `applied_at` is advisory only. integrator-finalize reads this
log to reconcile the cycle.

---

## 2026-06-05T211311Z-cycle-107-D1-layer-intro-author-bc-cluster-grounding
applied_at: 2026-06-05T213221Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/fe_assemble.md (Edit — added `depends-on (kind: absorbed-post-composition) → L4/eliminate_bc` to the `edges: depends-on:` list; all three pre-existing `reference:` entries PRESERVED)
- book/src/feature/eigenmode.L4.md (Edit — added `depends-on (kind: constrains-eigvec) → L3/divfree-projector` between the `eigsolve composes` and `cites-evidence` edges)
- book/src/L3/divfree-projector.md (Edit — added two `depends-on (kind: uses)` edges → `L1/set_subvector_zero` + `concepts/set_subvector_zero`)
- scaffolding/open-questions.md (append — `bc-divfree-absorbed-clusters-grounded-and-rescued (cycle-107 D1)`: resolves the two carried OQs grounded-and-rescued + records the `L1/divfree-projector` enumeration discrepancy + routes the batch-34 lowering-chain-liveness follow-up)

Gate hits:
- retroactive-budget (per-slice / global): 0
- concept_writes-on-existing-slug: 0 (frontmatter-only edge additions, no concept page creation)
- forward-edge-without-surface: 0 (all 3 edge targets exist on disk; cross-reference-integrity confirmed)
- edge-label/prose-mismatch: 0 (edge kinds honor the cited absorbed-construction relationships; critic edge-label-fidelity = pass)
- H1-reuses-page-heading: 0
- append-on-missing-slug: 0
- variant-axis-missing: 0
- SUMMARY-registration: n/a (no new chapter file created — all three targets are existing chapters)
- alphabetical-position-insert: n/a (no SUMMARY / index-table row inserted)
- index-placeholder-displacement: n/a
- implied-component-stub: n/a (no new component materialized; all edge targets pre-exist)
- graded-resolution rank gate: PASS — all three new `depends-on` edges are firm→firm (`fe_assemble` firm → `eliminate_bc` firm; `eigenmode.L4` firm → `divfree-projector` firm; `divfree-projector` firm → `L1/set_subvector_zero` firm) or firm→untyped-non-node (`concepts/set_subvector_zero`, tolerated exactly as the pre-existing `divfree-projector → L2/divfree-projector` untyped edge). No promotion flips in this report, so the rank-gate assertion `rank(u) ≤ min(deps)` is vacuously satisfied for liveness-only edges. Linter `rank_violations: none` (HELD 0) post-apply.
- citecheck-bounds + path-hygiene: 15 ok, 0 failing (no MISS/AMBIG/OOB) — the repairer's bare-path fix (`graded_stack_lint.py:431` → `tools/graded-stack-lint/graded_stack_lint.py:431`) resolved the earlier path-hygiene nit.

Per-report YAML round-trip: PASS on all three edited files (PyYAML `safe_load` of each frontmatter; edge lists parse cleanly; `fe_assemble` reference list = [L4/index, concepts/black-box-vs-accelerated-kernels, concepts/state-stratification] CONFIRMED INTACT — the repairer's reference-preservation fix held).

Linter rescue measurement (live tree, post-apply, `graded_stack_lint.py --show-inbound` + JSON detritus set-diff):
- rank_violations: 0 → 0 (HELD)
- reachable from roots: 88 → 95 (+7, EXACTLY as predicted)
- detritus: 156 → 149 (−7)
- untyped: 76 → 76 (HELD)
- regressions (nodes that ENTERED detritus): 0 (Python set-diff over the `detritus` JSON list)
- ACTUAL 7-node rescue set (nodes that LEFT detritus): L4/eliminate_bc, concepts/dofset, L3/divfree-projector, L2/divfree-projector, L1/set_subvector_zero, concepts/set_subvector_zero, AND L4-L3/bc-elimination-post-composition-dissolution (the last rode along transitively via eliminate_bc's depends-on).
- ENUMERATION DISCREPANCY (recorded, NOT a defect): the report enumerated `L1/divfree-projector` as one of the 7 rescued nodes, but it did NOT flip — it stays `[garbage?]`. Root cause: `book/src/L2/divfree-projector.md` is a PRE-SCHEME chapter with NO `---` frontmatter / `edges:` block, so the mark-sweep dead-ends at `L2/divfree-projector` (its outbound to `L1/divfree-projector` is prose-only, untyped). `L1/divfree-projector` is an "edge-untypedness artifact" detritus node, not genuine garbage; it flips when the pre-P1 lowering-edge typing lands on `L2/divfree-projector`. `L4-L3/bc-elimination-post-composition-dissolution` flipped in its place, so the headline +7/−7 is exactly correct. The substantive rescue (BC + divfree absorbed clusters grounded, rank held 0, no regressions, fe_assemble references preserved) is sound. Routed into the OQ ledger's batch-34 `lowering-chain-liveness-not-propagated-to-l1-ops` follow-up (same root cause as the L1 BC-op tail).

Open questions promoted:
- bc-divfree-absorbed-clusters-grounded-and-rescued (cycle-107 D1) — consolidated section: resolves `bc-driver-column-eliminate-bc-edge-gap-blocks-dofset-rescue` (c106 D3) + `set-subvector-zero-cluster-reachability-not-rescued-by-reference-backlink` (c106 D4) as grounded-and-rescued; records the `L1/divfree-projector` enumeration discrepancy; routes the batch-34 `lowering-chain-liveness-not-propagated-to-l1-ops` follow-up (L1 BC-op tail + `L1-L0/set-subvector-zero-mutation-rotation` + the L2→L1 divfree untyped gap).

Build-relevant: yes (edits touch book/src/*.md — frontmatter-only, no body/prose, no SUMMARY change; the rebuild should be a no-op for rendered content but is warranted to confirm no breakage).

Notes:
- I am the FIRST per-report integrator this cycle — created reports/cycle-107-integrator-staging/STAGING.md.
- All three `[old]` anchors matched on-disk byte-for-byte at apply time (re-read each file off disk this invocation before editing; did NOT trust an earlier read). The repairer's fix to the `fe_assemble.md` `[old]` block (three-entry `reference:` list) was confirmed present on disk and preserved through the edit.
- deferred integrated_at to finalize per role-spec (did NOT touch the report's `integrated_at`/`integration_commit` frontmatter).
- No book rebuild, no commit, no push, no cycle-end housekeeping — left to integrator-finalize.
- For finalize: re-run the linter post-rebuild to confirm the rescue survives; the +7/−7 delta is the authoritative measure (report's enumeration had the one-node discrepancy above, but the count is correct).

---

## 2026-06-05T211311Z-cycle-107-D2-layer-intro-author-strict-zero-concept-pages
applied_at: 2026-06-05T215600Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched (15 concept pages — each prepended a non-node `reference`-only `edges:` block, NO `rank:`):
- book/src/concepts/build-time-vs-run-time-stratification.md (Edit — 10 reference edges)
- book/src/concepts/capability-typing.md (Edit — 4 reference edges)
- book/src/concepts/chebyshev-iteration.md (Edit — 5 reference edges; anchor `# Chebyshev iteration`)
- book/src/concepts/constructed-operator-factory.md (Edit — 6 reference edges)
- book/src/concepts/constructed-operators.md (Edit — 4 reference edges; anchor `# constructed operators`)
- book/src/concepts/convergence-test.md (Edit — 3 reference edges)
- book/src/concepts/derived-view-hoisting.md (Edit — 5 reference edges; anchor `# Derived-view hoisting`)
- book/src/concepts/eigsolve.md (Edit — 18 reference edges)
- book/src/concepts/erasure-scope.md (Edit — 14 reference edges; anchor `# Concept: erasure-scope`)
- book/src/concepts/ksp_solve.md (Edit — 3 reference edges)
- book/src/concepts/nested-constructed-operator-gate.md (Edit — 12 reference edges)
- book/src/concepts/rotation.md (Edit — 3 reference edges)
- book/src/concepts/solve-monad.md (Edit — 4 reference edges)
- book/src/concepts/solver-as-operator.md (Edit — 6 reference edges)
- book/src/concepts/state-stratification.md (Edit — 4 reference edges)
- scaffolding/open-questions.md (append — `concepts-counter-update-needs-node-rank-and-depends-on-edges (cycle-107 D2)`: the deferred 16th page, ratified→node but rank unguessable on-disk; routed to batch-34)

Gate hits:
- retroactive-budget (per-slice / global): 0
- concept_writes-on-existing-slug: 0 (frontmatter-only edge prepends; no concept page created — all 15 pages pre-exist, only frontmatter added)
- forward-edge-without-surface: 0 (all 45 distinct `reference` targets resolve on-disk; `--strict` reports 0 unresolved targets, exit 0)
- edge-label/prose-mismatch: 0 (all 15 blocks are `reference:`-only per the batch-33-ratified non-node concept-page encoding `graded-stack-scheme.md` §5/§6 — a non-node asserts no blocking dependency; critic edge-label-fidelity = pass)
- H1-reuses-page-heading: 0 (frontmatter prepend leaves the existing `# <title>` H1 untouched)
- append-on-missing-slug: 0
- variant-axis-missing: 0
- SUMMARY-registration: n/a (no new chapter file — all 15 are existing registered concept pages)
- alphabetical-position-insert: n/a (no SUMMARY / index-table row inserted)
- index-placeholder-displacement: n/a
- implied-component-stub: n/a (no new component materialized)
- graded-resolution rank gate: PASS (vacuous) — NO `rank:` and NO `depends-on` edges introduced by any of the 15 blocks (all `reference`-only), so there is no promotion flip to gate; the well-foundedness assertion `rank(u) ≤ min(deps)` has no new edge to check. Linter `rank_violations: 0` (HELD 0) post-apply.
- citecheck-bounds + path-hygiene: 0 ok, 0 failing — the report's CYCLE.md carries NO `file:line` citations (pure-frontmatter typing pass; `citecheck --scan` reports "no citations found"). No MISS/AMBIG/OOB possible.

Per-report YAML round-trip: PASS on all 15 edited files (PyYAML `safe_load` of each prepended frontmatter; every `edges: reference:` list parses as a non-empty list; NO `rank:` key present on any — asserted). Edge counts per file recorded above (sum = 101 edges across 15 pages, 45 distinct targets).

Linter measurement (live tree, post-apply; baseline is post-D1, NOT the report's pre-D1 scratch baseline):
- BASELINE (post-D1 live): `0 rank violation(s), 149 detritus, 76 untyped` (totals: typed 279, reachable 95).
- AFTER (post-D2 live): `0 rank violation(s), 163 detritus, 61 untyped` (totals: typed 294, reachable 95).
- untyped: 76 → 61 (−15, EXACTLY the 15 typed pages — matches the planner's EXPECTED metric).
- typed: 279 → 294 (+15).
- detritus: 149 → 163 (+14, matches EXPECTED +14).
- rank_violations: 0 → 0 (HELD).
- reachable: 95 → 95 (HELD — NO node lost liveness).
- unresolved_depends_on_targets: 0 → 0; `--strict` exit 0.

DETRITUS RISE IS RECLASSIFICATION, NOT REGRESSION (verified by git-stash set-diff of the `detritus` JSON node-sets, BEFORE vs AFTER):
- ENTERED detritus: +14, and they are EXACTLY the 14 newly-typed non-node `concepts/*` pages (build-time-vs-run-time-stratification, capability-typing, chebyshev-iteration, constructed-operator-factory, constructed-operators, convergence-test, derived-view-hoisting, eigsolve, erasure-scope, ksp_solve, nested-constructed-operator-gate, rotation, solver-as-operator, state-stratification). They move from the *untyped-detritus* bucket into the *typed-but-non-node-detritus* bucket — the same `[garbage?]` disposition the pre-existing `concepts/{dot,nrm2,scal,apply_linop,axpy}` reference-only pages already hold (a non-node carries no liveness by construction).
- LEFT detritus: 0 (NO node rescued — and NONE orphaned). The 15th edited page, `concepts/solve-monad`, is NOT in the ENTERED set: it became reachable via an inbound navigational edge (the report's predicted "bonus"), which is why the delta is +14 not +15.
- NO genuine node newly-orphaned: `reachable` held 95→95 and `rank_violations` held 0→0. The detritus rise is purely the untyped→typed-non-node reclassification.

Open questions promoted:
- concepts-counter-update-needs-node-rank-and-depends-on-edges (cycle-107 D2) — the deferred 16th page; ratified→node (sole-definition site of L2 `counter_update`) but its `rank:` is unguessable from the on-disk page (no `## Status` / firm apparatus), so deferred per the planner's most-conservative-reading rule and routed to a batch-34 node-typing dispatch. No live rank/liveness impact (no DAG node carries a typed `depends-on: concepts/counter-update` today).

Deferrals:
- `concepts/counter-update.md` — DELIBERATELY NOT touched (it is a node needing `rank:`, not a non-node `reference`-only page). Confirmed clean in `git status` at apply time. The deferral is captured by the promoted OQ above.

Build-relevant: yes (edits touch book/src/*.md — frontmatter-only, no body/prose, no SUMMARY change; rebuild warranted to confirm no breakage but expected to be a no-op for rendered content).

Notes:
- Position 2 of 2 (FINAL per-report integrator this cycle). D1's row precedes this one; I re-read each of my 15 target files off disk this invocation before editing (did NOT trust an earlier read). All 15 `[old]` anchors matched the verbatim first heading byte-for-byte at apply time.
- D1/D2 write-set disjointness CONFIRMED on disk: D1 touched `L3/divfree-projector.md`, `L4/fe_assemble.md`, `feature/eigenmode.L4.md` (+ `concepts/{dofset,set_subvector_zero}` per its row) — NONE overlap my 15 concept pages. The full `git status --short book/` set is 18 files = my 15 + D1's 3, exactly as expected.
- The report's CYCLE.md linter numbers (156→170 detritus, 76→61 untyped) were a PRE-D1 scratch-tree run; my LIVE post-D1 measurement is 149→163 detritus, 76→61 untyped. The untyped delta (−15) and detritus delta (+14) match the report/planner EXPECTED metrics exactly; the absolute detritus baseline differs only because D1's +0-detritus / −7-rescue landed first (D1 lowered detritus 156→149 before my pass). The EXPECTED-metric semantics hold on the live tree.
- deferred integrated_at to finalize per role-spec (did NOT touch the report's `integrated_at`/`integration_commit` frontmatter).
- No book rebuild, no commit, no push, no cycle-end housekeeping — left to integrator-finalize.

---
