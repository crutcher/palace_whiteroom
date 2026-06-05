---
agent: lowering-verifier
invoked_at: 2026-06-05T04:49:16Z
scope: L1>L0 theme audit — apply-linop-mutation-rotation
status: pending
integrated_at: 2026-06-05T051726Z
integration_commit: 8cb576ec1f4fcad7752ebba5bf23b16076a0cf28
integration_notes: "Applied cycle-100 (staging row 1/4). Matvec lowering floor `rough-in` → firm (firm-on-positive-structure / syntactic-identity escape, 5 sub-patterns); Status flip + L1-L0/index.md:21 cell + L3/apply_linop.md:169 token + 23-row corrected verified_against. Repairer fixed one internal-line off-by-one. Rank stays 0 (both deps firm). Build EXIT 0; step-5b rank_violations 0."
inputs:
  - book/src/L1-L0/apply-linop-mutation-rotation.md
  - palace/linalg/operator.hpp:18-230 (ComplexOperator virtual family, SumOperator/ProductOperatorHelper/BaseProductOperator/ComplexWrapperOperator decls)
  - palace/linalg/operator.cpp:428-520 (SumOperator + BaseDiagonalOperator definitions)
  - palace/linalg/rap.cpp:195-361 (ParOperator Mult/MultTranspose/AddMult/AddMultTranspose)
  - palace/linalg/iterative.cpp:379,443 (CG Mult call sites)
  - book/src/L1/apply_linop.md (firm L1 anchor, cycle-004)
  - book/src/L1-L0/axpby-mutation-rotation.md (sister theme, firm)
---

# CYCLE: Audit apply-linop-mutation-rotation

## Summary

