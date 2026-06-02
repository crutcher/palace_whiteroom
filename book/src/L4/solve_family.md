---
layer: L4
operator: solve_family
firmness: rough-in (test-coverage-bounded)
consumes:
  - book/src/L4/ksp_solve.md (the firm outer-driver cap mapped over the family — the per-element solve)
  - book/src/L4/iterate-while.md (the pure-map degenerate of the strawman §3.7 iterate_while family)
  - book/src/concepts/state-stratification.md (op is the shared readonly operator stratum captured once; each element's SimState independent)
lowers_to:
  - book/src/L4-L3/solve-family-map-dissolution.md (the L4>L3 dissolution to the L3 explicit std::vector<Vector>-accumulating outer sweep — the authoritative L3-form home; NO standalone L3/solve_family entry, per the cycle-057 D1 NO-ENTRY warrant: the family loop carries no sequential-obstruction, so the L3 form is fully + concisely expressed by the dissolution theme's §"L3 form (RHS)" — a separate L3 chapter would mirror it)
variant_axes:
  - operator-capture (fixed: this combinator, op captured once / SetOperators hoisted outside the map | per-element: the batch-17 superset map_solve_over_(operator,rhs)_family, op rebuilt per family-element / SetOperators inside the map — driven)
  - family-index-domain (terminal-boundary / surface-current-boundary / frequency — absorbed into [Inputs]; does not shape the combinator)
  - element-type (real / complex — absorbed into OpParams / Inputs as at the ksp_solve cap)
  - collection-shape (pre-sized vector / append — transparent; the trajectory/map result IS the family, indexing is a lowering concern)
---

# solve_family

The L4 **fixed-operator map-over-RHS-family outer-driver combinator**: capture the system operator `op` once, build the solver once, map the [`ksp_solve`](./ksp_solve.md) cap over a family of right-hand sides `[rhs_i]`, and collect the solution family `[x_i]`. Where [`ksp_solve`](./ksp_solve.md) coordinates *one* solve to convergence, `solve_family` is the **next coordination shell out** — it maps the whole `ksp_solve` cap over an *independent* RHS family with a single shared operator capture. It is the **pure-`map` degenerate** of the strawman §3.7 [`iterate-while`](./iterate-while.md) family (each element independent, no carry between solves; the trajectory IS the collected family), reusing the firm iterate-while vocabulary rather than introducing a new iteration primitive — the same route [`chebyshev`](./chebyshev.md) took.

## Context

L4's job is to write algorithms in a graph-evaluation calculus that makes lifetimes, dispatch sites, and effect placement structural (`L4/index.md:7-13`). `solve_family` names a coordination shape one shell *above* the [`ksp_solve`](./ksp_solve.md) cap, analogous to how [`ksp_solve`](./ksp_solve.md)'s `solve_loop` sits above the inner [`krylov-step`](./krylov-step.md) kernel-fold:

- [`ksp_solve`](./ksp_solve.md) names the **per-solve cap** — one RHS → one `SimState` (`ksp_solve op inp = execState (solve_loop op inp) (initial_state inp)`, `L4/ksp_solve.md:38-40`).
- `solve_family` (this entry) names the **per-family shell** — a fixed `op`, a family `[rhs_i]` → the solution family `[x_i]`. It *consumes* [`ksp_solve`](./ksp_solve.md) as its mapped function.

The architectural altitude is the same as `solve_loop`'s — both are value-threaded loop combinators in the strawman's §3.7 family (`book/src/design/l4_calculus.md:150-184`) — but the combinator differs: where `solve_loop` is an **iterate-while** over inner cycles (`L4/ksp_solve.md:100`, "tail-recursion ≡ `iterate_while_pure` over outer cycles"), `solve_family` is a **map** over an independent RHS family. The map is the **pure-map degenerate** of `iterate_while`: each family element is independent (no carry threads between solves), so the per-element "extra" is the solution and the §3.7 `trajectory` IS the collected solution family.

The combinator is defined **in L4 vocabulary** (high→low discipline, CLAUDE.md §Methodology invariants): its semantics, signature, and laws are stated in terms of the [`ksp_solve`](./ksp_solve.md) cap, the [`iterate-while`](./iterate-while.md) family, and the [`state-stratification`](../concepts/state-stratification.md) operator stratum — NOT in terms of L3 value-threading primitives. The L4>L3 dissolution (the `map` collapsing to an L3 explicit `std::vector<Vector>`-accumulating loop with the operator construction hoisted outside the loop) is a separate batch-17 L4>L3 theme (`solve-family-map-dissolution`), narrated forward from L4 to L3; it is **not** authored here.

`solve_family` at L4 is a **methodology-level combinator** distilled from two Palace driver-source sweeps (electrostatic + magnetostatic `Solve(mesh)`), not a Palace-source artefact per se — there is no single L0 range that "is" the L4 `solve_family`. The Palace evidence is the two outer sweeps in §Specializations; L4 names the map combinator and the operator-capture-once stratification those two sweeps share.

## Signature

The combinator captures the operator once, outside the `map`, and threads it unchanged into every per-element [`ksp_solve`](./ksp_solve.md):

    -- entry point: capture the operator once, build the solver once, map ksp_solve over the RHS family
    solve_family :: OpParams -> [Inputs] -> [SimState]
    solve_family op rhss = map (\inp -> ksp_solve op inp) rhss

    -- equivalently, as the pure-map degenerate of the strawman §3.7 iterate_while family
    -- (each element independent; no carry; the "trajectory" IS the collected family):
    solve_family op rhss =
      (iterate_while
         (initial_family_state rhss)          -- carry = { remaining: [Inputs], solutions: [SimState] }
         (\st -> not (null st.remaining))      -- continue while RHSs remain
         (\st -> let inp = head st.remaining
                     sol = ksp_solve op inp     -- the SHARED op is captured, not re-passed per elem
                 in { state: { remaining: tail st.remaining
                             , solutions: st.solutions }
                    , extras: sol }))           -- per-element extra = the solution
        .trajectory                            -- == [ ksp_solve op inp | inp <- rhss ]

Shape contract (bunsen-style; named records and axes; the operator stratum per [`state-stratification`](../concepts/state-stratification.md)):

- `OpParams` — operator-internal configuration, **captured once at family construction; `readonly`** per [`state-stratification`](../concepts/state-stratification.md). This is the load-bearing typing: `op` is bound *once, outside the `map`*, and threaded *unchanged* into every [`ksp_solve`](./ksp_solve.md) call — the L4 typing of the `ksp.SetOperators(*K,*K)`-outside-the-loop capture (electrostatic `electrostaticsolver.cpp:36`, magnetostatic `magnetostaticsolver.cpp:36`). `op` is the *shared* operator stratum across the family; the [`ksp_solve`](./ksp_solve.md)-internal solver construction (`fresh_ksp op`) is invariant across the map and hoists out of it.
- `[Inputs]` — the RHS family the `map` ranges over. The family-index domain (terminal boundaries / surface-current boundaries / …) is *absorbed* into this list — it does not shape the combinator (it is just the list the map runs over). Each `Inputs` element is the per-index RHS that seeds one [`ksp_solve`](./ksp_solve.md)'s `initial_state` (`L4/ksp_solve.md:61`).
- `[SimState]` — the collected solution family. Each element is one [`ksp_solve`](./ksp_solve.md)'s terminal `SimState` (whose `.x` is the per-index solution, `L4/ksp_solve.md:62`). Per the family-map, `solutions[i]` aligns with `rhss[i]` (order-preserving collection).
- `FamilyState = { remaining: [Inputs], solutions: [SimState] }` — the `iterate_while` carry in the degenerate-form rendering; transient (the pure-map form `map (ksp_solve op)` does not name it). Each element's `SimState` is independent — there is **no** cross-element threading (no shared mutable state between solves), which is what makes the map a genuine map and not a fold.

The shape contract makes two things structural at the family level that are merely conventional in the Palace C++ sweep:

1. **The operator is captured once, outside the map.** `op : OpParams` appears once in the signature, bound before the `map`; every per-element solve reads the *same* `op`. This forbids per-element operator mutation at the type level — the property the driven pipeline (operator rebuilt per-ω, `drivensolver.cpp:176-180`) does **not** have, which is exactly why driven cannot use `solve_family`.
2. **Elements are independent; the collection is order-preserving.** Each `SimState` is a fresh, independent solve; the `map` carries no state between elements. The trajectory/collection preserves position (`solutions[i] ↔ rhss[i]`), but the underlying solves commute (reordering the family permutes the output identically).

## Semantics

`solve_family op rhss` is the complete fixed-operator family solve expressed as a `map` of the [`ksp_solve`](./ksp_solve.md) cap over the RHS family with a single shared operator capture. It has two equivalent presentations (the §Signature renders both):

1. **Direct map form** — `solve_family op rhss = map (\inp -> ksp_solve op inp) rhss`. The combinator *is* a `map`: the per-element function `ksp_solve op` closes over the once-captured `op` and is applied independently to each RHS. This is the form the combinator is named for, and the form that makes the algebraic laws (§Algebraic laws) immediate.

2. **Pure-map degenerate of `iterate_while`** — the §3.7 family rendering (`book/src/design/l4_calculus.md:150-184`), where the carry is `{ remaining, solutions }`, the predicate is `not (null st.remaining)`, the step pops one RHS and runs one [`ksp_solve`](./ksp_solve.md), and the per-element `extras` is the solution. By §3.7 the trajectory of extras is exactly `[ ksp_solve op inp | inp <- rhss ]` — the collected family. This presentation reuses the firm [`iterate-while`](./iterate-while.md) family rather than introducing a new iteration vocabulary (the same route [`chebyshev`](./chebyshev.md) took, `L4/index.md:37`); the choice between the two presentations is a presentation rotation, not a semantic distinction (the two produce element-for-element-identical solution families).

The combinator's **structural payoff** — the reason it is worth naming as a combinator rather than leaving the sweep inline — is the **operator-capture-once / `SetOperators`-hoist** stratification. Because `op` is `readonly` and shared across the map, the `op`-dependent solver construction (`fresh_ksp op`, the L4 image of `KspSolver ksp(...); ksp.SetOperators(*K,*K)`) is **invariant across the map and hoists out of it** — exactly matching the Palace sweeps where `SetOperators(*K,*K)` sits *outside* the `for` loop (electrostatic `:35-36` outside the `:60` loop; magnetostatic `:35-36` outside the `:66` loop). The general superset form lacks this hoist (the operator is per-element), which is the scope boundary (§Variant axes).

Per [`state-stratification`](../concepts/state-stratification.md), `op` is the shared `readonly` operator stratum captured once; each element's `SimState` is the independent per-solve stratum (no cross-element threading). The family map does not introduce a new monadic effect — each [`ksp_solve`](./ksp_solve.md) discharges its own `Solve` effect via `execState` (`L4/ksp_solve.md:98`), and the `map` simply collects the discharged terminal `SimState`s. The combinator is therefore a **pure function** `(op, rhss) -> [SimState]` (modulo the per-element non-determinism each [`ksp_solve`](./ksp_solve.md) inherits transitively through [`krylov-step`](./krylov-step.md); the map introduces no additional non-determinism).

### Demand-pruning interaction

Under the §3.8 pruning rule (`book/src/design/l4_calculus.md:186-228`), per-element solutions materialize only when a downstream consumer reads them — `solve_family op rhss` whose result is never observed prunes every solve. In Palace both sweeps unconditionally consume each solution immediately (post-processing per index: electrostatic field/energy measurement `electrostaticsolver.cpp:75-86`, magnetostatic `magnetostaticsolver.cpp:82-96`), so no element prunes in practice; but the combinator's typing makes the demand-driven materialization structural (the pure-map degenerate inherits the §3.7 trajectory's demand-pruning directly).

## Algebraic laws

`solve_family` is a **`map` combinator**, so its laws are the list-homomorphism / naturality laws of `map` specialised to the fixed-operator family, plus the operator-capture-once hoist identity that licenses them. Absences are catalogued explicitly to prevent decoration drift.

1. **Concatenation-homomorphism** (the load-bearing law). `solve_family op (a ++ b) = solve_family op a ++ solve_family op b`. The family map is a list homomorphism — it distributes over concatenation — *because the operator is shared and each solve is independent*. This is what licenses splitting, chunking, or reordering the family (and, downstream, the embarrassingly-parallel realization: the family can be solved in any partition). It is the algebraic statement of the structural payoff: the once-captured `op` makes every element's solve independent of every other.

2. **Operator-capture-once / `SetOperators`-hoist** (the identity that makes the combinator worth naming). `solve_family op rhss = map (ksp_solve op) rhss`, and the `op`-dependent solver construction `fresh_ksp op` is **invariant across the map**, so it hoists out of the map (computed once, before the family is traversed). This is the L4 typing of `SetOperators(*K,*K)` sitting outside the `for` loop (electrostatic `:35-36`/`:60`, magnetostatic `:35-36`/`:66`). **Consequence**: the general superset form `map_solve_over_(operator,rhs)_family` (operator per element) lacks this hoist; the hoist is precisely the `operator-capture = fixed` specialization (§Variant axes), and its absence is why the driven pipeline (`drivensolver.cpp:176-180`, `SetOperators` *inside* the loop) is NOT an instance of `solve_family`.

3. **Element-independence / order-preservation** (the map's naturality). The solutions do not depend on family order — `x_i` depends only on `(op, rhs_i)` — so the underlying solves commute: `solve_family op (permute rhss) = permute (solve_family op rhss)` for any permutation. The *collection* preserves position (`solutions[i] ↔ rhss[i]`), so the map is order-preserving even though the solves commute. (Naturality: `solve_family op . map g = map (solve op . g)` for any RHS-transform `g` that does not touch `op`.)

4. **Empty-family degenerate** (`solve_family op [] = []`). The empty RHS family maps to the empty solution family — a degenerate (not algebraic) identity, the same flavor as [`ksp_solve`](./ksp_solve.md)'s zero-RHS short-circuit (`L4/ksp_solve.md:114`). Palace excludes the empty family at the source level via `MFEM_VERIFY(n_step > 0, …)` (electrostatic `electrostaticsolver.cpp:42`, magnetostatic `magnetostaticsolver.cpp:42-43`), so the empty case is a calculus-level total-definition convenience, not a witnessed Palace path.

Laws that explicitly **do not** hold:

- **Distribution over operator composition.** `solve_family (op₁ ∘ op₂) rhss ≠ solve_family op₁ (solve_family op₂ rhss)` in general — inherited from the [`ksp_solve`](./ksp_solve.md) nested-cap non-commutativity (`L4/ksp_solve.md:116`, `A₁⁻¹ · A₂⁻¹` does not commute). The combinator distributes over *family concatenation* (law 1), not over operator composition.
- **Per-element law uniformity across the operator-capture axis.** The concatenation-homomorphism (law 1) and the hoist (law 2) hold **only** for `operator-capture = fixed`. For the `per-element` superset they do not (the operator differs per element, so the solves are not the *same* `ksp_solve op`, and `fresh_ksp` does not hoist). The laws here are scoped to the fixed-operator combinator (§Variant axes; the superset is batch-17).
- **Cross-element determinism / fusion.** The per-element solves do not fuse into a single closed-form whole-family op — each is an independent iterative solve with its own [`ksp_solve`](./ksp_solve.md) `sequential-obstruction` (`L4/ksp_solve.md:111`). The map collects independent fixed-point computations; it does not collapse them. (The embarrassing-parallelism licensed by law 1 is *independence*, not *fusion*.)
- **Linearity of the readout family in the RHS family.** The `SimState.it` / `.final_res` readout of each element is not linear in its RHS (different RHSes generate different residual histories) — inherited per-element from [`ksp_solve`](./ksp_solve.md) (`L4/ksp_solve.md:112`). Only each terminal `SimState.x` is linear in its `b` (modulo tolerance).

## Specializations

Per replace-and-propagate (CLAUDE.md §Methodology invariants vocabulary-shift redirect), `solve_family` is the **entry**; the two fixed-operator Palace sweeps are **specialization notes re-expressing THROUGH it**, not separate rectangular leaf chapters. Both instantiate `solve_family op rhss = map (ksp_solve op) rhss` with the same operator-capture-once shape; they differ only in the absorbed family-index domain, the RHS-construction call, and the post-processing (all of which are absorbed into `[Inputs]` / consume the `[SimState]` and so do **not** shape the combinator).

- **Electrostatic terminal-boundary sweep** (`palace/drivers/electrostaticsolver.cpp`, `ElectrostaticSolver::Solve`). `op = K = laplace_op.GetStiffnessMatrix()` assembled once (`:30`); the solver built once and the operator captured once via `KspSolver ksp(...)` (`:35`) + `ksp.SetOperators(*K, *K)` (`:36`) — *outside* the loop. The family is the **terminal-boundary index set** `laplace_op.GetSources()` (`:60`); per index, `laplace_op.GetExcitationVector(idx, *K, V[step], RHS)` (`:68`) forms the per-index RHS and `ksp.Mult(RHS, V[step])` (`:69`) is the per-element `ksp_solve op inp` writing into the collected family slot. The solution family is `std::vector<Vector> V(n_step)` (`:46`), index-collected by `step++` (`:89`). Element-type: real.

- **Magnetostatic surface-current sweep** (`palace/drivers/magnetostaticsolver.cpp`, `MagnetostaticSolver::Solve`). `op = K = curlcurl_op.GetStiffnessMatrix()` assembled once (`:30`); solver built once + operator captured once via `KspSolver ksp(...)` (`:35`) + `ksp.SetOperators(*K, *K)` (`:36`) — *outside* the loop. The family is the **surface-current-boundary index set** `curlcurl_op.GetSurfaceCurrentOp()` (`:66`); per index, `curlcurl_op.GetExcitationVector(idx, RHS)` (`:76`) forms the per-index RHS and `ksp.Mult(RHS, A[step])` (`:77`) is the per-element `ksp_solve op inp` writing into the collected family slot. The solution family is `std::vector<Vector> A(n_step)` (`:47`), index-collected by `step++` (`:99`). Element-type: real.

Both sweeps are **structurally identical** down to the `GetStiffnessMatrix()` / `SetOperators(*K,*K)`-outside-the-loop / `GetSources`-vs-`GetSurfaceCurrentOp` family-domain / `std::vector<Vector>` collect shape. The differences (which `*Operator` constructs the RHS, which `*ErrorEstimator` post-processes each solution) are absorbed into the family-index domain and the per-element consumer; they are *lowering-and-consumer* concerns, not combinator structure. (If the per-pipeline specifics — the RHS-construction operator family, the per-index post-processing chain — prove large enough to warrant dedicated chapters, that is an integrator size-judgment; the default here is notes-in-entry per combinator-as-entry.)

## Dependencies

L4 rows this combinator consumes:

- [`ksp_solve`](./ksp_solve.md) — the firm outer-driver cap mapped over the family (the per-element `ksp_solve op inp`). `solve_family` consumes it as its mapped function; one shell out from it.
- [`iterate-while`](./iterate-while.md) — the §3.7 family whose **pure-map degenerate** the combinator IS (each element independent, no carry; the trajectory is the collected family). Reused rather than introducing a new iteration vocabulary, the [`chebyshev`](./chebyshev.md) route.

L4 concept references:

- [`state-stratification`](../concepts/state-stratification.md) — the operator stratum: `op` is the shared `readonly` operator stratum captured once across the family; each element's `SimState` is the independent per-solve stratum. The capture-once typing is the structural payoff.
- [`solve-monad`](../concepts/solve-monad.md) — the `Solve = StateT SimState Identity` effect each per-element [`ksp_solve`](./ksp_solve.md) discharges; the family map collects the discharged terminal `SimState`s without introducing a new effect.
- [`derived-view-hoisting`](../concepts/derived-view-hoisting.md) — the §3.8 demand-pruning governing whether per-element solutions materialize (inherited from the §3.7 trajectory).
- [`variant-absorption`](../concepts/variant-absorption.md) — the operator-capture axis (`fixed | per-element`) and the family-index / element-type absorption into `OpParams` / `[Inputs]`.

**Strawman reference**: `book/src/design/l4_calculus.md` §3.7 (`iterate_while` + the `iterate_while_pure` sugar, `:150-184`) is the family this combinator's pure-map degenerate joins; §3.8 (demand-pruning, `:186-228`) governs per-element materialization.

## Lowers to

L4 `solve_family` lowers to an L3 explicit `std::vector<Vector>`-accumulating outer sweep (the Palace C++ shape, §Specializations) with the operator construction hoisted outside the loop — via the L4>L3 dissolution theme `solve-family-map-dissolution` (**batch-17; pending — dispatch #2 of cycle-055 authors it**; canonical slug `solve-family-map-dissolution`). The rotation is **substantive** (not identity-in-form): the `map` collapses to a positional `for`-loop accumulating into a pre-sized `std::vector<Vector>` indexed by `step`; the `op`-capture-once hoist becomes the `SetOperators(*K,*K)`-outside-the-`for` placement; the pure-map trajectory becomes the positional `V[step]` / `A[step]` collection. This entry records the rotation *direction* (L4 map combinator → L3 explicit accumulating loop) in-line per high→low discipline; it does **not** author the theme. There is **no standalone `L3/solve_family` entry** (cycle-057 D1 NO-ENTRY warrant): the L4>L3 map-shell rotation is substantive, but the resulting L3 family loop carries **no `sequential-obstruction`** (the family members are independent — embarrassingly parallel, written sequentially), so L3's iteration-rotation content for the family shell is the *negative* finding "the loop lifts" — already stated, in L3 vocabulary, in the dissolution theme's §"L3 form (RHS)" + §"What does NOT change" (where it is explicitly contrasted against the obstruction-carrying [`L3/ksp_solve`](../L3/ksp_solve.md)). A separate L3 chapter would mirror the dissolution theme's RHS, not shift vocabulary (the 2026-06-01 VOCABULARY-SHIFT REDIRECT anti-mirror principle). The authoritative L3-form home for the family shell is therefore the dissolution theme itself; the per-member solve `ksp.Mult` delegates to the firm [`L3/ksp_solve`](../L3/ksp_solve.md), which DOES carry its own (per-solve outer-loop) obstruction.

## Variant axes

Four axes, one load-bearing (operator-capture) and three absorbed:

1. **operator-capture** (`fixed | per-element`) — **THE load-bearing axis**, and the scope boundary of this combinator. `fixed` (this combinator, `solve_family`): operator captured once outside the map, `SetOperators` hoisted (electrostatic + magnetostatic). `per-element` (the batch-17 superset `map_solve_over_(operator,rhs)_family`): operator rebuilt per family-element, `SetOperators` *inside* the map (driven, `drivensolver.cpp:176-180`). The concatenation-homomorphism (law 1) and the hoist (law 2) hold ONLY for `fixed`. **This combinator claims `fixed` only** (§Status scope caveat).
2. **family-index domain** (`terminal-boundary | surface-current-boundary | frequency | …`) — the index set the family ranges over. **Absorbed into `[Inputs]`**; does not shape the combinator (it is just the list the map runs over). Terminal boundaries (electrostatic `electrostaticsolver.cpp:60`), surface-current boundaries (magnetostatic `magnetostaticsolver.cpp:66`); frequencies (driven, the `per-element` superset only).
3. **element-type** (`real | complex`) — absorbed into `OpParams` / `Inputs` as at the [`ksp_solve`](./ksp_solve.md) cap (`L4/ksp_solve.md:153`). Electrostatic real, magnetostatic real; driven complex (superset only).
4. **collection-shape** (`pre-sized vector | append`) — Palace pre-sizes `std::vector<Vector> V(n_step)` and indexes by `step` (electrostatic `:46`/`:89`, magnetostatic `:47`/`:99`); transparent — the L4 `trajectory` / `map` result IS the family, the pre-sizing-and-indexing is a lowering concern. Not a semantic axis.

## Status

`rough-in (test-coverage-bounded)` — the combinator's **structural signature is well-anchored** at L0 (the input/output family shape, the operator-capture-once stratification, the variant axes are all witnessed by two structurally-identical fixed-operator driver sweeps: electrostatic `electrostaticsolver.cpp:30-90` + magnetostatic `magnetostaticsolver.cpp:30-100`). But the **algebraic-law confidence is reduced pending dedicated test coverage**: the load-bearing concatenation-homomorphism (law 1) and the hoist (law 2) are stated against the strawman §3.7 family and the map list-homomorphism algebra, *not* confirmed by a dedicated unit test — the `Solve(mesh)` drivers are integration-level, with no `test-*.cpp` exercising the outer sweep under `reference/palace/test/unit/`. Per CLAUDE.md §Methodology invariants ("Two rough-in qualifiers are first-class"), this is the `rough-in (test-coverage-bounded)` tier: the structure is firm but the *laws* are stated-but-test-unconfirmed (distinct from `partly-constructive`, which is firm-structure + a *constructed* sub-part). **Promotion route**: a dedicated test exercising the family-map's concatenation/independence laws at the `Solve(mesh)` entry point (out of project write-scope while no driver-level unit test exists), OR a literature/strawman-derivation harvester pass that raises the list-homomorphism law confidence to `ksp_solve`-equivalent (the map is a standard total list combinator, so the strawman-derivation route is the more likely one). NOTE the firm-on-positive-structure consideration: the concatenation-homomorphism *is* a syntactic identity on `map` (and the operator-capture-once hoist *is* read directly off the positive `SetOperators`-outside-the-loop source), which is an argument toward `firm`; but the load-bearing claim the law *encodes* — that each element's solve is genuinely independent given the shared `op` (no hidden cross-element state in the `KspSolver` reuse) — is the part that the integration-level-only coverage leaves test-unconfirmed, so this entry honors the planner default of `rough-in (test-coverage-bounded)` rather than `firm`. The default may be revisited by a batch-17 lowering-verifier pass confirming the `KspSolver`-reuse carries no cross-element state.

**Scope (load-bearing)**: `solve_family` (fixed-operator) is witnessed by **electrostatic + magnetostatic ONLY** (2-of-5 pipelines). The other three: **driven** breaks shared-operator-capture (operator rebuilt per-frequency, `drivensolver.cpp:176-180`, `SetOperators` inside the loop) — it is a witness of the `per-element` superset `map_solve_over_(operator,rhs)_family`, NOT of `solve_family`; **transient** is unprobed (the canonical `fold` candidate, now homed at [`fold_solve`](./fold_solve.md)); **eigenmode** was probed (cycle-059 cross-layer-cross-cutter, `reports/2026-06-02T061737Z-cross-layer-cross-cutter-eigenmode-outer-machinery-probe/CYCLE.md`) and is **NOT a witness** of either `solve_family` or `fold_solve` — the eigenmode driver calls the opaque `eigen->Solve()` once (`eigensolver.cpp:367`), with no operator/RHS family to map and no state-threaded solve-march to fold; its only outer loop is a post-processing *readout* map over the already-converged eigenpair set (`eigensolver.cpp:425-471`). Do NOT claim cross-pipeline generality beyond the two fixed-operator witnesses. The general superset is **batch-17 future work** (OQ `solve-family-general-operator-rhs-superset-probe`), gated on a 3rd probe (confirm driven's per-ω rebuild is the only difference; check whether transient is a `map` or a stateful `fold`/`solve_loop` shape — a fold does NOT join this family).

This dispatch (cycle-055 D1) is the **L4 combinator firm-up** completing the headline batch-16 mine (`reports/2026-06-02T002600Z-combinator-miner-solve-family-combinator`), per replace-and-propagate (the combinator is the entry; the two sweeps are specialization notes under it). The L4>L3 dissolution theme (`L4-L3/solve-family-map-dissolution`) is dispatch #2's job this cycle; this entry records the rotation direction in-line but does not author the theme.

## L4 vs L3 distinction

- **L3**: value-threaded explicit outer sweep — a positional `for`-loop accumulating into a pre-sized `std::vector<Vector>` indexed by `step`, the operator construction hoisted outside the loop by hand (the Palace C++ shape). The map combinator collapses to the explicit accumulating loop; the operator-capture-once is a coding convention (`SetOperators` placed outside the `for`), not a type-level stratification.
- **L4**: the `map` combinator `solve_family op rhss = map (ksp_solve op) rhss`. The operator-capture-once is *structural* — `op : OpParams` is `readonly`, bound once outside the map; the family map is a list homomorphism (law 1); per-element independence is typed (no cross-element threading). The L4>L3 dissolution erases the map-combinator naming and the `readonly` typing, recovering the L3 explicit accumulating loop.

## Evidence

`solve_family` at L4 is a methodology-level combinator distilled from two Palace driver sweeps; Palace's C++ does not realise the L4 map form (it writes the explicit accumulating loop). All L0 citations self-verified against on-disk source this dispatch (exact-line anchor checks).

- **Fixed-operator witnesses (positive):**
  - `palace/drivers/electrostaticsolver.cpp:30` (operator `K` assembled once), `:35` (`KspSolver ksp(...)` built once), `:36` (`ksp.SetOperators(*K, *K)` — operator captured once, outside the loop), `:46` (`std::vector<Vector> V(n_step)` family storage), `:60` (`for (const auto &[idx, data] : laplace_op.GetSources())` outer sweep over the terminal-boundary index family), `:68` (`laplace_op.GetExcitationVector(idx, *K, V[step], RHS)` per-index RHS), `:69` (`ksp.Mult(RHS, V[step])` per-element solve), `:89` (`step++` family collection), `:42` (`MFEM_VERIFY(n_step > 0, …)` empty-family exclusion).
  - `palace/drivers/magnetostaticsolver.cpp:30` (operator `K` assembled once), `:35` (`KspSolver ksp(...)` built once), `:36` (`ksp.SetOperators(*K, *K)` — operator captured once, outside the loop), `:47` (`std::vector<Vector> A(n_step)` family storage), `:66` (`for (const auto &[idx, data] : curlcurl_op.GetSurfaceCurrentOp())` outer sweep over the surface-current-boundary index family), `:76` (`curlcurl_op.GetExcitationVector(idx, RHS)` per-index RHS), `:77` (`ksp.Mult(RHS, A[step])` per-element solve), `:99` (`step++` family collection), `:42-43` (`MFEM_VERIFY(n_step > 0, …)` empty-family exclusion).
- **Superset / scope-boundary witness (negative for fixed-operator):**
  - `palace/drivers/drivensolver.cpp:168` (`for (std::size_t omega_i = …)` the frequency loop), `:176` (`auto A = space_op.GetSystemMatrix(1.0 + 0.0i, 1i * omega, -omega * omega + 0.0i, …)` operator rebuilt per-ω, INSIDE the loop), `:180` (`ksp.SetOperators(*A, *P)` operator captured INSIDE the loop). The frequency-dependent operator `A = (K + iωC − ω²M)` cannot be fixed; this is the `per-element` superset, used as the scope boundary, not as supporting evidence for the fixed combinator.
- **Firm vocabulary grounding:**
  - `book/src/L4/ksp_solve.md:17-40` (the cap this combinator maps over), `:98` (the `execState`-discharge making each per-element solve a pure function), `:100` (the `solve_loop`-as-`iterate_while_pure` precedent for reusing the iterate-while family), `:111`/`:114`/`:116` (the per-element `sequential-obstruction` + zero-RHS-degenerate + nested-cap-non-commutativity laws inherited).
  - `book/src/L4/index.md:30-47` (the L4 outer-driver vocabulary cohort `solve_family` joins), `:7-13` (L4-is-vocabulary remit), `:37` (the `chebyshev` precedent for reusing the iterate-while family).
  - `book/src/design/l4_calculus.md:150-184` (§3.7 `iterate_while` + `iterate_while_pure` sugar — the family the pure-map degenerate joins), `:186-228` (§3.8 demand-pruning).
  - `book/src/concepts/state-stratification.md` (the `readonly` operator-stratum-shared-across-the-family typing).
- **No dedicated test** exercises the `Solve(mesh)` outer sweep (the drivers are integration-level, not unit-tested under `reference/palace/test/unit/`); the L0 evidence is the driver source above. This keeps the entry at `rough-in (test-coverage-bounded)` for its map-fusion / concatenation-homomorphism laws.
- **Provenance**: mined by `reports/2026-06-02T002600Z-combinator-miner-solve-family-combinator/CYCLE.md` (c054 D1; the signature, layer justification, laws, 2 witnesses); landed as the rough-in dep-map row `book/src/L4/index.md:76`; firmed (to `rough-in (test-coverage-bounded)`) by this dispatch (cycle-055 D1).
