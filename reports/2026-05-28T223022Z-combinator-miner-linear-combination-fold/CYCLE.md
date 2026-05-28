---
agent: combinator-miner
invoked_at: 2026-05-28T223022Z
scope: Pattern proposal — BLAS-1 variadic linear-combination fold (linear_combination at L2)
status: integrated
integrated_at: 2026-05-28T230323Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  Applied cycle-017 (per-report position 1). Landed the NEW L2 rough-in dep-map
  row for linear_combination at book/src/L2/index.md — the constructive prong (b)
  of the human-raised OQ blas1-variadic-linear-combination-fold-unification. L2
  rough-in cohort 0->1. BUILD-REPAIR by integrator-finalize: the dep-map row's
  live markdown link to the not-yet-authored ./linear_combination.md chapter
  failed mdbook-linkcheck2 (File not found); de-linked to a plain-text
  forward-reference (cycle-015 fem-bilinearform-file no-dead-link convention).
  2 OQs opened (linear-combination-harvester-formalization,
  inner-product-fold-sibling-candidate). The human-raised parent OQ prong-(a)
  (combinator-miner parametric-family-detection-mode spec extension) remains a
  batch-4 meta-phase item.
---

# CYCLE: Combinator candidate — linear-combination-fold

## Summary

Palace's four BLAS-1 "scalar-weighted vector sum" operators — `scal`, `axpy`, `axpby`, `axpbypcz` — are **fixed-arity specializations of a single variadic fold** over a list of (scalar, tensor) terms. They are NOT a literally-recurrent code shape (each is a distinct C++ symbol with its own overload set), so the combinator-miner's default `≥3 instances of an identical shape` heuristic is arity-blind to them — exactly the documented root cause in OQ `blas1-variadic-linear-combination-fold-unification` (HUMAN-RAISED, post-cycle-016). Working in explicit **parametric-family mode**, I treat operators that differ only in arity (the number of (scalar, tensor) terms) as instances of one combinator: `linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]`, semantically `foldl (\acc (a,t) -> acc + a*t) zeros pairs`. The four L1 ops are the arity-1/2/2/3 cases. I propose `linear_combination` as an **L2 (fusion-rotation) combinator** — it is the form into which Palace's distinct fixed-arity call shapes (`AXPY`/`AXPBY`/`AXPBYPCZ`/`operator*=`) dissolve, with the single aligned in-place pass being a transparent fusion implementation of the fold, not load-bearing. The four L1 fixed-arity leaves correctly stay (they mirror Palace's distinct C++ symbols, load-bearing for the L1>L0 mutation rotation). I add a rough-in dep-map row to `book/src/L2/index.md`; harvester will formalize. The sibling `dot` is a *different* fold (reduce-to-scalar inner product) and stays its own thing — explicitly out of scope here, noted as a follow-up `inner_product` candidate.

## Pattern instances

The family is a **parametric arity family**, so instances are counted two ways: (A) the four fixed-arity operator definitions, and (B) representative live L0 call sites grounding each arity. Both far exceed the ≥3 soft bar.

### (A) The four fixed-arity operator definitions (the family members)

- **Instance 1 — `scal` (arity 1)**: `book/src/L1/scal.md:15-18` — `scal :: (α, x) -> Tensor[N]; scal(α,x)=α·x`. L0 home: `ComplexVector::operator*=(std::complex<double>)` at `palace/linalg/vector.cpp:203-227` (member-only; no free function — verified `linalg::Scal`/`linalg::Scale` return zero hits).
- **Instance 2 — `axpy` (arity 2, one coeff fixed to 1)**: `book/src/L1/axpy.md:15-18` — `axpy(α,x,y)=α·x+y`. L0 home: free-function template `AXPY` at `palace/linalg/vector.hpp:305-307`; real-real definition `palace/linalg/vector.cpp:702-712` (with the `α == 1.0` fast path).
- **Instance 3 — `axpby` (arity 2)**: `book/src/L1/axpby.md:15-18` — `axpby(α,x,β,y)=α·x+β·y`. L0 home: free-function template `AXPBY` at `palace/linalg/vector.hpp:309-311`; real-real definition `palace/linalg/vector.cpp:726-730` delegating to MFEM `add(α,x,β,y,y)` (the single aligned fusion pass).
- **Instance 4 — `axpbypcz` (arity 3)**: `book/src/L1/axpbypcz.md:15-18` — `axpbypcz(α,x,β,y,γ,z)=α·x+β·y+γ·z`. L0 home: free-function template `AXPBYPCZ` at `palace/linalg/vector.hpp:313-316`; real-real definition `palace/linalg/vector.cpp:745-758` (single fused `add(α,x,β,y,z)` pass under `γ==0`).

