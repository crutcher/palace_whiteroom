# Master outline — *Tensor-Field Simulation: How the Synthesis Surface Simulates Its Targets*

An illustrated LaTeX textbook (memoir class, TikZ illustrations).
**Target: a reference-grade work, ≈ 1000–1200 pages** (user directive 2026-06-09: "deep + even
more chapters"). Audience: **college sophomore** math + engineering (vector calculus, linear
algebra, ODEs; basic E&M). No prior functional programming, monads, or type theory assumed — the
book teaches them.

> **Depth calibration (load-bearing for every authoring agent).** Part I (Orientation, Ch 1–4) is
> a deliberately concise *overview* (~8 pp/chapter). **Every chapter in Parts II–VI and the
> appendices is a DEEP chapter: ~22–35 pp**, which means: derive results, don't just state them;
> 4–8 TikZ/pgfplots figures per chapter; ≥2 fully worked numerical examples per chapter (small
> enough to check by hand); exercises; and a "Further reading" with real citations. When in doubt,
> go deeper and add a figure. The material (FEM for Maxwell, Krylov/eigensolvers/multigrid, the
> calculus) easily fills this; the orientation chapters' brevity is the exception, not the model.

This file is BOTH the structural plan and the per-chapter **authoring brief** (each chapter
lists its content + source files in `book/src/**` + figure list). Authoring agents read the
relevant section here + the named source files. The four survey content-maps that ground this
live in the dispatch record (synthesis surface; feature/drivers; framework calculus; field
theory + numerics).

## The book's spine (one sentence)

Every simulation Palace runs is the same skeleton — **assemble operators → solve → reduce to a
physical product** — overlaid on a small calculus of immutable tensors and combinators; the book
teaches that calculus, the field theory it discretizes, the numerical machinery it runs, and the
six physical analyses it composes, then shows the whole thing as one synthesized library.

## Three recurring "hero" structures (teach early, reuse everywhere)

1. **The skeleton** `config → mesh → assemble → solve → reduce → product` (+ the AMR outer fold).
2. **The four solve corners**: fixed-operator map (`solve_family`), operator-varying map
   (`frequency_sweep`), state-threaded fold (`fold_solve`), opaque black-box (`eigsolve`).
3. **The de Rham complex** `H1 --grad--> H(curl) --curl--> H(div) --div--> L2`.

## Conventions

- **Pseudo-language** = the L4 notation (Haskell `::` signatures + TypeScript `{field: type}`
  records + do-notation), rendered in the `l4` listings environment (NOT math mode — the `$S`
  shape-group sigil is literal there). Authoritative semantics live in `book/src/semantics/index.md`.
- **Math** in LaTeX math mode; **figures** in TikZ/pgfplots via `style/simtikz.sty`.
- Custom environments (in `style/simbook.sty`): `definition`, `theorem`, `lemma`, `example`,
  `workedexample` (boxed), `keyidea` (boxed sidebar), `pitfall` (boxed warning),
  `notation` (margin/inline note), `physicsbox` (physical-setup anchor).
- Each chapter opens with a short "Where we are / what you'll get" paragraph and closes with a
  "Summary" + "Further reading" + a handful of exercises.

---

# EXPANDED CHAPTER MAP (reference-grade; the live structure)

This supersedes the original part lists' *granularity* (the detailed prose briefs further below
remain valid CONTENT guides — the expanded chapters subdivide them). ~49 main chapters + 7
appendices. `[DONE]` = authored + compiling. Labels in `()`. Each non-Part-I chapter is a DEEP
chapter per the calibration note above.

**Front matter** — preface `[DONE]`, how-to-read `[DONE]`, notation primer `[DONE]`.

**Part I — Orientation (concise overview) `[DONE]`**
1. The Simulator and Its Targets `(ch:targets)` `[DONE]`
2. A Simulation's Life Cycle `(ch:lifecycle)` `[DONE]`
3. The Big Idea: Tensor-Field Simulation `(ch:bigidea)` `[DONE]`
4. Situating the Drivers on the Framework `(ch:situating)` `[DONE]`

