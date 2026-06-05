---
layer: L4
operator: frequency_sweep
firmness: firm
edges:
  depends-on:
    - L4/assemble_frequency_operator
    - L4/ksp_solve
    - L4/iterate-while
    - target: L4-L3/frequency-sweep-dissolution
      kind: lowers-to
  reference:
    - concepts/state-stratification
variant_axes:
  - operator-capture (per-element — THE load-bearing axis value that distinguishes this from solve_family's `fixed`; the operator is rebuilt per family-member, SetOperators inside the map; drivensolver.cpp:176,180)
  - operand-source (affine-in-ω rebuild via assemble_frequency_operator — the per-member operator is not arbitrary but the fixed-basis affine combination A(ω); a single-pipeline specializer, NOT a free per-element operator)
  - element-type (complex — pinned; the driven sweep is complex-valued, the {iω, −ω²} weights and the ComplexOperator basis)
  - family-index-domain (frequency — absorbed into [Scalar] (the swept ω list); does not shape the combinator)
---

# frequency_sweep

The L4 **driven per-ω frequency-sweep outer-driver combinator**: map over a
frequency family where **each member REBUILDS the system operator before
solving**. Per swept frequency ω, assemble the per-ω operator
`A(ω) = assemble_frequency_operator fam ω` (the affine-in-ω combination
`K + iω·C − ω²·M + A2(ω)`), then run one [`ksp_solve`](./ksp_solve.md) against it;
collect the per-ω solution family. Where [`solve_family`](./solve_family.md)
captures a **fixed** operator once outside the map and reuses it for every member
(`SetOperators` hoisted), `frequency_sweep` is the **operator-VARYING** counterpart
— the operator is rebuilt inside the map, `SetOperators` *inside* the loop. It is
the driven (frequency-domain) pipeline's **solve half** reaching the L4 feature
surface (directive-1: L4 is the outward backend-lowering target), the
solve-coordination companion to the now-firm
[`assemble_frequency_operator`](./assemble_frequency_operator.md) **assemble half**:
together they close the last pipeline-half L4 gap, bringing the whole assemble+solve
deliverable to L4 across all five pipelines' representable shells.

This is the **driven feature's OWN single-witness form** — it is NOT framed as a
shared generalized cross-pipeline `map_solve` parent (batch-21 meta decision 4: the
`map_solve` shared form is on the STOP-PROPOSING list; this entry is the driven
specialization, scoped single-witness-driven by design). It is the named **scope
boundary** that [`solve_family`](./solve_family.md) explicitly scopes the driven
pipeline *out* of (`L4/solve_family.md:65,90,137,163`): the `operator-capture =
per-element` axis value that `solve_family`'s `fixed`-only laws do NOT cover.

## Context

L4's job is to write algorithms in a graph-evaluation calculus that makes
lifetimes, dispatch sites, and effect placement structural (`L4/index.md:7-13`).
`frequency_sweep` names the driven pipeline's outer solve-coordination shape, the
operator-varying sibling of [`solve_family`](./solve_family.md)'s fixed-operator
map:

- [`solve_family`](./solve_family.md) names the **fixed-operator map shell** — `op`
  captured once outside the map, a family `[rhs_i]` → `[x_i]`, `SetOperators`
  hoisted; each member reuses the same operator (electrostatic + magnetostatic).
- `frequency_sweep` (this entry) names the **operator-varying map shell** — a fixed
  *basis* `fam = {K, C, M, A2}` captured once, but the per-member *operator* `A(ω)`
  **rebuilt** inside the map from the swept ω, `SetOperators` *inside* the loop
  (driven only).

The architectural altitude is the same as [`solve_family`](./solve_family.md)'s —
both are value-threaded loop combinators in the strawman's §3.7 family
(`book/src/design/l4_calculus.md:150-184`), both the **pure-map degenerate** (each
member independent, no carry between solves; the trajectory IS the collected
solution family). The combinator differs from [`solve_family`](./solve_family.md)
on exactly one axis — the **operator-capture** axis (§Variant axes): `solve_family`
is `fixed` (op captured once, hoisted), `frequency_sweep` is `per-element` (op
rebuilt per member, inside the map). This is the named `per-element` value that the
firm [`solve_family`](./solve_family.md) entry records as out-of-scope and
batch-17-gated (`L4/solve_family.md:137,146,163`). It reuses the firm
[`iterate-while`](./iterate-while.md) family rather than introducing a new iteration
primitive — the same route [`chebyshev`](./chebyshev.md) and
[`solve_family`](./solve_family.md) took.

The combinator is defined **in L4 vocabulary** (high→low discipline, CLAUDE.md
§Methodology invariants): its semantics, signature, and laws are stated in terms of
the [`assemble_frequency_operator`](./assemble_frequency_operator.md) operand verb,
the [`ksp_solve`](./ksp_solve.md) per-member cap, the
[`iterate-while`](./iterate-while.md) family, and the
[`state-stratification`](../concepts/state-stratification.md) operator stratum —
NOT in terms of L3 value-threading or the L0 C++ frequency loop. The L4>L3
dissolution (the `map` collapsing to an L3 explicit per-ω `for`-loop with the
operator rebuild + `SetOperators` *inside* the loop body) is a separate cycle-070
L4>L3 theme ([`frequency-sweep-dissolution`](../L4-L3/frequency-sweep-dissolution.md),
authored by D2 this same cycle), narrated forward from L4 to L3; it is **not**
authored here.

`frequency_sweep` at L4 is a **methodology-level combinator** distilled from the
single driven driver-source frequency sweep (`DrivenSolver::SweepUniform`), not a
Palace-source artefact per se — there is no single L0 range that "is" the L4
`frequency_sweep`. The Palace evidence is the per-ω loop in §Specialization; L4
names the operator-varying map combinator and the per-member operator rebuild that
sweep carries.

## Signature

The combinator captures the fixed operator **basis** `fam` once, but rebuilds the
per-member **operator** `A(ω)` inside the map via
[`assemble_frequency_operator`](./assemble_frequency_operator.md), then runs one
[`ksp_solve`](./ksp_solve.md) per member:

    -- entry point: map over the swept frequencies; REBUILD the operator per member, then solve
    frequency_sweep :: FrequencyOperatorFamily[N] -> [Scalar] -> [SimState]
    frequency_sweep fam omegas =
      map (\omega -> ksp_solve (assemble_frequency_operator fam omega)
                               (rhs_at fam omega))
          omegas

    -- the per-member RHS (driven excitation at ω; absorbed, ω-dependent):
    rhs_at :: FrequencyOperatorFamily[N] -> Scalar -> Inputs

    -- equivalently, as the pure-map degenerate of the strawman §3.7 iterate_while family
    -- (each member independent; no carry; the "trajectory" IS the collected family):
    frequency_sweep fam omegas =
      (iterate_while
         { remaining: omegas, solutions: [] }          -- carry: remaining freqs + collected solutions
         (\st -> not (null st.remaining))                -- continue while frequencies remain
         (\st -> let omega = head st.remaining
                     op_w  = assemble_frequency_operator fam omega  -- REBUILD per member
                     sol   = ksp_solve op_w (rhs_at fam omega)      -- solve the rebuilt operator
                 in { state: { remaining: tail st.remaining
                             , solutions: st.solutions }
                    , extras: sol }))                    -- per-member extra = the solution
        .trajectory                                      -- == [ ksp_solve (asm fam w) (rhs_at fam w) | w <- omegas ]

Shape contract (bunsen-style; named records and axes; the operator stratum per
[`state-stratification`](../concepts/state-stratification.md)):

- `fam : FrequencyOperatorFamily[N]` — the **fixed operator basis** `{K, C, M, A2}`,
  captured ONCE before the sweep (the L4 typing of `K`/`C`/`M` assembled once at
  `drivensolver.cpp:91-93`). Note the stratification subtlety that distinguishes
  this from [`solve_family`](./solve_family.md): the **basis** is captured-once and
  `readonly`, but the **operator** `A(ω)` the per-member solve consumes is *not* —
  it is rebuilt from the basis at each ω inside the map. So the captured-once
  stratum here is the *basis*, not the *operator*; the operator is a per-member
  value, which is exactly the `operator-capture = per-element` axis value (§Variant
  axes).
- `[Scalar]` — the swept frequency family the `map` ranges over (the `omega_sample`
  list, `drivensolver.cpp:80,172`; each `omega` is the per-member affine-weight
  parameter the rebuild and the RHS both consume). The family-index domain (here:
  frequency) is *absorbed* into this list — it does not shape the combinator (it is
  just the list the map runs over). Element-type pinned `complex` (the driven sweep
  weights `iω`, `−ω²` and the `ComplexOperator` basis).
- `[SimState]` — the collected per-ω solution family. Each element is one
  [`ksp_solve`](./ksp_solve.md)'s terminal `SimState` (whose `.x` is the per-ω field
  solution, the `E` written by `ksp.Mult(RHS, E)` at `drivensolver.cpp:196`). Per
  the family-map, `solutions[i]` aligns with `omegas[i]` (order-preserving
  collection).
