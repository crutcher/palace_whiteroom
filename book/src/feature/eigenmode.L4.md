---
kind: feature-surface
feature: eigenmode
level: L4
feature_root: seed
rank: firm
edges:
  depends-on:
    - target: L4/fe_assemble
      kind: composes
    - target: L4/eigsolve
      kind: composes
    - target: L3/divfree-projector
      kind: constrains-eigvec           # GROUNDING edge (c107): the eigenmode driver wires the divergence-free projector into the eigensolver (`eigen->SetDivFreeProjector(*divfree)` eigensolver.cpp:233; the initial starting vector projected `divfree->Mult(v0)` :262) to keep eigenvectors in the divergence-free subspace — a genuine directly-wired absorbed constituent of this pipeline (highest entry L3; no L4 entry by the constructed-operator-gate verdict). Grounds the firm-but-absorbed divfree-projector cluster (and its step-2 set_subvector_zero) from this root.
    - target: palace/drivers/eigensolver.cpp:32-477
      kind: cites-evidence
    - target: concepts/config-record
      kind: uses-record               # input signature: eigenmode :: EigenmodeConfig -> EigenmodeResult (the IoData surface)
  reference:
    - feature/eigenfrequency-qfactor.L4
---

# eigenmode — L4 composition-root

The **eigenmode simulation feature**, presented at L4 as a single composition of firm L4 combinators — the **outward backend-lowering entry point** for the generalized-eigenproblem pipeline. This chapter is a **composition root** (a **leaf feature column** in the FEATURE-SURFACE SPINE — a per-driver surface whose stage constituents are *vocabulary ops*, not other feature columns): it does not introduce a new combinator; it wires the already-firm L4 vocabulary into the user-facing feature (config → eigenfrequencies + Q-factors + mode fields), and links DOWN to each composed piece.

Eigenmode is the **cleanest test of the composition-root pattern over a single black-box-kernel constituent**. Unlike the [electrostatic](./electrostatic.L4.md) / [magnetostatic](./magnetostatic.L4.md) fixed-operator drivers — which map a [`solve_family`](../L4/solve_family.md) over a per-source RHS family — and unlike the `driven` / `transient` drivers *(sibling feature columns; not yet authored — forward-ref by slug)* (which carry an operator/RHS family-map or a state-fold respectively), the eigenmode driver has **no operator/RHS family to map and no state-fold**: it assembles the operator pencil once, hands it to the opaque [`eigsolve`](../L4/eigsolve.md) black-box kernel **once**, and reads out the converged eigenpair set. This is recorded as the explicit non-membership at `book/src/L4/solve_family.md:146` — the eigenmode driver is **NOT** a `solve_family` / `fold_solve` witness; its only outer loop is a post-processing *readout* map over the already-converged eigenpairs (`eigensolver.cpp:424-471`). The composition is therefore the minimal shape: `assemble (×3) ▷ eigsolve ▷ readout-map`.

## The composition

At L4 the whole simulation is the composition (Haskell-style; the strawman `book/src/design/l4_calculus.md` notation):

    -- inputs = config; output = the eigenfrequency / Q-factor / mode-field set (the physical product)
    eigenmode :: EigenmodeConfig -> EigenmodeResult
    eigenmode cfg =
      let space  = nd_space cfg                              -- the Nédélec H(curl) finite-element space (readonly construction stratum)
          k      = fe_assemble space [ curl_curl (reluctivity cfg) ]   -- (1a) assemble K ONCE  ── L4/fe_assemble (firm)
          c      = fe_assemble space [ conductivity_term cfg ]         -- (1b) assemble C ONCE (damping; may be empty) ── L4/fe_assemble
          m      = fe_assemble space [ mass_term (permittivity cfg) ]  -- (1c) assemble M ONCE  ── L4/fe_assemble (firm)
          pencil = eig_pencil k c m (target cfg) (n_modes cfg)         -- the (K, C, M) operator pencil + spectral-transform target
          eigs   = eigsolve pencil (initial_space cfg)                 -- (2) ONE opaque black-box eigen-solve ── L4/eigsolve (firm)
      in  map (readout cfg) eigs                                       -- (3) per-mode readout map → ω, Q, B = -1/(iω)∇×E

Three composed stages, each a link DOWN to firm L4 vocabulary:

1. **Assemble the operator pencil once** — [`fe_assemble`](../L4/fe_assemble.md) (**firm**), applied three times to build the generalized-eigenproblem matrix pencil `(K, C, M)`. The L4 assemble-fold combinator `fe_assemble space terms = sum (map (assemble_term space) terms)` folds each operator's weak-form term list into a global operator: `K` (the curl-curl stiffness, `DIAG_ONE` for the PEC-dof Dirichlet shift), `C` (the damping/conductivity matrix, possibly empty → the linear-EVP branch), and `M` (the mass matrix, `DIAG_ZERO`). `space` (the Nédélec H(curl) space) is the `readonly` construction stratum captured once across all three assembles. The damping matrix `C` being empty is the load-bearing problem-type axis (see Variant axes): `C = ∅ ⇒` linear EVP `K x = ω² M x`; `C ≠ ∅ ⇒` quadratic EVP `(K + λC + λ²M) x = 0`. L0: `auto K = space_op.GetStiffnessMatrix<ComplexOperator>(Operator::DIAG_ONE)` / `GetDampingMatrix` / `GetMassMatrix` (`palace/drivers/eigensolver.cpp:40-42`).

