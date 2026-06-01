---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T15:57:39Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-01T16:12:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "L4 + L4>L3 coverage survey — the L4-cap / L4>L3-theme denominator"

## Critique

This is a **survey/observation** dispatch (combinator-miner coverage pre-survey for the LEAD frontier `l4-l3-coverage-and-l4-expansion`). It makes **no `book/` mutation**; its deliverable is a coverage matrix + fan-out-ranked cycle-047 pick list. The checklist is applied with the load-bearing weight on **citation-validity** and **plan-kind-consistency**, per the task framing; the rotation / variant-axis / edge-label checks largely no-op on a pure survey and are marked accordingly rather than forced.

### Checks run

**citation-validity — warning.** I verified every load-bearing anchor against disk (Read + a mechanical `tools/citecheck/citecheck.py --scan` pass, 38 citations: 36 OK on bounds/path-hygiene). The substantive verdicts all hold:
- `book/src/L4/index.md:7` ("vocabulary, not architecture"), `:32-37` (4 firm caps), `:35` ("every iterative algorithm reduces to one or more folds"), `:47` (`solve-monad` `restart_cycle`/`solve_loop` "potential cycle-009+ harvester scope, not yet anchored") — all confirmed verbatim.
- `book/src/L3/apply_linop.md:160` — the exact three-marker criterion (a) monadic effect / (b) state-stratification typing / (c) outer-driver structure + the `CONFIRMED-NOT-NEEDED` verdict — confirmed; the report's whole warrant criterion is correctly sourced here. `:142-146` ("Lowers to", no-L2-by-design) supports the `apply_linop`-parallel framing — confirmed.
- `book/src/L4/iterate-while.md:188` and `book/src/L4/iterate-while-with-prev.md:200` — both confirm the standalone theme is unauthored, the sub-component at `krylov-step-typed-wrapper-dissolution.md:156-167` is cited as dropping the trajectory, and the Law 1 / Law 2 trajectory-keeping contrast — confirmed.
- `scaffolding/open-questions.md:200` — "answered cycle-008 — verdict-(c) collapse-rule + Condition 5 applied" — confirmed verbatim; the report's R1-vs-OQ-tension reasoning is faithfully grounded.
- `book/src/L3/ksp_solve.md:78,94` (marker (c): `iterate_while_L3` fold + restart nesting), `book/src/L3/eigsolve.md:203` (no firm L4 eigsolve, opaque-library obstruction), `book/src/L3/orthogonalize.md:75,78` (no L4 entry; imagined `{residual,coeffs}` form is marginal) — all confirmed.
- File inventory: L4 dir = exactly the 4 caps + index (no `L4/{ksp_solve,eigsolve,orthogonalize}.md`); L4-L3 dir = exactly the 3 themes named; L3 dir = exactly 18 operators. The 18-row matrix is one-to-one with disk. Status counts (14 firm / 3 partial-obstruction = `chebyshev`/`eigsolve`/`orthogonalize`) confirmed. The exact `CONFIRMED-NOT-NEEDED` token IS on-disk in 9 of the leaf entries (apply_linop, axpy, axpby, axpbypcz, scal, reciprocal, normalize, elementwise_product, assemble-diagonal).

The **warning** is driven by three minor fidelity/hygiene issues (see Issues found), none of which inverts a verdict: (i) the report attributes the exact uppercase token `CONFIRMED-NOT-NEEDED` to `dot.md:135` and `nrm2.md:134`, but those lines read "no L4 entry — leaf primitives are not first-class L4 vocabulary" (the exact token is absent from `dot.md`/`nrm2.md`; substance is correct); (ii) `jacobi-smoother.md:128` is the `## Status: firm` line, not the "no L4 entry needed" verdict line (off-by-a-few anchor; the no-L4 verdict is nearby in the same entry); (iii) the report's mid-prose nuance on the trajectory "drop" inherits the L4 entries' framing without noting that the cited sub-component actually presents BOTH an unpruned (trajectory-keeping) form and a pruned form, where the pruned form drops the trajectory *by* Law 1's demand-pruning rule rather than in contradiction of it.

**surface-or-evidence — pass.** This is a pure survey/observation; it proposes no surface change to any existing operator/theme text and asserts no rotation_claim. It is explicitly an evidence/coverage-cataloguing pass ("No `book/` edits this cycle (observation pass)", line 73). The check no-ops on this report shape; marked pass as a survey, not a refinement-shaped proposal.

