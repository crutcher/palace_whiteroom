# cycle-020 integrator staging log

Per-report integration staging for cycle-020. One row per `integrator-per-report` invocation,
appended newest-LAST (append-only). `integrator-finalize` reads this log to reconcile the cycle
(rebuild book, commit, housekeeping). Created by the first per-report integrator in cycle-020.

---

## 2026-05-29T034441Z-harvester-orthogonalize-l2-backfill
applied_at: 2026-05-29T044500Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/orthogonalize.md (full-file replacement — recovered the complete firm L2 body)
- scaffolding/open-questions.md (append — new OQ `firm-chapter-body-authored-outside-proposed-changes-fenced-block`)

Gate hits:
- (none) — single full-file-replacement of an existing chapter; no anchor inserts, no slug-creation, no SUMMARY/dep-map auto-fix (both already `firm` from cycle-019, correctly not re-touched per the report).

Open questions promoted:
- firm-chapter-body-authored-outside-proposed-changes-fenced-block (opened_at: cycle-020, opened_by: harvester; routes to meta-phase)

Build-relevant: yes

Notes:
- **CORRECTIVE BACKFILL of a cycle-019 fence-truncation defect.** cycle-019's `orthogonalize` L2
  harvest (integrated `efb8a0b`) landed only the 14-line intro because the firm body sections were
  authored OUTSIDE the report's `edit:` fenced block; `book/src/L2/orthogonalize.md` was a 14-line
  intro with NO `## Status` while `L2/index.md:27` dep-map + `SUMMARY.md:41` already said `firm`.
  This dispatch full-replaced the truncated file with the complete recovered firm chapter (verified
  landed: `## Status` (firm), Signature, Semantics, Algebraic laws, Variant axes, L2-vs-L1, Evidence
  — body closes after the final Evidence bullet `variant-absorption.md:131`). The cycle-019
  truncation bug is NOT reproduced.
- **No dep-map / SUMMARY edit** — the report deliberately proposed none (both already `firm` from
  cycle-019). I confirmed `L2/index.md:27` and `SUMMARY.md:41` both say `firm` and made no change
  (no double-edit).
- **ORDERING CONSTRAINT (for finalize / any later per-report integrator this cycle):** the META
  §Suggested-resolution states this backfill MUST land BEFORE the L2-refresh report
  (`reports/2026-05-29T034441Z-layer-intro-author-l2-refresh/`), whose firm-`orthogonalize`
  assertions depend on this firm body existing. This backfill is applied first (first row in this
  log) — constraint satisfied for whatever per-report integrators the parent dispatches next.
- **Telemetry for the `cargo make book` step (finalize):** the chapter is the first firm-corpus
  consumer of an out-of-book markdown link form `../../../skills/classify-variant-axis/SKILL.md`
  (in §Variant axes). Per the critic this is build-safe under `book.toml`
  `traverse-parent-directories = true` + the `.*/skills/.*` linkcheck-exclude; confirm `cargo make
  book` is clean on it (expected clean — telemetry only).
- The `L2-L1/orthogonalize-composition-lowering` forward-reference correctly stays plain-text (the
  chapter does not exist yet; abstractor follow-up, already in the cycle-019 OQ ledger — not
  re-appended).
