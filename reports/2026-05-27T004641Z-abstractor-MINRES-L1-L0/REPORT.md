---
agent: abstractor
invoked_at: 2026-05-27T00:46:41Z
scope: L1>L0 theme sketch — MINRES algorithm structure (greenfield; obstruction-flavoured)
status: integrated
integrated_at: 2026-05-27T01:00:00Z
integration_commit: b8332b98300205740c4be4a9b1a2b30a2743dee3
integration_notes: Applied. First obstruction theme (new category). 3 rough-in operators added to L1/index.md. follow_up_agent meta-phase routed via mfem-as-l0-substrate-policy.
inputs:
  - reference/palace/palace/linalg/ksp.cpp:53-57 (MINRES enum case routed to MFEM_ABORT)
  - reference/palace/palace/utils/labels.hpp:104-112 (KrylovSolver enum lists MINRES)
  - reference/palace/palace/utils/configfile.cpp:129 (config-name mapping for "MINRES")
  - book/src/spec/slices/arnoldi_step.md (structural sibling — Lanczos is the symmetric specialisation)
  - book/src/concepts/orthogonalization.md (MGS/CGS/CGS2; Lanczos collapses to 2-term recurrence)
  - book/src/concepts/incremental-least-squares.md (running QR + Givens; MINRES uses 3×3 band variant)
  - book/src/concepts/dependency-map.md:92 (existing `minres:::planned --> arnoldi-step:::planned` node)
  - integrator-signals cycle-003 (suggested harvester dispatch; abstractor chosen instead — see Open questions)
skill_uptake:
  - skill: verify-citation-range
    triggered: true
    decision: explained_non_applicable
    rationale: Three negative-anchor citations (ksp.cpp:53-57, labels.hpp:104-112, configfile.cpp:129) verified inline by direct source read; explicit skill invocation deferred pending critic-phase mechanism stabilisation. Critic spot-verified all three verbatim in META.md (citation-validity PASS). Absence-citation pattern may warrant a dedicated skill — surfaced to meta-phase via Open question §3 and Issues found #2.
  - skill: classify-variant-axis
    triggered: true
    decision: artifact_landed
    rationale: Lanczos-vs-Arnoldi variant absorption explicitly recorded under §Justification kind (Lanczos is the symmetric specialisation of Arnoldi; band-width-3 LS is the sparsified specialisation of running QR). Preconditioner axis (B present/absent, SPD requirement), restart axis (absent), and breakdown axis classified under §Applicability conditions §§1-4. Variant absorption flagged for future same-layer-cross-cutter pass once arnoldi_step is on the dep-map (Open question §5).
  - skill: propose-rotation
    triggered: true
    decision: artifact_landed
    rationale: Theme follows propose-rotation template (LHS / RHS / applicability / justification kind / verified-against / status) with the load-bearing adaptation that justification kind is `obstruction` and RHS is explicitly empty. The L1 sketch (Lanczos 3-term + band-3 Givens) is recorded as speculative parallel to arnoldi-step, not as a realised rewrite — preserves the template shape under the obstruction case.
---

# REPORT: L1>L0 theme sketch — minres-iteration (obstruction-grounded)

## Summary

The cycle-003 integrator signal listed MINRES as a shared-infrastructure priority for a harvester (L1 operator) dispatch. On surveying Palace, MINRES appears as a configuration token but **is not implemented**: `palace/linalg/ksp.cpp:53-57` routes the `KrylovSolver::MINRES` enum case to `MFEM_ABORT("Unexpected solver type for Krylov solver configuration!")`. Palace exposes the name in `utils/labels.hpp:108` and `utils/configfile.cpp:129` (so a user can write `"MINRES"` in a JSON config) but the factory has no construction path; the enum tag is a stub-with-rejection. The theme therefore lands as an **`obstruction`-justified L1>L0 lowering**: an L1 form for MINRES can be sketched algorithmically (Lanczos three-term recurrence + Givens-rotated Hessenberg-band least-squares; standard Saad 2003 §6.7), but no Palace L0 evidence exists to ground the rewrite RHS. The L0 side of the rewrite is **empty (no Palace site)** with a structural pointer to where the construction would slot in (`ksp.cpp:53` MakeSolver switch) if MFEM's `MINRESSolver` were integrated. Speculative L1 operators are emitted as rough-ins so the harvester can pick them up the moment MINRES gets a Palace-side site (or a deliberate decision is made to treat MFEM as an L0 substrate). The theme also doubles as a documented negative-result so that downstream cycles do not re-attempt a harvester pass against the same empty corpus.

