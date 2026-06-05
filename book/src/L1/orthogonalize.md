# orthogonalize

Mutation-lifted Gram-Schmidt orthogonalisation: given a stored basis `V[0..m-1]` and a
candidate vector `w`, produce the component `w'` of `w` orthogonal to `span(V)` together
with the projection coefficients `H[0..m-1]` (the leading entries of the Arnoldi/Hessenberg
column). The field-side core of the Krylov Arnoldi inner loop and of the ROM
basis-extension path. One runtime variant axis (`MGS | CGS | CGS2`).

## Context

`orthogonalize` lifts Palace's header-only inline Gram-Schmidt family —
`linalg::OrthogonalizeColumnMGS` and `linalg::OrthogonalizeColumnCGS` (with the `refine`
flag selecting CGS2), both in `palace/linalg/orthog.hpp` — to a single pure-functional
operator. The runtime dispatch over the three variants is the wrapper
`OrthogonalizeIteration` at `palace/linalg/iterative.cpp:308-325`, which switches on the
`Orthogonalization` enum (`MGS`, `CGS`, `CGS2`) and forwards to the two implementations
(`CGS2` is `OrthogonalizeColumnCGS(..., refine=true)`). The same family is invoked by the
ROM operator's basis-extension path via `romoperator.cpp:51-66`.

The L0 form is a mutating member idiom: it overwrites the candidate `w` in place
(`w.Add(-H[j], V[j])`) and writes the coefficients through a raw pointer `H` into the
caller's Hessenberg-column buffer. The L1 form drops both destination buffers from the
signature: the operator consumes `w`, `V`, and the variant, and produces a fresh pair
`(w', H)`. Buffer ownership, the in-place overwrite of `w`, and the raw-pointer `H` write
are L0 concerns; they reappear in the L1>L0 lowering theme, not in the L1 signature.

A load-bearing scope note from the L0 header (`orthog.hpp:18-23`): the routine **assumes
the basis columns `V[j]` are normalised and does not normalise the output `w'`**
("normalization has to be managed by hand"). Normalisation is therefore *not* part of this
operator — the caller (`arnoldi_step`) follows `orthogonalize` with `nrm2(w')` (the
Hessenberg sub-diagonal) and `scal(1/‖w'‖, w')`. The coefficient `H[j+1] = ‖w'‖` that the
concept page attaches to the "full Hessenberg column" is the *caller's* `nrm2` step, not a
product of this operator. This entry returns the length-`m` coefficient vector only.

