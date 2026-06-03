---
agent: layer-intro-author
invoked_at: 2026-06-03T020207Z
scope: magnetostatic feature column (L4 + L1 + L0) + feature/index.md matrix + SUMMARY block (both this-cycle columns)
status: pending
integrated_at: 2026-06-03T024500Z
integration_commit: PLACEHOLDER_SHA_CYCLE_072_FINALIZE
integration_notes: |
  Applied clean cycle-072 (D1; staging row 1/3). Created feature/magnetostatic.{L4,L1,L0}.md (status seed) + SOLE-edited feature/index.md (matrix +2 columns, seed (exemplar)->seed) + SUMMARY.md '# Feature surfaces' block (+6 rows for BOTH magnetostatic + lifecycle columns; D1 sole-owns the feature index/SUMMARY, applied D2's deferred lifecycle rows by canonical slug). 2nd per-driver composition-root exemplar; 2nd solve_family witness (fixed-operator corner); operator-weighted-Gram inductance reduction. 3 OQs promoted incl. the gram_reduce 2-witness combinator-mine candidate. cargo make book exit 0, linkcheck2 clean, all 3 new chapters render. retroactive-budget global 0; no gate hits. Feature-surface spine 1->3 columns this cycle; zero layer-vocabulary count change.
---

# CYCLE: magnetostatic feature column

## Summary

Authors the **magnetostatic feature column** — the 2nd instance of the composition-root feature-surface chapter kind (FEATURE-SURFACE SPINE directive, 2026-06-02), mirroring the cycle-070 electrostatic exemplar. Three new chapters (`feature/magnetostatic.{L4,L1,L0}.md`), each presenting the magnetostatic pipeline as a composition root: **config-in → `fe_assemble` (assemble curl-curl stiffness `K` once) → `solve_family` (fixed corner — per-surface-current-source RHS-varying map) → inductance-matrix reduction (B-weighted Gram `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)`) → inductance-out.**

The magnetostatic pipeline is the second witness of the **fixed-operator** `solve_family` corner (explicitly named the magnetostatic sibling at `book/src/L4/solve_family.md`): structurally identical to electrostatic down to the `GetStiffnessMatrix()` / `SetOperators(*K,*K)`-outside-the-loop / `std::vector<Vector>`-collect shape, differing only in the absorbed family-index domain (surface-current vs terminal boundaries), the RHS-construction call (`CurlCurlOperator::GetExcitationVector` vs `LaplaceOperator::GetExcitationVector`), the per-element field post-process (`B = ∇×A` vs `E = -∇V`), and the energy-form reduction weight (`I_inc` current normalization vs voltage). The physical product is the **inductance matrix** `M` (vs the capacitance matrix `C`).

As **sole index owner this cycle**, also updates `feature/index.md` (matrix + intro prose) and the SUMMARY block with BOTH this-cycle columns: the magnetostatic rows AND D2's lifecycle-root rows (`feature/lifecycle.{L4,L1,L0}.md`, wired by D2's canonical slug; D2 authors the files, integrator wires live links).

## L0 anchors confirmed on-disk (palace-codemap `read_range`, this dispatch)

All into `palace/drivers/magnetostaticsolver.{cpp,hpp}` — confirmed by direct `read_range`, NOT trusted from the planner scope or the `solve_family.md` specialization-note (which carries a pre-existing ~1-line drift on several anchors — flagged in Open questions):

- `Solve` signature: return type `:21`, `MagnetostaticSolver::Solve(const std::vector<std::unique_ptr<Mesh>> &mesh) const` `:22`; body `:22-108`.
- `CurlCurlOperator curlcurl_op(iodata, mesh)` `:28`; `auto K = curlcurl_op.GetStiffnessMatrix()` `:29`; `const auto &Curl = curlcurl_op.GetCurlMatrix()` `:30`.
- `KspSolver ksp(iodata, curlcurl_op.GetNDSpaces(), &curlcurl_op.GetH1Spaces())` `:34`; `ksp.SetOperators(*K, *K)` `:35`.
- `PostOperator<ProblemType::MAGNETOSTATIC> post_op(iodata, curlcurl_op)` `:39`; `int n_step = ... GetSurfaceCurrentOp().Size()` `:40`; `MFEM_VERIFY(n_step > 0, ...)` `:41-42`.
- `Vector RHS(Curl.Width()), B(Curl.Height())` `:46`; `std::vector<Vector> A(n_step)` `:47`; `std::vector<double> I_inc(n_step)` `:48`.
- loop `for (const auto &[idx, data] : curlcurl_op.GetSurfaceCurrentOp())` `:66`.
- `curlcurl_op.GetExcitationVector(idx, RHS)` `:76`; `ksp.Mult(RHS, A[step])` `:77`.
- `Curl.Mult(A[step], B)` `:85` (`B = ∇×A`); `I_inc[step] = data.GetExcitationCurrent()` `:88`; `post_op.MeasureAndPrintAll(step, A[step], B, idx)` `:91`; `step++` `:99`.
- `PostprocessTerminals(post_op, curlcurl_op.GetSurfaceCurrentOp(), A, I_inc)` call `:108`; def `:110`.
- inductance reduction (`:122-152`): `mfem::DenseMatrix M(A.size()), Mm(A.size())` `:122`; diagonal `Mᵢᵢ = (Aᵢᵀ K Aᵢ)/Iᵢ²` via `M_mag->Mult(A_gf, H_gf)` `:129` + `linalg::Dot<Vector>(...)/(I_inc[i]*I_inc[i])` `:130-131`; off-diagonal `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` `:135-138`; LAPACK inverse `mfem::DenseMatrix Minv(M); Minv.Invert()` `:151-152`. COMSOL AC/DC Module p. 97 energy formulation cited in source comment `:115-121`.
- driver returns `{indicator, curlcurl_op.GlobalTrueVSize()}` `:108`.
- class decl: `MagnetostaticSolver : public BaseSolver` with private `PostprocessTerminals(...)` `:28-31` and private `Solve(...) const override` `:33-34` (`magnetostaticsolver.hpp:24-39`).

