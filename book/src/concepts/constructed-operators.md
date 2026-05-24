# constructed operators

## Context

A peer concept to `rotation.md` and `variant-absorption.md`. **Constructed operators** are a standard pattern from evaluation / immutable-graph traditions (Haskell, MLIR, JAX, burn, …): an operator is built **once** with internal immutable state — configs, pre-built tables, factorizations, mesh+basis caches, time-step constants — and then **applied** as a pure function from the caller's perspective.

The construction and the application are separated by phase:

- **Construction phase.** Inputs include configs, raw tables, problem-specific data. Output is an operator object with internal immutable state. Often expensive (factorize, precompute, allocate).
- **Application phase.** Inputs include only the operand (the sim state being transformed). Output is the new sim state. Pure with respect to the operator's internals.

This concept was introduced by the user during 2026-05-24 meta-review #3 enactment, motivated by friction in cycles 7+9 where variant-absorption recurred because configs and selectors were being deep-plumbed through every L1 step. Constructed operators are one of the canonical routes to procedural and primitive-sequence absorption (per `variant-absorption.md` *Levels of absorption*).

This concept is **methodology**, not a tensor primitive (same kind as `rotation.md` and `variant-absorption.md`).

## When to construct

A concept is a candidate for "constructed operator" treatment when:

1. **Construction-time inputs are static across many applications.** Preconditioner kind + side + matrix → constructed once per solve, applied many times per iteration.
2. **Apply-time inputs are dynamic.** The sim state changes per call; the configuration doesn't.
3. **Variants would otherwise force deep-plumbing.** If `side ∈ {LEFT, RIGHT, NONE}` causes every per-step procedure to inspect `side` and branch, constructing a `PreconditionedOperator(M, side)` lets the per-step procedure call `op.apply(v)` without ever re-inspecting `side`.
4. **The cost is amortized.** Construction may be expensive; the value comes from many cheap applications. A constructed operator used once is overkill.

## Worked example: GMRES preconditioning (resolves cycle-7 / cycle-9 friction)

**Without constructed operators (cycle-7 / cycle-9 shape):**

L1 per-step procedure mentions `side` at multiple sites:

```
# Arnoldi step:
if side == LEFT:   w = M.apply(A.apply(v))
elif side == RIGHT: w = A.apply(M.apply(v))
else:               w = A.apply(v)

# Solution update:
if side == RIGHT and not flexible:
    x = x_0 + M.apply(V_m @ y_m)
else:
    x = x_0 + W_m @ y_m
```

Variant absorption is **invariant-clean** (`x = x_0 + W_m y_m`) but the procedural code re-inspects `side` at ≥2 sites and the primitive sequence differs per `side`. Levels (b) procedural and (c) primitive-sequence absorption (per `variant-absorption.md`) **fail**.

**With constructed operators:**

Construct once at solve start:

```
op     = construct_krylov_operator(A, M, side)        # internal: side, M, A
update = construct_update_basis(side, flexible, M)    # internal: side, flexible, M
```

L1 per-step procedure:

```
# Arnoldi step:
w = op.apply(v)                # uniform across side

# Solution update:
x = update.combine(x_0, V_m, y_m)   # uniform across side; update knows whether to apply M
```

The `side` parameter and `M` matrix are hidden inside the constructed `op` and `update`. The per-step procedure is **uniform across `side`** because the variant is absorbed into the constructed operator's internal state.

Variant-absorption levels (per `variant-absorption.md` *Levels of absorption*):

- **(a) invariant-level:** `x = x_0 + W_m y_m` ✓ (unchanged)
- **(b) procedural:** `side` mentioned 0 times in L1 procedure ✓ (was ≥2)
- **(c) primitive-sequence:** `op.apply(v)` is one primitive call across all `side` values ✓ (was 3 sequences)

All three levels achieved through construction. The `side` variant logic moves into the construct-time code, which is the right place for it — that's where the contract is established once per solve.

## Relationship to existing concepts

