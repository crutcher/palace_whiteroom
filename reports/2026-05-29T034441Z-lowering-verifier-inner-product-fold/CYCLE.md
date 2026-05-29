---
agent: lowering-verifier
invoked_at: 2026-05-29T034441Z
scope: L2>L1 theme audit — inner-product-fold-specialization
status: integrated
integrated_at: 2026-05-29T06:05:00Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-020 finalize (staging row #7). LOWERING-VERIFIER audit of inner-product-fold-specialization, verdict fully-supported / keep firm. Appended a verified_against: fenced yaml block at END OF FILE (15 audit rows + coverage_verdict fully-supported + status_recommendation keep firm + audit_caveat). Theme stays firm (no status change). Post-repair: the phantom :611→:612 SPD-comment drift dropped (file already pins :612); the 3 genuine inline-anchor corrections (:623→:624, :632→:634, :615-616→:616 on operator.cpp anchors) recorded in OQ inner-product-fold-specialization-operator-cpp-inline-anchor-drift for a future lifter touch (NOT applied this dispatch — not in the proposed-changes blocks). Confirms-firm plan Now #2; meta-phase enacts the plan flip + closes inner-product-harvester-formalization-and-conjugation-pinning (:140). Pure metadata append; retroactive-budget 0; clean build."
inputs:
  - book/src/L2-L1/inner-product-fold-specialization.md
  - palace/linalg/vector.cpp:263-274, 664-685 (ComplexVector::Dot / TransposeDot; real / complex LocalDot)
  - palace/linalg/vector.hpp:240-262 (LocalDot / Dot / Norml2 decls + arg-2-conj doc comments)
  - palace/linalg/operator.cpp:598-617 (Norml2 SPD-realness assert), 621-638 (weighted Dot overloads)
  - palace/linalg/iterative.cpp:395 (CG beta = Dot(comm, z, r))
  - palace/models/boundarymodeoperator.cpp:85,90 (Poynting diagonal + cross-coupling off-diagonal)
  - palace/linalg/nleps.cpp:487,492 (abs-projected norm witnesses)
  - book/src/L1/dot.md, book/src/L1/bilinear-form.md (RHS leaf anchors)
---

# CYCLE: Audit inner-product-fold-specialization

## Summary

Audited the firm L2>L1 theme `inner-product-fold-specialization` (landed cycle-019),
which lowers the L2 reduce-to-scalar fold `inner_product` into its three L1 leaf
specializations (`dot` / `tdot` / `bilinear_form`) via a three-key dispatch (conjugation
kernel, element type, weight presence), a value-level conjugate-pair re-order rule
(`xᴴ y = conj(yᴴ x)`), and a pinned summation-order table. I independently `read_range`-
verified every cited Palace L0 range plus the L1 anchor self-citations.

**Verdict: fully-supported, with a bounded inherited-miscitation lint.** Every dispatch
arm, the conjugate-pair re-order rule, and the summation-order table are *semantically*
faithful to the verified Palace bodies — the re-order identity is sound per-line, the
kernel sign tables match `Dot`/`TransposeDot`, the workspace/two-stage tree matches the
weighted `Dot`, and the `tdot` zero-call-sites caveat is exact. The applicability
conditions are complete. **However, the theme drifted by 1–2 lines on three `operator.cpp`
anchors** touched in the cycle-019 repair pass (the SPD-realness assertion range and the two
`Ax`-workspace allocation lines). These are precise, evidenced citation corrections (in-scope
per `lifter-scope-content-correction-boundary`) that I surface as a carry-forward for the
integrator + a follow-up lifter dispatch — they do NOT reduce the theme's `firm` status (the
dispatch structure and the named L0 bodies are correct; only the exact line offsets drifted).
(The SPD-realness *comment* is NOT a drift — the live theme already pins it at `:612`, the
verified value; an earlier framing of this report listed a `:611`→`:612` comment drift, but
`:611` appears nowhere in the committed theme. The repairer dropped that phantom item.)

## Per-citation audit

### vector.cpp — the conjugation-kernel + element-type bodies

