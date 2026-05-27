---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T223000Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-27T230000Z
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

# META: verification of harvester-matrix-weighted-norm-l1

## Critique

### Checks run

**citation-validity** — Verified all source-side anchors against Palace tree. The two primary anchors verified positively: `palace/linalg/operator.cpp:599-619` contains exactly the two `Norml2(comm, x, B, Bx)` template specializations for `Vector` and `ComplexVector`, including the `MFEM_ASSERT(dot > 0.0, ...)` guard in the real case and the `MFEM_ASSERT(dot.real() > 0.0 && std::abs(dot.imag()) < 1.0e-9 * dot.real(), ...)` guard in the complex case — matching the report's narrative precisely. The eigensolver-backend cohort (ARPACK, SLEPc, NLEPS) verified: `palace/linalg/arpack.cpp:438` is `linalg::Norml2(comm, x, *opB, Bx)`; `palace/linalg/slepc.cpp:475` and `palace/linalg/nleps.cpp:114` mirror that pattern; the `xscale.get()[i] = 1.0 / GetEigenvectorNorm(...)` scaling pattern is consistent across arpack:470, slepc:505, nleps:146. **Issue found**: the declaration anchor `palace/linalg/operator.hpp:372-374` is off by one — the actual `Norml2(...)` template declaration spans lines 372-373 (template line 372, function-signature line 373); line 374 is blank; the comment `// Calculate the vector norm with respect to an SPD matrix B.` is at line 371. The downstream L0 chapter `book/src/L0/linalg-operator-file.md` cites line 374 for the same declaration, so the off-by-one is inherited and consistent within the layered artifact, but it does not match the underlying source. Marking `warning`, not `fail`, because the cited range still contains the declaration (and the inherited inconsistency is not this report's to fix).

**surface-or-evidence** — Pass. This is a new-operator authoring (not a refinement of an existing operator/theme), so the surface-or-evidence-for-refinement rule does not bind. The closed-form definition `√(xᴴ B x)` is anchored both in the L0 source comment ("Calculate the vector norm with respect to an SPD matrix B." at `palace/linalg/operator.hpp:371`) and in the implementation behaviour (`B.Mult(x, Bx); dot = Dot(comm, Bx, x); return std::sqrt(dot)`). The L0 anchor is unambiguous and the proposed L1 surface is justified by it.

**rotation-quality** — Pass. The L_{n+1}→L_n rotation here is L1→L0; the L1 form is `α = matrix_weighted_norm(x, B) :: (Tensor, LinearOperator) → Scalar`, the L0 form is the three-step composition with caller-supplied workspace `Bx`, real/imaginary-part decomposition for the complex specialization, MPI collective inside `Dot`, and the `MFEM_ASSERT` defensive guard. The L1 form is **strictly more compact** (workspace `Bx` absorbed; element-type plumbing absorbed; MPI absorbed; defensive assertion lifted to explicit applicability condition) and **strictly more equational** (12 algebraic laws stated, including the closed-form identity `‖x‖² = xᴴ B x`). The Composition note explicitly states the unfolded form `√(dot(apply_linop(B, x), x))` is L1>L0 lowering-theme territory, not L1 semantics — consistent with the post-cycle-009 invariant "Layers are defined high→low; lifting notes go in working notes" (higher-layer entry defined in its own vocabulary, not in terms of L0 unfolding). This is well-disciplined L1 vocabulary.

