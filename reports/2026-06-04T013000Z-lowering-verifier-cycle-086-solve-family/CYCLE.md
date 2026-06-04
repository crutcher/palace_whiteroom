---
agent: lowering-verifier
invoked_at: 2026-06-04T013000Z
scope: L4 combinator law-confidence audit — solve_family (firm-on-positive-structure / list-homomorphism promotion pass)
status: integrated
integrated_at: 2026-06-04T015500Z
integration_commit: 7784b49
integration_notes: "Applied clean as D1 (cycle-086, batch-27 position 2/3). PROMOTED book/src/L4/solve_family.md rough-in (test-coverage-bounded) → firm via the firm-on-positive-structure / syntactic-identity escape (the c082/c083 route; element-independence read off const BaseKspSolver::Mult body ksp.cpp:297-310) + COUNT-OWNER L4/index.md per-operator cell + firm tally 16→17 (20→21 grand). L4 rough-in (test-coverage-bounded) 1→0 (solve_family was the sole entry). NO feature column flipped (electrostatic/magnetostatic stay seed on the remaining gram_reduce gate). Promoted durable OQ solve-family-firmed-discharges-one-of-two-electrostatic-magnetostatic-column-gates + the now-closed stale-evidence hygiene OQ. Build clean (cargo make book exit 0; no SUMMARY/dead-link change)."
inputs:
  - book/src/L4/solve_family.md (rough-in (test-coverage-bounded); 0 verified_against blocks)
  - reports/2026-06-04T000130Z-cycle-planner-cycle-086/CYCLE.md (D1 scope + codemap-confirmed anchors)
  - book/src/L4/sparameter_reduce.md §Status (the c082/c083 firm-on-positive-structure / syntactic-identity escape precedent)
  - palace/drivers/electrostaticsolver.cpp:28-92 (fixed-operator witness 1)
  - palace/drivers/magnetostaticsolver.cpp:28-100 (fixed-operator witness 2)
  - palace/linalg/ksp.cpp:297-310 + palace/linalg/ksp.hpp:46,71 (KspSolver::Mult — the no-cross-element-state decisive evidence)
  - palace/drivers/drivensolver.cpp:176-180 (per-element superset scope boundary, negative witness)
  - book/src/design/l4_calculus.md:150-184 (strawman §3.7 iterate_while family)
---

# CYCLE: Audit solve_family — firm-on-positive-structure law-confidence pass

## Summary

Audited `book/src/L4/solve_family.md` (`rough-in (test-coverage-bounded)`, 0 `verified_against:`
blocks) for the firm-on-positive-structure / list-homomorphism promotion route its §Status names.
**Verdict: fully-supported — the escape APPLIES; promote `solve_family` `rough-in
(test-coverage-bounded)` → `firm`.** The three load-bearing laws (concatenation-homomorphism,
operator-capture-once/`SetOperators`-hoist, element-independence/order-preservation) are all
**syntactic identities / closed-form structural read-offs of positive source**, not semantic
theorems the source only numerically asserts — the c082/c083 (`eigenfreq_qfactor_reduce`,
`sparameter_reduce`) situation, NOT the c080 (`matrix-weighted-norm`) situation. The ONE claim the
planner correctly flagged as the only thing integration-level-only coverage left test-unconfirmed —
*no hidden cross-element state in the reused `KspSolver`* — is **decisively discharged by reading the
positive `BaseKspSolver::Mult` body** (`palace/linalg/ksp.cpp:297-310`): `Mult` is `const`, writes
only its output vector, and its ONLY cross-call mutation is two `mutable int` monotone telemetry
counters (`ksp_mult++`, `ksp_mult_it += GetNumIterations()`) that never feed back into a solve. That
makes the no-cross-element-state property a syntactic read-off of positive source, exactly the
in-scope analog of the missing driver-level unit test. **Column-flip note (load-bearing): this
discharges ONLY ONE of the TWO own-constituent gates on the electrostatic/magnetostatic columns —
`gram_reduce` still gates them (convergently blocked on the `matrix-weighted-norm` √-cascade
NO-GO-HELD). I do NOT claim or schedule a column `status: seed` flip; that stays gated.** All 14
asserted anchors were independently confirmed exact on-disk via `tools/citecheck/citecheck.py
--anchor` (the no-drift mechanical proof; outputs pasted in §Supporting evidence).

## Per-citation audit

### Citation 1 — `palace/drivers/electrostaticsolver.cpp:35-36` (the SetOperators hoist, witness 1)
- **Theme claim**: `op` is captured once, outside the `map`; `SetOperators(*K,*K)` sits outside the
  `for` loop (law 2, the operator-capture-once/`SetOperators`-hoist).
- **Found**: `:35` `KspSolver ksp(iodata, laplace_op.GetH1Spaces());` then `:36`
  `ksp.SetOperators(*K, *K);` — both **before** the `:60` `for (const auto &[idx, data] :
  laplace_op.GetSources())` loop. `K = laplace_op.GetStiffnessMatrix()` assembled once at `:30`.
