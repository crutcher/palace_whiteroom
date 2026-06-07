---
verifies: ./CYCLE.md
critiqued_at: 2026-06-07T101500Z
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
overall_status: ready
---

# META: verification of the libceed + eigsolve realizes-kernel-api correspondence audit (cycle-122 D6)

## Critique

### Checks run

**citation-validity — pass.** I independently re-verified every load-bearing anchor against the
Palace source (palace-codemap `read_range` for the source tree; direct on-disk `sed` for the
single-`palace/` test tree). The decisive eigsolve anchor `slepc.cpp:635
EPSSetType(eps, EPSKRYLOVSCHUR)` lands EXACTLY (read 630-654: line 635 is the `KRYLOVSCHUR` arm;
zero drift) — the audit's verdict rests on this and it is solid. The shared libceed pivot
`integrator.hpp:58-61` is the `BilinearFormIntegrator::Assemble(...) const = 0;` pure-virtual,
exact (read 56-62). `integrator.cpp:423-427` `AssembleCeedOperator` master-assembler signature with
the six `trial_restr/test_restr/trial_basis/test_basis/geom_data/geom_data_restr` inputs — exact.
The empirical anchor `test-libceed.cpp:284` is `TestCeedOperatorFullAssemble` and `:298` is the
`mat_diff->MaxNorm() < 1.0e-12 * std::max(mat_ref.MaxNorm(), 1.0)` assert — both confirmed on disk
at `reference/palace/test/unit/...` (single-`palace/`, NOT doubled — the report's path-convention
note is correct). slepc `:687-709` Solve (`:693 Customize`, `:694 EPSSolve`, `:695 EPSGetConverged`,
`:707 RescaleEigenvectors`), `:734 EPSGetBV`, and `:602-628` problem-type (`:607 EPS_HEP`,
`:610 EPS_NHEP`, `:613 EPS_GHEP`, `:616 EPS_GHIEP`, `:619 EPS_GNHEP`) all verify exact. ARPACK
`:270 iparam[2]=arpack_it`, `:273 iparam[6]=sinvert?3:1`, `:278 which::largest_magnitude`,
`:318 naupd`, `:315 while(true)` all exact. **The ARPACK off-by-one nit is CORRECT and I confirmed
it independently:** reading 315-339, the `ido==99` block is `:331` (`else if (ido==99)`) → `:332` `{`
→ `:333 break;` → `:334` `}`, i.e. `:331-334`, while the original framing cited `:330-333` (`:330`
is the `ido==2` close-brace). The break at `:333` IS in-range, so the claim is supported — this is a
1-line range-start tidy, non-load-bearing, exactly as the report classifies it. Finally, both
proposed `verified_against:` YAML blocks (8 + 7 entries) round-trip cleanly under
`yaml.safe_load` and no `note:` value opens with a quote of either kind (the round-trip sub-check
passes).

**surface-or-evidence — pass (adapted for the audit kind).** This is a lowering-verifier
correspondence audit, not a refinement-shaped proposal. Its surface is the two append-only
`verified_against:` blocks (retroactive-evidence backfill, explicitly allowed) plus the routed
findings; no operator/theme algebra is mutated. The audit's evidence shape is correct for a
DIRECTIVE-3 correspondence review: it backs the `realizes-kernel-api-faithful` verdict with the
shared pivot anchor + the per-stage L0 sites + the deferred empirical target, which is the right
structural-audit posture for a rank-0 (roadmap_goal) impl pair. No signature-named record is
introduced. Pass.

**rotation-quality — pass (not applicable to the audit kind).** A correspondence audit asserts no
new algebraic/reduction rotation of its own; it verifies the impl↔API correspondence. No-op,
analogous to the feature-surface/stub no-op. Pass.

**variant-axis-coverage — pass.** The audit does not introduce variant axes; it reviews the impls'
existing axes (libceed: basis/diff-op/single-machine; eigsolve: eigen-algorithm / problem-symmetry /
spectral-transform / problem-type / restart-shape) and confirms each is grounded in a verified
anchor (`SetProblemType` `:602-628`, `SetType` `:630-654`, `EvalMode` `integrator.hpp:14-23`). The
single-machine and GSLIB-carve-out scoping is explicit and consistent with project scope. No hidden
branch. Pass.

