---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T22:30:00Z
critic_version: 1
checks:
  citation-validity: fail
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-27T22:54:30Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: unrepairable
overall_status: pass-after-repair
follow_up_agent: null
---

# META: verification of harvester bilinear-form L1 rough-in

## Critique

### Checks run

**citation-validity — FAIL.** The cited source ranges all exist and the line numbers resolve. However, a **load-bearing semantic claim about the L0 implementation is incorrect**, which the critic must surface as a citation-validity failure (the citation pointer is valid but the prose mischaracterises what the source range says).

Specifically, the report claims in *Semantics* (CYCLE.md lines 162-165) and in the *Open questions* §`bilinear-form-conjugation-convention-anchor` (CYCLE.md lines 513-520) that the L0 implementation at `palace/linalg/operator.cpp:621-639` returns `(Ax)ᴴ y = xᴴ Aᴴ y` (because `dot.md`'s L1 first-argument-conjugation convention is asserted to be the free-function convention). This **mischaracterises the free-function `linalg::Dot(comm, x, y)` semantics**. Verifying against `palace/linalg/vector.cpp:674-685` (free-function `LocalDot`):

```
LocalDot(x, y) returns:
  real = Re(x)·Re(y) + Im(x)·Im(y)
  imag = Im(x)·Re(y) - Re(x)·Im(y)
```

For `x = a + bi`, `y = c + di`: `xᴴ y = (a-bi)(c+di) = (ac+bd) + (ad-bc)i`. The function returns `(ac+bd) + (bc-ad)i = conj(xᴴ y) = yᴴ x`.

So **the free-function `linalg::Dot(comm, x, y)` conjugates the SECOND argument** — i.e., it returns `yᴴ x`, NOT `xᴴ y`. This matches the `palace/linalg/vector.hpp:110` comment "Vector dot product (yᴴ x)" cited in `book/src/L1/dot.md:109`. Substituting back: `Dot(comm, Ax, y) = yᴴ · (Ax) = yᴴ A x`, which **matches the source comment at `palace/linalg/operator.hpp:386`** ("yᴴ A x"). There is **no disagreement between the L0 comment and the L0 implementation** — the implementation returns exactly what the comment claims.

The L1 `dot.md` chapter (line 43, lines 104-105) explicitly notes the L0-vs-L1 conjugation asymmetry: the free-function form has the second argument conjugated (the receiver-vs-argument asymmetry in the C++ method form is what determines side-of-conjugation; the L1 convention chooses first-argument conjugation as a *normalisation*). The dispatch elided this distinction and propagated the L1 convention onto the L0 free-function call inside the matrix-weighted overload, fabricating a non-existent ambiguity.

Practical impact: the `bilinear-form-conjugation-convention-anchor` OQ is **resting on a false premise**. The dispatch's three-way ambiguity at CYCLE.md lines 520-530 (a/b/c options) is not real — the L0 comment AND implementation both express `yᴴ A x`. The L1 convention is a free choice; the report's L1 `bilinear_form(x, M, y) = xᴴ M y` convention is a fine choice, but the L1>L0 lowering theme simply needs an argument-swap (or matching choice `bilinear_form(y, M, x) = yᴴ M x` to align with Palace's surface). This is mechanical, not a research question.

**surface-or-evidence — pass.** This is a rough-in for a new L1 operator, not a refinement of an existing one; the surface-or-evidence check is naturally satisfied by the proposed-changes block adding the new operator surface (`book/src/L1/bilinear-form.md`) anchored to L0 evidence (`operator.hpp:386-394`, `operator.cpp:621-639`).

**rotation-quality — pass.** The L1 form `α = bilinear_form(x, M, y) = xᴴ M y` is strictly more compact and more abstract than the L0 form: workspace `ComplexVector Ax(A.Height())` is hidden, the real-`A`/complex-`A` overload split is collapsed to one operator, the MPI collective is folded out, the receiver-vs-argument C++ asymmetry is normalised. This is genuine state-hiding rotation, not a 1:1 rename. The dispatch's "closed-form `xᴴ M y` is the L1 definition; the `dot(x, apply_linop(M, y))` unfolding is informational only" framing (CYCLE.md lines 158-161) is exactly the closed-form discipline this check requires.

**variant-axis-coverage — pass.** Four orthogonal axes are recorded: precision-mode, output-arg-pattern, M-symmetry-property, parallel-wrapper. Element-type of `M` and operator-representation of `M` are explicitly recorded as collapsed (absorbed) axes with rationale. The M-symmetry-property axis has both witness values exercised (Hermitian `Bttr` at line 85; non-symmetric `Atn` at line 90). The element-type-of-x/y axis is implicitly complex-only because Palace's matrix-weighted overload set is complex-vector-only — this is documented in the OQ §`bilinear-form-real-vector-coverage-gap` as a deliberate scope choice. No hidden branches surfaced.

**cross-reference-integrity — pass.** All inter-document links resolve: `book/src/L1/dot.md`, `book/src/L1/apply_linop.md`, `book/src/L1/index.md`, `book/src/L0/linalg-operator-file.md`, `book/src/L0/mutable-workspace-pattern.md`, `book/src/concepts/dot.md` all exist. The OQ slug `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` resolves to `scaffolding/open-questions.md:1359`. Priority #17 resolves to `scaffolding/priorities.md:36`. The Palace source ranges `palace/linalg/operator.hpp:386-394`, `palace/linalg/operator.cpp:621-639`, `palace/models/boundarymodeoperator.cpp:85,90`, `palace/linalg/nleps.cpp:675` all verified in-range. **One minor note**: the report cites `palace/linalg/operator.hpp:385-394` in frontmatter inputs but `:386-394` in body — these are equivalent (line 385 is blank); not a defect, just inconsistency.

**edge-label-fidelity — pass.** Frontmatter says `layer: L1`, `firmness: rough-in`, no edge label since this is an L1 operator (not a lowering theme). No L_{n+1}→L_n edge label to honour or violate.

**plan-kind-consistency — pass.** The proposal is correctly labelled `rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)`. The Status section explicitly justifies rough-in over firm by naming two gating conditions (conjugation-convention OQ and narrow variant-axis coverage). However, see *Issues found* below — one of those two gating conditions is based on a misreading; if/when that OQ is closed-by-correction, the firm-promotion bar drops correspondingly.

**skill-uptake-survey — warning.** No invocation of `verify-citation-range` skill is mentioned in the dispatch report, despite the dispatch deliberately citing multiple source ranges (the matrix-weighted `Dot` overload pair, the two use sites in boundarymodeoperator.cpp, the nleps.cpp Newton denominator). A `verify-citation-range` invocation against the matrix-weighted `Dot` body and the free-function `LocalDot` body would have **caught the conjugation-convention misreading** that flagged citation-validity above — running `LocalDot`'s real/imag-part assembly against the canonical `xᴴ y = (a-bi)(c+di)` expansion directly exposes the second-argument-conjugation convention. This is the second cycle-010 report where verify-citation-range non-invocation correlates with a downstream citation-validity miss; surfacing the pattern but not blocking. `classify-variant-axis` invocation also not mentioned, though the four-axis classification (precision-mode, output-arg-pattern, M-symmetry-property, parallel-wrapper) is well-structured — this is presence-check telemetry only.

### Issues found

**Issue 1 (severity: high) — Conjugation-convention OQ is based on a misreading of `linalg::LocalDot`.** Location: CYCLE.md *Semantics* §"Composition into `apply_linop` + `dot`" (lines 158-167) and *Open questions* §`bilinear-form-conjugation-convention-anchor` (lines 513-545).

The dispatch claims the L0 implementation returns `(Ax)ᴴ y = xᴴ Aᴴ y` by applying `dot.md`'s L1 convention (conjugate-linear in first argument) to the **free-function** `linalg::Dot(comm, Ax, y)` call at the end of the matrix-weighted body. But `linalg::Dot`'s free-function form conjugates the **second** argument, not the first — this is directly verifiable from `palace/linalg/vector.cpp:674-685` (`LocalDot` body: `Im(x)·Re(y) - Re(x)·Im(y)` is the imaginary part of `yᴴ x`, not `xᴴ y`).

Substituting correctly: `linalg::Dot(comm, Ax, y) = yᴴ · Ax = yᴴ A x`. This **matches** the source comment at `palace/linalg/operator.hpp:386` ("Compute the bilinear form inner product yᴴ A x"). The "three-way ambiguity" the OQ raises (options a/b/c at CYCLE.md lines 520-526) does not exist. The L0 source is self-consistent.

The downstream impact is that:
- The OQ should be closed (or substantially reframed) — not promoted to a long-lived ledger entry. The actual L1>L0 lowering question is mechanical: does the L1 convention name the conjugated argument as `x` (then the lowering inserts an argument swap to align with Palace's `yᴴ M x` surface) or as `y` (then the lowering is identity-in-form)? Either choice is fine; there's no Palace-side ambiguity to resolve.
- The rough-in firmness gating reason #1 (CYCLE.md lines 345-349) is invalid. Reason #2 (narrow variant-axis coverage) still holds.
- The *Semantics* prose at CYCLE.md lines 158-167 needs the L0 unfolding rewritten: `linalg::Dot(comm, Ax, y) = yᴴ A x = conj(xᴴ Aᴴ y) = conj(law-7-applied)`. If the L1 convention chooses `bilinear_form(x, M, y) = xᴴ M y`, then the L1>L0 lowering is `bilinear_form(x, M, y) = conj(linalg::Dot(comm, x, M, y))` — or equivalently `bilinear_form(x, M, y) = linalg::Dot(comm, y, M, x)` via the argument swap (which still equals `xᴴ M y`).

**Issue 2 (severity: low) — `dot.md` L0/L1 convention asymmetry not surfaced in the report's L1-vs-L0 distinction.** Location: CYCLE.md §"L1 vs L0 distinction" (lines 358-376).

The L1 `dot.md` chapter at line 43 explicitly documents the L0-vs-L1 conjugation asymmetry ("the L1 signature names the conjugated argument first; the L0 method form has the receiver linear and the call argument conjugated"). The matrix-weighted entry should inherit and re-cite this asymmetry — the dispatch's *L1 vs L0 distinction* section names workspace, MPI, element-type collapse, but does **not** mention the conjugation-side normalisation that the L1 convention performs against the L0 free-function. Surfacing this would clarify the L1>L0 lowering's mechanical-not-research nature (per Issue 1).

**Issue 3 (severity: low) — non-symmetry of `Atn` is supported by a citation pointer one line off-claim.** Location: CYCLE.md lines 229-231 ("the inhomogeneous boundary coupling `Atn` in `palace/models/boundarymodeoperator.cpp:90` — a complex wrapper around a non-symmetric MFEM HypreParMatrix").

The non-symmetry of `Atn` is correct (verifiable at `boundarymodeoperator.cpp:38` "Btn = -Atn^T" comment, plus the explicit `Atnr->Transpose()` materialisation at line 40 — if `Atn = Atnᵀ` were guaranteed, no separate `Btnr` would be needed). The report should additionally cite the assembly site or the symmetry-asymmetry comment as load-bearing evidence rather than asserting the non-symmetry property without a direct citation.

**Issue 4 (severity: low) — slug-name OQ is over-elaborated.** Location: CYCLE.md *Open questions* §`bilinear-form-slug-name-coordination` (lines 576-611).

The OQ recommends keeping `bilinear-form` (matching the dispatch directive) and makes a strong argument. Per the "incremental process refinement default-accepted" methodology invariant, the slug coordination is a 1-line follow-up for the integrator (or a future layer-intro-author dispatch) and does not need a full long-lived OQ. The integrator (per `book/src/L0/linalg-operator-file.md`'s back-reference to `L1/dot_bilinear`) will need to make a one-character pen stroke after this dispatch lands; not a research question. Severity is low because the OQ format does not block firmness promotion (it is explicitly framed as procedural follow-up), but it adds to the OQ ledger that meta-phase batches must triage.

**Issue 5 (severity: low) — duplicated row in variant-axis OQ table conflates `precision-mode` and `output-arg-pattern` with actual M-symmetry coverage.** Location: CYCLE.md lines 624-634 (the variant-axis OQ table inside `bilinear-form-variant-axis-test-coverage`).

The table rows for `precision-mode`, `output-arg-pattern`, and `parallel-wrapper` are listed as having inherited or trivial coverage, while the M-symmetry-property rows are listed as the actual coverage delta. The "Unexercised" line then names "real-x / real-y cases" — but the Signature element-type table at CYCLE.md lines 124-127 explicitly omits the real case as not-surfaced-by-Palace. So "Unexercised" treating the absence as a coverage gap is inconsistent with the Signature's framing that the real case is not part of the operator's surface. Either: (a) keep the real case out of scope (per the *Variant axes* §"absorbed" framing and the `bilinear-form-real-vector-coverage-gap` OQ option-c recommendation), and remove from Unexercised; or (b) treat the real case as an L1-only-no-L0-anchor variant and surface it as a coverage gap. The two OQs partially contradict each other on this point.

**Issue 6 (severity: info) — the firm-promotion gating analysis would benefit from explicit conditional structure.** Location: CYCLE.md §"Status" (lines 338-356).

If Issue 1's correction lands, gating reason #1 evaporates; that leaves gating reason #2 (narrow variant-axis coverage). The dispatch should consider whether reason #2 alone is sufficient to hold the rough-in below firm, given that the M-symmetry axis has two witnesses (Hermitian + non-symmetric) and the unweighted special case `M=I` is already firm via `dot`. This is informational — the repairer / integrator may decide that on correction of Issue 1, the rough-in is firm-promotion-eligible immediately or that one more witness is needed.

### Critical methodology checks (cycle-010-specific)

**(A) OQ on conjugation convention — accurately characterised?** No. See Issue 1. The OQ is based on a misreading of `linalg::LocalDot`'s second-argument-conjugation convention. The L0 comment and the L0 implementation are consistent — both express `yᴴ A x`. The OQ should be closed-by-correction or substantially reframed as a mechanical L1-convention-normalisation note.

**(B) Conditional Hermitian symmetry law verified?** Yes. Law 7 (`Mᴴ = M ⇒ bilinear_form(x, M, y) = conj(bilinear_form(y, M, x))`) is correctly stated. Derivation: if `Mᴴ = M`, then `xᴴ M y = xᴴ Mᴴ y = (M x)ᴴ y = conj(yᴴ (M x)) = conj(yᴴ M x) = conj(bilinear_form(y, M, x))`. The witness at `boundarymodeoperator.cpp:85` (Hermitian `Bttr` boundary mass) is correctly identified as exercising the Hermitian-side of the law; the witness at line 90 (non-symmetric `Atn`) correctly exercises the non-Hermitian counterexample for non-law (general-M symmetry doesn't hold).

**(C) Operator distinct from matrix-weighted-norm?** Yes. The dispatch correctly identifies the distinction: bilinear-form has no SPD requirement on `M`, no outer sqrt, accepts non-Hermitian `M`, two distinct vector arguments. Matrix-weighted-norm (the sibling cycle-010 wave-1 dispatch) takes `x = y`, requires `B` SPD, and applies an outer sqrt — which makes it a strict specialisation of bilinear-form combined with a square-root step, not the same operator. The dispatch's Applicability Conditions section at CYCLE.md lines 322-335 makes this explicit and correctly distinguishes the operators.

### Summary

One high-severity content issue (conjugation-convention OQ rests on misreading the free-function `linalg::Dot` conjugation convention; the L0 source is actually self-consistent), one warning on skill-uptake (verify-citation-range non-invocation correlates with the citation-validity miss), and several low-severity tightenings. The structural shape of the rough-in (signature, laws, variant axes, applicability conditions, status framing) is sound; the conjugation analysis needs surgical correction.

## Critic notes for the repairer

- Issue 1 is the load-bearing one. Correcting it requires either: (a) closing the `bilinear-form-conjugation-convention-anchor` OQ with a "resolved-by-correction" note, or (b) reframing it as a 1-line L1>L0 lowering-convention pointer. The semantics prose at CYCLE.md lines 158-167 needs the L0 unfolding rewritten with the correct second-argument-conjugation convention for free-function `linalg::Dot`.
- Issue 1's correction also touches the *Status* §gating-reason #1 (firmness rationale) — the dispatch should re-evaluate whether firm-promotion is appropriate after closure.
- Issues 2-6 are tightenings; the repairer may bundle or skip per scope.
- The skill-uptake-survey warning is not a repair candidate; it is telemetry for the meta-phase.

## Repair

### Verification of critic's reading

Before applying any edits, verified the critic's analysis at the two cited source ranges:

1. **`reference/palace/palace/linalg/vector.cpp:674-685`** — confirmed: `LocalDot(ComplexVector x, ComplexVector y)` body assembles `{Re(x)·Re(y) + Im(x)·Im(y), Im(x)·Re(y) - Re(x)·Im(y)}`. For `x = a + bi`, `y = c + di`:
   - `xᴴ y = (a-bi)(c+di) = (ac+bd) + (ad-bc)i`
   - `yᴴ x = (c-di)(a+bi) = (ac+bd) + (bc-ad)i`
   - The function returns `(ac+bd) + (bc-ad)i = yᴴ x`. **The free-function conjugates the second argument.**
2. **`book/src/L1/dot.md:43, 104-105`** — confirmed: line 43 explicitly documents the L0-vs-L1 conjugation asymmetry ("the L1 signature names the conjugated argument first" while "the receiver is the linear argument and the call argument is the conjugated one" for the C++ method form); lines 104-105 reiterate ("Receiver-vs-argument asymmetry on the method form determines which side is conjugated... first argument is by convention the conjugated one" at L1). The L0/L1 conjugation asymmetry is already canonicalised in the firm `dot` chapter.

The critic's reading is correct: `linalg::Dot(comm, Ax, y) = yᴴ · Ax = yᴴ A x`, matching the L0 comment at `palace/linalg/operator.hpp:386`. There is no L0 disagreement.

### Fixes attempted

- **Finding (citation-validity, severity high)**: `bilinear-form-conjugation-convention-anchor` OQ rests on a misreading of `linalg::LocalDot`'s second-argument-conjugation convention; the dispatch incorrectly applied `dot.md`'s L1 first-argument-conjugation convention to the L0 free-function.
  - **Decision**: repaired.
  - **Action**: Applied four coordinated edits to `CYCLE.md`:
    1. **Summary section** — corrected the "two reasons" framing to one reason, with a repair note explaining the correction (CYCLE.md lines 29-44).
    2. **Context section (inside `edit:book/src/L1/bilinear-form.md` block)** — corrected the "two unresolved issues" sentence to name only the variant-axis-coverage gating reason, with a repair note (CYCLE.md lines 101-109).
    3. **Semantics §"Composition into `apply_linop` + `dot`" (inside edit block)** — replaced the false "Palace L0 implementation realises a *different* unfolding" / "three-way ambiguity" prose with the correct analysis: L0 returns `yᴴ A x` via second-argument-conjugation, matching the L0 comment; the L1>L0 lowering is conjugation-asymmetric but the asymmetry is the same one already documented in `dot.md`. Named both mechanical L1>L0 unfolding shapes (argument-swap vs outer-`conj`) (CYCLE.md lines 171-197).
    4. **Conjugation convention sub-section (inside edit block)** — explicitly noted that the Palace L0 free-function form uses second-argument-conjugation as documented at `book/src/L1/dot.md:43, 104-105`, and stated "There is no L0 ambiguity" (CYCLE.md lines 209-218).
    5. **Status section (inside edit block)** — removed false gating reason #1, leaving only the variant-axis-coverage gating reason; added repair note flagging that the integrator may consider whether the rough-in is now firm-promotion-eligible (CYCLE.md lines 376-396).
    6. **L1 vs L0 distinction section (inside edit block)** — surfaced the L0/L1 conjugation handedness explicitly in both bullets, including reference to `book/src/L1/dot.md:43, 104-105` (Issue 2 tightening); the L0 bullet now states `linalg::Dot(comm, A·x, y) = yᴴ A x` matches the L0 comment (CYCLE.md lines 408-426).
    7. **Evidence section (inside edit block)** — added a clarifying sub-bullet on the complex-`A` overload citation tying the L0 implementation back to the L0 comment via the documented second-argument-conjugation convention (CYCLE.md lines 437-444).
    8. **`bilinear-form-conjugation-convention-anchor` OQ (outside edit block)** — closed by changing status to `resolved-by-correction` and replacing the body with a full explanation of the misreading, the verification, and the canonical L0/L1 asymmetry reference. The OQ is now load-bearing only as documentation of the resolution path; it will not propagate to `scaffolding/open-questions.md` as an active question (CYCLE.md lines 580-620).
    9. **`book/src/L1/index.md` proposed-changes block (cohort listing)** — corrected the "rough-in status motivated by (a) unresolved L0 conjugation-convention ambiguity and (b) narrow variant-axis coverage" phrasing to just the variant-axis-coverage reason (CYCLE.md lines 501-506).

- **Finding (skill-uptake-survey, warning)**: `verify-citation-range` non-invocation correlates with the citation-validity miss.
  - **Decision**: unrepairable (telemetry only).
  - **Rationale**: Per critic notes for repairer §"skill-uptake-survey warning is not a repair candidate; it is telemetry for the meta-phase." Surfacing the pattern is meta-phase work, not repair work. The pattern (verify-citation-range non-invocation correlating with downstream citation-validity miss across multiple cycle-010 reports) is candidate-skill-uptake-policy material; flagging here for the cycle-012 meta-phase batch examination.

### Unrepairable findings

- **skill-uptake-survey warning** — not mechanically repairable; this is telemetry for the meta-phase, not a content defect. No follow-up agent assignment needed — the pattern will surface in the next meta-phase batch via the integrator-signals channel.

### Tightenings not addressed (per critic's "Issues 2-6 are tightenings; the repairer may bundle or skip per scope")

- **Issue 2** (L0/L1 dot.md conjugation asymmetry not surfaced in L1-vs-L0 section) — addressed in the L1 vs L0 distinction edit above.
- **Issue 3** (Atn non-symmetry citation pointer one line off-claim) — not addressed; the citation pointer is in the proposed L1 chapter body and the integrator can either accept the slight imprecision (the non-symmetry is documented adjacently at `boundarymodeoperator.cpp:38` with the `Btn = -Atnᵀ` comment, which is downstream-firm evidence) or flag for harvester revisit. Low severity; out of repair scope.
- **Issue 4** (slug-name OQ over-elaborated) — not addressed; OQ pruning is meta-phase / integrator domain. Low severity.
- **Issue 5** (variant-axis OQ table treats real case inconsistently) — not addressed; resolving the inconsistency requires deciding which framing is canonical (the Signature treatment of real-`x` as out-of-Palace-surface vs the OQ's treatment as a coverage gap). That decision is substantive (it picks a convention) and belongs with the harvester or layer-intro-author, not the repairer. Low severity.
- **Issue 6** (firm-promotion gating conditional structure) — partially addressed: the Status section now names only one gating reason (post-correction), and the repair note explicitly flags that the integrator should consider whether single-gating-reason is sufficient to hold rough-in. Whether to firm-promote on this dispatch alone is integrator authority.

## Suggested resolution

**`pass-after-repair`** — the load-bearing citation-validity issue has been fully resolved by in-place correction:

1. The false OQ premise is reframed as resolved-by-correction with explicit verification of the L0 free-function convention against `palace/linalg/vector.cpp:674-685`.
2. The Semantics section's L0 unfolding analysis is corrected: L0 returns `yᴴ A x` matching the L0 comment.
3. The L1>L0 lowering composition note now correctly identifies the L0/L1 conjugation asymmetry (inherited from `dot.md`) and names the two equivalent mechanical lowerings.
4. The Status section's gating-reason list is corrected to a single remaining reason (variant-axis coverage).
5. The L1 vs L0 distinction now explicitly surfaces the conjugation handedness on both sides (addressing Issue 2).

The L1 entry's core semantics (`bilinear_form(x, M, y) = xᴴ M y`, the six unconditional algebraic laws, the two conditional Hermitian-M laws, the four variant axes, the applicability conditions, and the dependency structure) remain sound and untouched. The corrections are surgical and confined to (a) the prose that *interpreted* the L0 implementation through the wrong conjugation convention and (b) the OQ that was opened as a result.

**Notes for the integrator**:

- The dispatch is ready for `integrator-per-report` application. The `bilinear-form` L1 entry will land as a rough-in with one remaining gating reason (narrow variant-axis coverage), per the corrected Status section.
- Per the corrected Status repair note: the integrator may consider whether the variant-axis-coverage gating reason alone (with two M-symmetry witnesses already exercised, and the unweighted M=I case firm via `dot`) is sufficient to hold the entry below firm-promotion threshold, or whether the rough-in is firm-promotion-eligible immediately. The dispatch defers to integrator authority on this; the repair leaves the firmness as `rough-in` per the dispatch.
- The three remaining OQs in this dispatch are: `bilinear-form-real-vector-coverage-gap`, `bilinear-form-slug-name-coordination`, `bilinear-form-variant-axis-test-coverage`. The fourth OQ (`bilinear-form-conjugation-convention-anchor`) is `resolved-by-correction` and should NOT propagate to `scaffolding/open-questions.md` as an active entry — it is now in-CYCLE documentation only.
- The cycle-010 critic's skill-uptake-survey warning on verify-citation-range non-invocation should surface in the cycle-012 meta-phase batch examination (per the critic's note "second cycle-010 report where verify-citation-range non-invocation correlates with a downstream citation-validity miss").
