# cycle-103 integrator staging log

Per-report integration rows, append-only, newest LAST. Row ORDER is the authoritative apply-order record (NOT the advisory `applied_at` timestamps). integrator-finalize reads this to reconcile the cycle.

---

## 2026-06-05T071904Z-layer-intro-author-dofset-record-home
applied_at: 2026-06-05T073500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/concepts/dofset.md (created — `DofSet[N]` record-definition home; typed `edges:` frontmatter, rank: firm, kind: record)
- book/src/SUMMARY.md (edit — registered `[DofSet — record definition](./concepts/dofset.md)` alpha-placed between derived-view-hoisting and dot, lines 308-309)
- scaffolding/open-questions.md (append — cycle-103 section: 3 c055-cohort OQs marked RESOLVED, 2 new OQs opened)

Gate hits:
- HARD-gate-new (typed-node): 0 (PASS — new node is fully typed: rank: firm + kind: record + typed edges:; not introduced untyped)
- rank-invariant: 0 (PASS — all blocking `depends-on` edges are `cites-evidence` to L0 source ranges [rank-terminal ground truth], so a `firm` record satisfies rank(u)≤rank(v) vacuously; producer/consumer/L4 edges are `reference`, navigational, correct for a named-by-use record)
- forward-edge-without-surface: 0
- append-on-missing-slug: 0 (file freshly created, not append)
- SUMMARY-registration auto-fix: 0 (report proposed the SUMMARY edit itself; no discretionary registration needed)
- alpha-position-insert: 0 (report specified the alpha position; verified der < dof < dot at SUMMARY.md:308-309)
- citecheck (scan): 14 ok, 0 failing — no MISS/AMBIG/OOB; clean. Re-ran `citecheck.py --scan` on this report's CYCLE.md.
- valid-YAML-frontmatter: PASS — `yaml.safe_load` round-trips the `edges:` block.
- SUMMARY-link-resolves: PASS — `[DofSet — record definition](./concepts/dofset.md)` points at the freshly-created file.

Open questions promoted:
- set-subvector-zero-references-dofset (NEW — reciprocal back-link from set_subvector_zero, routed not applied)
- eliminate-bc-record-definition-prose-now-stale (NEW — stale `DofSet.md` prose at eliminate_bc.md:126, non-link so not build-breaking)
- record-DofSet-needs-definition-home (RESOLVED/CLOSED — page authored)
- dof-set-concept-page (RESOLVED/CLOSED — same page)
- fe-bc-dof-set-and-set-subvector-concept-pages (RESOLVED/CLOSED — decided separate; dofset is home, set_subvector_zero references it)

Build-relevant: yes (touches book/src/concepts/dofset.md + book/src/SUMMARY.md)

