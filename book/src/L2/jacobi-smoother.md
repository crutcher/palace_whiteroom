---
layer: L2
operator: jacobi-smoother
firmness: firm
lowers_to:
  - book/src/L1/jacobi-smoother.md (identity-in-form on the constructed-operator-gate apply; the apply is a single whole-tensor elementwise product with no kernel fusion to unfold — the L2>L1 rotation is a degenerate identity-in-named-terms lowering annotated in-line in §"Lowers to", no dedicated theme file as of cycle-051 demotion; the substantive leaf-mutation rotation lives at L1>L0 reciprocal-elementwise-product-mutation-rotation sub-pattern B + jacobi-smoother-mutation-rotation)
lifts_from:
  - book/src/L3/jacobi-smoother.md (firm cycle-037; value-thread-isomorphic on the gate apply; the L3 iteration-rotation rendering this L2 floor sits beneath — identity-in-form, no L3-L2 theme, in-line annotation per cycle-012 non-adjacent-identity convention)
fold_parent: none (standalone constructed-operator gate; NOT a member of the linear_combination / inner_product fold cohort — fork-INDEPENDENT, the cycle-041 dot-l2-leaf-floor-vs-fold-only-design fork does not apply)
variant_axes:
  orthogonal:
    - element-type (real | complex; collapsed into the opaque JacobiSmoother closure)
    - damping-mode (default ω=1.0 | fixed ω≠0 | estimated ω=0; collapsed into op.dinv's committed value at setup)
  absorbed:
    - operator-representation (sparse-CSR | matrix-free-Nedelec | parallel-wrapped | complex-wrapped; collapsed at setup through assemble-diagonal's own representation-axis absorption)
---

# jacobi-smoother

Diagonal (Jacobi) preconditioner action as a base-algebra field operation at L2:
the constructed-operator gate `y = jacobi_smoother(op, x)` whose per-call body is
one elementwise product `op.dinv ⊙ x = (ω · D⁻¹) ⊙ x` of the damped inverse
diagonal against the input. The **thinnest constructed-operator gate** at the
fusion-rotation layer — a single elementwise multiplication, no operator-apply,
no reduction, no sweep loop, no convergence test, and (the defining
fusion-rotation fact) **no fused multi-operation kernel to unfold**. The
fusion-rotation rendering of the same diagonal-preconditioner-apply that L1
[`jacobi-smoother`](../L1/jacobi-smoother.md) provides and that L3
[`jacobi-smoother`](../L3/jacobi-smoother.md) renders as a whole-tensor field
operation; the rotation L2 ↔ L1 is identity-in-form on the constructed-operator-gate
apply.

## Context

L2 is the fusion-rotation layer (`book/src/L2/index.md`): "Kernel fusion across
multiple algebraic operations is unfolded into composition… Batched specialized
BLAS calls are written as compositions of base primitives." The L2 vocabulary is
tensors, linear operators, and base primitive operations, with HPC/SIMD fusion
tricks unfolded back into the base algebra. `jacobi-smoother` at L2 is the
base-algebra reading of the diagonal-preconditioner gate — the same
constructed-operator gate L1 names (replacing the L0
`JacobiSmoother<OperType>::Mult(x, y)` in-place output-arg mutation idiom), read
at L2 as a single field operation.

**`jacobi-smoother` is a constructed-operator gate, fork-INDEPENDENT, with NO
fold-parent.** It is **not** a member of the L2 fold cohort — it is neither an
arity member of [`linear_combination`](./linear_combination.md) (the
reduce-to-`Tensor[N]` term-axis fold) nor a leaf/consumer of
[`inner_product`](./inner_product.md) (the reduce-to-`Scalar` length-axis fold).
It is a constructed-operator gate in the same family as the firm
[`ksp_solve`](./ksp_solve.md) and [`eigsolve`](./eigsolve.md): its primary
argument `op` is a structured opaque value built once at solver setup (the
`SetOperator` step), carrying the captured operator `A` only via its assembled
inverse diagonal `dinv`, the damping factor `ω`, and the spectral-bound scaling
`sf_max`. The cycle-041 leaf-vs-fold design fork
(`dot-l2-leaf-floor-vs-fold-only-design`, `book/src/L2/index.md`,
pending the batch-12 meta-phase) is **about the BLAS-1 leaves** (`dot` / `scal`
as same-named floors vs fold-only); it does **not** reach `jacobi-smoother`,
which is a constructed-operator gate with no fold-parent on either codomain.

It is the **thinnest** such gate — unlike `ksp_solve` (an outer-driver fold over
the `krylov-step` kernel) and `eigsolve` (a named shift-invert composition over a
constructed inverse solver), `jacobi_smoother`'s per-call action is **one
elementwise product**. The closely-parallel sibling is
[`chebyshev-iteration`](./chebyshev-iteration.md): both lift the same
`op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup chain
(`palace/linalg/jacobi.cpp:79-80`; cf. `palace/linalg/chebyshev.cpp:177-178`),
and the Jacobi smoother is the **degree-zero member** of the
diagonally-scaled-polynomial-smoother family `chebyshev-iteration` parameterises
by degree. But where `chebyshev-iteration` is a genuine fusion-rotation entry —
its `ApplyOrder0` / `ApplyOrderK` element-fused HPC kernels de-fuse into a
parameterised three-term recurrence of L1 leaf primitives — the Jacobi apply has
**no fused multi-operation kernel to unfold** (see §Semantics, "Negative fusion
observation"). The L2 unification (a `polynomial_smoother` combinator subsuming
Jacobi as `order=0` and chebyshev as `order≥1`) is a candidate but **not pursued
here** — Jacobi's per-call action is a plain elementwise scaling, not a
polynomial action, and the unification would obscure the apply's identity with
the underlying elementwise-product field operation.

This is a thin **floor presence** entry. It exists so the firm L3
[`jacobi-smoother`](../L3/jacobi-smoother.md) (cycle-037) rests on a present
adjacent L2 parent, per the methodology invariant **Identity-lowerings still
require both L levels** (CLAUDE.md §Methodology invariants, cycle-009
codification): each layer is coherent within itself, and a reader at L2 must
find `jacobi-smoother` defined in L2 vocabulary without reaching down to L1 or up
to L3. The foundation-first directive `l2-floor-under-l3-jacobi-smoother`
(2026-05-31) names exactly this gap — the L3 constructed-operator-gate cohort
(`jacobi-smoother`, `divfree-projector`, and the obstruction-carrying
`ksp_solve` / `eigsolve`) was backfilled to L3 across cycles 020/037/038 with the
`jacobi-smoother` L3 entry resting on the L1 entry directly, skipping the L2
floor. This dispatch floors `jacobi-smoother`.

## Signature

    jacobi_smoother :: (op: JacobiSmoother[S], x: Tensor[(S: ...)]) -> Tensor[$S]
    jacobi_smoother op x = op.dinv ⊙ x
                         = (ω · diag(A)⁻¹) ⊙ x

Shape contract (bunsen-style named axes; the field shape group `S` follows the
named-shape-group convention of [`l4_calculus`](../semantics/index.md) §1.2.1;
positional values, no monadic effect, no destination buffer):

- **`op`** — `JacobiSmoother[S]` — the constructed smoother closure, an opaque
  value bound once at setup and immutable across calls. Carries
  `op.dinv : Tensor[$S]` (the damped inverse diagonal `ω · diag(A)⁻¹`, congruent
  to the field shape group `S`, same
  element-type as the operator), `op.omega : Real` (the damping factor, already
  absorbed into `dinv` at apply time), and `op.sf_max : Real` (the spectral-bound
  scaling factor, consumed only by the estimated-damping setup). The
  constructed-operator type is **opaque at L2** — the element-type variant and
  the operator-representation axis are absorbed; the L2 contract sees only the
  smoother-action interface.
- **`x`** — `Tensor[$S]` — the input vector (residual / RHS to smooth). Read-only
  at L2 (the L2 form is pure / out-of-place; the L0 in-place output-arg mutation
  is reintroduced only at the L1>L0 lowering).
- **result** — `Tensor[$S]` — the post-smoothing output, a fresh value produced by
  the elementwise product; no L0 destination buffer is mentioned at L2 (the
  destination-binding rotation is an L1>L0 concern). Same shape group `S`.

`JacobiSmoother[S]` is an **opaque constructed type** at L2: its internal
representation (real vs. complex `dinv`; the underlying operator `A`, already
forgotten once `dinv` is committed) is not part of the L2 signature. The setup
that builds `JacobiSmoother[S]` from `(A, omega, sf_max)` — the
`assemble_diagonal → reciprocal → ω-fold` chain, plus the opaque
`spectrum_estimate(A, dinv)` sub-action on the `ω = 0` path — is a separate setup
action (mirroring the L0 `SetOperator` / `Mult` split). It is authoritative at
the L1 entry (`book/src/L1/jacobi-smoother.md` §Signature) and is not re-derived
here; the L2 entry reads the apply, not the setup.

The L2 signature is **identical to the L3 signature** modulo notation, and
identity-in-form to the L1 floor's concrete rank-1 `Tensor[N]` spelling of the
same gate; the rotation is identity-in-form on the gate's apply.

## Semantics

`jacobi_smoother op x` returns the elementwise product of `x` with the damped
inverse diagonal `op.dinv = ω · D⁻¹`. The result is determined entirely by `op`
and `x` — no hidden state, no per-call side effects, no in-place mutation at the
L2 surface. The L2 form is **pure / out-of-place** (the same `op` applied to the
same `x` returns the same `Tensor[$S]` value); the L0 receiver-mutating idiom
(`Mult(x, y)` writes through `y`) is an L1>L0 lowering concern, not L2 algebra.

The apply is **inner-product-free, iteration-free, and reduction-free**: it is a
**single elementwise multiplication** `dinv ⊙ x` — no `apply_linop` call, no
residual recomputation, no `dot` / `nrm2` reduction, no sweep. This is the gate's
defining communication profile: linear-cost, embarrassingly parallel, zero
collective. Where `ksp_solve` folds `krylov-step` over a convergence-tested
trajectory and `chebyshev-iteration` runs an inner `k`-recurrence over an outer
`pc_it` sweep, the Jacobi apply is one base field operation.

The closure carries the **reduced** operator content: the underlying operator `A`
is forgotten once `dinv` is committed at setup. The L2 apply forgets that the
diagonal originated from any operator — it is a pure field operation against a
pre-committed inverse-diagonal vector. The **no-initial-guess precondition** (the
L0 `Mult` body asserts `!this->initial_guess`, `palace/linalg/jacobi.cpp:102`)
carries through to L2 as a precondition on the apply: callers compose
`jacobi_smoother` as a linear map (the gate is the preconditioner *action*, not
the Jacobi *iteration* — the Richardson sweep `y ← y + M·(x − A·y)` is the
consumer's responsibility, realized by wrapping the gate in a Krylov or
multigrid loop). Folding a non-zero initial guess into the apply would require an
`apply_linop` residual call the diagonal gate explicitly avoids.

### Negative fusion observation (the fusion-rotation content)

L2 is the layer where kernel fusion across multiple algebraic operations is
unfolded into composition. **`jacobi_smoother`'s apply has no fused
multi-operation kernel to unfold** — this is the entry's genuine fusion-rotation
fact, and it is a *negative* one. The L0 apply kernel
(`palace/linalg/jacobi.cpp:30-39` real; `:41-70` complex) is a single
`mfem::forall_switch` computing `Y[i] = DI[i] * X[i]` (real) or the four-multiply
componentwise complex product (`YR[i] = DIR[i]·XR[i] − DII[i]·XI[i]`,
`YI[i] = DII[i]·XR[i] + DIR[i]·XI[i]`, `:52-60`); there is no fusion of *distinct
algebraic operations* (no `α·x + β·y` pass, no fused residual-and-direction
update) — only one elementwise product. The complex kernel's four-multiply form
is a *single* elementwise complex product, the base-algebra realisation of
componentwise `ℂ` multiplication, **not** a fused composition of separate L2
primitives. So the fusion rotation here is a **no-op**: the L2 form is identical
to the L1 form because there is nothing to de-fuse.

This is the sharpest contrast with the sibling
[`chebyshev-iteration`](./chebyshev-iteration.md), whose `ApplyOrder0` /
`ApplyOrderK` element-fused HPC kernels DO de-fuse at L2 into a parameterised
three-term recurrence of distinct L1 leaves (`apply_linop`, `axpby`/`axpbypcz`,
`scal`, elementwise diagonal action). The Jacobi smoother, being the degree-zero
member of that family, has only the elementwise diagonal action and no
recurrence — so the de-fusion that produces chebyshev's recurrence produces, for
Jacobi, just the single elementwise product. The degree-zero member is the
fixed point of the fusion rotation.

`MultTranspose` aliases `Mult` (`palace/linalg/jacobi.hpp:43`): the Jacobi
smoother is its own transpose (law 6). For real `dinv` this is the mathematical
identity `M = Mᵀ` for any diagonal matrix; for complex `dinv` this is the
*transpose* (not conjugate-transpose) — the conjugate-`dinv` Hermitian kernel
exists in `Apply<Transpose=true>` (`palace/linalg/jacobi.cpp:61-69`) but is
**dead code** under the current symmetric wiring (no consumer instantiates
`Apply<true>`). Recorded as a non-law below; the symmetric-wiring assumption
matches the SPD precondition the smoother is consumed under.

## Algebraic laws

The six laws that hold at L1 (and transport unchanged to L3) hold unchanged at
L2, because the constructed-operator-gate apply is identity-in-form across both
the L2↔L1 and L3↔L2 rotations. The non-laws also transport unchanged. The laws
are reproduced here so the L2 reader does not have to reach to L1 for the
listing; the L1 entry (`book/src/L1/jacobi-smoother.md` §Algebraic laws) is
authoritative on every factual claim about the Palace surface.

1. **Linearity in `x`.** `jacobi_smoother op (α·x + β·z) = α · jacobi_smoother op x
   + β · jacobi_smoother op z` for any scalars `α`, `β` and vectors `x`, `z`. The
   apply is the linear operator `M = diag(op.dinv)`; elementwise multiplication
   is linear in each argument. Witnessed by the elementwise-multiply kernel
   `Y[i] = DI[i] * X[i]` (`palace/linalg/jacobi.cpp:38`). This is the structural
   law that makes `jacobi_smoother` an `apply_linop`-shaped operation at L2 (it
   consumes a whole tensor and returns its image under the linear map
   `M = diag(dinv)`).

2. **Zero-vector annihilation.** `jacobi_smoother op 0_$S = 0_$S`. Follows from law
   1 with `α = β = 0`.

3. **Diagonal-operator round-trip with `assemble_diagonal`.** For the
   default-damping setup (`ω = 1.0`): `jacobi_smoother (jacobi_setup A 1.0 sf_max)
   x = reciprocal(assemble_diagonal(A)) ⊙ x = D⁻¹ ⊙ x`. Witnessed by the setup
   chain `op.AssembleDiagonal(dinv); dinv.Reciprocal();`
   (`palace/linalg/jacobi.cpp:79-80`). Composes
   [`assemble-diagonal`](../L1/assemble-diagonal.md)'s diagonal-recovery law with
   the elementwise reciprocal; the law that names `jacobi_smoother` as the
   explicit realization of the `assemble_diagonal → reciprocal →
   elementwise_product` diagonal-preconditioner-apply chain. (The `reciprocal`
   and `elementwise_product` primitives have no L2 floor entry yet — see
   §Dependencies and the open question; at L2 the apply is a single field
   operation against the pre-committed `dinv`.)

4. **Damping absorption (`ω`-into-`dinv`).** For any `ω ≠ 0`: `jacobi_setup A ω
   sf_max = scale ω (jacobi_setup A 1.0 sf_max)`, so the damping factor is
   absorbed into the closure's `dinv` at setup and does not surface in the apply.
   Operationally `jacobi_smoother (jacobi_setup A ω ·) x = ω · (D⁻¹ ⊙ x) = (ω ·
   D⁻¹) ⊙ x`. Witnessed by `if (omega != 1.0) { dinv *= omega; }`
   (`palace/linalg/jacobi.cpp:90-93`); the `ω == 1.0` skip is a transparent
   performance trick — algebraically identical to `dinv *= 1.0`.

5. **Estimated-damping degenerate case (`ω = 0.0`).** When `ω = 0.0`, the setup
   substitutes the optimal `ω* = 2/(sf_max · λ_max(D⁻¹A))`; the apply law is
   identical to laws 1 + 4 with the substituted `ω*`: `jacobi_smoother
   (jacobi_setup A 0.0 sf_max) x = (ω* · D⁻¹) ⊙ x`. A setup-side specialization,
   not an apply-time branch — at the L2 apply the gate has already committed to a
   fixed `op.dinv`. Witnessed by `palace/linalg/jacobi.cpp:84-89`.

6. **Self-transpose under symmetric wiring.** `jacobi_smoother_transpose op x =
   jacobi_smoother op x`. Witnessed by `MultTranspose(x, y) const override {
   Mult(x, y); }` (`palace/linalg/jacobi.hpp:43`). For real `dinv` this is the
   mathematical identity `M = Mᵀ` for any diagonal matrix; for complex `dinv`
   this is the *transpose* (not conjugate-transpose) — see the non-law below.

Laws that explicitly **do not** hold (inherited unchanged from L1):

- **Hermitian-transpose identity for complex `dinv`.** Palace's `MultTranspose`
  aliases the *transpose* kernel (`palace/linalg/jacobi.hpp:43` calls `Mult`, not
  `Apply<true>`), so the realized `MultTranspose` is the transpose, not the
  Hermitian, for complex `dinv`. The conjugate-`dinv` Hermitian kernel exists in
  `Apply<Transpose=true>` (`palace/linalg/jacobi.cpp:61-69`) but is **dead code**
  under the current symmetric wiring. Recorded as a non-law because the law one
  might *expect* (Hermitian-transpose = conj-`dinv` apply) is not the law the
  source realizes; aligns with the SPD precondition under which the gate is
  consumed.

- **No fusion identity to assert.** Unlike the fold-cohort entries (whose laws
  include a fold-specialization identity, e.g. `scal(α,x) = linear_combination
  [(α,x)]`), `jacobi_smoother` has **no fold-parent and no fusion-decomposition
  identity** — its apply is a single field operation, not a fused composition of
  separable L2 primitives. The closest structural statement is law 3 (the
  diagonal-preconditioner-apply chain), which is a *setup-side* composition, not
  an apply-time fusion. Recorded as a deliberate absence: there is no
  fusion-rotation law because there is no fusion to rotate.

- **Iteration / multi-sweep equivalence.** `jacobi_smoother` is a *single-step*
  application: there is no `pc_it` parameter (contrast `chebyshev-iteration`'s
  outer sweeps). Two consecutive applies `M·M·x = M²·x` is the *square* of the
  preconditioner map, **not** a Jacobi sweep on the residual (which would be
  `M·(x − A·M·x)`). The Jacobi *iteration* is the consumer's responsibility — the
  bare L2 gate is the preconditioner action, not the iteration.

- **Bit-determinism across operator representations.** Inherited from
  [`assemble-diagonal`](../L1/assemble-diagonal.md): a matrix-free high-order
  Nedelec `A` yields a value-approximate `dinv` (face-dof sharing in 3D), so the
  apply value differs from the assembled-`A` case. Load-bearing per CLAUDE.md
  §"Optimization tricks vs. base algebra"; the L2 algebraic laws hold, but their
  floating-point realisations are representation-dependent.

The non-law set is **inherited unchanged** from L1; the L2 rendering introduces
no new non-laws. This is what makes the L2↔L1 hop identity-in-form on the gate's
apply: the entire algebraic profile (laws + non-laws) transports unchanged.

## Dependencies

**Same-layer (L2)**: the per-call apply has **no L2 operator dependencies** — it
is one elementwise product. Where `ksp_solve` lists `krylov-step` as a direct
dependency, `eigsolve` lists `ksp_solve` + `apply_linop`, and
`chebyshev-iteration` lists `apply_linop` / `axpby` / `scal` + the elementwise
diagonal action, `jacobi-smoother`'s apply lists **none**. The single elementwise
product `op.dinv ⊙ x` would be the L2 `elementwise_product` primitive — but
**no L2 `elementwise_product` (nor `reciprocal`) floor entry exists yet**: both
are firm at L1 and at L3 (cycle-038) but the L2 floor for the elementwise
primitives has not been built. At L2 the Jacobi apply is therefore a single base
field operation below the layer's current resolution (the same situation as the
L3 entry, where the elementwise product is below L3's resolution and the apply
lists no L3-operator dependency). Once the L2 `elementwise_product` floor lands,
this entry's body becomes the single call `elementwise_product(op.dinv, x)`; the
forward-reference is recorded as an open question, not a live link (the target
file does not exist — `rough-in-forward-reference-must-be-plain-text-not-live-link`).

The setup-side dependencies ([`assemble-diagonal`](../L1/assemble-diagonal.md)
for the `op.AssembleDiagonal(dinv)` step, elementwise `reciprocal` for
`dinv.Reciprocal()`, and the opaque `spectrum_estimate` for the `ω = 0` path) are
L1-entry concerns, not part of the L2 apply — they are consumed once at
construction, before the gate is folded into any L2 expression.

**Fold-parent**: **none.** `jacobi-smoother` is a standalone constructed-operator
gate, NOT a member of the `linear_combination` (reduce-to-`Tensor[N]`) or
`inner_product` (reduce-to-`Scalar`) fold cohort. This is the explicit
fork-independence fact: the cycle-041 `dot-l2-leaf-floor-vs-fold-only-design`
leaf-vs-fold fork (pending the batch-12 meta-phase) governs whether the BLAS-1
leaves get same-named L2 floors or fold-only treatment; it does not reach this
gate, which has no fold-parent on either codomain.

**Cross-cutting concepts**:

- [`constructed-operators`](../concepts/constructed-operators.md) — the
  level-(c) variant absorption of operator-representation; the
  `JacobiSmoother[S]` closure is the canonical thinnest instance (it carries
  only the inverse diagonal, having forgotten `A`).
- [`variant-absorption`](../concepts/variant-absorption.md) — the level-(b)/(c)
  absorption discipline; the element-type and damping-mode axes are absorbed into
  the closure, the operator-representation axis into `dinv` at setup.

**L1 anchor**: [`L1/jacobi-smoother`](../L1/jacobi-smoother.md) (firm; the
constructed-operator gate at L1) — authoritative on the Palace surface details,
the setup chain, the `spectrum_estimate` opaque sub-action, the dead-code
Hermitian kernel caveat, and the complete L0 evidence list. This L2 entry does
not duplicate those details; the L2↔L1 rotation is identity-in-form on the gate's
apply.

**L3 consumer**: [`L3/jacobi-smoother`](../L3/jacobi-smoother.md) (firm
cycle-037) — the iteration-rotation rendering this L2 floor sits beneath. The
L3↔L2 rotation is identity-in-form (the apply is a single whole-tensor field
operation at both layers); no `L3-L2/jacobi-smoother` theme file is needed (the
identity annotation lives in-line per the cycle-012 non-adjacent-identity
convention).

**Sibling (cited, NOT a dependency)**:
[`chebyshev-iteration`](./chebyshev-iteration.md) — the degree-`≥1` member of the
diagonally-scaled-polynomial-smoother family of which `jacobi-smoother` is the
degree-zero member. Same setup chain (`AssembleDiagonal + Reciprocal`); the
Jacobi apply is the chebyshev recurrence collapsed to its initial elementwise
diagonal action with no recurrence.

## Variant axes

`jacobi_smoother` has **two orthogonal variant axes at L2, plus one absorbed
axis** — the same framing as L1 / L3, transported unchanged. All three are
absorbed into the constructed-operator closure; none appears in the per-call
apply's positional signature.

Two orthogonal axes:

1. **element-type** (`real` | `complex`) — collapsed into the opaque
   `JacobiSmoother[S]` closure. The L0 source instantiates both (`template class
   JacobiSmoother<Operator>;` and `<ComplexOperator>`,
   `palace/linalg/jacobi.cpp:106-107`); the apply is identical in form (one
   elementwise product) and the per-element kernel dispatches on element type
   (`palace/linalg/jacobi.cpp:30-39` real; `:41-70` complex). The complex `dinv`
   is a *true complex* inverse diagonal (divergence from `chebyshev`'s real-only
   `dinv`, `palace/linalg/chebyshev.hpp:37`); at L2 the apply respects the
   complex structure fully via the four-multiply componentwise complex product.

2. **damping-mode** (`default ω = 1.0` | `fixed ω ≠ 0` | `estimated ω = 0`) —
   collapsed into `op.dinv`'s *committed* damping value at setup. The L0 source
   carries the three modes as ctor-argument branches; at L2 they collapse to one
   gate parameterised by the absorbed `dinv` (the apply does not branch on
   damping mode — the setup computes the absorbed `dinv`, the apply reads it).
   The `sf_max` spectral-bound scaling factor is a construction parameter carried
   in `op.sf_max`, *not* a variant axis (it parameterises one gate per call site,
   surfacing only in the `ω = 0` setup arithmetic at
   `palace/linalg/jacobi.cpp:87-88`).

Absorbed axis:

- **operator-representation** (`sparse-CSR | matrix-free-Nedelec |
  parallel-wrapped | complex-wrapped`) — **collapsed at setup** through the
  [`assemble-diagonal`](../L1/assemble-diagonal.md) operator's own
  representation-axis absorption. By the time `dinv` is committed to the closure,
  the representation distinction has been erased; the matrix-free-Nedelec
  approximation propagates as a non-law (the bit-determinism non-law above), not
  as a fresh axis.

The variant-axis profile (two orthogonal + one absorbed) matches the L1 and L3
entries exactly. **No new axes introduced by the L2 rendering; no axes merged or
split.**

## Status

`firm` — the L2 form is value-thread-isomorphic to the firm L1 form on the
constructed-operator-gate apply (identity-in-form rotation), and equally to the
firm L3 form above it; the algebraic laws are the same six that hold at L1
(linearity, zero-vector annihilation, the `assemble_diagonal` round-trip, damping
absorption, the estimated-damping degenerate case, self-transpose under symmetric
wiring); the non-laws are catalogued explicitly (the dead-code Hermitian-transpose
non-realisation, the no-fusion-identity absence, the no-iteration non-equivalence,
and the representation-dependent bit-determinism non-law); the variant-axis
profile is two orthogonal + one absorbed, inherited unchanged. The
constructed-operator-gate framing matches the firm L2
[`ksp_solve`](./ksp_solve.md) / [`eigsolve`](./eigsolve.md) precedents — opaque
constructed-operator argument, operator-representation absorbed.

**Firm-on-positive-structure.** The firm-on-positive-structure precedent (the firm
L1 `jacobi-smoother` / `apply_linop` / `chebyshev-smoother`) governs the absence
of a dedicated `test-jacobi.cpp` under `reference/palace/test/unit/`: every L2 law
is a syntactic identity readable straight off positive source — elementwise
multiply at `palace/linalg/jacobi.cpp:38`; setup chain at `:79-93`; transpose
alias at `palace/linalg/jacobi.hpp:43`; instantiations at
`palace/linalg/jacobi.cpp:106-107` — not literature-inferred convergence claims,
so the missing dedicated test does not gate firm. Behaviour is exercised through
integration paths only (`palace/linalg/ksp.cpp:198-200`, the principal Jacobi
consumer; four further consumer sites per the L1 entry —
`errorestimator.cpp:75-77`, `floquetcorrection.cpp:65`, `spaceoperator.cpp:640`,
`timeoperator.cpp:85`).

This dispatch (cycle-042 D5) is the **L2 floor backfill** under the
foundation-first directive `l2-floor-under-l3-jacobi-smoother`: the L2 form was
previously implicit only in the L1 and L3 entries; it now has its own L2 entry per
**Identity-lowerings still require both L levels**, so the firm L3
[`jacobi-smoother`](../L3/jacobi-smoother.md) (cycle-037) rests on a present
adjacent L2 parent rather than skipping a layer down to L1. It is **fork-INDEPENDENT** —
a standalone constructed-operator gate with no fold-parent, not subject to the
cycle-041 leaf-vs-fold design fork.

**Caveats (not status reductions):**

- The complex `Apply<Transpose=true>` Hermitian kernel
  (`palace/linalg/jacobi.cpp:61-69`) is dead code under symmetric wiring —
  `MultTranspose` aliases `Mult`, not `Apply<true>`. The conjugate-`dinv`
  Hermitian-transpose law is therefore *not realized* by the Palace surface even
  though the source contains the machinery. Inherited from the L1 entry's caveat;
  recorded as a non-law (above) and as the open question
  `reciprocal-elementwise-product-mr-dead-code-transpose-consumer-branch`.
- The `ω = 0.0` estimated-damping mode's setup-time correctness depends on the
  opaque `spectrum_estimate` sub-action (out-of-scope at L2), but the per-call
  apply law is identical regardless of damping mode (law 1 with the substituted
  `ω`).
- No L2 `elementwise_product` / `reciprocal` floor entry exists yet; the apply is
  recorded as a single base field operation below the layer's current resolution
  (forward-reference plain-text, open question below). This does not gate firm —
  the L2 form is identity-in-form to L1 regardless.

## Lowers to

L2 `jacobi-smoother` lowers to L1 [`jacobi-smoother`](../L1/jacobi-smoother.md)
via a **degenerate identity-in-named-terms** rotation, annotated in-line here
rather than as a dedicated L2>L1 theme file: the L2 form sees `jacobi_smoother ::
(op: JacobiSmoother[S], x: Tensor[(S: ...)]) -> Tensor[$S]` and the L1 floor the
concrete rank-1 `Tensor[N]` spelling of the same gate, with the same shape contract,
the same six algebraic laws, the same non-law set, and the same
two-orthogonal-plus-one-absorbed variant profile. There is **no kernel fusion to
unfold** — the apply is a single elementwise product (the negative fusion
observation above), so there is no vocabulary shift across the edge to rotate.
(The former `jacobi-smoother-leaf-identity` L2>L1 theme file was demoted to this
in-line note cycle-051 under the 2026-06-01 VOCABULARY-SHIFT REDIRECT
`METHODOLOGY-REDIRECT.md` — a degenerate identity-in-named-terms lowering, the §1d
smell the redirect names; cycle-050 D8 verify-body audit DEMOTE-OK,
`reports/2026-06-01T195100Z-cross-layer-cross-cutter-verify-divfree-jacobi/CYCLE.md`.)
This follows the `scal` / `dot` / `nrm2` L2-floor precedent for in-line
identity-rotation annotation.

The **substantive** rotation in the chain is the L1>L0 leaf-mutation rotation, not
the L2↔L1 hop: the apply's single elementwise product `op.dinv ⊙ x` lowers to
Palace's in-place `mfem::forall_switch` element-loop `Y[i] = DI[i] * X[i]`
writing through the output argument `y`. That rotation is captured by the firm
L1>L0 theme
[`reciprocal-elementwise-product-mutation-rotation`](../L1-L0/reciprocal-elementwise-product-mutation-rotation.md)
(sub-pattern B — the `elementwise_product` leaf; the consumer-duplicate
`Apply(dinv, x, y)` kernel at `palace/linalg/jacobi.cpp:30-39`) and the
constructed-operator-closure theme
[`jacobi-smoother-mutation-rotation`](../L1-L0/jacobi-smoother-mutation-rotation.md).
None of that destination-binding / `forall_switch` content is L2 content; the L2
form sees a single base elementwise product.

## Lifts from

L3 `jacobi-smoother` (firm cycle-037) lifts to this L2 entry — equivalently, this
L2 floor sits beneath the firm L3 entry — via the **value-thread-isomorphic**
identity rotation: the L3 form's signature has no element loop exposed, no
destination buffer, no MPI collective, and no kernel fusion — exactly the
properties that make it L2-native by construction as a base field operation. The
L2 entry exists for layer-coherence reasons: a reader navigating L2 (whose index
advertises base primitive operations and constructed-operator gates as L2
vocabulary) must find `jacobi-smoother` defined in L2 vocabulary, not have to
reach down to L1 or up to L3 to recover the constructed-operator-gate apply. The
firm L2 `scal` floor backfill (cycle-041) is the structural precedent for the
identity-in-form L2-floor-under-L3 backfill; the firm L2 `ksp_solve` (cycle-021)
and `eigsolve` (cycle-023) are the constructed-operator-gate siblings.

## Evidence

The L2 form is value-thread-isomorphic to the firm L1 form (per the
identity-in-form rotation on the constructed-operator-gate apply) and to the firm
L3 form above it; all L0 evidence is transitive through L1. Direct citations
relevant to this L2 entry (self-verified via `tools/citecheck/citecheck.py
--anchor` against on-disk `reference/palace/palace/linalg/jacobi.{hpp,cpp}` /
`ksp.cpp` / `errorestimator.cpp`, 2026-06-01):

- `book/src/L1/jacobi-smoother.md` (firm) — the L1 entry whose signature,
  semantics, six algebraic laws, non-laws, two-orthogonal-plus-one-absorbed
  variant profile, and complete L0 evidence list are transported unchanged to L2.
  Authoritative on every Palace-surface factual claim.
- `book/src/L3/jacobi-smoother.md` (firm cycle-037) — the L3 iteration-rotation
  rendering this L2 floor sits beneath; identical signature, laws, and variant
  axes (the L3↔L2 hop is identity-in-form).
- `book/src/L2/scal.md` (firm cycle-041 D3) — the L2-floor-under-L3 structural
  precedent (identity-in-form floor; in-line identity-rotation annotation).
- `book/src/L2/chebyshev-iteration.md` (firm cycle-012) — the degree-`≥1`
  polynomial sibling; the genuine fusion-rotation entry (`ApplyOrder0` /
  `ApplyOrderK` de-fusion) against which the Jacobi apply's no-fusion fact is the
  degree-zero contrast.
- `palace/linalg/jacobi.cpp:30-39` — real `Apply<Transpose>(dinv, x, y)`:
  `mfem::forall_switch(use_dev, N, [=] (int i) { Y[i] = DI[i] * X[i]; });` — the
  single elementwise-multiply kernel that realises the apply (law 1 witness; the
  body the L2 elementwise product is). Self-verified — anchor `Y[i] = DI[i] *
  X[i]` at `:38`.
- `palace/linalg/jacobi.cpp:41-70` — complex `Apply<Transpose>(dinv, x, y)`: the
  forward branch (`:52-60`) realises the four-multiply componentwise complex
  product (a single elementwise complex product, not a fused composition); the
  `Transpose = true` branch (`:61-69`) computes the conjugate-`dinv` apply (dead
  code under symmetric wiring; the non-law witness). Self-verified.
- `palace/linalg/jacobi.cpp:74-97` — `JacobiSmoother<OperType>::SetOperator(op)`:
  the setup body. `op.AssembleDiagonal(dinv)` (`:79`), `dinv.Reciprocal()`
  (`:80`) — the `assemble_diagonal → reciprocal` chain (law 3); the `ω = 0`
  optimal-damping computation (`:84-89`, law 5); the `ω`-fold `dinv *= omega;`
  (`:90-93`, anchor at `:92`, law 4). Self-verified — anchors `AssembleDiagonal`
  at `:79`, `Reciprocal` at `:80`, `dinv *= omega` at `:92`.
- `palace/linalg/jacobi.cpp:99-104` — `JacobiSmoother<OperType>::Mult(x, y)
  const`: the apply entry; `MFEM_ASSERT(!this->initial_guess, ...)` (`:102`) —
  the no-initial-guess precondition; `Apply(dinv, x, y);` (`:103`) — the single
  dispatch that is the entire per-call action. Self-verified — anchors
  `initial_guess` at `:102`, `Apply(dinv, x, y)` at `:103`.
- `palace/linalg/jacobi.hpp:19` — `class JacobiSmoother : public Solver<OperType>`
  — the class declaration. Self-verified.
- `palace/linalg/jacobi.hpp:28` — `VecType dinv;` — the inverse-diagonal member
  (`VecType = Vector` for real, `= ComplexVector` for complex). Self-verified.
- `palace/linalg/jacobi.hpp:43` — `void MultTranspose(...) const override {
  Mult(x, y); }` — the transpose self-alias (law 6) and the source of the
  dead-code Hermitian caveat. Self-verified.
- `palace/linalg/jacobi.cpp:106-107` — `template class JacobiSmoother<Operator>;
  template class JacobiSmoother<ComplexOperator>;` — the element-type variant axis
  instantiation. Self-verified — anchor `JacobiSmoother<Operator>` at `:106`.
- `palace/linalg/ksp.cpp:198-200` — the principal consumer: `case
  LinearSolver::JACOBI: pc = std::make_unique<JacobiSmoother<OperType>>(comm);
  break;` — the default-damping preconditioner-instantiation site inside
  `ConfigurePreconditioner`. Self-verified — anchor `JACOBI` at `:198`.
- `palace/linalg/errorestimator.cpp:75-77` — the only `ω = 0.0` estimated-damping
  call site ("Use eigenvalue estimate to compute optimal Jacobi damping
  parameter."); the third value of the damping-mode variant axis. Self-verified —
  anchor `JacobiSmoother` at `:76`.
- `palace/linalg/chebyshev.cpp:177-178` — sibling-precedent: the *identical*
  `op.AssembleDiagonal(dinv); dinv.Reciprocal();` setup chain inside
  `ChebyshevSmoother::SetOperator` — establishes `jacobi-smoother` as the
  degree-zero member of the diagonally-scaled-polynomial-smoother family.
- `book/src/L1-L0/reciprocal-elementwise-product-mutation-rotation.md` (firm) —
  the L1>L0 leaf-mutation rotation the apply's elementwise product lowers through
  (sub-pattern B; the `elementwise_product` leaf + the consumer-duplicate
  `Apply(dinv, x, y)` kernel). The substantive rotation in the chain; not L2
  content (referenced forward for the downward narrative).
- `book/src/L1-L0/jacobi-smoother-mutation-rotation.md` (firm) — the
  constructed-operator-closure L1>L0 theme.
- `book/src/L2/ksp_solve.md` (firm cycle-021), `book/src/L2/eigsolve.md` (firm
  cycle-023) — the L2 constructed-operator-gate siblings this entry follows in
  framing.

## L2 vs L1 distinction

- **L1**: constructed-operator gate as a pure-functional smoother action — the
  mutation-rotated form of the L0 `JacobiSmoother<OperType>::Mult(x, y)`
  output-arg-write idiom (the destination buffer `y` dropped from the signature;
  the `initial_guess` parameter dropped as a precondition; the element-type and
  damping-mode collapsed into the closure). The L1 vocabulary frames the gate
  against the L0 source — emphasising the *mutation rotation*.
- **L2**: constructed-operator gate as a base-algebra field operation — the
  *fusion-rotation* reading, in the layer where kernel fusion is unfolded into
  composition. **The gate's apply is identity-in-form to L1** — and the
  fusion-rotation content is *negative*: there is no fused multi-operation kernel
  to unfold (the apply is one elementwise product), so the fusion rotation is a
  no-op. The L2 entry exists for layer-coherence: a reader at L2 finds the gate
  defined in L2 vocabulary, without having to drop down to L1.

The L2 ↔ L1 rotation is identity-in-form on the body and signature; the surface
adjustment is documentary (mutation rotation at L1 vs the negative fusion
observation at L2). The methodology invariant **each layer is coherent within
itself** is what compels the L2 entry to exist as its own anchor — and the
foundation-first directive `l2-floor-under-l3-jacobi-smoother` is what schedules
it, so the firm L3 [`jacobi-smoother`](../L3/jacobi-smoother.md) rests on a
present adjacent L2 parent.
