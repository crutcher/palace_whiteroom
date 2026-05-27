---
verifies: ../REPORT.md
critiqued_at: 2026-05-27T00:30:00Z
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
---

# META: verification of REPORT — Formalize axpby at L1

## Critique

### Checks run

**citation-validity** — pass. Spot-checked the load-bearing source ranges. `vector.hpp:130-131` confirmed as `ComplexVector::AXPBY` member decl with the exact comment quoted (`In-place addition (*this) = alpha * x + beta * (*this).`). `vector.hpp:133-136` confirmed as `AXPBYPCZ` member decl. `vector.cpp:726-730`, `732-737`, `739-743` confirmed as the three explicit `AXPBY` template specialisations with the delegations as described (the real-real path calls `add(alpha, x, beta, y, y)` at line 729; the two complex-vector paths both delegate to `y.AXPBY(alpha, x, beta)`). `vector.cpp:745-758` confirmed as `AXPBYPCZ` real-path with `gamma == 0.0` branch delegating to `add(alpha, x, beta, y, z)`. Decision record `scaffolding/decisions/axpby-as-primitive.md` exists and contains the fused-primitive rationale exactly as the report claims.

**surface-or-evidence** — pass. Three surface-modifying proposed-changes blocks: new `book/src/L1/axpby.md` (full operator entry), row-replacement in `book/src/L1/index.md`, and `append-after` insertion in `book/src/SUMMARY.md`. All are concrete surface deltas, not pure rotation_claims. The promotion rough-in→firm carries new evidence (decision record + three L0 specialisation citations).

**rotation-quality** — pass. The L0→L1 rotation hides the destination-buffer aliasing (`y` as both input and overwrite target) and the kernel-fusion dispatch (three template specialisations + member-form delegation + MFEM `add(α,x,β,y,y)` collapse) into a single equational `axpby(α, x, β, y) = α·x + β·y`. The result is strictly more compact and more equational than the L0 form; not a renaming.

**variant-axis-coverage** — pass. Two axes named and covered: element-type {real | complex} and scalar-promotion sub-axis. All three L0 specialisations are accounted for (real-real at `vector.cpp:726-730`; complex-complex at `732-737`; real-scalar-on-complex-vector at `739-743`). The scalar-promotion sub-axis explicitly defers to open question `scalar-promotion-typing-rule` rather than hiding the branch. Mixed real/complex scalar pairs are explicitly scoped out ("not exposed by Palace and are not part of the L1 signature"). No hidden branches.

**cross-reference-integrity** — pass. `book/src/L1-L0/axpby-mutation-rotation.md` exists. `book/src/L1/axpy.md` exists and the subsumption claim `axpy(α, x, y) ≡ axpby(α, x, 1, y)` is consistent with axpy.md's `axpy(α, x, y) = α·x + y` (substituting β=1 gives identity). `scaffolding/decisions/axpby-as-primitive.md` exists. The L1/index.md anchor row matches the report's quoted text verbatim. The SUMMARY.md anchor line `- [dot](./L1/dot.md)` exists at line 27 under the "L1 — Mutation-Lifted Forms" Part. All referenced open-question slugs are present in `scaffolding/open-questions.md`. Note: the chapeau link `[scaffolding/decisions/axpby-as-primitive.md](../../../scaffolding/decisions/axpby-as-primitive.md)` from `book/src/L1/axpby.md` resolves correctly (three `..` from `book/src/L1/` reaches repo root).

**edge-label-fidelity** — pass (not applicable to this report-kind). This is an L1 operator entry promotion (not an L_{n+1}→L_n lowering theme). The cross-references to `L1-L0/axpby-mutation-rotation` discuss L1>L0 in alignment with the existing theme file.

**plan-kind-consistency** — pass. The proposal declares `firm` and the content shape supports it: canonical signature, nine numbered algebraic laws, four non-laws, full variant-axis coverage, eight L0 evidence citations, and a recorded decision for the primitive-vs-decomposition question. No rough-in placeholders.

