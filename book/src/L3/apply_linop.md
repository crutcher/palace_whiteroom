---
layer: L3
operator: apply_linop
firmness: firm
lowers_to:
  - book/src/L1/apply_linop.md (directly; identity-in-form on the primitive's signature; no L3-L2 theme — apply_linop is a leaf primitive whose L1 form is L3-native by signature shape, and L2 hosts no standalone apply_linop entry)
lifts_from:
  - (no L4 entry; apply_linop appears inside book/src/L4/krylov-step.md as a let-binding per book/src/L4/krylov-step.md §Semantics body; the L4 candidate was confirmed-not-needed by cycle-010 cross-layer-cross-cutter audit — leaf primitives carry no L4 calculus content)
variant_axes:
  orthogonal:
    - element-type (real | complex; collapsed to a single parameterised operator)
    - transpose-mode (forward | transpose | hermitian-transpose; recoverable algebraically via Aᵀ, Aᴴ)
    - accumulate-mode (overwrite | accumulate; recoverable as composition with axpby)
  absorbed:
    - operator-representation (sparse | dense | matrix-free | composition | multigrid | block | wrapped; absorbed into the opaque LinearOperator type)
---

# apply_linop

Whole-tensor linear-operator application at L3: `y = A·x` for an abstract linear operator `A : V → W`. The opaque-operator primitive at L3 — one of the whole-tensor field operations the L3 layer's index advertises (`book/src/L3/index.md:11-14`), the per-step matvec primitive consumed by [`krylov-step`](./krylov-step.md), and the iteration-rotation rendering of the same linear-map application that L1 [`apply_linop`](../L1/apply_linop.md) provides.

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as whole-tensor primitives with no element-loop exposed at the layer's vocabulary. `apply_linop` at L3 is the value-threaded form of the linear-map application primitive — the same operator that L1 names as the "pure-functional operator-as-function" (replacing the L0 `A.Mult(x, y)` in-place mutation idiom), but read at L3 as one of the field operations the layer enumerates as canonical vocabulary. The L3 index (`book/src/L3/index.md:13`) explicitly lists "matvec, axpy, dot, nrm2 as field operations" as L3 vocabulary; `apply_linop` is the matvec generalisation.

The relationship to the adjacent layers:

- **Upward** to L4: there is **no standalone L4 entry** for `apply_linop`. The cross-layer audit (`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"Per-candidate verdict") confirmed L4 candidacy as `CONFIRMED-NOT-NEEDED` — `apply_linop` carries no monadic effect, no state-stratification typing, no novel calculus content at L4. It appears inside the L4 `krylov-step` body (`book/src/L4/krylov-step.md` §Semantics, line 59) as a let-binding (`let w = apply_linop op.T K.<input_field>`), not as first-class L4 vocabulary. The L4 form's use of `apply_linop` is by reference to the same whole-tensor primitive this L3 entry names. Per CLAUDE.md §Methodology invariants "Layers are defined high→low", the absence of an L4 entry is a deliberate scoping verdict, not a gap.

- **Downward** to L1: `apply_linop` lowers to L1 [`apply_linop`](../L1/apply_linop.md) directly, with no interposed L2 entry and no `L3-L2/apply-linop-identity` theme. The rotation is **identity-in-form on the primitive's signature** — both L1 and L3 see `apply_linop :: LinearOperator[M, N] -> Tensor[N] -> Tensor[M]` with the same shape contract, the same algebraic laws, the same variant-axis profile (four), and the same absorbed operator-representation type. The L2 layer does not host a standalone `apply_linop` entry; the L2 vocabulary names `apply_linop` only as a referenced L1 primitive inside compositions (`book/src/L2/krylov-step.md` §Dependencies line 96, §"L2 vs L1 distinction" lines 130-132). The L3>L1 hop is therefore direct, not chained through L2. (Per the cycle-010 audit's L2 verdict: "CONFIRMED-NOT-NEEDED-WITH-CAVEAT" — L2's role is composition, not naming primitives; the duplication risk is acute and the entry would carry no algebraic novelty.)

This L3 entry is the **layer-coherence anchor**: a reader at L3 can find `apply_linop` here, in L3 vocabulary, without having to reach down to L1 to recover the signature, and without having to consult the L4 `krylov-step` body to see the primitive in use. The backfill is the second cycle-011 (cycle-010-audit-driven) enactment of the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase codification). The cycle-010 audit's HIGH CONFIDENCE recommendation for this entry rests on three convergent signals: (1) the L3 index advertises matvec as a field operation but the entry does not exist; (2) both firm cross-layer themes that bracket L3 (the L4>L3 wrapper-dissolution and the L3>L2 body-identity) render `apply_linop` as an L3-native let-binding; (3) the rotation is value-thread-isomorphic on the primitive's signature.

## Signature

```text
apply_linop :: LinearOperator[M, N] -> Tensor[N] -> Tensor[M]
apply_linop A x = A · x
```

Shape contract (positional values; L3 has no `readonly` annotation and no monadic effect — the typing distinctions are deferred to the wrapper layers above):

- **`A`** — `LinearOperator[M, N]`, an opaque linear-map type with named domain axis `N` and named codomain axis `M`. The operator-representation axis (sparse, dense, matrix-free, composition, multigrid, block, wrapped) is **absorbed at L3** into this opaque type; the L3 kernel does not branch on representation. The element type (real or complex) is parameterised; the L3 signature is uniform across the element-type axis.
- **`x`** — `Tensor[N]`, the input vector. Read-only at L3 (value-threaded positionally; the L3 layer has no in-place mutation in vocabulary — mutation reappears only in the L1>L0 lowering). The element type matches `A`'s element type.
- **result** — `Tensor[M]`, the output vector. A fresh value produced by the linear map; no L0 destination buffer is mentioned at L3 (the destination-binding rotation is an L1>L0 concern, per [`apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md) §"L0 form (RHS)"). The element type matches the domain.

