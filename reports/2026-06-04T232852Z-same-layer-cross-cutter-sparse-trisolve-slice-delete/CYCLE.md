---
agent: same-layer-cross-cutter
invoked_at: 2026-06-04T232852Z
scope: L1-L0 cross-cut — absorb-and-delete the sparse_triangular_solve negative-result slice
status: integrated
integrated_at: 2026-06-04T232852Z
integration_commit: 8c3b94baa1ff30bb724c108631c394bf7a471a41
integration_notes: "Applied clean by integrator-per-report (D3); sparse_triangular_solve slice DELETED + L0 findings absorbed into L1-L0/triangular-solve-obstruction.md §(d) + 7 anchors appended + 3 concept repoints + self-link collapse + annotated-and-retained framing retired. Batch finalize cycle-097: cargo make book EXIT 0, step-5b rank_violations=0 (GATE PASS), no newly-orphaned node. retroactive-budget global 0. OQs sparse-trisolve-rename-to-sparse-direct-solver-wrapper + sparse-trisolve-mfem-superlu-factor-allgatherv-family recommended-CLOSE for the batch-31 meta unify."
---

# CYCLE: L1-L0 observation — sparse-trisolve slice absorb-and-delete

## Summary

Comparing the Phase-1 negative-result slice `book/src/spec/slices/sparse_triangular_solve.md`
against its firm layered home `book/src/L1-L0/triangular-solve-obstruction.md`, I find the two
records carry **overlapping** L0 anchors (superlu/strumpack/mumps/blockprecond, all class-declaration
negative anchors) but the slice carries **three unique L0 findings the obstruction theme does NOT
yet hold**: (1) the *opaque-forwarding catalog* — that the Palace wrapper bodies literally forward
`Mult`/`MultTranspose`/`ArrayMult`/`ArrayMultTranspose` into MFEM and explicitly DISABLE iterative
refinement; (2) the `Mult2`/`MultTranspose2` solver-interface distinction (the `*2` variants are
multigrid-smoother workspace, not triangular-solve workspace, and the wrappers don't override them);
(3) the two negative *no-factor-MPI / residual-is-the-caller's* findings (Allgatherv's sole call
site is mesh edge-attribute gather, not factor movement; the wrappers install as preconditioner with
the outer Krylov owning residual). Under the graded-stack §6 retirement, the slice's
`annotated-and-retained` carve-out (slice `:3-10`) is eliminated; once these three findings are
absorbed into the firm theme and the inbound concept anchors repointed, the slice is
reachability-GC detritus (no inbound `depends-on` blocking edge — every referrer is a `reference`-kind
navigational link) and is deleted.

## Observation kind

**Redundancy** (with a residue) — the slice and the firm L1>L0 obstruction theme are two records of
the *same negative result* (the absence of a Palace-authored general triangular solve). The theme is
the firm layered home; the slice is the Phase-1-era duplicate. The redundancy is resolved by
**absorbing the slice's non-overlapping residue** (the 3 unique L0 findings) into the theme and
**deleting** the slice — the standard graded-stack P2 slice-deletion shape.

## Specific finding

### Three unique L0 findings to absorb (verified against `reference/palace` source)

**Finding 1 — opaque-forwarding catalog + iterative-refinement DISABLED.**
The obstruction theme currently anchors `superlu.hpp:22` only as a *class declaration* negative
anchor (`class SuperLUSolver : public mfem::Solver`). The slice's unique content is that the wrapper
**method bodies are literal one-line forwards** and that iterative refinement is **explicitly
disabled at construction**. Verified:

- `palace/linalg/superlu.hpp:43-58` — the four forwarding bodies, each a literal forward into the
  MFEM solver:
  ```cpp
  void Mult(const Vector &x, Vector &y) const override { solver.Mult(x, y); }
  void ArrayMult(const mfem::Array<const Vector *> &X,
                 mfem::Array<Vector *> &Y) const override { solver.ArrayMult(X, Y); }
  void MultTranspose(const Vector &x, Vector &y) const override { solver.MultTranspose(x, y); }
  void ArrayMultTranspose(const mfem::Array<const Vector *> &X,
                          mfem::Array<Vector *> &Y) const override { solver.ArrayMultTranspose(X, Y); }
  ```
