---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T071500Z
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
repaired_at: 2026-06-01T072000Z
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

# META: verification of "Formalize divfree-projector at L2" (cycle-042 D6)

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck.py --scan` (24 ok / 3 failing) and the 3 failing are confirmed scanner path-normalization quirks, NOT real misses: the scan stripped the leading `palace/` segment from `palace/fem/integrator.hpp:217` and `palace/fem/integ/mixedvecgrad.cpp:202` (reporting them as `fem/integrator.hpp` / `fem/integ/mixedvecgrad.cpp`), and the third is an `[AMBIG]` on the bare basename `integrator.hpp` (two candidates) — an artifact of the same prefix-strip, not a defect in the report's citation (which carries the full disambiguating path). I re-ran all three with the full report-as-written path + their anchors: `integrator.hpp:217` (anchor `grad`), `mixedvecgrad.cpp:202` (anchor `-1.0`), `mixedvecgrad.cpp:142` (anchor `PopulateCoefficientContext`) — all `[ok]`, both files exist on disk under `reference/palace/palace/fem/...`. So the report's own characterization of the 3 MISS as "path-normalization quirks (the `--anchor` checks passed)" is accurate. All load-bearing pinpoints verified by `--anchor`: `divfree.cpp:155-187` (anchor `Mult` resolves at [155,162,163,167,175,180,181,185], matching the report's claimed anchor set exactly), `:185` (`AddMult`, real branch), `:180-181` (`AddMult`, complex Re/Im), `:175` (`ksp`, inner solve), `:119` (`SPD`), `divfree.hpp:28-31` (`divergence`, the `Gᵀ M x = 0` defining condition, anchored at line 29 in range), `divfree.hpp:64-66` (`irrotational`, the stale per-method doc), `eigensolver.cpp:260-262` (`divfree`, call site), `test-libceed.cpp:905-916` (`WeakDivergence`, MFEM cross-validation). No `[DRIFT ±N]`, no off-by-one, no OOB. No `verified_against:` block in this report (harvester, not lowering-verifier) — the YAML round-trip sub-check is not applicable.

**surface-or-evidence — pass.** This is a `new:` file creation (an L2 floor entry), not a refinement of an existing operator/theme; the surface-or-evidence check targets refinement-shaped proposals modifying existing text. The new chapter carries its own evidence (the on-disk apply-body read + the full L0 anchor list, all verified). Not a pure rotation_claim against an existing surface, so the fail condition does not apply.

**rotation-quality — pass.** The report asserts ONE genuine fusion-rotation: step-4 `Grad->AddMult(ψ, y, 1.0)` de-fused into `apply_linop(P.Grad, ψ) ▷ axpy(1.0, ·, y)`. I read the apply body (`divfree.cpp:155-187`) directly and confirm this is the only fused kernel in the body: step 1 (`WeakDiv->Mult`, :162-163/:167) is a single operator apply, step 2 (`SetSubVector`, :173) a single subvector-zero primitive, step 3 (`ksp->Mult`, :175) the opaque inner solve — none carry multi-operation fusion. `AddMult` is the apply-and-accumulate idiom; de-fusing it into `apply_linop ▷ axpy` IS a state-hiding/coarser-substitution un-collapse (the fused form hides the intermediate `Grad·ψ`), so it qualifies as a real rotation, not a 1:1 rename. The MODERATE-floor judgment is sound and well-reasoned: the report correctly distinguishes this from a non-trivial decomposition (the L1 entry already names `AddMult` as an `axpy`-fused accumulate, and the four-step composition is already explicit at L1/L3), and correctly classifies the `Gᵀ M G` non-materialization as an algebraic-structuring choice (present at every layer) rather than an L2 de-fusion. The "exactly one fusion" claim holds against source.

**variant-axis-coverage — pass.** Two axes identified, matching L1/L3: one orthogonal (element-type real `Vector` | complex `ComplexVector`, anchored to the template instantiation `divfree.cpp:189-190` and the component-wise complex apply :159-184) and one absorbed (operator-representation, collapsed into the opaque `DivFreeProjector` closure at setup). The complex branch is explicitly covered (the apply body confirms the same four steps + same single `AddMult` fusion run component-wise on Re/Im with no cross-coupling). The inner `ksp_solve`'s own loop-shaping axes are correctly scoped out as interior to that gate. No hidden branches.

**cross-reference-integrity — pass.** All link targets verified on disk: `L1/divfree-projector.md`, `L3/divfree-projector.md`, `L2/ksp_solve.md`, `L2/eigsolve.md`, `L2/dot.md`, `L2/nrm2.md`, `L2/scal.md`, `L2/index.md`, `SUMMARY.md`, `L1/apply_linop.md`, `L1/axpy.md`, and the four concept pages (`set_subvector_zero`, `nested-constructed-operator-gate`, `sequential-obstruction`, `constructed-operators`) all EXIST. The L2 `apply_linop`/`axpy` chapters correctly do NOT exist, so the report's cross-layer L1 anchors (`../L1/apply_linop.md`, `../L1/axpy.md`) are the right call (not dead links). Build-readiness fence guard: the `new:` block (lines 67-537) ENCLOSES the full firm apparatus — `## Status` (line 409), Signature (128), Semantics (172), Algebraic laws (271), Evidence (480) are all INSIDE the fence. Fence enumeration shows 6 markers = 3 balanced pairs (`new:` 67/537, `edit:index` 539/542, `edit:SUMMARY` 544/547), even parity, no nested-fence imbalance. No firm-body-outside-fence defect. The SUMMARY `edit:` anchors correctly on the existing `- [eigsolve](./L2/eigsolve.md)` line (SUMMARY:62).

