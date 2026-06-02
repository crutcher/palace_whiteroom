---
verifies: ../CYCLE.md
critiqued_at: 2026-06-02T010000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
---

# META: verification of CYCLE — solve_family (fixed-operator map-over-RHS solve combinator)

## Critique

### Checks run

**citation-validity: pass.** Every load-bearing pinpoint was re-read via codemap and confirmed in-range and on-token. The two positive witnesses are exact: electrostatic `electrostaticsolver.cpp:30` (`auto K = laplace_op.GetStiffnessMatrix();`, operator captured once), `:35-36` (`KspSolver ksp(...)` + `ksp.SetOperators(*K, *K);`, solver built once OUTSIDE the loop), `:60` (`for (const auto &[idx, data] : laplace_op.GetSources())`), `:68-69` (`GetExcitationVector(idx, *K, V[step], RHS); ksp.Mult(RHS, V[step]);`), `:46` (`std::vector<Vector> V(n_step);`), `:42` (`MFEM_VERIFY(n_step > 0, ...)`) — all verbatim. Magnetostatic `magnetostaticsolver.cpp:30` / `:35-36` / `:66` (`for (... : curlcurl_op.GetSurfaceCurrentOp())`) / `:76-77` (`GetExcitationVector(idx, RHS); ksp.Mult(RHS, A[step]);`) / `:47` (`std::vector<Vector> A(n_step);`) / `:42-43` (`MFEM_VERIFY`) — all verbatim. The negative witness `drivensolver.cpp` is accurate: the `for (omega_i ...)` frequency loop opens at 168-170, `GetSystemMatrix(...)` at 176-177 assembles the ω-dependent `A`, and `ksp.SetOperators(*A, *P)` is at line 180 — INSIDE the loop, confirming the operator is rebuilt per-ω (the report's `:176-180` range encloses both, with the SetOperators-inside-loop break exactly as described). The firm-vocabulary grounding citations also resolve: `L4/index.md:75` is the `eigsolve` row (the stated insertion anchor); `L4/ksp_solve.md:28` ("sits *above* the `iterate-while` family … not inside it"), `:100` (`solve_loop` tail-recursion ≡ `iterate_while_pure`), `:114` (zero-RHS / Outcome degenerate-identity), `:116` (nested-cap non-commutativity), `:153` (element-type absorption) all carry the asserted content. The strawman `design/l4_calculus.md:150-184` is §3.7 `iterate_while`, and `:178-182` is precisely the `iterate_while_pure` sugar the "pure-map degenerate" claim rests on. `state-stratification.md` and `iterate-while.md` exist on disk. The cycle-053 discharge framing ("single-witness gate DISCHARGED → fixed-operator combinator mineable at 2-of-N") is corroborated verbatim by `log/cycle-053.md:5,9` including the explicit "3rd driven probe is NOT a mining precondition" note.

**surface-or-evidence: pass.** This is a combinator-mining proposal, not a refinement of existing operator/theme surface text. It proposes a NEW L4 rough-in dep-map row (additive vocabulary), grounded in two positive source witnesses + one negative scope-boundary witness + firm-vocabulary anchoring. The surface-or-evidence check is for refinement-shaped proposals modifying existing operators; here the proposal is net-new and evidence-backed, so the check is satisfied (additive proposal with rotation-claim-equivalent witness evidence). Not a pure unsupported rotation_claim.

**rotation-quality: pass (applies to the implied L4 abstraction over the L3 C++ shape).** The combinator is strictly more abstract than the witnessed L3 form: the Palace `std::vector<Vector> V(n_step)` pre-sized accumulator + positional `step++` indexing + `for`-loop over a `GetSources()`/`GetSurfaceCurrentOp()` index set collapses to `solve_family op rhss = map (\inp -> ksp_solve op inp) rhss`. This is genuine state-hiding (the positional `step` counter and the pre-sized vector disappear into the `map`), genuine operator-capture stratification (the `SetOperators(*K,*K)`-outside-the-loop hoist becomes the `op : OpParams` bound once outside the map, threaded unchanged — a `readonly` stratum), and a more-equational form (the map-fusion / concatenation-homomorphism law is stated as the structural payoff). Not a rename, not 1:1. The "pure-map degenerate of `iterate_while`" framing correctly reuses the firm iterate-while vocabulary rather than inventing a new iteration primitive (the chebyshev precedent, `index.md:37`).

**variant-axis-coverage: pass.** Four axes are enumerated, and the load-bearing one is handled correctly. The `operator-capture` axis (`fixed | per-element`) is THE distinguishing axis: `fixed` IS `solve_family` (this combinator, electrostatic + magnetostatic), `per-element` is the superset `map_solve_over_(operator,rhs)_family` (driven), explicitly scoped OUT to a batch-17 probe rather than silently folded in — no hidden branch. `family-index-domain`, `element-type` (real/complex, absorbed into `OpParams`/`Inputs` as at the `ksp_solve` cap per `:153`), and `collection-shape` (pre-sized-vector vs append, a lowering concern) are each named and dispositioned (absorbed / not-semantic). The driven break is the explicit witness for why the `per-element` branch is a distinct combinator, not a `solve_family` variant — the scope-out is principled.

**cross-reference-integrity: pass.** The proposed dep-map row's live links `[`ksp_solve`](./ksp_solve.md)` and `[`iterate-while`](./iterate-while.md)` both resolve to existing files. The `solve_family` slug itself is correctly rendered plain-text inline-code (`` `solve_family` *(rough-in)* ``), NOT a live link to the not-yet-existing `solve_family.md` — this respects the `rough-in-forward-reference-must-be-plain-text-not-live-link` convention and avoids a `linkcheck2` hard error. The report explicitly declines to register a `SUMMARY.md` row (correct — no chapter exists yet) and declines to author `solve_family.md` (harvester's job). Named concept slugs (`state-stratification`, `solve-monad`, `derived-view-hoisting`, `variant-absorption`) referenced in the row are pre-existing concept vocabulary. Build-readiness fence guard: the proposed-changes block (`edit:book/src/L4/index.md`, open line 175 / close line 179) has even fence parity and is a pure dep-map-row append (no firm-body-outside-fence concern — this is a rough-in row, no `## Status` apparatus claimed). The inner signature-sketch fence (106/127) is in the report body, not inside the proposed-changes block — no nesting hazard.

