---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-02T06:23:21Z
scope: L3↔L4 cross-cut — eigenmode pipeline OUTER machinery probe (solver-test-load item-3)
status: pending
integrated_at: 2026-06-02T061737Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-059 D3. Applied clean (1 surgical mid-paragraph clause replacement at L4/solve_family.md:146, prose-only). The eigenmode pipeline recorded SPINE-COMPLETE / NOT-A-WITNESS of either solve_family (map) or fold_solve (fold): one opaque eigen->Solve() (eigensolver.cpp:367), readout-only loop (:425-471), no operator/RHS family to MAP and no state-threaded solve-march to FOLD — the outer machinery adds NO new spine vocabulary. transient half re-pointed to the live ./fold_solve.md home (remaining unprobed AS a witness). 2 intake OQs verified present (eigenmode-outer-machinery-SPINE-COMPLETE-no-combinator-witness + eigenmode-hybrid-two-phase-refine-single-witness-refine_solve-candidate). citecheck --scan 19 ok / 0 failing. Build cargo make book exit 0; no build-repair needed."
---

# CYCLE: Cross-layer observation — eigenmode pipeline OUTER machinery is spine-complete (no new combinator witness)

## Summary

Probing the eigenmode driver's OUTER machinery (`palace/drivers/eigensolver.cpp`, `EigenSolver::Solve`, `:32-477`) — everything above the already-firm `L3/eigsolve` (`partial-obstruction`) + `L4/eigsolve` opaque-iteration cap — surfaces **NO new cleanly-describable spine vocabulary**. The driver calls `eigen->Solve()` **once** (`:367`); there is **no operator family and no RHS family** to map over (contrast electrostatic/magnetostatic, which map `ksp_solve` over a boundary-index family — the `solve_family` witnesses). The post-solve `for (i < num_conv)` loop (`:425-471`) is a **post-processing readout map over an already-converged eigenpair set** (`GetEigenvalue(i)` / `GetEigenvector(i)` are extractions from the single opaque solve, not per-element solves), and every load-bearing piece inside it is **already-firm or already-shared** spine/infrastructure vocabulary: `B = -1/(iω)∇×E` is `apply_linop(Curl)` (firm L3 `apply_linop`); `MeasureAndPrintAll` is the `PostOperator` measurement surface shared identically across all 5 drivers; the error-indicator accumulation is the pipeline-generic `ErrorIndicator::AddIndicator` RMS reduction. The eigenmode-specific arithmetic (`NormalizePhase` gauge fix, eigenvalue→ω `sqrt`/`/i` mapping, Q-factor) is solver-specific scalar bookkeeping, not new shared vocabulary. **Disposition: RECORDS the eigenmode pipeline OUTER machinery as spine-complete** — what the eigenmode driver does above the per-call cap is either (a) absorbed into the cap (operator assembly/scaling/shift-invert binding/initial-space), (b) the single opaque `eigen->Solve()` already capped, or (c) shared post-processing infrastructure that is not eigenmode-specific spine vocabulary. This closes the `solve_family` §Status "**eigenmode** [is] unprobed" item: eigenmode is **neither** a `solve_family` (map) **nor** a `fold_solve` (fold) witness.

## Observation kind

**Coverage gap (resolved-as-no-gap / spine-coverage finding).** The probe was scoped to find genuinely-new cleanly-describable OUTER-machinery vocabulary OR record the pipeline spine-complete. It records spine-complete. The one structurally-interesting shape (the per-mode post-processing loop, and the HYBRID two-phase refinement) is classified below against the `disciplined-cross-pipeline-combinator-mining-gate` and does NOT clear the witness/altitude bars for a new combinator.

## Specific finding

The eigenmode driver OUTER machinery decomposes into four regions; each is dispositioned:

1. **Setup / operator assembly + backend selection + scaling + shift-invert binding + initial-space + linear-solver construction** (`:37-358`). This is the construction of the `OpParams` the `L4/eigsolve` cap already absorbs (`L4/eigsolve.md` §Signature `OpParams` — "closes over the bound problem operators … the inner solver `op.inv` … the shift `σ` and spectral-transform mode … the optional divergence-free projector"). The driver-level `SetOperators` (`:184-202`), `SetShiftInvert` (`:288/305`), `SetWhichEigenpairs` (`:291/308`), `SetLinearSolver` (`:351`), `SetBMat`/`SetDivFreeProjector` (`:226/237`), `SetInitialSpace` (`:269`) calls are exactly the construction-bound configuration the cap types as `readonly` `OpParams` (`L4/eigsolve.md:66`). **No new vocabulary** — already absorbed.

