---
agent: layer-intro-author
invoked_at: 2026-06-04T223500Z
scope: P2 genuine-gap author — L4/preconditioning-framework.md (NEW, firm-on-first-authoring) + capability-typing.md repoint + L4 index/SUMMARY rows
status: integrated
integrated_at: 2026-06-05T001500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  Applied clean (D1, cycle-096 batch-30 position 3/3). NEW firm L4 chapter book/src/L4/preconditioning-framework.md (rank: firm; typed edges depends-on [L4/ksp_solve caps-the-binding, ksp.cpp:276-293 cites-evidence]; 8 concept reference refs) + capability-typing.md two-slice-ref repoint (:26/:55) + alpha-positioned SUMMARY row + L4/index dep-map row. L4 firm 19->20 main / 23->24 grand. rank-gate PASS (firm over firm ksp_solve). citecheck 11 ok / 0 failing. Build clean (preconditioning-framework.html built, all internal links resolve under linkcheck2). Slice cg_preconditioning_framework.md NOT deleted (deferred batch-31 P2 slice-deletion tranche). OQ l4-preconditioning-framework-promotion CLOSEABLE at meta unify.
---

# CYCLE: L4 preconditioning-framework (D1, cycle-096, batch-30 GRADED-STACK P2 first tranche)

## Summary

Authors the ONE genuine P2 gap: a NEW firm L4 entry `book/src/L4/preconditioning-framework.md`,
transcribing the `cg_preconditioning_framework` slice's unique-unlifted §L4 / §L4-v0.2 / §L4-v0.3
material (the `BaseKspSolver` composition framework — `KspParams`/`PcParams`/`OpBinding`
constructor-vs-body split, the `TrueOp`/`PcAssemblyOp` capability brands, and the `pcBoundOp`
derived-view hoist) into a firm chapter, **re-citing L0 DIRECTLY** at
`palace/linalg/ksp.cpp:276-293` (`BaseKspSolver::SetOperators`) and the surrounding constructor /
`Mult` / factory ranges (NOT via the slice). The chapter carries typed graded-stack frontmatter:
`rank: firm`, `edges: depends-on: [L4/ksp_solve]` (firm → firm-on-firm holds, rank invariant
satisfied) + the constructed-operator concept refs as `reference` (an edge to a root is `reference`;
all concept targets are non-root narrative/record pages, classified `reference`).

The records named in the chapter's signatures (`KspParams` / `PcParams` / `OpBinding` / `Ksp` / `Pc`
/ `Counters` / `BaseKspSolver`) are defined IN THEMSELVES in an in-chapter `## Record definition`
section per the record-definition obligation — **single-consumer** (only this chapter names them in
signatures), so an in-chapter section, NOT a concept page.

Re-points ONLY `concepts/capability-typing.md` lines 26 + 55 (the two `[cg_preconditioning_framework]
L4 v0.2 ... canonical first use site` refs) at the new firm chapter. Does NOT touch
`derived-view-hoisting.md` (disk-confirmed: it does NOT cite the slice — its examples are
CG/Chebyshev). Does NOT delete the slice, does NOT touch `spec/index.md` or the SUMMARY slice rows
(deferred to batch-31). D1 is SOLE owner of the L4-index/SUMMARY edits this cycle: adds the chapter's
SUMMARY row (alpha position in the "Outer-driver caps & coordination combinators" kind-group, between
`ksp_solve` and `solve_family`) + the `L4/index.md` dep-map row (same group, same alpha slot).

## Proposed changes

### 1. NEW FILE — `book/src/L4/preconditioning-framework.md`

