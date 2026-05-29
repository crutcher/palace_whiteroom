---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T084605Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-29T090000Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of `deflate` L2 firm (partly-constructive) harvest

## Critique

### Checks run

**citation-validity — pass.** Every claim carries a pointer and the pointers resolve line-exact.
I `read_range`-verified the full positive Schur-pipeline against `palace/linalg/nleps.cpp`:
`deflated_solve` lambda opens `:505` / closes `:537`; block-elimination comment with
`SS = (B - A T^-1 U) = - X^* X S^-1` on `:512` and `x1 = x1 - X S x2` on `:513`; `if (k == 0)
{ return; }` at `:516-518`; the coordinate loop `x2(j) = b2(j) - linalg::Dot(GetComm(), x1,
X[j])` at `:522`; `Eigen::MatrixXcd SS(k, k)` at `:524` with the Gram double-loop entry
`SS(i, j) = linalg::Dot(GetComm(), X[i], X[j])` at `:529`; `S = eig_opInv * Identity - H` at
`:532`; the three solves `SS = -S.fullPivLu().solve(SS)` (`:533`), `x2 = SS.fullPivLu().solve(x2)`
(`:534`), `MatVecMult(X, S.fullPivLu().solve(x2))` (`:535`); `linalg::AXPY(-1.0, XSx2, x1)`
(`:536`). `MatVecMult` body verified at `:329-347`. The residual-reuse (`:562-563`) and
Jacobian (`:664-667`) consumer sites verify exactly as cited, as does the basis-growth
`:606-619` (`scale=Norml2` `:610`, `X.resize` `:614`, `X[k]=v` `:615`, `k++` `:619`) and the
literature anchor `:354-362` (Jarlebring `:354`, Effenberger `:357`, SLEPc-NEP minimality
index 1). The two **negative anchors** verify by independent `search_text`: every `fullPivLu`
in `palace/linalg/*.cpp` is inside `nleps.cpp` and Schur-wrapped (no bare-Gram `(XᴴX)⁻¹`
solve), and `search_text` for `deflat` over `test/unit/**` returns zero hits (the
test-coverage caveat). Cross-artifact citations also verify line-exact: `dot.md:43`
(arg-1-conjugated convention), `lu_solve.md:3/56/58/63/64` (small-dense / RHS-linearity /
multi-RHS / kernel-conditioning non-law / A-nonlinearity non-law),
`nleps_deflated_residual.md:60` (non-orthonormal basis) and `:109` (the other-direction
over-unification guard), `orthogonalize.md:74/224/301` (orthonormal precondition / MGS
column-order / Householder scope-out). One minor imprecision noted under Issues (the
`index.md:26` do-NOT-merge precedent pointer).

**surface-or-evidence — pass.** This is a new firm-tier (partly-constructive) operator entry —
surface IS authored (the full `new:book/src/L2/deflate.md` chapter) AND it rests on positive
evidence. The firm/constructive SPLIT is correctly drawn and matches the CLAUDE.md
`partly-constructive` invariant exactly: (i) which sub-part is constructive — explicitly the
bare-Galerkin core `I − X(XᴴX)⁻¹Xᴴ` (`op.block = Galerkin`, `S = I` case) plus the
projector-specific laws 3–5; (ii) its negative-anchor citations — the deflation-scheme
literature (`:354-362`) plus the negative anchor that no bare-Gram solve appears outside the
Schur-wrapped block (independently re-confirmed above); (iii) the promotion condition — a
concrete positive Palace site exhibiting the bare Galerkin projector directly (future
linear-EVP deflation / preconditioner deflation / ROM Galerkin without the `S=λI−H` wrap),
with a stated fallback (scope to NLEPS-Schur-only ⇒ firm-on-positive-structure, a
same-layer-cross-cutter call). The firm part rests on the positive `deflated_solve` site
`:505-537`; the negative-anchor framing is correctly stated as evidence FOR a faithful
reconstruction, NOT as a positive claim. All three invariant requirements present and sound.

