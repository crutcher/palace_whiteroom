---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-09T000315Z
scope: cycle-148 maintenance-floor full-hygiene sweep (batch-49 OPENER) — standing per-batch graded-stack/RE-set/kernel-API/FINALIZATION hygiene
status: pending
---

# CYCLE: Cross-layer observation — batch-49 OPENER maintenance-floor full-hygiene sweep

## Summary
Ran the standing once-per-batch full-hygiene checklist (maintenance-floor item-1, `maintenance-floor-standing-hygiene`) against the held c148 baseline. **Verdict: CLEAN BILL on 6 of 7 checklist axes; 1 PRE-EXISTING (not-drift) finding** — `book/src/L1/index.md` retains 18 inline `cycle-NNN`/`cNNN` (and one `(cycle-008)`) process-accounting attributions that the batch-47/48 FINALIZATION de-bulk campaign (≈258/392 files) did not sweep. It is NOT a re-accretion this batch (no maintenance batch authored book content; last touch was the batch-47 rename commit `7678f72`, 2026-06-08), so the FINALIZATION static-state standing-liveness invariant (no NEW accounting) HOLDS — but the chapter is a residual un-finalized surface worth one targeted de-bulk pass. All two hard graded-stack invariants hold; all baseline totals matched exactly; the 3 `realizes-kernel-api` edges stay `reference`-class; the RE-set premises hold with no fired promotion; DIRECTIVE-1 MPI boundary intact.

## Observation kind
**Audit residue** — a FINALIZATION de-bulk residue (incomplete-campaign coverage of one index chapter), surfaced by the batch-48-codified static-state-surface liveness check. Not consistency drift (no signature changed); not a coverage gap, edge-mismatch, or vocabulary mismatch. All other axes: clean bill.

## Specific finding

### Checklist results (held c148 baseline)

1. **Graded-stack two-invariant tripwire — PASS.** `python3 tools/graded-stack-lint/graded_stack_lint.py --book-src book/src`: `rank_violations=0`, `unresolved_depends_on_targets=0` (RESULT line `0 rank violation(s)`, no unresolved-target line emitted). Baseline totals HELD EXACTLY: `files=392, typed=331, untyped=61, roots=45, promotion_frontier=11, detritus=123 (true_detritus=51 / reference_reachable=72), expected_unreachable=54`. No newly-orphaned node; detritus escalate-guard not tripped (123 unchanged, true_detritus 51 unchanged). Rank histogram unchanged (`firm 224, rough-in 4, partly-constructive 3, obstruction 2, partial-obstruction 4, roadmap_goal 4, typed-no-rank 90`).

2. **RE-set premise re-check — PASS (premises HOLD).** The 11-member promotion frontier is the expected terminal in-scope set (RE4-adjacent `L1-L0/bicgstab|minres|eigsolve-convergence` enum-only/consumer-gated leaves; `deflate`/`deflate-composition-lowering` (RE3); `eigsolve-impl`/`lanczos_step`/`nleps-deflated-eigensolve`; `L4/sharding-decompose-reduce` (§2g-extension); `feature/krylov-iteration.{L1,L4}` (RE8)). NO promotion condition has FIRED — every frontier member is "ready to climb IFF its own evidence/consumer arrives"; no new blocking `depends-on` consumer wired in. The `eigsolve-impl`/`lanczos_step` co-`roadmap_goal` gate stays NON-FIRING (arm-A positive-structure structurally-unsatisfiable per `palace/linalg/ksp.cpp:53-57` enum-only-stub; arm-B blocking consumer not in flight). Sharding-node solve-generalization consumer-gated, DIRECTIVE-1 MPI/distributed OUT. RE11 reference-only-reachable cohort (72) §2g-by-design.

3. **Semantic-surface liveness — PASS.** `book/src/semantics/index.md` §0.1 "Active-management discipline" present and intact. Maintenance batch authored no vocabulary → no new restatement cohort warranted, none observed. Surface untyped-by-design (root-class).

4. **Kernel-API/impl integrity (DIRECTIVE 3) — PASS.** All 3 `realizes-kernel-api` edges stay `reference`-class, NOT `depends-on`. The edge `kind:` annotations explicitly self-document as free/navigational/NOT-depends-on:
   - `L3/eigsolve-impl.md:21` — `kind: realizes-kernel-api … reference-class (navigational, free — does NOT constrain rank, does NOT carry liveness)` → `L3/eigsolve` (kernel-api) + `L4/eigsolve` sibling.
   - `L1/libceed-quadrature-kernel-impl.md:14` — `kind: realizes-kernel-api … (free, navigational; NOT depends-on)` → `fe-assemble-libceed-boundary-obstruction`.
   - `L1/multigrid-relaxation-smoother.md:26` — `kind: realizes-kernel-api … (free, NOT depends-on)` → the kept opaque GS-SSOR / `triangular-solve-obstruction` kernel-api.
   The lint confirms 0 blocking-edge introduction (rank/reachability totals unchanged; the impls remain reference-reachable in the §2g cohort, exactly the DIRECTIVE-3 design).