The L0 subsumption chain `AXPBYPCZ(…,γ=0,…) → AXPBY → (β=1) AXPY` is exhibited *in the source itself*: `vector.cpp:749-751` branches `if (gamma == 0.0) add(alpha, x, beta, y, z);` — the arity-3 op collapsing to the arity-2 fold when its third coefficient is zero. This is direct source evidence that the family IS one fold parameterized by arity.

### (B) Representative live L0 call sites (arity-family in the wild)

- **arity-3 (`axpbypcz`) accumulation, γ=1 (fold-into-output)**: `palace/linalg/nleps.cpp:343-344` — `linalg::AXPBYPCZ(y(j).real(), X[j].Real(), -y(j).imag(), X[j].Imag(), 1.0, z.Real())` (and `.imag()` line). The `γ=1` form `z ← α·x + β·y + 1·z` is literally `foldl` accumulating two more terms into the running sum `z` — the clearest in-the-wild evidence of the fold shape with output aliasing.
- **arity-3 accumulation, γ=1**: `palace/models/romoperator.cpp:188-189` — `linalg::AXPBYPCZ(y(j).real(), V[j], y(j+1).real(), V[j+1], 1.0, u.Real())` (ROM solution reconstruction; same accumulate-two-terms-into-output shape).
- **arity-3, γ=0 (pure two-term combination)**: `palace/models/timeoperator.cpp:217` — `linalg::AXPBYPCZ(1.0, RHS2, dt, k1, 0.0, k2)` (RK time-integrator stage; `k2 ← RHS2 + dt·k1`, the γ=0 collapse to `axpby`).
- **arity-3 member-form, eigensolver**: `palace/linalg/arpack.cpp:772, 787` and `palace/linalg/slepc.cpp:1986` — `*.AXPBYPCZ(…, 0.0)` shift-invert combinations.
- **arity-2 (`axpy`) accumulation**: `palace/linalg/operator.cpp:458-466` — `y.Add(a*c, z)` accumulating scaled operator outputs in `SumOperator::AddMult` (per axpy.md:81); `palace/linalg/rap.cpp:73, 317`.
- **arity-1 (`scal`)**: `palace/linalg/iterative.cpp:632, 811` — GMRES Arnoldi basis-normalization `w *= 1.0 / Hj[j+1]`; `palace/linalg/vector.hpp:262-270` (`Normalize` = fused `nrm2 + scal`).

(All ranges in this report self-verified via codemap `read_range` / `search_text` — see Supporting evidence.)

## Proposed combinator

- **Slug**: `linear-combination` (file `linear_combination`)