Notes: First per-report integrator this cycle — created the staging dir + log. Clean all-pass report (overall_status: ready set by critic directly, no repairer ran — valid path). All edits applied as proposed, no discretionary deviations. Re-read SUMMARY.md anchor on disk before editing (lines 308-309 confirmed). deferred integrated_at to finalize per role-spec (did NOT touch the report's `integrated_at`/`integration_commit` frontmatter). Cycle-id `cycle-103` taken from the parent dispatch prompt, not from report content. Report D4 later this cycle references `concepts/dofset.md` (this file) — hence FIRST dispatch; the file is now on disk for D4's edits to see.

---

## 2026-06-05T071838Z-layer-intro-author-p1-concepts-cluster-a
applied_at: 2026-06-05T074500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/concepts/dot.md (edit — prepend `reference`-only `edges:` frontmatter before H1)
- book/src/concepts/nrm2.md (edit — same)
- book/src/concepts/scal.md (edit — same)
- book/src/concepts/axpy.md (edit — same)
- book/src/concepts/apply_linop.md (edit — same)
- book/src/concepts/apply_BA.md (edit — same; H1 is the long `# Concept: \`apply_BA\` ...` form, matched verbatim)
- book/src/concepts/gemv_basis.md (edit — `reference` → concepts/orthogonalization only; no L1 home exists)
- book/src/concepts/elementwise-product.md (edit — same; H1 `# elementwise_product`)
- book/src/concepts/trsv.md (edit — `reference: []` empty; no L1/trsv home)
- book/src/concepts/two_operator_split.md (edit — same)
- book/src/concepts/set_subvector_zero.md (edit — `reference: []` empty; no L1/set_subvector_zero home)
- book/src/concepts/scalar-promotion.md (edit — same)
- book/src/concepts/complex-from-real-lift.md (edit — same)
- book/src/concepts/tensor-field-lift.md (edit — same; H1 `# Concept: tensor-field-lift`)
- book/src/concepts/variant-absorption.md (edit — same; H1 `# variant absorption`)
- book/src/concepts/finest-level-unwrap.md (edit — same)
- scaffolding/open-questions.md (append — cycle-103 P1-cluster-A section: 2 new OQs opened)

Gate hits:
- valid-YAML-frontmatter: 0 (PASS — all 16 `edges:` blocks round-trip through `yaml.safe_load`, including the two `reference: []` empty-list forms and the trailing-`#`-comment continuations on trsv/set_subvector_zero/gemv_basis)
- dangling-reference-target: 0 (PASS — 22 distinct edge targets, all present on disk; verified L1/{dot,nrm2,scal,axpy,apply_linop,axpby,axpbypcz,elementwise_product}, L2/{krylov-step,inner_product,elementwise_product}, L4/preconditioning-framework, all 12 cited concepts/*; AND confirmed L1/{trsv,set_subvector_zero,gemv_basis} ABSENT so deliberately not referenced)
- operator-entry-mutated: 0 (PASS — pure frontmatter prepend before H1 on each non-node concept page; no operator/theme entry touched, no prose mutated, no body link added/removed → linkcheck2 surface unchanged)
- H1-anchor-match: 0 (PASS — all 16 `[old]` H1 anchors matched verbatim on disk; no pre-existing frontmatter on any page, so `--- ... ---` prepend is collision-free)
- rank-invariant: 0 (PASS — every edge is `reference` [navigational], zero `depends-on`; a non-node `reference`-only block emits no rank/liveness claim, so the well-foundedness invariant is vacuously satisfied)
- forward-edge-without-surface: 0 (PASS — typed-edge pass, no surface claims)
- append-on-missing-slug / SUMMARY-registration auto-fix: 0 (no new files created, no SUMMARY edit needed — all 16 pages already registered)
- citecheck (scan): 14 ok, 0 failing — no MISS/AMBIG/OOB; clean. Re-ran `citecheck.py --scan` on this report's CYCLE.md.

Open questions promoted:
- concept-primitive-without-L1-home-trsv-set_subvector_zero-gemv_basis (NEW — harvester coverage gap; 3 homeless primitives carry concept pages but no L1/<name>.md entry; MEDIUM fan-out)
- concept-non-node-frontmatter-encoding-reference-only-vs-empty (NEW — convention divergence ROUTED FOR META-PHASE: `reference`-only vs strict §5 zero-frontmatter on non-node concept pages; does NOT re-open the already-CLOSED graded-stack-index-and-concept-node-status node-vs-not call)

Build-relevant: yes (16 book/src/concepts/*.md frontmatter prepends — finalize should rebuild)

Notes: Second per-report integrator this cycle (report 2/8). overall_status: ready set by critic directly (all-pass clean, no repairer ran — valid path per role-spec). All 16 prepends applied exactly as proposed; ZERO discretionary deviations. Re-read every target page's line 1 on disk before editing (none had pre-existing frontmatter; the prior D1 dispatch touched concepts/dofset.md + SUMMARY.md, none of which overlap this cluster's 16 pages — confirmed by the staging row above + direct on-disk reads this invocation). The three homeless primitives (trsv/set_subvector_zero/gemv_basis) are NOT a typing defect — the report correctly avoided dangling edges via `reference: []` / sibling-only pointers and routed the coverage gap as an OQ. deferred integrated_at to finalize per role-spec (did NOT touch the report's `integrated_at`/`integration_commit` frontmatter). Cycle-id `cycle-103` taken from the parent dispatch prompt, not report content.

---

## 2026-06-05T071928Z-layer-intro-author-p1-concepts-cluster-b
applied_at: 2026-06-05T075500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/concepts/config-record.md (edit — prepend `rank: firm` + typed `edges:` frontmatter before H1; the ONE node of the 17-page cluster-B set)
- scaffolding/open-questions.md (append — cycle-103 P1-cluster-B subsection: 2 new OQs opened)

Gate hits:
- valid-YAML-frontmatter: 0 (PASS — `yaml.safe_load` round-trips the prepended block; rank=firm, 3 depends-on + 8 reference edges)
- rank-invariant: 0 (PASS — `config-record` is `rank: firm`; its 3 `depends-on` edges are all `kind: cites-evidence` to L0 source ranges [iodata.hpp:31-60, configfile.hpp:57-1026, labels.hpp:18-26] = rank-terminal ground truth, so rank(u)≤rank(v) holds vacuously; the 8 `reference` edges to feature roots + sibling concept are navigational, no rank/liveness constraint — scheme §3 "edge to a feature root is `reference`, never `depends-on`")
- dangling-reference-target: 0 (PASS — all 8 `reference` targets present on disk: concepts/build-time-vs-run-time-stratification + 7 feature columns [lifecycle/electrostatic/magnetostatic/driven/transient/eigenmode/boundary-mode].L4; verified this invocation)
- cites-evidence-bounds: 0 (PASS — all 3 L0 edge targets exist with in-range spans: iodata.hpp 65L, configfile.hpp 1103L, labels.hpp 190L)
- H1-anchor-match: 0 (PASS — `[old]` H1 anchor `# config-record` matched verbatim on disk; no pre-existing frontmatter, so `--- ... ---` prepend is collision-free)
- operator-entry-mutated: 0 (PASS — pure frontmatter prepend before H1; no prose/body link touched → linkcheck2 surface unchanged)
- forward-edge-without-surface: 0 (PASS — typed-edge metadata-backfill pass, no surface claims)
- append-on-missing-slug / SUMMARY-registration auto-fix: 0 (no new file, no SUMMARY edit needed — config-record already registered)
- citecheck (scan): 7 ok, 1 failing — one AMBIG (`main.cpp:259`, a PRE-EXISTING body citation, NOT one of the 3 edge `cites-evidence` targets I applied; the edit's 3 ranges all use full paths and were re-verified by the critic via codemap + by me via on-disk existence/bounds). NOT blocking — the AMBIG sits on a pre-existing body line outside this edit's scope; no MISS/OOB on the applied edge targets.

Open questions promoted:
- config-record-reachability-gap (NEW — HARD; routed to a feature-column-typing tranche, NOT fixed here; config-record is reference-only-linked-by-roots → unreachable garbage until consuming columns add `depends-on`/`kind: uses-record` inbound edges; expected tracked baseline-exception, not a build break)
- graded-stack-concept-node-status-convention (NEW — D2 non-node encoding [strict zero-frontmatter] vs D1/D3 [`reference`-only block] divergence + 2 borderline calls counter-update/chebyshev-iteration; ROUTED for batch-close meta-phase unification; linter-invariant either way)

Build-relevant: yes (touches book/src/concepts/config-record.md — finalize should rebuild)

Notes: Third per-report integrator this cycle (report 3/8). overall_status: ready set by the REPAIRER (accept-and-route on the lone skill-uptake-survey WARNING — no in-place edit; all 7 other critic checks pass) — a valid `ready` path. ONLY artifact edit applied = the single `config-record` frontmatter block, exactly as proposed; ZERO discretionary deviations. The deliberate D2 divergence (16 non-node pages get NO frontmatter, vs D1/D3 `reference`-only blocks) is scheme-permitted (§2d/§6-item-4) and ROUTED for meta-phase — I did NOT add frontmatter to those 16 pages (honoring the dispatch + scheme). Re-read config-record.md line 1 on disk before editing (no pre-existing frontmatter — H1 on line 1, confirmed; the prior D1/cluster-A dispatches touched disjoint pages, none overlapping config-record — confirmed by the two staging rows above + my direct on-disk read this invocation; I make no claim about any sibling landing I did not directly observe). The AMBIG main.cpp:259 is a pre-existing body citation untouched by this edit, not a regression I introduced. deferred integrated_at to finalize per role-spec (did NOT touch the report's `integrated_at`/`integration_commit` frontmatter). Cycle-id `cycle-103` taken from the parent dispatch prompt, not report content.

---

## 2026-06-05T071837Z-layer-intro-author-p1-concepts-cluster-c
applied_at: 2026-06-05T080500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/concepts/gmres.md (edit — prepend `reference`-only `edges:` frontmatter before H1; 7 reference targets, no rank)
- book/src/concepts/givens.md (edit — same; 1 reference target)
- book/src/concepts/givens_apply.md (edit — same; H1 `# \`givens_apply\``; 1 reference target)
- book/src/concepts/givens_generate.md (edit — same; H1 `# \`givens_generate\``; 1 reference target)
- book/src/concepts/plane-rotation-stream.md (edit — same; 5 reference targets)
- book/src/concepts/orthogonalization.md (edit — same; H1 `# concept: orthogonalization`; 9 reference targets)
- book/src/concepts/incremental-least-squares.md (edit — same; 3 reference targets; edge typed to EXISTING concepts/givens, NOT the prose's non-existent givens-rotation slug — prose left untouched, flagged)
- book/src/concepts/first-iteration-unrolling.md (edit — same; 6 reference targets)
- book/src/concepts/sequential-obstruction.md (edit — same; H1 `# Concept: sequential-obstruction`; 7 reference targets)
- book/src/concepts/scope-out-obstruction.md (edit — same; 6 reference targets)
- book/src/concepts/negative-result-slice.md (edit — same; 3 reference targets)
- book/src/concepts/black-box-vs-accelerated-kernels.md (edit — same; 14 reference targets)
- scaffolding/open-questions.md (append — cycle-103 P1-cluster-C section: 1 new OQ opened, prose-drift flag)

Gate hits:
- valid-YAML-frontmatter: 0 (PASS — all 12 `edges:` blocks round-trip through `yaml.safe_load`; verified each parses to `{edges: {reference: [list]}}` this invocation)
- dangling-reference-target: 0 (PASS — 37 distinct edge targets across the 12 blocks, ALL present on disk; verified L_n homes / L1 / lowering / concepts/ siblings this invocation; AND confirmed `concepts/givens-rotation.md` ABSENT + `concepts/givens.md` PRESENT, so the incremental-least-squares repoint introduces no dangling link)
- rank-on-non-node-concept-page: 0 (PASS — NO `rank:` token emitted on any of the 12; all are non-DAG narrative-pointer / obstruction-classification / disposition-test meta-pages [the node-vs-not call is CLOSED-RESOLVED-BY-P1], so reference-only-no-rank is correct; per the repairer integrator note I did NOT add rank tokens)
- rank-invariant: 0 (PASS — every edge is `reference` [navigational], zero `depends-on`; a non-node reference-only block emits no rank/liveness claim → well-foundedness invariant vacuously satisfied)
- operator-entry-mutated / claim-mutation: 0 (PASS — pure frontmatter prepend before H1 on each non-node concept page; no operator/theme entry, no prose mutated, no body link added/removed → linkcheck2 surface unchanged; per the repairer integrator note I applied the 12 edges blocks AS-IS, did NOT strip them)
- H1-anchor-match: 0 (PASS — all 12 `[old]` H1 anchors matched verbatim on disk via Read; no pre-existing frontmatter on any page, so the `--- ... ---` prepend is collision-free)
- forward-edge-without-surface: 0 (PASS — typed-edge metadata-backfill pass, no surface claims)
- append-on-missing-slug / SUMMARY-registration auto-fix: 0 (no new files created, no SUMMARY edit needed — all 12 pages already registered)
- citecheck (scan): 0 citations found (no source citations in this typed-edge CYCLE.md — expected; the load-bearing edge targets were verified by direct on-disk existence checks above). No MISS/AMBIG/OOB.

Open questions promoted:
- incremental-least-squares-prose-names-nonexistent-givens-rotation-slug (NEW — PRE-EXISTING prose/naming drift at incremental-least-squares.md:35 names a non-existent `givens-rotation` slug; the edge was correctly typed to existing concepts/givens, prose left untouched; non-link drift so NOT build-breaking; routed for a future harvester/cross-cutter touch; LOW fan-out)
- (convention divergence NOT re-opened — the scheme-vs-dispatch `edges:`-on-non-node-concept-page question this report flags is ALREADY routed to batch-close meta-phase under `concept-non-node-frontmatter-encoding-reference-only-vs-empty` + `graded-stack-concept-node-status-convention`, both of which explicitly name the D1/D3 `reference`-only-block encoding this D3 dispatch applied; no duplicate OQ created)

Build-relevant: yes (12 book/src/concepts/*.md frontmatter prepends — finalize should rebuild)

Notes: Fourth per-report integrator this cycle (report 4/8). overall_status: ready set by the REPAIRER (accept-and-route on the lone edge-label-fidelity WARNING — no in-place edit; all 7 other critic checks pass) — a valid `ready` path. All 12 prepends applied EXACTLY as proposed; ZERO discretionary deviations. Per the repairer's explicit integrator note I applied the 12 `edges:` blocks AS-IS — did NOT strip them and did NOT add `rank:` tokens (the concept-page encoding convention is meta-phase-owned and ratified at batch close). Re-read every target page's line 1 on disk (via Read) before editing — none had pre-existing frontmatter, all 12 H1 anchors matched verbatim. The prior D1 (dofset) / cluster-A / cluster-B dispatches touched disjoint pages (dofset.md + SUMMARY.md; 16 cluster-A concept pages; config-record.md) — none overlapping this cluster-C set of 12; I observed this directly via the three staging rows above + my own on-disk reads this invocation, and make no claim about any sibling landing I did not directly observe. The incremental-least-squares→concepts/givens repoint is build-safe (givens-rotation absent, givens present — verified on disk this invocation). deferred integrated_at to finalize per role-spec (did NOT touch the report's `integrated_at`/`integration_commit` frontmatter). Cycle-id `cycle-103` taken from the parent dispatch prompt, not report content.

---

## 2026-06-05T072504Z-layer-intro-author-p1-concepts-infra-reconcile
applied_at: 2026-06-05T081500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/concepts/index.md (edit — prepend `kind: navigational-container` + `reference`-only `edges:` block [53 concept-page targets, NO `rank:`] before H1; AND insert `| [dofset](./dofset.md) | record |` member-table row alpha between derived-view-hoisting and dot)
- book/src/concepts/dependency-map.md (edit — prepend `kind: navigational-container` + `reference: [concepts/index]` frontmatter before H1; re-type the edge-convention prose [solid-`depends-on` → dashed-`ref` posture]; re-type all 3 Mermaid sub-graphs `-->` → `-.->|ref|` [c101 over-asserted blocking dependence among non-node pages]; add the `dofset` record node + its 3 edges [state-stratification, build-time-vs-run-time-stratification, eliminate-bc-consumers alias] + the config-record build-time edge; update the records paragraph to add dofset + the record-node-vs-meta-page typing + six-pending-record note)
- scaffolding/open-questions.md (append — cycle-103 D4 infra-reconcile subsection: 4 new OQs + 1 closure note)

Gate hits:
- retroactive-budget: 0 (no retroactive edits to prior reports)
- rank-invariant (graded-stack add-9): 0 (PASS — both infra pages carry NO `rank:` and emit ZERO `depends-on` edges [reference-only navigational containers]; the well-foundedness invariant `rank(u)≤min(deps)` is vacuously satisfied — no rank node, no blocking edge)
- forward-edge-without-surface: 0 (PASS — no `depends-on` / forward-edge claim on either page; typed-edge container reconciliation only)
- edge-label/prose mismatch: 0 (PASS — every re-typed Mermaid edge is `-.->|ref|` and the prose for each sub-graph states "all edges below are `reference`"; consistent)
- concept_writes on existing slug: 0 (N/A — no new concept page authored; `dofset.md` was CREATED by D7 [row 1 above], D4 only references it)
- H1-reuses-page-heading / H1-anchor-match: 0 (PASS — both edits are YAML frontmatter PREPEND above the existing single H1; no new H1 introduced; both `[old]` H1 anchors [`# Concepts — Shared Library`, `# Concept dependency map`] matched verbatim on disk, no pre-existing frontmatter so `--- ... ---` prepend is collision-free)
- append-on-missing-slug / SUMMARY-registration auto-fix: 0 (no new file created; D7 owns dofset's SUMMARY.md wiring per its staging row above — NOT duplicated here; D4 adds only the index.md member-table row, which is the index's OWN member list, distinct surface)
- variant-axis-missing: 0 (N/A — not a multi-variant operator)
- cross-reference-integrity (LOAD-BEARING this kind): 0 (PASS — verified on disk THIS invocation: all 53 `concepts/<slug>` `reference:` targets in index.md resolve to on-disk `book/src/concepts/<slug>.md` [54 pages on disk incl. index]; `dofset.md` confirmed present (10447 bytes, created by D7); every Mermaid node in the re-derived dependency-map resolves to an on-disk concept page EXCEPT the two prose-documented alias labels `krylov-step-record`→krylov and `eliminate-bc-consumers`→L1/L4 BC verb-pair [not file targets, explicitly stated in prose]; the `[dofset](./dofset.md)` member-table link + prose link both resolve since D7 landed first)
- citecheck (scan): 0 citations found — `python3 tools/citecheck/citecheck.py --scan <CYCLE.md> --quiet` reports "no citations found" (expected for a typed-edge / derived-view reconciliation report; the load-bearing edge targets were verified by direct on-disk existence checks above, not by citation ranges). No MISS/AMBIG/OOB. exit 0.
- valid-YAML-frontmatter: PASS — `yaml.safe_load` round-trips both prepended blocks (index.md: kind=navigational-container, no `rank`, reference list of 53; dependency-map.md: kind=navigational-container, no `rank`, reference list of 1).

Open questions promoted:
- dependency-map-not-recognized-outside-dag-by-linter (NEW — ROUTE TO META-PHASE/tools; `is_likely_outside_dag` does not match `concepts/dependency-map`, so once typed it reads as cosmetic detritus; fix = honor `kind: navigational-container`; same class as D5's 23 group-intros)
- graded-stack-six-record-concept-pages-need-frontmatter (NEW — follow-on record-page typing tranche; krylov/op-params/sim-state/step-outputs/prev-carry/solve-result still carry no on-disk frontmatter; node-status settled, frontmatter pending)
- graded-stack-concept-nonnode-edges-block-d1d3-vs-d2 (NEW — D4-vantage view, UNIFIED with cluster-A `concept-non-node-frontmatter-encoding-reference-only-vs-empty` + cluster-B `graded-stack-concept-node-status-convention`; no separate meta-phase ask; D4's reconciliation is invariant to the choice)
- dofset-reachability-needs-uses-record-edge (NEW — HARD; sibling of config-record-reachability-gap; dofset is reference-only-linked → unreachable garbage until a consumer adds inbound `depends-on (kind: uses-record)`; feature-column/BC-cohort tranche)
- graded-stack-index-and-concept-node-status (CLOSURE NOTE — DECIDED for the infra pair aligned with D5: both index + dependency-map are navigational containers, no `rank:`, reference-only; closes the `concepts/index` alignment point D5 flagged)

Build-relevant: yes (touches book/src/concepts/index.md + book/src/concepts/dependency-map.md — finalize should rebuild; both edits are frontmatter-prepend + table-row + Mermaid-text, all mdBook/linkcheck2-safe)

Notes: Fifth per-report integrator this cycle (report 5/8). overall_status: ready set by the CRITIC directly (all-8-pass clean, no repairer ran — valid path per role-spec). Both edits applied EXACTLY as proposed; ZERO discretionary deviations (no SUMMARY auto-fix, no alpha-position discretion — the report specified the dofset member-row alpha position [der < dof < dot], verified on disk). Re-read both target files on disk THIS invocation before editing — neither had pre-existing frontmatter (H1 on line 1 of each), both `[old]` anchors matched verbatim. PREREQUISITE CONFIRMED ON DISK (not assumed): `book/src/concepts/dofset.md` exists [10447 bytes] — created by D7 (row 1 above, status: applied); this is what makes the `[dofset](./dofset.md)` member-table link + dependency-map prose link resolve, so D4's edits are linkcheck2-safe. The c101 dependency-map drew non-node-page relations as solid `-->` (over-asserting blocking dependence); D4's reconciliation re-types them `-.->|ref|` to match the WAVE-1 per-page `edges:` findings (a non-record concept page emits ONLY `reference` edges) — the per-page frontmatter blocks are authoritative, this map is the derived mirror (scheme §4(b)). deferred integrated_at to finalize per role-spec (did NOT touch the report's `integrated_at`/`integration_commit` frontmatter). Cycle-id `cycle-103` taken from the parent dispatch prompt, not report content (the report discusses a batch-33 P1 campaign + follow-on tranches as forward-content, NOT a filing target).

---

## 2026-06-05T072032Z-layer-intro-author-p1-container-pages
applied_at: 2026-06-05T082500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/index.md (edit — prepend `kind: navigational-container (layer index)` + `reference`-only `edges:` [7 group-intro targets], NO rank, NO depends-on, before H1)
- book/src/L2/index.md (edit — same; 5 targets)
- book/src/L3/index.md (edit — same; 5 targets)
- book/src/L4/index.md (edit — same; 3 targets; FRONTMATTER ONLY [lines 1-11], above H1 line 13 — disjoint from the §Vocabulary cohort prose at line 42, which is D8's exclusive surface, untouched)
- book/src/L1-L0/index.md (edit — `kind: navigational-container (lowering index)`; 3 targets)
- book/src/L2-L1/index.md (edit — same; 11 targets)
- book/src/L3-L2/index.md (edit — same; 6 targets)
- book/src/L4-L3/index.md (edit — same; 11 targets)
- book/src/feature/index.md (edit — `kind: navigational-container (feature Part index)`; 3 targets)
- book/src/feature/spine-root.md (edit — `kind: navigational-container (feature group intro)`; 3 targets)
- book/src/feature/driver-leaf.md (edit — same; 18 targets)
- book/src/feature/output-product.md (edit — same; 15 targets)
- book/src/L1/blas1-elementwise-intro.md (edit — `kind: navigational-container (group intro)`; 13 targets)
- book/src/L1/operator-application-intro.md (edit — same; 4 targets)
- book/src/L1/constructed-operator-gates-intro.md (edit — same; 6 targets)
- book/src/L1/krylov-least-squares-intro.md (edit — same; 3 targets)
- book/src/L1/nep-interior-intro.md (edit — same; 6 targets)
- book/src/L1/fe-assembly-intro.md (edit — same; 4 targets)
- book/src/L1/fe-space-intro.md (edit — same; 3 targets)
- book/src/L2/step-kernels-intro.md (edit — same; 2 targets)
- book/src/L2/folds-intro.md (edit — same; 3 targets)
- book/src/L2/fold-family-stubs-intro.md (edit — same; 6 targets)
- book/src/L2/named-compositions-intro.md (edit — same; 5 targets)
- book/src/L2/elementwise-gate-floors-intro.md (edit — same; 6 targets)
- book/src/L3/blas1-intro.md (edit — same; 8 targets)
- book/src/L3/elementwise-intro.md (edit — same; 3 targets)
- book/src/L3/operator-apply-intro.md (edit — same; 2 targets)
- book/src/L3/smoother-intro.md (edit — same; 3 targets)
- book/src/L3/solver-caps-intro.md (edit — same; 5 targets)
- book/src/L4/iteration-combinators-intro.md (edit — same; 4 targets)
- book/src/L4/data-algebra-combinators-intro.md (edit — same; 11 targets)
- book/src/L4/outer-driver-combinators-intro.md (edit — same; 6 targets)
- book/src/L1-L0/mutation-rotation-intro.md (edit — same; 28 targets)
- book/src/L1-L0/construction-rotation-intro.md (edit — same; 5 targets)
- book/src/L1-L0/obstruction-intro.md (edit — same; 4 targets)
- scaffolding/open-questions.md (append — cycle-103 D5 subsection: 1 new OQ opened [linter outside-dag gap for 23 group-intros] + 1 convention-decision closure note [container node-status])

Gate hits:
- valid-YAML-frontmatter: 0 (PASS — all 35 `edges:` blocks round-trip through `yaml.safe_load`; verified this invocation, each parses to `{kind: navigational-container ..., edges: {reference: [...]}}` with the `#`-comment continuation lines harmless)
- rank-on-container: 0 (PASS — verified programmatically: 0 of 35 carry a `rank:` token; navigational containers make no resolution claim, not in the total order)
- depends-on-on-container: 0 (PASS — verified programmatically: 0 of 35 carry a `depends-on:` edge; reference-only, so no rank constraint and no liveness — an index cannot keep dead vocabulary alive)
- rank-invariant (well-foundedness): 0 (PASS — every edge is `reference` [navigational], zero `depends-on`, zero `rank:`; the `rank(u)≤min(deps)` invariant is vacuously satisfied — no rank node, no blocking edge)
- dangling-reference-target: 0 (PASS — 230 reference targets across the 35 blocks, ALL present on disk; parsed the CYCLE.md edit blocks programmatically and stat'd each `book/src/<slug>.md` — 0 missing; member sets match SUMMARY.md per the critic's independent re-derivation)
- H1-anchor-match / H1-reuses-page-heading: 0 (PASS — all 35 `[old]` H1 anchors matched verbatim on disk via Read before editing; no pre-existing frontmatter on any of the 35, so the `--- ... ---` prepend is collision-free; H1 preserved verbatim below the frontmatter in every file)
- same-file-partition (L4/index.md vs D8): 0 (PASS — D5's frontmatter occupies lines 1-11 ABOVE the `# L4 — Top of the stack` H1 [line 13]; the `## Vocabulary cohort` section is at line 42, fully disjoint; D8's mid-file prose surface is untouched. Confirmed on disk this invocation)
- forward-edge-without-surface: 0 (PASS — typed-edge container-typing pass, no surface claims; reference edges are navigational)
- variant-axis-missing: 0 (N/A — navigational containers carry no variant axes)
- append-on-missing-slug / SUMMARY-registration auto-fix: 0 (no new files created, no SUMMARY edit needed — all 35 container pages already registered; this is a frontmatter backfill on existing pages)
- alpha-position-insert: 0 (N/A — no SUMMARY/index-table row inserted; pure per-page frontmatter prepend)
- citecheck (scan): 1 ok, 0 failing — `python3 tools/citecheck/citecheck.py --scan <CYCLE.md> --quiet` → "1 ok, 0 failing (1 citations checked)", exit 0. No MISS/AMBIG/OOB. (The lone citation is the linter source-line reference `graded_stack_lint.py:637`; resolves.)

Open questions promoted:
- linter-outside-dag-misses-group-intro-container-pages (NEW — ROUTE TO META-PHASE/tools; `is_likely_outside_dag` recognizes the 8 `*/index` + `feature/index` + 3 feature-group pages [12 of 35] but NOT the 23 `L*/...-intro` group-intros → they shift to the `detritus_with_typed_edges` bucket once typed; informational NOISE, not a failure [rank_violations stays 0]; fix = honor `kind: navigational-container` tag, folds with D4's `dependency-map-not-recognized-outside-dag-by-linter` — one rule fixes both)
- graded-stack-index-and-concept-node-status (CONTAINER-HALF CLOSURE NOTE — DECIDED by D5: index + group-intro pages are navigational containers [no `rank:`, `reference`-only, `kind: navigational-container`]; aligned with D4's `concepts/index`+`dependency-map` decision; for batch-close meta-phase to RATIFY into graded-stack-scheme.md)

Build-relevant: yes (35 book/src/*.md frontmatter prepends — finalize should rebuild; mdBook strips the YAML frontmatter, no link/content change, build-safe)

Notes: Sixth per-report integrator this cycle (report 6/8). overall_status: ready set by the CRITIC directly (all-8-pass clean, no repairer ran — valid path per role-spec). All 35 frontmatter prepends applied EXACTLY as proposed; ZERO discretionary deviations (no SUMMARY auto-fix, no alpha-position discretion, no stub materialization — all 35 are pre-existing registered pages getting a frontmatter backfill). Re-read every one of the 35 target files' line 1 on disk (via Read) before editing — none had pre-existing frontmatter, all 35 H1 anchors matched verbatim. The L4/index.md edit is FRONTMATTER ONLY (lines 1-11, above the H1) and is byte-disjoint from D8's §Vocabulary-cohort prose surface (line 42) — confirmed by direct on-disk read this invocation (I make NO claim about whether D8 has landed; report 8/8 is applied AFTER this per the dispatch order, and I observed only the current L4/index.md disk state, which carries D5's frontmatter + the pre-existing body untouched). The ROUTED FINDING (linter `is_likely_outside_dag` does not recognize the 23 group-intro pages → detritus lint noise) was VERIFIED against the live linter source (`tools/graded-stack-lint/graded_stack_lint.py:637-647`: matches `OUTSIDE_DAG_PREFIXES` + `/index` suffix + `FEATURE_NON_COLUMN` only) and RECORDED as an OQ for meta-phase/tools — NOT fixed here (`tools/` is meta-phase write-authority). untyped-count reduction: per the report+critic, untyped 142→107 (−35 exact), rank_violations 0→0. deferred integrated_at to finalize per role-spec (did NOT touch the report's `integrated_at`/`integration_commit` frontmatter). Cycle-id `cycle-103` taken from the parent dispatch prompt, not report content.

---

## 2026-06-05T071856Z-abstractor-eliminate-rhs-l1-l0-disposition
applied_at: 2026-06-05T083500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/fe-operator-assemble-mutation-rotation.md (edit — §Status disposition note [FOLD, no sibling theme] + new anchored sub-section §"The `eliminate_rhs` leg (folded here)" appended at file end consolidating the rap.cpp:62-80 body walk as the linkable home for the 4 cross-ref sites)
- book/src/L1/eliminate_rhs.md (edit — frontmatter `lowers_to:` RE-POINTED `L1-L0/eliminate-rhs-mutation-rotation` [dangling, non-existent] → `L1-L0/fe-operator-assemble-mutation-rotation` [real firm]; line-46 forthcoming-ref → folded-home link; §"Downward to L0" rewritten from "(forthcoming)/references-but-does-not-contain" → the FOLD pointer, phantom `eliminate-essential-bc-mutation-rotation` slug removed)
- book/src/L4/eliminate_bc.md (edit — line ~312 de-stale: forthcoming RHS-rotation ref → folded-here pointer; CROSS-SCOPE c101 D1 content, see Notes)
- book/src/L4-L3/bc-elimination-post-composition-dissolution.md (edit — lines 78-80 de-stale: "(forthcoming)/no file exists yet" → folded-into-fe-operator-assemble-mutation-rotation pointer; CROSS-SCOPE c101 D1 content)
- book/src/L4-L3/index.md (edit — TWO sites de-staled: table row [actual line 35, report said "15"] + Vocabulary-cohort bullet [actual line 66, report said "46"]; both "RHS-side `eliminate-rhs-mutation-rotation` (forthcoming)" → folded-into pointer; CROSS-SCOPE c101 D1 content)
- scaffolding/open-questions.md (append — cycle-103 D6 subsection: OQ `eliminate-rhs-mutation-rotation-l1-l0-half-forthcoming-vs-already-folded` RESOLVED/CLOSED verdict already-folded [== `fe-bc-elimination-l1-l0-theme-split-vs-fold`, the line-1245 plan-migrated item]; 1 NEW OQ `eliminate-rhs-l1-index-bullet-stale-forthcoming-prose` opened)

Gate hits:
- retroactive-budget (per-slice / global): 0 (no retroactive edits to prior reports; the L4/L4-L3 touches are de-stale prose on already-integrated c101 ARTIFACT content, not report-content edits — see Notes)
- forward-edge-without-surface: 0 (FOLD adds NO new node; the new sub-section consolidates the EXISTING firm step-5 body walk into a named anchor — surface gains an anchor, carries the already-firm rap.cpp evidence)
- edge-label / prose mismatch: 0 (the re-pointed `lowers_to:` edge is L1>L0, the prose at each de-stale site discusses the L1→L0 half it names; consistent)
- rank-invariant (well-foundedness): 0 (PASS — the `lowers_to:` re-point resolves a DANGLING edge [pointed at a non-existent node = unsatisfiable rank constraint] to a real `firm` node: `eliminate_rhs` rank 3 → `fe-operator-assemble-mutation-rotation` rank 3, `rank(u)≤rank(v)` holds [3≤3]; no new node admitted so HARD-gate-new has nothing to admit)
- append-on-missing-slug: 0 (N/A — re-point to an EXISTING firm theme, not an append on a missing slug; the dangling target never existed and is now correctly NOT created [FOLD, not stub-materialize — the leg is already homed, so no stub warranted])
- concept_writes / variant-axis-missing / H1-reuse / SUMMARY-registration / alpha-position: 0 (N/A — no new file, no new chapter, no SUMMARY edit, no concept page; the new sub-section is a `##` heading inside an existing registered chapter, not an H1 page-heading reuse)
- dangling-reference-target (post-edit sweep): 0 (PASS — verified on disk THIS invocation: NO markdown link to a non-existent `eliminate-rhs-mutation-rotation.md` anywhere in book/src/; all remaining `eliminate-rhs-mutation-rotation` mentions are backtick plain-text "no separate / folded" disposition statements [non-link]; the new anchor `## The \`eliminate_rhs\` leg (folded here)` exists [grep count 1]; the `lowers_to:` target file exists [19913 bytes])
- citecheck (scan): 29 ok, 1 failing — `python3 tools/citecheck/citecheck.py --scan <CYCLE.md> --quiet` → exit 1. The lone failing is `[AMBIG] index.md:15` — this is the REPORT'S OWN descriptive prose naming its de-stale TARGET (`L4-L3/index.md:15,46`) as a bare basename, NOT a load-bearing L0 source citation that lands in the artifact. The 29 ok include the load-bearing rap.cpp:56-82 / rap.cpp:62-80 per-line cites + laplaceoperator.cpp:252 + the covering-theme back-refs, all resolving. NOT blocking (the AMBIG is on a basename in report prose, not a MISS/OOB on an applied edge's evidence). NOTE: the report's stated line numbers for the L4-L3/index.md sites ("15,46") are WRONG — the actual phrase lives at lines 35 (table row) + 66 (bullet); I located both by grepping the verbatim anchor phrase and de-staled both correctly.

Open questions promoted:
- eliminate-rhs-mutation-rotation-l1-l0-half-forthcoming-vs-already-folded (RESOLVED/CLOSED — verdict already-folded; == fe-bc-elimination-l1-l0-theme-split-vs-fold; closes the line-1245 plan-migrated item)
- eliminate-rhs-l1-index-bullet-stale-forthcoming-prose (NEW — L1/index.md:96 stale plain-text "(forthcoming)" tail; out of D6's enumerated scope so NOT touched here; non-link, non-build-breaking; routed for a future L1/index.md touch)

Build-relevant: yes (touches 5 book/src/*.md files — finalize should rebuild; all edits are prose + one frontmatter `lowers_to:` re-point, mdBook/linkcheck2-safe; the re-point RESOLVES a previously-dangling edge so it IMPROVES link health)

Notes: Seventh per-report integrator this cycle (report 7/8, D6). overall_status: ready set by the CRITIC directly (all-8-pass clean, no repairer ran — valid path per role-spec). All 7 proposed-change blocks applied; the only deviation from the report's literal text was CORRECTING its WRONG line numbers for the L4-L3/index.md sites (report said "15,46"; actual sites are 35+66 — located by grepping the verbatim "RHS-side `eliminate-rhs-mutation-rotation` (forthcoming)" anchor phrase, de-staled both). Re-read every target file on disk THIS invocation before editing. CROSS-SCOPE FLAG FOR FINALIZE: the 3 L4/L4-L3 edits (eliminate_bc.md:312, bc-elimination-post-composition-dissolution.md:78-80, L4-L3/index.md:35,46) touch ARTIFACT content authored by the already-integrated cycle-101 D1 dispatch — they are mechanical forward-ref de-stale corrections (the SAME reachability defect this OQ closes: the dangling `eliminate-rhs-mutation-rotation` slug), applied per the report+critic's reconciliation note (the critic confirmed the only co-batch L4-surface report, D8/L4-cohort-bullets, edits `book/src/L4/index.md` — a DIFFERENT file — so NO line-level collision within the cycle-103 batch). The load-bearing subset (closes the OQ + fixes the dangling edge) is (1) the covering-theme sub-section + §Status note and (2) the L1/eliminate_rhs.md `lowers_to:` re-point + §"Downward to L0" rewrite; the L4/L4-L3 de-stales are the complementary cleanup. I observed the on-disk state directly: the L4-L3/index.md I edited already carried D5's navigational-container frontmatter (D5's row 6 above) on lines 1-19, byte-disjoint from the table row (35) + bullet (66) I touched — no overlap with D5's frontmatter prepend. I make NO claim about whether D8 has landed (it is dispatched after me per the order; the prompt confirms D8 touches L4/index.md, a file I did not touch). deferred integrated_at to finalize per role-spec (did NOT touch the report's `integrated_at`/`integration_commit` frontmatter). Cycle-id `cycle-103` taken from the parent dispatch prompt, NOT report content (the report discusses forward-cycle disposition framing as content, not a filing target).

---

## 2026-06-05T072449Z-layer-intro-author-l4-cohort-bullets
applied_at: 2026-06-05T084500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/index.md (edit — inserted 2 §Vocabulary-cohort PROSE bullets: `eliminate_bc` immediately before the `fe_assemble` bullet; `preconditioning-framework` immediately before the `solve_family` bullet — mid-file prose surface, byte-disjoint from D5's frontmatter `edges:` block on lines 1-11)
- scaffolding/open-questions.md (append — cycle-103 D8 subsection: OQ `vocabulary-cohort-bullets-missing-for-precond-framework-and-eliminate-bc` RESOLVED/CLOSED)

Gate hits:
- retroactive-budget (per-slice / global): 0 (no retroactive edits to prior reports)
- forward-edge-without-surface: 0 (PASS — both bullets are Part-overview prose referencing already-firm chapters; no surface claim authored)
- edge-label / prose mismatch: 0 (PASS — the repairer corrected the cosmetic "between A and B" placement-justification gloss in CYCLE.md pre-integration; the two `edit:` blocks themselves were preserved unchanged and are anchor-defined, not list-position-defined)
- concept_writes on existing slug: 0 (N/A — no concept page written; pure cohort-bullet prose insertion into an existing index)
- variant-axis-missing: 0 (N/A — Part-overview prose, not a multi-variant operator entry; the underlying chapters carry their variant axes)
- H1-reuse / append-on-missing-slug / SUMMARY-registration auto-fix / alpha-position-insert: 0 (N/A — no new file, no H1, no SUMMARY edit; the two bullets are placed alpha-LOCALLY against their named on-disk anchors per the report, no integrator alpha-position discretion exercised)
- rank-invariant (well-foundedness): 0 (PASS — no `rank:` or `depends-on` edge authored; the two bullets narrate already-firm chapters and their `reference`-style cross-links, emitting no rank/liveness claim → invariant vacuously satisfied)
- cross-reference-integrity (verified on disk THIS invocation): 0 (PASS — all 13 distinct cross-links across the two new bullets resolve to on-disk firm chapters: ./eliminate_bc.md, ./preconditioning-framework.md, ./fe_assemble.md, ./ksp_solve.md, ./eigsolve.md, ./krylov-step.md, ./linear_combination.md, ./solve_family.md, ../L1/essential_dofs.md, ../L4-L3/bc-elimination-post-composition-dissolution.md, ../concepts/{state-stratification,capability-typing,derived-view-hoisting}.md — 13/13 present, build-safe for linkcheck2)
- same-file-partition (vs D5): 0 (PASS — D5's frontmatter `edges:` block occupies lines 1-11 ABOVE the `# L4 — Top of the stack` H1 [line 13]; I edited ONLY the §Vocabulary-cohort prose bullets [line 60 `fe_assemble` anchor; line 59 `solve_family` anchor as read on disk this invocation], a disjoint mid-file region. Did NOT touch the frontmatter, the `21 + 4` firm-count header [line 44], or any other surface. Re-read the §Vocabulary-cohort section on disk this invocation AFTER D5's frontmatter landed — confirmed the frontmatter present on lines 1-11 and both `[old]` anchors matched verbatim before editing.)
- citecheck (scan): 4 ok, 0 failing — `python3 tools/citecheck/citecheck.py --scan <CYCLE.md> --quiet` → "4 ok, 0 failing (4 citations checked)", exit 0. No MISS/AMBIG/OOB; clean.

Open questions promoted:
- vocabulary-cohort-bullets-missing-for-precond-framework-and-eliminate-bc (RESOLVED/CLOSED — the 2 firm L4 chapters [eliminate_bc c101, preconditioning-framework c096] now carry their §Vocabulary-cohort bullets; closes the plan-migrated line-1247 item, plan item 2 `bc-cohort-content-tail-and-record-homes` loses this sub-item)

Build-relevant: yes (touches book/src/L4/index.md — finalize should rebuild; the two prose-bullet insertions are mdBook/linkcheck2-safe, all 13 cross-links resolve)

Notes: Eighth and FINAL per-report integrator this cycle (report 8/8, D8) — staging COMPLETE for cycle-103. overall_status: ready set by the REPAIRER (the lone edge-label-fidelity WARNING was repaired in-report: the cosmetic "between A and B" placement-justification PROSE gloss in CYCLE.md was rewritten to anchor-based phrasing; the two `edit:book/src/L4/index.md` blocks themselves were preserved UNCHANGED and are correct) — a valid `ready` path. Both bullet insertions applied EXACTLY as proposed; ZERO discretionary deviations (no alpha-position discretion exercised — the report specified each anchor; I honored the named on-disk anchor for each insertion). Re-read the §Vocabulary-cohort section on disk THIS invocation BEFORE editing: confirmed D5's navigational-container frontmatter is present on lines 1-11 (the `# L4 — Top of the stack` H1 is at line 13), and both `[old]` anchors (the `fe_assemble` bullet opening at line 60, the `solve_family` bullet opening at line 59) matched verbatim. My edits are to the mid-file prose region only — byte-disjoint from D5's frontmatter prepend; I did NOT touch the frontmatter or the `21 + 4 outer-driver` firm-count header. I describe only the L4/index.md disk state I directly observed this invocation (D5's frontmatter + the pre-existing body); I make no assumption about any sibling landing beyond what I read off disk + the staging rows above. deferred integrated_at to finalize per role-spec (did NOT touch the report's `integrated_at`/`integration_commit` frontmatter). Cycle-id `cycle-103` taken from the parent dispatch prompt, NOT report content (the report discusses WAVE-2 / forward framing as content, not a filing target).

---