- `op_w = assemble_frequency_operator fam omega : LinearOperator[N, N]` — the per-ω
  **rebuilt** operator (the firm [`assemble_frequency_operator`](./assemble_frequency_operator.md),
  `A(ω) = K + iω·C − ω²·M + A2(ω)`); the per-member operand the inner
  [`ksp_solve`](./ksp_solve.md) inverts. This is the load-bearing structural element
  — the operator is a *function of the map index*, not a captured invariant.

The shape contract makes two things structural at the family level that are merely
conventional in the Palace C++ sweep:

1. **The operator is rebuilt per member, INSIDE the map.** `op_w` is computed inside
   the map body from `fam` and the per-member `omega`; it is *not* bound once before
   the map. This is the L4 typing of `GetSystemMatrix(...)` + `ksp.SetOperators(*A,
   *P)` sitting *inside* the `for (omega_i)` loop (`drivensolver.cpp:176,180`) — the
   property [`solve_family`](./solve_family.md) does **not** have (its `op` is hoisted
   outside the map), and exactly why driven cannot use `solve_family`.
2. **Members are independent; the collection is order-preserving.** Each `SimState`
   is a fresh, independent solve of its own rebuilt operator; the `map` carries no
   state between members. The trajectory/collection preserves position
   (`solutions[i] ↔ omegas[i]`), and the underlying solves commute (reordering the
   frequency family permutes the output identically — each `(op_w, rhs_w)` depends
   only on its own `omega`).

## Semantics

`frequency_sweep fam omegas` is the complete operator-varying frequency sweep
expressed as a `map` over the frequency family, where each member first rebuilds its
operator via [`assemble_frequency_operator`](./assemble_frequency_operator.md), then
runs one [`ksp_solve`](./ksp_solve.md) against it. It has two equivalent
presentations (the §Signature renders both):

