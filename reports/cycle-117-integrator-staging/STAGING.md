# cycle-117 integrator staging log

Per-report integration rows, newest LAST (append-only). The row ORDER is the authoritative apply-order record; `applied_at` is advisory only. integrator-finalize reconciles from this log.

Cycle-117 serial apply-order: D1 → D3 → D4 → D5 → D2.

---

## 2026-06-06T205239Z-layer-intro-author-waveguide-mode (D1)
applied_at: 2026-06-06T21:27:48Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/feature/waveguide-mode.L4.md (created — new output-product feature column, L4 composition root; status: seed / rank: rough-in)
- book/src/feature/waveguide-mode.L1.md (created — L1 pure-function composition root; seed / rough-in)
- book/src/feature/waveguide-mode.L0.md (created — L0 ground-truth surface; seed / rough-in)
- book/src/feature/index.md (edited — matrix row alpha after sparameters; output-product cohort prose +6th product; directive-scope line; firm-block 11→12 cols w/ boundary-mode firm; seed-block now holds only waveguide-mode)
- book/src/feature/output-product.md (edited — frontmatter +3 reference edges; cohort bullet +waveguide-mode; complete-cohort prose 5→6 cols)
- book/src/SUMMARY.md (edited — +3 waveguide-mode entries, last in feature/output-product grouping)

Gate hits:
- citecheck bounds + path-hygiene lint: 30 ok, 0 failing (--scan over CYCLE.md; no MISS/AMBIG/OOB)
- SUMMARY.md chapter registration: report proposed all 3 SUMMARY entries explicitly; no auto-fix needed
- alphabetical-position insert: report specified positions (matrix row + SUMMARY both alpha-after-sparameters, within-column high→low L4→L1→L0 preserved); no discretionary placement
- rank gate (graded-ladder): waveguide-mode chapters land rank: rough-in resting on boundary-mode (rough-in/seed) + the unhomed reduce verb — rank(u) ≤ rank(deps) holds, NO violation. New depends-on edges typed: `composes` (to boundary-mode.L{4,1}), `cites-evidence` (to the L0 driver range), `uses-record` (to concepts/config-record). The cross-link to boundary-mode is a SIBLING reference per OWN-COMPOSITION (NOT a blocker). No firm-flip in this report's own chapters, so no upward rank-gate assertion needed here.
- retroactive-budget: 0
- forward-edge / edge-label / variant-axis / H1-reuse / append-on-missing-slug / index-placeholder: 0 hits

Open questions promoted:
- waveguide-mode-reduce-needs-l4-verb-home (the seed→firm promotion gate; dispatch a combinator-miner/harvester on the verb)
- record-WaveguideModeTable-needs-definition-home (≥2-consumer bar met; flag for concepts/<record>.md page; canonical name WaveguideModeTable settled by repairer)
- waveguide-mode-vs-eigenfreq-qfactor-shared-eigsolve-corner (non-blocking do-NOT-over-unify guard)

