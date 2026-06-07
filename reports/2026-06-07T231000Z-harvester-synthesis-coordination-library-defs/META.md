---
verifies: ../REPORT.md
critiqued_at: 2026-06-07T233000Z
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
repaired_at: 2026-06-07T234500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: repaired
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Render the `coordination` library def bodies at Synthesis"

## Critique

### Checks run

**citation-validity — pass.** Every supporting-evidence pointer was checked on disk and is in-range and substantively correct. `book/src/L4/eigsolve.md` is 209 lines; the cited `:43-63` (signature block + opaque `eigen_iterate` + `EigStatus`/`EigOutcome`), `:70` (the `EigState` stratum: `pairs`/`converged`/`requested`/`error`/`EigStatus`), `:111` (the `apply_shift_invert` body-composition identity law), `:204` (`EPSSolve(eps)` opaque-call anchor) all resolve and back the claims. `book/src/L4/ksp_solve.md` (205 lines) `:56-57`/`:60-73`/`:98-101` match the rendered `ksp_solve` cap, `solve_loop`, `restart_cycle`, and `Outcome` exactly. `solve_family.md:52-53`, `fold_solve.md:49-50`/`:54`/`:94`, `frequency_sweep.md:105-109`, and `preconditioning-framework.md:171-176`/`:183-188`/`:251-258` all match the rendered bodies near-verbatim. The `concepts/solve-monad.md` (`:14-22` `Solve`/`execState`, `:66-76` Outcome) and `concepts/eigsolve.md`/`L1/eigsolve.md` (EigResult home) pointers resolve. No drift found.

**surface-or-evidence — pass (adapted for Synthesis implementation-rendering kind).** This is the Synthesis implementation VIEW — it renders code forms and links to the authoritative L4 chapters for laws/semantics rather than restating them; the evidence shape is the per-def `reference`-class back-link to the firm L4 chapter, which is present on every rendered def. The record-definition sub-check: the signatures name `EigState`, `SolveResult`, `SimState`, `OpParams`, `Inputs`, `Outcome`/`EigOutcome`. `SimState`/`OpParams` are routed to `types`/their concept homes; `Outcome`/`EigOutcome`/`Solve` get in-chapter utility-API type blocks (correct for a coordination-clustering carrier). `EigState` gets an in-chapter type block with a back-link to its authoritative `EigResult` schema home — verified that home genuinely exists (`L1/eigsolve.md:45` `EigResult[N, K_max] = {...}` and `concepts/eigsolve.md:44-48`), so the resolution is sound and not an evasion of the record-definition obligation. See Issue 2 on the `SolveResult` naming.

**rotation-quality — pass (no-op for this kind).** A Synthesis library chapter rotates nothing — it recomposes already-firm L4 vocabulary into a synthesized code rendering. Not applicable, marked pass per the feature-surface/implementation-rendering precedent.

**variant-axis-coverage — pass.** The rendered defs surface their variant axes by prose pointer to the owning L4 chapter (e.g. `ksp_solve`'s restart-shape note "or: one_cycle … for non-restarted solvers", `fold_solve`'s `schedule-source` fixed-list-vs-state-generated axis, `eigsolve`'s problem-type/spectral-transform axes absorbed into `OpParams`). No hidden branch is rendered as if it were the only one; the state-generated `fold_solve` form is explicitly scoped out with a pointer to the L4 chapter (report OQ confirms this matches the chapter's own treatment). Pass.

**cross-reference-integrity — pass.** All `../L4/<op>.md` back-links resolve to real firm chapters. The sibling `./iteration.md` / `./data-algebra.md` / `./types.md` / `./index.md` Synthesis links and `synthesis/coordination.md` itself do not yet exist on disk — but this is correct: the report MERGES-WITH the same-cycle layer-intro-author shell dispatch that creates them, and the `[old]` block matches that shell's stub content. The integrator applies the shell first. The `concepts/solve-monad.md` / `concepts/solve-result.md` / `concepts/eigsolve.md` / `L1/eigsolve.md` cross-refs all resolve. The report's own OQ flags the `krylov_step` forward-ref-vs-sibling-slug reconciliation honestly. No broken resolvable link.