## Constituent firmness as read on-disk (from each chapter's `## Status` line)

| constituent | on-disk `## Status` | used by |
|---|---|---|
| `L4/fe_assemble` | **firm** | L4 stage 1 |
| `L4/solve_family` | **rough-in (test-coverage-bounded)** | L4 stage 2 |
| `L4/ksp_solve` | **firm** | L4 stage 2 (per-element cap) |
| `L1/fe_assemble` | **firm** | L1 stage 1 |
| `L1/ksp_solve` | **firm** | L1 stage 2 |
| `L1/matrix-weighted-norm` | **rough-in (test-coverage-bounded)** | diagonal `Aᵢᵀ K Aᵢ` |
| `L1/bilinear-form` | **rough-in** (`rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)`) | off-diagonal `Aⱼᵀ K Aᵢ` |

Same firmness profile as the electrostatic column (the two share the entire constituent set). `L1/matrix-weighted-norm` is labeled `rough-in (test-coverage-bounded)` here (the electrostatic column initially mislabeled it firm; that critic finding is honored at authoring time).

## Critic-framing note (the feature-surface kind)

The critic's **surface-or-evidence** check ADAPTS for this kind: a feature chapter's "surface" IS the feature itself, evidenced by **(a)** the L0 driver-source range (`magnetostaticsolver.cpp:22-108` `Solve` + `:110-204` `PostprocessTerminals`) realizing the composition, plus **(b)** the constituent-op down-links to their firm chapters. There is NO single decomposed-op source site to check (the chapter carries the *compositional* claim, not per-op algebraic claims — those live in the linked chapters). The **rotation-quality** and **variant-axis-coverage** checks NO-OP on a feature chapter (like a stub): a composition root introduces no new rotation and no new variant axis; it composes existing firm vocabulary. The **cross-reference-integrity** check is load-bearing here (every down-link must resolve). See Open questions for a meta-phase framing note.

## Proposed changes

