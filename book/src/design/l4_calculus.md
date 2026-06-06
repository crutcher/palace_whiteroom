# L4 — Graph-Evaluation Calculus (strawman)

**Status:** first draft. Many specifics are placeholders — the point of this document is to surface friction early, not to be authoritative. Open questions and push-back signals are noted inline.

## 0. What L4 is and is not

L4 is the **top layer of the impedance-matching stack**: a small, formally-defined graph-evaluation calculus in which Palace's algorithms are described, with formal reduction rules governing equivalence to lower-layer (L3) forms.

L4 **is**:

- A language-agnostic notation for tensor algorithms.
- Code-like — readable, with TypeScript-style record syntax and Haskell-style monadic structure — but **not** intended to compile or run anywhere.
- Formally-equipped enough that L3↔L4 equivalence is a real reduction-chain argument, not hand-waving.
- Focused on **what operations happen**, **who owns what state**, and **how state evolution is coordinated**.

L4 is **not**:

- A burn API. Not a Rust crate sketch. Not a runtime design.
- Committed to eager-vs-traced execution, persistent-DS choices, or monad-transformer stacks. Those are realization concerns for the (separate, downstream) burn-realization spec.
- A complete language. It is the smallest calculus that admits Palace's algorithms cleanly; extensions are added as friction at the lower layers demands them.

## 1. Grammar

We give a syntax in BNF, with concrete code-like notation for examples. Identifiers follow standard conventions: `x`, `y` for value variables; `α`, `β` for type variables; `A`, `B` for type names; `f`, `g`, `op` for functions / operators.

### 1.1 Types

```bnf
τ ::= Scalar | Bool | Int | Float           -- ground scalar types
    | Tensor[σ]                              -- tensor with symbolic shape σ
    | { l₁: τ₁, ..., lₙ: τₙ }                -- record (TS-flavored)
    | τ₁ × ... × τₙ                          -- tuple
    | τ₁ → τ₂                                -- function
    | Sim τ                                  -- simulator monad
    | Op[τ_in → τ_out]                       -- operator carrying params; in / out types
    | !τ                                     -- shareable (non-linear) annotation
```

### 1.2 Shape expressions

Shapes are drawn from bunsen's `DimExpr` algebra:

```bnf
σ ::= n                                      -- literal natural
    | s                                      -- shape variable (named axis)
    | σ + σ | σ - σ | σ * σ | σ ^ n          -- algebraic combinations
    | [γ₁, ..., γₙ]                          -- shape tuple (a sequence of shape-group items)

γ ::= σ                                      -- a single axis (literal, variable, or algebraic)
    | ...                                    -- rank-wildcard: zero or more unconstrained axes
    | (S: γ₁, ..., γₖ)                       -- named shape group: binds S to the contiguous item run
    | S                                      -- shape-group reference (congruence by name reuse)
```

Examples:

- `Tensor[N]`             — rank-1 tensor of length `N`
- `Tensor[H, W, VY=3, VX=3]` — rank-4 with two free axes (`H`, `W`) and two pinned (`VY=3`, `VX=3`)
- `Tensor[m, n]`          — rank-2 with free axes `m`, `n`
- `Tensor[h_wins * window, w_wins * window, C]` — algebraic composition

#### 1.2.1 Named shape groups (shape congruence of unknown rank)

A **named shape group** `(S: ...)` gives a name to a *contiguous run of axes* inside a shape — **without committing to its rank or its individual dims**. It reads as *"the shape pattern `...`, named `S`"*. The name is then reused elsewhere in the same signature to assert that two shapes are **congruent** over that run.

- `Tensor[(S: ...)]`        — a tensor whose entire shape is the group `S` (rank unknown). Reusing `S` in another `Tensor[(S: ...)]` in the same signature asserts the two are the same shape.
- `Tensor[(S: a, ...), b]`  — a named group `S` (a leading axis `a` followed by any number of further axes), then a trailing dim `b`. The shape is the concatenation `[a, …, b]`; the leading run is named `S`.
- Once `S` is bound, a bare `S` (or `(S: ...)`) elsewhere in the signature **references** it: `f :: Tensor[(S: ...)] -> Tensor[(S: ...)] -> Tensor[S]` constrains all three shapes to one common `S`.

The rank-wildcard `...` matches zero or more axes; a group may mix pinned axes and a wildcard (`(S: a, ...)`), or be a pure wildcard (`(S: ...)`).

