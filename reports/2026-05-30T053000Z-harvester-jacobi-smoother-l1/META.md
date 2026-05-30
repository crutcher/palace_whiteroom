---
verifies: ../CYCLE.md
critiqued_at: 2026-05-30T05:55:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: fail
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-05-30T06:15:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of harvester `jacobi-smoother` at L1 (cycle-032)

## Critique

### Checks run

**citation-validity** — Ran `python3 tools/citecheck/citecheck.py --scan reports/2026-05-30T053000Z-harvester-jacobi-smoother-l1/CYCLE.md --quiet`: **68 ok, 0 failing (68 citations checked)** — all in-bounds, all paths resolve under `reference/palace/`. Then ran targeted `--anchor` probes on every load-bearing pinpoint:
- `palace/linalg/jacobi.cpp:74-97` `'SetOperator'` → ok at line 75
- `palace/linalg/jacobi.cpp:79` `'AssembleDiagonal'` → ok at line 79
- `palace/linalg/jacobi.cpp:80` `'Reciprocal'` → ok at line 80
- `palace/linalg/jacobi.cpp:99-104` `'Mult'` → ok at line 100
- `palace/linalg/jacobi.cpp:102` `'initial_guess'` → ok at line 102
- `palace/linalg/jacobi.cpp:103` `'Apply'` → ok at line 103
- `palace/linalg/jacobi.cpp:38` `'Y[i] = DI[i]'` → ok at line 38 (the elementwise kernel — law 1 witness)
- `palace/linalg/jacobi.cpp:30-39` `'forall_switch'` → ok at line 38
- `palace/linalg/jacobi.cpp:41-70` `'Apply'` → ok at line 42
- `palace/linalg/jacobi.cpp:84-89` `'lambda_max'` → ok at lines 86, 87, 88
- `palace/linalg/jacobi.cpp:90-93` `'omega'` → ok at lines 90, 92
- `palace/linalg/jacobi.cpp:106-107` `'template class JacobiSmoother'` → ok at lines 106, 107
- `palace/linalg/jacobi.cpp:14-28` `'GetLambdaMax'` → ok at lines 14, 22
- `palace/linalg/jacobi.hpp:19` `'class JacobiSmoother'` → ok at line 19
- `palace/linalg/jacobi.hpp:34` `'JacobiSmoother(MPI_Comm'` → ok at line 34
- `palace/linalg/jacobi.hpp:43` `'MultTranspose'` → ok at line 43
- `palace/linalg/solver.hpp:32-33` `'initial_guess'` → ok at line 33
- All 5 consumer citations (`ksp.cpp:198-200`, `errorestimator.cpp:75-77`, `floquetcorrection.cpp:65`, `spaceoperator.cpp:640`, `timeoperator.cpp:85`) → ok
- `palace/linalg/vector.cpp:248-261` `'Reciprocal'` → ok at line 248
- `palace/linalg/chebyshev.cpp:13-27` `'GetLambdaMax'` → ok at lines 14, 22 (sibling-precedent)
- `palace/linalg/chebyshev.cpp:177-178` `'AssembleDiagonal'` → ok at line 177 (sibling-precedent for identical setup chain)
- `palace/linalg/chebyshev.hpp:37` `'real-valued'` → ok at line 37

Independently spot-read `reference/palace/palace/linalg/jacobi.cpp:30-104` and `jacobi.hpp:14-43` to confirm the report's structural claims (elementwise multiply kernel at line 38; setup chain `AssembleDiagonal → Reciprocal → ω-fold` at lines 79-93; `Mult` body asserts `!initial_guess` at line 102 then dispatches `Apply(dinv, x, y)` at line 103; `MultTranspose` aliases `Mult` at hpp:43; complex `Apply<Transpose=true>` else-branch at lines 61-69; both `template class` instantiations at 106-107). All match. **One sub-range observation, not a fail**: the report repeatedly cites the complex `Transpose=true` kernel as `palace/linalg/jacobi.cpp:61-68` (e.g. lines 161, 275, 437, 506 of CYCLE.md). The else-block actually spans lines 61-69 (closing `}` at line 69); lines 61-68 captures the substantive kernel body including the `});` close at line 68 but excludes the brace at line 69. Substantively accurate — the cited content is in-range — but ideally tightened to `:61-69` (or `:63-68` for the kernel proper) when the repairer touches this region. PASS.

