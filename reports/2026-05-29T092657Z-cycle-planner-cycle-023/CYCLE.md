---
agent: cycle-planner
invoked_at: 2026-05-29T092657Z
scope: cycle-023 dispatch plan
status: pending
---

# Cycle-023 dispatch plan

**Cycle-023 is the SECOND primary cycle of meta-batch-6** (cycles 022/023/024). The batch-6 meta-phase fires after cycle-024 finalize (not this cycle). Cycle-022 closed with 9 firm landings (eigsolve L1 chain step-1 done, L2 entry unblocked, BLAS-1 floor 8/8, deflate/gram L2 vocabulary landed). This plan fills the cycle-023 wave slots from the highest-fan-out priorities and the cycle-022 integrator handoff.

## Goals selected this cycle

**Fan-out prioritization:**
- **L2 `eigsolve` entry (chain step 2)** — the strict prerequisite for L3 backfill; HIGH fan-out (unblocks the whole eigsolve layer cohort). Now unblocked by cycle-022's L1 firm.
- **`nleps_deflated_solve` L1** — next fan-out-ranked NLEPS piece; dual fan-out: interior NLEPS vocabulary + the **positive Galerkin source site** that would promote `deflate` partly-constructive→firm.
- **L2>L1 lowering themes for the new L2 ops** — `gram-fold-specialization` + `deflate-composition-lowering`; unblocked by the firm L2 anchors.
- **L1>L0 lowering themes for the new L1 ops** — `lu-solve-mutation-rotation` + `nleps-deflated-residual-mutation-rotation`; unblocked by firm L1 anchors.
- **Verified-against audit** — `orthogonalize-composition-lowering` three-way-delegation-boundary (low priority, mechanical audit).
- **Carry-forward layer-intro work** — L1 motif refresh + `eigsolve`-firm stale narrative cleanup.

This cycle consolidates the cycle-022 landings into lowering themes, promotes `deflate` partly-constructive→firm (if the `nleps_deflated_solve` source site surfaces), and unblocks L3 eigsolve by authoring the L2 entry.

## Dispatches

1. **agent: `harvester`** | **scope:** L2 `eigsolve` entry (the apply-linop ▷ ksp_solve composition, likely; possible stub first) | **deps:** none | **rationale:** Chain step 2, now unblocked by L1 firm cycle-022. The entry body should either be the firm named composition (if shift-invert is a simple `apply_linop(A_shift_inv, v)` pass-through) or authored as a stub for refinement if the Palace shape requires additional scoping. HIGH fan-out — gates the L3 backfill (predicted `partial-obstruction`). Routes to: plan Backlog "eigsolve-prerequisite-chain" High-fan-out item (chain step 2). Refs: OQ `eigsolve-l1-firm-landed-chain-step-1-done-l2-entry-unblocked` (integrator-signals cycle-022), plan priorities Backlog High fan-out. Positive anchor source: Palace shift-invert machinery, likely `slepc.cpp` solver setup range.