- **Verdict**: supports. `citecheck --anchor 'KspSolver ksp'` → line 35; `--anchor 'SetOperators'` →
  line 36; both exact on-disk.
- **Notes**: the hoist is read directly off positive source — there is no per-element `SetOperators`
  call inside the loop. This is law 2 verbatim.

### Citation 2 — `palace/drivers/electrostaticsolver.cpp:60` (the family-map loop)
- **Theme claim**: the combinator is `map (ksp_solve op)` over an RHS family; the per-element solve
  writes into the collected family slot (`solutions[i] ↔ rhss[i]`).
- **Found**: `:60` `for (... : laplace_op.GetSources())` (the terminal-boundary index family); per
  index `:68` `laplace_op.GetExcitationVector(idx, *K, V[step], RHS)` forms the per-index RHS, `:69`
  `ksp.Mult(RHS, V[step])` is the per-element solve writing into `V[step]`; `:46` `std::vector<Vector>
  V(n_step)` is the pre-sized family storage; `:89` `step++` advances the collection.
- **Verdict**: supports. All anchors (`GetSources`@60, `GetExcitationVector`@68, `ksp.Mult`@69,
  `std::vector<Vector> V`@46, `step++`@89) confirmed exact via `citecheck --anchor`.
- **Notes**: the map-over-RHS-family shape (the combinator) is positively exhibited; the loop carries
  no inter-element accumulator (each iteration reads the shared `ksp` and `K`, writes its own `V[step]`).

### Citation 3 — `palace/drivers/magnetostaticsolver.cpp:35-36` (the SetOperators hoist, witness 2)
- **Theme claim**: a second structurally-identical fixed-operator witness with the same hoist.
- **Found**: `:35` `KspSolver ksp(iodata, curlcurl_op.GetNDSpaces(), &curlcurl_op.GetH1Spaces());`,
  `:36` `ksp.SetOperators(*K, *K);` — both outside the `:66` `for (... :
  curlcurl_op.GetSurfaceCurrentOp())` loop. `K = curlcurl_op.GetStiffnessMatrix()` once at `:30`.
  Per-index `:76` `GetExcitationVector(idx, RHS)`, `:77` `ksp.Mult(RHS, A[step])`; `:47`
  `std::vector<Vector> A(n_step)`; `:99` `step++`.
- **Verdict**: supports. All anchors confirmed exact via `citecheck --anchor` (incl. the loop at `:66`
  — `GetSurfaceCurrentOp`@66, NOT the `:60` of electrostatic; the theme's §Semantics line 76 already
  states the magnetostatic loop is `:66`, correct).
- **Notes**: byte-identical hoist shape to electrostatic. The two witnesses are structurally identical
  down to the `GetStiffnessMatrix()` / `SetOperators(*K,*K)`-outside-the-loop / `std::vector<Vector>`
  collect shape, differing only in the absorbed family-index domain (terminal vs surface-current) and
  RHS-construction call.

### Citation 4 — `palace/linalg/ksp.cpp:297-310` (`BaseKspSolver::Mult` — THE decisive no-cross-element-state evidence)
- **Theme claim**: element-independence (law 3) — `x_i` depends only on `(op, rhs_i)`; the underlying
  solves commute; no cross-element threading / no shared mutable state between solves. This is the
  claim the planner flagged as the one thing integration-level coverage left test-unconfirmed.
- **Found**: `void BaseKspSolver<OperType>::Mult(const VecType &x, VecType &y) const` (`:297`, `const`
  method). Body: `ksp->Mult(x, y)` (`:300`, writes ONLY output `y` from input `x`), a non-convergence
  warning branch, then `ksp_mult++` (`:308`) and `ksp_mult_it += ksp->GetNumIterations()` (`:309`).
  Close-brace `:310`. The two incremented members are declared `mutable int ksp_mult, ksp_mult_it;`
  (`ksp.hpp:46`) with the comment "Counters for number of calls to Mult method for linear solves, and
  cumulative number of iterations."
- **Verdict**: supports — decisively. The ONLY cross-call mutable state in the reused `KspSolver` is
  two **monotone telemetry counters** (call-count and cumulative-iteration-count). They are pure
  observability accumulators: they are written but never read by the solve, and they do not feed back
  into `ksp->Mult`. Therefore reordering, splitting, or chunking the RHS family changes only the order
  in which those two counters increment (to the same final totals) and **cannot change any `V[step]` /
  `A[step]` numerical result**. The no-hidden-cross-element-state property is read directly off the
  positive `Mult` body — a syntactic/structural fact, NOT a property the source only numerically asserts.
