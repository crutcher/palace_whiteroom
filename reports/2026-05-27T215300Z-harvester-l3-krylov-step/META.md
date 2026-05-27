---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T22:10:00Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-27T22:25:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: unrepairable
overall_status: ready
follow_up_agent: null
---

# META: verification of L3 krylov-step harvester (cycle-010 wave-1, identity-lowering backfill)

## Critique

### Checks run

**citation-validity** — Most cited ranges check out: `cg.md:341-362` (L2→L3 rotation claims; Claim 1 at 341-349 outer-loop obstruction, Claim 2 at 351-362 body-identity); `arnoldi_step.md:178-213` (L2→L3 lift; uncontested primitives plus MGS sequential-obstruction at 194-213); `arnoldi_step.md:99-105` (L1 step) and `:285-298` (L4 monadic form `arnoldiStep`); `gmres.md:459-471` (GMRES `inner_loop`); `gmres.md:435-454` (GMRES `restart_cycle`); `chebyshev.md:354-362` (Chebyshev `innerStep`); `polynomial_recurrence_step.md:119-160` (polynomial-recurrence sites); `cg.md:172-188` (CG v0.4 `cg_step`); `cg.md:393-425` (CG v0.5 `cg_first_step` / `cg_steady_step`); `cg.md:208-220` and `:430-446` (CG outer-driver `cg_solve` consumer sites); `iterative.hpp:52-55` (four-scalar KSP result surface); `ksp.cpp:296-310` (`BaseKspSolver::Mult` sole consumer). Two off-target citations found:

1. **`reference/palace/palace/linalg/iterative.cpp:244-250` cited as the L0 anchor for `CheckDot`** (CYCLE.md §Evidence line 218 and §Dependencies signature contract). Verified: lines 244-250 contain `ApplyB` (the preconditioner-apply helper), NOT `CheckDot`. The actual `CheckDot` definitions are at `iterative.cpp:22` and `:28` (real and complex overloads). The semantic claim about breakdown-token routing is correct in spirit (`CheckDot` is the partial-function guard whose `BreakdownTag` would propagate through `outputs.breakdown_token`), but the cited line range is wrong.

2. **Strawman §3.7 cited as "(lines 164-213)"** (CYCLE.md §"Supporting evidence" line 493). Verified: `book/src/design/l4_calculus.md` §3.7 begins at line 150, not 164; §3.8 begins at 186. A range "164-213" covers the middle of §3.7 through §3.8 inclusive, missing the §3.7 header and signature. The narrative reference to §3.7 is otherwise valid; just the line range is off by ~14 lines on the start.

The other 20+ citations in the dispatch verify cleanly.

**surface-or-evidence** — This is a fresh-author dispatch (firm L3 entry where none existed), not a refinement of existing surface. The proposed `book/src/L3/krylov-step.md` is wholly new content; the proposed annotations on `L4-L3/krylov-step-typed-wrapper-dissolution.md` and `L3-L2/krylov-step-body-identity.md` are retroactive-supersession framing (cycle-006 verdict struck by cycle-009 methodology codification). Every algebraic, structural, and variant-axis claim is either inherited from the firm L4 / L2 entries (with explicit pointer) or cited to L0 / slice corpus. The "first cycle-010 enactment of priority #20" framing is correct: this dispatch produces the L3 entry that was previously absent. Pass.

**rotation-quality** — Two rotation edges are implicated. The L4→L3 edge is the upstream typed-wrapper-dissolution theme (cycle-008 firm), which the L3 entry inherits verbatim — at the wrapper level the L4 form is strictly more compact / more abstract (typed records, monadic effect, `readonly` typing); the L3 form is the dissolved positional-value-threaded trace; this is a valid abstraction-direction rotation (L_{n+1} more abstract, L_n more concrete). The L3→L2 edge is the downstream body-identity theme (cycle-009 firm), where the body is identity-in-form and the two wrapper rotations are state-hiding (`(K, s)` positional → unified `IterState`) and abstraction-by-role (explicit tail recursion → outer-driver-by-role) — both legitimate compaction rotations. The identity-in-form annotation between L4 and L3 bodies is faithful to the upstream theme's §"Audit of cycle-002 identity-in-form claim" verdict ("L4>L3>L2 step-body chain is identity-in-form on the kernel body's primitive sequence"). Pass.

