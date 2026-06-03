---
agent: lifter
invoked_at: 2026-06-03T045739Z
integrated_at: 2026-06-03T055824Z
integration_commit: 497cb76
integration_notes: "cycle-075 D5 (LOW hygiene). Applied clean — pure mechanical token re-anchor: 6 stale CHILD-status cross-refs seed (exemplar) -> bare seed in feature/lifecycle.L4.md (2 composes:-list descriptors :7,:8 + 2 dep-map cells :57,:58) + lifecycle.L1.md (2 dep-map cells :56,:57), mirroring the children's authoritative bare status: seed. Descriptive prose preserved; the lifecycle file's own bare seed token untouched. DISCHARGES OQ feature-column-child-status-reference-drift-in-lifecycle-depmap; opens NEW LOW OQ feature-column-self-status-qualifier-drift-in-prose (electrostatic.L1.md:65 self-qualifier, distinct sub-kind, out of scope). Build-safe (status-cell text not link-checked). citecheck 9 ok / 0 fail. retroactive 0. cargo make book exit 0, linkcheck2 clean."
scope: lifecycle ROOT feature column — child-status token micro-sweep (re-anchor stale `seed (exemplar)` child cross-refs → bare `seed`)
status: pending
inputs:
  - book/src/feature/lifecycle.L4.md
  - book/src/feature/lifecycle.L1.md
  - book/src/feature/electrostatic.L4.md (child whose status token is referenced)
  - book/src/feature/magnetostatic.L4.md (child whose status token is referenced)
  - book/src/feature/electrostatic.L1.md (child whose status token is referenced)
  - book/src/feature/magnetostatic.L1.md (child whose status token is referenced)
---

# CYCLE: Re-anchor lifecycle ROOT feature column — child-status token micro-sweep

## Summary
The lifecycle ROOT feature column's dep-maps and `composes:` list carry stale CHILD-status cross-references describing its electrostatic / magnetostatic child columns as `seed (exemplar)`. Those child columns were normalized to bare `seed` in c074 D5 (confirmed: `electrostatic.{L4,L1}.md:5` and `magnetostatic.{L4,L1}.md:5` all read `status: seed`), so the parent's annotations drifted (OQ `feature-column-child-status-reference-drift-in-lifecycle-depmap`). This is a pure re-anchor: re-token the 6 stale child-status cross-refs → bare `seed`. No prose, no structure, no signatures change. Build-safe (status-cell text and `composes:`-comment text are not link-checked). The OQ is discharged by this sweep.

## Proposed changes

```edit:book/src/feature/lifecycle.L4.md
[old]:   - book/src/feature/electrostatic.L4.md (seed (exemplar) — the ELECTROSTATIC ProblemType specialization)
  - book/src/feature/magnetostatic.L4.md (seed (exemplar) — the MAGNETOSTATIC ProblemType specialization)
[new]:   - book/src/feature/electrostatic.L4.md (seed — the ELECTROSTATIC ProblemType specialization)
  - book/src/feature/magnetostatic.L4.md (seed — the MAGNETOSTATIC ProblemType specialization)
```

```edit:book/src/feature/lifecycle.L4.md
[old]:| dispatch → electrostatic column | [`electrostatic.L4`](./electrostatic.L4.md) | seed (exemplar) | `palace/main.cpp:267` |
| dispatch → magnetostatic column | [`magnetostatic.L4`](./magnetostatic.L4.md) | seed (exemplar) | `palace/main.cpp:270` |
[new]:| dispatch → electrostatic column | [`electrostatic.L4`](./electrostatic.L4.md) | seed | `palace/main.cpp:267` |
| dispatch → magnetostatic column | [`magnetostatic.L4`](./magnetostatic.L4.md) | seed | `palace/main.cpp:270` |
```

```edit:book/src/feature/lifecycle.L1.md
[old]:| per-driver dispatch (electrostatic) | [`electrostatic.L1`](./electrostatic.L1.md) | seed (exemplar) | `palace/main.cpp:267` |
| per-driver dispatch (magnetostatic) | [`magnetostatic.L1`](./magnetostatic.L1.md) | seed (exemplar) | `palace/main.cpp:270` |
[new]:| per-driver dispatch (electrostatic) | [`electrostatic.L1`](./electrostatic.L1.md) | seed | `palace/main.cpp:267` |
| per-driver dispatch (magnetostatic) | [`magnetostatic.L1`](./magnetostatic.L1.md) | seed | `palace/main.cpp:270` |
```

