---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T19:05:00Z
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

# META: verification of the §1.2.2-R residual opaque-`LinearOperator[…]` calculus-codomain sweep (lifter c130 D2)

## Critique

### Checks run

**citation-validity — pass.** Every claim in the report cites a real, in-range location. The load-bearing anchors were confirmed mechanically with `citecheck --anchor`: the §1.3.1 exemplar codomain `mk_matrix_free_operator.md:60` (`Op[Tensor[(N: ...)] → Tensor[(N: ...)]]`) — anchor `ok` at line 60; the sibling-cap settled return `assemble_frequency_operator.md:99` (`LinOp[(N: ...), $N]`) — anchor `ok` at 99; the §1.2.2 rank-1-keep clause `semantics/index.md:95` (`flat dof-vector`) — anchor `ok` at 95; the §1.2.2-R discriminator ruling `semantics/index.md:150-158` (`non-compliant smell`) — anchor `ok` at 154/158; the square-op forms `semantics/index.md:89-95` (`LinOp[(S: ...), $S]`) — anchor `ok` at 93. The report's frontmatter cites the D1 ruling as "§1.3.1 lines 87-168" and the summary as "lines 150-158"; both ranges enclose the actual discriminator table (150-154) and the prose ruling (158) and are in-range (slightly loose, not a defect). The dep-map mirror row is correctly identified as `L4-L3/index.md:46` (verified). No YAML round-trip sub-check applies (no `verified_against:` block).

**surface-or-evidence — pass.** This is a pure prose/signature FIDELITY sweep (no status/rank/edge/maturity change), explicitly scoped as such; the surface modified is the codomain spelling, and the evidence is the D1-pinned §1.2.2-R discriminator + the already-settled in-file/sibling-cap spellings each conversion aligns to. No record is newly named in a signature here (the record-definition sub-check is moot — `FrequencyOperatorFamily` / `{K,C,M}` are pre-existing and out of scope). The c129-D2 `{K,C,M}` rank-1 record-field carve-out is correctly identified and left untouched (see edge-label-fidelity).

**rotation-quality — pass (not applicable).** No algebraic/structural/reduction rotation is asserted — this is a spelling re-anchor, not a lowering or abstraction. No L_{n+1}/L_n compaction claim to evaluate.

**variant-axis-coverage — pass (not applicable).** No new operator/theme with orthogonal variant axes is introduced; the sweep does not touch the variant-axis structure of any chapter.

**cross-reference-integrity — pass.** All edits are in-place string replacements in existing chapters; no new files, no new links, no SUMMARY wiring change. Every edit `old_string` was confirmed present on-disk in the named file (fe-assemble-fold-dissolution sigs at :30/:37; the seven fe_assemble.md monoid-carrier mentions; mk-matrix-free at :104/:122/:151/:370; frequency_sweep:151; index.md:46). The dep-map mirror at `L4-L3/index.md:46` stays consistent with the converted theme-LHS (§3): the quoted codomain `:: LinearOperator (Tensor[(N: ...)])` → `:: Op[Tensor[(N: ...)] → Tensor[(N: ...)]]`, matching the §3 edit-1 conversion, while the bare-word conceptual noun "matrix-free (un-materialized) `LinearOperator`" is correctly KEPT. The second mk-matrix-free mention in the by-kind list (`index.md:72`) carries no opaque type-application codomain (it narrates "flat-`Tensor[(N: ...)]`" prose without a `::`-codomain) and is correctly out of scope — no missed mirror.

**edge-label-fidelity — pass (the load-bearing check for this sweep).** Each CONVERT matches D1's pinned §1.2.2-R discriminator faithfully: every converted site is a genuine calculus operator-VALUE codomain (theme-LHS signature codomain, result-type line, constructor-call result annotation, or a within-cap monoid-carrier inside a file that already settled its own signature spelling at :35/:60/:71). Every KEEP is correctly a non-codomain: the bare-word English nouns at `mk-...:47,49,102,115` ("a matrix-free `LinearOperator` value") apply no bracket/paren args and so are NOT the opaque type-application form the discriminator targets (§1.2.2-R:158 explicitly targets "applies a bare type name to dimension/argument slots"); the `fe-...:3` theme-intro narrative monoid-carrier is correctly KEPT (no within-theme settled signature drives a same-file conversion, unlike the *cap* file). The c129-D2 dual-spelling carve-out is handled exactly right: the `{K,C,M}` rank-1 flat-dof record FIELDS at `assemble_frequency_operator.md:103-105` (verified on-disk as `LinearOperator[N, N]`) are out of scope and correctly stay rank-1 per §1.2.2:95, whereas `frequency_sweep:151` is a constructor-call RESULT ANNOTATION (`op_w = assemble_frequency_operator fam omega : …`) whose type must match that cap's settled `LinOp[(N: ...), $N]` return (:99/:293, verified) — correctly CONVERTed. No genuine rank-1 record field was incorrectly converted.

**plan-kind-consistency — pass.** Declared shape (lifter re-anchor / prose-signature fidelity sweep, no maturity change) matches the content exactly — every edit is a codomain re-spelling; frontmatter `status: pending` with no firmness/rank/edge mutation, consistent with the bounded fidelity scope.

**skill-uptake-survey — pass.** The report invokes `citecheck --anchor` for the §1.3.1 exemplar confirmation (cited in §Discipline notes and §Supporting evidence) — the relevant tooling for a citation-anchored fidelity sweep is referenced. Pure telemetry; non-blocking.

### Issues found

No issues. All eight checks pass. The sweep is a clean, faithful application of the D1-pinned §1.2.2-R discriminator.

Two items examined and cleared as **non-defects** (recorded for the integrator, not findings):

1. **Spelling-uniformity flag at `mk-matrix-free-operator-dissolution.md:151` (benign style choice, NOT a defect).** The report uses `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]` (verbatim from cap `mk_matrix_free_operator.md:60`) for the transcribed L4 constructor signature and `LinOp[(N: ...), $N]` (square-op) for the derived L3-form product, producing two spellings within the one theme file. Per `semantics/index.md:156` these denote the *same* square endomorphism and per :154 both `Op[...]` and `LinOp[...]` are sanctioned §1.2.2-compliant re-spelling targets. The report's rationale — match-the-cap-verbatim for the transcribed signature, square-op for the derived product — is principled and internally consistent, and the report flags the uniformity question without blocking. This is a benign style choice; if the integrator prefers a single uniform spelling across the theme, the :151 product could read `Op[Tensor[(N: ...)] → Tensor[(N: ...)]]`, but the current choice is correct as-is.

2. **Disambiguation of the two on-disk occurrences of the mk-matrix-free constructor signature (handled correctly).** The string `mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors -> LinearOperator (Tensor[(N: ...)])` appears twice on disk (the code-block form at :104 and the backtick-quoted supporting-evidence form at :370). The report's §3 edit-1 disambiguates by including the following comment line (`-- the operator-CONSTRUCTOR: build (once)…`, unique to :104), and §3 edit-4 targets the backtick-wrapped :370 form — so each integrator Edit call matches exactly one site. No ambiguity.

3. **Separable follow-up correctly deferred (not a defect).** The `fe-assemble-fold-dissolution.md:3` theme-intro monoid-carrier mention was KEPT and flagged as an optional separable consistency follow-up. This is correct narrative prose (a theme intro with no within-file settled signature driving a same-file conversion), not a smell; deferring it avoids over-reaching the named codomain sweep.