- **Citation**: `palace/linalg/vector.cpp:263-267` (`ComplexVector::Dot` body).
  - **Theme claim**: Hermitian kernel returning `{Re(x)Re(y)+Im(x)Im(y), Im(x)Re(y)−Re(x)Im(y)}`
    `= x·conj(y) = yᴴ x`; `this==&y` imag=0 fast path at `:266`.
  - **Found**: `:263` signature; `:265` real part `(Real()*y.Real()) + (Imag()*y.Imag())`;
    `:266` `(this == &y) ? 0.0 : ((Imag()*y.Real()) - (Real()*y.Imag()))`. Exact.
  - **Verdict**: **supports.** Math check: `x·conj(y) = (xr·yr+xi·yi) + i(xi·yr−xr·yi)` matches
    the code. `yᴴ x` in component form equals `x·conj(y)`. The arg-2-conjugated identity holds.

- **Citation**: `palace/linalg/vector.cpp:269-274` (`ComplexVector::TransposeDot` body).
  - **Theme claim**: same real part, **negated** imag cross-term (`Im(x)Re(y)+Re(x)Im(y)`),
    `this==&y` returns `2·Im·Re` at `:272-273`; the unconjugated `tdot` kernel.
  - **Found**: `:269` signature; `:271` real `(Real()*y.Real()) - (Imag()*y.Imag())`;
    `:272-273` `(this==&y) ? (2.0*(Imag()*y.Real())) : ((Imag()*y.Real()) + (Real()*y.Imag()))`.
    Note: `TransposeDot` real part has a `−` (`Re(x)Re(y) − Im(x)Im(y)`) where `Dot` has `+`,
    AND the imag has `+` where `Dot` has `−`. Together these = `x·y` (unconjugated). Exact.
  - **Verdict**: **supports.** The theme's framing "the ONLY per-element difference is the sign
    of the imaginary cross-term" (§dispatch key 1) is slightly imprecise — the real part sign
    ALSO flips (`+`→`−`). But the net effect is correctly characterized as `x·conj(y)` vs `x·y`,
    and the §Summation-order table's "the only tree difference from `dot` is that one [Im] sign"
    is about the *reduction tree* (four real LocalDots), not the per-element formula — under that
    reading it is correct (both decompose into the same four real dots; only the Im combination
    sign differs). Minor prose nuance, not a defect. See Open Questions.

- **Citation**: `palace/linalg/vector.cpp:664-672` (real `LocalDot(Vector,Vector)`).
  - **Theme claim**: single Hypre `hypre_SeqVectorInnerProd` strided pass with
    `MFEM_ASSERT(x.Size()==y.Size())` at `:667`.
  - **Found**: `:665` signature; `:667` `MFEM_ASSERT(x.Size() == y.Size(), "Size mismatch ...")`;
    `:668-669` `X.Update(x); Y.Update(y);`; `:670` `return hypre_SeqVectorInnerProd(X, Y)`. Exact.
  - **Verdict**: **supports.**

- **Citation**: `palace/linalg/vector.cpp:674-685` (complex `LocalDot(ComplexVector,ComplexVector)`).
  - **Theme claim**: four real `LocalDot`s combined into `(Re, Im)`,
    `Im = LocalDot(xi,yr) − LocalDot(xr,yi)`, `&x==&y` self-dot fast path returning imag=0 at `:679`.
  - **Found**: `:674` signature; `:676` `if (&x == &y)`; `:678` `{LocalDot(xr,yr)+LocalDot(xi,yi), 0.0}`
    (the imag=0 fast path — theme cites `:679`, the actual return is the line inside the `&x==&y`
    branch; close enough, the brace/return spans `:678`); `:682-683`
    `{LocalDot(xr,yr)+LocalDot(xi,yi), LocalDot(xi,yr) - LocalDot(xr,yi)}`. The `Im` cross-term
    sign is `−`. Exact match on the formula.
  - **Verdict**: **supports.** (Minor: the imag=0 return is at `:678` not `:679`; within tolerance —
    the fast-path branch occupies `:676-679`.)