```edit:book/src/L4/preconditioning-framework.md
[new file]:
---
layer: L4
operator: preconditioning-framework
firmness: firm
rank: firm
edges:
  depends-on:
    - target: L4/ksp_solve
      kind: caps-the-binding
    - target: reference/palace/palace/linalg/ksp.cpp:276-293
      kind: cites-evidence
  reference:
    - concepts/state-stratification
    - concepts/solve-monad
    - concepts/capability-typing
    - concepts/derived-view-hoisting
    - concepts/constructed-operator-factory
    - concepts/finest-level-unwrap
    - concepts/complex-from-real-lift
    - concepts/variant-absorption
    - concepts/solver-as-operator
consumes:
  - book/src/L4/ksp_solve.md (the outer-driver cap whose `(op, pc_op)` binding this framework holds and strata-types)
  - book/src/concepts/state-stratification.md (the three-stratum construction-vs-run-time split this framework enforces at type level)
  - book/src/concepts/capability-typing.md (the TrueOp / PcAssemblyOp brand discipline; this chapter is its canonical L4 use site)
  - book/src/concepts/derived-view-hoisting.md (the pcBoundOp stored-vs-bound derived view)
variant_axes:
  - krylov-method (CG / GMRES / FGMRES — absorbed into KspParams at construction; the body phase has no branch on it)
  - pc-type (AMS / BOOMER_AMG / SUPERLU / STRUMPACK / STRUMPACK_MP / MUMPS / JACOBI — absorbed into PcParams at construction)
  - multigrid (single-level pc / GMG-wrapped pc — absorbed into PcParams.multigrid; drives the finestLevelUnwrap branch of pcBoundOp)
  - scalar-field (real / complex — the E type parameter; complex pc unfolds via complex-from-real-lift, body-uniform)
  - op-pc_op-coincidence (distinct operators / pc_op = op double-branded — the intended escape hatch the brand discipline permits)
---

# preconditioning-framework

The L4 **composition framework** that binds a constructed Krylov solver to a constructed
preconditioner and holds the two-operator `(op, pc_op)` binding the [`ksp_solve`](./ksp_solve.md)
cap iterates against. Where `ksp_solve` is the outer-driver cap (the `Solve`-monadic *coordination*
that folds [`krylov-step`](./krylov-step.md) to convergence), `preconditioning-framework` is the
**construction-and-binding surface one shell outside it**: the `buildKspSolver` constructor that
assembles the `(ksp, pc)` pair via constructed-operator factories and the `setOperators` bind that
attaches the true operator and the (possibly distinct) preconditioner-assembly operator. It is the
L4 home of Palace's `BaseKspSolver` framework — the type at which build-time composition and
run-time iteration are stratified, the `(op, pc_op)` role distinction is capability-typed, and the
`finestLevelUnwrap` structural adapter is hoisted into a derived view.

## Context

L4's job is to write algorithms in a graph-evaluation calculus that makes lifetimes, dispatch
sites, and effect placement structural. The preconditioning framework is the part of Palace's
linear-solve stack that is **not** iteration at all: it is the construction and binding of the
operator graph the solve runs against. The L4 form captures three rotations of this surface that
the C++ leaves implicit:

1. **Build-time vs run-time stratification.** `buildKspSolver` and `setOperators` construct and
   bind the operator graph; they do not iterate. Only `solve` and `applyPreconditioner` are
   run-time, and both are already whole-vector operations. The L4 typing makes this a structural
   invariant — the build-time primitives cannot appear inside the monadic body
   ([`state-stratification`](../concepts/state-stratification.md), [`solve-monad`](../concepts/solve-monad.md)
   constructor-vs-body split).
2. **Capability typing of the `(op, pc_op)` roles.** The two operators are both `Op<E>` at the
   C++ layer (the L0 assertion-guards cannot tell them apart); L4 brands them `TrueOp<E>` and
   `PcAssemblyOp<E>` so a role swap is a type error ([`capability-typing`](../concepts/capability-typing.md)
   — this chapter is its canonical L4 use site).
3. **Derived-view hoisting of the unwrap adapter.** `setOperators` sometimes binds
   `finestLevelUnwrap(pc_op)` into `pc` rather than `pc_op` itself; storing the raw `pc_op` while
   binding the unwrapped operator is a stored-vs-bound divergence. L4 hoists the adapter into a
   `pcBoundOp` derived view computed on demand from the primitive binding
   ([`derived-view-hoisting`](../concepts/derived-view-hoisting.md)).

This framework is defined **in L4 vocabulary** (high→low discipline): its semantics, signatures,
and laws are stated in terms of the `Solve` monad, the state strata, and the brand discipline —
NOT in terms of L3 value-threading. The L4 form is **methodology-level**; the Palace evidence
sits at L0 (the `BaseKspSolver` class + the `SetOperators` body). The cap it binds is the firm
[`ksp_solve`](./ksp_solve.md); the per-method iteration that consumes the binding lives in the
`cg` / `gmres` / `fgmres` slices' own L4 forms (the `applyLinop s.ksp b` hand-off boundary).

## Record definition

The framework names seven L4 record/handle types. They are **single-consumer** (only this chapter
uses them in signatures), so they are defined here in-chapter (record-definition obligation — a
≥2-consumer record would earn a `concepts/` page). All are L4 calculus types; their L0 backing is
the `BaseKspSolver` C++ class (`palace/linalg/ksp.hpp:30-76`).

```ts
// Operator internal params — built once at construction, immutable through the solve.
// Construction-stratum (readonly).
type KspParams<E> = {
  ksp_method: "CG" | "GMRES" | "FGMRES",   // krylov-method variant; bound at construction
  pc_side: "LEFT" | "RIGHT",               // GMRES/FGMRES only
  gs_orthog: "MGS" | "CGS2",               // Gram-Schmidt orthogonalisation kind
  restart_dim: number,                     // GMRES/FGMRES restart dimension
  tol_rel: number,                         // relative convergence tolerance
  tol_abs: number,                         // absolute convergence tolerance
  max_it: number,                          // iteration cap
  initial_guess: boolean,                  // use the input x as the initial iterate
};

