---
agent: lifter
invoked_at: 2026-06-03T154956Z
scope: output-product↔driver reciprocal cross-link wiring pass (active-head #7, LOW) — re-anchor driver stage-3 sections UP to their now-on-disk output-product columns
status: pending
inputs:
  - book/src/feature/driven.L4.md
  - book/src/feature/eigenmode.L4.md
  - book/src/feature/electrostatic.L4.md
  - book/src/feature/magnetostatic.L4.md
  - book/src/feature/sparameters.L4.md (target, on-disk cycle-075)
  - book/src/feature/eigenfrequency-qfactor.L4.md (target, on-disk cycle-075)
  - book/src/feature/capacitance.L4.md (reciprocal down-link reference)
  - book/src/feature/inductance.L4.md (reciprocal down-link reference)
  - scaffolding/priorities.md (active-head #7 + ratified convention, batch-23 decision #3)
integrated_at: 2026-06-03T160000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: |
  Applied cycle-078 (batch-24 position 3/3, THIRD/FINAL). Output-product<->driver reciprocal
  cross-link wiring pass across the 4 existing driver .L4.md chapters (driven x3, eigenmode x5,
  electrostatic x1, magnetostatic x1; 10 blocks): plain-text/forward-ref -> live up-link +
  reciprocal "links DOWN" framing + the c074/c075 closed-negative gram_reduce-non-subsume-S-param
  correction. All 4 drivers stay seed (a wiring pass, not a status change -- the "seed (column)"
  cells refer to the OUTPUT-PRODUCT column maturity, not the driver). All up-link targets verified
  on disk (pure plain-text->live-link upgrade; no new dead links). Satisfies the ratified
  output-product<->driver up-link convention (batch-23 decision #3) on the side-(b) up-links. NO
  firm-count change. cargo make book exit 0, linkcheck2 clean, zero build-repair. Build-relevant: yes.
---

# CYCLE: Re-anchor driver stage-3 → output-product reciprocal up-links

## Summary

This is the `output-product-driver-cross-link-wiring` standing-state pass (active-head
#7, LOW; convention ratified batch-23 decision #3). The ratified convention is reciprocal:
**(a)** each output-product column down-links its reduce verb AND cross-links UP to its
producing driver, and **(b)** each driver stage-3 (postprocess) cross-links UP to its
output-product column. Audit result: side **(a)** is COMPLETE for all 4 pairs (every
output-product column links to its driver `.L4.md` — verified, see audit table). Side
**(b)** is the drift: **none** of the 4 driver chapters carries a markdown link UP to its
output-product column file, and **two** of them (`driven`, `eigenmode`) additionally carry
now-STALE "lands later / not-yet-authored" forward-ref markers — both columns
(`sparameters.L4.md`, `eigenfrequency-qfactor.L4.md`) landed on-disk in cycle-075. The
scope-named verified drift is `driven.L4.md` (`grep -c sparameters` → 0; it forward-refs
`sparameter_reduce` and never names/links the `sparameters` column). This report
re-anchors the driver stage-3 forward-refs to the now-on-disk output-product columns:
`driven`→`sparameters` (primary), `eigenmode`→`eigenfrequency-qfactor` (same-class stale
drift), and adds the lighter convention-required column up-link to
`electrostatic`→`capacitance` / `magnetostatic`→`inductance`. Pure wiring; no signature or
decomposition change.

## Audit: all 4 pairs, both directions

Slug-token grep (`grep -c <output-slug> <driver>.L4.md`) and link inspection:

| Pair | (a) output-product → driver up-link | (b) driver stage-3 → output-product col link | Stale "not-authored" markers in driver | Repair in this report |
|---|---|---|---|---|
| capacitance ↔ electrostatic | PRESENT (`capacitance.L4.md:7,15,17,34,47,57,64` → `electrostatic.L4.md`) | ABSENT (names "capacitance", links only `gram_reduce`) | none | add light column up-link |
| inductance ↔ magnetostatic | PRESENT (`inductance.L4.md:7,17,34,50,59,65` → `magnetostatic.L4.md`) | ABSENT (names "inductance", links only `gram_reduce`) | none | add light column up-link |
| sparameters ↔ driven | PRESENT (`sparameters.L4.md:7,17,19,30,37,50,60,67` → `driven.L4.md`) | **ABSENT — 0 mentions of `sparameters`** (forward-refs `sparameter_reduce`) | YES (`:97` "lands its own dedicated column in a later cycle"; `:157` "not authored here"; `:175` "not yet authored") | **PRIMARY repair** |
| eigenfrequency-qfactor ↔ eigenmode | PRESENT (`eigenfrequency-qfactor.L4.md:7,16,18,36,51,61,68` → `eigenmode.L4.md`) | ABSENT (names slug as PLAIN-TEXT, no link) | YES (`:40` "its column lands later"; `:55` "not-yet-authored"; `:70` "forward-ref — not authored here"; `:74` "not-yet-authored") | same-class stale-drift repair |

Side (a) needs no edits. Side (b) is the convention drift this pass repairs.

## Proposed changes

### 1. `driven.L4.md` — PRIMARY repair (the scope-verified drift: 0 `sparameters` mentions)

Stage-3 prose: re-anchor the `sparameter_reduce` plain-text forward-ref to a live up-link
to the now-on-disk `sparameters` output-product column.

```edit:book/src/feature/driven.L4.md
[old]: 3. **S-parameter / frequency-response reduction** — the per-ω reduction of the
   solution family `[Eᵢ]` to the user-facing frequency response (S-parameters,
   per-frequency energy / field measurements). This stage is the **output-product**
   half of the composition root; it is the per-ω post-process measurement
   `MeasureAndPrintAll(...)` (`drivensolver.cpp:216`) plus the B-field recovery `B =
   −1/(iω) ∇×E` (`:205-207`). There is no *new* L4 combinator authored here — the
   driven S-parameter reduction is the **driven output-product surface**, which lands
   its own dedicated column in a later cycle (named plain-text forward-reference here;
   `sparameter_reduce` is NOT authored in this chapter, mirroring how the
   electrostatic/magnetostatic columns forward-ref their capacitance/inductance
   reductions to the output-product spine). The shared operator-weighted-Gram
   energy-form reduction combinator (a ≥2-witness mine across the
   capacitance/inductance/S-param reductions) is a forward mine, not a blocker (see
   Open questions).
[new]: 3. **S-parameter / frequency-response reduction** — the per-ω reduction of the
   solution family `[Eᵢ]` to the user-facing frequency response (S-parameters,
   per-frequency energy / field measurements). This stage is the **output-product**
   half of the composition root; it is the per-ω post-process measurement
   `MeasureAndPrintAll(...)` (`drivensolver.cpp:216`) plus the B-field recovery `B =
   −1/(iω) ∇×E` (`:205-207`). There is no *new* L4 combinator authored here — the
   driven S-parameter reduction is the **driven output-product surface**, authored as
   its own dedicated output-product feature column [`sparameters`](./sparameters.L4.md)
   (the scattering-matrix `S` column, which links back DOWN to this driver as its
   producing column; its stage-(2) verb [`sparameter_reduce`](../L4/sparameter_reduce.md)
   *(rough-in)* is the port-projection reduction). This mirrors how the
   electrostatic/magnetostatic drivers feed their [`capacitance`](./capacitance.L4.md) /
   [`inductance`](./inductance.L4.md) output-product columns. The shared
   operator-weighted-Gram energy-form reduction combinator
   ([`gram_reduce`](../L4/gram_reduce.md), the capacitance/inductance reductions) does
   NOT subsume the S-parameter reduction (it is a port-projection, not a Gram-weight
   specialization — the c074 D6 / c075 closed-negative distinction); see Open questions.
```

Constituent down-link table row: re-anchor the `sparameter_reduce` cell + the
output-product status cell to the live column.

```edit:book/src/feature/driven.L4.md
[old]: | S-parameter reduction (output product) | `sparameter_reduce` *(output-product column; not authored here)* | forward-ref | `drivensolver.cpp:205-216` |
[new]: | S-parameter reduction (output product) | [`sparameters`](./sparameters.L4.md) output-product column (verb [`sparameter_reduce`](../L4/sparameter_reduce.md), *rough-in*) | seed (column) | `drivensolver.cpp:205-216` |
```

Status prose: de-stale the "not yet authored" claim (the column landed cycle-075); the
column still being `seed` is the still-true reason driven stays `seed`.

```edit:book/src/feature/driven.L4.md
[old]: here). All three composition-stage L4 combinators are **firm** — the cleanest
operator-varying composition the spine carries — but the column remains uniform
`status: seed` because the stage-3 S-parameter reduction is not yet authored as a
firm output-product column (a feature column promotes past `seed` only once ALL
composed constituents are firm).
[new]: here). All three composition-stage L4 combinators are **firm** — the cleanest
operator-varying composition the spine carries — but the column remains uniform
`status: seed` because the stage-3 S-parameter reduction's own output-product column
[`sparameters`](./sparameters.L4.md) is itself `seed` (its [`sparameter_reduce`](../L4/sparameter_reduce.md)
verb is `rough-in`) — a feature column promotes past `seed` only once ALL composed
constituents are firm.
```

### 2. `eigenmode.L4.md` — same-class stale-drift repair (column landed cycle-075)

Stage-3 prose: re-anchor the plain-text `eigenfrequency-qfactor` forward-ref + drop the
stale "its column lands later".

```edit:book/src/feature/eigenmode.L4.md
[old]: This is the eigenmode driver's *only* outer loop — and it is a pure post-processing `map`, NOT a solve-iteration (explicitly contrasted at `book/src/L4/solve_family.md:146`). The eigenfrequency / Q-factor reduction into the user-facing **output product** is a forward-ref: its dedicated output-product feature column (`eigenfrequency-qfactor`, plain-text — its column lands later) authors the physical reduction; this stage records only that the eigenmode driver feeds it the converged eigenpair set.
[new]: This is the eigenmode driver's *only* outer loop — and it is a pure post-processing `map`, NOT a solve-iteration (explicitly contrasted at `book/src/L4/solve_family.md:146`). The eigenfrequency / Q-factor reduction into the user-facing **output product** is authored as its dedicated output-product feature column [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) (which links back DOWN to this driver as its producing column); this stage records only that the eigenmode driver feeds it the converged eigenpair set.
```

Output line: link the slug to the column.

```edit:book/src/feature/eigenmode.L4.md
[old]: This is what the user ran the eigenmode solver to compute. The eigenfrequency / Q reduction into the reported product is owned by the `eigenfrequency-qfactor` output-product column (forward-ref). L0 home:
[new]: This is what the user ran the eigenmode solver to compute. The eigenfrequency / Q reduction into the reported product is owned by the [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) output-product column. L0 home:
```

"Why this composes" prose: de-stale "not-yet-authored".

```edit:book/src/feature/eigenmode.L4.md
[old]: Both composed combinators ([`fe_assemble`](../L4/fe_assemble.md), [`eigsolve`](../L4/eigsolve.md)) are **firm** — so the only thing keeping this column at `seed` (rather than promoting past it) is the readout stage's forward-ref to the not-yet-authored `eigenfrequency-qfactor` output-product reduction.
[new]: Both composed combinators ([`fe_assemble`](../L4/fe_assemble.md), [`eigsolve`](../L4/eigsolve.md)) are **firm** — so the only thing keeping this column at `seed` (rather than promoting past it) is the readout stage's reduction into the [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) output-product column, which is itself `seed` (its `eigenfreq_qfactor_reduce` verb is `rough-in`).
```

Constituent down-link table row.

```edit:book/src/feature/eigenmode.L4.md
[old]: | per-mode readout (ω, Q, B=-1/(iω)∇×E) | `eigenfrequency-qfactor` *(output-product column; forward-ref — not authored here)* | (forward-ref) | `eigensolver.cpp:424-458` |
[new]: | per-mode readout (ω, Q, B=-1/(iω)∇×E) | [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) output-product column | seed (column) | `eigensolver.cpp:424-458` |
```

Status prose: de-stale "(not-yet-authored)".

```edit:book/src/feature/eigenmode.L4.md
[old]: Stage (3) is a pure per-mode readout `map`; its reduction into the user-facing eigenfrequency/Q-factor product is a forward-ref to the (not-yet-authored) `eigenfrequency-qfactor` output-product column — the one reason this column stays `seed` rather than promoting (the two solve-side constituents being firm).
[new]: Stage (3) is a pure per-mode readout `map`; its reduction into the user-facing eigenfrequency/Q-factor product is owned by the [`eigenfrequency-qfactor`](./eigenfrequency-qfactor.L4.md) output-product column (itself `seed`) — the one reason this column stays `seed` rather than promoting (the two solve-side constituents being firm).
```

### 3. `electrostatic.L4.md` — light convention-required column up-link (no stale markers)

The convention requires a stage-3 link UP to the output-product column. The chapter
already names "capacitance"; add the column up-link at the "output product half" sentence.

```edit:book/src/feature/electrostatic.L4.md
[old]: The inverse (`Cinv = C⁻¹`, LAPACK) is the `gram_inverse` consumer downstream of the reduction, not part of it. This stage is the **output product** half of the composition root. L0: `PostprocessTerminals` (`electrostaticsolver.cpp:95`, def `:100`; the energy-form `Mult`/`Dot` at `:118-127`, the inverse at `:139-140`).
[new]: The inverse (`Cinv = C⁻¹`, LAPACK) is the `gram_inverse` consumer downstream of the reduction, not part of it. This stage is the **output product** half of the composition root — authored in full as its dedicated output-product feature column [`capacitance`](./capacitance.L4.md), which links back DOWN to this driver as its producing column. L0: `PostprocessTerminals` (`electrostaticsolver.cpp:95`, def `:100`; the energy-form `Mult`/`Dot` at `:118-127`, the inverse at `:139-140`).
```

### 4. `magnetostatic.L4.md` — light convention-required column up-link (no stale markers)

```edit:book/src/feature/magnetostatic.L4.md
[old]: The inverse (`Minv = M⁻¹`, LAPACK) is the `gram_inverse` consumer downstream of the reduction, not part of it. This stage is the **output product** half of the composition root. L0: `PostprocessTerminals` (`magnetostaticsolver.cpp:108`, def `:110`; the energy-form `Mult`/`Dot` at `:129-138`, the inverse at `:151-152`).
[new]: The inverse (`Minv = M⁻¹`, LAPACK) is the `gram_inverse` consumer downstream of the reduction, not part of it. This stage is the **output product** half of the composition root — authored in full as its dedicated output-product feature column [`inductance`](./inductance.L4.md), which links back DOWN to this driver as its producing column. L0: `PostprocessTerminals` (`magnetostaticsolver.cpp:108`, def `:110`; the energy-form `Mult`/`Dot` at `:129-138`, the inverse at `:151-152`).
```

## Discipline notes

- **Pure structural wiring, not authorship.** No signature, decomposition, status, or
  algebraic-law change. Every edit either (i) re-anchors a plain-text / `sparameter_reduce`
  forward-ref to a markdown link at the now-on-disk output-product column, or (ii) de-stales
  a "lands later / not-yet-authored" marker that the cycle-075 landing of
  `sparameters.L4.md` + `eigenfrequency-qfactor.L4.md` invalidated. The `## Status` line of
  every driver stays `seed` (the reason text is corrected, the verdict is unchanged — the
  columns are themselves `seed` so the driver-stays-`seed` reason still holds).
- **High→low discipline preserved.** All up-links are cross-column reciprocal links WITHIN
  the L4 feature surface (sibling `.L4.md` files), not lower→higher lifting prose. The
  driver chapter still narrates its own composition top-down; the added clause names where
  the output-product half is authored. No rewrite direction inverted.
- **L0-evidence prose-correction (bounded, recorded).** The `driven.L4.md:97` /
  `eigenmode.L4.md:40` "lands later / not-yet-authored" claims are now factually FALSE
  (`ls book/src/feature/sparameters.L4.md` + `eigenfrequency-qfactor.L4.md` confirm both are
  on-disk, 10211 / 11119 bytes, dated 2026-06-02, landed cycle-075 commit `497cb76`). The
  de-staling is the bounded correction of a now-wrong claim, supported by the on-disk file
  existence + the cycle-075 integrate commit; it does not re-architect any decomposition.
- **`gram_reduce` does NOT subsume `sparameter_reduce` — preserved the existing
  closed-negative.** The original `driven.L4.md` stage-3 text floated "the shared
  operator-weighted-Gram energy-form reduction combinator (a ≥2-witness mine across the
  capacitance/inductance/S-param reductions)" as a forward mine. The c074 D6 / c075 work
  closed that NEGATIVE: S-parameters are a port-PROJECTION reduction, not a `gram_reduce`
  weight specialization (`sparameters.L4.md:67` states it explicitly: "the port-projection
  sibling … NOT a `gram_reduce` weight specialization"). My driven edit re-states the
  non-subsume rather than carrying the now-resolved "forward mine" framing forward — this is
  a bounded prose correction supported by the on-disk `sparameters.L4.md:17,67`.
- **Convention reference:** `scaffolding/priorities.md:24` (ratified GO) + `:42` (active-head
  #7) — "each output-product column cross-links its producing driver AND each driver stage-3
  cross-links UP to its output-product column."
- **Edited ONLY the 4 driver `.L4.md` chapters' stage-3 / status / down-link sections.** Did
  NOT touch the new energy-fields / boundary-mode files (D1/D2), `feature/index.md` matrix,
  `SUMMARY.md` (D1), the output-product column files (side (a) is already complete), or any
  L0/L1/L2/L3 entry.

## Supporting evidence

- Side-(a) completeness (output-product → driver up-links present): `capacitance.L4.md:7`,
  `inductance.L4.md:7`, `sparameters.L4.md:7`, `eigenfrequency-qfactor.L4.md:7` (each
  frontmatter `composes`/`depends` row naming its driver column) + the in-body
  `[<driver>.L4](./...)` links enumerated in the audit table.
- Side-(b) drift: `grep -c sparameters book/src/feature/driven.L4.md` → 0 (the scope-verified
  drift); the stale-marker line numbers `driven.L4.md:97,157,175` and
  `eigenmode.L4.md:40,55,70,74`.
- Targets on-disk (verified `ls`): `book/src/feature/sparameters.L4.md` (10211 B),
  `book/src/feature/eigenfrequency-qfactor.L4.md` (11119 B), both cycle-075 (`497cb76`).
- No new L0 pinpoint citations emitted (cross-column markdown links only); `citecheck
  --anchor` N/A. Link targets confirmed present on-disk.

## Open questions / caveats

- **Edits #3/#4 (electrostatic/magnetostatic) are the lighter-confidence half.** The scope
  VERIFIED only the `driven` drift and framed the other 3 drivers as "having the reciprocal
  up-link" — true at the level of *naming* their output product by slug, but FALSE at the
  level of a markdown link to the column `.L4.md` file (none of the 4 had a column link
  before this pass). The ratified convention literally says "cross-links UP to its
  output-product column" (a link). I included the light electrostatic/magnetostatic column
  up-links to make side (b) uniformly satisfied, but flag them as droppable if the
  integrator/critic reads the convention as satisfied-by-named-reference. The driven (#1) +
  eigenmode (#2) repairs are unambiguous (both carry now-FALSE "lands later/not-authored"
  markers) and should land regardless.
- **No abstractor reread needed.** The firmed-up output-product columns' signatures
  (`sparameter_reduce` rough-in, `eigenfreq_qfactor_reduce` rough-in) do NOT contradict
  anything the driver themes assumed — the drivers always forward-ref'd the reduction as the
  output-product half; only the link target (now a real column) and the "not-authored"
  staleness changed. Pure lift, no signature/decomposition conflict surfaced.
