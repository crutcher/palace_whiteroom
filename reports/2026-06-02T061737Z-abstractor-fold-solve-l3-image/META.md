---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T06:40:00Z
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
repaired_at: 2026-06-02T07:05:00Z
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

# META: verification of "L3>L2 theme sketch + L3 entry — fold_solve L3-image (partial-obstruction)"

## Critique

### Checks run

**citation-validity — pass.** All eight load-bearing L0 anchors were re-read against on-disk source via `palace-codemap read_range` and verified exact: `transientsolver.cpp:33` (`TimeOperator time_op(iodata, space_op, dJdt_coef)`), `:35` (`delta_t = iodata.solver.transient.delta_t`), `:36` (`n_step = config::GetNumSteps(...)`), `:77` (`for (int step = 0; step < n_step; step++)`), `:89` (`time_op.Init()` under `if (step == 0)`), `:93` (`time_op.Step(t, delta_t)` under the `else`), `:98` (`const Vector &E = time_op.GetE()`), `:99` (`const Vector &B = time_op.GetB()`); `timeoperator.cpp:312` (`op = std::make_unique<TimeDependentFirstOrderOperator>(...)`), `:410` (`ode->Step(sol, t, dt)` inside `TimeOperator::Step`); `drivensolver.cpp:231` (`ErrorIndicator DrivenSolver::SweepAdaptive(SpaceOperator &space_op) const`), `:384` (`for (std::size_t it0 = it; it < max_size_per_excitation && memory < convergence_memory; it++)`), `:389` (`omega_star = prom_op.FindMaxError(excitation_idx)[0]`). Every pinpoint lands on exactly the cited token; no drift. The negative-anchor framing for the opaque per-step leaf ("the negative anchor is Palace's CALL `:410`, NOT MFEM internals") is sound and matches the actual forwarder body at `timeoperator.cpp:407-413`. Report carries no `verified_against:` YAML block (it is an abstractor report, not a lowering-verifier audit), so the YAML round-trip sub-check is N/A.

**surface-or-evidence — pass.** This is not a refinement of an existing operator/theme; it lands two NEW entries (an L3 operator + an L3>L2 theme) plus dual-registration and coupled re-anchors. The proposal modifies surface (new chapters + index/SUMMARY rows + three re-anchor edits) and carries rotation/obstruction evidence read off positive source. The three re-anchors are pure forward-reference resolution (deferred-question → resolved-verdict), the legitimate analogue of retroactive-evidence framing. Not a stranded rotation_claim.

**rotation-quality — pass (with one noted-not-blocking content/slug tension; see (c) below).** The L3>L2 theme asserts a genuine vocabulary translation: the L3 explicit value-threaded `step_loop` tail recursion carrying a first-class carry-threading `sequential-obstruction` marker dissolves into an L2 fold-by-role composition (`time_sweep_fold (time_step_op op) s0 schedule`) with the iteration view erased and the obstruction shadowed to L2 non-laws (no commutativity, no whole-march fusion). This is a strictly-more-abstract / state-hiding compression (the explicit imperative sweep + marker → a named fold-by-role driver), not a 1:1 rename — it passes. The L4>L3 direction (combinator → explicit in-place sweep) is also a genuine substantive rotation already firm at c058 D2. The L3 entry itself is correctly an iteration-rotation form, not a mirror of the dissolution RHS (see (b)).

**variant-axis-coverage — pass.** Four axes declared (schedule-source, per-step-operator, carry-shape, element-type), matching the L4 cap's profile. `schedule-source` is correctly named the load-bearing axis, with `fixed-list` scoped as the default L3 surface and `state-generated` (SweepAdaptive) explicitly scoped OUT of both the L3 entry's default surface and the L3>L2 theme's LHS, with the deferral gated on the cap's OQ `fold-solve-greedy-schedule-source-generalization` (batch-18) and a second-witness citation (`drivensolver.cpp:231,384,389`). No hidden branch — the state-generated superset is disclosed, cited, and bounded.

