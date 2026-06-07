---
layer: L2
operator: correction_step
firmness: firm
# Graded-stack scheme: this L2 step-kernel combinator composes two firm L1 primitives
# (apply_linop, axpby) — both depends-on (rank 3). It is the shared per-sweep body the
# jacobi-smoother / chebyshev-iteration L2 entries specialize (those cite it as the
# combinator-as-entry; the edge is reference — they are specializations choosing B, not
# build dependencies of this combinator). All depends-on targets firm (rank 3); this node
# firm (rank 3); well-foundedness holds.
rank: firm
edges:
  depends-on:
    - L1/apply_linop          # the operator action A·y (and, when B is itself an apply, B·r)
    - L1/axpby                # the residual x − A·y and the y + correction add
  reference:
    - L2/jacobi-smoother      # specialization: B = ω·D⁻¹ (non-iterated, degree-0)
    - L2/chebyshev-iteration  # specialization: B = p_order(D⁻¹A) (the polynomial correction)
    - L1/divfree-projector    # borderline NOTE (NOT a core instance; A = I complementary projector)
    - concepts/sequential-obstruction
    - concepts/constructed-operators
    - concepts/variant-absorption
variant_axes:
  parametric:
    - B-slot (the preconditioner LinOp; ω·D⁻¹ Jacobi | p_order(D⁻¹A) Chebyshev | conjugated T·B'·Tᵀ distributive/coarse-grid)
    - initial-guess (zero-guess degenerate-residual absorption r = x, y = 0 | nonzero-guess full r = x − A·y)
  absorbed:
    - element-type (real | complex; collapsed into the operand vectors / the B closure)
    - operator-representation (collapsed into A and B at setup)
---

# correction_step

The **preconditioned residual-correction step** `y + B·(x − A·y)` at the fusion-rotation
layer: given a system operator `A`, a preconditioner `B`, a right-hand side `x`, and a current
iterate `y`, compute the corrected iterate `y' = y + B·(x − A·y)`. This is **the single
per-sweep body shared across Palace's entire smoother + geometric-multigrid family** — the
GMG V-cycle pre/post-smooth, the distributive (Hiptmair) relaxation sweep, the Chebyshev
smoother sweep, and the Jacobi preconditioner action are all this combinator with a different
choice of `B`. Palace names the contract **verbatim** in its own source comments
(`palace/linalg/gmg.cpp:176` "compute Y <- Y + B (X - A Y)";
`palace/linalg/distrelaxation.cpp:104` "y = y + B (x - A y)";
`palace/linalg/chebyshev.cpp:193`,`:264` "Apply smoother: y = y + p(A) (x - A y)").

`correction_step` is a **step-kernel combinator** (the entry; sibling to
[`krylov-step`](./krylov-step.md) and [`chebyshev-iteration`](./chebyshev-iteration.md) in the
Step-kernels cohort). It is the **combinator-as-entry**: the smoothers are specializations that
choose `B`, NOT same-named floors mirrored beside it (the 2026-06-01 vocabulary-shift redirect,
`METHODOLOGY-REDIRECT.md` §1d). The outer `pc_it` smoothing sweep / the V-cycle recursion are
the **consumer's** `iterate_while` fold (`distrelaxation.cpp:102` `for (it < pc_it)`;
`gmg.cpp:172` `VCycle`), NOT folded into this kernel — `correction_step` is the per-sweep body,
the fold is the driver above it (the same kernel-plus-driver split `krylov-step` (kernel) /
L4 `iterate_while` (driver) establishes).

## Context

L2 is the fusion-rotation layer (`book/src/L2/index.md`): operations are written as
compositions of base tensor / operator primitives with HPC/SIMD fusion unfolded back into the
base algebra. `correction_step` is the base-algebra reading of the residual-correction body that
recurs, *verbatim and named*, across the smoother family. Mining it as a first-class combinator
is exactly the **conciseness-driven in-layer combinator** the redirect's vocabulary-shift model
calls for (`book/src/semantics/index.md` §0.1; redirect §combinator-primary): the smoother
entries no longer each spell out "compute the residual, precondition it, add it back" — they
state which `B` they plug into the shared step.

