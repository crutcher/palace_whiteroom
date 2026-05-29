---
agent: lowering-verifier
invoked_at: 2026-05-29T194558Z
scope: L1 firm leaf audit — back_solve (GMRES/FGMRES restart-correction back-solve; landed firm cycle-027 dispatch-4, renamed-in-repair from ls_update_column)
status: integrated
integrated_at: 2026-05-29T205500Z
integration_commit: 3319d88
integration_notes: "cycle-028 position 4/7 (per-report). Additive verified_against: audit of the firm L1 leaf back_solve (landed firm c027 D4). Verdict fully-supported, UPHELD firm, no status change — 18-row yaml block, all supports. Firm-on-positive-structure (syntactic-identity laws; no-dedicated-test non-gating per lu_solve/apply_linop precedent; descending column-oriented back-substitution reduction-order recorded as a non-law, not a status reduction). §Status untouched. Build clean (yaml fence balanced, zero build-repairs)."
inputs:
  - book/src/L1/back_solve.md (the firm L1 leaf under audit)
  - palace/linalg/iterative.cpp:652-660 (GMRES restart-correction back-solve) / :831-840 (FGMRES twin) — the cited L0 source
  - palace/linalg/iterative.cpp:612,631,642,644 (running-QR context anchors)
  - palace/linalg/iterative.hpp:193-194 (register element-type declarations)
  - book/src/L2/incremental-least-squares.md:81-83,:225-232,:278-285 (parent L2 composition cross-refs)
  - book/src/concepts/givens.md:29 (the "back_solve via trsv" concept anchor)
  - reports/2026-05-29T175529Z-harvester-ls-update-column-l1/CYCLE.md + META.md (harvester report + critic/repairer rename history)
---

# CYCLE: Audit back_solve

## Summary

I audited the firm L1 leaf `back_solve` (`book/src/L1/back_solve.md`) — the
GMRES/FGMRES restart-correction back-substitution, `y = back_solve(R, s)` solving
the small-dense Givens-rotated upper-triangular system `R · y = s` over the running-QR
R-factor — against its cited Palace L0 evidence. **Top-level verdict:
fully-supported.** All 17 pinpoint Palace anchors are **zero-drift on-disk** (every
`citecheck --anchor` returns `[ok]` at the exact cited line; no codemap +1
brace-boundary drift recurs in this region — the discipline target did NOT trigger,
and I confirmed the no-drift assertion on-disk, not via codemap `read_range`). The
GMRES back-solve loop `iterative.cpp:652-660` and the FGMRES twin `:831-840` are
**line-for-line identical** as the leaf claims (read in full from on-disk), grounding
law 6 (basis-lift independence) — the only downstream difference is `x.Add(s[k], V[k])`
(`:666`) vs `x.Add(s[k], Z[k])` (`:843`). The signature shape (square dense
upper-triangular `(j+1)×(j+1)` R-factor, dense RHS `s`, dense solution `y`) matches
the `ScalarType` Hessenberg/RHS registers (`iterative.hpp:192-193`); the
element-type axis (`ScalarType` for `H`/`s`/`sn`, `RealType` for `cs`) is exact at
`:192-194`. The applicability conditions (upper-triangular + non-singular `R`; the
singular/lucky-breakdown case handled by the upstream residual test exiting before
back-solve) are positively anchored and complete — I confirmed the convergence break
at `:603-607` precedes the RHS seed `s[0] = beta` (`:612`) and the inner loop, so the
back-solve at `:653` is genuinely unreachable in that case. The `firm`-on-positive-
structure status and the load-bearing reduction-order non-law are justified. No
contradictions; no status change. I propose appending the `verified_against:` block.

## Per-citation audit

### GMRES back-solve interior (the operator's core)