**Why this exists — the `Tensor[N]`-as-same-shape anti-pattern.** A single shape *variable* `σ` already expresses "same whole shape, any rank" (`axpy :: Scalar → Tensor[σ] → Tensor[σ] → Tensor[σ]`). Use `σ` when the whole shape is shared. Named groups add two things `σ` cannot: (i) naming a *partial* run so the shared and the free parts of a shape are distinguished (`Tensor[(S: ...), k]` — congruent leading block `S`, free trailing `k`); and (ii) a same-shape assertion that is **visibly rank-agnostic**. Do **not** reach for a bare concrete axis like `Tensor[N]` to mean "same shape as the other operand" — `Tensor[N]` denotes a **rank-1 tensor of length `N`** and silently pins the operands to one dimension. When the intent is congruence-of-unknown-rank, write `Tensor[(S: ...)]` (or reuse `σ`); reserve `Tensor[N]` for genuinely rank-1 vectors (e.g. a flat dof-vector of length `N`).

#### 1.2.2 Operator shapes — domain and range groups

A linear operator whose **domain shape differs from its range shape** names *two* groups: a range group `R` and a domain group `D`. Written **range-first**, matching the matrix convention (an `M×N` matrix maps a length-`N` domain to a length-`M` range):

- `LinOp[(R: ...), (D: ...)]` — an operator from domain shape `D` to range shape `R`, both of unknown rank.
- Applied: `apply_linop :: LinOp[(R: ...), (D: ...)] -> Tensor[(D: ...)] -> Tensor[R]` — the operand must be congruent to the domain group `D`; the result is the range group `R`.
- A square / endomorphic operator reuses one group: `LinOp[(S: ...), (S: ...)]` (e.g. a preconditioner or a symmetric system matrix, domain ≡ range).

This generalizes the rank-1 spelling `LinearOperator[M, N]` (where `M`, `N` are genuine flat dof-vector lengths) to the rank-agnostic case. At **L1/L0**, Palace operators act on flat dof-vectors and the concrete `LinearOperator[M, N]` / `Tensor[N]` rank-1 spelling is faithful — keep it there; the `LinOp[(R: ...), (D: ...)]` form is the L4/L3/L2 calculus rendering.

### 1.3 Terms

```bnf
e ::= x                                      -- variable
    | c                                      -- constant / literal
    | λ(x: τ). e                             -- abstraction
    | e₁ e₂                                  -- application
    | let x = e₁ in e₂                       -- let-binding
    | let { l₁, ..., lₙ } = e₁ in e₂         -- destructure-let
    | let { l₁, ..., lₖ, ...r } = e₁ in e₂   -- destructure-with-rest
    | { l₁: e₁, ..., lₙ: eₙ }                -- record literal
    | { ...e₀, lᵢ: eᵢ, ..., lⱼ: eⱼ }         -- record spread / update
    | e.l                                    -- field access
    | (e₁, ..., eₙ)                          -- tuple literal
    | πᵢ e                                   -- tuple projection
    | if e₀ then e₁ else e₂                  -- conditional
    | op(e₁, ..., eₙ)                        -- primitive operator application
    | apply A e                              -- operator application
    | return e                               -- monadic return (Sim)
    | e₁ >>= e₂                              -- monadic bind
    | do { s₁; ...; sₙ; e }                  -- do-notation block
    | get | put e | modify e                 -- state effects (Sim)
    | while_loop init cond step              -- pure tail-recursive loop
```

A `do`-block statement `s` is either `x ← e` (monadic bind), `let x = e` (pure binding), or just `e` (side-effect-only call returning `Sim ()`).

## 2. Ownership categories

The calculus distinguishes **three categories of value** at the syntactic level. This is the core of "ownership and update-operation extraction":

1. **Simulator state** — values threaded through the `Sim` monad. Accessed via `get` / `put` / `modify`. Treated as linear in the type system: a `Sim` action takes the current state and produces the next state; aliasing is impossible because the old state is shadowed.

2. **Operator internal parameters** — values closed over inside an `Op[_]`. Shareable (`!τ`); read-only from the operator's perspective; do not evolve during a solve. Examples: matrix entries, preconditioner factorizations, mesh/basis tables, lattice tables, time-step constants.

3. **Ephemeral intermediates** — values bound inside a `let` or `do` block. Their scope is local; they do not participate in sim-state evolution or operator closure. Examples: residual computed mid-iteration, search direction in CG, predicted intermediate in a multi-step time integrator.

