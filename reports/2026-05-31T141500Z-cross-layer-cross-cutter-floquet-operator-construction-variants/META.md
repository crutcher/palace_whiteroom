---
verifies: ../CYCLE.md
critiqued_at: 2026-05-31T14:30:00Z
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
repaired_at: 2026-05-31T14:45:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: repaired
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: unrepairable
overall_status: ready
follow_up_agent: null
---

# META: verification of cross-layer-cross-cutter floquet-correction-operator-construction-variants

## Critique

### Checks run

**citation-validity**: PASS. Ran `tools/citecheck/citecheck.py --scan` over the full report — **43 ok, 0 failing**. Spot-verified load-bearing pinpoints with `--anchor`: `floquetcorrection.cpp:72-85` resolves with `Cross->Mult` at line 76 (the Mult body); `:79-85` resolves with `this->Mult` at 83 and `AddMult` at 81 (the AddMult body); `apply-linop-mutation-rotation.md:43-81` resolves `Sub-pattern A` at 43; `:127-172` resolves `Sub-pattern D` at 127; `mutable-workspace-pattern.md:80` resolves `floquetcorrection` at 80; `apply-linop-overload-set.md:33` independently read and the non-exhaustive caveat the report relies on is verbatim present on line 33 ("A non-exhaustive list. Other operator-shaped types in Palace … all implement the same interface; the overload-set shape is uniform."). Direct on-disk read of `floquetcorrection.cpp:73-86` confirms the Mult body is `Cross->Mult(x, rhs); ksp->Mult(rhs, y);` and the AddMult body is `this->Mult(x, rhs); rhs *= a; y += rhs;` — bit-for-bit as quoted in the report. Direct read of `floquetcorrection.hpp:32-60` confirms the class exposes ONLY `Mult` and `AddMult` (no transpose / hermitian variants). `grep -n "floquet_corr" drivensolver.cpp` confirms the three AddMult sites at lines 212/336/468 and the one eigensolver site at 454 — the report's mid-sentence self-correction at line 75 ("actually three in drivensolver and one in eigensolver = 4 sites") is arithmetically accurate. No `verified_against:` block present (cross-cut observation report, no proposed-changes); YAML round-trip sub-check inapplicable.

**surface-or-evidence**: PASS. This is a cross-layer observation dispatch (no `book/` mutation, no proposed-changes block). The MATCH claim (`FloquetCorrSolver::Mult/AddMult` bit-for-bit match sub-patterns A/D) is evidence-backed: direct quotation of both bodies + signature comparison vs the sub-pattern A/D Haskell-style headers. The structural-isomorphism claim vs `divfree-projector` is grounded by independent read of `book/src/L1/divfree-projector.md:25-37` (confirms "constructed-operator gate", one nested `ksp` gate, closure-bound workspace, family-membership prose) and `book/src/L1-L0/divfree-projector-mutation-rotation.md:52-148` (confirms the sub-pattern A composition template that the new Floquet theme would port). Confirmed via `book/src/concepts/nested-constructed-operator-gate.md:62-89`: exactly 2 firm instances (`eigsolve`, `divfree-projector`) — the report's "third firm instance" framing is correct.

**rotation-quality / observation-soundness**: PASS. The negative finding (`apply_linop` needs no extension) is sound on multiple grounds: (a) `FloquetCorrSolver` does NOT inherit from `Operator`/`ComplexOperator` — it is a standalone constructed-operator class that *exposes the same overload-set surface*; the `apply-linop-overload-set.md:33` non-exhaustive caveat explicitly covers "Other operator-shaped types in Palace … the overload-set shape is uniform"; (b) the Mult body has NO apply-shape variant the survey could have missed — no per-step complex phase shift, no per-step scalar multiplication, no per-step transpose. The Floquet phase factor lives in the *wave vector* `kp` (a static construction-time material property — `mat_op.GetFloquetCross()` at `floquetcorrection.cpp:40-57`), NOT in any per-apply phase rotation. The cross-product `[kp ×]` matrix is built once at construction; per-apply is a pure `Cross->Mult` (a vanilla `apply_linop` instance on a constructed real/complex linop). The `M⁻¹` is solve-to-tolerance via the inner `ksp->Mult` (a vanilla `ksp_solve` gate-apply). Both inner calls have firm L1-L0 absorption in the existing themes. The two-line Mult + three-line AddMult body has no residual L0 patterns that the existing themes don't cover.

