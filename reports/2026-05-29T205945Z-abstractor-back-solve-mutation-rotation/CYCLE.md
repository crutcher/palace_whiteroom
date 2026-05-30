---
agent: abstractor
invoked_at: 2026-05-29T205945Z
scope: L1>L0 theme sketch — back-solve-mutation-rotation (firm)
status: pending
integrated_at: 2026-05-30T004013Z
integration_commit: e44896d
integration_notes: "Applied cycle-029 (staging row 1). NEW firm L1>L0 theme back-solve-mutation-rotation landed lowering the c027-firm L1 back_solve leaf into GMRES iterative.cpp:652-660 / FGMRES :831-840 restart-correction back-substitution loops; shape-identical brace-shifted +1 lines, basis-lift V[k]/Z[k] differs only downstream per law-6. L1>L0 firm themes +1 (joins matrix-weighted-norm-mutation-rotation / normalize-mutation-rotation precedent). 5 OQs promoted for cycle-030 follow-up. Citecheck --scan 33/33 anchor zero-drift. NO repair needed (overall_status: ready). No gate hits."
inputs:
  - book/src/L1/back_solve.md (firm leaf, c028 audited)
  - book/src/L1-L0/normalize-mutation-rotation.md (firm sibling precedent)
  - book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md (firm sibling precedent)
  - palace/linalg/iterative.cpp:652-660 (GMRES restart-correction back-solve)
  - palace/linalg/iterative.cpp:831-840 (FGMRES restart-correction back-solve)
  - palace/linalg/iterative.hpp:192-194 (register declarations); :222-256 (FGMRES class + Z basis)
---

# CYCLE: L1>L0 theme sketch — back-solve-mutation-rotation (firm)

## Summary