**edge-label-fidelity — pass.** The report's edge claims are L3→L2 (floor presence under firm L3) and L2→L1 (identity-in-form on the gate apply, the fusion-rotation living in the step-4 implementation). The prose discusses exactly those edges: the L3-parent-presence motivation, the L2↔L1 identity-in-form rotation with the one `AddMult` de-fusion, and the explicit deferral of the L2>L1 / L3>L2 lowering-theme authoring to the sibling D9 dispatch. The "Iteration rotation: obstruction carried by reference" section correctly keeps the inner-solve obstruction at the `ksp_solve` edge, not at the projector's. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared `firm` (moderate floor). Content shape matches: full signature, semantics, five algebraic laws + two non-laws (all transported from the firm L1 entry whose laws read off positive source), variant axes, dependencies, evidence — no rough-in placeholders, no TODO sentinels. The `firm-on-positive-structure` justification for the absent `test-divfree.cpp` is the correct precedent (syntactic-identity laws on positive source, not literature-inferred convergence claims). The MODERATE-floor classification (one genuine fusion beyond bare floor-presence) is internally consistent across Status / Fusion-note / OQ sections. The inner-solve obstruction is correctly carried as a caveat (NOT a status reduction) — appropriate, since the projector's own four-step body authors no loop and the obstruction is the inner `ksp_solve`'s property carried by reference.

**skill-uptake-survey — pass (telemetry).** The report references `tools/citecheck/citecheck.py --anchor` self-verification of all L0 anchors this invocation (Supporting evidence §) and names the cycle-041 `L2/dot.md` template as the structural precedent. The fusion-vs-thin judgment is the load-bearing call and is explicitly reasoned in Status + Fusion-note. No required skill invocation is missing for this shape.

### Issues found

No blocking or warning-level issues found. All eight checks pass. Specifically confirmed against the dispatch focus points:

1. **(Focus 1 — citation-validity)** The 3 `citecheck --scan` MISS reports are GENUINELY scanner path-normalization quirks (leading-`palace/`-segment strip), NOT real misses — both files exist on disk and resolve `[ok]` with the full report-as-written path + anchor. The report's flagging is accurate. No off-by-one anywhere (all `--anchor` checks clean, no `+1`-drift).

2. **(Focus 2 — MODERATE-floor judgment)** Verified against the on-disk apply body (`divfree.cpp:155-187`): step-4 `Grad->AddMult(ψ, y, 1.0)` is the ONLY genuine kernel fusion; steps 1-3 are single applies/primitives with no multi-op fusion. The "exactly one fusion" reasoning is sound and the moderate-floor classification (vs. pure-thin BLAS-1 floors, vs. non-trivial decomposition) is well-justified.

3. **(Focus 3 — inner-solve obstruction by reference)** Correctly carried by reference through the firm L2 `ksp_solve` dependency — neither introduced (the projector body has no projector-level loop) nor erased (the inner CG iteration stays interior to `ksp_solve`), per the `nested-constructed-operator-gate` fidelity rule and the firm L3 entry's discipline.

