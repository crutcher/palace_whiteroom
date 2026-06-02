---
agent: layer-intro-author
invoked_at: 2026-06-02T223435Z
scope: Feature surfaces Part seed — electrostatic exemplar feature column (L4 + L1 + L0)
status: integrated
integrated_at: 2026-06-02T233500Z
integration_commit: 502171088810f0f4bbf849acba3bf2fc9ff51f09
integration_notes: |
  Applied by integrator-per-report (staging row D3, applied_at 2026-06-02T230907Z); finalized by integrator-finalize cycle-070.
  NEW FEATURE-SURFACE SPINE OPENED (directive-5): new top-level Part "# Feature surfaces — entry points" — book/src/feature/index.md (overview + feature×level matrix + chapter-kind status) + the electrostatic exemplar at L4/L1/L0 (book/src/feature/electrostatic.{L4,L1,L0}.md; the composition root config → fe_assemble → solve_family → capacitance reduction → capacitance-out). FIRST instance of the composition-root chapter kind (status: seed (exemplar)), authored ahead of role-spec codification. SUMMARY wires the new Part between Methodology and L4 (disjoint region from D1/D2 — no collision). All in-chapter code 4-space-indented (zero fences). Firmness floor (repair-corrected, on-disk verified): two-of-four composed L1 constituents firm (fe_assemble, ksp_solve); both capacitance-reduction primitives rough-in (matrix-weighted-norm test-coverage-bounded + bilinear-form) — correct for a seed. +1 feature-surface Part / +1 exemplar column. Build-relevant: cargo make book exit 0; all 4 feature/ HTML files render; all 10 distinct relative links resolve. 2 OQs promoted (standing batch-22-meta items, LEFT OPEN): feature-surface-kind-adapted-check-codification + feature-surface-part-path-layout-and-within-column-level-ordering-ratification. Zero gate hits; retroactive-budget 0.
---

# CYCLE: Feature surfaces — electrostatic exemplar (composition-root spine seed)

## Summary

This is the FIRST exemplar of a NEW chapter kind — the **feature-surface / composition-root** chapter (USER DIRECTIVE 2026-06-02, FEATURE-SURFACE SPINE; not yet codified into role-specs, carried via the D3 dispatch prompt; batch-22 meta-phase will codify). A feature chapter presents a Palace **entry-point feature** (what Palace is *written for*) as a TOP-DOWN composition-root **parallel** to the bottom-up vocabulary spine: **inputs = config, outputs = the physical product, body = the composition of the already-firm decomposed vocabulary at that level, links DOWN to the constituent ops/combinators**. It COMPOSES the vocabulary; it does NOT replace it.

I author the **electrostatic simulation feature** — the simplest/cleanest entry point (a FIXED-operator solve: assemble `K` once, then a per-terminal-source RHS-varying map, producing a capacitance matrix) — as a composition-root at three levels (L4 / L1 / L0).