The type system uses **linear / affine annotations** sparingly, only to enforce the sim-state-vs-operator-param distinction. We do **not** track linearity at the tensor level — every tensor is immutable, so aliasing of tensor values is harmless. Linearity is about *which slot in the simulator state owns the canonical current value*.

## 3. Reduction rules (small-step)

Standard rules, with the bookkeeping that makes the calculus a useful target for L3↔L4 correspondence.

### 3.1 Core λ-calculus

$$
\begin{aligned}
(\lambda(x:\tau).\, e)\ v &\;\to\; e[v/x] & \text{(β)} \\
\textsf{let}\ x = v\ \textsf{in}\ e &\;\to\; e[v/x] & \text{(let)}
\end{aligned}
$$

### 3.2 Records

$$
\begin{aligned}
\{l_1\!:\!v_1,\dots,l_n\!:\!v_n\}.l_k &\;\to\; v_k & \text{(proj)} \\
\textsf{let}\ \{l_1,\dots,l_n\} = \{l_1\!:\!v_1,\dots,l_n\!:\!v_n\}\ \textsf{in}\ e &\;\to\; e[v_1/l_1,\dots,v_n/l_n] & \text{(destr)} \\
\{\dots\{l_1\!:\!v_1,\dots,l_n\!:\!v_n\},\ l_k\!:\!w\} &\;\to\; \{l_1\!:\!v_1,\dots,l_k\!:\!w,\dots,l_n\!:\!v_n\} & \text{(spread)}
\end{aligned}
$$

### 3.3 Monad laws

$$
\begin{aligned}
\textsf{return}\ v \,\texttt{>>=}\, f &\;\to\; f\ v & \text{(left identity)} \\
m \,\texttt{>>=}\, \textsf{return} &\;\to\; m & \text{(right identity)} \\
(m \,\texttt{>>=}\, f) \,\texttt{>>=}\, g &\;\to\; m \,\texttt{>>=}\, (\lambda x.\, f\ x \,\texttt{>>=}\, g) & \text{(associativity)}
\end{aligned}
$$

### 3.4 State effects

$$
\begin{aligned}
\textsf{do}\ \{ x \leftarrow \textsf{get};\ \textsf{put}\ f(x);\ \textsf{return}\ () \} &\;\to\; \textsf{modify}\ f \\
\textsf{modify}\ (f \circ g) &\;\to\; \textsf{do}\ \{\textsf{modify}\ g;\ \textsf{modify}\ f\}
\end{aligned}
$$

### 3.5 Operator application

Operators carry params; `apply A x` reduces by substituting the operator's body with its closed-over params and the argument.

$$
\textsf{apply}\ (\textsf{op-with-params}\ p,\ \lambda x.\,e)\ v \;\to\; e[p/\textsf{params},\ v/x]
$$

### 3.6 Primitive δ-rules