**variant-axis-coverage**: PASS. The report enumerates the variant axes correctly: (a) element-type axis (`VecType ∈ {Vector, ComplexVector}` template, only `ComplexVector` instantiated at `floquetcorrection.cpp:88`) — flagged explicitly in Open question #1 with two scoping options (deliberate-real-omission caveat vs. `rough-in (test-coverage-bounded)`); (b) transpose-mode axis — independently verified absent (header `:32-60` shows only `Mult` + `AddMult` declarations); the report correctly says sub-patterns B/C/E "do not need to apply." (c) MPI/Par axis — flagged in Open question #4 with the standard CLAUDE.md §Scope flag-once-skip + the divfree-projector precedent. No hidden branches; the survey is exhaustive at the apply surface.

**cross-reference-integrity**: PASS (with a small wording observation, not a failure). All `[link]` references in the report resolve to on-disk files: `apply-linop-mutation-rotation.md`, `apply-linop-overload-set.md`, `nested-constructed-operator-gate.md`, `divfree-projector.md`, `divfree-projector-mutation-rotation.md`, `mutable-workspace-pattern.md`, `jacobi-smoother.md` all exist. The `floquet-correction-mutation-rotation` slug is correctly referenced as not-yet-existing (proposed for the harvester landing). No proposed-changes block; no fence-parity / firm-body-inside-fence concern (NOT APPLICABLE to observation reports). Wording observation only: the report at line 28 says "*the matrix realization of `[kp ×]`*" — this is in-line prose, not a slug, so cross-reference-integrity doesn't fire on it.

**edge-label-fidelity**: PASS. The report's two-tier framing — "MATCH at the `apply_linop` tier" vs "GAP at the L1 `floquet_correction` tier" — is internally consistent. The L1>L0 edge for the proposed new theme is correctly labeled `floquet-correction-mutation-rotation` (an L1>L0 theme, matching the divfree-projector-mutation-rotation template). MPI/Par* scope correctly flagged once (Open question #4) with the standard CLAUDE.md §Scope reference + flag-once-skip discipline. No edge-label drift.

**plan-kind-consistency**: PASS. The observation correctly: (a) RESOLVES the apply_linop-extension dimension of the OQ `floquet-correction-operator-construction-variants` with a negative finding (no extension needed); (b) MIGRATES a concrete plan item `floquet-correction-l1-gate-harvest` rather than parking a new OQ, per the CLAUDE.md "intake feeds the plan, they don't hold work" invariant (cited verbatim at line 83); (c) does NOT enact the harvest itself — correct per cross-layer-cross-cutter role-spec (the harvester follow-up is a separate dispatch). The proposed L1 entry's fan-out + cost + variant-axis sketch + algebraic-laws-port guidance are all sized appropriately for a one-shot harvester landing. The dispatch is correctly labeled as "audit-mode classification" / pure cross-cut, no `book/` edits proposed (Open question #5).

**skill-uptake-survey**: WARNING (telemetry only — non-blocking, per role-spec "pure presence check"). The report would have benefited from explicit skill-invocation markers for the four skills that match the observation's shape: (a) `verify-citation-range` — implicit but not surfaced; (b) MCP-first localization — the report does cite a deep set of source ranges across `floquetcorrection.{hpp,cpp}` + the two driver files, consistent with `palace-codemap` localization, but no explicit `mcp__palace-codemap__search_text` / `get_call_sites` invocation log; (c) `establish-negative-finding-exhaustiveness` — the negative finding ("no apply-shape variant `apply_linop` should mention") is structurally argued via signature exhaustiveness (Mult + AddMult only; no transpose family) + non-membership in the `Operator`/`ComplexOperator` hierarchy + the existing non-exhaustive caveat. This is essentially the skill's procedure but not named; the skill's discipline (positive-anchors-for-the-non-implementation; negative-anchor enumeration) would have strengthened the negative finding's defensibility, especially the claim that "no real-branch instantiation" is a *deliberate* scope-out rather than an oversight. The promotion-condition framing in Open question #1 ((a)-deliberate vs (b)-test-coverage-bounded) is the right shape but could have been routed through the skill's procedure for sharper anchoring; (d) `phase-1-slice-reduction-audit` — N/A (no slice involved). Telemetry takeaway: cross-layer-cross-cutter observation dispatches that produce a negative finding on a coverage dimension should invoke `establish-negative-finding-exhaustiveness` to harden the negative anchor.