2. **agent: `harvester`** | **scope:** L1 `nleps_deflated_solve` (the Schur-complement block solve at `palace/linalg/nleps.cpp:504-537`) | **deps:** none (intra-cycle parallel safe; references firm L1 anchors `lu_solve`, `ksp_solve`, `dot`) | **rationale:** Next fan-out-ranked NLEPS piece. The `deflated_solve` lambda wraps `gram(coords) + lu_solve(coords) + linear_combination(deflate_correction) + dot(residuals)`. Firm-on-positive-structure (the sole literal Schur-solve site; full composition cited). DUAL fan-out: (a) NLEPS interior vocabulary (reused by remaining 3 deferred pieces: deflated-Jacobian, deflated-eigenvalue-correction), (b) the **positive anchor that would promote `deflate` partly-constructive→firm** (the bare-Galerkin core `I − X(XᴴX)⁻¹Xᴴ` currently constructive, this is its Palace use site). Routes to: plan Backlog High fan-out (nleps-deferred-l1-pieces #2). Refs: OQ `nleps-deflated-solve-is-next-fan-out-ordered-nleps-piece-and-l2-deflate-gram-positive-site` (integrator-signals cycle-022), `deflate-l2-partly-constructive-landed-promotion-gates-on-positive-galerkin-site` (integrator-signals cycle-022). Anchor source: `palace/linalg/nleps.cpp:504-537` lambda.

3. **agent: `abstractor`** | **scope:** `gram-fold-specialization` L2>L1 lowering theme | **deps:** dispatch #2 (ensures `nleps_deflated_solve` context + `gram` consumer anchored) | **rationale:** The double-Dot-loop fusion lowering the firm L2 `gram` fold (`G = XᴴX → Matrix[k,k]`) into its L1 `inner_product` constituent (or direct `dot` calls if inner_product is still rough-in; `gram` references both). Cites the sole literal Gram-build site `nleps.cpp:524-531` (the specific loop structure `for i,j: G[i,j] = X[j]ᴴ·X[i]`). Sibling to the firm `inner-product-fold-specialization` theme it lifts. Routes to: plan Backlog Medium fan-out. Refs: OQ `gram-l2-l1-lowering-theme-double-dot-loop-fusion` (integrator-signals cycle-022). Anchor sources: `book/src/L2/gram.md` (firm cycle-022), `palace/linalg/nleps.cpp:524-531`.

4. **agent: `abstractor`** | **scope:** `deflate-composition-lowering` L2>L1 lowering theme | **deps:** dispatch #2 (ensures `nleps_deflated_solve` + `deflate` composition anchored) | **rationale:** Narrates the firm L2 `deflate` Schur-form pipeline forward into L1: `coords ▷ schur-solve ▷ back-project` lowers to `gram(X) ▷ lu_solve(...) ▷ linear_combination(X, coords)` (the `dot` normalizer is a separate sub-step). Absorbs the Schur-factorization engineering (distinguishes Schur-modified core from bare-Galerkin `I − X(XᴴX)⁻¹Xᴴ` if both are evidenced). Routes to: plan Backlog Medium fan-out. Refs: OQ `deflate-l2-l1-lowering-theme-needed` (integrator-signals cycle-022). Anchor sources: `book/src/L2/deflate.md` (partly-constructive cycle-022), `palace/linalg/nleps.cpp:505-537`.

5. **agent: `abstractor`** | **scope:** `lu-solve-mutation-rotation` L1>L0 lowering theme | **deps:** none (L1 `lu_solve` firm cycle-022) | **rationale:** The small-dense direct solve `x = lu_solve(A, b)` lowers to the Eigen-backend `fullPivLu().solve(A, b)` at L0. Firm-on-positive-structure (Palace uses this one literal path `palace/linalg/lu.cpp` + the BLAS kernel path). Load-bearing factorization-variant axis (pivoting strategy, e.g., full-pivot vs partial). Routes to: plan Backlog High fan-out (new L1 ops section). Refs: OQ `lu-solve-mutation-rotation-l1-l0-theme-needed` (integrator-signals cycle-022). Anchor sources: `book/src/L1/lu_solve.md` (firm cycle-022), `palace/linalg/lu.cpp` (or equivalent).

6. **agent: `abstractor`** | **scope:** `nleps-deflated-residual-mutation-rotation` L1>L0 lowering theme | **deps:** none (L1 `nleps_deflated_residual` firm cycle-022; L1 `apply_nonlinear_pencil`, `nrm2`, `lu_solve`, `dot` all firm) | **rationale:** The deflated residual `r = T(λ)·(vv + X·(λI−H)⁻¹·vv₂), r₂ = Xᴴ·vv, norm = √(‖r‖²+‖r₂‖²)` lowers to composition: `apply_nonlinear_pencil` + `lu_solve(H, coords)` + `linear_combination(X, coords)` + `dot(deflation_extension)` + `nrm2(two_component_pair)`. Firm-on-positive-structure (the sole literal NLEPS deflation-residual site, `nleps.cpp:547-577`). Routes to: plan Backlog High fan-out (new L1 ops). Refs: OQ `nleps-deflated-residual-l1-l0-lowering-theme-needed` (integrator-signals cycle-022). Anchor sources: `book/src/L1/nleps_deflated_residual.md` (firm cycle-022), `palace/linalg/nleps.cpp:547-577`.

7. **agent: `lowering-verifier`** | **scope:** `orthogonalize-composition-lowering` L2>L1 three-way-delegation-boundary audit | **deps:** none (the firm L2>L1 theme from cycle-022 is in-place) | **rationale:** Standard `verified_against:` audit (per-citation `verdict`/`audited_at`). Confirms non-duplication across three delegation boundaries: (i) stage-selection ⟂ (ii) Sub-pattern D inner-product unfusing ⟂ (iii) orthogonalize-mutation-rotation in-place `w.Add` L1>L0. The three themes should partition the lowering without overlap; the audit verifies each orthogonal responsibility. Routes to: plan Backlog Medium fan-out. Refs: OQ `orthogonalize-composition-lowering-three-way-delegation-boundary-audit` (integrator-signals cycle-022). Anchor source: `book/src/L2-L1/orthogonalize-composition-lowering.md` (firm cycle-022).

8. **agent: `layer-intro-author`** | **scope:** L1 §Semantics motif refresh + `eigsolve`-firm narrative cleanup | **deps:** none | **rationale:** Two editorial follow-ups surfaced by cycle-022 integration: (a) the `lu_solve` entry introduces a fifth L1 semantic motif — "operator-to-data introspection" (like `assemble_diagonal`, returning operator properties rather than action). Append to L1 `index.md` §"Semantics (overlay)" motif list (candidate bullet). (b) The `eigsolve`-firm L1 entry has a stale cycle-009 narrative bullet ("test-coverage-bounded rough-in premise was over-stated") that should be lifted into the L1 intro prose to reflect the current firm law-confidence basis. Routes to: plan Backlog Low fan-out (navigational). Refs: OQs `lu-solve-layer-intro-count-refresh-and-fifth-motif`, `eigsolve-firm-stale-cycle-009-narrative-bullet-routes-to-layer-intro-author` (integrator-signals cycle-022). Anchor sources: `book/src/L1/index.md`, `book/src/L1/lu_solve.md`, `book/src/L1/eigsolve.md`.

## Overlap analysis

| Dispatch pair | Overlap? | Status | Notes |
|---|---|---|---|
| #1 (L2 eigsolve entry) vs others | NONE | PARALLEL | The L2 entry is a NEW file; no dep-map cross-writes with others. |
| #2 (L1 nleps_deflated_solve) vs #3,#4 | NONE | PARALLEL | Dispatch #2 is a NEW L1 file; #3/#4 write new L2>L1 themes to `L2-L1/index.md` (disjoint from L1/index.md). Safe parallel. |
| #3 (gram-fold-specialization) vs #4 (deflate-composition-lowering) | NONE | PARALLEL | Both are NEW themes under `L2-L1/index.md`; disjoint rows at dep-map append. The integrator re-reads disk fresh before each append. |
| #5,#6 (L1>L0 themes) vs others | NONE | PARALLEL | Both are NEW themes under `L1-L0/index.md`; disjoint rows. Safe parallel. |
| #7 (orthogonalize audit) vs others | NONE | PARALLEL | The lowering-verifier appends a `verified_against:` block INSIDE the existing firm chapter (`book/src/L2-L1/orthogonalize-composition-lowering.md`); does NOT touch dep-map or other files. Safe parallel. |
| #8 (layer-intro refresh) vs others | MINIMAL (L1 index) | PARALLEL | Dispatch #8 appends to `L1/index.md` motif list + potentially touches `eigsolve.md` prose. Dispatch #2 creates NEW L1 file (does NOT edit L1/index.md). The per-report integrator for #2 will append the NEW L1 file to L1-index (count bump 16→17). The #8 dispatch's motif list append and count annotation coexist; re-read-before-edit serializes cleanly. Safe parallel (standard multi-append pattern). |

**Conflict-tolerance note:** Dispatches #1–7 are all appendable (new files + new dep-map rows + append-only chapter edits). Dispatch #8's L1-index touch (motif append + stale-narrative refinement) is naturally serialized by per-report integrator re-reads: the #2 integrator appends its NEW L1 file to the count; the #8 integrator appends/edits the motif + narrative sections. All dispatches marked **PARALLEL**.

## Sequencing schedule

**Wave 1 (parallel, no dependencies):**
- Dispatch #1: `harvester`, L2 `eigsolve` entry
- Dispatch #2: `harvester`, L1 `nleps_deflated_solve`
- Dispatch #5: `abstractor`, `lu-solve-mutation-rotation` L1>L0
- Dispatch #6: `abstractor`, `nleps-deflated-residual-mutation-rotation` L1>L0
- Dispatch #7: `lowering-verifier`, `orthogonalize-composition-lowering` audit
- Dispatch #8: `layer-intro-author`, L1 motif + eigsolve narrative

**Wave 2 (depends on #2 landing; parallel after #2 integrator completes):**
- Dispatch #3: `abstractor`, `gram-fold-specialization` L2>L1
- Dispatch #4: `abstractor`, `deflate-composition-lowering` L2>L1

**Rationale:** Dispatch #2 (nleps_deflated_solve) must land before #3/#4 (its lowering themes) author context-fresh L2>L1 narratives referencing it. All wave-1 dispatches are independent: #1 is a new L2 file (no cross-write); #5/#6 are new L1>L0 themes (independent of #2's L1 file); #7 is an append-only audit; #8 is L1-index editorial. Wave-2 (#3/#4) depend on #2 integrator's disk write of the NEW L1 file, then proceed in parallel.

## Open questions / caveats

**None blocking dispatch.**

- **L2 `eigsolve` candidate scope:** The dispatch directive suggests the entry is likely a named composition `apply_linop ▷ ksp_solve` (shift-invert kernel). If Palace's shift-invert setter (`SetShiftInvert` or equivalent) does NOT materialize a simple composition, the entry may remain a stub ("shift-invert eigenvalue problem formulation") pending a more detailed harvester pass. Either outcome unblocks L3 backfill (the chain step 2 role, not the L2 maturity tier).

- **`deflate` promotion gate:** Dispatch #2 (`nleps_deflated_solve`) is the final ingredient for `deflate` partly-constructive→firm IF the source site at `nleps.cpp:504-537` is recognized as the positive Galerkin anchor the cycle-022 entry flagged as the promotion condition. The integrator-per-report for #2 will surface this in its Notes; the meta-phase may enact the promotion at batch-5 (if the site is firm-enough-to-anchor) or defer to a follow-on dispatch.

- **Inline-anchor drift note:** The five dispatches involving L1>L0 themes (#5/#6) and L2>L1 themes (#3/#4) should use the `tools/citecheck/citecheck.py --anchor` tool (or codemap MCP re-reads) to verify line-exact anchors. Cycle-022 integrator-signals noted inline-anchor drift as a stable 3-cycle pattern; the cycle-022 batch-5-ASK-enacted `tools/citecheck/` is available (cycles 022 lifter used it for citation-drift sweep). **Recommendation:** producer self-verify spot-lines via codemap before dispatch.

- **L1 motif framing (#8):** The "operator-to-data introspection" motif (e.g., `assemble_diagonal`, `lu_solve`) is distinct from operator-action and from reduction-to-scalar folds; the motif title is provisional. Confirm with `layer-intro-author` that the framing is philosophically sound before integrating.

---

## Suggested next-cycle dispatch (cycle-024, batch-6 third cycle)

The cycle-024 planner should prioritize:
- **Completion of deflation/orthogonalize audits** (if not finished cycle-023): `deflate` promotion-gate enactment, remaining lowering-verifier audits on the `gram`/`deflate` cohort.
- **L3 `eigsolve` backfill** (now unblocked if #1 firms the L2 entry): the strict prerequisite chain is complete; L3 backfill can author kernel+driver pair (predicted `partial-obstruction` for the linear-EVP, opaque-library-owned iteration).
- **Remaining NLEPS L1 pieces** (3 carried): `nleps_jacobian_action` (or fold into `apply_nonlinear_pencil` law-expansion), `nleps_eigenvalue_correction` (quasi-Newton step; likely `partly-constructive`).
- **Lower-layer vocabulary priority** (user directive): any remaining L1/L2 firm-gaps that unblock higher-layer work (e.g., if `incremental-least-squares` L2 stub needs firming, or matrix-weighted-norm L1>L0 theme).

---

**Cycle-023 plan authored by cycle-planner, invoked 2026-05-29T092657Z. Awaiting dispatch confirmation and integrator cycle closure.**