**variant-axis-coverage** — Six variant axes enumerated in both frontmatter and prose, matching the L4 and L2 entries exactly: (1) preconditioner-present-or-absent, (2) orthogonalization-variant (MGS / CGS / CGS2; below-body sequential-obstruction at MGS noted), (3) polynomial-kind (Chebyshev-4th / 1st), (4) first-iteration-unrolled-vs-branch-in-body (positional carry-threading at L3; Form A vs Form B), (5) restart-shape (non-restarted / restarted-fixed-dim / restarted-adaptive), (6) in-place-vs-out-of-place-buffer-use (transparent below L3). Each axis is rendered in L3 vocabulary (positional rather than typed; documented invariants rather than `readonly` typing). The MGS below-body obstruction is correctly scoped as below the kernel body (the kernel calls `op.orthog` as an opaque closure). Pass.

**cross-reference-integrity** — All `[link]` references and slug pointers checked. `../L4/krylov-step.md`, `../L2/krylov-step.md`, `../L4-L3/krylov-step-typed-wrapper-dissolution.md`, `../L3-L2/krylov-step-body-identity.md` all exist on disk. Concept references resolve: `sequential-obstruction`, `state-stratification`, `derived-view-hoisting`, `variant-absorption`, `first-iteration-unrolling`, `convergence-test`, `solve-monad`, `apply_BA`, `orthogonalization`, `solver-as-operator`, `constructed-operators`, `counter-update` — all are present in `book/src/concepts/` per the SUMMARY.md edit block. The reference to `book/src/L1-L0/axpby-mutation-rotation.md` is to an existing firm entry. One observation (not a failure): the prose mentions `iterate_while_L3` multiple times (e.g., §Algebraic laws Law 1; §"Iteration-rotation marker") as if it were a defined operator; it is published only in the upstream L4>L3 theme as a worked example, not as a standalone L3 entry. The CYCLE.md correctly notes this in OQ caveat 4 (routing observation). Pass.

**edge-label-fidelity** — Frontmatter `lowers_to: L2/krylov-step (via L3-L2/krylov-step-body-identity)` and `lifts_from: L4/krylov-step (via L4-L3/krylov-step-typed-wrapper-dissolution; identity-in-form on the kernel body)` accurately label the two adjacent edges. The prose §"Lowers to" discusses the L3→L2 edge (body line-for-line mapping; surface adjustments at wrapper); the prose §"Lifts from" discusses the L4→L3 edge (wrapper dissolution; body value-thread-isomorphism). No mismatched edge labels. The explicit identity-in-form annotation in §"Lifts from" — *"The L4 form is value-thread-isomorphic to this L3 form. ... This L3 entry exists for layer-coherence reasons ... The cycle-006 audit verdict 'no L3 row needed' is superseded by the methodology invariant codified cycle-009 meta-phase."* — is present and correctly worded per the dispatch prompt template. Pass.

**plan-kind-consistency** — Declared kind: `firm` L3 operator entry. Content shape matches: full Signature (Form A and Form B with positional carry), Semantics (let-chain body in L3 vocabulary), three Algebraic laws (output-extras distributivity, primitive-count invariance, state-stratum non-aliasing as documented partition), seven Non-laws catalogued, six Variant axes, Dependencies, Evidence with multiple L0 + slice corpus + lowering-chain citations, Lowers-to / Lifts-from / L3-vs-L4 / L3-vs-L2 distinction sections. No rough-in placeholders. The firm designation is appropriate — the pattern is well-attested via the cycle-005/006/008/009 chain. The two annotation-only proposed edits to `L4-L3/krylov-step-typed-wrapper-dissolution.md` and `L3-L2/krylov-step-body-identity.md` are correctly framed as supersession annotations (struck-through cycle-006 verdict + backfill pointer), not as content rewrites. Pass.

