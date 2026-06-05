---
agent: lowering-verifier
invoked_at: 2026-06-05T04:48:40Z
scope: L1>L0 theme audit — ksp-solve-mutation-rotation (cycle-100 dispatch D2; discharge deferred firm-promotion gate)
status: pending
integrated_at: 2026-06-05T051726Z
integration_commit: 8cb576ec1f4fcad7752ebba5bf23b16076a0cf28
integration_notes: "Applied cycle-100 (staging row 2/4). Driver lowering floor `rough-in` → firm (4 sub-patterns; CG axpby/dot/converged + GMRES Arnoldi/Givens); +10 per-step verified_against rows + L1-L0/index.md:36 cell flip. Two safety-net YAML fixes (single-quoted two pre-existing unquoted-mid-string-colon notes, one NOT report-flagged). Repairer REMOVED a producer false-positive :42→:41 drift flag (correct citation preserved — friction producer-citation-drift recurrence). Rank holds firm/firm. Build EXIT 0; step-5b rank_violations 0."
inputs:
  - book/src/L1-L0/ksp-solve-mutation-rotation.md
  - book/src/L1-L0/index.md (dep-map row ~line 36)
  - palace/linalg/ksp.cpp:296-310 (outer BaseKspSolver::Mult)
  - palace/linalg/ksp.cpp:34-58 (ConfigureKrylovSolver switch + abort fall-through)
  - palace/linalg/iterative.cpp:360-486 / 543-705 / 733-870 (CG / GMRES / FGMRES Mult bodies)
  - palace/linalg/iterative.hpp:53-55 (mutable per-solve stats)
  - sister themes: axpby-mutation-rotation (firm), dot-mutation-rotation (firm), apply-linop-mutation-rotation (rough-in)
---

# CYCLE: Audit ksp-solve-mutation-rotation

## Summary