A cross-cutting prose treatment lives at [`concepts/orthogonalization`](../concepts/orthogonalization.md);
the MGS-vs-CGS sequential-obstruction structure is at
[`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md) §"Example: MGS as
sequential-obstruction". The L1 entry here is the firm operator definition; the concept
pages are the narrative. Where they disagree on the coefficient/normalisation boundary, this
entry is authoritative.

## Signature

```text
orthogonalize :: (w: Tensor[N], V: Basis[N, m], variant: GSVariant) -> (Tensor[N], Tensor[m])
orthogonalize(w, V, variant) = (w', H)   where   H[j] = ⟨w_eff(j), V[j]⟩,   w' = w − Σ_j H[j]·V[j]
```

Shape contract (bunsen-style, named axes):

- `w` — `Tensor[N]` — read-only (the *prior* candidate; the un-normalised input).
- `V` — `Basis[N, m]` — read-only; `m` columns each of length axis `N`, assumed normalised
  (`‖V[j]‖ = 1`) and mutually orthogonal (`⟨V[i], V[j]⟩ = δ_ij`) as an input precondition.
- `variant` — `GSVariant ∈ {MGS, CGS, CGS2}` — bound once at solve setup; inspected exactly
  once (dispatch). Not re-inspected per column.
- result `w'` — `Tensor[N]` — same length axis `N`; the orthogonal residual,
  **not normalised**.
- result `H` — `Tensor[m]` — the projection coefficients (leading `m` entries of the
  Hessenberg column). Element type matches `w` / `V` (real or complex).

The `m = 0` case (empty basis) is well-defined and is the identity: `orthogonalize(w, [],
variant) = (w, [])`. (Witnessed across all three variants at `test-orthog.cpp:99-120`.)

Coefficient convention. `H[j] = ⟨w_eff(j), V[j]⟩` is the inner product with the candidate as
the **first** (conjugated, for complex) argument — matching the L0 `dot_op(w, V[j])` order
and the header comment "Note order is important for complex vectors" (`orthog.hpp:48`). This
follows the L1 [`dot`](./dot.md) convention (conjugate-linear in the first argument). `w_eff(j)`
is the candidate as seen by column `j`: for CGS it is the original `w` for every `j`; for MGS
it is the progressively-updated `w` after subtracting columns `0..j-1` (see Semantics). The
inner-product hook is a variant axis (the SLEPc/ROM B-weighted dot is a `dot_op`
substitution; see Variant axes).

## Semantics

The operator removes the `span(V)`-component of `w`, returning the orthogonal residual and
the coefficients of the removed component. In **exact arithmetic with an exactly orthonormal
`V`**, all three variants compute the same `(w', H)`: `H[j] = ⟨w, V[j]⟩` and
`w' = (I − V Vᴴ) w`, the orthogonal projection of `w` onto `span(V)`'s complement. The
variants differ only in finite precision and in their collective/dependency shape — this is
the entire reason all three exist.

- **CGS (classical).** Every coefficient is taken against the *same original* `w`:
  `H[j] = ⟨w, V[j]⟩` for all `j`, then `w' = w − Σ_j H[j]·V[j]`. The `m` inner products are
  mutually independent; there is no inter-`j` ordering.
- **MGS (modified).** Each coefficient is taken against the *progressively-updated*
  candidate: `H[j] = ⟨w^(j), V[j]⟩` where `w^(0) = w` and `w^(j+1) = w^(j) − H[j]·V[j]`, and
  `w' = w^(m)`. Equivalently `w' = (I − V[m-1] V[m-1]ᴴ) ⋯ (I − V[0] V[0]ᴴ) w` — a
  left-to-right composition of `m` rank-1 projectors. The `j+1`-th coefficient depends on the
  `j`-th update; the dependency is intrinsic, not an implementation artefact.
- **CGS2 (re-orthogonalised classical).** CGS applied twice: a first CGS pass produces a
  once-orthogonalised `w` and coefficients `H`; a second CGS pass against that `w` produces a
  correction `dH`; the returned coefficients are `H + dH` (so a caller recovers the full
  projection) and the returned residual is the twice-projected `w`. The second pass reads the
  once-orthogonalised `w` and is *not* algebraically fusible with the first ("twice is
  enough" — Kahan/Parlett — recovers MGS-level orthogonality precisely because `V` is only
  approximately orthonormal in practice).

The variant tag is inspected exactly once (the dispatch in `OrthogonalizeIteration`); per
[`variant-absorption`](../concepts/variant-absorption.md) MGS/CGS/CGS2 absorb at **all three
levels (a/b/c) under residual-axis disclosure** for the L2 collective shape
(`variant-absorption.md:131`): (a) the invariant unifies (law 1, the orthogonality contract
is variant-uniform), (b) the variant is bound at solve setup and threaded as a constructed
parameter with no per-column re-branch, and (c) the L_{n+1} primitive chain is the same
`[dot, axpy]` shape across all three — the only residual is the per-variant collective shape
(m×1 / 1×m / 2×m reductions), explicitly disclosed as the residual axis.

The MPI collective is **not** in the L1 signature (single-rank scope per `CLAUDE.md`). The
*number and size* of collectives differs across variants — MGS does `m` reductions of size
1, CGS does 1 of size `m`, CGS2 does 2 of size `m` — and this cost shape is the load-bearing
distinction that motivates the variant axis. At L1 it is recorded as a per-variant property;
it materialises as actual `MPI_Allreduce` calls only in the L1>L0 lowering. The
reduction-tree non-associativity inherited from [`dot`](./dot.md) is load-bearing in the same
sense as for `dot`/`nrm2`.

## Algebraic laws

The laws below hold; absences are deliberate. "Exact" means exact arithmetic with an exactly
orthonormal input basis `V`; floating-point caveats are recorded as explicit non-laws.

1. **Orthogonality (the defining contract).** `⟨w', V[i]⟩ = 0` for all `i ∈ [0, m)` (exact).
   This is the L1 contract shared by **all three variants** — it is what makes them
   substitutable. Witnessed empirically across MGS / CGS / CGS2 at `test-orthog.cpp:154-159`
   (the per-column orthogonality-check loop; the `⟨w', V[i]⟩ ≈ 0` assertion is at line 158)
   (and the complex / B-weighted parametrisations).
2. **Projection-coefficient identity.** In exact arithmetic with orthonormal `V`,
   `H[j] = ⟨w, V[j]⟩` and `w' = w − Σ_j H[j]·V[j]`, so `w = w' + Σ_j H[j]·V[j]` recovers the
   input. The pair `(w', H)` is a complete (loss-free) decomposition of `w` into its
   `span(V)` and `span(V)^⊥` parts.
3. **Identity on the empty basis.** `orthogonalize(w, [], variant) = (w, [])` for any `w` and
   any variant (the `m = 0` path returns `w` unchanged; `test-orthog.cpp:99-120`).
4. **Idempotence (exact).** `orthogonalize(w', V, variant)` returns `(w', 0)` — re-running on
   an already-orthogonal residual is a no-op on `w'` and yields zero coefficients (exact).
   This is the projector identity `(I − V Vᴴ)² = (I − V Vᴴ)` for orthonormal `V`. In finite
   precision the second pass yields a small non-zero correction — *which is exactly the
   mechanism CGS2 exploits* (CGS2 = one explicit re-application of this law to recover lost
   orthogonality).
5. **Linearity in the candidate (exact).** `orthogonalize(α·w₁ + w₂, V, variant)` has
   residual `α·w'₁ + w'₂` and coefficients `α·H₁ + H₂` (exact arithmetic; the projection
   `I − V Vᴴ` and the coefficient map `Vᴴ` are both linear). Conjugate-linearity in the
   complex case follows the [`dot`](./dot.md) first-argument convention.
6. **Variant agreement (exact).** MGS, CGS, and CGS2 return the *same* `(w', H)` in exact
   arithmetic with exactly orthonormal `V`. The three variants are one operator at the
   exact-arithmetic level; they diverge only in finite precision and in collective shape.

Laws that explicitly **do not** hold:

- **Variant agreement in floating point.** Law 6 fails in finite precision: the three
  variants produce different `(w', H)` at the bit level (and at larger amplitudes when `V` is
  ill-conditioned). This *is* the variant axis — recorded, not erased. MGS and CGS2 hold
  orthogonality to roundoff; CGS loses it faster for ill-conditioned bases.
- **Reduction-tree associativity (floating point).** Inherited from [`dot`](./dot.md):
  different summation orders give different bit-level coefficients. Load-bearing.
- **Linearity / idempotence at the bit level.** Laws 4 and 5 are exact-arithmetic identities;
  in floating point they hold only up to the orthogonality floor of the chosen variant.
- **Commutativity of the column order under MGS.** Permuting the columns of `V` changes the
  intermediate `w^(j)` and hence the MGS `(w', H)` at the bit level (CGS/CGS2 are
  column-order-invariant up to reduction-tree noise; MGS is not, because the left-to-right
  projector composition does not commute). This is the algebraic shadow of the MGS sequential
  dependency.

## Dependencies

- [`dot`](./dot.md) (firm) — the projection-coefficient inner product `H[j] = ⟨w, V[j]⟩`. The
  conjugate-linear first-argument convention is inherited directly.
- [`axpy`](./axpy.md) (firm) — the rank-1 residual update `w ← w − H[j]·V[j]` is
  `axpy(-H[j], V[j], w)`.

These two are the leaf BLAS-1 primitives the operator composes; the composition itself (the
per-variant sequencing and batching of `dot` and `axpy`) is L1>L0 / L2 territory and is not
restated here (it lives in the `orthog` slice's retained L2/L3/L4 sections and the forthcoming
L1>L0 orthogonalize-mutation-rotation theme). `nrm2` and `scal` are **not** dependencies of
this operator — they are the caller's normalisation step (`arnoldi_step`), excluded by the
header's "does not normalize the output" contract.

The reverse direction (consumers): [`ksp_solve`](./ksp_solve.md) via the GMRES/FGMRES Arnoldi
inner loop; the ROM basis-extension path; the L2 [`krylov-step`](../L2/krylov-step.md)
composition surface references `orthogonalization` as an all-three-level-absorbed
(residual-axis-disclosed; the residual is the per-variant collective shape) component.

## Variant axes

`orthogonalize` has two variant axes at L1:

- **gs_orthog** — `MGS | CGS | CGS2`. The primary runtime axis. At L0 these are
  `OrthogonalizeColumnMGS`, `OrthogonalizeColumnCGS`, and `OrthogonalizeColumnCGS(refine=true)`,
  dispatched by `OrthogonalizeIteration` (`iterative.cpp:308-325`). At L1 the *contract* is
  uniform across all three (law 1); the axis is preserved as a first-class residual axis
  because the variants differ in collective shape (m×1 / 1×m / 2×m reductions) and
  finite-precision stability — both load-bearing. Per
  [`variant-absorption`](../concepts/variant-absorption.md) (`:131`), MGS/CGS/CGS2 absorb at
  **all three levels (a/b/c) under residual-axis disclosure** for the L2 collective shape: the
  invariant unifies, the variant is inspected once at dispatch and never per-column, and the
  L_{n+1} primitive chain is the same `[dot, axpy]` shape; only the collective shape is the
  disclosed residual axis. **Householder is scoped out**: `variant-absorption.md:131` names a
  fourth orthogonalization variant (Householder) that threads a *reflector sequence* —
  fundamentally different state, with an L_{n+1} chain of `[reflect_apply, reflect_zero]`
  instead of `[dot, axpy]`, breaking level-(c) absorption. Palace's L0 has no Householder path
  (`orthog.hpp` defines exactly the two functions `OrthogonalizeColumnMGS` /
  `OrthogonalizeColumnCGS`), so Householder is out of scope for this operator per the
  unimplemented-component policy. The MGS branch carries a
  [sequential-obstruction](../concepts/sequential-obstruction.md) that surfaces at L3 (MGS has
  no global tensor-field form; CGS/CGS2 lift cleanly) — that obstruction is an L3 property of
  the variant, not an L1 contract distinction.
- **inner-product hook (`dot_op`)** — `identity (canonical ⟨·,·⟩) | B-weighted`. The L0
  family is templated over an `InnerProductHelper` (`orthog.hpp:25-37`,
  `IdentityInnerProduct`); the SLEPc/ROM paths substitute a `B`-weighted dot
  (`romoperator.cpp:59-65`, `test-orthog.cpp:276-389` weighted cases). At L1 this is a
  substitution of the [`dot`](./dot.md) used for `H[j]` (and equivalently a
  [`matrix-weighted-norm`](./matrix-weighted-norm.md)-flavoured inner product); the
  orthogonality contract becomes `⟨w', V[i]⟩_B = 0`. The operator's shape and laws are
  unchanged under the substitution; only the inner-product realisation differs.

The **element-type** axis (`real | complex`) is fully parametric (the L0 functions are
templated over `VecType ∈ {Vector, ComplexVector}`); it does not produce distinct operators
at L1 — the conjugation is absorbed by the [`dot`](./dot.md) dependency, exactly as for
`nrm2`. All parametric tests cover both element types
(`test-orthog.cpp:123, 234` real/complex).

## Status

`firm` — the L0 implementation is read in full (header-only inline, `orthog.hpp:18-90`), the
dispatch wrapper is read in full (`iterative.cpp:308-325`), all three variants carry dedicated
parametric test coverage across real / complex / B-weighted element types plus the empty-basis
edge case and a direct substitutability assertion (`⟨w', V[i]⟩ ≈ 0`,
`test-orthog.cpp:99-160, 234-389`), and the algebraic laws are standard Gram-Schmidt facts
modulo the explicitly-recorded floating-point caveats. This matches the firmness bar of the
BLAS-1 floor operators (`dot`, `nrm2`, `axpy`, `scal`).

## L1 vs L0 distinction

- **L0**: header-only inline mutating functions. `OrthogonalizeColumnMGS(comm, V, w, H, m,
  dot_op)` overwrites `w` in place (`w.Add(-H[j], V[j])`) and writes coefficients through the
  raw pointer `H`; per-`j` it does `H[j] = dot_op(w, V[j]); Mpi::GlobalSum(1, &H[j], comm);
  w.Add(-H[j], V[j])`. `OrthogonalizeColumnCGS(..., refine)` does `m` local dots, one
  `Mpi::GlobalSum(m, H, comm)`, `m` `w.Add`s, then optionally re-enters the same body
  accumulating into `dH` (`H[j] += dH[j]`). The variant is a runtime `switch` in
  `OrthogonalizeIteration`. Inputs assumed normalised; output **not** normalised.
- **L1**: pure functional `(w', H) = orthogonalize(w, V, variant)`. No destination buffers in
  the signature; no `comm` (single-rank scope); no in-place overwrite of `w`; no raw-pointer
  `H` write. The variant is a parameter inspected once. The per-variant collective shape and
  the MGS sequential dependency are recorded as properties (laws / variant-axis notes), not as
  separate operators. Normalisation stays the caller's `nrm2`+`scal` step, outside this
  operator's contract.

## Evidence

- `palace/linalg/orthog.hpp:18-23` — header scope contract: orthogonalises against a set of
  basis vectors using modified or classical Gram-Schmidt; "Assumes that the input vectors are
  normalized, but does not normalize the output vectors!" — the load-bearing
  no-output-normalisation contract.
- `palace/linalg/orthog.hpp:25-37` — `IdentityInnerProduct` and the `InnerProductHelper`
  concept: the `dot_op` template hook (canonical inner product `LocalDot`, plus the MPI
  reduction added by the routine) — the inner-product variant axis. (Range ends at the
  struct's closing `};` at line 37.)
- `palace/linalg/orthog.hpp:41-53` — `OrthogonalizeColumnMGS`: the per-`j` loop
  `H[j] = dot_op(w, V[j]); Mpi::GlobalSum(1, &H[j], comm); w.Add(-H[j], V[j])`. The
  interleaving of dot and `w.Add` in the same `j`-loop body is the source witness of the MGS
  sequential dependency; `m` reductions of size 1. (Range covers the function-name line through
  the closing brace at line 53.)
- `palace/linalg/orthog.hpp:57-89` — `OrthogonalizeColumnCGS`: empty-basis early return
  (`m == 0`); `m` local dots into `H[0..m-1]`; single `Mpi::GlobalSum(m, H, comm)`; `m`
  `w.Add`s against the original `w`; the `refine` branch re-enters with `dH`, accumulating
  `H[j] += dH[j]` (the CGS2 second pass). One (CGS) or two (CGS2) reductions of size `m`.
- `palace/linalg/iterative.cpp:308-325` — `OrthogonalizeIteration`: the runtime variant
  dispatch (`switch (type)` over `MGS / CGS / CGS2`, with `CGS2 = OrthogonalizeColumnCGS(...,
  true)`); confirms the variant is bound at solver construction and dispatched once, not
  re-inspected per column.
- `palace/linalg/iterative.cpp:630, 809` — GMRES and FGMRES Arnoldi inner-loop call sites
  `OrthogonalizeIteration(gs_orthog, comm, V, w, Hj, j)`, immediately followed by the caller's
  `nrm2` (sub-diagonal) and `scal` (normalisation) — confirming normalisation is the caller's,
  not this operator's.
- `palace/models/romoperator.cpp:51-66, 224, 633` — ROM basis-extension reuse of the same
  family with the `dot_op` hook (the second consumer; confirms the operator is not
  GMRES-specific).
- `test/unit/test-orthog.cpp:71-96` — `orthogonalize_wrapper` GENERATE harness running all
  three variants through one code path (the substitutability test fixture; the wrapper class
  spans the comment at 71 through the closing `};` at 96).
- `test/unit/test-orthog.cpp:99-120` — empty-basis edge case: all three variants leave `w`
  unchanged (`m = 0` identity, law 3).
- `test/unit/test-orthog.cpp:123-160` — parametric real test: all three variants zero the
  per-rank component and pass `⟨w', V[i]⟩ ≈ 0` to `1e-12` (law 1, the substitutability
  witness). The orthogonality assertion `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` is at line
  158, inside the check loop at 154-159; the full TEST_CASE closes at 160.
- `test/unit/test-orthog.cpp:164, 234, 276, 333` — real-2, complex, B-weighted-real,
  B-weighted-complex parametrisations: cover the element-type axis and the B-weighted
  inner-product variant axis.
- `book/src/concepts/orthogonalization.md` — cross-cutting prose (variants, L1 contract);
  consistent with this entry except on the coefficient/normalisation boundary, where this
  entry is authoritative (the concept page folds `h_{j+1} = ‖w'‖` into the column; that is the
  caller's `nrm2` step here).
- `book/src/concepts/sequential-obstruction.md:37-48` — the MGS-as-sequential-obstruction
  structural argument (an L3 property of the MGS variant; recorded here as the
  column-order-non-commutativity non-law and the variant-axis note).
- Cycle-002 firm [`dot`](./dot.md), cycle-002 firm [`axpy`](./axpy.md) — the two L1
  dependencies.

## Supporting evidence

- **Provenance.** This firm L1 entry was the lift target of the Phase-1 `orthog` slice
  (cycle-011 partial reduction → fully reduced and deleted cycle-098, graded-stack P2
  slice-deletion campaign; git history is the record). With this entry, the L2/L3/L4 dissections it
  retained (per-pass primitive sequences + transparent-vs-load-bearing classification; CGS/CGS2
  projector form + MGS sequential-obstruction; Solve-monad state stratification) are firm at
  `L2/orthogonalize.md`, `L3/orthogonalize.md`, and `concepts/orthogonalization.md`; its L0
  ground truth is cited directly there (`palace/linalg/orthog.hpp:18-90`).
- The (now-deleted) `arnoldi_step` slice named "a firm `L1/orthogonalize` (or
  `L1/orthogonalize-column`)" as a pending-lift prerequisite; this entry satisfies it. The
  `arnoldi_step` L1 procedure's `project(w, V[0..j]; gs_orthog)` step is now `orthogonalize(w,
  V[0..j], gs_orthog)`.
- OQ `l1-orthogonalize-promotion-from-arnoldi-step-and-orthog` (cycle-010, HIGH) is answered by
  this dispatch.

## Open questions / caveats

- **Naming: `orthogonalize` vs `orthogonalize-column`.** `arnoldi_step.md:5` floats both names.
  I chose `orthogonalize` (matches `concepts/orthogonalization.md`'s canonical signature and the
  dispatch wrapper's verb `OrthogonalizeIteration`). The L0 functions are
  `OrthogonalizeColumn{MGS,CGS}` (column-specific), but at L1 the "column" qualifier is an L0
  storage detail (the coefficients land in a Hessenberg *column*); the operator orthogonalises a
  *vector* against a *basis*, so the unqualified verb is the right L1 name. Flagging in case a
  future cross-cutter prefers the L0-faithful name.
- **L1>L0 lowering theme not yet authored.** This entry firms the L1 operator; the
  `orthogonalize-mutation-rotation` L1>L0 theme (in-place `w` overwrite + raw-pointer `H` write
  + per-variant collective shape, narrated forward from L1 to L0) is abstractor territory and is
  not part of this dispatch. The slice's retained L2 section is the raw material. Recommend the
  cycle-012+ planner queue it.
- **Coefficient sign / Hessenberg convention.** This entry returns `H[j] = ⟨w, V[j]⟩` (positive
  projection coefficient); the residual is `w − Σ H[j] V[j]`. Palace stores exactly these `H[j]`
  into the Hessenberg column (no sign flip), so the Arnoldi relation `T·V[j] = Σ H[i,j] V[i]`
  consumes them directly. No caveat — recording the convention explicitly so a downstream L2
  `krylov-step` lift does not re-derive a sign.
- **`concepts/orthogonalization.md` coefficient/normalisation drift.** The concept page describes
  the output as `(w', h)` with `h_{j+1} = ‖w'‖` folded in — that conflates this operator's `H`
  (length `m`) with the caller's `nrm2` sub-diagonal. Not in scope to edit here (one-operator
  discipline + concept pages are layer-intro-author territory); flagging for a future
  concept-page refresh. No layer-intro refresh is otherwise needed.