The c121 D6 combinator-miner dispatch
(`reports/2026-06-07T054924Z-combinator-miner-kernel-shared-substrate`) surfaced the pattern
across the GMG / distributive-relaxation / Chebyshev / Jacobi sites and proposed the rough-in
dep-map row (`book/src/L2/index.md:96`). This dispatch firms it.

**Over-unification guards** (the explicit do-NOT-subsume boundary, carried from the c121 row):

- The **bare preconditioner apply** `Y = B·X` (e.g. the Jacobi `op.dinv ⊙ x` action read in
  isolation, [`jacobi-smoother`](./jacobi-smoother.md)) is NOT a `correction_step` — there is
  no residual, no `A`, no add-back. `correction_step` is the *step that consumes* `B` as its
  preconditioner slot; the bare `B` apply is `correction_step`'s argument, not an instance.
- The **Krylov shift-invert step** `(K − σM)⁻¹·M·v` (the [`eigsolve`](./eigsolve.md) per-step
  body) is NOT a `correction_step` — it is an inverted-operator application against a spectral
  transform, with no `x − A·y` residual structure.
- The **libCEED `GᵀBᵀDBG` quadrature contraction** (the matrix-free FE operator-apply
  substrate, `L1/libceed-quadrature-kernel-impl`) is NOT a `correction_step` — it is the
  *realization of an `apply_linop`* (the `A·y` operand of a correction step), one layer of
  substrate below this combinator.
- The **`divfree-projector`** body `y + P.Grad·K⁻¹(Z(P.WeakDiv·y))` is a **borderline**
  case (see §Borderline below): it shares the `y + correction` skeleton but the correction is
  a complementary projection of `y` itself (the `A = I`, no-external-`x` degenerate), not a
  preconditioned residual against an external RHS. Annotated as a borderline NOTE, **kept out
  of the core-instance roster**.

## Signature

    correction_step
      :: (A: LinOp[(S: ...), $S], B: LinOp[(S: ...), $S], x: Tensor[(S: ...)], y: Tensor[$S])
         -> Tensor[$S]
    correction_step A B x y = axpby 1 y 1 (apply_linop B (axpby 1 x (-1) (apply_linop A y)))
                            = y + B·(x − A·y)

Shape contract (bunsen-style named axes; the field shape group `S` and the square-operator
form `LinOp[(S: ...), $S]` follow the named-shape-group convention of
[`semantics`](../semantics/index.md) §1.2.1–§1.2.2 — `A`, `B` are square on the field shape
group `S`; positional values, no monadic effect, no destination buffer):

- **`A`** — `LinOp[(S: ...), $S]` — the system operator (the matrix whose linear system
  `A·u = x` is being smoothed/solved). Square on the field shape group `S`. Applied exactly
  once per step, to the current iterate `y`, producing `A·y`.
- **`B`** — `LinOp[(S: ...), $S]` — the **preconditioner slot** (the approximate inverse
  `B ≈ A⁻¹`). Square on `S`. The slot that the smoother family specializes (see §Specializations).
  Opaque at the combinator level: `B` may be a damped inverse diagonal (Jacobi), a polynomial in
  `D⁻¹A` (Chebyshev), or a conjugated auxiliary-space correction `T·B'·Tᵀ` (distributive /
  coarse-grid) — the combinator sees only the LinOp interface.
- **`x`** — `Tensor[(S: ...)]` — the right-hand side (the residual target the correction drives
  toward). Read-only at L2.
- **`y`** — `Tensor[$S]` — the current iterate to correct. Read-only at L2 (the L2 form is
  pure / out-of-place; the L0 in-place receiver-mutating idiom — `Y` written through, the shared
  scratch `R` reused for the residual — is reintroduced only at the L1>L0 lowering).