**Part II — The Field Theory** (sources: `book/src/L1/weak_form_term.md`, `fe_assemble.md`,
`fe_space.md`, `fe_collection.md`, `interpolator.md`, `divfree_projector.md`, `L3/divfree_projector.md`,
`element_restrict.md`, `basis_apply.md`, `quad_point_contract.md`, `geom_factor_build.md`,
`libceed-quadrature-kernel-impl.md`, `build_mesh.md`, `concepts/element-local-tensor.md`,
`eliminate_essential_bc.md`, `eliminate_rhs.md`; physics is connective from sophomore vector calc)
5. Maxwell's Equations: A Working Review `(ch:maxwell)`
6. The Five Reductions of Maxwell `(ch:reductions-pde)` — static/eigen/driven/transient PDEs derived
7. From Strong to Weak: Integration by Parts `(ch:weak)`
8. Galerkin's Method and the Bilinear-Form Family `(ch:galerkin)` — `a(u,v)=(Q\diffop u,\diffop v)`
9. The Finite-Element Function Spaces `(ch:functionspaces)` — H1/H(curl)/H(div)/L2, DoFs, conformity
10. The de Rham Complex and Discrete Exactness `(ch:derham)` — hero diagram
11. Reference Elements, Basis Functions, and Quadrature `(ch:refelement)`
12. Assembly as a Fold `(ch:assembly)` — element→global; commutative-monoid sum over weak-form terms
13. The Matrix-Free Operator `(ch:matrixfree)` — `G·B·D·Bᵀ·Gᵀ`, element-local tensor anatomy
14. Boundary Conditions and the Helmholtz Decomposition `(ch:bc)`

**Part III — The Abstract Framework** (sources: `book/src/semantics/index.md`, `L4/index.md` +
intros, `L4/{iterate_while,krylov_step,fold_solve,ksp_solve}.md`, `concepts/{rotation,tensor-field-lift,
solve-monad,state-stratification,build-time-vs-run-time-stratification,capability-typing,
constructed-operators,constructed-operator-factory,solver-as-operator,variant-absorption,
scalar-promotion,SimState,OpParams,SolveResult,StepOutputs,PrevCarry,erasure-scope}.md`)
15. A Language for Computations: Values and Functions `(ch:language)`
16. Records and Immutability `(ch:records)`
17. Tensors and Shapes `(ch:tensors)`
18. Named Shape Groups and Rank-Agnostic Congruence `(ch:shapes)`
19. The Fold: `iterate_while` and the Iteration Combinators `(ch:fold)`
20. Maps, Folds, and the Combinator-Primary Model `(ch:combinators)`
21. Modeling Mutation Purely: The State Monad `(ch:monad)`
22. State Stratification and Lifetimes `(ch:strata)`
23. Operators as Values: Constructed Operators & Capability Typing `(ch:operators)`
24. The Layered View: Rotations and Representations `(ch:rotations)`

**Part IV — The Numerical Machinery** (sources: `book/src/concepts/{krylov,gmres,plane-rotation-stream,
givens,givens_generate,givens_apply,eigsolve}.md`, `L3/{krylov_step,eigsolve,eigsolve-impl,lanczos_step,
nleps-deflated-eigensolve,chebyshev,fold_solve}.md`, `L1/{ksp_solve,orthogonalize,jacobi-smoother,
chebyshev-smoother,multigrid-relaxation-smoother,dorfler_mark,flux_recovery_estimate,fe_space_hierarchy}.md`,
`L2/incremental_least_squares.md`, `feature/geometric-multigrid-preconditioner.L1.md`,
`L4/{domain_energy_reduce,gram_reduce,sparameter_reduce,eigenfreq_qfactor_reduce,waveguide_mode_reduce}.md`)
25. Sparse Linear Systems and Krylov Subspaces `(ch:krylov)`
26. Conjugate Gradients `(ch:cg)`
27. GMRES and FGMRES `(ch:gmres)`
28. Orthogonalization: Arnoldi, Lanczos, Gram–Schmidt `(ch:orthog)`
29. The Least-Squares Core: Givens Rotations and the Running QR `(ch:givens)`
30. Preconditioning `(ch:precond)`
31. Smoothers: Jacobi, Chebyshev, Hiptmair `(ch:smoothers)`
32. Geometric Multigrid: The V-Cycle `(ch:multigrid)`
33. Eigenvalue Problems and Spectral Transforms `(ch:eigenvalues)`
34. Lanczos, Arnoldi, and Krylov–Schur `(ch:krylovschur)`
35. Deflation and Nonlinear Eigenproblems `(ch:deflation)`
36. Time Integration `(ch:time)`
37. Adaptive Mesh Refinement `(ch:amr)`
38. Output Reductions: From Fields to Physical Quantities `(ch:reductions)`

**Part V — The Constituent Modalities** (sources: the six `book/src/feature/<driver>.{L4,L1,L0}.md`
+ the matching Palace drivers)
39. Electrostatics and Capacitance `(ch:electrostatics)` — the anchor; full end-to-end trace
40. Magnetostatics and Inductance `(ch:magnetostatics)`
41. Eigenmodes: Resonant Frequencies and Q `(ch:eigenmodes)`
42. Driven Simulations and S-Parameters `(ch:driven)`
43. Transient Simulations `(ch:transient)`
44. Wave Ports and Boundary Modes `(ch:waveports)`
45. Assembling a Driver: A Complete Worked Trace `(ch:fulltrace)`

