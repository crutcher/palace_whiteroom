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
---

# META: verification of "Formalize jacobi-smoother at L2" (cycle-042 D5, L2 floor)

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan --quiet` reports 29/29 OK (bounds + path-hygiene clean; every citation carries the full `palace/linalg/...` path, no `AMBIG`, all ranges in-bounds). I `--anchor`-checked all load-bearing pinpoints and read `jacobi.cpp:41-107` directly. All resolve: real apply `Y[i] = DI[i] * X[i]` at `:38` (`ok`); `SetOperator` at `:75` inside `:74-97` (`ok`); `AssembleDiagonal` `:79`, `Reciprocal` `:80`, `dinv *= omega` `:92`, `MFEM_ASSERT(!initial_guess)` `:102`, `Apply(dinv, x, y)` `:103`, instantiations `:106-107`, `MultTranspose` `jacobi.hpp:43`, `JACOBI` `ksp.cpp:198`, `JacobiSmoother` `errorestimator.cpp:76` — all `ok`. The dead-code branch claim was the one I adjudicated mechanically rather than hand-asserting: a bare `--anchor 'Transpose'` returned `[DRIFT]` (matched the template-parameter token at `:52`), but the report does NOT claim the *word* "Transpose" sits in `:61-69` — it claims the conjugate-`dinv` kernel BODY is there. `--anchor 'YR[i]'` lands at `:66` within `:61-69` (`ok`), and the direct read confirms the `else` branch at `:61-69` computes `YR[i] = DIR[i]·XR[i] + DII[i]·XI[i]; YI[i] = -DII[i]·XR[i] + DIR[i]·XI[i]` — exactly the conjugate-`dinv`/transpose form the report's §Supporting-evidence quotes. So the DRIFT was a probe artifact, not a report defect (the cycle-024 `--anchor`-settles-it discipline applied). No `verified_against:` block in this report, so that sub-check no-ops. (Two `NOANC`/`DRIFT` lines in my probe log were my own shell-escaping artifacts on `Y\[i\]` and the bare-`Transpose` token; both cleared on clean literals.)

**surface-or-evidence — pass.** Not a refinement of an existing entry — this is a NEW L2 floor file (`book/src/L2/jacobi-smoother.md` does not exist on disk). The proposal authors fresh surface (full chapter body inside the fence) plus the L2-index dep-map row and the SUMMARY entry. The identity-in-form framing is explicitly the "negative fusion observation" carried as the fusion-rotation content, with positive-source evidence; this is not a bare rotation_claim without surface.

**rotation-quality — pass.** The asserted rotation is L2↔L1 identity-in-form, and the report is candid that the fusion rotation is a *no-op* (degree-zero fixed point of the fusion that produces `chebyshev-iteration`'s recurrence). This is the legitimate "identity-lowerings still require both L levels" case, not a disguised renaming pretending to be a compaction — the report does not over-claim a non-existent abstraction gain. The genuine fusion-rotation *content* is the negative observation (one elementwise product, no fused multi-operation kernel to unfold), which is sourced (`:30-39` real, `:41-70` complex four-multiply = single elementwise complex product, NOT a fused composition) and contrasted against the chebyshev sibling's real de-fusion. Pass.

**variant-axis-coverage — pass.** Two orthogonal axes (element-type real|complex; damping-mode default|fixed|estimated) + one absorbed axis (operator-representation), each enumerated in frontmatter `variant_axes:` and §Variant-axes, all stated as absorbed into the constructed-operator closure. The element-type axis is source-witnessed at both kernels (`:30-39` real, `:41-70` complex) and the instantiations `:106-107`; damping-mode at the three setup branches (`:84-89` estimated, `:90-93` fixed-vs-default skip). `sf_max` is correctly called out as a construction parameter, NOT a variant axis. No hidden branches: the `Transpose` template axis on `Apply` is explicitly accounted for (the `=true` branch is dead code, never instantiated — I confirmed zero `Apply<true>` consumers across `reference/palace/palace/`).

**cross-reference-integrity — pass.** Every `[link]` target exists on disk: L2 siblings (`scal`, `chebyshev-iteration`, `ksp_solve`, `eigsolve`, `linear_combination`, `inner_product`, `index`), L1/L3 `jacobi-smoother`, `L1/assemble-diagonal`, both L1-L0 themes (`reciprocal-elementwise-product-mutation-rotation`, `jacobi-smoother-mutation-rotation`), both concepts (`constructed-operators`, `variant-absorption`). The two forward-references that do NOT resolve — the L2 `elementwise_product`/`reciprocal` floors and the L2>L1 `jacobi-smoother-apply-identity` (D8) theme — are correctly kept PLAIN-TEXT, not live links, per `rough-in-forward-reference-must-be-plain-text-not-live-link`; this is the right handling, not a broken link. Build-readiness fence guard: the `edit:book/src/L2/jacobi-smoother.md` block ENCLOSES the full firm apparatus inside the fence — `## Status`, Signature, Algebraic-laws, Evidence are all between the opening fence at line 44 and the close at 635 (verified by fence enumeration: opens 44/637/641, closes 635/639/643 — three balanced blocks, even parity, no nested ``` fences, inner code as 4-space-indented per the convert-nested-fences discipline). The `## Operator content` / `## Supporting evidence` sections are the report's own metadata OUTSIDE the fence and correctly do not duplicate the body — so this is NOT the cycle-019 firm-body-outside-fence defect.