- **result** — `Tensor[$S]` — the corrected iterate `y' = y + B·(x − A·y)`. Same field shape
  group `S`. The L2 form names no L0 destination buffer.

The general-shape congruence (square `A`, `B`, congruent `x`, `y`, result) follows the named
shape group rule — see [`semantics`](../semantics/index.md) §1.2.1 (the binding/use syntax +
the `Tensor[N]`-as-same-shape anti-pattern); not restated here.

## Semantics

`correction_step A B x y` computes the residual `r = x − A·y`, preconditions it through `B`
to produce the correction `c = B·r`, and adds the correction to the current iterate:
`y' = y + c = y + B·(x − A·y)`. The result is determined entirely by `(A, B, x, y)` — no hidden
state, no per-call side effects, no in-place mutation at the L2 surface.

The step decomposes into exactly three base operations:

```text
correction_step(A, B, x, y):
  r  = axpby(1, x, -1, apply_linop(A, y))   -- 1. residual:    r = x − A·y
  c  = apply_linop(B, r)                     -- 2. precondition: c = B·r
  y' = axpby(1, y, 1, c)                     -- 3. correct:      y' = y + c
  in y'
```

This is the **fixed three-stage sequence** the source realizes (the residual, then the
preconditioner apply, then the add-back) and it is **non-commutative**: the residual must be
computed against the *pre-correction* `y` (step 1 before step 3), and `B` preconditions the
residual *of the current `y`* (step 1 before step 2). Reordering changes the result; the
sequence is load-bearing.

The L2 form is **pure / out-of-place** — the same `(A, B, x, y)` returns the same `Tensor[$S]`
value. The L0 idiom reuses a single scratch vector `R` for the residual (`gmg.cpp:184-188`:
`B->Mult2(X, Y, R)` writes `R`, then `A->Mult(Y, R)` overwrites it, then
`AXPBY(1.0, X, -1.0, R)` finalizes the residual) and writes the result through `Y` in place —
the destination-binding / scratch-aliasing rotation is an L1>L0 concern, not L2 algebra.

### Zero-initial-guess absorption

When the step is invoked with a **zero initial guess** (the first sweep of a smoother that has
not yet accumulated, or the V-cycle pre-smooth at a fresh level), the residual degenerates:
`y = 0 ⟹ r = x − A·0 = x`, and `y' = 0 + B·x = B·x`. Palace specializes this branch
explicitly (`chebyshev.cpp:201-204` / `:271-274` `else { r = x; y = 0.0; }`;
`distrelaxation.cpp:105` `SetInitialGuess(this->initial_guess || it > 0)`;
`gmg.cpp:177-183` the `l == 0` coarse-solve sets `Y = 0` inside) as a performance trick — it
skips the `apply_linop(A, y)` against a known-zero `y`. Algebraically it is `correction_step`
with `y = 0`: the degenerate residual `r = x` (law 4). It is the **initial-guess variant axis**,
not a distinct operator.

### Conjugated preconditioner (the auxiliary-space / coarse-grid specialization)

The distributive (Hiptmair) relaxation and the multigrid coarse-grid correction are
`correction_step` with a **conjugated** preconditioner `B = T·B'·Tᵀ`, where `T` is a transfer
operator (the discrete gradient `G` for the de-Rham auxiliary-space leg; the prolongation `P`
for the coarse-grid correction). The body the source spells out
(`distrelaxation.cpp:108-117`):

```text
-- y = y + G·B_G·Gᵀ·(x − A·y)   (distrelaxation.cpp:108)
r   = axpby(1, x, -1, apply_linop(A, y))   -- residual x − A·y
x_G = apply_linop(transpose(G), r)          -- restrict residual to auxiliary space (Gᵀ·r)
y_G = apply_linop(B_G, x_G)                 -- solve in auxiliary space (B_G·Gᵀ·r)
y'  = axpby(1, y, 1, apply_linop(G, y_G))   -- prolong + add (y + G·B_G·Gᵀ·r)
```