The axes `M` and `N` are independent in general — `A` may be rectangular. For the iteration-rotation use case (per-step matvec inside `krylov-step`), `M = N` (square operator) is the common case. For mesh-coupling discrete differential operators (`Grad`: H1 → Nedelec; `WeakDiv`: Nedelec → H1), and for prolongation/restriction operators in multigrid (`trial_fespace.GetProlongationMatrix()`, witnessed at L0 by `palace/linalg/rap.cpp:212`), `M ≠ N` is genuine.

`LinearOperator[M, N]` is an **opaque type** at L3: its internal representation is not part of the L3 signature — sparse-matrix, dense-matrix, matrix-free quadrature, operator composition (`A · B`), multigrid V-cycle, block structure, parallel wrapping all collapse to the same opaque type by [`variant-absorption`](../concepts/variant-absorption.md) at the operator-representation axis. The L3 contract sees only the linear-map interface and the domain/codomain axes; the rest is below L3's level of abstraction.

Three pieces of L4 wrapper machinery are absent at L3, mirroring the krylov-step L3 entry's discipline:

1. **No `Solve` monad.** `apply_linop` is pure functional at L3; no `do`-block, no `modify`, no monadic effect. (At L4 it is used inside `Solve`-monadic `do`-blocks as a let-binding, e.g., `let w = apply_linop op.T K.<input_field>` in the L4 `krylov-step` body; but the primitive itself carries no monadic structure.)
2. **No `readonly` typing.** The L4 calculus would mark the `LinearOperator` argument as `readonly` (the operator is never written through `Mult`'s receiver); at L3 this is a documented invariant (the L3 vocabulary has no `readonly` annotation; the convention is preserved by reading the primitive's contract).
3. **No element-loop exposure.** The L3 form's "no element loop visible at the layer" property is structural — `apply_linop`'s signature has the linear-map application as a whole-tensor operation, never an iteration over `M` or `N` indices. This is what makes `apply_linop` **L3-native by signature shape**, per the cycle-002 combinator-miner argument and the cycle-006 audit (`book/src/L3-L2/krylov-step-body-identity.md` §"Applicability conditions" line 97).

## Semantics

`apply_linop A x` returns the image of `x` under the linear map `A`. The result is determined entirely by `A` and `x` — no hidden state, no per-call side effects, no in-place mutation at the L3 surface. The L3 form is **pure functional** (the same `A` applied to the same `x` returns the same `Tensor[M]` value), with bit-determinism caveats inherited from the L1 entry and recorded as an explicit non-law (see Algebraic laws §Reduction-tree non-associativity).

