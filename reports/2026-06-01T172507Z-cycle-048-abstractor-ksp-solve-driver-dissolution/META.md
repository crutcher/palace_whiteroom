---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T181500Z
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
repaired_at: 2026-06-01T182500Z
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

# META: verification of L4>L3 theme sketch — ksp-solve-driver-dissolution

## Critique

### Checks run

**citation-validity — pass.** `python3 tools/citecheck/citecheck.py --scan` on the report returns `42 ok, 0 failing (42 citations checked)`. I anchor-verified the load-bearing L0 pinpoints the report itself called out as citecheck-verified, all `[ok]`: `iterative.cpp:427` (anchor `for` → the CG outer-driver guard `for (; it < max_it && !converged; it++)`, confirmed via codemap read), `iterative.cpp:563` (anchor `restart` → the GMRES restart loop `for (; it < max_it; restart++)`, codemap-confirmed), `ksp.cpp:301-307` (anchor `Warning` at :303 → the soft-fail policy: `Mpi::Warning` then return-the-iterate-regardless, with the `ksp_mult`/`ksp_mult_it` counters at :308-309, codemap-confirmed), plus `iterative.cpp:463` (`converged = (res < eps)`), `:484-485` (`final_res`), `iterative.hpp:98` (`GetConverged`). Every L3-parent line range the report cites resolves exactly on disk: `L3/ksp_solve.md:38-54` (signature fold), `:63-70` (four-field result), `:76-80` ("No Solve monad"), `:90` (fold_iterate / restart-boundary), `:94` (restart nesting), `:100-104` (iteration-rotation marker / sequential-obstruction), `:160` (soft-fail axis 4), `:169-173` (substantive L3>L2 hop). The composed-theme citation `krylov-step-typed-wrapper-dissolution.md:158-200` lands on §"What the L3 form for `iterate_while` looks like" (the kernel-half precedent), and the `solve-monad.md:58-68` §"Termination as a sum type" matches the report's three-arm `Outcome` narrative verbatim. No `verified_against:` YAML block is present (the report uses a prose §Verified-against section), so that sub-check is N/A. Clean pass.

**surface-or-evidence — pass.** This is a NEW theme chapter (`new:book/src/L4-L3/ksp-solve-driver-dissolution.md`), not a refinement of existing surface, so the refinement-shaped-proposal branch does not strictly apply. The chapter nonetheless carries full rotation evidence: the four coordinated rewrites are each cited against the firm cap's §Signature/§Semantics/§"Algebraic laws", the firm L3 entry, the `solve-monad` concept, the strawman §3.3-3.4/§3.7/§3.8, and the citecheck-verified L0 anchors. Surface + rotation evidence both present.

**rotation-quality — pass.** This is a genuine substantive L4→L3 rotation, not identity-in-form and not a renaming. The L4 cap (LHS) is strictly more abstract than the L3 driver (RHS): the `Solve = StateT SimState Identity` monad → explicit positional `(K, s)` value-threading (state-hiding removed); the typed `Outcome = Continue | Done Bool` sum classified once at a single decision site → de-classified, scattered into the L3 predicate's two clauses + the restart re-seed + the soft-fail `Bool` `result.converged` (sum-type collapse); the `solve_loop` `do`/`unless` driver → the `iterate_while_L3` outer tail recursion; the once-per-cycle `modify`-correction → the explicit `fold_iterate` boundary write. Each is a coarsening/de-packaging in the L4→L3 direction (the higher form is more compact/equational), which is exactly the rotation-quality criterion. The composition discipline is correct: the theme delegates the inner-fold combinator dissolution to `iterate-while-dissolution` (firm c047) and the per-step body to `krylov-step-typed-wrapper-dissolution` (firm), narrating ONLY the outer-driver + Outcome-classification half. The §"What does NOT change" section correctly fences off the per-cycle dataflow as textually unchanged, and the §"What this lowering does NOT cover" section explicitly scopes out the two delegated halves and the pending L3>L2 hop — so the rotation does not duplicate the sibling themes. The outer-loop `sequential-obstruction` is correctly carried down unchanged. Strong pass.

**variant-axis-coverage — pass.** The driver's variant axes (the firm L3 entry's five loop-shaping axes: krylov-method, element-type, initial-guess-policy, convergence-failure-policy, restart-shape) are handled by reference to the firm L3 parent rather than re-enumerated, which is appropriate for a lowering theme (the theme transports the rotation, not the axis catalogue). The two relevant variant distinctions the rotation actually touches are covered explicitly: restarted vs non-restarted (rewrite 3, Phase 3 — `fold_iterate` is identity for CG/Chebyshev, materialises the last partial restart-cycle for GMRES/FGMRES) and the soft-fail convergence-failure-policy (rewrite 4 — the `Bool` `result.converged`, with the `eigsolve` partial-success arm explicitly scoped OUT as having no `ksp_solve` analog). No hidden branches.