2. **One opaque black-box eigen-solve** — [`eigsolve`](../L4/eigsolve.md) (**firm**). This is the **black-box-kernel constituent** (per the directive `project_blackbox_vs_accelerated_kernels`: an opaque/special op with a clean surface and non-local iterative behaviour RISES to L4 as an opaque-surface primitive — the positive reframe of "opaque-library obstruction"). The L4 `eigsolve` cap is a role-naming `Outcome`-wrapper over the entire eigen-iteration, which lives inside SLEPc `EPSSolve` / ARPACK `naupd` RCI — Palace authors **no** eigen-iteration loop, so the cap names the iteration by role and marks the obstruction rather than rendering a Palace-authored loop (see [`L4/eigsolve`](../L4/eigsolve.md) §Context). The cap is called **exactly once**: the whole pencil is handed to the library, which returns the converged eigenpair set. There is no `solve_family` map here (no operator/RHS family) and no `fold_solve` state-march (no value-threaded outer iteration the calculus owns) — the single black-box call IS the entire solve. L0: the per-mode `SetOperators` pencil setup at `eigensolver.cpp:172-196`, the single `int num_conv = eigen->Solve()` at `:367`.

3. **Per-mode readout map → the physical product** — a pure `map` over the already-converged eigenpair set, recovering each mode's physical observables: the eigenfrequency `ω` (recovered from the eigenvalue by the problem-type un-transform — `ω = √μ` for the linear EVP `μ = ω²`, `ω = λ/i` for the quadratic EVP `λ = iω`), the quality factor `Q` (from the complex `ω`), and the mode fields `E` (the eigenvector) + `B = -1/(iω) ∇×E` (the magnetic field from the curl of the electric eigenvector). This is the eigenmode driver's *only* outer loop — and it is a pure post-processing `map`, NOT a solve-iteration (explicitly contrasted at `book/src/L4/solve_family.md:146`). The eigenfrequency / Q-factor reduction into the user-facing **output product** is authored as its dedicated output-product feature column [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) (which links back DOWN to this driver as its producing column); this stage records only that the eigenmode driver feeds it the converged eigenpair set. L0: the readout loop `for (int i = 0; i < num_conv; i++)` at `eigensolver.cpp:424`, the eigenvalue/ω recovery `:427-439`, `eigen->GetEigenvector(i, E)` at `:443`, the field readout + `post_op.MeasureAndPrintAll(...)` at `:445-458`.

## Inputs / outputs (the feature surface)

- **Input — config.** `EigenmodeConfig`: the Nédélec H(curl) space construction (mesh + order → `nd_space`), the material coefficients (reluctivity/permittivity/conductivity → the K/C/M weak-form terms), the requested mode count + spectral-transform target (`iodata.solver.eigenmode.n` / `.target` → `eig_pencil`), and the linear-solver / divergence-free-projector configuration (→ the inner `ksp_solve` the eigen-iteration calls and the `SetDivFreeProjector`). All `readonly` construction-stratum inputs; none threads mutably through the composition. L0 home: `SpaceOperator space_op(iodata, mesh)` (`eigensolver.cpp:39`) — `iodata` is the config surface.
- **Output — the physical product.** `EigenmodeResult` — the set of converged modes, each carrying its eigenfrequency `ω`, quality factor `Q`, and mode fields `(E, B)`. This is what the user ran the eigenmode solver to compute. The eigenfrequency / Q reduction into the reported product is owned by the [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) output-product column. L0 home: the per-mode `omega` / `E` / `B` measured by `post_op.MeasureAndPrintAll(i, E, B, omega, error_abs, error_bkwd, num_conv)` (`eigensolver.cpp:458`).

## Why this composes cleanly (the minimal composition root)

The eigenmode feature is the **cleanest** composition-root test because its body is the shortest: a single black-box-kernel constituent flanked by an assemble-fold and a pure readout-map, with **no outer solve-loop the calculus has to own**.

- The assemble is three single-term `fe_assemble` folds (the K/C/M pencil) — `space` captured once, the three operators built once.
- The solve is **one** [`eigsolve`](../L4/eigsolve.md) black-box call — there is no `solve_family` map (no RHS family) and no `fold_solve` (no state-threaded march). The non-membership is the load-bearing fact: where the other drivers compose an outer-iteration combinator, eigenmode composes a single opaque primitive. This is why it is the cleanest test of the pattern over a single black-box constituent + assemble.
- The readout is a pure `map` over the converged eigenpairs — a post-processing fold, explicitly NOT a solve-iteration (`book/src/L4/solve_family.md:146`).

