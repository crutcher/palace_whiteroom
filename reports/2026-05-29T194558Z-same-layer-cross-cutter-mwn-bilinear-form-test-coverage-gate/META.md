---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T20:31:00Z
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
repaired_at: 2026-05-29T20:52:00Z
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

# META: verification of "L1 observation — matrix-weighted-norm + bilinear-form share a test-coverage gate that the corpus does NOT close"

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck.py --scan` on the report: **32 ok, 0 failing** (all bounds + path-hygiene clean). Anchor-verified every load-bearing pinpoint with `--anchor`: the source-side anchors (`operator.cpp:599-607` `Norml2`, `:609-619`/`:613-614` `Imag` lane-split, `:621-639` `Dot` overloads, `operator.hpp:372-374`/`:386-394` decls, `boundarymodeoperator.cpp:85` `Bttr`, `:90` `Atn`), the test-side anchors (`test-domainpostoperator.cpp:83-93` `WithinRel`, `:31-32` `TODO`, `test-orthog.cpp:53-68` `Imag`, `:368-376` `ComplexWrapperOperator`, `test-vector.cpp:209-211` `Norml2`), and the eigensolver weight-rep witnesses (`arpack.cpp:438` `Norml2`, `:442`/`:470`, `slepc.cpp:475`, `nleps.cpp:114`) ALL resolve in-range. Two items dropped this from `pass` to `warning` (see Issues #1, #2 — neither undermines the load-bearing conclusion):
- `citecheck --anchor "RealWeightedInnerProduct"` on `test-orthog.cpp:46-51` reports `[DRIFT]` pointing at line 38. This is a **false drift**: line 38 is the class constructor; the cited range `:46-51` is exactly the real `RealWeightedInnerProduct::operator()(const Vector&, const Vector&)` body (`weight_op->Mult(x, v_workspace); return linalg::LocalDot(v_workspace, y)`), which is precisely the "real weighted IP functor / `W.Mult` then unweighted `linalg::LocalDot`" the report describes. Adjudicated by reading the source — citation is **correct**, the anchor literal merely first appears earlier. Recorded so the repairer/integrator does not chase a phantom off-by-one.
- A **factual count error**: the report (Summary `:18`) states the corpus is "30 `test-*.cpp` files." On disk there are **23** `test-*.cpp` (25 total `.cpp` including `fixtures.cpp` + `main.cpp`). This is an overstatement of the corpus size; it does not weaken the survey conclusion (the negative grep claims hold regardless), but it is a wrong number in the artifact-feeding report.

**surface-or-evidence — pass.** This is a survey/observation report with no surface mutation and no proposed-changes block; the recommendation is explicitly ask-class (STAY rough-in, defer promotion). It is not a refinement proposal, so the surface-or-evidence gate is not the operative shape — but the load-bearing "0 callsites" evidence WAS independently verified and holds: `grep` over `reference/palace/test/unit/` confirms the 4-arg weighted `Norml2(comm,x,B,Bx)` appears **0 times** (only 2-arg/3-arg unweighted `linalg::Norml2(Mpi::World(), V[i])` forms in `test-orthog.cpp:191,206`), the 4-arg weighted `linalg::Dot(comm,x,A,y)` appears **0 times** (only the unweighted 3-arg `linalg::Dot(Mpi::World(), w, V[i])` forms in `test-orthog.cpp`/`test-romoperator.cpp`), and `GetEigenvectorNorm` appears **0 times** in `test/unit/`. The negative confirmation for `test-boundarymodeoperator.cpp` (no `Dot|Poynting|energy|Bttr|Atn`) reproduces exactly — NONE. The indirect/reimplemented framing (`test-domainpostoperator.cpp` real-energy, `test-orthog.cpp` test-local `RealWeightedInnerProduct`) is accurate evidence and correctly labelled as shape-only / not-at-entry-point.

**rotation-quality — pass (not applicable to survey-kind).** No algebraic/structural/reduction rotation is asserted; this report compares two existing L1 operators' test-coverage and explicitly declines to unify them. No rotation claim to grade.

**variant-axis-coverage — pass.** The asymmetry claim (bilinear-form strictly worse than matrix-weighted-norm) is evidence-grounded and survives scrutiny. The two variant-axis tables (`matrix-weighted-norm.md:94-106`, `bilinear-form.md:257-302`) are correctly transcribed. The "worse" verdict rests on two bilinear-form axis values with NO coverage at any granularity: the complex-weight `ComplexOperator` `A` (`operator.cpp:631-639`) and the non-symmetric-`M` law-7-failure (`Atn`, `boundarymodeoperator.cpp:90`) — both verified to have zero test reference, vs matrix-weighted-norm's element-type axes which ARE shape-covered by `test-orthog.cpp`. The report does NOT hide branches: it explicitly enumerates each axis value's coverage status and scopes out the not-surfaced real-`M`-real-`y` case (`bilinear-form.md:85-89`, confirmed verbatim). The complex `Norml2` lane-split / `RealWeightedInnerProduct` four-real-dot construction equivalence (`operator.cpp:613-614` ≡ `test-orthog.cpp:59-65`) is a real structural match, correctly used to narrow (not close) the element-type gate.

**cross-reference-integrity — pass.** Both L1 operators resolve in `SUMMARY.md` (`:73` matrix-weighted-norm, `:74` bilinear-form). The matrix-weighted-norm L1>L0 theme is wired (`SUMMARY.md:105`); there is NO bilinear-form theme row — confirming the report's central correction. Verified on disk: `book/src/L1-L0/` contains `matrix-weighted-norm-mutation-rotation.md` and NO `bilinear-form-*.md`. The status-line citations resolve: `matrix-weighted-norm.md` status `:108-110` with gates (a)/(b)/(c) at `:113`/`:114`/`:115`; `bilinear-form.md` status `:319-344` (report's `:321` and `:334-344` both land inside). The sibling theme's "forthcoming `bilinear-form-mutation-rotation`" reference (`:319-326`) and firm `## Status` (`:434`) both resolve. The OQ ledger references resolve exactly: `:26` is the migrated plan item (and confirms `bilinear-form-variant-axis-test-coverage` / `bilinear-form-real-vector-coverage-gap` exist ONLY as constituent references, not standalone slugs — as the report claims), `:769` is `matrix-weighted-norm-mixed-element-type-variant` plan-c028-#4, `:201` is the partially-answered cycle-008 OQ. No `[link]` is introduced (no proposed-changes block), so no firm-body-inside-fence guard applies.

