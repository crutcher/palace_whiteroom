---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T17:05:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T17:25:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of "Audit eigsolve-spectral-transform-composition" (lowering-verifier, cycle-026 dispatch-6c)

## Critique

### Checks run

**citation-validity (LOAD-BEARING) — pass.** Re-ran `tools/citecheck/citecheck.py --scan` on the CYCLE.md: **39 ok, 0 failing (39 citations checked)** — matches the report's claim exactly. Independently re-ran the load-bearing `--anchor` spot-checks the dispatch flagged:
- The **cycle-025 +7 repair** holds with NO regression: `slepc.cpp:1824 --anchor 'opM->Mult'` → `[ok]` (anchor at line 1824), `slepc.cpp:1825 --anchor 'delta'` → `[ok]` (anchor at line 1825). `read_range(1801-1827)` confirms the `__mat_apply_EPS_A1` body is `ctx->opM->Mult(ctx->x1, ctx->y1); ctx->y1 *= ctx->delta * ctx->gamma;` at exactly `:1824`/`:1825`, and `__mat_apply_EPS_A0` is `opK->Mult`@1809 `*= delta`@1810. The off-by-7 drift cycle-025 found and repaired is gone on disk; the report's "confirmed correct, no regression" is itself confirmed.
- ARPACK `ApplyOp` decisive lines: `:579 --anchor 'opM->Mult'`, `:580 --anchor 'opInv->Mult'`, `:581 --anchor 'gamma'` — all `[ok]`. `read_range(562-590)` shows the exact branch structure the report describes (shift-invert `opM->Mult ▷ opInv->Mult ▷ y1*=gamma`; no-transform dual `opK->Mult`@573 `▷ opInv->Mult`@574 `▷ y1*=1/gamma`@575; projector tail `opProj->Mult`@586).
- SLEPc `__pc_apply_EPS` (`:1858 opInv->Mult`, `:1870 opProj->Mult`) and the un-scales (`:1861 *=1/(delta*gamma)`, `:1865 *=1/delta`) — all `[ok]`; `read_range(1847-1877)` confirms, and the function header comment `:1849-1851` literally names it the `(K−σM)⁻¹ x` inverse-apply.
- Remaining anchors all `[ok]`: PEP `opInv->Mult`@761/@778; `sigma = s`@245; `STSINVERT`@388; `ST_MATMODE_SHELL`@391; modeeigensolver `SetLinearSolver`@1037/@1050, `KRYLOVSCHUR`@1045. The PEP block comment `arpack.cpp:736-743` matches the theme's `L₀=[[−K,0],[0,M]]`, `L₁=[[C,M],[M,0]]` exactly. The L2 LHS law anchors (`L2/eigsolve.md:99`/`:103`/`:105`/`:163`, `:55-67` body) are each precise.

**The `:715` GetEigenvalue nuance — verified, correctly NOT a defect.** `slepc.cpp:715 --show` returns `715 | return l * gamma;` — the cited line genuinely IS the `return l * gamma;` content. `slepc.cpp:714 --anchor 'GetEigenvalue'` confirms the function NAME sits at `:714`, so a naive `--anchor 'GetEigenvalue' :715` reports `[DRIFT -1]`. This is precisely the content-citation-vs-function-name false-positive the dispatch warned of: the theme cites `:715` for the content the theme describes, and the content is at `:715`. `--anchor 'return l' :715` → `[ok]`. The report's handling (flag the nuance, supply `gamma`/`return l` as the correct anchor token, decline to treat it as drift) is exactly right and is the model behaviour for this kind of probe.

**surface-or-evidence — pass.** This is an audit, not a refinement (it proposes only an additive `verified_against:` block; no surface mutation, no rotation_claim asserted afresh). The audit-shape variant of the check applies: I spot-checked that both backend faces genuinely realize the same `apply_linop ▷ ksp_solve ▷ scal` L1 sequence. ARPACK `ApplyOp` (`:562-590`) is the explicit hand-assembly: `opM->Mult` (stage-1 `apply_linop`) ▷ `opInv->Mult` (stage-2 `ksp_solve`) ▷ `y1 *= gamma` (`scale_untransform` `scal` tail) ▷ guarded `opProj->Mult`. SLEPc decomposes the identical action across the PETSc ST shell: the operand matvec in `__mat_apply_EPS_A0/A1` (Mat shell), the inverse-apply in `__pc_apply_EPS` (PC shell), composed by `STSINVERT` + `ST_MATMODE_SHELL` (`:391`). The two-faces framing is well-anchored — `ST_MATMODE_SHELL` at `:391` is the literal source for "SLEPc delegates assembly to the PETSc ST layer." The per-step-body vs eigen-iteration-loop boundary is clean: the theme owns only the per-step de-fusion; the loop is delegated to L3 `eigsolve` (`partial-obstruction`, cycle-024, verified `partial-obstruction` on disk — "the body lifts, the loop does not"), referenced and not re-derived. No content duplication between this theme and the L3 entry.

