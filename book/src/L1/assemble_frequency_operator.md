---
layer: L1
operator: assemble_frequency_operator
firmness: firm
edges:
  depends-on:
    - target: L2/linear_combination
      kind: folds
    - L1/apply_linop
    - target: L1-L0/assemble-frequency-operator-rotation
      kind: lowers-to
variant_axes:
  - operand-category (tensor-operand | operator-operand) — THIS operator is the operator-operand specialization of linear_combination; the axis itself is carried on the L2/L3 linear_combination entries (replace-and-propagate)
  - weight-schedule (constant | affine-in-parameter) — the driven case is affine-in-ω over a fixed scalar basis {1, iω, −ω²}
  - operand-stationarity (fixed-basis | parameter-dependent-operand) — {K, C, M} are fixed; A2 is the lone parameter-dependent operand carrying coeff 1 (the "affine modulo A2" caveat)
---

# assemble_frequency_operator

The driven (frequency-domain) pipeline's **per-ω system-operator assembly**: given a fixed operator basis and a frequency ω, produce the affine combination `A(ω) = K + iω·C − ω²·M + A2(ω)`. It is the **operator-operand specialization** of the firm scalar-weighted-sum fold [`linear_combination`](../L2/linear_combination.md) — a scalar-weighted sum of fixed operators, the operator-domain image of the tensor-domain BLAS-1 linear-combination cohort. It is **not** a new fold: it speaks *through* `linear_combination`'s newly-extended **operand-category** variant axis (`tensor-operand | operator-operand`; replace-and-propagate, 2026-06-01 anti-mirror discipline) — the driven case being the `operator-operand` + `affine-in-ω scalar weights` corner of that axis.

## Context

L1 is the mutation-rotation layer: Palace's in-place / output-arg / receiver-mutating source idioms are re-expressed as pure functions (`book/src/L1/index.md`). `assemble_frequency_operator` is the pure-functional rendering of Palace's per-frequency system-matrix build in the driven solver's frequency sweep. At L0, Palace re-assembles `A` fresh at every ω inside the sweep loop (`drivensolver.cpp:176-177`), capturing it into the Krylov solver via `ksp.SetOperators(*A, *P)` (`drivensolver.cpp:180`) before the per-ω solve. The pure L1 form takes the fixed basis + the frequency and returns the combined operator value; the imperative `SumOperator` construction and the per-ω capture are L1>L0 lowering concerns (see [`assemble-frequency-operator-rotation`](../L1-L0/assemble-frequency-operator-rotation.md)).

This operator is the **named content of the `map_solve` scope boundary**. `book/src/L4/solve_family.md` records the driven per-ω `SetOperators`-inside-the-loop as the boundary that scopes driven *out* of the shared `solve_family` (the `map_solve_over_(operator,rhs)_family` superset). This entry sharpens that boundary: the per-element operator the driven `map_solve` superset folds over is **not arbitrary** — it is an affine-in-ω fixed-basis operator-valued `linear_combination`, which is cleanly describable in existing spine vocabulary. The per-ω operator rebuild that scopes driven out of `solve_family` IS this affine-operator-family evaluation.

### Relationship to linear_combination (the replace-and-propagate framing)

`assemble_frequency_operator` does NOT introduce a second scalar-weighted-sum fold. The firm `linear_combination` (`L2/linear_combination.md`, `L3/linear_combination.md`) is `Σᵢ aᵢ·tᵢ` over a list of `(Scalar, Operand)` pairs; its operands were originally tensors (the BLAS-1 `scal`/`axpy`/`axpby`/`axpbypcz` cohort). The driven assembly is the *same fold* with the operand category lifted from **tensor** to **operator** (`ParOperator`: `K`/`C`/`M`/`A2`), under the operator monoid (operator addition + scalar-operator scaling, realized at L0 by `SumOperator::AddOperator`). Per the 2026-06-01 vocabulary-shift redirect, this is handled by **extending the existing combinator's operand-category variant axis** (`tensor-operand | operator-operand`) — the operator-operand case is witnessed by `BuildParSumOperator` (`rap.cpp:781-787`) — NOT by authoring a mirrored `operator_linear_combination` chapter. `assemble_frequency_operator` is then the **driven-pipeline specialization** of the operator-operand case: a fixed three-operator basis `{K, C, M}` combined under the affine-in-ω scalar weights `{1, iω, −ω²}`, plus the extra term `A2`.

