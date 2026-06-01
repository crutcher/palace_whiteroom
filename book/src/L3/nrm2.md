---
layer: L3
operator: nrm2
firmness: firm
lowers_to:
  - book/src/L1/nrm2.md (identity-in-form on the primitive's signature; no L3-L1 theme — see Lowers-to)
lifts_from:
  - (none) — `nrm2` is a leaf primitive; no L4 entry exists (leaf primitives don't get L4 rows per cycle-010 audit verdict)
variant_axes:
  - element-type (real / complex; collapsed to single operator at L3 — result is always real)
---

# nrm2

Whole-tensor Euclidean-norm reduction at L3: `α = ‖x‖₂ = √⟨x, x⟩`. The canonical BLAS-1 norm primitive rendered as an L3 field operation; the workhorse of residual-norm convergence tests, basis-vector normalization, and Arnoldi sub-diagonal coefficients at the iteration-rotation layer. Identity-in-form lowering to L1 [`nrm2`](../L1/nrm2.md); the rotation work is at the surrounding wrapper (the `krylov-step` body or the outer convergence-test consumer), not on the primitive itself.

## Context

L3 is the iteration-rotation layer: global tensor-field operations expressed as `state' = f(state, params)`, with sequential obstructions named explicitly per [`sequential-obstruction`](../concepts/sequential-obstruction.md). `nrm2` at L3 is a whole-tensor reduction — its signature `(x: Tensor[N]) -> Scalar` exposes no element loop; the reduction over the length axis `N` is a single semantic step at L3 just as it is at L1.

This entry is a **layer-coherence anchor** per the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, codified cycle-009 meta-phase). The L3 form is value-thread-isomorphic to the L1 form — the rotation L3→L1 is identity-in-form on the primitive's signature; only the surrounding context (the iteration view at L3 vs. the mutation-rotation view at L1) differs. The L3 entry exists because each layer is coherent within itself: a reader navigating L3 (whose index at `book/src/L3/index.md:13` advertises `nrm2` as a field operation in L3 vocabulary) cannot be required to reach down to L1 to find the primitive.

The companion concept page [`concepts/nrm2`](../concepts/nrm2.md) carries the BLAS-1 heritage framing; the L1 entry [`L1/nrm2`](../L1/nrm2.md) is authoritative on every factual claim about the Palace surface (in particular: Palace's `linalg::Norml2` computes the naive `√⟨x, x⟩` via `Dot`, not the BLAS scaled-summation algorithm — the concept page's claim to the contrary is noted as a correction-pending item at `book/src/L1/nrm2.md:11`). This L3 entry adds **iteration-rotation framing** to those — it names `nrm2` as an L3-native whole-tensor reduction consumed inside the surrounding `krylov-step` body's convergence-test readout and Arnoldi sub-diagonal computation — but does not duplicate algebraic-law content; the laws hold uniformly across L1 / L2 / L3 because the body is identity-in-form across the chain.

The B-weighted overload `linalg::Norml2(comm, x, B, Bx)` at `palace/linalg/operator.cpp:600-619` is **not** part of this operator (per the L1 entry's boundary documentation at `book/src/L1/nrm2.md:13`); it is a separate L1 operator candidate (the operator-weighted energy norm, depending on both `dot` and `apply_linop`; tracked as rough-in [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) at L1). At L3 the same boundary holds — `nrm2` is the unweighted Euclidean reduction; the energy-norm primitive is a separate forthcoming L3 candidate.

## Signature

```text
nrm2 :: Tensor[N] -> Scalar
nrm2(x) = √⟨x, x⟩
```

The L3 signature is identical to the L1 signature; only the surrounding layer's vocabulary differs.

Shape contract (positional value; bunsen-style named axis; no element loop exposed at L3):

- **`x`** — `Tensor[N]` — read-only whole-tensor argument.
- **result** — `Scalar` — **always real-valued** (`real`), regardless of whether `x` is real or complex.
- The result is non-negative: `nrm2(x) ≥ 0`.

The "result is always real" rule is load-bearing — it is what makes the element-type axis collapse to a single L3 operator (in contrast to `dot`, where the result element-type tracks the input). It follows from the L1 fact that `dot(x, x)` is a non-negative real scalar for both real (L1 dot law 4) and complex (L1 dot law 9) inputs.

No element loop is exposed at L3 — the reduction over `i ∈ [0, N)` is a single semantic step in the L3 calculus. This is what makes `nrm2` L3-native by signature shape (per `book/src/L3-L2/krylov-step-body-identity.md:97`).

## Semantics

Whole-tensor reduction with defining identity: `nrm2(x) = √dot(x, x)`. This is the principal (non-negative) square root of the Hermitian self-inner-product. At L3 the reduction is rendered as a single semantic step — one node in the iteration-rotation calculus.

For real element-type: `nrm2(x) = √Σ_i x[i]²`.

For complex element-type: `nrm2(x) = √Σ_i |x[i]|² = √Σ_i (re(x[i])² + im(x[i])²)`. The Hermitian self-dot `dot(x, x)` for complex `x` is `Σ_i conj(x[i])·x[i] = Σ_i |x[i]|²`, which is real and non-negative element-wise. Inherited unchanged from [`L1/nrm2`](../L1/nrm2.md) §Semantics.

Reduction-tree non-associativity is **load-bearing** — inherited unchanged from `dot`. The square root itself is a deterministic IEEE-754 operation (correctly rounded), so `nrm2`'s non-determinism is entirely the underlying `dot`'s. Recorded as a non-law (see §Algebraic laws below).

The MPI collective is **not** in the L3 signature — single-rank is in scope per CLAUDE.md §Scope. The reduction at L3 is a single step; the local-then-collective two-step reappears only in the L1>L0 lowering at L1.

### Iteration-rotation marker

L3 is the iteration-rotation layer, and `nrm2`'s iteration view is the reduction over the length axis `N`. **The reduction lifts as a whole-tensor operation** — the signature `Tensor[N] -> Scalar` exposes no element loop, and the reduction-tree shape is opaque at L3 (the bit-level non-associativity is a recorded non-law, not a structural element of the L3 form). There is **no sequential obstruction** for `nrm2` — the reduction over independent length-axis indices is a parallel operation in exact arithmetic; the load-bearing pinned tree at L0 is a floating-point implementation choice, not an algebraic obstruction at L3.

`nrm2` is **consumed inside** larger L3 forms in two distinct roles:

1. **Convergence-test readout in `outputs`** — per `book/src/L3/krylov-step.md` §Semantics, the per-step body's `derived_views K' op` projection typically produces `outputs.residual_norm = sqrt(abs K'.β)` (CG's residual norm, computed via `dot` and inferred via the recurrence) or `outputs.residual_norm = nrm2(K'.r)` (recompute-from-residual variants). The surrounding `iterate_while_L3` outer loop reads `outputs.residual_norm` against the convergence predicate; `nrm2` is a leaf reduction consumed by this projection.
2. **Arnoldi sub-diagonal coefficient** — `H[j+1, j] = nrm2(w)` after orthogonalization (per `palace/linalg/iterative.cpp:631, 810`, the Arnoldi loop's basis-vector normalization). Consumed inside the `op.orthog` closure at the L3 form; surfaces as a scalar field of `K'` in the iterate-and-scalar update.

At L3 `nrm2` is a leaf reduction; the iteration view is what the surrounding `krylov-step` body or outer convergence-test consumer provides, not what `nrm2` itself contributes.

## Algebraic laws

The L3 algebraic laws are **inherited unchanged from L1** because the L3 form is value-thread-isomorphic to the L1 form. Inheritance is total: every L1 law for `nrm2` holds at L3 with the same statement, and every L1 non-law remains a non-law at L3. The laws are reproduced here so the L3 reader does not have to reach to L1 for the listing.

The laws below hold for both real and complex element-types of `x`:

1. **Non-negativity**: `nrm2(x) ≥ 0` for all `x`.
2. **Positive-definite (separation)**: `nrm2(x) = 0` iff `x = 0` (in exact arithmetic). The "iff" direction follows from `dot` law 4 / 9.
3. **Positive homogeneity (absolute scalar)**: `nrm2(α·x) = |α|·nrm2(x)` for any scalar `α` (real or complex). The absolute value is necessary on both sign and complex phase.
4. **Triangle inequality**: `nrm2(x + y) ≤ nrm2(x) + nrm2(y)`.
5. **Reverse triangle inequality**: `|nrm2(x) − nrm2(y)| ≤ nrm2(x − y)`. (Follows from law 4.)
6. **Cauchy–Schwarz** (relating `nrm2` to `dot`): `|dot(x, y)| ≤ nrm2(x) · nrm2(y)`, with equality iff `x` and `y` are linearly dependent (in exact arithmetic).
7. **Parallelogram identity**: `nrm2(x + y)² + nrm2(x − y)² = 2·nrm2(x)² + 2·nrm2(y)²`. (Characterizes norms induced by an inner product; holds here because `nrm2` is defined as `√⟨·,·⟩`.)
8. **Self-dot identity**: `nrm2(x)² = dot(x, x)` (real and complex) — the defining identity, restated. The structural link to `dot` is preserved unchanged at L3.
9. **Zero in argument**: `nrm2(0) = 0`. (Special case of law 2.)
10. **Phase invariance (complex)**: for complex `x` and any unit-modulus complex scalar `e^{iθ}`: `nrm2(e^{iθ}·x) = nrm2(x)`. (Special case of law 3 with `|α| = 1`.)

Laws that explicitly **do not** hold (inherited unchanged from L1):

- **Linearity in `x`**: `nrm2(α·x + β·y) ≠ α·nrm2(x) + β·nrm2(y)` in general. `nrm2` is sub-additive (law 4), not additive. This is the defining feature that distinguishes a norm from a linear functional.
- **Strictness of Cauchy–Schwarz in floating point**: law 6 can fail by ULP-level amounts due to summation ordering inside `dot` (same load-bearing caveat as the `dot` operator).
- **Bit-determinism across reduction trees**: same load-bearing caveat as `dot` — different reduction orders produce different bit-level `nrm2` values. The mathematical laws above hold; their floating-point realizations are exact modulo summation-order noise.
- **Multiplicativity over the cross-element kernel**: not applicable — `nrm2` is a reduction, not a binary algebra on vectors.

## Dependencies

**Same-layer (L3)**: [`dot`](./dot.md) — `nrm2(x) = √dot(x, x)`. The dependency is direct and complete: the L0 source defines `Norml2` as a one-line composition `std::sqrt(std::abs(Dot(comm, x, x)))`, and the L3 form preserves this composition by Law 8. The outer `sqrt` and `abs` are scalar operations below the L3 layer's resolution (deterministic IEEE-754 primitives operating on a single scalar produced by `dot`). The dependency on `dot` is the **only** L3 dependency; `nrm2` is otherwise a leaf at L3.

The fact that `nrm2` factors so cleanly through `dot` is exactly the kind of compositional structure the L3 layer is meant to expose at the field-operation level; the L0 form makes the composition syntactically explicit (one line of source at `palace/linalg/vector.hpp:255-260`), and the L3 form preserves the algebraic identity by inheritance.

**Consumers (L3)**: [`krylov-step`](./krylov-step.md) — the per-step body's `derived_views K' op` projection consumes `nrm2` for the residual-norm readout (CG, MINRES) and the Arnoldi sub-diagonal scalar (GMRES). The convergence-test consumer at the surrounding `iterate_while_L3` outer loop reads `outputs.residual_norm` per the [`convergence-test`](../concepts/convergence-test.md) discipline.

**Cross-cutting concepts**:

- [`nrm2`](../concepts/nrm2.md) — the cross-cutting concept page with BLAS-1 heritage framing.
- [`dot`](../concepts/dot.md) — referenced transitively through the defining identity `nrm2(x) = √dot(x, x)`.
- [`convergence-test`](../concepts/convergence-test.md) — the consuming context at the outer `iterate_while_L3` loop.

**L1 anchor**: [`L1/nrm2`](../L1/nrm2.md) (firm cycle-003) — the L1 entry is authoritative on the Palace surface details, the one-line `linalg::Norml2` template definition, the relationship to the B-weighted overload (separately tracked), and the complete L0 evidence list. This L3 entry does not duplicate those details; the L3>L1 rotation is identity-in-form on the primitive itself.

## Variant axes

Inherited unchanged from L1 at **one** axis:

1. **element-type** (`real` | `complex`) — at L0 these are template specializations of `linalg::Norml2<VecType>` (`VecType ∈ {Vector, ComplexVector}`). At L1 / L3 these **collapse to a single operator** with the same signature `Tensor[N] -> Scalar(real)`, because the result is real-valued regardless of input element type (the Hermitian self-dot is real per `dot` law 4 / 9), and the defining identity `nrm2(x) = √dot(x, x)` is shared across element types.

This is a stronger collapse than `dot`'s element-type axis: `dot` retains an element-type-tracking return scalar (real `dot` → real, complex `dot` → complex); `nrm2` does not.

No other variant axes at L3:

- **B-weighting**: not a variant of `nrm2` — it is a distinct operator (the operator-weighted energy norm) tracked as [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) at L1 (rough-in cycle-010 wave-1). The L0 surface uses the same overloaded name `linalg::Norml2`, but the algebraic structure differs (requires an external `B`-application primitive, requires an SPD precondition on `B`, the workspace `Bx` is a load-bearing buffer at L0).
- **Stability variants**: BLAS-style scaled-summation `nrm2` is **not present** in Palace's `linalg::Norml2` — Palace uses the naive `√⟨x, x⟩` form. Not a variant axis of the L3 operator.

## Status

`firm` — L3 form is value-thread-isomorphic to the L1 form (identity-in-form rotation); algebraic laws inherited unchanged; variant-axis profile inherited unchanged at one axis. The entry exists as a **layer-coherence anchor** per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels** (cycle-009 codification). Harvested cycle-011 wave-1 as part of the BLAS-1 reduction cohort backfill (sibling dispatch to `apply_linop`, the axpy cohort, `dot`, and `scal` at L3).

## Lowers to

L3 `nrm2` lowers to L1 [`nrm2`](../L1/nrm2.md) as **identity-in-form on the primitive's signature**. There is no L3-L1 lowering theme — no `book/src/L3-L1/` directory currently exists (precedent: cycle-010 `L3/krylov-step.md` records its identity-in-form lowering in-line at the entry, not in a separate theme file). The rotation work for this primitive lives in the surrounding wrapper at the consuming `krylov-step` body or outer convergence-test consumer, captured by [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 (which names `nrm2` among the seven primitives that are "L3-native because [each primitive's] signature has no per-element loop visible").

The L1>L0 lowering of `nrm2` lives at the L1 entry's evidence section (`book/src/L1/nrm2.md` §Evidence) — Palace's `linalg::Norml2` template at `palace/linalg/vector.hpp:255-260` is the one-line composition `std::sqrt(std::abs(Dot(comm, x, x)))`; the `std::abs` outer guard is a load-bearing defensive non-negativity check against floating-point round-off pushing the sum slightly negative; the inner `Dot` carries the MPI_Allreduce. None of this is L3 content; the L3 form sees a single-step whole-tensor reduction.

### Downward to L2 (consumer identity-in-form; no theme file)

L3 `nrm2` lowers to L2 [`nrm2`](../L2/nrm2.md) as **identity-in-form on the primitive's signature**. There is no dedicated L3>L2 theme file: the rotation is a degenerate identity-in-named-terms lowering (the only textual delta is the inner-reduction NAME), so under the 2026-06-01 vocabulary-shift redirect it is recorded here in-line rather than as a thin theme.

- **`nrm2` is a CONSUMER of `inner_product`, not a fold member.** At L2 the defining identity is written through the `inner_product` fold at the diagonal — `nrm2 x = √ (abs (inner_product x x))`, the `√ ∘ abs ∘ inner_product` composition at `y = x`. `nrm2` post-composes two scalar maps (`abs`, then `√`) onto the fold's scalar output; it does NOT itself fold and is NOT a member of the fold cohort. Merging `nrm2` into `inner_product` would be a category error (the do-NOT-merge boundary, carried in the [`inner_product`](../L2/inner_product.md) dep-map row and [`L2/index`](../L2/index.md) §"Fold-cohort boundary"). The L2 entry lists `inner_product` under `consumes`, never as a fold the operator instantiates.
- **The only textual change L3 → L2 is the inner-reduction name.** L3 writes the defining identity through the same-layer `dot(x, x)` leaf (`L3/nrm2` §Dependencies); L2 writes it through the `inner_product(x, x)` fold at the diagonal `y = x`. These denote the same Hermitian self-inner-product value (`dot(x, x) = inner_product(x, x)` at `y = x` — the inner-product fold's diagonal degeneration, [`inner-product-fold-specialization`](../L2-L1/inner-product-fold-specialization.md) §"The diagonal degeneration (`y = x`)"). The signature `Tensor[N] -> Scalar` is identical at both layers; no element loop is exposed at either (the reduction over the length axis is a single semantic step), so the rotation is identity-in-form with **no wrapper to rotate** (`nrm2` is a leaf reduction — there is no `(op, K, s)` tuple or outer loop, strictly simpler than `krylov-step-body-identity`). `nrm2` is L3-native / L2-native by signature shape per [`krylov-step-body-identity`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 (`:97`).
- **The `std::abs` defensive guard is preserved as an explicit load-bearing numerical claim at L2** (it is implicit at L3, subsumed by the non-negativity claim). The guard is a no-op in exact arithmetic but load-bearing in floating point — it strips a sign that round-off in the reduction could have flipped negative on a numerically-zero vector, buying domain-safety for `√` (no NaN). Both framings are consistent (the guard implements the non-negativity invariant); the full classification lives at [`L1-L0/nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) §"The `std::abs` defensive guard — classification".

L0 anchor (transitive through L1; verified on-disk this dispatch via `citecheck --anchor Norml2`): `palace/linalg/vector.hpp:255-260` — `linalg::Norml2` template; body line 259 is `return std::sqrt(std::abs(Dot(comm, x, x)));`. The one-line unfolded composition that makes the L3>L2 rotation identity-in-form. (Path relative to `reference/palace/`; full L0 evidence at [`L1/nrm2`](../L1/nrm2.md) §Evidence.)

## Lifts from

`nrm2` has **no L4 entry** — leaf primitives are not first-class L4 vocabulary (per the cycle-010 audit verdict at `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` §"Per-candidate verdict" (2): "leaf primitives don't get L4 rows"). At L4, `nrm2` appears inside larger composed entries (e.g., `book/src/L4/krylov-step.md` §Semantics body — `outputs.residual_norm` computed via `nrm2` or via the recurrence shortcut) as a let-binding consuming the L3-native primitive surface; it carries no monadic effect, no state-stratification typing, no novel calculus content at L4.

## Evidence

The L3 form is value-thread-isomorphic to the L1 form (identity-in-form on the primitive's signature); all L0 evidence is transitive through L1. Direct citations relevant to this L3 entry:

- [`book/src/L1/nrm2.md`](../L1/nrm2.md) (firm cycle-003) — authoritative on Palace surface, signature, algebraic laws (inherited unchanged at L3), variant axes (inherited unchanged at L3), the defining identity `nrm2(x) = √dot(x, x)`, the B-weighted-overload boundary, and the complete L0 evidence list (`vector.hpp:255-260`, `vector.hpp:262-270`, `operator.hpp:372-374`, `operator.cpp:600-619`, etc.).
- [`book/src/L1/dot.md`](../L1/dot.md) (firm cycle-002) — the dependency anchor; provides laws 4 / 9 (Hermitian self-dot is non-negative real) on which `nrm2`'s real-valued result and positivity depend.
- [`book/src/L3/dot.md`](./dot.md) (firm cycle-011, sibling dispatch) — the L3 dependency anchor; the defining identity `nrm2(x) = √dot(x, x)` is L3-internal.
- [`book/src/L3/index.md`](./index.md) line 13 — the L3 vocabulary inventory explicitly names `nrm2` as an L3 field operation. This L3 entry closes the inventory-vs-content gap noted by the cycle-010 audit.
- [`book/src/L3/krylov-step.md`](./krylov-step.md) §Semantics — the consuming context at L3; the per-step body's `derived_views` projection consumes `nrm2` for residual-norm readout; the `op.orthog` closure consumes `nrm2` for Arnoldi sub-diagonal coefficients.
- [`book/src/L3-L2/krylov-step-body-identity.md`](../L3-L2/krylov-step-body-identity.md) §"Applicability conditions" point 3 — the load-bearing statement that the seven L1 primitives (including `nrm2`) are L3-native by signature shape. This is the structural justification for the L3>L1 identity-in-form rotation.
- [`book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`](../L4-L3/krylov-step-typed-wrapper-dissolution.md) §"L3 form (RHS)" — the L3 body let-chain renders `nrm2` as an L3-native primitive call identical in shape to its L1 signature.
- [`book/src/concepts/nrm2.md`](../concepts/nrm2.md) — the cross-cutting concept page; the BLAS-1 heritage framing. (Note: the concept page's stability claim ("Palace uses scaled summation") is incorrect per the L1 entry's correction-pending note at `book/src/L1/nrm2.md:11`; the L1 entry is authoritative.)
- `palace/linalg/iterative.cpp:408, 568, 578, 582, 631, 756, 762, 810` — CG and GMRES iterative solvers using `linalg::Norml2` for: initial right-hand-side norm `β = ‖b‖`, true residual norm `‖r‖`, and Arnoldi sub-diagonal coefficients `H[j+1,j] = ‖w‖`. Direct evidence `nrm2` is the convergence-test and Arnoldi-orthogonalization primitive, inherited transitively. (Paths relative to `reference/palace/`.)
- `test/unit/test-vector.cpp:209-211` — direct test: `double norm1 = vec1.Norml2(); CHECK_THAT(norm1, WithinRel(std::sqrt(14.0)));` for `vec1 = (1, 2, 3)`. L0-equivalent semantic documentation per CLAUDE.md §"Tests as semantic supplement", inherited transitively. (Path relative to `reference/palace/`.)
- Cycle-010 audit at [`reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`](../../../reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md) §"Per-candidate verdict" (2) — HIGH CONFIDENCE backfill recommendation for the BLAS-1 cohort at L3, including `nrm2`. This entry is the enactment.

## L3 vs L1 distinction

- **L1**: pure functional reduction `α = nrm2(x)`. Mutation-rotation layer — the L0 destination buffer is erased from the signature; the MPI collective is folded into the L1>L0 lowering. The B-weighted overload is factored out as a separate L1 operator (`matrix-weighted-norm` rough-in). The defining identity `nrm2(x) = √dot(x, x)` is stated as algebraic law 8.
- **L3**: whole-tensor reduction `α = nrm2(x)` rendered as an L3 field operation. Iteration-rotation layer — the surrounding consuming context (the `krylov-step` body's `derived_views` projection, or the Arnoldi sub-diagonal in `op.orthog`) renders the iteration view explicitly as `(K, s) -> (K', s')` value-threading; `nrm2` itself is consumed as a leaf reduction with no iteration view of its own. The signature is identical to L1; the rotation is at the surrounding wrapper, not on the primitive.

The two layers' entries are **value-thread-isomorphic** on the primitive itself. The L3 entry exists for layer-coherence — a reader at L3 navigating the `krylov-step` body or the L3 vocabulary inventory must find `nrm2` defined in L3 vocabulary at L3, per CLAUDE.md §Methodology invariants **Identity-lowerings still require both L levels**.