**Part VI — The Collection** (sources: `book/src/synthesis/{index,types,iteration,data-algebra,
coordination,drivers}.md`)
46. The Synthesized Library: Architecture `(ch:synthlib)`
47. A Tour of the Five Libraries `(ch:fivelibs)`
48. Composing a Driver, End to End `(ch:composing)`
49. The Whole Machine, and Where It Goes Next `(ch:wholemachine)`

**Appendices — Deep Computation Semantics** (sources: `book/src/semantics/index.md` §1,§3,§4,§5;
per-`L4/*` law sections; `CLAUDE.md` §Optimization-tricks; the matrix-free L1 chapters)
- A. The Formal Calculus: Grammar and Reduction Rules `(app:calculus)`
- B. Types, Shapes, and the Shape Algebra `(app:shapes)`
- C. Monad and Algebraic Laws `(app:laws)`
- D. Numerical and Floating-Point Semantics `(app:numerics)`
- E. The Matrix-Free Kernel in Detail `(app:kernel)`
- F. The Layered Stack: A Reference Map `(app:stack)`
- G. Symbol Glossary + Index `(app:glossary)`

**Cadence:** build part by part; fan out chapters per part (waves of ~5); compile + integrate each
wave; present at each part boundary. The detailed CONTENT briefs for each topic remain below.

---

# Page budget (≈ 800 pp)

| Part | Title | Pages |
|---|---|---|
| Front matter | titles, preface, how-to-read, notation primer, ToC/figures | ~28 |
| I | Orientation — what the simulator computes and how it's built | ~90 |
| II | The Field Theory — Maxwell, weak forms, function spaces, FEM | ~150 |
| III | The Abstract Framework — mechanics of the calculus | ~150 |
| IV | The Numerical Machinery — the shared algorithmic substrate | ~165 |
| V | The Constituent Modalities — deep dives | ~140 |
| VI | The Collection — the synthesized library | ~70 |
| Appendices | Deep computation semantics (with diagrams) | ~110 |
| **Total** | | **~803** |

---

# FRONT MATTER (~28 pp)

- **Title page, copyright, dedication.**
- **Preface** (~6pp): what this book is; the three reader-views (top-down feature spine,
  bottom-up vocabulary, the synthesized-library implementation view) and which one this book
  takes (it weaves all three for teaching); why a *functional / immutable-tensor* presentation of
  a classically array-mutation simulator; what the reader will be able to do at the end.
- **How to read this book** (~6pp): audience + prerequisites checklist; dependency map of
  parts/chapters (a TikZ roadmap); the pedagogical order (immutability → higher-order functions →
  the fold → records → the monad → operators-as-values → shapes → rotations); how worked examples /
  boxes are used.
- **A notation primer** (~10pp): reading the pseudo-language (`::`, `->`, curried args, records,
  `do`, `let`, list comprehensions, `foldl`/`foldr`/`map`); math notation + symbol conventions;
  the shape notation `Tensor[...]` (full treatment deferred to Ch 11); units (SI). Symbol glossary
  table. Source: `book/src/semantics/index.md` §1; `concepts/*` for record shapes.
- ToC, list of figures, list of worked examples.

---

# PART I — ORIENTATION (~90 pp)
*Goal: a reader finishes Part I able to say, for any of the six analyses, "it computes X by
assembling Y, solving Z, reducing to W," and recognizes the shared skeleton + four solve corners.*

### Ch 1. The Simulator and Its Targets (~22pp) — **EXEMPLAR CHAPTER (sets voice + TikZ style)**
- What an EM field simulator is; Palace in one paragraph; the user's-eye view (config in →
  physical product out).
- A guided tour of the **six analyses** with a physical-setup sketch + the quantity each yields:
  electrostatic→capacitance (capacitor), magnetostatic→inductance (coil), eigenmode→resonant
  frequencies+Q (cavity), driven→S-parameters (2-port microwave network), transient→time-domain
  fields (injected pulse), boundary-mode→waveguide propagation modes (waveguide cross-section).
- The promise: all six are the *same machine* with parts swapped (forward-reference to the
  skeleton + corners).
- Figures: 6 physical-setup TikZ sketches; a "config → simulator → product" black-box diagram; a
  table of (analysis, physical question, governing PDE, FE space, product).
- Source: `feature/index.md`, the six `feature/<driver>.L0.md`, `output-product.md`.

### Ch 2. A Simulation's Life Cycle: The Top-Level Driver (~22pp)
- `main → parse config → configure device → dispatch on problem type → build mesh → Solve →
  estimate-mark-refine fold → output`. What flows between stages (config read-only; mesh; solution;
  error indicators; product).