**edge-label-fidelity: pass.** The proposal carries no L_{n+1}→L_n edge label as its primary claim; it is an L4 vocabulary-row proposal. It correctly DEFERS the L4>L3 dissolution (`L4-L3/solve-family-map-dissolution`) to batch-17 and names it as pending in the "Lowers to" cell, rather than asserting a rotation it did not author. The high→low discipline is respected (the entry defines `solve_family` in L4 vocabulary only; the L4>L3 rewrite is explicitly not authored here). No edge-label/prose mismatch.

**plan-kind-consistency: pass.** Declared kind is a combinator-miner rough-in dep-map row, and the content matches: a `rough-in`-tagged row with provenance (`proposed-by: combinator-miner:...`), 2 fixed-operator witnesses + 1 superset witness cited, a signature sketch (explicitly "harvester will firm up"), and law-confidence flagged `test-coverage-bounded` pending harvester firming. It does NOT over-claim `firm` status, and it correctly routes the file authoring + the two specialization entries + the L4>L3 theme to batch-17. The maturity tier (rough-in row, file deferred) is consistent throughout.

**skill-uptake-survey: warning (non-blocking telemetry).** The proposal's shape implies relevant skills that the report does not reference invoking: `propose-rotation` / `verify-rotation-citation` (the combinator's abstraction-over-L3 rotation), and the cycle-053-discharge "single-witness → 2nd-pipeline-probe → discharge" disciplined-mining gate (which `log/cycle-053.md:13` flags as a reusable pattern but which is not yet a named skill). The report's mining discipline is in fact exemplary (≥2-witness bar honored, scope caveat carried, no over-unification), so this is pure surfacing — the underlying procedure is followed even though no skill invocation is cited. Candidate worth crystallizing (see skill-candidates note below). Not blocking.

### Issues found

No blocking issues. The report is citation-clean, scope-disciplined, and hygienically wired. Minor / telemetry-only observations:

1. **(telemetry, severity: info) skill-uptake not cited** — `reports/.../CYCLE.md` §Proposed combinator / §Open questions. The disciplined-mining gate ("don't author a cross-pipeline combinator from a single witness; confirm ≥2 pipelines first; a break sharpens scope") is followed in substance but no skill invocation is referenced, and no named skill yet exists for it. Surfaced for skill-candidate crystallization, not a defect in the report.

