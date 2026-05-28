---
verifies: ../CYCLE.md
critiqued_at: 2026-05-27T235000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: warning
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-27T235500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
  surface-or-evidence: not-needed
  rotation-quality: unrepairable
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: unrepairable
overall_status: pass-after-repair
follow_up_agent: null
---

# META: verification of CYCLE — harvester L3 BLAS-1 linear-update cohort (axpy + axpby + axpbypcz)

## Critique

### Checks run

**citation-validity — pass.** Every cited file path exists. Verified directly: `book/src/L1/axpy.md`, `book/src/L1/axpby.md`, `book/src/L1/axpbypcz.md`, `book/src/L3/krylov-step.md`, `book/src/L3/index.md`, `book/src/L2/krylov-step.md`, `book/src/L4/krylov-step.md`, `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md`, `book/src/L3-L2/krylov-step-body-identity.md`, `book/src/concepts/scalar-promotion.md`, `book/src/concepts/tensor-field-lift.md`, `book/src/concepts/sequential-obstruction.md`, `book/src/concepts/axpy.md`, `book/src/L1-L0/axpby-mutation-rotation.md`, `book/src/L1-L0/axpbypcz-mutation-rotation.md`, `scaffolding/decisions/axpby-as-primitive.md`, and the cycle-010 audit report `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md`. Specific line-range claims also check out: `book/src/L3-L2/krylov-step-body-identity.md:97` is the cited "seven L1 primitives ... L3-native by signature shape" passage (verified); `book/src/L4-L3/krylov-step-typed-wrapper-dissolution.md:65-68` contains the L3 body let-chain with `axpy`/`axpby`/`axpbypcz` named (verified — note the report sometimes cites line 67, sometimes range 55-89; both inside the §"L3 form (RHS)" block); `book/src/L3/index.md:13` advertises "axpy, dot, nrm2 as field operations" (line 12 actually; off-by-one but in the cited 11-14 range used elsewhere — acceptable); `book/src/L2/krylov-step.md:96` lists `axpy`/`axpby`/`axpbypcz` as L1 primitives (verified); `book/src/L1/axpby.md` has 9 laws and `book/src/L1/axpbypcz.md` has 12 laws (matches report's "nine" and "twelve" counts). L0 source ranges (`palace/linalg/vector.{hpp,cpp}` specific line ranges in §Evidence) are inherited via L1 — not re-validated at L0 by this critic, but consistent with the L1 entries' published citations.

**surface-or-evidence — pass.** This is firm-shaped harvester work authoring three new L3 entries (`book/src/L3/axpy.md`, `book/src/L3/axpby.md`, `book/src/L3/axpbypcz.md`) plus dep-map row + SUMMARY edits. Substantial surface text is supplied in §"Operator content — <op>" blocks (each operator's full chapter). The proposal does not present pure rotation_claims without surface; it is the canonical layer-coherence backfill shape (surface + retroactive-evidence framing via the upstream firm L1 / L4-L3 / L3-L2 corpus). Each entry's signature, semantics, algebraic laws, variant axes, lowering, lifting, and L0 evidence are populated to the cycle-010 `book/src/L3/krylov-step.md` precedent's section structure.

**rotation-quality — warning.** The dispatch explicitly characterises L3>L1 as "identity-in-form rotation on the primitive's signature shape" — i.e., the L3 surface is value-thread-isomorphic to the L1 surface and the algebraic-law set is "identical" to the L1 set. By the strict criterion in CLAUDE.md (rotation must make L_{n+1} strictly more compact / abstract / equational than L_n), this would be a **1:1 mapping**, not a rotation. However, this is explicitly NOT a rotation-shaped proposal under the methodology invariant **Identity-lowerings still require both L levels** (CLAUDE.md §Methodology invariants, cycle-009 meta-phase, supersedes cycle-006 "no L3 row needed"); the cycle-010 wave-1 `book/src/L3/krylov-step.md` precedent established that identity-in-form lowerings still warrant both layer entries on **layer-coherence** grounds, not on rotation-strictness grounds. Per the methodology, this is correct behavior. Flagging this as a **warning rather than fail** because the report is the second cohort-level enactment of an explicit methodology invariant that overrides the strict rotation-quality criterion; the invariant should be considered the authoritative reading. (A stricter critic mode would surface this as the expected friction: identity-in-form entries are an exception class to the rotation-quality check, and the check would benefit from a "lower-layer is on the identity track" carve-out that the cycle-010+ meta-phase may codify.)

**variant-axis-coverage — pass.** Each L3 entry declares two variant axes (`element-type`, `scalar-promotion`) and explicitly notes "matches L1 exactly; no new axes introduced; no axes merged or split". The dispatch closes the variant-axis envelope at the L1 count of two for each operator — consistent with the L1 entries' profiles. Per the L1 axpbypcz §Variant axes, the `γ == 0` real-real fast-path is a control-flow specialisation (transparent performance trick), not a variant axis; the L3 entry's §"Variant axes" section correctly notes "Internal control-flow axis at L0 (not an L3 variant axis)" for axpbypcz and explicitly says "the real-real specialisation's `γ == 0` branch is a transparent performance specialisation — algebraically equivalent at L1 — and not visible at L3". No hidden branches.

**cross-reference-integrity — pass.** All `[link]` references in the proposed entry contents resolve to existing files. Spot-checked: `[apply_linop](../L1/apply_linop.md)` exists; `[scalar-promotion](../concepts/scalar-promotion.md)` exists; `[tensor-field-lift](../concepts/tensor-field-lift.md)` exists; `[sequential-obstruction](../concepts/sequential-obstruction.md)` exists; `[axpy](../concepts/axpy.md)` exists; `[axpby-mutation-rotation](../L1-L0/axpby-mutation-rotation.md)` exists; `[axpbypcz-mutation-rotation](../L1-L0/axpbypcz-mutation-rotation.md)` exists; `[krylov-step](./krylov-step.md)` and sibling-to-be links `[axpy](./axpy.md)`, `[axpby](./axpby.md)`, `[axpbypcz](./axpbypcz.md)` resolve once the dispatch's three new files land. Forward references to `[scal](./scal.md)` (used in axpby Laws 2-3 restatement and axpbypcz Semantics) are explicitly flagged as forward-looking (consistent with L1 axpby Laws 2-3 doing the same — "when `scal` lands at L1, restates as ..."); sibling dispatch #4 is responsible for landing `scal` at L3. Subsumption chain `axpy ≺ axpby ≺ axpbypcz` is preserved in axpby Law 1, axpbypcz Laws 1-2, and in the Working Notes bullet of the proposed L3/index.md edit.

**edge-label-fidelity — pass.** Each entry's frontmatter `lowers_to` field cites `book/src/L1/<op>.md` directly, with parenthetical "no L2 intermediate" note. The §"Lowers to" section discusses exactly the L3→L1 edge, characterising the rotation as identity-in-form on the primitive's signature shape. The §"Lifts from" section explicitly states no L4 entry exists (cohort audit verdict CONFIRMED-NOT-NEEDED for the BLAS-1 cohort) — this is internally consistent with the dispatch's no-L4 verdict and matches the audit's verdict at `reports/2026-05-27T215315Z-cross-layer-cross-cutter-identity-in-form-audit/CYCLE.md:48-53`. The §"L3 vs L1 distinction" sections at the end of each entry discuss precisely the L3↔L1 edge (not, say, L3↔L2 or L3↔L4). No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Frontmatter declares `firmness: firm` for each entry. Content shape matches firm L_n operator definitions: complete signature, semantics, algebraic laws, dependencies, variant axes, status, lowering, lifting, L0 evidence, layer-distinction sections. No rough-in placeholders. The dispatch matches the firm-harvester kind: three new operator entries authored to the cycle-010 wave-1 precedent (`book/src/L3/krylov-step.md`) section structure. The cohort-bundle shape (three operators per dispatch) was explicitly invited by the cycle-010 audit (`reports/.../CYCLE.md:124-127`: "Suggested bundles ... (a) axpy + axpby + axpbypcz") — kind matches plan.

**skill-uptake-survey — warning.** The dispatch does not invoke any skill explicitly (no §"Skills invoked" section, no telemetry surface for skill use). Three skills in `skills/` directory are plausibly relevant: `verify-citation-range` (the dispatch makes many cross-references with specific line ranges — invocation would surface telemetry), `verify-refinement-surface` (each L3 entry refines via identity-in-form rotation — invocation would corroborate the surface vs. evidence framing), and `plan-sideways-concept-emission` (the dispatch could in principle have emitted a thin L3>L1 identity theme as a concept-emission, but explicitly defers per OQ `l3-l1-directory-naming-structure-policy` — invocation would have made the defer-decision more visible). Pure presence check — not blocking; surfaces telemetry. If a "harvester-cohort-bundle" skill emerges from this and sibling cohort dispatches, it could be promoted from the latent pattern.

### Issues found

1. **Subsumption chain Law 6 restatement — minor verbatim drift from L1.** The L3 axpby entry's Law 6 reads `axpby(α, x₁ + x₂, β, y) = axpby(α, x₁, β, y) + α·x₂ = α·x₁ + α·x₂ + β·y` (file:section: `proposed L3/axpby.md` §"Algebraic laws" Law 6). The L1 axpby Law 6 reads `axpby(α, x₁ + x₂, β, y) = axpby(α, x₁, β, y) + axpby(α, x₂, 0, y) = α·x₁ + α·x₂ + β·y` — i.e., the L1 form expresses the second term as the operator-self application `axpby(α, x₂, 0, y)` (which then evaluates to `α·x₂` per Law 3). The L3 form short-circuits to `α·x₂`. Mathematically equivalent (both equal `α·x₁ + α·x₂ + β·y`), but the L3 entry asserts the laws are "inherited verbatim from L1" / "identical to the L1 algebraic-law set". The verbatim claim is slightly weakened by this restatement. Severity: low. Repair shape: either restore the L1 phrasing `axpby(α, x₂, 0, y)` for the intermediate term in the L3 axpby Law 6, or weaken the "verbatim" claim to "value-equivalent restatement of the L1 set".

2. **Forward-reference to `[scal](./scal.md)` in three places assumes sibling dispatch #4 lands.** In `proposed L3/axpby.md` §"Algebraic laws" Laws 2-3 and `proposed L3/axpbypcz.md` Laws (implicit via the dependency rationale), the entries reference `[scal](./scal.md)` as a restatement target ("When [`scal`](./scal.md) lands at L3, restates as `axpby(0, x, β, y) = scal(β, y)`"). Open Question 6 of the report explicitly notes the dependence: "if sibling #4 does not land `scal`, the cross-references remain as forward-looking restatements". This is consistent with the L1 axpby's forward-looking treatment of `scal` (Laws 2-3 of L1 axpby say the same), but the L3 entries' Markdown links `./scal.md` would render as broken links at book-build time if sibling #4 fails. Severity: low (book-build breakage is the integrator-finalize's concern; the dispatch's link form mirrors the cycle-010 `book/src/L3/krylov-step.md` precedent that forward-references co-cohort entries that did not exist at the moment of authoring). Repair shape: integrator-finalize verifies sibling #4 lands, or weakens the links to plain prose if #4 defers.

3. **`book/src/L1-L0/axpbypcz-mutation-rotation.md` cross-reference is asserted but currently rough-in.** The proposed L3 axpbypcz entry §"Semantics" links `[axpbypcz-mutation-rotation](../L1-L0/axpbypcz-mutation-rotation.md)` for the in-place mutation lowering. The file exists, but per `book/src/L1-L0/index.md:19` it is currently `rough-in`, not firm. The L3 entry treats it as a stable cross-reference. Severity: low — the file exists and resolves; the firmness shift is downstream content concern, not link-integrity. Repair shape: optional caveat note in the L3 entry's §Semantics that the L1>L0 lowering for axpbypcz is rough-in, or accept the rough-in cross-reference as-is.

4. **The `book/src/L3/index.md` dep-map row insertion conflicts with sibling dispatches #1, #3, #4.** The proposed change to `book/src/L3/index.md` appends three rows (axpy, axpby, axpbypcz) "after the existing `krylov-step` row, with whatever ordering the sibling dispatches resolve to". Sibling dispatches #1 (apply_linop), #3 (dot, nrm2), and #4 (scal) will each append rows to the same table. Each sibling dispatch will produce its own integrator-per-report pass that touches the same file. The dispatch explicitly defers ordering to integrator-finalize (which is the correct mediator), but **the per-report integration sequence may produce git merge-conflict-shaped friction** if two integrator-per-report passes write the table concurrently. Severity: low (the integrator-per-report dispatch is serial per CLAUDE.md, so concurrent writes are not literal git conflicts), but ordering verification is needed across the wave-1 cohort. Repair shape: none required at the report level; integrator-finalize is the canonical mediator.

5. **Working Notes bullet specifies cycle-011 as the cycle-id, but report timestamp 2026-05-27T234525Z is the dispatch time, not the integrator-finalize commit time.** The dispatch's proposed Working Notes bullet says "Cycle-011 wave-1 cohort growth ... harvested cycle-011T234525Z". The cycle-011 cycle-id will only be finalized when the integrator-finalize runs (per CLAUDE.md, the cycle-id uses the third-cycle timestamp for meta-batches, but per-cycle it uses the cycle's own integrator-finalize timestamp). The dispatch-time timestamp (`T234525Z`) is correct as a dispatch timestamp; whether it should appear in the integrated artifact text is integrator-policy. Severity: low (a stylistic concern). Repair shape: optional — the integrator-per-report may adjust the timestamp to the integration timestamp.

6. **L4 verdict is asserted as the cohort audit's "CONFIRMED-NOT-NEEDED" verdict; per-operator restatement is consistent but not independently checked at L4.** The dispatch states "no L4 entry — leaf primitive, not a calculus combinator; per cycle-010 cohort audit verdict 'L4 candidate CONFIRMED-NOT-NEEDED' for the BLAS-1 cohort". The audit verdict was a cohort-level statement, not a per-operator restatement. Per-operator the verdict is also CONFIRMED-NOT-NEEDED (verified against the audit's `reports/.../CYCLE.md:53` line which gives the L4 verdict for the entire BLAS-1 cohort). No issue with the cohort propagation; flagging only that the verdict is inherited, not re-derived. Severity: minimal (informational).

