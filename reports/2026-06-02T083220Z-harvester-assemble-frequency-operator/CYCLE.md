---
agent: harvester
invoked_at: 2026-06-02T083220Z
scope: L1 operator: assemble_frequency_operator + L1>L0 rotation assemble-frequency-operator-rotation; replace-and-propagate operand-category axis extension on L2/L3 linear_combination
status: pending
integrated_at: 2026-06-02T103000Z
integration_commit: 4d621d1
integration_notes: "Applied clean by integrator-per-report (D3) at 2026-06-02T100200Z; finalized cycle-062. NEW firm L1/assemble_frequency_operator.md + NEW firm L1-L0/assemble-frequency-operator-rotation.md + linear_combination operand-category variant axis (tensor-operand | operator-operand) extended at L2+L3 (surgical, fold NOT re-derived) + L1/index dep-map row + cohort bullet + L1-L0/index row + SUMMARY x2. ENACTS the c061 D3 LICENSE-FUTURE candidate as the operator-operand specialization THROUGH linear_combination, NOT a mirrored fold (anti-mirror / replace-and-propagate, critic=pass). L1 firm 30->31; L1>L0 firm themes +1. Two anchor corrections at apply time (the L1-L0/index floquet-row old_string did not match disk, re-anchored as append-after; the L1/index anchors matched exactly). citecheck --scan 33 ok / 0 failing. Build clean (cargo make book exit 0; both new pages render)."
inputs:
  - reports/2026-06-02T075145Z-cross-layer-cross-cutter-driven-transient-outer-machinery-probe/CYCLE.md (c061 D3 finding — Region 1, the LICENSE-FUTURE candidate)
  - book/src/L2/linear_combination.md (firm L2 fold combinator — the operand-category extension target)
  - book/src/L3/linear_combination.md (firm L3 fold combinator — the operand-category extension target)
  - palace/drivers/drivensolver.cpp:91-93,175,176-177,180 (the per-ω affine combination + once-assembled fixed basis + per-ω capture)
  - palace/models/spaceoperator.cpp:521-528 (GetSystemMatrix ≡ BuildParSumOperator forward)
  - palace/linalg/rap.cpp:764-767,781-787 (BuildParSumOperator scalar-weighted operator fold)
---

# CYCLE: Formalize assemble_frequency_operator at L1

## Summary

The driven (frequency-domain) pipeline's per-ω system-matrix assembly `A = a0·K + a1·C + a2·M + 1·A2` (`drivensolver.cpp:176-177`, coefficients `{1, iω, −ω²}`) is the **operator-domain image of the firm tensor-domain `linear_combination` fold**: a scalar-weighted variadic sum of fixed operators, bottoming out in `SpaceOperator::GetSystemMatrix` → `BuildParSumOperator({a0,a1,a2,1},{K,C,M,A2})` (`spaceoperator.cpp:521-528` → `rap.cpp:764-787`, `sum->AddOperator(ops[i], coeff[i])`). The `{K,C,M}` are assembled ONCE before the ω-loop (`drivensolver.cpp:91-93`); only the scalar weights ω-vary → an **affine-in-ω fixed-basis operator family**, re-evaluated per ω inside the solve loop. This dispatch lands `assemble_frequency_operator` as an L1 operator that re-expresses **through** `linear_combination` with a new **operand-category variant axis** (`tensor-operand | operator-operand`) — the driven case is the `operator-operand` + `affine-in-ω scalar weights` specialization. This is the **replace-and-propagate** enactment (2026-06-01 anti-mirror discipline): I do NOT mint a new mirrored fold; I extend the firm `linear_combination`'s operand-category axis on `L2/linear_combination.md` and `L3/linear_combination.md` (the operator-operand case witnessed by `BuildParSumOperator`), and author the driven op as its single-pipeline specialization plus a forward L1>L0 rotation. Status: **firm** (firm-on-positive-structure — the structure is read off positive source; the laws are operator-algebra identities), carrying the c061 D3 caveats: (a) "affine modulo A2" (the 4th term `A2 = GetExtraSystemMatrix(omega)` is an ω-DEPENDENT OPERAND carrying literal coeff 1, not an ω-dependent coefficient); (b) single-pipeline-by-design (no 2nd-pipeline discharge owed). Dual-registration: my own L1 dep-map row + cohort bullet + both SUMMARY chapter lines + the L1-L0 theme row; the **consolidated running-count tally is DEFERRED to D2** (the layer-intro-author count-owner this cycle).

