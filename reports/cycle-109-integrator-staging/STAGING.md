# cycle-109 integrator staging log

Per-report integrator landings, newest LAST (append-only). Row ORDER is the authoritative
apply-order record; `applied_at` is advisory. integrator-finalize reconciles from this log.

---

## 2026-06-05T234424Z-layer-intro-author-l2-l1-theme-cohort-grounding
applied_at: 2026-06-06T000118Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Report: reports/2026-06-05T234424Z-layer-intro-author-l2-l1-theme-cohort-grounding/CYCLE.md
(batch-35 LEAD: the L2-L1 lowering-theme-cohort GROUNDING pass — faithful-path-or-finding, GROUND-don't-remove §(g))

Files touched (all frontmatter-only `edges:` edits, no prose claims, no new files, no SUMMARY.md change):
- book/src/L2/eigsolve.md (edit — ADD `depends-on` lowers-to → L2-L1/eigsolve-spectral-transform-composition)
- book/src/L2/ksp_solve.md (edit — ADD `depends-on` lowers-to → L2-L1/ksp-solve-outer-driver-unfold)
- book/src/L2/krylov-step.md (edit — AUTHOR `edges:` frontmatter block FROM SCRATCH: 7 firm/typed-no-rank L1 leaves depends-on + lowers-to → L2-L1/krylov-step-kernel-defusion + 10 concept references; rank: firm)
- book/src/L2/linear_combination.md (edit — UPGRADE reference→depends-on lowers-to → L2-L1/linear-combination-fold-specialization)
- book/src/L2/inner_product.md (edit — UPGRADE reference→depends-on lowers-to → L2-L1/inner-product-fold-specialization)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- concept_writes on existing slug: 0
- forward-edge claim without surface: 0
- variant-axis missing: 0
- SUMMARY.md chapter registration auto-fix: 0 (no new chapter files; pure edge-typing)
- rank-gate (graded-stack §1 well-foundedness, rank(u)≤min deps): 0 violations — re-verified on disk (see below). The 3 typed-no-rank L1 leaves (axpy/axpby/axpbypcz) make their inbound edges hold vacuously (no-rank target cannot violate), consistent with the report + repairer softening.
- citecheck bounds + path-hygiene: 9 ok, 2 failing (11 checked) — both failures are `AMBIG` on bare basenames in §Faithfulness-confirmations PROSE (`eigsolve.md:171`, `krylov-step.md:96`), where the full path is unambiguously established by adjacent context and the critic spot-checked both against the L2 files on disk. NON-BLOCKING: no prose-claim text lands in book/ (frontmatter-only edits); no MISS/OOB. Recorded, not repaired.

Linter (graded-stack-lint --show-inbound), re-run on-disk AFTER applying the 5 edits this invocation:
- BEFORE (baseline fd5fabd, per report+META): reachable 102, rank_violations 0, untyped 60, detritus 157
- AFTER (this invocation, observed on disk): reachable 107 (+5), rank_violations 0 (HOLDS), untyped 60 (HOLDS), detritus 152 (−5)
- 4 Group-A themes flipped OUT of [garbage?], now showing reachable inbound (verified on disk this invocation):
    L2-L1/eigsolve-spectral-transform-composition  <- L2/eigsolve
    L2-L1/krylov-step-kernel-defusion              <- L2/krylov-step
    L2-L1/ksp-solve-outer-driver-unfold            <- L2/ksp_solve
    L2-L1/linear-combination-fold-specialization   <- L2/linear_combination
- 5 Group-B + deflate + inner-product-fold REMAIN [garbage?] (expected — the finding; host L2 op itself unreachable):
    chebyshev-iteration-fusion, gram-fold-specialization, incremental-least-squares-composition-lowering,
    orthogonalize-composition-lowering, deflate-composition-lowering (FRONTIER, untouched), inner-product-fold-specialization
  (inner_product edge #5 laid correctly but non-flipping — L2/inner_product itself [GARBAGE*]; documented in OQ)

Open questions promoted:
- l2-reduce-orthogonalize-cohort-itself-unreachable-blocks-theme-grounding (the report's Group-B finding — promoted to scaffolding/open-questions.md this invocation; opened_at cycle-109, opened_by layer-intro-author)
- l1-blas-leaves-axpy-family-lack-rank-frontmatter (the repairer wrote this directly to scaffolding/open-questions.md during repair; confirmed already present, NOT duplicated)

Build-relevant: yes (5 edits to book/src/L2/*.md)

Notes:
- overall_status: ready (canonical token, set by repairer; META checks/repairs otherwise clean — rank-invariant warning was repaired in-place by rationale-only prose softening, the `edges:` blocks were left untouched).
- The repairer's softening edits to CYCLE.md rationale prose are NOT applied to the artifact (the edits are frontmatter-only `edges:` blocks; prose is not artifact content).
- Re-read all 5 target files off disk before editing this invocation; the on-disk `[old]` anchors matched the report's proposed-change blocks exactly (count==1 each).
- The +5 (vs predicted +4) is L2/krylov-step itself becoming a typed-and-reachable node when its `edges:` block is authored from scratch, on top of its 4 sibling theme flips — confirmed on disk (krylov-step-kernel-defusion shows inbound <- L2/krylov-step).
- No SUMMARY.md / index.md / running-count touched (pure edge-typing, disjoint 5-file write-set).
- deferred integrated_at to finalize per role-spec (did NOT touch the report's integrated_at / integration_commit frontmatter).

---
