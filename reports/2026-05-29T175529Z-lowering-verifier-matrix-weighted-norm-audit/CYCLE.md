---
agent: lowering-verifier
invoked_at: 2026-05-29T18:03:03Z
scope: L1>L0 theme audit — matrix-weighted-norm-mutation-rotation
status: integrated
integrated_at: 2026-05-29T21:15:00Z
integration_commit: 8f14978
integration_notes: "cycle-027 finalize. Pure additive audit landing: appended a 19-entry verified_against: block (~~~yaml tilde-fenced at EOF, toggle-safe) to L1-L0/matrix-weighted-norm-mutation-rotation.md. Verdict fully-supported; theme STAYS firm; ZERO content/status change. Residual matrix-weighted-norm-mixed-element-type-variant L1-ENTRY promotion gate migrates to the plan (the L1 entry matrix-weighted-norm.md stays rough-in (test-coverage-bounded), its own independent gate; a firm lowering of a rough-in operator is legitimate per the eigsolve-mutation-rotation precedent). retroactive-budget 0; clean build (the tilde-fenced yaml renders as a fenced code block, intended)."
inputs:
  - book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md
  - reference/palace/palace/linalg/operator.cpp:599-619 (two Norml2 specializations)
  - reference/palace/palace/linalg/operator.hpp:372-389 (decl + Normalize + bilinear-form sibling)
  - reference/palace/palace/linalg/arpack.cpp:433-444,470 (M-orthonormalisation callsite + reuse loop)
  - reference/palace/palace/linalg/slepc.cpp:470-481,505 (callsite + reuse loop)
  - reference/palace/palace/linalg/nleps.cpp:109-120,146 (callsite + reuse loop)
  - book/src/L0/linalg-operator-file.md:30-34 (L0 free-function chapter)
  - book/src/L1/matrix-weighted-norm.md (LHS operator, rough-in test-coverage-bounded)
  - book/src/L1-L0/apply-linop-mutation-rotation.md (Sub-pattern A reuse, step 1)
  - book/src/L1-L0/dot-mutation-rotation.md (Sub-pattern A reuse, step 2)
  - book/src/L1/apply_linop.md, book/src/L1/dot.md (L1 law anchors)
---

# CYCLE: Audit matrix-weighted-norm-mutation-rotation

## Summary

Audited the firm L1>L0 theme `matrix-weighted-norm-mutation-rotation` (authored firm
cycle-026, not previously audited) against on-disk `reference/palace/` L0 evidence, using
`tools/citecheck/citecheck.py --anchor`/`--scan` as the mechanical line-map adjudicator plus
deliberate `read_range` reads of every cited body. **Top-level verdict: fully-supported.** The
energy-norm lowering `‖x‖_B = √(xᴴBx)` → Palace's `linalg::Norml2(comm, x, B, Bx)` three-step
composition `B.Mult(x,Bx); dot=Dot(comm,Bx,x); return std::sqrt(dot)` appears verbatim at
`palace/linalg/operator.cpp:599-619` (both specializations); every body anchor (`:602`/`:603`/`:604-605`/`:606`
real, `:612`/`:613-614`/`:615`/`:616-617`/`:618` complex) lands clean. The full-file scan reports
**39 OK / 0 failing**. The two sibling sub-theme reuses (apply-linop Sub-pattern A for the leading
`B.Mult`; dot Sub-pattern A for the inner `Dot`) are structurally correct and non-duplicating —
each is referenced, not restated. The SPD `MFEM_ASSERT(dot > 0.0)` guard is correctly classified
load-bearing-defensive (with the complex branch's second clause correctly read as a numerical
Hermiticity witness). The variant axes (element-type real|complex collapsed at L1; weight-operator
M/B-weighted; B=I degenerate→nrm2) are complete and source-witnessed. Cycle-026's critic note holds:
operator.cpp/hpp and the callsite cohort are NOT affected by the nleps.cpp +1 codemap drift — all
nleps anchors land on the asserted lines. Recommend attaching the additive `verified_against:` block;
no contradictions, no status reduction. The `matrix-weighted-norm-mixed-element-type-variant` gate
(real-B-on-complex-x policy) remains an **upstream L1-entry promotion gate**, faithfully recorded by
this theme at the L0 surface but not resolved by it (and correctly not claimed resolved).