- The `ProblemType` dispatch as the "specialization seam" (one switch → six drivers).
- The adaptive outer loop as a fold (degenerates to a single solve when AMR is off) — first sight
  of `fold_solve`.
- Figures: the master lifecycle pipeline (with the AMR back-edge); the dispatch fan-out.
- Source: `feature/spine-root.md`, `feature/lifecycle.{L4,L1,L0}.md`; Palace `main.cpp`,
  `basesolver.cpp`.

### Ch 3. The Big Idea: Tensor-Field Simulation (~24pp)
- Fields as **tensors** (discretized degrees of freedom); a simulation as transformations of
  immutable tensors.
- The mental shift: from in-place array mutation (the C/Fortran picture the reader may have) to
  **pure functions over immutable values** + **combinators**. Why: clarity, composability, and the
  GPU/parallel backend (the "implementation VIEW").
- A gentle first look at the calculus's three structural questions (what ops happen / who owns
  state / how evolution is coordinated) — full treatment in Part III.
- Figures: array-mutation vs value-threading side-by-side; a tensor as a labeled box of axes; the
  "same algorithm, two memory models" picture.
- Source: `concepts/tensor-field-lift.md`, `L4/index.md`, `semantics/index.md` §6 (LBM idea, light).

### Ch 4. Situating the Drivers on the Framework (~22pp)
- The **skeleton** made explicit; the **four solve corners** (fixed-map / varying-map / fold /
  black-box) with one-line exemplars; the **three reduction shapes** (Gram / port-projection /
  scalar-or-mode table).
- The driver-vs-framework map (rows = drivers; cols = FE space, assemble, solve corner, reduction,
  product) — the table the rest of the book fills in.
- Figures: the four-corners classification; the driver×framework grid; "electrostatic is the
  universal entry point, everything else swaps one stage."
- Source: `feature/*.L4.md` (composition roots), `synthesis/drivers.md` (composition shapes).

---

# PART II — THE FIELD THEORY (~150 pp)
*Goal: build, from sophomore vector calculus + linear algebra, the continuous physics and its
finite-element discretization that the framework operates on. The spec starts at the discretized
operators; this part supplies the Maxwell→weak-form→FEM ladder and lands exactly on the operators
the drivers assemble.*

### Ch 5. Maxwell's Equations and Their Reductions (~30pp)
- Maxwell's equations (review); constitutive relations (ε, μ, σ); the static / time-harmonic /
  time-domain regimes.
- The five reductions: electrostatic (Laplace/Poisson `−∇·(ε∇V)=ρ`), magnetostatic (curl-curl
  `∇×(ν∇×A)=J`), eigenmode (`K x=λM x`), driven (`(K+iωC−ω²M)E=b`), transient (`Ms''+Cs'+Ks=J(t)`).
- Figures: the Maxwell→5-reductions tree; regime map (static/harmonic/transient).
- Source: derived/connective (spec starts post-discretization); landing operators in
  `L1/weak_form_term.md`, the driver `*.L0.md` files; Palace `laplaceoperator.cpp`,
  `curlcurloperator.cpp`, `spaceoperator.cpp`.

### Ch 6. From Strong to Weak: Variational Formulation (~28pp)
- Integration by parts / Green's identities; the weak form; the Galerkin method; existence/
  uniqueness intuition (coercivity, inf-sup — lightly).
- The unifying bilinear-form family `a(u,v) = (Q·𝒟u, 𝒟v)_Ω` (𝒟 ∈ {value, grad, curl, div}).
- Boundary conditions: essential (Dirichlet) vs natural; how each enters.
- Worked example: weak form of the electrostatic problem.
- Figures: IBP picture; the four `a(u,v)` forms in one table.
- Source: `L1/weak_form_term.md`, `L1/fe_assemble.md`.

### Ch 7. Function Spaces and the de Rham Complex (~32pp) — **hero diagram lives here**
- `H1, H(curl), H(div), L2`; nodal/edge/face/volume DoFs; conformity (what's continuous across
  faces).
- The **de Rham complex** `H1 --grad--> H(curl) --curl--> H(div) --div--> L2`; discrete exactness
  `curl∘grad=0`, `div∘curl=0`; why each PDE lives on its slot (scalar potential in H1; vector
  potential/E-field in H(curl)).
- The `FECollection` family (`H1_/ND_/RT_/L2_FECollection`) + p-multigrid order schedule.
- Figures: the de Rham complex (hero); reference element + basis functions per family (nodal
  Lagrange, Nédélec edge, RT face, L2).
- Source: `L1/fe_space.md`, `fe_collection.md`, `interpolator.md`, `divfree_projector.md`.

### Ch 8. The Finite Element Method: Discretization and Assembly (~38pp)
- Reference element → shape functions → quadrature → element matrices → global assembly (the
  gather/scatter); meshes & true DoFs.