- `palace/linalg/superlu.cpp:78` — `solver.SetIterativeRefine(mfem::superlu::NOREFINE);`
  (iterative refinement — the one operation that WOULD be a true factor-solve-then-residual loop —
  is turned off). Verified in context (the line sits in the constructor body, immediately after the
  `SymbolicFactorization` switch and before `SetSymmetricPattern(true)`).
- `palace/linalg/superlu.cpp:88` — `solver.SetFact(mfem::superlu::SamePattern_SameRowPerm);`
  (the factor-reuse path, gated on `reorder_reuse` — supports the contractual-invariant carry-through).
  Verified: sits inside `SetOperator`, in the `if (A && reorder_reuse)` branch.

This is genuinely additive: it shows the wrapper contributes **no factor data structure, no L/U
storage, no permutation, and no residual** — Palace authors only the forward, and the one
residual-bearing operation (refinement) is off. The theme's §(b3) currently says "Palace only wraps
them" at the class-declaration level but never cites the forwarding bodies or NOREFINE.

**Finding 2 — the `Mult2`/`MultTranspose2` solver-interface distinction.**
Not present anywhere in the obstruction theme. The `Solver<OperType>` base exposes a four-method
surface, and the `*2` (scratch-residual) variants exist for **multigrid smoothers**, NOT for
sparse-direct triangular-solve workspace; the direct-solver wrappers do not override them. Verified:

- `palace/linalg/solver.hpp:43` — `virtual void SetOperator(const OperType &op) = 0;`
- `palace/linalg/solver.hpp:45-49` — `void MultTranspose(...) const override { MFEM_ABORT(...); }`
- `palace/linalg/solver.hpp:52-56` — `virtual void Mult2(const VecType &x, VecType &y, VecType &r) const`
  (the preallocated-temporary-storage apply; base aborts).
- `palace/linalg/solver.hpp:59-63` — `virtual void MultTranspose2(const VecType &x, VecType &y, VecType &r) const`
  (transpose with preallocated temporary; base aborts).

The slice's claim that the `*2` variants are for "**multigrid smoothers** (Chebyshev, Jacobi) that
thread a residual buffer across recursive calls — *not* for sparse-direct triangular-solve
workspace" is the load-bearing distinction: a reader could mistake the scratch-`r` parameter for the
residual-workspace the scope-question's framing wanted. (The slice's `:42-65` citation pointed at
this block; the verified bounds are `solver.hpp:43-63`, with the comments documenting each method's
purpose. The base-class `Mult` itself comes from `OperType`/`Operator`, not from `Solver`.)

**Finding 3 — MPI Allgatherv is not for factors + residual is the caller's responsibility.**
Two negative findings, neither in the obstruction theme. They close the scope-question's framing
(factor-Allgatherv, residual check) at the Palace boundary. Verified:

- `palace/utils/communication.hpp:337-344` — the `Mpi::Allgatherv` wrapper definition (variable-count
  per-rank gather: `MPI_Allgatherv(sendbuf, sendcount, ..., recvcounts, displs, ..., comm)`).
- `palace/utils/geodata.cpp:1538-1539` — the **sole** Palace call site:
  ```cpp
  Mpi::Allgatherv(local_count, local_edge_attrs.data(), all_edge_attrs.data(),
                  recv_counts.data(), displs.data(), comm);
  ```
  This gathers **per-rank edge-attribute counts during mesh setup** (`all_edge_attrs`), NOT a factor
  (`L`, `U`, `P`, `Q`). Whatever factor-Allgatherv traffic the sparse-direct libraries generate lives
  inside SuperLU_DIST/STRUMPACK/MUMPS — beyond the Palace boundary, out of scope per the MPI-internals rule.
