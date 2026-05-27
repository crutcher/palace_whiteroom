---
agent: abstractor
invoked_at: 2026-05-26T23:18:43Z
scope: L1>L0 theme sketch — axpby-mutation-rotation
status: integrated
integrated_at: 2026-05-26T23:51:01Z
integration_commit: c3312a6
integration_notes: |
  Applied as-is per repaired META.md (overall_status: ready). All three proposed-changes blocks landed:
  (1) created book/src/L1-L0/axpby-mutation-rotation.md (first L1>L0 theme, rough-in);
  (2) appended `axpby` rough-in row to book/src/L1/index.md as plain text (no link, post-repair) since book/src/L1/axpby.md does not yet exist;
  (3) added `axpby-mutation-rotation` to SUMMARY.md under L1 > L0 Part.
  Slug-based filename adopted per report caveat #6 (preferred over plan's `theme-mutation-rotation.md` for forward-compatibility with future themes).
  Routed to `lowering-verifier` for full L0 corpus audit of three sub-patterns (open question `axpby-lowering-verifier-audit`).
  Build: cargo make book clean.
inputs:
  - book/src/L1/axpy.md (firm L1 operator, pilot-1)
  - book/src/concepts/axpy.md
  - book/src/L1-L0/index.md (empty theme list)
  - scaffolding/open-questions.md (axpy-l1-l0-three-subpatterns, axpby-axpbypcz-next-harvest)
  - reference/palace/palace/linalg/vector.cpp:276-311 (ComplexVector::AXPY definition)
  - reference/palace/palace/linalg/vector.cpp:701-712 (real AXPY dispatch + α==1 branch)
  - reference/palace/palace/linalg/vector.cpp:714-723 (complex AXPY dispatches)
  - reference/palace/palace/linalg/vector.cpp:726-743 (AXPBY family)
  - reference/palace/palace/linalg/vector.cpp:745-758 (AXPBYPCZ family)
  - reference/palace/palace/linalg/vector.hpp:115-128 (ComplexVector AXPY / Add / Subtract / += / -=)
  - reference/palace/palace/linalg/vector.hpp:130-136 (AXPBY, AXPBYPCZ member decls)
  - reference/palace/palace/linalg/vector.hpp:305-316 (free-function templates)
  - reference/palace/palace/linalg/operator.cpp:458-475 (SumOperator::AddMult uses y.Add(a*c, z))
  - reference/palace/palace/linalg/rap.cpp:73 (b.Add(-1.0, ty); α=-1 specialization)
  - reference/palace/palace/linalg/rap.cpp:317 (y.Add(a, ty); bare axpy)
skill_uptake:
  - skill: verify-citation-range
    triggered: true
    decision: explained_non_applicable
    rationale: Citations verified inline by reading source ranges (~15 evidence ranges spot-checked by critic in META.md); skill invocation deferred until critic-phase mechanism stabilizes. Repairer post-hoc tightened vector.hpp:115-117 → 116-117 to strict decl span.
  - skill: classify-variant-axis
    triggered: true
    decision: artifact_landed
    rationale: Scalar-value constant-folding axis classified into three sub-patterns (general α, α==1, α==-1); real-vs-complex element-type axis surfaced as a transparent performance-trick boundary, not a separate sub-pattern. See Sub-pattern A/B/C plus caveat #2.
  - skill: propose-rotation
    triggered: true
    decision: artifact_landed
    rationale: Theme follows propose-rotation template (LHS / RHS / applicability / justification kind / verified-against / status); rotation_claim is the L1→L0 mutation rotation under three constant-folding sub-rules.
---

# REPORT: L1>L0 theme sketch — axpby-mutation-rotation

## Summary

