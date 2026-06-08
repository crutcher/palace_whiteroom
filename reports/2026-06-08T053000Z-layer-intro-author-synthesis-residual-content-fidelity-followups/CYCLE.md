---
agent: layer-intro-author
invoked_at: 2026-06-08T053000Z
scope: synthesis-residual-content-fidelity-followups (3 LOW Synthesis correspondence-audit follow-ups)
status: integrated
integrated_at: 2026-06-08T165758Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-139 (batch-45 OPENER, 1/3). 3 content-fidelity fixes across 5 files — L4/iterate-while-with-prev.md (stale cg_solve call) + L4/eigsolve.md (7x initial_state->initial_eig_state) + L4/index.md (2 eigsolve-cap occurrences) + synthesis/coordination.md (stale NOTE re-phrased) + synthesis/types.md (units:Units added); 3 parent c138 OQs DISCHARGED. Meta-phase CLOSE-RESOLVES the 3 parent sections + retires their Backlog-Low migration lines at the batch-45 unify."
---

# CYCLE: synthesis residual content-fidelity follow-ups (3 fixes)

## Summary

Three migrated LOW content-fidelity nuances from the batch-44 Synthesis
correspondence audit. All benign — the rendered Synthesis correspondence is
faithful; these are upstream-chapter polish (content-staleness / completeness).
All three live in disjoint files; the edits are minimal and surgical, all
landing inside existing fences where applicable (no KaTeX `$`-sigil-fence
breakage introduced).

- **(a)** `book/src/L4/iterate-while-with-prev.md` §Evidence (line 233) — the
  "prototypical use" prose shows a stale `iterate_while_with_prev` call shape
  that no longer matches the canonical CG Form B call in `krylov-step.md`.
  Refresh to the canonical bootstrap / init-carry / steady / cont arg order
  (the secondary occurrence of the c138-finalize `krylov-step.md:192-197` fix).
  OQ `iterate-while-with-prev-evidence-prose-stale-cg-call-shape`.
- **(b)** `book/src/L4/eigsolve.md` — `initial_state` → `initial_eig_state`
  (the EigState-coherent ctor matching the cap's `StateT EigState` threading;
  the Synthesis render is already the more-correct form). **7 occurrences**
  (not 2): lines 44, 69, 70, 97, 109, 180, 189 — ALL name the same
  `EigState`-seeding constructor, so all flip for consistency. No L3-kernel or
  L4-sibling cross-file occurrence exists (this is the L4-cap file; the L3
  kernel is a separate doc and not in scope). OQ
  `l4-eigsolve-initial-state-vs-initial-eig-state-seed-inconsistency`.
- **(c)** `book/src/synthesis/types.md` `IoData` block (lines 38-44) — the
  rendered record omits the `units : Units` field that the authoritative
  `IoData` schema carries. Add the `units : Units` line + widen the cited-range
  comment `config-record.md:69-73` → `:69-74` (line 74 is the `units : Units`
  schema line). OQ `synthesis-types-iodata-omits-units-field`.

## Proposed changes

### Fix (a) — refresh stale `iterate_while_with_prev` prototypical-use prose

The current §Evidence bullet (line 233) shows a `iterate_while_with_prev s1
s0.beta (\(s, _) -> ...) (\(s, beta_prev) -> ...)` call shape: a 4-arg form
with `s1` then `s0.beta` as the first two positional args and the predicate
*before* the steady step. The canonical CG Form B call in `krylov-step.md`
(lines 192-199, the c138-current shape) is the **bootstrap-closure / init-carry
/ steady-step / cont-predicate** order:

```text
iterate_while_with_prev
  (\_ -> pure { state: s1, prev: s0.beta })   -- bootstrap
  s1                                          -- initial carry
  (\(s, beta_prev) -> ...)                    -- steady_step: (carry, prev)
  (\s -> s.it < config.max_it && not s.converged)  -- cont: pure on carry, fires LAST
```

The stale prose conflates the (now-split) bootstrap closure with the
`s0.beta` seed and places the predicate second; refresh it to name the
canonical four-argument order and point at the live `krylov-step.md` lines.

