---
agent: cycle-planner
invoked_at: 2026-05-29T070743Z
scope: cycle-022 dispatch plan
status: pending
---

# Cycle 022 dispatch plan

## Goals selected this cycle

Cycle-022 is the **first primary cycle of meta-batch-6** (cycles 022/023/024; next meta-phase fires after cycle-024 finalize). The batch-5 meta-phase (just closed) explicitly planned this cycle's scope: **8 fan-out-ranked picks from the active head**, targeting the closure of **BLAS-1 L1>L0 floor coverage (7/8 → 8/8)**, the unblocking of **two HIGH-fan-out blockers** (`lu_solve` L1 primitive → `deflate`/`gram` L2 firm, and the strict `eigsolve` prerequisite chain L1-firm → L2-entry → L3-backfill), and the **deferred NLEPS L1 pieces** now unblocked by the deflate/gram L2 shape. This cycle's 8 dispatches close gaps in shared-infrastructure vocabulary (BLAS-1 + dense-solve + deflation) that gate downstream solver coverage.

## Dispatches

| # | agent | scope | deps | rationale |
|---|---|---|---|---|
| 1 | lowering-verifier / abstractor | `axpbypcz-mutation-rotation` callsite-correction + firm | none | **CLOSES BLAS-1 L1>L0 floor 7/8 → 8/8.** The cycle-021 lowering-verifier UNBLOCKED this dispatch by drafting the firm body + verified_against YAML block, but gated enactment per the cycle-012 gated-promotion discipline: three confirmed call-site classification errors in the draft must be corrected first (`palace/linalg/nleps.cpp:343-344` D→A, `palace/models/romoperator.cpp:188-189` D→A, `palace/linalg/slepc.cpp:1986` γ≠0→γ=0). Enact the drafted corrections, promote rough-in→firm. Fan-out: foundational BLAS-1 lowering every solver reuses (high reuse × 1/cost). |
| 2 | harvester | `lu_solve` L1 dense-solve primitive | none | **HIGH-fan-out blocker for `deflate`/`gram`; gates cycle-022 wave-2.** The small-dense `k×k` `fullPivLu().solve` Gram/LU decomposition (distinct from iterative `ksp_solve` + triangular `trsv`). Read from Palace `palace/linalg/nleps.cpp:533-535` (quadratic `S.fullPivLu().solve` + projection updates) and `palace/linalg/nleps.cpp:665-667` (deflation low-rank update). L1 leaf operator. Fan-out: reused across all small-dense coordinate solves in eigensolver/ROM paths. |
| 3 | harvester | `eigsolve` L1 rough-in→firm | none | **First step of the strict eigsolve prerequisite chain** (L1-firm → L2-entry → L3-backfill, in strict order; L3 backfill BLOCKED until both anchors exist). Routes: literature-anchor pass at `ksp_solve`-equivalent confidence, OR lowering-verifier law-confidence re-evaluation of the existing rough-in. Fan-out: HIGH — unblocks L2 `eigsolve` entry → THEN L3 backfill; the whole eigenmode solver cohort gates on this chain. |
| 4 | harvester | `nleps_deflated_residual` L1 | none | **Next deferred NLEPS piece (fan-out-ordered: this → deflated-solve → Jacobian → eigenvalue-correction).** Now unblocked by the cycle-021 `deflate`/`gram` L2 shape landing. Read from `palace/linalg/nleps.cpp` (the deflation residual within the quasi-Newton loop; cite the shape/structure from cycle-021's combinator-miner rough-in rows). The deflation-vocabulary anchor the `L2/deflate` combinator + the remaining 3 NLEPS pieces build on. |
| 5 | harvester | `deflate` / `gram` L2 combinator firm | 2 (must land first) | **GATED ON #2 (`lu_solve` L1).** Dispatched **wave-2 after #2 lands.** The gram (all-pairs `inner_product` fold → `Matrix[k,k]`) + deflate (oblique/Galerkin complementary projector `I − X(XᴴX)⁻¹Xᴴ`; depends on `gram`+`lu_solve`+`linear_combination`+`dot`). Decide on the `project_oblique` vs Schur-modified NLEPS factoring (this is the substantive authoring decision; cycle-021 combinator-miner proposed both rows plain-text-forward-ref only). At firm: creates `book/src/L2/gram.md`+`deflate.md`, switches L2/index dep-map rows to live links, registers in SUMMARY. Fan-out: NLEPS lowering + any deflation/Galerkin-projection reuse. |
| 6 | lifter / lowering-verifier | L3-entry citation-drift sweep | none | **Mechanical/low-fan-out; keeps firm anchors consistent.** Correct the append-only L3 `ksp_solve` entry's inner-citation drift (`:464`→`:463` on CG, `:564`→`:563` on GMRES) + the carried `inner-product-fold-specialization` L2>L1 theme's `operator.cpp` inline-anchor drift (`:624`/`:634`/`:616`). Single pass over two entries. Cites the cycle-021 integrator-signals §New dependencies notes. |
| 7 | abstractor | `orthogonalize-composition-lowering` L2>L1 theme | none | **Carry from cycle-019; the now-firm L2 `orthogonalize` anchor is ready** (cycle-019 authorship blocked on L2 anchor; landed now). Cite `dot-mutation-rotation` Sub-pattern D for the unfused `LocalDot`+`GlobalSum` inner-product realization — do NOT re-derive; the subpattern already covers it (cycle-021 same-layer-cross-cutter surfaced this). Completes the orthogonalize lowering chain. |
| 8 | layer-intro-author | L2-index prose refresh | none | **Low-fan-out navigational hygiene.** Drop the now-stale "L3 `ksp_solve` not yet on disk" clause from the L2 overview prose. Upgrade the complementarity note to a live link (the L3 entry is now firm, cycle-020). Refresh the L2 `ksp_solve` row prose (now firm, not stub; cite the cycle-021 L2 harvest + L3>L2 outer-driver theme). Fold the two L2-intro-refresh meta-flags (`L2-layer-intro-refresh-for-named-compositions` + `-for-fold-cohort`). |

## Overlap analysis

**Dispatch pairs and artifact regions:**

- **#1 ↔ #2**: No overlap. #1 edits `book/src/L1-L0/axpbypcz-mutation-rotation.md` (status flip + verified_against block + dep-map row firm-flip). #2 creates `book/src/L1/lu_solve.md` (new file). These are distinct artifact files; parallel safe.

- **#1 ↔ #3 through #8**: No overlap. #1 modifies an L1>L0 theme; #3–8 write to L1/L2/L3 operators, themes, and intro prose.

- **#2 ↔ #3 through #8**: No overlap. #2 creates L1/lu_solve.md. #3 refines L1/eigsolve.md; #4 creates L1/nleps_deflated_residual.md; #5 creates L2/gram.md + L2/deflate.md + dep-map rows; #6 fixes citations in L3/ksp_solve.md + L2>L1 inner-product-fold theme; #7 creates L2>L1/orthogonalize-composition-lowering.md; #8 edits L2/index.md prose. Distinct files, except #5 and #8 both touch L2/index.md.

- **#5 ↔ #8 (both L2/index.md)**: #5 appends two rough-in dep-map rows (gram + deflate, plain-text forward-refs) after the ksp_solve row (:53). #8 edits the ksp_solve row prose and the complementarity note in the overview (separate prose region). These are spatially non-overlapping within the file (one appends to the dep-map table tail; the other edits prose sections). However, #5 occurs in wave-2 (after #2 lands), and #8 can run in wave-1. **If #8 runs before #5, it will re-read the disk L2/index.md at prose-edit time and will not conflict with the subsequent dep-map row append.** Marked PARALLEL within the same wave is safe; #5's dep-map append is tail-only and #8's prose edits are in the overview/vocabulary sections. The `per-report` integrator applies them serially in report order; natural serialization.

- **#3 ↔ #4 ↔ #5**: #3 creates L1/eigsolve.md; #4 creates L1/nleps_deflated_residual.md; #5 creates L2/gram.md + L2/deflate.md. No shared files. #4 may forward-reference the L2/deflate combinator (if the eigsolve machinery uses deflation), but the dep-map rows are available plain-text by cycle-021 row, so #4's scope is independent. These are three distinct L1/L2 entries. Parallel safe.

- **#6 ↔ others**: #6 edits L3/ksp_solve.md (append-only post-integration; only citations updated) + L2>L1/inner-product-fold-specialization.md (same append-only status). No new files created. No producer writes to these in wave-1; #6 is a citation-maintenance pass. Parallel safe.

- **#7 ↔ others**: #7 creates L2>L1/orthogonalize-composition-lowering.md (new file). No overlaps with other dispatches. Parallel safe.

- **#8 ↔ #6**: #8 edits L2/index.md (prose sections, overview, vocabulary-cohort subsection). #6 edits L2>L1/inner-product-fold-specialization.md (citations within an existing firm theme). Different files, different artifact layers. Parallel safe.

**Summary:** All dispatches are PARALLEL within their wave, with one **hard serial dependency**: #5 (deflate/gram firm) is **gated on #2** (`lu_solve` L1) landing first — this is a genuine content dependency (the deflate author must decide the `project_oblique` vs Schur factoring choice given the `lu_solve` interface). #5 and #8 both touch L2/index.md but in different regions (dep-map append vs prose edit); the per-report integrator serializes them naturally. All other pairs are independent.

## Sequencing schedule

**Wave 1 (parallel; 7 dispatches):**
- #1: lowering-verifier/abstractor — `axpbypcz-mutation-rotation` callsite-correction + firm
- #3: harvester — `eigsolve` L1 rough-in→firm
- #4: harvester — `nleps_deflated_residual` L1
- #6: lifter/lowering-verifier — L3-entry citation-drift sweep
- #7: abstractor — `orthogonalize-composition-lowering` L2>L1 theme
- #8: layer-intro-author — L2-index prose refresh

**Wave 2 (parallel; 1 dispatch; triggered by wave-1 completion):**
- #2: harvester — `lu_solve` L1 dense-solve primitive
- #5: harvester — `deflate`/`gram` L2 combinator firm (gated on #2)

**Rationale for two-wave structure:** The `lu_solve` L1 operator (#2) is a prerequisite for the `deflate`/`gram` L2 firm dispatch (#5). Wave-1 dispatches are all independent of `lu_solve`; they can run in parallel while #2 is drafted. Once #2 lands (integrator applies and confirms on-disk), #5 becomes actionable with the firm `lu_solve` interface anchored. This keeps parallelism high (6:1 ratio in wave-1) while respecting the load-bearing dependency chain.

## Open questions / caveats

- **Callsite-correction classifications in #1 (axpbypcz):** The lowering-verifier's cycle-021 audit draft flagged three callsite classification errors (`nleps.cpp:343-344` D→A, `romoperator.cpp:188-189` D→A, `slepc.cpp:1986` γ≠0→γ=0). The dispatch should apply these corrections as drafted. If the draft corrections are not yet written into the cycle-021 report, the cycle-planner should clarify with the lowering-verifier whether the corrections are inline in the draft or if they need to be re-derived by the #1 agent.

- **`eigsolve` L1 rough-in→firm route (#3):** The active-head planning note mentions "literature-anchor pass at `ksp_solve`-equivalent confidence OR lowering-verifier law-confidence re-eval." The dispatch should determine which route: is a literature anchor available to lift the rough-in to firm, or does a lowering-verifier law-confidence re-evaluation suffice? The OQ `l3-eigsolve-blocked-on-l1-firm-and-l2-entry` / `l3-eigsolve-linear-evp-has-no-krylov-step-kernel-analog` notes flag this; the dispatcher should clarify the firm-promotion gate.

- **`deflate` vs `gram` authorship boundary in #5:** The cycle-021 combinator-miner proposed both rows plain-text-forward-ref; the harvest dispatch in #5 is responsible for deciding on the architectural choice (`project_oblique` vs Schur-modified NLEPS factoring) and authoring the full firm-body decomposition. The integrator will confirm the firm apparatus is inside the proposed-changes fence (per the cycle-021 fence-guard guidance).

- **L2/index.md L3 ksp_solve staleness in #8:** The "L3 `ksp_solve` not yet on disk" clause is explicitly stale because L3/ksp_solve landed cycle-020. However, the refreshed prose should note whether the complementarity or any other structural notes need updating beyond the clause drop. The dispatcher should verify the L2 intro narratives remain congruent with the on-disk L3 entry (cycle-020) and the newly-firm L3>L2 theme (cycle-021 ksp-solve-outer-driver).

- **Wave-2 timing:** The integrator-per-report applies #2 (lu_solve) serially, and the planner assumes integrator-finalize is complete before #5 dispatch runs. The parent orchestrator schedules the two waves; no action from the planner needed, but flagged for clarity.

---

## Notes on codemap verification

All Palace source paths in dispatch scopes above were verified via `palace-codemap` (list_files + read_range):
- `palace/linalg/nleps.cpp:343-344` ✓ (AXPBYPCZ callsite D→A correction)
- `palace/models/romoperator.cpp:188-189` ✓ (file confirmed)
- `palace/linalg/slepc.cpp:1986` ✓ (AXPBYPCZ callsite γ-branching)
- `palace/linalg/nleps.cpp:533-535`, `:665-667` ✓ (fullPivLu().solve usage for Gram solve)
- `palace/linalg/` file list ✓ (linalg/*, iterative.cpp, ksp.cpp, slepc.cpp, nleps.cpp confirmed present)

Path citations are accurate to the reference tree.