- Assembly **as a fold (sum) over weak-form terms**; commutative-monoid structure.
- The **matrix-free pipeline** `A = Gᵀ∘B_𝒟ᵀ∘D∘B_𝒟∘G` (concept + the burn/GPU motivation); the
  element-local tensor anatomy (axes E/L/P/C/G); sum-factorization as a transparent perf trick.
- Worked example: assemble the diffusion stiffness on one triangle, then show the contraction
  factoring reproduces it.
- Figures: element→global gather/scatter with assembly multiplicity; the 5-stage matrix-free pipe.
- Source: `L1/fe_assemble.md`, `element_restrict.md`, `basis_apply.md`, `quad_point_contract.md`,
  `geom_factor_build.md`, `libceed-quadrature-kernel-impl.md`, `concepts/element-local-tensor.md`,
  `L1/build_mesh.md`. (Deepest contraction detail → App E.)

### Ch 9. Boundary Conditions and Keeping Fields Physical (~22pp)
- Essential-dof elimination (`eliminate_essential_bc`) + inhomogeneous lifting into the RHS
  (`eliminate_rhs`) as separable post-compositions on the assembled operator.
- The discrete Helmholtz decomposition + divergence-free projection
  `P = I − Grad(GᵀMG)⁻¹GᵀM`; why it keeps eigenvectors physical.
- Figures: BC elimination on the DoF set; Helmholtz decomposition (field = divfree + gradient).
- Source: `L1/eliminate_essential_bc.md`, `eliminate_rhs.md`, `L1/divfree_projector.md`,
  `L3/divfree_projector.md`.

---

# PART III — THE ABSTRACT FRAMEWORK: MECHANICS OF THE CALCULUS (~150 pp)
*Goal: teach the L4 calculus from zero FP background — values, higher-order functions, the fold,
records, the state monad, operators-as-values, shapes, and the layered "rotation" idea.*

### Ch 10. A Language for Computations: Notation and Values (~26pp)
- The pseudo-language in full (signatures, records, do-notation, comprehensions); immutability &
  values ("a tensor is a value like a number; you never change it, you make a new one"); `clone()`
  evaporates; higher-order functions; the closure-returning paren convention `foo -> (bar -> baz)`.
- Figures: a value-threading ribbon; an expression tree.
- Source: `semantics/index.md` §1, §1.3; `concepts/*` records.

### Ch 11. Tensors, Shapes, and Fields (~28pp)
- The tensor model; shape expressions; **named shape groups** `Tensor[(S: ...)]` / `$S` and
  rank-agnostic congruence (and the `Tensor[N]` rank-1 anti-pattern); operator shapes
  `LinOp[(R:...),(D:...)]`; concrete named axes (E/L/P/C/G); scalar promotion `real ⊑ complex`;
  the tensor-field lift.
- Figures: shape-algebra (axis boxes, congruence brackets, `$S` back-arrow); promotion lattice.
- Source: `semantics/index.md` §1.2, §4.1; `concepts/scalar-promotion.md`, `tensor-field-lift.md`,
  `element-local-tensor.md`.

### Ch 12. The Fold: Iteration as a Combinator (~30pp) — **keystone chapter**
- Iteration-as-recursion; `iterate_while` (the while convention, predicate-pure-on-carry, the
  predicate-on-extras pitfall); `iterate_while_with_prev`; `iterate_while_pure`; demand-pruned
  trajectories; maps & folds (`solve_family`, `fold_solve`) as specializations; combinator-primary.
- Worked example: Newton's method / fixed-point as `iterate_while`; preview of `krylov_step`.
- Figures: a fold unrolling with the trajectory + demand-pruning; map vs fold vs single-call.
- Source: `semantics/index.md` §3.7–3.8; `L4/iterate_while.md`, `iterate_while_with_prev.md`,
  `L4/iteration-combinators-intro.md`.

### Ch 13. Modeling Mutation Purely: State Monads (~32pp)
- The `Solve = StateT SimState Identity` monad (taught concretely, NOT category-theoretically);
  the single `modify it` effect point; `execState` discharge; **state stratification** (SimState /
  OpParams / ephemeral Krylov / scalar-recurrence) with lifetimes; build-time vs run-time; the LBM
  "mutation → pure record threading" worked example.
- Figures: the state-monad threading ribbon with the single write-point; the strata as nested
  lifetimes.
- Source: `concepts/solve-monad.md`, `state-stratification.md`,
  `build-time-vs-run-time-stratification.md`, `SimState.md`, `SolveResult.md` (the Solve overload),
  `semantics/index.md` §2, §6.

