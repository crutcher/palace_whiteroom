---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T08:35:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-27T09:05:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: null
---

# META: verification of L0 reference-notes bootstrap, bundle 2

## Critique

### Checks run

**citation-validity — pass.** Sampled 8 load-bearing citations against Palace source: `operator.hpp:21` (`using Operator = mfem::Operator;`), `operator.hpp:24-68` (`ComplexOperator` class with pure-virtual `Mult` at 54, non-pure `MultTranspose` at 56, `MultHermitianTranspose` at 58, `AddMult` family at 60-67), `operator.hpp:36-39` (Height/Width accessors), `operator.hpp:178-226` (`BaseProductOperator`) with the inline Mult body at 202-206 exactly `B.Mult(x, z); A.Mult(z, y)`, `ksp.cpp:272` (the load-bearing `SetPreconditioner` wiring line), `ksp.cpp:265-274` (move-in constructor), `ksp.cpp:296-310` (`Mult` body — `BlockTimer`, `ksp->Mult`, convergence-warning, counter-increments — all match), and `solver.hpp:21-65` (the `Solver<OperType> : public OperType` declaration at line 22 supports the report's "Solver is-an Operator" claim). Also spot-checked `iterative.cpp:379` (`A->Mult(x, r)`), `:443` (`A->Mult(p, z)`), `:389` (`ApplyB`), `:627` (`ApplyBA`), `rap.cpp:195`/`:236`/`:481` (function entry points), and `iterative.hpp:25-115` (`IterativeSolver` base class ends at line 115). All sampled citations point at the claimed content. The two ranges the agent self-flagged in Open Question #2 (`rap.cpp:236-275`, `operator.cpp:478-503`) were spot-checked and both contain the cited functions; the chapter does not make line-specific claims about their bodies that go beyond function-presence + one-line interpretation. One minor inexactness: `operator.cpp:478-503` is cited as containing "`BaseDiagonalOperator<Operator>::Mult` + `BaseDiagonalOperator<ComplexOperator>::Mult` definitions" — both are present (real at 478-487, complex at 489-507), but the cited range truncates the complex specialisation by ~4 lines. Non-load-bearing inexactness.

**surface-or-evidence — pass.** This is a layer-intro / reference-note dispatch — the proposal IS new surface (two new L0 chapters + index update + SUMMARY.md registration). Not a refinement-shaped proposal, so the surface-or-evidence rule (which targets rotation_claims on existing operators/themes) is satisfied by virtue of being a net-new-surface proposal.

**rotation-quality — pass.** Not applicable to L0 reference-note dispatch. L0 chapters do not assert layer-to-layer rotations; they anchor higher-layer rotations to concrete L0 surface. The two new chapters describe L0 surfaces (the `Mult` overload family + the `BaseKspSolver` composition class) and forward-reference the L1 / L2 / L4 entries that rotate over them — but they do not themselves *make* rotation claims.

**variant-axis-coverage — pass.** The `apply-linop-overload-set.md` chapter explicitly enumerates three orthogonal sub-axes (transpose mode × accumulate mode × element type) plus a fourth implicit operator-representation axis, and lists which concrete subclasses cover which combinations (including which override the Hermitian-transpose method vs. inherit it from the helper template). The variant-axis enumeration on the L0 surface side is the inverse of the L1 collapse — the chapter is explicit that L1 absorbs all four axes — and is comprehensive within the chapter's stated scope. The `kspsolver-base-class.md` chapter scopes its element-type axis to the `OperType ∈ {Operator, ComplexOperator}` static-assert (citing `ksp.hpp:32-34`); no hidden branches.

**cross-reference-integrity — warning.** Verified all concept-page targets exist: `concepts/solve-monad.md`, `concepts/solver-as-operator.md`, `concepts/ksp_solve.md`, `concepts/complex-from-real-lift.md`, `concepts/constructed-operators.md`, `concepts/variant-absorption.md` — all present. Verified `L1/apply_linop.md`, `L2/krylov-step.md`, `L1-L0/apply-linop-mutation-rotation.md`, `L0/ksp-factory-file.md`, `L0/mfem-vector-types.md` — all present. However, two issues surface:
  - The `kspsolver-base-class.md` chapter's `## Referenced from` block contains a self-loop link: `[`L0/apply-linop-overload-set`](./apply-linop-overload-set.md)` from the kspsolver chapter is fine, but the corresponding back-link in `apply-linop-overload-set.md`'s `## Referenced from` block points to `[`L0/kspsolver-base-class`](./kspsolver-base-class.md)`. Both new chapters cross-reference each other — sensible, but worth flagging that both forward-declarations land in the same bundle-2 commit. No resolution issue (both are being introduced together), just a structural observation.
  - The `concepts/convergence-test.md` page is referenced from `kspsolver-base-class.md`'s "Notes for higher layers" section. Cross-checked: this page exists in `book/src/concepts/` (per SUMMARY.md line 86) — pass.

  The warning is for the report's Open Question #4 disclosure: the L1 `ksp_solve` operator is referenced as "forthcoming firm-up" but does NOT currently exist at `book/src/L1/ksp_solve.md` (only the concept page exists). The `kspsolver-base-class.md` chapter's `## Referenced from` block lists `[L1/apply_linop]` (which exists) but cites `[concepts/ksp_solve]` (which exists) only — it does NOT actually link a nonexistent `L1/ksp_solve.md`. The prose mention of "forthcoming L1 `ksp_solve` operator" is forward-narrative without a broken link, but a reader following the trail of `concepts/ksp_solve` → expecting an `L1/ksp_solve.md` would find none. Mark warning so repairer can decide whether the forward-reference text should be qualified explicitly.

**edge-label-fidelity — pass.** Not strongly applicable — L0 reference-note chapters don't carry layer-to-layer edge labels in the rotation-edge sense. The two chapters do forward-reference L1>L0 lowering themes (specifically `apply-linop-mutation-rotation`) and describe what the L1 collapse will look like, but in a "this is the L0 side of the rotation" framing — consistent with the L0 reference-note discipline.

**plan-kind-consistency — pass.** The CYCLE.md frontmatter declares `scope: L0 reference-notes bootstrap, bundle 2`, which is consistent with the content shape (two new L0 reference-note chapters + index update + SUMMARY.md registration). No rough-in / firm / theme / observation / audit kind is declared on individual proposed-changes blocks because they are all "new file" / "edit existing file" mechanical inserts — consistent with the layer-intro-author role.

**skill-uptake-survey — warning.** The report does not explicitly reference invocation of any skill. Relevant skills that could have been invoked include `verify-citation-range` (for verifying the ~35 cited line ranges — particularly the load-bearing ones at `ksp.cpp:272`, `operator.hpp:202-206`, `solver.hpp:22`) and `summary-md-surgical-insert` (for the SUMMARY.md edit; this skill exists in `skills/`). The agent's Open Question #2 mentions "grep-verified the function signatures exist at the cited start-lines but did not read every line" — this is essentially the verify-citation-range procedure performed informally without invocation. Surfacing as telemetry, not blocking; the report follows the spirit of the skills without naming them.

### Issues found

1. **CYCLE.md "Evidence (representative)" for `kspsolver-base-class.md`, `operator.cpp:478-503` citation truncation** (severity: low). The cited range is "`BaseDiagonalOperator<Operator>::Mult` + `BaseDiagonalOperator<ComplexOperator>::Mult` definitions". Both functions are present in the range, but the complex specialisation extends to line 507 (closing brace of the `forall_switch` lambda body). Either extend the range to `:478-507` or rephrase the citation to "definitions begin at 478-503" if the range was intentionally chosen for the function signatures + opening bodies. Cosmetic precision; does not affect any claim made in the chapter prose.

2. **`kspsolver-base-class.md` "Referenced from" forward-references nonexistent `L1/ksp_solve` chapter implicitly** (severity: low-medium). The chapter prose in the "Notes for higher layers" section says *"`BaseKspSolver` is the natural anchor for the L1 `ksp_solve` operator (forthcoming)"*. The Referenced-from list itself only links to `[concepts/ksp_solve]` which does exist — so there is no broken link — but a reader who interprets "forthcoming" as a near-term commitment may try to find an `L1/ksp_solve.md` and find none. Worth either explicitly qualifying ("the future `L1/ksp_solve.md` chapter, not yet present") or removing the forward-reference until the L1 entry lands. The agent flagged this in Open Question #4 themselves.

3. **New "Overload sets and class interfaces" grouping in `L0/index.md`** (severity: low; agent-flagged in Open Question #7). The new grouping label is long ("Overload sets and class interfaces") but semantically distinct from the existing two groupings ("Conventions", "File overviews"). The two new chapters genuinely do not fit cleanly under either existing grouping — `apply-linop-overload-set.md` spans `operator.hpp` + `operator.cpp` + `rap.cpp` (so it's not a single-file overview), and both chapters describe surfaces rather than idioms (so they're not conventions). The new grouping is internally consistent with the L0 grouping discipline (each grouping has its own semantic axis). No correctness issue; flag is for repairer/integrator to confirm the grouping label is the preferred wording or whether a shorter label like "Class surfaces" or "Multi-overload surfaces" is desired.

4. **Bundle-2 chapter mutual cross-references both land in same commit** (severity: very low, structural observation). The two new chapters cross-reference each other in their `## Referenced from` blocks. Both forward-references resolve only when both chapters land — which is the case in this bundle, but the staging-by-cycle commit pattern means a reader checking out a mid-cycle commit would see one chapter referencing another that doesn't exist yet. No action needed at the per-report level; the integrator-finalize commit folds both into one atomic landing.

5. **No explicit invocation of `verify-citation-range` skill despite ~35 cited line ranges including several load-bearing ones** (severity: low; surfacing for skill-uptake telemetry). The agent's Open Question #2 effectively describes a `verify-citation-range` workflow performed informally. If skill-selection wants telemetry on uptake, this is a candidate datapoint: the procedure was used; the skill was not named.

6. **Open Question #6 acknowledges the retroactive-thinning sweep (priority #11) is not yet triggered by this bundle** (severity: very low; agent self-acknowledged). Per the priority #11 spec, the sweep unblocks at ≥6 reference-note chapters; bundle 1 landed 6, bundle 2 brings the total to 8, so priority #11 is now eligible. No issue with this report — just a note that the future-work claim should be picked up by cycle-007 planning or by integrator-finalize's integrator-signals emission.

## Repair

### Fixes attempted

- **Finding 1**: `operator.cpp:478-503` citation truncation — complex specialisation extends to line 507.
  - **Decision**: repaired
  - **Action**: Widened the citation range to `:478-507` in two places in CYCLE.md:
    - In the concrete-subclass family bullet for `BaseDiagonalOperator<OperType>` in the `apply-linop-overload-set.md` proposed-changes block (line ~53 of CYCLE.md). Now reads `operator.cpp:478-507` with a parenthetical split (real at 478-487, complex at 489-507).
    - In the `## Evidence (representative)` block for the same chapter (line ~103). Now reads `palace/linalg/operator.cpp:478-507` with per-specialisation line-range split in the prose.
    - Also updated the Supporting evidence section's source-files-anchored entry for `operator.cpp` (line ~291) to reflect the corrected range (`420-510` read; `478-507` cited).
  - Source verification: read `reference/palace/palace/linalg/operator.cpp:478-510`. Real specialisation occupies lines 478-487 (closing brace at 487); complex specialisation occupies lines 489-507 (closing brace at 507). Widening to `:478-507` is exact.

- **Finding 2**: Forward-reference to nonexistent `L1/ksp_solve.md` chapter not explicitly qualified.
  - **Decision**: repaired
  - **Action**: Added explicit qualification in three places in the `kspsolver-base-class.md` proposed-changes block in CYCLE.md:
    - In the `## Notes for higher layers` section, the first bullet now reads `"...the L1 ksp_solve operator (not yet authored — L1/ksp_solve.md does not currently exist; only the methodology concept page [concepts/ksp_solve](../concepts/ksp_solve.md) is present; harvester firm-up anticipated cycle-007+) — ..."`.
    - In the `## Referenced from` italic preface, qualified "queued, not yet firm" with "(queued, not yet firm — no L1/ksp_solve.md chapter exists yet; harvester firm-up anticipated cycle-007+)".
    - In the last bullet of the Referenced-from list, the `[concepts/ksp_solve]` entry now reads "(concept page only; L1/ksp_solve.md chapter not yet authored — anticipated cycle-007+)".
  - Reader trail is now explicit: anyone following `concepts/ksp_solve` looking for an `L1/ksp_solve.md` will see the qualification at three reading paths.

- **Finding 3**: New "Overload sets and class interfaces" grouping label review.
  - **Decision**: not-needed
  - **Rationale**: Critic flagged this as "no correctness issue; flag is for repairer/integrator to confirm wording." The label "Overload sets and class interfaces" is semantically precise and internally consistent with the L0 grouping discipline (each grouping has its own semantic axis). Alternative labels considered ("Class surfaces" loses the overload-set semantics; "Multi-overload surfaces" is awkward and excludes single-class chapters; slash-form "Overload sets / class interfaces" is purely cosmetic). The current label correctly covers both new chapters (`apply-linop-overload-set` is an overload-set spanning a hierarchy; `kspsolver-base-class` is a class-interface deep-dive). Cosmetic-only relabelling is a content judgment beyond mechanical-repair authority; defer to integrator if a future bundle reveals a clear alternative.

- **Finding 5** (and skill-uptake-survey check): No explicit skill invocation despite ~35 citations.
  - **Decision**: repaired
  - **Action**: Added a `## Skills invoked` section to CYCLE.md (between `## Supporting evidence` and `## Open questions / caveats`) recording telemetry for two skill-shaped procedures performed without explicit naming: `verify-citation-range` (the ~35 line-range verification + Open Question #2 description) and `summary-md-surgical-insert` (the two-bullet SUMMARY.md append). Both skills exist in `skills/`; the note records uptake-without-naming for skill-selection telemetry without inserting fake retroactive invocations.

### Unrepairable findings

None. The remaining issues called out by the critic (Issues 4 and 6) are very-low-severity structural observations that the critic explicitly tagged as "no action needed at the per-report level":
- **Issue 4** (mutual cross-references in same commit): inherent to the bundle-2 shape; integrator-finalize atomic commit folds both chapters into one landing.
- **Issue 6** (priority #11 now eligible at ≥6 reference-note chapters): integrator-signal for cycle-007 planning, not a per-report repair.

Neither requires authoring or substantive content decisions; both are properly deferred to integrator-finalize / next-cycle planning.

## Suggested resolution

`ready` — all four flagged findings handled:
- Citation truncation (`operator.cpp:478-503`) — widened to `:478-507` with per-specialisation split, verified against source.
- Forward-reference to nonexistent `L1/ksp_solve.md` — qualified in three places with "not yet authored — anticipated cycle-007+" so the reader trail is explicit.
- Grouping label — confirmed as-is; cosmetic-only relabel deferred (would be a content judgment).
- Skill-uptake telemetry — added a `## Skills invoked` section recording the two skill-shaped procedures performed informally.

Notes for the integrator:
- The repair targets the proposed-changes blocks inside CYCLE.md. When integrator-per-report applies the proposed changes to `book/src/L0/`, the repaired text is what will land.
- The grouping label "Overload sets and class interfaces" is being preserved; if a future cycle reveals a tighter label by precedent (e.g., bundle 3+ adding more multi-overload chapters), that's a SUMMARY.md / index.md edit at that point — not a current-cycle repair.
- The forward-reference qualification text uses "anticipated cycle-007+" as a soft hint, not a commitment. Integrator-finalize's integrator-signals emission can pick this up as a candidate harvester target for cycle-007 planning if desired.
- Open Question #6 (retroactive-thinning sweep / priority #11 now eligible at ≥6 reference-note chapters; bundle 2 brings total to 8) should be surfaced in integrator-finalize's integrator-signals append for cycle-007 planner consumption.
