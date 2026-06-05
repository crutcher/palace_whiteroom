---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T060000Z
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
repaired_at: 2026-06-05T064500Z
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

# META: verification of "Formalize eliminate_bc at L4 (BC-elimination cohort L4 disposition)"

## Critique

### Checks run

**citation-validity — warning.** Every load-bearing L0 citation was re-verified against on-disk Palace
source via codemap `read_range`, and the structural pinpoints are exact:
- `rap.cpp:18` ctor `diag_policy(DiagonalPolicy::DIAG_ONE)` default — confirmed.
- `rap.cpp:36-47` `SetEssentialTrueDofs` — confirmed: policy guard `:39-41`, squareness guard `:42-43`,
  `dbc_tdof_list.MakeRef` `:45` + `diag_policy = policy` `:46`.
- `rap.cpp:56-83` `EliminateRHS` — confirmed line-for-line: gather `SetSubVector(tx,...)` `:64`, prolong
  `:65`, `A->Mult(lx, ly)` `:69`, restrict `:72`, `b.Add(-1.0, ty)` `:73`, diagonal-policy pin `:74-81`.
- `rap.cpp:139-148` `EliminateBC` apply — confirmed: call at `:143` inside the `&trial_fespace ==
  &test_fespace` square guard `:141`, rectangular reject `:145-148`. The report's headline claim
  "EliminateBC confirmed at line 143" is exactly right.
- Witnesses `laplaceoperator.cpp:216` (construction), `:217` (`SetEssentialTrueDofs(..., DIAG_ONE)`),
  `:252` (`PtAP_K->EliminateRHS(X, RHS)`) — all confirmed.
- Eigenmode witnesses `modeeigensolver.cpp:571,574,608,611` — all four lines confirmed via `search_text`.
- `multigrid.hpp:99-100` (`GetEssentialTrueDofs` → the `DofSet[N]` backing) — confirmed.
- The firm-L1 law/framing ranges (`eliminate_essential_bc.md:99-109,148-159`, `eliminate_rhs.md:142-150,
  262-264`) all resolve in-range and back the cited claims; both L1 sources carry `firmness: firm`.
- Both new-chapter frontmatter blocks round-trip through `yaml.safe_load` cleanly (no `note:`-leading-quote
  hazard; the parenthetical edge annotations parse).

