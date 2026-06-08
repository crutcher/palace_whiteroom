# frequency-sweep-dissolution

The L4>L3 lowering theme for the [`frequency_sweep`](../L4/frequency_sweep.md) **operator-varying outer map-shell** — the L4 driven-pipeline map-over-frequency-family combinator `frequency_sweep fam omegas = map (\w -> ksp_solve (assemble_frequency_operator fam w) (rhs_at fam w)) omegas` that maps the [`ksp_solve`](../L4/ksp_solve.md) cap over a family of sample frequencies, **rebuilding the operator at every member** because the system matrix is a function of `ω`. The theme dissolves the L4 `map` combinator (the per-member operator-and-RHS function `\w -> ksp_solve (A ω) (b ω)`, the pure-map-over-an-independent-frequency-family shape, the order-preserving solution collection) into the L3 **explicit sequential per-ω loop** — the per-ω **rebuild-the-operator-then-re-bind-then-`ksp_solve` driver-call sequence** where the operator assembly (`GetSystemMatrix`) and the solver re-binding (`ksp.SetOperators`) sit **INSIDE** the loop, re-run for each frequency.

It is the **operator-varying companion** to the fixed-operator [`solve-family-map-dissolution`](./solve-family-map-dissolution.md): that theme dissolves a map whose operator is **captured once and hoisted outside the loop** (`SetOperators` before the `for`); this theme dissolves a map whose operator **varies per member and is rebuilt + re-bound inside the loop** (`SetOperators` per-ω, inside the `for`). The contrast — hoisted-once `SetOperators` vs per-ω `SetOperators` — is the crux of why these are distinct dissolution themes, and is exactly the load-bearing distinction D1 established at the [`frequency_sweep`](../L4/frequency_sweep.md) cap.

## Slug

`frequency-sweep-dissolution`

## Context

[`frequency_sweep`](../L4/frequency_sweep.md) is the L4 **operator-varying map-over-frequency-family combinator**, the driven pipeline's per-ω solve-half. The combinator's §"Lowers to" names the dissolution to L3 as **substantive** (not identity-in-form) and records the rotation *direction* in-line per the high→low discipline, deferring the theme itself to this chapter (canonical slug `frequency-sweep-dissolution`).

This theme sits in the L4>L3 **map-shell family** alongside its two siblings, distinguished by the **operator-capture axis**:

- [`solve-family-map-dissolution`](./solve-family-map-dissolution.md) — the **fixed-operator** map shell: a single `op` captured once, the solver built once, `SetOperators(*K,*K)` hoisted **outside** the `for` (electrostatic / magnetostatic, 2-of-5). The operator is INVARIANT across the family.
- `frequency-sweep-dissolution` (this theme) — the **operator-varying** map shell: the operator `A(ω)` is a function of the family index, rebuilt at every member, `ksp.SetOperators(*A,*P)` re-run **inside** the `for` (driven). The operator VARIES across the family.
- [`fold-solve-time-step-dissolution`](./fold-solve-time-step-dissolution.md) — the sequential-**fold** sibling (carry-threaded; the steps do NOT commute). The contrasting carry axis.

The first two are both **map shells with no cross-member carry** (the solves commute, the family loop carries no `sequential-obstruction`); they differ only on whether the operator hoists. This theme is the dedicated home for the **operator-varying corner** — a reader navigating from the firm [`frequency_sweep`](../L4/frequency_sweep.md) §"Lowers to" lands here, at the operator-varying map-shell dissolution, rather than re-deriving it inline or conflating it with the fixed-operator sibling whose operator-hoist this map LACKS.

The rotation direction is **L4 → L3**, narrated forward per the high→low discipline (CLAUDE.md §Methodology invariants "Layers are defined high→low"). Notes about the reverse lift (how the L3 explicit per-ω sweep lifts back into the `map` combinator, what evidence licenses recognizing the per-ω rebuild as `\w -> ksp_solve (A ω) (b ω)`) live in the cap's §"L4 vs L3 distinction" and in this report's working notes, not in this formal chapter.

This is a **genuine vocabulary translation, not an identity-in-named-terms rename** (CLAUDE.md §Methodology invariants vocabulary-shift redirect). The L4 vocabulary — `map`, the per-member operator-and-RHS function `\w -> ksp_solve (assemble_frequency_operator fam w) (rhs_at fam w)`, the pure-map-over-an-independent-frequency-family shape, the order-preserving solution trajectory — is a *different semantic organization* from the L3 vocabulary — an explicit sequential `for` over the frequency-sample list, the operator re-assembly and solver re-binding placed BY HAND inside the loop body, a single re-used solution vector overwritten each step. The reorganization (a single combinator naming the whole frequency sweep, with the operator-as-a-function-of-ω structural, dissolving into an imperative per-ω loop that re-assembles and re-binds the system at each frequency) is the substance of the theme.

