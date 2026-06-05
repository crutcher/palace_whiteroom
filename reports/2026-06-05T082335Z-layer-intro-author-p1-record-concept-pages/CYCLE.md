---
agent: layer-intro-author
invoked_at: 2026-06-05T08:23:35Z
scope: graded-stack typed-edge campaign P1 — type the 6 untyped RECORD concept pages
status: pending
integrated_at: 2026-06-05T093000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-104 D1, applied clean (staging row 1/4). 6 record-concept pages (krylov/op-params/sim-state/step-outputs/prev-carry/solve-result) typed rank:firm kind:record with cites-evidence depends-on to L0 iterative.{hpp,cpp}. Closes c103 carry-forward OQ graded-stack-six-record-concept-pages-need-frontmatter. rank_violations held 0; build EXIT 0."
---

# CYCLE: type the 6 RECORD concept pages (`krylov`, `op-params`, `sim-state`, `step-outputs`, `prev-carry`, `solve-result`)

## Summary

Cycle-104 D1, graded-stack typed-edge campaign P1 next tranche. The 6 named L4 record-definition
concept pages under `book/src/concepts/` carry **no `edges:`/`rank:` frontmatter** today (unlike the
c103 exemplars `concepts/dofset.md` + `concepts/config-record.md`, which were already typed). These
ARE DAG nodes (`record` Kind, per the scheme §5 record-definition sub-case), so each gets a typed
`edges:` frontmatter block prepended:

- `rank: firm` + `kind: record` for all 6 (judged per-page from each file's on-disk `## Status`
  line, which reads `firm` in every case — verified below).
- `depends-on` (each `kind: cites-evidence`) → the verified L0 backing struct / source ranges in
  `palace/linalg/iterative.hpp` / `iterative.cpp` (the iterative-solver class hierarchy these records
  un-mix). These are rank-terminal ground truth.
- `reference` → the producer/consumer operator + the sibling record / `state-stratification` /
  `solve-monad` pages each names (navigational; a record does NOT block on its consumers).

Well-foundedness holds vacuously for all 6: every blocking (`depends-on`) edge targets a rank-terminal
L0 source range; the consumer/sibling edges are `reference` (free). No record blocks on another record
or on its consumers.