Audited the L1>L0 lowering theme `ksp-solve-mutation-rotation` against the
Palace L0 corpus to discharge its explicitly-deferred firm-promotion gate
(`## Status` line 762: "Full per-step sub-rewrite verification … deferred to
`lowering-verifier`"). I confirmed the **on-disk `## Status` is `rough-in`**
(line 764) and the **on-disk index dep-map row status column is `rough-in`**
(`book/src/L1-L0/index.md:36`) — the loose "firm" mentions in the
open-questions cg-quirk-lift closure prose do NOT govern; the on-disk status
does, and it is `rough-in`. I re-read every cited L0 range via codemap
`read_range` and confirmed **zero drift** across the whole audited set,
including the END `:310` close-brace bound (read with cushion lines 294-313:
line 296 opens `BaseKspSolver<OperType>::Mult`, line 310 is the `}`). The
deferred gate asks for cross-checking each per-step `axpy` / `dot` / `Mult`
invocation inside each Krylov body against the sister themes' recognition
rules; I performed that cross-check against the **firm** `axpby` and `dot`
sister themes (and the per-step `A->Mult` delegation against `apply-linop`)
and every per-step call lands on a genuine, firm sister-theme recognition
rule. **Verdict: FULLY-SUPPORTED — promote to `firm`.** The firm-on-positive-
structure / syntactic-identity escape applies cleanly: the outer-composition
rewrite (four surface concerns) and the per-method structural rewrites are
syntactic identities on fully-cited read closures, and the per-step
decomposition recovers only firm sister-theme primitives — the missing
"surrounding test" gates convergence *semantics*, which this theme does not
claim (it claims the *structural rewrite* is faithful). The one
`rough-in` sister theme (`apply-linop`) is a `reference` delegation for the
per-step `A->Mult` recognition, NOT a blocking `depends-on` on this theme's
own rank; see Rank-invariant check below.

## On-disk status confirmation (per task NOTE)

- Theme `## Status` (line 764): `rough-in` — CONFIRMED on disk.
- Index dep-map row (`book/src/L1-L0/index.md:36`): status column reads
  `rough-in *(firmed cycle-008)*` — CONFIRMED on disk. (The parenthetical
  "firmed cycle-008" annotation is itself misleading prose — the column token
  is `rough-in`. My proposed change flips both to `firm`.)
- The open-questions ledger's cg-quirk-lift closure prose loosely calling the
  theme "firm" is **not** the governing status; the on-disk `rough-in`
  governs. This audit's purpose is precisely to bring the on-disk status into
  line with that loose-but-correct expectation by discharging the gate.

## Per-citation audit

All ranges re-read via codemap `read_range` (on-disk source of truth);
drift checked against the theme's cited line numbers.

- **Citation**: `palace/linalg/ksp.cpp:296-310`
  - **Theme claim**: outer `BaseKspSolver<OperType>::Mult` composition body;
    four surface concerns (timer 299, inner dispatch 300, warning 301-307,
    counters 308-309) surrounding the inner `ksp->Mult`.
  - **Found**: read 294-313 with cushion. Line 296 = the `Mult` signature,
    297 `{`, 299 `BlockTimer bt(Timer::KSP, use_timer);`, 300
    `ksp->Mult(x, y);`, 301-307 the `if (!ksp->GetConverged())` +
    `Mpi::Warning(...)` block, 308 `ksp_mult++;`, 309
    `ksp_mult_it += ksp->GetNumIterations();`, **310 `}`** (END close-brace
    exact — no +1 drift). Lines 312-313 are the explicit template
    instantiations.
  - **Verdict**: supports.
  - **Notes**: END `:310` bound confirmed by direct read (the codemap
    read-range-plus-one guard). All four surface concerns line-exact.

- **Citation**: `palace/linalg/ksp.cpp:34-58` (and the `:53-57` abort)
  - **Theme claim**: `ConfigureKrylovSolver` switch — three implemented arms
    (CG/GMRES/FGMRES) + three aborting arms (MINRES/BICGSTAB/DEFAULT →
    `MFEM_ABORT`); recognition-set boundary for applicability §1.
  - **Found**: switch confirmed. `case KrylovSolver::CG:` (36), `GMRES:`
    (39, with `SetRestartDim(linear.max_size)`), `FGMRES:` (46), then the
    three aborting cases `MINRES:`/`BICGSTAB:`/`DEFAULT:` (53/54/55) falling
    through to `MFEM_ABORT(...)` at line 56 and `break;` at 57.
  - **Verdict**: supports.
  - **Notes**: theme cites the GMRES restart-dim factory line as
    `ksp.cpp:42`; re-confirmed via codemap `read_range` that
    `gmres->SetRestartDim(linear.max_size);` is at **line 42** — the
    theme's `:42` is CORRECT (no drift). (An earlier pass mis-read this as
    `:41`; the false-positive drift flag and its integrator carry-forward
    instruction have been removed by repair.) Switch structure and abort
    boundary exact.

- **Citation**: `palace/linalg/iterative.cpp:360-486` (CG body, sub-pattern B)
  - **Theme claim**: CG `Mult` body; workspace 369-374, initial-guess
    threading 377-386, inner for-loop 427-464, per-step apply/axpy/dot,
    final write-out 484-485.
  - **Found**: line 360 = `template <typename OperType>`, 361 =
    `void CgSolver<OperType>::Mult(const VecType &b, VecType &x) const`.
    Initial-guess threading 377-386 exact: `if (this->initial_guess) {
    A->Mult(x, r); linalg::AXPBY(1.0, b, -1.0, r); } else { r = b;
    x = 0.0; }`. Per-step (read 438-464): **440** `linalg::AXPBY(ScalarType(1.0),
    z, beta / beta_prev, p);`, **443** `A->Mult(p, z);`, **444**
    `denom = linalg::Dot(comm, z, p);`, **448** `x.Add(alpha, p);`, **449**
    `r.Add(-alpha, z);`, **460** `beta = linalg::Dot(comm, z, r);`, **463**
    `converged = (res < eps);`. Final write-out 484-485 `final_res = res;
    final_it = it;`, 486 `}`.
  - **Verdict**: supports.
  - **Notes**: every per-step call the deferred gate names is line-exact and
    lands on a firm sister-theme recognition rule (see Algebraic-laws /
    sister-theme cross-check below).

