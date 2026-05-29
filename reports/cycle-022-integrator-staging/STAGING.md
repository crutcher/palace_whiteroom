# cycle-022 integrator staging log

Per-report integration landings, newest LAST (append-only). Read by integrator-finalize to reconcile the cycle.

---

## 2026-05-29T071041Z-lowering-verifier-axpbypcz-firm
applied_at: 2026-05-29T07:38:10Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/axpbypcz-mutation-rotation.md (full-file replace: rough-in → firm; enacts cycle-021 callsite corrections 1-3 + correction-6 range 402-427 + appended `## Verified-against` header + fenced `verified_against:` yaml block; `## Status` flipped to firm)
- book/src/L1-L0/index.md (dep-map row 19 firm-flip: rough-in → firm; expanded L0-anchor cell + firm annotation "structural; 4 sub-patterns A/B/C/D; mixed-justification γ==0 algebraic sub-rule; B+D defined-not-used; sole γ≠0 path is A's real-real slow-path")
- scaffolding/open-questions.md (append-only: 3 resolution-record sections)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0
- SUMMARY.md chapter registration auto-fix: 0 (chapter already registered at SUMMARY.md:75 — this is a firm-flip of an existing rough-in, not a new file)
- index-placeholder displacement auto-fix: 0 (row 19 was a real rough-in row, not a placeholder)
- implied-component stub materialization: 0
- bookkeeping incomplete: 0

Count deltas:
- L1>L0 firm theme: +1 (axpbypcz-mutation-rotation rough-in → firm)
- BLAS-1 L1>L0 lowering floor: 7/8 → 8/8 (FULLY CLOSED) — dot, scal, nrm2, assemble-diagonal, axpby, axpbypcz all firm; last rough-in BLAS-1 L1>L0 theme firmed