```create:book/src/feature/magnetostatic.L4.md
---
kind: feature-surface
feature: magnetostatic
level: L4
status: seed
composes:
  - book/src/L4/fe_assemble.md (firm — assemble curl-curl K once: the assemble-fold combinator)
  - book/src/L4/solve_family.md (rough-in (test-coverage-bounded) — fixed-operator per-source map)
  - book/src/L4/ksp_solve.md (firm — the per-source solve cap solve_family maps)
l0_ground_truth:
  - palace/drivers/magnetostaticsolver.cpp:22-108 (MagnetostaticSolver::Solve)
---

# magnetostatic — L4 composition-root

The **magnetostatic simulation feature**, presented at L4 as a single composition of firm L4 combinators — the **outward backend-lowering entry point** for the curl-curl pipeline. This chapter is a *composition root*: it does not introduce a new combinator; it wires the already-firm L4 vocabulary into the user-facing feature (config → inductance matrix), and links DOWN to each composed piece.

The magnetostatic pipeline is — like [electrostatic](./electrostatic.L4.md) — a **fixed-operator** solve: the curl-curl stiffness operator `K` is assembled **once**, then re-used unchanged across a family of per-surface-current right-hand sides. That fixed-operator shape is exactly the [`solve_family`](../L4/solve_family.md) combinator's load-bearing specialization (operator captured once, hoisted outside the map), and the assemble-once is exactly [`fe_assemble`](../L4/fe_assemble.md). Magnetostatic is the combinator's **second witness** of the fixed corner — named the magnetostatic sibling at `book/src/L4/solve_family.md:113` — structurally identical to electrostatic down to the `GetStiffnessMatrix()` / `SetOperators(*K,*K)`-outside-the-loop / `std::vector<Vector>`-collect shape.

## The composition

At L4 the whole simulation is the composition (Haskell-style; the strawman `book/src/design/l4_calculus.md` notation):

    -- inputs = config; output = the inductance matrix (the physical product)
    magnetostatic :: MagnetostaticConfig -> InductanceMatrix
    magnetostatic cfg =
      let space = nd_space cfg                          -- the Nédélec H(curl) finite-element space (readonly construction stratum)
          terms = [ curl_curl (reluctivity cfg) ]       -- the weak-form term list (single ν-weighted ∇×∇× term)
          k     = fe_assemble space terms               -- (1) assemble K ONCE  ── L4/fe_assemble (firm)
          rhss  = [ excitation cfg idx | idx <- surface_current_sources cfg ]  -- per-source RHS family
          as    = solve_family k rhss                   -- (2) fixed-operator per-source map  ── L4/solve_family
      in  inductance_reduce k as (currents cfg)         -- (3) Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ) reduction → inductance matrix

Three composed stages, each a link DOWN to firm L4 vocabulary:

1. **Assemble `K` once** — [`fe_assemble`](../L4/fe_assemble.md) (**firm**). The L4 assemble-fold combinator `fe_assemble space terms = sum (map (assemble_term space) terms)` folds the weak-form term list into the global curl-curl stiffness operator `K`. For magnetostatic the term list is the single ν-weighted curl-curl term `[ curl_curl(ν) ]` (the single-term reduction, `fe_assemble`'s law 5; magnetostatic is one of `fe_assemble`'s three mining-gate witnesses — the ∇× witness, named at `book/src/L4/fe_assemble.md:167`). `space` (the Nédélec H(curl) space) is the `readonly` construction stratum captured once. L0: `auto K = curlcurl_op.GetStiffnessMatrix()` (`palace/drivers/magnetostaticsolver.cpp:29`).

2. **Per-source map with the operator captured once** — [`solve_family`](../L4/solve_family.md) (**rough-in (test-coverage-bounded)**). The L4 fixed-operator map-over-RHS-family combinator `solve_family op rhss = map (ksp_solve op) rhss` captures `K` once and maps the [`ksp_solve`](../L4/ksp_solve.md) cap over the per-source RHS family, collecting the solution family `[Aᵢ]`. The magnetostatic surface-current sweep is `solve_family`'s **witness 2** (named at `book/src/L4/solve_family.md:113`): `op = K`, the family is the surface-current-boundary index set, each element is one `ksp_solve K rhsᵢ`. The operator-capture-once hoist (`solve_family` law 2) is the L4 typing of `ksp.SetOperators(*K,*K)` sitting OUTSIDE the loop. L0: solver built + captured once at `magnetostaticsolver.cpp:34-35`, the family map at `:66`, the per-element solve `ksp.Mult(RHS, A[step])` at `:77`.

3. **Inductance-matrix reduction** — the B-weighted Gram `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` over the solution family, producing the (symmetric) Maxwell inductance matrix `M` (the COMSOL magnetic-energy formulation: `Mᵢᵢ = 2Uₘ(Aᵢ)/Iᵢ²`, off-diagonals from the cross energy, normalized by the excitation currents `Iᵢ`). At L4 this is a `map`-then-`reduce` over the solution-family pairs using the operator-weighted-bilinear primitives — the rough-in L1 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) `Aᵢᵀ K Aᵢ` on the diagonal, the rough-in L1 [`bilinear-form`](../L1/bilinear-form.md) `Aⱼᵀ K Aᵢ` off-diagonal — each divided by the current normalization `Iᵢ Iⱼ`. There is no *new* L4 combinator here; the reduction is a fold of these bilinear-form evaluations over the family-pair grid, with the result inverted (`Minv = M⁻¹`, LAPACK) for the alternate Maxwell form. This stage is the **output product** half of the composition root; its dedicated L4 reduction-combinator — if the cross-pipeline post-processing proves to share a shape with the electrostatic capacitance reduction (it does, modulo the diagonal current-vs-voltage normalization weight) — is a forward mine, not authored here (see Open questions). L0: `PostprocessTerminals` (`magnetostaticsolver.cpp:108`, def `:110`; the energy-form `Mult`/`Dot` at `:129-138`, the inverse at `:151-152`).

## Inputs / outputs (the feature surface)

- **Input — config.** `MagnetostaticConfig`: the Nédélec H(curl) space construction (mesh + order → `nd_space`), the material reluctivity ν (→ the curl-curl term coefficient), the surface-current-boundary source set (→ the RHS family index domain), and the linear-solver configuration (→ the `ksp_solve` solver build). All `readonly` construction-stratum inputs; none threads mutably through the composition. L0 home: `CurlCurlOperator curlcurl_op(iodata, mesh)` (`magnetostaticsolver.cpp:28`) — `iodata` is the config surface.
- **Output — the physical product.** `InductanceMatrix` — the `n_source × n_source` Maxwell inductance matrix `M` (and its inverse `Minv`). This is what the user ran the magnetostatic solver to compute. L0 home: the `mfem::DenseMatrix M` written by `PostprocessTerminals` (`magnetostaticsolver.cpp:122`).

## Why this composes cleanly (sibling of the cleanest exemplar)

The magnetostatic feature composes as cleanly as [electrostatic](./electrostatic.L4.md) because **every stage composes a firm or rough-in L4 combinator with no obstruction at the composition level**:

- The assemble is a single-term `fe_assemble` (law 5; no multi-term concatenation needed) — the ∇× witness of the assemble-fold.
- The solve family is `solve_family`'s **fixed-operator** corner — the operator-capture-once specialization that *holds* the concatenation-homomorphism (the second witness; the driven pipeline's per-ω-rebuilt operator is the harder `per-element` superset, NOT this feature).
- The reduction is a fold of bilinear-form evaluations (rough-in diagonal + rough-in off-diagonal), differing from electrostatic's only in the per-element current normalization `Iᵢ Iⱼ` (a scalar weight absorbed into the fold) — no iterative obstruction.

The whole feature therefore lowers cleanly outward to the L4 backend surface: `magnetostatic = inductance_reduce ∘ solve_family ∘ fe_assemble`, a three-stage pipeline of firm combinators with a single shared operator capture. This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: it advances cleanly because the constituent vocabulary is firm and composes without forcing the spine.

## Constituent down-links

| Stage | L4 combinator | Status | L0 site |
|---|---|---|---|
| assemble K once | [`fe_assemble`](../L4/fe_assemble.md) | firm | `magnetostaticsolver.cpp:29` |
| per-source solve map | [`solve_family`](../L4/solve_family.md) | rough-in (test-coverage-bounded) | `magnetostaticsolver.cpp:34-35, 66, 76-77, 99` |
| per-element solve cap | [`ksp_solve`](../L4/ksp_solve.md) | firm | `magnetostaticsolver.cpp:77` |
| inductance reduction (Aⱼᵀ K Aᵢ / Iᵢ Iⱼ) | [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in) / [`bilinear-form`](../L1/bilinear-form.md) (rough-in) — no dedicated L4 reduction combinator yet | rough-in / rough-in (L1) | `magnetostaticsolver.cpp:108, 110-152` |

## Status

`seed` — the second feature-surface composition-root authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [electrostatic](./electrostatic.L4.md) exemplar. The composition is sound: stages (1) and (2) compose firm/rough-in L4 combinators (the second witness of the fixed-operator `solve_family` corner); stage (3) composes L1 bilinear-form primitives (rough-in diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + rough-in off-diagonal [`bilinear-form`](../L1/bilinear-form.md), each current-normalized; no dedicated L4 reduction combinator yet — a forward mine shared with the electrostatic capacitance reduction, not a blocker, since the reduction is a plain fold of evaluations). This chapter carries the *compositional* claim (magnetostatic = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `magnetostaticsolver.cpp:22-108` (`Solve`) + `:110-204` (`PostprocessTerminals`) realizing the composition, plus the firm constituent down-links.
```

