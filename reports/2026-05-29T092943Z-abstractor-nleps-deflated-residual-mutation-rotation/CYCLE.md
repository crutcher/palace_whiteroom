---
agent: abstractor
invoked_at: 2026-05-29T09:29:43Z
scope: L1>L0 theme sketch — nleps-deflated-residual-mutation-rotation
status: pending
integrated_at: 2026-05-29T10:46:32Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "Applied clean (staging row 5); applied the REPAIRED CYCLE.md (scaffolding-section link-depth fix only; new: fence intact, no cycle-019 truncation). NEW firm L1>L0 theme book/src/L1-L0/nleps-deflated-residual-mutation-rotation.md (3 sub-patterns A Mult+AddMult collapse / B deflation back-projection / C extended-space norm). L1>L0 firm themes +1 (2nd this cycle); SUMMARY + L1-L0/index dep-map row. 2 OQs promoted. Discharges the nleps_deflated_residual half of the NLEPS L1>L0 cohort. apply_nonlinear_pencil + nleps_deflated_solve L1>L0 themes still plain-text forward-refs. No gate hits."
inputs:
  - book/src/L1/nleps_deflated_residual.md (firm L1 operator, landed cycle-022)
  - palace/linalg/nleps.cpp:547-577 (compute_residual lambda — the L0 source)
  - palace/linalg/nleps.cpp:329-347 (MatVecMult — the X·y back-projection primitive)
  - palace/linalg/nleps.cpp:587, :702 (the two compute_residual call sites)
  - book/src/L1-L0/dot-mutation-rotation.md (Sub-pattern A — fused linalg::Dot)
  - book/src/L1/dot.md:43 (arg-1-conjugated convention)
  - book/src/L2-L1/linear-combination-fold-specialization.md (the X· back-projection lowering)
---

# CYCLE: L1>L0 theme sketch — nleps-deflated-residual-mutation-rotation

## Summary

The firm L1 `nleps_deflated_residual` operator (landed cycle-022) lowers into the
`compute_residual` lambda at `palace/linalg/nleps.cpp:547-577` — the deflated-residual
evaluator inside Palace's `QuasiNewtonSolver` NEP loop. This theme narrates that forward
rewrite (L1 → L0). The load-bearing rotation point is the **`Mult` + `AddMult` →
single-pencil-apply collapse**: Palace splits the big-space residual into `A->Mult(vv, rr)`
(`:559`, `T(λ)·vv`) and `A->AddMult(XSvv2, rr, 1.0)` (`:564`, `+T(λ)·X·(λI−H)⁻¹·vv₂`) sharing
**one** `BuildParSumOperator` pencil (`:557`); by the linearity-in-`v` of
`apply_nonlinear_pencil` the two-step accumulation realizes a single pencil apply of the
deflation-corrected vector `vv + X·(λI−H)⁻¹·vv₂`. The theme decomposes into three sub-patterns
(A: pencil apply via Mult+AddMult collapse; B: deflation correction via `fullPivLu().solve`
∘ `MatVecMult`; C: extended-space two-component norm), reuses the firm `dot-mutation-rotation`
Sub-pattern A for the fused `linalg::Dot` coordinate/self-dot surface (NOT re-derived), and is
justified **structural** (syntactic expansion of the pure L1 form into the C++ destination-buffer
composition). Status `firm`: every constituent reads from a positive source site, matching the
firm-on-positive-structure precedent of the operator it extends.

## Proposed changes