Palace expresses every BLAS-1 axpy-shaped update as an in-place member call on the destination vector: `y.Add(α, x)`, `y += x`, `y -= x`, or (for the fused form) `y.AXPBY(α, x, β)`. The L1 form is pure: `axpy(α, x, y_old) → y_new` and (rough-in) `axpby(α, x, β, y_old) → y_new = α·x + β·y_old`. The lowering theme `axpby-mutation-rotation` captures the structural rewrite that re-binds the L1 destination value back into the in-place buffer at L0, plus three algebraic sub-pattern rules that recognise the constant-folded forms Palace's source already specialised. The three sub-patterns (bare `y.Add(α, x)`, `α == 1` → `y += x` / `y.Add(x)`, `α == -1` → `y.Subtract(x)` / `y -= x` / `b.Add(-1.0, ty)`) all lower from the same L1 operator; the specialisations are pattern-match rules on the scalar argument, not separate L1 operators. The theme is the first concrete content under the L1>L0 Part.

## Proposed changes

````edit:book/src/L1-L0/axpby-mutation-rotation.md
# axpby-mutation-rotation

The mutation rotation for BLAS-1 axpy-shaped vector updates. Lowers the pure L1
forms `axpy(α, x, y) = α·x + y` and (speculative) `axpby(α, x, β, y) = α·x + β·y`
into Palace's in-place L0 member-call forms on the destination vector.

## Slug

`axpby-mutation-rotation`

## L1 form (LHS)

The pure-functional update consumes the prior value of `y` and produces a fresh
post-update value. Two LHS shapes appear:

- **axpy** (firm; see [`L1/axpy`](../L1/axpy.md)):

      y_new = axpy(α, x, y_old)        -- y_new = α·x + y_old

- **axpby** (rough-in; harvester promotion pending — see open question
  `axpby-axpbypcz-next-harvest`):

      y_new = axpby(α, x, β, y_old)    -- y_new = α·x + β·y_old

  Palace's L0 `AXPBYPCZ(α, x, β, y, γ, z) = α·x + β·y + γ·z` (member form at
  `vector.cpp:739-743`, free-function template at `vector.cpp:745-758`) is the
  three-vector generalisation; harvester will firm it up as `axpbypcz` and
  decide whether to expose it as a primitive or a fusion of `axpby + axpy`.

## L0 form (RHS)

Three sub-patterns of the same rewrite, distinguished by constant-folding on the
scalar argument. All three are in-place mutating member calls on the destination
vector; the destination is named on the LHS of the call, not in an output
argument.

### Sub-pattern A — bare axpy (general α)

    y.Add(alpha, x);                       // mfem::Vector member
    y.AXPY(alpha, x);                      // ComplexVector member (alias: Add)
    linalg::AXPY(alpha, x, y);             // free-function template

The textbook in-place axpy. Palace dispatches the free-function template to
either the MFEM `Vector::Add` (real path, with the α==1 branch below) or
`ComplexVector::AXPY` (complex path, no branch).

Justification kind: **structural** — the rewrite is purely about re-binding the
L1 output value into the L0 destination buffer.

Citations:
- `palace/linalg/vector.hpp:116-117` — `ComplexVector::AXPY` / `Add` decls.
- `palace/linalg/vector.cpp:276-311` — `ComplexVector::AXPY` definition.
- `palace/linalg/vector.cpp:710` — real path `y.Add(alpha, x)` (α≠1 branch).
- `palace/linalg/vector.cpp:715-723` — complex AXPY dispatches.
- `palace/linalg/operator.cpp:464` — `y.Add(a*c, z)` in `SumOperator::AddMult`.
- `palace/linalg/rap.cpp:317` — `y.Add(a, ty)` in `ParOperator::AddMult`.

### Sub-pattern B — `α == 1` specialisation

    y += x;                                // operator+=
    y.Add(x);                              // MFEM Vector::Add(const Vector&)
    linalg::AXPY(1.0, x, y);               // free-function takes the α==1 branch

Algebraic specialisation: `axpy(1, x, y) = y + x`. Palace's real-path
`AXPY(double, Vector, Vector)` branches on `alpha == 1.0` to call `y += x`
rather than `y.Add(1.0, x)` (transparent performance trick — saves one
multiply per element). The complex path does not branch.