## Proposed changes

```new:book/src/L1/assemble_frequency_operator.md
---
layer: L1
operator: assemble_frequency_operator
firmness: firm
depends_on:
  - book/src/L2/linear_combination.md (the firm scalar-weighted-sum fold this operator is the operator-operand specialization of — re-expressed THROUGH it via the operand-category variant axis; NOT a new mirrored fold)
  - book/src/L1/apply_linop.md (the opaque-operator gate — the fixed-basis operators {K, C, M, A2} are apply_linop-shaped opaque LinearOperator values; the assembled A is itself apply_linop-applicable)
lowers_to:
  - book/src/L1-L0/assemble-frequency-operator-rotation.md (the L1>L0 mutation rotation: the pure affine-operator-family value → the BuildParSumOperator / GetSystemMatrix imperative SumOperator assembly)
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
```

```new:book/src/L1-L0/assemble-frequency-operator-rotation.md
---
theme: assemble-frequency-operator-rotation
edge: L1>L0
lhs: book/src/L1/assemble_frequency_operator.md (firm)
status: firm
sources:
  - palace/drivers/drivensolver.cpp:91-93,175,176-177,180
  - palace/models/spaceoperator.cpp:521-528
  - palace/linalg/rap.cpp:764-787
---

# assemble-frequency-operator-rotation (L1 > L0)

How the pure L1 [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md) — the affine-in-ω fixed-basis operator-valued `linear_combination` `A(ω) = K + iω·C − ω²·M + A2(ω)` — lowers into Palace's imperative per-frequency `SumOperator` assembly. The narration is forward (L1 → L0) per the high→low discipline: the pure operator-family value on the left, the mutating C++ assembly + per-ω solver capture on the right.

## Rotation

The L1 form is a pure function `FrequencyOperatorFamily[N] -> Scalar -> LinearOperator[N, N]` returning the combined operator value. Palace realizes it as a three-hop imperative assembly re-run at every swept ω:

1. **Fixed-basis pre-assembly (once, outside the sweep).** `K`/`C`/`M` are assembled once before the frequency loop: `K = space_op.GetStiffnessMatrix<ComplexOperator>(...)`, `C = space_op.GetDampingMatrix<...>(...)`, `M = space_op.GetMassMatrix<...>(...)` (`drivensolver.cpp:91-93`). In the L1 form these are the `fam.{K,C,M}` fixed-basis fields (operand-stationarity = fixed-basis); the L0 hoist out of the loop is the transparent-performance realization of "the basis does not depend on ω".

2. **Per-ω extra term + combination (inside the sweep).** Inside the ω-loop: `A2 = space_op.GetExtraSystemMatrix<ComplexOperator>(omega, Operator::DIAG_ZERO)` (`drivensolver.cpp:175`) materializes the ω-dependent operand (the L1 `fam.A2 omega` closure application — the "affine modulo A2" operand). Then `A = space_op.GetSystemMatrix(1.0+0.0i, 1i*omega, -omega*omega+0.0i, K, C, M, A2)` (`drivensolver.cpp:176-177`) is the L1 `linear_combination [(1,K),(iω,C),(−ω²,M),(1,A2)]` call — the per-ω operator-operand fold with the affine-in-ω scalar weights `{1, iω, −ω²}`.

3. **The fold body — `GetSystemMatrix` → `BuildParSumOperator`.** `GetSystemMatrix` is a one-line forward: `return BuildParSumOperator({a0, a1, a2, ScalarType{1}}, {K, C, M, A2})` (`spaceoperator.cpp:521-528`) — the literal 4-term scalar-weighted operand list, with `A2`'s coefficient the constant `1` (the operand-not-coefficient placement of the extra term). `BuildParSumOperator<N>` (`rap.cpp:764-787`) is the operator-domain scalar-weighted-sum primitive: it allocates `auto sum = make_unique<SumOperator>(height, width)` (`rap.cpp:779-780`) seeded at the zero operator, then folds `for (i) if (ops[i] && coeff[i] != 0) sum->AddOperator(ops[i]->LocalOperator(), coeff[i])` (`rap.cpp:781-783`). The `coeff[i] != 0` guard (`rap.cpp:782`) is the operator-domain realization of the fold's zero-coefficient term-drop (`assemble_frequency_operator` law 4 / `linear_combination` law 5) — at `ω = 0` the `iω` and `−ω²` weights vanish and the `C`, `M` terms are skipped. The eager `SumOperator` materialization is the mutation the L1 pure value abstracts.

4. **Per-ω capture into the inner solve.** `ksp.SetOperators(*A, *P)` (`drivensolver.cpp:180`) installs the freshly-assembled `A` (and preconditioner `P`) into the Krylov solver before the per-ω solve. This is the `map_solve` superset scope boundary: the operator is rebuilt and re-captured per frequency, which is exactly why driven is scoped out of the shared `solve_family` (`book/src/L4/solve_family.md`). The L1 form has no `SetOperators` — the capture is the imperative residue of "feed the assembled operator to the per-element solve".

## Load-bearing residue

- **Accumulation order (load-bearing numerical).** `BuildParSumOperator`'s `AddOperator` accumulation order (`K`, then `C`, then `M`, then `A2`; `rap.cpp:781-783`) pins the operator-sum reduction order. The L1 algebra is order-agnostic for value (operator addition is commutative), but bit-reproduction of a given L0 assembly requires matching this order — the operator-domain analog of the tensor fold's IEEE summation-order non-law. Preserved as an explicit claim here (the lowering's substantive numerical content), not restated as an L1 law.
- **Sparsity prune (transparent performance trick).** The `coeff[i] != 0` skip (`rap.cpp:782`) avoids accumulating zero-weighted operands — algebraically the term-drop law (transparent for value), an L0 performance realization, not a semantic change.
- **Fixed-basis hoist (transparent performance trick).** Assembling `{K, C, M}` once outside the loop (`drivensolver.cpp:91-93`) rather than per-ω is the realization of operand-stationarity = fixed-basis — transparent for value, load-bearing for cost (the affine-family structure is exactly what licenses the hoist).

## Status

`firm` — the rotation is read in full from positive source: the per-ω combination call (`drivensolver.cpp:176-177`), the once-hoisted fixed basis (`:91-93`), the ω-dependent `A2` operand (`:175`), the per-ω capture (`:180`), the `GetSystemMatrix` forward (`spaceoperator.cpp:521-528`), and the `BuildParSumOperator` fold body with its sparsity prune (`rap.cpp:764-787`). The three load-bearing residues (accumulation order, sparsity prune, fixed-basis hoist) are positively anchored. No dedicated driven-assembly unit test exists; the rotation is firm-on-positive-structure (the `fe-operator-assemble-mutation-rotation` / `apply-linop-mutation-rotation` precedent), since every step is a syntactic transcription of fully-specified source.

## Evidence

Paths relative to `reference/palace/`; verified via `palace-codemap` `read_range` this dispatch:

- `palace/drivers/drivensolver.cpp:91-93` — fixed basis `K`/`C`/`M` assembled once before the sweep.
- `palace/drivers/drivensolver.cpp:175` — `A2 = GetExtraSystemMatrix<ComplexOperator>(omega, DIAG_ZERO)` (ω-dependent operand).
- `palace/drivers/drivensolver.cpp:176-177` — `A = GetSystemMatrix(1+0i, iω, −ω²+0i, K, C, M, A2)` (per-ω combination).
- `palace/drivers/drivensolver.cpp:180` — `ksp.SetOperators(*A, *P)` (per-ω capture).
- `palace/models/spaceoperator.cpp:521-528` — `GetSystemMatrix` ≡ `BuildParSumOperator({a0,a1,a2,1}, {K,C,M,A2})`.
- `palace/linalg/rap.cpp:764-767` — `BuildParSumOperator<N>` template signature.
- `palace/linalg/rap.cpp:779-787` — `SumOperator` allocation + the `AddOperator` accumulate fold (`:783`) + the `coeff[i] != 0` sparsity prune (`:782`).

Provenance: licensed by cross-layer-cross-cutter:2026-06-02T075145Z (c061 D3, Region 1); authored by harvester:2026-06-02T083220Z (cycle-062 D3) alongside the L1 [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md) entry.
```