The whole feature therefore lowers cleanly outward to the L4 backend surface: `eigenmode = map readout ∘ eigsolve ∘ eig_pencil ∘ (fe_assemble ×3)`. Both directly-composed combinators ([`fe_assemble`](../L4/fe_assemble.md), [`eigsolve`](../L4/eigsolve.md)) are **firm**, so under the OWN-COMPOSITION promotion rule (a column promotes off `seed` when its OWN composition + directly-owned constituents are firm; cross-linked sibling columns are references, NOT blockers) this column **promotes to `firm`**. The stage-(3) reduction into the [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) output-product column is a **sibling cross-link** (a reference / drift-guard), not a directly-owned constituent — it does NOT gate this driver column's promotion. (That column itself promotes independently on its own firm reduce verb `eigenfreq_qfactor_reduce`, firm cycle-082; the former mutual-blocking deadlock between the two — each citing the other's `seed` state — is exactly what the directive retires.) This is the test the FEATURE-SURFACE SPINE directive sets for pulling a feature up: it advances cleanly because the directly-owned constituent vocabulary is firm and composes without forcing the spine.

## Variant axes

Two axes shape the eigenmode composition; both are absorbed into the pencil-construction / cap, not into the composition shape:

1. **problem-type** (`linear EVP | quadratic EVP | nonlinear EVP`) — selects which operators the pencil carries and how the eigenvalue un-transforms to `ω`. `linear` (`C = ∅`, `K x = ω²M x`, `ω = √μ`); `quadratic` (`C ≠ ∅`, `(K + λC + λ²M)x = 0`, `ω = λ/i`); `nonlinear` (the `A2(ω)` extra-system-matrix branch, `funcA2`). Absorbed into `eig_pencil` + the [`eigsolve`](../L4/eigsolve.md) cap's `problem-type` axis. L0: the `SetOperators` dispatch (`eigensolver.cpp:172-196`), the `ω` recovery branch (`:430-439`).
2. **spectral-transformation** (`none | shift-invert | shift-invert-precond`) — selects the target the eigen-iteration drives toward. Absorbed into `eig_pencil (target cfg)` + the [`eigsolve`](../L4/eigsolve.md) cap's `spectral-transformation` axis. Not part of the composition shape — the single black-box call subsumes it.

## Constituent down-links

| Stage | L4 combinator | Status | L0 site |
|---|---|---|---|
| assemble K/C/M pencil once | [`fe_assemble`](../L4/fe_assemble.md) | firm | `eigensolver.cpp:40-42` |
| opaque eigen-solve (once) | [`eigsolve`](../L4/eigsolve.md) | firm | `eigensolver.cpp:172-196, 367` |
| per-mode readout (ω, Q, B=-1/(iω)∇×E) | [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) output-product column (sibling reference) | firm | `eigensolver.cpp:424-458` |

## Status

`firm` — the third per-driver feature-surface composition-root (a **leaf feature column**) authored under the FEATURE-SURFACE SPINE directive (2026-06-02), and the **cleanest test of the composition-root pattern over a single black-box-kernel constituent + assemble** (per the dispatch scope). **Promoted `seed → firm` cycle-085** under the OWN-COMPOSITION promotion rule (CLAUDE.md §Extraction-goal FEATURE-SURFACE SPINE; memory `project_feature_column_promotion_rule`): a column promotes off `seed` when its OWN composition + directly-owned constituents are firm, and cross-linked sibling columns are references, NOT blockers. Both directly-owned constituents are firm: stage (1) is three single-term [`fe_assemble`](../L4/fe_assemble.md) folds (the K/C/M pencil, firm), stage (2) is exactly one [`eigsolve`](../L4/eigsolve.md) black-box call (firm) — with NO `solve_family` map and NO `fold_solve` state-march (the explicit non-membership at `book/src/L4/solve_family.md:146`), the load-bearing structural fact that makes this the minimal composition shape. Stage (3) is a pure per-mode readout `map`; its reduction into the user-facing eigenfrequency/Q-factor product is owned by the [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) output-product column — a **sibling cross-link (a reference), NOT a directly-owned constituent**, so it does NOT gate this column's promotion (that column promotes independently on its own firm `eigenfreq_qfactor_reduce` verb, firm cycle-082; the former mutual-blocking deadlock between the two columns is exactly what the directive retires). This chapter carries the *compositional* claim (eigenmode = this composition of these constituent pieces), not the constituents' per-op algebraic claims (those live in the linked chapters). Evidence: the L0 driver range `eigensolver.cpp:32-477` (`EigenSolver::Solve`) realizing the composition, all anchors confirmed on-disk via palace-codemap `read_range`, plus the firm constituent down-links.