## L4 form (LHS)

The L4 [`frequency_sweep`](../L4/frequency_sweep.md) combinator — the firm-structure D1 operator-varying map shape (the firm entry §Signature). The entry point, transcribed from the firm cap:

    -- entry point: map ksp_solve over the frequency family, REBUILDING the operator per member
    frequency_sweep :: FrequencyOperatorFamily[N] -> [Scalar] -> [SimState]
    frequency_sweep fam omegas =
      map (\w -> ksp_solve (assemble_frequency_operator fam w) (rhs_at fam w)) omegas

    -- the per-member function is operator-VARYING: A and b are both functions of w
    --   assemble_frequency_operator :: FrequencyOperatorFamily[N] -> Scalar -> OpParams
    --   rhs_at                      :: FrequencyOperatorFamily[N] -> Scalar -> Inputs
    -- there is NO once-captured shared `op` — the operator is rebuilt at every member.

    -- equivalently, the pure-map degenerate of the strawman §3.7 iterate_while family
    -- (each element independent; no carry; the "trajectory" IS the collected family):
    frequency_sweep fam omegas =
      (iterate_while
         (initial_sweep_state omegas)               -- carry = { remaining: [Scalar], solutions: [SimState] }
         (\st -> not (null st.remaining))            -- continue while frequencies remain
         (\st -> let w   = head st.remaining
                     op  = assemble_frequency_operator fam w   -- the operator is REBUILT here, per w
                     b   = rhs_at fam w                         -- the RHS is rebuilt here, per w
                     sol = ksp_solve op b
                 in { state: { remaining: tail st.remaining
                             , solutions: st.solutions }
                    , extras: sol }))                -- per-element extra = the solution
        .trajectory                                  -- == [ ksp_solve (A w) (b w) | w <- omegas ]

The map-shell machinery this theme dissolves is **three** pieces, with the first piece carrying the load-bearing operator-varying distinction:

1. **The per-member operator-and-RHS function `\w -> ksp_solve (assemble_frequency_operator fam w) (rhs_at fam w)`.** Unlike the fixed-operator sibling, the operator is **not** a once-captured `readonly` stratum hoisted outside the `map`; it is the result of applying `assemble_frequency_operator fam` to the member frequency `w`. Each member rebuilds `A(ω)` from the operator family `fam` (the load-bearing operator-VARYING structure). The only `readonly` once-captured stratum is the **operator family `fam`** itself (the assembled component matrices `K`, `C`, `M`); the *system matrix* `A(ω) = K + iωC − ω²M + A₂(ω)` is a per-member function of `w`, NOT invariant across the map.

2. **The `map` over the independent frequency family.** `map (\w -> ...) omegas` applies the per-element function independently to each sample frequency in `[Scalar]`. The map carries no state between elements — each member's `SimState` is independent (the firm cap §Signature: "no cross-element threading"; the solves at distinct frequencies commute).

3. **The order-preserving solution trajectory.** The `map` result `[SimState]` aligns positionally with `omegas` (`solutions[i] ↔ omegas[i]`), order-preserving even though the underlying solves commute.

The load-bearing L4 properties this lowering must transport are the cap's family-map identities (the firm cap §"Algebraic laws"): **concatenation-homomorphism** — `frequency_sweep fam (a ++ b) = frequency_sweep fam a ++ frequency_sweep fam b`, the family map is a list homomorphism; **operator-per-member (NO hoist)** — the operator-dependent assembly + solver re-binding is INVARIANT only with respect to the family `fam`, but VARIES with the member `w`, so it does NOT hoist out of the map (the explicit negation of the fixed-operator sibling's hoist law); **element-independence / order-preservation** — the solves commute, the collection preserves position.

## L3 form (RHS)

