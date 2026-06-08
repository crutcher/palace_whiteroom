---
layer: L3
operator: orthogonalize
# `partial-obstruction` (rank: partial-obstruction): the per-step `dot`+`axpy` body lifts for all
# three variants AND the CGS/CGS2 loop lifts, but the MGS `j`-loop is a witnessed
# `sequential-obstruction` (§Status). The lifted body is firm (syntactic identities on the
# `orthog.hpp` source, inherited from the firm L1/L2 entries) → obstruction_resolution: firm.
# RE2 baseline-exception: `L4/krylov_step` composes the L2 surface directly, not the L3
# iteration-view, so there is no faithful reachable inbound depender (no forced inbound edge added).
rank: partial-obstruction
obstruction_resolution: firm
edges:
  depends-on:
    - target: L2/orthogonalize
      kind: lowers-to             # the firm L2 `project ▷ subtract` composition; per-step body identity-in-form (legacy lifts_from + lowers_to both name it)
    - target: L3-L2/orthogonalize-variant-split
      kind: lowers-to             # the dedicated SUBSTANTIVE L3>L2 loop-structure variant-split theme; this op is its UPPER endpoint
    - target: L3/inner_product
      kind: composes              # same-layer body primitive: the projection-coefficient inner product H_j = op.dot(w_eff(j), V[j]); the dot specialization-stub was eliminated into the combinator (see inner_product §Specializations)
    - target: L3/linear_combination
      kind: composes              # same-layer body primitive: the rank-1 residual update w − H_j·V[j] = axpy(-H_j, V[j], w); axpy leaf eliminated into the combinator (RE6), this is its arity-2 specialization (see linear_combination §arity-specializations)
  reference:
    - concepts/sequential-obstruction
    - concepts/tensor-field-lift
    - concepts/variant-absorption
    - concepts/orthogonalization
    - L1/orthogonalize
    - L3/chebyshev
    - L3/eigsolve
variant_axes:
  - gs_orthog (MGS = sequential per-column projector chain, NON-lifting / CGS = batched single-reduction, lifts / CGS2 = two CGS passes, lifts — this is the axis along which the L3 lift verdict SPLITS)
  - dot-hook (canonical ⟨·,·⟩ / B-weighted — parametric, the lift verdict is invariant under the hook substitution)
  - element-type (real / complex — fully parametric, absorbed by the dot dependency)
---

# orthogonalize

The L3 (iteration-rotation) view of `orthogonalize` — the **variant-split partial-obstruction**
case. `orthogonalize` removes the `span(V)`-component of a candidate `w` against a stored
orthonormal basis `V[0..m-1]`, producing the orthogonal residual `w'` and the projection
coefficients `H[0..m-1]` (the leading entries of the Arnoldi/Hessenberg column). At L3 the
iteration-rotation verdict **depends on the `gs_orthog` variant**:

- **CGS / CGS2 lift cleanly.** Every coefficient `H[j] = ⟨w, V[j]⟩` is taken against the *same
  original* (un-mutated) `w`, so the `m` inner products are mutually independent: the projection
  stage is the single global tensor-field statement `H = Vᴴ w` (one batched matvec by `Vᴴ`) and
  the subtraction stage is `w' = w − V H` (one batched matvec by `V`). CGS2 is two such passes.
  No per-column loop-carried dependency survives — the basis index `j` is a reduction/broadcast
  axis, not a recurrence.
- **MGS does not lift.** Each coefficient is taken against the *progressively-subtracted*
  candidate: `H[j] = ⟨w^(j), V[j]⟩` with `w^(j+1) = w^(j) − H[j]·V[j]`. The `j`-th subtraction
  must complete before the `(j+1)`-th dot — a genuine `sequential-obstruction` over the basis
  index. There is no global tensor-field form of MGS; any rewrite that touches all columns of
  `V` simultaneously is no longer MGS (`concepts/sequential-obstruction.md:37-48`).

This is the canonical **partial-obstruction** shape (body lifts, loop does not), here with the
distinguishing feature that the obstruction **lives on one variant branch only** — the
`gs_orthog` axis is the axis along which the L3 lift splits. Companion to L2
[`orthogonalize`](../L2/orthogonalize.md) (the same `project ▷ subtract` composition with the
iteration view erased) and L1 [`orthogonalize`](../L1/orthogonalize.md) (the pure leaf with the
variant as an opaque parameter).

## Context

L3 is the iteration-rotation layer: where the L2 algebra admits a global tensor-field form, L3
captures it; where no global form exists, the **obstruction** is a first-class output (per
[`sequential-obstruction`](../concepts/sequential-obstruction.md)). `orthogonalize` at L3 is the
**third `partial-obstruction`** operator, and the one that makes the body-lifts/loop-doesn't
shape **variant-dependent**:

- L3 [`chebyshev`](./chebyshev.md) (`partial-obstruction`) — body lifts, but the inner
  `k`-recurrence + outer `pc_it` sweep are sequential obstructions rooted in **numerical
  stability** (Phillips & Fischer 2022 §2: the recurrence form is chosen over explicit
  polynomial expansion). The obstruction is **unconditional** — it holds for every parameter
  value.
- L3 [`eigsolve`](./eigsolve.md) (`partial-obstruction`) — body lifts, but the
  eigen-iteration loop is a sequential obstruction rooted in **opaque-library-ownership** (SLEPc
  `EPSSolve` / ARPACK `naupd` RCI own the loop; Palace authors none). Also **unconditional**.