### To `rotation.md` (state hiding, criterion 1)

Constructing an operator is a direct route to **rotation criterion (1) state hiding**. The operator's internal state (config, tables, factorizations) is exposed at L_n (where you read `A`, `M`, `side`, factorizations) and hidden at L_{n+1} (where you call `op.apply(v)`).

The carry-through clause in `rotation.md` applies cleanly: tables and factorizations that carry through unchanged from construction to application are legitimate — they're already idiomatic in the constructed-operator pattern at L_{n+1}.

### To `variant-absorption.md` (levels of absorption)

Constructed operators are one of the canonical routes to achieving **all three levels** of variant absorption simultaneously. When a slice has orthogonal variants that don't admit a clean invariant unification (cycle-7's `side` case is the worked counter-example), constructing an operator that internalizes the variant decision is the standard fix.

The `variant-absorption.md` "test" question — "can the variant be expressed as a binding of a parameter introduced in the main L1 statement?" — generalizes for constructed operators to: "can the variant be made an argument to the constructor, so the binding happens once at construct time?"

### To L4 calculus (operator internal parameters)

The L4 calculus already distinguishes (per `CLAUDE.md` *Output structure*):

- **Sim state** — the iterate, residual, convergence flags; evolves through the algorithm.
- **Operator internal parameters** — matrix entries, preconditioner factorizations, mesh+basis tables, time-step constants; held as closure-like data, applied to sim state, but not themselves evolving during a solve.
- **Ephemeral intermediates** — per-step values that don't survive across iterations.

Constructed operators are **the realization of "operator internal parameters as closure-like data."** L4 already names the category; this concept page makes the construction pattern explicit at L1/L2 so the L3→L4 rotation has a clean primitive to map to.

## What constructed operators are NOT

- **Not a mutable cache.** The operator's internal state is set at construction and unchanged thereafter. If something needs to update mid-solve (iteration count, residual norm), it's sim state — thread it explicitly, do not stuff it into the operator.
- **Not a free pass on per-call cost.** Construction cost is real. The value is amortizing across many applies. Single-use operators are overkill — call the inner function directly.
- **Not a way to hide load-bearing spec content.** If a variant's behavior is load-bearing (changes numerical properties, convergence guarantees, condition numbers), construction must not hide it. The constructed operator's **contract** captures what `apply` does for each construction; the internal state is hidden, the *observable behavior* is not. The contract belongs in the slice; the implementation belongs in the constructor.

## Limits of constructed-operator absorption