**cross-reference-integrity — pass.** All `[link]` targets resolve on disk: the precedent/sibling chapters (`L3/chebyshev`, `L3/eigsolve`, `L3/orthogonalize`, `L3/krylov-step`, `L3/ksp_solve`, `L3/nrm2`, `L3/linear_combination`, `L3/inner_product`, `L4/fold_solve`, `L4/solve_family`, `L4/iterate-while`, `L4-L3/fold-solve-time-step-dissolution`, `L3-L2/eigsolve-opaque-eigen-iteration`, `L3-L2/chebyshev-nested-recurrence`, `L2/eigsolve`) and all five concept pages (`sequential-obstruction`, `tensor-field-lift`, `state-stratification`, `constructed-operators`, `variant-absorption`) exist. All five surgical OLD-text replace anchors match exactly once each (L4/fold_solve §Lowers-to; L4-L3 dissolution ×2; L3/index count tally; L3-L2/index cohort bullet). The SUMMARY.md insert anchors (`orthogonalize`, `chebyshev-nested-recurrence`) and the L3/index + L3-L2/index table-row insert anchors all match; no pre-existing `L3/fold_solve` / `fold-solve-time-step-body` row exists, so no duplication. Both new chapters are wired into SUMMARY.md. The dual-registration count bumps (L3 partial-obstruction 3→4, L3>L2 firm 5→6) are arithmetically consistent with the on-disk counts (L3 was "17 firm + 3"; L3>L2 was "5"). Note: neither new chapter is a `firm`-claimed body authored outside a fence — both are `new:` blocks enclosing their full bodies (the L3 entry carries `## Status`, signature, algebraic laws, evidence INSIDE the fence; the L3>L2 theme similarly), so the build-readiness firm-body-inside-fence guard passes.

**edge-label-fidelity — pass.** The L3>L2 theme is labeled L3→L2 and its prose narrates exactly that edge (LHS = L3 value-threaded form, RHS = L2 fold-by-role, direction stated L3→L2 forward per high→low). The three coupled re-anchors touch the L4 cap §Lowers-to and the L4>L3 dissolution theme; each correctly describes its own edge (the L4 entry's in-line L4→L3 direction record; the dissolution theme's L4→L3 rewrite) and points at the new L3 entry / L3>L2 theme as the lower-edge homes without mislabeling. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared content is an L3 operator entry at `partial-obstruction` + a `firm` L3>L2 theme. The L3 entry's shape matches `partial-obstruction` (body-lifts / loop-doesn't, with the obstruction carried as a witnessed `sequential-obstruction` + opaque-library leaf — the chebyshev/eigsolve template) — no rough-in placeholders masquerading as firm. The L3>L2 theme is `firm` on the structural outer-sweep erasure with a secondary `obstruction(opaque-library-ownership)` on the per-step leaf — the same firm-with-secondary-obstruction shape the sibling `eigsolve-opaque-eigen-iteration` carries; consistent.

**skill-uptake-survey — warning.** The report's shape implies two relevant skills whose invocation is not referenced. (1) `verify-citation-range` / the `tools/citecheck/` mechanical realization: the report ASSERTS "citecheck `[ok]` on all eight load-bearing anchors" (§Supporting evidence, line 506) but does not show the invocation form, and the citecheck assertion conflicts with the `--anchor` discipline being a per-pinpoint check (the assertion is a summary claim, not a transcript). This is telemetry-only, non-blocking — I independently re-verified all anchors via codemap and they are correct. (2) `proposed-changes-fence-encloses-full-body-guard` is a critic-side skill (not producer); N/A to uptake. The warning is purely the unsurfaced citecheck invocation; it does not affect correctness.

### Issues found

1. **(content/slug mismatch — self-flagged by the abstractor; severity: low, non-blocking) — `L3-L2/fold-solve-time-step-body.md` §Context + §Open-questions #1.** The canonical slug `fold-solve-time-step-body` implies a per-step-*body* lowering, but the theme's actual substantive content is the OUTER-SWEEP erasure + an opaque-per-step leaf that does NOT decompose into L2 primitives (unlike `eigsolve`, whose body opens to `apply_linop ▷ ksp_solve`). The abstractor retained the planner's canonical slug (correct per the cross-report slug-stability convention — do NOT self-invent) and recorded the mismatch as load-bearing scoping in §Context framing-correction, §Justification kind, §"What this lowering does NOT cover", and §Open-questions #1 (suggesting `fold-solve-sweep-erasure` would be more accurate). This is NOT a rotation-quality failure: the theme IS a genuine translation (verified against the firm sibling `eigsolve-opaque-eigen-iteration`, which is also `structural` + opaque-library; the only structural difference is that `fold_solve` has no body-identity half because its body is an opaque leaf — a legitimate, honestly-disclosed variant, and the L4>L3 dissolution already established the opaque per-step leaf treatment at `timeoperator.cpp:410`). The slug is descriptively imperfect but the content is well-formed and the mismatch is fully documented for integrator/meta-phase reconciliation. Flagging here as the repair candidate the abstractor themselves surfaced — a rename decision is above the abstractor's authority and is correctly deferred.

