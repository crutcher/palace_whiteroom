# linear-combination-fold-specialization

The fusion-selection rotation for the BLAS-1 scalar-weighted-vector-sum cohort. Lowers
the L2 variadic fold [`linear_combination`](../L2/linear_combination.md) into its L1
fixed-arity leaf — [`scal`](../L1/scal.md), [`axpy`](../L1/axpy.md),
[`axpby`](../L1/axpby.md), or [`axpbypcz`](../L1/axpbypcz.md) — by **selecting the
maximal fused L1 primitive that matches the fold's term-list length**, and beyond
arity 3 (Palace's fused-kernel ceiling) lowering the tail of the fold into an iterated
`axpbypcz`-into-output chain. Narrated forward: the one variadic L2 fold **re-fuses**
downward into Palace's bounded family of distinct fixed-arity call shapes, and this
theme records which fixed-arity shape each list-length picks and **the pinned summation
order that shape evaluates in** (the load-bearing-numerical content the L2 entry's
permutation IEEE-754 non-law deferred here).

## Slug

`linear-combination-fold-specialization`

## L2 form (LHS)

The L2 form is the variadic fold over a list of (coefficient, term) pairs
([`linear_combination`](../L2/linear_combination.md) §Signature):

```text
linear_combination :: [(Scalar, Tensor[(S: ...)])] -> Tensor[$S]
linear_combination pairs = foldl (\acc (a, t) -> acc + scal a t) (zeros $S) pairs
```

The fold is pure / out-of-place and **order-agnostic for value** (the L2 entry's
permutation EXACT-ARITHMETIC law, law 7): in exact arithmetic the result `Σᵢ aᵢ·tᵢ` is
invariant under permutation of the term list and under any reassociation of the
accumulation. The term list has no fixed length at L2 — the **arity axis is the axis
this single L2 operator unifies** (L2 entry §"L2 vs L1 distinction"). The shape
precondition `all tᵢ : Tensor[(S: ...)]` (every term is congruent over one shape group `S`
of arbitrary, unknown rank — NOT rank-1; named shape groups per
[`l4_calculus`](../design/l4_calculus.md) §1.2.1) is the
aligned-pass precondition the L0 fused kernels require.

## L1 form (RHS)

The L1 form is the **four distinct fixed-arity leaf primitives**, each mirroring one
Palace L0 C++ symbol one-to-one
([`scal`](../L1/scal.md) / [`axpy`](../L1/axpy.md) / [`axpby`](../L1/axpby.md) /
[`axpbypcz`](../L1/axpbypcz.md) §Signature). At this RHS the operands are the **concrete
Palace `Vector`s** — genuinely flat rank-1 dof-vectors of length `N` — so the `Tensor[N]`
rendering here is the literal L0/L1 call shape, NOT the shape-generic `(S: ...)` of the L2
fold above (the rank-1-ness is real at the lowered call, not an accidental implication):

```text
scal     :: (α: Scalar, x: Tensor[N])                                            -> Tensor[N]
axpy     :: (α: Scalar, x: Tensor[N], y: Tensor[N])                              -> Tensor[N]
axpby    :: (α: Scalar, x: Tensor[N], β: Scalar, y: Tensor[N])                   -> Tensor[N]
axpbypcz :: (α: Scalar, x: Tensor[N], β: Scalar, y: Tensor[N], γ: Scalar, z: Tensor[N]) -> Tensor[N]

scal(α, x)                 = α·x
axpy(α, x, y)              = α·x + y
axpby(α, x, β, y)          = α·x + β·y
axpbypcz(α, x, β, y, γ, z) = α·x + β·y + γ·z
```

At L1 the term list is **below the layer's resolution**: L1 sees four operators with
fixed argument counts, not one variadic fold. Each has a fixed evaluation order pinned
by its L0 body (the §"Summation-order recording" section below). The arity over which
L1 has four operators is exactly the axis the single L2 form unifies.

## The fusion-selection rewrite (L2 → L1)

The lowering reads the fold's term-list **length** and selects the **maximal fused L1
primitive matching that arity**, lowering the remaining terms (beyond what the maximal
fused leaf consumes) into an iterated accumulate-fold. This is a **resolution refinement
plus a fusion choice**, not an algebraic transformation of the value (L2 entry laws 6 +
2): each lowered call computes the same value the fold does (modulo the summation-order
non-law below).

```text
linear_combination []                          ⇒  zeros N                            -- arity 0 (the fold seed)
linear_combination [(α, x)]                    ⇒  scal(α, x)                          -- arity 1
linear_combination [(α, x), (1, y)]            ⇒  axpy(α, x, y)                       -- arity 2, unit 2nd coeff
linear_combination [(α, x), (β, y)]            ⇒  axpby(α, x, β, y)                   -- arity 2, general
linear_combination [(α, x), (β, y), (γ, z)]    ⇒  axpbypcz(α, x, β, y, γ, z)          -- arity 3
linear_combination ((α,x):(β,y):(γ,z):rest)    ⇒  let acc = axpbypcz(α, x, β, y, γ, z)
                                                  in foldl accumulate2 acc rest       -- arity ≥ 4: iterated chain
```

where the arity-≥4 tail is the **left-fold of `axpbypcz`-into-output with the aliased
coefficient pinned to 1** — i.e. each step consumes (up to) two further terms and folds
them into the running accumulator, exactly the `γ=1` accumulate-into shape Palace
open-codes:

```text
accumulate2 acc [(β, y), (δ, w)]  =  axpbypcz(β, y, δ, w, 1, acc)   -- acc ← β·y + δ·w + acc
accumulate2 acc [(β, y)]          =  axpy(β, y, acc)                -- odd tail: acc ← β·y + acc
```

The **selection rule** is: *pick the largest fused leaf whose fixed arity ≤ the
remaining term count, then recurse on the unconsumed tail*. The maximal fused leaf is
`axpbypcz` (arity 3) — **Palace's fused-kernel ceiling**; there is no fused L0 kernel
beyond three terms (the free-function family stops at `AXPBYPCZ`,
`palace/linalg/vector.hpp:305-316`). So an arity-`n` fold for `n > 3` does NOT lower
into one call — it lowers into a **sequence of L1 calls**: this is the exact point at
which Palace stops fusing, and the L2 fold's de-fusion into a base-primitive sequence
becomes the visible lowering work. Live witnesses of the iterated `γ=1` chain:
`palace/linalg/nleps.cpp:343-344` (eigenvector synthesis: `AXPBYPCZ(…, 1.0, z.Real())`
accumulates two real/imag terms per `j`-loop step into the running `z`) and
`palace/models/romoperator.cpp:188-189` (ROM solution reconstruction: the same
two-terms-into-`u` shape).

### Two sub-selections within arity 2

Arity 2 has **two** L1 targets, disambiguated by the second coefficient:

- if the second pair's coefficient is the literal `1` → `axpy(α, x, y)` (the
  unit-coefficient fused leaf; one fewer scalar multiply). This is the
  fold-length-2 case where the L2 entry's law-6 specialization fixes the second
  coefficient to 1.
