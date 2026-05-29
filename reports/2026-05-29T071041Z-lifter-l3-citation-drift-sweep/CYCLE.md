---
agent: lifter
invoked_at: 2026-05-29T071041Z
scope: L3 mechanical citation-drift sweep — ksp_solve.md (:464→:463, :564→:563) + inner-product-fold-specialization.md (operator.cpp :623→:624, :632→:634, :615-616→:616)
status: pending
integrated_at: 2026-05-29T1130Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-022 report 5/9 (wave-1). Applied clean — pure citation-drift sweep, 5 distinct inline-anchor re-anchors across L3/ksp_solve.md + L2-L1/inner-product-fold-specialization.md; both entries stay firm, 0 count delta. Enacts the inner-product theme's own embedded cycle-021 audit_caveat. retroactive-budget 0; build clean. See reports/cycle-022-integrator-staging/STAGING.md row 5 + reports/2026-05-29T1130Z-integrator-finalize-cycle-022/CYCLE.md."
inputs:
  - book/src/L3/ksp_solve.md
  - book/src/L2-L1/inner-product-fold-specialization.md
  - reference/palace/palace/linalg/iterative.cpp (source-of-truth, self-verified)
  - reference/palace/palace/linalg/operator.cpp (source-of-truth, self-verified)
---

# CYCLE: Re-anchor L3 citation-drift sweep (ksp_solve + inner-product-fold-specialization)

