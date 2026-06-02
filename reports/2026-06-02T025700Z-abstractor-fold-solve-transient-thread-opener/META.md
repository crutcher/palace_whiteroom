---
verifies: ../REPORT.md
critiqued_at: 2026-06-02T030949Z
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
repaired_at: 2026-06-02T031500Z
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

# META: verification of cycle-057 D4 — `fold_solve` / `time_step_fold` transient combinator thread-opener

## Critique

### Checks run

**citation-validity: pass.** Ran `citecheck.py --scan` (29 ok / 32; the 3 non-ok are tooling-scope artifacts, not drifts: `open-questions.md:899-910` and `:910` resolve to `scaffolding/open-questions.md` which the scanner does not search under `reference/`/`book/src`, and `index.md:61` is a bare-basename AMBIG that the prose disambiguates as `book/src/L4/index.md`). Anchor-confirmed every load-bearing pinpoint with `--anchor`: `transientsolver.cpp:93` ('Step'), `:77` ('for'), `:36` ('n_step'), `timeoperator.cpp:410` ('ode'), `timeoperator.hpp:37` ('ODESolver'), `:34` ('sol') — all OK, anchor on the cited line. Hand-verified the source ranges: `transientsolver.cpp:77-104` shows the `for (int step…)` sweep with the `step==0 → Init()` / `step!=0 → Step(t,delta_t)` branch (89/93) exactly as the report describes; `timeoperator.cpp:307-308` shows `E.MakeRef(sol,…)`/`B.MakeRef(sol,…)` aliasing; `:407-412` shows the `Step` body `ode->Step(sol,t,dt)` with the `dt = dt_input` restore. The report's §Supporting-evidence self-correction note (`:77` not `:78`, `:36` not `:35`, advance is `:93` not D1's `:94`) is accurate and the corrected lines verify. No `verified_against:` YAML block present (n/a — this is an abstractor sketch, not a lowering-verifier audit). No off-by-one survived.

**surface-or-evidence: pass.** Not a refinement of an existing operator/theme; it is a new-thread-opener that (a) modifies surface — two `edit:book/src/L4/index.md` blocks adding one rough-in dep-map row + one frontier bullet — and (b) carries the load-bearing fold-shape evidence (`transientsolver.cpp:93` → `timeoperator.cpp:410` in-place `sol` advance). The state-threaded-fold characterization is evidence-grounded, not asserted: the source shows each `Step` mutating the persistent `sol` whose views `E`/`B` the next postprocess reads, i.e. input_i = output_{i-1}, which is a genuine `foldl`, not a `map`. The map/fold contrast against `solve_family` is well-supported by the cited `solve_family.md` sibling.

**rotation-quality: pass (qualified — thread-opener authors no rotation theme by design).** No L_{n+1}>L_n rotation theme is authored this cycle, so there is no rotation surface to grade for compaction. The report explicitly defers the lowering theme (§Anchor-decision point 1: the L4 combinator entry precedes its lowering, mirroring `solve_family` → `solve-family-map-dissolution`). The *characterization* offered — recognizing the transient driver as a `foldl step_op s0 [t_0..t_{n-1}]` and as a non-degenerate `iterate_while_pure` carry-threading member of strawman §3.7 — is a genuine abstraction (it states the outer driver more equationally than the C++ `for`-loop + in-place mutation), not a rename. The "map is a fold whose step ignores the accumulator" observation is correct and is the load-bearing distinguishing axis, not a 1:1 mapping. Pass on the honest-thread-opener basis (CLAUDE.md: a thread-opener that declines to force a landing is a pass).

**variant-axis-coverage: pass.** The integrator-variant axis (GEN_ALPHA / RUNGE_KUTTA-SDIRK23 / ARKODE / CVODE) is identified and explicitly scoped: cited at `timeoperator.cpp:314-389`, declared "absorbed into `OpParams` at construction" (the `variant-absorption` concept), and routed through the opaque-MFEM-boundary finding rather than hidden. The MPI / `Par*` axis is flagged-once per project scope (§caveat). The `TimeState = {sol}` vs `{sol, E, B}` view-exposure axis is surfaced as an explicit refinement caveat for the eventual L4 entry, not silently chosen. No hidden branches.

