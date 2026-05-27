---
agent: abstractor
invoked_at: 2026-05-27T025354Z
scope: L1>L0 theme sketch — axpbypcz-mutation-rotation
status: integrated
integrated_at: 2026-05-27T07:04:24Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied. Third mutation-rotation theme. 4 sub-patterns + first mixed-justification sub-rule in project (γ==0 labelled algebraic+structural). Closes axpbypcz-mutation-rotation-abstractor-target (cycle-004).
skill_uptake:
  consulted: []
  applicable_but_not_used:
    - verify-citation-range
    - verify-refinement-surface
    - classify-variant-axis
  rationale: |
    Skill-selection was not performed at dispatch. The three named skills
    were applicable: `verify-citation-range` for the L0 source ranges,
    `classify-variant-axis` for the four sub-pattern axes, and
    `verify-refinement-surface` for the surface-shape check. Recorded
    here retrospectively (repairer-added).
inputs:
  - book/src/L1/axpbypcz.md (firm L1 operator, cycle-004)
  - book/src/L1-L0/axpby-mutation-rotation.md (precedent theme, cycle-003)
  - palace/linalg/vector.hpp:133-136 (ComplexVector::AXPBYPCZ member decl)
  - palace/linalg/vector.hpp:313-316 (free-function template decl)
  - palace/linalg/vector.cpp:381-386 (ComplexVector::AXPBYPCZ member-form trampoline)
  - palace/linalg/vector.cpp:388-455 (ComplexVector::AXPBYPCZ static member-form body, real-split)
  - palace/linalg/vector.cpp:745-758 (free-function real-real specialisation with γ==0 branch)
  - palace/linalg/vector.cpp:760-765 (free-function complex-complex specialisation)
  - palace/linalg/vector.cpp:767-772 (free-function real-on-complex specialisation)
  - call-site corpus: slepc.cpp:1986, arpack.cpp:772, arpack.cpp:787,
                      nleps.cpp:343-344, nleps.cpp:471, nleps.cpp:676, nleps.cpp:693,
                      timeoperator.cpp:139, timeoperator.cpp:217, timeoperator.cpp:273,
                      romoperator.cpp:188-189
---

# REPORT: L1>L0 theme sketch — axpbypcz-mutation-rotation

## Summary