The L4>L3 dissolution produces the L3 **explicit sequential per-ω loop with per-member operator re-assembly + solver re-binding** — the Palace C++ driven-sweep shape (`palace/drivers/drivensolver.cpp`). The L3 rendering (using the L3 value-thread vocabulary, with the per-member solve delegated to the [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md) chain):

    -- L3 explicit frequency-sweep: operator REBUILT + RE-BOUND inside the loop, per ω
    frequency_sweep_L3 :: (fam, omegas) -> solutions
    frequency_sweep_L3 fam omegas =
      let K, C, M  = assemble_family_matrices fam    -- 1. assemble the operator FAMILY once (the readonly stratum)
      let ksp      = build_ksp fam                    --    build the solver OBJECT once, outside the loop
      let n_step   = length omegas
      let solutions = []
      let solutions =                                 -- 2. sequential for-loop over the frequency-sample list
            for_index (0 .. n_step - 1) solutions (\omega_i solutions ->
              let w          = omegas[omega_i]                    --    omega_sample[omega_i]
              let A          = assemble_system_matrix K C M w     -- 3a. REBUILD A(ω) INSIDE the loop (per-ω)
              let P          = assemble_precond K C M w           --     rebuild the preconditioner INSIDE the loop
              let _          = set_operators ksp A P              -- 3b. RE-BIND the solver INSIDE the loop (per-ω)
              let rhs        = form_excitation fam w              --     per-ω RHS construction (inside the loop)
              let (s_final, _result) = ksp_solve A K_0 (seed rhs) --     per-member L3 driver (delegated)
              let solutions  = solutions ++ [s_final.x]           --     collect the member solution
              in solutions)
      in solutions

where:

- **`assemble_family_matrices fam` + `build_ksp fam`** are the L3 image of the *family-level* once-captured stratum — the component matrices `auto K = space_op.GetStiffnessMatrix<...>(...)` / `C = GetDampingMatrix` / `M = GetMassMatrix` (`drivensolver.cpp:91-93`) and `ComplexKspSolver ksp(iodata, space_op.GetNDSpaces(), &space_op.GetH1Spaces())` (`:98`), placed **outside** the `for` loop. NOTE the load-bearing asymmetry with the fixed-operator sibling: the *solver object* is built once (`:98`), but the *operator binding* (`SetOperators`) is NOT hoisted — it lives inside the loop (`:180`). Palace's own comment makes this explicit: "The operators are constructed for each frequency step and used to initialize the ksp" (`:97`).
- **`for_index (0 .. n_step - 1)`** is the explicit `for (std::size_t omega_i = ...; omega_i < omega_sample.size(); omega_i++)` (`:168-170`) sequential loop over the frequency-sample list `omega_sample` (`:80`, `= iodata.solver.driven.sample_f`), with `w = omega_sample[omega_i]` (`:172`) the per-member frequency.
- **`assemble_system_matrix K C M w` + `assemble_precond K C M w`** are the **per-ω operator rebuild INSIDE the loop** — `auto A = space_op.GetSystemMatrix(1.0 + 0.0i, 1i * omega, -omega * omega + 0.0i, K.get(), C.get(), M.get(), A2.get())` (`:176`) and `auto P = space_op.GetPreconditionerMatrix<...>(...)` (`:177-178`), with the frequency-dependent extra term `auto A2 = space_op.GetExtraSystemMatrix<...>(omega, ...)` (`:174`). This is the load-bearing dissolution detail — the operator is re-assembled at every frequency.
- **`set_operators ksp A P`** is `ksp.SetOperators(*A, *P)` (`:180`), the solver **re-binding INSIDE the loop** — the per-ω re-initialization the fixed-operator sibling does NOT have.
- **`form_excitation fam w`** is `space_op.GetExcitationVector(excitation_idx, omega, RHS)` (`:194`), the per-ω RHS construction (the incident field at the port boundaries, frequency-dependent), forming each member's `Inputs` inside the loop.
- **`ksp_solve A K_0 (seed rhs)`** is the per-member solve `ksp.Mult(RHS, E)` (`:196`), delegated to the per-solve [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md) → [`L3/ksp_solve`](../L3/ksp_solve.md). This theme treats it as one opaque per-member solve; the per-solve theme dissolves its interior. (The single re-used vector `E`, `:102`, is overwritten each member; the collection in Palace is by post-processing each `E` per-ω, not a pre-sized `std::vector` — see §"What does NOT change".)

The dissolution is **three** coordinated rewrites, one per piece of L4 map-shell machinery:

### 1. Per-member operator-and-RHS function → operator re-assembly + solver re-binding placed INSIDE the `for`