**edge-label-fidelity — pass (not applicable to survey-kind).** No L_{n+1}→L_n edge label is carried; the report discusses same-layer (L1) operators and references an absent L1>L0 theme by name. No edge-label-vs-prose mismatch possible.

**plan-kind-consistency — pass.** Content shape matches an observation/survey dispatch. The producer correctly did NOT mutate the artifact, did NOT write a proposed-changes block, and did NOT unilaterally promote either operator — it surfaces the promotion as an ask-class decision (`:157`, `:187-192`, "No promotion is enacted here") consistent with the CLAUDE.md `rough-in (test-coverage-bounded)` qualifier (promotion gated on test coverage partly out of write-scope). The "bilinear-form theme doesn't exist" re-scoping is accurate (verified absent on disk) and is a legitimate, valuable dispatch-framing correction, properly flagged in §Open questions `:259-264`. The recommendations (defer/record-sharpened-gate, narrow the mixed-element-type OQ, dispatch abstractor on the missing theme, do-not-unify) are all intake/follow-up class, not enacted edits — correct for this kind.

**skill-uptake-survey — pass.** The report's shape (citation-heavy survey with negative-confirmation greps) implies `verify-citation-range` / `tools/citecheck` uptake; the report explicitly states anchors were "citecheck `--anchor` verified this invocation" (`:118`, `:227`, `:235`) — the telemetry is surfaced. No other shape-implied skill is missing.

### Issues found

1. **(citation-validity, warning, factual) Corpus file-count overstatement.** CYCLE.md Summary `:18` says "30 `test-*.cpp` files" in `reference/palace/test/unit/`. The actual count is **23** `test-*.cpp` (25 `.cpp` total counting `fixtures.cpp` + `main.cpp`). The survey conclusion is unaffected (the 0-callsite negative claims reproduce exactly), but the number is wrong and feeds downstream as an inaccurate corpus-size assertion. Candidate for a one-token correction (30 → 23).

2. **(citation-validity, informational, no-fix-needed) False `[DRIFT]` on `test-orthog.cpp:46-51`.** `citecheck --anchor "RealWeightedInnerProduct"` flags drift to line 38, but the cited `:46-51` is correctly the real `operator()` body; line 38 is just the constructor where the type name first appears. The citation is accurate. Recorded only so a downstream agent does not "fix" a correct citation. If the repairer wants a cleaner mechanical anchor, the body is anchorable on `LocalDot` (line 50) rather than the type name.

