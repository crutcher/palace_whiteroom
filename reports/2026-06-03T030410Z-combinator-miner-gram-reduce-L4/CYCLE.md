---
agent: combinator-miner
invoked_at: 2026-06-03T030410Z
scope: Pattern proposal — gram_reduce (shared L4 operator-weighted symmetric-Gram reduction)
status: pending
integrated_at: 2026-06-03T214500Z
integration_commit: 03d43ae
integration_notes: "cycle-073 D1. Applied clean — new L4/gram_reduce.md (rough-in (test-coverage-bounded)) + L4/index.md dep-map row (alpha fe_assemble<gram_reduce<inner_product) + SUMMARY Data-algebra alpha-insert. DISCHARGES the c072 2-witness mine shared-l4-energy-form-reduction-combinator-gram-reduce-two-witness-mine. Feature-chapter §reduction re-anchors deferred to c074 (OQ). L4 rough-in 1->2. Build exit 0, linkcheck2 clean."
---

# CYCLE: Combinator candidate — gram_reduce

## Summary

Both the electrostatic capacitance reduction `Cᵢⱼ = Vⱼᵀ K Vᵢ` and the magnetostatic
inductance reduction `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` are the **same** post-processing
shape: a `map`-then-`reduce` over the *pairs of a solution family*, evaluating an
operator-weighted bilinear form `xⱼᵀ K xᵢ` at each grid entry, exploiting symmetry
(compute upper triangle, mirror lower), and inverting the result (LAPACK) for the
alternate Maxwell form. The **only** structural difference is a per-entry scalar
**normalization weight** `w(i,j)`: electrostatic is voltage-formulated `w = 1`,
magnetostatic is current-normalized `w = 1/(Iᵢ Iⱼ)`. Both feature L4 chapters
already flag this as "a forward mine" with the 2-witness gate explicitly met on disk
(`electrostatic.L4.md:40`, `magnetostatic.L4.md:40`).

I propose **`gram_reduce`** — the operator-weighted symmetric-Gram reduction
combinator over a solution family-pair grid, parameterized by the per-entry weight
`w(i,j)` — as the **L4 entry** (combinator-as-entry per the VOCABULARY-SHIFT
redirect: ONE symmetric-Gram reduction across the two output products; the weight is
the only difference). It folds the rough-in L1 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
(diagonal `xᵢᵀ K xᵢ`) + rough-in L1 [`bilinear-form`](../L1/bilinear-form.md)
(off-diagonal `xⱼᵀ K xᵢ`) over the grid. It is a **pure value-producing reduction**
(no `Solve` monad / carry / predicate), the **reduce-to-matrix** companion to the
`reduce-to-scalar` [`inner_product`](../L4/inner_product.md) and the `reduce-to-tensor`
[`linear_combination`](../L4/linear_combination.md) data-algebra combinators — so it
lands at **L4 in the Data-algebra combinators & named verbs group**.

The disciplined-cross-pipeline-combinator-mining-gate is run below and is **already
2-of-N met** (electrostatic + magnetostatic positive witnesses, structurally
identical at the load-bearing shape; the weight is a leaf-content variant axis, not a
break-witness). The eigenmode Q-factor and driven S-parameter post-processing are
noted as candidate 3rd+ witnesses for a stronger future mine — **not** authored now.

## Pattern instances