The L4 per-member function `\w -> ksp_solve (assemble_frequency_operator fam w) (rhs_at fam w)` dissolves into the L3 per-ω body that **rebuilds the system matrix** (`GetSystemMatrix`, `:176`) and **re-binds the solver** (`ksp.SetOperators(*A, *P)`, `:180`) at every iteration. This is the **load-bearing collapse, and the precise negation of the fixed-operator sibling's hoist**: the cap's operator-per-member law (the operator-dependent assembly VARIES with the member `w`) is exactly what forbids the L3 form from hoisting the operator construction out of the loop. Palace witnesses this directly: the system-matrix assembly (`:174`-`:178`) and the `SetOperators` call (`:180`) are *inside* the `for` (`:168`-`:170`), and Palace's comment states the design (`:97`, "The operators are constructed for each frequency step and used to initialize the ksp"). The only thing hoisted is the **operator family** (`K`/`C`/`M`, `:91-93`) and the solver *object* (`:98`) — the per-ω *system matrix* and its *binding* are not. This is the precise structural statement of why the **driven** pipeline is NOT an instance of the fixed-operator [`solve_family`](../L4/solve_family.md) (the sibling's §"What this lowering does NOT cover" forward-references exactly this `per-element` superset, `drivensolver.cpp:176`/`:180`): it lacks the operator-capture hoist, so its L4 form is `frequency_sweep`, not `solve_family`.

### 2. `map` over the independent frequency family → explicit sequential `for` over the sample list

The L4 `map (\w -> ...) omegas` dissolves into the L3 explicit sequential `for` loop over the frequency-sample list (`:168`-`:170`), each iteration reading one member frequency `w = omega_sample[omega_i]` (`:172`), running one per-member solve, and post-processing the result. The combinator dissolution — how the per-element `map` body becomes the L3 per-iteration body — **delegates** the per-member solve to [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md) (this theme composes strictly above it); what *this* theme adds is the **map → sequential-loop translation** with the operator-rebuild inside the body: the higher-order `map` collapses to a first-order sequential `for` that re-assembles and re-binds the system each member. The family the `for` ranges over (`omega_sample`, the precomputed frequency samples, `:80`) is the L4 `[Scalar]` family the `map` ran over. This is the L4→L3 statement of "the `map` combinator's higher-order application over an independent family becomes an explicit imperative sweep" — with the operator-varying body distinguishing it from the fixed-operator sibling.

### 3. Order-preserving solution trajectory → per-ω post-processing in sample order

The L4 order-preserving trajectory (`solutions[i] ↔ omegas[i]`, the `map` result `[SimState]`) dissolves into the L3 per-ω post-processing applied in `omega_sample` iteration order. Unlike the fixed-operator sibling (which materialises a pre-sized `std::vector<Vector>` indexed by a running counter), Palace re-uses a single solution vector `E` (`:102`) overwritten each member and **post-processes each member's `E` immediately within the loop body** (after `:196`); the "collection" is the ordered side-effect stream of per-ω post-processing (S-parameters, field exports), emitted in `omega_sample` order. The L4 `map`-result-IS-the-family dissolves into this **streamed-in-order** realization: the running `omega_i` index drives post-processing of member `i` at position `i`, so the emitted product stream is position-aligned with the frequency-sample order — even though (per the element-independence law) the underlying solves commute. (This collection-shape difference from the fixed-operator sibling — streamed post-processing of a re-used vector vs pre-sized indexed `std::vector` — is a secondary realization detail; both are order-preserving materializations of the same L4 trajectory.)

### What does NOT change in the rotation

The **per-member solve dataflow** survives the rotation unchanged — each member's `ksp_solve (A ω) (b ω)` (the `ksp.Mult(RHS, E)` call, `:196`) passes through unchanged in dataflow position; the rotation touches only the **map shell**: the per-member operator-and-RHS function becomes the in-loop operator re-assembly + solver re-binding, the higher-order `map` becomes the explicit sequential `for`, the trajectory collection becomes the in-order per-ω post-processing stream. The per-member solve interior passes through unchanged via the [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md) sibling theme.

The **family-member independence** survives at L3: each member reads only the shared operator family `fam` (`K`/`C`/`M`) and its own per-ω operator `A(ω)`, RHS `b(ω)`, and solution `E`; there is no cross-member state in the L3 loop (the re-used `E` is overwritten, not carried — its prior contents are not read by the next member). The embarrassing-parallelism the concatenation-homomorphism licenses is *preserved* by the L3 form (the loop iterations are independent given the shared family `fam`) but not *exploited* — Palace writes a sequential `for`, and re-uses one solver object across members (a sequential coding realization, not a data dependence). The L3 form's sequential `for` is a coding realization, NOT an obstruction: like the fixed-operator sibling's family loop (and unlike the per-solve [`L3/ksp_solve`](../L3/ksp_solve.md) outer-driver fold, which carries a genuine outer-loop `sequential-obstruction`), the **frequency loop has no cross-member dependence** — it is an embarrassingly-parallel sweep written sequentially, not a `sequential-obstruction`. (This is the structural alignment with the fixed-operator sibling and the contrast with the per-solve driver theme: that theme's RHS carries an obstruction; this theme's RHS does not.)