**No page is speculative / lower-rank.** All 6 on-disk `## Status` lines read `firm` — including the
two *constructive* records (`prev-carry`, `step-outputs`) and the constructive return-record
(`solve-result`), whose status prose explicitly affirms `firm` ("the record *shape* is firm"; "the
negative L0 anchoring … all stated and cited"). Their fields are individually backed by positive L0
source sites even though no single named C++ struct exists — so the `cites-evidence depends-on` edges
point at the per-field backing sites (still rank-terminal L0). **No dangling edges** — all 15 reference
targets confirmed on-disk.

## Edge-classification rationale (applies to all 6)

- **`depends-on` (blocking, `kind: cites-evidence`):** ONLY the L0 source ranges. A record-definition
  page's data shape *rests on* its backing struct/source (the dofset/config-record precedent: the L0
  backing is the record's sole blocking dependency). L0 ranges are rank-terminal, so `rank: firm` rests
  only on `firm`-equivalent ground truth — the §1b invariant holds.
- **`reference` (free):** the producer/consumer operator chapters (`L4/krylov-step`, `solve-monad`,
  `convergence-test`, …), the sibling record pages (`op-params`/`krylov`/`sim-state`/`step-outputs`/
  `prev-carry`/`solve-result`), and the conceptual-typing pages (`state-stratification`,
  `variant-absorption`, `first-iteration-unrolling`, `derived-view-hoisting`,
  `constructed-operators`/`constructed-operator-factory`). A record is *named-by-use*; it does not
  block on its consumers, and it does not block on its sibling record shapes (it narrates its place in
  the three-stratum typing, it is not structurally founded on the siblings).

## L0-anchor self-verification (codemap `read_range`, on-disk this dispatch)

All citations re-confirmed against `palace/linalg/iterative.{hpp,cpp}`:

- `iterative.hpp:26` — `class IterativeSolver` opens; `:41` `double rel_tol, abs_tol;`; `:44`
  `int max_it;`; `:48-49` `const OperType *A; const Solver<OperType> *B;`; `:52-54`
  `mutable bool converged; mutable double initial_res, final_res; mutable int final_it;`; `:97-108`
  the `GetConverged/GetInitialRes/GetFinalRes/GetNumIterations` accessor surface.
- `iterative.hpp:144` `mutable VecType r, z, p;` (CgSolver workspace); `:155` `class GmresSolver`
  opens; `:180` `mutable int max_dim;`; `:184` `Orthogonalization gs_orthog;`; `:187`
  `PreconditionerSide pc_side;`; `:190-194` the GMRES `V/r/H/s,sn/cs` workspace block;
  `:197-198` `Initialize()/Update(int j)`; `:222` `class FgmresSolver` opens; `:256`
  `mutable std::vector<VecType> Z;`.
- `iterative.cpp:21-31` `CheckDot` partial-function guard; `:395` `beta = linalg::Dot(comm, z, r);`,
  `:396` `CheckDot(beta, …)`, `:397` `res = std::sqrt(std::abs(beta));`; `:642`
  `beta = std::abs(s[j + 1]);`, `:643` `CheckDot(beta, …)`, `:644` `converged = (beta < eps);`.

(Note: the prose in op-params/sim-state cites a few hpp line numbers ±1 from the exact declaration
line — e.g. prose `:42`/`:45` vs. exact `:41`/`:44` for `rel_tol,abs_tol`/`max_it`; prose `:49-50` vs.
exact `:48-49` for `A`/`B`. These are pre-existing prose citations, OUT OF THIS DISPATCH'S SCOPE to
re-edit. The `cites-evidence` frontmatter edges I emit point at the *verified* backing region
`iterative.hpp:26-115` for the base-class fields, so the typed edge is anchored on confirmed ground
truth regardless of the ±1 prose drift. I flag the prose ±1 drift as an OQ for a future citation-audit
pass — it does not affect the rank/edge typing.)

## Proposed changes

Each block prepends a YAML frontmatter `edges:` + `rank:` + `kind:` header to the existing file (the
files currently begin directly with the `# <Name>` H1 — these are pure prepends, valid YAML, no body
change).

```edit:book/src/concepts/krylov.md
[old]:
# Krylov

> **Kind: `record`.** This page defines the *data shape* of the L4 `Krylov` record — its (slice-specific) field schemas, their types and meaning, the construction-vs-run-time stratum of each, and the L0 source home it mirrors.
[new]:
---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/linalg/iterative.hpp:119-150
      kind: cites-evidence            # CgSolver class + `mutable VecType r, z, p;` workspace (:144)
    - target: palace/linalg/iterative.hpp:155-217
      kind: cites-evidence            # GmresSolver class + V/r/H/s,sn/cs workspace (:190-194) + Initialize/Update (:197-198)
    - target: palace/linalg/iterative.hpp:222-275
      kind: cites-evidence            # FgmresSolver class + `mutable std::vector<VecType> Z;` (:256)
  reference:
    - L4/krylov-step
    - concepts/solve-monad
    - concepts/convergence-test
    - concepts/state-stratification
    - concepts/op-params
    - concepts/sim-state
    - concepts/first-iteration-unrolling
    - concepts/prev-carry
---

# Krylov

> **Kind: `record`.** This page defines the *data shape* of the L4 `Krylov` record — its (slice-specific) field schemas, their types and meaning, the construction-vs-run-time stratum of each, and the L0 source home it mirrors.
```

```edit:book/src/concepts/op-params.md
[old]:
# OpParams

> **Kind: `record`.** This page defines the *data shape* of the L4 `OpParams` record — its fields, their types and meaning, the construction-vs-run-time stratum of each, and the L0 source home it mirrors.
[new]:
---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/linalg/iterative.hpp:26-115
      kind: cites-evidence            # IterativeSolver base: rel_tol/abs_tol (:41), max_it (:44), A/B (:48-49)
    - target: palace/linalg/iterative.hpp:155-217
      kind: cites-evidence            # GmresSolver variant selectors: max_dim (:180), gs_orthog (:184), pc_side (:187)
  reference:
    - L4/krylov-step
    - concepts/solve-monad
    - concepts/state-stratification
    - concepts/sim-state
    - concepts/krylov
    - concepts/variant-absorption
    - concepts/constructed-operators
    - concepts/constructed-operator-factory
    - concepts/convergence-test
---

# OpParams

> **Kind: `record`.** This page defines the *data shape* of the L4 `OpParams` record — its fields, their types and meaning, the construction-vs-run-time stratum of each, and the L0 source home it mirrors.
```

```edit:book/src/concepts/sim-state.md
[old]:
# SimState

> **Kind: `record`.** This page defines the *data shape* of the L4 `SimState` record — its fields, their types and meaning, the construction-vs-run-time stratum of each, and the L0 source home it mirrors.
[new]:
---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/linalg/iterative.hpp:26-115
      kind: cites-evidence            # IterativeSolver base: mutable converged/initial_res,final_res/final_it (:52-54); accessor surface (:97-108)
    - target: palace/linalg/iterative.hpp:140-150
      kind: cites-evidence            # CgSolver::Mult iterate output arg `x` (:149)
    - target: palace/linalg/iterative.hpp:214-217
      kind: cites-evidence            # GmresSolver::Mult iterate output arg `x` (:216)
  reference:
    - L4/krylov-step
    - concepts/solve-monad
    - concepts/state-stratification
    - concepts/convergence-test
    - concepts/op-params
    - concepts/krylov
---

# SimState

> **Kind: `record`.** This page defines the *data shape* of the L4 `SimState` record — its fields, their types and meaning, the construction-vs-run-time stratum of each, and the L0 source home it mirrors.
```

```edit:book/src/concepts/step-outputs.md
[old]:
# step-outputs

`StepOutputs` is the **demand-prunable per-step readout bundle** returned by the L4 [`krylov-step`](../L4/krylov-step.md) kernel alongside the next `SimState` and `Krylov` values.
[new]:
---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/linalg/iterative.cpp:393-397
      kind: cites-evidence            # PCG residual proxy: beta = (Br,r) (:395), CheckDot (:396), res = sqrt|beta| (:397)
    - target: palace/linalg/iterative.cpp:640-644
      kind: cites-evidence            # GMRES LS-residual estimate: beta = |s[j+1]| (:642), CheckDot (:643), converged test (:644)
    - target: palace/linalg/iterative.cpp:21-31
      kind: cites-evidence            # CheckDot guard backing the breakdown_token slot
    - target: palace/linalg/iterative.hpp:26-115
      kind: cites-evidence            # persistent home of the readouts: mutable final_res statistic (:54)
  reference:
    - L4/krylov-step
    - concepts/derived-view-hoisting
    - concepts/solve-monad
    - concepts/state-stratification
    - concepts/solve-result
    - concepts/sim-state
    - concepts/krylov
---

# step-outputs

`StepOutputs` is the **demand-prunable per-step readout bundle** returned by the L4 [`krylov-step`](../L4/krylov-step.md) kernel alongside the next `SimState` and `Krylov` values.
```

```edit:book/src/concepts/prev-carry.md
[old]:
# prev-carry

`PrevCarry` is the **closure-threaded recurrence carry** that the [`first-iteration-unrolling`](./first-iteration-unrolling.md) rotation moves *out of* the steady-state iteration schema and threads through the loop driver as a closure argument.
[new]:
---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/linalg/iterative.cpp:393-397
      kind: cites-evidence            # CG beta_prev backing: beta = (Br,r) recurrence value (:395-396)
    - target: palace/linalg/iterative.cpp:636-644
      kind: cites-evidence            # GMRES H_prev backing: sub-diagonal Hessenberg entry in the Arnoldi/plane-rotation sequence
  reference:
    - concepts/first-iteration-unrolling
    - L4/krylov-step
    - concepts/state-stratification
    - concepts/solve-result
    - concepts/krylov
    - concepts/step-outputs
---

# prev-carry

`PrevCarry` is the **closure-threaded recurrence carry** that the [`first-iteration-unrolling`](./first-iteration-unrolling.md) rotation moves *out of* the steady-state iteration schema and threads through the loop driver as a closure argument.
```

```edit:book/src/concepts/solve-result.md
[old]:
# solve-result

`Solve { sim, krylov, outputs[, carry] }` is the **return-record shape** of the L4 [`krylov-step`](../L4/krylov-step.md) kernel — the record of values one step hands back.
[new]:
---
rank: firm
kind: record
edges:
  depends-on:
    - target: palace/linalg/iterative.hpp:26-115
      kind: cites-evidence            # `sim` backing: mutable solve-statistics fields (:52-54) mutated in place on the solver instance
    - target: palace/linalg/iterative.cpp:393-397
      kind: cites-evidence            # `outputs` backing: per-step derived readouts computed inline (residual proxy)
    - target: palace/linalg/iterative.cpp:640-644
      kind: cites-evidence            # `outputs` backing: GMRES LS-residual readout
    - target: palace/linalg/iterative.cpp:21-31
      kind: cites-evidence            # `outputs` backing: CheckDot guard
  reference:
    - concepts/solve-monad
    - L4/krylov-step
    - concepts/step-outputs
    - concepts/prev-carry
    - concepts/state-stratification
    - concepts/sim-state
    - concepts/krylov
---

# solve-result

`Solve { sim, krylov, outputs[, carry] }` is the **return-record shape** of the L4 [`krylov-step`](../L4/krylov-step.md) kernel — the record of values one step hands back.
```

## Supporting evidence

- The c103 record-page exemplars (`book/src/concepts/dofset.md`, `book/src/concepts/config-record.md`)
  establish the convention this dispatch follows exactly: `rank: firm` + `kind: record`; `depends-on`
  with `kind: cites-evidence` → the L0 backing ranges; `reference` → the producer/consumer entries; a
  record blocks ONLY on its L0 backing, never on its consumers.
- Scheme §5 ("Concept pages") record-definition sub-case: a record-definition page "**is** a DAG node
  and its rank is the resolution of that shape (typically `firm` once its L0 backing struct is cited)."
- Each page's on-disk `## Status` line reads `firm`:
  - `krylov.md:85` — `firm` (both CG + GMRES/FGMRES schemas settled, backed by `CgSolver`/`GmresSolver`/`FgmresSolver` `mutable`-workspace fields).
  - `op-params.md:76` — `firm` (construction-time stratum, every field backed by `IterativeSolver`/`GmresSolver` instance-field declarations).
  - `sim-state.md:59` — `firm` (five-field schema backed by `IterativeSolver` `mutable` statistics + the `Mult` iterate arg).
  - `step-outputs.md:54` — `firm` ("the record *shape* is firm"; `BreakdownTag` enum left open is the only constructed sub-part — does not lower the shape's rank).
  - `prev-carry.md:51` — `firm` (field/type/carry-stratum/negative-L0-anchoring all cited; the `carry` slot of the firm `krylov-step` Form B signature).
  - `solve-result.md:59` — `firm` (four fields + run-time discharge stratum + L0 mutated-state backing all cited).
- L0 anchors re-verified via codemap `read_range` this dispatch (see §L0-anchor self-verification).
- All 15 reference/sibling targets confirmed present on-disk (`L4/krylov-step` + 8 concept pages + 6
  sibling record pages) — no dangling edges.

## Open questions / caveats

- **`record-concept-prose-citation-pm1-drift` (low-severity, out-of-scope for this typing pass).**
  `op-params.md` / `sim-state.md` prose cites a handful of `iterative.hpp` line numbers ±1 from the
  exact declaration line (prose `:42`/`:45`/`:49-50`/`:53-55` vs. on-disk exact `:41`/`:44`/`:48-49`/
  `:52-54`). The typed `cites-evidence` frontmatter edges I emit anchor on the verified enclosing
  region (`iterative.hpp:26-115`), so the edges are sound; but a future citation-audit pass should
  re-anchor the prose ±1 drifts. Flagging rather than editing — prose-citation correction is outside
  this dispatch's edge-typing scope and would be an unrequested body edit.
- **Node-status convention divergence (already known; meta-phase owns).** The dispatch prompt notes the
  c103 batch surfaced a node-status convention divergence the meta-phase will unify — and explicitly
  states there is NO divergence for RECORD pages (they are unambiguously DAG `record` nodes). I followed
  the dofset/config-record pattern exactly; nothing here interacts with that open convention question.
- **`depends-on` granularity for the three constructive records** (`step-outputs`, `prev-carry`,
  `solve-result`): these have no single named C++ struct, so I pointed `cites-evidence` at the per-field
  backing *source ranges* (loop-body computations + in-place-mutated instance fields) rather than a
  struct declaration. This matches the pages' own "L0 source home" narration (they reify inline loop
  readouts / mutated statistics). The rank is unaffected — every such range is rank-terminal L0 ground
  truth — but if a future linter wants struct-granularity backing for record nodes, these three are the
  legitimate exceptions (constructive L4 reifications, by design with no 1:1 L0 struct).
