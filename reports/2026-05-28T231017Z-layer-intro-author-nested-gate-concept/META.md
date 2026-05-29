---
verifies: ../CYCLE.md
critiqued_at: 2026-05-28T233000Z
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
repaired_at: 2026-05-28T234500Z
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

# META: verification of CYCLE concepts/nested-constructed-operator-gate

## Critique

### Checks run

**citation-validity — pass.** All eleven cited pointers were resolved against live artifact files and found in-range. Spot-checked every focus citation: `book/src/L1/eigsolve.md:60` (line 60 binds `linear : Solver[A]` and `projector : Maybe DivFreeSolver[ComplexVector]` — two nested gates — VERIFIED); `:136` ("making `eigsolve` the first L1 operator to compose two layers of constructed-operator absorption" — VERIFIED, the source phrases it without the report's bold markup but the substance is exact); `:140` ("composed-not-inherited" appears verbatim at end of line 140 — VERIFIED); `book/src/L1-L0/eigsolve-mutation-rotation.md:213-258` (line 213 = "### Sub-pattern B — inner-solve mutation-rotation", line 215 = "the **core sub-pattern**", ten `opInv->Mult` call sites each rewriting by the firm `ksp-solve-mutation-rotation` theme — VERIFIED); `book/src/L1/divfree-projector-mutation-rotation.md:108-113` (the opaque `K⁻¹` action + the "first L1>L0 mutation-rotation whose closure carries another constructed-operator gate" claim — VERIFIED, and this confirms the prong-b inaccuracy the report flags); `:193-198` (`P.ksp` ← CG solver bound to `P.M`, "The inner constructed-operator gate" — VERIFIED); `book/src/L1/ksp_solve.md:31` (`K` "additionally binds an optional preconditioner `M⁻¹` (also a `LinearOperator[N, N]`)" — VERIFIED, latent-site basis is sound); `book/src/L1/chebyshev-smoother.md:58` (`op.A : LinearOperator[N, N]` — RAW operator negative case — VERIFIED); `chebyshev-smoother.md:140` (the "used as the `B` preconditioner inside an outer Krylov method" weaker-nesting passage — VERIFIED). The sibling-format anchors `constructed-operator-factory.md:1-42` and `solver-as-operator.md:1-12` resolve and match the claimed format (no frontmatter, `# <slug>` title, `## Background`, relative `./<slug>.md` links). No from-memory or out-of-range citations found.

**surface-or-evidence — pass.** This is a new concept-page authorship (net-new file) plus a SUMMARY registration, not a refinement of an existing operator/theme. It does not modify the surface of any existing operator or theme — it forwards citations into the L1 entries and themes without restating their algebraic laws. No rotation_claim is asserted against an existing surface, so the surface-or-evidence gate's refinement branch does not apply; the new-content branch (page is fully cited, no surface mutation of existing entries) is satisfied. Note that the report explicitly defers the only surface-correction work (prong b — the divfree theme's inaccurate "first" claims at `:108-113`, `:457-464`, OQ `:2897`) to a separate cycle-018 lifter/harvester dispatch, correctly keeping it out of this report's authority.

**rotation-quality — pass (not a rotation proposal).** The report does not assert an algebraic/structural/reduction rotation between two layers; it documents a cross-cutting structural pattern (gate-carrying-gate) and a lowering-fidelity discipline that already holds across two firm L1 operators. The "cross-layer fidelity rule" is a documentation convention (inner gate's iteration stays interior to its own theme; lowering of the whole = composition of adjacent-edge themes, never a flattened rewrite) — it asserts that the existing adjacent-edge themes already compose correctly, not that a new compaction is being introduced. This is consistent with the cycle-012 `l3-l1-inline-identity-rotation-convention` posture (composition of adjacent-edge themes, annotated, not a new directory). Inapplicable in the rotation-compaction sense; marked pass.

**variant-axis-coverage — pass.** The pattern's own variant axis is "how deep does the nesting go," and the page covers each realized combination explicitly: one-gate (`divfree-projector`, `P.ksp`), two-gate (`eigsolve`, `E.linear` + `E.projector`), and the three-deep transitive composition (`eigsolve ⊃ divfree-projector ⊃ ksp_solve`). The negative case (raw-operator field → not nesting: `chebyshev-smoother`'s `op.A`, `apply_linop`'s operand) is explicitly carved out as the distinguishing test. The one un-covered combination — preconditioner-as-`Solver` inside `ksp_solve` — is explicitly scoped out as a LATENT site with a stated promotion condition (confirm a concrete Palace L0 site where a `BaseKspSolver`'s preconditioner is itself a `BaseKspSolver`), not hidden. No hidden branches.