```create:book/src/feature/magnetostatic.L1.md
---
kind: feature-surface
feature: magnetostatic
level: L1
status: seed
composes:
  - book/src/L1/fe_assemble.md (firm — assemble curl-curl K once)
  - book/src/L1/ksp_solve.md (firm — per-source solve)
  - book/src/L1/matrix-weighted-norm.md (rough-in (test-coverage-bounded) — diagonal Aᵢᵀ K Aᵢ)
  - book/src/L1/bilinear-form.md (rough-in — off-diagonal Aⱼᵀ K Aᵢ = xᴴ M y)
l0_ground_truth:
  - palace/drivers/magnetostaticsolver.cpp:22-108 (MagnetostaticSolver::Solve)
---

# magnetostatic — L1 composition-root

The **magnetostatic simulation feature**, presented at L1 as a pure-function composition of firm L1 operators. This is the **pure-function feature surface**: the same composition root as the [L4 chapter](./magnetostatic.L4.md), but expressed in L1 vocabulary (explicit per-operator pure functions, no L4 combinator naming) — the form a reader navigating L1 sees when asking "what whole feature do these L1 operators add up to?"

At L1 the magnetostatic feature is a pure function `config → inductance matrix` built from four firm/rough-in L1 operators, with the **mutation already lifted** (each operator is mutation-free; the L0 in-place `ksp.Mult(RHS, A[step])` / `M_mag->Mult(...)` writes are lifted to value-returning forms per the L1>L0 mutation rotation).

## The composition

    -- inputs = config; output = the inductance matrix (the physical product)
    magnetostatic :: MagnetostaticConfig -> InductanceMatrix
    magnetostatic cfg =
      let space = nd_space cfg
          k     = fe_assemble space [ curl_curl (reluctivity cfg) ]    -- (1) assemble K once
          idxs  = surface_current_sources cfg
          as    = [ ksp_solve k (excitation cfg k idx) | idx <- idxs ]  -- (2) per-source pure solve
      in  inductance_matrix k as (currents cfg)                          -- (3) Mᵢⱼ = bilinear_form k aⱼ aᵢ / (Iᵢ Iⱼ)

1. **Assemble `K` once** — [`fe_assemble`](../L1/fe_assemble.md) (**firm**). The L1 assemble fold `K = Σ_i A(space, termᵢ)` over the single ν-weighted curl-curl term. Pure: consumes the Nédélec space + term list, produces a fresh operator `K`. L0: `curlcurl_op.GetStiffnessMatrix()` (`palace/drivers/magnetostaticsolver.cpp:29`).

2. **Per-source pure solve** — [`ksp_solve`](../L1/ksp_solve.md) (**firm**), applied once per surface-current source. Each call is the mutation-lifted pure solve `aᵢ = ksp_solve(K, rhsᵢ)` — the L1 form of the L0 `ksp.Mult(RHS, A[step])` (the destination-buffer write lifted to a value-returning solve). The per-source RHS `rhsᵢ` is the excitation vector for surface-current source `idx` (L0 `curlcurl_op.GetExcitationVector(idx, RHS)`, `:76`). The fixed-operator reuse (the same `K` across all sources) is explicit in the composition: `K` is bound once in the `let` and read by every `ksp_solve`. L0: the loop `:66`, the per-element solve `:77`.

3. **Inductance-matrix reduction** — the symmetric matrix `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)`, built from L1 bilinear-form evaluations (rough-in diagonal + rough-in off-diagonal), each normalized by the excitation currents:
   - diagonal `Mᵢᵢ = (Aᵢᵀ K Aᵢ)/Iᵢ²` — the operator-weighted self-form normalized by the squared current, the rough-in [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) squared (`matrix_weighted_norm(Aᵢ, K)² = Aᵢᵀ K Aᵢ`; the L0 source builds it directly as `M_mag->Mult(A_gf, H_gf)` then `linalg::Dot(A_gf, H_gf)`, then `/ (I_inc[i]*I_inc[i])`, `:129-131`).
   - off-diagonal `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` — the operator-weighted cross-pairing normalized by the current product, the (rough-in) [`bilinear-form`](../L1/bilinear-form.md) `α = xᴴ M y` instantiated `⟨Aⱼ, K Aᵢ⟩` (L0 `:135-138`, the same `Mult`/`Dot` with the `j` grid function, then `/ (I_inc[i]*I_inc[j])`).
   The result is the symmetric `M` (and its LAPACK inverse `Minv`, `:151-152`). This stage is a pure fold of current-normalized bilinear-form evaluations over the solution-family pair grid — no L1 operator is *new* here; the reduction composes [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in) + [`bilinear-form`](../L1/bilinear-form.md) (rough-in), with the current normalization a scalar weight on each entry.

## Inputs / outputs (the feature surface)

- **Input — config.** `MagnetostaticConfig` (mesh + order → Nédélec H(curl) space; reluctivity ν → curl-curl term; surface-current-source set → RHS index domain + the excitation currents `Iᵢ`; linear-solver config). All read-only.
- **Output — the physical product.** `InductanceMatrix` — the `n_source × n_source` Maxwell inductance matrix `M` (+ inverse). L0: `mfem::DenseMatrix M` (`magnetostaticsolver.cpp:122`).

## L1 vs L4

The L1 and L4 composition roots express the **same feature**; they differ in vocabulary:
- **L1** (this chapter): four explicit per-operator pure functions wired by a `let` + list comprehension; the fixed-operator reuse is a value bound once and read repeatedly; the per-source map is a comprehension.
- **L4** ([`magnetostatic.L4`](./magnetostatic.L4.md)): the per-source map is the [`solve_family`](../L4/solve_family.md) combinator (the operator-capture-once made *structural*, hoisted outside the map by type); the assemble is the [`fe_assemble`](../L4/fe_assemble.md) fold combinator. The L4 form is the one the outward backend consumes; the L1 form is the pure-function decomposition the L4 combinators name.

The L1→L0 direction (how each pure operator lowers to the in-place driver writes) is the per-operator L1>L0 mutation-rotation themes of the constituent ops; this composition root records only the L1 composition (high→low discipline).

## Constituent down-links

| Stage | L1 operator | Status | L0 site |
|---|---|---|---|
| assemble K once | [`fe_assemble`](../L1/fe_assemble.md) | firm | `magnetostaticsolver.cpp:29` |
| per-source solve | [`ksp_solve`](../L1/ksp_solve.md) | firm | `magnetostaticsolver.cpp:66, 76-77` |
| diagonal Aᵢᵀ K Aᵢ / Iᵢ² | [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) | rough-in (test-coverage-bounded) | `magnetostaticsolver.cpp:129-131` |
| off-diagonal Aⱼᵀ K Aᵢ / Iᵢ Iⱼ | [`bilinear-form`](../L1/bilinear-form.md) | rough-in | `magnetostaticsolver.cpp:135-138` |

## Status

`seed` — the L1 pure-function composition root for the magnetostatic feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [electrostatic.L1](./electrostatic.L1.md) exemplar. Two of the four composed L1 operators are firm ([`fe_assemble`](../L1/fe_assemble.md), [`ksp_solve`](../L1/ksp_solve.md)); BOTH inductance-reduction primitives are rough-in — the diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is `rough-in (test-coverage-bounded)` (no dedicated test exercises the SPD-weighted overload) and the off-diagonal [`bilinear-form`](../L1/bilinear-form.md) is rough-in (its `α = xᴴ M y` signature covers the cross-pairing, so the down-link is correct). The entire stage-3 reduction therefore rests on rough-in L1 primitives — consistent with the column being a `seed`, not a firm composition. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. Evidence: the L0 driver range `magnetostaticsolver.cpp:22-108` + `:110-204` realizing the composition, plus the firm L1 constituent down-links.
```

