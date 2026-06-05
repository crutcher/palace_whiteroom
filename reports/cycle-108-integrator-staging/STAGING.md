# cycle-108 integrator staging log

Per-report integration landings for cycle-108 (batch-34). Newest LAST, append-only.
Row ORDER is the authoritative apply-order record (NOT the `applied_at` timestamps).

---

## 2026-06-05T223620Z-cycle-108-D1-layer-intro-author-lowering-chain-liveness
applied_at: 2026-06-05T22:51:13Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/L4-L3/bc-elimination-post-composition-dissolution.md (frontmatter: legacy lhs:/rhs: → scheme edges: block; lowers-to {eliminate_essential_bc, eliminate_rhs, fe-operator-assemble-mutation-rotation}, lifts-from eliminate_bc, essential_dofs as reference operand)
- book/src/L1/eliminate_essential_bc.md (frontmatter: legacy lowers_to:/lifts_from:/depends_on: → scheme edges:; depends-on {essential_dofs (uses), fe-operator-assemble-mutation-rotation (lowers-to)}; variant_axes preserved verbatim)
- book/src/L1/essential_dofs.md (frontmatter: legacy → scheme edges:; depends-on essential-dofs-construction-rotation (lowers-to); variant_axes preserved verbatim)
- book/src/L1-L0/essential-dofs-construction-rotation.md (prepend edges: frontmatter — authored from scratch; lowers-to L1/essential_dofs + 3 cites-evidence L0)
- book/src/L2/divfree-projector.md (prepend edges: frontmatter — authored from scratch, was NO frontmatter; lowers-to {L1/divfree-projector, L2-L1/divfree-projector-leaf-identity}, depends-on L2/ksp_solve)
- book/src/L1/divfree-projector.md (prepend edges: frontmatter — authored from scratch, was NO frontmatter; lowers-to L1-L0/divfree-projector-mutation-rotation, depends-on {ksp_solve, apply_linop, axpy})
- book/src/L2-L1/divfree-projector-leaf-identity.md (prepend edges: frontmatter — authored from scratch; lifts-from L2/divfree-projector, lowers-to L1/divfree-projector)
- book/src/L1-L0/divfree-projector-mutation-rotation.md (prepend edges: frontmatter — authored from scratch; lowers-to L1/divfree-projector + 3 cites-evidence L0)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- concept_writes on existing slug: 0
- forward-edge without surface: 0
- edge-label / prose mismatch: 0 (critic edge-label-fidelity scrutinized pass)
- H1 reuse of page heading: 0
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (both edited L1 ops preserve variant_axes verbatim)
- SUMMARY.md chapter registration: 0 (no new files created — all 8 targets pre-existed; pure frontmatter edits)
- graded-stack rank gate (rank(u) ≤ min deps): PASS — every typed depends-on rests firm-on-firm; rank_violations 0
- bookkeeping incomplete: 0

Citecheck (`citecheck.py --scan` over CYCLE.md): not separately re-run by integrator; the producer + critic both ran `citecheck --anchor` on the 4 load-bearing L0 anchors (all [ok]) and the critic verified the additional cites-evidence ranges in edits #4/#8 in-bounds. No MISS/AMBIG/OOB reported upstream; the cites-evidence L0 paths resolve as rank-terminal ground truth (matches set-subvector-zero-mutation-rotation precedent). Non-blocking.

Open questions promoted:
- lowering-chain-liveness-grounded-and-rescued + L2-L1-cohort-gap (cycle-108 D1) — single appended section carrying:
  - RESOLVED: lowering-chain-liveness-not-propagated-to-l1-ops → grounded-and-rescued for all scoped legs (BC + divfree)
  - FOLLOW-UP (routed batch-34 meta-phase): l2-l1-theme-cohort-reachability-gap (the other 10 L2-L1 themes, identical operator→operator-not-operator→theme cause)
  - FOLLOW-UP (routed batch-34 meta-phase / scheme-doc): lowering-theme-reachability-vs-well-foundedness-scheme-clarification (graded-stack-scheme.md §5 one-line note)

Gate / linter verification (run on live tree post-apply):
- YAML round-trip: all 8 frontmatter blocks parse via yaml.safe_load — OK
- graded_stack_lint.py --show-inbound: rank_violations 0 (HELD), reachable from roots 95 → 102 (+7), detritus 163 → 156 (−7), untyped 61 (HELD)
- Node rescue confirmed MEASURABLE: all 8 target nodes now carry typed inbound `<-` edges, none shows residual [garbage?]/[GARBAGE*]:
    L1/eliminate_essential_bc <- L4-L3/bc-elimination-post-composition-dissolution
    L1/eliminate_rhs          <- L4-L3/bc-elimination-post-composition-dissolution
    L1/essential_dofs         <- L1-L0/essential-dofs-construction-rotation, L1/eliminate_essential_bc
    L1/divfree-projector      <- L1-L0/divfree-projector-mutation-rotation, L2-L1/divfree-projector-leaf-identity, L2/divfree-projector
    L2/divfree-projector      <- L2-L1/divfree-projector-leaf-identity, L3/divfree-projector
    L1-L0/divfree-projector-mutation-rotation   <- L1/divfree-projector
    L1-L0/essential-dofs-construction-rotation  <- L1/essential_dofs
    L2-L1/divfree-projector-leaf-identity       <- L2/divfree-projector