## Proposed changes

```edit:book/src/L1-L0/minres-iteration.md
# minres-iteration

The MINRES (Minimum Residual; Paige–Saunders 1975) Krylov iteration for
symmetric-indefinite linear systems. **Obstruction-flavoured theme** —
Palace exposes a `KrylovSolver::MINRES` enum tag but `MakeSolver` aborts
on it at runtime; there is no Palace-side L0 implementation to rewrite
into. The L1 form is sketched against the literature so that downstream
work has a hook, but the rewrite has no realised RHS in the Palace
corpus as of cycle-004.

## Slug

`minres-iteration`

## L1 form (LHS)

The MINRES outer iteration is structurally identical to GMRES but with the
Arnoldi step specialised to a **symmetric Lanczos three-term recurrence**
(the upper-Hessenberg matrix collapses to a symmetric tridiagonal; the
orthogonalisation loop in the Arnoldi step is replaced by two `dot+axpy`
pairs against `V[j-1]` and `V[j]` only). The outer least-squares update
acts on a band of width 3 rather than a dense Hessenberg column, but the
running-QR / Givens-rotation structure of
[`incremental-least-squares`](../concepts/incremental-least-squares.md)
is reused unchanged.

Speculative L1 per-step form (rough-in operators below):

    -- state: (V_prev, V_curr, alpha_curr, beta_curr, qr_state, s_residual)
    -- input: A  : LinOp                  -- system operator (symmetric, possibly indefinite)
    --        B  : LinOp (optional, SPD)  -- left preconditioner (preserves symmetry only if SPD)
    state_next = lanczos_step(A, B, state)            -- 3-term recurrence
        |> three_term_recurrence_update                -- emit (alpha, beta_prev, beta_curr) band column
        |> givens_apply_with_residual_min              -- band-width 3 Givens cascade; |s| is the LS residual

The full MINRES iteration is the unfolded fixpoint
`fold(lanczos_step, init_state)` with `s_residual < tol · beta_0`
termination, identical in shape to the GMRES outer loop modulo
band-vs-Hessenberg width.

## L0 form (RHS)

**Empty — no Palace site.**

The L0 anchor for the theme is the *absence* at the dispatch site:

    // [palace/linalg/ksp.cpp:53-57]
    case KrylovSolver::MINRES:
    case KrylovSolver::BICGSTAB:
    case KrylovSolver::DEFAULT:
      MFEM_ABORT("Unexpected solver type for Krylov solver configuration!");
      break;

The factory enumerates MINRES alongside CG/GMRES/FGMRES but routes it to
`MFEM_ABORT`. The config-file enum (`utils/labels.hpp:108`) and the
JSON-string mapping (`utils/configfile.cpp:129`) likewise carry a
`"MINRES"` token; both are observable to a user but result in an
abort. There is no construction site, no `MinresSolver<OperType>` class
under `palace/linalg/`, and no test linkage.

Were MINRES to be added, two structural integrations would be possible:

1. **In-tree implementation under `palace/linalg/iterative.cpp`** — a
   `MinresSolver<OperType>` class with `Mult` shaped like the existing
   `GmresSolver::Mult` (`iterative.cpp:614-642`) but with the Arnoldi
   inner body replaced by the Lanczos three-term recurrence. The
   speculative L1 operators below presume this realisation.
2. **MFEM-substrate adoption** — wrap `mfem::MINRESSolver` via the
   wrapper pattern of `MakeWrapperSolver` (`ksp.cpp:103-`). In this
   reading, MFEM is the L0 substrate; the abstractor would re-target
   the theme against vendored MFEM source (not currently checked into
   `reference/`). See Open questions.

## Applicability conditions

If MINRES is added to Palace, the L1>L0 rewrite is valid when:

1. **System symmetry**. `A = Aᵀ` (real) or `A = Aᴴ` (complex Hermitian).
   Without symmetry the Lanczos three-term recurrence loses its
   orthogonality property and MINRES no longer minimises the residual
   over the Krylov subspace.
2. **Preconditioner SPD**. If `B` is supplied, it must be symmetric
   positive definite, otherwise the preconditioned operator `BA`
   (`B`-inner-product Lanczos) is not symmetric in the `B`-inner-product
   and the recurrence breaks. (Unlike GMRES, MINRES cannot accept
   indefinite preconditioning.)
3. **No mid-iteration restart**. Unlike GMRES, MINRES has no restart
   parameter — the three-term recurrence stores only `V_prev, V_curr`,
   so the basis-storage growth that motivates GMRES restarts is absent.
4. **Breakdown handling**. `beta_curr == 0` is hard breakdown (the
   Krylov subspace is `A`-invariant; the iterate is exact). Palace's
   `iterative.cpp` `CheckDot` pattern (`iterative.cpp:643`) is the
   structural analogue, were the kernel implemented.

## Justification kind

`obstruction` — the L1 form has a clean three-term-recurrence shape and
the rewrite *would* be `structural` (the lift from a Lanczos kernel into
the pure-functional form mirrors `arnoldi-step` exactly), but the L0
side is empty: Palace does not implement the solver. The theme records
this as a first-class negative result rather than synthesising an L1
form without a Palace anchor.

The closely-related affirmative theme would be `arnoldi-iteration` (GMRES
outer loop; not yet sketched); when it lands, MINRES becomes a thin
variant axis of it — the Lanczos recurrence is the symmetric
specialisation of Arnoldi, and the band-width-3 LS update is the
sparsified specialisation of the running QR. The variant absorption is
recorded for future use; firming it requires either a Palace
implementation or an explicit decision to treat MFEM as L0 substrate.

## Speculative L1 operators

- `lanczos_step` — rough-in. Sibling of the planned `arnoldi_step`
  operator (`concepts/dependency-map.md:68-72`, currently `:::planned`).
  See Speculative operators proposed section for signature sketch.
- `three_term_recurrence_update` — rough-in. The band-column emission
  step; produces a 3-entry slice of a symmetric tridiagonal `T_j` each
  iteration.
- `givens_apply_with_residual_min` — rough-in. The band-width-3
  specialisation of the running-QR step in
  [`incremental-least-squares`](../concepts/incremental-least-squares.md);
  the LS residual `|s|` falls out of the Givens cascade as for GMRES,
  but only the last 3 entries of `s` are touched per step.

## Verified-against

L0 evidence ranges (all are *absence* citations; this is by design for
an obstruction theme):

- `palace/linalg/ksp.cpp:53-57` — `KrylovSolver::MINRES` enum case
  routed to `MFEM_ABORT`. **No construction**.
- `palace/utils/labels.hpp:104-112` — `KrylovSolver` enum definition;
  `MINRES` is item 3 of 6.
- `palace/utils/configfile.cpp:129` — JSON-string `"MINRES"` mapping;
  user-facing token exists, factory rejects.

No test linkage exists (no `test/unit/test-minres*` in
`reference/palace/test/`). No Palace site under `palace/linalg/`
implements a `MinresSolver`-shaped class.

Structural sibling (affirmative L1 evidence the rewrite would parallel):

- `book/src/spec/slices/arnoldi_step.md` — the four-line Arnoldi
  inner-body kernel (`apply → orthog → norm → scal`) is the structural
  parent of the Lanczos three-term recurrence; one-line variant axis
  (`gs_orthog` → fixed-to-symmetric) collapses Arnoldi to Lanczos.
- `book/src/concepts/incremental-least-squares.md` — the running-QR
  pattern; MINRES is the band-3 specialisation.

## Status

`rough-in` — sketched as `obstruction` per the absence in Palace; the
three speculative L1 operators are flagged for harvester promotion only
if and when a Palace-side site materialises, or when an integrator
decision is made to widen L0 to include vendored MFEM.
```

