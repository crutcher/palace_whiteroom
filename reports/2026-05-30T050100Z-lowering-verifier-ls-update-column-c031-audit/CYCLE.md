---
agent: lowering-verifier
invoked_at: 2026-05-30T050100Z
scope: L1>L0 theme audit — ls-update-column-mutation-rotation (c031 additive verified_against)
status: pending
inputs:
  - book/src/L1-L0/ls-update-column-mutation-rotation.md (firm, landed cycle-030)
  - palace/linalg/iterative.cpp (GMRES/FGMRES Givens stream + 4-call body + scalar kernels + shared-register hpp shapes)
  - palace/linalg/iterative.hpp (H/s/sn/cs register declarations + FgmresSolver inheritance + Z register)
  - book/src/L1/ls-update-column.md (firm L1 leaf + cycle-029 verified_against)
  - book/src/L1-L0/back-solve-mutation-rotation.md (firm sibling, GMRES-restart cohort terminal consumer)
  - book/src/L2/incremental-least-squares.md (firm L2 composition; replay-non-commutativity grounding)
  - book/src/L2-L1/incremental-least-squares-composition-lowering.md (firm L2>L1; Face-1 opaque-leaf wire)
  - tools/citecheck/citecheck.py --anchor (mechanical citation source-of-truth)
integrated_at: 2026-05-30T051734Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied clean (cycle-031 D1). Additive 33-row verified_against block (all supports) appended to ls-update-column-mutation-rotation.md. Theme stays firm — c030-landed firm theme UPHELD. Closes c030 follow-up OQ ls-update-column-mutation-rotation-cycle-031-verified-against-audit-c030 — audit IS the resolution. Standard firm-theme additive audit cadence (precedent: back-solve-mutation-rotation c030 / normalize-mutation-rotation c028).
---

# CYCLE: Audit ls-update-column-mutation-rotation (c031)

## Summary

Additive `verified_against:` audit of the firm L1>L0 theme
`book/src/L1-L0/ls-update-column-mutation-rotation.md` (landed firm cycle-030).
Standard sibling-follow-up to the c030 cohort closure
(`back-solve-mutation-rotation` 22-row block c030,
`normalize-mutation-rotation` c028, `back_solve` c028). Verdict
**fully-supported**: 33 of 33 cited Palace source ranges land zero-drift
on-disk via `tools/citecheck/citecheck.py --anchor`. All cross-anchor link
targets exist on disk. The c030 cross-confirmed fact that GMRES
`iterative.cpp:634-640` and FGMRES `:813-819` are byte-identical (with a +5
preceding-code line offset, NOT a brace-placement shift) is mechanically
reconfirmed this invocation by literal-anchor match on the same text at both
sites (5 line pairs: `634≡813, 636≡815, 638≡817, 639≡818, 640≡819`). No
contradictions, no drifted citations, no scope/audit gaps surfaced. The
theme's status stays `firm`; this audit is **additive** (append a new
`verified_against:` block at end of file; do NOT rewrite the theme body).

## Per-citation audit

All 33 rows below confirmed via `python3 tools/citecheck/citecheck.py
<path:lo-hi> --anchor '<token>'` against on-disk `reference/palace/`. Every
row is `[ok]` zero-drift. The audit also re-read each Citations block in the
theme prose (theme `:198-237` Sub-pattern A Citations; `:288-308` Sub-pattern
B Citations; `:621-697` §Verified-against) plus the additional in-prose
anchors in §"Applicability conditions" and §"machinery" sections; every
distinct citation pointer is covered by the verified_against block below.