7. **OQ `l3-l1-directory-naming-structure-policy` is referenced as defer-target but its codified status in `scaffolding/open-questions.md` is not re-asserted.** The dispatch §"Open questions / caveats" Item 1 defers the L3>L1 lowering-theme directory naming to the existing OQ; verified the OQ exists at `scaffolding/open-questions.md:1622`. No issue with the deferral; flagging only that the dispatch could have explicitly noted "OQ exists at line 1622" or similar to make the deferral self-verifying. Severity: minimal (informational).

8. **`scaffolding/decisions/axpby-as-primitive.md` §"Knock-on effects" is cited as the precedent that "explicitly invited the `axpbypcz` harvester to mirror the fused-primitive choice".** The dispatch §"Operator content — axpbypcz" §Context says the decision "mirrors `axpby`'s cycle-003 fused-primitive verdict per `scaffolding/decisions/axpby-as-primitive.md` §'Knock-on effects' — explicit invitation". File exists at the path. Section content not re-verified at L0 by this critic but consistent with the L1 axpbypcz entry's published treatment of the fused-primitive choice (the L1 axpbypcz fused-primitive choice is mature). Severity: minimal (informational).

## Repair

### Fixes attempted

- **Finding (warning, rotation-quality)**: dispatch is identity-in-form, which by strict rotation-quality criterion would be a 1:1 mapping rather than a rotation.
  - **Decision**: unrepairable (methodology-invariant compliance, not a content defect).
  - **Rationale**: CLAUDE.md §Methodology invariants codifies **Identity-lowerings still require both L levels** (cycle-009 meta-phase; supersedes cycle-006 "no L3 row needed" verdict). The dispatch is the second cohort-level enactment of this invariant (cycle-010 `book/src/L3/krylov-step.md` is the precedent). The critic explicitly noted the invariant overrides the strict rotation-quality criterion and flagged this as a warning rather than fail for that reason. Repairing would require either (a) rewriting the proposal to introduce non-identity content (substantive authoring; out of repair authority), or (b) overriding the methodology invariant (out of repair authority). Note as methodology-invariant compliance.

