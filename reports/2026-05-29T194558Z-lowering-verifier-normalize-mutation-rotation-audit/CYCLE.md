---
agent: lowering-verifier
invoked_at: 2026-05-29T19:45:58Z
scope: L1>L0 theme audit — normalize-mutation-rotation
status: integrated
integrated_at: 2026-05-29T205500Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-028 position 3/7 (per-report). Additive verified_against: audit of the firm L1>L0 normalize-mutation-rotation theme (landed c027 D1). UPHELD firm — 16-row yaml block (14 supports / 1 partially-supports / 1 does-not-support) + a :811→:810-811 second-GMRES-path citation-range parity fix at three occurrences. The 1 does-not-support row (F1: defined-but-uncalled fused Normalize(comm,x,B,Bx) at palace/linalg/operator.hpp:377-384 contradicts the theme's 'no fused B-Normalize' prose) recorded inline but the prose correction ROUTED to follow-up abstractor OQ normalize_B-note-says-no-fused-B-Normalize-but-uncalled-fused-operator-exists (substantive, exceeds integrator mechanical bar). Firm core UNAFFECTED; §Status untouched. Build clean (yaml fence balanced, zero build-repairs)."
inputs:
  - book/src/L1-L0/normalize-mutation-rotation.md (the firm theme under audit, landed c027 D1)
  - book/src/L1/normalize.md (the firm L1 operator, landed c026)
  - palace/linalg/vector.hpp:262-270 (linalg::Normalize positive source)
  - palace/linalg/iterative.cpp:631-632,810-811 (GMRES Arnoldi consumer)
  - palace/linalg/operator.cpp:660-661,673,676 (power-iteration consumer)
  - palace/linalg/nleps.cpp:610-611,617 (NEP deflation consumer)
  - palace/linalg/operator.hpp:377-384 (B-weighted fused Normalize — cohort-completeness finding)
  - reports/2026-05-29T175529Z-abstractor-normalize-rotation/CYCLE.md (the authoring report)
---

# CYCLE: Audit normalize-mutation-rotation

## Summary

Audited the firm L1>L0 `normalize-mutation-rotation` theme (landed firm cycle-027
dispatch-1) against its cited L0 evidence. **Top-level verdict: fully-supported on its
firm core** (the unweighted-normalise lowering `(β, û) = normalize(x)` → L0
`linalg::Normalize(comm, x)`), with **two refinement findings on the non-core
`normalize_B` rough-in note** and **one citation-precision nudge on the second GMRES
path**. Every one of the theme's 42 `path:lo-hi` citations is in-bounds (`citecheck
--scan` clean, exit 0); every load-bearing anchor lands **exactly** on-disk via
`citecheck --anchor` with **zero codemap drift** in this theme. The four-step L0
composition (reduction → guard → in-place rescale → returned norm) is read verbatim off
`vector.hpp:262-270`; the partiality guard `MFEM_ASSERT(norm > 0.0)` is positively
anchored at `:267`; the three load-bearing returned-norm consumer shapes (GMRES
Hessenberg, power-iteration eigenvalue, NEP deflation companion-scale) are all confirmed
semantically. The firm `firm` status is **upheld** — the firm core needs no status change.

The two findings touch only the `normalize_B` rough-in NOTE (not the firm claim):
**(F1)** the theme asserts "Palace has **no** `linalg::Normalize`-with-`B` free function"
(lines 285-287, 51, 311-313), but a fused B-weighted `Normalize(comm, x, B, Bx)`
**definition DOES exist** at `operator.hpp:377-384` — structurally identical to the
unweighted one. The theme is **internally inconsistent**: it cites that very range
(`operator.hpp:377-384`, lines 290-293) as the weighted-`Normalize` consumer while
elsewhere denying the free function exists. The theme's deeper point survives — that fused
B-`Normalize` is **uncalled** (no rescaling callsite; grep finds zero 4-arg invocations),
so there is no live B-weighted-normalise *callsite* — but the phrasing overstates and needs
a precision fix. **(F2)** the returned-norm consumer cohort is **larger than the cited
illustrative set** (the report flagged this as an Open question); nleps.cpp carries five
more invariant-pair companion-scale instances (`488-494,544-545,697-698,738-739`) of the
SAME Sub-pattern C shape — confirming the "no fourth shape" claim while showing the cited
`610-611,617` is illustrative not exhaustive. **(F3, minor)** the second GMRES path is
cited at `:811` but described as the full two-line `Hj[j+1]=Norml2; w*=...` shape, which is
`810-811` (`:811` is only the rescale half). All three are routed as proposed refinements;
none reduces the firm status of the unweighted-normalise core.

## Per-citation audit

### Firm-core L0 positive source

- **Citation**: `palace/linalg/vector.hpp:262-270`
  - **Theme claim**: the `linalg::Normalize(comm, x)` template — four-step composition
    `auto norm = Norml2(comm, x); MFEM_ASSERT(norm > 0.0, ...); x *= 1.0 / norm; return norm;`
    — is the positive source the L1 `normalize` lowers into; def at `:264`, reduction
    binding `:266`, guard `:267`, rescale `:268`, return `:269`.
  - **Found**: read verbatim. `:262` header comment ("possibly with respect to an SPD
    matrix B"); `:264` `inline auto Normalize(MPI_Comm comm, VecType &x)`; `:266` `auto
    norm = Norml2(comm, x);`; `:267` `MFEM_ASSERT(norm > 0.0, "Zero vector norm in
    normalization!");`; `:268` `x *= 1.0 / norm;`; `:269` `return norm;`. All five
    `--anchor` probes land at exactly the claimed lines.
  - **Verdict**: **supports**.
  - **Notes**: zero drift. Read-tool on-disk and `citecheck` on-disk agree; the codemap
    `read_range` +1 brace-boundary hazard does NOT affect this range (the report's own
    cross-check noted the same).

- **Citation**: `palace/linalg/vector.hpp:259`
  - **Theme claim**: `Norml2` body `std::sqrt(std::abs(Dot(comm, x, x)))` — the reduction
    chain Sub-pattern A inherits from `nrm2-mutation-rotation`.
  - **Found**: `:259` `return std::sqrt(std::abs(Dot(comm, x, x)));` exactly. `--anchor`
    lands at 259.
  - **Verdict**: **supports** (inherited boundary, correctly marked `[inherited]`).

### Sub-pattern C consumer cohort (load-bearing returned norm)

- **Citation**: `palace/linalg/iterative.cpp:631-632`
  - **Theme claim**: GMRES Arnoldi — `Hj[j + 1] = linalg::Norml2(comm, w); w *= 1.0 /
    Hj[j + 1];` — β stored as Hessenberg sub-diagonal AND used as rescale divisor; both
    outputs consumed; β feeds the plane-rotation solve at `:636-639`.
  - **Found**: `:631` `Hj[j + 1] = linalg::Norml2(comm, w);`, `:632` `w *= 1.0 / Hj[j +
    1];` exactly. `:636` `ApplyPlaneRotation(...)`, `:638` `GeneratePlaneRotation(...)` —
    the plane-rotation (Givens) least-squares confirmed at the cited `:636-639` range
    (`--anchor 'GeneratePlaneRotation'` → 638). The descriptive word "Givens" is not a
    literal token in the source but the plane-rotation primitives ARE there.
  - **Verdict**: **supports**.

- **Citation**: `palace/linalg/iterative.cpp:811` (second GMRES path)
  - **Theme claim**: "A second identical GMRES code path is at `iterative.cpp:811`"
    (line 137) / "second analogous GMRES Arnoldi path, identical `w *= 1.0 / Hj[j + 1];`"
    (lines 174-175, 341-342).
  - **Found**: `:811` IS `w *= 1.0 / Hj[j + 1];` exactly (`--anchor` → 811). BUT the full
    two-line shape the prose describes (`Hj[j+1] = linalg::Norml2(comm, w); w *= 1.0 /
    Hj[j + 1];`) spans **`810-811`** — the `Hj[j + 1] = linalg::Norml2` half is at `:810`,
    `:811` is only the rescale.
  - **Verdict**: **partially-supports** (citation in-bounds and the rescale anchor lands;
    but the range under-covers the full two-output shape the prose claims).
  - **Notes**: F3. The first path is cited `631-632` (correct two-line range); the second
    should be `810-811` for parity. Proposed refinement below.

- **Citation**: `palace/linalg/operator.cpp:673` and `:676`
  - **Theme claim**: power iteration — `l = Normalize(comm, u);` (`:673`) the returned
    norm IS the dominant-eigenvalue estimate, consumed by the convergence test
    `res = std::abs(l - l0) / l0;` (`:676`); the renormalised `u` carries to the next
    `A·u` (`:664`).
  - **Found**: `:673` `l = Normalize(comm, u);`, `:676` `res = std::abs(l - l0) / l0;`
    exactly. `:664` `A.Mult(u, v);` confirms the next-iteration carrier. Loop structure
    (660-682) confirms `l` is the working result and `u` is the carrier.
  - **Verdict**: **supports**.

- **Citation**: `palace/linalg/operator.cpp:660-661`
  - **Theme claim**: `SetRandom(comm, u); Normalize(comm, u);` — seed normalise; returned
    norm discarded (the `snd ∘ normalize` unit-vector-only shape).
  - **Found**: `:660` `SetRandom(comm, u);`, `:661` `Normalize(comm, u);` exactly — the
    seed call discards the return (no LHS), matching the projection-shape claim.
  - **Verdict**: **supports**.

- **Citation**: `palace/linalg/nleps.cpp:610-611` and `:617`
  - **Theme claim**: NEP deflation — `const auto scale = linalg::Norml2(GetComm(), v);
    v *= 1.0 / scale;` (`:610-611`) AND `H.col(k).head(k) = v2 / scale;` (`:617`); the
    returned norm `scale` is doubly load-bearing (normalises basis `v` AND rescales
    coordinate companion `v2`).
  - **Found**: `:610` `const auto scale = linalg::Norml2(GetComm(), v);`, `:611` `v *=
    1.0 / scale;`, `:617` `H.col(k).head(k) = v2 / scale;` exactly. The `:609` comment
    "Update the invariant pair with normalization" confirms the doubly-load-bearing
    reading (the invariant pair `(v, v2)` stays consistent under the shared `scale`).
  - **Verdict**: **supports**.

### Cross-theme / L1 / test anchors

- **Citation**: `book/src/L1/normalize.md:50,26,32` (factorisation law 6, partiality
  precondition β > 0, reciprocal-vs-divide note)
  - **Found**: all three anchors land exactly (`Factorisation` → 50; `β > 0` → 26;
    `reciprocal-vs-divide` → 32). The LHS the theme lowers matches the firm L1 signature.
  - **Verdict**: **supports**.

- **Citation**: `book/src/L1-L0/scal-mutation-rotation.md:48-49,55-58` ("names this very
  `Normalize` site")
  - **Found**: `Normalize` token at 48 and 55 within `48-58` — confirms the scal theme
    names the `Normalize` rescale as a Sub-pattern A instance. Inheritance boundary holds.
  - **Verdict**: **supports**.

- **Citation**: `palace/test/unit/test-orthog.cpp:193,208`
  - **Theme claim**: `V[0] *= 1 / v0_norm;` / `V[1] *= 1 / v1_norm;` — by-hand normalise
    (norm asserted, then rescale), empirical-match for the two-output shape.
  - **Found**: `:193` `V[0] *= 1 / v0_norm;`, `:208` `V[1] *= 1 / v1_norm;` exactly.
  - **Verdict**: **supports** (L0-equivalent test evidence; inherited).

- **Citation**: `palace/linalg/operator.cpp:599-619` (and report variants `600-619`,
  `600-607`) — B-weighted `Norml2(comm, x, B, Bx)`
  - **Found**: `:602` `B.Mult(x, Bx);` within range — the B-weighted reduction exists.
    All three range variants in-bounds (file 698 lines).
  - **Verdict**: **supports**, BUT see F1 — this reduction is fused into a B-weighted
    `Normalize` at `operator.hpp:377-384`, which the theme's `normalize_B` note denies.

- **Citation**: `palace/linalg/operator.hpp:377-384` (cited by the theme as the
  weighted-`Normalize` consumer of `matrix-weighted-norm-mutation-rotation`)
  - **Theme claim** (line 290-293): "the `Normalize`-with-`B` *inline* form `x *= 1.0/norm`
    after a weighted `Norml2` IS the consumer Sub-pattern C of
    `matrix-weighted-norm-mutation-rotation` at `palace/linalg/operator.hpp:377-384` — but
    that is the weighted-norm theme's consumer, **not a fused `normalize_B` operator**."
  - **Found**: `operator.hpp:377-384` is `inline double Normalize(MPI_Comm comm, VecType
    &x, const Operator &B, VecType &Bx) { double norm = Norml2(comm, x, B, Bx);
    MFEM_ASSERT(norm > 0.0, ...); x *= 1.0 / norm; return norm; }`. This is a **fused
    free-function `Normalize`-with-`B`** — structurally identical to the unweighted
    `vector.hpp:264` (reduction → guard → rescale → return). The anchor
    `'Normalize(MPI_Comm comm, VecType &x, const Operator &B'` lands at `:378`.
  - **Verdict**: **does-not-support** the surrounding "no fused B-Normalize free function"
    claim — it IS a fused free function, not an inline shape. (The range citation itself is
    correct; the *characterisation* is wrong.)
  - **Notes**: F1. See Applicability / Open-questions. This affects only the `normalize_B`
    rough-in note, not the firm unweighted core.

## Applicability conditions

The theme states four applicability conditions (lines 226-250):

- **Condition 1 — no observer of prior `x` after the call (read-before-write).**
  - **Verifiable**: yes, from the L0 source ordering. `:266` `Norml2(comm, x)` reads prior
    `x`; `:268` `x *= 1.0/norm` overwrites — strict read-then-write within the template
    body. Inherited from `scal-mutation-rotation` cond 1 (element-local rescale).
  - **Found counter-example?**: no.

- **Condition 2 — `x ≠ 0` (partiality).**
  - **Verifiable**: yes. `MFEM_ASSERT(norm > 0.0)` at `:267` is the run-time witness; the
    L1 operator is undefined on the zero vector. Anchor lands at `:267`.
  - **Found counter-example?**: no.

- **Condition 3 — element type real or complex, norm always real.**
  - **Verifiable**: partly — the `VecType`-generic template (`:263-264`) and the real-valued
    `Norml2` output are read off the source; the complex-path `imag(s)==0.0` promotion is
    inherited from `scal-mutation-rotation` Sub-pattern B (not re-read here, correctly
    marked inherited).
  - **Found counter-example?**: no.

- **Condition 4 — single-rank reading of the `MPI_Allreduce` collective.**
  - **Verifiable**: structurally (the collective is inside `Dot`, in scope per CLAUDE.md
    "Scope"); inherited from `nrm2`/`dot`. Not a per-line on-disk check.
  - **Found counter-example?**: N/A (scope decision, not a source claim).

The applicability set is **complete** for the firm unweighted core — it captures the one
semantic addition (partiality) plus the three inherited conditions. No missing condition.

## Algebraic laws (cited)

The theme rests on the L1 factorisation law 6 `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`
(`book/src/L1/normalize.md:50`) and asserts the rewrite is `structural` throughout.

- **Law**: factorisation `normalize(x) = (nrm2(x), scal(1/nrm2(x), x))`.
  - **Holds on operators?**: yes — confirmed against the L0 body: `norm = Norml2(comm, x)`
    realises `nrm2(x)`, `x *= 1.0/norm` realises `scal(1/β, x)`, `return norm` retains the
    `nrm2(x)` component. The fusion is the single-evaluation pairing; no new arithmetic.
- **Law**: partiality (Totality does NOT hold) — `normalize` undefined at `x = 0`.
  - **Holds on operators?**: yes — the divide `1.0/norm` at `norm == 0` is the failure;
    `MFEM_ASSERT(norm > 0.0)` (`:267`) is its positive witness. Correctly classified as a
    domain check (not a no-op, not a load-bearing value-changing trick).
- **Justification-kind ladder** (A structural / B structural+transparent-trick /
  C structural): each step is a syntactic identity on positive source, not a literature
  reconstruction — consistent with `firm` (not `partly-constructive`). The
  reciprocal-vs-divide transparent-trick sub-note (B) is correctly NOT promoted to an L1
  law (`book/src/L1/normalize.md:56` agrees).

All cited laws hold on the operator signatures. No algebraic defect.

## Proposed changes

The audit upholds the firm status of the unweighted-normalise core. The `verified_against:`
block below records the per-citation verdicts. Two refinement edits (F1, F3) are proposed;
F2 is recorded as an Open question (cohort is correctly characterised as "illustrative", so
no edit is forced). **All edits are GATED to a follow-up dispatch** per the dispatch-phase
write-guard — this audit proposes, it does not apply.

### Edit 1 (primary deliverable) — append the `verified_against:` block

```edit:book/src/L1-L0/normalize-mutation-rotation.md
[append at end of file]
~~~yaml
verified_against:
  - citation: palace/linalg/vector.hpp:262-270
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "linalg::Normalize four-step composition read verbatim; def :264, reduction :266, guard :267, rescale :268, return :269 — all anchors land exactly on-disk (zero codemap drift)."
  - citation: palace/linalg/vector.hpp:259
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "Norml2 body std::sqrt(std::abs(Dot(comm,x,x))) — inherited Sub-pattern A boundary; anchor at :259."
  - citation: palace/linalg/vector.hpp:267
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "MFEM_ASSERT(norm > 0.0) partiality witness — positively anchored; the one non-syntactic ingredient; firm not partly-constructive confirmed."
  - citation: palace/linalg/iterative.cpp:631-632
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "GMRES Arnoldi (first path): Hj[j+1]=Norml2 :631, w*=1.0/Hj[j+1] :632; beta feeds plane-rotation solve at :636-639 (GeneratePlaneRotation :638) — Hessenberg sub-diagonal consumer confirmed."
  - citation: palace/linalg/iterative.cpp:811
    verdict: partially-supports
    audited_at: 2026-05-29T19:45:58Z
    note: "Second GMRES path: :811 is the rescale half only (w*=1.0/Hj[j+1]); the full two-line shape the prose describes spans 810-811 (Hj[j+1]=Norml2 at :810). Recommend re-cite 810-811 for parity with the first path. In-bounds; rescale anchor lands at 811."
  - citation: palace/linalg/operator.cpp:660-661
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "Power-iteration seed: SetRandom :660, Normalize :661 (return discarded — snd-only projection shape)."
  - citation: palace/linalg/operator.cpp:673
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "l = Normalize(comm, u) — returned norm IS the dominant-eigenvalue estimate; carrier u feeds next A.Mult(u,v) at :664."
  - citation: palace/linalg/operator.cpp:676
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "res = std::abs(l - l0) / l0 — convergence test consuming the returned norm l; direct load-bearing evidence."
  - citation: palace/linalg/nleps.cpp:610-611
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "NEP deflation: scale = Norml2(GetComm(), v) :610, v *= 1.0/scale :611 — inline unweighted normalise; :609 comment 'Update the invariant pair with normalization' confirms reading."
  - citation: palace/linalg/nleps.cpp:617
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "H.col(k).head(k) = v2 / scale — returned norm reused to rescale coordinate companion v2; doubly load-bearing confirmed."
  - citation: book/src/L1/normalize.md:50
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "Factorisation law 6 — the LHS the theme lowers; anchor at :50."
  - citation: book/src/L1-L0/scal-mutation-rotation.md:48-58
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "scal Sub-pattern A names this Normalize site (Normalize token at :48 and :55) — inheritance boundary holds."
  - citation: palace/test/unit/test-orthog.cpp:193
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "V[0] *= 1 / v0_norm — by-hand normalise empirical-match (real path); inherited test evidence."
  - citation: palace/test/unit/test-orthog.cpp:208
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "V[1] *= 1 / v1_norm — second by-hand normalise instance."
  - citation: palace/linalg/operator.hpp:377-384
    verdict: does-not-support
    audited_at: 2026-05-29T19:45:58Z
    note: "Range correct, but the surrounding 'no fused linalg::Normalize-with-B free function' claim (lines 51, 285-287, 311-313) is WRONG: operator.hpp:378 IS a fused B-weighted Normalize(comm, x, B, Bx) free function (reduction->guard->rescale->return, identical to vector.hpp:264). The defensible fact is that this fused B-Normalize is UNCALLED (no 4-arg rescaling callsite in the tree). Affects only the normalize_B rough-in note, NOT the firm unweighted core. See F1 / Open questions."
  - citation: palace/linalg/operator.cpp:599-619
    verdict: supports
    audited_at: 2026-05-29T19:45:58Z
    note: "B-weighted Norml2 reduction (B.Mult(x,Bx) at :602) — the matrix-weighted-norm reduction; in-bounds. Note: it IS fused into operator.hpp:378 (see operator.hpp:377-384 row)."
~~~
```

### Edit 2 (F3, citation-precision) — re-cite the second GMRES path 810-811

Re-cite the second GMRES Arnoldi path to the full two-line range (parity with the first
path's `631-632`). Three occurrences in the theme refer to it as `iterative.cpp:811`:

```edit:book/src/L1-L0/normalize-mutation-rotation.md
[line 137] replace "(A second identical GMRES code path is at `iterative.cpp:811`.)"
        with "(A second identical GMRES code path is at `iterative.cpp:810-811`.)"
[lines 174-175] replace "- `palace/linalg/iterative.cpp:811` — second analogous GMRES Arnoldi path, identical
  `w *= 1.0 / Hj[j + 1];`."
        with "- `palace/linalg/iterative.cpp:810-811` — second analogous GMRES Arnoldi path:
  `Hj[j + 1] = linalg::Norml2(comm, w); w *= 1.0 / Hj[j + 1];` (the two-line shape; `:811` is the rescale half)."
[lines 341-342] replace "- `palace/linalg/iterative.cpp:811` — second analogous GMRES Arnoldi path, identical
  `w *= 1.0 / Hj[j + 1];`. **Self-verified** (cited inherited via `scal-mutation-rotation.md:61-62`)."
        with "- `palace/linalg/iterative.cpp:810-811` — second analogous GMRES Arnoldi path:
  `Hj[j + 1] = linalg::Norml2(comm, w); w *= 1.0 / Hj[j + 1];`. **Audited** (`--anchor 'Hj[j + 1] = linalg::Norml2'` → 810; `--anchor 'w *= 1.0 / Hj[j + 1]'` → 811)."
```

### Edit 3 (F1, correctness fix to the `normalize_B` note) — GATED, routed to abstractor

F1 is a content correction to the `normalize_B` rough-in NOTE (theme lines 51, 285-287,
311-313 and the parallel claim in `book/src/L1/normalize.md:13,87,99`). Because it touches
the *substance* of the note (not a mechanical re-anchor) AND spans two files (theme + L1
operator entry), it exceeds a verifier's audit authority and is **routed to a follow-up
abstractor/lifter dispatch**, not applied here. The precise edit:

Replace the recurring phrasing **"Palace has no `linalg::Normalize`-with-`B` free
function; the sole `Normalize` overload (`vector.hpp:264`) takes no `B`"** with a fact-
accurate form, e.g.:

> Palace ships a fused B-weighted `Normalize(comm, x, B, Bx)` free function
> (`palace/linalg/operator.hpp:377-384`, structurally identical to the unweighted
> `vector.hpp:264`), but it is **uncalled** — no rescaling callsite invokes it in the
> current tree. The B-weighted *reduction* `Norml2(comm, x, B, Bx)` is used at error-norm
> / eigenvector-norm callsites (`arpack.cpp:438`, `slepc.cpp:475`, `nleps.cpp:114`) that
> feed residual ratios and do **not** rescale. So `normalize_B` stays a rough-in note: the
> fused operator exists but has no live consumer, and its norm constituent
> `matrix-weighted-norm` is `rough-in (test-coverage-bounded)`.

This **strengthens** the `normalize_B`-stays-rough-in conclusion (now: "exists but
uncalled" rather than "does not exist") without changing it. The firm unweighted core is
untouched. **Do NOT change the theme's `## Status` (`firm`)** — F1 is on the non-firm note.

## Supporting evidence

- `reference/palace/palace/linalg/vector.hpp:255-270` — read: `Norml2` (256-260) +
  `Normalize` (262-270). Confirms the four-step composition and the inherited reduction.
- `reference/palace/palace/linalg/iterative.cpp:625-646` (first GMRES path) and
  `805-816` (second path) — read: both are `OrthogonalizeIteration → Hj[j+1]=Norml2 →
  w*=1.0/Hj[j+1] → ApplyPlaneRotation` shapes. First at 631-632, second at 810-811.
- `reference/palace/palace/linalg/operator.cpp:655-682` — read: the spectral-radius power
  iteration loop; `l = Normalize` (673) / convergence (676) / `A.Mult` carrier (664).
- `reference/palace/palace/linalg/nleps.cpp:484-494,603-622` — read: the deflation
  invariant-pair normalisations; the cited `610-611,617` plus five MORE companion-scale
  instances (488-494,544-545,697-698,738-739) of the same Sub-pattern C shape.
- `reference/palace/palace/linalg/operator.hpp:374-385` — read: the **fused B-weighted
  `Normalize`** (377-384) — the F1 finding.
- `grep` survey: `inline auto Normalize` / `Normalize(comm` / `*= 1.0 /` across
  `reference/palace/palace/` — confirms (a) `vector.hpp:264` is the sole UNWEIGHTED fused
  overload, (b) `operator.hpp:378` is a SECOND (B-weighted) fused overload, (c) zero 4-arg
  B-`Normalize` callsites, (d) the extra nleps companion-scale instances.
- `tools/citecheck/citecheck.py --scan book/src/L1-L0/normalize-mutation-rotation.md
  --quiet` → 42 ok, 0 failing, exit 0.

## Open questions / caveats

- **F2 — returned-norm consumer-cohort is illustrative, not exhaustive (no edit forced).**
  The report itself flagged this Open question. Confirmed: nleps.cpp carries five more
  invariant-pair companion-scale instances (`488-494,544-545,697-698,738-739`) of the SAME
  Sub-pattern C shape (a shared `norm` rescaling a vector + its `*2` companion). This
  **confirms** the theme's "no un-cited site discards-vs-consumes the norm in a fourth
  shape" claim (all extras are the already-recognised companion-scale shape) and shows the
  cited `610-611,617` is correctly characterised as illustrative. No edit is forced; a
  future abstractor MAY enrich the cohort list, but the firm claim does not require it.
  OQ `normalize-mutation-rotation-lowering-verifier-audit` is RESOLVED by this dispatch.
- **F1 promotion-side note.** F1 surfaces that a *fused* B-weighted `Normalize` operator
  ALREADY EXISTS in Palace (`operator.hpp:377-384`), uncalled. This is relevant to the
  `normalize_B` promotion gate: the theme/L1-entry say promotion waits for "an inline
  B-weighted-normalise *rescale* site". The fused operator existing-but-uncalled means the
  gate is really "a *callsite* of the fused B-`Normalize` (or an inline B-rescale) plus the
  `matrix-weighted-norm` test-coverage promotion" — a slightly different gate than written.
  Recommend the follow-up abstractor (Edit 3) also tighten the `normalize_B` promotion
  condition wording. Not a firm-core concern.
- **Direction-of-definition: clean.** The theme narrates forward (L1 `normalize` → L0
  `linalg::Normalize`); no reverse-direction (L0-lifts-to-L1) prose in the formal chapter.
  No high→low violation.
- **No status change.** The firm unweighted-normalise core is fully-supported and stays
  `firm`. F1/F3 are refinements to the non-firm `normalize_B` note and a citation-range
  precision nudge respectively; per the dispatch-phase write-guard, all edits are proposed
  here and applied by a follow-up integrator/abstractor dispatch, not by this audit.
