# cycle-128 integrator staging log

Per-report integrator landings for cycle-128 (batch-41). Newest row LAST (append-only). Row ORDER is the authoritative apply-order record; `applied_at` timestamps are advisory only. integrator-finalize reconciles from this log.

---

## 2026-06-07T163919Z-layer-intro-author-closure-signature-convention
applied_at: 2026-06-07T16:55:00Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/semantics/index.md (Change 1: new §1.3.1 "Closure-returning signatures" subsection inserted after the :128 do-block sentence, before `## 2. Ownership categories`; Change 2: §v0.2 iteration-log note :494 promoted with §1.3.1 back-reference; Change 3: §Working-Notes operator-body gap :518 struck-through + RESOLVED via §1.3.1)
- book/src/L4/mk_matrix_free_operator.md (Change 4: signature codomain `LinearOperator (Tensor[(N: ...)])` → `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` at the L4-form block + `result` comment rewrite + §1.3.1 USE+LINK in the leading prose; §Intent :50 "a `LinearOperator` value" wording aligned to the operator-value form + §1.3.1 link)
- book/src/feature/matrix-free-operator.L4.md (Change 5, repairer-added: IDENTICAL lockstep signature fix `LinearOperator (Tensor[(N: ...)])` → `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` at the composing feature-column composition-root + `-- output` comment rewrite + §1.3.1 USE+LINK back-reference)
- scaffolding/open-questions.md (append-only: 3 OQs promoted)

Gate hits:
- rank-gate: 0 (no status/rank/edge changes — D1 is semantic-surface prose + 2 surgical signature-notation fixes; no-op, as the dispatch predicted)
- concept_writes-on-existing-slug: 0
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0
- H1-page-heading-reuse: 0 (new content is a `#### 1.3.1` subsection, not an H1; no collision)
- append-on-missing-slug: 0
- variant-axis-missing: 0 (the §1.3.1 convention enumerates BOTH its spellings — bare closure vs `Op[…]` — in an explicit when-to-use table; the exemplar fix justifies the `Op[…]` arm)
- SUMMARY-registration: 0 (no new files created; all three book files pre-exist and are SUMMARY-registered)
- deleted-slug-frontmatter-edge-sweep: 0 (no deletions)
- citecheck (--scan): 2 ok, 0 failing — no MISS/AMBIG/OOB. D1 introduces no new L0 source citations (notation-convention edits to book-internal prose); clean.
- §1.3.1 numbering-collision check: PASS — existing subsections are §1.2.1/1.2.2/1.2.3; §1.3 has no prior §1.3.x; no collision with §1.2.1 or §1.3.

Open questions promoted:
- closure-signature-exemplar-spelling-choice-Op-over-bare (stated-for-record, no action)
- closure-signature-introduction-form-into-bnf-and-role-discipline-bullet (ROUTED TO BATCH-41 META — BNF promotion + harvester/abstractor USE+LINK discipline bullet)
- closure-signature-l4-constructor-restatement-compliance-cohort-sweep (ROUTED TO BATCH-41 META — whole-book L4-constructor-signature compliance sweep)