(Added 2026-05-24 meta-review #5, from cycle 14's FGMRES friction — the 4th instance of the variant-absorption recurrence cluster, all on `gmres`.)

Constructed operators absorb variants when the variant is **bound once at construction and applied many times** without changing. They DO NOT absorb variants when the variant is **per-step** — when the operator changes between applications during a single solve.

### When the pattern works

- Preconditioner choice + side at solve start: `M` is fixed for the whole solve. `op = construct_krylov_op(A, M, side)` absorbs all three axes (kind, side, identity-vs-nontrivial).
- Mesh + basis tables at simulation start: computed once, reused per timestep.
- Time-step coefficients in fixed-step integration.

### When the pattern fails (per-step variants)

- **Flexible preconditioners (FGMRES, etc.)**: the preconditioner `M_k` is allowed to change between Arnoldi steps in a single solve. `construct_krylov_op(A, M, side)` cannot internalize `M_k` because there is no single `M` to bind at construction.
- **Time-varying operators**: when `A_k` depends on the iteration index (active-set methods, IMEX integrators).
- **Adaptive parameters**: when an operator's behavior depends on a value computed mid-cycle.

### The fix: threaded state, not just constructed state

For per-step variants, the **threaded state itself** must change — the variant becomes part of the sim-state schema, not the operator-internal-parameters schema. Concretely for FGMRES:

- **Standard GMRES L1 state**: `{x, V, H, s, cs, sn, …}`. The preconditioner lives in the constructed `op`.
- **FGMRES L1 state**: `{x, V, H, s, cs, sn, Z, …}`. The per-step preconditioned basis `Z` is threaded because each `Z[j] = M_j · V[j]` may use a different `M_j`. The L4 ownership category for `Z` is **sim state** (evolves per step), not operator-internal-parameters.

The L1 state schema's expansion is **required**. Trying to absorb FGMRES into the standard `construct_krylov_op` interface fails primitive-sequence absorption (per `variant-absorption.md` *Levels of absorption*, criterion (c)): the cycle-close primitive sequence diverges (`x = x_0 + V_m y_m` for GMRES vs. `x = x_0 + Z_m y_m` for FGMRES).

### Decision rule

When considering a constructed-operator absorption for a variant:

1. **Is the variant bound at construction or per-step?**
2. If **construction**: constructed-operator pattern works; proceed.
3. If **per-step**: constructed-operator pattern fails. The variant must enter the threaded sim-state schema. Add the per-step value (e.g., the `Z` basis) to L1 state, and document it as sim state in L4 ownership categories.

Mixed cases (some parameters at construction, others per-step) are common — the construction-side absorbs what it can; the threaded state carries the rest.

## Signature pattern

Spec form (Haskell/Scheme-flavored, per `CLAUDE.md`):

```
construct_X :: Config -> PrebuiltTables -> X
apply       :: X -> Operand -> Operand
```

Or in TypeScript-flavored record form:

```
type X = { config: Config, tables: PrebuiltTables, ... }   -- internal, opaque to callers
construct_X(cfg, tables) -> X
apply(op: X, operand: Operand) -> Operand
```

The slice should name the type, the construct function, and the apply function. Internal-state fields are listed (so the Critic can verify what is hidden) but not inspected by the apply-side caller.

## Synthesizer / Critic responsibilities

For now (until friction-from-use motivates a dedicated check):

- **Synthesizer**: when a slice's L1 procedure repeatedly inspects the same parameter, OR when a tabular config is being threaded through many layers, consider constructing an operator that internalizes it. This is one route to satisfying variant-absorption levels (b) and (c) per `variant-absorption.md`, and to rotation criterion (1) per `rotation.md`.
- **Critic**: when verdicting variant-absorption (check #9), constructed operators are a legitimate path to all three absorption levels. A slice that uses constructed operators to absorb variants passes check #9 even when the construct-side has variant logic — that's where the variant logic belongs.

A dedicated Critic check is not added on first introduction. Friction-from-use will reveal whether one is needed (over-construction, under-construction, or construction that hides load-bearing spec content).

## Origin

Introduced by the user during 2026-05-24 meta-review #3 enactment, motivated by the variant-absorption friction in cycles 7+9 (`side`-conditional smuggled into procedural L1 sites) and the general observation that deep-plumbing of configs through every layer is the failure mode that constructed operators were invented to solve in graph-evaluation traditions. See `book/src/meta-reviews/2026-05-24-cycles-7-9.md`.

## Working Notes

- Not yet exercised in a real cycle. First cycle that touches a slice with serious variant + tabular state — FE assembly with quadrature tables and basis caches, preconditioner construction with factorization, time-stepping coefficient tables — will be the first test. Watch whether the Synthesizer correctly identifies construction opportunities, or whether the rule needs to be more prescriptive (e.g., "if you inspect a parameter at ≥2 L1 sites, you MUST consider a constructed-operator absorption").
- Relationship to the burn-realization downstream artifact: burn's `Module` pattern is essentially constructed operators with backward-pass support added. The spec-level abstraction here ("constructed operator") is the right grain for L1/L2; the burn realization is a separate downstream concern. The L4 calculus's "operator internal parameters" category is the formal home for this concept once L4 is built out for a slice that uses it.
- Possible future extension: a slice that uses a constructed operator could declare both construction-cost class (`cheap` / `expensive-but-once` / `per-iteration`) and apply-cost class. This information is load-bearing for L3/L4 work but not required at L1.