- otherwise → `axpby(α, x, β, y)` (the general two-coefficient fused leaf).

The choice is a **fusion-of-a-multiply** refinement (drop the `1·y` multiply), not a
value change; both compute `α·x + (β|1)·y`. It mirrors the L1 subsumption
`axpy ≺ axpby` (axpby.md law 1) — `axpy` is `axpby` with `β` pinned to 1.

### The arity-3 → arity-2 fall-through (the in-source collapse)

When the arity-3 fold's third coefficient `γ` is **zero**, the lowering does NOT emit
`axpbypcz` — it falls through to the arity-2 `axpby`, because the `γ·z` term drops (L2
entry law 5, zero-coefficient term-drop). This is **not** an abstraction we impose: it
is read directly off Palace's L0 body. The real-real `AXPBYPCZ` at
`palace/linalg/vector.cpp:745-758` branches on `γ`:

```text
if (gamma == 0.0) { add(alpha, x, beta, y, z); }        // :749-751  arity-3 collapses to the fused arity-2 pass
else              { AXPBY(alpha, x, gamma, z);           // :753-756  general arity-3: split two-pass
                    z.Add(beta, y); }
```

The `γ==0` branch (`:749-751`) is the in-source arity-collapse — the arity-3 call
dropping its third term and invoking the **same fused single-pass** `add(α, x, β, y, z)`
the arity-2 `AXPBY` uses. A live witness is the RK time-integrator stage
`palace/models/timeoperator.cpp:217` (`AXPBYPCZ(1.0, RHS2, dt, k1, 0.0, k2)` — `γ=0`,
collapsing to `k2 ← RHS2 + dt·k1`). This branch is **direct source evidence that the
family is one fold parameterized by arity** (the harvester's law-5 anchor), and it is
the reason the arity-3 → arity-2 selection edge is firm rather than inferred.

## Summation-order recording

This is the **load-bearing-numerical content the L2 entry deferred to this theme** (L2
entry permutation IEEE-754 non-law: "which order a given lowered call pins is recorded
by the L2>L1 lowering theme"). The L2 fold is order-agnostic for *value*; **bit-identical
reproduction of any L0 call requires matching that call's pinned summation order**. The
orders are read off the verified `vector.cpp` bodies (real-real path; the complex paths
delegate to MFEM member ops, and their operand-order parity with the real path is
MFEM-internal — not Palace-confirmed):

| lowered call | L0 body (verified) | pinned evaluation order |
|---|---|---|
| `scal(α, x)` | `vector.cpp:203-227` (`operator*=`) | single scaled pass `x ← α·x` (one rounding per element) |
| `axpy(α, x, y)` | `vector.cpp:702-712` | `α==1` fast-path `y += x` (FMA-free add); else `y.Add(α, x)` (`y ← y + α·x`, one FMA per element) |
| `axpby(α, x, β, y)` | `vector.cpp:726-730` | **single fused aligned pass** `add(α, x, β, y, y)` — MFEM 5-arg in-place linear-combine; one strided pass, fewest roundings |
| `axpbypcz(α, x, β, y, γ, z)`, `γ == 0` | `vector.cpp:749-751` | **single fused pass** `add(α, x, β, y, z)` — identical order to the fused `axpby` above |
| `axpbypcz(α, x, β, y, γ, z)`, `γ ≠ 0` | `vector.cpp:753-756` | **two-pass split**: first `AXPBY(α, x, γ, z)` ⟹ `z ← α·x + γ·z` (fused), then `z.Add(β, y)` ⟹ `z ← z + β·y`. The `β·y` term is added in a **separate, later pass** — a distinct rounding schedule from the one-pass `add(α,x,β,y,z)` |

The two arity-3 branches do **NOT** agree bit-for-bit (the L2 entry / axpbypcz.md
non-law): the `γ==0` fused branch sums its two surviving contributions (`α·x + β·y`) in
one strided pass (the `γ·z` term is dropped — `add(α, x, β, y, z)` is a two-term combine),
whereas the `γ≠0` branch computes `α·x + γ·z` first and folds `β·y` in afterward, so
the partial-sum magnitudes — and hence the IEEE-754 rounding — differ. **For the
arity-≥4 iterated chain, the pinned order is the left-fold order**: terms are folded
into the accumulator in list order, each `accumulate2` step a fused `γ=1` `add`-pass; a
different chunking or term permutation gives a different bit-level result. The canonical
order this theme names is the **L2 fold's `foldl` left-to-right order** (L2 entry law 7);
a downstream implementation reproducing a specific Palace call bit-for-bit must pin the
order in this table, not merely the value.

## Applicability conditions

The fusion-selection lowering preserves the L2 value when:

1. **Shared shape group (the aligned-pass precondition).** All terms satisfy
   `all tᵢ : Tensor[(S: ...)]` (the L2 signature precondition — congruence over one shape
   group `S`). At the lowered L0 call the operands are flat rank-1 `Vector`s, so this
   congruence is read concretely as a shared length `N`: the fused single-pass kernels
   (`add(α, x, β, y, z)`) stride over that one flat axis; if the terms did not share it
   the fused leaves would not apply and the lowering would have to fall back to
   per-term `scal` + add (which Palace does not do — the precondition always holds in
   the BLAS-1 cohort).

2. **Arity ceiling at 3.** The maximal fused leaf is `axpbypcz` (arity 3) — there is no
   `AXPBYPCZPDW` (`vector.hpp:305-316`). Folds of arity ≥ 4 lower to a **sequence** of
   L1 calls (the iterated `γ=1` chain), not a single fused call. This is where Palace
   stops fusing; the lowering is correct only if the iterated chain reproduces the
   fold's value (it does — concatenation-homomorphism, L2 entry law 2).

3. **Selection is value-preserving, summation-order is not free.** Each selected leaf
   computes the fold's value (L2 entry laws 6 + 2). Bit-reproduction of a *specific*
   Palace call additionally requires pinning that call's summation order (the table
   above). The lowering is valid under the **algorithmic-correctness** reading
   unconditionally, and under the **bit-reproduction** reading only when the order in
   the table is matched (the standard load-bearing-vs-transparent classification, per
   CLAUDE.md "load-bearing numerical tricks … non-associative reduction orderings …
   preserve as explicit algebraic claims").

4. **The arity-3 → arity-2 fall-through requires the literal-zero coefficient.** The
   `γ==0` fall-through (`:749-751`) selects `axpby` over `axpbypcz` only when `γ` is the
   literal `0.0` (a runtime branch in the L0 body, not a compile-time arity change). A
   non-zero-but-tiny `γ` does NOT take the branch — it stays `axpbypcz` with the
   two-pass split. The selection edge is the exact L0 `γ == 0.0` test.

5. **Element-type / scalar-promotion conformance.** Element type is one shared
   `T ∈ {real, complex}` with the `real ⊑ complex` promotion lattice
   ([`concepts/scalar-promotion`](../concepts/scalar-promotion.md)), inherited unchanged
   from the L1 leaves; the lowering dispatches to the real or complex L0 overload of the
   selected leaf. The complex overloads delegate to MFEM member ops
   (`y.AXPBY(...)` / `z.AXPBYPCZ(...)`, `vector.cpp:732-744, :760-769`); their operand
   order is presumed to match the real path but that parity is MFEM-internal (not
   Palace-confirmed) — bit-faithful summation order is verified only for the real-real path.

## Justification kind

`algebraic` — the selection rule **is** the L2 entry's already-firm laws read as a
lowering: law 6 (the four specialization identities `scal/axpy/axpby/axpbypcz =
linear_combination [...]`) gives the arity-1/2/3 dispatch directly, and law 2
(concatenation-homomorphism, the monoid homomorphism from `([(Scalar,Tensor[(S: ...)])], ++,
[])` to `(Tensor[$S], +, zeros)`) licenses the arity-≥4 split into an iterated chain
(`linear_combination (a ++ b) = linear_combination a + linear_combination b`, so the
fold over a long list equals the running accumulate of fixed-arity chunks). The
arity-3 → arity-2 fall-through is law 5 (zero-coefficient term-drop), and it is grounded
by **direct source-transcription** of the in-source `γ==0` branch
(`vector.cpp:749-751`). A **reduction-chain** flavour is present (the iterated-chain
fold is a small-step left-fold), but the governing justification is the algebraic
specialization+concatenation identity, so the theme is classified `algebraic`. The
single-aligned-pass fusion (the `add(α,x,β,y,z)` kernel) is a transparent-performance
trick (L2 entry §"Fusion note") nested inside each selected leaf; the two-branch
summation-order split is the load-bearing-numerical residue recorded above.

## Speculative L1 operators

**None.** All four RHS leaves are firm:
[`scal`](../L1/scal.md) / [`axpy`](../L1/axpy.md) / [`axpby`](../L1/axpby.md) /
[`axpbypcz`](../L1/axpbypcz.md), each mirroring one Palace L0 symbol one-to-one, and the
`axpby-as-primitive` decision
([`scaffolding/decisions/axpby-as-primitive.md`](../../../scaffolding/decisions/axpby-as-primitive.md))
keeps each as a leaf (fuse, don't decompose). The LHS
[`linear_combination`](../L2/linear_combination.md) is firm (harvested this cycle). This
theme proposes no new operators — it is the lowering edge between firm vocabulary on
both sides.

## Verified-against

L0 evidence ranges (self-verified via `palace-codemap` read_range this invocation —
producer-citation-drift discipline, `verify-citation-range` producer-self-verification):

- `palace/linalg/vector.cpp:702-712` — `AXPY(double, const Vector &, Vector &)`: the
  `α == 1.0` fast-path (`y += x`) vs the general `y.Add(alpha, x)`. The arity-2-coeff-1
  (`axpy`) leaf and its pinned order. **Self-verified.**
- `palace/linalg/vector.cpp:726-730` — `AXPBY(double, const Vector &, double, Vector &)`
  → `add(alpha, x, beta, y, y)`: the single fused aligned in-place linear-combine
  (the arity-2 `axpby` leaf; the fused-pass summation order). **Self-verified.**
- `palace/linalg/vector.cpp:745-758` — the real-real `AXPBYPCZ` body with the
  `if (gamma == 0.0) { add(alpha, x, beta, y, z); }` fast-path (`:749-751`, the arity-3 →
  arity-2 collapse / law-5 witness) and the `else { AXPBY(alpha, x, gamma, z);
  z.Add(beta, y); }` two-pass split (`:753-756`, the general-arity-3 pinned summation
  order). **Self-verified.**
- `palace/linalg/vector.hpp:305-316` — the `AXPY` / `AXPBY` / `AXPBYPCZ` free-function
  template declarations with their `// Addition …` comments; the bounded-arity surface
  (ceiling at `AXPBYPCZ` — no arity-4 fused kernel) the fold lowers into.
  **Self-verified.**
- `palace/linalg/nleps.cpp:343-344` — `AXPBYPCZ(y(j).real(), X[j].Real(), -y(j).imag(),
  X[j].Imag(), 1.0, z.Real())` and the `.imag()` line: the `γ=1` accumulate-two-terms-
  into-output, the live witness of the arity-≥4 iterated chain (eigenvector synthesis).
  **Self-verified** (the `z = 0.0` seed is at `:340`; the loop runs over `j`).
- `palace/models/romoperator.cpp:188-189` — `AXPBYPCZ(y(j).real(), V[j],
  y(j + 1).real(), V[j + 1], 1.0, u.Real())` and `u.Imag()`: ROM solution reconstruction,
  the same accumulate-two-terms-into-`u` `γ=1` iterated-chain shape. **Self-verified.**
- `palace/models/timeoperator.cpp:217` — `AXPBYPCZ(1.0, RHS2, dt, k1, 0.0, k2)`: RK
  stage, the `γ=0` collapse to the fused arity-2 `axpby` (`k2 ← RHS2 + dt·k1`); live
  witness of the arity-3 → arity-2 fall-through. **Self-verified.**

L2 / L1 anchors (firm both sides):

- `book/src/L2/linear_combination.md` — the firm L2 variadic fold (LHS); its laws 2 / 5 /
  6 / 7 + IEEE non-law are this theme's selection rule and summation-order deferral.
- `book/src/L1/scal.md`, `book/src/L1/axpy.md`, `book/src/L1/axpby.md`,
  `book/src/L1/axpbypcz.md` — the four firm fixed-arity leaves (RHS).

## Status

`firm` — the L2 LHS is firm (harvested this cycle), all four L1 RHS leaves are firm, and
the fusion-selection rule IS the L2 entry's already-firm laws 6 (specialization
identities) + 2 (concatenation-homomorphism) read as a lowering. The arity-3 → arity-2
fall-through and the per-call summation orders are read straight off the **verified**
`vector.cpp` bodies (the `γ==0` branch `:749-751`; the two-pass `else` `:753-756`; the
`AXPBY` fused pass `:726-730`; the `AXPY` fast-path `:702-712`), with three live
iterated-chain / collapse witnesses (`nleps.cpp:343-344`, `romoperator.cpp:188-189`,
`timeoperator.cpp:217`). No literature inference, no negative-anchor reconstruction, no
speculative operator. This is the second chapter under the `book/src/L2-L1/` Part
(after [`chebyshev-iteration-fusion`](./chebyshev-iteration-fusion.md)); a
`lowering-verifier` audit confirming the selection rule + summation-order table against
the L0 source is the standard follow-up, not a status reduction.

## Open questions / caveats

- **Lifting note (reverse direction, working notes only — NOT in the high→low chapter
  body).** Lifting an L1 fixed-arity call *up* to the L2 fold is determinate: each leaf
  IS a fixed-length term list (law 6), so `axpbypcz(α,x,β,y,γ,z)` lifts to
  `linear_combination [(α,x),(β,y),(γ,z)]` with no additional structure required, and an
  iterated `γ=1` chain lifts to the concatenated term list (law 2). The lift loses the
  pinned summation order (the L2 fold is order-agnostic), so the lift is value-faithful
  but NOT bit-faithful — re-lowering does not necessarily recover the original Palace
  call's order unless the table above is re-applied. This reverse-direction note lives
  here in working notes per the high→low layer-definition discipline; the formal chapter
  narrates only L2 → L1.

- **No dedicated test witness (inherited caveat, not a status reduction).** The L2 entry
  records that no unit test exercises the BLAS-1 linear-combination free functions (the
  `test-vector.cpp` "Vector Sum" tests exercise `linalg::Sum`, a different reduce-to-scalar
  fold). The selection rule is grounded by source-transcription + the live call sites, so
  the firm-without-dedicated-test bar (chebyshev-iteration precedent) carries through to
  this lowering theme unchanged. If a future cycle adds per-arity value-check tests, they
  would witness the selection rule's value-preservation directly.

- **Arity-≥4 chunking is a free choice (value), pinned choice (bits).** The selection
  rule consumes terms greedily three-at-the-head then two-per-accumulate-step. A different
  chunking (e.g. all `axpby` pairs) computes the same value (law 2) but a different
  bit-level result (the summation-order non-law). This theme records the **left-fold
  greedy-maximal** chunking as canonical because it matches the Palace `γ=1` iterated
  shape (`nleps.cpp`, `romoperator.cpp`); a downstream implementation free of a
  bit-reproduction requirement may chunk differently.

- **`inner_product` sibling fold (out of scope, forward-ref).** The L2 entry's
  `dot`-distinction §note points at OQ `inner-product-fold-sibling-candidate` (a separate
  reduce-to-scalar fold, axis = conjugation-convention, not arity). It has no
  linear-combination-style fixed-arity L1 family, so it gets its own (future) lowering
  theme, not this one. This cycle's combinator-miner-on-inner-product
  (`reports/2026-05-28T231046Z-combinator-miner-inner-product-fold/`) is the parallel
  track; this theme does not depend on it.