2. **The eigen-solve itself** — `num_conv = eigen->Solve()` (`:367`), called **ONCE**. This is the opaque-library eigen-iteration already capped at `L4/eigsolve` (the `eigen_iterate` role-named obstruction marker) and `L3/eigsolve` (`partial-obstruction`). **No new vocabulary** — already capped; the load-bearing fact (single opaque call, no Palace loop) is the one `L3/eigsolve.md:92-96` and `L4/eigsolve.md` §Semantics already record.

3. **HYBRID nonlinear refinement** (`:377-406`) — a SECOND solve via `QuasiNewtonSolver`, constructed *from* the prior `eigen` solve (`std::move(eigen)`, `num_conv` seeded in, `:379-381`) and re-`Solve()`d (`:404`). This is a **sequential two-phase refinement**, not a family map: the QN solve consumes the prior solve's converged set as its seed. Structurally it is a *fold-flavored* refine-prior-result step (NOT independent / NOT commuting). It is, however, (a) **single-witness** within the eigenmode pipeline (no second pipeline exhibits a "solve → refine-with-second-solver" shape — driven/transient/electro/magneto have no analog), and (b) **NOT a new combinator at the OUTER altitude** — it is two sequential applications of the *same* `EigenvalueSolver::Solve` cap surface (`QuasiNewtonSolver` is another `EigenvalueSolver`), so it is already covered by the `L4/eigsolve` cap applied twice with a seed-handoff. Per the gate step 1, a single intra-pipeline witness is a spine-coverage finding, not a mineable combinator. Recorded as such (no 2nd-pipeline probe routed — there is no candidate second witness).

4. **Per-mode post-processing readout loop** (`:425-471`) — `for (int i = 0; i < num_conv; i++)`. This is the only loop in the driver, and it is a **readout map over the already-converged set**, NOT a solve loop:
   - `eigen->GetEigenvalue(i)` (`:427`) + eigenvalue→ω map (`:436` `omega = sqrt(omega)` linear EVP / `:441` `omega /= 1i` quadratic) — extraction from the single opaque solve + solver-specific scalar map. Not a solve.
   - `eigen->GetEigenvector(i)` (`:445`) — extraction.
   - `NormalizePhase(comm, E)` (`:445`, `palace/linalg/vector.hpp:298-303`) — `x *= conj(mean)/abs(mean)`, a phase-gauge fix. Eigenmode-specific scalar arithmetic; NOT shared spine vocabulary.
   - `Curl.Mult(E.Real/Imag, B.Real/Imag)` (`:447-448`) + `B *= -1/(iω)` (`:450`) — the `B`-from-`E` recovery. This is `apply_linop(Curl)` then a scalar scale — **already firm L3 `apply_linop` vocabulary**, and shared identically with the driven driver (`drivensolver.cpp:205-206, 329-330, 461-462`). Not new.
   - `post_op.MeasureAndPrintAll(...)` (`:458`) — the `PostOperator<EIGENMODE>` measurement entry, **shared across ALL 5 pipelines** (eigenmode `:458`, driven `drivensolver.cpp:216/470`, magnetostatic `magnetostaticsolver.cpp:92`, electrostatic `electrostaticsolver.cpp:82`, transient `transientsolver.cpp:104`, boundarymode `boundarymodesolver.cpp:314`). A uniform shared post-processing surface, not eigenmode-specific spine.
   - `AddEstimate(...)` → `ErrorIndicator::AddIndicator` (`:458` consumer; `palace/fem/errorindicator.cpp:11-47`) — an **RMS-running-average reduction** `eₖ = √(1/N ∑ₙ ηₖₙ²)` folding per-mode error indicators into one accumulated `indicator`. This IS a genuine `fold`, but it is (a) a **post-processing error-estimate reduction over an already-solved set**, not a *solve* fold (no operator threading, no per-element solve — different altitude than `fold_solve`, whose carry is a field-state advanced by an opaque per-step solve), and (b) **pipeline-generic infrastructure** in `palace/fem/`, consumed identically by every driver. It is not eigenmode-specific OUTER-machinery vocabulary.

**Combinator-witness classification (per `disciplined-cross-pipeline-combinator-mining-gate`):**