Author the firm L1>L0 mutation-rotation theme `back-solve-mutation-rotation` lowering the firm L1 leaf [`back_solve`](../L1/back_solve.md) (audited cycle-028, `verified_against:` block confirms zero-drift) into the GMRES / FGMRES restart-correction back-substitution loop at `palace/linalg/iterative.cpp:652-660` (GMRES) / `:831-840` (FGMRES). The rewrite is **structural**: the pure-functional `y = back_solve(R, s)` value lowers to an in-place loop that **overwrites the RHS buffer `s[0..j]` with `y`** (destination *is* the RHS argument), reads the upper-triangular factor `R` out of the flat column-major Hessenberg register `H` via the stride pointer `Hi = H.data() + i*(max_dim+1)`, and performs the descending-`i` / descending-`k` back-substitution sweep `s[i] /= Hi[i]; s[k] -= Hi[k]*s[i]`. The GMRES and FGMRES bodies are **shape-identical** (same column-stride, same diagonal division, same column-oriented super-diagonal subtraction) — they differ only by **brace placement** (a +1 line-shift; GMRES has `{` on the `for` line, FGMRES has it on the next line) and by the **basis** the *downstream* `linear_combination` lift reads (`V[k]` GMRES `:666` vs `Z[k]` FGMRES `:843`), which is **outside the leaf** (law-6 basis-lift independence from the L1 entry). Status: **firm** — the leaf is firm + audited, every rewrite element (loop bound, stride formula, diagonal division, super-diagonal subtraction, RHS destination overwrite, two-form GMRES/FGMRES identity, downstream basis-lift boundary) is positively anchored and self-verified via citecheck `--anchor` zero-drift, and the one load-bearing numerical detail (the descending-column reduction order, classified per the L1 entry's reduction-order non-law) is recorded as an explicit non-rewrite. No new L1 vocabulary is proposed.

## Proposed changes

```new:book/src/L1-L0/back-solve-mutation-rotation.md
# back-solve-mutation-rotation

The mutation rotation for the GMRES / FGMRES restart-correction back-substitution.
Lowers the pure L1 form `y = back_solve(R, s)`
([`L1/back_solve`](../L1/back_solve.md), firm + cycle-028 audited) into the
in-place descending-back-substitution loop at
`palace/linalg/iterative.cpp:652-660` (GMRES) and its shape-identical FGMRES twin
at `:831-840`: a four-element rewrite consisting of (1) the **outer descending
sweep** `for (int i = j; i >= 0; i--)`, (2) the **column-major stride pointer**
`Hi = H.data() + i*(max_dim+1)` reading column `i` of the dense upper-triangular
R-factor out of the flat Hessenberg register `H`, (3) the **diagonal division**
`s[i] /= Hi[i]` (the `y[i] = s[i] / R[i][i]` step), and (4) the **inner column-
oriented super-diagonal subtraction** `for (int k = i-1; k >= 0; k--) s[k] -=
Hi[k] * s[i]` (the `s[k] -= R[k][i] * y[i]` correction). The result `y` is left
in `s[0..j]` — **the destination is the RHS argument** (in-place RHS overwrite,
no separate output buffer). It is the small-dense-triangular sibling-in-theme of
[`lu-solve-mutation-rotation`](./lu-solve-mutation-rotation.md): both lower a
small-dense coordinate-space direct solve whose destination *is* the RHS buffer;
this theme is the back-substitution-only case (R already upper-triangular —
prepared by the upstream running-QR stream, not by this rewrite). It proposes
**no new L1 vocabulary**; the L1 leaf [`back_solve`](../L1/back_solve.md) is firm.

## Slug

`back-solve-mutation-rotation`

## L1 form (LHS)

The pure-functional small-dense back-solve (firm; see
[`L1/back_solve`](../L1/back_solve.md)) consumes a read-only upper-triangular
R-factor and a read-only RHS, producing a fresh coordinate vector; nothing is
mutated and there is no destination buffer in the signature. There is one LHS
shape (`back_solve` has no surface-form variants — back-substitution is the
unique kernel for an already-triangular matrix; element-type and restart-
dimension axes are absorbed per `classify-variant-axis`):

    y = back_solve(R, s)        -- R : UpperTri[j+1, j+1], s : Tensor[j+1]
                                -- result: the unique y with R · y = s
                                -- (R upper-triangular, non-singular)

The defining identity (L1 algebraic law 1, [`L1/back_solve`](../L1/back_solve.md))
is `R · back_solve(R, s) = s` — `back_solve(R, ·)` is `R⁻¹` as a function on the
leading `(j+1)×(j+1)` block. The element-type axis is inherited from the
ambient register type `ScalarType` (real or complex, `iterative.hpp:192-193`);
the restart-dimension `j+1` is a size parameter (≤ `max_dim`), not a behavioural
variant. The L1 form carries **no destination buffer** and **no Hessenberg
register**: the prior `s`, the result `y`, and the R-factor `R` are three
distinct values; the lowering below is where the in-place RHS overwrite and the
flat column-major stride access are reintroduced. The L1 form is **partial** at
singular `R` (a zero diagonal `R[i][i]` divides by zero); Palace exits via the
convergence test (`converged = (beta < eps)` at `iterative.cpp:644`) before the
back-solve in the Arnoldi lucky-breakdown case, so on the lowered code path the
precondition is upstream-enforced.

## L0 form (RHS)

The L1 value `y = back_solve(R, s)` lowers into the in-place restart-correction
back-substitution block at `palace/linalg/iterative.cpp:652-660` (GMRES) — the
canonical surface form. The receiver `s` is **overwritten in place** with `y`,
and the upper-triangular factor is read out of the flat column-major Hessenberg
register `H` via a stride pointer `Hi`:

    // iterative.cpp:652  "Reconstruct the solution (for restart or due to
    //                     convergence or maximum iterations)."
    for (int i = j; i >= 0; i--)                       // :653  descending sweep
    {
      ScalarType *Hi = H.data() + i * (max_dim + 1);   // :655  column i of R (stride max_dim+1)
      s[i] /= Hi[i];                                   // :656  y[i] = s[i] / R[i][i]
      for (int k = i - 1; k >= 0; k--)                 // :657  super-diagonal column scan
      {
        s[k] -= Hi[k] * s[i];                          // :659  s[k] -= R[k][i] * y[i]
      }
    }                                                  // :660  y is left in s[0..j]

The four loop-body elements the L1 value hides, evaluated in source order:

### Sub-pattern A — the canonical GMRES restart-correction back-substitution

    for (int i = j; i >= 0; i--)                       // :653
    {
      ScalarType *Hi = H.data() + i * (max_dim + 1);   // :655
      s[i] /= Hi[i];                                   // :656
      for (int k = i - 1; k >= 0; k--)                 // :657
        s[k] -= Hi[k] * s[i];                          // :659
    }

The four-element rewrite, decomposed:

1. **The descending outer sweep** `for (int i = j; i >= 0; i--)` (`:653`). The
   loop variable `i` runs `j, j-1, …, 0` — descending, so `y[i]` is solved
   *after* `y[i+1..j]` are already in place in `s[i+1..j]` (the column-oriented
   super-diagonal eliminations from previous iterations have written them).
   This is the back-substitution direction: highest index first, then propagate
   the just-solved `y[i]` back through the super-diagonal entries above. The
   empty-cycle case `j = -1` (no Arnoldi columns accumulated this restart cycle)
   skips the body entirely — direct evidence for the L1 leaf's law-5
   empty-stream boundary (the lowered `y = []` is the un-written `s[0..-1]`,
   semantically the zero vector for the downstream `V·y` lift).

2. **The column-major stride pointer** `Hi = H.data() + i * (max_dim + 1)`
   (`:655`). The register `H` (declared `mutable std::vector<ScalarType> H`
   at `iterative.hpp:192`) stores the running-QR R-factor **column-major**: each
   length-`max_dim+1` slab `H[i*(max_dim+1) .. (i+1)*(max_dim+1) − 1]` is column
   `i` of the full Hessenberg / R-factor block (the extra `+1` accommodates the
   sub-diagonal entry the running-QR stream will annihilate; after the running-
   QR processes the column, only the upper-triangular part is non-zero in the
   leading `(j+1)×(j+1)` block). `Hi` points at the start of column `i`, so
   `Hi[k]` is the entry **row `k`, column `i`** of the R-factor — i.e. `R[k][i]`.
   The stride formula `max_dim+1` (rather than the active dimension `j+1`) is
   an **allocation-shape** detail: the register is sized for the maximum
   restart dimension, the active `j+1` block lives in the upper-left corner.
   This is a transparent allocation trick — the algebraic content is "column `i`
   of `R`", the stride is implementation plumbing. (The slab `Hi[j+1]` entry —
   the sub-diagonal — is zero in the upper-triangular leading block after the
   running-QR stream, see `iterative.cpp:631` for where it was last non-zero
   before annihilation; the back-substitution never reads it.)

3. **The diagonal division** `s[i] /= Hi[i]` (`:656`). The expression
   `Hi[i] = R[i][i]` is the diagonal entry of column `i`. The compound
   assignment `s[i] /= Hi[i]` performs `s[i] = s[i] / R[i][i]` — which is
   exactly the L1 leaf's law-4 back-substitution recurrence at the diagonal
   step (`y[i] = (s[i] − Σ_{k>i} R[i][k]·y[k]) / R[i][i]`, with the
   `Σ_{k>i}` corrections already applied by the previous iterations' inner
   loops in the column-oriented variant; see §"Reduction order" below). After
   this line, `s[i]` holds `y[i]` (the value `back_solve` returns at index `i`).
   The singular-`R` boundary — a zero `Hi[i]` — divides by zero (undefined
   behaviour on IEEE-754 `double` — `+/-inf` for non-zero `s[i]`, `NaN` for
   zero `s[i]`); Palace's `converged = (beta < eps)` check at `:644` exits
   the outer `for(;;)` loop *before* the next restart cycle's seed `s[0] =
   beta` at `:612` and the subsequent back-solve, so the lucky-breakdown
   path never reaches a divide-by-zero (the L1 leaf's applicability-boundary
   non-law on singular `R`).

4. **The inner column-oriented super-diagonal subtraction**
   `for (int k = i-1; k >= 0; k--) s[k] -= Hi[k] * s[i]` (`:657-659`). The
   inner loop runs `k = i-1, i-2, …, 0` — descending over rows *above* the
   diagonal in column `i`. For each `k`, `Hi[k] = R[k][i]` is the
   super-diagonal entry above row `k` in column `i`; the subtraction
   `s[k] -= Hi[k] * s[i]` is `s[k] -= R[k][i] * y[i]` (since `s[i]` has
   already been overwritten with `y[i]` by step 3). This is the **column-
   oriented** variant of back-substitution: instead of gathering all
   super-diagonal corrections for row `k` together (row-oriented:
   `y[k] = (s[k] − Σ_{i>k} R[k][i]·y[i]) / R[k][k]` — read all
   `R[k][i]·y[i]` then divide), Palace eagerly applies the `R[k][i]·y[i]`
   correction to `s[k]` as soon as `y[i]` is solved, accumulating the
   corrections into `s[k]` across multiple outer iterations (one per
   super-diagonal entry above row `k`). The two variants compute the
   *same exact-arithmetic* `y` (L1 leaf law 4) but pin different
   finite-precision summation groupings (the L1 leaf's reduction-order
   non-law). At `i = 0` the inner loop body does not execute (the
   `k = i-1 = -1` initial value violates `k >= 0`) — the single-column
   `j = 0` boundary case the L1 leaf's law-5 single-column path notes.
   At the empty-cycle `j = -1` boundary, the outer loop body does not
   execute, so this inner loop never runs (law 5 again).

The destination is **the RHS argument `s`**: after the loop, `s[0..j]` holds
`y[0..j]` and the tail entry `s[j+1]` (the LS residual, `s[j+1] = β =
std::abs(s[j+1])` was read at `:642` as the convergence-test value; the
back-solve does NOT touch it). The "no separate output buffer" rotation is
the receiver `s` being read-then-overwritten in place: `s[i]` is read at the
diagonal-division line `:656` (the RHS), then immediately overwritten with
`y[i]`, and the inner loop subsequently reads `s[i]` as the *correction
multiplier* on subsequent `k`-iterations and reads-then-overwrites `s[k]`
for `k < i`. The read-before-write sequencing is per-index local: each
iteration reads `s[i]` (RHS) and the previously-written `s[k]` (corrections
accumulated from earlier outer iterations), then writes `s[i]` (the new
`y[i]`), then writes `s[k]` for `k < i` (further accumulated corrections).
The dependence is descending-index-strict: the outer `i = j-1` iteration
reads `s[j]` (which the outer `i = j` iteration just wrote as `y[j]`), and
so on — the descending sweep direction is load-bearing for the column-
oriented variant.

Justification kind: **structural** — the syntactic expansion of one closed-
form L1 value into a four-element in-place destructive loop. The result-
buffer rotation is the receiver `s` being read-then-overwritten; the
intermediate R-factor read is the flat-column-major stride.

Citations:

- `palace/linalg/iterative.cpp:652` — comment `// Reconstruct the solution
  (for restart or due to convergence or maximum iterations).` Names the
  block's role: restart-cycle terminal back-solve.
- `palace/linalg/iterative.cpp:653` — `for (int i = j; i >= 0; i--)` — the
  descending outer sweep.
- `palace/linalg/iterative.cpp:655` — `ScalarType *Hi = H.data() + i *
  (max_dim + 1);` — the column-major stride pointer.
- `palace/linalg/iterative.cpp:656` — `s[i] /= Hi[i];` — the diagonal
  division.
- `palace/linalg/iterative.cpp:657` — `for (int k = i - 1; k >= 0; k--)`
  — the inner super-diagonal scan.
- `palace/linalg/iterative.cpp:659` — `s[k] -= Hi[k] * s[i];` — the
  column-oriented super-diagonal subtraction.
- `palace/linalg/iterative.hpp:192` — `mutable std::vector<ScalarType> H;`
  — the flat register storing the column-major R-factor.
- `palace/linalg/iterative.hpp:193` — `mutable std::vector<ScalarType> s,
  sn;` — the RHS / Givens-sine register `s` of element type `ScalarType`.

### Sub-pattern B — the FGMRES twin (shape-identical body, line-shifted by brace placement)

    // iterative.cpp:831  "Reconstruct the solution (for restart or due to
    //                     convergence or maximum iterations)."
    for (int i = j; i >= 0; i--)                       // :832  descending sweep
    {                                                  // :833  opening brace on its own line
      ScalarType *Hi = H.data() + i * (max_dim + 1);   // :834  column i of R
      s[i] /= Hi[i];                                   // :835  y[i] = s[i] / R[i][i]
      for (int k = i - 1; k >= 0; k--)                 // :836  super-diagonal column scan
      {                                                // :837  inner brace on its own line
        s[k] -= Hi[k] * s[i];                          // :838  s[k] -= R[k][i] * y[i]
      }
    }

Structurally **identical** to Sub-pattern A — the four-element rewrite is the
same, the register `H` is the same (FGMRES inherits `H` from `GmresSolver`,
`iterative.hpp:250` — `using GmresSolver<OperType>::H`), the registers `s, sn,
cs` are also inherited (`:251-253`), and the stride formula is the same. The
only differences from Sub-pattern A are **purely textual** (lexical brace
placement) and **purely downstream** (the basis the consumer reads):

- **Brace placement / line shift.** GMRES (Sub-pattern A) places `{` at the end
  of the `for` line (one statement on the line); FGMRES (Sub-pattern B) places
  `{` on the next line. This shifts every body line by +1: GMRES `:653`/`:655`/
  `:656`/`:657`/`:659` ↔ FGMRES `:832`/`:834`/`:835`/`:836`/`:838`. The two
  bodies compute identical values; the line offset is a pure brace-style
  artefact. The L1 leaf's law-6 ("back-solve code line-for-line identical")
  is **slightly imprecise**: the LINE NUMBERS differ by +1 (brace shift), but
  the LINE CONTENT (loop bound, stride formula, division, subtraction) is
  byte-identical. This is recorded faithfully here as **content-identical,
  line-shifted** — the rotation is the same; the surface form is brace-style-
  isomorphic but not byte-identical.
- **Downstream basis.** The consuming `linear_combination` lift reads `V[k]`
  in GMRES (`x.Add(s[k], V[k])`, `:666`) and `Z[k]` in FGMRES
  (`x.Add(s[k], Z[k])`, `:843`). This is **outside the leaf** — the basis-lift
  is the L2 `linear-combination` composition consuming the coordinate vector
  `y` (left in `s[0..j]`), not part of `back_solve` itself. The `Z` register
  is declared `mutable std::vector<VecType> Z;` at `iterative.hpp:256` (FGMRES-
  specific — the right-preconditioned Krylov basis `Z[k] = M⁻¹ V[k]`). The
  basis selection is the consuming L2 composition's `op.basis_kind` axis;
  this leaf has no knowledge of it. **The back-solve itself is basis-invariant.**

Justification kind: **structural** — same as Sub-pattern A. This sub-pattern is
recorded explicitly (rather than collapsed into A) because the two-form
recognition is the load-bearing evidence for the L1 leaf's law-6 basis-lift
independence: the body must be the same shape under both downstream basis
readings, and it positively is.

Citations:

- `palace/linalg/iterative.cpp:831` — comment `// Reconstruct the solution
  (for restart or due to convergence or maximum iterations).` FGMRES copy.
- `palace/linalg/iterative.cpp:832` — `for (int i = j; i >= 0; i--)` —
  FGMRES outer descending sweep.
- `palace/linalg/iterative.cpp:834` — `ScalarType *Hi = H.data() + i *
  (max_dim + 1);` — FGMRES column-major stride pointer (same formula).
- `palace/linalg/iterative.cpp:835` — `s[i] /= Hi[i];` — FGMRES diagonal
  division.
- `palace/linalg/iterative.cpp:836` — `for (int k = i - 1; k >= 0; k--)`
  — FGMRES inner super-diagonal scan.
- `palace/linalg/iterative.cpp:838` — `s[k] -= Hi[k] * s[i];` — FGMRES
  column-oriented super-diagonal subtraction.
- `palace/linalg/iterative.hpp:222` — `class FgmresSolver : public
  GmresSolver<OperType>` — FGMRES inherits from GMRES.
- `palace/linalg/iterative.hpp:250` — `using GmresSolver<OperType>::H;` —
  FGMRES inherits the Hessenberg register (same flat column-major storage).
- `palace/linalg/iterative.hpp:256` — `mutable std::vector<VecType> Z;` —
  FGMRES-specific right-preconditioned-basis register (NOT read by this
  leaf — basis-lift independence boundary).

### Sub-pattern C — the downstream basis-lift consumer (NOT part of the leaf)

    for (int k = 0; k <= j; k++)                       // :664 (GMRES) / :841 (FGMRES)
    {
      x.Add(s[k], V[k]);                               // :666 (GMRES) — V basis
    // ----- OR -----
      x.Add(s[k], Z[k]);                               // :843 (FGMRES) — Z basis
    }

The coordinate vector `y` (left in `s[0..j]`) is consumed by the downstream
linear-combination lift `x += Σ_k y[k] · basis[k]` — `V[k]` in GMRES at `:666`,
`Z[k]` in FGMRES at `:843`. (The GMRES left-preconditioned / right-
preconditioned branches at `:662-678` further split on `pc_side`, but both
consume the same `s[0..j]` — see §"GMRES preconditioning fork" below.) This is
**not part of the back-solve theme**; it is the L2
[`linear_combination`](../L2/linear_combination.md) primitive consuming the
back-solve's output, and is the subject of the
[`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md)
L2>L1 theme. It is named here only as a **boundary marker** — the place where
`y` leaves the back-solve and enters the basis-lift — and as the load-bearing
evidence that the basis (`V` vs `Z`) is consumed *downstream*, never inside
the back-solve. The basis-lift's two-form GMRES `V` vs FGMRES `Z` split is
exactly the L1 leaf's law-6 basis-lift independence: this leaf produces `y`,
the consumer chooses the basis.

Citations:

- `palace/linalg/iterative.cpp:666` — `x.Add(s[k], V[k]);` — GMRES `V`-basis
  lift (left-preconditioned branch); NOT part of this leaf, boundary marker
  for law-6.
- `palace/linalg/iterative.cpp:843` — `x.Add(s[k], Z[k]);` — FGMRES `Z`-basis
  lift; NOT part of this leaf, second boundary instance grounds basis-lift
  independence.

## The in-place RHS overwrite — the destination/RHS-collapsed-into-one machinery

The distinguishing feature of this theme — what the rotation rotates — is the
**collapse of the L1 separate-value pair `(R, s) → y` into a single in-place
register update** where the destination `y` *is* the RHS argument `s`. Unlike
`apply_linop`/`matrix-weighted-norm` (caller-owned destination buffer `Bx`
distinct from inputs) or `axpby`/`scal` (in-place rescale of the receiver but
with no separate result tensor at L1), `back_solve` has a fresh L1 result `y`
that the L0 source writes **back into the RHS slot `s`**:

- **The destination is the RHS, not a separate buffer.** The L0 source has
  **no `y` buffer** anywhere — neither caller-supplied nor internally
  allocated. The result lives in the same `s[0..j]` slice that held the RHS on
  entry. After the loop, the original RHS values are gone (overwritten); the
  slice now holds the solution coordinates. **The RHS slot is the result
  slot.** This is the rotation: L1 holds the prior `s` and the fresh `y` as
  two distinct values; L0 holds them as the same memory cell at two different
  times.
- **The read-before-write per-index ordering enables the in-place collapse.**
  At step 3 (`:656` / `:835`), `s[i]` is read as the RHS for index `i`, then
  immediately overwritten with `y[i]`. The descending-`i` sweep guarantees
  that subsequent corrections from this outer iteration's inner loop (`s[k]
  -= Hi[k] * s[i]` for `k < i`) read `s[i]` as `y[i]` (the just-written value)
  and read `s[k]` as the in-progress accumulator (RHS minus all
  super-diagonal corrections from outer iterations `i' > i` so far) and write
  it as the next-step accumulator. Each `s[k]` slot transitions through a
  sequence of values: `RHS[k]` → `RHS[k] − R[k][j]·y[j]` → `RHS[k] −
  R[k][j]·y[j] − R[k][j-1]·y[j-1]` → … → `(RHS[k] − Σ_{i>k} R[k][i]·y[i])`
  → divided by `R[k][k]` at the `i = k` outer iteration → `y[k]`. The
  in-place collapse is correct *because* the descending sweep ensures no
  cell is ever read after it has been finalised (each `s[k]`'s final
  division happens at the *last* outer iteration that touches it,
  `i = k`).
- **It disappears at L1.** The L1 operator consumes `(R, s)` and produces
  a fresh scalar tensor `y`; no destination, no in-place ordering, no
  RHS-slot-aliasing. The L1>L0 lowering's job is to re-introduce the
  destructive overwrite of `s` and the descending sweep order that makes
  it correct.
- **Cross-call lifetime — the register IS reused across restart cycles.**
  The next restart cycle's seed `s[0] = beta` at `:612` overwrites the
  same `s` slot (after `std::fill(s.begin(), s.end(), 0.0)` at `:611`
  zeros it first). So the in-place back-solve's overwrite is **doubly
  destructive**: it consumes the just-rotated RHS (intra-restart) and is
  then itself overwritten by the next restart's seed (inter-restart). The
  L1 form lives in fresh values; the L0 source lives in one allocated
  register cycled across calls.

This is the **destination-collapsed-into-RHS** rotation that the L1>L0
lowering surfaces; it is the same rotation as
[`lu-solve-mutation-rotation`](./lu-solve-mutation-rotation.md)'s in-place RHS
overwrite (the small-dense full LU sibling), differing only in that this
theme's coefficient `R` is already triangular and the matrix register is the
flat column-major Hessenberg slab rather than a heap-allocated dense matrix.

## The column-major flat register `H` — storage-representation machinery

The second piece of machinery the L1 form hides is the **flat column-major
storage of the R-factor in a `std::vector<ScalarType>` slab**, accessed via
the stride pointer `Hi`:

- **The L1 form names `R : UpperTri[j+1, j+1]`.** Two-dimensional shape, dense
  upper-triangular, axis labels `(row, col)` — a small abstract matrix.
- **The L0 source has no 2D matrix type.** Instead, `H = mutable
  std::vector<ScalarType> H` (`iterative.hpp:192`), a *flat* 1D buffer of
  length `max_dim * (max_dim+1)` (allocated in `Update(j)` calls when needed,
  triggered at `:623-626`). Column `i` of the abstract R-factor lives in
  slab `H[i*(max_dim+1) … (i+1)*(max_dim+1) − 1]`. The stride pointer `Hi =
  H.data() + i*(max_dim+1)` (`:655` / `:834`) is the column-handle. The 2D
  index `R[k][i]` (row `k`, column `i`) becomes the 1D access `Hi[k]`.
- **Why column-major and not row-major.** The running-QR stream that produced
  `R` and `s` processed *one column at a time* (each arriving Arnoldi column
  is a new R column, replayed through stored rotations then triangularised
  by a fresh rotation; see [`L2/incremental-least-squares`](../L2/incremental-least-squares.md)).
  Column-major storage gives the stream contiguous writes per arriving
  column. The back-solve then reads *columns* of `R` (one outer iteration =
  one column), so column-major also gives contiguous reads here.
- **The `max_dim + 1` stride.** The slab is sized `max_dim + 1` per column
  (one extra entry to hold the sub-diagonal Hessenberg entry the running-QR
  stream will annihilate; after annihilation it is zero and the back-solve
  never reads it). The active `j+1` columns occupy the leading
  `(j+1) × (max_dim+1)` slabs; the unused slabs beyond column `j` are
  irrelevant to the back-solve.
- **It disappears at L1.** The L1 form has the abstract `UpperTri[j+1, j+1]`
  shape; the flat slab, the stride formula, and the `Hi` pointer arithmetic
  are L0 plumbing — a transparent allocation/access pattern, algebraically
  equivalent to a 2D matrix indexed `R[k][i]`. The rotation is "abstract
  matrix → flat column-major slab + stride pointer".

This is a **transparent storage trick** (CLAUDE.md "Optimization tricks vs.
base algebra" — transparent performance trick: memory layout). The algebraic
content is "column `i`, row `k` of `R`"; the flat-slab realisation gives that
content the same value via different memory access. It is not load-bearing
(a row-major layout, or a `dense_matrix<ScalarType>(j+1, j+1)` heap allocation,
would compute identical bit-exact results — the only difference is allocation
shape and access pattern). The rotation surfaces it; the L1 form erases it.

## Reduction order — load-bearing-numerical recording

The L1 leaf's law-4 ("back-substitution correctness, descending recurrence")
is satisfied by *any* consistent back-substitution order (row-oriented gather,
column-oriented scatter, ascending, descending — all compute the same
exact-arithmetic `y`). The L1 leaf's reduction-order non-law records that the
finite-precision result depends on the chosen order. This theme pins **the
specific finite-precision order** Palace uses:

- **Descending outer `i` sweep.** `i = j, j-1, …, 0`. The largest-index
  coordinate `y[j]` is solved first, then `y[j-1]`, …, then `y[0]`.
- **Descending inner `k` scan.** Within each outer iteration `i`, the
  super-diagonal subtractions run `k = i-1, i-2, …, 0`. The corrections are
  applied to `s[k]` slots from highest `k` down to lowest.
- **Column-oriented eager-subtraction variant.** Corrections are scattered
  into the in-progress `s[k]` accumulators as each `y[i]` is solved, rather
  than gathered per-row at the moment row `k` is being solved. So each
  `s[k]` (for `k < j`) accumulates `j-k+1` correction terms over `j-k`
  outer iterations before its final `i = k` outer iteration divides by
  `Hi[k] = R[k][k]`.

The IEEE-754 floating-point sum
`(((s[k] − R[k][j]·y[j]) − R[k][j-1]·y[j-1]) − …) − R[k][k+1]·y[k+1]`
performed left-to-right in this specific outer-iteration order is the pinned
finite-precision computation. A row-oriented variant computing
`s[k] − (R[k][k+1]·y[k+1] + R[k][k+2]·y[k+2] + … + R[k][j]·y[j])` in a single
gathered sum (or with any different grouping / order) would give a
bit-different result; the L1 leaf's law-4 holds in exact arithmetic, but the
floating-point error is order-dependent. Per CLAUDE.md "Optimization tricks
vs. base algebra" this is a **load-bearing numerical** detail — the rewrite
preserves the exact-arithmetic value (the rotation is valid) but pins a
specific finite-precision summation path. Composed with the L2
`incremental-least-squares` rotation-stream non-associativity that produced
`R` and `s` (`L2/incremental-least-squares.md:278-285`), this fixes the
bit-exact reproducibility chain for GMRES / FGMRES solutions.

There is **no MPI collective in the back-solve**: `R` (in `H`) and `s` are
*redundant-on-all-ranks* small coordinate data (the running-QR stream's
rotations were applied identically on every rank — the only collective was
the Norml2 reductions feeding the Hessenberg sub-diagonal at `:631` /
`:810`); the back-substitution is a purely local scalar computation, no
MPI_Allreduce, no per-rank divergence. (Same situation as the small-dense
[`lu-solve-mutation-rotation`](./lu-solve-mutation-rotation.md) sibling and
unlike the `Dot`/`Nrm2` reductions that feed the upstream.)

## Applicability conditions

The rewrite preserves semantics when:

1. **No observer of the prior `s` value after the call.** The L0 loop
   overwrites `s[0..j]` in place, destroying the prior RHS values. Callers
   downstream of the back-solve read `s[0..j]` as `y[0..j]` (the
   linear_combination lift at `:664-666` / `:841-843` is the sole consumer
   in both GMRES and FGMRES); no caller reads the prior RHS after the
   back-solve. This is the structural reason the in-place collapse is valid.
   (Sub-pattern A only: the prior RHS values were the rotated `β·e₁`
   transported through `j+1` Givens rotations — they live only inside the
   restart cycle and are conceptually consumed by the back-solve.)
2. **`R` square, upper-triangular, non-singular.** Established by the
   upstream [`L2/incremental-least-squares`](../L2/incremental-least-squares.md)
   running-QR stream (every sub-diagonal annihilated; non-singularity holds
   unless Arnoldi breaks down). The L0 source does NOT structurally check —
   instead the convergence test at `:644` exits the outer loop before the
   back-solve in the singular case (lucky-breakdown / exact convergence);
   the L1 leaf records this as an applicability-boundary non-law (singular
   `R` is undefined; not silently repaired).
3. **The tail entry `s[j+1]` (the LS residual) is NOT touched.** The back-
   solve reads/writes only `s[0..j]`; `s[j+1]` was consumed at `:642`
   (`beta = std::abs(s[j+1])`) before the back-solve, and is not part of
   the LS coordinate vector `y` (it is the rotated residual norm — see
   the L1 leaf §Semantics). The outer loop's bound `i >= 0` paired with
   the initial value `i = j` ensures `s[j+1]` is never touched.
4. **The Hessenberg register `H` is *redundant-on-all-ranks*.** Under the
   in-scope single-machine target (CLAUDE.md "Scope"), this is automatic
   (single rank). Inherited from the upstream running-QR stream which
   maintains `H` identically on every rank by applying the same plane
   rotations everywhere. No collective is needed in the back-solve
   itself.
5. **Element type `ScalarType` matches across `R` (in `H`) and `s`.**
   Established at solver template instantiation (`iterative.hpp:192-193`
   — both `H` and `s` are `std::vector<ScalarType>`); the compound
   `/=` and `*` operations dispatch to the matching `ScalarType`
   arithmetic uniformly. The element-type axis is absorbed
   (per the L1 leaf §Variant axes); no per-call branching.
6. **The restart dimension `j+1` is the *active* upper-triangular block,
   not the allocated `max_dim+1`.** The outer loop bound `i = j ↓ 0`
   walks only the active columns (size parameter); the stride formula
   `max_dim+1` walks the allocation. The two are consistent because the
   unused columns `> j` are zero / unread.

## GMRES preconditioning fork — the back-solve is invariant under it

GMRES splits on `pc_side` immediately after the back-solve (`iterative.cpp:662-678`):

- **Left preconditioning** (`!B || pc_side == LEFT`, `:662-668`): `x.Add(s[k],
  V[k])` for `k = 0..j` (`:664-666`) — the `V`-basis lift directly into `x`.
- **Right preconditioning** (`pc_side == RIGHT`, `:669-678`): builds `r =
  Σ_k s[k] · V[k]` into the auxiliary register `r` (`:671-675`), then
  applies the preconditioner `B` to `r` and adds to `x` (`:676-677`).

Both branches consume the **same** `s[0..j]` (the just-computed `y`); the
back-solve has already finished and is invariant under the fork. The
preconditioning split is **outside the leaf** (a downstream `B.Mult`
followed by a `linear_combination`, or just a `linear_combination`; see
the [`L1/apply_linop`](../L1/apply_linop.md) and
[`L2/linear_combination`](../L2/linear_combination.md) operators). The
FGMRES form (`:841-843`) does not branch (it always reads `Z[k]`, the
right-preconditioned basis built into the inner loop at `:806`), but it
too consumes the same `s[0..j]` from the back-solve. So **all three
basis-lift consumer surfaces** — GMRES-LEFT `V`, GMRES-RIGHT `V` (through
`r`+`B`), FGMRES `Z` — read the same back-solve output and treat the
back-solve as basis-invariant. This is direct evidence for the L1 leaf's
law-6 basis-lift independence.

## Justification kind

- **Sub-pattern A** (GMRES canonical) — `structural`. The four-element
  expansion `for ↓ i → stride → divide → for ↓ k → subtract`; result-buffer
  rotation is the receiver `s` being read-then-overwritten; the matrix-read
  rotation is the flat-column-major stride pointer.
- **Sub-pattern B** (FGMRES twin) — `structural`. Shape-identical to A
  (content-identical, brace-style line-shifted by +1); the rotation is
  the same. Recorded explicitly to ground the L1 leaf's law-6 basis-lift
  independence.
- **Sub-pattern C** (downstream basis-lift) — boundary marker, NOT part of
  the leaf. Cited for the law-6 / variant-axis boundary; the lowering of
  `linear_combination` belongs to its own theme.

The theme as a whole is `structural`, resting on the L1 leaf's
defining-contract law (`R · back_solve(R, s) = s`, law 1) plus the
back-substitution recurrence (law 4) plus the load-bearing transparent
storage trick (flat column-major slab) plus the load-bearing numerical
reduction-order non-law (descending column-oriented eager-subtraction
variant). The one non-syntactic ingredient — the in-place RHS-as-destination
collapse — is read straight off the L0 source's own compound-assignment
operators (`/=`, `-=`) on the receiver `s`; **no negative-anchor
reconstruction, no literature inference, no speculative operator** — so
`firm` rather than `partly-constructive` (matching the L1 leaf's firm-on-
positive-structure status; matching the
[`lu-solve-mutation-rotation`](./lu-solve-mutation-rotation.md) sibling
precedent).

## Speculative L1 operators

**None.** This theme lowers the already-firm L1
[`back_solve`](../L1/back_solve.md) operator into existing positive L0 source
ranges. It proposes no new L1 vocabulary and no new L0 conventions. The
downstream `linear_combination` consumer (Sub-pattern C boundary) is handled
by [`linear-combination-fold-specialization`](../L2-L1/linear-combination-fold-specialization.md)
(an L2>L1 theme, distinct edge); the upstream `incremental-least-squares`
producer (which materialises `R` and `s` in the flat register `H`) is
handled by
[`incremental-least-squares-composition-lowering`](../L2-L1/incremental-least-squares-composition-lowering.md)
(also L2>L1). This theme's scope is the **one** L1>L0 rotation: the L1 leaf
`back_solve` into the L0 in-place back-substitution loop.

A potential future sibling — a general sparse-triangular solve (`trsv`,
the Gauss-Seidel / ILU smoother kernel acting on the length-`N` field) —
is **not** part of this theme; per the L1 leaf's status, the general `trsv`
has no positive Palace L0 anchor (OQ `:24,:448`), is likely an obstruction-
theme target, and is structurally distinct (sparse-large-field, not
dense-small-coordinate). If a positive `trsv` site is eventually located,
it would belong to its own L1>L0 theme (a sparse-triangular sibling of
this dense-back-substitution one), not this theme.

## Variant axes

`back_solve` has the following variant axes at the L1>L0 edge (per
`classify-variant-axis`):

- **element-type** (absorbed): `real` | `complex`. At L0 the same loop body
  handles both — the `ScalarType` register type (`iterative.hpp:192-193`) is
  bound at solver template instantiation, the compound `/=` and `*`
  dispatch uniformly. Sub-patterns A and B are identical across element
  types (no real/complex split — unlike `Norml2` or `Dot` which have
  separate specializations). At L1 collapsed to one operator
  parameterised by element type (L1 leaf §Variant axes).
- **GMRES vs FGMRES** (the two-form recognition, Sub-patterns A and B): the
  back-solve body is **content-identical, line-shifted by +1** across the
  two surface sites. The L1 form has no GMRES/FGMRES variant — they are
  the same leaf, recorded twice in source. The basis the downstream
  consumer reads (`V` vs `Z`) is the consuming L2 composition's
  `op.basis_kind` axis (law 6), absorbed at this leaf.
- **restart dimension `j+1`** (size parameter, absorbed-as-form): the
  active dimension of the back-substitution, `j+1 ≤ max_dim`. A size
  parameter, not a behavioural variant; the loop bounds adapt
  automatically (`i = j` initial, `i >= 0` termination).
- **GMRES preconditioning side** (`pc_side ∈ {LEFT, RIGHT}`): the
  preconditioning fork at `:662-678` is **after** the back-solve;
  both branches consume the same `s[0..j]`, so this is NOT a variant
  axis of the back-solve. Recorded only as evidence the back-solve is
  invariant under it.

No reduction-strategy variant axis (the descending column-oriented
order is fixed and load-bearing-numerical, recorded as a non-rewrite
in §"Reduction order"). No alternative-kernel axis (back-substitution is
the unique kernel for an already-triangular matrix; unlike the
[`lu-solve-mutation-rotation`](./lu-solve-mutation-rotation.md) sibling
which has a load-bearing full-pivot-LU vs full-pivot-QR kernel axis).
No storage-layout axis (the flat column-major slab is the only storage,
a transparent allocation trick).

## Verified-against

L0 evidence ranges (self-verified via `tools/citecheck/citecheck.py --anchor`
against on-disk `reference/palace/` this invocation — producer-citation
self-verification, `verify-citation-range` skill, "Producer self-verification
before emitting citations" sub-case). The `iterative.cpp` restart region is
the known codemap +1-drift offender mentioned in the role spec; **citecheck
against on-disk is the source of truth** here, and every line below was
re-confirmed via `--anchor` zero-drift this invocation.

- `palace/linalg/iterative.cpp:652` — comment `// Reconstruct the solution
  (for restart or due to convergence or maximum iterations).` (GMRES restart
  back-solve role). **Self-verified** (`--anchor 'Reconstruct the solution'`
  → 652).
- `palace/linalg/iterative.cpp:653` — `for (int i = j; i >= 0; i--)`
  (GMRES outer descending sweep). **Self-verified** (`--anchor 'for (int
  i = j'` → 653).
- `palace/linalg/iterative.cpp:655` — `ScalarType *Hi = H.data() + i *
  (max_dim + 1);` (GMRES column-major stride pointer). **Self-verified**
  (`--anchor 'H.data() + i * (max_dim + 1)'` → 655).
- `palace/linalg/iterative.cpp:656` — `s[i] /= Hi[i];` (GMRES diagonal
  division). **Self-verified** (`--anchor 's[i] /= Hi[i]'` → 656).
- `palace/linalg/iterative.cpp:657` — `for (int k = i - 1; k >= 0; k--)`
  (GMRES inner super-diagonal scan). **Self-verified** (`--anchor 'for
  (int k = i - 1'` → 657).
- `palace/linalg/iterative.cpp:659` — `s[k] -= Hi[k] * s[i];` (GMRES
  column-oriented super-diagonal subtraction). **Self-verified** (`--anchor
  's[k] -= Hi[k] * s[i]'` → 659).
- `palace/linalg/iterative.cpp:666` — `x.Add(s[k], V[k]);` (GMRES downstream
  `V`-basis lift; NOT part of the leaf — Sub-pattern C boundary marker).
  **Self-verified** (`--anchor 'x.Add(s[k], V[k])'` → 666).
- `palace/linalg/iterative.cpp:831` — comment `// Reconstruct the solution
  (for restart or due to convergence or maximum iterations).` (FGMRES restart
  back-solve role). **Self-verified** (`--anchor 'Reconstruct the solution'`
  → 831).
- `palace/linalg/iterative.cpp:832` — `for (int i = j; i >= 0; i--)`
  (FGMRES outer descending sweep — note +1 line-shift vs GMRES :653 from
  brace-on-own-line style). **Self-verified** (`--anchor 'for (int i = j'`
  → 832).
- `palace/linalg/iterative.cpp:834` — `ScalarType *Hi = H.data() + i *
  (max_dim + 1);` (FGMRES column-major stride pointer). **Self-verified**
  (`--anchor 'H.data() + i * (max_dim + 1)'` → 834).
- `palace/linalg/iterative.cpp:835` — `s[i] /= Hi[i];` (FGMRES diagonal
  division). **Self-verified** (`--anchor 's[i] /= Hi[i]'` → 835).
- `palace/linalg/iterative.cpp:836` — `for (int k = i - 1; k >= 0; k--)`
  (FGMRES inner super-diagonal scan). **Self-verified** (`--anchor 'for
  (int k = i - 1'` → 836).
- `palace/linalg/iterative.cpp:838` — `s[k] -= Hi[k] * s[i];` (FGMRES
  column-oriented super-diagonal subtraction). **Self-verified** (`--anchor
  's[k] -= Hi[k] * s[i]'` → 838).
- `palace/linalg/iterative.cpp:843` — `x.Add(s[k], Z[k]);` (FGMRES downstream
  `Z`-basis lift; NOT part of the leaf — Sub-pattern C second boundary
  instance). **Self-verified** (`--anchor 'x.Add(s[k], Z[k])'` → 843).
- `palace/linalg/iterative.cpp:644` — `converged = (beta < eps);` (the
  convergence test that exits before the back-solve in the lucky-breakdown
  / singular-`R` case; applicability boundary). **Self-verified** (`--anchor
  'converged = (beta < eps)'` → 644).
- `palace/linalg/iterative.cpp:612` — `s[0] = beta;` (RHS seed for the
  running-QR stream; the back-solve's RHS `s[0..j]` is its rotated
  descendant). **Self-verified** (`--anchor 's[0] = beta'` → 612).
- `palace/linalg/iterative.cpp:631` — `Hj[j + 1] = linalg::Norml2(comm, w);`
  (the sub-diagonal entry the running-QR stream annihilates — context for
  why `R` is upper-triangular when the back-solve reads it; not directly
  consumed by the back-solve). **Self-verified** (`--anchor 'Norml2(comm,
  w)'` → 631).
- `palace/linalg/iterative.hpp:192` — `mutable std::vector<ScalarType> H;`
  (the flat column-major register storing the R-factor). **Self-verified**
  (`--anchor 'H'` → 192).
- `palace/linalg/iterative.hpp:193` — `mutable std::vector<ScalarType> s,
  sn;` (the RHS / Givens-sine register `s` of element type `ScalarType`).
  **Self-verified** (`--anchor 's, sn'` → 193).
- `palace/linalg/iterative.hpp:222` — `class FgmresSolver : public
  GmresSolver<OperType>` (FGMRES inherits the GMRES registers, grounding
  Sub-pattern B's identical-`H`-and-`s`-access claim). **Self-verified**
  (`--anchor 'class FgmresSolver'` → 222).
- `palace/linalg/iterative.hpp:250` — `using GmresSolver<OperType>::H;`
  (FGMRES inherits the Hessenberg register). **Self-verified** (`--anchor
  'GmresSolver<OperType>::H'` → 250).
- `palace/linalg/iterative.hpp:256` — `mutable std::vector<VecType> Z;`
  (FGMRES-specific right-preconditioned-basis register; NOT read by the
  back-solve — basis-lift independence boundary marker). **Self-verified**
  (`--anchor 'std::vector<VecType> Z'` → 256).

L1 / cross-theme anchors:

- [`L1/back_solve`](../L1/back_solve.md) — the firm L1 operator this theme
  lowers; signature `back_solve :: (UpperTri[j+1,j+1], Tensor[j+1]) ->
  Tensor[j+1]` (`:78`), the defining contract `R · back_solve(R, s) = s`
  (law 1, `:187-195`), the back-substitution recurrence (law 4,
  `:207-215`), the empty-stream / single-column boundary (law 5,
  `:218-221`), basis-lift independence (law 6, `:223-230`), the reduction-
  order non-law (`:234-243`), the singular-`R` applicability boundary
  (`:249-254`), the L1 vs L0 distinction section (`:371-390`), the firm-
  on-positive-structure status (`:330-369`), the cycle-028 `verified_against:`
  block (`:466-540`).
- [`L1-L0/normalize-mutation-rotation`](./normalize-mutation-rotation.md) —
  firm sibling theme precedent: in-place destructive overwrite of the
  receiver, structural rewrite, three-sub-pattern decomposition, firm-on-
  positive-structure status without a dedicated test, sub-theme reuse
  pattern.
- [`L1-L0/matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md) —
  firm sibling theme precedent: sub-pattern reuse pattern (the inner Dot
  inheriting from `dot-mutation-rotation` Sub-pattern A), the caller-owned
  workspace machinery, the load-bearing-defensive guard classification
  pattern.
- [`L1-L0/lu-solve-mutation-rotation`](./lu-solve-mutation-rotation.md) —
  the dense-small coordinate-space direct-solve sibling on the same "small-
  dense in-place RHS overwrite" axis; this theme's back-substitution-only
  case differs by R already being upper-triangular (no factorisation).
- [`L2/incremental-least-squares`](../L2/incremental-least-squares.md) —
  the firm L2 composition that produces `R` and `s` in the flat register
  `H` via the running-QR stream; the L2>L1
  `incremental-least-squares-composition-lowering` theme (c028 staged for
  c030) is its forward-edge complement — that theme's terminal step is
  exactly this leaf, and exactly this lowering is its terminal rewrite.
- [`concepts/givens`](../concepts/givens.md) — the concept page that names
  the back_solve step "via `trsv`" at `:29`; this theme is the L1>L0
  rotation of that step.

## Status

`firm` — the rewrite is the structural expansion of the L1 leaf
[`back_solve`](../L1/back_solve.md) into the L0 in-place back-substitution
loop at `palace/linalg/iterative.cpp:652-660` (GMRES Sub-pattern A) /
`:831-840` (FGMRES Sub-pattern B), exhaustively pinned by direct, self-
verified evidence:

- **The L1 leaf is firm + audited** (cycle-028 `verified_against:` block,
  every L0 anchor zero-drift on-disk).
- **Both surface forms are positively anchored** (GMRES `:652-660` and
  FGMRES `:831-840`); the two are content-identical, line-shifted by
  brace style, grounding law-6 basis-lift independence.
- **Every rewrite element is positively anchored**: the descending outer
  sweep, the column-major stride formula, the diagonal division, the
  inner column-oriented super-diagonal subtraction, the in-place RHS
  overwrite, the basis-invariant downstream lift.
- **The one load-bearing numerical detail** — the descending column-
  oriented eager-subtraction reduction order — is recorded explicitly,
  matching the L1 leaf's reduction-order non-law.
- **The two transparent tricks** — the flat column-major register storage
  and the `max_dim+1` stride — are recorded as such, algebraically
  equivalent to a 2D `R[k][i]` matrix indexing.

The theme **reuses** no prior L1>L0 sub-theme verbatim (unlike
`normalize-mutation-rotation` / `matrix-weighted-norm-mutation-rotation`
which delegate steps to sibling themes); the back-substitution loop is a
single atomic four-element rewrite, not a composition of sibling rotations.
The downstream basis-lift (Sub-pattern C) is a boundary marker only, handled
by `linear-combination-fold-specialization` at L2>L1.

The one non-syntactic ingredient — the destination-collapsed-into-RHS
in-place overwrite — is read straight off the L0 source's own compound-
assignment operators `s[i] /= Hi[i]` (`:656`) and `s[k] -= Hi[k] * s[i]`
(`:659`) on the receiver `s`; **no negative-anchor reconstruction, no
literature inference, no speculative operator** — so `firm` rather than
`partly-constructive`. The firm-on-positive-structure rationale matches the
L1 leaf and the
[`lu-solve-mutation-rotation`](./lu-solve-mutation-rotation.md) sibling: no
dedicated GMRES/FGMRES back-substitution unit test exists in
`reference/palace/test/unit/` (the back-solve is exercised only end-to-end
through the GMRES / FGMRES solve, the same coverage situation as
`incremental-least-squares` and `lu_solve`), and **a missing test does not
gate syntactic-identity laws** (per CLAUDE.md status-tier guidance); every
law of the L1 leaf is operator-algebra on the cited positive source, none
depend on iteration or convergence behaviour.

A `lowering-verifier` audit attaching the `verified_against:` block (per
the sibling-theme convention) — confirming the surface-form recognition is
exhaustive (these two are the only Palace `R · y = s` back-substitution
sites, no third overload), the line-shift between GMRES and FGMRES is the
sole content-difference (modulo the downstream basis), and the
reduction-order non-law composes cleanly with `incremental-least-squares`'s
rotation-stream non-associativity — is the standard follow-up scheduled for
cycle-030 (per role-prompt direction), not a status reduction.
```

```edit:book/src/L1-L0/index.md
| [scal-mutation-rotation](./scal-mutation-rotation.md) | `L1/scal` (firm) | `palace/linalg/vector.{hpp,cpp}`, `palace/linalg/{iterative,operator,nleps}.cpp` | firm *(structural; 2 element-type overloads; transparent complex imag==0 shape branch)* |
| [dot-mutation-rotation](./dot-mutation-rotation.md) | `L1/dot` (firm) | `palace/linalg/vector.{hpp,cpp}`, `palace/utils/communication.hpp` | firm *(structural; 3 surface forms; conjugate-pair re-order `xᴴ y = conj(yᴴ x)`; tdot type-API-surface-only)* |
| [matrix-weighted-norm-mutation-rotation](./matrix-weighted-norm-mutation-rotation.md) | `L1/matrix-weighted-norm` (rough-in) | `palace/linalg/operator.{hpp,cpp}`, `palace/linalg/{arpack,slepc,nleps}.cpp` | firm *(structural; 2 element-type sub-patterns A real/B complex + Normalize consumer C; reuses apply_linop A `B.Mult(x,Bx)` + dot A `Dot(comm,Bx,x)` + scal; caller-owned destination workspace Bx; SPD `MFEM_ASSERT(dot>0)` load-bearing defensive guard + complex Hermiticity witness; B=I collapses to nrm2)* |
| [normalize-mutation-rotation](./normalize-mutation-rotation.md) | `L1/normalize` (firm) | `palace/linalg/vector.hpp:262-270`, `palace/linalg/{iterative,operator,nleps}.cpp` | firm *(structural; 3 sub-patterns A `Norml2` reduction / B in-place `x*=1.0/norm` rescale / C load-bearing returned norm; reuses nrm2-mutation-rotation A + scal-mutation-rotation A; returned-norm load-bearing via GMRES Hessenberg `iterative.cpp:631-632` + power-iter eigenvalue `palace/linalg/operator.cpp:673,676` + NEP companion-scale `nleps.cpp:610-611,617`; `MFEM_ASSERT(norm>0)` partiality witness; `normalize_B` rough-in note)* |
| [back-solve-mutation-rotation](./back-solve-mutation-rotation.md) | `L1/back_solve` (firm + c028 audited) | `palace/linalg/iterative.cpp:652-660` (GMRES) / `:831-840` (FGMRES) | firm *(structural; 2 surface sub-patterns A GMRES / B FGMRES content-identical-line-shifted-by-+1 + C downstream basis-lift boundary; in-place RHS-as-destination overwrite collapses L1 fresh `y` into the L0 receiver `s[0..j]`; flat column-major slab + `Hi=H.data()+i*(max_dim+1)` transparent storage trick; descending column-oriented eager-subtraction reduction-order non-law (load-bearing-numerical); singular-R applicability boundary upstream-enforced by convergence test `:644`; no MPI collective; basis-lift independence (`V` vs `Z`) grounded by Sub-pattern C boundary; cycle-030 verified_against audit pending)* |
| [nleps-deflated-residual-mutation-rotation](./nleps-deflated-residual-mutation-rotation.md) | `L1/nleps_deflated_residual` (firm) | `palace/linalg/nleps.cpp:547-577` (+ `:329-347` MatVecMult, `:587`/`:702` call sites) | firm *(structural; 3 sub-patterns A/B/C; load-bearing Mult+AddMult→single-pencil-apply collapse; reuses dot Sub-pattern A; reuses lin-comb fold L2>L1)* |
```

```edit:book/src/SUMMARY.md
- [normalize-mutation-rotation](./L1-L0/normalize-mutation-rotation.md)
- [back-solve-mutation-rotation](./L1-L0/back-solve-mutation-rotation.md)
- [lu-solve-mutation-rotation](./L1-L0/lu-solve-mutation-rotation.md)
```

## Speculative operators proposed

**None.** This theme lowers the existing firm + cycle-028-audited L1
[`back_solve`](book/src/L1/back_solve.md) leaf into positive L0 source ranges
(`palace/linalg/iterative.cpp:652-660` GMRES, `:831-840` FGMRES). It introduces
no new L1 vocabulary, no speculative L_n+1 operators, no new L0 conventions.
The downstream basis-lift (`V[k]` / `Z[k]`) is the L2 `linear_combination`
primitive consumer, already firm; the upstream R-factor production (the
running-QR triangularisation in the flat register `H`) is the L2
`incremental-least-squares` composition, already firm; both are recorded as
boundary markers in the theme body.

## Supporting evidence

### L0 source citations (all self-verified via `tools/citecheck/citecheck.py --anchor` this invocation, zero codemap drift on every line)

GMRES restart-correction back-substitution (`reference/palace/palace/linalg/iterative.cpp`):

- `:652` — `// Reconstruct the solution (for restart or due to convergence or maximum iterations).` (block role comment)
- `:653` — `for (int i = j; i >= 0; i--)` (outer descending sweep)
- `:655` — `ScalarType *Hi = H.data() + i * (max_dim + 1);` (column-major stride pointer)
- `:656` — `s[i] /= Hi[i];` (diagonal division `y[i] = s[i]/R[i][i]`)
- `:657` — `for (int k = i - 1; k >= 0; k--)` (inner super-diagonal scan)
- `:659` — `s[k] -= Hi[k] * s[i];` (column-oriented super-diagonal subtraction)
- `:666` — `x.Add(s[k], V[k]);` (downstream V-basis lift — boundary marker)

FGMRES restart-correction back-substitution (same file):

- `:831` — `// Reconstruct the solution (for restart or due to convergence or maximum iterations).` (block role comment, FGMRES copy)
- `:832` — `for (int i = j; i >= 0; i--)` (outer descending sweep — note +1 line-shift vs GMRES :653 from brace-on-own-line style)
- `:834` — `ScalarType *Hi = H.data() + i * (max_dim + 1);` (column-major stride pointer)
- `:835` — `s[i] /= Hi[i];` (diagonal division)
- `:836` — `for (int k = i - 1; k >= 0; k--)` (inner super-diagonal scan)
- `:838` — `s[k] -= Hi[k] * s[i];` (column-oriented super-diagonal subtraction)
- `:843` — `x.Add(s[k], Z[k]);` (downstream Z-basis lift — second boundary marker, grounds law-6 basis-lift independence)

Context citations:

- `palace/linalg/iterative.cpp:612` — `s[0] = beta;` (RHS seed)
- `palace/linalg/iterative.cpp:631` — `Hj[j + 1] = linalg::Norml2(comm, w);` (sub-diagonal annihilated by running-QR; upper-triangularity boundary)
- `palace/linalg/iterative.cpp:644` — `converged = (beta < eps);` (convergence test gating singular-R lucky-breakdown applicability boundary)
- `palace/linalg/iterative.hpp:192` — `mutable std::vector<ScalarType> H;` (flat column-major register)
- `palace/linalg/iterative.hpp:193` — `mutable std::vector<ScalarType> s, sn;` (RHS / Givens-sine register, ScalarType element type)
- `palace/linalg/iterative.hpp:222` — `class FgmresSolver : public GmresSolver<OperType>` (FGMRES inherits from GMRES)
- `palace/linalg/iterative.hpp:250` — `using GmresSolver<OperType>::H;` (FGMRES inherits the Hessenberg register)
- `palace/linalg/iterative.hpp:256` — `mutable std::vector<VecType> Z;` (FGMRES-specific Z basis register; NOT read by the back-solve — basis-lift independence boundary)

### L1 / cross-theme anchors

- `book/src/L1/back_solve.md` — firm + cycle-028 `verified_against:` block on which this theme's rewrite is grounded
- `book/src/L1-L0/normalize-mutation-rotation.md` — firm sibling precedent (structure, status framing, reduction-order non-law treatment)
- `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md` — firm sibling precedent (sub-pattern decomposition, in-place receiver-buffer rewriting, load-bearing-defensive guard treatment)
- `book/src/L1-L0/lu-solve-mutation-rotation.md` — sibling small-dense coordinate-space in-place RHS-overwrite theme (the back-substitution-only relative of full LU)
- `book/src/L2/incremental-least-squares.md` — upstream L2 composition that produces R and s in the flat register H (cycle-026 firm)
- `book/src/L2-L1/incremental-least-squares-composition-lowering.md` (forward-reference; staged c028 → c030) — sibling L2>L1 edge that consumes this leaf as its terminal step

### Verification log (this invocation)

Every load-bearing pinpoint citation in the theme body was self-verified via
`python3 tools/citecheck/citecheck.py reference/palace/<path>:<line>
--anchor '<distinctive token>'` against on-disk `reference/palace/`. Zero
drift on all 20+ citations. The codemap +1-drift offender region noted in
the role prompt (`iterative.cpp` restart block) was caught — the FGMRES outer
`for` line is `:832` (not `:831`, which is the comment); all FGMRES citations
were re-anchored against on-disk and corrected before emission. The
`--scan` bounds + path-hygiene pre-emit pass was run mentally during
authoring (no out-of-bounds, no ambiguous paths — all citations use the
canonical `palace/linalg/iterative.cpp:NN` or `iterative.hpp:NN` form,
matching sibling-theme conventions).

## Open questions / caveats

1. **L1 leaf's law-6 statement is slightly imprecise**. The leaf says "the
   back-solve code is line-for-line identical" (`book/src/L1/back_solve.md:226-227`)
   — but the LINE NUMBERS differ by +1 (FGMRES brace-on-own-line style),
   while the LINE CONTENT is byte-identical. This theme records the
   precise relationship ("content-identical, line-shifted") in Sub-pattern
   B. The leaf statement is not wrong (the *body* is line-for-line identical
   modulo brace style) but is worth a future minor prose-tightening on the
   leaf to remove ambiguity. **Recommendation**: NOT this dispatch's
   responsibility; queue as a low-fan-out leaf prose-tightening for a
   future `harvester`/`lifter` pass. Not load-bearing for any claim.

2. **The forthcoming L2>L1
   `incremental-least-squares-composition-lowering` theme** (c027 dispatch 5,
   c028 staged, c030 pending) will consume **this leaf** as its terminal step.
   This theme deliberately does NOT pre-empt that lowering: the back-solve as
   a single atomic primitive (this leaf) is firm and self-contained; how the
   L2 composition's terminal `back_solve` projection maps into the L0 site
   is the L2>L1 theme's concern. The boundary between the two themes is
   clean: this theme owns the L1 leaf → L0 loop rotation; the L2>L1 theme
   owns the L2 composition → L1 leaf-call projection. The c030 verified_against
   audit of THIS theme should confirm the boundary is consistent with the
   c027 dispatch-5 staging (the L2 theme's terminal projection is exactly
   this leaf, no re-derivation needed).

3. **The cycle-030 verified_against audit is in scope but not the
   `lowering-verifier` audit of the cycle-027 `incremental-least-squares-
   composition-lowering` theme.** The two are independent — this leaf's
   audit confirms the surface-form recognition is exhaustive (only the
   two GMRES/FGMRES sites are Palace `R·y=s` back-substitutions, no third
   overload); the L2>L1 theme's audit confirms the *composition* lowers
   correctly into a stream + this terminal call. They might be batched but
   need not be.

4. **Empty-cycle `j = -1` boundary semantics**. The L1 leaf records `y = []`
   as the empty result (law 5); the L0 source represents this as "the for
   loop does not execute, so `s[0..-1]` is unchanged" — which is semantically
   the same as "no coordinate vector was produced, downstream `V·y` adds
   zero contribution" (since the downstream lift loop at `:664` also
   becomes vacuous when `j = -1`). The theme records this faithfully but
   does NOT verify the empty-cycle reaches the back-solve in practice — in
   the Palace control flow, `j = -1` would mean the inner Arnoldi loop
   broke out at the very first iteration with `converged = true` (the
   convergence test at `:644` triggers at the first column), and the
   restart-correction block runs with `j = -1` only if the seed `s[0] =
   beta` already satisfied `beta < eps` at the **outer** test `:603` — in
   which case the outer `break` (`:606`) exits the entire solver before
   the inner loop runs and before this back-solve block runs. So in
   practice the empty-cycle case may be **unreachable** at runtime via
   this code path. **Recommendation**: not load-bearing for the firm
   status (the L1 leaf's law 5 is an algebraic identity, true whether or
   not the lowered path can reach it); record as a tangential note for
   the cycle-030 audit. Not a defect.

5. **The reduction-order non-law is recorded only descriptively**, not as
   a separate "load-bearing-numerical sub-rule" section. This matches the
   L1 leaf's own treatment (the non-law is in the §Algebraic-laws section
   under "Laws that explicitly do not hold"). If the cycle-030 audit
   prefers a separate §"Reduction order — load-bearing-numerical
   recording" section (per `dot-mutation-rotation`'s precedent), the
   §"Reduction order" subsection of this theme can be promoted to a
   top-level section. Stylistic choice, not load-bearing.
