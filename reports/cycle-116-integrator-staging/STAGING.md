# cycle-116 integrator staging log

Per-report integration staging for cycle-116 (batch-37; semantic-consolidation campaign WAVE-1/2 — D1 then D2, serial). Newest row LAST, append-only. Row ORDER is the authoritative apply-order record; `applied_at` is advisory only. integrator-finalize reads this log to reconcile the cycle (rebuild + commit + housekeeping).

---

## 2026-06-06T201018Z-layer-intro-author-semantic-surface-move (D1)
applied_at: 2026-06-06T203904Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied (verify-not-redo — edits were applied directly in book/src by the dispatch; this row records VERIFICATION of the on-disk applied state)

Files touched (by the dispatch; VERIFIED on disk this invocation, not re-applied):
- book/src/semantics/index.md (created — the moved semantic surface; 39117 bytes; verbatim `git mv` of the former design/l4_calculus.md, 513 lines)
- book/src/design/l4_calculus.md (deleted — confirmed gone: `ls` → No such file)
- book/src/design/index.md (reframed — exists, 1304 bytes; the same-dir `(./l4_calculus.md)` link converted to relative `(../semantics/index.md)` pointer note)
- book/src/SUMMARY.md (Part link rewritten — line 51 new Part header `# Semantic surface — calculus, rules & abstractions`; line 52 `- [L4 calculus & spec semantics (active-management surface)](./semantics/index.md)`; placed AFTER the Feature Part, BEFORE `# L4` per the consolidation-directive ordering)
- ~97 book/src/*.md files (bulk `l4_calculus.md` → `index.md` cross-reference rewrite — both `]()` link targets and inline-code prose citations)

Verification performed (this invocation, off disk):
- `grep -rl 'design/l4_calculus' book/src` → 0 matches (hard gate HOLDS; exit 1 = no matches)
- `grep -rn 'l4_calculus\.md' book/src` → 0 (the bulk basename rewrite reached prose inline-code citations too)
- book/src/semantics/index.md exists (39117 bytes); book/src/design/l4_calculus.md gone; book/src/design/index.md reframed (1304 bytes)
- SUMMARY.md Part header + link present at lines 51-52, correctly positioned (Feature Part → Semantic surface → L4)
- META overall_status: ready (canonical); checks all pass except citation-validity: warning → repaired (caveat-text accuracy only; artifact correct). cross-reference-integrity + plan-kind-consistency PASS, both load-bearing for a move dispatch, independently re-verified by the critic.
- Did NOT run `cargo make book` (integrator-finalize runs it once at cycle-end); the dispatch + critic both reported EXIT 0 on it.

Gate hits:
- citecheck bounds scan (per-report subset, --scan --quiet on the report CYCLE.md): 2 ok, 5 failing (7 checked). All 5 failures (2× MISS `l4_calculus.md:NNN`, 3× AMBIG `index.md:NNN`) are inside the report's OWN `## Open questions / caveats` PROSE — they are the report ILLUSTRATING the exact residual it is flagging (the `l4_calculus.md`→`index.md` rewrite examples + the §3.7 `index.md:151-184` drift). They are NOT proposed-change citations that land into book content (this is a claim-free verified mechanical move). The MISS hits resolve to nothing because `l4_calculus.md` no longer exists (that IS the move); the AMBIG hits are the bare-`index.md` ambiguity the report is promoting as an OQ. Disposition: NOT a defect in landed content — these ARE the two OQs promoted below. NOT blocking, NOT deferred.
- All other per-report safety-net gates: N/A for a file-move dispatch (no concept_writes / forward-edge / variant-axis / rank-promotion / dep-map-row / SUMMARY-chapter-registration-without-proposal — the SUMMARY Part link was proposed AND applied by the dispatch; no alpha-position insert choice was mine; no placeholder displacement; no implied-stub materialization).
- Graded-stack rank gate: no rank promotions in this report (frontmatter untouched — reachability/rank-neutral). Nothing to assert.

Open questions promoted (to scaffolding/open-questions.md, append-only, opened_at: cycle-116):
- ambiguous-bare-index-md-prose-refs-after-semantic-surface-move (re-scoped caveat 1 — bare-`index.md:NNN` prose-ref ambiguity; build-neutral hygiene item)
- l4-entries-section-3.7-line-range-citation-drift (tracked-observation, caveat 4 — pre-existing §3.7 line-range drift in L4 entries, preserved verbatim by the move; out-of-D1-scope correction)
- (Caveats 2 [linter expected-unreachable matcher confirm — already covered by the kept-deferred batch-37 linter-maintenance bundle] and 3 [pre-existing 135 "Potential incomplete link" warnings — no action] are benign flag-only notes; NOT promoted as new OQs.)

Build-relevant: yes (edits touch book/src/*.md extensively — the move + ~97-file cross-ref rewrite + SUMMARY.md; integrator-finalize MUST rebuild)

Reachability/rank impact: NEUTRAL — no frontmatter `rank:`/`edges:`/`status:` touched; no dep-map edges added or retyped. Pure path relocation + cross-ref rewrite + SUMMARY Part link.

Notes: VERIFY-NOT-REDO dispatch — the dispatch applied all edits directly in book/src and they pass the hard gate; my role was to verify the on-disk state (done, all checks green) rather than re-apply. The new `# Semantic surface` Part is correctly ordered (Feature Part → Semantic surface → L4) per the 2026-06-06 semantic-consolidation directive-A. `integrated_at:`/`integration_commit:` deferred to integrator-finalize per role-spec. D2 (the 24-file restatement-cohort relocation sweep) is the next serial per-report integration this cycle — I did NOT read D2 and make no claim about its on-disk state.

---

## 2026-06-06T201018Z-layer-intro-author-cohort-sweep (D2)
applied_at: 2026-06-06T205112Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied (verify-not-redo — edits were applied directly in book/src by the dispatch; this row records VERIFICATION of the on-disk applied state)

Files touched (by the dispatch; VERIFIED on disk this invocation, not re-applied):
- 24-file restatement-cohort relocation sweep — Tier B (5 files: `L2/nrm2.md`, `L3/nrm2.md`, `L2-L1/linear-combination-fold-specialization.md`, `L3/blas1-intro.md`, `concepts/elementwise-product.md`) dropped the residual general "NOT rank-1 / named shape groups per" echo, KEPT the §1.2.1 back-link; Tier C (19 files / 25 occurrences: L2/L3/L4 dot/inner_product/normalize/reciprocal/elementwise_product/axpy-family + `L2/gram.md`, `L2/scal.md`, `L2/axpby.md`, `L2/axpbypcz.md`, `L4/sparameter_reduce.md`) trimmed the bare "(arbitrary, unknown rank — NOT rank-1)" parenthetical to the op's OWN "arbitrary, unknown rank" fact, retaining the file's existing §1.2.1 back-link.
- 4-file L4 bare-basename prose-ref cleanup (`L4/iterate-while.md` 10×, `L4/ksp_solve.md` 4×, `L4/chebyshev.md` 1×, `L4/index.md` 1×) — stale inline-code citations `l4_calculus.md:NNN-MMM` → `index.md:NNN-MMM` (D1 moved content verbatim; line ranges preserved).

Verification performed (this invocation, off disk):
- `grep -rn 'l4_calculus\.md' book/src` → 0 (GATE 1 HOLDS; exit 1 = no matches) — all bare-basename prose refs gone.
- `grep -rln 'NOT rank-1\|not rank-1\|carries the same-shape contract\|accidentally read as' book/src` → 0 (GATE 2 HOLDS; exit 1) — cohort echo fully swept, no kept-exception.
- Spot-checked cohort files retain OWN shape fact + §1.2.1 back-link to `../semantics/index.md`: `L2/nrm2.md` ("operand is one shape group `S` of arbitrary unknown rank (see [`l4_calculus`](../semantics/index.md) §1.2.1)"); `L2/axpy.md` ("`S` is the shared shape group of arbitrary, unknown rank … (see [`l4_calculus`](../semantics/index.md) §1.2.1)"). Per-file `semantics/index.md` link counts ≥1 on all spot-checked files (L2/nrm2=1, L2/axpy=1, L3/dot=1, L4/inner_product=3, concepts/elementwise-product=2).
- META overall_status: ready (canonical); all 8 critic checks PASS (clean report, no repair needed). cross-reference-integrity + edge-label-fidelity (the load-bearing relocation-not-deletion axes) independently re-verified by the critic per-file.
- Did NOT run `cargo make book` (integrator-finalize runs it once at cycle-end); the dispatch + critic both reported EXIT 0 on it.

Gate hits:
- citecheck bounds scan (per-report subset, --scan --quiet on the report CYCLE.md): 25 ok, 0 failing (25 checked). All citations resolve. No MISS/AMBIG/OOB. Not blocking.
- All other per-report safety-net gates: N/A for a prose-trim sweep (no concept_writes / forward-edge / variant-axis / rank-promotion / dep-map-row / SUMMARY-chapter-registration-without-proposal / alpha-position-insert / placeholder-displacement / implied-stub-materialization).
- Graded-stack rank gate: no rank promotions in this report (frontmatter untouched — reachability/rank-neutral). Nothing to assert.

Open questions promoted (to scaffolding/open-questions.md, append-only):
- No NEW OQs. The D2 report's "Open questions / caveats" are: (1) the Tier-C judgment now RESOLVED by directive — appended a RESOLUTION NOTE (READY-TO-CLOSE) to the existing `named-shape-groups-general-rule-restatement-cohort-extent` entry (opened cycle-115, MIGRATED-to-plan), recording the cohort is FULLY SWEPT (Tier A+B+C) and meta-phase may close it; (2) no-frontmatter-touched + (3) `l4_calculus` link-text-retained — both benign flag-only notes, not new questions, not promoted.

Build-relevant: yes (edits touch book/src/*.md — 24-file cohort trim + 4-file L4 basename cleanup; integrator-finalize MUST rebuild)

Reachability/rank impact: NEUTRAL — no frontmatter `rank:`/`edges:`/`status:` touched; no dep-map edges added or retyped. Pure prose trim + inline-code prose-ref rewrite.

Notes: VERIFY-NOT-REDO dispatch — the dispatch applied all edits directly in book/src and they pass both hard gates; my role was to verify the on-disk applied state (done, all green) rather than re-apply. D1 (the semantic-surface move, applied this cycle) is recorded in the row ABOVE; I observed off disk this invocation that the surface lives at `book/src/semantics/index.md` and the cohort back-links resolve to `../semantics/index.md` (consistent with D1 having landed). With D2, the c116 LEAD `semantic-consolidation-campaign` cohort restatement sweep is COMPLETE. `integrated_at:`/`integration_commit:` deferred to integrator-finalize per role-spec.

---