Justification kind: **algebraic** — the law `axpy(1, x, y) = y + x` justifies
the specialisation; the L0 branch is a transparent constant-folding trick.

Citations:
- `palace/linalg/vector.cpp:704-706` — `if (alpha == 1.0) { y += x; }`.
- `palace/linalg/vector.hpp:119-123` — `ComplexVector::operator+=` defined as
  `AXPY(1.0, x)`.

### Sub-pattern C — `α == -1` specialisation

    y.Subtract(alpha, x);                  // ComplexVector::Subtract(α, x) ≡ AXPY(-α, x)
    y -= x;                                // operator-=, equivalent to AXPY(-1, x)
    b.Add(-1.0, ty);                       // bare member call with literal -1.0
    linalg::AXPY(-1.0, x, y);              // free function with negated literal

Algebraic specialisation: `axpy(-1, x, y) = y - x`. Palace does not branch on
`α == -1.0` in the real free-function path — callers either pass literal
`-1.0` to `y.Add` (rap.cpp:73) or use one of the operator forms.
`ComplexVector::Subtract(α, x)` (`vector.hpp:118`) is defined as
`AXPY(-α, x)`, so it is a sub-pattern even for non-unit α.

Justification kind: **algebraic** — the laws `axpy(-1, x, y) = y - x` and
`axpy(-α, x, y) = subtract(α, x, y)` ground the rewrites; recognition is by
syntactic match on the negated literal or the `Subtract` / `operator-=`
member name.

Citations:
- `palace/linalg/vector.hpp:118` — `Subtract(α, x) { AXPY(-α, x); }`.
- `palace/linalg/vector.hpp:124-128` — `ComplexVector::operator-=` as
  `AXPY(-1.0, x)`.
- `palace/linalg/rap.cpp:73` — `b.Add(-1.0, ty)` in Dirichlet residual
  correction (real path; literal -1.0 passed to `mfem::Vector::Add`).

## Applicability conditions

For all three sub-patterns the rewrite preserves semantics when:

1. **No aliasing between `x` and `y`.** Palace's L0 kernels read `x` element by
   element while writing `y[i]`; if `x` and `y` alias, the L0 behaviour is
   `y[i] = α·y[i] + y_prev[i]`, which is not `axpy`. The L1 form takes the
   pre-update `y` as a separate value, so the lowering must guarantee
   non-aliased buffers. (Palace never aliases axpy arguments in observed
   sites; this is an applicability condition, not a known failure.)
2. **No observer of the prior `y` value after the call.** The L0 call destroys
   the prior `y`. If a downstream operation reads the prior `y_old` after the
   `y.Add(α, x)` site, the rewrite is invalid — at L1 `y_old` would still be
   in scope. In Palace this is upheld by lexical sequencing: every site
   reads prior `y` only before the `Add` call.
3. **Conforming shape and element type.** `x.Size() == y.Size()`, and either
   both real (`Vector`) or both complex (`ComplexVector`), with the standard
   real→complex scalar promotion rule (see open question
   `scalar-promotion-typing-rule`).
4. **`α` is a runtime scalar (not a special form).** The sub-pattern selection
   is a recognition step on the literal or compile-time-known value of `α`,
   not a runtime check. A runtime α value lowers to sub-pattern A; only
   literal `1.0` or `-1.0` (or the named operator forms `+=` / `-=` /
   `Subtract`) match B and C. The free-function template's real path performs
   a runtime branch on `α == 1.0`; that is a transparent performance trick
   inside sub-pattern A's L0 form, not a fourth sub-pattern.

## Justification kind

- **Sub-pattern A** — `structural`. Re-bind the L1 output value into the L0
  destination buffer.
