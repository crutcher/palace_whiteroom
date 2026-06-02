---
agent: abstractor
invoked_at: 2026-06-02T010800Z
scope: L4>L3 theme sketch — solve-family-map-dissolution
status: integrated
integrated_at: 2026-06-02T034000Z
integration_commit: e9bbbbf9fcee8786ad94305a482f6835d2e0f40b
integration_notes: "D2 cycle-055. Applied clean — new book/src/L4-L3/solve-family-map-dissolution.md (firm, the outer map-shell dissolution completing the solve_family propagation, composes above ksp-solve-driver-dissolution; firm-on-structure, no sequential obstruction) + L4-L3/index theme-list row + §Vocabulary-cohort seed bullet + SUMMARY. Same-cycle cross-ref warning discharged (D1 landed solve_family.md first). L4>L3 firm 6→7."
inputs:
  - reports/2026-06-02T010700Z-harvester-solve-family-firm-entry/CYCLE.md (c055 D1 — the LHS L4 solve_family firm entry; signature, laws, 2 witnesses, status)
  - book/src/L3/ksp_solve.md (the L3 value-threaded per-member outer-driver loop — the per-element target)
  - book/src/L4-L3/ksp-solve-driver-dissolution.md (the inner per-solve driver-half this theme composes ABOVE)
  - book/src/L4-L3/index.md (the L4>L3 theme-list table — own row registration)
  - palace/drivers/electrostaticsolver.cpp:30-90 (operator-hoist + accumulating-loop witness 1)
  - palace/drivers/magnetostaticsolver.cpp:30-100 (operator-hoist + accumulating-loop witness 2)
  - palace/drivers/drivensolver.cpp:176-180 (per-element-operator scope-boundary witness — NOT this theme)
---

# CYCLE: L4>L3 theme sketch — solve-family-map-dissolution

## Summary