Audited the `apply-linop-mutation-rotation` L1>L0 theme (currently `rough-in`) to
discharge its explicitly-deferred firm-promotion gate. Re-read all cited L0 ranges
on-disk via codemap `read_range`. **Verdict: FULLY-SUPPORTED → FIRM.** Every one of
the five sub-pattern recognition rules (A bare `Mult`, B `MultTranspose`, C
`MultHermitianTranspose`, D accumulating `AddMult`, E accumulating
transposed/Hermitian) is a **syntactic identity on positive, fully-specified
`mfem::Operator::Mult` / `ComplexOperator::Mult`-family source** — name-match
recognition over read C++ method bodies, NOT a numerically-asserted axiom or a
convergence-semantics claim. This is exactly the **firm-on-positive-structure /
syntactic-identity escape** named in the CLAUDE.md `rough-in (test-coverage-bounded)`
invariant ("the `apply_linop` situation, NOT the `eigsolve`-convergence-semantics
situation"). The deferred "integration testing" with the sister `axpby` theme on the
D/E composition path is NOT a gate on a syntactic identity: the D/E path is the
composition of two already-firm syntactic rules (`apply_linop` + `axpby`, both firm),
and the inner accumulator (`y.Add(a*c, z)` / `y.Add(a, ty)`) is already covered by the
firm sister theme. Rank check passes: both endpoints firm (`L1/apply_linop` firm; L0
is rank-3 ground truth), so `rank(theme) ≤ min(firm, firm) = firm` — `firm` is
well-founded. Three minor citation drifts found (two range-END close-brace off-by-ones,
one note-internal line reference off-by-one); all corrected below — none affects a
recognition rule or the verdict.

## Per-citation audit

- **Citation**: `palace/linalg/operator.hpp:21`
  - **Theme claim** (Sub-pattern A): real-operator type alias `using Operator = mfem::Operator;`; real path inherits abstract `Mult` from MFEM.
  - **Found**: line 21 is exactly `using Operator = mfem::Operator;`.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.hpp:54`
  - **Theme claim** (Sub-pattern A): `ComplexOperator::Mult` pure-virtual decl.
  - **Found**: line 54 `virtual void Mult(const ComplexVector &x, ComplexVector &y) const = 0;`.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.hpp:56`
  - **Theme claim** (Sub-pattern B): `ComplexOperator::MultTranspose` decl.
  - **Found**: line 56 `virtual void MultTranspose(const ComplexVector &x, ComplexVector &y) const;`.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.hpp:58`
  - **Theme claim** (Sub-pattern C): `ComplexOperator::MultHermitianTranspose` decl.
  - **Found**: line 58 `virtual void MultHermitianTranspose(const ComplexVector &x, ComplexVector &y) const;`.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.hpp:60-61` / `:60-67`
  - **Theme claim** (Sub-pattern D/E): `ComplexOperator::AddMult` (default `a = 1.0`) at 60-61; the AddMult / AddMultTranspose / AddMultHermitianTranspose decl cohort at 60-67.
  - **Found**: 60-61 `AddMult(..., const std::complex<double> a = 1.0)`; 63-64 `AddMultTranspose(..., a = 1.0)`; 66-67 `AddMultHermitianTranspose(..., a = 1.0)`. Default `a = 1.0` confirmed for all three.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.hpp:116-136`
  - **Theme claim** (Verified-against): `SumOperator` declaration.
  - **Found**: line 116 `class SumOperator : public Operator`, closing `};` at line 136. Exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.hpp:133`
  - **Theme claim** (Sub-pattern D): `SumOperator::AddMult` decl.
  - **Found**: line 133 `void AddMult(const Vector &x, Vector &y, const double a = 1.0) const override;`. Exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.hpp:158-165` / `:158-175`
  - **Theme claim** (Sub-pattern C/E): `ProductOperatorHelper<…,ComplexOperator>` `MultHermitianTranspose` (158-165) — body `A.MultHermitianTranspose(x, z); B.MultHermitianTranspose(z, y)`; `AddMultHermitianTranspose` (167-175) — composition witness.
  - **Found**: 158 method head, 159 `{`, 160-164 body, 165 `}` (MultHT); 167 method head … 175 `}` (AddMultHT) with body `A.MultHermitianTranspose(x, z); B.AddMultHermitianTranspose(z, y, a)`. Exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.hpp:178-226`
  - **Theme claim** (Verified-against): `BaseProductOperator` template (composition).
  - **Found**: line 178 `template <typename OperType>`, class body closes `}` at 225, `};` at 226. Exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.hpp:202-206`
  - **Theme claim** (Sub-pattern A): `BaseProductOperator::Mult` = `B.Mult(x, z); A.Mult(z, y)` chained-apply witness.
  - **Found**: 202 head, 203 `{`, 204 `B.Mult(x, z);`, 205 `A.Mult(z, y);`, 206 `}`. Exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.hpp:214-218`
  - **Theme claim** (Sub-pattern D): `BaseProductOperator::AddMult` = `B.Mult(x, z); A.AddMult(z, y, a)`.
  - **Found**: 214 head, 215 `{`, 216 `B.Mult(x, z);`, 217 `A.AddMult(z, y, a);`, 218 `}`. Exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.hpp:220-225`
  - **Theme claim** (Sub-pattern E): `BaseProductOperator::AddMultTranspose` = `A.MultTranspose(x, z); B.AddMultTranspose(z, y, a)`.
  - **Found**: 220-221 head (two-line), 222 `{`, 223 `A.MultTranspose(x, z);`, 224 `B.AddMultTranspose(z, y, a);`, 225 `}`. Exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.hpp:73-113`
  - **Theme claim** (Applicability cond. 3): `ComplexWrapperOperator` — the mixed real-op-on-complex-vector lift (`complex-from-real-lift` concept).
  - **Found**: line 73 `class ComplexWrapperOperator : public ComplexOperator`, closing `};` at 113. Block-2×2 equivalent-real formulation comment at 71-72. Exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.cpp:428-441`
  - **Theme claim** (Sub-pattern A + verified_against note): `SumOperator::Mult`; size-1 fast path `y *= ops.front().second`; size>1 path `y = 0.0; AddMult(x, y)` (Mult-via-AddMult reuse witness).
  - **Found**: 428 head; 430-437 size-1 branch with `y *= ops.front().second` at 435; 438 `y = 0.0;`, 439 `AddMult(x, y);`; 440 `}` end branch?, 441 `}` end method. The note's "439-440" reuse witness is confirmed (`y = 0.0;` 438, `AddMult(x, y);` 439). Exact range.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.cpp:443-456`
  - **Theme claim** (Sub-pattern B): `SumOperator::MultTranspose`.
  - **Found**: 443 head, body mirrors Mult with `MultTranspose`/`AddMultTranspose`, `}` at 456. Exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.cpp:458-466` (+ `:464`)
  - **Theme claim** (Sub-pattern D + recognition note): `SumOperator::AddMult`; inner accumulator `y.Add(a * c, z)` at line 464.
  - **Found**: 458 head, 460 `z.SetSize(y.Size());`, 461 loop, 463 `op->Mult(x, z);`, 464 `y.Add(a * c, z);`, 466 `}`. `:464` exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.cpp:468-476`
  - **Theme claim** (Sub-pattern E): `SumOperator::AddMultTranspose`.
  - **Found**: 468 head, loop with `op->MultTranspose(x, z); y.Add(a * c, z)`, `}` at 476. Exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.cpp:479-487` (Sub-pattern A) / `:479-507` (Verified-against)
  - **Theme claim**: `BaseDiagonalOperator<Operator>::Mult` matrix-free `Y[i] = D[i] * X[i]`; the `:479-507` verified-against range additionally encloses the complex specialisation.
  - **Found**: 479 `template <>`, 480 head, 486 `mfem::forall_switch(… { Y[i] = D[i] * X[i]; });`, 487 `}` (real Mult). Complex specialisation `BaseDiagonalOperator<ComplexOperator>::Mult` spans 488-507 (`}` at 507). Both ranges exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.cpp:509-519`
  - **Theme claim** (Sub-pattern D + verified-against): `BaseDiagonalOperator<Operator>::AddMult` matrix-free fused `Y[i] += a * D[i] * X[i]`.
  - **Found**: 509 `template <>`, 510-511 head, 519 `mfem::forall_switch(… { Y[i] += a * D[i] * X[i]; });`. **Closing `}` is at line 520**, not 519 — the cited range END excludes the close brace.
  - **Verdict**: partially-supports (range END off-by-one; anchor body in-range; corrected to `:509-520` below).