The single sub-`pass` finding is a **carried-citation framing imprecision** (see Issue 1): the report
characterizes the eigenmode witnesses as "the A blocks the solve-side `DIAG_ONE`, the B blocks the
energy-block `DIAG_ZERO`," but the source shows `Ar=DIAG_ONE` `:571`, `Ai=DIAG_ZERO` `:574`, `Br=DIAG_ZERO`
`:608`, `Bi=DIAG_ZERO` `:611` — i.e. it is the *real-A* block that is `DIAG_ONE`; `Ai` is `DIAG_ZERO`,
not "A blocks → DIAG_ONE." The line numbers are correct and the load-bearing claim ("both policies
exercised") is true; only the per-block policy attribution is over-simplified. The report explicitly flags
these four lines as carried (not re-read this dispatch), which is honest, but the prose asserts a policy
split the cited lines don't fully support. Mechanical to correct; flagged not blocking.

**surface-or-evidence — pass.** This is a NEW firm L4 chapter (refinement-shaped: a new operator surface
with full evidence), not a pure rotation_claim. The eight algebraic laws split operator-side (idempotence,
free-block preservation, policy-determines-only-the-diagonal, DIAG_ZERO-distribution) / RHS-side (affine-on-
interior, linearity-in-boundary-data, homogeneous-BC identity) / cohort-level (separable post-composition),
and each is a read-off syntactic identity backed by a positive site: the operator-side laws on the
`EliminateBC` zero-rows-cols-then-set-diagonal body (`rap.cpp:139-148`) lifting the firm L1 law-set
(`eliminate_essential_bc.md:126-172`); the RHS-side laws on the `EliminateRHS` body (`rap.cpp:56-83`)
lifting `eliminate_rhs.md:112-162`. The non-laws are catalogued (no SPD guarantee, RHS not linear as a whole,
no per-term distribution, no policy commutativity) — good decoration-drift discipline.
Record-definition sub-check: `DofSet[N]` is named in both signatures and has ≥2 consumers; the report
correctly identifies it as a cross-cutting record (≥2 ⇒ concept page, NOT in-chapter), confirms
`concepts/DofSet.md` does not exist, FLAGS it `record-DofSet-needs-definition-home` in Open questions
(judge: flag, do not author — the layer-intro-author's domain), and provides a working description +
cross-reference pointer in the interim `## Record definition` section. This is exactly the prescribed
handling. `DiagPolicy` is single-use-shaped (named only by the two verbs in this chapter) and correctly
defined inline as the two-valued enum.

**rotation-quality — pass.** Two rotation claims to assess. (1) The L4 `eliminate_bc` cap promotes via
the **firm-on-positive-structure escape**, legitimately applied to BOTH verbs: every law is a syntactic
identity on fully-specified positive source (the `EliminateBC`/`EliminateRHS` bodies + the recorded
`(dofs, policy)`), so the missing dedicated test does not gate them — the `fe_assemble`/`apply_linop`
precedent. The escape is correctly scoped (the report verifies no `test/unit/**` hit and rests the
firmness on syntactic-identity-on-positive-source, not on absent test coverage). (2) The coupled L4>L3
dissolution theme is genuinely **substantive**, not identity-in-form: the pure value-returning
post-composition pair rotates to a deferred-config-then-apply two-step on a mutable `ParOperator` +
in-place `HypreParMatrix` mutation (operator-side) and an in-place pooled-scratch five-vector loop
(RHS-side). The L4 form is strictly more abstract (state hiding: `readonly` BC stratum captured once
→ mutable wrapper state; fresh-value return → destructive mutation; single logical `apply_linop` →
prolong/local-apply/restrict round-trip). This is a real rotation, not a rename. Route-(a)-vs-(b) and
the two-verb-one-chapter homing are assessed under Issues (both judged sound).

**variant-axis-coverage — pass.** Three orthogonal axes declared and each handled: `diagonal-policy`
(DIAG_ONE/DIAG_ZERO both covered, with the witnessed call-sites for each; MFEM's `DIAG_KEEP` explicitly
scoped out at the `ParOperator` boundary, anchored to the `:39-41` guard); `trial-test-coincidence`
(square = the only admissible case; rectangular explicitly a hard L0 reject, anchored to the `:145-148`
rectangular-reject branch); `bc-data-homogeneity` (RHS-side homogeneous vs inhomogeneous, with the
homogeneous-BC identity law 7 and both witnesses). No hidden branches.

**cross-reference-integrity — pass.** All `[link]` references resolve on disk: the four concept pages
(`state-stratification`, `black-box-vs-accelerated-kernels`, `constructed-operators`, `set_subvector_zero`),
`apply_linop`, `linear_combination`, `fe_assemble`, `essential_dofs`, `divfree-projector`, `fe_space`,
the sibling `fe-assemble-fold-dissolution` theme. SUMMARY.md alpha-placement is correct: `eliminate_bc`
inserts between `eigenfreq_qfactor_reduce` (`:61`) and `fe_assemble` (`:62`); the L4-L3 theme inserts
before `fe-assemble-fold-dissolution` (`:78`) — both alpha-correct. The L4/index.md dep-map insert anchor
(the `fe_assemble` row at `:48`) and the three L4-L3/index.md anchors (table row + bullet + tally) all
exist with exact old_string matches. The c069 re-anchor sites (`fe_assemble.md:119`,
`fe-assemble-fold-dissolution.md:127`) and the three essential_dofs mis-attribution edit targets in
`fe_assemble.md` all match their old_strings exactly. Rank-invariant: the one blocking `depends-on` edge
is to `linear_combination` (verified `firmness: firm`); the `fe_assemble` edge is classified `reference`
(post-composition position, not a blocking fold dep — backed by separability law 8). `firm` therefore
rests only on `firm` — invariant holds. Both new-file targets are clean (do not pre-exist).

**edge-label-fidelity — pass.** The dissolution theme carries the L4>L3 edge label and the prose discusses
exactly that edge (the L4 verb-pair lowering to the L3 imperative staging, narrated L4→RHS-L3 per high→low
discipline). The §"L3-entry-vs-dissolution-home verdict" correctly reasons about the L4→L3 image. The
depends-on/reference edge classification is sound and consistent across the cap, the dep-map row, and the
Status section.

**plan-kind-consistency — pass.** The report delivers two correctly-shaped kinds: a NEW firm L4 operator
cap (full Status/Signature/Algebraic-laws/Evidence apparatus, no rough-in placeholders, the firm claim
matched by the firm-on-positive-structure justification) and a firm L4>L3 dissolution theme (substantive
rotation, DISSOLUTION-HOME verdict, no interposed L3 entry — matching the `solve_family`/`fe_assemble`
NO-ENTRY precedent). The coupled mechanical fixes (essential_dofs mis-attribution correction, c069
re-anchor, index/SUMMARY registrations) are consistent with the route-(a) verdict. Both firm-claimed
bodies sit fully INSIDE their `new:`/`edit:` proposed-changes fences (build-readiness guard: confirmed —
the full `## Status` + Signature + Algebraic-laws + Evidence apparatus is enclosed within the
`new:book/src/L4/eliminate_bc.md` fence; nothing authored outside as top-level report sections).

**skill-uptake-survey — pass.** The disposition shape (warrant-first L4-lift, cross-pipeline mining-gate,
firm-on-positive-structure escape, record-definition obligation) implies several procedural skills; the
report explicitly invokes the disciplined-cross-pipeline-combinator-mining-gate, the firm-on-positive-
structure escape, the anti-mirror/over-unification guard, and the record-definition obligation, and
self-reports codemap `read_range` localization throughout. Telemetry-only check; nothing missing.

### Issues found

1. **Eigenmode policy-attribution imprecision (carried citation).** `CYCLE.md` §Specializations
   ("exercising **both** diagonal policies (the A blocks the solve-side `DIAG_ONE`, the B blocks the
   energy-block `DIAG_ZERO`)") and §Status ("the A blocks the solve-side `DIAG_ONE`, the B blocks the
   energy-block `DIAG_ZERO`"). Source shows `Ar=DIAG_ONE` (`:571`), `Ai=DIAG_ZERO` (`:574`),
   `Br=DIAG_ZERO` (`:608`), `Bi=DIAG_ZERO` (`:611`) — the `DIAG_ONE` is on the *real A* block only; the
   *imag A* block is `DIAG_ZERO`, contradicting the "A blocks → DIAG_ONE" framing. Line numbers correct;
   the load-bearing claim ("both policies are exercised") is true. Severity: low (cosmetic framing; does
   not affect any law or the route-(a) verdict). Candidate fix: rephrase to "the real-stiffness block
   `DIAG_ONE`, the imaginary/mass blocks `DIAG_ZERO`," or re-read `:560-612` to state the exact split.

2. **(Observation, not a defect) `eliminate-rhs-mutation-rotation` L1>L0 theme referenced in plain text,
   does not exist.** Both the L4 cap §"Lowers to" and the L4>L3 theme reference a forthcoming
   `L1-L0/eliminate-rhs-mutation-rotation.md`. The report correctly uses the missing-anchor plain-text
   convention (no broken `[link]`) and flags it in Open questions as out-of-scope-this-dispatch. Noted
   for cross-reference-integrity completeness; not a link defect (intentionally not linked). Surfaced so
   the integrator/repairer are aware the cross-reference resolves to prose, not a live link, by design.

### Route-(a) and homing judgments (rotation-quality detail)

- **Route (a) vs route (b): route (a) is the right call.** The cohort is positively established at L1 as
  a separable post-composition on the assembled operator value (verified: `eliminate_essential_bc.md:99-109`
  + `eliminate_rhs.md:142-150`), the laws are read-off syntactic identities, and there is genuine L4
  abstraction value (a backend-lowering BC-application verb-pair the backend wants AFTER its assemble
  engine). Route (b) — no-L4-by-design — would require an irreducible in-place index-masking op with no
  abstraction value; the positive separability framing refutes that. The ≥2 structurally-identical
  cross-pipeline witnesses (electrostatic + eigenmode, no break-witness) clear the mining-gate bar.
- **Two-verb-one-chapter homing is sound (not a forced split or forced merge).** The two verbs are
  genuinely distinct in codomain (`LinearOperator[N,N]` vs `Tensor[N]`) and algebra (the operator-side
  distributes over the fold under DIAG_ZERO; the RHS-side explicitly does NOT — law 4 vs the cataloged
  non-law), so merging into one combinator would be a forced merge. But they share the `(DofSet[N],
  DiagPolicy)` vocabulary and the single "apply Dirichlet BC after assembly" surface, and Palace applies
  them as a pair — so two thin mirror chapters would be the anti-mirror smell. One chapter, two co-equal
  verbs is the correct granularity.

---

## Repair

### Fixes attempted

- **Finding 1 (citation-validity, warning, low)**: Eigenmode policy-attribution imprecision — CYCLE.md
  §Specializations + §Status framed the eigenmode witnesses as "A blocks → DIAG_ONE, B blocks →
  DIAG_ZERO," but the source shows only the real-stiffness block `Ar` (`:571`) is `DIAG_ONE`; `Ai`
  (`:574`), `Br` (`:608`), and `Bi` (`:611`) are all `DIAG_ZERO`.
  - **Decision**: repaired.
  - **Action**: Re-read `modeeigensolver.cpp:565-615` via codemap `read_range`, confirming the exact
    per-block split (`Ar`→`DIAG_ONE` `:571`; `Ai`/`Br`/`Bi`→`DIAG_ZERO` `:574,608,611`). Corrected the
    over-simplified phrasing in three places: (i) CYCLE.md §Specializations (inside the
    `new:book/src/L4/eliminate_bc.md` chapter-body fence — so the correction flows into the authored
    chapter), rephrased to "the real-stiffness block `Ar` uses `DIAG_ONE`; the imaginary-stiffness block
    `Ai` and both mass blocks `Br`/`Bi` use `DIAG_ZERO`"; (ii) CYCLE.md §Status, where the mining-gate
    witness cite now carries the per-block split; (iii) the §Supporting evidence carried-citation note,
    updated to record that the four eigenmode lines were re-read this repair pass with the exact policies.
    The `L4/index.md` dep-map row (line 702, the `edit:` block) said only "both policies" with no false
    split, so it needed no change. The load-bearing claim ("both policies exercised") was preserved
    throughout; only the per-block attribution was sharpened. No law, signature, route-(a) verdict, or
    rotation argument was touched.

- **Finding 2 (Issue 2, informational, non-defect)**: `eliminate-rhs-mutation-rotation` L1>L0 theme
  referenced in plain text (no `L1-L0/eliminate-rhs-mutation-rotation.md` exists).
  - **Decision**: not-needed.
  - **Rationale**: This is the correct missing-anchor plain-text convention (no broken `[link]`), already
    flagged in §Open questions as out-of-scope-this-dispatch. The critic surfaced it only for integrator
    awareness; no fix is owed. Noted here so the integrator knows the cross-reference resolves to prose
    by design.

### Unrepairable findings

None. The single sub-`pass` finding was mechanically correctable (a per-block citation-precision fix
against fully-specified positive source) and within repair authority; the second finding is a non-defect.

## Suggested resolution

`ready`. The one warning was a cosmetic per-block policy-attribution imprecision, now corrected against
re-read source. The route-(a) verdict, the new firm L4 `eliminate_bc` chapter, the coupled L4>L3
`bc-elimination-post-composition-dissolution` theme, the firm-on-positive-structure escape, and all
coupled mechanical fixes (essential_dofs mis-attribution, c069 re-anchor, index/SUMMARY registrations)
are sound per the critic and preserved.

Integrator notes: (1) the `eliminate-rhs-mutation-rotation` reference is intentional plain-text per the
missing-anchor convention — do NOT treat it as a broken link; the OQ flags it for a future
abstractor/lifter L1>L0 pass. (2) `record-DofSet-needs-definition-home` is flagged in §Open questions
for a layer-intro-author concept-page pass (`concepts/DofSet.md` does not exist; the interim working
description lives in the chapter's `## Record definition` section). (3) The §Open-questions intro-refresh
note (L4/index.md firm-count narration) is layer-intro-author's domain, not blocking.
