---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T201500Z
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
repaired_at: 2026-06-02T202200Z
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

# META: verification of "Combinator candidates — `linear_combination` + `inner_product` rise to L4"

## Critique

### Checks run

**citation-validity — pass.** Spot-checked every load-bearing pinpoint against the artifact. The firm-L3-endpoint anchors resolve and are in-range: `L3/linear_combination.md` is `firm` (status line confirmed) with the stale "no L4" lines exactly where cited (`:7-8` frontmatter `lifts_from`, `:154-156` §"Lifts from"); `L3/inner_product.md` is `firm` with stale lines at `:7-8` and `:74-78` as cited. The classification-concept anchor `black-box-vs-accelerated-kernels.md:128-136` reads exactly "The combinators rise regardless … rise to L4 regardless … (Both combinators currently stop at L3 and are queued to rise to L4)" — the report's quotation is faithful. The §2 kept-named-abstraction anchor (`:88-109`) and the krylov-step anchor (`L4/krylov-step.md:67`) resolve. The `test-vector.cpp:206-207` real-dot witness is confirmed (`dot = vec1*vec2; CHECK_THAT(dot, WithinRel(32.0))`). The eigsolve/chebyshev in-line-marker precedent refs (`L4/index.md:39`/`:75`/`:81`) resolve and genuinely exhibit the "no dedicated L4>L3 theme / in-line marker-erasure" route the report claims to follow. No `verified_against:` YAML block in this report (combinator-miner kind), so that sub-check is N/A. No fresh `path:lo-hi` L0 range is asserted (all L0 evidence inherited transitively), so the close-brace recurrence-6 sub-check is vacuously satisfied — correctly self-flagged.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (two new L4 surface entries + an `L4/index.md` correction) with full surface text in the supporting docs AND a rotation-claim (the L4>L3 identity-in-form edge). The L4 bodies forward all algebraic detail to the firm L3 forms; I checked the carried-up content does not contradict the firm L3 entries — the seven laws, the conjugation-at-arg-1 convention, the deferred IEEE non-law, and the variant-axis profiles match the L3 endpoints (both `firm`). No positive claim is asserted that the firm L3 entries do not already support. The "rises as a feature-surface verb, no first-class L4 calculus structure of its own" framing is honest about what is and is not new.

**rotation-quality — pass.** The decision to declare the L4>L3 edge identity-in-form with NO dedicated `L4-L3/*-dissolution.md` theme is sound and is the methodologically-correct call. A dissolution theme here would be the degenerate identity-in-named-terms smell the 2026-06-01 redirect names (LHS and RHS the same named combinator at the same arity, no vocabulary shift) — the report correctly cites this (§1d smell) and routes via the established `eigsolve`/`chebyshev` in-line-marker convention, which I verified is genuinely how those entries handle their L4>L3 edges. The substantive rotation in the chain is correctly located at the L2>L1 fusion-selection themes (both confirmed on disk), not at this identity edge. The over-unification guard is well-constructed: `linear_combination` (tensor-producing term-list fold) and `inner_product` (scalar-producing length-axis reduction) are deliberately NOT merged (different result types, homomorphism domains, combining steps), and `nrm2`/`matrix-weighted-norm` are correctly classified as `√∘abs∘inner_product` consumers, NOT fold members. The guard is symmetric across both entries.

**variant-axis-coverage — pass.** Both entries enumerate their axes with explicit unification-axis identification. `linear_combination`: arity (unification axis), output-aliasing (scoped below-L3), element-type, operand-category (the next-pull `assemble_frequency_operator` corner). `inner_product`: conjugation-convention (unification axis), element-type, weight-presence; the `tdot × weight` cell is explicitly scoped out (Palace exposes no `tdot_M`), and diagonal-degeneration is explicitly excluded as a consumer-entry-point rather than an axis. No hidden branches.

