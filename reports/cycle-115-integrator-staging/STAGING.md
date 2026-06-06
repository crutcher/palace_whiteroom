# cycle-115 integrator staging log

Per-report integration rows, append-only, newest LAST. Row ORDER is the authoritative
apply-order record (NOT the advisory `applied_at` timestamps). integrator-finalize reconciles
the cycle from this log.

---

## 2026-06-06T185234Z-layer-intro-author-residual-untyped-hygiene (D2)
applied_at: 2026-06-06T19:15:41Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/fe_collection.md (frontmatter edit — add `rank: firm` + typed `edges:` [depends-on cites-evidence palace/fem/multigrid.hpp:22-73, lowers-to L1-L0/fe-collection-construction-rotation; reference L1/fe_space])
- book/src/L1-L0/dot-mutation-rotation.md (frontmatter PREPEND — file had NO frontmatter; add `rank: firm` + 6 `cites-evidence` depends-on edges to L0)
- book/src/L1-L0/nrm2-mutation-rotation.md (frontmatter PREPEND — file had NO frontmatter; add `rank: firm` + 4 `cites-evidence` depends-on edges to L0)
- book/src/L1-L0/scal-mutation-rotation.md (frontmatter PREPEND — file had NO frontmatter; add `rank: firm` + 2 `cites-evidence` depends-on edges to L0)