- **Instance 1 (positive witness — electrostatic capacitance):**
  `book/src/feature/electrostatic.L4.md:40` (the §reduction stage prose: "a
  `map`-then-`reduce` over the solution-family pairs using the operator-weighted-bilinear
  primitives … the rough-in L1 `matrix-weighted-norm` `Vᵢᵀ K Vᵢ` on the diagonal, the
  rough-in L1 `bilinear-form` `Vⱼᵀ K Vᵢ` off-diagonal … a forward mine").
  L0 home: `ElectrostaticSolver::PostprocessTerminals`,
  `palace/drivers/electrostaticsolver.cpp:100` (def), `:95` (call site). The per-pair
  evaluation: `M_elec->Mult(V_gf, D_gf)` (`:118`, the `K·Vᵢ` apply) then
  `linalg::Dot<Vector>(comm, V_gf, D_gf)` (`:119` diagonal `Vᵢᵀ K Vᵢ`, `:126`
  off-diagonal `Vⱼᵀ K Vᵢ`); the symmetric mirror at `:131-138`-analog (lower-triangle
  copy); the inverse `Cinv.Invert()` (`:140`, the copy `mfem::DenseMatrix Cinv(C)` at
  `:139`). Weight `w = 1` (voltage `Vᵢ ≡ 1` unit excitation — the `/ Vᵢ²` divides by 1).

- **Instance 2 (positive witness — magnetostatic inductance):**
  `book/src/feature/magnetostatic.L4.md:40` (the §reduction stage prose: "the B-weighted
  Gram `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` over the solution family … the rough-in L1
  `matrix-weighted-norm` `Aᵢᵀ K Aᵢ` on the diagonal, the rough-in L1 `bilinear-form`
  `Aⱼᵀ K Aᵢ` off-diagonal — each divided by the current normalization `Iᵢ Iⱼ` …
  a forward mine … it does, modulo the diagonal current-vs-voltage normalization weight").
  L0 home: `MagnetostaticSolver::PostprocessTerminals`,
  `palace/drivers/magnetostaticsolver.cpp:110` (def), `:105` (call site — **drifted**
  from the dispatch's `:108` to the verified `:105`). The per-pair evaluation:
  `M_mag->Mult(A_gf, H_gf)` (`:129`, the `K·Aᵢ` apply) then `linalg::Dot<Vector>(...)`
  normalized `/ (I_inc[i] * I_inc[i])` (`:131` diagonal) and `/ (I_inc[i] * I_inc[j])`
  (`:138` off-diagonal); the symmetric mirror (lower-triangle copy); the inverse
  `Minv.Invert()` (`:152`, the copy `mfem::DenseMatrix Minv(M)` at `:151`). Weight
  `w(i,j) = 1/(Iᵢ Iⱼ)` (current-normalized).

- **Instance 3 (variant-axis confirmation, NOT a 3rd mine witness — the weight is the
  ONLY structural difference):** the two PostprocessTerminals bodies are
  line-for-line skeleton-identical (`mfem::DenseMatrix C/M(family.size())`, the
  `for i { diagonal; for j>i { off-diagonal }; lower-triangle copy }` double loop, the
  `(.)inv(.); (.)inv.Invert()` tail) — differing ONLY in (a) the operator name
  (`M_elec` vs `M_mag` — both the domain energy operator the feature chapters call `K`),
  (b) the grid-function recovery (`V_gf` vs `A_gf`), and (c) the per-entry weight
  (`/ Vᵢ²` ≡ `×1` vs `/ (Iᵢ Iⱼ)`). (a) and (b) are leaf-content (absorbed into the
  `K : LinearOperator` and `xs : [Tensor]` arguments); (c) is the load-bearing
  **normalization-weight variant axis**.

## Proposed combinator

- **Slug**: `gram_reduce`
- **Layer**: **L4**, in the **Data-algebra combinators & named verbs** group (alpha
  position: between [`fe_assemble`](../L4/fe_assemble.md) and
  [`inner_product`](../L4/inner_product.md)).

  *Rationale — why L4 data-algebra, not adjacent.* `gram_reduce` is a **pure
  value-producing reduction** (no `Solve` monad, no carry, no convergence predicate) —
  it is the `reduce-to-matrix` member of the same L4 algebra-of-folds family as the
  `reduce-to-scalar` [`inner_product`](../L4/inner_product.md) and the
  `reduce-to-tensor` [`linear_combination`](../L4/linear_combination.md) (cf.
  `concepts/black-box-vs-accelerated-kernels.md` §"The combinators rise regardless":
  the general data-algebra combinators rise to L4 as feature-surface verbs the backend
  wants, regardless of solver-test-load). It is NOT an outer-driver/coordination
  combinator (it does not coordinate a solve — it consumes the *already-collected*
  solution family that [`solve_family`](../L4/solve_family.md) produced), so it does
  not belong in the Outer-driver group with `solve_family`/`fold_solve`/`frequency_sweep`.
  It is NOT L3/L2/L1: the feature chapters consume it as the L4 reduction stage of the
  composition root, and the per-entry building blocks already live at L1
  (`matrix-weighted-norm`/`bilinear-form`); `gram_reduce` is the L4 fold *over* them,
  the output-product reduction verb the backend lowers outward (directive-1: L4 is the
  backend-lowering target). L4-not-L1 is also forced by the redirect's
  replace-and-propagate: the feature columns down-link to the L4 combinator, not to
  the two L1 leaves.

- **Signature sketch** (best guess; harvester firms up):

      -- the operator-weighted symmetric-Gram reduction over a solution family-pair grid,
      -- parameterized by the per-entry normalization weight w(i,j):
      gram_reduce :: LinearOperator[N, N]        -- the operator weight K (the domain energy operator)
                  -> [Tensor[N]]                  -- the solution family xs = [x_0 .. x_{m-1}]
                  -> (Int -> Int -> Scalar)       -- the per-entry normalization weight w(i,j)
                  -> Matrix[m, m]                 -- the symmetric Gram matrix G, Gᵢⱼ = w(i,j) · (xⱼᵀ K xᵢ)
      gram_reduce k xs w =
        symmetric_from_upper                                  -- mirror lower triangle from upper (G symmetric)
          [ [ w i j * entry k xs i j | j <- [i .. m-1] ]      -- map over upper-triangle pairs
            | i <- [0 .. m-1] ]
        where
          m              = length xs
          entry k xs i j
            | i == j     = matrix_weighted_norm (xs!!i) k     -- diagonal: xᵢᵀ K xᵢ  (L1 matrix-weighted-norm)
            | otherwise  = bilinear_form (xs!!j) k (xs!!i)    -- off-diag: xⱼᵀ K xᵢ  (L1 bilinear-form)

      -- the alternate Maxwell form is the inverse (a CONSUMER, not part of the reduction):
      gram_inverse :: Matrix[m, m] -> Matrix[m, m]            -- = inv (LAPACK); Cinv / Minv

  Shape contract (bunsen-style): `K : LinearOperator[N, N]` read-only (the domain
  energy operator — `M_elec`/`M_mag` at L0, the feature chapters' `K`); `xs :
  [Tensor[N]]` the collected solution family ([`solve_family`](../L4/solve_family.md)'s
  output `[SimState.x]`); `w : Int -> Int -> Scalar` the per-entry weight; result
  `Matrix[m, m]` symmetric. The two specializations: **electrostatic** `w i j = 1`
  (voltage-formulated, unit excitation); **magnetostatic** `w i j = 1/(I!!i * I!!j)`
  (current-normalized, `I : [Scalar]` the excitation currents absorbed into the weight
  closure).

- **Algebraic intuition.**
  - **Symmetry** (load-bearing): `G` is symmetric — `Gⱼᵢ = Gᵢⱼ` — *because* `K` is
    symmetric/SPD (the energy operator) and `w(i,j) = w(j,i)` (both witnessed weights
    are symmetric: `1` and `1/(IᵢIⱼ)`). This is the law that licenses the
    compute-upper-triangle-then-mirror optimization (L0 `:131-138`-region lower-copy
    loops). Stated as a syntactic identity on the fold: `bilinear_form xⱼ K xᵢ =
    bilinear_form xᵢ K xⱼ` for symmetric `K`.
  - **Diagonal/off-diagonal decomposition** (structural): `entry` splits into the
    `matrix-weighted-norm` self-bilinear on the diagonal and the `bilinear-form`
    cross-bilinear off it — the *same* operator-weighted quadratic form, the diagonal
    being the `xⱼ = xᵢ` specialization (`matrix_weighted_norm x K = bilinear_form x K x`).
    This is the do-NOT-merge note: `matrix-weighted-norm` is the diagonal *consumer*,
    not a distinct fold (cf. the `nrm2`-is-a-consumer-of-`inner_product` guard).
  - **Weight factoring / bilinearity**: the weight `w(i,j)` factors out of each entry
    (`w(i,j) · (xⱼᵀ K xᵢ)`); the underlying `xⱼᵀ K xᵢ` is bilinear in `(xᵢ, xⱼ)`. The
    voltage form is the `w ≡ 1` identity-weight specialization (the multiplicative
    identity element on the weight axis).
  - **Inverse is a consumer, not part of the reduction**: `Cinv`/`Minv` (LAPACK
    `Invert()`) is a downstream scalar/matrix map on the produced `G`, kept OUT of the
    combinator (the `gram_inverse` consumer, the `nrm2`-style split).
  - **No iteration / no carry**: every entry is independent (the grid `map` is a list
    homomorphism over the pairs); the reduction collects, it does not thread state — so
    `gram_reduce` is embarrassingly parallel over the upper-triangle pairs.

- **Variant axes:**
  - **normalization-weight** (`unit | current-normalized` — THE load-bearing axis):
    electrostatic `w = 1` (voltage-formulated), magnetostatic `w = 1/(Iᵢ Iⱼ)`
    (current-normalized). Absorbed into the `w : Int -> Int -> Scalar` closure
    argument. This is the ONLY structural difference between the two witnesses.
  - **operator-source** (`mass-energy` — absorbed): `K` is the domain energy operator
    (`M_elec` diffusion-energy / `M_mag` curl-curl-energy); absorbed into the
    `K : LinearOperator` argument (leaf-content, not structural).
  - **element-type** (`real` — pinned for both witnessed pipelines; the eigenmode
    Q-factor extension would introduce complex, a future-witness axis value).
  - **family-index domain** (`terminal-boundary | surface-current` — absorbed into
    `[Tensor]` / the `w` closure; does not shape the combinator).

## Disciplined-cross-pipeline-combinator-mining-gate (cited: `disciplined-cross-pipeline-combinator-mining-gate`)

The gate is run end-to-end; it is **already 2-of-N met** on disk (the dispatch states
the 2-witness gate is met):

1. **≥2 positive witnesses, structurally identical at the load-bearing shape — MET.**
   electrostatic `electrostaticsolver.cpp:100-140` + magnetostatic
   `magnetostaticsolver.cpp:110-152`, codemap-verified this dispatch
   (`mcp__palace-codemap__read_range` + `search_text` line pinpoints). The two
   PostprocessTerminals bodies are skeleton-identical (Instance 3): same
   `DenseMatrix(family.size())`, same `for i { diag; for j>i { off-diag } }` +
   lower-triangle-mirror double loop, same `Invert()` tail. Differences are
   leaf-content (`M_elec`/`V_gf` vs `M_mag`/`A_gf`).

2. **Classify every break witness as a scope boundary — NONE; the only difference is a
   variant axis, not a break.** The current-vs-voltage normalization weight is NOT a
   structural break (it does not violate any load-bearing invariant — both weights are
   symmetric, both factor out of the bilinear entry); it is the **normalization-weight
   variant axis**, correctly absorbed into the `w` closure argument. (Contrast
   `solve_family`'s driven break-witness, which rebuilt the operator inside the map —
   that was a genuine scope boundary. Here there is no analogous break between the two
   witnesses.)

3. **Name every unprobed pipeline as DEFERRED, with the fold-vs-map flag — done.** The
   eigenmode + driven post-processing are unprobed for *this* reduction shape:
   - **eigenmode Q-factor / eigenfrequency post-processing** — candidate 3rd witness
     (energy-based modal post-processing is plausibly the same operator-weighted Gram
     shape per-mode); **fold-vs-map flag: likely map** (per-mode energy is independent),
     but UNVERIFIED — would introduce the complex element-type axis value. Not authored
     now.
   - **driven S-parameter post-processing** — candidate 3rd witness (port-mode
     overlap/scattering reductions are bilinear-form-shaped); **fold-vs-map flag:
     likely map over port pairs**, but UNVERIFIED and possibly a *different* reduction
     (S-parameters are not symmetric Gram in general — over-unification hazard). Not
     authored now; flagged as a 3rd+-witness probe for a stronger future mine (Open
     question).

4. **Replace-and-propagate, not mine-and-strand — planned.** `gram_reduce` is the
   **entry**; the electrostatic capacitance reduction and magnetostatic inductance
   reduction become **specialization notes re-expressing THROUGH it** (differing only
   in the `w` weight). Layer: L4 data-algebra (justified above). Propagation: the two
   output-product feature columns down-link to `gram_reduce` (the feature-chapter
   §reduction re-anchors — see *Proposed changes* for my coupled-pair decision).

## Proposed changes

### (1) Author `book/src/L4/gram_reduce.md` (combinator-as-entry)

Note: per the dispatch and CLAUDE.md write-authority partition, this report does not
write `book/`. The integrator applies the proposed-changes block below. Unlike a
combinator-miner rough-in *row*, the dispatch explicitly tasks me to **author the
chapter** as the combinator-as-entry; the harvester-formalization split is waived for
this LEAD dispatch (the chapter body is the proposed change, the harvester firms laws
in a later pass if promotion is pursued).

```edit:book/src/L4/gram_reduce.md
---
layer: L4
operator: gram_reduce
firmness: rough-in (test-coverage-bounded)
consumes:
  - book/src/L1/matrix-weighted-norm.md (rough-in — the diagonal self-bilinear xᵢᵀ K xᵢ; the diagonal CONSUMER, the xⱼ=xᵢ specialization of the off-diagonal bilinear)
  - book/src/L1/bilinear-form.md (rough-in — the off-diagonal cross-bilinear xⱼᵀ K xᵢ; the fold element)
  - book/src/L4/solve_family.md (rough-in (test-coverage-bounded) — produces the solution family [xᵢ] this combinator reduces over; the upstream stage in the composition root)
lowers_to:
  - book/src/L1/matrix-weighted-norm.md (the diagonal entry; identity-in-form on the body — the reduction is a fold of L1 bilinear-form evaluations, no dedicated L4>L3 theme; in-line §"Downward")
  - book/src/L1/bilinear-form.md (the off-diagonal entry; identity-in-form on the body)
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

- the diagonal entry `xᵢᵀ K xᵢ` is the rough-in L1
  [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (`√` dropped — `gram_reduce`
  reduces to the *squared* energy `xᵢᵀ K xᵢ = 2Uₑ/ₘ(xᵢ)`, the matrix-weighted-norm's
  radicand);
- the off-diagonal entry `xⱼᵀ K xᵢ` is the rough-in L1
  [`bilinear-form`](../L1/bilinear-form.md) (`xᴴ M y` at `M = K`).

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

    -- the operator-weighted symmetric-Gram reduction over a solution family-pair grid,
    -- parameterized by the per-entry normalization weight w(i,j):
    gram_reduce :: LinearOperator[N, N]        -- the operator weight K (the domain energy operator)
                -> [Tensor[N]]                  -- the solution family xs = [x_0 .. x_{m-1}]
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

Shape contract (bunsen-style; named axes):

- `K : LinearOperator[N, N]` — read-only; the **domain energy operator** (`M_elec`
  diffusion-energy at `electrostaticsolver.cpp:118`, `M_mag` curl-curl-energy at
  `magnetostaticsolver.cpp:129`; the feature chapters call it `K`). Symmetric/SPD —
  the load-bearing precondition for `G`-symmetry.
- `xs : [Tensor[N]]` — the collected solution family ([`solve_family`](./solve_family.md)'s
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

Candidate 3rd+ witnesses (NOT authored — a stronger future mine): eigenmode Q-factor /
eigenfrequency energy post-processing (likely a per-mode map, would introduce the
complex element-type axis) and driven S-parameter post-processing (port-pair map,
possibly a *different* reduction — S-parameters are not symmetric Gram in general, an
over-unification hazard to probe before subsuming). See the L4 index Open questions.

## Dependencies

L1 rows this combinator folds:

- [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in) — the diagonal
  self-bilinear (radicand); the diagonal consumer.
- [`bilinear-form`](../L1/bilinear-form.md) (rough-in) — the off-diagonal cross-bilinear;
  the fold element.

L4 rows:

- [`solve_family`](./solve_family.md) (rough-in (test-coverage-bounded)) — produces the
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

`rough-in (test-coverage-bounded)`. **Reasoning (warrant-first):** the combinator's
**structure** is firm-on-positive-structure — the symmetric-Gram skeleton
(map-over-upper-triangle-pairs, diagonal/off-diagonal split, weight factoring,
symmetric mirror, inverse-as-consumer) is read directly off the two skeleton-identical
positive PostprocessTerminals loops (electrostatic `:100-140` + magnetostatic
`:110-152`), and every law (§Algebraic laws) is a syntactic identity on that fold. So
the *structure* would satisfy the firm-on-positive-structure escape. BUT two factors
gate it to `rough-in (test-coverage-bounded)`:
1. the per-entry building blocks it folds — [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md)
   and [`bilinear-form`](../L1/bilinear-form.md) — are themselves **rough-in** (their
   laws are stated-but-test-unconfirmed), so the entry inherits their reduced maturity;
2. there is **no dedicated Palace unit test** for the Gram reduction (the
   PostprocessTerminals bodies are integration-level, exercised only through the full
   `Solve(mesh)` driver), so the reduction-level laws are test-unconfirmed.

Promotion route: (a) the L1 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) +
[`bilinear-form`](../L1/bilinear-form.md) primitives firm up, AND (b) a dedicated
family-pair Gram-reduction test OR a lowering-verifier pass raising the fold-law
confidence to `inner_product`-equivalent. (Contrast the firm-on-positive-structure
`frequency_sweep` / `fe_assemble`, whose folded primitives are themselves firm —
`gram_reduce`'s primitives are rough-in, which is the firm-vs-rough-in distinction
here.)

**Scope: 2-of-N pipelines** — electrostatic + magnetostatic output products (the two
energy-formulated symmetric-Gram reductions); eigenmode + driven post-processing are
candidate 3rd+ witnesses for a stronger future mine (§Specialization), not in scope
now. The disciplined-cross-pipeline-combinator-mining-gate is 2-of-N met (2 positive
witnesses, no break-witness — the normalization weight is a variant axis).

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
```

### (2) Add the dep-map row to `book/src/L4/index.md` (Data-algebra group, alpha position)

Insert between the `fe_assemble` row and the `inner_product` row in the
**### Data-algebra combinators & named verbs** table (alpha: `fe_assemble` <
`gram_reduce` < `inner_product`):

```edit:book/src/L4/index.md
| [`gram_reduce`](./gram_reduce.md) | `gram_reduce :: LinearOperator[N, N] -> [Tensor[N]] -> (Int -> Int -> Scalar) -> Matrix[m, m]`; `Gᵢⱼ = w(i,j) · (xⱼᵀ K xᵢ)`, symmetric (compute upper, mirror lower). The **operator-weighted symmetric-Gram reduction combinator**: reduce a collected solution family `[xᵢ]` against an operator weight `K` into the symmetric Gram matrix, parameterized by the per-entry normalization weight `w(i,j)`. The **reduce-to-matrix** member of the L4 algebra-of-folds (sibling of reduce-to-scalar [`inner_product`](./inner_product.md) + reduce-to-tensor [`linear_combination`](./linear_combination.md)). ONE reduction across the electrostatic capacitance (`w = 1`) + magnetostatic inductance (`w = 1/(IᵢIⱼ)`) output products — the **weight is the only difference**. Pure value-producing reduction — no `Solve` monad / carry / predicate. | Folds (rough-in L1): [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (diagonal self-bilinear `xᵢᵀ K xᵢ` — the diagonal CONSUMER, NOT a separate fold), [`bilinear-form`](../L1/bilinear-form.md) (off-diagonal cross-bilinear `xⱼᵀ K xᵢ`). Consumes: [`solve_family`](./solve_family.md) (produces the family `[xᵢ]`). Concepts: `black-box-vs-accelerated-kernels` (§"the combinators rise regardless"). Sibling combinators: [`inner_product`](./inner_product.md), [`linear_combination`](./linear_combination.md). | L1 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) / [`bilinear-form`](../L1/bilinear-form.md) by **identity-in-form on the body** (the reduction is a plain fold of L1 bilinear evaluations; **no dedicated L4>L3 theme** — the in-line-marker route; the substantive downward content lives in the L1 primitives' L1>L0 mutation rotations). | `rough-in (test-coverage-bounded)` (harvested cycle-073 D1 LEAD from the feature-chapter forward-mine flags `electrostatic.L4.md:40` + `magnetostatic.L4.md:40`; structure firm-on-positive-structure on 2 skeleton-identical witnesses electrostatic `electrostaticsolver.cpp:100-140` + magnetostatic `magnetostaticsolver.cpp:110-152`, but gated rough-in because the folded L1 primitives are themselves rough-in AND no dedicated Gram-reduction test; promotion = L1 primitives firm + dedicated test/verifier pass. Disciplined-mining-gate 2-of-N met, normalization-weight a variant axis not a break-witness; eigenmode/driven post-processing candidate 3rd+ witnesses for a future mine) |
```

(Also requires a `SUMMARY.md` insertion — the integrator adds
`  - [gram_reduce](./L4/gram_reduce.md)` in the **Data-algebra combinators & named
verbs** sub-list at alpha position between `fe_assemble` and `inner_product`, i.e.
after `book/src/SUMMARY.md:28`. Flagged for the integrator per the stub/chapter wiring
convention.)

### (3) Feature-chapter §reduction re-anchors — DECISION: sequence to c074, leave feature chapters untouched

The dispatch offers me the OPTION to include the electrostatic.L4.md:40 +
magnetostatic.L4.md:40 §reduction re-anchors ("two rough-in L1 primitives" → "the
rough-in L4 `gram_reduce` reduction") in my own proposed-changes IF I judge the
re-anchor mechanical. **My decision: leave the feature chapters untouched; sequence the
re-anchor to c074.**

Reasoning: the re-anchor is NOT purely mechanical. The feature §reduction prose
currently makes a *positive design statement* — "there is no *new* L4 combinator here;
the reduction is a fold of these bilinear-form evaluations" — which is the OPPOSITE of
the claim after `gram_reduce` lands. Re-anchoring requires rewriting that prose to
"the reduction is the L4 `gram_reduce` combinator (rough-in), the `w = 1` / `w =
1/(IᵢIⱼ)` specialization", updating the §"Constituent down-links" tables (the
"no dedicated L4 reduction combinator yet" cells), the `composes:` frontmatter, and the
§Status prose in BOTH chapters. That is substantive replace-and-propagate authoring,
not a mechanical string swap — and doing it in THIS dispatch would couple two feature
chapters' rewrites to a rough-in combinator that has not yet been critic-reviewed. The
coupled-pair form is preferred when mechanical; here it is not, so the safer
replace-and-propagate sequencing is: land `gram_reduce` (this cycle, c073), then
re-anchor the two feature columns through it (c074), once the combinator is in the
artifact and reviewed. I record this as a c074 follow-on in Open questions.

## Supporting evidence

- **Feature-chapter mine flags:** `book/src/feature/electrostatic.L4.md:40`,
  `book/src/feature/magnetostatic.L4.md:40` (both flag "a forward mine"; magnetostatic
  explicitly: "if it shares a shape with the electrostatic capacitance reduction (it
  does, modulo the diagonal current-vs-voltage normalization weight)").
- **L0 postprocess sites (codemap-verified this dispatch):**
  - electrostatic `electrostaticsolver.cpp:95` (call), `:100` (def), `:118` (Mult),
    `:119`/`:126` (Dot diag/off-diag), `:139-140` (Cinv copy + Invert).
  - magnetostatic `magnetostaticsolver.cpp:105` (call — **drifted from dispatch's
    `:108` to verified `:105`**), `:110` (def), `:129` (Mult), `:131`/`:138` (Dot
    normalized), `:151-152` (Minv copy + Invert).
- **L1 primitives folded:** `book/src/L1/matrix-weighted-norm.md` (rough-in),
  `book/src/L1/bilinear-form.md` (rough-in, frontmatter `firmness: rough-in`).
- **Sibling L4 combinators:** `book/src/L4/inner_product.md`,
  `book/src/L4/linear_combination.md` (the reduce-to-scalar / reduce-to-tensor halves
  of the L4 algebra-of-folds).
- **Skill cited:** `skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md`
  (the 2-witness gate, run end-to-end above; 2-of-N met).
- **Tests:** no dedicated unit test exercises the Gram reduction (integration-level via
  `Solve(mesh)`); this gates the status to `rough-in (test-coverage-bounded)`.

## Open questions / caveats

(Appended to `scaffolding/open-questions.md` — see below.)

1. **`gram_reduce` feature-chapter re-anchor sequences to c074** (the replace-and-propagate
   coupled half): the electrostatic + magnetostatic §reduction prose, §"Constituent
   down-links" tables, `composes:` frontmatter, and §Status in both feature columns
   should be re-anchored from "two rough-in L1 primitives / no dedicated L4 reduction
   combinator yet" to "the rough-in L4 `gram_reduce` reduction (the `w = 1` / `w =
   1/(IᵢIⱼ)` specialization)". Judged NOT mechanical (it inverts a positive design
   statement in the prose) — sequenced to c074, not done here.
2. **3rd+-witness probe for a stronger `gram_reduce` mine** (eigenmode Q-factor /
   driven S-parameter): probe whether eigenmode energy-based modal post-processing and
   driven S-parameter port-overlap reductions share the operator-weighted symmetric-Gram
   shape. Fold-vs-map flags: both likely *map* (per-mode / per-port-pair independent),
   but (a) eigenmode would introduce the complex element-type axis value, and (b)
   S-parameters are NOT symmetric Gram in general — an over-unification hazard to clear
   before subsuming. A clean 3rd witness would promote `gram_reduce` from a 2-pipeline
   output-product reduction to a broader feature-surface reduction verb.
3. **`gram_reduce` status promotion is double-gated** on the L1 primitives
   (`matrix-weighted-norm` + `bilinear-form`) firming AND a dedicated Gram-reduction
   test — record the coupling so a future L1-primitive-firming cycle re-checks
   `gram_reduce`'s promotion eligibility.
4. **`gram_inverse` consumer** (`Cinv`/`Minv` LAPACK `Invert()`): kept out of the
   combinator as a downstream matrix-map consumer (the `nrm2`-style split). If a future
   pipeline needs the inverse as a first-class verb, it is the `gram_reduce`-consumer
   to author then; not now.
