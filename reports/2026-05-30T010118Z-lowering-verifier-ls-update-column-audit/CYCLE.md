---
agent: lowering-verifier
invoked_at: 2026-05-30T010118Z
scope: L1 leaf audit — ls_update_column (cycle-030 dispatch-3)
status: integrated
integrated_at: 2026-05-30T050000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: Applied clean as report-4 of cycle-030; appended SECOND `verified_against:` block (25 rows, all supports, independent-verifier round) at `book/src/L1/ls-update-column.md:718-808`; dual-block convention with c029 21-row producer self-verify block at `:630-716` operating as designed; leaf stays firm. Paraphrase observation (firm-chapter-prose-cites-paraphrased-name-not-literal-anchor) recorded for batch-8 meta. See `reports/cycle-030-integrator-staging/STAGING.md` row 4 + `log/cycle-30.md` HEADLINE 2.
inputs:
  - book/src/L1/ls-update-column.md (the L1 leaf to audit; firm cycle-029 dispatch-5)
  - book/src/L1/back_solve.md (firm sibling leaf, cohort cross-check; firm cycle-027)
  - palace/linalg/iterative.cpp:634-640 (GMRES per-column running-QR)
  - palace/linalg/iterative.cpp:813-819 (FGMRES per-column running-QR; line-for-line identical)
  - palace/linalg/iterative.cpp:73-118 (GeneratePlaneRotation real+complex)
  - palace/linalg/iterative.cpp:227-241 (ApplyPlaneRotation real+complex)
  - palace/linalg/iterative.hpp:193-194 (register element-type split)
  - book/src/L2-L1/incremental-least-squares-composition-lowering.md:502-546 (parent verified_against block for inherited rows)
  - reports/2026-05-29T205945Z-harvester-ls-update-column-leaf/CYCLE.md (cycle-029 dispatch-5 harvester context)
---

# CYCLE: Audit ls_update_column (L1 leaf, cycle-029 firm landing)

## Summary

Per-line `verified_against:` audit of the firm L1 leaf `ls_update_column`
(`book/src/L1/ls-update-column.md`, landed firm cycle-029 dispatch-5, integration
commit `e44896d`). The leaf names the GMRES/FGMRES per-column running-QR update
(replay-stored-rotations / generate-new-rotation / apply-to-column /
apply-to-RHS) — the **column-streaming producer** sibling of the firm terminal
`back_solve` (cycle-027). **Verdict: fully-supported.** Every cited L0 anchor
is independently `citecheck --anchor` zero-drift on-disk (16/16 source anchors,
13/13 cross-reference book anchors, 40/40 via `--scan`). The two critical
load-bearing claims this audit was tasked to assess — (a) replay-non-commutativity
is a **structural law in exact arithmetic** (not merely a finite-precision
non-law) and (b) residual exposure is a **unitary byproduct** (`β = |s[j+1]|`
without an explicit residual evaluation) — both hold: (a) is mathematically
correct because Givens rotations on adjacent overlapping coordinate pairs
`(k, k+1)` and `(k+1, k+2)` share row `k+1` and therefore do NOT commute as
matrix products even in exact arithmetic; (b) is the standard GMRES
least-squares residual identity following from `cs²+|sn|²=1` (`iterative.cpp:118`
comment, the LAPACK c/zlartg contract) and 2-norm preservation under unitary
transforms. The leaf cleanly separates this **structural-law** non-commutativity
from the distinct **finite-precision** non-law on the replay chain (the
"approximately-commute" case yielding bit-different results). The
`back_solve` ↔ `ls_update_column` distinction (terminal-solve vs
per-column-update; producer/consumer split) is preserved in both directions
(this leaf and the c027 sibling). The firm-on-positive-structure judgment
(missing dedicated GMRES unit test does NOT gate syntactic-identity laws —
the `apply_linop` / `lu_solve` / `back_solve` precedent, per CLAUDE.md
status-tier guidance) holds. No corrections needed; the cycle-030 audit row
appended via the proposed-changes fence below preserves the c029 harvester
self-verify block and extends it with an independent verifier line per row.