**skill-uptake-survey** — The methodology invariant *"Identity-lowerings still require both L levels"* is the dispatch's organising principle; cited and respected throughout. The invariant *"Layers are defined high→low; lifting notes go in working notes"* is followed — the L3 entry is defined in L3 vocabulary (positional values, value-threaded; no L4 monadic vocabulary or L2 unified-record vocabulary intrudes into the body description; the §"Lifts from" section narrates the upward edge but does not redefine the L3 semantics in L4 terms). The dispatch does not reference any of the explicitly-named skills (`classify-variant-axis`, `verify-citation-range`, `skill-selection`, `verify-refinement-surface`, `plan-sideways-concept-emission`, `embed-and-persist-subagent-dispatch`); the `verify-citation-range` skill would have caught the `iterative.cpp:244-250` mis-attribution for `CheckDot`. Surfacing as `warning` rather than `fail` per the check's "surfaces telemetry, not blocking" framing.

### Critical-methodology-specific checks (per dispatch prompt)

**L3 semantics defined in L3 vocabulary (not L2 or L4)** — Verified. The body's let-chain (CYCLE.md §Semantics lines 102-116) is rendered in L3 vocabulary: positional `(op, K, s)` arguments, value-threaded results, explicit `let s' = s { it = s.it + 1 }` record-update line (the dissolved `modify`), `let`-chain instead of `do`-block. The primitives `apply_linop`, `axpy`, `axpby`, `axpbypcz`, `dot`, `nrm2`, `scal` are used as L3-native whole-tensor operations (this matches the cycle-006 audit's verdict that the L2 primitive vocabulary is *already L3-native by signature shape*); the §Dependencies section is explicit that "the body references the L3-native whole-tensor primitives by their L1 names ... — these are L3-native by signature shape (each operates on whole tensors with no element loop exposed), and their L1 entries serve as the citation anchors." This is a faithful application of the high→low discipline — the primitives are L3-native vocabulary that happens to share names with their L1 counterparts; the L3 entry is not defining its semantics *in terms of L1 vocabulary*. No L4 monadic vocabulary appears in the L3 signature; no L2 unified `IterState` record appears in the L3 body. The three absent L4 features (`Solve` monad, `readonly` typing, Form-A/B combinator distinction) are explicitly catalogued in §Signature lines 90-95.

**Lifts-from contains explicit identity-in-form annotation** — Verified. CYCLE.md §"Lifts from" (lines 202-206) carries the annotation: *"The L4 form is value-thread-isomorphic to this L3 form. The L4>L3 typed-wrapper-dissolution theme makes the dissolution explicit; after dissolution, the bodies are identical modulo notation (L4's do-block plus modify becomes L3's let-chain plus explicit record-update; L4's typed records become L3's positional values). This L3 entry exists for layer-coherence reasons — a reader navigating L3 must find krylov-step defined in L3 vocabulary, not have to reach up to L4. The cycle-006 audit verdict 'no L3 row needed for krylov-step' (on identity-in-form grounds) is superseded by the methodology invariant Identity-lowerings still require both L levels codified cycle-009 meta-phase."* This is the explicit template form requested by the dispatch prompt.

**Proposed SUPERSEDED annotations on the upstream and downstream lowering themes** — Both annotation-edits are faithful to the cycle-006 verdict being struck:
- The L4-L3 theme edit (CYCLE.md lines 443-453) correctly identifies the §"Audit of cycle-002 identity-in-form claim" §"Consequence for L3 dep-map" paragraph at line 218 (verified). The replacement text preserves the original verdict-as-historical-record framing and adds the cycle-010 backfill pointer with the methodology-invariant rationale. The audit verdict itself (§"Audit verdict — confirmed-with-refinement") is correctly left unchanged — the body's identity-in-form property *enabled* the trivial backfill, it did not eliminate the need.
- The L3-L2 theme edit (CYCLE.md lines 455-463) correctly identifies the §"Context" bullet at line 15 (verified). The replacement text adds the L3 entry pointer `[`L3/krylov-step`](../L3/krylov-step.md)`, marks `firm cycle-010`, and adds the methodology-invariant rationale. The original "(no standalone `L3/krylov-step.md`; the audit established that an L3 row would duplicate content)" framing is correctly converted to historical narrative.

### Issues found

1. **citation-validity (warning)**: `iterative.cpp:244-250` is mis-attributed to `CheckDot` (CYCLE.md §Evidence line 218, §Signature lines 88-90). Actual CheckDot definitions are at `iterative.cpp:22` and `:28`. The semantic claim (BreakdownTag propagation through `outputs.breakdown_token`) is correct; only the L0 anchor range needs repair. Severity: moderate — citation-grounding invariant violation.

2. **citation-validity (warning)**: Strawman §3.7 cited as "(lines 164-213)" in CYCLE.md §"Supporting evidence" line 493 — actual §3.7 starts at `book/src/design/l4_calculus.md:150`. Severity: minor — the narrative reference to §3.7 is otherwise valid; only the line range is off by ~14 lines on the start.

3. **skill-uptake-survey (warning)**: The `verify-citation-range` skill would have caught the two citation-range issues above. No skill invocation surfaced in the dispatch report. Severity: minor — telemetry-only check per role spec.

4. **Frontmatter convention precedent** (observation, not a failure): The L3 entry introduces YAML frontmatter with `layer`, `operator`, `firmness`, `lowers_to`, `lifts_from`, `variant_axes` fields. The corresponding L4 (`book/src/L4/krylov-step.md`) and L2 (`book/src/L2/krylov-step.md`) entries have NO frontmatter at all (verified). Not a violation — the L3 entry's frontmatter is informative and consistent with what other layered frameworks do — but it sets a precedent that may eventually need backfill to L4 / L2 / L1 entries for consistency. Surfaces as an observation for repairer / integrator awareness; not blocking. Severity: trivial — convention drift, not content failure.

5. **`iterate_while_L3` referenced but not anchored** (observation, not a failure): The L3 entry references `iterate_while_L3` multiple times (e.g., §Algebraic laws Law 1's RHS expression; §"Iteration-rotation marker" closing paragraph; §Lowers-to discussion). The operator is published only as a worked example in `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for `iterate_while` looks like" (with both unpruned and pruned forms; cycle-008 firm). It is not a standalone L3 entry. CYCLE.md correctly surfaces this in OQ caveat 4 (routing observation, future `same-layer-cross-cutter`). Severity: trivial — anchoring is via the upstream theme; no broken reference. Surfaces as a future-routing observation rather than a critique-blocker.

