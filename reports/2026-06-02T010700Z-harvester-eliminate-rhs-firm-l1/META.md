---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T013000Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-02T014500Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Formalize eliminate_rhs at L1" (cycle-055 D3)

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck --scan` (29 ok / 1 ambiguous-basename, the latter being the report's own intra-artifact `index.md:74` self-reference, not a Palace source cite). Anchor-checked the load-bearing pinpoints with `--anchor`. The L0 body citations are **correct on-disk**: `rap.cpp:64` (SetSubVector gather), `:65` (prolongation), `:69` (`A->Mult` = apply_linop — `--anchor Mult` OK), `:72` (RestrictionMatrixMult), `:73` (`b.Add(-1.0,ty)` = axpy — `--anchor Add` OK), `:74-81` (diag-policy pin), `:38-41` (DIAG_ONE/DIAG_ZERO `MFEM_VERIFY`), `rap.hpp:97-99` (decl + doc-comment). The report's stated `codemap +2 drift on the comment/brace boundary` was correctly handled — every emitted `rap.cpp` line matches on-disk truth (codemap `read_range` on 56-82 in fact returned aligned content this query, but the report's choice to use on-disk numbers is right and they are all correct). **One real drift in the witness**: `x.ParallelProject(X)` is cited at `laplaceoperator.cpp:248` (CYCLE.md §Context and §Evidence:288); on-disk it is line **247** (`:248` is the `dynamic_cast<const MultigridOperator *>` line). `--anchor ParallelProject` confirms `[DRIFT -1] suggested :247`. The other witness pinpoints are correct: `:238` (ProjectBdrCoefficient), `:252` (EliminateRHS call). Warning (not fail) because the load-bearing clean-gate anchors are all correct; the drift is on a supporting restriction-step cite.

**surface-or-evidence — pass.** This is a rough-in→firm promotion of an existing index bullet plus a new operator chapter (refinement-shaped). The promotion modifies surface (new `eliminate_rhs.md`, index bullet flip, dep-map row, SUMMARY) and is backed by line-by-line positive source evidence (`rap.cpp:56-82`). Not a pure rotation_claim. Pass.

**rotation-quality — pass.** The L1 form is strictly more compact/abstract than L0: the five-pooled-vector imperative scatter/apply/restrict/in-place-Add/pin protocol collapses to `set_essential(axpy(-1, apply_linop(K, restrict_essential(x_bc)), b), pin)`. State hiding (pooled `lx/ly/tx/ty` + in-place `b` mutation erased to a pure return), the prolongation/restriction round-trip absorbed into one `apply_linop`. Genuine compression, not a rename.

**variant-axis-coverage — pass.** Two axes declared and covered: `diagonal-policy` (DIAG_ONE | DIAG_ZERO, with the `:38-41` MFEM_VERIFY witnessing exactly-two-valued, and the interior block shown identical across both) and `bc-data-homogeneity` (homogeneous collapses via law 3 / inhomogeneous fires the full lift). A third axis `operator-true-dof-representation` is explicitly scoped-out ("absorbed") with the prolongation/restriction round-trip named as the L0 realization of one `apply_linop`. No hidden branches — the `if/else if` on `diag_policy` is the only L0 branch and both arms are covered.

**cross-reference-integrity — warning.** All live links resolve: `apply_linop.md`, `axpy.md`, `fe_assemble.md`, `divfree-projector.md` exist; `eliminate_rhs.md` is the new file (correctly absent pre-integration); the L1>L0 `eliminate-rhs-mutation-rotation` forward-ref is correctly plain-text (target not on disk). `fe_assemble.md:145-150` exactly supports law 4 (the "BC-elimination is NOT part of the fold" sibling statement — verified on-disk). Index anchors verified: `:74` is D3's own `eliminate_rhs` rough-in bullet (replacement target matches verbatim), the `:70` cohort header is correctly NOT touched (D7-owned), `:73` `eliminate_essential_bc` sibling correctly left rough-in, dep-map `floquet-correction` row at `:111` is the correct insertion anchor, SUMMARY `floquet-correction` at `:124` (L1 Part) is the correct anchor distinct from the L1-L0 one at `:141`. **Two issues**: (1) the `set_subvector` reuse claim is imprecise — `divfree-projector` names **`set_subvector_zero`** (a `concepts/set_subvector_zero.md` concept page, the boundary-*zeroing* special case), not a general `set_subvector`; `eliminate_rhs`'s DIAG_ONE pin writes the boundary *data* `x`, which is the general `SetSubVector`, of which `set_subvector_zero` is the zero-arm. The "same concept that divfree-projector names" framing slightly overstates the match (the DIAG_ZERO arm is exactly `set_subvector_zero`; the DIAG_ONE arm and the gather are its generalization). (2) **Fence parity defect** — see Issues.

**edge-label-fidelity — pass.** Not a lowering-theme report (no L_{n+1}→L_n edge label on the artifact). The L1>L0 `eliminate-rhs-mutation-rotation` is forward-referenced (forthcoming), and the §Downward-to-L0 prose discusses exactly that L1→L0 direction (gather→prolong→apply→restrict→in-place Add→pin). Consistent.

**plan-kind-consistency — pass.** Declared `firmness: firm` with a `## Status: firm` carrying the clean-gate PROMOTE verdict + the firm-on-positive-structure no-dedicated-test caveat (correctly non-gating per the apply_linop/fe_assemble precedent, since every law is a syntactic identity on fully-specified positive source). Content shape matches: full Signature + Semantics + 4 Algebraic-laws + 3 non-laws + Dependencies + Variant-axes + Evidence. No rough-in placeholders inside a firm-claimed body. The clean-gate call itself (PROMOTE — clean) is **sound**: the body verifiably lifts in existing spine vocabulary (`:69` apply_linop, `:73` axpy, `:64/:76/:80` set_subvector mask); D3 did not force it.

