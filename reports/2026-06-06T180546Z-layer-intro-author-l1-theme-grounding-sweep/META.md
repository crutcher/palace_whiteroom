---
verifies: ../CYCLE.md
critiqued_at: 2026-06-06T19:05:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
overall_status: ready
---

# META: verification of "L1 op→theme grounding sweep (dot / nrm2 / scal)"

## Critique

### Checks run

**citation-validity — pass.** Every load-bearing claim carries a pinpoint and each was re-read on disk. The three op-file `[old]` blocks match the live files exactly (`dot.md:5-8` `reference: [L1-L0/dot-mutation-rotation, concepts/dot]`; `nrm2.md:5-9` `depends-on: [L1/dot]` + `reference: [L1-L0/nrm2-mutation-rotation]`; `scal.md:5-8` `reference: [L1/axpby, L1-L0/scal-mutation-rotation]`). The three `## Status = firm` lines verified on disk at the cited locations (`dot-mutation-rotation.md:384`, `nrm2-mutation-rotation.md:223`, `scal-mutation-rotation.md:202`). The three theme opening-prose quotes verified verbatim (`dot-mutation-rotation.md:3-6`, `nrm2-mutation-rotation.md:3-5`, `scal-mutation-rotation.md:3-6`). The three op files carry `rank: firm` at line 4 as claimed. No frontmatter `verified_against:` block in this report, so the YAML round-trip sub-check is not applicable.

**surface-or-evidence — pass.** This is a pure frontmatter edge-typing change (grounding hygiene), not a refinement of operator/theme surface and not a record-defining signature change — the record-definition sub-check is not applicable (no new record named). The evidence shape is the linter delta + the per-edge faithfulness derivation, both of which are present and independently reproduced (see edge-label-fidelity and the reachability cross-check below). No surface prose was touched; the producer's stale-prose grep (0 rank-direction matches) was confirmed by inspection of the unchanged op-file bodies.

**rotation-quality — pass (not applicable to a grounding-hygiene edge-typing report).** No new algebraic/structural rotation is asserted; the report retypes existing op→theme edges from `reference` to `depends-on (kind: lowers-to)`. The underlying rotations (the three mutation-rotation themes) already exist and are firm; this dispatch does not re-derive them.

**variant-axis-coverage — pass (not applicable).** No variant axes are introduced or modified by an edge-typing change. The ops' own variant axes (e.g. `scal`'s real/complex axis) are untouched.

**cross-reference-integrity — pass.** All four edge targets that appear in the three `[new]` blocks resolve on disk: `book/src/L1-L0/dot-mutation-rotation.md`, `book/src/L1-L0/nrm2-mutation-rotation.md`, `book/src/L1-L0/scal-mutation-rotation.md`, and the preserved `book/src/concepts/dot.md` / `book/src/L1/axpby.md`. The template reference `book/src/L1/set_subvector_zero.md` exists.

**edge-label-fidelity — pass (load-bearing for this report; verified directly).** Each `lowers-to` edge is genuinely faithful — each theme's own opening prose explicitly states it lowers the matching L1 op into a real pure→in-place (or pure-reduction→L0-reduction-chain) translation: `dot-mutation-rotation` "Lowers the pure L1 form `dot(x, y) = xᴴ y` ([`L1/dot`], firm) into Palace's L0 reduction surface" (`:3-6`); `nrm2-mutation-rotation` "Lowers the pure L1 form `nrm2(x) = √⟨x, x⟩` into Palace's L0 `linalg::Norml2` one-line composition" (`:3-5`); `scal-mutation-rotation` "Lowers the pure L1 form `scal(α, x) = α·x` (firm; see [`L1/scal`]) into Palace's in-place L0 receiver-mutating member call `x *= α`" (`:3-6`). Each `L1/<op> → L1-L0/<op>-mutation-rotation` edge points at exactly the theme that lowers it — the edge label is faithful in all three cases.

**plan-kind-consistency — pass.** The content shape is genuine grounding hygiene (frontmatter-only edge retype to flow liveness DOWN the `lowers-to` edge per the c108 §5 convention), exactly the c113 D2 `set_subvector_zero` move it cites as template. The declared scope and the proposed changes match. The producer correctly respected the scope boundary — it did NOT touch the `normalize`/`reciprocal`/`elementwise_product` themes; those ops are RE5 baseline-exception garbage, so grounding their op→theme edge would not flip the theme reachable (hygiene-only, correctly routed to meta-phase). That boundary call is correct.

**skill-uptake-survey — pass.** No dedicated skill is implied by a one-paragraph edge-retype following an established convention; the report cites the canonical template chapter (`set_subvector_zero.md`) and the c108 §5 convention directly, which is the appropriate uptake here.

### Reachability claim — independently reproduced

I applied the three proposed `[new]` blocks on a clean tree (D1's parallel work stash-parked, exactly the producer's measurement protocol), ran `graded_stack_lint.py`, then reverted and restored D1's working-tree state. The producer's numbers reproduce **exactly**:

- clean baseline: reachable 124, detritus 135, STRONGER 24, edge-untyped detritus 111, rank_violations 0.
- after the 3 edits: reachable 127 (**+3**), detritus 132 (**−3**), STRONGER 24 (**HELD**), edge-untyped detritus 108 (**−3**), rank_violations 0 (**HELD**).
- `--show-inbound` confirms the three themes flip from `[garbage?]` to inbound-bearing (`L1-L0/{dot,nrm2,scal}-mutation-rotation <- L1/{dot,nrm2,scal}`).

The producer's CORRECTION reasoning is verified sound: the three themes carry NO frontmatter (their files open with `# <title>`, no `---` block, hence no typed outbound edges), placing them in the edge-untyped detritus subset, not the STRONGER subset ("declares typed deps yet stays unreachable"). Flipping them reachable therefore drops edge-untyped detritus 111→108 and leaves STRONGER unchanged at 24 — NOT the −3 the brief projected. The load-bearing deltas (reachable +3, detritus −3, rank_violations HOLD 0) match the brief exactly. The rank-well-foundedness claim also holds: each theme leads `## Status` with `firm` (rank 3) and each op is `rank: firm` (rank 3), so `rank(op=3) ≤ rank(theme=3)` is satisfied for all three edges (linter reports 0 rank violations after the edits).

### Preservation — verified

All required existing edges are kept (moved, not duplicated): `dot.md` keeps `reference: concepts/dot` and moves only the theme edge into `depends-on`; `nrm2.md` keeps `depends-on: L1/dot` and adds the theme as a second `depends-on (kind: lowers-to)`; `scal.md` keeps `reference: L1/axpby` and moves only the theme edge into `depends-on`. No edge is dropped or duplicated across the `reference`/`depends-on` partition.

### Issues found

None. All 8 checks pass; the reachability delta, rank-well-foundedness, preservation, the scope-boundary call, and the STRONGER-vs-edge-untyped correction were all independently reproduced and confirmed correct. `overall_status: ready`.