```edit:book/src/L2/linear_combination.md
2. **Element-type** — `real | complex`, with the `real ⊑ complex` scalar-promotion
   sub-axis ([`concepts/scalar-promotion`](../concepts/scalar-promotion.md)). Inherited
   unchanged from the L1 leaves; promote all-or-none across the scalar list. Note: this
   sub-axis is unified at the concept-page level, but its closure depends on the L1
   calculus formally adopting the `real ⊑ complex` scalar lattice — an upstream dependency
   tracked under OQ `scalar-promotion-typing-rule` and not yet committed
   (`concepts/scalar-promotion.md:49`); the inheritance here carries that dependency
   unchanged.
3. **Operand-category** — `tensor-operand | operator-operand`. The fold's operand monoid
   is parametric: the original cohort is the **tensor-operand** corner (the BLAS-1
   `scal`/`axpy`/`axpby`/`axpbypcz` family, operand monoid = tensor-addition +
   scalar-tensor-scaling). The **operator-operand** corner is the same fold over
   `LinearOperator[N, N]` operands under operator-addition + scalar-operator-scaling —
   witnessed by Palace's `BuildParSumOperator` (`palace/linalg/rap.cpp:764-787`,
   `sum->AddOperator(ops[i]->LocalOperator(), coeff[i])` for `coeff[i] != 0`), the
   operator-domain scalar-weighted sum. The driven pipeline's per-ω system-operator
   assembly `A(ω) = K + iω·C − ω²·M + A2(ω)` is the L1 operator-operand specialization
   [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md) (cycle-062;
   arity-4 instance, affine-in-ω scalar weights). The zero-coefficient term-drop law
   (law 5) holds verbatim at this corner — `BuildParSumOperator`'s `coeff[i] != 0`
   guard IS the operator-domain `γ==0` arity-collapse. This is the replace-and-propagate
   extension (2026-06-01 anti-mirror discipline): the operand category is a variant of
   the one fold, NOT a mirrored `operator_linear_combination` chapter.
```