| # | Citation | Theme-claim | citecheck verdict |
|---|----------|-------------|-------------------|
| 1 | `iterative.cpp:634` | GMRES strict-order replay-loop header | ok (anchor at 634) |
| 2 | `iterative.cpp:636` | GMRES replay body `ApplyPlaneRotation(Hj[k]...)` | ok (anchor at 636) |
| 3 | `iterative.cpp:638` | GMRES generate-into-registers | ok (anchor at 638) |
| 4 | `iterative.cpp:639` | GMRES column-apply (law-1 sub-diag annihilation) | ok (anchor at 639) |
| 5 | `iterative.cpp:640` | GMRES RHS-apply (law-3 residual exposure) | ok (anchor at 640) |
| 6 | `iterative.cpp:642` | downstream convergence-test residual read | ok (anchor at 642) |
| 7 | `iterative.cpp:629-632` | upstream Hj setup + orthogonalize + Norml2 boundary | ok (Hj=H.data anchor at 629) |
| 8 | `iterative.cpp:73-108` | GeneratePlaneRotation real (LAPACK-scaled) | ok (anchor at 73) |
| 9 | `iterative.cpp:101-108` | overflow/underflow scaling else-branch | ok (safmin anchor at 102) |
| 10 | `iterative.cpp:112-118` | GeneratePlaneRotation complex + unitarity comment | ok (anchor at 112) |
| 11 | `iterative.cpp:118` | in-comment unitarity contract `cs²+|sn|²=1` | ok (anchor at 118) |
| 12 | `iterative.cpp:227-241` | ApplyPlaneRotation real + complex kernel pair | ok (anchors at 227, 235) |
| 13 | `iterative.cpp:227` | ApplyPlaneRotation real-variant signature | ok (anchor at 227) |
| 14 | `iterative.cpp:235` | ApplyPlaneRotation complex-variant signature | ok (anchor at 235) |
| 15 | `iterative.cpp:612` | restart-cycle seed `s[0] = beta` | ok (anchor at 612) |
| 16 | `iterative.cpp:611` | restart-cycle zero-fill `std::fill(s, 0.0)` | ok (anchor at 611) |
| 17 | `iterative.cpp:615` | GMRES outer iteration loop header | ok (anchor at 615) |
| 18 | `iterative.cpp:631` | Norml2 producing h_new[j+1] (upstream boundary) | ok (anchor at 631) |
| 19 | `iterative.cpp:644-645` | convergence test + restart-cycle exit guard | ok (anchors at 644, 645) |
| 20 | `iterative.cpp:666` | GMRES basis-lift `x.Add(s[k], V[k])` (downstream boundary) | ok (anchor at 666) |
| 21 | `iterative.cpp:843` | FGMRES basis-lift `x.Add(s[k], Z[k])` (downstream boundary) | ok (anchor at 843) |
| 22 | `iterative.cpp:652-660` | terminal back-solve range (sibling-theme entry point) | ok (Reconstruct anchor at 652) |
| 23 | `iterative.hpp:192` | flat Hessenberg slab `mutable std::vector<ScalarType> H` | ok (anchor at 192) |
| 24 | `iterative.hpp:193` | `mutable std::vector<ScalarType> s, sn` | ok (anchor at 193) |
| 25 | `iterative.hpp:194` | `mutable std::vector<RealType> cs` (cs:Real) | ok (anchor at 194) |
| 26 | `iterative.cpp:813` | FGMRES replay-loop header (byte-identical to :634) | ok (anchor at 813; literal-text identical to :634) |
| 27 | `iterative.cpp:815` | FGMRES replay body (byte-identical to :636) | ok (anchor at 815) |
| 28 | `iterative.cpp:817` | FGMRES generate-into-registers (byte-identical to :638) | ok (anchor at 817) |
| 29 | `iterative.cpp:818` | FGMRES column-apply (byte-identical to :639) | ok (anchor at 818) |
| 30 | `iterative.cpp:819` | FGMRES RHS-apply (byte-identical to :640) | ok (anchor at 819) |
| 31 | `iterative.hpp:222` | FGMRES class declaration (public inheritance from GmresSolver) | ok (FgmresSolver anchor at 222) |
| 32 | `iterative.hpp:250` | `using GmresSolver<OperType>::H` | ok (anchor at 250) |
| 33 | `iterative.hpp:256` | FGMRES Z register `mutable std::vector<VecType> Z` | ok (anchor at 256) |

Net: 33 supports, 0 partially-supports, 0 does-not-support, 0 out-of-range.

## Byte-identical GMRES≡FGMRES re-confirmation (the c030 cross-confirmed fact)

