---
agent: cross-layer-cross-cutter
invoked_at: 2026-06-03T041103Z
integrated_at: 2026-06-03T044543Z
integration_commit: f5a405c
integration_notes: "cycle-074 D6 (LOW observation; OBSERVATION-ONLY cross-layer finding). Applied clean — single in-place §Specialization paragraph REPLACE in L4/gram_reduce.md recording the gram_reduce 3rd-witness probe CLOSED-NEGATIVE: eigenmode Q-factor (per-mode scalar-ratio map, wrong rank) + driven S-parameters (per-column port-mode linear projection with a decisive multi-pronged symmetry break) both NON-MATCH. gram_reduce stays the 2-pipeline energy-output-product reduction; future S-param/eigenfreq+Q output-product columns routed to author their OWN reduction verbs (sparameter_reduce port-projection map; eigenfreq/Q per-mode scalar-ratio map), NO gram_reduce broadening. Over-unification hazard cleared; subsume correctly REFUSED. No status change on gram_reduce. CLOSED-NEGATIVE discharge of OQ gram-reduce-third-witness-probe-eigenmode-driven-postprocess (note already on disk). citecheck 17 ok/0 fail. retroactive 0. cargo make book exit 0."
scope: L4 cross-cut — gram_reduce 3rd-witness probe (eigenmode + driven postprocess) with over-unification hazard as load-bearing guard
status: pending
---

# CYCLE: Cross-layer observation — gram_reduce has NO clean 3rd witness (both candidates non-match; over-unification hazard cleared)

## Summary