```create:book/src/feature/magnetostatic.L0.md
---
kind: feature-surface
feature: magnetostatic
level: L0
status: seed
l0_ground_truth:
  - palace/drivers/magnetostaticsolver.cpp:22-108 (MagnetostaticSolver::Solve)
  - palace/drivers/magnetostaticsolver.cpp:110-204 (MagnetostaticSolver::PostprocessTerminals)
  - palace/drivers/magnetostaticsolver.hpp:24-39 (class declaration)
lifts_to:
  - book/src/feature/magnetostatic.L1.md (the L1 pure-function composition root)
---

# magnetostatic — L0 ground-truth surface

The **magnetostatic simulation feature** at L0: the cited Palace driver source that realizes the composition root, with the per-stage source ranges that the L1 / L4 feature chapters lift. This is the ground-truth surface — every claim is a `(file:start-end)` citation into `palace/drivers/magnetostaticsolver.cpp`.

The driver is `MagnetostaticSolver::Solve(const std::vector<std::unique_ptr<Mesh>> &mesh) const`, returning `std::pair<ErrorIndicator, long long int>` (`palace/drivers/magnetostaticsolver.cpp:21-22`; declared `palace/drivers/magnetostaticsolver.hpp:33-34`). The class is `MagnetostaticSolver : public BaseSolver` with a private `PostprocessTerminals(...)` and the private `Solve(...) const override` (`magnetostaticsolver.hpp:24-39`).

## The composition, in source

The driver is a fixed-operator solve: assemble the curl-curl stiffness `K` once, sweep the surface-current-source family with the operator captured once, reduce to the inductance matrix. The source stages, in order:

1. **Assemble `K` once.** `CurlCurlOperator curlcurl_op(iodata, mesh)` (`:28`) constructs the operator builder from config (`iodata`) + mesh; `auto K = curlcurl_op.GetStiffnessMatrix()` (`:29`) assembles the curl-curl stiffness operator `K` ONCE; `const auto &Curl = curlcurl_op.GetCurlMatrix()` (`:30`) grabs the curl operator for the field post-process (`B = ∇×A`). This is the L0 site the L1/L4 [`fe_assemble`](../L1/fe_assemble.md) lift.

2. **Build the solver, capture the operator once — OUTSIDE the loop.** `KspSolver ksp(iodata, curlcurl_op.GetNDSpaces(), &curlcurl_op.GetH1Spaces())` (`:34`) builds the Krylov solver from config + the Nédélec H(curl) spaces (with the H1 spaces for the auxiliary-space preconditioner); `ksp.SetOperators(*K, *K)` (`:35`) captures `K` as both system and preconditioner operator. Both are *before* the source loop — this placement is the fixed-operator-capture that the L4 [`solve_family`](../L4/solve_family.md) operator-capture-once hoist makes structural.

3. **Set up the surface-current-source family.** `PostOperator<ProblemType::MAGNETOSTATIC> post_op(iodata, curlcurl_op)` (`:39`); `int n_step = static_cast<int>(curlcurl_op.GetSurfaceCurrentOp().Size())` (`:40`) — the surface-current-boundary count; `MFEM_VERIFY(n_step > 0, "No surface current boundaries specified for magnetostatic simulation!")` (`:41-42`) — the empty-family exclusion; `Vector RHS(Curl.Width()), B(Curl.Height())` (`:46`) — the RHS + B-field scratch; `std::vector<Vector> A(n_step)` (`:47`) — the solution family storage, pre-sized; `std::vector<double> I_inc(n_step)` (`:48`) — the per-source excitation-current storage (the inductance-matrix normalization).

4. **Per-source map (the fixed-operator sweep).** `for (const auto &[idx, data] : curlcurl_op.GetSurfaceCurrentOp())` (`:66`) iterates the surface-current-boundary index family. Per index: `A[step].SetSize(...)`/`A[step] = 0.0` (`:73-75`) zeros the family slot; `curlcurl_op.GetExcitationVector(idx, RHS)` (`:76`) forms the per-source RHS (prescribed current on surface `idx`); `ksp.Mult(RHS, A[step])` (`:77`) solves the fixed system into the family slot `A[step]`; the field post-process `Curl.Mult(A[step], B)` (`:85`) computes `B = ∇×A`; `I_inc[step] = data.GetExcitationCurrent()` (`:88`) records the excitation current; `step++` (`:99`) advances the family index. This loop is the L0 site the L4 [`solve_family`](../L4/solve_family.md) map (and per-element L1/L4 [`ksp_solve`](../L1/ksp_solve.md)) lift.

5. **Inductance-matrix reduction → the physical product.** After the loop, `PostprocessTerminals(post_op, curlcurl_op.GetSurfaceCurrentOp(), A, I_inc)` (`:108`, def `:110`) computes the Maxwell inductance matrix from the solution family. Inside (`:110-204`): `mfem::DenseMatrix M(A.size()), Mm(A.size())` (`:122`); the diagonal `Mᵢᵢ = (Aᵢᵀ K Aᵢ)/Iᵢ²` via `post_op.GetDomainPostOp().M_mag->Mult(A_gf, H_gf)` then `linalg::Dot<Vector>(post_op.GetComm(), A_gf, H_gf) / (I_inc[i]*I_inc[i])` (`:129-131`); the off-diagonal `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)` via the same energy-form `Mult`/`Dot` pairing with the `j` grid function, then `/ (I_inc[i]*I_inc[j])` (`:135-138`); the LAPACK inverse `mfem::DenseMatrix Minv(M); Minv.Invert()` (`:151-152`) for the alternate Maxwell form. The energy formulation (`Mᵢᵢ = 2Uₘ(Aᵢ)/Iᵢ²`) follows the COMSOL AC/DC Module manual p. 97 (cited inline in the source comment, `:115-121`). This is the L0 site the diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + off-diagonal [`bilinear-form`](../L1/bilinear-form.md) lift.

The driver returns `{indicator, curlcurl_op.GlobalTrueVSize()}` (`:108`) — the error indicator + the global true-dof count.

## Inputs / outputs (the feature surface, in source)

- **Input — config.** `iodata` (the `IoData` config surface) + `mesh`, consumed by `CurlCurlOperator curlcurl_op(iodata, mesh)` (`:28`) and `KspSolver ksp(iodata, ...)` (`:34`). The surface-current-source set is `curlcurl_op.GetSurfaceCurrentOp()` (`:40`, `:66`, `:108`); the excitation currents are `data.GetExcitationCurrent()` (`:88`).
- **Output — the physical product.** The Maxwell inductance matrix `mfem::DenseMatrix M` (and inverse `Minv`) written by `PostprocessTerminals` (`:122`, `:151-152`), plus the per-source fields `A[step]` / `B` measured by `post_op.MeasureAndPrintAll(step, A[step], B, idx)` (`:91`).

## Lifts to

This L0 surface lifts to the L1 pure-function composition root [`magnetostatic.L1`](./magnetostatic.L1.md) (each in-place driver write → a value-returning pure operator) and the L4 combinator composition root [`magnetostatic.L4`](./magnetostatic.L4.md) (the per-source loop → the [`solve_family`](../L4/solve_family.md) map; the assemble → the [`fe_assemble`](../L4/fe_assemble.md) fold). The per-operator L1>L0 mutation-rotation themes of the constituent ops carry the per-write lifts; this feature surface records the composition-root *site map* (which driver range realizes which composed stage).

## Status

`seed` — the L0 ground-truth surface for the magnetostatic feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02), mirroring the [electrostatic.L0](./electrostatic.L0.md) exemplar. Every stage is a cited range into `palace/drivers/magnetostaticsolver.cpp`, confirmed on-disk via palace-codemap `read_range` this dispatch. The chapter's evidence IS the driver-source range + the per-stage site map to the constituent ops (the adapted surface-or-evidence form for the feature-surface kind).
```

