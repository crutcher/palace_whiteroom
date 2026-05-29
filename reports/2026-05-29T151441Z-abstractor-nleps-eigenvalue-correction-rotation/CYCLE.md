---
agent: abstractor
invoked_at: 2026-05-29T151441Z
scope: L1>L0 theme sketch — nleps-eigenvalue-correction-mutation-rotation
status: integrated
integrated_at: 2026-05-29T17:15:00Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-025 finalize (first primary cycle of meta-batch-7). NEW firm L1>L0 theme nleps-eigenvalue-correction-mutation-rotation (the per-step δλ Rayleigh-functional scalar-correction rotation over firm BLAS-1 leaves dot Sub-pattern A / axpbypcz γ=0 / scal negation; zero law additions). CLOSES the NEP-interior L1>L0 cohort 5/5 (apply-nonlinear-pencil/nleps-deflated-residual/nleps-deflated-solve/nleps-jacobian-action/nleps-eigenvalue-correction); the full per-step quasi-Newton chain is lowered L1>L0 end-to-end. L1-L0/index row + SUMMARY :106 inserted immediately after dispatch-1's nleps-jacobian-action (serial dependency held, primary anchors used). L1>L0 theme files 21→22. retroactive-budget 0; clean build. Carry-forward OQ: nleps-eigenvalue-correction-l1-entry-two-anchor-reanchor (co-schedulable with the jacobian-action re-anchor as one NLEPS-L1-entry citation-correction pass)."
inputs:
  - book/src/L1/nleps_eigenvalue_correction.md (firm L1 operator, cycle-024)
  - palace/linalg/nleps.cpp:672-677 (the undamped Newton eigenvalue-correction block — the positive L0 site)
  - book/src/L1-L0/nleps-deflated-residual-mutation-rotation.md (residual sibling theme)
  - book/src/L1-L0/nleps-deflated-solve-mutation-rotation.md (solve sibling theme)
  - book/src/L1-L0/apply-nonlinear-pencil-mutation-rotation.md (interior-atom sibling theme)
  - reports/2026-05-29T151441Z-abstractor-nleps-jacobian-action-rotation/CYCLE.md (dispatch-1 sibling, shares :673-676 lines)
---

# CYCLE: L1>L0 theme sketch — nleps-eigenvalue-correction-mutation-rotation

## Summary

The firm L1 operator `nleps_eigenvalue_correction` (landed firm cycle-024) is the per-step
**scalar quasi-Newton eigenvalue-correction** atom of the deflated NEP: given the committed
extended residual `[u; u2]`, the Jacobian action `w = J·v`, and the normalized projection
direction `[w0; w2]`, it computes the undamped Newton eigenvalue increment `δλ = −⟨[w0;w2],
[u;u2]⟩ / ⟨[w0;w2], w⟩` and assembles the coupled vector-step RHS `[z; z2] = [−δλ·w − u; −u2]`
the deflated linear solve inverts. This theme narrates **forward** how that pure-functional L1
form lowers into its L0 source pattern: the `// Undamped Newton step for the eigenvalue` block
inside `QuasiNewtonSolver`'s `while (it < nleps_it)` loop (`palace/linalg/nleps.cpp:672-677`).
The rewrite is **structural** — three sub-patterns: (A) the projected Newton ratio over firm
`dot` leaves (`:673-675`); (B) the big-space step RHS `z = −δλ·w − u` as a firm `axpby`
(`AXPBYPCZ` with `γ = 0`, `:676`); (C) the coordinate step RHS `z2 = −u2` as a firm `scal`
(`:677`). Every constituent is firm BLAS-1 vocabulary (`dot`, `axpby`, `scal`) read from a
positive site, so the theme lands `firm` with no `partly-constructive` caveat — matching the
residual / solve / pencil / jacobian-action siblings. **No speculative operators are proposed.**
This closes the NEP-interior L1>L0 cohort alongside dispatch 1
(`nleps-jacobian-action-mutation-rotation`).

**Citation source-of-truth (load-bearing for the integrator).** The self-verify pass via
`tools/citecheck/citecheck.py` against the on-disk `reference/palace/` checkout confirms that the
**primary site `:672-677` is on-disk-correct** — the codemap +1 drift wave-1 found applies only
to the deflation block at `:659+`, which precedes this theme's site. So the firm L1 entry
`book/src/L1/nleps_eigenvalue_correction.md`'s primary anchors `:672-677`, `:673`, `:674-675`,
`:676`, `:677` are all correct. **Two secondary-context anchors in that L1 entry are drifted**
(unrelated to the deflation-block +1): it cites the `while (it < nleps_it)` loop as `:596`
(on-disk **590**, −6) and the Armijo `α` backtrack-factor as part of the `:691`/`:708`/`:709`
range where `:709` is actually `res = res_trial` and the `alpha *= backtrack_factor` update is at
on-disk **712**. These are recorded as a carry-forward correction to *propose* in §Open questions
— not applied here (dispatch-phase write-authority partition). This theme uses the
citecheck-verified on-disk line numbers throughout.

## Proposed changes

```new:book/src/L1-L0/nleps-eigenvalue-correction-mutation-rotation.md
---
status: firm
layer: L1>L0
theme: nleps-eigenvalue-correction-mutation-rotation
l1_anchor: book/src/L1/nleps_eigenvalue_correction.md
l0_anchor: palace/linalg/nleps.cpp:672-677
justification: structural
---

# nleps-eigenvalue-correction-mutation-rotation

How the firm L1 [`nleps_eigenvalue_correction`](../L1/nleps_eigenvalue_correction.md) form lowers
into its L0 source: the `// Undamped Newton step for the eigenvalue` block inside Palace's
`QuasiNewtonSolver` NEP loop (`palace/linalg/nleps.cpp:672-677`). This is the **scalar**
eigenvalue half of the coupled quasi-Newton `(λ, v)` step — the scalar counterpart of the
vector-valued [`nleps-deflated-solve-mutation-rotation`](./nleps-deflated-solve-mutation-rotation.md)
(the solve *inverts* a block linear system to move the eigenvector; this correction computes a
*scalar ratio* `δλ` to move the eigenvalue and *assembles* the RHS the solve then inverts) and the
consumer of the Jacobian action produced by
[`nleps-jacobian-action-mutation-rotation`](./nleps-jacobian-action-mutation-rotation.md). Its
constituents are firm BLAS-1 leaves: the projected Newton ratio is three [`dot`](../L1/dot.md)
folds, the big-space step RHS is an [`axpby`](../L1/axpby.md), the coordinate step RHS is a
[`scal`](../L1/scal.md). This entry, with its dispatch-1 sibling
`nleps-jacobian-action-mutation-rotation`, completes the NEP-interior L1>L0 lowering cohort (with
the cycle-022/023 residual + solve themes and the cycle-024
[`apply-nonlinear-pencil-mutation-rotation`](./apply-nonlinear-pencil-mutation-rotation.md)).

