# normalize

Mutation-lifted fused vector normalisation: compute `β = ‖x‖₂`, rescale `x ← x/β`, and **return both** `β` and the unit vector. The L1 lift of Palace's `linalg::Normalize` free function — the fused `nrm2` + `scal(1/nrm2, ·)` construct whose **returned norm** is load-bearing (Arnoldi Hessenberg sub-diagonal entry, spectral-radius eigenvalue estimate, deflation companion-vector scale).

## Context

`normalize` lifts the free-function template `linalg::Normalize(comm, x)` at `palace/linalg/vector.hpp:262-270` — which computes `auto norm = Norml2(comm, x); MFEM_ASSERT(norm > 0.0, ...); x *= 1.0 / norm; return norm;` — to a single pure-functional fused operator. It is the **only** Palace `scal` use that returns its scalar (the norm), and the returned scalar is the reason this is a distinct named operator rather than a bare composition: many call sites consume `β` *after* the rescale (the Arnoldi sub-diagonal, the power-iteration eigenvalue estimate, the deflation companion-vector scale). A bare `scal(1/nrm2(x), x)` discards that intermediate; `normalize` retains it in the result.

The two constituents are firm L1 leaves: [`nrm2`](./nrm2.md) (`β = √⟨x,x⟩`) and [`scal`](./scal.md) (`x/β = scal(1/β, x)`). `normalize` is the fused pairing — it is to `nrm2`/`scal` what `axpy` is to `scal`/vector-add: a recognised composite that Palace ships as one symbol. Unlike `axpy`, which returns nothing, `normalize` carries one extra load-bearing output (the recovered norm), and that extra returned scalar is what justifies naming the fusion. The fusion is named at [`scal`](./scal.md) §Dependencies and §L1-vs-L0, and the rescale half is the sub-pattern A of [`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md); this entry is the firm operator that consolidates them.

The element-type axis (real / complex, with a real-valued norm output regardless) is inherited from `nrm2` (the norm is always real) and `scal` (the rescale matches the input element type). No new variant axis is introduced by the fusion. The MPI collective folded inside `Norml2`'s inner `dot` is an L1>L0 concern, not part of this signature (single-rank is in scope per `CLAUDE.md`).

The B-weighted sibling `normalize_B` (rescale by the energy norm `√(xᴴ B x)`) is recorded below as a **rough-in note**, not a separate firm operator — Palace ships a fused B-weighted `Normalize(comm, x, B, Bx)` free function (`palace/linalg/operator.hpp:377-384`) and the underlying reduction [`matrix-weighted-norm`](./matrix-weighted-norm.md) (rough-in), but the fused B-Normalize is **uncalled** (zero 4-arg callsites in the tree), and the only inline B-energy contexts (`arpack.cpp:438`, `slepc.cpp:475`, `nleps.cpp:114`) call the reduction for residual-ratio computations that do not rescale. So `normalize_B` has the L1 algebraic form but no live consumer.

## Signature

    normalize :: (x: Tensor[N]) -> (Scalar, Tensor[N])
    normalize(x) = (β, x/β)  where  β = nrm2(x),  β > 0

Shape contract (bunsen-style, named axes):

- `x` — `Tensor[N]` — read-only (the *prior* value). Element type real or complex.
- result.0 — `Scalar` — **always real-valued and positive** (`β = ‖x‖₂ > 0`), regardless of `x`'s element type (inherited from `nrm2`'s real-valued-output collapse).
- result.1 — `Tensor[N]` — the unit vector `x/β`, same axis `N` and same element type as `x`. Has unit norm: `nrm2(result.1) = 1` (in exact arithmetic).

Applicability precondition: `β > 0`, i.e. `x ≠ 0`. The L0 source asserts this directly (`MFEM_ASSERT(norm > 0.0, "Zero vector norm in normalization!")` at `palace/linalg/vector.hpp:267`). `normalize` is **partial** — undefined on the zero vector. This is the one applicability condition distinguishing it from the (total) `nrm2` and `scal` leaves it composes.

## Semantics

Definitional: `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`. The norm is computed once and both returned and used as the rescale divisor — the fusion is the single-evaluation pairing, not a new arithmetic.

Reduction-tree non-associativity is **load-bearing**, inherited unchanged from the inner `nrm2` (hence from `dot`). The rescale `scal(1/β, ·)` is element-local and adds no reduction. The reciprocal-then-multiply (`1.0 / norm` then `x *= …`, rather than a per-element divide) is the L0 form; at L1 it is the algebraic `x/β`, and any reciprocal-vs-divide bit-difference is an L1>L0 transparent-trick note.

The **returned norm is the load-bearing output**. Three consumer shapes recur:
- The norm is captured into a separate structure and the unit vector is the working result (GMRES Arnoldi: `β` becomes the Hessenberg sub-diagonal `H[j+1,j]`, the unit `w` extends the Krylov basis — `palace/linalg/iterative.cpp:631-632`).
- The norm is the working result and the unit vector is the carrier for the next iteration (spectral-radius power iteration: `l = Normalize(comm, u)` returns the dominant-eigenvalue estimate, `u` is renormalised for the next `A·u` — `palace/linalg/operator.cpp:661` and `:673`).
- The norm rescales a *companion* quantity as well as `x` (NEP deflation: `scale` rescales both the basis vector `v` and its coordinate companion `v2 / scale` — `palace/linalg/nleps.cpp:610-611,617`; note this site uses the unweighted norm via an inline `Norml2` + `*=`, the same shape as `linalg::Normalize` but written out).

The operator is pure at L1: the prior `x` and the unit vector are distinct values, and `β` is a fresh scalar. The L0 source overwrites the receiver buffer in place and returns the norm by value; the L1>L0 lowering reintroduces the in-place rescale (it composes the [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) no-buffer reduction with the [`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md) sub-pattern A in-place rescale, plus the returned-scalar binding).