**cross-reference-integrity — warning.** Fence-parity is clean: exactly 6 ``` markers / 3 balanced blocks (`new:` 35-236, `edit:index` 238-241, `edit:SUMMARY` 243-246); the full firm body — `## Status` (line 226), `## Slug`, L4/L3 forms, the four rewrites, §Applicability, §Justification, §Verified-against, §"L4 vs L3 distinction" — sits ENTIRELY INSIDE the `new:` fence, and the L4/L3 pseudocode uses 4-space indented code blocks rather than nested ``` fences, so there is no fence-truncation hazard. SUMMARY insert is surgically correct (new line after the `iterate-while-with-prev-dissolution` line at SUMMARY:19). The index edit correctly appends after the existing last table row (index:19), and I confirmed `L4-L3/index.md` carries NO consolidated firm-count tally — it is a single §Theme list table — so D3 appending only its row is the correct registration shape. All concept references (`solve-monad`, `sequential-obstruction`, `convergence-test`, `derived-view-hoisting`) resolve on disk; the two delegated sibling themes (`iterate-while-dissolution.md`, `krylov-step-typed-wrapper-dissolution.md`) and the L3 parent (`L3/ksp_solve.md`) all resolve. The `warning` is driven by two cross-report wiring items, both already self-flagged by the report (§Context line 46, §"Open questions" line 263): **(i)** the same-cycle live links `[ksp_solve](../L4/ksp_solve.md)` and `[krylov-step](../L4/krylov-step.md)`→`../L4/iterate-while.md` — `L4/ksp_solve.md` is NOT yet on disk (it is D1's wave-1 create); this is a legitimate same-cycle forward-reference per the c047 D2→D1 precedent and resolves once D1's create lands before the single finalize build, but the integrator must order D1 before this report's finalize-build (the dead link is a hard `linkcheck2` error if D1 fails to land). **(ii)** the cross-report SLUG MISMATCH: D1's cap references this theme as `ksp-solve-outer-driver-dissolution`, but it landed as `ksp-solve-driver-dissolution`. The integrator must re-wire D1's cap's two in-line references (§"Lowers to" + the dep-map "Lowers to" cell) plus D1's §"Open questions" slug-mismatch note to the landed slug. The theme's OWN slug is internally consistent (`## Slug` line 42, filename, SUMMARY line, and index row all read `ksp-solve-driver-dissolution`). Neither item is a defect in THIS report — both are correctly surfaced co-wiring instructions for the integrator — hence `warning` not `fail`.

**edge-label-fidelity — pass.** The edge label is L4→L3 throughout: the index dep-map row's LHS is `L4 [ksp_solve] outer-driver cap`, RHS is `L3 [ksp_solve] value-threaded outer-driver fold`, justification `structural + secondary reduction-chain`; the prose, the §"Abstraction-direction note" (line 184), and §"L4 vs L3 distinction" (lines 230-235) all narrate the L4→L3 direction consistently. The dep-map row points L4>L3 at the correct theme/operators (`L4/ksp_solve` → `L3/ksp_solve`, with the `Solve`-monad/`Outcome`/`solve_loop`/`restart_cycle` machinery on the LHS and the positional-`(K,s)`/`iterate_while_L3`/`fold_iterate`/soft-fail-`Bool` images on the RHS). No edge-label drift.

**plan-kind-consistency — pass.** Declared kind is a `firm` L4>L3 theme (§Status line 228, index row Status cell). The content shape matches: a complete dissolution narrative with LHS form, RHS form, four exhaustively-cited coordinated rewrites, applicability conditions, justification kind, and full verified-against — no rough-in placeholders, no unresolved TODOs. The `firm` claim is supported because the theme lowers an already-firm cap into an already-firm L3 target using already-firm sibling themes; nothing constructive or test-gated is asserted. The one structural caveat — the L4 cap LHS is not yet on disk (same-cycle sibling) — is a wiring-ordering matter, not a maturity gap in the theme's content. Correct classification.

**skill-uptake-survey — pass.** The report references `summary-md-surgical-insert` (the SUMMARY-line shape, §Registration item 2) and `citecheck` (the L0-anchor verification, §Supporting evidence). The build-readiness fence-parity discipline (`proposed-changes-fence-encloses-full-body-guard`) is the critic-side guard, not a producer obligation. No missing skill-invocation is implied by the report's shape. Telemetry-only; pass.

### Issues found

1. **(cross-reference-integrity, warning) Cross-report slug mismatch requiring integrator re-wiring.** `CYCLE.md` §Context (line 46) + §"Open questions" (line 263). D1's firm cap (`book/src/L4/ksp_solve.md`, not yet on disk) names the pending L4>L3 theme with the working slug `ksp-solve-outer-driver-dissolution`; this dispatch lands `ksp-solve-driver-dissolution`. The integrator must reconcile D1's cap's two in-line references (§"Lowers to" + dep-map "Lowers to" cell) and D1's §"Open questions" slug-note from the working slug to the landed slug. Self-flagged by the report with an explicit co-wiring instruction; non-blocking for THIS report's own internal consistency (this theme's own slug is uniform across filename/`## Slug`/SUMMARY/index).

