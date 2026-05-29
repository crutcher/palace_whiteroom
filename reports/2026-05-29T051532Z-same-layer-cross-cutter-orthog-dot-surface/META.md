---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T053000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-29T054038Z
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
overall_status: ready
follow_up_agent: null
---

# META: verification of "L1 observation — the `orthog.hpp` Gram-Schmidt `LocalDot`+`GlobalSum` inner-product surface"

## Critique

### Checks run

**citation-validity — pass.** I independently re-read every load-bearing source range via `palace-codemap read_range`. All verify:
- `orthog.hpp:30-37` `IdentityInnerProduct`; `return LocalDot(x, y);` is exactly at `:35`. **Verified.**
- `orthog.hpp:46-52` MGS: `H[j] = dot_op(w, V[j]);` at `:49`, `Mpi::GlobalSum(1, &H[j], comm);` at `:50`, `w.Add(-H[j], V[j]);` at `:51`. **Verified.** The order-matters comment `// Global inner product: Note order is important for complex vectors.` is at `:48`. **Verified.**
- `orthog.hpp:66-70` CGS: `H[j] = dot_op(w, V[j]);  // Local inner product` at `:68`, `Mpi::GlobalSum(m, H, comm);` at `:70`. CGS2 `refine` second pass `:75-88`. **Verified.**
- `vector.cpp:674-685` complex `LocalDot`: source body is `{LocalDot(x.Real(),y.Real())+LocalDot(x.Imag(),y.Imag()), LocalDot(x.Imag(),y.Real())−LocalDot(x.Real(),y.Imag())}`, i.e. Re=xr·yr+xi·yi, Im=xi·yr−xr·yi = `x·conj(y) = yᴴ x` (arg-2 conjugated), with the `&x==&y` self-dot imag=0 fast path at `:678`. The report's transcription of this formula is exact. **Verified.**
- `vector.hpp:242` comment `// Calculate the local inner product yᴴ x or yᵀ x` + `LocalDot` decls `:243-244`. **Verified.**
- `vector.hpp:247-253` `Dot` template = `LocalDot(x,y)` then `Mpi::GlobalSum(1, &dot, comm)` — the FUSED form. **Verified.**
- `communication.hpp:266-270` `GlobalSum(int len, T *buff, MPI_Comm comm) { GlobalOp(len, buff, MPI_SUM, comm); }`. **Verified.**
- Bypass claim independently confirmed: `search_text "linalg::Dot|Dot\\(comm"` over `orthog.hpp` returns **zero hits** — `orthog.hpp` genuinely does not call the fused `linalg::Dot`. **Verified.**
- Incidental prose citations also check out: `iterative.cpp:630` (GMRES) and `:809` (FGMRES) are both `OrthogonalizeIteration(gs_orthog, comm, V, w, Hj, j);` call sites with `Hj[j+1] = Norml2(...)` immediately after — direct evidence the `H[j]` Hessenberg column is consumed. `OrthogonalizeIteration` dispatches to `OrthogonalizeColumnMGS/CGS/CGS2` at `iterative.cpp:316-322`. `romoperator.cpp:51-66` is the `OrthogonalizeColumn` wrapper with the `dot_op` substitution (`:59-65`). All confirmed.

**surface-or-evidence (CRUX) — pass.** This is the load-bearing check. The classification — that `orthog.hpp:35`'s `LocalDot`+self-applied-`GlobalSum` is the *unfused* form of `linalg::Dot`'s fused `GlobalSum∘LocalDot`, computing the identical `yᴴ x` inner product, hence **(a) an additional call-surface/variant-axis realization of the existing `dot` operator** and NOT a distinct primitive (b) — is **correct**. I verified the inner product is genuinely the same `yᴴ x`: both paths invoke the *same* `LocalDot` function (`vector.cpp:665-685`); `IdentityInnerProduct::operator()` literally `return LocalDot(x, y);`. The leaf kernel is byte-identical; the ONLY difference is the location/batching of the `Mpi::GlobalSum` collective (inside the fused `Dot` template vs. self-applied by the orthog routine, size-1-per-`j` for MGS vs. one size-`m` reduction for CGS). A distinct primitive (b) would require a different reduction kernel or a different conjugation convention — there is neither. Verdict (a) holds. The report is shaped as a pure observation feeding two **additive citation proposals** (no surface mutation, no status change), which is allowed — it is retroactive-evidence framing on existing firm themes, not a refinement-without-evidence. The "FIRST unweighted-observable witness outside the nleps deflation cohort" claim is corroborated: I read `inner-product-fold-specialization.md:301-329`, whose `observable_unweighted` cohort is exactly `nleps.cpp:522,529,568,675` and whose `finding` line confirms "the only intra-linalg/ unweighted observable sites are the four nleps.cpp SLEPc-NEP deflation/Newton sites." The orthog `H[j]` is observable (full complex value consumed in `w.Add(-H[j], V[j])` + Hessenberg store) and outside that cohort; the census missed it precisely because it scoped `linalg::Dot` callers while `orthog.hpp` bypasses `linalg::Dot`. The distinction is real and correctly stated.