```edit:book/src/feature/index.md
[old]: ## Feature × level matrix (seed)

The spine is seeded with the **electrostatic** exemplar — the simplest/cleanest entry point: a **fixed-operator** solve (assemble the stiffness operator `K` once, then a per-terminal-source RHS-varying map) producing a **capacitance matrix**. The composition root at every level is:

> **config → `fe_assemble` (assemble `K` once) → `solve_family` (fixed-operator per-terminal map) → capacitance-matrix reduction (`Vⱼᵀ K Vᵢ`) → capacitance-out.**

| Feature | L4 (combinator composition) | L1 (pure-function composition) | L0 (cited driver source) |
|---|---|---|---|
| [electrostatic](./electrostatic.L4.md) | [L4 root](./electrostatic.L4.md) | [L1 root](./electrostatic.L1.md) | [L0 surface](./electrostatic.L0.md) |

Planned (per the FEATURE-SURFACE SPINE directive scope; not yet authored): the other 4 sim drivers (magnetostatic, eigenmode, driven, transient), the top-level lifecycle (`main` → `BaseSolver`), the output products (S-params / capacitance / inductance / eigenfreq + Q / fields), and wave-port / boundary-mode. Each lands as a feature column when its constituent vocabulary is firm enough to compose cleanly (a feature that cannot yet be cleanly composed is a *finding about the spine*, surfaced as an open question — the same low-priority test-load discipline the solvers carry on the vocabulary spine).
[new]: ## Feature × level matrix

The spine is seeded with the **electrostatic** exemplar — the simplest/cleanest entry point: a **fixed-operator** solve (assemble the stiffness operator `K` once, then a per-terminal-source RHS-varying map) producing a **capacitance matrix**. The composition root at every level is:

> **config → `fe_assemble` (assemble `K` once) → `solve_family` (fixed-operator per-source map) → energy-form reduction (`Xⱼᵀ K Xᵢ`) → physical-product-out.**

The **magnetostatic** column (cycle-072) is the second witness of this fixed-operator shape — structurally identical to electrostatic down to the `GetStiffnessMatrix()` / `SetOperators(*K,*K)`-outside-the-loop / `std::vector<Vector>`-collect shape, differing only in the absorbed family-index domain (surface-current vs terminal boundaries), the per-element field post-process (`B = ∇×A` vs `E = -∇V`), and the energy-form normalization (the inductance matrix is current-normalized `(Aⱼᵀ K Aᵢ)/(Iᵢ Iⱼ)`; the capacitance matrix is voltage-formulated `Vⱼᵀ K Vᵢ`). The **lifecycle** column (cycle-072) is the top-level composition root — `main` → `BaseSolver` dispatch — that the per-feature columns hang under.

The within-column level ordering is **high→low** (L4 → L1 → L0), NOT alphabetized; the Feature Part does not use by-kind nesting yet (small-Part guard).

| Feature | L4 (combinator composition) | L1 (pure-function composition) | L0 (cited driver source) |
|---|---|---|---|
| [electrostatic](./electrostatic.L4.md) | [L4 root](./electrostatic.L4.md) | [L1 root](./electrostatic.L1.md) | [L0 surface](./electrostatic.L0.md) |
| [magnetostatic](./magnetostatic.L4.md) | [L4 root](./magnetostatic.L4.md) | [L1 root](./magnetostatic.L1.md) | [L0 surface](./magnetostatic.L0.md) |
| [lifecycle](./lifecycle.L4.md) | [L4 root](./lifecycle.L4.md) | [L1 root](./lifecycle.L1.md) | [L0 surface](./lifecycle.L0.md) |

Planned (per the FEATURE-SURFACE SPINE directive scope; not yet authored): the remaining sim drivers (eigenmode, driven, transient), the output products (S-params / capacitance / inductance / eigenfreq + Q / fields), and wave-port / boundary-mode. Each lands as a feature column when its constituent vocabulary is firm enough to compose cleanly (a feature that cannot yet be cleanly composed is a *finding about the spine*, surfaced as an open question — the same low-priority test-load discipline the solvers carry on the vocabulary spine).
```

