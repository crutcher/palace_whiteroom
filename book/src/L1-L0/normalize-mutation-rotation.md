# normalize-mutation-rotation

The mutation rotation for the fused BLAS-1 vector normalisation. Lowers the pure
L1 form `normalize(x) = (β, x/β)` with `β = nrm2(x)` ([`L1/normalize`](../L1/normalize.md),
firm) into Palace's L0 free-function template `linalg::Normalize(comm, x)`
(`palace/linalg/vector.hpp:262-270`): a four-step composition
`norm = Norml2(comm, x); MFEM_ASSERT(norm > 0.0, ...); x *= 1.0 / norm; return norm`.
It is the **fused pairing** of two sibling themes: the `Norml2` reduction is
[`nrm2-mutation-rotation`](./nrm2-mutation-rotation.md) (the no-buffer
`sqrt∘abs∘Dot(x,x)` chain), and the in-place `x *= 1.0/norm` rescale is
[`scal-mutation-rotation`](./scal-mutation-rotation.md) Sub-pattern A (the real-path
receiver overwrite by the runtime scalar `1.0/norm`). This theme **reuses both
sub-themes** rather than restating them — exactly as
[`matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md)
reuses apply-linop Sub-pattern A + dot Sub-pattern A. What this theme **adds** is the
machinery the fusion exists for: (1) the **load-bearing returned norm** — the value
`normalize` retains that a bare `scal(1/nrm2(x), x)` discards, consumed downstream as
the Arnoldi Hessenberg sub-diagonal, the power-iteration eigenvalue estimate, and the
NEP deflation companion-scale; and (2) the **`MFEM_ASSERT(norm > 0.0)` partiality
guard** — the one semantic addition over the total `nrm2`/`scal` leaves (classified
below).

## Slug

`normalize-mutation-rotation`

## L1 form (LHS)

The pure-functional fused normalisation (firm; see [`L1/normalize`](../L1/normalize.md))
consumes the *prior* value of `x` and produces a fresh **pair** — the recovered norm
and the unit vector — mutating nothing. There is one LHS shape (`normalize` has no
free-function variants and no constant-folding specialisations):

    (β, û) = normalize(x)        -- β = nrm2(x),  û = x/β,  β > 0

The defining identity (L1 algebraic law 6, the factorisation) is
`normalize(x) = (nrm2(x), scal(1/nrm2(x), x))` — both components in terms of the firm
leaves [`L1/nrm2`](../L1/nrm2.md) and [`L1/scal`](../L1/scal.md). The element-type axis
is inherited from the leaves (real / complex `x`, with the norm output **always real**);
no new variant axis is introduced by the fusion. The L1 form carries **no destination
buffer** — the prior `x`, the unit vector `û`, and the scalar `β` are three distinct
values; the lowering below is where the in-place receiver overwrite is reintroduced.

`normalize` is **partial**: undefined at `x = 0` (`β = 0`, division by zero). This is the
single semantic addition of the fusion over its (total) `nrm2` / `scal` constituents, and
it is the precondition the L0 `MFEM_ASSERT` enforces.

## L0 form (RHS)

The L1 pair lowers into the free-function template `linalg::Normalize(comm, x)`
(`palace/linalg/vector.hpp:262-270`). The receiver `x` is **overwritten in place** with
the unit vector, and the norm is **returned by value**:

    template <typename VecType>
    inline auto Normalize(MPI_Comm comm, VecType &x)
    {
      auto norm = Norml2(comm, x);                             // vector.hpp:266 — step A (reduction)
      MFEM_ASSERT(norm > 0.0, "Zero vector norm ...");          // vector.hpp:267 — guard (partiality)
      x *= 1.0 / norm;                                          // vector.hpp:268 — step B (in-place rescale)
      return norm;                                              // vector.hpp:269 — step C (returned norm)
    }

The four steps the L1 pair hides, evaluated in order:

### Sub-pattern A — the `Norml2` reduction (inherited from `nrm2-mutation-rotation`)

    auto norm = Norml2(comm, x);                               // vector.hpp:266

The norm component `β` is computed by the free-function template `Norml2(comm, x)` —
which is itself the four-stage chain `std::sqrt(std::abs(Dot(comm, x, x)))`
(`vector.hpp:259`). This is **exactly** [`nrm2-mutation-rotation`](./nrm2-mutation-rotation.md)
Sub-pattern A (the canonical free-function form): the no-destination-buffer reduction
into a stack scalar, the inner Hermitian self-`Dot`, the reintroduced `MPI_Allreduce`
(single-rank no-op, structurally present per CLAUDE.md "Scope"), the load-bearing
`std::abs` non-negativity guard (classified load-bearing-defensive there), and the outer
`std::sqrt`. This theme **inherits** that sub-theme wholesale — the reduction-tree
non-associativity, the surface-form recognition, and the `std::abs` classification are
all recorded there, not restated. The single difference is **binding**: in `Normalize`
the reduction result is bound to a local `norm` that is *both* the rescale divisor
(step B) *and* the returned value (step C), rather than discarded.

Justification kind: **structural** (inherited reduction expansion).

Citations:
- `palace/linalg/vector.hpp:266` — `auto norm = Norml2(comm, x);` (the reduction binding).
- `palace/linalg/vector.hpp:259` — `Norml2` body `std::sqrt(std::abs(Dot(comm, x, x)))`
  (the chain `nrm2-mutation-rotation` Sub-pattern A expands). [inherited — see Verified-against]

### Sub-pattern B — the in-place rescale (inherited from `scal-mutation-rotation` Sub-pattern A)

    x *= 1.0 / norm;                                          // vector.hpp:268

The unit-vector component `û = x/β` is materialised by the in-place receiver overwrite
`x *= 1.0 / norm` — the reciprocal-then-multiply form. This is **exactly**
[`scal-mutation-rotation`](./scal-mutation-rotation.md) **Sub-pattern A** (bare in-place
rescale, real path): the L1 value `scal(1/β, x)` binds to the L0 receiver buffer `x`, the
runtime scalar is `1.0/norm`. That theme already names *this very site* as one of its two
Sub-pattern A instances (`scal-mutation-rotation.md:48-49,55-58`: "inside `linalg::Normalize`
(`x *= 1.0 / norm;`)"). This theme **inherits** the sub-theme — the receiver-buffer
re-bind, the element-local no-aliasing-hazard (`x[i]` depends only on `x[i]`), and the
complex-path `imag(s) == 0.0` shape-specialisation (Sub-pattern B there) are all recorded
there. The **reciprocal-vs-divide** choice (`x *= 1.0/norm` rather than a per-element
`x[i] /= norm`) is a **transparent trick** (an IEEE-754 bit-difference; the algebraic
value `x/β` is identical) — matching the L1 entry's note that "any reciprocal-vs-divide
bit-difference is an L1>L0 transparent-trick note" (`book/src/L1/normalize.md:32`).

Justification kind: **structural** (inherited receiver-buffer re-bind), with the
reciprocal form as a transparent-trick sub-note.

Citations:
- `palace/linalg/vector.hpp:268` — `x *= 1.0 / norm;` (the in-place rescale; `scal`
  Sub-pattern A real path). [inherited — see Verified-against]

### Sub-pattern C — the load-bearing returned norm (the reason `normalize` is a named primitive)

    return norm;                                              // vector.hpp:269

This is the **distinguishing feature** of this theme — the half a bare composition
`scal(1/nrm2(x), x)` cannot express. The L0 `Normalize` returns `norm` by value
*after* the in-place rescale; at L1 this is `result.0`, the first component of the pair.
A bare `scal ∘ nrm2` discards the intermediate `nrm2(x)`; `normalize` retains it. The
returned scalar is **load-bearing** — three distinct downstream consumer shapes recur,
and each proves the norm is consumed *after* the rescale (so the fusion's single-evaluation
pairing is the natural unit):

1. **Hessenberg sub-diagonal + rescale divisor (GMRES Arnoldi)** — the norm is captured
   into a separate structure (the Hessenberg matrix) *and* used to normalise. Palace
   writes the inline (un-fused) form, consuming **both** outputs of `normalize`:

       Hj[j + 1] = linalg::Norml2(comm, w);                  // iterative.cpp:631 — β → H[j+1,j]
       w *= 1.0 / Hj[j + 1];                                  // iterative.cpp:632 — w ← w/β (unit)

   The norm `β` becomes the sub-diagonal entry `H[j+1,j]` of the Arnoldi/Hessenberg matrix
   (it feeds the Givens plane-rotation least-squares solve at `iterative.cpp:636-639`),
   the unit `w` extends the Krylov basis. This is `normalize(w)` open-coded with both
   components retained — direct evidence the returned norm is not a discardable side
   output. (A second identical GMRES code path is at `iterative.cpp:810-811`.)

2. **Dominant-eigenvalue estimate (spectral-radius power iteration)** — the norm is the
   working result and the unit vector is the carrier for the next iteration:

       l = Normalize(comm, u);                                // palace/linalg/operator.cpp:673 — l IS the eigenvalue estimate
       res = std::abs(l - l0) / l0;                           // palace/linalg/operator.cpp:676 — convergence test on l

   The returned norm `l` **is** the dominant-eigenvalue estimate consumed directly by the
   convergence test (`res = |l − l0|/l0` at `:676`); the renormalised `u` carries forward to
   the next `A·u` (`palace/linalg/operator.cpp:664`). If `Normalize` discarded its norm, this loop could
   not converge. (The seed normalise at `palace/linalg/operator.cpp:660-661`, `SetRandom(comm, u);
   Normalize(comm, u);`, discards the returned norm — the unit-vector-only consumer shape,
   the projection `snd ∘ normalize`.)

3. **Deflation companion-vector scale (NEP deflation-basis growth)** — the norm rescales a
   *companion* quantity as well as `x`, written inline (the same shape as `Normalize`):

       const auto scale = linalg::Norml2(GetComm(), v);       // nleps.cpp:610 — β
       v *= 1.0 / scale;                                      // nleps.cpp:611 — v ← v/β (unit basis vector)
       ...
       H.col(k).head(k) = v2 / scale;                         // nleps.cpp:617 — companion v2 rescaled by SAME β

   The returned norm `scale` is **doubly load-bearing**: it normalises the deflation basis
   vector `v` (`:611`) *and* rescales the coordinate companion `v2` (`:617`) so the
   invariant-pair `(v, v2)` stays consistent. The norm is reused twice after the rescale —
   it cannot be a transient. (This site uses the **unweighted** norm via inline `Norml2` +
   `*=`, the same shape as `linalg::Normalize` written out, not the B-weighted sibling.)

Justification kind: **structural** — the returned `norm` binds to `result.0`; the three
consumer shapes are the *evidence* that the binding is load-bearing (the rotation must
preserve the returned scalar, not elide it). This is the structural reason `normalize` is
a distinct named operator rather than a bare `scal ∘ nrm2` composition.

Citations (consumer evidence the returned norm is load-bearing):
- `palace/linalg/iterative.cpp:631-632` — GMRES Arnoldi: `Hj[j + 1] = linalg::Norml2(comm, w);
  w *= 1.0 / Hj[j + 1];` (β → Hessenberg sub-diagonal AND rescale divisor; both outputs consumed).
- `palace/linalg/iterative.cpp:810-811` — second analogous GMRES Arnoldi path:
  `Hj[j + 1] = linalg::Norml2(comm, w); w *= 1.0 / Hj[j + 1];` (the two-line shape; `:811` is the rescale half).
- `palace/linalg/operator.cpp:673` — `l = Normalize(comm, u);` (returned norm IS the
  dominant-eigenvalue estimate).
- `palace/linalg/operator.cpp:676` — `res = std::abs(l - l0) / l0;` (convergence test
  consuming the returned norm `l` — direct evidence it is load-bearing).
- `palace/linalg/operator.cpp:660-661` — `SetRandom(comm, u); Normalize(comm, u);` (seed
  normalise; returned norm discarded — the `snd ∘ normalize` unit-vector-only shape).
- `palace/linalg/nleps.cpp:610-611` — NEP deflation: `const auto scale = linalg::Norml2(GetComm(), v);
  v *= 1.0 / scale;` (inline unweighted normalise).
- `palace/linalg/nleps.cpp:617` — `H.col(k).head(k) = v2 / scale;` (the returned norm `scale`
  reused to rescale the coordinate companion — doubly load-bearing).

## The `MFEM_ASSERT(norm > 0.0)` partiality guard — classification

    MFEM_ASSERT(norm > 0.0, "Zero vector norm in normalization!");   // vector.hpp:267

The guard `MFEM_ASSERT(norm > 0.0, ...)` is the **partiality witness** — the one semantic
addition `normalize` carries over its total constituents. It is **distinct in kind** from the
`std::abs` guard inside the inherited `nrm2` reduction (Sub-pattern A) and the
`MFEM_ASSERT(dot > 0.0)` SPD guard in
[`matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md):