**rotation-quality — pass (not applicable to observation-kind report).** No algebraic/structural/reduction rotation is asserted; this is a same-layer observation feeding additive citations. The fuse/unfuse classification logic is sound (same leaf, collective relocated/batched), but it is not a layer-rotation claim. No-op.

**variant-axis-coverage — pass.** The MGS-vs-CGS axis is correctly framed and complete: MGS = `m` reductions of size 1 (interleaved per-`j` with `w.Add`, the sequential dependency), CGS = one batched size-`m` reduction, CGS2 = two size-`m` reductions (the `refine` pass). This matches the source (`orthog.hpp:46-52` / `:66-88`) and the existing `orthogonalize.md:107-110` per-variant collective-shape disclosure (m×1 / 1×m / 2×m), which I verified. The orthogonal weighted-vs-unweighted axis (`IdentityInnerProduct` vs the B-weighted `dot_op` hook) is explicitly scoped OUT in a caveat (CYCLE.md "Caveat — B-weighted hook is a DIFFERENT surface"), and the element-type axis (real conjugation no-op vs complex) is explicitly scoped in a caveat. No hidden branches.

**cross-reference-integrity — pass.** All four target/cited artifact files exist (`L1-L0/dot-mutation-rotation.md` 357 lines, `L2-L1/inner-product-fold-specialization.md` 593, `L1/orthogonalize.md` 335, `L1/dot.md`). Every cited artifact line range resolves in-range and on-point: `dot-mutation-rotation` Sub-patterns A/B/C `:44-145` (insertion point for proposed Sub-pattern D, "after C before §The conjugation asymmetry" at `:146`, is accurate); the "orthogonalization named in prose only" claim verified at `:333` ("CG / orthogonalization / NLEPS sites" — named, but no pointer to `orthog.hpp:35`); `inner-product-fold-specialization.md:301-329` census yaml; `orthogonalize.md:107-110` (collective shape), `:163-165` (`dot` dependency), `:204-211` (`dot_op`/`InnerProductHelper` hook axis), `:321-325` (L1>L0 theme un-authored); `dot.md:43` (arg-1-conj L1 convention), `:119` (test-orthog witness). The cycle-020 source-report follow-up at `:203-208` exists and explicitly calls for exactly this audit ("a `same-layer-cross-cutter` or harvester pass on `orthog.hpp` ... likely a coverage gap of its own"), so the OQ-resolution claim is grounded. The two proposed `edit:` blocks are **proposals**, not direct writes (CYCLE.md states "I do NOT touch `book/`"), so no new files / SUMMARY.md wiring is at issue this dispatch; the one Markdown link in Proposal 2 (`[\`dot-mutation-rotation\`](../L1-L0/dot-mutation-rotation.md)`) points at an existing file. No broken references.

**edge-label-fidelity — pass.** Proposal 1 targets `L1-L0/dot-mutation-rotation.md` (an L1>L0 surface-form inventory) and the prose discusses exactly the L1→L0 lowering of the `dot` reduction into `LocalDot`+`GlobalSum`. Proposal 2 targets `L2-L1/inner-product-fold-specialization.md` §Applicability Condition 5 and discusses the `linalg::Dot`-caller census scope — consistent with that theme's L2>L1 edge. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared `status: pending`, observation-shaped (same-layer-cross-cutter classification). The content matches: a classification verdict ((a) with additive citation gaps), no new operator/theme authored, no status promotion/demotion of any entry. The two proposed-changes blocks are well-formed `edit:<path>` fences with placement instructions, citations, and justification kind. Follow-up routing is correctly LIFTER (re-anchor an existing firm theme with an additive citation), explicitly NOT harvester (no new primitive) — this matches the (a)-not-(b) verdict. The abstractor follow-up (`orthogonalize-mutation-rotation` theme) is correctly flagged-deferred under one-observation discipline, not enacted.

**skill-uptake-survey — warning.** The report's Supporting-evidence section states "self-verified per `verify-citation-range`," so that skill's invocation is referenced — good. However, the report's shape strongly implies `classify-variant-axis` (it makes a same-layer (a)/(b)/(c) classification turning on a variant-axis distinction: unfused/batched-collective surface vs. fused, MGS-vs-CGS collective shape) and `verify-refinement-surface` (it is the (a)-additional-call-surface determination). Neither is referenced. This is a pure telemetry surface (non-blocking) — the classification reasoning is sound regardless — but the skill-uptake is partial.

### Issues found

1. **(low / skill-uptake)** — `CYCLE.md` Supporting-evidence section references only `verify-citation-range`. The report makes an explicit (a)/(b)/(c) same-layer classification on a variant-axis (unfused/batched-collective vs. fused; MGS m×1 vs CGS 1×m), which is the documented territory of `classify-variant-axis` and `verify-refinement-surface`, neither of which is cited as invoked. Telemetry-only; does not affect the verdict's correctness. (Where: CYCLE.md §Supporting evidence, line 236.)

