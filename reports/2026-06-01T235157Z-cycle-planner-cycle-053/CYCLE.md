---
agent: cycle-planner
invoked_at: 2026-06-01T235157Z
scope: cycle-053 dispatch plan
status: pending
---

# Cycle 053 dispatch plan

## Goals selected this cycle

Cycle-053 is the SECOND primary cycle of meta-batch-16 (cycles 052/053/054; the batch-16 meta-phase fires AFTER cycle-054's finalize). The refactor pass COMPLETED at cycle-052 (commit `9633c13`) — all 12 fold-family leaf chapters are combinator-pointer stubs; the spine is in its corrected vocabulary-shift shape. The c052 D5/D6 convergence is the controlling input: the firm BLAS/projector/smoother spine is **combinator-complete for in-layer conciseness** (D5 negative), so the next combinator comes from **newly-lifted solver test-load material** (D6 electrostatic probe surfaced 4 spine work-items).

This cycle pushes the **solver test-load** (redirect program item 3) + continued spine abstraction (item 2b) under the redirect's STRICT rules: a solver advances a layer ONLY when cleanly describable in existing shared vocabulary; what it can't cleanly say is a finding fed back as spine work; NEVER force/distort the spine. **This is an ALL-PROBE cycle — NO combinator, theme, or operator entry LANDS.** The load-bearing `electrostatic-solver-probe-findings-are-single-witness-generality-unverified` caveat binds: the highest-fan-out solve-family combinator must NOT be authored from one electrostatic witness. The disciplined move is a **2nd-pipeline (magnetostatic) probe** to discharge the single-witness gate, plus two independent observation-first probes (gram-variant unification + FE-assembly thread-opening) that ride the same 2nd witness. Combinator/entry landings are sequenced to cycle-054 gated on the c053 probe verdicts.

## Codemap pre-localization (2nd-witness confirmation, verified this cycle)

The magnetostatic driver was codemap-confirmed as a near-identical structural twin of electrostatic for BOTH gated shapes (anchors embedded in the D1/D2 scopes so the producers read the cited lines and proceed to analysis, not a localization loop):

- **Outer-solve-sweep (item 1 shape):** `magnetostaticsolver.cpp` — `auto K = curlcurl_op.GetStiffnessMatrix()` assembled ONCE at `:30`; `ksp.SetOperators(*K, *K)` at `:36`; outer loop `for (const auto &[idx, data] : curlcurl_op.GetSurfaceCurrentOp())` `:67-100`; `curlcurl_op.GetExcitationVector(idx, RHS)` + `ksp.Mult(RHS, A[step])` over a family at `:76-77`; collect `std::vector<Vector> A(n_step)` (declared `:47`). Same shared-operator-capture (assembled once OUTSIDE the sweep) the electrostatic D6 finding named load-bearing.
- **Gram-reduction (item 2 shape):** `magnetostaticsolver.cpp:110-152` `PostprocessTerminals` — `mfem::DenseMatrix M(A.size())`; diagonal `Mᵢᵢ = (Aᵢᵀ K Aᵢ)/Iᵢ²` (`:124-128`); off-diagonal `Mᵢⱼ = (Aⱼᵀ K Aᵢ)/(IᵢIⱼ)` (`:130-139`) via `linalg::Dot<Vector>(comm, A_gf, H_gf)` where `H_gf = M_mag·A_gf`; in-place `Minv.Invert()` `:153`. This is the inductance-matrix analog of the electrostatic capacitance matrix — the SAME O(n²) energy-product `(family)ᴴ K (family)` shape, same per-entry `Dot(x, K·x)` kernel, same in-place inverse.
- **gram on-disk hypothesis (item 2):** `book/src/L2/gram.md` is `firm` (status `:248`); its variant axes ALREADY include a `B`-weighted hook — `gram.md:58`: "substitute a `B`-weighted hook (`inner_product_M`), giving the weighted Gram `XᴴBX`". The capacitance/inductance matrices are exactly `XᴴKX` over a solution-family basis — a strong on-disk hypothesis for D2 to test.
- **FE-assembly (item 3 shape):** `laplaceoperator.cpp:184-223` `GetStiffnessMatrix` (`BilinearForm k(GetH1Space()); k.AddDomainIntegrator<DiffusionIntegrator>(epsilon_func); k.Assemble(...)`) + `:225-253` `GetExcitationVector` (`x.ProjectBdrCoefficient(one, source_marker)` `:240`; `PtAP_K->EliminateRHS(X, RHS)` `:252`). The magnetostatic analogs are `curlcurl_op.GetStiffnessMatrix()` (`:30`, `CurlCurlIntegrator`) + `GetExcitationVector` (`:76`) — same assembly-from-integrators pattern, different integrator/FE-space, for cross-pipeline generality framing.

## Dispatches

**D1 — `cross-layer-cross-cutter`**
- **scope:** Second-pipeline solve-sweep probe (`second-pipeline-solve-sweep-probe`). Probe the MAGNETOSTATIC pipeline (`palace/drivers/magnetostaticsolver.cpp:26-108`; anchors above) to discharge the `electrostatic-solver-probe-findings-are-single-witness-generality-unverified` gate for the outer parametric solve-sweep. Confirm/refute that the **shared-operator-capture outer-solve-sweep** shape — fix operator `K` once (assembled OUTSIDE the loop, `:30`), map `ksp_solve(K, ·)` over a family of RHS vectors (`{idx}` source boundaries → `ksp.Mult(RHS, A[step])` `:77`), collect the per-member solution family `{A[step]}` — recurs identically in magnetostatic vs the electrostatic witness (`electrostaticsolver.cpp:60-89`, D6). Report: (i) is the shape the SAME (≥2 witnesses ⟹ single-witness gate dischargeable for item 1)? (ii) what is the cross-pipeline-invariant structural core vs the pipeline-specific detail (terminal-V-excitation vs surface-current-excitation; K=stiffness vs K=curl-curl)? (iii) name the candidate combinator's shape in EXISTING shared vocabulary (a `map`-over-RHS-family with shared-operator capture, distinct from `ksp_solve`'s INNER Krylov `solve_loop`) WITHOUT authoring it. **Observation-only — NO `book/` mutation, NO entry/theme lands.** The combinator mining is sequenced to c054 IF this confirms.
- **deps:** none
- **rationale:** The LEAD, highest fan-out (a confirmed solve-family sweep combinator serves all 5 pipelines). The redirect's "advance only when cleanly describable across the shared spine" bar makes cross-pipeline confirmation load-bearing BEFORE any entry lands; per the OQ caveat (`open-questions.md:775`) the combinator must NOT be authored from one witness. Serves `electrostatic-outer-terminal-sweep-needs-solve-family-combinator` (the gate, not the landing).

