---
layer: L3
operator: linear_combination
rank: firm
edges:
  depends-on:
    - L2/linear_combination
  reference:
    - L4/linear_combination
    - L2-L1/linear-combination-fold-specialization
variant_axes:
  - arity (the UNIFICATION axis — not a remaining variant; recovered as term-list length)
  - output-aliasing (in-place vs out-of-place; orthogonal to arity; an L3>L2>L1 lowering concern, pure/out-of-place at L3)
  - element-type (real | complex)
  - scalar-promotion (sub-axis on the complex element-type; real ⊑ complex, inherited from concepts/scalar-promotion)
  - operand-category (tensor-operand | operator-operand; the operator-operand corner witnessed by BuildParSumOperator, driven specialization assemble_frequency_operator c062 — replace-and-propagate, not a mirrored fold)
---

# linear_combination

The L3 (iteration-rotation layer) rendering of the firm L2 scalar-weighted-tensor-sum fold combinator: a **whole-tensor variadic fold** over a list of `(Scalar, Tensor[(S: ...)])` terms, producing `Σᵢ aᵢ·tᵢ`. The L3-native form of the BLAS-1 linear-combination family — the same combinator that is firm at L2 ([`linear_combination`](../L2/linear_combination.md)), surfaced here in L3 vocabulary because **each layer is internally coherent** (CLAUDE.md §Methodology invariants). At L3 and above the four arity forms `scal` / `axpy` / `axpby` / `axpbypcz` speak **through** this combinator (as list-length specialization notes), not as re-derived base forms — the propagate half of the cycle-049 replace-and-propagate map (vocabulary-shift redirect 2026-06-01).

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as whole-tensor primitives, no element loops, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `linear_combination` at L3 is the whole-tensor variadic fold that the BLAS-1 scalar-weighted-sum cohort unifies — the L3 analog of the L2 combinator, carried up under the redirect's **replace-and-propagate** discipline so that the family speaks through one combinator at L3 rather than re-deriving four separate base forms.

The L3 form is **value-thread-isomorphic to the L2 form**: the L2 combinator's signature is already whole-tensor in / whole-tensor out over a term list (`[(Scalar, Tensor[(S: ...)])] -> Tensor[$S]`), with no element loop exposed at the layer's vocabulary. The L3 layer's vocabulary requirement — whole-tensor primitives, no element loops — is satisfied by the L2 signature shape directly. The relationship to the lower layer is therefore the identity rotation on the combinator itself (see §"Downward to L2"); the per-element semantics (`result[idx] = Σⱼ aⱼ·tⱼ[idx]` for every multi-index `idx` of `S`) is the **referent**, not the L3 surface — the L3 surface is the whole-tensor fold signature, which is already L3-native.

This entry is the **propagate half** of the cycle-049 D1 replace-and-propagate map (`reports/2026-06-01T190900Z-combinator-miner-refactor-pass-linear-combination-family/CYCLE.md` (b.3)): cycle-049 D1 inverted the L2 entry to combinator-as-entry (the four arity leaves became specialization notes under it) but did not propagate to L3; this entry is the L3 analog. The four L3 leaf chapters (`L3/{scal,axpy,axpby,axpbypcz}.md`) were re-expressed through this combinator cycle-051 (D2) and **reduced to specialization-stubs cycle-052** (D2) under the `collapsed-leaf-disposition-convention-cohort-wide` convention (reduce-to-stub, files KEPT on disk so inbound links stay live): each is the arity-1/2/2/3 readout label pointing up to this combinator, with its body collapsed into the §"Arity specializations" notes here. This combinator IS the L3 family entry.

The combinator is data-parallel, not iteration-structural: `linear_combination` is a pure value-producing reduction over a term list, with no control-flow, no monadic state threading, and no convergence predicate (contrast L4 `iterate_while`, which threads state through a stopping predicate). It lifts to [`L4/linear_combination`](../L4/linear_combination.md) (firm cycle-068) **identity-in-form on the body** — the L4 calculus combinator is value-thread-isomorphic to this L3 fold, with no dedicated L4>L3 theme file (the eigsolve/chebyshev in-line-marker route), precisely because there is no monadic state-threading or convergence predicate to dissolve across the edge. The combinator belongs with the tensor algebra at L3, alongside the BLAS-1 cohort, and rises to L4 as the calculus-level rendering of that same fold.