**rotation-quality — pass (not applicable to survey).** The report asserts no algebraic/structural/reduction rotation of its own. It *catalogues* existing rotations (the iterate-while dissolution, the krylov-step typed-wrapper dissolution) and judges whether new ones are warranted, but authors none. No L_{n+1}→L_n compaction claim to grade. Marked pass: inapplicable to an observation-kind report.

**variant-axis-coverage — pass.** No operator/theme is authored, so there are no variant axes to cover or scope out. The report does correctly *surface* a variant-axis-adjacent caveat (the `orthogonalize` MGS/CGS variant-split, line 60) as part of its MARGINAL warrant — handled as evidence, not introduced as a hidden branch. Marked pass: inapplicable to survey shape.

**cross-reference-integrity — pass.** Every `[link]`/path the survey names resolves on disk: the 4 L4 caps, 3 L4-L3 themes, 18 L3 operators, and the `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md` provenance source. No firm-chapter-body-inside-fence concern (no proposed-changes fence is emitted — observation pass). The build-readiness guard no-ops because there is no `edit:`/`new:` block. Marked pass.

**edge-label-fidelity — pass (not applicable to survey).** The report references edges (L4>L3, L3>L2, L3>L1) descriptively and consistently with the prose around each (e.g. the `iterate-while` dissolution is consistently an L4>L3 edge; `ksp_solve` carries an L4 outer-driver gap over L3). No mismatched edge-label-vs-prose instance. No edge label is *authored* as a proposal. Marked pass.

**plan-kind-consistency — pass.** Declared shape is a coverage survey + fan-out-ranked pick list; content matches exactly (matrix + per-gap warrant + ranked picks + "no book edits"). The warranted-vs-by-design reasoning is internally sound: the warrant criterion (markers a/b/c from `apply_linop.md:160`) is applied uniformly and correctly across all 20 rows — the 13 no-L4-by-design leaves genuinely carry none of the three markers; `ksp_solve`/`eigsolve` genuinely carry marker (c); the two `iterate-while*` combinator rows are genuinely firm caps with present-but-defective coverage. The fan-out ranks are internally consistent (R1 low-cost/high-leverage paired theme; R2 higher-absolute-fan-out but `solve-monad`-gated; R3 sequenced after R2 for `Outcome`-vocabulary reuse; R5 marginal-defer). The **R1-as-lifter-vs-abstractor caveat is sound and well-disclosed** (lines 96): the report correctly flags that the OQ was answered cycle-008 by a collapse-rule (which I confirmed at `open-questions.md:200` and as Condition 5 / the §3.8 collapse rule at `krylov-step-typed-wrapper-dissolution.md:188-198`), not by an authored standalone theme — so a lifter re-anchor to the collapse-rule may be the lighter correct realization, a convention call the report explicitly defers to the cycle-047 planner rather than overclaiming. The denominator caveat (lines 98) is also sound: the report correctly catches that a pure per-L3-operator survey would have missed the two L4-native loop combinators (no L3 same-named operator) and surfaces them in a separate table. Marked pass.