- **Layer**: **L2** (fusion-rotation layer).

  Rationale — why L2, not adjacent layers:

  - **Not L1.** L1 must mirror Palace's distinct L0 C++ symbols one-to-one (`AXPY` / `AXPBY` / `AXPBYPCZ` / `operator*=`), because the L1>L0 mutation rotation rewrites *each fixed-arity symbol* into its receiver-mutating / output-arg idiom. The fixed-arity L1 leaves are load-bearing for that rotation; the `axpby-as-primitive` decision (`scaffolding/decisions/axpby-as-primitive.md`) correctly keeps them as leaves. `linear_combination` is the form they fuse *up* into, not a replacement for them.
  - **L2 is exactly the fusion-rotation layer** (`book/src/L2/index.md:1-18`): "each operation written as composition of base tensor primitives, with HPC/SIMD optimization tricks unfolded back into the base algebras… Kernel fusion across multiple algebraic operations is unfolded into composition." Palace's distinct fixed-arity call shapes ARE a kernel-fusion choice (one aligned pass over the operands); unfolding them into the canonical multi-term fold is precisely the L2 rotation. The L2 index even lists `axpy, axpby, scal` in its overlay vocabulary (`:17`) and states "This is the layer most populated by combinator-miner output" (`:28`).
  - **Not L4.** L4 is the graph-evaluation calculus of high-order combinators + state monads + immutable tensors (`iterate_while`, `solve-monad`). `linear_combination` is a **pure tensor-algebra fold** — a value-producing reduction over a term list with no control-flow, no monadic state threading, no convergence predicate. It is data-parallel, not iteration-structural. It belongs with the tensor algebra at L2, the same layer as `krylov-step`'s L1-primitive vocabulary, not with the control-flow combinators at L4. (Contrast `iterate_while`, which IS an L4 combinator because it threads state through a stopping predicate.)

- **Signature sketch** (best guess; harvester firms up):

  ```text
  linear_combination :: [(Scalar, Tensor[N])] -> Tensor[N]
  linear_combination pairs = foldl (\acc (a, t) -> acc + scal a t) (zeros N) pairs
  ```

  Specializations (the four L1 leaves as fixed-arity instances):

  ```text
  scal(α, x)                    = linear_combination [(α, x)]
  axpy(α, x, y)                 = linear_combination [(α, x), (1, y)]      -- one coeff fixed to 1
  axpby(α, x, β, y)             = linear_combination [(α, x), (β, y)]
  axpbypcz(α, x, β, y, γ, z)    = linear_combination [(α, x), (β, y), (γ, z)]
  ```

  Shape precondition: `all tᵢ : Tensor[N]` for one shared `N` — the "aligned fusion kernels" precondition (every term shares the length axis). Element type is one shared `T ∈ {real, complex}` across all terms and scalars, with the `real ⊑ complex` scalar promotion lattice inherited from `concepts/scalar-promotion` (all-or-none across the scalar list — `linear_combination` unifies the family along the *arity* axis exactly as `scalar-promotion` already unified it along the *element-type* axis).

