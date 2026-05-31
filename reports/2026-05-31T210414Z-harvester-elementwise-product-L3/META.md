---
verifies: ../CYCLE.md
critiqued_at: 2026-05-31T212000Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-31T213000Z
repairer_version: 1
repairs:
  citation-validity: repaired
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

# META: verification of "Formalize elementwise_product at L3"

## Critique

### Checks run

**citation-validity — warning.** Ran `tools/citecheck/citecheck.py --scan` on the report: **16 ok, 0 failing** — all bounds + path-hygiene clean, confirming the report's claim that the one bare-`operator.cpp` AMBIG was resolved (both witnesses are fully qualified as `reference/palace/palace/linalg/operator.cpp`, distinguishing them from the second `reference/palace/palace/fem/libceed/operator.cpp` — verified two `operator.cpp` files exist; the report cites the correct `linalg/` one). Re-verified a sample of the load-bearing pinpoints with `--anchor` and by reading source: `operator.cpp:478-487` anchor `Y[i] = D[i] * X[i]` lands at 486 [ok]; `:545-568` anchor `MultHermitianTranspose` [ok]; `jacobi.cpp:30-39` `forall_switch` at 38 [ok] and the SetOperator chain at `:74-93` (`AssembleDiagonal → Reciprocal → *= omega` at 79-92) is exactly as described. The L1 anchors (`elementwise_product.md:41/:43/:99`) and `krylov-step-body-identity.md:97` ("L3-native by its signature shape") all resolve to the cited content. The warning is **one numeric-fidelity discrepancy, not a citation-bounds failure** (see Issues): the report describes the conjugate variant as "**three** sign flips on the cross-terms" (lines 84, 200) but the actual diff between the straight complex multiply (`operator.cpp:504-505`) and the conjugate (`:564-565`) is **two** sign changes, and the report's own line 84 contradicts itself by also saying "the two forms differ only in the sign of **two** cross-terms."

**surface-or-evidence — pass.** This is a `new:` firm L3 operator entry (an identity-in-form layer-coherence backfill), not a refinement of existing operator/theme surface. It modifies surface (creates `book/src/L3/elementwise_product.md`, inserts a SUMMARY row, adds an L3-index dep-map row) and carries an explicit identity-in-form rotation claim grounded in the firm L1 home + transitive L0 evidence. Not a pure rotation_claim-without-surface case. Pass.

**rotation-quality — pass.** The asserted rotation is L3→L1 identity-in-form. Per the project's "Identity-lowerings still require both L levels" invariant, an identity rotation is explicitly first-class and does NOT fail rotation-quality as a "renaming/1:1 mapping" would in the L_{n+1}-compaction sense — the L3 entry exists for layer-coherence, and the report correctly frames the *substantive* rotation as the L1>L0 `reciprocal-elementwise-product-mutation-rotation` (sub-pattern B), with the L3>L1 hop framed as layer-coherence, not algebraic compaction (line 173, 215). The "firm-on-positive-structure" rationale (every law a syntactic identity on the positive `BaseDiagonalOperator::Mult` multiply lambdas) is faithfully applied and matches the `apply_linop`/`assemble-diagonal`/`scal` precedents. The "no sequential obstruction / embarrassingly parallel" framing is faithful — `forall_switch` over `N` with one per-element multiply, no cross-element carry (confirmed at `operator.cpp:486`, `jacobi.cpp:38`); the sharpest-contrast-with-`chebyshev`/`eigsolve` framing is sound. Pass.

**variant-axis-coverage — pass.** Two variant axes declared and covered: (1) element-type (real | complex), collapsed to a parameterised operator with both source template specialisations witnessed (real `:478-487`, complex `:489-507`); (2) conjugation sub-axis on the complex side (straight `Mult` vs conjugate `MultHermitianTranspose`, `:545-568`), with the real side explicitly NOT carrying the axis (real `MultTranspose` aliases `Mult`). Non-axes are explicitly scoped out (constant-folding on `a`/`b` — confirmed no fast-path branch in source; operator-action-vs-free-binary — recovered by law 9, not a variant). No hidden branches. The frame matches the L1 entry's profile. Pass.