The defining property at L3 is **linearity**: `apply_linop A (α·x + β·y) = α · apply_linop A x + β · apply_linop A y` for any scalars `α`, `β` and any vectors `x`, `y` in the domain. This is what makes `A` a *linear* operator at L3 (distinguishing `apply_linop` from a general nonlinear function-application primitive); the iteration-rotation use case relies on this property for every per-step algebraic argument inside `krylov-step` (residual updates, descent-direction updates, polynomial-recurrence updates).

**Transpose modes** (forward, transpose, hermitian-transpose) are not separate L3 operators. They are recoverable by replacing `A` with the algebraic transform: `apply_linop Aᵀ x` for the transpose, `apply_linop Aᴴ x` for the conjugate-transpose. At L0 these are dedicated virtual methods (`MultTranspose`, `MultHermitianTranspose`) because the operator's internal representation may permit more efficient transpose paths; the L1>L0 lowering reintroduces those dedicated methods per [`apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md) sub-patterns B and C. At L3 the transpose-mode variant axis is fully absorbed by the algebraic transform.

**Constructed operators** (`A · B`, `M⁻¹ · A`, `Gᵀ M G`, the preconditioner-side surface `apply_BA`) are not separate L3 operators either — they are values of type `LinearOperator[M, N]` formed by other operator-level constructors (operator composition, sum, scaling, preconditioner inversion). The L3 form `apply_linop (A · B) x` is algebraically `apply_linop A (apply_linop B x)`; this is law 4 below, witnessed at L0 by `BaseProductOperator::Mult`'s `B.Mult(x, z); A.Mult(z, y)` two-step apply. Inside `krylov-step` at L3 the construction surface is named `op.T` (the preconditioner-side variant absorbed into one operator value); see [`apply_BA`](../concepts/apply_BA.md).