// Preconditioner internal params — built once at construction, immutable. Construction-stratum.
type PcParams<E> = {
  pc_type: "AMS" | "BOOMER_AMG" | "SUPERLU" | "STRUMPACK" | "STRUMPACK_MP" | "MUMPS" | "JACOBI",
  multigrid: boolean,        // fespaces.num_levels > 1 — wraps pc in a GeometricMultigridSolver
  aux_smoothing: boolean,    // aux_fespaces present — auxiliary-space smoothing
  scalar_field: "real" | "complex",   // the E specialisation
};

// The constructed operators themselves — typed handles, internal state opaque.
type Ksp<E> = IterativeSolver<E> & { params: KspParams<E> };   // construction-stratum
type Pc<E>  = Solver<E>          & { params: PcParams<E> };     // construction-stratum

// Sim-state binding — set once by setOperators, read every solve. The (op, pc_op) pair the
// solver is bound to, capability-branded (see §"Capability typing").
type OpBinding<E> = {
  op:    TrueOp<E>,         // primitive: the true operator ksp iterates against, as the caller passed it
  pc_op: PcAssemblyOp<E>,   // primitive: the pc-assembly operator, as the caller passed it (may be a multigrid wrapper)
};

// Bookkeeping — accumulated across solve calls. The only mutable cross-call run-time state.
type Counters = {
  mult:    number,     // number of Mult (solve) invocations
  mult_it: number,     // cumulative inner iterations across all solves
};

// The full solver bundle.
type BaseKspSolver<E> = {
  ksp:      Ksp<E>,                       // construction-stratum (readonly after build)
  pc:       Pc<E>,                        // construction-stratum (readonly after build)
  binding:  OpBinding<E> | null,          // sim-state; null before setOperators (the bind precondition)
  counters: Counters,                     // run-time bookkeeping
};
```

| record | stratum | meaning | L0 home |
|---|---|---|---|
| `KspParams<E>` | construction (readonly) | Krylov-method + tolerance config; the krylov-method/orthog/restart variant absorbed here | `LinearSolverData` config surface; consumed by `ConfigureKrylovSolver` (`palace/linalg/ksp.cpp:25-99`) |
| `PcParams<E>` | construction (readonly) | preconditioner-type + multigrid + scalar-field config; the pc-type/multigrid variant absorbed here | consumed by `ConfigurePreconditionerSolver` (`palace/linalg/ksp.cpp:125-235`) |
| `Ksp<E>` | construction (readonly) | the constructed iterative solver handle (internal Krylov state opaque) | the `unique_ptr<IterativeSolver<OperType>> ksp` member (`palace/linalg/ksp.hpp:40`) |
| `Pc<E>` | construction (readonly) | the constructed preconditioner handle (internal factorisation opaque) | the `unique_ptr<Solver<OperType>> pc` member (`palace/linalg/ksp.hpp:41`) |
| `OpBinding<E>` | sim-state (set-once) | the `(op, pc_op)` operators the solver is bound to; null until `setOperators` | set by `BaseKspSolver::SetOperators` (`palace/linalg/ksp.cpp:276-293`) |
| `Counters` | run-time | per-solve telemetry (call count + cumulative iterations) — the only mutable cross-call state | the `mutable int ksp_mult, ksp_mult_it` members (`palace/linalg/ksp.hpp:46`); accumulated in `Mult` (`palace/linalg/ksp.cpp:296-310`) |
| `BaseKspSolver<E>` | mixed | the full bundle: two readonly constructed handles + the set-once binding + run-time counters | the `BaseKspSolver` class (`palace/linalg/ksp.hpp:30-76`) |

Ephemeral intermediates (per-iteration residuals, search directions, Krylov bases, Givens
accumulators) live inside `Ksp<E>`'s opaque internal state and are not surfaced here — they belong
to the per-method slices' L4 forms.

## Signature

The framework has two construction primitives and two run-time primitives. The construction
primitives are **pure** (no iteration state flows through them); the run-time primitives run in the
`Solve E` monad.

    -- Construction phase (build-time, pure)
    buildKspSolver :: LinearConfig -> FESpaceHierarchy -> Maybe AuxFESpaces -> BaseKspSolver E
    setOperators   :: TrueOp E -> PcAssemblyOp E -> BaseKspSolver E -> BaseKspSolver E

    -- Run-time phase (monadic)
    solve               :: BaseKspSolver E -> Vec E -> Vec E -> Solve E (Vec E)
    applyPreconditioner :: BaseKspSolver E -> Vec E -> Solve E (Vec E)

### Constructor phase (build-time)

`buildKspSolver` is a sequence of constructed-operator-factory calls
([`constructed-operator-factory`](../concepts/constructed-operator-factory.md)) and a one-shot
preconditioner bind. The two factory calls are independent; the
[`variant-absorption`](../concepts/variant-absorption.md) of all four variant axes (krylov-method,
pc-type, multigrid, scalar-field) completes inside the factories and is not re-inspected downstream:

```text
buildKspSolver cfg fes auxFes =
  let ksp = constructedOperatorFactory KrylovRole cfg     -- absorbs ksp_method, pc_side, orthog, restart
      pc  = constructedOperatorFactory PrecondRole cfg fes auxFes
                                                          -- absorbs pc_type, multigrid, aux, scalar_field
      _   = bindPreconditioner ksp pc                     -- one-shot bind on ksp internals
  in BaseKspSolver { ksp, pc, binding = Nothing, counters = Counters 0 0 }