- **The inner `nrm2` `std::abs`** (`vector.hpp:259`, classified load-bearing-defensive in
  `nrm2-mutation-rotation`) repairs a round-off sign-flip on a numerically-tiny *non-negative*
  self-dot, so that `std::sqrt` does not return `NaN`. It is a no-op in exact arithmetic on a
  non-zero input. It runs **before** this guard, on `dot(x,x)`.
- **This `MFEM_ASSERT(norm > 0.0)`** runs on the *already-real-non-negative* `norm` and aborts
  on `norm == 0.0` — i.e. exactly on the **zero-vector input** `x = 0`, where `β = 0` and the
  subsequent `1.0 / norm` would divide by zero. It is the run-time enforcement of `normalize`'s
  **applicability precondition** `x ≠ 0` (`book/src/L1/normalize.md:26`).

Applying the CLAUDE.md "Optimization tricks vs. base algebra" framing:

- **In exact arithmetic it is a domain check, not a no-op.** Unlike the `nrm2` `std::abs` (which
  vanishes at L1 because `dot(x,x) ≥ 0` is an algebraic law), this assertion encodes the
  **partiality** of `normalize` — `nrm2(0) = 0` and `scal(α, 0) = 0` are both total, but the
  fused operator is undefined at `x = 0` (the divide). At L1 it is **not** subsumed by an
  algebraic law; it surfaces as the explicit applicability condition `β > 0` and the "Totality
  does not hold" law (`book/src/L1/normalize.md:54`).