**Part / path layout chosen.** A new top-level `# Feature surfaces` Part, with one feature-column directory per entry-point feature, and **one chapter per level** inside it:
- `book/src/feature/index.md` — Part overview (the spine's purpose + the feature/level matrix).
- `book/src/feature/electrostatic.L4.md` — the L4 composition-root (the outward backend-lowering entry point).
- `book/src/feature/electrostatic.L1.md` — the L1 composition-root (the pure-function feature surface).
- `book/src/feature/electrostatic.L0.md` — the L0 ground-truth feature surface (the driver-source map).

Rationale for **three files per column** (not a single combined chapter): each level narrates the feature in *its own level's vocabulary* (the same high→low / per-level coherence discipline that governs the vocabulary spine), so one file per level keeps each level's vocabulary clean and lets the forthcoming directive-3 by-kind grouping nest a "feature surfaces / entry points" kind that mirrors the existing per-layer Parts. The `electrostatic.<level>.md` flat naming (vs. `electrostatic/<level>.md` nesting) keeps the column visually contiguous in `SUMMARY.md` and defers the directory-nesting decision to the meta-phase once a 2nd feature column lands (see Open questions / pattern note).

The three chapters are wired into `SUMMARY.md` as a new Part inserted **after the Methodology Part and before L4** (the spine is read top-down: features first, then the vocabulary they decompose into) — alpha-ordered within the column by level descending (L4, L1, L0) to match the high→low reading order, NOT alpha-by-filename (a deliberate exception surfaced as a pattern note).

**Critic-framing note (carry into critique).** The critic's **surface-or-evidence** check ADAPTS for this kind: a feature chapter's "surface" IS the feature (the composition root), evidenced by **(a)** the L0 driver-source range that realizes the composition + **(b)** the down-links to the already-firm constituent ops/combinators it composes — NOT a single decomposed operator's source site. A composition-root makes no *new* per-op algebraic claim (the ops it composes carry those); its claims are *compositional* (this feature = this composition of these firm ops, at this level). Please do not mis-flag the composition-root form as "surface without per-op evidence" — the per-op evidence lives in the linked constituent chapters; this chapter's evidence is the driver range + the link set. (Any producer/critic friction with this framing is itself a finding routed to the batch-22 meta-phase — noted in Open questions.)

## L0 anchors confirmed (on-disk this dispatch, via palace-codemap read_range)

All against `palace/drivers/electrostaticsolver.{cpp,hpp}`:
- `electrostaticsolver.cpp:20-21` — `ElectrostaticSolver::Solve(const std::vector<std::unique_ptr<Mesh>> &mesh) const` signature; returns `std::pair<ErrorIndicator, long long int>`.
- `:28-30` — `LaplaceOperator laplace_op(iodata, mesh)` then `auto K = laplace_op.GetStiffnessMatrix()` — the operator `K` assembled ONCE (the `fe_assemble` half).
- `:31` — `const auto &Grad = laplace_op.GetGradMatrix()` — the gradient operator for the post-process `E = -∇V`.
- `:34-36` — `KspSolver ksp(iodata, laplace_op.GetH1Spaces())` then `ksp.SetOperators(*K, *K)` — solver built once, operator captured once, OUTSIDE the loop (the fixed-operator capture).
- `:38` — `PostOperator<ProblemType::ELECTROSTATIC> post_op(iodata, laplace_op)`.
- `:39` — `int n_step = static_cast<int>(laplace_op.GetSources().size())` — the terminal-boundary family size.
- `:40` — `MFEM_VERIFY(n_step > 0, "No terminal boundaries specified for electrostatic simulation!")` — empty-family exclusion.
- `:44` — `Vector RHS(Grad.Width()), E(Grad.Height())`; `:45` — `std::vector<Vector> V(n_step)` — the solution family storage.
- `:59` — `for (const auto &[idx, data] : laplace_op.GetSources())` — the per-terminal-source outer sweep (the `solve_family` map).
- `:68` — `laplace_op.GetExcitationVector(idx, *K, V[step], RHS)` — per-terminal RHS construction.
- `:69` — `ksp.Mult(RHS, V[step])` — the per-element solve (`ksp_solve op inp`), writing into the family slot.
- `:75-76` — `E = 0.0; Grad.AddMult(V[step], E, -1.0)` — `E = -∇V` post-process.
- `:89` — `step++` — family index collection.
- `:95` — `PostprocessTerminals(post_op, laplace_op.GetSources(), V)` — the capacitance-matrix reduction call.
- `:100-160+` — `ElectrostaticSolver::PostprocessTerminals(...)` def. The capacitance reduction:
  - `:111` — `mfem::DenseMatrix C(V.size()), Cm(V.size())`.
  - `:118-119` — diagonal `C(i,i) = Vᵢᵀ K Vᵢ` via `post_op.GetDomainPostOp().M_elec->Mult(V_gf, D_gf)` + `linalg::Dot<Vector>(post_op.GetComm(), V_gf, D_gf)` (the energy-form `Mult`-then-`Dot`).
  - `:122-127` — off-diagonal `C(i,j) = Vⱼᵀ K Vᵢ` via the same `Mult`/`Dot` bilinear pairing.
  - `:139-140` — `mfem::DenseMatrix Cinv(C); Cinv.Invert()` (the COMSOL-formula Maxwell-capacitance inverse; LAPACK).
- `electrostaticsolver.hpp:34-44` — class `ElectrostaticSolver : public BaseSolver`; private `PostprocessTerminals(...)` + private `Solve(...) const override`.

Constituent-vocabulary down-link targets confirmed on-disk (read-only; not modified):
- `book/src/L4/fe_assemble.md` (**firm**) — the assemble-fold combinator (`K = Σ_i assemble_term space term_i`).
- `book/src/L4/solve_family.md` (**rough-in (test-coverage-bounded)**) — the fixed-operator map-over-RHS-family combinator; its §Specializations names the electrostatic terminal-boundary sweep as witness 1 (`electrostaticsolver.cpp:30/35/36/46/60/68/69/89`).
- `book/src/L4/ksp_solve.md` (firm) — the per-element solve cap `solve_family` maps.
- `book/src/L1/fe_assemble.md` (firm) — the L1 assemble fold.
- `book/src/L1/ksp_solve.md` (firm) — the L1 per-solve operator.
- `book/src/L1/matrix-weighted-norm.md` (rough-in (test-coverage-bounded)) — the diagonal energy-form `Vᵢᵀ K Vᵢ`.
- `book/src/L1/bilinear-form.md` (**rough-in**) — the off-diagonal pairing `Vⱼᵀ K Vᵢ` (`α = xᴴ M y`).

## Proposed changes

```edit:book/src/SUMMARY.md
[old]: [Introduction](./introduction.md)
# Methodology
- [Overview](./methodology/overview.md)
- [Goal & Flow](./methodology/goal-flow.md)
# L4 — Graph-Evaluation Calculus
[new]: [Introduction](./introduction.md)
# Methodology
- [Overview](./methodology/overview.md)
- [Goal & Flow](./methodology/goal-flow.md)
# Feature surfaces — entry points
- [Overview](./feature/index.md)
- [electrostatic — L4 composition-root](./feature/electrostatic.L4.md)
- [electrostatic — L1 composition-root](./feature/electrostatic.L1.md)
- [electrostatic — L0 ground-truth surface](./feature/electrostatic.L0.md)
# L4 — Graph-Evaluation Calculus
```

```edit:book/src/feature/index.md
[old]:
[new]:# Feature surfaces — entry points

This Part is the **top-down composition-root spine** — a presentation of Palace's high-level **entry-point features** (what Palace is *written for*) that runs *parallel* to the bottom-up vocabulary spine (L4→L0 + lowerings). Where the vocabulary Parts climb from cited source (L0) to calculus combinators (L4) by *decomposing* operations into reusable algebra, the feature Parts run the other direction: each chapter is a **composition root** that *recomposes* the already-firm decomposed vocabulary back into the user-facing feature.

A feature chapter is **not** a new operator. It is a distinct *kind* of chapter:

- **inputs = config** — the simulation's configuration surface (the `iodata` / problem definition).
- **outputs = the physical product** — the thing the user ran Palace to get (a capacitance matrix, an inductance matrix, S-parameters, eigenfrequencies + Q, fields).
- **body = the composition of the already-firm vocabulary at that level** — the feature is expressed as a wiring of firm ops / combinators, in *that level's* vocabulary (high→low per-level coherence: the L4 chapter composes L4 combinators, the L1 chapter composes L1 operators, the L0 chapter is the cited driver source).
- **links DOWN to the constituent ops/combinators** — every composed piece is a live link to its firm chapter; the feature chapter carries the *compositional* claim (this feature = this composition of these firm pieces), not the per-op algebraic claims (those live in the linked chapters).

It **composes** the vocabulary; it does **not** replace it. Even as a feature decomposes into collections of internal vocabulary, the entry point itself remains a dedicated, navigable surface at each level — so a reader can enter top-down ("what does the electrostatic solver *do*, and what does it compose?") as well as bottom-up ("what is `fe_assemble`, and where is it used?").

## Why a parallel spine

The vocabulary spine answers *"what are the reusable pieces, and how do they lower?"* The feature spine answers *"what are the deliverable features, and how are they assembled from those pieces?"* The two are duals: the vocabulary spine is mined *inward* (decompose for reuse + conciseness); the feature spine is composed *outward* (recompose for the backend-lowering target). The L4 feature chapter in particular is the **outward backend-lowering entry point** — it presents a whole simulation as a single composition of L4 combinators, which is the form an external GPU-tensor / distributed backend wants to consume (the feature surface, not the unfolded driver loop).

## Feature × level matrix (seed)

The spine is seeded with the **electrostatic** exemplar — the simplest/cleanest entry point: a **fixed-operator** solve (assemble the stiffness operator `K` once, then a per-terminal-source RHS-varying map) producing a **capacitance matrix**. The composition root at every level is:

> **config → `fe_assemble` (assemble `K` once) → `solve_family` (fixed-operator per-terminal map) → capacitance-matrix reduction (`Vⱼᵀ K Vᵢ`) → capacitance-out.**

| Feature | L4 (combinator composition) | L1 (pure-function composition) | L0 (cited driver source) |
|---|---|---|---|
| [electrostatic](./electrostatic.L4.md) | [L4 root](./electrostatic.L4.md) | [L1 root](./electrostatic.L1.md) | [L0 surface](./electrostatic.L0.md) |

Planned (per the FEATURE-SURFACE SPINE directive scope; not yet authored): the other 4 sim drivers (magnetostatic, eigenmode, driven, transient), the top-level lifecycle (`main` → `BaseSolver`), the output products (S-params / capacitance / inductance / eigenfreq + Q / fields), and wave-port / boundary-mode. Each lands as a feature column when its constituent vocabulary is firm enough to compose cleanly (a feature that cannot yet be cleanly composed is a *finding about the spine*, surfaced as an open question — the same low-priority test-load discipline the solvers carry on the vocabulary spine).

## Chapter-kind status

`seed (exemplar)` — the electrostatic column is the first exemplar of the feature-surface kind, authored under the FEATURE-SURFACE SPINE user directive (2026-06-02) ahead of role-spec codification (the batch-22 meta-phase codifies the kind into the role-specs + groups it under the forthcoming directive-3 by-kind grouping). The critic's surface-or-evidence check is adapted for this kind: a feature chapter's evidence is the L0 driver-source range + the constituent-op down-links, not a single decomposed op's source site.
```

```edit:book/src/feature/electrostatic.L4.md
[old]:
[new]:---
kind: feature-surface
feature: electrostatic
level: L4
status: seed (exemplar)
composes:
  - book/src/L4/fe_assemble.md (firm — assemble K once: the assemble-fold combinator)
  - book/src/L4/solve_family.md (rough-in (test-coverage-bounded) — fixed-operator per-terminal map)
  - book/src/L4/ksp_solve.md (firm — the per-element solve cap solve_family maps)
l0_ground_truth:
  - palace/drivers/electrostaticsolver.cpp:21-98 (ElectrostaticSolver::Solve)
---

# electrostatic — L4 composition-root

The **electrostatic simulation feature**, presented at L4 as a single composition of firm L4 combinators — the **outward backend-lowering entry point** for the simplest Palace pipeline. This chapter is a *composition root*: it does not introduce a new combinator; it wires the already-firm L4 vocabulary into the user-facing feature (config → capacitance matrix), and links DOWN to each composed piece.

The electrostatic pipeline is the cleanest entry point because it is a **fixed-operator** solve: the stiffness operator `K` is assembled **once**, then re-used unchanged across a family of per-terminal right-hand sides. That fixed-operator shape is exactly the [`solve_family`](../L4/solve_family.md) combinator's load-bearing specialization (operator captured once, hoisted outside the map), and the assemble-once is exactly [`fe_assemble`](../L4/fe_assemble.md).

## The composition

At L4 the whole simulation is the composition (Haskell-style; the strawman `book/src/design/l4_calculus.md` notation):

    -- inputs = config; output = the capacitance matrix (the physical product)
    electrostatic :: ElectrostaticConfig -> CapacitanceMatrix
    electrostatic cfg =
      let space  = h1_space cfg                       -- the H1 finite-element space (readonly construction stratum)
          terms  = [ diffusion (permittivity cfg) ]   -- the weak-form term list (single ε-weighted ∇ term)
          k      = fe_assemble space terms            -- (1) assemble K ONCE  ── L4/fe_assemble (firm)
          rhss   = [ excitation cfg idx | idx <- terminal_sources cfg ]  -- per-terminal RHS family
          sols   = solve_family k rhss                -- (2) fixed-operator per-terminal map  ── L4/solve_family
      in  capacitance_reduce k sols                   -- (3) Cᵢⱼ = Vⱼᵀ K Vᵢ reduction → capacitance matrix

Three composed stages, each a link DOWN to firm L4 vocabulary:

1. **Assemble `K` once** — [`fe_assemble`](../L4/fe_assemble.md) (**firm**). The L4 assemble-fold combinator `fe_assemble space terms = sum (map (assemble_term space) terms)` folds the weak-form term list into the global stiffness operator `K`. For electrostatic the term list is the single ε-weighted diffusion term `[ diffusion(ε) ]` (the single-term reduction, `fe_assemble`'s law 5; the electrostatic specialization is named at `book/src/L4/fe_assemble.md:127`). `space` (the H1 space) is the `readonly` construction stratum captured once. L0: `auto K = laplace_op.GetStiffnessMatrix()` (`palace/drivers/electrostaticsolver.cpp:30`).

2. **Per-terminal map with the operator captured once** — [`solve_family`](../L4/solve_family.md) (**rough-in (test-coverage-bounded)**). The L4 fixed-operator map-over-RHS-family combinator `solve_family op rhss = map (ksp_solve op) rhss` captures `K` once and maps the [`ksp_solve`](../L4/ksp_solve.md) cap over the per-terminal RHS family, collecting the solution family `[Vᵢ]`. The electrostatic terminal-boundary sweep is `solve_family`'s **witness 1** (named at `book/src/L4/solve_family.md:107`): `op = K`, the family is the terminal-boundary index set, each element is one `ksp_solve K rhsᵢ`. The operator-capture-once hoist (`solve_family` law 2) is the L4 typing of `ksp.SetOperators(*K,*K)` sitting OUTSIDE the loop. L0: solver built + captured once at `electrostaticsolver.cpp:34-36`, the family map at `:59`, the per-element solve `ksp.Mult(RHS, V[step])` at `:69`.

3. **Capacitance-matrix reduction** — the quadratic-form reduction `Cᵢⱼ = Vⱼᵀ K Vᵢ` over the solution family, producing the (symmetric) Maxwell capacitance matrix `C` (the COMSOL energy formulation: `Cᵢᵢ = 2Uₑ(Vᵢ)/Vᵢ²`, off-diagonals from the cross energy). At L4 this is a `map`-then-`reduce` over the solution-family pairs using the operator-weighted-bilinear primitives (the rough-in L1 [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) `Vᵢᵀ K Vᵢ` on the diagonal, the rough-in L1 [`bilinear-form`](../L1/bilinear-form.md) `Vⱼᵀ K Vᵢ` off-diagonal) — there is no *new* L4 combinator here; the reduction is a fold of these bilinear-form evaluations over the family-pair grid, with the result inverted (`Cinv = C⁻¹`, LAPACK) for the alternate Maxwell form. This stage is the **output product** half of the composition root; its dedicated L4 reduction-combinator (if the cross-pipeline post-processing proves to share a shape with the magnetostatic inductance reduction) is a forward mine, not authored here (see Open questions). L0: `PostprocessTerminals` (`electrostaticsolver.cpp:95`, def `:100`; the energy-form `Mult`/`Dot` at `:118-127`, the inverse at `:139-140`).

## Inputs / outputs (the feature surface)

- **Input — config.** `ElectrostaticConfig`: the H1 space construction (mesh + order → `h1_space`), the material permittivity ε (→ the diffusion term coefficient), the terminal-boundary source set (→ the RHS family index domain), and the linear-solver configuration (→ the `ksp_solve` solver build). All `readonly` construction-stratum inputs; none threads mutably through the composition. L0 home: `LaplaceOperator laplace_op(iodata, mesh)` (`electrostaticsolver.cpp:28`) — `iodata` is the config surface.
- **Output — the physical product.** `CapacitanceMatrix` — the `n_terminal × n_terminal` Maxwell capacitance matrix `C` (and its inverse). This is what the user ran the electrostatic solver to compute. L0 home: the `mfem::DenseMatrix C` written by `PostprocessTerminals` (`electrostaticsolver.cpp:111`).

## Why this is the cleanest exemplar

The electrostatic feature is the cleanest composition root because **every stage composes a firm or rough-in L4 combinator with no obstruction at the composition level**:

- The assemble is a single-term `fe_assemble` (law 5; no multi-term concatenation needed) — the simplest possible use of the assemble-fold.
- The solve family is `solve_family`'s **fixed-operator** corner — the operator-capture-once specialization that *holds* the concatenation-homomorphism (the cleanest member; the driven pipeline's per-ω-rebuilt operator is the harder `per-element` superset, NOT this feature).
- The reduction is a fold of bilinear-form evaluations (rough-in diagonal + rough-in off-diagonal) — no iterative obstruction.

The whole feature therefore lowers cleanly outward to the L4 backend surface: `electrostatic = capacitance_reduce ∘ solve_family ∘ fe_assemble`, a three-stage pipeline of firm combinators with a single shared operator capture. This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: it advances cleanly because the constituent vocabulary is firm and composes without forcing the spine.

## Constituent down-links

| Stage | L4 combinator | Status | L0 site |
|---|---|---|---|
| assemble K once | [`fe_assemble`](../L4/fe_assemble.md) | firm | `electrostaticsolver.cpp:30` |
| per-terminal solve map | [`solve_family`](../L4/solve_family.md) | rough-in (test-coverage-bounded) | `electrostaticsolver.cpp:34-36, 59, 68-69, 89` |
| per-element solve cap | [`ksp_solve`](../L4/ksp_solve.md) | firm | `electrostaticsolver.cpp:69` |
| capacitance reduction (Vⱼᵀ K Vᵢ) | [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in) / [`bilinear-form`](../L1/bilinear-form.md) (rough-in) — no dedicated L4 reduction combinator yet | rough-in / rough-in (L1) | `electrostaticsolver.cpp:95, 100-138` |

## Status

`seed (exemplar)` — the first feature-surface composition-root authored under the FEATURE-SURFACE SPINE directive (2026-06-02). The composition is sound: stages (1) and (2) compose firm/rough-in L4 combinators; stage (3) composes L1 bilinear-form primitives (rough-in diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + rough-in off-diagonal [`bilinear-form`](../L1/bilinear-form.md); the capacitance reduction has no dedicated L4 reduction combinator yet — a forward mine, not a blocker, since the reduction is a plain fold of evaluations). This chapter carries the *compositional* claim (electrostatic = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `electrostaticsolver.cpp:21-98` (`Solve`) + `:100-138` (`PostprocessTerminals`) realizing the composition, plus the firm constituent down-links.
```

```edit:book/src/feature/electrostatic.L1.md
[old]:
[new]:---
kind: feature-surface
feature: electrostatic
level: L1
status: seed (exemplar)
composes:
  - book/src/L1/fe_assemble.md (firm — assemble K once)
  - book/src/L1/ksp_solve.md (firm — per-terminal solve)
  - book/src/L1/matrix-weighted-norm.md (rough-in (test-coverage-bounded) — diagonal Vᵢᵀ K Vᵢ)
  - book/src/L1/bilinear-form.md (rough-in — off-diagonal Vⱼᵀ K Vᵢ = xᴴ M y)
l0_ground_truth:
  - palace/drivers/electrostaticsolver.cpp:21-98 (ElectrostaticSolver::Solve)
---

# electrostatic — L1 composition-root

The **electrostatic simulation feature**, presented at L1 as a pure-function composition of firm L1 operators. This is the **pure-function feature surface**: the same composition root as the L4 chapter, but expressed in L1 vocabulary (explicit per-operator pure functions, no L4 combinator naming) — the form a reader navigating L1 sees when asking "what whole feature do these L1 operators add up to?"

At L1 the electrostatic feature is a pure function `config → capacitance matrix` built from four firm L1 operators, with the **mutation already lifted** (each operator is mutation-free; the L0 in-place `ksp.Mult(RHS, V[step])` / `M_elec->Mult(...)` writes are lifted to value-returning forms per the L1>L0 mutation rotation).

## The composition

    -- inputs = config; output = the capacitance matrix (the physical product)
    electrostatic :: ElectrostaticConfig -> CapacitanceMatrix
    electrostatic cfg =
      let space = h1_space cfg
          k     = fe_assemble space [ diffusion (permittivity cfg) ]   -- (1) assemble K once
          idxs  = terminal_sources cfg
          vs    = [ ksp_solve k (excitation cfg k idx) | idx <- idxs ] -- (2) per-terminal pure solve
      in  capacitance_matrix k vs                                       -- (3) Cᵢⱼ = bilinear_form k vⱼ vᵢ

1. **Assemble `K` once** — [`fe_assemble`](../L1/fe_assemble.md) (**firm**). The L1 assemble fold `K = Σ_i A(space, termᵢ)` over the single ε-weighted diffusion term. Pure: consumes the space + term list, produces a fresh operator `K`. L0: `laplace_op.GetStiffnessMatrix()` (`palace/drivers/electrostaticsolver.cpp:30`).

2. **Per-terminal pure solve** — [`ksp_solve`](../L1/ksp_solve.md) (**firm**), applied once per terminal source. Each call is the mutation-lifted pure solve `vᵢ = ksp_solve(K, rhsᵢ)` — the L1 form of the L0 `ksp.Mult(RHS, V[step])` (the destination-buffer write lifted to a value-returning solve). The per-terminal RHS `rhsᵢ` is the excitation vector for terminal `idx` (L0 `laplace_op.GetExcitationVector(idx, *K, V[step], RHS)`, `:68`). The fixed-operator reuse (the same `K` across all terminals) is explicit in the composition: `K` is bound once in the `let` and read by every `ksp_solve`. L0: the loop `:59`, the per-element solve `:69`.

3. **Capacitance-matrix reduction** — the symmetric matrix `Cᵢⱼ = Vⱼᵀ K Vᵢ`, built from L1 bilinear-form evaluations (firm diagonal + rough-in off-diagonal):
   - diagonal `Cᵢᵢ = Vᵢᵀ K Vᵢ` — the operator-weighted self-form, the rough-in [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) squared (`matrix_weighted_norm(Vᵢ, K)² = Vᵢᵀ K Vᵢ`; the L0 source builds it directly as `M_elec->Mult(V_gf, D_gf)` then `linalg::Dot(V_gf, D_gf)`, `:118-119`).
   - off-diagonal `Cᵢⱼ = Vⱼᵀ K Vᵢ` — the operator-weighted cross-pairing, the (rough-in) [`bilinear-form`](../L1/bilinear-form.md) `α = xᴴ M y` instantiated `⟨Vⱼ, K Vᵢ⟩` (L0 `:122-127`, the same `Mult`/`Dot` with the `j` grid function).
   The result is the symmetric `C` (and its LAPACK inverse `Cinv`, `:139-140`). This stage is a pure fold of bilinear-form evaluations over the solution-family pair grid — no L1 operator is *new* here; the reduction composes [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) (rough-in) + [`bilinear-form`](../L1/bilinear-form.md) (rough-in).

## Inputs / outputs (the feature surface)

- **Input — config.** `ElectrostaticConfig` (mesh + order → H1 space; permittivity ε → diffusion term; terminal-source set → RHS index domain; linear-solver config). All read-only.
- **Output — the physical product.** `CapacitanceMatrix` — the `n_terminal × n_terminal` Maxwell capacitance matrix `C` (+ inverse). L0: `mfem::DenseMatrix C` (`electrostaticsolver.cpp:111`).

## L1 vs L4

The L1 and L4 composition roots express the **same feature**; they differ in vocabulary:
- **L1** (this chapter): four explicit per-operator pure functions wired by a `let` + list comprehension; the fixed-operator reuse is a value bound once and read repeatedly; the per-terminal map is a comprehension.
- **L4** ([`electrostatic.L4`](./electrostatic.L4.md)): the per-terminal map is the [`solve_family`](../L4/solve_family.md) combinator (the operator-capture-once made *structural*, hoisted outside the map by type); the assemble is the [`fe_assemble`](../L4/fe_assemble.md) fold combinator. The L4 form is the one the outward backend consumes; the L1 form is the pure-function decomposition the L4 combinators name.

The L1→L0 direction (how each pure operator lowers to the in-place driver writes) is the per-operator L1>L0 mutation-rotation themes of the constituent ops; this composition root records only the L1 composition (high→low discipline).

## Constituent down-links

| Stage | L1 operator | Status | L0 site |
|---|---|---|---|
| assemble K once | [`fe_assemble`](../L1/fe_assemble.md) | firm | `electrostaticsolver.cpp:30` |
| per-terminal solve | [`ksp_solve`](../L1/ksp_solve.md) | firm | `electrostaticsolver.cpp:59, 68-69` |
| diagonal Vᵢᵀ K Vᵢ | [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) | rough-in (test-coverage-bounded) | `electrostaticsolver.cpp:118-119` |
| off-diagonal Vⱼᵀ K Vᵢ | [`bilinear-form`](../L1/bilinear-form.md) | rough-in | `electrostaticsolver.cpp:122-127` |

## Status

`seed (exemplar)` — the L1 pure-function composition root for the electrostatic feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02). Two of the four composed L1 operators are firm ([`fe_assemble`](../L1/fe_assemble.md), [`ksp_solve`](../L1/ksp_solve.md)); BOTH capacitance-reduction primitives are rough-in — the diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is `rough-in (test-coverage-bounded)` (no dedicated test exercises the SPD-weighted overload) and the off-diagonal [`bilinear-form`](../L1/bilinear-form.md) is rough-in (its `α = xᴴ M y` signature covers the cross-pairing, so the down-link is correct). The entire stage-3 reduction therefore rests on rough-in L1 primitives — consistent with the column being a `seed (exemplar)`, not a firm composition. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. Evidence: the L0 driver range `electrostaticsolver.cpp:21-98` + `:100-138` realizing the composition, plus the firm L1 constituent down-links.
```

```edit:book/src/feature/electrostatic.L0.md
[old]:
[new]:---
kind: feature-surface
feature: electrostatic
level: L0
status: seed (exemplar)
l0_ground_truth:
  - palace/drivers/electrostaticsolver.cpp:21-98 (ElectrostaticSolver::Solve)
  - palace/drivers/electrostaticsolver.cpp:100-160 (ElectrostaticSolver::PostprocessTerminals)
  - palace/drivers/electrostaticsolver.hpp:34-44 (class declaration)
lifts_to:
  - book/src/feature/electrostatic.L1.md (the L1 pure-function composition root)
---

# electrostatic — L0 ground-truth surface

The **electrostatic simulation feature** at L0: the cited Palace driver source that realizes the composition root, with the per-stage source ranges that the L1 / L4 feature chapters lift. This is the ground-truth surface — every claim is a `(file:start-end)` citation into `palace/drivers/electrostaticsolver.cpp`.

The driver is `ElectrostaticSolver::Solve(const std::vector<std::unique_ptr<Mesh>> &mesh) const`, returning `std::pair<ErrorIndicator, long long int>` (`palace/drivers/electrostaticsolver.cpp:20-21`; declared `palace/drivers/electrostaticsolver.hpp:39-41`). The class is `ElectrostaticSolver : public BaseSolver` with a private `PostprocessTerminals(...)` and the private `Solve(...) const override` (`electrostaticsolver.hpp:34-44`).

## The composition, in source

The driver is a fixed-operator solve: assemble `K` once, sweep the terminal-source family with the operator captured once, reduce to the capacitance matrix. The source stages, in order:

1. **Assemble `K` once.** `LaplaceOperator laplace_op(iodata, mesh)` (`:28`) constructs the operator builder from config (`iodata`) + mesh; `auto K = laplace_op.GetStiffnessMatrix()` (`:30`) assembles the stiffness operator `K` ONCE; `const auto &Grad = laplace_op.GetGradMatrix()` (`:31`) grabs the gradient operator for the field post-process. This is the L0 site the L1/L4 [`fe_assemble`](../L1/fe_assemble.md) lift.

2. **Build the solver, capture the operator once — OUTSIDE the loop.** `KspSolver ksp(iodata, laplace_op.GetH1Spaces())` (`:34`) builds the Krylov solver from config + the H1 space; `ksp.SetOperators(*K, *K)` (`:36`) captures `K` as both system and preconditioner operator. Both are *before* the terminal loop — this placement is the fixed-operator-capture that the L4 [`solve_family`](../L4/solve_family.md) operator-capture-once hoist makes structural.

3. **Set up the terminal-source family.** `PostOperator<ProblemType::ELECTROSTATIC> post_op(iodata, laplace_op)` (`:38`); `int n_step = static_cast<int>(laplace_op.GetSources().size())` (`:39`) — the terminal-boundary count; `MFEM_VERIFY(n_step > 0, "No terminal boundaries specified for electrostatic simulation!")` (`:40`) — the empty-family exclusion; `std::vector<Vector> V(n_step)` (`:45`) — the solution family storage, pre-sized.

4. **Per-terminal-source map (the fixed-operator sweep).** `for (const auto &[idx, data] : laplace_op.GetSources())` (`:59`) iterates the terminal-boundary index family. Per index: `laplace_op.GetExcitationVector(idx, *K, V[step], RHS)` (`:68`) forms the per-terminal RHS (prescribed nonzero voltage on terminal `idx`); `ksp.Mult(RHS, V[step])` (`:69`) solves the fixed system into the family slot `V[step]`; the field post-process `E = 0.0; Grad.AddMult(V[step], E, -1.0)` (`:75-76`) computes `E = -∇V`; `step++` (`:89`) advances the family index. This loop is the L0 site the L4 [`solve_family`](../L4/solve_family.md) map (and per-element L1/L4 [`ksp_solve`](../L1/ksp_solve.md)) lift.

5. **Capacitance-matrix reduction → the physical product.** After the loop, `PostprocessTerminals(post_op, laplace_op.GetSources(), V)` (`:95`, def `:100`) computes the Maxwell capacitance matrix from the solution family. Inside (`:100-138`): `mfem::DenseMatrix C(V.size()), Cm(V.size())` (`:111`); the diagonal `Cᵢᵢ = Vᵢᵀ K Vᵢ` via `post_op.GetDomainPostOp().M_elec->Mult(V_gf, D_gf)` then `linalg::Dot<Vector>(post_op.GetComm(), V_gf, D_gf)` (`:118-119`); the off-diagonal `Cᵢⱼ = Vⱼᵀ K Vᵢ` via the same energy-form `Mult`/`Dot` pairing (`:122-127`); the LAPACK inverse `mfem::DenseMatrix Cinv(C); Cinv.Invert()` (`:139-140`) for the alternate Maxwell form. The energy formulation (`Cᵢᵢ = 2Uₑ(Vᵢ)/Vᵢ²`) follows the COMSOL AC/DC Module manual p. 97 (cited inline in the source comment, `:105-110`). This is the L0 site the diagonal [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) + off-diagonal [`bilinear-form`](../L1/bilinear-form.md) lift.

The driver returns `{indicator, laplace_op.GlobalTrueVSize()}` (`:97`) — the error indicator + the global true-dof count.

## Inputs / outputs (the feature surface, in source)

- **Input — config.** `iodata` (the `IoData` config surface) + `mesh`, consumed by `LaplaceOperator laplace_op(iodata, mesh)` (`:28`) and `KspSolver ksp(iodata, ...)` (`:34`). The terminal-source set is `laplace_op.GetSources()` (`:39`, `:59`, `:95`).
- **Output — the physical product.** The Maxwell capacitance matrix `mfem::DenseMatrix C` (and inverse `Cinv`) written by `PostprocessTerminals` (`:111`, `:139-140`), plus the per-terminal fields `V[step]` / `E` measured by `post_op.MeasureAndPrintAll(step, V[step], E, idx)` (`:82`).

## Lifts to

This L0 surface lifts to the L1 pure-function composition root [`electrostatic.L1`](./electrostatic.L1.md) (each in-place driver write → a value-returning pure operator) and the L4 combinator composition root [`electrostatic.L4`](./electrostatic.L4.md) (the per-terminal loop → the [`solve_family`](../L4/solve_family.md) map; the assemble → the [`fe_assemble`](../L4/fe_assemble.md) fold). The per-operator L1>L0 mutation-rotation themes of the constituent ops carry the per-write lifts; this feature surface records the composition-root *site map* (which driver range realizes which composed stage).

## Status

`seed (exemplar)` — the L0 ground-truth surface for the electrostatic feature, authored under the FEATURE-SURFACE SPINE directive (2026-06-02). Every stage is a cited range into `palace/drivers/electrostaticsolver.cpp`, confirmed on-disk via palace-codemap `read_range` this dispatch. The chapter's evidence IS the driver-source range + the per-stage site map to the constituent ops (the adapted surface-or-evidence form for the feature-surface kind).
```

## Supporting evidence

- **Constituent vocabulary (all on-disk, read-only):** `book/src/L4/fe_assemble.md` (firm), `book/src/L4/solve_family.md` (rough-in (test-coverage-bounded)), `book/src/L4/ksp_solve.md` (firm), `book/src/L1/fe_assemble.md` (firm), `book/src/L1/ksp_solve.md` (firm), `book/src/L1/matrix-weighted-norm.md` (rough-in (test-coverage-bounded)), `book/src/L1/bilinear-form.md` (rough-in; signature `α = xᴴ M y` covers the asymmetric cross-pairing). `solve_family.md` §Specializations already names the electrostatic terminal-boundary sweep as witness 1 with the exact `electrostaticsolver.cpp` line anchors I reuse — the feature chapter's stage (2) is the *composition-root view* of the same sweep `solve_family` mines as a combinator.
- **L0 driver anchors:** all confirmed on-disk this dispatch via palace-codemap `read_range` on `palace/drivers/electrostaticsolver.{cpp,hpp}` (the full `Solve` `:21-98` + `PostprocessTerminals` `:100-160` + the `.hpp` class decl). Line-anchor list above under "L0 anchors confirmed".
- **The composition root is the directive's specified one:** config-in → `fe_assemble` (assemble `K` once) → `solve_family` (fixed corner) → capacitance reduction (`PostprocessTerminals`) → capacitance-out. The three chapters present this at L4 / L1 / L0 respectively.

## Open questions / caveats

1. **Critic-framing for the feature-surface kind (route to batch-22 meta-phase).** The surface-or-evidence check must adapt: a composition-root's evidence is the L0 driver range + the constituent-op down-links, NOT a single decomposed op's source site (stated in each chapter's §Status + the Part index's §Chapter-kind status). If the critic mis-flags the composition-root form (no per-op algebraic claim of its own), that is itself a finding for the batch-22 meta-phase codifying the kind. The kind also needs its variant-axis-coverage / rotation-quality checks formally no-op'd (a feature chapter rotates nothing and has no variant axes — it composes), analogous to how the `stub` tier no-ops those checks.

2. **Pattern note for the meta-phase — Part/path layout.** I chose `book/src/feature/electrostatic.<level>.md` (flat per-level files in a single `feature/` directory) + a new top-level `# Feature surfaces — entry points` Part placed after Methodology, before L4. Rationale in the Summary. The **directory-nesting decision** (`feature/electrostatic/<level>.md` vs the flat `feature/electrostatic.<level>.md`) should be settled by the meta-phase once a 2nd feature column lands — with 5+ planned feature columns × ~3 levels each (~15+ chapters), the flat naming will crowd the Part list, and nesting per-feature directories (each a directive-3 by-kind sub-grouping with its own intro page) is the likely end state. I deferred nesting to avoid over-structuring a 1-column Part (per the directive-3 "don't over-structure a Part with too few chapters" guard). The meta-phase should also decide whether the **level ordering within a column is L4→L1→L0 (high→low reading, my choice) or alpha-by-filename** — I used high→low deliberately (a feature is read top-down), which is an exception to the alpha-within-cohort rule that the by-kind reorg should ratify or correct.

3. **No dedicated L4 capacitance-reduction combinator yet.** Stage (3) (the `Cᵢⱼ = Vⱼᵀ K Vᵢ` reduction) composes L1 bilinear-form primitives (rough-in `matrix-weighted-norm` diagonal + rough-in `bilinear-form` off-diagonal) but has no dedicated L4 reduction combinator. This is a forward combinator-mine candidate IFF the magnetostatic **inductance** reduction (the `Mⱼᵢ = Aⱼᵀ K Aᵢ` cross-energy, the dual feature column) shares the shape — a 2-witness cross-pipeline mine (the same gate `fe_assemble` / `solve_family` passed). Surfaced as an output-product-reduction mine candidate for the planner; NOT a blocker for the electrostatic seed (the reduction is a plain fold of bilinear-form evaluations).

4. **Reduction-primitive firmness (both read on-disk this dispatch).** BOTH capacitance-reduction primitives are **rough-in**. The diagonal primitive [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is **`rough-in (test-coverage-bounded)`** (`## Status` line `rough-in (test-coverage-bounded)` — no dedicated Palace test exercises the SPD-weighted `linalg::Norml2(comm, x, B, Bx)` overload at this exact entry point; cycle-009 precedent); its `√(xᴴ B x)`, squared, gives the diagonal `Vᵢᵀ K Vᵢ`, so the down-link target is correct. The off-diagonal primitive [`bilinear-form`](../L1/bilinear-form.md) is **`rough-in`** (`## Status` line `rough-in (lower-layer-shared-vocabulary, cycle-010-wave-1)`, frontmatter `firmness: rough-in`) — its signature `α = xᴴ M y` (asymmetric weighted inner product, the matrix-weighted generalisation of `dot`) DOES cover the cross-pairing `⟨Vⱼ, K Vᵢ⟩`, so the down-link target is correct. Only the status labels were corrected (no re-target needed), now reflected throughout (frontmatter + both tables + L1/L4 prose). (Surveyed from each on-disk `## Status` line per the survey-chapter-firmness-from-on-disk-Status discipline, NOT from SUMMARY presence.) Consequence: the electrostatic feature composition is firm at stages (1)+(2) (firm/rough-in L4) but stage (3) leans entirely on rough-in L1 primitives (both diagonal AND off-diagonal) — only TWO of the four composed L1 operators (`fe_assemble`, `ksp_solve`) are firm — so the feature column as a whole is a `seed (exemplar)`, not a firm composition, which is correct for a first-exemplar seed.