**cross-reference-integrity — pass.** Ran the fence-parity / build-readiness guard: `grep -n '\`\`\`'` returns 6 fences = 3 balanced blocks (`new:` 22-216, `edit:SUMMARY` 218-222, `edit:index` 224-228). The firm body is fully ENCLOSED in the `new:` fence — `## Status` (161), `## Signature` (56), `## Semantics` (76), `## Algebraic laws` (96), `## Evidence` (183) all sit inside the fence; the body's two signature blocks (58-59, 69-70) are **4-space-indented code, not nested ```text fences** (confirmed via `cat -A`), so the cycle-019 fence-truncation defect is absent. The "## Operator content"/"## Supporting evidence" sections after line 230 are the report's own meta-commentary OUTSIDE the fence (correct — not chapter body). Forward-references to the three not-yet-on-disk L3 chapters (`reciprocal`, `normalize`, `divfree-projector`) are written **plain-text** (verified those files do NOT exist on disk; lines 114, 129, 262); `book/src/L1/reciprocal.md`, `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md`, and all four concept pages exist and are live-linked. SUMMARY insert context (`scal` then `jacobi-smoother`) is consecutive in the current file (lines 29-30) so the surgical insert is valid; the L3-index `scal` and `jacobi-smoother` context rows reproduced in the `edit:` block match the current index byte-for-byte. Pass.

**edge-label-fidelity — pass.** The entry's lowering edge is L3→L1 (identity-in-form, no interposed L2 / no `L3-L2`/`L3-L1` theme file); the prose (§Lowers-to, §Downward, §L3-vs-L1) discusses exactly that edge and the transitive L1>L0 substantive rotation. No edge-label/prose mismatch. Pass.

**plan-kind-consistency — pass.** Declared kind: firm identity-in-form L3 backfill. Content shape matches — full firm apparatus (Signature, Semantics, 10 algebraic laws + non-laws, Variant axes, Status, Lowers-to, Lifts-from, Evidence) with no rough-in placeholders. The `firm` status is justified via firm-on-positive-structure (positive source, syntactic-identity laws, missing-test-does-not-gate), consistent with the cited cohort precedents. Pass.

**skill-uptake-survey — pass.** The report references `tools/citecheck/citecheck.py --anchor` for on-disk citation self-verification (lines 244-250) and names `upgrade-plain-text-ref-to-live-link-when-target-on-disk` as the follow-up skill for when the `reciprocal` forward-refs land (line 262). The `proposed-changes-fence-encloses-full-body-guard` and `summary-md-surgical-insert` shapes are not named by slug but their disciplines are visibly followed. Adequate uptake for this report shape. Pass.

### Issues found

1. **Conjugate-variant "three sign flips" is a numeric-fidelity error (should be two), and the report self-contradicts.** `CYCLE.md:84` ("three sign flips on the cross-terms; algebraically `ā ⊙ b`") and `CYCLE.md:200` ("three sign flips at `:564-565`"). Comparing the straight complex multiply at `operator.cpp:504-505` (`YR = DR*XR - DI*XI`, `YI = DI*XR + DR*XI`) with the conjugate at `:564-565` (`YR = DR*XR + DI*XI`, `YI = -DI*XR + DR*XI`) shows exactly **two** sign changes (`-DI*XI → +DI*XI`; `+DI*XR → -DI*XR`). The report's own `CYCLE.md:84` simultaneously states "the two forms differ only in the sign of **two** cross-terms," contradicting the "three" count in the same sentence-cluster. Severity: low (does not affect the algebraic claim `ā ⊙ b`, which is correct; the cited source ranges are in-bounds and the anchors land). Candidate fix: change "three sign flips" → "two sign flips" at lines 84 and 200 for internal consistency. (Note: line 152 says "three sign flips on the cross-terms" for `MultHermitianTranspose` as well — same correction applies there.)