### vector.hpp — the documented arg-2 convention + collective scaffold + norm consumer

- **Citation**: `palace/linalg/vector.hpp:240-262` (LocalDot/Dot/Norml2 decls + comments).
  - **Theme claim**: doc strings `// Calculate the … inner product yᴴ x or yᵀ x` at `:242,:246`;
    `Dot` template `= Mpi::GlobalSum ∘ LocalDot` at `:247-253`; `Norml2(comm,x) = √|Dot(comm,x,x)|`
    at `:256-260`.
  - **Found**: `:242` `// Calculate the local inner product yᴴ x or yᵀ x.` (exact); `:246`
    `// Calculate the parallel inner product yᴴ x or yᵀ x.` (exact); `:247` `Dot` template signature,
    `:249` `auto dot = LocalDot(x, y)`, `:251` `Mpi::GlobalSum(1, &dot, comm)`, `:252` `return dot`,
    `:253` close (exact); `:255` comment, `:257` `Norml2` signature, `:260`
    `return std::sqrt(std::abs(Dot(comm, x, x)))` (the cite start `:256` is one early — the comment
    is `:255` — but the range encloses the body correctly).
  - **Verdict**: **supports.** The arg-2-conjugation documented convention (`yᴴ x`) — the source of
    the conjugate-pair re-order — is exactly as cited at `:242,:246`.

### operator.cpp — the weighted member, the workspace, the SPD-realness consumer

- **Citation**: `palace/linalg/operator.cpp:621-628` (weighted `Dot`, real-`Operator`).
  - **Theme claim**: allocates `ComplexVector Ax(A.Height())` at **`:623`**,
    `A.Mult(x.Real(), Ax.Real())` / `A.Mult(x.Imag(), Ax.Imag())`, then `Dot(comm, Ax, y) = yᴴ A x`.
  - **Found**: `:621-622` signature; **`:624` `ComplexVector Ax(A.Height());`** (NOT `:623`);
    `:625` `A.Mult(x.Real(), Ax.Real())`; `:626` `A.Mult(x.Imag(), Ax.Imag())`; `:628`
    `return Dot(comm, Ax, y)`; `:629` close. The body content is exactly as the theme describes.
  - **Verdict**: **supports (semantically); citation drift on the inline `Ax` anchor.** The §weighted-
    workspace section cites the `Ax` allocation at `operator.cpp:623` — **actual is `:624`** (off by 1).
    The range `:621-628` itself is fine (it contains `:624`); only the *inline* `:623` anchor in
    §"The weighted-member workspace" is drifted.

- **Citation**: `palace/linalg/operator.cpp:631-638` (weighted `Dot`, `ComplexOperator`).
  - **Theme claim**: `A.Mult(x, Ax)` then `Dot(comm, Ax, y)`; `Ax` cited at `:632`.
  - **Found**: `:631-632` signature; **`:634` `ComplexVector Ax(A.Height());`** (NOT `:632`);
    `:635` `A.Mult(x, Ax)`; `:636` `return Dot(comm, Ax, y)`; `:637` close. Body exact.
  - **Verdict**: **supports (semantically); citation drift on the inline `Ax` anchor.** §weighted-
    workspace cites the `ComplexOperator` `Ax` at `:632` — **actual `:634`** (off by 2). The range
    `:631-638` is correct. Only the inline `:632` anchor drifted.

