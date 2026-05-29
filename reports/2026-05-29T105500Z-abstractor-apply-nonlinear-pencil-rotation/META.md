---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T11:20:00Z
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
repaired_at: 2026-05-29T11:35:00Z
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

# META: verification of "L1>L0 theme sketch — apply-nonlinear-pencil-mutation-rotation"

## Critique

### Checks run

**citation-validity — pass.** Every L0 range cited in the proposed theme was independently
re-verified this invocation via `palace-codemap` `read_range` (not trusting the report's own
self-verification table). All load-bearing ranges land on-disk exactly as cited:
- `nleps.cpp:807-821` (`GetResidualNorm`, Form A): `opK->Mult(x, r)` :812, `if (opC) { opC->AddMult(x, r, l); }` :813-816, `opM->AddMult(x, r, l*l)` :817, `auto A2 = (*funcA2)(std::abs(l.imag()))` :818, `A2->AddMult(x, r, 1.0)` :819, `return linalg::Norml2(comm, r)` :820 — all confirmed; the source's own residual comment is at :809-810 (the report cites the comment as `:810-811`, off by one — the `// Compute ... residual` line is :809 and the `for eigenvalue λ.` continuation is :810; the comment body is the two lines :809-810, see Issues #1, cosmetic).
- `nleps.cpp:494-500` (in-`Solve` setup): `opA2 = (*funcA2)(...)` :497, `opA = BuildParSumOperator({1, eig, eig*eig, 1}, {opK, opC, opM, opA2.get()}, true)` :498-499 — confirmed.
- `nleps.cpp:547-560` (`compute_residual` core, Form B): `A2_out = (*funcA2)(std::abs(lam.imag()))` :556, `BuildParSumOperator({1, lam, lam*lam, 1}, {opK, opC, opM, A2_out.get()}, true)` :557-558, `A->Mult(vv, rr)` :559 — confirmed.
- `nleps.cpp:650-657` (Jacobian): `opA2p`/`opAJ` divided-difference build :650-654, `opJ = BuildParSumOperator({0, 1, 2eig, 1}, {opK, opC, opM, opAJ.get()}, true)` :655-656, `opJ->Mult(v, w)` :657 — confirmed (the `{0, 1, 2λ, 1}` coefficient vector is correct).
- `nleps.cpp:725-733` (lagged refresh): `opA2 = (*funcA2)(std::abs(eig_opInv.imag()))` :727, `opA = BuildParSumOperator(...)` spanning :728-730 with `{1, eig_opInv, eig_opInv*eig_opInv, 1}` — confirmed (the report cites `opA =` at :728, args :729-730; accurate).
- `nleps.cpp:177-181` (`SetExtraSystemMatrix`, real-argument closure type) — confirmed.
- `nleps.cpp:191`/`:221` (the two `SetOperators` overloads: 2-arg `(K, M, type)` = without-C at :191, 3-arg `(K, C, M, type)` = with-C at :221) — confirmed.
- `nleps.hpp:146` (class comment `(K + λ C + λ² M + A2(λ)) x = 0`) — confirmed, immediately preceding the class decl.
- `nleps.hpp:232`/`:246` (`Interpolation` / `NewtonInterpolationOperator`) — confirmed.
- `eps.hpp:69-74` (nonlinear `SetOperators` virtual; complex-argument `A2` closure) — confirmed, and the report's distinction (this overload's `A2` is complex-argument `std::function<const ComplexOperator &(std::complex<double>)>`, distinct from the operative real-argument `SetExtraSystemMatrix`) is accurate.
- `rap.cpp:832-841` (`BuildParSumOperator` signature; `nullptr`-entry skip via `std::find_if(... p != nullptr ...)` at :837) — confirmed.
All L1 cross-reference line citations into `book/src/L1/apply_nonlinear_pencil.md` were checked against the live file and are accurate: `:21-26` (signature), `:51` (semantics pt 1 `|Im λ|`), `:63` (law 3 term-decomposition), `:71` (two-build-form bit non-law), `:72` (A2-recompute non-law), `:89` (purpose/coeff-vector axis), `:93` (A2-representation axis), `:94` (L0-build-form axis), `:98` (firm-on-positive-structure status). The sibling-theme citation `nleps-deflated-residual-mutation-rotation.md:23-35` correctly points at that theme's firm-on-positive-structure Status block. The OQ reference `open-questions.md` line 461 correctly contains the `nleps_jacobian_action` / `divided_difference_operator` "Defer the decision to the harvest that needs it" deferral. Every claim carries a pointer; pointers are in range.