## Slug

`nleps-eigenvalue-correction-mutation-rotation`

## Status

`firm` — every constituent of the rewrite is read from a **positive** source site (the
eigenvalue-correction block, `palace/linalg/nleps.cpp:672-677`, opened by the source's own comment
`// Undamped Newton step for the eigenvalue; the line search damps it.` at `:672`). The coordinate
inner product is the positive Eigen `w2.adjoint() * u2` (`:673`), the projected Newton ratio is the
positive scalar expression `-(linalg::Dot(GetComm(), u, w0) + u2_w0) / linalg::Dot(GetComm(), w,
w0)` (`:674-675`), the big-space step RHS is the positive `z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0)`
(`:676`), and the coordinate step RHS is the positive Eigen negation `z2 = -u2` (`:677`). The
rewrite is a **structural** syntactic expansion — no sub-part is materialized from negative
anchors, so there is no `partly-constructive` caveat. Every leaf is firm BLAS-1 vocabulary read
from a positive site ([`dot`](../L1/dot.md), [`axpby`](../L1/axpby.md), [`scal`](../L1/scal.md),
[`axpbypcz`](../L1/axpbypcz.md) the literal L0 form of the big-space RHS). This matches the
firm-on-positive-structure status of the operator this theme lowers
(`book/src/L1/nleps_eigenvalue_correction.md:114`) and of its residual / solve / pencil /
jacobian-action siblings: the laws are syntactic identities on fully-specified positive source, so
the NLEPS test-coverage absence (`search_text` for `QuasiNewton|nleps|funcA2|delta_eig` over
`test/unit/**` returns zero hits) does not gate the firm decision.

**The two non-syntactic facts are recorded as explicit non-laws, not asserted as identities**, so
they do not require a test to firm: (i) the `⟨[w0;w2], w⟩ = 0` near-singularity — the ratio
`δλ = −num/den` is a *partial* function, undefined when the projected Jacobian-apply vanishes, with
the source's own near-singular note at `:684-686` and recovery via the Armijo line search +
divergence-restart; and (ii) the **undamped** `δλ` — the committed eigenvalue is `eig + α·δλ` for
the Armijo `α` (`:691`, commit at `:708`), the line search's concern, not this atom's. The
*structure* (which inner products, the projection-direction conjugation, the `−num/den` ratio, the
two-term RHS) is fully positive.

## L1 form (LHS)

The pure-functional L1 operator — no destination buffers, no consume-then-reuse aliasing, no
Armijo `α` in the signature (`book/src/L1/nleps_eigenvalue_correction.md:16-32`):

    nleps_eigenvalue_correction
      :: (resid: ExtendedVec[N, k], jac_action: Tensor[N], proj_dir: ExtendedVec[N, k])
         -> NewtonStep[N, k]

    type ExtendedVec[N, k] = { big: Tensor[N], coord: Vec[k] }
    type NewtonStep[N, k]  = { δλ: Complex, z: Tensor[N], z2: Vec[k] }

    nleps_eigenvalue_correction(resid, jac_action, proj_dir) =
      let u   = resid.big,   u2 = resid.coord       -- committed extended residual [u; u2]
          w0  = proj_dir.big, w2 = proj_dir.coord    -- normalized projection direction [w0; w2]
          w   = jac_action                           -- Jacobian action J·v  (big-space only)
          num = dot(w0, u) + dot(w2, u2)             -- ⟨[w0;w2], [u;u2]⟩   projected residual
          den = dot(w0, w)                           -- ⟨[w0;w2], w⟩        projected Jacobian-apply
          δλ  = − num / den                          -- undamped Newton eigenvalue increment
          z   = axpby(−δλ, w, −1, u)                 -- −δλ·w − u           coupled vector-step RHS (big)
          z2  = scal(−1, u2)                         -- −u2                 coupled vector-step RHS (coord)
      in { δλ, z, z2 }

`resid` is the committed extended residual `[u; u2]` (written by the residual sibling at `:587`);
`jac_action` is the big-space-only Jacobian action `w = J·v` (written by the jacobian-action atom
at `:657`, no coordinate part — the extended Jacobian's lower block-row `[Xᴴ, 0]` is `λ`-independent,
`book/src/L1/nleps_eigenvalue_correction.md:68`); `proj_dir` is the normalized projection direction
`[w0; w2] = T(σ)⁻¹c` for a fixed random `c` (`:542-545`); `k = 0` is the un-deflated case (the
coordinate parts `u2`, `w2`, `z2` are empty, `num = dot(w0, u)`,
`book/src/L1/nleps_eigenvalue_correction.md:42`). The conjugated operand in all three inner
products is the **projection direction** (`w0` / `w2`), the **first** argument of the L1
[`dot`](../L1/dot.md) convention `⟨x, y⟩ = xᴴy` (`book/src/L1/dot.md:43`). The destination buffers
`z`/`z2`, the consume-then-reuse aliasing of `u`/`u2`, and the Armijo `α` are **not** in the L1
signature — they are exactly what this lowering exposes.

## L0 form (RHS)

The eigenvalue-correction block — **not** a named lambda (unlike the residual `compute_residual` /
solve `deflated_solve` siblings) but a straight-line block inside the quasi-Newton
`while (it < nleps_it)` loop (`palace/linalg/nleps.cpp:590`) that reads the committed-residual
buffers `u`/`u2`, the Jacobian-action buffer `w`, and the normalized projection-direction buffers
`w0`/`w2`, and writes into the in-out destination buffers `z` (a `ComplexVector`) / `z2` (an
`Eigen::VectorXcd`):

    // nleps.cpp:672 — the source's own statement of the undamped eigenvalue correction:
    // Undamped Newton step for the eigenvalue; the line search damps it.
    const std::complex<double> u2_w0 =                                   // :673  ⟨w2, u2⟩ = w2ᴴ u2
        std::complex<double>(w2.adjoint() * u2);
    const std::complex<double> delta_eig =                               // :674-675  δλ = −num/den
        -(linalg::Dot(GetComm(), u, w0) + u2_w0) / linalg::Dot(GetComm(), w, w0);
    z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0);                             // :676  z := −δλ·w − u
    z2 = -u2;                                                            // :677  z2 := −u2

