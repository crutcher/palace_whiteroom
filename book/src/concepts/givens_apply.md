# `givens_apply`

Apply a stored plane rotation $(c, s)$ to a 2-vector $(dx, dy)$ in place.

## Signature

```
givens_apply(c: real(T), s: T, dx: T, dy: T) -> (dx', dy')
```

computing

$$\begin{pmatrix} dx' \\ dy' \end{pmatrix} = G(c, s) \cdot \begin{pmatrix} dx \\ dy \end{pmatrix} = \begin{pmatrix} c \cdot dx + s \cdot dy \\ -\bar{s} \cdot dx + c \cdot dy \end{pmatrix}.$$

The operation is in-place on the two scalar operands.

## Background

The "apply" half of the Givens rotation pair. Used both to apply a freshly-generated rotation to its generating 2-vector (zeroing the second entry) and to apply previously-stored rotations to subsequent columns and to the running RHS during incremental least-squares (Saad 2003, §6.5.3).

## Palace citation

[palace/linalg/gmres.cpp:ApplyPlaneRotation](../../reference/palace/linalg/gmres.cpp).

## Used in

- [`orthog` slice](../spec/slices/orthog.md) — applied repeatedly per Arnoldi step: $k$ times to the new Hessenberg column (replay of stored rotations), once to the same column (new rotation), once to the $\bar{g}$ vector pair.