## Per-citation audit

### Real specialization body — `palace/linalg/operator.cpp:599-607`
- **Citation**: `palace/linalg/operator.cpp:599-607`; pinpoints `:602`, `:603`, `:604-605`, `:606`.
- **Theme claim**: real `Norml2` = `B.Mult(x,Bx); double dot=Dot(comm,Bx,x); MFEM_ASSERT(dot>0.0,...); return std::sqrt(dot)`.
- **Found** (read + citecheck `--anchor`): line-exact. `:600` signature `double Norml2(MPI_Comm comm, const Vector &x, const Operator &B, Vector &Bx)`; `:602 B.Mult(x, Bx);`; `:603 double dot = Dot(comm, Bx, x);`; `:604-605 MFEM_ASSERT(dot > 0.0, "Non-positive vector norm ...")`; `:606 return std::sqrt(dot);`. Every `--anchor` returned `[ok]` at the exact line.
- **Verdict**: supports.
- **Notes**: The theme's Sub-pattern A code block transcribes the source faithfully (the `Vector` element type, the exact three-step order). No drift.

### Complex specialization body — `palace/linalg/operator.cpp:609-619`
- **Citation**: `palace/linalg/operator.cpp:609-619`; pinpoints `:612`, `:613-614`, `:615`, `:616-617`, `:618`.
- **Theme claim**: complex `Norml2` splits the leading apply into two real lanes, computes a complex `dot`, asserts a two-part guard, returns `std::sqrt(dot.real())`.
- **Found**: line-exact. `:612 // For SPD B, xᴴ B x is real.`; `:613 B.Mult(x.Real(), Bx.Real());`; `:614 B.Mult(x.Imag(), Bx.Imag());`; `:615 std::complex<double> dot = Dot(comm, Bx, x);`; `:616-617 MFEM_ASSERT(dot.real() > 0.0 && std::abs(dot.imag()) < 1.0e-9 * dot.real(), ...)`; `:618 return std::sqrt(dot.real());`. All `--anchor` checks `[ok]`.
- **Verdict**: supports.
- **Notes**: The theme reads the `// For SPD B, xᴴ B x is real.` comment as a *positive* anchor for the value-level identity `xᴴBx ∈ ℝ` — this is correct and is what licenses `firm` over `partly-constructive` (the identity is not negative-anchor-reconstructed; it is read off the source's own comment + assertion). The 1e-9 relative tolerance literal in the theme matches the source exactly.

### Header decl + SPD comment — `palace/linalg/operator.hpp:372-374`
- **Citation**: `palace/linalg/operator.hpp:372-374`, comment at `:372`.
- **Theme claim**: `Norml2(comm, x, B, Bx)` template decl with `// Calculate the vector norm with respect to an SPD matrix B.`; SPD precondition stated at L0.
- **Found**: `:372 // Calculate the vector norm with respect to an SPD matrix B.`; `:373 template <typename VecType>`; `:374 double Norml2(MPI_Comm comm, const VecType &x, const Operator &B, VecType &Bx);`. `--anchor` `[ok]`.
- **Verdict**: supports.
- **Notes**: The SPD precondition at L0 is genuinely a *comment* (documentation), not a structural check — the theme is precise about this (the structural SPD enforcement is the `MFEM_ASSERT(dot>0.0)` run-time guard, separately classified). Good distinction.

### Normalize consumer — `palace/linalg/operator.hpp:377-384`
- **Citation**: `palace/linalg/operator.hpp:377-384`; `:380`, `:381`, `:382`.
- **Theme claim** (Sub-pattern C): `Normalize` calls `Norml2`, asserts positive, scales `x *= 1.0/norm` in place; at L1 = `scal(1/matrix_weighted_norm(x,B), x)`, the `scal` step inherited.
- **Found**: `:378 inline double Normalize(MPI_Comm comm, VecType &x, const Operator &B, VecType &Bx)`; `:380 double norm = Norml2(comm, x, B, Bx);`; `:381 MFEM_ASSERT(norm > 0.0, "Zero vector norm in normalization!");`; `:382 x *= 1.0 / norm;`. `--anchor` `[ok]`.
- **Verdict**: supports.
- **Notes**: The theme's observation that the `Normalize` `MFEM_ASSERT(norm > 0.0)` is "redundant with `Norml2`'s internal `dot > 0.0` guard but documents the divisor-positivity contract at the call boundary" is exactly right — `Norml2` already aborts on non-positive `dot`, so `norm` is provably positive before line 381 fires. The redundancy framing is accurate.

### Sibling bilinear-form boundary — `palace/linalg/operator.hpp:386-389`
- **Citation**: `palace/linalg/operator.hpp:386-389`; comment `:386-387`.
- **Theme claim**: cited only to mark the boundary — bilinear-form `Dot(comm, x, A, y) = yᴴ A x` allocates its workspace `Ax` internally (Category-4 synthetic), contrasting the caller-supplied `Bx`; it is a *different operator*, not part of this theme.
- **Found**: `:386-387 // Compute the bilinear form inner product yᴴ A x for a real operator A and complex vectors. Allocates workspace internally.`; the implementation at `palace/linalg/operator.cpp:621-639` confirms `ComplexVector Ax(A.Height());` (internal allocation, `palace/linalg/operator.cpp:624`). The theme's `palace/linalg/operator.cpp:621-639` citation for the impl is in-bounds (operator.cpp has 698 lines per citecheck) and the internal-allocation claim is directly witnessed at `palace/linalg/operator.cpp:624`.
- **Verdict**: supports.
- **Notes**: Correct boundary-marking. The "diagonal case y=x of the bilinear form, plus the outer √ and SPD condition" framing of the energy norm vs. the bilinear form is accurate and a clean delineation. The forthcoming `bilinear-form-mutation-rotation` theme is named as a forward-reference (plain text — appropriate, not yet on disk).

### M-orthonormalisation callsite cohort (arpack / slepc / nleps)
- **Citations**: `arpack.cpp:433-444` (`:438`,`:442`), `:470`; `slepc.cpp:470-481` (`:475`,`:479`), `:505`; `nleps.cpp:109-120` (`:114`,`:118`), `:146`.
- **Theme claim**: three-backend `GetEigenvectorNorm` dispatches to weighted `linalg::Norml2(comm, x, *opB, Bx)` when `opB` non-null, else unweighted `linalg::Norml2(comm, x)`; the reuse loop `xscale.get()[i] = 1.0 / GetEigenvectorNorm(x1, y1)` reuses a single `Bx` (named `y1`) across all eigenvectors.
- **Found**: all line-exact. arpack `:438 return linalg::Norml2(comm, x, *opB, Bx);` / `:442 return linalg::Norml2(comm, x);` / `:470 xscale.get()[i] = 1.0 / GetEigenvectorNorm(x1, y1);`. slepc identical pattern with `:475 return linalg::Norml2(GetComm(), x, *opB, Bx);` (note `GetComm()` not bare `comm` — **theme correctly flags this**) / `:479 return linalg::Norml2(GetComm(), x);` / `:505`. nleps `:114 return linalg::Norml2(comm, x, *opB, Bx);` / `:118 return linalg::Norml2(comm, x);` / `:146`. All `--anchor` `[ok]`.
- **Verdict**: supports.
- **Notes**: The cycle-026 critic note is confirmed — the nleps.cpp +1 codemap drift (cycle-025) does NOT affect these anchors; `nleps.cpp:114` and `:146` land on the asserted lines under on-disk read. The "reuse `Bx` across eigenvectors = transparent performance trick (allocation hoisting)" classification is sound: `y1` is allocated once outside the `for (int i = 0; i < num_eig; i++)` loop and passed by reference into every `GetEigenvectorNorm` call. The reuse-loop body at `:471`/`:506-507`/`:147` also uses `y1` again for the residual-norm computation, reinforcing the caller-owned-reuse reading (out of this theme's scope, but consistent with it).

### L0 chapter — `book/src/L0/linalg-operator-file.md:30-34`
- **Citation**: `book/src/L0/linalg-operator-file.md:30-34`.
- **Theme claim**: the L0 chapter names the `linalg::` free-function block (SPD-weighted `Norml2`, `Normalize`, bilinear-form `Dot(comm,x,A,y)`, `SpectralNorm`).
- **Found**: `:30` heads the `linalg:: free functions` bullet; `:31` names `Norml2(comm, x, B, Bx)` with impl at `palace/linalg/operator.cpp:600-619`; `:32` `Normalize`; `:33` bilinear-form `Dot(comm, x, A, y)` (Category 4 synthetic workspace); `:34` `SpectralNorm`. `--scan` `[ok]`.
- **Verdict**: supports.
- **Notes**: One benign framing difference — the L0 chapter (`:31`) gives the `Norml2` impl as `palace/linalg/operator.cpp:600-619` (starting at line 600, the signature line), while this theme uses `:599-607`/`:609-619` (starting at line 599, the `template <>` line). Both bracket the same two bodies; the theme's split-by-specialization form is the more precise one. No contradiction.

## Applicability conditions

1. **Read-only `x` and `B`.**
   - **Verifiable**: yes. `Norml2` takes `const Vector &x` / `const ComplexVector &x` and `const Operator &B`; `B.Mult` is a `const` virtual (apply-linop condition 4). The only buffer mutation is the `Bx` overwrite (the inherited apply_linop rotation). Read-confirmed at `palace/linalg/operator.cpp:600`/`:610` signatures.
   - **Found counter-example?**: no.

2. **`B` square, SPD (or SPSD seminorm caveat).**
   - **Verifiable**: yes. Run-time positivity enforced via `MFEM_ASSERT(dot > 0.0)` (`:604-605` real, `:616` clause-1 complex) — strict SPD, treating SPSD-zero as error (matches the L1 entry `:76` reading). Squareness is implicit via the `Bx` (length `B.Height()`) dotted against `x` (length `N`) ⇒ the inherited dot aligned-pass `MFEM_ASSERT(Bx.Size()==x.Size())` forces `B.Height()==N`.
   - **Found counter-example?**: no.

3. **`B` Hermitian (self-adjoint).**
   - **Verifiable**: partially — not structurally checked at L0 (no `B == Bᴴ` test). The complex branch's `std::abs(dot.imag()) < 1e-9 * dot.real()` (`:616-617`) is the numerical proxy. The theme states this precisely (numerical witness, not structural check). Confirmed by read.
   - **Found counter-example?**: no — and the theme does NOT over-claim a structural check, which is the correct posture.

4. **Caller-supplied `Bx` of length `B.Height()`, aliasing neither `x` nor the result.**
   - **Verifiable**: yes. `VecType &Bx` is a caller parameter (`:600`/`:610`); step 1 overwrites it entirely (`B.Mult(x, Bx)`); step 2 reads `Bx` and `x`. Allocation-hoist/reuse across calls is witnessed at the three reuse loops (`y1` reused across `num_eig`). Read-confirmed.
   - **Found counter-example?**: no.

5. **Single-rank reading of the collective.**
   - **Verifiable**: yes (inherited from dot-mutation-rotation condition 4). The `MPI_Allreduce` inside the inner `Dot` is a local no-op single-machine, structurally present, bit-determinism caveat carried. Correctly inherited, not restated.
   - **Found counter-example?**: N/A (inherited; scope-flagged per CLAUDE.md "Scope").

6. **Conjugate-pair re-order invisible.**
   - **Verifiable**: yes. The inner `Dot(comm, Bx, x)` computes `xᴴ(B·x)` (arg-2 conjugated, per dot Sub-pattern A leaf `yᴴx`); the result feeds `std::sqrt` as a real projection (real `double`; complex `dot.real()`), so `xᴴy = conj(yᴴx)` re-order is invisible — same re-order-invisible case as `nrm2`. Cross-checked against `book/src/L1/dot.md:43` (L1 conjugate-in-first convention) — consistent.
   - **Found counter-example?**: no.

All six conditions are verifiable from cited evidence and none has a counter-example.

## Algebraic laws (cited)

- **L1 law 8** — `matrix_weighted_norm(x, B)² = xᴴ B x`. Cited at `L1/matrix-weighted-norm.md:58`.
  - **Holds on operators?**: yes. The L1 entry `:58` itself records the L0 factorization `B.Mult(x,Bx); dot=Dot(comm,Bx,x); return std::sqrt(dot)`; squaring the L0 return gives `dot = Dot(comm,Bx,x) = xᴴ(Bx) = xᴴBx`. The defining identity is exactly the lowering's first two steps before the `√`. Holds.

- **L1 law 9** — `matrix_weighted_norm(x, I) = nrm2(x)` (identity-weight collapse). Cited at `L1/matrix-weighted-norm.md:59`.
  - **Holds on operators?**: yes. With `B=I`, step 1 `I.Mult(x,Bx)` ⇒ `Bx = x`, so step 2 `Dot(comm,x,x) = xᴴx`, and `√(xᴴx) = nrm2(x)`. The theme's degenerate-collapse claim (the two themes meet at the identity weight, the weighted `MFEM_ASSERT(dot>0)` replacing nrm2's `std::abs`) is sound. The eigensolver fallback path (`opB` null → unweighted `Norml2(comm, x)`) is the live L0 witness of this boundary — confirmed at `:442`/`:479`/`:118`.

- **apply_linop laws 1, 4, 5, 6** — linearity-in-x / composition / sum / scalar. Cited at `book/src/L1/apply_linop.md:50,53-55`.
  - **Holds on operators?**: yes — these underwrite the `B·x` step. Read-confirmed at `:50` (linearity), `:53` (composition, witnessed by `BaseProductOperator::Mult`), `:54` (sum), `:55` (scalar). The theme uses them correctly to justify that the `apply_linop(B,x)` step is collapse-invariant across `B`'s operator-representation axis.

- **dot conjugation convention + reduction-tree non-law** — `book/src/L1/dot.md:43,45`.
  - **Holds on operators?**: yes. `:43` confirms the L1 conjugate-in-first convention (free-function form names the conjugated argument first); `:45` confirms the load-bearing reduction-tree non-associativity. The theme correctly maps the L0 surface `Dot(comm, Bx, x)` (= `xᴴ(Bx)`, arg-2 = `x` conjugated) onto the L1 convention, and correctly inherits the reduction non-law rather than restating it.

No algebraic law is misstated; every cited law holds on the operator signatures and is used consistently with its source statement.

## Sibling sub-theme reuse — correctness + non-duplication

- **apply-linop Sub-pattern A (step 1, `B.Mult(x, Bx)`)**: CORRECT and non-duplicating. apply-linop Sub-pattern A ("bare forward apply (`Mult`)") exists at `apply-linop-mutation-rotation.md:43`. The theme references it for the leading apply and does NOT restate the operator-representation variant-axis collapse (sparse/matrix-free/composition/multigrid) — it inherits it. The complex-branch two-lane split (`B.Mult(x.Real(),Bx.Real()); B.Mult(x.Imag(),Bx.Imag())`) is correctly attributed to apply-linop's **condition 3** (`:216-225`), which covers "Mixed real-operator-on-complex-vector requires lifting via `ComplexWrapperOperator` ... the `complex-from-real-lift` concept." Attribution verified line-exact.
- **dot Sub-pattern A (step 2, `Dot(comm, Bx, x)`)**: CORRECT and non-duplicating. dot Sub-pattern A ("free-function template `linalg::Dot(comm, x, y)`") exists at `dot-mutation-rotation.md:44`, with the `LocalDot` + `Mpi::GlobalSum` two-step (`:50-51`) and the **arg-2-conjugated** leaf (`:59-60`, `yᴴx`). The theme inherits the two-step + MPI collective + reduction-tree non-law rather than restating, and correctly maps the arg-order onto `xᴴ(B·x)`.
- **scal (Sub-pattern C consumer, `x *= 1.0/norm`)**: CORRECT inherited step. The `Normalize` in-place scale delegates to `scal-mutation-rotation` (referenced, not restated).

No duplication: each sub-theme is referenced by slug + sub-pattern, and the genuinely-new content (caller-owned `Bx` workspace, real/imag Mult split, outer `√`, SPD guard, Normalize consumer) is what the theme actually authors. This is a clean structural reuse.

## SPD guard classification audit

The theme classifies `MFEM_ASSERT(dot > 0.0, ...)` (`:604-605` real; `:616-617` complex) as **load-bearing numerical (defensive guard + SPD-violation detector)**. Audit:
- **Exact-arithmetic no-op for SPD `B`, `x≠0`**: correct — `xᴴBx > 0` strictly, so the assertion never fires; it disappears at L1 (subsumed by L1 laws 1/2/8). Sound.
- **Floating-point load-bearing**: correct — guards against a round-off sign-flip on a tiny `xᴴBx` (which would make `std::sqrt` return `NaN`) AND is the run-time witness that the SPD applicability condition is violated for an indefinite `B`. Sound.
- **Stronger than nrm2's `std::abs`**: correct and well-argued — nrm2 *silently repairs* a tiny-negative self-dot (`abs` strips the sign), whereas `Norml2` *aborts*; the rationale (for the weighted form a non-positive value signals a violated SPD precondition, not mere round-off, and silent repair would mask an algorithm error) is exactly right.
- **Complex branch second clause = numerical Hermiticity witness** (`std::abs(dot.imag()) < 1e-9*dot.real()`): correct — asserts the imaginary part is round-off relative to the real part; the source does NOT verify `B = Bᴴ` directly, this is the proxy; the return discards `dot.imag()`. Read-confirmed at `:616-618`.

**Verdict: the load-bearing-defensive classification is sound and consistent** with the nrm2 abs-guard precedent and the `L0/transparent-vs-load-bearing-tricks` "Defensive non-negativity guard" worked example, with the additional SPD-detector role correctly noted.

## Variant-axis completeness audit

Per `classify-variant-axis`, the theme states two orthogonal axes + one degenerate collapse:
- **element-type (real|complex)** — the two `Norml2<VecType>` specializations (`VecType ∈ {Vector, ComplexVector}`, `palace/linalg/operator.cpp:599-619`); collapsed at L1 to a single real-valued operator. COMPLETE and source-witnessed (both bodies read).
- **weight-operator-representation of `B` (M-weighted / B-weighted)** — runtime polymorphism of `B.Mult`; collapsed at L1 per apply_linop's representation-axis absorption. Witnessed by the `*opB` callsites passing the mass matrix; null `opB` → unweighted fallback (`arpack.cpp:438-442`, `slepc.cpp:475-479`, `nleps.cpp:114-118` — all in-bounds). COMPLETE.
- **degenerate collapse B=I → nrm2** — L1 law 9; the live L0 witness is the eigensolver `opB`-null fallback to unweighted `Norml2(comm, x)`. COMPLETE.

The theme correctly states "no other variant axes — unconditionally exhaustive over length axis `N`, no masking/strided variants" and correctly separates the output-arg-vs-return distinction (the `Bx` workspace) as the workspace-ownership boundary, not a variant axis. **Variant-axis coverage is complete and exhaustive.**

## The mixed-element-type variant gate — disposition

The `matrix-weighted-norm-mixed-element-type-variant` (real-B-on-complex-x policy) question — whether L1 admits the real-`B`-on-complex-`x` case as a *distinct element-type variant* or absorbs it into a *uniform element-type rule* — is faithfully recorded by this theme at the L0 surface (Sub-pattern B, the lane split `:613-614`) and explicitly flagged as an **upstream L1-side question** (theme lines 134-137, referencing `L1/matrix-weighted-norm.md` §Variant axes). Read-confirmed at the L1 entry `:106`: the promotion-to-firm gate for the L1 entry names exactly this — "whether the complex-x-with-real-B specialization should be treated as a distinct element-type variant at L1 or be absorbed into a uniform element-type rule," recorded as an Open question.

**Assessment**: This is NOT resolved by this theme, and the theme correctly does NOT claim to resolve it. The L1-entry-side resolution is a separate gate (the L1 entry is `rough-in (test-coverage-bounded)` per `:110`). The relationship is sound and consistent with the "Note on the upstream L1 gate" in the theme's Status section: a *firm lowering of a rough-in L1 operator* is legitimate because the lowering's structural fidelity (does the L1 form expand into this L0 source? — YES, verified) is independent of the L1 law-confidence / variant-policy gate. The theme does not over-reach; the gate remains open on the L1 side. **Disposition: remains an upstream promotion-gate; not blocking this theme's firm status; faithfully recorded.**

## Proposed changes

Recommend attaching the additive `verified_against:` block. The audit found the theme fully-supported with no contradictions, so the only change is the metadata block (consumed by `cross-layer-cross-cutter`). Append at end of file:

```edit:book/src/L1-L0/matrix-weighted-norm-mutation-rotation.md
[append at end of file]
~~~yaml
verified_against:
  - citation: palace/linalg/operator.cpp:599-607
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: real Norml2 spec; B.Mult(:602)/Dot(:603)/MFEM_ASSERT(:604-605)/sqrt(:606) all citecheck --anchor OK
  - citation: palace/linalg/operator.cpp:609-619
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: complex Norml2 spec; lane split(:613-614)/dot(:615)/two-part guard(:616-617)/sqrt(dot.real())(:618); SPD-real comment(:612) positively anchors xᴴBx∈ℝ
  - citation: palace/linalg/operator.hpp:372-374
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: Norml2 decl + SPD comment(:372); precondition is documentation, structural SPD enforcement is the run-time guard
  - citation: palace/linalg/operator.hpp:377-384
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: Sub-pattern C Normalize; norm=Norml2(:380)/assert(:381)/x*=1/norm(:382); assert redundant-but-boundary-documenting
  - citation: palace/linalg/operator.hpp:386-389
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: bilinear-form boundary marker; internal Ax alloc confirmed at palace/linalg/operator.cpp:624; correctly excluded from theme
  - citation: palace/linalg/arpack.cpp:433-444
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: GetEigenvectorNorm dispatch; weighted(:438)/unweighted-fallback(:442)
  - citation: palace/linalg/arpack.cpp:470
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: reuse-Bx-across-eigenvectors loop body (y1 reused)
  - citation: palace/linalg/slepc.cpp:470-481
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: identical pattern; GetComm()(:475) not bare comm, theme correctly flags; unweighted-fallback(:479)
  - citation: palace/linalg/slepc.cpp:505
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: SLEPc reuse loop body
  - citation: palace/linalg/nleps.cpp:109-120
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: identical pattern; weighted(:114)/unweighted-fallback(:118); NOT affected by cycle-025 nleps +1 codemap drift (anchors land on asserted lines)
  - citation: palace/linalg/nleps.cpp:146
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: NLEPS reuse loop body
  - citation: book/src/L0/linalg-operator-file.md:30-34
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: L0 chapter names the linalg:: free-function block; benign framing diff (:31 gives impl as :600-619 vs theme :599/:609)
  - citation: book/src/L1/matrix-weighted-norm.md:58
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: L1 law 8 self-bilinear identity; underwrites the lowering's √(dot) structure
  - citation: book/src/L1/matrix-weighted-norm.md:59
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: L1 law 9 identity-weight collapse; underwrites B=I→nrm2 degenerate boundary (eigensolver opB-null fallback is the L0 witness)
  - citation: book/src/L1/matrix-weighted-norm.md:106
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: mixed-element-type variant gate is an UPSTREAM L1-entry promotion gate; faithfully recorded, not resolved by this theme, correctly not claimed resolved
  - citation: book/src/L1-L0/apply-linop-mutation-rotation.md:43
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: Sub-pattern A reuse (step 1 B.Mult); complex-from-real-lift correctly attributed to apply-linop condition 3 (:216-225)
  - citation: book/src/L1-L0/dot-mutation-rotation.md:44
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: Sub-pattern A reuse (step 2 Dot); arg-2-conjugated leaf(:59-60) + reduction-tree non-law inherited, not restated
  - citation: book/src/L1/apply_linop.md:50
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: laws 1/4/5/6 (:50,:53-55) underwrite the B·x apply across operator-representation axis
  - citation: book/src/L1/dot.md:43
    verdict: supports
    audited_at: 2026-05-29T18:03:03Z
    note: conjugate-in-first convention(:43) + load-bearing reduction-tree non-law(:45)
~~~
```

No content edits are proposed (no contradiction found). The two benign framing differences noted
(L0-chapter `:600` vs theme `:599`/`:609` enclosing-range start; L1-entry `:601-606` vs theme
`:599-607` for the real spec) are NOT drift — both bracket the same bodies and the theme's
split-by-specialization form is the more precise one. No carry-forward citation correction needed.

## Supporting evidence

- `reference/palace/palace/linalg/operator.cpp:595-644` — read; both `Norml2` specializations + the
  sibling bilinear-form `Dot` impls (internal `Ax` alloc at `:624`) + `SpectralNorm` head.
- `reference/palace/palace/linalg/operator.hpp:368-392` — read; `Norml2` decl + `Normalize` inline +
  bilinear-form decls.
- `reference/palace/palace/linalg/arpack.cpp:431-446,466-473` — read; `GetEigenvectorNorm` + reuse loop.
- `reference/palace/palace/linalg/slepc.cpp:468-483,502-508` — read; identical pattern + reuse loop.
- `reference/palace/palace/linalg/nleps.cpp:107-122,143-148` — read; identical pattern + reuse loop.
- `book/src/L0/linalg-operator-file.md:25-38` — read; L0 free-function chapter.
- `book/src/L1/matrix-weighted-norm.md:1-25,58-59,72-79,106,108-140` — read; LHS operator, laws,
  applicability conditions, status (`rough-in test-coverage-bounded`).
- `book/src/L1-L0/apply-linop-mutation-rotation.md:43,215-229,252` — read; Sub-pattern A + condition 3.
- `book/src/L1-L0/dot-mutation-rotation.md:5-6,44-78` — read; Sub-pattern A + conjugation asymmetry.
- `book/src/L1/apply_linop.md:50,53-55`, `book/src/L1/dot.md:43,45` — read; cited L1 laws.
- `tools/citecheck/citecheck.py --anchor` (21 anchor checks, all `[ok]`) + `--scan` on the theme file
  (**39 OK / 0 failing**) — mechanical line-map adjudication.

## Open questions / caveats

- **Directionality**: the theme narrates forward (L1 → L0): "Lowers the pure L1 form ... into Palace's
  L0 ...". No high→low directionality violation.
- **`bilinear-form-mutation-rotation` forward-reference**: the theme names a not-yet-on-disk sibling
  theme (`bilinear-form-mutation-rotation`) as plain text — appropriate per the
  `rough-in-forward-reference-must-be-plain-text` convention. Not a finding.
- **Mixed-element-type gate**: remains OPEN on the L1-entry side (see disposition above) — it is the
  upstream L1 operator's promotion gate, not this theme's. This theme is correctly firm over the
  rough-in L1 operator (lowering structural fidelity is independent of the L1 law/variant gate).
- **Nothing un-auditable**: every cited L0 range resolved and read; no runtime-state dependence; no
  out-of-range citation.

### OQ ledger disposition (append to scaffolding/open-questions.md)

Append the following disposition under slug
`matrix-weighted-norm-mutation-rotation-lowering-verifier-audit-followup`:

> **matrix-weighted-norm-mutation-rotation-lowering-verifier-audit-followup** (cycle-027,
> lowering-verifier). The firm L1>L0 theme `matrix-weighted-norm-mutation-rotation` was audited
> against on-disk `reference/palace/` L0 evidence (citecheck `--anchor` ×21 all OK; `--scan` 39/39).
> **Verdict: fully-supported, no contradiction, no status reduction.** The `verified_against:` block
> (19 entries) is recommended for attachment by `integrator-per-report`. The
> `matrix-weighted-norm-mixed-element-type-variant` (real-B-on-complex-x) question is confirmed to
> remain an **upstream L1-entry promotion gate** (`L1/matrix-weighted-norm.md` is `rough-in
> test-coverage-bounded`, gated on a dedicated `linalg::Norml2(comm,x,B,Bx)` unit test + the
> element-type-variant-vs-uniform-rule policy decision) — NOT a defect in this theme, which is
> correctly firm over the rough-in LHS. cycle-026 critic's nleps.cpp-not-drift note CONFIRMED
> (operator.cpp/hpp + callsite cohort all land on asserted lines). **Disposition: AUDIT-CLOSED for the
> theme; the residual L1-entry promotion gate migrates to the plan as the next harvester/test-coverage
> target on `L1/matrix-weighted-norm.md` (lower priority — test entry point may be out of write-scope
> if no `test-operator*.cpp`/`test-eigen*.cpp` exercises the weighted overload, per the L1 entry's own
> status note).**