```edit:book/src/feature/index.md
[old]: `seed (exemplar)` — the electrostatic column is the first exemplar of the feature-surface kind, authored under the FEATURE-SURFACE SPINE user directive (2026-06-02) ahead of role-spec codification (the batch-22 meta-phase codifies the kind into the role-specs + groups it under the forthcoming directive-3 by-kind grouping). The critic's surface-or-evidence check is adapted for this kind: a feature chapter's evidence is the L0 driver-source range + the constituent-op down-links, not a single decomposed op's source site.
[new]: `seed` — the electrostatic column is the first exemplar of the feature-surface kind, authored under the FEATURE-SURFACE SPINE user directive (2026-06-02) ahead of role-spec codification; the magnetostatic + lifecycle columns (cycle-072) are the second-wave instances confirming the kind scales (the batch-22 meta-phase codifies the kind into the role-specs + groups it under the forthcoming directive-3 by-kind grouping). The critic's surface-or-evidence check is adapted for this kind: a feature chapter's evidence is the L0 driver-source range + the constituent-op down-links, not a single decomposed op's source site; the rotation-quality + variant-axis-coverage checks no-op (a composition root introduces no new rotation or variant axis — it composes existing firm vocabulary).
```

```edit:book/src/SUMMARY.md
[old]: # Feature surfaces — entry points
- [Overview](./feature/index.md)
- [electrostatic — L4 composition-root](./feature/electrostatic.L4.md)
- [electrostatic — L1 composition-root](./feature/electrostatic.L1.md)
- [electrostatic — L0 ground-truth surface](./feature/electrostatic.L0.md)
[new]: # Feature surfaces — entry points
- [Overview](./feature/index.md)
- [electrostatic — L4 composition-root](./feature/electrostatic.L4.md)
- [electrostatic — L1 composition-root](./feature/electrostatic.L1.md)
- [electrostatic — L0 ground-truth surface](./feature/electrostatic.L0.md)
- [magnetostatic — L4 composition-root](./feature/magnetostatic.L4.md)
- [magnetostatic — L1 composition-root](./feature/magnetostatic.L1.md)
- [magnetostatic — L0 ground-truth surface](./feature/magnetostatic.L0.md)
- [lifecycle — L4 composition-root](./feature/lifecycle.L4.md)
- [lifecycle — L1 composition-root](./feature/lifecycle.L1.md)
- [lifecycle — L0 ground-truth surface](./feature/lifecycle.L0.md)
```