```edit:book/src/L4/iterate-while-with-prev.md
[old]: - `book/src/L4/krylov-step.md` Form B — the canonical v0.5 CG form using this combinator (firm-homed there cycle-099). The `cg_first_step` / `cg_steady_step` split is the prototypical Form B pair; the call `iterate_while_with_prev s1 s0.beta (\(s, _) -> ...) (\(s, beta_prev) -> ...)` is the prototypical use. **Note on closure-argument convention**: the L4 row's `steady_step` signature `((α, β) -> ...)` adopts the *carry-first, prev-second* convention. This matches the [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) pseudo-code at `first-iteration-unrolling.md:34-37` (`\(s, carry) -> (steady_step ... carry s, extract_carry s)` — `s` precedes `carry`) AND the CG v0.5 call site (`\(s, beta_prev) -> ...` — `s` precedes `beta_prev`). The L4 row's convention is therefore consistent with both renderings.
[new]: - `book/src/L4/krylov-step.md` Form B (`krylov-step.md:192-199`) — the canonical v0.5 CG form using this combinator (firm-homed there cycle-099). The `cg_first_step` / `cg_steady_step` split is the prototypical Form B pair; the prototypical call is the four-argument **bootstrap-closure / init-carry / steady-step / cont-predicate** form: `iterate_while_with_prev (\_ -> pure { state: s1, prev: s0.beta }) s1 (\(s, beta_prev) -> ...) (\s -> s.it < config.max_it && not s.converged)` — the first argument is the *bootstrap closure* producing the initial `prev` (here seeding `prev = s0.beta`), the second is the *initial carry* `s1`, the third is the *steady step* consuming `(carry, prev)`, and the predicate is the *last* argument (pure on the carry, fired after the steady step). **Note on closure-argument convention**: the L4 row's `steady_step` signature `((α, β) -> ...)` adopts the *carry-first, prev-second* convention. This matches the [`first-iteration-unrolling`](../concepts/first-iteration-unrolling.md) pseudo-code at `first-iteration-unrolling.md:34-37` (`\(s, carry) -> (steady_step ... carry s, extract_carry s)` — `s` precedes `carry`) AND the CG v0.5 call site (`\(s, beta_prev) -> ...` — `s` precedes `beta_prev`). The L4 row's convention is therefore consistent with both renderings.
```

### Fix (b) — `initial_state` → `initial_eig_state` (7 occurrences, all the EigState ctor)

All seven occurrences name the same `EigState`-seeding constructor; the
Synthesis render already uses the EigState-coherent `initial_eig_state` form
matching the cap's `Solve = StateT EigState Identity` threading. Each is a
distinct anchor; one edit per occurrence below.

```edit:book/src/L4/eigsolve.md
[old]: eigsolve op inp = execState (solve_loop op inp) (initial_state inp)
[new]: eigsolve op inp = execState (solve_loop op inp) (initial_eig_state inp)
```

```edit:book/src/L4/eigsolve.md
[old]: - `Inputs` — the per-solve inputs that seed `initial_state` (the optional initial-subspace seed `control.initial_space`; when absent, the library generates its own by internal RNG). Read-only.
[new]: - `Inputs` — the per-solve inputs that seed `initial_eig_state` (the optional initial-subspace seed `control.initial_space`; when absent, the library generates its own by internal RNG). Read-only.
```

```edit:book/src/L4/eigsolve.md
[old]: Threaded by `Solve a = StateT EigState Identity a`; the cap's net effect is the `EigState` transition from `initial_state inp` to the terminal state, extracted by `execState`.
[new]: Threaded by `Solve a = StateT EigState Identity a`; the cap's net effect is the `EigState` transition from `initial_eig_state inp` to the terminal state, extracted by `execState`.
```

```edit:book/src/L4/eigsolve.md
[old]: out of the `solve_loop op inp` action run from `initial_state inp`. The eigenpair extraction
[new]: out of the `solve_loop op inp` action run from `initial_eig_state inp`. The eigenpair extraction
```

```edit:book/src/L4/eigsolve.md
[old]: 1. **`execState`/`StateT` discharge fusion** (the cap's defining identity). `eigsolve op inp = execState (solve_loop op inp) (initial_state inp)` — the cap *is* the `execState`-discharge of the `solve_loop` action.
[new]: 1. **`execState`/`StateT` discharge fusion** (the cap's defining identity). `eigsolve op inp = execState (solve_loop op inp) (initial_eig_state inp)` — the cap *is* the `execState`-discharge of the `solve_loop` action.
```

```edit:book/src/L4/eigsolve.md
[old]: `firm` — the `Solve`-monadic outer-driver cap `eigsolve op inp = execState (solve_loop op inp) initial_state` is the canonical top-of-stack coordination shape for the generalized eigenproblem,
[new]: `firm` — the `Solve`-monadic outer-driver cap `eigsolve op inp = execState (solve_loop op inp) initial_eig_state` is the canonical top-of-stack coordination shape for the generalized eigenproblem,
```

```edit:book/src/L4/eigsolve.md
[old]: - **L4**: `Solve`-monadic outer-driver cap `eigsolve op inp = execState (solve_loop op inp) initial_state`. The coordination is typed
[new]: - **L4**: `Solve`-monadic outer-driver cap `eigsolve op inp = execState (solve_loop op inp) initial_eig_state`. The coordination is typed
```

#### Fix (b) cross-file completion — repairer-added (cross-reference-integrity warning)