**surface-or-evidence** — This is a NEW operator entry (refinement-shape inapplicable in the strict "modifying surface of existing operator" sense; the report creates `book/src/L1/jacobi-smoother.md` from scratch). The creation IS the surface; every L1 claim is either traced to a cited L0 range (the 22+ inline cites in the body — `:38` for elementwise kernel; `:79-80` for AssembleDiagonal+Reciprocal; `:84-89` for spectral damping; `:90-93` for omega absorption; `hpp:43` for transpose alias; etc.) or stated as an algebraic law derivable from those cites. The 4 explicitly-named non-laws each carry their own evidentiary basis (e.g. dead-code Hermitian kernel grounded in `:61-69` source presence + `hpp:43` non-reference; matrix-free non-law propagated from cited `assemble-diagonal` law). PASS.

**rotation-quality** — The L1 form `y = jacobi_smoother(op, x) = op.dinv ⊙ x` vs the L0 form `Mult(x, y) const` (writes through `y` via `Apply(dinv, x, y)`) is a genuine state-hiding rotation: the destination buffer is dropped; the function returns a fresh tensor. The `op` closure carries the **reduced** operator content (`dinv, omega, sf_max`) — the captured `A` is dropped post-setup (a true forgetting, not just renaming). The `!initial_guess` precondition is hoisted from L0 assertion to L1 type-precondition. The damping-mode branching is collapsed at setup (the apply does not branch). The element-type variant is absorbed into the closure type `JacobiSmoother[N]`. Strictly more compact + more abstract than L0 (L0 has destination-buffer mutation + initial_guess flag + per-element runtime kernel dispatch + `Apply<Transpose>` template branch; L1 has a single equational `dinv ⊙ x`). Firm-on-positive-structure rationale is well-grounded: every law is a syntactic identity on the read closure (linearity from `Y[i] = DI[i] * X[i]`; round-trip from `AssembleDiagonal + Reciprocal`; damping absorption from `dinv *= omega`; self-transpose from `MultTranspose{ Mult(x,y); }`) — not literature-inferred convergence claims, so the missing dedicated `test-jacobi.cpp` does not gate. The `chebyshev-smoother` precedent (cited and cross-checked) is the matching prior. Negative-anchor independently verified: `grep -rn 'JacobiSmoother' reference/palace/test/unit/` returns 0 matches; `grep -rn 'Jacobi' …` returns exactly one match (`test-libceed.cpp:1128`, an unrelated `// MFEM's GradientIntegrator only supports square Jacobians` comment) — the no-dedicated-test claim is real. PASS.

**variant-axis-coverage** — Two variant axes claimed, both source-witnessed and absorbed: (a) **element-type** (real `Operator` / complex `ComplexOperator`) — both instantiations cited (`:106-107`); the divergence from `chebyshev-smoother`'s real-only `dinv` is correctly identified and grounded (`hpp:28` `VecType dinv` for jacobi vs `chebyshev.hpp:37` "real-valued for now"); the complex `ComplexVector::Reciprocal` implementing the full complex reciprocal is cited (`vector.cpp:248-261`). (b) **damping-mode** (`default ω=1.0` | `fixed ω≠0` | `estimated ω=0`) — all three branches grounded in `:84-93` source; all five call sites correctly attributed (4 default + 1 estimated; 0 fixed, called out as a recorded asymmetry in OQ #5). The `sf_max` is correctly identified as a parameter, not a variant axis. The dead-code `Apply<Transpose=true>` kernel is acknowledged as a caveat (existing in source but unreferenced under symmetric `MultTranspose = Mult` wiring) — not a hidden branch. The representation-axis of the underlying `A` (sparse/matrix-free) is correctly identified as collapsed via inherited `assemble-diagonal` absorption (law 6 propagation, not a fresh axis). No hidden branches detected; all source-witnessed combinations either covered or explicitly scoped out (the fixed-`ω` consumer-coverage gap is documented in OQ #5 as a known asymmetry, not a missed branch). PASS.