2. **Minor wording slip — `MultTranspose` real-aliasing claim is asserted but not cited.** `CYCLE.md:152` states "the L0 real `MultTranspose` aliases to `Mult`" to justify the real side carrying no conjugation axis. This is plausible (real conjugation is identity) but no source line is cited for the aliasing; all other variant-axis claims carry a pinpoint. Severity: very low (the conjugation-is-identity-on-reals reasoning is self-evidently correct and the claim is non-load-bearing — it only supports a non-axis disambiguation). Candidate fix: either cite the real `MultTranspose` site or soften to "real conjugation is identity, so the variant collapses." Not blocking.

---

## Repair

### Fixes attempted

- **Finding 1 (citation-validity warning): conjugate-variant "three sign flips" should be "two".**
  - **Decision**: repaired.
  - **Verification (on-disk, source of truth)**: read `reference/palace/palace/linalg/operator.cpp:504-505` (straight `Mult`: `YR = DR*XR - DI*XI`, `YI = DI*XR + DR*XI`) and `:564-565` (conjugate `MultHermitianTranspose`: `YR = DR*XR + DI*XI`, `YI = -DI*XR + DR*XI`). Diff is exactly **two** sign changes (`-DI*XI → +DI*XI`; `+DI*XR → -DI*XR`). Critic count confirmed; the report's own line 84 already said "two cross-terms", so the fix resolves the in-sentence self-contradiction.
  - **Action**: corrected "three sign flips" → "two sign flips" at the three critic-flagged sites (CYCLE.md §Semantics line 84, §Variant-axes line 152, §Supporting-evidence line 200) PLUS one additional same-error occurrence the critic did not enumerate (§Lowers-to line 173, "conjugate three-sign-flip variant" → "two-sign-flip"), so the count is now uniformly correct and internally consistent across the whole report. The algebraic claim `ā ⊙ b` and the source ranges (`operator.cpp:564-565`) were already correct and are untouched.

- **Finding 2 (citation-validity low): uncited real-`MultTranspose`-aliases-`Mult` claim.**
  - **Decision**: repaired.
  - **Verification (on-disk)**: located the alias via codemap search; `reference/palace/palace/linalg/operator.hpp:279` in the `BaseDiagonalOperator<OperType>` class body reads `void MultTranspose(const VecType &x, VecType &y) const override { Mult(x, y); }` — a direct, in-bounds witness that the real diagonal operator's transpose aliases `Mult`. `citecheck --scan` reports it `[ok]`.
  - **Action**: added the pinpoint citation to CYCLE.md §Variant-axes line 152 (`reference/palace/palace/linalg/operator.hpp:279`, with the alias line quoted inline), bringing the non-axis disambiguation claim up to the same evidentiary standard as the sibling variant claims. Did not invent — the alias is a verbatim on-disk line.

### Post-repair checks

- **Fence parity** (`proposed-changes-fence-encloses-full-body-guard`): `grep -c '```'` = 6 fences = 3 balanced blocks (`new:` + `edit:SUMMARY` + `edit:index`); firm body still fully enclosed. Intact.
- **citecheck** (`tools/citecheck/citecheck.py --scan`): 17 ok, 0 failing (was 16 ok before — the one added `operator.hpp:279` citation is `[ok]`; all pre-existing citations still pass).

### Unrepairable findings

None. Both findings were mechanical/surgical and supported by trivially-locatable on-disk source.

## Suggested resolution

`ready`. Both warning/low findings repaired against on-disk source of truth; the load-bearing count fix (two sign flips, matching the `operator.cpp:504-505` vs `:564-565` diff) is applied at all four occurrences and the previously-self-contradicting sentence is now consistent. No substantive authoring was required. Integrator may apply the report as-is.