The critic (META.md Issues 1+2) correctly found the rename leaves un-flipped
eigsolve-cap occurrences in two cross-files the report asserted absent. The
following three edits complete the rename at cross-file scope. Verified on-disk
via `grep -n 'initial_state' book/src/L4/index.md`: lines **53, 68, 135, 140**
are the `ksp_solve` / generic `solve_loop` **SimState** rows and CORRECTLY STAY
`initial_state` (they are NOT flipped); only the two **eigsolve-cap**
occurrences (**56** the bullet, **132** the dep-map row) share the rename
rationale and flip.

```edit:book/src/L4/index.md
[old]: - [`eigsolve`](./eigsolve.md) — the `Solve`-monadic outer-driver **cap** for the generalized eigenproblem: `eigsolve op inp = execState (solve_loop op inp) initial_state`. Unlike the `ksp_solve` cap,
[new]: - [`eigsolve`](./eigsolve.md) — the `Solve`-monadic outer-driver **cap** for the generalized eigenproblem: `eigsolve op inp = execState (solve_loop op inp) initial_eig_state`. Unlike the `ksp_solve` cap,
```

```edit:book/src/L4/index.md
[old]: | [`eigsolve`](./eigsolve.md) | `eigsolve :: OpParams -> Inputs -> EigState`; entry `eigsolve op inp = execState (solve_loop op inp) (initial_state inp)`.
[new]: | [`eigsolve`](./eigsolve.md) | `eigsolve :: OpParams -> Inputs -> EigState`; entry `eigsolve op inp = execState (solve_loop op inp) (initial_eig_state inp)`.
```

The `synthesis/coordination.md:225-229` NOTE pins `eigsolve.md:44` by line and
calls the L4 chapter's `initial_state` reuse "a latent inconsistency to
reconcile upstream — lowering-verifier." Fix (b) IS that reconciliation: once it
lands, `eigsolve.md:44` writes `initial_eig_state inp`, so the NOTE's factual
premise goes stale and its "reconcile upstream" call is discharged. Re-phrase
(not a token-flip) to record that the reconciliation has landed and the L4
chapter now uses the EigState-coherent constructor.

```edit:book/src/synthesis/coordination.md
[old]: -- NOTE: the seed is `initial_eig_state` (the EigState constructor in the type block above),
-- DELIBERATELY eigen-specific. The authoritative L4 chapter (book/src/L4/eigsolve.md:44) writes
-- `initial_state inp`; here the cap threads `Solve a = StateT EigState Identity a`, so an
-- EigState-seeding constructor is the correct discharge (the L4 chapter's reuse of `initial_state`
-- for the EigState-threaded cap is a latent inconsistency to reconcile upstream — lowering-verifier).
[new]: -- NOTE: the seed is `initial_eig_state` (the EigState constructor in the type block above),
-- DELIBERATELY eigen-specific (the cap threads `Solve a = StateT EigState Identity a`, so an
-- EigState-seeding constructor is the correct discharge). The authoritative L4 chapter
-- (book/src/L4/eigsolve.md:44) now also writes `initial_eig_state inp` — the formerly-latent
-- naming inconsistency (the L4 chapter once reused `initial_state` for the EigState-threaded cap)
-- has been reconciled upstream; this render and the L4 chapter now agree.
```

### Fix (c) — add the omitted `units : Units` field to the synthesis `IoData` render

The rendered `IoData` block in `synthesis/types.md` lists only the five
`config::*Data` sub-records and omits the sixth top-level field `units :
Units`, which the authoritative `IoData` schema carries (`config-record.md:74`
in the schema block / `:85` in the field table; L0 home `iodata.hpp:38`,
`Units units;`, verified on-disk). Add the `units : Units` line, and widen the
cited-range comment that pins the sub-record correspondence from `:69-73` to
`:69-74` so it covers the `units` schema line too.

```edit:book/src/synthesis/types.md
[old]: -- The five sub-record type names below are the synthesized (clean-room) renderings
-- of the authoritative `config::*Data` types (config-record.md:69-73):
--   ProblemConfig ≡ config::ProblemData,  ModelConfig ≡ config::ModelData,
--   DomainConfig  ≡ config::DomainData,   BoundaryConfig ≡ config::BoundaryData,
--   SolverConfig  ≡ config::SolverData.
IoData = {
  problem    : ProblemConfig,     -- driver selector (problem.type) + solver-pipeline knobs
  model      : ModelConfig,       -- mesh file + refinement + material assignment
  domains    : DomainConfig,      -- per-domain materials + postprocessing energy regions
  boundaries : BoundaryConfig,    -- BC surfaces (PEC/PMC/impedance/lumped-port/wave-port/…)
  solver     : SolverConfig       -- linear/eigen/driven/transient solver settings + tolerances
}
[new]: -- The five sub-record type names below are the synthesized (clean-room) renderings
-- of the authoritative `config::*Data` types, plus the `Units` scale converter
-- (config-record.md:69-74):
--   ProblemConfig ≡ config::ProblemData,  ModelConfig ≡ config::ModelData,
--   DomainConfig  ≡ config::DomainData,   BoundaryConfig ≡ config::BoundaryData,
--   SolverConfig  ≡ config::SolverData.
IoData = {
  problem    : ProblemConfig,     -- driver selector (problem.type) + solver-pipeline knobs
  model      : ModelConfig,       -- mesh file + refinement + material assignment
  domains    : DomainConfig,      -- per-domain materials + postprocessing energy regions
  boundaries : BoundaryConfig,    -- BC surfaces (PEC/PMC/impedance/lumped-port/wave-port/…)
  solver     : SolverConfig,      -- linear/eigen/driven/transient solver settings + tolerances
  units      : Units              -- SI ↔ nondimensional scale converter (set by nondimensionalization)
}
```

