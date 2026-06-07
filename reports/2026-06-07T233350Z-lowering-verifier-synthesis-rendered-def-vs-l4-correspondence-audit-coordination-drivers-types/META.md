---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T235900Z
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

# META: verification of "Audit synthesis-rendered-def-vs-l4-correspondence — coordination / drivers / types"

## Critique

### Checks run

**citation-validity** — pass. This is an audit-class report whose anchors are book-internal (rendered-def line ↔ authoritative-chapter line), not L0 source citations, so the report correctly notes (CYCLE.md:457-460) that the citecheck L0 adjudicator is N/A (the synthesis defs carry no L0 citations by convention; L0 is owned by the linked L4/feature/concept chapters). I spot-checked the load-bearing book-internal pinpoints by direct on-disk Read: (a) `L4/eigsolve.md:44` does write `eigsolve op inp = execState (solve_loop op inp) (initial_state inp)`, and `:70`+`:74` both establish `Solve a = StateT EigState Identity a` over `EigState` — the exact self-inconsistency the report's Residual 1 rests on; (b) `config-record.md:67-75` is a 6-field `IoData` brace form with `units : Units` at `:74`, confirming the Residual 2 elision; (c) `synthesis/coordination.md:230` renders `... (initial_eig_state inp)` with the inline disclosure NOTE at `:225-229` citing `:44`, and `#extern eigen_iterate` after the sig at `:242-243`; (d) `synthesis/types.md:38-44` renders exactly 5 fields (no `units`) with the cited `config-record.md:69-73` range at `:34`; (e) `synthesis/coordination.md` ksp_solve discharge matches `ksp_solve.md:57`; (f) `synthesis/drivers.md:87-93` renders the electrostatic `gram_reduce k vs (\i j -> 1)` composition. Every spot-checked pinpoint resolved in-range and supported the prose.

**surface-or-evidence** — pass. This audit proposes NO mutation to any L4/feature/concept chapter (CYCLE.md:404-405); the two residuals route as gated OQ follow-ups, not in-this-report surface edits. So the surface-or-evidence frame is "pure verification with routed-out findings," which is the allowed audit shape — no orphan rotation_claim. The record-definition sub-check is satisfied for the record names appearing in the audited defs (`IoData`/`OpParams`/`SimState`/`EigState`/`StepReturn`): each is shown to have a definition home that the synthesis links to rather than restates — `IoData`/`OpParams`/`SimState` → `concepts/` pages (verified `config-record.md` exists with the brace form at `:67-75`); `EigState`/`StepReturn` rendered single-consumer in the coordination type block with links to `concepts/eigsolve.md` / `concepts/solve-result.md`. No signature-named record left undefined.

**rotation-quality** — pass (not applicable to the audited kind, by the same logic as the feature-surface no-op). The Synthesis Part is an implementation VIEW, not a lowering theme — it renders the synthesized code form of already-firm L4 vocabulary, it rotates nothing. The report states this explicitly (CYCLE.md:377-381, 486-490) and re-frames the law-bearing check as body-equivalence-preservation, which it then spot-confirms per def (CYCLE.md §Algebraic laws). The directionality / rank-violation surface is correctly noted as N/A for a reference-class-only Part.

**variant-axis-coverage** — pass. The two opaque-kernel variant boundaries in scope (the eigsolve dual-surface, the fold_solve opaque per-step op) are each handled with the `#extern`-after-sig convention and the variant axes deferred to the kernel-impl node (`eigsolve-impl`, whose own variant_axes I confirmed on disk at `eigsolve-impl.md:28-30`: eigen-algorithm / problem-symmetry). The audit verifies the `#extern`-vs-inline split tracks the kernel-API/impl distinction rather than hiding a branch (CYCLE.md:350-358). No hidden branch surfaced.

**cross-reference-integrity** — pass, and load-bearing for this report (the audit's value IS the rendered-def ↔ authoritative-chapter link integrity). I confirmed the DIRECTIVE-3 dual-surface integrity directly: `L3/eigsolve-impl.md:19-23` carries the `realizes-kernel-api` edges to BOTH `L3/eigsolve` and `L4/eigsolve` as `reference`-class (not `depends-on`), exactly as the report claims (CYCLE.md:133-135, 443-447). The coordination.md frontmatter carries `edges: reference:` only with no `depends-on:` key and no `rank:`, confirming the report's "zero spurious depends-on" claim (CYCLE.md:341-348). The audited link targets (L4 ops, feature columns, concept pages) resolve.

**edge-label-fidelity** — pass (no L_{n+1}→L_n edge label is carried — the Synthesis Part is a VIEW, not a lowering edge). The one typed correspondence in scope (`realizes-kernel-api`, eigsolve-impl → eigsolve) is discussed by the prose that carries it, and its `reference`-class typing is verified on disk. No edge-label/prose mismatch.

**plan-kind-consistency** — pass. The report is declared as a `lowering-verifier` audit and behaves as one throughout: a verdict (SUPPORTED with 2 flagged residuals), per-citation findings, no book mutation, residuals routed as OQs. The PARTIALLY-SUPPORTED sub-verdicts on the two specific defs (eigsolve seed, IoData elision) are honestly scoped to the def level while the top-level verdict stays SUPPORTED — consistent classification, no rough-in placeholders masquerading as firm.

**skill-uptake-survey** — pass (telemetry only). The audit-class shape implies the citecheck adjudicator and a correspondence-audit procedure; the report explicitly addresses citecheck applicability (N/A here, with a sound rationale) and performs the rendered-def↔chapter line-correspondence audit by direct Read throughout. No missing-skill-invocation gap blocks anything.

### Issues found

No blocking issues. The audit's two load-bearing claims (the upstream L4/eigsolve `initial_state`-vs-`StateT EigState` self-inconsistency, and the `IoData` `units`-field elision) are both independently confirmed correct by on-disk Read, and both are correctly characterized as NON-defects of the synthesis rendering (one upstream-chapter issue, one shell completeness gap), correctly routed to OQs (`l4-eigsolve-initial-state-vs-initial-eig-state-seed-inconsistency` → abstractor; `synthesis-types-iodata-omits-units-field` → layer-intro-author), and genuinely non-blocking for the batch.

Two non-blocking observations (recorded for the integrator, not check failures):

- **(minor, surfaced-and-self-disclosed)** The report's third Open-question (CYCLE.md:476-484) notes a status-token inconsistency: `synthesis/coordination.md:19` carries `> Status: seed` in body prose while drivers.md/types.md carry the `navigational-container` convention. I confirmed coordination.md:19 does read `> **Status: \`seed\`.**`. The report correctly classifies this as a shell-author/meta normalization item (not a correspondence defect, since the rendered bodies are faithful regardless of the cell label) and routes it rather than auto-fixing — appropriate, but worth the integrator's awareness as a pre-existing per-chapter inconsistency, not introduced by this audit.

- **(informational, no action)** The eigsolve Residual 1 is the strongest finding in the report and I weighted my verification toward it: the synthesis def's inline NOTE additionally claims the inconsistency recurs at `L4/eigsolve.md:97` (§Semantics prose). I confirmed `:97` does repeat the `initial_state inp` reference in the net-effect prose, so the report's "carries the inconsistency in two places" claim (CYCLE.md:148) is accurate, and the proposed upstream edit correctly targets both `:44` and `:97`.