**cross-reference-integrity — pass.** Every intra-`concepts/` link in the new page resolves: `constructed-operators.md`, `constructed-operator-factory.md`, `solver-as-operator.md`, `variant-absorption.md`, `ksp_solve.md` all present. The cross-Part references (`book/src/L1-L0/eigsolve-mutation-rotation.md`, `book/src/L1-L0/divfree-projector-mutation-rotation.md`, `book/src/L1/divfree-projector.md`) all exist; `divfree-projector.md` confirmed present in `book/src/L1/`. The See-also section anchors into divfree `§"Sub-pattern A"` and `§"Sub-pattern C"` resolve (Sub-pattern A at line 52, Sub-pattern C at line 171). The SUMMARY insertion point matches live text exactly: line 151 `- [scalar-promotion](./concepts/scalar-promotion.md)` followed by blank line and `# Design Artifacts` (line 153) — the proposed `[old]` block is verbatim and the new entry threads in cleanly as the final concepts row.

**edge-label-fidelity — pass.** The report carries no single L_{n+1}→L_n edge label; it is a concepts-Part page that spans the L1 and L1>L0 surfaces by reference. The cross-layer fidelity rule it states ("the inner gate's iteration stays interior to its own lowering theme; the lowering of the whole is the composition of the two adjacent-edge themes") is itself an edge-discipline claim, and the prose discusses exactly the edges it names — the `divfree-projector` L1>L0 theme's `ksp->Mult` opaque action delegating to the `ksp_solve` theme, and the `eigsolve` L1>L0 theme's ten `opInv->Mult` sites delegating to the same. The edge prose matches the cited edges; no L3→L4-says-but-discusses-L2→L3 mismatch.

**plan-kind-consistency — pass.** Declared shape is a documentation/fidelity concept page (cross-cutting concept authorship), and the content is exactly that: a named structural shape, a discipline rule, two firm instances with citations, one explicitly-latent site, and sibling relationships. The report correctly classifies the `eigsolve` instance as a clean FIRM instance of the nesting shape (the `LinearSolveFailed` partly-constructive caveat is a separate status concern on a discarded convergence value, NOT on the gate-nesting structure — the report states this distinction explicitly and it checks out against the sub-pattern-B text). It correctly classifies the `ksp_solve` preconditioner as LATENT (not firm) with a stated promotion condition, and explicitly flags the concept-vs-combinator boundary (documentation now, re-route to combinator-miner only if calculus-level support is later needed). No firm-claimed-but-rough-in placeholders; classifications are internally consistent.

**skill-uptake-survey — warning.** The report's shape — authoring a concept page whose entire load is eleven cross-artifact citations self-verified via `Read`, plus a variant-axis carve-out (raw-operator-field vs gate-field, latent-site classification) — implies two relevant skills exist (`verify-citation-range` for the citation-resolution pass; `classify-variant-axis` for the nesting-depth/latent-site classification) yet the report references neither by name. The Supporting-evidence section states citations were "self-verified via `Read` against the cited artifact lines (no from-memory citations)" — the work was clearly done, but the skill invocation is not surfaced in telemetry. Pure presence check; non-blocking. Surfaced so the meta-phase can see whether layer-intro-author concept-page dispatches are routinely skipping the `verify-citation-range` self-emit reference.

### Issues found

1. **Supporting-evidence over-attribution: eigsolve theme header "firm-structure framing".** CYCLE.md Supporting evidence (the `eigsolve-mutation-rotation.md:213-258` bullet) states "Theme header (`:1-16`) confirms firm-structure framing." The header at `:1-16` confirms the *structured-opaque-primary-argument* framing and lists the two nested sub-fields (`E.linear`, `opProj`), which supports the nesting claim — but the literal word "firm" does not appear in `:1-16`; the "firm" attribution lives at the sub-pattern justification level (`eigsolve-mutation-rotation.md:251`, "rewrites by the firm `ksp-solve-mutation-rotation` theme"). Location: CYCLE.md §"Supporting evidence", the eigsolve sub-pattern-B bullet. Severity: minor / cosmetic. The page-content claim is sound (the nesting sub-pattern B is firm and source-anchored); only the citation-line attribution in the evidence ledger is slightly loose. Candidate for a one-line attribution tightening (point at `:251` for the "firm" word, keep `:1-16` for the structured-argument framing).