**cross-reference-integrity: pass.** All live `[link]`s in the two proposed `edit:` blocks resolve on disk: `solve_family.md`, `iterate-while.md`, `chebyshev.md`, `index.md` all exist under `book/src/L4/`. The new `fold_solve` slug is correctly rendered as a backtick code-span (plain text), NOT a live link to a non-existent `fold_solve.md` — verified `book/src/L4/fold_solve.md` is absent and no `[…](./fold_solve.md)` link appears, so the missing-anchor convention is honored and no `linkcheck2` dead-link would be introduced. Build-readiness guard: the report claims `rough-in`, not `firm`, so the firm-body-inside-fence guard does not apply (no firm body need be enclosed). Fence enumeration: 4 ``` markers = even parity, the two `edit:` blocks balanced, no nested-fence truncation risk (the inner shape sketches use indented-code, not nested fences). The named concepts referenced (`state-stratification`, `solve-monad`, `sequential-obstruction`, `derived-view-hoisting`, `variant-absorption`) are established spine concepts.

**edge-label-fidelity: pass.** The dep-map row carries an "L1>L0 (eventual)" lowering note; the prose at that point discusses exactly the L1>L0 edge (the `for (int step…)` time sweep threading `sol`, per `transientsolver.cpp:77-104`, with the per-step body a wrapper over the opaque MFEM step). The label and the prose agree. No mismatched edge label.

**plan-kind-consistency: pass.** Declared kind is rough-in / observation-first thread-opener, and the content matches: speculative best-guess signatures, an explicit ≥2-witness gate citing the 1-of-1 witness count, a "NOT firm" status string, and a registered-but-deferred home (dep-map row + frontier bullet, no chapter file, no SUMMARY entry). The status string `rough-in` is the correct tier for a single-witness sketch — it does not over-claim `firm` nor under-claim by burying a real structural finding. The opaque-MFEM-boundary routing correctly anticipates the eventual `obstruction (opaque-library-ownership)` sub-kind for the per-step body (the `eigsolve` shape), consistent with the codified obstruction sub-kind taxonomy.

**skill-uptake-survey: pass.** The report invokes the relevant procedural surfaces by name: `tools/citecheck/citecheck.py --anchor` for the self-verified L0 citations (§Supporting-evidence), and the `disciplined-cross-pipeline-combinator-mining-gate` skill's ≥2-witness bar as the explicit rationale for declining a firm landing (§Anchor-decision point 3, dep-map status). Telemetry present; non-blocking check satisfied.

### Issues found

No blocking issues. Minor observations (informational, candidate-for-repair but none load-bearing):

1. **`time-step-op-opaque-mfem-integrator-boundary` is legitimately scoped — no over-reach.** (book/src/L4/index.md proposed dep-map row + CYCLE.md §OQ) The report cites Palace's *call* (`timeoperator.cpp:410` `ode->Step(sol,t,dt)`) and the *member declaration* (`timeoperator.hpp:37` `unique_ptr<mfem::ODESolver> ode`), and explicitly flags that the integrator's internal per-step semantics are upstream MFEM behavior to log as an OQ "at that point, do not localize into Palace." This is the correct opaque-library discipline — it does NOT assert MFEM internals as Palace's. No issue.

2. **§3.7 shared-parent observation is sound for the meta-phase.** (CYCLE.md §Shared-parent-question + OQ `fold-solve-solve-family-share-iterate-while-parent`) The claim that `solve_family` (map) and `fold_solve` (fold) are both §3.7 `iterate_while`-family specializations distinguished solely by whether the step consumes the accumulator is mathematically correct (`foldl (\_ x -> f x) = map f`). The recommendation to NOT introduce a third parent abstraction is well-reasoned and correctly routed as a ratification question to the batch-17 meta-phase rather than decided unilaterally by the thread-opener. Sound observation.

3. **Minor (cosmetic, non-blocking): `iterate_while_pure` mapping precision.** (CYCLE.md §Sketch lines 49-57) The `fold_solve`-as-`iterate_while_pure` rendering models the carry as `{ field, step }` with a `step < length timesteps` predicate and `timesteps !! c.step` indexing. The strawman `iterate_while_pure : α → (α → Bool) → (α → α) → α` (l4_calculus.md:178-182) supports this exactly — the carry α absorbs both the field-state and the step-counter, and the predicate is a step-count predicate (the same `chebyshev` route the report cites). The mapping is faithful. The one place a future firm landing should tighten: the schedule `[Time]` is threaded into the step closure by index rather than consumed positionally as a list, which is a modelling choice (closure-captured schedule vs. list-folded schedule) the eventual L4 entry should state explicitly — already implicitly covered by the report's "the schedule is genuinely-new vocabulary" note, so this is a refinement nudge, not a defect.

4. **`verified_against:` round-trip sub-check: not applicable** — no such block in this abstractor report.

Overall shape: an honest, evidence-grounded thread-opener that declines to force a firm landing on a single witness, registers the thread at the lightest discoverable weight (plain-text rough-in row + frontier bullet, no chapter/SUMMARY churn), and routes its three open questions correctly (2nd-witness gate to batch-18, shared-parent ratification to batch-17 meta-phase, upstream-MFEM behavior as an OQ). The load-bearing state-threaded-FOLD characterization is confirmed against Palace source.

## Repair

### Fixes attempted

All 8 critic checks PASS. The "Issues found" section contains only informational sub-items (1–4), each explicitly tagged non-blocking / non-load-bearing by the critic:

- **Finding (1)**: `time-step-op-opaque-mfem-integrator-boundary` scoping — critic confirms legitimate, no over-reach. **Decision**: not-needed (critic verdict is "No issue").
- **Finding (2)**: §3.7 shared-parent observation — critic confirms mathematically sound (`foldl (\_ x -> f x) = map f`) and correctly routed to meta-phase. **Decision**: not-needed (sound observation, no defect).
- **Finding (3)**: `iterate_while_pure` mapping precision — critic confirms the mapping is faithful; the schedule-by-index vs list-folded note is a "refinement nudge, not a defect" for the eventual firm landing. **Decision**: not-needed. The nudge concerns a *future firm L4 entry's* modelling choice, which is substantive authoring out of repair scope — and it is already implicitly covered by the report's "schedule is genuinely-new vocabulary" note, so there is nothing mechanical to fix in this rough-in thread-opener.
- **Finding (4)**: `verified_against:` round-trip sub-check — n/a (no such block in an abstractor sketch). **Decision**: not-needed.

No citation drifts, no fence-parity issues, no broken cross-references, no edge-label mismatches, no plan-kind over-claim. The `fold_solve` slug is correctly plain-text (no `linkcheck2` risk), the two self-corrected citation drifts verify, no tool-tag leakage. Nothing falls within repair authority because nothing is broken.

### Unrepairable findings

None. No finding was deferred — all are `not-needed` (pass-clean), not `unrepairable`.

## Suggested resolution

`ready` — clean thread-opener, apply as-is. Notes for the integrator:

- **Proposed-changes**: D4 = `edit:book/src/L4/index.md` adding (i) one `rough-in` `fold_solve` dep-map row with a **plain-text** slug (NOT a live link — `fold_solve.md` is intentionally absent) + (ii) one frontier bullet.
- **Co-edit flag**: D1 (cycle-057) ALSO edits `book/src/L4/index.md` — correcting the `:80` `solve_family` L3-image reference. D4's `fold_solve` additions are an **anchor-distinct region** from D1's `:80` correction. Apply serially (per-report integration naturally serializes artifact writes); the two edits do not overlap.
- **Promote D4's OQs** (3):
  1. `fold_solve` + `solve_family` share the §3.7 `iterate_while` parent — **no third abstraction** (route to batch-17/meta-phase to ratify).
  2. `fold_solve` 2nd-witness gate — SweepAdaptive ROM fold is the batch-18 candidate second witness.
  3. `time_step_op` opaque-MFEM-integrator boundary — upstream `mfem::ODESolver::Step` semantics logged as an OQ; do not localize into Palace.