1. **Direct map form** — `frequency_sweep fam omegas = map (\w -> ksp_solve
   (assemble_frequency_operator fam w) (rhs_at fam w)) omegas`. The combinator *is* a
   `map`: the per-member function closes over the once-captured **basis** `fam` and
   is applied independently to each frequency, rebuilding the operator and solving.
   This is the form the combinator is named for, and the form that makes the
   algebraic laws (§Algebraic laws) immediate.

2. **Pure-map degenerate of `iterate_while`** — the §3.7 family rendering
   (`book/src/design/l4_calculus.md:150-184`), where the carry is `{ remaining,
   solutions }`, the predicate is `not (null st.remaining)`, the step pops one
   frequency, rebuilds the operator, runs one [`ksp_solve`](./ksp_solve.md), and the
   per-member `extras` is the solution. By §3.7 the trajectory of extras is exactly
   `[ ksp_solve (asm fam w) (rhs_at fam w) | w <- omegas ]` — the collected family.
   This presentation reuses the firm [`iterate-while`](./iterate-while.md) family
   rather than introducing a new iteration vocabulary (the
   [`solve_family`](./solve_family.md) / [`chebyshev`](./chebyshev.md) route,
   `L4/index.md:37`); the choice between the two presentations is a presentation
   rotation, not a semantic distinction (they produce member-for-member-identical
   solution families).

