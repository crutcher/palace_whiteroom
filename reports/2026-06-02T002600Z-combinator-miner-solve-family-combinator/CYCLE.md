---
agent: combinator-miner
invoked_at: 2026-06-02T002600Z
scope: Pattern proposal — fixed-operator solve-family combinator (solve_family / map_solve)
status: integrated
integrated_at: 2026-06-02T011000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  cycle-054 D1, applied clean by integrator-per-report (STAGING row 1), finalized by integrator-finalize.
  Mined `solve_family` — the fixed-operator map-over-RHS-family combinator at L4 outer-driver vocabulary
  (the pure-map degenerate of `iterate_while`). Landed as ONE rough-in dep-map row in book/src/L4/index.md
  (after the `eigsolve` row; plain-text inline-code slug; inner [ksp_solve]/[iterate-while] links resolve).
  Fixed-operator-only (2-of-5 pipelines: electrostatic electrostaticsolver.cpp:111-137 + magnetostatic
  magnetostaticsolver.cpp:110-152). The full solve_family.md entry + 2 specializations +
  L4-L3/solve-family-map-dissolution theme deferred to batch-17. Driven breaks shared-operator-capture
  (drivensolver.cpp:176/:180) => general map_solve_over_(operator,rhs)_family superset is batch-17.
  Discharges the action-half of the c053 solve-family-combinator-confirmed-2-of-n-mine-now OQ.
  2 OQs promoted. L4 outer-driver rows 4->5; L4 firm unchanged 6. Build exit 0; row renders plain-text
  (zero dangling). Gate hits: 0. Batch-16 final cycle; the batch-16 meta-phase fires next as a separate dispatch.
---

# CYCLE: Combinator candidate — solve_family (fixed-operator map-over-RHS solve)

## Summary

Two of Palace's five solver pipelines — **electrostatic** and **magnetostatic** — share a single
outer-sweep shape that the existing `ksp_solve` cap does NOT name: **fix the system operator `K`
once, build the `ksp` solver once (`SetOperators(*K,*K)` outside the loop), then map
`ksp_solve(K, ·)` over a family of right-hand sides `[rhs_i]` and collect the solution family
`[x_i]`.** Each pipeline's `Solve(mesh)` loops over a finite index set (terminal boundaries /
surface-current boundaries), forms one RHS per index, and reuses the *same* assembled `ksp` for
every solve. This is a **map-over-family** combinator that sits strictly *above* the `ksp_solve`
outer-driver cap (analogous to how `solve_loop` sits above `krylov-step`): `ksp_solve` coordinates
one solve to convergence; `solve_family` coordinates `ksp_solve` over a family with a single shared
operator capture. I propose **`solve_family`** as a new **L4 outer-driver combinator** (the layer
above the `ksp_solve` cap, in L4 outer-driver vocabulary), with the electrostatic and magnetostatic
outer sweeps as its two specialization pointers (replace-and-propagate: the combinator is the
entry, the sweeps are notes under it; the two specialization *entries* sequence to batch-17). The
**fixed-operator** form is the only one I claim (2 of 5 pipelines); the **driven** pipeline breaks
shared-operator-capture (operator rebuilt per-frequency inside the loop), so I flag the general
`map_solve_over_(operator,rhs)_family` as the **superset** and gate it on a batch-17 3rd-probe.

## Pattern instances

- **Instance 1 (electrostatic, FIXED-OPERATOR):**
  `palace/drivers/electrostaticsolver.cpp:30` — `auto K = laplace_op.GetStiffnessMatrix();`
  (operator assembled ONCE);
  `:35-36` — `KspSolver ksp(...)` + `ksp.SetOperators(*K, *K);` (solver built ONCE, outside the
  loop);
  `:60-90` — `for (const auto &[idx, data] : laplace_op.GetSources())` outer sweep over the
  terminal-boundary index family;
  `:68-69` — `laplace_op.GetExcitationVector(idx, *K, V[step], RHS); ksp.Mult(RHS, V[step]);` —
  form the per-index RHS, then `ksp.Mult` ( = `ksp_solve(K, RHS_idx)` ) into `V[step]`;
  `:46` `std::vector<Vector> V(n_step);` + `:89` `step++` — collect the solution family `[V_i]`.