## Per-citation audit

(Source anchors first, all `citecheck --anchor` confirmed on-disk; then
in-book cross-references.)

### L0 — GMRES per-column block (the primary L0 site)

- **Citation**: `palace/linalg/iterative.cpp:634`
  - **Theme claim**: GMRES replay loop header `for (int k = 0; k < j; k++)`;
    strictly-ordered k=0..j-1; skip-replay-for-j=0 boundary (law 5).
  - **Found**: line 634 reads `for (int k = 0; k < j; k++)` exactly. j=0
    skips body trivially (loop condition false).
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:636`
  - **Theme claim**: replay body `ApplyPlaneRotation(Hj[k], Hj[k+1], cs[k],
    sn[k]);` — each stored rotation k applied in-place to pair `(Hj[k], Hj[k+1])`.
  - **Found**: line 636 reads exactly that. Rotation k acts on the
    `(k, k+1)` row pair — overlapping with rotation k+1 acting on `(k+1, k+2)`.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:638`
  - **Theme claim**: generate `GeneratePlaneRotation(Hj[j], Hj[j+1], cs[j],
    sn[j]);` — produces the new rotation annihilating sub-diagonal `Hj[j+1]`
    against `Hj[j]`.
  - **Found**: line 638 reads exactly that. The generate-contract (per the
    LAPACK c/zlartg comment at :115-118) produces `(cs, sn)` such that the
    rotation maps `[dx; dy] → [r; 0]`.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:639`
  - **Theme claim**: column-apply `ApplyPlaneRotation(Hj[j], Hj[j+1], cs[j],
    sn[j]);` — writes `Hj[j+1] := 0` exactly (law 1 defining contract).
  - **Found**: line 639 reads exactly that. Applying the just-generated
    rotation to its own annihilation pair zeros the sub-diagonal by
    construction.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:640`
  - **Theme claim**: RHS-apply `ApplyPlaneRotation(s[j], s[j+1], cs[j],
    sn[j]);` — same rotation propagated to RHS pair; concentrates residual in
    `s[j+1]` tail (law 3).
  - **Found**: line 640 reads exactly that. With `s[j+1] = 0` on entry (RHS
    initialised as `β₀·e_1` per `:612`), the apply yields
    `(s_j, s_{j+1}) = (cs_j · s[j], -conj(sn_j) · s[j])` — the residual
    falls into the new tail as a unitary byproduct.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:642`
  - **Theme claim**: residual exposure `beta = std::abs(s[j+1])` — byproduct
    read without explicit residual evaluation; the load-bearing property the
    running-QR exists for (law 3).
  - **Found**: line 642 reads exactly `beta = std::abs(s[j + 1]);`. The
    convergence test at `:644` reads it directly as `converged = (beta < eps)`.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:629-632`
  - **Theme claim**: upstream orthogonalize + nrm2 `Hj[j+1] = Norml2(comm, w)`
    producing `h_new[j+1]`; NOT part of this leaf — grounds upstream boundary.
  - **Found**: line 631 reads exactly `Hj[j + 1] = linalg::Norml2(comm, w);`.
    Upstream of the per-column-update block (which begins :634); correctly
    marked as out-of-scope of this leaf.
  - **Verdict**: supports.

### L0 — FGMRES per-column block (line-for-line identical to GMRES)

- **Citation**: `palace/linalg/iterative.cpp:813-819`
  - **Theme claim**: FGMRES per-column running-QR; line-for-line identical
    to GMRES `:634-640` (law 6 basis-lift independence).
  - **Found**: `diff` of lines 634-640 vs lines 813-819 returns **zero
    bytes** — the two blocks are byte-identical. citecheck anchor scan on
    range :813-819 finds `ApplyPlaneRotation` at :815, :818, :819 and
    `GeneratePlaneRotation` at :817 — the same per-line layout as the GMRES
    twin.
  - **Verdict**: supports (and stronger than claimed — byte-identical, not
    just line-for-line).