- **`solve_family` (map) witness?** NO. `solve_family` requires a fixed operator captured once + a `map` of the `ksp_solve` cap over an RHS/index family producing a *solution family by independent solves* (`L4/solve_family.md:40-41`, the map-combinator signature; the `operator-capture = fixed` load-bearing axis at `:137`). The eigenmode driver calls `Solve()` **once**; the per-mode loop solves nothing (it reads out an already-converged set). There is no per-element solve and no RHS family. The post-mode loop is a *readout* map, not a *solve* map — it does not instantiate `map (ksp_solve op)`.
- **`fold_solve` (fold) witness?** NO at the solve altitude. `fold_solve` requires a field-state carry threaded through a schedule, each step's input the prior step's output, advanced by an opaque per-step *solve* operator (`L4/fold_solve.md:20, 27`). The eigenmode driver has no such state-threaded solve march. The two fold-shaped things present — (i) the HYBRID `Solve → QN-refine → Solve` handoff, (ii) the `AddIndicator` RMS reduction — are at different altitudes (a two-phase cap re-application; a post-processing estimate reduction), neither a schedule-of-solves carry-fold.
- **Scope-boundary / break-witness?** The eigenmode pipeline does not break any mined combinator's load-bearing invariant; it simply does not exhibit the shape at all (no family, no solve-march). Per gate step 2, "does not exhibit" is distinct from "breaks the invariant" — eigenmode is neither a positive witness nor a scope-boundary break-witness for `solve_family`/`fold_solve`; it is OUT of the family-solve / fold-solve domain entirely (one opaque solve → readout post-processing).

## Recommendation

**Defer — record spine-complete; no future landing licensed.** The eigenmode pipeline OUTER machinery introduces no new cleanly-describable shared spine vocabulary beyond the already-firm `eigsolve` chain (`L1`→`L2`→`L3` `partial-obstruction`→`L4` cap) and the already-shared post-processing infrastructure (`apply_linop(Curl)`, `PostOperator::MeasureAndPrintAll`, `ErrorIndicator::AddIndicator`). This is the redirect's "what a solver can't cleanly say is a finding about the spine" inverted into the positive case: the eigenmode solver says everything it needs in existing vocabulary, so it advances no layer and forces no spine. Concrete consequences for the plan:

- **Close the `solve_family` §Status "eigenmode … unprobed" item** (`L4/solve_family.md:146`) and the `fold_solve` implicit eigenmode-coverage gap: eigenmode is confirmed NEITHER a `solve_family` map witness NOR a `fold_solve` fold witness. An integrator may surgically update the `solve_family` §Status scope note from "transient and eigenmode are unprobed" to "transient … unprobed; eigenmode probed (cycle-059) — NOT a witness (single opaque solve, no family)". (Proposed-changes block below; for `integrator-per-report` to apply — I do NOT touch `book/`.)
- **No new combinator dispatch warranted** for eigenmode OUTER machinery. The HYBRID two-phase refinement is a single intra-pipeline witness (gate step 1: spine-coverage finding, not mineable) and is already cap-covered.

## Proposed changes

Surgical `solve_family` §Status scope-note update (one sentence), for `integrator-per-report` to apply in Phase 5. NOT applied by me (dispatch-phase write-authority partition).

In `book/src/L4/solve_family.md`, §Status, the "Scope (load-bearing)" paragraph (`solve_family.md:146`) contains, mid-paragraph, the clause:

> **transient** and **eigenmode** are unprobed.

(The paragraph continues past this clause with "Do NOT claim cross-pipeline generality… The general superset is **batch-17 future work** (OQ …)…" — the clause is NOT paragraph-final; this is an in-place clause replacement, not a paragraph-terminal append.)

Replace the exact clause "**transient** and **eigenmode** are unprobed" (the rest of the paragraph is unchanged) with:

> **transient** is unprobed (the canonical `fold` candidate, now homed at [`fold_solve`](./fold_solve.md)); **eigenmode** was probed (cycle-059 cross-layer-cross-cutter, `reports/2026-06-02T061737Z-cross-layer-cross-cutter-eigenmode-outer-machinery-probe/CYCLE.md`) and is **NOT a witness** of either `solve_family` or `fold_solve` — the eigenmode driver calls the opaque `eigen->Solve()` once (`eigensolver.cpp:367`), with no operator/RHS family to map and no state-threaded solve-march to fold; its only outer loop is a post-processing *readout* map over the already-converged eigenpair set (`eigensolver.cpp:425-471`).

(If the integrator judges this stale-by-batch — `fold_solve` already landed transient as its witness — the transient half may be trimmed; the load-bearing addition is the eigenmode no-witness record.)