- **Instance 2 (magnetostatic, FIXED-OPERATOR):**
  `palace/drivers/magnetostaticsolver.cpp:30` — `auto K = curlcurl_op.GetStiffnessMatrix();`
  (operator assembled ONCE);
  `:35-36` — `KspSolver ksp(...)` + `ksp.SetOperators(*K, *K);` (solver built ONCE, outside the
  loop);
  `:66-100` — `for (const auto &[idx, data] : curlcurl_op.GetSurfaceCurrentOp())` outer sweep over
  the surface-current-boundary index family;
  `:76-77` — `curlcurl_op.GetExcitationVector(idx, RHS); ksp.Mult(RHS, A[step]);` — form the
  per-index RHS, then `ksp.Mult` ( = `ksp_solve(K, RHS_idx)` ) into `A[step]`;
  `:47` `std::vector<Vector> A(n_step);` + `:99` `step++` — collect the solution family `[A_i]`.

- **Instance 3 (driven — NEGATIVE / superset witness, NOT a fixed-operator instance):**
  `palace/drivers/drivensolver.cpp:176-180` — `auto A = space_op.GetSystemMatrix(1.0, iω, -ω², ...)`
  + `ksp.SetOperators(*A, *P);` **inside** the frequency loop `:168-170`
  (`for (omega_i ...)`). The operator `A = (K + iωC − ω²M)` is **frequency-dependent** and rebuilt
  per-ω; `SetOperators` is called *inside* the loop. This pipeline maps a solve over a frequency
  family but **cannot fix the operator** — it is an instance of the *superset*
  `map_solve_over_(operator,rhs)_family`, NOT of the fixed-operator `solve_family`. Used here as the
  scope boundary, not as supporting evidence for the proposed (fixed) combinator.

Two positive fixed-operator instances (the soft bar for a same-shape combinator is ≥3; this is at
the borderline-2). The proposal is nonetheless grounded because (a) the cycle-053 discharge of the
single-witness gate explicitly unblocked this at 2-of-N, (b) the two instances are
structurally *identical* down to the `GetStiffnessMatrix()` / `SetOperators(*K,*K)` / `GetSources`-vs-
`GetSurfaceCurrentOp` / `std::vector<Vector>` collect shape, and (c) the third pipeline's *break*
sharpens the scope rather than weakening it. The 2-of-5-pipelines scope is stated explicitly below
and the >2 generalization is deferred to a batch-17 probe (Open question).

## Proposed combinator

- **Slug**: `solve_family`
- **Layer**: **L4** (outer-driver vocabulary — the layer *above* the `ksp_solve` cap).

  **Rationale (why L4 outer-driver, not adjacent layers):** `solve_family` coordinates the
  `ksp_solve` *cap* over a family. The `ksp_solve` cap is itself L4 outer-driver vocabulary
  (`book/src/L4/ksp_solve.md:38`, "the `Solve`-monadic outer-driver cap"), assembled from
  `solve_loop` / `restart_cycle` / `Outcome` (`book/src/L4/index.md:41-46`). `solve_family` is the
  *next coordination shell out*: where `solve_loop` is an **iterate-while** over inner cycles
  (`L4/ksp_solve.md:100`, "tail-recursion ≡ `iterate_while_pure` over outer cycles"),
  `solve_family` is a **map** over an *independent* RHS family — a different combinator (map, not
  iterate-while) at the *same architectural altitude* as `solve_loop` but one shell further out
  (it drives whole `ksp_solve` solves, not single cycles). It belongs at L4 because:
  - It is **vocabulary, not architecture** (`L4/index.md:7`): it captures *what operation happens*
    (map a solve over a family) and *who owns the state* (the operator captured once vs the
    per-element RHS/solution) — exactly the L4 remit.
  - Its body is a **value-threaded loop combinator** in the strawman's §3.7 family
    (`book/src/design/l4_calculus.md:150-184`) — specifically the **pure-map degenerate** of
    `iterate_while` where each element is independent (no carry between solves), so the per-element
    extras are the solutions and the trajectory IS the collected family. This reuses the firm
    `iterate-while` family rather than introducing a new iteration vocabulary (the same route
    `chebyshev` took, `L4/index.md:37`).
  - It is **NOT L3**: at L3 the value-threading is positional and the map collapses to an explicit
    `std::vector<Vector>`-accumulating loop (the Palace C++ shape); the L4 form is what *names* the
    map combinator and the operator-capture-once stratification. The L4>L3 dissolution
    (`solve_family` → an L3 explicit accumulating loop) is a separate batch-17 theme, not authored
    here.
  - It is **NOT inside the `ksp_solve` cap**: `ksp_solve` is per-solve (one RHS → one solution);
    `solve_family` is per-family and *consumes* `ksp_solve` as its mapped function. Folding it into
    `ksp_solve` would conflate two distinct coordination shells (the `solve_loop` cap and the
    `solve_family` shell), the same error the `L4/ksp_solve.md:28` "sits *above* the
    `iterate-while` family, not inside it" stratification guards against.