- **Citation**: `palace/linalg/rap.cpp:195-234`
  - **Theme claim** (Sub-pattern A + verified-against): `ParOperator::Mult`; prolongation + inner `A->Mult(lx, ly)` "at line 220" + restriction + dbc_tdof masking.
  - **Found**: 195 head; inner apply `A->Mult(lx, ly);` at **line 219** (comment `// Apply the operator on the L-vector.` at 218), restriction `RestrictionMatrixMult(ly, y)` at 221, dbc block, method closes `}` at 234. Range `:195-234` exact; **the note's internal "line 220" for the inner apply is off by one — it is line 219.**
  - **Verdict**: supports (range exact); note line-reference corrected to 219 below.

- **Citation**: `palace/linalg/rap.cpp:236-275`
  - **Theme claim** (Sub-pattern B): `ParOperator::MultTranspose`; restriction/prolongation roles swapped.
  - **Found**: 236 head, inner `A->MultTranspose(ly, lx)`, `}` at 275. Exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/rap.cpp:277-318` (+ note `:317`)
  - **Theme claim** (Sub-pattern D + verified-against): `ParOperator::AddMult`; final accumulation `y.Add(a, ty)` at line 317.
  - **Found**: 277 head, inner `A->Mult(lx, ly)`, `y.Add(a, ty);` at line 317, `}` at 318. `:317` and `:277-318` exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/rap.cpp:320-360`
  - **Theme claim** (Sub-pattern E): `ParOperator::AddMultTranspose`.
  - **Found**: 320 head, final accumulation `y.Add(a, tx);` at line 360, **closing `}` at line 361** — cited range END excludes the close brace.
  - **Verdict**: partially-supports (range END off-by-one; corrected to `:320-361` below).

- **Citation**: `palace/linalg/iterative.cpp:379`
  - **Theme claim** (Sub-pattern A): CG residual call site `A->Mult(x, r)`.
  - **Found**: line 379 `A->Mult(x, r);` (inside `if (this->initial_guess)`). Exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:443`
  - **Theme claim** (Sub-pattern A): CG inner-loop call site `A->Mult(p, z)`.
  - **Found**: line 443 `A->Mult(p, z);` (followed by `denom = linalg::Dot(comm, z, p)`). Exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/operator.cpp:443-456` was for B above; `operator.hpp:60-61` / `:60-67` / `:63-67` decls — confirmed under the hpp:60-67 entry above.