**rotation-quality — pass.** This is an L2 fusion-rotation: a hand-written fused L0 block (the
`deflated_solve` Gram double-loop + three `fullPivLu().solve` + `MatVecMult` + `AXPY`) is
de-fused into a named `coords ▷ schur-solve ▷ back-project` composition with first-class
constituents (`dot`, `gram`, `lu_solve`, `linear_combination`) and projector laws stated at
the composition level. This is strictly more abstract / more equational than the L0 fused
form — not a renaming or 1:1 mapping. The firm/constructive split is the rotation honestly
declared: the de-fusion of the *structure* (the pipeline) is firm; only the bare-Galerkin
*specialization* of the solve block is constructive. Pass.

**variant-axis-coverage — pass.** Three orthogonal axes are enumerated per the
`classify-variant-axis` output contract (absorption path / load-bearing primitive / state
binding): the central `op.block ∈ {Galerkin, Schur}` axis (correctly the partly-constructive
hinge), the `op.dot` hook ∈ {canonical, B-weighted} (parametric closure absorption, law-6
invariant), element type ∈ {real, complex} (absorbed by `dot`/`linear_combination`), and
in-place vs out-of-place (transparent-perf, scoped to L2>L1, matching `linear_combination`).
The empty-basis `k=0` branch is covered (law 1). No hidden branches — the `:515-518`
early-return, the `:562-563`/`:664-667` consumer reuses, and the outer deflation-growth loop
(`:606-619`) are all explicitly scoped (the last out to the NLEPS driver, not here).