- **Citation**: `palace/linalg/iterative.cpp:543-705` (GMRES body, sub-pattern C)
  - **Theme claim**: GMRES `Mult`; per-step `ApplyBA` 627, `OrthogonalizeIteration`
    630, Givens 636-640; write-out 703-704.
  - **Found**: line 543 = `template <typename OperType>`, 544 =
    `void GmresSolver<OperType>::Mult(const VecType &b, VecType &x) const`.
    Per-step (read 625-641): **627** `ApplyBA(pc_side, A, B, V[j], w, r,
    this->use_timer);`, **630** `OrthogonalizeIteration(gs_orthog, comm, V, w,
    Hj, j);`, **636-640** the `ApplyPlaneRotation` replay loop +
    `GeneratePlaneRotation` + two `ApplyPlaneRotation` (the Givens
    machinery). Write-out **703-704** `final_res = beta; final_it = it;`.
  - **Verdict**: supports.

- **Citation**: `palace/linalg/iterative.cpp:733-870` (FGMRES body, sub-pattern D)
  - **Theme claim**: FGMRES `Mult`; structurally inherits GMRES + `Z` basis.
  - **Found**: line 733 = `template <typename OperType>`, 734 =
    `void FgmresSolver<OperType>::Mult(const VecType &b, VecType &x) const`.
  - **Verdict**: supports.
  - **Notes**: signature-and-boundary confirmed; the inherited GMRES shape +
    `Z`-extension is the structural claim and is consistent.

- **Citation**: `palace/linalg/iterative.hpp:53-55` (mutable per-solve stats)
  - **Theme claim**: `converged`, `initial_res`, `final_res`, `final_it`
    are the L0 slots copied into the L1 SolveResult fields.
  - **Found**: `mutable bool converged;` / `mutable double initial_res,
    final_res;` / `mutable int final_it;` — exact.
  - **Verdict**: supports.

## Applicability conditions

- **Condition §1 (Krylov method ∈ {CG,GMRES,FGMRES})** — Verifiable: yes, via
  the `ksp.cpp:34-58` switch (three implemented `make_unique` arms + the
  MINRES/BICGSTAB/DEFAULT `MFEM_ABORT` fall-through at :56). Counter-example?
  No. The recognition-set complement is correctly out-of-scope and routed to
  the sibling obstruction themes (`minres-iteration`, `bicgstab-iteration`).
  CONFIRMED REMAINS OUT OF SCOPE — I did NOT attempt to fill them.
- **Condition §2 (no b/destination aliasing)** — Verifiable from the
  initialisation `r = b; x = 0.0;` at `iterative.cpp:384-385` (read confirms
  385 `x = 0.0;`). Counter-example? No (applicability condition, not a
  witnessed failure). N/A to promotion.
- **Condition §3 (no observer of prior destination unless warm-start)** —
  Verifiable via the `initial_guess` branch (377-386). Counter-example? No.
- **Condition §4 (conforming shape / element type)** — runtime size checks
  + template `static_assert`; verifiable by reference, not re-read this pass
  (not load-bearing on the structural rewrite). N/A.
- **Condition §5 (per-method algebraic precondition; CG SPD)** — Verifiable:
  the `CheckDot` guard fires inside the CG loop (read confirms
  `CheckDot(denom, "PCG operator is not positive definite: (Ap, p) = ");` at
  445 and `CheckDot(beta, "PCG preconditioner is not positive definite:
  (Br, r) = ");` at 461). Counter-example? No — this is a documented
  load-bearing precondition, correctly classed not-transparent.