**skill-uptake-survey — pass.** A coverage/fan-out survey implies the `verify-citation-range` skill (which the report's citation density would have benefited from on the bare-basename pinpoints) and possibly `survey-friction-window`; the report references neither by name. This is a non-blocking telemetry surface only. The report does carry good self-disclosure of its own scope limits (the denominator caveat, the lifter-vs-abstractor caveat, the write-filter note). Marked pass as a presence-check; noting the skill-reference absence as telemetry, not a defect.

### Issues found

1. **Over-attributed exact verdict token at `dot.md:135` / `nrm2.md:134`** (CYCLE.md §Coverage matrix rows 8–9 + §Supporting evidence line 86) — **warning, citation-validity.** The report labels these rows `CONFIRMED-NOT-NEEDED` as if that exact on-disk token sits at the cited lines. On disk, `dot.md:135` and `nrm2.md:134` read "`<op>` has **no L4 entry** — leaf primitives are not first-class L4 vocabulary"; the exact uppercase `CONFIRMED-NOT-NEEDED` token does NOT appear in `dot.md` or `nrm2.md` (grep: 0 occurrences each), unlike the 9 leaf entries that DO carry it verbatim. The substance (no-L4-by-design leaf verdict) is fully correct at both anchors; only the quoted token form is imprecise. Low severity.

2. **Off-by-a-few anchor at `jacobi-smoother.md:128`** (CYCLE.md §Coverage matrix row 17 + §Supporting evidence line 86) — **warning, citation-validity.** The report cites `L3/jacobi-smoother.md:128` for "`no L4 entry needed`". Line 128 is actually the entry's `## Status: firm` line; the "no L4 entry" verdict text lives nearby in the same entry (constructed-operator gate, apply-is-one-elementwise-product). The verdict the report attributes is real and in the right file; the line number points one beat off. Low severity.

3. **Trajectory-"drop" framing inherited without the both-forms nuance** (CYCLE.md §Summary line 14, §combinator-row table line 45, §Per-gap line 54) — **warning, citation-validity (fidelity).** The report states the shared sub-component "renders the L3 form as a single `readout` **dropping the `trajectory` accumulator**" in flat contradiction of Law 1/Law 2. On disk, `krylov-step-typed-wrapper-dissolution.md` §"What the L3 form for `iterate_while` looks like" presents BOTH an **unpruned form** (`:164-171`, which KEEPS the trajectory: `readout : traj`, returns `reverse traj`) AND a **pruned form** (`:176-184`, which drops it) — and the pruned form drops the accumulator *by* the §3.8 demand-pruning rule (the explicit Law-1 image at `:188-198`), i.e. when the consumer reads only `final_state`. So the "drop" is the consumer-demand-resolved pruned form, not an unconditional contradiction of the Law. The report's framing is a faithful transcription of the L4 entries' OWN caveat wording (`iterate-while.md:188` / `iterate-while-with-prev.md:200` do assert the `:156-167` sub-component "drops the trajectory ... per Law 1"), so this is inherited-citation fidelity, not invented; but the survey would be more precise to note that the gap is "no *standalone* theme + the rendered (pruned) form is the demand-collapsed one, leaving the unpruned trajectory-keeping form un-anchored as a dedicated chapter" rather than "the theme drops the trajectory in contradiction of the Law." This nuance does NOT change the R1 warrant (a standalone theme / lifter re-anchor is still genuinely unauthored). Low severity; flagged because the load-bearing R1 pick rests on this framing.

4. **Bare-basename citation hygiene** (CYCLE.md throughout, esp. §Coverage matrix + §Supporting evidence) — **warning, citation-validity (path-hygiene).** The report cites pinpoints by bare basename (`ksp_solve.md:78`, `dot.md:135`, etc.) rather than full `book/src/L3/...` paths. `citecheck --scan` flags `ksp_solve.md:78` as `[AMBIG]` (basename matches 4 files: L1/L2/L3/concepts). The surrounding matrix context makes each contextually unambiguous (I confirmed every load-bearing one resolves to the intended L3 file), and the §Supporting evidence block does give full paths for the headline anchors, so this is hygiene not error. Low severity.

5. **Garbled/redundant status-count sentence** (CYCLE.md §Supporting evidence line 83) — **warning, plan-kind-consistency (presentational).** The sentence reads "Statuses: 14 `firm`, 3 `partial-obstruction` (`chebyshev`, `eigsolve`, `orthogonalize`), and `chebyshev` (`partial-obstruction`)." The trailing "and `chebyshev` (`partial-obstruction`)" double-counts `chebyshev`, which is already inside the 3-element partial-obstruction list. The underlying counts are correct (verified: 14 firm + 3 partial-obstruction = 18; the 3 are exactly chebyshev/eigsolve/orthogonalize); only the prose is redundant. Cosmetic.

### Note on non-applicable checks

Per role-spec, rotation-quality, variant-axis-coverage, and edge-label-fidelity are marked `pass` as **not applicable to an observation/survey-kind report** — the survey authors no rotation, no operator/theme surface, and no proposed edge label; it only catalogues and ranks existing ones. surface-or-evidence is `pass` as a pure coverage/evidence pass (explicitly no `book/` mutation). The two load-bearing checks the task names — citation-validity and plan-kind-consistency — received the full mechanical + hand verification; citation-validity lands `warning` on the five minor fidelity/hygiene items above (no verdict-inverting defect), and plan-kind-consistency lands `pass` (the warranted-vs-by-design reasoning, fan-out ranks, and R1 lifter-vs-abstractor caveat are all sound).

## Repair

All five critic findings were mechanical/surgical citation-fidelity and presentational fixes confined to CYCLE.md prose (this is an observation-only survey; no `book/` mutation). None inverted a verdict; the survey's substantive conclusions (the warrant criterion, the no-L4-by-design closure of rows 6–18, the R1/R2/R3/R5 fan-out ranking) are untouched and stand.

### Fixes attempted

- **Finding 1 — over-attributed `CONFIRMED-NOT-NEEDED` token at `dot.md:135` / `nrm2.md:134`** (citation-validity).
  - **Decision**: repaired.
  - **Action**: Verified on disk — both lines read "has **no L4 entry** — leaf primitives are not first-class L4 vocabulary"; the literal uppercase token is absent. Rewrote matrix rows 8–9 (§Coverage matrix) to cite `no L4 entry` (leaf-primitive verdict) with full `book/src/L3/...` paths, and rewrote the §Supporting evidence verdict line to distinguish the 9 entries that DO carry the verbatim token from the rows (`dot`/`nrm2`/`jacobi-smoother`/`divfree-projector`) carrying the equivalent prose / lowercase form. Substance (no-L4-by-design leaf verdict) was already correct.

- **Finding 2 — off-by-a-few anchor at `jacobi-smoother.md:128`** (citation-validity).
  - **Decision**: not-needed.
  - **Rationale**: On-disk verification shows line 128 is the `## Status` paragraph whose final clause literally ends "…opaque-operator gate, operator-representation absorbed, **no L4 entry needed**." The report's quoted verdict `no L4 entry needed` at `L3/jacobi-smoother.md:128` is therefore an exact on-disk match, not off-by-a-few. No edit applied (the critic's off-by-a-few read does not hold against disk; the citation is accurate). The §Supporting-evidence rewrite (Finding 1) restates this anchor with the correct phrase for clarity.

