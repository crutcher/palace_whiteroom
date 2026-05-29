# Cycle-019 integrator staging log

Per-report integrators append one row each (newest LAST, append-only). integrator-finalize reads this
as the authoritative landing record to reconcile the cycle (rebuild, commit, housekeeping).

---

## 2026-05-29T023000Z-layer-intro-author-fespace-l0
applied_at: 2026-05-29T04:05:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L0/fespace-file.md (created — new L0 source-anchor chapter for palace/fem/fespace.{hpp,cpp})
- book/src/SUMMARY.md (edited — inserted L0 file-overview row for fespace-file between fem-libceed-operator-file:103 and the MPI-collectives row:104)
- book/src/L0/index.md (edited — inserted fespace-file bullet into the "File overviews" cohort, after the fem-bilinearform-file bullet)
- scaffolding/open-questions.md (appended — new "fem / FE-space family" group under §Open — deferred / contingent, 3 OQs)

Gate hits:
- SUMMARY chapter registration auto-fix: 0 (report proposed the SUMMARY insert itself; new file registered via block 2 — no auto-fix needed)
- index-placeholder displacement: 0 (no placeholder; index "File overviews" is a live cohort list)
- implied-component stub materialization: 0 (forward-refs — libceed basis/restriction, quadrature, geometric factors — correctly plain-text per the report; only speculative-vs-clearly-implied bar not met for a stub this pass; left as OQ fem-libceed-basis-restriction-l0-anchor)
- forward-edge / edge-label / variant-axis / H1-reuse / retroactive-budget: 0 (n/a — L0 descriptive source-anchor, no rotation/edge/variant claims; critic passed all 8 checks)
- append-on-missing-slug: 0

Open questions promoted:
- fem-libceed-basis-restriction-l0-anchor (folds the deferred quadrature + geometric-factor regions)
- l0-index-summary-file-overview-drift-libceed-operator
- fespace-tvector-lvector-workspace-prose-treatment

Build-relevant: yes

Notes:
- All three proposed-changes blocks applied verbatim from the repaired CYCLE.md (the repairer's one MINOR
  fix — finding 1, the `diag = 0.0` citation 122→121 in §Evidence + §Supporting evidence of the report — is
  internal to the report's evidence prose, not the operator body I wrote; the operator body's matrix-free
  Evidence bullet already reads "line 121" as I transcribed it).
- Anchors re-read on disk before each Edit: L1/assemble-diagonal.md (full stub-body confirmed present —
  status:stub blockquote at line 3), L1/index.md ("Firm (11)" cohort header at :29, divfree-projector firm
  bullet at :41, divfree-projector dep-map row at :75), SUMMARY.md ("- [assemble-diagonal (stub)]..." at :67)
  — all matched the report's proposed [old] strings verbatim.
- deferred integrated_at to finalize per role-spec.

Second per-report integrator in cycle-019 (after fespace-l0).

---

## 2026-05-29T023000Z-harvester-assemble-diagonal-l1
applied_at: 2026-05-29T04:35:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/assemble-diagonal.md (full-rewrite — stub → firm; flipped the `status: stub` placeholder body to the firm operator-to-data entry: signature `(A: LinearOperator[N,N]) -> Tensor[N]`, 6 algebraic laws + 4 non-laws, element-type live axis + operator-representation absorbed axis + 3 non-axes, exhaustive Evidence across operator/rap/hypre/libceed + the two smoother consumers + the libceed diagonal-assembly test)
- book/src/L1/index.md (edited — 3 wiring edits: cohort count `**Firm (11)**` → `**Firm (12)**` at the Vocabulary-cohort header; appended the `assemble-diagonal` firm-cohort bullet after the `divfree-projector` bullet; appended the `assemble-diagonal` dep-map row after the `divfree-projector` row)
- book/src/SUMMARY.md (edited — dropped the `(stub)` label on the L1 chapter line: `- [assemble-diagonal (stub)](./L1/assemble-diagonal.md)` → `- [assemble-diagonal](./L1/assemble-diagonal.md)`)
- scaffolding/open-questions.md (appended — new "### assemble-diagonal / diagonal-preconditioning family" group under §Open — deferred / contingent, opened_at: cycle-019 / opened_by: harvester, 5 OQs)

Gate hits:
- retroactive-budget: 0 (stub→firm promotion authoring fresh surface; not a retroactive backfill)
- forward-edge / edge-label / variant-axis / H1-reuse: 0 (L1 operator entry, lowering deferred to a forthcoming L1>L0 theme — no L_{n+1}→L_n edge proposed; element-type axis declared + operator-representation absorption + non-axes all documented; H1 `# assemble-diagonal` is the canonical slug-named heading, not a page-heading reuse)
- SUMMARY chapter registration auto-fix: 0 (chapter already registered — this report de-stubs the existing line; no new file to register)
- append-on-missing-slug: 0 (all three targets existed; index appends anchored after divfree-projector matched verbatim)
- index-placeholder displacement: 0 (the L1 "Firm" cohort + dep-map are live lists, no placeholder text)
- implied-component stub materialization: 0 (per dispatch instruction — the forward-refs `reciprocal` / `elementwise_product` and the `assemble-diagonal-mutation-rotation` L1>L0 theme stay PLAIN-TEXT this pass; each is a singleton reference, NOT clearly-implied by ≥2 converging refs, so the stub bar is not met — left as plain-text + OQ per the speculative-fallback rule)