```edit:book/src/L3/linear_combination.md
variant_axes:
  - arity (the UNIFICATION axis — not a remaining variant; recovered as term-list length)
  - output-aliasing (in-place vs out-of-place; orthogonal to arity; an L3>L2>L1 lowering concern, pure/out-of-place at L3)
  - element-type (real | complex)
  - scalar-promotion (sub-axis on the complex element-type; real ⊑ complex, inherited from concepts/scalar-promotion)
  - operand-category (tensor-operand | operator-operand; the operator-operand corner witnessed by BuildParSumOperator, driven specialization assemble_frequency_operator c062 — replace-and-propagate, not a mirrored fold)
```

```edit:book/src/L3/linear_combination.md
2. **Element-type** — `real | complex`, with the `real ⊑ complex` scalar-promotion sub-axis ([`scalar-promotion`](../concepts/scalar-promotion.md)). Inherited unchanged from the L2 combinator; promote all-or-none across the scalar list. Carries the open `scalar-promotion-typing-rule` upstream dependency unchanged.
3. **Operand-category** — `tensor-operand | operator-operand`. The fold's operand monoid is parametric: the BLAS-1 cohort is the **tensor-operand** corner; the **operator-operand** corner is the same fold over `LinearOperator[N, N]` operands under operator-addition + scalar-operator-scaling, witnessed by Palace's `BuildParSumOperator` (`palace/linalg/rap.cpp:764-787`). The driven per-ω system-operator assembly `A(ω) = K + iω·C − ω²·M + A2(ω)` is the L1 operator-operand specialization [`assemble_frequency_operator`](../L1/assemble_frequency_operator.md) (cycle-062). The zero-coefficient term-drop law holds verbatim (the `coeff[i] != 0` guard is the operator-domain `γ==0` collapse). Replace-and-propagate extension (2026-06-01 anti-mirror discipline), NOT a mirrored fold.
```