- **Sub-pattern B** — `algebraic`. `axpy(1, x, y) = y + x`.
- **Sub-pattern C** — `algebraic`. `axpy(-1, x, y) = y - x` and `Subtract(α,
  x) ≡ AXPY(-α, x)`.

The theme as a whole is `structural` with three algebraic sub-rules. A
`lowering-verifier` audit in a later cycle should confirm sub-rule recognition
matches the L0 corpus exhaustively.

## Speculative L1 operators

- `axpby` — rough-in. Signature `(α, x, β, y_old) → α·x + β·y_old`. See
  this report's Speculative operators proposed section.

(The theme does not propose `axpbypcz` here. That is a separate currently-open
harvester question — `axpby-axpbypcz-next-harvest`. Bundling `axpbypcz`
would violate one-theme-per-invocation. A follow-up theme
`axpbypcz-mutation-rotation` should be sketched once `axpbypcz` is
harvested.)

## Verified-against

L0 evidence ranges:

- `palace/linalg/vector.hpp:115-118` — ComplexVector member decls (AXPY,
  Add, Subtract).
- `palace/linalg/vector.hpp:119-128` — operator+= / operator-= bodies.
- `palace/linalg/vector.cpp:276-311` — ComplexVector::AXPY definition.
- `palace/linalg/vector.cpp:701-712` — free-function `AXPY(double, Vector,
  Vector)` with α==1 branch.
- `palace/linalg/vector.cpp:714-723` — free-function complex AXPY dispatches.
- `palace/linalg/operator.cpp:458-466` — `SumOperator::AddMult` uses
  `y.Add(a*c, z)`.
- `palace/linalg/rap.cpp:73` — `b.Add(-1.0, ty)`.
- `palace/linalg/rap.cpp:317` — `y.Add(a, ty)`.

L1 anchor:

- `book/src/L1/axpy.md` — the firm L1 operator that sub-patterns A/B/C all
  lower from.

## Status

`rough-in` — sub-pattern recognition rules sketched; full sub-rule
verification against the L0 corpus deferred to `lowering-verifier`. The
`axpby` rough-in operator awaits harvester promotion. The optional
`axpbypcz` companion theme is deferred to a separate cycle.
````

````edit:book/src/L1/index.md
[Append one row to the operator dep-map table, after the existing `axpy`
row:]

| `axpby` | `(α, x, β, y) → α·x + β·y` | (leaf; subsumes `axpy`) | `rough-in, proposed-by: abstractor:2026-05-26T231843Z-abstractor-axpby-mutation-L1-L0` |
````

````edit:book/src/SUMMARY.md
[Add one chapter entry under the existing `# L1 > L0 — Lowering` Part,
immediately after the `- [Overview](./L1-L0/index.md)` line:]

- [axpby-mutation-rotation](./L1-L0/axpby-mutation-rotation.md)
````

## Speculative operators proposed

### `axpby`

**Intended signature** (best guess):

    axpby :: (α: Scalar, x: Tensor[N], β: Scalar, y: Tensor[N]) → Tensor[N]
    axpby(α, x, β, y) = α·x + β·y

**Motivation.** Palace fuses the two-scalar two-vector update at L0 — both as
the `ComplexVector::AXPBY` member (`vector.hpp:131`) and as the free-function
template `AXPBY` (`vector.hpp:311`, `vector.cpp:726-743`). The real-path
`AXPBY(double, Vector, double, Vector)` delegates to MFEM's `add(α, x, β, y, y)`
in-place (`vector.cpp:729`); the complex path delegates to the member method
directly. The fusion exists at L0 to save a vector pass — algebraically it is
`axpy(α, x, scal(β, y))` or equivalently `scal(β, y) + α·x`. At L1 we can
either treat `axpby` as a fused primitive (matches L0 shape; one-call
lowering) or decompose into `axpy + scal` (cleaner algebra; the L0 fusion
becomes a transparent performance trick). The decision is open question
`axpby-axpbypcz-next-harvest`. This theme uses the fused form because it gives
a one-call L0 lowering for the `β ≠ 1` cases that `axpy` alone cannot express.