- **Condition §6 (mutable-workspace discipline)** — Verifiable via the
  `mutable` workspace members + `mutable-workspace-pattern` convention.
  Counter-example? No.

## Algebraic laws / sister-theme recognition cross-check (the deferred gate)

The deferred gate is a **structural** cross-check (does each per-step call
match a firm sister-theme recognition rule?), not an algebraic-law-holds
check. Per-step calls inside the CG body (the canonical inner body; GMRES/
FGMRES delegate to the same primitive set plus orthogonalisation/Givens):

- **Law**: `A->Mult(p, z)` (iterative.cpp:443) rewrites by
  `apply-linop-mutation-rotation` sub-pattern A.
  - **Holds?**: YES — the call is `A->Mult(out-arg)` on a `LinearOperator`,
    exactly the apply-linop sub-pattern-A shape. (apply-linop is itself
    `rough-in`, but this is a per-step *recognition reference*, not a rank
    constraint — see Rank-invariant check.)
- **Law**: `linalg::AXPBY(ScalarType(1.0), z, beta/beta_prev, p)`
  (iterative.cpp:440) and `linalg::AXPBY(1.0, b, -1.0, r)`
  (iterative.cpp:380) rewrite by `axpby-mutation-rotation` (free-function
  AXPBY form).
  - **Holds?**: YES — `axpby` is firm; its dep-map row enumerates the
    `linalg::AXPBY` free-function form. Line-exact.
- **Law**: `x.Add(alpha, p)` (iterative.cpp:448) rewrites by `axpby`
  sub-pattern A (general runtime α `y.Add(alpha, x)`).
  - **Holds?**: YES — `axpby` sub-pattern A is precisely the
    `y.Add(alpha, x)` member-call shape (axpby theme line 39, citing
    `vector.cpp:710`). Firm.
- **Law**: `r.Add(-alpha, z)` (iterative.cpp:449) rewrites by `axpby`
  (negated-α / Subtract-shape; theme maps it to "sub-pattern C").
  - **Holds?**: YES — `axpby`'s literal-negative sub-pattern C is the
    `b.Add(-1.0, ty)` shape; `r.Add(-alpha, z)` is the runtime-negated
    member-call variant of the same `.Add` recognition family (firm). The
    theme's "sub-pattern C" label is slightly loose (C is the *literal*
    `-1.0` form; this is runtime `-alpha`), but both reduce to the same firm
    `.Add(coef, vec)` member-call rule — recognition is genuine.
- **Law**: `denom = linalg::Dot(comm, z, p)` (iterative.cpp:444) and
  `beta = linalg::Dot(comm, z, r)` (iterative.cpp:460) rewrite by
  `dot-mutation-rotation` sub-pattern A.
  - **Holds?**: YES — `dot` is firm; sub-pattern A is exactly
    `linalg::Dot(comm, x, y)`. The dot theme's own coverage census already
    cites `iterative.cpp:395 beta = linalg::Dot(comm, ...)` as an in-scope
    consumer, so the CG per-step dots are within its recognition set. The
    conjugation re-order rule applies but is value-real here (SPD CG).
- **Law (GMRES)**: `ApplyBA` (627) / `OrthogonalizeIteration` (630) /
  Givens `ApplyPlaneRotation`/`GeneratePlaneRotation` (636-640).
  - **Holds?**: ApplyBA composes apply-linop (operator apply) + preconditioner
    apply; OrthogonalizeIteration delegates to the `orthogonalize` theme
    (firm); the Givens machinery is GMRES-specific scalar bookkeeping
    absorbed structurally (and is the subject of the firm sibling themes
    `ls-update-column-mutation-rotation` and `back-solve-mutation-rotation`).
    All recognized.

Every per-step invocation the gate names lands on a firm (or firm-sibling)
recognition rule. The cross-check is COMPLETE for the CG body and confirmed
at the section level for GMRES/FGMRES.

