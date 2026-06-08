# ls-update-column-mutation-rotation

The mutation rotation for the GMRES / FGMRES per-column running-QR update.
Lowers the pure L1 form `{h_out, cs_j, sn_j, s_j, s_jp1, beta} =
ls_update_column(variant, cs, sn, s, j, h_new)`
([`L1/ls_update_column`](../L1/ls_update_column.md), firm) into the
in-place four-`*PlaneRotation`-call sequence at
`palace/linalg/iterative.cpp:634-640` (GMRES) and its **byte-identical** FGMRES
twin at `:813-819`: the rewrite consists of (1) the **strict-order replay loop**
`for (int k = 0; k < j; k++) ApplyPlaneRotation(Hj[k], Hj[k+1], cs[k], sn[k])`
applying the stored rotations `0..j-1` in-place to the new Hessenberg column,
(2) the **generate-into-registers call**
`GeneratePlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j])` producing the new
rotation and writing it into the register slots `cs[j], sn[j]`, (3) the
**column-apply sub-diagonal annihilation**
`ApplyPlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j])` overwriting the pair
`(Hj[j], Hj[j+1])` with `(triangularised, 0)`, and (4) the **RHS-apply
residual-into-tail** `ApplyPlaneRotation(s[j], s[j+1], cs[j], sn[j])`
concentrating the least-squares residual into `s[j+1]`. The four calls
overwrite four pre-allocated registers in place; the L1 fresh value bundle has
**no buffer of its own** at L0 — every result slot is a slot of an input
register. It is the column-streaming sibling-in-cohort of
[`back-solve-mutation-rotation`](./back-solve-mutation-rotation.md) (the
restart-cycle terminal consumer): both lower a small-dense coordinate-space
operator whose destination *is* the register the L1 form names as input; this
theme is the per-column-incremental producer, the sibling is the terminal
consumer. It proposes **no new L1 vocabulary**; the L1 leaf
[`ls_update_column`](../L1/ls_update_column.md) is firm.

## Slug

`ls-update-column-mutation-rotation`

## L1 form (LHS)

The pure-functional per-column running-QR update (firm; see
[`L1/ls_update_column`](../L1/ls_update_column.md)) consumes read-only
rotation registers `(cs, sn)`, a read-only RHS register `s`, the column index
`j`, and the read-only newly-arrived Hessenberg column `h_new`, producing a
fresh six-tuple value bundle; nothing is mutated and there is no destination
buffer in the signature. There is one LHS shape (`ls_update_column` has no
surface-form variants — the per-column-update sequence
`replay ▷ generate ▷ apply ▷ apply_rhs` is fixed and unique; element-type and
column-index axes are absorbed per `classify-variant-axis`):

    {h_out, cs_j, sn_j, s_j, s_jp1, beta}
      = ls_update_column(variant, cs, sn, s, j, h_new)
        -- variant : GivensKind = real | complex   (absorbed at instantiation)
        -- cs : Tensor[m] of RealScalar            (stored cosines, slots 0..j-1 populated)
        -- sn : Tensor[m] of Scalar                (stored sines,   slots 0..j-1 populated)
        -- s  : Tensor[m+1] of Scalar              (rotated RHS, slots 0..j populated; s[j+1] = 0 on entry)
        -- j  : Int, 0 <= j < m
        -- h_new : Tensor[j+2] of Scalar           (Hessenberg column; h_new[j+1] = nrm2(residual))
        -- result h_out : Tensor[j+2]              (h_out[0..j] = R-factor column j; h_out[j+1] = 0)
        -- result cs_j  : RealScalar               (new rotation cosine; always real)
        -- result sn_j  : Scalar                   (new rotation sine)
        -- result s_j, s_jp1 : Scalar              (rotated RHS pair)
        -- result beta  : RealScalar = |s_jp1|     (LS residual byproduct, load-bearing)

The defining identities (the L1 leaf's algebraic laws,
[`L1/ls_update_column`](../L1/ls_update_column.md) §Algebraic-laws):

- Law 1 — sub-diagonal annihilation: `h_out[j+1] = 0` exactly.
- Law 2 — replay non-commutativity (a structural law, **not** a non-law): the
  stored rotations `cs[0..j-1], sn[0..j-1]` must be applied in generation
  order `k = 0, 1, ..., j-1`; reordering yields a different rotation product
  in exact arithmetic.
- Law 3 — residual exposure: `beta = |s_jp1| = min_y ‖β₀·e₁ − H̄_j · y‖₂` exactly.
- Law 4 — unitarity preservation: `cs_j² + |sn_j|² = 1`.
- Law 5 — empty/first-column boundary (`j = 0`): replay fold is empty, lowered call
  is `generate ▷ apply ▷ apply_rhs` only.
- Law 6 — basis-lift independence (GMRES ≡ FGMRES at this leaf).
- Law 7 — per-call scalar-kernel-variant invariance (real/complex absorption).

The element-type axis is absorbed at solver template instantiation
(`iterative.hpp:193` for `s, sn`; `:194` for `cs`); the column index `j` is a
size parameter. The L1 form carries **no destination buffer** and **no flat
Hessenberg register**: the prior `(cs, sn, s, h_new)` and the result bundle
are distinct values; the lowering below is where the four in-place register
overwrites and the `Hj` column-pointer arithmetic are reintroduced. The L1
form is **partial** at exact-zero `(h1[j], h1[j+1])` (Arnoldi lucky-breakdown);
Palace's convergence test reads `beta` after the leaf and the next outer
iteration's exit happens before another invocation, so on the lowered code
path the degenerate input is upstream-absorbed (not silently repaired here).

