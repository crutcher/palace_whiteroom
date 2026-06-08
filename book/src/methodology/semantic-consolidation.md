# Methodology — Semantic consolidation (the active-management semantic surface)

> **⟢ NON-AUTHORITATIVE — reader-facing mirror; a review point, not a source.**
>
> This chapter is a **reader-facing exposition** of the project's semantic-consolidation
> discipline. It is **not** a directive source. The authoritative statement is the
> 2026-06-06 user directive, distilled operationally in `CLAUDE.md` §Methodology
> invariants ("SEMANTIC CONSOLIDATION"); the discipline itself lives on the
> [semantic surface](../semantics/index.md) (§0.1).
>
> **If this chapter contradicts `CLAUDE.md` or the semantic surface's §0.1, those win
> and this chapter is corrected.** A contradiction surfacing here is a *drift signal*,
> not a decision to adjudicate.

## What this is

Semantic definitions — the rules, definitions, and abstractions **about the language
and the spec itself** (as opposed to the domain vocabulary of operators and lowering
themes) — are a **first-class, actively-managed surface**. They are held under the
**same liveness / unification / consolidation discipline** that the
[graded resolution ladder & reachability](./resolution-ladder.md) machinery applies to
the *vocabulary*. The two disciplines are deliberately parallel:

| Vocabulary (graded stack) | Semantics (this discipline) |
|---|---|
| An operator/theme lives in its layer Part | A semantic rule/def/abstraction lives **once**, on the semantic surface |
| A degenerate identity-in-named-terms lowering is a **smell** | A general semantic rule **restated at a functional-unit scope** is a **smell** |
| An unreachable node is **detritus** — GC it (ground / route / remove) | A duplicated semantic rule is the semantic detritus — **relocate to the surface + back-link** |
| Resolve a smell by combinator re-expression / in-line note | Resolve a restatement by **relocation-to-the-surface + a back-link** |

## The surface

The single home for the spec's semantics is
[**L4 calculus & spec semantics**](../semantics/index.md) — promoted (2026-06-06) out
of its former "design strawman" status into the project's **active-management semantic
surface**. It holds: the calculus grammar (types / shapes / terms), the shape semantics
including **named shape groups** (`Tensor[(S: ...)]` binding / `Tensor[$S]` use), the
**L4/L3 pseudo-language notation invariant** (Haskell `::` signatures, TS
`{ field: type }` records, do-notation bodies, `$$` math for reduction rules), and the
monad / ownership / reduction-rule / scalar-promotion conventions.

In `SUMMARY.md` it sits under the top-level `# Semantic surface — calculus, rules &
abstractions` Part, placed **before the `# L4` Part** — it defines the language the
layers are written in, so it is read first.

## The rule: USE + LINK, don't RE-STATE

A semantic rule/def/abstraction lives **once**, on the surface. A functional-unit entry
(an operator chapter, a lowering theme, a layer-intro, a concept page) that needs a
general semantic rule:

- keeps its **own concrete fact** (e.g. "`axpy` is whole-tensor shape-congruent:
  `Tensor[(S: ...)] → ...`"), and
- **links** to the governing section on the surface (e.g. "see §1.2.1");
- it does **not** transcribe the general teaching (the binding/use syntax, the
  anti-pattern explanation, the migration note).

A general rule found restated at a functional-unit scope is the **semantic analog of a
degenerate identity-lowering smell or an un-grounded detritus node**. It is resolved by
**relocation to the surface + a back-link**, not by leaving the duplication in place.

## Active management — how it stays live

The surface's §0.1 carries the operative discipline; in summary:

- **Authoring + relocation sweeps** are owned by `layer-intro-author` (the surface's
  authoring role).
- **Surfacing restatement cohorts** is done by the cross-cutters (`same-layer-cross-cutter`
  especially) — a restatement-cohort is surfaced the same way a unification opportunity
  is.
- **Every-batch liveness / unification refresh** is a standing duty of the `meta-phase`
  (the semantic analog of the graded-stack GC sweep): re-check the surface against the
  authoritative sources, migrate any new restatement-cohort sweep into the plan, and
  confirm newly-mined general semantic abstractions earned a consolidated home.

The named-shape-groups general rule lives once on the surface (§1.2.1) with the
functional-unit entries (the `linear_combination` cohort and the broader
named-shape-groups cohort) using + linking it rather than restating it — the founding
sweep governed by this discipline.