## Supporting evidence

L0 (codemap `read_range`-verified this dispatch against on-disk `reference/palace/`):

- `palace/drivers/eigensolver.cpp:32-477` — `EigenSolver::Solve`, the full OUTER machinery.
  - `:184-202` `SetOperators` / `:226` `SetBMat` / `:237` `SetDivFreeProjector` / `:269` `SetInitialSpace` / `:288,305` `SetShiftInvert` / `:291,308` `SetWhichEigenpairs` / `:351` `SetLinearSolver` — the construction-bound `OpParams` config (absorbed by the cap).
  - `:367` `int num_conv = eigen->Solve()` — the SINGLE opaque eigen-solve (the capped obstruction).
  - `:377-406` HYBRID `QuasiNewtonSolver` refinement (`:379-381` constructed from prior `eigen` via `std::move` + `num_conv` seed; `:404` second `Solve()`) — sequential two-phase refine, single-witness, cap-re-application altitude.
  - `:425-471` `for (i < num_conv)` post-processing readout map; `:427` `GetEigenvalue(i)`; `:436/441` ω-map; `:445` `GetEigenvector(i)` + `NormalizePhase`; `:447-450` `Curl.Mult` + `B *= -1/(iω)` (`apply_linop(Curl)`); `:458` `MeasureAndPrintAll` + `AddEstimate`; `:469` `MeasureFinalize`.
- `palace/linalg/vector.hpp:298-303` — `NormalizePhase`: `x *= conj(mean)/abs(mean)` (eigenmode-specific gauge fix scalar arithmetic).
- `palace/fem/errorindicator.cpp:11-47` — `ErrorIndicator::AddIndicator`: RMS running-average reduction `eₖ = √(1/N ∑ₙ ηₖₙ²)` (pipeline-generic post-processing fold; NOT a solve-fold).
- Shared-surface confirmation (codemap `search_text`): `MeasureAndPrintAll` in eigenmode `:458`, driven `drivensolver.cpp:216/470`, magnetostatic `magnetostaticsolver.cpp:92`, electrostatic `electrostaticsolver.cpp:82`, transient `transientsolver.cpp:104`, boundarymode `boundarymodesolver.cpp:314`; `Curl.Mult(E,B)` in eigenmode `:447-448`, driven `:205-206/329-330/461-462`.

Artifact (firm chain this probe sits above):

- `book/src/L4/eigsolve.md` — the firm opaque-iteration cap (`eigen_iterate` role-named obstruction marker; §Signature `OpParams` absorbs the driver-level config).
- `book/src/L3/eigsolve.md` — the `partial-obstruction` parent (body lifts, loop opaque-library-owned; single `EPSSolve`/`naupd`).
- `book/src/L4/solve_family.md:33,40-41` (the map combinator: named at `:33`, signature `solve_family op rhss = map (\inp -> ksp_solve op inp) rhss` at `:40-41`) + `:146` (the §Status "eigenmode unprobed" item this probe closes). (`:137` is variant-axis-1 `operator-capture`, not the map combinator.)
- `book/src/L4/fold_solve.md:20,27` — the fold combinator (transient/driven-PROM witnesses) eigenmode is confirmed NOT to join.
- `skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md` — the witness-count / scope-boundary / map-vs-fold gate applied above (no shape cleared the bar; eigenmode is out-of-domain, not a positive witness or a break-witness).

## Open questions / caveats

- The HYBRID two-phase refinement (`:377-406`) is the only OUTER-machinery shape with any combinator flavor, and it is single-witness within eigenmode with no second-pipeline candidate. If a future pipeline surfaces a "solve → refine-with-second-solver" shape, it could be re-probed as a `refine_solve` candidate — but there is no such second witness today, so this is a non-actionable note, not a routed probe. (Routed as an OQ-ledger intake entry, not a plan item.)
- The eigenvalue→frequency map (`:436/441`) and Q-factor are eigenmode-specific scalar post-processing; they were checked and are NOT shared spine vocabulary (no other pipeline computes them). Recorded as solver-specific, consistent with the redirect's "solvers advance a layer only when cleanly describable in EXISTING shared vocabulary" — these are not, and correctly stay solver-internal.
- This probe did NOT re-audit the per-mode `MeasureAndPrintAll` measurement internals (the `PostOperator` surface) — that is a separate shared-infrastructure surface, out of this OUTER-machinery scope; flagged only as already-shared, not characterized.
