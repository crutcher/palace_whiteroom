---
verifies: ../CYCLE.md
critiqued_at: 2026-06-05T22:47:02Z
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

# META: verification of "concepts/counter-update node typing"

## Critique

This report is a **graded-stack NODE-typing** dispatch: it prepends a `rank: firm` + `edges:`
frontmatter block to an existing concept page (`book/src/concepts/counter-update.md`), changing
no body prose. It resolves OQ `concepts-counter-update-needs-node-rank-and-depends-on-edges`. The
checklist is read through the node-typing lens (the page's claim content is its existing,
already-integrated body; this dispatch adds typing metadata + edge classifications).

### Checks run

**citation-validity — pass.** Every load-bearing pinpoint was anchor-verified mechanically with
`citecheck.py --anchor`, all `OK` (no `[DRIFT]`): `preconditioning-framework.md:201` (`modifyCounters`),
`L3/krylov-step.md:64` (`counter-update`), `counter-update.md:5-12` (`counter_update` L2 form),
`dependency-map.md:131` (`counter-update`). The `dependency-map.md:131` line reads verbatim
`counter-update -.->|ref| state-stratification`, exactly as the report quotes — the "already wired
`ref`" claim is true. The reciprocal-link line numbers in the §2 table (`:201`, `:64`) are accurate.
The linter BEFORE/AFTER table was independently reproduced (see cross-reference-integrity): exact
match. No fabricated citations; the report explicitly declines to invent a `cites-evidence` edge for
a non-existent L0 struct, which is the citation-honest call.

**surface-or-evidence — pass.** This is the central focus area. The `rank: firm` justification rests
on the **firm-on-positive-structure / syntactic-identity escape** (CLAUDE.md §`rough-in
(test-coverage-bounded)`): the page's `## L2 form` is fully specified positive source
(`c ← c + δ`, explicit `&mut` in-place semantics, `counter-update.md:5-12`), and the laws are
syntactic identities on that fully-specified form (integer increment), so no surrounding test gates
them — this is the `apply_linop` situation, NOT the `eigsolve`-convergence situation. The escape is
applied correctly: an in-place scalar increment is genuinely a syntactic identity, not a
semantically-loaded claim awaiting empirical confirmation. The record-definition sub-check does NOT
fire: `counter-update` is typed `kind: primitive` (a verb, in-place increment), not a record/struct
naming a `{field: type}` shape — the report explicitly reasons this and it is correct. No surface
gap.

**rotation-quality — pass (not applicable to node-typing dispatch).** This dispatch asserts no new
algebraic/structural rotation — it adds typing metadata to an already-integrated concept page whose
L2-form content is unchanged. No L_{n+1}→L_n compaction claim is made, so the rotation check no-ops
(analogous to the stub/feature-surface no-op). The existing page's iteration-counter/iterate
separation is prior settled content, not a claim of this report.

**variant-axis-coverage — pass.** `counter-update` is a single scalar-increment primitive with no
orthogonal variant axes (no preconditioner-present/absent, no in-place/out-of-place fork — it is
definitionally in-place). Nothing to cover or scope out.

**cross-reference-integrity — pass.** All three `reference:` targets resolve on-disk
(`concepts/state-stratification.md`, `L4/preconditioning-framework.md`, `L3/krylov-step.md` — all
confirmed present). The maturity claim "`preconditioning-framework` (firm)" was verified: that page
carries `rank: firm` on-disk. The linter table was reproduced from a clean tree: BEFORE
`0 rank violation(s), 163 detritus, 61 untyped` (exact match), and AFTER (temporarily applying the
proposed frontmatter, then reverting — tree confirmed clean, no diff persisted)
`0 rank violation(s), 164 detritus, 60 untyped`, with `counter-update` appearing as
`[garbage?] concepts/counter-update` — exactly the report's claimed AFTER row. `rank_violations`
held 0, `reachable` held 95→95, `unresolved depends-on` held 0. No broken link, no maturity
overclaim.

**edge-label-fidelity — pass.** This is the crux focus area, and the report's central departure from
the OQ recommendation is **correct**. The OQ recommended `depends-on (kind: classifies) →
state-stratification`; the report down-types it to `reference`. I verified the well-foundedness
reasoning end-to-end: (1) `state-stratification.md` frontmatter carries only `edges: reference:` and
**no `rank:` line** (confirmed by grep — "NO rank: line") — it is genuinely a non-node. (2) A `firm`
(rank-3) node taking a *blocking* `depends-on` on a no-rank node is exactly the well-foundedness
murk the scheme forbids (`rank(u) ≤ rank(v)` is undefined when `v` has no rank). The report's claim
that the `depends-on` would "violate well-foundedness" is therefore confirmed — `reference` is the
honest, scheme-consistent typing, and it is consistent with the pre-existing derived `ref` edge at
`dependency-map.md:131`. The two reciprocal `reference` edges to the use-sites
(`preconditioning-framework`, `krylov-step`) are correctly characterized as navigational inbound
references, carrying no liveness — faithful to the §3 `reference` semantics. Edge prose matches edge
labels throughout.

**plan-kind-consistency — pass.** This is the third focus area. The declared kind (node-typing /
graded-stack audit) matches the content shape: frontmatter typing + edge-classification table, no
semantics authoring. The report **honestly declines to force reachability** — `counter-update` stays
`[garbage?]` (NOT reachable), and the report explicitly refuses to manufacture a `depends-on` to
make it live, citing the "note honestly, don't force" discipline and the §3 liveness semantics. This
is the correct discipline: liveness is a measured property, not something a single page-typing
dispatch should fabricate. Leaving `depends-on: []` is faithful — the page cites no L0 backing
struct, so there is no genuine blocking dependency to record, and inventing a `cites-evidence` edge
would be a fabricated citation. The `firm` rank is honestly supported by the page content (fully-
specified L2 form + ≥2 real consumers + syntactic-identity laws), not inflated to chase
reachability. No mis-classification.

**skill-uptake-survey — pass (telemetry).** The report invokes `graded_stack_lint.py` (the rank +
reachability linter) and reasons explicitly in graded-stack-scheme terms. No dedicated node-typing
skill is implied beyond the linter, which is referenced and run. Pure presence check; nothing
missing.

### Issues found

None. The ≥2-consumer claim was independently verified by grep: `counter-update` is referenced by
`L4/preconditioning-framework.md:201` (firm), `L3/krylov-step.md:64`,
`L4-L3/krylov-step-typed-wrapper-dissolution.md:83`, and `L1-L0/ksp-solve-mutation-rotation.md:130`
— four real on-disk consumers, comfortably ≥2. The central well-foundedness reasoning (firm node
cannot take a blocking `depends-on` on the no-rank `state-stratification` non-node) is confirmed
correct on disk. The honest non-forcing of reachability is the right discipline. The linter
BEFORE/AFTER table reproduced exactly. All eight checks pass; this is a clean report. (Note: the
report's caveat that `state-stratification` arguably warrants promotion to a rank-bearing node in a
future P1 pass is a sound forward observation, correctly scoped out of this one-page-per-invocation
dispatch and not requiring a new OQ — it is a known consequence of the c103/c107 taxonomy-page
non-node encoding.)
