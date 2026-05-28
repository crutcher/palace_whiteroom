---
agent: same-layer-cross-cutter
invoked_at: 2026-05-27T234651Z
scope: Phase 1 corpus reduction audit — batch 2 (orthog / chebyshev / polynomial_recurrence_step)
status: integrated
integrated_at: 2026-05-28T013333Z
integration_commit: 8bb16b7
integration_notes: cycle-011 wave-2 pass 9 (final per-report integrator dispatch of cycle-011); second-instance execution of priority #19 (phase-1-corpus-reduction-audit); 3 slices reduced (orthog + chebyshev + polynomial_recurrence_step); cumulative slice-corpus coverage 6 of 10; first negative-result slice audited (polynomial_recurrence_step.md verdict "blocked / minimal reduction; the slice IS the artifact"); 9 in-place edits applied cleanly; 0 safety-net gate hits; 5 new OQs promoted + 1 amendment to existing cycle-010 OQ l1-orthogonalize-promotion-from-arnoldi-step-and-orthog; phase-1-slice-reduction-audit skill candidate reinforced (template detailed and machine-replayable across cycle-010 batch-1 + cycle-011 batch-2); phase-1-corpus-audit-line-range-arithmetic-brittleness friction at recurrence-2 (mitigation applied successfully both cycles)
inputs:
  - book/src/spec/slices/orthog.md (464 lines)
  - book/src/spec/slices/chebyshev.md (442 lines)
  - book/src/spec/slices/polynomial_recurrence_step.md (204 lines)
  - book/src/L1/ksp_solve.md (firm; cycle-007)
  - book/src/L1-L0/ksp-solve-mutation-rotation.md (firmed cycle-008; status: rough-in *(firmed cycle-008)* per L1-L0/index.md:21)
  - book/src/L2/krylov-step.md (firm; cycle-005)
  - book/src/L3/krylov-step.md (firm; cycle-010 wave-1)
  - book/src/L3-L2/krylov-step-body-identity.md (firm; cycle-009)
  - book/src/L4/krylov-step.md (firm; cycle-006)
  - book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md (firm; cycle-008)
  - book/src/L4-L3/gmres-inner-loop-iterate-while-migration.md (firm)
  - book/src/concepts/orthogonalization.md (firm)
  - book/src/concepts/plane-rotation-stream.md (firm)
  - book/src/concepts/givens.md, givens_generate.md, givens_apply.md (firm)
  - book/src/concepts/sequential-obstruction.md (firm; with worked example "MGS as sequential-obstruction")
  - book/src/concepts/chebyshev-iteration.md (firm)
  - book/src/concepts/negative-result-slice.md (firm)
  - book/src/concepts/derived-view-hoisting.md (firm)
  - book/src/concepts/state-stratification.md (firm)
  - book/src/concepts/solve-monad.md (firm)
  - book/src/concepts/constructed-operators.md, variant-absorption.md, first-iteration-unrolling.md (firm)
  - CLAUDE.md §Methodology invariants ("Phase 1 corpus reduces as material is lifted")
  - scaffolding/priorities.md #19 (phase-1-corpus-reduction-audit)
  - reports/2026-05-27T220000Z-same-layer-cross-cutter-phase-1-corpus-reduction-audit/CYCLE.md (cycle-010 template precedent)
---

# CYCLE: Phase 1 corpus reduction audit — batch 2 (orthog / chebyshev / polynomial_recurrence_step)

## Summary

Second-instance execution of priority #19 (`phase-1-corpus-reduction-audit`) under the methodology invariant "Phase 1 corpus reduces as material is lifted". Audits three slices from the cycle-010 audit's suggested priority order (#1, #2, #3): `orthog.md` (464 lines), `chebyshev.md` (442 lines), and `polynomial_recurrence_step.md` (204 lines).

Result: all three slices are **blocked from full reduction**, but each has substantial sections that are now redundant with firm entries and warrant partial reduction (stub-with-pointer). Per-slice headline findings:

- **orthog.md**: blocked by the missing firm `L1/orthogonalize` (per cycle-010 OQ `l1-orthogonalize-promotion-from-arnoldi-step-and-orthog`). The slice's L2/L3/L4 Gram-Schmidt sections AND its L0/L1/L2/L3/L4 plane-rotation-stream sections both contain unique material that has not been lifted. **The L0/L1/L2/L3/L4 plane-rotation-stream sections (lines 313-464) overlap `book/src/spec/slices/plane_rotation_stream.md` (a sibling slice deferred to batch-3 by cycle-010 priority order)** — auditing this overlap should happen before the plane-rotation sections are reduced. Recommended action: **partial-reduction** (stub the Gram-Schmidt L1 section that is fully superseded by `concepts/orthogonalization.md`; retain L2/L3/L4 Gram-Schmidt sections and all plane-rotation-stream sections pending the deferred lifts).
- **chebyshev.md**: blocked by absence of a firm Chebyshev row in the layered artifact. Despite being cited by the firm `L2/krylov-step` Evidence list (as one of the five canonical slice instances) and by `L3-L2/krylov-step-body-identity` Evidence (`chebyshev.md:354-362`), the slice's L1/L2/L3/L4 Chebyshev-smoother content is the **only** firm Chebyshev definition in the artifact — there is no `L1/chebyshev-smoother` or `L2/chebyshev-iteration` operator entry, and the `concepts/chebyshev-iteration.md` page is a high-level prose overview (not an operator entry). Recommended action: **partial-reduction** (stub only the §Consumers + §"Concept references" + §"Open questions" sections that are now redundant with the firm artifact; retain L1/L2/L3/L4 Chebyshev-smoother content as canonical evidence pending lift of a firm L1/L2/L3/L4 Chebyshev row).
- **polynomial_recurrence_step.md**: explicitly a **negative-result slice** per `concepts/negative-result-slice.md` (the slice is itself cited as the canonical worked example at `concepts/negative-result-slice.md:46`). Its load-bearing content (the falsifiable absence claim + the cross-family distinction catalog + the within-Chebyshev partial-positive self-tightening) is **structurally not subject to reduction** — negative-result slices preserve the distinction catalog as the result. Recommended action: **blocked / minimal reduction** (only the §"L0 — Chebyshev fused-update helpers" + §"L0 — Chebyshev scalar-coefficient sequences" sub-sections that overlap firm chebyshev citations may be stubbed; the rest of the slice IS the artifact and is retained verbatim). This is a different verdict from the cycle-010 reductions because the slice's role is documentation-of-non-existence rather than precursor-to-firm-entries.

Six OQ actions are surfaced (1 amendment to an existing OQ + 5 new OQs) for material that needs lifting before further reduction is safe. The two headline blockers:
1. **L1/orthogonalize firm promotion** (amendment of cycle-010 OQ `l1-orthogonalize-promotion-from-arnoldi-step-and-orthog`; now affects 2 slices not just arnoldi_step.md). See §"Open questions / caveats" item 2 for the amendment recommendation.
2. **Firm L1/L2/L3/L4 Chebyshev-smoother row** (new) — without it, chebyshev.md cannot be reduced beyond cosmetic stubbing.

The remaining 4 OQ actions cover the plane-rotation-stream sub-slice batch-3 deferral, two concept-page extensions (state-stratification four-stratum + derived-view-hoisting control-flow-boundary), and the negative-result-slice partial-positive sub-pattern lift. Full enumeration in §"Open questions / caveats" items 1, 4, 5, 6.

The audit template established in cycle-010 is applied directly with no methodology changes. The cycle-010 friction signal `phase-1-corpus-audit-line-range-arithmetic-brittleness` (recurrence-1) is mitigated this dispatch by enumerating H2 boundaries with `grep -n "^## "` before proposing any line ranges.

## Observation kind

