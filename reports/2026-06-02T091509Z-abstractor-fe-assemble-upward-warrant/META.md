---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T092620Z
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
repaired_at: 2026-06-02T093140Z
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

# META: verification of "L2 upward-propagation WARRANT for `fe_assemble` — NO-ENTRY"

## Critique

### Checks run

**citation-validity — pass.** Mechanical `citecheck.py --scan` reports 17 ok / 0 failing (all bounds + path hygiene clean). I additionally anchor-confirmed the load-bearing pinpoints via `palace-codemap read_range`: `palace/fem/bilinearform.cpp:77` and `:97` are BOTH exactly `op->AddSubOperator(sub_op);  // Sub-operator owned by ceed::Operator` (domain loop at :77, boundary loop at :97 — the report attributes them correctly to the two branches); `:104` is exactly `op->Finalize();`. `palace/fem/libceed/operator.cpp:455` is the `CeedOperatorFullAssemble` function header (confirmed via `search_text`), and lines 455-490 do enclose the per-thread COO assembly + `OperatorCOOtoCSR` materialization the report cites as "where the fusion physically lives." The two solver-K witnesses verify exactly: `laplaceoperator.cpp:191-192` is `BilinearForm k(GetH1Space())` + `DiffusionIntegrator(epsilon_func)` (electrostatic ∇/diffusion), `curlcurloperator.cpp:179-181` is `BilinearForm k(GetNDSpace())` + `CurlCurlIntegrator(muinv_func)` (magnetostatic curl-curl). The L1 anchors round-trip against `book/src/L1/fe_assemble.md` (283 lines): fold signature :61-62, law-2 concatenation-homomorphism :123-128, law-4 term-position commutativity :134-140. The L2 index anchors round-trip: `linear_combination` term-axis fold :24, codomain-distinct do-NOT-merge boundary :22-26. No `verified_against:` block is emitted (record-only warrant), so the YAML round-trip sub-check is not applicable.

**surface-or-evidence — pass.** This is a pure record-only disposition (NO-ENTRY verdict), not a refinement of existing surface. No operator/theme text is mutated; the work product is the warrant note itself. The verdict is independently sound: the accumulation IS order-commutative with no sequential carry — `AddSubOperator` adds each independently-built `sub_op` to the composite (source-confirmed at :77/:97), and addition's commutativity/associativity is the L1 law-4 basis. The per-term kernel IS libCEED-opaque — Palace consumes it via `integ->Assemble(...)` building one `CeedOperator`, with the actual fusion (COO→CSR) inside `CeedOperatorFullAssemble`. Both anti-mirror axes hold as claimed. The check's "pure rotation_claims = fail" condition does not trigger because no rotation is asserted — the report asserts the *absence* of a warrantable rotation, which is the legitimate anti-mirror disposition under redirect §1d.

**rotation-quality — pass (not applicable as a positive-rotation check; the inverse is the load-bearing finding).** No rotation is proposed, so there is no L_{n+1}-more-compact claim to grade. The relevant adjacent check is whether the report correctly identifies that NO genuine rotation exists — i.e. an L2 `fe_assemble` would be a 1:1 degenerate mirror (the exact "renaming-only / 1:1 mapping = fail" pattern this check exists to catch, here applied as a *reason to decline the entry* rather than as a defect in a proposed entry). The reasoning is correct: restating `Σ_i A(space, term_i)` in identical fold vocabulary with the same opaque leaf is no vocabulary shift. The contrast against `fold_solve` (genuine carry → L3 entry) and `solve_family` (no-carry → no L3 entry) is the right discriminant and is source-grounded.

**variant-axis-coverage — pass.** The relevant variant axes of `fe_assemble` (assembly-representation PA/FA dual; differential-operator axis of `WeakFormTerm`; OMP-per-thread parallelization) are each addressed and explicitly scoped as L1 / L1>L0 concerns that do NOT seed L2 content: PA/FA collapses at L1 (cited :104-108, :180-185); the two witnesses differ only in the differential-operator L1 variant axis (:161-169); OMP-per-thread is transparent parallelization absorbed at L1>L0 (:236-237). No hidden branch licenses an L2 fusion the warrant overlooked. The two-list domain+boundary L0 structure is correctly folded into one L1 term list. Coverage is complete and each combination is scoped out with rationale.

**cross-reference-integrity — pass.** All slug references resolve: `linear_combination` (`book/src/L2/linear_combination.md` exists), `weak_form_term`, the L1 `fe_assemble` entry. The fold_solve no-floor precedent directory (`reports/2026-06-02T071603Z-cross-layer-cross-cutter-l2-fold-solve-no-floor-warrant/`) exists on disk and is cited correctly in inputs + §Supporting evidence. There is no `L2/fe_assemble.md` on disk (consistent with the NO-ENTRY verdict — no dangling chapter). The build-readiness firm-body-inside-fence guard is not applicable: this report authors no proposed-changes fence and claims no `firm` chapter (it is record-only).

**edge-label-fidelity — pass.** The report concerns the L2/L1 upward edge (does `fe_assemble` warrant an L2 floor above its firm L1). The prose discusses exactly that edge throughout; the precedent contrasts correctly distinguish the L3/L2 edge of `fold_solve` (carry → L3) from the L2-floor question. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared shape is a record-only WARRANT verdict (audit/observation-kind). Content matches: no book mutation, no SUMMARY.md/dep-map/index touches, no chapter forced, no speculative L2 operators. The frontmatter `status: pending` and the explicit "This CYCLE.md IS the work product" framing are consistent with a disposition dispatch. No firm-operator-with-placeholder mis-classification risk (nothing is claimed firm).