**surface-or-evidence — pass.** This is a `new:` theme file, not a refinement of existing operator/theme text. It both creates surface (the `apply-nonlinear-pencil-mutation-rotation` chapter) and carries the L1→L0 rotation evidence. Not a pure rotation_claim, not a retroactive-evidence backfill — it is a fresh lowering theme with a positive source site. Pass.

**rotation-quality — pass.** The L1 form `apply_nonlinear_pencil(T, λ, v) = T(λ)·v` is strictly more compact/abstract than the L0 forms: the destination buffer, the term-by-term in-place accumulation order, the `A2`-caching across line search, and the build-form choice (term-by-term vs `BuildParSumOperator`-materialize) are all hidden at L1. This is genuine state-hiding / threaded-state compression, not a 1:1 rename. The five L0 sites collapse to one parameterized apply. Pass.

**variant-axis-coverage — pass.** Four axes are accounted for: (1) damping-present — `Maybe C` / `if (opC)` guard, covered (Sub-pattern A); (2) L0-build-form — Form A vs Form B, covered and collapsed by `apply_linop` law 5 (Sub-pattern B); (3) A2-representation — collapsed to the opaque `Real -> LinearOperator` closure, explicitly scoped to L0 (Sub-pattern C + Open questions); (4) purpose/coefficient-vector — residual `{1, λ, λ², 1}` vs Jacobian `{0, 1, 2λ, 1}`, explicitly scoped OUT as an upstream-deferred decision with the `:655` witness cited (not lowered here). No hidden branches. Pass.

**cross-reference-integrity — pass.** All six `[link]` targets in the `new:` body resolve to live files (`nleps-deflated-residual-mutation-rotation.md`, `apply-linop-mutation-rotation.md`, `axpby-mutation-rotation.md`, `axpbypcz-mutation-rotation.md`, `../L1/apply_nonlinear_pencil.md`, `../L1/eigsolve.md` — all confirmed on disk). The new chapter is wired into `SUMMARY.md` by the `edit:` block. Build-readiness guard (firm-body-inside-fence): the firm theme's full apparatus — `## Status` (line 74), `## L1 form`, `## L0 form`, Sub-patterns A/B/C with citations, `## Justification kind`, `## Verified-against` — is entirely ENCLOSED inside the `new:` fence (lines 48–432). The body is NOT authored as the report's own top-level sections outside the fence. No cycle-019 fence-truncation defect. Pass.

**edge-label-fidelity — pass.** Frontmatter `layer: L1>L0`; the "Rewrite — forward (L1 → L0)" section and all prose discuss exactly the L1→L0 lowering of `apply_nonlinear_pencil`. The edge label and the discussed edge match. Pass.

**plan-kind-consistency — pass.** Declared `status: firm`. Content shape is firm: positive source site (`GetResidualNorm`) + four corroborating positive sites, full Status/laws/citations apparatus, no rough-in placeholders, "Speculative L1 operators: None." The firm-on-positive-structure rationale (laws are syntactic identities on a fully-specified read closure; NLEPS test absence does not gate syntactic-identity laws) is the correct application of the `apply_linop`-situation escape, inherited from the operator it lowers (`apply_nonlinear_pencil.md:98`). Kind matches content. Pass.

**skill-uptake-survey — pass.** The report references `verify-citation-range` (the self-verification pass, line 378) and flags the standard `lowering-verifier` `verified_against:` audit as the follow-up. The relevant skill for this shape (citation self-verification) is invoked. Telemetry only; non-blocking. Pass.

### Task-directed spot-checks (all confirmed)