**edge-label-fidelity — pass.** The entry carries L2↔L1 (lowers_to) and L3↔L2 (lifts_from) edges. The §Lowers-to prose discusses exactly L2→L1 (identity-in-form, the elementwise-product-down narrative to L1>L0); §Lifts-from discusses exactly L3→L2 (the firm L3 cycle-037 entry resting on this floor). No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared `firm` (frontmatter `firmness: firm`, §Status, dep-map row). The content shape matches firm: complete signature, six algebraic laws each with a positive-source witness, four explicit non-laws, full variant profile, no rough-in placeholders, no `TODO`/`pending` body holes. The firm-on-positive-structure justification is sound and correctly applied: every law is a syntactic identity readable off the small fully-present `Apply`/`SetOperator`/`Mult` surface (not a literature-inferred convergence claim), so the absent dedicated `test-jacobi.cpp` does not gate firm — this is the `apply_linop`/`scal` precedent, not the `eigsolve`-convergence-semantics situation. The three "Caveats (not status reductions)" — dead-code transpose branch, `ω=0` opaque `spectrum_estimate`, no L2 elementwise floor yet — are correctly framed as non-status-reducing (each is a non-law or below-resolution note, not an unconfirmed claim). The `Apply<Transpose=true>` dead-code branch is a recognition-rule caveat / non-law, NOT a downgrade — consistent with the dispatch directive (focus point 4) and confirmed dead by the zero-consumer grep.

**skill-uptake-survey — pass (telemetry).** The report references `tools/citecheck/citecheck.py --anchor` / `--scan` self-verification (§Evidence, §Supporting-evidence), the `convert-nested-fences-to-indented-code-in-proposed-changes-block` discipline (§Operator-content), and the count-ownership partition deferring the L2-index tally to D11 (§Open-questions item 4). Appropriate skills for an L2-floor harvest are surfaced; nothing missing.

### Issues found

No blocking or warning-level issues. Minor / informational only:

1. **SUMMARY.md insertion block carries no anchoring context** (`CYCLE.md` §Proposed-changes, the `edit:book/src/SUMMARY.md` block, lines 641-643). The block is the bare bullet `- [jacobi-smoother](./L2/jacobi-smoother.md)` with no surrounding line to pin WHERE in the L2 section (line 48+) it inserts. This is an integrator-placement concern (resolved via `summary-md-surgical-insert`), not a content defect — the target line is well-formed and the L2 section is unambiguous — but flagging it as the kind of under-anchored single-line SUMMARY edit the integrator should place deliberately. Severity: informational.

2. **§Semantics phrasing "conjugate-`dinv` Hermitian kernel"** (`CYCLE.md` §Semantics, line ~235, and §Caveats line ~479). The `Apply<Transpose=true>` branch at `:61-69` computes the *transpose* (negated off-diagonal: `YR = DIR·XR + DII·XI`, `YI = -DII·XR + DIR·XI`), which the report elsewhere correctly calls "the *transpose* (not conjugate-transpose)". The "Hermitian kernel" / "conjugate-`dinv`" labels for this same branch are internally consistent with the report's framing (transpose-of-`dinv` = conjugate-`dinv` apply for a diagonal) but a reader skimming could conflate "Hermitian" (conjugate-transpose) with the transpose-only kernel the source realizes. The report's non-law section already disambiguates this precisely, so it is not an error — noting only that the §Semantics one-liner leans on the §Algebraic-laws non-law for full disambiguation. Severity: informational (no fix required; the precise statement is present).