- **Citation**: `palace/linalg/operator.cpp:598-617` (`Norml2` SPD-realness consumer; the cycle-019
  repairer pinned the SPD comment to `:612` and the assertion to `:615-616`).
  - **Theme claim**: B-weighted norm `√ Dot(comm, Bx, x)`; SPD assertion
    `dot.real() > 0.0 && |dot.imag()| < 1e-9·dot.real()` at **`:615-616`**, comment
    "For SPD B, xᴴ B x is real" at **`:612`**.
  - **Found**: real `Norml2` signature `:600`; `:601` `B.Mult(x, Bx)`; `:603` `double dot = Dot(comm, Bx, x)`;
    `:604` `MFEM_ASSERT(dot > 0.0, ...)`; `:605` `return std::sqrt(dot)`. Complex `Norml2` signature `:610`;
    **`:612` `// For SPD B, xᴴ B x is real.`** (the theme ALREADY says `:612` — exact, no change);
    `:613-614` `B.Mult(x.Real(), Bx.Real())` / `B.Mult(x.Imag(), Bx.Imag())`;
    `:615` `std::complex<double> dot = Dot(comm, Bx, x)`;
    **`:616` `MFEM_ASSERT(dot.real() > 0.0 && std::abs(dot.imag()) < 1.0e-9 * dot.real(), ...)`**
    (single line — NOT `:615-616`); `:617` `return std::sqrt(dot.real())`.
  - **Verdict**: **supports (semantically); one citation drift on a repairer-pinned anchor.** The
    SPD-realness comment is at **`:612`** and the theme already pins it at `:612` — verified, no change
    (an earlier framing of this report called it a `:611`→`:612` drift; that was a phantom, `:611` is
    nowhere in the committed theme — the repairer dropped it). The SPD assertion is a **single line at
    `:616`** (theme says `:615-616` — `:615` is actually the `dot = Dot(...)` line, `:616` is the
    assertion), so the assertion range should narrow to `:616`. The enclosing range `:598-617` contains
    everything; only the SPD-assertion pinpoint anchor is drifted.

### iterative.cpp + boundarymodeoperator.cpp + nleps.cpp — the re-order witnesses

- **Citation**: `palace/linalg/iterative.cpp:395` (`beta = linalg::Dot(comm, z, r)`).
  - **Theme claim**: CG's `(Br, r)` coefficient, consumed in real arithmetic (re-order-invisible).
  - **Found**: `:395` `beta = linalg::Dot(comm, z, r);` exact (note a second `beta = linalg::Dot(comm, z, r)`
    at `:460` — the cited `:395` is the correct primary CG site; `:396` `CheckDot(beta, "PCG preconditioner
    is not positive definite: (Br, r) = ")` confirms the SPD/real consumption).
  - **Verdict**: **supports.**

- **Citation**: `palace/models/boundarymodeoperator.cpp:85` (Poynting diagonal `Dot(comm, et, *Bttr, et)`).
  - **Theme claim**: M-weighted diagonal (`y = x = et`), Hermitian `Bttr` → real, re-order invisible.
  - **Found**: `:85` `std::complex<double> P = 0.5 * std::conj(kn) / omega * linalg::Dot(comm, et, *Bttr, et);`
    exact. The operands are both `et` (diagonal). The realness rests on `Bttr` Hermitian + diagonal — a
    physics/domain property, not asserted at this line (see caveat).
  - **Verdict**: **supports.**

- **Citation**: `palace/models/boundarymodeoperator.cpp:90` (cross-coupling `Dot(comm, en, Atn, et)`).
  - **Theme claim**: M-weighted off-diagonal (`en ≠ et`), non-Hermitian `Atn` → full complex value,
    re-order **observable** — the genuine-lowering-work witness.
  - **Found**: `:88-89` `ComplexWrapperOperator Atn(const_cast<...>(Atnr.get()), const_cast<...>(Atni.get()))`;
    `:90` `P += std::complex<double>(0.0, 1.0) / (2.0 * omega) * linalg::Dot(comm, en, Atn, et);`. `en ≠ et`
    (off-diagonal); `Atn` is a general real+imag wrapper operator (non-Hermitian in general). Exact.
  - **Verdict**: **supports.** The non-Hermitian-off-diagonal observable case is genuinely present.

- **Citation**: `palace/linalg/nleps.cpp:487,492` (abs-projected norm witnesses — in §re-order-invisible prose).
  - **Theme claim**: `std::abs(linalg::Dot(...))` norms — magnitude convention-blind.
  - **Found**: `:487` `double norm_c = std::sqrt(std::abs(linalg::Dot(GetComm(), c, c)) + ...)`;
    `:492` `double norm_v = std::sqrt(std::abs(linalg::Dot(GetComm(), v, v)) + ...)`. Exact.
  - **Verdict**: **supports.**