**cross-reference-integrity — pass.** The `realizes-kernel-api` reference edges, both API obstruction
statuses, and both impl ranks were re-confirmed against the on-disk chapters: libceed impl
`rank: roadmap_goal`, `realizes-kernel-api` + `realizes-leaf` both under `reference:` (free), depends-on
= the four substrate ops only; eigsolve impl `rank: roadmap_goal`, depends-on =
krylov-step/lanczos_step/ksp_solve/apply_linop/orthogonalize, reference =
`realizes-kernel-api → {L3/eigsolve, L4/eigsolve}`. API surfaces: libceed `status: obstruction,
sub_kind: opaque-library-ownership`; eigsolve `firmness: partial-obstruction` — both undowngraded.
All four audit-target chapters + `L4/eigsolve` exist on disk; eigsolve's firm constituents
(krylov-step/ksp_solve/apply_linop firm, orthogonalize rank firm, lanczos_step roadmap_goal) all
resolve. The stale-prose finding is correctly routed (NOT applied) to the integrator/repairer with a
clear before/after and a same-file SEQUENTIAL rationale. The `verified_against:` blocks are
append-only at end-of-file (no body mutation of the audit targets). Pass. (See the one informational
note below re the four libceed substrate ops being off-disk at audit time — correctly disclosed, not
a defect.)

**edge-label-fidelity — pass.** Both `realizes-kernel-api` edges are `reference`-class and the prose
discusses exactly those edges (impl → opaque-API contract, navigational/free, NOT depends-on, does
not constrain rank or carry liveness). The audit correctly distinguishes `realizes-kernel-api` from
the libceed `realizes-leaf` edge (impl → firm `fe_assemble` fold) and recommends keeping them
distinct as free documentation — sound, since the linters ignore the `kind:` token. The eigsolve
sibling `realizes-kernel-api → L4/eigsolve` is likewise reference-class and so labeled. No
edge-label/prose mismatch. Pass.

**plan-kind-consistency — pass.** Declared kind is an audit; content is an audit (per-citation
verification tables, linkage-integrity checks, FAITHFUL verdicts, routed non-blocking findings). The
rank-invariant / reachability framing is applied correctly for two rank-0 roadmap_goal impls (the
graded-stack `[GARBAGE*]` disposition is the intended grounded-future state pending the blocking
RE3/RE8 consumers, correctly read as not-a-defect). No firm-claim-with-placeholder mis-classification.
Pass.

**skill-uptake-survey — pass (telemetry only).** The audit invokes the citecheck/codemap localization
discipline and the `verified_against:` YAML round-trip self-check (notes confirmed quote-free), and
references `lifter-scope-content-correction-boundary` for the carry-forward range correction. Adequate
skill surfacing for the shape. Pass.

### Issues found

No blocking or warning issues. All eight checks pass; this is an all-pass clean report and I set
`overall_status: ready`.

Informational (no severity; verified as correctly-disclosed, NOT defects):

- **Four libceed substrate depends-on targets (`L1/element_restrict`, `L1/basis_apply`,
  `L1/quad_point_contract`, `L1/geom_factor_build`) are absent from disk at audit time** (confirmed
  MISSING). This is the expected Wave-2 mid-cycle state — they live in the D4 harvester report's
  proposed-changes (integration is Phase 5), and the report explicitly audits the correspondence
  against D4's authored substrate semantics and flags the resulting `[UNRESOLVED]` linter edges as
  the expected transient. Not a citation-validity or cross-reference failure for this report; the
  linker will resolve once D4 lands.
- **Stale-prose finding in the libceed consumer is genuine** — I confirmed the impl's depends-on NOTE
  (frontmatter ~lines 33-39) tags each substrate target "(rough-in; no anchor yet)", which is stale
  if D4 authored them as `roadmap_goal` with anchors. Correctly routed as a navigational re-anchor
  (text refresh, edges/rank unchanged), not applied — the right disposition for a same-file-SEQUENTIAL
  audit target.
- **ARPACK `:330-333` → `:331-334` carry-forward** — independently confirmed correct; non-load-bearing
  (break at `:333` is in-range), routed to a future lifter, does not affect the audit verdict.
