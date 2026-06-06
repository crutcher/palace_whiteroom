---
verifies: ../CYCLE.md
critiqued_at: 2026-06-06T003500Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
  rank-invariant: pass
  reachability: warning
repaired_at: 2026-06-06T004200Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
  rank-invariant: not-needed
  reachability: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of reduce/orthogonalize/chebyshev cohort grounding (cycle-110 D1)

## Critique

### Checks run

**citation-validity** — `warning`. The body-verb citations into `book/src/L4/krylov-step.md` are all REAL and in-range: `:142` (`dot Ap p'`) and `:145` (`dot r' r'`) in `cg_first_step`; `:158`/`:161` the same two in `cg_steady_step`; `:94` (`op.orthog (K.V_prefix, w)`); `:104` (`derived_views K' op ... typically residual_norm`); `:146`/`:162` (`res' = sqrt (abs beta')`). The altitude-justifying cross-cites are correct: `L4/inner_product.md:44-47` does state the krylov-step body CG α/β coefficients are `inner_product` let-bindings; `L4/dot.md:18-20` and `L4/nrm2.md:18-20` carry the quoted "named unit a CG/GMRES description wants" / "residual `nrm2(r)`" text; `L2/orthogonalize.md:11-13` carries "the op.orthog surface `krylov-step` folds". The `warning` is NOT a citation defect but a **measurement defect** in the §Verification block (see reachability + Issue 1): the report's recorded after-state numbers do not reproduce.

**surface-or-evidence** — `pass`. This is a frontmatter-only grounding edit (no prose claims, no new surface), shape-analogous to the c107/c108/c109 grounding passes. The three new `composes` `depends-on` edges are each backed by a consumer-body citation showing krylov-step genuinely composes the target verb. No record is named-only-by-use; no new record introduced. Allowed shape.

**rotation-quality** — `pass`. Not applicable to a grounding/edge-typing dispatch — no algebraic/structural rotation is asserted; the edits add reachability edges over already-firm vocabulary. No-op (mark pass).

**variant-axis-coverage** — `pass`. No variant axes introduced or modified; the edit types existing edges. The altitude exception (orthogonalize → L2 because no `L4/orthogonalize` op exists) is correctly handled and disclosed, not a hidden branch.

**cross-reference-integrity** — `pass` (load-bearing here). Every edge target slug exists on disk: `book/src/L4/dot.md`, `book/src/L4/nrm2.md`, `book/src/L2/orthogonalize.md` (the three new edges); and the routed/declined targets `L4/gram_reduce.md`, `L4/preconditioning-framework.md`, `L3/{dot,inner_product,nrm2}.md`, `L2/{inner_product,gram,incremental-least-squares}.md`, `L4/ksp_solve.md`. The proposed-changes `[old]` anchor matches the on-disk text exactly (verified by a clean apply). All resolve.

**edge-label-fidelity** — `pass`. Each new `composes` edge's prose discusses the exact edge it labels. `L4/krylov-step → L4/dot` is backed by the `dot` calls in the body; `→ L4/nrm2` by the residual-norm readout; `→ L2/orthogonalize` by `op.orthog`. The altitude calls are correct: `dot`/`nrm2` exist as firm L4 ops (so the L4-chapter body edge faithfully points L4→L4, mirroring `L4/ksp_solve → L4/krylov-step`), while orthogonalize has no L4 op so the edge crosses to the L2 named composition — the report flags this exception explicitly and it is faithful.

**plan-kind-consistency** — `pass`. The content shape (frontmatter edge grounding + faithful-path-or-finding split + routed OQ findings) matches the declared grounding-pass kind and the §(g) GROUND-don't-remove directive. The DECLINED `gram_reduce → inner_product` edge and the ROUTED chebyshev/jacobi + gram/ils findings are correctly dispositioned as findings, not forced edges — exactly the faithful-edge-or-finding behavior the kind calls for.

**skill-uptake-survey** — `pass`. The report references the c107/c108/c109 grounding precedents and the lint invocation (`graded_stack_lint.py --show-inbound`); the verify-apply-revert discipline is followed and book/ confirmed clean. No missing skill reference for this shape.