```

`setOperators` stores the primitive operators and binds them; the structural-adapter branch lives
in the `pcBoundOp` derived view (see §"Derived-view hoisting"):

```text
setOperators op pc_op s =
  let binding'   = OpBinding op pc_op                       -- primitives stored verbatim
      pc_bound   = pcBoundOp binding' s.pc                  -- derived view
      _          = s.ksp `setOpInternal` op
      _          = s.pc  `setOpInternal` pc_bound
  in s { binding = Just binding' }
```

### Body phase (run-time, monadic)

`solve` delegates the iteration to `ksp` (whose own L4 form carries the per-step state) and threads
the telemetry counters monadically; `applyPreconditioner` is a whole-vector application of the
preconditioner:

```text
solve s x_initial b = do
  x_out <- applyLinop s.ksp b                  -- delegates to ksp's per-method body
  n_it  <- getNumIterations s.ksp
  modifyCounters $ \c -> c { mult    = c.mult    + 1
                           , mult_it = c.mult_it + n_it }
  return x_out

applyPreconditioner s r = applyLinop s.pc r
  -- For E = Complex with a non-multigrid pc, applyLinop on Pc<Complex> unfolds via
  -- complex-from-real-lift (see concepts/complex-from-real-lift):
  --   applyLinop pc r = do
  --     z_re <- applyLinop pc.inner r.re
  --     z_im <- applyLinop pc.inner r.im
  --     return (Complex z_re (scal (-1) z_im))
```

The `Solve E` monad threads the counter state; vector results are returned pure-functionally at
this layer. The per-iteration state is hidden inside `applyLinop s.ksp b` — that call is the
boundary at which the framework hands off to the per-method slice's L4 form.

## Capability typing

The `(op, pc_op)` distinction is a calculus-level fact, not a naming convention. Both operators are
`Op<E>`; the framework brands them with phantom (zero-runtime) capability markers
([`capability-typing`](../concepts/capability-typing.md)):

```ts
type TrueOp<E>       = Op<E> & { readonly __cap: "true" };
type PcAssemblyOp<E> = Op<E> & { readonly __cap: "pc_assembly" };

declare function asTrueOp<E>(o: Op<E>):       TrueOp<E>;
declare function asPcAssemblyOp<E>(o: Op<E>): PcAssemblyOp<E>;
```

`setOperators :: TrueOp E -> PcAssemblyOp E -> ...` consumes them role-positionally; passing one
brand where the other is expected is a type error at L4 — catching a class of misuse the C++ layer
cannot (both are `Operator*`). The brand discipline is internal to the framework: model-layer
callers brand the operators once at construction and the brands flow through unchanged.

The **escape hatch** is intended: `pc_op = op` (the same underlying operator double-branded
`asTrueOp(K)` / `asPcAssemblyOp(K)`) is permitted — the brand discipline forbids passing one brand
where the other is expected, NOT applying both brands to one operator. Some model-layer call sites
legitimately precondition the true operator against itself.

## Derived-view hoisting

`setOperators` binds the **finest-level-unwrapped** preconditioner operator into `pc` whenever the
caller hands a multigrid `pc_op` to a non-multigrid `pc`, but stores the raw `pc_op` in the binding
— a stored-vs-bound divergence the brand typing does not catch (both carry the `PcAssemblyOp<E>`
brand). The framework hoists the adapter into a derived view
([`derived-view-hoisting`](../concepts/derived-view-hoisting.md);
[`finest-level-unwrap`](../concepts/finest-level-unwrap.md)):

```ts
// Derived view: the operator actually bound into pc after the structural adapter.
// Computed from pc_op plus the type of pc; never stored.
declare function pcBoundOp<E>(binding: OpBinding<E>, pc: Pc<E>): PcAssemblyOp<E>;
// pcBoundOp(b, pc) =
//   if isMultigridOp(b.pc_op) && !isMultigridSolver(pc) then finestLevelUnwrap(b.pc_op)
//   else b.pc_op
```

`finestLevelUnwrap :: PcAssemblyOp E -> PcAssemblyOp E` is brand-preserving (the unwrapped finest
level inherits the pc-assembly role from its multigrid parent) — the load-bearing observation that
matches the source: the unwrap is only ever applied to `pc_op`, never to `op`. The binding stores
only the primitive inputs; `pcBoundOp` is the single definition site of the adapter, recomputed on
demand and never cached.

## Algebraic laws

1. **Bind precondition.** `solve s _ _` is well-defined only when `s.binding ≠ null`. The
   `binding : OpBinding<E> | null` typing makes a `solve` on an unbound solver a type error at L4 —
   the structural form of the L0 assertion-guard.
2. **Stratification.** `KspParams` / `PcParams` (construction, readonly) and `Ksp` / `Pc`
   (construction handles) are immutable through the solve; `binding` is set once by `setOperators`;
   only `counters` mutates per `solve`. Cross-stratum aliasing is type-forbidden — the build-time
   primitives (`constructedOperatorFactory`, `bindPreconditioner`, `finestLevelUnwrap`) cannot
   appear inside the `Solve E` body.
3. **Brand role-fixity.** `asTrueOp` and `asPcAssemblyOp` are run-time identities;
   `setOperators` demands the two brands positionally. Role confusion is type-rejected; the
   `pc_op = op` double-brand is the permitted escape.
4. **Derived-view consistency.** `pcBoundOp` is the unique path from `(binding, pc)` to the
   operator bound into `pc`; the stored `binding.pc_op` and the bound operator agree exactly when
   no unwrap fires (single-level pc or non-multigrid `pc_op`), and `pcBoundOp` returns the unwrapped
   operator otherwise. `pcBoundOp` is a build-time derived view — it changes only on `setOperators`
   or a `pc`-type change, never in the monadic body.
5. **Counter monotonicity.** `solve` increments `counters.mult` by 1 and `counters.mult_it` by the
   inner iteration count; the counters are the only cross-`solve` state and are monotone
   non-decreasing (read off the const `Mult` body, `palace/linalg/ksp.cpp:296-310`). This is the
   element-independence witness `solve_family` relies on for its map homomorphism.

## Variant axes

- **krylov-method** (CG / GMRES / FGMRES) — absorbed into `KspParams` at construction; the body
  phase has no branch on it.
- **pc-type** (AMS / BOOMER_AMG / SUPERLU / STRUMPACK / STRUMPACK_MP / MUMPS / JACOBI) — absorbed
  into `PcParams` at construction by `ConfigurePreconditionerSolver`.
- **multigrid** (single-level pc / GMG-wrapped pc) — absorbed into `PcParams.multigrid`; drives the
  `finestLevelUnwrap` branch of `pcBoundOp`.
- **scalar-field** (real / complex) — the `E` type parameter; a complex pc unfolds via
  [`complex-from-real-lift`](../concepts/complex-from-real-lift.md), body-uniform.
- **op-pc_op-coincidence** (distinct / `pc_op = op` double-branded) — the intended capability-typing
  escape hatch.

## Evidence

The framework's L0 home is `BaseKspSolver`:

- **The class** — `BaseKspSolver<OperType>` owns `unique_ptr<IterativeSolver<OperType>> ksp` and
  `unique_ptr<Solver<OperType>> pc`, the `mutable int ksp_mult, ksp_mult_it` counters, and declares
  `SetOperators` / `Mult` (`palace/linalg/ksp.hpp:30-76`).
- **The bind** — the direct-injection constructor binds the preconditioner via
  `ksp->SetPreconditioner(*pc)` (`palace/linalg/ksp.cpp:264-273`, bind at `:272`); the auto-config
  constructor delegates to `ConfigureKrylovSolver` + `ConfigurePreconditionerSolver`.
- **The `(op, pc_op)` binding** — `BaseKspSolver::SetOperators(const OperType &op, const OperType
  &pc_op)` binds `ksp` to the true operator (`ksp->SetOperator(op)`) and `pc` to the
  preconditioner-assembly operator, with the finest-level-unwrap branch when a multigrid `pc_op`
  meets a non-multigrid `pc` (`palace/linalg/ksp.cpp:276-293`; the unwrap branch
  `mg_op && !mg_pc ⇒ pc->SetOperator(mg_op->GetFinestOperator())` at `:281-292`).
- **The counter accumulation** — the const `Mult` body does the solve and accumulates
  `ksp_mult++` / `ksp_mult_it += ksp->GetNumIterations()` (`palace/linalg/ksp.cpp:296-310`).
- **The factories** — `ConfigureKrylovSolver` dispatches the krylov-method
  (`palace/linalg/ksp.cpp:25-99`); `ConfigurePreconditionerSolver` dispatches the pc-type and wraps
  in a `GeometricMultigridSolver` when `fespaces.GetNumLevels() > 1`
  (`palace/linalg/ksp.cpp:125-235`).

## Status

`firm` (harvested cycle-096 D1 from OQ `l4-preconditioning-framework-promotion`; the
firm-on-positive-structure / syntactic-identity escape). Every law is a syntactic read-off over the
positive `BaseKspSolver` source plus the firm [`ksp_solve`](./ksp_solve.md) cap (c048): the bind
precondition is the L0 binding guard, the stratification is the build-vs-run split read off the const
class, the brand role-fixity and derived-view-consistency are type-level rotations of the
`SetOperators` body (no run-time content added), and the counter monotonicity is read off the const
`Mult` body (`palace/linalg/ksp.cpp:296-310`). The `depends-on: [L4/ksp_solve]` dependency is firm,
so the rank invariant `rank(preconditioning-framework) ≤ rank(ksp_solve)` holds (firm ≤ firm). No
constructive sub-part rests on a negative anchor; the v0.2 capability typing and v0.3 derived-view
hoist are type-level refinements of positive source, not literature reconstructions. Source-of-truth
absorbed from the `cg_preconditioning_framework` slice's §L4 / §L4-v0.2 / §L4-v0.3 (the slice is the
cycle-001-era precursor; this chapter is its firm L4 home, re-citing L0 directly).
```

### 2. `book/src/concepts/capability-typing.md` — re-point the two slice refs (lines 26, 55)

```edit:book/src/concepts/capability-typing.md
[old]: - **`(op, pc_op)` in `BaseKspSolver`** — both are `Op<E>`; confusing them produces a wrong preconditioned Krylov iteration that may still converge to a wrong answer. See [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) L4 v0.2.
[new]: - **`(op, pc_op)` in `BaseKspSolver`** — both are `Op<E>`; confusing them produces a wrong preconditioned Krylov iteration that may still converge to a wrong answer. See [`preconditioning-framework`](../L4/preconditioning-framework.md) §"Capability typing".
```

```edit:book/src/concepts/capability-typing.md
[old]: - [`cg_preconditioning_framework`](../spec/slices/cg_preconditioning_framework.md) L4 v0.2 — the canonical first use site (TrueOp / PcAssemblyOp brands on the KSP binding).
[new]: - [`preconditioning-framework`](../L4/preconditioning-framework.md) §"Capability typing" — the canonical L4 use site (TrueOp / PcAssemblyOp brands on the KSP binding).
```

### 3. `book/src/SUMMARY.md` — add the chapter row (alpha position in the Outer-driver kind-group)

```edit:book/src/SUMMARY.md
[old]:   - [ksp_solve](./L4/ksp_solve.md)
  - [solve_family](./L4/solve_family.md)
[new]:   - [ksp_solve](./L4/ksp_solve.md)
  - [preconditioning-framework](./L4/preconditioning-framework.md)
  - [solve_family](./L4/solve_family.md)
```

### 4. `book/src/L4/index.md` — add the dep-map row (Outer-driver group, alpha between ksp_solve and solve_family)

The new row goes in the "Outer-driver caps & coordination combinators" table. The group's full
row set sorts alphabetically (case-insensitive) as: `EigOutcome`, `eigsolve`, `fold_solve`,
`frequency_sweep`, `ksp_solve`, `Outcome`, `preconditioning-framework`, `restart_cycle`,
`solve_family`, `solve_loop` (`Outcome` < `preconditioning-framework` < `restart_cycle`: `o` <
`p` < `r`). So the new row inserts between the `Outcome` row (line 118) and the `restart_cycle`
row (line 119). The edit below anchors on the `restart_cycle` row to place the new row immediately
before it.

```edit:book/src/L4/index.md
[old]: | `restart_cycle` | `restart_cycle :: OpParams -> Inputs -> Solve Outcome` (`one_cycle` non-restarted specialisation). Builds `fresh_krylov`, runs the inner `iterate-while`-family kernel fold (sole `SimState` effect `modify (\s -> s { it = s.it + 1 })`), folds the correction into `SimState.x` via one `modify`, classifies the returned bundle into an `Outcome` once at the boundary. `Krylov` threaded as a plain `let`-bound value (born at cycle entry, discarded at exit). |
[new]: | [`preconditioning-framework`](./preconditioning-framework.md) | `buildKspSolver :: LinearConfig -> FESpaceHierarchy -> Maybe AuxFESpaces -> BaseKspSolver E`; `setOperators :: TrueOp E -> PcAssemblyOp E -> BaseKspSolver E -> BaseKspSolver E`; `solve :: BaseKspSolver E -> Vec E -> Vec E -> Solve E (Vec E)`. The **composition-and-binding framework** one shell outside the [`ksp_solve`](./ksp_solve.md) cap: the `buildKspSolver` constructor assembles the `(ksp, pc)` pair via constructed-operator factories; `setOperators` binds the capability-typed `(TrueOp, PcAssemblyOp)` pair (the C++ `BaseKspSolver` `(op, pc_op)` two-operator convention). Build-time vs run-time stratified; `(op, pc_op)` capability-typed (`TrueOp`/`PcAssemblyOp` brands); the `finestLevelUnwrap` adapter hoisted into the `pcBoundOp` derived view. Records `KspParams`/`PcParams`/`OpBinding`/`Ksp`/`Pc`/`Counters`/`BaseKspSolver` defined in-chapter §Record definition (single-consumer). | Caps: [`ksp_solve`](./ksp_solve.md) (the outer-driver cap whose `(op, pc_op)` binding this framework holds). Concepts: `state-stratification` (build-vs-run strata), `capability-typing` (the `TrueOp`/`PcAssemblyOp` brands — this is its canonical L4 use site), `derived-view-hoisting` (`pcBoundOp`), `constructed-operator-factory`, `finest-level-unwrap`, `complex-from-real-lift`, `variant-absorption`, `solve-monad`, `solver-as-operator`. | L0 directly (`BaseKspSolver`, `palace/linalg/ksp.cpp:276-293` `SetOperators`; the class `palace/linalg/ksp.hpp:30-76`); no dedicated L4>L3 theme (this is a construction/binding framework, not an iteration the loop-rotation themes carry — the per-method iteration it binds lowers via the krylov-step/ksp-solve dissolution themes). | `firm` (harvested cycle-096 D1 from OQ `l4-preconditioning-framework-promotion`; firm-on-positive-structure / syntactic-identity escape — every law a read-off over the positive `BaseKspSolver` source + the firm `ksp_solve` cap (c048); the v0.2 capability typing + v0.3 derived-view hoist are type-level rotations of positive source, not literature reconstructions. `depends-on: [L4/ksp_solve]` firm so the rank invariant holds. Absorbed from the `cg_preconditioning_framework` slice §L4/v0.2/v0.3, re-citing L0 directly) |
| `restart_cycle` | `restart_cycle :: OpParams -> Inputs -> Solve Outcome` (`one_cycle` non-restarted specialisation). Builds `fresh_krylov`, runs the inner `iterate-while`-family kernel fold (sole `SimState` effect `modify (\s -> s { it = s.it + 1 })`), folds the correction into `SimState.x` via one `modify`, classifies the returned bundle into an `Outcome` once at the boundary. `Krylov` threaded as a plain `let`-bound value (born at cycle entry, discarded at exit). |
```

## Supporting evidence

### L0 citations (all self-verified this cycle via codemap read + citecheck --anchor, on-disk)

- `palace/linalg/ksp.cpp:276-293` — `BaseKspSolver::SetOperators(const OperType &op, const OperType &pc_op)` (decl at `:277`, body `:278-293`); citecheck `[ok]` anchor `SetOperators` at 277. END line 293 = closing brace (disk-confirmed via read_range 274-314).
- `palace/linalg/ksp.cpp:281-292` — the finest-level-unwrap branch (`mg_op`/`mg_pc` dynamic_casts `:282-283`, `if (mg_op && !mg_pc) ⇒ pc->SetOperator(mg_op->GetFinestOperator())` `:284-287`); citecheck `[ok]` anchor `GetFinestOperator` at 287.
- `palace/linalg/ksp.cpp:264-273` — the direct-injection ctor `SetPreconditioner(*pc)` bind; citecheck `[ok]` anchor `SetPreconditioner` at 272.
- `palace/linalg/ksp.cpp:296-310` — the const `Mult` body, `ksp_mult++` / `ksp_mult_it +=` (`:308`/`:309`); citecheck `[ok]` anchor `ksp_mult` at 308/309.
- `palace/linalg/ksp.cpp:25-99` — `ConfigureKrylovSolver` (anchor at 28); `:125-235` — `ConfigurePreconditionerSolver` (anchor at 127); both citecheck `[ok]`.
- `palace/linalg/ksp.hpp:30-76` — the `BaseKspSolver` class (`ksp`/`pc` members `:40`/`:41`, `ksp_mult,ksp_mult_it` counters `:46`, `SetOperators` decl `:70`, `Mult` decl `:72`); citecheck `[ok]` anchor `BaseKspSolver`.

(All re-cited L0 directly — NOT via the slice. The slice's existing §L0 ranges, lines 58-72,
were the localization map.)

### Slice provenance (source-of-truth absorbed, NOT cited)

`book/src/spec/slices/cg_preconditioning_framework.md`:
- §L4 (lines 308-426) — the `KspParams`/`PcParams`/`OpBinding`/`BaseKspSolver` records + constructor/body split.
- §L4 v0.2 (lines 428-485) — capability typing (`TrueOp`/`PcAssemblyOp` brands, `finestLevelUnwrap` brand-preservation, the `pc_op = op` escape hatch).
- §L4 v0.3 (lines 487-548) — derived-view hoisting (`pcBoundOp`, stored-vs-bound divergence elimination).

### Chapters / pages touched

- NEW `book/src/L4/preconditioning-framework.md` (firm).
- `book/src/concepts/capability-typing.md` (lines 26, 55 re-pointed at the new chapter).
- `book/src/SUMMARY.md` (chapter row added, alpha in Outer-driver kind-group).
- `book/src/L4/index.md` (dep-map row added, same group/slot — D1 SOLE owner this cycle).

### Graded-stack frontmatter (HARD-gate-new)

- `rank: firm` + `edges: depends-on: [L4/ksp_solve (firm) + the L0 evidence range with kind: cites-evidence]`.
- All concept refs classified `reference` (none is a feature-surface root; they are narrative /
  record / discipline pages — `reference` per the scheme §2 deliberate-classification rule).
- Rank invariant: `rank(preconditioning-framework=firm=3) ≤ rank(L4/ksp_solve=firm=3)` — holds.
  No feature-root in the `depends-on` set (the one root-adjacent relationship, the cap, is itself
  vocabulary not a root, so `depends-on` is correct; no edge-to-root mis-typed as blocking).

## Open questions / caveats

- **`l4-preconditioning-framework-promotion` OQ is now CLOSED-by-this-chapter** (the slice header's
  pending-lift note named exactly this chapter + OQ). Flag for the integrator to mark it resolved
  in `scaffolding/open-questions.md` (the slice itself stays — deletion is the deferred batch-31
  tranche).
- **Record-definition obligation discharged in-chapter (single-consumer).** `KspParams` /
  `PcParams` / `OpBinding` / `Ksp` / `Pc` / `Counters` / `BaseKspSolver` are named in signatures
  ONLY in this chapter, so they earn an in-chapter `## Record definition`, not a `concepts/` page.
  IF a future chapter (e.g. a `geometric_multigrid` L4 form, or a `boundary-mode` driver column)
  comes to name `OpBinding` / `BaseKspSolver` in its own signatures, that crosses the ≥2-consumer
  bar and `OpBinding` (or `BaseKspSolver`) should be promoted to a `concepts/<record>.md` page —
  flag `record-OpBinding-may-need-concept-page` as a watch item, NOT actionable now.
- **`derived-view-hoisting.md` deliberately NOT edited** — disk-confirmed it does not cite the
  slice (its worked examples are CG/Chebyshev; the slice header's "cites v0.3" claim is the slice's
  own framing). The new chapter's §"Derived-view hoisting" still *references* the concept page
  (downward orientation link), which is correct and one-directional.
- **The other ~9 concept pages naming the slice** (`two_operator_split`,
  `constructed-operator-factory`, `complex-from-real-lift`, `finest-level-unwrap`, `counter-update`,
  `solver-as-operator`, `build-time-vs-run-time-stratification`, `rotation`, `dependency-map`)
  resolve fine while the slice exists; their repoint is the DEFERRED batch-31 deletion tranche, NOT
  this cycle (per the planner scope).
- **Dep-map alpha-slot note for the integrator:** the new row sorts between the `Outcome` row and
  the `restart_cycle` row in the "Outer-driver caps & coordination combinators" table
  (`Outcome` < `preconditioning-framework` < `restart_cycle` alphabetically). The proposed-changes
  edit anchors on the `restart_cycle` row to place the new row immediately before it.