is **`correction_step A (G·B_G·Gᵀ) x y`** — the conjugated `B` factored into restrict
(`Tᵀ`) ▷ inner-solve (`B'`) ▷ prolong (`T`). The coarse-grid correction (`gmg.cpp:189-200`:
restrict residual `Pᵀ·R`, recurse `VCycle(l-1)`, prolong-and-add `Y += P·Y_{l-1}`) is the same
shape with `T = P` and `B' = ` the recursive V-cycle solve. **This is why the one-operator form
is sufficient** (settling the one-vs-two-operator OQ in the negative): the conjugated correction
is a *choice of `B`*, closed under the LinOp interface — `T·B'·Tᵀ` is itself a LinOp — so no
distinct `conjugated_correction_step` operator is needed. The conjugation is a specialization
NOTE (law 6), not a second combinator.

### Borderline: divfree-projector is NOT a core instance

The [`divfree-projector`](./divfree-projector.md) body `y' = y − P.Grad·K⁻¹(Z(P.WeakDiv·y))`
(read with the sign at step 4 absorbed) shares the `y + correction` skeleton, and its
restrict ▷ inner-solve ▷ prolong middle is *shaped like* the conjugated correction above. But it
is **borderline, not a core instance**: the correction is a complementary projection of `y`
**onto its divergence-free part** — the "residual" is `P.WeakDiv·y` (the divergence of `y`
itself), not `x − A·y` against an external right-hand side. There is no system operator `A`
being smoothed (equivalently `A = I` and there is no external `x`); the projector removes the
gradient part of its own input. Annotated here as a borderline specialization NOTE so a reader
sees the structural kinship, but `divfree-projector` is **kept out of the core `correction_step`
roster** (it is a complementary-projector gate in its own right — firm
[`L2/divfree-projector`](./divfree-projector.md)). Settles
`correction-step-divfree-projector-borderline-7th-instance` in the negative.

## Algebraic laws

1. **Linearity in `(x, y)`.** `correction_step A B (α·x₁ + β·x₂) (α·y₁ + β·y₂)
   = α · correction_step A B x₁ y₁ + β · correction_step A B x₂ y₂` for scalars `α`, `β`.
   The step is the affine-linear map `y' = (I − B·A)·y + B·x`; with `x`, `y` scaled jointly the
   constant-free affine map is linear. Witnessed by the all-linear-primitive body
   (`apply_linop`, `axpby`); `gmg.cpp:176` names the contract.

2. **Linearity in `B` (preconditioner-additive).** `correction_step A (B₁ + B₂) x y
   = y + (B₁ + B₂)·(x − A·y) = correction_step A B₁ x y + correction_step A B₂ x y − y`.
   Follows from the linearity of `apply_linop` in the operator slot; the `− y` term is the
   shared base point. (Used implicitly by the distributive sweep, which composes a
   pre-smoother `B` correction THEN an auxiliary `G·B_G·Gᵀ` correction on the updated residual —
   sequential, not the additive form, since each re-reads the residual; see non-laws.)

3. **Fixed-point at the exact solution.** If `A·y = x` (i.e. `y` solves the system), then
   `r = x − A·y = 0` and `correction_step A B x y = y + B·0 = y` for any `B`. The exact solution
   is a fixed point of the step regardless of preconditioner. Witnessed by the residual
   construction `axpby(1, x, -1, apply_linop(A, y))` collapsing to `0`.

4. **Zero-initial-guess degeneracy.** `correction_step A B x 0 = B·x` (the residual degenerates
   to `r = x − A·0 = x`, the correction to `B·x`, the add-back to `0 + B·x`). The positive
   anchor is the explicit `else { r = x; y = 0.0; }` first-sweep branch
   (`chebyshev.cpp:201-204`,`:271-274`) — a performance specialization of this law, not a
   separate operator.

