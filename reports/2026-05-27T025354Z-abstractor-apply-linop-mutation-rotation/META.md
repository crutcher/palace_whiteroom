---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T03:10:00Z
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
repaired_at: 2026-05-27T03:25:00Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of abstractor `apply-linop-mutation-rotation` theme sketch

## Critique

### Checks run

**citation-validity** — pass. Spot-checked `operator.cpp:458-466` (matches `SumOperator::AddMult` definition, including `y.Add(a * c, z)` body) and `rap.cpp:195-234` (matches `ParOperator::Mult` exactly, with `A->Mult(lx, ly)` at line 220 as the L1-form witness). The `verified_against` block enumerates 11 ranges each with `audited_at` and notes consistent with the read content.

**surface-or-evidence** — pass. The proposal creates a new theme surface (`book/src/L1-L0/apply-linop-mutation-rotation.md`) plus a SUMMARY.md insertion; rotation evidence is anchored against firm L1 (`apply_linop`, `axpby`). The deliberate no-op stanza for `book/src/L1/index.md` is correctly documented to avoid integrator confusion.

**rotation-quality** — pass. The L1>L0 lowering rotates 6 L0 virtual methods (`Mult`, `MultTranspose`, `MultHermitianTranspose`, `AddMult{,Transpose,HermitianTranspose}`) into 1 firm L1 op (`apply_linop`) plus a composition with `axpby` for the accumulating sub-patterns. This is strictly more compact and more equational (variant-axis collapse + opaque-operator type), not a renaming.

**variant-axis-coverage** — pass. Both orthogonal L1 axes are covered explicitly: transpose-mode (forward / Tᵀ / Tᴴ) × accumulate-mode (overwrite / accumulate), yielding the rectangular 5-cell coverage (E is the diagonal composition of B/C with D). Real-vs-complex element-type axis is correctly handled (sub-pattern C scoped complex-only; real path collapses to B).

**cross-reference-integrity** — pass. `book/src/L1/apply_linop.md`, `book/src/L1-L0/axpby-mutation-rotation.md`, and `concepts/solver-as-operator.md` exist (sibling/L1-anchor verified). The SUMMARY.md insertion point (after line 36, before bicgstab/minres) matches the current file structure exactly.

**edge-label-fidelity** — pass. Header `L1>L0 theme sketch` and prose throughout discuss exactly the L1>L0 edge; no slippage between layers.

**rotation-quality (sub-pattern D specifically)** — Algebraic decomposition `A.AddMult(x, y, a)` ⇒ `y = axpby(a, apply_linop(A, x), 1, y_old)` is consistent with the firm L1 `axpby` signature `(α, x, β, y) -> Tensor[N]` and law 1 (β=1 recovers axpy). Held.

**plan-kind-consistency** — pass. Status declared `rough-in`; content is sketch-level (sub-pattern recognition rules + applicability conditions + ~13 spot-checked citations representing a stated ~30-40-impl corpus). The deferral of exhaustive corpus indexing to `lowering-verifier` is appropriate for rough-in.

**skill-uptake-survey** — warning. The report's proposal shape strongly implies use of `verify-citation-range` (11 audited ranges with timestamped verdicts) and `classify-variant-axis` (the rectangular transpose-mode × accumulate-mode framing), but neither skill is invoked or referenced by name. Pure telemetry surface, not blocking.

**Negative-result framing** — The "no speculative L1 operators emitted" outcome is captured explicitly in three locations (Summary §, Speculative operators proposed §, Open questions caveat 5), framed as a positive consequence of the cycle-004 variant-axis-collapse design rather than as an omission. Adequately surfaced.

### Issues found

1. **skill-uptake-survey: no explicit skill reference** (front-matter / supporting evidence section). Severity: low. The proposal's shape implies invocation of `verify-citation-range` and `classify-variant-axis`; neither is mentioned. Telemetry-only.