## Signature

    assemble_frequency_operator
      :: FrequencyOperatorFamily[N] -> Scalar -> LinearOperator[N, N]

    -- where the fixed-basis family is the once-assembled operator basis:
    type FrequencyOperatorFamily[N] =
      { K  : LinearOperator[N, N]          -- stiffness (curl-curl), assembled once
      , C  : LinearOperator[N, N]          -- damping (impedance/conductivity), assembled once
      , M  : LinearOperator[N, N]          -- mass (permittivity), assembled once
      , A2 : Scalar -> LinearOperator[N, N] -- frequency-dependent extra term (closure over ω)
      }

    assemble_frequency_operator fam omega =
      linear_combination          -- operator-operand specialization (see §"Through linear_combination")
        [ (1,            fam.K)
        , (1i * omega,   fam.C)
        , (-(omega^2),   fam.M)
        , (1,            fam.A2 omega)
        ]

Shape contract (bunsen-style; named axes):

- `fam.K`, `fam.C`, `fam.M` — `LinearOperator[N, N]` — **shape precondition**: all share one square axis `N` (the global FE-space dimension); assembled ONCE before the frequency sweep (`drivensolver.cpp:91-93`). Operand-stationarity = `fixed-basis`.
- `fam.A2` — `Scalar -> LinearOperator[N, N]` — the frequency-dependent extra term, applied at the swept `omega` (`drivensolver.cpp:175`). Operand-stationarity = `parameter-dependent-operand` (the lone non-fixed operand; the "affine modulo A2" caveat).
- `omega` — `Scalar` — the (real) sweep frequency; the affine-weight parameter. The scalar weights `{1, iω, −ω²}` are the affine-in-ω schedule (weight-schedule = `affine-in-parameter`).
- result — `LinearOperator[N, N]` — the combined operator `A(ω)`, square on the same axis `N`; itself [`apply_linop`](./apply_linop.md)-applicable (it is captured into the Krylov solver at `drivensolver.cpp:180`).

The L0 surface materializes the result eagerly as an `mfem::SumOperator`-backed `ParOperator` (`rap.cpp:779-787`); the L1 form is a pure value (operator-as-value), the eager materialization is an L1>L0 concern.

## Through linear_combination (the operand-operand specialization)

The body is exactly `linear_combination` at the **operator-operand** corner of its operand-category variant axis:

    assemble_frequency_operator fam omega
      = linear_combination [ (1, fam.K), (1i*omega, fam.C), (-(omega^2), fam.M), (1, fam.A2 omega) ]

This is the arity-4 instance of the fold (`linear_combination` at term-list length 4), with the operand monoid being operator-addition / scalar-operator-scaling rather than tensor-addition. The four-term list is the literal `BuildParSumOperator({a0,a1,a2,1},{K,C,M,A2})` argument shape (`spaceoperator.cpp:527`). All of `linear_combination`'s algebraic laws hold here by the operand-category extension (operator addition is a commutative monoid with identity the zero operator; scalar-operator scaling distributes) — see §"Algebraic laws". Palace's L0 surface even exposes the fold's **zero-coefficient term-drop** law directly: `BuildParSumOperator` skips terms with `coeff[i] != 0 == false` (`rap.cpp:782`), the exact operator-domain analog of the tensor `γ==0` arity-collapse (`linear_combination` law 5).

Naming note: `assemble_frequency_operator` is the **driven specialization label** (one ω → one summed operator), the operator-domain sibling of `axpbypcz` as an arity-3 *tensor* readout label. It is a useful named entry because the driven pipeline's per-ω rebuild is the `map_solve` scope boundary and deserves a navigable L1 home; it is NOT a separate fold algebra.

