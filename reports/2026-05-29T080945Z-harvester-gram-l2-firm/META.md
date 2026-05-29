---
verifies: ../REPORT.md
critiqued_at: 2026-05-29T091500Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-29T093000Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Formalize gram at L2" (firm promotion)

## Critique

### Checks run

**citation-validity — pass.** All 14 evidence-section ranges plus every inline pinpoint were verified by `read_range` and `tools/citecheck/citecheck.py --scan` (26 citations extracted, 26 ok, 0 failing — citecheck's superset includes the inline citations beyond the 14 evidence rows). The load-bearing sole-Gram-build site `palace/linalg/nleps.cpp:524-531` reads exactly as claimed: `Eigen::MatrixXcd SS(k, k);` (`:524`), the double-loop `for i { for j { SS(i, j) = linalg::Dot(GetComm(), X[i], X[j]); } }` (`:525-531`, cell body on `:529`). The supporting ranges all confirm: `k==0` early return (`:515-518`), coordinate-extraction `x2(j) = b2(j) - linalg::Dot(GetComm(), x1, X[j])` (`:520-523`), Schur-modify + LU-solve chain (`:532-535`), `deflated_solve` lambda + block comment `SS = (B - A T^-1 U) = - X^* X S^-1` (`:504-537`, comment at `:512-513`), the `:561-569` and `:660-668` second/third Gram-solve consumers, `MatVecMult` (`:329-347`), the literature anchors Effenberger 2013 / Jarlebring-Koskela-Mele 2018 / SLEPc-NEP minimality-index-1 (`:354-362`), basis growth `X.resize(k+1); X[k]=v; ...; k++` (`:613-619`), and the live call site (`:542`). The coverage-caveat non-instance `palace/models/romoperator.cpp:757-765` reads as `Ar.ldlt().solve` / `Ar.selfadjointView<...>().ldlt().solve` / `Ar.fullPivHouseholderQr().solve` on a reduced operator `Ar` — confirmed NOT an `XᴴX` Gram build. The two inner_product anchoring citations (`test/unit/test-vector.cpp:206-207` real-member value test, `palace/linalg/operator.cpp:615-616` SPD-realness `MFEM_ASSERT`) both read as claimed. I independently re-ran the caveat search predicates: `fullPivLu|Gram|deflat` over `palace/**/*.cpp` returns hits **only** in `nleps.cpp` (romoperator uses `ldlt`/`fullPivHouseholderQr`, never `fullPivLu`), and `nleps|deflat|MatVecMult|invariant pair` over `palace/test/**` returns **zero** hits — both coverage-caveat claims are sound.

**surface-or-evidence — pass.** This is not a refinement of an existing operator; it is a firm-promotion authoring a `new:book/src/L2/gram.md` chapter (surface) backed by a positive source site. The proposed chapter modifies surface and the firm judgment is grounded in the read source (`nleps.cpp:524-531`) plus the firm parent `inner_product`. Not a pure rotation_claim; not a retroactive-evidence-only backfill. Surface + evidence both present.

**rotation-quality — pass.** The L2 fusion rotation is genuine and strictly more compact/abstract than the L0 form: Palace's fused double `for`-loop of `linalg::Dot` calls (`nleps.cpp:525-531`) is de-fused into the named all-pairs `inner_product` fold `gram dot X = Matrix (\i j -> dot X[j] X[i])`. This is state/loop-structure compression (an explicit nested mutation loop collapses into a single equational matrix-comprehension over the firm scalar fold), not a 1:1 rename. The conjugation reconciliation is the load-bearing simplification the lift buys: `linalg::Dot(comm, a, b) = bᴴa` conjugates arg-2 (confirmed against `dot.md:43`), so `SS(i,j) = linalg::Dot(GetComm(), X[i], X[j]) = X[j]ᴴX[i] = inner_product(X[j], X[i])` — pinned once at `gram` rather than re-derived per cell. The off-diagonal is correctly identified as the convention-sensitive part, diagonal as convention-invariant (real).

**variant-axis-coverage — pass.** Three orthogonal axes are declared and each combination is addressed: (1) `dot` hook ∈ {canonical Hermitian, B-weighted} → `XᴴX` vs `XᴴBX`; (2) single-set vs cross-Gram (`gram` vs `gram2`, single-set ≡ diagonal block of cross); (3) element-type ∈ {real, complex}, absorbed by the hook. Two candidate axes are explicitly scoped OUT with justification: symmetry-exploitation is named a transparent perf-trick non-law (Palace's `:525-531` computes all k² cells, no triangle-exploit), and basis cardinality `k` is the natural fold parameter (variadic-in-k, certified by the incremental-Gram law 6), not a fixed-k specialization family. No hidden branches.

**cross-reference-integrity — pass (build-readiness guard PASSES).** Fence enumeration: 6 markers (even parity). Nesting is balanced — outer `new:book/src/L2/gram.md` (line 47) → nested ` ```text ``` ` Signature fence (89–97) → outer close (386); then `edit:book/src/L2/index.md` (388–390). **The full firm apparatus is INSIDE the `new:` fence:** `## Status` (firm) at 291, `## Signature` at 87, `## Algebraic laws` at 158, `## Evidence` at 327 — all between the open (47) and close (386). This is the OPPOSITE of the cycle-019 fence-truncation defect (where the firm body was authored as the report's own top-level sections OUTSIDE the fence); here the report's own scaffolding (`## Summary`, `## Proposed changes`) correctly sits before line 47 and the chapter body is fully enclosed. The 3-backtick-outer-enclosing-3-backtick-`text` nesting is a PROVEN-parseable pattern: the landed-firm `ksp_solve` L2 report (`2026-05-29T051532Z-harvester-l2-ksp-solve-firm`) used the identical structure (`edit:` outer at line 27, nested `text` fences at 68–78 / 82–92, outer close at 215) and integrated cleanly cycle-021; `inner_product.md`/`ksp_solve.md` both carry nested text fences in their landed form. All live `[link]`s resolve: `[inner_product](./inner_product.md)`, `[dot](../L1/dot.md)`, `[orthogonalize](./orthogonalize.md)` all exist; the cited section anchors are real (`inner_product.md` §"Conjugation convention (pinned)":46, §"Algebraic laws":184, §"Sibling fold":364; `dot.md:43`; `orthogonalize.md:40-44,67-71,73-76`). The `deflate` forward-reference is correctly **plain-text everywhere** (no `[deflate](./deflate.md)` live link anywhere — verified by grep) — `deflate.md` does not yet exist (the parallel wave-2 sibling), so plain-text is the build-safe choice per `rough-in-forward-reference-must-be-plain-text-not-live-link`; no dead-link build error.

**edge-label-fidelity — pass (n/a-ish).** This is an L2 operator entry, not a lowering-theme entry; it carries no `L_{n+1}→L_n` edge label. The L2>L1 lowering is explicitly forward-referenced as forthcoming abstractor work and not authored here. The one directional claim made (L2 all-pairs fold de-fuses Palace's L0 double-loop) is narrated in the correct forward direction (L2 unfolds toward L1/L0). No edge mislabeling.

**plan-kind-consistency — pass.** Declared kind is `firm` and the content shape matches: complete Signature with shape contract, six numbered algebraic laws each tied to an inner_product law, four explicit non-laws, three variant axes, a Dependencies block, and a 14-range Evidence section with a bounded coverage caveat. No rough-in placeholders. The firm-on-positive-structure route is correctly invoked: every law is a syntactic identity on the firm `inner_product` fold (verified — laws 1–6 each lift a confirmed `inner_product` law 1/2/4/5; the IEEE and Cauchy-Schwarz non-laws are inherited from the parent's stated non-laws at `inner_product.md:241,253`), so the absent NLEPS test does not gate firmness per the cycle-021 `apply_nonlinear_pencil`/`apply_linop` codification. The coverage caveat is framed as a non-status-reduction with a closed-form promotion condition, matching the directive's posture. The dep-map row status cell (`firm (cycle-022; ...)`) is consistent with the chapter `## Status` (firm) — the orchestrator completion is faithful (see Issue 1).

**skill-uptake-survey — warning (non-blocking).** The report's shape implies several relevant skills exist and were exercised in substance but not named: `verify-citation-range` (the `read_range` + `citecheck` 14/14 pass is exactly its procedure), `verify-rotation-citation`/`propose-rotation` (the de-fusion rotation), `classify-variant-axis` (the three-axis + two-scoped-out enumeration), and the cycle-021 `proposed-changes-fence-encloses-full-body-guard` (the firm-body-inside-fence discipline the report visibly honored). The report references the citecheck tool and cycle-021 status-tier codification by name but does not cite any `skills/<name>` invocation. Pure telemetry — surfaces under-naming of skill uptake, does not block.

### Issues found

1. **(severity: low — verification of orchestrator completion, NOT a defect) `book/src/L2/index.md` dep-map row completion is faithful.** The transparency note flagged that a transient API 529 truncated the original `edit:book/src/L2/index.md` block, completed surgically by the orchestrator. I verified the completed row at `CYCLE.md:389` against the chapter content: the row flips the name to live link `[gram](./gram.md)`, the signature cell matches the chapter Signature verbatim (`(dot: (Tensor[N], Tensor[N]) -> Scalar, X: Basis[N, k]) -> Matrix[k, k]`, arg-1-conjugated, entry `(i,j) = ⟨X[j], X[i]⟩ = X[j]ᴴ X[i]`), the dependency cell correctly names the `inner_product` constituent + `dot` L1 kernel + hook axis + Hermitian/PSD/PD-iff-full-rank + diagonal-real + incremental-Gram block law + `deflate` consumer, and the status cell `firm (cycle-022; all-pairs inner_product syntactic-identity laws on the positive Gram-build site nleps.cpp:524-531; firm-on-positive-structure)` is consistent with the chapter `## Status` (firm) and its rationale. **Conclusion: the orchestrator completion is a faithful surgical close, not a fabrication — it accurately reflects the chapter content.** No repair needed; recorded for the integrator's confidence.

2. **(severity: informational) The `edit:book/src/L2/index.md` block carries ONLY the replacement firm row, not the surrounding multiline rough-in row it replaces.** The current `book/src/L2/index.md:54` rough-in row (`| `gram` *(rough-in; no anchor yet)* | ... | rough-in (proposed-by combinator-miner...) |`) is a single table row; the `edit:` block (CYCLE.md:388–390) supplies the single replacement firm row without an explicit `[old]:`/`[new]:` delimiter pair. The integrator must locate the existing rough-in row by its `gram` left-cell and substitute. This matches the surgical-row-replace convention used by the landed `ksp_solve`/`inner_product` index.md edits (their `edit:book/src/L2/index.md` blocks were likewise single-row), so it is within the established pattern — flagged only so the integrator-per-report applies it as a row-substitution (find the `gram` rough-in row, replace with the firm row), not an append. The `deflate` consumer row (index.md:55) is untouched and stays rough-in (correct — `deflate` is the parallel wave-2 sibling).

3. **(severity: very low — prose precision, not a citation error) PSD law 4 derivation understates its inner_product dependencies.** Algebraic law 4 (`gram dot X ⪰ 0`, PD iff full column rank) is described as "the pointwise lift of `inner_product`'s PSD-at-diagonal law 5." The `vᴴ G v = inner_product(Xv, Xv) ≥ 0` argument actually composes inner_product law 3 (sesquilinearity) with law 5 (diagonal-PSD) — law 5 alone gives only diagonal non-negativity, not the full quadratic-form PSD. The cited law 5 is the load-bearing one and the conclusion is mathematically sound (the matrix lift is correct), so this is a precision nit in the attribution prose, not a wrong claim. Optional tightening: "lift of inner_product law 5 via sesquilinearity (law 3)."

4. **(severity: informational — over-unification guard confirmed sound) `gram` is correctly NOT redundant with `inner_product` or `orthogonalize`, and `deflate` is consumer-not-merge.** Verified against the same-layer cohort: `gram` is the matrix-valued lift (`Matrix[k,k]`) of the scalar fold `inner_product` (`Scalar`) — distinct codomain, not a duplicate; the report states `gram` "does not replace inner_product; it is the all-pairs lift of it." The `orthogonalize` sibling distinction is sound and grounded (orthogonalize = the orthonormal-basis Gram-Schmidt with implicit `gram = I` and NO Gram-matrix/solve; `gram` is the explicit `XᴴX` build needed exactly when the basis is NOT orthonormal — matching the `deflate` rough-in's over-unification guard at index.md:55, and the non-orthonormality is source-grounded at `nleps.cpp:613-619` where the basis is raw-normalized, not orthonormalized). `deflate` is correctly classified as a consumer (NOT a constituent) — `gram` builds the matrix, `deflate` LU-solves it; the `lu_solve` primitive is `deflate`'s dependency, not `gram`'s. No over-unification.

## Repair

### Fixes attempted

- **Finding 1** (Issue 1 — orchestrator dep-map-row completion is faithful; severity low, verification-of-completion, NOT a defect).
  - **Decision**: not-needed.
  - **Rationale**: the critic verified the orchestrator-completed `book/src/L2/index.md` firm row (`CYCLE.md:392-394`) is a faithful surgical close that accurately reflects the chapter content — explicitly "no repair needed." Record-only confirmation for the integrator's confidence. Nothing for the repairer to apply.

- **Finding 2** (Issue 2 — the `edit:book/src/L2/index.md` block carries only the single replacement firm row, no `[old]`/`[new]` delimiter pair; severity informational).
  - **Decision**: not-needed.
  - **Rationale**: this matches the landed surgical-row-replace convention used by `ksp_solve` / `inner_product` (their `edit:book/src/L2/index.md` blocks were likewise single-row substitutions). It is within the established pattern; the integrator-per-report applies it as a row-substitution (locate the existing `gram` rough-in row by its left-cell, replace with the firm row), not an append. No edit; surfaced for integrator handling. The `edit:` block was left untouched and its fence remains balanced (markers at CYCLE.md:392/394).

- **Finding 3** (Issue 3 — PSD law 4 attribution understates its `inner_product` dependencies; severity very low, prose precision).
  - **Decision**: repaired.
  - **Action**: edited the `new:book/src/L2/gram.md` body in `CYCLE.md` (the `## Algebraic laws` section, law 4 "Positive semi-definiteness"). The attribution now reads as the matrix lift of `inner_product` PSD-at-diagonal law 5 **via sesquilinearity (law 3)**: sesquilinearity collapses `vᴴ G v` into `inner_product(Xv, Xv)`, then diagonal-PSD law 5 gives `≥ 0`; with an explicit parenthetical noting law 5 alone yields only per-entry diagonal non-negativity `G[i,i] ≥ 0`, and law 3 is what assembles the off-diagonal cross-terms into the quadratic form. The verb "pointwise lift" → "matrix lift" since the quadratic-form PSD is a genuine composition, not a pointwise per-cell consequence. Verified against `book/src/L2/inner_product.md` law numbering: law 3 = "Conjugate-linearity in arg-1, linearity in arg-2" (`:208-212`), law 5 = "Positive semi-definiteness at the diagonal" (`:218-227`). Mechanical attribution correction only — the conclusion (PSD lift, PD-iff-full-rank) was already mathematically sound and is unchanged; no new claim authored.

- **Finding 4** (Issue 4 — over-unification guard confirmed sound; `gram` not redundant with `inner_product`/`orthogonalize`, `deflate` consumer-not-merge; severity informational).
  - **Decision**: not-needed.
  - **Rationale**: critic confirmed the same-layer distinctions are sound and source-grounded (distinct codomain `Matrix[k,k]` vs `Scalar`; orthonormal-vs-non-orthonormal-basis split; `deflate` as consumer with `lu_solve` as ITS dependency). No defect. Record-only.

- **skill-uptake-survey** (critic `warning` — relevant skills exercised in substance but not named by slug: `verify-citation-range`, `verify-rotation-citation`/`propose-rotation`, `classify-variant-axis`, the cycle-021 fence-encloses-full-body guard).
  - **Decision**: not-needed.
  - **Rationale**: pure telemetry, explicitly non-blocking. The procedures were performed in substance (the 14/14 citecheck pass, the de-fusion rotation, the three-axis enumeration, the firm-body-inside-fence discipline) — only the by-slug naming is absent. Under-naming is not a repairable artifact defect and does not gate readiness.

### Unrepairable findings

None. All findings were either record-only/informational (not-needed) or a mechanical prose-attribution correction (repaired). No finding required substantive authoring or exceeded repair authority.

## Suggested resolution

`ready`. The firm promotion of `gram` at L2 is sound and well-evidenced (7 critic passes; the lone warning is non-blocking skill-uptake telemetry). Notes for the integrator:

- Apply the `edit:book/src/L2/index.md` block (CYCLE.md:392-394) as a **row-substitution**: find the existing `gram` rough-in row in `book/src/L2/index.md` (currently at `:54`, identified by its `gram` left-cell), replace it with the single firm row supplied. Do NOT append. The orchestrator-completed firm row was verified faithful to the chapter content (Issue 1). Leave the `deflate` consumer row (`:55`) untouched — it stays rough-in (parallel wave-2 sibling).
- The `deflate` forward-reference is correctly plain-text everywhere in the `gram.md` body (no live `[deflate](./deflate.md)` link); `deflate.md` does not yet exist, so plain-text is the build-safe choice. No dead-link build error.
- The law-4 attribution prose fix (Finding 3) is in the `new:book/src/L2/gram.md` body; both proposed-change fences remain balanced (6 markers, even parity, well-nested) after the repair.
