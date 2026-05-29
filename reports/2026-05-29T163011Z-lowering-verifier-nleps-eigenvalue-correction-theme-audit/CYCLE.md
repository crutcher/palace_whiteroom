---
agent: lowering-verifier
invoked_at: 2026-05-29T16:47:49Z
scope: L1>L0 theme audit — nleps-eigenvalue-correction-mutation-rotation
status: pending
inputs:
  - book/src/L1-L0/nleps-eigenvalue-correction-mutation-rotation.md
  - palace/linalg/nleps.cpp:672-677 (primary L0 site)
  - palace/linalg/nleps.cpp:540,542-545,587,657,668-669,682,684-686,691,704-708,712,637-647,606-619,354-362 (context)
  - palace/linalg/vector.hpp:246 ; palace/linalg/vector.cpp:674-685 (dot convention)
  - book/src/L1/nleps_eigenvalue_correction.md (firm operator lowered)
  - book/src/L1/dot.md:43 (arg-1 conjugation convention)
integrated_at: 2026-05-29T203000Z
integration_commit: 1de17ed
integration_notes: "Applied clean (cycle-026 dispatch-6b). Additive verified_against: YAML block (19 entries, all verdict:supports) appended at EOF; theme stays firm, ZERO content/status change. Audit-followup OQ DISCHARGED; the two re-confirmed L1-entry drifts (:596→:590, :709→:712) resolved same-cycle by D1's lifter re-anchor. Zero gate hits."

# CYCLE: Audit nleps-eigenvalue-correction-mutation-rotation

## Summary

Audited the firm L1>L0 theme `nleps-eigenvalue-correction-mutation-rotation` (authored firm
cycle-025, first audit) against on-disk `reference/palace/palace/linalg/nleps.cpp`. The theme lowers
the pure L1 `nleps_eigenvalue_correction(resid, jac_action, proj_dir)` into the
`// Undamped Newton step for the eigenvalue` block at `:672-677`, decomposed into three firm BLAS-1
sub-patterns (A: projected Newton ratio δλ=−num/den over three `dot` folds; B: big-space step RHS
z=−δλ·w−u as an `axpby` via `AXPBYPCZ` γ=0; C: coordinate step RHS z2=−u2 as a `scal` α=−1), plus a
load-bearing big/coordinate RHS asymmetry and two recorded non-laws. **Verdict: fully-supported.**
All five primary-site lines (`:673`, `:674`, `:675`, `:676`, `:677`) land exactly on-disk via
`citecheck --anchor`; all 31 citations in the theme bounds-check clean (`citecheck --scan` → 31 ok, 0
failing). The three sub-patterns, the Newton-correction semantics, the big/coordinate asymmetry (the
Jacobian action being big-space-only at `:657`/`:668`/`:669`), and both non-laws are all confirmed
on positive source. The `:672-677` block carries **no codemap +1 drift** (the wave-1 codemap drift
was confined to the earlier deflation block `:659+`, as the theme already states). I recommend the
additive `verified_against:` block; no theme mutation is required. Two inherited operator-entry
drifts (`:596`→on-disk `:590`; `:709`→on-disk `:712`) are already correctly flagged BY the theme as
carry-forward notes — they are operator-entry defects routed around, not theme defects (carry-forward
recorded below for the eventual operator-entry lifter pass).

## Per-citation audit

### Primary site `:672-677` (the eigenvalue-correction block)

- **Citation**: `palace/linalg/nleps.cpp:672`
  - **Theme claim**: the source's own comment names the operator: `// Undamped Newton step for the eigenvalue; the line search damps it.`
  - **Found**: `:672` is exactly that comment.
  - **Verdict**: supports. `citecheck --anchor 'Undamped Newton step for the eigenvalue'` → line 672, in range.