```new:book/src/L1-L0/nleps-deflated-residual-mutation-rotation.md
---
status: firm
layer: L1>L0
theme: nleps-deflated-residual-mutation-rotation
l1_anchor: book/src/L1/nleps_deflated_residual.md
l0_anchor: palace/linalg/nleps.cpp:547-577
justification: structural
---

# nleps-deflated-residual-mutation-rotation

How the firm L1 [`nleps_deflated_residual`](../L1/nleps_deflated_residual.md) form lowers into
its L0 source: the `compute_residual` lambda inside Palace's `QuasiNewtonSolver` NEP loop
(`palace/linalg/nleps.cpp:547-577`). This is the **deflation extension** of the bare-pencil
lowering; when `k = 0` it degenerates to one `apply_nonlinear_pencil` of `vv` plus a norm.

## Slug

`nleps-deflated-residual-mutation-rotation`

## Status

`firm` — every constituent of the rewrite is read from a **positive** source site (the
`compute_residual` lambda, `palace/linalg/nleps.cpp:547-577`, with the source's own naming
comment at `:547-549`). The big-space residual is two `Mult`/`AddMult` calls on a
`BuildParSumOperator` pencil (`:557-564`), the deflation correction is a positive
`MatVecMult(X, S.fullPivLu().solve(vv2))` (`:563`), the coordinate residual is a positive
`linalg::Dot` loop (`:565-570`), the norm is a positive `std::sqrt(...)` (`:575`). The rewrite
is a **structural** syntactic expansion — no sub-part is materialized from negative anchors,
so there is no `partly-constructive` caveat. This matches the firm-on-positive-structure
status of the operator this theme lowers (`book/src/L1/nleps_deflated_residual.md:111-117`) and
of the interior atom it extends (`book/src/L1/apply_nonlinear_pencil.md:98`): the laws are
syntactic identities on fully-specified positive source, so the NLEPS test-coverage absence
(`search_text` for `QuasiNewton|nleps|funcA2|GetResidualNorm` over `test/unit/**` returns zero
hits) does not gate the firm decision.

## L1 form (LHS)

The pure-functional L1 operator — no destination buffers, no `A2`-caching, no build-form choice
in the signature (`book/src/L1/nleps_deflated_residual.md:16-29`):

```text
nleps_deflated_residual
  :: (T: NonlinearPencil[N], λ: Complex, P: DeflationState[N, k], vv: Tensor[N], vv₂: Vec[k])
     -> { r: Tensor[N], r₂: Vec[k], norm: Real }

nleps_deflated_residual(T, λ, P, vv, vv₂) =
  let S  = λ·I[k] − P.H                       -- the k×k linearization block
      c  = lu_solve(S, vv₂)                   -- (λI − H)⁻¹ · vv₂   (dense k×k solve)
      d  = vv + linear_combination(P.X, c)    -- deflation-corrected vector: vv + X·c
      r  = apply_nonlinear_pencil(T, λ, d)    -- T(λ)·(vv + X·(λI−H)⁻¹·vv₂)
      r₂ = [ dot(P.X[j], vv) | j ← 0..k−1 ]   -- Xᴴ·vv   (deflation coordinates)
  in { r, r₂, norm = √(‖r‖₂² + ‖r₂‖₂²) }
```

## L0 form (RHS)

The `compute_residual` lambda — captures `k`, `H`, `X` by reference and takes `(lam, vv, vv2,
rr, rr2, A2_out)`, overwriting the destination buffers `rr` / `rr2` and returning the scalar
norm (`palace/linalg/nleps.cpp:547-577`):

```text
// nleps.cpp:547-549 — the source's own statement of the residual:
//   "Evaluate the deflated residual r = T(lam) vv + T(lam) X (lam I - H)^-1 vv2, with
//    rr2 = X^* vv. A2_out returns the built A2 operator so the caller can hold onto it..."
auto compute_residual = [this, &k, &H, &X]
  (std::complex<double> lam, const ComplexVector &vv, const Eigen::VectorXcd &vv2,
   ComplexVector &rr, Eigen::VectorXcd &rr2,
   std::unique_ptr<ComplexOperator> &A2_out) -> double
{
  A2_out = (*funcA2)(std::abs(lam.imag()));                                  // :556
  auto A = BuildParSumOperator({1.0 + 0.0i, lam, lam * lam, 1.0 + 0.0i},     // :557-558
                               {opK, opC, opM, A2_out.get()}, true);
  A->Mult(vv, rr);                                                          // :559  T(λ)·vv
  if (k > 0)                                                                // :560
  {
    const Eigen::MatrixXcd S = lam * Eigen::MatrixXcd::Identity(k, k) - H;  // :562  S = λI − H
    const ComplexVector XSvv2 = MatVecMult(X, S.fullPivLu().solve(vv2));    // :563  X·(λI−H)⁻¹·vv₂
    A->AddMult(XSvv2, rr, 1.0);                                             // :564  += T(λ)·XSvv2
    rr2.conservativeResize(k);                                             // :565
    for (int j = 0; j < k; j++)                                            // :566
    {
      rr2(j) = linalg::Dot(GetComm(), vv, X[j]);                          // :568  X[j]ᴴ·vv
    }
  }
  else
  {
    rr2.resize(0);                                                        // :573
  }
  return std::sqrt(std::abs(linalg::Dot(GetComm(), rr, rr))               // :575  √(‖r‖² + ‖r₂‖²)
                   + rr2.squaredNorm());
};
```

## Rewrite — forward (L1 → L0)

The pure `nleps_deflated_residual(T, λ, P, vv, vv₂)` rewrites to the `compute_residual` lambda
applied with destination buffers `rr`, `rr₂` (in place of the returned `r`, `r₂`) and an
`A2_out` cache (in place of the absorbed pencil build). The rewrite proceeds in three stages;
each is a sub-pattern below.

The L0-only material the L1 signature drops:

- **Destination buffers.** `rr` (a `ComplexVector &`) and `rr2` (an `Eigen::VectorXcd &`) are
  output reference parameters overwritten in place (`:559`, `:564`, `:565-570`, `:573`); the L1
  form returns `{ r, r₂, norm }` by value. The committed-point and backtrack call sites pass
  the *same* `u` / `u2` scratch buffers across iterations (`:587`, `:702`) — buffer reuse, a
  transparent L1>L0 trick.
- **`A2_out` carry-back.** `A2_out = (*funcA2)(|Im λ|)` (`:556`) is returned by reference so the
  caller can hold the built nonlinear closure and skip re-assembly at the same `λ` across a line
  search (`:547-549` comment). Pure-functional re-evaluation at L1; an L0 caching concern only.
- **The pencil build is duplicated logic.** `BuildParSumOperator({1, λ, λ², 1}, {opK, opC, opM,
  A2_out.get()}, true)` (`:557-558`) re-builds the same pencil shape used in the solver's
  in-`Solve` setup; inherited from `apply_nonlinear_pencil`'s lowering (the `{1, λ, λ², 1}`
  pencil-build form), referenced here, not re-derived.

### Sub-pattern A — big-space residual: `Mult` + `AddMult` → single pencil apply (the collapse)

This is the load-bearing rotation point. Palace builds the big-space residual `r` with **two
operator applies sharing one pencil**:

```text
A->Mult(vv, rr);              // :559   rr  := T(λ)·vv
A->AddMult(XSvv2, rr, 1.0);   // :564   rr  += 1.0 · T(λ)·XSvv2   (only when k > 0)
```

where `A` is the *single* `BuildParSumOperator({1, λ, λ², 1}, {opK, opC, opM, A2_out.get()},
true)` (`:557-558`) and `XSvv2 = X·(λI−H)⁻¹·vv₂` is the deflation correction (Sub-pattern B).
Both applies invoke the **same** operator `A`; `Mult` writes the destination, `AddMult`
accumulates with scale `1.0`. The L0 thus computes

```text
rr = T(λ)·vv + T(λ)·XSvv2.
```

By the **linearity-in-`v`** of `apply_nonlinear_pencil` (its law 1 — `T(λ)·a + T(λ)·b =
T(λ)·(a + b)`, `book/src/L1/apply_nonlinear_pencil.md`), this two-step accumulation is exactly

```text
rr = T(λ)·(vv + XSvv2) = apply_nonlinear_pencil(T, λ, vv + X·(λI−H)⁻¹·vv₂),
```

i.e. one pencil apply of the deflation-corrected vector — the L1 `r = apply_nonlinear_pencil(T,
λ, d)` with `d = vv + linear_combination(P.X, c)`. The L0 split into `Mult` + `AddMult` **avoids
materializing the `vv + XSvv2` temporary** (it accumulates the second term directly into the
destination already holding the first); this is a **transparent performance trick** at L1 — the
value is identical, only the intermediate buffer is elided.

The split is, however, **not bit-identical** to the single corrected-vector apply: the two-step
accumulation orders the floating-point additions differently from `T(λ)·(vv + d)`, and the
matrix-free `A2` term inherits reduction-tree non-associativity from `apply_linop`. Law 2's
identity is mathematical; its floating-point realization is exact modulo accumulation-order
noise (`book/src/L1/nleps_deflated_residual.md:85`, the recorded non-law). Load-bearing per the
CLAUDE.md trick taxonomy, recorded not erased.

Justification kind: **structural** (with a load-bearing accumulation-order note) — the rewrite
is the syntactic recognition that the `Mult`+`AddMult` pair on one pencil is a linearity-collapse
of the corrected-vector apply.

Citations:
- `palace/linalg/nleps.cpp:547-549` — the source's own residual statement (`r = T(lam) vv +
  T(lam) X (lam I - H)^-1 vv2`).
- `palace/linalg/nleps.cpp:557-558` — `BuildParSumOperator({1, λ, λ², 1}, {opK, opC, opM,
  A2_out.get()}, true)`: the single shared pencil.
- `palace/linalg/nleps.cpp:559` — `A->Mult(vv, rr)`: `rr := T(λ)·vv`.
- `palace/linalg/nleps.cpp:564` — `A->AddMult(XSvv2, rr, 1.0)`: `rr += T(λ)·XSvv2` (the
  accumulating apply with scale 1.0).
- `palace/linalg/nleps.cpp:560` — `if (k > 0)`: the `AddMult` is gated; when `k = 0` only
  `:559` runs, so `rr = T(λ)·vv` is the bare-pencil residual (law 1 reduction).

### Sub-pattern B — deflation correction: `fullPivLu().solve` ∘ `MatVecMult` (the back-projection)

The corrected-vector addend `XSvv2 = X·(λI−H)⁻¹·vv₂` is built in one C++ line (`:563`):

```text
const Eigen::MatrixXcd S = lam * Eigen::MatrixXcd::Identity(k, k) - H;   // :562  S = λI − H
const ComplexVector XSvv2 = MatVecMult(X, S.fullPivLu().solve(vv2));     // :563
```

This composes the two firm constituents `c = lu_solve(S, vv₂)` and `linear_combination(X, c)`:

1. **`S = lam * Identity(k,k) - H`** (`:562`) materializes the `k×k` linearization block `S =
   λI[k] − H` as a dense `Eigen::MatrixXcd`. (`H` is the redundantly-stored Rayleigh block; `k`
   is the deflation cardinality.)
2. **`S.fullPivLu().solve(vv2)`** (`:563`) is the dense `k×k` factor-and-solve — the L1
   [`lu_solve`](../L1/lu_solve.md) leaf realizing `c = (λI−H)⁻¹·vv₂` (full-pivot LU, `Eigen`).
   This is distinct from the iterative big-space `ksp_solve`; the small-dense solve runs entirely
   on the redundant coordinate space. *(`lu_solve` has no L1>L0 theme yet — plain-text
   forward-reference.)*
3. **`MatVecMult(X, c)`** (`:563`) is the back-projection `X·c = Σⱼ c(j)·X[j]` — the length-`k`
   [`linear_combination`](../L2/linear_combination.md) fold over the deflation basis. Its L0 body
   (`palace/linalg/nleps.cpp:329-347`) zero-initializes `z`, then for each `j` does two
   real-valued `linalg::AXPBYPCZ` calls (the complex-vector real/imag split:
   `z.Real += c(j).real·X[j].Real − c(j).imag·X[j].Imag`,
   `z.Imag += c(j).imag·X[j].Real + c(j).real·X[j].Imag`). The complex `c(j)·X[j]` is the
   four-real-multiply complex product expanded across the `.Real()` / `.Imag()` carriers — a
   transparent realization of the complex AXPY accumulation. The L2>L1 lowering of this fold is
   [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md);
   this theme references its `MatVecMult` realization, it does not re-derive the fold.

The composition order is `lu_solve` first (small-dense), then `linear_combination` (big-space
fold) — matching the L1 `c = lu_solve(S, vv₂)`; `d = vv + linear_combination(P.X, c)`. The `vv +`
addition does **not** appear here as a separate vector add: it is folded into Sub-pattern A's
`Mult`+`AddMult` collapse (`A->Mult(vv,…)` supplies the `T(λ)·vv` term, `A->AddMult(XSvv2,…)`
supplies the `T(λ)·XSvv2` term — their sum is `T(λ)·(vv + XSvv2)`).

**The deflation basis `X` is NOT orthonormal** — it stores raw normalized eigenvectors with no
inter-column orthogonalization (`palace/linalg/nleps.cpp:606-619`: each converged `v` scaled by
`1/‖v‖₂` at `:610-611`, stored at `X[k] = v` at `:615`, no Gram-Schmidt). This is *why* the
coupling carries the `(λI−H)⁻¹` linearization-block solve rather than a trivial transpose; the
non-orthonormal basis is load-bearing and is the same fact that keeps the L2 `deflate` combinator
distinct from `orthogonalize` (the cycle-021 over-unification guard). Recorded here so the
lowering does not collapse the `fullPivLu().solve` into a no-op.

Justification kind: **structural** — `:563` is the syntactic composition `MatVecMult ∘
fullPivLu().solve`; the two firm leaves are recognized, not constructed.

Citations:
- `palace/linalg/nleps.cpp:562` — `S = lam * Eigen::MatrixXcd::Identity(k, k) - H`: the `k×k`
  block `S = λI − H`.
- `palace/linalg/nleps.cpp:563` — `MatVecMult(X, S.fullPivLu().solve(vv2))`: the `lu_solve`
  (dense `fullPivLu().solve`) composed with `linear_combination` (`MatVecMult(X, ·)`).
- `palace/linalg/nleps.cpp:329-347` — `MatVecMult(X, y)`: the `X·y` fold body (`z = 0`;
  per-`j` complex AXPY via two `AXPBYPCZ` on the real/imag carriers).
- `palace/linalg/nleps.cpp:606-619` — deflation-basis growth (normalize at `:610-611`, store at
  `:615`, no orthogonalization): the `X`-not-orthonormal fact.

### Sub-pattern C — extended-space two-component norm + coordinate residual (the fused `linalg::Dot` surface)

The coordinate residual and the norm both reach the `yᴴ x` reduction through the **fused**
free-function `linalg::Dot` — `dot-mutation-rotation` **Sub-pattern A**
(`book/src/L1-L0/dot-mutation-rotation.md:44-81`), the `Mpi::GlobalSum(1, &dot) ∘ LocalDot(x, y)`
two-step where `LocalDot(x, y) = yᴴ x` conjugates the **C++ arg-2**. This is the canonical fused
form, **not** the unfused hook-routed Sub-pattern D — `compute_residual` does not route through
the `InnerProductHelper` template hook (that is the Gram-Schmidt-only surface); it calls
`linalg::Dot` directly. The conjugation is **not re-derived here**; it is cited from
Sub-pattern A.

**Coordinate residual** `r₂` (`:565-570`):

```text
rr2.conservativeResize(k);                          // :565
for (int j = 0; j < k; j++)                          // :566
  rr2(j) = linalg::Dot(GetComm(), vv, X[j]);        // :568   = X[j]ᴴ · vv
```

Under Sub-pattern A's `linalg::Dot(comm, x, y) = yᴴ x` with `x = vv`, `y = X[j]`, the **C++
arg-2 `X[j]`** (the basis vector) is conjugated: `rr2(j) = X[j]ᴴ·vv`. This is the L1 `r₂(j) =
dot(P.X[j], vv) = X[j]ᴴ vv` — the L1 `dot` convention conjugates its **arg-1**
(`book/src/L1/dot.md:43`), and the L1 arg-1 is the same conjugated operand as the C++ arg-2:
both name the **basis vector `X[j]`** as the conjugated operand. The two framings ("C++
arg-2-conjugating" / "L1 arg-1-conjugated") refer to the identical conjugated operand; pinned
once, not re-argued. This is the `Xᴴ·` half of the deflation projection (Sub-pattern B's
`X·(λI−H)⁻¹·` back-projection is the `X·` half).

**Extended-space norm** (`:575`):

```text
return std::sqrt(std::abs(linalg::Dot(GetComm(), rr, rr)) + rr2.squaredNorm());   // :575
```

Two components summed under one `std::sqrt`:

1. **Big-space** `‖r‖₂² = linalg::Dot(GetComm(), rr, rr)` — the self-dot `rrᴴ rr`, the
   distributed [`nrm2`](../L1/nrm2.md)² via the fused `linalg::Dot` (Sub-pattern A again). The
   `std::abs(...)` strips the (exactly-zero, modulo round-off) imaginary part of the Hermitian
   self-dot — the same transparent self-dot abs-guard recorded in `nrm2-mutation-rotation`.
2. **Coordinate-space** `‖r₂‖₂² = rr2.squaredNorm()` — the **local** `Eigen::VectorXcd`
   squared-norm; `rr2` is the redundantly-stored coordinate vector (length `k`), so its norm is
   a rank-local `Eigen` reduction with **no** MPI collective (the coordinate space is replicated
   on all ranks).

The norm is the **extended-space 2-norm** `√(‖r‖² + ‖r₂‖²)` over `ℂ^{n+k}` — the convergence
quantity the quasi-Newton/Armijo loop drives below tolerance (`:587` committed-point call, `:702`
backtrack-trial call), *not* the big-space `nrm2` alone. When `k = 0` the `else { rr2.resize(0)
}` branch (`:573`) makes `rr2.squaredNorm() = 0`, so the norm degenerates to the bare-pencil
`‖T(λ)·vv‖₂` (the law-1 reduction).

Justification kind: **structural** — `:568` and `:575` are syntactic `linalg::Dot` /
`squaredNorm` reductions; the conjugation and the fused two-step are inherited from
`dot-mutation-rotation` Sub-pattern A.

Citations:
- `palace/linalg/nleps.cpp:565` — `rr2.conservativeResize(k)`: coordinate-residual sizing.
- `palace/linalg/nleps.cpp:566` — `for (int j = 0; j < k; j++)`: the `k`-entry loop.
- `palace/linalg/nleps.cpp:568` — `rr2(j) = linalg::Dot(GetComm(), vv, X[j])`: `r₂(j) =
  X[j]ᴴ·vv` (fused `linalg::Dot`, arg-2 = basis vector conjugated).
- `palace/linalg/nleps.cpp:571-574` — `else { rr2.resize(0); }`: the `k = 0` empty-coordinate
  branch.
- `palace/linalg/nleps.cpp:575` — `std::sqrt(std::abs(linalg::Dot(GetComm(), rr, rr)) +
  rr2.squaredNorm())`: the extended-space 2-norm (big-space self-dot + local coordinate
  squared-norm).
- `book/src/L1-L0/dot-mutation-rotation.md:44-81` — Sub-pattern A: the fused `linalg::Dot(comm,
  x, y) = yᴴ x` two-step (arg-2-conjugated). NOT Sub-pattern D (Gram-Schmidt hook-routed).
- `book/src/L1/dot.md:43` — the L1 `⟨x, y⟩ = xᴴ y` arg-1-conjugated convention.

## Applicability conditions

- The pencil `T(λ)` is bound exactly as for `apply_nonlinear_pencil` — `{1, λ, λ², 1}` over
  `{opK, opC, opM, A2(|Im λ|)}` (`:556-558`); the `with-C` / `without-C` damping axis is
  absorbed by the pencil argument.
- Element type is **complex-only** (the NEP pencil and the `ComplexVector` / `Eigen::VectorXcd`
  carriers). No real specialization.
- The deflation cardinality `k` is **variadic** — it grows by one per converged eigenpair
  (`:606-619`); the rewrite is parameterized by `k`, with the `k = 0` branch the un-deflated
  degeneration (the `if (k > 0)` guard at `:560`, `else { rr2.resize(0) }` at `:573`).
- Single-rank scope (CLAUDE.md "Scope"): the `Mpi::GlobalSum` inside `linalg::Dot` (Sub-pattern
  A) lowers to a local no-op on one rank but is structurally present and carries the
  bit-deterministic-reduction-order trade-off. The coordinate `rr2.squaredNorm()` is rank-local
  by construction (replicated coordinate space).

## Justification kind

**Structural** — the rewrite is the syntactic expansion of one pure L1 form into the L0
destination-buffer composition. Three structural recognitions carry the theme: (A) the
`Mult`+`AddMult`-on-one-pencil pair is a linearity-in-`v` collapse of the corrected-vector
pencil apply; (B) `:563` is the syntactic composition `MatVecMult ∘ fullPivLu().solve` of two
firm leaves; (C) `:568` / `:575` are fused `linalg::Dot` / `squaredNorm` reductions inherited
from `dot-mutation-rotation` Sub-pattern A. The one load-bearing non-structural note is the
`Mult`+`AddMult` accumulation-order bit-difference (Sub-pattern A), recorded per the trick
taxonomy.

## Speculative L1 operators

None. Every constituent is **already firm L1 vocabulary**: `apply_nonlinear_pencil` (firm,
cycle-021), `lu_solve` (firm, cycle-022), `dot` (firm), `nrm2` (firm), `linear_combination`
(firm L2). This theme proposes no new rough-in operators — it composes existing firm leaves.

## Verified-against

- `palace/linalg/nleps.cpp:547-577` — the complete `compute_residual` lambda (the positive L0
  site). All pinpoint anchors below mechanically confirmed via `tools/citecheck` (bounds + token
  anchor) and `palace-codemap` `read_range`.
- `palace/linalg/nleps.cpp:587` — `compute_residual(eig, v, v2, u, u2, A2n)`: the committed-point
  residual call (convergence quantity).
- `palace/linalg/nleps.cpp:702` — `compute_residual(eig_trial, v_trial, v2_trial, u, u2, A2n)`:
  the Armijo-backtrack trial residual call (line-search convergence quantity).
- `palace/linalg/nleps.cpp:329-347` — `MatVecMult(X, y)`: the back-projection fold body.
- `palace/linalg/nleps.cpp:606-619` — deflation-basis growth (`X`-not-orthonormal, variadic-`k`).
- `book/src/L1/nleps_deflated_residual.md` — the firm L1 operator this theme lowers (its laws 1
  and 2 are the basis for Sub-patterns A and B; its `:111-117` firm-status is the precedent).
- `book/src/L1/apply_nonlinear_pencil.md` — the interior pencil-apply atom (linearity-in-`v` law
  1; the `{1, λ, λ², 1}` pencil-build form). No L1>L0 theme yet — plain-text reference.
- `book/src/L1-L0/dot-mutation-rotation.md:44-81` — Sub-pattern A (fused `linalg::Dot`), reused
  for the coordinate residual and the big-space norm self-dot.
- `book/src/L2-L1/linear-combination-fold-specialization.md` — the L2>L1 lowering of the
  `MatVecMult` back-projection fold; live link.
- No dedicated unit test (NLEPS test-coverage absence inherited from `apply_nonlinear_pencil` /
  `eigsolve`); the firm decision rests on exhaustive positive structural citation.
```

```edit:book/src/L1-L0/index.md
| [dot-mutation-rotation](./dot-mutation-rotation.md) | `L1/dot` (firm) | `palace/linalg/vector.{hpp,cpp}`, `palace/utils/communication.hpp` | firm *(structural; 3 surface forms; conjugate-pair re-order `xᴴ y = conj(yᴴ x)`; tdot type-API-surface-only)* |
| [nleps-deflated-residual-mutation-rotation](./nleps-deflated-residual-mutation-rotation.md) | `L1/nleps_deflated_residual` (firm) | `palace/linalg/nleps.cpp:547-577` (+ `:329-347` MatVecMult, `:587`/`:702` call sites) | firm *(structural; 3 sub-patterns A/B/C; load-bearing Mult+AddMult→single-pencil-apply collapse; reuses dot Sub-pattern A; reuses lin-comb fold L2>L1)* |
```

```edit:book/src/SUMMARY.md
- [dot-mutation-rotation](./L1-L0/dot-mutation-rotation.md)
- [nleps-deflated-residual-mutation-rotation](./L1-L0/nleps-deflated-residual-mutation-rotation.md)
- [nrm2-mutation-rotation](./L1-L0/nrm2-mutation-rotation.md)
```

(Integrator: the SUMMARY insert anchor is the `dot-mutation-rotation` line; the new
`nleps-deflated-residual-mutation-rotation` line is inserted between it and the existing
`nrm2-mutation-rotation` line. The `nrm2` line is shown only to disambiguate the insert
position — it already exists and is not added.)

## Speculative operators proposed

None. This theme composes only **already-firm** L1/L2 leaves:

- [`apply_nonlinear_pencil`](../../book/src/L1/apply_nonlinear_pencil.md) — firm (cycle-021); the big-space pencil apply.
- [`lu_solve`](../../book/src/L1/lu_solve.md) — firm (cycle-022); the dense `k×k` `(λI−H)⁻¹` solve.
- [`dot`](../../book/src/L1/dot.md) — firm; the coordinate residual + big-space self-dot.
- [`nrm2`](../../book/src/L1/nrm2.md) — firm; the big-space norm.
- `linear_combination` — firm L2; the `MatVecMult(X, ·)` back-projection fold.

No rough-in operators are introduced; harvester has nothing to pick up from this dispatch.

## Supporting evidence

All citations mechanically verified before emit (bounds via `tools/citecheck/citecheck.py`,
token anchors via `--anchor` / `--regex`, source confirmed via `palace-codemap` `read_range`):

- `palace/linalg/nleps.cpp:547-577` — the `compute_residual` lambda (full positive L0 site). Read in full.
- `:556` `A2_out = (*funcA2)(std::abs(lam.imag()))`; `:557-558` `BuildParSumOperator({1, λ, λ², 1}, …)`.
- `:559` `A->Mult(vv, rr)`; `:560` `if (k > 0)`; `:562` `S = lam*Identity(k,k) - H`;
  `:563` `MatVecMult(X, S.fullPivLu().solve(vv2))`; `:564` `A->AddMult(XSvv2, rr, 1.0)`.
- `:565` `rr2.conservativeResize(k)`; `:566` loop; `:568` `rr2(j) = linalg::Dot(GetComm(), vv, X[j])`;
  `:571-574` `else { rr2.resize(0); }`; `:575` `std::sqrt(std::abs(linalg::Dot(...)) + rr2.squaredNorm())`.
- `:587` committed-point call; `:702` Armijo-backtrack trial call.
- `:329-347` `MatVecMult(X, y)` body; `:606-619` deflation-basis growth (X-not-orthonormal, variadic-k).
- `book/src/L1-L0/dot-mutation-rotation.md:44-81` — Sub-pattern A (fused `linalg::Dot`), reused.
- `book/src/L1/dot.md:43` — arg-1-conjugated convention.

Every pinpoint anchor reported `[ok]` with the token on the asserted line (zero drift).

## Open questions / caveats

- **`apply_nonlinear_pencil` and `lu_solve` have no L1>L0 themes yet** — the references in
  Sub-patterns A/B are plain-text (the `BuildParSumOperator` pencil-build form and the
  `fullPivLu().solve` dense-solve lowering live elsewhere). When those themes land, this theme's
  Sub-pattern A (the pencil-build duplication note) and Sub-pattern B (the `lu_solve` step) can
  cross-link them as live links. Tracked as a forward-reference; not a blocker (this theme's job
  is the *composition* — the deflation extension — not the leaf lowerings).
- **Reverse-direction (lifting) note — working-note only, NOT in the theme body.** The L0
  `Mult`+`AddMult`-on-one-pencil pair is what *licenses* the L1 single-pencil-apply form: the
  lift recognizes the shared `A` operator across the two applies and the scale-`1.0` accumulation
  as the linearity collapse. The additional structure the lift needs is the
  `apply_nonlinear_pencil` linearity-in-`v` law (so the two applies compose to one corrected-vector
  apply) and the recognition that `A` is the same object in both calls (`:557` build, `:559`+`:564`
  use). Per the high→low discipline this is recorded here, not in the chapter.
- **Sub-pattern A's bit-non-determinism is the only non-structural element.** Everything else is a
  clean syntactic expansion. If a future lowering-verifier wants to tighten the accumulation-order
  claim, the relevant comparison is `T(λ)·vv + T(λ)·XSvv2` (two `AddMult`-into-`rr` accumulations)
  vs `T(λ)·(vv + XSvv2)` (one apply of a pre-summed vector) — the matrix-free `A2` reduction tree
  differs between them. This is already recorded as a non-law in the operator entry
  (`book/src/L1/nleps_deflated_residual.md:85`).
- **No over-unification with L2 `deflate`.** The theme deliberately does NOT identify the
  `Xᴴ·`/`X·` constituents with the L2 `deflate` projector — the coupling here is the Schur-modified
  `(λI−H)⁻¹` block, not the Gram inverse `(XᴴX)⁻¹`. The shared-constituents relationship is noted
  (Sub-patterns B and C name the halves) without asserting a projector identity, per the cycle-021
  over-unification guard carried in the operator entry.