- **It does not change any result on the operator's domain.** For `x ≠ 0` the assertion never
  fires; on the zero vector the L1 operator is simply undefined (no value to compare against).
  The guard is therefore the L0 realisation of the L1 domain restriction, not a load-bearing
  numerical trick that changes a computed value.

**Verdict: the L0 run-time witness of `normalize`'s partiality precondition `x ≠ 0`.** It is
not erasable without silently producing `inf`/`NaN` on a zero-vector input (the `1.0/0.0` divide).
It is positively anchored — read straight off the L0 source line `:267` — and it is the **only**
new ingredient the fusion adds over re-using the `nrm2` + `scal` sub-themes.

## Applicability conditions

The rewrite preserves semantics when:

1. **No observer of the prior `x` value after the call.** The L0 `x *= 1.0/norm`
   overwrites the receiver in place, destroying the prior value. The L1 `x` (the input
   to `normalize`) is read **strictly before** the rescale — `Norml2(comm, x)` (step A)
   reads the prior `x` to compute `β`, *then* the rescale (step B) overwrites it. This
   read-before-write sequencing is the structural reason the fusion is valid: the prior
   `x` is fully consumed by the reduction before the in-place rescale begins. Inherited
   from `scal-mutation-rotation` applicability condition 1 (the `scal` operation is
   element-local — `x[i]` depends only on `x[i]` — so no separate read buffer aliases).
