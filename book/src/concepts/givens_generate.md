---
edges:
  reference:
    - L1/ls-update-column
---

# `givens_generate`

Generate a plane (Givens) rotation $(c, s)$ that zeros the second component of a 2-vector $(dx, dy)$.

## Signature

```
givens_generate(dx: T, dy: T) -> (c: real(T), s: T, r: real(T))
```

where `T` is real or complex. The returned $(c, s, r)$ satisfy

$$G(c, s) \cdot \begin{pmatrix} dx \\ dy \end{pmatrix} = \begin{pmatrix} r \\ 0 \end{pmatrix}, \quad r = \sqrt{|dx|^2 + |dy|^2}, \quad c \in \mathbb{R}_{\geq 0}.$$

For real `T`: $c = dx/r$, $s = dy/r$. For complex `T`: $c$ is real, $s = \overline{dx} \cdot dy / (|dx| \cdot r)$ (the real-cosine convention).

## Background

Classical Givens rotation (Golub & Van Loan 2013, §5.1.8). The naive formula $r = \sqrt{dx^2 + dy^2}$ overflows when either component is near the square root of the floating-point overflow threshold, and underflows symmetrically. Palace uses the **scaled-Givens** variant (Bindel, Demmel, Kahan, Marques 2002, *On Computing Givens Rotations Reliably and Efficiently*), which scales by $\max(|dx|, |dy|)$ before squaring. The scaled form is the de-facto LAPACK-style implementation.

## Palace citation

[palace/linalg/gmres.cpp:GeneratePlaneRotation](../../reference/palace/linalg/gmres.cpp) — real and complex specializations.

## Used in

- [`ls-update-column`](../L1/ls-update-column.md) — once per Arnoldi step, to generate the rotation that zeros the sub-diagonal of the new Hessenberg column.