**skill-uptake-survey — warning.** The report's shape (citation-range verification + a warrant/decline-to-author disposition) implies two relevant skills exist — `verify-citation-range` (with its mechanical `tools/citecheck/` realization) and `propose-rotation` (whose decline-path is the GENUINE-FORM exit being exercised here). The report asserts "all citations self-verified against source" and "verified exact via palace-codemap read_range" but does not name an invoked skill. This is a pure-telemetry surface (non-blocking): the verification was evidently performed (my own re-check confirms exactness), but the skill-invocation reference is absent.

### Issues found

1. **(minor, skill-uptake) No skill invocation referenced** — CYCLE.md §Supporting evidence + Summary, throughout. Severity: low / telemetry-only. The citation verification and the rotation-decline analysis both map onto existing skills (`verify-citation-range` mechanical realization; `propose-rotation` decline-path) but none is named. The verification was actually performed correctly; this is a survey-surface gap, not a correctness defect.

2. **(very minor, provenance-label) "c060 D2" label vs. directory provenance** — CYCLE.md §Summary axis-2 ("exactly the c060 D2 no-floor-warrant"), table row ("`fold_solve` at L2 (c060 D2)"), and §GENUINE-FORM. The cited precedent's actual directory is `2026-06-02T071603Z-cross-layer-cross-cutter-l2-fold-solve-no-floor-warrant` (a `cross-layer-cross-cutter` dispatch). The "c060 D2" shorthand is an informal cycle/dispatch label whose mapping to that directory is not self-evident from the path. The underlying citation (the report path) is correct and resolves; only the human-readable shorthand is unverifiable from the artifact. Severity: very low — does not affect the verdict or any source claim.

3. **(observation, not a defect) `weak_form_term` L2 NO-ENTRY consistency is flagged-forward, not established here** — CYCLE.md §Open questions bullet 3. The report correctly does NOT claim to settle `weak_form_term`'s own L2 disposition; it flags the two NO-ENTRY warrants for the batch-19 meta-phase to record coherently together. This is appropriately scoped (one-operator-per-dispatch discipline) and is noted only so the repairer/integrator see it is an intentional forward-flag, not an unsupported sibling claim.

The core verdict — NO-ENTRY on both anti-mirror axes (no-carry concatenation-homomorphism fold + opaque libCEED per-term leaf), GENUINE-FORM exit correctly declined (the term-axis fold is already shared L2 vocabulary via `linear_combination`'s operator-codomain sibling; the `fe_assemble`-specific material is exactly the opaque leaf that does not lift; no ≥2-pipeline combinator emerges), and "no batch-20 candidate" — is source-grounded and sound. The two solver-K witnesses confirm the ≥2-pipeline check reduces to the same fold over the same opaque `A`. No fail-level finding.

## Repair

### Fixes attempted

- **Finding (1)**: skill-uptake-survey warning — no skill invocation referenced (`verify-citation-range` / `propose-rotation` decline-path); pure telemetry surface, verification was actually performed correctly.
  - **Decision**: not-needed.
  - **Rationale**: telemetry-only / non-blocking. The critic confirmed the verification was performed and exact (independent codemap re-check). The missing artifact is a *survey reference*, not content or a correctness defect — outside mechanical-repair scope (would require authoring a skill-invocation narrative the producer did not record, and the survey value is captured by the critic's note). No `overall_status` impact.

- **Finding (2)**: provenance-label shorthand — "c060 D2" informal label whose mapping to the actual `cross-layer-cross-cutter` precedent directory is not self-evident; underlying report-path citation is correct and resolves.
  - **Decision**: repaired (minimal, surgical clarification at first use; not a full 5-site rewrite).
  - **Action**: `reports/2026-06-02T091509Z-abstractor-fe-assemble-upward-warrant/CYCLE.md` §Summary axis-2 (line 22) — annotated the first "c060 D2" occurrence with the actual provenance path (`reports/2026-06-02T071603Z-cross-layer-cross-cutter-l2-fold-solve-no-floor-warrant/`), anchoring the shorthand used in the later table row / §GENUINE-FORM. The underlying citation was already correct (§Supporting evidence line 85 cites the full directory path); this only ties the human-readable shorthand to it at first use. Within human-readable-label repair authority.

- **Finding (3)**: observation (not a defect) — `weak_form_term` L2 NO-ENTRY consistency is intentionally flagged-forward to batch-19 meta-phase, not claimed-settled here.
  - **Decision**: not-needed.
  - **Rationale**: explicitly noted by the critic as an intentional forward-flag (one-operator-per-dispatch discipline), not an unsupported sibling claim. Nothing to repair.

### Unrepairable findings

None. No finding required deferral; the one warning is telemetry-only and the two nits are cosmetic (one repaired, one no-op observation).

## Suggested resolution

`ready`. Notes for the integrator:
- This is a **record-only NO-ENTRY warrant** — no book/concepts mutation, no SUMMARY.md/dep-map/index touches, no proposed-changes fence to apply. Integration is the disposition carry-forward only.
- Carry the disposition to **batch-19 meta-phase**: (a) record the `L2/fe_assemble` NO-ENTRY warrant coherently alongside the `fold_solve` L2 no-floor-warrant (same opaque-library-ownership anti-mirror axis); (b) **recommend adding `L2/fe_assemble` to the STOP-PROPOSING negative list** so future cycles do not re-derive it; (c) the §Open-questions forward-flag on `weak_form_term`'s own L2 disposition is for the meta-phase to record together with this verdict, not to settle here.
