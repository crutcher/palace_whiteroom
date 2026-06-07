---
kind: feature-surface
feature: geometric-multigrid-preconditioner
level: L1
feature_root: seed
rank: rough-in
edges:
  depends-on:
    - target: L1/fe_space_hierarchy
      kind: composes                  # the prolongation level-stack the V-cycle restricts/prolongs over (GROUNDS RE9)
    - target: L1/multigrid-relaxation-smoother
      kind: composes                  # D3 kernel-impl: the per-level relaxation smoother (forward-ref)
    - target: L1/reciprocal
      kind: composes                  # diagonal-preconditioner extract dinv.Reciprocal() (GROUNDS RE7)
    - target: L1/normalize
      kind: composes                  # the diagonal-precond scaling chain (GROUNDS RE5)
    - target: palace/linalg/gmg.cpp:126-205
      kind: cites-evidence            # the pure V-cycle recursion (Mult + VCycle) read as nested pure functions
  reference:
    - feature/geometric-multigrid-preconditioner.L4
    - L3/chebyshev
    - L2/jacobi-smoother
---

# geometric-multigrid preconditioner — L1 composition-root

The **GMG preconditioner** presented at L1 as the pure-function rendering of the V-cycle —
the mutation-rotated form of `GeometricMultigridSolver::Mult` / `VCycle`
(`palace/linalg/gmg.cpp:126-205`), where the in-place vector mutations (`X.back() = x`,
`Y[l] += R[l]`, the `Mult2`/`MultTranspose2` residual-correction sweeps) are re-expressed as
pure tensor-in / tensor-out functions threaded through the level recursion. This is the
infrastructure / shared-substrate column at L1; it composes the firm L1 vocabulary into the
recursive preconditioner action and links DOWN to each piece. The L4 surface
([`geometric-multigrid-preconditioner.L4`](./geometric-multigrid-preconditioner.L4.md))
carries the full composition narrative; this L1 surface is the pure-function shape the L4
combinator composition lowers onto.

## The pure V-cycle

The V-cycle is a **level-recursive pure function** over flat dof-vectors (`Vector` is rank-1
at L1, so the shapes here are genuinely flat `Tensor[N]`):

    -- one V-cycle sweep at level l, pure (no in-place mutation)
    vcycle :: [LinOp[(S: ...), $S]]   -- A[l]  per-level operators (square)
           -> [Smoother]              -- B[l]  per-level smoothers
           -> [LinOp[(C: ...), (F: ...)]] -- P[l]  prolongations  (coarse → fine)
           -> Solver                  -- b0    coarse solve
           -> Int -> Tensor[N] -> Tensor[N]
    vcycle as bs ps b0 0 x = b0 x                                   -- coarse solve
    vcycle as bs ps b0 l x =
      let y   = presmooth (bs!l) x                                  -- Y ← B(X − A·0)   gmg.cpp:184
          r   = axpby 1.0 x (-1.0) (apply (as!l) y)                -- R ← X − A Y       gmg.cpp:187-188
          rc  = apply_transpose (ps!(l-1)) r                       -- Pᵀ R (restrict)  gmg.cpp:191
          ec  = vcycle as bs ps b0 (l-1) rc                        -- recurse coarser   gmg.cpp:196
          y'  = y `vadd` apply (ps!(l-1)) ec                       -- Y += P E (prolong) gmg.cpp:199-200
      in  postsmooth (bs!l) x y'                                   -- MultTranspose2    gmg.cpp:204

    -- the outer driver: pc_it Richardson sweeps over the finest level
    geometric_multigrid as bs ps b0 pc_it x =
      iterate pc_it (vcycle as bs ps b0 (length as - 1)) x         -- gmg.cpp:135-141

Three composed pieces, each a firm L1 link:

1. **Prolongation level-stack** — [`fe_space_hierarchy`](../L1/fe_space_hierarchy.md)
   (firm). The per-level prolongations `P[l]` are the firm hierarchy's
   `GetProlongationOperators()`; the V-cycle's `restrict = apply_transpose (P[l])` and
   `prolong = apply (P[l])` are the only inter-level transfers. **GROUNDS RE9.** L0:
   `gmg.cpp:191` (restrict), `:199` (prolong).
2. **Per-level smoother** — [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md)
   (D3 kernel-impl, forward-ref) / the Chebyshev/Jacobi polynomial smoothers
   ([`L3/chebyshev`](../L3/chebyshev.md) / [`L2/jacobi-smoother`](../L2/jacobi-smoother.md),
   cross-linked as references). The smoother's diagonal-preconditioner setup
   (`dinv = reciprocal(assemble_diagonal A)`) composes the firm
   [`reciprocal`](../L1/reciprocal.md)/[`normalize`](../L1/normalize.md) chains. **GROUNDS
   RE1/RE5/RE7.** L0: `chebyshev.cpp:177-178`.
3. **Coarse solve** — the level-0 base case `b0` (the supplied coarse solver, opaque at this
   surface). L0: `gmg.cpp:178-183` (the `l==0` base case, `B[l]->Mult(X[l], Y[l])` at `:181`).

The residual / update steps (`axpby`, `vadd`) are the firm whole-vector primitives; the body
is whole-tensor by signature shape at each step (the L1 mutation-rotation of the in-place
`R[l]`/`Y[l]` scratch vectors), but the **level recursion and the `pc_it` Richardson sweep
are sequential obstructions** inherited from [`L3/chebyshev`](../L3/chebyshev.md) — see the
L4 surface's §"Why this is rough-in".

## Status

`rough-in` — the L1 pure-function surface of the infrastructure / shared-substrate GMG
preconditioner column. `feature_root: seed` preserved. Held at rough-in by the same
well-foundedness gate as the [L4 surface](./geometric-multigrid-preconditioner.L4.md): the
smoother leg rests on the partial-obstruction [`L3/chebyshev`](../L3/chebyshev.md) + D3's
forward-referenced [`multigrid-relaxation-smoother`](../L1/multigrid-relaxation-smoother.md).
The V-cycle body is the mutation-rotated pure rendering of `gmg.cpp:126-205`; the level
recursion + Richardson sweep are the documented sequential obstructions. Evidence:
`gmg.cpp:126-205`.