## Rewrite — forward (L1 → L0)

The pure `nleps_eigenvalue_correction(resid, jac_action, proj_dir)` rewrites to the
eigenvalue-correction block, evaluated with the destination buffers `z`, `z2` (in place of the
returned `z`, `z2`) and producing the scalar `delta_eig` (in place of the returned `δλ`). The
rewrite proceeds in three sub-patterns. The L0-only material the L1 signature drops:

- **Destination buffers + consume-then-reuse aliasing.** `z` (a `ComplexVector`) and `z2` (an
  `Eigen::VectorXcd`) are overwritten in place (`:676`, `:677`); the L1 form returns `{ δλ, z, z2 }`
  by value. Crucially the source **consumes `u`/`u2` into `z`/`z2` here** so the subsequent
  line-search trial may freely overwrite `u`/`u2` — the source's own comment at `:700`
  (`// In-place writes into u, u2, A2n are safe: u/u2 were consumed into z above,`). This
  consume-then-reuse is a transparent L1>L0 buffer-lifetime trick, absorbed at L1 by the value
  return.
- **The Armijo `α` damping + commit.** The undamped `delta_eig` (`:674-675`) is applied damped:
  `eig_trial = eig + alpha * delta_eig` (`:691`) for the backtracking `α ∈ {1, 0.5, 0.25, …}`
  (`alpha *= backtrack_factor` at `:712`), with the eigenvector trial `v_trial` formed in lock-step
  (`:693-694`); the commit `eig = eig_trial` happens once the Armijo sufficient-decrease test passes
  (`:704-708`). The L1 operator produces the **undamped** `δλ`; the damping and commit are the
  line-search orchestration's concern (the `direct_newton` orchestration), absorbed at L1.
- **The projection-direction lag + normalization.** The projection direction `[w0; w2]` is the
  lagged deflated solve `T(σ)⁻¹c` normalized to unit extended-norm (`:542-545`); the lag
  (`σ = eig_opInv`) and per-use normalization are upstream numerical-Newton concerns, absorbed at
  L1 by the pre-normalized `proj_dir` argument.

The three sub-patterns are **sequentially coupled**: the ratio `δλ` (Sub-pattern A) is computed
first, then both the big-space RHS (Sub-pattern B, which reads `δλ` and `w` and `u`) and the
coordinate RHS (Sub-pattern C, which reads only `u2`) are assembled. Sub-pattern C is independent
of `δλ` (the structural big/coordinate asymmetry, §The big/coordinate RHS asymmetry).

### Sub-pattern A — projected Newton ratio: three `dot` folds → the scalar `δλ` (the `−num/den` ratio)

This is the load-bearing rotation point of the theme: `δλ` is a **scalar projected one-dimensional
Newton ratio** over the extended space, not a vector solve. Palace computes it in two C++ lines
(`:673-675`):

    const std::complex<double> u2_w0 = std::complex<double>(w2.adjoint() * u2);  // :673  w2ᴴ u2
    const std::complex<double> delta_eig =                                       // :674-675
        -(linalg::Dot(GetComm(), u, w0) + u2_w0) / linalg::Dot(GetComm(), w, w0);

Three firm-leaf recognitions:

1. **Coordinate inner product `w2ᴴu2` (`:673`).** The local Eigen `w2.adjoint() * u2` is the
   coordinate-space [`dot`](../L1/dot.md) `⟨w2, u2⟩`. Eigen `.adjoint()` is the conjugate-transpose,
   so the **projection-direction operand `w2` is conjugated** — the L1 `dot(w2, u2)`, arg-1
   (`book/src/L1/dot.md:43`). This term is rank-local (the coordinate space is replicated on all
   ranks); no `Mpi::GlobalSum` is involved.
2. **Big-space numerator + denominator inner products (`:675`).** `linalg::Dot(GetComm(), u, w0)`
   is the big-space `dot` `⟨w0, u⟩` and `linalg::Dot(GetComm(), w, w0)` is `⟨w0, w⟩`. Under the
   fused free-function convention `linalg::Dot(comm, x, y) = yᴴx` — the **second** C++ argument
   conjugated (`palace/linalg/vector.hpp:246`, corroborated by the `LocalDot` real/imag split
   `palace/linalg/vector.cpp:674-685`; the
   [`dot-mutation-rotation`](./dot-mutation-rotation.md) Sub-pattern A form) — with `x = u`,
   `y = w0` the **C++ arg-2 `w0`** is conjugated: `linalg::Dot(GetComm(), u, w0) = w0ᴴu` and
   `linalg::Dot(GetComm(), w, w0) = w0ᴴw`. This is the L1 `dot(w0, u)` / `dot(w0, w)` — the L1
   arg-1 convention names the **same** conjugated operand `w0` (the projection direction). The
   conjugation is **not re-derived here**; it is cited from `dot-mutation-rotation` Sub-pattern A.
