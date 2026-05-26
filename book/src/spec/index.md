# Specification — Slice Status

The specification grows as a set of **slices** (one per algorithm / routine / coherent piece of Palace), each pushed depth-first through the four-layer stack L1 → L2 → L3 → L4 above the cited L0 source.

This index is maintained by the Synthesizer after every push. It is the **first place to read** to see where the work is.

## Status table

| Slice | Highest layer | Last touched | Status notes |
|-------|---------------|--------------|--------------|
| [CG](./slices/cg.md) | L1 | 2026-05-26 | L0 cited to palace/linalg/iterative.cpp::CgSolver::Mult; L1 form names CgState bundle and the standard preconditioned CG recurrence; all three variant axes (scalar field, preconditioner present/absent, initial guess) absorbed parametrically. |
| [GMRES](./slices/gmres.md) | L4 v0.6 | 2026-05-26 | L0/L1/L2/L3/L4 with v0.6 stop-witness extraction: `PostKrylov` carries a `StopReason` constructor field, eliminating the `error` arm in `classify`; `check_stop` becomes the sole budget-axis dispatch site. |
| [Orthogonalization (plane-rotation stream)](./slices/orthog.md) | L4 (Gram-Schmidt) + L1 (plane-rotation) | 2026-05-26 | Gram-Schmidt stream at L4 (state-stratified, Solve-monadic, sequential-obstruction at L4). Plane-rotation stream lifted to L1 in same slice; uses `givens` and `trsv` primitives. Open question: split into orthog/gram_schmidt and orthog/plane_rotation once both reach L4. |
| [divfree](./slices/divfree.md) | L4 | 2026-05-26 | Full rotation L0→L4; tightening pass closed copy/alias ambiguity in L1 and flagged WeakDiv sign-convention as the remaining L0 open question (carries through all layers). |
| [chebyshev](./slices/chebyshev.md) | L4 | 2026-05-26 | L4 form: ChebOp<E,S> closure with variant-typed scalar state, Solve-monad apply with forM_/foldM sequential obstructions; capability-typed ChebSim, initial_guess as per-call Bool (not a variant axis). |
| [plane rotation stream](./slices/plane_rotation_stream.md) | L3 | 2026-05-26 | L3 negative result: replay-prefix loop is class-(a) sequential obstruction (shared boundary slot read-after-write); per-step extend/apply triple lifts trivially. Canonical small-N obstruction case. |
| [arnoldi step](./slices/arnoldi_step.md) | L4 | 2026-05-26 | Tightening refinement: clarified scope-separation rationale for the small-dense Givens obstruction vs. field-side MGS obstruction in Open questions. Substantive: the two obstructions live on disjoint state (DoF-space `w`-mediated vs. small-dense `H[:,j]`-mediated) and have different variant-dependency profiles. |
| [sparse triangular solve](./slices/sparse_triangular_solve.md) | L0 (obstruction) | 2026-05-26 | Negative result: no Palace-level sparse triangular solve. Palace forwards into MFEM-wrapped SuperLU/STRUMPACK/MUMPS as opaque ksp_solve. L0→L1 rotation declared out-of-scope-obstructed; follow-up slice `sparse_direct_solver_wrapper` proposed. |
| [cg_preconditioning_framework](./slices/cg_preconditioning_framework.md) | L4 v0.3 | 2026-05-26 | L4 v0.3 self-rotation: derived-view hoisting for `OpBinding<E>`. The `finestLevelUnwrap` branch in `setOperators` is hoisted out of the body into a `pcBoundOp(binding, pc)` derived view; `OpBinding<E>` now stores only the primitive operator inputs, eliminating the stored-vs-bound divergence the v0.2 form left as a structural hazard. |
| [polynomial recurrence step](./slices/polynomial_recurrence_step.md) | L1 | 2026-05-26 | Negative-result catalog: no Palace-level `polynomial_recurrence_step` kernel. Three independent sites (Chebyshev-4th-kind, Chebyshev-1st-kind, GMRES Givens stream) catalogued with state schemas; eigenvalue-tracking branch obstructed (below Palace boundary, delegated to SLEPc/ARPACK). |

