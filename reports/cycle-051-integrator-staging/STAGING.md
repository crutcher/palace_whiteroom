# cycle-051 integrator staging log

Per-report integration rows, append-only, newest LAST. Read by integrator-finalize to reconcile the cycle (rebuild + commit + housekeeping).

---

## 2026-06-01T210700Z-lifter-linear-combination-family-demotion
applied_at: 2026-06-01T21:46:48Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L3-L2/scal-body-identity.md (DELETE)
- book/src/L3-L2/axpy-body-identity.md (DELETE)
- book/src/L3-L2/axpby-body-identity.md (DELETE)
- book/src/L3-L2/axpbypcz-body-identity.md (DELETE)
- book/src/L2-L1/scal-leaf-identity.md (DELETE)
- book/src/L2-L1/axpy-leaf-identity.md (DELETE)
- book/src/L2-L1/axpby-leaf-identity.md (DELETE)
- book/src/L2-L1/axpbypcz-leaf-identity.md (DELETE)
- book/src/L3/scal.md (edit — re-expressed as arity-1 specialization of linear_combination; frontmatter + H1 + Context + Lowers-to + Lifts-from)
- book/src/L3/axpy.md (edit — arity-2, second-coeff-1; frontmatter + H1 + Dependencies + Lowers-to + Evidence dep-block)
- book/src/L3/axpby.md (edit — general arity-2; same 4 sections)
- book/src/L3/axpbypcz.md (edit — arity-3 incl γ==0 collapse; same 4 sections)
- book/src/L3/index.md (edit — (f) repairer block: rows 24/25/26 re-pointed the 6 stale live links to the combinator route + KEPT fold-specialization theme — BUILD-CRITICAL)
- book/src/L3-L2/index.md (edit — (d) reshaped kept-neighbor-re-emit: [old] rows 16–20, [new] re-emits row 16 ksp-solve-outer-driver; dropped 4 *-body-identity rows; table stays contiguous)
- book/src/L2-L1/index.md (edit — (d) [old] rows 15–20, [new] re-emits rows 16/17 inner-product-fold-specialization + dot-leaf-identity; dropped 4 *-leaf-identity rows; row 14 linear-combination-fold-specialization KEPT)
- book/src/L3/linear_combination.md (edit — (e) §111 stale future-tense + dead axpy-body-identity live link → past-tense + de-linked)
- book/src/L3-L2/jacobi-smoother-body-identity.md (edit — (c) 2 defensive de-links of scal-body-identity live links → plain-text + demotion note)
- book/src/L3-L2/divfree-projector-body-identity.md (edit — (c) de-link scal-body-identity live link)
- book/src/L2-L1/divfree-projector-leaf-identity.md (edit — (c) de-link scal-leaf-identity live link)
- book/src/SUMMARY.md (edit — (d) removed the 8 deleted-theme TOC lines; running-count tally DEFERRED to D5)
- scaffolding/open-questions.md (append — 1 OQ: linear-combination-home-residual-future-tense-sweep)

Gate hits:
- citecheck-scan-bounds: 0 (27 ok, 0 failing — re-confirmed on the report at apply time; pre-delete)
- dangling-link (8 deleted slugs): 0 LIVE markdown links survive (grep `]\(...*-{body,leaf}-identity.md\)` over book/src returns none). Residual mentions are all code-spans / narrative prose (non-breaking) — see Notes.
- fence-parity / anchor-byte-exactness: 0 (all [old] anchors matched on-disk byte-exact; applied via Edit, not raw fence-parse)
- retroactive-budget: 0
- index-placeholder displacement: n/a
- SUMMARY chapter registration auto-fix: n/a (deletions only; no new chapter created)

Open questions promoted:
- linear-combination-home-residual-future-tense-sweep

Build-relevant: yes