**Accumulating mode** (`y ← y + a · A · x`) is not a separate L3 operator. It is the L3 composition `axpby a (apply_linop A x) 1 y` — two L3-native primitives in sequence. The L0 source provides `AddMult` as a fused method for transparent-performance reasons (skipping zero-initialisation; for matrix-free operators, fusing element-contribution accumulation directly into `y`); both fusions are L1>L0 lowering concerns and are covered by [`apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md) sub-patterns D and E. At L3 the accumulate-mode axis is fully absorbed by the composition with `axpby`.

The body is **stateless across calls** — `A` is an opaque operator value (immutable from the L3 caller's perspective; the L0 representation may have a `mutable` workspace member like `BaseProductOperator::z`, but this is private and not observable from the L3 surface); `x` flows in, the result flows out as a fresh `Tensor[M]` value; no inputs are written. This is what makes `apply_linop` foldable inside a tail-recursive `iterate_while_L3` at L3 — every per-step matvec is a pure function of the carry's input field.

### Iteration-rotation marker

L3 is the iteration-rotation layer. **`apply_linop` lifts as a whole-tensor operation at L3** — the primitive's signature has no element loop exposed at the layer, and the L1 form's `Tensor[N] -> Tensor[M]` signature is identity-in-form to the L3 form. The primitive does **not** carry an outer-loop sequential-obstruction itself (the obstruction lives in the *trajectory* of an iterative solver that calls `apply_linop` repeatedly, not in any single application). Where `krylov-step` at L3 has an outer-loop `sequential-obstruction` because the step-trajectory is intrinsically sequential, `apply_linop` at L3 has **no obstruction at the L3 level** — it is one of the layer's clean whole-tensor field operations.

A subtle below-the-surface caveat: for matrix-free operator representations (quadrature-based partial-assembly, libCEED kernels), the L0 evaluation involves a reduction over element-local contributions. This reduction has a **load-bearing summation-order** dependency for bit-reproduction (CLAUDE.md §"Optimization tricks vs. base algebra"); different summation orders produce mathematically-equivalent but bit-distinct outputs. The L3 form names this as a non-law (see Algebraic laws §"Bit-determinism across operator representations"), not as an obstruction — the algebraic correctness of `apply_linop` is unaffected; only the bit-reproduction property is.

## Algebraic laws

The seven laws that hold at L1 transport unchanged to L3, because the primitive's signature is identity-in-form across the L3→L1 hop. The non-laws also transport unchanged.

1. **Linearity in `x`**: `apply_linop A (α·x + β·y) = α · apply_linop A x + β · apply_linop A y` for any scalars `α`, `β` and any vectors `x`, `y` in the domain of `A`. The defining property at L3; foundational for every algebraic argument inside `krylov-step` and the iterative-solver consumer chain.

2. **Zero-vector annihilation**: `apply_linop A 0_N = 0_M` (where `0_N` is the zero vector of axis `N` and `0_M` is the zero vector of axis `M`). Follows from law 1 with `α = β = 0`.

3. **Identity operator**: `apply_linop I x = x` for the identity operator `I : V → V` (where `V` is some space with axis `N`; `M = N`). The identity-operator construct exists implicitly in the opaque-operator surface.

4. **Composition (operator product)**: `apply_linop (A · B) x = apply_linop A (apply_linop B x)` where `A · B` is the operator-composition construct (an operator with domain matching `B`'s domain and codomain matching `A`'s codomain, requiring `B`'s codomain axis to equal `A`'s domain axis). This is the L3 algebraic identity that enables constructed-operator chains like `apply_BA = A · M⁻¹` to be unfolded into a sequence of single-operator applies — directly consumed by `krylov-step` at L3 in the form `apply_linop op.T K.<input_field>` (where `op.T` may be a composed operator). Witnessed at L0 transitively via the L1 entry's `palace/linalg/operator.hpp:202-206` citation.

5. **Sum operator distributes over addition**: `apply_linop (A + B) x = apply_linop A x + apply_linop B x` where `A + B` is the operator-sum construct (both `A` and `B` share the same domain and codomain axes).

6. **Scaled operator (operator-side scalar absorption)**: `apply_linop (α·A) x = α · apply_linop A x` for any scalar `α`. The L1>L0 lowering may realise this either as the operator-side scaling baked into the L0 representation or as a post-apply `axpby`-style scaling.

7. **Zero operator**: `apply_linop 0_op x = 0_M` for the zero operator `0_op : V → W`. Special case of law 6 with `α = 0`.

These seven laws are inherited from the L1 entry's seven laws (`book/src/L1/apply_linop.md` §"Algebraic laws") unchanged. The transport is structural: the primitive's signature is identity-in-form, and the laws are statements about the linear-map relationship between `A`, `x`, and the result — independent of which layer renders the primitive.

Laws that explicitly **do not** hold (also inherited from L1):

- **Commutativity of operator composition**: `apply_linop (A · B) x ≠ apply_linop (B · A) x` in general. Operator product is non-commutative; only in special structured cases (e.g., simultaneously diagonalisable operators) does the equality hold. Recorded as an absence because constructed-operator chains at L3 (e.g., `apply_BA = A · M⁻¹` vs. `M⁻¹ · A`) depend on this non-commutativity.
- **Self-inverse / involutivity**: `apply_linop A (apply_linop A x) ≠ x` in general. Only true for involutive `A` (e.g., reflections); most operators in Palace's solver corpus are not involutive.
- **Bit-determinism across operator representations**: a sparse-matrix realisation of `A` and a matrix-free realisation of the *same* mathematical operator produce results that agree mathematically but may differ at the bit level (different summation orders in the assembly/quadrature stage). Load-bearing per CLAUDE.md §"Optimization tricks vs. base algebra"; the choice of L0 representation can change the bit-level output even though the algebraic correctness is preserved. The L3 mathematical laws hold; their floating-point realisations are exact modulo summation-order noise.
- **Floating-point linearity strictness**: law 1 is the mathematical identity in ℝ / ℂ. In IEEE-754 the equality is approximate (the two sides round differently). Algorithms that depend on exact linearity (recurrence-residual update schemes that recompute the residual to check the recurrence; orthogonalisation reorthogonalisation predicates) must guard. Recorded as an absence inherited from L1.

The non-law set is **inherited unchanged** from L1; the L3 rendering introduces no new non-laws. This is what makes the L3>L1 hop identity-in-form on the primitive's signature: not only does the signature transport unchanged, the entire algebraic profile (laws + non-laws) transports unchanged.

## Dependencies

**Same-layer (L3)**: `apply_linop` is a **leaf primitive at L3** — no other L3 operator is used in its definition. It is the foundational matvec primitive in the L3 vocabulary, consumed by [`krylov-step`](./krylov-step.md) at L3 as the per-step operator-application.

**Cross-cutting concepts**:

- [`apply_BA`](../concepts/apply_BA.md) — the constructed-operator surface that absorbs the preconditioner-side variant of `op.T` in `krylov-step`'s L3 body. `apply_BA = A · M⁻¹` (or `M⁻¹ · A`, or `B^{1/2} · A · B^{1/2}` depending on the slice); each form is an instance of operator composition (law 4) and is applied via `apply_linop`. Documented at the concept level; instantiated by each consuming slice.
- [`constructed-operators`](../concepts/constructed-operators.md) — the level-(c) variant absorption of operator-representation. The L3 `apply_linop` is uniform across all concrete L0 representations because the construction discipline keeps the operator-representation axis off the L3 signature.
- [`variant-absorption`](../concepts/variant-absorption.md) — the level-(b)/(c) absorption discipline. Three of `apply_linop`'s four variant axes (element-type, transpose-mode, operator-representation) are absorbed at L3 either by parameterisation, algebraic transform, or opaque-type absorption.

**Strawman reference**: `book/src/design/l4_calculus.md` is the L4 conventions source; this L3 entry follows the strawman's Haskell `::` signature notation. The L4 layer does not surface `apply_linop` as a standalone entry (per the cycle-010 cross-layer audit verdict); the L4 form is the implicit use inside the L4 `krylov-step` body's let-chain.

No L4 monadic vocabulary appears in the L3 signature (no `Solve`, no `modify`, no `do`-block). No L2 composition vocabulary appears (no `krylov_update`, no `apply_BA` as a named L2 entry; the constructed-operator surface is referenced as the [`apply_BA`](../concepts/apply_BA.md) concept). That is the discipline of the layer.

## Variant axes

`apply_linop` has **three orthogonal variant axes at L3, plus one collapsed-and-absorbed axis** — the same framing as L1 (`book/src/L1/apply_linop.md:75-83`), transported unchanged.

Three orthogonal axes:

1. **element-type** (`real | complex`) — collapsed to a single parameterised operator at L3. The L0 source splits this into two parallel class hierarchies (`Operator` real, `ComplexOperator` complex, `palace/linalg/operator.hpp:24-68`); the L3 form is uniform across the element-type axis. Semantics are identical across element types — the per-operator linear-map relationship is the same; only the field of the underlying scalar differs.

2. **transpose-mode** (`forward | transpose | hermitian-transpose`) — recoverable algebraically. At L3 the three transpose modes are **not** separate operators; they are recoverable via `apply_linop A x`, `apply_linop Aᵀ x`, `apply_linop Aᴴ x` from the algebraic transforms `Aᵀ` and `Aᴴ`. The L0 source exposes three dedicated virtual methods (`Mult`, `MultTranspose`, `MultHermitianTranspose`); the L1>L0 lowering reintroduces them per [`apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md) sub-patterns A, B, C. At L3 there is one operator. (For real operators the hermitian-transpose collapses to the transpose; `MultHermitianTranspose` is meaningful only on `ComplexOperator`.)