**rotation-quality — pass (not the primary lens for an audit, but the lowered edge is a genuine de-fusion).** The underlying theme is an L2>L1 lowering whose `▷`-composition de-fuses into an explicit two-stage `apply_linop`-then-`ksp_solve` body — a structural (syntactic) expansion read line-for-line off positive source, not a rename. The audit neither degrades nor inflates this; it confirms the de-fusion is value-preserving by construction (the `▷` is by-definition the left-to-right dataflow the L1 sequence spells out). No 1:1 renaming masquerading as a rotation.

**variant-axis-coverage — pass.** The theme's variant axes are covered, and the audit walks each: spectral-transformation (none/shift-invert), problem-type (linear EPS / quadratic PEP / nonlinear NEP), and backend-orchestration (ARPACK explicit vs SLEPc ST-shell). The NEP per-step body is explicitly scoped OUT (deferred to the NLEPS-deflation cohort, `apply_nonlinear_pencil` recorded as the operand-stage variant, not folded in) — a clean scope-out, not a hidden branch. The B-matrix shell matvec `__mat_apply_EPS_B` (`:1831-1845`) is correctly noted as omitted (generalized-inner-product metric, not the shift-invert operand stage) — the audit explicitly checks this is not a coverage gap.

**cross-reference-integrity — pass.** All `[link]` targets in the theme resolve on disk: sibling themes (`orthogonalize-composition-lowering`, `gram-fold-specialization`, `deflate-composition-lowering`), concepts (`sequential-obstruction`, `solver-as-operator`, `constructed-operators`, `variant-absorption`), and the L1/L2/L3 chapters (`L1/{apply_linop,ksp_solve,scal,apply_nonlinear_pencil,eigsolve}.md`, `L2/eigsolve.md`, `L3/eigsolve.md`) all exist. The theme is wired into `SUMMARY.md:59` and `L2-L1/index.md:19`. **Build-readiness fence guard:** the report's proposed-changes block is a single ` ```edit:... ``` ` fence (lines 291/356, even parity) enclosing a `~~~yaml ... ~~~` tilde-fenced YAML block (lines 293/355) — the correct nested-fence technique (tilde for the inner block, backtick for the edit wrapper), no collision, body fully INSIDE the fence. No firm-body-outside-fence defect. (The theme itself is already firm + integrated cycle-025; this audit adds metadata only, so the firm-body-inside-fence guard is satisfied trivially for the edit.)

**edge-label-fidelity — pass.** The edge label is L2>L1 (`eigsolve-spectral-transform-composition`); every section of the audit discusses exactly that edge (the L2 `apply_shift_invert` LHS de-fusing into L1 `apply_linop`/`ksp_solve`/`scal` leaves). The L3 boundary is referenced as a boundary (the loop obstruction), not conflated with the L2>L1 edge. No mismatch.

**plan-kind-consistency — pass.** Declared kind is a lowering-verifier audit with verdict fully-supported; the content is an audit (per-citation verdicts, applicability-condition walk, no surface authoring). The proposed change is an additive `verified_against:` block leaving the theme `firm` — consistent with an audit that found no defect. The theme stays firm; both RHS leaves (`apply_linop`, `ksp_solve`, plus `scal` and `apply_nonlinear_pencil` tails) are confirmed firm on disk; no speculative operator. Classification matches content shape.

**skill-uptake-survey — pass.** The audit shape implies `verify-citation-range` (invoked, via the mechanical `tools/citecheck/` `--anchor`/`--scan` realization — the cycle-024 wiring) and the partly-constructive / proposed-changes-fence guards (N/A — no partly-constructive sub-part, fence is clean). The report explicitly references the citecheck-as-shared-line-map adjudication. Telemetry present; nothing missing.

### Issues found

No blocking issues. The audit is mechanically sound — every load-bearing anchor independently re-verified `[ok]`, `--scan` reproduces the claimed 39/0, the cycle-025 +7 repair confirmed non-regressed, both backend faces confirmed to realize the same L1 sequence, the body/loop boundary confirmed clean, and the OQ followup (`eigsolve-spectral-transform-composition-lowering-verifier-audit-followup`) is properly appended to `scaffolding/open-questions.md:863` as RESOLVED/fully-supported. Two minor, non-blocking observations for the repairer/integrator (neither gates application):

1. **Count-label off-by-one (cosmetic, `CYCLE.md:38` Summary and §Proposed changes).** The Summary calls it "the additive `verified_against:` block" and the dispatch framing said "16-entry," but the proposed block (`CYCLE.md:294-354`) contains **15** `- citation:` entries (15 `verdict: supports`, confirmed by count). All 15 are valid and complete; the L0 evidence ranges (14 distinct source citations) plus the L2/L3 artifact citations are all covered. This is a label/count discrepancy only — no entry is missing, no entry is wrong. Severity: trivial. (The "14 distinct L0 citations" claim at `CYCLE.md:380` is the source-only subset; the 15 block entries = 13 source-file ranges as listed + L2/eigsolve + L3/eigsolve artifact rows. Internally consistent once the source-vs-artifact split is read.)