**rank-invariant** — `pass`. The three new `depends-on` edges are well-founded: `L4/krylov-step` is `rank: firm` (rank 3); `L4/dot` carries `rank: firm` via... — correction: `L4/dot.md` and `L4/nrm2.md` declare `firmness: firm` but I did not confirm a `rank:` token on `dot`/`nrm2` (only krylov-step and gram_reduce carry an explicit `rank: firm` line in the files I read). Regardless, the lint reports **RANK VIOLATIONS: none (0)** both before and after the applied edit (reproduced — see below), so the invariant HOLDS over the new edges. `L2/orthogonalize` has no frontmatter at all (typed-no-rank), so its inbound edge holds vacuously, as the report states. No new violation introduced.

**reachability** — `warning`. The qualitative claim is CORRECT and reproduced: applying the three edges flips exactly the claimed nodes reachable (`L4/dot`, `L4/nrm2`, `L4/inner_product`, `L3/dot`, `L3/inner_product`, `L3/nrm2`, `L2/inner_product`, `L2/orthogonalize`, plus the `L2-L1/inner-product-fold-specialization` theme — all confirmed gone from the garbage list via `--show-inbound`). STRONGER GARBAGE SIGNAL 34→26 (−8) reproduces EXACTLY. The host krylov-step is genuinely reachable (`← L3/krylov-step, L4/ksp_solve ← feature/{driven,electrostatic,magnetostatic}.L4`). BUT the headline magnitude does not reproduce — see Issue 1.

### Issues found

**Issue 1 — reachability headline overcounts by 2 (`CYCLE.md` §Summary + §Verification, MEDIUM).** The report claims **reachable 107→119 (+12)** and **detritus 152→140 (−12)**. I independently reproduced the edit on a scratch copy of `book/src/L4/krylov-step.md` and ran `python3 tools/graded-stack-lint/graded_stack_lint.py` (deterministic, confirmed by two identical runs, then reverted — `git status --short book/` empty):

- baseline: reachable **107**, rank_violations 0, stronger-garbage **34**, detritus **152**, untyped 60 — matches the report's "Before" block exactly.
- after the 3 edges: reachable **117** (NOT 119; +10 not +12), rank_violations **0** (HELD — matches), stronger-garbage **26** (−8 — matches exactly), detritus **142** (NOT 140; −10 not −12), untyped **60** (HELD — matches).

So three of the five after-numbers reproduce exactly (rank_violations 0, stronger-garbage 26, untyped 60) but the two reachability-count figures are each off by +2: actual reachable is 117 (report says 119) and actual detritus is 142 (report says 140). The directional claim, the specific flipped node set (8 ops + 1 theme ≈ +9/+10, consistent with the measured +10), and the −8 garbage drop are all sound — only the +12/119 and −12/140 headline figures are wrong. The report's own enumerated flip list ("8 ops + theme") is internally inconsistent with a +12 claim and consistent with the measured +10. This is a recording error in the §Verification "After" block, propagated into §Summary, the OQ progress note, and the per-leg table. The integrator should treat the true post-D1 reachable count as **117**, not 119.

**Issue 2 — D1/D2 reachability deltas are NOT additive; the cumulative number must be re-measured at apply time (cross-cycle, MEDIUM — flagged per dispatch instruction).** The parallel dispatch D2 (axpy-family typing, not critiqued here) reportedly ALSO claims reachable 107→119. D1's flipped set is the inner_product/dot/nrm2/orthogonalize reduce-to-scalar chain; D2's set is the axpy-family (`L2/axpy`, `L2/axpby`, `L2/axpbypcz`, etc. — all present in the current stronger-garbage list). These are **disjoint node sets**, so the two deltas are largely independent — but BOTH start from the same baseline of 107, and any shared cascade-interior node (e.g. a common L1 leaf both chains reach) would be double-counted if the integrator naively sums. The combined post-both-land reachable is therefore NOT 107+12+12 and NOT 107+10+10 by simple addition; it MUST be re-measured by running the lint after both edit-sets are applied. D1's measured contribution in isolation is +10 (107→117); this is attributable specifically to D1's three krylov-step edges. Note this for the integrator: do not sum; re-measure.

**Issue 3 — declined/routed dispositions are CORRECT (no defect; recorded as positive confirmation).** I verified the faithful-path-or-finding split:
- `gram_reduce → inner_product` decline is faithful: `book/src/L4/gram_reduce.md:6-13` shows `gram_reduce depends-on L1/matrix-weighted-norm + L1/bilinear-form` and `reference: L4/inner_product`; the body (`:32-34`) explicitly calls it "the reduce-to-matrix member ... the **sibling** of the reduce-to-scalar `inner_product`". Typing it `depends-on inner_product` would misclassify a sibling as a constituent — correctly declined.
- chebyshev/jacobi preconditioner routing is faithful: `L4/preconditioning-framework` appears in `L4/ksp_solve`'s INBOUND list (`L4/ksp_solve ← ... L4/preconditioning-framework ...`), so the framework CONSUMES ksp_solve — the reversed direction the report claims. A `ksp_solve → preconditioning-framework` edge would invert the real consumer→producer direction. Correctly routed to a baseline-exception, not forced.