- **Citation**: `palace/linalg/nleps.cpp:673`
  - **Theme claim** (Sub-pattern A.1): coordinate inner product `w2ᴴu2`; the local Eigen `w2.adjoint() * u2`, arg-1 (`w2`) conjugated; rank-local, no `Mpi::GlobalSum`.
  - **Found**: `:673` `const std::complex<double> u2_w0 = std::complex<double>(w2.adjoint() * u2);`. `.adjoint()` is conjugate-transpose, so `w2` is conjugated. Local Eigen op, no MPI reduction.
  - **Verdict**: supports. `citecheck --anchor 'w2.adjoint() * u2'` → line 673, in range.

- **Citation**: `palace/linalg/nleps.cpp:674-675`
  - **Theme claim** (Sub-pattern A.2/A.3): `delta_eig = −(linalg::Dot(GetComm(), u, w0) + u2_w0) / linalg::Dot(GetComm(), w, w0)`; numerator `num = w0ᴴu + w2ᴴu2 = ⟨[w0;w2],[u;u2]⟩`, denominator `den = w0ᴴw = ⟨[w0;w2],w⟩`, ratio `δλ = −num/den`. Under `linalg::Dot(comm,x,y)=yᴴx`, C++ arg-2 `w0` conjugated.
  - **Found**: `:674-675` is exactly that two-line expression. `Dot(GetComm(), u, w0)` with x=u, y=w0 ⇒ `w0ᴴu`; `Dot(GetComm(), w, w0)` ⇒ `w0ᴴw`. `num = w0ᴴu + w2ᴴu2`; `den = w0ᴴw`; `δλ = −num/den`. The conjugated operand in every term is the projection direction (`w0`/`w2`).
  - **Verdict**: supports. `citecheck --anchor 'delta_eig'` → 674; `--anchor 'linalg::Dot(GetComm(), w, w0)'` → 675; both in range. Conjugation convention corroborated below (`vector.hpp:246`).

- **Citation**: `palace/linalg/nleps.cpp:676`
  - **Theme claim** (Sub-pattern B): big-space step RHS `z = −δλ·w − u` = `z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0)`; γ=0 reduces `AXPBYPCZ(α,x,β,y,γ)=α·x+β·y+γ·z` to the firm `axpby(−δλ, w, −1, u)` (overwrite, not accumulate); δλ couples in through `w`.
  - **Found**: `:676` `z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0);` — α=−delta_eig, x=w, β=−1.0, y=u, γ=0.0, so `z := −δλ·w − u + 0·z`. The `axpby ≺ axpbypcz` γ=0 subsumption is correctly applied.
  - **Verdict**: supports. `citecheck --anchor 'z.AXPBYPCZ(-delta_eig, w, -1.0, u, 0.0)'` → line 676, in range.

- **Citation**: `palace/linalg/nleps.cpp:677`
  - **Theme claim** (Sub-pattern C): coordinate step RHS `z2 = −u2` = the firm `scal(−1, u2)`; Eigen unary-minus, rank-local, no `Mpi::GlobalSum`; independent of δλ.
  - **Found**: `:677` `z2 = -u2;` — Eigen `VectorXcd` negation, `scal` with α=−1. No dependence on `delta_eig` or `w`.
  - **Verdict**: supports. `citecheck --anchor 'z2 = -u2'` → line 677, in range.

### Producer/consumer context sites

- **Citation**: `palace/linalg/nleps.cpp:587` — **Theme claim**: `compute_residual(eig,...,u,u2,...)` writes the committed `[u;u2]` (the `resid` argument). **Found**: `:587` `double res = compute_residual(eig, v, v2, u, u2, A2n);`. **Verdict**: supports. `--anchor 'compute_residual(eig'` → 587.

- **Citation**: `palace/linalg/nleps.cpp:657` (+ `:668-669`) — **Theme claim**: `opJ->Mult(v, w)` is the big-space-only Jacobian action `w=J·v`; the deflation `AddMult`s also accumulate only into `w`, never a `w2` (the basis for the big/coordinate asymmetry). **Found**: `:657` `opJ->Mult(v, w);`; `:668` `opJ->AddMult(XSv2, w, 1.0);`; `:669` `A->AddMult(XSSv2, w, -1.0);` — all three write into the big-space `w`; no coordinate `w2` write exists anywhere in the Jacobian-action block (`:649-670`). **Verdict**: supports — confirms the load-bearing big-space-only contract. `--anchor 'opJ->Mult(v, w)'` → 657.

