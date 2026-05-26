# givens

Base primitive family for plane (Givens) rotations: a 2×2 unitary applied to a coordinate pair. Used in GMRES to triangularise the Hessenberg matrix one column at a time.

## Generate

`(cs, sn) ← givens_generate(dx, dy)`. Computes the rotation that, applied to `(dx, dy)`, produces `(r, 0)` with `r = √(|dx|² + |dy|²)`. Production implementations are LAPACK-style scaled — they handle the case `|dx|, |dy|` near overflow or underflow without intermediate `dx² + dy²` overflowing.

- Real version: `cs = dx/r, sn = dy/r` with scaling.
- Complex version: more branches; both arguments may be complex; the algorithm preserves unitarity exactly.

## Apply

`givens_apply2(dx, dy, cs, sn)` — in-place 2-vector update:

```
(dx', dy') = (cs · dx + sn · dy,  -s̄n · dx + cs · dy)
```

Where `s̄n` is `conj(sn)` in the complex case. Applied to either column entries of an upper-Hessenberg matrix or to the RHS pair of the LS problem.

## Contract

- Both operations are element-local; no reduction.
- The pair `(cs, sn)` is stored across iterations (in GMRES, the registers `K.cs`, `K.sn`) and replayed on subsequent columns. Replay order is load-bearing: a previously-stored rotation `k` must be applied to a new column before any newly-generated rotation `j > k` touches it.

## Role in higher-layer rotations

In GMRES (`gmres.md`), the inner step's `ls_update_column` is a sequence of `givens_apply2` calls (replaying stored rotations on a new column) followed by one `givens_generate` (producing the new rotation) and two `givens_apply2` calls (annihilating `h[j+1]` and updating the RHS pair). This converts the Hessenberg least-squares problem into an upper-triangular one, enabling `back_solve` via `trsv`.

## Palace mapping

- `GeneratePlaneRotation` — `palace/linalg/iterative.cpp:73–108`.
- `ApplyPlaneRotation` — `palace/linalg/iterative.cpp:227–241`.

## L2 usage shape

In primitive composition (L2), the two `givens` primitives compose
as an **incremental QR stream** — see
[plane_rotation_stream slice](../spec/slices/plane_rotation_stream.md)
for the canonical use site. The stream pattern is:

- `gen` produces one new rotation scalar pair `(c[j], s[j])` per
  outer step.
- `apply` is called once per (step, target) pair: at step `j` it is
  invoked `j+2` times — `j` times to replay prior rotations on the
  new column tail, once to triangularize the new column, once to
  propagate the rotation to the rotated RHS.

The `(c, s)` scalar buffers are append-only and indexed by step.
The two L2 primitives compose at the call site as the explicit
loop `for k in 0..j-1: (col[k], col[k+1]) = apply(col[k], col[k+1], c[k], s[k])`;
no fused stream primitive is invoked.

Cross-target reuse is the structural reason `(c, s)` is stored
rather than recomputed: each pair is applied to at least two
independent targets (the producing column and the rotated RHS in
GMRES) without re-deriving the scalars.