Open questions promoted:
- axpbypcz-mutation-rotation-callsite-correction-and-firm-RESOLVED (resolves the Open blocker at open-questions.md:487; answer-link book/src/L1-L0/axpbypcz-mutation-rotation.md = firm)
- blas1-l1-l0-lowering-floor-CLOSED-8-of-8-axpbypcz-firm (resolves open-questions.md:25 `blas1-l1-l0-lowering-theme-gap` parent + :498 `blas1-l1-l0-lowering-floor-7-of-8-axpbypcz-remains`; answer-link book/src/L1-L0/index.md)
- axpbypcz-mutation-rotation-firm-direction-of-definition-clean (informational affirmation; high→low direction confirmed; no deliverable)
- (NOT re-opened: report OQ #3 MFEM add alias-safety already tracked at open-questions.md:519 `axpbypcz-mfem-add-alias-safety-carry`, Open, out-of-Palace-scope, unchanged; report OQ #4 axpby sibling naming already tracked at :505 `axpby-theme-covers-axpy-family-naming`, Open, sibling theme untouched by this dispatch)

Build-relevant: yes

Notes: Clean firm-flip; both `book/` edits applied verbatim (full-file chapter replace + surgical index row-19 match). Proposed-changes parsed cleanly (2 `edit:` fences); the report's `## Verified-against` header (repairer-inserted) + nested `yaml` block landed inside the chapter. All link targets (../L1/axpbypcz.md, ../L1/axpby.md, ../L1/axpy.md, axpby-mutation-rotation.md) confirmed existing; SUMMARY.md:75 registration confirmed pre-existing. No dead links, fences balanced, no auto-fixes/gate-hits. Correction-6 range 402-427 (not the cycle-021 draft's 402-429) was already folded into the report's firm body — no integrator carry-forward. Per role-spec, deferred `integrated_at:` (and `integration_commit:`) on the consumed report's frontmatter to integrator-finalize. Cross-cycle note for finalize: this report touches ONLY the L1-L0 layer; subsequent cycle-022 reports touch L1/index.md (firm count) — no shared-file collision expected. Book rebuild needed (book/src/*.md touched).

---

## 2026-05-29T071041Z-harvester-lu-solve-l1
applied_at: 2026-05-29T07:52:40Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/lu_solve.md (NEW firm chapter, full-file Write — small-dense direct solve `x = lu_solve(A, b)` of `A x = b` for a square dense `k×k` matrix via a pivoted factorization; leaf; firm-on-positive-structure per the apply_linop/apply_nonlinear_pencil precedent; contracted load-bearing-numerical factorization-kernel variant axis)
- book/src/L1/index.md (3 surgical edits: (1) cohort bullet inserted after `apply_nonlinear_pencil` bullet; (2) dep-map row inserted after `apply_nonlinear_pencil` row at :81; (3) Firm-count header `**Firm (13)**` → `**Firm (14)**` + extended the count-header gate-list with "the small-dense direct-solve gate")
- book/src/SUMMARY.md (chapter registration `- [lu_solve](./L1/lu_solve.md)` inserted after the `apply_nonlinear_pencil` L1 entry, line 71, inside the L1 Part before the `# L1 > L0` heading)
- scaffolding/open-questions.md (append-only: 4 sections — 1 resolution-record + 3 forward-flags)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (defer aggregate check to finalize)
- concept_writes on existing slug: 0 (lu_solve.md verified absent before Write — net-new file, no slug collision)
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0 (chapter H1 `# lu_solve` is the slug, not the L1 Part page heading)
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (3 variant axes enumerated + dispositioned: factorization-kernel contracted load-bearing, single/multi-RHS absorbed-as-form, element-type absorbed)
- SUMMARY.md chapter registration auto-fix: 0 (the report explicitly proposed the SUMMARY edit — applied as-proposed, no auto-fix needed)
- index-placeholder displacement auto-fix: 0 (no placeholder rows touched; index.md edits are real cohort/dep-map inserts + a count bump)
- implied-component stub materialization: 0 (the 3 forward-refs — deflate, gram, lu_solve-mutation-rotation — correctly stay PLAIN-TEXT, not stubbed: each is single-converging-reference / not-yet-shape-settled, below the clearly-implied-by-≥2 bar; verified absent on disk and verified rendered as plain text not live links in lu_solve.md)
- bookkeeping incomplete: 0

Count deltas:
- L1 firm operators: 13 → 14 (lu_solve NEW firm). On-disk Firm-count header now reads **Firm (14)**.
- L1 dep-map rows: 22 → 23 (lu_solve row added). 23 total = 14 firm + 9 rough-in (3 test-coverage-bounded/lower-layer + 6 obstruction).

Open questions promoted:
- lu-solve-l1-firm-landed-unblocks-deflate-gram (RESOLUTION-RECORD; resolves the Open blocker `deflate-needs-small-dense-lu-solve-primitive` at open-questions.md:569 + the compact plan-pointer at :34; answer-link book/src/L1/lu_solve.md = firm; meta-phase migrates the :569/:34 entries to Closed)
- lu-solve-mutation-rotation-l1-l0-theme-needed (future abstractor item — the L1>L0 lowering theme; forward-referenced plain-text in the firm chapter; plan candidate `lu-solve-mutation-rotation-l1-l0`)
- lu-solve-layer-intro-count-refresh-and-fifth-motif (layer-intro-author follow-up — count bump 13→14 applied here as the shared-file step; the §Semantics motif-framing refresh / candidate 5th "small-dense direct solve" motif deferred to layer-intro-author; repairer-routed)
- lu-solve-adjacent-future-leaves-prolongate-and-real-variant (two small forward-flags: the `MatVecMult(X, ·)` basis-expansion prolongation future L1 leaf; the unwitnessed real element-type variant)

Build-relevant: yes

Notes: Clean firm-on-positive-structure L1 operator landing (META overall_status: ready; repairer had corrected two annotative pinpoint drifts `:760-763`→`:762-764` and `:756`→`:754` directly in the CYCLE.md proposed-changes blocks pre-integration — those corrected ranges are what landed). Proposed-changes parsed cleanly (1 `new:` block + 2 `edit:book/src/L1/index.md` blocks + 1 `edit:book/src/SUMMARY.md` block). Verified pre-apply: lu_solve.md absent (net-new Write); the three forward-ref targets (book/src/L2/deflate.md, book/src/L2/gram.md, book/src/L1-L0/lu_solve-mutation-rotation.md) all absent — so the report's plain-text (no-live-link) forward-references are correct and MUST stay plain-text (a live link would be a linkcheck2 build break). Post-apply gates: lu_solve.md fence parity even (one balanced `text` Signature block); all 4 live relative links in lu_solve.md (./apply_linop.md, ./apply_nonlinear_pencil.md, ./assemble-diagonal.md, ./ksp_solve.md) resolve to existing siblings; index.md dep-map table intact (23 rows). SHARED-FILE NOTE for the next integrator (report 3 of 7, eigsolve flip): I left book/src/L1/index.md Firm-count header at **Firm (14)** on disk; the eigsolve flip takes it 14 → 15, then nleps_deflated_residual 15 → 16 — each should reconcile against the THEN-CURRENT on-disk value, NOT against a proposed-changes old_string that may still say 13/14. Per role-spec, deferred `integrated_at:` (and `integration_commit:`) on the consumed report's frontmatter to integrator-finalize. Book rebuild needed (book/src/*.md touched).

---

## 2026-05-29T071041Z-harvester-eigsolve-l1-firm
applied_at: 2026-05-29T08:58:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/eigsolve.md (3 surgical edits, ALL verbatim-matched on disk: (1) Algebraic-laws "Rough-in status caveat" → firm "Law character" positive-source rationale paragraph; (2) `## Status` section rough-in (test-coverage-bounded) → firm + retired-qualifier rationale + downstream-chain L3-partial-obstruction note; (3) Evidence — sharpened the `test-boundarymodeoperator.cpp` line + appended 10 new positive-source law anchors (slepc.cpp:497-509/470-481/483-495/828-835/551-554/273-274/694-695, arpack.cpp:463-473/603-610, + the apply_nonlinear_pencil/chebyshev-smoother precedent cross-links). repairer's sharpened slepc.cpp:273-274 descriptor landed as-is.)
- book/src/L1/index.md (SHARED FILE — 4 surgical edits reconciled against current on-disk state, NOT against proposed old_strings: (1) dep-map row line 73 eigsolve rough-in → firm (verbatim old_string matched — report 2 did not touch this row); (2) removed the eigsolve bullet from the §Vocabulary-cohort "Rough-in (test-coverage-bounded)" cohort; (3) inserted the firmed eigsolve bullet into the "Firm" cohort after the ksp_solve bullet (report's Edit-5 NEW text); (4) Firm-count header **Firm (14) → Firm (15)** reconciled against the on-disk value report 2 left, + extended the gate-list enumeration with "the eigenmode-solve gate")
- scaffolding/open-questions.md (append-only: 5 sections — 1 resolution-record (chain-step-1-done / L2-entry-unblocked) + 4 forward-flags (L3-still-blocked-predicted-partial-obstruction, source-read-confirmed-empirically-unwitnessed residual caveat, stale-cycle-009-narrative-routes-to-layer-intro-author, + the chain consolidation))

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (defer aggregate check to finalize)
- concept_writes on existing slug: 0 (this is a status flip on an existing chapter, no new slug)
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0 (no L_{n+1}→L_n edge carried; intra-L1 maturity flip)
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (4 live + 3 collapsed axes unchanged by the flip; firm verified to hold across all 4 backends)
- SUMMARY.md chapter registration auto-fix: 0 (eigsolve already wired at SUMMARY.md:63 — confirmed pre-existing; this is a status flip, not a new chapter)
- index-placeholder displacement auto-fix: 0 (no placeholder rows touched)
- implied-component stub materialization: 0 (no new forward-references introduced; the downstream-chain L2/L3 references are prose pointers to OQ-tracked future work, not dangling links)
- bookkeeping incomplete: 0

Count deltas:
- L1 firm operators: 14 → 15 (eigsolve rough-in (test-coverage-bounded) → firm). On-disk §Vocabulary-cohort Firm-count header now reads **Firm (15)**. Firm cohort bullet count verified = 15.
- L1 rough-in (test-coverage-bounded) cohort: 3 → 2 (eigsolve left; matrix-weighted-norm + bilinear-form remain).
- L1 dep-map rows: 23 → 23 (unchanged — eigsolve row 73 status flipped IN PLACE; no row added/removed). 23 = 15 firm + 2 rough-in(test-coverage-bounded) + 6 rough-in(obstruction).
- eigsolve prerequisite chain (per OQ `l3-eigsolve-blocked-on-l1-firm-and-l2-entry` `:613`): step 1 (L1 firm) DONE; step 2 (L2 entry) now UNBLOCKED; step 3 (L3 backfill) stays BLOCKED until L2 exists.

Open questions promoted:
- eigsolve-l1-firm-landed-chain-step-1-done-l2-entry-unblocked (RESOLUTION-RECORD; chain step 1 done; meta-phase re-frames the Open blocker at `:613` + marks plan candidate `eigsolve-l1-rough-in-to-firm` done / promotes `eigsolve-l2-entry` actionable; answer-link book/src/L1/eigsolve.md = firm)
- eigsolve-l3-backfill-still-blocked-predicted-partial-obstruction (forward-flag; does NOT supersede the structural finding `:624`; L1-firm does not change the L3 prediction)
- eigsolve-firm-source-read-confirmed-empirically-unwitnessed-residual-caveat (forward-flag, low-priority; the residual caveat survives the firm flip but does not gate it; test-eigensolver.cpp likely out of write-scope; consolidates with `:76`/chapter `:289`)
- eigsolve-firm-stale-cycle-009-narrative-bullet-routes-to-layer-intro-author (forward-flag; layer-intro-author follow-up per repairer finding-4 + META follow_up_agent; consolidate with `:658` for the whole-cohort prose refresh)

Build-relevant: yes

Notes: Clean rough-in→firm status flip on an existing 290-line chapter (META overall_status: ready; critic independently re-read every cited Palace body via codemap read_range and confirmed the flip SOUND — laws are positive-source syntactic identities, not convergence-semantics conjectures; all 8 critic checks pass; repairer findings 1-3 confined to report-prose self-verification / Evidence-anchor descriptor (none in the artifact-bound edit blocks except finding-3's sharpened slepc.cpp:273-274 descriptor which landed)). All 5 proposed `edit:` blocks parsed cleanly; the 3 eigsolve.md edits applied VERBATIM (all OLD strings matched on disk char-faithfully). SHARED-FILE RECONCILIATION (book/src/L1/index.md): report 2 (lu_solve) had left the Firm count at **Firm (14)** on disk; I reconciled the eigsolve flip against that current value → **Firm (15)** (NOT a blind apply of any stale proposed old_string — report's Edit blocks 4/5 were anchored on the rough-in-cohort placement, which I instead MOVED to the firm cohort + bumped the count surgically per the dispatch directive). The dep-map row (line 73) old_string matched verbatim (report 2 did not touch eigsolve's row). Post-apply gates: eigsolve.md fence parity even (4 markers = 2 balanced `text` blocks: Signature + verified_against yaml); index.md has no fences (pure prose+table, parity 0); all cross-links resolve (apply_nonlinear_pencil.md, chebyshev-smoother.md, ksp_solve.md, apply_linop.md all exist); SUMMARY.md:63 eigsolve registration confirmed pre-existing (no edit). No dead links, no new forward-references, no auto-fixes triggered. SHARED-FILE NOTE for the NEXT integrator (report 4 of 7, nleps_deflated_residual): I left book/src/L1/index.md Firm-count header at **Firm (15)** on disk; the nleps_deflated_residual landing takes it 15 → 16 — reconcile against the THEN-CURRENT on-disk **Firm (15)** value, NOT a stale proposed old_string. Per role-spec, deferred `integrated_at:` (and `integration_commit:`) on the consumed report's frontmatter to integrator-finalize. Book rebuild needed (book/src/*.md touched).

---

## 2026-05-29T071041Z-harvester-nleps-deflated-residual-l1
applied_at: 2026-05-29T09:42:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/nleps_deflated_residual.md (NEW firm chapter, full-file Write — the **deflated residual** of Palace's quasi-Newton NEP solver `QuasiNewtonSolver`: residual of the extended deflated problem of size `n + k`, `r = T(λ)·(vv + X·(λI−H)⁻¹·vv₂)`, `r₂ = Xᴴ·vv`, `norm = √(‖r‖²+‖r₂‖²)`; the deflation extension of `apply_nonlinear_pencil`, `k=0` degenerates to `apply_nonlinear_pencil` + `nrm2`; firm-on-positive-structure per the `apply_nonlinear_pencil` precedent; complex-only, variadic-in-`k`)
- book/src/L1/index.md (3 surgical edits, reconciled against CURRENT on-disk state: (1) Firm-count header `**Firm (15)** → **Firm (16)**` + extended the gate-list prose with "the NEP deflated-residual extension"; (2) Firm-cohort bullet inserted after the `apply_nonlinear_pencil` bullet, before the `lu_solve` bullet; (3) dep-map row inserted after the `apply_nonlinear_pencil` row, before the `lu_solve` row)
- book/src/SUMMARY.md (chapter registration `- [nleps_deflated_residual](./L1/nleps_deflated_residual.md)` inserted after the `apply_nonlinear_pencil` L1 entry, before the `lu_solve` entry — line 71, inside the L1 Part)
- scaffolding/open-questions.md (append-only: 3 sections — 1 resolution-record (firm landed + in-cycle `lu_solve`-dep caveat resolved) + 2 forward-flags (`nleps_deflated_solve` next-piece / L2-`deflate`-gram-positive-site; L1>L0 lowering theme))

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (defer aggregate check to finalize)
- concept_writes on existing slug: 0 (nleps_deflated_residual.md verified absent before Write — net-new file, no slug collision)
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0 (L1 operator entry; no L_{n+1}→L_n edge carried — the L1>L0 lowering is correctly deferred)
- H1 reuses page heading: 0 (chapter H1 `# nleps_deflated_residual` is the slug, not the L1 Part page heading)
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (deflation-present `k=0|k>0` + damping-present + committed-vs-trial axes enumerated; A2-representation/build-form/Mult-AddMult-split absorbed; the do-NOT-over-unify-with-L2-`deflate` guard present)
- SUMMARY.md chapter registration auto-fix: 0 (the report explicitly proposed the SUMMARY edit — applied as-proposed, no auto-fix needed)
- index-placeholder displacement auto-fix: 0 (no placeholder rows touched; index.md edits are real count-bump + cohort bullet + dep-map row)
- implied-component stub materialization: 0 (the forward-refs `deflate`/`gram` correctly stay PLAIN-TEXT — chapter files `book/src/L2/{deflate,gram}.md` verified absent on disk, below the clearly-implied-by-≥2 bar / not-yet-shape-settled; `lu_solve` was NOT a stub case — it already exists firm on disk, so it was UPGRADED to a live link, see Notes)
- bookkeeping incomplete: 0

Count deltas:
- L1 firm operators: 15 → 16 (nleps_deflated_residual NEW firm). On-disk §Vocabulary-cohort Firm-count header now reads **Firm (16)**; Firm-cohort bullet count verified = 16.
- L1 dep-map rows: 23 → 24 (nleps_deflated_residual row added). 24 = 16 firm + 2 rough-in(test-coverage-bounded: matrix-weighted-norm, bilinear-form) + 6 rough-in(obstruction).
- NEP-interior L1 atoms: 1 → 2 (apply_nonlinear_pencil + nleps_deflated_residual).

Open questions promoted:
- nleps-deflated-residual-l1-firm-landed (RESOLUTION-RECORD; the firm landing + the in-cycle resolution of the harvester's `lu_solve`-not-yet-firm caveat; answer-link book/src/L1/nleps_deflated_residual.md = firm; meta-phase marks plan candidate `nleps-deflated-residual-l1` done)
- nleps-deflated-solve-is-next-fan-out-ordered-nleps-piece-and-l2-deflate-gram-positive-site (forward-flag; the highest-fan-out next NLEPS harvest — `deflated_solve` lambda nleps.cpp:504-537 — which is the positive site firming the L2 `deflate`/`gram` combinator; plan candidate `nleps-deflated-solve-l1`)
- nleps-deflated-residual-l1-l0-lowering-theme-needed (forward-flag; future abstractor item — the L1>L0 mutation rotation; plan candidate `nleps-deflated-residual-mutation-rotation-l1-l0`)

Build-relevant: yes

Notes: Clean NEW firm L1 operator landing (META overall_status: ready; critic all-8-pass; the 3 repairer findings — conjugation arg-1/arg-2 disambiguation, `linear_combination` live-link upgrade, `else`-range `:571-574` — were surgical and pre-applied to the report's proposed-changes blocks, so the corrected text is what landed). Proposed-changes parsed cleanly (1 `new:` block + 1 `edit:book/src/SUMMARY.md` block + 1 `edit:book/src/L1/index.md` block describing 3 sub-edits). SHARED-FILE RECONCILIATION (book/src/L1/index.md Firm count): report 3 (eigsolve) left the Firm count at **Firm (15)** on disk; I reconciled the nleps_deflated_residual landing against that CURRENT value → **Firm (16)** (the report's proposed old_string said "Firm (13)→(14)", stale by two — NOT applied blindly; the surgical match was on the on-disk "Firm (15)" string). The cohort bullet + dep-map row were inserted relative to the on-disk `apply_nonlinear_pencil`/`lu_solve` anchors (both present — report 2 landed `lu_solve` earlier this cycle). IN-CYCLE `lu_solve` LIVE-LINK UPGRADE: the report was authored before `lu_solve` landed (same cycle, report 2 of 7), so it referenced `lu_solve` plain-text as "not-yet-firm vocabulary". Per the dispatch directive (`lu_solve` NOW EXISTS on disk → integrator MAY upgrade to a live link) and the harvester's own Open-question #1 (which anticipated exactly this mechanical follow-up), I upgraded all `lu_solve` cross-references in the chapter (Signature prose, Dependencies section, Status section, + added an Evidence line) and the dep-map dependency cell from plain-text to live links `./lu_solve.md`, and corrected the stale "not-yet-firm vocabulary" framing to "firm at L1 (harvested cycle-022)" — a mechanical in-cycle reconciliation against the report-2 landing, exactly analogous to the Firm-count reconciliation. The genuinely-absent forward-refs `deflate`/`gram` (chapter files `book/src/L2/{deflate,gram}.md` verified absent) correctly stay PLAIN-TEXT (a live link would be a `linkcheck2` break). Post-apply gates: nleps_deflated_residual.md fence parity even (4 markers = 2 balanced `text` blocks: Signature + Semantics); all 8 live-link targets resolve (apply_nonlinear_pencil.md, eigsolve.md, dot.md, nrm2.md, ksp_solve.md, lu_solve.md, ../L2/linear_combination.md, ../L0/eigensolver-wrapper.md); index.md dep-map intact (24 rows); SUMMARY ordering apply_nonlinear_pencil → nleps_deflated_residual → lu_solve clean within the L1 Part. No dead links, no auto-fixes/gate-hits. Per role-spec, deferred `integrated_at:` (and `integration_commit:`) on the consumed report's frontmatter to integrator-finalize. SHARED-FILE NOTE for the NEXT integrator (report 5 of 7): I left book/src/L1/index.md Firm-count header at **Firm (16)** on disk — any subsequent L1 firm landing this cycle should reconcile against the THEN-CURRENT on-disk value, NOT a stale proposed old_string. Book rebuild needed (book/src/*.md touched).

---

## 2026-05-29T071041Z-lifter-l3-citation-drift-sweep
applied_at: 2026-05-29T10:25:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L3/ksp_solve.md (8 surgical citation-digit edits, ALL old_strings matched verbatim on disk: `iterative.cpp:464`→`:463` ×3 — CG in-loop convergence-test point anchors at chapter lines 74/88/185; `iterative.cpp:564`→`:563` ×6 — GMRES restart-loop point anchors at lines 88/94/102/157/161/186. The body-range `:434-464` at line 185 intentionally kept as a range — `:464` there is the loop-body's legitimate closing-brace span endpoint, only the embedded convergence-test point corrected to `:463`. Entry stays firm: `firmness: firm` frontmatter + §Status `firm` untouched.)
- book/src/L2-L1/inner-product-fold-specialization.md (3 surgical citation-digit edits, ALL old_strings matched verbatim: `operator.cpp:623,632`→`:624,634` compound at chapter lines 141-142; inner `:623`→`:624` at line 415; SPD-assertion range `:615-616`→`:616` at lines 422-424. The embedded `verified_against` audit yaml block + `audit_caveat` (chapter lines 540-605) left VERBATIM — integrated append-only audit record; this dispatch ENACTS its caveat without mutating it. §Status `firm` untouched.)
- scaffolding/open-questions.md (append-only: 2 RESOLVED resolution-record sections — `l3-ksp-solve-citation-drift-463-563-correction`, `inner-product-fold-specialization-operator-cpp-inline-anchor-drift`)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (defer aggregate check to finalize)
- concept_writes on existing slug: 0 (no new slug — pure inline-anchor maintenance on two existing firm entries)
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0 (no edge label carried/changed; citation-digit-only deltas)
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (no variant-axis surface touched)
- SUMMARY.md chapter registration auto-fix: 0 (both entries already registered — ksp_solve at SUMMARY.md:30, inner-product theme at SUMMARY.md:51; confirmed pre-existing, no new chapter)
- index-placeholder displacement auto-fix: 0 (no index.md / placeholder touched)
- implied-component stub materialization: 0 (no forward-references introduced)
- bookkeeping incomplete: 0

Count deltas:
- NONE. Both target entries stay firm (no status flip). Pure citation re-anchor — 11 line-integer corrections (5 distinct drifts: iterative.cpp :464→:463, :564→:563; operator.cpp :623→:624, :632→:634, range :615-616→:616), 0 count delta, 0 new files, 0 status change.

Open questions promoted:
- l3-ksp-solve-citation-drift-463-563-correction (RESOLVED — the L3 ksp_solve :463/:563 fix; meta-phase close/migrate; answer-link book/src/L3/ksp_solve.md)
- inner-product-fold-specialization-operator-cpp-inline-anchor-drift (RESOLVED — the operator.cpp :624/:634/:616 fix; enacts the theme's own embedded cycle-021 audit_caveat; meta-phase close/migrate; answer-link book/src/L2-L1/inner-product-fold-specialization.md)

Build-relevant: yes

Notes: Clean pure-mechanical citation-drift sweep (META overall_status: ready; all 8 critic checks pass, no findings, no repairs — repair phase skipped per spec). Critic independently re-verified each of the 5 distinct corrections via tight `read_range` AND `tools/citecheck/citecheck.py --anchor` (`[DRIFT]` on each old line suggested exactly the new line) and confirmed all 8 untouched over-correction-guard anchors correct. All 11 `edit:` blocks parsed cleanly and matched on disk char-faithfully — no defer/reject, no auto-fixes triggered. NO SHARED-FILE COLLISION: this report touches ONLY book/src/L3/ksp_solve.md + book/src/L2-L1/inner-product-fold-specialization.md — disjoint from reports 1-4 this cycle (L1-L0/axpbypcz, L1/lu_solve, L1/eigsolve, L1/nleps_deflated_residual + their L1/index.md / SUMMARY.md touches) and from remaining reports 6 (creates L2-L1/orthogonalize-composition-lowering.md + L2-L1/index row) and 7 (L2/index.md prose). I did NOT touch book/src/L1/index.md — its on-disk Firm-count header remains **Firm (16)** as report 4 left it. Post-apply gates: no fences altered (citation-digit-only edits inside prose); no links added/removed/altered (new_strings differ from old_strings only in citation integers → no dead-link risk); both entries' firm status preserved (frontmatter + §Status verified unchanged). The inner-product theme's embedded `verified_against`/`audit_caveat` block (which documents these exact three operator.cpp drifts with the same target lines) was correctly left verbatim per the report — this dispatch ENACTS that already-recorded caveat. Per role-spec, deferred `integrated_at:` (and `integration_commit:`) on the consumed report's frontmatter to integrator-finalize. Book rebuild needed (book/src/*.md touched).

---

## 2026-05-29T071041Z-abstractor-orthogonalize-composition-lowering
applied_at: 2026-05-29T10:58:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2-L1/orthogonalize-composition-lowering.md (NEW firm L2>L1 theme, full-file Write — the variant-dispatch rotation for Gram-Schmidt orthogonalize-against-basis; lowers the firm L2 named composition `orthogonalize` (cycle-019) `project ▷ subtract` pipeline FORWARD into L1 by selecting, per variant `gs_orthog ∈ {MGS, CGS, CGS2}`, the batching+pass-count of the constituent `dot`/`axpy` L1 primitives — MGS `[dot,axpy]×m` interleaved / CGS `[dot×m, reduce, axpy×m]` separated / CGS2 `[CGS]×2` doubled; collective shape `m×1`/`1×m`/`2×m`; inner-product realization CITES `dot-mutation-rotation` §Sub-pattern D, not re-derived; in-place `w.Add` deferred to firm `orthogonalize-mutation-rotation` L1>L0; `algebraic` justification; both L1 RHS faces firm)
- book/src/L2-L1/index.md (1 surgical edit: dep-map firm row inserted after the `inner-product-fold-specialization` row — L2 anchor `L2/orthogonalize` (firm, cycle-019), L1 anchor `L1/orthogonalize` (firm leaf) + `L1/dot` + `L1/axpy`, status firm *(algebraic)*. The Part overview carries NO theme-count header, so no count to bump — the dep-map table now naturally shows 4 firm rows)
- book/src/SUMMARY.md (chapter registration `- [orthogonalize-composition-lowering](./L2-L1/orthogonalize-composition-lowering.md)` inserted after `inner-product-fold-specialization`, line 52, inside the `# L2 > L1 — Lowering` Part before the `# L1` heading)
- scaffolding/open-questions.md (append-only: 3 sections — 2 resolution-records (`orthogonalize-composition-lowering-l2-l1-theme-FIRM-LANDED` resolving the `:120` carry-forward OQ; `orthogonalize-mutation-rotation-l1-l0-theme-should-cite-dot-subpattern-d-DISCHARGED-ON-L2L1-SIDE` resolving the `:606` OQ on the L2>L1 side) + 1 forward-flag (`orthogonalize-composition-lowering-three-way-delegation-boundary-audit` — the lowering-verifier audit flag))

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (defer aggregate check to finalize)
- concept_writes on existing slug: 0 (orthogonalize-composition-lowering.md verified absent before Write — net-new file, no slug collision)
- forward-edge claim without surface: 0 (the L2→L1 forward edge IS the chapter surface; LHS firm L2, RHS firm L1 both sides)
- edge-label / prose mismatch: 0 (chapter narrates clean FORWARD L2→L1 throughout; the critic's edge-label `warning` was the reverse-direction caveat-bullet, which the repairer relocated OUT of the chapter fence into report-level working notes pre-integration — the published chapter is high→low compliant)
- H1 reuses page heading: 0 (chapter H1 `# orthogonalize-composition-lowering` is the slug, not the L2>L1 Part page heading)
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (the `gs_orthog ∈ {MGS, CGS, CGS2}` axis exhaustively covered with per-variant `[dot,axpy]` sequence + collective shape + source-witnessed body; the `dot`-hook axis canonical→B-weighted covered as closure substitution; Householder scoped out with cited rationale)
- SUMMARY.md chapter registration auto-fix: 0 (the report explicitly proposed the SUMMARY edit — applied as-proposed, no auto-fix needed)
- index-placeholder displacement auto-fix: 0 (the L2-L1/index.md edit is a real dep-map firm-row insert, not a placeholder displacement)
- implied-component stub materialization: 0 (no forward-references to not-yet-existing slugs introduced — every link target on both faces is firm-and-on-disk: L2/orthogonalize, L1/orthogonalize, L1/dot, L1/axpy, L1-L0/dot-mutation-rotation, L1-L0/orthogonalize-mutation-rotation, both sibling L2-L1 themes; no speculative not-yet-firm vocabulary, so nothing stayed plain-text)
- bookkeeping incomplete: 0

Count deltas:
- L2>L1 firm themes: 3 → 4 (chebyshev-iteration-fusion, linear-combination-fold-specialization, inner-product-fold-specialization, + orthogonalize-composition-lowering). On-disk dep-map firm-row count VERIFIED = 4. (NO Part-overview count header exists in L2-L1/index.md, so no count-bump edit was needed/possible — the table is the count surface.)
- orthogonalize lowering chain on the L2>L1 edge: COMPLETE (firm L2 `orthogonalize` → firm L1 leaf + `dot`/`axpy`; inner-product delegated to Sub-pattern D, in-place step to orthogonalize-mutation-rotation L1>L0).

Open questions promoted:
- orthogonalize-composition-lowering-l2-l1-theme-FIRM-LANDED (RESOLUTION-RECORD; resolves the Open carry-forward OQ `orthogonalize-composition-lowering-l2-l1-theme` at open-questions.md:120 — blocked on the L2 anchor since cycle-019, now firm; answer-link book/src/L2-L1/orthogonalize-composition-lowering.md = firm; meta-phase migrates :120 to Closed + marks plan candidate `orthogonalize-composition-lowering-l2-l1` done)
- orthogonalize-mutation-rotation-l1-l0-theme-should-cite-dot-subpattern-d-DISCHARGED-ON-L2L1-SIDE (RESOLUTION-RECORD on the L2>L1 side; resolves the L2>L1-side of the Open OQ at open-questions.md:606 — the `project` stage cites Sub-pattern D; the L1>L0-side residual stays with the un-authored `orthogonalize-mutation-rotation` theme; carries the load-bearing anchor note that this report's `orthog.hpp:35` is verified-correct and was NOT reverted to the stale `:34` in dot-mutation-rotation.md)
- orthogonalize-composition-lowering-three-way-delegation-boundary-audit (forward-flag; the standard lowering-verifier `verified_against:` audit + three-way delegation-boundary non-duplication confirmation — L2>L1 stage-selection ⟂ Sub-pattern D inner-product unfusing ⟂ orthogonalize-mutation-rotation in-place w.Add; plan candidate `orthogonalize-composition-lowering-verifier-audit`)

Build-relevant: yes

Notes: Clean NEW firm L2>L1 theme landing (META overall_status: ready; critic 7-of-8 pass + edge-label-fidelity `warning` RESOLVED by the repairer's pre-integration relocation of the reverse-direction L1→L2 lift caveat-bullet OUT of the chapter `new:` fence into the report-level §Open questions / caveats — so the published chapter body is strictly high→low forward-narration L2→L1, and the reverse-direction note will NOT land in the artifact). Proposed-changes parsed cleanly (1 `new:` block + 1 `edit:book/src/L2-L1/index.md` block + 1 `edit:book/src/SUMMARY.md` block). VERIFIED PER REPAIRER INSTRUCTION: this report's `palace/linalg/orthog.hpp:35` Sub-pattern D anchor (`IdentityInnerProduct::operator()` returns `LocalDot(x, y)`) landed AS AUTHORED (`:35`) — explicitly NOT reverted to the stale `:34` that appears in the neighbor `dot-mutation-rotation.md:160,183` (the `:34` drift is upstream and out of this dispatch's scope; the cycle-022 critic re-confirmed `:35` correct via codemap). Post-apply gates: orthogonalize-composition-lowering.md fence parity = 8 (EVEN — 4 balanced `text` blocks: L2-form Signature, Face-1 leaf, Face-2 dot/axpy, the variant-dispatch rewrite); all 8 relative cross-links resolve to existing files (../L2/orthogonalize.md, ../L1/orthogonalize.md, ../L1/dot.md, ../L1/axpy.md, ../L1-L0/dot-mutation-rotation.md, ../L1-L0/orthogonalize-mutation-rotation.md, ./linear-combination-fold-specialization.md, ./inner-product-fold-specialization.md) — the live link to the new file in the dep-map is OK (created this same batch); L2-L1/index.md dep-map firm-row count = 4 (the 3→4 delta verified on disk); SUMMARY ordering inner-product-fold-specialization → orthogonalize-composition-lowering clean within the L2>L1 Part. No dead links, no auto-fixes/gate-hits. NO SHARED-FILE COLLISION with the prior 5 cycle-022 reports: this report touches ONLY book/src/L2-L1/{orthogonalize-composition-lowering.md (new), index.md} + SUMMARY.md (a disjoint SUMMARY region — the L2>L1 Part, vs reports 2/4's L1-Part region; the two SUMMARY edits anchor on different lines and do not overlap). I did NOT touch book/src/L1/index.md — its on-disk Firm-count header remains **Firm (16)** as report 4 left it. Per role-spec, deferred `integrated_at:` (and `integration_commit:`) on the consumed report's frontmatter to integrator-finalize. Book rebuild needed (book/src/*.md touched).

---

## 2026-05-29T071041Z-layer-intro-author-l2-index-refresh
applied_at: 2026-05-29T08:05:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/index.md (3 surgical `edit:` blocks — navigational-prose refresh, NO firmness promotion: (1) dep-map `ksp_solve` row clause "theme `L3-L2/ksp-solve-outer-driver` pending" → live link `../L3-L2/ksp-solve-outer-driver.md` annotated "firm cycle-021"; (2) "Two stubs queued" Working Note → "One stub queued" + dropped now-firm `ksp_solve` bullet + added sibling "L2 outer-driver `ksp_solve` is now firm" note with live-linked `../L1/ksp_solve.md` / `./krylov-step.md` / `../L3-L2/krylov-step-body-identity.md` / `../L3/ksp_solve.md` / `../L3-L2/ksp-solve-outer-driver.md` cross-refs; (3) "L3 driver/kernel complementarity" Working Note → dropped stale "`L3/ksp_solve.md` not yet on disk" + "plain-text forward-reference pending" clauses, live-linked `../L3/ksp_solve.md` + `../L3/krylov-step.md` + `../L3-L2/ksp-solve-outer-driver.md`)
- scaffolding/open-questions.md (append-only: 3 closed-disposition resolution-record sections — `l2-index-working-note-staleness-l3-ksp-solve-on-disk-RESOLVED`, `L2-layer-intro-refresh-for-named-compositions-DISCHARGED`, `L2-layer-intro-refresh-for-fold-cohort-DISCHARGED`)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0 (critic edge-label-fidelity pass — all 3 edits narrate exactly the L2↔L1 / L3↔L2 edges the `ksp_solve` row carries)
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (no operator authored — navigational refresh)
- SUMMARY.md chapter registration auto-fix: 0 (no new chapter created; `L2/index.md` already registered)
- index-placeholder displacement auto-fix: 0 (no placeholder rows; all edits replace live prose)
- implied-component stub materialization: 0
- bookkeeping incomplete: 0

Count deltas:
- NONE — navigational-prose refresh only; firmness unchanged (L2 stays 6 firm + 1 stub). No new chapter, no firm-flip, no L0-citation change.

Pre-apply safety-net verification:
- All 3 `old_string` anchors matched the live `book/src/L2/index.md` byte-for-byte (critic-confirmed; re-read disk at apply per role-spec — `L2/index.md` was touched by NONE of the prior 6 cycle-022 reports, so the file at dispatch was unchanged).
- Newly-live-linked targets exist on disk + firm: `../L3/ksp_solve.md` (firm cycle-020), `../L3-L2/ksp-solve-outer-driver.md` (firm cycle-021), `../L3/krylov-step.md`, `../L1/ksp_solve.md`, `../L3-L2/krylov-step-body-identity.md` — all present (verified via `ls`).
- gram/deflate dep-map rough-in rows (`:54-55`) left UNTOUCHED as plain-text (no `book/src/L2/gram.md` / `book/src/L2/deflate.md` on disk — verified absent; correct per `rough-in-rows-must-be-plain-text-when-anchor-missing`).
- No fence changes (all 3 edits are inline clause/bullet replacements; index carries no code fences). No dead links.

Open questions promoted:
- l2-index-working-note-staleness-l3-ksp-solve-on-disk-RESOLVED (resolves the Open entry at open-questions.md:533; answer-link book/src/L2/index.md refreshed Working Notes + dep-map row; meta-phase to migrate to Closed index + mark plan candidate `l2-index-ksp-solve-prose-refresh` done)
- L2-layer-intro-refresh-for-named-compositions-DISCHARGED (discharges the meta-flag at open-questions.md:123; parent plan item `l2-named-composition-lifts` at :22 keeps only its `incremental-least-squares` stub→firm residue)
- L2-layer-intro-refresh-for-fold-cohort-DISCHARGED (discharges the meta-flag at open-questions.md:149; pairs with the named-compositions flag — meta-phase may fold both into one closed disposition)

Build-relevant: yes

Notes: Final wave-1 report (7 of 7). Navigational-prose-only refresh of `book/src/L2/index.md` — no firmness promotion, no L0-citation mutation, no count delta. META overall_status: ready (critic 7-of-8 pass; sole `skill-uptake-survey: warning` is non-blocking telemetry — citation-range + firmness-survey procedures done in substance but not slug-referenced; repairer recorded not-needed). The repairer corrected this report's META `verifies:` pointer (`../REPORT.md` → `./CYCLE.md`); no CYCLE.md change was needed for that. All 3 edits applied cleanly on a byte-for-byte anchor match. NO shared-file collision with the prior 6 cycle-022 reports (those touched L1-L0/, L1/, L3/, L2-L1/, SUMMARY.md, L3-L2/ — disjoint from `book/src/L2/index.md`). Per role-spec, deferred `integrated_at:` (and `integration_commit:`) on the consumed report's frontmatter to integrator-finalize. Book rebuild needed (book/src/L2/index.md touched). After this row, all 7 wave-1 reports are integrated; integrator-finalize runs after wave-2.

---

## 2026-05-29T080945Z-harvester-gram-l2-firm
applied_at: 2026-05-29T11:05:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/gram.md (NEW firm chapter, full-file Write — the **all-pairs `inner_product` fold** building the `k×k` Gram matrix `G = XᴴX` (entry `G[i,j] = inner_product(X[j], X[i]) = X[j]ᴴ X[i]`) from a `k`-column basis `X`; matrix-valued lift of the firm L2 scalar fold `inner_product`; firm-on-positive-structure per the cycle-021 `apply_nonlinear_pencil`/`apply_linop` precedent — every law is a syntactic identity on the firm `inner_product` fold; sole literal Gram-build site `nleps.cpp:524-531`)
- book/src/L2/index.md (2 surgical edits: (1) dep-map gram row-substitution `:54` rough-in → firm + live link `[gram](./gram.md)` (the orchestrator-completed firm row, critic-verified faithful; old rough-in row old_string matched verbatim on disk — the wave-1 layer-intro-author L2-index refresh did NOT touch this row, confirmed in its staging row); (2) §Vocabulary-cohort "Firm at L2" list +1 bullet `gram` after the `ksp_solve` bullet)
- book/src/SUMMARY.md (chapter registration `- [gram](./L2/gram.md)` inserted after the `ksp_solve` L2 entry (line 45), inside the L2 Part before the `# L2 > L1` heading — AUTO-FIX: the report did NOT propose a SUMMARY edit, so the per-report SUMMARY.md-chapter-registration gate added it to preserve sidebar discoverability)
- scaffolding/open-questions.md (append-only: 3 sections — 1 resolution-record (`gram-l2-firm-landed-unblocks-deflate-firm-and-nleps-deflation-lowering`) + 1 low-priority coverage caveat (`gram-l2-coverage-caveat-single-gram-build-site`) + 1 forward-flag (`gram-l2-l1-lowering-theme-double-dot-loop-fusion`))

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (defer aggregate check to finalize)
- concept_writes on existing slug: 0 (gram.md verified absent before Write — net-new file, no slug collision)
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0 (L2 operator entry; no L_{n+1}→L_n edge carried — the L2>L1 lowering correctly deferred)
- H1 reuses page heading: 0 (chapter H1 `# gram` is the slug, not the L2 Part page heading)
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (3 variant axes enumerated — `dot` hook ∈ {canonical, B-weighted}, single-set vs cross-Gram, element-type — + 2 scoped-out with rationale: symmetry-exploitation transparent-perf-trick, basis cardinality `k` as fold parameter)
- SUMMARY.md chapter registration auto-fix: 1 (the report's blocks did NOT include a SUMMARY edit; per the gate I added `- [gram](./L2/gram.md)` under the L2 Part after `ksp_solve` — new chapter must be registered for sidebar discoverability; rationale: existing-pattern-preservation, every L2 chapter is SUMMARY-registered)
- index-placeholder displacement auto-fix: 0 (the gram dep-map row was a real cycle-021 rough-in row, not a `(empty — Phase B skeleton.)` placeholder; row-substituted in place)
- implied-component stub materialization: 0 (the `deflate` forward-reference correctly stays PLAIN-TEXT — `book/src/L2/deflate.md` verified absent on disk; it is the parallel wave-2 report-2 sibling landing next, so plain-text is the build-safe choice per `rough-in-forward-reference-must-be-plain-text-not-live-link`; a live link would be a linkcheck2 break)
- bookkeeping incomplete: 0

Count deltas:
- L2 firm combinators: 6 → 7 (gram NEW firm). On-disk §Vocabulary-cohort "Firm at L2" bullet count verified = 7; dep-map firm-row count verified = 7 (krylov-step, chebyshev-iteration, linear_combination, inner_product, orthogonalize, ksp_solve, + gram).
- L2 dep-map rough-in rows: 2 → 1 (only `deflate` remains rough-in — the parallel wave-2 sibling).

Open questions promoted:
- gram-l2-firm-landed-unblocks-deflate-firm-and-nleps-deflation-lowering (RESOLUTION-RECORD; the firm landing unblocks the L2 `deflate` firm gate on the `gram` constituent — all `deflate` constituents now firm except the `:583` single-algorithm-concentration scope review; also unblocks the NLEPS deflation L2>L1 lowering; meta-phase migrates the `:35` plan-pointer + `:418` source OQ `gram` halves to Closed, marks the `deflate-gram-harvester-firm` `gram` deliverable done; answer-link book/src/L2/gram.md = firm)
- gram-l2-coverage-caveat-single-gram-build-site (low-priority coverage caveat, NOT a status reduction — single literal `XᴴX` Gram-build site `nleps.cpp:524-531` + no dedicated NLEPS test; same posture as `inner_product`'s `tdot` caveat; pairs with the `:583` `deflate` scope review; promotion-to-closed on a second Gram site or a dedicated test)
- gram-l2-l1-lowering-theme-double-dot-loop-fusion (forward-flag; future abstractor item — the L2>L1 lowering theme: how the all-pairs fold lowers onto the `nleps.cpp:524-531` double-`linalg::Dot` loop, the per-cell `dot`-leaf dispatch + symmetry-exploitation transparent note + per-cell reduction-tree IEEE non-law; plan candidate `gram-fold-specialization-l2-l1`, sibling to the firm `inner-product-fold-specialization` it lifts)

Build-relevant: yes

Notes: Clean NEW firm L2 combinator landing (META overall_status: ready; critic 7-of-8 pass + non-blocking `skill-uptake-survey: warning`; repairer finding-3 — PSD law-4 attribution as the matrix lift of `inner_product` law 5 via sesquilinearity law 3 — was pre-applied to the report's `new:` block, so the corrected body is what landed). Proposed-changes parsed cleanly (1 `new:book/src/L2/gram.md` block + 1 `edit:book/src/L2/index.md` row-substitution block). The `edit:book/src/L2/index.md` block was the orchestrator-completed firm row (transient API 529 truncated the original final block); critic Issue-1 verified the completion FAITHFUL to the chapter content (signature/dependency/status cells all consistent) — applied as a row-substitution against the on-disk cycle-021 rough-in gram row (`:54`), NOT an append, per the surgical-row-replace convention used by the landed `ksp_solve`/`inner_product` index edits. The report did NOT propose a SUMMARY edit → I added the `- [gram](./L2/gram.md)` registration under the L2 Part myself (SUMMARY.md-chapter-registration auto-fix; every L2 chapter is registered). Pre-apply verification: gram.md absent (net-new Write); deflate.md absent (so the `deflate` forward-ref MUST stay plain-text — verified no `[deflate](./deflate.md)` live link anywhere in the chapter); inner_product.md / orthogonalize.md / ../L1/dot.md all present (the 3 live cross-links resolve). Post-apply gates: gram.md fence parity even (2 markers = 1 balanced `text` Signature block); the 3 relative live links resolve (./inner_product.md, ../L1/dot.md, ./orthogonalize.md); index.md dep-map intact (8 rows: 7 firm + 1 rough-in `deflate`); §Vocabulary-cohort Firm-at-L2 bullet count = 7. No dead links, no other auto-fixes/gate-hits. Per role-spec, deferred `integrated_at:` (and `integration_commit:`) on the consumed report's frontmatter to integrator-finalize. CONFIRMED FOR NEXT INTEGRATOR (wave-2 report 2 of 2, `deflate`): `book/src/L2/gram.md` now EXISTS firm on disk — the `deflate` chapter's `gram` references MAY be upgraded from plain-text to live link `[gram](./gram.md)` at that apply (the in-cycle live-link-upgrade analogue of report-4's `lu_solve` upgrade). The `deflate` dep-map row (`book/src/L2/index.md:55`) is the only remaining L2 rough-in row, left untouched. Book rebuild needed (book/src/*.md touched).

---

## 2026-05-29T080945Z-harvester-deflate-l2-firm
applied_at: 2026-05-29T11:18:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/deflate.md (NEW `partly-constructive` chapter, full-file Write — the L2 named-composition **oblique / Galerkin complementary projector** `deflate(X, v) = v − X·(coords-solve)` removing the deflation subspace `span(X)`; the `coords ▷ schur-solve ▷ back-project` pipeline over `gram` + `lu_solve` + `linear_combination` + `dot`. Firm Schur-form pipeline on positive site `nleps.cpp:505-537`; constructive bare-Galerkin core `I − X(XᴴX)⁻¹Xᴴ` (S=I degenerate case) from literature + negative anchor; promotion-to-firm gate = a positive Palace Galerkin-deflation source site. Over-unification guard vs `orthogonalize` first-class. IN-CYCLE LIVE-LINK UPGRADE applied: all `gram` references upgraded from the report's plain-text `<!--rough-in-->` to live link `[gram](./gram.md)` since `book/src/L2/gram.md` landed firm earlier this wave-2 — see Notes.)
- book/src/L2/index.md (2 surgical edits: (1) dep-map deflate row-substitution `:56` rough-in → `partly-constructive` + live link `[deflate](./deflate.md)`, with the report's `edit:` firm-substitution row applied AND its `gram` constituent-cell ref upgraded to `[gram](./gram.md)` + `lu_solve` to `[lu_solve](../L1/lu_solve.md)` (the repairer-refreshed live link, since lu_solve is firm); old rough-in row old_string matched verbatim on disk; (2) §Vocabulary-cohort NEW **Partly-constructive at L2** tier inserted before the Queued/stub tier, carrying the `deflate` bullet with firm/constructive split + promotion condition + over-unification guard. **Firm-at-L2 count UNCHANGED at 7** — deflate is partly-constructive, NOT firm.)
- book/src/SUMMARY.md (chapter registration `- [deflate](./L2/deflate.md)` inserted after the `gram` L2 entry (line 47), inside the L2 Part before the `# L2 > L1` heading — AUTO-FIX: the report did NOT propose a SUMMARY edit, so the per-report SUMMARY.md-chapter-registration gate added it to preserve sidebar discoverability)
- scaffolding/open-questions.md (append-only: 3 sections — 1 landing resolution-record + promotion-gate (`deflate-l2-partly-constructive-landed-promotion-gates-on-positive-galerkin-site`), 1 forward-flag (`deflate-l2-l1-lowering-theme-needed`), 1 consolidation/progress-marker (`nleps-deflation-lowering-chain-substantially-anchored-post-cycle-022`))

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (defer aggregate check to finalize)
- concept_writes on existing slug: 0 (deflate.md verified absent before Write — net-new file, no slug collision)
- forward-edge claim without surface: 0 (L2 operator entry; the forthcoming L2>L1 lowering correctly deferred plain-text)
- edge-label / prose mismatch: 0 (no L_{n+1}→L_n edge carried; the L2 named composition de-fuses the L0 block, narrated correct direction)
- H1 reuses page heading: 0 (chapter H1 `# deflate` is the slug, not the L2 Part page heading)
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (central `op.block ∈ {Galerkin, Schur}` axis = the partly-constructive hinge, + `op.dot` hook, element-type, in-place/out-of-place — all enumerated per classify-variant-axis contract)
- SUMMARY.md chapter registration auto-fix: 1 (the report's blocks did NOT include a SUMMARY edit; per the gate I added `- [deflate](./L2/deflate.md)` under the L2 Part after `gram` — new chapter must be registered for sidebar discoverability; rationale: existing-pattern-preservation, every L2 chapter is SUMMARY-registered)
- index-placeholder displacement auto-fix: 0 (the deflate dep-map row was a real cycle-021 rough-in row, not a `(empty — Phase B skeleton.)` placeholder; row-substituted in place)
- implied-component stub materialization: 0 (the only forward-reference — the L2-L1/deflate-composition-lowering theme — correctly stays PLAIN-TEXT: that chapter is genuinely not-yet-existing future abstractor work; `gram` was NOT a stub case — it already exists firm on disk, so it was UPGRADED to a live link, see Notes)
- bookkeeping incomplete: 0

Count deltas:
- L2 firm combinators: 7 → 7 (UNCHANGED — `deflate` lands `partly-constructive`, NOT firm). On-disk §Vocabulary-cohort "Firm at L2" bullet count verified = 7.
- L2 partly-constructive combinators: 0 → 1 (`deflate` NEW; new tier created in the cohort section).
- L2 dep-map rough-in rows: 1 → 0 (deflate was the LAST rough-in row — cohort fully drained). Dep-map now 9 rows = 7 firm + 1 partly-constructive (`deflate`) + 1 stub (`incremental-least-squares`).

Open questions promoted:
- deflate-l2-partly-constructive-landed-promotion-gates-on-positive-galerkin-site (RESOLUTION-RECORD for the landing + Open promotion-to-firm gate; meta-phase migrates the `:35` plan-pointer + `:418` source OQ `deflate` halves to Closed with answer-link book/src/L2/deflate.md, keeps the positive-Galerkin-site gate Open + the `:583` scope review folded in)
- deflate-l2-l1-lowering-theme-needed (forward-flag; future abstractor item — the L2>L1 lowering; plan candidate `deflate-composition-lowering-l2-l1`)
- nleps-deflation-lowering-chain-substantially-anchored-post-cycle-022 (consolidation/progress-marker; the NLEPS deflation cohort is now substantially-firm L1/L2 vocabulary — remaining work is lowering-completion + the deflate promotion gate, ranked by fan-out for the planner)

Build-relevant: yes

Notes: Clean NEW `partly-constructive` L2 combinator landing (META overall_status: ready; critic 7-of-8 pass + cross-reference-integrity `warning` RESOLVED by the repairer's pre-integration `lu_solve` dep-cell live-link refresh — the orchestrator-completed `edit:book/src/L2/index.md` row's stale "NOT yet vocabulary; candidate L1 leaf, OQ below" phrase was already fixed to `[lu_solve](../L1/lu_solve.md)` (L1, firm cycle-022) in the report's CYCLE.md before this apply, so the firm live link is what landed). Proposed-changes parsed cleanly (1 `new:book/src/L2/deflate.md` block + 1 `edit:book/src/L2/index.md` row-substitution block; the report did NOT propose a SUMMARY edit). The `partly-constructive` judgment is SOUND (critic re-read the full positive Schur pipeline via read_range + both negative anchors via search_text + all cross-artifact citations line-exact): the three-part invariant is satisfied (which sub-part is constructive = bare-Galerkin core + laws 3-5; negative-anchor citations = literature `:354-362` + the no-bare-Gram-solve search_text; promotion condition = a positive Galerkin source site). KEY IN-CYCLE LIVE-LINK UPGRADE (the load-bearing apply directive): the report was authored before `gram` landed (same wave-2, report 1 of 2 landed `book/src/L2/gram.md` firm), so it referenced `gram` plain-text with `<!--rough-in-->` markers throughout the chapter body (intro, Algorithm-table over-unification row, Dependencies, coords-solve narration) + the dep-map row. I verified `book/src/L2/gram.md` EXISTS firm on disk, then upgraded ALL link-bearing `gram` references to live links `[gram](./gram.md)` and removed every `<!--rough-in-->` marker (grep confirms 0 residual rough-in markers) — exactly the report-2 `lu_solve` / report-4 `lu_solve` in-cycle upgrade pattern. The remaining bare-backtick `` `gram` `` instances in the chapter are prose mentions (inline-code in narrative sentences, not markdown links) — correct to leave as inline code. Pre-apply verification: deflate.md absent (net-new Write); gram.md present (so the upgrade is build-safe). Post-apply gates: deflate.md fence parity EVEN (4 markers = 2 balanced `text` blocks: Signature + coords-solve); ALL 10 relative link targets resolve (./gram.md, ./inner_product.md, ./linear_combination.md, ./orthogonalize.md, ../L1/dot.md, ../L1/lu_solve.md, ../L1/ksp_solve.md, ../L1/nleps_deflated_residual.md, ../../../scaffolding/priorities.md, ../../../skills/classify-variant-axis/SKILL.md); index.md dep-map intact (9 rows, 0 rough-in remaining), all 15 index link targets resolve including the new ./deflate.md; SUMMARY ordering gram → deflate clean within the L2 Part. No dead links, no other auto-fixes/gate-hits. SHARED-FILE NOTE: this report touches book/src/L2/{deflate.md (new), index.md} + SUMMARY.md (L2-Part region, after `gram`). The wave-2 report 1 (`gram`) touched the same L2/index.md + SUMMARY L2 region — I re-read both at this apply: the gram firm row (index.md:59) + the gram SUMMARY entry (:46) + the §Vocabulary-cohort 7-firm gram bullet were all present from report 1, and my deflate edits anchor on the (then-current) on-disk rough-in deflate row + insert AFTER the gram tier/entry. No collision. I did NOT touch book/src/L1/index.md (its Firm-count header remains **Firm (16)** as report 4 left it — this is an L2 landing). Per role-spec, deferred `integrated_at:` (and `integration_commit:`) on the consumed report's frontmatter to integrator-finalize. This is the FINAL report of cycle-022 (wave-2 report 2 of 2) — after this row all cycle-022 reports (7 wave-1 + 2 wave-2 = 9 total) are integrated; integrator-finalize runs next (book rebuild + commit + housekeeping). Book rebuild needed (book/src/*.md touched).

---
