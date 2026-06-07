---
layer: L4
operator: gram_reduce
firmness: firm
rank: firm
edges:
  depends-on:
    - L1/matrix-weighted-norm
    - L1/bilinear-form
    - L4/solve_family
  reference:
    - L4/inner_product
    - L4/linear_combination
variant_axes:
  - normalization-weight (unit | current-normalized — THE load-bearing axis; absorbed into the w closure)
  - operator-source (mass-energy — absorbed into K)
  - element-type (real — pinned for the two witnessed pipelines)
  - family-index-domain (terminal-boundary | surface-current — absorbed into [Tensor] / w)
---

# gram_reduce

The L4 **operator-weighted symmetric-Gram reduction combinator**: reduce a collected
solution family `[xᵢ]` against an operator weight `K` into the symmetric Gram matrix
`Gᵢⱼ = w(i,j) · (xⱼᵀ K xᵢ)`, parameterized by the per-entry normalization weight
`w(i,j)`. It is the **output-product reduction** shared by the electrostatic
capacitance matrix (`Cᵢⱼ = Vⱼᵀ K Vᵢ`, `w = 1`) and the magnetostatic inductance
matrix (`Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)`, `w = 1/(Iᵢ Iⱼ)`) — ONE symmetric-Gram reduction
across the two output products; the **weight is the only difference**.

