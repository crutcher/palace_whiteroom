# orthogonalize-variant-split

The L3>L2 lowering theme for the `orthogonalize` Gram-Schmidt family. The rewrite is
**substantive (non-identity)** along **one variant branch**: at L3 the operator is a
`partial-obstruction` whose iteration view splits by the `gs_orthog ∈ {MGS, CGS, CGS2}` axis —
the MGS `j`-loop is a first-class `sequential-obstruction`, while CGS/CGS2 lift to batched global
tensor-field statements. The L3 `case op.variant` form (the CGS/CGS2 straight-line global
statements + the explicit MGS `jloop` tail recursion carrying the named obstruction) **dissolves**
into the L2 `project ▷ subtract` per-variant-sequenced composition, and the named MGS
`sequential-obstruction` is **erased to its L2 shadow** (the column-order-non-commutativity non-law
+ the collective-shape residual-axis disclosure `m×1`/`1×m`/`2×m`). This is the **variant-split**
analogue of the sibling driver theme [`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md): there
the *whole* operator is the loop and the erasure is unconditional; here the operator is a
GS-family whose erasure shadows the **MGS branch only**, with the CGS/CGS2 branches clean lifts on
both sides of the hop.

## Slug

`orthogonalize-variant-split`

## Context

The `orthogonalize` lowering chain spans the layer-edges of the artifact:

- **L1 firm** ([`L1/orthogonalize`](../L1/orthogonalize.md), cycle-012) — the single pure leaf
  `orthogonalize(w, V, variant) → (w', H)`; the GS variant is an opaque parameter inspected once,
  the per-variant collective shape recorded as a *property* (a variant-axis note + the
  column-order-non-commutativity non-law).
- **L2 firm** ([`L2/orthogonalize`](../L2/orthogonalize.md), cycle-012) — the **named composition**
  `(op, w, V) -> { residual, coeffs }` = `project ▷ subtract`, with the variant's load-bearing
  difference disclosed as the **collective-shape residual axis** (`m` reductions of size 1 for MGS,
  one of size `m` for CGS, two of size `m` for CGS2). The iteration view is erased. The RHS of this
  theme.
- **L2>L1 firm**
  ([`L2-L1/orthogonalize-composition-lowering`](../L2-L1/orthogonalize-composition-lowering.md)) —
  the un-collapse of the L2 named composition into the L1 leaf; variant-dispatch and per-lowered
  reduction-order pinning.
- **L3 firm** ([`L3/orthogonalize`](../L3/orthogonalize.md), cycle-040) — the **iteration-rotation**
  view: the value-threaded `(op, w, V) -> { residual, coeffs }` with the `gs_orthog` axis selecting
  the iteration structure rendered explicitly — CGS/CGS2 as straight-line global field statements
  (basis index a reduction/broadcast axis), MGS as the explicit `jloop` tail recursion carrying the
  first-class `sequential-obstruction`. The **third** `partial-obstruction` L3 operator, and the
  first whose obstruction is **variant-conditional**. The LHS of this theme.
- **L3>L2 firm — this theme.** Narrates how the L3 variant-split iteration-rotation form lowers into
  the L2 per-variant-sequenced composition. **Substantive (non-identity)** on the MGS branch (the
  iteration view is erased and the named obstruction shadows to the L2 non-laws); identity-in-form on
  the per-step body; clean-lift on the CGS/CGS2 branches.

This theme is the **second substantive L3>L2 theme**, after the sibling
[`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md). The two share the structural shape
"substantive iteration-rotation erasure" — the L3 explicit iteration form (tail recursion +
named `sequential-obstruction`) dissolves into the L2 surface where the iteration view is erased and
the obstruction survives only as L2-vocabulary non-laws. The **distinguishing feature** of this
theme is that the erasure is **variant-conditional**: the MGS branch carries the substantive
erasure, while the CGS/CGS2 branches are clean global lifts on *both* sides of the hop (the L3 CGS/CGS2
arms are straight-line global statements, and the L2 CGS/CGS2 stages are separated `[dot×m,
allreduce, axpy×m]` / `[CGS]×2`). See §"Variant-split / unconditional-erasure contrast".

## L3 form (LHS)

The L3 form is reproduced from [`L3/orthogonalize`](../L3/orthogonalize.md) §"Value-threaded form
(L3 rendering)" — the `case op.variant` form with the iteration structure rendered explicitly:

    orthogonalize :: (op, w, V) -> { residual, coeffs }
    orthogonalize op w V =
      case op.variant of
        CGS  -> let coeffs   = batched_dot V w           -- H = Vᴴw : one global reduction (j is a reduction axis)
                    residual = batched_subtract w coeffs V   -- w − V H : one global matvec (j is a broadcast axis)
                in { residual, coeffs }                  -- LIFTS: no inter-j recurrence
        CGS2 -> let (h1, w1) = cgs_pass w V              -- first clean lift
                    (dh, w2) = cgs_pass w1 V             -- second clean lift (against once-projected w1; non-fusible)
                in { residual = w2, coeffs = h1 + dh }   -- LIFTS: [CGS lift] × 2
        MGS  -> jloop 0 w (zeros m)                      -- SEQUENTIAL OBSTRUCTION over basis index j
      where
        jloop j w coeffs =                               -- MGS per-column tail recursion (NON-lifting)
          if j >= m then { residual = w, coeffs }
          else let h_j = op.dot w V[j]                   -- dot against the progressively-subtracted w
                   w'  = axpy (-h_j) V[j] w              -- w^(j+1) = w^(j) − H_j·V[j]
                   c'  = coeffs `with` (j := h_j)
               in jloop (j+1) w' c'                      -- the recurrence: w' gates the next dot

The L3 form is value-threaded (positional `(op, w, V)`; no `Solve` monad, no `readonly`, no L1
opacity). The `case op.variant` is the L3 rendering of the L0 runtime dispatch
(`OrthogonalizeIteration`'s `switch (type)`); the variant is inspected exactly once. It carries the
**variant-conditional iteration-rotation verdict** (per [`L3/orthogonalize`](../L3/orthogonalize.md)
§"Iteration-rotation marker"): the per-step body lifts for all variants; the CGS/CGS2 *loops* lift
to the batched global statements; the **MGS `jloop`** is a first-class `sequential-obstruction` over
the basis index (field-side loop-carried candidate `w^(j)`, numerical-stability-rooted — the serial
projector chain is what buys MGS's roundoff-orthogonality). This obstruction is the L3 entry's reason
to exist on the MGS branch.

## L2 form (RHS)

The L2 form is reproduced from [`L2/orthogonalize`](../L2/orthogonalize.md) §Semantics — the named
`project ▷ subtract` composition with the iteration view erased and the per-variant sequencing
disclosed as the residual axis:

    orthogonalize :: (op: OrthogOp, w: Tensor[(S: ...)], V: Basis[N, m]) -> { residual: Tensor[S], coeffs: Tensor[m] }
    orthogonalize op w V =
      let coeffs   = project op.variant op.dot w V      -- the per-variant batched inner products
      let residual = subtract w coeffs V                -- w − Σ_j coeffs[j]·V[j]
      in { residual, coeffs }

where `project` / `subtract` are the two composition stages whose **interleaving** is the variant
axis (disclosed as the collective-shape residual axis, not rendered as iteration):

- **CGS** — `project` batches all `m` inner products against the same original `w` (one reduction of
  size `m`), then `subtract` applies all `m` updates. The two stages are **separated**:
  `[dot × m, allreduce_sum, axpy × m]`. No inter-`j` ordering.
- **MGS** — `project` and `subtract` are **interleaved per column**: `[dot, axpy] × m` (`m`
  reductions of size 1, each gating the next). The interleaving is the
  [`sequential-obstruction`](../concepts/sequential-obstruction.md) that blocks MGS's global
  tensor-field form *at L3*; **at L2 it is recorded as the column-order non-commutativity non-law
  and the `m×1` residual axis**, not as an explicit obstruction marker.
- **CGS2** — the CGS composition applied twice: `[CGS chain] × 2` (two reductions of size `m`); the
  second pass is non-fusible.

The L2 form **erases the iteration view** per [`L2/index`](../L2/index.md) §Context: the variant
tag is inspected once, the composition body's textual shape does not branch per column, and the
per-variant difference is disclosed as the *number and size* of reductions (the residual axis), not
as a rendered loop. **No `sequential-obstruction` is named at L2.** The obstruction survives only as
the two L2 §"Algebraic laws" non-laws: **"Column-order commutativity under MGS"** does not hold (the
L2 statement of "the MGS projection is sequential," without rendering the iteration), and the
residual-axis disclosure itself (`m×1` MGS vs `1×m` CGS vs `2×m` CGS2 — the L2 statement of "MGS
synchronises per column where CGS synchronises once").

## Rewrite shape

The rewrite is the **substantive, variant-conditional erasure of the iteration view**, with the
per-step body identity-in-form. The hop has three branches, one per variant; the MGS branch carries
the substantive content, the CGS/CGS2 branches are clean lifts on both sides.

1. **The per-step body is identity-in-form (all variants).** The L3 inner-step body — one
   [`dot`](../L3/dot.md) for `H_j = op.dot(w_eff(j), V[j])`, one [`axpy`](../L3/axpy.md) for
   `w − H_j·V[j]` — maps line-for-line to the L2 `project`/`subtract` stage primitives. This is the
   same body-identity the BLAS-1 `-body-identity` cohort records for its leaves; it is **shared
   across MGS / CGS / CGS2** and is not the substantive content of this hop.

2. **CGS / CGS2 branches: clean lift on both sides (identity-on-the-lift).** At L3 the CGS arm is the
   straight-line `coeffs = Vᴴw; residual = w − V·coeffs` global statement (basis index a
   reduction/broadcast axis); the L2 CGS stages are the separated `[dot × m, allreduce, axpy × m]`
   composition. These are the *same* batched global statement at two resolutions — L3 names it as the
   lift (`H = Vᴴw` matvec), L2 names it as the separated `project ▷ subtract` stages with the `1×m`
   residual axis. **No obstruction on either side; the hop is information-preserving on these
   branches.** CGS2 is `[CGS lift] × 2` at L3 and `[CGS chain] × 2` at L2 — the non-fusibility of the
   second pass is preserved as the L2 "Stage-fusion across the project/subtract boundary (CGS2)" non-law (it was
   the L3 "CGS2 second pass non-fusible" note). The CGS/CGS2 branches carry **no substantive
   rotation**.

3. **MGS branch: substantive iteration-rotation erasure (the heart of the hop).** This is the
   load-bearing forward-narration step. At L3 the MGS arm is the explicit `jloop` tail recursion and
   the obstruction is **named and first-class** (the `w^(j)` recurrence does not lift; per
   [`L3/orthogonalize`](../L3/orthogonalize.md) §"Iteration-rotation marker"). At L2 the iteration
   view is erased — the MGS branch is the `project ▷ subtract` composition with `[dot, axpy] × m`
   interleaving disclosed as the `m×1` residual axis — so the obstruction is **not expressible** at
   the L2 surface (there is no rendered loop to attach it to). But it is not *gone*: it survives as
   the L2-vocabulary residue in:
   - the **"Column-order commutativity under MGS"** non-law (the L2 statement of "the left-to-right
     rank-1-projector composition is sequential and does not commute," without naming the iteration),
     and
   - the **collective-shape residual axis** `m×1` (the L2 statement of "MGS synchronises per column,"
     the disclosed shape of the erased loop).
   The L2 entry states the handoff explicitly (§Semantics, MGS bullet): "The interleaving is the
   `sequential-obstruction` that blocks MGS's global tensor-field form at L3 (CGS/CGS2 lift cleanly)."
   This theme is the forward narration of that handoff: **obstruction named-and-first-class at L3 →
   obstruction erased to its non-law + residual-axis shadow at L2, on the MGS branch only.**

The mapping at the variant-arm level:

| L3 arm | L2 form | Mapping |
|---|---|---|
| `CGS -> coeffs = batched_dot V w; residual = batched_subtract w coeffs V` | `project` (one reduction of size `m`) `▷ subtract` (`[dot×m, allreduce, axpy×m]`) | **Clean lift, both sides.** The L3 batched global statement `H = Vᴴw` / `w − VH` and the L2 separated `project ▷ subtract` are the same batched computation at two resolutions; basis index a reduction/broadcast axis. No obstruction, no rotation. L0 witness `orthog.hpp:66-74` (dots against original `w`, single `GlobalSum(m,…)`, batched `w.Add`s). |
| `CGS2 -> (h1,w1)=cgs_pass w V; (dh,w2)=cgs_pass w1 V; {w2, h1+dh}` | `[CGS chain] × 2` (two reductions of size `m`); second pass non-fusible | **Clean lift, both sides.** Two clean CGS lifts in sequence; the L3 "second pass non-fusible" note becomes the L2 "Stage-fusion across the project/subtract boundary (CGS2)" non-law. L0 witness `orthog.hpp:75-88` (the `refine` re-entry accumulating `H[j] += dH[j]`). |
| `MGS -> jloop 0 w (zeros m)` (explicit tail recursion + first-class `sequential-obstruction`) | `project ▷ subtract` interleaved `[dot, axpy] × m`; iteration view erased; `m×1` residual axis | **Substantive (non-identity).** The L3 EXPLICIT `jloop` tail recursion dissolves into the L2 per-column-interleaved composition referenced by its residual-axis shape; the iteration view is erased. **This is the branch where the iteration-rotation is erased — the heart of the hop.** L0 witness `orthog.hpp:46-52` (the `dot` + `w.Add` in the same `j`-loop iteration, the `w.Add` feeding the next iteration's `dot`). |
| (the MGS `sequential-obstruction` named in L3 §"Iteration-rotation marker") | (no surface statement; shadows to the L2 "column-order commutativity under MGS" non-law + the `m×1` residual axis) | **Substantive (non-identity).** The L3 first-class obstruction is **erased** from the L2 surface (no rendered iteration to attach it to) and survives only as the column-order-non-commutativity non-law + the residual-axis disclosure. **Variant-conditional**: this shadow attaches to the MGS branch only; CGS/CGS2 have no such non-law. |
| the per-step body (one `dot`, one `axpy`) — shared across all three arms | the `project`/`subtract` stage primitives | Identity-in-form. The per-step tensor-field body maps line-for-line; same `dot`/`axpy` calls. Not the substantive content (shared with the BLAS-1 `-body-identity` cohort). |

The mapping is total on the operator's structure, but unlike the BLAS-1 `-body-identity` cohort it is
**not** the identity-in-form mapping: the MGS arm carries a genuine rotation (explicit `jloop` tail
recursion → per-column-interleaved composition referenced by residual-axis shape) and a genuine
erasure (named obstruction → non-law + residual-axis shadow). Unlike the sibling
[`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md), the substantive content is **confined to one
variant branch**: the CGS/CGS2 arms are clean lifts with no rotation, and the per-step body is
identity-in-form across all arms. **This is the variant-split partial-obstruction made visible at the
L3>L2 edge.**

## Applicability conditions

The rewrite is valid when all of the following hold (satisfied for the firm L3 and L2 forms by
construction):

1. **The L3 form is the firm `L3/orthogonalize` variant-split partial-obstruction.** The `case
   op.variant` form with the CGS/CGS2 arms as straight-line global statements and the MGS arm as the
   explicit `jloop` tail recursion carrying the named `sequential-obstruction`. If a future
   orthogonalization variant lands at L3 with a different loop structure (Householder — currently
   scoped out, Palace's L0 has no Householder path, `orthog.hpp` defines exactly
   `OrthogonalizeColumnMGS` / `OrthogonalizeColumnCGS`), the erasure narration would need re-audit
   against the new branch. Per the unimplemented-component policy Householder is not an implementation
   target.
2. **The L2 form is the firm `L2/orthogonalize` named composition.** The `project ▷ subtract`
   pipeline with the iteration view erased per [`L2/index`](../L2/index.md) §Context, the per-variant
   sequencing disclosed as the collective-shape residual axis (`m×1`/`1×m`/`2×m`), and the MGS
   obstruction's shadow present as the "Column-order commutativity under MGS" non-law. The firm L2
   entry's §Semantics MGS bullet records the reverse direction in-line (the MGS interleaving "becomes
   the L3 obstruction"); this theme narrates the forward L3→L2.
3. **The per-step body's L3>L2 rotation is identity-in-form (shared with the BLAS-1 cohort).** The
   one-`dot`-one-`axpy` body maps line-for-line; this theme's substantive content is the *loop*
   (MGS branch), not the body. The body identity relies on the `dot`/`axpy` L3-native-by-signature
   classification (`krylov-step-body-identity.md:97`), which is stable for the BLAS-1 leaves this
   operator's body is built from.
4. **The variant-axis profiles are aligned across the hop.** Both forms close over the same three
   axes: `gs_orthog` (the axis the lift verdict — and this hop's substantive content — splits along),
   `dot`-hook (parametric; the body, laws, and the MGS/CGS split are invariant under the
   substitution), and element-type (parametric, absorbed by the `dot` dependency). The rotation does
   not interact with the parametric axes; it is confined to the `gs_orthog = MGS` branch.

## Justification kind

**`structural`** (dominant) with secondary **`reduction-chain`**.

**Structural (dominant)**: the substantive content is a structural fact about the layer surfaces —
the L3 MGS arm renders the iteration explicitly (a `jloop` tail recursion is a structural form), the
L2 MGS branch erases the iteration view to a per-column-interleaved composition referenced by its
residual-axis shape (a structural absence). The MGS `sequential-obstruction`'s erasure-to-shadow is
structural: the obstruction is a property of the explicit iteration structure, so erasing the
structure erases the named obstruction, leaving only the L2-expressible residue (the
column-order-non-commutativity non-law + the residual-axis disclosure). The **variant-split** is
itself a structural observation: the body's primitive sequence is shape-invariant across the hop (all
three arms), the CGS/CGS2 loops lift identically on both sides, and only the MGS loop's iteration
view is erased — a claim about the shapes of the two forms per variant branch, not about algebraic
laws or step-semantics, hence structural. This matches the dominant justification of the sibling
[`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md).

**Reduction-chain (secondary)**: the MGS `jloop` → per-column-interleaved-composition consolidation
is grounded in the small-step `iterate_while` semantics from the strawman
`book/src/design/l4_calculus.md` §3.7 — the L3 `jloop` tail recursion is the unfolded reduction
sequence of the per-column projection, and the L2 per-variant-sequenced composition is the folded
(un-unfolded) form referenced by its collective shape. The forward L3→L2 narration re-folds the
explicit reduction sequence back into the named composition. This is the reduction-chain backing for
the MGS arm; it is secondary because the load-bearing content (the iteration-view erasure +
obstruction shadow, variant-conditional) is structural.

**Abstraction-direction note**: L3 is the higher-abstraction layer for this edge (it has the
iteration rotation done and the MGS obstruction named); L2 is the lower-abstraction layer (it erases
the iteration view, disclosing the per-variant difference as the residual axis). The rotation
direction is L3 → L2: the L3 form lowers to the L2 form by **dissolving** the explicit MGS `jloop`
tail recursion into the per-variant-sequenced composition and **erasing** the named obstruction to
its non-law + residual-axis shadow, on the MGS branch only. This matches the methodology's high→low
lowering direction; the reverse (how the L2 column-order-non-commutativity non-law un-erases into the
L3 explicit MGS `jloop` + obstruction) is a working-note / OQ concern, recorded only in the L2 and L3
entries' in-line lift notes, not narrated here.

## Speculative L3 operators

**None.** This theme is the substantive variant-split erasure rotation between two firm endpoints; no
new L3 vocabulary is introduced. The L3 form referenced in the LHS is the firm
[`L3/orthogonalize`](../L3/orthogonalize.md) entry; the L2 form referenced in the RHS is the firm
[`L2/orthogonalize`](../L2/orthogonalize.md) entry. The per-step body's `dot` / `axpy` primitives are
firm at both layers ([`L3/dot`](../L3/dot.md), [`L3/axpy`](../L3/axpy.md); [`L2/dot`](../L2/dot.md),
[`L2/axpy`](../L2/axpy.md)); they are referenced, not introduced.

## Variant-split / unconditional-erasure contrast

The two substantive L3>L2 themes share the structural shape "iteration-rotation erasure" but differ
in **scope of the erasure**:

| | [`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md) | `orthogonalize-variant-split` (this theme) |
|---|---|---|
| L3 form | explicit `iterate_while_L3` tail recursion + named outer-loop `sequential-obstruction` | `case op.variant`: CGS/CGS2 straight-line global statements + explicit MGS `jloop` tail recursion + named MGS `sequential-obstruction` |
| L2 form | `iterate_while (krylov-step op) …` named-by-role; obstruction erased | `project ▷ subtract` per-variant-sequenced; iteration view erased; per-variant difference disclosed as residual axis |
| substantive content | iteration view erased; obstruction shadows to L2 fold non-laws | **MGS branch only:** iteration view erased; obstruction shadows to the column-order-non-commutativity non-law + the `m×1` residual axis |
| erasure scope | **unconditional** — the whole operator IS the loop | **variant-conditional** — the MGS branch carries the erasure; CGS/CGS2 are clean lifts on both sides; the per-step body is identity-in-form across all arms |
| obstruction root | trajectory scalars gate the next step (intrinsic step-boundary sequentiality) | MGS roundoff-orthogonality (numerical-stability-rooted; the serial projector chain is what MGS buys) |

The distinguishing structural fact this theme records: **a substantive L3>L2 iteration-rotation
erasure can be confined to a single variant branch.** The operator is not wholly an iteration (unlike
`ksp_solve`) — its CGS/CGS2 branches lift cleanly and its per-step body is identity-in-form. Only the
MGS branch carries the substantive erasure. This is the L3>L2-edge expression of the L3 entry's
**variant-conditional partial-obstruction** verdict: the partial-obstruction splits along the
`gs_orthog` axis, and so does this theme's substantive content.

## Verified-against

L3 evidence (the LHS):

- `book/src/L3/orthogonalize.md` (firm `partial-obstruction`, cycle-040) — the L3 variant-split form
  this theme references as LHS. §"Value-threaded form (L3 rendering)" (the `case op.variant` with the
  MGS `jloop` tail recursion), §"Iteration-rotation marker" (the variant-conditional verdict: body
  lifts all variants, CGS/CGS2 lift, MGS does not), §"CGS / CGS2 — the global lift" + §"MGS — the
  sequential obstruction", §Status (the `partial-obstruction` reflecting the MGS loop structure), and
  §"L3 vs L2 distinction" / §"Downward" (records the L3>L2 hop as erasing the iteration view, body
  identity-in-form — the same rotation this theme narrates forward).
- `book/src/L3/dot.md`, `book/src/L3/axpy.md` (firm) — the L3 per-step body primitives, identity-in-form
  across the hop.

L2 evidence (the RHS):

- `book/src/L2/orthogonalize.md` (firm, cycle-012) — the L2 named composition this theme references as
  RHS. §Signature (the `project ▷ subtract` surface), §Semantics (the per-variant sequencing
  `[dot,axpy]×m` MGS / `[dot×m, allreduce, axpy×m]` CGS / `[CGS]×2` CGS2 disclosed as the
  collective-shape residual axis; the MGS bullet's explicit "the interleaving is the
  `sequential-obstruction` that blocks MGS's global tensor-field form at L3 (CGS/CGS2 lift cleanly)"),
  §"Algebraic laws" non-laws "Column-order commutativity under MGS" + "Stage-fusion across the
  project/subtract boundary (CGS2)" (the L2-vocabulary shadow of the erased MGS obstruction + the
  CGS2 non-fusibility), §"L2 vs L1 distinction" (the iteration view erased to a property).

Sibling-theme evidence (the substantive-theme precedent):

- `book/src/L3-L2/ksp-solve-outer-driver.md` (firm, cycle-021) — the first substantive L3>L2 theme;
  the structural precedent for the iteration-view erasure + obstruction-to-non-law shadow rotation.
  §"Rewrite shape" step (2) ("The outer-loop `sequential-obstruction` erases from the surface,
  shadowing to the L2 non-laws") is exactly the rotation this theme makes variant-conditional. This
  theme's §"Variant-split / unconditional-erasure contrast" extends that precedent's
  kernel/driver-division template to the variant-split axis.

L0 evidence (self-verified against `reference/palace/` source on-disk via `read_range` + `citecheck
--anchor` this dispatch; the codemap is localization-only, citecheck/on-disk is the citation source
of truth per the cycle-027 brace-drift guard):

- `reference/palace/palace/linalg/orthog.hpp:18-23` — header scope contract: orthogonalises against a
  set of basis vectors using modified or classical Gram-Schmidt; "Assumes that the input vectors are
  normalized, but does not normalize the output vectors!" (`:22`) — the no-output-normalisation
  contract (the `{ residual, coeffs }` record stops at the un-normalised residual; `nrm2`/`scal` are
  the caller's, not dependencies). Self-verified.
- `reference/palace/palace/linalg/orthog.hpp:41-53` — `OrthogonalizeColumnMGS` (def `:41`): the per-`j`
  loop (`:46`) `H[j] = dot_op(w, V[j])` (`:49`); `Mpi::GlobalSum(1, &H[j], comm)` (`:50`); `w.Add(-H[j],
  V[j])` (`:51`). The `dot` and the `w.Add` in the **same** `j`-loop iteration — the `w.Add` feeding the
  next iteration's `dot` — is the L0 witness of the MGS `sequential-obstruction` (`[dot, axpy] × m`, `m`
  reductions of size 1). The non-lifting branch; the substantive-erasure branch of this hop.
  Self-verified.
- `reference/palace/palace/linalg/orthog.hpp:57-89` — `OrthogonalizeColumnCGS` (def `:57`): empty-basis
  early return (`m == 0`, `:62-64`); `m` batched local dots into `H[0..m-1]` against the **original**
  `w` (`:66-69`); single `Mpi::GlobalSum(m, H, comm)` (`:70`); `m` batched `w.Add`s (`:71-74`); the
  `refine` branch (`:75-88`) re-enters with `dH` accumulating `H[j] += dH[j]` / `w.Add(-dH[j], V[j])`
  (`:85-86`) — the CGS2 `[CGS] × 2` second pass. The dots-against-original-`w` structure is the L0
  witness that CGS/CGS2 **lift** (basis index a reduction axis, no recurrence). The clean-lift branches;
  no substantive rotation at this hop. Self-verified.
- `reference/palace/palace/linalg/iterative.cpp:308-325` — `OrthogonalizeIteration` (def `:308`): the
  runtime variant dispatch `switch (type)` over `MGS / CGS / CGS2` (`:313-323`; MGS→`OrthogonalizeColumnMGS`
  `:315-316`, CGS→`OrthogonalizeColumnCGS` `:318-319`, CGS2→`OrthogonalizeColumnCGS(..., true)`
  `:321-322`), orthogonalizing against the leading `j + 1` columns — the L0 source of the L3 `case
  op.variant` (variant inspected exactly once at dispatch). Self-verified.
- `reference/palace/palace/linalg/iterative.cpp:630-632` — GMRES Arnoldi consumer:
  `OrthogonalizeIteration(...)` (`:630`) immediately followed by the caller's `Norml2` (sub-diagonal) and
  `scal` (normalisation) — confirming normalisation is the caller's, outside this operator (the
  `{ residual, coeffs }` boundary preserved across the hop). Self-verified.
- `reference/palace/palace/linalg/iterative.cpp:809-811` — FGMRES Arnoldi consumer: the identical
  `OrthogonalizeIteration` (`:809`) + `Norml2` + `scal` sequence. Self-verified.
- `reference/palace/test/unit/test-orthog.cpp:99-120` — empty-prefix edge case ("...Empty"): all three
  variants leave `w` unchanged (`m = 0` identity; the `orthog.hpp:62-64` early return). Self-verified.
- `reference/palace/test/unit/test-orthog.cpp:154-159` — the per-rank orthogonality-check loop;
  the `⟨residual, V[i]⟩ ≈ 0` assertion `CHECK_THAT(dot, WithinAbs(0.0, 1e-12))` at line 158, witnessing
  the shared orthogonality contract (variant agreement / substitutability) across MGS / CGS / CGS2.
  Self-verified.

Strawman / combinator evidence (the reduction-chain backing):

- `book/src/design/l4_calculus.md` §3.7 — the `iterate_while` conventions source; the L3 MGS `jloop`
  tail recursion is the unfolded reduction sequence of the per-column projection, the L2 per-variant
  composition is the folded form referenced by its collective shape.
- `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for `iterate_while`
  looks like" (firm cycle-008) — the L3 tail-recursion rendering convention the L3 MGS `jloop` follows.

Cross-cutting concept references (consumed across the rotation):

- `book/src/concepts/sequential-obstruction.md` — the canonical MGS-as-sequential-obstruction
  structural argument (`:37-48`, the MGS-vs-CGS example: CGS `H = Vᴴ w` parallel statement vs MGS
  left-to-right rank-1 projector chain; `:41-42` the CGS/MGS structural contrast; `:22` the MGS-example
  classifying CGS as the parallel-reduction alternative exposed as the `gs_orthog` variant). Named
  first-class at L3 (MGS branch), erased to the column-order-non-commutativity non-law + residual-axis
  shadow at L2.
- `book/src/concepts/tensor-field-lift.md` — the body-lifts / MGS-loop-doesn't variant-split partial
  case; the lift that succeeds for CGS/CGS2 and fails for MGS.
- `book/src/concepts/variant-absorption.md` (`:131`) — the `gs_orthog` residual-axis disclosure
  discipline; the L2-side shadow shape (`m×1`/`1×m`/`2×m`) is the disclosed residual axis.

Open-questions ledger:

- This is the **first substantive L3>L2 theme for a `partial-obstruction` operator**, and the second
  substantive L3>L2 theme overall (after `ksp-solve-outer-driver`). The remaining substantive L3>L2
  rotations are `chebyshev` (in-line at `chebyshev-iteration` already; its obstruction is
  unconditional) and `eigsolve` (`partial-obstruction`, opaque-library-owned loop). Flagged for the
  meta-phase taxonomy review (see this report's §Open questions).

## Status

`firm` — the theme's content is firm: both endpoints are firm
([`L3/orthogonalize`](../L3/orthogonalize.md) `partial-obstruction` cycle-040;
[`L2/orthogonalize`](../L2/orthogonalize.md) firm cycle-012); the substantive non-identity content
(the variant-conditional iteration-view erasure on the MGS branch + the named MGS
`sequential-obstruction`'s shadow to the L2 column-order-non-commutativity non-law and the `m×1`
residual axis) is structurally grounded and citation-backed at both layers and the L0 source (the
`orthog.hpp:46-52` MGS interleaving + the `orthog.hpp:66-74` CGS dots-against-original-`w`, both read
in full and self-verified this dispatch); the per-step body's L3>L2 rotation is identity-in-form
(shared with the BLAS-1 `-body-identity` cohort); the CGS/CGS2 branches are clean lifts with no
rotation on either side; the rewrite-shape table is total on the operator's structure with the MGS
non-identity arm and the obstruction-shadow row explicitly delimited; no speculative L3 vocabulary is
introduced; the four applicability conditions are stated and confirmed. This is the **second
substantive L3>L2 theme** and the **first for a `partial-obstruction` operator**, extending the
sibling [`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md)'s unconditional iteration-rotation
erasure to the **variant-conditional** case: the substantive erasure is confined to the MGS branch,
the CGS/CGS2 branches lift cleanly, and the per-step body is identity-in-form.

Authored cycle-044 (abstractor), enacting **Identity-lowerings still require both L levels** (both
layers carry an `orthogonalize` entry; this theme is the connecting rotation — non-identity on the
MGS branch) and **Layers are defined high→low** (LHS L3, RHS L2, forward narration). Unlike the
BLAS-1 cohort (clean identity-lowerings) and the per-step body (identity-in-form), the L3>L2 rotation
here is **substantive on the MGS branch** — the iteration view is erased and the named obstruction
shadows to the L2 non-laws + residual axis.

## L3>L2 vs sibling-theme distinction

The two substantive L3>L2 themes both narrate an iteration-rotation erasure, divided by erasure
scope:

- **[`ksp-solve-outer-driver`](./ksp-solve-outer-driver.md) (driver loop)**: substantive
  **unconditional** — the whole operator IS the loop, so the explicit `iterate_while_L3` →
  outer-driver-by-role rotation is the whole content of the hop, erasing the iteration view and the
  named `sequential-obstruction` (which shadows to the L2 fold non-laws).
- **`orthogonalize-variant-split` (this theme)**: substantive **variant-conditional** — the operator
  is a GS-family whose CGS/CGS2 branches lift cleanly and whose per-step body is identity-in-form;
  only the MGS branch carries the substantive erasure (the explicit `jloop` tail recursion → the
  per-column-interleaved composition disclosed as the `m×1` residual axis, erasing the named MGS
  `sequential-obstruction` to the column-order-non-commutativity non-law + residual-axis shadow).

Together they map the two shapes a substantive L3>L2 erasure can take: whole-operator (the loop is
the operator) and variant-conditional (one branch of a variant-split partial-obstruction). The
distinguishing fact is the **scope of the erasure**, both rooted in a `sequential-obstruction` named
first-class at L3 and erased to its L2-vocabulary shadow.
