---
verifies: ./CYCLE.md
critiqued_at: 2026-05-28T2330Z
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
repaired_at: 2026-05-28T2345Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of "L1 partly-constructive→firm enactment — divfree-projector"

## Critique

### Checks run

**citation-validity — pass.** I re-verified the two load-bearing anchors via `read_range`.
`palace/fem/integrator.hpp:217` is exactly `// Integrator for a(u, v) = -(Q u, grad v) for u in H(curl) and v in H1.` (215=`};`, 216 blank, 217 the doc; class opens 218). `palace/fem/integ/mixedvecgrad.cpp:202` is exactly `auto ctx = PopulateCoefficientContext(space_dim, Q, transpose, -1.0);` — the cycle-014 `:203`→`:202` drift is correctly resolved (`:203` is the `AssembleCeedOperator` call, NOT the `-1.0`). The non-negated sibling at `:142` (`...transpose)`, no `-1.0`) and the `:199-200` `EvalMode::Interp/Grad` claims also check out. The `ksp` tolerance anchors are confirmed: `divfree.cpp:140`=`SetRelTol(tol)`, `:142`=`SetAbsTol(...epsilon())` — Edit 2's `:141`→`:140,142` correction is right. `test/unit/test-libceed.cpp:905-916` resolves (Palace `MixedVectorWeakDivergenceIntegrator` paired against `mfem::` in `AddIntegrators`). The `divfree.cpp:177` "subtract" intent comment + `+1.0` AddMult at `:180-181,185` are confirmed, grounding Edit 4's doc-tension note. All load-bearing pointers are real and in-range.