**D2 — `same-layer-cross-cutter`**
- **scope:** Gram-variant-axis unification probe (`capacitance-reduction-gram-variant-axis-probe`). Test the `capacitance-reduction-may-be-gram-variant-axis-extension` hypothesis IN DEPTH against the FIRM `book/src/L2/gram.md` (read it fully; its variant axes already carry a `B`-weighted hook `inner_product_M` → `XᴴBX`, `gram.md:58`). Both the electrostatic capacitance reduction (`electrostaticsolver.cpp:111-137`, in-place `Cinv.Invert()` `:139`) AND the magnetostatic inductance reduction (`magnetostaticsolver.cpp:110-152`, in-place `Minv.Invert()` `:153`) are the SAME O(n²) energy-product `(family)ᴴ K (family)` Gram shape with per-entry kernel `Dot(x_gf, K·x_gf)` (firm-structure `bilinear-form`, `book/src/L1/bilinear-form.md`, rough-in; law 8 `nrm2_M(x)²=bilinear_form(x,M,x)` is literally the diagonal `Cᵢᵢ`/`Mᵢᵢ`). Report: does the existing `gram` surface ABSORB this as a variant-axis extension (general matrix-weight `K` instead of identity/Krylov-basis; solution-family columns instead of converged-eigenpair basis), or does the family-reduction structure genuinely need a NEW operator? Distinguish the convention-invariant diagonal from the off-diagonal; check whether `gram`'s NLEPS/Krylov-orthogonalization framing cleanly generalizes. **Observation-only — NO `book/` mutation; if absorbed, the variant-axis landing is c054.**
- **deps:** none (independent surface; rides D1's 2nd witness for cross-pipeline confidence but does not require D1's report)
- **rationale:** Cheap unification probe (Medium-HIGH); a positive verdict avoids a redundant new operator and extends a firm entry. The 2nd witness (magnetostatic inductance) means D2 inherits cross-pipeline confirmation of the Gram shape "for free." Serves `capacitance-reduction-may-be-gram-variant-axis-extension`.