I probed whether the L4 `gram_reduce` operator-weighted symmetric-Gram reduction
(`book/src/L4/gram_reduce.md`; currently 2-witness: electrostatic capacitance `w=1`,
magnetostatic inductance `w=1/(IᵢIⱼ)`) has a clean 3rd witness in (a) eigenmode
Q-factor / eigenfrequency energy post-processing or (b) driven S-parameter port-overlap
reductions. Running the `disciplined-cross-pipeline-combinator-mining-gate`
single-witness → probe → discharge sequence and applying its **step-1 positive-shape
check FIRST** (does the symmetric operator-weighted family-PAIR bilinear shape
`Gᵢⱼ = w(i,j)·xⱼᵀ K xᵢ` POSITIVELY hold?), **both candidates are NON-MATCHES**. The
over-unification hazard flagged in OQ `gram-reduce-third-witness-probe-eigenmode-driven-postprocess`
("S-parameters are NOT symmetric-Gram in general") is **confirmed and cleared**: not
only is the S-matrix not symmetric-Gram, the eigenmode post-processing isn't a Gram
reduction at all (it's a per-mode scalar-ratio map). This is a **spine-boundary finding**,
not a coverage gap — `gram_reduce` stays 2-pipeline by-design.

## Observation kind

**Consistency drift / vocabulary boundary (spine finding)** — a probed cross-pipeline
generalization of an existing L4 combinator (`gram_reduce` broadening from 2 witnesses
to 3+) is REFUTED on positive-shape grounds. The redirect's "what a solver can't
cleanly say is a finding about the spine" routing applies: the eigenmode and driven
output-product reductions are **structurally distinct reduction verbs**, not
`gram_reduce` specializations. (NOT a coverage gap — `gram_reduce` is correctly scoped
at 2 witnesses; NOT an edge-label mismatch; NOT audit residue.)

## Specific finding

**The load-bearing structural shape under test** (`book/src/L4/gram_reduce.md:75-115`):
a symmetric operator-weighted bilinear `Gᵢⱼ = w(i,j)·(xⱼᵀ K xᵢ)` evaluated over the
**upper-triangle of a solution-family PAIR grid** `[i][j]`, then mirrored
(`symmetric_from_upper`), with `K` symmetric/SPD and `w(i,j)=w(j,i)`. The two firm
witnesses fold L1 `bilinear-form` (off-diagonal `xⱼᵀ K xᵢ`) and `matrix-weighted-norm`
(diagonal `xᵢᵀ K xᵢ`) over the grid.

### Candidate (a) — eigenmode Q-factor / eigenfrequency energy: NON-MATCH (wrong shape — per-mode scalar-ratio MAP, no family-pair grid)

- The eigenmode post-processing loop `eigensolver.cpp:424-471` is a **per-mode MAP**
  (`for (int i = 0; i < num_conv; i++)`), each iteration reading exactly ONE eigenpair
  `(ωᵢ, Eᵢ)` independently (`GetEigenvalue(i)` `:427`, `GetEigenvector(i, E)` `:443`).
- The Q-factor `postoperator.cpp:1188-1191` is `Q_mj = ω_m / |κ_mj|` — a **per-mode,
  per-port SCALAR RATIO**. The coupling rate `κ_mj = ½ R_j I_mj² / E_m`
  (`:1183-1191`, `MeasureLumpedPortsEig`) is a per-mode **self-energy quotient**
  (mode-`m` resistor power over mode-`m` total energy), and the energy-participation
  ratio `p_mj = ½ L_j I_mj² / E_m` (`:1210-1217`) is likewise per-mode self-referential.
- **There is no family-PAIR grid.** No cross-mode `Eⱼᵀ K Eᵢ` term exists anywhere in
  the eigenmode post-processing — modes are never reduced against each other. The shape
  is a per-element map of scalar ratios (the `inner_product`-family scalar-reduce per
  mode), the **wrong rank** for `gram_reduce` (which is the reduce-to-MATRIX combinator
  over pairs).
- The complex element-type axis (flagged in the OQ as the anticipated wrinkle) is
  **moot** — the shape never reaches a Gram matrix to which a complex element type would
  apply; the non-match is at the grid/rank level, upstream of element-type.

### Candidate (b) — driven S-parameters: NON-MATCH (port-mode LINEAR projection, one-column-per-solve, decisive multi-pronged symmetry break)

- `Sᵢⱼ = GetSParameter(E)` is a **port-mode LINEAR PROJECTION** of the solved field `E`
  onto port `i`'s mode linear-form `sᵢ`: `LumpedPortData::GetSParameter`
  (`lumpedportoperator.cpp:283-294`) computes `dot = (*s) · E` — a single-vector linear
  functional (linear form `s` applied to one field `E`), NOT an operator-weighted
  bilinear `xⱼᵀ K xᵢ` of two solution-family members. Wave-port form is structurally
  the same (`postoperator.cpp:1239` `vi.S = data.GetSParameter(*E)`).
- The S-matrix is assembled **one drive-column at a time** (`MeasureSParameter`,
  `postoperator.cpp:1246-1308`): the column index is `drive_port_idx`
  (`measurement_cache.ex_idx`, `:1263`) — the single excited port of THIS solve. Each
  driven solve produces ONE column `S[·][drive]`; there is no upper-triangle family-PAIR
  map within a single reduction. (This is the same one-excitation-per-solve structure
  that, at the solve stage, is the `solve_family` / per-excitation map — the reduction
  rides one column of it, not a pair grid.)
- **The symmetry break is decisive and multi-pronged** (confirming "S-parameters NOT
  symmetric-Gram in general"):
  1. **Inhomogeneous diagonal self-term:** `if (idx == drive_port_idx) vi.S.real() -= 1.0`
     (`:1275` lumped, `:1297` wave) subtracts the incident wave on the diagonal — an
     inhomogeneous self-correction with NO analog in the homogeneous Gram diagonal
     `xᵢᵀ K xᵢ`.
  2. **Directional generalized-S scaling:** `vi.S *= std::sqrt(src_data.R / data.R)`
     (`:1280`) scales by the **directional** ratio `√(R_drive/R_idx)` — `src≠dst`
     asymmetric, not a symmetric `w(i,j)=w(j,i)` weight.
  3. **Per-endpoint distinct de-embedding phase:** wave ports apply
     `exp(i·k_n,src·d_src)` AND `exp(i·k_n,idx·d_idx)` as **two separately-computed
     per-endpoint factors** (`:1301-1302`), not a symmetric `w(i,j)`.
  4. **Complex, no mirror construction:** `vi.S` is `std::complex<double>` and Palace
     **computes every entry directly** (all rows for the one column, all columns across
     solves) — there is NO `symmetric_from_upper` mirror. S-matrix symmetry `Sᵢⱼ=Sⱼᵢ`
     when it holds is a *reciprocity physical property* of the system, NOT a
     compute-upper-then-mirror construction. `gram_reduce`'s load-bearing law-1
     (symmetry-by-construction, `gram_reduce.md:136-140`) is exactly what S-parameters
     do NOT have.

### Gate disposition (`disciplined-cross-pipeline-combinator-mining-gate`)

- **Step 1 (≥2 positive structurally-identical witnesses):** the existing 2 (electro/magneto)
  hold; **neither candidate adds a 3rd** — both fail the positive-shape precondition
  (a is the wrong rank; b is a linear projection, not a bilinear, with an asymmetric
  inhomogeneous assembly).
- **Step 2 (classify break-witnesses as scope boundaries, never variant axes):** both
  candidates are **SCOPE BOUNDARIES / distinct reductions**, NOT variant axes of
  `gram_reduce`. Folding either into a `w`-closure variant axis would assert a
  symmetric-Gram generality the source contradicts (the over-unification failure the
  gate forbids).
- **Step 3 (fold-vs-map flag on deferred shapes):** both are MAPs (per-mode / per-column
  independent), so no fold-into-map hazard — but the map elements are the *wrong shape*
  (scalar ratio / linear projection), so map-ness doesn't rescue the subsume.
- **Step 4 (replace-and-propagate):** N/A — no broadening is licensed; nothing to propagate.

## Recommendation

**Defer (record the boundary) — NO `gram_reduce` broadening, NO combinator-miner/harvester
follow-up for a `gram_reduce` generalization.** Specifically:

- `gram_reduce` stays a **2-pipeline** energy-output-product reduction
  (electrostatic + magnetostatic). Its §Specialization "Candidate 3rd+ witnesses"
  paragraph (`gram_reduce.md:178-182`) is now **resolved NEGATIVE** — see proposed-changes
  block below for an optional one-line in-place note recording the discharge (a future
  integrator MAY apply it; the substantive finding lives in this report + the OQ ledger).
- **CONFIRMS the by-design forward-refs** in the two deferred output-product columns:
  - `eigenfrequency-qfactor-output-product-column-and-seed-promotion` (c073 D4) — when
    authored, this column should mine its OWN reduction verb (a **per-mode scalar-ratio
    map**: `Q = ω/κ`, `κ = ½RI²/E`, energy-participation `p = ½LI²/E`), NOT a
    `gram_reduce` specialization.
  - `driven-sparameter-output-product-column-and-seed-promotion` (c073 D2) — when
    authored, `sparameter_reduce` should be its OWN verb (a **per-column port-mode
    linear-projection** with inhomogeneous diagonal self-term subtraction + directional
    generalized-S scaling + per-endpoint de-embedding), NOT a `gram_reduce`
    specialization.
  Those two reduction verbs are **separate future mining targets** for the
  combinator-miner WHEN those columns land — flagged here for the planner, but NOT
  dispatched now and NOT as `gram_reduce` broadening.

## Proposed-changes (OPTIONAL — for integrator-per-report Phase 5 if applied; not load-bearing)

The substantive output of this dispatch is the OQ discharge (already appended,
append-only) + this report. An optional in-place clarification to the `gram_reduce`
§Specialization candidate-witness paragraph records the negative result so a future
reader does not re-probe:

```text
FILE: book/src/L4/gram_reduce.md
REPLACE:
Candidate 3rd+ witnesses (NOT authored — a stronger future mine): eigenmode Q-factor /
eigenfrequency energy post-processing (likely a per-mode map, would introduce the
complex element-type axis) and driven S-parameter post-processing (port-pair map,
possibly a *different* reduction — S-parameters are not symmetric Gram in general, an
over-unification hazard to probe before subsuming). See the L4 index Open questions.
WITH:
Candidate 3rd+ witnesses — PROBED c074 D6, both NON-MATCH (the symmetric-Gram subsume
is correctly REFUSED): (i) eigenmode Q-factor / energy post-processing is a per-mode
SCALAR-RATIO map (`Q_mj = ω_m/κ_mj`, `κ_mj = ½R_jI_mj²/E_m`,
`eigensolver.cpp:424-471` + `postoperator.cpp:1174-1217`) — no family-PAIR grid, the
wrong rank for a Gram reduction; (ii) driven S-parameters are a per-column port-mode
LINEAR PROJECTION (`Sᵢⱼ = sᵢ·E`, `lumpedportoperator.cpp:283-294`) assembled one
drive-column per solve with an inhomogeneous diagonal self-term (`-1`), directional
generalized-S scaling, and per-endpoint de-embedding (`postoperator.cpp:1246-1308`) —
NOT symmetric-Gram (no `symmetric_from_upper`; S-symmetry is reciprocity physics, not a
construction). `gram_reduce` stays the 2-pipeline energy-output-product reduction; the
eigenfreq/Q and S-parameter output-product columns author their OWN reduction verbs.
See OQ `gram-reduce-third-witness-probe-eigenmode-driven-postprocess` (CLOSED-NEGATIVE).
```

## Supporting evidence

All L0 citations codemap-verified this dispatch (`mcp__palace-codemap__read_range` /
`search_text`).

- **`gram_reduce` shape under test:** `book/src/L4/gram_reduce.md:75-115` (signature +
  shape contract — the family-PAIR grid + `symmetric_from_upper`), `:136-140` (law-1
  symmetry-by-construction, the load-bearing precondition), `:178-182` (the candidate-
  witness paragraph this probe resolves), `:243-247` (§Status "Scope: 2-of-N").
- **Candidate (a) eigenmode — NON-MATCH:** `palace/drivers/eigensolver.cpp:424` (per-mode
  `for i in num_conv` loop head), `:427` (`GetEigenvalue(i)`), `:443`
  (`GetEigenvector(i, E)` — one eigenpair per iter), `:459` (`MeasureAndPrintAll(i, ...)`);
  `palace/models/postoperator.cpp:1174-1191` (`MeasureLumpedPortsEig`: `κ_mj = ½RI²/E_m`,
  `Q_mj = ω_m/|κ_mj|` — per-mode scalar ratio), `:1210-1217` (per-mode energy-participation
  `p_mj = ½LI²/E_m`).
- **Candidate (b) driven S-parameters — NON-MATCH:** `palace/models/lumpedportoperator.cpp:283-294`
  (`GetSParameter`: `dot = (*s)·E` — linear projection of one field onto one port mode);
  `palace/models/postoperator.cpp:1141` + `:1239` (`vi.S = data.GetSParameter(*E)` lumped/wave),
  `:1246-1308` (`MeasureSParameter` — one-drive-column assembly): `:1263`
  (`drive_port_idx = measurement_cache.ex_idx`, single excited port per solve), `:1275`/`:1297`
  (diagonal `vi.S.real() -= 1.0` inhomogeneous self-term), `:1280` (`S *= √(R_src/R_dst)`
  directional scaling), `:1301-1302` (per-endpoint de-embedding phase). Wave-port S-form
  decl `palace/models/waveportoperator.hpp:146`.
- **Tests confirming the linear-projection shape:** `test/unit/test-lumpedportintegration.cpp:364-367`
  + `:717-720` ("SParameter Linear form should be the field form e_t / eta" —
  `GetSParameter(gridfunction)` is a linear-form application, semantic doc that it is a
  projection not a bilinear).
- **Gate skill:** `skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md`
  (step-1 positive-shape precondition + step-2 break-witness-as-scope-boundary applied).
- **OQ context:** `scaffolding/open-questions.md:930`
  (`gram-reduce-third-witness-probe-eigenmode-driven-postprocess`, c073 D1 — the probe
  this dispatch discharges NEGATIVE), `:932` (`driven-sparameter-output-product-column...`,
  c073 D2), and the c073 D4 `eigenfrequency-qfactor-output-product-column...` entry — the
  two deferred output-product columns whose by-design forward-refs this finding confirms.

## Open questions / caveats

- **Scope-discipline check (the point of the probe):** the discharge does NOT license an
  over-broad subsume. I explicitly did NOT broaden `gram_reduce` and did NOT fold either
  candidate into a `w`-closure variant axis (gate step-2 violation avoided). The finding
  is that the two candidates are **separate reduction verbs**, not `gram_reduce` cases.
- The eigenmode and driven reductions ARE mineable on their own terms (each has the
  cross-pipeline-witness question internal to it — e.g. is the per-mode scalar-ratio map
  shared with another pipeline?), but that is a DIFFERENT mine, to be run WHEN those
  output-product columns are authored. Not in scope here; flagged for the planner.
- I did not read the wave-port `GetSParameter` body (`waveportoperator.cpp:780`) line by
  line — only its decl + the call sites; the lumped-port body + the assembly loop already
  establish the linear-projection + asymmetric-assembly shape decisively. A future
  authoring pass on the S-parameter output-product column should read both port bodies
  fully.
- One-observation-per-invocation discipline honored: this report surfaces the SINGLE
  observation "`gram_reduce` has no clean 3rd witness; the boundary is a spine finding."