The theme narrates the GMRES `:634-640` vs FGMRES `:813-819` byte-identical
recognition (and explicitly corrects the c030-audited error in the sibling
`back-solve-mutation-rotation` theme that mis-attributed a +1 line shift to
brace placement). This audit mechanically reconfirms the byte-identity by
literal-anchor match on the same five token strings at both sites:

| line pair | text (anchor token) | citecheck verdict |
|-----------|---------------------|-------------------|
| `:634 ≡ :813` | `for (int k = 0; k < j; k++)` | both ok with same literal anchor |
| `:636 ≡ :815` | `ApplyPlaneRotation(Hj[k]` | both ok with same literal anchor |
| `:638 ≡ :817` | `GeneratePlaneRotation(Hj[j]` | both ok with same literal anchor |
| `:639 ≡ :818` | `ApplyPlaneRotation(Hj[j]` | both ok with same literal anchor |
| `:640 ≡ :819` | `ApplyPlaneRotation(s[j]` | both ok with same literal anchor |

The +5 line offset is from preceding code differences (the FGMRES
right-preconditioner build `Z[k] = M⁻¹ V[k]` before the orthogonalize step),
NOT brace placement — exactly as the theme states at `:254-262`. The
theme's correction of the c030 sibling-theme error stands.

## Applicability conditions

The theme states 7 applicability conditions at `:467-526`. Each is mapped to
its cited anchor and verified.

| # | Condition (paraphrased) | Anchor | Verified |
|---|--------------------------|--------|----------|
| 1 | No observer reads prior `Hj[0..j+1]` after the call | (structural — leaf-internal) | yes (in-place overwrite is per-call local; downstream back-solve at `:652-660` consumes only the post-leaf triangularised column) |
| 2 | No observer reads prior `cs[j]/sn[j]` before the call | (structural — slot-`j` uninitialised) | yes (generate-into-registers at `:638` reads only the column pair `(Hj[j], Hj[j+1])`, not the register slots) |
| 3 | `s[j+1] = 0` on entry | `:611` zero-fill + `:612` seed + per-call advance | yes (anchors verified; the running-RHS invariant — populated prefix s[0..j] + zero tail) |
| 4 | Non-degenerate `(Hj[j], Hj[j+1])` after replay (lucky-breakdown boundary) | `:644` convergence test | yes (the test exits *before* the next outer iteration; the leaf does NOT guard) |
| 5 | Registers `cs, sn, s, H` redundant-on-all-ranks | (in-scope single-machine; automatic) | yes (CLAUDE.md §Scope; the upstream orthogonalize + nrm2 produce identical h_new on every rank) |
| 6 | Element type `ScalarType` matches across `cs/sn/s/Hj` | `iterative.hpp:192-194` | yes (template-instantiation binding; the four `*PlaneRotation` calls dispatch uniformly) |
| 7 | `0 <= j < max_dim` (active column-index bounds) | `:615` outer loop + `:645` exit | yes (the exit `if (... || j+1 == max_dim || ...) break;` terminates one short of overflow; the leaf is NOT invoked at `j = max_dim`) |

Found counter-example? None.

## Algebraic laws (the L1 leaf laws this theme realises)

The theme rests on the L1 leaf's 7 laws (theme `:62-73`; L1 leaf
`book/src/L1/ls-update-column.md:252-318`). Each is mapped to its anchor.

