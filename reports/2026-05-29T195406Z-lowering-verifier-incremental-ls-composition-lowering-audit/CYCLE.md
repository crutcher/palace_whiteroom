---
agent: lowering-verifier
invoked_at: 2026-05-29T195406Z
scope: L2>L1 theme audit — incremental-least-squares-composition-lowering
status: integrated
integrated_at: 2026-05-29T205500Z
integration_commit: 3319d88
integration_notes: "cycle-028 position 5/7 (per-report; DEPENDS on position 1 — report-1 created the theme file, verified on disk 499 lines pre-append). Additive verified_against: audit of the firm L2>L1 incremental-least-squares-composition-lowering theme (landed firm c028 D1 same cycle, the dependency root). Verdict fully-supported, firm confirmed, no corrective edits to the theme body — 22-row yaml block (17 L0 + 5 book-internal), all supports. One land-time discretionary repair: two note: values began with a literal double-quote (failed yaml.safe_load); single-quote-wrapped (mechanical transport-quoting, content unchanged) — flagged the leading-quote channel-format hazard for the meta-phase. §Status untouched. Build clean (yaml fence balanced, zero build-repairs)."
inputs:
  - book/src/L2-L1/incremental-least-squares-composition-lowering.md (the theme — NOT yet on disk; landed THIS cycle by dispatch-1's new: block; audited from reports/2026-05-29T194558Z-lifter-.../CYCLE.md lines 26-525)
  - reports/2026-05-29T194558Z-lifter-incremental-ls-composition-lowering-reanchor/CYCLE.md (authoritative re-anchored theme body)
  - book/src/L1/back_solve.md (the firm leaf the terminal back-solve re-anchors onto; firm c027)
  - book/src/L2/incremental-least-squares.md (the firm L2 parent / LHS; firm c026)
  - book/src/L2/linear_combination.md (firm; back-solve reconstruction)
  - book/src/concepts/givens_generate.md, givens_apply.md, plane-rotation-stream.md, incremental-least-squares.md (de-fused Face-2 + Face-1 contract)
  - book/src/L2-L1/orthogonalize-composition-lowering.md (firm sibling; firm-promotion template)
  - reference/palace/palace/linalg/iterative.cpp + iterative.hpp (L0 evidence)
---

# CYCLE: Audit incremental-least-squares-composition-lowering

## Summary

Per-line `verified_against:` audit of the L2>L1 `incremental-least-squares-composition-lowering`
theme (cycle-028 dispatch-1's `new:` block: a `rough-in → firm` re-anchor of the c027-D5-deferred
theme onto the now-firm `back_solve` leaf). I independently `citecheck --anchor`-confirmed **every**
L0 range the theme cites against on-disk `reference/palace/`, read the full GMRES (`iterative.cpp:632-680`)
and FGMRES (`:812-844`) stream + back-solve + correction bodies, and confirmed every book-internal
cross-reference resolves and means what the theme asserts. **Top-level verdict: fully-supported.**
All 17 L0 anchors verify clean with **zero drift** — including the known codemap +1-drift offender
`iterative.hpp:193-194`, which is exact on-disk (citecheck/on-disk authoritative). The four-sub-step
fan-down (`replay×j ▷ generate ▷ apply ▷ apply_rhs`), the fixed replay-before-generate non-commutative
ordering, the terminal back-solve fan-down, the two parametric variant axes (`op.basis_kind∈{V,Z}`,
`op.variant∈{real,complex}`), and the per-sub-step reduction-path table all match the source bodies
exactly. The **back_solve re-anchor is sound**: the terminal solve at `:652-660`/`:831-840` genuinely
IS the firm `back_solve` leaf (body line-identical to `back_solve.md`'s own L0 evidence), a small-dense
back-substitution over the running-QR R-factor — **not** a general `trsv` (which has no positive L0
anchor and remains the separately-blocked L3-inventory item, `open-questions.md:24`). The
**`ls_update_column` column-streaming Face-1 forward-note is accurate**: the file does not exist on
disk (confirmed by `find`), so the plain-text (not live-link) treatment is correct and not a false
live-link. The `firm` status and the high→low direction are both confirmed appropriate. **No
contradictions; no proposed content edits.** This audit attaches the `verified_against:` block as the
standard non-status-reducing follow-up the lifter flagged.

## Per-citation audit

L0 ranges (the theme's §Verified-against L0 list + reduction-path table + applicability conditions):

- **Citation**: `palace/linalg/iterative.cpp:73-108` (`GeneratePlaneRotation` real kernel, LAPACK-scaled)
  - **Theme claim**: the `generate` sub-step's real kernel; overflow/underflow scaling at `:101-108`.
  - **Found**: `--anchor 'GeneratePlaneRotation'` at line 73, in range; `--show :101-108` confirms the
    scaled branch `u = min(safmax, max(safmin, max(dx1, dy1)))` … `cs = abs(dxs)/d; sn = dys/copysign(d, dx)`.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:112-118` (`GeneratePlaneRotation` complex; unitarity contract)
  - **Theme claim**: real `cs`, complex `sn`, in-comment "cs is real and cs² + |sn|² = 1" at `:118`.
  - **Found**: `--anchor 'cs is real'` resolves at line 118 within range.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:227-241` (`ApplyPlaneRotation` real `:227` + complex `:235`)
  - **Theme claim**: in-place 2-vector update `(dx', dy') = (cs·dx + sn·dy, −s̄n·dx + cs·dy)`, `s̄n = conj(sn)` complex.
  - **Found**: `--anchor 'ApplyPlaneRotation'` at lines [227, 235]. Body read in full: real
    `t = cs*dx + sn*dy; dy = -sn*dx + cs*dy` (`:229-230`); complex `dy = -std::conj(sn)*dx + cs*dy`
    (`:239`). Exactly the theme's signature, incl. the conjugate convention.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:612` (`s[0] = beta`, RHS seed `s = β₀·e₁`)
  - **Theme claim**: the running-QR RHS seed.
  - **Found**: `--anchor 's[0] = beta'` exact at line 612.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:631` (`Hj[j+1] = Norml2(comm, w)`, sub-diagonal entry)
  - **Theme claim**: the arriving column's sub-diagonal `h_new[j+1]`; orthogonalize coeffs occupy `0..j`.
  - **Found**: `--anchor 'Norml2'` exact at line 631.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:634-636` (GMRES **replay**)
  - **Theme claim**: `for (k=0; k<j; k++) ApplyPlaneRotation(Hj[k], Hj[k+1], cs[k], sn[k]);` — law-2 ordering, strictly `k=0..j-1`.
  - **Found**: `--anchor` literal at line 636; full body read (`:634` loop head, `:636` call). The `k < j`
    bound is the empty-fold-for-`j=0` skip-replay boundary the theme asserts.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:638` (GMRES **generate**)
  - **Theme claim**: `GeneratePlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j]);` AFTER replay (law 2).
  - **Found**: `--anchor` exact at line 638; body confirms it follows the `:634-637` replay loop —
    the replay-before-generate ordering is positively witnessed (replay closes `:637`, generate `:638`).
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:639` (GMRES **apply**, triangularise own column)
  - **Theme claim**: `ApplyPlaneRotation(Hj[j], Hj[j+1], cs[j], sn[j]);`, zeroes `Hj[j+1]`.
  - **Found**: `--anchor` exact at line 639.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:640` (GMRES **apply_rhs**)
  - **Theme claim**: `ApplyPlaneRotation(s[j], s[j+1], cs[j], sn[j]);`, concentrates residual in `s[j+1]`.
  - **Found**: `--anchor` exact at line 640.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:642` (`beta = std::abs(s[j+1])`, residual exposure law 1)
  - **Theme claim**: the residual exposure as a free byproduct.
  - **Found**: `--anchor 'beta = std::abs(s[j + 1])'` exact at line 642.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:644` (`converged = (beta < eps)`)
  - **Theme claim**: convergence read with no explicit residual evaluation.
  - **Found**: `--anchor` exact at line 644.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:652-660` (GMRES **back-solve**, the firm `back_solve` leaf body)
  - **Theme claim**: in-place back-substitution `s[i] /= Hi[i]` (`:656`) / `s[k] -= Hi[k]·s[i]` (`:659`),
    descending sweep, leaving `y = s[0..j]`; the terminal triangular solve IS the firm `back_solve` leaf.
  - **Found**: full body read — `// Reconstruct the solution` (`:652`), `for (int i=j; i>=0; i--)` (`:653`),
    `Hi = H.data() + i*(max_dim+1)` (`:655`), `s[i] /= Hi[i]` (`:656`), inner `for (k=i-1; k>=0; k--)`
    (`:657`), `s[k] -= Hi[k]*s[i]` (`:659`). **Line-identical to `back_solve.md`'s own §Evidence L0
    citations** (`back_solve.md:135-141`, `:394-413`). This IS the firm `back_solve` leaf, not a
    general trsv. `--anchor 'Reconstruct the solution'`/`'s[i] /= Hi[i]'`/`'s[k] -= Hi[k] * s[i]'` all exact.
  - **Verdict**: supports. (Back-solve re-anchor soundness confirmed — see §"back_solve re-anchor".)

- **Citation**: `palace/linalg/iterative.cpp:666` (GMRES V-correction, `op.basis_kind = V`)
  - **Theme claim**: `x.Add(s[k], V[k]);` — the `linear_combination` reconstruction (left/unpreconditioned).
  - **Found**: `--anchor 'x.Add(s[k], V[k])'` exact at 666; body confirms it sits in the
    `!B || pc_side == LEFT` branch (`:662-668`), matching the theme's left/unpreconditioned characterisation.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:674-677` (GMRES right-preconditioned correction)
  - **Theme claim**: `r.Add(s[k], V[k])` (`:674`) then `ApplyB(B, r, V[0]); x += V[0]` (`:676-677`) —
    preconditioner post-applied to the V-correction; back-solve identical.
  - **Found**: full body read — the `else // RIGHT` branch (`:669`): `r = 0.0` (`:671`),
    `r.Add(s[k], V[k])` (`:674`), `ApplyB(B, r, V[0], ...)` (`:676`), `x += V[0]` (`:677`). Exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:812-821` (FGMRES running-QR stream)
  - **Theme claim**: replay `:813-815`, generate `:817`, apply `:818`, apply_rhs `:819`, beta `:821` —
    **line-for-line identical** to the GMRES stream (law 6, `op.basis_kind`-invariant).
  - **Found**: full body read — `:813-815` replay loop, `:817` generate, `:818` apply, `:819` apply_rhs,
    `:821` beta. **Byte-for-byte identical** to GMRES `:634-642` (verified by reading both ranges full).
    Law-6 invariance is positively witnessed.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:831-840` (FGMRES back-solve) + `:843` (Z-correction)
  - **Theme claim**: back-solve identical to GMRES `:652-660`; then `x.Add(s[k], Z[k])` (`:843`), the
    `op.basis_kind = Z` reconstruction.
  - **Found**: full body read — `:831` "Reconstruct the solution", `:832-840` back-substitution
    (identical to GMRES `:652-660`), `:843` `x.Add(s[k], Z[k])`. The **only** difference from GMRES is
    `Z[k]` (`:843`) vs `V[k]` (`:666`) — exactly the theme's law-6 claim. `--anchor` both exact.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.hpp:193-194` (rotation-register element-type split)
  - **Theme claim**: `mutable std::vector<ScalarType> s, sn;` (`:193`) / `mutable std::vector<RealType> cs;`
    (`:194`) — the split underwriting `op.variant`; the c026 codemap +1 brace drift confirmed corrected.
  - **Found**: `--anchor 'std::vector<ScalarType> s, sn'` exact at 193; `--anchor 'std::vector<RealType> cs'`
    exact at 194. **The known codemap +1-drift offender is exact on-disk** (on-disk authoritative).
  - **Verdict**: supports.

Book-internal cross-references (the theme's L2 / L1 / concept / cross-theme anchor list):

- **Citation**: `book/src/L2/incremental-least-squares.md:81-83` / `:278-285` / `:334-340`
  - **Theme claim**: the `back_solve` terminal-projection signature (`:81-83`), the deferred
    rotation-stream-non-associativity non-law (`:278-285`, the load-bearing residue this theme picks up),
    and the §Dependencies forward-reference (`:334-340`).
  - **Found**: `:81-83` `back_solve :: LsqState' -> {...}` exact; `:278-285` "Rotation-stream
    associativity / re-factorisation equivalence at the bit level" non-law exact, ending "The exact
    per-lowered-call reduction order is pinned by the forthcoming L2>L1 theme" — this theme IS that
    forthcoming theme, so the residue pickup is correct; `:334-340` the forward-ref exact.
  - **Verdict**: supports.

- **Citation**: `book/src/L1/back_solve.md:44-61` / §Algebraic-laws law 6 / reduction-order non-law
  - **Theme claim**: the firm leaf the terminal back-solve targets; its §"Why this is NOT a general `trsv`"
    argument (`:44-61`), basis-lift-independence (law 6), reduction-order non-law.
  - **Found**: `:44-61` "Why this is NOT a general `trsv`" exact (small-dense `(j+1)×(j+1)`, `O(j²)`,
    N-independent, sibling of `lu_solve`). `back_solve.md` law 6 (`:223-230`) confirms basis-lift
    independence with the identical `:666`/`:843` anchors. The theme's terminal-back-solve fan-down
    lowers correctly onto this leaf.
  - **Verdict**: supports.

- **Citation**: `book/src/concepts/incremental-least-squares.md:14` / `:22-27`
  - **Theme claim**: the `ls_update_column` L1 column-streaming-leaf contract (`:14`); the "What is hidden
    at L1" list (`:22-27`).
  - **Found**: `:14` binds the `ls_update_column(K, j, h_new) → K'` per-column contract; `:22-27` "What is
    *hidden* at L1" = the Givens kernels, the replay-before-generate bookkeeping, the residual-off-the-RHS
    exposure — exactly the Face-1 "hidden inside the leaf" characterisation the theme asserts.
  - **Verdict**: supports.

- **Citation**: `book/src/concepts/plane-rotation-stream.md:5-15` / `:21-23` / `:25-33`
  - **Theme claim**: stream §Shape (`:5-15`), §"Sequential character" replay-chain sequential-obstruction
    candidate (`:21-23`), §"Variants the stream is invariant to" (`:25-33`).
  - **Found**: `:5-15` the 5-step shape (replay/generate/apply-to-self/propagate/read) matches the theme's
    4-sub-step + residual-read decomposition; `:21-23` "The replay step (1) is a length-k chain of 2-vector
    updates, each reading the output of the previous … sequential-obstruction candidate when lifting to L3" —
    exactly the theme's L3-forecast claim; `:25-33` the parametric-invariance list.
  - **Verdict**: supports.

- **Citation**: `book/src/concepts/givens_generate.md` / `givens_apply.md` / `givens.md`
  - **Theme claim**: the firm scalar Givens kernel pair carrying the de-fused Face-2 value.
  - **Found**: all three exist on disk; `givens_apply.md:13` states `(dx', dy') = (c·dx + s·dy, −s̄·dx + c·dy)`
    matching the L0 kernel body `:229-230`/`:238-240` and the theme's Face-2 signature. (Drive-by: see
    §Open questions — both concept pages carry a STALE `palace/linalg/gmres.cpp` citation; NOT cited by
    this theme, so it does not affect the audit.)
  - **Verdict**: supports.

- **Citation**: `book/src/L2/linear_combination.md` / `book/src/L2-L1/orthogonalize-composition-lowering.md`
  - **Theme claim**: the firm fold the terminal reconstruction lowers into; the firm sibling template (firm bar).
  - **Found**: both exist on disk (357 / 485 lines). The sibling is the structural template the theme
    matches (two-face L1 RHS, dispatch-rule prose, reduction-path table, `algebraic` classification).
  - **Verdict**: supports.

## Applicability conditions

1. **Replay-before-generate ordering is mandatory.**
   - **Verifiable**: yes — positively witnessed. The L0 control flow puts the replay loop (`:634-637`,
     closing brace `:637`) strictly before `GeneratePlaneRotation` (`:638`). The `k < j` loop bound also
     grounds the `j=0` skip-replay boundary. L2 law 2 (`:234-243`) and `givens.md` §Contract corroborate.
   - **Found counter-example?**: no.

2. **Unitary kernels, exact residual exposure.**
   - **Verifiable**: yes — the complex kernel's in-comment `cs² + |sn|² = 1` (`:118`) + the unitary
     2-vector update (`:227-241`) give the per-rotation unitarity; `β = |s[j+1]|` (`:642`/`:821`) is the
     apply_rhs byproduct. The algorithmic-correctness-vs-bit-reproduction split matches CLAUDE.md
     §Optimization tricks (load-bearing numerical trick).
   - **Found counter-example?**: no.

3. **`op.variant` is a scalar-kernel substitution.**
   - **Verifiable**: yes — register split `iterative.hpp:193-194` (`s`, `sn` `ScalarType`; `cs` `RealType`),
     inspected once; no per-column branch in the stream body (`:634-642`). The real/complex kernels differ
     only by `conj(sn)` (`:230` vs `:239`).
   - **Found counter-example?**: no.

4. **`op.basis_kind` reads only the terminal reconstruction.**
   - **Verifiable**: yes — the GMRES (`:634-642`) and FGMRES (`:813-821`) streams are byte-identical
     (read in full); the ONLY divergence is `V[k]` (`:666`) vs `Z[k]` (`:843`). Right-precond post-applies
     `B` to the V-correction (`:674-677`) but the back-solve is identical. Exactly law 6.
   - **Found counter-example?**: no.

5. **Leaf-stops-at-L1; kernel L0 deferred.**
   - **Verifiable**: yes (boundary cleanliness). The theme defers the four `*PlaneRotation` in-place writes
     to the forthcoming `ls_update_column` L1>L0 theme, the back-solve in-place `s[0..j]` overwrite to the
     firm `back_solve` leaf's own L1>L0 concern (`back_solve.md` §"L1 vs L0 distinction" `:371-390`), and
     the `x.Add` reconstruction to `linear_combination`. **No duplication of the L0 in-place step**: the
     theme cites the L0 sites for *identification* (reduction-path table) but does not re-derive the in-place
     mechanics — it stops at the L1 leaves, the same boundary the sibling draws. Clean.
   - **Found counter-example?**: no.

## Algebraic laws (the fan-down rule, read as a lowering)

- **Law 1 (residual exposure, `β = |s[j+1]|`)**: Holds on operators. The apply_rhs sub-step (`:640`/`:819`)
  then `beta = std::abs(s[j+1])` (`:642`/`:821`) is the free byproduct; unitarity (`:118`) preserves the
  2-norm. The fan-down preserves it (Face 2 emits the apply_rhs as its 4th sub-step; Face 1 hides it in `K'.beta`).
- **Law 2 (replay-before-generate, non-commutative)**: Holds. Positively witnessed by the L0 control flow
  ordering (`:634-637` before `:638`). The theme correctly marks the replay fold as the bit-level
  non-commutative chain and the L3 sequential-obstruction candidate.
- **Law 6 (`op.basis_kind` / `op.variant` parametric invariance)**: Holds. The byte-identical GMRES/FGMRES
  streams + the single `V[k]`/`Z[k]` reconstruction divergence (`:666`/`:843`) establish basis_kind
  invariance of the stream; the register-type split (`hpp:193-194`) establishes variant absorption. The
  theme's "no per-variant sequence selection — the sub-step sequence is fixed and identical across both
  axes" is correct (contrast the sibling's MGS/CGS/CGS2 axis, which IS structural).
- **Justification kind `algebraic`**: Confirmed appropriate. The fan-down rule IS the L2 entry's already-firm
  laws 1/2/6 read as a lowering — matching the sibling `orthogonalize-composition-lowering` `algebraic`
  classification. The structural (Face-2 de-fusion) and reduction-chain (replay fold + back-solve recurrence)
  flavours are correctly noted as present-but-not-governing.

## back_solve re-anchor (the load-bearing re-anchor decision)

**Sound.** The theme's terminal-back-solve fan-down targets the firm L1 `back_solve` leaf, NOT a general
`trsv`. Confirmed by:
- The L0 back-solve body (`iterative.cpp:652-660` GMRES / `:831-840` FGMRES) is **line-identical** to
  `back_solve.md`'s own §Evidence L0 citations — it is the same operator.
- `back_solve.md:44-61` ("Why this is NOT a general `trsv`") positively argues the small-dense,
  N-independent, `(j+1)×(j+1)`, no-collective character — the theme's characterisation matches verbatim.
- The general `trsv` / `sparse_triangular_solve` has **no positive L0 anchor** and remains the
  separately-**blocked** L3-inventory item (`open-questions.md:24` confirms "REMAINING: `trsv` ONLY
  (BLOCKED, no L1 anchor)"). The theme correctly demotes the general-`trsv` mention to a forward note and
  does **not** claim it exists. **The `trsv` gap is NOT falsely touched/closed by this firm theme.**

## ls_update_column column-streaming forward-note (the false-live-link check)

**Accurate; correctly plain-text.** `find book/src -name 'ls_update_column*'` returns nothing —
`book/src/L1/ls_update_column.md` does **not** exist on disk. The theme's Face-1 reference is therefore
correctly **plain text** (not a live link); a live link would be a `linkcheck2` hard error. The theme's
characterisation is accurate: `ls_update_column` is the DISTINCT per-column running-QR streaming leaf
(`concepts/incremental-least-squares.md:14`), separate from the terminal `back_solve` — the `back_solve.md:31-34`
note independently confirms this slug-disambiguation. The firm-promotion judgment (Face 1 co-extensive with
the firm de-fused Face 2, so the opaque-leaf forward-ref is a presentation choice not a value-gate) is sound
and matches the sibling firm bar; I concur the `firm` status is appropriate (see §Status confirmation).

## Status confirmation (firm)

I concur with `firm`. The lifter flagged the one non-mechanical judgment (promote despite the Face-1
`ls_update_column` leaf not being on disk) for critic/integrator confirmation. My audit supports the
promotion: (i) the back-solve target is now resolved to the firm `back_solve` leaf (the deferred draft's
sole hard gate); (ii) Face 2 (de-fused scalar Givens) is fully firm and co-extensive in value with Face 1
— the value the fan-down computes is carried by Face 2 + `back_solve` + `linear_combination`, all firm;
(iii) all L0 evidence is self-verified clean. This is the sibling `orthogonalize-composition-lowering`
firm bar (fan-down rule IS the L2 entry's firm laws read as a lowering). No literature inference, no
negative-anchor reconstruction, no speculative operator. **The audit does NOT reduce the status** — it is
the standard non-status-reducing `verified_against:` follow-up.

## Direction-of-definition (high→low)

Confirmed forward (L2 → L1): the LHS is the L2 named composition, the RHS the L1 leaves, the prose narrates
the rewrite L2-into-L1. The reverse-direction (L1→L2 lift) notes are absent from the chapter (correctly in
working notes). No direction-of-definition violation.

## Proposed changes

The integrator will apply this append AFTER dispatch-1's `new:` block lands the theme on disk; the theme is
referenced by its on-disk path. The block is emitted as a fenced ```yaml``` code block per the
channel-format requirement. One audit row per cited range; all verdicts `supports` (the audit found no
partial-support or out-of-range citations).

```edit:book/src/L2-L1/incremental-least-squares-composition-lowering.md
[append at end of file]
~~~yaml
verified_against:
  - citation: palace/linalg/iterative.cpp:73-108
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: GeneratePlaneRotation real kernel; LAPACK scaling :101-108 confirmed via --show. citecheck --anchor clean.
  - citation: palace/linalg/iterative.cpp:112-118
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: GeneratePlaneRotation complex; "cs is real and cs²+|sn|²=1" anchor exact at :118.
  - citation: palace/linalg/iterative.cpp:227-241
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: ApplyPlaneRotation real :227 / complex :235; body confirms (cs·dx+sn·dy, −conj(sn)·dx+cs·dy).
  - citation: palace/linalg/iterative.cpp:612
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: s[0]=beta RHS seed; anchor exact.
  - citation: palace/linalg/iterative.cpp:631
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: Hj[j+1]=Norml2 sub-diagonal entry; anchor exact.
  - citation: palace/linalg/iterative.cpp:634-636
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: GMRES replay; ApplyPlaneRotation(Hj[k],Hj[k+1],cs[k],sn[k]) at :636; k<j skip-replay-for-j=0 boundary witnessed.
  - citation: palace/linalg/iterative.cpp:638
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: GMRES generate; positively follows replay loop close :637 (replay-before-generate ordering witnessed).
  - citation: palace/linalg/iterative.cpp:639
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: GMRES apply (triangularise own column); anchor exact.
  - citation: palace/linalg/iterative.cpp:640
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: GMRES apply_rhs; ApplyPlaneRotation(s[j],s[j+1],...) concentrates residual; anchor exact.
  - citation: palace/linalg/iterative.cpp:642
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: beta=std::abs(s[j+1]) residual exposure (law 1); anchor exact.
  - citation: palace/linalg/iterative.cpp:644
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: converged=(beta<eps); convergence read with no explicit residual eval; anchor exact.
  - citation: palace/linalg/iterative.cpp:652-660
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: GMRES back-solve; body line-identical to firm back_solve.md L0 evidence (s[i]/=Hi[i] :656, s[k]-=Hi[k]*s[i] :659) — IS the firm back_solve leaf, NOT general trsv.
  - citation: palace/linalg/iterative.cpp:666
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: GMRES V-correction in !B||LEFT branch; linear_combination reconstruction (op.basis_kind=V); anchor exact.
  - citation: palace/linalg/iterative.cpp:674-677
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: GMRES right-precond r.Add(s[k],V[k]) :674 then ApplyB(B,r,V[0]) :676 / x+=V[0] :677; back-solve identical.
  - citation: palace/linalg/iterative.cpp:812-821
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: FGMRES stream (replay :813-815, generate :817, apply :818, apply_rhs :819, beta :821) — byte-identical to GMRES :634-642 (law 6).
  - citation: palace/linalg/iterative.cpp:831-840
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: FGMRES back-solve identical to GMRES :652-660; x.Add(s[k],Z[k]) :843 the op.basis_kind=Z reconstruction (only V/Z divergence).
  - citation: palace/linalg/iterative.hpp:193-194
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: register split ScalarType s,sn :193 / RealType cs :194 underwriting op.variant; KNOWN codemap +1-drift offender confirmed EXACT on-disk (on-disk authoritative).
  - citation: book/src/L2/incremental-least-squares.md:278-285
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: rotation-stream non-associativity non-law — the load-bearing residue this theme picks up ("forthcoming L2>L1 theme"); :81-83 terminal back_solve sig + :334-340 forward-ref also confirmed.
  - citation: book/src/L1/back_solve.md:44-61
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: "Why this is NOT a general trsv" — terminal back-solve target re-anchor confirmed sound; small-dense N-independent leaf, not blocked general trsv.
  - citation: book/src/concepts/incremental-least-squares.md:22-27
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: "What is hidden at L1" list matches Face-1 opaque-leaf characterisation; :14 ls_update_column contract confirmed.
  - citation: book/src/concepts/plane-rotation-stream.md:21-23
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: replay-chain sequential-obstruction candidate (L3 forecast) confirmed; :5-15 shape + :25-33 invariance also confirmed.
  - citation: book/src/concepts/givens_apply.md
    verdict: supports
    audited_at: 2026-05-29T195406Z
    note: Face-2 de-fused kernel; signature (c·dx+s·dy, −s̄·dx+c·dy) matches L0 body :229-230/:238-240. (Stale gmres.cpp self-citation in concept page noted as drive-by, not cited by this theme.)
~~~
```

(The `~~~` triple-tilde above denotes the triple-backtick fence delimiter in the actual emitted edit;
the integrator writes a literal ```` ```yaml ```` / ```` ``` ```` fence.)

**No corrective edits proposed** — the audit found zero contradictions, zero drift, and confirmed the
firm status, the high→low direction, the back_solve re-anchor, and the plain-text `ls_update_column`
forward-note are all correct.

## Supporting evidence

- L0: `reference/palace/palace/linalg/iterative.cpp:73-241` (kernels), `:612-680` (GMRES stream + back-solve
  + correction, read in full), `:812-844` (FGMRES, read in full); `iterative.hpp:193-194` (registers).
- citecheck: all 17 L0 anchors (22 verified_against rows = 17 L0 + 5 book-internal) + the LAPACK `:101-108` sub-range (a `--show` sub-range inside the `:73-108` anchor, not a separate anchor) run via
  `python3 tools/citecheck/citecheck.py <path:lo-hi> --anchor '<token>'` against on-disk `reference/` —
  all `[ok]`, zero `[DRIFT]`.
- Book artifact: `book/src/L1/back_solve.md` (firm leaf, re-anchor target + slug-disambiguation),
  `book/src/L2/incremental-least-squares.md` (firm LHS, non-law residue), `book/src/L2/linear_combination.md`,
  `book/src/concepts/{incremental-least-squares,plane-rotation-stream,givens_generate,givens_apply,givens}.md`,
  `book/src/L2-L1/orthogonalize-composition-lowering.md` (firm sibling template).
- `find book/src -name 'ls_update_column*'` → no hits (Face-1 plain-text forward-ref confirmed correct).
- `scaffolding/open-questions.md:24` (trsv BLOCKED), `:766` (the c028-active deferral OQ this dispatch chain resolves).

## Open questions / caveats

- **Drive-by (out of audit scope, NOT a theme defect): stale `gmres.cpp` self-citations in two concept
  pages.** `book/src/concepts/givens_generate.md:23` and `givens_apply.md:23` both cite
  `palace/linalg/gmres.cpp:GeneratePlaneRotation` / `:ApplyPlaneRotation` — but the kernels live in
  `palace/linalg/iterative.cpp` (no `gmres.cpp` in the current tree). The theme under audit does NOT cite
  those concept-page paths (it cites the kernels at `iterative.cpp:73-241` directly), so this does not
  affect any audit verdict. Flagged so a future concept-page re-anchor (layer-intro-author / lifter scope)
  can correct the two pages. Not in this audit's correction scope (the theme is clean).

- **`ls_update_column` column-streaming leaf still un-harvested (carried forward, not a blocker).** The
  theme correctly leaves Face-1 as a plain-text forward-note (the file is confirmed absent on disk) and
  the lifter flagged a follow-on harvester target. This audit confirms the forward-note is accurate and
  the theme's firmness does not depend on the leaf. The harvest remains a fresh plan candidate (small L1
  leaf, L0 site `iterative.cpp:634-642`), as the lifter's §Open-questions recorded — no change.

- **L3 sequential-obstruction forecast (replay chain + back-solve recurrence) is a forward note, not
  audited as content.** The theme's L3 forecast (replay fold `:634-636` + back-solve inner `k`-recurrence
  `:659` are sequential-obstruction candidates) is correctly scoped as a forward note for a future L3
  pass; `plane-rotation-stream.md:21-23` corroborates the replay-chain claim. Recorded for the L3 author;
  nothing to audit here.

- **Nothing un-auditable.** Every cited range resolved to the correct on-disk file and the correct token;
  no range was out-of-bounds, mis-filed, or runtime-state-dependent. The audit is complete and clean.