- **Notes**: THIS is the audit's pivotal finding. The planner's open question ("does the
  strawman-derivation + the positive `SetOperators`-hoist source discharge the no-cross-element-state
  claim") is answered YES, and not merely by the hoist — by the `Mult` body itself. The
  `solve_family.md:144` hedge ("the load-bearing claim the law encodes — that each element's solve is
  genuinely independent given the shared `op` (no hidden cross-element state in the `KspSolver` reuse)
  — is the part that the integration-level-only coverage leaves test-unconfirmed") is now resolved by
  positive source and is removed in the §Status re-narration.

### Citation 5 — `palace/linalg/ksp.hpp:46` (the `mutable int` counters declaration)
- **Theme claim**: corroborates Citation 4 — the only cross-call state is telemetry.
- **Found**: `mutable int ksp_mult, ksp_mult_it;` with the "Counters for number of calls … cumulative
  number of iterations" comment.
- **Verdict**: supports. `citecheck --anchor 'mutable int ksp_mult'` → line 46, exact.
- **Notes**: the `mutable` qualifier is precisely why `Mult` can be `const` while still bumping the
  counters; it confirms the counters are observability, deliberately excluded from logical const-ness.

### Citation 6 — `book/src/design/l4_calculus.md:150-184` (strawman §3.7 iterate_while family)
- **Theme claim**: `solve_family` is the pure-map degenerate of the §3.7 `iterate_while` family; the
  concatenation-homomorphism (law 1) is the standard `map` list-homomorphism specialized to it.
- **Found**: §3.7 `iterate_while` + `iterate_while_pure` sugar (anchor `iterate_while` resolves at
  lines 150,155,162,179,182 within the range). The degenerate-form rendering in `solve_family.md`
  §Signature (`:45-54`) faithfully instantiates this: carry `{remaining, solutions}`, predicate `not
  (null st.remaining)`, per-element extra = the solution, trajectory = the collected family.
- **Verdict**: supports. The concatenation-homomorphism `map f (a ++ b) = map f a ++ map f b` is the
  defining list-homomorphism of `map`, a syntactic identity in the strawman algebra; specialized to the
  fixed-`op` family it is law 1.
- **Notes**: this is the "strawman-derivation route" the §Status named as the more-likely promotion
  path. It holds — the map is a standard total list combinator.

### Citation 7 — `book/src/L4/ksp_solve.md:38-40` (the firm cap the family maps over)
- **Theme claim**: `solve_family` consumes the firm `ksp_solve` cap as its mapped function.
- **Found**: `ksp_solve op inp = execState (solve_loop op inp) (initial_state inp)` (`:38-40`),
  `ksp_solve.md` firmness firm.
- **Verdict**: supports. The one consumed combinator is firm; the family map folds a firm primitive,
  so the A2-style structure-side gate (the folded primitive is firm) is discharged.
- **Notes**: parallel to the `sparameter_reduce` gate-b discharge (its folded `port_projection` is firm
  L1). Here the folded `ksp_solve` is firm L4.

### Citation 8 — `palace/drivers/drivensolver.cpp:176-180` (the per-element superset scope boundary, negative witness)
- **Theme claim**: driven is NOT an instance of `solve_family` — it rebuilds the operator per-ω
  (`SetOperators` inside the loop), so it witnesses the `per-element` superset, scoping the
  fixed-operator laws.
- **Found**: `:176` `GetSystemMatrix(...)` rebuilding the ω-dependent operator INSIDE the `:168`
  frequency loop; `:180` `ksp.SetOperators(*A, *P)` INSIDE the loop.
- **Verdict**: supports (as a negative/scope-boundary witness, exactly as the theme uses it). The hoist
  (law 2) and concatenation-homomorphism (law 1) are correctly scoped to `operator-capture = fixed`;
  driven's `per-element` operator is the documented exclusion.
- **Notes**: confirms the laws are NOT over-claimed across the operator-capture axis. `citecheck
  --anchor 'GetSystemMatrix'`@176, `'SetOperators'`@180 — both exact.

## Applicability conditions

The §Status promotion is conditional on the firm-on-positive-structure escape applying. The decisive
discriminator (per the c080 matrix-weighted-norm contrast) is: **are the laws syntactic identities on
positive source, or semantic theorems the source only numerically asserts?**

- **Condition A — concatenation-homomorphism (law 1) is a syntactic identity on `map`.**
  - **Verifiable**: yes, from strawman §3.7 (Citation 6). `map f (a++b) = map f a ++ map f b` is the
    defining list-homomorphism of `map`. No inner-product/positivity axiom is smuggled in.
  - **Counter-example?**: no.
- **Condition B — operator-capture-once/`SetOperators`-hoist (law 2) is read off positive source.**
  - **Verifiable**: yes, from both driver sweeps (Citations 1, 3). `SetOperators` is positively
    outside the loop in electrostatic and magnetostatic; positively inside the loop in driven
    (Citation 8, the scope boundary).
  - **Counter-example?**: no (driven is correctly the superset, not a counter-example to the
    fixed-operator law).
- **Condition C — element-independence (law 3) carries no hidden cross-element state (THE pivotal
  condition; the planner's open question).**
  - **Verifiable**: yes — and this is the audit's key positive finding. `BaseKspSolver::Mult`
    (Citation 4) is `const`, writes only its output vector, and mutates only two monotone telemetry
    counters that never feed the solve. The independence is a structural read-off of the positive
    `Mult` body, NOT a numerically-asserted property.
  - **Counter-example?**: no. I specifically looked for solver-internal solution caching / warm-start
    state carried between `Mult` calls; there is none in the `Mult` body (the only retained members
    touched are the telemetry counters).

**Contrast with c080 matrix-weighted-norm (escape INAPPLICABLE there):** its triangle /
Cauchy–Schwarz / parallelogram laws are theorems conditional on an inner-product structure
(SPD/Hermitian `B`) the L0 source only *numerically* asserts — a property no positive source line
establishes syntactically. **No such theorem-needing-proof exists in `solve_family`'s laws:** the
concatenation-homomorphism is `map`'s definitional list-homomorphism, the hoist is a literal
`SetOperators`-outside-the-loop placement, and element-independence is a literal `const`-`Mult`-with-
telemetry-only-state read-off. All three are positive-structure facts. The escape applies.

## Algebraic laws (cited)

- **Law 1 — concatenation-homomorphism** `solve_family op (a++b) = solve_family op a ++ solve_family op
  b`. **Holds on the operator signature?** Yes — `solve_family op = map (ksp_solve op)`, and `map`'s
  list-homomorphism is definitional (strawman §3.7). The fixed shared `op` makes every element's
  `ksp_solve op` the *same* function, so the map genuinely distributes over concatenation. Syntactic
  identity. ✔
- **Law 2 — operator-capture-once/`SetOperators`-hoist** `fresh_ksp op` invariant across the map,
  hoists out. **Holds?** Yes — positively witnessed by `SetOperators(*K,*K)` outside the loop in both
  fixed-operator sweeps (Citations 1, 3). Read off positive source. ✔
- **Law 3 — element-independence/order-preservation** `x_i` depends only on `(op, rhs_i)`; solves
  commute; collection preserves position. **Holds?** Yes — `BaseKspSolver::Mult` (Citation 4) is
  `const`, writes only its output, mutates only monotone telemetry counters. No solve-affecting
  cross-call state ⇒ independence is structural. ✔ (This is the law whose confidence was previously
  reduced; it is now positively discharged.)
- **Law 4 — empty-family degenerate** `solve_family op [] = []`. **Holds?** Yes (degenerate, total-
  definition; Palace excludes the empty family via `MFEM_VERIFY(n_step>0,…)` at `electrostaticsolver.cpp:42`
  / `magnetostaticsolver.cpp:42`, both confirmed). ✔
- **Do-not-hold laws** (distribution over operator composition; per-element law uniformity across the
  operator-capture axis; cross-element fusion; linearity of the residual-history readout) — all
  correctly catalogued as absences in the entry; none is required for the promotion and none is a
  semantic theorem the promotion would smuggle in. The "per-element law uniformity" non-law is exactly
  the driven scope boundary (Citation 8). ✔

## Proposed changes

Three edits to `book/src/L4/solve_family.md` ONLY (no consumer/feature files — that is D2's job):
(1) flip the frontmatter `firmness:` line; (2) re-narrate §Status to record the firm verdict and the
discharged no-cross-element-state claim; (3) append the fenced `verified_against:` block. The
`verified_against:` YAML was validated with `python3 -c "import yaml; yaml.safe_load(...)"` (clean
parse, 8 entries, no `note:` begins with a quote of either kind).

```edit:book/src/L4/solve_family.md
[replace the frontmatter firmness line]

OLD:
firmness: rough-in (test-coverage-bounded)

NEW:
firmness: firm
```

```edit:book/src/L4/solve_family.md
[replace the entire ## Status section body — from the "`rough-in (test-coverage-bounded)` —" paragraph through the end of the "This dispatch (cycle-055 D1) is the **L4 combinator firm-up** ..." paragraph — i.e. replace lines 144-148 inclusive. The "## Status" heading line itself (143) is retained; the "## L4 vs L3 distinction" heading that follows (150) is retained. Append the verified_against block immediately before the "## L4 vs L3 distinction" heading.]

OLD (the paragraph beginning "`rough-in (test-coverage-bounded)` — the combinator's"):
`rough-in (test-coverage-bounded)` — the combinator's **structural signature is well-anchored** at L0 (the input/output family shape, the operator-capture-once stratification, the variant axes are all witnessed by two structurally-identical fixed-operator driver sweeps: electrostatic `electrostaticsolver.cpp:30-90` + magnetostatic `magnetostaticsolver.cpp:30-100`). But the **algebraic-law confidence is reduced pending dedicated test coverage**: the load-bearing concatenation-homomorphism (law 1) and the hoist (law 2) are stated against the strawman §3.7 family and the map list-homomorphism algebra, *not* confirmed by a dedicated unit test — the `Solve(mesh)` drivers are integration-level, with no `test-*.cpp` exercising the outer sweep under `reference/palace/test/unit/`. Per CLAUDE.md §Methodology invariants ("Two rough-in qualifiers are first-class"), this is the `rough-in (test-coverage-bounded)` tier: the structure is firm but the *laws* are stated-but-test-unconfirmed (distinct from `partly-constructive`, which is firm-structure + a *constructed* sub-part). **Promotion route**: a dedicated test exercising the family-map's concatenation/independence laws at the `Solve(mesh)` entry point (out of project write-scope while no driver-level unit test exists), OR a literature/strawman-derivation harvester pass that raises the list-homomorphism law confidence to `ksp_solve`-equivalent (the map is a standard total list combinator, so the strawman-derivation route is the more likely one). NOTE the firm-on-positive-structure consideration: the concatenation-homomorphism *is* a syntactic identity on `map` (and the operator-capture-once hoist *is* read directly off the positive `SetOperators`-outside-the-loop source), which is an argument toward `firm`; but the load-bearing claim the law *encodes* — that each element's solve is genuinely independent given the shared `op` (no hidden cross-element state in the `KspSolver` reuse) — is the part that the integration-level-only coverage leaves test-unconfirmed, so this entry honors the planner default of `rough-in (test-coverage-bounded)` rather than `firm`. The default may be revisited by a batch-17 lowering-verifier pass confirming the `KspSolver`-reuse carries no cross-element state.

NEW (the firm re-narration):
`firm`. **Reasoning (firm-on-positive-structure / syntactic-identity escape, c086 lowering-verifier law-confidence pass):** the combinator's **structural signature is well-anchored** at L0 (the input/output family shape, the operator-capture-once stratification, the variant axes are all witnessed by two structurally-identical fixed-operator driver sweeps: electrostatic `electrostaticsolver.cpp:30-90` + magnetostatic `magnetostaticsolver.cpp:30-100`), AND **every load-bearing law is a syntactic identity / closed-form structural read-off of positive source** — the same escape that landed the sibling output-product verbs [`sparameter_reduce`](./sparameter_reduce.md) (c083) and [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) (c082) firm, NOT the c080 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) situation (whose norm-axiom laws are inner-product-structure theorems the L0 source only *numerically* asserts):

- **Law 1 (concatenation-homomorphism)** is the definitional list-homomorphism of `map` (strawman §3.7, `book/src/design/l4_calculus.md:150-184`) — `map f (a ++ b) = map f a ++ map f b` — specialized to the fixed shared `op`. A syntactic identity, not a numerically-asserted axiom.
- **Law 2 (operator-capture-once / `SetOperators`-hoist)** is read directly off the positive `SetOperators(*K,*K)`-outside-the-loop source (electrostatic `electrostaticsolver.cpp:35-36` outside the `:60` loop; magnetostatic `:35-36` outside the `:66` loop). The driven `SetOperators`-inside-the-loop site (`drivensolver.cpp:180`) is the *scope boundary*, not a counter-example.
- **Law 3 (element-independence / order-preservation)** — the one claim the prior `rough-in (test-coverage-bounded)` qualifier held on (that each element's solve is genuinely independent given the shared `op`, with no hidden cross-element state in the reused `KspSolver`) — is now **discharged by reading the positive `BaseKspSolver::Mult` body** (`palace/linalg/ksp.cpp:297-310`): `Mult` is `const`, its body `ksp->Mult(x, y)` writes ONLY its output vector `y` (the per-element slot `V[step]` / `A[step]`) from its input `x` (the per-element RHS), and its ONLY cross-call mutation is two `mutable int` MONOTONE TELEMETRY counters (`ksp_mult++` `:308`, `ksp_mult_it += GetNumIterations()` `:309`; declared `palace/linalg/ksp.hpp:46` "Counters for number of calls to Mult method … cumulative number of iterations") that never feed back into any solve. Reordering / splitting / chunking the RHS family changes only the order those telemetry counters increment (to identical totals) — it cannot change any numerical `V[step]` / `A[step]`. So the no-cross-element-state property is a **syntactic read-off of positive source**, the in-scope analog of the (out-of-scope) driver-level unit test.

The `Solve(mesh)` drivers remain integration-level (no `test-*.cpp` exercises the outer sweep under `reference/palace/test/unit/`), but per the firm-on-positive-structure escape (CLAUDE.md §Methodology invariants, the c082/c083 route) the absence of a dedicated test does NOT gate laws that are syntactic identities over fully-specified positive source. There is **no theorem-needing-proof** in any of `solve_family`'s laws (contrast the c080 `matrix-weighted-norm` triangle / Cauchy–Schwarz / parallelogram theorems): the hoist is a literal placement, the homomorphism is `map`'s definitional law, and the independence is a literal `const`-`Mult`-with-telemetry-only-state read-off. The entry therefore promotes from `rough-in (test-coverage-bounded)` to `firm` (c086 D1).

**Scope (load-bearing, UNCHANGED by this promotion)**: `solve_family` (fixed-operator) is witnessed by **electrostatic + magnetostatic ONLY** (2-of-5 pipelines). The other three: **driven** breaks shared-operator-capture (operator rebuilt per-frequency, `drivensolver.cpp:176-180`, `SetOperators` inside the loop) — it is a witness of the `per-element` superset `map_solve_over_(operator,rhs)_family`, NOT of `solve_family`. The per-ω operator driven rebuilds is the now-firm [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md) (the affine-in-ω fixed-basis operator family `A(ω)=K+iω·C−ω²·M+A2(ω)`, the operator-operand specialization of `linear_combination`); it is the named per-element operator of the `map_solve_over_(operator,rhs)_family` superset, and its existence sharpens (does not move) this scope boundary: driven's per-element operator is not arbitrary but a fixed-basis affine combination, yet it is still *per-element* (rebuilt inside the loop), which is exactly the `operator-capture = per-element` axis value that scopes driven out of the `fixed`-only `solve_family`. **transient** is unprobed (the canonical `fold` candidate, now homed at [`fold_solve`](./fold_solve.md)); **eigenmode** was probed (cycle-059 cross-layer-cross-cutter, `reports/2026-06-02T061737Z-cross-layer-cross-cutter-eigenmode-outer-machinery-probe/CYCLE.md`) and is **NOT a witness** of either `solve_family` or `fold_solve` — the eigenmode driver calls the opaque `eigen->Solve()` once (`eigensolver.cpp:367`), with no operator/RHS family to map and no state-threaded solve-march to fold; its only outer loop is a post-processing *readout* map over the already-converged eigenpair set (`eigensolver.cpp:425-471`). Do NOT claim cross-pipeline generality beyond the two fixed-operator witnesses. The general superset is **batch-17 future work** (OQ `solve-family-general-operator-rhs-superset-probe`), gated on a 3rd probe (confirm driven's per-ω rebuild is the only difference; check whether transient is a `map` or a stateful `fold`/`solve_loop` shape — a fold does NOT join this family).

**Column-gate note (load-bearing — this promotion does NOT flip a feature column).** Firming `solve_family` discharges only ONE of the TWO own-constituent gates on the [`electrostatic`](../feature/electrostatic.L4.md) + [`magnetostatic`](../feature/magnetostatic.L4.md) driver columns. The SECOND gate — [`gram_reduce`](./gram_reduce.md) (`rough-in (test-coverage-bounded)`, folding plain-`rough-in` [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + [`bilinear-form`](../L1/bilinear-form.md)) — remains, convergently blocked on the `matrix-weighted-norm` √-cascade NO-GO-HELD (c080 D1 ruled the firm-on-positive-structure escape INAPPLICABLE for `matrix-weighted-norm`). Those columns stay `status: seed` this cycle; the column flip is NOT claimed or scheduled by this dispatch.

This dispatch (cycle-086 D1) is the **L4 combinator firm-up** completing the batch-17 lowering-verifier law-confidence route the §Status (and the cycle-055 D1 landing) named — the firm-on-positive-structure / strawman-derivation pass that the rough-in qualifier reserved. The L4>L3 dissolution theme ([`L4-L3/solve-family-map-dissolution`](../L4-L3/solve-family-map-dissolution.md)) is unaffected (its substantive rotation is independent of this verb's law-confidence).

verified_against:

    verified_against:
      - citation: palace/drivers/electrostaticsolver.cpp:35-36
        verdict: supports
        audited_at: 2026-06-04T013000Z
        note: KspSolver ksp(...) built once (line 35) + ksp.SetOperators(*K,*K) (line 36), BOTH outside the line-60 for-loop. citecheck --anchor confirms KspSolver-ksp at 35, SetOperators at 36 on-disk. The operator-capture-once hoist (law 2) is read directly off positive source.
      - citation: palace/drivers/electrostaticsolver.cpp:60
        verdict: supports
        audited_at: 2026-06-04T013000Z
        note: for(const auto &[idx,data] - laplace_op.GetSources()) is the terminal-boundary family loop; ksp.Mult(RHS,V[step]) per-element solve at line 69; std::vector<Vector> V(n_step) at line 46; step++ collect at line 89. The map-over-RHS-family structure (the combinator shape) is positively exhibited.
      - citation: palace/drivers/magnetostaticsolver.cpp:35-36
        verdict: supports
        audited_at: 2026-06-04T013000Z
        note: KspSolver ksp(...) at line 35 + ksp.SetOperators(*K,*K) at line 36 OUTSIDE the line-66 GetSurfaceCurrentOp() loop, byte-identical hoist to electrostatic. ksp.Mult(RHS,A[step]) at line 77; std::vector<Vector> A(n_step) at line 47; step++ at line 99. Second structurally-identical witness of the fixed-operator map.
      - citation: palace/linalg/ksp.cpp:297-310
        verdict: supports
        audited_at: 2026-06-04T013000Z
        note: BaseKspSolver Mult def(line 297)+body+close-brace(line 310), DECISIVE for the element-independence law (law 3 / the no-cross-element-state claim the planner flagged test-unconfirmed). Mult is const; body is ksp->Mult(x,y) writing ONLY output y (the per-element slot V[step]/A[step]) from input x (per-element RHS); the ONLY cross-call mutation is ksp_mult++ (line 308) and ksp_mult_it += GetNumIterations() (line 309), two mutable-int MONOTONE TELEMETRY counters that do not feed back into any solve. The no-hidden-cross-element-state claim is therefore a SYNTACTIC read-off of positive source, not a numerically-asserted property, so the firm-on-positive-structure escape applies (the c082/c083 route, NOT the c080 matrix-weighted-norm norm-axiom situation).
      - citation: palace/linalg/ksp.hpp:46
        verdict: supports
        audited_at: 2026-06-04T013000Z
        note: mutable int ksp_mult, ksp_mult_it with the comment Counters-for-number-of-calls-to-Mult-method and cumulative-number-of-iterations. Confirms the only KspSolver cross-call mutable state is observability telemetry, NOT solve-affecting state, the structural basis for element-independence.
      - citation: book/src/design/l4_calculus.md:150-184
        verdict: supports
        audited_at: 2026-06-04T013000Z
        note: strawman section 3.7 iterate_while + iterate_while_pure sugar, the family whose pure-map degenerate solve_family IS (each element independent, no carry, the trajectory is the collected family). The concatenation-homomorphism (law 1) is the standard map list-homomorphism specialized to this family, a syntactic identity on map derivable from the strawman algebra.
      - citation: book/src/L4/ksp_solve.md:38-40
        verdict: supports
        audited_at: 2026-06-04T013000Z
        note: the firm ksp_solve cap (ksp_solve op inp = execState (solve_loop op inp) (initial_state inp)) that solve_family maps over. The ONE consumed combinator is firm, so the family map folds a firm primitive (the A2-style structure-side gate is discharged).
      - citation: palace/drivers/drivensolver.cpp:176-180
        verdict: supports
        audited_at: 2026-06-04T013000Z
        note: scope-boundary NEGATIVE witness, GetSystemMatrix(...) operator rebuilt per-omega INSIDE the loop (line 176) + ksp.SetOperators(*A,*P) INSIDE the loop (line 180). Confirms driven is the per-element superset (operator-capture = per-element), NOT solve_family (fixed), so the laws are correctly scoped to operator-capture-fixed.
```

Note on the §Evidence section: its closing bullet ("No dedicated test … keeps the entry at `rough-in
(test-coverage-bounded)` for its map-fusion / concatenation-homomorphism laws") and the Provenance
line ("firmed (to `rough-in (test-coverage-bounded)`) by this dispatch (cycle-055 D1)") now describe a
superseded maturity. These are **stale-after-promotion** but are NOT in the D1 ONLY-touch-§Status
scope strictly required for the promotion; I flag them in §Open questions as a bounded follow-on
lifter touch (D2 or a finalize hygiene pass) rather than expanding this edit's blast radius. If the
integrator prefers, the minimal additional edit is: in the §Evidence final bullet, replace "This keeps
the entry at `rough-in (test-coverage-bounded)` for its map-fusion / concatenation-homomorphism laws."
with "Per the firm-on-positive-structure escape (c086 D1), the absence of a dedicated test does not
gate the syntactic-identity laws — see §Status." (offered as optional; left out of the load-bearing
edit set to honor the ONLY-§Status scope).

## Applicability conditions — column-flip discipline (re-stated for the integrator)

- **Condition**: does firming `solve_family` unblock the electrostatic/magnetostatic `status: seed`
  flip? **Verifiable**: yes, from the columns' dep-maps + §Status (planner pasted: both carry TWO
  own-constituent rough-in gates, `solve_family` AND `gram_reduce`). **Found counter-example?**: N/A —
  the answer is NO, the flip stays gated. `gram_reduce` is the remaining gate, convergently blocked on
  `matrix-weighted-norm` (the √-cascade NO-GO-HELD). **This dispatch does NOT flip any column `status`
  and touches NO feature/consumer file.**

## Supporting evidence

Mechanical no-drift proof — every asserted anchor confirmed exact on-disk via
`tools/citecheck/citecheck.py --anchor` (all `[ok]`, zero `[DRIFT]`):

```
electrostaticsolver.cpp:35  'KspSolver ksp'        -> line 35  [ok]
electrostaticsolver.cpp:36  'SetOperators'         -> line 36  [ok]
electrostaticsolver.cpp:46  'std::vector<Vector> V'-> line 46  [ok]
electrostaticsolver.cpp:60  'GetSources'           -> line 60  [ok]
electrostaticsolver.cpp:68  'GetExcitationVector'  -> line 68  [ok]
electrostaticsolver.cpp:69  'ksp.Mult'             -> line 69  [ok]
electrostaticsolver.cpp:89  'step++'               -> line 89  [ok]
electrostaticsolver.cpp:42  'MFEM_VERIFY(n_step'   -> line 42  [ok]
magnetostaticsolver.cpp:35  'KspSolver ksp'        -> line 35  [ok]
magnetostaticsolver.cpp:36  'SetOperators'         -> line 36  [ok]
magnetostaticsolver.cpp:47  'std::vector<Vector> A'-> line 47  [ok]
magnetostaticsolver.cpp:66  'GetSurfaceCurrentOp'  -> line 66  [ok]
magnetostaticsolver.cpp:76  'GetExcitationVector'  -> line 76  [ok]
magnetostaticsolver.cpp:77  'ksp.Mult'             -> line 77  [ok]
magnetostaticsolver.cpp:99  'step++'               -> line 99  [ok]
magnetostaticsolver.cpp:42  'MFEM_VERIFY(n_step'   -> line 42  [ok]
ksp.cpp:297  'BaseKspSolver<OperType>::Mult'       -> line 297 [ok]
ksp.cpp:300  'ksp->Mult(x, y)'                     -> line 300 [ok]
ksp.cpp:308  'ksp_mult++'                          -> line 308 [ok]
ksp.cpp:309  'ksp_mult_it'                         -> line 309 [ok]
ksp.cpp:310  '}'  (Mult close-brace, range END)    -> line 310 [ok]
ksp.hpp:46   'mutable int ksp_mult'                -> line 46  [ok]
ksp.hpp:71   'void Mult'                           -> line 71  [ok]
drivensolver.cpp:176  'GetSystemMatrix'            -> line 176 [ok]
drivensolver.cpp:180  'SetOperators'               -> line 180 [ok]
l4_calculus.md:150-184  'iterate_while'  -> in-range (150,155,162,179,182) [ok]
L4/ksp_solve.md:38-40   'ksp_solve'      -> in-range (39,40) [ok]
```

The `ksp.cpp:297-310` range END (`}`, the `Mult` close-brace) was confirmed by a DIRECT on-disk read
(`mcp__palace-codemap__read_range` `ksp.cpp:297-340` showed the body ending at the close-brace before
`template class BaseKspSolver<Operator>;`) AND a `citecheck --anchor '}'` at `:310` — per the cycle-066
FE-source-class caveat that `--anchor` alone does not discharge a range-END close-brace off-by-one, the
END line is verified by direct read, not by anchor-in-range alone.

Files consulted:
- `palace/drivers/electrostaticsolver.cpp:28-92`, `palace/drivers/magnetostaticsolver.cpp:28-100` (the
  two fixed-operator witnesses; read in full via codemap).
- `palace/linalg/ksp.cpp:297-340`, `palace/linalg/ksp.hpp:40-90` (the `BaseKspSolver::Mult` body +
  member declarations — the decisive no-cross-element-state evidence).
- `book/src/L4/sparameter_reduce.md` §Status + `verified_against:` block (the c083 precedent; same
  firm-on-positive-structure escape wording followed here).
- `book/src/L4/solve_family.md` (the audited theme, in full).

## Open questions / caveats

- **OQ for the integrator (column-gate, 1-of-2):** `solve-family-firmed-discharges-one-of-two-electrostatic-magnetostatic-column-gates`
  — firming `solve_family` (c086 D1) discharges the FIRST of the two own-constituent gates on the
  `electrostatic` + `magnetostatic` driver columns; the SECOND, `gram_reduce`, STILL gates them (it
  folds plain-`rough-in` `matrix-weighted-norm`, the √-cascade NO-GO-HELD). The column `status: seed`
  flip is NOT unblocked by this pass alone and is NOT claimed. The batch-27 meta-phase (fires after
  c087) should weigh whether the now-singly-remaining `gram_reduce` → `matrix-weighted-norm`
  convergent blocker (also gating capacitance/inductance and, via `domain_energy_reduce`,
  energy-fields) has accumulated enough downstream demand to justify the dedicated √-cascade own-cycle
  wave under its sharpened re-weigh trigger. **Please append to `scaffolding/open-questions.md`.**

- **Stale-after-promotion prose in §Evidence + §Provenance (bounded follow-on, NOT in this edit's
  scope):** `solve_family.md`'s §Evidence final bullet ("This keeps the entry at `rough-in
  (test-coverage-bounded)` …") and the §Provenance line ("firmed (to `rough-in (test-coverage-bounded)`)
  by this dispatch (cycle-055 D1)") now describe a superseded maturity. I deliberately kept this edit
  to the §Status + frontmatter (the load-bearing promotion) per the D1 ONLY-touch-`solve_family.md`
  scope and to avoid blast-radius; the optional minimal §Evidence patch is offered in §Proposed
  changes. Recommend a finalize-time hygiene touch (or the c087 land-clean lifter pass) reconcile these
  two lines. NOT a build blocker.

- **`L4_rough_in_test_coverage_bounded` cycle-record count reconciliation** (planner-flagged, finalize
  scope): the on-disk count is `1` while three L4 entries carried the qualifier; with `solve_family`
  promoted to `firm`, the integrator-finalize should reconcile the `counts_after` L4 sub-tallies
  (`L4_firm` +1, the rough-in-test-coverage-bounded sub-cohort −1 if `solve_family` was counted). Out
  of this dispatch's scope; flagged for finalize.

- **D2 (lifter) consumer re-anchor is now UNLOCKED to the firm branch:** per the cycle-086 plan, D2
  flips the `solve_family` maturity labels in `gram_reduce.md:8,:202` + `electrostatic.L4.md` +
  `magnetostatic.L4.md` from `rough-in (test-coverage-bounded)` → `firm`, AND re-narrates the columns'
  promotion-route clause to "`solve_family` now FIRM (c086); the column stays `seed` on the REMAINING
  own-constituent gate `gram_reduce`." D2 must NOT flip either column's `status: seed` (the honest
  non-flip). This audit's verdict (FIRM) is the trigger for D2's firm-branch.
