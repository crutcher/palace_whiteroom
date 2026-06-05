---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T073049Z
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

# META: verification of "P1 typed-edge — navigational container pages + node-status convention"

## Critique

### Checks run

**citation-validity (pass).** The report's load-bearing assertions all resolve. The scheme citations check out exactly: `graded-stack-scheme.md` §4 frames the `L_n/index.md` as "a navigational overview, not a DAG leaf node carrying claims; its dep-map table is a derived view" and §5 explicitly carves out "**Whether an index page is itself a DAG node** … is NOT cleanly resolvable in this single … pass … carved out as a **P1 sub-task + an OQ**" — the report is deciding precisely the OQ the scheme defers to P1. The `reference`-edge semantics it leans on are verbatim in §2 ("Constrains nothing; carries **no** liveness — a mere mention must not keep dead vocabulary alive"). The linter citations are accurate: `is_likely_outside_dag` lives at the cited region (FEATURE_NON_COLUMN = `{feature/driver-leaf, feature/output-product, feature/spine-root, feature/index}`, `*/index` suffix match); the `untyped` flag clears as soon as ANY edge is read (`read_any_edge`); the only `kind` comparison the linter makes is `== "feature-surface"`. No record is named in any container signature, so the record-definition sub-check no-ops (correctly noted in Open questions). This is a typing/convention dispatch, not a source-claim dispatch, so there are no Palace L0 line-range citations to bounds-check.

**surface-or-evidence (pass).** Not a refinement of an operator/theme surface — it is a structural/frontmatter typing pass plus an authoritative convention decision. The "evidence" shape is the scheme §4/§5 carve-out (the OQ it resolves) + the programmatic edge-existence + member-set verification, all of which I reproduced independently. No claim is asserted without its support.

**rotation-quality (pass — not applicable).** No algebraic/structural/reduction rotation is asserted; the dispatch types navigational containers with `reference`-only edges and makes a node-status convention decision. Check no-ops, as it does for the `stub`/`roadmap_goal`/feature-surface kinds.

**variant-axis-coverage (pass — not applicable).** Navigational container pages carry no orthogonal variant axes (the axes live in the indexed member chapters). No hidden branches.

**cross-reference-integrity (pass — LOAD-BEARING, fully verified).** I extracted all 35 `edit:` blocks and all `reference` targets programmatically: **230 targets across 35 container files, 0 dangling** — every `book/src/<slug>.md` exists on disk, matching the report's claim exactly. I then re-derived each container's member set from `SUMMARY.md` (Part-aware: a layer/lowering/feature index's members = the Part-top sibling group-intro pages excluding its own "Overview"; a group-intro / feature-group page's members = its direct nested nav children) and compared against the report's edge lists: **35/35 containers match their SUMMARY.md nav children exactly — 0 missing, 0 extra.** The member-derivation prose is precise: flat lowering indexes (L2-L1/L3-L2/L4-L3) point directly at theme-leaf chapters (no group-intro layer), while L1-L0/index points at its 3 theme-group-intros — both confirmed. The 230 decomposes as 7+5+5+3 (layer idx) + 3+11+6+11 (lowering idx) + 3 (feature idx) + 3+18+15 (feature groups) + 23 group-intros = 230.

**edge-label-fidelity (pass — the load-bearing convention decision is sound).** The reference-only / no-rank / no-`depends-on` convention for index pages is correct per scheme §3/§4. The core argument — an index does NOT `depends-on` its members (a `reference` edge constrains no rank and carries no liveness, so an index cannot keep dead vocabulary alive; a chapter is live only because a feature root transitively depends-on it) — is exactly the §2/§3 semantics and is the right call: typing an index with `depends-on` would (a) wrongly impose `rank(index) ≤ min(members)` on a page that makes no resolution claim, and (b) wrongly make the index a liveness source, defeating the reachability GC. `reference`-only flips the page out of `untyped` (clearing the WARNING) without creating either pathology. The decision is the fully scheme-aligned resolution of OQ `graded-stack-index-and-concept-node-status` for the container half. The D8 same-file partition is clean: L4/index.md's `[old]` anchor is line 1 (the `# L4 — Top of the stack` H1) with frontmatter prepended ABOVE it; the `## Vocabulary cohort` section (line 30, mid-file) is D8's exclusive surface and is untouched — non-overlapping anchors confirmed on disk.

**plan-kind-consistency (pass).** Content shape matches the declared kind (a P1 typed-edge container-typing dispatch + authoritative convention decision). Every block is a `reference`-only `edges:` frontmatter prepend with `kind: navigational-container`, no `rank:`, no `depends-on` — consistent with "navigational container, not a DAG node." I verified all 35 YAML frontmatter blocks parse (`yaml.safe_load`), none carry `rank:`, none carry `depends-on:`, all carry `reference:` edges, and the H1 title line is preserved verbatim in every block. The parenthetical `kind` value (`navigational-container (layer index)`) loads as a plain string and never equals `"feature-surface"`, so it correctly will not trigger the linter's root-inference. Build-safety: 35 valid-YAML frontmatter prepends, no content/link changes, mdBook strips the frontmatter.

**skill-uptake-survey (pass).** No directly-matching skill exists for the graded-stack container-typing pass (this is the first P1 container tranche, deciding a convention rather than applying an established procedure). The dispatch appropriately leans on the scheme page (`graded-stack-scheme.md`) and the linter as its procedural anchors. Telemetry only; non-blocking.

### Issues found

No issues. All eight checks pass; the report is clean.

Two of the report's own flags are verified-correct rather than defects:

1. **Linter detritus-classification gap for the 23 group-intro pages — REAL and correctly routed.** I confirmed against the live linter: `is_likely_outside_dag` recognizes only `*/index` + `FEATURE_NON_COLUMN`, so the 9 layer/lowering indexes + 3 feature group pages + feature/index land in `expected_unreachable_outside_dag` (currently 21), but the 23 `L*/...-intro` group-intro pages do not — once typed-but-unreachable they shift into the `detritus_with_typed_edges_stronger_signal` bucket (currently 63). This is informational lint noise, not an exit-code failure (the linter trips only on rank violations; `rank_violations: 0`), and `tools/` is meta-phase write-authority, not this dispatch's. The recommendation (key `is_likely_outside_dag` off the `kind: navigational-container` tag rather than the brittle `-intro` suffix) is sound — the frontmatter introduced here is the robust signal. Correctly filed as a meta-phase/tools follow-up, not a defect in this dispatch.

2. **D4 / concepts/index alignment divergence-risk — correctly flagged, out of this dispatch's surface.** The report does not touch `concepts/index` (D4's surface) and only flags that the batch-close meta-phase unify should give `concepts/index` the same container treatment by the identical argument. Sound and non-blocking; nothing for this dispatch to change.

I independently reproduced the report's headline metrics against the live linter: current `untyped = 142`, all 35 container slugs are presently untyped, post-typing `untyped = 107` (−35 exact), `rank_violations = 0`. The delta arithmetic and the zero-new-rank-obligation claim are mechanically exact.