**skill-uptake-survey — pass (telemetry).** The report cites use of `citecheck --scan`/`--anchor` and on-disk verification (the documented `codemap-read-range-plus-one-drift-on-brace-boundary` friction is named). No fence-parity self-check via `proposed-changes-fence-encloses-full-body-guard` is referenced — and a fence defect slipped through (see Issues), so that skill's invocation would have caught it. Surfaced, non-blocking.

### Issues found

1. **[warning] Citation drift on the witness restriction step.** `CYCLE.md` §Context (the `:72`-numbered narrative line) and §Evidence (line 288) cite `x.ParallelProject(X)` at `laplaceoperator.cpp:248`; on-disk it is line **247** (`:248` is `dynamic_cast<const MultigridOperator *>`). `--anchor ParallelProject` → `[DRIFT -1] suggested :247`. The dep-map row's witness range `laplaceoperator.cpp:225-252,252` brackets it so the range stays in-bounds, but the pinpoint `:248` is wrong by +1. Repair: change the two `:248` pinpoints to `:247`.

2. **[warning/build-risk] Fence-parity defect — orphan closing fence at CYCLE.md:321.** The `edit:book/src/L1/index.md` proposed-changes region is authored as three sub-blocks: old-bullet (309 open / 311 close), replace-with (313/315), dep-map row (318/320). Immediately after the dep-map block closes at line 320, **line 321 is a stray standalone ` ``` ` with no matching opener** (confirmed: lines 320 and 321 are two consecutive fence lines, 322 blank, 323 opens the SUMMARY block). Total fence count is 15 (odd). This orphan fence can cause the integrator's proposed-changes parser to mis-associate the following `edit:SUMMARY.md` block or swallow content. Repair: delete line 321.

3. **[warning] `set_subvector` reuse claim slightly overstates the existing-vocabulary match.** §Dependencies, §Status (clean-gate honesty note), and the dep-map row all assert the essential-dof mask is "the same `set_subvector` concept that `divfree-projector` already names and uses." `divfree-projector.md` actually names `set_subvector_zero` (`concepts/set_subvector_zero.md`) — the boundary-*zeroing* special case. The DIAG_ZERO pin arm IS exactly that; but the gather (`:64`, writes `x`) and the DIAG_ONE pin (`:76`, writes boundary data) are the *general* `SetSubVector`, of which `set_subvector_zero` is the zero-arm. The clean-gate still holds (the mask is a thin projection either way and `apply_linop`+`axpy` carry the load), but the claim as written should be tightened to "the general `set_subvector` write-mask, whose zeroing special case `divfree-projector` names as `set_subvector_zero`." Not a clean-gate-breaker — surface-precision only.

4. **[observation, non-blocking] Witness double-cite cosmetic.** The dep-map row cites `palace/models/laplaceoperator.cpp:225-252,252` (range + redundant trailing `:252`). The trailing `:252` is the precise EliminateRHS call within the already-stated range — harmless but redundant. Optional tidy.

### Summary for repairer

The clean-gate call is sound and the load-bearing apply_linop/axpy anchors are correct — the firm promotion is well-founded. Three repairable surface defects: (1) `:248`→`:247` witness drift (2 occurrences), (2) **delete the orphan fence at line 321** (build-risk), (3) tighten the `set_subvector`/`set_subvector_zero` reuse wording. None touch the load-bearing structure.

## Repair

### Fixes attempted

- **Finding** [warning/build-risk]: orphan closing fence at `CYCLE.md:321` after the dep-map sub-block (15 fences, odd parity) — can mis-associate the following `edit:SUMMARY.md` block at integration.
  - **Decision**: repaired
  - **Action**: Deleted the stray standalone ` ``` ` fence (`CYCLE.md` proposed-changes region, between the dep-map row close and the SUMMARY edit block). Re-verified fence parity: now **14 fences, even**, all blocks balanced — `new:eliminate_rhs.md` (open/close + nested `text` Signature block), `edit:index.md` (3 sub-blocks: old-bullet / replace-with / dep-map row), `edit:SUMMARY.md` (old / replace-with). This is the `proposed-changes-fence-encloses-full-body-guard` shape (the skill the critic noted was not self-invoked).