- `palace/linalg/ksp.cpp:155` / `:165` / `:187` — the SuperLU / STRUMPACK / MUMPS wrappers are
  constructed via `MakeWrapperSolver<OperType, ...>` and assigned to **`pc`** (the preconditioner of
  an outer iterative method), verified:
  ```cpp
  pc = MakeWrapperSolver<OperType, SuperLUSolver>(linear, comm, ...);   // :155
  pc = MakeWrapperSolver<OperType, StrumpackSolver>(linear, comm, ...); // :165
  pc = MakeWrapperSolver<OperType, MumpsSolver>(linear, comm, ...);     // :187
  ```
  The outer Krylov tracks its own residual; the sparse-direct apply is one opaque preconditioner step.
  No residual-of-triangular-solve check exists at Palace level (and refinement — Finding 1 — is
  disabled). (The slice's `MakeWrapperSolver` / `ksp.cpp:105-200` framing is confirmed: the function
  is declared at `ksp.cpp:104` and the three direct-solver cases install to `pc` at the lines above.)

### What is NOT unique (already in the theme — do not re-absorb)

- The `superlu.hpp:22` / `strumpack.hpp:18-21` / `mumps.hpp:21` class-declaration negative anchors
  (theme §(b3), Verified-against `:428-443`).
- The `blockprecond.hpp:16-29` red-herring (theme §(c) + Applicability cond. 3).
- The general-`trsv`-has-no-Palace-site claim (theme's entire thesis).
- The literature framing (Davis 2006 / Li 2005 / Ghysels 2016 / Amestoy 2001) — the theme is
  citation-grounded on Palace negative anchors; the slice's literature paragraph is background, not
  an L0 finding, and is dropped on deletion (git history retains it).

### Old carve-out being eliminated (slice `:3-10`)

The slice's `> **Reduction status ... annotated-and-retained**` header (lines `:3-10`, repeated at
`:6`/`:8`) is the OLD carve-out framing the graded-stack §6 retires. It is removed **by deletion** of
the whole slice — no separate stub is left (the graded-stack replacement for `annotated-and-retained`
is a `roadmap_goal` chapter where intent persists, but a *redundant duplicate of a firm theme* is GC
detritus, not orphaned intent — there is nothing to preserve that the firm theme won't hold post-absorption).

## Recommendation

**Apply the absorption + repoints + deletion below (this dispatch is the harvester-equivalent for a
negative-result slice — there is no positive form to harvest, only a finding-residue to fold into the
firm obstruction theme).** No follow-up combinator-miner / harvester dispatch is needed; the absorption
is complete in this report's proposed-changes. After integration, the firm theme
`triangular-solve-obstruction.md` is the sole home for this negative result.

## Proposed changes

### Change 1 — ABSORB the 3 unique findings into `book/src/L1-L0/triangular-solve-obstruction.md`

Insert a new subsection **(d)** into the §"L0 form (RHS)" block, immediately AFTER the §(c) red-herring
subsection (after current line 199, before `## Applicability conditions` at line 201). This holds the
three absorbed findings with verified Palace L0 cites.

```edit
file: book/src/L1-L0/triangular-solve-obstruction.md
after_line: 199
insert: |

  ### (d) The direct-solver wrappers are pure opaque forwarders — no factor, no MPI, no residual at the Palace level

  (Absorbed cycle-097 from the retired Phase-1 `sparse_triangular_solve` negative-result slice; these
  are the slice's three unique L0 findings, re-verified against source. The wrapper *class declarations*
  are already anchored in §(b3); the additional facts here are that the wrapper **bodies** are literal
  forwards, that the one residual-bearing operation is disabled, and that no Palace MPI / residual
  machinery surrounds the factor.)

  **(d1) The wrapper method bodies are literal forwards; iterative refinement is DISABLED.** The
  `SuperLUSolver` wrapper's four apply methods forward verbatim into the MFEM solver, contributing no
  factor data structure, no `L`/`U` storage, no permutation, and no residual:

      // superlu.hpp:43-58
      void Mult(const Vector &x, Vector &y) const override { solver.Mult(x, y); }
      void ArrayMult(...) const override { solver.ArrayMult(X, Y); }
      void MultTranspose(const Vector &x, Vector &y) const override { solver.MultTranspose(x, y); }
      void ArrayMultTranspose(...) const override { solver.ArrayMultTranspose(X, Y); }

  Critically, the one operation that would be a true factor-solve-then-residual loop — iterative
  refinement — is **explicitly turned off** at construction:

      // superlu.cpp:78
      solver.SetIterativeRefine(mfem::superlu::NOREFINE);

  Factor reuse across `SetOperator` calls is the only solver-state knob Palace touches, gated on
  `reorder_reuse` (`superlu.cpp:88`: `solver.SetFact(mfem::superlu::SamePattern_SameRowPerm)`) — and
  even that is MFEM-enforced, not a Palace-authored factor operation. The substitution interior stays
  opaque-library-owned (cf. §(b3)).

  **(d2) The `*2` scratch-residual interface is multigrid-smoother workspace, NOT triangular-solve
  workspace.** The `Solver<OperType>` base exposes a four-method surface; the `Mult2` / `MultTranspose2`
  variants accept a preallocated scratch residual `r` and exist for **multigrid smoothers** (Chebyshev,
  Jacobi) that thread a residual buffer across recursive calls — not for sparse-direct triangular-solve
  workspace, and the direct-solver wrappers do not override them:

      // solver.hpp:43        virtual void SetOperator(const OperType &op) = 0;
      // solver.hpp:45-49     void MultTranspose(...) const override { MFEM_ABORT(...); }
      // solver.hpp:52-56     virtual void Mult2(const VecType &x, VecType &y, VecType &r) const   // base aborts
      // solver.hpp:59-63     virtual void MultTranspose2(const VecType &x, VecType &y, VecType &r) const   // base aborts

  This forecloses a reading in which the scratch-`r` parameter is the residual-workspace a sparse
  triangular solve would carry: the `r` buffer belongs to the polynomial/Jacobi smoother recursion
  (cf. [`chebyshev`](../L3/chebyshev.md)), not to any factor substitution.

  **(d3) No Palace MPI moves a factor, and the residual is the outer Krylov's responsibility.** The
  scope-question framing (factor-Allgatherv + residual-of-triangular-solve) has no Palace-side referent:

  - `Mpi::Allgatherv` (`communication.hpp:337-344`) is invoked at exactly **one** Palace call site,
    `geodata.cpp:1538-1539`, to gather per-rank **edge-attribute counts during mesh setup**
    (`all_edge_attrs`) — never a factor (`L`, `U`, `P`, `Q`). Any factor-Allgatherv traffic lives
    inside SuperLU_DIST / STRUMPACK / MUMPS, beyond the Palace boundary (out of scope per the
    MPI-internals rule, CLAUDE.md §Scope).
  - The wrappers install as the **preconditioner** of an outer iterative method
    (`ksp.cpp:155` / `:165` / `:187`: `pc = MakeWrapperSolver<OperType, {SuperLU,Strumpack,Mumps}Solver>(...)`,
    function declared `ksp.cpp:104`). The outer Krylov tracks its own residual; the sparse-direct apply
    is one opaque preconditioner step. Combined with the NOREFINE disable in (d1), there is no
    residual-of-triangular-solve check anywhere at the Palace level.

  Together (d1)–(d3) close the original scope question (forward/transpose pair, in-place vs.
  out-of-place workspace, factor-Allgatherv, residual check) entirely on the *negative* side: each named
  primitive resolves to either an MFEM/third-party-internal mechanism or a deliberately-disabled path.
```

Also extend the §"Verified-against" L0-evidence list (the prose bullet list, after the
`blockprecond.hpp:16-29` bullet ending at line 359, before the "Two exhaustive whole-tree zero-hit
codemap text searches" paragraph at line 361) with the seven newly-cited absorbed anchors:

```edit
file: book/src/L1-L0/triangular-solve-obstruction.md
after_line: 359
insert: |
  - `palace/linalg/superlu.hpp:43-58` — the four `SuperLUSolver` apply bodies (`Mult` / `ArrayMult` /
    `MultTranspose` / `ArrayMultTranspose`), each a literal one-line forward into `mfem::SuperLUSolver`;
    the wrapper contributes no factor / residual machinery. (Absorbed from the retired slice, §(d1).)
  - `palace/linalg/superlu.cpp:78` — `solver.SetIterativeRefine(mfem::superlu::NOREFINE);` — iterative
    refinement (the one factor-solve-then-residual loop) is explicitly DISABLED. (Absorbed, §(d1).)
  - `palace/linalg/superlu.cpp:88` — `solver.SetFact(mfem::superlu::SamePattern_SameRowPerm);` — the
    sole factor-reuse knob, gated on `reorder_reuse`; MFEM-enforced, not a Palace factor op. (Absorbed, §(d1).)
  - `palace/linalg/solver.hpp:43-63` — the `Solver<OperType>` base interface: `SetOperator` (`:43`),
    `MultTranspose` (`:45-49`), `Mult2` (`:52-56`), `MultTranspose2` (`:59-63`); the `*2` scratch-residual
    variants are multigrid-smoother workspace (base-class `MFEM_ABORT`), not triangular-solve workspace,
    and the direct-solver wrappers do not override them. (Absorbed, §(d2).)
  - `palace/utils/communication.hpp:337-344` — the `Mpi::Allgatherv` variable-count wrapper definition.
    (Absorbed, §(d3).)
  - `palace/utils/geodata.cpp:1538-1539` — the sole Palace `Mpi::Allgatherv` call site: gathers per-rank
    edge-attribute counts during mesh setup (`all_edge_attrs`), NOT a factor. (Absorbed, §(d3).)
  - `palace/linalg/ksp.cpp:155` / `:165` / `:187` — the SuperLU / STRUMPACK / MUMPS wrappers are
    constructed via `MakeWrapperSolver<OperType, ...>` (declared `ksp.cpp:104`) and installed as the
    preconditioner `pc` of an outer iterative method; the outer Krylov owns the residual. (Absorbed, §(d3).)
```

(Optional, integrator's discretion: the structured `verified_against:` YAML block at `:383-475` MAY
receive matching `verdict: negative-anchor` entries for the seven absorbed cites with
`audited_at: 2026-06-04T232852Z` and `note:` mirroring the prose bullets above. Not required for the
absorption to be sound — the prose Verified-against list is the load-bearing record; the YAML is the
machine-checkable mirror.)

### Change 2 — UPDATE the theme's self-reference to the (now-deleted) slice

The theme's §"Related" (lines 273-308) and its `verified_against` YAML entry at `:464-467` link the
slice as a cross-link partner. After deletion the slice link is a dangling `linkcheck2` error and the
`annotated-and-retained` framing is retired. Repoint to ground-truth + collapse the cross-link.

Replace the §"Related" slice-cross-link paragraph. Current lines 273-308 open:

```edit
file: book/src/L1-L0/triangular-solve-obstruction.md
replace_lines: 273-308
with: |
  ## Related

  This theme is the **sole** home for the negative result that Palace authors no general
  triangular-solve primitive. (Through cycle-096 a Phase-1 duplicate,
  `spec/slices/sparse_triangular_solve.md`, co-recorded this finding under the now-retired
  `annotated-and-retained` carve-out; per the graded-stack §6 retirement that slice was absorbed
  into this theme — its three unique L0 findings are §(d) above — and deleted in cycle-097. git
  history retains the slice.)

  The two concept pages that previously named the slice as their §"Canonical instance" now point here:

  - [`scope-out-obstruction`](../concepts/scope-out-obstruction.md) §"Canonical instance" — the L0→L1
    scope-out obstruction (Palace forwards sparse-direct solves into MFEM / SuperLU_DIST / STRUMPACK /
    MUMPS opaquely; no Palace-level triangular-solve form to lift). This theme is the L0-evidence home.
  - [`sequential-obstruction`](../concepts/sequential-obstruction.md) §"Sub-kind:
    out-of-scope-obstruction" — the out-of-scope sub-kind distinguished from genuine L2→L3 sequential
    obstruction; this theme holds the L0 wrapper-surface evidence.

  This L1>L0 theme sits alongside [`minres-iteration`](./minres-iteration.md) and
  [`bicgstab-iteration`](./bicgstab-iteration.md) as the third obstruction-flavoured L1>L0 theme. It
  additionally records the engineered-absence evidence (Adams-2003 polynomial-over-GS,
  GPU GS→Jacobi flip) — see §(b2) — that the obstruction is deliberate.
```

Replace the `verified_against` YAML entry for the slice (lines 464-467) with a deletion-record entry
so the machine-checkable list no longer cites a dangling file:

```edit
file: book/src/L1-L0/triangular-solve-obstruction.md
replace_lines: 464-467
with: |
      - citation: book/src/L1-L0/triangular-solve-obstruction.md
        verdict: absorbed-and-deleted
        audited_at: 2026-06-04T232852Z
        note: "Phase-1 negative-result slice `spec/slices/sparse_triangular_solve.md` absorbed into this theme (§(d) — opaque-forwarding catalog + NOREFINE, the `*2` smoother-workspace distinction, no-factor-MPI / outer-residual) and DELETED cycle-097 per graded-stack §6 (annotated-and-retained carve-out retired). git history retains the slice. The two concept pages it was the canonical instance of (scope-out-obstruction, sequential-obstruction) now point to this theme."
```

(The two concept-page `verified_against` YAML entries at `:468-475` — `scope-out-obstruction.md:68`
and `sequential-obstruction.md:53` — remain VALID after Change 3 repoints; their line anchors may
shift by a line or two from the repoint edits. Integrator: re-anchor the `:68` / `:53` line numbers if
the repointed concept-page edits move them, but the citations themselves stay.)

### Change 3 — REPOINT the inbound concept anchors off the slice

**3a — `book/src/concepts/scope-out-obstruction.md:68`** (the §"Canonical instance" link). Repoint the
slice link onto the firm theme + L0:

```edit
file: book/src/concepts/scope-out-obstruction.md
replace_lines: 68-68
with: |
  [triangular-solve-obstruction](../L1-L0/triangular-solve-obstruction.md) (the firm L1>L0 home;
  the absorbed §(d) holds the wrapper-surface L0 evidence — sparse triangular solves with
```
(The continuation prose on lines 69-78 — "the scope question targeted sparse triangular solves with
factor-Allgatherv and residual checks…" — is preserved; only the opening link target on `:68` changes.
The bare `sparse_triangular_solve` *token* no longer appears as a link; the prose remains accurate.)

**3b — `book/src/concepts/sequential-obstruction.md:53`** (the §"Sub-kind: out-of-scope-obstruction"
link — CONFINED to this region; D4 owns `:83-85`). Repoint the slice link onto the firm theme.
**Context-anchored (NOT a bare line number)** so the edit survives D4's `:83-85` edits regardless of
apply order: the `[old]` block carries the unique line-52 sentence opener as context, so the
integrator's by-context match locates the link independent of any line-shift D4 introduces.

```edit
file: book/src/concepts/sequential-obstruction.md
old: |
  A structurally distinct sub-kind of obstruction surfaced in the
  [sparse_triangular_solve slice](../spec/slices/sparse_triangular_solve.md):
new: |
  A structurally distinct sub-kind of obstruction surfaced in the
  [triangular-solve-obstruction theme](../L1-L0/triangular-solve-obstruction.md) (the firm L1>L0 home
  for the absorbed `sparse_triangular_solve` negative result):
```
The plain-text token `sparse_triangular_solve` at `:79` ("in `sparse_triangular_solve`'s case: rename
to `sparse_direct_solver_wrapper`") is **not a link** and does not break on deletion; however the
rename-to-`sparse_direct_solver_wrapper` suggestion is a retired OQ (see Open questions). Integrator's
discretion to soften `:79` to past tense ("the absorbed sparse-trisolve case, whose follow-up rename OQ
is retired"); not required for linkcheck.

**3c — `book/src/concepts/negative-result-slice.md:47`** (the §"Examples in this spec" bullet — planner
named `concepts/negative-result-slice.md` in scope). Repoint the slice link onto the firm theme:

```edit
file: book/src/concepts/negative-result-slice.md
replace_lines: 47-47
with: |
  - [`triangular-solve-obstruction`](../L1-L0/triangular-solve-obstruction.md) (the firm L1>L0 home; the
    Phase-1 `sparse_triangular_solve` slice was absorbed here cycle-097) — the scope question (sparse
    `Ly=b`/`Uy=b`, factor Allgatherv, residual check) returns a negative result: Palace carries no
    Palace-level triangular-solve form. SuperLU/STRUMPACK/MUMPS are thin opaque `mfem::Solver`
    forwarders (the factor interior lives below the project boundary). This is the canonical L0→L1
    **scope-out obstruction** (`trsv` obstruction-shadow) — the L0→L1 analogue of
    [`sequential-obstruction`](./sequential-obstruction.md)'s L2→L3 negative result.
```

### Change 4 — DELETE the slice file

```edit
file: book/src/spec/slices/sparse_triangular_solve.md
action: delete
rationale: |
  Reachability-GC detritus per graded-stack §6 + §Axis-2. After Changes 1-3, the slice's three unique
  L0 findings live in the firm theme triangular-solve-obstruction.md §(d), and all inbound links are
  repointed. Confirmed: NO inbound `depends-on` blocking edge targets the slice (the slice carries no
  typed frontmatter; every referrer — scope-out-obstruction.md:68, sequential-obstruction.md:53,
  negative-result-slice.md:47, the firm theme's §Related + verified_against — is a `reference`-kind
  navigational link, now repointed). The remaining bare-token mentions are non-link prose
  (L2-L1/incremental-least-squares-composition-lowering.md, L1/back_solve.md, meta-reviews/*) that name
  the general `trsv` / `sparse_triangular_solve` *shape*, not the slice file, and do not break.
  NOTE: book/src/SUMMARY.md:300 and book/src/spec/index.md:21 also register the slice — those rows are
  OWNED BY D5 (out of this dispatch's scope per hard constraint); D5 removes them in the same cycle.
```

## Supporting evidence

- Slice under absorb-and-delete: `book/src/spec/slices/sparse_triangular_solve.md` (full read — the
  `annotated-and-retained` header `:3-10`; the four L0-facts §"L0 — implementation facts" `:38-121`;
  the three unique findings at §"Sparse-direct factor application is opaque MFEM forwarding" `:52-74`,
  §"Solver interface: forward/transpose pair" `:76-86`, §"MPI Allgatherv is not used for factors"
  `:88-98`, §"Residual check is the caller's responsibility" `:100-109`).
- Firm home: `book/src/L1-L0/triangular-solve-obstruction.md` (full read — §(b3) class-declaration
  anchors `:151-170`; §(c) red herring `:172-199`; §Related slice cross-link `:273-308`; Verified-against
  prose `:312-381` + YAML `:383-475`).
- L0 verification (all via `palace-codemap` `read_range`, paths relative to `reference/`):
  - `palace/linalg/superlu.hpp:43-58` (forwarding bodies), `superlu.cpp:78` (NOREFINE), `superlu.cpp:88`
    (SetFact reuse).
  - `palace/linalg/solver.hpp:43-63` (`SetOperator` / `MultTranspose` / `Mult2` / `MultTranspose2`).
  - `palace/utils/communication.hpp:337-344` (Allgatherv def), `palace/utils/geodata.cpp:1538-1539`
    (sole call site — edge-attribute gather).
  - `palace/linalg/ksp.cpp:104` (`MakeWrapperSolver` decl), `:155` / `:165` / `:187` (`pc = ...` installs).
- Inbound-link grep: `grep -rn "sparse_triangular_solve" book/src/` — link references vs. plain-token
  mentions classified above.

## Open questions / caveats

- **Retired follow-up OQs from the slice.** The slice carried two live OQs (slice `:199-209`): (1)
  rename to `sparse_direct_solver_wrapper` + re-push to L1; (2) whether an MFEM/SuperLU-level slice
  family owns the factor-Allgatherv / residual framing. Under the graded-stack redirect these are
  **retired, not migrated**: there is no Palace-side primitive to push to L1 (the whole finding is
  negative), and the MFEM-internal family is out of scope (CLAUDE.md §Target system — "cite Palace
  source, not vendored upstream"). The wrapper-as-opaque-`ksp_solve`-preconditioner rotation the
  rename was reaching for is already captured by `apply_linop` / `ksp_solve` absorption (cited in the
  slice's L1 section and unaffected). I recommend the integrator close both OQs as
  **resolved-by-obstruction** rather than carrying them forward. Flagging here rather than self-closing
  (OQ-ledger authority is meta-phase / per-report integrator, not this dispatch).
- **Collision boundary with D4 (`sequential-obstruction.md`).** My Change 3b edits ONLY `:53` (the
  out-of-scope sub-kind link); D4 edits `:83-85` (the Givens-stream worked example). These are 30 lines
  apart with no overlap. If the integrator applies both in one pass, the `:53` edit (no line-count change
  — one link line replaced by two prose lines, net +1) shifts D4's `:83-85` target down by 1; integrator
  should apply edits bottom-up (higher line numbers first) or re-anchor D4's range. Surfaced so the
  per-report integrator sequences them safely. (Repairer note cycle-097: Change 3b's `[old]` block was
  hardened from a bare `replace_lines: 53-53` to a **context-anchored** match carrying the line-52
  sentence opener, so D3's repoint locates its link by surrounding context and applies correctly
  regardless of whether D4's same-file edit lands first — the bottom-up recommendation is now a
  belt-and-suspenders convenience, no longer a correctness requirement for D3.)
- **`back_solve.md` plain-token mentions left intact.** `book/src/L1/back_solve.md:46` and `:256`
  reference `sparse_triangular_solve` as the *general-`trsv` shape* name (the sibling distinction:
  small-dense `back_solve` vs. the general field-sized `trsv`), NOT as a link to the slice file. They do
  not break on deletion and their semantics are unchanged (the theme §Applicability cond. 2 already owns
  that sibling split). Intentionally untouched — confirming this is not an oversight.
- **`L2-L1/incremental-least-squares-composition-lowering.md` token mentions** (`:148`, `:326`, `:447`)
  likewise name the general `trsv` / `sparse_triangular_solve` shape as plain prose tokens, not links.
  Untouched. (One of them, `:326`, references `scaffolding/open-questions.md:24` — an OQ-ledger line
  outside any dispatch's book-write scope; no action.)
- **YAML re-anchoring on the firm theme.** Change 2's `verified_against` YAML entries for the two
  concept pages (`:468-475`) cite `scope-out-obstruction.md:68` and `sequential-obstruction.md:53`. The
  Change-3 repoints keep those anchors valid in *meaning* but may nudge the line numbers by ±1-2.
  Integrator should re-verify the `:68` / `:53` line anchors after applying Change 3 (low-risk; the
  citations remain sound, only the line int may drift).