- **Signature sketch** (L4/L3 pseudo-language; harvester will firm up):

  ```text
  -- entry point: capture the operator once, build the solver once, map ksp_solve over the RHS family
  solve_family :: OpParams -> [Inputs] -> [SimState]
  solve_family op rhss = map (\inp -> ksp_solve op inp) rhss

  -- equivalently, as the pure-map degenerate of the strawman §3.7 iterate_while family
  -- (each element independent; no carry; the "trajectory" IS the collected solution family):
  solve_family op rhss =
    (iterate_while
       (initial_family_state rhss)            -- carry = (remaining RHSs, accumulated solutions)
       (\st -> not (null st.remaining))       -- continue while RHSs remain
       (\st -> let inp  = head st.remaining
                   sol  = ksp_solve op inp     -- the SHARED op is captured, not re-passed per elem
               in { state: { remaining: tail st.remaining
                           , solutions: st.solutions }
                  , extras: sol }))            -- per-element extra = the solution
      .trajectory                              -- == [ksp_solve op inp | inp <- rhss]

  -- the family input/output records (TS brace form):
  -- FamilyInputs  = { op: OpParams, rhss: [Inputs] }   -- op captured ONCE (shared across the map)
  -- FamilyOutputs = { solutions: [SimState] }          -- collected solution family
  ```

  The load-bearing structural fact the signature encodes: **`op : OpParams` is bound once, outside
  the `map`**, and threaded *unchanged* into every `ksp_solve` call — this is the L4 typing of the
  `ksp.SetOperators(*K,*K)`-outside-the-loop capture. Per `state-stratification`
  (`book/src/concepts/state-stratification.md`), `op` is the `readonly` operator stratum shared
  across the family; each element's `SimState` is independent (no cross-element threading).

- **Algebraic intuition:**
  - **Map-fusion / naturality** (the load-bearing law): `solve_family op (rhss₁ ++ rhss₂) =
    solve_family op rhss₁ ++ solve_family op rhss₂` — the family map is a list homomorphism
    (concatenation-preserving) *because the operator is shared and each solve is independent*. This
    is what licenses splitting/reordering the family (and, downstream, the embarrassingly-parallel
    realization). It is the structural payoff of operator-capture-once.
  - **Operator-capture-once / `SetOperators`-hoist** (the identity that makes the combinator
    worth naming): `solve_family op rhss = map (ksp_solve op) rhss` and the `op`-dependent solver
    construction (`fresh_ksp op`) is **invariant across the map**, so it hoists out of the loop —
    matching `SetOperators(*K,*K)` being outside the `for`. The general superset form lacks this
    hoist (the operator is per-element), which is exactly why driven cannot use `solve_family`.
  - **No identity element in the family-arg** in the algebraic sense: `solve_family op []` is the
    empty family `[]` (a degenerate, not algebraic, identity — same flavor as the `ksp_solve`
    zero-RHS short-circuit, `L4/ksp_solve.md:114`); Palace `MFEM_VERIFY(n_step > 0, ...)`
    (`electrostaticsolver.cpp:42`, `magnetostaticsolver.cpp:42-43`) excludes the empty family at the
    source level.
  - **Independence / commutativity of elements**: the solutions do not depend on family order
    (`x_i` depends only on `(op, rhs_i)`); the *collection* preserves order (`solutions[i]`
    aligns with `rhss[i]`). The map is order-preserving; the underlying solves commute.
  - **Does NOT distribute over operator composition**: `solve_family (op₁ ∘ op₂) rhss ≠
    solve_family op₁ (solve_family op₂ rhss)` in general (inherited from the `ksp_solve`
    nested-cap non-commutativity, `L4/ksp_solve.md:116`).

- **Variant axes:**
  - **operator-capture** (`fixed | per-element`) — THE load-bearing axis. `fixed` (this combinator,
    `solve_family`): operator captured once, `SetOperators` hoisted. `per-element` (the superset
    `map_solve_over_(operator,rhs)_family`): operator rebuilt per family-element, `SetOperators`
    inside the map. Electrostatic + magnetostatic are `fixed`; driven is `per-element`.
  - **family-index domain** (`terminal-boundary | surface-current-boundary | frequency | ...`) —
    the index set the family ranges over. Absorbed into `[Inputs]`; does not shape the combinator
    (it is just the list the map runs over). Terminal boundaries (electrostatic), surface-current
    boundaries (magnetostatic), frequencies (driven, superset only).
  - **element-type** (`real | complex`) — absorbed into `OpParams` / `Inputs` as at the `ksp_solve`
    cap (`L4/ksp_solve.md:153`). Electrostatic real, magnetostatic real, driven complex.
  - **collection-shape** (`pre-sized vector | append`) — Palace pre-sizes `std::vector<Vector>
    V(n_step)` and indexes by `step`; transparent (the L4 `trajectory`/`map` result is the family,
    indexing is a lowering concern). Not a semantic axis.