- **Load-bearing ranges re-read on disk:** `:807-821`, the four `BuildParSumOperator` `{1, λ, λ², 1}` sites (`:498-499`, `:557-558`, `:729`, plus the `{0, 1, 2λ, 1}` Jacobian `:655`), and the `A2(|Im λ|)` real-projection sites (`:818` Form A, `:556` Form B, closure type `:177-181`) — all match cited text. No inline-anchor drift detected.
- **High→low authoring:** the theme is defined as "how the L1 form lowers into the L0 form" (LHS = L1, RHS = L0, prose narrates the forward rewrite). Conforms to the layers-defined-high→low invariant.
- **Form-A↔Form-B accumulation-order bit-difference:** correctly recorded as a load-bearing NON-LAW ("algebraically identical but **not bit-identical**", lines 255–260; Applicability conditions 347–350), citing the L1 entry's recorded non-law at `:71`. It is NOT asserted as a bit-level equality. Correct.
- **No speculative operators promoted:** "Speculative L1 operators: None" — the theme composes existing firm `apply_linop` / `axpby` / `axpbypcz` and treats `A2` as an opaque leaf; the `divided_difference_operator` candidate is explicitly deferred to the upstream Jacobian OQ, not promoted here. Confirmed.
- **Fence parity:** 22 top-level fence markers; the `new:` block (48→432) encloses 8 balanced nested `text` fence pairs (16 lines); the two `edit:` blocks (434→437, 439→442) are each balanced. Even parity throughout. Clean.

### Issues found

1. **[cosmetic] Source-comment line citation off by one.** CYCLE.md line 128–129 (inside the Form A code block) and the Sub-pattern A citation list (line 214) attribute the source's own residual statement to `nleps.cpp:810-811`. On disk the comment is two lines, `:809` (`// Compute the i-th eigenpair residual: || P(λ) x ||₂ = ...`) and `:810` (`// for eigenvalue λ.`); line :811 is the blank/`opK->Mult` boundary. The cited content (the residual-equation comment) exists and is correctly described — only the line numbers are shifted by ~1 (`:810-811` should be `:809-810`). Location: CYCLE.md proposed-theme Sub-pattern A citations + the inline code comment at :128. Severity: cosmetic (the comment is real and correctly characterized; the load-bearing code lines :812-820 are all cited correctly). Note the L1 entry (`apply_nonlinear_pencil.md`) does not pin this comment to a line, so there is no carry-forward inconsistency.

2. **[low] SUMMARY.md insertion anchor is shared with the parallel `nleps-deflated-solve` report.** The report's "Integrator note" (CYCLE.md lines 508–513) states "No overlap with the `nleps_deflated_solve` rows." This is accurate at the slug/row level (distinct slugs, distinct content), and the index.md insertions use *different* anchors (this report inserts after `nleps-deflated-residual-mutation-rotation` at index.md line 30; the parallel report inserts after `lu-solve-mutation-rotation` at line 32 — no collision). However, BOTH reports' `edit:book/src/SUMMARY.md` blocks anchor on the SAME line (`lu-solve-mutation-rotation`, SUMMARY.md:99) as the insertion point. This is not a true content overlap — both are distinct, non-conflicting appends under the same Part, and the parallel report (`2026-05-29T105500Z-abstractor-nleps-deflated-solve-rotation`, lines 542–544) explicitly cross-flags it and says "place both" — but the integrator must apply the two SUMMARY.md edits serially against a moving anchor, not treat them as independent line-targeted patches. Location: CYCLE.md `edit:book/src/SUMMARY.md` block (lines 439–442) + Integrator note (508–513). Severity: low (serialization-ordering note for the integrator; both reports already acknowledge the shared file). The "No overlap" phrasing slightly understates the shared SUMMARY.md insertion anchor.

3. **[informational] `eps.hpp:69-74` cited range vs L1 entry's `:57-74`.** The report's Verified-against cites the nonlinear `SetOperators` overload at `eps.hpp:69-74` and re-read it via `read_range 57-74`. On disk lines 69-74 are exactly that overload (`virtual void SetOperators(const ComplexOperator &K, const ComplexOperator &M, std::function<...> A2, ScaleType type)`). The L1 entry it lowers cites the broader `eps.hpp:57-74` (covering the two preceding overloads too). Both are correct for their respective claims (the theme's narrower `:69-74` is the exact nonlinear overload; the L1 entry's `:57-74` covers the overload set). No drift — flagged only because the narrower vs broader range could look inconsistent to a reader cross-checking; it is not. Severity: informational, no action needed.