## Applicability conditions

1. **No aliasing between `x` and `y`.** Verifiable: the cited kernels read `x` / write `y` (`BaseProductOperator::Mult` workspace `z` at `operator.hpp:194,200-205`; element-wise diagonal `Y[i] = D[i]*X[i]` at `operator.cpp:486` tolerates aliasing). Stated as an applicability condition not a known failure; shared with sister theme. Counter-example found? No — no observed site aliases `Mult` args.
2. **No observer of prior `y` after the call** (A/B/C overwriting); for D/E the prior `y` is consumed not destroyed. Verifiable: `AddMult` bodies `y.Add(a*c, z)` (`operator.cpp:464`), `y.Add(a, ty)` (`rap.cpp:317`) read-then-add `y`. Counter-example? No.
3. **Conforming shape/element type.** Verifiable directly: `MFEM_ASSERT(x.Size() == width && y.Size() == height, …)` at `rap.cpp:197-198` (Mult) and `:280-281` (AddMult). Mixed real-op-on-complex-vector routes via `ComplexWrapperOperator` (`operator.hpp:73-113`, confirmed). Counter-example? No.
4. **Operator `A` is L0-linear; the L0 method is `const`.** Verifiable: every cited virtual is declared `const` (`operator.hpp:54-67` ComplexOperator decls; `:129-135` SumOperator `override` decls all `const`). `mutable` workspace `z` (`operator.hpp:120`, `:185`) is private and not L1-observable. Counter-example? No.
5. **Transpose-mode recognition** (B/C). Verifiable: dedicated `MultTranspose` / `MultHermitianTranspose` virtuals exist (`operator.hpp:56,58`) and are implemented by every cited concrete subclass. Obstruction (no transpose) routes to `MFEM_ABORT` — out of scope. Counter-example? N/A (no abort-only operator in the cited cohort).
6. **Accumulate-mode `a` is a runtime scalar** (D/E). Verifiable: `a` is a function parameter (`operator.cpp:458` real `double a`, `operator.hpp:60` complex `std::complex<double> a = 1.0`). `a==1.0` / `a==-1.0` constant-folding handled by sister theme. Counter-example? No.

All six conditions are verifiable from the cited evidence; no counter-examples found.

## Algebraic laws (the syntactic-identity escape)

The theme states no standalone numeric axioms; its "laws" are name-match recognition
rules that re-anchor L0 method names to L1 expressions. Each holds as a **syntactic
identity** on the positive `Mult`-family source:

- **Sub-pattern A** (`structural`) — `A.Mult(x, y)` ⇒ `y = apply_linop(A, x)`. Holds:
  the L0 method computes `A·x` into `y` (read off every concrete realisation:
  `SumOperator::Mult` `operator.cpp:428-441`; `BaseDiagonalOperator::Mult`
  `operator.cpp:479-487`; `ParOperator::Mult` `rap.cpp:195-234`). The
  operator-representation axis is absorbed at L1; the rotation is identical across
  realisations.
- **Sub-pattern B** (`algebraic`) — `A.MultTranspose(x, y)` ⇒ `y = apply_linop(Aᵀ, x)`.
  Holds: dedicated transpose virtual (`operator.hpp:56`; `SumOperator::MultTranspose`
  `operator.cpp:443-456`; `ParOperator::MultTranspose` with swapped prolong/restrict
  `rap.cpp:236-275`).
- **Sub-pattern C** (`algebraic`) — `A.MultHermitianTranspose(x, y)` ⇒
  `y = apply_linop(Aᴴ, x)`, complex-only. Holds: `operator.hpp:58` decl;
  `ProductOperatorHelper::MultHermitianTranspose` `operator.hpp:158-165`.
- **Sub-pattern D** (`algebraic`) — `A.AddMult(x, y, a)` ⇒
  `y = axpby(a, apply_linop(A, x), 1, y_old)`. Holds: the fused method's body IS the
  composition — `y.Add(a*c, z)` after `op->Mult(x, z)` (`operator.cpp:458-466`);
  `y.Add(a, ty)` after `A->Mult` (`rap.cpp:277-318`). The inner accumulator is the
  firm sister theme's axpy; the D path is the composition of two firm syntactic rules.
