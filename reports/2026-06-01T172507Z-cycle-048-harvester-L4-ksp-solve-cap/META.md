---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T180000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-01T183000Z
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

# META: verification of "Formalize ksp_solve at L4 (outer-driver cap)" (cycle-048 R2)

## Critique

### Checks run

**citation-validity — pass.** Every L0 anchor the report claims codemap-verified was spot-checked via palace-codemap `read_range` and confirmed in-range and on-point:
- `iterative.cpp:417-418` — disk shows `eps = std::max(rel_tol * initial_res, abs_tol)` at :417 and `converged = (res < eps)` at :418 (the eps + pre-loop converged short-circuit). Correct.
- `iterative.cpp:427` — `for (; it < max_it && !converged; it++)` (CG outer-driver loop). Correct.
- `iterative.cpp:484-485` — `final_res = res; final_it = it;` (CG terminal readout). Correct.
- `iterative.cpp:563` — `for (; it < max_it; restart++)` (GMRES restart outer loop). Correct.
- `iterative.cpp:703-704` — `final_res = beta; final_it = it;` (GMRES terminal readout). Correct.
- `iterative.hpp:52-55` — the four mutable result fields `converged` / `initial_res, final_res` / `final_it`. Correct.
- `iterative.hpp:98` — `GetConverged()` with the `rel_tol > 0.0 || abs_tol > 0.0` gate. Correct.
- `iterative.hpp:101-108` — `GetInitialRes` / `GetFinalRes` / `GetNumIterations` accessors. Correct.
- `ksp.cpp:296-310` — `BaseKspSolver::Mult`; the soft-fail `Mpi::Warning` + return-regardless is at :301-307, counters `ksp_mult++`/`ksp_mult_it +=` at :308-309. Correct; the report's `:301-307` soft-fail sub-anchor and `:308-309` counter sub-anchor are both precise.
Concept-page anchors verified: `concepts/solve-monad.md` §Shape (:5-17), §"Worked example — GMRES" (:47-56), §"Termination as a sum type" (:58-68) — all in-range (file ends :69) and content matches (the `Outcome = Continue | Done Bool` classify-once / fold-uniformly law is verbatim at :58-68). Strawman anchors verified: §3.3 monad laws at :123-125, §3.4 state-effect `modify (f∘g) → do {modify g; modify f}` at :134, §3.7 `iterate_while_pure` sugar at :178-182 — all in-range (file is 473 lines) and the cited content is exactly what Laws 2 and 3 lean on. The firm L3 parent `book/src/L3/ksp_solve.md` (firm), L1 parent `book/src/L1/ksp_solve.md` (firm), and the c047 `book/src/L4/index.md` `solve_loop`/`restart_cycle`/`Outcome` rows (:66-68, all firm) all exist as claimed. No `verified_against:` YAML block present (not a lowering-verifier audit), so that sub-check no-ops.

**surface-or-evidence — pass.** This is a NEW firm L4 operator cap (an addition, not a refinement of an existing operator/theme), so the refinement-surface-plus-rotation-claim rule applies only to the bundled `edit:` re-anchors. Those three `L3/ksp_solve.md` edits are pure live-link upgrades of existing forward-references (concept-page-only → cite the now-firm L4 cap) — surface modifications backed by the now-on-disk target, the allowed retroactive-evidence/upgrade shape, not bare rotation_claims. The cap entry itself carries its evidence base (L3/L1/L4-kernel pages + solve-monad concept + strawman + transitive L0). Pass.

**rotation-quality — pass (not a rotation claim).** Per the dispatch shape this is an L4 vocabulary cap, not an L_{n+1}>L_n rotation; the L4>L3 rotation is explicitly scoped out to D3's theme. The cap is correctly defined in L4 vocabulary (the `Solve` monad, the `solve-monad` outer-driver surface, the `iterate-while` family) and does NOT define its semantics in L3 value-threading primitives — the high→low discipline holds (§Context, §Signature, §Semantics all stay in `Solve`/`SimState`/`Outcome` terms; the L3 positional-`(K,s)` collapse appears only in the §"Lowers to" rotation-direction note, which is the licensed in-line forward narration). The five laws are sound L4-level claims (the `execState`/`StateT` discharge fusion, `solve_loop`-as-`iterate_while_pure` fold equivalence, monad-law normal form, terminal operator-inverse, `Outcome` classify-once) and each is anchored to a verified strawman/concept rule. Pass.

**variant-axis-coverage — pass.** The cap declares four coordination-shaping axes (outcome-classification 3-arm `Outcome`, restart-shape, element-type, convergence-failure-policy) and explicitly distinguishes them from `krylov-step`'s six body-variant axes, with the one shared axis (restart-shape) reconciled (kernel restart-agnostic, cap restart-owning). The `Outcome` 3-arm axis (`Done True` / `Done False` / `Continue`) is fully enumerated against `(K.beta, K.j, SimState.it, ε)` and matches the firm c047 `Outcome` row + the solve-monad concept. No hidden branch. Pass.