3. **The ratio `δλ = −num/den` (`:674-675`).** The numerator
   `num = ⟨w0, u⟩ + ⟨w2, u2⟩ = w0ᴴu + w2ᴴu2 = ⟨[w0;w2], [u;u2]⟩` is the residual projected onto the
   direction `[w0; w2]` (the scalar "`f`"); the denominator `den = ⟨w0, w⟩ = w0ᴴw = ⟨[w0;w2], w⟩` is
   the Jacobian-times-eigenvector projected onto the same direction (the scalar "`f'`" — note `w`
   has **no coordinate part**, so only the big-space `w0ᴴw` appears, no `w2`-analog; the Jacobian
   action's big-space-only contract from the jacobian-action sibling). The increment `δλ = −f/f'`
   is the standard scalar Newton step lifted to the projected extended subspace. **This is the
   load-bearing structural fact that makes the eigenvalue update rank-one / scalar** rather than a
   full linear solve: the eigenvalue is a single complex unknown, corrected by a ratio of two
   extended-space inner products, not by an inverse-of-a-matrix.

The **extended-space sum** `num = w0ᴴu + w2ᴴu2` is one big-space distributed `dot` plus one local
Eigen `dot`, then a scalar add (`:674-675`); the ratio is a single complex division. There are
**no vector destination writes in this sub-pattern** — it produces only the scalar `delta_eig`.

Justification kind: **structural** — `:673-675` are the syntactic `dot` compositions of firm
leaves; the conjugation convention is inherited from `dot-mutation-rotation` Sub-pattern A
(big-space) and the Eigen `.adjoint()` form (coordinate); the `−num/den` ratio is the syntactic
scalar expression.

Citations:
- `palace/linalg/nleps.cpp:672` — `// Undamped Newton step for the eigenvalue; the line search
  damps it.` — the source's own naming of the operator.
- `palace/linalg/nleps.cpp:673` — `const std::complex<double> u2_w0 = std::complex<double>
  (w2.adjoint() * u2);` — the coordinate inner product `w2ᴴu2` (the local Eigen `dot`; arg-1 = `w2`
  conjugated).
- `palace/linalg/nleps.cpp:674-675` — `const std::complex<double> delta_eig = -(linalg::Dot
  (GetComm(), u, w0) + u2_w0) / linalg::Dot(GetComm(), w, w0);` — the projected Newton ratio: the
  big-space numerator `⟨w0, u⟩` and denominator `⟨w0, w⟩` (arg-2 = `w0` conjugated per
  `dot-mutation-rotation` Sub-pattern A; L1 arg-1 convention `book/src/L1/dot.md:43`), the
  extended sum `num = w0ᴴu + w2ᴴu2`, the `δλ = −num/den` ratio.
- `palace/linalg/vector.hpp:246` — `// Calculate the parallel inner product yᴴ x or yᵀ x` — the
  C++ free-function convention `linalg::Dot(comm, x, y) = yᴴx`, the **second** argument conjugated.
- `palace/linalg/vector.cpp:674-685` — `LocalDot(const ComplexVector &x, const ComplexVector &y)`
  — the real/imag split corroborating which operand is conjugated.
- `book/src/L1-L0/dot-mutation-rotation.md` — Sub-pattern A: the fused `linalg::Dot(comm, x, y) =
  yᴴx` (arg-2-conjugated); reused for the big-space numerator/denominator (not re-derived).

### Sub-pattern B — big-space step RHS: `AXPBYPCZ` (γ=0) → one `axpby` (the `−δλ·w − u` fused update)

The big-space coupled vector-step RHS `z = −δλ·w − u` is one fused C++ line (`:676`):

    z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0);   // :676   z := (−δλ)·w + (−1)·u + 0·z

Recognized as the firm [`axpby`](../L1/axpby.md): `z = axpby(−δλ, w, −1, u)`. The `AXPBYPCZ(α, x, β,
y, γ)` computes `z := α·x + β·y + γ·z`; here `α = −delta_eig`, `x = w`, `β = −1.0`, `y = u`, and the
third coefficient `γ = 0.0`, so the `γ·z` term vanishes and the destination `z` is **overwritten**
(not accumulated): `z = −δλ·w − u`. This is the `axpby ≺ axpbypcz` subsumption — the
[`axpbypcz`](../L1/axpbypcz.md) is the literal L0 build form; with `γ = 0` it reduces to the
two-vector [`axpby`](../L1/axpby.md) (the same `γ = 0` reduction recorded in
[`axpbypcz-mutation-rotation`](./axpbypcz-mutation-rotation.md) and the solve sibling's final
correction). The big-space RHS is the **linearized residual at the eigenvalue-corrected point**:
once `δλ` is fixed (Sub-pattern A), the eigenvector increment solves the linearized equation whose
RHS is `−(u + δλ·w)` — the residual plus the eigenvalue-correction's first-order contribution. This
coupling of the chosen `δλ` (through the Jacobian action `w`) into the eigenvector solve is what
makes the `(λ, v)` step a **genuine coupled Newton step** rather than two independent univariate
updates.

Justification kind: **structural** — `:676` is the syntactic `AXPBYPCZ` with `γ = 0` recognized as
the firm `axpby` leaf; the subsumption is inherited from `axpbypcz-mutation-rotation`.

Citations:
- `palace/linalg/nleps.cpp:676` — `z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0);` — the big-space
  step RHS `z = −δλ·w − u` (the `axpby` via `AXPBYPCZ` with `γ = 0`; `δλ` coupled in through `w`).
- `book/src/L1-L0/axpbypcz-mutation-rotation.md` — the `γ == 0` algebraic sub-rule reducing
  `AXPBYPCZ` to `axpby` (this theme references, not re-derives).

### Sub-pattern C — coordinate step RHS: Eigen negation → one `scal` (the `−u2` bare scaling)

The coordinate coupled vector-step RHS `z2 = −u2` is one Eigen line (`:677`):

    z2 = -u2;   // :677   z2 := (−1)·u2

Recognized as the firm [`scal`](../L1/scal.md): `z2 = scal(−1, u2)` — a pure scaling of the
coordinate residual by `−1`, into the destination `z2` (an `Eigen::VectorXcd`). This is the L0
realization of the coordinate vector-step RHS; the Eigen unary-minus on a `VectorXcd` is the
length-`k` rank-local scaling (no `Mpi::GlobalSum`, the coordinate space is replicated).

Justification kind: **structural** — `:677` is the syntactic Eigen negation recognized as the firm
`scal` leaf with `α = −1`.

Citations:
- `palace/linalg/nleps.cpp:677` — `z2 = -u2;` — the coordinate step RHS `z2 = −u2` (the `scal`
  with `α = −1`; rank-local Eigen scaling).
- `book/src/L1-L0/scal-mutation-rotation.md` — the `scal` mutation rotation (the negation form;
  this theme references the leaf).

## The big/coordinate RHS asymmetry — the load-bearing recording