| # | Law | Anchor (per theme) | Holds on L0 source? |
|---|-----|---------------------|----------------------|
| 1 | sub-diagonal annihilation `h_out[j+1] = 0` exactly | `:639` (column-apply) + generate-apply pair contract | yes (definitional — the generate kernel pins (cs, sn) such that subsequent apply zeros the y-component; verified at scalar-kernel `:73-108` / `:112-118`) |
| 2 | replay non-commutativity (load-bearing structural law) | `:634, :636` (ascending k = 0..j-1) | yes (the loop variable is `k++`, the call overwrites the pair in place before the next read; pinned in-source) |
| 3 | residual exposure `beta = |s_jp1|` | `:640` (RHS-apply) + `:642` (read) | yes (the apply with s[j+1] = 0 on entry concentrates s[j+1] = -conj(sn) * s[j] = -|sn|*|s[j]|; the convergence test at :642 reads it as beta) |
| 4 | unitarity preservation `cs² + |sn|² = 1` | `:118` in-comment contract | yes (the LAPACK-scaled generate kernel's defining property; the in-comment contract underwrites it; cs:RealType at `iterative.hpp:194` is the type-shape side of the same constraint) |
| 5 | empty-replay boundary (j = 0): no replay sub-step | `:634` (loop body does not execute when j=0) | yes (the `k < j` test is false for k=0 when j=0; the loop body is skipped; generate ▷ apply ▷ apply_rhs is the only sub-call sequence) |
| 6 | basis-lift independence (GMRES ≡ FGMRES at this leaf) | `:634-640` ≡ `:813-819` byte-identical + `:666` vs `:843` downstream-only basis differ | yes (byte-identical bodies confirmed by direct literal-anchor cross-match; the basis-lift `V` vs `Z` happens at `:666` / `:843` post-leaf in the L2 composition, not in the leaf body) |
| 7 | per-call scalar-kernel-variant invariance (real/complex) | `iterative.hpp:193-194` + `iterative.cpp:73, :112, :227, :235` | yes (the variant is bound at template instantiation; the four `*PlaneRotation` calls dispatch uniformly to the matching scalar kernel; no per-call branching) |

All 7 laws hold on the cited L0 source as the theme states. No
algebraic-law contradictions surfaced.

## Proposed changes

Append the additive `verified_against:` block (33 rows, all `supports`) at
the end of the theme file. The theme body is NOT rewritten — this is a
standard additive sibling-follow-up audit per the c030 cohort precedent.

```edit:book/src/L1-L0/ls-update-column-mutation-rotation.md
[append at end of file]
```yaml
verified_against:
  - citation: palace/linalg/iterative.cpp:634
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: GMRES strict-order replay-loop header for (int k = 0; k < j; k++) — citecheck --anchor zero-drift on-disk.
  - citation: palace/linalg/iterative.cpp:636
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: GMRES replay sub-step body ApplyPlaneRotation(Hj[k], Hj[k+1], cs[k], sn[k]) — citecheck zero-drift.
  - citation: palace/linalg/iterative.cpp:638
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: GMRES generate-into-registers GeneratePlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j]) — citecheck zero-drift; writes cs[j], sn[j] by reference.
  - citation: palace/linalg/iterative.cpp:639
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: GMRES column-apply ApplyPlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j]) — citecheck zero-drift; post-condition Hj[j+1] = 0 by generate-apply pair contract (law 1).
  - citation: palace/linalg/iterative.cpp:640
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: GMRES RHS-apply ApplyPlaneRotation(s[j], s[j+1], cs[j], sn[j]) — citecheck zero-drift; residual concentrated into s[j+1] (law 3).
  - citation: palace/linalg/iterative.cpp:642
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: convergence-test residual read beta = std::abs(s[j+1]) — citecheck zero-drift; downstream boundary marker for the law-3 byproduct, NOT part of the leaf body.
  - citation: palace/linalg/iterative.cpp:629-632
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: upstream Hj = H.data() + j*(max_dim+1) at :629 + OrthogonalizeIteration at :630 + Hj[j+1] = Norml2 at :631 + w-normalize at :632 — citecheck --anchor 'Hj = H.data' lands at 629 within range; upstream orthogonalize + nrm2 boundary marker, NOT part of the leaf.
  - citation: palace/linalg/iterative.cpp:73-108
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: GeneratePlaneRotation real scalar kernel — citecheck --anchor 'GeneratePlaneRotation' lands at 73; LAPACK-scaled rotation generator with overflow/underflow scaling at :101-108 (the safmin/safmax branch).
  - citation: palace/linalg/iterative.cpp:101-108
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: overflow/underflow scaling branch (the else clause guarding non-finite intermediates) — citecheck --anchor 'safmin' lands at 102 within range; pinned finite-precision composition path for the load-bearing-numerical replay chain.
  - citation: palace/linalg/iterative.cpp:112-118
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: GeneratePlaneRotation complex scalar kernel — citecheck --anchor 'GeneratePlaneRotation' lands at 112 within range; signature with cs as RealType + sn as complex<T> at :112-113, in-comment unitarity contract cs is real and cs² + |sn|² = 1 at :118.
  - citation: palace/linalg/iterative.cpp:118
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: in-comment unitarity contract cs is real and cs² + |sn|² = 1 — citecheck zero-drift; underwrites law 4 (unitarity preservation).
  - citation: palace/linalg/iterative.cpp:227-241
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: ApplyPlaneRotation real :227 + complex :235 — citecheck --anchor 'ApplyPlaneRotation' lands at both 227 and 235 within range; the in-place 2-vector update kernel called at the replay loop, column-apply, and RHS-apply; complex variant uses conj(sn) at :239.
  - citation: palace/linalg/iterative.cpp:227
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: ApplyPlaneRotation real-variant scalar kernel signature inline void ApplyPlaneRotation(T &dx, T &dy, const T cs, const T sn) — citecheck zero-drift.
  - citation: palace/linalg/iterative.cpp:235
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: ApplyPlaneRotation complex-variant scalar kernel signature inline void ApplyPlaneRotation(std::complex<T> &dx, std::complex<T> &dy, const T cs, ...) — citecheck zero-drift.
  - citation: palace/linalg/iterative.cpp:612
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: restart-cycle RHS seed s[0] = beta; — citecheck zero-drift; boundary marker establishing s[j+1] = 0 on entry (the applicability-condition 3 invariant for residual-into-tail).
  - citation: palace/linalg/iterative.cpp:611
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: restart-cycle RHS zero-fill std::fill(s.begin(), s.end(), 0.0) — citecheck zero-drift; the upstream zeroing companion to :612 establishing the running-RHS invariant.
  - citation: palace/linalg/iterative.cpp:615
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: GMRES outer iteration loop header for (;; j++, it++) — citecheck zero-drift; the unbounded outer iteration that drives this leaf's repeated invocation at columns j = 0, 1, ... max_dim - 1.
  - citation: palace/linalg/iterative.cpp:631
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: upstream Hj[j+1] = linalg::Norml2(comm, w) — citecheck zero-drift; the nrm2 producer of h_new[j+1] (the orthogonalisation residual) — boundary marker NOT part of this leaf.
  - citation: palace/linalg/iterative.cpp:644-645
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: convergence test converged = (beta < eps) at :644 + restart-cycle exit if (converged || j+1 == max_dim || it+1 == max_it) at :645 — citecheck --anchor 'converged' lands at both lines within range; the upstream-absorbed degenerate-input / restart-boundary guard cited in applicability conditions 4 and 7.
  - citation: palace/linalg/iterative.cpp:666
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: GMRES basis-lift x.Add(s[k], V[k]) — citecheck zero-drift; the downstream consumer of the rotated RHS s[0..j] reading the Arnoldi basis V (basis-lift boundary marker for law-6 narrative).
  - citation: palace/linalg/iterative.cpp:843
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: FGMRES basis-lift x.Add(s[k], Z[k]) — citecheck zero-drift; the downstream consumer reading the right-preconditioned basis Z; pairs with GMRES :666 to ground law-6 basis-lift independence.
  - citation: palace/linalg/iterative.cpp:652-660
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: terminal back-solve range with "Reconstruct the solution" comment at :652 + descending for (int i = j; i >= 0; i--) at :653 + per-column-handle Hi = H.data() + i*(max_dim+1) at :655 + s[i] /= Hi[i] at :656 + inner eager-subtraction s[k] -= Hi[k]*s[i] at :659 — citecheck --anchor 'Reconstruct' lands at 652 within range; the downstream back-solve sibling theme entry point (NOT part of this leaf).
  - citation: palace/linalg/iterative.hpp:192
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: flat Hessenberg slab declaration mutable std::vector<ScalarType> H — citecheck zero-drift; underwrites the flat column-major storage trick + the Hj = H.data() + j*(max_dim+1) stride pointer.
  - citation: palace/linalg/iterative.hpp:193
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: RHS + sine registers mutable std::vector<ScalarType> s, sn — citecheck zero-drift; the element-type binding for s and sn (ScalarType, complex in the complex variant); underwrites law 7 (per-call scalar-kernel-variant invariance).
  - citation: palace/linalg/iterative.hpp:194
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: cosine register mutable std::vector<RealType> cs — citecheck zero-drift; cs always RealType (the law-4 cs² + |sn|² = 1 contract relies on cs being real).
  - citation: palace/linalg/iterative.cpp:813
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: FGMRES replay-loop header for (int k = 0; k < j; k++) — citecheck zero-drift; byte-identical to GMRES :634 (confirmed by literal-anchor match on the same text); the +5 line offset is from preceding FGMRES code, NOT brace placement.
  - citation: palace/linalg/iterative.cpp:815
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: FGMRES replay sub-step ApplyPlaneRotation(Hj[k], Hj[k+1], cs[k], sn[k]) — citecheck zero-drift; byte-identical to GMRES :636.
  - citation: palace/linalg/iterative.cpp:817
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: FGMRES generate-into-registers GeneratePlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j]) — citecheck zero-drift; byte-identical to GMRES :638.
  - citation: palace/linalg/iterative.cpp:818
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: FGMRES column-apply ApplyPlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j]) — citecheck zero-drift; byte-identical to GMRES :639.
  - citation: palace/linalg/iterative.cpp:819
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: FGMRES RHS-apply ApplyPlaneRotation(s[j], s[j+1], cs[j], sn[j]) — citecheck zero-drift; byte-identical to GMRES :640; the four-call sub-pattern B sequence cross-confirmed byte-identical to A.
  - citation: palace/linalg/iterative.hpp:222
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: FGMRES class declaration (FgmresSolver derives publicly from GmresSolver<OperType>) — citecheck zero-drift; the public-inheritance binding underwriting law-6 basis-lift independence + the shared-register chassis at :250.
  - citation: palace/linalg/iterative.hpp:250
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: FGMRES using-declaration using GmresSolver<OperType>::H — citecheck zero-drift; inherits the flat H slab from GmresSolver (the same register the four-call body indexes via Hj).
  - citation: palace/linalg/iterative.hpp:256
    verdict: supports
    audited_at: 2026-05-30T050100Z
    note: FGMRES Z register declaration mutable std::vector<VecType> Z — citecheck zero-drift; the FGMRES-specific right-preconditioned basis register (Z[k] = M⁻¹ V[k]); the basis-lift independence boundary marker (this leaf does NOT read Z).