## Semantics

`assemble_frequency_operator` combines a fixed operator basis under frequency-dependent scalar weights to produce the driven pipeline's per-frequency system operator `A(ω) = K + iω·C − ω²·M + A2(ω)`. The three fixed operators `{K, C, M}` are the FE-assembled stiffness / damping / mass operators (assembled once, `drivensolver.cpp:91-93`); the frequency only enters through the **scalar weights** `{1, iω, −ω²}` and through the extra term `A2(ω)`. The result is the operator the per-ω linear solve inverts.

The operator is **pure / out-of-place at L1**: it consumes the fixed basis and ω and produces a fresh operator value; the L0 in-place / eager-`SumOperator`-allocation idiom (and the per-ω `ksp.SetOperators(*A, *P)` capture) is the L1>L0 mutation rotation, captured by [`assemble-frequency-operator-rotation`](../L1-L0/assemble-frequency-operator-rotation.md).

It is **affine-in-ω modulo `A2`** (caveat, carried from the c061 D3 finding): for the three fixed-basis terms the per-ω rebuild is a genuine affine operator family — fixed basis, ω-varying scalar weights. The fourth term `A2` is the exception: `A2 = GetExtraSystemMatrix(omega)` (`drivensolver.cpp:175`) is itself ω-dependent — an ω-dependent **operand** carrying the constant coefficient `1`, NOT an ω-dependent coefficient. So the literal `BuildParSumOperator` shape is a four-operand affine combination whose fourth operand happens to vary with ω. The "affine-in-ω fixed-basis operator family" abstraction is exact for `{K, C, M}` and holds for `A2` only if one folds `A2`'s ω-dependence into the operand (the literal source shape). This is stated honestly rather than hidden: `assemble_frequency_operator` is affine-in-ω **modulo the `A2` ω-dependence**.

### Why this is a single-pipeline specialization (by design)

The operator-operand `linear_combination` is shared spine vocabulary (the fold is firm at the tensor-operand layer; this is the operand-category extension). The `assemble_frequency_operator` **specialization** — an affine-in-parameter fixed-basis operator *family* re-evaluated per parameter inside a solve loop — is witnessed by the driven pipeline ONLY, and that is permanent by design (a finding, not a gap):

- The **transient** pipeline bakes its time-excitation into the captured `TimeOperator` at construction (`transientsolver.cpp:33`); it does NOT rebuild an operator family per step (`fold_solve` op-capture-once stratum).
- **Electrostatic / magnetostatic** capture a single fixed `K` (one operator, no family).
- **Eigenmode** is opaque-library-owned (`eigen->Solve`); no Palace-assembled operator family.

So **no second-pipeline discharge probe is owed**. `assemble_frequency_operator` lands as a single-pipeline specialization, which is fine under the redirect (solvers are pulled up as a low-priority test-load; a clean single-pipeline specialization through existing vocabulary is a legitimate landing). The *fold* generality comes from the tensor-operand BLAS-1 cohort, not from a second assembly witness.

## Algebraic laws

The laws are `linear_combination`'s laws read at the operator-operand corner (operator addition `+` is a commutative monoid with identity the zero operator `0[N,N]`; scalar-operator scaling distributes over operator addition and over scalar addition). They hold; absences are deliberate.

1. **Reduces to the operator-operand `linear_combination` (the defining identity).** `assemble_frequency_operator fam omega = linear_combination [(1, K), (iω, C), (−ω², M), (1, A2(ω))]` — the arity-4 operator-operand instance of the firm fold. Every law below is that fold's law specialized to this fixed term list.