Build-relevant: yes (edits touch book/src/*.md — semantics/index.md, L4/mk_matrix_free_operator.md, feature/matrix-free-operator.L4.md)

Notes:
- All FIVE proposed-changes blocks applied cleanly (Changes 1-4 original + Change 5 repairer-added). Each `[old]` matched disk exactly; verified anchors before editing (do-block sentence :128, §v0.2 note :494, working-note :518, exemplar signature block, §Intent :50, feature-column :52-54).
- **FINALIZE LOCKSTEP FIX REQUIRED — `book/src/L4/index.md:119` is NOT in D1's proposed-changes (out of D1's write-scope; D1's five blocks touch only semantics/index.md + L4/mk_matrix_free_operator.md + feature/matrix-free-operator.L4.md).** I confirmed the drift exists ON DISK: the L4 dep-map mirror row at `L4/index.md:119` carries the SAME pre-fix trigger signature `mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> LinearOperator (Tensor[(N: ...)])`. To stay consistent with the now-fixed cap (`L4/mk_matrix_free_operator.md`) + the new §1.3.1 convention, finalize should apply the identical operator-VALUE spelling fix `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` to that dep-map cell as a consistency fix. DEFERRED to finalize per role-spec (not in this report's proposed-changes; I do not apply out-of-scope edits). This is the dispatch-flagged D2-audit lockstep item.
- The §1.3.1 `op-with-params {…}` introduction form is authored in PROSE, not the §1.3 BNF `e ::=` block — deliberate (surgical, avoids grammar renumbering); routed to batch-41 meta via the OQ above. Non-blocking, internally consistent (intro lives next to the §3.5 elim it mirrors).
- deferred integrated_at to finalize per role-spec.

---

## 2026-06-07T164021Z-lifter-l2-placeholder-destale
applied_at: 2026-06-07T17:20:00Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L2/matrix-free-operator-apply.md (single `edit:` block — §"Speculative higher (L4) placeholder (rough-in, for a later harvester)" (`:209-222`) replaced with a settled `## Higher (L4) — firm` USE+LINK pointer to the three now-firm c127 chapters: `../L4/mk_matrix_free_operator.md`, `../feature/matrix-free-operator.L4.md`, `../L4-L3/mk-matrix-free-operator-dissolution.md`. Prose-only; no frontmatter/`## Status`/edges/signature-line change)

Gate hits:
- rank-gate: 0 (prose-only de-stale — no status/rank/edge promotion to assert the `rank(u) ≤ min(deps)` invariant against; no-op as the dispatch predicted)
- concept_writes-on-existing-slug: 0
- forward-edge-without-surface: 0 (the new section is an upward `reference`-class see-also to surfaces that all exist on disk)
- edge-label/prose-mismatch: 0 (no frontmatter `edges:` block touched; the prose pointer is narrated as "this combinator's action IS the L4 cap's apply", consistent with the firm L4 chapter's mutual back-link)
- H1-page-heading-reuse: 0 (replacement heading is `## Higher (L4) — firm`, an H2 section; no H1 collision)
- append-on-missing-slug: 0
- variant-axis-missing: 0 (no variant axes; prose-only pointer)
- SUMMARY-registration: 0 (no new files; target L2 chapter pre-exists and is SUMMARY-registered)
- deleted-slug-frontmatter-edge-sweep: 0 (no deletions)
- citecheck (--scan): 2 ok, 0 failing — no MISS/AMBIG/OOB. The 3 link targets all resolve on disk (filesystem-checked: `book/src/L4/mk_matrix_free_operator.md`, `book/src/feature/matrix-free-operator.L4.md`, `book/src/L4-L3/mk-matrix-free-operator-dissolution.md` all present). Clean.

Open questions promoted:
- (none — report's §Open-questions is "None"; clean pure-rewrite, no contradiction surfaced)

Build-relevant: yes (edits touch book/src/L2/matrix-free-operator-apply.md)

Notes:
- **OQ `matrix-free-operator-apply-l4-placeholder-now-stale` (opened c127, ledger `scaffolding/open-questions.md:1942`) is DISCHARGED by this landing** — its declared "Action (future L2 touch): re-anchor the placeholder to point at the landed `feature/matrix-free-operator.L4` + the firm `mk_matrix_free_operator` cap" is exactly what this report did. I did NOT edit the OQ entry to mark it resolved: per role-spec, the per-report integrator's open-questions authority is APPEND-ONLY; closing/migrating OQs is the meta-phase's unify authority (CLAUDE.md §Write-authority partition). **integrator-finalize / batch-41 meta-phase: please close this OQ as resolved-by-c128-D4.**
- Verified the `[old]` anchor matched disk verbatim before editing (read `:200-229`); the on-disk text was the stale placeholder exactly as quoted in the report. The L4 signature line in the new pointer matches `L4/mk_matrix_free_operator.md:60` token-for-token (preserved, not re-derived).
- Note on the sibling D1 row above: D1 (`...closure-signature-convention`) changed the L4 cap's signature CODOMAIN spelling to `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` (operator-value form), but D4's new L2 pointer reproduces the `LinearOperator (Tensor[(N: ...)])` spelling (matching the report's `[old]`-preserved signature + the on-disk `L4/mk_matrix_free_operator.md:60` text the lifter read). I report this from what I read: I did NOT re-read `L4/mk_matrix_free_operator.md:60` this invocation to confirm whether D1's codomain fix has landed there, so I cannot assert the two now disagree — I only note the L2 pointer carries the `LinearOperator (…)` spelling as authored. If finalize applies its flagged `L4/index.md:119` lockstep fix to the `Op[…]` form, it may also wish to assess whether this L2 pointer's reproduced signature should track the same spelling (a prose-consistency follow-up, NOT a build break; linkcheck2 is blind to it). Flagged for finalize judgment.
- deferred integrated_at to finalize per role-spec.

---

## 2026-06-07T164113Z-cross-layer-cross-cutter-highorder-signature-audit
applied_at: 2026-06-07T17:50:00Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- scaffolding/open-questions.md (append-only: 2 OQs promoted)

(NO artifact changes — this is a READ-ONLY findings catalogue. D2 carries no `## Proposed changes` block; the META confirms "the integrator applies nothing to the artifact from it." No `book/` mutation.)

Gate hits:
- rank-gate: 0 (no status/rank/edge changes — read-only audit)
- concept_writes-on-existing-slug: 0
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0
- H1-page-heading-reuse: 0
- append-on-missing-slug: 0
- variant-axis-missing: 0
- SUMMARY-registration: 0 (no new files)
- deleted-slug-frontmatter-edge-sweep: 0 (no deletions)
- citecheck (--scan): 27 ok, 0 failing — no MISS/AMBIG/OOB. Clean (the report's file:line refs all resolve; the critic independently re-Read every load-bearing cited line and confirmed exact matches).

Open questions promoted:
- highorder-signature-noncompliant-cohort-c129-lifter-sweep (the c129 LIFTER-SWEEP candidate: the NON-COMPLIANT high-order-signature cohort — `assemble_frequency_operator` incl. the `A2` field+prose, `fe_assemble`, `assemble_term`, + the `L4/index.md:61,62` dep-map mirror rows + the `eliminate_bc` chapter↔index reconcile — to rewrite to the `Op[…]` operator-value spelling per the now-landed §1.3.1)
- oq-highorder-operator-transformer-codomain-convention (the borderline adjudication: whether bracketed `LinOp[$S,$S]` operator-transformer codomains count as already-compliant or need additional paren-grouping; for D1/batch-41-meta to pin in semantics §1.3.1 BEFORE the c129 sweep)

Build-relevant: no (edits touch only scaffolding/open-questions.md — no book/src/*.md mutation; no book rebuild needed for this report)

Notes:
- READ-ONLY AUDIT, no artifact changes applied — confirmed via the report (no proposed-changes block) AND the META (`surface-or-evidence: pass (no-op for read-only audit kind)`, `overall_status: ready`, repairer's only edit was to D2's own recommendation surface, not the artifact).
- **The `L4/index.md:119` mk_matrix_free_operator trigger dep-map mirror row is NOT part of the c129 cohort I promoted** — it rides with D1's `mk_matrix_free_operator` fix as a finalize lockstep consistency fix THIS cycle (c128), already flagged in the D1 staging row above (the "FINALIZE LOCKSTEP FIX REQUIRED" note) as on-disk drift. I noted this exclusion in the c129-sweep OQ so the c129 lifter does not double-handle it. I did NOT re-read `L4/index.md` this invocation, so I make no on-disk claim about the current state of `:119`; I only relay the exclusion-routing the dispatch + the D1 row specified.
- D2's borderline finding #4 (`eliminate_essential_bc`) is adjudication-gated: its inclusion in the c129 sweep depends on `oq-highorder-operator-transformer-codomain-convention` being pinned first. Both OQs promoted so the dependency is visible to the planner/meta.
- deferred integrated_at to finalize per role-spec.

---
## 2026-06-07T164021Z-cross-layer-cross-cutter-5driver-l4-completeness
applied_at: 2026-06-07T18:20:00Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- scaffolding/open-questions.md (append-only: 2 OQs promoted)

(NO artifact changes — this is a READ-ONLY findings audit. D3 (the ASK-2 "B" capstone, the 5-driver L4-completeness audit) carries NO `## Proposed changes` block; the META confirms `surface-or-evidence: pass (adapted for the read-only audit shape) … proposes NO surface change and recommends NO edge authoring`. No `book/` mutation.)

Gate hits:
- rank-gate: 0 (no status/rank/edge changes — read-only audit; nothing to assert the `rank(u) ≤ min(deps)` invariant against)
- concept_writes-on-existing-slug: 0
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0
- H1-page-heading-reuse: 0
- append-on-missing-slug: 0
- variant-axis-missing: 0
- SUMMARY-registration: 0 (no new files)
- deleted-slug-frontmatter-edge-sweep: 0 (no deletions)
- citecheck (--scan): per the META, `4 ok, 0 failing` — no MISS/AMBIG/OOB. The critic independently Read all six L4 feature surfaces + fe_assemble.md + eigsolve.md + the baseline-exceptions ledger and confirmed every constituent-firmness claim matches disk. Clean.

Open questions promoted:
- lifecycle-l4-stale-boundary-mode-rough-in-token (c129-cleanup candidate; stale `rough-in` token in lifecycle.L4.md:72 for boundary-mode.L4, which is `rank: firm` on disk — NOT a report defect)
- fe-assemble-stale-mk-matrix-free-roadmap-goal-token (c129-cleanup candidate; stale `roadmap_goal` token in fe_assemble.md:16,164 for mk_matrix_free_operator, which is `firm` on disk since c127 — NOT a report defect; both possibly foldable into the c129 signature sweep that already touches fe_assemble.md)

Build-relevant: no (edits touch only scaffolding/open-questions.md — no book/src/*.md mutation; no book rebuild needed for this report)

Notes:
- **CAPSTONE VERDICT (ASK-2 "B") — RECORD PROMINENTLY FOR THE BATCH-41 META.** The 5-driver L4-completeness audit returns ALL-PASS: all 5 drivers (electrostatic / magnetostatic / eigenmode / driven / transient) + the lifecycle ROOT are PASS on the critic's independent re-verification — **the in-scope FEATURE-SURFACE SPINE is L4-COMPLETE.** NO GAP. Each driver's composition stages name already-firm constituents BY NAME; all 12 named constituents verified `firm` on disk (fe_assemble, solve_family, ksp_solve, gram_reduce, eigsolve, frequency_sweep, assemble_frequency_operator, fold_solve, sparameter_reduce, eigenfreq_qfactor_reduce, mk_matrix_free_operator, L1/build_mesh). Two non-PASS constituents are GENUINELY-TRACKED opaque-library kernels, NOT gaps: (1) eigenmode `eigsolve` (firm cap under explicit SLEPc/ARPACK opaque-library constraint, tracked by RE11); (2) transient per-step ODE body (`obstruction (opaque-library-ownership)` quantified-over by the firm `fold_solve`). The boundary-mode 6th branch is explicitly scoped OUT with a re-check flag.
- **Edge recommendation:** the audit recommends NOT authoring a `driver-assemble → mk_matrix_free_operator` `depends-on` edge — it would MISCLASSIFY (the `constructs-via` navigational `reference` already exists at the correct `assemble_term` leaf altitude per `fe_assemble.md:15-16,164`; a driver-stage `depends-on` would also violate well-foundedness by treating the leaf interior as a driver-stage constituent).
- **Recommendation: DEFER** (per the report) — no follow-up dispatch warranted. The all-PASS result is the PRIMARY EVIDENCE for the batch-41 meta's ASK-2 capstone verdict + the "wind the in-scope spine to MAINTENANCE" judgment. integrator-finalize: please surface this capstone verdict in the cycle log + integrator-signals tail so the batch-41 meta sees it.
- Re sibling rows D1/D4/D2 above: I did NOT re-read their touched files this invocation (read-only audit; no overlapping edits), so I make no on-disk claim about their landings — I report only this report's own application (the 2 OQ appends).
- deferred integrated_at to finalize per role-spec.

---