5. **FINALIZATION static-state-surface liveness — PASS on the NO-NEW-ACCRETION invariant; ONE PRE-EXISTING residue surfaced.** Zero `verified_against:` blocks, zero `reports/2026…` pointers in `book/src/**` outside the carve-out (`methodology/goal-flow.md` + `meta-reviews/*`). The maintenance batches authored no `book/` content → the no-new-accretion invariant is vacuously satisfied (CLEAN). **Residue:** `book/src/L1/index.md` is the SOLE chapter carrying inline `cycle-NNN`/`cNNN` process attributions — 18 occurrences (`c022`×3, `c077`, `c088`×2, `c089`×2, `c091`×2, `c124`×4, `c125`×2, `(cycle-008)`×1), e.g. line 39 "The L1>L0 lowering — `ksp-solve-mutation-rotation` (cycle-008) — is the first…". Last touch = batch-47 rename commit `7678f72` (2026-06-08), so this is PRE-EXISTING finalization-campaign residue, NOT a this-batch re-accretion. The `## Status`-as-sole-rank-carrier tokens (the L1 prose-dep-map convention) are intact (not stripped). No firm-frontmatter-rank entry carries `## Status` promotion-history prose.

6. **DIRECTIVE-1 MPI boundary — PASS.** No MPI/sharding lifted as active work. The `Par*` hits in active L1-L4 chapters are L0 source-symbol citations read as single-rank equivalents (e.g. `L1/fe_assemble.md:155` cites `ParOperator::SetEssentialTrueDofs`, `palace/linalg/rap.cpp`) — the documented DIRECTIVE-1 disposition, not active lifts. Sharding-math stays exploratory `roadmap_goal`-class (`L4/sharding-decompose-reduce`).

7. **Opportunistic detritus / edge-typing GC — PASS, no new dead-intent.** `true_detritus=51` unchanged, dominated by the consumer-gated GROUND-don't-remove false-detritus cohorts (GMG/AMR leaves `dorfler_mark`/`flux_recovery_estimate`/`amr-estimate-mark-refine`/`assemble_diagonal`/`chebyshev`/`jacobi-smoother`/`normalize`/`reciprocal`/`elementwise_product`; the eigsolve-impl/NLEPS/`lanczos_step` consumer-gated cluster; `libceed-quadrature-kernel-impl` reference-reachable via realizes-kernel-api). The 19 STRONGER-GARBAGE-SIGNAL nodes are all recognized consumer-gated future-deps of reachable goal nodes (GMG/AMR/eigsolve consumers) — GROUND-don't-remove applies; none is genuine NEW dead-intent. No node recommended for removal.

## Recommendation
- **Primary (the one finding): Defer — record for the batch-49 meta-phase as a targeted FINALIZATION de-bulk follow-up.** `book/src/L1/index.md` should get a single `finalization-debulk` pass to strip the 18 inline `cycle-NNN`/`cNNN`/`(cycle-008)` provenance attributions (the same strip-keep-lift discipline the batch-47 campaign applied to the ≈258 swept files), preserving the dep-map structure, the prose `## Status` rank-carrier tokens, and the lowering cross-links (drop only the parenthetical cycle stamps). This is a content edit on `book/`, so it is NOT mine to apply (audit-class dispatch, no `book/` mutation). Route: a `layer-intro-author` (index-page owner) de-bulk dispatch in a future cycle that opens `L1/index.md`, OR fold into the batch-49 meta-phase's FINALIZATION-liveness standing duty. Fan-out: LOW/hygiene; non-urgent (it does not affect any invariant or any rendered claim — the cycle stamps are accurate, merely process-accounting that the static-state directive removes).
- **All other axes: CLEAN BILL — no action.**

## Supporting evidence
- Lint output (this run): `rank_violations=0`, `unresolved_depends_on_targets=0`, `files=392 typed=331 untyped=61 roots=45 promotion_frontier=11 detritus=123 (true_detritus=51 reference_reachable=72) expected_unreachable=54` — matches held c148 baseline exactly.
- Kernel-API edges: `book/src/L3/eigsolve-impl.md:21,23`; `book/src/L1/libceed-quadrature-kernel-impl.md:14`; `book/src/L1/multigrid-relaxation-smoother.md:26` — all `kind: realizes-kernel-api`, reference-class.
- Semantic surface: `book/src/semantics/index.md:24` (`## 0.1 Active-management discipline`).
- FINALIZATION residue: `book/src/L1/index.md` — 18 inline cycle attributions; `git log -1 -- book/src/L1/index.md` = `7678f72` (batch-47, 2026-06-08), confirming pre-existing-not-re-accreted.
- DIRECTIVE-1: `book/src/L1/fe_assemble.md:155,157` — `ParOperator::*` as L0 single-rank citations.
- Git: HEAD `81b3e09` (batch-48 meta commit), working tree clean except the new `reports/` dir — confirms no book mutation since batch-48; the hygiene targets are byte-identical to the held baseline.

## Open questions / caveats
- **OQ (for batch-49 meta-phase): `l1-index-finalization-debulk-residue`** — `book/src/L1/index.md` carries 18 inline `cycle-NNN`/`(cycle-008)` process-accounting attributions un-swept by the batch-47/48 FINALIZATION campaign. Pre-existing (not drift); strip via one `finalization-debulk` pass when a cycle next opens the file, or fold into the meta-phase FINALIZATION-liveness standing sweep. LOW/hygiene, no invariant impact. (Worth a quick grep across ALL `book/src/**/index.md` group-intro pages in that future pass — `L1/index.md` was the only hit in the L*/feature/synthesis/concepts scan, but the meta-phase may want to confirm the other Part `index.md` pages are equally clean of inline cycle stamps; this sweep found none beyond `L1/index.md` in the scanned scope.)
- The pre-existing deferred-cosmetic `l2-index-acc-katex-render-warn` (planner-flagged, step-5c-safe table-cell) was NOT re-examined this sweep (out of the checklist scope; carried, not force-fixed).
- No methodology-adjustment signal warranting a mid-batch friction-ledger flag. The maintenance-floor near-empty texture is the post-resolution steady state (`plateau-as-scope-boundary-not-project-boundary`, addressed, non-escalating).