## Supporting evidence

- **(a)** Canonical CG Form B call shape verified at
  `book/src/L4/krylov-step.md:192-199` (the c138-current bootstrap-closure /
  init-carry / steady / cont arg order). The stale §Evidence prose at
  `book/src/L4/iterate-while-with-prev.md:233` showed the pre-split
  `iterate_while_with_prev s1 s0.beta (\(s, _) -> ...) (\(s, beta_prev) -> ...)`
  shape; the carry-first/prev-second closure-convention note is preserved
  verbatim (it remains correct and is not part of the staleness).
- **(b)** All `initial_state` occurrences in `book/src/L4/eigsolve.md`
  enumerated by grep: lines 44, 69, 70, 97, 109, 180, 189 — every one names the
  `EigState`-seeding constructor threaded by `Solve = StateT EigState Identity`
  (§Signature line 70, §Laws line 109). No occurrence references an L3-kernel
  `initial_state` or a non-EigState ctor; the L3 kernel `L3/eigsolve.md` is a
  separate file and out of scope for this fix. Flipping all seven keeps the
  cap's signature, prose, laws, status, and L4-vs-L3 sections internally
  consistent and aligned with the already-correct Synthesis render.
- **(c)** Authoritative `IoData` schema carries six top-level fields including
  `units : Units` — `book/src/concepts/config-record.md:67-75` (schema block,
  `units : Units` at line 74) and `:78-85` (field table, `units` row at line 85,
  L0 home `iodata.hpp:38`). L0 backing verified on-disk via codemap
  `read_range palace/utils/iodata.hpp:28-42` → line 38 is `Units units;`
  (member of `IoData`, with the preceding comment "Class that holds mesh scale
  and converts between SI quantities and normalized values."). The added field
  meaning is paraphrased from the authoritative table row (config-record.md:85);
  the synthesis chapter remains a VIEW that links to the authoritative schema
  (no L0 re-cite added to the chapter body — the `config-record.md` pointer at
  `types.md:28/32` already carries the authoritative-home link).

## Open questions / caveats

- None of these three are correspondence or citation defects — the Synthesis
  rendered defs were already faithful; these fixes bring the **upstream L4
  chapters** (a, b) and the **synthesis type-render completeness** (c) into line
  with the audited-correct Synthesis forms. The three named OQs
  (`iterate-while-with-prev-evidence-prose-stale-cg-call-shape`,
  `l4-eigsolve-initial-state-vs-initial-eig-state-seed-inconsistency`,
  `synthesis-types-iodata-omits-units-field`) are discharged by these edits.
- Fix (b) widened from the 2 prompt-named lines (44, 97) to all 7 in-file
  occurrences after the per-prompt consistency check — flagging the extra 5
  (69, 70, 109, 180, 189) here for the integrator's awareness: they are the
  same ctor token and must flip together, else the chapter would carry a mixed
  `initial_state` / `initial_eig_state` naming (the exact inconsistency the OQ
  names). No `eigsolve.md` occurrence was left un-flipped.
  **REPAIRER CORRECTION (cross-reference-integrity warning):** the original
  report's claim that "no L3-kernel or L4-sibling cross-file occurrence exists"
  was FALSE at cross-file scope — the eigsolve cap recurs un-flipped in
  `L4/index.md` (the bullet :56 + the dep-map row :132) and the
  `synthesis/coordination.md:225-229` NOTE explicitly pins `eigsolve.md:44` as
  the reconcile-upstream target. The repairer added the two `L4/index.md` flips
  (with `index.md:53/68/135/140` SimState rows correctly left as `initial_state`)
  and re-phrased the now-stale `coordination.md` NOTE; see the "Fix (b)
  cross-file completion" block under §Proposed changes. The cross-file rename is
  now complete.
- No `synthesis/index.md` matrix-mirror cell flips needed: these are content
  edits within already-bodied chapters (no rendered-status shell→bodied
  transition), so the index-cell-drift guard does not fire.