- **Citation**: `search_text TransposeDot over palace/**` → 2 hits (decl + def, zero callers).
  - **Found**: exactly `palace/linalg/vector.hpp:112` (decl) + `palace/linalg/vector.cpp:269` (def).
    Zero call sites. Exact.
  - **Verdict**: **supports.** The `tdot` type-API-surface-only caveat is verified.

### L1 / L2 anchors (RHS leaves)

- **`book/src/L1/dot.md:33-34`** (real + complex Hermitian kernel rows) — **supports** (`:33` real
  `x[i]*y[i]`, `:34` complex `conj(x[i])*y[i]`).
- **`book/src/L1/dot.md:35`** (`tdot` unconjugated row) — **supports**.
- **`book/src/L1/dot.md:43-44`** (arg-1-conjugated convention, "conjugate-linear in the first
  argument") — **supports** (`:43`).
- **`book/src/L1/dot.md:49`** (self-dot trick) — **supports**.
- **`book/src/L1/bilinear-form.md:63`** (`bilinear_form(x, M, y) = xᴴ M y`) — **supports**.
- **`book/src/L1/bilinear-form.md:39-43`** (Category-4 workspace `Ax`) — **supports**.
- **`book/src/L1/bilinear-form.md:119-145`** (conjugation-asymmetry reconciliation) — **supports**;
  the theme's re-order narration is consistent with the leaf's own reconciliation prose.
- **`book/src/L2/inner_product.md`** (LHS fold) — **supports as a live link** (exists on disk; the
  theme correctly notes dispatch #1 flips it stub→firm in this same wave). Not the audit target; the
  dispatch rule, re-order deferral, and IEEE-non-law deferral attributions are sound against the L2
  §Signature / §Algebraic-laws structure as authored.

## The conjugate-pair re-order — soundness check (per-line)

The headline rule `inner_product x y = xᴴ y = conj(yᴴ x) = conj(linalg::Dot(comm, x, y)) = linalg::Dot(comm, y, x)`
is **sound per-line** against the verified bodies:

- `linalg::Dot(comm, a, b) = LocalDot(a, b) ∘ GlobalSum`, and `LocalDot(ComplexVector x, y)` computes
  `x·conj(y)` (verified `:682-683`: `Im = LocalDot(xi,yr) − LocalDot(xr,yi)`). So
  `linalg::Dot(comm, x, y) = x·conj(y) = yᴴ x` (arg-2 conjugated). ✓ matches the doc comment `:242,:246`.
- Operand-swap form: `linalg::Dot(comm, y, x) = y·conj(x) = xᴴ y`. ✓ recovers the L2 fold.
- Outer-conj form: `conj(linalg::Dot(comm, x, y)) = conj(yᴴ x) = xᴴ y`. ✓ recovers the L2 fold.
- Weighted: Palace computes `Dot(comm, Ax, y) = yᴴ A x` (verified `:624-628`); for Hermitian `M`,
  `yᴴ M x = conj(xᴴ M y)` so outer-conj recovers it; for non-Hermitian `M` (the `:90` `Atn` witness),
  only the operand-swap form is faithful. ✓ matches the theme's distinction.

The identity `xᴴ y = conj(yᴴ x)` and the swap/conj recovery are correct; the re-order is value-bearing
exactly where the theme says (full-complex-value off-diagonal non-Hermitian uses).

## Summation-order table — verification

| theme row | verified against | verdict |
|---|---|---|
| `dot` real → single Hypre `hypre_SeqVectorInnerProd` pass | `vector.cpp:670` | supports |
| `dot` complex → four real Hypre passes, `Im` cross-term `−` | `vector.cpp:682-683` | supports |
| `tdot` complex → same four real dots, `Im` sign `+` | `vector.cpp:271-273` | supports (see nuance: `TransposeDot` is the *member* form returning `x·y` directly, not literally a four-real-LocalDot decomposition; the §table's "(member)" annotation acknowledges this. The four-real-dot framing is the `LocalDot` complex path; `TransposeDot`-the-member open-codes `Re(x)Re(y)−Im(x)Im(y), Im(x)Re(y)+Re(x)Im(y)`. Both are valid descriptions of the unconjugated complex kernel; the table conflates the member and free-function reduction shapes slightly but the *sign* claim is exact.) |
| `bilinear_form` → two-stage (M-apply tree then four-real-dot of `Dot(comm,Ax,y)`) | `operator.cpp:624-628` / `:634-636` | supports (the `Ax` workspace is the verified stage boundary) |

## Applicability conditions

- **Condition 1 (shared length axis)**: Verifiable — `MFEM_ASSERT(x.Size()==y.Size())` at
  `vector.cpp:667` (verified, exact). Weighted-member codomain/domain match deferred to
  `bilinear-form` §Applicability. **No counter-example.** Complete.
- **Condition 2 (conjugation key value-bearing for complex)**: Verifiable — `dot` (`:265-266`) vs
  `tdot` (`:271-273`) differ; `dot` is PSD-at-diagonal (`:266` imag=0), `tdot` not (`:272` returns
  `2·Im·Re`). **No counter-example.** Complete.
- **Condition 3 (element-type conformance)**: Verifiable — real path `:664-672`, complex lift
  `:674-685`. **No counter-example.** Complete.
- **Condition 4 (value-preservation vs bit-reproduction split)**: Verifiable against the §Summation-
  order table + the load-bearing-trick classification. **No counter-example.** Complete.
- **Condition 5 (re-order observable for full-complex-value uses)**: Verifiable — invisible witnesses
  (`iterative.cpp:395`, `boundarymodeoperator.cpp:85`, `nleps.cpp:487,492`) vs observable witness
  (`boundarymodeoperator.cpp:90`). **No counter-example.** Complete.

The caveats are also complete: `tdot` type-API-surface-only (verified zero call sites),
`bilinear-form` rough-in member status (confirmed in the leaf frontmatter `firmness: rough-in`),
and the non-Hermitian-M operand-swap-vs-outer-conj distinction (verified at `:90`).

## Algebraic laws (cited)

- **Law 7 weight specialization** (`dot = inner_product_M x I y`, `bilinear_form = inner_product_M x M y`):
  holds on the operator signatures — the weight key dispatch is the law read as a lowering. Confirmed
  against `operator.cpp:621-638` (the weighted `Dot` open-codes `inner_product (apply_linop M x) y`).
- **Law 5 (PSD-at-diagonal for the Hermitian/SPD form)**: holds — `vector.cpp:266` returns imag=0 at
  the diagonal; `operator.cpp:612,616` assert `xᴴ B x` real for SPD `B`. The theme's law-5 invocations
  at the re-order-invisible witnesses are sound.
- **Conjugate-pair identity** `xᴴ y = conj(yᴴ x)`: holds on the complex element type (verified above).

## Proposed changes

The theme is `firm` and semantically fully supported; **no status change and no content
rewrite is warranted.** The only proposed change is the standard `verified_against:` metadata
addition (consumed by `cross-layer-cross-cutter`), recording the audit verdicts AND the three
drifted inline anchors. Append to the end of `book/src/L2-L1/inner-product-fold-specialization.md`:

```edit:book/src/L2-L1/inner-product-fold-specialization.md
[append at end of file]
```yaml
verified_against:
  - citation: palace/linalg/vector.cpp:263-267
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: ComplexVector::Dot = x·conj(y) = yᴴ x; Hermitian kernel + conjugate-pair source. Exact.
  - citation: palace/linalg/vector.cpp:269-274
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: TransposeDot = x·y (unconjugated); real-part sign ALSO flips vs Dot (not only the Im cross-term) — prose nuance, value correct.
  - citation: palace/linalg/vector.cpp:664-672
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: real LocalDot single Hypre pass; MFEM_ASSERT(x.Size()==y.Size()) at :667. Exact.
  - citation: palace/linalg/vector.cpp:674-685
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: complex LocalDot four real dots, Im cross-term '−'; self-dot imag=0 branch at :678 (theme cites :679, off by 1, within fast-path span).
  - citation: palace/linalg/vector.hpp:240-262
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: arg-2-conj doc comments :242,:246 exact; Dot template :247-253; Norml2 :257-260 (comment :255).
  - citation: palace/linalg/operator.cpp:621-628
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: real-Operator weighted Dot body exact; INLINE Ax anchor drift — actual ComplexVector Ax(A.Height()) at :624 not :623.
  - citation: palace/linalg/operator.cpp:631-638
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: ComplexOperator weighted Dot body exact; INLINE Ax anchor drift — actual Ax at :634 not :632.
  - citation: palace/linalg/operator.cpp:598-617
    verdict: partially-supports
    audited_at: 2026-05-29T034441Z
    note: Norml2 SPD-realness consumer present; SPD comment at :612 (theme ALREADY pins :612 — verified, no change); SPD assertion is a single line at :616 (theme says :615-616, but :615 is the dot=Dot(...) line — narrow to :616).
  - citation: palace/linalg/iterative.cpp:395
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: CG beta = linalg::Dot(comm, z, r) exact; real-consumed (re-order invisible). Second site at :460.
  - citation: palace/models/boundarymodeoperator.cpp:85
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: Poynting diagonal Dot(comm, et, *Bttr, et); realness rests on Bttr-Hermitian + diagonal (domain property, not source-asserted here).
  - citation: palace/models/boundarymodeoperator.cpp:90
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: cross-coupling Dot(comm, en, Atn, et); en≠et off-diagonal, Atn ComplexWrapperOperator non-Hermitian → full complex value, re-order observable. Exact.
  - citation: palace/linalg/nleps.cpp:487,492
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: std::abs(linalg::Dot(...)) norm witnesses (magnitude convention-blind). Exact.
  - citation: TransposeDot search_text over palace/**
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: exactly 2 hits — vector.hpp:112 decl + vector.cpp:269 def; zero call sites. tdot type-API-surface-only caveat verified.
  - citation: book/src/L1/dot.md:33-35,43,49
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: dot/tdot kernel rows, arg-1-conj convention, self-dot trick — all present.
  - citation: book/src/L1/bilinear-form.md:39-43,63,119-145
    verdict: supports
    audited_at: 2026-05-29T034441Z
    note: xᴴ M y signature, Category-4 workspace, conjugation-asymmetry reconciliation — all present.
coverage_verdict: fully-supported
status_recommendation: keep firm (no status change; semantic content fully supported)
audit_caveat: three inline operator.cpp anchors drifted (Ax :623→:624, :632→:634; SPD assert range :615-616→:616) — citation-correction follow-up, not a status reduction. (SPD comment is ALREADY :612 in the live theme — verified, no change.)
```
```

**Carry-forward citation corrections (integrator + follow-up lifter — bounded, evidenced,
in-scope per `lifter-scope-content-correction-boundary`).** These are the four inline-anchor
drifts the theme's prose asserts as verified but which `read_range` places one-to-two lines
off. They do NOT block integration of the `verified_against:` block; they are precise
corrections for a lifter dispatch (or an integrator carry-forward touch):

1. §"The weighted-member workspace": `operator.cpp:623` → **`:624`** (real-`Operator` `Ax` allocation).
2. §"The weighted-member workspace": `operator.cpp:632` → **`:634`** (`ComplexOperator` `Ax` allocation).
3. §"diagonal degeneration" + §Verified-against: `operator.cpp:615-616` (SPD assertion range) → **`:616`**
   (single line; `:615` is the preceding `std::complex<double> dot = Dot(comm, Bx, x)` line).

(The SPD comment is NOT a drift: the live theme already pins it at `operator.cpp:612` — verified
against the file, no change needed. An earlier framing of this report listed it as a `:611`→`:612`
drift; that was a phantom — `:611` appears nowhere in the committed theme. The repairer dropped it.)

(The wide enclosing ranges `:598-617`, `:621-628`, `:631-638` are NOT in error — they contain the
content. Only the pinpoint inline anchors drifted. This mirrors the cycle-012 SLEPc-NEP precedent
where an inherited `:387`→`:383` drift was both a report-anchor fix and an integrator carry-forward.)

## Supporting evidence

Files consulted (all read this invocation):
- `/home/crutcher/git/palace_whiteroom/reference/palace/palace/linalg/vector.cpp:260-278, 660-690` (kernels + LocalDot)
- `/home/crutcher/git/palace_whiteroom/reference/palace/palace/linalg/vector.hpp:238-262` (decls + doc comments)
- `/home/crutcher/git/palace_whiteroom/reference/palace/palace/linalg/operator.cpp:595-640` (Norml2 SPD + weighted Dot)
- `/home/crutcher/git/palace_whiteroom/reference/palace/palace/linalg/iterative.cpp:390-398` (CG beta)
- `/home/crutcher/git/palace_whiteroom/reference/palace/palace/models/boundarymodeoperator.cpp:70-92` (Poynting + cross-coupling)
- `/home/crutcher/git/palace_whiteroom/reference/palace/palace/linalg/nleps.cpp` (abs-projected norms, search_text)
- `/home/crutcher/git/palace_whiteroom/book/src/L1/dot.md`, `book/src/L1/bilinear-form.md` (RHS leaf anchors)

## Open questions / caveats

- **OQ (citation-correction follow-up, small, not blocking)** — `inner-product-fold-specialization-operator-cpp-inline-anchor-drift`:
  the theme asserts three inline `operator.cpp` anchors as verified that `read_range` places 1-2 lines
  off (`Ax` `:623`→`:624`, `:632`→`:634`; SPD assert range `:615-616`→`:616`).
  **Follow-up**: a `lifter` dispatch (or integrator carry-forward touch) corrects the three inline
  anchors in `book/src/L2-L1/inner-product-fold-specialization.md`. Evidenced and bounded; no status
  change. The SPD-realness assertion is now a single line at `:616` (`:615` is the preceding
  `dot = Dot(...)` line). The SPD comment is NOT in this list: the live theme already pins it at `:612`
  (verified); an earlier framing of this report called it a `:611`→`:612` drift, but `:611` appears
  nowhere in the committed file — that item was a phantom and the repairer dropped it.

- **Prose nuance (non-blocking, optional lifter tightening)** — §dispatch-key-1 says "the ONLY
  per-element difference between the two L0 kernels is the sign of the imaginary cross-term". This is
  imprecise: `TransposeDot` flips BOTH the real-part sign (`Re(x)Re(y) − Im(x)Im(y)` vs `Dot`'s `+`)
  AND the imag-part sign. The *net* characterization (`x·conj(y)` vs `x·y`) is correct, and the
  §Summation-order table's "only tree difference is that one [Im] sign" is correct under the
  four-real-LocalDot reduction-tree reading. No correction required for firmness; a lifter could tighten
  the dispatch-key-1 sentence to "the sign pattern that distinguishes `x·conj(y)` from `x·y`" if
  re-anchoring the theme. Surfaced for awareness, not as a defect.

- **Domain-property note (not a defect)** — the realness of the Poynting diagonal at
  `boundarymodeoperator.cpp:85` rests on `Bttr` being Hermitian plus the diagonal `y=x`. `Bttr`'s
  Hermitian-ness is a physics/assembly property not asserted at the cited line. The theme's law-5/law-8
  framing is sound, but a reader should know the realness there is a domain claim, not a source-line
  assertion. (The SPD assertion at `operator.cpp:616` IS the source-asserted realness witness; the
  `:85` realness is the un-asserted analogue.)

- **No new structural OQ.** The two-stage weighted-member reduction-tree caveat the theme already
  tracks under `apply-linop-lowering-verifier-audit-cohort` is correctly scoped (the M-apply tree is
  `apply_linop`-internal). No new question needed there. The theme's recommendation to treat
  `linear-combination-fold-specialization-theme-followups` as resolvable on the sibling side is sound
  and does not bear on this audit.

- **Direction-of-definition: clean.** The chapter body narrates L2 → L1 forward throughout; the reverse
  (lifting) note is correctly quarantined to §"Open questions / caveats" as working-note material. No
  high→low violation.