## Algebraic laws

The laws below hold for `x ≠ 0` (the operator's domain); absences are deliberate. Write `normalize(x) = (β, û)` with `β = nrm2(x)` and `û = x/β`.

1. **Unit output**: `nrm2(û) = 1` (in exact arithmetic). The defining property — the second result has unit norm.
2. **Norm recovery**: `β = nrm2(x)`. The first result is exactly the input's norm; this is the projection `fst ∘ normalize = nrm2`.
3. **Reconstruction**: `scal(β, û) = x`, i.e. `β · (x/β) = x`. The pair `(β, û)` losslessly reconstructs `x` (the inverse of the `scal` law-8 round-trip, with `α = 1/β`). This is why `normalize` is information-preserving where a bare unit-vector projection would not be.
4. **Positive homogeneity collapse (scale invariance of the unit vector)**: for any scalar `α ≠ 0`, `snd(normalize(scal(α, x))) = scal(α/|α|, û)`. For real positive `α`: `snd(normalize(α·x)) = û` (the unit vector is invariant under positive rescaling of the input). For complex `α`: the unit vector picks up the phase `α/|α|`. Correspondingly `fst(normalize(scal(α, x))) = |α|·β` (positive homogeneity inherited from `nrm2`).
5. **Idempotence of the unit vector (up to the trivial norm)**: `normalize(û) = (1, û)`. Normalising an already-unit vector returns norm `1` and the same vector. Equivalently `snd ∘ normalize ∘ snd ∘ normalize = snd ∘ normalize` (the unit-vector projection is idempotent) and `fst(normalize(snd(normalize(x)))) = 1`.
6. **Factorisation (the defining decomposition)**: `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`. This is the L1 statement of the fusion — both components in terms of the firm leaves. It is the law a lowering theme or an L2 consumer rewrites against.

Laws that explicitly **do not** hold:

- **Totality**: `normalize` is undefined at `x = 0` (`β = 0`, division by zero; the L0 `MFEM_ASSERT(norm > 0.0)` fires). Unlike `nrm2(0) = 0` and `scal(α, 0) = 0` (both total), the fused operator is **partial**. This is the single semantic addition of the fusion over its constituents.
- **Additivity / linearity**: `normalize(x + y) ≠ (β_x + β_y, û_x + û_y)` in any form — the norm is sublinear (triangle inequality, from `nrm2`) and the unit vector is a nonlinear (projective) function of the input. The operator is **not** linear in `x`; it is positively-homogeneous-of-degree-zero in the unit-vector component (law 4) and degree-one in the norm component.
- **Bit-level fusion equivalence**: the L0 reciprocal-then-multiply (`x *= 1.0/norm`) and an idealised per-element divide (`x[i] /= norm`) may differ at the bit level in IEEE-754. The reciprocal form is Palace's actual L0 (`vector.hpp:268`); pinning it is an L1>L0 transparent-trick note, not an L1 law — the algebraic value `x/β` is the same.

## Dependencies

L1-internal dependencies (this is a fused composite, not a leaf):

- [`nrm2`](./nrm2.md) — the norm computation `β = √⟨x,x⟩` (result.0, and the rescale divisor).
- [`scal`](./scal.md) — the rescale `û = scal(1/β, x)` (result.1).

Subsumption / sibling relationships (not dependencies):
- `normalize` is the fused pairing flagged at `book/src/L1/scal.md:65,85` and `book/src/L1/nrm2.md` — those entries name the composition; this entry consolidates it as a firm operator with the returned-norm output made first-class.
- Bare `scal(1/nrm2(x), x)` (norm discarded) is the projection `snd ∘ normalize`. When a consumer needs only the unit vector and not the norm, the `scal ∘ nrm2` spelling is equivalent; `normalize` is preferred when the norm is consumed downstream (the load-bearing case).

Downstream consumers at L1/L2 (cross-reference, not reverse-dependencies):
- GMRES Arnoldi basis-normalisation `H[j+1,j] = β; w ← w/β` (`iterative.cpp:631-632, 811`) — the L2 `krylov-step` Arnoldi body.
- Spectral-radius power iteration (`palace/linalg/operator.cpp:661,673` via `linalg::Normalize`) — the returned norm is the eigenvalue estimate.
- NEP deflation-basis growth (`nleps.cpp:610-611,617`) — inline form; norm rescales basis + coordinate companion.
- Gram-Schmidt output normalisation in [`orthogonalize`](./orthogonalize.md) / [`orthogonalize-composition-lowering`](../L2-L1/orthogonalize-composition-lowering.md) — the `nrm2`/`scal` normalize step after orthogonalisation (FGMRES, ROM basis-extension).

## Variant axes

`normalize` inherits exactly the element-type axis of its constituents and adds none:

- **element-type**: `real` | `complex`. The `linalg::Normalize` template is `VecType`-generic (`mfem::Vector` real / `ComplexVector` complex); the inner `Norml2` returns a real scalar in both cases (per [`nrm2`](./nrm2.md)) and the `*= 1.0/norm` rescale dispatches to the matching `operator*=` (per [`scal`](./scal.md), including the `imag(s)==0.0` real-into-complex promotion). At L1 these collapse to one operator parameterised by element type; the norm output is real-valued in all variants.

No constant-folding axis (the rescale scalar `1/β` is a runtime value, never `0`/`1`/`-1` by construction since `β > 0`). No reduction-order variant beyond `nrm2`'s inherited one. The only non-trivial semantic axis relative to the leaves is the **partiality** at `x = 0`, which is uniform across element types.

### B-weighted sibling `normalize_B` — rough-in note (NOT a separate firm operator)

The energy-norm normalisation `(β_B, x/β_B)` with `β_B = √(xᴴ B x)` for SPD `B` is a *recognised* construct but lands here as a **rough-in note**, deliberately not a separate firm chapter, for two reasons:

1. **Fused B-Normalize defined but uncalled.** Palace ships a fused B-weighted `Normalize(comm, x, B, Bx)` at `palace/linalg/operator.hpp:377-384` (def `:378`, B-weighted reduction `:380`, partiality guard `:381`, rescale `:382`, return `:383`) — structurally identical to the unweighted `vector.hpp:264` modulo threading `(B, Bx)` into the inner `Norml2`. The header comment at `palace/linalg/vector.hpp:262` ("Normalize the vector, possibly with respect to an SPD matrix B") is realised by the `palace/linalg/operator.hpp:378` overload, not by the unweighted `vector.hpp:264`. **However, the fused B-Normalize is uncalled**: a grep across `palace/` for 4-arg `Normalize(comm, x, B, Bx)` invocations finds zero callsites. The B-weighted *reduction* `linalg::Norml2(comm, x, B, Bx)` ([`matrix-weighted-norm`](./matrix-weighted-norm.md), `palace/linalg/operator.cpp:600-619`) IS used at three callsites (`palace/linalg/arpack.cpp:438`, `palace/linalg/slepc.cpp:475`, `palace/linalg/nleps.cpp:114`) but they are **error-norm / eigenvector-norm computations that do not rescale** — they feed `GetError` / residual ratios, not an in-place normalise.
2. **Inherited test-coverage bound.** `normalize_B`'s norm component is `matrix-weighted-norm`, which is `rough-in (test-coverage-bounded)` (no dedicated test on the SPD-weighted overload — `book/src/L1/matrix-weighted-norm.md:108-110`, `book/src/L1/index.md:80`). A fused `normalize_B` cannot be firmer than its norm constituent.

If/when a positive *callsite* of the fused B-Normalize surfaces — either a direct 4-arg `Normalize(comm, v, B, Bv)` invocation OR an inline B-weighted-rescale shape (`scale = Norml2(comm, v, B, Bv); v *= 1/scale`, distinct from the unweighted `nleps.cpp:610-611`) — `normalize_B` promotes to a firm sibling with signature:

    normalize_B :: (x: Tensor[N], B: LinearOperator[N, N]) -> (Scalar, Tensor[N])
    normalize_B(x, B) = (β_B, x/β_B)  where  β_B = matrix_weighted_norm(x, B),  B SPD,  β_B > 0

Its laws mirror `normalize`'s with `nrm2` → `matrix_weighted_norm` (unit output is B-unit: `matrix_weighted_norm(û, B) = 1`), conditioned on `B` SPD. Until a callsite surfaces, `normalize_B` is tracked as a queued candidate inheriting the `matrix-weighted-norm` promotion gate, NOT a firm operator. The mere existence of the fused operator at `palace/linalg/operator.hpp:378` does not promote it — a defined-but-dead operator carries no live algebraic-law evidence beyond the syntactic identity to the unweighted core (which the unweighted `normalize` already records).

## Status

`firm` — firm-on-positive-structure (the `apply_nonlinear_pencil` / `lu_solve` precedent). The signature matches `linalg::Normalize` exactly; the body is a read closure (`vector.hpp:262-270`), not a literature reconstruction; the six algebraic laws are syntactic identities on that positive source plus the inherited `nrm2`/`scal` algebra (themselves firm). The absence of a dedicated `test-normalize` does not gate the laws — they are operator-algebra identities, not convergence claims (the `apply_nonlinear_pencil` cycle-021 / `chebyshev-smoother` cycle-012 no-dedicated-test precedent applies; the `eigsolve` rough-in framing does **not** bind, as `normalize`'s laws carry no literature-inferred semantics). The one semantic addition over the leaves — partiality at `x = 0` — is positively anchored by the L0 `MFEM_ASSERT`. The B-weighted sibling `normalize_B` is an in-chapter **rough-in note** (no fused Palace site + inherited `matrix-weighted-norm` test-coverage bound), not part of the firm claim.

## L1 vs L0 distinction

- **L0**: mutating free-function template `linalg::Normalize(comm, x)` (`palace/linalg/vector.hpp:262-270`). Computes `norm = Norml2(comm, x)`, asserts `norm > 0`, rescales the receiver in place `x *= 1.0/norm`, returns `norm` by value. Three consuming shapes inline the norm (Arnoldi Hessenberg `palace/linalg/iterative.cpp:631-632`, power-iteration eigenvalue estimate `palace/linalg/operator.cpp:661` and `:673`, NEP deflation companion-scale `palace/linalg/nleps.cpp:610-611,617`). The MPI collective is folded inside `Norml2`'s inner `Dot`.
- **L1**: pure functional `(β, û) = normalize(x)`. No destination buffer, no communicator, no in-place mutation. The returned norm is a first-class result component (not a side output). The in-place rescale, the reciprocal-vs-divide trick, the `MPI_Allreduce`, and the receiver overwrite are all L1>L0 lowering concerns — the lowering composes [`nrm2-mutation-rotation`](../L1-L0/nrm2-mutation-rotation.md) (no-buffer reduction) with [`scal-mutation-rotation`](../L1-L0/scal-mutation-rotation.md) sub-pattern A (in-place rescale) plus a returned-scalar binding. The full L1>L0 rotation is the firm theme [`normalize-mutation-rotation`](../L1-L0/normalize-mutation-rotation.md) (authored cycle-027).

## Evidence

- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template: `auto norm = Norml2(comm, x); MFEM_ASSERT(norm > 0.0, "Zero vector norm in normalization!"); x *= 1.0 / norm; return norm;`. The positive source site — `normalize` verbatim, returning the norm. The rescale is line 268; the assert (partiality precondition) line 267; the `return norm` line 269. **Self-verified** (`citecheck --anchor 'Normalize'` → line 264 def; `--anchor 'return norm'` → 269; `--anchor '1.0 / norm'` → 268).
- `palace/linalg/iterative.cpp:631-632` — GMRES Arnoldi: `Hj[j + 1] = linalg::Norml2(comm, w); w *= 1.0 / Hj[j + 1];` — the returned norm stored as the Hessenberg sub-diagonal entry AND used to normalize. The inline (un-fused) form of `normalize` with both outputs consumed. **Self-verified** (`--anchor 'Hj[j + 1] = linalg::Norml2'` → 631; `--anchor '1.0 / Hj'` → 632).
- `palace/linalg/iterative.cpp:811` — second analogous GMRES Arnoldi code path, identical `w *= 1.0 / Hj[j + 1];`. **Self-verified** (`--anchor 'Hj'` → 811).
- `palace/linalg/operator.cpp:660-661` — `SetRandom(comm, u); Normalize(comm, u);` — power-iteration initial normalisation (returned norm discarded on the seed). **Self-verified** (`--anchor 'SetRandom(comm, u)'` → 660).
- `palace/linalg/operator.cpp:673` — `l = Normalize(comm, u);` — the returned norm `l` IS the dominant-eigenvalue estimate, consumed by the convergence test. **Self-verified** (`--anchor 'l = Normalize'` → 673).
- `palace/linalg/operator.cpp:676` — `res = std::abs(l - l0) / l0;` — the convergence test consuming the returned norm `l` from `:673`. Direct evidence the returned scalar is load-bearing. **Self-verified** (`--anchor 'res = std::abs(l - l0)'` → 676).
- `palace/linalg/nleps.cpp:610-611` — NEP deflation-basis growth: `const auto scale = linalg::Norml2(GetComm(), v); v *= 1.0 / scale;` — inline unweighted normalise. **Self-verified** (`--anchor 'Norml2(GetComm(), v)'` → 610; `--anchor '1.0 / scale'` → 611).
- `palace/linalg/nleps.cpp:617` — `H.col(k).head(k) = v2 / scale;` — the returned norm `scale` reused to rescale the coordinate companion `v2`. Doubly-load-bearing returned-norm. **Self-verified** (`--anchor 'v2 / scale'` → 617).
- `palace/linalg/operator.cpp:600-607` — B-weighted `Norml2(comm, x, B, Bx)` (the `matrix-weighted-norm` reduction): `B.Mult(x, Bx); double dot = Dot(comm, Bx, x); ...; return std::sqrt(dot);`. Evidence the B-weighted *reduction* exists but is **not** fused into a `Normalize`-with-`B` (no rescale). **Self-verified** (`--anchor 'B.Mult(x, Bx)'` → 602).
- L1 anchors: `book/src/L1/nrm2.md` (firm; `β = √⟨x,x⟩`, real-valued output), `book/src/L1/scal.md` (firm; `û = scal(1/β, x)`, law 8 round-trip), `book/src/L1/matrix-weighted-norm.md` (rough-in; the `normalize_B` norm constituent), `book/src/L1-L0/scal-mutation-rotation.md:48-49,141-147` (sub-pattern A names the `Normalize` rescale + defers this decision to this OQ).

Test evidence (L0-equivalent semantic documentation):
- `palace/test/unit/test-orthog.cpp:193,208` — `V[0] *= 1 / v0_norm;` / `V[1] *= 1 / v1_norm;` on real `Vector`s, each immediately after a `CHECK_THAT(v*_norm, ...)` assertion on the norm. The textbook by-hand `normalize` (norm asserted, then rescale) on the real path — empirical-match for the fused operator's two-output shape (cited via `scal-mutation-rotation.md:183-186`, inherited).