**cross-reference-integrity** — Verified each live link in the chapter body against on-disk state. **PASS targets**: `./assemble-diagonal.md`, `./chebyshev-smoother.md`, `./ksp_solve.md`, `./eigsolve.md`, `./divfree-projector.md`, `./apply_linop.md`, `./apply_nonlinear_pencil.md`, `../concepts/variant-absorption.md` — all on disk. **Fence-parity check**: ran `grep -n '^\`\`\`' CYCLE.md` → 8 fences (lines 31, 580, 582, 586, 588, 591, 593, 596) — even parity, 4 paired blocks. The `new:book/src/L1/jacobi-smoother.md` block runs `31→580` (~549 lines); the full firm-apparatus (`## Signature`, `## Semantics`, `## Algebraic laws`, `## Dependencies`, `## Variant axes`, `## Status` at line 405, `## L1 vs L0 distinction`, `## Evidence`) is INSIDE the fence. The cycle-019 firm-body-outside-fence defect class does NOT apply here. **The two `edit:book/src/L1/index.md` blocks** insert after the existing `ls_update_column` prose row (book/src/L1/index.md:54) and table row (:97) — well-positioned. The `edit:book/src/SUMMARY.md` block adds `jacobi-smoother` after `ls_update_column` (already at SUMMARY:87) — thin-anchor edit, conventional. **The L1>L0 mutation-rotation theme is correctly plain-text** (not a live link) in the report's chapter and OQ #1 — the theme is forthcoming.

**FAIL — dead live links to non-existent on-disk targets**: at chapter line 324 (CYCLE.md line 324), the body contains: `([`reciprocal`](./reciprocal.md), [`elementwise_product`](./elementwise_product.md), recorded here as plain text)`. Both `book/src/L1/reciprocal.md` and `book/src/L1/elementwise_product.md` do NOT exist on disk (verified via `ls`). This is the canonical `rough-in-forward-reference-must-be-plain-text-not-live-link` defect: the parenthetical *says* "recorded here as plain text" but the syntax is in fact live-link Markdown that would cause a `linkcheck2` build error on `cargo make book`. The repair is mechanical (drop the link wrappers; keep as bold backticks: `` `reciprocal` `` and `` `elementwise_product` ``). Note OQ #3 also discusses these as forthcoming primitives — fully consistent with plain-text-only treatment until stubs are materialized. The contradiction between the prose ("recorded here as plain text") and the actual Markdown (live links) is the giveaway. FAIL.

**edge-label-fidelity** — The report carries no L_{n+1}→L_n edge label per se (this is a single-layer L1 operator harvest, not a lowering theme). The "L1 vs L0 distinction" section narrates the rotation between L1 (pure functional) and L0 (in-place Mult) but uses standard direction (L1 form → L0 source, the forward narration matching the codified high→low layer-definition invariant). No edge-label / prose mismatch detected. PASS (not applicable to single-layer L_n harvester scope in the strict L_{n+1}→L_n edge-label sense; the implicit L1→L0 narrative direction is correct).

**plan-kind-consistency** — Harvester formalizing one L1 operator, declared `firm` status, full chapter body with all expected sections (Context, Signature, Semantics, Algebraic laws, Dependencies, Variant axes, Status, L1 vs L0 distinction, Evidence). The firm-on-positive-structure framing matches the `apply_linop` / `chebyshev-smoother` / `apply_nonlinear_pencil` precedent class. Two `edit:` blocks for the L1 index (prose row + table row) and one for SUMMARY are the conventional harvester-companion deltas. The `partly-constructive` / `rough-in (test-coverage-bounded)` qualifiers are NOT used — appropriate here because the laws are syntactic identities on positive source (the firm-on-positive-structure escape applies), not constructed from negative anchors and not test-gated semantics. The shape matches the declared kind precisely. PASS.