**edge-label-fidelity — pass.** The report asserts `reference`-class links only with no new `depends-on` edges, and the `#extern` callouts (`eigen_iterate` = SLEPc EPS loop, `time_step_op` = MFEM ODESolver step) are correctly framed as kernel-API boundaries, NOT manufactured as `depends-on` edges to the opaque kernels (the `realizes-kernel-api` correspondence is correctly attributed to the not-yet-standing `eigsolve-impl` impl node, owned there, not here). This matches the directive's kernel-API/impl mechanics. The `eigsolve-impl` deep-link-not-inline decision is correct: it is a separate kernel-impl REALIZATION, not a deep-linked-unchanged lowering of the opaque API, so the "render unchanged artifacts inline" rule does not pull it in.

**plan-kind-consistency — pass.** Content shape matches the implementation-rendering kind: concrete def bodies in the L4 pseudo-language, code-doc `# Arguments`/`# Returns` per def, topological order (type block → construction framework → caps → map/fold combinators), `#extern` after type sigs, `where`-clause helpers. The `stub`→`seed` status flip is consistent with the directive's chapter-KIND (navigational-container, reference-edges only, no rank claim); the report flags it for reconciliation since the directive does not pin a token. Reasonable.

**skill-uptake-survey — pass (telemetry only).** No specific skill is implied for Synthesis def-rendering. The KaTeX `$`-sigil-fence rule was correctly applied (verified: the only def-body `$S` occurrence, `Tensor[$S]` in `apply_shift_invert`, sits inside a ` ```text ` fence at report `:267-296`; all other `$` mentions are prose about the rule). Closure-signature §1.3.1 + named-shape-group §1.2.1 conventions were correctly consulted and exist on disk. Pass.

### Issues found

1. **`eigsolve` entry diverges from the L4 chapter body: `initial_eig_state inp` vs `initial_state inp`** (CYCLE.md §`eigsolve`, report `:274`; L4 `book/src/L4/eigsolve.md:44`). The authoritative L4 chapter renders `eigsolve op inp = execState (solve_loop op inp) (initial_state inp)`; the Synthesis rendering uses `initial_eig_state inp`. As an *implementation VIEW* whose correspondence to the L4 body is reviewable, this is a literal divergence. It is arguably *more* correct (the eigsolve threads `Solve a = StateT EigState Identity a`, so an `EigState`-seeding function is the right thing, and the L4 chapter's reuse of `initial_state` for the EigState-threaded cap is a latent inconsistency in the L4 chapter itself). Severity: low / informational — flag for the `lowering-verifier` correspondence audit and possibly an upstream L4-chapter fix; not a fidelity error per se, but the divergence should be deliberate-and-noted, not silent. The report's own narrative does not call out that this seed-name differs from the rendered L4 source.

2. **The `SolveResult` type-block name does not match its authoritative home's record name** (CYCLE.md §"Coordination type block" → `### `SolveResult``, report `:164-179`). The block renders `type SolveResult = { sim, krylov, outputs }` and back-links `concepts/solve-result.md` as the authoritative schema — but that page (whose *slug* is `solve-result`) names the record `StepReturn` (`StepReturn = Solve { sim, krylov, outputs }`) and `StepReturnB` (the carry-bearing Form B), at `concepts/solve-result.md:31`/`:34`. The name `SolveResult` appears nowhere in the authoritative concept page. So the rendered type invents a name that does not correspond to the home it links. Severity: low-to-moderate — a code-rendering fidelity divergence (a reader following the back-link finds a differently-named record). The report's prose does acknowledge "Form A; Form B adds a `carry` field", correctly distinguishing the two forms, but the type *name* is the mismatch. Repair candidate: rename the block to `StepReturn` (matching the home) or note the alias explicitly.

3. **(Minor / forward-ref, already self-flagged) inner `iteration`-library identifiers rendered as plain tokens** (`krylov_step`, `iterate_while`, `fresh_krylov`, `applyBasis`, `Krylov`, `StepOutputs`). The report transparently flags this in its OQ (forward-refs to the sibling Wave-2 `iteration` library; underscore form chosen to match the L4 calculus identifier convention vs the L4 chapter's hyphenated chapter slug `krylov-step`). Not a defect — surfaced for completeness so the integrator reconciles the canonical rendered-def slug if the abstractor's differs. No action required of this report.

## Repair

### Fixes attempted

- **Finding 1**: `eigsolve` renders `initial_eig_state inp`, diverging silently from the L4 chapter's `initial_state inp` (`book/src/L4/eigsolve.md:44`).
  - **Decision**: repaired (made the divergence deliberate-and-noted).
  - **Action**: CYCLE.md §`eigsolve` def body — added a one-line `-- NOTE:` above `eigsolve op inp = execState (...) (initial_eig_state inp)` explaining the seed is the eigen-specific `EigState` constructor (already defined in the chapter's type block at `initial_eig_state :: Inputs -> EigState`), that this is the correct discharge for the `StateT EigState Identity` threading, and that the L4 chapter's reuse of `initial_state` for the EigState-threaded cap is a latent upstream inconsistency to reconcile (lowering-verifier). I did NOT change the rendered identifier to `initial_state`: the render is internally consistent with its own utility-API block (which defines `initial_eig_state`, not `initial_state`), and the critic judged the eigen-specific name *more* correct — so the surgical fix is to remove the *silence*, not to introduce a name that contradicts the chapter's own type block. Mechanical (one-line note), no authoring.
  - **Rationale**: this is the critic's offered "add a one-line note justifying the eigen-specific constructor name" branch, which the critic itself verified is the defensible reading.

- **Finding 2**: the `SolveResult` type block invents a name absent from its linked home, which authoritatively names the record `StepReturn` / `StepReturnB` (`concepts/solve-result.md:31`/`:34`).
  - **Decision**: repaired (align-to-authoritative-name, per link-don't-restate).
  - **Action**: CYCLE.md §"Coordination type block" — renamed the rendered type block `type SolveResult = {...}` → `type StepReturn = {...}`, renamed the section heading `### \`SolveResult\`` → `### \`StepReturn\``, retargeted the utility-API line `residual_proxy :: SolveResult -> Scalar` → `... StepReturn -> Scalar`, and updated the def-body comment to name `StepReturnB` as Form B. Updated the three internal prose references to match (the type-block operator-list bullet line 76→`StepReturn`; the clustering-types narrative line 86→`StepReturn`; the Summary line 27 + Supporting-evidence line 406 → `StepReturn`). The `[old]` matcher block's verbatim shell prose (which mentions `SolveResult`) was left UNTOUCHED so the integrator's `[old]`-match still applies cleanly; the `[new]` body is fully consistent under `StepReturn`. Mechanical rename, no schema authoring.
  - **Rationale**: this is the critic's "rename the block to `StepReturn` (matching the home)" branch — a pure name alignment to the authoritative concept page, no field-semantics change.

- **Finding 3 (Minor / forward-ref)**: inner `iteration`-library identifiers rendered as plain tokens.
  - **Decision**: not-needed.
  - **Rationale**: the critic explicitly marked "No action required of this report"; the report self-flags the forward-ref slug-reconciliation in its OQ for the integrator. Nothing to repair.

### Unrepairable findings

None. Both substantive findings (1, 2) were low-severity code-rendering fidelity divergences fixable by mechanical note/rename within repair authority; finding 3 needs no action.

## Suggested resolution

`ready`. All 8 critic checks passed; the two flagged fidelity divergences are repaired surgically. Integrator notes:
- The `[old]`/`[new]` edit block is intact — the `[old]` matcher was not modified, so the proposed-change application is unaffected; the `[new]` body now renders `StepReturn` consistently and carries the `initial_eig_state` divergence note.
- Per the report's own OQ (untouched), the integrator should still reconcile the rendered inner-kernel slug (`krylov_step` underscore vs `krylov-step` hyphen) against the sibling Wave-2 `iteration` library when both land.
- The `initial_eig_state` vs L4-chapter `initial_state` divergence note routes a follow-up to `lowering-verifier` (correspondence audit) / a possible upstream `book/src/L4/eigsolve.md:44` fix — flagged in-line, not blocking this report.
