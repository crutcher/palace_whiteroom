# orthogonalize

The L2 first-class composition naming the Gram-Schmidt **orthogonalize-against-basis**
pattern: it lifts the firm L1 leaf [`orthogonalize`](../L1/orthogonalize.md) into the named
L2 surface where the `gs_orthog ∈ {MGS, CGS, CGS2}` variant axis is no longer an opaque
parameter but the **visible per-variant batching and sequencing** of the constituent
`dot` / `axpy` primitives. The fusion-rotation form: Palace exposes one runtime-dispatched
entry point (`OrthogonalizeIteration` / the ROM `OrthogonalizeColumn` wrapper) that switches
on the orthogonalization enum into three distinct loop-structures; L2 unfolds that single
dispatch into the canonical composition `(project against V) then (subtract)`, with the
variant's load-bearing difference disclosed as the **collective-shape residual axis** (`m`
reductions of size 1 vs 1 of size `m` vs 2 of size `m`). This is the level-(b)-absorbed
`op.orthog` surface that [`krylov-step`](./krylov-step.md) folds, and the composition
GMRES / FGMRES / Arnoldi / eigenmode-ROM basis-extension all consume.