```edit:book/src/L1/index.md
| [`floquet-correction`](./floquet-correction.md) | `(F: FloquetCorrector[N_nd, N_rt], x: Field[N_nd, Complex]) → Field[N_rt, Complex]` (i.e. `F.M_RT⁻¹ · F.Cross · x`) | `ksp_solve` (direct, inner RT mass solve), `apply_linop` (direct, the `Cross · x` cross-product step); `jacobi-smoother` (inner CG preconditioner, closure-bound); `axpy` (the AddMult-as-axpy composition) | `firm` (constructed-operator gate; sixth at L1; third firm instance of nested-constructed-operator-gate; element-type scope-out: `<ComplexVector>` only; L0: `palace/linalg/floquetcorrection.cpp:20-86,88` + 4 AddMult consumer sites `palace/drivers/drivensolver.cpp:212,336,468` + `palace/drivers/eigensolver.cpp:454`; harvested cycle-036; firm-on-positive-structure; AddMult-as-axpy buffer-economy fusion with inner-ksp aliasing applicability) |
| [`assemble_frequency_operator`](./assemble_frequency_operator.md) | `(fam: FrequencyOperatorFamily[N], ω: Scalar) → LinearOperator[N, N]` (i.e. `A(ω) = K + iω·C − ω²·M + A2(ω)`) | [`linear_combination`](../L2/linear_combination.md) (the fold this specializes — operator-operand corner of the operand-category axis, NOT a new fold); `apply_linop` (operands + result are opaque square operators) | `firm` (driven per-ω system-operator assembly; **operator-operand specialization of `linear_combination`** — replace-and-propagate, 2026-06-01 anti-mirror; L0: `palace/drivers/drivensolver.cpp:91-93,175,176-177,180` + `palace/models/spaceoperator.cpp:521-528` + `palace/linalg/rap.cpp:764-787`; L1>L0: [`assemble-frequency-operator-rotation`](../L1-L0/assemble-frequency-operator-rotation.md); harvested cycle-062; firm-on-positive-structure, no-dedicated-test caveat non-gating; **affine modulo A2** (A2 is an ω-dependent operand carrying coeff 1, not an ω-dependent coefficient); **single-pipeline-by-design** (driven only — transient bakes excitation into the captured op, electro/magnetostatic capture a single fixed K, eigenmode opaque — no 2nd-pipeline discharge owed); sharpens the `map_solve` scope boundary (`book/src/L4/solve_family.md`)) |
```

