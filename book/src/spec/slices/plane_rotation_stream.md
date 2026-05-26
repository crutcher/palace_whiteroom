# plane_rotation_stream

## Context

GMRES and FGMRES maintain an upper-Hessenberg matrix `H̄` produced by Arnoldi
and triangularize it incrementally via a stream of [Givens rotations](../../concepts/givens.md).
Each Arnoldi step appends one column to `H̄`; the slice's job is to (i) replay
prior rotations on the new column, (ii) generate a fresh rotation that zeroes
the new sub-diagonal entry, and (iii) apply that fresh rotation to the rotated
right-hand side `s` so that the trailing entry `|s[j+1]|` is the next residual
proxy.

This slice scopes the minimal Givens-on-2-element-window interface used by the
[GMRES](./gmres.md) and [FGMRES](./gmres.md#fgmres) inner loops. The compositional
use (the per-step rotation block embedded inside the Arnoldi/least-squares
recurrence) lives in those slices; this slice fixes the primitives and the
stream-shape they compose into.

## Background

Givens rotations are the classical 2×2 unitary transforms
`[[c, s], [-s̄, c]]` (real: `s̄ = s`; complex: `c ∈ ℝ`, `s ∈ ℂ`, with
`c² + |s|² = 1`) that zero one entry of a 2-vector. Stacked into a stream
they are the standard incremental QR mechanism inside GMRES — see
Saad 2003 ch. 6.5 and Golub & Van Loan 2013 §5.1. Palace's two primitives
are straight ports of LAPACK's `xLARTG` (rotation-scalar producer) and
`xROT` style application; the real specialization mirrors `s/dlartg`,
the complex specialization mirrors `c/zlartg`. Deviations from textbook
are numerical-safety branches (overflow/underflow scaling), not
algebraic.

## L0

### Primitives

- **`GeneratePlaneRotation<T, ScalarType>(dx, dy, cs, sn)`** —
  [palace/linalg/iterative.cpp:72-108](../../../../reference/palace/linalg/iterative.cpp#L72-L108) (real specialization);
  [palace/linalg/iterative.cpp:110-222](../../../../reference/palace/linalg/iterative.cpp#L110-L222) (complex specialization).
  Read-only on `dx, dy` (by value); write-only on `cs, sn` (output reference
  parameters). Real form: `cs: T, sn: T`. Complex form: `cs: T, sn: complex<T>`.
  Both specializations port LAPACK `xLARTG` (real: 36 lines branching on
  `dy == 0` / `dx == 0` / safe-range / overflow-scaling; complex: 112 lines
  with additional `dy` purely-real / purely-imaginary sub-branches and an
  inner re-scaling factor `w`). The algebraic invariant across all branches
  is `cs² + |sn|² = 1` and applying the resulting rotation to `(dx, dy)`
  yields `(r, 0)` with `r = sign(dx) · √(|dx|² + |dy|²)`.

- **`ApplyPlaneRotation<T, ScalarType>(dx, dy, cs, sn)`** —
  [palace/linalg/iterative.cpp:226-232](../../../../reference/palace/linalg/iterative.cpp#L226-L232) (real);
  [palace/linalg/iterative.cpp:234-242](../../../../reference/palace/linalg/iterative.cpp#L234-L242) (complex).
  In-place on `(dx, dy)`; read-only on `(cs, sn)`. Real form computes
  `t = cs·dx + sn·dy; dy = -sn·dx + cs·dy; dx = t`. Complex form computes
  `t = cs·dx + sn·dy; dy = -conj(sn)·dx + cs·dy; dx = t`. The scratch
  `t` is the standard trick to break the read-write dependency between
  the two output entries.

### Call sites

- **GMRES inner loop** — [palace/linalg/iterative.cpp:634-643](../../../../reference/palace/linalg/iterative.cpp#L634-L643).
  At Arnoldi step `j`: replay `cs[0..j-1], sn[0..j-1]` on the new column
  tail `H[:,j][k..k+1]` for `k = 0..j-1`; then `GeneratePlaneRotation` on
  `(H[j,j], H[j+1,j])` producing `(cs[j], sn[j])`; then `ApplyPlaneRotation`
  to zero `H[j+1,j]`; then the SAME fresh rotation is applied to `(s[j], s[j+1])`.

- **FGMRES inner loop** — [palace/linalg/iterative.cpp:813-822](../../../../reference/palace/linalg/iterative.cpp#L813-L822).
  Byte-identical primitive sequence to the GMRES site. The fixed-vs-flexible-
  preconditioner axis does NOT enter the rotation stream.

### Storage

The `(cs, sn)` pairs are stored in two `std::vector`-like buffers indexed by
the Arnoldi step index. The stream is append-only: step `j` writes to slot
`j` and reads slots `[0, j)` during the replay phase. `cs` is always real
(type `T`); `sn` shares `ScalarType` with the Hessenberg entries.

### Negative result

No fused "apply stream of rotations" primitive exists. There is no LAPACK
`xLASR`-style block call wrapped or invoked. Each `ApplyPlaneRotation` is
invoked individually inside an explicit `for k = 0..j-1` loop. The minimal
interface is exactly the two primitives Generate + Apply on 2-element
windows; everything stream-shaped is constructed at the call site.

## L1

### State schema

The slice's state, as seen from a single GMRES/FGMRES Arnoldi step `j`:

```
{
  cs: T[]              // accumulated cosine scalars, length j+1 after step j
  sn: ScalarType[]     // accumulated sine scalars, length j+1 after step j
  Hj: ScalarType[]     // new Hessenberg column, length j+2, mutated
  s:  ScalarType[]     // rotated RHS, length m+1, slots [0..j+1] live
}
```

The two scalar buffers `(cs, sn)` are the *stream*; the column `Hj` and the
RHS `s` are the *targets* of the stream. `Hj` and `s` carry their own roles
in the GMRES least-squares recurrence and are owned by that slice; this
slice borrows two-element windows of each.

### Primitives (named at L1)

- **`generate(dx, dy) → (c, s)`** — pure function on a 2-tuple of scalars
  producing a rotation that zeroes the second entry. Numerically-safe
  Givens generation; the LAPACK branching is absorbed as an implementation
  detail of the primitive (rotation cost and overflow safety live below L2).

- **`apply(window, c, s)`** — in-place rotation of a 2-element window of
  some host array. The window is named by `(array, k)` denoting
  `(array[k], array[k+1])`.

Both primitives are typed by the scalar field of their inputs; the
real/complex split is static dispatch resolved at compile time, not a
runtime variant.

### Procedure (per Arnoldi step `j`)

```
step_plane_rotation_stream(state, j):
    # 1. Replay accumulated stream on the new column tail.
    for k in 0..j-1:
        apply(Hj, k, cs[k], sn[k])
    # 2. Extend the stream by generating from the bottom 2-tuple.
    (cs[j], sn[j]) = generate(Hj[j], Hj[j+1])
    # 3. Apply the fresh rotation to triangularize the column.
    apply(Hj, j, cs[j], sn[j])
    # 4. Apply the SAME fresh rotation to the rotated-RHS pair.
    apply(s, j, cs[j], sn[j])
    # The residual proxy is now |s[j+1]|; returned by the host slice.
```

The stream interface at L1 is therefore an ordered append-only sequence of
`(c, s)` pairs together with two operations: **replay-prefix** on a
2-element window (a `for k < j` loop of `apply`s) and **extend** (one
`generate` plus one `apply` on the producing window). No third operation
exists at L1.

### Cross-target reuse

A single rotation index `k` is applied to two distinct targets — `Hj` and
`s` — without re-deriving the rotation scalars. This is the structural
reason `cs` and `sn` are stored as a stream rather than recomputed: the
GMRES algorithm uses each pair twice (once on its producing column to
zero a sub-diagonal entry, once on the RHS to propagate the
triangularization to the residual proxy).

### Variant axes

- **Real vs. complex scalar field**: resolved by template instantiation
  at compile time; `cs` real in both cases, `sn` shares `ScalarType`
  with the host column. No L1-level branching.
- **Fixed vs. flexible preconditioner (GMRES vs. FGMRES)**: does NOT enter
  the rotation stream; both call sites are byte-identical.

The variant axes are absorbed parametrically at L1 — see
[variant-absorption](../../concepts/variant-absorption.md). The L1
procedure mentions no variant parameter; the primitives are
type-parametrized but the procedure shape is invariant.

### Open questions

- No targeted unit test for `GeneratePlaneRotation` / `ApplyPlaneRotation`;
  coverage is integration-only via GMRES KSPType in `test-romoperator.cpp`.
  Logged in `scaffolding/test-linkages.md` (pending).
- The complex specialization's safe-range branching (112 vs. 36 lines) is
  absorbed at L1 as numerically-safe Givens generation; whether L2 should
  unfold the branching as separate primitives or keep the single
  `generate` primitive is deferred to the L2 cycle.