2. **`eigsolve.md:136` quoted with added bold emphasis.** CYCLE.md §"Supporting evidence" and the page body (line 116) render the line-136 quote as "**first L1 operator to compose two layers of constructed-operator absorption**" with bold markup; the source at `:136` carries the phrase without bold. Location: CYCLE.md §"Firm instances" (page body line 116) + §"Supporting evidence" (line 212-213). Severity: trivial. The substance is verbatim-correct; only the emphasis markup is the report's own. Not a fidelity problem (added emphasis on a quoted phrase), noted for completeness.

3. **Skill-invocation telemetry absent (see skill-uptake-survey).** Neither `verify-citation-range` nor `classify-variant-axis` is referenced by name despite the report's shape implying both. Location: CYCLE.md §"Supporting evidence" + §"Open questions / caveats" (the latent-site classification). Severity: informational/telemetry only.

No citation-validity, cross-reference, edge-label, surface, or plan-kind defects were found. Phase-boundary is clean: `git status` shows only `reports/` directories untracked; `book/src/concepts/nested-constructed-operator-gate.md` does not exist on disk, confirming no dispatch-phase `book/` write leaked. The two surface-correction follow-ups (prong b on the divfree theme; latent-site harvester confirmation) are correctly surfaced as out-of-authority routing in §"Open questions / caveats" rather than enacted here.

## Repair

### Fixes attempted

- **Finding 1**: Supporting-evidence over-attribution — the eigsolve sub-pattern-B bullet claims theme header `:1-16` "confirms firm-structure framing," but the literal word "firm" is at `eigsolve-mutation-rotation.md:251`, not `:1-16`.
  - **Decision**: repaired
  - **Action**: CYCLE.md §"Supporting evidence", eigsolve sub-pattern-B bullet. Re-pointed the "firm" attribution to `:251` ("rewrites by the firm `ksp-solve-mutation-rotation` theme") and kept `:1-16` scoped to the structured-opaque-primary-argument framing + the two-nested-sub-field listing. Verified against source first: `eigsolve-mutation-rotation.md:251` reads "Each `opInv->Mult(b, x)` rewrites by the firm `ksp-solve-mutation-rotation` theme" (the only "firm" occurrence in the cited neighborhood); `:1-16` (theme header) reads "second L1>L0 mutation-rotation theme for a structured opaque primary argument" with no "firm" word. Surgical citation-offset correction — no page-content claim changed (the sub-pattern-B-is-firm substance was already sound).

- **Finding 2**: `eigsolve.md:136` quoted with added **bold** emphasis not present in source — rendered as "**first L1 operator to compose two layers of constructed-operator absorption**" in two spots.
  - **Decision**: repaired
  - **Action**: CYCLE.md §"Firm instances" page-body bullet (the `eigsolve` instance) + §"Supporting evidence" (the `:136` VERIFIED bullet). Removed the report-added bold on the "first L1 operator to compose two layers of constructed-operator absorption" phrase to match source verbatim. Verified against source first: `eigsolve.md:136` carries this phrase in plain text (the only legitimately-bold span on that line is the preceding "**This is the second L1 operator … constructed-operator type**" sentence, which is bold in source and was left intact in the supporting-evidence quote). Quote-fidelity fix only — substance was already verbatim-correct.

- **Finding 3**: Skill-invocation telemetry absent (`verify-citation-range` / `classify-variant-axis` not referenced by name). Tied to the `skill-uptake-survey: warning`.
  - **Decision**: not-needed
  - **Rationale**: Non-blocking, informational/telemetry only (the critic marked it as such). The work was demonstrably done (eleven citations self-verified via `Read`; variant-axis carve-out present); only the by-name skill reference is missing. Surfacing the absent telemetry is the critic's `warning`, which the repairer does not override; adding skill-invocation prose would be substantive narration of process rather than a mechanical fix, so it is left for the meta-phase trend view (whether layer-intro-author concept-page dispatches routinely skip the `verify-citation-range` self-emit reference).

### Unrepairable findings

None. The two surgical findings were repaired; the third is non-blocking telemetry left for meta-phase visibility.

## Suggested resolution

`ready`. Both citation/quote-fidelity findings are fixed in CYCLE.md; the proposed-changes block (concept-page create-content + SUMMARY registration) is unchanged in substance. Integrator notes:
- The two out-of-authority follow-ups the report already surfaces stand: prong b (divfree theme's inaccurate "first" / "no other op" claims at `divfree-projector-mutation-rotation.md:108-113`, `:457-464`, OQ `:2897`) needs a separate cycle-018 lifter/harvester append-only correction dispatch citing `eigsolve` as the prior two-gate instance; the `ksp_solve` preconditioner-as-`Solver` latent site awaits harvester L0 confirmation before promotion.
- The `skill-uptake-survey: warning` is informational only and does not block application.