- **Citation**: `palace/linalg/nleps.cpp:540` (+ `:542-545`) — **Theme claim**: `[w0;w2]` is the lagged deflated solve `T(σ)⁻¹c` normalized to unit extended-norm; "only used as a projection direction for the eigenvalue correction". **Found**: `:539-540` comment confirms the projection-direction role; `:542` `deflated_solve(c, c2, w0, w2);`, `:543` `norm_w0 = sqrt(|Dot(w0,w0)| + w2.squaredNorm())`, `:544` `w0 *= 1/norm_w0`, `:545` `w2 *= 1/norm_w0` — the extended-norm normalization. **Verdict**: supports. `--anchor 'projection direction for the eigenvalue correction'` → 540; `:542-545` read on-disk exactly as claimed.

- **Citation**: `palace/linalg/nleps.cpp:682` — **Theme claim**: downstream `deflated_solve(z, z2, du, du2)` consumes this atom's output `[z;z2]` as its RHS (the solve sibling). **Found**: `:682` `deflated_solve(z, z2, du, du2);`. **Verdict**: supports. `--anchor 'deflated_solve(z, z2, du, du2)'` → 682.

- **Citation**: `palace/linalg/nleps.cpp:691` — **Theme claim**: the damped application `eig_trial = eig + alpha * delta_eig` (the undamped non-law). **Found**: `:691` `const std::complex<double> eig_trial = eig + alpha * delta_eig;`. **Verdict**: supports. `--anchor 'eig_trial = eig + alpha'` → 691.

- **Citation**: `palace/linalg/nleps.cpp:704-708` — **Theme claim**: Armijo sufficient-decrease test (`:704`) and the eigenvalue commit `eig = eig_trial` (`:708`). **Found**: `:704` `if (res_trial <= (1.0 - armijo_c * alpha) * res || bt == max_backtrack - 1)`; `:708` `eig = eig_trial;`. **Verdict**: supports. `--anchor 'eig = eig_trial'` → 708 (in 704-708).