## L0 form (RHS)

The L1 value bundle `{h_out, cs_j, sn_j, s_j, s_jp1, beta} =
ls_update_column(...)` lowers into the in-place per-column running-QR update
block at `palace/linalg/iterative.cpp:634-640` (GMRES) — the canonical
surface form. The four `*PlaneRotation` calls overwrite four pre-allocated
registers by reference; the column pointer `Hj` indexes into the flat
column-major Hessenberg register `H` via stride pointer arithmetic established
at `:629`:

    // iterative.cpp:629  Hj = H.data() + j * (max_dim + 1);  (column-handle for column j)
    // iterative.cpp:634-640  the four-call per-column running-QR update:
    for (int k = 0; k < j; k++)                                 // :634  replay loop, strictly ordered k=0..j-1
    {
      ApplyPlaneRotation(Hj[k], Hj[k + 1], cs[k], sn[k]);       // :636  apply stored rotation k in-place to (Hj[k], Hj[k+1])
    }
    GeneratePlaneRotation(Hj[j], Hj[j + 1], cs[j], sn[j]);      // :638  generate new rotation; writes cs[j], sn[j]
    ApplyPlaneRotation(Hj[j], Hj[j + 1], cs[j], sn[j]);         // :639  apply new rotation to column; Hj[j+1] := 0
    ApplyPlaneRotation(s[j], s[j + 1], cs[j], sn[j]);           // :640  apply new rotation to RHS pair; s[j+1] gets the LS residual

The four sub-step calls the L1 value bundle hides, evaluated in source order:

### Sub-pattern A — the canonical GMRES per-column running-QR update

    for (int k = 0; k < j; k++)                                 // :634
    {
      ApplyPlaneRotation(Hj[k], Hj[k + 1], cs[k], sn[k]);       // :636
    }
    GeneratePlaneRotation(Hj[j], Hj[j + 1], cs[j], sn[j]);      // :638
    ApplyPlaneRotation(Hj[j], Hj[j + 1], cs[j], sn[j]);         // :639
    ApplyPlaneRotation(s[j], s[j + 1], cs[j], sn[j]);           // :640

The four-element rewrite, decomposed:

1. **The strict-order replay loop** `for (int k = 0; k < j; k++)
   ApplyPlaneRotation(Hj[k], Hj[k+1], cs[k], sn[k])` (`:634-636`). The
   ascending loop variable `k` runs `0, 1, ..., j-1` — **strictly in
   generation order**, the load-bearing ordering the L1 leaf's law 2 names a
   structural law. Each `ApplyPlaneRotation` call dispatches to the
   variant-appropriate scalar kernel (real `:227` or complex `:235`) and
   overwrites the pair `(Hj[k], Hj[k+1])` in place with
   `(cs[k]·Hj[k] + sn[k]·Hj[k+1], −s̄n[k]·Hj[k] + cs[k]·Hj[k+1])` (s̄n is
   conj(sn) in the complex case). After the loop, `Hj[0..j-1]` carry the
   super-diagonal entries of column `j` of the R-factor (the result the L1
   bundle calls `h_out[0..j-1]`), and the pair `(Hj[j], Hj[j+1])` is the
   un-annihilated 2-vector the new rotation will act on. The empty-replay
   case `j = 0` (first column of a restart cycle) is the **skip-replay**
   boundary — the `k < j` loop body does not execute — which lowers the L1
   law-5 boundary exactly.
2. **The generate-into-registers call**
   `GeneratePlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j])` (`:638`). The
   LAPACK-style scaled rotation generator (real kernel `iterative.cpp:73-108`
   with overflow/underflow scaling at `:101-108`; complex kernel `:112-118`
   with the in-comment unitarity contract `cs²+|sn|²=1` at `:118`) reads the
   pair `(Hj[j], Hj[j+1])` and **writes its two outputs into the register
   slots** `cs[j]` and `sn[j]` by reference. The L0 call has FOUR arguments
   (two reads, two writes); the L1 form has the same generate sub-step
   computing `(cs_j, sn_j)` as two fresh values returned in the bundle. The
   L0 in-place write into `cs[j]/sn[j]` is the **append** of the new rotation
   to the running stored-rotation register — this is the only call in the
   leaf that mutates a *fresh* register slot (the other three rewrite
   already-populated slots).