**skill-uptake-survey** — The report carries explicit `tools/citecheck/citecheck.py --anchor` invocations for all load-bearing pinpoints (CYCLE.md lines 614-632, 16 anchor probes recorded) — the cycle-024 mechanical-citecheck adoption is well-uptaken. The `find-tests-for-region` skill is implicitly invoked via the negative-anchor `grep -rn 'Jacobi' test/unit/` probe (CYCLE.md lines 633, 573-579) with the one unrelated match explicitly catalogued — the skill's negative-finding-exhaustiveness shape is followed. The `chebyshev-smoother` firm-on-positive-structure precedent is cited verbatim (multiple times). The `verify-rotation-citation` skill's shape is followed implicitly (every law cited to a positive source range). The cycle-022 stub-creation invariant is correctly deferred to the integrator in OQ #3 (the harvester does not unilaterally create stubs; recognizes the ≥2-forward-reference threshold has been crossed but defers the decision). No skill mis-uptake or skill-friction signal. PASS.

### Issues found

1. **CYCLE.md:324 — dead live links to non-existent forward-referenced L1 primitives** (severity: blocking-build). The chapter's `## Dependencies` section has `([`reciprocal`](./reciprocal.md), [`elementwise_product`](./elementwise_product.md), recorded here as plain text)` — both targets are not on disk (`book/src/L1/reciprocal.md` and `book/src/L1/elementwise_product.md` do not exist). The parenthetical explicitly says "recorded here as plain text" but the Markdown is live-link syntax. This is the canonical `rough-in-forward-reference-must-be-plain-text-not-live-link` friction-ledger defect; it would surface as a `linkcheck2` build error at `integrator-finalize` `cargo make book` time. Repair is mechanical: convert `[`reciprocal`](./reciprocal.md)` → `` `reciprocal` `` and `[`elementwise_product`](./elementwise_product.md)` → `` `elementwise_product` `` (preserving backticks). Affects only line 324 of CYCLE.md (and one chapter location once applied).

2. **CYCLE.md:161, 275, 437, 506 — minor sub-range tightening on Transpose=true citation** (severity: low; not blocking). The complex `Apply<Transpose=true>` else-branch is cited as `palace/linalg/jacobi.cpp:61-68` in four places. The else-block actually spans lines 61-69 (closing `}` at line 69; final `});` at line 68). The cited range substantively captures the kernel body and is in-bounds, but ideally is `:61-69` (full else-block) or `:63-68` (kernel proper, excluding `else {`). Citecheck `--anchor` on `'else'` against `:61-69` succeeds; the substantive content is correct in all four citing sentences (the negation of `DII` real-part and `XR` imaginary-part terms is on lines 66-67 which are inside `:61-68`). No semantic error; range-bound polish only.

3. **CYCLE.md OQ #5 — fixed-damping mode consumer-coverage gap** (severity: informational; correctly self-disclosed). The report notes 0/5 consumer sites use the `ω ≠ 0 ∧ ω ≠ 1.0` fixed-damping mode, and that the source path exists at `:90-93` but is consumer-dead. This is correctly recorded as an OQ rather than a status reduction, and matches the variant-axis-coverage invariant (source-witnessed branches counted; the fixed mode IS source-witnessed at `:90-93` even if not consumer-exercised). No action required from the repairer; flagged here so the integrator/planner can route the OQ.

## Repair

### Fixes attempted

- **Finding 1 (cross-reference-integrity, blocking)**: CYCLE.md:324 — dead live links `[`reciprocal`](./reciprocal.md)` and `[`elementwise_product`](./elementwise_product.md)` to non-existent on-disk targets `book/src/L1/reciprocal.md` and `book/src/L1/elementwise_product.md`.
  - **Decision**: repaired.
  - **Action**: stripped both link wrappers in the chapter body's `## Dependencies` parenthetical at CYCLE.md:324 (inside the `new:book/src/L1/jacobi-smoother.md` proposed-changes fence). Result: `(`reciprocal`, `elementwise_product`, recorded here as plain text)` — bold-backtick inline-code, matching the parenthetical's stated "recorded here as plain text" intent and aligning with `rough-in-forward-reference-must-be-plain-text-not-live-link`. Verified post-edit: `grep '](./'` over the file now lists only on-disk-existing targets (the 11 verified `./assemble-diagonal.md`, `./chebyshev-smoother.md`, `./ksp_solve.md`, `./eigsolve.md`, `./divfree-projector.md`, `./apply_linop.md`, `./apply_nonlinear_pencil.md`, `./jacobi-smoother.md`, `./back_solve.md`, `./ls-update-column.md`, `./lu_solve.md`, `./orthogonalize.md`, plus the SUMMARY entries `./L1/jacobi-smoother.md`, `./L1/ls-update-column.md`). The two non-existent targets are gone.