- **Citation**: `palace/linalg/nleps.cpp:712` — **Theme claim**: Armijo backtrack-factor update `alpha *= backtrack_factor` (α ∈ {1, 0.5, 0.25, …}). **Found**: `:712` `alpha *= backtrack_factor;`. **Verdict**: supports. `--anchor 'alpha *= backtrack_factor'` → 712. (Note: the L1 operator entry's `:709` for this is a −3 drift; the theme uses the corrected `:712` and already flags `:709` — see carry-forward.)

- **Citation**: `palace/linalg/nleps.cpp:684-686` — **Theme claim**: the `⟨[w0;w2],w⟩=0` near-singularity, source comment `<w0, w> is near-singular`. **Found**: `:684-686` Armijo comment; `:685-686` `... or <w0, w> is // near-singular — observed on adapter/hybrid mode 3 at NP >= 32.` **Verdict**: supports.

- **Citation**: `palace/linalg/nleps.cpp:700` — **Theme claim**: consume-then-reuse aliasing license, `// In-place writes into u, u2, A2n are safe: u/u2 were consumed into z above,`. **Found**: `:700-701` exactly that comment. **Verdict**: supports.

- **Citation**: `palace/linalg/nleps.cpp:637-647` — **Theme claim**: divergence-restart branch (`restart++` at `:645`, `break` at `:646`), near-singular recovery context. **Found**: `:636` `if (diverged_it > 10)`; `:645` `restart++;`; `:646` `break;`. The cited range `:637-647` is the branch body; the pinpointed sub-lines land. **Verdict**: supports (the `if`-opener is at `:636`, one above the cited range start, but the body and named sub-lines are correctly captured).

- **Citation**: `palace/linalg/nleps.cpp:606-619` — **Theme claim**: deflation-basis growth (normalize `:610-611`, store `X[k]=v` `:615`, `k++` `:619`), the variadic-in-`k` axis. **Found**: `:610` `const auto scale = linalg::Norml2(GetComm(), v);`, `:611` `v *= 1.0 / scale;`, `:615` `X[k] = v;`, `:619` `k++;`. All pinpointed sub-lines land. **Verdict**: supports (the range opens at `:606`, inside a `Mpi::Print` format string, but the range is in-bounds and the named sub-lines are exact).

- **Citation**: `palace/linalg/nleps.cpp:354-362` — **Theme claim**: deflation-scheme literature (Effenberger 2013; Jarlebring–Koskela–Mele 2018; SLEPc-NEP minimality index 1). **Found**: `:354-355` Jarlebring/Koskela/Mele 2018; `:356` "SLEPc's NEP solver with minimality index set to 1"; `:357-358` Effenberger 2013. **Verdict**: supports.

### Dot-convention corroboration

- **Citation**: `palace/linalg/vector.hpp:246` — **Theme claim**: `linalg::Dot(comm, x, y) = yᴴx`, the **second** C++ argument conjugated. **Found**: `:246` `// Calculate the parallel inner product yᴴ x or yᵀ x`. **Verdict**: supports. `--anchor 'inner product'` → 246.
- **Citation**: `palace/linalg/vector.cpp:674-685` — **Theme claim**: `LocalDot(const ComplexVector &x, const ComplexVector &y)` real/imag split corroborating which operand is conjugated. **Found**: `:674` `LocalDot(...)`. **Verdict**: supports. `--anchor 'LocalDot'` → 674.
- **Citation**: `book/src/L1/dot.md:43` — **Theme claim**: L1 `⟨x,y⟩=xᴴy` arg-1-conjugated convention; the L1 signature names the conjugated operand first. **Found**: `:43` "conjugate-linear in the **first** argument ... the L1 signature names the conjugated argument first." **Verdict**: supports — the framing reconciliation (C++ arg-2-conjugating ⇔ L1 arg-1-conjugated, both naming `w0`/`w2`) is sound.

### L1 operator-entry cross-references

- **Citation**: `book/src/L1/nleps_eigenvalue_correction.md:16-32` (signature), `:68` (Jacobian big-space-only / `[Xᴴ,0]` λ-independent), `:80` (law 3 Newton-ratio defining property), `:82` (law 4 coordinate-RHS independence), `:110` (over-unification guard vs deflated-solve), `:114` (firm-on-positive-structure Status).
  - **Found**: signature range `:16-32` in bounds; semantics point 4 (big-space-only) at `:68`; law 3 at `:80`, law 4 at `:82` (both exactly as the theme summarizes); over-unification guard at `:110`; Status `firm` (firm-on-positive-structure escape) at `:114`. All operator-entry pinpoints land.
  - **Verdict**: supports. The theme faithfully carries the operator entry's law 3, law 4, and big-space-only contract.

## Applicability conditions

The theme states six conditions. Each audited against the cited evidence:

1. **Condition**: the three inputs are bound exactly as for the per-step chain (`resid`←`:587`, `jac_action`←`:657`/`:668-669`, `proj_dir`←`:542-545`), consistent within one outer iteration.
   - **Verifiable**: yes, from the producer sites read above. `:587` writes `[u;u2]`, `:657`+`:668`+`:669` write the big-space `w`, `:542-545` produce normalized `[w0;w2]`. All three sit in the same `while (it < nleps_it)` iteration body (`:590` loop).
   - **Found counter-example?**: no.

2. **Condition**: element type is complex-only (`ComplexVector`/`Eigen::VectorXcd`).
   - **Verifiable**: yes — `u2_w0` is `std::complex<double>` (`:673`), `delta_eig` is `std::complex<double>` (`:674`), `z` is the `ComplexVector`, `z2` the `Eigen::VectorXcd`. No real specialization in the block.
   - **Found counter-example?**: no.

3. **Condition**: deflation cardinality `k` is variadic; `k=0` is the un-deflated degeneration (`u2`/`w2`/`z2` zero-length, `w2.adjoint()*u2=0`, `num=w0ᴴu`, `z2=[]`).
   - **Verifiable**: yes — `k` grows by one per converged pair (`:619` `k++`, within `:606-619`). The `:673` `w2.adjoint()*u2` is a uniform Eigen op that yields 0 for zero-length operands; `:677` `z2=-u2` is the empty vector when `u2` is empty. The block runs uniformly across `k`.
   - **Found counter-example?**: no.

4. **Condition**: in-place destination overwrite of `z`/`z2` is permitted (dead-on-entry scratch); consume-then-reuse of `u`/`u2` is licensed (`:700` comment); execution order δλ(`:673-675`)→z/z2(`:676-677`) is load-bearing (z reads the just-computed δλ).
   - **Verifiable**: yes — `:676`/`:677` overwrite `z`/`z2`; `:700` comment licenses the subsequent line-search overwrite of `u`/`u2` ("u/u2 were consumed into z above"); the straight-line ordering at `:673`→`:677` makes `:676` read `delta_eig` from `:674`.
   - **Found counter-example?**: no.

5. **Condition**: denominator `⟨[w0;w2],w⟩` is nonzero — partial function, undefined at the near-singular case (`:684-686`), recovered via Armijo + divergence-restart (`:637-647`); the undamped δλ does not commit `eig` (commit is `eig=eig_trial` for `α·δλ`, `:691`/`:708`).
   - **Verifiable**: yes — the denominator is the bare `Dot(w,w0)` at `:675` (division at `:674-675`); near-singular note at `:685`; recovery at `:637-647`; damping/commit at `:691`/`:708`.
   - **Found counter-example?**: no. (This is correctly recorded as a non-law, not asserted as a law.)

6. **Condition**: single-rank scope — `Mpi::GlobalSum` inside the big-space `linalg::Dot` (`:675`) lowers to a local no-op on one rank but carries the bit-deterministic-reduction-order trade-off (inherited from `dot-mutation-rotation`); the coordinate `w2.adjoint()*u2` (`:673`) and `z2=-u2` (`:677`) are rank-local.
   - **Verifiable**: yes, structurally — the two `linalg::Dot(GetComm(), ...)` calls at `:675` are the distributed (MPI-reducible) inner products; `:673` and `:677` are local Eigen ops. The reduction-order trade-off is inherited, not re-derived, from `dot-mutation-rotation`.
   - **Found counter-example?**: no (consistent with project scope: MPI single-rank).

## Algebraic laws (cited from the operator entry)

The theme carries (does not re-derive) the operator-entry laws. Audited for soundness on the operator signature:

- **Law (carried) — Newton-ratio defining property** (operator `:80`, theme §"The Newton-ratio defining property"): `⟨[w0;w2],[u;u2]⟩ + δλ·⟨[w0;w2],w⟩ = 0 ⟺ δλ = −num/den`.
  - **Holds on operators?**: yes. With `num = ⟨[w0;w2],[u;u2]⟩` and `den = ⟨[w0;w2],w⟩`, `num + δλ·den = 0` solves to `δλ = −num/den`, which is exactly the `:674-675` expression. Syntactic identity on the positive site. Sound.

- **Law (carried) — coordinate-RHS independence from δλ** (operator `:82` law 4, theme §"The big/coordinate RHS asymmetry"): `z2 = −u2` does not depend on δλ or `jac_action`; δλ couples into `z` only.
  - **Holds on operators?**: yes. `z2=-u2` (`:677`) has no `delta_eig`/`w` operand; `z=−δλ·w−u` (`:676`) does. The structural cause — the Jacobian action being big-space-only — is witnessed at `:657`/`:668`/`:669` (no `w2` write). The asymmetry is **correctly characterized as load-bearing** per the CLAUDE.md trick taxonomy (it is part of the algorithm: collapsing `z2` into a δλ-dependent form would invent a coordinate Jacobian-coupling Palace never computes). Sound.

- **Non-law (i) — well-definedness at `⟨[w0;w2],w⟩=0`**: the theme records δλ as a **partial** function, undefined when the denominator vanishes, with the source's own near-singular note (`:684-686`) and recovery (Armijo + divergence-restart `:637-647`). **Sound** — this is a genuine non-law (division by zero), correctly recorded rather than asserted as an identity; it does not require a test.

- **Non-law (ii) — undamped δλ does not commit `eig`**: the committed eigenvalue is `eig + α·δλ` (`:691`, commit `:708`), the line search's concern, not this atom's. **Sound** — the atom produces the undamped δλ; the damping/commit is correctly placed in the orchestration, not the atom. Recorded as a non-law, no test required.

Both non-laws are sound and correctly scoped. The firm-on-positive-structure status decision is justified: every constituent is a syntactic identity on fully-specified positive source, so the absent NLEPS unit test (`QuasiNewton|nleps|funcA2|delta_eig` → zero `test/unit/**` hits, re-confirmed below) does not gate the firm decision — the same escape used by the `apply_nonlinear_pencil` / `nleps_deflated_residual` / `nleps_deflated_solve` siblings.

## Proposed changes

Audit verdict is **fully-supported**; no contradiction found, so the only proposed change is the
additive `verified_against:` metadata block (consumed by `cross-layer-cross-cutter`). The theme body
is **not** mutated.

```edit:book/src/L1-L0/nleps-eigenvalue-correction-mutation-rotation.md
[append at end of file]
~~~yaml
verified_against:
  - citation: palace/linalg/nleps.cpp:672
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: source comment names the operator; --anchor lands at 672
  - citation: palace/linalg/nleps.cpp:673
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "Sub-pattern A coordinate dot w2ᴴu2 (w2.adjoint()*u2); --anchor → 673"
  - citation: palace/linalg/nleps.cpp:674-675
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "Sub-pattern A ratio δλ=−num/den; num=w0ᴴu+w2ᴴu2, den=w0ᴴw; --anchor delta_eig→674, Dot(w,w0)→675"
  - citation: palace/linalg/nleps.cpp:676
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "Sub-pattern B axpby via AXPBYPCZ γ=0 (z=−δλ·w−u); --anchor → 676"
  - citation: palace/linalg/nleps.cpp:677
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "Sub-pattern C scal α=−1 (z2=−u2); --anchor → 677"
  - citation: palace/linalg/nleps.cpp:657
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "big/coordinate asymmetry — Jacobian action big-space-only (opJ->Mult(v,w)); :668/:669 AddMult also into w only, no w2 write"
  - citation: palace/linalg/nleps.cpp:587
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "resid producer (compute_residual writes [u;u2])"
  - citation: palace/linalg/nleps.cpp:542-545
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "proj_dir [w0;w2] = normalized deflated solve T(σ)⁻¹c"
  - citation: palace/linalg/nleps.cpp:682
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "consumer — deflated_solve(z,z2,du,du2) inverts this atom's RHS"
  - citation: palace/linalg/nleps.cpp:684-686
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "non-law (i) near-singularity <w0,w> — sound, recorded as partial function"
  - citation: palace/linalg/nleps.cpp:691
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "non-law (ii) undamped δλ — eig_trial = eig + alpha*delta_eig"
  - citation: palace/linalg/nleps.cpp:704-708
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "Armijo test + commit eig=eig_trial at :708"
  - citation: palace/linalg/nleps.cpp:712
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "Armijo backtrack-factor update (theme correctly uses :712, not the operator-entry :709 drift)"
  - citation: palace/linalg/nleps.cpp:637-647
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "divergence-restart recovery context for non-law (i)"
  - citation: palace/linalg/nleps.cpp:606-619
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "variadic-in-k deflation growth (k++ at :619)"
  - citation: palace/linalg/nleps.cpp:354-362
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "deflation-scheme literature (Jarlebring 2018, Effenberger 2013, SLEPc minimality index 1)"
  - citation: palace/linalg/vector.hpp:246
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "Dot(comm,x,y)=yᴴx convention (arg-2 conjugated)"
  - citation: palace/linalg/vector.cpp:674-685
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "LocalDot real/imag split corroborates conjugation"
  - citation: book/src/L1/dot.md:43
    verdict: supports
    audited_at: 2026-05-29T16:47:49Z
    note: "L1 arg-1-conjugated convention reconciles with C++ arg-2 form; both name projection direction"
~~~
```

(The inner `~~~yaml ... ~~~` tilde-fenced block is the actual block to append to the theme file. No body
sections are flipped or rewritten — the theme is already `firm` and the audit confirms it; this is a
metadata-only addition.)

## Supporting evidence

Source / cross-reference files consulted (all absolute paths):

- `/home/crutcher/git/palace_whiteroom/reference/palace/palace/linalg/nleps.cpp` — primary L0 site (read `:538-549`, `:585-596`, `:604-647`, `:650-717`, `:683-687`, `:352-363`) + `citecheck --anchor` on the five primary lines and 9 context lines.
- `/home/crutcher/git/palace_whiteroom/reference/palace/palace/linalg/vector.hpp` (`:246`) and `vector.cpp` (`:674`) — dot-convention corroboration via `citecheck --anchor`.
- `/home/crutcher/git/palace_whiteroom/book/src/L1/nleps_eigenvalue_correction.md` — read `:60-114` (semantics points, laws, dependencies, variant axes, Status); confirmed `:16-32`, `:68`, `:80`, `:82`, `:110`, `:114` land.
- `/home/crutcher/git/palace_whiteroom/book/src/L1/dot.md:43` — arg-1 conjugation convention.
- Sibling/leaf theme + operator files confirmed on disk: `nleps-jacobian-action-mutation-rotation.md`, `nleps-deflated-solve-mutation-rotation.md`, `nleps-deflated-residual-mutation-rotation.md`, `apply-nonlinear-pencil-mutation-rotation.md`, `dot-mutation-rotation.md`, `axpbypcz-mutation-rotation.md`, `scal-mutation-rotation.md`; L1 leaves `dot.md`, `axpby.md`, `scal.md`, `axpbypcz.md`.
- `tools/citecheck/citecheck.py --scan` over the theme: **31 ok, 0 failing**.
- NLEPS test-coverage absence re-confirmed in the role of the firm-decision gate check (see Open questions).

## Open questions / caveats

- **Carry-forward (inherited operator-entry drifts, NOT theme defects)** — the theme itself already
  flags two minor drifts in the L1 operator entry `book/src/L1/nleps_eigenvalue_correction.md` and
  routes around them with corrected on-disk numbers: (1) the `while (it < nleps_it)` loop, cited in
  the operator entry as `:596`, is on-disk **`:590`** (−6); (2) the Armijo α update, referenced in
  the operator entry's semantics point 5 (`:70`) and collapsed-axes (`:108`) as `:709`, is on-disk
  **`:712`** (`:709` is `res = res_trial`). The theme's `:712` is correct. These are operator-entry
  citation drifts for the eventual `lifter` / harvester re-anchor pass on
  `book/src/L1/nleps_eigenvalue_correction.md`; they do not affect any anchor this theme asserts as
  verified. Routed as a carry-forward (operator-entry, not theme).
- **Codemap +1 drift** — re-confirmed the theme's claim: the `:672-677` primary block lands exactly
  on-disk (`citecheck --anchor` clean on all five lines); the wave-1-discovered codemap +1 drift is
  confined to the earlier deflation block `:659+`, which precedes this site. No correction needed.
- **NLEPS test-coverage absence** — re-confirmed there is no dedicated `test/unit/**` exercise of the
  QuasiNewton NEP loop (consistent with the eigsolve / pencil / residual / solve / jacobian-action
  siblings). The firm decision correctly rests on exhaustive positive structural citation +
  explicit non-laws (the firm-on-positive-structure escape), not on a test. This is recorded as the
  standing NEP-interior test gap, not a blocker for this theme.
- **Minor range-opener observations (non-blocking)** — two cited ranges open one line "early"
  relative to the named anchor: `:637-647` opens at `:637` while the `if (diverged_it > 10)` opener
  is at `:636` (the body and named sub-lines `:645`/`:646` land); `:606-619` opens at `:606` which is
  inside a `Mpi::Print` format string (the named sub-lines `:610-611`/`:615`/`:619` land). Both
  ranges are in-bounds and capture the intended content; recorded for completeness, no change
  recommended.