**variant-axis-coverage** — Pass. Two orthogonal axes identified at L1: `element-type` (real | complex) and `output-arg vs return-value pattern`. Both are explicitly justified for collapse at L1 (the SPD precondition guarantees the result is real regardless of input element-type; the L1 form picks return-value uniformly). Two absorbed axes additionally noted: `parallel-wrapper` (MPI comm absorbed; reappears in L1>L0 lowering) and `operator-representation of B` (inherited from `apply_linop`'s variant absorption). One residual variant question scoped out explicitly: the "complex-x with real-B" sub-variant (Open question #2 — `matrix-weighted-norm-mixed-element-type-variant`). The scope-out is explicit and routes to a future OQ, satisfying the variant-axis-coverage invariant for rough-in status.

**cross-reference-integrity** — Pass. All `[link]` references resolve: `book/src/L0/linalg-operator-file.md` exists and contains the cited matrix-weighted free-function block at lines 30-33; `book/src/L0/mutable-workspace-pattern.md` exists; `book/src/L1/dot.md` and `book/src/L1/apply_linop.md` are both firm and contain the cited algebraic-law anchors (dot's law 7 conjugate-linearity-left is at dot.md:64; apply_linop's law 1 linearity-in-x is at apply_linop.md:46). The "Queued" line in `book/src/L1/index.md:51` for `nrm2_B` exists exactly as quoted (the diff is faithful). The OQ slug `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` exists in `scaffolding/open-questions.md:1359`. Priority #17 exists at `scaffolding/priorities.md:36`. The naming-axis observation (L0 chapter uses `nrm2_weighted`, OQ uses `matrix-weighted-norm`, index uses `nrm2_B`) is empirically confirmed by direct grep. The sibling-boundary statement in `book/src/L1/nrm2.md:13` is verbatim-quoted faithfully.

**edge-label-fidelity** — Pass (not strictly applicable — this is a new operator, not a refinement carrying an edge label). The report's "L1 vs L0 distinction" section discusses the L1→L0 lowering direction in narration form; while the entry is L1-only, the prose around the rotation correctly identifies what stays at L1 vs what gets pushed to the L1>L0 theme. No mis-labeled edges.

**plan-kind-consistency** — Pass. The dispatch is declared `rough-in (test-coverage-bounded)`. The frontmatter `status: pending` is correct (pre-integrator). The rough-in status is well-justified: no dedicated test exercising `linalg::Norml2(comm, x, B, Bx)` exists at `test/unit/test-vector.cpp:209-211` (which covers only the unweighted method form `Vector::Norml2()`) — verified by direct read. Three promotion gates are explicitly named (direct test, indirect eigensolver-test coverage, algebraic-law completeness verification) and aligned with the cycle-009 `eigsolve` precedent. The content shape — well-anchored signature + 12 laws + dense callsite evidence + no dedicated test — matches the `rough-in (test-coverage-bounded)` shape exactly. No mis-classification.

**skill-uptake-survey** — Warning. The report's shape implies at least three relevant skills could have been invoked: `verify-citation-range` (high relevance — the report cites a dozen+ source ranges; the off-by-one on the `.hpp:372-374` decl might have been caught), `classify-variant-axis` (high relevance — two orthogonal axes plus two absorbed axes, exactly the skill's use case), and `verify-refinement-surface` (lower relevance since this is new-operator authoring, not refinement). None are referenced or invoked in the report. Telemetry-only — not blocking, but worth flagging that the skill-discovery channel is under-utilised on this dispatch.

### Issues found

1. **citation-validity / off-by-one on decl range** (CYCLE.md frontmatter L0 anchor; Operator-content "Context" §; multiple places). The cited range `palace/linalg/operator.hpp:372-374` for the `Norml2(comm, x, B, Bx)` template declaration is off by one. Actual: template-line is 372, declaration-line is 373, line 374 is blank. The leading comment `// Calculate the vector norm with respect to an SPD matrix B.` is at line 371. Suggested replacement: `palace/linalg/operator.hpp:371-373` (includes the SPD-anchor comment) or `palace/linalg/operator.hpp:372-373` (the template + declaration alone). Severity: low — the declaration is still inside the range, but the range is mis-stated. Note: the L0 chapter `book/src/L0/linalg-operator-file.md:31, 113` makes the same off-by-one (cites line 374 for the signature); fixing here without also fixing the L0 chapter creates a cross-artifact inconsistency, which is an integrator-coordination issue. Tracking only — the artifact-wide reconciliation is integrator scope.

2. **citation-validity / `arpack.cpp:433-444` vs actual function range** (CYCLE.md "Evidence" §). The function `ArpackEigenvalueSolver::GetEigenvectorNorm` actually spans lines 433-444 (definition body lines 434-444; signature line 433-434). The report cites `433-444`. **Verified — correct.** No issue. (Recorded here as the verification trail.)

3. **citation-validity / SLEPc and NLEPS ranges off by a line** (CYCLE.md "Evidence" §). `palace/linalg/slepc.cpp:470-481` — the function `SlepcEigenvalueSolver::GetEigenvectorNorm` actually spans 470-481 (signature 470-471, body 472-481). **Verified — correct.** `palace/linalg/nleps.cpp:109-119` — actual range is 109-120 for the full function definition (signature 109-110, body 111-120). Report cites `109-119` (clipping last brace line). Severity: trivial — the body's behavioural lines are all within `109-119`, the off-by-one omits only the closing brace.