- **Citation**: `palace/linalg/iterative.cpp:821`
  - **Theme claim**: FGMRES residual exposure `beta = std::abs(s[j+1])` —
    identical to GMRES `:642`.
  - **Found**: line 821 reads exactly `beta = std::abs(s[j + 1]);`.
  - **Verdict**: supports.

### L0 — scalar Givens kernels (inherited from parent L2>L1 theme verified_against)

- **Citation**: `palace/linalg/iterative.cpp:73-108`
  - **Theme claim**: real `GeneratePlaneRotation` kernel; LAPACK-style scaled
    rotation generator; overflow/underflow scaling at :101-108.
  - **Found**: signature `inline void GeneratePlaneRotation(const T dx,
    const T dy, T &cs, T &sn)` at line 73; rescue branches dy==0 / dx==0 at
    :80-91; main branch at :94-98; the safmin/safmax scaled-rescue branch at
    :101-108 (literal `safmin` at :102).
  - **Verdict**: supports (independently citecheck-confirmed beyond the
    inherited row; not a transcription).

- **Citation**: `palace/linalg/iterative.cpp:112-118`
  - **Theme claim**: complex `GeneratePlaneRotation`; in-comment unitarity
    contract `cs² + |sn|² = 1` at :118 (underwrites law 4).
  - **Found**: signature
    `inline void GeneratePlaneRotation(const std::complex<T> dx, const
    std::complex<T> dy, T &cs, std::complex<T> &sn)` at :112-113; the
    [cs sn; -conj(sn) cs] matrix-form comment :115-117; literal "cs is real
    and cs² + |sn|² = 1" at line 118. The unitarity contract is in the
    COMMENT, not in code — but the comment IS the algebraic spec the LAPACK
    c/zlartg implements (and what the L1 leaf law 4 inherits).
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:227-241`
  - **Theme claim**: `ApplyPlaneRotation` real `:227` + complex `:235`;
    body `(dx', dy') = (cs·dx + sn·dy, -conj(sn)·dx + cs·dy)` (complex; real
    drops conj).
  - **Found**: real signature at :227; body :229-231 reads
    `t = cs*dx + sn*dy; dy = -sn*dx + cs*dy; dx = t;` exactly. Complex
    signature at :235-236; body :238-240 reads
    `t = cs*dx + sn*dy; dy = -std::conj(sn)*dx + cs*dy; dx = t;` exactly.
    The leaf's notation `s̄n = conj(sn) complex` (the inline parenthetical
    at line 115 of the leaf) correctly handles both cases.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:612`
  - **Theme claim**: RHS initialisation `s[0] = beta` — the `s = β₀·e_1`
    restart-cycle seed.
  - **Found**: line 612 reads exactly `s[0] = beta;`. Combined with the
    register's per-restart zero-initialisation, this gives `s[0] = β₀` and
    `s[k] = 0` for k ≥ 1 — the law-5 boundary precondition.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:644`
  - **Theme claim**: convergence test `converged = (beta < eps);` — reads
    law-3 byproduct directly.
  - **Found**: line 644 reads exactly that. Bounds when the outer loop exits
    before the next call.
  - **Verdict**: supports.

### L0 — register declarations (the element-type axis)

- **Citation**: `palace/linalg/iterative.hpp:193`
  - **Theme claim**: `mutable std::vector<ScalarType> s, sn;` — grounds s/sn
    element type as ScalarType (law 7).
  - **Found**: line 193 reads exactly that. Combined with `H` also ScalarType
    at :192, this establishes the complex-or-real-ness of the Hessenberg
    register + rotation sine + RHS.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.hpp:194`
  - **Theme claim**: `mutable std::vector<RealType> cs;` — cosine register
    always real (underwrites law 4 `cs² + |sn|² = 1` since cs:Real).
  - **Found**: line 194 reads exactly that.
  - **Verdict**: supports.