5. **Exact-inverse one-step solve.** If `B = A⁻¹`, then `correction_step A A⁻¹ x y
   = y + A⁻¹·(x − A·y) = y + (A⁻¹·x − y) = A⁻¹·x` for any `y` — one step reaches the exact
   solution. This is the structural statement that `B` is an *approximate inverse*: the step is a
   stationary (Richardson-type) iteration whose preconditioner `B` approximates `A⁻¹`, exact in
   the `B = A⁻¹` limit. (Connects to the consumer fold: the `pc_it` sweep / V-cycle iterates the
   step precisely because `B ≈ A⁻¹` is inexact.)

6. **Conjugation closure (the auxiliary-space / coarse-grid law).** For any transfer operator
   `T : LinOp[(S': ...), $S]` (range `S`, domain `S'`) and inner preconditioner
   `B' : LinOp[(S': ...), $S']`, the conjugated correction is a `B`-specialization:
   `correction_step A (T·B'·transpose T) x y = y + T·(B'·(transpose T·(x − A·y)))`. The
   right-hand factoring (restrict `Tᵀ` ▷ inner-solve `B'` ▷ prolong `T`) is the source body
   (`distrelaxation.cpp:108-117` with `T = G`; `gmg.cpp:189-200` with `T = P`). This is the law
   that makes the **one-operator combinator sufficient** for the two-operator conjugated form —
   `T·B'·Tᵀ` is itself a LinOp on `S`, so it is a legal `B`.

Laws that explicitly **do not** hold:

- **`B`-A commutativity / step idempotence.** `correction_step` is **not** idempotent:
  applying it twice, `correction_step A B x (correction_step A B x y)`, is the *second* Richardson
  sweep `y'' = y' + B·(x − A·y')`, which recomputes the residual against the updated `y'` — it is
  NOT `y'` (unless already converged, law 3). The smoother's `pc_it`-sweep loop is genuinely
  sequential: each sweep re-reads the post-previous-sweep `y` to recompute `r`
  (`distrelaxation.cpp:102` `for (it < pc_it)`). Standard outer-iteration sequentiality; the
  root of the consumer's `sequential-obstruction`.

- **Stage-reordering (non-commutativity of the three stages).** The residual (stage 1) must
  precede both the precondition (stage 2) and the add-back (stage 3); `B` preconditions the
  residual of the *current* `y`, and the add-back uses the *pre-correction* `y`. Reordering
  changes the value. The fixed three-stage sequence is load-bearing (cf. §Semantics).

- **Bit-determinism across `B`-representations.** Inherited from the `B`-slot specializations:
  a matrix-free high-order-Nedelec `A` (or a `B` built from an approximate `assemble_diagonal`)
  yields a representation-dependent floating-point value (the approximate-diagonal non-law of
  [`assemble-diagonal`](./assemble-diagonal.md) propagates through `B = ω·D⁻¹`). The algebraic
  laws hold; their IEEE-754 realizations are representation-dependent. Load-bearing per CLAUDE.md
  §"Optimization tricks vs. base algebra".

## Specializations

The smoother family chooses `B`. Each is a specialization NOTE under this combinator (the
combinator is the entry; these are NOT same-named floors mirrored beside it):