Authors the L4>L3 lowering theme `book/src/L4-L3/solve-family-map-dissolution.md` — the **outer map-shell dissolution** for the cycle-055 `solve_family` propagation lead. The LHS is the firm-structure L4 `solve_family` combinator D1 authored this cycle (`map (\inp -> ksp_solve op inp) rhss`); the RHS is the L3 explicit positional accumulating outer loop. The theme narrates FORWARD (L4→L3) the genuine vocabulary translation: the L4 `map` over an independent RHS family **dissolves** into an L3 positional `for` over the index family, each iteration writing into a pre-sized `std::vector<Vector>` collection slot indexed by `step`. The **load-bearing dissolution detail** is the **operator-capture hoist**: the L4 once-captured `op` (the `readonly` operator stratum bound outside the `map`) dissolves into the L3 `SetOperators(*K,*K)` / `KspSolver ksp(...)` construction placed *outside* the `for` loop, by hand — exactly matching both Palace sweeps (electrostatic `:35-36` outside `:60`; magnetostatic `:35-36` outside `:66`). This theme is the **outer-shell** companion that **composes strictly ABOVE** the existing inner per-solve `ksp-solve-driver-dissolution` (firm c048): the outer map-shell dissolves here; each per-member solve `ksp_solve op inp` dissolves into the L3 value-threaded `ksp_solve` driver via that existing theme. The rotation is **substantive** (a genuine `map`-combinator → explicit-accumulating-loop translation with operator-hoist), NOT an identity-in-named-terms rename. Status is **`firm`** on the structural rotation (the map→accumulating-loop + operator-hoist shape is read directly off positive Palace source and does not depend on the LHS's test-gated independence law), with the inherited LHS `rough-in (test-coverage-bounded)` caveat scoped to the *upstream cap's laws*, not to this rotation's shape — reasoning stated in §Status. Scope is fixed-operator (2-of-5 pipelines); the driven per-element-operator superset is the explicit scope boundary, batch-17-gated.

All L0 citations self-verified against on-disk source this dispatch (`sed -n` exact-line anchor checks; all 14 anchors landed exact — electrostatic `:30`/`:35`/`:36`/`:46`/`:60`/`:68`/`:69`/`:89`, magnetostatic `:30`/`:35`/`:36`/`:47`/`:66`/`:76`/`:77`/`:99`, driven `:176`/`:180`; both `MFEM_VERIFY` n_step gates at `:42`).

## Proposed changes

```new:book/src/L4-L3/solve-family-map-dissolution.md
# solve-family-map-dissolution

The L4>L3 lowering theme for the [`solve_family`](../L4/solve_family.md) **outer map-shell** — the L4 fixed-operator map-over-RHS-family combinator `solve_family op rhss = map (\inp -> ksp_solve op inp) rhss` that captures the system operator once, builds the solver once, and maps the [`ksp_solve`](../L4/ksp_solve.md) cap over a family of right-hand sides. The theme dissolves the L4 `map` combinator (the once-captured `readonly` `op` stratum, the pure-map-over-an-independent-family shape, the order-preserving trajectory collection) into the L3 **explicit positional accumulating outer loop**: a `for` over the family-index set, the operator construction hoisted by hand outside the loop, each iteration writing one solution into a pre-sized `std::vector<Vector>` collection slot. It is the **outer-shell** companion to the inner per-solve [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md): that theme dissolves *one* `ksp_solve op inp` per-member solve into the L3 value-threaded driver; this theme dissolves the *map shell around the family of solves*. It **composes strictly above** the per-solve driver dissolution.

## Slug

`solve-family-map-dissolution`

## Context

The cycle-055 D1 harvester firmed [`solve_family`](../L4/solve_family.md) — the L4 **fixed-operator map-over-RHS-family outer-driver combinator**, one coordination shell *above* the [`ksp_solve`](../L4/ksp_solve.md) cap. The combinator's own §"Lowers to" names the dissolution to L3 as **substantive** (not identity-in-form) and records the rotation *direction* in-line per the high→low discipline, but defers the theme itself to "a separate batch-17 L4>L3 theme (`solve-family-map-dissolution`), narrated forward from L4 to L3". This chapter is that theme (canonical slug `solve-family-map-dissolution`, cycle-055 dispatch #2).

The L4>L3 hop for the iterative-solve family is now **stratified across the coordination shells**, each shell a dedicated theme one level out from the last:

- [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) (firm) — the **per-step body**: the L4 `krylov-step` typed wrapper → the L3 value-threaded kernel `(op, K, s) -> (K', s', outputs)`.
- [`iterate-while-dissolution`](./iterate-while-dissolution.md) (firm c047) — the **inner-fold combinator**: the L4 `iterate_while` → the L3 `iterate_while_L3` tail-recursive worker the inner solve-loop invokes.
- [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md) (firm c048) — the **per-solve outer driver**: the L4 `solve_loop` / `restart_cycle` / `Outcome` coordination of *one* solve → the L3 value-threaded outer-driver fold [`L3/ksp_solve`](../L3/ksp_solve.md) `(op, K_0, s_0) -> (s_final, result)`.
- `solve-family-map-dissolution` (this theme) — the **family map shell**: the L4 `map` of the `ksp_solve` cap over a *family* of RHSs, with the once-captured shared operator → the L3 explicit positional accumulating `for` over the family-index set, the operator construction hoisted outside the loop, each member written into a pre-sized collection slot.

The four compose, shell by shell: the full L4 `solve_family` combinator lowers to the full L3 explicit family-sweep by applying **this theme** to the outer map shell, and [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md) to each per-member solve `ksp_solve op inp` the map runs (which itself composes [`iterate-while-dissolution`](./iterate-while-dissolution.md) to the inner fold and [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) to the per-step body). This theme is the **dedicated home** for the outermost shell — a reader navigating from the firm [`solve_family`](../L4/solve_family.md) §"Lowers to" lands here, at the map-shell dissolution, rather than re-deriving it inline or conflating it with the per-solve driver theme.

The rotation direction is **L4 → L3**, narrated forward per the high→low discipline (CLAUDE.md §Methodology invariants "Layers are defined high→low"). Notes about the reverse lift (how the L3 explicit accumulating loop lifts back into the `map` combinator, what evidence licenses the lift) live in the cap's §"L4 vs L3 distinction" and in this report's working notes, not in this formal chapter.

This is a **genuine vocabulary translation, not an identity-in-named-terms rename** (CLAUDE.md §Methodology invariants vocabulary-shift redirect). The L4 vocabulary — `map`, the `readonly` once-captured operator stratum, the pure-map-over-an-independent-family shape, the order-preserving trajectory — is a *different semantic organization* from the L3 vocabulary — an explicit positional `for` over an index set, a hand-hoisted operator construction, a pre-sized mutable collection indexed by a running counter. The reorganization (a single combinator naming the whole family solve, with capture-once typed structural, dissolving into an imperative accumulating loop with the capture-once as a hand-placed coding convention) is the substance of the theme.

## L4 form (LHS)

The L4 [`solve_family`](../L4/solve_family.md) combinator — the firm-structure D1 outer-driver map shape (the firm entry §Signature). The entry point, transcribed from the firm cap:

    -- entry point: capture the operator once, build the solver once, map ksp_solve over the RHS family
    solve_family :: OpParams -> [Inputs] -> [SimState]
    solve_family op rhss = map (\inp -> ksp_solve op inp) rhss

    -- equivalently, the pure-map degenerate of the strawman §3.7 iterate_while family
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

The map-shell machinery this theme dissolves is **three** pieces (distinct from the per-solve driver, inner-fold, and per-step machinery the sibling themes dissolve):

1. **The once-captured `readonly` operator stratum.** `op : OpParams` is bound *once, outside the `map`*, per [`state-stratification`](../concepts/state-stratification.md); it is the shared `readonly` stratum threaded *unchanged* into every per-member [`ksp_solve`](../L4/ksp_solve.md). The `op`-dependent solver construction (`fresh_ksp op`, the L4 image of `KspSolver ksp(...); ksp.SetOperators(*K,*K)`) is **invariant across the map and hoists out of it** — this is the load-bearing dissolution detail.

2. **The `map` over the independent RHS family.** `map (\inp -> ksp_solve op inp) rhss` applies the per-element function `ksp_solve op` (closing over the once-captured `op`) independently to each RHS in `[Inputs]`. The map carries no state between elements — each member's `SimState` is independent (the firm cap §Signature: "no cross-element threading").

3. **The order-preserving trajectory collection.** The `map` result `[SimState]` aligns positionally with `rhss` (`solutions[i] ↔ rhss[i]`), order-preserving even though the underlying solves commute (the firm cap §"Algebraic laws" law 3).

The load-bearing L4 properties this lowering must transport are the cap's family-map identities (the firm cap §"Algebraic laws"): **Law 1 (concatenation-homomorphism)** — `solve_family op (a ++ b) = solve_family op a ++ solve_family op b`, the family map is a list homomorphism; **Law 2 (operator-capture-once / `SetOperators`-hoist)** — the `op`-dependent solver construction is invariant across the map and hoists out of it; **Law 3 (element-independence / order-preservation)** — the solves commute, the collection preserves position.

## L3 form (RHS)

The L4>L3 dissolution produces the L3 **explicit positional accumulating outer loop** — the Palace C++ family-sweep shape (the firm cap §Specializations). The L3 rendering (using the L3 value-thread vocabulary, with the per-member solve delegated to [`L3/ksp_solve`](../L3/ksp_solve.md)):

    -- L3 explicit family-sweep: operator hoisted outside the loop, accumulate into a pre-sized collection
    solve_family_L3 :: (op, rhss) -> solutions
    solve_family_L3 op rhss =
      let ksp       = build_ksp op             -- 1. build the solver ONCE, outside the loop
      let _         = set_operators ksp op     --    capture the operator ONCE (SetOperators outside the for)
      let n_step    = length rhss
      let solutions = pre_size n_step          -- 2. pre-sized collection: std::vector<Vector>(n_step)
      let solutions =                          -- 3. positional accumulating for-loop over the index family
            for_index (0 .. n_step - 1) solutions (\step solutions ->
              let inp                = rhss[step]
              let rhs                = form_excitation op inp        -- per-index RHS construction
              let (s_final, _result) = ksp_solve op K_0 (seed inp)   -- per-member L3 driver (delegated)
              let solutions          = solutions `with` (step, s_final.x)  -- write into the slot
              in solutions)
      in solutions

where:

- **`build_ksp op` + `set_operators ksp op`** are the L3 image of the operator-capture hoist — `KspSolver ksp(...)` (electrostatic `electrostaticsolver.cpp:35`, magnetostatic `magnetostaticsolver.cpp:35`) and `ksp.SetOperators(*K, *K)` (electrostatic `:36`, magnetostatic `:36`), placed *outside* the `for` loop by hand. The L4 `readonly` once-captured stratum dissolves into this explicit placement; there is no type-level enforcement at L3 that the operator is not rebuilt per element — it is a *coding convention* (the construction sits outside the loop).
- **`pre_size n_step`** is `std::vector<Vector> V(n_step)` (electrostatic `:46`) / `std::vector<Vector> A(n_step)` (magnetostatic `:47`) — the pre-sized collection the map result materialises into.
- **`for_index (0 .. n_step - 1)`** is the explicit `for (const auto &[idx, data] : laplace_op.GetSources())` (electrostatic `:60`) / `... : curlcurl_op.GetSurfaceCurrentOp())` (magnetostatic `:66`) accumulating loop over the family-index set, with `step++` (electrostatic `:89`, magnetostatic `:99`) the running collection index.
- **`ksp_solve op K_0 (seed inp)`** is the per-member solve `ksp.Mult(RHS, V[step])` (electrostatic `:69`) / `ksp.Mult(RHS, A[step])` (magnetostatic `:77`), delegated to the per-solve [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md) → [`L3/ksp_solve`](../L3/ksp_solve.md). This theme treats it as one opaque per-member solve (`ksp.Mult`); the per-solve theme dissolves its interior.

The dissolution is **three** coordinated rewrites, one per piece of L4 map-shell machinery:

### 1. Once-captured `readonly` operator stratum → operator construction hoisted outside the `for`

The L4 once-captured `op : OpParams` (the `readonly` stratum bound outside the `map`) dissolves into the L3 `KspSolver ksp(...)` + `ksp.SetOperators(*K, *K)` placed *by hand* outside the `for` loop. This is the **load-bearing collapse** — the cap's Law 2 (the `op`-dependent solver construction is invariant across the map and hoists out of it) is exactly what licenses the L3 form's operator construction sitting outside the loop. In both Palace sweeps the placement is witnessed directly: `KspSolver ksp(...)` (electrostatic `:35`, magnetostatic `:35`) and `ksp.SetOperators(*K, *K)` (electrostatic `:36`, magnetostatic `:36`) are *outside* the `for` (electrostatic `:60`, magnetostatic `:66`). The L4 type-level guarantee (the `readonly` stratum forbids per-element operator mutation) dissolves into a *coding convention* at L3: the construction sits outside the loop, but nothing at L3 type-enforces it. This is the precise statement of why the **driven** pipeline (operator rebuilt per-ω *inside* the loop, `drivensolver.cpp:176` / `:180`) is NOT an instance of `solve_family` — it lacks the hoist, so the L4 once-captured stratum has no L4 `solve_family` form to dissolve from.

### 2. `map` over the independent RHS family → explicit positional accumulating `for` over the index set

The L4 `map (\inp -> ksp_solve op inp) rhss` dissolves into the L3 explicit positional `for` loop over the family-index set, each iteration running one per-member solve and writing the result into a collection slot. The combinator dissolution — how the per-element `map` body `\inp -> ksp_solve op inp` becomes the L3 per-iteration body — **delegates** the per-member solve to [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md) (this theme composes strictly above it); what *this* theme adds is the **map → accumulating-loop translation**: the higher-order `map` collapses to a first-order positional `for` that mutates a running collection. The family-index set the `for` ranges over (`laplace_op.GetSources()` for terminal boundaries, electrostatic `:60`; `curlcurl_op.GetSurfaceCurrentOp()` for surface-current boundaries, magnetostatic `:66`) is the L4 `[Inputs]` family the `map` ran over; the absorbed family-index domain (firm cap §Variant axes axis 2) is just the loop's range. The per-index RHS construction (`laplace_op.GetExcitationVector(idx, *K, V[step], RHS)`, electrostatic `:68`; `curlcurl_op.GetExcitationVector(idx, RHS)`, magnetostatic `:76`) forms each member's `Inputs` inside the loop. This is the L4→L3 statement of "the `map` combinator's higher-order application over an independent family becomes an explicit imperative sweep".

### 3. Order-preserving trajectory collection → pre-sized `std::vector<Vector>` indexed by a running counter

The L4 order-preserving trajectory (`solutions[i] ↔ rhss[i]`, the `map` result `[SimState]`) dissolves into the L3 pre-sized `std::vector<Vector>` collection indexed by the running `step` counter. Palace pre-sizes the collection (`std::vector<Vector> V(n_step)`, electrostatic `:46`; `std::vector<Vector> A(n_step)`, magnetostatic `:47`) and writes member `step` into slot `V[step]` / `A[step]` via the per-member solve's output argument (`ksp.Mult(RHS, V[step])`, electrostatic `:69`; `ksp.Mult(RHS, A[step])`, magnetostatic `:77`), incrementing `step++` (electrostatic `:89`, magnetostatic `:99`) each iteration. The L4 `map`-result-IS-the-family (the firm cap §Variant axes axis 4, collection-shape transparent) dissolves into the explicit pre-sizing-and-positional-indexing. The order-preservation the cap's Law 3 names survives: the `step++` running index writes member `i` into slot `i`, so the collection is position-aligned with the family-index set's iteration order — even though (per Law 3) the underlying solves commute.

### What does NOT change in the rotation

The **per-member solve dataflow** survives the rotation unchanged — each member's `ksp_solve op inp` (the `ksp.Mult(RHS, V[step])` call) passes through unchanged in dataflow position; the rotation touches only the **map shell**: the `readonly` once-captured stratum becomes the hand-hoisted operator construction, the higher-order `map` becomes the explicit positional `for`, the trajectory collection becomes the pre-sized indexed `std::vector<Vector>`. The per-member solve interior passes through unchanged via the [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md) sibling theme.

The **family-member independence** survives at L3 (the cap's Law 3 / law 1): each `ksp.Mult` writes its own collection slot, reading only the shared once-built `ksp` and its own per-index RHS; there is no cross-member state in the L3 loop. The embarrassing-parallelism the cap's concatenation-homomorphism (Law 1) licenses is *preserved* by the L3 form (the loop iterations are independent given the shared `ksp`) but not *exploited* — Palace writes a sequential `for`. The L3 form's sequential `for` is a coding realization, not an obstruction: unlike the inner [`L3/ksp_solve`](../L3/ksp_solve.md) outer-driver fold (which carries a genuine outer-loop `sequential-obstruction` because each step reads scalars from the previous), the *family* loop has **no cross-member dependence** — it is an embarrassingly-parallel sweep written sequentially, not a `sequential-obstruction`. (This is the key structural contrast with the per-solve driver theme: that theme's RHS carries an obstruction; this theme's RHS does not.)

### What this lowering does NOT cover

- **The per-member solve dissolution** — delegated to [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md) (firm c048). This theme dissolves the *map shell* (operator-hoist, the `for`-loop, the collection); the per-member `ksp_solve op inp` → L3 value-threaded outer-driver fold is that theme's job. This theme composes strictly above it, treating each member solve as one opaque `ksp.Mult`.
- **The inner-fold and per-step body dissolutions** — delegated transitively through the per-member solve to [`iterate-while-dissolution`](./iterate-while-dissolution.md) (firm c047) and [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md) (firm).
- **The per-element-operator superset (`map_solve_over_(operator,rhs)_family`).** When the operator is rebuilt per family-element (the operator-capture hoist is absent — `SetOperators` *inside* the loop, driven `drivensolver.cpp:176`/`:180`), the L4 form is the superset, not `solve_family`, and its dissolution is a separate batch-17 theme (the operator construction does NOT hoist out of the loop). This theme covers the **fixed-operator** family only; the per-element-operator case is the explicit scope boundary (§Applicability conditions).
- **The L3>L2 hop**, which (for the family shell) consolidates into the L2 outer-driver framing — a separate L3>L2 theme, batch-17-pending, gated on the L3 `solve_family` entry (itself batch-17). Not duplicated here.

## Applicability conditions

The rewrite is valid when all four of the following hold (the first three are the family-shell conditions; the fourth is the operator-capture condition that is the scope boundary):

1. **The operator is captured once, shared across the family.** `op : OpParams` is bound once, outside the `map`, and threaded unchanged into every per-member [`ksp_solve`](../L4/ksp_solve.md) — the `readonly` once-captured stratum (the firm cap §Signature). This is what lets the L3 operator construction (`KspSolver ksp(...); ksp.SetOperators(*K,*K)`) hoist outside the `for` loop. **When this fails (operator per element), the form is the superset, not `solve_family`, and this rewrite does not apply** (driven, `drivensolver.cpp:176-180`).

2. **The family members are independent — no cross-member state.** Each `map` element's `SimState` is independent; the `map` carries no state between elements (the firm cap §Signature: "no cross-element threading"). This is what lets the L3 `for`-loop write each member into its own collection slot with no cross-iteration carry, and is the source of the family loop carrying **no `sequential-obstruction`** (the §"What does NOT change" verdict).

3. **The collection is order-preserving.** `solutions[i] ↔ rhss[i]` (the firm cap §"Algebraic laws" law 3); the L3 form realizes this with the `step++` running index writing member `i` into slot `i`. The pre-sizing (`std::vector<Vector>(n_step)`) requires the family size `n_step` to be known before the loop (witnessed: `int n_step = ... .size()` precedes the loop, electrostatic `:42`-context, magnetostatic likewise).

4. **The family is non-empty (Palace source-level), or the degenerate empty-family identity is honored (calculus-level).** Palace excludes the empty family via `MFEM_VERIFY(n_step > 0, ...)` (electrostatic `electrostaticsolver.cpp:42`, magnetostatic `:42`); the L4 empty-family degenerate `solve_family op [] = []` (the firm cap §"Algebraic laws" law 4) dissolves to the L3 loop running zero iterations over an empty pre-sized collection (a calculus-level total-definition convenience, not a witnessed Palace path).

## Justification kind

**`structural`** with secondary **`reduction-chain`**.

- **Structural** (dominant): the L4 map-shell machinery (the once-captured `readonly` operator stratum, the `map` over the independent family, the order-preserving trajectory collection) dissolves into the L3 explicit positional accumulating loop; the map shell is preserved by construction (every L4 shell piece becomes an L3 shell piece at the same dataflow position — capture-once → hoisted construction, `map` → `for`, trajectory → pre-sized indexed collection). The dissolution is read **directly off positive Palace source** — the operator-hoist placement (construction outside the `for`), the accumulating loop, and the pre-sized collection are all witnessed exactly by two structurally-identical fixed-operator sweeps (electrostatic `electrostaticsolver.cpp:30-90` + magnetostatic `magnetostaticsolver.cpp:30-100`).
- **Reduction-chain** (secondary): the higher-order `map (\inp -> ksp_solve op inp) rhss` desugars to the explicit positional `for` with the accumulator threaded (the standard `map`-to-fold-to-imperative-loop reduction); the pure-map degenerate of the strawman §3.7 `iterate_while` family (the cap's alternate rendering) desugars to the same accumulating loop with the carry `{ remaining, solutions }` becoming the loop index + the mutable collection (`book/src/design/l4_calculus.md` §3.7).

**Abstraction-direction note**: L4 is the higher-abstraction layer (the `map` combinator, the typed `readonly` once-captured operator stratum, the order-preserving trajectory). L3 is the lower-abstraction layer (the explicit positional `for`, the hand-hoisted operator construction, the pre-sized mutable `std::vector<Vector>` indexed by a running counter). The rotation direction is **L4 → L3**, narrated forward per the high→low discipline.

## Speculative L4 operators

None. This theme lowers an already-authored L4 combinator ([`solve_family`](../L4/solve_family.md), firm-structure cycle-055 D1, status `rough-in (test-coverage-bounded)`) assembled from the already-firm [`ksp_solve`](../L4/ksp_solve.md) cap mapped via the already-firm [`iterate-while`](../L4/iterate-while.md) family. No new speculative operator is introduced.

## Verified-against

L4 source (the LHS of this rewrite):

- `book/src/L4/solve_family.md` (cycle-055 D1; **same-cycle sibling** — authored by D1, lands at integration before the single finalize build; the live link resolves once D1's create is applied) — the L4 map-over-RHS-family combinator: §Signature (the `solve_family` / `map (\inp -> ksp_solve op inp) rhss` shape + the pure-map degenerate rendering), §Semantics (the direct-map form + the operator-capture-once structural payoff), §"Algebraic laws" (Law 1 concatenation-homomorphism, Law 2 operator-capture-once / `SetOperators`-hoist, Law 3 element-independence / order-preservation — the load-bearing transported properties), §"Lowers to" (the in-line rotation-direction record this theme realizes), §Specializations (the two fixed-operator sweeps), §Variant axes (the operator-capture scope boundary, the absorbed family-index / collection-shape axes), §Status (the `rough-in (test-coverage-bounded)` caveat this theme's §Status reasons about).
- `book/src/L4/ksp_solve.md` (firm cycle-048) — the per-member cap the map runs (the per-element solve, delegated to its own theme).
- `book/src/L4/iterate-while.md` (firm cycle-007) — the §3.7 family whose pure-map degenerate the combinator IS (the alternate LHS rendering).

L3 source (the RHS of this rewrite):

- `book/src/L3/ksp_solve.md` (firm cycle-020) — the per-member solve target [`L3/ksp_solve`](../L3/ksp_solve.md) `(op, K_0, s_0) -> (s_final, result)` each loop iteration delegates to: §Signature (`:38-54`, the fold the per-member solve dissolves into), §"Iteration-rotation marker" (`:100-104`, the **per-solve** outer-loop `sequential-obstruction` — contrasted in this theme's §"What does NOT change" against the family loop, which carries NO obstruction).
- `book/src/L4-L3/ksp-solve-driver-dissolution.md` (firm cycle-048) — the per-member solve dissolution this theme composes **strictly above** (the `ksp_solve op inp` → L3 value-threaded outer-driver fold each map element dissolves through).
- `book/src/L4-L3/iterate-while-dissolution.md` (firm cycle-047) + `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (firm) — the inner-fold and per-step body dissolutions, transitive through the per-member solve.