2. **(taxonomy-prose deferral — self-flagged; severity: low, non-blocking) — `L3/index.md` count-tally bump + §Open-questions #3.** The report adds a SIXTH obstruction-profile shape (f) (combined carry-threading-sequential-obstruction + opaque-per-step-leaf on a Palace-authored, L3-rendered sweep) INSIDE the count-tally bullet (the authoritative count home) rather than folding it into the §Semantics-overlay obstruction-profile spectrum prose at `L3/index.md:15`. The abstractor flags this as a low-priority layer-intro-author follow-up. The shape-(f) characterization is internally consistent and correctly distinguished from (b)/(c)/(e); the deferral is a reasonable scope boundary (the count-tally bullet is the authoritative enumeration). Recorded as a candidate, not a defect.

3. **(no-L2-RHS entry — self-flagged; severity: low, non-blocking) — `L3-L2/fold-solve-time-step-body.md` §L2 form (RHS) + §Open-questions #2.** There is no standalone `L2/fold_solve` entry; the L2 RHS is a fold-by-role form modeled on `L2/eigsolve`'s eigen-iteration-fold-by-role rather than a citation to a standalone L2 chapter. This is consistent with the redirect's "no degenerate mirror" posture (the body is opaque, so an L2 entry would carry no decomposition) and with how `solve_family`'s dissolution theme is the authoritative L3-form home for its map. The abstractor correctly did not open a formal OQ (low fan-out until a downstream L2 consumer pulls). Surfaced for completeness; not a cross-reference-integrity failure (the RHS is a by-design role-form, not a dead link — `L2/eigsolve.md` exists and is cited as the model).

### Anti-mirror warrant assessment (the planner's load-bearing (b) focus)

The L3-ENTRY verdict is **sound and well-evidenced**. I independently confirmed the decisive distinction against on-disk artifact state: `L4/solve_family.md` §Lowers-to states the NO-ENTRY warrant turns precisely on "the family members are independent — embarrassingly parallel ... so L3's iteration-rotation content for the family shell is the negative finding 'the loop lifts'" — a mirror of the dissolution RHS. `fold_solve`'s sweep, by contrast, carries a real carry-threading `sequential-obstruction` (verified: `ode->Step(sol, t, dt)` at `timeoperator.cpp:410` mutates the persistent `sol` in place; the next step reads it — the schedule does not commute) PLUS an opaque-library per-step leaf. That is the `chebyshev` (c013) / `eigsolve` (c024) `partial-obstruction` shape (both confirmed `partial-obstruction` on disk). `partial-obstruction` is the correct status: the body lifts (one opaque whole-state advance, identity-in-form to the firm L4 cap), the loop is the obstruction — matching the CLAUDE.md "Two rough-in qualifiers are first-class" definition (status reflects loop structure, not body). The report's refinement over the precedents — that `fold_solve`'s sweep is Palace-AUTHORED (`transientsolver.cpp:77`) and therefore RENDERS as a tail recursion (the `ksp_solve`/`chebyshev` rendering), unlike `eigsolve`'s un-renderable library-owned loop — is accurate and correctly cited; it is what makes the new combined "shape (f)" genuinely distinct rather than a redundant re-statement of an existing precedent. The anti-mirror principle is satisfied: the L3 entry shifts vocabulary (explicit value-threaded sweep + first-class obstruction markers) rather than mirroring the c058 D2 dissolution theme's forward-rewrite narration.

---

## Repair

### Fixes attempted

- **Finding**: skill-uptake-survey — warning. The report ASSERTS "citecheck `[ok]` on all eight load-bearing anchors" (§Supporting evidence, line 506) but does not show the invocation form; the citecheck summary claim is telemetry, not a transcript.
  - **Decision**: not-needed.
  - **Rationale**: Telemetry-only, explicitly non-blocking per the critic, who independently re-verified all eight L0 anchors via `palace-codemap read_range` and found every pinpoint lands on exactly the cited token (citation-validity = pass). The missing invocation transcript does not affect correctness; no claim is unsupported and no surface is wrong. Surfacing the invocation form would require the original agent to re-run/re-narrate its own tooling step — that is producer telemetry hygiene, not a mechanical surgical fix the repairer can apply without authoring new content. Per-finding accountability: nothing to repair in CYCLE.md.

