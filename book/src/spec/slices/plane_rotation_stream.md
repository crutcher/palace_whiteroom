# plane_rotation_stream

> **Reduction status (cycle-012+):** the Givens-rotation primitives and the per-step procedure of this slice are firm in the concept-page family [`plane-rotation-stream`](../../concepts/plane-rotation-stream.md) (Shape) + [`givens`](../../concepts/givens.md) / [`givens_generate`](../../concepts/givens_generate.md) / [`givens_apply`](../../concepts/givens_apply.md) (the 2×2 primitives) + [`trsv`](../../concepts/trsv.md) (back-solve). The §L0 §Primitives, §L1 §Procedure/§Cross-target-reuse, and §L2 §Primitives/§Procedure are superseded by those firm pages. RETAINED here as unique material: §L0 §"Call sites" (the GMRES `iterative.cpp:634-643` / FGMRES `:813-822` byte-identical-site finding), §L0 §"Negative result" (no fused `xLASR`), §L2 §"Stream operations as primitive sequences" (the boundary-slot read-after-write analysis that bridges to L3), and the **entire §L3** — which is the canonical detailed source for [`sequential-obstruction`](../../concepts/sequential-obstruction.md) §"Worked example: Givens-stream replay-prefix" (that firm worked example cites this slice's §L3 and excerpts the loop + the boundary-slot RAW + the representational-obstruction framing, but elides this slice's quadratic-vs-linear cost argument, the cross-target-no-batch-dim analysis, the local-triviality-at-extend, and the Householder-WY sibling-slice boundary).
>
> **This slice is now the canonical plane-rotation-stream dissection** (the `orthog.md` plane-rotation sub-slice was reduced to a stub pointing here, cycle-012 — realizing the long-recorded `orthog/plane_rotation.md` split). The firm Givens concept pages' "Used in" / "primary dissection" cross-references should be repointed from the `orthog` slice to this slice (pending `layer-intro-author` dispatch; OQ `plane-rotation-concept-page-canonical-pointer-repoint`).
>
> **Pending lift / verify:** the L0 citation line ranges here (`iterative.cpp:72-108` generate-real / `:226-242` apply) differ by one from the firm `concepts/givens.md` ranges (`:73-108` / `:227-241`); a `verify-citation-range` pass should reconcile (OQ `plane-rotation-givens-l0-citation-range-reconcile`).

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

> **Reduced (cycle-012):** the two 2×2-rotation primitives are firm at
> [`givens_generate`](../../concepts/givens_generate.md) (`GeneratePlaneRotation`, real `iterative.cpp:72-108` / complex `:110-222`)
> and [`givens_apply`](../../concepts/givens_apply.md) (`ApplyPlaneRotation`, real `:226-232` / complex `:234-242`).
> Both port LAPACK `xLARTG` / `xROT`; the invariant `cs² + |sn|² = 1`, the safe-range branch detail,
> and the scratch-`t` read-write-dependency-break are firm-side. (See the reduction-status note above re: the
> one-off line-range discrepancy with `concepts/givens.md`.)

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

### Procedure (per Arnoldi step `j`) and cross-target reuse

> **Reduced (cycle-012):** the per-step procedure (replay-prefix on the new
> column tail → generate from the bottom 2-tuple → apply-to-self → propagate
> to the RHS pair → read residual proxy `|s[j+1]|`) is firm at
> [`plane-rotation-stream`](../../concepts/plane-rotation-stream.md) §"Shape"
> (steps 1-5). The two abstract stream operations — **replay-prefix** and
> **extend** — are named there; the L2 binding is unfolded in §L2 below. See
> §"Invariant" below (hoisted from `orthog.md`) for the formal
> least-squares-residual relation.

### Invariant

After `step_plane_rotation_stream(state, j)` returns: the product `G(c_j, s_j) ⋯ G(c_0, s_0)` applied to the original `H̄[0..j+1, 0..j]` equals `R[0..j+1, 0..j]` (upper-triangular through column `j`, with `R[j+1, 0..j] = 0`), and the same product applied to the original `s_0 = (β, 0, …, 0)ᵀ` equals the current `s[0..j+1]`. Equivalently, for any `y ∈ ℂ^{j+1}`: `‖R[0..j, 0..j]·y − s[0..j]‖² + |s[j+1]|² = ‖H̄[0..j+1, 0..j]·y − βe₁‖²`, so minimizing the first term yields the GMRES iterate and the second term gives the residual norm. (Hoisted from the now-reduced `orthog.md` plane-rotation sub-slice, cycle-012.)

### Cross-target reuse

> **Reduced (cycle-012):** the cross-target reuse — one `(c_j, s_j)` applied
> to two distinct targets (`Hj` column triangularization + `s` residual-proxy
> propagation) without re-derivation, the structural reason `(c, s)` is stored
> as a stream rather than recomputed — is firm at [`givens`](../../concepts/givens.md)
> §"L2 usage shape" (cross-target-reuse paragraph).

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

### Primitives and procedure (L2)

> **Reduced (cycle-012):** the L2 primitive binding (`givens_gen` /
> `givens_apply` from the [`givens`](../../concepts/givens.md) family) and the
> 5-line per-step procedure are firm at `concepts/givens.md` §"L2 usage shape"
> + [`plane-rotation-stream`](../../concepts/plane-rotation-stream.md) §"Shape".
> The mutation-pattern legibility (pure `givens_apply` returning a 2-tuple,
> tuple-destructuring breaking the read-write dependency) is firm-side. The
> unique L2 material — the boundary-slot read-after-write analysis that is the
> input to the L3 obstruction — is retained in §"Stream operations as primitive
> sequences" below.

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
`k+1` reads `(Hj[k+1], Hj[k+2])` and writes both. The shared slot
`Hj[k+1]` carries a **read-after-write** dependency across adjacent
iterations: the value of `Hj[k+1]` consumed at iteration `k+1` is the
value **written** by iteration `k` (not the pre-loop value). The
rotation chain cannot be re-expressed as a single elementwise or
gather/scatter tensor-field operation on `Hj` because each successive
two-element window overlaps its predecessor by one slot, and that
overlap is load-bearing — replacing the written value with the
pre-loop value would compute a different (incorrect) result.

This is the canonical [sequential-obstruction](../../concepts/sequential-obstruction.md)
class-(a) shape: the dependency graph of the loop iterations is a
chain (each iteration depends on its immediate predecessor through
the shared boundary slot), and a chain of length `j` admits no
parallel re-expression as a tensor-field operation. The same shape
appears in [trsv](../../concepts/trsv.md) (triangular solve, where
each `x[i]` depends on `x[0..i-1]`) and in Gauss-Seidel sweeps; in all
three the algebraic structure (Givens-product / triangular-inverse /
relaxation sweep) forces the chain.

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
The boundary between *this slice* and *a hypothetical Householder-QR
slice* is the choice of factored representation: Givens-stream stores
`j` scalar pairs and replays a chain; Householder-WY stores a block
reflector `(V, T)` and applies it via two `gemv`/`gemm` calls — the
latter HAS an L3 global form, but at a different L0 (and different
flop profile per step).

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