```
```

YAML self-check: `python3 -c "import yaml; yaml.safe_load(open(<extracted-block>))"` returns 33 rows parsed clean (no `mapping values are not allowed here` / `ScannerError`); no `note:` value begins with `'` or `"` (verified via the leading-quote lint per friction-ledger `verified-against-note-no-leading-quote-of-either-kind`). The block is fenced as ` ```yaml ... ``` ` per the channel-format invariant.

## Supporting evidence

Files consulted (all absolute):
- `/home/crutcher/git/palace_whiteroom/book/src/L1-L0/ls-update-column-mutation-rotation.md` — the audited theme.
- `/home/crutcher/git/palace_whiteroom/reference/palace/palace/linalg/iterative.cpp` — every cited line range verified via `tools/citecheck/citecheck.py --anchor`; 33 distinct anchor probes, all `[ok]` zero-drift.
- `/home/crutcher/git/palace_whiteroom/reference/palace/palace/linalg/iterative.hpp` — register-shape declarations at `:192, :193, :194` (H/s/sn/cs) + FGMRES inheritance at `:222, :250, :256` (FgmresSolver/H/Z).
- `/home/crutcher/git/palace_whiteroom/book/src/L1/ls-update-column.md` — L1 leaf cross-anchors: Signature `:80-115`, the four-sub-step semantics `:75-78`, Algebraic laws `:251-318`, Dependencies `:356-417`, Status `:457-503`, L1 vs L0 distinction `:505+`, cycle-029 verified_against `:631-716` (the leaf's own audit block) — all sections present on-disk at the cited ranges.
- `/home/crutcher/git/palace_whiteroom/book/src/L1-L0/back-solve-mutation-rotation.md` — sibling theme exists; theme prose at `:24-27` notes it is the column-streaming sibling; sibling's c030 audited Sub-pattern B mis-attribution is acknowledged explicitly in this theme at `:259-262` (no theme-body fix needed here — the correction lives in this theme's narrative).
- `/home/crutcher/git/palace_whiteroom/book/src/L1-L0/orthogonalize-mutation-rotation.md` — upstream-boundary sibling exists.
- `/home/crutcher/git/palace_whiteroom/book/src/L1-L0/nrm2-mutation-rotation.md` — upstream-boundary sibling exists.
- `/home/crutcher/git/palace_whiteroom/book/src/L2/incremental-least-squares.md` — replay-non-commutativity grounding at `:275-285` confirmed (theme cites `:278-285`; the load-bearing-numerical bullet is in fact `:278-285`, off-by-zero).
- `/home/crutcher/git/palace_whiteroom/book/src/L2-L1/incremental-least-squares-composition-lowering.md` — Face-1 wire exists; this theme is its opaque-leaf face.
- `/home/crutcher/git/palace_whiteroom/book/src/concepts/givens_generate.md`, `/home/crutcher/git/palace_whiteroom/book/src/concepts/givens_apply.md`, `/home/crutcher/git/palace_whiteroom/book/src/concepts/plane-rotation-stream.md` — all exist; concept-page `plane-rotation-stream.md:21-23` confirmed (sequential-character forward note).

