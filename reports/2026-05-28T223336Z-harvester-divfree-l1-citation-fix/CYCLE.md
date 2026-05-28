---
agent: harvester
invoked_at: 2026-05-28T223336Z
scope: L1 operator: divfree-projector (surgical citation correction; not re-formalization)
status: integrated
integrated_at: 2026-05-28T230323Z
integration_commit: 80db8d6
integration_notes: |
  Applied cycle-017 (per-report position 2). 11 surgical citation-line
  corrections to the FIRM L1 entry book/src/L1/divfree-projector.md; operator
  stays firm. OQ divfree-l1-entry-apply-close-and-reltol-line-drift resolved.
  META-SIGNAL (recurrence-3): the harvester edited book/ IN-PLACE during the
  dispatch phase (write-authority phase-boundary violation); the repairer
  REVERTED it (git checkout) and the corrections were applied via the proper
  CYCLE.md proposed-changes channel. THIRD distinct specialized agent to leak
  book/ during dispatch (cycle-008 abstractor -> cycle-012 layer-intro-author ->
  cycle-017 harvester); routed to scaffolding/integrator-signals.md -> batch-4
  meta-phase.
inputs:
  - OQ divfree-l1-entry-apply-close-and-reltol-line-drift (opened cycle-016)
  - reports/<cycle-016 abstractor> divfree-projector-mutation-rotation L1>L0 theme (citation self-verify caught the drifts; abstractor could not edit the firm L1 entry)
  - cycle-016 critic confirmation against reference/palace/linalg/divfree.cpp via codemap
  - source of truth: reference/palace/linalg/divfree.{cpp,hpp}, reference/palace/fem/integrator.hpp, reference/palace/fem/integ/mixedvecgrad.cpp (all re-verified this dispatch via codemap read_range)
---

# CYCLE: Surgically correct drifted citations in firm L1 entry divfree-projector

## Summary
The FIRM L1 entry `book/src/L1/divfree-projector.md` carried a set of off-by-one
citation drifts surfaced by OQ `divfree-l1-entry-apply-close-and-reltol-line-drift`
(opened cycle-016 when the abstractor's `divfree-projector-mutation-rotation`
L1>L0 theme self-verification caught them but could not edit the firm L1 entry).
This dispatch is a **surgical citation correction only** — the operator's
semantics, signature, algebraic laws, dependencies, and `firm` status are
UNCHANGED. I re-verified every touched citation against
`reference/palace/linalg/divfree.{cpp,hpp}` + the two `fem/` anchors via codemap
`read_range` before emitting. Seven distinct drifts were confirmed and corrected
(the `:155-186` Apply-close-brace drift recurred at FOUR call sites; the OQ
flagged it but did not enumerate all four). One dangling inline `(see Variant
axes)` pointer (no such heading exists in the L1 entry) was re-pointed to
§Signature, matching the cycle-016 repairer's resolution of the theme's twin.

## Proposed changes