4. **algebraic-laws / law 6 separation-condition over-specification** (Operator content "Algebraic laws" §, law 6). The "Cauchy–Schwarz in the B-inner-product" equality condition states "with equality iff `x` and `y` are linearly dependent **modulo the null space of `B`** (in exact arithmetic)". This is the SPSD-not-just-SPD-aware statement; the law itself is otherwise SPD-conditioned. The "modulo the null space of `B`" parenthetical only fires for SPSD `B` (under SPD, the null space is `{0}` and "linearly dependent modulo `{0}`" is just "linearly dependent"). This is correct but the prose mixes the SPD and SPSD cases without an explicit guard. Severity: low — the law as stated is mathematically true under both SPD and SPSD `B`. Could be clarified.

5. **algebraic-laws / law 7 parallelogram identity scope** (Operator content "Algebraic laws" §, law 7). The parallelogram identity is stated to hold "because the B-inner-product `⟨x, y⟩_B` is a genuine inner product when `B` is SPD." Mathematically, the parallelogram identity holds for any **semi**-inner-product (SPSD `B` suffices); the identity is purely algebraic and does not require non-degeneracy. The report's framing under-states the law's scope (it would hold under the weaker SPSD condition that already governs laws 1, 4, 5). Severity: low — the law as stated is correct under the strictly-SPD condition; the weaker SPSD-sufficient framing would be more accurate but is a refinement, not a fix.

6. **algebraic-laws / law 8 self-bilinear-identity wording** (Operator content "Algebraic laws" §, law 8). The "L0 source factors as `B.Mult(x, Bx); dot = Dot(comm, Bx, x); return std::sqrt(dot)`" citation references `palace/linalg/operator.cpp:601-606`. Direct read confirms lines 601-606 hold the body for the real specialization (`B.Mult(x, Bx)` at 601, `Dot` at 602, `MFEM_ASSERT` at 603-604, `return std::sqrt(dot)` at 606). **Verified — correct.** No issue.

7. **algebraic-laws / law 10 diagonal-scaling form for complex** (Operator content "Algebraic laws" §, law 10). The diagonal-scaling formula `matrix_weighted_norm(x, D) = √Σ_i d_i · |x[i]|²` is stated for "a diagonal SPD operator `D = diag(d_1, ..., d_N)` with `d_i > 0`". For complex `x`, the formula uses `|x[i]|²` (modulus squared), which is the correct Hermitian form since `conj(x[i]) · (D·x)[i] = conj(x[i]) · d_i · x[i] = d_i · |x[i]|²`. **Verified — algebraically correct.** No issue.

8. **skill-uptake-survey / no skill invocations recorded** (full report). The report does not reference any skill invocations. Both `verify-citation-range` and `classify-variant-axis` were relevant. The off-by-one citations in issue #1 and #3 are exactly the class of artifact that `verify-citation-range` is designed to catch. Severity: low (telemetry-only per skill-uptake-survey policy).

9. **wave-1 coherence with sibling dispatches** (Proposed-changes §, "Change 4" coordination note). The report explicitly addresses the wave-1 coordination question: it notes the planner may also be dispatching `bilinear-form` and possibly a `nrm2_B-weighted` slug; the report names this entry as the `matrix-weighted-norm` slug per planner directive and proposes a path for the integrator if `nrm2_B-weighted` is collapsed (merge into this entry) or kept distinct (serialise as adjacent rows). The proposed L1/index.md diff edits the "Queued" list to (a) remove the old `nrm2_B` line and (b) add a forward-pointer mentioning that the matrix-weighted-norm half of cycle-008 OQ `matrix-weighted-norm-and-bilinear-form-l1-rough-ins` is now landed and the `bilinear-form` half remains queued — this is the correct coordination posture. The SUMMARY.md diff adds a single line after `eigsolve`. **Pass on coherence**; the report has anticipated the merge scenario and given the integrator clear guidance.

