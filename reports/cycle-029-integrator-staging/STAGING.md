# Cycle-029 integrator-per-report staging log

This is the per-cycle staging log appended to by each `integrator-per-report`
dispatch as it serially applies one report's proposed-changes. `integrator-finalize`
reads this log at cycle end to reconcile the batch (rebuild book, repair build
breakage, mark consumed reports' `integrated_at`, write log/cycle-N.md, append to
cycle-record.jsonl + integrator-signals.md, batch CYCLE.md, single commit + push).

Newest entries LAST (append-only).

---

## 2026-05-29T205945Z-abstractor-back-solve-mutation-rotation
applied_at: 2026-05-30T00:11:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/back-solve-mutation-rotation.md (created — firm L1>L0 theme)
- book/src/L1-L0/index.md (dep-map row insert between `normalize-mutation-rotation` and `nleps-deflated-residual-mutation-rotation`)
- book/src/SUMMARY.md (chapter registration between `normalize-mutation-rotation` and `lu-solve-mutation-rotation`)
- scaffolding/open-questions.md (appended 5 OQs: back-solve-law-6-leaf-prose-tightening-c029, back-solve-mutation-rotation-cycle-030-verified-against-audit-c029, back-solve-mutation-rotation-l2-l1-incremental-least-squares-boundary-c029, back-solve-mutation-rotation-empty-cycle-j-minus-one-reachability-c029, back-solve-mutation-rotation-reduction-order-section-promotion-stylistic-c029)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (this report)
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0
- bookkeeping incomplete: 0
- citecheck (--scan on applied chapter): 33 ok, 0 failing
- citecheck (--scan on source report): 41 ok, 0 failing
- SUMMARY.md chapter registration auto-fix: not-applied (report's edit explicitly registered)

Open questions promoted:
- back-solve-law-6-leaf-prose-tightening-c029
- back-solve-mutation-rotation-cycle-030-verified-against-audit-c029
- back-solve-mutation-rotation-l2-l1-incremental-least-squares-boundary-c029
- back-solve-mutation-rotation-empty-cycle-j-minus-one-reachability-c029
- back-solve-mutation-rotation-reduction-order-section-promotion-stylistic-c029

Build-relevant: yes

Notes: First per-report integration of cycle-029 (this STAGING.md is freshly created).
The report applied cleanly with all critic checks pass + zero repair needed
(overall_status: ready). The producer's emit-time `citecheck --anchor`
self-verification of the FGMRES +1-brace-shift hazard worked as intended; the
post-apply `--scan` of the chapter on disk confirms 33/33 citations zero-drift.
The cycle-024 `convert-nested-fences-to-indented-code-in-proposed-changes-block`
defensive idiom was used (4-space-indented inner code, no nested triple-backtick
fences) — the `new:` block parsed cleanly as a single literal write. The 5 OQs
promoted are appropriate downstream-hand-off notes (no defects); the cycle-030
verified_against audit is the standard sibling-theme follow-up. deferred
`integrated_at:` to finalize per role-spec (per-report integrator does NOT touch
report frontmatter). This applies BEFORE the in-cycle report-4 trsv-obstruction
theme so its plain-text reference to `back-solve-mutation-rotation` can be
upgraded by report-4's integrator to a live link.

---

## 2026-05-29T205945Z-abstractor-bilinear-form-mutation-rotation
applied_at: 2026-05-30T00:35:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/bilinear-form-mutation-rotation.md (created — firm L1>L0 theme, off-diagonal sibling of matrix-weighted-norm-mutation-rotation)
- book/src/L1-L0/index.md (dep-map row insert immediately after `matrix-weighted-norm-mutation-rotation`, before `normalize-mutation-rotation`)
- book/src/SUMMARY.md (chapter registration immediately after `matrix-weighted-norm-mutation-rotation`, before `normalize-mutation-rotation`)
- scaffolding/open-questions.md (appended 4 OQs: bilinear-form-mutation-rotation-cycle-030-verified-against-audit-c029, bilinear-form-l0-surface-comment-callout-polish-c029, bilinear-form-l2-weighted-inner-product-reduction-combinator-c029, bilinear-form-l1-entry-upstream-variant-axis-coverage-gaps-c029-tracking)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (this report)
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0
- bookkeeping incomplete: 0
- citecheck (--scan on applied chapter): 19 ok, 0 failing
- citecheck (--scan on source report): 20 ok, 0 failing
- SUMMARY.md chapter registration auto-fix: not-applied (report's edit explicitly registered)

Open questions promoted:
- bilinear-form-mutation-rotation-cycle-030-verified-against-audit-c029
- bilinear-form-l0-surface-comment-callout-polish-c029
- bilinear-form-l2-weighted-inner-product-reduction-combinator-c029
- bilinear-form-l1-entry-upstream-variant-axis-coverage-gaps-c029-tracking

Build-relevant: yes

Notes: Second per-report integration of cycle-029 (after the back-solve-mutation-rotation report-1). Re-read `book/src/L1-L0/index.md` + `book/src/SUMMARY.md` on disk at dispatch time per the role's "re-read disk before each Edit" discipline — both already carried report-1's back-solve row+entry; appended this theme's row+entry at the report-requested location (after `matrix-weighted-norm-mutation-rotation`, not after back-solve) preserving the report-stated grouping rationale (bilinear-form belongs next to matrix-weighted-norm because they share the L0 file block and inherited sub-themes). The report applied cleanly with all critic checks pass-or-repaired (one citation-validity warning was repaired by the repairer in three places: the misquoted L1 composition identity `dot(apply_linop(M,y),x)` → upstream-canonical `dot(x, apply_linop(M,y))`; plus one cosmetic off-by-one `:88-90` → `:88-89` Atn-construction span correction). The repaired identity matches the upstream `book/src/L1/bilinear-form.md:112-113` verbatim, and the §"Conjugation asymmetry" section was already correct (per critic's note that the defect did NOT propagate into the rotation rule). Post-apply `--scan` on the chapter on disk: 19/19 citations zero-drift. The cycle-024 `convert-nested-fences-to-indented-code-in-proposed-changes-block` defensive idiom was used (4-space-indented inner code blocks at lines :112-126 / :202-217 of the report, no nested triple-backtick fences) — the `new:` block parsed cleanly as a single literal write. The 4 OQs promoted are appropriate downstream-hand-off notes (no defects); the cycle-030 verified_against audit is the standard sibling-theme follow-up. The L1 operator `bilinear-form` stays `rough-in (test-coverage-bounded)` upstream — this theme being firm does NOT promote the L1 operator (per report explicit statement and the `matrix-weighted-norm-mutation-rotation`/`eigsolve-mutation-rotation` firm-theme-over-rough-in-L1-entry precedent). deferred `integrated_at:` to finalize per role-spec (per-report integrator does NOT touch report frontmatter).

---

## 2026-05-29T234506Z-abstractor-triangular-solve-obstruction
applied_at: 2026-05-30T00:55:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/triangular-solve-obstruction.md (created — obstruction-flavoured L1>L0 theme; status: obstruction, claim-free, opaque-library-ownership sub-kind)
- book/src/L1-L0/index.md (dep-map row insert immediately after the `bicgstab-iteration` obstruction row — clustered with the other two obstruction-flavoured themes)
- book/src/SUMMARY.md (chapter registration immediately after `minres-iteration`, before `chebyshev-smoother-mutation-rotation`; obstruction cluster)
- scaffolding/open-questions.md (appended 2 OQ sections: triangular-solve-obstruction-l1-l0-theme-LANDED-c029 [resolution-record for the c028-opened OQ at ledger :877 + flagging the cascading parent closures at :24/:868], sparse-triangular-solve-slice-reduction-after-l1l0-theme-lands [low-fan-out same-layer-cross-cutter follow-up])

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (this report)
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (obstruction theme; applicability-conditions section enumerates 4 axes with verdicts)
- bookkeeping incomplete: 0
- citecheck (--scan on applied chapter): 52 ok, 0 failing
- citecheck (--scan on source report): 55 ok, 0 failing
- SUMMARY.md chapter registration auto-fix: not-applied (report's edit explicitly registered)

Open questions promoted:
- triangular-solve-obstruction-l1-l0-theme-LANDED-c029
- sparse-triangular-solve-slice-reduction-after-l1l0-theme-lands

Build-relevant: yes

Notes: Third per-report integration of cycle-029 (after back-solve-mutation-rotation report-1 and bilinear-form-mutation-rotation report-2). Re-read `book/src/L1-L0/index.md` + `book/src/SUMMARY.md` on disk at dispatch time per the "re-read disk before each Edit" discipline — both carried the prior two reports' edits; appended this theme's row+entry at the report-requested locations (index: clustered with the other two obstructions after `bicgstab-iteration`; SUMMARY: clustered with `minres-iteration`/`bicgstab-iteration` obstructions). Applied the integrator skill `upgrade-plain-text-ref-to-live-link-when-target-on-disk` to the TWO plain-text references the report carried to `back-solve-mutation-rotation` (in §"L1 form" bullet and §"Sibling firm L1 evidence" bullet): verified `book/src/L1-L0/back-solve-mutation-rotation.md` is on disk (landed by report-1 earlier this cycle), then upgraded both plain-text mentions to live links `[`back-solve-mutation-rotation`](./back-solve-mutation-rotation.md)`. The verified_against YAML row at line 405-411 of the source was also condensed (the parenthetical "NOT yet on disk at the time this theme is authored — integrator-finalize upgrade-pass converts this plain-text reference to a live link" was removed since the upgrade happened at this integrator step, not at finalize). The report applied cleanly with all critic checks pass-or-repaired (one cross-reference-integrity warning was repaired by the repairer adding a §"Related" section + 3 `verified_against:` positive-cross-reference rows + 1 §"Open questions / caveats" entry — all surgical pointer-and-relationship additions to existing on-disk content, no new substantive claims). Post-apply `--scan` on the chapter on disk: 52/52 citations zero-drift. All 9 live links verified on disk (`back-solve-mutation-rotation.md`, `minres-iteration.md`, `bicgstab-iteration.md`, `../L1/back_solve.md`, `../L1/lu_solve.md`, `../L1/ksp_solve.md`, `../spec/slices/sparse_triangular_solve.md`, `../concepts/scope-out-obstruction.md`, `../concepts/sequential-obstruction.md`). The obstruction-cluster grouping is now 3 themes — `bicgstab-iteration`, `minres-iteration`, `triangular-solve-obstruction` — with the cycle-029 entry being the FIRST opaque-library-ownership obstruction (distinct from the two cycle-004 enum-only-stub obstructions), a distinction the §Justification-kind section calls out and the c029 abstractor's §Open-questions flagged as a possible meta-phase methodology refinement (`opaque-library-ownership` vs `enum-only-stub` obstruction sub-kinds). The two OQs promoted: the resolution-record OQ flags THREE meta-phase closures (the c028 `trsv`-leaf at ledger :868, the c028 `triangular-solve-obstruction-l1-l0-theme-needed` at :877, AND the parent migrated plan item `l3-vocabulary-inventory-gap` at :24 — all four leaves done after this lands); the slice-reduction OQ is the low-fan-out follow-up the repairer added per the cross-reference-integrity finding. Per role-spec the per-report integrator does NOT strike the c028 OQ entries in-place — that is meta-phase unify authority; recorded the disposition via appended sections per the OQ-channel convention. deferred `integrated_at:` to finalize per role-spec (per-report integrator does NOT touch report frontmatter).

---

## 2026-05-29T205945Z-harvester-ls-update-column-leaf
applied_at: 2026-05-30T01:25:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/ls-update-column.md (created — firm L1 leaf; GMRES/FGMRES per-column running-QR Face-1 of L2 incremental-least-squares; sibling-producer to back_solve)
- book/src/L1/index.md (cohort header "Firm (21)" -> "Firm (22)" + enumeration extended with ", and the GMRES/FGMRES per-column running-QR leaf"; cohort bullet inserted after the back_solve bullet; dep-map table row inserted after the back_solve row, before lanczos_step)
- book/src/SUMMARY.md (chapter registration `- [ls_update_column](./L1/ls-update-column.md)` inserted immediately after the existing `- [back_solve](./L1/back_solve.md)` entry, before the L1 > L0 — Lowering Part header)
- scaffolding/open-questions.md (appended 2 OQs: ls-update-column-l2-l1-theme-plain-text-ref-upgrade-to-live-link-c029, ls-update-column-mutation-rotation-l1l0-theme-forthcoming-c029)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (this report)
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0
- bookkeeping incomplete: 0
- citecheck (--scan on applied chapter): 40 ok, 0 failing
- citecheck (--scan on source report): 45 ok, 0 failing
- SUMMARY.md chapter registration auto-fix: not-applied (report's edit explicitly registered)

Open questions promoted:
- ls-update-column-l2-l1-theme-plain-text-ref-upgrade-to-live-link-c029
- ls-update-column-mutation-rotation-l1l0-theme-forthcoming-c029

Build-relevant: yes

Notes: Fourth per-report integration of cycle-029 (after back-solve-mutation-rotation report-1, bilinear-form-mutation-rotation report-2, triangular-solve-obstruction report-3). Re-read `book/src/L1/index.md` + `book/src/SUMMARY.md` on disk at dispatch time per the role's "re-read disk before each Edit" discipline — index showed Firm (21) (the cycle-028 finalize's last bump, with back_solve as the 21st), confirming the report's pre-supplied current-state assumption; bumped to Firm (22) and extended the enumeration tail to add ", and the GMRES/FGMRES per-column running-QR leaf". The report applied cleanly with all critic checks pass-or-repaired (one citation-validity warning was repaired in three places: off-by-one anchor :88 -> :87-88 on the slug-bearing sentence in the L2-L1 theme — repaired in-place by the repairer at CYCLE.md:89/:526/:861 with the slug-bearing sentence range correctly identified). Post-apply `--scan` on the chapter on disk: 40/40 citations zero-drift (the 45-vs-40 delta is the report's META and "Supporting evidence" outer-prose adjacent extras vs the chapter body's anchor cohort — both clean). The cycle-024 `convert-nested-fences-to-indented-code-in-proposed-changes-block` defensive idiom was used (4-space-indented inner code blocks in the Signature/Semantics/L1 vs L0 sections, plus a single nested ` ```yaml ` verified_against fence at the bottom — the same landed-convention pattern as cycle-027 axpby-axpbypcz and bilinear-form). The `new:` block parsed cleanly as a single literal write.

L2-L1 theme plain-text refs at `:69`/`:87-88`/`:307-310` were NOT upgraded inline this integration (per the dispatch's optional clause) — the `:69` ref is a clean slug-relink but `:87-88` requires substantive prose rewrite (the entire "forthcoming / not yet on disk / plain text per the rough-in-forward-reference convention" sentence is now factually obsolete and needs replacement, not just slug-relinking), and `:307-310` requires the speculative-L1-operators §framing to be updated to a closed-target record. Both are content edits beyond the mechanical-token-relink integrator skill scope; deferred to the OQ `ls-update-column-l2-l1-theme-plain-text-ref-upgrade-to-live-link-c029` for a follow-on lifter or same-layer-cross-cutter dispatch (per the report's §Open-questions item-1 explicit guidance).

The 2 OQs promoted: (1) the plain-text-ref upgrade follow-up just discussed, with the load-bearing detail that `:87-88` carries the "forthcoming" framing that must be replaced (not just relinked); (2) the forthcoming `ls-update-column-mutation-rotation` L1>L0 theme as a fresh abstractor target — sibling to the c029-report-1-landed `back-solve-mutation-rotation` and the firm `orthogonalize-mutation-rotation`, completing the GMRES inner-loop L1>L0 cohort. Per role-spec, deferred `integrated_at:` to finalize (per-report integrator does NOT touch report frontmatter). This is the first L1 firm operator landed in cycle-029 (the prior three reports landed L1-L0 themes); the chapter brings the L1 firm cohort from 21 -> 22, closing the cycle-027 back_solve harvest's "producer counterpart still forthcoming" forward-reference half of the GMRES restart-cycle least-squares chain.

---

## 2026-05-29T205945Z-abstractor-normalize-b-prose-correction
applied_at: 2026-05-30T01:50:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/normalize-mutation-rotation.md (3 edits: §Speculative-L1-operators rough-in note rewrite :283-293 "no fused" → "exists but uncalled"; §L0-form intro :51 parenthetical add; §promotion-gate :298-301 tightening "find that the function exists" → "find a positive *callsite*")
- book/src/L1/normalize.md (4 edits: chapter-intro :13 parallel rewrite; rough-in-note item-1 :87-88 parallel rewrite; promotion-gate :90 parallel tightening; rough-in-section paragraph closing-sentence append)
- scaffolding/open-questions.md (appended 2 OQs: normalize_B-note-says-no-fused-B-Normalize-but-uncalled-fused-operator-exists-RESOLVED-c029 [closure record for the c028-opened OQ at ledger :811]; normalize-mutation-rotation-verified-against-row-466-469-stale-after-c029-prose-correction [the verified_against row :466-469 will be stale after this lands — needs a future lowering-verifier refresh])

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (this report)
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0
- bookkeeping incomplete: 0
- citecheck (--scan on normalize-mutation-rotation.md): 48 ok, 0 failing (after path-hygiene repair — initial scan showed 2 AMBIG on bare `operator.hpp:378`/`operator.hpp:377-384` introduced by report edits; repaired in-place at land time to full-path `palace/linalg/operator.hpp:...` against the sibling `palace/fem/libceed/operator.hpp` ambiguity)
- citecheck (--scan on normalize.md): 32 ok, 0 failing (after path-hygiene repair — initial scan showed 1 AMBIG on bare `operator.hpp:378` at :87/:95 introduced by report edits; repaired in-place at line :87 by adding the full-path `palace/` prefix)
- SUMMARY.md chapter registration auto-fix: not-applied (no chapter additions)

Open questions promoted:
- normalize_B-note-says-no-fused-B-Normalize-but-uncalled-fused-operator-exists-RESOLVED-c029
- normalize-mutation-rotation-verified-against-row-466-469-stale-after-c029-prose-correction

Build-relevant: yes

Notes: Fifth per-report integration of cycle-029 (after back-solve-mutation-rotation report-1, bilinear-form-mutation-rotation report-2, triangular-solve-obstruction report-3, ls-update-column harvest report-4). This is a PROSE-ONLY correction (NO `## Status` changes, NO new files, NO SUMMARY.md edits, NO dep-map edits). Re-read both target files on disk at dispatch time per the role's "re-read disk before each Edit" discipline — both already carried the c028 lowering-verifier audit's edits (the verified_against block at :408-474 of normalize-mutation-rotation.md and the c028 F3 :810-811 fix), and the strings the report's edit blocks targeted matched on-disk verbatim. The report applied cleanly with all 8 critic checks pass + zero repair needed (overall_status: ready); the corrective scope was per role-spec abstractor authority (substantive prose rewrite spanning two firm files, exceeds repairer's mechanical scope).

The path-hygiene repair (a per-report safety-net gate enacted at land-time per `.claude/agents/integrator-per-report.md` §Process step 5 "citecheck bounds + path-hygiene lint") replaced 3 bare-basename `operator.hpp` references introduced by the report's edit blocks with the unambiguous `palace/linalg/operator.hpp` full path. The critic's META.md had noted these as report-prose-only AMBIGs (the report's narration sections had them); on inspection the bare basenames also appeared in two `edit:` block targets that landed in the artifact (normalize-mutation-rotation.md:292 + :301 and normalize.md:87). Mechanical-token substitution; no semantic change. Both files clean post-repair.

Both file `## Status` lines verified unchanged at `firm` (line 398 / line 97 respectively). `normalize_B` rough-in note correctly stays a rough-in (the gate STAYS OPEN — the gate-tightening makes the bar STRICTER not looser; the evidence-set widens to accept a 4-arg `Normalize(comm, v, B, Bv)` callsite, but mere existence of the def at `:378` is now explicitly insufficient).

Two OQs promoted: (1) the closure record for the c028-opened OQ `normalize_B-note-says-no-fused-B-Normalize-but-uncalled-fused-operator-exists` at ledger :811 — per role-spec the per-report integrator does NOT strike the c028 OQ entry in-place (that is meta-phase unify authority); recorded the disposition via appended section per the OQ-channel convention. (2) the new follow-up OQ flagging that the verified_against row at normalize-mutation-rotation.md:466-469 (verdict `does-not-support`, with F1 diagnostic note) is now stale — the prose F1 cited is no longer present in the artifact; a future lowering-verifier refresh should update the row's verdict + note to reflect the corrected "exists but uncalled" prose. Low-priority, non-gating, audit-row staleness only — NOT a defect of the firm unweighted core.

deferred `integrated_at:` to finalize per role-spec (per-report integrator does NOT touch report frontmatter).

---

## 2026-05-29T234506Z-layer-intro-author-l2-l1-l2-index-prose-refresh
applied_at: 2026-05-30T02:15:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2-L1/index.md (1 edit: appended Vocabulary-cohort subsection — 7 firm + 1 partly-constructive — between the dep-map table and Working Notes; appended Cohort-growth-log bullet to Working Notes)
- book/src/L2/index.md (3 edits: refreshed Named-compositions motif paragraph at §Semantics overlay — extended from 2-exemplar to 4-exemplar framing; removed now-empty "Queued at L2 (stub)" subsection from Vocabulary cohort; added `incremental-least-squares` + `eigsolve` to the "Firm at L2" sub-list — closing the stale-by-omission gap the critic flagged; refreshed the Working-Notes stub-queue bullet to a `l2-named-composition-lifts`-closed bullet)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0 (this report)
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- edge-label / prose mismatch: 0
- H1 reuses page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0
- bookkeeping incomplete: 0
- citecheck (--scan on book/src/L2-L1/index.md): 4 ok, 0 failing
- citecheck (--scan on book/src/L2/index.md): 12 ok, 1 failing — pre-existing MISS `spec/slices/chebyshev.md:354-362` at line 70 (Pattern-instances historical/provenance bullet; the slice was absorbed into `book/src/L4/chebyshev.md` cycle-015 and the source slice no longer exists; the citation parenthetical literally narrates this absorption — "absorbed the former `spec/slices/chebyshev.md:354-362`" — so the dead anchor is semantically intentional historical-provenance prose, not a defect of this report). NOT touched by this report's edits; out of prose-only scope.
- citecheck (--scan on source report CYCLE.md): 6 ok, 0 failing
- SUMMARY.md chapter registration auto-fix: not-applied (no chapter additions)

Open questions promoted:
- (none) — the report's §Open-questions has 3 items, all explicit "not a defect / framing choice" notes the critic + repairer confirmed do NOT require ledgering: (1) cohort-log gap for cycles 014/015/016/017 — "not an issue, just noting"; (2) `ls_update_column` plain-text forward-ref — already covered by the existing report-4 OQ `ls-update-column-l2-l1-theme-plain-text-ref-upgrade-to-live-link-c029` at ledger :969 (which addresses the L2-L1 theme's plain-text refs, the same forward-reference the L2-L1 dep-map row carries — the cohort prose I added inherits the framing); (3) `ksp_solve`/`eigsolve` placement in named-compositions motif as "third"/"fourth" — already downstream-anchored at `L2/eigsolve.md:23` per the critic's verification ("alongside [`orthogonalize`] and [`ksp_solve`]").

Build-relevant: yes

Notes: Sixth + final per-report integration of cycle-029 (after back-solve-mutation-rotation report-1, bilinear-form-mutation-rotation report-2, triangular-solve-obstruction report-3, ls-update-column harvest report-4, normalize-B prose correction report-5). This is a PURE PROSE / NAVIGATIONAL refresh — NO dep-map rows, NO `## Status` lines, NO chapter-body content edited. Re-read both target files on disk at dispatch time per the role's "re-read disk before each Edit" discipline — neither L2-L1/index.md nor L2/index.md was touched by any prior c029 per-report integration (the prior 5 reports touched L1-L0/, L1/, SUMMARY.md, and chapter-body files but not these two Part overviews); strings the report's edit blocks targeted matched on-disk verbatim. The report applied cleanly with all 8 critic checks pass + zero repair needed (overall_status: ready).

Counts re-verified post-apply (the source-of-truth dep-map counts the prose claims): `grep -c "^| \[" book/src/L2-L1/index.md` returns 8 (7 firm + 1 partly-constructive `deflate-composition-lowering`, exact match); `grep -c "^| \[" book/src/L2/index.md` returns 10 (9 firm + 1 partly-constructive `deflate`, exact match). The cohort prose I added matches the on-disk dep-map maturity distribution exactly.

The pre-existing citecheck MISS at `book/src/L2/index.md:70` is a historical/provenance bullet in the Pattern-instances Working-Notes block that literally narrates a cycle-015 absorption ("absorbed the former `spec/slices/chebyshev.md:354-362`"). The slice file was removed at that absorption and the citation has been dead since then — a multi-cycle-old condition out of this report's prose-only scope and arguably out of book-scope (the parenthetical is correct as written; the citecheck simply cannot prove the dead anchor is intentional). Recording in this row's Notes per the role-spec discipline of "record the scan result in the staging row Notes"; non-blocking per the role-spec ("Non-blocking unless a `MISS`/`AMBIG`/`OOB` is unrepairable" — this MISS is unrepairable WITHOUT rewriting the historical-provenance prose, which is out of this report's scope, AND the prose is semantically correct as-is); finalize may flag for a future lifter / same-layer-cross-cutter slice-reduction-audit follow-up if desired.

deferred `integrated_at:` to finalize per role-spec (per-report integrator does NOT touch report frontmatter). This is the last per-report integration for cycle-029 — integrator-finalize is the next dispatch.

---