3. **accumulate-mode** (`overwrite | accumulate`) — recoverable as composition. At L3 the accumulating form is **not** a separate operator; it is the composition `axpby a (apply_linop A x) 1 y`. The L0 source exposes `Mult` (overwriting) and `AddMult` (accumulating) as separate virtual methods for transparent performance reasons (skipping zero-initialisation; matrix-free direct accumulation); the L1>L0 lowering reintroduces the fusion per [`apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md) sub-patterns D and E. At L3 the accumulate-mode axis is composition-recoverable.

Collapsed (absorbed) axis:

- **operator-representation** (`sparse-matrix | dense-matrix | matrix-free | composition | multigrid | block | wrapped | ...`) — **absorbed** into the opaque `LinearOperator[M, N]` type. The L0 concrete subclasses (`SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`, `BaseMultigridOperator`, `ComplexWrapperOperator`, `ParOperator`, `ComplexParOperator`, all preconditioners, all FE assembly closures) collapse to a single L3 type. The L1 contract collapses this axis identically; the L3 inheritance is by signature shape — no element loop exposed, no per-representation branching at the L3 surface. This is the canonical application of [`variant-absorption`](../concepts/variant-absorption.md).

The variant-axis profile (three orthogonal + one absorbed) matches the L1 entry exactly. **No new axes introduced by the L3 rendering; no axes merged or split; the orthogonal-vs-absorbed framing is preserved.** The L1>L0 lowering theme (`book/src/L1-L0/apply-linop-mutation-rotation.md`) re-surfaces orthogonal axes 2 and 3 as five concrete L0 sub-patterns (A: bare forward apply; B: transposed apply; C: Hermitian-transposed apply; D: accumulating forward apply; E: accumulating transposed/Hermitian applies); the L3 form is uniformly axis-collapsed.

## Status

`firm` — value-threaded positional signature is the canonical iteration-rotation form for the linear-operator application primitive; algebraic laws are the same seven that hold at L1 (linearity, zero-vector annihilation, identity, composition, sum distribution, scalar absorption, zero operator); non-laws are catalogued explicitly (operator-composition non-commutativity, non-involutivity, bit-determinism across representations, floating-point linearity strictness); variant-axis profile is three orthogonal + one absorbed (the same framing as L1), inherited unchanged.

The pattern is well-attested via the chain: L1 firm-up cycle-004; cross-layer audit cycle-010 confirmed HIGH CONFIDENCE backfill candidacy. The two firm cross-layer themes that bracket L3 — `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (cycle-008 firm) and `book/src/L3-L2/krylov-step-body-identity.md` (cycle-009 firm) — both render `apply_linop` as an L3-native let-binding in `krylov-step`'s body, ratifying the L3 form's signature shape. This dispatch (cycle-011 wave-1) is the **layer-coherence backfill** — the L3 form was previously published only inside the L4 `krylov-step` body's let-chain (as a let-binding) and inside the two cross-layer themes' code blocks (as a referenced primitive); it now has its own L3 entry per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md, cycle-009 meta-phase).