**Variant-axis coverage gap (audit-scoped)** — same kind as cycle-010 audit: the slices substantially overlap firm entries (or, in polynomial_recurrence_step.md's case, are explicitly referenced as canonical negative-result evidence), but each retains material that has NOT yet been lifted (or is methodologically required to remain in the slice corpus).

## Specific finding

### Slice 1: `book/src/spec/slices/orthog.md` (464 lines)

**Audit verdict**: partial-reduction (full-reduction blocked by the missing firm `L1/orthogonalize` AND by the in-slice overlap with the deferred `plane_rotation_stream.md` sibling slice).

**Structure** (per `grep -n "^## \|^# "`):
- Line 1: `# Slice: orthog` (intro)
- Lines 7-105: `## L0 → L1` (Gram-Schmidt L1 form + Citations + Test linkage + Open questions)
- Lines 106-109: `## L1 → L2` ("Deferred to next cycle on this slice.")
- Lines 110-176: `## L2 — primitive composition` (Gram-Schmidt L2 form)
- Lines 177-244: `## L3 — global tensor-field form (with sequential obstruction)` (Gram-Schmidt L3 form + MGS obstruction)
- Lines 245-312: `## L4 — calculus form` (Gram-Schmidt L4 form)
- Lines 313-322: `## Context` (start of plane-rotation-stream sub-slice; this is structurally a SECOND slice merged into the same file)
- Line 315: `# Orthogonalization (plane-rotation stream)` (note: this is an H1, indicating a major sub-slice boundary)
- Lines 323-335: `## Background` (Givens-stream textbook background)
- Lines 336-345: `## Variant axes` (plane-rotation-stream variant axes)
- Lines 346-363: `## L0 — citations` (plane-rotation-stream L0)
- Lines 364-398: `## L1 — per-element procedure` (plane-rotation-stream L1)
- Lines 399-404: `## Open questions` (plane-rotation-stream OQs)
- Lines 405-464: `## L1 — per-element procedure (plane-rotation-stream)` (second L1 entry; appears to be a refinement / second pass of the L1 above, with a scope note explaining the merge)

The file is **structurally two slices in one** — a Gram-Schmidt slice (lines 1-312) and a plane-rotation-stream slice (lines 313-464). Both already have their own scope notes calling out the merge:
- Line 407 (in the second L1 — per-element procedure): "Scope note. This section dissects the **plane-rotation stream** ... It is structurally distinct from the **block Gram-Schmidt orthogonalization** dissected in the earlier sections of this slice ... Open question: split this slice into `orthog/gram_schmidt.md` and `orthog/plane_rotation.md` once both reach L4. Recorded in Open questions."

**Supersession map** (slice section → firm entries that cover it):

- §"Slice: orthog" intro (lines 1-5) → **partially** covered by [`concepts/orthogonalization.md`, `concepts/sequential-obstruction.md` (the worked example "MGS as sequential-obstruction" at lines 37-48 of that file is a direct lift of orthog.md's L3 content)]. The intro names the three-variant family + GMRES/Arnoldi caller surface; both are firm in the concept page.
- §"L0 → L1" (lines 7-105) → **partially** covered by [`concepts/orthogonalization.md` (signature + variants + dispatch site), `L1-L0/ksp-solve-mutation-rotation` §"Sub-pattern C — inner GMRES body" (calls `OrthogonalizeIteration` at iterative.cpp:307-325), `book/src/spec/slices/arnoldi_step.md` (reduced cycle-010; cites `OrthogonalizeIteration` workspace and inner loop)]. **Unique material**:
  - The detailed L1 contract — read-only `V_basis`, mutated `w`, written `H`, routine-owns-reduction `dot_op` — is more granular than `concepts/orthogonalization.md`'s "L1 contract" section (3 lines: heading at :13 + 2-line prose at :14-15; no signature block in the concept page).
  - The variant-absorption table (level-(a)/(b)/(c) per `concepts/variant-absorption.md`) for {algorithm choice, scalar type, weighting} is unique to this slice.
  - The MPI-collective shape disclosure (MGS: m reductions of size 1; CGS: 1 of size m; CGS2: 2 of size m) is also documented in `book/src/spec/slices/arnoldi_step.md` §"MPI-collective shape" (per cycle-010 audit) but is NOT in any firm entry.
  - The parametric test linkage `test/unit/test-orthog.cpp:70-97, :123-160` is unique to this slice (also referenced by `L2/krylov-step.md:170-171` but as test-linkage evidence, not as a unique citation).
- §"L1 → L2" (lines 106-109) → empty placeholder. Stub-eligible.
- §"L2 — primitive composition" (lines 110-176) → **NOT covered** by firm entries. The detailed MGS/CGS/CGS2 L2 unfoldings (per-pass bodies, the `allreduce_sum` primitive, the gemv_basis batched update, the non-fusion-of-CGS2-passes load-bearing claim) are unique to this slice. The firm `L2/krylov-step.md` references `orthogonalization` as a level-(b)-absorbed surface but does not enumerate the MGS/CGS/CGS2 L2 chains.
- §"L3 — global tensor-field form (with sequential obstruction)" (lines 177-244) → **partially** covered by [`concepts/sequential-obstruction.md` §"Example: MGS as sequential-obstruction" (lines 37-48 of that file)]. The concept page's worked example is a direct lift of the structural argument; it cites this slice's L3 section as the source. **Unique material**: the projector-form derivation (`w ← (I − V Vᴴ) w`), the CGS-vs-CGS2 unification at L3 (both are projector applications, differing in pass count), and the block-MGS hybrid pointer (out-of-scope) are unique.
- §"L4 — calculus form" (lines 245-312) → **NOT covered** by firm entries. The `OrthogParams` / `OrthogState` typing, the Solve-monad action `orthogonalize :: OrthogParams -> Solve OrthogState ()`, and the sequential-obstruction-as-monad-shape treatment ("the `get s.w` in iteration `j+1` reads the `s.w` written by iteration `j`'s `modify`") are unique. **This is canonical evidence** for `concepts/state-stratification` and `concepts/solve-monad` applied to a non-Krylov-step Solve-monad action.
- §"Context" + §"Background" (lines 313-335) → **partially** covered by [`concepts/plane-rotation-stream.md` (firm; lines 17-19 cite Saad 2003 §6.5.3 + Paige & Saunders for textbook background)]. The slice's scaled-Givens citation (Bindel/Demmel/Kahan/Marques 2002) is more specific than the firm concept page.
- §"Variant axes" (plane-rotation-stream; lines 336-345) → covered by [`concepts/plane-rotation-stream.md` §"Variants the stream is invariant to" (heading at line 25, content at lines 27-33 of that file)].
- §"L0 — citations" (plane-rotation-stream; lines 346-363) → **partially** covered by [`L1-L0/ksp-solve-mutation-rotation` §"Sub-pattern C" (cites `iterative.cpp:73-120` GeneratePlaneRotation and `:227-250` ApplyPlaneRotation per the polynomial_recurrence_step.md L0 §"GMRES Givens scalar recurrence" cross-reference)]. **Unique material**: the per-step driver decomposition (steps (i)-(iv): replay, generate, apply, propagate-to-RHS) is unique to this slice.
- §"L1 — per-element procedure" (plane-rotation-stream; lines 364-398, near-duplicate of lines 405-464 — the two L1 entries diverge slightly in content; see the next bullet for the precise relation) → covered by [`concepts/plane-rotation-stream.md` §"Shape" (lines 7-13 of that file)]. The slice's procedure body (steps 1-5) maps directly to the concept page's 5-step shape.
- §"L1 — per-element procedure (plane-rotation-stream)" (lines 405-464; the second L1 entry) → **near-duplicate** of the first L1 entry (lines 364-398). The second entry has slightly tighter prose, adds an Invariant subsection, and points at `concepts/givens.md`. **The two L1 entries should be merged** — both describe the same procedure at the same layer.

**Residual gaps** (blockers for full reduction):

1. **Missing firm `L1/orthogonalize`**: the slice references `orthogonalize_column(variant, V[0..m-1], w; dot_op)` as the canonical L1 primitive, but no firm `L1/orthogonalize` operator entry exists. This is the same blocker recorded by cycle-010 OQ `l1-orthogonalize-promotion-from-arnoldi-step-and-orthog`. **Lifting target**: a harvester dispatch on `L1/orthogonalize` (the OQ already routes this). Without it, the slice's L1 Gram-Schmidt content cannot be stubbed beyond cosmetic touches.

2. **The slice is structurally two slices**. The Open questions at line 102, 174, 402-403, and 449-450 all reference the eventual split into `orthog/gram_schmidt.md` + `orthog/plane_rotation.md` once both reach L4 (both have). **Lifting target**: a structural split of the file into two stub-headers pointing at firm entries, with the unique L2/L3/L4 Gram-Schmidt content retained on one stub and the unique plane-rotation-stream L0/L1 content retained on the other stub. This is a refactor that should follow the firm L1/orthogonalize lift.

3. **Missing firm `L2/orthogonalize` or `L2/gemv_basis`**: the slice's L2 unfolding introduces `gemv_basis` (batched coefficient-basis combination) and `allreduce_sum` as L2-level primitives. The firm `L2/krylov-step.md` lists `orthogonalization` as an L2-composition surface (with concept-page link only) and notes at `:38` that an L2 first-class `orthogonalize` operator is a future harvester candidate. **Lifting target**: the same harvester dispatch that promotes L1/orthogonalize should consider whether L2/orthogonalize is also needed (or whether the L1 + concept page is sufficient).

4. **The plane-rotation-stream L0/L1 unique content overlaps `book/src/spec/slices/plane_rotation_stream.md`** (a sibling slice deferred to batch-3 by cycle-010 priority order). **Action**: the plane-rotation-stream content in `orthog.md` lines 313-464 should be audited *jointly* with `plane_rotation_stream.md` in batch-3 to determine the supersession map across the two slices and decide where the canonical home for plane-rotation-stream L0/L1/L2/L3/L4 content lives. Doing the reduction unilaterally here risks creating a stale stub in one slice that points at content that has been moved to the other.

**Recommended action**: **partial-reduction** (with explicit deferral of the plane-rotation-stream sub-slice to batch-3).

- Stub sections that are fully superseded:
  - §"L0 → L1" (lines 7-105) — the L1 contract + Procedure (variant-parametric) + Variant axes table + State/mutation pattern + Caller interface are partially covered by `concepts/orthogonalization.md` and the firm krylov-step chain; the citations + test linkage + Open questions sections contain unique material that should hoist into the stub header's "Open questions still pending lift" subsection. **Action**: stub the L0→L1 section with a header note pointing at `concepts/orthogonalization.md` and `concepts/sequential-obstruction.md` §"MGS as sequential-obstruction"; hoist the unique L1 invariants (read-only `V_basis` / mutated `w` / written `H` / `dot_op` is local + routine owns reduction) and the test linkage into a residual "Open questions pending lift to firm L1/orthogonalize" subsection.
  - §"L1 → L2" (lines 106-109) — empty placeholder; can be removed entirely.
- Retain (pending firm `L1/orthogonalize` + firm `L2/orthogonalize`):
  - §"L2 — primitive composition" (lines 110-176) — the MGS/CGS/CGS2 L2 chains are unique and not in firm entries.
  - §"L3 — global tensor-field form (with sequential obstruction)" (lines 177-244) — the projector-form derivation and CGS/CGS2 L3 unification are unique.
  - §"L4 — calculus form" (lines 245-312) — the `OrthogParams`/`OrthogState` typing and Solve-monad action are unique evidence for state-stratification / solve-monad applied to a non-Krylov-step action.
- **Defer to batch-3** (do not stub or modify in this batch):
  - §"Context" + §"Background" + §"Variant axes" + §"L0 — citations" + §"L1 — per-element procedure" + §"Open questions" + §"L1 — per-element procedure (plane-rotation stream)" (lines 313-464) — audit jointly with `book/src/spec/slices/plane_rotation_stream.md` in batch-3.
- Add a header note: "This slice is the cycle-001-era precursor to the firm `concepts/orthogonalization.md` + `concepts/sequential-obstruction.md` §'MGS as sequential-obstruction' + the firm krylov-step chain's level-(b) orthogonalization-variant absorption. The L2/L3/L4 Gram-Schmidt sections are retained pending lift to firm `L1/orthogonalize` and `L2/orthogonalize` (OQ `l1-orthogonalize-promotion-from-arnoldi-step-and-orthog`). The plane-rotation-stream sub-slice (lines 313-464) overlaps `book/src/spec/slices/plane_rotation_stream.md` and is deferred to batch-3 for joint audit."

### Slice 2: `book/src/spec/slices/chebyshev.md` (442 lines)

**Audit verdict**: partial-reduction (full-reduction blocked by the absence of a firm `L1/chebyshev-smoother` or `L2/chebyshev-iteration` operator entry — the slice's L1/L2/L3/L4 content is currently the **only** firm Chebyshev definition in the artifact).

**Structure** (per `grep -n "^## \|^# "`):
- Line 1: `# Slice: chebyshev` (intro, lines 1-20: scope + variant description)
- Lines 21-87: `## L1` (state + setup + apply procedure)
- Lines 89-96: `## Consumers` (consumer list: gmg.cpp, distrelaxation.cpp)
- Lines 98-111: `## Open questions` (no direct unit test; spectrum-estimate backends; MPI; dead transpose code)
- Lines 113-123: `## Concept references` (apply_linop, axpy, elementwise-product, etc.)
- Lines 125-230: `## L2 — primitive composition` (setup primitives + apply primitives + variant absorption + numerical-claim preservation)
- Lines 232-288: `## L3 — tensor-field form (partial obstruction)` (body-lifts-loop-doesn't sequential obstruction)
- Lines 290-442: `## L4 — calculus form` (state stratification + apply as monadic action + setup as separate monadic action + capability-typed sim state + initial-guess shape)

**Supersession map** (slice section → firm entries that cover it):

- §intro (lines 1-20) → **partially** covered by [`concepts/chebyshev-iteration.md` (high-level prose overview; lines 1-7 describe `T_k` minimax + interval), `L2/krylov-step.md` §Evidence (cites `chebyshev.md:354-362` as one of five canonical L4 worked examples), `L4/krylov-step.md` §Variant axes (the single `## Variant axes` section at line 135 with a 6-item list; the polynomial-kind axis is list-item 3 at line 141 — {4th, 1st}, absorbed at level (c) into `op.scalars`)]. **Unique material**: the slice's variant description (4th-kind requires only `lambda_max`; 1st-kind requires `[lambda_min, lambda_max]`) is more concrete than the concept page; the constructed-operator absorption is the same posture as `L4/krylov-step` Form A's `op.scalars`.
- §"L1" (lines 21-87) → **NOT covered** by firm entries. The L1 state schema (`A`, `dinv`, variant-specific persisted scalars, `order`, `pc_it`) + Setup procedure (purity of `(A, sf_max[, sf_min], order, pc_it, variant)`) + Apply procedure (Richardson sweep with polynomial recurrence) are the **only** firm Chebyshev L1 definition in the artifact. There is no `L1/chebyshev-smoother` entry; the `concepts/chebyshev-iteration.md` page is high-level prose, not an operator entry.
- §"Consumers" (lines 89-96) → **partially** covered by [the slice corpus' `cg_preconditioning_framework.md` (cited at `L1/ksp_solve` §Evidence; deferred to batch-4 by cycle-010 priority order)]. The slice's consumer mention of `gmg.cpp` (geometric multigrid) and `distrelaxation.cpp` (distributive relaxation) is unique pending an L2/L3 multigrid slice landing.
- §"Open questions" (lines 98-111) → **partially** lifted. OQ "No direct unit test under `test/unit/`" survives as a documentation note. OQ "`spectrum_estimate` build-flag-dependent backend" survives. OQ "complex `Transpose=true` dead code" is in scope for future harvester work on `apply_linop` complex specializations. The MPI scope is closed (out of scope per CLAUDE.md).
- §"Concept references" (lines 113-123) → **fully** covered by firm concept-page entries (`concepts/apply_linop.md`, `concepts/axpy.md`, `concepts/elementwise-product.md`, etc.). The references list is redundant with the firm concept index at `book/src/concepts/index.md`.
- §"L2 — primitive composition" (lines 125-230) → **NOT covered** by firm entries. The L2 setup primitives (`extract_diagonal → reciprocal → spectrum_estimate`), the apply primitives table (`copy`, `zero`, `apply_linop`, `axpy`, `elementwise_product`, `scal`), the `scalars(op, k)` variant-dependent scalar-generator (both 4th-kind closed-form and 1st-kind three-term recurrence over `rho_k`), and the variant-absorption-at-L2 treatment are unique. This is the canonical L2 Chebyshev evidence cited by `L2/krylov-step.md:140` and `L2/krylov-step.md:142` (the polynomial-recurrence pattern instance).
- §"L3 — tensor-field form (partial obstruction)" (lines 232-288) → **partially** covered by [`L3/krylov-step.md` (cycle-010 wave-1; references the polynomial-recurrence pattern at variant axis (3)), `concepts/sequential-obstruction.md` (the `k` and `pc_it` loops are both classified as sequential-obstructions; the slice cites this concept directly)]. **Unique material**: the body-lifts-loop-doesn't tabulation (the "What lifts vs. what does not" table at lines 270-277), the scalar-recurrence side note for 1st-kind `rho_k`, and the Phillips & Fischer §2 citation justifying the non-removability of the sequentiality are unique.
- §"L4 — calculus form" (lines 290-442) → **partially** covered by [`L4/krylov-step.md` Form A + Form B (variant axis 3, polynomial-kind), `concepts/state-stratification.md`, `concepts/solve-monad.md`, `concepts/derived-view-hoisting.md` (cited for the initial-guess shape as control-flow boundary), `concepts/constructed-operators.md`]. **Unique material**:
  - The `ChebOp<E, S>` parameterized closure type (`Kind4 :: ChebOp<E, Unit>`, `Kind1 :: ChebOp<E, { rho_prev: E }>`) — the scalar-recurrence stratum encoded as a type parameter — is unique evidence for the "constructed-operator absorbs variant at level (c)" pattern. The L4/krylov-step entry references variant axis 3 but does not enumerate the type-parameter encoding of the scalar-state stratum.
  - The four-way state stratification (sim / operator-internal / ephemeral / scalar-recurrence) is one stratum more than `concepts/state-stratification.md`'s three-stratum split — the scalar-recurrence stratum is per-call ephemeral but threaded across `k`-iterations. This is canonical evidence for a state-stratification refinement.
  - The `initial-guess shape: branch vs. derived view` section (lines 419-436) is unique evidence for `concepts/derived-view-hoisting.md` applied at the control-flow boundary (rather than the state-shape boundary) — the slice argues why `initial_guess: Bool` is a per-call argument rather than a constructed-operator variant axis. This is canonical methodology evidence.
  - The capability-typed `ChebSim<E> = { x: Read<Field<E>>; y: ReadWrite<Field<E>> }` is referenced from `L4/krylov-step.md` indirectly (via `concepts/solve-monad.md`), but the explicit Read/ReadWrite split for Chebyshev's per-level rhs/correction pair is unique evidence.

**Residual gaps** (blockers for full reduction):

1. **No firm `L1/chebyshev-smoother` operator entry**. The slice's L1 section is the only firm Chebyshev L1 definition in the artifact. **Lifting target**: a harvester dispatch on `L1/chebyshev-smoother`. The operator-internal-state stratum (constructed-operator absorbs variant at level (c) per cycle-005 firm `L2/krylov-step` variant axis (3)) makes this a natural promotion candidate — the operator is small (Richardson sweep over polynomial recurrence) AND it would simplify the higher forms (the `L2/krylov-step` polynomial-recurrence pattern instance would gain a concrete L1 operator to fold over).

2. **No firm `L2/chebyshev-iteration` operator entry**. The slice's L2 section names the Chebyshev variant of the krylov-step polynomial-recurrence pattern; `L2/krylov-step` cites this slice but does not enumerate the Chebyshev-specific L2 primitive composition. **Lifting target**: harvester dispatch on `L2/chebyshev-iteration` (or the slice's L2 section is sufficient evidence + the `concepts/chebyshev-iteration.md` page is upgraded to enumerate the L2 primitive composition). Promotion criterion: simplifies higher forms — yes, would let the `L2/krylov-step` variant axis (3) point at a concrete L2 entry.

3. **The four-stratum state-stratification finding is unique methodology evidence.** The slice's L4 section establishes that Chebyshev requires a fourth stratum (scalar-recurrence) beyond the three (sim/operator-internal/ephemeral) documented in `concepts/state-stratification.md`. **Lifting target**: extend `concepts/state-stratification.md` with a worked example showing the four-stratum split, OR document the scalar-recurrence stratum as a sub-kind of the operator-internal stratum (the slice's framing) with the per-call-ephemeral-but-threaded distinction made explicit.

4. **The initial-guess-as-derived-view-hoisting-at-control-flow-boundary finding is unique methodology evidence.** **Lifting target**: extend `concepts/derived-view-hoisting.md` with a worked example showing the control-flow-boundary application (as distinct from the state-shape-boundary application that's the typical case for derived-view-hoisting).

**Recommended action**: **partial-reduction**.

- Stub sections that are fully superseded:
  - §"Consumers" (lines 89-96) — content is a 2-line consumer list with no unique material beyond the file names; the slice corpus `cg_preconditioning_framework.md` + `divfree.md` (both deferred to later batches) will cover the consumer pattern when audited. Replace with a one-line pointer.
  - §"Concept references" (lines 113-123) — redundant with `book/src/concepts/index.md`; remove entirely.
- Retain (pending firm `L1/chebyshev-smoother` and `L2/chebyshev-iteration`):
  - §"L1" (lines 21-87) — the only firm Chebyshev L1 definition.
  - §"L2 — primitive composition" (lines 125-230) — the only firm Chebyshev L2 primitive composition.
  - §"L3 — tensor-field form (partial obstruction)" (lines 232-288) — unique partial-obstruction worked example.
  - §"L4 — calculus form" (lines 290-442) — unique four-stratum state-stratification + initial-guess-as-derived-view-hoisting evidence.
- Retain partially:
  - §"Open questions" (lines 98-111) — keep "no direct unit test" and "spectrum-estimate build-flag-dependent backend" + "dead transpose code" notes; remove the MPI-scope note (out of scope per CLAUDE.md; redundant).
- Add a header note: "This slice is the cycle-001-era precursor to a firm `L1/chebyshev-smoother` + `L2/chebyshev-iteration` row that has not yet been promoted. The slice's L1/L2/L3/L4 content is currently cited as canonical evidence by `book/src/L2/krylov-step.md:140` (the polynomial-recurrence pattern instance), `book/src/L4/krylov-step.md` §Variant axes list-item 3 (polynomial-kind at line 141), and `book/src/concepts/chebyshev-iteration.md` (high-level prose overview). The slice is retained in full pending lift to firm L1/L2 entries (OQ to be filed for batch-2)."

### Slice 3: `book/src/spec/slices/polynomial_recurrence_step.md` (204 lines)

**Audit verdict**: blocked / minimal reduction (the slice is explicitly a **negative-result slice** per `concepts/negative-result-slice.md` and is cited as the canonical worked example at `concepts/negative-result-slice.md:46`; its load-bearing content is structurally not subject to reduction).

**Structure** (per `grep -n "^## \|^# "`):
- Line 1: `# Polynomial recurrence step` (H1)
- Lines 3-7: `## Context` (negative-result framing)
- Lines 9-13: `## Background` (textbook vs source-side framing)
- Lines 15-60: `## L0` (Chebyshev fused-update helpers + scalar-coefficient sequences + outer driver + GMRES Givens scalar recurrence + LOBPCG/eigenvalue tracking obstruction)
- Lines 62-160: `## L1 — distinction catalog` (falsification criterion + distinguishing-features table + catalog + shared surface + non-shared surface + procedure)
- Lines 162-191: `## L1 ↔ L1 self-tightening — chebyshev-internal partial unification` (the within-Chebyshev partial-positive)
- Lines 193-198: `## Open questions`
- Lines 199-204: `## See also` (cross-references to firm concept entries)

**Supersession map** (slice section → firm entries that cover it):

- §"Context" (lines 3-7) → **NOT covered** by firm entries. The negative-result framing ("structured record of three independent per-step scalar-update sequences and one out-of-scope") is the slice's load-bearing claim. **The slice itself is cited at `concepts/negative-result-slice.md:46` as the canonical worked example** — this is unique methodology evidence.
- §"Background" (lines 9-13) → **NOT covered** by firm entries. The textbook-vs-source-side framing (Saad ch. 12, Phillips & Fischer 2022 §3, Saad ch. 6.5) and the explicit "Palace does not realize that shape" statement are unique.
- §"L0" subsections (lines 15-60):
  - §"L0 — Chebyshev fused-update helpers" (lines 17-24) → **partially** covered by [the firm `chebyshev.md` slice's L1/L2 sections (which describe the `ApplyOrder0`/`ApplyOrderK` helpers via the `apply_linop` + `axpy` + `elementwise_product` + `scal` primitive table; the firm `L2/krylov-step.md:142` cites `polynomial_recurrence_step.md:119-160` directly)]. **Unique material**: the explicit file-local-translation-unit-private framing ("Both helpers are `static` in an anonymous namespace, not exported") is unique evidence for the in-source non-unification.
  - §"L0 — Chebyshev scalar-coefficient sequences" (lines 26-33) → **partially** covered by [the firm `chebyshev.md` slice's L2 §"Apply primitives" `scalars(op, k)` generator (which enumerates both 4th-kind closed-form and 1st-kind `rho_k` recurrence)]. **Unique material**: the explicit per-variant `Mult2` line-range citation pair (chebyshev.cpp:191-220 for 4th, :261-293 for 1st) is unique.
  - §"L0 — Chebyshev outer driver" (lines 35-39) → **NOT covered**. The duplicated-95%-identical-`Mult2`-bodies claim with the explicit chebyshev.cpp:230-258 citation and the "no `PolynomialSmoother` intermediate base class" finding is unique.
  - §"L0 — GMRES Givens scalar recurrence" (lines 41-51) → **partially** covered by [`concepts/plane-rotation-stream.md` §"Shape" (the per-step driver shape: replay-stored, generate-new, apply-new, propagate-to-RHS), `concepts/givens.md`, `concepts/givens_generate.md`, `concepts/givens_apply.md`]. **Unique material**: the explicit framing of GMRES-Givens as a "fundamentally different state shape" from Chebyshev (not a polynomial recurrence at all) is the load-bearing cross-family non-unification claim.
  - §"L0 — LOBPCG / eigenvalue tracking" (lines 53-60) → **NOT covered**. The Palace-boundary-obstruction framing (SLEPc/ARPACK delegate the scalar-update sequence to below the Palace boundary) is unique evidence for `concepts/sequential-obstruction.md` §"Sub-kind: out-of-scope-obstruction".
- §"L1 — distinction catalog" (lines 62-160):
  - §"Falsification criterion" (lines 66-75) → **NOT covered**. **This is the load-bearing structural element** required by `concepts/negative-result-slice.md` §"Falsification criterion (required structural element)" (lines 48-59 of that file). The 4-item enumeration is unique and structurally required.
  - §"Distinguishing features" (lines 77-91) → **NOT covered**. The five-axis non-unification table (scalar-state cardinality, scalar recurrence kind, persisted derived state, vector-update shape, termination shape) is the load-bearing cross-family-distinction-catalog evidence. Unique.
  - §"Catalog" (lines 93-100) → **NOT covered**. The four-row catalog (Chebyshev-4th, Chebyshev-1st, GMRES Givens stream, eigenvalue tracking) with per-site state/scalar-update/vector-update enumeration is the slice's L1 result. Unique.
  - §"Shared surface" (lines 102-104) → **NOT covered**. The `ApplyOrder0`/`ApplyOrderK` file-local-only-shared-surface finding is unique.
  - §"Non-shared surface" (lines 106-111) → **NOT covered**. The four-item non-shared-surface list is unique.
  - §"Procedure (abstract; the slice's L1 statement)" (lines 113-160) → **NOT covered**. The four-site site-by-site procedure listing IS the slice's L1 statement; reducing it would erase the artifact.
- §"L1 ↔ L1 self-tightening — chebyshev-internal partial unification" (lines 162-191) → **NOT covered**. The within-Chebyshev partial-positive (4-of-5-axes-shared between 4th-kind and 1st-kind; refactor potential as `ChebyshevSmootherBase<ScalarGenerator>`) is unique methodology evidence for the **partial-positive-within-a-negative-result-slice** pattern. The dedicated falsification criterion subsection (lines 183-191) is also structurally required.
- §"Open questions" (lines 193-198) → **partially** lifted. OQ 1 ("spec-side unification") is resolved within the slice itself (NO at cross-family scope; DEFER at within-Chebyshev scope). OQ 2 ("refactor potential within Chebyshev") is structurally documented in the self-tightening section. OQ 3 ("`ApplyOrderK<Transpose=true>` liveness") survives as a dead-code candidate observation; this is also flagged in `chebyshev.md` Open questions.
- §"See also" (lines 199-204) → **partially** redundant with `concepts/negative-result-slice.md` §"Examples in this spec" (which cites this slice as the canonical example) and `concepts/sequential-obstruction.md` (cited as the sister pattern). The cross-references are useful navigation aids.

**Residual gaps** (blockers for any further reduction):

1. **The slice IS a methodological artifact, not a precursor.** Negative-result slices preserve the distinction catalog AS the result. Per `concepts/negative-result-slice.md:9-12`, the slice's value is in three structural roles: (a) prevents future cycles from re-asking the question, (b) prevents the spec from inventing fictional kernels, (c) right output shape when the source has obstructions or genuine independence. Reducing the slice beyond cosmetic stubbing would erase the artifact's methodological role.

2. **The slice is cited as the canonical worked example for `concepts/negative-result-slice.md`** (at `concepts/negative-result-slice.md:46`). Reducing the slice would break the concept page's worked-example anchor.

3. **The falsification criteria (both at lines 66-75 and lines 183-191) are structurally required** per `concepts/negative-result-slice.md` §"Falsification criterion (required structural element)". Removing them would violate the negative-result-slice contract.

4. **The within-Chebyshev partial-positive (§L1↔L1 self-tightening)** is unique methodology evidence for the "partial-positive-within-a-negative-result-slice" pattern. This is NOT documented in any firm concept page. **Lifting target**: extend `concepts/negative-result-slice.md` with a "Partial-positive sub-pattern" subsection citing this slice's self-tightening section as the canonical worked example. If lifted, the slice's self-tightening section could be stubbed; until then, it stays.

**Recommended action**: **blocked / minimal reduction**.

- Stub sections that are partially superseded (very narrow scope):
  - §"L0 — Chebyshev fused-update helpers" (lines 17-24) — can add a forward-pointer to `book/src/spec/slices/chebyshev.md` §L2 §"Apply primitives" without removing the unique anonymous-namespace framing. This is a 1-line note, not a stub.
  - §"L0 — Chebyshev scalar-coefficient sequences" (lines 26-33) — same as above: 1-line forward-pointer to `chebyshev.md` §L2 §"Apply primitives" + `scalars(op, k)` generator without removing the per-variant line-range citation pair.
- Retain (in full, verbatim):
  - §"Context", §"Background", §"L0 — Chebyshev outer driver", §"L0 — GMRES Givens scalar recurrence", §"L0 — LOBPCG / eigenvalue tracking", entire §"L1 — distinction catalog" (including the four sub-sections), entire §"L1 ↔ L1 self-tightening" (including the falsification criterion subsection), §"Open questions" (OQ 3 only — `Transpose=true` dead code), §"See also".
- Add a header note at line 2 (after the H1 line): "This slice is a **negative-result slice** per `book/src/concepts/negative-result-slice.md`. It is cited as the canonical worked example at `concepts/negative-result-slice.md:46`. The slice's distinction catalog IS the result; it is structurally not subject to reduction beyond narrow forward-pointers in the L0 fused-update-helpers and scalar-coefficient sub-sections that overlap firm `book/src/spec/slices/chebyshev.md` §L2 evidence. The within-Chebyshev partial-positive (§L1↔L1 self-tightening) is pending lift to `concepts/negative-result-slice.md` as a 'Partial-positive sub-pattern' subsection."

## Recommendation

**Dispatch a triplet of integrator-per-report applications** that materialize the three slices' partial reductions per the audit verdicts above. The action profile for batch-2 is materially different from batch-1:

- `orthog.md`: partial-reduction with explicit deferral of the plane-rotation-stream sub-slice to batch-3 (joint audit with `plane_rotation_stream.md`).
- `chebyshev.md`: partial-reduction — stub §Consumers + §"Concept references"; retain L1/L2/L3/L4 + §"Open questions" (trimmed) pending firm L1/L2 Chebyshev row lift.
- `polynomial_recurrence_step.md`: blocked / minimal reduction (narrow forward-pointers only); the slice is a methodological artifact and is structurally retained.

Subsequent dispatches should handle the residual lift work surfaced as new OQs:
1. Continue routing the cycle-010 OQ `l1-orthogonalize-promotion-from-arnoldi-step-and-orthog` — now affects 2 slices.
2. New: route firm `L1/chebyshev-smoother` + `L2/chebyshev-iteration` lift (blocks `chebyshev.md` reduction).
3. New: extend `concepts/state-stratification.md` with the four-stratum worked example from `chebyshev.md` §L4.
4. New: extend `concepts/derived-view-hoisting.md` with the control-flow-boundary worked example from `chebyshev.md` §L4 "Initial-guess shape" section.
5. New: extend `concepts/negative-result-slice.md` with a "Partial-positive sub-pattern" subsection citing `polynomial_recurrence_step.md` §L1↔L1 self-tightening.

Concretely, the proposed integrator actions per slice are encoded as proposed_changes blocks below.

## Proposed changes

### Proposed change 1: Partial reduction of `book/src/spec/slices/orthog.md`

```edit:book/src/spec/slices/orthog.md
[Replace lines 7-109 (the §"L0 → L1" Gram-Schmidt L1 form section + the §"L1 → L2" empty placeholder section) with a stub header that points at firm entries; retain lines 110-312 (§L2 + §L3 + §L4 Gram-Schmidt) and lines 313-464 (the plane-rotation-stream sub-slice; deferred to batch-3) verbatim. The lines-1-6 H1 + intro paragraph is retained.

The stub header text replacing lines 7-109 (which currently contains the §"L0 → L1" with the L1 form + citations + test linkage + Open questions + the §"L1 → L2" empty placeholder):

## L0 → L1 (reduced)

The Gram-Schmidt L1 form has been partially lifted into the firm artifact:

- `book/src/concepts/orthogonalization.md` — the L1 contract: `orthogonalize(gs_orthog, V[0..j], w) → (w', h)` dispatching on `gs_orthog ∈ {MGS, CGS, CGS2}` exactly once. The variant axis is named here; the level-(b) variant absorption is the slice's pattern.
- `book/src/concepts/sequential-obstruction.md` §"Example: MGS as sequential-obstruction" (lines 37-48 of that file) — the structural argument for MGS's L3 non-liftability is lifted verbatim from this slice's L3 section.
- `book/src/L2/krylov-step.md` references `orthogonalization` as a level-(b)-absorbed L2-composition surface (per `L2/krylov-step.md:38` future harvester candidate); the slice's L1 invariants (read-only `V_basis` / mutated `w` / written `H` / `dot_op` is local + routine owns reduction) and the MPI-collective shape disclosure (MGS: m reductions of size 1; CGS: 1 of size m; CGS2: 2 of size m) are NOT in firm entries.
- `book/src/L1-L0/ksp-solve-mutation-rotation.md` §"Sub-pattern C — inner GMRES body" cites `OrthogonalizeIteration` at `iterative.cpp:307-325` as the dispatch site.

**Pending lift to firm `L1/orthogonalize` operator entry** (OQ `l1-orthogonalize-promotion-from-arnoldi-step-and-orthog` at `scaffolding/open-questions.md:1804`): the unique L1 invariants and the MPI-collective shape are retained in the L2/L3/L4 sections below pending a firm L1 row.

**Citations and test linkage retained** in the L2/L3/L4 sections (the unique parametric test coverage of all three variants at `test/unit/test-orthog.cpp:70-97, :123-160` is also cited by `L2/krylov-step.md:170-171`).

---

(L2 — primitive composition, starting here, retained verbatim from the original slice...)
]
```

### Proposed change 2: Partial reduction of `book/src/spec/slices/chebyshev.md`

```edit:book/src/spec/slices/chebyshev.md
[Replace lines 89-96 (§"Consumers") + lines 113-123 (§"Concept references") with stub pointers; trim §"Open questions" (lines 98-111) to retain only the unit-test and spectrum-estimate-backend and dead-transpose-code observations (removing the MPI scope note); retain all other sections verbatim. Add a header note at line 2 (after the H1) pointing at firm entries.

Header note inserted at line 2 (after `# Slice: chebyshev`):

> **Reduction status (cycle-011+):** this slice is the cycle-001-era precursor to a firm `L1/chebyshev-smoother` + `L2/chebyshev-iteration` row that has not yet been promoted. The slice's L1/L2/L3/L4 content is currently cited as canonical evidence by:
> - `book/src/L2/krylov-step.md:140` (`chebyshev.md:354-362` cited as one of five canonical L4 slice instances).
> - `book/src/L2/krylov-step.md:142` (the polynomial-recurrence pattern instance).
> - `book/src/L3-L2/krylov-step-body-identity.md:127` (the L3>L2 identity-in-form claim's Chebyshev evidence).
> - `book/src/L4/krylov-step.md` §Variant axes list-item 3 (polynomial-kind at line 141, absorbed at level (c) into `op.scalars`).
> - `book/src/concepts/chebyshev-iteration.md` (high-level prose overview; not an operator entry).
>
> **Pending lift to firm entries**:
> - `L1/chebyshev-smoother` — promotes the L1 Apply procedure to a firm L1 operator (criterion: small AND simplifies higher forms; both plausibly met).
> - `L2/chebyshev-iteration` — promotes the L2 primitive composition to a firm L2 operator (would let `L2/krylov-step` variant axis (3) point at a concrete L2 entry).
> - Extend `concepts/state-stratification.md` with the four-stratum worked example from §L4 (sim / operator-internal / ephemeral / scalar-recurrence).
> - Extend `concepts/derived-view-hoisting.md` with the control-flow-boundary worked example from §L4 "Initial-guess shape: branch vs. derived view".

The replacement for lines 89-96 §"Consumers":

## Consumers

Multigrid V-cycle smoother (`gmg.cpp`) and distributive relaxation (`distrelaxation.cpp`); pending audit when the multigrid + cg-preconditioning slices are reduced in later batches.

The replacement for lines 113-123 §"Concept references":

(REMOVED — concept references are now navigable via `book/src/concepts/index.md`.)

Trim of §"Open questions" (lines 98-111) — retain lines 100-101 (no direct unit test), lines 102-103 (spectrum_estimate backend), lines 107-111 (dead transpose code); remove lines 104-106 (MPI involvement note; out of scope per CLAUDE.md):

## Open questions

- No direct unit test under `test/unit/`; behavior exercised through multigrid integration only.
- `spectrum_estimate` has a build-flag-dependent backend (power iteration vs. SLEPc); L2 unfold will need to acknowledge both.
- The complex `Transpose=true` template specializations of the inner kernels exist but are unreachable: `MultTranspose` forwards to `Mult` under the symmetry assumption, so the transpose-conjugate paths are dead code under current wiring. Flagged for future cleanup or for use by an asymmetric variant.
]
```

### Proposed change 3: Minimal narrow forward-pointer additions to `book/src/spec/slices/polynomial_recurrence_step.md`

```edit:book/src/spec/slices/polynomial_recurrence_step.md
[Retain the entire slice verbatim. Add a header note at line 2 (after the H1) explicitly recording the negative-result-slice status; add two narrow 1-line forward-pointers in the §"L0 — Chebyshev fused-update helpers" and §"L0 — Chebyshev scalar-coefficient sequences" sub-sections pointing at the chebyshev.md slice (which itself is partially-reduced and retains the unique evidence). No content is removed.

Header note inserted at line 2 (after `# Polynomial recurrence step`):

> **Reduction status (cycle-011+):** this slice is a **negative-result slice** per `book/src/concepts/negative-result-slice.md`. It is cited as the canonical worked example at `concepts/negative-result-slice.md:46`. The slice's distinction catalog (§L1) and the within-Chebyshev partial-positive (§L1↔L1 self-tightening) are load-bearing methodology artifacts and are structurally retained in full.
>
> **Pending lift**: extend `concepts/negative-result-slice.md` with a "Partial-positive sub-pattern" subsection citing §L1↔L1 self-tightening as the canonical worked example. Until lifted, this slice is retained verbatim.

Forward-pointer added after line 22 (the end of the `ApplyOrder0` / `ApplyOrderK` enumeration in §"L0 — Chebyshev fused-update helpers"):

> Forward-pointer: the file-local `ApplyOrder0` / `ApplyOrderK` helpers are also enumerated as the canonical Chebyshev L2 primitive composition at `book/src/spec/slices/chebyshev.md` §L2 §"Apply primitives" (in the per-call apply procedure). The anonymous-namespace / translation-unit-private framing here is unique to this slice (and is load-bearing evidence for the non-promotion to a shared kernel).

Forward-pointer added after line 32 (the end of the 4th-kind / 1st-kind scalar-recurrence enumeration in §"L0 — Chebyshev scalar-coefficient sequences"):

> Forward-pointer: the per-variant scalar-coefficient sequences are also enumerated as the canonical Chebyshev `scalars(op, k)` generator at `book/src/spec/slices/chebyshev.md` §L2 §"Apply primitives" (which factors both the 4th-kind closed-form and the 1st-kind `rho_k` three-term recurrence). The "no shared scalar generator is factored out" framing here is unique to this slice.
]
```

## Supporting evidence

- `book/src/spec/slices/orthog.md` (464 lines; read in full). The Gram-Schmidt L1 section (lines 7-105) is partially superseded by `concepts/orthogonalization.md` + `concepts/sequential-obstruction.md` §"MGS as sequential-obstruction"; the L2/L3/L4 sections (lines 110-312) are unique evidence; the plane-rotation-stream sub-slice (lines 313-464) overlaps `plane_rotation_stream.md` and is deferred to batch-3.
- `book/src/spec/slices/chebyshev.md` (442 lines; read in full). The L1/L2/L3/L4 sections are the **only** firm Chebyshev definition in the artifact; the slice is cited by `L2/krylov-step.md:140` and `L3-L2/krylov-step-body-identity.md:127` as canonical evidence.
- `book/src/spec/slices/polynomial_recurrence_step.md` (204 lines; read in full). Explicitly a negative-result slice per `concepts/negative-result-slice.md:46`; the distinction catalog is the result.
- `book/src/L2/krylov-step.md` (172 lines; read in full). Cites all three slices: Chebyshev at `:7, :140, :142`; polynomial_recurrence_step at `:7, :142`; orthog/MGS/CGS/CGS2 via `concepts/orthogonalization.md` at `:11, :97`.
- `book/src/L4/krylov-step.md` (177 lines; read in full). §Variant axes list-item 3 (polynomial-kind at line 141) absorbs the Chebyshev variant.
- `book/src/L3-L2/krylov-step-body-identity.md` (cycle-009 firm; lines 99 + 127 cite both chebyshev.md and polynomial-kind absorption).
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (cycle-008 firm; line 87 cites polynomial-kind variant axis).
- `book/src/concepts/orthogonalization.md` (63 lines; read in full). L1 contract is firm; the slice's L1 invariants are more granular.
- `book/src/concepts/plane-rotation-stream.md` (39 lines; read in full). Cites both `orthog.md` (as primary dissection at line 38) and `gmres.md` (as consumer at line 39); the firm concept page is the canonical home of the plane-rotation-stream shape.
- `book/src/concepts/sequential-obstruction.md` (113 lines; read in full). The "Example: MGS as sequential-obstruction" subsection (lines 37-48) is a direct lift of `orthog.md` §L3; the "Worked example: Givens-stream replay-prefix" (lines 83-112) cites `plane_rotation_stream.md`.
- `book/src/concepts/chebyshev-iteration.md` (35 lines; read in full). High-level prose overview; not an operator entry.
- `book/src/concepts/negative-result-slice.md` (60 lines; read in full). Cites `polynomial_recurrence_step.md` at line 46 as the canonical worked example; §"Falsification criterion (required structural element)" (lines 48-59) is the structural requirement that the slice satisfies.
- `book/src/concepts/givens.md` (59 lines; read in full). The slice's §L0/L1/L2 plane-rotation content is consistent with this concept page; the firm `concepts/plane-rotation-stream.md` is the higher-level stream pattern; the slice's plane-rotation-stream content is the more detailed dissection.
- `book/src/concepts/dependency-map.md` (lines 77-79, 98, 179-181, 186-188 read). Cites `polynomial-recurrence-step` as `:::planned`; cites `polynomial_recurrence_step → negative-result-slice / elementwise-product / givens` in the slice-corpus L0 map; cites `orthog → plane-rotation-stream` and `plane-rotation-stream → givens_generate / givens_apply`.
- `scaffolding/open-questions.md` (lines 1804 + 1816 read). Cycle-010 audit OQs route the `L1/orthogonalize` promotion and the remaining-7-slices priority order.
- `reports/2026-05-27T220000Z-same-layer-cross-cutter-phase-1-corpus-reduction-audit/CYCLE.md` (252 lines; read in full). The cycle-010 first-instance audit template; this batch follows it directly.
- `CLAUDE.md` §Methodology invariants ("Phase 1 corpus reduces as material is lifted", added cycle-009 meta-batch-1).
- `scaffolding/priorities.md` #19 (`phase-1-corpus-reduction-audit`).

## Open questions / caveats

1. **The plane-rotation-stream sub-slice (lines 313-464) of `orthog.md` overlaps `book/src/spec/slices/plane_rotation_stream.md`** (deferred to batch-3 by cycle-010 priority order). The proposed_changes for `orthog.md` (proposed change 1) explicitly defer the plane-rotation-stream content to a joint batch-3 audit with `plane_rotation_stream.md`. **Recommendation**: when batch-3 cycle audits `plane_rotation_stream.md`, audit it jointly with `orthog.md` lines 313-464; decide where the canonical home for plane-rotation-stream L0/L1/L2/L3/L4 content lives. The slice corpus' Open questions already records the eventual structural split (`orthog/gram_schmidt.md` + `orthog/plane_rotation.md`) at `orthog.md:407` + `:449-450`.

   **OQ to add to `scaffolding/open-questions.md`**: "The plane-rotation-stream sub-slice in `book/src/spec/slices/orthog.md` lines 313-464 overlaps `book/src/spec/slices/plane_rotation_stream.md` (deferred to batch-3 of the phase-1-corpus-reduction-audit). Both slices have unique material; the eventual structural split into `orthog/gram_schmidt.md` + `orthog/plane_rotation.md` is flagged in the slice corpus' Open questions but pending. Batch-3 of the audit should perform the joint reduction. Source: cycle-011 phase-1-corpus-reduction-batch-2 §"Open questions" item 1."

2. **The `L1/orthogonalize` promotion** is now blocking 2 slices (arnoldi_step.md from cycle-010; orthog.md from this batch) and is referenced by 5 firm entries (`concepts/orthogonalization.md`, `L2/krylov-step.md`, `L3/krylov-step.md`, `L4/krylov-step.md`, `L1-L0/ksp-solve-mutation-rotation.md`). This is a high-priority promotion candidate; OQ `l1-orthogonalize-promotion-from-arnoldi-step-and-orthog` at `scaffolding/open-questions.md:1804` should be routed for batch-2-or-3 harvester dispatch.

   **OQ update recommendation**: amend the existing OQ entry to record the now-2-slice-blocker status and the 5-firm-entry citation count, raising its priority weight.

3. **The `L1/chebyshev-smoother` + `L2/chebyshev-iteration` firm row promotion** is blocking `chebyshev.md` reduction. The slice's L1/L2 sections are currently the only firm Chebyshev definition; without promotion, `chebyshev.md` cannot be reduced beyond the cosmetic stubbing proposed here.

   **OQ to add**: "A firm `L1/chebyshev-smoother` operator entry (and possibly `L2/chebyshev-iteration`) is pending lift. The slice corpus' `book/src/spec/slices/chebyshev.md` §L1 and §L2 are currently the only firm Chebyshev definition in the artifact; they are cited as canonical evidence by `L2/krylov-step.md:140, :142` and `L4/krylov-step.md` §Variant axes list-item 3 (polynomial-kind at line 141). Promotion criterion: small AND simplifies higher forms — both plausibly met (the operator is a Richardson sweep over polynomial recurrence; lifting would let `L2/krylov-step` variant axis (3) point at a concrete L2 row). Source: cycle-011 phase-1-corpus-reduction-batch-2 §slice-2 residual gaps #1-2."

4. **The four-stratum state-stratification finding in `chebyshev.md` §L4** (sim / operator-internal / ephemeral / scalar-recurrence) is unique methodology evidence — `concepts/state-stratification.md` documents three strata only. **Lifting target**: extend the concept page with the four-stratum worked example, OR document the scalar-recurrence stratum as a sub-kind of operator-internal with the per-call-ephemeral-but-threaded distinction made explicit.

   **OQ to add**: "The `chebyshev.md` §L4 establishes a fourth state stratum (scalar-recurrence — per-call ephemeral but threaded across `k`-iterations) beyond the three documented in `concepts/state-stratification.md`. Should this be lifted as a firm extension to the state-stratification concept (four-stratum split), OR as a sub-kind of operator-internal stratum (the slice's framing)? Source: cycle-011 phase-1-corpus-reduction-batch-2 §slice-2 residual gap #3."

5. **The control-flow-boundary application of `derived-view-hoisting`** in `chebyshev.md` §L4 "Initial-guess shape" section (lines 419-436) is unique methodology evidence — the existing `concepts/derived-view-hoisting.md` worked examples are all state-shape-boundary applications. **Lifting target**: extend the concept page with the control-flow-boundary worked example.

   **OQ to add**: "The `chebyshev.md` §L4 'Initial-guess shape: branch vs. derived view' section (lines 419-436) is unique methodology evidence for `derived-view-hoisting` applied at the control-flow boundary (as distinct from the state-shape boundary that's the typical case). Lifting target: extend `concepts/derived-view-hoisting.md` with the control-flow-boundary worked example. Source: cycle-011 phase-1-corpus-reduction-batch-2 §slice-2 residual gap #4."

6. **The partial-positive-within-a-negative-result-slice pattern** documented in `polynomial_recurrence_step.md` §L1↔L1 self-tightening is unique methodology evidence — `concepts/negative-result-slice.md` does not document the sub-pattern. **Lifting target**: extend the concept page with a "Partial-positive sub-pattern" subsection citing the slice's self-tightening section as the canonical worked example.

   **OQ to add**: "The `polynomial_recurrence_step.md` §L1↔L1 self-tightening section is unique methodology evidence for the 'partial-positive-within-a-negative-result-slice' pattern (cross-family negative-result alongside within-family partial-positive). Lifting target: extend `concepts/negative-result-slice.md` with a 'Partial-positive sub-pattern' subsection. Source: cycle-011 phase-1-corpus-reduction-batch-2 §slice-3 residual gap #4."

7. **Friction signal forward-mitigation**: this dispatch applied the cycle-010 friction signal `phase-1-corpus-audit-line-range-arithmetic-brittleness` (recurrence-1) mitigation directly — H2 boundaries were enumerated via `grep -n "^## \|^# "` before line-range arithmetic. Cycle-012 meta-phase watch-item; recurrence stays at 1 unless reactivated.

8. **Batch progress**: cycle-010 audit covered 3 of 10 slices; this dispatch covers 3 more (orthog.md, chebyshev.md, polynomial_recurrence_step.md); cumulative coverage 6 of 10. Remaining 4 slices for batch-3+: `cg_preconditioning_framework.md`, `divfree.md`, `plane_rotation_stream.md`, `sparse_triangular_solve.md`. The cycle-010 priority order has `divfree.md` and `cg_preconditioning_framework.md` next (priorities #4 and #5); `plane_rotation_stream.md` (priority #6) should be audited jointly with `orthog.md` lines 313-464 (per OQ item 1 above); `sparse_triangular_solve.md` (priority #7) is expected to be a low-overlap audit.

9. **No slice file is mutated by this dispatch.** All proposed reductions are encoded as `proposed_changes` blocks for integrator-per-report. The verdicts and supersession maps in this CYCLE.md are inspection-only.

10. **Negative-result-slice handling is methodologically distinct from precursor-slice handling.** This is the first batch to audit a negative-result slice; the verdict (blocked / minimal reduction; the slice IS the artifact) is materially different from the cycle-010 audit's precursor-slice verdicts (partial-reduction with stub-pointer). Future batch audits should consider this distinction up-front: not every slice is a precursor; some are methodological artifacts that resist reduction by construction.