### Ch 14. Operators as Values: Constructed Operators & Capability Typing (~30pp)
- Constructed operators (build-once/apply-many; the construction/application phase split);
  solver-as-operator (an approximate inverse IS an operator); the constructed-operator factory;
  capability typing (role-branding, phantom types, zero runtime); variant absorption (three levels;
  the silent-partial-absorption anti-pattern); the per-step-flexible case that defeats
  constructed-operators (FGMRES).
- Figures: construction→apply phase split; capability brands vs variant axes.
- Source: `concepts/constructed-operators.md`, `constructed-operator-factory.md`,
  `solver-as-operator.md`, `capability-typing.md`, `variant-absorption.md`,
  `L4/preconditioning-framework.md`.

### Ch 15. The Layered View: Rotations and Representations (~24pp)
- The **rotation** idea (re-expressing work while turning one impedance); the three rotation tests
  (state hiding / coarser substitution / threaded-state compression) and the renaming smell; the
  L4→L0 stack as a sequence of rotations (mutation / fusion / iteration / calculus); justification
  kinds incl. obstruction as a first-class negative result; erasure-scope (brief).
- Figures: the layered-rotation stack with impedance dials; the algorithmic-substitution test.
- Source: `concepts/rotation.md`, `erasure-scope.md`, `tensor-field-lift.md`, `L4/index.md`.

---

# PART IV — THE NUMERICAL MACHINERY (~165 pp)
*Goal: the shared algorithmic substrate every modality composes — Krylov solves, preconditioning/
multigrid, eigensolvers, time integration, AMR, and output reductions — each as both classical
algorithm and framework combinator. Worked numerical micro-examples throughout.*

### Ch 16. Solving Linear Systems: Krylov Methods (~36pp)
- Sparse systems & why iterative; Krylov subspaces; CG (SPD, electrostatic/magnetostatic); GMRES/
  FGMRES (general, driven/eigen-inner); Arnoldi/Lanczos; least-squares via Givens (the running-QR
  stream, residual free as `|s[j+1]|`); restart; the `krylov_step` kernel; convergence &
  conditioning; load-bearing non-determinism (reduction-tree non-associativity).
- Worked examples: CG on a 2×2 SPD system; one Arnoldi step + Givens rotation.
- Figures: Krylov subspace growth; convergence plot (CG monotone vs GMRES min-residual vs erratic);
  the Givens/Hessenberg triangularization stream.
- Source: `concepts/krylov.md`, `gmres.md`, `plane-rotation-stream.md`, `givens*.md`;
  `L3/krylov_step.md`, `L1/ksp_solve.md`, `orthogonalize.md`, `L2/incremental_least_squares.md`.

### Ch 17. Preconditioning and Geometric Multigrid (~34pp)
- Why precondition; smoothers (Jacobi/diagonal; Chebyshev polynomial of `D⁻¹A`; Hiptmair/AMS
  distributive relaxation for H(curl)); the **V-cycle** (presmooth→restrict→recurse→prolong→
  postsmooth); the FE-space hierarchy (h/p); `correction_step` as the V-cycle leg; solver-as-
  operator in action.
- Worked example: one V-cycle on a 1-D Poisson 2-level problem.
- Figures: the V-cycle (hero); smoother spectra; the AMS auxiliary-space picture.
- Source: `feature/geometric-multigrid-preconditioner.L1.md`, `L3/chebyshev.md`,
  `L1/multigrid-relaxation-smoother.md`, `jacobi-smoother.md`, `chebyshev-smoother.md`,
  `fe_space_hierarchy.md`.

### Ch 18. Eigenvalue Problems (~34pp)
- The generalized EVP `K x=λM x` (+ quadratic PEP, nonlinear NEP); Lanczos (symmetric three-term
  recurrence, tridiagonal T, loss-of-orthogonality caveat); Arnoldi/Krylov-Schur (thick restart);
  **shift-invert** spectral transform `(K−σM)⁻¹M`; deflation; NLEPS (deflated quasi-Newton); the
  opaque-library boundary (SLEPc EPS / ARPACK own the loop) and its constructive reconstruction.
- Worked example: shift-invert on a 3-eigenvalue toy spectrum.
- Figures: shift-invert spectrum reordering; the Lanczos tridiagonalization; the opaque-kernel
  boundary with the realizes-kernel-api correspondence.
- Source: `concepts/eigsolve.md`; `L3/eigsolve.md`, `eigsolve-impl.md`, `lanczos_step.md`,
  `nleps-deflated-eigensolve.md`.

### Ch 19. Time Integration (~24pp)
- The semi-discrete 2nd-order ODE system `Ms''+Cs'+Ks=J(t)`; recast as first-order IVP; ODE
  integrators (Generalized-α, SDIRK); the **state-threaded fold** `fold_solve` (each step ← prior
  step — a sequential carry, not a map); checkpoint/resume = schedule split.