## Lowers to

L3 `apply_linop` lowers to L1 [`apply_linop`](../L1/apply_linop.md) directly — **no interposed L2 entry, no L3-L2 theme**. The rotation is identity-in-form on the primitive's signature: both L1 and L3 see `apply_linop :: LinearOperator[M, N] -> Tensor[N] -> Tensor[M]` with the same shape contract, the same seven algebraic laws, the same four-non-law set, and the same four-axis variant profile. The L3>L1 hop is structural rather than mechanical — the L2 layer does not host an `apply_linop` entry (per the cycle-010 audit's L2 verdict, primitives like `apply_linop` are referenced from L2 compositions but do not get standalone L2 entries; the duplication risk vs. algebraic novelty trade-off favours leaving them in L1).

The L1>L0 lowering theme [`apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md) is the substantive rotation in the chain — it lowers the L1 pure-functional form into Palace's in-place L0 virtual `Mult`/`MultTranspose`/`MultHermitianTranspose`/`AddMult`/`AddMultTranspose`/`AddMultHermitianTranspose` family across five sub-patterns. The L3>L1 hop is by contrast a layer-coherence rotation (each layer is coherent within itself), not an algebraic one; no L3-L1 theme is needed because the rotation is value-thread-isomorphic on the primitive's signature.

**Practical reading**: an algorithm written at L3 that calls `apply_linop` is reading the L1 entry's algebraic content (laws, non-laws, signature) one layer down; the L3 entry's role is to anchor the primitive in the L3 vocabulary inventory (so the L3 index's "matvec, axpy, dot, nrm2 as field operations" advertisement at `book/src/L3/index.md:13` is honoured).

## Lifts from

**`apply_linop` has no standalone L4 entry.** Per the cycle-010 cross-layer audit (`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"Per-candidate verdict" point 1), the L4 candidate was confirmed-not-needed: leaf primitives like `apply_linop` carry no monadic effect, no state-stratification typing, no novel calculus content at L4. They appear inside L4 entries as let-bindings, not as first-class L4 vocabulary.

The implicit L4 use of `apply_linop` is at `book/src/L4/krylov-step.md` §Semantics (line 59) — the L4 `krylov-step` body has `let w = apply_linop op.T K.<input_field>` as the first line of its do-block. The L4 form's `apply_linop` is read as the same whole-tensor primitive this L3 entry names; the rotation from the L4 mention to the L3 entry is the identity (the primitive's signature does not change between layers — only the surrounding wrapper does, and `apply_linop` carries no wrapper at L4 or L3).