3. **(cross-reference-integrity / precision, minor) "No `test-operator*.cpp`" phrasing is glob-literal-true but imprecise.** CYCLE.md Summary `:19-20` and the matrix-weighted-norm status it quotes assert "There is no `test-operator*.cpp` / `test-eigen*.cpp`." Literally true for those exact prefixes, but the corpus DOES contain operator-family tests — `test-boundarymodeoperator.cpp`, `test-domainpostoperator.cpp`, `test-postoperator.cpp`, `test-romoperator.cpp`, `test-materialoperator.cpp`. The report DOES engage those files directly (it cites `test-domainpostoperator.cpp` and the `test-boundarymodeoperator.cpp` negative), so this is not a hidden branch — just a phrasing that could read as "no operator tests at all" when the precise claim is "no test at the `linalg::` weighted free-function entry point." Optional sharpening; the substantive coverage claim is sound.

## Repair

### Fixes attempted

- **Finding #1 (citation-validity, warning): Corpus file-count overstatement.** Summary `:18` says "30 `test-*.cpp` files"; true count is 23.
  - **Decision**: repaired.
  - **Action**: verified the count independently (`ls test-*.cpp | wc -l` in `reference/palace/test/unit/` → 23; 25 `.cpp` total counting `fixtures.cpp` + `main.cpp`), then corrected the figure in CYCLE.md Summary §Summary `:18` (30 → 23). Mechanical one-token fix; the survey conclusion was already unaffected (the 0-callsite negative claims reproduce regardless), so this is pure factual-accuracy correction, no content authored.

- **Finding #2 (citation-validity, informational): False `[DRIFT]` on `test-orthog.cpp:46-51`.** citecheck `--anchor` pointed at line 38 (the constructor), but `:46-51` is correctly the real `operator()` body.
  - **Decision**: not-needed (LEAVE AS-IS).
  - **Rationale**: the citation is accurate per the critic's source-read adjudication; the anchor literal merely first appears at the constructor. "Fixing" a correct citation would introduce an error. The critic explicitly recorded this so no downstream agent chases the phantom off-by-one. No edit applied.

- **Finding #3 (cross-reference-integrity / precision, minor): "No `test-operator*.cpp`" phrasing glob-literal-true but imprecise.** Could read as "no operator tests at all" when the precise claim is "no test at the `linalg::` weighted free-function entry point."
  - **Decision**: repaired (optional sharpening applied).
  - **Action**: sharpened the Summary phrasing at CYCLE.md §Summary `:19-20` to state the precise claim — "no test at the `linalg::` weighted free-function entry point" — while preserving the glob-literal-true fact and explicitly noting that operator-*family* tests (`test-boundarymodeoperator.cpp` / `test-domainpostoperator.cpp`) do exist and are engaged below. Mechanical phrasing tightening over the critic's exact precise-claim wording; no new evidence or content authored.

### Unrepairable findings

None. The two repaired findings were mechanical (a factual count correction verified against disk, and a phrasing tightening to the critic's stated precise claim); the third was correctly a no-op.

## Suggested resolution

`ready`. Notes for the integrator:

- This is a **survey/observation dispatch with NO proposed-changes block and NO artifact mutation** — there is nothing to apply to `book/`. The repairs landed entirely within the report's own text (CYCLE.md Summary).
- The report's load-bearing recommendation is **ask-class**: STAY `rough-in` for both `matrix-weighted-norm` and `bilinear-form` with sharpened, asymmetric promotion gates; do NOT unilaterally promote (the qualifier ties promotion to test coverage partly out of project write-scope). The integrator should **record this as a deferred-contingent OQ / plan item**, not enact a book mutation:
  - Record the per-operator sharpened gates against the plan item `matrix-weighted-norm + bilinear-form firm-promotion` (`scaffolding/open-questions.md:26`).
  - Narrow OQ `matrix-weighted-norm-mixed-element-type-variant` (`:769`): the real-`B`-on-complex-`x` element-type variant is now shape-witnessed by `test-orthog.cpp`; residual gate is the named-entry-point √+SPD-guard test.
  - The follow-up `bilinear-form-mutation-rotation` L1>L0 theme (named "forthcoming", does not exist on disk) is a future abstractor dispatch, not an edit to apply this cycle.