The sibling reduction `dot` / `inner_product` is a **different** fold — reduce-to-`Scalar`, not scalar-weighted-tensor-sum — and is deliberately NOT merged (see §"Sibling fold").

## Signature

```text
linear_combination :: [(Scalar, Tensor[(S: ...)])] -> Tensor[$S]
linear_combination pairs = foldl (\acc (a, t) -> acc + scal a t) (zeros $S) pairs
```

Positional value-threading; no monadic effect (L3 has no `Solve` monad), no record-typing.

Shape contract (bunsen-style; named shape groups per [`l4_calculus`](../design/l4_calculus.md) §1.2.1):

- `pairs` — `[(Scalar, Tensor[(S: ...)])]` — a finite list of (coefficient, term) pairs. Order is the fold's evaluation order (see §"Algebraic laws", permutation law/non-law pair).
- each `tᵢ` — `Tensor[(S: ...)]` — **shape precondition**: all terms are *congruent*, sharing one shape group `S` of arbitrary (unknown) rank; the combination is element-local at every position of `S`. (The general named-shape-group convention is in [`l4_calculus`](../design/l4_calculus.md) §1.2.1, linked above.)
- each `aᵢ` — `Scalar` — element type one shared `T ∈ {real, complex}` across all scalars and all terms, with the `real ⊑ complex` scalar-promotion lattice inherited unchanged from [`scalar-promotion`](../concepts/scalar-promotion.md) (promote all-or-none across the scalar list).
- result — `Tensor[$S]` — same shape group `S`; `zeros[$S]` on the empty list.

The L3 calculus has no record-typing and no `readonly` annotation; the signature is positional. The discipline that the coefficients flow in only (never out) is structural (the return position has only one slot, of type `Tensor[$S]`).

### Arity specializations (the family members, as notes under the combinator)

The four arity forms are list-length specializations of the combinator — **specialization notes, not standalone L3 chapters under this combinator's algebra** (vocabulary-shift redirect). Each is the combinator at a fixed term-list length:

```text
scal(α, x)                 = linear_combination [(α, x)]                 -- arity 1
axpy(α, x, y)              = linear_combination [(α, x), (1, y)]         -- arity 2, second coeff fixed to 1
axpby(α, x, β, y)          = linear_combination [(α, x), (β, y)]         -- arity 2, general
axpbypcz(α, x, β, y, γ, z) = linear_combination [(α, x), (β, y), (γ, z)] -- arity 3
```

These names remain useful as *readout labels* for the bounded-arity L0 call shapes. They are NOT separate L3 operators with their own algebra — every law below is the combinator's; the per-arity facts (`axpby` bilinearity, `axpbypcz` trilinearity, etc.) are the multilinearity law (law 3) read at a fixed list length. **The L3 leaf chapters `L3/{scal,axpy,axpby,axpbypcz}.md` were reduced to specialization-stubs cycle-052** (reduce-to-stub, files KEPT on disk) — each defers its semantics / laws to these notes and points up to this combinator. The L3 form differs from the four leaf readout labels only in **resolution**, along the arity axis: the leaves see four distinct fixed-arity operators; this combinator sees one variadic fold whose list length recovers each fixed arity.

## Semantics

`linear_combination` accumulates a running tensor sum: starting from the zero tensor of shape group `S`, it folds left over the term list, adding each scaled term `aᵢ·tᵢ` into the accumulator. The result is the tensor `Σᵢ aᵢ·tᵢ` (the linear combination of the terms with the paired coefficients).