Mechanical-tool runs (`tools/citecheck/citecheck.py --anchor` invocations
this invocation, all returning `[ok]` zero-drift): see §"Per-citation
audit" table — 33 distinct anchor probes. Two probes ran with `--regex`
syntax (`'s\[0\] = beta'`, `'for (int k = 0; k < j; k\+\+)'`); the latter
returned `[NOANC]` because of regex special-character escape interaction
with the underlying anchor matcher, but the same anchor as a literal text
match (`--anchor 'for (int k = 0; k < j; k++)'`) returned `[ok]` at line 634
zero-drift. No on-disk drift surfaced.

## Open questions / caveats

None substantive — the audit is fully-supported with 33 of 33 supports.

Two narrow observations recorded for completeness, neither requiring action:

1. **L1 leaf §Algebraic-laws range fencepost** — the theme cites the L1 leaf
   §Algebraic-laws as `:252-318`. On disk the `## Algebraic laws` heading is
   at `:251` with the lead-in prose at `:253` and laws running `:255-317`
   (law 7 ends at `:317-318`; the "Laws that explicitly **do not** hold"
   sub-section starts at `:320`). The cited range is one-line-off-by-one on
   the START (citing `:252` for content that begins at `:251` heading / `:253`
   prose), but the END (`:317-318`) is correct. This is an inclusive-fencepost
   off-by-one of MINIMAL load-bearing impact (the cited content all falls
   within the cited range; no drifted claim). Recording but NOT flagging for
   theme-body edit — the citation is **substantively correct**, the
   convention "cite the section heading line" would push the start to `:251`,
   the convention "cite the first content line" would push the start to
   `:253`. The theme's `:252` is a reasonable midpoint and supports the
   claim.

2. **L1 leaf §"L1 vs L0 distinction" END not directly verified** — the theme
   cites `:505-531`; the `## L1 vs L0 distinction` heading is at `:505`
   (confirmed); the file extends past `:531` (the verified_against blocks at
   `:629-716` and beyond), so the `:531` end is a partial-section bound, NOT
   a section-end. This is acceptable (the cited range is `## L1 vs L0
   distinction` content as far as `:531`); recording but NOT flagging.

These are not citation drifts; both anchors land within the cited ranges
and support the theme's claims. No follow-up dispatch action needed.

The theme's status stays `firm` (no promotion gate, no demotion). The
GMRES-restart-cycle L1>L0 cohort end-to-end firm status declared in the
c030 finalize commit (`f0a8f50`/`21dedc3`) — `ls_update_column` (per-column
producer) + `back_solve` (terminal consumer) — stands.

This audit is the standard cycle-031 sibling-follow-up to the c030 cohort
landing; no methodology adjustments surfaced.
