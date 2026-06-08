---
kind: navigational-container (synthesis library — data-algebra)
# Implementation VIEW, reference-class links only. No `rank:` — renders the
# synthesized code form of firm L4 ops; the authoritative laws/semantics live in
# the linked ../L4/<op>.md chapters. Adds no `depends-on` blocking edge.
edges:
  reference:
    - L4/data-algebra-combinators-intro
    - L4/linear_combination
    - L4/inner_product
    - L4/dot
    - L4/nrm2
    - L4/fe_assemble
    - L4/mk_matrix_free_operator
    - L4/eliminate_bc
    - L4/assemble_frequency_operator
    - L4/gram_reduce
    - L4/domain_energy_reduce
    - L4/eigenfreq_qfactor_reduce
    - L4/sparameter_reduce
    - L4/waveguide_mode_reduce
    - L4/sharding-decompose-reduce
    - concepts/dofset
    - concepts/WaveguideModeTable
    - synthesis/types
    - synthesis/index
---

# Library `data-algebra` — data-algebra combinators & named verbs

The synthesized rendering of the L4 [Data-algebra combinators & named verbs](../L4/data-algebra-combinators-intro.md) doc-group: the pure value-producing combinators (folds + reductions) and the kept named verbs the backend wants. This is the implementation VIEW — it renders the synthesized code form of each operator; the authoritative laws / semantics / shape-group conventions live in the linked `../L4/<op>.md` chapters and the [semantic surface](../semantics/index.md), which this chapter LINKS to (it does not restate them).

The defs below are in **topological order** (a def appears after everything it uses): the general folds first, then their named-verb specializations / consumers, then the operator constructor + assemble fold, the post-assembly BC pair, the per-ω assemble verb, and the reductions. The clustering types ([`DofSet`](../concepts/dofset.md), [`WaveguideModeTable`](../concepts/WaveguideModeTable.md)) are rendered immediately before their consuming operators, each bundled with its own **utility API** (constructors / accessors / predicates); the consuming operators stay in the group after the type+utility block. Cross-cutting types (`IoData` / `OpParams` / `SimState`) live in [`types`](./types.md).

## Rendering conventions