**D3 — `abstractor`**
- **scope:** FE-assembly-from-integrators thread-opening probe (`fe-assembly-from-integrators-probe`). Open the dedicated `fe-assembly-from-integrators-is-an-unspined-surface` thread with an OBSERVATION-FIRST probe — NOT a full harvest (LARGE scope; the sub-spine boundary must be scoped before any harvest). Probe `palace/models/laplaceoperator.cpp:184-223` (`GetStiffnessMatrix`: `BilinearForm k(GetH1Space()); k.AddDomainIntegrator<DiffusionIntegrator>(epsilon_func); k.Assemble(GetH1Spaces(), skip_zeros)`) + `:225-253` (`GetExcitationVector`: `x.ProjectBdrCoefficient(one, source_marker)` `:240`; `PtAP_K->EliminateRHS(X, RHS)` `:252`). Note the magnetostatic analogs (`curlcurl_op.GetStiffnessMatrix()` `:30` with `CurlCurlIntegrator`; `curlcurl_op.GetExcitationVector` `:76`) for cross-pipeline framing. Report: (i) scope the assembly-from-integrators sub-spine boundary (distinct from `assemble-diagonal`, which extracts `diag(A)` from an ALREADY-assembled `A` — opposite direction; and from `bilinear-form`, a matrix-weighted reduction `xᴴMy`, NOT assembly); (ii) name the candidate operator family (`assemble-from-integrators` / `excitation-vector` / `bc-elimination`) + variant axes (integrator kind, FE-space kind, quadrature); (iii) flag whether it lands as its OWN operator family (mesh/FE sub-spine, in scope per CLAUDE.md) rather than a solver-pipeline concern, and recommend the c054+ sequencing (assembly item BEFORE the BC-elimination companion). **Observation-only — NO `book/` mutation, NO operator harvest this cycle.**
- **deps:** none (independent surface)
- **rationale:** Opens the largest unspined surface incrementally (Medium fan-out, slowest to land — observation-first avoids a coarse-scope token blowup on a substantial sub-spine). The assembly surface underlies EVERY pipeline's operator construction; scoping it now feeds the c054+ harvest. Serves `fe-assembly-from-integrators-is-an-unspined-surface`.

## Deliverable-presence verification

All three dispatches are **OBSERVATION-ONLY probes that land NO named artifact** — they emit findings (OQ-ledger entries / spine-coverage verdicts), not `book/` files. Per the cycle-planner role-spec, the four-step deliverable-presence sequence applies to dispatches whose scope resolves to a named `book/src/` path; these do not. The relevant check here is the inverse: confirm the GATED candidate landings (which these probes feed) do NOT already exist on disk (no premature combinator/theme/entry), and that the findings are genuinely OPEN. Evidence pasted below.

