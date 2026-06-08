# ls_update_column

Mutation-lifted per-column running-QR update: `K' = ls_update_column(K, j, h_new)`
returns an advanced incremental-factorisation bundle `K'` produced by **replaying**
the stored Givens rotations `0..j-1` against the freshly-arrived Hessenberg column
`h_new`, **generating** one new rotation `(cs[j], sn[j])` that annihilates the
sub-diagonal `h_new[j+1]`, **applying** that rotation to the column (writing the
triangularised column into the `j`-th Hessenberg slot), and **applying** the same
rotation to the rotated-RHS pair `(s[j], s[j+1])` — concentrating the
least-squares residual norm `β = |s[j+1]|` in the tail as a unitary byproduct. The
**GMRES / FGMRES per-column running-QR step** — the column-streaming face that
incrementally triangularises the `(j+2)×(j+1)` upper-Hessenberg least-squares
problem `min_y ‖β₀·e₁ − H̄_j·y‖₂` and exposes the residual norm without an
explicit residual evaluation.

## Context

The GMRES / FGMRES inner loop maintains a *running QR factorisation* of the
growing `(j+2)×(j+1)` upper-Hessenberg matrix `H̄_j` produced by Arnoldi: each
arriving Hessenberg column is reduced to upper-triangular form by replaying the
stored plane rotations and generating one new rotation, so that after `j+1`
columns the leading `(j+1)×(j+1)` block is an upper-triangular factor `R`, and the
rotated RHS `s` (initialised `s = β₀·e₁`) carries the least-squares residual in its
tail entry `s[j+1]`. This per-column update — `replay ▷ generate ▷ apply ▷
apply_rhs` — is the **L2 named composition**
[`incremental_least_squares`](../L2/incremental_least_squares.md);
the fan-down of that composition onto the L1 leaves is the firm theme
[`incremental-least-squares-composition-lowering`](../L2-L1/incremental-least-squares-composition-lowering.md).

`ls_update_column` is the **opaque single-column leaf** of that fan-down — Face 1
in the theme's two-face presentation. It mirrors Palace's per-column loop body
one-to-one (`iterative.cpp:634-640` GMRES, `:813-819` FGMRES — line-for-line
identical) and hides the four per-column sub-steps (replay / generate / apply /
apply_rhs) and the residual-exposure mechanism inside the leaf as a single
"incremental triangularisation with residual side-output" operation, exactly as
the concept page's "What is *hidden* at L1" list states
(`book/src/concepts/incremental_least_squares.md:22-27`). The co-extensive
**de-fused Face 2** in the L2>L1 theme spells the same value out into the explicit
scalar Givens kernel pair ([`givens_generate`](../concepts/givens_generate.md) /
[`givens_apply`](../concepts/givens_apply.md)); the two faces advance the
factorisation state identically — the choice is presentational, not algebraic.

This leaf is the column-streaming **producer** of the R-factor `R` and rotated
RHS `s` that the firm sibling [`back_solve`](./back_solve.md) consumes at
restart-cycle close. The two are the **per-column** and **terminal** halves of
the GMRES restart-cycle least-squares chain: `ls_update_column` is invoked once
per Arnoldi column (the inner loop) and incrementally triangularises; `back_solve`
is invoked once at convergence / restart / max-iterations (the outer cycle close)
and finishes the LS solve. They share the rotation registers `cs`, `sn` and the
RHS register `s` as bundle state, but they are distinct operators with distinct
shapes and distinct algebraic content (see [`back_solve.md`](./back_solve.md) for
the naming distinction).

It is split out as its own firm L1 primitive — rather than left as a sub-step
inside the L2 composition — because (i) each layer is coherent within itself
(per CLAUDE.md "Identity-lowerings still require both L levels"), and the
column-streaming step is a self-contained, reusable atomic update with its own
laws; (ii) the L2 theme's Face-1 forward-reference was already plain-text-deferred
to a follow-on harvester (`incremental-least-squares-composition-lowering.md:87-88,
307-310`); and (iii) the per-column step is the cleanly-bounded L0 site — the
**four** `*PlaneRotation` calls — whose own L1>L0 in-place mechanics are
deferred to a forthcoming `ls-update-column-mutation-rotation` L1>L0 theme, sibling
to `back-solve-mutation-rotation` and to `orthogonalize-mutation-rotation`.

This leaf is **not** an [`apply_linop`](./apply_linop.md) variant (it operates on
small-coordinate registers `cs`, `sn`, `s` and writes a single Hessenberg column,
not a length-`N` field application of an opaque operator) and **not** a
[`back_solve`](./back_solve.md) variant (the back-solve is the terminal triangular
solve; this leaf produces the triangular factor the back-solve consumes). Its
closest structural sibling at L1 is [`orthogonalize`](./orthogonalize.md) — both
are column-streaming Krylov-state advance primitives, each invoked once per Arnoldi
column inside the [`krylov_step`](../L2/krylov_step.md) inner loop; both consume
the candidate column and the stored side-state and advance it; they differ in
what they advance (`orthogonalize` advances the *basis* and produces the
orthogonalisation coefficients that become the Hessenberg column `h_new`;
`ls_update_column` advances the *factorisation* of that same column and produces
the running R-factor + residual byproduct).