## Summary
Pure mechanical citation-line maintenance over two **firm** entries — no prose/semantic change, no status change. Both entries stay `firm`. (1) `book/src/L3/ksp_solve.md` carried two inline source anchors that had drifted by +1 line against the live `iterative.cpp`: the CG **in-loop** convergence test `converged = (res < eps)` was cited at `:464` but sits at `:463` (`:464` is the loop's closing brace), and the GMRES restart loop `for (; it < max_it; restart++)` was cited at `:564` but sits at `:563` (`:564` is its opening brace). (2) `book/src/L2-L1/inner-product-fold-specialization.md` carried three inline `operator.cpp` anchors flagged by its own embedded `verified_against` lowering-verifier audit (cycle-021): the real-`Operator` weighted-`Dot` workspace `ComplexVector Ax(A.Height())` cited at `:623` sits at `:624`; the `ComplexOperator` sibling's `Ax` cited at `:632` sits at `:634`; the complex-`Norml2` SPD assertion `MFEM_ASSERT(dot.real() > 0.0 && ...)` cited as range `:615-616` is a single line at `:616` (`:615` is the `dot = Dot(...)` line). Every corrected `path:lo-hi` was self-verified line-exact via `palace-codemap` `read_range` against `reference/` source this dispatch. The OQ-suggested corrections (`463`/`563` for ksp_solve; `624`/`634`/`616` for the inner-product theme) all match source.

## Proposed changes

### Entry 1 — `book/src/L3/ksp_solve.md`

Two drifted point-anchors, each appearing in multiple sentences. `:464`→`:463` (CG in-loop convergence test) and `:564`→`:563` (GMRES restart loop). The CG loop-guard `:427`, the pre-loop test `:417-418`, CG result `:484-485`, GMRES result `:703-704`, and the GMRES `Mult` span `:544-705` were all re-verified and are **correct** — left untouched. The body-span range `:434-464` (line 185) stays as a range (`:464` there is the loop-body's genuine closing brace) — only the embedded point anchor for the convergence test within that same sentence corrects to `:463`.

```edit:book/src/L3/ksp_solve.md
[old]: The fold's predicate `\s -> not s.converged && s.it < op.max_it` is the **convergence test** (per [`convergence-test`](../concepts/convergence-test.md)). It is the L3 rendering of the L0 loop-guard `it < max_it && !converged` (`reference/palace/palace/linalg/iterative.cpp:427`) with the per-step convergence flag `converged = (res < eps)` (`:464`) folded into `s.converged` by the kernel's `outputs.residual_norm` readout.
[new]: The fold's predicate `\s -> not s.converged && s.it < op.max_it` is the **convergence test** (per [`convergence-test`](../concepts/convergence-test.md)). It is the L3 rendering of the L0 loop-guard `it < max_it && !converged` (`reference/palace/palace/linalg/iterative.cpp:427`) with the per-step convergence flag `converged = (res < eps)` (`:463`) folded into `s.converged` by the kernel's `outputs.residual_norm` readout.
```

```edit:book/src/L3/ksp_solve.md
[old]: the predicate reads `s.converged` (set from `outputs.residual_norm < eps`, the L0 `converged = (res < eps)` at `:464`). The fold is published as a tail recursion
[new]: the predicate reads `s.converged` (set from `outputs.residual_norm < eps`, the L0 `converged = (res < eps)` at `:463`). The fold is published as a tail recursion
```

```edit:book/src/L3/ksp_solve.md
[old]: GMRES/FGMRES are a **double-nested** fold: the outer restart loop `for (; it < max_it; restart++)` (`reference/palace/palace/linalg/iterative.cpp:564`) wraps the inner Arnoldi-iteration fold.
[new]: GMRES/FGMRES are a **double-nested** fold: the outer restart loop `for (; it < max_it; restart++)` (`reference/palace/palace/linalg/iterative.cpp:563`) wraps the inner Arnoldi-iteration fold.
```

```edit:book/src/L3/ksp_solve.md
[old]: the L0 `for`-loop (`reference/palace/palace/linalg/iterative.cpp:427` for CG; `:564` for GMRES restart) re-expressed as a value-threaded tail recursion.
[new]: the L0 `for`-loop (`reference/palace/palace/linalg/iterative.cpp:427` for CG; `:563` for GMRES restart) re-expressed as a value-threaded tail recursion.
```

```edit:book/src/L3/ksp_solve.md
[old]: GMRES/FGMRES are a restart-nested double fold (outer restart loop `:564` wrapping the inner Arnoldi fold).
[new]: GMRES/FGMRES are a restart-nested double fold (outer restart loop `:563` wrapping the inner Arnoldi fold).
```

```edit:book/src/L3/ksp_solve.md
[old]: it selects the outer restart loop's re-seed cadence (`max_dim`-bounded inner cycles, outer loop `reference/palace/palace/linalg/iterative.cpp:564`). This is the *outer* of the two loops; it is loop-shaping by definition.
[new]: it selects the outer restart loop's re-seed cadence (`max_dim`-bounded inner cycles, outer loop `reference/palace/palace/linalg/iterative.cpp:563`). This is the *outer* of the two loops; it is loop-shaping by definition.
```

```edit:book/src/L3/ksp_solve.md
[old]: the per-step body folding `krylov-step` (`:434-464`, with the in-loop convergence test `converged = (res < eps)` at `:464`); result extraction `final_res = res; final_it = it;` (`:484-485`).
[new]: the per-step body folding `krylov-step` (`:434-464`, with the in-loop convergence test `converged = (res < eps)` at `:463`); result extraction `final_res = res; final_it = it;` (`:484-485`).
```

```edit:book/src/L3/ksp_solve.md
[old]: The outer restart loop `for (; it < max_it; restart++)` (`:564`); result extraction `final_res = beta; final_it = it;` (`:703-704`).
[new]: The outer restart loop `for (; it < max_it; restart++)` (`:563`); result extraction `final_res = beta; final_it = it;` (`:703-704`).
```

### Entry 2 — `book/src/L2-L1/inner-product-fold-specialization.md`

Three drifted inline `operator.cpp` anchors in the prose (`:623`→`:624`, `:632`→`:634`, `:615-616`→`:616`). **Left untouched (verified correct, NOT drift):** the `:612` SPD-comment anchor (line 423); the `:615` entry inside the `conjugation_caller_inventory` YAML (line 318) — that block enumerates `linalg::Dot` *caller* sites, and `:615` is exactly the `std::complex<double> dot = Dot(comm, Bx, x);` call line, so it correctly points at the Dot call site, not the assertion. The embedded `verified_against` YAML audit block + `audit_caveat` (lines 540-605) are the integrated cycle-021 lowering-verifier audit record that *documents* this drift and its corrections; they are descriptive findings, left verbatim (append-only audit record).

```edit:book/src/L2-L1/inner-product-fold-specialization.md
[old]: that the L0 weighted `Dot` allocates (`ComplexVector Ax(A.Height())`,
`palace/linalg/operator.cpp:623,632`) — the Category-4 "synthetic workspace" instance of
[new]: that the L0 weighted `Dot` allocates (`ComplexVector Ax(A.Height())`,
`palace/linalg/operator.cpp:624,634`) — the Category-4 "synthetic workspace" instance of
```

```edit:book/src/L2-L1/inner-product-fold-specialization.md
[old]:   allocates `ComplexVector Ax(A.Height())` (`:623`), `A.Mult(x.Real(), Ax.Real())` /
[new]:   allocates `ComplexVector Ax(A.Height())` (`:624`), `A.Mult(x.Real(), Ax.Real())` /
```

```edit:book/src/L2-L1/inner-product-fold-specialization.md
[old]:   complex (`:608-618`): the B-weighted norm `√ Dot(comm, Bx, x)`, with the SPD assertion
  `dot.real() > 0.0 && |dot.imag()| < 1e-9·dot.real()` (`:615-616`, comment "For SPD B,
  xᴴ B x is real" at `:612`). The `matrix-weighted-norm` consumer + law-5/diagonal
[new]:   complex (`:608-618`): the B-weighted norm `√ Dot(comm, Bx, x)`, with the SPD assertion
  `dot.real() > 0.0 && |dot.imag()| < 1e-9·dot.real()` (`:616`, comment "For SPD B,
  xᴴ B x is real" at `:612`). The `matrix-weighted-norm` consumer + law-5/diagonal
```

Note: the `:632` workspace anchor appears only inside the `:623,632` compound on line 142 (corrected in the first inner-product edit above). The Evidence-section ComplexOperator citation (line 418-419) cites the function span `:631-638` and prose `A.Mult(x, Ax)` without an inline `Ax` line-anchor, so no separate `:632`/`:634` point-edit is needed there.

## Discipline notes
- **Pure citation maintenance — no status change, no prose/semantic change.** Both entries remain `firm`. This is the `verify-citation-range` "producer self-verification" sweep applied as a standalone re-anchor: each emitted `path:lo-hi` was `read_range`-confirmed line-exact this dispatch before being written into the proposed edits.
- **What I changed and why (per anchor, source-confirmed):**
  - `iterative.cpp` CG in-loop convergence test `converged = (res < eps)` is at **`:463`** (line `:464` is the loop's closing `}`). Confirmed via `read_range 460-487`. Entry's `:464`→`:463` (lines 74, 88, 185).
  - `iterative.cpp` GMRES restart loop `for (; it < max_it; restart++)` is at **`:563`** (line `:564` is its opening `{`). Confirmed via `read_range 560-566`. Entry's `:564`→`:563` (lines 88, 94, 102, 157, 161, 186).
  - `operator.cpp` real-`Operator` weighted `Dot` workspace `ComplexVector Ax(A.Height())` is at **`:624`** (`:623` is the `{`). Confirmed via `read_range 598-640`. Entry's `:623`→`:624` (lines 142, 415).
  - `operator.cpp` `ComplexOperator` weighted `Dot` workspace `ComplexVector Ax(A.Height())` is at **`:634`** (`:632` is the decl's second line). Confirmed same read. Entry's `:632`→`:634` (line 142).
  - `operator.cpp` complex-`Norml2` SPD assertion `MFEM_ASSERT(dot.real() > 0.0 && std::abs(dot.imag()) < 1.0e-9 * dot.real(), ...)` is a single line at **`:616`** (`:615` is `std::complex<double> dot = Dot(comm, Bx, x);`). Confirmed same read. Entry's range `:615-616`→`:616` (line 423).
- **NOT a content correction.** No backward conventions, no drifted-claim fixes beyond the line numbers — the cited *constructs* and the surrounding prose are correct; only the line integers moved. This is within "Touch evidence pointers … re-anchoring a citation that broke" — strictly the line-number half.
- **Anchors re-verified and left untouched** (guarding against over-correction): ksp_solve `:417-418`, `:427`, `:484-485`, `:703-704`, `:544-705`, `:361-486`; inner-product `:612` (SPD comment), `:615` (the `Dot` call-site row in the caller-inventory YAML, distinct from the assertion), `:621-638`/`:621-628`/`:631-638` (function spans), `:603` (real Norml2 Dot caller). All confirmed correct against source this dispatch.

## Supporting evidence
- Source self-verification (this dispatch, `palace-codemap` `read_range`):
  - `reference/palace/palace/linalg/iterative.cpp:413-430` — CG setup: `eps = std::max(...)` `:417`, pre-loop `converged = (res < eps)` `:418`, loop guard `for (; it < max_it && !converged; it++)` `:427`.
  - `reference/palace/palace/linalg/iterative.cpp:460-487` — CG in-loop: `converged = (res < eps)` **`:463`**, closing `}` `:464`, `final_res = res;` `:484`, `final_it = it;` `:485`.
  - `reference/palace/palace/linalg/iterative.cpp:560-566` — GMRES restart loop `for (; it < max_it; restart++)` **`:563`**, opening `{` `:564`.
  - `reference/palace/palace/linalg/iterative.cpp:700-705` — GMRES result `final_res = beta;` `:703`, `final_it = it;` `:704`, `Mult` close `}` `:705`. (`search_text final_res = (res|beta)` corroborates `:484` / `:703`.)
  - `reference/palace/palace/linalg/operator.cpp:598-638` — real-`Operator` `Dot`: workspace `ComplexVector Ax(A.Height())` **`:624`**; `ComplexOperator` `Dot`: workspace `ComplexVector Ax(A.Height())` **`:634`**; complex-`Norml2`: SPD comment `:612`, `dot = Dot(...)` `:615`, SPD assertion **`:616`**.
- OQ sources: `l3-ksp-solve-citation-drift-463-563-correction`; `inner-product-fold-specialization-operator-cpp-inline-anchor-drift`. Both OQ-suggested corrections match source.
- The inner-product theme's own embedded `verified_against` audit (lines 540-605, cycle-021 lowering-verifier) independently flagged these three `operator.cpp` drifts with the same target lines (`:624` / `:634` / `:616`) — this dispatch enacts that already-recorded `audit_caveat` ("citation-correction follow-up, not a status reduction").

## Open questions / caveats
- **No re-architecture, no signature shift.** The firmed-up constructs are unchanged; this is the pure line-number half of a re-anchor. No abstractor reread needed.
- **Integrator note (OQ closure):** applying these edits resolves OQ `l3-ksp-solve-citation-drift-463-563-correction` and OQ `inner-product-fold-specialization-operator-cpp-inline-anchor-drift` — recommend close/migrate. The inner-product theme's `audit_caveat` line (605) may be left as-is (append-only integrated audit record) or, if the integrator prefers, annotated as "enacted cycle-022"; I did not propose editing the audit block to avoid mutating an integrated audit record.
- **Body-range `:434-464` (ksp_solve line 185) intentionally kept as a range.** The `:464` inside that compound is the loop-body's closing brace (a legitimate span endpoint); only the explicit convergence-test point anchor in the same sentence corrected to `:463`. If a future lowering-verifier prefers the body range to end at the convergence test (`:434-463`), that is a stylistic tightening, not a drift fix — out of this dispatch's mechanical scope.