- **Finding (warning, skill-uptake-survey)**: dispatch declares no `§Skills invoked` section; three plausibly-relevant skills (`verify-citation-range`, `verify-refinement-surface`, `plan-sideways-concept-emission`) not surfaced as telemetry.
  - **Decision**: unrepairable (telemetry, retrospective; the repairer cannot retroactively invoke skills the producer did not invoke).
  - **Rationale**: Skill-uptake-survey is a presence/telemetry check; the dispatch's CYCLE.md is a fixed artifact of which skills the producer chose to invoke. Authoring a §"Skills invoked" section after the fact would fabricate telemetry. The latent pattern (a "harvester-cohort-bundle" skill candidate) may be propagated to `scaffolding/skill-candidates.md` by meta-phase if it recurs.

- **Finding (low, issue #1)**: L3 axpby Law 6 phrasing — uses short-circuited `α·x₂` for the intermediate term; the L1 axpby Law 6 uses the operator-self application `axpby(α, x₂, 0, y)`. The L3 entry asserts the laws are "inherited verbatim from L1".
  - **Decision**: repaired.
  - **Action**: rewrote the intermediate term in `proposed L3/axpby.md` §"Algebraic laws" Law 6 (CYCLE.md line 304) from `axpby(α, x₁, β, y) + α·x₂` to `axpby(α, x₁, β, y) + axpby(α, x₂, 0, y)` and appended a parenthetical "(The `axpby(α, x₂, 0, y)` term is `α·x₂` per Law 3; the `+` is tensor addition. Verbatim form from L1 axpby Law 6.)" mirroring the L1 entry's parenthetical at `book/src/L1/axpby.md:50`. The "verbatim from L1" claim now holds at the law-statement level (with the layer-appropriate `vector → tensor` vocabulary shift in the law header).

- **Finding (low, issue #2)**: Forward-references to `[scal](./scal.md)` in three places (axpby Laws 2-3, axpbypcz Semantics) depend on sibling dispatch #4 landing.
  - **Decision**: not-needed (the dispatch explicitly flags the forward-reference shape and the critic confirms it mirrors the cycle-010 `book/src/L3/krylov-step.md` precedent's forward-reference treatment; integrator-finalize is the canonical mediator).
  - **Rationale**: Cross-reference integrity at book-build time is integrator-finalize's concern; the forward-looking link shape is the methodology-conformant pattern for cohort-internal references (L1 axpby Laws 2-3 do the same). Not a repair-authority concern.

- **Finding (low, issue #3)**: Cross-reference to `book/src/L1-L0/axpbypcz-mutation-rotation.md` is currently rough-in, not firm. The L3 entry treats it as a stable cross-reference.
  - **Decision**: not-needed (informational; the file exists and resolves — firmness-shift is downstream content concern, not link-integrity).
  - **Rationale**: The critic flagged this as severity-low informational, noting the link resolves and the firmness shift is a separate concern. No repair action requested.

- **Finding (low, issue #4)**: L3/index.md dep-map row insertion order conflicts with sibling dispatches #1, #3, #4.
  - **Decision**: not-needed (integrator-finalize is the canonical mediator per CLAUDE.md cycle-005 split-integrator boundary).
  - **Rationale**: The dispatch explicitly defers ordering to integrator-finalize; the critic confirms the per-report integration is serialized (no literal git conflicts). Integrator coordination is out of repair authority.

- **Finding (low, issue #5)**: Working Notes bullet timestamp uses dispatch-time `cycle-011T234525Z`; integrator-finalize commit time may differ.
  - **Decision**: not-needed (cosmetic; the critic noted "integrator-per-report may adjust the timestamp to the integration timestamp").
  - **Rationale**: Stylistic concern routed to integrator policy. No repair action requested.

- **Finding (low, issue #6-8)**: Informational items — cohort-level L4 verdict propagated per-operator without independent re-derivation (#6); OQ `l3-l1-directory-naming-structure-policy` is referenced but line-number not self-asserted (#7); `scaffolding/decisions/axpby-as-primitive.md` §"Knock-on effects" section content not re-verified at L0 by critic (#8).
  - **Decision**: not-needed (all flagged as severity-minimal/informational by the critic; no repair action requested).

### Unrepairable findings

- **rotation-quality warning** — methodology-invariant compliance. No follow-up agent needed; this is expected behavior for the identity-lowering layer-coherence backfill class. The cycle-010+ meta-phase may codify a "lower-layer is on the identity track" carve-out for the rotation-quality check (critic's parenthetical) — that is a methodology-level proposal, not a per-report repair.
- **skill-uptake-survey warning** — telemetry, retrospective. If a "harvester-cohort-bundle" skill emerges from this and the sibling cohort dispatches (#1, #3, #4), meta-phase may promote it from the latent pattern via `scaffolding/skill-candidates.md`.

## Suggested resolution

`pass-after-repair` (one mechanical fix applied to L3 axpby Law 6 verbatim alignment; two warnings noted as methodology-invariant compliance / telemetry retrospection; six informational items left as flagged). Integrator-per-report may apply the report's proposed-changes blocks as-is; the repaired Law 6 phrasing is now embedded in CYCLE.md §"Operator content — axpby". Integrator-finalize coordinates the L3/index.md row ordering and SUMMARY.md ordering across the wave-1 cohort (sibling dispatches #1, #3, #4).