```edit:book/src/L1/index.md
[append three rows to the "Operator dep-map" table, after the existing `axpby` row, then append a "Rough-in (proposed, awaiting harvester promotion)" sub-section. Concretely:

| [`lanczos_step`](../L1-L0/minres-iteration.md) | `(A, B?, V_prev, V_curr) → (V_next, alpha, beta)` | `apply_linop`, `dot`, `axpy`, `nrm2` | `rough-in` (proposed-by: abstractor:2026-05-27T004641Z-abstractor-MINRES-L1-L0) |
| [`three_term_recurrence_update`](../L1-L0/minres-iteration.md) | `(alpha_curr, beta_prev, beta_curr) → BandColumn3` | (leaf) | `rough-in` (proposed-by: abstractor:2026-05-27T004641Z-abstractor-MINRES-L1-L0) |
| [`givens_apply_with_residual_min`](../L1-L0/minres-iteration.md) | `(qr_state, BandColumn3) → (qr_state', s_residual)` | `givens` | `rough-in` (proposed-by: abstractor:2026-05-27T004641Z-abstractor-MINRES-L1-L0) |

Note in Working Notes: these three are emitted by the `minres-iteration`
L1>L0 theme, which is `obstruction`-justified (Palace lacks MINRES); the
harvester should not attempt promotion until either (a) MINRES is added
to Palace or (b) the L0 scope is widened to include vendored MFEM.]
```

```edit:book/src/SUMMARY.md
[Append-after the existing axpby-mutation-rotation chapter line in the "L1 > L0 — Lowering" Part:

- [minres-iteration](./L1-L0/minres-iteration.md)
]
```

## Speculative operators proposed

- **`lanczos_step`**
  Intended signature: `(A: LinOp, B?: LinOp, V_prev: Vec, V_curr: Vec) → (V_next: Vec, alpha: Scalar, beta: Scalar)`.
  Motivation: the symmetric-system sibling of `arnoldi_step`. One step accepts the prior two basis columns and emits a new unit-norm column plus the diagonal entry `alpha = ⟨A·V_curr, V_curr⟩` and the subdiagonal `beta = ‖w'‖` of the symmetric tridiagonal `T`. Replaces the full orthogonalisation loop of `arnoldi_step` (over `V[0..j]`) with a fixed two-term projection (`V_prev`, `V_curr`), exploiting the theoretical orthogonality of all earlier columns when `A` is symmetric. Storage requirement collapses from `O(j)` to `O(1)` basis columns; this is *the* reason MINRES exists as a distinct method (CG-like cost on symmetric-indefinite systems where CG fails).