Open questions promoted:
- assemblediagonal-is-not-apply-linop-variant (recorded RESOLVED-by-this-harvest with the firm entry as resolution-anchor; meta-phase closes/migrates per write-authority partition)
- assemble-diagonal-mutation-rotation (Backlog migration — abstractor L1>L0 theme; pair with diagonal-extraction-l1)
- assemble-diagonal-reciprocal-elementwise-product-l1-primitives (Backlog migration — forthcoming L1 primitives)
- assemble-diagonal-mfem-real-path-upstream (upstream-behaviour dependency; non-blocking, cross-layer-pass trigger)
- l1-index-fifth-motif-operator-to-data-introspection (layer-intro-author refresh flag)

Build-relevant: yes

Notes:
- The MFEM-upstream real-path dependency the dispatch flagged is promoted as OQ
  `assemble-diagonal-mfem-real-path-upstream` (does not block firm — all surfaced smoother consumers call
  into overriding subclasses; the entry cites Palace call-sites/overrides, not the MFEM base virtual's body,
  per CLAUDE.md upstream-symbol policy).
- The report's §Open-questions ALSO requested closing OQ `assemblediagonal-is-not-apply-linop-variant` and
  filing three Backlog migrations + a layer-intro fifth-motif flag. Per CLAUDE.md §Write-authority partition,
  OQ close/migrate is meta-phase authority (I only append). I recorded all five as OQ entries (the close one
  marked RESOLVED-by-this-harvest with the firm entry as resolution-anchor); meta-phase enacts the close +
  the plan migrations.
- deferred integrated_at to finalize per role-spec.

---

## 2026-05-29T023000Z-abstractor-nrm2-l1-l0
applied_at: 2026-05-29T05:05:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/nrm2-mutation-rotation.md (full-rewrite — stub → firm; dropped the `status: stub` blockquote + "What this will be"/"Implied by"/"Refinement pending" placeholder body; wrote the firm L1>L0 theme: L1 LHS `alpha = nrm2(x)`, L0 RHS one-line `Norml2` template + the four-stage `Dot→MPI_Allreduce→std::abs→std::sqrt` chain, 3 surface forms A/B/C, the `std::abs` load-bearing-defensive-guard classification, applicability conditions, element-type variant-axis collapse, verified-against L0 ranges, `Status: firm`)
- book/src/L1-L0/index.md (edited — inserted the `nrm2-mutation-rotation` firm dep-map row into the Theme-list table, between the `orthogonalize-mutation-rotation` row and the `minres-iteration` row; L1 anchor `L1/nrm2` (firm), L0 anchors `vector.hpp`/`communication.hpp`/`errorindicator.hpp`, status `firm (structural; 3 surface forms; abs-guard classified load-bearing defensive)`)
- book/src/SUMMARY.md (edited — in-place de-stub of the existing `:83` row: `- [nrm2-mutation-rotation (stub)](./L1-L0/nrm2-mutation-rotation.md)` → `- [nrm2-mutation-rotation](./L1-L0/nrm2-mutation-rotation.md)`; NOT an append — a second link would be a duplicate-link build error)
- scaffolding/open-questions.md (appended — new "### nrm2-mutation-rotation lowering family" group under §Open — deferred / contingent, opened_at: cycle-019 / opened_by: abstractor, 4 OQs: 2 resolution-markers + 2 forward-looking caveats)

