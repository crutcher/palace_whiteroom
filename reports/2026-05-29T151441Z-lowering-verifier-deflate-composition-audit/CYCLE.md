---
agent: lowering-verifier
invoked_at: 2026-05-29T15:19:15Z
scope: L2>L1 theme audit — deflate-composition-lowering
status: integrated
integrated_at: 2026-05-29T17:15:00Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-025 finalize (first primary cycle of meta-batch-7). Audit verdict gate STAYS-GATED-correctly → theme STAYS partly-constructive (NO status change; ## Status line untouched). Additive verified_against: YAML (19 entries, all supports) + gate_verdict: stays-gated-correctly block appended at EOF. No positive bare-Gram (XᴴX)⁻¹ Galerkin-core solve found in palace/*.cpp; the near-candidate romoperator.cpp:757-765 solves against Ar=VᴴAV (ROM system-operator pencil), not a Gram. The shared bare-Galerkin-core promotion gate STAYS OPEN, triple-referenced (L2 deflate :774 + L1>L0 nleps-deflated-solve + this L2>L1 theme). OQ RE-SCOPED (NOT closed): the 2nd of 4 slugs on open-questions.md:327 — audit half discharged, promotion-watch remains (co-keyed with deflate-galerkin-core-promotion at :35, trigger = a positive bare-Gram-solve site). retroactive-budget 0; clean build."
inputs:
  - book/src/L2-L1/deflate-composition-lowering.md
  - palace/linalg/nleps.cpp:505-537 (the positive deflated_solve block — firm Schur fan-down)
  - palace/linalg/nleps.cpp:329-347 (MatVecMult back-projection primitive)
  - palace/linalg/nleps.cpp:354-362 (deflation-scheme literature anchors)
  - palace/linalg/nleps.cpp:508-513, 562-563, 606-619, 664-667 (supporting positive sites)
  - palace/models/romoperator.cpp:74, 729-734, 757-765 (ROM Ar=VᴴAV solve — candidate unblock site, checked)
  - book/src/L2/deflate.md (LHS L2 composition + inherited Status/promotion gate)
  - book/src/L1/{lu_solve.md,dot.md}, book/src/L2/{gram.md,linear_combination.md}
---

# CYCLE: Audit deflate-composition-lowering

## Summary

Audited the `partly-constructive` L2>L1 theme `deflate-composition-lowering` (the
`coords ▷ (schur-)solve ▷ back-project` fan-down of the `deflate` composition) against concrete L0
evidence in `palace/linalg/nleps.cpp`, and assessed whether the audit unblocks the **shared,
triple-referenced bare-Galerkin-core promotion gate** (L2 `deflate` + L1>L0
`nleps-deflated-solve-mutation-rotation` + this L2>L1 theme all promote together). **Top-level
verdict: fully-supported** — every per-line anchor of the firm Schur-form fan-down (`nleps.cpp:505-537`)
verifies with **zero drift** (mechanically via `tools/citecheck/ --anchor` and independent codemap
`read_range`), and the constructive Galerkin-core sub-part is correctly held `partly-constructive`.
**Gate verdict: STAYS-GATED-correctly.** An exhaustive codemap search for any positive bare-Gram
`(XᴴX)⁻¹` deflation-coordinate solve — across every dense `.solve()` / `.inverse()` /
LU/LDLT/QR/Cholesky site in the Palace `*.cpp` tree — returns **no unwrapped Galerkin-core site**.
The one near-candidate (`romoperator.cpp:757-765`) solves against `Ar = VᴴAV`, a ROM-projected
**system operator** pencil, NOT a Gram matrix `XᴴX` — it does not unblock the gate. The
"NLEPS-scoped is acceptable" outcome (the bare-Gram core genuinely never appears unwrapped in
Palace, so the constructive sub-part is a faithful `S = I` reduction) is the realized verdict. The
negative anchor is both **correct and complete**. I AUDIT only — I did not mutate the theme.

**Skill uptake:** this audit followed `verify-citation-range` (the cycle-024 `tools/citecheck/ --anchor`/`--scan`
realization — every decisive pinpoint line carries an explicit `citecheck --anchor → line N, zero drift`
annotation) and `partly-constructive-promotion-checklist` (cycle-015 — the gate-verdict section assesses the
constructive Galerkin-core sub-part against its named promotion condition before concluding STAYS-GATED-correctly).

## Per-citation audit

### Firm Schur-form fan-down — the positive `deflated_solve` block

- **Citation**: `palace/linalg/nleps.cpp:505-537`
  - **Theme claim**: the complete fan-down target; `auto deflated_solve =` at `:505`, closing `};`
    at `:537`.
  - **Found**: `read_range :505-537` returns exactly that lambda; `:505` is
    `auto deflated_solve = [&](const ComplexVector &b1, ...)`, `:537` is `};`. citecheck bounds OK.
  - **Verdict**: **supports**.
  - **Notes**: file has 952 lines; range well in bounds.

- **Citation**: `palace/linalg/nleps.cpp:508-513` (source block-elimination comment).
  - **Theme claim**: `:512` names the Schur complement `SS = (B − A T⁻¹ U) = − XᴴX·S⁻¹`; `:513`
    says `x1 = x1 − X S x2`. Positive evidence the projector is Schur-modified, not bare Gram.
  - **Found**: `:512` is `// x2 = SS^-1 (b2 - A x1) where SS = (B - A T^-1 U) = - X^* X S^-1`;
    `:513` is `// x1 = x1 - X S x2`. Exact match.
  - **Verdict**: **supports**. This is the decisive in-source evidence the projector IS
    Schur-wrapped (so the bare-Gram core is genuinely a *reduction*, not the implemented form).

- **Citation**: `palace/linalg/nleps.cpp:515-518` (Stage 0 empty-basis short-circuit).
  - **Theme claim**: `if (k == 0) { return; }`.
  - **Found**: `:515` `if (k == 0)  // no deflation`, `:516` `{`, `:517` `return;`, `:518` `}`. Exact.
  - **Verdict**: **supports**.

- **Citation**: `palace/linalg/nleps.cpp:519-523` (Stage 1 coordinate extraction; decisive line `:522`).
  - **Theme claim**: `:519` `x2.conservativeResize(k)`; the loop; decisive `:522`
    `x2(j) = b2(j) − linalg::Dot(GetComm(), x1, X[j])`.
  - **Found**: `:519` `x2.conservativeResize(k);`, `:520` `for (int j = 0; j < k; j++)`, `:522`
    `x2(j) = b2(j) - linalg::Dot(GetComm(), x1, X[j]);`. citecheck `--anchor 'x2(j) = b2(j) -
    linalg::Dot'` → anchor at line **522**, zero drift.
  - **Verdict**: **supports**. The `b2 −` term is correctly identified as the extended-block RHS
    (NLEPS shift); the `−linalg::Dot(...)` is the deflation coordinate `X[j]ᴴ x1`.

- **Citation**: `palace/linalg/nleps.cpp:524-531` (Stage 2 Gram build; `:524` materialization,
  `:529` assignment).
  - **Theme claim**: `Eigen::MatrixXcd SS(k, k)` at `:524`; `SS(i, j) = linalg::Dot(GetComm(),
    X[i], X[j])` at `:529`.
  - **Found**: `:524` `Eigen::MatrixXcd SS(k, k);`; `:529` `SS(i, j) = linalg::Dot(GetComm(),
    X[i], X[j]);`. citecheck `--anchor 'SS(i, j) = linalg::Dot'` → anchor at line **529**, zero drift.
  - **Verdict**: **supports**. The buffer-aliasing note (theme: Palace names the Gram buffer `SS`
    and overwrites it in place at `:533` with the Schur-modified form) is independently confirmed —
    `SS` holds the bare Gram `XᴴX` at `:524-531` and is overwritten to `−S⁻¹(XᴴX)` at `:533`. Sharp
    and correct.

- **Citation**: `palace/linalg/nleps.cpp:532` (Stage 3 Schur block).
  - **Theme claim**: `S = scale(eig_opInv) Identity(k) − H`.
  - **Found**: `:532` `const Eigen::MatrixXcd S = eig_opInv * Eigen::MatrixXcd::Identity(k, k) - H;`.
    citecheck regex `--anchor 'eig_opInv \* Eigen::MatrixXcd::Identity'` → anchor at **532**, zero drift.
  - **Verdict**: **supports**.

- **Citation**: `palace/linalg/nleps.cpp:533` (Stage 3 multi-RHS solve).
  - **Theme claim**: `SS = lu_solve(S, scale(-1) G)` = `−S⁻¹·(XᴴX)`, the multi-RHS `k×k` solve.
  - **Found**: `:533` `SS = -S.fullPivLu().solve(SS);`. citecheck `--anchor 'SS =
    -S.fullPivLu().solve(SS)'` → anchor at **533**, zero drift. This is the `lu_solve` multi-RHS
    column-wise form (`lu_solve.md:58`, independently verified).
  - **Verdict**: **supports**.

- **Citation**: `palace/linalg/nleps.cpp:534` (Stage 3 single-RHS solve).
  - **Theme claim**: `c' = lu_solve(SS, c)` = `SS⁻¹·c`.
  - **Found**: `:534` `x2 = SS.fullPivLu().solve(x2);`. citecheck anchor → line **534**, zero drift.
  - **Verdict**: **supports**.

- **Citation**: `palace/linalg/nleps.cpp:535` (Stage 3+4 fused).
  - **Theme claim**: `XSx2 = MatVecMult(X, S.fullPivLu().solve(x2))` = `X·(S⁻¹·c')`; the source
    fuses Stage 3's final `S⁻¹·` with Stage 4's `X·`.
  - **Found**: `:535` `const ComplexVector XSx2 = MatVecMult(X, S.fullPivLu().solve(x2));`.
    citecheck `--anchor 'XSx2 = MatVecMult'` → line **535**, zero drift. The fusion claim
    (inner `S.fullPivLu().solve(x2)` is Stage 3's `y`, wrapped by `MatVecMult` = Stage 4's `X·`) is
    correct: the L2 un-fuse into `lu_solve ▷ linear_combination` is faithful.
  - **Verdict**: **supports**.

- **Citation**: `palace/linalg/nleps.cpp:536` (Stage 5 subtraction).
  - **Theme claim**: `linalg::AXPY(-1.0, XSx2, x1)` = `x1 ← x1 − X·(…)`, in place on `x1`.
  - **Found**: `:536` `linalg::AXPY(-1.0, XSx2, x1);`. citecheck anchor → line **536**, zero drift.
    The in-place-destination claim (`x1` is both input `v` and output) holds — `x1` is the lambda's
    `ComplexVector &x1` out-param.
  - **Verdict**: **supports**.

- **Citation**: `palace/linalg/nleps.cpp:329-347` (MatVecMult back-projection primitive).
  - **Theme claim**: `MatVecMult(const std::vector<ComplexVector>&X, const Eigen::VectorXcd&y)` at
    `:329`; the `z = 0; for j: AXPBYPCZ(…)` fold with the complex real/imag split; closing `}` at `:347`.
  - **Found**: `:329` `ComplexVector MatVecMult(const std::vector<ComplexVector> &X, const
    Eigen::VectorXcd &y)`; body has `z = 0.0;` then a `for (int j...)` loop with two
    `linalg::AXPBYPCZ(...)` calls (real/imag split); `:347` `}`. citecheck `--anchor 'ComplexVector
    MatVecMult'` → line **329**, zero drift.
  - **Verdict**: **supports**. The `linear_combination` = length-`k` `MatVecMult` identification is exact.

- **Citation**: `palace/linalg/nleps.cpp:354-362` (literature anchors for the constructive sub-part).
  - **Theme claim**: Jarlebring–Koskela–Mele 2018 (`:354`), SLEPc-NEP minimality index 1 (`:356`),
    Effenberger 2013 (`:357`).
  - **Found**: `:354` `// Reference: Jarlebring, Koskela, Mele, Disguised and new quasi-Newton
    methods for`; `:356` `// Using the deflation scheme used by SLEPc's NEP solver with minimality
    index set to 1.`; `:357` `// Reference: Effenberger, Robust successive computation of eigenpairs
    for`. Exact.
  - **Verdict**: **supports**. The literature anchor for the Galerkin-core constructive fan-down is
    real and correctly cited.

- **Citation**: `palace/linalg/nleps.cpp:606-619` (deflation-basis growth; non-orthonormal precondition).
  - **Theme claim**: `X.resize(k+1)` at `:614`, `X[k] = v` at `:615`, `k++` at `:619`; confirms `X`
    is the raw normalized-eigenvector basis (NOT orthonormalized).
  - **Found**: `:614` `X.resize(k + 1);`, `:615` `X[k] = v;`, `:619` `k++;`. citecheck `--anchor
    'X.resize(k + 1)'` → line **614**, zero drift. Crucially, `:611` `v *= 1.0 / scale;` (Norml2
    normalization) is the ONLY conditioning applied — there is **no Gram-Schmidt /
    orthonormalization** step before `X[k] = v`. Confirms the oblique-projector precondition (`X`
    full-rank but non-orthonormal).
  - **Verdict**: **supports**. This is the load-bearing evidence that Stage 3's `lu_solve` is NOT
    erasable (the over-unification guard against collapsing to `orthogonalize`).

- **Citation**: `palace/linalg/nleps.cpp:562-563` (residual-site reuse of back-projection).
  - **Theme claim**: `S = lam·I − H` at `:562`, `XSvv2 = MatVecMult(X, S.fullPivLu().solve(vv2))` at `:563`.
  - **Found**: `:562` `const Eigen::MatrixXcd S = lam * Eigen::MatrixXcd::Identity(k, k) - H;`;
    `:563` `const ComplexVector XSvv2 = MatVecMult(X, S.fullPivLu().solve(vv2));`. Exact.
  - **Verdict**: **supports**. Stages 3+4 reused on the residual — consumer relationship correctly
    characterized; still Schur-wrapped (`S = lam·I − H`), again NOT a bare Gram.

- **Citation**: `palace/linalg/nleps.cpp:664-667` (Jacobian deflation terms).
  - **Theme claim**: `S = eig·I − H` (`:664`), `Sv2 = S.fullPivLu().solve(v2)` (`:665`),
    `XSv2 = MatVecMult(X, Sv2)` (`:666`), `XSSv2 = MatVecMult(X, S.fullPivLu().solve(Sv2))` (`:667`).
  - **Found**: `:664` `const Eigen::MatrixXcd S = eig * Eigen::MatrixXcd::Identity(k, k) - H;`;
    `:665` `const Eigen::VectorXcd Sv2 = S.fullPivLu().solve(v2);`; `:666` `const ComplexVector XSv2
    = MatVecMult(X, Sv2);`; `:667` `const ComplexVector XSSv2 = MatVecMult(X,
    S.fullPivLu().solve(Sv2));`. Exact.
  - **Verdict**: **supports**. Stages 3+4 reused with carried coordinates (no fresh Stage-1 `dot`);
    again Schur-wrapped, never bare Gram.

### Constructive Galerkin-core sub-part — the bare-Gram solve

- **Citation**: `palace/linalg/nleps.cpp:186` (theme: empty-basis law) — *not asserted by this
  theme's anchors; deferred to deflate.md L2 law set.* (No drift to flag.)
- **Citation (negative anchor)**: `book/src/L2/deflate.md:343-348` AND `:386-391`.
  - **Theme claim**: no bare-Gram `(XᴴX)⁻¹` deflation solve appears anywhere in Palace;
    `search_text` for a Gram-only deflation projection across `palace/linalg/*.cpp` returns only the
    Schur-wrapped `nleps.cpp` block.
  - **Found**: `deflate.md:343-345` states "not positively exhibited anywhere in Palace
    (`search_text` ... returns hits only inside the Schur-wrapped `nleps.cpp` block)"; `:387-389`
    repeats the negative anchor in the Status section ("no bare-Gram `(XᴴX)⁻¹` deflation solve
    appears anywhere in Palace"). Both ranges are valid, consistent pointers to the same negative
    anchor — no internal contradiction, no drift.
  - **Verdict**: **supports** (negative anchor is faithfully inherited AND independently
    re-confirmed — see "Gate verdict" below).

### Inherited book-internal cross-references (leaf vocabulary)

- **`book/src/L2/deflate.md:362-415`** (inherited Status). Found `partly-constructive` Status with
  matching firm-part / constructive-sub-part / promotion-condition tri-structure. **supports.**
- **`book/src/L2/deflate.md:55-66`** (LHS signature) / **`:248-276`** (over-unification guard). In
  bounds; the over-unification guard (`deflate` vs `orthogonalize`, distinguisher = the `lu_solve`)
  is the one this theme carries into Stage 3. **supports.**
- **`book/src/L1/dot.md:43`** — found "conjugate-linear in the **first** argument ... `⟨x, y⟩ = xᴴ
  y` ... the L1 signature names the conjugated argument first". Exactly the convention the theme
  pins at Stage 1. **supports.**
- **`book/src/L1/lu_solve.md:45`** (invertibility precondition), **`:58`** (multi-RHS column-wise,
  law 4 witnessed at `nleps.cpp:533`), **`:59`** (solve-composition, nested `lu_solve(S,
  lu_solve(SS, ·))` at `:533-534`). All read and confirmed. **supports.** Note `lu_solve.md:45`
  independently names `Ar` as "a ROM matrix" — corroborating my ROM-is-not-a-Gram finding.
- **`book/src/L2/gram.md`, `book/src/L2/linear_combination.md`** — cited as firm leaves consumed
  whole (gram fan-down deferred to `gram-fold-specialization`; `linear_combination` =
  `MatVecMult`). In-scope, consumed-whole; not re-derived here (correct per one-theme-per-dispatch).
  **supports.**

## Applicability conditions

- **Condition**: `X` full column rank (so `XᴴX` / `S` / `SS` invertible).
  - **Verifiable**: yes, structurally — `X` is the converged invariant-pair basis grown one distinct
    eigenvector at a time (`nleps.cpp:614-615`); full-rank by construction.
  - **Found counter-example?**: no.

- **Condition**: `X` NOT assumed orthonormal (raw normalized-eigenvector basis).
  - **Verifiable**: yes, and **directly confirmed** at `nleps.cpp:609-615` — the only conditioning
    before `X[k] = v` is the L2-norm normalization `v *= 1.0/scale` (`:610-611`); there is **no
    orthonormalization** step. This is exactly why Stage 3's `lu_solve` is load-bearing (oblique, not
    orthogonal projector). The over-unification guard is well-founded.
  - **Found counter-example?**: no.

- **Condition**: `op.block = Schur` for the firm fan-down; `op.block = Galerkin` invokes the
  constructive single-solve.
  - **Verifiable**: yes — Palace exclusively exhibits the Schur form (`S = λI − H` everywhere:
    `:532`, `:562`, `:664`). The Galerkin single-solve is the unwitnessed `S = I` case.
  - **Found counter-example?**: no (this IS the gate; see below).

- **Condition**: element type complex at the Palace site; conjugation lives in `dot`.
  - **Verifiable**: yes — `Eigen::MatrixXcd` / `ComplexVector` throughout; `MatVecMult` (`:340-345`)
    has the explicit real/imag `AXPBYPCZ` split. The real case is absorbed by the leaves.
  - **Found counter-example?**: no.

## Algebraic laws (cited)

The theme cites laws as inherited leaf-vocabulary properties (it is a fan-down theme, not a
law-authoring entry); each holds on the operator signatures as cited:

- **Law**: `lu_solve` multi-RHS = column-wise single-RHS (`lu_solve.md:58`, law 4).
  - **Holds on operators?**: yes — witnessed by `SS = -S.fullPivLu().solve(SS)` (`:533`, a `k×k`
    RHS-matrix solve) alongside the single-RHS `x2 = SS.fullPivLu().solve(x2)` (`:534`). The theme's
    Stage-3 "multi-RHS `k×k`" label on `:533` is correct.

- **Law**: `lu_solve` solve-composition (nested solves), `lu_solve.md:59`, law 5.
  - **Holds on operators?**: yes as the *recorded compositional shape* — the nested `lu_solve(S,
    lu_solve(SS, ·))` form at `:533-534` is exactly law 5's witnessed pattern; the theme correctly
    cites it as the witnessed form, not as a coefficient-merging identity.

- **Law**: the Galerkin-core `S = I` reduction (`SS = −I⁻¹·G = −G`, `SS⁻¹·c = −G⁻¹·c`, `S⁻¹·(·) =
  (·)`, composing to `−(−G⁻¹·c) = G⁻¹·c`).
  - **Holds on operators?**: yes — the algebra is correct: with `S = I`, the Schur triple-solve
    `S⁻¹·SS⁻¹·c` with `SS = −S⁻¹G = −G` gives `I·(−G)⁻¹·c = −G⁻¹·c`, and the theme also folds in the
    leading `−1` from the `SS = −S.fullPivLu().solve(SS)` sign so the net coordinate solve reduces to
    `G⁻¹·c = (XᴴX)⁻¹·(Xᴴv)`. The reduction is sound; it is **constructive** only in that no positive
    site exercises `S = I` — the *algebra* is firm, the *positive-source-witness* is what is absent.

- **Law (conjugation)**: deflation coordinate is `X[j]ᴴ v` (basis vector conjugated), matching
  `book/src/L1/dot.md:43`.
  - **Holds on operators?**: yes — `linalg::Dot(comm, a, b) = bᴴ a` conjugates arg-2 (`X[j]`), which
    re-orders to the L1 `dot`'s arg-1-conjugated `dot(X[j], v)`. Gram entry `G(i,j) = X[i]ᴴ X[j]`
    (`:529`) is consistent.

## Gate verdict: STAYS-GATED-correctly (NLEPS-scoped is the realized outcome)

The shared bare-Galerkin-core promotion gate **stays gated correctly.** I ran an **exhaustive**
codemap search for any positive bare-Gram `(XᴴX)⁻¹` Galerkin-core deflation-coordinate solve — every
dense factor/solve idiom in the Palace `*.cpp` tree:

| Search | Hits | Bare-Gram solve? |
|---|---|---|
| `fullPivLu` (`*.cpp`) | `nleps.cpp:533,534,535,563,665,667` | No — all solve against `S = λI − H` or `SS = −S⁻¹(XᴴX)` (Schur-wrapped) |
| `.solve(` (`*.cpp`) | the 6 `nleps.cpp` sites + `romoperator.cpp:757,758,765` | No (see ROM below) |
| `.inverse()` (`*.cpp`) | `geodata_impl.cpp:555` (3×3 bounding-ball geometry) | No |
| `gram`/`XHX`/`VHV`/`GtG`/`VtV` (`*.cpp`) | only unrelated comments (dof-diagram, parallelogram-area) | No |
| `.llt`/`.ldlt`/`.lu`/`partialPivLu`/`colPivHouseholderQr` (`*.cpp`) | `romoperator.cpp:757,758` | No (see ROM below) |

**The one near-candidate — `romoperator.cpp:757-765` — is NOT a bare-Gram solve.** The theme's
own promotion condition names "a ROM Galerkin projection using the Gram inverse" as a possible
unblock site, so I checked it carefully:

- `:765` `RHSr = Ar.fullPivHouseholderQr().solve(RHSr);` (active path; `:757-758` LDLT path is
  dead under `if constexpr (false)`).
- `Ar` is the **ROM-projected system operator**, not a Gram matrix. `romoperator.cpp:74` comments
  `Ar = Vᴴ A V`, and `:729-734` build it as `Ar += Kr; Ar += iω·Cr; Ar += −ω²·Mr` — i.e. `Ar =
  Vᴴ(K + iωC − ω²M)V`, the reduced **operator pencil**. The solve `Ar⁻¹·RHSr` is the reduced
  *linear-system* solve at a frequency, NOT a deflation-coordinate Gram `(XᴴX)⁻¹·(Xᴴv)` solve.
- This is independently corroborated by the firm L1 `lu_solve.md:45`, which already classifies `Ar`
  as "a ROM matrix `Ar` that is expected invertible at the evaluation point ... `Ar(ω)` is the
  regular reduced system" — a system matrix, not a Gram.

**Conclusion: the negative anchor is correct AND complete.** No unwrapped Galerkin-core
`(XᴴX)⁻¹` deflation solve exists anywhere in Palace. The constructive sub-part is therefore a
**faithful `S = I` reduction** of the positively-sourced Schur fan-down, materialized from
literature + this (now re-confirmed) negative anchor. The promotion condition is **well-formed**
(it names concrete future unblock-site shapes: linear-EVP deflation, preconditioner deflation, ROM
Galerkin-with-Gram-inverse) and is correctly **NOT closed** here. The "NLEPS-scoped is acceptable"
verdict is the realized outcome: the bare-Gram core genuinely never appears unwrapped in Palace.

**I do NOT UNBLOCK the gate** (no positive site found) and **do NOT ENACT any promotion** (out of
role even if I had). The theme's `partly-constructive` status is **correctly held**, and so is the
shared gate across all three references (`deflate` L2, `nleps-deflated-solve-mutation-rotation`
L1>L0, this L2>L1). I propose only the additive `verified_against:` audit block below.

## Proposed changes

The audit is fully-supporting and adds no contradictions. The only proposed change is the additive
per-theme `verified_against:` metadata block (consumed by `cross-layer-cross-cutter` for coverage
analysis). **The `## Status` line is left UNCHANGED** (`partly-constructive` correctly held). No
firming edits are proposed because the gate did not unblock.

```edit:book/src/L2-L1/deflate-composition-lowering.md
[append at end of file]
```yaml
verified_against:
  - citation: palace/linalg/nleps.cpp:505-537
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: firm Schur-form fan-down; every Stage 0-5 anchor zero-drift (citecheck --anchor)
  - citation: palace/linalg/nleps.cpp:508-513
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: source block-elimination comment; :512 Schur complement, :513 back-projection
  - citation: palace/linalg/nleps.cpp:515-518
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Stage 0 k==0 short-circuit
  - citation: palace/linalg/nleps.cpp:519-523
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Stage 1 dot-fold; decisive :522 zero-drift
  - citation: palace/linalg/nleps.cpp:524-531
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Stage 2 Gram build; :524 materialization, :529 assignment zero-drift; SS buffer-aliasing confirmed
  - citation: palace/linalg/nleps.cpp:532
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Stage 3 Schur block S = eig_opInv*I - H
  - citation: palace/linalg/nleps.cpp:533
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Stage 3 multi-RHS solve SS = -S^-1(XHX) (lu_solve law 4)
  - citation: palace/linalg/nleps.cpp:534
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Stage 3 single-RHS solve c' = SS^-1 c
  - citation: palace/linalg/nleps.cpp:535
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Stage 3+4 fused MatVecMult(X, S^-1 c'); L2 un-fuse faithful
  - citation: palace/linalg/nleps.cpp:536
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Stage 5 in-place AXPY(-1, XSx2, x1)
  - citation: palace/linalg/nleps.cpp:329-347
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: MatVecMult back-projection primitive (:329 sig, :347 close)
  - citation: palace/linalg/nleps.cpp:354-362
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: literature anchors (Jarlebring-Koskela-Mele 2018 :354, SLEPc-NEP minimality :356, Effenberger 2013 :357)
  - citation: palace/linalg/nleps.cpp:606-619
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: non-orthonormal precondition; only Norml2-normalization at :610-611, no orthonormalization
  - citation: palace/linalg/nleps.cpp:562-563
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: residual-site reuse of Stages 3+4 (still Schur-wrapped)
  - citation: palace/linalg/nleps.cpp:664-667
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: Jacobian reuse of Stages 3+4 with carried coordinates (still Schur-wrapped)
  - citation: book/src/L2/deflate.md:343-348
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: negative anchor (no bare-Gram solve in Palace) re-confirmed complete by exhaustive *.cpp dense-solve search
  - citation: book/src/L1/dot.md:43
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: arg-1-conjugated dot convention pinned at Stage 1
  - citation: book/src/L1/lu_solve.md:58
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: multi-RHS column-wise law 4 (witnessed :533)
  - citation: book/src/L1/lu_solve.md:59
    verdict: supports
    audited_at: 2026-05-29T15:19:15Z
    note: solve-composition law 5 (witnessed nested :533-534)
gate_verdict:
  shared_gate: bare-Galerkin-core-positive-source-site
  status: stays-gated-correctly
  audited_at: 2026-05-29T15:19:15Z
  finding: >-
    Exhaustive codemap search of every dense .solve()/.inverse()/LU/LDLT/QR/Cholesky
    site in palace/*.cpp found NO unwrapped bare-Gram (XHX)^-1 deflation solve. The
    one near-candidate romoperator.cpp:757-765 solves against Ar = V^H A V (ROM-projected
    system operator pencil, per romoperator.cpp:74 + :729-734), NOT a Gram matrix.
    Negative anchor correct AND complete; NLEPS-scoped is acceptable; partly-constructive
    correctly held across all 3 shared references.
```
```

(The outer ```` ```edit ```` block wraps the appended content; the inner fenced ` ```yaml ` block is
the literal text to append to the theme file. The `## Status` line and all body sections are left
unchanged — this is an additive metadata-only proposal.)

## Supporting evidence

Files consulted (all via codemap `read_range` / `search_text` and `tools/citecheck`; paths relative
to `reference/` for Palace, repo-root for book):

- `palace/linalg/nleps.cpp` — `read_range` on `:329-347`, `:354-362`, `:505-537`, `:560-564`,
  `:606-619`, `:662-668`; `search_text` `fullPivLu`, `\.solve\(` (the negative-anchor confirmation).
- `palace/models/romoperator.cpp` — `read_range :740-770`; `search_text 'Ar\s*[=+]'` (the
  ROM-`Ar`-is-not-a-Gram determination; `:74` `Ar = VᴴAV`, `:729-734` build, `:757-765` solve).
- `palace/utils/geodata_impl.cpp:555` — the only `.inverse()` site (3×3 geometry; ruled out).
- `tools/citecheck/citecheck.py` — bounds-checked 7 primary + 8 book-internal ranges (15 OK, 0
  failing); `--anchor` drift-checked the 9 decisive pinpoint lines (`:522, :529, :532, :533, :534,
  :535, :536, :329, :614`) — all zero-drift.
- `book/src/L2/deflate.md` — `:340-394` (Status + variant axes + negative anchor) read directly.
- `book/src/L1/dot.md:40-47`, `book/src/L1/lu_solve.md:43-62` — read directly (leaf vocabulary).

## Open questions / caveats

- **OQ (carry-forward, unchanged):** `deflate-composition-lowering-mutation-rotation-lowering-verifier-audit-followup`.
  This audit DISCHARGES the audit half of that OQ for the L2>L1 theme: the firm Schur fan-down is
  per-line verified zero-drift, and the gate is confirmed STAYS-GATED-correctly with the negative
  anchor re-confirmed complete. The OQ should be **re-scoped to a pure promotion-watch**: it now
  tracks only the future appearance of a positive bare-Gram-solve site (linear-EVP deflation /
  preconditioner deflation / ROM Galerkin-with-Gram-inverse). When such a site is dissected, a
  lowering-verifier UNBLOCK + follow-up ENACT promotes all three shared references together. No
  audit work remains on the *current* Palace source for this theme.

- **Caveat (no drift to flag, recorded for transparency):** the theme cites the negative anchor at
  TWO `deflate.md` ranges — `:343-348` (variant-axes section) and `:386-391` (Status section). I
  read both; they are consistent, non-contradictory pointers to the same negative anchor (the
  variant-axes copy at `:340-348`, the Status copy at `:387-389`). No reconciliation needed — this
  is intentional redundancy across two sections of the same source entry, not a citation conflict.

- **Caveat (scope boundary, not this dispatch):** the theme's promotion condition notes a possible
  `same-layer-cross-cutter` call to scope `deflate` to "the NLEPS Schur form only", which would
  make this theme `firm` on positive structure with the Galerkin-core demoted to a literature note.
  That is an alternative resolution of the gate (NOT a promotion via a positive site). It is
  explicitly out of this dispatch's scope and out of lowering-verifier authority — I neither make
  that call nor recommend for/against it; I record only that the audit found the NLEPS-scoped
  reading is evidentially sound (no bare-Gram core exists, so a Schur-only scoping would lose no
  positive Palace content).

- **Caveat (consumed-whole leaf):** the Stage 2 `gram` fan-down (the `k²` `dot` double-loop /
  Hermitian-symmetry trick) is deferred to the parallel-cycle `gram-fold-specialization` theme and
  NOT audited here (correct per one-theme-per-dispatch). I confirmed only that `nleps.cpp:524-531`
  is the Gram build the leaf stands for; the leaf's own internal fan-down is that theme's audit.