**cross-reference-integrity — warning.** Build-readiness fence-parity verified mechanically: 14 triple-backtick lines = 7 balanced pairs (matching the report's claim), with the `new:book/src/L4/ksp_solve.md` block spanning lines 36-225 and ENCLOSING the full firm apparatus inside the fence — `## Algebraic laws` (130), `## Status` (194), `## Evidence` (203) are all within 36-225; inner code uses 4-space indentation (no nested triple-backtick fences), so no fence-truncation defect. All `[link]` targets resolve on disk: the seven concept pages, the two L4 siblings (`krylov-step`, `iterate-while`), the L3/L1 parents. The three `L3/ksp_solve.md` `edit:` old-strings match disk exactly (:78 "No `Solve` monad" bullet, :142 solve-monad dependency bullet, :160 convergence-failure-policy axis). SUMMARY insert old-string `- [chebyshev](./L4/chebyshev.md)` matches disk line 11; the new `ksp_solve` line lands at 12 before the `# L4 > L3` header — surgically correct. Both L4/index `edit:` old-strings match disk exactly (the chebyshev §Vocabulary-cohort bullet at :37; the `Outcome` dep-map row at :68). D1 correctly DEFERS the count tally and Queued prose — grep confirms the report does NOT touch the `(4 + 3 outer-driver)` token (~:32) or the §Queued-at-L4 prose (:53-58); those are explicitly handed to D4. **The warning is the slug mismatch — see Issue 1.**

**edge-label-fidelity — pass.** The L4/index dep-map row's "Lowers to" cell points L4→L3 (`L3/ksp_solve` via the dissolution theme) and the prose discusses exactly that edge. The three L3/ksp_solve re-anchor edges correctly cite the now-firm L4 cap as the upward home (L4←L3 reference direction), and the live-link upgrade prose at each site discusses the same edge. No edge-label/prose mismatch. (The slug-name defect under Issue 1 is a slug-reconciliation problem, not an edge-direction/label-fidelity problem — the edge endpoints are correct.)

**plan-kind-consistency — pass.** Declared kind is a firm L4 operator cap; content shape matches — full Signature/Semantics/Algebraic-laws (5 + 7 non-laws)/Dependencies/Variant-axes/Status/Evidence, no rough-in placeholders, `firmness: firm` frontmatter. The firm maturity is justified: the cap is fully determined from the firm c047 solve-monad vocabulary + the firm L3 parent + the firm L4 kernel/iterate-while siblings, with no constructed sub-part requiring a `partly-constructive` qualifier and no test-gate on the (syntactic-identity / inherited-fixed-point) laws. Appropriately firm.

**skill-uptake-survey — pass.** The report's shape implies two skills, both referenced: the live-link upgrade invokes `upgrade-plain-text-ref-to-live-link-when-target-on-disk` (named at §Supporting evidence line 271), and the SUMMARY insertion follows the `summary-md-surgical-insert` shape (named at §Registration line 32). The proposed-changes-fence-encloses-full-body guard was effectively self-applied (the report pre-declares "7 balanced pairs, full body inside fence" and "inner code as 4-space-indented blocks (no nested fences)"). Telemetry surfaced; non-blocking.

### Issues found

**Issue 1 (cross-report slug mismatch — for integrator reconciliation; severity: medium, build-relevant). `CYCLE.md` frontmatter + §Context + §"Lowers to" + §Status + L4/index dep-map `edit:` row + §Open-questions — 6 sites.** D1's cap references the pending L4>L3 theme as `ksp-solve-outer-driver-dissolution`, but D3 (this same cycle) landed the theme as `ksp-solve-driver-dissolution`. The wrong slug appears at **6 sites**:
- line 45 — frontmatter `lowers_to:` (`theme L4-L3/ksp-solve-outer-driver-dissolution pending`)
- line 66 — §Context prose (`a separate L4>L3 theme (\`L4-L3/ksp-solve-outer-driver-dissolution\`, D3's dispatch this cycle)`)
- line 181 — §"Lowers to" prose (`via the L4>L3 dissolution theme \`L4-L3/ksp-solve-outer-driver-dissolution\``)
- line 196 — §Status prose (`The L4>L3 dissolution theme (\`L4-L3/ksp-solve-outer-driver-dissolution\`) is D3's dispatch`)
- line 246 — **the `edit:book/src/L4/index.md` dep-map row** (`via the **substantive** ... dissolution \`L4-L3/ksp-solve-outer-driver-dissolution\``) — this is the one that lands in the artifact, so it is build-relevant
- line 275 — §Open-questions caveat (`**\`L4-L3/ksp-solve-outer-driver-dissolution\` is D3's dispatch this cycle**`)

None of these are live `[link]`s (they are plain-text slug references, consistent with the theme not being on disk yet — neither `ksp-solve-outer-driver-dissolution` nor `ksp-solve-driver-dissolution` exists under `book/src/L4-L3/`), so there is no immediate linkcheck2 break; but they will read as a dangling/inconsistent slug once D3's `ksp-solve-driver-dissolution` lands. The report itself anticipates the reconciliation generically at line 275 ("if D3's dispatch lands a different slug, the integrator should reconcile the in-line reference") — but it does not know the landed slug, so the integrator must re-wire all 6 sites (especially the artifact-bound L4/index row at line 246) to `ksp-solve-driver-dissolution`. Flag for integrator reconciliation.

**Issue 2 (minor — citation precision; severity: low). `CYCLE.md` frontmatter line 13.** The `inputs:` frontmatter L0-anchor list includes a trailing `ksp.cpp:296-310,301-307` (the `,301-307` sub-range appended), whereas the §Evidence body (line 223) and §Supporting evidence (line 268) cite `ksp.cpp:296-310` with `:301-307` correctly described as the soft-fail sub-line WITHIN that range. The frontmatter's compressed `296-310,301-307` is not wrong (both ranges verify on disk) but is redundant/slightly malformed as a citation token (the second range is a subset of the first). Cosmetic; does not affect any artifact-bound text.

**Note (not an issue): the live-link upgrade premise is sound.** Verified that `book/src/L3/ksp_solve.md` carries NO "no L4 cap exists" / "forthcoming L4/ksp_solve" false assertion (grep returned zero such hits), confirming the report's claim that the three re-anchors are pure plain-text→live-link upgrades, not stale-assertion corrections. The L3 status correctly stays `firm` (unchanged). `book/src/L4/ksp_solve.md` is confirmed absent on disk (a genuine create, not an overwrite).

---

## Repair

### Fixes attempted

- **Finding (Issue 1, cross-reference-integrity — slug mismatch, medium/build-relevant)**: D1's cap referenced the pending L4>L3 dissolution theme as `ksp-solve-outer-driver-dissolution` at 6 sites, but D3 (same cycle) landed the canonical slug `ksp-solve-driver-dissolution` (matching the cycle-048 plan's D3 scope `book/src/L4-L3/ksp-solve-driver-dissolution.md`).
  - **Decision**: repaired.
  - **Action**: Global replace `ksp-solve-outer-driver-dissolution` → `ksp-solve-driver-dissolution` in `CYCLE.md`, re-wiring all 6 sites — frontmatter `lowers_to:` (L45), §Context prose (L66), §"Lowers to" prose (L181), §Status prose (L196), the **artifact-bound `edit:book/src/L4/index.md` dep-map row** (L246, the build-relevant one), and the §Open-questions caveat (L275). Post-edit re-grep confirms zero `ksp-solve-outer-driver-dissolution` remain; all 6 now read the canonical slug. The §Open-questions caveat (L275) was additionally updated from the generic "if D3 lands a different slug, integrator should reconcile" hedge to a resolved note recording that the reconciliation was performed at repair (canonical slug `ksp-solve-driver-dissolution`, no further integrator action needed). Purely mechanical slug reconciliation against the cycle-mate's landed canonical slug — no content authored; edge endpoints/direction were already correct (the critic confirmed edge-label-fidelity pass), so this is a slug-name fix only.