2. **`x ≠ 0` (partiality).** The L0 `MFEM_ASSERT(norm > 0.0)` (`vector.hpp:267`) enforces
   this; the L1 operator is undefined on the zero vector. This is the one applicability
   condition distinguishing `normalize` from the total `nrm2` / `scal` leaves.
3. **Element type real or complex, norm always real.** The variant axis is absorbed
   entirely by the inherited `nrm2` (real-valued output regardless of input element type)
   and `scal` (rescale matches input element type) sub-themes; the fusion introduces no
   new element-type handling. The `1.0/norm` divisor is a real `double` in all variants
   (`norm` is real); on a complex `x` the rescale reaches `scal` Sub-pattern B's
   `imag(s) == 0.0` real-into-complex promotion branch (a transparent shape-specialisation,
   inherited).
4. **Single-rank reading of the collective.** The `MPI_Allreduce` inside the inner
   `Norml2 → Dot` reduction is a local no-op under the in-scope single-machine target
   (CLAUDE.md "Scope"), structurally present, carrying the bit-determinism caveat.
   Inherited from `nrm2-mutation-rotation` (hence `dot-mutation-rotation`) applicability
   conditions.

## Justification kind

- **Sub-pattern A** (`Norml2` reduction) — `structural` (inherited from
  `nrm2-mutation-rotation`).
