---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-02T07:57:39Z
scope: driven↔transient OUTER machinery — beyond-the-solve-loop spine-vocabulary probe (redirect solver-test-load item-3)
status: pending
integrated_at: 2026-06-02T082437Z
integration_commit: 018eea5
integration_notes: "Applied cycle-061 (D3; batch-19 position 1/3). Observation-only cross-layer-cross-cutter probe — NO book/ mutation (§Proposed-changes None for book/). Verdict: ONE batch-19 LICENSE-FUTURE candidate assemble_frequency_operator (the operator-domain image of the firm tensor-domain linear_combination; the driven per-ω A=(a0·K+a1·C+a2·M+A2) scalar-weighted sum of fixed operators, drivensolver.cpp:176-177 -> spaceoperator.cpp:522-528 BuildParSumOperator -> rap.cpp:780-786; single positive witness, driven-only, low-priority pull-gated; anti-mirror disposition = extend the EXISTING firm L3/linear_combination operand-category axis rather than mint a new slug, so no stub owed) + Regions 2/3/4 (transient coefficient setup, both pipelines' RHS/excitation eval, both pipelines' post-step field collection) RECORDED spine-complete-or-solver-specific. Both c061 D3 OQ-ledger intake entries (driven-affine-frequency-operator-as-operator-valued-linear-combination :821 with the map_solve scope-boundary sharpening + driven-transient-outer-machinery-spine-complete-except-affine-operator-assembly :822) pre-appended by the dispatch agent; verified present, NOT duplicated. citecheck --scan 26 ok/3 AMBIG (all fold_solve.md bare-basename in prose, resolve unambiguously to L4/fold_solve.md by context; observation-only, nothing ambiguous lands; non-blocking). No build change. Two-phase SHA patch to follow."
---

# CYCLE: Cross-layer observation — driven/transient outer machinery beyond the characterized solve loops

## Summary

Probing the driven + transient pipelines' OUTER machinery beyond the already-characterized solve-loop shapes (`map_solve` single-witness, `SweepAdaptive` = `fold_solve` 2nd witness, transient time-march = `fold_solve` primary witness), I find **one cleanly-describable SHARED spine-vocabulary candidate** and three regions that are **solver-specific arithmetic / per-pipeline postprocessing** (spine-findings, not mineable). The shared candidate is the driven per-ω **operator assembly** `A = (a0·K + a1·C + a2·M + A2)` (`drivensolver.cpp:176-177`), which bottoms out in `SpaceOperator::GetSystemMatrix` → `BuildParSumOperator({a0,a1,a2,1},{K,C,M,A2})` (`spaceoperator.cpp:522-528`) → `sum->AddOperator(ops[i], coeff[i])` (`rap.cpp:780-786`): a **scalar-weighted sum of fixed operators** — structurally the existing firm `linear_combination` fold, but lifted from the **vector/tensor operand domain** to the **operator operand domain**. I **LICENSE a future landing** of this as an `assemble_frequency_operator` specialization note re-expressing through an **operator-valued `linear_combination`** — but flag it as a **single positive witness** under the disciplined-mining gate (driven only), so it is a coverage-finding routed for a 2nd-pipeline probe, NOT a mine-now. The transient coefficient setup, both pipelines' RHS/excitation evaluation, and both pipelines' post-step field collection are **solver-specific or already-spine-covered** — recorded as spine-complete-or-solver-specific.

## Observation kind

**Coverage gap** (latent shared vocabulary): the operator-valued scalar-weighted-sum shape (`BuildParSumOperator`) recurs in the driven outer machinery and is the operator-domain analog of the firm tensor-domain `linear_combination` fold — currently NOT named anywhere in the spec's operator vocabulary, and the driven `A`-assembly's L1>L0 / L2 home is unwritten. Secondarily an **edge classification** of the other three machinery regions as solver-specific (spine-finding).

## Specific finding