**Candidate landing targets — confirmed ABSENT (correct; gated/unspined):**
```
$ ls book/src/L2/solve_family.md book/src/L2/solve-family.md book/src/L2/map_solve.md book/src/L4/solve_family.md
ls: cannot access 'book/src/L2/solve_family.md': No such file or directory
ls: cannot access 'book/src/L2/solve-family.md': No such file or directory
ls: cannot access 'book/src/L2/map_solve.md': No such file or directory
ls: cannot access 'book/src/L4/solve_family.md': No such file or directory
$ ls book/src/L1/assemble-stiffness.md book/src/L1/fe-assembly.md book/src/L1/excitation-vector.md book/src/L2/assemble-operator.md
(all four: No such file or directory)
$ ls book/src/L2/capacitance-reduction.md book/src/L2/inductance-matrix.md book/src/L3/gram.md
(all three: No such file or directory)
```
⟹ No solve-family combinator, FE-assembly operator, or capacitance/inductance-reduction entry exists — D1/D2/D3 correctly do NOT re-propose landed work; the landings they feed are genuinely open and are sequenced to c054 gated on the probe verdicts.

**Probe-target surfaces — confirmed FIRM / present (the probes have real referents):**
```
$ grep -m1 -n '^## Status' -A2 book/src/L2/gram.md   →  :248  `firm`.        (D2 referent)
$ grep -m1 -n '^## Status' -A2 book/src/L1/bilinear-form.md  →  :320  `rough-in (...)`  (D2 per-entry kernel referent)
```

**OQ-ledger RESOLVED-grep — confirmed all four D6 findings still OPEN (not closed/stale):**
```
$ grep -i 'single-witness.*RESOLVED|...gram-variant.*RESOLVED|...fe-assembly.*RESOLVED' scaffolding/open-questions.md
(no matches)
```
⟹ `electrostatic-outer-terminal-sweep-needs-solve-family-combinator` (`open-questions.md:772`), `capacitance-reduction-may-be-gram-variant-axis-extension` (`:773`), `fe-assembly-from-integrators-is-an-unspined-surface` (`:774`), and the gating caveat `electrostatic-solver-probe-findings-are-single-witness-generality-unverified` (`:775`) are all live, unresolved. The probes are OPEN by construction (fresh solver test-load material, no prior-cycle probe of magnetostatic — `ls -d reports/*magnetostatic*` → none).

**Structural-gate check:** D1 is the dispatch that DISCHARGES the single-witness gate (`:775`); it is the correct probe-first response to that gate, not a gate-violating premature landing. D2/D3 are unspined-surface observations with no structural block. No dispatch targets a STOP-PROPOSING NEGATIVE LIST slug (`lu_solve`, `back_solve`, `ls-update-column`, 4 NLEPS atoms; `apply_nonlinear_pencil` HELD) — these are solver-driver/FE-assembly surfaces, disjoint from the disqualified small-dense L3-backfill list.

## Overlap analysis

- **D1 × D2:** D1 reads `magnetostaticsolver.cpp:26-108` (outer-sweep structure); D2 reads `magnetostaticsolver.cpp:110-152` (`PostprocessTerminals` reduction) + `electrostaticsolver.cpp:111-137` + `book/src/L2/gram.md`. Disjoint source regions; both observation-only (no `book/` writes). The reduction (D2) is the POSTPROCESS step that consumes the solution-family the sweep (D1) produces — conceptually adjacent but separately analyzable. **NOT overlapping — PARALLEL.**
- **D1 × D3:** D1 reads the driver `magnetostaticsolver.cpp`; D3 reads the model `laplaceoperator.cpp:184-253` (+ notes the magnetostatic assembly analogs). Different files, different layers of the call graph (driver vs operator-construction). Both observation-only. **NOT overlapping — PARALLEL.**
- **D2 × D3:** D2 = the Gram reduction + `gram.md`; D3 = FE assembly + excitation-vector construction. Disjoint surfaces (terminal-postprocessing reduction vs operator/RHS assembly), both observation-only. **NOT overlapping — PARALLEL.**

