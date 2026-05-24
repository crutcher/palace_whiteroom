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