## Slice conventions

- **Granularity**: one slice per coherent algorithm or routine.
- **File shape**:
  - Small / medium slices → single file: `book/src/spec/slices/<snake_case_slice_name>.md`, with consistent `## L0` / `## L1` / `## L2` / `## L3` / `## L4` section headings.
  - **Genuinely large slices** → subdirectory **from the start**: `book/src/spec/slices/<slice_name>/`. Split into per-layer files (`l0.md`, `l1.md`, …) or per-aspect files (`overview.md`, `state_types.md`, `step.md`, `convergence.md`, …) per Synthesizer's judgment. The subdirectory should have an `index.md` that orients the reader and links to the per-piece files.
  - Reach for the subdirectory shape when the single-file form would exceed ~400 lines or any L-section would become book-chapter-sized. Splitting after-the-fact is more disruptive than planning multi-file from the start.
- **Per-slice section headings**: each slice file uses the headings `## L0` / `## L1` / `## L2` / `## L3` / `## L4` consistently. Within each, sub-headings as needed.
- **L0 citations**: plain text `reference-relative/path/file.ext:start-end`, e.g., `palace/linalg/cg.cpp:42-67`. Editors with line-aware navigation (VS Code, etc.) resolve these directly against the local clones under `reference/`.
- **Optional agent-facing sections** (may appear on any slice file):
  - **`## Context`** — at the top, after the title: a short paragraph orienting a fresh reader. Why this slice exists, what it covers, what to know before reading the layered content.
  - **`## Working Notes`** — at the bottom, after L4: a loose-form section for issues, todos, ongoing needs, breadcrumbs for the next agent. The place to leave "I noticed X but didn't address it" without forcing it into the question ledger or `problems/`.

## Recommended file template

```markdown
# <slice name>

## Context
(optional — short orientation paragraph)

## L0
- `palace/path/file.cpp:start-end` — what this range is.
- ...

## L1
...

## L2
...

## L3
...

## L4
...

## Working Notes
(optional — todos, open questions tied to this slice, breadcrumbs)
```

## Slice acceptance criteria

Added 2026-05-24 meta-review (cycles 1–3 enactment).

A slice diff produced by the Synthesizer is **accepted** (eligible for the Critic to verdict `pass`) only when all of the following hold:

1. **Single closed rotation chain.** A slice must form a single closed L0→L1 reduction. If any link in the chain is unverified or deferred to an "Open questions" section, the slice MUST be split into (a) one closed slice covering the verified portion and (b) one explicitly-deferred slice scoping the unknown, rather than asserted as complete. Originating example: cycle 1's `cg_solver_integration` attempted to span ProblemType dispatch, IoData resolution, AND BaseKspSolver composition with the middle link unverified — the Critic correctly flagged the slice as over-scoped.

2. **Per-assertion rotation_claim coverage.** Every L1 assertion that compresses one or more L0 facts must be accompanied by a `rotation_claim` entry with `file:line` citation (per `prompts/synthesizer.md` *Output discipline*). A slice diff with zero rotation_claims is structurally unauditable. Originating example: cycle 2's GMRES L1 slice was a substantive prose decomposition with zero rotation_claims — verdict `pass` from the Critic on what was actually unverifiable narrative.

3. **Genuine rotation per `book/src/concepts/rotation.md`.** For every Li → Li+1 transition the slice proposes, at least one of {state hiding, coarser substitution, threaded-state compression} must hold. A renaming-only rotation is not a rotation. The Critic verifies this per check #8 in `prompts/critic.md`. Originating example: cycle 3's GMRES L1→L2 collapsed to primitive renaming — same index arithmetic, same threaded state bundle.

These criteria are layered on top of the citation-mandatory and methodology-conformance rules in `CLAUDE.md`. A slice can technically pass the Critic's per-claim verification while failing these structural rules; the Critic checks both.

## Push history

The full push history (forward / back / sideways) is in the episodic log (`episodic.jsonl` at the repo root once the agent loop is running). This page summarizes only the *current* state.