It is **pure / out-of-place at L3**: it consumes the coefficient/term list and produces a fresh tensor; no destination buffer appears in the signature. The L0 in-place idioms (the receiver-mutating / output-arg forms where one term's tensor aliases the output buffer) are an L3>L2 (and onward L2>L1>L0) lowering concern, captured by the output-aliasing variant axis below — not by the L3 algebra. (The substantive in-place mutation rotation is the L1>L0 `axpby-mutation-rotation` and siblings, reached transitively through the L2>L1 fusion-selection theme.)

Each accumulate step is **element-local and reduction-free over `S`** (every output position `result[idx] = Σⱼ aⱼ·tⱼ[idx]` for every multi-index `idx` of `S` depends only on position `idx` of each term). The fold's sequencing is over the **term list**, not over `S` — there is no cross-element communication and no MPI collective (terms are rank-local; ranks own disjoint slices of `S`). Contrast `dot` / `nrm2`, which reduce over `S` and do carry an MPI collective.

**The operator carries no sequential obstruction.** The fold is over the **term list** (a fixed, finite, statically-known list of `(Scalar, Tensor[(S: ...)])` pairs — typically length 1–3, recovering the bounded-arity L0 family), and each fold step is element-local over `S`. There is no loop-carried recurrence over the field axis, no convergence predicate, no inter-element communication: the entire combination is `result[idx] = Σⱼ aⱼ·tⱼ[idx]` at every multi-index `idx` of `S` independently. The term-list fold is a finite static unrolling, not an iteration over a trajectory — so the L3 iteration-rotation marker (per [`sequential-obstruction`](../concepts/sequential-obstruction.md)) does not apply, exactly as it does not apply to the individual BLAS-1 leaves (the cohort obstruction-free precedent, `L3/axpy.md` §"Specialization": the operator carries no sequential obstruction — there is no fold over `axpy`'s output to invoke). This combinator is the obstruction-free fold over the cohort's terms; the obstruction (where it exists) lives at the *consuming* compositions (the outer `iterate_while_L3` loop folding `krylov-step`, whose iterate-stratum update is itself a `linear_combination` over basis-correction terms — see §"Dependencies").

Palace's L0 surface stops at arity 3 (`AXPBYPCZ`; there is no `AXPBYPCZPDW`). Combinations of more than three terms are realized in Palace as **iterated** `axpbypcz`-into-output with the aliased coefficient fixed to 1 (the `γ=1` accumulation sites). The variadic `linear_combination` is therefore the L3 (and L2) abstraction the bounded-arity L0 family approximates; this is the correct generalization direction, not scope creep (per CLAUDE.md — the higher form may inform extensions Palace open-codes as accumulation loops).

### Iteration-rotation marker

L3 is the iteration-rotation layer, but `linear_combination` is a **finite term-list fold** with no iteration view of its own — it is a single whole-tensor reduction over a statically-known term list, not a fold over a trajectory with a carry/successor relation. The iteration view applies to compositions that *consume* `linear_combination` (notably `krylov-step`'s iterate-stratum update, where the GMRES basis-correction sum is exactly a `linear_combination` over scalar-weighted basis terms — the unfolding of GMRES basis-correction sums into axpy chains, this combinator's law 6 specialization-identities read at term-list length 2; that unfolding IS a `linear_combination`). At the fold itself, there is no iteration carry, no successor relation over the field axis. The L3 layer-coherence reason for this entry is **vocabulary inventory + family unification**, not iteration-view content.

## Algebraic laws

Carried up from the L2 combinator (per the identity-in-form rotation across the L3>L2 edge). The laws below hold at L3 because they hold at L2 and the L3 form is value-thread-isomorphic to the L2 form (the laws are statements about the operator's value, not about its surface; the surface rewrite is a no-op on the value). The laws below hold; absences are deliberate.

1. **Empty-list identity (the fold's seed).** `linear_combination [] = zeros[$S]` — the additive identity of `Tensor[$S]`. This is the fold's initial accumulator.

2. **Concatenation-homomorphism (the defining law).** `linear_combination (a ++ b) = linear_combination a + linear_combination b`, where `+` on the right is element-wise tensor addition. **This is the law that makes the four arities one operator**: `axpbypcz`'s 3-term list is the concatenation of an `axpby` 2-term list and a `scal` 1-term list. It is a monoid homomorphism from `([(Scalar,Tensor[(S: ...)])], ++, [])` to `(Tensor[$S], +, zeros)`.

3. **Multilinearity in the scalar list.** `linear_combination` is linear separately in each coefficient `aᵢ` with all other terms held fixed: `linear_combination ((a₁+a₂, t):rest) = a₁·t + a₂·t + linear_combination rest`, and (combined with law 2) `linear_combination` is a multilinear function of the coefficient tuple. This is the variadic generalization of the per-leaf bilinearity / trilinearity (the L3 `axpby` / `axpbypcz` linearity laws, read at a fixed list length).

4. **Coefficient-scaling / scalar absorption.** `linear_combination ((κ·a, t):rest) = linear_combination ((a, κ·t):rest)` — each coefficient absorbs into its paired term.

5. **Zero-coefficient term-drop.** `linear_combination ((0, t):rest) = linear_combination rest` for any term `t` — a term with zero coefficient drops from the combination (its contribution is the zero tensor). This is the **exact algebraic content of the L0 `γ==0` arity-collapse branch** (inherited from the L2 combinator's law 5; the source site `vector.cpp:749-751` is cited by inheritance, not re-localized — see §Evidence). It generalizes the per-leaf identity laws.

6. **Specialization identities (derived).** Each L3 leaf is the fixed-arity instance: `scal(α,x) = linear_combination [(α,x)]`; `axpy(α,x,y) = linear_combination [(α,x),(1,y)]`; `axpby(α,x,β,y) = linear_combination [(α,x),(β,y)]`; `axpbypcz(α,x,β,y,γ,z) = linear_combination [(α,x),(β,y),(γ,z)]`. These follow from law 2 (concatenation) plus the L3 leaves' own definitions; the subsumption chain `scal ≺ axpy ≺ axpby ≺ axpbypcz` recorded across the L3 entries is the bounded-arity shadow of the concatenation law.

7. **Permutation-invariance — EXACT-ARITHMETIC LAW.** In exact arithmetic, `linear_combination` is invariant under permutation of the term list: `linear_combination (permute pairs) = linear_combination pairs` (tensor addition is commutative and associative over an exact field). The `foldl` left-to-right order is the **canonical** order this L3 form names.

Laws that explicitly **do not** hold:

- **Permutation-invariance under IEEE-754 (paired non-law) — DEFERRED to the L2>L1 lowering theme, not restated here as an L3 law.** The exact-arithmetic permutation law (law 7) does NOT hold bit-for-bit in floating-point: the summation order is a **load-bearing numerical concern** (per CLAUDE.md "load-bearing numerical tricks… non-associative reduction orderings… preserve as explicit algebraic claims"). The L3 algebra is order-agnostic for value, but bit-identical reproduction of any L0 call requires matching that call's pinned summation order; **which order a given lowered call pins is recorded by the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) theme** (its pinned-summation-order table — the load-bearing residue this entry, like the L2 entry, defers there per the cycle-049 D1(c) KEEP verdict). It is NOT an L3 law of this combinator; it is the lowering theme's substantive numerical content.

- **Idempotence of re-folding.** `linear_combination` over a singleton list is `scal`, which is not idempotent in general; there is no fold-level idempotence to claim.

- **Bit-level fusion identity against the multi-pass form.** `linear_combination [(α,x),(β,y),(γ,z)]` computed as one fused pass is not bit-identical to the three-pass `scal(α,x) + scal(β,y) + scal(γ,z)` chain (the multi-pass form rounds more times). Mathematically equal; the L0 fusion choice is load-bearing for bit-reproduction, transparent for value (recorded, again, by the L2>L1 fusion-selection theme, not as an L3 law).

The algebraic-law set at L3 is **identical** to the L2 combinator's law set (laws 1–7 + the deferred non-laws). This is structural: the rotation is identity-in-form on the combinator; laws about the combinator's value are unchanged across the rotation. Stating the laws at L3 is the layer-coherence invariant — an L3 reader can verify the laws against the L3 signature without reaching down to L2.

## Downward to L2

The L3 `linear_combination` fold lowers to the firm L2 [`linear_combination`](../L2/linear_combination.md) as **identity-in-form on the combinator's body**: the L3 whole-tensor fold and the L2 fold are value-thread-isomorphic. Both layers see the same signature `linear_combination :: [(Scalar, Tensor[(S: ...)])] -> Tensor[$S]`, the same `foldl (\acc (a,t) -> acc + scal a t) (zeros $S) pairs` body, the same seven algebraic laws, the same deferred IEEE non-law, and the same variant-axis profile. There is no `(op, K, s)`→`IterState` consolidation and no outer-loop dissolution to perform (the surface adjustments the `krylov-step` body-identity theme carries at its wrapper) — `linear_combination` is a pure value-producing fold, not a step body with a state carrier or an outer driver. The body IS the identity across the L3>L2 edge.

This identity is the family-entry analog of the four `{scal,axpy,axpby,axpbypcz}-body-identity` L3>L2 themes — each of which recorded the same "the body IS the identity, no wrapper rotation" verdict for its individual arity leaf. Under the cycle-049 replace-and-propagate map (b.2), those four thin per-leaf themes were degenerate identity-in-named-terms smells (the §1d smell — the vocabulary did not shift, LHS and RHS being the same named operator at the same arity); they were **demoted cycle-051 D1** into this single §"Downward to L2" combinator-identity note, with the four L3 leaves (`L3/{scal,axpy,axpby,axpbypcz}.md`) re-expressed to speak through this combinator as arity-1/2/2/3 specializations. This note is the home for the four leaf-edge identities, which are the concatenation-law specializations of this one combinator identity (the arity-1/2/2/3 readings of `linear_combination`'s body-identity).

The **substantive** rotation in the downward chain is NOT this identity edge but the L2>L1 [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md) fusion-selection theme (firm; cycle-049 D1(c) KEEP verdict): it reads the fold's term-list *length* and selects the maximal fused L0 leaf (length 1→`scal`, 2→`axpy`/`axpby`, 3→`axpbypcz`, ≥4→iterated `axpbypcz`-into-output chain — the unbounded→bounded de-fusion), and records the pinned summation order each lowered call carries (the load-bearing numerical content this entry defers there). The transitive L3>L1 identity (this L3>L2 combinator identity ∘ the L2>L1 fusion-selection's value-identity) is annotated in-line per the cycle-012 non-adjacent-identity convention (lowering directories are per-adjacent-edge only; no `book/src/L3-L1/` directory is created).

## Dependencies

**Same-layer (L3)**: this combinator unifies the four L3 BLAS-1 linear-update leaves [`scal`](./scal.md) (arity 1), [`axpy`](./axpy.md) (arity 2, second coeff 1), [`axpby`](./axpby.md) (arity 2), [`axpbypcz`](./axpbypcz.md) (arity 3) as list-length specializations (law 6). These four leaf chapters were re-expressed through this combinator cycle-051 and reduced to specialization-stubs cycle-052 (reduce-to-stub, files KEPT on disk) — each defers to the §"Arity specializations" notes here. The composition surfaces that *consume* `linear_combination` at L3 are the iterate-stratum update inside [`krylov-step`](./krylov-step.md)'s `krylov_update` (the GMRES basis-correction sum is a `linear_combination` over scalar-weighted basis terms).

**Cross-cutting concepts** (consumed unchanged across the chain):

- [`scalar-promotion`](../concepts/scalar-promotion.md) — the `real ⊑ complex` typing rule for scalar promotion on the complex element-type. Inherited from L2 verbatim; promote all-or-none across the scalar list. Carries its open upstream dependency unchanged (closure depends on the L1 calculus adopting the `real ⊑ complex` lattice — OQ `scalar-promotion-typing-rule`, not yet committed; `concepts/scalar-promotion.md:49`).
- [`tensor-field-lift`](../concepts/tensor-field-lift.md) — the methodology concept underwriting the L3-native-by-signature-shape claim for the BLAS-1 cohort, applied here to the fold over the cohort's terms.

**Upward (L2)**: the firm L2 [`linear_combination`](../L2/linear_combination.md) combinator (cycle-018, inverted-to-entry cycle-049 D1) — the body this L3 entry is value-thread-isomorphic to (§"Downward to L2").

**Sibling fold (do NOT merge)**: the reduce-to-scalar `inner_product` (L3 rough-in `book/src/L3/index.md:29`; sibling D2's cohort — plain-text reference, chapter not yet on disk) — see §"Sibling fold".

## Sibling fold: dot / inner_product is not subsumed

`inner_product :: Tensor[(S: ...)] -> Tensor[$S] -> Scalar` (the L3 analog of the L2 `inner_product` combinator, capturing `dot` / `tdot` as conjugation-convention variants) is a **different** fold — a **reduce-to-scalar** inner product, NOT a scalar-weighted **tensor** sum. Its result type is `Scalar`, not `Tensor[$S]`; it reduces over the shape group `S` (and carries an MPI collective), whereas `linear_combination` is element-local over `S` and folds over the term list. Its combining step is zip-and-reduce-over-`S`; this combinator's is scale-and-accumulate-over-the-term-list. Its laws are symmetry / Hermitian-symmetry / positive-semi-definiteness, which have no analogue here. The two are the small **algebra of folds** — one tensor-producing (`linear_combination`), one scalar-producing (`inner_product`) — deliberately **NOT merged** into one mega-combinator. The do-NOT-merge boundary is load-bearing and symmetric, recorded here and (when the L3 `inner_product` entry firms — sibling D2's propagation) in its §"Sibling fold". (`inner_product` is currently a rough-in row in `book/src/L3/index.md:29`; the reference here is plain-text — the chapter is not yet on disk; upgrade to a live link once it lands.)

## Variant axes

`linear_combination` has the following variant axes; the **arity** axis is the one this operator unifies (it is NOT a remaining variant — it is the unification axis), so the remaining axes are orthogonal to it:

1. **Output aliasing (in-place vs out-of-place)** — the in-place forms (`y ← α·x + β·y`, `z ← α·x + β·y + γ·z`) are the case where one term's tensor `tᵢ` **aliases the output buffer**. Orthogonal to arity: every arity ≥ 1 has both an aliasing form and a fresh-output form. At L3 the fold is pure / out-of-place; aliasing is an L3>L2>L1 lowering concern, NOT an arity axis. (Aliasing is congruent over `S` — the aliased term and output share the shape group.)
2. **Element-type** — `real | complex`, with the `real ⊑ complex` scalar-promotion sub-axis ([`scalar-promotion`](../concepts/scalar-promotion.md)). Inherited unchanged from the L2 combinator; promote all-or-none across the scalar list. Carries the open `scalar-promotion-typing-rule` upstream dependency unchanged.
3. **Operand-category** — `tensor-operand | operator-operand`. The fold's operand monoid is parametric: the BLAS-1 cohort is the **tensor-operand** corner; the **operator-operand** corner is the same fold over `LinearOperator[N, N]` operands under operator-addition + scalar-operator-scaling, witnessed by Palace's `BuildParSumOperator` (`palace/linalg/rap.cpp:764-787`). The driven per-ω system-operator assembly `A(ω) = K + iω·C − ω²·M + A2(ω)` is the L1 operator-operand specialization [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md) (cycle-062). The zero-coefficient term-drop law holds verbatim (the `coeff[i] != 0` guard is the operator-domain `γ==0` collapse). Replace-and-propagate extension (2026-06-01 anti-mirror discipline), NOT a mirrored fold.

**Fusion order (an L0 implementation detail, NOT an L3 variant axis)**: single aligned pass vs multi-call split — transparent for value, load-bearing for bit-reproduction. This is the L2>L1>L0 realization of the fold's seed-and-accumulate; recorded in the L2>L1 fusion-selection theme, not as an L3 axis.

## L3 vs L2 distinction

- **L2** (fusion-rotation layer): the variadic fold `linear_combination` over `[(Scalar, Tensor[(S: ...)])]`; the layer where Palace's distinct fixed-arity call shapes (`operator*=` / `AXPY` / `AXPBY` / `AXPBYPCZ`, each a kernel-fusion choice) are unfolded into the canonical multi-term combination, the single aligned pass de-fused into the fold's seed-and-accumulate.
- **L3** (iteration-rotation layer): the same variadic fold, rendered as a whole-tensor field operation; value-thread-isomorphic to the L2 fold because the L2 signature is already whole-tensor / no-element-loop. The L3 entry exists for layer-coherence + family unification — an L3 reader finds the combinator defined in L3 vocabulary, and the four BLAS-1 leaves speak through it rather than re-deriving four base forms. The fold carries **no sequential obstruction** (the term-list fold is finite and static; each step is element-local over `S`).

The two layers' entries share the algebraic-law set, the variant-axis profile, the referent semantics, and the cited (inherited) L0 evidence. They differ in **layer-coherence framing**: L2 frames the combinator as the fusion-rotation unfolding of Palace's fixed-arity call shapes; L3 frames it as a whole-tensor field-operation fold at the iteration-rotation layer. The body of the combinator is the identity rotation across this edge.

## Status

`firm` — the L3 whole-tensor variadic-fold signature is canonical at L3 (value-thread-isomorphic to the firm L2 combinator); the seven algebraic laws are carried up unchanged from the firm L2 entry (each is a syntactic identity or a standard linear-combination fact); the IEEE-754 summation-order non-law is deferred to the firm L2>L1 fusion-selection theme per the cycle-049 D1(c) KEEP verdict (NOT restated as an L3 law); the combinator carries **no sequential obstruction** (finite static term-list fold, element-local over `S` — the obstruction-free profile shared with the BLAS-1 leaf cohort, `L3/axpy.md` §"Specialization"); the variant-axis profile is closed (arity = the unification axis; output-aliasing + element-type orthogonal). The L0 anchors are **inherited from the firm L2 combinator** (cited there as self-verified at cycle-018), not re-localized this pass — this is the propagate half of the replace-and-propagate map, an in-layer rendering, not a fresh family discovery. The empirical-match caveat is inherited unchanged from L2 (no dedicated unit test for the BLAS-1 linear-combination free functions; grounded by source-transcription + verified live call sites + the `chebyshev`-precedent firm-without-dedicated-test bar; `L2/linear_combination.md:317-329`); the missing test does not gate firm because every L3 law is a syntactic identity carried up from the firm L2 combinator.

## Lifts from

This L3 fold lifts to [`L4/linear_combination`](../L4/linear_combination.md) (firm cycle-068) — the calculus-level rendering of the same variadic whole-tensor `[(Scalar, Tensor[(S: ...)])] -> Tensor[$S]` fold. The lift is **identity-in-form on the body**: the L4 combinator is value-thread-isomorphic to this L3 entry (same signature, same `foldl (\acc (a,t) -> acc + scal a t) (zeros $S)` body, same seven laws, same deferred IEEE non-law). There is **no dedicated L4>L3 theme file** — the identity-in-form annotation lives in-line in the L4 entry's §"Downward to L3", per the cycle-012 non-adjacent-identity / in-line-marker convention (the same route [`L4/eigsolve`](../L4/eigsolve.md) and [`L4/chebyshev`](../L4/chebyshev.md) take to their L3 forms): there is no monadic state-threading, no `Solve` monad, and no convergence predicate to dissolve across the edge, so the fold rises unchanged.

> **Superseded admission.** Earlier revisions of this entry asserted "no L4 entry exists" on the pre-2026-06-01 reasoning that the fold "is not a calculus combinator" — that admission is **superseded** by the c068 `L4/linear_combination` landing and the 2026-06-01 vocabulary-shift redirect (`METHODOLOGY-REDIRECT.md` §4-§5; CLAUDE.md §Methodology invariants ⟢), under which the combinator IS first-class L4 vocabulary that rises to the feature surface as a named verb. The fold's members still also appear inside other L4 operator bodies as let-bindings (e.g. `axpy` / `axpby` / `axpbypcz` inside `krylov-step`'s body, `L4/krylov-step.md:67`); a future L4-propagation pass (cycle-049 D1 (b.4), low-priority — flag, don't force) may re-express the krylov-step update group through `linear_combination` (the GMRES correction sum is exactly a scalar-weighted term-list).

## Evidence

L2 / L3 anchors (firm endpoints; the value-isomorphism this entry rests on):

- `book/src/L2/linear_combination.md` (cycle-018 firm; inverted-to-entry cycle-049 D1 / commit `92327f7`) — the L2 combinator this L3 entry is value-thread-isomorphic to: signature (`:56-57`), the §"Arity specializations" notes (`:74-99`), the seven algebraic laws + the deferred IEEE non-law (`:132-211`), the dependencies + forthcoming-theme forward-reference (`:213-238`), variant axes (`:240-267`), the firm-without-dedicated-test caveat (`:317-329`).
- `book/src/L3/axpy.md` (cycle-011 firm; reduced to an arity-2 specialization-stub cycle-052 D2) — the representative L3 BLAS-1 leaf: the L3-layer conventions this entry follows, the "value-thread-isomorphic" identity-in-form framing (§ chapter intro), the **no-sequential-obstruction** precedent for the cohort (§"Specialization"), and law 6 naming the GMRES-correction-sum unfolding as a `linear_combination` (now deferred to this combinator's §"Algebraic laws" law 6 — the consuming-composition hook).
- `book/src/L3-L2/axpy-body-identity.md` (cycle-043 firm) — the per-leaf "the body IS the identity, no wrapper rotation" theme (`:3-14`) that the §"Downward to L2" note is written to accommodate the cycle-051 demotion of (one of the four `*-body-identity` themes).
- `book/src/L2-L1/linear-combination-fold-specialization.md` (firm; cycle-049 D1(c) KEEP verdict) — the substantive L2>L1 fusion-selection theme: arity-dispatch (length→maximal fused L0 leaf), the `γ==0` fall-through, and **the pinned-summation-order table** (the load-bearing IEEE residue this entry defers there, not restating as an L3 law).
- `book/src/L3/index.md:29` — the sibling-fold `inner_product` L3 rough-in row (the propagation-pattern precedent this `linear_combination` row mirrors); `:58` — the BLAS-1-cohort no-obstruction confirmation carried in the §Working-Notes narrative.

L0 source ranges (**inherited via the firm L2 combinator; NOT re-localized this refactor-pass** — the propagate half is an in-layer rendering, L0 evidence transitive through the firm L2 entry where it was self-verified at cycle-018; paths relative to `reference/palace/`):

- `palace/linalg/vector.cpp:702-712` — free-function `AXPY(double, Vector, Vector)` with the `α == 1.0` fast-path (the arity-2-coeff-1 `axpy` leaf).
- `palace/linalg/vector.cpp:726-730` — `AXPBY` → MFEM 5-arg `add(alpha, x, beta, y, y)` single aligned in-place linear-combine (the arity-2 fusion witness).
- `palace/linalg/vector.cpp:745-758` — the `AXPBYPCZ` real-real body including the `γ == 0` arity-collapse branch (`:749-751`, `add(alpha, x, beta, y, z)`) — exact algebraic content of law 5 (zero-coefficient term-drop).
- `palace/linalg/vector.hpp:305-316` — the free-function template decls `AXPY` / `AXPBY` / `AXPBYPCZ` (the bounded-arity L0 surface the fold unifies).
- `palace/linalg/nleps.cpp:343-344`, `palace/models/romoperator.cpp:188-189` — the `γ=1` fold-into-output accumulation sites (output-aliasing variant axis; multi-term combination open-coded as iterated arity-3 fold).

Provenance: combinator-miner:2026-06-01T190900Z `reports/2026-06-01T190900Z-combinator-miner-refactor-pass-linear-combination-family/CYCLE.md` (b.3) — the L3-propagation plan of the replace-and-propagate map; this dispatch (harvester:2026-06-01T195100Z, cycle-050 D1) enacts it.
