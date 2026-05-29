---
agent: cross-layer-cross-cutter
invoked_at: 2026-05-29T034441Z
scope: L2↔L1 / L1↔L0 cross-cut — caller-site classification of every Palace linalg::Dot site (conjugate-pair re-order risk inventory)
status: integrated
integrated_at: 2026-05-29T06:05:00Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-020 finalize (staging row #8). CROSS-LAYER census evidence-backfill (additive, NOT a status change). Appended a conjugation_caller_inventory: fenced yaml block + a one-paragraph lead-in into §Applicability — Condition 5 of inner-product-fold-specialization.md (AFTER Condition 5 prose, BEFORE ## Justification kind, ~200 lines ABOVE the #7 verified_against EOF block — non-overlapping, EOF block untouched). Headline: Dot conjugation load-bearing in exactly ONE algorithm (SLEPc-NEP nleps.cpp, 4 observable sites); palace/fem ZERO Dot callers; 11 invisible + 4 observable = 15 caller sites. Resolves OQ inner-product-conjugate-pair-reorder-caller-classification (:152; meta-phase migrates/closes). Two NEW follow-ups opened: nleps-deflation-subspace-projection-combinator-deflate-gram (combinator-miner) + orthog-hpp-localdot-globalsum-unweighted-inner-product-surface (coverage gap). Theme stays firm. retroactive-budget 0; clean build."
inputs:
  - reports/2026-05-29T034441Z-lowering-verifier-inner-product-fold/CYCLE.md (wave-1 confirmed per-line rules)
  - palace/linalg/iterative.cpp:395,404,444,460 (CG / PCG coefficients)
  - palace/linalg/operator.cpp:603,615 (Norml2 SPD-realness consumers) + 621-638 (weighted-Dot defs, :628/:637 internal passthrough)
  - palace/linalg/nleps.cpp:487,492,522,529,543,568,575,675(×2),696,737 (SLEPc-NEP quasi-Newton)
  - palace/linalg/vector.hpp:243-259 (LocalDot/Dot/Norml2 decls), vector.cpp:263-274,664-685 (kernels — definitions, not callers)
  - palace/linalg/orthog.hpp:35 (LocalDot caller — NOT a Dot caller; noted out-of-band)
  - book/src/L2-L1/inner-product-fold-specialization.md, book/src/L1/dot.md, book/src/L1/bilinear-form.md
---

# CYCLE: Cross-layer observation — Palace linalg::Dot caller-site conjugation-risk inventory

## Summary

The cycle-020 wave-1 lowering-verifier confirmed that Palace's `linalg::Dot(comm, x, y)`
computes `x·conj(y) = yᴴ x` (arg-2 conjugated) whereas the L1/L2 `inner_product`/`dot`
vocabulary pins `xᴴ y` (arg-1 conjugated), the two being complex conjugates of each other.
It cited five witnesses (four invisible, one observable). This report **completes the
caller-site census**: I scanned EVERY `Dot` / `linalg::Dot` / `.Dot(` call site across
`palace/linalg/` and `palace/fem/`, `read_range`-verified each consumption, and classified
each as **invisible** (result real-projected — the `yᴴ x` vs `xᴴ y` choice is unobservable)
or **observable** (full complex value, including the imaginary part / Hermitian-transpose
structure, is consumed downstream so the conjugation convention is load-bearing).

**Headline finding: `palace/fem/` has ZERO `Dot` callers** (the scope's other half is empty).
**Within `palace/linalg/`, 11 of the 15 caller sites are invisible** (CG SPD coefficients,
B-weighted SPD norms, `std::abs(·)` self-norms) **and 4 are observable** — all four in
`nleps.cpp`'s SLEPc-NEP deflated quasi-Newton: the deflation projection `:522`, the Gram
matrix `:529`, the residual deflation-coords `:568`, and the complex Newton eigenvalue-step
ratio `:675` (two sites). **The wave-1 census missed all four** because it sampled
`nleps.cpp` only at the two `std::abs(·)` norm lines `:487,:492` (both invisible). The
genuine intra-`linalg/` conjugation risk lives entirely in the SLEPc-NEP deflation algebra,
not in the iterative solvers or the norms. This is the risk inventory the dot/inner_product
lowering themes' applicability conditions should cite by line.

## Observation kind

**Coverage gap** (in the lowering themes' applicability evidence) — the
`inner-product-fold-specialization` theme's Condition 5 ("re-order observable for
full-complex-value uses") is structurally complete and its sole `linalg/`-internal observable
witness is correctly identified as a *weighted* `Dot` (`boundarymodeoperator.cpp:90`, out of
my scope but cited by wave-1). But the theme's evidence set does **not** name the four
**unweighted** `linalg::Dot` observable sites inside `palace/linalg/nleps.cpp`. These are the
in-scope, intra-`linalg/` instances where the bare two-argument `Dot` convention is
load-bearing — exactly the sites a future `dot-mutation-rotation` (L1>L0) lowering or the
`inner-product-fold-specialization` (L2>L1) theme must point at to make Condition 5 concrete
for the unweighted `dot` leaf (the wave-1 observable witness is the *weighted* `bilinear_form`
leaf). The classification below closes that evidence gap.

## Caller-site classification table

Convention recap (wave-1 verified): `linalg::Dot(comm, a, b) = a·conj(b) = bᴴ a`. So
`Dot(comm, x, X[j]) = X[j]ᴴ x`. The L1/L2 fold pins `xᴴ y`; recovering it from Palace
requires either operand-swap (`Dot(comm, y, x)`) or outer-conjugation. The conjugation is
**invisible** when the result is real-projected (`.real()`, `std::abs`, an SPD/Hermitian
diagonal, or a ratio of two same-convention dots where the conjugation cancels), and
**observable** otherwise.

| Site (rel. to `reference/`) | call | classification | consumption evidence |
|---|---|---|---|
| `palace/linalg/iterative.cpp:395` | `beta = Dot(comm, z, r)` (`z=Br`, PCG `(Br,r)`) | **invisible** | `:396` `CheckDot(beta, ...)` (asserts SPD-real); `:397` `res = sqrt(abs(beta))`; later `beta/beta_prev`, `beta/denom` — ratio of same-convention dots cancels conjugation. SPD `B` ⟹ real. |
| `palace/linalg/iterative.cpp:404` | `beta_rhs = Dot(comm, p, b)` (`p=Bb`, `(Bb,b)`) | **invisible** | `:410` `CheckDot(beta_rhs, ...)`; `:411` `initial_res = sqrt(abs(beta_rhs))`. SPD `B`. |
| `palace/linalg/iterative.cpp:444` | `denom = Dot(comm, z, p)` (`z=Ap`, `(Ap,p)`) | **invisible** | `:445` `CheckDot(denom, ...)` (asserts SPD-real); `:446` `alpha = beta/denom`. SPD `A`. |
| `palace/linalg/iterative.cpp:460` | `beta = Dot(comm, z, r)` (in-loop `(Br,r)`) | **invisible** | `:461` `CheckDot(beta, ...)`; `:462` `res = sqrt(abs(beta))`. Same as `:395`. |
| `palace/linalg/operator.cpp:603` | `double dot = Dot(comm, Bx, x)` (real `Norml2`) | **invisible** | `:604` `MFEM_ASSERT(dot > 0.0, ...)`; `:605` `return sqrt(dot)`. Real element type — no conjugation exists. |
| `palace/linalg/operator.cpp:615` | `complex<double> dot = Dot(comm, Bx, x)` (cplx `Norml2`) | **invisible** | `:616` asserts `dot.real()>0 && abs(dot.imag()) < 1e-9*dot.real()` (SPD `B` ⟹ imag≈0); `:617` `return sqrt(dot.real())` — only `.real()` consumed. Comment `:612` "For SPD B, xᴴ B x is real." |
| `palace/linalg/operator.cpp:628` | `return Dot(comm, Ax, y)` (real-`Operator` weighted-`Dot` body) | **definition-internal** | Not an independent caller — the convention passes through to whoever calls the weighted `Dot(comm,x,A,y)`. Observability is decided at THAT caller (e.g. `boundarymodeoperator.cpp:85` invisible / `:90` observable). |
| `palace/linalg/operator.cpp:637` | `return Dot(comm, Ax, y)` (`ComplexOperator` weighted-`Dot` body) | **definition-internal** | Same passthrough as `:628`. |
| `palace/linalg/nleps.cpp:487` | `norm_c = sqrt(abs(Dot(c,c)) + c2.squaredNorm())` | **invisible** | `std::abs(·)` magnitude (self-dot); `:488` `c *= 1/norm_c`. Wave-1 witness. |
| `palace/linalg/nleps.cpp:492` | `norm_v = sqrt(abs(Dot(v,v)) + ...)` | **invisible** | `std::abs(·)` self-norm; `:493` `v *= 1/norm_v`. Wave-1 witness. |
| `palace/linalg/nleps.cpp:522` | `x2(j) = b2(j) - Dot(GetComm(), x1, X[j])` (`=X[j]ᴴ x1`) | **OBSERVABLE** | `x2` is the deflation block-coord vector; `:533` `x2 = SS.fullPivLu().solve(x2)` (complex LU solve), then `:534` `XSx2 = MatVecMult(X, S·solve(x2))` and `:535` `AXPY(-1.0, XSx2, x1)` into `x1`. Full complex value, no real-projection. Comment `:513-517` `x1 = x1 - X S x2`. |
| `palace/linalg/nleps.cpp:529` | `SS(i,j) = Dot(GetComm(), X[i], X[j])` (`=X[j]ᴴ X[i]`) | **OBSERVABLE** | Deflation Gram matrix; `:532-533` `SS = -S.solve(SS); x2 = SS.solve(x2)` — full complex matrix into LU solves. Comment `:516` `SS = (B - A T^-1 U) = - X^* X S^-1`. Off-diagonal entries complex; convention fixes `SS(i,j)=X[j]ᴴX[i]` vs the transpose. |
| `palace/linalg/nleps.cpp:543` | `norm_w0 = sqrt(abs(Dot(w0,w0)) + ...)` | **invisible** | `std::abs(·)` self-norm; `:544` `w0 *= 1/norm_w0`. |
| `palace/linalg/nleps.cpp:568` | `rr2(j) = Dot(GetComm(), vv, X[j])` (`=X[j]ᴴ vv`) | **OBSERVABLE** | `rr2` (= `X^* vv`, comment `:561`) is an out-param; at the `:587` call `compute_residual(eig,v,v2,u,u2,A2n)` it binds to `u2`, which at `:674` feeds `u2_w0 = w2.adjoint()*u2` and then the `:675` complex Newton numerator. (It is ALSO consumed via `.squaredNorm()` at `:575`, which alone would be invisible — but the out-param escape into `:674-675` makes the full complex value load-bearing.) |
| `palace/linalg/nleps.cpp:675` (numerator) | `Dot(GetComm(), u, w0)` (`=w0ᴴ u`) | **OBSERVABLE** | `:673-675` `delta_eig = -(Dot(u,w0) + u2_w0) / Dot(w,w0)` — complex eigenvalue Newton correction; `:676` `z.AXPBYPCZ(-delta_eig, w, ...)` and `:685` `eig_trial = eig + alpha*delta_eig` (with `eig.imag()` load-bearing throughout). No real-projection. |
| `palace/linalg/nleps.cpp:675` (denominator) | `Dot(GetComm(), w, w0)` (`=w0ᴴ w`) | **OBSERVABLE** | Same `delta_eig` ratio; full complex denominator. Two distinct `Dot` calls on one source line. |
| `palace/linalg/nleps.cpp:696` | `norm_v_trial = sqrt(abs(Dot(v_trial,v_trial)) + ...)` | **invisible** | `std::abs(·)` self-norm; `:697-698` `v_trial *= 1/norm_v_trial`. |
| `palace/linalg/nleps.cpp:737` | `norm_w0 = sqrt(abs(Dot(w0,w0)) + ...)` (lagged-precond recompute) | **invisible** | `std::abs(·)` self-norm; `:738` `w0 *= 1/norm_w0`. |

**Out-of-scope but adjacent (cited for completeness, NOT in `linalg/`/`fem/`):**

| Site | classification | note |
|---|---|---|
| `palace/models/boundarymodeoperator.cpp:85` | invisible | Wave-1 witness (Poynting diagonal, Hermitian `Bttr`, `y=x`). Weighted `Dot`. |
| `palace/models/boundarymodeoperator.cpp:90` | **observable** | Wave-1 witness (`ComplexWrapperOperator Atn` non-Hermitian off-diagonal). The only WEIGHTED observable site; complements the four UNWEIGHTED ones found here. |
| `palace/models/postoperator.cpp:1759,1760,1795,1796` | **observable** | `V.real(Dot(...)); V.imag(Dot(...))` — port voltage/current; real AND imag parts separately consumed. Outside scope (`models/`) but materially observable; flag for a `models/`-scoped follow-up. |

**Definitions / decls / non-`Dot` (excluded from the caller census, for the record):**
`vector.hpp:111-113,243-244,248-259` (decls + `Dot` template + `Norml2`), `vector.cpp:263-274`
(`ComplexVector::Dot`/`TransposeDot` member defs), `vector.cpp:664-685` (`LocalDot` defs),
`iterative.cpp:22,28` (`CheckDot` helper), `operator.cpp:621,631` + `operator.hpp:388,393`
(weighted-`Dot` decl/def signatures), `orthog.hpp:35` (`return LocalDot(x, y)` — a `LocalDot`
caller, NOT a `Dot` caller; the Gram-Schmidt inner products route through `LocalDot`+`GlobalSum`
in `orthog.hpp` rather than `linalg::Dot`, so they are out of THIS census but are a sibling
conjugation surface — see Open questions).

## Risk-inventory observation

1. **`palace/fem/` is empty of `Dot` callers.** The conjugation risk does not touch the FE
   assembly layer at all (FE-space inner products go through MFEM bilinear forms / libCEED, not
   `linalg::Dot`). Half the declared scope contributes zero sites; the entire risk surface is in
   `palace/linalg/` (+ the `models/` adjacencies).

2. **The iterative solvers and all norms are conjugation-safe.** Every `iterative.cpp` site
   (4) and every `std::abs(·)`/`.real()` norm site (`operator.cpp:603,615`; `nleps.cpp:487,492,
   543,696,737` — 7) is invisible. CG's coefficients are SPD-real-asserted by `CheckDot`; the
   B-weighted `Norml2` asserts `xᴴBx` real for SPD `B`; the self-norms take magnitudes. **11 of
   the 15 in-scope caller sites** are invisible by real-projection (the other 4 observable; the 2
   `operator.cpp:628,:637` rows are definition-internal passthroughs, not independent callers, and
   the `:575` `squaredNorm` consumer of `:568`'s out-param has no caller row of its own). This is
   strong evidence that a future
   `dot-mutation-rotation` lowering can lower these arms with the conjugation convention left
   *unspecified* (a "convention-blind" applicability sub-condition).

3. **The conjugation convention is load-bearing in exactly one algorithm: SLEPc-NEP deflated
   quasi-Newton (`nleps.cpp`).** All four observable in-scope sites are there:
   - **`:522`** deflation projection coords `X[j]ᴴ x1` → complex LU solve.
   - **`:529`** deflation Gram matrix `X[j]ᴴ X[i]` → complex LU solve (off-diagonal entries
     are the convention-sensitive ones; a diagonal-only Gram would be invisible).
   - **`:568`** residual deflation coords `X[j]ᴴ vv` → escapes via out-param `u2` into the
     Newton numerator.
   - **`:675` (×2)** the complex eigenvalue Newton step `−(w0ᴴu + u2_w0)/(w0ᴴw)`.

   For all four, the L1/L2 `xᴴ y` convention must be reconciled with Palace's `yᴴ x` by
   **operand-swap or outer-conjugation** when lowering — the deferred-IEEE / convention-blind
   treatment that suffices for the norms is **not** sound here. A naive lowering that keeps the
   L1 arg-1-conj convention while emitting Palace's arg-order would compute the conjugate of the
   intended deflation coordinate / Gram entry / Newton ratio — silently transposing the deflation
   subspace algebra and conjugating the eigenvalue correction. This is precisely a "load-bearing
   numerical trick" in the CLAUDE.md sense (the conjugation is part of the algorithm, not a
   transparent rearrangement).

4. **The unweighted observable witnesses were absent from the wave-1 evidence set.** Wave-1's
   sole observable witness (`boundarymodeoperator.cpp:90`) is a *weighted* `Dot` exercising the
   `bilinear_form` leaf. The four `nleps.cpp` sites exercise the *bare* `dot` leaf
   (no operator argument). So the L1 `dot` leaf and the `inner-product-fold-specialization`
   §Condition-5 currently have **no cited unweighted observable site**; this report supplies them.

## Proposed changes

These are **proposals for the integrator / a follow-up lifter** — I do NOT touch `book/`.
The cleanest carrier is an `applicable_witnesses:`-style evidence note appended to the theme's
Condition 5 (or to the L1 `dot` leaf's conjugation-asymmetry reconciliation prose), recording
the unweighted observable inventory. Suggested append to
`book/src/L2-L1/inner-product-fold-specialization.md` (Condition 5 evidence block):

```edit:book/src/L2-L1/inner-product-fold-specialization.md
[append to §Applicability — Condition 5, or as a new "Caller-site conjugation inventory" note]
```yaml
conjugation_caller_inventory:
  audited_at: 2026-05-29T034441Z
  by: cross-layer-cross-cutter
  scope: every linalg::Dot caller across palace/linalg/ and palace/fem/
  invisible_unweighted:
    - palace/linalg/iterative.cpp:395   # PCG (Br,r), CheckDot SPD-real + abs
    - palace/linalg/iterative.cpp:404   # PCG (Bb,b)
    - palace/linalg/iterative.cpp:444   # PCG (Ap,p), CheckDot SPD-real
    - palace/linalg/iterative.cpp:460   # PCG in-loop (Br,r)
    - palace/linalg/nleps.cpp:487       # std::abs self-norm
    - palace/linalg/nleps.cpp:492       # std::abs self-norm
    - palace/linalg/nleps.cpp:543       # std::abs self-norm
    - palace/linalg/nleps.cpp:696       # std::abs self-norm
    - palace/linalg/nleps.cpp:737       # std::abs self-norm
  invisible_weighted:
    - palace/linalg/operator.cpp:603    # real Norml2 B-weighted, dot>0 assert
    - palace/linalg/operator.cpp:615    # complex Norml2 B-weighted, SPD imag~0 assert + .real()
  observable_unweighted:               # bare dot leaf — convention load-bearing
    - palace/linalg/nleps.cpp:522       # deflation proj X[j]ᴴ x1 -> complex LU solve
    - palace/linalg/nleps.cpp:529       # deflation Gram X[j]ᴴ X[i] -> complex LU solve
    - palace/linalg/nleps.cpp:568       # residual deflation coords X[j]ᴴ vv -> Newton numerator via out-param u2
    - palace/linalg/nleps.cpp:675       # complex eigenvalue Newton ratio -(w0ᴴu + u2_w0)/(w0ᴴw); TWO Dot calls on this line
  observable_weighted:                 # bilinear_form leaf
    - palace/models/boundarymodeoperator.cpp:90   # ComplexWrapperOperator Atn non-Hermitian off-diagonal (wave-1 witness, models/)
  out_of_scope_observable_flagged:
    - palace/models/postoperator.cpp:1759,1760,1795,1796  # port V/I real+imag separately consumed (models/, not audited line-by-line here)
  finding: palace/fem/ has zero Dot callers; the only intra-linalg/ unweighted observable sites are the four nleps.cpp SLEPc-NEP deflation/Newton sites.
```
```

If the integrator prefers minimal theme touch, the alternative is to record this as an OQ only
(below) and let a follow-up `lifter` dispatch fold the inventory into Condition 5 when next
re-anchoring the theme. Either is acceptable; the inventory itself is the load-bearing output.

## Follow-up candidates (for combinator-miner / lifter / abstractor)

- **lifter** — re-anchor `inner-product-fold-specialization` §Condition 5 (or the L1 `dot.md`
  conjugation-asymmetry reconciliation) to cite the four `nleps.cpp` unweighted observable sites,
  giving the bare `dot` leaf its first cited observable witness (today only the weighted leaf has
  one).
- **combinator-miner** — the `nleps.cpp` deflation algebra (`X[j]ᴴ x` projection at `:522,:568`
  + `X[j]ᴴ X[i]` Gram at `:529`) is a recurrent **"project-onto-deflation-subspace"** pattern;
  candidate for an L2 combinator (`deflate` / `gram` over an invariant-pair basis `X`). The
  conjugation convention would be pinned once at the combinator boundary rather than re-derived
  per site.
- **abstractor / harvester** — `orthog.hpp:35` routes Gram-Schmidt inner products through
  `LocalDot` (+`GlobalSum`) directly, bypassing `linalg::Dot`. That is a SECOND unweighted
  inner-product surface with the same arg-2-conj convention but a different call shape; it was
  out of this `Dot`-caller census. A `same-layer-cross-cutter` or harvester pass on `orthog.hpp`
  should classify its conjugation observability (Gram-Schmidt coefficients are generally
  observable) — likely a coverage gap of its own.

## Supporting evidence

All ranges `read_range`-verified this invocation (paths relative to `reference/`):
- `palace/linalg/iterative.cpp:388-470` — the four CG/PCG coefficient sites + their `CheckDot`/`sqrt(abs)` consumers.
- `palace/linalg/operator.cpp:595-640` — `Norml2` real (`:600-605`) + complex (`:610-617`) SPD-realness consumers; weighted-`Dot` defs (`:621-638`) with internal `return Dot(comm,Ax,y)` at `:628,:637`.
- `palace/linalg/nleps.cpp:480-580` — `:487,:492` self-norms; `:522` deflation proj; `:529` Gram; `:543` self-norm; `:568` residual coords; `:575` `squaredNorm` consumer.
- `palace/linalg/nleps.cpp:580-745` — `:587` `compute_residual` call binding `u2=rr2`; `:674` `u2_w0=w2.adjoint()*u2`; `:675` the two Newton-ratio `Dot` calls; `:696,:737` self-norms; the `deflated_solve(z,z2,du,du2)` → `v2_trial` → `compute_residual` flow confirming `x2`/`u2` are complex-consumed.
- search_text `Dot\(` over `palace/linalg/**` (44 hits, triaged) and `palace/fem/**` (0 hits); `\.Dot\(|->Dot\(` over `palace/**` (0 hits); `linalg::Dot\(` over `palace/**` (20 hits, incl. the `models/` adjacencies).
- Wave-1 audit `reports/2026-05-29T034441Z-lowering-verifier-inner-product-fold/CYCLE.md` — confirmed `linalg::Dot = x·conj(y) = yᴴ x` per-line, and the invisible/observable witness pair.

## Open questions / caveats

- **OQ (evidence-completion, small, non-blocking)** —
  `dot-conjugation-observable-callers-nleps-cohort`: the four `nleps.cpp` unweighted observable
  `Dot` sites (`:522,:529,:568,:675`) are the only intra-`linalg/` instances where the L1 arg-1
  vs Palace arg-2 conjugation convention is load-bearing. **Follow-up**: lifter folds them into
  `inner-product-fold-specialization` §Condition 5 (the proposed-changes block above), giving the
  bare `dot` leaf its first cited unweighted observable witness. No status change implied.

- **Caveat (Gram realness at `:529`)** — the deflation Gram `SS(i,j) = X[j]ᴴ X[i]` is Hermitian,
  so its *diagonal* is real and a diagonal-only consumption would be invisible. It is classified
  observable because the **off-diagonal** entries (complex, convention-sensitive) feed the LU
  solves at `:532-533`. The risk is the off-diagonal transpose, not the diagonal.

- **Caveat (`:568` invisibility-via-`squaredNorm` is a near-miss)** — `rr2`'s immediate
  consumption at `:575` is `.squaredNorm()` (invisible). It is classified **observable** only
  because `rr2` escapes as the out-param `u2` into the `:674-675` Newton numerator. A reader
  checking only the residual-norm return would wrongly classify it invisible; the out-param data
  flow is the load-bearing link. (This is the subtlest site in the census.)

- **Caveat (weighted-`Dot` passthrough)** — `operator.cpp:628,:637` are not independent caller
  sites; they are the bodies of the weighted `Dot(comm,x,A,y)` overloads. Observability is
  decided at the *caller* of the weighted form. In scope there are no `linalg/`-internal callers
  of the weighted `Dot` (the only callers are in `models/boundarymodeoperator.cpp:85,:90`), so the
  weighted leaf contributes no in-scope observable site.

- **Caveat (scope boundary)** — `palace/models/postoperator.cpp:1759-1796` (port V/I) and
  `boundarymodeoperator.cpp:85,:90` are in `models/`, outside my declared `linalg/`+`fem/` scope.
  I cite them for completeness (and `:90` is the wave-1 witness) but did NOT exhaustively audit
  the `models/` tree; a `models/`-scoped cross-cut should census `postoperator.cpp` (the V/I sites
  are clearly observable — real and imag consumed separately). Flagged, not enacted.

- **Direction-of-definition: clean.** This is a read-only L0-evidence census feeding an L2>L1
  theme's applicability evidence; no high→low violation, no `book/` mutation. The proposed-changes
  block is a proposal for the integrator, per dispatch-phase write-guard.