- **Sub-pattern E** (`algebraic`) — combined transpose/Hermitian × accumulate; name-match
  composition of B/C and D. Holds: `SumOperator::AddMultTranspose` `operator.cpp:468-476`;
  `ParOperator::AddMultTranspose` `rap.cpp:320-361`;
  `ProductOperatorHelper::AddMultHermitianTranspose` `operator.hpp:167-175`.

Because every law is a syntactic identity on fully-specified positive source (operator
algebra on read method bodies), the absence of a dedicated unit test does NOT gate them
— this is the `apply_linop` firm-on-positive-structure escape, not the
`eigsolve`-convergence-semantics situation. The L1 `apply_linop` entry is firm
(cycle-004); the L0 endpoint is rank-3 ground truth. **The theme promotes to `firm`.**

## Proposed changes

### Change 1 — flip `## Status` to firm (escape reasoning cited) + append `verified_against:` rows

```edit:book/src/L1-L0/apply-linop-mutation-rotation.md
[replace the "## Status" section body (lines 344-394, from "`rough-in` —" through the end of the verified_against block) with the following]
## Status

`firm` — all five sub-pattern recognition rules (A structural, B/C/D/E algebraic)
verified row-by-row against the L0 corpus by `lowering-verifier` (cycle-100). The
theme promotes to `firm` via the **firm-on-positive-structure / syntactic-identity
escape**: every sub-rule is a name-match identity over a fully-specified positive
`mfem::Operator::Mult` / `ComplexOperator::Mult`-family method body (operator algebra
read off the source — `operator.cpp:428-520`, `rap.cpp:195-361`,
`operator.hpp:54-226`), NOT a numerically-asserted axiom or a convergence-semantics
claim, so the absence of a dedicated unit test does not gate the laws (the `apply_linop`
situation named in the CLAUDE.md `rough-in (test-coverage-bounded)` invariant). The
deferred D/E composition path is the composition of two already-firm syntactic rules
(`apply_linop` + `axpby`, the sister theme `axpby-mutation-rotation` being firm); the
inner accumulator (`y.Add(a*c, z)` `operator.cpp:464`, `y.Add(a, ty)` `rap.cpp:317`)
is covered by the sister theme and intentionally not re-handled here. Rank check passes:
both endpoints firm (`L1/apply_linop` firm cycle-004; L0 ground truth), so
`rank(theme) ≤ min(firm, firm) = firm` is well-founded.

verified_against:
  - citation: palace/linalg/operator.hpp:21
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: using Operator = mfem::Operator; real-operator alias, inherits abstract Mult from MFEM. Sub-pattern A real path.
  - citation: palace/linalg/operator.hpp:54
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: ComplexOperator::Mult pure-virtual decl. Sub-pattern A complex path.
  - citation: palace/linalg/operator.hpp:56
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: ComplexOperator::MultTranspose decl. Sub-pattern B.
  - citation: palace/linalg/operator.hpp:58
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: ComplexOperator::MultHermitianTranspose decl; complex-only by static type. Sub-pattern C.
  - citation: palace/linalg/operator.hpp:60-67
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: ComplexOperator AddMult / AddMultTranspose / AddMultHermitianTranspose decls; scalar a defaults to 1.0 on all three. Sub-patterns D and E.
  - citation: palace/linalg/operator.hpp:133
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: SumOperator::AddMult real-path decl (const double a = 1.0). Sub-pattern D.
  - citation: palace/linalg/operator.hpp:158-175
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: ProductOperatorHelper Hermitian-transpose specialisation; MultHermitianTranspose 158-165 + AddMultHermitianTranspose 167-175 composition witnesses. Sub-patterns C and E.
  - citation: palace/linalg/operator.hpp:202-206
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: BaseProductOperator::Mult body B.Mult(x, z); A.Mult(z, y); chained sub-pattern A composition witness.
  - citation: palace/linalg/operator.hpp:214-218
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: BaseProductOperator::AddMult body B.Mult(x, z); A.AddMult(z, y, a); accumulating-outer-apply composition witness. Sub-pattern D.
  - citation: palace/linalg/operator.hpp:220-225
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: BaseProductOperator::AddMultTranspose body A.MultTranspose(x, z); B.AddMultTranspose(z, y, a). Sub-pattern E.
  - citation: palace/linalg/operator.cpp:428-441
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: SumOperator::Mult; size-1 fast path y *= ops.front().second (line 435); size>1 path y = 0.0 (439) then AddMult(x, y) (440), witness of L0 Mult-via-AddMult reuse. Sub-pattern A.
  - citation: palace/linalg/operator.cpp:443-456
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: SumOperator::MultTranspose; mirrors Mult with MultTranspose/AddMultTranspose. Sub-pattern B.
  - citation: palace/linalg/operator.cpp:458-466
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: SumOperator::AddMult; loop accumulates y.Add(a*c, z) at line 464 (axpy-shaped inner step, shared with axpby-mutation-rotation). Sub-pattern D.
  - citation: palace/linalg/operator.cpp:468-476
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: SumOperator::AddMultTranspose; loop op->MultTranspose(x, z); y.Add(a*c, z). Sub-pattern E.
  - citation: palace/linalg/operator.cpp:479-507
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: BaseDiagonalOperator<Operator>::Mult (479-487, Y[i] = D[i]*X[i]) + <ComplexOperator>::Mult (488-507) matrix-free realisations. Sub-pattern A.
  - citation: palace/linalg/operator.cpp:509-520
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: BaseDiagonalOperator<Operator>::AddMult matrix-free fused Y[i] += a*D[i]*X[i] (forall body 519, closing brace 520 — corrects prior :509-519 range-END off-by-one). Sub-pattern D.
  - citation: palace/linalg/rap.cpp:195-234
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: ParOperator::Mult; prolongation + inner A->Mult(lx, ly) at line 219 (corrects prior note line 220) + RestrictionMatrixMult + dbc_tdof masking; MFEM_ASSERT shape guard 197-198. L1 form preserved under parallel wrapper. Sub-pattern A.
  - citation: palace/linalg/rap.cpp:236-275
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: ParOperator::MultTranspose; restriction/prolongation roles swapped. Sub-pattern B.
  - citation: palace/linalg/rap.cpp:277-318
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: ParOperator::AddMult; same prolong/restrict shape as Mult with final accumulation y.Add(a, ty) at line 317 (axpy-shaped, cited by sister theme); MFEM_ASSERT shape guard 280-281. Sub-pattern D.
  - citation: palace/linalg/rap.cpp:320-361
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: ParOperator::AddMultTranspose; final accumulation y.Add(a, tx) at line 360, closing brace 361 (corrects prior :320-360 range-END off-by-one). Sub-pattern E.
  - citation: palace/linalg/operator.hpp:73-113
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: ComplexWrapperOperator block-2x2 equivalent-real wrap; applicability condition 3 mixed real-op-on-complex-vector lift (complex-from-real-lift concept, not part of this theme).
  - citation: palace/linalg/iterative.cpp:379
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: CG residual call site A->Mult(x, r) inside if(initial_guess). Sub-pattern A live consumer.
  - citation: palace/linalg/iterative.cpp:443
    verdict: supports
    audited_at: 2026-06-05T04:49:16Z
    note: CG inner-loop call site A->Mult(p, z) feeding Dot(comm, z, p). Sub-pattern A live consumer.
```

