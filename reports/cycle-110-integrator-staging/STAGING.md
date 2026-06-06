# cycle-110 integrator staging log

Per-report integration rows, newest LAST (append-only). Row ORDER is the authoritative apply-order record (NOT the `applied_at` timestamps, which are advisory). integrator-finalize reconciles from this log.

---

## 2026-06-06T001708Z-layer-intro-author-reduce-cohort-grounding
applied_at: 2026-06-06T003932Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4/krylov-step.md (frontmatter edit: +3 `composes` `depends-on` edges → L4/dot, L4/nrm2, L2/orthogonalize, inserted after the L2/krylov-step lowers-to edge, before the concepts/op-params uses-record block)
- scaffolding/open-questions.md (append-only: 4 OQ blocks promoted — see below)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- rank-invariant violations: 0 (graded-stack lint HELD 0 before and after)
- forward-edge-without-surface: 0
- edge-label/prose mismatch: 0 (critic verified each new edge's prose discusses the exact edge it labels)
- concept_writes-on-existing-slug: 0 (frontmatter-only, no new concept page)
- SUMMARY/index registration: n/a (frontmatter-only, no new chapter/row)
- citecheck (bounds + path-hygiene): 24 ok, 2 failing — see Notes (NOT in the applied edge block; non-blocking, routed-finding prose imprecision)

Open questions promoted:
- reduce-to-scalar-chain-grounded-via-krylov-step-body-composes-edges (RESOLVED-PARTIAL)
- chebyshev-jacobi-preconditioner-leg-absorbed-below-column-baseline-exception (OPEN → batch-35 meta-phase)
- gram-reduce-inner-product-is-sibling-not-composes-edge-declined (OPEN → batch-35 meta-phase)
- l3-l2-reduce-orthogonalize-midnodes-lack-typed-edges-blocks (OPEN → plan graded-stack-lazy-tail-typing)
(Progress note on the carried OQ `l2-reduce-orthogonalize-cohort-itself-unreachable-blocks-theme-grounding` is captured inside the RESOLVED-PARTIAL block above, which explicitly advances it.)

Build-relevant: yes

Notes:
- D1 is the cycle-110 LEAD. The proposed-change `[old]` anchor matched on-disk `book/src/L4/krylov-step.md` exactly; clean apply, single byte-disjoint frontmatter region.
- LINTER (graded_stack_lint.py --show-inbound), D1 in ISOLATION: reachable 107→117 (+10); rank_violations HELD 0; STRONGER GARBAGE SIGNAL 34→26 (−8); detritus 152→142 (−10); untyped HELD 60. These reproduce the repairer's META figures EXACTLY (the repairer corrected the producer's original 119/+12/140/−12 headline down to 117/+10/142/−10; the `edges:` block was NOT touched by the repairer).
- CUMULATIVE re-measure required: this is report 1 of 2. D2 (axpy-family typing, L1/{axpy,axpby,axpbypcz}.md) lands next and rescues a DISJOINT node set. Do NOT sum the per-dispatch deltas — combined reachable ≈ 119 per the producer, but the authoritative number must be re-measured by running the lint after BOTH edit-sets apply (finalize computes the cycle-record figure). My recorded 117 is D1's isolated contribution only.
- citecheck: 24 ok, 2 failing. Both failures are in NON-EDGE prose, NOT in the applied `composes` edge block (whose edge-comment citations the critic+repairer independently verified REAL + in-range). (1) [AMBIG] `krylov-step.md:94` — bare basename matching L2/L3/L4; the report's authoritative §Faithfulness uses the full `book/src/L4/krylov-step.md:94` form; line :94 exists in the L4 file. (2) [OOB] `gmres.md:471-489` resolving to `book/src/concepts/gmres.md` (35 lines) — sits inside the ROUTED Finding-2 OQ about `L2/incremental-least-squares`; the citation intends a Palace GMRES source (no `gmres.md` found under reference/palace; bare basename → producer-format imprecision). Neither failure is in the load-bearing landed edge; non-blocking. Flagged for the meta-phase to clean when it triages the routed findings.
- DECLINED/ROUTED dispositions left untouched (critic-confirmed correct): gram_reduce→inner_product sibling decline; chebyshev/jacobi preconditioner baseline-exception; L2/gram (deflate-gated) + L2/incremental-least-squares (absorbed) routings.
- Deferred integrated_at to finalize per role-spec (did NOT touch the report frontmatter).
- book/ NOT rebuilt, NOT committed (finalize's job).

---
## 2026-06-06T001708Z-layer-intro-author-axpy-family-typing
applied_at: 2026-06-06T010000Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L1/axpy.md (frontmatter prepend: layer/operator/rank:firm + edges block — 4 cites-evidence L0 depends-on + 1 lowers-to→L1-L0/axpby-mutation-rotation + 6 reference)
- book/src/L1/axpby.md (frontmatter prepend: rank:firm + edges — 5 cites-evidence L0 depends-on + 1 lowers-to→L1-L0/axpby-mutation-rotation + 5 reference)
- book/src/L1/axpbypcz.md (frontmatter prepend: rank:firm + edges — 5 cites-evidence L0 depends-on + 1 lowers-to→L1-L0/axpbypcz-mutation-rotation + 5 reference)
- scaffolding/open-questions.md (append-only: 1 OQ promoted — l1-l0-axpy-family-themes-need-scheme-frontmatter)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- rank-invariant violations: 0 (graded-stack lint HELD 0)
- forward-edge-without-surface: 0
- edge-label/prose mismatch: 0 (critic verified each lowers-to/cites-evidence edge against prose)
- concept_writes-on-existing-slug: 0 (frontmatter-only, no new concept page)
- SUMMARY/index registration: n/a (frontmatter-only, no new chapter/row)
- citecheck (bounds + path-hygiene): 14 ok, 1 failing — see Notes (NOT in any applied edge block; non-blocking)

Open questions promoted:
- l1-l0-axpy-family-themes-need-scheme-frontmatter (OPEN → plan graded-stack-lazy-tail-typing)

Build-relevant: yes

Notes:
- D2 is cycle-110 report 2 of 2 (D1 = reduce-cohort-grounding landed first; its STAGING row above this one). The three H1 anchors matched on-disk exactly; clean prepend of a single byte-disjoint frontmatter region per file. DISJOINT from D1's L4/krylov-step.md write — no conflict; I re-read all three L1 files off disk before editing and they carried no pre-existing frontmatter (began directly at `# axpy`/`# axpby`/`# axpbypcz`), confirming D1 did not touch them.
- TRUE CUMULATIVE LINTER (graded_stack_lint.py --show-inbound, run on the post-apply tree with BOTH D1 and D2 landed): reachable from roots = 119 (climbed 117 post-D1-isolation → 119 with D2's +2 disjoint themes); rank_violations = none (HELD 0); untyped (warning) = 60 (HELD); firm histogram = 201 (HELD); detritus = 140; STRONGER GARBAGE SIGNAL = 26. THIS 119 is the authoritative cycle-record figure for finalize.
- D2's standalone contribution is +2 reachable: --show-inbound confirms `L1-L0/axpby-mutation-rotation <- L1/axpby, L1/axpy` and `L1-L0/axpbypcz-mutation-rotation <- L1/axpbypcz` — both LEFT detritus. The earlier producer +12 headline was a measurement contamination (D1's krylov-step write present during D2 verification); the repairer corrected it to the standalone +2 and instructed the integrator to re-measure cumulatively, which I did → 119. The reduce-chain rescue is D1's cascade, not D2's.
- citecheck on the report: 14 ok, 1 failing. The single [MISS] is `graded_stack_lint.py:425-437` — a reference to the LINTER TOOL'S OWN source line in the OQ-premise prose (explaining the prose-`## Status` rank fallback), NOT a Palace L0 citation and NOT in any applied `edges:` block. citecheck cannot resolve a tool-internals path under reference/. All 14 L0/theme citations inside the applied edge blocks resolve [ok]. Non-blocking (no MISS/AMBIG/OOB on a load-bearing landed citation).
- OQ RESOLUTION FOR THE META-PHASE TO UNIFY: this report RESOLVES the c109 repairer-filed OQ `l1-blas-leaves-axpy-family-lack-rank-frontmatter` (open-questions.md:1311) — the three L1 leaves now carry explicit `rank: firm` + `edges:` frontmatter (mirroring scal/apply_linop/set_subvector_zero), so inbound depends-on edges from L2 consumers now rest verified firm→firm instead of vacuously. I did NOT edit that OQ block (OQ ledger is append-only between meta-phases; the meta-phase has unify/close authority) — recording the resolution here per role-spec for finalize/meta-phase visibility. Note the OQ-premise metric correction the producer flagged: the predicted untyped 60→57 was WRONG (untyped HELD 60) because the linter's prose-`## Status` rank fallback already ranked these prose-firm; the real win was Axis-2 reachability (+2), not Axis-1 untyped.
- Deferred integrated_at to finalize per role-spec (did NOT touch the report frontmatter).
- book/ NOT rebuilt, NOT committed (finalize's job).

---