- **Finding 2 (citation-validity, non-blocking sub-range tightening)**: CYCLE.md cites the complex `Apply<Transpose=true>` else-branch as `palace/linalg/jacobi.cpp:61-68` in 5 places (CYCLE.md:159, 183, 275, 433, 505, 585, and the citation-summary line 637) plus the in-prose "(lines 61-68)" at lines 159 and 505. The else-block actually spans lines 61-69 (closing `}` at line 69).
  - **Decision**: repaired.
  - **Action**: verified `:61-69` on disk with `tools/citecheck --anchor 'else'` (passes — anchor at line 61, range 61-69 in bounds; `--show` confirms the range cleanly captures `else { ... }` including the closing brace at line 69). Applied `replace_all` for `jacobi.cpp:61-68` → `jacobi.cpp:61-69` (5 occurrences) and for `(lines 61-68)` → `(lines 61-69)` (2 occurrences in prose at lines 159, 505), plus the bare `:61-68` token in the citation-summary at line 637. Total: 8 in-place updates across CYCLE.md. No semantic content changed — the kernel body the surrounding prose references is unchanged; the range just now includes the closing brace. The `:63-68` alternative (kernel proper, excluding `else {`) was not adopted because the prose narration at lines 159 and 505 says "the `Transpose = true` branch (lines 61-69)" which reads the else-block as a unit; the kernel-proper sub-tightening would re-anchor that prose, exceeding the repair authority's "sub-range tightening" bar.

- **Finding 3 (informational, no action)**: fixed-damping consumer-coverage asymmetry self-disclosed as OQ #5.
  - **Decision**: not-needed.
  - **Action**: none — correctly recorded by the harvester as an OQ for planner routing, not a defect.

### Unrepairable findings

None.

### Post-repair verification

- `python3 tools/citecheck/citecheck.py --scan reports/2026-05-30T053000Z-harvester-jacobi-smoother-l1/CYCLE.md --quiet` → **68 ok, 0 failing** (exit 0). Citation set unchanged in cardinality (the `:61-68` → `:61-69` are in-place edits of existing tokens, not new citations); all still in bounds.
- Fence parity preserved: `grep -n '^```'` → 8 fences at lines 31, 580, 582, 586, 588, 591, 593, 596 — 4 paired blocks (the ~550-line `new:book/src/L1/jacobi-smoother.md` body 31→580, plus the three short `edit:` blocks for `book/src/L1/index.md` × 2 and `book/src/SUMMARY.md`). The firm-apparatus (`## Signature`, `## Semantics`, `## Algebraic laws`, `## Dependencies`, `## Variant axes`, `## Status`, `## L1 vs L0 distinction`, `## Evidence`) stays fully INSIDE the new-chapter fence.
- Cross-reference scan: `grep '](./'` over CYCLE.md now shows ZERO references to non-existent on-disk targets. Every `[name](./path.md)` resolves to a real file under `book/src/L1/` (or `book/src/` for the SUMMARY entries).
- OQ #3 (`reciprocal-and-elementwise-product-l1-primitives`) is correctly preserved as the forward route for stub-creation per the cycle-022 "Integration may materialize implied components as stubs" invariant — the ≥2-forward-reference threshold (assemble-diagonal + jacobi-smoother) is recorded; the integrator-per-report or a future cycle decides whether to materialize the stubs.

## Suggested resolution

`overall_status: ready` — both blocking finding 1 (cross-reference-integrity dead-link defect) and non-blocking finding 2 (sub-range tightening) are mechanically repaired in place. Citation count holds at 68/68 ok; fence parity holds at 4 paired blocks; relative-link targets are all on-disk. The integrator-per-report can apply the proposed changes as-is. The deferred stub-creation decision for `reciprocal` and `elementwise_product` (OQ #3) is routed to the integrator-per-report under the cycle-022 invariant — that is a content decision out of repair scope.
