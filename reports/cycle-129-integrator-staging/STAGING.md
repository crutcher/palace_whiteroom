# cycle-129 integrator staging log

Per-report integration staging for cycle-129 (batch-41 BATCH-CLOSING). Newest row LAST (append-only). Row ORDER is the authoritative apply-order record; `applied_at` is advisory.

---

## 2026-06-07T171604Z-layer-intro-author-transformer-codomain-adjudication
applied_at: 2026-06-07T18:55:00Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/semantics/index.md (edit — §1.3.1: appended the operator-transformer/-constructor ruling bullet after the reconciliation paragraph at :155; added a "Grouping" column + a third opaque-`LinearOperator[N,N]` row to the `Op[…]`-vs-bare-closure table at :150-154)

Gate hits:
- retroactive-budget (per-slice / global): 0
- concept_writes-on-existing-slug: 0
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0
- H1-reuses-page-heading: 0 (no new file/H1)
- append-on-missing-slug: 0
- variant-axis-missing: 0
- SUMMARY-registration auto-fix: 0 (no new chapter; existing file edited in place)
- alpha-position-insert: 0 (no SUMMARY/index-table row)
- index-placeholder-displacement: 0
- implied-component-stub: 0
- deleted-slug-frontmatter-edge-sweep: 0 (no deletions)
- rank-gate (depends-on rank invariant): n/a (no status/rank/edge change — semantic surface is the §0.1-governed active-management surface, not a rank'd DAG node)
- citecheck bounds + path-hygiene: 4 ok, 1 failing — the single failing is a MISS on `1.3.1:155`, which is the report's prose shorthand for "§1.3.1 line 155 of semantics/index.md" (a section/line reference, NOT a file citation). The 4 real file citations (semantics/index.md:155, :95, L4/eliminate_bc.md:83-84, the cycle-planner report) all resolve OK. False-positive on a section-ref token; NOT a real MISS/AMBIG/OOB → non-blocking, nothing deferred.

Open questions promoted:
- (none promoted to open-questions.md by this report)

Notes:
- Prose-only edit to the active-management semantic surface (`book/src/semantics/index.md` §1.3.1). EXTENDS the c128 §1.3.1 reconciliation clause + table — does NOT contradict or duplicate it (the c128 :155 sentence is preserved verbatim; the new bullet generalizes it to the operator-TRANSFORMER and operator-CONSTRUCTOR cases). Verified both `[old]` anchors matched on-disk before applying.
- Table verified well-formed post-edit: 4-col header (:150) + 4-dash separator (:151) + 3 data rows (:152-154) each with 4 cells; mdBook will render cleanly.
- OQ `oq-highorder-operator-transformer-codomain-convention` flagged RESOLVED by this pin (bracketed operator-value codomain = already compliant; opaque `LinearOperator[...]` type-application = the non-compliant smell, re-spell-not-wrap). Per the report + plan D1, the resolution-marker append authority is the **batch-41 meta's header-close unify-authority** — so this report did NOT edit `scaffolding/open-questions.md`, and neither did I. FLAGGING for the batch-41 meta to land the RESOLVED marker. The two META-owned follow-on OQs (`closure-signature-introduction-form-into-bnf-and-role-discipline-bullet`; `closure-signature-l4-constructor-restatement-compliance-cohort-sweep`) are deliberately untouched; this pin supplies the scope predicate (opaque `LinearOperator[...]` = in-scope; bracketed `Op[…]`/`LinOp[…]` = compliant) the cohort sweep will use.
- This is D1 (LEAD, WAVE-1). D2 (the WAVE-2 lifter sweep) depends on this ruling — it is NOT in this report; the report's "Consequence for D2" section narrows D2's sweep to the opaque-`LinearOperator[...]` sites (two chapter bodies + two narrative index rows) and declares `eliminate_bc.md:83-84` + the bracketed index TABLE rows out-of-cohort. That is D2's scope, not landed here.
- No status/rank/edge change; RE baseline holds unchanged.
- Deferred `integrated_at` to finalize per role-spec.

Build-relevant: yes

---

## 2026-06-07T171929Z-lifter-closure-signature-cohort-sweep
applied_at: 2026-06-07T19:20:00Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/assemble_frequency_operator.md (edit — 4 opaque high-order/closure codomains re-spelled `LinearOperator[N, N]` → `LinOp[(N: ...), $N]`: :99 sig two-line block, :106 A2 closure-returning record field, :127 shape-contract prose, :293 "Downward to L1" inline-backtick restated sig)
- book/src/L4/fe_assemble.md (edit — 3 opaque high-order codomains re-spelled → `LinOp[(N: ...), $N]`: :60 fe_assemble sig, :71 assemble_term §Signature leaf, :35 §Context point-2 leaf; + 2 stale-token corrections — the `constructs-via` edge inline-comment :16 and the prose paragraph :164, both `mk_matrix_free_operator` `roadmap_goal`→`firm (c127)`)
- book/src/L4/index.md (edit — 2 narrative rows: :61 eliminate_bc embedded `eliminate_essential_bc` sig opaque → bracketed `LinOp[(S: ...), $S] -> LinOp[$S, $S]` (reconcile to canonical chapter/TABLE form per D1); :62 fe_assemble embedded `assemble_term` leaf sig opaque → `LinOp[(N: ...), $N]`)
- book/src/feature/lifecycle.L4.md (edit — stale-token :72 dispatch-table cell `boundary-mode` `rough-in`→`firm`)

Gate hits:
- retroactive-budget (per-slice / global): 0
- concept_writes-on-existing-slug: 0
- forward-edge-without-surface: 0
- edge-label/prose-mismatch: 0
- H1-reuses-page-heading: 0 (no new file/H1)
- append-on-missing-slug: 0
- variant-axis-missing: 0
- SUMMARY-registration auto-fix: 0 (no new chapter; existing files edited in place)
- alpha-position-insert: 0 (no SUMMARY/index-table row)
- index-placeholder-displacement: 0
- implied-component-stub: 0
- deleted-slug-frontmatter-edge-sweep: 0 (no deletions)
- rank-gate (depends-on rank invariant): n/a (NO status/rank/edge change — pure prose/signature re-spell + 2 maturity-token corrections; the `constructs-via` edge stays `reference`-class `kind: constructs-via`, only its inline-comment stale wording corrected; no DAG-node rank move; linter baseline / RE set holds unchanged)
- citecheck bounds + path-hygiene: 11 ok, 3 failing — all 3 failing are `[AMBIG]` basename-collision nits on the report's PROSE-DISCUSSION references (`assemble_frequency_operator.md:103-105`, `fe_assemble.md:71`, `fe_assemble.md:77` — bare basenames colliding L4/ vs L1/), NOT edit-block paths and NOT bounds drift; the edit-blocks themselves all use full `book/src/L4/...` paths and applied unambiguously. No MISS/OOB; the AMBIG sit on out-of-scope discussion pointers that are unambiguous in context → non-blocking, nothing deferred. (Critic recorded the identical 3 AMBIG as info-level sub-warnings.)

Open questions promoted:
- (none promoted to open-questions.md by this report) — the report's single §Open-questions caveat (the deferred plain operator-VALUE `LinearOperator[N, N]` §1.2.2 flat-vector-rendering cohort) is explicitly the PRE-EXISTING META-owned OQ `closure-signature-l4-constructor-restatement-compliance-cohort-sweep`, not a new question this report opens. Flagging for the batch-41 meta below; did NOT re-append to the ledger.

Notes:
- This is D2 (WAVE-2, dep D1; D1's row is above). Pure-rewrite fidelity sweep + 2 evidenced maturity-token corrections, exactly as dispatched. Verified on-disk before applying that the :99 (two-line code block, lines 98-99) and :293 (inline-backtick with trailing comma) `[old]` strings are DISTINCT unique literal matches — they are; no mis-apply.
- All 7 opaque high-order/closure codomain sites re-spelled to `LinOp[(N: ...), $N]` (the §1.2.2 square-operator calculus rendering D1 sanctioned, chosen for consistency with the already-compliant TABLE rows for these same two chapters). The 2 narrative index rows moved (:61 eliminate_bc reconciles to the canonical bracketed chapter/TABLE form; :62 fe_assemble matches the now-swept chapter sig).
- 2 stale-token corrections applied, each evidenced on-disk THIS dispatch: `mk_matrix_free_operator.md:5-6` carries `status: firm`/`rank: firm` (c127) — the two `fe_assemble.md` prose tokens (:16 edge inline-comment, :164 paragraph) updated `roadmap_goal`→`firm`; `boundary-mode.L4.md:6` carries `rank: firm` — the `lifecycle.L4.md:72` dispatch-table cell updated `rough-in`→`firm`. (The report's verification-note pointers said `:4-5`/`:5`; actual frontmatter is at `:5-6`/`:6` — a benign ±1 prose-pointer drift in non-claim-backing notes; the underlying facts are correct, critic also noted this as info-level.)
- CONFIRMED untouched (read off disk this dispatch): `eliminate_bc.md:83-84` stays the bracketed compliant `LinOp[(S: ...), $S] -> ... -> LinOp[$S, $S]` (read-only consult); the `L4/index.md` bracketed TABLE rows `:110`/`:114`/`:115` (all `LinOp[(S: ...), $S]`) and `:119` (`mk_matrix_free_operator` `Op[Tensor[(N: ...)] → ...]`) are all unchanged.
- DELIBERATE within-chapter dual-spelling PRESERVED (NOT "fixed", per dispatch): the plain operator-VALUE record fields + result/prose lines stay rank-1 `LinearOperator[N, N]` (`assemble_frequency_operator.md:69,103-105,121,137-138,146,214-215,335`; `fe_assemble.md:64,77-78,84,92,102,118`). These are the §1.2.2 flat-vector-rendering cohort = the META-owned OQ above, NOT this §1.3.1 closure-signature sweep's scope. Verified narrative index rows :61/:62 carry 0 remaining `LinearOperator`.
- The `L4/index.md` TABLE cell :119 still narrates `mk_matrix_free_operator` as `roadmap_goal` — this is the dep-map TABLE cell, NOT in this report's stale-token cohort (the report scoped the `roadmap_goal`→`firm` correction to the two `fe_assemble.md` prose sentences only). Left untouched as out-of-cohort; flagging for the batch-41 meta in case it wants to fold the index TABLE-cell maturity-snapshot into a later sweep.
- No book rebuild / commit / housekeeping (finalize's job). Deferred `integrated_at` to finalize per role-spec.

Build-relevant: yes

---