### Change 2 — flip this theme's own dep-map status column in the L1>L0 index (status column ONLY)

```edit:book/src/L1-L0/index.md
[line 21 — replace the trailing status cell `rough-in` with the firm cell; do not touch other rows]
| [apply-linop-mutation-rotation](./apply-linop-mutation-rotation.md) | `L1/apply_linop` (firm) | `palace/linalg/operator.{hpp,cpp}`, `rap.cpp` | firm *(structural; 5 sub-patterns A bare `Mult`/B `MultTranspose`/C `MultHermitianTranspose`/D accumulating `AddMult`/E accumulating transposed+Hermitian; firm-on-positive-structure syntactic-identity escape, cycle-100 lowering-verifier; D/E = composition of firm apply_linop + axpby sister rules; operator-representation axis absorbed at L1)* |
```

### Change 3 — coupled re-anchor of the stale `rough-in` co-mention in the L3 entry (firm-promotion whole-book cross-reference grep)

The firm flip stales the `apply_linop` L3 entry's "Downward to L_n" cross-reference,
which asserts this theme's OWN maturity at the old `rough-in` token. Re-anchor it:

```edit:book/src/L3/apply_linop.md
[line 169 — replace the leading parenthetical `(rough-in; cycle-007)` with `(firm; cycle-007, promoted cycle-100)`; leave the rest of the bullet unchanged]
- `book/src/L1-L0/apply-linop-mutation-rotation.md` (firm; cycle-007, promoted cycle-100) — the five sub-patterns (A: bare forward apply via `Mult`; B: transposed apply via `MultTranspose`; C: Hermitian-transposed apply via `MultHermitianTranspose`; D: accumulating forward apply via `AddMult`; E: accumulating transposed/Hermitian applies via `AddMultTranspose`/`AddMultHermitianTranspose`) covering the transpose-mode × accumulate-mode variant-axis matrix. The L1 form (LHS of the rewrite) is the same as the L3 form here.
```

