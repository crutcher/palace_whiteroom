---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T01:29:43Z
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
repaired_at: 2026-06-02T01:33:27Z
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

# META: verification of cycle-055 D1 — Formalize solve_family at L4

## Critique

### Checks run

**citation-validity — pass.** All 14 L0 anchors re-read against on-disk Palace source via codemap `read_range`; every one lands exact. Electrostatic (`palace/drivers/electrostaticsolver.cpp`): `:30` `auto K = laplace_op.GetStiffnessMatrix()`, `:35` `KspSolver ksp(...)`, `:36` `ksp.SetOperators(*K,*K)`, `:42` `MFEM_VERIFY(n_step > 0,…)`, `:46` `std::vector<Vector> V(n_step)`, `:60` `for (… : laplace_op.GetSources())`, `:68` `GetExcitationVector(idx, *K, V[step], RHS)`, `:69` `ksp.Mult(RHS, V[step])`, `:89` `step++` — all exact. Magnetostatic (`magnetostaticsolver.cpp`): `:30`/`:35`/`:36` same shape, `:42-43` `MFEM_VERIFY(n_step > 0,` + message (the report's `:42-43` span is correct), `:47` `std::vector<Vector> A(n_step)`, `:66` `for (… : curlcurl_op.GetSurfaceCurrentOp())`, `:76` `GetExcitationVector(idx, RHS)`, `:77` `ksp.Mult(RHS, A[step])`, `:99` `step++` — all exact. Driven scope-boundary witness (`drivensolver.cpp`): `:168` frequency loop `for (std::size_t omega_i = …)`, `:176` `auto A = space_op.GetSystemMatrix(1.0 + 0.0i, 1i * omega, …)` (operator rebuilt per-ω INSIDE the loop), `:180` `ksp.SetOperators(*A, *P)` (inside the loop) — all exact. Firm-vocabulary grounding into `L4/ksp_solve.md` (`:17`, `:38-40`, `:61`, `:62`, `:98`, `:100`, `:111`, `:114`, `:116`, `:153`) all verify; strawman `l4_calculus.md` `:150-184` (§3.7), `:178-182` (`iterate_while_pure` sugar), `:186-228` (§3.8 pruning) verify; `L4/index.md` `:7`/`:13`/`:37`/`:47` verify. The report's self-claim of "zero drift" holds.

**surface-or-evidence — pass.** This is a `new:` operator chapter (a fresh L4 combinator firm-up), not a refinement of existing operator/theme surface, so the refinement-surface rotation_claim gate does not apply in its modify-existing-surface form. It does carry the index `:76` row flip (existing-surface modification) — and that modification is paired with the substantive evidence (the 14 L0 anchors + the firm-vocabulary grounding) authored in the same report. No pure unsupported rotation-claim. Not the retroactive-backfill shape either; this is forward-frontier authoring with evidence in hand.

**rotation-quality — pass.** The §Lowers-to records an L4→L3 rotation (`map` combinator → L3 explicit `std::vector<Vector>`-accumulating positional `for`-loop with the operator-construction hoisted outside) and explicitly labels it **substantive (not identity-in-form)**: the `map` collapses to a positional loop, the once-captured `op` becomes the `SetOperators`-outside-the-`for` placement, the pure-map trajectory becomes the positional `V[step]`/`A[step]` collection. This is genuine compression at L4 (the in-layer combinator names the operator-capture-once stratification that the L3 sweep leaves as a coding convention), and the lowering is a real vocabulary shift, not a 1:1 rename. The combinator-as-entry framing (the entry IS the `map (ksp_solve op)`, the leaves are absorbed) is itself the in-layer abstraction the redirect calls for. The theme itself is correctly NOT authored here (deferred to dispatch #2), so only the rotation *direction* is recorded — appropriate.

**variant-axis-coverage — pass.** Four axes declared (§Variant axes): operator-capture (`fixed | per-element`) is the load-bearing scope boundary and is explicitly handled — `fixed` is this combinator, `per-element` is scoped OUT to the batch-17 superset with the driven witness (`drivensolver.cpp:176-180`) named as the boundary case. family-index-domain, element-type, and collection-shape are each declared **absorbed** (into `[Inputs]` / `OpParams` / lowering concern) with rationale. No hidden branch: the driven per-ω-rebuild case that would otherwise be a silent miss is explicitly surfaced as the not-an-instance scope boundary in both §Variant-axes, §Algebraic-laws (non-law 2), and §Status scope caveat. The report does not over-claim past the 2 fixed-operator witnesses (electrostatic + magnetostatic), correctly flags transient/eigenmode as unprobed, and gates the superset to batch-17 (OQ filed).

**cross-reference-integrity — pass.** All in-body markdown links resolve to existing files: `./ksp_solve.md`, `./iterate-while.md`, `./chebyshev.md`, `./krylov-step.md`, `../concepts/{state-stratification,solve-monad,derived-view-hoisting,variant-absorption}.md` — all confirmed on disk. The two forward-referenced not-yet-existing targets (`L4-L3/solve-family-map-dissolution.md` and `L3/solve_family.md`, both batch-17/dispatch-#2 pending) are correctly kept as **plain-text inline-code** (not live `[](...)` links) in the dep-map "Lowers to" cell and in the `lowers_to:` YAML frontmatter, per the `rough-in-forward-reference-must-be-plain-text-not-live-link` convention — so no dead-link build break. The canonical slug `solve-family-map-dissolution` is used consistently across §Lowers-to, §Status, the dep-map cell, and the frontmatter. Build-readiness fence guard: the `new:` chapter body (report lines 26–197) encloses the full apparatus — `## Status` (line 168), Signature, Algebraic-laws, Evidence are all INSIDE the fence; the Haskell signatures use 4-space indented code (lines 65–80), no nested ` ``` ` fences, so no fence-truncation risk. The SUMMARY.md insertion (`- [solve_family](./L4/solve_family.md)` after line 13) lands correctly inside the L4 Part (line 13 is the last L4 entry before the `# L4 > L3` Part header at line 15).

**edge-label-fidelity — pass.** The only edge label in play is the L4→L3 lowering (`solve-family-map-dissolution`, L4>L3). The §Lowers-to and §Status prose discuss exactly that edge (L4 map combinator → L3 explicit accumulating loop), narrated forward L4→L3 per high→low discipline. No mislabeled edge.

**plan-kind-consistency — pass (with a noted tension; see Issues).** Declared kind is `rough-in (test-coverage-bounded)` — a first-class qualifier per CLAUDE.md. The content shape matches: the structural signature is well-anchored at L0 (two structurally-identical witnesses), and the algebraic laws are stated-but-test-unconfirmed because the drivers are integration-level (no `test-*.cpp` exercising the outer sweep). This is the textbook `rough-in (test-coverage-bounded)` situation, distinct from `partly-constructive` (correctly noted). The report is also transparent about the firm-on-positive-structure tension (the apply_linop escape) and resolves it conservatively with a named residual + OQ — see Issues for the one observation.

**skill-uptake-survey — pass (telemetry).** The report's shape (citation-heavy L4 firm-up, fence-enclosed proposed-changes, rough-in forward-references) implicates `verify-citation-range`/`citecheck`, `proposed-changes-fence-encloses-full-body-guard`, and `verify-rotation-citation`. The report self-reports manual `sed -n` anchor verification of all 14 L0 anchors but does not reference invoking `tools/citecheck/` or the fence guard skill by name. This is a producer-side telemetry note only (non-blocking) — the anchors independently verify exact regardless.

### Issues found

1. **(low / observation) Status sits in a genuine firm-on-positive-structure tension** — `book/src/L4/solve_family.md` §Status (report line 170) + §Open-questions (report line 239). The report's own analysis concedes that law 1 (concatenation-homomorphism) IS a syntactic `map` identity and law 2 (the `SetOperators`-hoist) IS read directly off positive source — both of which point toward the `firm` classification under the CLAUDE.md "firm-on-positive-structure escape" (the `apply_linop` situation, where syntactic-identity laws are not gated by a missing test). The report chooses the conservative `rough-in (test-coverage-bounded)` on the grounds that the *independence* claim — that `KspSolver ksp` reuse (constructed once at `:35`, `ksp.Mult` called per-element at `:69`/`:77`) carries no hidden cross-element mutable state — is the one part not confirmable from driver source alone. This residual is real and named, the conservative choice is defensible, and the report files OQ `solve-family-status-firm-on-positive-structure-vs-test-coverage-bounded` (batch-17) + defers promotion to a lowering-verifier `KspSolver`-statefulness pass. Surfaced as an observation, not a defect: a reviewer/integrator may reasonably take the firm-on-positive-structure escape now, but the report's deferral is within bounds. No repair required.

2. **(informational) `RHS` buffer is a single reused `Vector` across the sweep** — §Specializations / §Algebraic-laws (law 3, report lines 118, 133, 135). The witnesses declare `Vector RHS(...)` once (electrostatic `:45`, magnetostatic `:46`) and overwrite it each iteration via `GetExcitationVector`. The report's law 3 (element-independence / order-preservation / commutativity) is algebraically sound because each `ksp.Mult` writes into its own slot (`V[step]`/`A[step]`) and `RHS` is fully recomputed per index before each solve — so the shared buffer is a sequential coding artifact, not a cross-element data dependency. The report does not mislead here (it correctly attributes independence to the per-element fresh RHS + own-slot write). Flagging only because the shared-`RHS`-buffer detail is exactly the kind of thing the batch-17 `KspSolver`-statefulness lowering-verifier pass should also confirm carries no aliasing hazard at L3 lowering time. No repair required.

3. **(informational) skill-invocation not referenced by name** — report §Summary line 22 + §Supporting-evidence line 235. The report self-reports manual `sed -n` exact-line anchor verification but does not name `tools/citecheck/` or `verify-citation-range`/`proposed-changes-fence-encloses-full-body-guard`. Telemetry only; all anchors and fence parity independently verified clean here.

## Repair

### Fixes attempted

All 8 critic checks landed `pass`. No warning/fail findings exist; the three Issues are explicitly `(low / observation)` / `(informational)` and the critic states "No repair required" on each. No mechanical or surgical edits were applicable.

- **Finding**: Status sits in a genuine firm-on-positive-structure tension (Issue 1) — `rough-in (test-coverage-bounded)` chosen over `firm` on the named residual (KspSolver-reuse cross-element statefulness not confirmable from driver source alone).
  - **Decision**: not-needed
  - **Rationale (accepted)**: This is a content classification decision, not a mechanical defect. The conservative choice is defensible (a real named residual + filed OQ `solve-family-status-firm-on-positive-structure-vs-test-coverage-bounded` + batch-17 lowering-verifier deferral). Re-classifying to `firm` would be a substantive authoring/content call — out of repair scope. Accepted as-is.

- **Finding**: Shared single `RHS` buffer reused across the sweep (Issue 2) — flagged as a sequential coding artifact (not a cross-element dependency) for the batch-17 lowering-verifier to confirm carries no aliasing hazard at L3.
  - **Decision**: not-needed
  - **Rationale (accepted)**: The report's law 3 is algebraically sound (per-element fresh RHS + own-slot `V[step]`/`A[step]` write); the critic confirms no mislead. This is a forward note to the batch-17 lowering-verifier, not a present defect. Accepted as-is.

- **Finding**: skill-invocation telemetry not referenced by name (Issue 3) — manual `sed -n` anchor verification reported instead of `tools/citecheck/` / named guard skills.
  - **Decision**: not-needed
  - **Rationale (accepted)**: Producer-side telemetry only; all anchors and fence parity independently verified clean by the critic. No content or build impact. Accepted as-is.

### Unrepairable findings

None. No finding requires deferral; all observations are accepted-as-is within the producer's bounds.

## Suggested resolution

`overall_status: ready` — clean headline deliverable, all 8 checks pass.

Notes for the integrator:

- **D1 proposed-changes**: `new:book/src/L4/solve_family.md` (status `rough-in (test-coverage-bounded)`) + `edit:book/src/L4/index.md` (flip the `:76` row to a live link + add own-cohort bullet) + `edit:book/src/SUMMARY.md` (insert `- [solve_family](./L4/solve_family.md)` after line 13, inside the L4 Part before the `# L4 > L3` header at line 15).
- **Tally ownership**: the consolidated count tally — including the `index.md:47` Rough-in-at-L4 `0→1` flip — belongs to **D7** (the consolidating dispatch), NOT D1. Do not apply the `:47` flip from this report.
- **Promote D1's OQs**: (1) `solve-family-status-firm-on-positive-structure-vs-test-coverage-bounded` — routed to the batch-17 lowering-verifier (KspSolver-statefulness / RHS-buffer-aliasing pass that can promote the status; Issues 1 + 2 both feed this). (2) the `map_solve` superset OQ (per-element operator-capture variant, driven `drivensolver.cpp:176-180` as the witness boundary case) — gated to batch-17.
- Forward-references `L4-L3/solve-family-map-dissolution.md` and `L3/solve_family.md` are correctly plain-text (dispatch-#2 / batch-17 pending) — do not create live links until those land.