The structural signature distinguishing this lowering is that **the eigenvalue increment `δλ`
couples into the big-space RHS `z` only (through the Jacobian action `w`), never into the
coordinate RHS `z2`**. The big-space RHS is `z = −δλ·w − u` (Sub-pattern B, depends on `δλ`); the
coordinate RHS is the bare negation `z2 = −u2` (Sub-pattern C, independent of `δλ` and of
`jac_action`). The asymmetry is the structural consequence of the Jacobian action being
**big-space only** — the extended Jacobian's lower block-row `[Xᴴ, 0]` is `λ`-independent, so its
parameter-derivative coordinate part is zero (`book/src/L1/nleps_eigenvalue_correction.md:68`;
witnessed by the jacobian-action sibling accumulating only into the big-space `w`, never a `w2`,
`palace/linalg/nleps.cpp:657`/`:668-669`). Because the Jacobian action has no coordinate part, the
denominator is `⟨[w0;w2], w⟩ = w0ᴴw` (only the big-space inner product, `:675`) and the eigenvalue
increment does not enter the coordinate RHS. Collapsing `z2` into a `δλ`-dependent form (by analogy
to `z`) would silently invent a coordinate Jacobian-coupling the source never computes.

Per the CLAUDE.md trick taxonomy this is a **load-bearing** recording (the big/coordinate asymmetry
is part of the algorithm, not a transparent rewrite): the structural-asymmetry law from the
operator entry (`book/src/L1/nleps_eigenvalue_correction.md:82`, law 4) is carried here.

## The Newton-ratio defining property — the algebraic characterization

`δλ` is the increment that zeroes the *projected linearized residual* to first order:

    ⟨[w0;w2], [u;u2]⟩ + δλ·⟨[w0;w2], w⟩ = 0     ⟺     δλ = −num/den

by construction (`:674-675` solves exactly this for `δλ`). This is the scalar Newton condition: the
residual projected onto `[w0; w2]`, plus the eigenvalue increment times the Jacobian-apply
projected onto `[w0; w2]`, vanishes. Recorded as the algebraic characterization of the ratio (it is
*why* the L0 formula is `−num/den`, `book/src/L1/nleps_eigenvalue_correction.md:80`, law 3). The
projection direction `[w0; w2]` is the deflated solve of a *fixed* random extended `c` (`:542`),
constant across the inner correction; its only role is to project the coupled extended system down
to the one-dimensional eigenvalue subspace (the source's own statement, `:540`,
`// ... only used as a projection direction for the eigenvalue correction ...`).

## Applicability conditions

The rewrite preserves semantics when:

1. **The three inputs are bound exactly as for the per-step chain** — `resid = [u; u2]` is the
   committed-point residual written by `compute_residual` (`:587`, the residual sibling);
   `jac_action = w` is the big-space-only Jacobian action written by `opJ->Mult(v, w)` + the
   deflation `AddMult`s (`:657`/`:668-669`, the jacobian-action sibling); `proj_dir = [w0; w2]` is
   the lagged-and-normalized deflated solve `T(σ)⁻¹c` (`:542-545`). The three are consistent within
   one outer iteration.
2. **Element type is complex-only** — the NEP pencil and the `ComplexVector` / `Eigen::VectorXcd`
   carriers. No real specialization is witnessed.
3. **The deflation cardinality `k` is variadic** — it grows by one per converged eigenpair
   (`:606-619`); the rewrite is parameterized by `k`, with the `k = 0` case the un-deflated
   degeneration (`u2`/`w2`/`z2` are zero-length `Eigen::VectorXcd`, so `w2.adjoint() * u2 = 0` at
   `:673` runs uniformly, `num = w0ᴴu`, `z2 = []`).
4. **In-place destination overwrite is permitted because `z`/`z2` are dead-on-entry scratch, and
   the consume-then-reuse of `u`/`u2` is licensed.** `z`/`z2` are overwritten (`:676`, `:677`);
   `u`/`u2` are consumed into `z`/`z2` here, which is why the subsequent line-search trial may
   overwrite them (`:700` comment). The execution order (`δλ` at `:673-675` → `z`/`z2` at
   `:676-677`) is load-bearing: `z` reads the just-computed `δλ`.
5. **The denominator `⟨[w0;w2], w⟩` is nonzero** — the ratio `δλ = −num/den` is a partial function,
   undefined at the near-singular case the source notes (`:684-686`, `<w0, w> is near-singular`),
   recovered via the Armijo line search + the outer divergence-restart (`:637-647`). The undamped
   `δλ` does **not** commit `eig`; the commit is `eig = eig_trial` for the damped `α·δλ` (`:691`,
   `:708`) — the line-search's concern.
6. **Single-rank scope** (CLAUDE.md "Scope"): the `Mpi::GlobalSum` inside the big-space
   `linalg::Dot` reductions (`:675`) lowers to a local no-op on one rank but is structurally present
   and carries the bit-deterministic-reduction-order trade-off (inherited from
   `dot-mutation-rotation`). The coordinate `w2.adjoint() * u2` (`:673`) and the `z2 = -u2` Eigen
   scaling (`:677`) are rank-local by construction (the coordinate space is replicated on all
   ranks).

## Justification kind