- **Finding (Issue 2, citation-validity — citation precision, low/cosmetic)**: frontmatter (L13) carried a redundant `ksp.cpp:296-310,301-307` token (the `:301-307` sub-range is a subset of `:296-310`).
  - **Decision**: repaired.
  - **Action**: Dropped the redundant subset → `ksp.cpp:296-310` in the L13 `inputs:` L0-anchor list. The §Evidence (L223) and §Supporting evidence (L268) bodies already cite `296-310` with `301-307` correctly described as the soft-fail sub-line *within* that range; those clean citations were left untouched. Mechanical de-duplication of an overlapping range token; no claim changed.

### Unrepairable findings

None. Both flagged findings were mechanical (cross-report slug reconciliation against a known-canonical landed slug; redundant-subset citation-token tidy). The critic's remaining 7 checks all passed and required no action.

## Suggested resolution

`ready`. Content is sound (7 critic passes; the L0 anchors codemap-verified, fence-parity clean with full body inside the `new:` fence, the 3 L3 re-anchor old-strings match disk, the live-link-upgrade premise verified). The two repairs were both mechanical and neither was verdict-inverting. Integrator notes:
- The L4>L3 dissolution slug is now `ksp-solve-driver-dissolution` at all 6 sites — consistent with D3's landed theme; no cross-report reconciliation remains for the integrator to perform on this report.
- D1 correctly defers the §Vocabulary-cohort count tally (`(4 + 3 outer-driver)` token ~L32 in `L4/index.md`) and the §Queued-at-L4 prose flip to D4 (the count-owner). The integrator should ensure D4's dispatch is applied for those, as D1 deliberately does not touch them.