Per the [Synthesis overview](./index.md#rendering-conventions): topological def order; `#extern NAME` after the type signature for opaque kernels (libCEED quadrature in `fe_assemble` / `mk_matrix_free_operator`); deep-linked-unchanged lower artifacts inline; Haskell `where` for private helpers; code-doc per def; `$`-sigil pseudocode inside ` ```text ` fences; named shape groups for shape-generic ops; link to `../L4/<op>.md`, do not re-cite L0.

## Rendered defs

### `linear_combination` — scalar-weighted-tensor-sum fold

Renders [`L4/linear_combination`](../L4/linear_combination.md). The variadic term-list fold `Σᵢ aᵢ·tᵢ`; the four arity leaves (`scal`/`axpy`/`axpby`/`axpbypcz`) are term-list-length specializations, rendered as `where`-local readout aliases.

```text
-- The scalar-weighted-tensor-sum combinator: a pure fold over a finite
-- (Scalar, Tensor[(S: ...)]) term list, producing Σᵢ aᵢ·tᵢ. No Solve monad, no carry.
-- Laws (concatenation-homomorphism, multilinearity, permutation-invariance): see
-- ../L4/linear_combination.md §Algebraic laws.
--
-- # Arguments
--   pairs : [(Scalar, Tensor[(S: ...)])]  -- (coefficient, term) pairs; all terms congruent
--                                            on one shape group S of arbitrary rank.
-- # Returns
--   Tensor[$S]                            -- the same shape group S; `zeros $S` on the empty list.
linear_combination :: [(Scalar, Tensor[(S: ...)])] -> Tensor[$S]
linear_combination pairs = foldl (\acc (a, t) -> acc + scal a t) (zeros $S) pairs
  where
    -- the four BLAS-1 arity leaves: this combinator at a fixed term-list length
    -- (specialization notes, not co-equal ops — accelerated kernels stopped low).
    scal     a x          = linear_combination [(a, x)]
    axpy     a x y        = linear_combination [(a, x), (1, y)]
    axpby    a x b y      = linear_combination [(a, x), (b, y)]
    axpbypcz a x b y c z  = linear_combination [(a, x), (b, y), (c, z)]
```

### `inner_product` — reduce-to-scalar inner-product fold

Renders [`L4/inner_product`](../L4/inner_product.md). The whole-tensor reduction `α = ⟨x, y⟩` over the shape group `S`; the weighted member `inner_product_M` pre-applies `M` to arg-1. The per-element conjugation kernel is the unchanged lower artifact, rendered inline.

```text
-- The reduce-to-scalar inner-product combinator: a pure reduction over the shape
-- group S. Convention conjugate-linear in arg-1, linear in arg-2 (⟨x, y⟩ = xᴴ y).
-- Laws (split-additivity / shape-concatenation-homomorphism, Hermitian symmetry,
-- PSD-at-the-diagonal): see ../L4/inner_product.md §Algebraic laws.
--
-- # Arguments
--   x : Tensor[(S: ...)]   -- the conjugated (arg-1) operand
--   y : Tensor[$S]         -- the linear (arg-2) operand; same shape group + element type as x
-- # Returns
--   Scalar                 -- the reduced inner product; `zero` on the empty tensor.
inner_product   :: Tensor[(S: ...)] -> Tensor[$S] -> Scalar
inner_product_M :: Tensor[(S: ...)] -> LinOp[$S, $S] -> Tensor[$S] -> Scalar

inner_product   x y   = reduce (+) zero (zipWith kernel x y)
inner_product_M x M y = inner_product (apply_linop M x) y    -- weighted ≡ pre-apply M to arg-1
inner_product   x y   = inner_product_M x I y                -- plain ≡ M = I
  where
    -- per-element conjugation × element-type kernel (the unchanged lower artifact,
    -- rendered inline — it IS the implementation):
    --   real    : x[idx] · y[idx]          (bilinear symmetric; conjugation a no-op)
    --   complex : conj(x[idx]) · y[idx]    (Hermitian sesquilinear; arg-1 conjugated)
    kernel xi yi = conj_if_complex xi * yi
```

### `dot` — Hermitian/symmetric inner-product verb

Renders [`L4/dot`](../L4/dot.md). The kept named verb: `inner_product` at `M = I` with the Hermitian/symmetric kernel; `tdot` is the unconjugated complex-only co-variant. A permitted dual (named specialization re-expressed THROUGH the rising combinator).

```text
-- The Hermitian/symmetric inner-product verb: the named unit a CG/GMRES description
-- writes as dot(p, Ap). It IS inner_product at M = I.
-- Laws read at M = I; see ../L4/dot.md §Algebraic laws.
--
-- # Arguments
--   x : Tensor[(S: ...)]   -- conjugated (arg-1) operand
--   y : Tensor[$S]         -- linear (arg-2) operand
-- # Returns
--   Scalar                 -- ⟨x, y⟩ (Hermitian, complex / symmetric, real)
dot  :: Tensor[(S: ...)] -> Tensor[$S] -> Scalar
tdot :: Tensor[(S: ...)] -> Tensor[$S] -> Scalar     -- unconjugated complex-only co-variant

dot  x y = inner_product x y                          -- Hermitian (complex) / symmetric (real); M = I
tdot x y = inner_product x y  -- with unconjugated kernel (the conjugation-axis second value)
```

### `nrm2` — Euclidean-norm verb (CONSUMER of `inner_product`)

Renders [`L4/nrm2`](../L4/nrm2.md). The kept named verb `‖x‖₂ = √⟨x, x⟩`; a **consumer** of `inner_product` at the diagonal post-composed with `√ ∘ abs`, NOT a fold member (the do-NOT-merge guard). The `abs` is the load-bearing defensive non-negativity guard, preserved as an explicit part of the scalar map.

```text
-- The Euclidean-norm verb: √ ∘ abs ∘ inner_product at the diagonal y = x.
-- A CONSUMER of inner_product, not a fold member (split-additivity lost under √).
-- The `abs` is the defensive non-negativity guard (round-off domain-safety for √).
-- Laws (non-negativity, absolute homogeneity, triangle inequality): see ../L4/nrm2.md.
--
-- # Arguments
--   x : Tensor[(S: ...)]   -- the single operand (shape group S, arbitrary rank)
-- # Returns
--   Scalar                 -- always real-valued and non-negative; `zero` on the empty tensor.
nrm2 :: Tensor[(S: ...)] -> Scalar
nrm2 x = sqrt (abs (inner_product x x))
```

### `mk_matrix_free_operator` — matrix-free operator constructor

Renders [`L4/mk_matrix_free_operator`](../L4/mk_matrix_free_operator.md). The backend-lowering operator-constructor for the un-materialized (partial matrix-free) FE linear operator; its `apply` is the five-stage contraction chain (the firm [`L2/matrix-free-operator-apply`](../L2/matrix-free-operator-apply.md), rendered inline as the unchanged lower artifact). The codomain is the operator-VALUE spelling `Op[τ_in → τ_out]` ([semantics §1.3.1](../semantics/index.md)).

```text
-- The matrix-free (un-materialized) FE linear-operator constructor. Builds an operator
-- VALUE (a closure carrying closed-over params) whose `apply` is a tensor-contraction
-- graph, not a CSR spmv — the partial matrix-free (UseFullAssembly-false) branch.
-- The operator-VALUE codomain Op[τ_in → τ_out] makes the higher-order intent explicit
-- (semantics/index.md §1.3.1). See ../L4/mk_matrix_free_operator.md.
--
-- # Arguments
--   space : FESpace          -- the FE space (the readonly construction stratum fe_assemble captures once)
--   term  : WeakFormTerm     -- (Q, 𝒟): coefficient Q + differential operator 𝒟; selects the basis EvalMode B_𝒟
--   geom  : GeomFactors      -- the build-stratum [E, P, G] geometry-factor carrier
-- # Returns
--   Op[Tensor[(N: ...)] → Tensor[(N: ...)]]   -- an operator instance closing over [space, term, geom];
--                                                its body lambda is the un-materialized contraction chain.
mk_matrix_free_operator :: FESpace -> WeakFormTerm -> GeomFactors
                        -> Op[Tensor[(N: ...)] → Tensor[(N: ...)]]
mk_matrix_free_operator space term geom = mkOp (\v -> apply_chain v)
  where
    -- apply is the firm L2 contraction chain A = Gᵀ ∘ B_𝒟ᵀ ∘ D ∘ B_𝒟 ∘ G
    -- (the unchanged lower artifact, rendered inline; see ../L2/matrix-free-operator-apply.md):
    --   G  / Gᵀ  : element_restrict     -- [(N: ...)] ↔ [E, L] gather / scatter-add
    --   B_𝒟/ B_𝒟ᵀ: basis_apply         -- [E, L] ↔ [E, P, C] basis-eval contraction, keyed on 𝒟
    --   D        : quad_point_contract  -- pointwise [E, P, C] per-quad-point diagonal against [E, P, G] geom
    apply_chain v =
      element_restrict_T (basis_apply_T term
        (quad_point_contract geom (basis_apply term (element_restrict space v))))
```

### `fe_assemble` — assemble-fold combinator (libCEED quadrature leaf as `#extern`)

Renders [`L4/fe_assemble`](../L4/fe_assemble.md). The assemble-fold `K = Σ_t assemble_term(space, t)` — a `foldr` over a `[WeakFormTerm]` list producing a commutative-monoid (operator-`+`) sum. The per-term assembly leaf `assemble_term` is the **libCEED-owned opaque kernel** ([`fe-assemble-libceed-boundary-obstruction`](../L1-L0/fe-assemble-libceed-boundary-obstruction.md), the kernel-API node) — rendered as `#extern` after its type signature.

```text
-- The assemble-fold combinator: capture the FE space once (readonly), fold the
-- weak-form-term list by the opaque per-term leaf assemble_term, sum the contributions.
-- A foldr producing a commutative-monoid sum (operator-+); the homomorphic sibling of
-- solve_family's map. Laws (concatenation-homomorphism, space-capture-once hoist,
-- term-position commutativity): see ../L4/fe_assemble.md §Algebraic laws.
--
-- # Arguments
--   space : FiniteElementSpace[N]   -- trial/test FE space, captured once at construction; readonly.
--                                      N = space.GetTrueVSize() (the operator's square dimension).
--   terms : [WeakFormTerm]          -- the immutable weak-form-term list (domain ++ boundary integrators).
-- # Returns
--   LinOp[(N: ...), $N]             -- the global operator K = Σ_t assemble_term(space, t); `zero` on [].
fe_assemble :: FiniteElementSpace[N] -> [WeakFormTerm] -> LinOp[(N: ...), $N]
fe_assemble space terms = foldr (\t acc -> assemble_term space t + acc) zero terms
  -- equivalently, the map-then-reduce the foldr-over-a-commutative-monoid IS:
  --   fe_assemble space terms = sum [ assemble_term space t | t <- terms ]

-- The opaque per-term assembly leaf: ONE weak-form term to its global-dof contribution
-- (element-local quadrature contraction + restriction). libCEED-owned (the kernel-API
-- boundary; ../L1-L0/fe-assemble-libceed-boundary-obstruction.md). Rendered #extern in
-- place of its implementation, after its type signature.
assemble_term :: FiniteElementSpace[N] -> WeakFormTerm -> LinOp[(N: ...), $N]
#extern assemble_term
```

### type `DofSet[N]` + utility API (clusters with `eliminate_bc`)

Renders the synthesized form of the [`DofSet`](../concepts/dofset.md) record (authoritative schema there) — the essential (Dirichlet) true-dof index set the BC verb-pair consumes — bundled with its intrinsic utility API. Placed immediately before its consumer `eliminate_bc`. `DiagPolicy` (the two-valued diagonal-policy enum, named only here) is rendered inline alongside.

```text
-- An immutable index set over the true-dof axis N of a finite-element space; a subset
-- of 0..N. Authoritative schema + construction-time readonly stratum + L0 backing:
-- ../concepts/dofset.md (rank: firm).
DofSet[N] = { indices : Set<TrueDofIndex> }   -- subset of 0..N (genuine flat-index set, NOT a tensor shape)

-- the diagonal-policy enum (named only by eliminate_bc; defined inline as the two-valued enum)
DiagPolicy = DIAG_ONE | DIAG_ZERO

-- # Arguments / # Returns (utility API — the type's intrinsic namespace)
-- member         :: TrueDofIndex -> DofSet[N] -> Bool   -- essential-dof membership predicate
-- size           :: DofSet[N] -> Int                    -- |E| (essential-dof count)
-- is_empty       :: DofSet[N] -> Bool                   -- the empty-dof-set identity case (no elimination)
-- complement     :: DofSet[N] -> DofSet[N]              -- the free-dof set F = 0..N \ E
```

### `eliminate_bc` — post-assembly BC application verb-pair

Renders [`L4/eliminate_bc`](../L4/eliminate_bc.md). The separable post-composition pair `(eliminate_essential_bc, eliminate_rhs)` over the `(DofSet[N], DiagPolicy)` readonly BC stratum; both post-compose AFTER `fe_assemble` on the assembled `K`. The RHS-side `b − K·x_bc` is one `linear_combination`.

```text
-- Operator-side: pin the essential dofs into the assembled square operator.
-- Idempotent; free-block preserving; DIAG_ZERO is the linear free-block projection P_F K P_F.
-- See ../L4/eliminate_bc.md §Algebraic laws.
--
-- # Arguments
--   K      : LinOp[(S: ...), $S]   -- the assembled SQUARE operator (fe_assemble output); readonly.
--   dofs   : DofSet[N]             -- the essential (Dirichlet) true-dof index set; readonly BC stratum.
--   policy : DiagPolicy            -- DIAG_ONE (essential diagonal ← 1) | DIAG_ZERO (← 0).
-- # Returns
--   LinOp[$S, $S]                  -- K with essential rows/cols zeroed + the policy diagonal installed.
eliminate_essential_bc :: LinOp[(S: ...), $S] -> DofSet[N] -> DiagPolicy -> LinOp[$S, $S]

-- RHS-side: lift the inhomogeneous Dirichlet data into the right-hand side.
-- Three data-algebra steps: apply K to the boundary-data extension, subtract from b
-- (one linear_combination), pin the essential rows per policy. See ../L4/eliminate_bc.md.
--
-- # Arguments
--   K      : LinOp[(S: ...), $S]   -- the assembled operator (applied opaquely); readonly.
--   x_bc   : Tensor[(S: ...)]      -- the essential boundary data (only essential entries read); readonly.
--   b      : Tensor[$S]            -- the RHS to adjust; readonly (L4 returns a fresh value).
--   policy : DiagPolicy            -- the essential-row pin value (x_bc for DIAG_ONE, 0 for DIAG_ZERO).
-- # Returns
--   Tensor[$S]                     -- b − K·x_bc with essential rows pinned per policy.
eliminate_rhs :: LinOp[(S: ...), $S] -> Tensor[$S] -> Tensor[$S] -> DiagPolicy -> Tensor[$S]
eliminate_rhs K x_bc b policy =
  let y    = apply_linop K (restrict_essential x_bc)      -- K · Eₑ(x_bc)
      b'   = linear_combination [(1, b), (-1, y)]         -- b − K·x_bc
      pin  = case policy of DIAG_ONE -> x_bc ; DIAG_ZERO -> zeros
  in  set_essential b' pin                                -- BC rows ← pin
  where
    -- restrict_essential / set_essential are essential-dof gather/scatter masks over
    -- DofSet[N] (the set_subvector write-mask family), not separate spine verbs.
    restrict_essential v = mask_to dofs v
    set_essential w pin  = scatter_essential dofs w pin
```

### `assemble_frequency_operator` — driven per-ω system-operator assembly verb

Renders [`L4/assemble_frequency_operator`](../L4/assemble_frequency_operator.md). The affine-in-ω operator combination `A(ω) = K + iω·C − ω²·M + A2(ω)`; the operator-operand specialization of `linear_combination` (operand monoid = operator-`+`), at term-list length 4. The fixed basis is the `FrequencyOperatorFamily[N]` readonly construction stratum (a record def rendered inline).

```text
-- The driven per-ω system-operator assembly verb: the operator-operand specialization
-- of linear_combination at the affine-in-ω corner. Pure value-producing combination
-- (no Solve monad). Laws are linear_combination's read at the operator-operand corner;
-- see ../L4/assemble_frequency_operator.md §Algebraic laws.

-- the once-assembled fixed-basis family (the readonly construction stratum):
type FrequencyOperatorFamily[N] =
  { K  : LinearOperator[N, N]            -- stiffness (curl-curl), assembled once
  , C  : LinearOperator[N, N]            -- damping (impedance/conductivity), assembled once
  , M  : LinearOperator[N, N]            -- mass (permittivity), assembled once
  , A2 : Scalar -> LinOp[(N: ...), $N]  -- frequency-dependent extra term (closure over ω)
  }

-- # Arguments
--   fam   : FrequencyOperatorFamily[N]  -- the fixed basis {K, C, M} + the ω-dependent A2; captured once.
--   omega : Scalar                      -- the (real) sweep frequency; the affine-weight parameter.
-- # Returns
--   LinOp[(N: ...), $N]                 -- the combined operator A(ω), square on axis N.
assemble_frequency_operator :: FrequencyOperatorFamily[N] -> Scalar -> LinOp[(N: ...), $N]
assemble_frequency_operator fam omega =
  linear_combination                     -- operator-operand corner (operand monoid = operator-+)
    [ (1,          fam.K)
    , (1i * omega, fam.C)
    , (-(omega^2), fam.M)
    , (1,          fam.A2 omega)
    ]
```

### `gram_reduce` — operator-weighted symmetric-Gram reduce-to-matrix

Renders [`L4/gram_reduce`](../L4/gram_reduce.md). The operator-weighted symmetric Gram reduction over a solution family: `Gᵢⱼ = w(i,j)·(xⱼᵀ K xᵢ)`, computed on the upper triangle and mirrored. The diagonal is the `matrix-weighted-norm` radicand (the `xⱼ = xᵢ` specialization — a consumer, not a separate fold); `gram_inverse` is a downstream consumer kept OUT.

```text
-- The operator-weighted symmetric-Gram reduce-to-matrix over a solution family-pair grid.
-- map-then-reduce, symmetric by construction. Laws (symmetry, diagonal-is-self-bilinear,
-- weight-factoring, grid-map independence): see ../L4/gram_reduce.md §Algebraic laws.
--
-- # Arguments
--   k  : LinOp[(S: ...), $S]      -- the domain energy operator K (symmetric/SPD); readonly.
--   xs : [Tensor[$S]]            -- the solution family [x_0 .. x_{m-1}] (congruent to K's domain S); readonly.
--   w  : Int -> Int -> Scalar    -- the per-entry normalization weight closure w(i,j) (symmetric).
-- # Returns
--   Matrix[m, m]                 -- the symmetric Gram matrix G (m = length xs).
gram_reduce :: LinOp[(S: ...), $S] -> [Tensor[$S]] -> (Int -> Int -> Scalar) -> Matrix[m, m]
gram_reduce k xs w =
  symmetric_from_upper                                  -- mirror lower triangle from upper (G symmetric)
    [ [ w i j * entry k xs i j | j <- [i .. m-1] ]      -- map over upper-triangle pairs
      | i <- [0 .. m-1] ]
  where
    m              = length xs
    entry k xs i j
      | i == j     = matrix_weighted_norm (xs!!i) k     -- diagonal: xᵢᵀ K xᵢ  (radicand; the diagonal consumer)
      | otherwise  = bilinear_form (xs!!j) k (xs!!i)    -- off-diag: xⱼᵀ K xᵢ

-- the alternate Maxwell form is the inverse (a CONSUMER, not part of the reduction):
gram_inverse :: Matrix[m, m] -> Matrix[m, m]            -- = inv (LAPACK); the Cinv / Minv tail
```

### `domain_energy_reduce` — per-domain energy-table reduction

Renders [`L4/domain_energy_reduce`](../L4/domain_energy_reduce.md). The per-domain `(energyᵢ, pᵢ)` table over a configured domain-operator map; the per-domain numerator is itself a domain-restricted SPD energy (the `matrix-weighted-norm`-squared), folded alongside the participation quotient. Driver-agnostic.

```text
-- The per-domain energy-table reduction over a solved field against a domain-operator map.
-- map-then-collect (no inter-domain state). Laws (concatenation-homomorphism, restricted-
-- energy-is-mwn-squared, shared-denominator invariance, total-guard totality): see
-- ../L4/domain_energy_reduce.md §Algebraic laws.
--
-- # Arguments
--   doms    : DomainOpMap   -- the configured domain-operator map {idx → M_idx}; readonly.
--   field   : Field         -- the solved field (E/B; possibly complex); readonly.
--   e_total : Scalar        -- the whole-domain total energy (the shared denominator); real ≥ 0; readonly.
-- # Returns
--   [DomainData]            -- per domain: (idx, energyᵢ = ½⟨field, M_idx field⟩, pᵢ = energyᵢ / e_total).
--                              (DomainData defined in ../feature/energy-fields.L4.md §Record definition.)
domain_energy_reduce :: DomainOpMap -> Field -> Scalar -> [DomainData]
domain_energy_reduce doms field e_total =
  [ let energy_i = restricted_energy m_idx field    -- ½⟨field, M_idx field⟩ (domain-restricted SPD form)
        p_i      = if e_total > 0                    -- the UNIFORM denominator guard
                   then energy_i / e_total           -- the participation_ratio quotient
                   else 0                            -- lossless / energy-free total ⇒ p_i = 0
    in  DomainData idx energy_i p_i
  | (idx, m_idx) <- doms ]                           -- map over the configured domain set (no inter-domain state)
  where
    restricted_energy m field = 0.5 * inner_product field (m `apply` field)   -- ⟨field, M field⟩, real ≥ 0
```

### `eigenfreq_qfactor_reduce` — per-mode (f, Q) scalar-table reduction

Renders [`L4/eigenfreq_qfactor_reduce`](../L4/eigenfreq_qfactor_reduce.md). The eigenmode per-mode `(fₘ, Qₘ)` table over the converged eigenpair family; `untransform` is the per-mode problem-type un-transform, `Q = ω/κ` with the lossless `κ=0 ⇒ Q=∞` guard.

```text
-- The eigenmode per-mode (f, Q) scalar-table reduction over the converged eigenpair set.
-- map-then-collect (no inter-mode state). Laws (concatenation-homomorphism, un-transform
-- purity, lossless-totality): see ../L4/eigenfreq_qfactor_reduce.md §Algebraic laws.
--
-- # Arguments
--   ptype : ProblemType        -- selects the eigenvalue→ω un-transform (linear | quadratic | nonlinear EVP)
--   kappa : Mode -> Scalar     -- the per-mode loss-rate closure κₘ (= ½R|Iₘⱼ|²/Eₘ); readonly.
--   eigs  : [Eigenpair]        -- the converged eigenpair family [(λᵢ, Eᵢ)] (eigsolve output); readonly.
-- # Returns
--   [(Scalar, Scalar)]         -- per mode: (fₘ = Re ωₘ, Qₘ = ωₘ / κₘ).
eigenfreq_qfactor_reduce :: ProblemType -> (Mode -> Scalar) -> [Eigenpair] -> [(Scalar, Scalar)]
eigenfreq_qfactor_reduce ptype kappa eigs =
  [ let omega = untransform ptype lambda               -- ω = √μ (linear) | λ/i (quadratic)
        f     = re omega                               -- eigenfrequency fₘ = Re ωₘ
        k     = kappa mode                             -- loss rate κₘ
        q     = if k == 0 then infinity else f / abs k -- quality factor Qₘ = ωₘ / κₘ
    in  (f, q)
  | (lambda, _E) <- eigs ]                             -- map over the eigenpair family (no inter-mode state)
  where
    untransform Linear    mu  = sqrt mu                -- μ = -λ² = ω²   (linear EVP)
    untransform Quadratic lam = lam / i                -- λ = iω         (quadratic EVP)
```

### `sparameter_reduce` — driven S-parameter reduce-to-matrix

Renders [`L4/sparameter_reduce`](../L4/sparameter_reduce.md). The driven per-ω per-port scattering-matrix reduction: project each solved column onto each receiver port mode, subtract the drive-port self-term, apply the port-kind impedance/de-embed scale. One drive-column per solved family member; the ω-axis is factored out (the driven composition root owns the ω map).

```text
-- The driven per-ω per-port S-parameter reduce-to-matrix. map-then-collect over the
-- column × receiver grid (no symmetric_from_upper — every entry independent). Laws
-- (column-grid map-homomorphism): see ../L4/sparameter_reduce.md §Algebraic laws.
--
-- # Arguments
--   ports  : [PortMode]                  -- the receiver port mode functionals + impedance/de-embed params
--                                           (lumped s; wave port_sr + i·port_si); readonly. p = length ports.
--   family : [(Int, Tensor[(S: ...)])]   -- the driven family: (drive_port_idx j, Eⱼ) per solved column
--                                           (at a single ω); readonly.
-- # Returns
--   Matrix[p, p]                         -- the (complex) scattering matrix S for that ω; Sᵢⱼ = receiver i, drive j.
sparameter_reduce :: [PortMode] -> [(Int, Tensor[(S: ...)])] -> Matrix[p, p]
sparameter_reduce ports family =
  matrix_from_columns
    [ [ scale ports i j * (project (ports!!i) e - selfterm i j)  -- entry Sᵢⱼ for receiver i, drive column j
        | i <- [0 .. p-1] ]
      | (j, e) <- family ]
  where
    p               = length ports
    project s e     = port_dot s e                  -- the linear functional sᵢ·E (lumped (*s)·E / wave (E×H⋆)·n)
    selfterm i j    = if i == j then 1 else 0       -- the inhomogeneous diagonal −1 self-term (drive-port subtract)
    scale ports i j = port_scale (ports!!i) (ports!!j)  -- lumped: √(R_src/R_dst); wave: exp(ikₙᵢdᵢ)·exp(ikₙⱼdⱼ)
```

### type `WaveguideModeTable` + utility API (clusters with `waveguide_mode_reduce`)

Renders the synthesized form of the [`WaveguideModeTable`](../concepts/WaveguideModeTable.md) record (authoritative schema there) — the per-mode propagation-mode table the boundary-mode reduction produces — bundled with its intrinsic utility API. Placed immediately before its producer `waveguide_mode_reduce`. The mode fields `Et`/`En`/`Bz` are genuine flat rank-1 dof-vectors (NOT named shape groups, per [semantics §1.2.1](../semantics/index.md)).

```text
-- The per-mode waveguide propagation-mode table. Authoritative schema + field strata
-- + L0 backing: ../concepts/WaveguideModeTable.md.
WaveguideModeTable = [ WaveguideModeRow ]
WaveguideModeRow = {
  kn    : Complex,            -- propagation constant (complex scalar)
  n_eff : Complex,            -- effective index kn/ω (complex scalar)
  et    : Tensor[N_nd],       -- transverse E field (2D-submesh ND space; flat rank-1 dof-vector, complex)
  en    : Tensor[N_h1],       -- longitudinal E field (H1 space; flat rank-1, complex)
  bz    : Maybe Tensor[N_curl]  -- longitudinal B (curl space); Just only for propagating modes, else Nothing
}

-- # Arguments / # Returns (utility API — the type's intrinsic namespace)
-- num_modes   :: WaveguideModeTable -> Int                  -- the converged-mode count
-- mode_at     :: Int -> WaveguideModeTable -> WaveguideModeRow
-- propagating :: WaveguideModeRow -> Bool                   -- isJust row.bz (the is_propagating predicate)
```

### `waveguide_mode_reduce` — boundary-mode field-carrying per-mode reduction

Renders [`L4/waveguide_mode_reduce`](../L4/waveguide_mode_reduce.md). The boundary-mode per-mode reduction: un-transform to the propagation constant `kn`, divide to `n_eff`, VD-back-transform + power-normalize the eigenvector to physical fields `(Et, En)`, and form the conditional longitudinal `Bz` for propagating modes. The field-carrying member of the output-product reduce-verb algebra.

```text
-- The boundary-mode per-mode propagation-mode reduction over the converged eigenpair set.
-- map-then-collect (no inter-mode state). Field-carrying rows (the load-bearing non-unify
-- vs the scalar-only / matrix siblings). Laws: see ../L4/waveguide_mode_reduce.md.
--
-- # Arguments
--   res : EigResult            -- the converged eigenpair family (2D-submesh ND⊕H1 GEP; eigsolve output); readonly.
--   w   : Scalar               -- the operating angular frequency ω; a fixed scalar parameter; readonly.
-- # Returns
--   WaveguideModeTable         -- per mode: {kn, n_eff, (Et, En, Bz)}.
waveguide_mode_reduce :: EigResult -> Scalar -> WaveguideModeTable
waveguide_mode_reduce res w =
  [ let kn         = propagation_constant (res.eigenvalues ! i)   -- eigenvalue shift-invert un-transform
        n_eff      = kn / w                                       -- effective index
        (et, en)   = vd_back_transform (res.eigenvectors ! i) kn  -- VD back-transform → physical (Et, En)
        (et', en') = power_normalize (et, en) w kn                -- normalize so |P| = 1 (Poynting power)
        bz         = if is_propagating kn                         -- conditional longitudinal B
                       then Just (curl et' / (1i * w))
                       else Nothing
    in  { kn, n_eff, et = et', en = en', bz }
  | i <- [0 .. res.converged - 1] ]                              -- map over converged modes (no inter-mode state)
```

### `sharding-decompose-reduce` — roadmap_goal stub note (NOT a filled def)

[`sharding-decompose-reduce`](../L4/sharding-decompose-reduce.md) is a **rank-0 `roadmap_goal`** — the speculative sharding-as-decomposition-abstraction MATH the batch-43 (C) gate authorizes as a future direction. It is NOT firm vocabulary and is NOT rendered as a synthesized def here; it asserts no claims, and the MPI/distributed mechanism it would eventually realize against is the deferred-future mechanism (DIRECTIVE-1, cited-not-lifted). The synthesized library therefore carries it only as this **stub note**: the intended combinator pair is `subdomain_reduce = mconcat ∘ map (reduce ∘ restrict_to_block) ∘ blocks` — recovering a global reduction over a partition of the index set by the firm reduce verbs' standing concatenation-homomorphism. See the roadmap_goal chapter for the speculative forms and the gate provenance; no implementation is rendered (a roadmap_goal has no firm def to synthesize).

## Status

`navigational-container` (rendered library chapter — implementation VIEW): it renders the synthesized code form of the firm L4 data-algebra operators, linking `reference`-class to the authoritative `../L4/<op>.md` chapters; it manufactures no `depends-on` edge and constrains no firm node's rank/liveness, and makes no resolution claim (matching its sibling synthesis library chapters). The `sharding-decompose-reduce` roadmap_goal is rendered only as a note (no firm def to synthesize).

(NOTE: this leading `stub` token is the SOLE on-disk rank carrier — the frontmatter has no `rank:`/`status:`. It is the only `stub`-ranked node in the book, and unlike its `navigational-container`-untyped sibling library chapters it reads as rank-1; flagged for the integrator/meta-phase to reconcile the inconsistency without moving the baseline in this de-bulk pass.)