## Supporting evidence

- **L0 driver**: `palace/drivers/magnetostaticsolver.cpp` (`Solve` `:22-108`, `PostprocessTerminals` `:110-204`) + `magnetostaticsolver.hpp:24-39` — all read on-disk via codemap `read_range` this dispatch.
- **Constituent firmness** (read from each chapter's `## Status` line on-disk): `L4/fe_assemble` firm, `L4/solve_family` rough-in (test-coverage-bounded), `L4/ksp_solve` firm, `L1/fe_assemble` firm, `L1/ksp_solve` firm, `L1/matrix-weighted-norm` rough-in (test-coverage-bounded), `L1/bilinear-form` rough-in.
- **`solve_family` magnetostatic-sibling reference**: `book/src/L4/solve_family.md` — the §Specializations magnetostatic note (around `:113`) + the load-bearing operator-capture axis (`:137`) name magnetostatic as fixed-corner witness 2; verified on-disk.
- **Electrostatic exemplar** (mirrored for structure/path/level-ordering): `book/src/feature/{index,electrostatic.L4,electrostatic.L1,electrostatic.L0}.md`.

## Open questions / caveats

1. **Pre-existing anchor drift in `book/src/L4/solve_family.md` §Specializations magnetostatic note** (NOT my file to edit; flag for a lifter/repairer). The magnetostatic specialization note cites `op = K ... GetStiffnessMatrix() (:30)`, `KspSolver ksp(...) (:35)`, `ksp.SetOperators(*K,*K) (:36)`. On-disk (codemap `read_range` this dispatch) those sites are `:29`, `:34`, `:35` respectively (the electrostatic note in the same file shares the off-by-one). My feature chapters cite the on-disk-confirmed numbers (`:29/:34/:35`). The `:66`, `:76`, `:77`, `:47`, `:99` anchors in that note match on-disk. Recommend a follow-up repair pass re-anchor the `solve_family.md` specialization notes (both electro + magneto) to the on-disk `:29/:34/:35`.

2. **Forward mine: a shared L4 energy-form-reduction combinator.** Both electrostatic (capacitance) and magnetostatic (inductance) stage-3 reductions are the same `map`-then-`reduce` over solution-family pairs of an operator-weighted bilinear form `Xⱼᵀ K Xᵢ`, differing only in the scalar normalization (voltage-formulated vs current-normalized `Iᵢ Iⱼ`). This is now a **two-witness** pattern — it meets the ≥2-witness combinator-miner gate. A dedicated L4 `energy_reduce` / `gram_reduce` combinator (folding the rough-in `matrix-weighted-norm` diagonal + `bilinear-form` off-diagonal over the family-pair grid, parameterized by the per-entry normalization) would let both feature L4 chapters link DOWN to a firm reduction combinator instead of two rough-in L1 primitives. Surfaced for combinator-miner / cycle-planner; NOT authored here (one feature column per dispatch, and the reduction is a plain fold so it is not a blocker). The eigenmode/driven Q-factor + S-param post-processing may add further witnesses.

3. **Meta-phase framing note (batch-22 codification of the feature-surface kind).** This 2nd instance confirms the kind's structure scales cleanly: the magnetostatic column was authorable by near-mechanical mirroring of the electrostatic exemplar (same constituent set, same fixed-operator `solve_family` corner, same 3-stage shape), with the only genuine differences being the absorbed family-domain / RHS-construction / field-post-process / normalization-weight — all of which sit BELOW the composition-root claim and are carried by the linked constituent chapters, not restated. Recommended role-spec codifications for the batch-22 meta-phase: **(a)** the feature-surface chapter kind (inputs=config / outputs=physical-product / body=composition-of-firm-vocabulary / links-DOWN), with the high→low within-column level ordering (L4→L1→L0) and the `feature/<name>.{L4,L1,L0}.md` path convention; **(b)** the adapted critic surface-or-evidence check (evidence = L0 driver range + constituent down-links; rotation/variant-axis checks no-op); **(c)** the single-index-owner convention when ≥2 feature columns land in one cycle (this dispatch sole-owned `feature/index.md` + the SUMMARY block for both columns, D2 deferred — the same parallel-blind-shared-index guard the layer indexes carry). **(d)** Whether a feature column whose constituents are all firm should itself promote past `seed` (status-aggregation question: both this column and electrostatic carry rough-in stage-3 primitives, so neither is a clean test of "all-firm → firm feature"; the eigenmode column, if it composes only firm ops, would be the first test).

4. **Status value `seed` vs `seed (exemplar)`.** The electrostatic exemplar carries `status: seed (exemplar)`. I used plain `status: seed` for the magnetostatic chapters (it is no longer THE exemplar — it is a second instance). If the meta-phase prefers a uniform status token across all feature columns, normalize at integration; flagged rather than silently diverging.