## Signature

    ls_update_column
      :: (variant: GivensKind,
          cs:    Tensor[m],          -- stored cosines, slots 0..j-1 populated
          sn:    Tensor[m],          -- stored sines,   slots 0..j-1 populated
          s:     Tensor[m+1],        -- rotated RHS, slots 0..j populated (s[j+1] yet to be touched)
          j:     Int,                -- index of the new column (0-based; j+1 total columns after this call)
          h_new: Tensor[j+2])        -- the freshly-arrived Hessenberg column, entries 0..j+1
      -> { h_out: Tensor[j+2],       -- triangularised column: h_out[0..j] upper-triangular, h_out[j+1] = 0
           cs_j:  RealScalar,        -- new cosine appended at slot j (always real)
           sn_j:  Scalar,            -- new sine    appended at slot j (Scalar = ScalarType)
           s_j:   Scalar,            -- updated RHS entry s[j]
           s_jp1: Scalar,            -- updated RHS entry s[j+1] = the LS residual entry (|s_jp1| = β)
           beta:  RealScalar }       -- |s_jp1|, the least-squares residual norm byproduct

    ls_update_column variant cs sn s j h_new =
      let h1            = replay   variant cs sn j h_new        -- apply stored rotations 0..j-1
      let (cs_j, sn_j)  = generate variant h1[j] h1[j+1]        -- generate the new rotation
      let (h_j, h_jp1)  = apply    variant cs_j sn_j h1[j] h1[j+1]  -- triangularise: h_jp1 := 0
      let (s_j, s_jp1)  = apply    variant cs_j sn_j s[j] s[j+1]    -- propagate to RHS
      let h_out         = h1 with [j ↦ h_j, j+1 ↦ h_jp1]        -- the triangularised column
      in { h_out, cs_j, sn_j, s_j, s_jp1, beta = |s_jp1| }

    where
      replay :: (GivensKind, Tensor[m], Tensor[m], Int, Tensor[j+2]) -> Tensor[j+2]
      replay variant cs sn j h_new
        = foldl (\h k -> let (h_k', h_kp1') = apply variant cs[k] sn[k] h[k] h[k+1]
                          in h with [k ↦ h_k', k+1 ↦ h_kp1'])
                h_new
                [0, 1, ..., j-1]                                  -- STRICTLY ordered, left-to-right

      generate :: (GivensKind, Scalar, Scalar) -> (RealScalar, Scalar)
        -- the firm `givens_generate` concept page; (cs, sn) annihilating dy against dx; cs² + |sn|² = 1
      apply    :: (GivensKind, RealScalar, Scalar, Scalar, Scalar) -> (Scalar, Scalar)
        -- the firm `givens_apply` concept page; (dx', dy') = (cs·dx + sn·dy, −s̄n·dx + cs·dy);  s̄n = conj(sn) complex

Shape contract (bunsen-style, named axes):

- `variant` — `GivensKind ∈ {real, complex}` — selects the scalar kernel pair; the
  L0 type-split on `ScalarType` vs `RealType` registers (`iterative.hpp:193-194`).
  Absorbed at solver instantiation; no per-call branching.
- `cs` — `Tensor[m]` of `RealScalar` — the stored cosine register (always real per
  `iterative.hpp:194` `mutable std::vector<RealType> cs;`). Slots `0..j-1` carry the
  rotations accumulated by the prior `j` invocations; slot `j` is written by this
  call. The register has capacity `m = max_dim` (the GMRES restart dimension).
- `sn` — `Tensor[m]` of `Scalar` (`ScalarType` per `iterative.hpp:193`) — the
  stored sine register. Same population / write pattern as `cs`.
- `s` — `Tensor[m+1]` of `Scalar` — the rotated RHS register. Slots `0..j` carry
  the rotated RHS so far (initialised `s[0] = β₀`, `s[k] = 0` for `k ≥ 1` at the
  start of each restart cycle, `iterative.cpp:612`); this call updates `s[j]` and
  writes `s[j+1]`.
- `j` — `Int` — the index of the new column being absorbed, `0 ≤ j < m`. The
  invariant is `j` = number of rotations already in `cs`/`sn` = number of
  populated R-factor columns = `s`'s populated-prefix length minus one.
- `h_new` — `Tensor[j+2]` of `Scalar` — the freshly-arrived Hessenberg column with
  the orthogonalisation coefficients in entries `0..j` (produced by the upstream
  [`orthogonalize`](./orthogonalize.md) call) and the sub-diagonal entry
  `h_new[j+1] = ‖residual‖` produced by the [`nrm2`](./nrm2.md) of the
  orthogonalisation residual (`iterative.cpp:629-631`). The orthogonalisation +
  nrm2 step is **upstream**, not part of this leaf.