**surface-or-evidence — pass.** This is a refinement-shaped proposal that modifies surface (the L1 entry's Idempotence law, Non-law/sign bullet, Semantics paragraph, §Status, §Evidence, §Signature bullet, plus two L1/index.md cells) AND carries the positive-source evidence backing the status flip. Not a pure rotation_claim. The surface edits and the evidence are coupled.

**rotation-quality — pass (not a rotation report).** This enacts a status promotion, not an inter-layer rotation. The L1 form is unchanged in shape; only its evidence-grounding and status change. Marked pass as not applicable to a status-flip enactment.

**variant-axis-coverage — pass.** The `VecType ∈ {Vector, ComplexVector}` axis was already covered in the firm entry (component-wise real apply, `:159-184`); this enactment does not touch it. The sign-anchor edits are variant-uniform.

**cross-reference-integrity — pass.** Internal links (`./chebyshev-smoother.md`, `./ksp_solve.md`, `./eigsolve.md`, `../concepts/set_subvector_zero.md`) resolve; the two OQ slugs (`divfree-projector-partly-constructive-to-firm-enactment`, `divfree-weakdiv-sign-convention-l0-verify`) and the newly-surfaced `divfree-mult-doc-irrotational-vs-divfree-stale` are tracked. The cycle-014 audit report dir is correctly referenced.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried; this is an intra-L1 status flip. Not applicable.

**plan-kind-consistency — pass.** Declared kind (partly-constructive→firm enactment) matches content shape: it consumes the cycle-014 UNBLOCK-PROMOTION verdict, applies the prescribed firming edits, and drops the caveat. The firm flip is genuinely warranted — see Issues for the residual-caveat analysis (the `ksp`-tolerance and empty-boundary residuals are correctly NOT treated as partly-constructive blockers).

**skill-uptake-survey — warning.** The report's shape (re-verify a `:203`→`:202` citation drift; confirm in-range anchors before a firm flip) is the exact use case for the `verify-citation-range` skill — which CLAUDE.md notes was extended cycle-012 with an "Audit-report / inherited-citation sub-case" section precisely for consuming an upstream audit's anchors. The report does the verification (re-`read_range`) but does not reference invoking the skill. Pure telemetry; non-blocking.

### Issues found

1. **(skill-uptake, low) `verify-citation-range` invocation not referenced** — CYCLE.md §"Anchor re-confirmation" performs the inherited-citation re-verification by hand without citing the `verify-citation-range` skill's audit-report sub-case. Surfaces telemetry only; the verification itself is correct and complete.

2. **(plan-kind / informational, non-blocking) firm flip is fully warranted — no residual contingency keeps it partly-constructive.** I scrutinized whether any residual caveat should retain `partly-constructive` status. It should not:
   - The cycle-013 `partly-constructive` gate named exactly ONE contingent sub-part: the idempotence law `P∘P=P` + divergence-free characterization, contingent on the `WeakDiv ≈ -GᵀM` sign reading. That reading is now positively anchored in Palace-owned source (`integrator.hpp:217` + `mixedvecgrad.cpp:202`, both re-verified above). The single named contingency is resolved at the evidence level. Per the cycle-012 codification, the promotion condition ("an upstream positive source site") is met exactly.
   - The **`ksp`-tolerance "modulo" caveat** ("`GᵀM(P·y)=0` only up to convergence tolerance") is NOT a partly-constructive contingency — it is a property of the *approximate solve* that applies identically to the Linearity law (which was always firm) and to every solve-to-tolerance operator (cf. `ksp_solve` firm). It is a normal "holds in exact arithmetic; modulo ksp tolerance" qualifier, not a negative-anchor caveat. Correctly retained as prose, not as a status gate.
   - The **empty-boundary pin** (`divfree.cpp:51-81`) is absorbed into `P` at construction and was never part of the named contingent sub-part; it does not bear on the firm flip.
   - The newly-surfaced `divfree-mult-doc-irrotational-vs-divfree-stale` is a Palace-internal *documentation* inconsistency (the `Mult` doc-comment `divfree.hpp:64-66` says "irrotational … ∇×y=0" vs the class doc's divergence-free target), explicitly carried as a non-blocking OQ and recorded in-line by Edit 4. It does not re-introduce semantic contingency.
   No residual caveat warrants retaining `partly-constructive`. The flip to `firm` is sound.

3. **(consistency, pass) L1 firm-count delta + dep-map cell are consistent.** Current L1/index.md reads `**Firm (10)**` (line 29) and the divfree dep-map row (line 74) reads `partly-constructive`. Edit 7 flips the row to `firm` with the positive-anchor citation; Edit 8 bumps the cohort header to `**Firm (11)**` and appends the firm bullet. 10→11 matches a single operator promotion; no other row changes. Internally consistent.

4. **(scope hygiene, informational) deferred anchor-hygiene edits acknowledged.** The report explicitly defers three cycle-014-flagged non-load-bearing off-by-ones (`divfree.hpp:68-72`→`:67-71`, `:28-31`→`:27-30`) to a later lifter/repairer pass to avoid prose churn in a status-flip enactment. This is a reasonable scope boundary, not a defect; noted so the integrator/repairer can track the residual. (The one load-bearing-adjacent off-by-one, `:141`→`:140,142`, IS fixed in Edit 2 — confirmed correct.)

## Repair

### Fixes attempted

- **Finding**: (skill-uptake, low) `verify-citation-range` invocation not referenced — CYCLE.md §"Anchor re-confirmation" performs the inherited-citation re-verification by hand without citing the `verify-citation-range` skill's audit-report sub-case.
  - **Decision**: not-needed
  - **Rationale**: Pure telemetry per the critic. The verification itself (re-`read_range` of both load-bearing anchors `integrator.hpp:217`, `mixedvecgrad.cpp:202`) is correct, complete, and in-range; the missing skill-invocation breadcrumb does not alter the report's content or the firm verdict. Acknowledged as a skill-uptake signal for the batch-3 meta-phase; not a CYCLE.md edit (adding a retroactive skill-invocation note would be authoring, not a mechanical fix).

- **Finding**: (plan-kind / informational) firm flip is fully warranted — no residual contingency keeps it `partly-constructive`.
  - **Decision**: not-needed
  - **Rationale**: Critic-confirmed `pass`. The single cycle-013-named contingency (idempotence sub-law `P∘P=P` + divergence-free characterization, contingent on the `WeakDiv ≈ -GᵀM` sign) is now positively anchored in Palace-owned source, re-verified by both critic and producer. The `ksp`-tolerance "modulo" and empty-boundary qualifiers are correctly NOT treated as status gates. No edit warranted.

- **Finding**: (cross-reference, pass) newly-surfaced documentation-tension OQ `divfree-mult-doc-irrotational-vs-divfree-stale` (the `divfree.hpp:64-66` "irrotational … ∇×y=0" `Mult` doc-comment vs the established divergence-free sign).
  - **Decision**: not-needed
  - **Rationale**: Confirmed recorded as a non-blocking carry-forward OQ. The slug is already referenced in two existing `scaffolding/open-questions.md` entries (cycle-013 `divfree-weakdiv-sign-convention-l0-verify` follow-up + cycle-014 audit OQ, the latter explicitly recommending it be filed), and CYCLE.md §"Open questions / caveats" item 3 + Edit 4 record it in-line with the correct anchors. The standalone ledger entry is the integrator's append (outside repairer write authority; `open-questions.md` is integrator-per-report-owned). Not a content tension to resolve — it is a Palace-internal documentation inconsistency correctly left as an OQ. No repairer action.

### Unrepairable findings

None. No finding required substantive authoring or contradicted artifact content; the sole non-pass finding (skill-uptake) is non-blocking telemetry.

## Suggested resolution

`ready`. The firm flip is fully warranted — all 8 critic checks pass except the non-blocking skill-uptake telemetry warning, both load-bearing sign anchors (`fem/integrator.hpp:217`, `fem/integ/mixedvecgrad.cpp:202`) re-verified, the cycle-014 `:203`→`:202` drift correctly resolved, and the `:141`→`:140,142` abs-tol off-by-one fixed in Edit 2. No mechanical defects.

Notes for the integrator:
- On application, close OQ `divfree-projector-partly-constructive-to-firm-enactment` and confirm-closed OQ `divfree-weakdiv-sign-convention-l0-verify` (resolved by the cycle-014 audit this dispatch consumes).
- Ensure the doc-tension OQ `divfree-mult-doc-irrotational-vs-divfree-stale` exists as a standalone `scaffolding/open-questions.md` entry (currently only referenced from related entries; the cycle-014 audit recommended filing it). Non-blocking.
- The deferred non-load-bearing anchor-hygiene off-by-ones (`divfree.hpp:68-72`→`:67-71`, `:28-31`→`:27-30`) remain open for a later lifter/repairer pass — track but do not block.
- L1 firm-count delta 10→11 (Edit 8) is consistent with the single-operator promotion; no other dep-map rows change.