**cross-reference-integrity — warning.** All named slugs except one resolve on disk: `L3/linear_combination`, `L3/inner_product`, `L3/apply_linop`, both L2>L1 fold-specialization themes, all three concept pages, and `L1/assemble_frequency_operator` all EXIST. The single unresolved link is `book/src/L4/fe_assemble.md` (MISSING on disk), referenced by both the §Active-frontier prose and the `(10+4)` tally narrative. This is correctly flagged in the report as D1's same-cycle landing (forward-reference; the integrator wires it). The warning (not fail) is because this is a known parallel-dispatch forward-ref with an explicit integrator note and an explicit recount-fallback ("if D1 lands a status OTHER than firm, integrator-finalize recounts from `## Status` and adjusts 10 → audited value"). **Count-ownership is correct:** I independently audited the firm count from each linked chapter's `## Status` line (NOT index cells, per the c057-meta guard) — 7 prior firm (`krylov-step`, `iterate-while`, `iterate-while-with-prev`, `chebyshev`, `ksp_solve`, `eigsolve`, `fold_solve` all `firm`; `solve_family` is `rough-in (test-coverage-bounded)`, correctly NOT counted) + `fe_assemble` (D1) + `linear_combination` + `inner_product` (D3) = 10 firm + 4 outer-driver. The `(7+4)→(10+4)` arithmetic and the per-operator 7→10 transition are right, conditional only on D1's `fe_assemble` landing firm (D1's report is firm) and D3's two entries being firm (their supporting-doc `firmness: firm` + `## Status: firm` are present). The §Active-frontier prose registers all three c068 landings as required. The build-readiness guard (firm-body-inside-fence) is N/A in the cycle-019 sense because the firm bodies live in supporting docs the integrator applies verbatim, not inside a proposed-changes fence — confirmed below under fence parity.

**edge-label-fidelity — pass.** Every edge label is L4>L3 and the surrounding prose discusses exactly the L4>L3 edge (identity-in-form, value-thread-isomorphic body). The transitive L4>L3>L2>L1 chain is correctly narrated as composition (in-line L4>L3 identity ∘ firm L3>L2 identity ∘ substantive L2>L1 fusion-selection), with the substantive content correctly attributed to the L2>L1 edge, not mis-labeled onto the L4>L3 edge.

**plan-kind-consistency — pass.** Declared as a combinator-miner upward in-layer rendering (rise of two already-firm mined combinators), and the content shape matches: firm entries propagating settled L3 combinators upward, NOT new mines. The `firm` status claim is consistent with the syntactic-identity / firm-on-positive-structure escape (laws carried up unchanged from firm endpoints; missing dedicated `linear_combination` test does not gate because every L4 law is a syntactic identity — the `chebyshev` precedent). No rough-in placeholders in firm-claimed bodies.

**skill-uptake-survey — pass.** The report cites `disciplined-cross-pipeline-combinator-mining-gate` and correctly argues the 4 gate points are satisfied by the firm L3 endpoints (the gate is for new mines; this is an upward rendering of a settled one — not re-mined). It also cites the `convert-nested-fences-to-indented-code-in-proposed-changes-block` guard as the rationale for the indented-code-block body strategy. Both invocations are appropriate to the proposal shape.

### Issues found