- **Sub-pattern B** (in-place rescale) — `structural` (inherited from
  `scal-mutation-rotation` Sub-pattern A), with the reciprocal-vs-divide transparent-trick
  sub-note.
- **Sub-pattern C** (returned norm) — `structural` (the returned `norm` binds to
  `result.0`); the three consumer shapes are the load-bearing evidence.

The theme as a whole is `structural`, resting on the L1 factorisation law
`normalize(x) = (nrm2(x), scal(1/nrm2(x), x))` (`book/src/L1/normalize.md:50`, law 6),
two inherited sub-themes (`nrm2-mutation-rotation`, `scal-mutation-rotation` Sub-pattern A),
and one positively-anchored guard classification (the `MFEM_ASSERT(norm > 0.0)` partiality
witness). The one non-syntactic ingredient — the partiality of the fused operator at
`x = 0` — is read straight off the L0 source's own assertion (`vector.hpp:267`); **no
negative-anchor reconstruction, no literature inference, no speculative operator** — so
`firm` rather than `partly-constructive`. A future `lowering-verifier` audit should confirm
the `linalg::Normalize` template is the sole fused-normalise surface form (the inline
open-coded shapes — Arnoldi `iterative.cpp:631-632`, NEP `nleps.cpp:610-611` — are
recognition instances, not distinct overloads).

## Speculative L1 operators

**None.** This theme lowers the already-firm L1 [`normalize`](../L1/normalize.md) operator
into existing firm L1 vocabulary — `nrm2` for the reduction, `scal` for the rescale. It
proposes no new L1 vocabulary. The B-weighted sibling `normalize_B` (energy-norm
normalisation `(β_B, x/β_B)` with `β_B = √(xᴴ B x)`) is recorded as a **rough-in note**,
NOT a speculative operator of this theme, for the reasons the L1 entry gives
(`book/src/L1/normalize.md:83-95`):

- **No fused Palace site.** Palace has **no** `linalg::Normalize`-with-`B` free function;
  the sole `Normalize` overload (`vector.hpp:264`) takes no `B`. The header comment
  ("...possibly with respect to an SPD matrix B", `vector.hpp:262`) is aspirational. The
  B-weighted reduction exists ([`matrix-weighted-norm`](../L1/matrix-weighted-norm.md), via
  `linalg::Norml2(comm, x, B, Bx)`, `palace/linalg/operator.cpp:599-619`) but its callsites are
  error-norm / eigenvector-norm computations that **do not rescale** — they feed residual
  ratios, not an in-place normalise. (Contrast: the `Normalize`-with-`B` *inline* form
  `x *= 1.0/norm` after a weighted `Norml2` IS the consumer Sub-pattern C of
  [`matrix-weighted-norm-mutation-rotation`](./matrix-weighted-norm-mutation-rotation.md)
  at `palace/linalg/operator.hpp:377-384` — but that is the weighted-norm theme's consumer, not a fused
  `normalize_B` operator.)