## Proposed changes

```edit:book/src/L4/index.md
[append to the "Operator dep-map" table, after the `eigsolve` row (line 75), a new rough-in row:]

| `solve_family` *(rough-in)* | `solve_family :: OpParams -> [Inputs] -> [SimState]`; entry `solve_family op rhss = map (\inp -> ksp_solve op inp) rhss`. The fixed-operator map-over-RHS-family outer-driver combinator: capture the system operator `op` once (the L4 typing of `SetOperators(*K,*K)` hoisted outside the loop), build the solver once, map the [`ksp_solve`](./ksp_solve.md) cap over the RHS family `[rhs_i]`, collect the solution family `[x_i]`. The pure-map degenerate of the strawman §3.7 `iterate_while` family (each element independent, no carry; the trajectory IS the collected family). Sits *above* the `ksp_solve` cap (one shell further out than `solve_loop`: `solve_loop` iterate-whiles over inner cycles, `solve_family` maps over an independent RHS family). | Concepts: `state-stratification` (`op` is the shared `readonly` operator stratum captured once; each element's `SimState` independent), `solve-monad`, `derived-view-hoisting`, `variant-absorption` (the operator-capture axis). L4 rows: [`ksp_solve`](./ksp_solve.md) (the mapped per-element cap); [`iterate-while`](./iterate-while.md) (the pure-map degenerate body). | L3 explicit `std::vector<Vector>`-accumulating loop with the operator-construction hoisted outside (the Palace C++ outer-sweep shape); L4>L3 theme `L4-L3/solve-family-map-dissolution` *(batch-17; pending)*. | `rough-in` (proposed-by: combinator-miner:2026-06-02T002600Z-combinator-miner-solve-family-combinator; 2 fixed-operator witnesses electrostatic `palace/drivers/electrostaticsolver.cpp:30-90` + magnetostatic `palace/drivers/magnetostaticsolver.cpp:30-100`; the driven pipeline `drivensolver.cpp:176-180` is the `per-element`-axis superset, batch-17-gated) |
```