### Issues found

1. **Wording self-correction in the call-site arithmetic (line 75, severity: LOW, cosmetic only)** — the prose reads "one in `palace/drivers/eigensolver.cpp:454`, two in `palace/drivers/drivensolver.cpp:212, 336, 468` — actually three in drivensolver and one in eigensolver = 4 sites". The "two … 212, 336, 468 — actually three" mid-sentence self-correction reaches the right answer (4 total, independently verified by `grep -n "floquet_corr"` on drivensolver.cpp), but leaves the sentence with both the wrong-then-corrected count visible. The arithmetic conclusion is right; the prose flow is awkward. Cosmetic clean-up candidate at repair-time.

2. **Supporting-evidence line 108 mixes two reference kinds (severity: LOW, citation-presentation)** — the line reads "`palace/drivers/drivensolver.cpp:138-141, 212, 289-292, 336, 468`" combining (a) the *declaration / instantiation* sites at 138-141 and 289-292 (which `grep` confirms are `std::unique_ptr<FloquetCorrSolver<ComplexVector>> floquet_corr;` + `floquet_corr = std::make_unique<...>` lines) with (b) the *AddMult consumption* sites at 212, 336, 468. The line's prose framing ("three additional `floquet_corr->AddMult(E, B, 1.0 / omega)` sites") doesn't match the citation list (which includes the two declaration ranges). All cited line numbers are real / in-range (verified via `grep`), so this is a citation-presentation issue, not a citation-validity failure. The single citation-list could be split into "declaration sites: 138-141, 289-292" and "consumption sites: 212, 336, 468" for clarity.

3. **Variant-axis Open question #1 framing could be sharper (severity: LOW, framing)** — the "Element-type collapse vs. ComplexVector-only instantiation" Open question correctly identifies the template-vs-instantiation gap but defers the decision to the harvester. The cited Palace physics rationale ("Floquet phase factors are inherently complex") is correct (Floquet/Bloch theory inherently involves complex phase factors e^{ik·r}), but the report could have *anchored* this rationale — either via a Palace source site that documents the complex-only scope-out, or via the `establish-negative-finding-exhaustiveness` skill's procedure to confirm no `<Vector>` instantiation exists anywhere in the source tree (the report says "no `<Vector>` instantiation in source" but doesn't surface a grep-confirmed result). Stronger anchoring would let the harvester land the L1 entry with `firm` + a documented scope-out caveat rather than `rough-in (test-coverage-bounded)`.

4. **Skill-uptake telemetry: `establish-negative-finding-exhaustiveness` not invoked (severity: LOW, telemetry)** — see skill-uptake-survey check above. The observation makes a load-bearing negative claim (no apply-shape variant `apply_linop` should accommodate) but does not route it through the skill that exists for hardening such claims. Non-blocking — the negative claim is structurally sound — but a telemetry signal worth recording.

## Repair

### Fixes attempted

- **Finding 1 — call-site arithmetic self-correction (LOW, cosmetic)**
  - **Decision**: repaired
  - **Action**: edited CYCLE.md §"Is this a coverage GAP…" (the paragraph at the original line 75) to remove the visible mid-sentence "two … 212, 336, 468 — actually three" self-correction. The revised sentence reads "**four AddMult call sites total** — three in `palace/drivers/drivensolver.cpp:212, 336, 468` and one in `palace/drivers/eigensolver.cpp:454` (grep-verified)". Independently re-confirmed via `grep -n "floquet_corr" reference/palace/palace/drivers/{drivensolver,eigensolver}.cpp`: drivensolver consumption at lines 212/336/468; eigensolver consumption at 454; total = 4. Mechanical prose-flow cleanup; no analytical change.