10. **OQ ledger naming-axis residue** (Open questions / caveats §#1). The "naming reconciliation across artifacts" OQ proposes a future cross-layer cross-cutter sweep to swap `nrm2_weighted` for `matrix-weighted-norm` at `book/src/L0/linalg-operator-file.md:30-33, 73, 88`. This is correctly scoped out of integrator authority (the L0 chapter is informational on L1 naming, not authoritative). Recommend the integrator append the new OQ slug `matrix-weighted-norm-naming-sweep` to `scaffolding/open-questions.md` per the report's recommendation.

11. **methodology-discipline check (positive)** (Composition note §, "L1 vs L0 distinction" §). The report explicitly observes the post-cycle-009 invariant: "**The L1 operator is defined by the closed-form `√(xᴴ B x)`; the unfolding into three sub-operations belongs in the (not-yet-authored) `matrix-weighted-norm-mutation-rotation` L1>L0 theme**." This is the in-spirit application of the "Layers are defined high→low; lifting notes go in working notes" invariant — the L1 entry stays in L1 vocabulary, the L1→L0 unfolding is pushed to the lowering theme. **Pass on methodology discipline**; this is exemplar usage of the new invariant.

## Repair

### Fixes attempted

- **Finding 1 (citation-validity / off-by-one on `palace/linalg/operator.hpp:372-374`)**
  - **Decision**: not-needed (finding does not replicate).
  - **Action**: Verified actual file content directly via `Read` and `grep -n`. Results:
    - `palace/linalg/operator.hpp:371` — blank line (after `namespace linalg {` opener at 369-370).
    - `palace/linalg/operator.hpp:372` — `// Calculate the vector norm with respect to an SPD matrix B.` (the SPD-anchor comment).
    - `palace/linalg/operator.hpp:373` — `template <typename VecType>`.
    - `palace/linalg/operator.hpp:374` — `double Norml2(MPI_Comm comm, const VecType &x, const Operator &B, VecType &Bx);` (the function-signature line).
    - `palace/linalg/operator.hpp:375` — blank line.
  - **Result**: the report's range `372-374` correctly covers comment + template + signature, and the L0 chapter's narrower citation `374` correctly points at the signature line itself. The critic's "off-by-one" verdict was itself based on a misread of the file (the critic asserted comment at 371 / template at 372 / signature at 373 / blank at 374; actual content is offset by one in the other direction). No fix applied; cross-artifact reconciliation is moot because both citations are already correct.
  - **Rationale for tracking**: this is exactly the kind of artifact `verify-citation-range` skill is designed to surface; recorded as a `skill-uptake-survey` lesson rather than a citation error.

- **Finding 2 (skill-uptake-survey / no skill invocations recorded)**
  - **Decision**: not-needed (telemetry-only, not mechanically repairable).
  - **Action**: None. Per skill-uptake-survey policy, this is informational. The lesson — that `verify-citation-range` would have prevented even the critic-side misreading uncovered in Finding 1 above — is recorded here for the meta-phase pattern survey.

- **Minor algebraic refinement (law 7 parallelogram identity SPSD scope, raised in critic Issues §5; not flagged as a check warning)**
  - **Decision**: repaired (one-clause SPSD-applicability clarification, inline).
  - **Action**: Edited `CYCLE.md` Operator-content "Algebraic laws" §, law 7: renamed to "Parallelogram identity (SPSD sufficient)" and added the clause "the identity itself is purely algebraic and holds for any semi-inner-product (SPSD `B` suffices — non-degeneracy is not required)." The substantive law and its derivation are unchanged; the clause restores parity with laws 1 and 4 which are already SPSD-conditioned.
  - **Rationale**: borderline-mechanical (one-clause guard, no new derivation, parity with adjacent laws); leaning into the dispatcher's explicit "if you can add a one-clause SPSD-applicability guard inline, do so" instruction.

- **Minor algebraic refinement (law 6 Cauchy–Schwarz mixed SPD/SPSD prose, raised in critic Issues §4; not flagged as a check warning)**
  - **Decision**: not-needed (under-stated, not wrong; the existing "modulo the null space of `B`" parenthetical already silently handles the SPSD case).
  - **Action**: None. The existing prose is mathematically correct under both SPD and SPSD; a stronger SPSD-applicability re-write would author substantive new content and is out of repair scope.

### Unrepairable findings

None. Both warning checks resolve as `not-needed`: Finding 1 is a non-issue (citation is correct; critic's verdict was itself based on a misread), Finding 2 is telemetry-only.

## Suggested resolution

`overall_status: ready`. The report is integrator-eligible as-is. No follow-up agent is needed.

Notes for the integrator:
- Both the report's citation `palace/linalg/operator.hpp:372-374` and the L0 chapter's citation `palace/linalg/operator.hpp:374` correctly anchor the `Norml2(comm, x, B, Bx)` declaration. No cross-artifact reconciliation is required for this citation.
- A one-clause SPSD-applicability guard has been added inline to law 7 in `CYCLE.md`; the proposed-changes block for `book/src/L1/matrix-weighted-norm.md` includes the updated law text. No other content changes.
- The naming-axis OQ (`matrix-weighted-norm-naming-sweep`) and the lowering-theme OQ (`matrix-weighted-norm-mutation-rotation-l1-l0-theme`) noted in the report's "Open questions" §1 and §3 should be appended to `scaffolding/open-questions.md` per the report's recommendations; the bilinear-form sibling half of the cycle-008 OQ should be marked `partially-answered`.
- `skill-uptake-survey` warning is telemetry-only; surface to meta-phase pattern survey at cycle-012 closure (priority: low; the finding is procedural, not content).