- unresolved depends-on targets: 0
- No regression: no previously-reachable node became garbage

Build-relevant: yes

Notes: All 8 [old] anchors matched on-disk verbatim (re-read at apply time). Three legacy-frontmatter files (edits #1/#2/#3) had their legacy lhs:/rhs:/lowers_to:/lifts_from:/depends_on: keys fully REPLACED by the scheme edges: block (not left dangling). Five files (#4–#8) acquired edges: frontmatter; two of those (L2/divfree-projector, L1/divfree-projector) had NO frontmatter at all before. Report enumerated 7 rescued + 1 faithful refinement (the operator→theme L2/divfree-projector lowers-to L2-L1/divfree-projector-leaf-identity edge, mirroring how L1 ops reach their L1-L0 theme) = the +7 reachable delta; verified exact on live tree. The c107-noted L1/divfree-projector discrepancy (pre-scheme L2 parent dead-ending the sweep) is now CLOSED. Deferred integrated_at to finalize per role-spec. No book rebuild / commit / housekeeping done (finalize's job). Position 1 of 2 in cycle-108 — one more ready report follows.

---

## 2026-06-05T223620Z-cycle-108-D2-layer-intro-author-counter-update-node-typing
applied_at: 2026-06-05T23:02:00Z  (advisory only — row ORDER is the apply-order record, NOT this timestamp)
applied_by: integrator-per-report
status: applied

Files touched:
- book/src/concepts/counter-update.md (prepend graded-stack NODE frontmatter: rank: firm, kind: primitive, edges: depends-on: [], reference: [concepts/state-stratification, L4/preconditioning-framework, L3/krylov-step]; body prose UNCHANGED)

Gate hits:
- retroactive-budget per-slice: 0
- retroactive-budget global: 0
- concept_writes on existing slug: 0 (frontmatter prepend to existing page, no new concept slug; body unchanged)
- forward-edge without surface: 0
- edge-label / prose mismatch: 0 (critic edge-label-fidelity pass; reference-vs-depends-on down-typing verified scheme-correct)
- H1 reuse of page heading: 0 (frontmatter goes ABOVE the existing H1; H1 unchanged)
- append on missing slug: 0
- variant-axis missing on multi-variant operator: 0 (single scalar-increment primitive, no variant axes)
- graded-stack rank gate (rank(u) ≤ min deps): PASS vacuously — depends-on: [] (no blocking edge to check); rank_violations 0
- SUMMARY.md chapter registration: 0 (page pre-existed and was already registered; no new file)
- bookkeeping incomplete: 0

Citecheck (`citecheck.py --scan` over CYCLE.md): 8 ok, 0 failing (8 citations checked). No MISS/AMBIG/OOB. Non-blocking — clean.

Open questions promoted:
- concepts-counter-update-needs-node-rank-and-depends-on-edges — RESOLVED by this typing (appended a RESOLVED resolution section to open-questions.md; the cycle-107-opened deferral is now closed: counter-update typed firm NODE, depends-on → state-stratification down-typed to reference per well-foundedness)

Gate / linter verification (run on live tree post-apply):
- YAML round-trip: frontmatter parses via yaml.safe_load — OK ({rank: firm, kind: primitive, edges: {depends-on: [], reference: [3 targets]}})
- graded_stack_lint.py: rank_violations 0 (HELD); untyped 61 → 60 (counter-update leaves the untyped set, as EXPECTED); detritus 156 → 157 (+1, counter-update joins as typed-but-unreached); reachable from roots 102 (HELD — no node lost reachability); unresolved depends-on targets 0
- counter-update reachability: [garbage?] concepts/counter-update — typed NODE, reachable-only-via-reference, NOT reachable from any feature root. Honestly NOT forced live (nothing depends-on it; no depends-on manufactured to chase reachability). This is the EXPECTED, critic-reproduced outcome.
- All 3 reference targets resolve on-disk: concepts/state-stratification.md, L4/preconditioning-framework.md, L3/krylov-step.md — all confirmed present.
- No regression: no previously-reachable node became garbage (reachable held at 102).

Build-relevant: yes

Notes: The [old] anchor matched on-disk verbatim (re-read at apply time after D1 landed; D1 touched a disjoint file set — no overlap with concepts/counter-update.md). BEFORE-linter baseline observed on the live tree was detritus 156 / untyped 61 / rank_violations 0 (NOT the report's clean-tree 163/61 — D1's +7-reachable/−7-detritus landing this same cycle had already moved detritus to 156; the report's BEFORE was measured against a clean pre-D1 tree). The expected DELTAS (untyped −1, detritus +1, rank_violations held, reachable held) reproduced exactly against the live post-D1 baseline. The reference-vs-depends-on down-typing on state-stratification is scheme-correct: state-stratification has no rank: line on-disk (confirmed — non-node), so a firm depends-on would be well-foundedness murk. Deferred integrated_at to finalize per role-spec. No book rebuild / commit / housekeeping done (finalize's job). Position 2 of 2 in cycle-108 — FINAL report; cycle-108 per-report integration COMPLETE, ready for integrator-finalize.

---
