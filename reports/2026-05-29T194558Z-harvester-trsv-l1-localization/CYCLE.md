---
agent: harvester
invoked_at: 2026-05-29T19:45:58Z
scope: L1/L3 localization — trsv (triangular solve) primitive characterization (routing decision)
status: integrated
integrated_at: 2026-05-29T205500Z
integration_commit: 3319d88
integration_notes: "cycle-028 position 7/7 (per-report; LAST). HARVESTER localization-only dispatch — NO proposed-changes block / NO book/ mutation. Sole integration action = 2 OQ promotions. Negative-finding resolution of the LAST leaf of l3-vocabulary-inventory-gap: Palace exposes NO standalone trsv primitive (two exhaustive zero-hit searches, critic-reproduced; densematrix.hpp:24-36 has no triangular solve), so trsv routes resolved-by-obstruction (NOT perpetually BLOCKED) — opaque-library-owned (HYPRE GS/SSOR relax-type flags + external direct-solver wrappers) or a block-triangular red herring. Closes the parent migrated-plan-item l3-vocabulary-inventory-gap (all four leaves done). Routed fresh triangular-solve-obstruction L1>L0 obstruction-theme abstractor candidate. Critic-filed skill-candidate establish-negative-finding-exhaustiveness left for the meta-phase. Build-relevant: no."
inputs:
  - OQ parent `l3-vocabulary-inventory-gap` REMAINING leaf: `trsv` (BLOCKED, no L1 anchor)
  - palace-codemap localization of palace/linalg/* + preconditioner/smoother files
  - book/src/L3/index.md:7 (existing L3 obstruction note naming GS-flavoured / triangular solves)
  - book/src/L1/back_solve.md (firm c027 — the small-dense restart-correction leaf, distinct target)
---

# CYCLE: Localize/characterize `trsv` (triangular solve) at L1 — routing decision

## Summary
This is a **localization-only** dispatch (no L1 `trsv` entry authored). It resolves the last open leaf of the L3 vocabulary-inventory gap: whether Palace exposes a standalone general sparse/dense triangular-solve (`trsv`) primitive. **Conclusion: it does not.** There is no `trsv`/`trsm`/`TriangularSolve`/`SpTrSV` symbol anywhere in the tree (two exhaustive searches, zero hits). Triangular solves appear in Palace **only as internal substitution sweeps inside opaque library calls** — the Gauss-Seidel / SSOR relaxation sweeps inside HYPRE BoomerAMG/AMS (selected by integer `relax_type` config flags) and the forward/back substitution inside the MUMPS/SuperLU/STRUMPACK direct-solver factorizations (external-library wrappers). The only Palace-authored smoothers are **Jacobi** and **Chebyshev** (the latter deliberately chosen *over* Gauss-Seidel per Adams et al. 2003). The one "block lower-triangular preconditioner" in Palace is a 2×2 **block** structure (applies sub-solvers `P0^{-1}`, `P1^{-1}`), not a scalar triangular solve. **Routing recommendation: (ii) obstruction-theme target** — `trsv` is an L1>L0 (and L3) obstruction, not a firm-L1-operator candidate. It is exactly the case `book/src/L3/index.md:7` already advertises ("Gauss-Seidel-flavored smoothers, certain triangular solves, sequentially-reordered preconditioners").

## Proposed changes
None (localization-only dispatch). No `book/` edits. The follow-on authoring (an L1>L0 obstruction theme + possibly an L3 obstruction row) is a separate dispatch routed below. Per the dispatch-phase write-guard, this report emits the characterization only.

## Characterization

### (a) Is there a stand-alone `trsv`-shaped public API in Palace? — NO

Two exhaustive codemap text searches returned **zero hits**:
- `trsv|trsm|TriSolve|TriangularSolve|SpTrSV` — no hits anywhere in the tree.
- A repo-wide grep for `GaussSeidelSmoother|SORSmoother|class …(ILU|IncompleteLU|IC0|Cholesky)…Smoother` — no hits (no Palace-authored GS/SOR/ILU/IC smoother class exists).

The small-dense matrix utility module exposes no triangular solve and no triangular factorization:
- `palace/linalg/densematrix.hpp:24-36` — the full public API is `MatrixSqrt` (`densematrix.hpp:24`, `:26`), `MatrixPow` (`densematrix.hpp:28`, `:30`), `SingularValueMax` (`densematrix.hpp:32`), `SingularValueMin` (`densematrix.hpp:34`), `Mult` (`densematrix.hpp:36`). No `LU`/`Cholesky`/`Solve`/`trsv`. A grep of `densematrix.cpp` for `Factor|LU|Cholesky|GETRS|trsv|TriangularSolve|Solve` returned nothing — the module does dense matrix functions (sqrt/pow via eigen-decomposition) and products, never a triangular substitution.

This is distinct from the firm `back_solve` leaf (`book/src/L1/back_solve.md`, firm c027): that is the **small-dense upper-triangular** restart-correction back-substitution specific to GMRES/FGMRES (solving the `R y = g` system against the Hessenberg-derived upper-triangular factor inside the Krylov restart). It is a Krylov-internal leaf, not a general-purpose `trsv` primitive, and its existence does not imply a standalone triangular-solve API.

### (b) Where triangular solves appear as internal steps — only inside opaque library calls

**(b1) HYPRE-internal Gauss-Seidel / SSOR relaxation sweeps.** The only Gauss-Seidel / SOR relaxation in Palace is selected by **integer config flags passed into the opaque HYPRE library** — the actual forward/back substitution sweeps live inside HYPRE, not in Palace source:
- `palace/linalg/amg.cpp:19` — `int relax_type = 8;  // 8 = l1-symm. GS, 13 = l1-GS, 18 = l1-Jacobi, 16 = Chebyshev` — passed via `HYPRE_BoomerAMGSetRelaxType(*this, relax_type)` at `palace/linalg/amg.cpp:29`. (On GPU the default flips to `18` = l1-Jacobi, `amg.cpp:24`, because the GS sweep is sequential and GPU-hostile.)
- `palace/linalg/ams.cpp:162` — `int relax_type = 2;  // 2 = l1-SSOR, 4 = trunc. l1-SSOR, 1 = l1-Jacobi, 16 = Chebyshev` — passed via `HYPRE_AMSSetSmoothingOptions(ams, relax_type, …)` at `palace/linalg/ams.cpp:173`. The AMG sub-options similarly select `amg_relax_type = 18` (l1-Jacobi, `ams.cpp:158`) with a GS coarse-relax fallback (`coarse_relax_type = 9` Gaussian elimination, `ams.cpp:179`).

These are **negative anchors** in the obstruction sense: Palace does not *author* a triangular solve here — it hands HYPRE an enum selecting one of HYPRE's internal relaxation kernels. The triangular substitution is opaque-library-owned.

**(b2) Palace-authored smoothers are GS-free.** The Palace-native smoother cohort contains **no** triangular relaxation:
- `palace/linalg/jacobi.hpp:15-19` / `jacobi.cpp:100` — `JacobiSmoother` (diagonal-only; no triangular sweep).
- `palace/linalg/chebyshev.hpp:23` (`ChebyshevSmoother`), `chebyshev.hpp:86` (`ChebyshevSmoother1stKind`) — matrix-free polynomial smoothing `y = y + p(A)(x − A y)` (`chebyshev.cpp:193`). The header explicitly cites **Adams et al., "Parallel multigrid smoothing: polynomial versus Gauss–Seidel," JCP (2003)** (`palace/linalg/chebyshev.hpp:82`) — Palace deliberately uses a polynomial smoother *in place of* Gauss-Seidel, precisely because the GS triangular sweep does not parallelize / does not lift to a global tensor-field op.
- `palace/linalg/distrelaxation.hpp:30` (`DistRelaxationSmoother`) — Hiptmair distributive relaxation, which wraps two `ChebyshevSmoother` instances (`distrelaxation.cpp:23-33`), not a triangular sweep.

**(b3) Direct-solver factorizations are external-library wrappers.** The full LU/Cholesky factorizations (whose forward/back substitution *is* a triangular solve) live entirely inside external libraries; Palace only wraps them:
- `palace/linalg/strumpack.hpp:21` — `StrumpackSolverBase : public StrumpackSolverType` (subclasses `mfem::STRUMPACKSolver`; "A wrapper for the STRUMPACK direct solver package", `strumpack.hpp:18`).
- `palace/linalg/superlu.hpp:22` — `SuperLUSolver : public mfem::Solver`.
- `palace/linalg/mumps.hpp:21` — `MumpsSolver : public mfem::MUMPSSolver`.

The triangular substitutions inside these factorizations are owned by STRUMPACK / SuperLU / MUMPS (and ultimately out of scope as opaque-library kernels), not by Palace source.

**(b4) The "block lower-triangular preconditioner" is NOT a scalar triangular solve.** `palace/linalg/blockprecond.hpp:16-29` defines `BlockDiagonalPreconditioner` with an optional lower off-diagonal `L10`, applied as a 2×2 **block** forward substitution: `z0 = P0^{-1} r0; z1 = P1^{-1}(r1 − L10 z0)` (`blockprecond.hpp:25-27`). The "forward solve" here applies the diagonal sub-solvers `P0`, `P1` to whole blocks — it is block-structured Gaussian elimination at the 2-block level, not an element-wise triangular substitution against the matrix entries. This is a red herring for `trsv` (it is the same block-triangular concept seen at `modeeigensolver.cpp:448`, `modeeigensolver.hpp:245`), and should not be conflated with a triangular-solve primitive.

**Connection to `book/src/L3/index.md:7`**: that L3 Context paragraph already names "Gauss-Seidel-flavored smoothers, certain triangular solves, sequentially-reordered preconditioners" as canonical L3 obstructions where no global tensor-field form exists. The present localization is the concrete L0 evidence behind that note: the only triangular solves in Palace are (b1) HYPRE-internal GS/SSOR sweeps and (b3) external-library direct-solver substitutions — both opaque, both un-liftable, both already anticipated by the L3 index.

### (c) ROUTING RECOMMENDATION: (ii) obstruction-theme target

`trsv` is **not a firm-L1-operator candidate** and **not a "something else" leaf** — it is an **obstruction-theme target** (route to a follow-on `abstractor` obstruction-theme dispatch). Justification with citations:

1. **No standalone API to anchor a firm L1 operator** — the zero-hit searches above + the GS-free `densematrix.hpp:24-36` API mean there is no positive Palace source site exposing a `trsv`-shaped function to lower. An L1 firm operator requires a positive source site (the `apply_linop` / `ksp_solve` standard); there is none.
2. **Where triangular solves do occur, they are opaque-library-owned** — HYPRE relax-type flags (`amg.cpp:19`, `ams.cpp:162`) and external direct-solver wrappers (`strumpack.hpp:21`, `superlu.hpp:22`, `mumps.hpp:21`). These match the established **opaque-library-ownership obstruction** shape — the *same reason* the L3 `eigsolve` is `partial-obstruction` (the SLEPc/ARPACK loop is library-owned, `book/src/L3/index.md:31`, `:45`). The obstruction theme should cite these as negative anchors.
3. **Palace deliberately avoids the GS triangular sweep** — the Chebyshev-over-Gauss-Seidel choice (`chebyshev.hpp:82`, Adams et al. 2003) is itself evidence that the triangular solve is a recognized non-liftable / non-parallelizable obstruction Palace engineered around. The GPU fallback flipping `relax_type` from GS to Jacobi (`amg.cpp:24`) reinforces this. The obstruction theme can note this as the *reason* the obstruction is load-bearing rather than incidental.

**Per the unimplemented/opaque-stub policy** (CLAUDE.md §Scope): document the obstruction with negative-anchor citations; do **not** target a general `trsv` for filling in. A literature-anchored `trsv` form *may* later inform higher abstractions if it simplifies an L2/L4 combinator, but there is no current upstream simplification that would license promoting it to firm — so it stays obstruction documentation.

**Follow-on dispatch shape** (for the planner): an `abstractor` L1>L0 obstruction theme, slug suggestion `triangular-solve-obstruction` (or `trsv-obstruction`), citing (b1)+(b3)+(b4) as negative anchors and connecting to `book/src/L3/index.md:7`. Optionally a thin L3 obstruction row mirroring the `eigsolve`/`chebyshev` `partial-obstruction` precedent IF a consuming L3 context wants `trsv` named — but since no Palace operator *exposes* `trsv` (it only appears inside opaque calls), the cleaner home is a single L1>L0 obstruction theme, with the L3 index's existing line `:7` already covering the L3 side. This closes the `trsv` leaf of OQ `l3-vocabulary-inventory-gap` as **resolved-by-obstruction** rather than leaving it perpetually BLOCKED.

## Supporting evidence

Citation self-verification (all load-bearing pinpoints checked against on-disk via `tools/citecheck/citecheck.py --anchor`; codemap `read_range` used for localization only):
- `reference/palace/palace/linalg/amg.cpp:19` anchor `'l1-symm. GS'` — OK (line 19).
- `reference/palace/palace/linalg/ams.cpp:162` anchor `'l1-SSOR'` — OK (line 162).
- `reference/palace/palace/linalg/ams.cpp:173` anchor `'HYPRE_AMSSetSmoothingOptions'` — OK (line 173).
- `reference/palace/palace/linalg/blockprecond.hpp:25` anchor `'forward solve'` — OK (line 25).
- `reference/palace/palace/linalg/chebyshev.hpp:82` anchor `'polynomial versus Gauss'` — OK (line 82).

Localization-only evidence (codemap, not pinpoint-cited for prose claims but corroborating):
- `densematrix.hpp:24/26/28/30/32/34/36` API list (no triangular solve) — codemap `search_text`.
- `strumpack.hpp:18/21`, `superlu.hpp:22`, `mumps.hpp:21` direct-solver wrapper class declarations — grep.
- `jacobi.hpp:15-19`, `chebyshev.hpp:23/86`, `distrelaxation.hpp:30` smoother cohort — codemap `search_text`.
- `amg.cpp:24` (GPU GS→Jacobi flip), `amg.cpp:29` (`HYPRE_BoomerAMGSetRelaxType`), `ams.cpp:158/179` (AMG sub-relax types) — codemap `read_range`.
- Zero-hit searches: `trsv|trsm|TriSolve|TriangularSolve|SpTrSV` (whole tree); `class …(GaussSeidel|SOR|ILU|IncompleteLU|IC0|Cholesky)…Smoother` (whole tree).

## Open questions / caveats

- **OQ `l3-vocabulary-inventory-gap` — `trsv` leaf**: recommend closing as **resolved-by-obstruction** (route to obstruction theme) rather than BLOCKED. The other three leaves (`gemv`/`ksp_solve`/`eigsolve`) are done; `trsv` is the last, and it terminates in an obstruction, not a firm operator. The planner should migrate this into the plan as a small `abstractor` obstruction-theme item (low fan-out: an obstruction leaf consumed by no upstream combinator), or accept the L3-index `:7` line as already-sufficient documentation and close the leaf with no further dispatch. I lean toward authoring the thin L1>L0 obstruction theme so the OQ closes with a citable home rather than an in-prose mention.
- **`back_solve` disambiguation**: the firm `book/src/L1/back_solve.md` (c027) is the small-dense GMRES/FGMRES restart-correction triangular back-substitution. A future obstruction theme for general `trsv` should cross-reference `back_solve` to make explicit that Palace *does* author one narrow triangular-substitution leaf (Krylov-internal, small-dense, sequential-by-construction) but **no general sparse/dense `trsv` primitive** — these are different objects and the existence of the former does not promote the latter.
- **Scope note (no caveat, just flagging)**: STRUMPACK/SuperLU/MUMPS internal triangular substitutions are out of scope as opaque-library kernels (CLAUDE.md §Target system — "Many symbols resolve into upstream libraries … cite Palace source, not vendored upstream"). The obstruction theme cites the Palace *wrapper* sites as negative anchors; it does not attempt to dissect the library factorizations.
- **Did NOT author any `book/` content** (localization-only dispatch + dispatch-phase write-guard). No layer-intro refresh needed — `book/src/L3/index.md:7` already carries the correct obstruction framing; if the follow-on obstruction theme lands, the layer-intro-author may want to add a back-reference from `:7` to the new theme file (note for that dispatch, not this one).