L0 evidence (the fixed-operator family-sweep witnesses; self-verified exact against on-disk source this dispatch):

- **Electrostatic terminal-boundary sweep** (`palace/drivers/electrostaticsolver.cpp`):
  - `:30` — `auto K = laplace_op.GetStiffnessMatrix()` (operator `K` assembled once).
  - `:35` — `KspSolver ksp(iodata, laplace_op.GetH1Spaces())` (solver built once, outside the loop).
  - `:36` — `ksp.SetOperators(*K, *K)` (operator captured once, **outside** the loop — the load-bearing hoist).
  - `:46` — `std::vector<Vector> V(n_step)` (pre-sized collection).
  - `:60` — `for (const auto &[idx, data] : laplace_op.GetSources())` (accumulating loop over the terminal-boundary index family).
  - `:68` — `laplace_op.GetExcitationVector(idx, *K, V[step], RHS)` (per-index RHS construction, inside the loop).
  - `:69` — `ksp.Mult(RHS, V[step])` (per-member solve writing into the collection slot — the delegated `ksp_solve op inp`).
  - `:89` — `step++` (running collection index).
  - `:42` — `MFEM_VERIFY(n_step > 0, ...)` (non-empty-family gate).
- **Magnetostatic surface-current sweep** (`palace/drivers/magnetostaticsolver.cpp`):
  - `:30` — `auto K = curlcurl_op.GetStiffnessMatrix()` (operator `K` assembled once).
  - `:35` — `KspSolver ksp(iodata, curlcurl_op.GetNDSpaces(), &curlcurl_op.GetH1Spaces())` (solver built once, outside the loop).
  - `:36` — `ksp.SetOperators(*K, *K)` (operator captured once, **outside** the loop).
  - `:47` — `std::vector<Vector> A(n_step)` (pre-sized collection).
  - `:66` — `for (const auto &[idx, data] : curlcurl_op.GetSurfaceCurrentOp())` (accumulating loop over the surface-current-boundary index family).
  - `:76` — `curlcurl_op.GetExcitationVector(idx, RHS)` (per-index RHS construction).
  - `:77` — `ksp.Mult(RHS, A[step])` (per-member solve writing into the collection slot).
  - `:99` — `step++` (running collection index).
  - `:42` — `MFEM_VERIFY(n_step > 0, ...)` (non-empty-family gate).