- Figures: the time-march filmstrip; fold (carry) vs map (independent) contrast.
- Source: `L4/fold_solve.md`, `L3/fold_solve.md`; `feature/transient.*`; Palace
  `timeoperator.cpp`.

### Ch 20. Adaptive Mesh Refinement (~26pp)
- The estimate→mark→refine loop as a state-generated fold; **ZZ flux recovery** error estimation
  (`η²_K=∫_K‖flux−G‖²`); **Dörfler/bulk marking** (smallest set with `Σe²≥θΣe²`); refinement
  (MFEM-opaque); convergence intuition.
- Worked example: Dörfler marking on 5 elements with θ=0.7.
- Figures: the AMR cycle; Dörfler bulk-marking on a sorted error histogram; a refined mesh.
- Source: `L1/flux_recovery_estimate.md`, `dorfler_mark.md`, `L1-L0/amr-estimate-mark-refine.md`,
  `feature/lifecycle.L0.md`.

### Ch 21. Output Reductions: From Fields to Physical Quantities (~28pp)
- Energy integrals + participation (`domain_energy_reduce`); Gram reductions for capacitance/
  inductance (`gram_reduce`, weight = 1 vs 1/(IᵢIⱼ)); port-projection for S-parameters
  (`sparameter_reduce`, why NOT a Gram); eigenfrequency+Q (`eigenfreq_qfactor_reduce`, `Q=ω/κ`);
  waveguide modes (`waveguide_mode_reduce`). The **reduction-shape taxonomy** (rank-2 Gram /
  rank-2 projection / rank-1 table).
- Worked example: 2-terminal capacitance via a 2×2 Gram.
- Figures: the three reduction shapes; the energy/participation picture.
- Source: `L4/{domain_energy_reduce,gram_reduce,sparameter_reduce,eigenfreq_qfactor_reduce,
  waveguide_mode_reduce}.md`; `feature/output-product.md` + the product `*.L0.md`.

---

# PART V — THE CONSTITUENT MODALITIES: DEEP DIVES (~140 pp)
*Goal: one chapter per analysis. Electrostatic is the anchor (full end-to-end trace); each later
chapter is "the anchor, with these stages swapped," foregrounding the modality's physics, FE space,
solve corner, and product. Heavy cross-reference to Parts II–IV.*

### Ch 22. Electrostatics and Capacitance (~30pp) — **anchor deep-dive**
- The physics (potential, capacitance, the energy form `C=2U/V²`); H1 space; assemble `K` once;
  fixed-operator `solve_family` over per-terminal unit-voltage RHS; `gram_reduce` (w=1) → C matrix.
- Full end-to-end trace (config → product), the template every later chapter mirrors.
- Source: `feature/electrostatic.{L4,L1,L0}.md`, `L4/gram_reduce.md`, Palace
  `electrostaticsolver.cpp`.

### Ch 23. Magnetostatics and Inductance (~20pp)
- "Electrostatic, but H(curl) + curl-curl `K` + current-normalized Gram weight 1/(IᵢIⱼ)"; `B=∇×A`;
  the one-change-at-a-time contrast with Ch 22.
- Source: `feature/magnetostatic.*`, `magnetostaticsolver.cpp`.

### Ch 24. Eigenmodes: Resonant Frequencies and Q (~24pp)
- The cavity resonance problem; the generalized/quadratic EVP; the opaque black-box solve corner
  (one `eigsolve` call, no Palace loop) + readout map; `eigenfreq_qfactor_reduce`; divergence-free
  projection to keep modes physical.
- Source: `feature/eigenmode.*`, `eigensolver.cpp`.

### Ch 25. Driven Simulations and S-Parameters (~26pp)
- Frequency response; `A(ω)=K+iωC−ω²M+A2(ω)`; the operator-varying map corner (`SetOperators`
  *inside* the loop) — the explicit contrast with electrostatic's hoist; port projection →
  S-matrix; uniform vs adaptive (PROM) sweep.
- Source: `feature/driven.*`, `assemble_frequency_operator.md`, `sparameter_reduce.md`,
  `drivensolver.cpp`.

### Ch 26. Transient Simulations (~20pp)
- Time-domain pulse response; the state-threaded fold corner; per-step opaque ODE step; port
  voltages/currents and energy over time.
- Source: `feature/transient.*`, `transientsolver.cpp`, `timeoperator.cpp`.

### Ch 27. Wave Ports and Boundary Modes (~20pp)
- Waveguide propagation modes; the 2D boundary-submesh extraction preface (3D→2D projection,
  material-tensor rotation); the block ND⊕H1 pencil; shift-invert eigsolve; `waveguide_mode_reduce`;
  how it feeds the driven solver's port definitions.