- **`three_term_recurrence_update`**
  Intended signature: `(alpha_curr: Scalar, beta_prev: Scalar, beta_curr: Scalar) → BandColumn3`.
  Motivation: the symmetric-tridiagonal emission step. Each Lanczos step contributes 3 nonzeros to a single column of `T_j`: entries `(j-1, j)`, `(j, j)`, `(j+1, j)` equal to `beta_prev`, `alpha_curr`, `beta_curr` respectively. This is the symmetric specialisation of the dense Hessenberg-column emission in GMRES; emitted separately because the band-width-3 sparsity is what makes the downstream Givens cascade cheap.

- **`givens_apply_with_residual_min`**
  Intended signature: `(qr_state: RunningQR, col: BandColumn3) → (qr_state', s_residual: Scalar)`.
  Motivation: the band-width-3 specialisation of the running-QR + Givens scheme described in `concepts/incremental-least-squares.md`. Because the column has only 3 nonzeros, only the trailing 2 stored Givens rotations need replay before the new rotation is generated (rather than `j` replays as in GMRES). The LS residual `|s_residual|` is exposed as a byproduct of the Givens application on the right-hand side vector `g_bar`; same pattern as GMRES, just bookkeeping-cheaper.

All three are intentionally left at signature-sketch granularity; harvester is the right role to firm them up against a concrete L0 site, which currently does not exist.

## Supporting evidence

L0 (negative-result):
- `reference/palace/palace/linalg/ksp.cpp:53-57` — MINRES enum case → `MFEM_ABORT`.
- `reference/palace/palace/utils/labels.hpp:104-112` — `KrylovSolver` enum.
- `reference/palace/palace/utils/configfile.cpp:129` — `{KrylovSolver::MINRES, "MINRES"}` JSON mapping.

Negative greps (used to confirm absence):
- `grep -ril minres reference/palace/` returns only the 3 files above; no test, no implementation source, no driver site.
- No `MinresSolver` class anywhere under `palace/`.
- No `reference/palace/` vendoring of MFEM source (`mfem::MINRESSolver` cannot be located in this tree).