- **Per-element-operator scope-boundary witness (negative for fixed-operator)** (`palace/drivers/drivensolver.cpp`):
  - `:176` — `auto A = space_op.GetSystemMatrix(1.0 + 0.0i, 1i * omega, -omega * omega + 0.0i, ...)` (operator rebuilt per-ω, **inside** the frequency loop — the hoist is absent).
  - `:180` — `ksp.SetOperators(*A, *P)` (operator captured **inside** the loop). The frequency-dependent operator cannot be fixed; this is the `per-element` superset, used as the scope boundary, not as supporting evidence for the fixed-operator family-map dissolution.

Concept-page references:

- [`state-stratification`](../concepts/state-stratification.md) — the `op` shared `readonly` operator stratum captured once across the family; the capture-once typing that dissolves to the hand-hoisted operator construction.
- [`variant-absorption`](../concepts/variant-absorption.md) — the operator-capture axis (`fixed | per-element`, the scope boundary) and the family-index / collection-shape absorption.
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the **per-solve** outer-loop obstruction the inner [`L3/ksp_solve`](../L3/ksp_solve.md) carries (NOT the family loop — the family loop carries no obstruction; the contrast is the theme's §"What does NOT change" verdict).

## Status

`firm` — on the **structural rotation**. The map-shell dissolution (the once-captured `readonly` operator stratum → the operator construction hoisted outside the `for`; the `map` over the independent family → the explicit positional accumulating loop; the order-preserving trajectory → the pre-sized `std::vector<Vector>` indexed by a running counter) is read **directly off positive Palace source** — every piece of the rotation shape is witnessed exactly by two structurally-identical fixed-operator sweeps (electrostatic `electrostaticsolver.cpp:30-90` + magnetostatic `magnetostaticsolver.cpp:30-100`), and the operator-hoist placement (construction outside the loop) is a positive source fact, not a reconstruction. The three coordinated rewrites are exhaustively cited against the firm cap's §Signature / §"Algebraic laws" / §Specializations and the L0 family-sweep witnesses. Justification is `structural` + secondary `reduction-chain`. No speculative operator introduced. This theme **composes strictly above** the firm per-member solve dissolution [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md) (the per-member `ksp_solve op inp` each map element dissolves through).

**On the inherited LHS test-coverage caveat (reasoning, load-bearing).** The LHS [`solve_family`](../L4/solve_family.md) is status `rough-in (test-coverage-bounded)`: its *algebraic laws* (the concatenation-homomorphism and the underlying family-member independence) are stated against the strawman §3.7 family / the `map` list-homomorphism algebra but are **test-unconfirmed** (the drivers are integration-level; no unit test exercises the family-map's independence at the `Solve(mesh)` entry). This theme is **`firm` rather than inheriting that caveat** because the *rotation shape* — what this theme asserts — does **not depend on the independence law**. The theme asserts that the L4 map shell *dissolves into* the L3 accumulating-loop shape with the operator hoisted; that assertion is a **structural identity on the map-shell syntax**, read directly off positive source (the `SetOperators`-outside-the-`for` placement, the pre-sized `std::vector<Vector>`, the `step++` accumulator are all *present in the Palace source*, not reconstructed). The independence law is what licenses *reordering / parallelizing* the family (the cap's Law 1 consequence) — a property of the *family-map semantics*, not of the *dissolution shape*. Concretely: even if a future test were to reveal hidden cross-member state in the `KspSolver` reuse (which would demote the cap's independence law), the *dissolution itself* would still hold — the L4 map shell would still dissolve into the same L3 accumulating loop (the loop would simply not be safely reorderable, exactly as the L3 sequential `for` already is not exploited for parallelism). So the test-coverage gate sits on the **upstream cap's laws**, not on **this rotation's shape**; the rotation is firm. **Promotion-of-the-cap note**: should a batch-17 lowering-verifier pass confirm the `KspSolver`-reuse carries no cross-element state (promoting the LHS cap to `firm`), this theme is unaffected — it is already firm on structure; the cap promotion would only strengthen the family-map *semantics* this theme's RHS faithfully renders. (OQ `solve-family-map-dissolution-firm-on-structure-vs-lhs-test-coverage` records this scoping for the batch-17 verifier.)

**Scope (load-bearing)**: this theme covers the **fixed-operator** family-map dissolution, witnessed by **electrostatic + magnetostatic ONLY** (2-of-5 pipelines). The **driven** pipeline (operator rebuilt per-ω *inside* the loop, `drivensolver.cpp:176`/`:180`) lacks the operator-capture hoist and is the `per-element` superset `map_solve_over_(operator,rhs)_family` — its dissolution (where the operator construction does NOT hoist out of the loop) is a separate batch-17 theme, NOT covered here. Transient and eigenmode are unprobed. Do NOT claim cross-pipeline generality beyond the two fixed-operator witnesses.

This dispatch (cycle-055 D2) is the **outer map-shell dissolution** for the `solve_family` propagation lead, the L4>L3 half (the firm cap D1 authored this cycle is the LHS). It realizes the in-line rotation direction the firm cap's §"Lowers to" records and is the dedicated home for the map-shell stratum, composing above the per-member [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md).

## L4 vs L3 distinction

- **L4**: the `map`-combinator family shell. `solve_family op rhss = map (\inp -> ksp_solve op inp) rhss`; the operator `op : OpParams` is a `readonly` stratum captured **once, outside the map** (the capture-once is *structural*, type-enforced); the family map is a list homomorphism (the concatenation-homomorphism law); per-member independence is typed (no cross-element threading); the trajectory IS the order-preserving collected family.
- **L3**: the value-threaded explicit family-sweep. The `map` has dissolved to an explicit positional `for` over the family-index set; the operator construction (`KspSolver ksp(...); ksp.SetOperators(*K,*K)`) is hoisted outside the loop **by hand** (a coding convention, not a type-level stratification); the family collection is a pre-sized `std::vector<Vector>` indexed by a running `step` counter; per-member independence survives as a structural property of the loop (each iteration writes its own slot) but carries no L3 type enforcement.

The two layers share the per-member solve dataflow (each `ksp.Mult` ≡ one `ksp_solve op inp`) and the operator-capture-once placement (outside the loop / outside the map); they differ in **the combinator vocabulary (`map` vs explicit `for`), the operator-capture enforcement (`readonly` stratum vs hand-placed construction), and the collection representation (order-preserving trajectory vs pre-sized indexed `std::vector<Vector>`)**. The rotation erases the `map` combinator into the explicit accumulating loop, demotes the type-level capture-once to a hand-hoisted coding convention, and materialises the trajectory into the pre-sized positional collection — narrated forward L4→L3. The family loop carries **no `sequential-obstruction`** (unlike the per-solve outer-driver fold it wraps): the family members are independent, so the sweep is embarrassingly parallel, written sequentially.
```

```edit:book/src/L4-L3/index.md
[APPEND a new row to the "Theme list" table, after the `ksp-solve-driver-dissolution` row (currently the last row, line 20). This is D2's OWN row (anchor-distinct, parallel-safe):]

| [`solve-family-map-dissolution`](./solve-family-map-dissolution.md) | L4 [`solve_family`](../L4/solve_family.md) **outer map shell** — the fixed-operator map-over-RHS-family combinator `solve_family op rhss = map (\inp -> ksp_solve op inp) rhss`: the once-captured `readonly` `op` stratum (the L4 typing of `SetOperators(*K,*K)` hoisted outside the loop), the `map` over the independent RHS family, the order-preserving trajectory collection. The **outer-shell** companion to the per-solve `ksp-solve-driver-dissolution`; composes strictly above it. | L3 explicit **positional accumulating outer loop**: the once-captured `readonly` `op` stratum dissolves to the `KspSolver ksp(...)` / `SetOperators(*K,*K)` construction hoisted by hand outside the `for`; the `map` dissolves to a positional `for` over the family-index set (`GetSources` / `GetSurfaceCurrentOp`); the trajectory collection dissolves to a pre-sized `std::vector<Vector>` indexed by a running `step` counter; each iteration delegates one `ksp_solve op inp` per-member solve into its slot. Substantive (a `map`-combinator → explicit-accumulating-loop translation with operator-hoist, not identity-in-named-terms). The family loop carries NO `sequential-obstruction` (members independent). | `structural` + secondary `reduction-chain` | `firm` (cycle-055 D2 abstractor; the outer map-shell rotation for the `L4/solve_family` combinator D1 firmed this cycle; composes strictly above the per-solve `ksp-solve-driver-dissolution` (firm c048); firm on structure — the rotation shape is read directly off positive source, independent of the LHS's test-gated independence law (reasoning in the chapter §Status); fixed-operator scope ONLY 2-of-5, driven `per-element` superset batch-17-gated; realizes the cap's in-line §"Lowers to" direction) |
```

```edit:book/src/L4-L3/index.md
[APPEND a new §Vocabulary-cohort section after the "Working Notes" section (after line 34) IF none exists, registering D2's OWN cohort bullet. This is D2's own substantive-vs-identity sub-grouping entry. (DEFER the consolidated running-count TALLY — the cohort-summing firm count + coverage-gap line + growth-log — to D7, the count-owner this cycle.) If D7 establishes the §Vocabulary-cohort section structure, this bullet merges under the appropriate "Substantive themes (firm)" sub-list; otherwise it stands as the section seed:]

## Vocabulary-cohort

Themes in this lowering layer, grouped by whether the rotation is a **substantive vocabulary translation** or a thin identity-in-named-terms note (per the vocabulary-shift redirect). The consolidated firm-count tally + coverage-gap line are maintained by the count-owner (deferred to D7 this cycle).

**Substantive themes (firm):**

- [`solve-family-map-dissolution`](./solve-family-map-dissolution.md) — the L4 `solve_family` **outer map shell** → L3 explicit positional accumulating loop. A genuine `map`-combinator → explicit-accumulating-`for` translation with the **operator-capture hoist** (the L4 once-captured `readonly` `op` stratum → the `SetOperators(*K,*K)` construction hand-hoisted outside the loop) the load-bearing dissolution detail. Composes strictly above the per-solve [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md). The family loop carries NO `sequential-obstruction` (members independent — the contrast with the per-solve outer-driver fold it wraps). Firm on structure; fixed-operator scope (2-of-5, driven `per-element` superset batch-17-gated). Cycle-055 D2.
```

```edit:book/src/SUMMARY.md
[INSERT a new L4>L3 chapter entry after the `ksp-solve-driver-dissolution` line (line 22), under the "L4 > L3 — Lowering" Part:]

- [solve-family-map-dissolution](./L4-L3/solve-family-map-dissolution.md)
```

## Speculative operators proposed

None. This theme lowers the already-authored L4 `solve_family` combinator (cycle-055 D1) assembled from the firm `ksp_solve` cap and the firm `iterate-while` family. No new speculative L4 operator is introduced; the per-member solve delegates to the firm `ksp-solve-driver-dissolution`.

## Supporting evidence

- **LHS (D1's firm cap)**: `reports/2026-06-02T010700Z-harvester-solve-family-firm-entry/CYCLE.md` — the authoritative LHS input (signature `solve_family :: OpParams -> [Inputs] -> [SimState]` = `map (\inp -> ksp_solve op inp) rhss`; the 4 laws incl. the load-bearing concatenation-homomorphism + operator-capture-once / `SetOperators`-hoist; the 2 fixed-operator witnesses + the driven scope-boundary; the `rough-in (test-coverage-bounded)` status this theme's §Status reasons about).
- **Per-member solve target + inner sibling theme**: `book/src/L3/ksp_solve.md` (firm c020, the per-member outer-driver fold) + `book/src/L4-L3/ksp-solve-driver-dissolution.md` (firm c048, the per-member solve dissolution this theme composes strictly above).
- **L0 family-sweep witnesses (all 14 anchors self-verified exact this dispatch via `sed -n`)**: electrostatic `electrostaticsolver.cpp:30`/`:35`/`:36`/`:46`/`:60`/`:68`/`:69`/`:89`/`:42`; magnetostatic `magnetostaticsolver.cpp:30`/`:35`/`:36`/`:47`/`:66`/`:76`/`:77`/`:99`/`:42`; driven scope-boundary `drivensolver.cpp:176`/`:180`. Zero drift.
- **Operator-hoist confirmation**: in both fixed-operator sweeps `KspSolver ksp(...)` (`:35`) + `ksp.SetOperators(*K,*K)` (`:36`) sit *outside* the `for` (`:60` / `:66`); in driven `ksp.SetOperators(*A,*P)` (`:180`) sits *inside* the frequency loop (`:168`-context) with the operator rebuilt per-ω (`:176`) — the positive/negative witness pair for the hoist.

## Open questions / caveats

- **Firm-on-structure vs inherited LHS test-coverage caveat (OQ for batch-17 verifier).** I marked the theme `firm` (not inheriting the LHS's `rough-in (test-coverage-bounded)` caveat), with the reasoning recorded in §Status: the rotation *shape* (map shell → accumulating loop + operator-hoist) is a structural identity read directly off positive source and does NOT depend on the cap's test-gated *independence law* (which governs family-map *semantics* / reorderability, not the *dissolution shape*). A batch-17 lowering-verifier should (a) confirm this scoping (the dissolution holds regardless of whether `KspSolver`-reuse carries hidden cross-member state), and (b) note that a cap promotion to `firm` strengthens the RHS semantics but does not change this theme's firmness. OQ: `solve-family-map-dissolution-firm-on-structure-vs-lhs-test-coverage` (batch-17). I flagged this explicitly rather than reflexively inheriting the caveat — if the planner/verifier prefers conservative inheritance, demote to `rough-in (test-coverage-bounded)` matching the LHS, but I believe firm-on-structure is the correct reading per the shape/semantics split.

- **No `sequential-obstruction` on the family loop (deliberate structural contrast).** Unlike the per-solve [`L3/ksp_solve`](../L3/ksp_solve.md) outer-driver fold (which carries a genuine outer-loop `sequential-obstruction` because each step reads scalars from the previous), the *family* loop has NO cross-member dependence — it is an embarrassingly-parallel sweep written sequentially. I made this contrast load-bearing in §"What does NOT change" and §"L4 vs L3 distinction" because it is the key reason this theme's RHS is *cleaner* than the per-solve theme it composes above. If a cross-layer-cross-cutter later examines the family-vs-per-solve obstruction distinction, this is the anchor.

- **Per-element-operator superset dissolution is batch-17 future work.** The driven pipeline (operator rebuilt per-ω inside the loop, `drivensolver.cpp:176`/`:180`) is the `per-element` superset `map_solve_over_(operator,rhs)_family`; its dissolution (where the operator construction does NOT hoist out of the loop — `SetOperators` stays inside) is a separate batch-17 theme, gated on the superset L4 combinator being firmed. I covered the fixed-operator case ONLY and made the scope boundary explicit (§Applicability conditions condition 4 / §Status scope). OQ inherited from D1: `solve-family-general-operator-rhs-superset-probe` (batch-17).

- **L3 `solve_family` entry + L3>L2 hop are batch-17/pending.** The firm L3 image `L3/solve_family` (the dissolution target as a layer-coherent L3 entry) and the further L3>L2 hop on the family shell are both batch-17/pending (per D1's entry). This theme narrates the L4→L3 rotation forward; it does not author the L3 entry or the L3>L2 theme. I referenced `L3/solve_family` only in prose context (not as a live link, since it does not yet exist on disk).

- **Index §Vocabulary-cohort section may not pre-exist (dual-registration partition honored).** The `book/src/L4-L3/index.md` currently has a "Theme list" table + "Working Notes" but NO §Vocabulary-cohort section. Per the dual-registration partition I wrote (1) my OWN table row (appended, anchor-distinct, parallel-safe) and (2) my OWN §Vocabulary-cohort bullet — authored as a section seed (`## Vocabulary-cohort` with a "Substantive themes (firm)" sub-list) in case D7 has not yet established the section, with an explicit note that if D7 establishes the section structure my bullet merges under it. I **DEFERRED** (3) the consolidated firm-count TALLY (cohort-summing firm count + coverage-gap line + growth-log + fork-flip prose) to **D7** (the count-owner this cycle, per my dispatch scope). If D7's structure differs, the integrator should merge my bullet under D7's "Substantive themes (firm)" sub-list. SUMMARY.md registration is mine (added).

- **Forward-reference slugs.** I forward-referenced the LHS by the canonical slug `../L4/solve_family.md` (D1's entry, stated in my dispatch scope) and the inner sibling by `./ksp-solve-driver-dissolution.md` (firm, on disk). Both resolve as live links at integration (D1's create lands before the finalize build; the inner theme is already on disk). No guessed slugs.