Note: this report does **not** create `book/src/L4/solve_family.md` (harvester's job — formalization) and does **not** register a `SUMMARY.md` row (the rough-in row names a chapter that does not yet exist; per the forward-reference convention the dep-map cell is plain-text/inline-code `solve_family`, NOT a live link, and no `SUMMARY.md` entry is added until the harvester authors the file). The `[`ksp_solve`](./ksp_solve.md)` / `[`iterate-while`](./iterate-while.md)` links inside the row ARE live (those targets exist on disk).

## Supporting evidence

- **Fixed-operator witnesses (positive):**
  - `palace/drivers/electrostaticsolver.cpp:30` (operator once), `:35-36` (solver once,
    `SetOperators(*K,*K)`), `:60-90` (outer sweep over `GetSources()`), `:68-69` (RHS + `ksp.Mult`),
    `:46` + `:89` (collect `V[step]`). Read in full this dispatch.
  - `palace/drivers/magnetostaticsolver.cpp:30` (operator once), `:35-36` (solver once,
    `SetOperators(*K,*K)`), `:66-100` (outer sweep over `GetSurfaceCurrentOp()`), `:76-77` (RHS +
    `ksp.Mult`), `:47` + `:99` (collect `A[step]`). Read in full this dispatch.
- **Superset / scope-boundary witness (negative for fixed-operator):**
  - `palace/drivers/drivensolver.cpp:176-180` (operator `A=(K+iωC−ω²M)` rebuilt + `SetOperators`
    INSIDE the loop), `:168-170` (the frequency loop), `:194-196` (per-ω RHS + `ksp.Mult`). Read
    this dispatch.
- **Firm vocabulary grounding:**
  - `book/src/L4/ksp_solve.md:17-40` (the `ksp_solve` cap this combinator maps over), `:100`
    (`solve_loop`-as-`iterate_while_pure` — the iterate-while shell `solve_family` sits beside/above),
    `:114`/`:116` (the zero-RHS-degenerate-identity + nested-cap-non-commutativity laws inherited).
  - `book/src/L4/index.md:30-46` (the L4 outer-driver vocabulary cohort `solve_loop`/`restart_cycle`/
    `Outcome` + the `ksp_solve`/`eigsolve` caps — the layer `solve_family` joins), `:7-13`
    (L4-is-vocabulary remit), `:37` (the `chebyshev` precedent for reusing the `iterate-while`
    family rather than a new iteration vocabulary).
  - `book/src/design/l4_calculus.md:150-184` (§3.7 `iterate_while` + `iterate_while_pure` sugar —
    the value-threaded-loop family the pure-map degenerate joins), `:186-228` (§3.8 demand-pruning —
    governs whether per-element solutions materialize).
  - `book/src/concepts/state-stratification.md` (the `readonly` operator-stratum-shared-across-the-
    family typing).
- **No dedicated test exercises the outer sweep** (the `Solve(mesh)` drivers are integration-level,
  not unit-tested under `reference/palace/test/unit/`); the L0 evidence is the driver source above.
  This keeps the rough-in at `rough-in` (test-coverage-bounded for its map-fusion law) until a
  harvester firms the laws against the strawman §3.7 family.

## Open questions / caveats

- **2-of-5-pipelines scope is explicit and load-bearing.** `solve_family` (fixed-operator) is
  witnessed by electrostatic + magnetostatic ONLY. The other three pipelines: **driven** breaks it
  (operator per-frequency, `drivensolver.cpp:176-180`); **transient** and **eigenmode** are
  unprobed this dispatch. Do NOT claim cross-pipeline generality beyond the 2 fixed-operator
  witnesses.

- **General-form superset probe (BATCH-17, 3rd-probe-gated).** The superset
  `map_solve_over_(operator,rhs)_family :: [(OpParams, Inputs)] -> [SimState]` (operator per
  family-element) has `solve_family` as the `operator=const`-across-the-family specialization. The
  **driven** pipeline is a witness of the superset (operator rebuilt per-ω). Before promoting the
  *general* form, batch-17 should run a 3rd probe: (i) confirm driven's per-ω operator rebuild is
  the only difference from the fixed form (i.e. the map structure is otherwise identical), and
  (ii) check whether **transient** (time-stepping) is a `map`-over-family at all or a genuine
  *fold* (state carried between steps) — if transient carries state, it is `solve_loop`-shaped, not
  `solve_family`-shaped, and does NOT join this family. The general form should be proposed only
  after the transient/eigenmode shape is known, to avoid over-unifying a fold into a map. OQ:
  `solve-family-general-operator-rhs-superset-probe` (batch-17).

- **Two specialization entries sequenced to batch-17.** Per replace-and-propagate, the
  electrostatic + magnetostatic outer sweeps are `solve_family`'s specializations (notes under the
  combinator). Authoring their dedicated entries (the per-pipeline `solve_family` instances with
  their index-domain + RHS-construction + post-processing specifics) is batch-17 work; this c054
  landing is the **combinator dep-map row + the specialization pointers** (named in the row's
  provenance), not the two specialization chapters. Flag for cycle-planner: schedule the two
  specialization entries + the `L4-L3/solve-family-map-dissolution` theme in batch-17.

- **L4>L3 dissolution not authored here.** The `solve_family` → L3 explicit accumulating loop
  rotation (the `map` collapsing to a `std::vector<Vector>`-accumulating `for`, the operator
  construction hoisting outside) is a batch-17 L4>L3 theme (`L4-L3/solve-family-map-dissolution`),
  named in the rough-in row's "Lowers to" cell as pending. Per high→low discipline, this entry
  defines `solve_family` in L4 vocabulary only.

- **Map-fusion law confidence is test-coverage-bounded.** The concatenation-homomorphism law
  (`solve_family op (a ++ b) = solve_family op a ++ solve_family op b`) is the load-bearing payoff
  but is stated against the strawman §3.7 family, not confirmed by a dedicated test (the drivers are
  integration-level). The harvester should mark the law `rough-in (test-coverage-bounded)` until
  either a strawman-derivation firms it or a dedicated test appears.

- **Naming.** I propose `solve_family` over `map_solve` because (a) it signals the *family*
  (the collected `[x_i]`) as the unit, (b) it parallels `solve_loop` (both `solve_`-prefixed
  outer-driver verbs), and (c) `map_solve` reads as the general superset (which IS a `map` over
  `(op, rhs)` pairs). Reserve `map_solve` (or `map_solve_over_(operator,rhs)_family`) for the
  batch-17 superset. The harvester / same-layer-cross-cutter may revisit if a cleaner pairing
  emerges.