- **Finding 2 — supporting-evidence line mixes declaration + consumption sites (LOW, citation-presentation)**
  - **Decision**: repaired
  - **Action**: split the single supporting-evidence bullet `palace/drivers/drivensolver.cpp:138-141, 212, 289-292, 336, 468 — three additional 'floquet_corr->AddMult' sites` into two separate bullets at CYCLE.md §"Supporting evidence" L0 block: (a) the two *declaration / instantiation* ranges `138-141, 289-292` with the `std::unique_ptr<FloquetCorrSolver<ComplexVector>> floquet_corr;` + `make_unique<...>` framing, and (b) the three *consumption* sites `212, 336, 468` with the `AddMult` framing. All line numbers were already grep-verified during the critic's citation-validity check; this is a presentation split only.

- **Finding 3 — Element-type Open question #1 anchoring could be sharper (LOW, framing)**
  - **Decision**: repaired
  - **Action**: added a one-line **negative-anchor grep** result to OQ #1 in CYCLE.md §"Open questions / caveats". Repairer-verified at repair time via `grep -rn "FloquetCorrSolver" reference/palace/` — the only instantiations anywhere in the source tree are `FloquetCorrSolver<ComplexVector>` (the explicit template instantiation at `floquetcorrection.cpp:88` + 5 `<ComplexVector>` use-sites across the two driver files); no `<Vector>` instantiation exists. Added the grep-confirmed framing + the noted lean toward option (a) (deliberate scope-out), while preserving the harvester's final-call authority on the scoping verdict. One-line additive verification; no analytical change.

- **Finding 4 — skill-uptake telemetry: `establish-negative-finding-exhaustiveness` not invoked (LOW, telemetry)**
  - **Decision**: unrepairable (acknowledged / not-repairable-in-place)
  - **Rationale**: this is a producer-time skill-invocation telemetry signal, not an artifact defect. The repairer cannot retroactively invoke a skill at authoring time; the artifact's negative claim is already structurally sound (PASS on rotation-quality / variant-axis-coverage / surface-or-evidence) and the Finding 3 repair partially compensates by surfacing the grep-confirmed negative anchor that the skill's procedure would have produced. Noted for the meta-phase: if cross-layer-cross-cutter observation dispatches that yield negative findings on coverage dimensions repeat this pattern (skill-uptake-survey WARNING for `establish-negative-finding-exhaustiveness` non-invocation), the meta-phase may want to consider amending the cross-layer-cross-cutter role-spec to mandate explicit invocation when the observation produces a negative coverage finding. Not a friction-ledger candidate on a single occurrence; logging here for meta-phase aggregation.

### Unrepairable findings

- **Finding 4 (skill-uptake-survey WARNING)** — telemetry-only, not artifact-fixable. No follow-up agent required for THIS report; the meta-phase aggregates across the 3-cycle batch and may choose to act if the pattern recurs.

## Suggested resolution

`overall_status: ready`. The load-bearing content survives intact: (a) clean MATCH on `apply_linop` (no extension to `apply-linop-mutation-rotation` or `apply-linop-overload-set` needed), backed by signature exhaustiveness + non-membership in the `Operator`/`ComplexOperator` hierarchy + the existing non-exhaustive caveat; (b) the `floquet-correction-l1-gate-harvest` plan-migration recommendation (plan-item-not-OQ, per the "intake feeds the plan" invariant) routed to `harvester` with the divfree-projector precedent as the template, sized as low-to-medium fan-out / small cost / third firm instance of `nested-constructed-operator-gate`.

Notes for the integrator:
- This is a survey/observation report; `integrator-per-report` should NOT expect a `book/` proposed-changes block. The integration actions are: (i) close the OQ `floquet-correction-operator-construction-variants` as resolved with a link to this report; (ii) append the new plan candidate `floquet-correction-l1-gate-harvest` to `scaffolding/priorities.md` Backlog with the rank/tag/scope sketch from CYCLE.md §Recommendation item 2.
- No build-impact (no `book/` changes); finalize need not check `cargo make book` for this report's own surface.
- The repaired CYCLE.md additions are surgical (3 in-place edits at lines around the original 75 + 108 + the OQ #1 paragraph); the supporting-evidence split adds one bullet (net +1 line in the L0 evidence block).
- Cycle-planner / meta-phase: telemetry from Finding 4 is logged above for batch aggregation; no immediate enactment needed.