2. **(cross-reference-integrity, warning) Same-cycle forward-reference live link to not-yet-on-disk cap.** `CYCLE.md` line 38 (and throughout) + §"Open questions" (line 263). The live link `[ksp_solve](../L4/ksp_solve.md)` targets D1's wave-1 create, which is absent on disk at critique time (confirmed: `ls book/src/L4/ksp_solve.md` → No such file). This is a legitimate same-cycle forward-reference per the c047 D2→D1 precedent and resolves at integration IF D1's create lands before the single finalize build. Integrator dependency: D1 must be applied before this report's finalize-build, else the link is a hard `linkcheck2` error. No plain-text defang is warranted (both files land the same cycle); the note is a sequencing reminder, not a content defect.

3. **(informational, no severity) L0 anchor `iterative.cpp:417-418` and `:703-704` not independently re-anchored.** §Verified-against (lines 208, 213). The report claims the full L0 anchor set is "transitive through the firm L3 driver, which already carries the citecheck-verified provenance." citecheck `--scan` confirms all 42 ranges are in-bounds and path-clean; I spot-anchored the six load-bearing pinpoints (all `[ok]`) but did not re-anchor `:417-418` (eps formula) or `:703-704` (GMRES `final_res = beta`). The L3 parent (`L3/ksp_solve.md:72,90,92`) carries these exact anchors as pre-verified firm provenance, so the transitive claim is sound; noting only that these two were taken on the L3 parent's verified record rather than independently re-anchored this critique.

## Repair

### Fixes attempted

The single `warning` (cross-reference-integrity) is driven by **two cross-report co-wiring items**, both already self-flagged by the report and both confirmed by the critic to be NOT defects in THIS report. Neither is a repairable-in-D3 defect: both belong to D1's repair / the integrator. D3's own content is sound and internally consistent. No edits to D3's CYCLE.md or supporting docs were required.

- **Finding 1 — Cross-report slug mismatch.** D1's cap references this theme as `ksp-solve-outer-driver-dissolution`; this report lands the **canonical** slug `ksp-solve-driver-dissolution` (matches the cycle-048 plan and the firm sibling naming `krylov-step-typed-wrapper-dissolution` / `iterate-while-dissolution`).
  - **Decision**: not-needed (in D3).
  - **Verification performed**: grepped both slug variants across D3's CYCLE.md. D3's OWN slug is uniform `ksp-solve-driver-dissolution` at every registration site — the `new:` file path (line 35), `## Slug` (line 42), the `L4-L3/index.md` row link (line 240), and the SUMMARY line (line 245). The only two occurrences of `ksp-solve-outer-driver-dissolution` (lines 46 §Context, 263 §"Open questions") are intentional, backtick-quoted references to **D1's working slug** as part of D3's self-flagged co-wiring note — not stray uses of the wrong slug for this theme. D3 is internally consistent; no edit needed.
  - **Owner**: D1's repairer / integrator re-wires D1's 6 references (D1 cap §"Lowers to" + dep-map "Lowers to" cell + §"Open questions" slug-note) from the working slug `ksp-solve-outer-driver-dissolution` to D3's canonical `ksp-solve-driver-dissolution`. Cross-reference: see the D1 report's repair section (`reports/<...>-harvester-L4-ksp-solve-cap/META.md`).

- **Finding 2 — Same-cycle live link to not-yet-on-disk cap.** The chapter links D1's wave-1 create `[ksp_solve](../L4/ksp_solve.md)` (and `[krylov-step](../L4/krylov-step.md)` → `../L4/iterate-while.md`), which is absent on disk at critique time.
  - **Decision**: not-needed (KEEP the live link, do NOT defang).
  - **Rationale**: legitimate same-cycle forward-reference per the c047 D2→D1 precedent; both files land the same cycle. Plain-text defang is the fallback only when the target is speculative, which is not the case here.
  - **INTEGRATOR-ORDERING NOTE**: D1's `L4/ksp_solve.md` create must be applied **before** this report at integration, so the live link resolves at the single finalize `linkcheck2` build. If D1 fails to land, the link is a hard `linkcheck2` error. This is a sequencing reminder, not a content defect.

### Unrepairable findings

None. The single warning carries no D3-side defect to repair — both items are correctly-surfaced cross-report co-wiring instructions owned by D1's repair and the integrator's ordering/re-wire step. (Critic informational item 3 is a transitive-anchor telemetry note, no action.)

## Suggested resolution

`overall_status: ready`. D3's content is sound and internally consistent — all 8 checks pass or carry only cross-report co-wiring warnings with no D3-side defect. Integrator notes:

1. **Order D1 before D3 at integration** so the `[ksp_solve](../L4/ksp_solve.md)` live link resolves at the single finalize build (same-cycle forward-reference; KEEP the live link).
2. **The slug re-wire is D1's**, not D3's — D1's 6 references to `ksp-solve-outer-driver-dissolution` reconcile to D3's canonical `ksp-solve-driver-dissolution` (handled in D1's repair).
3. SUMMARY insert and `L4-L3/index.md` row append are surgically correct; the index carries no consolidated tally, so D3 correctly appends only its row.