Structural anchors (sibling evidence the L1 form would parallel):
- `book/src/spec/slices/arnoldi_step.md` (esp. the 4-line kernel at lines 38-48).
- `book/src/concepts/incremental-least-squares.md` (running-QR pattern).
- `book/src/concepts/orthogonalization.md` (MGS/CGS/CGS2 — collapses to fixed 2-term for symmetric).
- `book/src/concepts/dependency-map.md:92` — `minres:::planned --> arnoldi-step:::planned` (existing planned-node confirms this theme has been anticipated by earlier methodology work).

Literature anchor (for the L1 form when no L0 ground truth exists):
- Paige & Saunders 1975 *Solution of Sparse Indefinite Systems of Linear Equations* (SIAM J. Numer. Anal. 12).
- Saad 2003 *Iterative Methods for Sparse Linear Systems* §6.7 (Lanczos / MINRES).

## Open questions / caveats

1. **Role-choice rationale**. Cycle-003 integrator-signals listed MINRES as a candidate for **harvester** dispatch (firm L1 operator extraction). The cycle-004 planner dispatched **abstractor** instead. The harvester role would have required a Palace L0 site to extract from; on inspection no such site exists. Abstractor was the right call because the appropriate output for "L_n+1 form, but L_n is empty" is an obstruction-flavoured lowering theme, not a firm L1 operator with nothing to ground it. Worth recording for cycle-planner heuristics: **before queuing a harvester pass for an algorithm, grep for its presence**; queue abstractor with obstruction-anticipation when grep returns ≤ 3 hits all in enum/labels/config.

2. **Shared-Infrastructure priority re-scoping**. The cycle-003 priorities list put MINRES at #10 of shared-infra items. The implicit assumption was that Palace implements MINRES; with that assumption disconfirmed, item #10 needs re-scoping. Two candidate re-framings:
   - (a) Drop MINRES from shared-infra entirely — it's not Palace infrastructure.
   - (b) Reinterpret as "the symmetric-indefinite Krylov layer Palace *would* need" — a forward-looking gap, useful when downstream burn-port work needs symmetric-indefinite solves (the eigenmode driver may; uncertain).
   This is a methodology question for the meta-phase, not for the abstractor; surfacing here for the integrator to forward.

3. **Is MFEM in L0 scope?** CLAUDE.md's "Scope" section says mesh / FE-space construction (MFEM-equivalent FE assembly) is in scope. It is *ambiguous* whether this extends to MFEM's Krylov solvers (`mfem::MINRESSolver`, `mfem::SLBQPOptimizer`, etc.) as L0 substrate. If yes, the obstruction in this theme is recoverable — the L1>L0 rewrite would target MFEM source rather than Palace source. If no, the obstruction stands. This question should be answered before any harvester promotion of the three rough-in operators. Filing as open question for the integrator to route to `scaffolding/open-questions.md`.

4. **BICGSTAB and DEFAULT share the MFEM_ABORT fate**. `ksp.cpp:53-55` aborts on all three of `MINRES`, `BICGSTAB`, `DEFAULT`. BICGSTAB is the more interesting twin (non-symmetric, would need separate L1 form); DEFAULT is presumably handled by an earlier resolution step that wasn't read here. A follow-up cycle should sketch BICGSTAB as a sibling obstruction-theme if BICGSTAB is also of practical interest; otherwise drop both from shared-infra alongside MINRES per (2).

5. **Lanczos as variant of Arnoldi**. The proposed `lanczos_step` is a clean variant-axis of the planned `arnoldi_step` (symmetry collapses `j`-term recurrence to 2-term). If `arnoldi_step` is harvested first against an affirmative L0 site (GMRES Arnoldi inner body, `iterative.cpp:614-642`), `lanczos_step` may collapse from a separate rough-in into a `variant_of(arnoldi_step, symmetry=true)` row. Worth a same-layer-cross-cutter pass once both are on the dep-map.

6. **Caveat on signature sketches**. The three speculative operator signatures above are written tensor-typed and stateless; in practice MINRES requires the running QR state to thread through `givens_apply_with_residual_min`, which couples it to `qr_state` lifetime. Harvester should expect to rework the signature shape; the signatures here are scaffolding, not contracts.