Gate hits:
- rank-well-foundedness: 0 (every new edge firm→firm or firm→rank-terminal-L0; lint rank_violations HELD 0)
- edge-label/prose-mismatch: 0 (critic verified edge-label-fidelity pass; fe_collection `reference→fe_space` backed by §Dependencies "consumed-by relation ... not a dependency")
- YAML round-trip: ok (lint build_graph parsed all 4 frontmatter blocks; the reachable +1 confirms fe_collection's `lowers-to` edge was read)
- SUMMARY-registration: pre-existing (all 4 chapters already registered: SUMMARY.md:220,236,250,253) — no auto-fix needed
- retroactive-budget: 0
- citecheck (--scan): 20 ok, 0 failing — no MISS/AMBIG/OOB

Open questions promoted:
- graded-stack-prose-status-inference-masks-untyped

Build-relevant: yes

Notes:
  Linter delta confirmed EXACTLY as the repair note / dispatch predicted (NOT a discrepancy):
  reachable 132→133 (+1), detritus 127→126 (−1), rank_violations HELD 0, unresolved HELD 0,
  untyped HELD 60, roots HELD 36, typed HELD 295, files HELD 355. The +1 reachable is the
  fe_collection→L1-L0/fe-collection-construction-rotation `lowers-to` depends-on edge RESCUING
  that baseline-detritus theme into the live set (forward mark-sweep from roots). `untyped` does
  NOT drop — the four nodes were never in the untyped-60 list (the linter prose-`## Status`-infers
  their rank), which is exactly the subject of the promoted OQ. FRONTMATTER-ONLY; no prose/body
  edits. Producer reverted to a clean tree per dispatch; applied fresh from the proposed-changes
  [old]/[new] blocks, all four [old] anchors matched on disk. First per-report integrator this
  cycle — created the staging dir + this log. Deferred `integrated_at` to finalize per role-spec.
  Book rebuild deferred to finalize (Build-relevant: yes — touches book/src/*.md, frontmatter only).

---

## 2026-06-06T185234Z-layer-intro-author-named-shape-groups-relocation (D3)
applied_at: 2026-06-06T19:17:43Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/linear_combination.md (PROSE trim — shape-precondition bullet :97-102: removed the general same-shape-contract restatement + the `Tensor[N]`-rank-1 anti-pattern teaching + the past-edit migration note; kept the op's OWN shape fact "congruent over one group `S` of arbitrary/unknown rank; element-local at every position of `S`" + added a parenthetical pointing the general convention to §1.2.1)
- book/src/L3/linear_combination.md (PROSE trim — shape-precondition bullet :47: removed "the name `S` carries the same-shape contract; reuse of `S` … asserts congruence"; kept op's own shape fact + §1.2.1 pointer)
- book/src/L2/linear_combination.md (PROSE trim — shape-precondition bullet :82-86: removed "the name `S` carries the same-shape contract"; KEPT the aligned-fusion-kernels precondition [this op's OWN consequence, rephrased to "This congruence is also the aligned-fusion-kernels precondition"] + §1.2.1 pointer)

Gate hits:
- edge-label/prose-mismatch: 0 (PROSE-ONLY — confirmed no `edges:` frontmatter touched; all three edits operated strictly on body shape-contract bullets, well below frontmatter; critic edge-label-fidelity = pass)
- §1.2.1 anchor-link resolution: 0 broken (verified `[`l4_calculus`](../design/l4_calculus.md)` references intact: L4 = 3 refs incl. the NEW parenthetical, L3 = 2, L2 = 2; all the same existing working relative path; `design/l4_calculus.md` §1.2.1 exists `:62`; no fragment-anchor in the link URLs so nothing to break; no linkcheck2 exposure)
- rank-well-foundedness: 0 (prose-only; lint rank_violations HELD 0)
- citecheck (--scan): 10 ok, 16 failing — ALL 16 are `[AMBIG]` (bare basenames `axpy.md:43` … `nrm2.md:78`) confined to the §"Cohort-wide extent" FINDING section's grep-roll-up listing of Tier-B/C cohort files. NONE backs an applied proposed-change; the 3 edit-block targets + the §1.2.1 home citations all resolve. The producer wrote bare basenames deliberately as a cohort inventory, not as resolvable citations. NON-BLOCKING for the apply (the AMBIG defect class is real per role-spec but here is isolated to informational finding-prose, not a landed citation). Disposition routed to the cohort OQ for the forthcoming semantic-consolidation sweep.

Open questions promoted:
- named-shape-groups-general-rule-restatement-cohort-extent

Build-relevant: yes

Notes:
  DIRECT USER DIRECTIVE (2026-06-06): general named-shape-groups rule should live where shape
  semantics are described (l4_calculus.md §1.2.1/§1.2.2/§4.1), NOT in the linear_combination entries.
  PROSE-ONLY relocation/trim — NO `l4_calculus.md` edit (critic verified §1.2.1/§1.2.2/§4.1 already
  carry the complete rule; nothing added there). All three [old] anchors matched on disk VERBATIM
  (producer reverted to a clean tree per dispatch; applied fresh from the [old]/[new] blocks).
  LINTER DELTA: reachable HELD 133 (prose-only, reachability-neutral — D2's +1 to 133 preserved),
  rank_violations HELD 0, detritus HELD 126, untyped HELD 60, roots HELD 36, typed HELD 295,
  files HELD 355 — exactly as predicted for a prose-only edit. SECOND per-report integrator this
  cycle (D2's row above; I re-read all three target files off disk this invocation — they carried
  the pre-trim general-rule prose, NOT any sibling's edit, consistent with D2 being frontmatter-only
  on a disjoint file set). LEDGER NOTE recorded in the promoted OQ: the cohort-wide sweep (Tier B/C)
  is now governed by the forthcoming semantic-consolidation USER DIRECTIVE (2026-06-06) — the
  meta-phase will handle it, superseding the producer's original "defer Tier C" recommendation.
  Deferred `integrated_at` to finalize per role-spec. Book rebuild deferred to finalize.

---

## 2026-06-06T185234Z-cross-layer-cross-cutter-plateau-probe (D1)
applied_at: 2026-06-06T19:20:14Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- scaffolding/open-questions.md (append-only — added 1 READ-CONTEXT note under the producer's existing cycle-115 D1 plateau-probe section; see "Open questions promoted" below)

Artifact changes: NONE — OBSERVATION-ONLY report. `## Proposed-changes` = "None" (DISPATCH-phase frontier-exhaustion audit; mutates no `book/` artifact). Nothing applied to `book/`.

Gate hits:
- all per-report safety-net gates: 0/N-A (no proposed-changes → no concept_writes / forward-edge / edge-label / H1 / append-on-missing-slug / variant-axis / retroactive-budget / SUMMARY-registration / index-placeholder / implied-component-stub / rank-well-foundedness exposure; observation-only)
- citecheck (--scan): 21 ok, 2 failing — both failing are `[MISS] priorities.md:801` / `priorities.md:848`. These are `scaffolding/priorities.md` INTERNAL cross-references (citecheck searches only under reference/* + book/src, NOT scaffolding/, so the path can't resolve in its roots) — NOT Palace-source citation defects. They back a FINDING (Front-3 build_mesh tracked-deferral provenance), NOT any applied proposed-change (there are none). Verified on disk: scaffolding/priorities.md:801 (candidate-(c) Mesh-wrapper) + :848 (CLEAN-GATE scope-out ruling) resolve VERBATIM at those lines; critic META.md:47 independently confirmed the same anchors. NON-BLOCKING (MISS class is real per role-spec, but here it is a citecheck-search-root artifact over an internal scaffolding ref in informational finding-prose, not a landed citation).

Open questions promoted:
- (producer already appended 4 plateau-probe OQs — CONFIRMED present, lines 1364-1374: `plateau-probe-front1-no-missed-faithful-ground`, `plateau-probe-front2-all-8-frontier-members-genuinely-gated`, `plateau-probe-front3-no-true-coverage-hole`, `plateau-probe-linter-roots-36-vs-columns-40-and-seed-root-in-frontier`)
- READ-CONTEXT note appended by me under the existing section (the batch-37 meta-phase framing: verdict = exhaustion-OF-CURRENT-SCOPE; NEW USER DIRECTIVE 2026-06-06 "post consolidation, all remaining feature fronts opened simultaneously" now fires the demand-gate trigger — verdict stands AND deferred fronts now slated to open; not a terminal stop)

Build-relevant: no (no `book/src/*.md` touched — only scaffolding/open-questions.md, append-only)

Notes:
  THIRD per-report integrator this cycle (D2 + D3 rows above; both `applied`, both frontmatter/prose-only on disjoint book/ files). I did NOT re-read the D2/D3 book targets this invocation — this report touches no book/ artifact, so there is no overlap to reconcile; I observed only scaffolding/open-questions.md + the report + this staging log directly off disk. The load-bearing output of D1 is the NEGATIVE VERDICT (exhaustion CONFIRMED on all 3 fronts: no missed faithful ground, all 8 promotion_frontier members genuinely gated, no true in-scope coverage hole — build_mesh is a tracked candidate-(c) deferral, not a hole), plus 2 benign linter-semantics flags carried into the producer's OQ for the meta-phase: (i) roots=36 = 12 columns × 3 levels reconciles the "40 columns" headline (counting convention); (ii) boundary-mode.{L0,L1,L4} double-counted as ROOT + promotion_frontier inflates the "8" by 3. Critic META.md = all 8 checks pass, overall_status: ready (set by critic on a clean all-pass observation-only report — valid `ready` path, no repairer ran). FOR FINALIZE: the batch-37 meta-phase terminal-state decision should read this verdict together with the READ-CONTEXT note I appended (deferred fronts now slated to open by directive — exhaustion is of-current-scope, not terminal). Deferred `integrated_at` to finalize per role-spec. No book rebuild needed for this report (Build-relevant: no).

---