### What this lowering does NOT cover

- **The per-member solve dissolution** — delegated to [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md). This theme dissolves the *map shell* (the in-loop operator rebuild + re-binding, the `for`-loop, the in-order collection); the per-member `ksp_solve (A ω) (b ω)` → L3 value-threaded outer-driver fold is that theme's job. This theme composes strictly above it, treating each member solve as one opaque `ksp.Mult`.
- **The inner-fold and per-step body dissolutions** — delegated transitively through the per-member solve to [`iterate-while-dissolution`](./iterate-while-dissolution.md) and [`krylov-step-typed-wrapper-dissolution`](./krylov-step-typed-wrapper-dissolution.md).
- **The operator-family assembly internals** (`GetSystemMatrix` / `GetStiffnessMatrix` / `GetExtraSystemMatrix` etc.). This theme treats `assemble_frequency_operator fam w` as one opaque per-ω operator rebuild; the FE-assembly machinery that constructs the component matrices is the concern of the [`fe-assemble-fold-dissolution`](./fe-assemble-fold-dissolution.md) chain and its L1>L0 obstruction homes, not this map-shell theme.
- **The adaptive frequency sampling (SweepAdaptive / driven-PROM).** Palace's `drivensolver.cpp` carries a SECOND, state-generated sweep (the greedy PROM basis construction, `:234`-context) where the next sample frequency is GENERATED from accumulated state. That sweep is the carry-threaded **fold** (the [`fold-solve-time-step-dissolution`](./fold-solve-time-step-dissolution.md) `schedule-source = state-generated` axis), NOT this fixed-list map. This theme covers the **fixed-frequency-list** uniform-sample sweep (`omega_sample = iodata.solver.driven.sample_f`, `:80`) only.
- **The L3>L2 hop.** Following the fixed-operator sibling's NO-ENTRY warrant: the frequency-sweep map loop carries **no `sequential-obstruction`** (independent members; the loop lifts), so it has no L3 obstruction to render as a distinct chapter and none to *erase* at an L3>L2 hop. A `frequency_sweep` L3>L2 theme would be a degenerate identity-in-named-terms restatement (the §1d smell). The L3 form of the frequency-sweep shell lives here (§"L3 form (RHS)"); the per-member solve's L3>L2 consolidation is the inner [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md) chain's concern.

## Applicability conditions

The rewrite is valid when all of the following hold (the first is the operator-varying condition that is the distinguishing axis from the fixed-operator sibling):

1. **The operator is a function of the family index — rebuilt per member, NOT captured once.** `assemble_frequency_operator fam w` produces a distinct operator `A(ω)` for each member `w`; the operator-dependent assembly + solver re-binding VARY with the member and do NOT hoist out of the `map` (the firm cap §Signature). This is what forces the L3 operator construction (`GetSystemMatrix`, `:176`) and solver re-binding (`ksp.SetOperators`, `:180`) **inside** the `for` loop. **When this fails (operator captured once, invariant across the family), the form is the fixed-operator [`solve_family`](../L4/solve_family.md), and the [`solve-family-map-dissolution`](./solve-family-map-dissolution.md) theme applies instead** (electrostatic/magnetostatic, `SetOperators` outside the loop).

2. **The family members are independent — no cross-member state.** Each `map` element's `SimState` is independent; the `map` carries no state between elements (the firm cap §Signature: "no cross-element threading"; distinct frequencies commute). This is what lets the L3 `for`-loop post-process each member with no cross-iteration carry (the re-used `E` vector is overwritten, not read), and is the source of the frequency loop carrying **no `sequential-obstruction`**.

3. **The frequency sample list is precomputed (fixed-list schedule).** `omegas : [Scalar]` is a precomputed list known before the loop (`omega_sample = iodata.solver.driven.sample_f`, `:80`); the L3 `for` ranges over `0 .. omega_sample.size() - 1` (`:168`-`:170`). **When the next sample is GENERATED from accumulated state (adaptive/greedy sampling), the form is the carry-threaded fold, not this map** (the [`fold-solve-time-step-dissolution`](./fold-solve-time-step-dissolution.md) `state-generated` axis), and this rewrite does not apply.