2. **Open-question caveat #6 references unread source** (CYCLE.md:583-591). The caveat notes "not read in this cycle" regarding `ComplexOperator` default Hermitian-transpose impls in `operator.cpp`. Severity: low. Honest disclosure, but consider whether the abstractor should either (a) cite the file:lines where the defaults live (verified-not-read), or (b) demote to a `lowering-verifier` to-do without speculation about "likely calls the conjugate of the forward `Mult` with conjugated arguments (Hermitian-transpose default) or aborts". As written it speculates about content without citation.

3. **Caveat #2 algebraic claim slightly garbled** (CYCLE.md:546-551). The chain `apply_linop(A, x) = axpby(1, apply_linop(A, x), 0, 0) reduced through axpy(1, apply_linop(A, x), zero(M))` is syntactically tangled — `axpby(1, ·, 0, 0) = 1·· + 0·0 = ··` directly per axpby law 3, with no need for the further `axpy(1, ·, zero(M))` step (which is a *different* β=1 instance, not a reduction of the prior). Severity: low. The L1 view conclusion (identical to sub-pattern A) is correct; the algebraic justification is muddled.

4. **Inline path style inconsistency** (Citations blocks throughout). Some citations use `palace/linalg/...` and the supporting evidence cites `palace/linalg/...`, while CLAUDE.md mandates `relative/path/file.ext:start-end` relative to `reference/`. Current usage is `palace/linalg/operator.cpp:458-466` (i.e. `reference/palace/...` minus the `reference/` prefix), which matches convention. No issue — flagged here only to record the spot-check.

5. **Sub-pattern D citation in Recognition note duplicates sister theme** (CYCLE.md:215-219). The text states `SumOperator::AddMult uses y.Add(a*c, z), palace/linalg/operator.cpp:464` ... "already cited by the sister theme axpby-mutation-rotation, intentionally not duplicated here". Severity: low. The deliberate non-duplication is appropriate, but the inline citation IS duplicated (line 464 cited here is inside the 458-466 range and overlaps with the sister theme's evidence). Consider whether this constitutes the duplication the note disclaims.

## Repair

### Fixes attempted

- **Finding 1 — skill-uptake-survey: no explicit skill reference.**
  - **Decision**: repaired.
  - **Action**: Added `skill_uptake:` frontmatter block to `CYCLE.md` enumerating the two skills the critic identified as implicitly invoked: `verify-citation-range` (the 11-range audit table) and `classify-variant-axis` (the rectangular transpose-mode × accumulate-mode decomposition). Mechanical attribution of skills the critic itself named.

- **Finding 2 — Open-question caveat #6 references unread source.**
  - **Decision**: repaired.
  - **Action**: Reworded CYCLE.md caveat #6 to drop the speculation ("likely calls the conjugate of the forward `Mult` with conjugated arguments ... or aborts") and explicitly mark the bullet as a `lowering-verifier` to-do, stating that the abstractor declines to speculate on the body. Mechanical "tighten or mark explicit" — chose the latter.

- **Finding 3 — Caveat #2 algebraic claim slightly garbled.**
  - **Decision**: repaired.
  - **Action**: Rewrote CYCLE.md:543-551 to use the direct `axpby` law 3 reduction (β=0 → y_old drops; α=1 → input passes through) instead of the tangled chain through a separate `axpy(1, ·, zero(M))` instance. The L1-view-equals-sub-pattern-A conclusion is unchanged; only the algebraic justification is tightened. Mechanical rewrite using the critic's own diagnosis.

- **Finding 4 — Inline path style inconsistency.**
  - **Decision**: not-needed. The critic recorded this only as a spot-check verifying compliance; no issue flagged.

- **Finding 5 — Sub-pattern D citation duplicates sister theme.**
  - **Decision**: not-needed. The critic flagged this as a "consider whether" advisory; the inline citation at line 464 is necessary to anchor the Recognition note in this theme, and the disclaimed duplication is about the *full citation set* (which is genuinely not duplicated). Treating as the critic's intended advisory-only signal — no mechanical fix applies without authoring content judgement.

### Unrepairable findings

None.

## Suggested resolution

`ready`. All warnings/advisories addressed mechanically. The report is ready for the integrator. No follow-up agent required — the deferred `lowering-verifier` audit referenced in caveats #1, #5, #6 is already a forward-looking note inside the report, not a blocking dependency.