2. **Self-acknowledged cosmetic span non-uniformity (NOT a defect — already flagged by the report, recorded here for completeness).** The theme cites `slepc.cpp:364-366` for `SetLinearSolver` (`opInv = &ksp`) while the L2 entry §Signature cites `:364-367`; the body on disk is `:364-367` (4 lines incl. the closing brace) and `opInv = &ksp` is at `:366`. Both ranges bound the same construct and both pass `--scan`; this is a non-uniform range width across sibling chapters, not a drift. Similarly `:715` vs the L2 `:711-716` GetEigenvalue spans. The report correctly classifies both as cosmetic carry-notes for an optional future uniformity pass, explicitly out of this audit's edit scope. No action required; surfaced only so a downstream lifter/cross-cutter uniformity pass is aware.

The `frontmatter` `verifies:` field points at `../REPORT.md` per the META template convention; the actual report file is `CYCLE.md` in this directory (the project-wide rename). Not an issue with this report — noting the template/convention mismatch is repo-wide, not specific to this audit.

---

## Repair

### Fixes attempted

- **Finding**: Count-label off-by-one — Summary / §Proposed changes purportedly say the `verified_against:` block is "16-entry" but the block has 15 entries.
  - **Decision**: not-needed
  - **Rationale**: The literal "16" / "16-entry" count-label does **not appear anywhere in CYCLE.md** (`grep -n "16" CYCLE.md` returns only timestamp fragments `16:47:39Z`; no count-label). The "16-entry" phrasing lived in the **dispatch framing**, not in the report. The report's Summary (`:18-38`) and §Proposed changes (`:284-289`) refer to the block generically as "the additive `verified_against:` block" with no entry-count claim. The block itself has 15 `- citation:` entries (`grep -c '^  - citation:'` → 15, all valid). The only in-report count claim is `:380` "across all 14 distinct L0 citations", which the critic already adjudicated **correct** (source-only subset; 13 source ranges + L2 + L3 = the 15 block rows once the source-vs-artifact split is read). The artifact (CYCLE.md) is already internally self-consistent — there is no anchor text to edit. Mechanical fix has no target.

- **Finding** (critic item 2): Self-acknowledged cosmetic span non-uniformity (`slepc.cpp:364-366` vs L2 entry's `:364-367`; `:715` vs `:711-716`).
  - **Decision**: not-needed
  - **Rationale**: Correctly classified by the report as a non-drift carry-note for an optional future uniformity pass (`CYCLE.md:382-389`), explicitly out of this audit's edit scope. Both ranges bound the same construct and both pass `--scan`. No edit warranted; surfacing-only.

- **Finding** (dispatch directive): If the `verified_against:` block uses a `~~~yaml` nested-fence stand-in, ensure proper ```` ```yaml ```` encoding for the integrator.
  - **Decision**: not-needed (left as `~~~yaml`)
  - **Rationale**: The block already uses the **correct** nested-fence technique — a `~~~yaml` tilde fence (`CYCLE.md:293`/`:355`) nested inside the ` ```edit:... ``` ` backtick wrapper (`:291`/`:356`). Both fences have even parity; the body is fully inside both. The critic independently verified this (META critique, cross-reference-integrity check: "the correct nested-fence technique... no collision, body fully INSIDE the fence"). Converting `~~~yaml` → ```` ```yaml ```` would create a backtick-fence **collision** with the outer ` ```edit: ` wrapper — the exact defect the tilde stand-in exists to avoid (cf. `convert-nested-fences-to-indented-code-in-proposed-changes-block`, which converts to *indented code*, never to a colliding backtick fence). The tilde form is already integrator-ready; changing it would be a regression.

- **Finding** (dispatch directive): Fix stale `verifies: ../REPORT.md` → `../CYCLE.md` if present.
  - **Decision**: repaired
  - **Action**: `META.md` frontmatter `verifies:` — `../REPORT.md` → `../CYCLE.md`. Trivial cross-reference fix to the project-wide REPORT.md→CYCLE.md rename (in-scope: "trivial cross-reference fix to a renamed file"). Filed under the `cross-reference-integrity` check.

### Unrepairable findings

None. No finding required substantive authoring or exceeded repair authority.

## Suggested resolution

`ready`. The critic graded all 8 checks `pass`; the audit is mechanically sound (39 ok / 0 failing, cycle-025 +7 repair confirmed non-regressed, both backend faces confirmed to realize the same L1 sequence, `:715` content-citation false-positive correctly declined). The two non-blocking observations resolved as `not-needed` (the count-label "16" has no anchor in the report — the artifact is already self-consistent; the span non-uniformity is a correctly-classified carry-note). The lone applied edit is the trivial `verifies:` frontmatter rename. The additive `verified_against:` block is integrator-ready as-is (proper `~~~yaml`-inside-` ```edit: ` nesting). Integrator: apply the additive block; the theme stays `firm`; promote the RESOLVED/fully-supported OQ (`eigsolve-spectral-transform-composition-lowering-verifier-audit-followup`, `open-questions.md:863`).