## Repair

### Fixes attempted

**Finding 1 — citation-validity: `iterative.cpp:244-250` mis-attributed to `CheckDot`**
- **Decision**: repaired
- **Verification**: Re-read `reference/palace/palace/linalg/iterative.cpp` directly. Lines 22-32 contain the two `CheckDot` overloads (real at `:21-25` definition starting at template line :21; complex at `:27-32` definition starting at template line :27; the inline keyword + signature lines are :22 and :28 respectively, with bodies extending through :25 and :32). Lines 244-250 contain `ApplyB` (the preconditioner-apply helper that calls `B->Mult(x, y)` inside a `BlockTimer`). The critic's identification is correct.
- **Action**: Three sites in CYCLE.md were corrected (all referenced the same bad range):
  - §Semantics line 123 (inside the `edit:book/src/L3/krylov-step.md` proposed-changes block): `iterative.cpp:244-250 (CheckDot)` → `iterative.cpp:22-32 (CheckDot; real overload at :22, complex overload at :28)`. The integrator-per-report will read the corrected anchor when applying the artifact write.
  - §Evidence line 218 (inside the same proposed-changes block): same correction applied. This is the entry-level citation list inside the L3 entry's Evidence section.
  - §"Operator content" recap line 480 (outside the proposed-changes block; the dispatch's own self-description): `iterative.cpp:244-250` → `iterative.cpp:22-32 for CheckDot`. Self-consistency repair.
- **Range selection**: The critic noted `CheckDot` definitions are at lines 22 and 28 (the `inline void CheckDot(...)` signature lines). The full overload-set spans `:21-32` (template + real overload + template + complex overload). I selected `:22-32` as the closest faithful range — it covers both overload signatures plus their bodies, anchored on the first overload's signature line. The semantic claim (`BreakdownTag` propagation through `outputs.breakdown_token` via the partial-function guard) is preserved unchanged.

**Finding 2 — citation-validity: Strawman §3.7 cited as "(lines 164-213)"**
- **Decision**: repaired
- **Verification**: Re-read `book/src/design/l4_calculus.md` directly. §3.7 (`### 3.7 Loops (\`iterate_while\`)`) starts at line 150. §3.8 (`### 3.8 Demand-driven evaluation and pruning`) starts at line 186. §3.7 spans 150-184; §3.8 spans 186-213 (the section continues past 213, but the critic's stated end at 213 captures the load-bearing pruning rule). The original range "164-213" started in the middle of §3.7's small-step semantics block (skipped the section header, signature, and intro prose) and extended through §3.8.
- **Action**: CYCLE.md §"Supporting evidence" line 493 corrected from `§3.7 (lines 164-213)` → `§3.7 (lines 150-184) and §3.8 (lines 186-213) — the strawman's iterate_while reduction rule (§3.7) and demand-driven pruning rule (§3.8)`. The narrative was already referencing both §3.7 (for the `iterate_while` reduction) and §3.8 (for the demand-pruning rule cited transitively via the upstream theme); the corrected citation now anchors both sections explicitly. This is the dispatch's own §"Supporting evidence" section (outside the proposed-changes blocks); the L3 entry's §Dependencies section already references §3.7 narratively without a line range, so no in-artifact citation needs adjustment.

**Finding 3 — skill-uptake-survey: `verify-citation-range` skill not invoked**
- **Decision**: unrepairable
- **Rationale**: This is a telemetry-only check per the critic's framing ("surfaces telemetry, not blocking"). The skill-invocation telemetry is a per-dispatch behavioral signal that cannot be retroactively added to a completed dispatch's record — invoking the skill now would not change the dispatch's actual skill-uptake pattern. The fact that the citation-validity issues were caught by the critic and repaired here (rather than caught up-front by the producer via the skill) is the substantive signal the check surfaces; the appropriate follow-up is procedural (future harvester dispatches at this scope should invoke `verify-citation-range` after authoring citations), not corrective. Routed to no follow-up agent — this is an integrator-finalize / meta-phase observation, not blocking.

### Unrepairable findings

- **skill-uptake-survey (telemetry)**: As above. Informational signal for future cycles' planner / meta-phase consideration. Not a follow-up dispatch target.

The critic also surfaced two observations (Issues #4 frontmatter convention precedent; #5 `iterate_while_L3` anchoring) that were not flagged as warnings — both are `pass`-level observations the critic explicitly marked as non-blocking. No repair action needed; they surface as routing notes for integrator / future cycles.

## Suggested resolution

`ready` — both citation-validity warnings have been repaired in-place in CYCLE.md (including inside the embedded `edit:book/src/L3/krylov-step.md` proposed-changes block; the integrator-per-report will see the corrected anchors). The remaining `skill-uptake-survey` warning is telemetry-only and does not block integration. The dispatch's substantive content (L3 layer-coherence backfill per the cycle-009 methodology invariant) is unchanged; the algebraic-laws section, semantics, variant-axis profile, and rotation analysis all verified clean by the critic's other 6 checks (all `pass`).

The integrator-per-report can apply this report's proposed-changes blocks as-is. The two annotation-only edits to the upstream L4>L3 theme and downstream L3>L2 theme (struck cycle-006 verdict + cycle-010 backfill pointers) are verified clean by the critic and unchanged by repair.

Observations for the integrator:
- The L3 entry's frontmatter convention (Issues #4) is new at L3 but harmless; if future layer-intro-author dispatches normalize frontmatter across L1/L2/L4 entries, this L3 entry is the precedent.
- The `iterate_while_L3` references (Issues #5) are anchored transitively via the upstream theme; a future `same-layer-cross-cutter` dispatch may want to firm `iterate_while_L3` as a standalone L3 entry.
