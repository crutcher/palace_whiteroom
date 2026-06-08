# krylov-step-kernel-defusion

The per-step-kernel de-fusion. Lowers the firm L2 named composition
[`krylov_step`](../L2/krylov_step.md) — the fold-kernel `(op, s) -> { state', outputs }`
that every Krylov-shaped slice in the corpus factors into — into its L1 form by **expanding
the five-primitive-group step body into the explicit sequence of seven firm L1 leaves**
([`apply_linop`](../L1/apply_linop.md), [`axpy`](../L1/axpy.md), [`axpby`](../L1/axpby.md),
[`axpbypcz`](../L1/axpbypcz.md), [`dot`](../L1/dot.md), [`nrm2`](../L1/nrm2.md),
[`scal`](../L1/scal.md) — the firm dependency list at `book/src/L2/krylov_step.md:96`) under
an outer fold, **plus the in-place→out-of-place buffer rotation** that the L2 entry deferred
here (variant-axis 6, `book/src/L2/krylov_step.md:121`). Narrated forward (L2→L1): the one
named L2 kernel composition **fans down** into Palace's dataflow-forced primitive sequence —
exactly one `apply_linop`, an optional absorbed auxiliary stage, an iterate-stratum
`axpy`/`axpby`/`axpbypcz` chain, a scalar-stratum `dot`/`nrm2` chain, and a demand-pruned
derived-view readout — and the L2's **uniformly out-of-place** buffer convention
**specialises down** to the L0 in-place buffer reuse (`Vector::Add` overwrite; Arnoldi's
`w` aliasing `V[j+1]`). This is the **kernel half** that `ksp_solve`, `chebyshev-iteration`,
and (transitively) `eigsolve` fold; the **outer-driver half** is the sibling theme
[`ksp-solve-outer-driver-unfold`](./ksp-solve-outer-driver-unfold.md) (the `iterate_while`
fold that wraps this kernel). Sibling in structure to
[`orthogonalize-composition-lowering`](./orthogonalize-composition-lowering.md) (a
one-L2-composition-fans-into-L1-vocabulary theme) and in load-bearing-residue treatment to
[`chebyshev-iteration-fusion`](./chebyshev-iteration-fusion.md) (the kernel-boundary
numerical re-association).

## Slug

`krylov-step-kernel-defusion`

## L2 form (LHS)