`gram_reduce` is a **pure value-producing reduction** (no `Solve` monad, no carry, no
convergence predicate) — the **reduce-to-matrix** member of the L4 algebra-of-folds
family, the sibling of the reduce-to-scalar [`inner_product`](./inner_product.md) and
the reduce-to-tensor [`linear_combination`](./linear_combination.md). It rises to L4
as a **feature-surface verb the backend wants**
([`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
§"The combinators rise regardless"; directive-1: L4 is the outward backend-lowering
target) — the output-product half of the electrostatic + magnetostatic composition
roots reaches the L4 surface through it.

Per replace-and-propagate (CLAUDE.md §Methodology invariants VOCABULARY-SHIFT
redirect), `gram_reduce` is the **entry**; the electrostatic capacitance reduction and
the magnetostatic inductance reduction are **specialization notes re-expressing
THROUGH it** (§Specialization), NOT two rectangular leaf chapters. The two feature
columns ([`electrostatic`](../feature/electrostatic.L4.md),
[`magnetostatic`](../feature/magnetostatic.L4.md)) down-link to this combinator.

## Context

L4 is **vocabulary** (`L4/index.md:7-13`). `gram_reduce` names the symmetric-Gram
reduction shape both energy-formulated output products share. It consumes the
collected solution family that [`solve_family`](./solve_family.md) produces (the
fixed-operator map's `[SimState.x]` output), folding each family-pair through the
operator-weighted bilinear primitives:

- the diagonal entry `xᵢᵀ K xᵢ` is the now-**firm** (c091) L1
  [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (`√` dropped — `gram_reduce`
  reduces to the *squared* energy `xᵢᵀ K xᵢ = 2Uₑ/ₘ(xᵢ)`, the matrix-weighted-norm's
  radicand);
- the off-diagonal entry `xⱼᵀ K xᵢ` is the now-**firm** (c095) L1
  [`bilinear-form`](../L1/bilinear-form.md) (`xᴴ M y` at `M = K`) — the last
  remaining folded gate, discharged by the cycle-095 firm-flip-and-cascade wave
  (see §Status).

The diagonal is the `xⱼ = xᵢ` specialization of the off-diagonal bilinear
(`matrix_weighted_norm x K = bilinear_form x K x` modulo the `√`), so
`matrix-weighted-norm` is the diagonal **consumer**, not a second fold — the do-NOT-merge
over-unification guard (the `nrm2`-consumes-`inner_product` pattern,
`concepts/black-box-vs-accelerated-kernels.md` §2).

The combinator is defined **in L4 vocabulary** (high→low discipline): its semantics,
signature, and laws are stated in terms of the L1 bilinear primitives it folds and the
[`solve_family`](./solve_family.md) family it consumes — NOT in terms of the L0 C++
double loop. It is a methodology-level combinator distilled from the two PostprocessTerminals
bodies; Palace's C++ writes the explicit double loop, not the L4 reduction form.

## Signature

```text
-- the operator-weighted symmetric-Gram reduction over a solution family-pair grid,
-- parameterized by the per-entry normalization weight w(i,j):
gram_reduce :: LinOp[(S: ...), $S]   -- the operator weight K (square SPD domain energy operator)
            -> [Tensor[$S]]           -- the solution family xs = [x_0 .. x_{m-1}] (congruent to K's domain S)
            -> (Int -> Int -> Scalar)       -- the per-entry normalization weight w(i,j)
            -> Matrix[m, m]                 -- the symmetric Gram matrix G, Gᵢⱼ = w(i,j) · (xⱼᵀ K xᵢ)
gram_reduce k xs w =
  symmetric_from_upper                                  -- mirror lower triangle from upper (G symmetric)
    [ [ w i j * entry k xs i j | j <- [i .. m-1] ]      -- map over upper-triangle pairs
      | i <- [0 .. m-1] ]
  where
    m              = length xs
    entry k xs i j
      | i == j     = matrix_weighted_norm (xs!!i) k     -- diagonal: xᵢᵀ K xᵢ   (L1 matrix-weighted-norm radicand)
      | otherwise  = bilinear_form (xs!!j) k (xs!!i)    -- off-diag: xⱼᵀ K xᵢ   (L1 bilinear-form)

-- the alternate Maxwell form is the inverse (a CONSUMER, not part of the reduction):
gram_inverse :: Matrix[m, m] -> Matrix[m, m]            -- = inv (LAPACK); the Cinv / Minv tail
```

Shape contract (bunsen-style; named shape groups per
[`l4_calculus`](../semantics/index.md) §1.2.1):

- `K : LinOp[(S: ...), $S]` — read-only; the **domain energy operator** (`M_elec`
  diffusion-energy at `electrostaticsolver.cpp:118`, `M_mag` curl-curl-energy at
  `magnetostaticsolver.cpp:129`; the feature chapters call it `K`). Symmetric/SPD —
  the load-bearing precondition for `G`-symmetry.
- `xs : [Tensor[(S: ...)]]` — the collected solution family (each congruent to `K`'s
  domain group `S` of arbitrary unknown rank; [`solve_family`](./solve_family.md)'s
  `[SimState.x]`): electrostatic `[Vᵢ]` (per-terminal), magnetostatic `[Aᵢ]`
  (per-surface-current). Read-only.
- `w : Int -> Int -> Scalar` — the per-entry normalization weight closure: electrostatic
  `w i j = 1` (voltage-formulated, unit excitation); magnetostatic `w i j = 1/(I!!i * I!!j)`
  (current-normalized, `I : [Scalar]` the excitation currents absorbed into the closure).
  Symmetric (`w i j = w j i`) for both witnesses — required for `G`-symmetry.
- result `Matrix[m, m]` — the symmetric Gram matrix (`m = length xs`).

The shape contract makes structural what is conventional in the C++ double loop:

1. **Each grid entry is independent (the upper-triangle `map` is a list homomorphism
   over pairs).** No state threads between entries; the reduction collects.
2. **`G` is symmetric by construction** (compute upper, mirror lower) — the C++
   lower-triangle-copy loops are the L4 `symmetric_from_upper`.

## Semantics

`gram_reduce K xs w` evaluates the operator-weighted bilinear form at each
upper-triangle family-pair, scales by the per-entry weight, and mirrors to a symmetric
matrix. The diagonal uses the self-bilinear ([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
radicand `xᵢᵀ K xᵢ`); the off-diagonal uses the cross-bilinear
([`bilinear-form`](../L1/bilinear-form.md) `xⱼᵀ K xᵢ`). It is a `map`-then-`reduce`
with no `Solve` effect — a pure function `(K, xs, w) -> Matrix[m, m]`.

The combinator's structural payoff: the electrostatic capacitance reduction and the
magnetostatic inductance reduction are the **same** reduction, differing **only** in
the `w` weight closure (`w ≡ 1` voltage vs `w = 1/(IᵢIⱼ)` current). The operator
(`M_elec`/`M_mag`) and the family (`[Vᵢ]`/`[Aᵢ]`) are leaf-content absorbed into the
`K` and `xs` arguments.

## Algebraic laws

Every law is a **syntactic identity on the fold structure**, read off the two positive
PostprocessTerminals loops.

1. **Symmetry** (load-bearing). `Gⱼᵢ = Gᵢⱼ` because `K` is symmetric/SPD and `w i j =
   w j i`. Licenses the compute-upper-triangle-then-mirror realization
   (`electrostaticsolver.cpp` lower-triangle copy; `magnetostaticsolver.cpp` likewise).
   The underlying identity: `bilinear_form xⱼ K xᵢ = bilinear_form xᵢ K xⱼ` for
   symmetric `K`.
2. **Diagonal-is-self-bilinear** (the do-NOT-merge structural identity). `entry K xs i
   i = matrix_weighted_norm (xs!!i) K = bilinear_form (xs!!i) K (xs!!i)` (modulo the
   `√` the norm takes and `gram_reduce` does not) — the diagonal is the `xⱼ = xᵢ`
   specialization of the off-diagonal, so `matrix-weighted-norm` is the diagonal
   *consumer*, NOT a separate fold.
3. **Weight factoring / bilinearity.** `w(i,j)` factors out of each entry; `xⱼᵀ K xᵢ`
   is bilinear in `(xᵢ, xⱼ)`. The voltage form `w ≡ 1` is the multiplicative-identity
   specialization on the weight axis.
4. **Grid-map independence.** Each entry depends only on `(K, xs!!i, xs!!j, w i j)`;
   the upper-triangle map carries no state — embarrassingly parallel over pairs.

Laws that explicitly **do not** hold:

- **The inverse is NOT part of the reduction.** `Cinv`/`Minv` (LAPACK `Invert()`,
  `electrostaticsolver.cpp:140` / `magnetostaticsolver.cpp:152`) is a downstream matrix
  map on the produced `G` (the `gram_inverse` consumer), kept OUT of the combinator —
  the `nrm2`-style consumer split.
- **No cross-output-product fusion.** Electrostatic and magnetostatic each call
  `gram_reduce` with their own `(K, xs, w)`; the combinator does not fuse the two
  output products (they are distinct simulations).

## Specialization

Per replace-and-propagate, `gram_reduce` is the **entry**; the two output-product
reductions re-express THROUGH it:

- **Electrostatic capacitance** (`electrostaticsolver.cpp:100-140`,
  `ElectrostaticSolver::PostprocessTerminals`). `gram_reduce M_elec V (\i j -> 1)` —
  the voltage-formulated unit-weight specialization. Diagonal `Cᵢᵢ = Vᵢᵀ K Vᵢ`
  (`:118-119`), off-diagonal `Cᵢⱼ = Vⱼᵀ K Vᵢ` (`:126`), symmetric mirror, then
  `gram_inverse` → `Cinv` (`:139-140`). Weight `w = 1` (unit voltage excitation: `/Vᵢ² ≡ ×1`).
- **Magnetostatic inductance** (`magnetostaticsolver.cpp:110-152`,
  `MagnetostaticSolver::PostprocessTerminals`). `gram_reduce M_mag A (\i j -> 1/(I!!i * I!!j))`
  — the current-normalized specialization. Diagonal `Mᵢᵢ = (Aᵢᵀ K Aᵢ)/Iᵢ²`
  (`:129-131`), off-diagonal `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` (`:138`), symmetric mirror,
  then `gram_inverse` → `Minv` (`:151-152`). Weight `w = 1/(Iᵢ Iⱼ)` (current-normalized).

Candidate 3rd+ witnesses — PROBED c074 D6, both NON-MATCH (the symmetric-Gram subsume
is correctly REFUSED): (i) eigenmode Q-factor / energy post-processing is a per-mode
SCALAR-RATIO map (`Q_mj = ω_m/κ_mj`, `κ_mj = ½R_jI_mj²/E_m`,
`eigensolver.cpp:424-471` + `postoperator.cpp:1174-1217`) — no family-PAIR grid, the
wrong rank for a Gram reduction; (ii) driven S-parameters are a per-column port-mode
LINEAR PROJECTION (`Sᵢⱼ = sᵢ·E`, `lumpedportoperator.cpp:283-294`) assembled one
drive-column per solve with an inhomogeneous diagonal self-term (`-1`), directional
generalized-S scaling, and per-endpoint de-embedding (`postoperator.cpp:1246-1308`) —
NOT symmetric-Gram (no `symmetric_from_upper`; S-symmetry is reciprocity physics, not a
construction). `gram_reduce` stays the 2-pipeline energy-output-product reduction; the
eigenfreq/Q and S-parameter output-product columns author their OWN reduction verbs.
See OQ `gram-reduce-third-witness-probe-eigenmode-driven-postprocess` (CLOSED-NEGATIVE).

## Dependencies

L1 rows this combinator folds:

- [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (firm c091) — the diagonal
  self-bilinear (radicand); the diagonal consumer.
- [`bilinear-form`](../L1/bilinear-form.md) (firm c095) — the off-diagonal cross-bilinear;
  the fold element. **Promoted rough-in→firm by the cycle-095 firm-flip-and-cascade wave (the last folded gate discharged).**

L4 rows:

- [`solve_family`](./solve_family.md) (firm) — produces the
  solution family `[xᵢ]` this combinator reduces over (the upstream composition-root stage).

Sibling data-algebra combinators (the L4 algebra-of-folds family):

- [`inner_product`](./inner_product.md) (reduce-to-scalar) — `gram_reduce`'s off-diagonal
  entry `xⱼᵀ K xᵢ` is an `inner_product_M`-shaped weighted bilinear at the single-pair
  level; `gram_reduce` is the *grid* reduction over the family-pair matrix of them.
- [`linear_combination`](./linear_combination.md) (reduce-to-tensor) — the tensor-producing
  fold sibling.

## Lowers to

`gram_reduce` lowers by **identity-in-form on the body** to the L1 bilinear-form
evaluations it folds (the reduction is a plain fold of `matrix-weighted-norm` /
`bilinear-form` over the family-pair grid — there is no intervening L3/L2 absorption
that reshapes the fold). No dedicated L4>L3 theme file — the in-line-marker route (the
[`inner_product`](./inner_product.md) / [`linear_combination`](./linear_combination.md)
pattern); the substantive downward content (the C++ double loop, the symmetric mirror,
the workspace `D_gf`/`H_gf`, the LAPACK inverse) lives in the L1 primitives' own
L1>L0 mutation rotations. This entry records the rotation direction in-line per
high→low discipline; it does not author a theme.

## Status

`firm` (promoted from `rough-in (test-coverage-bounded)` at **cycle-095**, the
`bilinear-form-firm-flip-and-cascade-wave` D3, on the **firm-on-positive-structure
escape**). **Reasoning (warrant-first):** the combinator's **structure** is
firm-on-positive-structure — the symmetric-Gram skeleton
(map-over-upper-triangle-pairs, diagonal/off-diagonal split, weight factoring,
symmetric mirror, inverse-as-consumer) is read directly off the two skeleton-identical
positive PostprocessTerminals loops (electrostatic `:100-140` + magnetostatic
`:110-152`), and every law (§Algebraic laws) is a syntactic identity on that fold.
After the cycle-091 + cycle-095 cascade, **both** folded gates are now discharged:

1. the diagonal building block [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
   is **firm** (c091, the batch-29 firm-flip-and-cascade wave — both norm-axiom
   law-sides discharged on the firm-on-positive-structure escape) — **gate discharged**;
2. the off-diagonal building block [`bilinear-form`](../L1/bilinear-form.md) is now
   **firm** (c095, this cascade wave's D1 — promoted on the firm-on-positive-structure
   escape, firmability DISCHARGED by the cycle-092 `lowering-verifier` probe) — **the
   last residual gate, now discharged**;
3. the absence of a dedicated Palace unit test for the Gram reduction (the
   PostprocessTerminals bodies are integration-level, exercised only through the full
   `Solve(mesh)` driver) is **REDUNDANT** under the firm-on-positive-structure escape:
   every reduction-level law is a syntactic identity on the fold over two now-firm
   primitives (no theorem-needing-proof; the assembly is bare grid-fold arithmetic over
   firm halves with no inner-product-axiom content) — there is NO law for which that
   absent test is the only evidence.

A reduction is as firm as its least-firm folded primitive, and after the cascade BOTH
folded primitives are firm, so `gram_reduce` promotes to **firm** — the materially
identical disposition to its four reduce-verb siblings on the same escape: the
per-DOMAIN [`domain_energy_reduce`](./domain_energy_reduce.md) (firmed cycle-091 in
this same cascade family, because BOTH its primitives — matrix-weighted-norm c091 +
participation_ratio c077 — firmed), [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md)
(c082), [`sparameter_reduce`](./sparameter_reduce.md) (c083), and
[`solve_family`](./solve_family.md) (c086). This is NOT a forcing: the structure was
already firm-on-positive-structure on disk, and the only thing that held the verb at
`rough-in (test-coverage-bounded)` was the least-firm-folded-primitive inheritance
rule — which the c095 bilinear-form flip clears.

**Scope: 2-of-N pipelines** — electrostatic + magnetostatic output products (the two
energy-formulated symmetric-Gram reductions); eigenmode + driven post-processing are
candidate 3rd+ witnesses for a stronger future mine (§Specialization), not in scope
now. The disciplined-cross-pipeline-combinator-mining-gate is 2-of-N met (2 positive
witnesses, no break-witness — the normalization weight is a variant axis). The firm
flip is a law-confidence judgment, NOT a witness-count change: scope is unchanged.

## Evidence

All L0 citations self-verified on-disk this dispatch via the codemap
(`mcp__palace-codemap__read_range` + `search_text` line pinpoints against
`reference/palace/palace/drivers/{electrostatic,magnetostatic}solver.cpp`).

- **Electrostatic capacitance Gram (positive witness 1):**
  `palace/drivers/electrostaticsolver.cpp:95` (the `PostprocessTerminals(post_op,
  laplace_op.GetSources(), V)` call), `:100` (`void
  ElectrostaticSolver::PostprocessTerminals(...)` def), `:118`
  (`M_elec->Mult(V_gf, D_gf)` — the `K·Vᵢ` apply), `:119` (`linalg::Dot<Vector>(comm,
  V_gf, D_gf)` — diagonal `Vᵢᵀ K Vᵢ`), `:126` (off-diagonal `Vⱼᵀ K Vᵢ`), `:139-140`
  (`mfem::DenseMatrix Cinv(C); Cinv.Invert()` — the `gram_inverse` consumer).
- **Magnetostatic inductance Gram (positive witness 2):**
  `palace/drivers/magnetostaticsolver.cpp:105` (the `PostprocessTerminals(post_op,
  curlcurl_op.GetSurfaceCurrentOp(), A, I_inc)` call), `:110` (`void
  MagnetostaticSolver::PostprocessTerminals(...)` def), `:129`
  (`M_mag->Mult(A_gf, H_gf)` — the `K·Aᵢ` apply), `:131` (`linalg::Dot<Vector>(...) /
  (I_inc[i] * I_inc[i])` — diagonal `(Aᵢᵀ K Aᵢ)/Iᵢ²`), `:138` (off-diagonal
  `(Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)`), `:151-152` (`mfem::DenseMatrix Minv(M); Minv.Invert()`).
- **Feature-chapter witnesses (the §reduction stages that flagged the mine):**
  `book/src/feature/electrostatic.L4.md:40`, `book/src/feature/magnetostatic.L4.md:40`.
- **Firm vocabulary grounding:** `book/src/L4/inner_product.md` (the reduce-to-scalar
  sibling), `book/src/L4/linear_combination.md` (the reduce-to-tensor sibling),
  `book/src/concepts/black-box-vs-accelerated-kernels.md` §"The combinators rise
  regardless" (the L4-feature-surface-verb warrant).
- **No dedicated test** exercises the Gram reduction (the PostprocessTerminals bodies
  are integration-level under `Solve(mesh)`, not unit-tested under
  `reference/palace/test/unit/`) — the test-coverage-bounded gate.
- **Provenance:** harvested cycle-073 D1 (LEAD) from the feature-chapter forward-mine
  flags (`electrostatic.L4.md:40` + `magnetostatic.L4.md:40`); the
  disciplined-cross-pipeline-combinator-mining-gate 2-of-N met. WARRANT verdict:
  genuine L4 entry (the shared output-product reduction verb; ONE symmetric-Gram
  reduction across two output products, the weight the only difference — a navigable
  L4 home as the reduce-to-matrix data-algebra combinator, NOT a stranded mine).

```yaml
verified_against:
  - citation: book/src/L1/matrix-weighted-norm.md:110
    verdict: supports
    audited_at: 2026-06-04T205500Z
    note: diagonal folded primitive firm c091; the rank-invariant diagonal input
  - citation: book/src/L1/bilinear-form.md
    verdict: supports
    audited_at: 2026-06-04T205500Z
    note: off-diagonal folded primitive firmed c095 (D1, this cascade); the last residual gate discharged
  - citation: book/src/L4/solve_family.md:4
    verdict: supports
    audited_at: 2026-06-04T205500Z
    note: consumed composition-root family-producer firm c086; the depends-on input
  - citation: reference/palace/palace/drivers/electrostaticsolver.cpp:118-119
    verdict: supports
    audited_at: 2026-06-04T205500Z
    note: M_elec apply + diagonal Dot — capacitance Gram witness 1; citecheck --anchor ok
  - citation: reference/palace/palace/drivers/electrostaticsolver.cpp:139-140
    verdict: supports
    audited_at: 2026-06-04T205500Z
    note: Cinv Invert — the gram_inverse consumer split; citecheck --anchor ok
  - citation: reference/palace/palace/drivers/magnetostaticsolver.cpp:129-131
    verdict: supports
    audited_at: 2026-06-04T205500Z
    note: M_mag apply + diagonal Dot — inductance Gram witness 2; citecheck --anchor ok
  - citation: reference/palace/palace/drivers/magnetostaticsolver.cpp:151-152
    verdict: supports
    audited_at: 2026-06-04T205500Z
    note: Minv Invert — the gram_inverse consumer split; citecheck --anchor ok
```