Each primitive (`axpy`, `dot`, `matvec`, `conv`, `unfold`, `reduce`, etc.) has its own δ-rule giving its action on values. These are deferred to the `concepts/` library — primitive semantics are defined there, not here. The calculus assumes each primitive comes with a δ-rule that the Critic can check against a reference implementation (most directly, against bunsen's `kits::sims` and `ops` modules).

### 3.7 Loops (`iterate_while`)

The step of an iteration may produce **per-step output extras** alongside the next state; the iteration collects them into a trajectory record. The general form (v0.3):

```
iterate_while
  : α
  → (α → Bool)
  → (α → { state: α, ...extras })
  → { final_state: α, trajectory: [{ ...extras }] }
```

`iterate_while init cont step` reads: "starting from `init`, while `cont` holds of the current state, take a step that produces the next state plus any extras." Small-step semantics:

$$
\begin{aligned}
\textsf{iterate\_while}\ a\ p\ f &\;\to\; \textsf{if}\ p(a) \\
&\quad \textsf{then}\ \textsf{let}\ \{\textsf{state}: a',\ \dots e\} = f(a)\ \textsf{in} \\
&\quad\quad \textsf{let}\ \{\textsf{final\_state},\ \textsf{trajectory}\} = \textsf{iterate\_while}\ a'\ p\ f\ \textsf{in} \\
&\quad\quad \{\textsf{final\_state},\ \textsf{trajectory}: [\{\dots e\}] \mathop{++} \textsf{trajectory}\} \\
&\quad \textsf{else}\ \{\textsf{final\_state}: a,\ \textsf{trajectory}: [\,]\,\}
\end{aligned}
$$

By §3.8 (demand-driven pruning, below), if no consumer reads `trajectory`, the per-step extras are *never computed* — only the threaded state advances. Consumers that read `trajectory` materialize the per-step records.

For the common case where the step has no extras (returns only the next state), a sugared form:

```
iterate_while_pure : α → (α → Bool) → (α → α) → α
```

is the special case where `extras = ()` and the trajectory is always empty. Definitionally `iterate_while_pure init cont step = (iterate_while init cont (\a -> { state: step a })).final_state`.

Total correctness depends on the predicate eventually becoming false; the spec records the convergence argument as part of the slice that uses the loop (typically tied to an algorithmic convergence guarantee or a bounded `maxIter` clause folded into the predicate).

### 3.8 Demand-driven evaluation and pruning

The L4 calculus is a **graph-evaluation language**. Operators and aggregate operations produce records of outputs; their evaluation is **demand-driven**. At evaluation time (graph solve time), only outputs that some root consumer transitively reaches are computed. Unused outputs are **pruned** — they never materialize.

Operationally, this is captured by an "observed" relation on expressions. Root observation comes from:

- The return value of `runSim` (when `Sim` is used at orchestration level).
- The result expression of a top-level program.
- Explicit observation channels (file writes, external sinks — these are out of scope here; see §8).

Observation propagates structurally:

- If a binding `let { l_i: x_i }_i = e in body` has `body` observe `x_k`, then `l_k` is observed in `e`'s output record.
- If `body` does not observe `x_k` (uses `_` placeholder, or never references `x_k`), then `l_k` is not observed in `e`'s output record.

The **pruning rule** is an equivalence in the operational semantics:

$$
\frac{
  \text{output } l_k \text{ of } \textsf{op} \text{ is not observed}
}{
  \textsf{let}\ \{l_1: x_1, \dots, l_k: \_, \dots, l_n: x_n\} = \textsf{op}(\bar{e})\ \textsf{in}\ \textsf{body}
  \;\equiv\;
  \textsf{let}\ \{l_i: x_i\}_{i \neq k} = \textsf{op}_{\neg k}(\bar{e})\ \textsf{in}\ \textsf{body}
}
$$

where $\textsf{op}_{\neg k}$ is the subgraph of $\textsf{op}$ that does not compute the $l_k$-output (formally: the dependency-closure of the remaining outputs over $\textsf{op}$'s body). This is **dead-code elimination at the graph level**.

This rule is **the** mechanism for what other systems would express via:

- **Writer monads / effect channels** for logging or metric accumulation.
- **Phase-configuration flags** ("if verbose, also compute residual norm").
- **Conditional branches** around optional metric computation.

In L4 none of those exist as separate concepts: operators *unconditionally* declare all outputs as record fields; consumers read what they need; pruning handles the rest. An algorithm written once works correctly whether or not its optional outputs are consumed.

Implications for the calculus:

- Operators returning structured records are the norm, not the exception.
- The simulator's coordination layer does **not** need a Writer effect to thread "metrics" alongside "state" — metrics are just additional outputs of the same step, collected by `iterate_while`'s trajectory, pruned when unobserved.
- `Sim` recedes to genuine orchestration concerns (file I/O, multi-stage workflows, RNG threading) — *not* per-algorithm state evolution, which `iterate_while_pure` already expresses purely.

## 4. Type and shape rules

Standard typed-λ form. Judgment `Γ ⊢ e : τ`. Selected rules below; full table is mechanical.

```
Γ, x: τ ⊢ x : τ                            (var)

Γ ⊢ e₁ : τ₁ → τ₂    Γ ⊢ e₂ : τ₁
─────────────────────────────────          (app)
        Γ ⊢ e₁ e₂ : τ₂

Γ ⊢ e_i : τ_i  for each i
────────────────────────────────────────   (record)
Γ ⊢ { l₁: e₁, ..., lₙ: eₙ } : { l₁: τ₁, ..., lₙ: τₙ }

Γ ⊢ e : { l₁: τ₁, ..., lₙ: τₙ }    Γ ⊢ w : τ_k
─────────────────────────────────────────────────  (spread)
Γ ⊢ { ...e, l_k: w } : { l₁: τ₁, ..., lₙ: τₙ }

Γ ⊢ e : τ
──────────────────────                     (return)
Γ ⊢ return e : Sim τ

Γ ⊢ m : Sim α    Γ, x: α ⊢ k : Sim β
─────────────────────────────────────       (bind)
Γ ⊢ m >>= λx. k : Sim β
```

### 4.1 Shape contracts on primitives

Primitive type signatures carry symbolic shapes:

```
axpy         : Scalar → Tensor[σ] → Tensor[σ] → Tensor[σ]
dot          : Tensor[σ] → Tensor[σ] → Scalar
matvec       : Tensor[m, n] → Tensor[n] → Tensor[m]
outer        : Tensor[m] → Tensor[n] → Tensor[m, n]
reduce       : Tensor[..., σ] → Tensor[...]            -- reduces a labeled axis
unfold       : Tensor[σ] → (axis, size, stride) → Tensor[..., size]
conv         : Tensor[N, C_in, σ_in] → Tensor[C_out, C_in, σ_k] → Tensor[N, C_out, σ_out]
broadcast_to : (target_shape: [σ_1, …, σ_n]) → Tensor[σ_a] → Tensor[σ_1, …, σ_n]
                                          -- target shape must be a broadcast extension of σ_a;
                                          -- shape-side-condition resolved by the DimExpr solver
```

Where shapes match symbolically (`σ` on both inputs of `axpy`), they must be syntactically identical *modulo the* `DimExpr` *equational theory*. Where shapes are related (`m, n` of `matvec`), the relation is stated in the signature. Where only a *partial run* of axes must agree across operands of unknown rank, name it with a shape group (§1.2.1) and reuse the name: every occurrence of a group `S` in a signature must resolve to one congruent axis-run under the same `DimExpr` theory. A named group is the rank-agnostic same-shape contract; a bare concrete axis (`Tensor[N]`) is **not** — it is a rank-1 commitment.

### 4.2 Linear annotations for sim-state ownership

Sim-state slots are linear — they can be read once and must be re-bound. The discipline is encoded by the `Sim` monad's `get` / `put` semantics rather than by per-tensor linearity annotations:

```
get : Sim S
put : S → Sim ()
modify : (S → S) → Sim ()
```

A `Sim S` action consumes the implicit input state and produces the output state. Aliasing of "the canonical current state vector" is structurally impossible because there is exactly one state slot in scope at any point in a `do` block.

Operator parameters carry `!` (shareable) — they can be read repeatedly without consumption. Inside `Op[_]`, all closed-over data is `!`-tagged by construction.

## 5. Algebraic equational laws

Many primitive operators satisfy useful equations. These are the rewriting rules the Synthesizer / Critic appeal to when arguing L3→L4 correspondence:

- `axpy α v 0 = α • v`     (axpy with zero accumulator is just scaling)
- `axpy 0 v y = y`         (zero scaling is identity)
- `dot v w = dot w v`      (symmetry)
- `dot (axpy α v w) x = α * dot v x + dot w x`     (bilinearity)
- `matvec A (αv) = α • matvec A v`                 (linearity in vector)
- `matvec (A + B) v = matvec A v + matvec B v`     (linearity in matrix)
- `(matvec A) ∘ (matvec B) = matvec (A∘B)`         (composition)

Full library lives in `concepts/`. The Critic relies on these to walk L3-form-to-L4-form reduction chains.

## 6. Worked example: LBM streaming + collision (v0.3)

Pulled from `bunsen/crates/bunsen/src/kits/sims/lbm/d2q9/`. Three ownership categories visible. This is the v0.3 rewrite — v0.2 used a `Sim LbmState` monad for the step; v0.3's pruning-driven model makes the step a pure `LbmState → LbmState` function. The trajectory of any per-step extras (here: nothing — LBM has no monitoring metrics in this minimal example) is pruned automatically.

### 6.1 Types

```typescript
// Sim state — only the canonical evolving state.
// Macroscopics (density, velocity) are derived views, not stored.
type LbmState = {
  dist: Tensor[H, W, VY=3, VX=3],   // population distribution
  step: Int,                        // step counter
}

// Closed-over data for operators. The `!` annotation marks these as
// shareable (non-linear) — read repeatedly, never consumed.
type LbmTables = !{
  e:       Tensor[VY=3, VX=3, 2],   // discrete velocity vectors
  weights: Tensor[VY=3, VX=3],      // equilibrium weights w_v
  c2:      Scalar,                  // sound-speed-squared
}

type Boundary = !{
  solid_mask: Tensor[H, W, Bool],
}
```

### 6.2 Operator constructors

Each step-level operation is bundled as an `Op` carrying its closed-over params, constructed once at simulator setup. The dataflow signature (input → output) appears in the `Op` type:

```haskell
-- No internal params: a pure shift. One stream operator instance is enough.
Stream :: Op[Tensor[H, W, VY=3, VX=3] → Tensor[H, W, VY=3, VX=3]]

-- Constructed once per setup with (tables, τ) closed in. Returns dist + the
-- macroscopics computed during collision, so callers don't recompute them
-- (v0.2 resolves P-1: macroscopics are returned, not cached in state).
Bgk :: !LbmTables → Scalar → Op[Tensor[H, W, VY=3, VX=3] → {
  dist:     Tensor[H, W, VY=3, VX=3],
  density:  Tensor[H, W],
  velocity: Tensor[H, W, 2],
}]

-- Constructed once per setup with boundary closed in (v0.2 resolves P-2:
-- boundary becomes an operator-internal param, not a step-level argument).
Reflect :: !Boundary → Op[Tensor[H, W, VY=3, VX=3] → Tensor[H, W, VY=3, VX=3]]
```

The L3-level primitive bodies that these operators close over (`stream`, `bgk_collision`, `reflect`, `sum_velocities`, `momentum`, `equilibrium`, …) live in `concepts/`. The calculus references them by name and trusts their δ-rules; the spec doesn't redefine them here.

### 6.3 L4 step in the calculus (v0.3, pure)

Given pre-constructed operators (`streamOp`, `bgkOp`, `reflectOp`), one LBM step is a **pure function** `LbmState → LbmState`:

```typescript
lbm_step :: Op[Tensor[..] → Tensor[..]]
         -> Op[Tensor[..] → { dist: Tensor[..], density: Tensor[H, W], velocity: Tensor[H, W, 2] }]
         -> Op[Tensor[..] → Tensor[..]]
         -> LbmState
         -> LbmState
lbm_step streamOp bgkOp reflectOp s =
  let streamed = apply streamOp s.dist in
  let { dist: collided, density: _, velocity: _ } = apply bgkOp streamed in
  let dist_next = apply reflectOp collided in
  { ...s, dist: dist_next, step: s.step + 1 }
```

The destructure `{ dist: collided, density: _, velocity: _ }` makes it explicit that this step *does not consume* the macroscopics. Per the **demand-driven pruning rule** of §3.8, `bgkOp` is rewritten to its `dist`-only subgraph at solve time — `density` and `velocity` are *never computed* here. A different step — say, one that logs the density's L² norm for monitoring, or terminates when velocity goes below a threshold — would destructure those fields and use them, automatically demanding their computation. The same `bgkOp` definition serves both cases; only consumer demand differs. No phase-config flags. No conditional branches. The calculus makes the dataflow visible at the syntactic level and the pruning happens automatically.

A full run wires the operator instances once and iterates the step purely:

```typescript
run_lbm :: !LbmTables -> Scalar -> !Boundary -> Int -> LbmState -> LbmState
run_lbm tables tau boundary maxSteps initial =
  let streamOp  = Stream in
  let bgkOp     = Bgk tables tau in
  let reflectOp = Reflect boundary in
  iterate_while_pure initial
    (\s -> s.step < maxSteps)
    (\s -> lbm_step streamOp bgkOp reflectOp s)
```

No `Sim`; no `runSim`. The whole algorithm is pure functions over records. (If a real simulator wraps this — reading mesh from disk, writing snapshots to file — *that* code uses `Sim`. The algorithm itself doesn't need it.)

### 6.4 Ownership analysis

- `Stream`, `Bgk tables tau`, `Reflect boundary`: `Op`-typed values, constructed once at setup with their internal params closed in. **Operator instances** — the "compiled" form of the algorithm's verbs.
- `tables`, `tau`, `boundary`: `!`-tagged; flow into operator constructors; never themselves evolve. **Operator internal parameters** at the syntactic level.
- `s : LbmState`: the iteration's threaded state. `iterate_while_pure` plumbs exactly one current state per step; no aliasing.
- `streamed`, `collided`, `dist_next`, `density: _`, `velocity: _`: ephemeral intermediates inside `lbm_step`. No special annotation needed — scope governs. Destructured-but-discarded values use `_` as in TypeScript / Rust; per §3.8 these are pruned at solve time.

### 6.5 L3 ↔ L4 correspondence

L3 form (paraphrased from bunsen's `lbm/d2q9/mod.rs:test_debug_flow_loss`):

```rust
let mut current: Tensor<B, 4> = dist_t0.clone();
for t_idx in 1..=k {
    let stream_phase = outflow_clipping_stream(current.clone());
    let thermal_phase = bgk_collision_with_spherical_reflection(
        stream_phase, solid_mask.clone(),
        RelaxationParam::Tau(1.0), None, &lbm_tables,
    );
    current = thermal_phase;
}
```

Correspondence steps:

1. The L3 mutable `current` corresponds to `s.dist` in L4, threaded as a record field through `iterate_while_pure`'s accumulator. The L3 mutation `current = thermal_phase` becomes the L4 record-spread `{ ...s, dist: dist_next }` returned by the step.
2. The L3 cloning `current.clone()` is a no-op in L4 — tensors are immutable values; there is nothing to clone.
3. The L3 reference-passing `&lbm_tables` and `solid_mask.clone()` correspond to operator closure in L4: `&` becomes `!` shareability; `clone()` evaporates; the references are closed into `Bgk tables tau` and `Reflect boundary` at construction time.
4. The L3 call `bgk_collision_with_spherical_reflection(stream_phase, …)` *fuses* collision and reflection (an L1→L2 transparent perf trick — see CLAUDE.md *Optimization tricks vs. base algebra*). The L4 form takes the **unfolded** version as canonical: `apply reflectOp (... apply bgkOp ...)`.
5. The L3 `for t_idx in 1..=k` is bounded iteration; L4 uses `iterate_while_pure` with `s.step < maxSteps` as the continuation predicate, encoding the `k`-step bound inside the state and the predicate.

Reduction chain: β, let-substitution, the spread rule, monadic associativity (to flatten the do-block), the `apply Op v` substitution rule, and the δ-rules for each primitive. The `bgk_collision` δ-rule expands into its constituent operations (`sum_velocities`, `momentum`, `equilibrium`, axpy-style relaxation) — see the `bgk_collision` concept entry once it is written. Each step in the chain is mechanical; no exotic reductions are needed.

## 7. Iteration log

### v0.3 — decisions made

**Demand-driven evaluation and pruning added (§3.8).** L4 is formally a graph-evaluation language. Operators produce records of outputs; only those that some root consumer transitively reaches are computed; the rest are pruned at solve time. **This replaces the "effects beyond state" open question from v0.2** — instead of adding a Writer-style effect channel for residual logging / monitoring / metrics, optional outputs become regular record fields, and demand pruning handles whether they're computed.

The CG slice's v0.1 push-back ("residual-norm logging forces a Writer effect") is **resolved by this**: `cg_step` returns `{ state, residual_norm }`; `iterate_while` collects per-step extras into a trajectory; a caller reading `residual_history` materializes the residual norms; a caller reading only `final_state` prunes them.

**`iterate_while` generalized (§3.7).** The step now returns `{ state, ...extras }`; the iteration produces `{ final_state, trajectory: [{ ...extras }] }`. `iterate_while_pure` sugar covers the no-extras case.

**`Sim` recedes.** With pruning + extras-bearing iteration, `Sim` is no longer needed for per-algorithm state evolution or for "place to put metrics." Per-algorithm code is **pure** functions over records. `Sim` is reserved for genuine top-level orchestration concerns: file I/O, multi-stage workflows, RNG threading. Algorithm bodies (CG, GMRES, LBM step, eigensolver step) are pure.

### v0.2 — decisions made

**P-1 resolved (state shape).** v0.1 cached `density` and `velocity` in `LbmState`, forcing recomputation each step. v0.2 drops them: `LbmState` carries only `dist` and `step`; macroscopics are *derived views* produced by `bgkOp` as part of its return record, and consumed (or discarded) by the step's destructure pattern. This makes the dataflow explicit and removes the recomputation problem.

**P-2 resolved (operator currying).** v0.1 threaded `!Boundary` (and `!LbmTables`, `τ`) through every step call. v0.2 introduces the operator-with-closed-params pattern: `Stream`, `Bgk tables tau`, `Reflect boundary` are constructed once at simulator setup, closing their params in; the step applies them via `apply opInst arg`. This is the standard operator-with-weights pattern from PL theory and operator-algebra literature.

**P-3 resolved (no Reader monad needed).** With operators-carrying-closed-params (P-2), the shared-param concern partly evaporates — params are closed into operator instances at construction time, not threaded by the monad. The `Sim` monad threads only state. A Reader layer can be added if a future slice surfaces a real need (e.g., deeply-nested sub-computations that all need the same env), but the LBM and projected CG slices don't.

**P-4 resolved (explicit broadcasting).** v0.2 commits to explicit `broadcast_to [shape] e` rather than numpy-style implicit broadcasting. Adds slight noise; wins on dataflow clarity. The `broadcast_to` primitive is added to §4.1.

### v0.2 — additions to the calculus

- `iterate_while` formalized in §3.7 with small-step semantics (standard fixed-point unfolding).
- `broadcast_to` added to the primitive signatures in §4.1.
- Operator constructors written as curried functions returning `Op[τ_in → τ_out]`: e.g., `Bgk :: !LbmTables → Scalar → Op[…]`. This isn't a calculus extension, just a convention surfaced by the v0.2 example.

## 8. Remaining open questions

- **External observation channels** (file I/O, stdout, on-disk snapshots): pruning handles in-graph optionality, but a runtime needs *some* way to mark certain consumers as "always observed." Likely modeled as `Sim`-level orchestration with explicit `write_to_file` / `emit_event` ops that always demand their inputs. Not yet drafted.
- **Sub-jaxprs / higher-order primitives.** JAX's `cond` and `while_loop` embed sub-jaxprs as parameters (program-as-data). Our `iterate_while` takes lambdas. Whether the calculus also admits the program-as-data form (free-monad style) for cases like `cond branches` is open. May matter for control-flow that gets transformed (vmap-like patterns).
- **Primitive closure.** Which operators are primitives (have δ-rules) vs. composites (defined in terms of primitives) is not pinned. The `concepts/` library grows this on demand.
- **Shape solving formalization.** Symbolic shape equations are solved by bunsen's `DimExpr` solver. Whether to formalize this in L4 (as side-conditions in type rules) or treat it as an external check is open. Likely external, with type judgments annotated by shape-side-conditions.
- **Pruning of operator-internal data.** The §3.8 pruning rule is stated for operator outputs. Whether it extends *inside* operator bodies — pruning sub-expressions whose values feed only to outputs that are themselves pruned — needs formalizing. This is standard graph DCE, but worth pinning the rule explicitly.

## 9. Next steps

1. Exercise the calculus on **one Palace slice** — CG is the obvious first candidate. It has iterative-solver structure, convergence predicates, and multiple state fields, all of which test L4's loop construct and monadic facilities. The CG slice will likely force a v0.3 around effects (residual-norm monitoring).
2. Surface effects-beyond-state demand and design a `Writer` / `Eff` layer if the CG slice forces it.
3. Build the first `concepts/` entries — at minimum `axpy`, `dot`, `matvec` for CG; possibly `stream`, `bgk_collision`, `reflect` once an LBM-style slice is needed.

## Working Notes

- **v0.3** added demand-driven pruning (§3.8), generalized `iterate_while` to carry per-step extras (§3.7), and *displaced* the v0.2 "effects-beyond-state" open question: optional outputs become record fields, demand pruning handles whether they're computed, no separate effect channel needed. `Sim` recedes from per-algorithm code; algorithms are pure.
- **v0.2** resolved P-1 (state shape), P-2 (operator currying), P-3 (no Reader needed), P-4 (explicit broadcasting). The worked LBM example was rewritten accordingly.
- Sub-jaxprs (embedded-program-as-value) deferred.
- Shape-solving formalization deferred.
- The `iterate_while` semantics are total only when the predicate is eventually false — algorithmic correctness obligation on the slice that uses the loop, not enforced by the calculus.
- `runSim :: Sim S α → S → S` is named as the state-only eliminator but not formally defined. Will be tightened when an orchestration-level use (multi-stage simulation, file I/O) actually surfaces — purely algorithmic slices don't force it.
- An operator's body `Op[τ_in → τ_out]` is described informally as "closure with params + body lambda" but not given an explicit term-level form in §1.3. Tighten when needed — possibly `Op { params; \x. e }` or similar.
- The §3.8 pruning rule is stated for operator outputs at the binding level; its effect on operator-internal sub-expressions ("standard graph DCE") is implicit. Pin formally when needed.