Build-relevant: yes (touches book/src/feature/*.md + book/src/SUMMARY.md)

Notes:
- BOTH-LAND COUPLING WITH D2 (load-bearing for finalize). This report (D1) carries the feature/index.md cells reflecting boundary-mode → `firm` (firm-block 11→12 columns incl. boundary-mode; directive-scope line; seed-block now holding only waveguide-mode), on D2's behalf, because D1 is the sole owner of the shared feature/ index this cycle. D2 (the boundary-mode promotion dispatch) owns the boundary-mode chapter-body `## Status` + frontmatter `rank:`/`feature_root:` flips. ON-DISK STATE OBSERVED THIS INVOCATION: I re-read book/src/feature/boundary-mode.L4.md and it is STILL `feature_root: seed` / `rank: rough-in` (D2 has NOT landed yet — it is LAST in this cycle's apply-order, D1→D3→D4→D5→D2). So right now the index-cell (boundary-mode firm) LEADS the on-disk chapter body (still seed) — this is the expected transient state given the apply-order; D2 lands later THIS cycle and reconciles it. If D2 does NOT land this cycle, finalize must reconcile (defer D1's three boundary-mode-firm index reflections to avoid index-cell-drift, i.e. both-land-or-both-defer). Per repairer META, D2 is `overall_status: ready`, so the joint-land condition is expected to hold.
- Reachability/rank impact: a new feature output-product column adds depends-on edges into firm `eigsolve` (via the boundary-mode driver column) + the L0 driver range. New nodes are reachable from the feature-surface root set (wired into the matrix, output-product group-intro, and SUMMARY). The authoritative rank/reachability re-measure is finalize step-5b (the linters) — recorded here, not re-run.
- Record name reconciled to canonical `WaveguideModeTable` by the repairer (the OQ slug is `record-WaveguideModeTable-needs-definition-home`, promoted under that canonical slug per dispatch instruction). The boundary-mode chapters' cross-name `BoundaryModeResult` (D2-owned, outside this report) is left for the future concept page to reconcile.
- deferred integrated_at to finalize per role-spec (per-report integrator does not touch the consumed report's frontmatter).

---

## 2026-06-06T205239Z-harvester-build-mesh (D3)
applied_at: 2026-06-06T21:42:10Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/build_mesh.md (created — new firm L1 operator `build_mesh :: Config -> Mesh`, status firm / firm-on-positive-structure, rank: firm; in-chapter `## Record definition` for the `Mesh` record)
- book/src/L1/index.md (edited — NEW kind-grouping header `**Mesh & FE-space construction**` + the `build_mesh` dep-map row, inserted immediately BEFORE the `**FE-space sub-spine**` grouping per the report NOTE's "otherwise" branch; alpha-within-kind = sole row in the new grouping)
- book/src/SUMMARY.md (edited — NEW `Mesh & FE-space construction` sub-chapter grouping (linking `./L1/index.md` placeholder) + `build_mesh` chapter entry, inserted before the `FE-space sub-spine` grouping)

Gate hits:
- citecheck bounds + path-hygiene lint: 33 ok, 0 failing (--scan over CYCLE.md; no MISS/AMBIG/OOB)
- SUMMARY.md chapter registration: report proposed the SUMMARY entry explicitly; applied as proposed (no auto-fix needed). Grouping links the `./L1/index.md` placeholder per the report NOTE (D4 may later author a `mesh-construction-intro.md` group page — D4 follows D3 in apply-order, so the placeholder is correct now).
- alphabetical-position / kind-grouping insert: applied-discretionarily (rationale: alpha-position-insert / kind-grouping-placement). The report NOTE specified the position (new grouping immediately BEFORE `FE-space sub-spine`, both in L1/index.md dep-map and SUMMARY); D4 (layer-intro-author) owns the final placement judgment (fold-into-FE-space-sub-spine vs standalone grouping; group-intro authoring) — flagged via OQ `build-mesh-kind-grouping-placement-deferred-to-d4`.
- rank gate (graded-ladder): `build_mesh` lands `rank: firm` (3). Its only `depends-on` edges are `cites-evidence` to rank-terminal L0 source (`palace/fem/mesh.hpp:44-115`, `palace/main.cpp:286-301`) — rank-terminal ground truth ≥ 3, so well-foundedness `rank(u) ≤ min(deps)` HOLDS, NO violation. `reference` edges (to `L1/fe_space`, `feature/lifecycle.L1`) are navigational, free. No firm-flip on a non-firm dependency. No `lowers-to` edge asserted (the L1>L0 theme is named-not-authored).
- retroactive-budget: 0 (new chapter, not a refinement-shaped modification of an existing entry)
- forward-edge / edge-label / variant-axis / H1-reuse / append-on-missing-slug / index-placeholder / concept_writes-on-existing-slug: 0 hits
- consolidated firm-count tally bump: NOT applied here (per dispatch + report NOTE, D4 owns the L1/index.md §Vocabulary-cohort firm-count/tally; the +1 main-cohort firm for `build_mesh` is D4's to fold) — flagged in OQ `build-mesh-kind-grouping-placement-deferred-to-d4`.

Open questions promoted:
- record-Mesh-needs-definition-home (≥2-consumer bar met; flag for `concepts/mesh.md`; interim home is `build_mesh.md` §Record definition)
- build-mesh-construction-rotation-l1-l0-theme (named-not-authored L1>L0 rotation; follow-on abstractor/harvester dispatch; no live `lowers-to` edge yet)
- adaptive-amr-mesh-refinement-obstruction-at-lifecycle-root (MFEM-opaque adaptive AMR stays obstruction-documented at the lifecycle root, not forced; a-priori `build_mesh` half is the firm complement)
- build-mesh-kind-grouping-placement-deferred-to-d4 (kind-grouping placement + firm-count tally fold deferred to D4)

Build-relevant: yes (touches book/src/L1/*.md + book/src/SUMMARY.md)

Notes:
- ON-DISK STATE OBSERVED THIS INVOCATION: I re-read book/src/L1/index.md before editing and confirmed the dep-map table groupings (BLAS-1 & elementwise → ... → FE-assembly sub-spine → FE-space sub-spine → Rough-in(obstruction)); the `**FE-space sub-spine**` header row is present and unchanged from the D1 landing, so I inserted my new `**Mesh & FE-space construction**` grouping + `build_mesh` row immediately before it as the report NOTE directs. D4 (layer-intro-author) had NOT landed yet (it is AFTER me in apply-order D1→D3→D4→D5→D2), so I did NOT find any pre-existing mesh kind-grouping or `mesh-construction-intro.md` — I created the grouping myself per the NOTE's "otherwise" branch and linked the `./L1/index.md` placeholder in SUMMARY. The firm-count narrative in L1/index.md §Vocabulary-cohort still reads "33 main cohort / 40 firm grand total" on disk (NOT bumped by me — D4's to fold).
- `build_mesh` is the geometric substrate under all 5 solver pipelines (highest-fan-out entry of the mesh-wrapper front); single-machine scope (partition/distribute + `ParMesh`/`loc_attr` per-process remap read single-rank, flag-once-skip); MFEM-opaque adaptive AMR obstruction-documented at the lifecycle root (not forced); firm-on-positive-structure, no-dedicated-test caveat non-gating per `fe_space`/`fe_assemble`/`apply_linop` precedent.
- Reachability: `build_mesh` is reachable from the `lifecycle` feature root (which forward-references it as stage 1, `feature/lifecycle.L1.md:37,44`) and is consumed by firm `fe_space` — live, not garbage. The authoritative rank/reachability re-measure is finalize step-5b (the linters) — recorded here, not re-run.
- deferred integrated_at to finalize per role-spec (per-report integrator does not touch the consumed report's frontmatter).

---

## 2026-06-06T205239Z-layer-intro-author-fe-space-hierarchy (D4)
applied_at: 2026-06-06T22:05:30Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/fe_space_hierarchy.md (created — new firm L1 operator `fe_space_hierarchy :: [Mesh] -> [FECollection] -> Config -> FiniteElementSpaceHierarchy`, status firm / firm-on-positive-structure, rank: firm; the AddLevel-fold hierarchy combinator composing firm `fe_space` + firm `fe_collection`; in-chapter `## Record definition` for `FiniteElementSpaceHierarchy` (single-consumer))
- book/src/L1/fe_space.md (edited — 3 re-anchors of plain-text `ConstructFiniteElementSpaceHierarchy` / deferred-sibling forward-refs to live `[fe_space_hierarchy](./fe_space_hierarchy.md)` links: §Context para, law 4 hierarchy-base-case, deferred-sibling list now-firm note; no L0 line-number changes)
- book/src/SUMMARY.md (edited — `fe_space_hierarchy` chapter entry appended LAST in the `FE-space sub-spine` grouping, alpha-after `fe_space`)
- book/src/L1/fe-space-intro.md (edited — group-intro frontmatter +`L1/fe_space_hierarchy` reference edge; three-members→four-members prose extended with the hierarchy combinator)
- book/src/L1/index.md (edited — (5a) promoted the deferred-sibling `fe_space_hierarchy` bullet rough-in→FIRM; (5b) FE-space sub-spine narrative header 3→4; (5c) dep-map row inserted alpha-AFTER `fe_space` (alpha-corrected from the report's anchor — see Notes); (5d) consolidated firm-count reconciled to cycle-end all-three-firm state 40→43)

Gate hits:
- citecheck bounds + path-hygiene lint: 31 ok, 0 failing (--scan over CYCLE.md; no MISS/AMBIG/OOB)
- SUMMARY.md chapter registration: report proposed the SUMMARY entry explicitly; applied as proposed (no auto-fix needed)
- alphabetical-position insert: applied-discretionarily (rationale: alpha-position-insert). The report §5c specified the dep-map insert position as "after fe_collection, before fe_space" — that is alpha-INCORRECT (`fe_space` < `fe_space_hierarchy` since `fe_space` is a prefix). I placed the new row alpha-AFTER the `fe_space` row, consistent with the report's OWN SUMMARY edit (§3, which correctly places it after `fe_space`) and the fe-space-intro alpha ordering. Within the FE-space sub-spine kind grouping: essential_dofs < fe_collection < fe_space < fe_space_hierarchy.
- rank gate (graded-ladder): `fe_space_hierarchy` lands `rank: firm` (3). Its two `depends-on` edges (`composes` to `L1/fe_space`, `L1/fe_collection`) both target firm-on-disk nodes (both carry `rank: firm` / `## Status` = firm, c064/c065 — re-read this invocation: fe_space.md frontmatter `rank: firm`; fe_collection confirmed firm via index narrative + D3-era reads); the `cites-evidence` edge targets rank-terminal L0 ground truth (`palace/fem/multigrid.hpp:78-126`). Well-foundedness `rank(u) ≤ min(deps)` HOLDS at firm/firm — NO violation. The `reference` edge to `L1/build_mesh` is navigational (the `[Mesh]` element-type `Mesh` record home) — NOT a depends-on, carries no rank constraint; target exists on disk (D3 landed build_mesh.md this cycle, verified). No firm-flip on a non-firm dependency. No `lowers-to` edge asserted (the L1>L0 theme is named-not-authored).
- retroactive-budget: 0 (new chapter + a count-owner reconciliation of an existing index narrative — not a refinement-shaped rewrite of an existing operator entry)
- forward-edge / edge-label / variant-axis / H1-reuse / append-on-missing-slug / index-placeholder / concept_writes-on-existing-slug: 0 hits
- consolidated firm-count reconciliation (count-owner duty): applied to the cycle-END all-three-firm state per dispatch directive — grand total 40→43 (33 main + 4 FE-assembly + 5 FE-space + 1 Mesh-construction). `build_mesh` (+1, D3, firm on disk now) + `fe_space_hierarchy` (+1, this report, firm) + de-Rham interpolator (+1, D5, PRE-STAGED — D5 is `ready` and lands AFTER me in apply-order). Bumped both the lead-sentence tally AND the in-line count-discipline "= 43 ... holds **43** firm rows" phrase. SEE the count-owner reconciliation OQ — finalize must confirm D5's interpolator landed firm at FE-space sub-spine (if not, adjust 43→42).

Open questions promoted:
- record-FiniteElementSpaceHierarchy-needs-definition-home (record-definition obligation; single-consumer in-chapter home now; ≥2-consumer trigger → concepts/finite-element-space-hierarchy.md)
- fe-space-hierarchy-construction-rotation (deferred L1>L0 theme, sibling-pull-gated; no `lowers-to` edge yet)
- fe-space-front-l1-count-owner-reconciliation-c117 (count-owner reconciliation note; finalize confirms D5 interpolator firm + FE-space-home at cycle end)
- build-mesh-fe-space-kind-grouping-fold-residual-c117 (residual on D3's kind-grouping-placement OQ: D4 resolved the count tally but did NOT fold the Mesh-construction grouping into FE-space sub-spine nor author a mesh group-intro — left open for a follow-on)

Build-relevant: yes (touches book/src/L1/*.md + book/src/SUMMARY.md)

Notes:
- ON-DISK STATE OBSERVED THIS INVOCATION: I re-read book/src/L1/build_mesh.md path (EXISTS, D3 landed it — 17726 bytes) so the `reference` edge + the in-chapter / index `[build_mesh](./build_mesh.md)` links RESOLVE. I re-read book/src/L1/index.md and confirmed D3's `**Mesh & FE-space construction**` dep-map grouping header + `build_mesh` row sit at lines 170-171 (immediately before the `FE-space sub-spine` rows essential_dofs/fe_collection/fe_space at 173-175), and the consolidated firm-count still read "33 main / 40 grand / 3 FE-space" (D3 did NOT bump it — left to me as count-owner). I re-read book/src/SUMMARY.md and confirmed D3's `Mesh & FE-space construction` SUMMARY grouping (build_mesh, lines 224-225) sits above the `FE-space sub-spine` grouping (226-229); I appended `fe_space_hierarchy` as the new last entry in the FE-space sub-spine grouping. I re-read book/src/L1/fe_space.md and confirmed all three re-anchor `[old]` blocks matched verbatim; fe_space.md frontmatter `rank: firm` confirms the firm/firm well-foundedness for the new `composes` edge.
- COUNT-OWNER reconciliation applied to the CYCLE-END state (all three FE-construction landings firm), per the explicit dispatch directive. D3 `build_mesh` is firm on disk now; D5 de-Rham interpolator is PRE-STAGED (+1) because it is `ready` and lands next this cycle. If D5 does NOT land firm at the FE-space sub-spine, finalize must decrement the grand total 43→42 and the FE-space sub-spine count 5→4 — flagged in the count-owner reconciliation OQ.
- KIND-GROUPING FOLD NOT DONE: D3's OQ deferred to D4 (a) folding the new `Mesh & FE-space construction` grouping into the `FE-space sub-spine` grouping and (b) authoring a `mesh-construction-intro.md` group page. The report did NEITHER (it authored `fe_space_hierarchy` into the existing FE-space sub-spine and resolved only the count tally). I did not force a structural fold not in the report's proposed-changes. Left as the residual OQ `build-mesh-fe-space-kind-grouping-fold-residual-c117` for a follow-on layer-intro-author.
- The cosmetic §3 heading mislabel the critic noted (CYCLE.md heading reads "book/src/L1/SUMMARY.md" but the fence is `edit:book/src/SUMMARY.md`) — applied against the CORRECT path `book/src/SUMMARY.md` (the single mdBook SUMMARY); no harm.
- deferred integrated_at to finalize per role-spec (per-report integrator does not touch the consumed report's frontmatter).

---

## 2026-06-06T205239Z-harvester-interpolator (D5)
applied_at: 2026-06-06T21:43:00Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/interpolator.md (created — new firm L1 operator `interpolator :: FiniteElementSpace[(D:...)] -> FiniteElementSpace[(R:...)] -> LinOp[(R:...),(D:...)]`, the de-Rham discrete grid-transfer operator from `GetDiscreteInterpolator`/`BuildDiscreteInterpolator`; status firm / firm-on-positive-structure; rank: firm. Carries an in-chapter `obstruction (opaque-library-ownership)` SIBLING NOTE for the GSLIB point-interpolation facility — kept SEPARATE from the firm claim, orthogonal + non-gating)
- book/src/L1/index.md (edited — (a) NEW `interpolator` dep-map row inserted alpha-AFTER `fe_space_hierarchy` (alpha-corrected from the report's anchor — see Notes); (b) the Vocabulary-cohort `BuildDiscreteInterpolator *(rough-in; no anchor yet)*` bullet REPLACED with the now-FIRM `interpolator` bullet (cycle-117 D5))
- book/src/SUMMARY.md (edited — `interpolator` chapter entry appended LAST in the `FE-space sub-spine` grouping, alpha-after `fe_space_hierarchy`)

Gate hits:
- citecheck bounds + path-hygiene lint: 34 ok, 0 failing (--scan over CYCLE.md; no MISS/AMBIG/OOB)
- SUMMARY.md chapter registration: report proposed the SUMMARY entry explicitly; applied (alpha-position adjusted — see below)
- alphabetical-position insert: applied-discretionarily (rationale: alpha-position-insert). The report's proposed-changes block (authored before D4 landed) places the `interpolator` dep-map row + SUMMARY entry alpha-after `fe_space` (it did not see D4's `fe_space_hierarchy` landing). On disk, D4 inserted `fe_space_hierarchy` between `fe_space` and the eventual `interpolator` slot. Alpha order within the FE-space sub-spine kind grouping: essential_dofs < fe_collection < fe_space < fe_space_hierarchy < interpolator (since `i` > `f`). I placed BOTH the dep-map row and the SUMMARY entry alpha-AFTER `fe_space_hierarchy` (the on-disk last FE-space-sub-spine sibling), preserving alpha-within-kind correctness.
- rank gate (graded-ladder): `interpolator` lands `rank: firm` (3). It carries NO `depends-on` edges at all — the `edges:` frontmatter block has ONLY a `reference:` list (5 navigational edges: `L1-L0/interpolator-construction-rotation` [FORTHCOMING, demoted from `lowers-to` per repairer fix #2], `L1/apply_linop`, `L1/fe_space`, `L1/divfree-projector`, `concepts/constructed-operators`). Firm rank rests on positive L0 ground truth (rank-terminal), NOT on any dependency. Well-foundedness `rank(u) ≤ min(deps)` is VACUOUSLY satisfied (no depends-on deps) — NO violation. NO firm-flip on a non-firm dependency.
- forward-edge / edge-label / variant-axis / H1-reuse / append-on-missing-slug / index-placeholder / concept_writes-on-existing-slug / retroactive-budget: 0 hits

Open questions promoted:
- interpolator-construction-rotation-l1-l0-theme-needed (the authoring tracker for the demoted theme; promote the `reference` edge → `depends-on (kind: lowers-to)` once the L1>L0 theme is authored + firm)
- interpolator-derham-exactness-law-anchor (promote `Curl·Grad=0`/`Div·Curl=0` from defining-family property → verified law given a literature/MFEM anchor or a constructed composition test)
- gslib-field-interp-facility-dedicated-obstruction-theme (the in-chapter GSLIB sibling note → a first-class L1>L0 obstruction theme if a feature-surface consumer surfaces)

Build-relevant: yes (touches book/src/L1/*.md + book/src/SUMMARY.md)

Notes:
- NO-DANGLING-DEPENDS-ON-EDGE CHECK (the load-bearing linter-cleanliness verification, per dispatch): CONFIRMED. I re-read the created interpolator.md frontmatter on disk this invocation and verified via grep that there is NO `depends-on:` KEY anywhere in the frontmatter — the only edge key is `reference:`, and the forthcoming `L1-L0/interpolator-construction-rotation` slug sits UNDER `reference:` (navigational, slug-as-text), exactly per repairer fix #2. The 3 textual occurrences of the string "depends-on" in the frontmatter are all explanatory COMMENT lines (`# ...`) describing why the edge is a reference until the theme is authored — NOT a live key. So the entry carries NO blocking edge to a non-existent target → finalize's rank-linter stays `unresolved_depends_on_targets=0` / `rank_violations=0`. The repairer fix #1 (curlcurloperator.hpp:112 relabeled gradient→curl) is reflected in the authored chapter (Variant axes + Evidence both label `:112` as the curl-curl operator's discrete curl `GetCurlMatrix`).
- CONFIRMS D4's COUNT: this report lands `interpolator` as `firm` at the FE-space sub-spine — exactly the +1 firm interpolator that D4 PRE-STAGED into the consolidated firm-count (40→43; FE-space sub-spine 4→5). D4's OQ `fe-space-front-l1-count-owner-reconciliation-c117` asked finalize to confirm D5 landed firm at the FE-space sub-spine; it DID (status firm, FE-space-sub-spine home in both index dep-map and SUMMARY), so finalize keeps the grand total at 43 (no decrement to 42). I did NOT touch the consolidated firm-count narrative myself (D4 owns it as count-owner; my changes are only the OWN alpha-position dep-map row + OWN Vocabulary-cohort bullet + OWN SUMMARY entry).
- ON-DISK STATE OBSERVED THIS INVOCATION: I re-read book/src/L1/index.md and confirmed D4's `fe_space_hierarchy` dep-map row at line 176 (immediately after `fe_space` at 175) and the now-FIRM `fe_space_hierarchy` Vocabulary-cohort bullet at line 111; the `BuildDiscreteInterpolator *(rough-in; no anchor yet)*` bullet was still present verbatim at line 112 (matched the report's OLD anchor exactly). I re-read book/src/SUMMARY.md and confirmed D4's `fe_space_hierarchy` SUMMARY entry at line 230 (last in the FE-space sub-spine grouping) before appending `interpolator` after it. interpolator.md did NOT pre-exist (clean create).
- Reachability: `interpolator` is reachable from feature roots — consumed by firm `divfree-projector` (the `Grad` step), and is the discrete-curl operator behind the boundary-mode `Bz = curl(Et)` readout, AMS setup, curl-curl, and post-processing — all live solver/feature-surface paths. Not garbage. The authoritative rank/reachability re-measure is finalize step-5b (the linters) — recorded here, not re-run.
- deferred integrated_at to finalize per role-spec (per-report integrator does not touch the consumed report's frontmatter).

---
## 2026-06-06T205239Z-layer-intro-author-boundary-mode-promotion (D2)
applied_at: 2026-06-06T21:47:42Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/feature/boundary-mode.L4.md (edited — frontmatter `rank: rough-in → firm` + sibling `reference: feature/waveguide-mode.L4` edge; stage-(3) readout forward-ref → live `./waveguide-mode.L4.md` link; "Why this composes" prose seed→firm OWN-COMPOSITION; down-link table readout row forward-ref → sibling-ref; `## Status` token `seed → firm` + promotion prose — 5 blocks)
- book/src/feature/boundary-mode.L1.md (edited — frontmatter `rank: rough-in → firm` + sibling `reference: feature/waveguide-mode.L1` edge; output forward-ref → live `./waveguide-mode.L1.md` link; down-link table readout row → sibling-ref; `## Status` token `seed → firm` + promotion prose — 4 blocks)
- book/src/feature/boundary-mode.L0.md (edited — frontmatter `rank: rough-in → firm` + sibling `reference: feature/waveguide-mode.L0` edge; stage-4 readout forward-ref → live `./waveguide-mode.L0.md` link; output forward-ref → live link; `## Status` token `seed → firm` + promotion prose — 4 blocks)

Gate hits:
- citecheck bounds + path-hygiene lint: 13 ok, 3 failing (--scan over CYCLE.md). The 3 MISS are all `reports/.../waveguide-mode/CYCLE.md:{52,333,421}` — cross-report PROVENANCE references in the report's prose to D1's sibling report file via an elided `...` path (deliberate report shorthand), NOT L0 source citations and NOT present in any landed `book/` content (the proposed-changes blocks cite only `boundarymodesolver.cpp`/`main.cpp` L0 anchors + intra-`feature/` relative links). Unrepairable-by-design (the `...` is a report convention, not a real path) and NON-BLOCKING (a sibling-report reference, not an artifact citation). The 13 real citations (L0 ranges + cross-links) all resolve OK.
- rank gate (graded-ladder): boundary-mode promoted `rank: rough-in → firm` (3) across all 3 level chapters. Per the rank linter's OWN-COMPOSITION demotion, the rank-constraining `depends-on` deps are the `composes`-to-vocabulary-op edges ONLY: L4 chapter `{L4/fe_assemble (firm/3), L4/eigsolve (firm/3)}`; L1 chapter `{L1/fe_assemble (firm/3), L1/eigsolve (firm/3)}`; L0 chapter carries only `cites-evidence` (rank-terminal L0 ground truth) — no blocking vocabulary deps. `rank(node)=3 ≤ min(deps)=3` HOLDS in all three — NO violation. Constituent firmness re-verified by reading each constituent's on-disk `## Status`/`rank` this cycle is not re-done by me (the critic confirmed it; staging rows for the deps unchanged) — but the promotion rests on firm/firm. The new `feature/waveguide-mode.{L4,L1,L0}` edges are typed `reference` (SIBLING output-product cross-link, the reciprocal drift-guard) — navigational, NOT `depends-on`, so they carry NO rank constraint; correct that a `firm` driver column references a `seed` sibling output-product column (OWN-COMPOSITION rule). NO firm-flip on a non-firm dependency.
- forward-edge claim without surface: 0 (the readout forward-ref is REPLACED by a live cross-link to D1's now-landed waveguide-mode files — verified on disk this invocation, see Notes)
- edge-label / variant-axis / H1-reuse / append-on-missing-slug / index-placeholder / concept_writes-on-existing-slug: 0 hits
- SUMMARY.md chapter registration / alphabetical-position insert: N/A — this report edits ONLY the three existing boundary-mode chapter BODIES + frontmatter; D1 sole-owns feature/index.md + feature/SUMMARY.md and already landed the boundary-mode index-cell delta + (D1 row) the SUMMARY entries. I did NOT touch index.md or SUMMARY.md.
- retroactive-budget: per-slice this report = 0 new (3 same-column promotion edits of EXISTING entries; a status/rank flip is a promotion, not a retroactive refinement-rewrite of settled content). Global aggregate is finalize's to assess across the staging log.

Open questions promoted:
- (none new) — the report's `## Open questions / caveats` are all D1-owned / coordination notes: `waveguide-mode-reduce-needs-l4-verb-home` was already promoted by D1 (confirmed present in scaffolding/open-questions.md, 1 occurrence, §header line 1430-ish); the Index/SUMMARY-ownership item + the whole-`feature/` sibling-status grep are integration-coordination notes (recorded below for finalize), not new questions.

Build-relevant: yes (touches book/src/feature/*.md — three chapter bodies + frontmatter)

Notes:
- BOTH-LAND COUPLING WITH D1 — RESOLVED THIS INVOCATION. D1's row (this log, line 38) flagged that D1 had landed the feature/index.md cells reflecting boundary-mode `firm` (firm-block 11→12 cols incl. boundary-mode; directive-scope line; seed-block now holding only waveguide-mode) on D2's behalf, leaving a transient state where the index cell LED the on-disk chapter body (still `seed`/`rough-in` per the apply-order D1→D3→D4→D5→D2). I (D2, LAST) flipped the three chapter bodies to `firm`, reconciling the pair. CONFIRMATION (on-disk, read this invocation): boundary-mode.L4.md frontmatter now reads `feature_root: seed` / `rank: firm`; the D1-owned feature/index.md (re-read this invocation) describes boundary-mode as `firm` at all touch-points — line 71 "cycle-117 cleared boundary-mode's own-readout gate ... promoting boundary-mode to `firm`. After cycle-117 only `waveguide-mode` remains `seed`"; line 78 driver-leaf cell "promoted `seed`→`firm` c117". The index cell and the chapter bodies now MATCH — no index-cell-drift. The both-land-or-both-defer pair is satisfied (both landed this cycle).
- CROSS-LINK RESOLUTION (forward-ref → live) — VERIFIED ON DISK. The three NEW cross-link targets `book/src/feature/waveguide-mode.{L4,L1,L0}.md` EXIST on disk (D1 created them this cycle — `ls` this invocation shows L4 11923B / L1 8843B / L0 6305B, mtimes 14:24-14:26, before this D2 apply). So the boundary-mode `[waveguide-mode](./waveguide-mode.{L4,L1,L0}.md)` links + the reciprocal `reference` frontmatter edges RESOLVE — finalize's `cargo make book` linkcheck2 will not fail on a missing anchor. The integration-ordering constraint the report flagged (D1 file-creation before D2 link-edits) is satisfied by the D1→…→D2 apply-order.
- PROMOTED-SIBLING CONVENTION verified: re-read book/src/feature/eigenmode.L4.md:5-6 this invocation — `feature_root: seed` (line 5) co-exists with `rank: firm` (line 6). boundary-mode now matches that convention (`feature_root: seed` KEPT, `rank: firm`, body `## Status` token `firm`). `feature_root: seed` is the permanent GC-root marker, NOT a maturity rung.
- REACHABILITY/RANK IMPACT: the promotion adds NO new garbage; boundary-mode is itself a feature-surface GC root (`kind: feature-surface`), trivially live. The new `reference` edges to waveguide-mode increase liveness of D1's new column (boundary-mode now has an inbound→waveguide-mode reference path). The authoritative rank/reachability re-measure is finalize step-5b (the linters) — recorded here, not re-run. No `depends-on` edge to a non-existent target (the waveguide-mode edges are `reference`, and the targets exist on disk).
- FINALIZE COORDINATION: re-run `grep -rn 'boundary-mode' book/src/feature | grep -E '\(\*?\*?seed\*?\*?\)'` after the full cycle integrates to confirm zero residual stale sibling-status mentions calling boundary-mode `(seed)` (D1's waveguide-mode chapters already describe boundary-mode's gate as cleared/promoted, per D1's row; no other on-disk feature/ file should call it `(seed)`).
- deferred integrated_at to finalize per role-spec (per-report integrator does not touch the consumed report's frontmatter).

---