The two firm cross-layer themes that bracket L3 — `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` and `book/src/L3-L2/krylov-step-body-identity.md` — both render `apply_linop` as an L3-native let-binding inside `krylov-step`'s body. The L4-L3 theme (`§"L3 form (RHS)"` line 64) writes the L3 form as `apply_linop op.T K.<input_field>`; the L3-L2 theme (`§"L3 form (LHS)"` line 30) reproduces the same form. Both themes treat `apply_linop` as a primitive whose L3 form is given (not invented by the theme); this L3 entry is the canonical anchor for that form.

**Why no L4 entry**: L4 is the typed-wrapper/monadic-coordination layer. First-class L4 vocabulary carries one of: (a) monadic effect (`Solve` monad threading state); (b) state-stratification typing (typed records like `OpParams`, `Krylov`, `SimState`); (c) outer-driver structure (`iterate_while`, `restart_cycle`, `solve_loop`). `apply_linop` carries none of these — it is a pure linear-map application with no state, no typed records, no driver structure. Promoting it to a standalone L4 entry would over-promote a leaf primitive and add no calculus content. The cycle-010 audit's verdict is `CONFIRMED-NOT-NEEDED` for the L4 candidate, and this entry adopts that verdict.

## Evidence

The L3 form is value-thread-isomorphic to the L1 form on the primitive's signature; all L0 evidence is transitive through L1.

**Direct citations relevant to this L3 entry**:

- `book/src/L1/apply_linop.md` (cycle-004 firm) — the L1 entry whose signature, semantics, algebraic laws, variant axes, and L0 evidence are transported unchanged to L3. The seven laws and the four non-laws cited above are reproduced from the L1 entry's §"Algebraic laws" section.
- `book/src/L1-L0/apply-linop-mutation-rotation.md` (rough-in; cycle-007) — the five sub-patterns (A: bare forward apply via `Mult`; B: transposed apply via `MultTranspose`; C: Hermitian-transposed apply via `MultHermitianTranspose`; D: accumulating forward apply via `AddMult`; E: accumulating transposed/Hermitian applies via `AddMultTranspose`/`AddMultHermitianTranspose`) covering the transpose-mode × accumulate-mode variant-axis matrix. The L1 form (LHS of the rewrite) is the same as the L3 form here.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` (cycle-008 firm) §"L3 form (RHS)" line 64 — `let w = apply_linop op.T K.<input_field>` is the first line of the L3 `krylov-step` body's let-chain. This is one of the two firm cross-layer themes that render the L3 form of `apply_linop`.
- `book/src/L3-L2/krylov-step-body-identity.md` (cycle-009 firm) §"L3 form (LHS)" line 30 — reproduces the same L3 form; §"Applicability conditions" line 97 explicitly names `apply_linop` as one of the seven L1 primitives that "operate on whole-tensor inputs with no element-loop exposed at L2. This is what makes the L3>L2 rotation identity-in-form rather than requiring a decomposition step (each L1 primitive is *also* L3-native because its signature has no per-element loop visible)." This is the **load-bearing structural argument** for the L3 backfill: the primitive's signature is L3-native by inspection.
- `book/src/L3/krylov-step.md` (cycle-010 firm) §Semantics — the wave-1 precedent L3 entry consumes `apply_linop` as a per-step matvec at the very first line of the `krylov-step` body (`let w = apply_linop op.T K.<input_field>`). The L3 form named by this entry is the form that L3 `krylov-step` reads.
- `book/src/L3/index.md:13` — "Whole-tensor primitives (matvec, axpy, dot, nrm2 as field operations)" — the L3 vocabulary inventory advertisement that this entry honours.
- `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` — the cycle-010 audit identifying this L3 backfill as HIGH CONFIDENCE. §"Per-candidate verdict" point 1 (the L3 verdict + the L2/L4 confirmed-not-needed verdicts).

**Transitive L0 evidence (via the L1 entry; not duplicated here in detail)**:

- `palace/linalg/operator.hpp:21, :24-68, :36-39, :116-136, :178-229, :298-367` — operator class hierarchy declarations (real / complex; transpose / accumulate variants; concrete subclass structure).
- `palace/linalg/operator.cpp:428-441, :458-466, :479-487` — `SumOperator::Mult`, `SumOperator::AddMult`, `BaseDiagonalOperator::Mult` definitions (witnesses for laws 5, 6, and matrix-free realisation).
- `palace/linalg/operator.hpp:202-206` — `BaseProductOperator::Mult` (witness for law 4, operator composition).
- `palace/linalg/rap.cpp:195-234, :481-517` — `ParOperator::Mult`, `ComplexParOperator::Mult` (parallel wrapper realisations; single-rank reading per CLAUDE.md Scope reduces to inner-operator-plus-BC-masking).
- `palace/linalg/iterative.cpp:379, :443, :544-734` — call sites in CG (residual + inner-loop matvec) and GMRES (Arnoldi-step matvec).

Phase-1 slice instances where `apply_linop` appears as the per-step matvec (transitive via L1; instantiations of the L3 form's consumption pattern):

- CG L4 v0.5 step bodies (`cg_first_step` and `cg_steady_step`; firm-homed at `book/src/L4/krylov-step.md` Form B, cycle-099); each has `let Ap = apply opA p'` as the per-step matvec call. The L0 matvec home is `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern B (`iterative.cpp:360-486`).
- GMRES `inner_loop` body; `apply_linop` at the Arnoldi-step matvec — firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C (`iterative.cpp:543-705`).
- `book/src/L4/chebyshev.md` §Semantics `innerStep` — `apply_linop` (`applyLinop op.A d`) in the polynomial-recurrence body (firm cycle-015, absorbing the former `chebyshev.md:354-362` slice §L4).
- Arnoldi step procedure — `apply_BA : w ← apply_linop(T, V[j])`, the pure-functional form, and the L3-form rendering `w ← apply_linop(T, V[j])` (field-side, global); `apply_linop` at the Krylov-basis extension matvec. Firm L0 home `book/src/L1-L0/ksp-solve-mutation-rotation.md` Sub-pattern C inner Arnoldi loop (within `iterative.cpp:563-683`).