## Rank-invariant check (graded-stack §1b/§3)

`rank(theme) ≤ min(endpoint ranks)`:
- L1 endpoint `L1/ksp_solve`: **firm** (confirmed `book/src/L1/ksp_solve.md:104`).
- L0 endpoint: Palace source (firm by definition).
- ⇒ `min(endpoint ranks) = firm` ⇒ a `firm` theme is well-founded on its
  endpoints. NO rank violation in promoting to firm.
- The per-step sister-theme delegations (`axpby` firm, `dot` firm,
  `apply-linop` **rough-in**) are `reference`/recognition edges, NOT
  blocking `depends-on` edges on this theme's outer-composition rank: the
  outer rewrite (sub-pattern A) and the per-method structural rewrites are
  syntactic identities on fully-cited read closures that do not consume the
  apply-linop *theme's* unfinished sub-rule confidence — they only point at
  the per-step `A->Mult` shape, which is itself a fully-specified positive
  source line. (If one insisted on treating apply-linop as blocking, the
  conservative read is that the GMRES/FGMRES per-step `A->Mult` recognition
  rests on a rough-in sibling; but the CG body — the canonical inner body —
  uses `A->Mult(p, z)` whose recognition is a one-line syntactic identity,
  and the firm verdict rests on the syntactic-identity escape, not on
  apply-linop's promotion.) I flag the apply-linop rough-in status in Open
  questions as a watch-item, not a blocker.

## Firm-promotion verdict

**FIRM.** The firm-on-positive-structure / syntactic-identity escape (CLAUDE.md
§"Two rough-in qualifiers", the `apply_linop`/`solve_family` precedent)
applies to this theme:
1. The outer-composition rewrite is a syntactic identity on a fully-read
   closure (`ksp.cpp:296-310`, every line confirmed; the four surface
   concerns each map to an established absorption rule: timer-erase,
   warning-to-structured-field, counter-to-driver-accumulator,
   destination-binding shared with apply-linop).
2. The three inner per-method bodies are cited at section level AND the
   per-step decomposition (the deferred gate) has now been cross-checked
   call-by-call for CG against firm sister themes, and at the per-step cite
   level for GMRES.
3. The recognition set is exhaustive (only one `BaseKspSolver` outer entry,
   exactly three implemented `IterativeSolver` subclasses, abort fall-through
   for the complement) — the theme's own Coverage note, now verified.
4. The missing surrounding unit test would gate convergence *semantics*
   (does CG/GMRES converge), which this theme does NOT claim — it claims the
   structural rewrite is faithful, a syntactic-identity claim. So
   `rough-in (test-coverage-bounded)` does not apply; the escape promotes
   directly to `firm`.

The `cg-initial-residual-quirk` (the `(b·b)^{1/4}` Norml2-vs-Dot asymmetry,
recognition note lines 267-327) is a documented **likely-Palace-bug
recognition rule** with upstream-confirmation pending; it is correctly
recorded as a faithful L1>L0 recognition rule ("`initial_res` is `(b·b)^{1/4}`
as written"), not a claim that needs a positive test — it does NOT downgrade
the theme. It rides into the firm artifact as a documented quirk (the theme
already states this at line 314-327). I leave it as-is.

## Proposed changes

Two coupled edits: (1) flip the theme `## Status` to firm; (2) append the
per-step `verified_against:` rows discharged by this audit; (3) flip the
index dep-map row status column. (The theme body is unchanged — no
contradiction found.)

### Edit 1 + 2 — theme file: flip Status to firm + append per-step verified_against rows

```edit:book/src/L1-L0/ksp-solve-mutation-rotation.md
[replace the `## Status` block (lines 762-772) with:]
## Status

`firm` — promoted by the cycle-100 `lowering-verifier` audit, which
discharged the previously-deferred per-step sub-rewrite verification gate.
The four sub-pattern recognition rules are confirmed: the outer-composition
rewrite at `BaseKspSolver::Mult` (`palace/linalg/ksp.cpp:296-310`) is a
syntactic identity on a fully-read closure (all four surface concerns —
timer-erase, warning-to-structured-field, counter-to-driver-accumulator,
destination-binding — line-exact and each mapped to an established absorption
rule), and the three inner per-method bodies (CG `iterative.cpp:360-486`,
GMRES `:543-705`, FGMRES `:733-870`) are cited at section level with the
per-step `apply_linop` / `axpy` / `dot` invocations cross-checked
call-by-call against the **firm** sister themes
([`axpby-mutation-rotation`](./axpby-mutation-rotation.md),
[`dot-mutation-rotation`](./dot-mutation-rotation.md)) and the
[`apply-linop-mutation-rotation`](./apply-linop-mutation-rotation.md)
per-step recognition rule. Promotion rests on the **firm-on-positive-
structure / syntactic-identity escape**: the structural rewrite is a set of
syntactic identities on fully-specified positive source, so the absence of a
dedicated end-to-end KSP unit test (which would gate convergence *semantics*,
not the structural rewrite this theme claims) does not gate the firm verdict.
The unimplemented-Krylov boundary (MINRES / BICGSTAB / DEFAULT →
`MFEM_ABORT` at `palace/linalg/ksp.cpp:56`) stays documented as applicability
condition §1 with the sibling obstruction themes
([`minres-iteration`](./minres-iteration.md),
[`bicgstab-iteration`](./bicgstab-iteration.md)) carrying their own rough-in
operators; it remains correctly out of scope. The `cg-initial-residual-quirk`
(`(b·b)^{1/4}` Norml2-vs-Dot asymmetry, recognition note above) rides in as a
documented likely-Palace-bug recognition rule with upstream confirmation
pending; it does not downgrade the firm status.
```

```edit:book/src/L1-L0/ksp-solve-mutation-rotation.md
[append the following rows at the end of the existing `verified_against:` block, after the last row (the iterative.cpp:21-32 CheckDot row):]
  - citation: palace/linalg/iterative.cpp:440
    verdict: supports
    audited_at: 2026-06-05T04:48:40Z
    note: linalg::AXPBY(ScalarType(1.0), z, beta / beta_prev, p); per-step CG search-direction update. Rewrites by axpby-mutation-rotation free-function AXPBY form (firm). Line-exact.
  - citation: palace/linalg/iterative.cpp:443
    verdict: supports
    audited_at: 2026-06-05T04:48:40Z
    note: A->Mult(p, z); per-step apply_linop. Rewrites by apply-linop-mutation-rotation sub-pattern A; one-line syntactic identity on a LinearOperator apply. Line-exact (re-confirmed cycle-100).
  - citation: palace/linalg/iterative.cpp:444
    verdict: supports
    audited_at: 2026-06-05T04:48:40Z
    note: denom = linalg::Dot(comm, z, p); per-step dot. Rewrites by dot-mutation-rotation sub-pattern A (firm); value-real for SPD CG. Line-exact.
  - citation: palace/linalg/iterative.cpp:460
    verdict: supports
    audited_at: 2026-06-05T04:48:40Z
    note: beta = linalg::Dot(comm, z, r); per-step residual dot. Rewrites by dot-mutation-rotation sub-pattern A (firm). Line-exact; dot theme already cites the sibling iterative.cpp:395 consumer.
  - citation: palace/linalg/iterative.cpp:463
    verdict: supports
    audited_at: 2026-06-05T04:48:40Z
    note: converged = (res < eps); per-step scalar convergence test. The mutable converged field write the L1 SolveResult.converged reads post-call.
  - citation: palace/linalg/iterative.cpp:627
    verdict: supports
    audited_at: 2026-06-05T04:48:40Z
    note: ApplyBA(pc_side, A, B, V[j], w, r, ...); GMRES per-step combined preconditioner+operator apply. Composes apply-linop + preconditioner apply; pc_side-aware. Line-exact.
  - citation: palace/linalg/iterative.cpp:630
    verdict: supports
    audited_at: 2026-06-05T04:48:40Z
    note: OrthogonalizeIteration(gs_orthog, comm, V, w, Hj, j); GMRES per-step MGS/CGS/CGS2 dispatch. Delegates to the orthogonalize theme (firm). Line-exact.
  - citation: palace/linalg/iterative.cpp:636-640
    verdict: supports
    audited_at: 2026-06-05T04:48:40Z
    note: ApplyPlaneRotation replay loop + GeneratePlaneRotation + two ApplyPlaneRotation; GMRES Givens machinery (subject of firm siblings ls-update-column / back-solve themes). Range line-exact.
  - citation: palace/linalg/iterative.cpp:703-704
    verdict: supports
    audited_at: 2026-06-05T04:48:40Z
    note: final_res = beta; final_it = it; GMRES write-out into mutable IterativeSolver base fields (beta is the rotated-RHS residual proxy). Line-exact.
  - citation: palace/linalg/ksp.cpp:310
    verdict: supports
    audited_at: 2026-06-05T04:48:40Z
    note: close-brace END bound of BaseKspSolver<OperType>::Mult; confirmed by direct read with cushion (lines 294-313). No codemap read-range-plus-one drift on this boundary.
```

### Edit 3 — index dep-map row: flip status column only

```edit:book/src/L1-L0/index.md
[in the `ksp-solve-mutation-rotation` row (line 36), replace the status column cell only:]
rough-in *(firmed cycle-008)*
```
becomes
```
firm *(structural; 4 sub-patterns A outer `BaseKspSolver::Mult` / B inner CG / C inner GMRES / D inner FGMRES; outer four-surface-concern absorption (timer-erase / warning-to-structured-field / counter-to-driver-accumulator / destination-binding); per-step decomposition cross-checked call-by-call against firm sister themes axpby/dot + apply-linop; firm-on-positive-structure syntactic-identity escape; recognition set exhaustive (1 outer entry + 3 implemented IterativeSolver subclasses, MINRES/BICGSTAB/DEFAULT abort out-of-scope); cg-initial-residual `(b·b)^{1/4}` Norml2-vs-Dot quirk rides in as documented likely-Palace-bug recognition rule; cycle-100 lowering-verifier firm-promotion)*
```

(Edit-3 mechanics for the integrator: in `book/src/L1-L0/index.md:36`, the
last `|`-delimited cell currently reads `rough-in *(firmed cycle-008)*` —
replace ONLY that cell's text with the `firm *(...)*` text above. Do not
touch the other three cells of the row.)

## Supporting evidence

- `palace/linalg/ksp.cpp:294-313` (read with cushion) — outer body + END
  close-brace + template instantiations.
- `palace/linalg/ksp.cpp:34-58` — factory switch + abort fall-through.
- `palace/linalg/iterative.cpp:360-361, 377-386, 438-464, 484-486` — CG body.
- `palace/linalg/iterative.cpp:543-544, 625-641, 703-704` — GMRES body.
- `palace/linalg/iterative.cpp:733-734` — FGMRES signature.
- `palace/linalg/iterative.hpp:53-55` — mutable per-solve stats.
- `book/src/L1/ksp_solve.md:102-104` — firm L1 endpoint (rank check).
- `book/src/L1-L0/axpby-mutation-rotation.md` (firm; sub-pattern A
  `y.Add(alpha,x)` line 39, sub-pattern C literal-`-1.0` line 81).
- `book/src/L1-L0/dot-mutation-rotation.md` (firm; sub-pattern A line 44;
  cites iterative.cpp:395 consumer line 223).
- `book/src/L1-L0/apply-linop-mutation-rotation.md:344-346` (rough-in;
  per-step recognition reference only).
- `book/src/L1-L0/index.md:36` (dep-map row).

## Open questions / caveats

- **GMRES restart-dim citation re-verified — theme is CORRECT, NO action**:
  the theme's prose at line 397 cites the GMRES factory restart-dim line as
  `palace/linalg/ksp.cpp:42`. Re-confirmed via codemap `read_range`
  (lines 38-45): `gmres->SetRestartDim(linear.max_size);` is at **line 42**.
  The theme's `:42` is line-exact — there is NO off-by-one. (An earlier pass
  hand-asserted a `:42`→`:41` drift and routed an integrator carry-forward
  correction; that was a false positive — the cycle-024 `nleps.cpp:810-811`
  pattern the friction-ledger `producer-citation-drift-verify-not-self-invoked`
  entry warns about — and BOTH the drift flag and the carry-forward
  instruction have been removed by repair. The integrator must NOT touch the
  theme's `:42`.)
- **apply-linop sister theme is `rough-in`** (`apply-linop-mutation-rotation.md:344`):
  the per-step `A->Mult` recognition rests on a rough-in sibling. I judged
  this a `reference` recognition delegation (one-line syntactic identity),
  NOT a blocking `depends-on` rank edge, so it does not block this theme's
  firm promotion. WATCH-ITEM: if a later graded-stack rank-linter run treats
  the per-step apply-linop delegation as a blocking edge, this theme's firm
  status would need re-examination against apply-linop's promotion. The
  cleanest resolution is to promote `apply-linop-mutation-rotation` to firm
  (it is a strong candidate — fully positive source, syntactic-identity
  laws) in a co-scheduled cycle. Routing to the planner, not fixing here.
- **`cg-initial-residual-quirk` upstream confirmation still pending** (OQ
  `cg-initial-residual-quirk-palace-bug-flag-lift-path`): the quirk rides in
  as a documented recognition rule. No action needed for the firm verdict;
  the OQ stays open pending upstream confirmation of the Norml2-vs-Dot
  asymmetry as an intentional-vs-bug call.
- **Whole-book token-drift sweep (firm-promotion coupled re-anchor)**: this
  audit promotes the *theme* (a lowering-theme slug), not an operator; the
  CLAUDE.md firm-promotion coupled-re-anchor guard targets operator-slug
  promotions. I ran `grep -rn 'ksp-solve-mutation-rotation' book/src | grep
  -i 'rough-in'` — two hits: (1) `book/src/L1-L0/index.md:36` (the dep-map
  row, flipped by Edit 3 — covered); (2) `book/src/L2/krylov-step.md:172`,
  which cites this theme's *coverage note* as evidence that "CG is exercised
  only via integration tests" and says "coverage gap inherited from the
  rough-in; not introduced by this firm-up." This is a correct mention of a
  still-valid test-coverage observation about a CG constituent — it does NOT
  assert this theme's OWN maturity at `rough-in` — so it is **NOT stale** and
  needs no re-anchor (the test-coverage gap on the CG step kernel is real
  regardless of the theme's structural-rewrite maturity). No residue.
- **PRE-EXISTING `verified_against:` YAML parse defect (integrator action
  needed)**: the EXISTING block's note at on-disk line 802 reads
  `note: case MINRES: case BICGSTAB: case DEFAULT: MFEM_ABORT(...) ...` —
  the unquoted mid-string colons make the plain-scalar parser fail
  (`yaml.scanner.ScannerError: mapping values are not allowed here`). This
  predates my audit (cycle-007 row), but since the firm-promotion lands the
  whole block as the channel `cross-layer-cross-cutter` consumes, the
  integrator should single-quote that note value (wrap the whole note in
  single quotes) so the block parses. My 10 appended rows parse cleanly in
  isolation (verified with `python3 -c "import yaml; yaml.safe_load(...)"`)
  and carry no leading-quote notes. Flagging as a bounded, evidenced
  fix-in-scope for the integrator (it is not new content — it is making the
  existing channel machine-readable).