- `orthogonalize` (this entry) — body lifts (one `dot` + one `axpy` against whole tensors), but
  the obstruction is **conditional on the variant**: present for MGS (a Palace-authored
  per-column recurrence rooted, like `chebyshev`, in **numerical stability** — MGS holds
  orthogonality to roundoff where CGS loses it for ill-conditioned bases), **absent** for
  CGS/CGS2 (which lift to batched global field operations). The `gs_orthog` axis is therefore
  the axis along which the partial-obstruction verdict splits — a structure neither precedent
  exhibits.

The load-bearing structural fact this entry records: **`orthogonalize` at L3 has a lifting body
and a loop whose liftability is variant-dependent — CGS/CGS2 lift, MGS is a Palace-authored
numerical-stability sequential obstruction.** This is the L3-cohort-growth audit's **(B)**
prediction enacted (`book/src/L3/index.md:48`: "MGS variant has sequential-obstruction at L3
explicitly noted at L1; CGS/CGS2 variants lift cleanly — would be a third `partial-obstruction`
row after `chebyshev` and `eigsolve`").

The relationship to the adjacent layers:

- **Upward** to L4: no firm L4 `orthogonalize` entry exists (the `L4/orthogonalize.md` chapter
  is not yet authored). The L2 [`krylov_step`](../L2/krylov_step.md) consumer absorbs
  `orthogonalize` at level-(b) as the optional `op.orthog (V_prefix, w)` auxiliary stage; an
  imagined L4 form would thread the `{ residual, coeffs }` record through the Arnoldi-step
  monad, but that surface is a future dispatch. This entry lifts from L2 only.
- **Downward** to L2: [`orthogonalize`](../L2/orthogonalize.md) (firm) is the same
  `project ▷ subtract` composition with the iteration view erased (the per-variant batched /
  interleaved primitive sequence named, the collective shape disclosed as the residual axis).
  The L3>L2 rotation on the **body** is **identity-in-form**: the L3 per-step tensor-field
  update (one `dot` for `H[j]`, one `axpy` for `w − H[j]·V[j]`) maps line-for-line to the L2
  composition stages (the L2 §Semantics `project` / `subtract` stages are exactly this body
  with the field-algebra operators spelled as their L1-primitive names). The single surface
  adjustment is that L3 makes the **per-variant loop structure** explicit as an
  iteration-rotation verdict: MGS as a `sequential-obstruction` marker (the `[dot, axpy] × m`
  interleaved chain), CGS as a clean batched lift (`[dot × m, allreduce, axpy × m]`), CGS2 as
  `[CGS] × 2`. This is information-preserving — the L2 entry already records the same
  per-variant sequencing as the collective-shape residual axis and the MGS-interleaving non-law
  (column-order non-commutativity).

**Non-adjacent identity (in-line, no directory).** Because the L3>L2 body rotation is
identity-in-form **and** the L2>L1 body rotation is identity-in-form (the L2
[`orthogonalize`](../L2/orthogonalize.md) §"L2 vs L1 distinction" establishes that the L2 named
composition lifts the L1 leaf without a structural body rewrite — L2 changes the *resolution*
along the batching axis, surfacing the per-variant `dot`/`axpy` sequence that L1 carried as an
opaque parameter; the L1↔L2 edge is a resolution change, not a structural rewrite), the
composition (L3>L2 identity ∘ L2>L1 identity ⟹ L3>L1 identity) makes this L3 body
value-thread-isomorphic to the L1 [`orthogonalize`](../L1/orthogonalize.md) leaf body as well,
at the per-step body level. That non-adjacent relationship is the **transitive consequence of
the two adjacent-edge identities** and is annotated **in-line** here (and in the dep-map),
citing the existing adjacent entries; **no `book/src/L3-L1/` directory is created** (per the
meta-phase decision `l3-l1-inline-identity-rotation-convention`, lowering directories
are per-adjacent-edge only). Note the caveat: the L1↔L2↔L3 body identity is on the **per-step
`dot`+`axpy` body**; it does **not** erase the L3 loop-structure obstruction, which is a
property of the surrounding `j`-loop *for the MGS variant only* (the same way `chebyshev`'s body
identity does not erase its inner/outer loop obstruction).

A cross-cutting prose treatment lives at
[`concepts/orthogonalization`](../concepts/orthogonalization.md); the MGS-vs-CGS
sequential-obstruction structure is at
[`concepts/sequential-obstruction`](../concepts/sequential-obstruction.md) §"Example: MGS as
sequential-obstruction" (`:37-48`). This L3 entry is the firm operator definition of the
iteration-rotation form; the concept pages are the narrative.

## Signature

    orthogonalize :: (op, w, V) -> { residual, coeffs }

Shape contract (positional values; L3 has no `readonly` annotation and no monadic effect; the candidate vector shape group `S` follows the named-shape-group convention of [`l4_calculus`](../semantics/index.md) §1.2.1; the basis `Basis[N, m]` is a genuine 2-D `m`-column basis whose columns `V[j]` are length-`N` dof-vectors congruent to `S`, and `coeffs : Tensor[m]` is genuinely 1-D — both KEEP their concrete length axes):

- **`op`** — orthogonalization-parameters value, closure-captured by the body (a positional
  argument never present in the return position). The body reads:
  - `op.variant : GSVariant ∈ {MGS, CGS, CGS2}` — the orthogonalization variant; **inspected
    exactly once at dispatch**, never re-branched per column. This is the axis along which the
    L3 lift verdict splits (MGS non-lifting / CGS, CGS2 lifting).
  - `op.dot : (Tensor[(S: ...)], Tensor[$S]) -> Scalar` — the inner-product hook; the canonical
    [`dot`](./inner_product.md#specializations) (conjugate-linear in the first argument) by default, the SLEPc/ROM paths
    substitute a `B`-weighted dot. A parametric axis: the lift verdict is invariant under the
    hook (the body shape and the MGS/CGS structural split are unchanged).
- **`w`** — `Tensor[(S: ...)]` — read-only; the (un-normalised) candidate vector to orthogonalize.
- **`V`** — `Basis[N, m]` — read-only; `m` columns each a length-`N` dof-vector (congruent to `S`), the **precondition**
  being orthonormal (`⟨V[i], V[j]⟩ = δ_ij`) under `op.dot`. The operator does not enforce the
  precondition (inherited from the L1 leaf, whose L0 header states it, `orthog.hpp:18-23`).
- **result `{ residual, coeffs }`** — a record with two whole-tensor fields:
  - `residual : Tensor[$S]` — the orthogonal residual `w − Σ_j coeffs[j]·V[j]`, **not
    normalised** (the L0 header's load-bearing no-output-normalisation contract,
    `orthog.hpp:22`). Same shape group `S` as `w`.
  - `coeffs : Tensor[m]` — the projection coefficients (the leading `m` entries of the
    Hessenberg column). Element type matches `w` / `V`.

The `m = 0` case (empty basis) is the identity for every variant:
`orthogonalize op w [] = { residual = w, coeffs = [] }` (the L0 CGS early-return
`orthog.hpp:62-64`, witnessed across all three variants at `test-orthog.cpp:99-120`).

**Normalisation is not part of this operator.** Every consumer follows the call with its own
`nrm2` (the Hessenberg sub-diagonal `H[m] = ‖residual‖`) and `scal (1/‖residual‖)` — the GMRES
site `iterative.cpp:630-632`, the FGMRES site `iterative.cpp:809-811`. `nrm2` / `scal` are
therefore **not** dependencies; the record stops at the un-normalised residual. This boundary is
inherited verbatim from the firm L1 leaf.

L4 wrapper machinery absent at L3 (structural for the layer): there is **no `Solve` monad** and
**no `Read`/`ReadWrite` capability typing** — the value-threaded `(op, w, V) -> { residual,
coeffs }` form is positional; `w` and `V` flow in read-only, the residual/coeffs record flows
out as a fresh value. The variant tag is a single positional `op.variant` inspected once (no
closure-typed variant absorption); the per-variant loop structure is rendered explicitly at L3
(see §Semantics).

## Semantics

`orthogonalize` removes the `span(V)`-component of `w`. In **exact arithmetic with an exactly
orthonormal `V`** all three variants compute the same record: `coeffs[j] = op.dot(w, V[j])` and
`residual = (I − V Vᴴ) w`, the orthogonal projection onto `span(V)`'s complement. The variants
differ only in finite precision and in the **iteration structure** of the projection — and at
L3 that iteration structure is the load-bearing content, because it determines whether the
operation lifts to a global tensor-field form.

### Tensor-field body (one inner step `j`)

Fix the inner-step body that runs once for each basis column `j ∈ {0, …, m−1}`. With the basis
column `V[j] : Tensor[N]` (a basis column) and the candidate `w_eff(j) : Tensor[$S]`, the body is

$$
\begin{aligned}
H_j        &= \langle w_{\mathrm{eff}}(j),\, V[j] \rangle, \\
w^{(j+1)}  &= w^{(j)} - H_j \cdot V[j],
\end{aligned}
$$

where `w_eff(j)` is the candidate as seen by column `j`. Each line is a global tensor-field
expression: `H_j` is a [`dot`](./inner_product.md#specializations) reduction (whole-tensor in, scalar out), and the
update is an [`axpy`](./linear_combination.md#arity-specializations) (`w − H_j·V[j]` = `axpy(-H_j, V[j], w)`). There is no
per-element dependence *within* a line; the **per-step body lifts cleanly** to whole-tensor
field arithmetic, identically to the firm L2 `project`/`subtract` stages. **What differs across
variants is `w_eff(j)` and the inter-`j` structure** — and that is the iteration-rotation
verdict.

### CGS / CGS2 — the global lift (no obstruction)

For **CGS**, `w_eff(j) = w` for *every* `j`: all `m` coefficients are taken against the same
original candidate. The `m` `dot` reductions are mutually independent, so the projection stage
collapses to a single batched global statement and the subtraction to another:

$$
H = V^{\mathsf{H}} w \qquad (\text{one batched matvec by } V^{\mathsf{H}}), \qquad
w' = w - V H \qquad (\text{one batched matvec by } V).
$$

This is a parallel tensor-field statement — the basis index `j` is a reduction/broadcast axis,
not a recurrence. **CGS lifts cleanly: no sequential obstruction.** **CGS2** (re-orthogonalised
classical) is the CGS lift applied **twice**: a first pass `(H, w₁) = (Vᴴw, w − VH)`, then a
second pass `(dH, w₂) = (Vᴴw₁, w₁ − V·dH)` producing a correction, with returned coefficients
`H + dH` and residual `w₂`. Both passes are clean global lifts; the second pass reads the
once-orthogonalised `w₁` and is **not** algebraically fusible with the first (the
re-orthogonalisation property — "twice is enough", Kahan/Parlett — requires the second
projection against the once-projected vector). CGS2 is the `[CGS lift] × 2` shape: two clean
lifts in sequence, no per-column obstruction.

### MGS — the sequential obstruction (no global lift)

For **MGS**, `w_eff(j) = w^(j)` — the *progressively-subtracted* candidate, with `w^(0) = w` and
`w^(j+1) = w^(j) − H_j·V[j]`. The `j`-th subtraction must complete before the `(j+1)`-th dot is
computed. Equivalently `residual = (I − V[m-1] V[m-1]ᴴ) ⋯ (I − V[0] V[0]ᴴ) w` — a left-to-right
composition of `m` rank-1 projectors applied serially. **MGS therefore has no global
tensor-field form**: any rewrite that touches all columns of `V` simultaneously computes the
coefficients against the original `w` and is, by definition, CGS — not MGS. The dependency is a
[`sequential-obstruction`](../concepts/sequential-obstruction.md) over the **basis index `j`**:
the loop-carried state is the field-side candidate `w^(j)` (per-DoF, `O(N)`), and the
recurrence is over `j` (the basis index), with each step a global `dot`+`axpy` on field state
(`concepts/sequential-obstruction.md:37-48`). The source witness is the L0 MGS `j`-loop body
`H[j] = dot_op(w, V[j]); … w.Add(-H[j], V[j])` — the `dot` and the `w.Add` in the **same**
`j`-loop iteration, the second feeding the next iteration's `dot` (`orthog.hpp:46-52`).

The obstruction is rooted in **numerical stability** (like `chebyshev`'s recurrence, unlike
`eigsolve`'s opaque-library loop): MGS exists precisely *because* the serial projector
composition holds orthogonality to roundoff where the batched CGS form loses it for
ill-conditioned bases. The sequentiality is fundamental to MGS's numerical behaviour, not an
implementation artefact. CGS is the parallel-reduction alternative; the choice between them is
exposed as the `gs_orthog` variant axis (per `concepts/sequential-obstruction.md:22`, the MGS
example: "CGS is the parallel-reduction alternative; the choice is exposed as the `gs_orthog`
variant").

### Value-threaded form (L3 rendering)

    orthogonalize op w V =
      case op.variant of
        CGS  -> let coeffs = batched_dot V w           -- H = Vᴴw : one global reduction, j is a reduction axis
                    residual = batched_subtract w coeffs V   -- w − V H : one global matvec, j is a broadcast axis
                in { residual, coeffs }                 -- LIFTS: no inter-j recurrence
        CGS2 -> let (h1, w1)  = cgs_pass w V            -- first clean lift
                    (dh, w2)  = cgs_pass w1 V           -- second clean lift (against once-projected w1; non-fusible)
                in { residual = w2, coeffs = h1 + dh }  -- LIFTS: [CGS lift] × 2
        MGS  -> jloop 0 w (zeros m)                     -- SEQUENTIAL OBSTRUCTION over basis index j
      where
        -- MGS per-column tail recursion: w^(j+1) depends on H_j which reads w^(j) — NON-lifting
        jloop j w coeffs =
          if j >= m then { residual = w, coeffs }
          else let h_j  = op.dot w V[j]                 -- dot against the progressively-subtracted w
                   w'   = axpy (-h_j) V[j] w            -- w^(j+1) = w^(j) − H_j·V[j]
                   c'   = coeffs `with` (j := h_j)
               in jloop (j+1) w' c'                     -- the recurrence: w' gates the next dot

The `case op.variant` is the L3 rendering of the L0 runtime dispatch (`OrthogonalizeIteration`'s
`switch (type)`, `iterative.cpp:313-323`); the variant is inspected exactly once. The CGS / CGS2
arms are straight-line global field statements (the basis index is a reduction/broadcast axis);
the MGS arm is the explicit `jloop` tail recursion over the basis index — the
`sequential-obstruction` made load-bearing at L3, the iteration view L3 exists to expose.

### Iteration-rotation marker

L3 is the iteration-rotation layer. `orthogonalize`'s iteration view is the relationship between
successive candidate states `w^(j) -> w^(j+1)` along the basis index — and the verdict splits by
variant:

- **The body lifts (all variants).** The per-column body — one `dot`, one `axpy` against whole
  tensors — is a global tensor-field expression by signature shape. This is shared across MGS /
  CGS / CGS2.
- **CGS / CGS2 lift entirely** — no `w^(j)` recurrence survives (`w_eff(j) = w` for all `j`); the
  `m` columns collapse to the batched `H = Vᴴw` / `w' = w − VH` global statements (`[dot × m,
  allreduce, axpy × m]` for CGS, `[CGS] × 2` for CGS2). **No obstruction.**
- **The MGS `j`-loop does not lift** — `w^(j+1)` depends on `H_j`, which depends on `w^(j)`: the
  rank-1-projector composition is genuinely serial in `j`. A *symbolic* global form exists (the
  same projection `(I − V Vᴴ)w` that CGS computes) but evaluating it *as MGS* re-derives the
  serial recurrence; replacing it with the batched form **is** replacing MGS with CGS, which
  loses the roundoff-orthogonality property MGS buys. Recorded as a
  [`sequential-obstruction`](../concepts/sequential-obstruction.md) over the basis index,
  field-side loop-carried state, numerical-stability-rooted.

This is the **variant-split partial obstruction**: body lifts (all variants), the loop lifts for
CGS/CGS2 and does not for MGS (per [`tensor-field-lift`](../concepts/tensor-field-lift.md)). It
is **identity-in-form to the L2 body** precisely because the lift split is in the surrounding
loop structure, not in the per-step body — and the L2 entry records the same split as the
collective-shape residual axis (m×1 vs 1×m vs 2×m) and the MGS column-order non-commutativity
non-law.

## Algebraic laws

The laws below hold; absences are deliberate. They are the L2 laws restated in L3 vocabulary
(the per-step body is identity-in-form), with the variant-split obstruction structure made
explicit at L3. "Exact" means exact arithmetic with an exactly orthonormal input basis `V`;
floating-point caveats are recorded as explicit non-laws.

1. **Orthogonality (the defining contract).** `op.dot(residual, V[i]) = 0` for all
   `i ∈ [0, m)` (exact). This is the contract shared by **all three variants** — it is what
   makes them substitutable as the same operator. Witnessed empirically across MGS / CGS / CGS2
   at `test-orthog.cpp:154-159` (the per-rank orthogonality-check loop — leading comment at
   `:154`, the `for` opens at `:155`, body runs `:155-159`; the
   `⟨residual, V[i]⟩ ≈ 0` assertion `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` is at line 158),
   under both the canonical and the `B`-weighted `op.dot`.

2. **Loss-free decomposition.** In exact arithmetic with orthonormal `V`,
   `w = residual + Σ_j coeffs[j]·V[j]` — a complete (loss-free) decomposition of `w` into its
   `span(V)` and `span(V)^⊥` parts. (The L3 restatement of L1/L2 leaf law 2.)

3. **Empty-prefix identity.** `orthogonalize op w [] = { residual = w, coeffs = [] }` for any
   `w` and any variant (the `m = 0` path, `orthog.hpp:62-64`; `test-orthog.cpp:99-120`).

4. **Variant agreement (exact).** MGS, CGS, and CGS2 produce the *same* `{ residual, coeffs }`
   in exact arithmetic with exactly orthonormal `V`. At the exact-arithmetic level the three are
   one operator; they diverge only in finite precision and in **iteration structure** (the L3
   lift verdict). This is the substitutability law that lets `krylov_step` carry the variant as
   a level-(b)-absorbed closure.

5. **Per-step body identity-in-form across the L3↔L2↔L1 chain.** The L3 per-step tensor-field
   body (one `dot` for `H_j`, one `axpy` for the residual update) maps line-for-line to the L2
   [`orthogonalize`](../L2/orthogonalize.md) `project`/`subtract` stages and, transitively
   (L3>L2 identity ∘ L2>L1 identity), is value-thread-isomorphic to the L1
   [`orthogonalize`](../L1/orthogonalize.md) leaf body. **This is a body-level law, not a
   loop-level one** — the L3 MGS loop-structure obstruction (non-law below) is not erased by the
   body identity.

6. **CGS / CGS2 global-lift law (the field-side iteration-rotation result).** For
   `op.variant ∈ {CGS, CGS2}`, the operator is the batched global tensor-field statement
   `coeffs = Vᴴw`, `residual = w − V·coeffs` (CGS2 = two such passes). The basis index `j` is a
   reduction/broadcast axis with no loop-carried dependency; the operation lifts to whole-tensor
   field arithmetic with no sequential obstruction. This is the **positive** half of the
   variant-split verdict — the half that lifts.

7. **`dot`-hook invariance of shape and lift verdict.** Substituting `op.dot` (canonical →
   `B`-weighted) leaves the per-step body, laws 1–6, **and the MGS/CGS lift split** unchanged;
   only the inner-product realisation differs and the orthogonality contract reads
   `⟨residual, V[i]⟩_B = 0`. The hook is a closure substitution, not a structural variant.

Laws that explicitly **do NOT** hold:

- **MGS loop lift to a single tensor-field op.** The MGS map `w^(j) ↦ w^(j+1)` is genuinely
  sequential in `j` (`w^(j+1)` reads `H_j` reads `w^(j)`); the per-column projector chain does
  **not** lift to one whole-tensor operation. **Sequential obstruction** — field-side
  loop-carried state, basis-index recurrence, numerical-stability-rooted — see
  Iteration-rotation marker. This is the half of the variant-split verdict that does *not* lift,
  and the reason this entry is `partial-obstruction` rather than `firm`.
- **Variant agreement in floating point.** Law 4 fails in finite precision: the three variants
  produce different `{ residual, coeffs }` at the bit level (and at larger amplitudes when `V`
  is ill-conditioned). MGS and CGS2 hold orthogonality to roundoff; CGS loses it faster for
  ill-conditioned bases. This *is* the load-bearing distinction motivating the variant axis (and
  the MGS obstruction's numerical-stability root). Inherited from L1/L2.
- **Column-order commutativity under MGS.** Permuting the columns of `V` changes the
  intermediate `w^(j)` and hence the MGS `{ residual, coeffs }` at the bit level (CGS/CGS2 are
  column-order-invariant up to reduction-tree noise; MGS is not, because the left-to-right
  rank-1-projector composition does not commute). This is the algebraic shadow of the MGS
  sequential obstruction. Inherited from L1/L2.
- **Reduction-tree associativity (floating point).** Inherited from [`dot`](./inner_product.md#specializations): different
  summation orders inside the projection give different bit-level coefficients. Load-bearing.
- **Stage-fusion across the CGS2 pass boundary.** The second CGS pass is not fusible with the
  first — fusing them would compute the correction against the *un*-orthogonalised `w` and
  destroy the re-orthogonalisation property. The `[CGS] × 2` shape is genuinely two passes.
  Inherited from L2.
- **Linearity / idempotence at the bit level.** The leaf's linearity and idempotence
  (`(I − V Vᴴ)² = (I − V Vᴴ)`) are exact-arithmetic identities; in floating point they hold only
  up to the orthogonality floor of the chosen variant. Inherited from L1/L2.

## Dependencies

**Same-layer (L3)** — the per-step body references the L3-native whole-tensor primitives by
their L1 names (L3-native by signature shape, each operating on whole tensors with no element
loop exposed):

- [`dot`](./inner_product.md#specializations) — the projection-coefficient inner product `H_j = op.dot(w_eff(j), V[j])`
  (and, for CGS/CGS2, the batched `coeffs = Vᴴw` reduction). The conjugate-linear
  first-argument convention is inherited; the `op.dot` hook is a `dot` substitution.
- [`axpy`](./linear_combination.md#arity-specializations) — the rank-1 residual update `w − H_j·V[j]` = `axpy(-H_j, V[j], w)` (and,
  for CGS/CGS2, the batched `w − V·coeffs` subtraction).

`orthogonalize` does **not** depend on the L3 reductions in a normalisation role:
[`nrm2`](./inner_product.md#consumer-nrm2-and-matrix-weighted-norm) and [`scal`](./linear_combination.md#arity-specializations) are the **caller's** normalisation step (the
Hessenberg sub-diagonal + rescale), excluded by the L0 header's "does not normalize the output"
contract — they are not dependencies of this operator.

**Cross-cutting concepts:**

- [`sequential-obstruction`](../concepts/sequential-obstruction.md) — the classification for the
  MGS `j`-loop (`:37-48`, the canonical MGS-as-sequential-obstruction example; `:22`, the
  CGS-as-parallel-alternative note).
- [`tensor-field-lift`](../concepts/tensor-field-lift.md) — the body-lifts / MGS-loop-doesn't
  variant-split partial case.
- [`variant-absorption`](../concepts/variant-absorption.md) — the `gs_orthog` axis absorbed at
  all three levels under residual-axis disclosure (`:131`); at L3 a documented invariant (the
  variant is inspected once, the body does not re-branch per column).

**Adjacent-layer siblings:**

- L2: [`orthogonalize`](../L2/orthogonalize.md) (firm) — the named `project ▷
  subtract` composition this entry's body is identity-in-form to; the per-variant collective
  shape it discloses as the residual axis is the L2 reading of this entry's lift split.
- L1: [`orthogonalize`](../L1/orthogonalize.md) (firm) — the pure leaf the body is
  value-thread-isomorphic to (transitively; in-line annotation, no `L3-L1/` directory).
- L4: no firm `L4/orthogonalize.md` (unauthored; the natural Arnoldi-step-monad target is a
  future dispatch).

The **substantive** rotation is downward in two places. At L1>L0 the in-place `w` overwrite
(`w.Add(-H[j], V[j])`), the raw-pointer `H` write, and the per-variant collective shape are
narrated forward from L1 to L0 by the firm
[`orthogonalize-mutation-rotation`](../L1-L0/orthogonalize-mutation-rotation.md) theme (and the
L2>L1 [`orthogonalize-composition-lowering`](../L2-L1/orthogonalize-composition-lowering.md)
theme narrates the L2 composition into the L1 leaf). At L3>L2 the **per-step `dot`+`axpy` body** is
identity-in-form (annotated in-line above, per the non-adjacent-identity convention), but
the **variant-split loop rotation** — the MGS `jloop` tail recursion collapsing into the L2
per-variant sequencing, and the CGS/CGS2 batched-arm straight-line statements collapsing into the
L2 collective-shape residual axis — is **substantive** and is narrated forward from L3 to L2 by the
[`orthogonalize-variant-split`](../L3-L2/orthogonalize-variant-split.md) theme. The
L3>L2 edge therefore carries both an in-line body-identity note (the per-step body) and a dedicated
theme (the loop-structure variant split).

## Variant axes

Three axes; the **`gs_orthog`** axis is the one the L3 lift verdict splits along, and the
distinguishing feature of this entry against the precedent partial-obstruction operators:

1. **gs_orthog** (`MGS | CGS | CGS2`) — the primary runtime axis, absorbed at construction
   (per [`variant-absorption`](../concepts/variant-absorption.md) `:131`, all three levels under
   residual-axis disclosure). At L0 these are `OrthogonalizeColumnMGS`,
   `OrthogonalizeColumnCGS`, and `OrthogonalizeColumnCGS(refine=true)`, dispatched by
   `OrthogonalizeIteration` (`iterative.cpp:313-323`). **The L3 lift verdict splits along this
   axis**: `MGS` is a **non-lifting** sequential obstruction (`[dot, axpy] × m` serial chain, `m`
   reductions of size 1, each gating the next; numerical-stability-rooted); `CGS` **lifts** to
   the batched `[dot × m, allreduce, axpy × m]` global statement (one reduction of size `m`);
   `CGS2` **lifts** to `[CGS lift] × 2` (two reductions of size `m`, second pass non-fusible). At
   L3 the body does not branch per column; the variant selects the *iteration structure* (and
   hence whether the operation lifts), not the per-step body. **Householder is scoped out**:
   Palace's L0 has no Householder path (`orthog.hpp` defines exactly the two functions
   `OrthogonalizeColumnMGS` / `OrthogonalizeColumnCGS`), so it is out of scope per the
   unimplemented-component policy (inherited from the L1/L2 leaf scope-out at
   `variant-absorption.md:131`).
2. **dot-hook** (`canonical ⟨·,·⟩ | B-weighted`) — parametric absorption; the body shape, laws
   1–7, **and the MGS/CGS lift split** are invariant under the substitution (only the
   inner-product realisation differs, the orthogonality contract reads `⟨residual, V[i]⟩_B = 0`).
   The canonical hook is the GMRES/FGMRES Arnoldi default; the `B`-weighted hook is the SLEPc/ROM
   basis-extension substitution.
3. **element-type** (`real | complex`) — fully parametric, absorbed by the `op.dot` dependency
   (the conjugation lives in [`dot`](./inner_product.md#specializations)); it does not produce distinct operators at L3,
   and the lift verdict is element-type-invariant. All parametric tests cover both element types
   (`test-orthog.cpp:123` real, `:234` complex).

## Status

`partial-obstruction` — the **per-step body** (one `dot` for the coefficient, one `axpy` for the
residual update) lifts cleanly to a global tensor-field expression for **all three variants**
(whole-tensor by signature shape, identity-in-form to the firm L2 `project`/`subtract` stages
and the firm L1 leaf body); the **CGS / CGS2 loop structure also lifts** (the batched
`H = Vᴴw` / `w' = w − VH` global statements, law 6); but the **MGS `j`-loop is a witnessed
`sequential-obstruction`** (field-side loop-carried candidate `w^(j)`, basis-index recurrence,
non-removable because the batched form *is* CGS — the serial projector chain is what buys MGS's
roundoff-orthogonality) with a cited non-removability reason (numerical stability;
`concepts/sequential-obstruction.md:37-48`). This is the **third** `partial-obstruction` L3 row
after `chebyshev` (numerical-stability obstruction, **unconditional**) and `eigsolve`
(opaque-library obstruction, **unconditional**); `orthogonalize`'s distinguishing feature
is that the obstruction is **variant-conditional** — present for MGS, absent for CGS/CGS2 — so
the partial-obstruction verdict splits along the `gs_orthog` axis. The body's algebraic laws are
syntactic identities on fully-specified C++ source (the `orthog.hpp:41-89` MGS/CGS bodies,
read in full) inherited from the firm L1/L2 entries; the obstruction structure is
explicit and cited. **Caveat (not a status reduction)**: the operator carries dedicated
parametric test coverage across all three variants (real / complex / B-weighted, the empty-basis
edge case, the direct substitutability assertion `⟨residual, V[i]⟩ ≈ 0`,
`test-orthog.cpp:99-160, 234`), exceeding the test bar of the precedent partial-obstruction
operators (`chebyshev` has no dedicated test). The `partial-obstruction` status reflects the
**MGS loop structure**, not the body — it is the honest L3 verdict for a Gram-Schmidt family
whose MGS branch is intrinsically serial, and it does not impeach the firm L1/L2 rows (whose
firmness is on the per-step body and the variant contract, both of which hold).

## L3 vs L2 distinction

- **L3**: value-threaded positional form `(op, w, V) -> { residual, coeffs }`. The
  iteration view is load-bearing — the `gs_orthog` variant selects the iteration structure, and
  L3 renders it explicitly: the CGS/CGS2 arms as straight-line global field statements (basis
  index a reduction/broadcast axis), the MGS arm as the explicit `jloop` tail recursion with the
  sequential obstruction named. The body lifts; the MGS loop does not.
- **L2**: named-composition form `orthogonalize { variant, dot } w V -> { residual, coeffs }`
  with the iteration view erased — the `project ▷ subtract` pipeline whose internal sequencing
  the variant selects, with the per-variant collective shape (m×1 / 1×m / 2×m reductions)
  disclosed as the residual axis. The MGS interleaving is recorded as the column-order
  non-commutativity non-law rather than as an explicit obstruction marker.

The L3>L2 hop erases the explicit iteration view (the `jloop` tail recursion / the batched-arm
straight-line statements collapse to L2's per-variant sequencing) and leaves the **per-step body**
identity-in-form. The body identity-in-form annotation lives in-line here (per the
meta-phase non-adjacent-identity convention; precedent `book/src/L3/chebyshev.md`,
`book/src/L3/eigsolve.md`); the **substantive loop-structure variant split** (which is NOT an
identity rotation — the MGS `jloop`/CGS-batched-arm collapse is a real rewrite) is the dedicated
[`orthogonalize-variant-split`](../L3-L2/orthogonalize-variant-split.md) L3>L2 theme (the
first substantive — non-identity — `L3-L2/` theme).

## Evidence

- `palace/linalg/orthog.hpp:18-23` — header scope contract: orthogonalises against a set of
  basis vectors using modified or classical Gram-Schmidt; "Assumes that the input vectors are
  normalized, but does not normalize the output vectors!" (`:22`) — the load-bearing
  no-output-normalisation contract (the `{ residual, coeffs }` record stops at the un-normalised
  residual). 
- `palace/linalg/orthog.hpp:41-53` — `OrthogonalizeColumnMGS`: the per-`j` loop
  `H[j] = dot_op(w, V[j]); Mpi::GlobalSum(1, &H[j], comm); w.Add(-H[j], V[j])` (`:46-52`). The
  interleaving of `dot` and `w.Add` in the **same** `j`-loop iteration — the `w.Add` feeding the
  next iteration's `dot` — is the source witness of the MGS **sequential obstruction**
  (`[dot, axpy] × m`, `m` reductions of size 1). The non-lifting half of the variant-split
  verdict. 
- `palace/linalg/orthog.hpp:57-89` — `OrthogonalizeColumnCGS`: empty-basis early return
  (`m == 0`, `:62-64`); `m` batched local dots into `H[0..m-1]` against the **original** `w`
  (`:66-69`); single `Mpi::GlobalSum(m, H, comm)` (`:70`); `m` batched `w.Add`s (`:71-74`); the
  `refine` branch (`:75-88`) re-enters with `dH`, accumulating `H[j] += dH[j]` (the CGS2 `[CGS]
  × 2` second pass). The dots-against-original-`w` structure is the source witness that CGS/CGS2
  **lift** (the basis index is a reduction axis, no recurrence): `H = Vᴴw`, `w' = w − VH`. The
  lifting half of the variant-split verdict. 
- `palace/linalg/iterative.cpp:308-325` — `OrthogonalizeIteration`: the runtime variant dispatch
  (`switch (type)` over `MGS / CGS / CGS2` at `:313-323`, `CGS2 = OrthogonalizeColumnCGS(...,
  true)` at `:321-322`); confirms the variant is bound at solver construction and dispatched
  once, against the leading `j + 1` columns — the L3 `case op.variant`. 
- `palace/linalg/iterative.cpp:630-632` — GMRES Arnoldi consumer:
  `OrthogonalizeIteration(gs_orthog, comm, V, w, Hj, j)` immediately followed by the caller's
  `Norml2` (sub-diagonal) and `scal` (normalisation) — confirming normalisation is the caller's,
  outside this operator. 
- `palace/linalg/iterative.cpp:809-811` — FGMRES Arnoldi consumer: the identical
  `OrthogonalizeIteration` call + `Norml2` + `scal` sequence. 
- `test/unit/test-orthog.cpp:99-120` — empty-prefix edge case: all three variants leave `w`
  unchanged (`m = 0` identity, law 3). 
- `test/unit/test-orthog.cpp:123-160` — parametric real test: all three variants zero the
  per-rank component and pass `⟨residual, V[i]⟩ ≈ 0` to `1e-12` (law 1, the substitutability
  witness); the orthogonality assertion `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` is at line 158,
  inside the check loop (leading comment `:154`, `for` opens `:155`, body `:155-159`); TEST_CASE
  closes at 160. 
- `test/unit/test-orthog.cpp:234` — complex parametrisation (the element-type axis). 
- `book/src/L2/orthogonalize.md` (firm) — the L2 named composition this entry's body
  is identity-in-form to; §Semantics `project`/`subtract` stages and the per-variant collective
  shape are the L2 reading of this entry's lift split. The L2 column-order-non-commutativity
  non-law is the L3 MGS obstruction.
- `book/src/L1/orthogonalize.md` (firm) — the L1 leaf the body is
  value-thread-isomorphic to (transitively, in-line); the coefficient/normalisation boundary and
  the variant-axis contract are inherited from it.
- `book/src/L3/chebyshev.md` (partial-obstruction) — the precedent for the
  body-lifts/loop-doesn't shape and the in-line identity-rotation annotation (§Downward); the
  contrast operator (numerical-stability obstruction, **unconditional**) vs this entry's
  **variant-conditional** obstruction.
- `book/src/L3/eigsolve.md` (partial-obstruction) — the second precedent
  (opaque-library obstruction, unconditional); the contrast on obstruction *root* (Palace
  authors no loop) vs this entry (Palace authors the MGS recurrence; the obstruction is
  numerical-stability-rooted like `chebyshev`).
- `book/src/concepts/sequential-obstruction.md:37-48` — the canonical
  MGS-as-sequential-obstruction structural argument (the L3 property this entry records);
  `:22` — the MGS example classifying CGS as the parallel-reduction alternative exposed as the
  `gs_orthog` variant.
- `book/src/L1-L0/orthogonalize-mutation-rotation.md` (firm) — the substantive downward rotation
  (the in-place `w` overwrite + raw-pointer `H` write + per-variant collective shape).
- `book/src/L2-L1/orthogonalize-composition-lowering.md` (firm) — the L2 composition → L1 leaf
  lowering.

## Supporting evidence

- The L3-cohort-growth audit verdict (B) at `book/src/L3/index.md:48`: "`orthogonalize` (MGS
  variant has sequential-obstruction at L3 explicitly noted at L1; CGS/CGS2 variants lift cleanly
  — would be a third `partial-obstruction` row after `chebyshev` and `eigsolve`)".
- The L1 leaf (`book/src/L1/orthogonalize.md:200-203`) and L2 composition
  (`book/src/L2/orthogonalize.md:133-134, 290-292`) both forecast this L3 entry: "The MGS branch
  carries a sequential-obstruction that surfaces at L3 (MGS has no global tensor-field form;
  CGS/CGS2 lift cleanly) — that obstruction is an L3 property of the variant, not an L1 contract
  distinction." This entry is that L3 property, formalised.

## Open questions / caveats

- **No firm L4 `orthogonalize`.** The `L4/orthogonalize.md` chapter is unauthored; the natural
  L4 target is the Arnoldi-step-monad auxiliary stage that `krylov_step` carries as `op.orthog`.
  This entry lifts from L2 only and notes the L4 surface as a future direction.
- **MGS-obstruction-root parallel with `chebyshev` (not `eigsolve`).** The MGS obstruction is
  numerical-stability-rooted (Palace authors the serial recurrence to buy roundoff-orthogonality)
  — the same *root* as `chebyshev`, distinct from `eigsolve`'s opaque-library root. But unlike
  both precedents the obstruction is **variant-conditional** (present for MGS, absent for
  CGS/CGS2): a partial-obstruction sub-shape (variant-split) the existing MGS example in
  `concepts/sequential-obstruction.md` already covers structurally.