- **Finding (Issue 1)**: content/slug mismatch — `fold-solve-time-step-body` descriptively under-describes the content (it is outer-sweep erasure, not body-lowering, because `fold_solve`'s per-step body is the opaque `ode->Step` leaf with no L2 composition). Abstractor suggested `fold-solve-sweep-erasure` would be more accurate.
  - **Decision**: by-design-no-repair.
  - **Rationale**: The abstractor correctly retained the planner's canonical slug per the cross-report slug-stability convention (do NOT self-invent a divergent slug mid-dispatch) and documented the mismatch as load-bearing scoping in §Context framing-correction, §Justification kind, §"What this lowering does NOT cover", and §Open-questions #1. A slug RENAME is a content/scope decision above repair authority (it would re-author the canonical slug and ripple through every cross-reference) and is correctly deferred. Carried as an OQ-intake-note for the integrator (below). Not a defect.

- **Finding (Issue 2)**: taxonomy-prose deferral — the report adds a SIXTH obstruction-profile shape (f) (combined carry-threading-sequential-obstruction + opaque-per-step-leaf on a Palace-authored, L3-rendered sweep) inside the `L3/index.md` count-tally bullet rather than folding it into the §Semantics-overlay obstruction-profile spectrum prose at `L3/index.md:15`.
  - **Decision**: by-design-no-repair.
  - **Rationale**: The shape-(f) characterization is internally consistent and correctly distinguished from (b)/(c)/(e); placing it in the count-tally bullet (the authoritative enumeration home) is a reasonable scope boundary. Folding it into the spectrum prose is substantive layer-intro-author authoring (a new taxonomy sub-shape narration), not a mechanical fix. Carried as an OQ-intake-note for the integrator (below). Not a defect.

- **Finding (Issue 3)**: no-`L2/fold_solve` RHS entry — the L2 RHS is a fold-by-role form modeled on `L2/eigsolve`'s eigen-iteration-fold-by-role rather than a citation to a standalone L2 chapter.
  - **Decision**: by-design-no-repair.
  - **Rationale**: Consistent with the redirect's "no degenerate mirror" posture (the per-step body is opaque, so a standalone `L2/fold_solve` entry would carry no decomposition) and with how `solve_family`'s dissolution theme is the authoritative L3-form home for its map. The RHS is a by-design role-form, not a dead link — `L2/eigsolve.md` exists and is cited as the model (cross-reference-integrity = pass). The abstractor correctly declined to open a formal OQ (low fan-out until a downstream L2 consumer pulls). Nothing to repair.

### Unrepairable findings

None. The single warning is telemetry-only and non-blocking; the three self-flagged issues are by-design dispositions, not defects requiring revision. No follow-up agent is needed.

## Suggested resolution

`overall_status: ready`. All eight critic checks are `pass` or a non-blocking `warning` (independently re-verified), and the three self-flagged issues are documented by-design dispositions. The report applies cleanly. Notes for the integrator:

- **OQ-intake-note (Issue 1, slug rename)**: append an open question proposing the eventual rename of canonical slug `fold-solve-time-step-body` → `fold-solve-sweep-erasure` (or equivalent), since the theme's content is outer-sweep erasure + opaque-per-step-leaf, not a per-step-body lowering. Cross-report slug-stability blocked the in-dispatch rename; a rename is a cross-cutting edit (chapter filename + all inbound links from `L3/fold_solve.md`, the L4 cap, the L4>L3 dissolution theme, and both index tables) best done deliberately. Fan-out: low (descriptive-accuracy only).
- **OQ-intake-note (Issue 2, shape-(f) taxonomy)**: append an open question / layer-intro-author follow-up to fold the new combined obstruction-profile shape (f) (carry-threading-sequential-obstruction + opaque-per-step-leaf on a Palace-authored, L3-rendered sweep) from the `L3/index.md` count-tally bullet into the §Semantics-overlay obstruction-profile spectrum prose at `L3/index.md:15`. Fan-out: low (index-prose coherence).