- **Algebraic intuition**:

  - **Empty-list identity**: `linear_combination [] = zeros[N]` — the fold's seed; the additive identity of `Tensor[N]`.
  - **Concatenation law (the fold's defining homomorphism)**: `linear_combination (a ++ b) = linear_combination a + linear_combination b` (vector addition on the right). This is the law that makes the four arities one operator: `axpbypcz`'s 3-term list is the concatenation of an `axpby` 2-term list and a `scal` 1-term list. It directly generalizes the per-operator distribution laws already recorded (axpby.md laws 5-7; axpbypcz.md laws 7-10).
  - **Multilinearity in the scalar list**: linear separately in each `aᵢ` with all other terms held fixed; `linear_combination ((a₁+a₂, t):rest) = a₁·t + a₂·t + linear_combination rest`. This is the variadic generalization of axpby.md law 5 (bilinearity in `(α,β)`) and axpbypcz.md law 7 (trilinearity in `(α,β,γ)`).
  - **Coefficient-scaling / scalar absorption**: `linear_combination ((κ·a, t):rest) = linear_combination ((a, κ·t):rest)` — each scalar absorbs into its paired tensor (generalizes scal.md law 4, axpby.md law 8, axpbypcz.md law 11).
  - **Term-with-zero-coefficient drop**: `linear_combination ((0, t):rest) = linear_combination rest` — generalizes the per-op identity laws (axpby.md laws 2-3, axpbypcz.md laws 3-5) and is the *exact algebraic content of the L0 `γ==0` branch* at `vector.cpp:749-751`.
  - **Permutation-invariance — EXACT-ARITHMETIC ONLY (IEEE caveat)**: in exact arithmetic, `linear_combination` is invariant under permutation of the term list (addition is commutative + associative). **In IEEE-754 it is NOT** — the summation order is a load-bearing numerical concern per CLAUDE.md (different reduction orderings give different bit-level results). The per-op entries already record this as an explicit non-law (axpby.md "Floating-point associativity"; axpbypcz.md notes the two L0 branches `add(…)` fused vs `AXPBY(…); z.Add(…)` split do NOT match each other bit-for-bit). So permutation-invariance is stated as an exact-arithmetic law with an explicit "bit-identical reproduction of an L0 site requires matching that site's summation order" caveat. The fold's `foldl` left-to-right order is the *canonical* order the L2 form names; L2>L1 lowering records which L0 fusion order a given call pins.

- **Variant axes** (for harvester; orthogonal to arity):

  1. **Output aliasing (in-place vs out-of-place)** — the in-place mutation forms (`y ← α·x + β·y`, `z ← …+ γ·z`) are the case where one term's tensor `tᵢ` **aliases the output buffer**. This is orthogonal to arity: every arity ≥ 1 has both an aliasing form (member `operator*=`/`AXPY`/`AXPBY`/`AXPBYPCZ` writing through the receiver) and a fresh-output form. The `γ=1` accumulation call sites (`nleps.cpp:343-344`, `romoperator.cpp:188-189`) are the aliasing case where the aliased term's coefficient is 1 (accumulate-into). At L2 the fold is pure / out-of-place; aliasing is an L2>L1 (and onward L1>L0) lowering concern, NOT an arity axis.
  2. **Element-type** — `real | complex`, with the `real ⊑ complex` scalar-promotion sub-axis (`concepts/scalar-promotion`). Already unified across the family along this axis; `linear_combination` inherits it unchanged.
  3. **Fusion order (L0 implementation detail)** — single aligned pass (`add(α,x,β,y,z)`) vs multi-call split (`AXPBY(…); z.Add(…)`); transparent for value, load-bearing for bit-reproduction. NOT an L2 variant axis — it's the L2>L1>L0 realization of the fold's seed-and-accumulate.

## Proposed changes

```edit:book/src/L2/index.md
| [`linear_combination`](./linear_combination.md) | `[(Scalar, Tensor[N])] -> Tensor[N]` (≡ `foldl (\acc (a,t) -> acc + a·t) zeros pairs`) | L1 fixed-arity specializations: `scal` (arity 1), `axpy` (arity 2, coeff 1 fixed), `axpby` (arity 2), `axpbypcz` (arity 3). Concepts: `scalar-promotion` (element-type axis, already-unified sibling of this arity-axis unification). Sibling fold (do NOT merge): `dot` (reduce-to-scalar inner product). | `(rough-in, proposed-by: combinator-miner:2026-05-28T223022Z)` |
```

Append the row to the L2 operator dep-map table (after the `chebyshev-iteration` row at `book/src/L2/index.md:24`).

Note: this report does **not** create `book/src/L2/linear_combination.md`. That is harvester's job (formalization). Combinator-miner only adds the dep-map rough-in row.

Suggested companion (integrator may apply or defer to harvester): the L2 "Working Notes" section could gain a provenance bullet mirroring the `krylov-step` precedent (`book/src/L2/index.md:30-37`):
- **Pattern provenance** (combinator-miner:2026-05-28T223022Z): arity-family unification of the BLAS-1 scalar-weighted-sum cohort. Specializations: `scal`/`axpy`/`axpby`/`axpbypcz`. Distinct from the inner-product fold `dot` (out of scope; follow-up `inner_product` candidate). Closes the constructive half of OQ `blas1-variadic-linear-combination-fold-unification`.

## Supporting evidence

All Palace ranges self-verified via codemap `read_range` / `search_text` this invocation:

- `palace/linalg/vector.hpp:305-307` — `AXPY` free-function template decl. **Verified** (`read_range`): `template <typename VecType, typename ScalarType> void AXPY(ScalarType alpha, const VecType &x, VecType &y);` with comment `Addition y += alpha * x.`
- `palace/linalg/vector.hpp:309-311` — `AXPBY` template decl. **Verified**: comment `Addition y = alpha * x + beta * y.`
- `palace/linalg/vector.hpp:313-316` — `AXPBYPCZ` template decl. **Verified**: comment `Addition z = alpha * x + beta * y + gamma * z.`
- `palace/linalg/vector.cpp:702-712` — `AXPY(double, Vector, Vector)` with `if (alpha == 1.0) y += x; else y.Add(alpha, x);`. **Verified** (exact match to axpy.md:80).
- `palace/linalg/vector.cpp:715-723` — `AXPY` complex overloads (real-promoted + complex), both `y.AXPY(alpha, x)`. **Verified**.
- `palace/linalg/vector.cpp:726-730` — `AXPBY(double,…)` → `add(alpha, x, beta, y, y)` (single aligned MFEM fusion pass). **Verified** (exact match to axpby.md:92).
- `palace/linalg/vector.cpp:732-743` — `AXPBY` complex + real-promoted overloads → member `y.AXPBY(alpha, x, beta)`. **Verified**.
- `palace/linalg/vector.cpp:745-758` — `AXPBYPCZ(double,…)` with `if (gamma == 0.0) add(alpha, x, beta, y, z); else { AXPBY(alpha, x, gamma, z); z.Add(beta, y); }`. **Verified** (exact match to axpbypcz.md:111; this is the in-source arity-collapse evidence).
- `palace/linalg/vector.cpp:760-772` — `AXPBYPCZ` complex + real-promoted overloads → member `z.AXPBYPCZ(…)`. **Verified**.
- `palace/linalg/vector.cpp:203-227` — `ComplexVector::operator*=(std::complex<double>)` (the `scal` site) with `if (si == 0.0)` real fast-path branch. **Verified** (exact match to scal.md:90, scalar-promotion.md:22).
- `palace/linalg/vector.hpp:96-136` — `ComplexVector` member decls: `operator*=` (`:98-99`), `Dot`/`TransposeDot` (`:110-112`), `AXPY`/`Add`/`Subtract` (`:115-118`), `AXPBY` (`:130-131`), `AXPBYPCZ` (`:133-136`). **Verified** with matching mutation comments.
- **No `linalg::Scal`/`linalg::Scale`** — `search_text` `linalg::(Scal|Scale)\b` → **zero hits** (confirms scal.md:7's "notable absence" claim; `scal` is member-`operator*=`-only).
- `linalg::AXPBYPCZ(` / `*.AXPBYPCZ(` live call sites — `search_text` returned 20 hits across `nleps.cpp:343-344,471,676,693`, `arpack.cpp:772,787`, `slepc.cpp:1986`, `timeoperator.cpp:139,217,273`, `romoperator.cpp:188-189`, plus the `vector.cpp` defs. **Verified** — the arity-3 member is heavily used in eigensolvers + time integrators, grounding the family as live (not vestigial).

Artifact citations (read this invocation):
- `book/src/L1/scal.md`, `book/src/L1/axpy.md`, `book/src/L1/axpby.md`, `book/src/L1/axpbypcz.md` — the four fixed-arity leaves (signatures, laws, variant axes).
- `book/src/L1/dot.md` — the sibling fold (distinct; see Open questions).
- `book/src/concepts/scalar-promotion.md` — the already-existing element-type-axis unification of the same four ops (the precedent for an arity-axis unification).
- `scaffolding/decisions/axpby-as-primitive.md` — the fused-leaf decision; its "What would change the decision" (`:49-52`) does NOT preclude an L2 fold (it only governs L1 leaf-vs-decompose).
- `book/src/L2/index.md` — L2 layer charter + dep-map (rough-in row target); `krylov-step` provenance-bullet precedent (`:30-37`).
- `scaffolding/open-questions.md:2937-2946` — OQ `blas1-variadic-linear-combination-fold-unification` (HUMAN-RAISED), the root-cause analysis this dispatch enacts the constructive half (b) of.

Tests exercising the pattern (L0-equivalent, per `find-tests-for-region`): `test/unit/test-vector.cpp` (axpy/axpby/axpbypcz value checks — cited transitively via the L1 entries' evidence; not re-read this invocation, flagged as a harvester follow-up to cite per-arity test assertions for the empirical-match of the concatenation law).

## Open questions / caveats

1. **`dot` is a DIFFERENT fold — recommend it stays its own thing (do NOT over-unify).** `dot :: (x, y) -> Scalar` is `foldl (+) 0 (zipWith (*) x y)` (or `conj`-weighted for the Hermitian complex case) — a *reduce-to-scalar* inner-product fold, NOT a scalar-weighted *tensor* sum. Its result type is `Scalar`, not `Tensor[N]`; its laws are symmetry / Hermitian-symmetry / positive-semi-definiteness (dot.md:55-75), which have no analogue in `linear_combination`. The target is a small **algebra of folds** — a tensor-producing linear-combination fold AND a scalar-producing inner-product fold — not one mega-combinator. **Follow-up candidate (OUT of scope for this one-pattern proposal):** a sibling `inner_product :: (Tensor[N], Tensor[N]) -> Scalar` L2 fold capturing `dot`/`tdot` as conjugation-convention variants. I deliberately do NOT propose it here (one pattern per invocation); a future combinator-miner invocation should mine it as a separate parametric family (the axis there is conjugation-convention, not arity). Filed against OQ `blas1-variadic-linear-combination-fold-unification`'s "algebra of folds, not one mega-combinator" nuance.

2. **L2>L1 lowering theme is needed but is abstractor work, not mine.** Once harvester formalizes `linear_combination` at L2, an `L2-L1/linear-combination-fold-specialization` theme should narrate how the variadic L2 fold lowers into the fixed-arity L1 leaves (the arity-dispatch: list-length 1 → `scal`, 2 → `axpy`/`axpby`, 3 → `axpbypcz`; longer lists → left-fold of `axpby`/`axpbypcz` chains). The fold's left-to-right summation order vs the L0 pinned orders (single fused pass vs split-call) is the load-bearing numerical content of that theme. Not authored here.

3. **Unbounded-arity beyond 3.** Palace's L0 surface stops at arity 3 (`AXPBYPCZ`) — there is no `AXPBYPCZPDW`. The `γ=1` accumulation call sites (`nleps.cpp:343-344`, `romoperator.cpp:188-189`) show arity-> 3 combinations realized as *iterated* `axpbypcz`-into-output (a fold over a loop, accumulating ≤3 terms per step). So the **variadic** `linear_combination` is genuinely more general than any single Palace symbol — it is the L2 abstraction that the bounded-arity L0 family approximates. This is the correct direction (per CLAUDE.md "literature-anchored L1 form may inform higher abstractions / extensions Palace hasn't implemented"): the variadic form may later let an L4 combinator express n-term basis-reconstruction (ROM/eigenvector synthesis) directly, which Palace open-codes as accumulation loops. Flagged as upside, not scope creep.

4. **Permutation-invariance phrasing for harvester.** I recommend harvester state permutation-invariance as an explicit **exact-arithmetic law** with the IEEE non-associativity caveat as a paired explicit non-law (matching the established pattern in axpby.md:59 and axpbypcz.md:76). The fold's `foldl` order is the canonical naming order; bit-identical reproduction of any L0 call requires the L2>L1 theme to record that call's pinned order. Do NOT assert unqualified permutation-invariance.

5. **Self-verify note.** The `test/unit/test-vector.cpp` per-arity value-check assertions were not re-read this invocation (cited transitively via the L1 entries). Harvester should pull the concrete assertions to anchor the concatenation law as an `empirical_match` rather than a purely algebraic claim (per `feedback_tests_as_semantic_supplement`).