- **Citation**: `palace/linalg/iterative.cpp:652`
  - **Theme claim**: the restart-cycle terminal back-solve comment "Reconstruct the solution (for restart or due to convergence or maximum iterations)".
  - **Found**: `citecheck --anchor 'Reconstruct the solution'` → `[ok]` at line 652. On-disk read confirms the comment verbatim, immediately preceding the back-substitution loop.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:653`
  - **Theme claim**: `for (int i = j; i >= 0; i--)` — descending back-substitution sweep; `i = -1` empty-cycle skips the body (law 5).
  - **Found**: `--anchor 'for (int i = j'` → `[ok]` at 653. On-disk: `for (int i = j; i >= 0; i--)` opens at 653 (brace `{` on 654). The descending sweep and empty-cycle skip are exactly as claimed.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:655`
  - **Theme claim**: `ScalarType *Hi = H.data() + i * (max_dim + 1);` — column `i` of the flat column-major R-factor (stride `max_dim+1`).
  - **Found**: `--anchor 'H.data() + i * (max_dim + 1)'` → `[ok]` at 655. On-disk verbatim. Grounds the dense-materialized upper-triangular shape + L0 flat storage.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:656`
  - **Theme claim**: `s[i] /= Hi[i];` — diagonal division `y[i] = s[i]/R[i][i]` (law 1, law 4; the singular-`R` divide-by-zero boundary).
  - **Found**: `--anchor 's[i] /= Hi[i]'` → `[ok]` at 656. On-disk verbatim.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:657`
  - **Theme claim**: `for (int k = i - 1; k >= 0; k--)` — inner super-diagonal subtraction loop (empty for `i=0`, single-column case, law 5).
  - **Found**: `--anchor 'for (int k = i - 1'` → `[ok]` at 657. On-disk: opens at 657 (brace on 658), empty body for `i=0` confirmed.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:659`
  - **Theme claim**: `s[k] -= Hi[k] * s[i];` — column-oriented super-diagonal subtraction `s[k] -= R[k][i]·y[i]` (law 4 transposed-index form; the reduction-order non-law).
  - **Found**: `--anchor 's[k] -= Hi[k] * s[i]'` → `[ok]` at 659. On-disk verbatim. The column-oriented (eager-update) variant of back-substitution is exactly as the leaf describes (law 4).
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:666`
  - **Theme claim**: `x.Add(s[k], V[k]);` — downstream `linear_combination` lift `x += Σ_k y[k]·V[k]` (GMRES `V` basis); NOT part of this leaf — grounds law 6.
  - **Found**: `--anchor 'x.Add(s[k], V[k])'` → `[ok]` at 666. On-disk: inside `if (!B || pc_side == LEFT)` block (`:662-668`), correctly downstream of the back-solve loop.
  - **Verdict**: supports.

### FGMRES twin (grounds law 6: line-for-line identity)

- **Citation**: `palace/linalg/iterative.cpp:831`
  - **Theme claim**: FGMRES back-solve comment "Reconstruct the solution" — the FGMRES restart-cycle terminal back-solve.
  - **Found**: `--anchor 'Reconstruct the solution'` → `[ok]` at 831. On-disk verbatim, identical comment to GMRES `:652`.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:835`
  - **Theme claim**: FGMRES `s[i] /= Hi[i];` — diagonal division identical to GMRES `:656`.
  - **Found**: `--anchor 's[i] /= Hi[i]'` → `[ok]` at 835. On-disk verbatim.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:838`
  - **Theme claim**: FGMRES `s[k] -= Hi[k] * s[i];` — super-diagonal subtraction identical to GMRES `:659`.
  - **Found**: `--anchor 's[k] -= Hi[k] * s[i]'` → `[ok]` at 838. On-disk verbatim.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:843`
  - **Theme claim**: FGMRES `x.Add(s[k], Z[k]);` — downstream lift against the flexible-preconditioner basis `Z` (the `op.basis_kind = Z` reconstruction); NOT part of this leaf — grounds law 6.
  - **Found**: `--anchor 'x.Add(s[k], Z[k])'` → `[ok]` at 843. On-disk: inside the FGMRES `for (int k = 0; k <= j; k++)` lift block (`:841-844`). The ONLY downstream difference from GMRES is `Z[k]` vs `V[k]`.
  - **Verdict**: supports. **The full-range read (`:831-840` vs `:652-660`) confirms the back-solve bodies are byte-identical — the leaf's "line-for-line identical" claim (law 6) is exact, not approximate.**

### Running-QR context anchors (boundary/applicability grounding; NOT the back-solve body)

- **Citation**: `palace/linalg/iterative.cpp:612`
  - **Theme claim**: `s[0] = beta;` — the RHS initialisation `s = β₀·e₁` (running-QR seed; the back-solve RHS is the rotated descendant of this seed).
  - **Found**: `--anchor 's[0] = beta'` → `[ok]` at 612. On-disk verbatim, immediately after `std::fill(s.begin(), s.end(), 0.0)` (`:611`).
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:631`
  - **Theme claim**: `Hj[j + 1] = linalg::Norml2(comm, w);` — the sub-diagonal `‖residual‖` entry the running-QR stream annihilates (context: the R-factor is what remains after the stream zeroes every sub-diagonal).
  - **Found**: `--anchor 'Norml2'` → `[ok]` at 631. On-disk verbatim. Correctly grounds the upper-triangular-establishment-is-upstream claim (the leaf does NOT establish triangularity; the running-QR stream does).
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:642`
  - **Theme claim**: `beta = std::abs(s[j + 1]);` — the LS residual (the *tail* entry `s[j+1]`, NOT part of the back-solve RHS — the back-solve uses `s[0..j]`).
  - **Found**: `--anchor 'beta = std::abs'` → `[ok]` at 642. On-disk verbatim. Confirms the back-solve RHS is `s[0..j]` and the tail `s[j+1]` is the residual (excluded from the back-solve), exactly as the signature's `s` shape contract states.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:644`
  - **Theme claim**: `converged = (beta < eps);` — the convergence test that exits before the back-solve in the lucky-breakdown case (singular-`R` non-law boundary).
  - **Found**: `--anchor 'converged = (beta < eps)'` → `[ok]` at 644. On-disk verbatim. **Cross-checked the control flow (`:594-612`): the outer-loop residual test at `:603-607` (`if (beta < eps) { converged = true; break; }`) exits BEFORE the RHS seed `s[0] = beta` (`:612`) and the inner loop, so when convergence is already detected at restart entry the back-solve loop at `:653` is unreachable. The applicability boundary (singular `R` handled upstream) is correctly anchored and complete.**
  - **Verdict**: supports.

### Register element-type anchors (the element-type axis)

- **Citation**: `palace/linalg/iterative.hpp:193`
  - **Theme claim**: `mutable std::vector<ScalarType> s, sn;` — the RHS register `s` (and rotation register `sn`) element type `ScalarType` (complex in the complex case).
  - **Found**: `--anchor 's, sn'` → `[ok]` at 193. On-disk verbatim. Also confirmed `H` is `ScalarType` (`:192`), so the R-factor and RHS share the `ScalarType` element type as the axis claim requires.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.hpp:194`
  - **Theme claim**: `mutable std::vector<RealType> cs;` — the cosine register `cs` always `RealType` (the element-type split underwriting the real/complex axis).
  - **Found**: `--anchor 'cs'` → `[ok]` at 194. On-disk verbatim. Completes the register-type picture (`cs` `RealType` while `s`/`sn`/`H` are `ScalarType`).
  - **Verdict**: supports.

### Intra-book parent / concept cross-references

- **Citation**: `book/src/L2/incremental-least-squares.md:81-83` (terminal `back_solve` projection)
  - **Theme claim**: this leaf is the L2 entry's terminal `back_solve` projection.
  - **Found**: `--anchor 'back_solve'` → `[ok]` at line 83 within 81-83. The L2 signature names a `back_solve` terminal projection; this leaf is its L1 home. Confirms the slug `back_solve` (the repair-renamed artifact-native slug) matches the L2 source — NOT `ls_update_column`.
  - **Verdict**: supports.

- **Citation**: `book/src/L2/incremental-least-squares.md:225-232` (residual-exposure law) and `:278-285` (rotation-stream non-associativity non-law)
  - **Theme claim**: the running-QR stream's norm-preservation (law 1 LS interpretation) and the rotation-stream non-associativity non-law that this leaf's reduction-order non-law composes with.
  - **Found**: both ranges in-bounds and read on-disk; `:225-232` is the "Residual exposure (the defining contract)" law (unitary rotation preserves 2-norm); `:278-285` is the "Rotation-stream associativity / re-factorisation equivalence at the bit level" load-bearing-numerical non-law. Both semantically match what the leaf cites them for.
  - **Verdict**: supports.

- **Citation**: `book/src/concepts/givens.md:29` (the "back_solve via trsv" concept anchor)
  - **Theme claim**: the concept page names the `back_solve` step "via `trsv`" at `:29` (the repair re-pointed this from the incorrect `concepts/incremental-least-squares.md:10`).
  - **Found**: `--anchor 'trsv'` → `[ok]` at 29. On-disk: the line ends "…enabling `back_solve` via `trsv`." The repair's cite-pointer correction is confirmed landed and exact.
  - **Verdict**: supports. **Note (carry-forward, not a defect of this leaf):** `givens.md:29` ALSO uses the slug `ls_update_column` for the column-streaming step in the SAME sentence — consistent with the leaf's disambiguation (the leaf is `back_solve`, the column step is `ls_update_column`), and matches the harvester's flagged low-fan-out prose-tightening trigger (tighten "via `trsv`" → name `back_solve`). Not blocking; future lifter/concept-recite work.

## Applicability conditions

- **Condition**: `R` square, upper-triangular (`(j+1)×(j+1)`).
  - **Verifiable**: Yes — the upper-triangularity is established UPSTREAM by the running-QR stream (`iterative.cpp:634-640` rotations + `:631` sub-diagonal annihilation), not by this leaf; the leaf reads the leading `(j+1)×(j+1)` block of the column-major `H` register via the `Hi = H.data() + i*(max_dim+1)` stride (`:655`). The shape is positively anchored.
  - **Found counter-example?**: No.

- **Condition**: `R` non-singular (for the contracted semantics).
  - **Verifiable**: Yes — and I confirmed the boundary is correctly handled. A zero diagonal `R[i][i]` divides-by-zero at `:656`; Palace avoids reaching the back-solve in the lucky-breakdown / exact-convergence case via the residual test. I traced TWO exit paths: (1) the outer-loop test `:603-607` exits before the RHS seed `:612` and the inner loop; (2) the inner-loop test `:644-649` breaks with `j` retained to reach the back-solve normally. The leaf's claim "Palace exits via the residual test before reaching the back-solve in that case" is exact.
  - **Found counter-example?**: No.

- **Condition**: RHS is the leading `j+1` entries `s[0..j]`; the tail `s[j+1]` (the LS residual) is excluded.
  - **Verifiable**: Yes — `:642` reads `s[j+1]` as the residual `beta`; the back-solve sweep `:653` runs `i = j … 0` over `s[0..j]` only. The signature's `s: Tensor[j+1]` shape and the "tail entry is not part of the RHS" note are both confirmed.
  - **Found counter-example?**: No.

- **Condition**: empty-cycle (`j = -1`) → `y = []`; single-column (`j = 0`) → one scalar division.
  - **Verifiable**: Yes — `for (int i = j; i >= 0; i--)` with `j = -1` skips the body; with `j = 0` runs once with the inner `k`-loop (`for k = -1; k >= 0`) empty. Law 5 is structurally exact.
  - **Found counter-example?**: No.

## Algebraic laws (cited)

- **Law 1 — Solve inverts apply (defining contract).** `R · back_solve(R, s) = s`; `back_solve(R, ·) = R⁻¹`. **Holds on operators?** Yes — syntactic identity: the back-substitution at `:656,:659` computes `R⁻¹s` exactly for upper-triangular non-singular `R` (a standard operator-algebra fact, not a convergence claim). The LS interpretation rests on the L2 residual-exposure law (`:225-232`, verified in-bounds).

- **Law 2 — Linearity in the RHS.** `back_solve(R, ·)` is linear. **Holds?** Yes — `R⁻¹` is a linear map for fixed `R`. `back_solve(R, 0) = 0` follows.

- **Law 3 — Compose-with-scale on the coefficient.** `back_solve(c·R, s) = (1/c)·back_solve(R, s)`. **Holds?** Yes — `(cR)⁻¹ = c⁻¹R⁻¹`, and `c·R` stays upper-triangular. A true identity (not exploited in Palace; correctly noted).

- **Law 4 — Back-substitution correctness (descending recurrence).** **Holds?** Yes — the Palace loop realises the column-oriented (transposed-index, eager-update) variant: it sweeps column `i` and subtracts `R[k][i]·y[i]` from `s[k]` for `k < i` (`:659`), computing the same exact-arithmetic `y` as the row-oriented form. Confirmed against the on-disk loop structure.

- **Law 5 — Empty / single-column boundary.** **Holds?** Yes — structural degenerate cases of the loop bounds (`:653`); see applicability above.

- **Law 6 — Basis-lift independence.** **Holds?** Yes — and this is the strongest confirmation of the audit: the GMRES (`:652-660`) and FGMRES (`:831-840`) back-solve bodies are **byte-identical** (read in full on-disk); the basis is read only by the downstream lift (`:666` `V` vs `:843` `Z`), never inside the back-solve. The leaf has no basis knowledge — exact.

- **Non-laws** (reduction-order independence; coefficient linearity; definedness without non-singularity; general-`trsv` membership). All correctly recorded:
  - Reduction-order: the descending column-oriented sweep (`:653,:657,:659`) pins a finite-precision path — load-bearing per the CLAUDE.md numerical-trick taxonomy. Composes with the L2 rotation-stream non-associativity non-law (`:278-285`, verified). Correctly a non-law, NOT a status reduction (the *value* is reduction-order-independent).
  - General-`trsv` membership: the leaf is the small-dense coordinate-space back-solve (dim `j+1` ≤ `max_dim`, no MPI collective), a SIBLING of the unanchored general `trsv` (sparse-triangular smoother, length-`N` field). I confirmed the `trsv` gap stays open — this leaf does not falsely close it.

## Proposed changes

Append the `verified_against:` metadata block to the firm L1 leaf. The audit found
**no contradictions and no status change** — the block records the per-citation
no-drift verdicts for cross-layer-cross-cutter coverage consumption. (Code sample
inside the fence is 4-space-indented per the nested-fence discipline.)

```edit:book/src/L1/back_solve.md
[append at end of file]
    verified_against:
      - citation: palace/linalg/iterative.cpp:652
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: GMRES back-solve comment "Reconstruct the solution"; citecheck --anchor zero-drift on-disk.
      - citation: palace/linalg/iterative.cpp:653
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: descending back-substitution sweep `for (int i = j; i >= 0; i--)`; empty-cycle (j=-1) skip grounds law 5; zero-drift.
      - citation: palace/linalg/iterative.cpp:655
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: column-major stride `Hi = H.data() + i*(max_dim+1)`; grounds dense upper-triangular shape; zero-drift.
      - citation: palace/linalg/iterative.cpp:656
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: diagonal division `s[i] /= Hi[i]` (laws 1,4; singular-R divide-by-zero boundary); zero-drift.
      - citation: palace/linalg/iterative.cpp:657
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: inner super-diagonal loop `for (int k = i-1; k >= 0; k--)` (empty for j=0, law 5); zero-drift.
      - citation: palace/linalg/iterative.cpp:659
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: column-oriented subtraction `s[k] -= Hi[k]*s[i]` (law 4 transposed-index; reduction-order non-law); zero-drift.
      - citation: palace/linalg/iterative.cpp:666
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: downstream GMRES `V`-basis lift `x.Add(s[k], V[k])` (grounds law 6; NOT part of leaf); zero-drift.
      - citation: palace/linalg/iterative.cpp:831-840
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: FGMRES back-solve twin (body range :831-840); full-range read confirms BYTE-IDENTICAL to GMRES :652-660 (law 6); :831/:835/:838 body anchors + :843 downstream Z-basis lift (outside the body range) all zero-drift.
      - citation: palace/linalg/iterative.cpp:612
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: RHS seed `s[0] = beta` (s = β₀·e₁); back-solve RHS is its rotated descendant; zero-drift.
      - citation: palace/linalg/iterative.cpp:631
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: "`Hj[j+1] = Norml2(comm, w)` sub-diagonal the running-QR stream annihilates (upper-triangularity is upstream); zero-drift."
      - citation: palace/linalg/iterative.cpp:642
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: "`beta = std::abs(s[j+1])` LS residual tail entry, EXCLUDED from the back-solve RHS s[0..j]; zero-drift."
      - citation: palace/linalg/iterative.cpp:644
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: convergence test `converged = (beta < eps)`; control-flow traced (outer :603-607 exits before seed :612 + inner loop) — singular-R back-solve unreachable in lucky-breakdown case; applicability boundary complete; zero-drift.
      - citation: palace/linalg/iterative.hpp:193
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: RHS register `s, sn` ScalarType (H also ScalarType :192); grounds element-type axis; zero-drift.
      - citation: palace/linalg/iterative.hpp:194
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: cosine register `cs` RealType; completes the real/complex element-type split; zero-drift.
      - citation: book/src/L2/incremental-least-squares.md:81-83
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: parent L2 terminal `back_solve` projection (anchor at :83); confirms the artifact-native slug `back_solve` matches the L2 source (NOT ls_update_column).
      - citation: book/src/L2/incremental-least-squares.md:225-232
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: residual-exposure law (unitary rotation 2-norm preservation) underwriting law 1's LS interpretation; in-bounds, semantically exact.
      - citation: book/src/L2/incremental-least-squares.md:278-285
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: rotation-stream non-associativity load-bearing-numerical non-law the leaf's reduction-order non-law composes with; in-bounds, semantically exact.
      - citation: book/src/concepts/givens.md:29
        verdict: supports
        audited_at: 2026-05-29T194558Z
        note: 'the "back_solve via trsv" concept anchor (repair-corrected from the wrong pointer book/src/concepts/incremental-least-squares.md:10, where trsv does not appear); zero-drift; low-fan-out prose-tightening trigger noted (tighten to name back_solve).'
```

## Supporting evidence

Files consulted (all on-disk, citation source of truth):
- `reference/palace/palace/linalg/iterative.cpp` — read GMRES `:594-674` and FGMRES `:826-850` in full; ran `citecheck --anchor` against all 15 `iterative.cpp` pinpoints.
- `reference/palace/palace/linalg/iterative.hpp` — read `:188-197`; confirmed `H`/`s`/`sn` `ScalarType`, `cs` `RealType`.
- `book/src/L1/back_solve.md` — the leaf under audit (read in full).
- `book/src/L1/index.md` — confirmed dep-map row (`:95`), cohort bullet (`:53`), `**Firm (21)**` count (`:31`) all landed with the `back_solve` slug.
- `book/src/SUMMARY.md` — confirmed `back_solve` chapter entry (`:85`).
- `book/src/L2/incremental-least-squares.md` — confirmed `:81-83`, `:225-232`, `:278-285`.
- `book/src/concepts/givens.md:29` — confirmed the repair-corrected "back_solve via trsv" anchor.
- `reports/2026-05-29T175529Z-harvester-ls-update-column-l1/CYCLE.md` + `META.md` — the harvester report + critic/repairer rename history (ls_update_column → back_solve slug collision repair).

Tooling: `tools/citecheck/citecheck.py --anchor` (the shared authoritative on-disk line-map) on all 17 Palace + 4 intra-book pinpoints — **17/17 Palace anchors `[ok]` zero-drift**, all intra-book ranges in-bounds.

## Open questions / caveats

- **No drift, despite the discipline warning.** The cycle-027 dispatch directive flagged
  the `iterative.cpp`/`nleps.cpp` region as a known codemap +1 brace-boundary offender.
  This audit rested its no-drift assertion on `citecheck --anchor` against ON-DISK
  (not codemap `read_range` output) per the discipline. **The drift did NOT recur** for
  any of the 17 anchors — every anchor is at its exact cited line on-disk. This matches
  the critic/repairer META.md finding (43 ok / 0 failing). No carry-forward citation
  correction needed for this leaf. (The discipline target is confirmed quiescent here;
  the on-disk-wins protocol was applied and found nothing to correct.)

- **Slug-collision rename history (resolved, recorded for context).** The leaf was
  harvested under `ls_update_column` and renamed to `back_solve` in repair (the critic
  found `ls_update_column` already binds the DISTINCT column-streaming step at
  `L2/incremental-least-squares.md:412` + `concepts/incremental-least-squares.md:14`). I
  confirmed the renamed slug `back_solve` matches the parent L2 terminal-projection
  source (`:83`) and `givens.md:29`. The rename is correct and fully landed (index.md +
  SUMMARY.md + the leaf all use `back_solve`). No residual collision.

- **Carry-forward prose-tightening trigger (low fan-out, NOT this audit's scope).**
  `concepts/givens.md:29` says "enabling `back_solve` via `trsv`" — now that `back_solve`
  has its own firm L1 leaf distinct from the unanchored general `trsv`, that prose could
  be tightened to name `back_solve` (the GMRES-restart-correction back-solve) rather than
  the general `trsv`. The harvester already flagged this (pairs with the
  `givens-concept-page-gmres-md-to-iterative-cpp-recite` plan candidate). Mechanical;
  future lifter/concept-recite dispatch. Not a defect of the audited leaf.

- **`trsv` L3-inventory gap stays open (correctly).** The leaf does NOT close the
  `trsv` gap (`scaffolding/open-questions.md:24,:448`) — it is a sibling of, not the
  realisation of, the general sparse-triangular solve. The "general-`trsv` membership"
  non-law is sound and well-anchored. Confirmed not falsely closed.

- **Status unchanged.** The audit confirms `firm` (firm-on-positive-structure, the
  `lu_solve`/`apply_linop` precedent; the no-dedicated-test caveat is non-gating for
  syntactic-identity laws; the reduction-order non-law is a recorded non-law, not a
  status reduction). I propose no status change — only the `verified_against:` append.