2. **(borderline, severity: info, NOT a defect) 2-witness soft-bar** — §Pattern instances:62 self-discloses "the soft bar for a same-shape combinator is ≥3; this is at the borderline-2." This is correctly disclosed and explicitly licensed by the cycle-053 single-witness-gate discharge (`log/cycle-053.md:9`, which set the bar at 2-of-N for this specific combinator and declared the 3rd probe NOT a precondition). The two witnesses are structurally identical down to the `GetStiffnessMatrix()` / `SetOperators(*K,*K)` / `std::vector<Vector>` shape (verified verbatim), and the negative driven witness sharpens rather than weakens the scope. The borderline-2 is honestly framed and methodologically sanctioned — flagged here only so the integrator sees it was checked, not as a finding to repair.

3. **(scope, severity: info, correctly handled) transient/eigenmode unprobed** — §Open questions:216-232. The report does NOT over-claim cross-pipeline generality: it scopes `solve_family` to the 2 fixed-operator witnesses, names driven as the `per-element` superset witness, and explicitly leaves transient + eigenmode unprobed with the load-bearing caveat that transient may be a `fold` (state carried between time-steps → `solve_loop`-shaped, NOT `solve_family`-shaped) and must be probed before any general-form promotion "to avoid over-unifying a fold into a map." This is exactly the right guard against over-unification. No over-claim.

---
repaired_at: 2026-06-02T013000Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

## Repair

### Fixes attempted

- **Finding**: skill-uptake-survey warning — disciplined cross-pipeline combinator-mining gate ("don't author from a single witness; confirm ≥2 pipelines; a break sharpens scope") followed in substance but no skill invocation cited, and no named skill yet exists for it.
  - **Decision**: not-needed (telemetry-only, non-blocking).
  - **Rationale**: This is pure surfacing. The critic explicitly notes the underlying procedure is followed (≥2-witness bar honored, scope caveat carried, no over-unification) — there is no defect in the report to repair. The candidate is a skill-crystallization signal, not a report flaw. The critic has already appended `disciplined-cross-pipeline-combinator-mining-gate` to `scaffolding/skill-candidates.md`; no further repairer action is warranted. A `warning` of severity `info/telemetry` does not gate `ready`.

- **Findings (issues-found items 2 and 3)**: 2-witness soft-bar borderline; transient/eigenmode unprobed.
  - **Decision**: not-needed (both flagged `severity: info, NOT a defect` / `correctly handled` by the critic).
  - **Rationale**: Item 2 is honestly disclosed and methodologically sanctioned by the cycle-053 single-witness-gate discharge (bar set at 2-of-N for this combinator; 3rd probe explicitly NOT a precondition). Item 3 is the correct over-unification guard (transient may be a `fold`, not a `map`), correctly scoped out to a batch-17 probe. Neither is a finding to repair; both were surfaced so the integrator sees they were checked.

### Unrepairable findings

None. No finding exceeds repair authority because no finding is a defect — all 7 substantive checks pass and the single warning is telemetry-only.

## Suggested resolution

`ready`. Notes for the integrator:

- **D1 proposed-changes = ONE rough-in dep-map row** in `book/src/L4/index.md` (`edit:` block, open line 175 / close line 179, even fence parity). The `solve_family` slug is rendered plain-text inline-code (`` `solve_family` *(rough-in)* ``) — NOT a live link — so there is no `linkcheck2` hazard. Do NOT expect a `solve_family.md` file, a `SUMMARY.md` row, the two specialization entries, or the `L4-L3/solve-family-map-dissolution` theme: all of those are explicitly batch-17 (harvester + abstractor follow-on). The row's two live links (`./ksp_solve.md`, `./iterate-while.md`) resolve to existing files.
- **Promote D1's OQs** for the batch-16 meta-phase, flagged as the lead batch-17 frontier item:
  - the general-form superset `map_solve_over_(operator,rhs)_family` (the `per-element` operator-capture axis; driven is the witness — `drivensolver.cpp:176-180` rebuilds the operator inside the loop);
  - the driven/transient 3rd-probe (transient may be a `fold`/`solve_loop`, not a `map`/`solve_family` — must be probed before any general-form promotion, to avoid over-unifying a fold into a map).