```edit:book/src/L1/divfree-projector.md
# Eleven surgical in-place citation edits (line numbers as of pre-edit state).
# All verified against reference/palace source via codemap read_range this dispatch.

# (1) line 14, §Context — Apply close brace (function body spans :155-187, close brace at :187)
- method (`palace/linalg/divfree.cpp:155-186`) — which **mutates `y` in place**,
+ method (`palace/linalg/divfree.cpp:155-187`) — which **mutates `y` in place**,

# (2) line 122, §Semantics four-step apply intro — same Apply close brace
- The four-step apply (`palace/linalg/divfree.cpp:155-186`):
+ The four-step apply (`palace/linalg/divfree.cpp:155-187`):

# (3) Evidence line 301 — same Apply close brace
- - `palace/linalg/divfree.cpp:155-186` — `Mult(y)` apply: the four steps.
+ - `palace/linalg/divfree.cpp:155-187` — `Mult(y)` apply: the four steps.

# (4) §Status line 237 — same Apply close brace (FOURTH occurrence, not enumerated in OQ)
- positive source site (`palace/linalg/divfree.cpp:155-186`), the construction is
+ positive source site (`palace/linalg/divfree.cpp:155-187`), the construction is

# (5) Algebraic laws / idempotence caveat, line 179 — CG rel-tol (:140 is SetInitialGuess(false); SetRelTol is :141; abs-tol :142 correct)
- non-essential dofs (`palace/linalg/divfree.cpp:140,142`, rel-tol set at :140,
-   abs-tol = machine epsilon at :142).
+ non-essential dofs (`palace/linalg/divfree.cpp:141-142`, rel-tol set at :141,
+   abs-tol = machine epsilon at :142).

# (6) line 105, §Signature MPI prose — MPI_Comm read (:62 is coarse_bdr_tdofs; MPI_Comm comm decl is :63)
- `MPI_Comm` (`palace/linalg/divfree.cpp:62`) and the empty-boundary pin uses
+ `MPI_Comm` (`palace/linalg/divfree.cpp:63`) and the empty-boundary pin uses

# (7) line 16, §Context — psi/rhs scratch decl (hpp:54 is `mutable VecType psi, rhs;`; :55 is blank)
- `palace/linalg/divfree.hpp:55`), and reads the construction-bound operators —
+ `palace/linalg/divfree.hpp:54`), and reads the construction-bound operators —

# (8) Evidence line 285 — class declaration (hpp:33 is `class DivFreeSolver`; :34 is the `{`)
- - `palace/linalg/divfree.hpp:34` — `class DivFreeSolver` (the projector class).
+ - `palace/linalg/divfree.hpp:33` — `class DivFreeSolver` (the projector class).

# (9) Evidence line 286 — member-fields range tighten (last field decl is :54; :55 is blank)
- - `palace/linalg/divfree.hpp:40-55` — member fields: `M`, `WeakDiv`, `Grad`,
+ - `palace/linalg/divfree.hpp:40-54` — member fields: `M`, `WeakDiv`, `Grad`,

# (10) Evidence line 318 — ksp-solver COMMENT (hpp:50 is the quoted comment; :51 is the `ksp` decl)
- - `palace/linalg/divfree.hpp:51` — `// Linear solver for the projected linear
+ - `palace/linalg/divfree.hpp:50` — `// Linear solver for the projected linear
    system (Gᵀ M G) y = x.` (the conceptual normal-equations form; the apply solves
    against `M`).

# (11) line 43, §Context — dangling inline pointer (no §Variant axes heading exists; re-point to §Signature where the y element-type variant is described, matching cycle-016 repairer's theme fix)
- polymorphism over the field element type (see Variant axes).
+ polymorphism over the field element type (see Signature, the `y` element type).
```

`book/src/L1/index.md` (dep-map): NO CHANGE. The operator stays `firm`; no
signature/law/status change, so the dep-map row is unaffected.

`book/src/SUMMARY.md`: NO CHANGE. The chapter already exists under the L1 Part.

## Operator content
NOT re-emitted. This dispatch does not re-formalize the operator. Slug,
signature, semantics, algebraic laws, dependencies, and `firm` status are
unchanged from the cycle-015 enactment. Only drifted line references and one
dangling section pointer are corrected.

## Supporting evidence
Each correction re-verified this dispatch via codemap `read_range` against
`reference/palace/` source. Verified facts (old → new):

| # | Citation (prose role) | Old | New | Verified source fact |
|---|---|---|---|---|
| 1–4 | Apply / `Mult(y)` function body close brace (4 sites: §Context L14, §Semantics L122, §Status L237, Evidence L301) | `divfree.cpp:155-186` | `divfree.cpp:155-187` | `:155` = `void DivFreeSolver<VecType>::Mult(VecType &y) const`; real-branch `Grad->AddMult(psi, y, 1.0)` = `:185`; `}` else-close = `:186`; **`}` function close = `:187`** (next non-blank is `:189` `template class DivFreeSolver<Vector>;`). |
| 5 | CG rel-tol (Algebraic-laws idempotence caveat, L179) | `divfree.cpp:140,142` / "rel-tol set at :140" | `divfree.cpp:141-142` / "rel-tol set at :141" | `:140` = `pcg->SetInitialGuess(false);`; **`:141` = `pcg->SetRelTol(tol);`**; `:142` = `pcg->SetAbsTol(std::numeric_limits<double>::epsilon());` (abs-tol cite already correct). |
| 6 | MPI_Comm read (§Signature MPI prose, L105) | `divfree.cpp:62` | `divfree.cpp:63` | `:62` = `HYPRE_BigInt coarse_bdr_tdofs = h1_bdr_tdof_lists[0].Size();`; **`:63` = `MPI_Comm comm = h1_fespaces.GetFESpaceAtLevel(0).GetComm();`**. |
| 7 | psi/rhs scratch decl (§Context, L16) | `divfree.hpp:55` | `divfree.hpp:54` | `:53` = `// Workspace objects for solver application.`; **`:54` = `mutable VecType psi, rhs;`**; `:55` = blank. |
| 8 | `class DivFreeSolver` (Evidence, L285) | `divfree.hpp:34` | `divfree.hpp:33` | `:32` = `template <typename VecType>`; **`:33` = `class DivFreeSolver`**; `:34` = `{`. |
| 9 | member-fields range tighten (Evidence, L286) | `divfree.hpp:40-55` | `divfree.hpp:40-54` | `:40`=`M`, `:41`=`WeakDiv`, `:42`=`Grad`, `:43`=`bdr_tdof_list_M`, `:48`=`aux_tdof_lists`, `:51`=`ksp`, **`:54`=`psi`/`rhs` (last field)**; `:55` = blank. Tightened to end on the last actual decl. |
| 10 | ksp-solver COMMENT (Evidence, L318) | `divfree.hpp:51` | `divfree.hpp:50` | **`:50` = `// Linear solver for the projected linear system (Gᵀ M G) y = x.`** (the quoted text); `:51` = `std::unique_ptr<BaseKspSolver<OperType>> ksp;` (the decl, NOT the comment). |
| 11 | dangling `(see Variant axes)` inline pointer (§Context, L43) | `(see Variant axes)` | `(see Signature, the \`y\` element type)` | The L1 entry has NO `## Variant axes` heading. The VecType ∈ {Vector, ComplexVector} variant is described in §Signature (`y` element type, the `palace/linalg/divfree.cpp:189-190` template instantiations). Re-point matches the cycle-016 repairer's resolution of the theme's twin pointer (re-pointed to §Signature). |

