# chebyshev-nested-recurrence

The L3>L2 lowering theme for the `chebyshev` fixed-degree polynomial smoother. The
rewrite is **substantive (non-identity)** on the loop surface: at L3 the operator is a
`partial-obstruction` whose iteration view is **two nested sequential folds** — the inner
degree-`order` three-term `k`-recurrence and the outer `pc_it` Richardson sweep, both rendered
as explicit `iterate_while_pure_L3` tail recursions carrying first-class `sequential-obstruction`s.
The L3 nested-tail-recursion form **dissolves** into the L2
[`chebyshev-iteration`](../L2/chebyshev-iteration.md) `sweep`-iterated-by-role composition (the
`for k in 1 .. order-1` loop referenced as a composition driver, the `pc_it` sweep named by role),
and the **two named obstructions are erased to their L2 shadows** (the step-reordering /
`k`-recurrence-associativity non-law + the `pc_it`-sweep-non-commutativity non-law). The per-inner-step
**body** is **identity-in-form** across the hop. This is the **unconditional nested-double-loop**
member of the substantive L3>L2 cohort — the sibling of the unconditional single-loop
[`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md) and the variant-conditional
[`orthogonalize-variant-split`](./orthogonalize-variant-split.md).

## Slug

`chebyshev-nested-recurrence`

## Context

The `chebyshev` lowering chain spans the layer-edges of the artifact:

- **L1 firm** ([`L1/chebyshev-smoother`](../L1/chebyshev-smoother.md), cycle-012) — the closed-form
  polynomial action `y + p_order(D⁻¹ A)·(x − A·y)` as one smoother step; the recurrence body and the
  sweep loop are both below L1 resolution (the polynomial is one closed-form action; `apply_linop` and
  the opaque setup `spectrum_estimate` are the only L1 dependencies).
- **L2 firm** ([`L2/chebyshev-iteration`](../L2/chebyshev-iteration.md), cycle-012) — the
  **fusion-rotation** form `(op: ChebOp[(S: ...)], x, y, initial_guess) -> Tensor[$S]`: the closed-form
  polynomial unfolded into an explicit `order`-step three-term recurrence built from named L1 leaf
  primitives (`apply_linop`, `axpby`, `scal`, `elementwise_product`), with the HPC element-fused
  kernels (`ApplyOrder0`, `ApplyOrderK`) de-fused into base composition and the scalar generator made
  explicit as `op.scalars(k, st)`. The iteration view is **erased**: `sweep` is named, iterated
  `op.pc_it` times "by role", and the inner `for k in 1 .. order-1` loop is referenced as a
  composition driver, not rendered as recursion. The RHS of this theme.
- **L2>L1 firm**
  ([`L2-L1/chebyshev-iteration-fusion`](../L2-L1/chebyshev-iteration-fusion.md)) — the
  un-fusion of the L2 base composition into the L1 closed-form action; the `ApplyOrder0`/`ApplyOrderK`
  fusion transparency and the L1↔L2 polynomial-action equivalence (modulo floating-point
  reassociation).
- **L3 firm** ([`L3/chebyshev`](../L3/chebyshev.md), cycle-013) — the **iteration-rotation** view:
  the value-threaded `(op, x, y, initial_guess) -> y'` with the two nested loops rendered
  **explicitly** as `iterate_while_pure_L3` tail recursions over **step-count predicates** (outer
  `itloop` over `s.it <= op.pc_it`; inner `kloop` over `c.k <= op.order - 1`), each carrying a
  first-class `sequential-obstruction`. The **first** `partial-obstruction` L3 operator (c013), and
  the only one whose obstruction is a **nested double loop**. The LHS of this theme.
- **L3>L2 firm — this theme.** Narrates how the L3 nested-tail-recursion iteration-rotation form
  lowers into the L2 `sweep`-iterated-by-role composition. **Substantive (non-identity)** on the loop
  surface (the iteration view is erased and the two named obstructions shadow to the L2 non-laws);
  identity-in-form on the per-inner-step body.

This theme is the **third substantive L3>L2 theme**, after the sibling
[`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md) (cycle-021) and
[`orthogonalize-variant-split`](./orthogonalize-variant-split.md) (cycle-044). All three share the
structural shape "substantive iteration-rotation erasure" — the L3 explicit iteration form (tail
recursion + named `sequential-obstruction`) dissolves into the L2 surface where the iteration view is
erased and the obstruction survives only as L2-vocabulary non-laws. The **distinguishing features** of
this theme are: (i) the erasure is **unconditional** (holds for every parameter value — like
`ksp-solve-outer-driver`, unlike the variant-conditional `orthogonalize-variant-split`), and (ii) the
erased iteration is a **nested double loop** (the inner `k`-recurrence + the outer `pc_it` sweep — a
structure neither sibling exhibits; `ksp-solve-outer-driver` is a single outer fold,
`orthogonalize-variant-split`'s MGS obstruction is a single `j`-loop). See §"Erasure-scope contrast".

## L3 form (LHS)

The L3 form is reproduced from [`L3/chebyshev`](../L3/chebyshev.md) §"Value-threaded form (L3
rendering)" — the value-threaded nested tail recursion:

```text
chebyshev :: (op, x, y, initial_guess) -> y'
chebyshev op x y initial_guess =
  let sweep s_first y =                                   -- one Richardson sweep
        let r0   = if s_first && not initial_guess
                     then x                               -- with y := 0 below
                     else axpby 1 x (-1) (apply_linop op.A y)   -- r = x − A·y
        let y0   = if s_first && not initial_guess then zero else y
        let (c0, st0) = op.scalars 0 op.scalar_init
        let d0   = scal c0.α₀ (elementwise_product op.dinv r0)  -- d = α₀·(dinv ⊙ r)
        let (rN, dN, _stN, yN) =
              kloop 1 (r0, d0, st0, y0)                   -- sequential inner recurrence
        in axpy 1 dN yN                                   -- final accumulate y += d
      kloop k (r, d, st, y) =                             -- tail recursion over k = 1 .. order-1
        if k >= op.order then (r, d, st, y)
        else let y'        = axpy 1 d y                   -- y += d
                 r'        = axpby 1 r (-1) (apply_linop op.A d)  -- r −= A·d
                 (c, st')  = op.scalars k st
                 t         = elementwise_product op.dinv r'
                 d'        = axpby c.sd d c.sr t          -- d = sd·d + sr·t
             in kloop (k+1) (r', d', st', y')
  in itloop 1 y                                           -- tail recursion over it = 1 .. pc_it
  where itloop it y = if it > op.pc_it then y
                      else itloop (it+1) (sweep (it == 1) y)
```

The L3 form is value-threaded (positional `(op, x, y, initial_guess)`; no `Solve` monad, no
`readonly`) and **both** loops are rendered as **explicit `iterate_while_pure_L3` tail recursions** over
step-count predicates: the outer `itloop` (`it <= op.pc_it`) and the inner `kloop` (`k <= op.order -
1`). It carries **two `sequential-obstruction`s** (per [`L3/chebyshev`](../L3/chebyshev.md)
§"Iteration-rotation marker"):

- **The inner `k`-loop does not lift** — `d_{k+1}` reads `r_{k+1}` reads `d_k`; the three-term
  recurrence is genuinely sequential in `k`. A symbolic global form exists but evaluating the
  polynomial matrix-free re-derives the same recurrence; replacing it with an explicit monomial sum is
  **numerically unstable** for the operative `order` range (Phillips & Fischer 2022 §2). The
  sequentiality is **fundamental to the smoother's numerical behaviour**.
- **The outer `pc_it`-loop does not lift** — each Richardson sweep consumes the previous sweep's
  accumulated `y`; standard outer-iteration sequentiality.

Both obstructions are the L3 entry's reason to exist — the load-bearing iteration-rotation content. The
inner obstruction is **numerical-stability-rooted** (parallel to `chebyshev`'s sibling
`orthogonalize`'s MGS obstruction, *not* `eigsolve`'s opaque-library root); the outer is standard
outer-iteration sequentiality.

## L2 form (RHS)

The L2 form is reproduced from [`L2/chebyshev-iteration`](../L2/chebyshev-iteration.md) §Semantics —
the `sweep`-iterated-by-role composition:

```text
chebyshev_iteration :: (op: ChebOp[(S: ...)], x, y, initial_guess) -> Tensor[$S]
sweep(op, x, y, first):
  -- 1. residual: r = x − A·y   (or r = x, y = 0 on first sweep without guess)
  r = if first && not initial_guess
        then x                  -- with y := 0 (degenerate absorption)
        else axpby(1, x, -1, apply_linop(op.A, y))    -- r = x − A·y
  -- 2. initial direction:  d = α₀ · (dinv ⊙ r)
  (α₀, st) = op.scalars(0, op.scalar_init)
  d        = scal(α₀, elementwise_product(op.dinv, r))
  -- 3. inner recurrence  k = 1 .. order-1                 (LOOP NAMED BY ROLE)
  for k in 1 .. op.order - 1:
    y         = axpy(1, d, y)                          -- y += d
    r         = axpby(1, r, -1, apply_linop(op.A, d))  -- r -= A·d
    (sd, sr, st) = op.scalars(k, st)
    t         = elementwise_product(op.dinv, r)        -- dinv ⊙ r
    d         = axpby(sd, d, sr, t)                    -- d = sd·d + sr·t
  -- 4. final accumulate
  y = axpy(1, d, y)
  in y
-- The full action is `sweep` iterated `op.pc_it` times.   (SWEEP NAMED BY ROLE)
```

The L2 form is the base-algebra `sweep` composition with the iteration view **erased**: the inner
`for k in 1 .. order-1` loop is referenced **as a composition driver** (not rendered as recursion), and
the outer `pc_it`-sweep is **named by role** ("the full action is `sweep` iterated `op.pc_it` times").
**No `sequential-obstruction` is named at L2** (the iteration view is erased per
[`L2/index`](../L2/index.md) §Context). The two obstructions survive only as the L2 §"Algebraic laws"
non-laws:

- "Step-reordering / associativity of the `k`-recurrence" does not hold (`d_{k+1}` reads `r_{k+1}`
  reads `d_k`) — the L2 statement of "the inner loop is sequential," without naming the loop.
- "`pc_it`-sweep commutativity with the residual recompute" does not hold (each sweep recomputes
  `r = x − A·y` from the post-previous-sweep `y`) — the L2 statement of "the outer loop is sequential,"
  without naming the loop.
- "Polynomial-expansion equivalence" does not hold (the monomial sum is numerically unstable) — the L2
  statement of the inner obstruction's *root* (the numerical-stability reason the recurrence is not
  replaceable), without naming the obstruction.

## Rewrite shape

The rewrite has **two disjoint subjects**: the per-inner-step **body** (identity-in-form) and the
**nested loop surface** (substantive erasure). This is the same kernel/driver division
`ksp-solve-outer-driver` makes for `ksp_solve` — except here the body and the loops live in the *same*
operator entry (the L2 `chebyshev-iteration` is the body-composition *plus* the loop-as-driver), so this
single theme carries **both** subjects (where the Krylov chain split them into two themes:
`krylov-step-body-identity` + `ksp-solve-outer-driver`).

### Part A — the body is identity-in-form (the non-substantive part)

The per-inner-step body (the three-line `k`-update plus the initial-direction / final-accumulate) maps
**line-for-line** from the L3 `kloop`/`sweep` body to the L2 `sweep` body:

| L3 body line | L2 body line | Mapping |
|---|---|---|
| `r0 = axpby 1 x (-1) (apply_linop op.A y)` | `r = axpby(1, x, -1, apply_linop(op.A, y))` | Identity. Residual `r = x − A·y`. |
| `d0 = scal c0.α₀ (elementwise_product op.dinv r0)` | `d = scal(α₀, elementwise_product(op.dinv, r))` | Identity. Initial direction `d₀ = α₀·(dinv ⊙ r)`. |
| `y' = axpy 1 d y` | `y = axpy(1, d, y)` | Identity. Accumulate `y += d`. |
| `r' = axpby 1 r (-1) (apply_linop op.A d)` | `r = axpby(1, r, -1, apply_linop(op.A, d))` | Identity. Residual update `r −= A·d`. |
| `t = elementwise_product op.dinv r'; d' = axpby c.sd d c.sr t` | `t = elementwise_product(op.dinv, r); d = axpby(sd, d, sr, t)` | Identity. Direction recurrence `d = sd·d + sr·(dinv ⊙ r)`. |
| `axpy 1 dN yN` | `y = axpy(1, d, y)` | Identity. Final accumulate. |

The `op.scalars(k, st)` call is identical across the hop (the scalar generator is a closure carried in
`op`, not part of the tensor-field state; the 4th/1st-kind variant is absorbed identically at both
layers). This body identity-in-form is the part the L3 entry's §"Downward to L2" already annotates
in-line, and it is **retained** in-line — the body annotation is not the subject of this theme. (It is
the chebyshev analogue of `krylov-step-body-identity`; per the cycle-012 non-adjacent-identity
convention the body identity needs no theme. What needed a theme is Part B.)

### Part B — the nested loop surface is a substantive erasure (the load-bearing part)

The L3 nested tail recursion dissolves into the L2 loop-as-driver composition, and the two named
obstructions are erased to their L2 non-law shadows. This is the substantive content of the hop.

1. **The inner L3 `kloop` tail recursion dissolves into the L2 `for k in 1 .. order-1`
   composition-driver loop.** At L3 the inner recurrence is rendered as an explicit value-threaded
   `iterate_while_pure_L3` tail recursion over the carry `(r, d, st, y)` with the step-count predicate
   `k <= op.order - 1` (per [`L4-L3/krylov-step-typed-wrapper-dissolution`](../L4-L3/krylov-step-typed-wrapper-dissolution.md)
   §"What the L3 form for `iterate_while` looks like" and the strawman `book/src/semantics/index.md`
   §3.7 conventions). At L2 it is referenced **as a composition driver** — the `for k` loop sequences
   the body composition, not rendered as recursion. **Substantive**: the explicit recursion view is
   erased to a driver reference.

2. **The outer L3 `itloop` tail recursion dissolves into the L2 "iterated `op.pc_it` times"
   role-reference.** At L3 the outer sweep is an explicit `iterate_while_pure_L3` tail recursion over
   `y` with the step-count predicate `it <= op.pc_it`. At L2 it is referenced **by role** ("the full
   action is `sweep` iterated `op.pc_it` times"). **Substantive**: the explicit recursion view is
   erased to a role reference.

3. **The two named `sequential-obstruction`s erase from the surface, shadowing to the L2 non-laws.**
   This is the load-bearing forward-narration step. At L3 both obstructions are named and first-class
   (the inner `k`-recurrence does not lift; the outer `pc_it`-sweep does not lift). At L2 the iteration
   view is erased, so the obstructions are **not expressible** at the surface — but they are not *gone*:
   they survive as the L2-vocabulary residue in the §"Algebraic laws" non-laws:
   - the inner obstruction → "Step-reordering / associativity of the `k`-recurrence" non-law (+ its root
     in the "Polynomial-expansion equivalence" non-law: the numerical-stability reason the recurrence is
     not replaceable);
   - the outer obstruction → "`pc_it`-sweep commutativity with the residual recompute" non-law.
   The L2 entry itself records the handoff: its non-laws cite "(This is the L3 sequential-obstruction's
   root)" and "(L3 records this as a sequential obstruction)" — this theme is the forward narration of
   that handoff: **obstructions named at L3 → obstructions erased to their non-law shadows at L2.**

The mapping at the loop's structural level:

| L3 line | L2 line | Mapping |
|---|---|---|
| `let (rN, dN, _stN, yN) = kloop 1 (r0, d0, st0, y0)` | `for k in 1 .. op.order - 1: { … body … }` | **Substantive (non-identity).** The L3 EXPLICIT inner tail recursion over the `(r, d, st, y)` carry dissolves into the L2 composition-driver loop. The iteration view is erased: L3 renders the recursion, L2 references it as a driver. **The line where the inner iteration-rotation is erased.** |
| `in itloop 1 y where itloop it y = … itloop (it+1) (sweep (it == 1) y)` | `-- The full action is sweep iterated op.pc_it times.` | **Substantive (non-identity).** The L3 EXPLICIT outer tail recursion over `y` dissolves into the L2 named-by-role sweep iteration. **The line where the outer iteration-rotation is erased.** |
| (the inner-`k` + outer-`pc_it` `sequential-obstruction`s named in §"Iteration-rotation marker") | (no surface statement; shadows to §"Algebraic laws" non-laws) | **Substantive (non-identity).** The L3 first-class obstructions are **erased** from the L2 surface (no explicit iteration to attach them to) and survive only as the L2 step-reordering / `pc_it`-commutativity / polynomial-expansion non-laws. |

The body lines (Part A) are identity-in-form; the loop lines (Part B) carry genuine rotation (explicit
nested recursion → composition-driver + role reference) and genuine erasure (two named obstructions →
non-law shadows). The composition of Part A + Part B is the full L3>L2 story for `chebyshev`: **body
identity-in-form + nested-loop substantive erasure**.

## Applicability conditions

The rewrite is valid when all of the following hold (satisfied for the firm L3 and L2 forms by
construction):

1. **The L3 form is the firm `L3/chebyshev` partial-obstruction nested-tail-recursion form** — the
   value-threaded `(op, x, y, initial_guess) -> y'` with the inner `kloop` and outer `itloop`
   `iterate_while_pure_L3` tail recursions over step-count predicates, each carrying a named
   `sequential-obstruction`.
2. **The L2 form is the firm `L2/chebyshev-iteration` fusion-rotation composition** — the `sweep`
   base-algebra composition with the inner `for k` loop referenced as a composition driver and the
   outer `pc_it`-sweep named by role, the iteration view erased per [`L2/index`](../L2/index.md)
   §Context, and the two L3 obstructions' shadows present as the §"Algebraic laws" step-reordering /
   `pc_it`-commutativity / polynomial-expansion non-laws.
3. **The per-inner-step body's L3>L2 rotation is identity-in-form** (Part A) — every primitive call
   (`apply_linop`, `axpby`, `scal`, `elementwise_product`, `axpy`) maps line-for-line, and the
   `op.scalars(k, st)` scalar generator is identical across the hop. The body identity is retained
   in-line in the L3 §"Downward to L2"; this theme's substantive content is the loop surface (Part B).
4. **The variant axes are loop-invariant.** Both `chebyshev` variant axes (polynomial-kind
   {4th-kind, 1st-kind}; element-type {real, complex}) are absorbed into `op.scalars` / the primitive
   element-type dispatch and do **not** branch the loop structure — the nested-loop shape is identical
   across all variants (contrast `orthogonalize-variant-split`, where the obstruction is
   variant-conditional). The erasure is therefore **unconditional**: the same two-obstruction shadow
   holds for every `(polynomial-kind, element-type, order, pc_it)` configuration.

## Justification kind

**`structural`** (dominant) with secondary **`reduction-chain`**.

**Structural (dominant)**: the substantive content (Part B) is a structural fact about the layer
surfaces — L3 renders the two nested iterations explicitly (tail recursions are structural forms), L2
erases the iteration view to a composition-driver + role reference (structural absences). The two
`sequential-obstruction`s' erasure-to-non-law-shadow is structural: each obstruction is a property of
the explicit iteration structure, so erasing the structure erases the named obstruction, leaving only
the L2-expressible residue (the step-reordering / `pc_it`-commutativity / polynomial-expansion
non-laws). The body identity-in-form (Part A) is also a structural observation: the body's primitive
sequence is shape-invariant across the hop, the loops' iteration views are not.

**Reduction-chain (secondary)**: the `iterate_while_pure_L3` (inner + outer) →
loop-as-driver/role-reference consolidation is grounded in the small-step `iterate_while` semantics from
the strawman `book/src/semantics/index.md` §3.7 — each L3 tail recursion is the unfolded reduction
sequence of the bounded `iterate_while_pure` combinator, and the L2 driver/role reference is the folded
(un-unfolded) form. The forward L3→L2 narration re-folds the explicit reduction sequences back into the
named loop-as-composition-driver.

**Abstraction-direction note**: L3 is the higher-abstraction layer for this edge (it has the iteration
rotation done and the two obstructions named); L2 is the lower-abstraction layer (it erases the explicit
loop view, leaving the iteration to the consumer). The rotation direction is L3 → L2: the L3 form lowers
to the L2 form by **dissolving** the two explicit tail recursions into the loop-as-driver + role
reference and **erasing** the two named obstructions to their non-law shadows. This matches the
methodology's high→low lowering direction; the reverse (how the L2 loop-as-driver un-erases into the L3
explicit nested recursion + obstructions) is a working-note / OQ concern, recorded only in the L2 entry's
non-laws in-line, not narrated here.

## Speculative L3 operators

**None.** This theme is the substantive erasure rotation between two firm endpoints; no new L3
vocabulary is introduced. The L3 form referenced in the LHS is the firm
[`L3/chebyshev`](../L3/chebyshev.md) entry; the L2 form referenced in the RHS is the firm
[`L2/chebyshev-iteration`](../L2/chebyshev-iteration.md) entry. The `iterate_while_pure_L3` /
`iterate_while_pure` combinators are firm (`book/src/L4/iterate-while.md`, firmed cycle-007); they are
referenced, not introduced.

## Erasure-scope contrast

The three substantive L3>L2 themes divide along the **erasure-scope** axis (the c044 §Working-Notes
taxonomy candidate, now populated to three members):

| Theme | Operator | Erasure scope | Loop structure | Obstruction root |
|---|---|---|---|---|
| [`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md) | `ksp_solve` | **unconditional** | single outer fold (loop IS the operator) | the loop's own sequentiality (convergence-predicate-driven) |
| [`orthogonalize-variant-split`](./orthogonalize-variant-split.md) | `orthogonalize` | **variant-conditional** (MGS branch only) | single `j`-loop (MGS arm) | numerical stability (MGS roundoff-orthogonality) |
| `chebyshev-nested-recurrence` (this theme) | `chebyshev` | **unconditional** | **nested double loop** (inner `k`-recurrence + outer `pc_it` sweep) | numerical stability (inner) + outer-iteration sequentiality (outer) |

**`chebyshev`'s distinguishing features**: (i) the erasure is **unconditional** (like
`ksp-solve-outer-driver`, unlike the variant-conditional `orthogonalize-variant-split` — the nested-loop
shape holds for every parameter value); (ii) the erased iteration is a **nested double loop** (a
structure neither sibling exhibits — `ksp-solve-outer-driver` is a single outer fold,
`orthogonalize-variant-split`'s MGS arm is a single `j`-loop); (iii) the inner obstruction shares
`orthogonalize`'s **numerical-stability** root (the recurrence is chosen for stability over explicit
polynomial expansion), *not* `eigsolve`'s opaque-library root. The three erasure scopes are now:
**unconditional-single-loop** (`ksp-solve-outer-driver`), **unconditional-nested-double-loop**
(`chebyshev`, this theme), **variant-conditional-single-loop** (`orthogonalize-variant-split`). The
fourth substantive candidate `eigsolve` (`partial-obstruction`, opaque-library-owned) is the
**unconditional-opaque-library** member — still in-line at `L3/eigsolve` pending a dedicated theme.

## Body-identity / loop-erasure division

Like the Krylov chain, `chebyshev`'s L3>L2 lowering has two parts — but where the Krylov chain split
them into two themes (`krylov-step-body-identity` kernel + `ksp-solve-outer-driver` driver), `chebyshev`
carries both in this single theme because the L2 `chebyshev-iteration` entry is the body-composition
*and* the loop-as-driver in one (there is no separate L2 `chebyshev-step` kernel entry):

- **Body (Part A)**: identity-in-form on the per-inner-step primitive sequence (six line-for-line
  mappings); the chebyshev analogue of `krylov-step-body-identity`. Retained in-line in the L3 §"Downward
  to L2".
- **Loop surface (Part B)**: substantive (non-identity) — the two nested `iterate_while_pure_L3` tail
  recursions dissolve to the L2 loop-as-driver + role reference, erasing the iteration view and the two
  named `sequential-obstruction`s (which shadow to the L2 non-laws). The chebyshev analogue of
  `ksp-solve-outer-driver`, but **nested-double-loop** and **unconditional**.

`body-identity + nested-loop-erasure = the full chebyshev L3>L2 story.` This theme makes the
loop-erasure (Part B) the explicit subject; the body identity (Part A) is recorded as the
non-substantive counterpart, retained in-line per the cycle-012 non-adjacent-identity convention.

## Verified-against

L3 evidence (the LHS):

- `book/src/L3/chebyshev.md` (firm `partial-obstruction`, cycle-013) — the L3 nested-tail-recursion form
  this theme references as LHS. §"Value-threaded form (L3 rendering)" (the inner `kloop` + outer `itloop`
  `iterate_while_pure_L3` tail recursions), §"Iteration-rotation marker" (the two first-class
  `sequential-obstruction`s — inner `k`-recurrence + outer `pc_it`-sweep), §"Downward to L2" (records the
  body identity-in-form + the no-L3-L2-theme assertion that this theme supersedes for the substantive
  loop surface).
- `book/src/L4/chebyshev.md` (firm cycle-015) — the L4 `Solve`-monad wrapper whose two nested
  `iterate_while_pure` folds the L3 form renders as the `iterate_while_pure_L3` tail recursions this theme
  dissolves.

L2 evidence (the RHS):

- `book/src/L2/chebyshev-iteration.md` (firm, cycle-012) — the L2 fusion-rotation composition this theme
  references as RHS. §Semantics (the `sweep` body composition with the inner `for k` loop as a
  composition driver + the outer `pc_it`-sweep named by role; iteration view erased), §"Algebraic laws"
  non-laws "Step-reordering / associativity of the `k`-recurrence" + "`pc_it`-sweep commutativity with the
  residual recompute" + "Polynomial-expansion equivalence" (the L2-vocabulary shadows of the two erased
  obstructions and their numerical-stability root).
- `book/src/L1/chebyshev-smoother.md` (firm, cycle-012) — the L1 closed-form action; the body is
  value-thread-isomorphic to it transitively (in-line, no `L3-L1/` directory).

Sibling-theme evidence (the substantive L3>L2 cohort):

- `book/src/L3-L2/ksp-solve-outer-driver.md` (firm cycle-021) — the first substantive L3>L2 theme; the
  **unconditional single-loop** sibling. §"Rewrite shape" (the iteration-view-erasure + obstruction-shadow
  pattern this theme mirrors for the nested-double-loop case), §"Kernel-identity / driver-non-identity
  contrast" (the body/loop division template).
- `book/src/L3-L2/orthogonalize-variant-split.md` (firm cycle-044) — the second substantive L3>L2 theme;
  the **variant-conditional single-loop** sibling. §"Variant-split / unconditional-erasure contrast" (the
  erasure-scope axis this theme populates with a third member). Line 381 flags `chebyshev` "(in-line at
  `chebyshev-iteration` already; its obstruction is unconditional)" — superseded for the substantive loop
  surface by this theme.

L0 evidence (self-verified against `reference/palace/` source via `palace-codemap` `read_range` this
dispatch):

- `reference/palace/palace/linalg/chebyshev.cpp:191-220` — `ChebyshevSmoother<OperType>::Mult2` (4th-kind)
  — the canonical nested-double-loop body the L3 form renders as nested tail recursions. The outer
  `pc_it` sweep `for (int it = 0; it < pc_it; it++)` (`:194`); `r = x − A·y` (`ApplyOp(*A, y, r);
  AXPBY(1, x, -1, r)`, `:198-199`) or `r = x; y = 0` on first sweep without guess (`:203-204`);
  `ApplyOrder0(4/(3·λ_max), dinv, r, d)` (`:209`); the inner `k`-loop `for (int k = 1; k < order; k++)`
  (`:210`) with `y += d`, `ApplyOp(*A, d, r, -1.0)`, `sd = (2k−1)/(2k+3)`, `sr = (8k+4)/((2k+3)·λ_max)`,
  `ApplyOrderK(sd, sr, dinv, r, d)` (`:212-217`); final `y += d` (`:219`). The two nested loops whose
  explicit-recursion view L3 renders and L2 erases.
- `reference/palace/palace/linalg/chebyshev.cpp:261-293` — `ChebyshevSmoother1stKind<OperType>::Mult2`
  — identical nested-double-loop scaffold (the variant-invariant loop structure: same outer `pc_it`
  sweep + inner `k`-loop, only `op.scalars` differs). Witnesses applicability condition 4 (the loop is
  variant-invariant → the erasure is unconditional).
- `reference/palace/palace/linalg/chebyshev.hpp:72-75` — `MultTranspose2(x, y, r) { Mult2(x, y, r); }`
  — the symmetry alias (the transpose-identity law is body-level, loop-invariant; unaffected by the loop
  erasure).

Strawman / combinator evidence (the reduction-chain backing):

- `book/src/semantics/index.md` §3.7 — the `iterate_while` conventions source; each L3 tail recursion
  is the unfolded reduction sequence of the bounded `iterate_while_pure` combinator, the L2 driver/role
  reference is the folded form.
- `book/src/L4/iterate-while.md` (firm cycle-007) — the firm `iterate_while`/`iterate_while_pure`
  combinators both forms reference (L3 explicit tail recursions / L2 loop-as-driver).
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (firm cycle-008) — publishes the L3
  tail-recursion rendering of a bounded loop; the conventions source the L3 form's explicit recursion
  follows.

Cross-cutting concept references (consumed unchanged across the rotation):

- `book/src/concepts/sequential-obstruction.md` (firm) — the canonical write-up; both `chebyshev`
  obstructions named first-class at L3, erased to their non-law shadows at L2.
- `book/src/concepts/tensor-field-lift.md` — the body-lifts-but-loop-doesn't canonical partial case.
- `book/src/concepts/variant-absorption.md` — the (c) primitive-sequence axis (the polynomial-kind
  variant absorbed into `op.scalars`, loop-invariant — the basis of applicability condition 4).
- `book/src/concepts/chebyshev-iteration.md` — narrative.

Open-questions ledger:

- `scaffolding/open-questions.md` slug `l3-l2-chebyshev-substantive-theme-vs-in-line-decision`
  (this dispatch's question) — the open question this theme closes. Status updates to `closed` on
  integration with answer-link `book/src/L3-L2/chebyshev-nested-recurrence.md` (this file).

## Status

`firm` — the theme's content is firm: both endpoints are firm ([`L3/chebyshev`](../L3/chebyshev.md)
cycle-013 `partial-obstruction`; [`L2/chebyshev-iteration`](../L2/chebyshev-iteration.md) cycle-012); the
substantive non-identity content (Part B: the nested-loop iteration-view erasure + the two obstructions'
shadow-to-non-laws) is structurally grounded and citation-backed at both layers and the L0 source; the
body identity-in-form (Part A) is information-preserving and retained in-line; the rewrite-shape tables
are total on the body + loop structure with the three non-identity lines (the two fold lines + the
obstruction line) explicitly delimited; no speculative L3 vocabulary is introduced; the four
applicability conditions are stated and confirmed for both variant bodies. This theme is the **third
substantive L3>L2 theme** and the **unconditional-nested-double-loop** member of the erasure-scope axis,
joining `ksp-solve-outer-driver` (unconditional-single-loop) and `orthogonalize-variant-split`
(variant-conditional-single-loop).

Authored cycle-045 wave-1 (cross-layer-cross-cutter, audit-first dispatch — landed because the
substantive loop-erasure exceeds the cycle-012 in-line non-adjacent-identity convention, which covers
only IDENTITY edges; the `ksp-solve-outer-driver` + `orthogonalize-variant-split` precedents establish
that a `partial-obstruction`'s substantive loop-erasure gets a dedicated theme while the body identity
stays in-line), enacting **Identity-lowerings still require both L levels** (both layers carry a
chebyshev entry; this theme is the connecting substantive rotation) and **Layers are defined high→low**
(LHS L3, RHS L2, forward narration).

## L3>L2 vs body-identity distinction

The body identity-in-form (Part A) is the chebyshev analogue of `krylov-step-body-identity`; per the
cycle-012 non-adjacent-identity convention it needs no theme and stays in-line in the L3 §"Downward to
L2". The substantive content of this theme is the loop surface (Part B): the two nested
`iterate_while_pure_L3` tail recursions dissolve to the L2 loop-as-driver + role reference, erasing the
iteration view and the two named `sequential-obstruction`s. Together: **body identity-in-form +
nested-loop substantive erasure = the full chebyshev L3>L2 story** — the body/loop division made visible
in the `book/src/L3-L2/` Part, exactly as the Krylov chain's two-theme split makes it visible (here in
one theme because the L2 entry carries both the body composition and the loop driver).