Notes:
- BUILD-CRITICAL (f) block landed: the 6 stale live links in L3/index.md rows 24/25/26 to deleted `*-body-identity` slugs are re-pointed through the combinator route. Verified zero surviving LIVE links to any of the 8 deleted slugs across book/src.
- Non-breaking residual code-spans / prose references to the deleted slugs remain by design (critic findings 3/4/5, report deferred-tense scope): L3-L2/index.md:33-37 "Lowering themes" bullets; L3-L2/jacobi-smoother-body-identity.md:130/177/215/269; L3/linear_combination.md:162 §Evidence; L2/axpby.md:274; L2/axpbypcz.md:292; L2/index.md:118/121/123; L3/elementwise_product.md:166. None is a live link → none breaks linkcheck2. Captured in the promoted OQ for a D5/batch-15-16 tense-sweep.
- Consolidated index tally (running firm counts on L3-L2/index.md, L2-L1/index.md, SUMMARY) DEFERRED to D5 per the report's (d) scope — only D1's own 8 lines + own dep-map rows removed here. integrator-finalize / D5 owns the reconciliation; pairs with OQ `c050-firm-theme-count-drop-is-vehicle-change-not-coverage-regression`.
- deferred integrated_at to finalize per role-spec (did NOT touch the report's frontmatter integrated_at / integration_commit).
- First per-report integrator of cycle-051; created this STAGING.md.

---
## 2026-06-01T210700Z-lifter-inner-product-dot-demotion
applied_at: 2026-06-01T21:52:52Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L3-L2/dot-body-identity.md (DELETE)
- book/src/L2-L1/dot-leaf-identity.md (DELETE)
- book/src/L3/dot.md (edit — RE-EXPRESSED through L2/inner_product: frontmatter lowers_to/lifts_from, lede, §Context, §"Lowers to"→§"Downward to L2 (through inner_product)", §Dependencies combinator+L2>L1-translation anchors, §Status, §Evidence dep-block, §"L3 vs L1 distinction"; 6 [old/new] blocks)
- book/src/L3/inner_product.md (edit — (c) de-tense: frontmatter lowers_to line + §"Downward to L2" pre-built-home note → past-tense statement of fact, file-deleted note added)
- book/src/L2/inner_product.md (edit — (c) de-tense 2 plain-text/code-span notes: lede block + cycle-050-enactment note → "theme files were deleted at cycle-051, content absorbed")
- book/src/L3/index.md (edit — (c) de-tense 2: inner_product dep-map "Downward" cell + cohort-growth-log line 65 dot-body-identity clause → past-tense + deleted-files note)
- book/src/L2-L1/divfree-projector-leaf-identity.md (edit — (c) 3 de-links of dot-leaf-identity live links at on-disk lines 19/22/266; line-266 used the DISTINCT dot-leaf-identity-only substring — composes order-independently with D3's nrm2-leaf-identity de-link; nrm2-leaf-identity link LEFT LIVE for D3)
- book/src/SUMMARY.md (edit — (d) removed OWN 2 TOC lines: dot-body-identity + dot-leaf-identity)
- book/src/L3-L2/index.md (edit — (d) removed OWN dot-body-identity dep-map row + bullet)
- book/src/L2-L1/index.md (edit — (d) removed OWN dot-leaf-identity dep-map row + bullet)
- scaffolding/open-questions.md (append — 2 OQs)

Gate hits:
- citecheck-scan-bounds: 1 OOB (19 ok, 1 failing) — L2-L1/index.md:73 (report-prose see-also reference in D2's Open-questions caveat CYCLE.md:333; cohort-growth-log shrank to line 67 after D1+D2 row/bullet deletions, content intact). NON-BLOCKING: narrative see-also in append-only report prose, not a load-bearing artifact claim; OOB is a consequence of D2's own correct deletions. Recorded for D5 line-number re-pin in promoted OQ.
- dangling-link (2 deleted dot-* slugs): 0 LIVE links survive in D2's OWN de-link survivors (KEPT divfree-projector-leaf-identity.md clean). Broad grep finds 4 live links in SIBLING-DISPATCH delete-target files only: divfree-projector-body-identity.md:22,231 (D4 delete target) + jacobi-smoother-leaf-identity.md:12,35 (D8 DEMOTE-OK delete target) — links die with the files; D2 correctly did NOT edit them (cross-dispatch conflict avoidance). integrator-finalize re-greps after all dispatches.
- fence-parity: 0 (L3/dot.md fence count even = 2; §"Lowers to"→§"Downward to L2" rename clean; all 6 [old] blocks applied via Edit byte-exact)
- anchor-byte-exactness: 0 (all D2 [old] anchors matched current on-disk state byte-exact, incl. files D1 had already touched — L3/index.md line 65, divfree-projector-leaf-identity.md; D2's substrings were distinct from D1's)
- retroactive-budget: 0
- SUMMARY chapter registration auto-fix: n/a (deletions only)
- index-placeholder displacement: n/a

Open questions promoted:
- divfree-projector-leaf-identity-three-way-co-edit-line-266-serial-ordering
- dot-family-cross-dispatch-dangler-and-cohort-log-line-drift-d5-finalize-checks

Build-relevant: yes

Notes:
- D2 is the SECOND per-report integrator of cycle-051 (D1 = linear_combination family landed first). Re-read all targets at apply time; confirmed D1's prior touches to L3/index.md (line 65 BLAS-1 re-points) + divfree-projector-leaf-identity.md (scal-leaf-identity de-link) did NOT alter D2's distinct dot-* anchor substrings.
- THREE-WAY co-edit on KEPT divfree-projector-leaf-identity.md (D2/D3/D4): D2's 3 de-links APPLIED here. Line 266 now has dot-leaf-identity de-linked, nrm2-leaf-identity STILL LIVE — D3 (next per-report integrator on this file) must de-link it; repairer narrowed D2's line-266 old_string to the dot-leaf-identity-only substring so D2/D3 compose order-independently. Flagged in promoted OQ + for integrator-finalize.
- The repairer-DROPPED divfree-projector-body-identity.md edits (D4 deletes that file) were correctly absent from the report — did not look for or apply them.
- Consolidated firm-theme TALLY (running counts on L3-L2/index.md cohort-growth-log line ~32, L2-L1/index.md cohort-growth-log line 67, L2/index.md, SUMMARY) DEFERRED to D5 per report scope (d). D2 removed ONLY its own 2 TOC lines + own 2 dep-map rows + own 2 bullets. The cohort-growth-log narrative lines (which still mention dot-leaf-identity in historical/tally context) are D5's.
- deferred integrated_at to finalize per role-spec (did NOT touch the report's frontmatter integrated_at / integration_commit).

---
## 2026-06-01T210700Z-lifter-nrm2-consumer-demotion
applied_at: 2026-06-01T22:01:30Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L3-L2/nrm2-body-identity.md (DELETE)
- book/src/L2-L1/nrm2-leaf-identity.md (DELETE)
- book/src/L3/nrm2.md (edit — (b1) NEW §"Downward to L2 (consumer identity-in-form; no theme file)" inserted after §"Lowers to"; records identity-in-form on the primitive's signature, CONSUMER-of-inner_product-NOT-a-fold-member do-NOT-merge boundary, std::abs guard as explicit load-bearing claim, vector.hpp:255-260 Norml2 L0 anchor preserved)
- book/src/L2/nrm2.md (edit ×3 — (b2): frontmatter lowers_to de-tensed (dropped "narrated by D5 L2-L1 theme" → in-line/no-theme-file); §"Lowers to" body de-tensed + NEW §"Downward to L1 (consumer identity-in-form; no theme file)"; §"Lifts from" re-anchored deleted-L3-L2-theme ref → in-line note. std::abs guard preserved-as-claim in both notes; Norml2 anchor preserved)
- book/src/L2-L1/divfree-projector-leaf-identity.md (edit — (c) de-link the surviving `nrm2-leaf-identity` live link on on-disk line 266; narrow single-substring repair composes order-independently with D1's scal- and D2's dot- de-links already applied to same line)
- book/src/SUMMARY.md (edit ×2 — (d) removed OWN 2 TOC lines: L3-L2/nrm2-body-identity + L2-L1/nrm2-leaf-identity)
- book/src/L3-L2/index.md (edit ×2 — (d) removed OWN nrm2-body-identity dep-map row + cohort bullet → "(demoted cycle-051)" annotation)
- book/src/L2-L1/index.md (edit ×2 — (d) removed OWN nrm2-leaf-identity dep-map row + cohort bullet → "(demoted cycle-051)" annotation)
- scaffolding/open-questions.md (append — 2 OQs)

Gate hits:
- citecheck-scan-bounds: 1 OOB + 1 AMBIG, both the SAME report-prose reference (8 ok, 2 failing). `L2-L1/index.md:73` (OOB — file now 67 lines after D1/D2/D3 deletions; content intact ~line 67) and the bare-basename `index.md:73` (AMBIG). Both are the cross-report-split see-also in D3's §Supporting-evidence / OQ-1 narrative — NON-LOAD-BEARING report prose, not artifact claims; consequence of D1/D2/D3's own correct deletions. The load-bearing L0 citation vector.hpp:255-260 (Norml2) used in both in-line notes is one of the 8 ok. NON-BLOCKING; D5/finalize re-pin recorded in promoted OQ.
- dangling-link (2 deleted nrm2-* slugs): 1 LIVE link survives — `book/src/L3-L2/divfree-projector-body-identity.md:231` → `nrm2-body-identity.md`. This file is sibling D4's (lifter-jacobi-divfree-demotion, CYCLE.md:36) WHOLESALE DELETE TARGET; the link dies with the file when D4 applies. D3 correctly did NOT edit it (repairer DROPPED that de-link as moot — cross-dispatch conflict avoidance). D3's OWN de-link survivor (KEPT divfree-projector-leaf-identity.md) is CLEAN: zero live links to either deleted slug. integrator-finalize re-greps after all dispatches.
- fence-parity / anchor-byte-exactness: 0 (all [old] anchors matched current on-disk state byte-exact; applied via Edit not raw fence-parse; surrounding-context SUMMARY/index anchors shifted by D1/D2's prior deletions so anchored each removal on its own line + one surviving sibling line)
- retroactive-budget: 0
- index-placeholder displacement: n/a
- SUMMARY chapter registration auto-fix: n/a (deletions only)
- implied-component stub: n/a

Open questions promoted:
- nrm2-consumer-demotion-d5-tally-and-l2-index-historical-narrative-refresh
- nrm2-leaf-identity-d3-apply-status-and-divfree-body-identity-cross-dispatch-dangler

Build-relevant: yes

Notes:
- D3 is the THIRD per-report integrator of cycle-051 (after D1 linear_combination-family, D2 inner_product/dot-family). Re-read all targets at apply time; confirmed D1's + D2's prior touches (SUMMARY axp*/dot line removals, L3-L2/L2-L1 index row+bullet removals, divfree-leaf line-266 scal-/dot- de-links) did NOT alter D3's distinct nrm2-* anchor substrings.
- CONSUMER-DEMOTION (do-NOT-merge) honored: nrm2 NOT folded into inner_product, inner_product/L1/nrm2/any-fold-entry NOT touched. Both new in-line notes land ON the nrm2 entries themselves and record the consumer-not-member boundary explicitly. std::abs load-bearing guard preserved as explicit claim in BOTH notes (directive requirement). vector.hpp:255-260 Norml2 anchor preserved + byte-exact.
- THREE-WAY (D1/D2/D3) co-edit on KEPT divfree-projector-leaf-identity.md line 266 landed correctly order-independently: scal- (D1), dot- (D2), nrm2- (D3) all de-linked, all narrow distinct substrings. KEPT file is now clean of all three deleted-slug live links.
- The repairer-DROPPED divfree-projector-body-identity.md edit (D4 deletes that file) was correctly ABSENT from the report — did not look for or apply it. The 1 surviving dangler there is D4's to resolve via deletion.
- Consolidated firm-theme TALLY (running counts on L3-L2/index.md cohort §, L2-L1/index.md cohort-growth-log ~line 67, L2/index.md historical narrative :118/:121/:123) DEFERRED to D5 per report scope (d). D3 removed ONLY its own 2 TOC lines + own 2 dep-map rows + own 2 cohort bullets. L2/index.md historical code-span mentions of the deleted nrm2-* slugs (non-live, non-blocking) left for D5 honesty-annotation.
- deferred integrated_at to finalize per role-spec (did NOT touch the report's frontmatter integrated_at / integration_commit).

---
## 2026-06-01T210700Z-lifter-jacobi-divfree-demotion
applied_at: 2026-06-01T22:12:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L3-L2/jacobi-smoother-body-identity.md (DELETE — git rm -f; D1/D2/D3 sibling de-link edits had left local modifications, force-removed per the report's expectation that those edits die with the file)
- book/src/L2-L1/jacobi-smoother-leaf-identity.md (DELETE — git rm)
- book/src/L3-L2/divfree-projector-body-identity.md (DELETE — git rm -f; carried D1/D2/D3 de-link mods + the surviving nrm2/dot-body-identity danglers D2/D3 flagged at :22/:231; all die with the file)
- book/src/L3/jacobi-smoother.md (edit x2 — §Context "Downward" bullet + §"Lowers to" re-anchored to in-line degenerate-identity note, no L3>L2 theme file named; jacobi.cpp:38 DI[i]*X[i] anchor preserved/added)
- book/src/L2/jacobi-smoother.md (edit x2 — frontmatter lowers_to line + §"Lowers to" body de-tensed to in-line degenerate-identity note, no L2>L1 theme file)
- book/src/L3/divfree-projector.md (edit x3 — frontmatter line 6 + §Context "Downward" bullet + §"Lowers to" re-anchored; DIRECT live link onward to KEPT ../L2-L1/divfree-projector-leaf-identity.md added; divfree.cpp:185 real / :180-181 complex + :155-187 anchors preserved)
- book/src/L2-L1/divfree-projector-leaf-identity.md (edit — §7b de-link of its line-36 live link to the now-deleted divfree-projector-body-identity slug -> plain-text sibling-pointer + live link to L3 entry; KEPT theme otherwise untouched. Distinct substring from D1/D2/D3's line-266 de-links — composed order-independently)
- book/src/SUMMARY.md (edit x2 — removed OWN 3 TOC lines: jacobi-smoother-body-identity + divfree-projector-body-identity (adjacent) + jacobi-smoother-leaf-identity; KEPT divfree-projector-leaf-identity line)
- book/src/L3-L2/index.md (edit x4 — removed OWN 2 -body-identity dep-map rows + updated cohort note + collapsed 2 bullets into a DEMOTED-cycle-051 bullet + cohort-growth 17->13->11)
- book/src/L2-L1/index.md (edit x3 — removed OWN jacobi-smoother-leaf-identity row + DEMOTED bullet + cohort-log split-note; KEPT divfree-projector-leaf-identity row + bullet)
- scaffolding/open-questions.md (append — 1 OQ: d4-jacobi-divfree-demotion-applied-divfree-body-identity-dangler-resolved-and-d5-count)

Gate hits:
- citecheck-scan-bounds: 0 (7 ok, 0 failing — re-confirmed on the report at apply time; no MISS/AMBIG/OOB)
- dangling-link (3 deleted slugs jacobi-smoother-{body,leaf}-identity + divfree-projector-body-identity): 0 LIVE markdown links survive anywhere in book/src after deletion. The cross-dispatch danglers D2/D3 flagged at divfree-projector-body-identity.md:22,231 (dot-/nrm2-body-identity) are RESOLVED — that file is deleted. Residual mentions are plain-text code-spans in prose/index narrative (non-breaking).
- KEPT-theme-reachability: PASS — divfree-projector-leaf-identity.md reachable via DIRECT live link from L3/divfree-projector.md (2 links: §Context Downward note + §Lowers-to note). The genuine step-4 Grad->AddMult fusion rotation is NOT orphaned. KEPT file + its 1 SUMMARY line + 1 L2-L1 index row all present.
- fence-parity / anchor-byte-exactness: 0 (all [old] anchors matched current on-disk state byte-exact, incl. lines D1/D2/D3 had shifted; applied via Edit not raw fence-parse. The 4 touched L3/L2 entries + KEPT theme use 4-space-indented code blocks, ZERO triple-backtick fences -> parity trivially even, no fence-truncation risk)
- retroactive-budget: 0
- SUMMARY chapter registration auto-fix: n/a (deletions only)
- index-placeholder displacement: n/a
- implied-component stub: n/a

Open questions promoted:
- d4-jacobi-divfree-demotion-applied-divfree-body-identity-dangler-resolved-and-d5-count

Build-relevant: yes

Notes:
- D4 is the FOURTH per-report integrator of cycle-051 (after D1 linear_combination-family, D2 inner_product/dot-family, D3 nrm2 consumer-demotion). Re-read all targets at apply time; confirmed D1/D2/D3's prior touches (SUMMARY line removals shifting line numbers; L3-L2/L2-L1 index row/bullet removals; the 3-way line-266 de-links on the KEPT divfree-projector-leaf-identity.md) did NOT alter D4's distinct anchor substrings. D4's §7b edit targets line 35-37 (sibling-pointer prose), distinct from the line-266 cohort D1/D2/D3 edited.
- KEEP/DEMOTE partition honored exactly: 3 theme files deleted (jacobi x2 edges + divfree-projector-body-identity L3>L2); the KEPT divfree-projector-leaf-identity (L2>L1, the one genuine step-4 Grad->AddMult fusion rotation) is preserved (file, SUMMARY line, L2-L1 index row 27, working-notes bullet all survive) with only the §7b de-link applied.
- The git status shows my 3 deletions staged (D in index, via git rm) while D1/D2/D3's deletions show unstaged D — integrator-finalize's git add -A at commit reconciles all into one atomic commit.
- Consolidated firm-theme TALLY (FINAL cross-dispatch counts across D1-D4) DEFERRED to D5 per the dispatch brief's D4-before-D5 serial dependency — D5's anchor is D4's [new] 17->13->11 intermediate. D4 removed ONLY its own 3 SUMMARY lines + 3 dep-map rows (2 in L3-L2/index, 1 in L2-L1/index) + working-notes bullets, and rewrote the cohort-count narratives to its local-scope view.
- deferred integrated_at to finalize per role-spec (did NOT touch the report's frontmatter integrated_at / integration_commit).

---
## 2026-06-01T210700Z-layer-intro-author-c051-count-ownership
applied_at: 2026-06-01T22:09:17Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L3-L2/index.md (edit ×2 — (A.1) collapsed the gutted BLAS-1-leaf cohort-header italic intro to an ALL-SIX-DEMOTED discharge note (on-disk line 26); (A.2) consolidated cohort-growth bullet `17 → 13 cycle-050 → 5 cycle-051` (on-disk line 51) — anchor was D4's `[new]` `17 → 13 → 11` verbatim, corrected to FINAL consolidated 5)
- book/src/L2-L1/index.md (edit — (B) cohort-growth-log head bracket → CONSOLIDATED `firm 21 → 17 (cycle-050) → 10 (cycle-051)` (on-disk line 65); disjoint head-bracket substring preceding D4's already-applied "NOTE the cycle-050-vs-051 split" sentence on the same logical line)
- book/src/L3/index.md (edit — (C) degenerate-cohort discharge note on the cycle-050 combinator bullet (on-disk line 65); RECONCILED: D5's C `[old]` was the pre-D2 future-tense form, D2 had already partially past-tensed the line, so applied D5's INTENT against the current on-disk tail. Authoritative L3 count tally (line 63) NOT touched — stays 17 firm + 3 partial-obstruction)
- scaffolding/open-questions.md (append — 3 OQs)

Gate hits:
- anchor-byte-exactness: 0 hard failures. A.1/A.2/B matched on-disk byte-exact (line numbers shifted from D5's documented 34/61/73 to 26/51/65 by D1–D4 deletions, text identical). C RECONCILED: D5's `[old]` was superseded by D2's prior past-tensing of L3/index.md line 65; applied D5's INTENT (re-expressed-cycle-051 + sweep-COMPLETE) against the current on-disk tail substring — per the dispatch reconcile instruction.
- citecheck-scan-bounds: 2 OOB (2 ok, 2 failing). Both OOB are report-PROSE line-references that drifted from the cycle-051 deletions shrinking the index files: `L2-L1/index.md:73` (file now 66 lines) and `L3-L2/index.md:63` (file now 62 lines). Both are non-load-bearing narrative see-also references in D5's Supporting-evidence / Open-questions prose, NOT artifact claims; consequence of D1–D5's own correct deletions (matches D2/D3's flagged cohort-log line-drift). NON-BLOCKING. The load-bearing edits all applied against byte-exact anchors.
- dangling-link (ALL cycle-051 deleted slugs: `{scal,axpy,axpby,axpbypcz,dot,nrm2}-{body,leaf}-identity` + `jacobi-smoother-{body,leaf}-identity` + `divfree-projector-body-identity`): 0 LIVE markdown links survive anywhere in book/src (broadest `]\(...slug...)` grep returns NONE). All 15 deleted theme files confirmed absent; KEPT `divfree-projector-leaf-identity.md` confirmed present.
- fence-parity: 0 (D5 CYCLE.md has 8 ``` markers = 4 balanced edit blocks; no nested fences; no firm chapter body authored)
- retroactive-budget: 0
- SUMMARY chapter registration auto-fix: n/a (count/narrative reconciliation only; no new chapter; D1–D4 already removed the deleted-theme SUMMARY lines)
- index-placeholder displacement: n/a
- implied-component stub: n/a

Tally verification (against on-disk survivor enumeration, all D1–D4 applied):
- L3>L2 firm: 17 → 13 → **5** (correct) — `ls book/src/L3-L2/*.md` minus index = 5: krylov-step-body-identity, ksp-solve-outer-driver, orthogonalize-variant-split, eigsolve-opaque-eigen-iteration, chebyshev-nested-recurrence
- L2>L1 firm: 21 → 17 → **10** (+1 partly-constructive `deflate-composition-lowering` unchanged) — `ls book/src/L2-L1/*.md` minus index = 11 = 10 firm + 1 pc; `divfree-projector-leaf-identity` KEPT
- L3 firm: **UNCHANGED at 17 firm + 3 partial-obstruction** — C touched only the discharge note, not the authoritative line-63 tally

Open questions promoted:
- d5-consolidated-count-applied-refactor-pass-theme-demotion-sweep-complete
- l2-index-and-operator-chapter-historical-narrative-and-stale-future-tense-micro-sweep
- leaf-chapter-disposition-remains-meta-gated-after-cycle-051-theme-demotion

Build-relevant: yes

Notes:
- D5 is the FIFTH and FINAL per-report integrator of cycle-051 (sole consolidated-count owner; D1–D4 deferred all consolidated tallies). Re-read all targets at apply time; D1–D4 are all applied on-disk (15 theme deletions + L3-leaf re-expressions + KEEP confirmed).
- SERIAL-ORDER honored: A.2's `[old]` was D4's change-#6 `[new]` (`17 → 13 → 11`) verbatim — matched on-disk byte-exact because D4 applied first; corrected to FINAL consolidated 5.
- RECONCILE on change C: D5's C `[old]` was the pre-D2 future-tense form of L3/index.md line 65; D2's staging row records it past-tensed part of that line. Applied D5's INTENT against the current on-disk tail (from "The four L3 BLAS-1 leaves" to end-of-line) — the count semantics (L3 unchanged at 17, sweep COMPLETE) are unchanged; only the anchor substring was reconciled to current disk. Per the dispatch's explicit reconcile instruction.
- The 2 citecheck OOB are the same cohort-log line-drift D2/D3 flagged in their OQs (report-prose see-also references, non-load-bearing); integrator-finalize need not act — they are append-only report prose.
- Residual non-build-breaking narrative (L2/index.md historical code-spans naming demoted slugs; stale future-tense in L3/linear_combination.md operator chapter) is OUT of D5's count-owner scope — captured in the promoted micro-sweep OQ for batch-16. Verified these are code-spans / prose, NOT live links — `linkcheck2`-safe.
- deferred integrated_at to finalize per role-spec (did NOT touch the report's frontmatter integrated_at / integration_commit).
- FINAL per-report integrator of cycle-051 — integrator-finalize now runs once on this completed staging log (rebuild + commit + housekeeping).

---