```edit:book/src/L1/index.md
- [`floquet-correction`](./floquet-correction.md) — pure-functional **Floquet B-field correction primitive** `y = floquet_correction(F, x)`; consumes a Nedelec input field `x` and produces the RT-space corrected field `y = F.M_RT⁻¹ · F.Cross · x` where `F.Cross = [kp ×]` is the cross-product with the Floquet wave vector and `F.M_RT` is the RT vector-FE mass operator. The **sixth constructed-operator gate at L1** (after `ksp_solve`, `eigsolve`, `chebyshev-smoother`, `divfree-projector`, `jacobi-smoother`), and the **third firm instance** of the [`nested-constructed-operator-gate`](../concepts/nested-constructed-operator-gate.md) shape (closure carries `F.ksp : Solver[F.M_RT]`). Structurally isomorphic to `divfree-projector` (same Mult+AddMult surface, same `Solver[F.M]` sub-field, same `VectorFEMassIntegrator`-based construction) but **strictly thinner**: no boundary-zeroing, no gradient correction, no empty-boundary nullspace pin — just `Cross · x` followed by `M_RT⁻¹ · rhs`. **Element-type scope-out**: only `<ComplexVector>` is instantiated (`palace/linalg/floquetcorrection.cpp:88`); the parametric `<VecType>` template is dead-code in any hypothetical real-only client (the first L1 gate with a deliberately-narrowed element-type scope). Inner CG uses a `JacobiSmoother` preconditioner (not BoomerAMG — RT mass is well-conditioned), making the gate transitively three-deep: `floquet → ksp → jacobi-smoother`. Firm-on-positive-structure (the `divfree-projector` / `jacobi-smoother` no-dedicated-test precedent): every law is a syntactic identity on positive source. Four AddMult consumer sites (`palace/drivers/drivensolver.cpp:212,336,468` + `palace/drivers/eigensolver.cpp:454`), three construction sites (`drivensolver.cpp:141,292`, `eigensolver.cpp:240`), all gated on `space_op.GetMaterialOp().HasWaveVector()`. **AddMult-as-axpy non-law**: `AddMult` is not a separate L1 operator — it unfolds into `axpy(a, floquet_correction(F, x), y)` (a load-bearing buffer-economy fusion that re-uses the scratch member as transient scaled-output buffer, with an inner-ksp aliasing applicability not present in any sister theme).
- [`assemble_frequency_operator`](./assemble_frequency_operator.md) — pure-functional **driven per-ω system-operator assembly** `A(ω) = assemble_frequency_operator(fam, ω) = K + iω·C − ω²·M + A2(ω)`; the **operator-operand specialization of [`linear_combination`](../L2/linear_combination.md)** (the operator-domain image of the firm tensor-domain scalar-weighted-sum fold), NOT a new fold — it speaks through `linear_combination`'s operand-category variant axis (`tensor-operand | operator-operand`), extended this cycle (replace-and-propagate, 2026-06-01 anti-mirror discipline). The fixed basis `{K, C, M}` is assembled ONCE before the frequency sweep (`drivensolver.cpp:91-93`); only the scalar weights `{1, iω, −ω²}` ω-vary → an **affine-in-ω fixed-basis operator family** re-evaluated per ω inside the solve loop (`drivensolver.cpp:176-177`), captured into the inner Krylov solve at `ksp.SetOperators(*A, *P)` (`:180`). Bottoms out in `GetSystemMatrix` → `BuildParSumOperator({a0,a1,a2,1},{K,C,M,A2})` (`spaceoperator.cpp:521-528` → `rap.cpp:764-787`, `sum->AddOperator(ops[i], coeff[i])` for `coeff[i] != 0` — the operator-domain `γ==0` term-drop). **Affine modulo A2**: the 4th term `A2 = GetExtraSystemMatrix(omega)` (`:175`) is an ω-dependent **operand** carrying the literal coefficient 1, not an ω-dependent coefficient — the affine/degree-≤2-in-ω structure is exact for `{K, C, M}` only; stated honestly. **Single-pipeline-by-design**: the affine-operator-family specialization is witnessed by the driven pipeline ONLY and permanently so (transient bakes its excitation into the captured `TimeOperator`; electro/magnetostatic capture a single fixed `K`; eigenmode is opaque-library `eigen->Solve`) — it lands as a single-pipeline specialization with NO 2nd-pipeline discharge owed (the *fold* generality comes from the tensor-operand BLAS-1 cohort). Sharpens the `map_solve` scope boundary (`book/src/L4/solve_family.md`): the per-ω operator rebuild that scopes driven out of `solve_family` IS this affine-operator-family evaluation. Firm-on-positive-structure (the `apply_linop` / `fe_assemble` no-dedicated-test precedent): every law is a syntactic operator-algebra identity on positive source, with the term-drop law positively anchored in the operator domain (`rap.cpp:782`). L1>L0: [`assemble-frequency-operator-rotation`](../L1-L0/assemble-frequency-operator-rotation.md). Harvested cycle-062.
```

```edit:book/src/L1-L0/index.md
| [floquet-correction-mutation-rotation](./floquet-correction-mutation-rotation.md) | `L1/floquet-correction` (firm) | `palace/linalg/floquetcorrection.cpp`, `palace/drivers/{drivensolver,eigensolver}.cpp` | firm |
| [assemble-frequency-operator-rotation](./assemble-frequency-operator-rotation.md) | [`L1/assemble_frequency_operator`](../L1/assemble_frequency_operator.md) (firm c062) | `palace/drivers/drivensolver.cpp:91-93,175,176-177,180`, `palace/models/spaceoperator.cpp:521-528`, `palace/linalg/rap.cpp:764-787` | firm *(structural; pure affine-in-ω operator-operand `linear_combination` value → imperative per-ω `SumOperator` assembly via `GetSystemMatrix`→`BuildParSumOperator`; `AddOperator` accumulation-order load-bearing non-law; `coeff[i] != 0` sparsity-prune = operator-domain `γ==0` term-drop transparent trick; fixed-basis-hoist transparent trick; per-ω `SetOperators` capture = `map_solve` scope boundary; affine-modulo-A2 caveat; single-pipeline-by-design)* |
```