## Discipline notes
- Pure re-anchor (lifter mandate): only the drifted `seed (exemplar)` CHILD-status tokens are changed → bare `seed`. The lifecycle file's own `status:` token (`lifecycle.{L4,L1}.md:5`) was already normalized in c074 D5 and is untouched. Descriptive prose around each token is preserved verbatim (e.g. "the ELECTROSTATIC ProblemType specialization", "per-driver dispatch (electrostatic)").
- The re-token is justified by reading the children's authoritative `## Status` / frontmatter tokens on disk: `book/src/feature/electrostatic.L4.md:5` = `status: seed`, `magnetostatic.L4.md:5` = `status: seed`, `electrostatic.L1.md:5` = `status: seed`, `magnetostatic.L1.md:5` = `status: seed`. The parent's cross-references must mirror the child's authoritative token; they had drifted. This is a status-cell-mirror correction, the index-cell-drift class formalized in the c057 `index-table-status-cell-drifts-when-theme-file-promoted` friction guard, applied here to a feature-column dep-map / `composes:`-list cross-reference (the same hand-maintained-derived-surface drift, one tier over).
- `lifecycle.L0.md` carries no `seed (exemplar)` / `seed (composition-root)` tokens (grep returned nothing) — no L0 edit needed.
- No L0-evidence-driven prose correction was needed; this is token re-anchoring only.

## Supporting evidence
- Grep `seed (exemplar)|seed (composition-root)` across `lifecycle.{L4,L1,L0}.md` → exactly the 6 scoped loci (L4: 7, 8, 57, 58; L1: 56, 57), all matching the dispatch's `~:` estimates. No additional drift inside the lifecycle column.
- Child authoritative tokens: `electrostatic.L4.md:5`, `magnetostatic.L4.md:5`, `electrostatic.L1.md:5`, `magnetostatic.L1.md:5` all `status: seed`.
- OQ `feature-column-child-status-reference-drift-in-lifecycle-depmap` is discharged by this re-token (all 6 lifecycle cross-refs re-anchored to the children's bare-`seed` authoritative tokens).

## Open questions / caveats
- **Additional same-class residual drift, out of scope, NOT fixed here:** `book/src/feature/electrostatic.L1.md:65` contains a self-referential status assertion in *descriptive prose* — "consistent with the column being a `seed (exemplar)`, not a firm composition". This is (i) in a different feature column (electrostatic, not lifecycle), (ii) descriptive prose narrating the seed-tier rationale, NOT a dep-map status cell or a `composes:` cross-ref token, and (iii) outside my scoped loci. Per the dispatch directive ("Edit ONLY the drifted child-status tokens … leave descriptive prose"; "don't necessarily fix beyond your scoped loci unless trivial"), I left it untouched. It is borderline — it is a stale `seed (exemplar)` token, but it is prose-embedded and self-referential rather than a cross-reference cell. A follow-up micro-pass (or the c074 D5 normalizer's owner) should decide whether the electrostatic column's own prose should drop the `(exemplar)` qualifier to match its now-bare `status: seed` frontmatter. Flagging for OQ append (see below); not blocking this sweep.
- No signature / decomposition / convention change surfaced — pure rewrite, no abstractor reread warranted.

## OQ ledger note
Recommend appending to `scaffolding/open-questions.md` (integrator-per-report, append-only):
- DISCHARGE `feature-column-child-status-reference-drift-in-lifecycle-depmap` (c075 D5: all 6 lifecycle.{L4,L1} child-status cross-refs re-anchored `seed (exemplar)` → bare `seed`).
- NEW (low-priority residual): `feature-column-self-status-qualifier-drift-in-prose` — `electrostatic.L1.md:65` prose still self-describes the column as `seed (exemplar)` though its frontmatter is bare `status: seed` (c074 D5 normalization). Prose-embedded, self-referential; left for a follow-up prose-correction pass. Class-sibling of the discharged lifecycle dep-map drift.