## Repair

### Fixes attempted

- **Finding**: [cosmetic] Source-comment line citation off by one — critic claims the residual comment cited as `nleps.cpp:810-811` should be `:809-810` (CYCLE.md inline comment at :128 + Sub-pattern A citation list at :214 + Verified-against at :382).
  - **Decision**: not-needed.
  - **Action**: none — verified the cited range is already correct on disk; applying the critic's proposed shift would have *introduced* an error.
  - **Rationale**: Before editing, I re-read the exact range with single-line anchors via `palace-codemap` `read_range` (the off-by-one shape is itself easy to mis-count). Precise reads: `read_range 809-811` returns `{` (:809), `// Compute the i-th eigenpair residual: || P(λ) x ||₂ = ...` (:810), `// for eigenvalue λ.` (:811); `read_range 812-812` returns `opK->Mult(x, r);` (:812); `read_range 820-821` returns `return linalg::Norml2(comm, r);` (:820) and `}` (:821). So the residual comment is at **:810-811** exactly as the report cites, and the load-bearing code at :812-820 lands as cited. The critic's single-line counting drifted by one (it placed `{` at :808 and the comment at :809-810); the report's `:810-811` is the correct on-disk range. **No edit applied** — the citation is already right; the trivial-correction instruction is satisfied by NOT corrupting a correct citation.

- **Finding**: [low / coordination] SUMMARY.md insertion anchor shared with the parallel `nleps-deflated-solve` report — both `edit:book/src/SUMMARY.md` blocks anchor on `lu-solve-mutation-rotation` (SUMMARY.md:99); the report's "No overlap" phrasing slightly understates the shared anchor.
  - **Decision**: not-needed.
  - **Rationale**: The report's Integrator note (CYCLE.md :508-513) already explicitly flags the shared `book/src/SUMMARY.md` + `book/src/L1-L0/index.md` files with the parallel `nleps_deflated_solve` abstractor and states the distinct-slug / non-colliding-anchor situation; the parallel report cross-flags it too. This is a serialization-ordering note for the integrator (apply the two SUMMARY.md appends serially against a moving anchor), not a content overlap and not a repairable defect. No authoring required; the integrator has the flag. Tightening the "No overlap" prose would be a content edit beyond mechanical-repair authority and is unnecessary — both reports already surface the shared file clearly.

- **Finding**: [informational] `eps.hpp:69-74` (theme, narrow nonlinear overload) vs `:57-74` (L1 entry, broader overload set) — both correct for their respective claims.
  - **Decision**: not-needed.
  - **Rationale**: Critic explicitly marked this no-action; both ranges are correct. Nothing to repair.

### Unrepairable findings

None. All three findings resolve to `not-needed` (one was a critic-side mis-count of a citation that is already correct on disk; two were explicitly non-action coordination/informational notes). No finding required substantive authoring or exceeded repair authority.

## Suggested resolution

`ready`. All 8 critic checks pass; no blocking findings. Notes for the integrator:

- **Citation #1 is correct as-is** — the residual comment at `nleps.cpp:810-811` matches disk. Do NOT apply the critic's suggested `:809-810` shift; it would corrupt a correct range. (The critic's off-by-one observation was itself off by one.)
- **Shared SUMMARY.md / index.md anchor** — this report's `edit:book/src/SUMMARY.md` block (append `apply-nonlinear-pencil-mutation-rotation` after `lu-solve-mutation-rotation`, SUMMARY.md:99) and `edit:book/src/L1-L0/index.md` row (after the `nleps-deflated-residual-mutation-rotation` row) share both files with the parallel `2026-05-29T105500Z-abstractor-nleps-deflated-solve-rotation` report. Apply the two reports' SUMMARY.md/index.md edits **serially** against the moving anchor — they are distinct, non-conflicting appends under the same Part, not independent line-targeted patches. Both reports cross-flag this.