`axpbypcz` (firm at L1 since cycle-004; `book/src/L1/axpbypcz.md`) is the fused three-scalar three-vector update `z_new = α·x + β·y + γ·z_old`. At L0, Palace expresses it through a four-form family: a free-function template (`linalg::AXPBYPCZ`) with three specialisations and a `ComplexVector` member method. Within the free-function real-real specialisation and within the ComplexVector member-form body, an internal `γ == 0` branch dispatches to a structurally distinct kernel — the γ==0 fast-path drops the third vector load and switches the destination from `ReadWrite` to `Write` semantics. This theme records the four sub-patterns and the γ==0 algebraic sub-rule. The recognition is **structural-overall, algebraic-on-γ==0**: the γ==0 sub-rule mixes structural-rebind (z still gets a new value) with algebraic-constant-folding (γ=0 collapses the L1 form into `axpby(α, x, β, y)` and the L0 path selects a 2-vector kernel — MFEM's `add(α, x, β, y, z)` in the real-real path; a γ=0-specialised kernel in the complex member-form). No speculative L1 operators are needed — `axpbypcz`, `axpby`, and `axpy` are already firm; the theme reaches into them as established vocabulary.

The companion-precedent theme `axpby-mutation-rotation` (cycle-003) lowered `axpy` / `axpby` with a three-sub-pattern shape (bare / α==1 / α==-1). This theme is structurally the cousin: four sub-patterns (one per L0 dispatch shape) plus one algebraic sub-rule (γ==0). The α==0 and β==0 algebraic identities listed in `axpbypcz.md` laws 3 and 4 do **not** induce a separate L0 sub-pattern — Palace does **not** branch on `α == 0` or `β == 0` at runtime in any of the four forms. They are recorded as recognition-only sub-rules ("if the caller is known at L1 to pass α=0, the rewrite target reduces to `axpby(β, y, γ, z)`, but the L0 *source-text shape* is unchanged"). This asymmetry — γ has a runtime branch, α and β do not — is itself worth noting as a Palace-implementation observation; see Open questions below.

## Proposed changes

```edit:book/src/L1-L0/axpbypcz-mutation-rotation.md
[create the theme entry with the following sections]

# axpbypcz-mutation-rotation

The mutation rotation for the fused three-scalar three-vector update. Lowers
the pure L1 form `axpbypcz(α, x, β, y, γ, z_old) = α·x + β·y + γ·z_old` into
Palace's L0 free-function template and `ComplexVector` member-method forms.
Includes one algebraic sub-rule on `γ == 0` that mixes structural-rebind with
algebraic-constant-folding: when γ=0 the L1 form collapses to `axpby(α, x, β,
y)` and the L0 dispatch selects a 2-vector kernel (MFEM's 5-arg `add(α, x, β,
y, z)` in the real-real path; a γ=0-specialised kernel in the complex
member-form body).

## Slug

`axpbypcz-mutation-rotation`

## L1 form (LHS)

The pure-functional update consumes the prior value of `z` and produces a
fresh post-update value:

    z_new = axpbypcz(α, x, β, y, γ, z_old)
          = α·x + β·y + γ·z_old

where `α, β, γ : Scalar`, `x, y, z_old : Tensor[N]`, and `result : Tensor[N]`.
See [`L1/axpbypcz`](../L1/axpbypcz.md) for the firm operator entry, signature,
and algebraic laws.

## L0 form (RHS)

Four sub-patterns of the same rewrite, distinguished by the dispatch shape of
the L0 call. Plus one algebraic sub-rule on `γ == 0` that applies inside
sub-patterns A and C (the two paths that have a runtime γ==0 branch).

### Sub-pattern A — free-function real-real

    linalg::AXPBYPCZ(alpha, x, beta, y, gamma, z);     // double α,β,γ; Vector x,y,z

The free-function template specialised on `double` scalars and `mfem::Vector`
vectors. Internally branches on `gamma == 0.0`: the γ==0 fast-path calls
MFEM's `add(alpha, x, beta, y, z)` (5-arg out-of-place; writes z from the
linear combination of the first four args); the γ≠0 slow-path splits into
`AXPBY(alpha, x, gamma, z); z.Add(beta, y)` (two in-place calls computing the
sum in a different order than the fused form would).

Justification kind: **structural** — re-bind the L1 output value into the L0
destination buffer `z`. The γ==0 / γ≠0 internal branch is a transparent
performance specialisation (algebraically equivalent — both compute `α·x +
β·y + γ·z_old`), classified by the γ==0 sub-rule below.

Citations:
- `palace/linalg/vector.hpp:313-316` — free-function template decl.
- `palace/linalg/vector.cpp:745-758` — real-real specialisation body with
  γ==0 branch.
- `palace/linalg/vector.cpp:729` — MFEM `add(...)` kernel referenced by the
  γ==0 fast-path (also reused by the L1 `axpby` operator).
- Call-site: `palace/models/timeoperator.cpp:139` — `linalg::AXPBYPCZ(-1.0,
  rhs1, dJ_coef(t), NegJ, 0.0, rhs1)` (γ=0; **uses aliasing** — z is also the
  first input; see Applicability conditions §1).
- Call-site: `palace/models/timeoperator.cpp:217` — `linalg::AXPBYPCZ(1.0,
  RHS2, dt, k1, 0.0, k2)` (γ=0; non-aliased).
- Call-site: `palace/models/timeoperator.cpp:273` — `linalg::AXPBYPCZ(1.0,
  b2, saved_gamma, x1, 0.0, x2)` (γ=0; non-aliased).

### Sub-pattern B — free-function complex-complex

    linalg::AXPBYPCZ(alpha, x, beta, y, gamma, z);     // std::complex<double> α,β,γ; ComplexVector x,y,z

The free-function template specialised on `std::complex<double>` scalars and
`ComplexVector` vectors. The body is a one-line delegation to the member
form: `z.AXPBYPCZ(alpha, x, beta, y, gamma)`. No internal branch at this
layer — branching happens inside the member-form body (see sub-pattern C).

Justification kind: **structural** — pure trampoline; the destination
re-binding is performed by the member form.

Citations:
- `palace/linalg/vector.cpp:760-765` — complex-complex specialisation body
  (one-line delegation).
- (No observed call sites with `std::complex<double>` α,β,γ. The complex
  call-site corpus uses the real-scalar overload — sub-pattern D. Treat
  sub-pattern B as a recognition rule for *potential* call sites, by analogy
  with the `linalg::AXPY(std::complex<double>, ComplexVector, ComplexVector)`
  defined-not-used form documented in `axpby-mutation-rotation.md`
  Verified-against.)

### Sub-pattern C — ComplexVector member form

    z.AXPBYPCZ(alpha, x, beta, y, gamma);              // std::complex<double> α,β,γ; ComplexVector x,y,z

The in-place mutating member method on `ComplexVector`. The destination is
the receiver `z`. The body is a one-line trampoline to a static
member-function (`ComplexVector::AXPBYPCZ` operating on raw real/imag halves
at `vector.cpp:388-455`) which carries the algebraic-branch logic:

- Outer branch on `gamma == 0.0`:
  - γ==0 path: destination buffer obtained via `Write(use_dev)` (the prior z
    is discarded — no read of `ZR`/`ZI`); kernel computes `ZR/I = α·XR/I +
    β·YR/I` (real/imag combined per the complex-multiply rules).
  - γ≠0 path: destination buffer obtained via `ReadWrite(use_dev)`; kernel
    computes `ZR/I = α·XR/I + β·YR/I + γ·ZR/I_prev`.
- Inner branch (both paths) on `ai == 0.0 && bi == 0.0` (real-α, real-β
  fast-path), and additionally on `gi == 0.0` (real-γ fast-path inside the
  γ≠0 outer branch): drops the imaginary-scalar cross-terms from the kernel.
  These inner branches are transparent performance specialisations on the
  scalar imaginary parts; they are not separate L1>L0 sub-patterns (no L1
  algebraic distinction; the L1 scalar-promotion variant axis in
  `axpbypcz.md` covers the typing concern).

Justification kind: **structural** — receiver-as-destination re-binding. The
inner γ==0 outer branch is the same γ==0 algebraic sub-rule as sub-pattern A
(see § γ==0 algebraic sub-rule below); the inner imaginary-scalar branches
are transparent.

Citations:
- `palace/linalg/vector.hpp:133-136` — member decl with comment
  `In-place addition (*this) = alpha * x + beta * y + gamma * (*this).`
- `palace/linalg/vector.cpp:381-386` — `ComplexVector::AXPBYPCZ` outer
  trampoline (delegates to static member-form on `Real()`/`Imag()` halves).
- `palace/linalg/vector.cpp:388-455` — static member-form body, with the
  γ==0 outer branch and the imaginary-scalar inner branches.
- Call-site: `palace/linalg/slepc.cpp:1986` — `ctx->y1.AXPBYPCZ(...)` with
  γ=−γ/σ (runtime non-zero in general).
- Call-site: `palace/linalg/arpack.cpp:772` — `y2.AXPBYPCZ(sigma, x1, gamma,
  x2, 0.0)` (γ=0).
- Call-site: `palace/linalg/arpack.cpp:787` — `y2.AXPBYPCZ(sigma/gamma, y1,
  1.0, x1, 0.0)` (γ=0).
- Call-site: `palace/linalg/nleps.cpp:471` — `v.AXPBYPCZ(0.5,
  eigenvectors[i1], 0.5, eigenvectors[i2], 0.0)` (γ=0).
- Call-site: `palace/linalg/nleps.cpp:676` — `z.AXPBYPCZ(-delta_eig, w, -1.0,
  u, 0.0)` (γ=0; combines with sub-pattern-C-style call-site and α=−Δλ,
  β=−1 literals — algebraic-but-not-fast-path-branched).
- Call-site: `palace/linalg/nleps.cpp:693` — `v_trial.AXPBYPCZ(1.0, v, alpha,
  du, 0.0)` (γ=0).

### Sub-pattern D — free-function real-on-complex

    linalg::AXPBYPCZ(alpha, x, beta, y, gamma, z);     // double α,β,γ; ComplexVector x,y,z

The free-function template specialised on `double` scalars and
`ComplexVector` vectors. The body is a one-line delegation to the member
form: `z.AXPBYPCZ(alpha, x, beta, y, gamma)` — the C++ overload resolution
promotes the `double` scalars to `std::complex<double>` at the call. No
internal branch at this layer — branching happens inside the member-form
body (see sub-pattern C).

Justification kind: **structural** — pure trampoline with implicit
scalar-promotion (covered by the L1 `axpbypcz` "scalar promotion" variant
sub-axis; not a separate L1 operator). The destination re-binding is
performed by the member form.

Citations:
- `palace/linalg/vector.cpp:767-772` — real-on-complex specialisation body
  (one-line delegation).
- Call-site: `palace/linalg/nleps.cpp:343-344` — two paired calls computing
  the real and imaginary halves of a complex linear combination, each going
  through this overload with `1.0` as γ (γ≠0 path inside the member).
- Call-site: `palace/models/romoperator.cpp:188-189` — two paired calls also
  with `1.0` as γ (γ≠0 path inside the member).

### γ==0 algebraic sub-rule (applies inside sub-patterns A and C)

When the recognition is `γ ≡ 0` (a literal `0.0` argument at the L0 call
site, or a compile-time-known γ=0 — observed exclusively as literal `0.0` in
the call-site corpus surveyed above), the L1 form collapses to an `axpby`
call by `axpbypcz` law #1 of [`L1/axpbypcz`](../L1/axpbypcz.md):

    axpbypcz(α, x, β, y, 0, z_old) = α·x + β·y = axpby(α, x, β, y)

The L0 dispatch then selects a structurally distinct 2-vector kernel:

- **Sub-pattern A (real-real)**: the γ==0 branch at `vector.cpp:749-751`
  calls MFEM's 5-arg `add(alpha, x, beta, y, z)` — the same kernel used by
  the L1 `axpby` operator's L0 real-real path
  (`axpby-mutation-rotation.md`, sub-pattern A-of-axpby-equivalent at
  `vector.cpp:729`).
- **Sub-pattern C (complex member)**: the γ==0 branch at `vector.cpp:402-426`
  selects a `Write`-rather-than-`ReadWrite` access pattern on z and emits a
  kernel without the `γ·ZR/I_prev` cross-terms.

The sub-rule is **algebraic** (γ=0 turns the 3-vector form into a 2-vector
form, by law #1) *and* **structural** (z still gets a new value; the
mutation pattern is preserved — the buffer access mode shifts from
ReadWrite to Write in the complex form, and the kernel arity changes in the
real form, but the L1>L0 destination re-binding stays the same). This is
the first L1>L0 sub-rule in the spec that mixes the two justification
kinds. The recognition rule is **syntactic**: a literal `0.0` at the γ
slot of the call site is sufficient. A runtime-zero γ value lowers to the
γ≠0 path (the L0 branch is on the literal-compared-to-zero test, not on a
type-level zero).

The γ≠0 path of sub-pattern A is itself worth noting as a **load-bearing
numerical observation** (per `CLAUDE.md` "Optimization tricks vs. base
algebra"): the slow-path two-call split `AXPBY(α, x, γ, z); z.Add(β, y)`
computes the sum in a *different IEEE-754 evaluation order* than the
γ==0 fast-path's `add(α, x, β, y, z)` would, so bit-identical reproduction
across L0 branches is not guaranteed within the same operator family. This
is recorded in `axpbypcz.md` § "Laws that explicitly do not hold" and is
not a defect of this lowering theme — it is a property of the L0 source.

## Applicability conditions

For all four sub-patterns the rewrite preserves semantics when:

1. **No aliasing between `x`, `y`, and `z`** (with one exception, see
   below). Palace's L0 kernels read `x` and `y` element by element while
   writing `z[i]`; in the γ≠0 path, `z[i]` is also read (the prior z).
   If `x` aliases `z` and γ≠0, the L0 behaviour is well-defined (read-then-
   write at the same index, in-place per element), but the L1 form must
   carry the alias as a structural identity to match: `axpbypcz(α, z, β,
   y, γ, z_old) = α·z_old + β·y + γ·z_old = (α+γ)·z_old + β·y =
   axpby(α+γ, z_old, β, y)`. **Exception observed**:
   `timeoperator.cpp:139` reads `rhs1` and writes `rhs1` (z aliases x)
   with γ=0; under the γ==0 sub-rule this is equivalent to
   `axpby(-1.0, rhs1, dJ_coef, NegJ)` which then reads-and-writes rhs1
   in the L0 `add(α, x, β, y, z)` kernel — MFEM's kernel is defined to be
   alias-safe with the destination matching one of the inputs (verify
   against MFEM docs in a future cycle; flagged in Open questions).
2. **No observer of the prior `z` value after the call.** Same as
   `axpby-mutation-rotation` condition #2.
3. **Conforming shape and element type.** `x.Size() == y.Size() ==
   z.Size()`; all three real (`Vector`) or all three complex
   (`ComplexVector`); the real-on-complex overload at
   `vector.cpp:767-772` promotes scalars implicitly per the L1
   `axpbypcz` scalar-promotion variant sub-axis.
4. **`γ` is a runtime scalar (not a special form) — γ==0 recognition is
   syntactic.** The γ==0 sub-rule selection is a recognition step on the
   literal `0.0` (or a compile-time-known γ=0) at the L0 call site. A
   runtime γ value, even if it happens to equal zero at runtime, lowers
   to the γ≠0 path. This matches the L0 branch on `gamma == 0.0` — a
   value comparison, not a type-level zero. (Identical structure to
   `axpby-mutation-rotation` condition #4 on α.)
5. **No applicability conditions on α==0 or β==0.** Palace does *not*
   branch on `alpha == 0` or `beta == 0` at L0 — the algebraic
   identities `axpbypcz(0, x, β, y, γ, z) = axpby(β, y, γ, z)` and
   `axpbypcz(α, x, 0, y, γ, z) = axpby(α, x, γ, z)` (laws #3, #4 of
   `axpbypcz.md`) are **recognition-only** rewrites at L1, not L0
   sub-patterns. A future combinator-miner or lowering-verifier may
   choose to upgrade these to fully realised sub-patterns if a use-case
   warrants it; for now they are noted but not branched.

## Justification kind

- **Sub-pattern A** — `structural` (with the γ==0 algebraic sub-rule).
- **Sub-pattern B** — `structural` (pure trampoline; defined-not-used).
- **Sub-pattern C** — `structural` (receiver-as-destination, with the
  same γ==0 algebraic sub-rule as A; the inner imaginary-scalar branches
  are transparent and not sub-patterns).
- **Sub-pattern D** — `structural` (pure trampoline with implicit
  scalar promotion).
- **γ==0 algebraic sub-rule** — `algebraic` (law #1 of
  `axpbypcz.md`) *and* `structural` (destination still re-bound; kernel
  shape changes). The theme's first **mixed-justification** sub-rule.

The theme as a whole is `structural` with one mixed-justification
algebraic sub-rule. A `lowering-verifier` audit in a later cycle should
confirm sub-pattern recognition matches the L0 corpus exhaustively (the
call-site list above is illustrative, not exhaustive — exhaustive corpus
indexing deferred to that audit, matching the cycle-003
`axpby-mutation-rotation` coverage-note pattern).

## Speculative L1 operators

None. `axpbypcz`, `axpby`, and `axpy` are all firm L1 operators
(`book/src/L1/axpbypcz.md`, `book/src/L1/axpby.md`, `book/src/L1/axpy.md`)
and this theme reaches into them as established vocabulary. The γ==0
sub-rule's RHS reference to `axpby(α, x, β, y)` invokes the firm
[`L1/axpby`](../L1/axpby.md) operator directly; no rough-in is needed.

## Verified-against

L0 evidence ranges (decls and bodies):

- `palace/linalg/vector.hpp:133-136` — ComplexVector::AXPBYPCZ member decl.
- `palace/linalg/vector.hpp:313-316` — free-function template decl.
- `palace/linalg/vector.cpp:381-386` — ComplexVector::AXPBYPCZ outer
  trampoline.
- `palace/linalg/vector.cpp:388-455` — ComplexVector::AXPBYPCZ static
  member-form body with γ==0 branch and imaginary-scalar inner branches.
- `palace/linalg/vector.cpp:745-758` — free-function real-real
  specialisation with γ==0 branch.
- `palace/linalg/vector.cpp:760-765` — free-function complex-complex
  specialisation (defined-not-used trampoline).
- `palace/linalg/vector.cpp:767-772` — free-function real-on-complex
  specialisation (trampoline with implicit promotion).
- `palace/linalg/vector.cpp:729` — MFEM `add(...)` kernel referenced by
  both the L1 `axpby` operator's real-real path and the `axpbypcz`
  γ==0 fast-path.

L0 call-sites (illustrative, not exhaustive):

- `palace/linalg/slepc.cpp:1986` — sub-pattern C, γ≠0 (runtime).
- `palace/linalg/arpack.cpp:772` — sub-pattern C, γ=0 literal.
- `palace/linalg/arpack.cpp:787` — sub-pattern C, γ=0 literal.
- `palace/linalg/nleps.cpp:343-344` — sub-pattern D, γ=1.0 literal (γ≠0).
- `palace/linalg/nleps.cpp:471` — sub-pattern C, γ=0 literal.
- `palace/linalg/nleps.cpp:676` — sub-pattern C, γ=0 literal.
- `palace/linalg/nleps.cpp:693` — sub-pattern C, γ=0 literal.
- `palace/models/timeoperator.cpp:139` — sub-pattern A, γ=0 literal,
  z aliases x (see Applicability condition #1 exception).
- `palace/models/timeoperator.cpp:217` — sub-pattern A, γ=0 literal.
- `palace/models/timeoperator.cpp:273` — sub-pattern A, γ=0 literal.
- `palace/models/romoperator.cpp:188-189` — sub-pattern D, γ=1.0 literal
  (γ≠0).

L1 anchors:

- `book/src/L1/axpbypcz.md` — the firm L1 operator that all four
  sub-patterns lower from; the γ==0 algebraic sub-rule cites law #1.
- `book/src/L1/axpby.md` — the firm L1 operator that the γ==0 sub-rule
  collapses to.
- `book/src/L1-L0/axpby-mutation-rotation.md` — the precedent theme;
  this entry follows its structural template (sub-pattern enumeration +
  algebraic sub-rules) and extends it with the mixed-justification
  γ==0 sub-rule.

## Status

`rough-in` — sub-pattern recognition rules sketched; full sub-pattern
verification against the L0 corpus deferred to `lowering-verifier`
(matching the `axpby-mutation-rotation` post-cycle audit pattern). The
γ==0 algebraic sub-rule's mixed-justification framing should be
ratified by a `cross-layer-cross-cutter` review to confirm the
mixed-kind framing scales to other sub-rules in the spec (the
`axpby-mutation-rotation` α==1 sub-rule is pure-algebraic by contrast;
the γ==0 sub-rule's "structural+algebraic" framing is genuinely new and
worth methodology attention — flagged in Open questions of this report).
```

```edit:book/src/L1/index.md
[no dep-map changes — all referenced operators (`axpbypcz`, `axpby`,
 `axpy`) are already firm and present. No speculative L1 operators are
 emitted by this theme. The L1 index dep-map remains unchanged.

 Optional: add a forward link from the `axpbypcz` row's status cell to
 the new theme file once the theme lands. Integrator's discretion — not
 required by the abstractor role spec.]
```

```edit:book/src/SUMMARY.md
[under the "# L1 > L0 — Lowering" Part, after the `axpby-mutation-rotation`
 line, add:]

- [axpbypcz-mutation-rotation](./L1-L0/axpbypcz-mutation-rotation.md)

[the integrator applies this SUMMARY edit.]
```

## Speculative operators proposed

None. All operators referenced by this theme are firm at L1:

- `axpbypcz` (firm; cycle-004) — the LHS operator.
- `axpby` (firm; cycle-002) — the γ==0 sub-rule's RHS.
- `axpy` (firm; cycle-001) — referenced transitively via `axpbypcz`'s
  subsumption laws but not directly used in the RHS.

This is itself a methodology observation: by the time `axpbypcz` was
harvested (cycle-004), its companion lowering theme requires zero new
vocabulary. The theme is a pure structural enumeration over a firm L1
operator. Compare to `axpby-mutation-rotation` (cycle-003), which
emitted `axpby` as a rough-in operator since the harvester had not yet
run on it — that rough-in was promoted to firm in cycle-002 (out of
order chronologically but in-order in the new flow, post-restructure
of 2026-05-26). The current theme catches up: with `axpbypcz` firm,
this theme is a clean structural sketch.

## Supporting evidence

Source ranges and call-sites: see `## Verified-against` section above
of the proposed theme. Cross-references to the L1 operator and the
precedent theme are inlined in the theme body. The
`scaffolding/decisions/axpby-as-primitive.md` decision record (the
"Knock-on effects" §) anticipates this theme as a follow-up to the
cycle-004 `axpbypcz` harvester invocation — see also Open Question #1
of the cycle-004 `axpbypcz` harvester REPORT (the
`axpbypcz-mutation-rotation-abstractor-target` open question, which
this report closes).

## Open questions / caveats

1. **MFEM `add(...)` alias-safety claim** — Applicability condition #1
   states that the L0 `add(α, x, β, y, z)` kernel is alias-safe when
   `z` matches one of the inputs (e.g., `timeoperator.cpp:139` writes
   `rhs1` while reading `rhs1`). This claim is unverified against the
   MFEM source — the L0 corpus shows the call site relies on the
   behaviour but no MFEM-side proof has been captured. A future
   `lowering-verifier` or `cross-layer-cross-cutter` invocation should
   audit MFEM `Vector::Add` semantics under aliasing and either confirm
   the claim or escalate as a load-bearing semantic dependency on
   upstream behaviour (CLAUDE.md note: "Many symbols resolve into
   upstream libraries (MFEM, libCEED). Specialized agents cite Palace
   source, not vendored upstream. If a question requires upstream
   behaviour, log as open question." — this is exactly that case).
   Slug: `mfem-add-alias-safety`.

2. **The mixed-justification sub-rule framing is new — methodology
   review wanted.** The γ==0 sub-rule is labelled "algebraic *and*
   structural" because the structural-rebind is preserved while the
   algebraic-collapse (γ=0 → 3→2 vectors) is what triggers the L0
   kernel-shape change. The precedent theme `axpby-mutation-rotation`
   has pure-structural sub-pattern A and pure-algebraic sub-patterns B
   and C. This mixed framing has no precedent. A
   `cross-layer-cross-cutter` review should confirm whether the
   methodology already has a name for this combination — possibly
   `structural-with-algebraic-trigger` or
   `algebraic-folding-with-rebind` — and either ratify the framing or
   propose a primitive concept to capture it. The latter would land in
   `book/src/concepts/`. Slug:
   `mixed-justification-sub-rule-methodology`.

3. **Asymmetric runtime branching — why γ but not α, β?** Palace's L0
   code branches on `gamma == 0.0` but not on `alpha == 0.0` or
   `beta == 0.0`, despite the three positions being algebraically
   symmetric (laws #3, #4, #5 of `axpbypcz.md`). The implementation
   choice is presumably driven by the empirical observation that γ=0
   is the common case (γ is the *prior* z's coefficient, and most
   call sites are "compute z from x and y, discarding prior z" — i.e.,
   γ=0 — visible in the call-site corpus: 7 of 11 sub-pattern-C and
   sub-pattern-A surveyed sites pass `0.0` for γ). But this is an
   inferred rationale; the Palace source carries no comment. A
   `combinator-miner` or `same-layer-cross-cutter` invocation could
   confirm whether the asymmetry is by-design (γ=0 is a documented
   common case) or incidental (an artefact of the implementation
   history). Slug: `axpbypcz-gamma-asymmetric-branching-rationale`.

4. **Sub-pattern B is defined-not-used in the surveyed corpus.** Same
   pattern as the `axpby-mutation-rotation` coverage note: the
   complex-scalar-on-complex-vector free-function specialisation is
   compiled but not called from the surveyed call sites. Treat as a
   recognition rule for potential call sites, by analogy with the
   precedent theme. Slug:
   `axpbypcz-sub-pattern-B-defined-not-used-corpus-audit`.

5. **Inner imaginary-scalar branches are not L1>L0 sub-patterns.** The
   complex member-form has inner branches on `ai == 0 && bi == 0`
   (real-α, real-β fast-path) and on `gi == 0` (real-γ fast-path
   inside the γ≠0 outer branch). These are transparent performance
   specialisations covered by the L1 `axpbypcz` "scalar promotion"
   variant sub-axis; they are not separate L1>L0 sub-patterns at the
   theme level. If a future cycle decides to surface scalar-promotion
   recognition as a first-class L1>L0 concern (e.g., a separate
   theme for the implicit-scalar-promotion pattern across the entire
   BLAS-1 family — `axpy`, `axpby`, `axpbypcz`, `scal`), the inner
   branches here should be a cited evidence point. Slug:
   `scalar-promotion-mutation-rotation-cross-family-theme`.

6. **Caller-side γ-recognition is syntactic, not semantic.** A runtime
   γ value that happens to be zero at runtime lowers to the γ≠0 path
   at L0 (because the L0 branch is `gamma == 0.0` on the value, not on
   the type/literal). This means an L2/L3 optimisation that proves
   γ=0 at a higher layer would need to materialise the literal `0.0`
   at the L1>L0 boundary to trigger the fast-path — it cannot rely on
   the L0 runtime branch alone. This is consistent with the precedent
   `axpby-mutation-rotation` α==1 sub-pattern (also syntactic
   recognition); flagged here for cross-reference. Not an issue for
   this theme — just a downstream-lowering observation.