4. **(Focus 4 — stale-doc disposition)** Honored: `divfree.hpp:64-66` per-method `Mult` doc ("irrotational … ∇×y=0") is correctly identified as inverted/stale; authoritative semantics = `Gᵀ M x = 0` (`divfree.hpp:28-31`, verified). Carried as inherited caveat (OQ `divfree-mult-doc-irrotational-vs-divfree-stale`), not silently dropped. (Corroborating L0 detail: the source's own inline comment at `divfree.cpp:177` "Compute the irrotational portion of y and subtract" likewise mismatches the additive `AddMult(...,1.0)` + divergence-free result — consistent with the flagged inversion.)

5. **(Focus 5 — NO-fold-parent / fork-independent)** Correctly framed as a standalone constructed-operator gate with no fold-parent and no do-NOT-merge boundary, distinct from the cycle-041 BLAS-1 fold-leaf floors. The OQ explicitly notes the entry is fork-INDEPENDENT of the `dot-l2-leaf-floor-vs-fold-only-design` meta fork.

6. **(Focus 6 — count-ownership + fence parity)** Count-ownership correctly deferred to D11 (the report appended ONLY its own dep-map row + body + SUMMARY entry, did NOT touch the L2/index consolidated firm-count tally) — flagged in the OQ. Fence parity clean (3 balanced pairs, firm apparatus inside the `new:` fence).

Minor (informational, non-blocking, no repair needed): the SUMMARY `edit:` block (lines 544-547) gives only the two-line context (`- [eigsolve]` + new `- [divfree-projector]`) as an insertion anchor; this resolves unambiguously against the current SUMMARY (single `L2/eigsolve` match at SUMMARY:62), so it is fine — noting only that it relies on that line remaining unique at integration time.

## Repair

### Fixes attempted

No findings required repair. All eight critic checks returned `pass`; the critic recorded no blocking or warning-level issues. The only flagged items are informational and confirmed non-defects:

- **Finding**: 3 `citecheck --scan` MISS reports (`palace/fem/integrator.hpp:217`, `palace/fem/integ/mixedvecgrad.cpp:202`, bare-basename `[AMBIG]` on `integrator.hpp`).
  - **Decision**: not-needed.
  - **Rationale**: Confirmed scanner path-normalization quirks (leading-`palace/`-segment strip), NOT real misses. The critic re-ran all three with the full report-as-written path + their anchors and got `[ok]`; both files exist on disk under `reference/palace/palace/fem/...`. The report's citations carry the full disambiguating path and verify clean via `--anchor`. No off-by-one, no DRIFT, no OOB. There is nothing in the report to "fix" — touching the citations would diverge them from the correct on-disk paths.

- **Finding**: SUMMARY `edit:` anchor relies on the `- [eigsolve](./L2/eigsolve.md)` line being unique.
  - **Decision**: not-needed.
  - **Rationale**: The anchor resolves unambiguously against the current SUMMARY (single `L2/eigsolve` match at SUMMARY:62). This is an integration-time precondition note, not a present defect. The anchor is correct as written; no surgical change is warranted (and broadening/narrowing it would be a content decision, out of repair scope).

- **Note (forward-flag, not a finding)**: if firm `book/src/L3/divfree-projector.md` asserts "no interposed L2 entry," a downstream lifter touch will be needed to drop the stale L3 §Lowers-to once this L2 floor lands (parallel to the `elementwise_product` situation; the D9 themes already flag stale L3 §Lowers-to).
  - **Decision**: not-needed (out of this report's scope).
  - **Rationale**: This is a cross-entry artifact-state observation about the existing firm L3 entry, not a defect in *this* report. The repairer does not modify the artifact (`book/`) and does not author substantive content. Routed forward to the sibling D9 lowering-theme / lifter dispatch, which already carries the stale-§Lowers-to flag; recorded here for integrator awareness, no edit applied.

### Unrepairable findings

None. No finding exceeds repair authority because no finding is a defect — all flagged items are informational-no-defect.

## Suggested resolution

`ready`. The report applies cleanly as-is. Notes for the integrator:
- The 3 `--scan` MISS are scanner artifacts; the on-disk citations are correct (verified via `--anchor`). Do not "correct" the cited paths.
- The SUMMARY `edit:` anchor depends on `- [eigsolve](./L2/eigsolve.md)` remaining the unique `L2/eigsolve` line at apply time — currently true.
- Count-ownership of the L2/index consolidated firm-count tally is deferred to D11 per the report's OQ (this report appended only its own dep-map row + body + SUMMARY entry).
- Forward-flag: a downstream lifter/D9 touch may need to drop a stale "no interposed L2 entry" §Lowers-to assertion in firm `book/src/L3/divfree-projector.md` once this L2 floor lands — not in this report's scope, already tracked by the D9 themes.