2. **(informational / non-defect, no action required)** — `dot.md:119` describes `linalg::Dot` as "used as the orthogonalisation-coefficient primitive in MGS and CGS," whereas this report's thesis is that the *production* orthog routines bypass `linalg::Dot` via `LocalDot`+`GlobalSum`. These are not in conflict: `dot.md:119` cites `test-orthog.cpp` (the test harness computes reference coefficients via `linalg::Dot` to check `orthog.hpp`'s output), i.e. test-reference path vs. production path. The report does not surface this nuance, but it introduces no error. Flagging only so a downstream lifter applying Proposal 1 does not misread the existing `dot.md:119` test citation as contradicting Sub-pattern D's bypass claim. (Where: CYCLE.md §Specific finding vs. existing `book/src/L1/dot.md:119`.)

3. **(trivial / citation-precision)** — Minor span discrepancy between report and existing artifact for the `IdentityInnerProduct` struct: this report cites `orthog.hpp:30-37` / `:35`, while `orthogonalize.md:205` cites the same struct as `orthog.hpp:25-37`. The struct definition is `:29-37` (the `:25-26` lines are the `// Concept: InnerProductHelper ...` doc comment). Both spans contain the struct; the report's `:30-37` is tighter and the `return LocalDot(x,y)` at `:35` is exact. No correction needed — noting for consistency only. (Where: CYCLE.md §Specific finding / Proposal 1 citations, vs. `book/src/L1/orthogonalize.md:205`.)

## Repair

### Fixes attempted

- **Finding 1 (low / skill-uptake telemetry)** — only `verify-citation-range` referenced; `classify-variant-axis` / `verify-refinement-surface` not cited despite the (a)/(b)/(c) classification.
  - **Decision**: not-needed.
  - **Rationale**: the critic scoped this as pure telemetry, non-blocking — the classification reasoning is sound regardless. Adding retroactive skill-invocation telemetry to the report's prose would be authoring, not a mechanical repair, and changes no claim. No edit.

- **Finding 2 (informational / non-defect)** — `dot.md:119` describes `linalg::Dot` as the orthogonalisation-coefficient primitive (test-reference path), which a downstream lifter applying Proposal 1 could misread as contradicting the report's production-bypass thesis.
  - **Decision**: repaired (the critic offered this as an optional one-line clarification).
  - **Action**: CYCLE.md §"Already-covered-transitively check (the (c) question)" — added a nested **Clarification** bullet under the operator-level bullet, restating the critic's exact observation (test-reference path via `test-orthog.cpp` vs production bypass; the two coexist) so the lifter does not read `dot.md:119` as conflicting with Sub-pattern D's bypass claim. Surgical, additive, no claim altered.

- **Finding 3 (trivial / citation-precision)** — `IdentityInnerProduct` struct span discrepancy (`:30-37` here vs `:25-37` in `orthogonalize.md:205`); the critic believed the report's `:35` for the `return` was exact.
  - **Decision**: repaired.
  - **Action**: Re-read `palace/linalg/orthog.hpp:1-38` via `palace-codemap read_range` (anchored from line 1 to fix the offset arithmetic). Exact source: `struct IdentityInnerProduct` at `:29`, the struct closes at `:36`, and `return LocalDot(x, y);` is at **`:34`** — i.e. the report's `:30-37` / `:35` is an off-by-one slip throughout (the "citation line range off by a small offset" repair case). Reconciled every occurrence in CYCLE.md to `:29-36` (struct) / `:34` (return): §Summary, §Observation-kind, §Specific finding heading + body, §Already-covered-transitively check, Proposal 1 (edit-block comment + prose + citations), Proposal 2, §Supporting evidence, and the §Open-questions OQ + B-weighted caveat. The tighter `:29-36` is preferred over `orthogonalize.md:205`'s `:25-37` (which folds in the `:25-28` Concept doc comment) since the report's scope is the struct + its return; the two artifacts are not in conflict (both spans contain the struct). The MGS `:49-51` / CGS `:68-70` line citations were independently re-confirmed by the critic and are unchanged.

### Unrepairable findings

None. All three findings were either not-needed (Finding 1) or mechanically repaired (Findings 2, 3) within repair authority.

## Suggested resolution

`ready`. Notes for the integrator: this is a clean observation feeding two additive citation proposals (no `book/` mutation, no status change). The citation slip (`:34` not `:35`; struct `:29-36`) is now reconciled, so the lifter applying **Proposal 1** (add Sub-pattern D to `L1-L0/dot-mutation-rotation.md`) inherits exact spans. The added Finding-2 clarification ensures the lifter does not misread `dot.md:119` (test-reference path) as contradicting the bypass thesis. Follow-up routing per the report stands: **lifter** for Sub-pattern D (load-bearing, additive, no status change); abstractor `orthogonalize-mutation-rotation` theme is correctly flagged-deferred under one-observation discipline. Promote the OQ `orthog-hpp-localdot-globalsum-unfused-dot-surface` as the report directs.