Gate hits:
- retroactive-budget: 0 (stub→firm promotion authoring fresh firm surface; not a retroactive backfill)
- SUMMARY chapter registration auto-fix: 0 (chapter already registered at `:83` — this de-stubs the existing line in place per the repairer's rewritten block; no new file to register, no naive-append collision)
- index-placeholder displacement: 0 (the L1-L0 Theme-list table is a live list, no placeholder text)
- implied-component stub materialization: 0 (forward-refs `dot-mutation-rotation` (stub, file exists), `matrix-weighted-norm`, `L1/dot`, `concepts/nrm2`, `L0/transparent-vs-load-bearing-tricks` ALL resolve to existing on-disk homes per the critic's cross-reference-integrity verification — no dangling plain-text forward-reference to a missing clearly-implied component, so no stub to materialize)
- forward-edge / edge-label / variant-axis / H1-reuse / append-on-missing-slug: 0 (L1>L0 edge has live firm `L1/nrm2.md` surface; critic passed edge-label-fidelity + variant-axis-coverage; H1 `# nrm2-mutation-rotation` is the canonical slug heading, not a page-heading reuse; all three targets existed, index insert anchored between orthogonalize + minres rows matched verbatim)
- variant-axis missing on multi-variant operator: 0 (element-type real/complex axis collapses to one L1 operator, documented + critic-passed)

Open questions promoted:
- nrm2-std-abs-defensive-guard-classification (recorded RESOLVED-by-this-theme: load-bearing defensive guard; meta-phase closes on the migrated-to-plan `blas1-l1-l0-lowering-theme-gap` constituent per write-authority partition)
- nrm2-lowering-theme-deliverables (recorded ADDRESSED-by-this-theme; meta-phase closes on the same migrated-to-plan constituent)
- nrm2-mutation-rotation-dot-stub-collective-double-statement-recheck (deferred / contingent — lifter trigger when dot-mutation-rotation firms)
- nrm2-mutation-rotation-verified-against-audit (deferred / contingent — lowering-verifier trigger; surface-form exhaustiveness audit + verified_against: block)

Build-relevant: yes

Notes:
- Report went through significant repair (critic found 2 FAILs: citation-validity 258→259 off-by-one wrongly framed as a "correction", and cross-reference-integrity 2 stale carry-forwards; both repaired → ready). Applied the repaired CYCLE.md content as-is: the `259` citation, the corrected "inside the L1 entry's already-correct 255-260 range" framing, the same-sign-strip complex-path mechanism (`std::abs(std::complex{re,0.0}) = |re|` via the `this==&y` self-aliasing fast path at vector.cpp:264-267), and the de-stubbed concept-page / L0-tricks-page notes all transcribed verbatim from the repaired body.
- The repairer DROPPED the stale `concepts/nrm2.md` BLAS-scaled-summation carry-forward (the targeted defect no longer exists — concepts/nrm2.md:9 already states the opposite) and the stale L0-tricks "no defensive-guards treatment" carry-forward (tricks.md:22 already has the worked example). Per the META.md integrator note I did NOT migrate either as actionable work; they are omitted from the promoted OQ set entirely (no redundant downstream planner work).
- SUMMARY edit verified as in-place de-stub: re-read `:83` on disk before editing = `- [nrm2-mutation-rotation (stub)](./L1-L0/nrm2-mutation-rotation.md)` (matched the repairer's `replace … with …` old-string verbatim). dot-mutation-rotation:82 + scal:84 + matrix-weighted-norm:85 remain `(stub)` rows untouched.
- All anchors re-read on disk before each Edit: nrm2-mutation-rotation.md (status:stub blockquote at :3 confirmed present, full placeholder body replaced), L1-L0/index.md (orthogonalize row :26 + minres row :27 matched verbatim for the between-insert).
- deferred integrated_at to finalize per role-spec.

Third per-report integrator in cycle-019 (after fespace-l0, assemble-diagonal-l1).

---

## 2026-05-29T023000Z-harvester-orthogonalize-l2
applied_at: 2026-05-29T05:35:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/orthogonalize.md (full-rewrite — stub → firm; dropped the `status: stub` blockquote + "What this will be"/"Implied by"/"Refinement pending" placeholder body; wrote the firm L2 first-class-composition intro body — the named `project ▷ subtract` Gram-Schmidt composition lifting the firm L1 leaf, with the `gs_orthog ∈ {MGS,CGS,CGS2}` variant axis surfaced as the visible per-variant batching/sequencing and the collective-shape residual axis `m×1 / 1×m / 2×m` named as the load-bearing L2 content)
- book/src/L2/index.md (edited — ADD: inserted the firm `orthogonalize` dep-map row into the `## Operator dep-map` table, immediately after the `inner_product` rough-in row at `:26`; signature `(op: OrthogOp, w: Tensor[N], V: Basis[N, m]) → { residual: Tensor[N], coeffs: Tensor[m] }`, deps = L1 leaf `orthogonalize` (firm) + `dot`/`axpy` stage primitives + concepts + `krylov-step`/ROM consumers + `inner_product` sibling-fold-constituent, status `firm` cycle-019)
- book/src/SUMMARY.md (edited — in-place de-stub of the existing `:41` row: `- [orthogonalize (stub)](./L2/orthogonalize.md)` → `- [orthogonalize](./L2/orthogonalize.md)`; NOT an append — a second link would be a duplicate-link build error)
- scaffolding/open-questions.md (appended — new "### orthogonalize L2 composition family" group under §Open — deferred / contingent, opened_at: cycle-019 / opened_by: harvester, 4 OQs)

Gate hits:
- retroactive-budget: 0 (stub→firm promotion authoring fresh firm surface; not a retroactive backfill)
- SUMMARY chapter registration auto-fix: 0 (chapter already registered at `:41` — this de-stubs the existing line in place; no new file to register, no naive-append collision)
- index-placeholder displacement: 0 (the L2 `## Operator dep-map` is a live table, no `(empty — Phase B skeleton.)` placeholder text)
- implied-component stub materialization: 0 (per dispatch instruction — the forward-ref to the not-yet-authored `L2-L1/orthogonalize-composition-lowering` theme stays PLAIN-TEXT; singleton reference, NOT clearly-implied by ≥2 converging refs, so the stub bar is not met — left as plain-text + OQ `orthogonalize-composition-lowering-l2-l1-theme` per the speculative-fallback rule)
- forward-edge / edge-label / variant-axis / H1-reuse / append-on-missing-slug: 0 (L2 first-class composition entry; no L_{n+1}→L_n edge proposed — the L2>L1 lowering is deferred/forthcoming; the `project`/`subtract` stages reference LIVE firm `L1/dot.md` + `L1/axpy.md` surfaces; critic passed edge-label-fidelity + variant-axis-coverage [gs_orthog residual-axis + dot-hook parametric, element-type absorbed, Householder scoped out]; H1 `# orthogonalize` is the canonical slug heading, not a page-heading reuse; all three targets existed on disk, dep-map ADD anchored after the `inner_product` row matched verbatim)
- variant-axis missing on multi-variant operator: 0 (two axes closed + element-type absorbed; critic-passed)

Open questions promoted:
- orthogonalize-composition-lowering-l2-l1-theme (Backlog migration — abstractor L2>L1 theme; now-firm L2 anchor ready)
- orthogonalize-l2-record-vs-l1-tuple-naming ({ residual, coeffs } record vs L1 leaf's (w', H) tuple; cross-cutter trigger)
- orthogonalize-inner-product-constituent-tightening (deferred / contingent — fires when `inner_product` firms; constituent-not-parent)
- L2-layer-intro-refresh-for-named-compositions (layer-intro-author refresh flag — `L2/index.md:41` Working-Notes prose now stale)

Build-relevant: yes

Notes:
- Applied the repaired CYCLE.md content as-is. CRITICAL per the repairer's explicit integrator note: I did NOT renumber ANY citations. The critic raised 3 `citation-validity: warning` spot-line nits (orthogonality assertion 158→156, `m==0` guard `orthog.hpp:62-64`→61, no-normalise sentence `:22`→21) and the repairer independently re-verified via `read_range`/`search_text` against `reference/palace` and found the report's ORIGINAL pointers correct (the critic read against a 1–2-line-shifted offset). All three citations stand AS-IS in the firm body / dep-map.
- The repairer's one applied fix was STRUCTURAL only: it closed the missing `\`\`\`` fence on the first proposed-changes block so the edit-fence parser captures exactly the intended firm body (the "# orthogonalize" intro paragraph ending "…basis-extension all consume."), terminating before "## Context". I wrote exactly that body; the report's Context/Signature/Semantics/Laws/Variant-axes/Evidence sections are the report's own structured documentation of the harvest, NOT the chapter body, per the closed-fence boundary.
- The report also flagged the cycle-018 `linear_combination` firm-L2-composition precedent and the `krylov-step` §"L2 vs L1 distinction" forecast as the structural template; this is the forecasted entry. Critic verified the forecast quote is verbatim (krylov-step.md:132) and all `[link]` targets resolve.
- All anchors re-read on disk before each Edit: L2/orthogonalize.md (status:stub blockquote at :3 confirmed present, full placeholder body replaced), L2/index.md (the `inner_product` rough-in row at :26 matched verbatim for the after-insert; row added BELOW it — the inner_product row is still rough-in at this point per the staging-log note, flips to firm by a later integration, which does not affect this anchor), SUMMARY.md (`- [orthogonalize (stub)]…` at :41 matched verbatim).
- Drive-by skill-friction NOT in my authority: the critic/repairer flagged `classify-variant-axis` SKILL.md:64-68 `gs_orthog` worked example as stale vs L0 (lists `gemv_basis` / `axpy_scalar` / a `refine_threshold` scalar the actual `OrthogonalizeColumnCGS` does not have). Filed by the repairer to `scaffolding/skill-candidates.md` for meta-phase. Not an OQ I promoted (skill-correction is meta-phase authority); flagging here so integrator-finalize/meta-phase see it.
- The repairer's META also recorded a possible critic-side line-offset-drift signal (3-of-3 spot pointers shifted in the same direction) worth a meta-phase friction-window glance if it recurs. Surfaced for finalize/meta-phase, not actioned here.
- deferred integrated_at to finalize per role-spec.

Fourth per-report integrator in cycle-019 (after fespace-l0, assemble-diagonal-l1, nrm2-l1-l0).

---

## 2026-05-29T023000Z-cross-layer-cross-cutter-divfree-doc
applied_at: 2026-05-29T06:05:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1-L0/divfree-projector-mutation-rotation.md (edited — OPTIONAL cross-link sharpening of the §"Open questions / caveats" first bullet ("Stale `Mult` doc comment", :460-468): replaced the stale-comment note with the repaired NEW text that (i) cites the per-method comment as `:64-66`, (ii) names the inversion explicitly via the Helmholtz/Hodge `y = y_divfree + Grad·ψ` framing, (iii) names the **class** doc `:28-31` as the authoritative L0 site + the implementation `:155-190`, (iv) folds in the third L0 witness `divfree.cpp:176` inline comment, (v) records the closure cycle. Zero semantics change — divergence-free claim and all step citations unchanged)
- scaffolding/open-questions.md (appended — new "### divfree Mult doc-comment fidelity" group under §Open — deferred / contingent, opened_at: cycle-019 / opened_by: cross-layer-cross-cutter; the `divfree-mult-doc-irrotational-vs-divfree-stale` OQ recorded RESOLVED-by-this-report / closure-ready with full disposition text + the meta-phase-close trigger)

Gate hits:
- retroactive-budget: 0 (single optional prose-sharpening edit to one firm-entry bullet; not a backfill, not a per-slice/global accumulation)
- forward-edge / edge-label / variant-axis / H1-reuse / append-on-missing-slug: 0 (n/a — observation/resolution report; the edit replaces prose inside an existing §Open-questions bullet, no new live `[link]` introduced — citations stay plain-text `file:line` form per cross-reference-integrity; no edge/variant/heading claims; critic passed 7/8 with only skill-uptake-survey at warning [telemetry])
- SUMMARY chapter registration auto-fix: 0 (no new file; both divfree firm slugs already registered at SUMMARY :66/:81 per critic)
- index-placeholder displacement: 0 (no index touched)
- implied-component stub materialization: 0 (no dangling forward-reference; the report references only existing firm entries + L0 source sites)
- concept_writes-on-existing-slug / prose-mismatch: 0

Open questions promoted:
- divfree-mult-doc-irrotational-vs-divfree-stale (recorded RESOLVED-by-this-report / closure-ready; meta-phase unify-pass to close + migrate to the Closed index and flip priorities.md:27 to resolved — per write-authority partition the OQ close + plan-item flip are meta-phase authority, I only append the disposition)

Build-relevant: yes

Notes:
- OLD block matched `book/src/L1-L0/divfree-projector-mutation-rotation.md:460-468` byte-for-byte on a fresh disk re-read (no cycle-019 line drift — no prior cycle-019 report touched this file, confirmed against the 4 prior staging rows). Applied the repaired NEW text verbatim from the report's proposed-changes block (the repairer's additive `divfree.cpp:176` third-witness fold is present in the NEW text only; OLD untouched).
- The actual OQ-ledger CLOSE of `divfree-mult-doc-irrotational-vs-divfree-stale` and the `priorities.md:27` plan-item flip are **meta-phase unify-pass authority** — I appended the closure-ready disposition to open-questions.md (intake) so the next meta-phase enacts it. The slug was NOT previously present in open-questions.md (tracked only via priorities.md + cycle-019-resume-notes.md); this append gives it a ledger home with the RESOLVED disposition.
- Critic-flagged INFO items surfaced for finalize/meta-phase (not actioned, not my authority): (i) minor cross-entry citation-range divergence `:63-66` (L1-L0 theme) vs `:64-66` (L1 entry) for the same stale-comment site — both defensible, deferred to a future divfree-cohort normalization pass, no new OQ; (ii) skill-uptake-survey warning (the `verify-citation-range` skill was effectively used firsthand but not named in the report prose) — pure telemetry, non-blocking.
- deferred integrated_at to finalize per role-spec.

Fifth per-report integrator in cycle-019 (after fespace-l0, assemble-diagonal-l1, nrm2-l1-l0, orthogonalize-l2).

---

## 2026-05-29T023000Z-combinator-miner-parametric-family
applied_at: 2026-05-29T06:35:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- scaffolding/open-questions.md (appended — TWO new groups under §Open — deferred / contingent: (1) "### combinator-miner parametric-family mode — first live exercise" with 3 harvester-input OQs + a 4th conjugation-pinning pointer-to-existing-plan-item; (2) "### Routes to meta-phase — combinator-miner parametric-family mode-gap" with the Qualification-B mode-gap finding + the `variant-absorption-vs-instance-counting-policy` confirmation, both flagged for the next meta-phase. opened_at: cycle-019 / opened_by: combinator-miner)

NO book/ files touched — this is a PROPOSAL / mode-validation report. It emitted NO `edit:book/...` block (correctly, per the dispatch-phase write-guard; the `inner_product` L2 rough-in row already stands from cycle-018). Nothing to apply to the artifact. Confirmed `## Proposed changes` carries no book edit-block (CYCLE.md:70-74 explicitly states "No `edit:book/...` block is emitted").

Gate hits:
- retroactive-budget / forward-edge / edge-label / variant-axis / H1-reuse / append-on-missing-slug / concept_writes / index-placeholder displacement / implied-component stub materialization / SUMMARY chapter registration auto-fix: 0 (ALL no-op — no book mutation. No proposed-changes block to parse for gates; the only actionable persistence is the OQ-ledger append, which is not gate-governed.)

Open questions promoted:
- inner-product-fold-family-mode-characterization (harvester-input — feeds the in-flight cycle-019 `inner_product` L2 harvester, integration #7 next: fold-law membership test + 4 parameter axes + 3 over-unification guards + post-repair `yᴴ A x` weighted-member L0 form matching the stub)
- inner-product-tdot-uncalled-evidentiary-weight (harvester-input — `tdot` 0 call sites; firm-vs-rough-in citation tier question for the harvester)
- inner-product-weighted-split-additivity-whole-vector-only (harvester-input — state the split-additivity law at whole-vector granularity for the weighted member)
- combinator-miner-nonfold-parametric-family-no-positive-channel (ROUTES TO NEXT META-PHASE — Qualification B, the load-bearing mode-validation finding: the smoother/constructed-operator-action cohort is parametric but NOT a fold, and the mode gives no positive channel for non-fold parametric families; feeds friction-ledger `combinator-miner-arity-blind-parametric-family-detection` resolution)
- variant-absorption-vs-instance-counting-policy confirmation (ROUTES TO NEXT META-PHASE — confirms the cycle-018 parametric-family mode DOES address the existing meta-agenda OQ; refinement: the mode's distinctive deliverable is characterizer [fold-law + axis taxonomy], not just surfacer; meta-phase closes the existing slug per write-authority partition)
- conjugation-pinning — NOT a new slug; the existing plan-active OQ `inner-product-harvester-formalization-and-conjugation-pinning` (plan Now #1/#2) owns it. This report raises it to hard-must-resolve-before-firm and supplies the resolved L0 reading; recorded as a pointer in the new group, no duplicate slug.

Build-relevant: no

Notes:
- Proposal/mode-validation report — the actionable outputs are entirely (a) harvester-input characterization for the in-flight `inner_product` harvester (the fold-law + axis taxonomy + the post-repair `yᴴ A x` weighted-member math), and (b) the methodology-agenda mode-gap finding for the next meta-phase. Both land as OQ-ledger appends (the role's only non-book write authority besides STAGING). finalize does NOT need a book rebuild on account of this report.
- The repairer fixed 3 mechanical findings in the report body pre-integration (wrong-operand conjugation `(Ax)ᴴ y` → correct `yᴴ A x`; kernel-difference wording `Im·Im` real-part sign + imaginary cross-terms; the `constructed-operator-gate` → `nested-constructed-operator-gate` slug). I transcribed the post-repair characterization (`yᴴ A x` weighted-member form, the corrected over-unification-guard slug `nested-constructed-operator-gate`) into the OQ append so the harvester inherits the corrected math, NOT the report's original erroneous `(Ax)ᴴ y`.
- OQ CLOSE / migration authority is meta-phase, not mine. I APPENDED the `variant-absorption-vs-instance-counting-policy` *confirmation* as intake under the new "Routes to meta-phase" group (did NOT edit the existing line ~95 entry — ledger is append-only between meta-phases per the maintenance protocol); the meta-phase enacts the close + the friction-ledger resolution + the `priorities.md` §Next-meta-phase-methodology-agenda mirror.
- No report-frontmatter touch — `integrated_at:` deferred to finalize per role-spec.

Sixth per-report integrator in cycle-019 (after fespace-l0, assemble-diagonal-l1, nrm2-l1-l0, orthogonalize-l2, divfree-doc).

---

## 2026-05-29T024500Z-harvester-inner-product-l2
applied_at: 2026-05-29T07:05:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/inner_product.md (full-rewrite — stub → firm; dropped the `status: stub` blockquote + "What this will be"/"Implied by"/"Refinement pending" placeholder body; wrote the firm L2 reduce-to-`Scalar` fold entry: `(x: Tensor[N], y: Tensor[N]) -> Scalar ≡ foldl (+) zero (zipWith kernel x y)` unifying the L1 leaves `dot` (Hermitian) / `tdot` (unconjugated) / `bilinear-form` (M-weighted member) along the conjugation-convention / element-type / weight-presence axes; conjugation PINNED arg-1 `xᴴ y` / `xᴴ M y` with the §"Conjugation convention (pinned)" reconciliation against Palace's arg-2-conjugated `yᴴ x` source; 7 algebraic laws incl. the defining split-additivity/length-concatenation-homomorphism + the IEEE reduction-tree load-bearing non-law; §"Sibling fold: linear_combination is not subsumed"; §"Consumer: nrm2 / matrix-weighted-norm = √∘inner_product"; member-level `tdot` type-API-only + empirical-match caveats; `Status: firm`)
- book/src/L2/index.md (edited — FLIP: the `inner_product` dep-map row rough-in → firm. Targeted the `inner_product` row specifically by slug text [the `orthogonalize` row added by integration #4 now sits at :27 immediately after it — NOT touched]; new row: signature with the arg-1-conjugated pinned convention note, deps `dot`/`tdot` (type-API-surface only — zero call sites)/`bilinear-form` + `apply_linop` + concepts + sibling-fold `linear_combination` (do NOT merge) + consumer `nrm2`/`matrix-weighted-norm`, status `firm` cycle-019 with conjugation-pinning provenance)
- book/src/SUMMARY.md (edited — in-place de-stub of the existing `:40` row: `- [inner_product (stub)](./L2/inner_product.md)` → `- [inner_product](./L2/inner_product.md)`; NOT an append — a second link would be a duplicate-link build error)
- scaffolding/open-questions.md (appended — new "### inner_product L2 fold family" group under §Open — deferred / contingent, opened_at: cycle-019 / opened_by: harvester, 7 OQs: 2 RESOLVED-by-this-entry markers [the headline plan item + the sibling-candidate], 1 forward L2>L1-theme pointer, 4 member/test/layer-intro caveats)

Gate hits:
- retroactive-budget: 0 (stub→firm promotion authoring fresh firm surface; not a retroactive backfill)
- forward-edge claim without surface: 0 (no L_{n+1}→L_n edge claimed — the L2>L1 lowering `inner-product-fold-specialization` is deferred to the NEXT report, integration #8, correctly forward-referenced plain-text; the dep-map flip is a same-layer row with live firm surface now present)
- edge-label / prose mismatch: 0 (the only structural row touched is `L2/index.md:26`; prose discusses exactly that rough-in→firm flip; critic passed edge-label-fidelity)
- variant-axis missing on multi-variant operator: 0 (three axes — conjugation [the unification axis] / element-type / weight-presence — classified + two correctly-scoped-out non-axes [diagonal `y=x` consumer entry point, reduction tree L0 detail]; critic passed variant-axis-coverage)
- H1 reuse / append-on-missing-slug: 0 (`# inner_product` is the canonical slug heading, not a page-heading reuse; all three targets existed on disk, dep-map row + SUMMARY line matched verbatim by slug)
- SUMMARY chapter registration auto-fix: 0 (chapter already registered at `:40` — this de-stubs the existing line in place; no new file to register, no naive-append collision)
- index-placeholder displacement: 0 (the L2 `## Operator dep-map` is a live table, no `(empty — Phase B skeleton.)` placeholder text)
- implied-component stub materialization: 0 (per dispatch instruction — the forward-ref to `inner-product-fold-specialization` (L2>L1) stays PLAIN-TEXT [the next report firms it; the stub file already exists]; `matrix-weighted-norm` is an L1 slug `book/src/L1/matrix-weighted-norm.md` referenced PLAIN-TEXT — a live link would need to target `../L1/...` and would be a layer-placement upgrade, NOT made this pass. Neither materialized — both correctly plain-text)
- concept_writes-on-existing-slug: 0 (no concept-page writes)

Open questions promoted:
- inner-product-harvester-formalization-and-conjugation-pinning (recorded RESOLVED-by-this-entry — the headline highest-fan-out plan Now #1/#2 item; conjugation pinned arg-1, reconciliation documented, Palace verified self-consistent; meta-phase closes + flips the plan item per write-authority partition)
- inner-product-fold-sibling-candidate (recorded RESOLVED-by-this-entry — the sibling-fold boundary is drawn two-sided, the fold is firm; meta-phase closes)
- inner-product-fold-specialization-l2-l1-theme (forward L2>L1 theme pointer — the NEXT integration #8 this cycle firms it; now-firm L2 anchor ready)
- inner-product-tdot-member-status-citation-tier (member-level type-API-only caveat; non-status-reducing; lowering-verifier/cross-cutter trigger)
- inner-product-weighted-split-additivity-whole-vector-only (whole-vector-granularity law confirmation; pairs with the wave-1 combinator-miner same-slug intake row — meta-phase may dedup)
- inner-product-empirical-match-complex-weighted-untested (complex/weighted members source-transcription-grounded, no dedicated value-test; chebyshev-iteration/linear_combination precedent)
- L2-layer-intro-refresh-for-fold-cohort (layer-intro-author refresh flag — L2 index overlay/Working-Notes now stale with two firm fold siblings; pairs with the wave-2 orthogonalize `L2-layer-intro-refresh-for-named-compositions` row, meta-phase may fold into one)

Build-relevant: yes

Notes:
- HEADLINE report of cycle-019. Applied the repaired CYCLE.md content as-is. The repairer's two citation-range fixes are already baked into the §"Operator content" body I transcribed: the SPD-realness anchor reads `operator.cpp:611-616` with the comment "For SPD B, xᴴ B x is real" attributed to `:611` and the assertion to `:615-616` (law 5, Status, Evidence), and the wide `operator.cpp:598-618` self-verify window is tightened to `598-617` at the Consumer / Evidence sites. I did NOT renumber any citation — the body carries the repaired pointers verbatim.
- CRITICAL anchor disambiguation (per dispatch + the integration-#4 staging note): the `orthogonalize` dep-map row added by integration #4 now sits at `L2/index.md:27`, immediately AFTER the `inner_product` row at `:26`. I matched the `inner_product` row by its full slug-text [old] string (the cycle-018 rough-in row with the "(stub — harvester to firm)" label + the "see caveat 7" shorthand) — the orthogonalize row was NOT touched. Re-read disk before the Edit; the `inner_product` rough-in row matched verbatim.
- The conjugation-pinning crux (arg-1 `xᴴ y` against Palace's arg-2 `yᴴ x`) PASSED critique as sound: internally consistent with both L1 leaves, value-level divergence explicitly recorded + forward-handed to the lowering (not silently absorbed), Palace verified self-consistent. No `unclear` mark; the entry is firm.
- Critic-flagged telemetry surfaced for finalize/meta-phase (not actioned — outside my authority): (i) skill-uptake-survey warning — the harvester performed `verify-citation-range` / `verify-rotation-citation` / `classify-variant-axis` / `find-tests-for-region` substance inline but named no skill invocation (pure meta-phase telemetry); (ii) the latent layer-placement note that any future live-link of `matrix-weighted-norm` must target `../L1/matrix-weighted-norm.md` (L1, not same-layer) — no defect now, plain-text is correct.
- All anchors re-read on disk before each Edit: L2/inner_product.md (status:stub blockquote at :3 confirmed present, full placeholder body replaced), L2/index.md (the `inner_product` rough-in row at :26 matched verbatim; orthogonalize row at :27 untouched), SUMMARY.md (`- [inner_product (stub)](./L2/inner_product.md)` at :40 matched verbatim).
- deferred integrated_at to finalize per role-spec.

Seventh per-report integrator in cycle-019 (after fespace-l0, assemble-diagonal-l1, nrm2-l1-l0, orthogonalize-l2, divfree-doc, combinator-miner-parametric-family). HEADLINE — the next report (inner-product-fold L2>L1 theme, integration #8) depends on this firm L2 anchor.

---

## 2026-05-29T024500Z-abstractor-inner-product-fold
applied_at: 2026-05-29T07:35:00Z
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2-L1/inner-product-fold-specialization.md (full-rewrite — stub → firm; dropped the `status: stub` blockquote + "What this will be"/"Implied by"/"Refinement pending" placeholder body; wrote the firm L2>L1 theme: L2 reduce-to-`Scalar` fold `inner_product` LHS, three-key dispatch (conjugation kernel / element-type / weight-presence) selecting the L1 leaves `dot` (Hermitian) / `tdot` (unconjugated) / `bilinear-form` (M-weighted member), the headline value-level conjugate-pair re-order §"The conjugate-pair re-order" — L1/L2 pin `xᴴ y` arg-1, Palace L0 computes `yᴴ x` arg-2, `xᴴ y = conj(yᴴ x)`, re-order invisible under real-projection [CG `iterative.cpp:395`, Poynting diagonal `boundarymodeoperator.cpp:85`] / observable for full-complex [non-Hermitian cross-coupling `boundarymodeoperator.cpp:90`] — the §"Summation-order recording" pinned-reduction-tree table (the load-bearing IEEE-non-law content the L2 entry deferred), `Status: firm` + `tdot` API-surface-only member caveat blockquote)
- book/src/L2-L1/index.md (edited — APPEND: inserted the firm `inner-product-fold-specialization` theme row into the `## Theme list` table, immediately after the `linear-combination-fold-specialization` row at `:14`; L2 anchor `L2/inner_product` (firm), L1 anchor `L1/dot` (firm; `dot`+`tdot`) + `L1/bilinear-form` (rough-in, M-weighted member), status `firm (algebraic; conjugation-convention / element-type / weight dispatch + value-level xᴴ y↔yᴴ x conjugate-pair re-order + pinned reduction tree)`)
- book/src/SUMMARY.md (edited — in-place de-stub of the existing `:49` row: `- [inner-product-fold-specialization (stub)](./L2-L1/inner-product-fold-specialization.md)` → `- [inner-product-fold-specialization](./L2-L1/inner-product-fold-specialization.md)`; NOT an append — a second link would be a duplicate-link build error)
- scaffolding/open-questions.md (appended — new "### inner-product-fold-specialization L2>L1 theme family" group under §Open — deferred / contingent, opened_at: cycle-019 / opened_by: abstractor, 5 OQs: 1 RESOLVED-by-this-theme forward-pointer close + 2 lowering-verifier/caller-classification follow-ups + 1 cross-reference to the existing apply-linop audit cohort + the `linear-combination-fold-specialization-theme-followups` resolvable-on-the-linear_combination-side disposition)

Gate hits:
- retroactive-budget: 0 (stub→firm promotion authoring fresh firm surface; not a retroactive backfill)
- forward-edge claim without surface: 0 (the L2>L1 edge has a LIVE FIRM L2 surface — `book/src/L2/inner_product.md` was flipped stub→firm by integration #7 this cycle (verified on disk: the `status: stub` blockquote is gone, the firm body is present); the L1 leaves `dot.md` (firm) + `bilinear-form.md` (rough-in) both exist on disk; the M-weighted-member dispatch arm rides the rough-in leaf with a member-level caveat, not a missing surface)
- edge-label / prose mismatch: 0 (the theme carries the L2>L1 edge label throughout; the dep-map row append target `L2-L1/index.md:14` (the `linear-combination-fold-specialization` row) matched verbatim; the new row's L2/L1 anchor + status columns match the table schema `:11-14`; critic passed edge-label-fidelity)
- variant-axis missing on multi-variant operator: 0 (three orthogonal dispatch keys — conjugation / element-type / weight-presence — each mapped to its L1 leaf + L0 site; critic passed variant-axis-coverage; the two member caveats (`tdot` API-surface-only, `bilinear-form` rough-in) are correctly scoped member-level, NOT theme-status reductions per the dispatch instruction)
- H1 reuse / append-on-missing-slug: 0 (`# inner-product-fold-specialization` is the canonical slug heading, not a page-heading reuse; all three targets existed on disk, dep-map row anchored after the linear-combination row + SUMMARY line matched verbatim by slug)
- SUMMARY chapter registration auto-fix: 0 (chapter already registered at `:49` — this de-stubs the existing line in place; no new file to register, no naive-append collision)
- index-placeholder displacement: 0 (the L2-L1 `## Theme list` is a live table, no `(empty — Phase B skeleton.)` placeholder text)
- implied-component stub materialization: 0 (no dangling forward-reference to a missing clearly-implied component — every `[link]` target resolves on disk: `../L2/inner_product.md` (firm post-#7), `../L1/dot.md` (firm), `../L1/bilinear-form.md` (rough-in), `../L0/mutable-workspace-pattern.md`, `./linear-combination-fold-specialization.md`, `./chebyshev-iteration-fusion.md` — all verified present this pass)
- concept_writes-on-existing-slug: 0 (no concept-page writes)

Open questions promoted:
- inner-product-fold-specialization-l2-l1-theme (recorded RESOLVED-by-this-theme — closes the forward pointer the #7 harvester opened at OQ-ledger line 141; meta-phase closes + dedups against that line)
- inner-product-fold-specialization-lowering-verifier-audit (standard lowering-verifier follow-up — per-line dispatch-rule + re-order-rule + summation-order-table audit; non-status-reducing)
- inner-product-conjugate-pair-reorder-caller-classification (caller audit classifying every `linalg::Dot` site real-projected-invisible vs full-complex-observable; small, not blocking; bit-determinism half covered by existing `dot-reduction-tree-determinism-survey`)
- inner-product-weighted-member-two-stage-reduction-tree (cross-reference to the existing `apply-linop-lowering-verifier-audit-cohort` per the abstractor note — recorded as cross-ref, not a duplicate tracker)
- linear-combination-fold-specialization-theme-followups (abstractor disposition: RESOLVABLE on the linear_combination side — its 3 follow-ups are caveats already in that theme, none consumed by the inner-product theme; meta-phase to assess close/migrate on the sibling side)

Build-relevant: yes

Notes:
- LAST report of cycle-019 (integration #8). Applied the repaired CYCLE.md content verbatim. The repairer's two fixes were both honored AS-AUTHORED: (1) the cross-reference-integrity warning — I confirmed `book/src/L2/inner_product.md` is FIRM on disk (the stub blockquote is gone post-#7, the firm body present), so the §Verified-against L2-anchor bullet's repaired "the link target already exists on disk as a `stub` today, resolves at build now; dispatch #1 flips it stub→firm" wording is build-accurate (and the now-firm content is live, exactly as the wave-2 serial sequencing intended); (2) the softened forward-attributions ("per the cycle-019 `inner_product` harvester, dispatch #1 … live once dispatch #1 integrates") are transcribed verbatim — I did NOT re-tighten them to direct live-artifact claims even though dispatch #1 IS now integrated, since the report body is append-only-after-integration and the wording is correct as-is.
- I did NOT renumber ANY citation — the firm body carries the report's verified pointers verbatim (the 11 L0 ranges the critic independently re-verified via `palace-codemap`: `vector.cpp:263-274,664-685`, `operator.cpp:598-618,621-638`, `vector.hpp:240-262`, `operator.hpp:386,391`, `iterative.cpp:395`, `boundarymodeoperator.cpp:85,90`, `nleps.cpp:487,492`, `search_text TransposeDot`→2 hits).
- Anchor disambiguation: the `L2-L1/index.md` theme-list table has the `linear-combination-fold-specialization` row at `:14` as the last firm row before the `## Working Notes` section; I matched it by its full row text and appended BELOW it (the new inner-product row becomes `:15`). Re-read disk before the Edit; matched verbatim.
- The two member caveats (`tdot` type-API-surface-only — zero call sites, critic-confirmed; `bilinear-form` rough-in L1 with its M-weighted-member arm structurally firm) are carried IN the theme body (§"Speculative L1 operators" + the Status blockquote) as member-level evidentiary notes, NOT blockers and NOT theme-status reductions — exactly as the dispatch flagged.
- Critic telemetry surfaced for finalize/meta-phase (not actioned — outside my authority): skill-uptake-survey warning (the abstractor performed `verify-citation-range` / rotation-citation / variant-axis substance inline but named only `verify-citation-range` + the MCP path — pure naming-hygiene telemetry, the verification was evidently done per the critic's 11/11 range re-verification).
- deferred integrated_at to finalize per role-spec.

Eighth (and LAST) per-report integrator in cycle-019 (after fespace-l0, assemble-diagonal-l1, nrm2-l1-l0, orthogonalize-l2, divfree-doc, combinator-miner-parametric-family, inner-product-l2). Depended on integration #7's firm `book/src/L2/inner_product.md` L2 anchor (confirmed firm on disk). The L2 reduce-to-`Scalar` fold cohort now has BOTH its operator (L2) and its lowering theme (L2>L1) firm; the L2-L1 Part has 3 firm themes. integrator-finalize: cycle-019 staging log COMPLETE (8/8 rows) — proceed to rebuild + commit.

---