3. **Forward-reference dependency on missing L2 `elementwise_product`/`reciprocal` floors** (§Dependencies, §Open-questions item 1) is correctly self-flagged as a genuine cohort gap, NOT a defect of this entry, and per the dispatch note those co-land this cycle (D2/D3) — so not a real gap. Confirmed the forward-references are plain-text (not live links). No action. Severity: none (cleared).

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
repaired_at: 2026-06-01T073000Z
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

## Repair

### Fixes attempted

All 8 critic checks returned `pass` with no blocking or warning-level issues. The three "Issues found" entries are explicitly informational-no-defect; none names a repairable surface/citation/cross-reference/edge defect. No mechanical edit applies to any of them.

- **Finding 1**: SUMMARY.md insertion block carries no anchoring context (bare bullet `- [jacobi-smoother](./L2/jacobi-smoother.md)`, no surrounding pin line).
  - **Decision**: not-needed.
  - **Rationale**: This is the normal under-anchored single-line SUMMARY edit the critic flags for deliberate integrator placement via `summary-md-surgical-insert` — the target bullet is well-formed and the L2 section is unambiguous. It is not a content defect, and adding anchoring context to the proposed-changes block would be authoring placement intent that belongs to the integrator, not a mechanical repair. No edit.

- **Finding 2**: §Semantics one-liner phrasing "conjugate-`dinv` Hermitian kernel" for the `Apply<Transpose=true>` (transpose-only) branch.
  - **Decision**: not-needed.
  - **Rationale**: The critic confirmed the phrasing is internally consistent (transpose-of-`dinv` = conjugate-`dinv` apply for a diagonal) and that the report's §Algebraic-laws non-law section already disambiguates "transpose (not conjugate-transpose)" precisely. The precise statement is present; the critic explicitly tagged this "no fix required." Rewording a candid, internally-consistent semantics one-liner would be a content/clarity judgment, not a mechanical fix — out of repair authority. No edit.

- **Finding 3**: Forward-reference on missing L2 `elementwise_product`/`reciprocal` floors.
  - **Decision**: not-needed.
  - **Rationale**: Self-flagged cohort gap, NOT an entry defect; the floors co-land this cycle (D2/D3, cleared per dispatch note) and the forward-references are correctly plain-text (not live links) per `rough-in-forward-reference-must-be-plain-text-not-live-link`. Critic marked severity none (cleared). No edit.

### Unrepairable findings

None. No finding requires substantive authoring or contradicts artifact content; every finding is informational-no-defect.

### Follow-up noted (out of this report's repair scope — not a defect in this report)

Per the dispatch note (elementwise_product precedent): firm `book/src/L3/jacobi-smoother.md` asserts "no interposed L2 entry" — confirmed live at **line 31** ("with no interposed L2 entry and no `L3-L2/jacobi-smoother-identity` theme") and **line 141** ("**no interposed L2 entry, no L3-L2 theme, no non-adjacent L3-L1 directory**"). Once this L2 floor (`book/src/L2/jacobi-smoother.md`) lands, those two assertions become stale (an L2 entry now exists; the L3>L1 identity-in-form annotation should re-anchor to acknowledge the interposed L2 floor while preserving the non-adjacent-identity convention — there is still no `L3-L2/` theme file, but "no interposed L2 entry" is no longer true). This is a **lifter** touch on the L3 entry, NOT in this report's repair scope (repairer does not modify `book/` directly; substantive re-anchoring of L3 prose is authoring). The D8 themes already flag stale L3 §Lowers-to; this L3-entry-prose staleness is the same class. No fix needed in this report.

## Suggested resolution

`ready`. Integrator notes:

1. Place the SUMMARY.md `- [jacobi-smoother](./L2/jacobi-smoother.md)` bullet deliberately within the L2 section (the under-anchored single-line edit per Finding 1; `summary-md-surgical-insert`).
2. Verify the D2/D3 L2 `elementwise_product`/`reciprocal` floors co-land this cycle so this entry's plain-text forward-references can later upgrade to live links (Finding 3 — not blocking; the plain-text handling is correct as-is if they slip).
3. Stale-assertion follow-up: `book/src/L3/jacobi-smoother.md` lines 31 / 141 assert "no interposed L2 entry" — now superseded by this L2 floor. Route a **lifter** touch to re-anchor that prose (preserving the cycle-012 non-adjacent-identity convention; only the "no interposed L2 entry" clause is stale). Out of this report's repair scope.
