# Cycle-127 integrator staging log

Per-report integration rows, newest LAST (append-only). The row ORDER is the authoritative
apply-order record; `applied_at` is advisory only. integrator-finalize reads this log to
reconcile the cycle (build + commit + housekeeping).

---

## 2026-06-07T153621Z-layer-intro-author-matrix-free-column (D1 — the LEAD)
applied_at: 2026-06-07T155614Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/feature/matrix-free-operator.L4.md (new-file — firm L4 backend-lowering feature-surface column)
- book/src/feature/matrix-free-operator.L1.md (new-file — firm L1 pure-function composition-root)
- book/src/feature/index.md (edit — Infrastructure matrix row added, alpha-correct after krylov-iteration)
- book/src/feature/infrastructure.md (edit — 2 reference frontmatter edges + narrative member entry)
- book/src/SUMMARY.md (edit — 2 chapter rows under Infrastructure grouping, alpha-correct)
- book/src/L4/mk_matrix_free_operator.md (edit ×7 — cap firm-flip roadmap_goal→firm: frontmatter status/rank + reference→depends-on edge promotion + 2 banners + 4 section headers + the repairer's surgical :58 stale-edge-label fix)
- scaffolding/open-questions.md (append — 1 OQ promoted)

Gate hits:
- graded-ladder rank gate: 0 violations. Cap flip roadmap_goal→firm rests on depends-on dep L2/matrix-free-operator-apply (firm); rank(cap)=firm ≤ min(deps)=firm — legal. Both new firm column files: L4 depends-on {mk_matrix_free_operator (now firm), L2/matrix-free-operator-apply (firm)}; L1 depends-on {element_restrict, basis_apply, quad_point_contract, geom_factor_build — all firm}. All rank-legal. Critic independently verified every dep firm on disk.
- citecheck bounds + path-hygiene lint: 20 ok, 3 failing (all [AMBIG] on bare basenames operator.hpp / integrator.cpp / operator.cpp appearing in PROSE only; the load-bearing edge + signature citations carry fully-qualified palace/fem/libceed/... paths, all [ok]). No MISS/OOB. Non-blocking (critic verified the same; the qualified forms resolve).
- concept_writes on existing slug: n/a (no concept pages).
- SUMMARY.md chapter registration: report proposed the SUMMARY edits itself; applied as-given. No auto-fix needed.
- alphabetical-position insert: matrix-free-operator (m) sorts after krylov-iteration (k) within the Infrastructure grouping; the report's append-after-krylov placement (index matrix + SUMMARY + infrastructure.md narrative + frontmatter) is alpha-correct as-authored. No discretionary repositioning.
- new-SUMMARY-kind-grouping group-intro: n/a — the Infrastructure grouping + its group-intro (infrastructure.md) already exist; not a new grouping.
- deleted-slug frontmatter-edge sweep: n/a — no delete: blocks.
- residual-stale-framing grep (OQ-1 self-flagged + critic finding 2): ran `grep -n 'SPECULATIVE\|roadmap_goal\|speculative reconstruction\|not asserted as Palace\|reference.-class .lowers-to'` on the firmed cap post-apply — only 2 LEGITIMATE firm-era hits remain (the firm-flip banner :46 ending "now the *asserted* L4 form, not a speculative reconstruction" — the negation; and the :25 frontmatter comment "FIRMED it off roadmap_goal"). No stale roadmap_goal-era claim survives. The repairer's :58 surgical edit applied (reference-class lowers-to → depends-on (lowers-to)). OQ-1 cleared, finding-2 cleared.

Open questions promoted:
- matrix-free-operator-apply-l4-placeholder-now-stale (the L2 §"Speculative higher (L4) placeholder" :209-222 is now stale; out-of-scope L2 touch, low priority prose-drift)

(Report OQ-2 — the D2 forward-ref — is an integration-ordering note recorded below, not a standing question. Report OQ-1 — residual SPECULATIVE framing — was resolved during apply via the grep above. The "no new record" note needs no ledger entry.)

Build-relevant: yes (touches book/src/*.md — both new feature files + index/infrastructure/SUMMARY/cap).

Notes:
- FORWARD-REF FOR FINALIZE LINKCHECK (NON-BLOCKING per dispatch): both new L4 files AND the cap reference `book/src/L4-L3/mk-matrix-free-operator-dissolution.md` (reference-class — no rank/liveness coupling), which does NOT exist on disk yet. It is authored by D2 (reports/2026-06-07T153721Z-abstractor-matrix-free-dissolution, applied NEXT this same cycle). The forward-ref will resolve before finalize runs `cargo make book`; mdbook-linkcheck2 would hard-error if D2 did not land. Confirm D2 landed before the book build (the repairer confirmed D2 authors that exact slug + its SUMMARY.md row, co-batch).
- deferred integrated_at to finalize per role-spec (per-report integrator does not touch the consumed report's integrated_at / integration_commit frontmatter).
- The cap firm-flip's three gates (well-foundedness; composition-algebra exhaustively cited with no loop obstruction — firm-on-positive-structure escape; faithful root-reaching blocking depends-on pull from the new column) were all independently verified by the critic (plan-kind-consistency pass). NOT forced.
- RE11 grounding: the L1 column's four blocking depends-on (composes) edges to {element_restrict, basis_apply, quad_point_contract, geom_factor_build} + the cap's now-blocking depends-on chain to the L2 combinator form a genuine depends-on reachability flip from a feature root. Finalize/meta should run `graded-stack-lint --show-inbound` on the four substrate ops to confirm the RE11 libceed-substrate sub-cohort now grounds (per the report's RE11-grounding finalize-duty re-check).

---
## 2026-06-07T153721Z-abstractor-matrix-free-dissolution (D2 — the matrix-free constructive-interior L4>L3 theme)
applied_at: 2026-06-07T171200Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4-L3/mk-matrix-free-operator-dissolution.md (new-file — firm L4>L3 lowering theme: the matrix-free constructive-INTERIOR dissolution; RE11 libceed-substrate sub-cohort grounder)
- book/src/L4-L3/index.md (edit ×4 — [1] frontmatter reference: list insert; [2] §"Theme list" table row; [3] §"Vocabulary-cohort" Substantive-themes bullet; [4] Consolidated-tally 11→12 replace — all at the repairer-CORRECTED alpha slot)
- book/src/SUMMARY.md (edit — 1 chapter row under the # L4 > L3 Part, alpha-correct slot)
- scaffolding/open-questions.md (append — 1 OQ promoted)

Gate hits:
- graded-ladder rank gate: 0 violations. The new firm theme's 5 depends-on (composes) edges all target FIRM nodes — verified on disk: L2/matrix-free-operator-apply (rank firm), L1/element_restrict (firm), L1/basis_apply (firm), L1/quad_point_contract (firm), L1/geom_factor_build (firm). rank(theme)=firm ≤ min(deps)=firm — LEGAL. The reference-class edges (lowers → L4/mk_matrix_free_operator [now status:firm on disk, D1 flipped it]; sibling → L4-L3/fe-assemble-fold-dissolution; concepts/element-local-tensor [firm]; semantics/index; L4-L3/index) constrain no rank/liveness — correctly NOT depends-on. No flip-while-dep-unresolved. NOT forced.
- alphabetical-position insert: report (repairer-corrected) specified the slot; verified on disk before applying. # L4 > L3 grouping is strictly alpha — ksp-solve-driver-dissolution < mk-matrix-free-operator-dissolution < solve-family-map-dissolution (ksp < mk < solve). All 4 index inserts + the SUMMARY insert land at that single slot. Confirmed post-apply: index frontmatter lines 17/18/19 = ksp/mk/solve in order; SUMMARY between on-disk lines 103/104. No discretionary repositioning (report already alpha-correct after repair).
- citecheck bounds + path-hygiene lint: 16 ok, 2 failing — both [AMBIG] on bare basename `operator.cpp` appearing in PROSE (matches linalg/operator.cpp + fem/libceed/operator.cpp). The load-bearing forms are fully qualified `palace/fem/libceed/operator.cpp:182-189` and `:483` (inputs frontmatter + §Verified-against body), which resolve unambiguously; critic independently verified on-disk. No MISS/OOB. Non-blocking.
- SUMMARY.md chapter registration: report proposed the SUMMARY edit itself; applied as-given. No auto-fix needed.
- new-SUMMARY-kind-grouping group-intro: n/a — the # L4 > L3 Part + its index.md already exist; not a new grouping.
- implied-component stub materialization: n/a — all referents (LHS cap, L2/L1 deps, sibling theme, concept page) exist firm on disk.
- deleted-slug frontmatter-edge sweep: n/a — no delete: blocks.
- concept_writes on existing slug: n/a (no concept pages authored).

Open questions promoted:
- mk-matrix-free-dissolution-re11-grounding-recheck (finalize/meta duty: run graded-stack-lint --show-inbound on the 4 substrate ops to confirm RE11 grounds via this theme's faithful root-reaching depends-on inbound; match the reference_reachable climb node-for-node to the new firm theme + D1's firm column/cap)

Build-relevant: yes (touches book/src/*.md — the new theme chapter + L4-L3/index + SUMMARY).

Notes:
- D1 FORWARD-REF NOW RESOLVES. D1's STAGING.md row flagged a NON-BLOCKING forward-ref: D1's two new feature files + the firmed L4 cap carry a reference-class link to book/src/L4-L3/mk-matrix-free-operator-dissolution.md, which did not exist on disk at D1-apply time (the D1 linkcheck2 hazard). THIS report authored that exact file; it is now present on disk (verified: ls confirms the path created). The D1 forward-ref resolves before finalize runs cargo make book — the D1 linkcheck2 hazard is CLEARED.
- D2's own forward-refs resolve: the LHS link to L4/mk_matrix_free_operator (D1 landed it status:firm — verified on disk), the up-link to feature/matrix-free-operator.L4 (D1 landed it firm — verified on disk). D2's OQ-1 "D1 cap firm-flip dependency" is moot: the cap IS firm on disk, so the LHS reference link points at a firm node (no rank-0 fallback note needed).
- Report OQ "reverse-lift working note" is an abstractor working-note (explicitly NOT a formal-chapter / ledger item) — no ledger entry. Report OQ "per-term-loop-vs-per-geometry-loop nesting" is a critic-overlap disambiguator the critic resolved (scope statements partition cleanly) — no standing question.
- deferred integrated_at to finalize per role-spec (per-report integrator does not touch the consumed report's integrated_at / integration_commit frontmatter).
- The firm-theme verdict (DISSOLUTION-HOME, no interposed L3/mk_matrix_free_operator; firm-on-positive-structure) was the critic's plan-kind-consistency pass — NOT forced here. This integrator only verified the 5 depends-on deps are firm on disk for the rank gate + the alpha-slot correctness.

---
## 2026-06-07T153702Z-cross-layer-cross-cutter-geom-factor-shape (D3 — substrate↔combinator faithful-render re-align)
applied_at: 2026-06-07T173000Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/matrix-free-operator-apply.md (edit ×1 — surgical inline-annotation realign at :79: `quad_point_contract geom Q -- D :: [E,P,C] -> [E,P,C]` → `quad_point_contract geom -- D :: [E,P,C] -> [E,P,C']` with a "C' = test components, = C in the symmetric trial==test case" note; faithful-render to firm substrate signature L1/quad_point_contract.md:55)

Gate hits:
- citecheck bounds + path-hygiene lint: 13 ok, 3 failing — all 3 [AMBIG] on bare basename `integrator.cpp` (matches reference/palace/palace/fem/integrator.cpp AND .../fem/libceed/integrator.cpp); the report's prose + Supporting-evidence block disambiguate to the libceed file, and the cited ranges (:451-495 / :468-469 / :451-469) are in-range there (critic independently verified via codemap read_range). NO MISS/OOB. Path-hygiene nit only — non-blocking per role-spec.
- graded-ladder rank gate: n/a — no status/rank flip, no new/changed frontmatter edge (the report explicitly leaves the `depends-on (composes)` edge to quad_point_contract unchanged). Pure inline-prose realign inside an already-firm L2 chapter; rank/liveness untouched.
- edge-label / prose mismatch: n/a — this realign FIXES a substrate↔combinator render drift; it does not introduce one. The combinator's `depends-on (composes)` edge to quad_point_contract was already correct (the drift was inline-annotation-only, not an edge-label).
- forward-edge / variant-axis / H1-reuse / append-on-missing-slug / concept_writes / deleted-slug sweep / SUMMARY registration / alpha-insert / stub-materialization / group-intro: all n/a — single in-place edit to an existing chapter body; no new file, no SUMMARY/index touch, no slug created/deleted, no edge added.

Open questions promoted:
- (none) — the report's "Open questions / caveats" section carries only caveats (single-chapter low-blast-radius; the C'=C symmetric-case note already consistent with the combinator's symmetry law :113-122; no RE11/reachability interaction), plus the verify-before-applying D2 note recorded below. No standing question to add to the ledger.

Build-relevant: yes (touches book/src/L2/matrix-free-operator-apply.md — but the edit is inline prose inside a fenced code block; no link/heading/SUMMARY change, so linkcheck/TOC are unaffected. Rebuild is still warranted to render the corrected text.)

Notes:
- ON-DISK PRE-APPLY VERIFY: the :79 line read EXACTLY `|> quad_point_contract geom Q -- D :: [E, P, C] -> [E, P, C]  (pointwise, against [E, P, G])` before the edit (matches the report's OLD block verbatim — the report's verify-before-applying caveat is satisfied). Applied the realign; on-disk now reads `|> quad_point_contract geom -- D :: [E, P, C] -> [E, P, C'] (pointwise, against [E, P, G]; C' = test components, = C in the symmetric trial==test case)`.
- D2-SAME-DRIFT FLAG FOR FINALIZE/FOLLOW-UP (note-only per dispatch — D3 owns no D2 region, NOT edited here): D2's just-landed theme `book/src/L4-L3/mk-matrix-free-operator-dissolution.md:168` exhibits the SAME drift the report anticipated in its verify-before-applying caveat (report :178-182): it renders `|> quad_point_contract geomd Q -- D :: [(E, P, C)] -> [(E, P, C)]  (pointwise, against [(E, P, G)])` — i.e. (1) threads a run-time `Q` arg (should be pre-multiplied into `geomd` at build per quad_point_contract.md:61-65 + geom_factor_build.md:66-68), and (2) pins the `D` output to `C` rather than `C'` (the trial-in/test-out distinction L0 keys separately, integrator.cpp:468-469). This is the IDENTICAL faithful-render drift just corrected in the L2 combinator. Verified on-disk this invocation (grep of the D2 file). Recommend finalize (or a next-cycle lifter/critic-on-D2 follow-up) re-align D2:168 to `quad_point_contract geomd -- D :: [(E, P, C)] -> [(E, P, C')]` for substrate-faithfulness consistency. NOT applied here per the dispatch's "do NOT expand into D2's region" instruction.
- deferred integrated_at to finalize per role-spec (per-report integrator does not touch the consumed report's integrated_at / integration_commit frontmatter).

---
## 2026-06-07T153840Z-combinator-miner-inner-product-refactor (D4 — inner-product-family RE-style elimination)
applied_at: 2026-06-07T161223Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/dot.md (DELETE — standalone specialization-stub folded into inner_product §Specializations)
- book/src/L2/nrm2.md (DELETE — standalone consumer-stub folded into inner_product §Consumer)
- book/src/L3/dot.md (DELETE — standalone specialization-stub folded into combinator)
- book/src/L3/nrm2.md (DELETE — standalone consumer-stub folded into combinator)
- book/src/L3/inner_product.md (edit ×6 — §Specializations dot-fold provenance + L4/dot up-link; §tdot co-defined; §Consumer nrm2-fold provenance + L4/nrm2 up-link; §Consumers nrm2→in-section anchor; §Evidence 2 deleted-leaf items → self-section refs; §Downward-to-L2 precedent code-span re-point)
- book/src/L4/dot.md (edit ×3 — frontmatter depends-on L3/dot→L3/inner_product; body lift-link ×2 + §Evidence provenance item → ../L3/inner_product §Specializations anchor)
- book/src/L4/nrm2.md (edit ×3 — frontmatter depends-on L3/nrm2→L3/inner_product; body lift-links + §Evidence provenance item → ../L3/inner_product §Consumer anchor)
- book/src/L3/normalize.md (edit — frontmatter depends-on L3/nrm2→L3/inner_product; 11 body nrm2-link re-points → §Consumer anchor via sed)
- book/src/L3/orthogonalize.md (edit — frontmatter depends-on (composes) L3/dot→L3/inner_product; 6 body dot-link re-points → §Specializations anchor via sed)
- book/src/L2/normalize.md (edit — LEGACY consumes: frontmatter book/src/L2/nrm2.md→L2/inner_product [lint-caught silent dangler, NOT in report inventory]; body nrm2-link re-points via sed)
- book/src/L2/fold-family-stubs-intro.md (edit — frontmatter reference: L2/dot+L2/nrm2 → L2/inner_product+L2/linear_combination; full body rewrite to eliminated-stubs framing per report)
- book/src/L3/blas1-intro.md (edit — frontmatter reference: strike L3/dot+L3/nrm2; body links re-pointed to combinator anchors + elimination note)
- book/src/L2/divfree-projector.md, L2/reciprocal.md, L2/assemble-diagonal.md, L3/chebyshev.md, L3/reciprocal.md, L3/ksp_solve.md (edit — same-dir ./dot.md/./nrm2.md body-link re-points to combinator anchors via sed)
- book/src/L3-L2/orthogonalize-variant-split.md (edit — ../L3/dot.md + ../L2/dot.md body links re-pointed to combinator §Specializations anchors via sed)
- book/src/L4/index.md (edit — the mixed-link rows :52/:55/:112/:120: re-pointed ONLY the ../L3/dot.md / ../L3/nrm2.md substrings via sed; the ./dot.md / ./nrm2.md SURVIVOR self-links to kept L4/dot,L4/nrm2 left intact)
- book/src/SUMMARY.md (edit — struck 4 chapter entries: L3/dot, L3/nrm2, L2/dot, L2/nrm2; relabeled the now-empty L2 fold-family group to "Fold-family combinators (former stubs — eliminated)")
- book/src/L2/index.md (edit — STRUCK 2 dep-map rows [dot, nrm2] from the BLAS-1 vocab table; re-pointed the normalize-row nrm2 prose link → §Consumer anchor)
- book/src/L3/index.md (edit — STRUCK 2 dep-map rows [dot, nrm2]; re-pointed 3 prose links [obstruction-free-end list dot; normalize-row nrm2; orthogonalize-row dot] → combinator anchors)
- scaffolding/open-questions.md (append — 1 OQ: inner-product-combinator-section-anchor-stability)

Gate hits:
- deleted-slug FRONTMATTER-EDGE SWEEP (the new gate): RESIDUAL EDGES = 0. Pre-apply grep (typed `edges:` list-item + `target:` forms) found the 8 report-inventoried edges (4 re-point: L3/normalize:7, L3/orthogonalize:29, L4/dot:9, L4/nrm2:8 → L3/inner_product; 4 strike: fold-family-stubs-intro:8,9, blas1-intro:8,11). ALL applied. POST-apply: `grep -rnE '(depends-on|reference|...)\b(L2/dot|L2/nrm2|L3/dot|L3/nrm2)\b'` + the list-item form = ZERO residual. **graded-stack-lint --book-src caught ONE additional silent dangler the report inventory MISSED: `L2/normalize -> L2/nrm2` via the LEGACY `consumes:` frontmatter (full-path `book/src/L2/nrm2.md`, pre-graded-stack-typing form the typed-edge grep does not match).** Defensively re-pointed per the gate to L2/inner_product (the surviving consolidation target). Re-run lint: UNRESOLVED depends-on targets = 0. This is exactly the `deleted-slug-frontmatter-edge-gap` friction the gate guards — moved from finalize-time to per-report-time.
- graded-ladder RANK GATE: 0 violations (lint confirms "RANK VIOLATIONS: none"). All 5 re-pointed depends-on land on firm L3/inner_product (rank firm=3): L4/dot (firm→firm ✓), L4/nrm2 (firm→firm ✓), L3/normalize (firm→firm ✓), L3/orthogonalize (partial-obstruction ~2.5 ≤ firm 3 ✓), L2/normalize→L2/inner_product (firm→firm ✓). unresolved_depends_on_targets stays 0.
- citecheck bounds + path-hygiene: 57 ok, 1 failing — [MISS] `linalg/operator.cpp:598-617` in the report's §Supporting-evidence prose (line 410). The repairer qualified the bare basename to `linalg/operator.cpp` but the citecheck-resolvable path is `palace/linalg/operator.cpp` (relative-to-reference/), so --scan still flags MISS. NON-BLOCKING: this is a prose path-hygiene nit in the REPORT only (no book chapter carries this citation as a load-bearing claim — the referent is the already-firm inner_product L0 evidence anchor, present in the book at L2/L3 inner_product §Evidence as the fully-qualified `palace/linalg/operator.cpp:598-617`). The critic independently resolved it in-range under palace/linalg/. Not a MISS on any landed book content.
- cross-reference de-link (all 3 surfaces): body links + prose code-spans + frontmatter edges all swept. POST-apply: ZERO residual live `](./dot.md)`/`](./nrm2.md)` in L2/L3 dirs; ZERO residual `](../L2|L3/dot|nrm2.md)` anywhere. SURVIVOR INTEGRITY VERIFIED: L1/dot, L1/nrm2, L4/dot, L4/nrm2, concepts/dot, concepts/nrm2 all present; their `./`-relative SELF-links NOT re-pointed (the L4/index mixed-link rows had only the ../L3/* substring re-pointed; the L4/dot ./nrm2.md sibling self-link left intact).
- SUMMARY registration / mdBook duplicate-file: n/a deletions only — struck 4 entries; the now-childless L2 fold-family-stubs-intro group becomes a leaf chapter (valid mdBook; the intro file survives as a navigational container, single SUMMARY reference, no duplicate-file).
- alpha-insert / new-grouping group-intro / stub-materialization / H1-reuse / variant-axis: n/a (destructive consolidation, no new chapters/groupings/stubs).

Open questions promoted:
- inner-product-combinator-section-anchor-stability (latent build-fragility: ~30+ inbound links now depend on the two long combinator §-heading anchors staying verbatim; candidate follow-up = shorten headings in a single count-owner sweep — out of D4 scope)

Build-relevant: yes (4 deletions + ~20 book/src/*.md edits — book rebuild needed; the L2-fold-family SUMMARY group relabel + the 4 struck SUMMARY entries change the TOC).

Notes:
- FOR D5 (applied next) — L2/index dep-map count reconcile: I struck EXACTLY 2 L2/index dep-map rows from the BLAS-1 vocabulary table — `[`dot`](./dot.md)` (former :117) and `[`nrm2`](./nrm2.md)` (former :118). The surviving BLAS-1-cohort dep-map link-rows include `inner_product` and `linear_combination` (verified post-strike: `grep '^\| \[`(dot|nrm2)`\]' book/src/L2/index.md` = EMPTY). D5's L2/index firm-count reconcile subtracts these 2 firm rows. (I also struck 2 L3/index dep-map rows — dot :39, nrm2 :42 — but D5's dispatch is about the L2/index count.)
- RESIDUAL NON-BREAKING NARRATION (not re-pointed, by design — out of D4's load-bearing scope): several bare code-span (NOT live-link) references to `book/src/L2/dot.md` / `book/src/L3/nrm2.md` etc. remain in HISTORICAL-RECORD prose — the cycle-051 demotion-log bullets at L3-L2/index.md:42-68 and L2-L1/index.md:67-85, and a few §Evidence/§Provenance code-spans (L2/normalize.md:163, L3/normalize.md:157, orthogonalize-variant-split.md:293, L2/inner_product.md narrations, L2/elementwise_product.md:447). These are code-spans → do NOT break mdbook-linkcheck2; they are legitimate history narration describing what happened to those files. The load-bearing surfaces (live links + frontmatter edges + SUMMARY + index dep-map rows) are all clean. The two clearest survivor-file §Evidence provenance pointers (L4/dot.md, L4/nrm2.md) WERE re-pointed to the combinator §-anchors.
- The do-NOT-merge boundary HELD on apply: dot folded into §"Specializations", nrm2 into §"Consumer (NOT an instance)" — kept distinct; nrm2 NEVER moved into §Specializations. The combinator content already partitioned them (critic-verified); I only added elimination-provenance + the kept-L4-verb up-links.
- deferred integrated_at to finalize per role-spec (per-report integrator does not touch the consumed report's integrated_at / integration_commit frontmatter).

---
## 2026-06-07T154422Z-layer-intro-author-l2-index-count (D5 — L2/index firm-count prose reconcile, WAVE-2, dep D4)
applied_at: 2026-06-07T174500Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/index.md (edit ×3 — prose firm-count reconcile to the post-D4 self-summing dep-map row count: [1] :95 the authoritative current-state count line `23 firm`→`17 firm + 1 pc = 18 rows`; [2] the cycle-043 growth-log standing-count claim `dep-map now 22 rows = 21 firm + 1 pc`→annotated as-of-cycle-043 + forwarded to current 18 rows; [3] the cycle-052 "count is UNCHANGED = 22 rows" standing claim→annotated as-of-cycle-052 + superseded-by-deletion forward to current 18 rows)

Gate hits:
- INDEPENDENT FIRM-ROW COUNT (the load-bearing verification): I surveyed every dep-map table row on the LANDED tree by its trailing `## Status` cell (NOT prose). Post-D4 count = **17 firm + 1 partly-constructive (`deflate`) = 18 rows** — MATCHES D5's post-D4 arithmetic EXACTLY. Enumeration: Step kernels {chebyshev-iteration, correction_step, krylov-step} = 3 firm; Fold combinators {gram, inner_product, linear_combination} = 3 firm; Fold-family stubs grouping = EMPTY (header-only table at :113-117 — D4's 2 strikes of dot/nrm2 landed, confirmed); Named compositions {deflate=PC, eigsolve, incremental-least-squares, ksp_solve, orthogonalize} = 4 firm + 1 pc; Elementwise & gate floors {assemble-diagonal, divfree-projector, elementwise_product, jacobi-smoother, normalize, reciprocal} = 6 firm; Constructive-kernel {matrix-free-operator-apply} = 1 firm. Total firm = 3+3+4+6+1 = 17; pc = 1; rows = 18. NO discrepancy — applied as-authored.
- citecheck bounds + path-hygiene lint: n/a — the 3 edits introduce ZERO citations (pure count-prose reconcile); no MISS/AMBIG/OOB possible.
- graded-ladder rank gate: n/a — no status/rank flip, no frontmatter edge added/changed/deleted; rank/liveness untouched.
- edge-label / forward-edge / variant-axis / H1-reuse / append-on-missing-slug / concept_writes / deleted-slug frontmatter-edge sweep / SUMMARY registration / alpha-insert / new-grouping group-intro / stub-materialization: all n/a — three in-place prose edits inside an existing index body; no new file, no SUMMARY/index-row touch, no slug created/deleted, no edge.
- frozen-snapshot exclusion VERIFIED: the cycle-042 growth-log snapshot at :165 (`dep-map now 18 rows = 17 firm + 1 partly-constructive`) was correctly LEFT UNTOUCHED — it is a cycle-prefixed past-tense delta (`firm 12 → 17`), its old-string `18 rows` is distinct from Edit 2's `22 rows` (no ambiguous match), and its 18-rows figure coincidentally equals today's total but is a frozen historical record, not a standing-count claim. D5's NOT-reconciled note (report §"NOT reconciled") matches.

Open questions promoted:
- (none) — the report's Open-questions/caveats carries only the D5↔D4 ordering dependency (now SATISFIED — D4's 2 row strikes are on disk this invocation, verified by the empty Fold-family stubs table + my 17-firm count) and a prose-only scope note. Neither is a standing ledger question.

Build-relevant: yes (touches book/src/L2/index.md — prose-only inside an existing chapter; no link/heading/SUMMARY change, so linkcheck/TOC unaffected, but rebuild renders the corrected count text).

Notes:
- ON-DISK PRE-APPLY VERIFY (narrated from what I directly read this invocation, NOT an assumed sibling landing): the LANDED book/src/L2/index.md showed D4's 2 strikes already applied — the "Fold-family specialization / consumer stubs" dep-map table (:113-117) is HEADER-ONLY with zero rows (dot/nrm2 gone). All 3 D5 edit old-strings matched verbatim on disk despite line drift from D4's strikes (distinct regions — D4 struck dep-map rows, D5 edits prose at the count-line/growth-log surfaces). My independent firm-row count = 17, equal to D5's post-D4 expectation, so applied without discrepancy.
- The D4→D5 serial sequencing the planner intended HELD: D4 (immediately prior row above) struck the rows; D5 (this row) reconciles the prose to the now-true count. Prose and table now agree (18 rows = 17 firm + 1 pc).
- deferred integrated_at to finalize per role-spec (per-report integrator does not touch the consumed report's integrated_at / integration_commit frontmatter).

---