- **Jacobi** — `B = ω·D⁻¹` (the damped inverse diagonal). The *non-iterated, degree-zero* case:
  the bare [`jacobi-smoother`](./jacobi-smoother.md) gate IS the `B` apply `op.dinv ⊙ x`, and
  the Jacobi *iteration* (the consumer's Richardson sweep) is `correction_step` with this `B`.
  The L0 contract: the Jacobi smoother is consumed as the `B` slot of a `correction_step`-shaped
  sweep wrapped in a Krylov / multigrid loop (the `jacobi-smoother` entry's §Semantics
  no-initial-guess precondition is exactly "the bare gate is the preconditioner *action*, the
  Richardson sweep is the consumer's responsibility" — i.e. `correction_step` is that consumer).

- **Chebyshev** — `B = p_order(D⁻¹A)` (the order-`order` correction polynomial in `D⁻¹A`). The
  [`chebyshev-iteration`](./chebyshev-iteration.md) sweep body
  `y = y + p(A)·(x − A·y)` (`chebyshev.cpp:193`/`:264`) is **exactly** `correction_step A
  p_order(D⁻¹A) x y` with the inner polynomial recurrence realizing `B·r` (the three-term
  recurrence over `dinv ⊙ r` IS the application of `p_order(D⁻¹A)` to the residual `r`). The
  combinator names the residual-correction skeleton; `chebyshev-iteration` fills the `B` slot
  with the polynomial and unfolds the polynomial's internal recurrence.

- **Distributive (Hiptmair) / coarse-grid** — `B = T·B'·Tᵀ` (the conjugated auxiliary-space /
  coarse-grid correction; law 6). `T = G` (discrete gradient, de-Rham auxiliary leg) or `T = P`
  (prolongation, coarse-grid correction); `B'` the inner auxiliary-space solve or recursive
  V-cycle. The `multigrid-relaxation-smoother` (L1) / GMG V-cycle (feature column) compose this.

## Dependencies

**Same-layer (L2)**: none as *blocking* same-layer-combinator dependencies — the three stages
compose L1 primitives directly. The body is `apply_linop` (the `A·y` operand, and `B·r` when `B`
is itself an apply) + `axpby` (the residual `x − A·y` and the `y + correction` add).

**L1 primitives (depends-on)**:

- [`apply_linop`](../L1/apply_linop.md) (firm) — the operator action `A·y` (one per step) and
  the preconditioner apply `B·r` (when `B` is realized as a LinOp apply).
- [`axpby`](../L1/axpby.md) (firm; arity-2 specialization of `linear_combination`) — the residual
  `axpby(1, x, -1, A·y)` and the add-back `axpby(1, y, 1, c)`. Palace realizes the residual
  literally as `linalg::AXPBY(1.0, X, -1.0, R)` (`gmg.cpp:188`, `distrelaxation.cpp:110`,
  `chebyshev.cpp:199`/`:270`).

**Specializations (reference — they cite THIS combinator; the combinator does not depend on
them)**: [`jacobi-smoother`](./jacobi-smoother.md), [`chebyshev-iteration`](./chebyshev-iteration.md).

**Borderline reference (NOT a core instance)**: [`divfree-projector`](./divfree-projector.md).

**Cross-cutting concepts**:

- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the `pc_it`-sweep / V-cycle
  recurrence (each sweep re-reads the residual; the step-idempotence non-law). The *step* is not
  obstructed; the *fold over steps* is the consumer's obstruction.
- [`constructed-operators`](../concepts/constructed-operators.md) — `B` is a constructed
  preconditioner closure built once at setup (the damped inverse diagonal, the polynomial
  coefficients, the conjugated transfer-operator chain).
- [`variant-absorption`](../concepts/variant-absorption.md) — element-type and
  operator-representation absorbed into `A` / `B`.

## Variant axes

`correction_step` has **two parametric axes + two absorbed axes**:

Parametric:

1. **`B`-slot** (`ω·D⁻¹` Jacobi | `p_order(D⁻¹A)` Chebyshev | `T·B'·Tᵀ` conjugated
   distributive/coarse-grid) — the defining parametric axis; the choice of `B` is what the
   smoother family specializes. Parametric (one combinator per `B` at each call site), not a
   distinct operator per choice.
2. **initial-guess** (`zero-guess` degenerate-residual `r = x, y = 0` | `nonzero-guess` full
   `r = x − A·y`) — the law-4 degeneracy, realized as the explicit first-sweep branch
   (`chebyshev.cpp:201-204`/`:271-274`; `distrelaxation.cpp:105`).

Absorbed:

- **element-type** (`real` | `complex`) — collapsed into the operand vectors and the `B`
  closure; the source instantiates both (`gmg.cpp:208-209`, `distrelaxation.cpp` template
  instantiations).
- **operator-representation** (`sparse-CSR | matrix-free-Nedelec | parallel-wrapped`) —
  collapsed into `A` and `B` at setup, via the operators' own representation-axis absorption.

## Status

`firm` — the combinator is a direct transcription of the residual-correction body Palace names
**verbatim** at four positive source sites (`gmg.cpp:176`, `distrelaxation.cpp:104`,
`chebyshev.cpp:193`, `chebyshev.cpp:264`), each spelling the contract `y + B·(x − A·y)` in the
source's own comment AND realizing it with the all-linear-primitive body
(`apply_linop` + `linalg::AXPBY`). The six algebraic laws are syntactic identities on that
positive structure (linearity in `(x,y)` and in `B`; fixed-point at the exact solution; the
zero-guess degeneracy; the exact-inverse one-step solve; the conjugation closure); the non-laws
(step non-idempotence / `pc_it` sequentiality, stage non-commutativity, representation-dependent
bit-determinism) are catalogued explicitly. The two parametric + two absorbed variant axes are
exhaustive.

**Firm-on-positive-structure.** No dedicated `test-correction-step.cpp` exists, and none is
needed: every law is a syntactic identity readable straight off fully-present positive source —
the contract comments name the algebra, the bodies realize it with named L1 primitives — not a
literature-inferred convergence claim. (The *convergence* of the iterated step is the consumer's
fold's property, gated at the smoother / V-cycle entries; the *step* itself is firm operator
algebra.) This matches the `apply_linop` / `jacobi-smoother` / `chebyshev-iteration`
firm-on-positive-structure precedents. Behaviour is exercised through every smoother integration
path (the GMG / distributive-relaxation / Chebyshev / Jacobi consumers).

Well-foundedness: both `depends-on` targets (`apply_linop`, `axpby`) are firm (rank 3); this
node is firm (rank 3). The specialization edges to `jacobi-smoother` / `chebyshev-iteration` are
`reference` (they cite this combinator as their entry; this combinator does not build-depend on
them), so they do not constrain rank.

## Evidence

Self-verified via `tools/citecheck/citecheck.py --anchor` against on-disk
`reference/palace/palace/linalg/{gmg,distrelaxation,chebyshev,jacobi}.cpp`, 2026-06-07 (codemap
`read_range` drifted +1 on the chebyshev comment lines; on-disk citecheck wins):

- `palace/linalg/gmg.cpp:174-176` — the V-cycle contract comment: "Important to note that the
  smoothers must respect the initial guess flag correctly (given X, Y, compute
  **Y <- Y + B (X - A Y)**)." The verbatim `correction_step` contract. Self-verified — anchor
  `Y <- Y + B (X - A Y)` at `:176`.
- `palace/linalg/gmg.cpp:184-188` — the V-cycle pre-smooth `B[l]->Mult2(X, Y, R)` + residual
  `A[l]->Mult(Y, R); linalg::AXPBY(1.0, X, -1.0, R)` — the residual stage realized as
  `apply_linop` ▷ `axpby`. Self-verified — anchor `AXPBY(1.0, X[l], -1.0, R[l])` at `:188`.
- `palace/linalg/gmg.cpp:189-200` — coarse-grid correction (`B = P·B_c·Pᵀ`, law 6): restrict
  `RealMultTranspose(*P, R, X_{l-1})` (`:191`), recurse `VCycle(l-1)` (`:196`), prolong-and-add
  `RealMult(*P, Y_{l-1}, R); Y += R` (`:199-200`). Self-verified — anchor `VCycle(l - 1, false)`
  at `:196`.
- `palace/linalg/distrelaxation.cpp:104` — the distributive sweep contract comment
  "**y = y + B (x - A y)**" (the pre-smoother `B` leg). Self-verified — anchor at `:104`.
- `palace/linalg/distrelaxation.cpp:108-117` — the conjugated auxiliary leg comment
  "**y = y + G B_G Gᵀ (x - A y)**" (`:108`) + body: residual `A->Mult(y,r); AXPBY(1.0, x, -1.0,
  r)` (`:109-110`), restrict `RealMultTranspose(*G, r, x_G)` (`:111`), inner-solve
  `B_G->Mult2(x_G, y_G, r_G)` (`:116`), prolong-add `RealAddMult(*G, y_G, y)` (`:117`) —
  `correction_step A (G·B_G·Gᵀ) x y` (law 6, `T = G`). Self-verified — anchor `y = y + G B_G` at
  `:108`.
- `palace/linalg/distrelaxation.cpp:102` — the consumer fold `for (int it = 0; it < pc_it;
  it++)` — the `pc_it`-sweep iterate_while driver above the step (NOT folded into the
  combinator). Self-verified.
- `palace/linalg/chebyshev.cpp:193` — 4th-kind smoother sweep contract comment "Apply smoother:
  **y = y + p(A) (x - A y)** ." — `correction_step A p_order(D⁻¹A) x y`. Self-verified — anchor
  `y = y + p(A) (x - A y)` at `:193`.
- `palace/linalg/chebyshev.cpp:196-199` — 4th-kind residual stage: `ApplyOp(*A, y, r);
  linalg::AXPBY(1.0, x, -1.0, r)` (the `nonzero-guess` residual branch). Self-verified — anchor
  `AXPBY(1.0, x, -1.0, r)` at `:199`.
- `palace/linalg/chebyshev.cpp:201-204` — the `zero-guess` degenerate branch
  `else { r = x; y = 0.0; }` (law 4). Self-verified.
- `palace/linalg/chebyshev.cpp:264` — 1st-kind smoother sweep contract comment "Apply smoother:
  y = y + p(A) (x - A y) ." Self-verified — anchor `y = y + p(A) (x - A y)` at `:264`.
- `palace/linalg/chebyshev.cpp:270-271` — 1st-kind residual `ApplyOp(*A, y, r); AXPBY(1.0, x,
  -1.0, r)`. Self-verified — anchor `AXPBY(1.0, x, -1.0, r)` at `:270`.
- `palace/linalg/jacobi.cpp:90-93` — the Jacobi `B = ω·D⁻¹` slot setup (`dinv *= omega` at
  `:92`); the bare `B` apply is `jacobi-smoother`, consumed as the `B` slot of a
  `correction_step` sweep. Self-verified — anchor `dinv *= omega` at `:92`.
- `book/src/L2/chebyshev-iteration.md` (firm) — the `B = p_order(D⁻¹A)` specialization; its sweep
  body §Semantics is `correction_step` with the polynomial filling the `B` slot.
- `book/src/L2/jacobi-smoother.md` (firm) — the `B = ω·D⁻¹` (degree-zero, non-iterated)
  specialization; the bare gate is the `B` apply.
- `book/src/L1/divfree-projector.md` (firm) — the borderline case (complementary projector,
  `A = I` / no external `x`), kept OUT of the core roster.
- `book/src/semantics/index.md` §1.2.1–§1.2.2 — the named-shape-group convention `S` follows
  (USE+LINK, not restated).

## L2 vs lower-layer distinction

- **L1**: the residual-correction body appears only *inside* each smoother's L1 entry (the
  `jacobi-smoother` Richardson-sweep note, the `chebyshev-smoother` closed-form step). There is
  no L1 `correction_step` primitive — the body is realized per-smoother via the in-place
  receiver-mutating L0 kernels.
- **L2**: `correction_step` is mined as a first-class **combinator** — the shared per-sweep body
  named once, with the smoothers as `B`-choosing specializations. This is the
  conciseness-driven in-layer combinator the vocabulary-shift redirect calls for: the smoother
  entries state which `B` they plug in, rather than re-spelling the residual-correction skeleton.

The combinator does NOT lower as a single L1 entry (no L1 `correction_step` exists); it lowers
*through its specializations* — each smoother's L1 entry realizes the step with its concrete `B`.
The combinator is an L2-native abstraction (it exists because L2 conciseness demands it), with
the L1 evidence transitive through the specialization entries' L0 anchors.