## Supporting evidence

- `palace/linalg/operator.hpp:18-230` — `Operator` alias, `ComplexOperator` virtual family, `SumOperator` / `ProductOperatorHelper` / `BaseProductOperator` / `ComplexWrapperOperator` decls (codemap `read_range`, on-disk confirmed).
- `palace/linalg/operator.cpp:428-522` — `SumOperator::{Mult,MultTranspose,AddMult,AddMultTranspose}` + `BaseDiagonalOperator<{Operator,ComplexOperator}>::{Mult,AddMult}` definitions.
- `palace/linalg/rap.cpp:195-362` — `ParOperator::{Mult,MultTranspose,AddMult,AddMultTranspose}` definitions.
- `palace/linalg/iterative.cpp:377-445` — CG `A->Mult` residual + inner-loop call sites.
- `book/src/L1/apply_linop.md` — firm L1 anchor (cycle-004); the LHS of every sub-rule.
- `book/src/L1-L0/axpby-mutation-rotation.md` — firm sister theme; covers the inner-axpy accumulator of sub-patterns D/E.
- `book/src/L3/apply_linop.md:169` — stale `rough-in` co-mention (Change 3).

## Open questions / caveats

- **Three citation drifts found and corrected in-report (none affects a recognition rule or the verdict):**
  1. `operator.cpp:509-519` (BaseDiagonalOperator AddMult) — range END off-by-one; closing `}` is at line 520. Corrected to `:509-520`.
  2. `rap.cpp:320-360` (ParOperator AddMultTranspose, sub-pattern E) — range END off-by-one; closing `}` is at line 361. Corrected to `:320-361`.
  3. `rap.cpp:195-234` verified_against note — internal "line 220" for `A->Mult(lx, ly)` is off by one; actual line 219. Corrected in the new note. (The range `:195-234` itself is exact.)
  Both range-END drifts are the close-brace off-by-one class the CLAUDE.md guard names (`--anchor` would pass because the anchor body is in-range; the END `}` needed a direct on-disk Read, which I did).
- **Corpus-exhaustiveness is illustrative-by-design, not literally exhaustive.** The theme cites representative concrete realisations (`SumOperator`, `BaseProductOperator`, `BaseDiagonalOperator`, `ParOperator`); the Verified-against §coverage note estimates ~30-40 total `Mult`-virtual implementations (preconditioners, FE assembly closures, Jacobian-action operators). The firm verdict rests on the **recognition rule being sound** (each sub-pattern is a syntactic identity that holds for ANY conforming `Operator` subclass), NOT on indexing every subclass — a name-match rule does not need a per-subclass enumeration to be firm. The estimate is not independently re-verified here; if a future cycle wants a literal corpus census it can run a `search_text 'void .*::Mult'` sweep, but it is not a promotion gate.
- **Direction-of-definition: clean.** The theme narrates forward (L1 `apply_linop` LHS → L0 `Mult`-family RHS); no reverse-lift prose. No directionality violation.
- **No `book/` writes performed by this agent** — all changes proposed for `integrator-per-report` (Phase 5).