I examined four OUTER-machinery regions (the brief's enumerated targets), each verified against on-disk source via codemap `read_range`:

### Region 1 — driven per-ω operator assembly `A = (K + iωC − ω²M + A2)` — SHARED-VOCABULARY CANDIDATE (single witness)

`drivensolver.cpp:176-177`:
```
auto A = space_op.GetSystemMatrix(1.0 + 0.0i, 1i * omega, -omega * omega + 0.0i,
                                  K.get(), C.get(), M.get(), A2.get());
```
`GetSystemMatrix` (`spaceoperator.cpp:522-528`) is a one-line forward to `BuildParSumOperator({a0, a1, a2, 1}, {K, C, M, A2})`, whose body (`rap.cpp:765-786`) is:
```
auto sum = std::make_unique<SumOperator>(...);
for (i ...) if (ops[i] && coeff[i] != 0) sum->AddOperator(ops[i]->LocalOperator(), coeff[i]);
```
This is **exactly the `linear_combination` fold** `Σᵢ aᵢ·tᵢ` — `foldl (\acc (a,op) -> acc + scal a op) (zeros) pairs` — but with the operands being **fixed operators** (`ParOperator`: `K`/`C`/`M`/`A2`) rather than tensors/vectors. The fixed operators `K`/`C`/`M` are assembled **once, before the frequency loop** (`drivensolver.cpp:92-94` `GetStiffnessMatrix`/`GetDampingMatrix`/`GetMassMatrix`); only the **scalar coefficients are ω-dependent** (`1`, `iω`, `−ω²`). So the per-ω assembly is a genuine **affine-in-ω operator family**: a fixed operator basis `{K, C, M}` (+ the ω-dependent `A2` extra term, `drivensolver.cpp:174`) combined under ω-varying scalar weights, evaluated fresh each ω inside the `solve` loop.

Two structural observations relevant to the existing spine:

1. **This is the operator-domain image of the firm `linear_combination`** (`L3/linear_combination.md`, `L2/linear_combination.md`, firm; the BLAS-1 `scal`/`axpy`/`axpby`/`axpbypcz` family unify through it). The existing entry's signature is `[(Scalar, Tensor[N])] -> Tensor[N]`; the driven assembly is `[(Scalar, Operator)] -> Operator`. Same fold skeleton (scalar-weighted variadic sum, empty→zero, the `coeff != 0` sparsity prune is a transparent optimization of the fold), different operand category. This is **not a rename** of `linear_combination` — it is a genuine vocabulary extension: the operand monoid is operator-addition / scalar-operator-scaling, not tensor-addition. It would serve as the clean L1>L0 home for what is currently an unwritten driven-assembly region, and the `assemble_frequency_operator` name in the brief is a faithful specialization label (one ω → one summed operator).

2. **It is the per-element operator rebuild that scopes `map_solve` out of `solve_family`.** `solve_family.md:65,90,163` already records the driven per-ω `SetOperators`-inside-the-loop as the scope boundary (the `map_solve_over_(operator,rhs)_family` superset). This finding NAMES what that rebuild *is*: an operator-valued `linear_combination` over a fixed `{K,C,M}` basis with ω-varying coefficients. That is a useful sharpening — the `map_solve` superset's per-element operator is not arbitrary; it is an affine-operator-family evaluation, which is cleanly describable.

**Witness count: ONE (driven only).** Under `disciplined-cross-pipeline-combinator-mining-gate` step 1, a single witness is a SPINE-COVERAGE FINDING, not a mineable cross-pipeline combinator. BUT — and this is the disposition nuance — the *shape itself* (`BuildParSumOperator`) is **already firm at the tensor-operand layer** as `linear_combination`; the operator-operand extension is a vocabulary lift of an existing firm fold, not a from-scratch cross-pipeline mine. The honest classification: the **operator-valued `linear_combination` fold is cleanly-describable shared vocabulary** (it factors cleanly, the operand-category is the variant axis), and `assemble_frequency_operator` is its **single-pipeline specialization** (driven). I do NOT force a cross-pipeline generality claim on the *specialization* (only driven assembles an affine-ω operator); I DO observe the *fold* is shared with the firm BLAS-1 cohort by operand-category extension.

### Region 2 — driven post-sweep result collection / S-parameter / port postprocessing — SOLVER-SPECIFIC (spine-finding)

Per ω the driven loop does field recovery + measurement: `B = -1/(iω) ∇×E` via `Curl.Mult` (`drivensolver.cpp:205-206`, with `B *= -1/(iω)` at `:207`), an optional Floquet correction `floquet_corr->AddMult` (`:212`), then `post_op.MeasureAndPrintAll(excitation_idx, omega_i, E, B, omega)` (`:216`) and `AddEstimate` error-indicator accumulation (`:220`). The S-parameter / port-quantity reduction lives inside `PostOperator::MeasureAndPrintAll`. This is **per-pipeline measurement arithmetic** (the `B = curl E / iω` recovery is driven-specific complex-frequency-domain physics; the port S-parameters are a driven-only readout). It is the per-element *consumer* of the `map_solve` result family — already accounted for in the spine model as "the per-element post-processing chain … a lowering-and-consumer concern, not combinator structure" (`solve_family.md:111`, the analogous electrostatic/magnetostatic note). **Not shared spine vocabulary**; it is solver-specific postprocessing. Spine-finding: what the driven postprocess can't cleanly say in shared vocabulary (S-parameters, complex-frequency curl recovery) is a finding that these are genuinely driven-specific, not a missing combinator.

### Region 3 — transient time-integration coefficient setup + per-step excitation (RHS) evaluation — SOLVER-SPECIFIC / ALREADY-SPINE-COVERED (spine-finding)

The transient coefficient setup is `delta_t = iodata.solver.transient.delta_t` (`transientsolver.cpp:35`) + `n_step = config::GetNumSteps(0, max_t, delta_t)` (`:36`) — this is exactly the `fold_solve` **fixed-list `[Time]` schedule** construction already recorded as the default surface (`fold_solve.md:63,113`, the `schedule-source: fixed-list` axis). No new vocabulary. The per-step excitation is the time-dependent source `J_coef = GetTimeExcitation(false)` / `dJdt_coef = GetTimeExcitation(true)` (`transientsolver.cpp:30-31`), with `dJdt_coef` captured **once into the `TimeOperator` at construction** (`:33`) — i.e. it is absorbed into the `op : OpParams` stratum the `fold_solve` entry already quantifies over (`fold_solve.md:61`). `J_coef(t)` is evaluated per-step only as a postprocessing *input* (`:104` `MeasureAndPrintAll(step, E, B, t, J_coef(t))`), not as a re-assembled operator. So the transient RHS/excitation is **already inside the `fold_solve` op-capture-once stratum** — no new spine vocabulary; the time-excitation closure is solver-specific physics absorbed into `OpParams`. Spine-finding: transient's RHS handling is *more degenerate* than driven's (the excitation is baked into the captured operator, not rebuilt per step), so there is no per-step assembly analog to Region 1 here.

### Region 4 — transient post-march field collection / reduction — ALREADY-SPINE-COVERED

Per step: `E = time_op.GetE()` (`transientsolver.cpp:98`), `B = time_op.GetB()` (`:99`), then `MeasureAndPrintAll` (`:104`) + `AddEstimate`. This is the per-step trajectory consumption already recorded at `fold_solve.md:64,90,113` (the demand-pruning §, "transient DOES consume each step's (E,B) for postprocessing"). No new vocabulary; the field readout is the `TimeState` carry's per-step observation. Solver-specific measurement, spine-covered as the fold's consumed trajectory.

## Recommendation

**LICENSE a future landing (batch-19, low-priority, pull-gated)** of the **operator-valued `linear_combination`** vocabulary + its `assemble_frequency_operator` driven specialization:

- Dispatch a **harvester** (or combinator-miner replace-and-propagate pass) on the driven per-ω assembly to land `assemble_frequency_operator` as an **L1 operator** (the affine-ω fixed-basis operator combination, `drivensolver.cpp:176-177` + `spaceoperator.cpp:522-528` + `rap.cpp:765-786`) with an **L1>L0 theme** narrating `GetSystemMatrix`/`BuildParSumOperator` → the scalar-weighted operator sum. Re-express it **through** the existing `linear_combination` fold by extending that combinator's operand-category variant axis (`tensor-operand | operator-operand`) — replace-and-propagate, NOT a new mirrored fold. Witness count for the *fold* is strong (the tensor-operand form is firm BLAS-1; this is the operator-operand extension); witness count for the *driven specialization* is ONE — so land it as a single-pipeline specialization note, with the explicit caveat that no other pipeline assembles an affine-operator family (transient bakes the excitation into the captured op; electrostatic/magnetostatic capture a single fixed `K`).

- This is **pull-gated** per the redirect's solver-test-load discipline: it advances the spine only because it is cleanly describable in existing (`linear_combination`) vocabulary. If a future FE-assembly / `weak_form_term` cohort dispatch (the batch-19 lead) pulls on the operator-sum vocabulary, this lands alongside it; otherwise it is low priority.

**RECORD as spine-complete-or-solver-specific** Regions 2, 3, 4: the driven S-parameter/port postprocessing (solver-specific physics), the transient coefficient/excitation setup (absorbed into the `fold_solve` op-capture-once stratum + the fixed-`[Time]` schedule), and the transient post-march collection (the `fold_solve` consumed trajectory). No new shared spine vocabulary in these regions — what they can't say in shared vocabulary is genuinely solver-specific, not a missing combinator.

## Supporting evidence

- **Driven per-ω assembly (Region 1, the candidate):**
  - `palace/drivers/drivensolver.cpp:92-94` — fixed operators `K`/`C`/`M` assembled ONCE before the loop (`GetStiffnessMatrix`/`GetDampingMatrix`/`GetMassMatrix`).
  - `palace/drivers/drivensolver.cpp:174` — `A2 = space_op.GetExtraSystemMatrix<ComplexOperator>(omega, ...)` (the ω-dependent extra term).
  - `palace/drivers/drivensolver.cpp:176-177` — `A = space_op.GetSystemMatrix(1+0i, iω, −ω²+0i, K, C, M, A2)` (the per-ω affine combination, INSIDE the loop).
  - `palace/drivers/drivensolver.cpp:180` — `ksp.SetOperators(*A, *P)` (the per-element operator capture = the `map_solve` scope boundary).
  - `palace/models/spaceoperator.cpp:522-528` — `GetSystemMatrix` ≡ `BuildParSumOperator({a0,a1,a2,1}, {K,C,M,A2})`.
  - `palace/linalg/rap.cpp:765-786` — `BuildParSumOperator` body: `SumOperator` + `sum->AddOperator(ops[i]->LocalOperator(), coeff[i])` for `coeff[i] != 0` (the scalar-weighted operator fold; the `!= 0` sparsity prune).
- **Firm tensor-operand `linear_combination` (the shape this extends):**
  - `book/src/L3/linear_combination.md:34-37` — `linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]` = `foldl (\acc (a,t) -> acc + scal a t) (zeros N) pairs`.
  - `book/src/L2/linear_combination.md` (firm L2 fold), `L3/linear_combination.md:50-59` (the `scal`/`axpy`/`axpby`/`axpbypcz` arity specializations through it).
- **`map_solve` scope-boundary already records the per-ω rebuild (this finding names it):**
  - `book/src/L4/solve_family.md:65,90,137,163` — driven's per-element operator rebuild as the `map_solve_over_(operator,rhs)_family` superset scope boundary.
- **Region 2 — driven postprocessing (solver-specific):**
  - `palace/drivers/drivensolver.cpp:205-206` (`B = -1/(iω) Curl·E`, `Curl.Mult` calls; `B *= -1/(iω)` at `:207`), `:212` (Floquet `AddMult`), `:216` (`MeasureAndPrintAll`), `:220` (`AddEstimate`), `:232` (`MeasureFinalize`).
- **Region 3 — transient coefficient/excitation (spine-covered):**
  - `palace/drivers/transientsolver.cpp:30-31` (`J_coef`/`dJdt_coef = GetTimeExcitation`), `:33` (`dJdt_coef` captured into `TimeOperator`), `:35-36` (`delta_t` + `n_step` = the fixed `[Time]` schedule), `:104` (`J_coef(t)` per-step postprocess input only).
  - `book/src/L4/fold_solve.md:61,63,113` (op-capture-once stratum + `schedule-source: fixed-list` default surface).
- **Region 4 — transient post-march collection (spine-covered):**
  - `palace/drivers/transientsolver.cpp:98-99` (`GetE`/`GetB`), `:104` (`MeasureAndPrintAll`).
  - `book/src/L4/fold_solve.md:64,90` (consumed-trajectory demand-pruning §).
- **Mining-gate skill cited:** `skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md` (step 1 single-witness → coverage-finding-not-mine; step 2 break-witness scope-boundary; applied to classify the `assemble_frequency_operator` specialization as single-pipeline, the underlying fold as operand-category-extended firm vocabulary).

## Open questions / caveats

- **Operand-category extension vs. new entry:** the operator-valued `linear_combination` should be landed as an operand-category variant axis on the EXISTING firm `linear_combination` (replace-and-propagate, avoid a mirrored fold), NOT a separate `operator_linear_combination` chapter — the 2026-06-01 anti-mirror principle. A harvester landing `assemble_frequency_operator` must verify the operand monoid (operator-addition + scalar-operator-scaling) is a clean variant of the tensor monoid and not a semantically distinct fold (it appears clean: `SumOperator::AddOperator` is the operator-domain `axpy`-accumulate). Verify before authoring.
- **`A2` extra-term placement:** the 4th term `A2` carries coefficient `1` and is itself ω-dependent (`GetExtraSystemMatrix(omega)`), unlike the fixed `{K,C,M}` basis. So the affine-in-ω characterization is *almost* clean — `A2` is an ω-dependent operand, not an ω-dependent coefficient. A harvester should decide whether `A2` is (a) absorbed as a 4th basis operator with a coefficient-1 (the literal `BuildParSumOperator` shape) or (b) a non-affine correction noted separately. The literal source shape is (a); the "affine operator family" abstraction is (a) modulo the `A2` ω-dependence caveat.
- **Witness count for the specialization is permanently ONE** unless a future pipeline assembles an operator family — likely permanent (transient bakes excitation into the captured op; electro/magnetostatic capture a single fixed `K`; eigenmode is opaque-library `eigen->Solve`). So `assemble_frequency_operator` is a single-pipeline specialization by design — record it as such, do not route a 2nd-pipeline probe expecting a discharge (none will come). The *fold* generality comes from the tensor-operand BLAS-1 cohort, not from a 2nd assembly witness.
- **OQ-ledger intake appended** (append-only) naming `driven-affine-frequency-operator-as-operator-valued-linear-combination` for the batch-19 plan migration decision.

## Proposed-changes

None for `book/` this dispatch (observation-only, per D3 brief). The only write is the append-only OQ-ledger intake entry below (applied by this agent per the brief's explicit allowance; integrator need not re-apply).