The L2 form is the firm fold-kernel composition ([`krylov_step`](../L2/krylov_step.md)
§Signature, §Semantics):

    krylov_step :: (op: OpParams, s: IterState) -> { state: IterState', outputs: StepOutputs }

    krylov_step op s =
      let w         = apply_linop op.T s.<input_field>             -- field-side operator apply
      let s_aux     = optionally apply op.orthog (V_prefix, w)     -- absorbed orthogonalize / project
                      or       apply op.scalars (k, scalar_state)  -- absorbed scalar generator
                      or       (no-op for vanilla CG)
      let s'_iter   = axpy / axpby / axpbypcz updates over          -- iterate-stratum update
                      s.{x, r, p, z, ...}
      let s'_scalar = dot / nrm2 / recurrence-update                -- scalar-stratum update
      let outputs   = derived-view of s' (per derived-view-hoisting) -- ephemeral; demand-pruned
      in { state: s' ⊕ s'_iter ⊕ s'_scalar, outputs }

At L2 the body is a **composition of five primitive groups in one dataflow-forced order**
(L2 entry §Semantics): the group boundaries are visible but the **constituent L1 primitives
are named-but-not-spelled** (the entry says "one or more `axpy`/`axpby`/`axpbypcz` calls",
"one or more `dot`/`nrm2` calls" — the exact sequence is slice-specific and left to the
lowering). The kernel is **stateless across calls** (`op` closed over; `s'` a fresh record —
L2 entry §Semantics), **uniformly out-of-place** in its buffer convention (variant-axis 6,
`book/src/L2/krylov_step.md:121`, "the L2 form is uniformly out-of-place, with the in-place
specialisation reappearing in the L2>L1 lowering"), and carries its variant axes
**absorbed at construction** (`op.T`, `op.orthog?`, `op.scalars?` — L2 entry §Variant axes,
not re-dispatched here).

## L1 form (RHS)

The L1 form is the **explicit sequence of seven firm L1 leaves** under the outer fold, with
the buffer convention rotated to its in-place L0-faithful form. The seven leaves are the firm
L2 dependency list (`book/src/L2/krylov_step.md:96`); their L1 signatures
([`L1/apply_linop`](../L1/apply_linop.md), [`L1/axpy`](../L1/axpy.md), etc.). At this RHS the
operands are the **concrete Palace `Vector`s** — genuinely flat rank-1 dof-vectors of length
`N`, and the operator a flat square `LinearOperator[N,N]` — so the `Tensor[N]` /
`LinearOperator[N,N]` rendering here is the literal L0/L1 call shape, NOT the shape-generic
`(S: ...)` of the L2 kernel composition above (the rank-1-ness is real at the lowered leaf
call):

    apply_linop :: (T: LinearOperator[N,N], x: Tensor[N])          -> Tensor[N]   -- T·x
    axpy        :: (α: Scalar, x: Tensor[N], y: Tensor[N])         -> Tensor[N]   -- α·x + y
    axpby       :: (α: Scalar, x, β: Scalar, y: Tensor[N])         -> Tensor[N]   -- α·x + β·y
    axpbypcz    :: (α,x, β,y, γ,z)                                 -> Tensor[N]   -- α·x + β·y + γ·z
    dot         :: (x: Tensor[N], y: Tensor[N])                    -> Scalar      -- xᴴ y
    nrm2        :: (x: Tensor[N])                                  -> Scalar      -- √(xᴴ x)
    scal        :: (α: Scalar, x: Tensor[N])                       -> Tensor[N]   -- α·x

The de-fusion writes each L2 primitive-group as a fixed sequence of these leaves. Read off the
**CG specialisation** (the firm L0 home is `book/src/L1-L0/ksp-solve-mutation-rotation.md`
Sub-pattern B; the per-step kernel for-loop `iterative.cpp:427-464`):

    krylov_step op s =                                              -- L1 de-fused (CG specialisation)
      let p'  = if s.it == 0 then s.z                               -- first-iteration branch (variant-axis 4)
                else axpby 1.0 s.z (s.β / s.β_prev) s.p             -- AXPBY(1.0, z, beta/beta_prev, p)  :440
      let z'  = apply_linop op.T p'                                 -- A->Mult(p, z)                    :443
      let den = dot z' p'                                           -- linalg::Dot(comm, z, p)          :444
      let α   = s.β / den                                           -- (CheckDot guard on den)          :445
      let x'  = axpy α p' s.x                                       -- x.Add(alpha, p)                  :448
      let r'  = axpy (-α) z' s.r                                    -- r.Add(-alpha, z)                 :449
      let z'' = apply_B? op.B r'                                    -- ApplyB (pc-absorbed; else z=r)   :451-458
      let β'  = dot z'' r'                                          -- linalg::Dot(comm, z, r)          :461
      let res = sqrt (abs β')                                       -- nrm2-shaped readout (derived)    :462
      in { state = s ⊕ {p=p', z=z'', x=x', r=r', β=β', β_prev=s.β, it=s.it+1},
           outputs = { residual_norm = res } }                     -- (CheckDot guard on β')

The seven-leaf map is exact for the CG specialisation: `apply_linop` (the one `A->Mult` per
step, `:443`); `axpby` (the `AXPBY(1.0, z, beta/beta_prev, p)` recurrence update, `:440`);
`axpy` ×2 (the `x.Add(α,p)` / `r.Add(-α,z)` iterate updates, `:448-449`); `dot` ×2 (the two
`linalg::Dot` reductions, `:444`/`:461`); the `nrm2`-shaped `sqrt(abs β')` readout (`:462`,
the derived-view residual norm — `nrm2` proper appears in the Arnoldi/normalise specialisation
and in GMRES's `Norml2`). `scal` and `axpbypcz` are **leaves of the family** that the other
specialisations pin: `scal` is Arnoldi's `v ← w/h` normalise rescale and Chebyshev's `d ← α₀·r`
seed; `axpbypcz` is Chebyshev's fused three-term polynomial-recurrence update (L2 entry
§Semantics "chebyshev: one axpbypcz + one axpy"). The seven-leaf set is the **family the
fold-kernel draws from**; each slice pins a specific sub-sequence (the per-slice primitive-call
enumeration, L2 entry law 2).

### The in-place→out-of-place buffer rotation (variant-axis 6)

The L2 form is **uniformly out-of-place** (each leaf returns a fresh tensor). The L0 form is
**in-place**: `x.Add(alpha, p)` overwrites `x` in its own buffer (`iterative.cpp:448`),
`r.Add(-alpha, z)` overwrites `r` (`:449`), and Arnoldi's candidate `w` **aliases** the new
basis column `V[j+1]` (`arnoldi_step.md:129-131`, L2 entry variant-axis 6). The rotation from
the out-of-place L2 form to the in-place L0 form is **transparent-performance-equivalent**
(CLAUDE.md §Optimization tricks): the L1 leaf `axpy α p' s.x` is value-faithful (returns a
fresh `x'`), and the **in-place realisation of that leaf** (overwriting the `x` buffer when no
observer of the prior `x` survives the call) is the firm L1>L0 leaf lowering's concern —
[`axpby-mutation-rotation`](../L1-L0/axpby-mutation-rotation.md) for the `axpy` `x.Add`/`r.Add`
overwrites (that theme lowers both `axpy` and `axpby` into Palace's in-place `Vector::Add`
member-call form),
[`apply-linop-mutation-rotation`](../L1-L0/apply-linop-mutation-rotation.md) for the `A->Mult`
write-into-`z`. **This theme stops at the L1 leaf** and defers the per-leaf in-place buffer
overwrite to those L1>L0 themes — exactly as
[`orthogonalize-composition-lowering`](./orthogonalize-composition-lowering.md) §applicability
condition 6 defers `w.Add` to `orthogonalize-mutation-rotation`. The variant-axis-6 selection
(`in-place | out-of-place`) is therefore a **buffer-aliasing annotation on the lowering, not a
value branch**: the de-fused L1 sequence is identical; the axis records which buffer the L0
realisation writes into (and, for Arnoldi, that `w` and `V[j+1]` are the same storage).

## The de-fusion rewrite (L2 → L1)

The lowering expands each L2 primitive group into its L1 leaf sub-sequence, **preserving the
dataflow-forced order** (L2 entry §Semantics: the ordering is rigid — `apply_linop` precedes
the `axpy` that reads `w`; the scalar-stratum `dot` follows the iterate update it reads; the
readout is downstream of both):

| L2 primitive group (entry §Semantics) | L1 leaf sub-sequence (de-fused) | dataflow constraint |
|---|---|---|
| operator apply | exactly one `apply_linop op.T s.<input>` (or the `apply_BA` unfold into one/two `apply_linop`, per `concepts/apply_BA`) | head of the chain; everything reads its output `w` |
| optional auxiliary | `op.orthog` → `orthogonalize` composition (itself `dot`-fold ▷ `axpy`-fold, the sibling theme); `op.scalars` → closed-form coefficient arithmetic (no field leaf); CG → ∅ | reads `w`; precedes the iterate update when it modifies the search direction |
| iterate-stratum update | one or more `axpy` / `axpby` / `axpbypcz` (CG: `axpby` + `axpy`×2; Arnoldi: `scal` + orthog unfold; Chebyshev: `axpbypcz` + `axpy`) | each reads `w` and/or scalars; mutually independent across disjoint fields (L2 law 3) |
| scalar-stratum update | one or more `dot` / `nrm2` + closed-form recurrence (CG: `dot z p`, `dot z r`; GMRES: `dot v_i w` per orthog column) | `dot` reads the post-apply / post-update fields; gates the next step's iterate update |
| output readout | a derived view (`nrm2`-shaped `sqrt(abs β)`, or `nrm2` proper) written to `outputs`; **demand-pruned** (L2 law 1) | downstream of all; skippable when no consumer reads it |

The **de-fusion rule** is: *expand each named primitive group into its slice-pinned L1 leaf
sub-sequence in the dataflow-forced order; absorb the construction-time variant axes into the
leaves' arguments (`op.T`, `op.orthog`, `op.scalars` flow through unchanged); rotate the
uniformly-out-of-place buffer convention to the in-place L0 form per the variant-axis-6
annotation, deferring each leaf's in-place overwrite to its L1>L0 mutation-rotation theme.*
The expansion is **value-preserving** — the seven L1 leaves are pure (L2 entry §Semantics
"the L1 primitives `axpy`/`axpby`/`axpbypcz` are themselves pure at L1") and their composition
in the forced order reproduces the kernel's `{ state', outputs }` exactly.

### Demand-pruning of the output readout (the one carried law)

The output-readout group is **demand-pruned** per the L2 entry's load-bearing Law 1
(output-extras distributivity over the trajectory, inherited from
[`derived-view-hoisting`](../concepts/derived-view-hoisting.md)). At the de-fused L1 level
this means the `nrm2`-shaped `sqrt(abs β')` readout leaf (and any `ls_residual` / Hessenberg
subdiagonal readout) is emitted **iff a downstream consumer reads `.outputs.f`**; when pruned,
the de-fused sequence drops the readout leaf and the `state'` projection is unchanged. This is
the single non-trivial algebraic law that survives the de-fusion — it is **carried by
reference** to the L2 entry's Law 1, not re-derived here. The L0 witness is that the residual
norm `res = std::sqrt(std::abs(beta))` (`iterative.cpp:462`) is computed every iteration in
Palace's eager form but is a pure function of `beta` (already needed for `converged`), so its
materialisation is a derived view (L2 entry §Semantics output readout).

## Applicability conditions

The de-fusion preserves the L2 kernel's `{ state', outputs }` value when:

1. **Dataflow-forced order preserved.** The L1 leaf sub-sequences must be emitted in the
   dataflow order (apply ▷ auxiliary ▷ iterate-update ▷ scalar-update ▷ readout). The L2 entry
   §Algebraic-laws "Commutativity of the primitive sequence" **does not hold** — swapping
   adjacent groups produces a different state or a type error. Within independent leaves of the
   same group (e.g. CG's two `axpy`s over disjoint fields `x`/`r`, L2 law 3) reordering is
   value-exact but may change MPI-collective shape (load-bearing per CLAUDE.md §Optimization
   tricks).

2. **Variant axes absorbed at construction, not re-dispatched in the body.** The six L2 variant
   axes (preconditioner side, orthogonalization variant, polynomial kind, first-iteration
   unrolling, restart shape, buffer use) are absorbed into `op.T` / `op.orthog` / `op.scalars`
   closures (L2 entry §Variant axes, level (b)/(c) of `variant-absorption`). The de-fused body
   does **not** branch on them — it expands the slice-pinned sequence the absorbed closures
   already determine. (The one exception is variant-axis 4, the first-iteration branch, which
   for the v0.4 in-body form keeps an `if s.it == 0` in the de-fused sequence, `:434-441`; the
   v0.5 unrolled form splits `cg_first_step`/`cg_steady_step` and removes it.)

3. **Buffer rotation is transparent (value) but load-bearing (aliasing/collective).** The
   in-place→out-of-place rotation (variant-axis 6) preserves the value unconditionally; the L0
   in-place realisation is valid only when no observer of a prior buffer survives the overwrite
   (the per-leaf L1>L0 mutation-rotation themes' aliasing conditions). For Arnoldi, the
   `w`-aliases-`V[j+1]` identification (`arnoldi_step.md:129-131`) is the specific aliasing the
   axis records. This theme stops at the L1 leaf and defers the in-place mechanics to
   `axpby-mutation-rotation` (the `axpy`/`axpby` in-place `Vector::Add` family) /
   `apply-linop-mutation-rotation`.

4. **`CheckDot` partial-function guard carried as a step-local precondition, not a body
   branch.** The scalar-stratum `dot` results are partial-functioned on finiteness and (SPD)
   positivity by `CheckDot` (`iterative.cpp:21-32`, called for CG at `:445`/`:461`). At the
   de-fused L1 level this surfaces as a precondition on the `dot`-leaf results feeding the
   `α = β/den` and `β' = dot z'' r'` arithmetic — the kernel does **not** branch on breakdown
   (the outer driver does, on `outputs.breakdown_token`, L2 entry §Semantics). The guard is
   carried as a claim, not re-derived (it is the L2 entry's breakdown-token slot).

5. **Output readout demand-pruned (Law 1).** The readout leaf is emitted iff a consumer reads
   it (condition for the §"Demand-pruning" sub-section); pruning it does not change `state'`.

## Justification kind

`structural` — the de-fusion **is** the syntactic expansion of the L2 entry's five-primitive-
group §Semantics body into the explicit sequence of seven firm L1 leaves, preserving the
dataflow-forced order. The group→leaf map (the table in §"The de-fusion rewrite") is read
straight off the L2 §Semantics text and the CG L0 specialisation (`iterative.cpp:427-464`)
— each named group expands to a fixed leaf sub-sequence with no algebraic law
needed beyond the purity of the leaves. An **algebraic** flavour is present on the buffer
rotation (the in-place/out-of-place forms are transparent-performance-equivalent, CLAUDE.md
§Optimization tricks — value-identical, differing only in storage) and the demand-pruning of
the readout (L2 Law 1, carried by reference). A **reduction-chain** flavour is present in the
dataflow-forced order (each `dot` reads the prior apply/update; the recurrence threads the
scalar stratum). But the governing content is the **structural group→leaf expansion**, so the
theme is classified `structural` (matching the standalone-gate de-fusion siblings
`divfree-projector-leaf-identity` and the composition siblings, where the syntactic fan-down
is the governing content). No load-bearing numerical re-association is **introduced** by the
de-fusion (contrast `chebyshev-iteration-fusion`, where the recurrence↔polynomial fusion IS
the load-bearing content) — the kernel's only carried numerical residue is the
`CheckDot`-guarded `dot` and the slice's MPI-collective shape, both carried by reference.

## Speculative L1 operators

**None.** All seven L1 RHS leaves are firm (the firm list at
`book/src/L2/krylov_step.md:96`):

- [`apply_linop`](../L1/apply_linop.md), [`axpy`](../L1/axpy.md), [`axpby`](../L1/axpby.md),
  [`axpbypcz`](../L1/axpbypcz.md), [`dot`](../L1/dot.md), [`nrm2`](../L1/nrm2.md),
  [`scal`](../L1/scal.md) — all firm.

The LHS [`krylov_step`](../L2/krylov_step.md) is firm (the canonical
fold-kernel shape). This theme proposes **no new operators** — it is the lowering edge between
firm vocabulary on both sides. The optional auxiliary stage's `op.orthog` composition is the
firm sibling theme [`orthogonalize-composition-lowering`](./orthogonalize-composition-lowering.md)
(cited, not re-derived); `op.scalars`'s closed-form coefficient arithmetic is scalar-stratum
(below the field-leaf resolution). The MINRES / BiCGStab specialisations remain **obstruction
documentation** (`book/src/L1-L0/minres-iteration.md`, `bicgstab-iteration.md`) per CLAUDE.md
unimplemented-component policy — their speculative `lanczos_step` / `bicgstab_step` would
specialise this kernel but are not promoted (L2 entry §Status).

## Evidence

L0 evidence ranges (paths relative to `reference/`):

- `palace/linalg/iterative.cpp:427-464` — the CG per-step kernel for-loop (the de-fusion's L0
  specialisation witness).
- `palace/linalg/iterative.cpp:440` — `linalg::AXPBY(1.0, z, beta/beta_prev, p)`: the `axpby`
  recurrence update (inside the `else` of the first-iteration branch `:434-441`).
- `palace/linalg/iterative.cpp:443` — `A->Mult(p, z)`: the one `apply_linop` per step.
- `palace/linalg/iterative.cpp:444` — `denom = linalg::Dot(comm, z, p)`: the first `dot`.
- `palace/linalg/iterative.cpp:445` — `CheckDot(denom, ...)`: the SPD partial-function guard on
  the `dot` result (applicability condition 4).
- `palace/linalg/iterative.cpp:448-449` — `x.Add(alpha, p)` / `r.Add(-alpha, z)`: the two
  `axpy` iterate updates (the in-place L0 buffer overwrite — variant-axis-6 rotation target).
- `palace/linalg/iterative.cpp:461` — `beta = linalg::Dot(comm, z, r)`: the second `dot`
  (scalar-stratum thread).
- `palace/linalg/iterative.cpp:462` — `res = std::sqrt(std::abs(beta))`: the `nrm2`-shaped
  derived-view residual readout (demand-pruning Law 1 witness).
- `palace/linalg/iterative.cpp:21-32` — `CheckDot` partial-function guard (real overload :22,
  complex :28; the `MFEM_ASSERT(std::isfinite(dot) && dot >= 0.0, ...)`). The breakdown-token
  precondition (applicability condition 4).

L2 / L1 / cross-theme anchors (firm on every side):

- `book/src/L2/krylov_step.md` — the firm L2 named composition (LHS); §Signature (the
  fold-kernel shape), §Semantics (the five-primitive-group body the de-fusion expands), `:96`
  (the seven-leaf firm dependency list), `:121` (variant-axis-6, the in-place/out-of-place
  buffer axis this theme resolves), `:129-132` (the L2-vs-L1 distinction — context, not the
  lowering), Law 1 (demand-pruning, carried by reference).
- `book/src/L1/apply_linop.md`, `axpy.md`, `axpby.md`, `axpbypcz.md`, `dot.md`, `nrm2.md`,
  `scal.md` — the seven firm L1 leaves the de-fused body composes.
- `book/src/L1-L0/ksp-solve-mutation-rotation.md` — Sub-pattern B: the firm L0 terminal home
  for the CG body (`iterative.cpp:360-486`); the per-step kernel for-loop `:427-464` is
  recognised there. This theme cites it as the L0 home; the per-leaf in-place mechanics are its
  and the per-leaf L1>L0 mutation-rotation themes' concern (the de-fusion stops at the L1 leaf).
- `book/src/L1-L0/axpby-mutation-rotation.md` (lowers both `axpy` and `axpby`),
  `book/src/L1-L0/apply-linop-mutation-rotation.md` — the per-leaf in-place buffer-overwrite
  themes the variant-axis-6 rotation defers to (the `x.Add`/`r.Add` and `A->Mult`-into-`z`
  in-place realisations). Cited, not re-derived.
- `book/src/L2-L1/orthogonalize-composition-lowering.md` — the structural sibling
  (one-L2-composition-fans-into-L1-vocabulary) and the de-fusion target of the optional
  auxiliary `op.orthog` stage (the `dot`-fold ▷ `axpy`-fold). Cited for the auxiliary stage,
  not re-derived.
- `book/src/L2-L1/chebyshev-iteration-fusion.md` — the kernel-boundary-numerical-residue
  sibling (the recurrence↔polynomial fusion); contrast — this theme introduces no numerical
  re-association, only the structural de-fusion.
- `book/src/L2-L1/ksp-solve-outer-driver-unfold.md` — the **outer-driver half** sibling:
  the `iterate_while` fold that wraps this kernel. This theme owns the
  **per-step kernel de-fusion**; that theme owns the **outer fold unfold** — clean partition.

## Status

`firm` — the LHS [`krylov_step`](../L2/krylov_step.md) and all seven L1 RHS leaves are firm
(the firm dependency list `:96`), and the de-fusion rule IS the syntactic expansion of the L2
§Semantics five-primitive-group body into the slice-pinned L1 leaf sequence — read straight off
the L2 entry text and the CG L0 specialisation (`iterative.cpp:427-464`). The group→leaf map, the
dataflow-forced order, and the seven-leaf assignment are all anchored on firm vocabulary or L0;
the one carried algebraic law (demand-pruning, L2 Law 1) and the breakdown guard (`CheckDot`) are
carried by reference to the firm L2 entry, not re-derived; the in-place→out-of-place buffer rotation
(variant-axis 6) is delegated to the firm per-leaf L1>L0 mutation-rotation themes
(`axpby-mutation-rotation` for the `axpy`/`axpby` `Vector::Add` family, `apply-linop-mutation-rotation`)
— the de-fusion stops at the L1 leaf. No literature inference, no negative-anchor reconstruction, no
speculative operator.

## Open questions / caveats

- **Per-leaf in-place delegation boundary.** This theme deliberately does NOT re-derive the
  in-place buffer overwrites (`x.Add`/`r.Add`/`A->Mult`) — it cites the per-leaf L1>L0
  mutation-rotation themes. The boundary: this L2>L1 theme owns the **group→leaf de-fusion + the
  variant-axis-6 buffer-use annotation**; the per-leaf L1>L0 themes own the **in-place buffer
  mechanics**; the L2 entry owns the **construction-time variant absorption + Law 1**.

- **CG-specialisation is the worked example; Arnoldi/Chebyshev sequences stated, not
  per-line-verified.** The de-fusion is worked in full on the CG specialisation
  (`iterative.cpp:427-464`). The Arnoldi (`scal` + orthog unfold) and Chebyshev (`axpbypcz` +
  `axpy`) leaf sub-sequences are stated from the L2 entry §Semantics per-slice enumeration. The
  structural de-fusion rule is slice-invariant; only the exact per-slice sub-sequence is
  slice-specific.