**Structural** — the rewrite is the syntactic expansion of one pure L1 form into the L0
destination-buffer composition. Three structural recognitions carry the theme: (A) `:673-675` is
the projected Newton ratio recognized as three firm `dot` folds (big-space numerator/denominator +
coordinate numerator) composed into `δλ = −num/den`, with the conjugated operand the projection
direction; (B) `:676` is the big-space step RHS recognized as the firm `axpby` (the `AXPBYPCZ` with
`γ = 0`); (C) `:677` is the coordinate step RHS recognized as the firm `scal` (`α = −1`). The one
load-bearing structural recording is the **big/coordinate RHS asymmetry** (`δλ` couples into `z`
only, never `z2` — the Jacobian action's big-space-only contract), read straight off the verified
site; it does not change the structural character of the lowering but must be carried, not
absorbed. The two non-syntactic facts — the `⟨[w0;w2], w⟩ = 0` near-singularity and the Armijo
damping — are recorded as explicit non-laws above, not asserted as identities. The in-place
destination overwrite, the consume-then-reuse of `u`/`u2`, the projection-direction lag +
normalization, and the Armijo `α` are L1>L0 residues recorded above.

## Speculative L1 operators

**None.** Every constituent is **already firm L1 BLAS-1 vocabulary**: [`dot`](../L1/dot.md) (firm),
[`axpby`](../L1/axpby.md) (firm), [`scal`](../L1/scal.md) (firm), [`axpbypcz`](../L1/axpbypcz.md)
(firm, the literal L0 form of the big-space RHS). This theme composes existing firm leaves; it
proposes no new rough-in operators. This matches the residual / solve / pencil / jacobian-action
sibling themes, all of which proposed zero speculative operators.

## Verified-against

L0 evidence ranges — **self-verified this invocation** via `tools/citecheck/citecheck.py`
(`--anchor` token-drift check + `--show` line-map confirmation) against the on-disk
`reference/palace/` checkout, the producer-citation self-verification discipline
(`verify-citation-range`). The wave-1-discovered codemap +1 drift applies only to the deflation
block at `:659+`, which **precedes** this theme's `:672-677` primary site; the primary site is
confirmed on-disk-correct. All line numbers below are the on-disk ground truth:

- `palace/linalg/nleps.cpp:672-677` — the complete eigenvalue-correction block (the positive L0
  site). Comment `:672` ("Undamped Newton step for the eigenvalue; the line search damps it.")
  names the operator. **Self-verified** (`citecheck --show` 670-680; 672-677 in bounds).
- `palace/linalg/nleps.cpp:673` — `const std::complex<double> u2_w0 = std::complex<double>
  (w2.adjoint() * u2);`. **Self-verified** (`citecheck --anchor 'w2.adjoint() * u2'` → line 673).
- `palace/linalg/nleps.cpp:674-675` — `const std::complex<double> delta_eig = -(linalg::Dot
  (GetComm(), u, w0) + u2_w0) / linalg::Dot(GetComm(), w, w0);`. **Self-verified** (`citecheck
  --anchor 'delta_eig'` → 674; `--anchor 'linalg::Dot(GetComm(), w, w0)'` → 675).
- `palace/linalg/nleps.cpp:676` — `z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0);`. **Self-verified**
  (`citecheck --anchor 'z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0)'` → line 676).
- `palace/linalg/nleps.cpp:677` — `z2 = -u2;`. **Self-verified** (`citecheck --anchor 'z2 = -u2'`
  → line 677).
- `palace/linalg/nleps.cpp:587` — `double res = compute_residual(eig, v, v2, u, u2, A2n);` — the
  committed-point residual writing `u`/`u2` (the `resid` argument; residual sibling producer).
  **Self-verified** (`citecheck --anchor 'compute_residual(eig'` → line 587).
- `palace/linalg/nleps.cpp:657` — `opJ->Mult(v, w);` — the big-space Jacobian action `w = J·v`
  (the `jac_action` argument; jacobian-action sibling producer; big-space-only). **Self-verified**
  (`citecheck --anchor 'opJ->Mult(v, w)'` → line 657).
- `palace/linalg/nleps.cpp:540` — `// The w0 vector is only used as a projection direction for the
  eigenvalue correction, so moderate accuracy suffices` — the source's statement of `[w0; w2]`'s
  role. **Self-verified** (`citecheck --anchor 'projection direction for the eigenvalue
  correction'` → line 540).
- `palace/linalg/nleps.cpp:542-545` — `deflated_solve(c, c2, w0, w2);` (`:542`), the extended-norm
  normalization (`norm_w0` at `:543`, `w0 *= 1/norm_w0` at `:544`, `w2 *= 1/norm_w0` at `:545`) —
  the projection direction `[w0; w2]` (lagged `T(σ)⁻¹c`, normalized; absorbed). **Self-verified**
  (`citecheck --show` 542-545).
- `palace/linalg/nleps.cpp:682` — `deflated_solve(z, z2, du, du2);` — the downstream deflated solve
  consuming this atom's output `[z; z2]` as its RHS (consumer; the solve sibling). **Self-verified**
  (`citecheck --anchor 'deflated_solve(z, z2, du, du2)'` → line 682).
- `palace/linalg/nleps.cpp:691` — `const std::complex<double> eig_trial = eig + alpha * delta_eig;`
  — the damped application of `δλ` (the "undamped" non-law). **Self-verified** (`citecheck --anchor
  'eig_trial = eig + alpha'` → line 691).
- `palace/linalg/nleps.cpp:704-708` — the Armijo sufficient-decrease test (`:704`) and the
  eigenvalue commit `eig = eig_trial` (`:708`). **Self-verified** (`citecheck --show` 704-708).
- `palace/linalg/nleps.cpp:712` — `alpha *= backtrack_factor;` — the Armijo backtrack-factor update
  (`α ∈ {1, 0.5, 0.25, …}`). **Self-verified** (`citecheck --show` 710-714).
- `palace/linalg/nleps.cpp:684-686` — the source comment `// ... <w0, w> is // near-singular ...`
  — the `⟨[w0;w2], w⟩ = 0` near-singularity (the well-definedness non-law). **Self-verified**
  (`citecheck --show` 684-686).
- `palace/linalg/nleps.cpp:700` — `// In-place writes into u, u2, A2n are safe: u/u2 were consumed
  into z above,` — the consume-then-reuse aliasing license. **Self-verified** (`citecheck --show`
  699-700).
- `palace/linalg/nleps.cpp:590` — `while (it < nleps_it)` — the quasi-Newton outer loop the block
  sits inside. **Self-verified** (`citecheck --show` 588-598; the L1 entry's `:596` is a −6 drift,
  carry-forward note below).
- `palace/linalg/nleps.cpp:637-647` — the divergence-restart branch (`restart++` at `:645`,
  `break` at `:646`) — the near-singular recovery context (the non-law). **Self-verified**
  (`citecheck --show` 637-647).
- `palace/linalg/nleps.cpp:606-619` — deflation-basis growth (normalize `:610-611`, store
  `X[k] = v` `:615`, `k++` `:619`) — the variadic-in-`k` axis. **Self-verified** (`citecheck
  --show` 606-619).
- `palace/linalg/nleps.cpp:354-362` — the deflation-scheme literature references (Effenberger 2013;
  Jarlebring–Koskela–Mele 2018; SLEPc-NEP minimality index 1) — the coupled quasi-Newton `(λ, v)`
  step this scalar correction is the eigenvalue half of. **Self-verified** (`citecheck --show`
  354-362).
- `palace/linalg/vector.hpp:246` — `// Calculate the parallel inner product yᴴ x or yᵀ x` — the
  C++ `Dot(comm, x, y) = yᴴx` convention (the conjugated operand). **Self-verified** (`citecheck
  --anchor 'inner product'` → line 246).
- `palace/linalg/vector.cpp:674-685` — `LocalDot(const ComplexVector &x, const ComplexVector &y)`
  — the real/imag split corroborating the conjugation. **Self-verified** (`citecheck --anchor
  'LocalDot'` → line 674).

L1 / cross-theme anchors:

- `book/src/L1/nleps_eigenvalue_correction.md` — the firm L1 operator this theme lowers (signature
  `:16-32`, Semantics `:48-70`, laws `:76-89`, Status `:114`, Evidence `:127-148`). **Drift note**:
  its `:596` (the `while` loop, on-disk **590**, −6) and `:709`-range (the Armijo `α` update is at
  on-disk **712**, not `:709` which is `res = res_trial`) are minor secondary-context drifts; the
  primary `:672-677` anchors are on-disk-correct. This theme uses the corrected on-disk numbers.
- `book/src/L1-L0/nleps-jacobian-action-mutation-rotation.md` — the jacobian-action sibling
  (dispatch 1): the producer of the big-space-only `jac_action = w` this correction consumes
  through `⟨w0, w⟩` (`:675`). Its `w`-is-big-space-only contract is the basis for this theme's
  big/coordinate RHS asymmetry.
- `book/src/L1-L0/nleps-deflated-solve-mutation-rotation.md` — the solve sibling: it inverts this
  atom's output `[z; z2]` (`:682`). This correction computes a *scalar* ratio + assembles the RHS;
  the solve *inverts* a block linear system — adjacent in the chain, structurally different
  (scalar-ratio + BLAS-1 RHS here, Schur-complement block solve there; the over-unification guard,
  `book/src/L1/nleps_eigenvalue_correction.md:110`).
- `book/src/L1-L0/nleps-deflated-residual-mutation-rotation.md` — the residual sibling: the producer
  of the committed `[u; u2]` this atom consumes (`:587`).
- `book/src/L1-L0/apply-nonlinear-pencil-mutation-rotation.md` — the interior pencil-apply atom; its
  firm-on-positive-structure status is the precedent for this entry's firm decision.
- `book/src/L1-L0/dot-mutation-rotation.md` — Sub-pattern A (fused `linalg::Dot(comm, x, y) =
  yᴴx`); reused for the big-space numerator/denominator (`:675`).
- `book/src/L1-L0/axpbypcz-mutation-rotation.md` — the `γ == 0` algebraic sub-rule reducing
  `AXPBYPCZ` to `axpby` (Sub-pattern B at `:676`).
- `book/src/L1-L0/scal-mutation-rotation.md` — the `scal` negation form (Sub-pattern C at `:677`).
- `book/src/L1/dot.md:43` — the L1 `⟨x, y⟩ = xᴴy` arg-1-conjugated convention (the three projected
  inner products).
- `book/src/L1/axpby.md` — the big-space step RHS `z = −δλ·w − u` leaf (`:676`).
- `book/src/L1/scal.md` — the coordinate step RHS `z2 = −u2` leaf (`:677`).
- `book/src/L1/axpbypcz.md` — the literal L0 form of the big-space RHS (`AXPBYPCZ`); the `γ = 0`
  subsumption to `axpby`.
- No dedicated unit test: NLEPS has zero `test/unit/**` hits (`QuasiNewton|nleps|funcA2|delta_eig`)
  — same absence as `eigsolve` / `apply_nonlinear_pencil` / `nleps_deflated_residual` /
  `nleps_deflated_solve` / `nleps_jacobian_action`; the firm decision rests on exhaustive positive
  structural citation.
```

```edit:book/src/L1-L0/index.md
[append this row to the L1>L0 dep-map table. INSERT ANCHOR: place it immediately AFTER dispatch-1's
`nleps-jacobian-action-mutation-rotation` row (which dispatch 1 inserts after the
`nleps-deflated-solve-mutation-rotation` row, line 34). The integrator applies dispatch 1 first
(serial), so the `| [nleps-jacobian-action-mutation-rotation](...)` row will exist when this report
is applied — anchor to it and insert after. FALLBACK if dispatch-1's row is not yet present: insert
after the `nleps-deflated-solve-mutation-rotation` row (line 34) so the NEP-interior cohort stays
grouped. The anchor file `nleps-eigenvalue-correction-mutation-rotation.md` is created by this
report, so the live-link form is correct]:

| [nleps-eigenvalue-correction-mutation-rotation](./nleps-eigenvalue-correction-mutation-rotation.md) | `L1/nleps_eigenvalue_correction` (firm) | `palace/linalg/nleps.cpp:672-677` (+ `:587`/`:657`/`:542-545` producers, `:682` consumer, `:691`/`:708` line-search) | firm *(structural; 3 sub-patterns A projected Newton ratio `−num/den` over `dot` / B big-space RHS `axpby` (`AXPBYPCZ` γ=0) `−δλ·w−u` / C coordinate RHS `scal` `−u2`; load-bearing big/coordinate RHS asymmetry — `δλ` couples into `z` only; `⟨w0,w⟩=0` near-singularity + undamped-`δλ` non-laws; reuses dot Sub-pattern A / axpbypcz γ=0)* |
```

```edit:book/src/SUMMARY.md
[add this chapter entry under the "L1 > L0 — Lowering" Part. INSERT ANCHOR: place it immediately
AFTER dispatch-1's `nleps-jacobian-action-mutation-rotation` entry, which dispatch 1 inserts after
the `apply-nonlinear-pencil-mutation-rotation` entry (line 105). The integrator applies dispatch 1
first (serial), so the `- [nleps-jacobian-action-mutation-rotation](...)` line will exist when this
report is applied — anchor to it and insert after, keeping the per-step chain
residual→jacobian-action→eigenvalue-correction→solve grouped. FALLBACK if dispatch-1's entry is not
yet present: insert after the `apply-nonlinear-pencil-mutation-rotation` entry (line 105)]:

- [nleps-eigenvalue-correction-mutation-rotation](./L1-L0/nleps-eigenvalue-correction-mutation-rotation.md)
```

## Speculative operators proposed

**None.** Every constituent of this theme is already firm L1 BLAS-1 vocabulary (`dot`, `axpby`,
`scal`, `axpbypcz` the literal L0 form of the big-space RHS). This theme composes existing firm
leaves into the L1→L0 rewrite; it introduces no rough-in operators for harvester promotion. This
matches the residual / solve / pencil / jacobian-action sibling themes, all of which proposed zero
speculative operators.

## Supporting evidence

- **L1 operator entry**: `book/src/L1/nleps_eigenvalue_correction.md` (firm, cycle-024) — the
  signature (`:16-32`), the five load-bearing semantic points (`:48-70`), the four algebraic laws +
  four non-laws (`:76-89`), the firm-on-positive-structure status (`:114`), and the per-line
  Evidence (`:127-148`). This theme narrates the forward lowering of that operator's pure form into
  its L0 source.
- **L0 positive site**: `palace/linalg/nleps.cpp:672-677` — the eigenvalue-correction block, the
  complete positive source for the operator's structure, read in full this invocation via
  `citecheck --show` (670-680).
- **Sibling themes** (read for structure/conventions): the solve sibling
  `book/src/L1-L0/nleps-deflated-solve-mutation-rotation.md` (the scalar/vector duality, the
  over-unification guard, the `[z; z2]`-as-RHS consumer relationship), the residual sibling
  `book/src/L1-L0/nleps-deflated-residual-mutation-rotation.md` (the `[u; u2]` producer), and
  dispatch-1's jacobian-action report (the big-space-only `w` producer, the shared `:673-676`
  citation range).
- **Citecheck self-verify**: all load-bearing anchors run through `tools/citecheck/citecheck.py`
  (`--anchor` drift check + `--show` line-map) against the on-disk `reference/palace/` checkout; the
  primary site `:672-677` confirmed on-disk-correct (no codemap +1 drift — that drift is confined to
  the deflation block at `:659+`). Two secondary-context anchors in the L1 entry found drifted
  (`:596` while-loop → on-disk **590**; Armijo `α` update → on-disk **712**), recorded as
  carry-forward.

## Open questions / caveats

1. **Carry-forward correction to PROPOSE (not apply) — L1 operator entry
   `nleps_eigenvalue_correction.md` carries two minor secondary-context anchor drifts.** The
   primary `:672-677` anchors (and the `:673`/`:674-675`/`:676`/`:677` sub-anchors) are
   **on-disk-correct** (the wave-1 codemap +1 drift is confined to the deflation block at `:659+`,
   which precedes this site). But two secondary anchors in the L1 entry are drifted, *independent*
   of the codemap-brace issue: (a) the `while (it < nleps_it)` outer-loop citation `:596` is the
   on-disk **590** (−6; the L1 entry's `:596` lands on the `restart, res` print argument); and (b)
   the Armijo `α` backtracking is cited via the `:691`/`:708`/`:709` range, but on-disk `:709` is
   `res = res_trial` and the `alpha *= backtrack_factor` update is at on-disk **712**. The
   `:691` (eig_trial), `:704-708` (Armijo test + `eig = eig_trial` commit), and `:688-714` (Armijo
   block range) anchors in the L1 entry are correct. This is a **change to propose**, not to apply
   (dispatch-phase write-authority partition): a follow-up lifter / repairer pass should re-anchor
   the L1 entry's `while`-loop citation (`book/src/L1/nleps_eigenvalue_correction.md:7`) from `:596`
   to `:590`, and add the `:712` `alpha *= backtrack_factor` anchor to the line-search non-law
   evidence (`:88`, `:108`). This theme uses the corrected on-disk numbers, so the theme and the
   operator entry will disagree on these two secondary anchors until the operator entry is
   re-anchored — the integrator should be aware the theme is the citecheck-verified-correct one.
2. **The `:673-676` lines are shared with dispatch-1 (`nleps_jacobian_action`).** Dispatch 1 cites
   `:673`/`:675`/`:676` as *downstream context* (the `w`-is-big-space-only confirmation — `w` enters
   the eigenvalue correction only through the big-space dot `⟨w, w0⟩`). This theme lowers those same
   lines as its **primary subject** (the projected Newton ratio + the big-space step RHS). No
   conflict — the two NEP-interior themes share the `:673-676` citation range with different roles
   (context there, subject here). The integrator should expect this expected overlap.
3. **Integration insert-anchor coordination with dispatch 1.** Both this theme and dispatch 1 append
   a row to `book/src/L1-L0/index.md` and an entry to `SUMMARY.md`. The integrator applies serially;
   dispatch 1 (`nleps-jacobian-action-mutation-rotation`) lands first. This report's edit blocks
   anchor to **dispatch-1's just-landed row/entry** and insert *after* it (sequencing the per-step
   chain residual → jacobian-action → eigenvalue-correction → solve), with a documented fallback
   anchor (the `nleps-deflated-solve-mutation-rotation` row / `apply-nonlinear-pencil` entry) if
   dispatch-1's row is somehow not yet present. The two anchors are distinct, so no edit collision.
4. **No L2>L1 / L1 algebraic-law changes proposed.** This theme reuses the `dot` Sub-pattern A
   conjugation convention, the `axpbypcz` `γ = 0` reduction, and the `scal` negation form — all firm
   and unchanged. The theme adds no new law; it composes existing firm BLAS-1 vocabulary. No L2
   combinator is touched (this atom's projected inner products are leaf-`dot` overlaps with the
   solve sibling's Gram/coordinate folds, a leaf-vocabulary overlap, not a unification — the
   over-unification guard, `book/src/L1/nleps_eigenvalue_correction.md:110`).
5. **NEP-interior L1>L0 cohort now complete.** With this theme (the per-step scalar
   eigenvalue-correction) and dispatch 1 (the per-step Jacobian action), the five deflated
   NEP-interior atoms all have firm L1>L0 lowering themes: `apply_nonlinear_pencil` (pencil apply),
   `nleps_deflated_residual` (residual), `nleps_deflated_solve` (solve), `nleps_jacobian_action`
   (Jacobian action), `nleps_eigenvalue_correction` (eigenvalue correction). The per-step
   quasi-Newton chain `residual → jacobian-action → eigenvalue-correction → deflated-solve →
   line-search` is fully lowered. The OQ
   `nleps-eigenvalue-correction-mutation-rotation-l1-l0-lowering-theme` is resolved by this report.