- Source: `feature/boundary-mode.*`, `boundarymodesolver.cpp`, `modeeigensolver.cpp`.

---

# PART VI — THE COLLECTION: THE SYNTHESIZED LIBRARY (~70 pp)
*Goal: assemble everything into the unified implementation VIEW — the synthesis surface — and show
the whole simulator as one small library of composed combinators.*

### Ch 28. The Synthesized Library: Architecture (~22pp)
- The 5-library partition (`types` ← `iteration`/`data-algebra`/`coordination` ← `drivers` ←
  `lifecycle`) and why it mirrors the three calculus doc-groups; the dependency stack; the
  implementation-VIEW vs semantics distinction; `#extern` opaque-kernel boundaries.
- Figures: the library-stack bracket; the dependency graph (depends-on vs reference edges).
- Source: `synthesis/index.md`, `synthesis/{types,iteration,data-algebra,coordination}.md`.

### Ch 29. Composing a Driver, End to End (~26pp)
- The six driver compositions in the unifying algebra (`electrostatic = gram_reduce ∘ solve_family
  ∘ fe_assemble`, …); a full traced rendering of one driver (electrostatic clean, driven rich)
  from `IoData` projection to physical product; the three coordination shapes side by side.
- Worked example: the `krylov_step` / CG flagship def rendered + explained (Form A → Form B, the
  `it` effect, `PrevCarry` threading).
- Figures: composition trees per driver; data-flow through `driven`.
- Source: `synthesis/drivers.md`, `synthesis/{iteration,coordination,data-algebra}.md`.

### Ch 30. The Whole Machine, and Where It Goes Next (~22pp)
- The lifecycle ROOT tying it together; the implementation-VIEW as the GPU/burn backend-lowering
  target; the deferred frontiers (sharding/MPI, the kernel impls); a reflective close on the
  three-views triality and the simulate-by-composition thesis.
- Source: `synthesis/drivers.md` (lifecycle), `L4/index.md`, `feature/infrastructure.md`.

---

# APPENDICES — DEEP COMPUTATION SEMANTICS (~110 pp)
*All explained with discussion + diagrams (not bare rule dumps).*

- **App A. The Formal Calculus: Grammar and Reduction Rules (~24pp)** — BNF; small-step semantics;
  operator application; the `iterate_while` rule; demand-driven pruning as graph DCE.
  Source: `semantics/index.md` §1, §3.
- **App B. Types, Shapes, and the Shape Algebra (~20pp)** — the `Γ ⊢ e:τ` judgments; the `DimExpr`
  equational theory; named-group resolution; shape side-conditions. Source: `semantics/index.md`
  §1.2, §4.
- **App C. Monad and Algebraic Laws (~20pp)** — monad laws; state-effect laws; the per-operator
  law / **non-law** catalogue (the explicit "laws that do NOT hold"). Source: `semantics/index.md`
  §3.3–3.5, §5; each `L4/*.md` §Algebraic-laws.
- **App D. Numerical and Floating-Point Semantics (~18pp)** — transparent perf tricks vs
  load-bearing numerical tricks (non-associative reductions, fast-math, mixed precision,
  deterministic vs atomic); the property each buys. Source: CLAUDE.md §Optimization-tricks; the
  per-op load-bearing-non-law notes.
- **App E. The Matrix-Free Kernel in Detail (~16pp)** — the full `G·B·D·Bᵀ·Gᵀ` contraction; the
  element-local tensor shapes; the libCEED boundary; sum-factorization cost. Source:
  `L1/libceed-quadrature-kernel-impl.md` + the five stage chapters; `concepts/element-local-tensor.md`.
- **App F. The Layered Stack: A Reference Map (~12pp)** — L4→L0, the rotation between each pair,
  obstructions catalogued. Source: `L*/index.md`, the lowering `*-intro.md`.
- **(Back matter)** Symbol glossary; bibliography; index.

---

# Authoring / build mechanics

- LaTeX: `memoir` class, `pdflatex` (+ `latexmk`), TikZ/pgfplots, `listings` for pseudocode,
  `natbib`+`bibtex` for references (biblatex/biber are not installed).
- Files: one `.tex` per chapter under `partN-.../chNN-slug.tex`, `\include`d from `main.tex`.
  Front matter + appendices likewise. Shared style in `style/simbook.sty` + `style/simtikz.sty`.
- Per-chapter authoring brief = the chapter block above + its named `book/src/**` sources.
- **Voice/quality bar set by Ch 1** (the exemplar). Authoring waves: Part by part, agents per
  chapter, compiled + integrated incrementally.
- Diagrams are first-class: every chapter carries multiple TikZ figures from its figure list.