4. **The order-preserving collection is honored.** `solutions[i] ↔ omegas[i]` (the firm cap §"Algebraic laws"); the L3 form realizes this with the `omega_i` running index driving per-ω post-processing in sample order.

## Justification kind

**`structural`** with secondary **`reduction-chain`**.

- **Structural** (dominant): the L4 map-shell machinery (the per-member operator-and-RHS function, the `map` over the independent frequency family, the order-preserving trajectory) dissolves into the L3 explicit sequential per-ω loop; the map shell is preserved by construction (every L4 shell piece becomes an L3 shell piece at the same dataflow position — per-member operator function → in-loop operator rebuild + re-binding, `map` → sequential `for`, trajectory → in-order post-processing). The dissolution is read **directly off positive Palace source** — the in-loop operator rebuild (`GetSystemMatrix`, `:176`), the in-loop solver re-binding (`ksp.SetOperators`, `:180`), the sequential frequency loop (`:168`-`:170`), and Palace's own design comment (`:97`) are all witnessed exactly by the driven pipeline (`drivensolver.cpp:80,98,166-196`).
- **Reduction-chain** (secondary): the higher-order `map (\w -> ksp_solve (A w) (b w)) omegas` desugars to the explicit sequential `for` with the per-member operator-and-RHS function applied in the loop body (the standard `map`-to-imperative-loop reduction); the pure-map degenerate of the strawman §3.7 `iterate_while` family (the cap's alternate rendering) desugars to the same sequential loop with the carry `{ remaining, solutions }` becoming the loop index + the in-order post-processing stream (`book/src/semantics/index.md` §3.7).

**Abstraction-direction note**: L4 is the higher-abstraction layer (the `map` combinator, the per-member operator-and-RHS function, the order-preserving trajectory). L3 is the lower-abstraction layer (the explicit sequential `for`, the hand-placed in-loop operator re-assembly + solver re-binding, the in-order per-ω post-processing). The rotation direction is **L4 → L3**, narrated forward per the high→low discipline.

## Speculative L4 operators

None. This theme lowers an already-authored L4 combinator ([`frequency_sweep`](../L4/frequency_sweep.md)) assembled from the already-firm [`ksp_solve`](../L4/ksp_solve.md) cap mapped via the already-firm [`iterate_while`](../L4/iterate_while.md) family, with the per-member operator-and-RHS functions `assemble_frequency_operator` / `rhs_at` constituents of the cap. No new speculative operator is introduced.

## Evidence

L4 source (the LHS of this rewrite):

- `book/src/L4/frequency_sweep.md` — the L4 operator-varying map-over-frequency-family combinator: §Signature (the `frequency_sweep` / `map (\w -> ksp_solve (A w) (b w)) omegas` shape + the operator-varying per-member function), §Semantics (the direct-map form + the operator-rebuilt-per-member structural payoff), §"Algebraic laws" (concatenation-homomorphism, operator-per-member NO-hoist, element-independence / order-preservation — the load-bearing transported properties), §"Lowers to" (the in-line rotation-direction record this theme realizes), §Variant axes (the operator-capture distinction from the fixed sibling, the fixed-list vs state-generated schedule axis).
- `book/src/L4/ksp_solve.md` — the per-member cap the map runs (the per-element solve, delegated to its own theme).
- `book/src/L4/iterate_while.md` — the §3.7 family whose pure-map degenerate the combinator IS (the alternate LHS rendering).
- `book/src/L4/solve_family.md` — the **fixed-operator** sibling whose operator-capture hoist this map LACKS; the load-bearing contrast.

L3 source (the RHS of this rewrite):

- `book/src/L3/ksp_solve.md` — the per-member solve target [`L3/ksp_solve`](../L3/ksp_solve.md) `(op, K_0, s_0) -> (s_final, result)` each loop iteration delegates to: §Signature (the fold the per-member solve dissolves into), §"Iteration-rotation marker" (the **per-solve** outer-loop `sequential-obstruction` — contrasted in this theme's §"What does NOT change" against the frequency loop, which carries NO obstruction).
- **No `book/src/L3/frequency_sweep.md`** — following the fixed-operator sibling's NO-ENTRY warrant: the frequency-map loop carries no `sequential-obstruction` (independent members; the loop lifts), so the L3 frequency-sweep-shell form is fully expressed by this theme's §"L3 form (RHS)"; a standalone L3 chapter would mirror it (the vocabulary-shift redirect anti-mirror principle). This theme is the authoritative L3-form home for the frequency-sweep shell.
- `book/src/L4-L3/ksp-solve-driver-dissolution.md` — the per-member solve dissolution this theme composes **strictly above**.
- `book/src/L4-L3/solve-family-map-dissolution.md` — the **fixed-operator** map-shell sibling; this theme is its operator-varying analog (the §Context contrast).
- `book/src/L4-L3/iterate-while-dissolution.md` + `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` — the inner-fold and per-step body dissolutions, transitive through the per-member solve.

L0 evidence (the driven frequency-sweep witness):

- **Driven frequency sweep** (`palace/drivers/drivensolver.cpp`):
  - `:80` — `const auto &omega_sample = iodata.solver.driven.sample_f` (the precomputed fixed frequency-sample list — the L4 `[Scalar]` family).
  - `:91`-`:93` — `auto K = space_op.GetStiffnessMatrix<...>(...)` / `C = GetDampingMatrix` / `M = GetMassMatrix` (the operator FAMILY component matrices assembled once, outside the loop — the family-level `readonly` stratum).
  - `:97` — comment: "The operators are constructed for each frequency step and used to initialize the ksp" (Palace's explicit statement of the operator-VARYING design — the load-bearing distinction; `:96` is the preceding "// Set up the linear solver." line, not part of the quoted text).
  - `:98` — `ComplexKspSolver ksp(iodata, space_op.GetNDSpaces(), &space_op.GetH1Spaces())` (the solver OBJECT built once, outside the loop — but NOT bound to an operator here; the binding is per-ω).
  - `:102` — `ComplexVector RHS(...), E(...), B(...)` (the re-used solution/RHS vectors, overwritten each member).
  - `:168`-`:170` — `for (std::size_t omega_i = ...; omega_i < omega_sample.size(); omega_i++)` (the sequential frequency loop).
  - `:172` — `auto omega = omega_sample[omega_i]` (the per-member frequency `w`).
  - `:174` — `auto A2 = space_op.GetExtraSystemMatrix<ComplexOperator>(omega, Operator::DIAG_ZERO)` (the frequency-dependent extra term, rebuilt per-ω).
  - `:176` — `auto A = space_op.GetSystemMatrix(1.0 + 0.0i, 1i * omega, -omega * omega + 0.0i, K.get(), C.get(), M.get(), A2.get())` (the system matrix `A(ω)` rebuilt **INSIDE** the loop — the load-bearing operator-varying rebuild).
  - `:177`-`:178` — `auto P = space_op.GetPreconditionerMatrix<ComplexOperator>(...)` (the preconditioner rebuilt per-ω).
  - `:180` — `ksp.SetOperators(*A, *P)` (the solver **re-bound INSIDE** the loop — the per-ω `SetOperators`, the explicit negation of the fixed-operator sibling's hoist).
  - `:194` — `space_op.GetExcitationVector(excitation_idx, omega, RHS)` (the per-ω RHS construction, inside the loop).
  - `:196` — `ksp.Mult(RHS, E)` (the per-member solve — the delegated `ksp_solve (A ω) (b ω)`).
- **Fixed-operator hoist contrast (negative for operator-varying)** (`palace/drivers/electrostaticsolver.cpp` / `magnetostaticsolver.cpp`): `ksp.SetOperators(*K, *K)` placed `:36` **outside** the loop (`:60`/`:66`) — the fixed-operator sibling's hoist this theme's driven form LACKS (cited via the [`solve-family-map-dissolution`](./solve-family-map-dissolution.md) sibling's L0 evidence; the contrast, not supporting evidence for this rewrite).

Concept-page references:

- [`state-stratification`](../concepts/state-stratification.md) — the operator-FAMILY `fam` (`K`/`C`/`M`) shared `readonly` stratum captured once; contrasted with the per-ω *system matrix* `A(ω)` which is NOT a captured stratum but a per-member function (the load-bearing distinction from the fixed-operator sibling).
- [`variant-absorption`](../concepts/variant-absorption.md) — the operator-capture axis (`fixed | per-element`, the distinguishing axis: this theme is the `per-element` corner) and the schedule-source axis (`fixed-list | state-generated`, this theme is `fixed-list`).
- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the **per-solve** outer-loop obstruction the inner [`L3/ksp_solve`](../L3/ksp_solve.md) carries (NOT the frequency loop — the frequency loop carries no obstruction; the contrast is the theme's §"What does NOT change" verdict).

## Status

`firm` — on the **structural rotation**. The map-shell dissolution (the per-member operator-and-RHS function → the in-loop operator re-assembly + solver re-binding; the `map` over the independent frequency family → the explicit sequential `for`; the order-preserving trajectory → the in-order per-ω post-processing) is read **directly off positive Palace source** — every piece of the rotation shape is witnessed exactly by the driven pipeline (`drivensolver.cpp:80,98,166-196`), and the in-loop operator-rebuild + re-binding (the operator-varying distinction) is a positive source fact reinforced by Palace's own design comment (`:97`). Justification is `structural` + secondary `reduction-chain`. This theme **composes strictly above** the per-member solve dissolution [`ksp-solve-driver-dissolution`](./ksp-solve-driver-dissolution.md).

**On the operator-varying distinction (load-bearing).** The defining structural fact that makes this a DISTINCT theme from the fixed-operator [`solve-family-map-dissolution`](./solve-family-map-dissolution.md) is the **per-ω `SetOperators` placement**: in the fixed-operator sweeps the operator binding hoists OUTSIDE the loop (`electrostaticsolver.cpp:36` before `:60`); in the driven sweep the operator rebuild + binding sit INSIDE the loop (`drivensolver.cpp:176`/`:180`). This is not a stylistic choice — it is forced by the operator being a function of `ω` (the frequency-dependent system matrix `A(ω) = K + iωC − ω²M + A₂(ω)` cannot be assembled once). The firm cap's operator-per-member NO-hoist law is the L4 statement of this fact; this theme renders it forward into the L3 in-loop placement.

**Scope (load-bearing)**: this theme covers the **operator-varying, fixed-frequency-list** map dissolution, witnessed by the **driven** pipeline ONLY (1-of-5 pipelines). The fixed-operator sweeps (electrostatic/magnetostatic) are the sibling [`solve-family-map-dissolution`](./solve-family-map-dissolution.md)'s scope, NOT this theme's. The driven **SweepAdaptive / PROM** state-generated sampling (`drivensolver.cpp:234`-context) is the carry-threaded fold ([`fold-solve-time-step-dissolution`](./fold-solve-time-step-dissolution.md) `state-generated` axis), NOT this fixed-list map. Eigenmode and transient are out of scope. Do NOT claim cross-pipeline generality beyond the driven fixed-list witness.

## L4 vs L3 distinction

- **L4**: the `map`-combinator frequency-sweep shell. `frequency_sweep fam omegas = map (\w -> ksp_solve (assemble_frequency_operator fam w) (rhs_at fam w)) omegas`; the operator `A(ω)` is a **per-member function of `w`** (the operator family `fam` is the `readonly` captured stratum; the system matrix is NOT captured — it varies); the family map is a list homomorphism; per-member independence is typed (no cross-element threading; distinct frequencies commute); the trajectory IS the order-preserving collected family.
- **L3**: the value-threaded explicit frequency-sweep. The `map` has dissolved to an explicit sequential `for` over the frequency-sample list; the operator re-assembly (`GetSystemMatrix`) and solver re-binding (`ksp.SetOperators`) are placed **INSIDE** the loop **by hand**, re-run per-ω (the operator-varying realization — the negation of the fixed-operator sibling's hoist); the family collection is the in-order per-ω post-processing stream over a re-used solution vector `E`; per-member independence survives as a structural property of the loop (each member overwrites its own `E`, reading no prior member's state) but carries no L3 type enforcement.

The two layers share the per-member solve dataflow (each `ksp.Mult` ≡ one `ksp_solve (A ω) (b ω)`) and the operator-VARYING placement (per-member operator function / per-ω in-loop rebuild + re-binding); they differ in **the combinator vocabulary (`map` vs explicit sequential `for`), the operator realization (per-member function of `w` vs hand-placed in-loop `GetSystemMatrix` + `SetOperators`), and the collection representation (order-preserving trajectory vs in-order per-ω post-processing stream)**. The rotation erases the `map` combinator into the explicit sequential loop, materialises the per-member operator function into the in-loop operator re-assembly + solver re-binding, and streams the trajectory as in-order per-ω post-processing — narrated forward L4→L3. The frequency loop carries **no `sequential-obstruction`** (like the fixed-operator sibling, unlike the per-solve outer-driver fold it wraps): the frequency members are independent, so the sweep is embarrassingly parallel, written sequentially.
