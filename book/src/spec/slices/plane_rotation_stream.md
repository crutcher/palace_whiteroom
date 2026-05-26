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

## L2 — primitive composition

### State schema (unchanged from L1)

```
{
  cs: T[]              // accumulated cosine scalars, length j+1
  sn: ScalarType[]     // accumulated sine scalars, length j+1
  Hj: ScalarType[]     // new Hessenberg column, length j+2
  s:  ScalarType[]     // rotated RHS, length m+1
}
```

The schema carries through unchanged from L1 — see [rotation](../../concepts/rotation.md)
*Carry-through*. The L1→L2 rotation is a primitive-substitution edge:
L1's two abstract operations (`generate`, `apply`) bind to named L2
primitives drawn from the [givens](../../concepts/givens.md) family;
the stream's append-only structure becomes explicit as indexed buffer
access.

### Primitives

- **`givens_gen(dx, dy) → (c, s)`** — see
  [givens](../../concepts/givens.md) primitive `gen`. LAPACK
  `xLARTG`-equivalent: numerically-safe construction of a 2×2 unitary
  zeroing the second input. Pure function on two scalars; the
  overflow-scaling and zero-handling branches are absorbed inside the
  primitive (they are L2-internal, not L1-visible).

- **`givens_apply(x, y, c, s) → (x', y')`** — see
  [givens](../../concepts/givens.md) primitive `apply`. Pure 2×2
  unitary application. Real form: `x' = c·x + s·y; y' = -s·x + c·y`.
  Complex form: `x' = c·x + s·y; y' = -conj(s)·x + c·y`. The L1 `apply
  on window` reduces at L2 to `givens_apply` on the two scalars
  read from / written to indexed buffer slots.

### Procedure (per Arnoldi step `j`)

```
step_plane_rotation_stream(state, j):
    # 1. Replay accumulated stream on the new column tail.
    for k in 0..j-1:
        (Hj[k], Hj[k+1]) = givens_apply(Hj[k], Hj[k+1], cs[k], sn[k])

    # 2. Extend the stream: generate from the bottom 2-tuple.
    (cs[j], sn[j]) = givens_gen(Hj[j], Hj[j+1])

    # 3. Apply the fresh rotation to triangularize the column.
    (Hj[j], Hj[j+1]) = givens_apply(Hj[j], Hj[j+1], cs[j], sn[j])

    # 4. Apply the SAME fresh rotation to the rotated-RHS pair.
    (s[j], s[j+1]) = givens_apply(s[j], s[j+1], cs[j], sn[j])

    # Residual proxy: |s[j+1]|.
```

The procedure shape is the L1 shape with each abstract operation
bound to its named L2 primitive. The buffer indexing made implicit
by L1's `window` notation becomes explicit at L2 — `(Hj[k], Hj[k+1])`
is the 2-tuple read/written by the rotation. The mutation pattern
is legible at L2: `givens_apply` is a pure function returning a
2-tuple, and assignment back into the indexed slots is the in-place
update (per the meta-review #8 mutation-pseudocode discipline,
explicit tuple destructuring makes the read-write dependency
break visible without a scratch variable — the right-hand side
reads both inputs before either assignment commits).

### Stream operations as primitive sequences

L1 named two stream operations: **replay-prefix** and **extend**.
At L2 these unfold to fixed primitive sequences:

- **replay-prefix** on target window `(target, k_lo, k_hi)`:
  `for k in k_lo..k_hi: (target[k], target[k+1]) = givens_apply(target[k], target[k+1], cs[k], sn[k])`.
  At step `j` for column `Hj`: `k_lo = 0, k_hi = j-1`.

- **extend** at index `j` on producing window `(Hj, j)`:
  `(cs[j], sn[j]) = givens_gen(Hj[j], Hj[j+1])` followed by
  `(Hj[j], Hj[j+1]) = givens_apply(Hj[j], Hj[j+1], cs[j], sn[j])`.

The replay-prefix loop is genuinely sequential along `k` only when
the target is `Hj` (each `apply` depends on the previous's output
at position `k+1` becoming position `k`'s input on the next
iteration via the shared slot — but in fact, after the kth apply,
slots `k` and `k+1` are final-written; the (k+1)th apply reads
slots `k+1` and `k+2`, so adjacent applies share slot `k+1`). The
sequential read-after-write on the shared boundary slot is the
L3-level obstruction signal — recorded for the L2→L3 edge.

### Cross-target rotation reuse

The L1 cross-target reuse property — one `(cs[j], sn[j])` applied to
two distinct targets `Hj` and `s` — is preserved at L2 as two
identical `givens_apply` calls reading the same `(cs[j], sn[j])`
slots. Both `Hj` (column triangularization) and `s` (residual-proxy
propagation) are independent targets at L2; the rotation scalars
are shared read-only state across the two `apply` sites.

### Variant axes

- **Real vs. complex scalar field**: `givens_gen` and `givens_apply`
  are template-instantiated on `ScalarType`; the L2 primitive sequence
  is invariant (see [variant-absorption](../../concepts/variant-absorption.md)
  level (c) — primitive-sequence invariance). Real and complex
  share the same 5-line L2 procedure with the same named primitive
  calls.
- **GMRES vs. FGMRES**: invariant — the rotation stream's L2 form
  is the same primitive sequence at both call sites. Confirmed by
  L0's byte-identical-call-site finding.