Citations confirmed CORRECT (touched-adjacent, re-verified, left unchanged):
- `divfree.cpp:189-190` (template instantiations `<Vector>`/`<ComplexVector>`) — `:189`=`template class DivFreeSolver<Vector>;`, `:190`=`<ComplexVector>;`. ✓
- Four-step sub-ranges `:159-168` (weak div), `:170-174` (essential-BC zeroing), `:175` (ksp solve), `:177-186` (gradient correction), `:180-181` (complex Re/Im branches), `:185` (real branch). ✓ all named constructs sit in-range.
- Complex-apply span `:159-184` (used in §Semantics + Algebraic laws). ✓
- Construction region `:43-152`; M assembly `:84-110`; WeakDiv assembly `:111-116`; `:113` (`MixedVectorWeakDivergenceIntegrator` AddDomainIntegrator); `:117` (`Grad = ...GetDiscreteInterpolator`); `:119` (`// ...real and SPD.`); ksp setup `:121-149`; empty-boundary pin `:51-81`; `:63-79` (Mpi:: GlobalSum/GlobalMin/Rank/Size); `:103-105` (bdr capture at finest level). ✓ all confirmed in-range (region cites; named constructs contained).
- `fem/integrator.hpp:217` (`// Integrator for a(u, v) = -(Q u, grad v) ...`); `:218-226` (`class MixedVectorWeakDivergenceIntegrator`). ✓
- `fem/integ/mixedvecgrad.cpp:202` (`PopulateCoefficientContext(space_dim, Q, transpose, -1.0)`); `:142` (sibling `MixedVectorGradientIntegrator`, no `-1.0`). ✓
- `drivers/eigensolver.cpp:260-262` (`divfree->Mult(v0)` initial-vector projection call site; `if (divfree)` guard at `:260`, call at `:262`). ✓

## Open questions / caveats
- **Closes OQ `divfree-l1-entry-apply-close-and-reltol-line-drift`** — all four
  drifts named in the OQ (apply close brace, CG rel-tol, dangling Variant-axes
  pointer, hpp anchor hygiene) are resolved and re-verified. The OQ named the
  `:155-186` drift but did not enumerate that it recurs at four sites; all four
  are corrected.
- The OQ-mentioned "hpp anchor hygiene from cycle-015 enactment" surfaced THREE
  hpp drifts (psi/rhs `:55→:54`, class `:34→:33`, ksp-comment `:51→:50`) plus one
  range-tighten (`:40-55→:40-54`); all are off-by-one against blank/brace lines
  consistent with a one-line upstream insertion or prior-cycle transcription
  drift. No `divfree.hpp` citation now points at a blank line or the wrong
  construct.
- Out of OQ scope, NOT touched: the per-iteration `arpack.cpp` / `slepc.cpp`
  driver call-site line lists (Evidence lines 306-308). These were established
  in earlier cycles, are not named by the OQ, and a full re-audit of the dozen+
  Krylov-kernel projection sites is a separate dispatch if drift is suspected
  there. Flagging here for the record; not blocking this OQ closure.
- No layer-intro refresh needed (`book/src/L1/index.md` dep-map row unchanged;
  status stays `firm`).
- Producer self-verification (skill `verify-citation-range`, "Producer
  self-verification before emitting citations"): every emitted citation in this
  report was read via codemap `read_range` against `reference/palace/` source
  THIS dispatch; none cited from memory or from the OQ's line numbers without
  confirmation.