### In-book cross-references

- **Citation**: `book/src/L2/incremental-least-squares.md`
  - **Theme claim**: parent L2 named composition (firm cycle-026); this leaf
    is its Face-1 single-column projection.
  - **Found**: file exists; status firm cycle-026 confirmed by integrator
    metadata. The leaf's slug appears in the L2 entry's signature (`back_solve`
    at :81-83, `ls_update_column` at :412 — distinct).
  - **Verdict**: supports.

- **Citation**: `book/src/L2/incremental-least-squares.md:81-83` (referenced
  via the inheritance chain through back_solve.md and via the leaf's L2-laws
  mapping)
  - **Theme claim**: L2 terminal `back_solve` projection.
  - **Found**: anchor `back_solve` at line 83 within range — supports.
  - **Verdict**: supports.

- **Citation**: `book/src/L2/incremental-least-squares.md:225-232` (residual-
  exposure law, inherited via back_solve.md)
  - **Theme claim**: L2 residual-exposure law underwriting leaf law 3.
  - **Found**: anchor `residual` at lines 226, 231 within range. Semantically
    the L2 law 1.
  - **Verdict**: supports.

- **Citation**: `book/src/L2/incremental-least-squares.md:278-285`
  (rotation-stream non-associativity reference, inherited via back_solve.md
  context)
  - **Theme claim**: rotation-stream non-associativity non-law the leaf's
    reduction-order non-law composes with.
  - **Found**: lines 278-285 contain the **"Rotation-stream associativity /
    re-factorisation equivalence at the bit level"** non-law bullet. The
    leaf's prose paraphrases this as "non-associativity non-law" — the
    literal token `non-associativity` does NOT appear at :278-285 (it
    appears at line 339, in a downstream forward-reference summary). The
    citation `:278-285` is **semantically correct** (it IS the right non-law);
    the leaf uses a shorter paraphrase nickname. Not a drift; a paraphrase.
  - **Verdict**: supports (semantic match; paraphrase noted).

- **Citation**: `book/src/L2-L1/incremental-least-squares-composition-lowering.md`
  - **Theme claim**: parent L2>L1 theme (firm cycle-028); Face-1 forward-ref
    at :67-90 + speculative-L1 entry :307-310 resolved by this leaf; theme's
    Face-1 plain-text ref upgradable post-integration.
  - **Found**: file exists; firm cycle-028 confirmed; Face-1 region at :87-88
    (anchor `Face` at :88); speculative-L1 region at :307-310 (anchor
    `ls_update_column` at :307). The leaf indeed resolves these.
  - **Verdict**: supports.

- **Citation**: `book/src/L1/back_solve.md`
  - **Theme claim**: firm sibling leaf (cycle-027); structural template +
    slug-naming precedent (back_solve ≠ general trsv; ls_update_column ≠
    back_solve).
  - **Found**: file exists; status firm cycle-027 confirmed. The :30-34
    region contains the **distinction passage** (literal "DISTINCT" at :32):
    "the slug `ls_update_column` at L2/...:412 and concepts/...:14 names the
    DISTINCT per-column streaming update step ... not this terminal
    back-solve". The c027 entry's preservation of the distinction is
    bidirectional with this leaf — no conflation in either direction.
  - **Verdict**: supports.

- **Citation**: `book/src/concepts/incremental-least-squares.md:14`
  - **Theme claim**: `ls_update_column` slug contract.
  - **Found**: anchor `ls_update_column` at line 14 within range. The
    contract `ls_update_column(K, j, h_new) → K'` is bound here.
  - **Verdict**: supports.

- **Citation**: `book/src/concepts/incremental-least-squares.md:22-27`
  - **Theme claim**: "What is hidden at L1" list characterising the leaf's
    hiding boundary.
  - **Found**: anchor `hidden` at line 22 within range. The list correctly
    characterises the four sub-steps the leaf hides.
  - **Verdict**: supports.