- **Inherited test-coverage bound.** `normalize_B`'s norm constituent
  [`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) is `rough-in (test-coverage-bounded)`;
  a fused `normalize_B` cannot be firmer than its constituent.

If/when an inline B-weighted-normalise site surfaces (a `scale = Norml2(comm, v, B, Bv);
v *= 1.0/scale` pattern distinct from the unweighted `nleps.cpp:610-611`), `normalize_B`
would promote to a firm sibling inheriting the `matrix-weighted-norm` promotion gate.
Until then it is tracked as a queued candidate, not part of this theme's firm claim.

## Variant axes

`normalize` inherits exactly the element-type axis of its constituents and adds none (per
`classify-variant-axis`):

- **element-type**: `real` | `complex`. The `linalg::Normalize` template is `VecType`-generic
  (`vector.hpp:263-264`); the inner `Norml2` returns a real scalar in both cases (inherited
  `nrm2` axis collapse) and the `x *= 1.0/norm` rescale dispatches to the matching `operator*=`
  (inherited `scal` element-type axis, including the `imag(s) == 0.0` real-into-complex
  promotion on the complex path). At L1 these collapse to one operator parameterised by element
  type; the norm output is real-valued in all variants.

No constant-folding axis (the rescale scalar `1.0/norm` is a runtime value, never `0`/`1`/`-1`
by construction since `norm > 0`). No reduction-order variant beyond the one inherited from
`nrm2` (hence `dot`). The only non-trivial semantic axis relative to the leaves is the
**partiality** at `x = 0` (the `MFEM_ASSERT`), which is uniform across element types and is
the guard classified above, not a variant axis.

## Verified-against

L0 evidence ranges (self-verified via `tools/citecheck/citecheck.py --anchor` against on-disk
`reference/palace/` this invocation — producer-citation self-verification, `verify-citation-range`;
the on-disk `vector.hpp` was confirmed authoritative against the Read tool, and the `Normalize`
def line is `264`, the `MFEM_ASSERT` `267`, the rescale `268`, the `return norm` `269`, all
within the cited `262-270` range):

- `palace/linalg/vector.hpp:262-270` — `linalg::Normalize` template: `auto norm = Norml2(comm, x);`
  (`:266`), `MFEM_ASSERT(norm > 0.0, "Zero vector norm in normalization!")` (`:267`),
  `x *= 1.0 / norm;` (`:268`), `return norm;` (`:269`). The positive source site — `normalize`
  verbatim, returning the norm. **Self-verified** (`--anchor 'Normalize'` → 262/264 def in range;
  `--anchor 'MFEM_ASSERT'` → 267; `--anchor '1.0 / norm'` → 268; `--anchor 'return norm'` → 269;
  `--anchor 'Norml2'` → 266).
- `palace/linalg/vector.hpp:259` — `Norml2` body `std::sqrt(std::abs(Dot(comm, x, x)))` (the
  reduction chain Sub-pattern A inherits from `nrm2-mutation-rotation`). [inherited boundary]
- `palace/linalg/iterative.cpp:631-632` — GMRES Arnoldi: `Hj[j + 1] = linalg::Norml2(comm, w);
  w *= 1.0 / Hj[j + 1];` (returned norm → Hessenberg sub-diagonal AND rescale divisor; the inline
  un-fused `normalize` with both outputs consumed). **Self-verified** (`--anchor 'Hj[j + 1] =
  linalg::Norml2'` → 631; `--anchor '1.0 / Hj'` → 632).
- `palace/linalg/iterative.cpp:810-811` — second analogous GMRES Arnoldi path:
  `Hj[j + 1] = linalg::Norml2(comm, w); w *= 1.0 / Hj[j + 1];`. **Audited** (`--anchor 'Hj[j + 1] = linalg::Norml2'` → 810; `--anchor 'w *= 1.0 / Hj[j + 1]'` → 811).
- `palace/linalg/operator.cpp:660-661` — `SetRandom(comm, u); Normalize(comm, u);` (power-iteration
  seed normalise; returned norm discarded — the `snd ∘ normalize` shape). **Self-verified**
  (`--anchor 'SetRandom(comm, u)'` → 660).
- `palace/linalg/operator.cpp:673` — `l = Normalize(comm, u);` (returned norm IS the
  dominant-eigenvalue estimate). **Self-verified** (`--anchor 'l = Normalize'` → 673).
- `palace/linalg/operator.cpp:676` — `res = std::abs(l - l0) / l0;` (convergence test consuming the
  returned norm `l` — direct evidence the returned scalar is load-bearing). **Self-verified**
  (`--anchor 'res = std::abs(l - l0)'` → 676).
- `palace/linalg/nleps.cpp:610-611` — NEP deflation: `const auto scale = linalg::Norml2(GetComm(), v);
  v *= 1.0 / scale;` (inline unweighted normalise). **Self-verified** (`--anchor 'Norml2(GetComm(), v)'`
  → 610; `--anchor '1.0 / scale'` → 611).
- `palace/linalg/nleps.cpp:617` — `H.col(k).head(k) = v2 / scale;` (returned norm reused to rescale
  the coordinate companion — doubly load-bearing). **Self-verified** (`--anchor 'v2 / scale'` → 617).

L1 / cross-theme anchors:

- `book/src/L1/normalize.md` — the firm L1 operator this theme lowers: signature
  `normalize :: (x: Tensor[N]) -> (Scalar, Tensor[N])` (`:17-18`), the factorisation law 6
  (`:50`), the partiality precondition `β > 0` (`:26`), the reciprocal-vs-divide
  transparent-trick note (`:32`), the three load-bearing consumer shapes (`:34-37`), the
  `normalize_B` rough-in note (`:83-95`).
- `book/src/L1-L0/nrm2-mutation-rotation.md` — Sub-pattern A inherited (the
  `std::sqrt(std::abs(Dot(comm, x, x)))` no-buffer reduction chain + the load-bearing `std::abs`
  defensive-guard classification).
- `book/src/L1-L0/scal-mutation-rotation.md` — Sub-pattern A inherited (the in-place
  `x *= 1.0/norm` receiver overwrite; names this very `Normalize` site at `:48-49,55-58`; the
  complex-path `imag(s) == 0.0` promotion at Sub-pattern B).
- `book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md` — the sub-pattern-reuse precedent
  (reuses apply-linop A + dot A) and the B-weighted boundary (its Sub-pattern C is the
  weighted-`Normalize` consumer `palace/linalg/operator.hpp:377-384`, distinct from this unweighted theme).
- `book/src/L1/nrm2.md`, `book/src/L1/scal.md` — the two firm L1 leaves the fusion composes.

Test evidence (L0-equivalent semantic documentation; inherited):

- `palace/test/unit/test-orthog.cpp:193,208` — `V[0] *= 1 / v0_norm;` / `V[1] *= 1 / v1_norm;`
  on real `Vector`s, each immediately after a `CHECK_THAT(v*_norm, ...)` assertion on the norm.
  The textbook by-hand `normalize` (norm asserted, then rescale) on the real path — empirical-match
  for the fused operator's two-output shape. Cited via `scal-mutation-rotation.md:181-186` and
  `book/src/L1/normalize.md:120` (inherited).

## Status

`firm` — the rewrite is the structural expansion of the L0 `linalg::Normalize(comm, x)`
four-step composition (reduction → guard → in-place rescale → returned norm), exhaustively
pinned by direct, self-verified evidence from the positive source `vector.hpp:262-270`. The
three sub-patterns (A `Norml2` reduction, B in-place rescale, C returned norm) **reuse** the
firm sibling sub-themes (`nrm2-mutation-rotation`, `scal-mutation-rotation` Sub-pattern A)
rather than restating them — following the cycle-026 `matrix-weighted-norm-mutation-rotation`
precedent. The load-bearing returned norm (Sub-pattern C) — the reason `normalize` is a named
primitive — is evidenced by three distinct, self-verified consumer shapes (GMRES Hessenberg
`iterative.cpp:631-632`, power-iteration eigenvalue `palace/linalg/operator.cpp:673,676`, NEP deflation
companion-scale `nleps.cpp:610-611,617`), each consuming the norm *after* the rescale. The one
non-syntactic ingredient — the partiality at `x = 0` — is positively anchored to the L0
`MFEM_ASSERT(norm > 0.0)` (`vector.hpp:267`); **no negative-anchor reconstruction, no literature
inference, no speculative operator** — so `firm` rather than `partly-constructive`. The B-weighted
sibling `normalize_B` is an in-chapter rough-in note (no fused Palace site + inherited
`matrix-weighted-norm` test-coverage bound), not part of the firm claim.

A `lowering-verifier` audit attaching the `verified_against:` block (per the sibling-theme
convention) confirming the surface-form recognition is exhaustive (the `linalg::Normalize`
template is the sole fused-normalise overload; the inherited-sub-theme boundaries hold; the
returned-norm consumer cohort is complete) is the standard follow-up, not a status reduction.
This audit was performed cycle-028 (lowering-verifier); the `verified_against:` block below
records the per-citation verdicts (fully-supported on the firm unweighted core).

```yaml
verified_against:
  - citation: palace/linalg/vector.hpp:262-270
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "linalg::Normalize four-step composition read verbatim; def :264, reduction :266, guard :267, rescale :268, return :269 — all anchors land exactly on-disk (zero codemap drift)."
  - citation: palace/linalg/vector.hpp:259
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "Norml2 body std::sqrt(std::abs(Dot(comm,x,x))) — inherited Sub-pattern A boundary; anchor at :259."
  - citation: palace/linalg/vector.hpp:267
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "MFEM_ASSERT(norm > 0.0) partiality witness — positively anchored; the one non-syntactic ingredient; firm not partly-constructive confirmed."
  - citation: palace/linalg/iterative.cpp:631-632
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "GMRES Arnoldi (first path): Hj[j+1]=Norml2 :631, w*=1.0/Hj[j+1] :632; beta feeds plane-rotation solve at :636-639 (GeneratePlaneRotation :638) — Hessenberg sub-diagonal consumer confirmed."
  - citation: palace/linalg/iterative.cpp:810-811
    verdict: partially-supports
    audited_at: 2026-05-29T19:45:58Z
    note: "Second GMRES path: the full two-line shape spans 810-811 (Hj[j+1]=Norml2 at :810, w*=1.0/Hj[j+1] at :811). Re-cited to 810-811 for parity with the first path (Edit 2). Both anchors land exactly on-disk."
  - citation: palace/linalg/operator.cpp:660-661
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "Power-iteration seed: SetRandom :660, Normalize :661 (return discarded — snd-only projection shape)."
  - citation: palace/linalg/operator.cpp:673
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "l = Normalize(comm, u) — returned norm IS the dominant-eigenvalue estimate; carrier u feeds next A.Mult(u,v) at :664."
  - citation: palace/linalg/operator.cpp:676
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "res = std::abs(l - l0) / l0 — convergence test consuming the returned norm l; direct load-bearing evidence."
  - citation: palace/linalg/nleps.cpp:610-611
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "NEP deflation: scale = Norml2(GetComm(), v) :610, v *= 1.0/scale :611 — inline unweighted normalise; :609 comment 'Update the invariant pair with normalization' confirms reading."
  - citation: palace/linalg/nleps.cpp:617
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "H.col(k).head(k) = v2 / scale — returned norm reused to rescale coordinate companion v2; doubly load-bearing confirmed."
  - citation: book/src/L1/normalize.md:50
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "Factorisation law 6 — the LHS the theme lowers; anchor at :50."
  - citation: book/src/L1-L0/scal-mutation-rotation.md:48-58
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "scal Sub-pattern A names this Normalize site (Normalize token at :48 and :55) — inheritance boundary holds."
  - citation: palace/test/unit/test-orthog.cpp:193
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "V[0] *= 1 / v0_norm — by-hand normalise empirical-match (real path); inherited test evidence."
  - citation: palace/test/unit/test-orthog.cpp:208
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "V[1] *= 1 / v1_norm — second by-hand normalise instance."
  - citation: palace/linalg/operator.hpp:377-384
    verdict: does-not-support
    audited_at: 2026-05-29T19:45:58Z
    note: "Range correct, but the surrounding 'no fused linalg::Normalize-with-B free function' claim (lines 51, 285-287, 311-313) is WRONG: palace/linalg/operator.hpp:378 IS a fused B-weighted Normalize(comm, x, B, Bx) free function (reduction->guard->rescale->return, identical to vector.hpp:264). The defensible fact is that this fused B-Normalize is UNCALLED (no 4-arg rescaling callsite in the tree). Affects only the normalize_B rough-in note, NOT the firm unweighted core. Routed to follow-up abstractor (F1)."
  - citation: palace/linalg/operator.cpp:599-619
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "B-weighted Norml2 reduction (B.Mult(x,Bx) at :602) — the matrix-weighted-norm reduction; in-bounds. Note: it IS fused into palace/linalg/operator.hpp:378 (see palace/linalg/operator.hpp:377-384 row)."
```