## L3 vs L4 distinction

- **L4**: no standalone `apply_linop` entry. The primitive appears inside L4 operator entries (e.g., `book/src/L4/krylov-step.md` §Semantics body line 59) as a let-binding within a `Solve`-monadic do-block. The let-binding has type `Tensor[N]` (a pure value); the surrounding `do`-block carries the monadic effect on `SimState`. The L4 `apply_linop` is the same primitive as this L3 entry; the L4 wrapper (the `do`-block, the typed records, the `readonly` typing) is what makes the surrounding `krylov-step` L4-distinct — not the `apply_linop` call itself.
- **L3**: standalone entry (this file). Positional value-threading: `apply_linop A x = A · x`. No monadic effect, no typed records, no `readonly` typing, no `do`-block. The primitive's signature is the L4 let-binding's RHS type, lifted out of the monadic context.

## L3 vs L1 distinction

- **L1**: pure-functional linear-operator application; the "closest pure-functional layer to the source" per `book/src/L1/index.md` §Context. The mutation rotation has happened (the L0 destination buffer `y` has been dropped from the signature); the operator-representation axis has been absorbed (the opaque `LinearOperator` type). The L1 vocabulary mirrors the source operations with pure-functional binding.
- **L3**: whole-tensor linear-operator application; one of the "Whole-tensor primitives (matvec, axpy, dot, nrm2 as field operations)" advertised by the L3 index (line 13). The iteration-rotation layer reads the primitive as a global tensor-field operation. **The primitive's signature is identity-in-form to L1** — no change in shape, no change in algebraic laws, no change in variant axes. The L3 entry exists for layer-coherence: a reader at L3 finds the primitive defined in L3 vocabulary, without having to drop down to L1.

The two layers' entries share signature, algebraic laws (seven), non-laws (four), variant-axis profile (three orthogonal + one absorbed), and the cited L0 evidence (transitive). They differ in **layer interpretation**: L1 frames the primitive as the mutation-rotated form of the L0 `Mult` virtual; L3 frames the primitive as one of the field operations the iteration-rotation layer enumerates as canonical vocabulary. The two framings are complementary — they read the same primitive from different layer roles — and the layer-coherence invariant (CLAUDE.md §Methodology invariants "Identity-lowerings still require both L levels") requires both entries to exist.