3. **The column-apply sub-diagonal annihilation**
   `ApplyPlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j])` (`:639`). The same
   variant scalar kernel as the replay loop, now applied to the column's own
   `(j, j+1)` pair with the just-generated rotation. By the generate
   contract, the post-condition is `Hj[j+1] = 0` **exactly** — this is the
   defining property of the generate ▷ apply pair (the L1 leaf's law 1). The
   pair-overwrite stores `(triangularised, 0)` in `(Hj[j], Hj[j+1])`; after
   this line, `Hj[0..j]` is the upper-triangular `j`-th column of the running
   R-factor (zero in row `j+1` and below).
4. **The RHS-apply residual-into-tail**
   `ApplyPlaneRotation(s[j], s[j+1], cs[j], sn[j])` (`:640`). The **same
   just-generated rotation** is applied to the RHS pair `(s[j], s[j+1])`,
   propagating the new triangularisation to the RHS so the running rotated
   system stays consistent. Since `s[j+1] = 0` on entry (the RHS was
   `β₀·e₁` and no rotation has yet touched the tail entry — the running RHS
   has populated prefix `s[0..j]` and zero tail), the overwrite stores
   `(cs[j]·s[j], −s̄n[j]·s[j])` in `(s[j], s[j+1])`. The new tail entry
   `s[j+1]` carries the least-squares residual: `|s[j+1]| = β`, the
   **residual exposure** byproduct the convergence test reads at `:642`
   (`beta = std::abs(s[j+1])`).

The destination is **four pre-allocated registers** (`Hj`/`cs`/`sn`/`s`,
inherited via stride pointer / register references from the calling
`GmresSolver::Mult`): after the four calls, `Hj[0..j+1]` carry the
triangularised column (with `Hj[j+1] = 0`), `cs[j]` and `sn[j]` carry the
newly-generated rotation (appended to the running register), and `s[j]` /
`s[j+1]` carry the rotated RHS pair with the residual concentrated in the
tail. The "no separate output bundle" rotation is each result slot being a
slot of an already-allocated input register — read-then-overwritten in place
for the column / RHS overwrites, write-into-fresh-slot for the
generate-into-registers append. The read-before-write sequencing is per-call
local (each `*PlaneRotation` reads then writes its named pair in one call);
the four calls' inter-call ordering is `replay-loop ▷ generate ▷ column-apply
▷ rhs-apply` and is load-bearing — the column-apply requires the rotation
just generated, the rhs-apply requires the same rotation just generated and
applied. No third-party register dependency, no MPI collective.

Justification kind: **structural** — the syntactic expansion of one closed-form
L1 value bundle into a four-`*PlaneRotation`-call sequence with four in-place
register overwrites. The result-bundle rotation is the four input registers
being read-then-overwritten (or written-into-fresh-slot for the
generate-into-registers append); the column-handle rotation is the flat
column-major stride pointer `Hj = H.data() + j * (max_dim + 1)` (set at
`:629`, the upstream boundary). No new vocabulary; the four scalar kernel
calls are themselves the L0 mechanism, with their own concept pages
([`givens_generate`](../concepts/givens_generate.md),
[`givens_apply`](../concepts/givens_apply.md)).

Citations:

- `palace/linalg/iterative.cpp:634` — `for (int k = 0; k < j; k++)` — the
  strict-order replay loop header.
- `palace/linalg/iterative.cpp:636` —
  `ApplyPlaneRotation(Hj[k], Hj[k + 1], cs[k], sn[k]);` — the replay
  sub-step body.
- `palace/linalg/iterative.cpp:638` —
  `GeneratePlaneRotation(Hj[j], Hj[j + 1], cs[j], sn[j]);` — the
  generate-into-registers call.
- `palace/linalg/iterative.cpp:639` —
  `ApplyPlaneRotation(Hj[j], Hj[j + 1], cs[j], sn[j]);` — the column-apply
  sub-diagonal annihilation.
- `palace/linalg/iterative.cpp:640` —
  `ApplyPlaneRotation(s[j], s[j + 1], cs[j], sn[j]);` — the RHS-apply
  residual-into-tail.
- `palace/linalg/iterative.cpp:642` — `beta = std::abs(s[j + 1]);` — the
  downstream convergence-test residual read (boundary marker; NOT part of the
  leaf, grounds the law-3 byproduct).
- `palace/linalg/iterative.cpp:629-632` — `Hj[j + 1] = linalg::Norml2(comm,
  w);` (`:631`) plus the column-handle setup `Hj = H.data() + j * (max_dim +
  1);` (`:629`) — the upstream `orthogonalize ▷ nrm2` producing `h_new` and
  setting `Hj` (boundary marker; NOT part of the leaf).
- `palace/linalg/iterative.cpp:73-108` — `GeneratePlaneRotation` (real); the
  LAPACK-style scaled rotation generator with overflow/underflow scaling at
  `:101-108`; the scalar kernel called at step 2.
- `palace/linalg/iterative.cpp:112-118` — `GeneratePlaneRotation` (complex);
  the in-comment unitarity contract `cs²+|sn|²=1` at `:118` underwriting the
  L1 leaf's law 4; the scalar kernel called at step 2 in the complex variant.
- `palace/linalg/iterative.cpp:227-241` — `ApplyPlaneRotation` (real `:227`,
  complex `:235`); the in-place 2-vector update kernel called at the replay
  loop, the column-apply, and the RHS-apply.
- `palace/linalg/iterative.cpp:612` — `s[0] = beta;` — the RHS register's
  first-call input state at the start of each restart cycle (boundary
  marker; the leaf is invoked with `s[0..j]` populated from this seed
  rotated through `j` prior rotations).
- `palace/linalg/iterative.hpp:193` — `mutable std::vector<ScalarType> s,
  sn;` — the RHS register `s` and the sine register `sn` element type
  `ScalarType` (complex in the complex case).
- `palace/linalg/iterative.hpp:194` — `mutable std::vector<RealType> cs;` —
  the cosine register `cs` always `RealType` (the law-4 `cs²+|sn|²=1`
  contract relies on cs:Real).

### Sub-pattern B — the FGMRES twin (byte-identical body)

    for (int k = 0; k < j; k++)                                 // :813
    {
      ApplyPlaneRotation(Hj[k], Hj[k + 1], cs[k], sn[k]);       // :815
    }
    GeneratePlaneRotation(Hj[j], Hj[j + 1], cs[j], sn[j]);      // :817
    ApplyPlaneRotation(Hj[j], Hj[j + 1], cs[j], sn[j]);         // :818
    ApplyPlaneRotation(s[j], s[j + 1], cs[j], sn[j]);           // :819

Structurally **byte-identical** to Sub-pattern A — the four-call rewrite is
the same call sequence with the same arguments, the registers `H, cs, sn, s`
are the **same registers** (FGMRES inherits them from `GmresSolver`,
`iterative.hpp:250-253` `using GmresSolver<OperType>::H;` etc.), the stride
formula for `Hj` is the same, and the four `*PlaneRotation` calls dispatch
to the same variant scalar kernel. **The +5 line offset between GMRES
`:634-640` and FGMRES `:813-819` is from PRECEDING differing FGMRES code
(the right-preconditioner `Z[k] = M⁻¹ V[k]` build before the orthogonalize
step), NOT from brace placement.** A line-by-line diff of the two ranges
confirms each of `:634 ≡ :813`, `:636 ≡ :815`, `:638 ≡ :817`, `:639 ≡ :818`,
`:640 ≡ :819`. (The sibling `back-solve-mutation-rotation` theme's
Sub-pattern B narrative mis-attributes a +1 line shift to brace placement;
that is incorrect — the per-column update bodies are byte-identical and the
offset is from preceding code.)

The only difference from Sub-pattern A is **purely downstream** (the basis
the consumer reads at restart-cycle close): GMRES's downstream
`linear_combination` lift reads `V[k]` (`x.Add(s[k], V[k])` at
`iterative.cpp:666`), FGMRES's reads `Z[k]` (`x.Add(s[k], Z[k])` at `:843`).
This is **outside the leaf** — the basis-lift is the L2
[`linear_combination`](../L2/linear_combination.md) composition consuming the
coordinate vector `y` (left in `s[0..j]` by the **sibling**
[`back-solve-mutation-rotation`](./back-solve-mutation-rotation.md), not by
this theme — this theme produces only the running R-factor and the rotated
RHS `s[0..j]` plus the residual byproduct `s[j+1]`). The `Z` register is
declared `mutable std::vector<VecType> Z;` at `iterative.hpp:256`
(FGMRES-specific — the right-preconditioned Krylov basis `Z[k] = M⁻¹ V[k]`).
The basis selection is the consuming L2 composition's `op.basis_kind` axis;
this leaf has no knowledge of it. **The per-column running-QR update itself
is basis-invariant** (the L1 leaf's law 6).

Justification kind: **structural** — same as Sub-pattern A. This sub-pattern
is recorded explicitly (rather than collapsed into A) because the two-form
recognition is the load-bearing evidence for the L1 leaf's law 6 basis-lift
independence: the body must be the same shape under both downstream basis
readings, and it positively is — byte-identical, in fact.

Citations:

- `palace/linalg/iterative.cpp:813` — `for (int k = 0; k < j; k++)` — FGMRES
  replay loop header (byte-identical to GMRES `:634`).
- `palace/linalg/iterative.cpp:815` —
  `ApplyPlaneRotation(Hj[k], Hj[k + 1], cs[k], sn[k]);` — FGMRES replay
  sub-step (byte-identical to GMRES `:636`).
- `palace/linalg/iterative.cpp:817` —
  `GeneratePlaneRotation(Hj[j], Hj[j + 1], cs[j], sn[j]);` — FGMRES
  generate-into-registers (byte-identical to GMRES `:638`).
- `palace/linalg/iterative.cpp:818` —
  `ApplyPlaneRotation(Hj[j], Hj[j + 1], cs[j], sn[j]);` — FGMRES column-apply
  sub-diagonal annihilation (byte-identical to GMRES `:639`).
- `palace/linalg/iterative.cpp:819` —
  `ApplyPlaneRotation(s[j], s[j + 1], cs[j], sn[j]);` — FGMRES RHS-apply
  residual-into-tail (byte-identical to GMRES `:640`).
- `palace/linalg/iterative.hpp:222` — `class FgmresSolver : public
  GmresSolver<OperType>` — FGMRES inherits from GMRES.
- `palace/linalg/iterative.hpp:250` — `using GmresSolver<OperType>::H;` —
  FGMRES inherits the Hessenberg register.
- `palace/linalg/iterative.hpp:256` — `mutable std::vector<VecType> Z;` —
  FGMRES-specific right-preconditioned-basis register (NOT read by this
  leaf — basis-lift independence boundary marker).

## The in-place four-register overwrite — the destination/RHS-collapsed-into-input machinery

The distinguishing feature of this theme — what the rotation rotates — is the
**collapse of the L1 fresh six-tuple value bundle `{h_out, cs_j, sn_j, s_j,
s_jp1, beta}` into four in-place register updates** where each result slot
*is* an already-allocated input register slot. Unlike `apply_linop` (caller-
owned destination buffer `Bx` distinct from inputs) or `dot` (returns a fresh
scalar, no register overwrite), `ls_update_column` has fresh L1 result values
that the L0 source writes **back into the same four registers it reads from**:

- **Hj is the destination AND the input.** The L0 source has **no `h_out`
  buffer** anywhere — neither caller-supplied nor internally allocated. The
  L1 result `h_out[0..j+1]` lives in the same `Hj[0..j+1]` slice that held
  `h_new[0..j+1]` on entry. The replay loop overwrites entries `0..j-1`
  in-place (pair-by-pair), the column-apply overwrites entries `j, j+1`
  in-place (storing `Hj[j+1] = 0` exactly). After the four calls, `Hj` holds
  the triangularised column; the original `h_new` is gone.
- **cs[j]/sn[j] are write-into-fresh-slot appends.** Unlike the other three
  registers (where the call reads then overwrites a populated slot), the
  generate-into-registers call (step 2) writes into slot `j` of `cs/sn`
  whose prior content is unread (slot `j` is uninitialised / zero-initialised
  garbage on the first call to the leaf at column `j`; the algorithm only
  reads `cs[0..j-1] / sn[0..j-1]` in the replay loop). The L1 fresh values
  `cs_j, sn_j` collapse into the slot `j` *append* — the slot was waiting to
  receive them. The register length `m = max_dim` is pre-allocated; the
  leaf's `j`-th invocation populates slot `j`, and the next invocation reads
  it as part of its own replay loop.
- **s[j]/s[j+1] are read-then-overwritten in place.** The RHS-apply (step 4)
  reads `(s[j], s[j+1])` and overwrites the same pair. The pre-condition
  `s[j+1] = 0` on entry is upstream-maintained (the running RHS has
  populated prefix `s[0..j]` and the tail `s[j+1..m]` is zero from
  `std::fill(s.begin(), s.end(), 0.0)` at `:611` plus the seed `s[0] = beta`
  at `:612`). After step 4, `s[j]` holds the rotated component (no longer
  the prior `s[j]`) and `s[j+1]` holds the residual entry (the load-bearing
  byproduct). **The next call's input `s[j+1]` is *this* call's output
  `s_jp1`** — the leaf cycles the populated-prefix advance through the same
  register one slot at a time.
- **It disappears at L1.** The L1 operator consumes `(cs, sn, s, j, h_new)`
  as read-only values and produces a fresh six-tuple value bundle; no
  destination, no in-place ordering, no register-slot aliasing across
  successive invocations. The L1>L0 lowering's job is to re-introduce the
  four register overwrites and the per-call read-before-write per-pair
  semantics that make the in-place collapse correct.
- **Cross-call lifetime — the registers ARE cycled across restart cycles.**
  The next restart cycle's seed at `:611-612` zeros `s` and writes `s[0] =
  beta`, the registers `cs, sn` are re-populated from slot `0` upward, the
  flat Hessenberg register `H` is overwritten in column order by successive
  invocations. The L0 source lives in four allocated registers cycled across
  many invocations (within a restart cycle: `j = 0, 1, ..., max_dim - 1`)
  and across many restart cycles (outer `for(;;)` loop). The L1 form lives
  in fresh values; the L0 source lives in four cycled registers.

This is the **destination-collapsed-into-input** rotation that the L1>L0
lowering surfaces; it is the small-register-streaming sibling of
[`back-solve-mutation-rotation`](./back-solve-mutation-rotation.md)'s
in-place RHS overwrite (the small-dense restart-cycle terminal-consumer
sibling), differing in that this theme writes FOUR registers (the running
producer accumulating R + new rotation + rotated RHS one slot at a time
across many calls) where the back-solve sibling writes ONE (the terminal
consumer collapsing R⁻¹·s back into `s` in one call).

## The flat column-major register `H` + `Hj` stride pointer — storage-representation machinery

The second piece of machinery the L1 form hides is the **flat column-major
storage of the Hessenberg / R-factor in a `std::vector<ScalarType>` slab**,
accessed via the column-handle pointer `Hj`:

- **The L1 form names `h_new : Tensor[j+2]` and `h_out : Tensor[j+2]`.** A
  one-dimensional column shape — a small abstract column vector of the new
  Hessenberg column.
- **The L0 source has no 2D matrix type for the running R + new column.**
  Instead, `H = mutable std::vector<ScalarType> H` (`iterative.hpp:192`), a
  *flat* 1D buffer of length `max_dim * (max_dim+1)` storing the full
  upper-Hessenberg matrix `H̄` column-by-column. The column-handle pointer
  `Hj = H.data() + j * (max_dim + 1)` (set at `:629` immediately before this
  leaf's loop, the upstream boundary) is the **only column-handle this leaf
  reads** — entries `Hj[0..j+1]` are this column, the rest of the slab is
  other columns this leaf does not touch.
- **Why column-major and not row-major.** The running-QR stream processes
  *one column at a time* (each arriving Arnoldi column is a new R column,
  replayed through stored rotations then triangularised by a fresh rotation
  — exactly this leaf's body). Column-major storage gives the leaf
  contiguous writes per arriving column. The downstream
  [`back-solve-mutation-rotation`](./back-solve-mutation-rotation.md) then
  reads *columns* of R one outer iteration at a time, so column-major also
  gives contiguous reads at the terminal consumer.
- **The `max_dim + 1` stride.** The slab is sized `max_dim + 1` per column
  (one extra entry to hold the sub-diagonal Hessenberg entry produced by
  `nrm2` at `:631`, which this leaf's column-apply sub-step then annihilates
  to zero at `:639` storing `Hj[j+1] = 0`). The active `j+1` columns occupy
  the leading `(j+1) × (max_dim+1)` slabs.
- **It disappears at L1.** The L1 form has the abstract `Tensor[j+2]` shape;
  the flat slab and the `Hj` pointer arithmetic are L0 plumbing — a
  transparent allocation/access pattern, algebraically equivalent to a 2D
  Hessenberg matrix indexed by `(row, column)`. The rotation is "abstract
  column → flat column-major slab + column-handle pointer".

This is a **transparent storage trick** (CLAUDE.md "Optimization tricks vs.
base algebra" — transparent performance trick: memory layout). The algebraic
content is "column `j` of the running upper-Hessenberg"; the flat-slab
realisation gives that content the same value via different memory access.
It is not load-bearing (a row-major layout, or a `dense_matrix<ScalarType>`
heap allocation, would compute identical bit-exact results — the only
difference is allocation shape and access pattern). The rotation surfaces it;
the L1 form erases it.

## Reduction order — load-bearing-numerical recording

The L1 leaf's law 2 (replay non-commutativity) records that the running-QR's
stored rotations MUST be applied **in generation order** `k = 0, 1, ..., j-1`.
This theme pins the **specific finite-precision composition** Palace
performs:

- **Ascending replay loop.** `for (int k = 0; k < j; k++)` (`:634`). `k`
  runs `0, 1, ..., j-1` — ascending, the order the rotations were
  generated by the previous `j` invocations of this leaf.
- **Strict per-rotation in-place pair update.** Each `ApplyPlaneRotation`
  call overwrites the pair `(Hj[k], Hj[k+1])` *before* the next call reads
  `(Hj[k+1], Hj[k+2])`. The replay chain is a length-`j` ordered
  composition of 2-vector FMAs, each pinning a specific finite-precision
  result.
- **Generate-before-apply ordering on the new pair.** `GeneratePlaneRotation`
  at `:638` reads the post-replay `(Hj[j], Hj[j+1])` (the pair the replay
  has *just* deposited at the column's bottom-two entries), then writes
  the new rotation into `cs[j], sn[j]`; the subsequent `ApplyPlaneRotation`
  at `:639` reads the same `(Hj[j], Hj[j+1])` (still unchanged, the generate
  did NOT mutate the column — only the registers) plus the *just-generated*
  `cs[j], sn[j]`, then overwrites the column pair with `(triangularised, 0)`.
  The two calls share the same input pair; the ordering is fixed by the
  generate-into-registers contract (write registers, then read by apply).

The IEEE-754 floating-point ordered chain
`apply(j-1, apply(j-2, ..., apply(1, apply(0, (h_new[k], h_new[k+1]))) ...))`
for each pair `(Hj[k], Hj[k+1])` in the ascending `k` order, with each
2-vector FMA `(cs[k]·Hj[k] + sn[k]·Hj[k+1], −s̄n[k]·Hj[k] + cs[k]·Hj[k+1])`
performed in the variant scalar kernel's pinned arithmetic order, is the
pinned finite-precision computation. The L1 leaf's law 2 holds in exact
arithmetic (the rotation product `Qⱼ` is what the chain computes, and `Qⱼ`
is order-sensitive), AND the chain is bit-different at finite-precision even
when rotations approximately commute (the L1 leaf §Algebraic-laws non-law).
Composed with the L2 `incremental_least_squares` rotation-stream
non-associativity that the leaf's law 2 implements
(`book/src/L2/incremental_least_squares.md:278-285`) and with the sibling
`back-solve-mutation-rotation`'s descending column-oriented eager-subtraction
order, this fixes the bit-exact reproducibility chain for GMRES / FGMRES
solutions end-to-end.

There is **no MPI collective in the per-column update**: the registers `cs,
sn, s, h_new` and the column slab `Hj` are *redundant-on-all-ranks* small
coordinate / column data (the upstream `orthogonalize` and `nrm2` at
`:630-631` were the rank-collective sites; their `Allreduce`s produce the
identical `h_new` on every rank, so this leaf's four `*PlaneRotation` calls
are purely local element-wise FMAs on identical-on-all-ranks data with no
divergence between ranks). The L1 leaf's §Semantics §"No MPI collective" is
exactly this fact. (Same situation as the sibling `back-solve-mutation-rotation`
and unlike the upstream `Dot`/`Nrm2` reductions.)

## Applicability conditions

The rewrite preserves semantics when:

1. **No observer of the prior `Hj[0..j+1]` value after the call.** The L0
   loop overwrites all `j+2` slots of the column in place, destroying the
   prior `h_new` values. The only consumer of the column after the leaf is
   the downstream `back-solve-mutation-rotation` (which reads `Hj[0..j]` as
   the upper-triangular R-factor column entries), and that consumer **wants
   the post-leaf triangularised values** — the prior `h_new` is conceptually
   consumed by the leaf. No caller reads the original `h_new` after the
   leaf. This is the structural reason the in-place column overwrite is
   valid.
2. **No observer of the prior `cs[j]/sn[j]` value before the call.** Slots
   `j` of `cs/sn` are uninitialised / zero-initialised garbage prior to this
   leaf's `j`-th invocation (the prior `j` invocations populated slots
   `0..j-1`). The generate-into-registers call (step 2) reads the column
   pair `(Hj[j], Hj[j+1])`, not the register slots — so the prior content
   of `cs[j]/sn[j]` is irrelevant. The write-into-fresh-slot append is
   valid by virtue of the slot being unused-up-to-this-call.
3. **`s[j+1] = 0` on entry.** Established by the running-RHS invariant: the
   restart-cycle seed at `:611-612` zeros `s` then writes `s[0] = beta`, and
   the prior `j` invocations of this leaf have rotated the populated prefix
   forward one slot at a time but have never touched slot `j+1`. The
   RHS-apply (step 4) relies on `s[j+1] = 0` for the residual exposure: the
   2-vector update `(cs[j]·s[j] + sn[j]·0, −s̄n[j]·s[j] + cs[j]·0) =
   (cs[j]·s[j], −s̄n[j]·s[j])` concentrates the residual into the tail
   exactly (the L1 leaf's law 3).
4. **Non-degenerate `(Hj[j], Hj[j+1])` after replay.** If the post-replay
   pair is exactly `(0, 0)` (Arnoldi lucky-breakdown: the orthogonalisation
   residual was exact-zero), the generate kernel's behaviour is degenerate
   (`cs_j = 1, sn_j = 0` typically; the rotation is identity), and the
   downstream `back-solve` would hit a zero diagonal. Palace handles this
   case by the convergence test `converged = (beta < eps)` at `:644`
   exiting **before** the next outer iteration; the leaf does **not** guard
   against degenerate input — it is an applicability boundary upstream-
   absorbed by the convergence test, not silently repaired here. (The L1
   leaf's §Algebraic-laws non-law on `(h1[j], h1[j+1]) = (0, 0)`.)
5. **The registers `cs, sn, s, H` are *redundant-on-all-ranks*.** Under the
   in-scope single-machine target (CLAUDE.md "Scope"), this is automatic
   (single rank). Inherited from the upstream `orthogonalize` and `nrm2`
   `Allreduce`s producing identical `h_new` on every rank. No collective is
   needed in this leaf itself.
6. **Element type `ScalarType` matches across `cs/sn/s` and `Hj`.**
   Established at solver template instantiation
   (`iterative.hpp:192-194` — `H, s, sn` are `std::vector<ScalarType>`;
   `cs` is `std::vector<RealType>`); the four `*PlaneRotation` calls
   dispatch to the matching variant scalar kernel uniformly. The
   element-type axis is absorbed (per the L1 leaf §Variant axes); no
   per-call branching.
7. **The column index `j` is the *active* column index within the restart
   cycle, `0 <= j < max_dim`.** The outer GMRES loop header at `:615`
   (`for (;; j++, it++)`) is unbounded; the restart-cycle exit test at
   `:645` (`if (converged || j + 1 == max_dim || it + 1 == max_it) break;`)
   triggers `break` when `j + 1 == max_dim`, terminating one short of
   overflow and guaranteeing the column-handle
   `Hj = H.data() + j * (max_dim + 1)` stays in-allocated and the register
   slots `cs[j], sn[j], s[j+1]` are within bounds. The leaf is **not
   invoked at `j = max_dim`** — the restart-cycle boundary is the outer
   loop's responsibility, not this leaf's.

## Justification kind

- **Sub-pattern A** (GMRES canonical) — `structural`. The four-call expansion
  `replay-loop ▷ generate-into-registers ▷ column-apply ▷ rhs-apply`; the
  destination-collapsed-into-input rotation is four input registers being
  read-then-overwritten or written-into-fresh-slot in place; the
  column-handle rotation is the flat column-major stride pointer set
  upstream at `:629`.
- **Sub-pattern B** (FGMRES twin) — `structural`. **Byte-identical** to A
  (same call sequence, same arguments, same register inheritance via
  `GmresSolver`); the rotation is the same. Recorded explicitly to ground
  the L1 leaf's law 6 basis-lift independence.

The theme as a whole is `structural`, resting on the L1 leaf's defining
contract laws (sub-diagonal annihilation law 1, replay non-commutativity
law 2, residual exposure law 3, unitarity preservation law 4) plus the
load-bearing transparent storage trick (flat column-major slab + `Hj` stride
pointer) plus the load-bearing numerical replay-order chain. The one
non-syntactic ingredient — the destination-collapsed-into-four-input-
registers in-place collapse — is read straight off the L0 source's own four
`*PlaneRotation` calls' reference-update semantics; **no negative-anchor
reconstruction, no literature inference, no speculative operator** — so
`firm` rather than `partly-constructive` (matching the L1 leaf's firm-on-
positive-structure status, matching the sibling `back-solve-mutation-
rotation` precedent).

## Speculative L1 operators

**None.** This theme lowers the already-firm L1
[`ls_update_column`](../L1/ls_update_column.md) operator into existing positive
L0 source ranges. It proposes no new L1 vocabulary and no new L0 conventions.

The four scalar Givens kernels (`GeneratePlaneRotation` real `:73-108` /
complex `:112-118`; `ApplyPlaneRotation` real `:227` / complex `:235`) are
covered by the cross-cutting concept pages
[`givens_generate`](../concepts/givens_generate.md) and
[`givens_apply`](../concepts/givens_apply.md); they are L0 element-local
scalar kernels with their own contract, not L1 operators in their own right
(per the L1 leaf §Dependencies decision to keep them as concept pages rather
than promote them).

The upstream column-handle setup `Hj = H.data() + j * (max_dim + 1)` at
`:629` and the upstream `orthogonalize ▷ nrm2` producing `h_new[0..j+1]` at
`:630-631` are boundary markers; the corresponding L1 leaves are
[`orthogonalize`](../L1/orthogonalize.md) (firm; the
[`orthogonalize-mutation-rotation`](./orthogonalize-mutation-rotation.md) theme
covers its lowering) and [`nrm2`](../L1/nrm2.md) (firm; the
[`nrm2-mutation-rotation`](./nrm2-mutation-rotation.md) theme covers its
lowering). They are NOT part of this theme's scope (this theme starts at
`:634` and ends at `:640`).

The downstream consumers — the convergence-test residual read at `:642` and
the terminal `back-solve` at `:652-660` — are handled by their own homes
(the L1 leaf's law-3 byproduct; the sibling theme
[`back-solve-mutation-rotation`](./back-solve-mutation-rotation.md) for the
back-solve).

## Variant axes

`ls_update_column` has the following variant axes at the L1>L0 edge (per
`classify-variant-axis`):

- **element-type / scalar-kernel-variant** (absorbed): `real` | `complex`.
  At L0 the same four-call sequence handles both — the `ScalarType` /
  `RealType` register split (`iterative.hpp:193-194`) is bound at solver
  template instantiation, the four `*PlaneRotation` calls dispatch to the
  variant scalar kernel uniformly (real `:73,:227` vs complex `:112,:235`,
  with `s̄n = conj(sn)` in the complex case). Sub-patterns A and B are
  identical across element types. At L1 collapsed to one operator
  parameterised by element type (L1 leaf §Variant axes; law 7).
- **GMRES vs FGMRES** (the two-form recognition, Sub-patterns A and B): the
  per-column update body is **byte-identical** across the two surface sites
  (the +5 line offset between `:634-640` and `:813-819` is from preceding
  FGMRES code, NOT brace placement). The L1 form has no GMRES/FGMRES
  variant — they are the same leaf, recorded twice in source. The basis the
  downstream consumer reads (`V` vs `Z`) is the consuming L2 composition's
  `op.basis_kind` axis (law 6), absorbed at this leaf.
- **restart-cycle column index `j`** (size parameter, absorbed-as-form):
  `0 <= j < max_dim`. The replay-loop length scales with `j`; the rest of
  the leaf is `j`-uniform. A size parameter, not a behavioural variant; the
  loop bounds adapt automatically (`k = 0` initial, `k < j` termination).

No sub-step-sequence axis (the running-QR stream has exactly one sub-step
ordering — `replay ▷ generate ▷ column-apply ▷ rhs-apply` — fixed at
`:634-640`; no Householder / two-sided alternative — Householder scoped out
per CLAUDE.md unimplemented-component policy, recorded at the L1 leaf
§Variant axes). No collective-reduction axis (no MPI collective in this
leaf). No reduction-strategy axis on the replay loop (the strict ascending
`k = 0..j-1` order is fixed and load-bearing — the L1 leaf's law 2, not a
selectable strategy).

## Related themes

L1 / cross-theme anchors:

- [`L1/ls_update_column`](../L1/ls_update_column.md) — the firm L1 operator
  this theme lowers; the four-sub-step semantics `replay ▷ generate ▷ apply ▷
  apply_rhs`, the seven algebraic laws (esp. law 1 sub-diagonal annihilation,
  law 2 replay non-commutativity, law 3 residual exposure, law 4 unitarity
  preservation, law 6 basis-lift independence).
- [`back-solve-mutation-rotation`](./back-solve-mutation-rotation.md) — the
  sibling theme: the restart-cycle terminal consumer of the R-factor and
  rotated RHS this leaf produces (small-dense in-place register overwrite,
  two-form GMRES/FGMRES recognition for law-6 basis-lift independence).
- [`orthogonalize-mutation-rotation`](./orthogonalize-mutation-rotation.md) —
  the upstream producer of `h_new[0..j]` (the Arnoldi orthogonalisation
  coefficients); boundary marker, NOT part of this leaf.
- [`nrm2-mutation-rotation`](./nrm2-mutation-rotation.md) — the upstream
  producer of `h_new[j+1]` (the orthogonalisation residual nrm2 at `:631`);
  boundary marker, NOT part of this leaf.
- [`L2/incremental_least_squares`](../L2/incremental_least_squares.md) — the
  firm L2 named composition; this leaf is its Face-1 single-column projection.
  L2 laws 1/2/3/6 read as L1 leaf laws 3/2/4/6 and as this theme's
  load-bearing-structural ingredients.
- [`L2-L1/incremental-least-squares-composition-lowering`](../L2-L1/incremental-least-squares-composition-lowering.md) —
  the firm L2>L1 theme; §Face-1 references this leaf as the opaque-leaf face
  of the named-composition fan-down.
- [`concepts/givens_generate`](../concepts/givens_generate.md) — the scalar
  generate kernel concept page (the LAPACK-scaled rotation generator).
- [`concepts/givens_apply`](../concepts/givens_apply.md) — the scalar apply
  kernel concept page (the element-local 2-vector FMA).
- [`concepts/plane-rotation-stream`](../concepts/plane-rotation-stream.md) —
  §"Sequential character" flagging the replay chain as a
  `sequential-obstruction` candidate at L3.

## Status

`firm` — the structural expansion of the L1 leaf into its L0 form.