- **Citation**: `book/src/concepts/plane-rotation-stream.md:21-23`
  - **Theme claim**: §"Sequential character" flagging replay chain as
    sequential-obstruction candidate at L3.
  - **Found**: anchor `Sequential` at line 21 within range.
  - **Verdict**: supports.

## Applicability conditions

- **Condition**: `R` (the running R-factor under construction) is built
  upper-triangular by this leaf via the generate-then-apply sub-diagonal
  annihilation; non-singularity holds unless Arnoldi breaks down
  (lucky-breakdown / exact-convergence).
  - **Verifiable**: yes; the law 1 defining contract `h_out[j+1] = 0` is the
    direct algebraic consequence of `:638`+`:639` (generate-then-apply on
    same pair). Non-singularity is the upstream boundary (Palace's residual
    test at `:644` exits before the next call in the breakdown case).
  - **Found counter-example?**: no.

- **Condition**: `j < max_dim` — the leaf is not invoked at j=max_dim
  (the restart bound).
  - **Verifiable**: yes; the outer loop condition at iterative.cpp:617-ish
    bounds j strictly below max_dim. The leaf's prose accurately states
    "**not invoked at j = m**" (line 156).
  - **Found counter-example?**: no.

- **Condition**: `s[j+1] = 0` on entry (the RHS tail not yet touched).
  - **Verifiable**: yes; `s[0] = beta` at :612, and the inner loop's prior
    iterations only touch `s[0..j]` (each prior call apply-RHS on
    `(s[k], s[k+1])` for some smaller k). Entry-time `s[j+1] = 0` holds by
    induction.
  - **Found counter-example?**: no.

- **Condition**: The rotation `(cs, sn)` generated at `:638` satisfies
  `cs² + |sn|² = 1` (unitarity contract, law 4).
  - **Verifiable**: yes; the literal contract is in the comment at :118 for
    the complex kernel ("cs is real and cs² + |sn|² = 1"); the real kernel
    at :73-108 implements the same contract via the LAPACK-scaled rotation
    formula.
  - **Found counter-example?**: no.

## Algebraic laws

The 7 laws below are positively-anchored syntactic identities on positive
Palace source — the firm-on-positive-structure precedent.

- **Law 1: Sub-diagonal annihilation** (`h_out[j+1] = 0` exactly).
  - **Holds on operators?**: yes. The generate-contract at :118 +
    apply-immediately-on-same-pair at :639 makes the annihilation a
    construction-by-definition identity.