**cross-reference-integrity — warning.** Build-readiness guard PASSES: this is a `new:` chapter
file, so the firm/partly-constructive apparatus (`## Status` line 407, Signature 98,
Algebraic-laws 216, Evidence 474) is entirely INSIDE the `new:` fence (opens line 44, closes
line 546) — no cycle-019 fence-truncation defect. Fence enumeration: 8 markers, even parity,
with two nested ` ```text ` blocks (100–111, 143–154) properly balanced inside the `new:`
block, and a separate `edit:` block (548–550). Live links resolve on disk: `lu_solve.md`,
`linear_combination.md`, `inner_product.md`, `dot.md`, `orthogonalize.md`,
`nleps_deflated_residual.md`, `ksp_solve.md` all EXIST. `gram` is correctly a plain-text
forward-reference with `<!--rough-in-->` (created in parallel wave-2; not yet on disk —
integrator upgrades to a live link). The warning is the **stale dependency-cell phrase** in
the completed `edit:` dep-map row (see Issues) — a cross-reference fidelity defect, not a
build break.

**edge-label-fidelity — pass.** Not a lowering theme; no L_{n+1}→L_n edge label is carried.
The L2 vs L1 / L2 vs L0 distinction sections (462-472) and the forthcoming-L2>L1-theme
forward-reference (364-368) discuss the correct adjacent edges. Pass (the report's directional
prose is consistent — the L2 named composition de-fuses the L0 block, narrated in the correct
direction).

**plan-kind-consistency — pass.** Declared kind is firm-tier `partly-constructive`, and the
content shape matches: full Signature + Semantics + six numbered Algebraic-laws + explicit
non-laws + Variant-axes + a Status section that draws the firm/constructive line. No rough-in
placeholders in the firm/constructive prose. The one rough-in element (`gram`) is correctly
marked plain-text `<!--rough-in-->`, consistent with its not-yet-on-disk state. The
`partly-constructive` classification is correct (not over-claimed `firm`, not under-claimed
`rough-in`) per the central question.

**skill-uptake-survey — pass.** The report references `classify-variant-axis` (line 372, with
the per-axis output contract followed) and `verify-citation-range` is implied by the
"`read_range`-verified and `citecheck.py`-anchor-checked" Evidence-section note (line 476).
The `propose-rotation` / `verify-rotation-citation` skills are implicitly satisfied by the
fusion-rotation framing. Surfaces telemetry only; non-blocking.

### Issues found

1. **Stale dependency-cell phrase in completed `edit:` dep-map row** —
   `reports/.../CYCLE.md` line 549 (the `edit:book/src/L2/index.md` block) / will land at
   `book/src/L2/index.md:55`. The dependency cell still reads: "`lu_solve` (the small-dense
   `k×k` Gram solve — **NOT yet vocabulary; candidate L1 leaf, OQ below**)". This is stale:
   `lu_solve` is FIRM on disk (`book/src/L1/lu_solve.md` EXISTS, landed cycle-022 wave-1) and
   the chapter body itself links it as `[lu_solve](../L1/lu_solve.md)` (firm). The cell should
   be refreshed to a live link `[lu_solve](../L1/lu_solve.md)` (L1, firm cycle-022) with the
   "NOT yet vocabulary / candidate L1 leaf / OQ below" clause dropped. Severity: medium
   (cross-reference fidelity / staleness; not a build break since `lu_solve` is referenced in
   prose-name form in the row cell, but it asserts a false maturity state). Repairer/integrator
   candidate — surgical cell edit. (This is the transparency-noted item from the dispatch
   framing; confirmed present.)

2. **Completed `edit:` status-cell faithfulness — VERIFIED FAITHFUL (no defect), recorded for
   the integrator.** The orchestrator-completed row (line 549) status cell reads
   "`partly-constructive` (cycle-022; firm Schur-form pipeline on positive site
   `nleps.cpp:505-537`; constructive bare-Galerkin core `I − X(XᴴX)⁻¹Xᴴ` from literature +
   negative anchor; promotion on a positive Galerkin deflation site)". This is a faithful
   condensation of the chapter `## Status` (lines 407-460): same status value, same
   firm/constructive split, same positive site, same promotion condition. The row name is a
   live link `[deflate](./deflate.md)` matching the new chapter slug. No fidelity defect in the
   status cell. (Recorded as a non-issue to discharge the dispatch's verification ask.)

3. **Minor citation imprecision — `index.md:26` do-NOT-merge precedent pointer** — CYCLE.md
   line 318 cites the `inner_product`/`linear_combination` do-NOT-merge boundary precedent as
   `book/src/L2/index.md:26`. Line 26 is the prose sentence "They share the fold skeleton but
   target different codomains... the do-NOT-merge note... is load-bearing" — it IS the
   do-NOT-merge statement, so the pointer is in-range and supports the claim, but the boundary
   conceptually spans the §"Fold cohorts" block (lines 22-26). Pointer is supportive, not
   wrong. Severity: low (citation-precision polish, optional). Repairer may widen to
   `book/src/L2/index.md:22-26` or leave as-is.

4. **Over-unification guard — VERIFIED PRESENT and load-bearing (no defect), recorded.** The
   chapter states the `deflate` vs `orthogonalize` distinction as a first-class § (lines
   293-321) with a three-axis comparison table, names `orthogonalize = deflate|_{gram=I}` as an
   over-unification to AVOID, and identifies the decisive distinguisher as the Gram-matrix
   `lu_solve` carrying the `(XᴴX)⁻¹` oblique correction (which Gram-Schmidt does not). The
   non-law "orthogonality of the projector (`deflate ≠ I − XXᴴ`)" (lines 275-279) reinforces it,
   and the guard is mirrored from the other direction at `nleps_deflated_residual.md:109`
   (verified). The guard is present, correct, and cross-referenced. (Recorded as a non-issue to
   discharge the dispatch's load-bearing over-unification-guard ask.)

5. **`gram` forward-reference correctly plain-text, but tracked for integrator wiring** — the
   chapter and dep-map both carry `gram` as `<!--rough-in-->` plain-text (chapter lines 55, 81,
   304, 327; dep-map row at index.md:54 remains rough-in). `book/src/L2/gram.md` does NOT exist
   yet (parallel wave-2 dispatch). This is CORRECT per the rough-in-forward-reference-must-be-
   plain-text convention — flagged not as a defect but so the integrator wires the live link
   once `gram.md` lands (the report explicitly defers this, lines 330, 367). Severity: info
   (no action needed at critique; integrator-time wiring). Not a build risk as-authored.

## Repair

### Fixes attempted

- **Finding 1 (medium — the real fix): Stale dependency-cell phrase in completed `edit:`
  dep-map row.**
  - **Decision**: repaired.
  - **Action**: Edited `reports/.../CYCLE.md` line 549 (the `edit:book/src/L2/index.md` deflate
    row, which lands at `book/src/L2/index.md:55`). Replaced the stale dependency-cell phrase
    "``lu_solve`` (the small-dense `k×k` Gram solve — **NOT yet vocabulary; candidate L1 leaf,
    OQ below**)" with the live-link form "``[lu_solve](../L1/lu_solve.md)`` (L1, firm
    cycle-022 — the small-dense `k×k` Gram solve)". `book/src/L1/lu_solve.md` verified to EXIST
    on disk (landed cycle-022 wave-1, 23783 bytes), so the live link is safe (no dead link
    introduced). The false-maturity assertion ("NOT yet vocabulary / candidate L1 leaf / OQ
    below") is dropped — it asserted a maturity state that is now incorrect. **Chapter-body
    check** (`new:book/src/L2/deflate.md`): grep'd the entire CYCLE.md for the stale framing
    ("NOT yet vocabulary", "candidate L1 leaf", "OQ below") — **zero residual hits**; the
    chapter body already carried `lu_solve` exclusively as live links `[lu_solve](../L1/lu_solve.md)`
    (lines 56, 79, 331, 380) and as correct plain-text citation anchors
    (`book/src/L1/lu_solve.md:56/58/63/64`, lines 234/269/282/497/527). The staleness was
    confined to the single dep-map row cell. No chapter-body edit needed beyond the row fix.
    `gram` correctly left plain-text `<!--rough-in-->` (gram.md not on disk; integrator upgrades
    at integration) — no dead link introduced.

- **Finding 2 (verified faithful — orchestrator-completed status cell + live-link name): no
  defect.**
  - **Decision**: not-needed. The critic already verified the status cell as a faithful
    condensation of the chapter `## Status`, and the row name is a correct live link
    `[deflate](./deflate.md)`. No repair action.

- **Finding 3 (low — `index.md:26` do-NOT-merge precedent citation precision): optional widen.**
  - **Decision**: repaired (optional fix applied).
  - **Action**: Edited `reports/.../CYCLE.md` line 318 — widened the do-NOT-merge precedent
    citation from `book/src/L2/index.md:26` to `book/src/L2/index.md:22-26`. Verified against
    `book/src/L2/index.md`: the §"Fold cohorts" block spans lines 22-26 (line 22 the cohort
    header, lines 23-24 the two folds, line 26 the do-NOT-merge sentence). Line 26 was in-range
    and supportive on its own; the widened range now captures the whole conceptual boundary
    block. Citation-precision polish; the original pointer was not wrong.

- **Finding 4 (info — `gram` forward-ref correctly plain-text): no action.**
  - **Decision**: not-needed. `gram` is correctly a plain-text `<!--rough-in-->`
    forward-reference (gram.md lands same wave-2 cycle; integrator wires the live link at
    integration). Confirmed left untouched in both the row fix and the chapter body — no dead
    link risk.

### Unrepairable findings

None. Both actionable findings (1, 3) were clean mechanical/surgical edits within repair
authority: a stale-maturity dependency-cell refresh with a verified-existing live-link target
(finding 1) and an optional citation-range widen verified against the cited file (finding 3).
No substantive authoring, no contradiction with artifact content, no methodology-level concern.

The `partly-constructive` judgment is SOUND and was not touched: the firm/constructive split is
correctly drawn, the three-part `partly-constructive` invariant (which sub-part is constructive,
its negative-anchor citations, the explicit promotion condition) is satisfied, and the
over-unification guard against `orthogonalize` is present and load-bearing. The critic's
`checks:` values are not overridden.

## Suggested resolution

`ready`. The lone cross-reference-integrity warning was a clean mechanical staleness refresh
(`lu_solve` is firm on disk; the dep-map row was the only stale site), now repaired. The
optional citation widen (finding 3) is also applied. All other checks pass and the
`partly-constructive` judgment is sound.

Integrator notes:
- The `edit:book/src/L2/index.md` deflate row now carries a live link `[lu_solve](../L1/lu_solve.md)`
  in its dependency cell — safe (lu_solve.md exists on disk). No further refresh needed there.
- `gram` remains a plain-text `<!--rough-in-->` forward-reference in both the chapter body and
  the dep-map (gram.md lands same wave-2 cycle). Wire the `gram` live links
  (`[gram](./gram.md)`) at integration once `book/src/L2/gram.md` is on disk — the report
  explicitly defers this (CYCLE.md lines 330, 367; META finding 5).
- Fence parity verified EVEN after edits (8 markers: `new:` 44→546 with nested `text` blocks
  100→111 / 143→154, `edit:` 548→550) — no fence touched by the two single-line text edits.
