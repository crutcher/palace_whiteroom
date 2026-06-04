---
verifies: ../CYCLE.md
critiqued_at: 2026-06-04T022442Z
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

# META: verification of "Audit matrix-weighted-norm — norm-axiom law-confidence probe"

## Critique

### Checks run

**citation-validity — pass.** Every citation was resolved and verified against the live source via `read_range`, and the load-bearing SPD-premise trace was checked end-to-end. The three crux citations confirm exactly:
- `palace/drivers/eigensolver.cpp:205-213` — the comment "the real **SPD part of the mass matrix**" sits at lines 205-207; `KM = space_op.GetInnerProductMatrix(0.0, 1.0, nullptr, M.get())` at :212; `eigen->SetBMat(*KM)` at :213. Verified verbatim.
- `palace/models/spaceoperator.cpp:530-537` — `GetInnerProductMatrix(a0, a2, K, M)` returns `BuildParSumOperator({a0,a2},{... PtAP_M->Real()})`; called as `(0.0, 1.0, nullptr, M)` it yields `1.0·M->Real()`, the real part of the FE mass matrix. Verified.
- `palace/linalg/operator.cpp:599-619` — real √ at :606, complex √ at :618, asserts at :604/:616, the comment `// For SPD B, xᴴ B x is real.` at :612. Verified.
The `citecheck --scan` returned 16 ok / 1 "failing", where the single non-ok is an `[AMBIG]` on basename `operator.cpp` (collides with `fem/libceed/operator.cpp`); the report consistently qualifies it as `palace/linalg/operator.cpp` in prose, so the AMBIG is a tool basename-collision artifact, not a bounds/drift defect — all bounds resolve in-range. The gate-(a) test-absence claim was independently reproduced: `grep -rn Norml2 reference/palace/palace/test/unit/` returns ZERO hits. The intended merged `verified_against:` block was extracted and round-tripped under `yaml.safe_load` (4 entries, clean); all new `note:` scalars begin with prose (`cycle-088 ...` / `GetElectricFieldEnergy ...`), satisfying the no-leading-quote rule.

**SPD-trace crux — confirmed complete (the DISCHARGE verdict is NOT over-claimed).** The dispatch's central worry was whether a different (merely-PSD or indefinite) operator could reach `Norml2`'s `opB` in some usage. I enumerated every `SetBMat` callsite (`search_text "SetBMat"`): the only two *driver-level* `SetBMat` calls are `eigensolver.cpp:213` and `:419`, and BOTH pass `*KM` where `KM = GetInnerProductMatrix(0.0, 1.0, nullptr, M.get())` — the SPD mass form (the :419 site is the "normalize finalized eigenvectors w.r.t. mass matrix" path, same `KM`). The backend `SetBMat` overrides (arpack/slepc/nleps) merely store `opB = &B`; `GetEigenvectorNorm` (arpack :433-444, slepc :470-481) routes to `linalg::Norml2(comm, x, *opB, Bx)` only when `opB` non-null. So across the entire eigensolver corpus the `B` reaching the weighted `Norml2` is uniformly the SPD `KM`. The trace is complete and the verdict's "provably SPD by construction, not merely PSD" holds. The report itself correctly preserves the only genuine residual caveat (Open-questions: a hypothetical future *non-eigensolver* caller passing a non-SPD `B` would void the premise — recorded, not over-claimed).