2. **Affine-in-ω over the fixed basis (the family law).** Holding `{K, C, M}` fixed and treating `A2` as a separate additive term, `A(ω) − A2(ω) = K + iω·C − ω²·M` is an affine (degree-≤2 polynomial-in-ω with operator coefficients) function of ω: the ω-derivative `d/dω (A − A2) = i·C − 2ω·M` is itself a fixed-basis operator combination. This is the law that makes the per-ω rebuild a *family* rather than independent assemblies. **Modulo `A2`**: with `A2`'s ω-dependence included, the affine/polynomial-in-ω structure holds only for the `{K, C, M}` part (the `A2` caveat).

3. **Operator-linearity in the weights (multilinearity, operator-operand).** `A` is linear separately in each scalar weight with the operands held fixed: scaling the C-weight by κ scales `C`'s contribution by κ. This is `linear_combination`'s multilinearity (law 3) at the operator-operand corner.

4. **Zero-coefficient term-drop.** A term whose scalar weight is zero drops from the sum: at `ω = 0` the C-weight `iω = 0` and the M-weight `−ω² = 0`, so `A(0) = K + A2(0)`. This is the **exact algebraic content of the L0 `coeff[i] != 0` sparsity prune** (`rap.cpp:782`) — the operator-domain analog of `linear_combination` law 5 (the tensor `γ==0` arity-collapse). Positively anchored in the operator domain (not inherited): `BuildParSumOperator` literally skips zero-coefficient operands.

