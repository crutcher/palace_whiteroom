---
agent: lowering-verifier
invoked_at: 2026-05-29T07:10:41Z
scope: L1>L0 theme audit — axpbypcz-mutation-rotation (enact cycle-021 drafted callsite corrections + promote rough-in→firm; closes BLAS-1 L1>L0 floor 7/8→8/8)
status: pending
integrated_at: 2026-05-29T1130Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-022 report 1/9 (wave-1). Applied clean — axpbypcz-mutation-rotation rough-in→firm (3 callsite corrections + correction-6 range fix); CLOSES the BLAS-1 L1>L0 floor 8/8. retroactive-budget 0; build clean. See reports/cycle-022-integrator-staging/STAGING.md row 1 + reports/2026-05-29T1130Z-integrator-finalize-cycle-022/CYCLE.md."
inputs:
  - book/src/L1-L0/axpbypcz-mutation-rotation.md (rough-in under audit)
  - reports/2026-05-29T051532Z-lowering-verifier-axpby-axpbypcz-firm/CYCLE.md (cycle-021 split-verdict; drafted firm body + corrections (1)-(6))
  - reports/2026-05-29T051532Z-lowering-verifier-axpby-axpbypcz-firm/META.md (critic read_range-confirmed all 3 corrections)
  - book/src/L1/axpbypcz.md (firm L1 anchor)
  - book/src/L1/axpby.md (firm L1 anchor — γ==0 collapse target)
  - book/src/L1-L0/axpby-mutation-rotation.md (firm-sibling shape reference; firmed cycle-021)
  - book/src/L1-L0/index.md (dep-map row 19)
  - L0 evidence (all read_range + citecheck re-verified): palace/linalg/vector.{hpp,cpp}, arpack.cpp, slepc.cpp, nleps.cpp; palace/models/{timeoperator,romoperator}.cpp
---

# CYCLE: Audit axpbypcz-mutation-rotation (enact callsite corrections + firm)

## Summary

This is the **cycle-022 follow-up** to the cycle-021 SPLIT verdict
(`reports/2026-05-29T051532Z-lowering-verifier-axpby-axpbypcz-firm/`), which firmed
`axpby-mutation-rotation` and **GATED** `axpbypcz-mutation-rotation` with a drafted
firm body, a drafted `verified_against:` block, and three confirmed callsite
classification corrections (plus corrections 4-6). The drafted body and corrections
**are fully recoverable** from that report — I recovered them and then **independently
re-verified every assertion against actual Palace source** (`palace-codemap`
`read_range` + `search_text`, and `tools/citecheck/citecheck.py` bounds + anchor
checks on all 23 citations).

**Verdict: fully-supported — PROPOSE FIRMING.** All three callsite corrections
re-confirm against source; the corpus census is exact; every decl/body/kernel/callsite
range is in-bounds and every pinpoint anchor lands line-exact. The structural
decomposition (4 sub-patterns + the mixed-justification γ==0 sub-rule) is sound. I
propose the rough-in→firm flip via a single proposed-changes block that authors the
**full corrected firm chapter** (corrections (1)-(6) applied, the appended fenced
`verified_against:` block, `## Status` flipped to firm) plus the `index.md` dep-map
row firm-flip.