**surface-or-evidence — pass.** This is a refinement that modifies surface (the §Status gate-(c) bullet text + the `verified_against:` block) AND carries rotation/evidence backing (the literature-anchor derivation + the SPD premise's positive L0 home). The legitimacy question — is the literature anchor an in-scope law-confidence anchor, or is it smuggling an unverified positive claim? — resolves in favor of the report. The discharge is correctly SCOPED to the *structure-side* (exact-arithmetic validity of laws 4/6/7 as inner-product-space theorems that follow once the SPD premise is established), and the SPD premise genuinely HAS a positive L0 home (`eigensolver.cpp:206-207` + `spaceoperator.cpp:530-537`). The report does NOT claim the FP sub-claims (`:69-70` ULP strict-CS, bit-determinism) are discharged — those stay test-bounded, which is exactly why the verb is held at rough-in. This is the structure-side analog of the firm-on-positive-structure escape (a positive structural read discharging a derivable consequence), correctly framed as "one inferential step removed" via the SPD premise rather than a syntactic identity — and the report explicitly marks the discharge PARTIAL and does not promote, which is the conservative reading. The c080 D1 ruling is characterized faithfully (see edge-label-fidelity below). Legitimate in-scope anchor, not a smuggled positive claim.

**rotation-quality — pass (not the primary axis for this kind; the relevant sub-check is the no-flip claim, which holds).** A law-confidence probe is not an algebraic/structural rotation, so the strict rotation criterion is largely inapplicable; treated as pass. The load-bearing adjacent claim — that the verb STAYS `rough-in (test-coverage-bounded)` and the probe does NOT trigger the cascade — is verified: the two proposed-changes edit-blocks target only the gate-(c) bullet (`:115`) and the `verified_against:` YAML block (`:145-159`); neither touches the `## Status` verb token at `:110`. The HARD CONSTRAINT (this file only, no cascade) is respected.

**variant-axis-coverage — pass.** The probe scope is the three inner-product-structure laws (4/6/7), not the variant axes. The chapter's element-type and output-arg/return-value axes are unchanged by this probe; no hidden branch is introduced. Not the focus of this report-kind.

**cross-reference-integrity — pass.** Every anchor into `book/src/L1/matrix-weighted-norm.md` resolves to the claimed content: `:54` = law 4 (triangle), `:56` = law 6 (Cauchy–Schwarz), `:57` = law 7 (parallelogram), `:69-70` = the two FP caveats, `:79` = the "SPD by construction" applicability claim, `:115` = the gate-(c) bullet the first edit replaces (the edit's OLD text matches the on-disk line verbatim), `:145`/`:159` = the `~~~yaml` fence open/close. The new `verified_against:` citations (`eigensolver.cpp:205-213`, `spaceoperator.cpp:530-537`, `matrix-weighted-norm.md:54-57`) all resolve. No firm-token / fence-truncation guard applies here (the verb is not flipped to firm).

**edge-label-fidelity — pass (the relevant fidelity check here is the c080-D1 citation-support).** The report claims to cite the c080 D1 ruling as "refined, not overturned." I read the c080 source (`reports/2026-06-03T185421Z-lowering-verifier-matrix-weighted-norm-2nd-gate/CYCLE.md`): D1 ruled the firm-on-positive-structure escape INAPPLICABLE because laws 4/6/7 "carry genuine norm-axiom / inner-product-structure content that the L0 source does NOT verify" — the `eigsolve`-convergence-semantics situation, not the `apply_linop` syntactic-identity situation (lines 58, 72, 127). The current report's characterization (CYCLE.md :76) matches this faithfully: it agrees the c080 observation about the L0 *source* is correct, and refines by reframing to the SPD premise's positive L0 home. Notably, c080 line 72 itself already named this exact alternative route ("or a literature-anchor pass raising law-4/6/7 confidence to `ksp_solve`-equivalent"), so the probe is the route c080 explicitly left open — not a contradiction of it. The "refined, not overturned" framing is accurate; no `citation-does-not-support`.

**plan-kind-consistency — pass.** Declared kind is a lowering-verifier audit with a DISCHARGE (partial — structure-side) verdict. The content shape matches: a per-citation audit table, an applicability-condition adjudication, a per-law assessment, and a scoped proposed-changes block that lands a §Status refinement + a `verified_against:` block without promoting the maturity token. The partial/structure-side scoping is internally consistent with leaving the verb at `rough-in (test-coverage-bounded)`.

**skill-uptake-survey — pass.** The report demonstrates uptake of the relevant procedural skills implicitly: it ran the `Norml2` test-absence grep, used `read_range`/codemap for the SPD anchors, applied the `verified_against:` no-leading-quote round-trip discipline (self-noted at :131), and invoked the c080-D1 precedent. Telemetry only; non-blocking.

### Issues found

No blocking issues. Two minor observations, neither rising to warning:

1. **`verified_against:` splice is delicate but correctly flagged (CYCLE.md :92-110, :131).** The second edit-block's leading `note:` line (:95) is a deliberate *placement anchor* that reproduces the existing `:150` note in plain ASCII (`half-eps0-E0^2-V`, `(E, M_elec E)`) — DIFFERENT text from the Unicode-glyph version actually on disk (`½·ε₀·E₀²·V`, `⟨E, M_elec E⟩`). The NOTE-TO-INTEGRATOR (:110) instructs the integrator to IGNORE that leading line and splice only the three new `- citation:` items before the `~~~` fence at :159. I confirmed the intended merged block (existing 3 entries + 3 new) round-trips under `yaml.safe_load`. This is an integrator splice-clarity item the report itself surfaces and pre-mitigates; it is not a citation or YAML-validity defect (the YAML is valid as intended). Recorded for integrator attention, not flagged.

2. **citecheck `[AMBIG]` on `operator.cpp` (CYCLE.md prose, multiple sites).** `citecheck --scan` reports 1 "failing" purely because basename `operator.cpp` collides with `fem/libceed/operator.cpp`; the report disambiguates as `palace/linalg/operator.cpp` everywhere in prose, so the bound is correct and in-range. Cosmetic tool artifact; if a future producer wants a clean `--scan`, full-path-qualifying the bare `operator.cpp` mentions would clear it. Not a defect.

All 8 checks pass; the SPD-trace crux is verified complete and the DISCHARGE (partial — structure-side) verdict is not over-claimed. `overall_status: ready`.