**skill-uptake-survey** — pass. Frontmatter surveys three skills: `verify-citation-range` (explained_non_applicable — citations verified inline), `classify-variant-axis` (artifact_landed — two-axis section), `verify-refinement-surface` (explained_non_applicable — inspected against cycle-002 dot precedent). The deferral rationale for `verify-citation-range` is consistent with the pilot-1 / cycle-002 harvester precedent; this is a telemetry surface, not blocking.

### Issues found

**(observation, not a fault)** — wave-conflict at SUMMARY.md insertion anchor. The report's `append-after:book/src/SUMMARY.md` block inserts a new line `- [axpby](./L1/axpby.md)` immediately after the existing `- [dot](./L1/dot.md)` line (line 27). Cycle-003 dispatch 1 (`nrm2` harvester) targets the same anchor. The report flags this explicitly in the integrator-hint paragraph (REPORT.md:173) and suggests merging both insertions with order following the L1/index.md dep-map row order. Per user directive, parallel-wave anchor collisions are good signal and the integrator resolves; flagging here for visibility only.

**(low-severity, prose-only)** — Law 5 ("Bilinearity") chain (REPORT.md:97-100) uses a clumsy correction-term expansion: `axpby(α₁ + α₂, x, β, y) = axpby(α₁, x, β, y) + axpby(α₂, x, 0, y) - β·y + β·y = α₁·x + α₂·x + β·y`. The `- β·y + β·y` cancellation is algebraically valid but stylistically opaque — a cleaner statement would be `axpby(α₁ + α₂, x, β, y) = axpby(α₁, x, β, y) + α₂·x` or simply assert linearity in α directly. Algebraically correct; readability nit.

**(low-severity, prose-only)** — Law 8 ("Scalar absorption") chain (REPORT.md:103) presents the three-way identity `axpby(α·γ, x, β, y) = axpby(α, γ·x, β, y) = axpby(α, x, β·γ, γ⁻¹·y)`. The third equality requires invertible scalar `γ` (noted), but the chained reading is mildly misleading — the first two terms equal each other unconditionally; only the bridge to the third needs the invertibility caveat. A minor reformatting could split into two laws.

**(low-severity)** — "Identities in both" is numbered Law 4 in the chapeau Summary's count ("two zero-identities, the reduction-to-`scal` identity, β=1 reduction" — REPORT.md:39) but the Summary's enumeration ("nine algebraic laws") drifts from the in-body numbering. The body has 9 numbered items; the Summary's prose enumeration mentions "subsumption of `axpy`, two zero-identities, the reduction-to-`scal` identity, β=1 reduction, bilinearity, one distributivity in x, one distributivity in y, chained-axpby collapse" — that's 8 named items, but Law 8 (scalar absorption) is not in that prose list. Cosmetic inconsistency between summary prose and body list.

**(low-severity)** — Frontmatter `inputs` lists `scaffolding/decisions/axpby-as-primitive.md (NEW — captures the fused-primitive decision)` as an input, but the file is created by this report's cycle, not consumed as input. Slight category-conflation — should arguably be under proposed outputs / new artifacts. Cosmetic; does not affect validity.

**(low-severity)** — Subsumption-relation prose at the chapeau says `axpby` is "the fused BLAS-1 primitive that subsumes both `axpy` (β=1) and pure-scaling (α=0)". The α=0 case yields `β·y` (scalar-times-vector), which the report itself notes is *not yet* an L1 primitive (no `scal` operator exists — flagged in caveat #2 and Law 2 parenthetical). Calling this a "subsumption" of "pure-scaling" presumes the primitive that doesn't yet exist; technically the report subsumes `axpy` (which exists) but only foreshadows subsuming `scal` (which doesn't). Minor terminological imprecision.

**(low-severity)** — Open-question status update is recommended in prose (REPORT.md:187): `axpby-axpy-scal-decomposition-decision` should be marked `answered` by the integrator. The report cannot self-promote that ledger entry (write-authority partition: harvester writes only to `reports/<id>/`). Flagging for the integrator handoff — no fault.