5. **Empty-combination identity (the fold seed).** The operator-operand `linear_combination` over the empty list is the zero operator `0[N,N]`; `BuildParSumOperator` guards against this with `MFEM_VERIFY(it != ops.end())` (`rap.cpp:769-771`) — at least one non-null operand is required (a precondition on the L1 signature, the empty case is the fold's seed, not a runtime path Palace exercises). The driven call always supplies the non-null `K`.

6. **Result is `apply_linop`-applicable.** `A(ω)` is itself a `LinearOperator[N, N]`, applied by the inner Krylov solve (captured at `drivensolver.cpp:180`); its action `A(ω)·v = K·v + iω·(C·v) − ω²·(M·v) + A2(ω)·v` distributes over the basis (the `SumOperator::AddMult` action). This is the apply/assemble duality: the assembled sum's action is the weighted sum of the basis actions ([`apply_linop`](./apply_linop.md)).

Laws that explicitly **do not** hold:

- **Affine-in-ω as a whole (paired non-law).** `A(ω)` is NOT globally affine-in-ω because (a) the M-weight `−ω²` makes it quadratic-in-ω over the fixed basis (law 2 records "affine modulo the quadratic M-term" precisely — it is degree-≤2 polynomial-in-ω, not strictly affine) and (b) `A2(ω)` is an unknown-degree ω-dependent operand. The honest characterization is "fixed-basis polynomial-in-ω (degree ≤ 2) plus the `A2` correction" — the "affine operator family" phrasing in the literature/finding refers to the fixed-basis-with-scalar-weights structure, not literal degree-1.
- **Operand-permutation bit-identity (IEEE residue).** The operator-domain sum order (`AddOperator` accumulation order, `rap.cpp:781-783`) is a load-bearing reduction-order concern exactly as for the tensor fold; bit-reproduction of a given L0 assembly requires matching `BuildParSumOperator`'s accumulation order. This is the L1>L0 lowering's substantive content (see [`assemble-frequency-operator-rotation`](../L1-L0/assemble-frequency-operator-rotation.md)), NOT restated as an L1 law — the same disposition `linear_combination` uses for its IEEE non-law.

## Dependencies

**Through (the fold this specializes):** the firm [`linear_combination`](../L2/linear_combination.md) (L2; L3 [`linear_combination`](../L3/linear_combination.md)) — at the **operator-operand** corner of its operand-category variant axis (extended this cycle, replace-and-propagate). `assemble_frequency_operator` is the arity-4 driven specialization; it does not re-derive the fold.

**Same-layer (L1):** [`apply_linop`](./apply_linop.md) — the fixed-basis operands `{K, C, M, A2}` are opaque `LinearOperator[N, N]` values (apply_linop-shaped), and the assembled result `A(ω)` is itself apply_linop-applicable (its action is the weighted sum of the basis actions, law 6). The FE assembly of `{K, C, M}` themselves is the [`fe_assemble`](./fe_assemble.md) sub-spine (consumed-by, not a dependency — the basis is an input to this operator).

**Cross-cutting:** the result is captured into the per-ω inner solve; the per-ω `(operator, rhs)` family it parameterizes is the `map_solve_over_(operator,rhs)_family` superset scope boundary recorded at `book/src/L4/solve_family.md` (driven scope-out). This operator NAMES the per-element operator of that superset.

## Variant axes

1. **Operand-category** (`tensor-operand | operator-operand`) — the axis this operator's existence motivates extending onto `linear_combination`. `assemble_frequency_operator` is the `operator-operand` corner; the BLAS-1 cohort is the `tensor-operand` corner. The axis itself is carried on the L2/L3 `linear_combination` entries (replace-and-propagate); this entry is its driven specialization.
2. **Weight-schedule** (`constant | affine-in-parameter`) — the driven case is `affine-in-parameter` (the `{1, iω, −ω²}` schedule over the swept ω). A single fixed-coefficient operator sum (e.g. a one-shot `K + M`) would be `constant`.
3. **Operand-stationarity** (`fixed-basis | parameter-dependent-operand`) — `{K, C, M}` are `fixed-basis`; `A2` is the lone `parameter-dependent-operand` (the "affine modulo A2" caveat). This axis distinguishes the genuinely-fixed basis from the ω-dependent extra term.

Element-type here is fixed `complex` (the driven assembly is `<ComplexOperator>`-typed, `drivensolver.cpp:175`; the weights `iω`, `−ω²` are complex). The real/complex element-type variant general to `linear_combination` collapses to complex-only for this driven specialization (a scope-out, not a remaining axis).

## Downward to L0

The pure affine-operator-family value lowers to Palace's imperative per-ω `SumOperator` assembly via the L1>L0 theme [`assemble-frequency-operator-rotation`](../L1-L0/assemble-frequency-operator-rotation.md): `GetSystemMatrix` (`spaceoperator.cpp:521-528`) forwards to `BuildParSumOperator` (`rap.cpp:764-787`), which allocates a `SumOperator` and accumulates `sum->AddOperator(ops[i]->LocalOperator(), coeff[i])` for each non-zero-coefficient operand, then the per-ω `ksp.SetOperators(*A, *P)` capture (`drivensolver.cpp:180`). The rotation narrates forward (L1 → L0) per the high→low discipline.

## Status

`firm` — **firm-on-positive-structure** (the `apply_linop` / `lu_solve` / `fe_assemble` no-dedicated-test precedent). The structure is read off positive source in full: the per-ω combination (`drivensolver.cpp:176-177`), the once-assembled fixed basis (`:91-93`), the ω-dependent `A2` operand (`:175`), the per-ω capture (`:180`), the `GetSystemMatrix` forward (`spaceoperator.cpp:521-528`), and the `BuildParSumOperator` scalar-weighted operator fold including the `coeff[i] != 0` sparsity prune (`rap.cpp:764-787`). Every algebraic law is a syntactic operator-algebra identity on this positive source (the operator-operand specialization of `linear_combination`'s laws, with the term-drop law positively anchored in the operator domain at `rap.cpp:782`), so the absence of a dedicated driven-assembly unit test does not gate firm. Two recorded caveats are non-gating because they are **stated facts**, not unconfirmed laws: (a) **affine modulo `A2`** — the fixed-basis affine/degree-≤2 structure is exact for `{K, C, M}`; `A2` is an ω-dependent operand carrying coeff 1, recorded as the `parameter-dependent-operand` stationarity case + the affine-as-a-whole non-law; (b) **single-pipeline-by-design** — the affine-operator-family specialization is witnessed by driven only and permanently so (transient/electrostatic/magnetostatic/eigenmode do not assemble an operator family), so it lands as a single-pipeline specialization with no second-pipeline discharge owed. The operand-category generality of the underlying fold comes from the firm tensor-operand BLAS-1 cohort plus this operator-operand witness, not from a second assembly site.

## Evidence

L0 source ranges (paths relative to `reference/palace/`; verified via `palace-codemap` `read_range` against the on-disk file this dispatch):

- `palace/drivers/drivensolver.cpp:91-93` — the fixed operator basis assembled ONCE before the frequency sweep: `K = GetStiffnessMatrix`, `C = GetDampingMatrix`, `M = GetMassMatrix` (operand-stationarity = fixed-basis).
- `palace/drivers/drivensolver.cpp:175` — `A2 = space_op.GetExtraSystemMatrix<ComplexOperator>(omega, Operator::DIAG_ZERO)` (the ω-dependent extra-term operand; the "affine modulo A2" caveat).
- `palace/drivers/drivensolver.cpp:176-177` — `A = space_op.GetSystemMatrix(1.0+0.0i, 1i*omega, -omega*omega+0.0i, K, C, M, A2)` (the per-ω affine combination, INSIDE the sweep loop; weights `{1, iω, −ω²}`).
- `palace/drivers/drivensolver.cpp:180` — `ksp.SetOperators(*A, *P)` (the per-ω operator capture = the `map_solve` superset scope boundary).
- `palace/models/spaceoperator.cpp:521-528` — `SpaceOperator::GetSystemMatrix(a0, a1, a2, K, C, M, A2)` ≡ `BuildParSumOperator({a0, a1, a2, ScalarType{1}}, {K, C, M, A2})` (the one-line forward; the literal 4-term scalar-weighted operand list).
- `palace/linalg/rap.cpp:764-767` — `BuildParSumOperator<N>(const std::array<double,N>& coeff, const std::array<const ParOperator*,N>& ops, ...)` — the template signature (the operator-operand scalar-weighted-sum primitive). **Coeff-type note (repairer cycle-062 D3):** this `:764-767` signature is the **real-`double`-coeff** overload; the driven `<ComplexOperator>` path actually resolves to the **complex-coeff overload** `BuildParSumOperator(const std::array<std::complex<double>, N>& coeff, …)` at `palace/linalg/rap.cpp:833` (declared `palace/linalg/rap.hpp:238`; explicit `std::complex<double>` instantiations at `palace/linalg/rap.cpp:971-977`) — the complex `a1 = iω` weight requires it. The two overloads share the identical fold shape (`SumOperator` seed + `AddOperator` accumulate + `coeff[i] != 0` prune), so every structural/algebraic claim holds verbatim; the complex overload is the precise instantiation the driven path uses.
- `palace/linalg/rap.cpp:779-787` — the fold body: `auto sum = make_unique<SumOperator>(...)` then `for (i) if (ops[i] && coeff[i] != 0) sum->AddOperator(ops[i]->LocalOperator(), coeff[i])` — the scalar-weighted operator accumulate (`:783`) with the zero-coefficient sparsity prune (`:782`, the operator-domain `γ==0` term-drop, law 4).

Firm endpoint this entry specializes:

- `book/src/L2/linear_combination.md` (firm; cycle-018, inverted-to-entry cycle-049 D1) — the scalar-weighted-sum fold this operator is the **operator-operand** specialization of (operand-category axis extended this cycle); signature (`:55-57`), the variant-axes prose (`:240-267`), the zero-coefficient term-drop law (the tensor `γ==0` analog of `rap.cpp:782`).
- `book/src/L3/linear_combination.md` (firm; cycle-050 D1) — the L3 rendering of the same fold (operand-category axis extended this cycle in lockstep).

Provenance: cross-layer-cross-cutter:2026-06-02T075145Z `reports/2026-06-02T075145Z-cross-layer-cross-cutter-driven-transient-outer-machinery-probe/CYCLE.md` (Region 1, the LICENSE-FUTURE candidate + the replace-and-propagate disposition + the "affine modulo A2" + single-pipeline caveats); this dispatch (harvester:2026-06-02T083220Z, cycle-062 D3) enacts the licensed landing.
