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

## Evidence

Paths relative to `reference/palace/`:

- `palace/drivers/drivensolver.cpp:91-93` — fixed basis `K`/`C`/`M` assembled once before the sweep.
- `palace/drivers/drivensolver.cpp:175` — `A2 = GetExtraSystemMatrix<ComplexOperator>(omega, DIAG_ZERO)` (ω-dependent operand).
- `palace/drivers/drivensolver.cpp:176-177` — `A = GetSystemMatrix(1+0i, iω, −ω²+0i, K, C, M, A2)` (per-ω combination).
- `palace/drivers/drivensolver.cpp:180` — `ksp.SetOperators(*A, *P)` (per-ω capture).
- `palace/models/spaceoperator.cpp:521-528` — `GetSystemMatrix` ≡ `BuildParSumOperator({a0,a1,a2,1}, {K,C,M,A2})`.
- `palace/linalg/rap.cpp:764-767` — `BuildParSumOperator<N>` template signature.
- `palace/linalg/rap.cpp:779-787` — `SumOperator` allocation + the `AddOperator` accumulate fold (`:783`) + the `coeff[i] != 0` sparsity prune (`:782`).