- **Law 2: Replay non-commutativity** (structural law — different rotation
  product Q'_j ≠ Q_j in exact arithmetic for reordered replay).
  - **Holds on operators?**: yes — and this is the critical claim the audit
    was asked to scrutinise. Givens rotations on **overlapping adjacent
    coordinate pairs** (`(k, k+1)` and `(k+1, k+2)`) share row k+1 and so
    do NOT commute as matrix products even in exact arithmetic. The leaf
    correctly classifies this as a STRUCTURAL law (the rotation product
    itself is order-sensitive in exact arithmetic), not a finite-precision
    artefact. It cleanly separates this from the distinct finite-precision
    non-law on the replay chain (the bit-level "approximately-commute"
    case yielding bit-different results — recorded as the first non-law
    at lines 322-330). Both classifications are correct.
- **Law 3: Residual exposure** (`beta = |s_{j+1}|` = LS-residual norm
  exactly).
  - **Holds on operators?**: yes — and this is the second critical claim.
    Follows from (i) unitarity of `Q_j` (cs²+|sn|²=1 contract at :118 +
    LAPACK c/zlartg implementation at :73-108 / :112-118); (ii) 2-norm
    preservation under unitary transforms; (iii) the upper-triangular
    structure of `Q_j · H̄_j` localising the residual to the last entry.
    Standard GMRES least-squares residual identity.
- **Law 4: Unitarity preservation across the call**
  (`|s_j|² + |s_{j+1}|² = |s[j]|²` on s[j+1]=0 entry).
  - **Holds on operators?**: yes; algebraic consequence of `cs²+|sn|²=1`
    applied to a 2-vector with one zero entry.
- **Law 5: Empty / first-column boundary** (j=0 skip-replay).
  - **Holds on operators?**: yes; the `for (int k = 0; k < j; k++)` at :634
    with j=0 trivially skips the body. Laws 1, 3, 4 reduce cleanly to the
    single-rotation case.
- **Law 6: Basis-lift independence** (GMRES ≡ FGMRES at this leaf).
  - **Holds on operators?**: yes — independently confirmed STRONGER than
    claimed: `diff` of :634-640 vs :813-819 is byte-zero (not just
    line-for-line, byte-identical).
- **Law 7: Per-call scalar-kernel-variant invariance** (real/complex
  parametric absorption).
  - **Holds on operators?**: yes; the same sub-step sequence dispatches
    uniformly to the appropriate kernel pair (real :73,:227 vs complex
    :112,:235), no per-call branching, fixed at solver instantiation.

The recorded non-laws (lines 320-354 of the leaf) are also correctly
classified:
- **Non-law: bit-level reduction-order independence** — distinct from law 2;
  this is the FP-summation-order non-law on the replay chain (recorded so
  callers don't treat replay order as a free choice even where rotations
  approximately commute).
- **Non-law: per-column call-sequence commutativity** — correctly recorded:
  the (j=i+1) call reads the i-th rotation written by the (j=i) call;
  left-fold-only.
- **Non-law: definedness at (h1[j], h1[j+1]) = (0,0)** — the
  Arnoldi-lucky-breakdown applicability boundary.
- **Non-law: residual-by-shortcut avoidance** — correctly classified
  load-bearing (the residual exposure is NOT a transparent reorder).

## Proposed changes

The cycle-029 dispatch-5 harvester already authored a `verified_against:`
block (lines 631-715 of the leaf), populated via citecheck self-verify. Per
the friction-ledger `producer-citation-drift-verify-not-self-invoked` entry
and the recurrence-4 division of labour (producer self-verify ≠ independent
lowering-verifier audit), this cycle-030 audit records its own per-line
verifier rows. Append the following block AFTER the existing
`verified_against:` block (after line 716, the closing fence of the
existing block).

```edit:book/src/L1/ls-update-column.md
[append at end of file]
```yaml
verified_against:
  # cycle-030 dispatch-3 lowering-verifier independent audit (separate
  # invocation from the cycle-029 dispatch-5 harvester self-verify above).
  - citation: palace/linalg/iterative.cpp:634
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'for (int k = 0; k < j' zero-drift on-disk; reads exactly the replay loop header; law 2 and law 5 (skip-replay-for-j=0) both witnessed.
  - citation: palace/linalg/iterative.cpp:636
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'ApplyPlaneRotation(Hj[k]' zero-drift; replay body in-place pair update; rotation k acts on overlapping pair (k, k+1).
  - citation: palace/linalg/iterative.cpp:638
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'GeneratePlaneRotation(Hj[j]' zero-drift; generate-contract per LAPACK c/zlartg comment :115-118.
  - citation: palace/linalg/iterative.cpp:639
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'ApplyPlaneRotation(Hj[j]' zero-drift; apply-on-just-generated-pair zeros Hj[j+1] by construction (law 1 definitional).
  - citation: palace/linalg/iterative.cpp:640
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'ApplyPlaneRotation(s[j]' zero-drift; RHS-apply concentrates residual in s[j+1] tail since s[j+1]=0 on entry (law 3).
  - citation: palace/linalg/iterative.cpp:642
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'beta = std::abs' zero-drift; residual exposure read without explicit residual eval (law 3 load-bearing byproduct).
  - citation: palace/linalg/iterative.cpp:629-632
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'Norml2' zero-drift; upstream nrm2 producing h_new[j+1] sub-diagonal entry; correctly out-of-scope of this leaf.
  - citation: palace/linalg/iterative.cpp:813-819
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent verify STRONGER than claimed — diff of :634-640 vs :813-819 returns ZERO bytes (byte-identical, not just line-for-line); law 6 GMRES≡FGMRES at this leaf fully grounded.
  - citation: palace/linalg/iterative.cpp:821
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'beta = std::abs' zero-drift; FGMRES residual exposure identical to GMRES :642.
  - citation: palace/linalg/iterative.cpp:73-108
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independently re-read on-disk (not transcribed from parent theme); real GeneratePlaneRotation signature :73, dy=0/dx=0 rescues :80-91, main branch :94-98, safmin/safmax scaled-rescue :101-108; literal 'safmin' at :102.
  - citation: palace/linalg/iterative.cpp:112-118
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independently re-read on-disk; complex GeneratePlaneRotation signature :112-113, matrix-form comment :115-117, unitarity contract literal 'cs is real and cs² + |sn|² = 1' at :118 (LAPACK c/zlartg spec).
  - citation: palace/linalg/iterative.cpp:227-241
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independently re-read; real ApplyPlaneRotation signature :227 body :229-231 (no conj — real is own conjugate); complex signature :235-236 body :238-240 (explicit std::conj(sn) at :239); leaf's s̄n=conj(sn)-complex notation correct.
  - citation: palace/linalg/iterative.cpp:612
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor exact; s[0]=beta restart-cycle RHS seed; s[k]=0 for k≥1 by inductive register zero-init underwrites law-5 entry precondition.
  - citation: palace/linalg/iterative.cpp:644
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'converged = (beta < eps)' exact; convergence test reads law-3 byproduct directly.
  - citation: palace/linalg/iterative.hpp:193
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'ScalarType> s, sn' zero-drift; H also ScalarType at :192 (the leaf does not separately cite :192 but the register triple is consistent); law 7 element-type axis grounded.
  - citation: palace/linalg/iterative.hpp:194
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'RealType> cs' zero-drift; cs always-Real underwrites the law-4 cs²+|sn|²=1 contract (the cs:Real assumption is load-bearing).
  - citation: book/src/L2/incremental-least-squares.md:81-83
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'back_solve' at :83; the parent L2 terminal back_solve projection (NOT this leaf — this leaf is the column-streaming sibling); naming distinction preserved.
  - citation: book/src/L2/incremental-least-squares.md:225-232
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'residual' at :226/:231 within range; L2 residual-exposure law underwriting leaf law 3.
  - citation: book/src/L2/incremental-least-squares.md:278-285
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'Rotation-stream associativity' at :278 exact; semantically the rotation-stream bit-level non-associativity non-law (literal 'non-associativity' token is at :339 in a downstream summary; the cite :278-285 IS the right region; leaf prose uses a shorter paraphrase nickname); supports — not a drift.
  - citation: book/src/L2-L1/incremental-least-squares-composition-lowering.md:87-88
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'Face' at :88; the Face-1 forward-ref region this leaf resolves; theme's plain-text ref upgradable post-integration.
  - citation: book/src/L2-L1/incremental-least-squares-composition-lowering.md:307-310
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'ls_update_column' at :307; the speculative-L1 entry resolved by this leaf landing firm.
  - citation: book/src/L1/back_solve.md:30-34
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'DISTINCT' at :32; the c027 sibling's naming-distinction passage (back_solve ≠ ls_update_column); bidirectional preservation confirmed — neither leaf conflates with the other.
  - citation: book/src/concepts/incremental-least-squares.md:14
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'ls_update_column' at :14; the slug contract `ls_update_column(K, j, h_new) → K'`.
  - citation: book/src/concepts/incremental-least-squares.md:22-27
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'hidden' at :22; the 'What is hidden at L1' list correctly characterises the four sub-steps.
  - citation: book/src/concepts/plane-rotation-stream.md:21-23
    verdict: supports
    audited_at: 2026-05-30T010118Z
    note: independent citecheck --anchor 'Sequential' at :21; the L3 sequential-obstruction-candidate forward note.
```
```

(The append lands the new block as a SECOND fenced YAML body inside the leaf
file, immediately after the cycle-029 harvester's block. The
`cross-layer-cross-cutter` coverage tool consumes both blocks indifferently
— it scans all `verified_against:` keys per file. The two blocks together
record the producer self-verify and the independent verifier audit as
distinct rounds. No row in the existing block needs to be edited; this audit
neither contradicts nor refines any prior verdict — it independently
ratifies them.)

## Supporting evidence

- `reference/palace/palace/linalg/iterative.cpp:625-650` — the GMRES inner
  loop including the per-column-update block; read directly on-disk via the
  Read tool (NOT via codemap, per the cycle-027 codemap+1-drift cautionary
  observation in the role-spec, even though this region is not in the
  +1-brace zone).
- `reference/palace/palace/linalg/iterative.cpp:805-829` — the FGMRES inner
  loop twin; read directly on-disk; diff of the two per-column-update blocks
  confirmed byte-identical via shell diff.
- `reference/palace/palace/linalg/iterative.cpp:70-241` — the four
  Givens scalar kernels read on-disk: `GeneratePlaneRotation` real
  :73-108, complex :112-118; `ApplyPlaneRotation` real :227-232, complex
  :235-241; with the unitarity contract comment at :115-118.
- `reference/palace/palace/linalg/iterative.hpp:188-200` — the register
  declarations read on-disk: `H`/`s`/`sn` ScalarType, `cs` RealType.
- `tools/citecheck/citecheck.py --scan book/src/L1/ls-update-column.md` —
  40/40 citations bounds-OK, 0 failing.
- `tools/citecheck/citecheck.py --anchor ...` — 16/16 source anchors
  zero-drift, 13/13 in-book cross-reference anchors all OK or paraphrase-OK
  (one paraphrase case: `:278-285` literal `non-associativity` vs prose
  nickname — semantically correct, not a drift).

## Open questions / caveats

- **Paraphrase pattern for the L2 non-law nickname**: the leaf references
  `book/src/L2/incremental-least-squares.md:278-285` as the
  "rotation-stream non-associativity non-law" — semantically correct, the
  cited range IS that non-law, but the LITERAL token `non-associativity`
  appears at :339 (a downstream forward-reference summary), not in the
  cited range. The citation is fine and the paraphrase is fair; recording
  the pattern only so that a future critic running anchor-scans on the
  literal token does not flag it as a drift. (Cycle-021 friction-ledger
  bullet `firm-chapter-prose-cites-paraphrased-name-not-literal-anchor`
  is the latent home; not promoted because it is per-cycle paraphrase
  judgment, not a generic mechanical issue.) No corrective action; this
  caveat is informational.

- **The cycle-029 harvester's self-verify rows already populate the
  `verified_against:` block.** This audit independently re-runs the same
  citecheck commands and reads the source on-disk — not transcribing the
  harvester's "self-verified" labels but re-establishing each anchor from
  scratch. The new appended block (proposed-changes above) is therefore
  the **independent verifier round**, distinct from the producer self-
  verify round. Both rounds support every cited anchor. The CYCLE.md /
  cross-layer-cross-cutter parser will count both rounds and the per-row
  audit timestamps make the chain auditable.

- **No firm-status flip is gated by this audit.** The leaf was landed
  firm at cycle-029; this is a verification round only, not a promotion.
  No status-line edit is proposed.

- **The forthcoming `ls-update-column-mutation-rotation` L1>L0 theme** is
  the natural next dispatch target (sibling to `back-solve-mutation-rotation`
  and `orthogonalize-mutation-rotation`); this audit does not enter that
  territory — the L1>L0 in-place mechanics (the four reference-update
  `*PlaneRotation` calls, the `Hj` column-pointer arithmetic, the flat
  Hessenberg-register stride) are explicitly deferred by the leaf's prose
  to that theme. Recording so the cycle-030+ planner has the next-up
  trigger visible.