The combinator's **structural contrast with [`solve_family`](./solve_family.md)** —
the reason it is a distinct entry rather than a reuse of the fixed-operator map — is
the **per-member operator rebuild**. [`solve_family`](./solve_family.md)'s per-member
function `ksp_solve op inp` reads the **same** hoisted `op` for every member (the
operator-capture-once / `SetOperators`-hoist identity, `L4/solve_family.md:90`).
`frequency_sweep`'s per-member function rebuilds `op_w = assemble_frequency_operator
fam omega` afresh at each member → the operator is a function of the map index, so
the `SetOperators`-hoist does **not** apply (the solver-operator binding is re-done
inside the map). This is the `operator-capture = per-element` axis value
(§Variant axes); the two combinators are siblings under the one §3.7 map parent
(both pure-map degenerates), differing solely on whether the operator is captured-
once or rebuilt-per-member.

Per [`state-stratification`](../concepts/state-stratification.md), the captured-once
`readonly` stratum here is the operator **basis** `fam`, not the operator itself;
the per-member operator `A(ω)` is a value rebuilt inside the map, and each member's
`SimState` is the independent per-solve stratum (no cross-member threading). The
family map does not introduce a new monadic effect — each
[`ksp_solve`](./ksp_solve.md) discharges its own `Solve` effect via `execState`
(`L4/ksp_solve.md:40`), and the `map` simply collects the discharged terminal
`SimState`s. The combinator is therefore a **pure function** `(fam, omegas) ->
[SimState]` (modulo the per-member non-determinism each
[`ksp_solve`](./ksp_solve.md) inherits transitively through
[`krylov-step`](./krylov-step.md); the map introduces no additional non-determinism).

### The per-member operand verb

`frequency_sweep`'s per-member operator rebuild is named — it is the firm
[`assemble_frequency_operator`](./assemble_frequency_operator.md), not an opaque
per-member operator the entry quantifies over (contrast
[`fold_solve`](./fold_solve.md)'s opaque-library `time_step_op`). The per-member
operand `A(ω) = K + iω·C − ω²·M + A2(ω)` is the **operator-operand specialization of
[`linear_combination`](./linear_combination.md)** at the affine-in-ω corner
(`L4/assemble_frequency_operator.md:17-31`). So the driven solve half (this entry)
and the driven assemble half ([`assemble_frequency_operator`](./assemble_frequency_operator.md))
compose cleanly: `frequency_sweep` is `map (ksp_solve ∘ assemble_frequency_operator
fam) ∘ (paired with rhs_at)` over the swept frequencies. The `operand-source` axis
(§Variant axes) records that the per-member operator is **not arbitrary** but the
fixed-basis affine combination — this sharpens (does not loosen) the operator-capture
= per-element scope: driven's per-member operator is rebuilt, but rebuilt *from a
fixed basis via a named verb*, which is what makes it a single-pipeline
specialization rather than a free per-element-operator general combinator.

### Demand-pruning interaction

Under the §3.8 pruning rule (`book/src/design/l4_calculus.md:186-228`), per-member
solutions materialize only when a downstream consumer reads them — `frequency_sweep
fam omegas` whose result is never observed prunes every solve. In Palace the driven
sweep unconditionally consumes each ω's solution immediately (per-ω post-processing:
the `E` solution feeds the post-operator measurement right after
`ksp.Mult(RHS, E)`, `drivensolver.cpp:196`+), so no member prunes in practice; but
the combinator's typing makes the demand-driven materialization structural (the
pure-map degenerate inherits the §3.7 trajectory's demand-pruning directly).

## Algebraic laws

`frequency_sweep` is a **`map` combinator**, so its laws are the list-homomorphism /
naturality laws of `map` specialised to the operator-varying frequency family, with
the per-member operator a *function of the map index* (the load-bearing contrast
with [`solve_family`](./solve_family.md), whose per-member operator is invariant).
Every law is a **syntactic identity on the read map** — read directly off the single
positive driven loop. Absences are catalogued explicitly to prevent decoration
drift.

1. **Concatenation-homomorphism** (the load-bearing law). `frequency_sweep fam
   (a ++ b) = frequency_sweep fam a ++ frequency_sweep fam b`. The frequency map is a
   list homomorphism — it distributes over concatenation — *because the basis `fam`
   is shared and each member's solve (of its own rebuilt operator) is independent*.
   This licenses splitting, chunking, or reordering the swept-frequency family (and,
   downstream, the embarrassingly-parallel realization: the sweep can be solved in
   any partition). Note this holds **despite** the operator varying per member: the
   per-member operator `A(ω)` is a pure function of the member's own `omega` and the
   shared `fam`, so members remain mutually independent. This is the **same
   homomorphism** [`solve_family`](./solve_family.md) law 1 carries, here over the
   operator-varying map — the per-member-rebuild does not break independence because
   the rebuild is index-local.

2. **Per-member operator rebuild / NO `SetOperators`-hoist** (the identity that
   distinguishes this combinator from [`solve_family`](./solve_family.md) — the
   load-bearing **non**-hoist). `frequency_sweep fam omegas = map (\w -> ksp_solve
   (assemble_frequency_operator fam w) (rhs_at fam w)) omegas`, and the operator
   construction `assemble_frequency_operator fam w` is **NOT invariant across the
   map** (it depends on the per-member `w`), so it does **NOT** hoist out of the map.
   This is the L4 typing of `GetSystemMatrix(...)` + `ksp.SetOperators(*A, *P)`
   sitting *inside* the `for (omega_i)` loop (`drivensolver.cpp:176,180`) — the exact
   negation of [`solve_family`](./solve_family.md) law 2 (whose `fresh_ksp op` hoists
   because `op` is invariant). What **does** hoist is the operator *basis* `fam`
   (assembled once, `drivensolver.cpp:91-93`); the per-member operator does not.
   This non-hoist is the `operator-capture = per-element` axis value (§Variant axes).

3. **Member-independence / order-preservation** (the map's naturality). The solutions
   do not depend on family order — `x_i` depends only on `(fam, omega_i)` — so the
   underlying solves commute: `frequency_sweep fam (permute omegas) = permute
   (frequency_sweep fam omegas)` for any permutation. The *collection* preserves
   position (`solutions[i] ↔ omegas[i]`), so the map is order-preserving even though
   the solves commute. (Naturality: `frequency_sweep fam . map g = map (solve_at fam .
   g)` for any frequency-transform `g` that does not touch `fam` — where `solve_at fam
   w = ksp_solve (assemble_frequency_operator fam w) (rhs_at fam w)`.)

4. **Empty-family degenerate** (`frequency_sweep fam [] = []`). The empty frequency
   family maps to the empty solution family — a degenerate (not algebraic) identity,
   the same flavor as [`solve_family`](./solve_family.md) law 4 / the per-member
   [`ksp_solve`](./ksp_solve.md)'s zero-RHS short-circuit. Palace's driven sweep runs
   over the non-empty configured `omega_sample` list (`drivensolver.cpp:80`), so the
   empty case is a calculus-level total-definition convenience, not a witnessed
   Palace path.

Laws that explicitly **do not** hold:

- **`SetOperators`-hoist / fixed-operator-capture** (the load-bearing *non*-law — the
  map/map distinction from [`solve_family`](./solve_family.md)). The operator
  construction does NOT hoist out of the map (law 2): each member rebuilds its own
  `A(ω)` inside the map. This is precisely what scopes `frequency_sweep` *out* of
  [`solve_family`](./solve_family.md) (whose law 2 IS the hoist) and into the
  `operator-capture = per-element` axis value. `frequency_sweep` is NOT an instance
  of `solve_family`; it is the operator-varying sibling under the same §3.7 map
  parent.
- **Per-member operator fusion across the sweep.** The per-member operators
  `{A(ω_0), A(ω_1), ...}` do NOT fuse into a single whole-sweep operator — each is a
  distinct affine combination at a distinct ω, and each member's solve is an
  independent iterative [`ksp_solve`](./ksp_solve.md) with its own
  `sequential-obstruction` (`L4/ksp_solve.md`). The map collects independent
  fixed-point computations over distinct operators; it does not collapse them. (The
  embarrassing-parallelism licensed by law 1 is *independence*, not *fusion*.) Note
  the per-member operators DO share the affine-in-ω family structure
  (`L4/assemble_frequency_operator.md` law 2 — degree-≤2 polynomial-in-ω over the
  fixed basis); that family structure is a property of the *operands*
  (`assemble_frequency_operator`'s law), not a fusion of the *solves*.
- **Cross-member determinism / solve fusion.** As with
  [`solve_family`](./solve_family.md), the per-member solves do not fuse into a single
  closed-form whole-family solve — each is an independent iterative solve. The map
  collects; it does not collapse.
- **Linearity of the readout family in the frequency family.** The `SimState.it` /
  `.final_res` readout of each member is not linear in its `omega` (different ω
  generate different operators, different RHSes, different residual histories) —
  inherited per-member from [`ksp_solve`](./ksp_solve.md) (`L4/ksp_solve.md`). Only
  each terminal `SimState.x` is the (operator-dependent) solution of its own
  `A(ω) x = b(ω)` (modulo tolerance).

## Specialization

Per replace-and-propagate (CLAUDE.md §Methodology invariants vocabulary-shift
redirect), `frequency_sweep` is the **entry**; the single driven Palace sweep is a
**specialization note re-expressing THROUGH it**, not a separate rectangular leaf
chapter. (Unlike [`solve_family`](./solve_family.md) / [`fold_solve`](./fold_solve.md),
which each carry two witnesses, `frequency_sweep` is **single-witness-driven by
design** — the operator-varying frequency sweep is exhibited by the driven pipeline
only, and that is permanent, a finding not a gap: §Status scope.)

- **Driven uniform frequency sweep** (`palace/drivers/drivensolver.cpp`,
  `DrivenSolver::SweepUniform`). The operator **basis** is assembled once before the
  sweep: `K = GetStiffnessMatrix<ComplexOperator>(...)` (`:91`),
  `C = GetDampingMatrix<ComplexOperator>(...)` (`:92`),
  `M = GetMassMatrix<ComplexOperator>(...)` (`:93`) — `fam`'s fixed `{K, C, M}`. The
  family is the **frequency index set** `omega_sample = iodata.solver.driven.sample_f`
  (`:80`), traversed by `for (std::size_t omega_i = ...; omega_i <
  omega_sample.size(); omega_i++)` (`:168-170`), `omega = omega_sample[omega_i]`
  (`:172`). Per member, the operator is **REBUILT inside the loop**: the ω-dependent
  extra term `A2 = GetExtraSystemMatrix<ComplexOperator>(omega, ...)` (`:175`), then
  `A = GetSystemMatrix(1.0 + 0.0i, 1i * omega, -omega * omega + 0.0i, K, C, M, A2)`
  (`:176`) — the [`assemble_frequency_operator`](./assemble_frequency_operator.md)
  rebuild — and **captured inside the loop** by `ksp.SetOperators(*A, *P)` (`:180`).
  The per-member RHS is `space_op.GetExcitationVector(excitation_idx, omega, RHS)`
  (`:194`, ω-dependent), and the per-member solve is `ksp.Mult(RHS, E)` (`:196`) —
  the `ksp_solve op_w inp_w` writing into the per-ω solution slot `E`. Element-type:
  complex.

The driven adaptive sweep (`DrivenSolver::SweepAdaptive`, `drivensolver.cpp:231`) is
**NOT** a `frequency_sweep` member — it is a state-generated greedy march, the
[`fold_solve`](./fold_solve.md) `schedule-source = state-generated` form
(`L4/fold_solve.md:115,150`): the swept frequencies are *generated from the carry*
(the growing PROM basis + error history), not consumed from a fixed `[Scalar]` list,
and each step reads the prior carry — a sequential fold, not an independent map.
`frequency_sweep` is the **uniform** (fixed frequency-list) driven sweep; the
adaptive sweep is `fold_solve`'s greedy state-generated fold. (This is the clean
map/fold split: uniform driven = `frequency_sweep` map; adaptive driven-PROM =
`fold_solve` fold.)

## Dependencies

L4 rows this combinator consumes:

- [`assemble_frequency_operator`](./assemble_frequency_operator.md) — the per-member
  operator rebuild `A(ω) = K + iω·C − ω²·M + A2(ω)` (the driven assemble half this
  solve half maps the rebuild over). The named per-member operand verb (NOT an opaque
  per-member operator) — the load-bearing distinction from
  [`fold_solve`](./fold_solve.md)'s opaque `time_step_op`. The driven assemble + solve
  halves compose: `frequency_sweep` is `map (ksp_solve ∘ assemble_frequency_operator
  fam, paired with rhs_at) omegas`.
- [`ksp_solve`](./ksp_solve.md) — the per-member solve cap mapped (one rebuilt
  `(op_w, rhs_w)` → one `SimState`). `frequency_sweep` consumes it as its mapped
  function; one shell out from it.
- [`iterate-while`](./iterate-while.md) — the §3.7 family whose **pure-map degenerate**
  the combinator IS (each member independent, no carry; the trajectory is the
  collected family). Reused rather than introducing a new iteration vocabulary, the
  [`solve_family`](./solve_family.md) / [`chebyshev`](./chebyshev.md) route.

L4 contrast-sibling (not consumed, referenced for the operator-capture distinction):

- [`solve_family`](./solve_family.md) — the **fixed-operator** map sibling. Same §3.7
  map parent, same family-map list-homomorphism (law 1) + member-independence (law 3);
  differs solely on the **operator-capture** axis (`solve_family` `fixed`: op captured
  once, hoisted — law 2 IS the hoist; `frequency_sweep` `per-element`: op rebuilt per
  member, inside the map — law 2 is the NON-hoist). `frequency_sweep` IS the named
  `per-element` superset value that `solve_family` scopes the driven pipeline out of
  (`L4/solve_family.md:65,90,137,146,163`).
- [`fold_solve`](./fold_solve.md) — the state-threaded **fold** sibling (the carry IS
  threaded; members are sequential). The adaptive driven-PROM sweep is a `fold_solve`
  member (state-generated schedule), NOT a `frequency_sweep` member — the uniform/
  adaptive split is the map/fold split.

L4 concept references:

- [`state-stratification`](../concepts/state-stratification.md) — the operator stratum
  subtlety: the captured-once `readonly` stratum is the operator **basis** `fam`, not
  the operator itself; the per-member operator `A(ω)` is rebuilt inside the map (the
  `operator-capture = per-element` distinction from
  [`solve_family`](./solve_family.md)). Each member's `SimState` is independent.
- [`solve-monad`](../concepts/solve-monad.md) — the `Solve = StateT SimState Identity`
  effect each per-member [`ksp_solve`](./ksp_solve.md) discharges; the family map
  collects the discharged terminal `SimState`s without introducing a new effect.
- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the §3.8
  demand-pruning governing whether per-member solutions materialize (inherited from
  the §3.7 trajectory).
- [`variant-absorption`](../concepts/variant-absorption.md) — the operator-capture
  axis (`fixed | per-element`), the operand-source axis (the named affine rebuild),
  and the family-index / element-type absorption.

**Strawman reference**: `book/src/design/l4_calculus.md` §3.7 (`iterate_while` + the
`iterate_while_pure` sugar, `:150-184`) is the family this combinator's pure-map
degenerate joins; §3.8 (demand-pruning, `:186-228`) governs per-member
materialization. This verb adds **no reduction rule** (it is a `map` over the
existing [`ksp_solve`](./ksp_solve.md) cap composed with the existing
[`assemble_frequency_operator`](./assemble_frequency_operator.md) verb).

## Lowers to

L4 `frequency_sweep` lowers to an L3 explicit per-ω `for`-loop with the operator
**rebuild + `SetOperators` inside the loop body** (the Palace C++ shape,
§Specialization) and the operator basis hoisted outside — via the L4>L3 dissolution
theme [`frequency-sweep-dissolution`](../L4-L3/frequency-sweep-dissolution.md)
(**cycle-070 D2 abstractor; authored this same cycle**; canonical slug
`frequency-sweep-dissolution`). The rotation is **substantive** (not identity-in-form):
the `map` collapses to a positional `for (std::size_t omega_i = ...)` loop; the
per-member operator rebuild `assemble_frequency_operator fam omega` becomes the inline
`GetSystemMatrix(...)` call *inside* the loop; the `ksp.SetOperators(*A, *P)` capture
is placed *inside* the loop (the operator-varying placement — the L3 image of the
NON-hoist law 2); the pure-map trajectory becomes the per-ω solution write
`ksp.Mult(RHS, E)` consumed in place. This entry records the rotation *direction*
(L4 operator-varying map combinator → L3 explicit per-ω rebuild-and-solve loop)
in-line per high→low discipline; it does **not** author the theme. The standalone
L3-entry-vs-dissolution-home question is **D2's** (likely the
[`solve_family`](./solve_family.md) NO-ENTRY shape — the frequency loop carries **no
`sequential-obstruction`** because the members are independent (embarrassingly
parallel, written sequentially), so the L3 form is fully + concisely expressed by the
dissolution theme's §"L3 form (RHS)"; the per-member solve delegates to the firm
[`L3/ksp_solve`](../L3/ksp_solve.md), which DOES carry its own per-solve obstruction —
contrast [`fold_solve`](./fold_solve.md), whose carry-threading obstruction warrants a
standalone L3 entry).

## Variant axes

Four axes, one load-bearing (operator-capture) and three absorbed/pinned:

1. **operator-capture** (`per-element`) — **THE load-bearing axis**, and the scope
   boundary that distinguishes this combinator from [`solve_family`](./solve_family.md).
   `frequency_sweep` claims `per-element` ONLY: the operator is rebuilt per member,
   `SetOperators` *inside* the map (`drivensolver.cpp:176,180`). The
   concatenation-homomorphism (law 1) and member-independence (law 3) hold (the rebuild
   is index-local), but the `SetOperators`-hoist does NOT (law 2 non-hoist). This is the
   named `per-element` value that [`solve_family`](./solve_family.md)'s `fixed`-only
   laws explicitly exclude (`L4/solve_family.md:137`).
2. **operand-source** (`affine-in-ω rebuild`) — the per-member operator is NOT arbitrary
   but the fixed-basis affine combination
   [`assemble_frequency_operator`](./assemble_frequency_operator.md) `A(ω) = K + iω·C −
   ω²·M + A2(ω)`. Absorbed into the per-member operator verb; sharpens the per-element
   scope (driven's per-member operator is rebuilt-from-a-fixed-basis, which is what makes
   this a single-pipeline specialization rather than a free per-element-operator general
   combinator — the `map_solve` shared form STOP-PROPOSING boundary, batch-21 meta
   decision 4).
3. **element-type** (`complex`) — pinned. The driven sweep is complex-valued (the
   `{iω, −ω²}` weights and the `ComplexOperator` basis, `drivensolver.cpp:91-93,176`);
   the general `real | complex` axis collapses to complex-only here.
4. **family-index-domain** (`frequency`) — the index set the family ranges over;
   **absorbed into `[Scalar]`** (the swept `omega_sample` list). Does not shape the
   combinator (it is just the list the map runs over).

## Status

`firm` — the **firm-on-positive-structure escape** applies (CLAUDE.md §Methodology
invariants "Two rough-in qualifiers are first-class", the `apply_nonlinear_pencil` /
[`fold_solve`](./fold_solve.md) / [`assemble_frequency_operator`](./assemble_frequency_operator.md)
precedent). The combinator's structural signature is well-anchored at L0 (the
operator-basis-captured-once + operator-rebuilt-per-member + map-collect shape, the
operator-capture = per-element axis, the per-member operand = the firm
`assemble_frequency_operator` verb) by the **single positive driven loop**
(`drivensolver.cpp:91-93,168-196`). Every law (§Algebraic laws) is a **syntactic
identity on the read map**: the concatenation-homomorphism is `map (a++b) = map a ++
map b` (with the per-member operator a pure function of the index, so independence
holds), the member-independence is the map's naturality, and the load-bearing **non**-law
(the `SetOperators`-NON-hoist) is read directly off the `GetSystemMatrix`/`SetOperators`-
*inside*-the-loop placement. These are read-off identities on the positive driven loop +
the firm [`assemble_frequency_operator`](./assemble_frequency_operator.md) operand (firm
cycle-069 D1) + the firm [`ksp_solve`](./ksp_solve.md) cap (firm cycle-048) — NOT
test-gated convergence-semantics claims (the [`eigsolve`](./eigsolve.md) distinction) —
so the absence of a dedicated driven-sweep unit test does NOT gate them, and the entry is
`firm`. (Contrast the **operator-capture axis** against [`solve_family`](./solve_family.md),
also `firm` (c086): `solve_family`'s load-bearing independence claim — that the `KspSolver`
*reuse* across members carries no hidden cross-member state — was ultimately discharged on
positive structure (read off the const `BaseKspSolver::Mult` body, `palace/linalg/ksp.cpp:297-310`,
whose only cross-call state is two monotone telemetry counters); `frequency_sweep` instead
rebuilds a *fresh* operator and re-captures it per member, so its no-cross-member-state
property is read directly off the per-member `SetOperators(*A, *P)` rebuild rather than off a
reused solver. The two entries are now equal in maturity (both firm); the load-bearing
distinction is the **fixed-shared-capture vs. fresh-per-member-rebuild** axis itself, not a
firm-vs-rough-in maturity gap.)

**Scope (load-bearing) — single-witness-driven BY DESIGN**: `frequency_sweep`
(operator-varying frequency sweep) is witnessed by the **driven uniform sweep ONLY**
(1-of-5 pipelines), and that is **permanent by design** (a finding, not a gap), exactly
as [`assemble_frequency_operator`](./assemble_frequency_operator.md) is single-pipeline by
design (`L4/assemble_frequency_operator.md:264-283`). The other four pipelines: electrostatic
+ magnetostatic are the **fixed-operator** [`solve_family`](./solve_family.md) map (operator
captured once, hoisted — NOT operator-varying); transient is the state-threaded
[`fold_solve`](./fold_solve.md) (carry-threaded sequential fold, not an independent map);
the adaptive driven-PROM sweep is `fold_solve`'s state-generated greedy form (NOT the
uniform fixed-list map); eigenmode is opaque-library-owned (no Palace-assembled per-member
operator sweep). So the operator-VARYING map is exhibited by the uniform driven sweep alone
— `frequency_sweep` lands as a **single-witness driven specialization**, which is fine under
the redirect (solvers are pulled up as a low-priority test-load; a clean single-witness
driven form through existing vocabulary is a legitimate landing). It is **NOT** framed as a
shared generalized `map_solve` cross-pipeline parent (batch-21 meta decision 4: `map_solve`
is on the STOP-PROPOSING list as a SHARED form) — it is the driven feature's OWN form. The
operator-capture = per-element generality is recorded on [`solve_family`](./solve_family.md)'s
variant axis as the named superset value; this entry is the driven instance of that value, not
a second-pipeline witness (none exists, by design).

This dispatch (cycle-070 D1, LEAD) is the **driven-pipeline solve-half L4 lift** (plan-tag the
driven feature-surface completion), closing the last pipeline-half L4 gap: with
[`assemble_frequency_operator`](./assemble_frequency_operator.md) (the driven assemble half,
cycle-069) firm and `frequency_sweep` (the driven solve half) landing here, the whole
assemble+solve deliverable reaches L4 across all 5 pipelines' representable shells
(directive-1: L4 is the outward backend-lowering target). The L4>L3 dissolution theme
([`frequency-sweep-dissolution`](../L4-L3/frequency-sweep-dissolution.md)) is cycle-070 D2's
job this same cycle; this entry records the rotation direction in-line but does not author the
theme.

## L4 vs L3 distinction

- **L3**: value-threaded explicit per-ω outer sweep — a positional `for (std::size_t
  omega_i = ...)` loop with the operator rebuild (`GetSystemMatrix(...)`) + `SetOperators`
  *inside* the loop body, the operator basis hoisted outside the loop by hand, the per-ω
  solution written in place (the Palace C++ shape). The operator-varying map collapses to
  the explicit per-ω rebuild-and-solve loop; the operator-rebuild-per-member is a coding
  convention (`GetSystemMatrix`/`SetOperators` placed *inside* the `for`), not a type-level
  axis value.
- **L4**: the `map` combinator `frequency_sweep fam omegas = map (\w -> ksp_solve
  (assemble_frequency_operator fam w) (rhs_at fam w)) omegas`. The operator-basis-capture-once
  is *structural* (`fam : FrequencyOperatorFamily[N]` `readonly`, bound once outside the map),
  the per-member operator rebuild is *typed* (a value computed inside the map from `fam` and
  the per-member ω — the `operator-capture = per-element` axis), per-member independence is
  typed (no cross-member threading). The L4>L3 dissolution erases the map-combinator naming and
  the typed operator-capture axis, recovering the L3 explicit per-ω rebuild-and-solve loop.

## Evidence

`frequency_sweep` at L4 is a methodology-level combinator distilled from the single driven
driver sweep; Palace's C++ does not realise the L4 map form (it writes the explicit per-ω
rebuild-and-solve loop). All L0 citations self-verified against on-disk source this dispatch
via `tools/citecheck/citecheck.py --anchor` (the codemap `read_range` confirmed against the
on-disk `reference/palace/palace/drivers/drivensolver.cpp`).

- **Operator-varying frequency-sweep witness (positive, single-witness driven):**
  - `palace/drivers/drivensolver.cpp:80` (`const auto &omega_sample =
    iodata.solver.driven.sample_f` — the swept frequency family `[Scalar]` the map ranges
    over), `:91` (`K = space_op.GetStiffnessMatrix<ComplexOperator>(...)` — the operator
    basis assembled ONCE before the sweep), `:92` (`C = GetDampingMatrix<ComplexOperator>(...)`),
    `:93` (`M = GetMassMatrix<ComplexOperator>(...)` — `fam`'s fixed `{K, C, M}`), `:168-170`
    (`for (std::size_t omega_i = ...; omega_i < omega_sample.size(); omega_i++)` — the map
    loop), `:172` (`auto omega = omega_sample[omega_i]` — the per-member frequency).
  - `palace/drivers/drivensolver.cpp:175` (`A2 =
    space_op.GetExtraSystemMatrix<ComplexOperator>(omega, Operator::DIAG_ZERO)` — the
    ω-dependent extra term, rebuilt inside the loop), `:176`
    (`A = space_op.GetSystemMatrix(1.0 + 0.0i, 1i * omega, -omega * omega + 0.0i, K.get(),
    C.get(), M.get(), A2.get())` — the per-ω operator REBUILD inside the loop, the
    [`assemble_frequency_operator`](./assemble_frequency_operator.md) verb), `:180`
    (`ksp.SetOperators(*A, *P)` — the per-ω operator CAPTURE inside the loop; the
    operator-VARYING placement = the NON-hoist law 2 = the scope boundary vs
    [`solve_family`](./solve_family.md)).
  - `palace/drivers/drivensolver.cpp:194` (`space_op.GetExcitationVector(excitation_idx,
    omega, RHS)` — the per-ω RHS, ω-dependent), `:196` (`ksp.Mult(RHS, E)` — the per-member
    solve = `ksp_solve op_w inp_w`, writing the per-ω solution into `E`).
- **Contrast-siblings (negative for operator-varying-map):**
  - [`solve_family`](./solve_family.md) (electrostatic + magnetostatic) is the **fixed-operator**
    map sibling — operator captured once, hoisted (NOT operator-varying); cited for the
    operator-capture axis distinction, not as `frequency_sweep` evidence.
  - [`fold_solve`](./fold_solve.md) (transient + driven-PROM SweepAdaptive) is the **fold**
    sibling — carry threaded, members sequential. The adaptive driven sweep
    (`drivensolver.cpp:231`, `SweepAdaptive`) is `fold_solve`'s state-generated form, NOT a
    `frequency_sweep` member; cited for the uniform/adaptive = map/fold split.
- **Firm vocabulary grounding:**
  - `book/src/L4/assemble_frequency_operator.md:17-31` (the per-member operator rebuild verb —
    the operator-operand `linear_combination` specialization), `:264-283` (the
    single-pipeline-by-design precedent this entry follows for its single-witness scope).
  - `book/src/L4/ksp_solve.md:36-40` (the per-member solve cap mapped, `ksp_solve :: OpParams
    -> Inputs -> SimState`, `= execState (solve_loop op inp) (initial_state inp)`).
  - `book/src/L4/solve_family.md:65` (the operator-capture distinction making driven NOT a
    `solve_family` instance), `:90` (the operator-capture-once / `SetOperators`-hoist law this
    entry's law 2 negates), `:137,146,163` (the `per-element` superset scope boundary naming
    the driven `drivensolver.cpp:176-180` site `frequency_sweep` formalizes).
  - `book/src/L4/index.md:30-47` (the L4 outer-driver vocabulary cohort `frequency_sweep`
    joins), `:7-13` (L4-is-vocabulary remit), `:37` (the iterate-while-family-reuse precedent).
  - `book/src/design/l4_calculus.md:150-184` (§3.7 `iterate_while` + `iterate_while_pure` sugar
    — the family the pure-map degenerate joins), `:186-228` (§3.8 demand-pruning).
  - `book/src/concepts/state-stratification.md` (the operator-basis-captured-once vs
    operator-rebuilt-per-member stratum distinction).
- **No dedicated test** exercises the `Solve(mesh)` driven frequency sweep (the driver is
  integration-level, not unit-tested under `reference/palace/test/unit/`); the L0 evidence is
  the driver source above. This does NOT gate the map laws (they are read-off syntactic
  identities on the positive driven loop — the firm-on-positive-structure escape; the
  operator-capture = per-element axis value is read directly off the per-member `SetOperators`
  rebuild, not assumed), so the entry is `firm`.
- **Provenance**: the batch-21 meta-phase-decided LIFT (the driven solve-half → L4 decision
  closing the last pipeline-half L4 gap); harvested cycle-070 D1 (LEAD). The firm
  [`assemble_frequency_operator`](./assemble_frequency_operator.md) (cycle-069 D1, the driven
  assemble half / per-member operand) + the firm [`ksp_solve`](./ksp_solve.md) (cycle-048, the
  per-member solve cap) + the [`solve_family`](./solve_family.md) `per-element` scope boundary
  (cycle-055) are the direct inputs. WARRANT verdict: genuine L4 entry (the driven feature's OWN
  single-witness solve-half form; the operator-varying map is a distinct shell from
  `solve_family`'s fixed-operator map and `fold_solve`'s sequential fold — a navigable L4 home as
  the driven solve-coordination verb + the named `per-element` scope boundary, NOT a shared
  `map_solve` parent per batch-21 meta decision 4).
