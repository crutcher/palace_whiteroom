---
kind: feature-surface
feature: krylov-iteration
level: L1
feature_root: seed
rank: rough-in
edges:
  depends-on:
    - target: L1/orthogonalize
      kind: composes                  # the pure orthogonalize leaf the iteration's auxiliary stage applies (firm); the L1 image of the L3 orthogonalize view
    - target: L1/apply_linop
      kind: composes                  # the whole-tensor operator-apply A·v per step (firm)
    - target: L1/axpy
      kind: composes                  # the iterate update x += α p / r -= α z (firm)
    - target: L1/axpby
      kind: composes                  # the direction update p ← z + (β/β_prev) p (firm)
    - target: L1/dot
      kind: composes                  # the recurrence inner products (Ap,p) / (Br,r) (firm)
    - target: L1/nrm2
      kind: composes                  # the residual / Hessenberg-subdiagonal norm (firm)
    - target: L1/scal
      kind: composes                  # the basis-column normalization v ← w/β (firm)
    - target: palace/linalg/iterative.cpp:421-464
      kind: cites-evidence            # CgSolver::Mult pure-function-rendered per-step body + outer fold
    - target: palace/linalg/iterative.cpp:563-705
      kind: cites-evidence            # GmresSolver::Mult restart + inner Arnoldi/orthogonalize
  reference:
    - feature/krylov-iteration.L4
    - L3/krylov_step
    - L3/fold_solve
    - L3/orthogonalize
    - concepts/sequential-obstruction
---

# Krylov-iteration spine — L1 composition-root

The **Krylov iteration spine** presented at L1 as the pure-function rendering of the per-step
basis-extension body and the outer fold — the mutation-rotated form of `CgSolver::Mult` /
`GmresSolver::Mult` (`palace/linalg/iterative.cpp:361-464`, `:544-705`), where the in-place
vector mutations (`x.Add(alpha, p)`, `r.Add(-alpha, z)`, `w.Add(-H[j], V[j])`) are re-expressed
as pure tensor-in / tensor-out functions threaded through the iteration. This is the
infrastructure / shared-substrate column at L1; it composes the firm L1 BLAS-1 + orthogonalize
vocabulary into the per-step iterate update and links DOWN to each piece. The L4 surface
([`krylov-iteration.L4`](./krylov-iteration.L4.md)) carries the full iteration-rotation
composition narrative (the three L3 iteration-views it composes, the RE2/RE8 discharge); this L1
surface is the pure-function shape the L4 combinator composition lowers onto.

## The pure per-step body

The per-step Krylov body is a **pure function** over flat dof-vectors (`Vector` is rank-1, so
the L1 shape group is the flat `Tensor[N]` per the named-shape-group convention; KEEP `Tensor[N]`
at L1). For CG (`iterative.cpp:434-463`), one step is:

    -- per-step CG body (pure form; the in-place x.Add / r.Add re-expressed as pure axpy):
    cg_step :: (op, K) -> K'
    cg_step op K =
      let p'    = if K.first then K.z else axpby K.z (K.beta / K.beta_prev) K.p  -- direction update (L1/axpby)
          z'    = apply_linop op.A p'                                             -- A·p           (L1/apply_linop)
          denom = dot z' p'                                                       -- (Ap, p)        (L1/dot)
          alpha = K.beta / denom
          x'    = axpy alpha p' K.x                                              -- x += α p       (L1/axpy)
          r'    = axpy (negate alpha) z' K.r                                     -- r -= α z       (L1/axpy)
          z''   = apply_B op.B r'                                                -- preconditioner apply
          beta' = dot z'' r'                                                     -- (Br, r)        (L1/dot)
      in  K { x = x', r = r', p = p', z = z'', beta = beta', beta_prev = K.beta }

For GMRES the per-step body additionally runs the [`orthogonalize`](../L1/orthogonalize.md) leaf
against the stored basis prefix (`iterative.cpp:615-632`) and normalizes via
[`nrm2`](../L1/nrm2.md) + [`scal`](../L1/scal.md). The body **lifts** — every primitive is a pure
whole-vector L1 op; the sequentiality is in the *outer fold over the body* (the carry-threading),
not the body itself. This is the L1 pure-function image of the firm [`krylov_step`](../L3/krylov_step.md)
iteration-view (the L3>L2>L1 body identity-in-form chain).

## The outer fold

The outer fold is a tail recursion threading the iterate-bundle carry `K` over the iteration —
the L1 image of the L3 [`fold_solve`](../L3/fold_solve.md) outer-driver. Each step's input `K` is
the prior step's output `K'`: the read-after-write that is the carry-threading
[`sequential-obstruction`](../concepts/sequential-obstruction.md). L0: the CG outer loop
`for (; it < max_it && !converged; it++)` (`iterative.cpp:427`); the GMRES restart loop
(`:563`) folding the inner Arnoldi loop (`:615`).

## Constituent down-links

| Stage | Constituent | Status | L0 site |
|---|---|---|---|
| direction / iterate update | [`axpy`](../L1/axpy.md) / [`axpby`](../L1/axpby.md) | firm | `iterative.cpp:440,448,449` |
| operator apply | [`apply_linop`](../L1/apply_linop.md) | firm | `iterative.cpp:443` (`A->Mult(p, z)`) |
| recurrence inner products | [`dot`](../L1/dot.md) | firm | `iterative.cpp:444,461` (`linalg::Dot`) |
| residual / subdiagonal norm | [`nrm2`](../L1/nrm2.md) | firm | `iterative.cpp:462` / GMRES `:630` |
| basis-column normalize | [`scal`](../L1/scal.md) | firm | GMRES `:631` |
| auxiliary orthogonalize | [`orthogonalize`](../L1/orthogonalize.md) | firm | `iterative.cpp:629` (`OrthogonalizeIteration`) |

## Status

`rough-in` — the L1 pure-function surface of the Krylov iteration spine. The L1 constituents are
all firm BLAS-1 + orthogonalize leaves, but the column inherits the L4 surface's `rough-in` rank:
the *iteration-rotation* claim it composes (the [`krylov-iteration.L4`](./krylov-iteration.L4.md)
view) rests on the L3 iteration-views, two of which are `partial-obstruction`. The L1 per-step
bodies lift cleanly; the obstruction is in the outer fold over the body (carry-threading), recorded
via the L3 `fold_solve` reference. **Promotion route:** `rough-in → firm` if the two
partial-obstruction L3 iteration-views promote (their obstructions are intrinsic carry-threading,
so this is the honest standing state). This chapter carries the *compositional* claim (the iteration
spine's per-step body = this pure composition of these firm L1 leaves), not the constituents' per-op
algebra. Evidence: `iterative.cpp:421-464` (CG) + `:563-705` (GMRES) mutation-rotated to the pure
per-step body + outer fold.