- result `h_out` — `Tensor[j+2]` of `Scalar` — the triangularised column: entries
  `h_out[0..j]` are the upper-triangular R-factor's `j`-th column (the
  super-diagonal + diagonal entries of column `j` of the running `R`); entry
  `h_out[j+1] = 0` (the apply sub-step's defining annihilation).
- result `(cs_j, sn_j)` — the new rotation appended to the registers at slot `j`.
- result `(s_j, s_jp1)` — the updated `s[j]` and `s[j+1]` entries.
- result `beta` — `RealScalar` — `|s_jp1|`, the least-squares residual norm. This
  is the load-bearing side-output: the convergence test reads `beta` without an
  explicit residual evaluation (`iterative.cpp:642,:644`).

The empty case (`j = 0`, first column of a restart cycle) is the **skip-replay**
form: the replay fold has empty support (the `k < j` loop body does not execute,
`iterative.cpp:634-636`), and the lowered call is `generate ▷ apply ▷ apply_rhs`
only — the residual-exposure property still holds (`β = |s[1]|`). The leaf is
**not invoked at `j = m`** (the restart bound; the outer loop terminates one short
of overflow — `iterative.cpp:617`).

The lift of the bundle state forward (the next call's `cs`/`sn`/`s` are this
call's outputs spliced in) is performed by the caller (the L2
[`incremental_least_squares`](../L2/incremental_least_squares.md) named composition
that threads the column index across the inner loop). This leaf produces only the
per-column updates and the residual byproduct; the state-threading is invisible
here.

## Semantics

`ls_update_column(variant, cs, sn, s, j, h_new)` advances the incremental QR
factorisation of the upper-Hessenberg least-squares system by **one column**: the
new column is reduced to its place in the triangular factor, one new plane
rotation is appended to the register, and the rotated RHS is brought up to the new
column count. The four sub-steps:

1. **Replay** — apply the stored rotations `0..j-1` to `h_new`, **strictly in the
   order they were generated**. Each `apply(cs[k], sn[k], h[k], h[k+1])` overwrites
   the pair `(h[k], h[k+1])` with `(cs[k]·h[k] + sn[k]·h[k+1], −s̄n[k]·h[k] +
   cs[k]·h[k+1])`. After the fold, `h1[0..j-1]` are exactly the super-diagonal
   entries of the R-factor's `j`-th column, and the pair `(h1[j], h1[j+1])` is the
   un-annihilated 2-vector the new rotation will act on.
2. **Generate** — produce `(cs_j, sn_j)` annihilating `h1[j+1]` against `h1[j]`
   via [`givens_generate`](../concepts/givens_generate.md) (the LAPACK-style scaled
   rotation; the real kernel at `iterative.cpp:73-108` with overflow/underflow
   scaling `:101-108`, the complex kernel at `:112-118` with the
   `cs²+|sn|²=1` unitarity contract `:118`).
3. **Apply (column)** — apply the new rotation to its own pair: `(h_j, h_jp1) =
   apply(cs_j, sn_j, h1[j], h1[j+1])`. By the generate contract,
   `h_jp1 = 0` exactly: this is the sub-diagonal annihilation that makes the
   running factor upper-triangular.
4. **Apply (RHS)** — apply the *same* rotation to the RHS pair `(s[j], s[j+1])`:
   `(s_j, s_jp1) = apply(cs_j, sn_j, s[j], s[j+1])`. Since `s[j+1] = 0` on entry
   (the RHS was `β₀·e₁` and no rotation has yet touched the new tail), this is
   `(s_j, s_jp1) = (cs_j · s[j], −s̄n_j · s[j])`. The new tail `s_jp1` carries the
   least-squares residual: `|s_jp1| = β`, the **residual exposure** byproduct.

The L1 form is pure-functional: the same `(variant, cs, sn, s, j, h_new)` yields
the same `(h_out, cs_j, sn_j, s_j, s_jp1, beta)`. The L0 source overwrites the
caller's `Hj` / `cs` / `sn` / `s` buffers in place — the destination *is* the
input — via four `*PlaneRotation` reference-update calls:

    // iterative.cpp:634-640  (GMRES; FGMRES :813-819 is line-for-line identical)
    for (int k = 0; k < j; k++) {                                  // :634  replay loop, strictly ordered k=0..j-1
      ApplyPlaneRotation(Hj[k], Hj[k + 1], cs[k], sn[k]);          // :636  apply stored rotation k to (Hj[k], Hj[k+1])
    }
    GeneratePlaneRotation(Hj[j], Hj[j + 1], cs[j], sn[j]);         // :638  generate the new rotation; writes cs[j], sn[j]
    ApplyPlaneRotation(Hj[j], Hj[j + 1], cs[j], sn[j]);            // :639  apply it to the column; Hj[j+1] := 0
    ApplyPlaneRotation(s[j], s[j + 1], cs[j], sn[j]);              // :640  apply it to the RHS pair; s[j+1] = residual entry

The in-place reference semantics of the four kernel calls, the `Hj` column-pointer
arithmetic into the flat Hessenberg register, and the register-vs-tensor
representation difference are L1>L0 lowering concerns (the forthcoming
`ls-update-column-mutation-rotation` theme), not part of the L1 signature.

Three semantic points are load-bearing and recorded rather than smoothed:

**(1) Replay-before-generate ordering is mandatory.** The stored rotations
`0..j-1` MUST be applied to the new column before the new rotation `j` is
generated (the `for k=0..j-1` loop at `iterative.cpp:634` strictly precedes the
`GeneratePlaneRotation` at `:638`). Generating from an un-replayed column would
annihilate against the wrong diagonal and produce a non-triangular running factor.
This is the running-QR's **structural invariant**, inherited from the
[`givens`](../concepts/givens.md) §Contract replay-order rule and recorded as the
L2 entry's law 2 (`incremental_least_squares.md` §Algebraic-laws law 2). The leaf
is **not** order-invariant in this sub-step.

**(2) Residual exposure is a unitary byproduct, not an explicit norm computation.**
The least-squares residual `β = min_y ‖β₀·e₁ − H̄_j · y‖₂` is read off `|s[j+1]|`
*without* assembling or norming the residual vector in the length-`N` field — the
rotation stream `Qⱼ` is unitary (`cs² + |sn|² = 1`, `iterative.cpp:118`), so
2-norm preservation under `Qⱼ` reduces the field-space norm to the tail of the
rotated RHS. This is the load-bearing numerical property the running-QR exists for
(the *raison d'être* of the leaf, not a transparent reorder). The convergence test
reads it directly: `beta = std::abs(s[j+1])` (`iterative.cpp:642`); `converged =
(beta < eps)` (`iterative.cpp:644`).

**(3) The replay chain is bit-level non-commutative; the in-kernel reduction is
element-local.** The length-`j` ordered chain of 2-vector updates pins a specific
finite-precision composition (the L2 entry's law 2 / rotation-stream
non-associativity non-law, `book/src/L2/incremental_least_squares.md:278-285`);
reordering the stored rotations would produce the same exact-arithmetic factor
but a bit-different finite-precision factor. Per the CLAUDE.md numerical-trick
taxonomy this is a **load-bearing numerical** detail — recorded as a non-law so
callers do not treat the replay order as a free choice. **Within each scalar
kernel call**, however,
the work is element-local: a single 2-vector FMA, no cross-element reduction, no
collective. The leaf has **no MPI collective** — the registers `cs`, `sn`, `s`
are redundant-on-all-ranks small coordinate data, exactly like the registers
[`back_solve`](./back_solve.md) consumes. The
[`plane-rotation-stream`](../concepts/plane-rotation-stream.md) §"Sequential
character" `:21-23` flags the replay chain as a `sequential-obstruction`
candidate for the eventual L3 iteration rotation; recorded here as forward note.

## Algebraic laws

The laws below hold; absences are deliberate. "Exact" means exact arithmetic.

1. **Sub-diagonal annihilation (the defining contract).** After the call,
   `h_out[j+1] = 0` exactly. This is the definitional property of the
   generate ▷ apply pair: the generated rotation is **precisely the one** that
   zeros `h1[j+1]` against `h1[j]`, so the apply leaves zero in `h_out[j+1]`. The
   L0 sequence `:638-639` (`GeneratePlaneRotation` then `ApplyPlaneRotation` on the
   same pair) computes exactly this. With this law, the leading `(j+1)×(j+1)`
   block of the Hessenberg register after the leaf's `j`-th invocation is **upper
   triangular** — the structural invariant the `back_solve` leaf depends on.

2. **Replay non-commutativity (recorded as a structural law, not a non-law).**
   `ls_update_column(variant, cs, sn, s, j, h_new)` requires the stored rotations
   `cs[0..j-1]`, `sn[0..j-1]` to be applied **in generation order** (`k = 0, 1,
   …, j-1`). Reordering the stored rotations within `cs`/`sn` (or applying them
   in a different order) yields a different rotation product `Q'_j ≠ Q_j` —
   exactly as for the L2 composition (law 2; the
   [`givens`](../concepts/givens.md) replay-order rule). This is a *structural*
   law of the leaf's contract, not a finite-precision artefact: the rotation
   product itself is order-sensitive in exact arithmetic.

3. **Residual exposure (the load-bearing byproduct).** `beta = |s_jp1| =
   min_y ‖β₀·e₁ − H̄_j · y‖₂` exactly. Holds because the rotation stream
   `Qⱼ = R_j ∘ R_{j-1} ∘ … ∘ R_0` is unitary (`cs² + |sn|² = 1`,
   `iterative.cpp:118`) and 2-norm-preserving: `‖β₀·e₁ − H̄_j · y‖₂ = ‖Qⱼ · (β₀·e₁
   − H̄_j · y)‖₂`, and the `Qⱼ`-rotated system's residual lives entirely in the
   last entry (the leading `(j+1)×(j+1)` block becomes triangular and is solvable
   exactly). The L2 entry's law 1 read as a leaf-level law: `iterative.cpp:642`
   reads `beta = std::abs(s[j+1])` without an explicit residual evaluation.

4. **Unitarity preservation across the call.** If the input `(cs, sn)` are a
   valid stored-rotation register (each `(cs[k], sn[k])` satisfies
   `cs[k]² + |sn[k]|² = 1`), then the appended `(cs_j, sn_j)` also satisfies
   `cs_j² + |sn_j|² = 1` (the generate kernel's contract, `iterative.cpp:118`),
   and the rotated RHS magnitude is preserved: `|s_j|² + |s_jp1|² = |s[j]|²`
   (since `s[j+1] = 0` on entry — the rotation is applied to the 2-vector
   `(s[j], 0)`, yielding `(cs_j·s[j], −s̄n_j·s[j])` whose squared magnitude is
   `(cs_j² + |sn_j|²)·|s[j]|² = |s[j]|²`). The whole stream `Qⱼ` is therefore
   unitary, which underwrites law 3.

5. **Empty / first-column boundary.** At `j = 0` (first column of a restart
   cycle) the replay fold is empty (the `for (int k = 0; k < j; k++)` loop body
   at `iterative.cpp:634-636` does not execute) and the lowered call is
   `generate ▷ apply ▷ apply_rhs` only. Laws 1, 3, 4 hold: `h_out[1] = 0`,
   `beta = |s_1|`, unitarity preserved. The single-rotation case (`j = 0`) is a
   degenerate boundary of laws 1–4, not a special case.

6. **Basis-lift independence (GMRES ≡ FGMRES).** The bundle update this leaf
   computes is **independent of which basis the caller will lift the eventual
   `y` against** (`V` for GMRES / left-preconditioned, `Z` for FGMRES). The GMRES
   and FGMRES per-column running-QR code is line-for-line identical
   (`iterative.cpp:634-640` ≡ `:813-819`); the registers `cs`, `sn`, `s` and the
   Hessenberg column are basis-agnostic. Only the **downstream** `linear_combination`
   reconstruction (`x.Add(s[k], V[k])` `iterative.cpp:666` vs `x.Add(s[k], Z[k])`
   `:843`, after the `back_solve` leaf produces `y`) reads a different basis.
   This leaf has no knowledge of the basis — the basis choice is the consuming L2
   composition's `op.basis_kind` axis, invisible here. Same law shape as
   [`back_solve`](./back_solve.md) law 6.

7. **Per-call scalar-kernel-variant invariance (parametric absorption).** The
   real and complex variants substitute only the element-local scalar kernel
   (`generate` real `:73-108` ↔ complex `:112-118`; `apply` real `:227` ↔
   complex `:235`, with `s̄n = conj(sn)` in the complex case). The sub-step
   sequence, the ordering, the register-shape contract, and laws 1–6 are
   variant-invariant. No per-call branching on `variant`; it is fixed at solver
   instantiation.

Laws that explicitly **do not** hold:

- **Order-independence of the replay chain (bit-level).** The replay fold's
  reduction order (`k = 0, 1, …, j-1`) pins a specific finite-precision
  composition; reordering yields the same exact-arithmetic rotation product
  `Q'_j ≠ Q_j` (law 2 — different in *exact* arithmetic, since rotations don't
  commute) AND a bit-different finite-precision result even when the rotations
  *do* approximately commute. Recorded so callers do not treat the replay order
  as a free choice. (Composes with the back-solve's reduction-order non-law to
  pin the entire GMRES finite-precision solution path; `back_solve.md`
  §Algebraic-laws non-law.)

- **Per-column commutativity of the call sequence.** `ls_update_column(…, j=i,
  h_i) ▷ ls_update_column(…, j=i+1, h_{i+1})` is **not** equal to the reversed
  sequence: the `j = i+1` call's replay sub-step reads the `i`-th rotation written
  by the prior call. The leaf is **left-fold-only**, not commutative.

- **Definedness when `(h1[j], h1[j+1]) = (0, 0)`.** If the new column's
  `(j, j+1)` pair is exactly zero after replay (an Arnoldi lucky-breakdown:
  the orthogonalisation residual was exact-zero and `nrm2` returned zero), the
  generate kernel's behaviour is degenerate (`cs_j = 1`, `sn_j = 0` typically;
  the rotation is the identity), and the downstream `back_solve` would hit a
  zero diagonal `R[j][j]` and divide by zero (`back_solve.md` §Algebraic-laws
  non-law). Palace handles this case by the residual test exiting **before** the
  next outer iteration (the residual `beta` would already be at convergence). The
  leaf does **not** guard against this — it is an applicability boundary, not a
  law. Recorded so callers do not treat `h_new = 0` as a normal input.

- **Avoidance of the unitarity exposure (the residual-by-shortcut).** The
  load-bearing residual byproduct `β = |s_jp1|` is **not** a transparent
  algebraic identity that could be skipped — it is the entire reason the
  running-QR exists; replacing it with an explicit residual evaluation
  (`r = b − A·x`, `‖r‖₂`) at every step would be `O(N)` work per column instead
  of `O(j)` and would defeat the algorithm's structure. Recorded so the
  residual-by-shortcut is not classified as a transparent optimization.

## Dependencies

(scalar-kernel-composed) — `ls_update_column` is the per-column orchestration of
the firm scalar Givens kernel pair, with **no dependency on other L1 operators**.
It consumes:

- a **dense stored-rotation register** `(cs, sn)` (small coordinate space,
  dimension `m = max_dim`, redundant-on-all-ranks),
- a **dense rotated-RHS register** `s` (same dimension),
- a **dense Hessenberg column** `h_new` (dimension `j+2`),

and produces the updated rotation + RHS slots and the residual byproduct. The
four `*PlaneRotation` calls (the replay loop, the generate, the
column-apply, the RHS-apply) are atomic at L1 — their element-local 2-vector
update bodies are L0 mechanism, deferred to the forthcoming
`ls-update-column-mutation-rotation` L1>L0 theme (sibling to
`back-solve-mutation-rotation`, sibling to `orthogonalize-mutation-rotation`).

In particular it is **not** built on [`apply_linop`](./apply_linop.md) (which
applies an *opaque* operator to a length-`N` field; this leaf operates on
small-coordinate registers and a length-`j+2` column, with no opaque-operator
application), **not** built on [`back_solve`](./back_solve.md) (the back-solve
*consumes* this leaf's output `R`/`s` — apply/inverse duality, not a dependency),
**not** built on [`nrm2`](./nrm2.md) (the residual exposure is a 2-norm-free
byproduct — `|s_jp1|` reads a single scalar's magnitude, not a vector reduction),
and **not** built on [`dot`](./dot.md) (no inner product appears; the scalar
kernels are element-local FMAs).

It is the column-streaming **producer** sibling of [`back_solve`](./back_solve.md)
(the **terminal** consumer) on the GMRES restart-cycle least-squares chain
(`ls_update_column` × (j+1) ▷ `back_solve`), split by per-column-incremental vs
once-per-restart and by produces-R/s vs consumes-R/s. It is the
factorisation-streaming sibling of [`orthogonalize`](./orthogonalize.md) (the
basis-streaming column-update) on the Krylov-state-advance axis — both are invoked
once per Arnoldi column inside [`krylov_step`](../L2/krylov_step.md), and
`orthogonalize`'s output **is** this leaf's `h_new` input (the Hessenberg column
the basis-streaming produces).

`ls_update_column` is the per-column streaming atom that the L2
[`incremental_least_squares`](../L2/incremental_least_squares.md) named
composition's Face-1 (opaque-leaf) projection depends on, and the L2>L1 theme
[`incremental-least-squares-composition-lowering`](../L2-L1/incremental-least-squares-composition-lowering.md)
forward-references as Face 1 (the de-fused Face 2 is the alternative presentation,
spelled out into the scalar Givens kernel pair).

Concept references (cross-cutting; do not duplicate):

- [`concepts/givens`](../concepts/givens.md) — the cross-cutting concept page;
  contains the replay-before-generate ordering rule the leaf's law 2 inherits.
- [`concepts/givens_generate`](../concepts/givens_generate.md) — the scalar
  generate kernel concept page (the LAPACK-scaled rotation generator); the
  kernel inside the leaf's `generate` sub-step.
- [`concepts/givens_apply`](../concepts/givens_apply.md) — the scalar apply
  kernel concept page (the element-local 2-vector FMA); the kernel inside the
  leaf's `replay`, `apply`, and `apply_rhs` sub-steps.
- [`concepts/plane-rotation-stream`](../concepts/plane-rotation-stream.md) —
  the §"Sequential character" `:21-23` flagging the replay chain as a
  `sequential-obstruction` candidate at L3 (forward note for the iteration
  rotation).
- [`concepts/incremental_least_squares`](../concepts/incremental_least_squares.md) —
  the `ls_update_column` slug contract `:14` and the "What is hidden at L1" list
  `:22-27` characterising the leaf's hiding boundary.

## Variant axes

`ls_update_column` has the following variant axes at L1; all are absorbed (no
contracted load-bearing kernel axis — the sub-step sequence is fixed and unique).

- **element type / scalar-kernel variant** (absorbed, parametric per law 7):
  `complex` | `real`. The Palace GMRES/FGMRES registers are `ScalarType` (complex
  in the complex-arithmetic case, real otherwise) — `s`, `sn`, `H`, `Hj` are
  `ScalarType` (`iterative.hpp:193`); `cs` is always `RealType`
  (`iterative.hpp:194`). The four `*PlaneRotation` calls dispatch to the
  appropriate kernel variant uniformly (real `:73,:227` vs complex `:112,:235`,
  with `s̄n = conj(sn)` in the complex case); the element type is fixed at
  solver instantiation, no per-call branching. Absorbed as a uniform element-type
  parameter.
- **basis the eventual `y` is lifted against** (absorbed — NOT a structural axis
  of this leaf): `V` (GMRES / left-preconditioned) | `Z` (FGMRES /
  flexible-preconditioner). The per-column running-QR code is line-for-line
  identical across the two (`iterative.cpp:634-640` ≡ `:813-819`); the basis is
  read only by the **downstream** `linear_combination` reconstruction (after the
  `back_solve`), not by this leaf. This is the consuming L2 composition's
  `op.basis_kind` axis; it is invisible at this leaf and recorded here only to
  make the no-structural-variant explicit (law 6).
- **restart-cycle column index `j`** (parameterised, absorbed-as-form): the
  per-call column index, `0 ≤ j < max_dim`. The replay-fold length scales with
  `j`; the rest of the leaf is `j`-uniform. A size parameter, not a behavioural
  variant.

There is **no** sub-step-sequence axis (unlike the sibling
[`orthogonalize`](./orthogonalize.md) `MGS | CGS | CGS2` axis): the running-QR
stream has exactly one sub-step ordering, fixed at `iterative.cpp:632-642` —
there is no Householder / two-sided alternative (Householder scoped out per
CLAUDE.md unimplemented-component policy; recorded at the L2 entry §Variant axes
and the L2>L1 theme §"Why the sequence is fixed"). There is **no**
collective-reduction axis (the leaf has no MPI collective). There is **no**
reduction-strategy axis on the replay fold — the strict `k = 0..j-1` ordering is
fixed and load-bearing (the replay-non-commutativity law 2), not a selectable
strategy.

## Status

`firm` — firm-on-positive-structure: the per-column running-QR loop body is read
in full from positive source (`iterative.cpp:634-640` GMRES + its line-for-line
identical FGMRES twin `:813-819`), and every law is a syntactic identity on that
source (operator-algebra facts about the rotation product `Qⱼ` plus the
LAPACK-style generate kernel's annihilation contract), not a convergence fact. No
dedicated GMRES/FGMRES running-QR unit test exists (the path is exercised only
end-to-end), but a missing test does not gate syntactic-identity laws (the
`apply_linop` / `lu_solve` precedent). The two load-bearing caveats (the
replay-order non-law and the per-column non-commutativity) are carried as recorded
non-laws, not a status reduction.

## L1 vs L0 distinction

- **L0**: an in-place per-column running-QR update writing four registers
  by reference. GMRES: `for (int k = 0; k < j; k++) ApplyPlaneRotation(Hj[k],
  Hj[k+1], cs[k], sn[k]); GeneratePlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j]);
  ApplyPlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j]); ApplyPlaneRotation(s[j],
  s[j+1], cs[j], sn[j]);` (`iterative.cpp:634-640`) — the strict-order replay
  loop, the generate-writes-into-registers call, the column-apply
  sub-diagonal-zero, the RHS-apply residual-into-tail. FGMRES: line-for-line
  identical (`iterative.cpp:813-819`). The `Hj` column-pointer arithmetic into
  the flat Hessenberg register (`Hj = H + j * (max_dim + 1)`,
  `iterative.cpp:632`), the in-place reference-update semantics of all four
  kernel calls, the register-vs-tensor representation difference, and the four
  scalar kernels' own LAPACK-style scaling are L0 mechanism.
- **L1**: pure-functional `{h_out, cs_j, sn_j, s_j, s_jp1, beta} =
  ls_update_column(variant, cs, sn, s, j, h_new)`. No destination buffer in the
  signature, no `Hj` pointer arithmetic, no flat-storage stride; the result is
  a value bundle, the inputs are read-only. One operator over the rotation
  registers + RHS register + new Hessenberg column, parameterised by the
  element-type axis (absorbed) and the column-index size (absorbed). Sub-diagonal
  annihilation, replay non-commutativity, residual exposure, unitarity, and
  variant invariance hold; replay-order, per-call non-commutativity,
  `(0,0)`-pair degenerate behaviour, and residual-by-shortcut are recorded as
  explicit non-laws. (The detailed lowering — how the value-bundle output
  rewrites into the in-place four-register write at L0 — belongs to the
  forthcoming L1>L0 `ls-update-column-mutation-rotation` theme, sibling to
  `back-solve-mutation-rotation` and to `orthogonalize-mutation-rotation`.)

## Evidence

- `palace/linalg/iterative.cpp:634` — `for (int k = 0; k < j; k++)` — the GMRES
  replay loop header; strictly-ordered `k = 0..j-1` (laws 1, 2; the
  skip-replay-for-`j=0` boundary law 5).
- `palace/linalg/iterative.cpp:636` — `ApplyPlaneRotation(Hj[k], Hj[k + 1],
  cs[k], sn[k]);` — the replay sub-step body; each stored rotation `k` applied
  in-place to the `(Hj[k], Hj[k+1])` pair (law 2).
- `palace/linalg/iterative.cpp:638` — `GeneratePlaneRotation(Hj[j], Hj[j + 1],
  cs[j], sn[j]);` — the generate sub-step; produces the new rotation
  `(cs[j], sn[j])` annihilating the sub-diagonal `Hj[j+1]` against `Hj[j]` (laws
  1, 4).
- `palace/linalg/iterative.cpp:639` — `ApplyPlaneRotation(Hj[j], Hj[j + 1],
  cs[j], sn[j]);` — the column-apply sub-step; writes `Hj[j+1] := 0` exactly
  (law 1).
- `palace/linalg/iterative.cpp:640` — `ApplyPlaneRotation(s[j], s[j + 1],
  cs[j], sn[j]);` — the RHS-apply sub-step; the same rotation applied to the
  RHS pair concentrates the residual in the new tail entry (law 3).
- `palace/linalg/iterative.cpp:642` — `beta = std::abs(s[j + 1]);` — the
  residual exposure: the LS residual norm `β = |s[j+1]|` read off the RHS tail
  with no explicit residual evaluation (law 3 byproduct).
- `palace/linalg/iterative.cpp:629-632` — `Hj[j + 1] = linalg::Norml2(comm,
  w);` (`:631`) — the upstream orthogonalisation + nrm2 producing the new
  column's sub-diagonal entry; NOT part of this leaf (the
  [`orthogonalize`](./orthogonalize.md) leaf produces `h_new[0..j]`, the
  [`nrm2`](./nrm2.md) produces `h_new[j+1]`), grounded here to mark the leaf's
  upstream boundary.
- `palace/linalg/iterative.cpp:813-819` — FGMRES per-column running-QR update;
  **line-for-line identical** to GMRES `:634-640` (law 6: GMRES ≡ FGMRES at
  this leaf).
- `palace/linalg/iterative.cpp:821` — FGMRES `beta = std::abs(s[j + 1]);` —
  the residual exposure in the FGMRES twin; identical to GMRES `:642`.
- `palace/linalg/iterative.cpp:73-108` — `GeneratePlaneRotation` (real): the
  LAPACK-style scaled rotation generator inside the leaf's `generate` sub-step
  for the real variant; scaling at `:101-108`.
- `palace/linalg/iterative.cpp:112-118` — `GeneratePlaneRotation` (complex):
  the complex variant; in-comment unitarity contract "cs is real and
  cs²+|sn|²=1" at `:118` (underwrites law 4).
- `palace/linalg/iterative.cpp:227-241` — `ApplyPlaneRotation` (real `:227` +
  complex `:235`): the in-place 2-vector update `(dx', dy') = (cs·dx + sn·dy,
  −s̄n·dx + cs·dy)` inside the leaf's replay, column-apply, and RHS-apply
  sub-steps.
- `palace/linalg/iterative.cpp:644` — `converged = (beta < eps);` — the
  convergence test reading the residual byproduct directly (the leaf's
  byproduct law 3 ground-trothed; not part of the leaf but bounds when the
  outer loop exits before the next call).
- `palace/linalg/iterative.cpp:612` — `s[0] = beta;` — the RHS initialisation
  `s = β₀·e₁` at the start of each restart cycle; sets the leaf's first-call
  input state.
- `palace/linalg/iterative.hpp:193` — `mutable std::vector<ScalarType> s, sn;`
  — the RHS register `s` and the sine register `sn` element type `ScalarType`
  (complex in the complex case). Grounds the `s` / `sn` element-type axis (law
  7).
- `palace/linalg/iterative.hpp:194` — `mutable std::vector<RealType> cs;` —
  the cosine register `cs` always `RealType` (the element-type split
  underwriting the real/complex variant axis; cs is always real per the
  generate kernel's contract `iterative.cpp:118`).
- `book/src/L2/incremental_least_squares.md` — the firm L2 named composition;
  this leaf is its Face-1 single-column projection (the
  composition's per-column body collapses into one `ls_update_column` call).
  The L2 entry's laws 1, 2, 3, 6 (residual exposure, replay ordering, unitary
  byproduct, basis-lift independence) read as leaf-level laws 3, 2, 4, 6.
- `book/src/L2-L1/incremental-least-squares-composition-lowering.md` — the firm
  L2>L1 theme; §Face-1 (`:67-90`) forward-references this leaf as
  the opaque-leaf face of the named-composition fan-down; §"Speculative L1
  operators" (`:307-310`) records the leaf as a follow-on harvester target —
  resolved by this entry.
- `book/src/L1/back_solve.md` — the firm sibling leaf; the
  terminal consumer of the R-factor and rotated RHS this leaf produces. The
  structural template (small-dense register operating leaf,
  firm-on-positive-structure with no dedicated test, recorded reduction-order
  non-law) and the slug-naming precedent (`back_solve` distinct from the
  general `trsv`; this leaf `ls_update_column` distinct from `back_solve`).
- `book/src/concepts/incremental_least_squares.md:14` — the `ls_update_column`
  slug contract (`ls_update_column(K, j, h_new) → K'`); the cross-method reuse
  rationale and the "What is hidden at L1" list `:22-27` characterising the
  leaf's hiding boundary.
- `book/src/concepts/plane-rotation-stream.md:21-23` — the §"Sequential
  character" flagging the replay chain as a `sequential-obstruction`
  candidate at L3 (forward note; not content of this L1 entry).