- Deferred `integrated_at` to finalize per role-spec (per-report integrator does not touch the
  consumed report's frontmatter).

---

## 2026-05-29T034441Z-abstractor-dot-mutation-rotation
applied_at: 2026-05-29T045500Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/dot-mutation-rotation.md (full-file replacement — stub → firm chapter)
- book/src/L1-L0/index.md (dep-map row appended after the nrm2 row at :27)
- book/src/SUMMARY.md (in-place de-stub at :82 — dropped the ` (stub)` suffix; path unchanged)
- scaffolding/open-questions.md (append — new OQ `dot-mutation-rotation-verified-against-audit`)

Gate hits:
- (none) — full-file replacement of an existing stub chapter (no anchor inserts beyond the dep-map row); the chapter was already SUMMARY-registered (de-stub in place, no SUMMARY auto-fix); no concept_writes, no missing-slug, no forward-edge-without-surface, no H1-page-heading reuse, no variant-axis-missing (two axes declared), no index-placeholder displacement, no implied-component stub creation, no retroactive-budget hit.

Open questions promoted:
- dot-mutation-rotation-verified-against-audit (opened_at: cycle-020, opened_by: abstractor; routes to lowering-verifier — standard verified_against follow-up)

Build-relevant: yes

Notes:
- **stub → firm promotion** of the cycle-020-materialized `dot-mutation-rotation` stub (materialized 2026-05-28). Post-repair report: both citation-validity inline-anchor drifts (`:667`→`:668` ×5, `:679`→`:678` ×3) were fixed in CYCLE.md before this apply; the landed chapter carries the corrected pinpoints (`:668` for the `MFEM_ASSERT`, `:678` for the complex-leaf self-dot imag=`0.0`). Enclosing ranges (`:665-672`, `:674-685`) were always correct.
- **De-stub semantics verified before applying:** SUMMARY.md:82 read exactly `- [dot-mutation-rotation (stub)](./L1-L0/dot-mutation-rotation.md)` — applied as an in-place ` (stub)`-suffix drop (NOT a duplicate append). index.md:27 nrm2 row matched verbatim — applied as an append-after-nrm2 (no pre-existing dot row; no duplicate-row hazard). Critic Issue 4 (informational) confirmed both application semantics.
- **OQ handling:** the report's §Open questions are nearly all already-tracked. `l1-l0-dot-lowering-asymmetry` (constituent of plan item `blas1-l1-l0-lowering-theme-gap`, OQ-ledger :25) is RESOLVED by this firm theme — flagged for meta-phase/finalize to close on the migrated-to-plan constituent (per-report integrator does not close OQs). The caller-audit follow-up maps to the existing OQ `inner-product-conjugate-pair-reorder-caller-classification` (:151) — not re-appended. The bit-determinism half maps to existing `dot-reduction-tree-determinism-survey` (:40) — not re-appended. The `tdot` type-API-surface-only note explicitly needs no new OQ (mirrors existing notes). The lifting note is working-notes-only (lives in the report). Only genuinely-new OQ appended: `dot-mutation-rotation-verified-against-audit` (parallel to the established `nrm2-mutation-rotation-verified-against-audit` pattern at :53).
- Closes the cycle-019 forward-reference from `nrm2-mutation-rotation` sub-pattern A (`nrm2 = √∘abs∘dot`); a lifter re-check of nrm2's collective double-statement is tracked under the existing OQ `nrm2-mutation-rotation-dot-stub-collective-double-statement-recheck` (:52) — now triggerable since dot is firm. Not re-appended.
- **Out-of-book link telemetry for finalize's `cargo make book` step:** the chapter cites `skills/classify-variant-axis` only by name in §Variant axes (no markdown link to the out-of-book SKILL.md), so no linkcheck exposure beyond the orthogonalize-backfill row's already-noted form. All in-chapter `[link]` targets are intra-book and resolve (critic cross-reference-integrity: pass). Expected clean.
- Deferred `integrated_at` / `integration_commit` to finalize per role-spec (per-report integrator does not touch the consumed report's frontmatter).

---

## 2026-05-29T034441Z-abstractor-scal-mutation-rotation
applied_at: 2026-05-29T050500Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/scal-mutation-rotation.md (full-file replacement — stub → firm chapter)
- book/src/L1-L0/index.md (dep-map row inserted after the nrm2 row at :27, before the dot row)
- book/src/SUMMARY.md (in-place de-stub at :84 — dropped the ` (stub)` suffix; path unchanged)
- scaffolding/open-questions.md (append — new OQ `scal-mutation-rotation-verified-against-audit`)

Gate hits:
- (none) — full-file replacement of an existing stub chapter (only anchor insert is the dep-map row); chapter was already SUMMARY-registered (de-stub in place, no SUMMARY auto-fix); no concept_writes, no missing-slug append, no forward-edge-without-surface (all `[link]` targets resolve to existing files), no H1-page-heading reuse, no variant-axis-missing (two axes: element-type real/complex + scalar-promotion), no index-placeholder displacement (index.md Theme-list table is populated, not a placeholder), no implied-component stub creation (no dangling forward-refs), no retroactive-budget hit.

Open questions promoted:
- scal-mutation-rotation-verified-against-audit (opened_at: cycle-020, opened_by: abstractor; routes to lowering-verifier — standard verified_against follow-up, parallel to the nrm2 :53 / dot :54 siblings)

Build-relevant: yes

Notes:
- **stub → firm promotion** of the cycle-020-materialized `scal-mutation-rotation` stub (materialized 2026-05-28). Post-repair report (6 findings all repaired): citation inline-anchor drift `nleps.cpp` `(491)`→`(493)` + range `486-491`→`486-493` fixed in CYCLE.md before this apply; the landed chapter carries the corrected `nleps.cpp:486-493` range and the `v *= 1.0/norm_v;` (493) pinpoint. Sibling-maturity correction landed (the chapter prose + §Summary now accurately say `nrm2` firm, `axpby`/`axpbypcz` rough-in — NOT "fourth-and-last … floor"). Stale-OQ `scalar-promotion-typing-rule` re-framed as resolved-cycle-005 (no live OQ; points at `concepts/scalar-promotion.md`). Dangling slug `normalize-fused-primitive` corrected to the registered `normalize-as-fused-l1-primitive`.
- **De-stub semantics verified before applying:** SUMMARY.md:84 read exactly `- [scal-mutation-rotation (stub)](./L1-L0/scal-mutation-rotation.md)` — applied as an in-place ` (stub)`-suffix drop (NOT a duplicate append). index.md nrm2 row (:27) matched verbatim — inserted the scal row after nrm2 / before the dot row that integration #2 appended (re-read disk: dot's row was present at :28 before this apply; no pre-existing scal row, no duplicate-row hazard). Critic Issue #5 (SUMMARY in-place de-stub) + Issue plan-kind warning (index insert-after-nrm2 idiom) both confirmed the application semantics.
- **OQ handling:** the report's §Open questions are mostly already-tracked or resolved. The scalar-promotion bullet is resolved-cycle-005 (no new OQ). `normalize-as-fused-l1-primitive` is an existing registered OQ (constituent of `normalize-l1-primitive-harvest` plan item) — NOT re-appended (the report flags it for the planner as a fan-out unification across GMRES / power-iteration / nleps normalize sites). Coverage-exhaustiveness folds into the new verified-against-audit OQ. The lifting-note is working-notes-only (lives in the report, not the chapter, per high→low discipline). Only genuinely-new OQ appended: `scal-mutation-rotation-verified-against-audit` (parallel to nrm2 :53 / dot :54).
- **PLAN-ITEM STATE for finalize/meta-phase (do NOT close the parent gap on this landing):** the report instructs striking the constituent slug `scal-mutation-rotation-l1-l0-theme` from the migrated plan item `blas1-l1-l0-lowering-theme-gap` constituent list (`scaffolding/open-questions.md:25`). Per role-spec I did NOT edit that constituent list / close the OQ (OQ-closure on migrated-to-plan constituents is meta-phase/finalize authority, not per-report integrator). **Recorded state, accurately:** the BLAS-1 L1>L0 lowering floor is NOT yet complete after scal lands — `nrm2` firm + `dot` firm (integration #2 this cycle) + `scal` firm (this integration); `axpby`/`axpbypcz` still **rough-in**. So `blas1-l1-l0-lowering-theme-gap` is closing but should NOT be fully closed/resolved on the scal landing. (The repairer explicitly cautioned against closing the gap on scal; note dot firmed in integration #2 earlier this cycle, so the dot constituent `l1-l0-dot-lowering-asymmetry` is also resolved per integration #2's row — finalize/meta-phase should reconcile both constituent strikes together against the still-rough-in axpby/axpbypcz remainder.)
- **Out-of-book link telemetry for finalize's `cargo make book` step:** the chapter has no out-of-book markdown links (no SKILL.md link); all in-chapter `[link]` targets are intra-book and resolve (`L1/scal.md`, `L1-L0/{axpby,axpbypcz,nrm2}-mutation-rotation.md`, `L0/linalg-free-functions.md`, `concepts/scalar-promotion.md` all exist). Expected clean.
- Deferred `integrated_at` / `integration_commit` to finalize per role-spec (per-report integrator does not touch the consumed report's frontmatter).

---

## 2026-05-29T034441Z-abstractor-assemble-diagonal-rotation
applied_at: 2026-05-29T051500Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/assemble-diagonal-mutation-rotation.md (NEW file — fresh firm L1>L0 theme; Write, not a stub promotion)
- book/src/L1-L0/index.md (dep-map row appended after the dot row at :29, before the minres/bicgstab obstruction rows)
- book/src/SUMMARY.md (NEW chapter entry inserted after the scal-mutation-rotation line at :84, before the matrix-weighted-norm stub — NOT a de-stub)
- scaffolding/open-questions.md (append ×2 — new OQs `assemble-diagonal-mutation-rotation-verified-against-audit` + `assemble-diagonal-l1-anchor-absmulttranspose-line-drift`)

Gate hits:
- SUMMARY chapter-registration auto-fix: 0 (the report's SUMMARY block was present + well-formed; applied as-is — NO auto-fix needed). Recorded that the chapter IS registered (gate satisfied).
- (all other gates) — 0. NEW-file firm theme (the only anchor inserts are the dep-map row + the SUMMARY chapter line); no concept_writes; no append-on-missing-slug (the new file is the slug, created first); no forward-edge-without-surface (the in-file `[link]` targets `./apply-linop-mutation-rotation.md` + `../L1/assemble-diagonal.md` both resolve to existing files; the `reciprocal`/`elementwise_product` forward-refs are correctly plain-text, no live link); no edge-label/prose mismatch (L1>L0 throughout); no H1-page-heading reuse; no variant-axis-missing (element-type real/complex axis declared, operator-representation axis absorbed-at-L1 + surfaced as 4 L0 sub-patterns, all non-axes justified); no index-placeholder displacement (the L1-L0/index.md Theme-list table is fully populated, not a placeholder); no implied-component stub creation (no dangling forward-ref needing a stub — the two plain-text forward-refs are speculative-tier, correctly NOT stubbed, and already tracked under OQ `assemble-diagonal-reciprocal-elementwise-product-l1-primitives` :111); no retroactive-budget hit.

Open questions promoted:
- assemble-diagonal-mutation-rotation-verified-against-audit (opened_at: cycle-020, opened_by: abstractor; routes to lowering-verifier — standard verified_against follow-up; folds the report's lowering-verifier-audit, RAP-delegate-sub-pattern, and caveat-lifetime follow-ups into one entry parallel to the nrm2 :53 / dot :54 / scal :319 siblings)
- assemble-diagonal-l1-anchor-absmulttranspose-line-drift (opened_at: cycle-020, opened_by: abstractor; routes to a future L1-entry touch — the repairer-flagged inherited `:172`→`:174` drift in the already-integrated firm L1 anchor `book/src/L1/assemble-diagonal.md` near :111; do NOT fix the L1 entry now per dispatch)

Build-relevant: yes

Notes:
- **FRESH firm L1>L0 theme (NOT a stub promotion).** Unlike integrations #2 (dot) and #3 (scal) this cycle — which were stub→firm full-file replacements with an in-place SUMMARY de-stub — this is a brand-new file `Write` + a brand-new SUMMARY chapter entry (no ` (stub)` suffix existed to drop). The critic confirmed `L1-L0/assemble-diagonal-mutation-rotation.md` did NOT pre-exist (cross-reference-integrity: pass). Closes the cycle-019 harvester forward-reference for this exact theme.
- **Upstream-MFEM OQ NOT re-appended (cross-reference to existing).** The report's §Open-questions upstream-MFEM dependency (real-path `AssembleDiagonal` resolves into vendored MFEM via `using Operator = mfem::Operator`, operator.hpp:21) explicitly asks to cross-reference an existing OQ rather than open a fresh one. That OQ already exists: `assemble-diagonal-mfem-real-path-upstream` (ledger :112, opened cycle-019). NOT re-appended (no duplicate). The forward-refs-stay-plain-text bullet is already tracked under `assemble-diagonal-reciprocal-elementwise-product-l1-primitives` (:111) — also NOT re-appended.
- **THEME-AUTHORING OQ now resolvable (for meta-phase/finalize, do NOT close here):** the ledger entry `assemble-diagonal-mutation-rotation` (:110) was the theme-authoring follow-up whose trigger was "an abstractor L1>L0 dispatch on assemble_diagonal" — that dispatch is THIS report, now landed firm. Per role-spec the per-report integrator does NOT close OQs (meta-phase close authority). Flagged in the new verified-against-audit OQ for the meta-phase to migrate :110 to the Closed index.
- **Dep-map / SUMMARY placement:** dep-map row inserted after the dot row (re-read `L1-L0/index.md` at dispatch time — dot's row from integration #2 was at :29, scal's at :28, both after nrm2 at :27; the report's textual anchor "after nrm2" is satisfied by placing the assemble-diagonal row at the end of the BLAS-1+ cohort, contiguous and before the minres/bicgstab obstruction rows). SUMMARY chapter line inserted after scal (:84) / before the matrix-weighted-norm stub (:85) — re-read `SUMMARY.md`, scal's de-stubbed line from integration #3 was present at :84. Both files were touched by integrations #2 (dot) and #3 (scal) earlier this cycle; I re-read both from disk before editing (no stale cache).
- **Citation-drift repairs already in the report:** post-repair report — the 4 narrow-line-attribution drifts (`AbsMultTranspose :172`→`:174`, `rtol=1.0e-12 :363`→`:360`, `rtol=1.0 :372`→`:371`, ND-Nedelec condition `:367-374`→`:365-369`+`:371`) were all fixed in CYCLE.md before this apply; the landed chapter + verified_against block carry the corrected pinpoints. Enclosing ranges (`rap.cpp:154-193`, `test-libceed.cpp:343-376`) were always correct.
- **`firm` (NOT `partly-constructive`) status confirmed by the critic + repairer:** the matrix-free high-order-Nedelec approximate-diagonal caveat is a **positively-anchored load-bearing non-law** (Palace comment `jacobi.hpp:15-16` naming the approximation + the convergent comment `rap.cpp:163-164` + the test relaxing tolerance `test-libceed.cpp` `rtol=1.0`), NOT a negative-anchor reconstruction — so `partly-constructive` correctly does NOT apply. Landed `firm`.
- **Out-of-book link telemetry for finalize's `cargo make book` step:** the chapter has NO out-of-book markdown links (no SKILL.md link); all in-chapter `[link]` targets are intra-book and resolve (`./apply-linop-mutation-rotation.md`, `../L1/assemble-diagonal.md` both exist). Expected clean.
- Deferred `integrated_at` / `integration_commit` to finalize per role-spec (per-report integrator does not touch the consumed report's frontmatter).

---

## 2026-05-29T034441Z-harvester-l3-ksp-solve
applied_at: 2026-05-29T052500Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L3/ksp_solve.md (NEW file — Write; firm L3 operator entry, the outer-driver `iterate_while_L3` fold over `krylov-step`; genuine iteration-rotation, NOT identity)
- book/src/L3/index.md (dep-map row inserted after the chebyshev row at :29, before `## Working Notes`)
- book/src/SUMMARY.md (NEW chapter entry inserted after `- [chebyshev](./L3/chebyshev.md)` at :29, before the blank line preceding `# L3 > L2 — Lowering`)
- scaffolding/open-questions.md (append ×2 — new OQs `l3-vocabulary-inventory-gap-ksp-solve-resolved-and-remaining-inventory` + `l3-l2-ksp-solve-outer-driver-theme-warranted-gated-on-l2-promotion`)

Gate hits:
- SUMMARY chapter-registration auto-fix: 0 — the report's SUMMARY block (Block 3) was present + well-formed; applied as-is. NO auto-fix needed (the NEW L3 chapter IS registered under the L3 Part). Recorded that the chapter is wired into SUMMARY (gate satisfied).
- (all other gates) — 0. NEW-file firm L3 operator (anchor inserts are only the dep-map row + the SUMMARY chapter line); no concept_writes; no append-on-missing-slug (the new file is the slug, created first via Write — confirmed ABSENT before apply); no forward-edge-without-surface (all in-chapter `[link]` targets resolve to existing files — `./krylov-step.md`, `./apply_linop.md`, `./axpy.md`, `./axpby.md`, `./axpbypcz.md`, `./dot.md`, `./nrm2.md`, `./scal.md`, `./index.md`, `../L1/ksp_solve.md`, `../L2/ksp_solve.md`, `../L2/krylov-step.md`, `../L3-L2/krylov-step-body-identity.md`, all 8 `../concepts/*.md`; the `L3-L2/ksp-solve-outer-driver` theme is correctly plain-text, no live link); no edge-label/prose mismatch (Lowers-to L3→L2 + Lifts-from L3←L1 both narrated in the labelled direction, critic edge-label-fidelity: pass); no H1-page-heading reuse (H1 `# ksp_solve` ≠ the L3 Part heading); no variant-axis-missing (5 loop-shaping axes declared, partitioned against the kernel's 6 body axes); no index-placeholder displacement (the L3 dep-map table is fully populated, not a `(empty — Phase B skeleton.)` placeholder); no implied-component stub creation (see Notes — the one plain-text forward-ref is gated/speculative-tier, correctly NOT stubbed); no retroactive-budget hit (the entry modifies surface AND carries rotation evidence — surface-or-evidence: pass, CRUX).

Open questions promoted:
- l3-vocabulary-inventory-gap-ksp-solve-resolved-and-remaining-inventory (opened_at: cycle-020, opened_by: harvester; routes to cycle-021+ planner + meta-phase — records the `ksp_solve` constituent of plan item `l3-vocabulary-inventory-gap` as done, keeps the parent open against trsv/eigsolve; carries the gemv=done-via-apply_linop / trsv=blocked-no-L1-anchor / eigsolve=next-kernel+driver inventory)
- l3-l2-ksp-solve-outer-driver-theme-warranted-gated-on-l2-promotion (opened_at: cycle-020, opened_by: harvester; deferred/contingent — the L3>L2 rotation is substantive/non-identity so the theme IS warranted but NOT authored this dispatch; gated on L2 `ksp_solve` stub→firm promotion; carries the critic finding-5 layer-edge ratification note for the eventual abstractor)

Build-relevant: yes

Notes:
- **FRESH firm L3 operator (NOT a stub promotion, NOT a corrective backfill).** Distinct from this cycle's earlier rows: not a stub→firm full-file replacement (integrations #2 dot, #3 scal), not a fence-truncation recovery (#1 orthogonalize-backfill). This is a brand-new `Write` of `book/src/L3/ksp_solve.md` + a brand-new SUMMARY chapter entry + a brand-new dep-map row. Confirmed the file did NOT pre-exist (ABSENT before apply; critic cross-reference-integrity also confirmed). Closes the `ksp_solve` portion of the long-advertised `l3-vocabulary-inventory-gap` OQ.
- **The CRUX (surface-or-evidence) is a `pass` that HOLDS:** L3 `ksp_solve` is a **genuine iteration-rotation, NOT identity** — the driver half (outer-driver `iterate_while_L3` fold) carrying the outer-loop `sequential-obstruction`, complementing the firm L3 `krylov-step` kernel half (whose body IS identity-in-form). This is why the entry is a distinct L3 entry rather than a corollary of `krylov-step`, and why its L3>L2 rotation is substantive (not the BLAS-1-cohort clean-identity pattern). The determination is source-grounded and internally consistent across the artifact (critic verified against the `krylov-step` L2/L3 §Context complementarity claims).
- **`L3-L2/ksp-solve-outer-driver` theme NOT authored (correctly deferred):** the report establishes the theme is WARRANTED (substantive L3>L2 rotation) but does not author it — one-op-per-dispatch + high→low discipline (the L3 entry records only rotation direction + non-identity judgment in-line per §"Lowers to"), AND the L2 `ksp_solve` anchor is still a `stub` (no firm L2 RHS to lower into yet). The forward-reference to that theme stays **plain-text** (correct per the rough-in-forward-reference convention — NOT stubbed; it is gated-on-L2-promotion, not clearly-implied-ready). Promoted as OQ `l3-l2-ksp-solve-outer-driver-theme-warranted-gated-on-l2-promotion` with the recommended sequencing (L2 harvester first, then abstractor).
- **Maturity-gradient inversion recorded (for finalize/meta-phase/planner):** this L3 entry is `firm` above a `stub` L2 anchor (`book/src/L2/ksp_solve.md`) — an inversion of the usual high→low maturity gradient, acceptable under **Identity-lowerings still require both L levels** (each layer coherent within itself; the L3 entry is defined in L3 vocabulary independent of the L2 framing). The L2 `ksp_solve` promotion remains the higher-priority follow-on (worth a plan row — flagged in the deferred OQ).
- **OQ-closure / plan-item authority deferred to meta-phase+finalize:** per role-spec I did NOT close or strike the `ksp_solve` constituent of the migrated plan item `l3-vocabulary-inventory-gap` (:24) — recorded as resolvable in the new inventory OQ for the meta-phase to mark done while keeping the parent open against `trsv` (blocked, no L1 anchor) + `eigsolve` (next, scope as kernel+driver).
- **Critic finding-5 (layer-edge judgment) carried forward, not a defect:** the "substantive/non-identity" L3>L2 classification is in mild tension with the kernel sibling `krylov-step-body-identity` "surface adjustment" framing for the *same syntactic collapse*; the report's reconciliation ("for `ksp_solve` the loop IS the operator") is defensible + artifact-consistent. Folded into the deferred theme OQ as a ratification note for the eventual abstractor. No artifact contradiction; no integrator action.
- **Out-of-book link telemetry for finalize's `cargo make book` step:** the chapter has NO out-of-book markdown links (no SKILL.md link); all in-chapter `[link]` targets are intra-book and resolve (verified above + critic cross-reference-integrity: pass). The only non-resolving link the critic flagged (`../book/src/L3/apply_linop.md` in the report's OQ prose, finding-4) was repaired to `./apply_linop.md` BEFORE this apply and is confined to the report prose — NOT in the published chapter body. Expected clean.
- **Citation-range repairs already in the report (post-repair):** the four citation-drift findings were all fixed in CYCLE.md before this apply — accessor cluster `:100-106 → :101-108`, four result fields `→ :52-55`, eps/pre-loop pair `:417-419 → :417-418` (+ lone `:418-419 → :418`). The landed chapter carries the corrected pinpoints (verified the body text uses `:101-108`, `:52-55`, `:417-418`).
- Deferred `integrated_at` / `integration_commit` to finalize per role-spec (per-report integrator does not touch the consumed report's frontmatter).

---

## 2026-05-29T034441Z-lifter-gmres-l4-self-rotation
applied_at: 2026-05-29T053500Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md (9 surgical [old]/[new] edits — Edits 1-9: opening-para firm reframe, §Context slice-ref re-anchor, §"does NOT cover" para + bullet reframe, LHS provenance note flip, variant-axis pass-through citation re-anchor, §Verified-against L4-source bullet, §Open-question disposition, §Status rough-in → firm + sibling/lowering-verifier notes)
- book/src/spec/slices/gmres.md (Edit 10 — appended the §L4 v0.7 inner-loop iterate_while migration self-rotation section after the v0.6 §"Open questions" final bullet at :671; re-quoted the final bullet verbatim then appended)
- scaffolding/open-questions.md (append ×3 — new OQs `gmres-l4-standalone-operator-entry-vs-slice-l4-placement`, `fgmres-inner-loop-iterate-while-migration-firm-against-gmres-sibling`, `gmres-l4-l3-theme-dep-map-firm-sync`)

Gate hits:
- forward-edge-without-surface: 0 — the theme flips to `firm` WITH its LHS surface landing this same apply (the slice §L4 v0.7 section, Edit 10). The theme's LHS is no longer speculative; surface-or-evidence holds. The fgmres-sibling and `L3/krylov-step`/`krylov-step-typed-wrapper-dissolution` `[link]`s all resolve to existing files (critic cross-reference-integrity: pass).
- index-placeholder displacement: 0 — N/A. No `L4/index.md` edit applied (the dep-map firm-sync is NOT in the proposed-changes blocks; routed to finalize/layer-intro-author per report OQ 3 — see Notes). The L4 dep-map rows are populated, not `(empty — Phase B skeleton.)` placeholders.
- implied-component stub materialization: 0 — NOT triggered. The report chose the conservative slice §L4 + theme-LHS home; did NOT create a standalone `book/src/L4/gmres.md` (harvester-scope new-operator decision, surfaced as OQ `gmres-l4-standalone-operator-entry-vs-slice-l4-placement`). The `check_stop_into_carry` speculative L4 helper stays `rough-in` with a plain-text dep-map row (per `rough-in-rows-must-be-plain-text-when-anchor-missing`) — correctly NOT stubbed/promoted (harvester decision; FGMRES is the second-consumer promotion trigger).
- (all other gates) — 0. Surgical [old]/[new] edits to an existing firm-flipping theme + a self-rotation append to an existing slice; no concept_writes, no append-on-missing-slug, no SUMMARY auto-fix (both files already SUMMARY-registered; no new chapter), no H1-page-heading reuse, no variant-axis-missing (the four GMRES axes are addressed + shown to pass through the rotation; critic variant-axis-coverage: pass), no edge-label/prose mismatch (L4>L3 narrated forward; self-rotation framed L4→L4; critic edge-label-fidelity: pass), no retroactive-budget hit.

Open questions promoted:
- gmres-l4-standalone-operator-entry-vs-slice-l4-placement (opened_at: cycle-020, opened_by: lifter; routes to cycle-021+ planner — structural-home decision, harvester scope)
- fgmres-inner-loop-iterate-while-migration-firm-against-gmres-sibling (opened_at: cycle-020, opened_by: lifter; deferred/HELD — routes to a cycle-021 follow-up lifter dispatch against this now-firm gmres sibling)
- gmres-l4-l3-theme-dep-map-firm-sync (opened_at: cycle-020, opened_by: lifter; routes to integrator-finalize / layer-intro-author — the L4/index.md:44 + :53 rough-in→firm dep-map sync, fgmres row STAYS rough-in)

Build-relevant: yes

Notes:
- **LIFTER self-rotation + theme firm-flip (NOT a stub promotion, NOT a new file).** Edits 1-9 are surgical `[old]`/`[new]` prose/status edits firming the rough-in L4>L3 theme `gmres-inner-loop-iterate-while-migration` (rough-in → firm); Edit 10 appends the upstream gmres §L4 v0.6→v0.7 self-rotation (the LHS the theme firms against) to the slice. All 10 `[old]` anchors matched on-disk verbatim before edit (re-read the theme + the slice §671 anchor at dispatch time).
- **cg.md:215-219 repair already in the report (post-repair) — applied as-is.** The repairer re-anchored all three NEW-content re-emissions of the stale `cg.md:215-219` CG-precedent ref to the firm `L4/krylov-step.md` §Semantics Form A (+ the in-range `cg.md:86-108` for the residual cg-slice material). I applied the `[new]` content carrying those repaired refs. Per the repairer's note, the surviving `cg.md:215-219` inside Edit 2's `[old]` ANCHOR block is the verbatim on-disk theme §Context text required for anchor-matching — it matched disk exactly and the `[new]` I wrote does NOT carry the stale ref. Landed §Context + slice-append prose + slice-append §Citations all point at `L4/krylov-step` Form A / `cg.md:86-108`.
- **DEP-MAP FIRM-SYNC NOT APPLIED HERE — routed to finalize/layer-intro-author (report OQ 3).** The `rough-in → firm` flip means `book/src/L4/index.md:44` (theme row) + `:53` (`iterate-while` "Lowers to" cell) carry stale `*(rough-in; landed cycle-008 wave-2)*` annotations that must sync to `*(firm; cycle-020 wave-1 lifter re-anchor)*`. The report **deliberately did NOT emit this as a proposed-change block** (dep-map wording is layer-intro-author territory); I did NOT improvise the `L4/index.md` edit. Promoted as OQ `gmres-l4-l3-theme-dep-map-firm-sync` so finalize/layer-intro-author syncs it — a firm theme with a rough-in dep-map annotation is a cross-reference-integrity drift. **The fgmres sibling row STAYS rough-in** (held for cycle-021); only the gmres theme row + the iterate-while "Lowers to" cell flip.
- **OQ-closure deferred to meta-phase/finalize (do NOT close here):** Edit 8 proposes closing the cycle-007 OQ `gmres-inner-loop-iterate-while-migration` as `resolved`. That OQ has a Closed-index entry at `scaffolding/open-questions.md:192` (`answered-by-rough-in-theme cycle-008`). Per role-spec the per-report integrator does NOT close/edit OQ-ledger Closed-index entries (meta-phase authority); I left :192 unchanged. **Recorded for meta-phase/finalize:** update :192 to `resolved cycle-020` (the migration landed firm, slice §L4 v0.7, option (a) `check_stop_into_carry`). The two OTHER OQs the theme touches (`iterate-while-l3-rendering-trajectory-accumulation-gap`, `iterate-while-log-effect-vs-trajectory-channel`) are explicitly NOT closed by this dispatch (stay open).
- **fgmres sibling forward-reference is a LIVE link, not plain-text** — `[fgmres-inner-loop-iterate-while-migration](./fgmres-inner-loop-iterate-while-migration.md)` (Edit 9 §Status). The target file EXISTS (critic cross-reference-integrity: pass), so the live link is correct (not a dangling forward-ref needing plain-text/stub). The sibling stays `rough-in` content-wise; only its firm-flip is held for cycle-021.
- **Out-of-book link telemetry for finalize's `cargo make book` step:** all in-chapter/in-slice `[link]` targets are intra-book and resolve (`../L4/iterate-while.md`, `../L4/iterate-while-with-prev.md`, `../L4/krylov-step.md`, `../L3/krylov-step.md`, `./krylov-step-typed-wrapper-dissolution.md`, `./fgmres-inner-loop-iterate-while-migration.md`; slice-append `../../L4/iterate-while.md`, `../../L4/krylov-step.md`, `../../L4-L3/gmres-inner-loop-iterate-while-migration.md`, `../../concepts/derived-view-hoisting.md`). No out-of-book SKILL.md links. Expected `cargo make book` clean.
- Deferred `integrated_at` / `integration_commit` to finalize per role-spec (per-report integrator does not touch the consumed report's frontmatter).

---

## 2026-05-29T034441Z-lowering-verifier-inner-product-fold
applied_at: 2026-05-29T054500Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2-L1/inner-product-fold-specialization.md (append at end of file — the standard `verified_against:` fenced yaml block recording 15 audit rows + `coverage_verdict: fully-supported` + `status_recommendation: keep firm` + `audit_caveat`)
- scaffolding/open-questions.md (append — new OQ `inner-product-fold-specialization-operator-cpp-inline-anchor-drift`)

Gate hits:
- (all gates) — 0. Pure metadata append (a `verified_against:` yaml block) at end of an EXISTING firm chapter; no status change (theme stays `firm`, audit verdict `fully-supported`). No anchor inserts, no slug-creation, no SUMMARY/dep-map touch, no concept_writes, no append-on-missing-slug, no forward-edge-without-surface, no edge-label/prose mismatch, no H1-page-heading reuse, no variant-axis-missing, no index-placeholder displacement, no implied-component stub creation, no retroactive-budget hit. Audit-shape report (read-only verification emitting a `verified_against:` append) — the citation/surface/rotation/variant-axis checks no-op on a metadata-only append.

Open questions promoted:
- inner-product-fold-specialization-operator-cpp-inline-anchor-drift (opened_at: cycle-020, opened_by: lowering-verifier; routes to a future `lifter` dispatch / integrator carry-forward touch — the 3 genuine inline-anchor corrections `:623`→`:624`, `:632`→`:634`, `:615-616`→`:616` on the theme's `operator.cpp` anchors; NOT a status reduction)

Build-relevant: yes

Notes:
- **LOWERING-VERIFIER audit, `fully-supported` / keep firm.** Post-repair report (critic `citation-validity: warning` → repairer `repaired`): the repairer dropped the phantom `:611`→`:612` SPD-comment "drift" (the live theme already pins `:612`; `:611` appears nowhere in the committed file) and kept the **3 genuine** inline-anchor corrections (`Ax` `:623`→`:624`, `:632`→`:634`; SPD assertion range `:615-616`→`:616`). The `verified_against:` block I appended carries exactly the repaired content (15 audit rows; the `operator.cpp:598-617` row is `partially-supports` noting the SPD comment is already `:612` + the assertion narrows to `:616`; the two `Ax` rows are `supports` with INLINE-drift notes; the `audit_caveat` lists the three genuine drifts and parenthesizes the SPD comment as already-`:612`).
- **The 3 inline-anchor corrections are NOT applied as edits this dispatch — they are NOT in the report's proposed-changes blocks** (the only proposed-change is the `verified_against:` metadata append; the report explicitly surfaces the 3 corrections as a "carry-forward for a follow-up lifter dispatch / integrator carry-forward touch", NOT as edit blocks). So I recorded them ONLY in the new OQ `inner-product-fold-specialization-operator-cpp-inline-anchor-drift` for a future lifter/integrator touch (per dispatch + per the report's carry-forward framing). The theme's inline `operator.cpp:623`/`:632`/`:615-616` anchors in §"The weighted-member workspace" / §"diagonal degeneration" / §Verified-against are LEFT AS-IS this cycle (drift documented, not fixed).
- **§Condition 5 LEFT INTACT for the next report (integration #8, dot-callers).** Per dispatch: the next per-report integrator will append a `conjugation_caller_inventory:` block to §Condition 5 (the §"Applicability conditions" item 5, the file's lines ~284-289). I appended the `verified_against:` yaml at END OF FILE (per the report's `[append at end of file]` directive), which does NOT touch §Condition 5 or the human-prose §Verified-against section (lines ~336-400). The file is clean for #8's §Condition 5 append.
- **OQ handling:** the report's other §Open-questions items are all already-tracked or working-notes-only — NOT re-appended: the lifting note is working-notes-only (lives in the chapter §Open-questions, high→low discipline); `linear-combination-fold-specialization-theme-followups` is already-tracked (ledger :154, the report recommends resolvable-on-the-sibling-side for meta-phase to assess); the weighted-member two-stage tree folds into `apply-linop-lowering-verifier-audit-cohort` (:57) + the explicit cross-ref `inner-product-weighted-member-two-stage-reduction-tree` (:153); the conjugate-pair caller audit maps to `inner-product-conjugate-pair-reorder-caller-classification` (:152) + `dot-reduction-tree-determinism-survey` (:40); the plan/OQ bookkeeping recommendation (close `inner-product-harvester-formalization-and-conjugation-pinning` :140, flip plan Now #2) is meta-phase/finalize authority, NOT actioned here. Only genuinely-new OQ appended: the inline-anchor-drift follow-up.
- **PLAN-ITEM STATE for finalize/meta-phase (do NOT close here):** this audit confirms-firm plan **Now (active) #2** (`L2-L1/inner-product-fold-specialization`) — recorded as audited/firm-confirmed (the standard lowering-verifier follow-up the theme's §Status named). Per role-spec I did NOT close/flip the plan item or close `inner-product-harvester-formalization-and-conjugation-pinning` (:140, RESOLVED-by-dispatch-#1, flagged for meta-phase close) — meta-phase/finalize authority.
- **Out-of-book link telemetry for finalize's `cargo make book` step:** the appended `verified_against:` yaml block introduces NO markdown links (plain-text citation strings only); the chapter's existing in-chapter `[link]` targets are unchanged + all intra-book. Expected `cargo make book` clean (metadata-only append to an already-building chapter).
- Deferred `integrated_at` / `integration_commit` to finalize per role-spec (per-report integrator does not touch the consumed report's frontmatter).

---

## 2026-05-29T034441Z-cross-layer-cross-cutter-dot-callers
applied_at: 2026-05-29T055500Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2-L1/inner-product-fold-specialization.md (anchor-insert into §Applicability — Condition 5: a "Caller-site conjugation inventory" prose lead-in + the `conjugation_caller_inventory:` fenced yaml block, placed AFTER Condition 5's prose / BEFORE `## Justification kind`)
- scaffolding/open-questions.md (append ×3 — new OQs `dot-conjugation-observable-callers-nleps-cohort`, `nleps-deflation-subspace-projection-combinator-deflate-gram`, `orthog-hpp-localdot-globalsum-unweighted-inner-product-surface`)

Gate hits:
- (all gates) — 0. Additive evidence block (Condition 5 caller-site inventory) into an EXISTING firm chapter; no status change (theme stays `firm`). No retroactive-budget hit (additive, no surface rewrite); no concept_writes; no forward-edge-without-surface (all cited L0 sites are census evidence, critic citation-validity: pass post-`:534` repair); no edge-label/prose mismatch; no H1-page-heading reuse (the inserted `**Caller-site conjugation inventory**` is a bold sub-note under numbered list item 5, not a new H1); no append-on-missing-slug (theme file exists); no variant-axis-missing (census/observation report — critic variant-axis-coverage: pass, N/A); no SUMMARY/dep-map touch (no new file/slug/row); no index-placeholder displacement; no implied-component stub creation (no dangling forward-ref). Census/observation-shape report — the citation/surface/rotation/variant-axis checks no-op on an additive evidence append.

Open questions promoted:
- dot-conjugation-observable-callers-nleps-cohort (opened_at: cycle-020, opened_by: cross-layer-cross-cutter; evidence-complete — also RECORDS that the pre-existing OQ `inner-product-conjugate-pair-reorder-caller-classification` (:152) is RESOLVED by this census, flagged for meta-phase to migrate/close — NOT closed here per role-spec)
- nleps-deflation-subspace-projection-combinator-deflate-gram (opened_at: cycle-020, opened_by: cross-layer-cross-cutter; combinator candidate — the recurrent `X[j]ᴴ·` deflation-subspace projection pattern in nleps.cpp; routes to combinator-miner + plan candidate)
- orthog-hpp-localdot-globalsum-unweighted-inner-product-surface (opened_at: cycle-020, opened_by: cross-layer-cross-cutter; coverage gap — the second unweighted inner-product surface routing through `LocalDot`+`GlobalSum` that the Dot-caller census did not cover; routes to same-layer-cross-cutter / harvester)

Build-relevant: yes

Notes:
- **CROSS-LAYER CENSUS evidence-backfill (additive, NOT a status change).** This is integration #8, the dot-callers census. The proposed-changes block is a single `conjugation_caller_inventory:` evidence block; I placed it inside **§Applicability — Condition 5** (lines ~284-289 of the live chapter), AFTER Condition 5's prose and BEFORE `## Justification kind`, with a one-paragraph `**Caller-site conjugation inventory**` lead-in summarizing the headline (load-bearing in exactly one algorithm — SLEPc-NEP `nleps.cpp`, at 4 observable sites; `palace/fem/` has zero Dot callers; 11 invisible + 4 observable = 15 caller sites). The report offered two carriers (Condition 5 evidence block OR OQ-only); I applied the **Condition 5 block** (the report's preferred carrier, and the theme's own §Open-questions caller-audit item at lines 469-478 anticipated exactly this) AND opened the OQ — both, not either/or, so the inventory is both surfaced in the chapter and tracked for the combinator/orthog.hpp follow-ups.
- **#7's `verified_against:` block at EOF NOT disturbed.** Per dispatch, integration #7 (lowering-verifier) appended a `verified_against:` yaml block at END OF FILE (lines ~488-553). I re-read the file fresh at dispatch time (confirmed #7's block present, terminating with the closing ``` fence at :553), and inserted the Condition 5 inventory ~200 lines ABOVE it — the EOF block is untouched. The chapter now carries BOTH the §Condition 5 caller inventory (this report) and the EOF audit `verified_against` block (#7), non-overlapping.
- **Pre-existing OQ RESOLVED (do NOT close here):** the ledger OQ `inner-product-conjugate-pair-reorder-caller-classification` (:152) requested EXACTLY this caller audit ("classify every `linalg::Dot` site real-projected vs full-complex … tighten the re-order story to per-site precision"). The census resolves it. Per role-spec the per-report integrator does NOT close OQs (meta-phase authority) — recorded the resolution in the new `dot-conjugation-observable-callers-nleps-cohort` OQ for meta-phase/finalize to migrate/close :152. The bit-determinism sibling `dot-reduction-tree-determinism-survey` (:40) stays open (not addressed by this census). Did NOT re-append :152 or :40.
- **Two NEW follow-ups surfaced (per dispatch flag), opened as fresh OQs:** (1) `nleps-deflation-subspace-projection-combinator-deflate-gram` — the recurrent `X[j]ᴴ·` deflation-subspace projection pattern (`:522,:529,:568`) is a combinator-miner candidate (`deflate`/`gram` over an invariant-pair basis `X`), pins the conjugation convention once at the combinator boundary; (2) `orthog-hpp-localdot-globalsum-unweighted-inner-product-surface` — `orthog.hpp:35` (`return LocalDot(x,y)`) is a SECOND unweighted inner-product surface bypassing `linalg::Dot` (routes through `LocalDot`+`GlobalSum`), out of the Dot-caller census, likely a coverage-gap extension to Condition 5 (Gram-Schmidt coefficients generally observable). Both framed as candidates/coverage-gaps, not enacted.
- **The report's `:534` MatVecMult-anchor + the 11/15 tally were already reconciled in the report (post-repair)** — the landed inventory yaml carries the census as repaired (the `observable_unweighted` rows cite `:522,:529,:568,:675` and the prose lead-in states 11 invisible + 4 observable = 15 caller sites, matching the repaired §Summary / §Risk-inventory item 2). No content of mine re-derives the tally; I applied the report's proposed yaml verbatim (it carries the corrected `:534` flow implicitly via the `:522` comment, and the line-anchor drift was confined to the report's table prose, not the yaml block).
- **Out-of-book link telemetry for finalize's `cargo make book` step:** the inserted block is a fenced `yaml` code block of plain-text citation strings (no markdown links); the surrounding Condition 5 prose adds no new `[link]`. All the chapter's existing in-chapter links are unchanged + intra-book. Expected `cargo make book` clean (additive evidence block to an already-building firm chapter).
- Deferred `integrated_at` / `integration_commit` to finalize per role-spec (per-report integrator does not touch the consumed report's frontmatter).

---

## 2026-05-29T034441Z-layer-intro-author-l2-refresh
applied_at: 2026-05-29T060500Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/index.md (2 surgical [old]/[new] section rewrites — Block 1: §"Semantics (overlay)" + two emergent motifs + NEW §"Vocabulary cohort" subsection + 5-row→7-row §"Operator dep-map" rewrite at :15-27; Block 2: §"Working Notes" — replaced the single stale cycle-005-deferral bullet at :42 with 4 refreshed bullets)
- scaffolding/open-questions.md (append ×1 — new OQ `l2-index-ksp-solve-l3-crossref-upgrade-now-possible`)

Gate hits:
- (all gates) — 0. Two surgical [old]/[new] section rewrites of an EXISTING Part-overview index.md (no new file/slug, no anchor-insert into a foreign region); no SUMMARY auto-fix (all 7 L2 chapters — incl. the two stub rows — were already SUMMARY-registered at SUMMARY.md:37-43; no new chapter, no chapter-registration auto-fix needed); no append-on-missing-slug (both stub rows `incremental-least-squares.md` + `ksp_solve.md` exist on disk + are SUMMARY-wired, so their LIVE `[slug](./slug.md)` links are build-safe — NOT plain-text-fallback); no implied-component stub creation (both stubs pre-exist from the 2026-05-28 materialization — nothing to materialize); no concept_writes; no forward-edge-without-surface (the firm-orthogonalize assertions now have their surface — see ordering note; the L3-ksp_solve cross-ref is correctly plain-text); no edge-label/prose mismatch (the `firm`/`stub` dep-map status column matches on-disk after the backfill landed); no H1-page-heading reuse (no new H1; the NEW `## Vocabulary cohort` is an H2 section, not a page-heading reuse); no variant-axis-missing (structural intro/dep-map refresh — N/A, critic variant-axis-coverage: pass); no index-placeholder displacement (the L2 dep-map is a populated table, NOT a `(empty — Phase B skeleton.)` placeholder — this was a full-section rewrite, not a first-firm-row displacement); no retroactive-budget hit (structural refresh, no rotation-claim, surface-or-evidence: pass).

Open questions promoted:
- l2-index-ksp-solve-l3-crossref-upgrade-now-possible (opened_at: cycle-020, opened_by: layer-intro-author; deferred follow-up — the L2-index Working Note's L3-`ksp_solve` complementarity bullet stays plain-text this cycle but `L3/ksp_solve.md` now exists (integration #5), so a future layer-intro-author/lifter touch can upgrade it to a live link + reconcile the L2-stub non-identity framing against the firm L3 entry; routes alongside plan item `ksp-solve-l2-promotion-non-identity-substantive-gap`)

Build-relevant: yes

Notes:
- **LAST report of cycle-020 (integration #9).** Structural L2 Part-overview refresh — NOT a stub promotion, NOT a new file. Two surgical `[old]`/`[new]` section rewrites of `book/src/L2/index.md`; both `[old]` anchors matched live disk VERBATIM (re-read fresh at dispatch — Block 1 reproduced :15-27 exactly, Block 2 reproduced the :42 bullet exactly). No other cycle-020 report touched `L2/index.md` (confirmed across all 8 prior staging rows — none lists `book/src/L2/index.md`), so disk was unmodified from authoring time; no drift-re-match needed.
- **ORDERING PRECONDITION SATISFIED (load-bearing, verified).** The META §Suggested-resolution made this report `ready` contingent on the orthogonalize firm-body backfill (`harvester-orthogonalize-l2-backfill`) landing BEFORE it — required because this report's `firm`-orthogonalize dep-map row + named-composition-cohort framing + "orthogonalize is now firm" Working Note assert a firm body that the cycle-019 fence-truncation defect had stripped to a 14-line intro. CONFIRMED: that backfill is **row #1** of this staging log (status: applied; full-file-replacement landed `## Status: firm` + Signature + 7 algebraic laws + Variant axes + Evidence on disk). So all of this report's firm-orthogonalize assertions are now correct against on-disk state — the critic's two FAILs (citation-validity, edge-label-fidelity) + the cross-reference-integrity warning are all dissolved post-backfill. Applied with the precondition met.
- **`inner_product` sibling-fold re-label is correct on disk:** Block 1's `orthogonalize` row now reads "Sibling fold (constituent, not parent): `inner_product` (firm)" — corrects the prior stale live `(rough-in)` label; `inner_product.md` is `firm` on disk (critic verified `:408`). The fold-cohort do-NOT-merge boundary is now carried in BOTH `inner_product`'s and `linear_combination`'s dep-map rows (codomain distinction `Scalar` vs `Tensor[N]` — load-bearing, preserved verbatim).
- **2 stub rows use LIVE links (correct, NOT plain-text):** `[incremental-least-squares.md](./incremental-least-squares.md)` + `[ksp_solve.md](./ksp_solve.md)` — both anchor files exist on disk (materialized 2026-05-28) and are SUMMARY-wired (SUMMARY.md:42-43), so the live-link form is build-safe; the plain-text-when-anchor-missing convention does NOT apply (per the report's §Supporting-evidence + critic cross-reference-integrity: pass).
- **L3 `ksp_solve` cross-ref LEFT AS PLAIN-TEXT (per dispatch directive — deliberately NOT upgraded).** The report kept the L2-index Working Note's L3 driver/kernel-complementarity reference as a plain-text forward-reference (because `L3/ksp_solve.md` did not exist at authoring time). Integration #5 THIS cycle (`harvester-l3-ksp-solve`, staging row #5) created `book/src/L3/ksp_solve.md`, so a live link is NOW technically possible — BUT per the dispatch directive I left the report's plain-text choice exactly as authored (build-safe either way; no broken link in EITHER form). I did NOT alter the report's plain-text choice. The now-possible upgrade is captured as the deferred OQ `l2-index-ksp-solve-l3-crossref-upgrade-now-possible` for a future touch.
- **OQ handling:** of the report's four §Open-questions items, only ONE is genuinely-new and appended: `l2-index-ksp-solve-l3-crossref-upgrade-now-possible` (the L2→L3 cross-ref upgrade, now actionable since `L3/ksp_solve.md` landed integration #5 — a distinct follow-up from #5's own OQs `l3-vocabulary-inventory-gap-ksp-solve-resolved-and-remaining-inventory` :341 + `l3-l2-ksp-solve-outer-driver-theme-warranted-gated-on-l2-promotion` :356, which track the L3-side / L3>L2-theme side, not the L2-index lag). The other three items are NOT re-appended: (2) stub-row-signatures-are-placeholders folds into the existing per-stub OQs `incremental-least-squares-as-future-L2-firstclass-entry` + `ksp-solve-l2-promotion-non-identity-substantive-gap` (both cited in the dep-map rows — same harvester-refinement they already track); (3) no-rough-in-cohort is a working-notes-only structural caveat (no OQ warranted); (4) `scalar-promotion` open dependency is explicitly carried-verbatim/unresolved and already tracked by the existing OQ `scalar-promotion-typing-rule`.
- **Out-of-book link telemetry for finalize's `cargo make book` step:** the refresh introduces NO out-of-book markdown links (no SKILL.md link); all `[link]` targets in the rewritten sections are intra-book and resolve — the 5 firm chapter links (`./krylov-step.md`, `./chebyshev-iteration.md`, `./linear_combination.md`, `./inner_product.md`, `./orthogonalize.md`) + the 2 stub links (`./incremental-least-squares.md`, `./ksp_solve.md`) all exist on disk. The L3-`ksp_solve` reference is plain-text (no link). Expected `cargo make book` clean.
- Deferred `integrated_at` / `integration_commit` to finalize per role-spec (per-report integrator does not touch the consumed report's frontmatter).

---