### Negative result (carried from L0, sharpened at L2)

No fused stream-apply primitive (LAPACK `xLASR`-equivalent) exists
at L2. The replay-prefix is unfolded as an explicit `for` loop over
individual `givens_apply` calls. A hypothetical `lasr(Hj, cs[0..j-1],
sn[0..j-1])` primitive would compress the replay-prefix to one call,
but Palace does not realize it — the L2 form must spell the loop.
The loop's sequential dependency structure is the input to the L2→L3
rotation.

## L3 — tensor-field lift

### State schema (unchanged from L2)

```
{
  cs: T[]              // accumulated cosine scalars, length j+1
  sn: ScalarType[]     // accumulated sine scalars, length j+1
  Hj: ScalarType[]     // new Hessenberg column, length j+2
  s:  ScalarType[]     // rotated RHS, length m+1
}
```

The schema carries through from L2 — see [rotation](../../concepts/rotation.md)
*Carry-through*. The L2→L3 rotation is **negative for the replay-prefix
loop** and **trivial for the per-step extend/apply triple**. This slice is
the canonical small-N obstruction case: the rotation stream is an
essentially-sequential incremental QR, not a global tensor-field
operation. See [sequential-obstruction](../../concepts/sequential-obstruction.md).

### Obstruction: replay-prefix is sequential along the stream

At L2 the replay-prefix on column `Hj` at step `j` is:

```
for k in 0..j-1:
    (Hj[k], Hj[k+1]) = givens_apply(Hj[k], Hj[k+1], cs[k], sn[k])
```

Iteration `k` reads `(Hj[k], Hj[k+1])` and writes both slots. Iteration
`k+1` reads `(Hj[k+1], Hj[k+2])`. The shared slot `Hj[k+1]` carries a
**read-after-write** dependency across adjacent iterations: the value of
`Hj[k+1]` consumed at step `k+1` is the value written by step `k`. The
rotation chain cannot be re-expressed as a single elementwise or
gather/scatter tensor-field operation on `Hj` because each successive
two-element window overlaps its predecessor by one slot.

The algebraic shape of the obstruction: the product
`G_{j-1} · G_{j-2} · … · G_0` is an upper-Hessenberg-triangulating
unitary, but the *factored* form is what gets stored and replayed.
Materializing the product as a dense `j × j` unitary `Q_{j-1}` and
applying it as `Hj ← Q_{j-1} · Hj` would be a tensor-field operation,
but at `O(j²)` storage and `O(j² · m)` flops per step versus the
factored stream's `O(j)` storage and `O(j)` flops per step — a
quadratic-vs-linear blowup that defeats the whole point of
incremental QR.

### Obstruction: cross-target reuse is per-step, not per-stream

The two `givens_apply` calls on `(Hj[j], Hj[j+1])` and `(s[j], s[j+1])`
at L2 step 4 use the SAME `(cs[j], sn[j])` pair but on **disjoint
targets**. This is not a tensor-field broadcast: each call is one 2×2
rotation on one 2-tuple. A `vmap`-style lift over a batch dimension
does not apply — there is no batch dimension; there are exactly two
call sites with hard-coded distinct targets.

### Local triviality at extend

The per-step **extend** triple (one `givens_gen` + one `givens_apply`
on `Hj` + one `givens_apply` on `s`) is a fixed three-primitive
sequence with no loop. At L3 it lifts unchanged: there is no iteration
structure to globalize, so the rotation is the identity. The negative
result applies specifically to the replay-prefix loop.

### Negative result (recorded)

The replay-prefix `for k in 0..j-1: givens_apply(target[k], target[k+1], cs[k], sn[k])`
has NO L3 tensor-field global form on `target = Hj`. The obstruction is
the read-after-write dependency on shared boundary slot `target[k+1]`
between adjacent iterations. This is a structural property of the
Givens-stream incremental-QR pattern, not a Palace-specific
implementation choice — any incremental-QR replay carries the same
shape.

The obstruction is class-(a) per [sequential-obstruction](../../concepts/sequential-obstruction.md):
*intrinsic algorithm sequentiality*. Removing it requires changing the
algorithm (e.g., switching to Householder-block QR with WY
representation, which is a different slice and a different stream
shape — recorded as a sibling slice candidate, not an L3 of this one).

### What DOES lift

Across independent target arrays the replay-prefix loops are
independent: replaying the same stream on `Hj` and on `s` could be
fused as a vector-of-targets broadcast, but Palace does not — the two
applications happen at different stream stages (replay-prefix touches
only `Hj`; cross-target reuse on `s` only ever happens at the SAME
step `j` index, never as a replay). So even this potential lift is
structurally absent from the algorithm and the L3 form remains the L2
form with the loop spelled.

### Variant axes

- **Real vs. complex scalar field**: invariant. The obstruction shape
  (read-after-write on the shared boundary slot) is independent of
  scalar type.
- **GMRES vs. FGMRES**: invariant — the rotation stream's L3 form is
  the same obstruction at both call sites.

### Push-back consideration

The slice's L1/L2 already names the stream as append-only and
spells the replay loop explicitly. No lower-layer restructuring would
yield an L3 global form — the obstruction is algebraic, not
representational. If a future cycle needs a tensor-field replay, it
should be a new sibling slice for Householder-block QR, not a back-
correction of this one.
