---
layer: L4
operator: linear_combination
firmness: firm
edges:
  depends-on:
    - L3/linear_combination
  reference:
    - concepts/black-box-vs-accelerated-kernels
    - concepts/scalar-promotion
variant_axes:
  - arity (the UNIFICATION axis — not a remaining variant; recovered as term-list length; the scal/axpy/axpby/axpbypcz accelerated-kernel leaves are the bounded-arity readout labels, stopped low)
  - output-aliasing (in-place vs out-of-place; orthogonal to arity; pure/out-of-place at L4 as at L3; a below-L3 lowering concern)
  - element-type (real | complex; scalar-promotion sub-axis real ⊑ complex)
  - operand-category (tensor-operand | operator-operand; the operator-operand corner is the driven assemble_frequency_operator specialization — the next-pull L4 consumer that rides this combinator rising)
---

# linear_combination

The L4 **scalar-weighted-tensor-sum combinator**: a variadic fold over a list of
`(Scalar, Tensor[(S: ...)])` terms producing `Σᵢ aᵢ·tᵢ`, lifted to the top of the stack
as a **feature-surface verb the backend wants**. This is the BLAS-1 *combinator*
(NOT the fused per-arity accelerated kernels) that **rises to L4 regardless** of
how its specializations are disposed, per the
[`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
§"The combinators rise regardless": whichever disposition the `scal` / `axpy` /
`axpby` / `axpbypcz` fused leaves land in (case 3 — accelerated kernels stopped
low), the general combinator `linear_combination` rises in their place. The L4
form re-expresses **through** the firm L3 [`linear_combination`](../L3/linear_combination.md)
fold (replace-and-propagate, not a rectangular mirror); the four arity leaves are
**specialization notes** under it (§"Arity specializations"), tied below, not
co-equal L4 chapters.

## Context

L4 is **vocabulary, not architecture** (`L4/index.md:7-13`): it captures *what
operations happen* with their signatures and shape contracts, and is the
**backend-lowering target** — the feature surface whose semantics match the
external GPU-tensor backend. The deliberate L4-is-the-backend-lowering-target
framing (project memory `project_l4_is_backend_lowering_target`) is the reason
`linear_combination` rises even though it carries no *novel calculus structure*:
a scalar-weighted sum is a primitive the backend supplies directly, and the L4
surface must name it so every in-scope feature (assemble AND solve) can reach L4
written against the backend's verb set.

`linear_combination` is **not** an iteration-structural combinator like
[`iterate-while`](./iterate-while.md) / [`solve_family`](./solve_family.md) /
[`fold_solve`](./fold_solve.md). Those thread a `SimState` carry through a
stopping predicate or a schedule; `linear_combination` is a **pure
value-producing data-parallel reduction** over a *statically-known finite term
list* — no control-flow, no monadic `Solve` effect, no convergence predicate, no
carry-dependence between terms. It is the **data-algebra half** of the L4
vocabulary (alongside its sibling [`inner_product`](./inner_product.md)), the
half the iteration-structural combinators *consume* in their step bodies (e.g.
the GMRES basis-correction sum inside [`krylov-step`](./krylov-step.md)'s body,
`L4/krylov-step.md:67`, IS a `linear_combination` over scalar-weighted basis
terms).

**This supersedes the prior "no L4 entry" verdict.** The firm L3
[`linear_combination`](../L3/linear_combination.md) entry (and the L2 entry it
propagated from) records "no L4 entry — the fold is a pure value-producing
reduction… not a calculus combinator with monadic state-threading or a
convergence predicate" — the cycle-010 audit reading that *iteration-structural*
content is the L4 admission test. The 2026-06-01 VOCABULARY-SHIFT REDIRECT +
L4-is-the-backend-lowering-target framing (memory
`project_blackbox_vs_accelerated_kernels`, `project_l4_is_backend_lowering_target`)
**change the admission test**: L4 is the *feature surface*, and the data-algebra
combinators are feature-surface verbs the backend wants, so they rise regardless
of carrying iteration structure. The L3 entry's "no L4" lines are now **stale**
and are re-anchored to this entry by a follow-up lifter pass (flagged §"Downward
to L3" + the report's Open questions — not edited this cycle, out of dispatch
scope).

## Semantics (overlay)

The L4 calculus is specified in the strawman
[`../design/l4_calculus.md`](../design/l4_calculus.md). `linear_combination` is a
pure term-list fold; its L4 rendering uses the strawman's term/type BNF (§1) with
no reduction-rule extension (it adds no new evaluation rule — it is a fold
expressible in the existing `foldl` / `+` / `scal` vocabulary). Pseudo-language is
Haskell `::` signatures inside a `text` fence per the L4/L3 notation invariant.

## Signature

    -- entry point: the variadic scalar-weighted-tensor-sum combinator
    -- a pure fold over a finite (Scalar, Tensor[(S: ...)]) term list; no Solve monad, no carry
    linear_combination :: [(Scalar, Tensor[(S: ...)])] -> Tensor[$S]
    linear_combination pairs = foldl (\acc (a, t) -> acc + scal a t) (zeros $S) pairs

Shape contract (bunsen-style; named shape groups per [`l4_calculus`](../design/l4_calculus.md)
§1.2.1; identical to the firm L3 signature — the L4 form is value-thread-isomorphic
to it, §"Downward to L3"):

- `pairs` — `[(Scalar, Tensor[(S: ...)])]` — a finite list of (coefficient, term) pairs;
  list order is the fold's canonical evaluation order (the IEEE summation-order
  residue is a below-L3 lowering concern, not an L4 law — see §"Algebraic laws").
- each `tᵢ` — `Tensor[(S: ...)]` — **shape precondition**: all terms are *congruent*,
  sharing one shape group `S` of arbitrary, unknown rank (the name `S` carries the
  same-shape contract; `S` is **not** pinned to rank-1 — the combination is
  element-local at every position of `S`, see §"Algebraic laws"). The earlier
  `Tensor[N]` rendering accidentally read as a single length axis; `(S: ...)` states
  the congruence-of-unknown-rank intent directly.
- each `aᵢ` — `Scalar` — one shared element type `T ∈ {real, complex}` across all
  scalars and terms, with the `real ⊑ complex` promotion lattice from
  [`scalar-promotion`](../concepts/scalar-promotion.md) (promote all-or-none).
- result — `Tensor[$S]` — the same shape group `S`; `zeros $S` on the empty list.

The L4 calculus has no monadic effect on this combinator (contrast the
`Solve`-threaded iteration combinators): `linear_combination` is a plain
value-producing fold, threaded as a `let`-binding inside the bodies that consume
it. The discipline that coefficients flow in only is structural (the single
return slot is `Tensor[$S]`).

### Arity specializations (the family members, tied below as notes)

The four BLAS-1 arity forms are list-length specializations of this combinator —
**specialization notes, NOT co-equal L4 chapters** (vocabulary-shift redirect;
replace-and-propagate). Each is the combinator at a fixed term-list length:

    scal(α, x)                 = linear_combination [(α, x)]                 -- arity 1
    axpy(α, x, y)              = linear_combination [(α, x), (1, y)]         -- arity 2, second coeff fixed to 1
    axpby(α, x, β, y)          = linear_combination [(α, x), (β, y)]         -- arity 2, general
    axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)] -- arity 3

Per [`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
§3 (accelerated kernel — stopped low), these named BLAS routines lean toward
**fusion** (per-case judgment, leaning toward fusion): they are
performance-fused special cases of this combinator with no standalone abstraction
value, **identified low** (the L1/L0 fused calls) and tied to this combinator,
which **rises in their place**. They get no L4 chapter; this combinator does.
They remain useful as *readout labels* for the bounded-arity L0 call shapes —
exactly the role they carry in the firm L3 entry's §"Arity specializations".

## Algebraic laws

Carried up **unchanged** from the firm L3 [`linear_combination`](../L3/linear_combination.md)
(laws are statements about the operator's *value*, and the L4 form is
value-thread-isomorphic to the L3 fold — §"Downward to L3"). Reproduced for L4
layer-coherence (an L4 reader verifies them against the L4 signature without
reaching down):

1. **Empty-list identity (fold seed).** `linear_combination [] = zeros[$S]`.

2. **Concatenation-homomorphism (the defining law).**
   `linear_combination (a ++ b) = linear_combination a + linear_combination b`
   (element-wise tensor `+` on the right). This is what makes the four arities one
   combinator — `axpbypcz`'s 3-term list is the concatenation of an `axpby`
   2-term and a `scal` 1-term list. A monoid homomorphism from
   `([(Scalar,Tensor[(S: ...)])], ++, [])` to `(Tensor[$S], +, zeros)`.

3. **Multilinearity in the scalar list.** Linear separately in each `aᵢ` with all
   other terms fixed; combined with law 2, a multilinear function of the
   coefficient tuple (the variadic generalization of per-leaf bilinearity /
   trilinearity).

4. **Coefficient-scaling / scalar absorption.**
   `linear_combination ((κ·a, t):rest) = linear_combination ((a, κ·t):rest)`.

5. **Zero-coefficient term-drop.** `linear_combination ((0, t):rest) =
   linear_combination rest` — the algebraic content of the L0 `γ==0`
   arity-collapse branch.

6. **Specialization identities (derived).** Each arity leaf is the fixed-length
   instance (the four equations in §"Arity specializations"); the subsumption
   chain `scal ≺ axpy ≺ axpby ≺ axpbypcz` is the bounded-arity shadow of law 2.

7. **Permutation-invariance — EXACT-ARITHMETIC LAW.**
   `linear_combination (permute pairs) = linear_combination pairs` (tensor
   addition commutative + associative over an exact field). The `foldl`
   left-to-right order is the **canonical** order.

Laws that explicitly **do not** hold (all deferred to the lowering chain, NOT
restated as L4 laws):

- **Permutation-invariance under IEEE-754 (paired non-law).** The summation order
  is a load-bearing numerical concern (CLAUDE.md §"Optimization tricks vs. base
  algebra"); bit-identical reproduction of an L0 call requires matching its pinned
  summation order. Which order a lowered call pins is recorded by the L2>L1
  [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md)
  theme — it is NOT an L4 law of this combinator (it is the lowering theme's
  substantive numerical content). At L4 the value is order-agnostic; the backend
  supplies its own reduction order.
- **Bit-level fusion identity** against the multi-pass form — mathematically
  equal, load-bearing for bit-reproduction, recorded by the same lowering theme.

The L4 law set is **identical** to the L3 (and L2) combinator's set — structural,
because the rotation is identity-in-form on the combinator and laws about the
value are unchanged across it.

## Variant axes

1. **Arity** — the **unification axis** (NOT a remaining variant): recovered as
   term-list length; the four accelerated-kernel leaves are the bounded-arity
   readout labels, stopped low.
2. **Output-aliasing (in-place vs out-of-place)** — orthogonal to arity; pure /
   out-of-place at L4 (as at L3); the aliasing forms are a below-L3 lowering
   concern. The backend, as the lowering target, owns its own in-place/out-of-place
   buffer policy.
3. **Element-type** — `real | complex`, with the `real ⊑ complex` scalar-promotion
   sub-axis ([`scalar-promotion`](../concepts/scalar-promotion.md); carries the open
   `scalar-promotion-typing-rule` upstream dependency unchanged).
4. **Operand-category** — `tensor-operand | operator-operand`. The fold's operand
   monoid is parametric; the BLAS-1 cohort is the tensor-operand corner, and the
   **operator-operand corner** is the driven per-ω system-operator assembly
   `A(ω) = K + iω·C − ω²·M + A2(ω)` — the L1
   [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md)
   specialization (cycle-062). **This is the next-pull L4 consumer** that rides
   `linear_combination` rising: its L4 lift re-expresses *through* this present L4
   combinator (the cycle-068 planner sequenced it to c069 precisely because it is
   GATED on this entry existing on disk — OQ in the c068 plan §Open questions).

## Downward to L3

The L4 `linear_combination` combinator lowers to the firm L3
[`linear_combination`](../L3/linear_combination.md) as **identity-in-form on the
body**: the two forms are value-thread-isomorphic. Both layers see the same
signature `linear_combination :: [(Scalar, Tensor[(S: ...)])] -> Tensor[$S]`, the same
`foldl (\acc (a,t) -> acc + scal a t) (zeros $S) pairs` body, the same seven
algebraic laws, the same deferred IEEE non-law, and the same variant-axis profile.

**There is no dedicated L4>L3 theme file** — the identity-in-form annotation lives
in-line here, per the cycle-012 non-adjacent-identity / in-line-marker convention
(CLAUDE.md §Methodology invariants "Identity rotations across non-adjacent layers
are annotated in-line"). This is the **same in-line-marker route**
[`eigsolve`](./eigsolve.md) takes to its L3 form (L4>L3 by in-line marker-erasure,
no dedicated theme, `L4/index.md:39`/`:81`) and [`chebyshev`](./chebyshev.md)
takes (substantive at wrapper, identity-in-form on body, no L4-L3 theme file,
`L4/index.md:75`): there is **no monadic wrapper, no `Solve` monad, no
state-stratification record, no convergence predicate, no outer driver** to
dissolve across the L4>L3 edge — `linear_combination` is a pure value-producing
fold at both layers, so the rotation is the identity on the combinator body.
Creating an `L4-L3/linear-combination-*-dissolution.md` would be a **degenerate
identity-in-named-terms theme** (the §1d smell of the vocabulary-shift redirect:
LHS and RHS the same named combinator at the same arity with no vocabulary shift)
— so it is correctly an in-line note, not a theme file.

The **substantive** rotation in the downward chain is not this identity edge but
the L2>L1
[`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md)
fusion-selection theme (firm): it reads the fold's term-list length, selects the
maximal fused L0 leaf, and records the pinned summation order (the load-bearing
numerical residue). The transitive L4>L3>L2>L1 identity-then-fusion chain is the
composition of this in-line L4>L3 identity with the firm L3>L2 identity (the L3
entry's §"Downward to L2") and the substantive L2>L1 fusion-selection — annotated
in-line per the per-adjacent-edge directory convention (no `L4-L2`/`L4-L1`
directory).

**Staleness note (out of this cycle's edit scope):** the firm L3
[`linear_combination`](../L3/linear_combination.md) §"Lifts from" + frontmatter
`lifts_from` currently assert "no L4 entry". With this entry on disk those lines
are stale and should be re-anchored to point up here (a thin lifter/lowering-verifier
re-anchor pass, the same routine `eigsolve` triggered for the seven stale
`L3/eigsolve` §Upward "no L4 cap" assertions, `L4/index.md:81`). Flagged in the
report's Open questions; not edited this dispatch (one-operator-per-dispatch +
the L3 entry is outside this report's write-scope).

## Sibling combinator (do NOT merge)

The reduce-to-scalar [`inner_product`](./inner_product.md) (this cycle's sibling
L4 entry) is a **different** fold — reduce-to-`Scalar`, not scalar-weighted-tensor
sum. Its result type is `Scalar`, not `Tensor[$S]`; it reduces over the shape
group `S` (a shape-concatenation homomorphism to `(Scalar, +)`), whereas
`linear_combination` is element-local over `S` and folds over the *term list*
(a term-list concatenation homomorphism to `(Tensor[$S], +)`). Its combining step
is zip-and-reduce-over-`S`; this combinator's is scale-and-accumulate-over-the-
term-list. The two are the small **algebra of folds** at L4 — one
tensor-producing, one scalar-producing — deliberately **NOT merged** (the
over-unification guard, symmetric in both entries). The do-NOT-merge boundary is
load-bearing and is carried identically at L2/L3/L4.

## Status

`firm` — the L4 form is the calculus-level rendering of the firm L3
[`linear_combination`](../L3/linear_combination.md) combinator (firm cycle-050,
propagated from the firm L2 entry cycle-018 / inverted-to-entry cycle-049 D1):
the same variadic whole-tensor `[(Scalar, Tensor[(S: ...)])] -> Tensor[$S]` fold,
value-thread-isomorphic across the L4>L3 edge (identity-in-form on the body; no
monadic wrapper to dissolve — §"Downward to L3"). The seven algebraic laws are
carried up unchanged (each a syntactic identity or a standard linear-combination
fact); the IEEE-754 summation-order non-law is deferred to the firm L2>L1
fusion-selection theme (NOT restated as an L4 law); the variant-axis profile is
closed (arity = the unification axis; output-aliasing + element-type +
operand-category orthogonal). It carries **no first-class L4 calculus structure of
its own** (no `Solve` monad, no iteration carry) — it rises as a **feature-surface
verb the backend wants** per the
[`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
§"The combinators rise regardless" + L4-is-the-backend-lowering-target framing,
NOT because it carries iteration structure. The L0 anchors are **inherited
transitively through the firm L3/L2 combinator** (self-verified at L2 cycle-018),
not re-localized this pass — this is an upward in-layer rendering, not a fresh
family discovery. The empirical-match caveat is inherited unchanged from L2 (no
dedicated unit test for the BLAS-1 linear-combination free functions; grounded by
source-transcription + verified live call sites + the `chebyshev`-precedent
firm-without-dedicated-test bar); the missing test does not gate firm because
every L4 law is a syntactic identity carried up from the firm combinator below
(the firm-on-positive-structure / syntactic-identity escape).

## Evidence

L2 / L3 endpoints (firm; the value-isomorphism this L4 entry rests on):

- `book/src/L3/linear_combination.md` (firm cycle-050) — the firm L3 fold this L4
  entry re-expresses through: signature (`:36-37`), the §"Arity specializations"
  notes (`:51-62`), the seven algebraic laws + deferred IEEE non-law (`:80-104`),
  the §"Downward to L2" identity-in-form note (`:108-114`), variant axes
  (`:133-141`), the firm-without-dedicated-test caveat (`:152`).
- `book/src/L2/linear_combination.md` (firm cycle-018; inverted-to-entry cycle-049
  D1, commit `92327f7`) — the original combinator inversion; authoritative on the
  self-verified L0 evidence list (inherited transitively here).
- `book/src/L2-L1/linear-combination-fold-specialization.md` (firm; cycle-049
  D1(c) KEEP) — the substantive L2>L1 fusion-selection theme: arity-dispatch +
  the pinned-summation-order table (the load-bearing IEEE residue deferred there).

Classification / methodology anchors:

- `book/src/concepts/black-box-vs-accelerated-kernels.md` (cycle-067 D3) — the
  three-way disposition: §"The combinators rise regardless" (`:128-136`) names
  `linear_combination` as the combinator that rises to L4 regardless; §3
  "Accelerated kernel — stopped low" (`:111-126`) names the `scal`/`axpy`/`axpby`/
  `axpbypcz` family as the stopped-low accelerated-kernel candidates this
  combinator rises in place of.
- `skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md` — the
  combinator-mining gate; this rise is **propagation of an already-firm mined
  combinator** (the c049 mine + c050 L3 propagation), so the 4 gate points are
  satisfied by the firm L3 endpoint, not re-mined here (the gate is for *new*
  mines; this is an upward in-layer rendering of a settled one).
- `book/src/design/l4_calculus.md` — the strawman; this combinator adds no
  reduction rule (a fold in the existing `foldl`/`+`/`scal` vocabulary).

Provenance: combinator-miner:2026-06-02T195402Z (cycle-068 D3) — the
`linear-combination-inner-product-rise-to-l4` plan-tag enactment; rises the firm
L3 combinator to L4 as the directive-2 disposition-2 / L4-is-the-backend-lowering-
target feature-surface verb.
