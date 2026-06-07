---
verifies: ../REPORT.md
critiqued_at: 2026-06-07T074500Z
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
repaired_at: 2026-06-07T080500Z
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

# META: verification of "Formalize flux_recovery_estimate at L1"

## Critique

### Checks run

**citation-validity — warning.** `citecheck --scan` clears all 27 citations on bounds + path-hygiene (`27 ok, 0 failing`). All BLOCK anchors verify exactly against on-disk source / codemap symbol defs: `ComputeErrorEstimates` `:184-268` (exact), `GradFluxErrorEstimator` ctor `:273-378` (exact), `CurlFluxErrorEstimator` ctor `:391-500` (exact), `FluxProjector` ctor `:109-167` (exact), `projector.Mult(F,G)` `:193` (exact), composite `grad_estimates += curl_estimates` `:536` and `:566` (BOTH exact — the producer's +3 drift correction is CONFIRMED correct via `search_text`, not relied on read_range), the Grad `linalg::Sqrt` energy epilogue `:386` (exact), Grad/Curl `AddErrorIndicator` `:381`/`:503` (exact). The drift correction the producer flagged is genuine and was applied correctly. HOWEVER, a cluster of **interior pinpoints drifted -2 to -4 within otherwise-correct block ranges**, confirmed by direct on-disk `Read` (on-disk wins): see Issues. These are real anchor drifts (the cited line does not carry the asserted token), so the check is `warning` not `pass`; none invalidate a claim (the surrounding block ranges are correct and the claims hold), so not `fail`.

**surface-or-evidence — pass.** This modifies surface: it promotes the rough-in dep-map row to a firm chapter with full Signature/Semantics/Laws/Evidence, and carries positive-structure evidence (the firm-on-positive-structure escape, not a bare rotation_claim). Record-definition sub-check: the signature NAMES two records, `FluxEstimator` and the nested `FluxProjector`. Both have a definition home — the in-chapter `## Record definition` section enumerates fields, types, construction-vs-run-time stratum, and L0 home for each (single-consumer case, correctly chosen since only this verb consumes `FluxEstimator`). The nested `FluxProjector` is defined in the same section with its own field table. No undefined signature-named record. Pass.

**rotation-quality — pass (not a rotation entry).** This is an L1 operator harvest, not a cross-layer lowering asserting an algebraic/reduction rotation. No L_{n+1}→L_n compaction claim is made; the chapter's job is to define the verb in L1 vocabulary. The check is inapplicable to a same-layer harvest; marked pass.

**variant-axis-coverage — pass.** The verb has one material variant axis (flux-channel: Grad/Curl), explicitly enumerated in a table (`§Flux-channel variant axis`) with both channels' flux map, spaces, and L0 ctor cited, and correctly characterized as a closure-absorbed parametric axis (not a hidden body branch). The Grad+Curl "composite" is correctly scoped OUT as NOT a third verb — it is an elementwise `linear_combination`/`axpy(1,·)` over squared indicator vectors (`:536`/`:566`, both verified), resolving the c121 OQ. The complex-vs-real element-type axis is covered (`§Semantics` complex two-pass, `:254-260`). No hidden branch. Pass.

**cross-reference-integrity — pass.** Every `[link]` resolves on disk: `apply_linop`, `ksp_solve`, `nrm2`, `fe_space`, `interpolator`, `libceed-quadrature-kernel-impl` (all `L1/`), `fe-assemble-libceed-boundary-obstruction`, `amr-estimate-mark-refine` (both `L1-L0/`), `semantics/index.md`. The cited theme `amr-estimate-mark-refine.md` independently names `flux_recovery_estimate` as its estimate stage and cites the SAME `:184-268`/`:273-378`/`:391-500` ranges as `cites-evidence` (verified by grep) — the verb↔theme correspondence is real. Rank-invariant (graded-stack check 9): the three `depends-on (uses)` deps `ksp_solve`/`apply_linop`/`nrm2` are all `firm` (rank 3), so a `firm` entry resting only on firm deps satisfies `rank(u) ≤ rank(v)`. The `reference`-class edges (libceed-boundary obstruction, amr theme, fe_space, interpolator, kernel-impl) constrain nothing (correctly typed `reference`/`uses`). The kernel-api leaf is referenced not depended-on, consistent with DIRECTIVE-3 (verb is a consumer, not the realization). Reachability (check 10): the verb is reachable via the AMR consumer chain (DIRECTIVE-2 grounded consumer-(2)). Pass.

**edge-label-fidelity — pass.** The chapter declares it is the L1>L0 estimate stage of `amr-estimate-mark-refine`; the prose discusses exactly that edge (`ComputeErrorEstimates` L0 body lifted to the L1 verb). No mismatched edge label.

**plan-kind-consistency — pass.** Declared kind is a firm L1 operator harvest; content shape matches — full Signature/Semantics/Laws/Evidence with no rough-in placeholders. The `firm` claim is justified via the firm-on-positive-structure escape: every law is a syntactic identity / squared-norm / operator-algebra fact read off fully-specified positive source (the recovery projection, the per-element reduction, both channel ctors all read in full), and the no-dedicated-test caveat correctly does not gate syntactic-identity laws (the documented `apply_linop`/`jacobi-smoother`/`reciprocal` precedent). The two opaque sub-parts (libCEED integral, ksp_solve convergence) are referenced kernel-api/firm-constituent boundaries, NOT reconstructed claims, so `firm` (not `partly-constructive`) is correctly chosen. The build-readiness fence guard (check 5 sub-guard) holds: the firm body (`## Status` + Signature + Algebraic laws + Evidence) is fully ENCLOSED inside the `new:book/src/L1/flux_recovery_estimate.md` fence; no firm apparatus authored outside the fence.

**skill-uptake-survey — pass (telemetry).** The report's `§Supporting evidence` references a citecheck on-disk `--anchor` self-verification pass — the expected skill for a citation-heavy harvest. (Note the irony surfaced under citation-validity: the self-reported anchor pass listed `FluxProjector::Mult :170 [ok]` — the function signature line IS at `:170`, but the interior `Flux->Mult`/`ksp->Mult` call lines the report actually cites at `:180`/`:181` were NOT re-anchored and are off by -4. The anchor survey checked the wrong line within the block. Surfaced, non-blocking.)

### Issues found

1. **`book/src/L1/flux_recovery_estimate.md` §Semantics step 1, §Dependencies, §Evidence — `FluxProjector::Mult` interior pinpoints `:180`/`:181` are -4 drifted; block over-reaches.** The report cites `Flux->Mult(x, rhs)` at `:180` and `ksp->Mult(rhs, y)` at `:181`, and repeats the `:170-181` block range. On-disk (confirmed by direct `Read`): `Flux->Mult(x, rhs)` is `:176`, `ksp->Mult(rhs, y)` is `:177`; the `Mult` body is `:170-178` (closes at `:178`). Lines `:180-181` are `namespace {` + blank — the cited pinpoints land OUTSIDE the function on unrelated lines, and the `:170-181` block over-reaches into the following anonymous namespace. Severity: moderate (the load-bearing "the projection is `Flux->Mult` + `ksp->Mult`" anchor points at the wrong lines; the claim itself is correct). Correct: block `:170-178`, `Flux->Mult` `:176`, `ksp->Mult` `:177`.

2. **`book/src/L1/flux_recovery_estimate.md` §Semantics step 1, §Record definition table, §Evidence — `ksp` configuration pinpoint `:165` is -2 drifted.** The report cites the Krylov solver configuration at `:165` in three places. On-disk: `ksp = ConfigureLinearSolver<OperType>(...)` is at `:163`. Severity: minor. Correct: `:163`.

3. **`book/src/L1/flux_recovery_estimate.md` §Semantics step 2 + §Algebraic laws law 2 — zero-init pinpoint `:209-210` is wrong (actual `:211`).** The report says `estimates` is "initialized to zero at `:209-210`" (and law 2 cites `:209-210` for zero-init). On-disk: `:209` is `Vector estimates(mesh.GetNE());`, `:210` is `estimates.UseDevice(true);`, and the actual `estimates = 0.0;` is at `:211`. The cited range stops one line short of the zero-init it claims to anchor. Severity: minor. Correct: zero-init at `:211` (allocation+init block `:209-211`).

4. **`book/src/L1/flux_recovery_estimate.md` §Algebraic laws law 1 — "non-overlapping entries" comment pinpoint `:248` is -3 drifted.** The report cites the comment "Each thread writes to non-overlapping entries" at `:248`. On-disk it is at `:245`. Severity: minor. Correct: `:245`.

5. **`book/src/L1/flux_recovery_estimate.md` §Evidence + §Status — `CeedOperatorApplyAdd` `:252-254` and complex two-pass `:240-258` are off by ~1 at the boundaries.** The first `CeedOperatorApplyAdd` call spans `:251-253` (report `:252-254`; `:252` is in-range so the anchor token is hit); the second (complex) apply is `:258-260` (report's `:240-258` range stops at `:258`, one line short of the call's close). Severity: minor (block ranges substantially correct; flagged for precision). 

6. **`book/src/L1/flux_recovery_estimate.md` §Evidence — `errorestimator.hpp` class end-lines over-reach.** The report cites `errorestimator.hpp:65-94` (Grad class), `:98-130` (Curl class), `:34-55` (FluxProjector class), wrapped as `:34-130`. Codemap symbol defs report Grad class `:65-92`, Curl class `:98-125`, FluxProjector class `:34-56`. Start lines exact; end lines over-reach +2 to +5 (still in-file, citecheck-passing). Severity: low. Correct end lines: Grad `:92`, Curl `:125`, FluxProjector `:56`.

7. **`book/src/L1/flux_recovery_estimate.md` §Supporting evidence — informal "√ epilogue at `:386`/`:506`" misstates the Curl Sqrt line.** The Curl `linalg::Sqrt` energy epilogue is at `:508` (verified via `search_text`), not `:506`. The load-bearing law-5 citation uses `:386` (Grad, correct) and the Curl block `:503-506` is in-bounds for the Curl `AddErrorIndicator` function (`:503-509`), so no chapter claim is wrong — this is only the informal self-verification note. Severity: low (informal note only). Correct: Curl Sqrt `:508`.

8. **Non-issue, noted for the integrator (NOT a defect): SUMMARY edit references a not-yet-existing intro `./L1/amr-estimate-mark-intro.md`.** The proposed `edit:book/src/SUMMARY.md` adds a group header pointing at `book/src/L1/amr-estimate-mark-intro.md`, which does NOT exist on disk (verified) — a live link to a missing file is a hard `linkcheck2` error. HOWEVER the report EXPLICITLY flags this (the SUMMARY note + OQ `amr-estimate-mark-group-intro-needs-authoring`) and instructs the fallback: register the chapter FLAT under the L1 Part if the intro does not land this cycle. This is a correctly-flagged integrator routing instruction with a safe fallback, not a report defect — surfaced here so the integrator applies the flat-registration fallback rather than the group-header edit. (The `layer-intro-author` owns the intro page.)

---

## Repair

### Fixes attempted

**citation-validity — repaired.** The single warning was an interior-pinpoint drift cluster (all 27 citations clear `citecheck --scan` bounds; the drift is fine-grained pinpoint slip *inside* otherwise-correct block ranges). The critic confirmed none invalidate a claim (warning, not fail). Each correction was re-verified against on-disk `reference/palace/palace/linalg/errorestimator.{cpp,hpp}` via direct `Read` (NOT `read_range`, per its +1 brace drift) + codemap `search_text` / `get_symbol_def` (NOT relied on for `.cpp` interior lines). All applied surgically across CYCLE.md (no claim text touched, pinpoints only):

- **Finding 1 (moderate):** `FluxProjector::Mult` interior calls `:180`/`:181` are -4 drifted and the `:170-181` block over-reaches past the body close.
  - **Decision:** repaired.
  - **Action:** verified on-disk — body `:170-178` (closes `:178`), `Flux->Mult(x, rhs)` `:176`, `ksp->Mult(rhs, y)` `:177` (`:180-181` are `namespace {` + blank). Fixed block `:170-181`→`:170-178` in §Summary, §Semantics step 1, §Status, §Evidence, and the dep-map NEW row; `Flux->Mult` `:180`→`:176` and `ksp->Mult` `:181`→`:177` in §Semantics step 1, §Evidence, §Dependencies (`ksp_solve` `:181`→`:177`, `apply_linop` `:180`→`:176`).
- **Finding 2 (minor):** `ksp` config pinpoint `:165` is -2 drifted.
  - **Decision:** repaired.
  - **Action:** verified `ksp = ConfigureLinearSolver<OperType>(...)` at `:163`. Fixed `:165`→`:163` in §Semantics step 1, §Record-definition table, §Evidence (FluxProjector ctor entry).
- **Finding 3 (minor):** zero-init pinpoint `:209-210` wrong (actual `:211`).
  - **Decision:** repaired.
  - **Action:** verified `:209` allocation `Vector estimates(...)`, `:210` `UseDevice`, `:211` `estimates = 0.0;`. Fixed §Semantics step 2 (now "allocated `:209-210` and initialized to zero at `:211`") and §Algebraic-laws law 2 (`:209-210`→`:211`).
- **Finding 4 (minor):** "non-overlapping entries" comment `:248` is -3 drifted.
  - **Decision:** repaired.
  - **Action:** verified comment at `:245`. Fixed §Algebraic-laws law 1 `:248`→`:245`.
- **Finding 5 (minor precision):** `CeedOperatorApplyAdd` `:252-254` / complex two-pass `:240-258` boundary slip.
  - **Decision:** repaired.
  - **Action:** verified first apply `:251-253`, complex `if constexpr` second-pass block `:254-260`. Fixed §Semantics step 2 (`:252-254`→`:251-253`), §Complex-fields prose (`:240-258`→`:254-260`), §libCEED-leaf (`:252-254`→`:251-253`), §Algebraic-laws law 2 (`:252-254`→`:251-253`), §Evidence ComputeErrorEstimates entry (libCEED `:252-254`→`:251-253`, complex `:240-258`→`:254-260`).
- **Finding 6 (low):** `errorestimator.hpp` class end-lines over-reach +2/+5.
  - **Decision:** repaired.
  - **Action:** verified via `get_symbol_def` — Grad `:65-92`, Curl `:98-125`, FluxProjector `:34-56`. Fixed §Record-definition prose (`:65-94`→`:65-92`, `:98-130`→`:98-125`) and §Evidence hpp line (wrapper `:34-130`→`:34-125`; `:34-55`→`:34-56`, `:65-94`→`:65-92`, `:98-130`→`:98-125`).
- **Finding 7 (low):** informal Curl Sqrt note `:506` misstates the line (`:508`).
  - **Decision:** repaired.
  - **Action:** verified Curl `linalg::Sqrt` at `:508`, Grad at `:386` (via `search_text`). Also corrected the per-channel `AddErrorIndicator` evidence ranges to enclose the Sqrt: Grad `:381-384`→`:380-388` (Sqrt `:386`), Curl `:503-506`→`:502-510` (Sqrt `:508`); §Signature caller-epilogue pinpoints `:382-384`/`:504-506`→`:386`/`:508`; §Supporting-evidence informal note `:506`→`:508` (Curl).

- **Finding 8 (non-issue, noted for integrator — not a defect, not repaired):** the `edit:book/src/SUMMARY.md` group header points at a not-yet-existing `./L1/amr-estimate-mark-intro.md`.
  - **Decision:** not-needed (no repair). The report itself ALREADY flags this and instructs the safe fallback (register `flux_recovery_estimate` FLAT under the L1 Part if the group intro does not land this cycle), plus OQ `amr-estimate-mark-group-intro-needs-authoring` routes the intro to `layer-intro-author`. This is a correctly-flagged integrator routing instruction, not a report defect. **Integrator action:** apply the flat-registration fallback rather than the live group-header edit (a link to a missing file is a hard `linkcheck2` error). The intro page is the `layer-intro-author`'s artifact.

### Unrepairable findings

None. The lone warning was a mechanical pinpoint-drift cluster fully within repair authority (off-by-small-offset citation line ranges); all corrections were verified against on-disk source and applied surgically without touching any claim text.

## Suggested resolution

`ready`. All eight checks are now `pass`/`repaired`/`not-needed`; no claim was ever invalidated (the surrounding block ranges were correct throughout, so the warning never approached `fail`). Note for the integrator: apply the **flat-registration fallback** for `flux_recovery_estimate` under the L1 Part (do NOT apply the `SUMMARY.md` group-header edit pointing at the missing `./L1/amr-estimate-mark-intro.md`) — the report flags this with a safe fallback and routes the intro page to `layer-intro-author` via OQ `amr-estimate-mark-group-intro-needs-authoring`.