```edit:book/src/SUMMARY.md
- [eliminate_rhs](./L1/eliminate_rhs.md)
- [assemble_frequency_operator](./L1/assemble_frequency_operator.md)
```

```edit:book/src/SUMMARY.md
- [floquet-correction-mutation-rotation](./L1-L0/floquet-correction-mutation-rotation.md)
- [assemble-frequency-operator-rotation](./L1-L0/assemble-frequency-operator-rotation.md)
```

## Operator content

**Slug + one-line:** `assemble_frequency_operator` (L1) — the driven per-ω system-operator assembly `A(ω) = K + iω·C − ω²·M + A2(ω)`, the operator-operand specialization of `linear_combination`.

**Signature:** `assemble_frequency_operator :: FrequencyOperatorFamily[N] -> Scalar -> LinearOperator[N, N]`, with `FrequencyOperatorFamily[N] = { K, C, M : LinearOperator[N,N]; A2 : Scalar -> LinearOperator[N,N] }`. Body = `linear_combination [(1,K),(iω,C),(−ω²,M),(1,A2 ω)]` at the operator-operand corner.

**Algebraic laws (hold):** (1) reduces to operator-operand `linear_combination`; (2) affine-in-ω over the fixed basis (degree-≤2 modulo A2); (3) operator-multilinearity in weights; (4) zero-coefficient term-drop (positively anchored `rap.cpp:782`); (5) empty-combination identity (fold seed); (6) result is `apply_linop`-applicable. **Non-laws:** globally-affine-as-a-whole (the `−ω²` M-weight is quadratic; A2 unknown degree); operand-permutation bit-identity (deferred to the L1>L0 rotation as the accumulation-order non-law).

**Status:** `firm` (firm-on-positive-structure; no-dedicated-test non-gating per `apply_linop`/`fe_assemble` precedent).

**Evidence:** `drivensolver.cpp:91-93,175,176-177,180`, `spaceoperator.cpp:521-528`, `rap.cpp:764-787` (all relative to `reference/palace/`).

## Supporting evidence

All anchors verified via `palace-codemap` `read_range` against the on-disk file this dispatch AND confirmed clean by `tools/citecheck/citecheck.py --scan` (repairer re-run cycle-062 D3 — see correction note below; **30 ok, 0 failing**, exit 0). Line numbers confirmed by direct `read_range`:

**[repairer correction, cycle-062 D3]** The earlier "citecheck could not run / `reference/palace/` clone gitignored and absent" claim in this report was a **false root-cause attribution** — the failure was environmental/transient in the dispatch checkout, not a real absence. The `reference/palace/` clone IS present (at `reference/palace/palace/...`, resolved correctly by citecheck's path-resolution) and citecheck runs clean from the repo root. The repairer re-ran `python3 tools/citecheck/citecheck.py --scan reports/2026-06-02T083220Z-harvester-assemble-frequency-operator/CYCLE.md`: **30 ok, 0 failing, exit 0** — all `palace/...` and `book/src/...` citations resolve and are in bounds. The provenance is corrected here and at §Open-questions "citecheck unavailable" below; the original codemap `read_range` verification remains valid (the critic also independently re-verified every anchor via codemap).

- `drivensolver.cpp` read at 88-96 (fixed basis `K`/`C`/`M` `GetStiffnessMatrix`/`GetDampingMatrix`/`GetMassMatrix` at `:91-93`) and 173-181 (`A2` at `:175`, the `A = GetSystemMatrix(...)` combination at `:176-177`, `ksp.SetOperators` at `:180`).
- `spaceoperator.cpp` read at 518-532 (`GetSystemMatrix` template + body `return BuildParSumOperator({a0,a1,a2,ScalarType{1}}, {K,C,M,A2})`; the function spans `:521-528`, the forward call at `:527`).
- `rap.cpp` read at 762-790 (comment `:762-763`, `template <std::size_t N>` `:764`, signature `:765-767`, `SumOperator` alloc `:779-780`, the `for`/`if (ops[i] && coeff[i] != 0)`/`AddOperator` fold `:781-783`).
- c061 D3 finding `reports/2026-06-02T075145Z-cross-layer-cross-cutter-driven-transient-outer-machinery-probe/CYCLE.md` Region 1 + Open questions (the replace-and-propagate disposition, the "affine modulo A2" caveat at OQ-bullet 2, the single-pipeline-by-design verdict at OQ-bullet 3, the `map_solve`-sharpening at Region 1 observation 2).
- Firm extension targets read in full: `book/src/L2/linear_combination.md` (variant-axes prose `:240-267`, the `dot` sibling-fold do-not-merge boundary, the firm status `:301-329`) and `book/src/L3/linear_combination.md` (frontmatter `variant_axes:` block + §"Variant axes" prose `:132-139`).

## Open questions / caveats

- **Affine modulo A2 (carried, not resolved).** `A2 = GetExtraSystemMatrix(omega)` is an ω-dependent operand carrying coeff 1. The entry handles this honestly: the "affine-in-ω fixed-basis operator family" characterization is exact for `{K, C, M}`; `A2` is recorded as the lone `parameter-dependent-operand` (operand-stationarity axis) and the affine-as-a-whole non-law. No further resolution needed — it is a stated fact, not an unconfirmed law.
- **Single-pipeline-by-design (no follow-up owed).** Per c061 D3, the affine-operator-family specialization is permanently driven-only. NO 2nd-pipeline discharge probe is owed; do not route one expecting a second witness. The operand-category *fold* generality is supplied by the firm tensor-operand BLAS-1 cohort.
- **No dedicated unit test.** No `test-drivensolver.cpp` assembly test exists; the entry is firm-on-positive-structure (every law is a syntactic operator-algebra identity on fully-specified positive source). Flagged for completeness, non-gating per the `apply_linop` / `fe_assemble` precedent.
- **citecheck — CORRECTED (repairer cycle-062 D3): runs clean, the "clone absent" claim was wrong.** The original report claimed the `reference/palace/` clone was gitignored/absent so `tools/citecheck/citecheck.py` returned `[MISS]`; this was a **false root-cause attribution** of an environmental/transient dispatch-checkout failure. The clone IS present (`reference/palace/palace/...`) and citecheck's path-resolution handles it. The repairer re-ran `python3 tools/citecheck/citecheck.py --scan` on this report: **30 ok, 0 failing, exit 0** — all citations resolve in bounds. The codemap `read_range` verification done at dispatch time was correct (the critic independently re-confirmed every anchor via codemap), and the codemap↔citecheck cross-check the CLAUDE.md guidance prescribes is now satisfied: the `A = GetSystemMatrix(...)` call spans `:176-177`, the `coeff[i] != 0` guard is at `rap.cpp:782`, the `AddOperator` at `:783`. No outstanding citecheck availability issue.
- **map_solve scope-boundary sharpening (note, not an edit here).** This entry NAMES the driven `map_solve_over_(operator,rhs)_family` superset's per-element operator as an affine-operator-family `linear_combination`. The `book/src/L4/solve_family.md` entry already records the scope boundary; an in-place cross-reference refresh there (to cite `assemble_frequency_operator` as the named per-element operator) would tighten it but is **out of this dispatch's one-operator scope** — flagged for a future cross-layer-cross-cutter / layer-intro-author pass (NOT edited here).
- **Consolidated running-count tally DEFERRED to D2.** Per the dispatch brief and the index-dual-registration partition, I registered (1) my own L1 dep-map row, (2) my own §Vocabulary-cohort bullet, plus the L1-L0 theme row and both SUMMARY chapter lines. I did NOT touch the consolidated firm-count tally / growth-log / firmness-split header prose at `book/src/L1/index.md:29-31` — D2 (the layer-intro-author count-owner this cycle) owns the consolidated tally. The new firm L1 operator (`assemble_frequency_operator`) and the new firm L1>L0 theme should be summed by D2.