These are the correct behaviors; no repair needed for the dispositions.

**Issue 4 — minor: `rank:` token absence on `L4/dot`/`L4/nrm2` (LOW, informational).** The report (§Faithfulness, well-foundedness paragraph) asserts "`L4/dot`/`L4/nrm2` carry `rank: firm`". I read both files: they declare `firmness: firm` but I did not observe an explicit `rank: firm` line (unlike `krylov-step.md:5` and `gram_reduce.md:5` which do). This does not change the rank-invariant verdict (the lint reports 0 violations before and after), but the report's specific claim that these two targets "carry `rank: firm`" may be imprecise. Not blocking; flagged for accuracy.

## Repair

### Fixes attempted

- **Finding (reachability / Issue 1)**: reachability headline overcounts by 2 — report claims reachable 107→119 (+12) / detritus 152→140 (−12), but the true ISOLATED D1 contribution is reachable 107→117 (+10) / detritus 142 (−10).
  - **Decision**: repaired
  - **Action**: independently reproduced apply→lint→revert on `book/src/L4/krylov-step.md` (3 `composes` edges), confirming reachable **117**, rank_violations **0**, STRONGER GARBAGE **26**, detritus **142**, untyped **60** — matching the critic's reproduction exactly (then reverted; `git status --short book/` empty). Corrected every occurrence of the 119/+12/140/−12 figures to 117/+10/142/−10 in CYCLE.md: §Summary bullets, §Faithfulness "to produce the +12 cascade", §Verification "After" block + "+12 nodes" prose, the OQ progress note, the per-leg-table preamble, and the Caveats "(+12 reachable…)" line. The proposed-change `edges:` block was NOT touched (edges verified correct).

- **Finding (reachability / Issue 2)**: D1/D2 deltas are NOT additive; cumulative reachable must be re-measured at apply time.
  - **Decision**: repaired
  - **Action**: added an explicit blockquote note to §Summary (and inline to the OQ progress note) telling the integrator the +10/117 figure is D1's isolated contribution, that D1 and D2 rescue disjoint node sets, that the combined count lands near 119, and that it MUST be re-measured by running the lint after both edit-sets apply — do not sum the deltas.

- **Finding (citation-validity / Issue 4)**: report asserts `L4/dot`/`L4/nrm2` "carry `rank: firm`"; on disk both declare `firmness: firm` with no explicit `rank:` line.
  - **Decision**: repaired
  - **Action**: verified on disk (`head` of both files: `firmness: firm`, no `rank:` token). Softened the §Faithfulness well-foundedness paragraph to "`L4/dot`/`L4/nrm2` declare `firmness: firm` (no explicit `rank:` line, but the lint reports 0 violations over the new edges either way)". The `rank: firm` reference for `L4/krylov-step` is retained (it genuinely declares it on `krylov-step.md:5`). Rank-invariant verdict unaffected (lint 0 violations).

The `citation-validity` warning was, per the critic, a label for the §Verification measurement defect (not a citation defect); it is resolved by the same number-correction. All routed/declined dispositions (chebyshev/jacobi baseline-exception, `gram_reduce` sibling decline, `L2/gram` / `L2/incremental-least-squares` OQs, lazy-tail typing OQ) were left untouched — the critic confirmed them correct.

### Unrepairable findings

None. Both warnings were measurement/wording defects, mechanically fixable within repair authority. The `edges:` proposed-change block is correct and verified; no substantive authoring was required.

## Suggested resolution

`ready`. Integrator notes:
- Apply the single `book/src/L4/krylov-step.md` frontmatter edit (+3 `composes` edges) as written in §Proposed changes.
- D1's isolated reachable contribution is **+10 (107→117)**, detritus **142**, STRONGER GARBAGE **26**, rank_violations **0**, untyped **60** (repairer-reproduced).
- **Re-measure the cumulative reachable after BOTH D1 and D2 land** — do not sum the per-dispatch deltas (disjoint rescue sets; combined ≈ 119 but the lint number is authoritative). Run `python3 tools/graded-stack-lint/graded_stack_lint.py` after applying both edit-sets for the cycle-record figure.