No dispatch mutates `book/`; none names an operator another proposes; none writes a shared index or tally. Zero shared-artifact contention. (No count-ownership / dual-registration partition needed — this cycle lands no chapter and touches no layer index. The retired rectangular-floor machinery is correctly NOT invoked.)

## Sequencing schedule

**Single wave — all three PARALLEL (wave 1):** D1, D2, D3. All observation-only, disjoint source regions, no `book/` mutation, no forward-references between them. Per the conflict-tolerance philosophy (when in doubt, PARALLEL), and here there is no doubt — zero artifact contention.

Then the standard post-dispatch pipeline: 3 critics (parallel) → repairers as needed → `integrator-per-report` ×3 (serial) → ONE `integrator-finalize` (rebuild + commit + push + housekeeping; the probes' findings promote to the OQ ledger as spine-coverage verdicts).

## Open questions / caveats

- **This cycle deliberately lands NOTHING in `book/`.** That is the correct redirect-disciplined response to the single-witness gate (`open-questions.md:775`): the highest-fan-out combinator must not be authored from one witness, and the gram-variant / FE-assembly surfaces are observation-first by nature. The c052 cadence (D5/D6 observation-only) already established that solver-test-load probes feed the OQ ledger rather than the artifact. If the orchestrator/critic expects a per-cycle count delta, note this is an intentional probe cycle (mirrors c042 D1, c049 D3, c052 D5/D6 — observation dispatches that produce findings, not landings).
- **D1 is very likely to CONFIRM** (the codemap pre-localization already shows magnetostatic is near-byte-identical in structure to electrostatic). If it confirms, the single-witness gate is dischargeable and the solve-family combinator-miner replace-and-propagate dispatch is the c054 LEAD. I have NOT pre-authored that dispatch — the probe verdict is load-bearing and the combinator's exact shape (which layer it lands at, whether it is `solve_loop`-adjacent or a new `map_solve` vocabulary) should follow from the confirmed cross-pipeline core, not be guessed now. Flagged for the c054 planner.
- **Two-witness sufficiency question for the batch-16 meta-phase:** the redirect bar is "≥2 pipelines" before mining. D1 gives the 2nd (magnetostatic). Whether 2-of-5 is sufficient to mine, or whether driven/eigenmode/transient should also be spot-checked before propagating a combinator into all 5, is a judgment the c054 combinator-miner + batch-16 meta-phase should weigh. Magnetostatic + electrostatic are the two STRUCTURALLY-SIMPLEST/most-similar pipelines (both: assemble-K-once, loop-over-boundaries, energy-Gram-reduce); the driven (frequency-sweep) and transient (time-stepping) pipelines differ more (the operator may change per step in driven/transient, breaking the shared-operator-capture invariant). I recommend the c054 mining EXPLICITLY scope the combinator to the shared-operator-capture case and FLAG the per-step-operator-change pipelines as a possible variant axis / separate combinator — do NOT over-generalize from the two static-operator witnesses. Noted here for the batch-16 meta-phase (no friction-ledger entry yet for this; surfaced per the cadence-staleness clause).
- **D2 has a strong on-disk hypothesis but a real risk of NOT cleanly absorbing:** `gram` was built for Krylov-basis orthogonalization / NLEPS deflation; the capacitance/inductance use is a different consumer (energy reduction over a solution family with a physical scaling `1/(IᵢIⱼ)`). The `1/(IᵢIⱼ)` normalization and the `Cinv`/`Minv` in-place inverse are OUTSIDE the bare Gram — D2 should report whether those are a thin post-scaling on a `gram` core (clean variant-axis extension) or genuinely entangled (needs a new operator). Either verdict is a valid finding.
- **No ASK items for the human.** The batch-14 strategic-pivot ASK was answered by the 2026-06-01 redirect (continue the shared spine on the corrected model; solvers as low-priority test-load; no burn-pivot yet). No new architectural escalation this cycle.