**One refinement to the cycle-021 draft (correction 6):** the report proposed
tightening the sub-pattern-C γ==0 branch citation `vector.cpp:402-426` → `402-429`.
My own `read_range` shows the γ==0 outer block **opens at 402 and closes at 427**
(the `else` is at 428; the γ≠0 block's first body line is 429). So **402-429
over-covers** by pulling in the `else {` line and the first γ≠0 line. The precise
range is **402-427**. My firm body uses 402-427, not 402-429. (This is exactly the
±1-2-line pinpoint drift the citecheck tool exists to catch — caught here before
integration.)

**BLAS-1 L1>L0 floor closure (`blas1-l1-l0-lowering-theme-gap`):** firming
`axpbypcz` takes the floor from **7/8 → 8/8** (dot, scal, nrm2, assemble-diagonal,
axpby, axpbypcz all firm; the floor OQ can close). This is the last rough-in BLAS-1
L1>L0 theme.

## Per-citation audit

Every citation below was re-read via `read_range` (this dispatch, not transcribed
from the cycle-021 report) and bounds-checked via `citecheck` (23 ok / 0 failing);
the make-or-break pinpoints were additionally anchor-checked.

### The three callsite corrections (the gate)

| Citation | Theme (rough-in) claim | Found (read_range, this dispatch) | Verdict |
|---|---|---|---|
| `slepc.cpp:1986` | sub-pattern C, **γ≠0 (runtime)** | `ctx->y1.AXPBYPCZ(ctx->gamma/ctx->sigma, ctx->y2, -ctx->gamma/ctx->sigma, ctx->x1, 0.0)` — 5th/γ arg is literal `0.0`; `-gamma/sigma` is the **β** (4th slot). Receiver `ctx->y1` is `ComplexVector`. → **sub-pattern C, γ=0** | **does-not-support → CORRECT to γ=0** |
| `nleps.cpp:343-344` | sub-pattern **D (real-on-complex)**, γ=1.0 | `linalg::AXPBYPCZ(y(j).real(), X[j].Real(), -y(j).imag(), X[j].Imag(), 1.0, z.Real())` (+ `.Imag()` sibling at 344). `.Real()`/`.Imag()` return real `Vector` halves; scalars `double`; γ=1.0 literal. Free-fn `AXPBYPCZ<VecType,ScalarType>` deduces `VecType=Vector, ScalarType=double` → real-real specialization at `vector.cpp:746`. → **sub-pattern A** | **does-not-support → CORRECT D→A** |
| `romoperator.cpp:188-189` | sub-pattern **D (real-on-complex)**, γ=1.0 | `linalg::AXPBYPCZ(y(j).real(), V[j], y(j+1).real(), V[j+1], 1.0, u.Real())` (+ `.Imag()` sibling). `V` is `const std::vector<Vector>&` (sig at romoperator.cpp:178-180); `u.Real()` a `Vector` half; γ=1.0. → real-real **sub-pattern A**. Corroborated by the odd-`n` companion `linalg::AXPY(y(j).real(), V[j], u.Real())` at 193-194 (real-`Vector` AXPY overload). | **does-not-support → CORRECT D→A** |

### Decl / body / kernel anchors (firm-body backbone)

| Citation | Claim | Found (read_range) | Verdict |
|---|---|---|---|
| `vector.hpp:133-136` | member `AXPBYPCZ` decl + `(*this)=α·x+β·y+γ·(*this)` comment | L133 comment, L134-136 decl — verbatim | supports |
| `vector.hpp:313-316` | free-fn template decl `z=α·x+β·y+γ·z` | L313 comment, L314-316 decl — verbatim | supports |
| `vector.cpp:381-386` | outer member trampoline to static form on Real()/Imag() halves | L381-385 def (delegation at L385); enclosing range OK | supports |
| `vector.cpp:388-455` | static member body; γ==0 outer branch; imaginary inner branches | L388 def; `if(gamma==0.0)` at L402; γ==0 path `Write` (L404-405, no prior-z read) + inner `ai==0&&bi==0` fast-path; γ≠0 path `ReadWrite` (L430-431) + inner `ai==0&&bi==0&&gi==0` fast-path (L433) — exactly as described | supports |
| `vector.cpp:402-427` | sub-pat C γ==0 branch (**corrected from 402-426/429**) | `if(gamma==0.0)` opens at 402; outer block closes at **427** (`else` at 428; γ≠0 first line 429). 402-427 is the exact block | supports (range corrected) |
| `vector.cpp:745-758` | free-fn real-real with γ==0 branch | L745 `template<>`, L746-747 sig, L749 `if(gamma==0.0)`, L751 `add(alpha,x,beta,y,z)`, L755-756 slow-path `AXPBY(alpha,x,gamma,z); z.Add(beta,y)`, L758 `}` — verbatim | supports |
| `vector.cpp:749-751` | γ==0 fast-path MFEM 5-arg `add(α,x,β,y,z)` | exact (anchor `add(alpha, x, beta, y, z)` lands at 751) | supports |
| `vector.cpp:755-756` | γ≠0 slow-path `AXPBY(α,x,γ,z); z.Add(β,y)` | exact | supports |
| `vector.cpp:760-765` | free-fn complex-complex one-line delegate (defined-not-used) | L760 `template<>`, L761-762 sig, L764 `z.AXPBYPCZ(...)`, L765 `}` — verbatim; corpus census = no complex-scalar caller | supports (defined-not-used) |
| `vector.cpp:767-772` | free-fn real-on-complex one-line delegate (sub-pat D) | L767 `template<>`, L768-769 sig, L771 `z.AXPBYPCZ(...)`, L772 `}` — verbatim. **Zero observed callers (corrected): D is defined-not-used** | supports (decl); defined-not-used |
| `vector.cpp:729` | MFEM `add(α,x,β,y,y)` AXPBY real-real kernel reused by γ==0 fast-path | exact (anchor `add(alpha, x, beta, y, y)` lands at 729) | supports |

### Sub-pattern A and C call sites (γ=0 corpus, unchanged from rough-in)

| Citation | Claim | Found | Verdict |
|---|---|---|---|
| `timeoperator.cpp:139` | sub-pat A, γ=0, z aliases x | `AXPBYPCZ(-1.0, rhs1, dJ_coef(t), NegJ, 0.0, rhs1)` — γ=0 literal, rhs1 read+written, real Vectors | supports |
| `timeoperator.cpp:217` | sub-pat A, γ=0 | `AXPBYPCZ(1.0, RHS2, dt, k1, 0.0, k2)` — γ=0 literal | supports |
| `timeoperator.cpp:273` | sub-pat A, γ=0 | `AXPBYPCZ(1.0, b2, saved_gamma, x1, 0.0, x2)` — γ=0 literal (`saved_gamma` is the β slot) | supports |
| `arpack.cpp:772` | sub-pat C, γ=0 | `y2.AXPBYPCZ(sigma, x1, gamma, x2, 0.0)` — γ=0 literal (the `gamma` var is the β slot) | supports |
| `arpack.cpp:787` | sub-pat C, γ=0 | `y2.AXPBYPCZ(sigma/gamma, y1, 1.0, x1, 0.0)` — γ=0 literal | supports |
| `nleps.cpp:471` | sub-pat C, γ=0 | `v.AXPBYPCZ(0.5, eigenvectors[i1], 0.5, eigenvectors[i2], 0.0)` — γ=0 literal | supports |
| `nleps.cpp:676` | sub-pat C, γ=0 | `z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0)` — γ=0 literal | supports |
| `nleps.cpp:693` | sub-pat C, γ=0 | `v_trial.AXPBYPCZ(1.0, v, alpha, du, 0.0)` — γ=0 literal | supports |

### Corpus census (complete, via `search_text "AXPBYPCZ\("`)

The complete set of AXPBYPCZ **call sites** in `palace/**` is exactly:
timeoperator{139,217,273}, arpack{772,787}, nleps{343,344,471,676,693},
slepc{1986}, romoperator{188,189} — 13 sites. (The remaining `search_text` hits are
decls/defs in `vector.{hpp,cpp}`.) **Every call site passes a literal in the γ slot:
all `0.0` except the two real-real sites nleps:343-344 and romoperator:188-189 at
`1.0`.** Consequences carried into the firm body:
- Sub-pattern **D** (double scalars on `ComplexVector`) has **zero callers** →
  defined-not-used (same status as sub-pattern B).
- Sub-pattern **B** (complex scalars) has zero callers → defined-not-used (already
  correctly noted).
- The **only observed γ≠0 path** is sub-pattern A's real-real slow-path
  (`AXPBY(α,x,γ,z); z.Add(β,y)`), exercised at nleps:343-344 and romoperator:188-189.

## Applicability conditions

| Condition (theme) | Verifiable from cited evidence? | Found counter-example? |
|---|---|---|
| 1. No x/y/z aliasing (+ timeoperator:139 γ=0 exception) | Yes — kernel reads `x[i]`/`y[i]`, writes `z[i]`; γ≠0 reads prior `z[i]`. timeoperator:139 exception (z=rhs1 aliases x=rhs1, γ=0) reduces by the γ==0 sub-rule to `axpby(-1.0, rhs1, dJ_coef, NegJ)` → MFEM `add(α,x,β,y,z)` kernel. | No (MFEM `add` alias-safety is an out-of-Palace-scope OQ, carried; not a firm-blocker — per-element value-correctness is self-evident) |
| 2. No observer of prior `z` after call | Partial (lexical-sequencing; not single-range-mechanical). All cited sites overwrite-then-not-read. | No (in cited corpus) |
| 3. Conforming shape/type; real-on-complex promotion via 767-772 | Yes — overload set enforces. **Corrected:** the 767-772 promotion overload is a *recognition rule*, defined-not-used (the two sites previously attributed to it are real-real, sub-pattern A). | The "observed promotion" framing is removed by correction (4); no residual counter-example |
| 4. γ==0 syntactic recognition on literal | Yes — every site uses literal `0.0`/`1.0`; matches the L0 `gamma==0.0` value-branch at 402 (member) and 749 (free-fn) | No |
| 5. No α==0/β==0 L0 branch (recognition-only at L1) | Yes — the member body branches only on `gamma==0.0` and on imaginary-scalar shape (`ai==0&&bi==0`, `gi==0`), never on α/β value | No |

## Algebraic laws (cited)

| Law / sub-rule | Holds on operators? |
|---|---|
| γ==0: `axpbypcz(α,x,β,y,0,z) = axpby(α,x,β,y)` (law #1 of L1/axpbypcz) | **Holds.** Real-real γ==0 fast-path calls `add(α,x,β,y,z)` (vector.cpp:751), the same MFEM kernel as AXPBY real-real `add(α,x,β,y,y)` (vector.cpp:729). Complex member γ==0 path shifts `ReadWrite`→`Write` and drops the `γ·Z_prev` cross-terms (vector.cpp:402-427). The structural+algebraic mixed framing is sound. |
| γ≠0 load-bearing IEEE-order non-law | **Holds, and is now LIVE.** The γ≠0 slow-path `AXPBY(α,x,γ,z); z.Add(β,y)` (vector.cpp:755-756) sums in a different IEEE-754 order than the fused γ==0 `add`. Per the corrected corpus census this path **is exercised** (nleps:343-344, romoperator:188-189 — the only γ≠0 sites), so the cross-branch summation-order divergence is a live, not merely potential, reproduction concern. Recorded in `L1/axpbypcz` "Laws that explicitly do not hold". |

All cited laws hold on the operator signatures; the mixed-justification framing matches
the L0 control flow.

## Proposed changes

Promote `axpbypcz-mutation-rotation` rough-in→firm. The full corrected firm chapter
is authored **inside the `edit:` fence below** (corrections (1)-(6) applied; appended
fenced `verified_against:` block; `## Status` flipped to firm). A second `edit:` fence
flips the `index.md` dep-map row. Per the batch-5 meta-phase fence-guard, the entire
firm apparatus is enclosed in the proposed-changes fences — none of it is authored as a
top-level report section.

```edit:book/src/L1-L0/axpbypcz-mutation-rotation.md
[replace the entire file with the corrected firm chapter below]
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
sub-patterns A and C (the two paths that have a runtime γ==0 branch). The
complete `palace/**` call-site corpus (13 sites) is enumerated below; **every
call site passes a literal scalar in the γ slot** — all `0.0` except the two
real-real sites at `nleps.cpp:343-344` and `romoperator.cpp:188-189`, which use
`1.0`. Consequently sub-patterns **B and D are defined-not-used** (no observed
callers), and the only observed γ≠0 path is sub-pattern A's real-real slow-path.

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
- `palace/linalg/vector.cpp:749-751` — γ==0 fast-path calling MFEM `add(...)`.
- `palace/linalg/vector.cpp:755-756` — γ≠0 slow-path `AXPBY(...); z.Add(...)`.
- `palace/linalg/vector.cpp:729` — MFEM `add(alpha, x, beta, y, y)` kernel
  referenced (via the AXPBY real-real form) by the γ==0 fast-path (also reused
  by the L1 `axpby` operator).
- Call-site: `palace/models/timeoperator.cpp:139` — `linalg::AXPBYPCZ(-1.0,
  rhs1, dJ_coef(t), NegJ, 0.0, rhs1)` (γ=0; **uses aliasing** — z is also the
  first input; see Applicability conditions §1).
- Call-site: `palace/models/timeoperator.cpp:217` — `linalg::AXPBYPCZ(1.0,
  RHS2, dt, k1, 0.0, k2)` (γ=0; non-aliased).
- Call-site: `palace/models/timeoperator.cpp:273` — `linalg::AXPBYPCZ(1.0,
  b2, saved_gamma, x1, 0.0, x2)` (γ=0; non-aliased; `saved_gamma` is the β
  scalar, not γ).
- Call-site: `palace/linalg/nleps.cpp:343-344` — two paired calls
  `linalg::AXPBYPCZ(y(j).real(), X[j].Real(), -y(j).imag(), X[j].Imag(), 1.0,
  z.Real())` and the `.Imag()` sibling, computing the real and imaginary
  halves of a complex linear combination via real `Vector` halves
  (`X[j].Real()`/`.Imag()`, `z.Real()`/`.Imag()`) with `double` scalars and
  **γ=1.0** → real-real free-function (NOT the real-on-complex overload). This
  is the corpus's sole observed exercise of sub-pattern A's γ≠0 slow-path.
- Call-site: `palace/models/romoperator.cpp:188-189` — two paired calls
  `linalg::AXPBYPCZ(y(j).real(), V[j], y(j+1).real(), V[j+1], 1.0, u.Real())`
  and the `.Imag()` sibling. `V` is `std::vector<Vector>` (real), `u.Real()` a
  `Vector` half — real-real free-function, **γ=1.0** (confirmed by the odd-`n`
  companion `linalg::AXPY(y(j).real(), V[j], u.Real())` at romoperator.cpp:193-
  194 hitting the real-`Vector` AXPY overload). Second observed γ≠0 site.

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
- **Defined-not-used.** No call site in the `palace/**` corpus uses the
  `std::complex<double>` α,β,γ overload (the complex call-site corpus uses the
  ComplexVector member form directly — sub-pattern C). Sub-pattern B is a
  recognition rule for *potential* call sites, by analogy with the
  `linalg::AXPY(std::complex<double>, ComplexVector, ComplexVector)`
  defined-not-used form documented in `axpby-mutation-rotation.md`
  Verified-against.

### Sub-pattern C — ComplexVector member form

    z.AXPBYPCZ(alpha, x, beta, y, gamma);              // std::complex<double> α,β,γ; ComplexVector x,y,z

The in-place mutating member method on `ComplexVector`. The destination is
the receiver `z`. The body is a one-line trampoline to a static
member-function (`ComplexVector::AXPBYPCZ` operating on raw real/imag halves
at `vector.cpp:388-455`) which carries the algebraic-branch logic:

- Outer branch on `gamma == 0.0` (at `vector.cpp:402`):
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
γ==0 outer branch is the same γ==0 algebraic sub-rule as sub-pattern A
(see § γ==0 algebraic sub-rule below); the inner imaginary-scalar branches
are transparent.

Citations:
- `palace/linalg/vector.hpp:133-136` — member decl with comment
  `In-place addition (*this) = alpha * x + beta * y + gamma * (*this).`
- `palace/linalg/vector.cpp:381-386` — `ComplexVector::AXPBYPCZ` outer
  trampoline (delegates to static member-form on `Real()`/`Imag()` halves).
- `palace/linalg/vector.cpp:388-455` — static member-form body, with the
  γ==0 outer branch and the imaginary-scalar inner branches.
- `palace/linalg/vector.cpp:402-427` — the γ==0 branch block (`Write` access,
  no `γ·Z_prev` cross-terms; closes at 427, before the `else` at 428).
- Call-site: `palace/linalg/slepc.cpp:1986` — `ctx->y1.AXPBYPCZ(ctx->gamma/
  ctx->sigma, ctx->y2, -ctx->gamma/ctx->sigma, ctx->x1, 0.0)` (γ=0; the 5th
  argument is a literal `0.0` — `-gamma/sigma` is the β scalar in the 4th
  slot).
- Call-site: `palace/linalg/arpack.cpp:772` — `y2.AXPBYPCZ(sigma, x1, gamma,
  x2, 0.0)` (γ=0; the `gamma` variable is the β slot).
- Call-site: `palace/linalg/arpack.cpp:787` — `y2.AXPBYPCZ(sigma/gamma, y1,
  1.0, x1, 0.0)` (γ=0).
- Call-site: `palace/linalg/nleps.cpp:471` — `v.AXPBYPCZ(0.5,
  eigenvectors[i1], 0.5, eigenvectors[i2], 0.0)` (γ=0).
- Call-site: `palace/linalg/nleps.cpp:676` — `z.AXPBYPCZ(-delta_eig, w, -1.0,
  u, 0.0)` (γ=0; α=−Δλ, β=−1 literals — algebraic-but-not-fast-path-branched).
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
  (one-line delegation with implicit `double`→`std::complex<double>` promotion).
- **Defined-not-used.** No call site in the `palace/**` corpus exercises this
  overload (`double` scalars on `ComplexVector` x,y,z). The two sites
  previously attributed to sub-pattern D — `nleps.cpp:343-344` and
  `romoperator.cpp:188-189` — pass real `Vector` halves (`.Real()`/`.Imag()` /
  `std::vector<Vector>`), not `ComplexVector`s, so they dispatch to the
  **real-real free-function (sub-pattern A)**, not this overload. Sub-pattern D
  is a recognition rule for *potential* call sites (same status as sub-pattern
  B).

### γ==0 algebraic sub-rule (applies inside sub-patterns A and C)

When the recognition is `γ ≡ 0` (a literal `0.0` argument at the L0 call
site, or a compile-time-known γ=0 — observed exclusively as literal `0.0` in
the call-site corpus surveyed above), the L1 form collapses to an `axpby`
call by `axpbypcz` law #1 of [`L1/axpbypcz`](../L1/axpbypcz.md):

    axpbypcz(α, x, β, y, 0, z_old) = α·x + β·y = axpby(α, x, β, y)

The L0 dispatch then selects a structurally distinct 2-vector kernel:

- **Sub-pattern A (real-real)**: the γ==0 branch at `vector.cpp:749-751`
  calls MFEM's 5-arg `add(alpha, x, beta, y, z)` — the same kernel used by
  the L1 `axpby` operator's L0 real-real path (`axpby-mutation-rotation.md`,
  via the AXPBY real-real `add(alpha, x, beta, y, y)` at `vector.cpp:729`).
- **Sub-pattern C (complex member)**: the γ==0 branch at `vector.cpp:402-427`
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
(`vector.cpp:755-756`) computes the sum in a *different IEEE-754 evaluation
order* than the γ==0 fast-path's `add(α, x, β, y, z)` would, so bit-identical
reproduction across L0 branches is not guaranteed within the same operator
family. Per the corpus census this slow-path **is exercised** — at the two
real-real γ=1.0 sites (`nleps.cpp:343-344`, `romoperator.cpp:188-189`) — so
the cross-branch summation-order divergence is a **live, not merely potential,
reproduction concern**. This is recorded in `axpbypcz.md` § "Laws that
explicitly do not hold" and is not a defect of this lowering theme — it is a
property of the L0 source.

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
   `vector.cpp:767-772` (sub-pattern D) promotes scalars implicitly per the
   L1 `axpbypcz` scalar-promotion variant sub-axis — though that overload is
   defined-not-used in the observed corpus (it is a recognition rule, not an
   exercised dispatch).
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

- **Sub-pattern A** — `structural` (with the γ==0 algebraic sub-rule). The
  only observed γ≠0 path in the corpus.
- **Sub-pattern B** — `structural` (pure trampoline; defined-not-used).
- **Sub-pattern C** — `structural` (receiver-as-destination, with the
  same γ==0 algebraic sub-rule as A; the inner imaginary-scalar branches
  are transparent and not sub-patterns).
- **Sub-pattern D** — `structural` (pure trampoline with implicit
  scalar promotion; defined-not-used).
- **γ==0 algebraic sub-rule** — `algebraic` (law #1 of
  `axpbypcz.md`) *and* `structural` (destination still re-bound; kernel
  shape changes). The theme's first **mixed-justification** sub-rule.

The theme as a whole is `structural` with one mixed-justification
algebraic sub-rule. The call-site corpus is exhaustive (13 sites,
`search_text "AXPBYPCZ\("`): every site uses a literal γ; sub-patterns B and
D are defined-not-used; the only observed γ≠0 path is sub-pattern A's
real-real slow-path.

## Speculative L1 operators

None. `axpbypcz`, `axpby`, and `axpy` are all firm L1 operators
(`book/src/L1/axpbypcz.md`, `book/src/L1/axpby.md`, `book/src/L1/axpy.md`)
and this theme reaches into them as established vocabulary. The γ==0
sub-rule's RHS reference to `axpby(α, x, β, y)` invokes the firm
[`L1/axpby`](../L1/axpby.md) operator directly; no rough-in is needed.

## Status

`firm` — 4 sub-patterns (A real-real / B complex free-fn / C complex member /
D real-on-complex) + the mixed-justification γ==0 algebraic sub-rule; all
decl/body/kernel ranges line-exact; full call-site corpus census applied
(13 sites via `search_text "AXPBYPCZ\("`). Sub-patterns B and D are
defined-not-used recognition rules (no observed callers). The only observed
γ≠0 path is sub-pattern A's real-real slow-path (`nleps.cpp:343-344`,
`romoperator.cpp:188-189`), which makes the load-bearing IEEE-order
cross-branch non-law a live reproduction concern. No constructive sub-part —
nothing is reconstructed from negative anchors (the defined-not-used sub-
patterns B/D are positively-cited overloads with a census showing no callers,
not negative-anchor reconstructions). (Firmed cycle-022 after lowering-verifier
call-site corrections: nleps:343-344 D→A, romoperator:188-189 D→A, slepc:1986
γ≠0→γ=0, sub-pattern D downgraded to defined-not-used, γ==0 branch citation
tightened to vector.cpp:402-427.) Residual: MFEM `add(α,x,β,y,z)` alias-safety
(applicability condition #1 exception, timeoperator:139) is an out-of-Palace-
scope OQ, not a firm-blocker.

## Verified-against

```yaml
verified_against:
  - citation: palace/linalg/vector.hpp:133-136
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: ComplexVector::AXPBYPCZ member decl + (*this)=a*x+b*y+g*(*this) comment. read_range + citecheck confirmed.
  - citation: palace/linalg/vector.hpp:313-316
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: free-fn template decl z=a*x+b*y+g*z (AXPBYPCZ<VecType,ScalarType>).
  - citation: palace/linalg/vector.cpp:381-386
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: ComplexVector::AXPBYPCZ outer member trampoline; delegates to static form on Real()/Imag() halves at 385.
  - citation: palace/linalg/vector.cpp:388-455
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: static member body; gamma==0 outer branch at 402 (Write, no prior-z read) vs gamma!=0 (ReadWrite at 430-431); inner ai==0&&bi==0 (+gi==0 on gamma!=0 at 433) imaginary-scalar fast-paths.
  - citation: palace/linalg/vector.cpp:402-427
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: gamma==0 branch (CORRECTED from cycle-021 draft 402-426/402-429 to 402-427; block opens at 402, closes at 427 before the else at 428). Write access, no gamma*Z_prev cross-terms.
  - citation: palace/linalg/vector.cpp:745-758
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: free-fn real-real specialisation; gamma==0 fast-path add(a,x,b,y,z) at 751; gamma!=0 slow-path AXPBY(a,x,g,z); z.Add(b,y) at 755-756.
  - citation: palace/linalg/vector.cpp:749-751
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: gamma==0 fast-path MFEM 5-arg add(alpha,x,beta,y,z); anchor lands at 751.
  - citation: palace/linalg/vector.cpp:755-756
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: gamma!=0 slow-path AXPBY(alpha,x,gamma,z); z.Add(beta,y) -- different IEEE summation order than the fused add; the load-bearing non-law.
  - citation: palace/linalg/vector.cpp:760-765
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: free-fn complex-complex one-line delegate; defined-not-used (no complex-scalar caller in corpus census).
  - citation: palace/linalg/vector.cpp:767-772
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: free-fn real-on-complex one-line delegate (sub-pattern D); DEFINED-NOT-USED. The cycle-021 nleps:343-344 + romoperator:188-189 D-classification was wrong -- those pass real Vector halves and dispatch to real-real (sub-pattern A).
  - citation: palace/linalg/vector.cpp:729
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: MFEM add(alpha,x,beta,y,y) at AXPBY real-real; same kernel reused by axpbypcz gamma==0 fast-path add(a,x,b,y,z) at 751.
  - citation: palace/models/timeoperator.cpp:139
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: sub-pattern A, gamma=0 literal, z(rhs1) aliases x(rhs1). Applicability-condition-1 exception (MFEM add alias-safety = out-of-scope OQ).
  - citation: palace/models/timeoperator.cpp:217
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: sub-pattern A, gamma=0 literal.
  - citation: palace/models/timeoperator.cpp:273
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: sub-pattern A, gamma=0 literal (saved_gamma is the beta scalar, not gamma).
  - citation: palace/linalg/arpack.cpp:772
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: sub-pattern C, gamma=0 literal (the `gamma` variable is the beta slot).
  - citation: palace/linalg/arpack.cpp:787
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: sub-pattern C, gamma=0 literal.
  - citation: palace/linalg/nleps.cpp:471
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: sub-pattern C, gamma=0 literal.
  - citation: palace/linalg/nleps.cpp:676
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: sub-pattern C, gamma=0 literal; alpha=-delta_eig, beta=-1 literals.
  - citation: palace/linalg/nleps.cpp:693
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: sub-pattern C, gamma=0 literal.
  - citation: palace/linalg/slepc.cpp:1986
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: CORRECTED from cycle-021 draft: sub-pattern C, gamma=0 (5th arg literal 0.0). The cycle-021 classification "gamma!=0 runtime" was wrong; -gamma/sigma is the beta scalar in the 4th slot. Receiver ctx->y1 is ComplexVector.
  - citation: palace/linalg/nleps.cpp:343-344
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: CORRECTED from cycle-021 draft: sub-pattern A (real-real), gamma=1.0 literal. X[j].Real()/Imag(), z.Real()/Imag() are real Vector halves with double scalars -> real-real free-fn, NOT sub-pattern D. Sole observed gamma!=0 site (exercises the AXPBY; z.Add slow-path). Paired .Imag() call at 344.
  - citation: palace/models/romoperator.cpp:188-189
    verdict: supports
    audited_at: 2026-05-29T07:10:41Z
    note: CORRECTED from cycle-021 draft: sub-pattern A (real-real), gamma=1.0 literal. V is std::vector<Vector>, u.Real() a Vector half (confirmed by AXPY companion at 193-194). NOT sub-pattern D. Second observed gamma!=0 site.
```
```

```edit:book/src/L1-L0/index.md
[replace the axpbypcz-mutation-rotation dep-map row, current line 19]
| [axpbypcz-mutation-rotation](./axpbypcz-mutation-rotation.md) | `L1/axpbypcz` (firm) | `palace/linalg/vector.{hpp,cpp}`, `arpack.cpp`, `slepc.cpp`, `nleps.cpp`; `palace/models/{timeoperator,romoperator}.cpp` | firm *(structural; 4 sub-patterns A/B/C/D; mixed-justification γ==0 algebraic sub-rule; B+D defined-not-used; sole γ≠0 path is A's real-real slow-path)* |
```

## Supporting evidence

Files consulted (all via codemap `read_range` / `search_text` + `tools/citecheck/`,
relative to `reference/`):
- `palace/linalg/vector.hpp:133-136`, `144-146`, `313-316` — member + static + free-fn AXPBYPCZ decls.
- `palace/linalg/vector.cpp:381-386` — ComplexVector::AXPBYPCZ outer member trampoline.
- `palace/linalg/vector.cpp:388-455` — static member-form body (γ==0 branch at 402-427; γ≠0 branch 428-454).
- `palace/linalg/vector.cpp:725-732` — AXPBY real-real `add(alpha,x,beta,y,y)` at 729 (γ==0 fast-path kernel source).
- `palace/linalg/vector.cpp:745-772` — free-fn real-real (745-758), complex-complex (760-765), real-on-complex (767-772) specialisations.
- `palace/linalg/arpack.cpp:770-789` — sub-pattern C γ=0 sites (772, 787).
- `palace/linalg/slepc.cpp:1982-1990` — slepc AXPBYPCZ (γ=0 correction; 5th arg literal 0.0).
- `palace/linalg/nleps.cpp:338-346` (real-real γ=1.0 sites 343-344), `471`, `676`, `693`.
- `palace/models/timeoperator.cpp:137-141`, `217`, `273` — sub-pattern A sites (139 aliasing exception).
- `palace/models/romoperator.cpp:176-195` — `ProlongatePROMSolution`; real-real γ=1.0 sites 188-189 + AXPY companion 193-194.
- `search_text "AXPBYPCZ\("` — complete 13-site call-site census.
- `tools/citecheck/citecheck.py` — 23 citations bounds-checked (23 ok / 0 failing); anchor-drift confirmed for slepc:1986 (AXPBYPCZ), nleps:343 (X[j].Real), romoperator:188 (V[j]), vector.cpp:402 (gamma == 0.0), vector.cpp:729 (add(...y,y)), vector.cpp:751 (add(...y,z)).

## Open questions / caveats

1. **Correction-6 refinement (folded into the firm body): the γ==0 branch range is
   402-427, not the cycle-021 draft's 402-429.** The cycle-021 report proposed
   tightening `vector.cpp:402-426` → `402-429`; my independent `read_range` shows the
   γ==0 outer block opens at 402 and **closes at 427** (the `else` is at 428; the γ≠0
   block's first body line is 429). So 402-429 over-covers into the `else` and the
   first γ≠0 line. The firm body uses **402-427**. This is the ±1-2-line pinpoint drift
   the citecheck tool targets — caught and corrected before integration. No
   integrator carry-forward needed (the rough-in file's existing citation was 402-426,
   which under-covered; the firm body replaces it with the exact 402-427).

2. **BLAS-1 L1>L0 floor (`blas1-l1-l0-lowering-theme-gap`) closes 8/8 with this
   dispatch.** dot, scal, nrm2, assemble-diagonal, axpby (firmed cycle-021), and now
   axpbypcz are all firm. The floor OQ can be marked closed by the integrator /
   meta-phase. This was the last rough-in BLAS-1 L1>L0 theme.

3. **MFEM `add(α,x,β,y,z)` alias-safety (carried, out of Palace scope; NOT a
   firm-blocker).** Applicability-condition-1 exception (timeoperator:139, z aliases x
   with γ=0) relies on MFEM's `add` kernel being alias-safe when the destination
   matches an input. This is an MFEM-library property, not verifiable from Palace
   source; carried as the theme's existing flagged OQ per CLAUDE.md "symbols resolving
   into MFEM are logged as open questions." Per-element value-correctness is
   self-evident; only bit-level reproduction is unverified.

4. **Naming-vs-scope nuance on the SIBLING `axpby-mutation-rotation` (NOT this
   theme; carried from cycle-021 OQ `axpby-theme-covers-axpy-family-naming`).** The
   cycle-021 audit flagged that `axpby-mutation-rotation` is *named* axpby but its body
   covers the `axpy` family; the fused 2-scalar `AXPBY` L0 surface
   (`vector.cpp:315-360`, `727-743`) is a separate uniformly-delegating lowering. That
   is a sibling-theme concern, untouched by this dispatch; flagged here only so the
   floor-closure bookkeeping does not conflate it with `axpbypcz`. The
   `axpbypcz-mutation-rotation` theme is correctly named (it covers the genuine
   3-scalar AXPBYPCZ surface).

5. **Direction-of-definition: clean (high→low).** The firm body narrates the rewrite
   forward (L1 `axpbypcz` pure form → L0 `AXPBYPCZ` kernels), per the high→low layer-
   definition invariant. No reverse-direction (L0-lifts-to-L1) prose in the chapter.