- **Finding 3 — trajectory-"drop" framing inherited without the both-forms nuance** (citation-validity / fidelity).
  - **Decision**: repaired.
  - **Action**: Verified `krylov-step-typed-wrapper-dissolution.md` presents BOTH an unpruned trajectory-keeping form (`:164-171`, returns `reverse traj`) AND a pruned form (`:176-184`), with the pruned form dropping the accumulator *by* the §3.8 demand-pruning rule (the L3-side image of Law 1, `:188-198`) when only `final_state` is observed — not in contradiction of the Law. Reworded all four occurrences (§Summary, §combinator-row table, §Per-gap, §Supporting evidence) so the gap is stated as "no *standalone* L4>L3 theme + the trajectory-keeping unpruned form is left un-anchored as a dedicated chapter," and corrected the cited range `156-167` → `156-198` (the span covering both forms + the collapse rule). The **R1 recommendation is unchanged** — a standalone theme / lifter re-anchor is still genuinely unauthored, exactly as the survey ranked it.

- **Finding 4 — bare-basename citation hygiene (`ksp_solve.md:78` AMBIG)** (citation-validity / path-hygiene).
  - **Decision**: repaired.
  - **Action**: Expanded the load-bearing pinpoints in §Coverage-matrix rows 3–5 and the §Per-gap paragraphs from bare basenames to full `book/src/L3/...` / `book/src/L4/...` paths (`ksp_solve.md:78,94`, `eigsolve.md:203`, `orthogonalize.md:75,78`, `index.md:47`), removing the `citecheck --scan` `[AMBIG]` 4-file basename collisions. Each was confirmed to resolve to the intended L3/L4 file.

- **Finding 5 — garbled/redundant status-count sentence (line 83 double-counts `chebyshev`)** (plan-kind-consistency / presentational).
  - **Decision**: repaired.
  - **Action**: Rewrote §Supporting-evidence line to "14 `firm` + 3 `partial-obstruction` (`chebyshev`, `eigsolve`, `orthogonalize`) = 18", dropping the redundant trailing "and `chebyshev` (`partial-obstruction`)" clause. Underlying counts were already correct.

### Unrepairable findings

None. All five findings were within repair authority (citation-fidelity re-wording / path-hygiene / count fix); no substantive re-authoring was required, and the R1 framing repair preserved the survey's recommendation without changing its content judgment.

## Suggested resolution

`ready`. The five warnings were all minor fidelity/hygiene/presentational items, now mechanically repaired in CYCLE.md; no verdict was inverted and the survey's substantive output (warrant criterion, no-L4-by-design closure of the 13-leaf cohort, the R1/R2/R3/R5 ranked pick list, the lifter-vs-abstractor and `solve-monad`-dependency caveats) is sound per the critic and unchanged. Notes for the integrator: this is an observation-only survey with **no `book/` proposed-changes block** — its product is the coverage matrix + ranked cycle-047 pick list, which the cycle-planner migrates into `scaffolding/priorities.md` (planner action, not integrator). When cycle-047's abstractor authors the R1 standalone `iterate-while-dissolution` / `iterate-while-with-prev-dissolution` themes, the corrected framing (pruned form drops the trajectory BY §3.8 demand-pruning; the gap is the missing standalone theme + the un-anchored unpruned trajectory-keeping form) is the accurate starting point.