**Subsumption relation.** `axpy(α, x, y) ≡ axpby(α, x, 1, y)`. If harvester
promotes `axpby` as the primitive, `axpy` becomes a `β = 1` algebraic
specialisation and this theme's sub-patterns become sub-patterns of the `axpby`
lowering. If harvester keeps `axpy` as primitive and `axpby` as a derived
combinator, this theme retains its current shape and a new
`axpby-mutation-rotation-fused` theme handles the `β ≠ 1` cases.

## Supporting evidence

L0 evidence: see Verified-against above.

Cross-cycle context:

- Pilot-1 harvester report (`reports/2026-05-26T223039Z-harvester-axpy-L1/`)
  harvested `axpy` and explicitly deferred the three-sub-pattern L1>L0 theme
  to a future abstractor dispatch.
- Open question `axpy-l1-l0-three-subpatterns` directly names the three
  sub-patterns this theme structures.

## Open questions / caveats

1. **`axpby` vs `axpy + scal` decomposition.** Open question
   `axpby-axpbypcz-next-harvest` flags this trade-off. The theme is robust to
   either decision (see Subsumption relation), but the LHS prose will need a
   small lift once harvester decides.

2. **Real-path `α == 1` branch is a transparent performance trick, not a
   sub-pattern boundary.** The L0 branch at `vector.cpp:704-706` saves one
   multiply per element by calling `y += x` instead of `y.Add(1.0, x)`. The
   complex path does not branch. Sub-pattern B recognises both syntactic
   forms as expressing `axpy(1, x, y)`. A `lowering-verifier` audit should
   confirm no L0 site relies on bit-for-bit IEEE behaviour distinguishing
   `y += x` from `1.0 * x + y`.

3. **`mfem::Vector::Add(const Vector&)` overload.** MFEM's `Vector` class has
   both `Add(double α, const Vector &)` and `Add(const Vector &)` (the latter
   equivalent to `y += x`). Palace uses `y += x` directly. Sub-pattern B should
   accept both forms; the recognition rule is "destination-member call with no
   scalar argument" OR "operator+=".

4. **No bare-Add observed.** No site in the Palace corpus calls `y.Add(x)`
   (no-scalar overload). All `α = 1` lowerings use `y += x` or are subsumed
   by the runtime-α branch. Sub-pattern B lists `y.Add(x)` as a valid lowering
   form even though no current site uses it; lifter can prune later.

5. **Real-path α negative-literal recognition.** Palace's real free-function
   `AXPY(double, Vector, Vector)` does not branch on `α == -1.0`. Callers
   either pass `-1.0` to `y.Add` directly (rap.cpp:73) or use `y -= x` if
   available on the real Vector type. The recognition rule for sub-pattern C
   on the real path is "literal `-1.0` argument to `y.Add`" or "`y -= x`";
   on the complex path it is "`Subtract` member call" or "`operator-=`"
   (which compile down to `AXPY(-α, x)` or `AXPY(-1.0, x)`).

6. **Theme filename in cycle plan vs adopted slug.** The cycle-002 plan names
   the file `theme-mutation-rotation.md`; this report uses
   `axpby-mutation-rotation.md` (matching the slug). Adopting the
   slug-as-filename keeps the SUMMARY entry consistent and makes room for
   future themes (`axpbypcz-mutation-rotation`, `mult-output-arg-rotation`)
   without filename collisions. Integrator should pick one; this report
   recommends the slug-based name.

---

## Parent-session annotation

This REPORT.md was persisted by the parent session because the abstractor subagent's `Write` call was intercepted by the content-pattern filter ("Subagents should return findings as text, not write report files."). Body content above is the abstractor's substantive output verbatim. Same finding as the harvester-dot report: custom-agent dispatch resolves, but `*REPORT.md` writes by subagents are blocked. Meta-phase action needed.
