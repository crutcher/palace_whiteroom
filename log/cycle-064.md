## 2026-05-25 cycle-64 — forward cg [L4→L4] — revise

- Synthesis: CG L4→L4 self-rotation v0.4: makes the state-schema choice explicit — `res` is hoisted from a hypothetical state field to a step-output field, surfacing the §3.8 demand-driven pruning hook. State schema unchanged from v0.3 (which was already correct); documentary rotation names what produced it. Note: this content was already present on disk; this cycle emits the rotation_claim retroactively for the audit trail.
- Verdict: revise.
- Friction: Rotation-quality check #8: the claim is framed as L3→L4 but the from_form is a hypothetical alternative L4 schema, not the actual L3 form. This is a self-rotation at L4 (v0.3→v0.4 documentary refinement, as log_synthesis admits: 'L4→L4 self-rotation'). Labeling it L3→L4 while the structural content is L4-internal blurs the edge taxonomy. The state-hiding argument (res derivable from beta) is real and substantive, but it lives within L4 — it's a schema-design refinement, not a layer rotation. Carrying it as L3→L4 sets a precedent where any L4 refinement gets re-attributed to the layer edge..
- Structural change: applied: 1 lesson(s); 1 rotation_claim(s).
