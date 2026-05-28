---
agent: cycle-planner
invoked_at: 2026-05-28T201856Z
scope: cycle-015 dispatch plan (THIRD and FINAL primary cycle of meta-batch-3; meta-phase fires after this cycle's finalize)
status: pending
---

# Cycle-015 dispatch plan

## Goals selected this cycle

**Two HEADLINE GATED PROMOTIONS ready to ENACT** (cycle-014 audit/verification set them up):

1. **divfree-projector partly-constructive→firm** — cycle-014 lowering-verifier UNBLOCKED this (the `WeakDiv ≈ −GᵀM` sign is positively anchored in Palace-owned `palace/fem/integrator.hpp:217` + `palace/fem/integ/mixedvecgrad.cpp:202`, refuting cycle-013's "out-of-scope MFEM-vendored" premise). Cycle-015 enacts the 5 firming edits queued in the report + drops the partly-constructive caveat → `L1/divfree-projector.md` becomes firm. This closes the partly-constructive ENTRY→FIRM PROMOTION lifecycle for the meta-phase to assess.

2. **chebyshev-L4 rough-in→firm via iterate-while reanchor** — cycle-014 combinator-miner decided REUSE the `iterate-while` family (do NOT firm a new combinator). Cycle-015 enacts the re-anchor of `L4/chebyshev.md`'s `apply` body from `forM_`/`foldM` to `iterate_while_pure` + step-count predicate + flips rough-in→firm (L4 firm 3→4). This demonstrates the gated-promotion "audit cycle-N, enact cycle-N+1" pattern across the three instances (eigsolve 013, divfree 014→015, chebyshev-L4 014→015).

**Additional strong carry-overs (all VERIFIED in cycle-014 integrator-signals + open-questions):**
- `chebyshev-anchor-element-kernel-and-mult2-carry-forward-sweep` — 4 sites in `L2/chebyshev-iteration.md` (lines 35/143/245/247) + 2 sites in `L1/chebyshev-smoother.md` (lines 245/247) + `Mult2 :191`→`:190` in theme + L2 form. A lifter citation-sweep.
- `l3-krylov-step-cg-md-citation-sweep` — `L3/krylov-step.md` has 6 dangling `cg.md` pointers (lines 108/129/188/196/202/204); sibling residual of cycle-014's L4>L3 theme sweep. A lifter.
- `chebyshev-slice-l4-full-removal` — re-point `L2/krylov-step.md` + `L2/index.md` + `L3/krylov-step.md` + `L3/apply_linop.md` + `L3-L2/krylov-step-body-identity.md` §L4 citations onto `L4/chebyshev.md` anchors, THEN remove the chebyshev slice (removals 8/10 → 9/10). MUST batch with L4/chebyshev firming (gated).
- `bundle-6-l0-file-overview-next-ranking` — cycle-014 landed `linalg-rap-file` (#2); next candidate is `fem/bilinearform` (#4, per the OQ ranking). A layer-intro-author dispatch.

**Bias toward CLOSING OPEN THREADS so batch-3 ends clean:** the three citation-sweep OQs + the two gated promotions + the slice-removal gate collectively close a major wave of carry-forwards and demonstrate clean discipline under recurring citation-line-drift signal (now ≥2 cycles, affecting even the citation-AUDITING lowering-verifier role). The cycle-015 meta-phase will assess partly-constructive mechanism, gated-promotion pattern, citation discipline, and in-line non-adjacent identity rotations.

## Dispatches

| # | Agent | Scope | Deps | Rationale |
|---|-------|-------|------|-----------|
| 1 | abstractor | `divfree-projector-partly-constructive-to-firm-enactment` — apply 5 queued firming edits to `L1/divfree-projector.md`, flip §Status to `firm` | none | **HEADLINE GATED PROMOTION** (cycle-014 verifier UNBLOCKED via Palace-owned WeakDiv sign anchor). First partly-constructive→firm ENTRY promotion (complements cycle-013 EXIT). Closes OQ `divfree-projector-partly-constructive-to-firm-enactment`. |
| 2 | lifter/abstractor | `chebyshev-l4-firm-via-iterate-while-reanchor` — re-express §Signature/§Semantics `apply` body using `iterate_while_pure` + step-count predicate (sketch in cycle-014 combinator-miner report), rewrite `L4/index.md` dep-map row, flip §Status rough-in→firm (L4 firm 3→4) | 1 | **HEADLINE GATED PROMOTION** (cycle-014 combinator-miner decided REUSE iterate-while family). Demonstrates the gated-promotion pattern at its second enactment. Closes OQ `chebyshev-l4-firm-via-iterate-while-reanchor`. |
| 3 | same-layer-cross-cutter | `chebyshev-slice-l4-full-removal` — re-point all krylov-step §L4 citations onto `L4/chebyshev.md` anchors (6 files × 7 citation sites total per cycle-014 integrator-signals), THEN remove the §L4 stub from `spec/slices/chebyshev.md` (removals 8/10→9/10) | 2 | **GATED on L4/chebyshev firming** (dispatch 2). The slice §L4 ranges are intentionally STALE-until-re-point; they land only after L4/chebyshev firms. Closes OQ `chebyshev-slice-l4-full-removal`. |
| 4 | lifter | `chebyshev-anchor-element-kernel-and-mult2-carry-forward-sweep` — citation-sweep on 6 sites in `L1/chebyshev-smoother.md` + `L2/chebyshev-iteration.md` (element-kernel `:69-78`/`:114-123` drift + Mult2 `:191`→`:190` reconcile per cycle-014 verifier finding); apply repairer-corrected anchors | 2 | **Citation-line-drift closure.** Sibling to cycle-014's L1>L0/L2>L1 lowering-theme audits; firm operator anchor entries now brought in-line. Closes OQ `chebyshev-anchor-element-kernel-and-mult2-carry-forward-sweep`. |
| 5 | lifter | `l3-krylov-step-cg-md-citation-sweep` — sibling residual of cycle-014's L4>L3 theme sweep; re-anchor 6 dangling `cg.md` pointers in `L3/krylov-step.md` (lines 108/129/188/196/202/204) to the lifted-evidence convention (firm `L3-L2/krylov-step-body-identity.md` + `L3/krylov-step.md` §Algebraic-laws + concepts/sequential-obstruction.md) | 1 | **Citation-line-drift closure + operator-entry follow-up.** Cycle-014 swept theme-file dangling pointers; this sweeps the distinct operator-entry residual. Closes OQ `l3-krylov-step-cg-md-citation-sweep`. |
| 6 | layer-intro-author | `bundle-6-l0-file-overview-next-ranking` — author `fem/bilinearform` L0 file-overview chapter (next-ranked bundle-6 candidate #4). Focus: the sparse-assembly pattern (full vs partial vs matrix-free), summation family (AssemblyLevel, symmetric sparsity, precompute vs lazy), SparseMatrix + HypreParMatrix dual, single-rank-reading of Par-types. | 1 | **Lower-layer-shared-vocabulary priority** (per user directive 2026-05-27). Continues the L0 bootstrap bundle series. Closes OQ `bundle-6-l0-file-overview-next-ranking`. |

Total: **6 dispatches** (all parallel-when-in-doubt baseline, with explicit sequencing noted for gated promotions).

## Overlap analysis

**Key sequencing gates:**
- Dispatches 1, 2, 4, 5, 6 are **genuinely independent** and CAN run parallel (they edit distinct regions: L1/L2 operator entries, L3 operator, L4 operator+index, L0 new chapter, L4>L3 theme).
- Dispatch 3 (chebyshev-slice removal) **DEPENDS on dispatch 2** (L4/chebyshev firming) — the `:354-362`, `:355-362`, `:308-323`, `:330-353`, `:421-436` ranges that dispatch 3 re-points LAND in dispatch 2's L4/chebyshev.md body.
- **Dispatch 1 (divfree promotion) has NO dependencies within this cycle** — it stands alone and can run parallel with 4/5/6.
- **Dispatch 4 (chebyshev L1/L2 anchor-sweep) has NO structural dependency on dispatch 2** — it is purely a citation-range tightening in already-firm entries, independent of whether L4 firms in dispatch 2. However, **logically it's WISE to batch after dispatch 2** so the anchor-corrected entries are synchronized with the theme anchors to which cycle-014 set them; this is a **wave-2 scheduling preference, not a hard conflict**.

**File edit regions (overlap verification):**
- Dispatch 1: `L1/divfree-projector.md:§Status` — SAFE parallel.
- Dispatch 2: `L4/chebyshev.md:§Signature/§Semantics` + `L4/index.md:dep-map row` — SAFE parallel (distinct file).
- Dispatch 3: `L2/krylov-step.md:7/79/85/140` + `L2/index.md:35` + `L3/krylov-step.md:198/206` + `L3/apply_linop.md:188` + `L3-L2/krylov-step-body-identity.md:127` + `spec/slices/chebyshev.md:§L4 removal` — DEPENDS on dispatch 2 landing first (reads L4/chebyshev.md line numbers).
- Dispatch 4: `L1/chebyshev-smoother.md:245/247` + `L2/chebyshev-iteration.md:35/143/245/247` — SAFE parallel (distinct file from dispatch 1/2/3).
- Dispatch 5: `L3/krylov-step.md:108/129/188/196/202/204` — SAFE parallel (dispatch 3 touches lines 198/206, no overlap).
- Dispatch 6: `L0/fem-bilinearform.md:§new` + `L0/index.md:§registration` + `SUMMARY.md:§registration` — SAFE parallel.

**Conclusion:** Dispatch 3 is SEQUENTIALLY blocked by dispatch 2. All others can run parallel. **Wave structure:** Wave-1: {1, 2, 4, 5, 6}; Wave-2: {3}.

## Sequencing schedule

**Wave-1 (parallel):** Dispatches 1, 2, 4, 5, 6
  - Abstractor on divfree-projector firming
  - Lifter/abstractor on L4/chebyshev iterate-while re-anchor (PRODUCES the L4/chebyshev.md body that wave-2 will cite)
  - Lifter on chebyshev L1/L2 anchor-sweep
  - Lifter on L3/krylov-step citation-sweep
  - Layer-intro-author on L0 bundle-6 #4

**Wave-2 (serial after wave-1):** Dispatch 3
  - Same-layer-cross-cutter on chebyshev-slice L4-full-removal (CONSUMES the L4 anchors from dispatch 2)

**Rationale for wave-2 delay:** Dispatch 3 must read the freshly-landed `L4/chebyshev.md` line numbers from dispatch 2 to correctly re-point the 7 krylov-step citation sites. The integrator-per-report serial dispatch order will naturally enforce this (dispatch 2 integrates first, then dispatch 3 re-reads disk before applying re-points).

## Open questions / caveats

1. **Citation-line-drift signal strengthened to ≥2-cycle escalation.** Cycle-014 was specifically an audit/verification cycle (4 lowering-verifiers + 1 combinator-miner), yet 5 of 8 reports carried off-by-1-to-N anchor drift (divfree `:203` vs `:202`, rap `:140` vs `:142`, chebyshev L1>L0 `:191` vs `:190`, chebyshev L2>L1 `:190` vs `:44` (member vs comment), L4 reconcile `:309` vs `:221-233`). **All caught + repaired by the repairer pre-apply**, so integration was clean, but the volume signals a process gap. The critic's skill-uptake-survey repeatedly flags `verify-citation-range` not self-invoked by producers (3-cycle strengthening: 012/013/014). **Flagged for cycle-015 meta-phase** as a strong candidate for friction-ledger entry + possible tooling fix (e.g., mandatory pre-emit `verify-citation-range` gate, or a codemap-backed anchor-check tool). The cycle-015 dispatches above (dispatches 4, 5) are citation-sweep work that demonstrates clean discipline IF they use the skill to self-verify anchors pre-emit.

2. **Partly-constructive mechanism fully exercised across cycles 013/014/015.** EXIT (eigsolve-mutation-rotation cycle-013) + ENTRY-validated (divfree-projector cycle-014) + STAYS (eigsolve-convergence-reason-mapping cycle-014) + TWO ENACTMENTS (divfree + chebyshev-L4, cycle-015). The cycle-012-codified mechanism is in active, healthy use. Dispatch 1 and 2 above are the final enactments of this batch's gated-promotion cycle. **Flagged for cycle-015 meta-phase** as evidence that the partly-constructive status + promotion gate + lifter-scope clarifications (per CLAUDE.md) are working as designed.

3. **Gated-promotion "audit cycle-N, enact cycle-N+1" pattern now established (3 instances: eigsolve 013, divfree 014→015, chebyshev-L4 014→015).** This pattern is visible across cycles and the integrator-signals channel surfaces both the audit outcome + the enactment conditions cleanly. **Flagged for cycle-015 meta-phase** as a process pattern that's working well — the pattern naturally surfaces what's ready to promote, avoids double-work, and lets the planner stage both the audit and the follow-up. No process fix needed; just codify as methodology once meta-phase validates.

4. **In-line non-adjacent identity rotations convention (CLAUDE.md invariant, codified cycle-012 meta-phase).** Cycle-015 dispatch 5 (L3/krylov-step citation-sweep) applies the lifted-evidence convention (in-line annotation using firm `L3-L2/krylov-step-body-identity` + concepts cross-refs) rather than creating an `L3-L1/` directory. This is the enforcement cycle for the in-line annotation pattern. **If successful, the pattern is validated; flagged for cycle-015 meta-phase** as evidence supporting the non-adjacent-directory avoidance decision.

5. **Cycle-015 is the THIRD and FINAL primary cycle of meta-batch-3; the meta-phase fires after this cycle's finalize.** The three signals above (citation-line-drift escalation, partly-constructive mechanism exercise, gated-promotion pattern establishment, in-line identity convention enforcement) are all **flagged in cycle-014 integrator-signals** for the batch-3 meta-phase aggregation. Dispatch planning for cycle-015 is framed with these signals in mind — closing open threads, demonstrating clean discipline, and providing clean evidence for the batch-3 meta-phase review.