- **Finding** [warning, citation-validity]: `x.ParallelProject(X)` cited at `laplaceoperator.cpp:248`; on-disk it is `:247` (`:248` is the `dynamic_cast<const MultigridOperator *>` line). Two occurrences (§Context line 72, §Evidence line 291).
  - **Decision**: repaired
  - **Action**: Both `:248` → `:247` (`CYCLE.md` §Context + §Evidence). Verified byte-exact via codemap `read_range` on `laplaceoperator.cpp:244-253`: line 247 is `x.ParallelProject(X);  // Restrict to the true dofs`, line 248 is the `dynamic_cast`. Off-by-one slip, in repair scope (a few-line drift on a supporting witness cite). Load-bearing `rap.cpp` anchors (`:69`, `:73`, `:64/:76/:80`) left untouched per critic confirmation.

- **Finding** [warning, cross-reference-integrity]: the `set_subvector` reuse claim says `divfree-projector` "names and uses" `set_subvector`, but it names `set_subvector_zero` (the zeroing special case). The DIAG_ZERO arm matches `set_subvector_zero` exactly; the gather + DIAG_ONE arm are the general write-mask.
  - **Decision**: repaired
  - **Action**: Tightened wording in two places (`CYCLE.md` §Dependencies + §Status clean-gate honesty note): the gather (`:64`) and DIAG_ONE pin (`:76`) are now stated as the **general** `set_subvector` write-mask, of which the DIAG_ZERO arm (`:80`) is the zeroing special case `set_subvector_zero` (`concepts/set_subvector_zero.md`) that `divfree-projector` names. Surface-precision only; the clean-gate (the mask is a thin projection either way; `apply_linop`+`axpy` carry the load) is unchanged. The dep-map row's "shared with `divfree-projector`, NOT a spine dep" phrasing did not overstate the concept name and was left as-is.

- **Finding** [observation, cosmetic]: dep-map row double-cite `laplaceoperator.cpp:225-252,252` (range + redundant trailing `:252`).
  - **Decision**: repaired (trivial tidy)
  - **Action**: `225-252,252` → `225-252` in the dep-map row (the `:252` EliminateRHS call is already bracketed by the range).

### Unrepairable findings

None. All findings were either `pass` (from critic), mechanically repaired, or `not-needed`.

## Suggested resolution

`ready`. Notes for the integrator:
- Fence parity is even (14) and all proposed-changes blocks are balanced after the orphan-fence deletion — the `edit:SUMMARY.md` block will parse cleanly.
- The firm clean-gate PROMOTE for `eliminate_rhs` stands (critic verified the body lifts in spine vocabulary; D3 did not force it).
- The L1>L0 `eliminate-rhs-mutation-rotation` lowering theme remains a plain-text forward-reference (correctly, per the missing-anchor convention) — a future abstractor pass authors it (sibling to `eliminate-essential-bc-mutation-rotation`), at which point the plain-text refs upgrade to live links.