1. **Forward-reference to a not-yet-on-disk file: `book/src/L4/fe_assemble.md` (cross-reference-integrity, low severity).** Location: CYCLE.md §"Proposed changes" — the §Active-frontier edit block (`L4/index.md` append, the `[fe_assemble](./fe_assemble.md)` link) and the `(10+4)` tally narrative; also the cohort-header replacement at the `[fe_assemble](./fe_assemble.md)` link. The target does not exist on disk yet (it is D1's same-cycle landing). This is a genuine dead link IF D1 does not land or lands under a different slug. The report explicitly flags it as a forward-ref with an integrator-recount fallback, so it is a coordinated parallel-dispatch dependency rather than a drop — but the integrator must confirm `fe_assemble.md` is on disk before applying the D3 `L4/index.md` edits (the `linkcheck2` build gate will hard-fail on a live link to a missing file). Candidate repair note for downstream: if D1's landing slips, the `fe_assemble` link must be demoted to plain-text and the tally adjusted to `(9+4)` per the stated recount rule.

2. **Stale "no L4" lines in the firm L3 entries are a recorded OQ, not an unflagged drop (cross-reference-integrity, informational — no defect).** Location: CYCLE.md §"Open questions / caveats" bullet 1 + both supporting docs §"Downward to L3" staleness notes. I confirmed both `L3/linear_combination.md` (`:7-8`, `:154-156`) and `L3/inner_product.md` (`:7-8`, `:74-78`) still assert "no L4 entry exists," which becomes stale once these L4 entries land. The report correctly scopes the re-anchor OUT of this dispatch (one-operator-per-dispatch + L3 entries outside write-scope) and files it as a c069/meta plan candidate, following the exact `eigsolve` precedent (the seven stale `L3/eigsolve` §Upward assertions, re-anchored by a later pass). This is the correct handling — recorded, not silently dropped. Noted here only so the integrator/planner carries the follow-up forward; no repair needed in this report.

3. **`L4/krylov-step.md:67` is an interpretive citation, not a literal one (citation-validity, very low severity).** Location: CYCLE.md §"Pattern instances" Instance 4 ("the GMRES basis-correction sum is a `linear_combination` over scalar-weighted basis terms; CG `α`/`β` + GMRES orthogonalization coefficients are `inner_product` let-bindings"). Line 67 literally reads "update primitives are L1 calls — axpy, axpby, axpbypcz, dot, nrm2, scal." The claim that these constitute `linear_combination`/`inner_product` usage is a sound interpretation (those L1 calls ARE the combinator members/specializations), but the line does not literally name the combinators. The reading is fair and the supporting context (`krylov-step.md:60-75`, the `krylov_update`/`K_aux` group) backs it; flagged only for precision — the pinpoint supports the weaker "these primitives appear in the body" claim directly and the combinator-identity claim by member-subsumption. Not a misuse; no repair required.

### Note on fence parity / build-readiness

Both supporting docs (`L4-linear_combination.md`, `L4-inner_product.md`) use **indented code blocks throughout (zero backtick fences)** — confirmed by grep. This is the deliberate nested-fence-truncation-avoidance strategy the report names (the `convert-nested-fences-to-indented-code-in-proposed-changes-block` guard). Fence parity is therefore trivially clean. The firm bodies are full and self-contained in the supporting docs (status + signature + algebraic-laws + evidence all present and INSIDE the doc), so the cycle-019 firm-body-outside-fence defect does not apply — the integrator applies these verbatim as the named target files, not from inside a proposed-changes fence.

## Repair

### Fixes attempted

- **Finding 1 (warning, cross-reference-integrity): live link `[fe_assemble](./fe_assemble.md)` in the `L4/index.md` dep-map / cohort-header / §Active-frontier edits points at `book/src/L4/fe_assemble.md`, which is NOT yet on disk (D1's same-cycle landing).**
  - **Decision:** not-needed (integration-ordering constraint, not a content defect).
  - **Rationale:** This is not a dead link to be demoted or a forgotten reference to be filled — it is a **coordinated parallel-dispatch forward-reference** to D1's same-cycle artifact. D1 (the `fe_assemble` harvester) authors `book/src/L4/fe_assemble.md` **firm** (D1's report `overall_status: ready`, status `firm`) in this same cycle-068. The per-report integrators run **serially** (artifact writes naturally serialize — CLAUDE.md §Cycle structure Phase 5). Therefore the resolution is purely a **sequencing requirement on the orchestrator/integrator**, not an edit to this report: apply D1 (which puts `L4/fe_assemble.md` on disk) **before** applying D3's `L4/index.md` edits, and `linkcheck2` resolves the link cleanly. The report already carries the matching integrator-recount fallback (CYCLE.md §Open questions bullet 3 + the dep-map integrator note) for the contingency that D1 lands a status other than firm. Demoting the link to plain-text and adjusting the tally to `(9+4)` is the **fallback only if D1 does not land** — it must NOT be pre-applied, because D1 is landing. No mutation to CYCLE.md is warranted; the correct artifact is the explicit integrator-ordering note below.

- **Finding 2 (informational, cross-reference-integrity): stale "no L4" lines in the firm `L3/linear_combination` (`:7-8`, `:154-156`) and `L3/inner_product` (`:7-8`, `:74-78`) become stale once these L4 entries land.**
  - **Decision:** not-needed.
  - **Rationale:** Correctly scoped OUT of this dispatch by the report (one-operator-per-dispatch + the L3 entries are outside this report's write-scope) and filed as a c069/batch-21-meta re-anchor plan candidate (CYCLE.md §Open questions bullet 1), following the established `eigsolve` precedent. Recorded, not silently dropped. Re-anchoring is substantive content authored on out-of-scope files — outside repair authority, and it does not gate this report's application. The c069 planner carries it forward (see Suggested resolution).

- **Finding 3 (informational, citation-validity): `L4/krylov-step.md:67` is an interpretive citation (the line names the L1 calls `axpy/axpby/axpbypcz/dot/nrm2/scal`; the combinator-identity reading is member-subsumption, not literal).**
  - **Decision:** not-needed.
  - **Rationale:** The critic confirmed the reading is fair and backed by surrounding context (`krylov-step.md:60-75`); the pinpoint directly supports the weaker "these primitives appear in the body" claim and the combinator-identity claim by member-subsumption. Flagged for precision only; the critic explicitly states "no repair required." No mechanical fix applies (the citation is correct for what it supports).

### Unrepairable findings

None. The single warning is an integration-ordering constraint resolved by serial integrator sequencing (D1→D3), not a content defect; the two informational notes are correctly-filed OQs requiring no in-report change.

### Integrator-ordering requirement (load-bearing)

**Apply D1 BEFORE D3.** The per-report integrators run serially. D3's `book/src/L4/index.md` edits add a live link `[fe_assemble](./fe_assemble.md)`. That target is created by **D1** (`fe_assemble` harvester, this same cycle-068, status firm). The integrator MUST:
1. Apply **D1 first** so `book/src/L4/fe_assemble.md` is on disk.
2. Then apply **D3's** `L4/index.md` edits (cohort-header `(10+4)` tally, dep-map rows, §Vocabulary-cohort bullets, §Active-frontier prose) + the two new L4 combinator files.
3. At `integrator-finalize`, the `(10 + 4)` firm tally is counted from `## Status` lines per the c057-meta count-owner guard. If D1's `fe_assemble` lands a status OTHER than firm, recount and adjust `10` → audited value AND demote the `fe_assemble` link to plain-text per the report's stated fallback (CYCLE.md §Open questions bullet 3). D1 is currently firm/ready, so the expected outcome is `(10 + 4)` with the live link intact.

D3 is the **sole `L4/index.md` consolidated-count/tally/frontier-prose owner** this cycle; D1 owns only its own `fe_assemble` dep-map row + cohort bullet (anchor-distinct, parallel-safe). No write conflict on `L4/index.md` between D1 and D3 beyond this ordering.

## Suggested resolution

`overall_status: ready`. All 8 checks are pass/not-needed — the lone warning is an ordering constraint with no content edit required. Notes for the integrator:

1. **Sequence D1 → D3** (see Integrator-ordering requirement above). This is the only constraint that gates a clean `linkcheck2` build.
2. **Count from `## Status` lines** for the `(10 + 4)` tally; D1=firm is the expectation, recount-and-demote is the documented fallback.
3. **Promote the c069 follow-up:** the stale "no L4" re-anchor of `L3/linear_combination` (`:7-8`, `:154-156`) and `L3/inner_product` (`:7-8`, `:74-78`) to "lifts to `L4/{linear_combination,inner_product}` (firm cycle-068)" — file/carry as a c069 or batch-21-meta lifter/lowering-verifier plan candidate (the `eigsolve` precedent route). Out of D3's write-scope; not a blocker.
