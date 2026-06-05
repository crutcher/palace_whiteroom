---
agent: lifter
invoked_at: 2026-06-05T06:28:48Z
scope: L4>L3 theme citation-hygiene full-path pass — fe-assemble-fold-dissolution
status: pending
inputs:
  - book/src/L4-L3/fe-assemble-fold-dissolution.md
  - palace/fem/integrator.hpp:58-61
  - palace/fem/libceed/operator.cpp:455
integrated_at: 2026-06-05T070500Z
integration_commit: 45b7d854bb1f9b9bbfe4bdf93fe8d3b69a089f95
integration_notes: >
  Applied clean (cycle-102 D2, staging row 2). 5 inline-prose citations in
  L4-L3/fe-assemble-fold-dissolution.md full-path-disambiguated (integrator.hpp:58-61 AMBIG →
  palace/fem/integrator.hpp:58-61; libceed/operator.cpp:455 MISS → palace/fem/libceed/operator.cpp:455).
  All-pass clean (no repair phase ran). Build green (cargo make book EXIT 0); citecheck on the
  landed file 16 ok / 0 failing (the 2 pre-existing AMBIG/MISS flags now both resolve [ok]).
  step-5b rank_violations: 0 (no nodes/edges added — pure citation-path repointing; theme stays
  firm). No OQs. Batch-32 BATCH-CLOSING cycle; the batch-32 meta-phase fires next.
---

# CYCLE: Re-anchor fe-assemble-fold-dissolution (citation full-path disambiguation)

## Summary
Pure citation-format firm-up of `book/src/L4-L3/fe-assemble-fold-dissolution.md` (cycle-102 D2). Two pre-existing citecheck basename-ambiguity flags are disambiguated to their full paths in the theme's **inline prose**: `integrator.hpp:58-61` → `palace/fem/integrator.hpp:58-61` (the `BilinearFormIntegrator::Assemble` pure-virtual leaf-kernel contract; AMBIG competitor `fem/libceed/integrator.hpp` is `AssembleCeedOperator`, NOT what's cited) and `libceed/operator.cpp:455` → `palace/fem/libceed/operator.cpp:455` (`CeedOperatorFullAssemble`). The disambiguating prefix is `palace/fem/...` (NOT the dispatch's literal `fem/...`): `palace/fem/...` is the form that BOTH disambiguates the basename collision AND resolves under `citecheck` (the on-disk repo layout is `reference/palace/palace/fem/...`); the bare `fem/...` form `[MISS]`es under citecheck. This also matches the file's own §Evidence section-header convention (lines 195/197 already write `palace/fem/libceed/operator.cpp` / `palace/fem/integrator.hpp`). Five inline-prose occurrences across three paragraphs (lines 86, 102, 106 ×2, 126) are repointed; the §Evidence sub-bullets at lines 196/198 already carry the full disambiguating paths in their section headers and are NOT ambiguous, so they stay as-is. No claim, rotation, law, verdict, or status changes — the theme stays `firm`. All citation text is inline-code backticks (build-safe; no markdown links).

## Re-confirmation against source (this dispatch)

Both targets re-confirmed via codemap `read_range` AND `citecheck --anchor` against on-disk, no drift:

- `palace/fem/integrator.hpp:58-61` — `BilinearFormIntegrator::Assemble` pure-virtual (`virtual void Assemble(Ceed ceed, CeedElemRestriction trial_restr, ... CeedOperator *op) const = 0;`). `citecheck --anchor 'Assemble'` → anchor at line 58 within range 58-61, zero-drift. This is the pure-virtual dispatch target cited; the basename competitor `fem/libceed/integrator.hpp` (`AssembleCeedOperator`) is a different construct.
- `palace/fem/libceed/operator.cpp:455` — `CeedOperatorFullAssemble` function signature (`std::unique_ptr<hypre::HypreCSRMatrix> CeedOperatorFullAssemble(const Operator &op, bool skip_zeros, bool set)` opening at line 455). `citecheck --anchor 'CeedOperatorFullAssemble'` → anchor at line 455 within range 455-455, zero-drift.

No drift found in either target; both line-ranges carry exactly the cited content. This is purely a path-prefix disambiguation, not a line re-anchor.

## Proposed changes

```edit:book/src/L4-L3/fe-assemble-fold-dissolution.md
[old]: - **`assemble_term_leaf ...`** is the per-term `integ->Assemble(ceed, trial_restr, test_restr, trial_basis, test_basis, geom_data, geom_data_restr, &sub_op)` call (`bilinearform.cpp:75`) — the pure-virtual dispatch (`integrator.hpp:58-61`) into the **libCEED element-local quadrature kernel**.
[new]: - **`assemble_term_leaf ...`** is the per-term `integ->Assemble(ceed, trial_restr, test_restr, trial_basis, test_basis, geom_data, geom_data_restr, &sub_op)` call (`bilinearform.cpp:75`) — the pure-virtual dispatch (`palace/fem/integrator.hpp:58-61`) into the **libCEED element-local quadrature kernel**.
```

```edit:book/src/L4-L3/fe-assemble-fold-dissolution.md
[old]: The L4 opaque quantified-over `assemble_term` dissolves into the concrete per-term library CALL `integ->Assemble(...)` (`bilinearform.cpp:75`) — the pure-virtual dispatch (`integrator.hpp:58-61`) into the **libCEED element-local quadrature kernel**.
[new]: The L4 opaque quantified-over `assemble_term` dissolves into the concrete per-term library CALL `integ->Assemble(...)` (`bilinearform.cpp:75`) — the pure-virtual dispatch (`palace/fem/integrator.hpp:58-61`) into the **libCEED element-local quadrature kernel**.
```

```edit:book/src/L4-L3/fe-assemble-fold-dissolution.md
[old]: The per-term body bottoms out in an **opaque element-local quadrature kernel that lives entirely outside Palace** — Palace's `integ->Assemble` (`bilinearform.cpp:75`) is a pure-virtual dispatch (`integrator.hpp:58-61`) that builds a `CeedOperator` encapsulating the element-local quadrature contraction (basis evaluation at quadrature points, geometric-factor / coefficient weighting, contract-back to element dofs); that contraction runs **inside libCEED**. The full-assemble materialization (`CeedOperatorFullAssemble`, `libceed/operator.cpp:455`) similarly extracts the assembled entries via the libCEED `CeedOperatorAssembleCOO` API
[new]: The per-term body bottoms out in an **opaque element-local quadrature kernel that lives entirely outside Palace** — Palace's `integ->Assemble` (`bilinearform.cpp:75`) is a pure-virtual dispatch (`palace/fem/integrator.hpp:58-61`) that builds a `CeedOperator` encapsulating the element-local quadrature contraction (basis evaluation at quadrature points, geometric-factor / coefficient weighting, contract-back to element dofs); that contraction runs **inside libCEED**. The full-assemble materialization (`CeedOperatorFullAssemble`, `palace/fem/libceed/operator.cpp:455`) similarly extracts the assembled entries via the libCEED `CeedOperatorAssembleCOO` API
```

```edit:book/src/L4-L3/fe-assemble-fold-dissolution.md
[old]: Both compute the same operator *action*; the representation choice is a Palace-owned variant axis on the firm fold (already absorbed at L1, the L1 cap §"assembly-representation" axis), not part of this fold-shell rotation. The COO→CSR materialization (`CeedOperatorFullAssemble`, `libceed/operator.cpp:455`) is the `full` realization of the leaf, recorded by the L1>L0 obstruction annotation.
[new]: Both compute the same operator *action*; the representation choice is a Palace-owned variant axis on the firm fold (already absorbed at L1, the L1 cap §"assembly-representation" axis), not part of this fold-shell rotation. The COO→CSR materialization (`CeedOperatorFullAssemble`, `palace/fem/libceed/operator.cpp:455`) is the `full` realization of the leaf, recorded by the L1>L0 obstruction annotation.
```

## Discipline notes
- **Pure citation-format firm-up, lifter mandate.** Every edit repoints a bare-basename `path:lo-hi` to its full disambiguating path. The theme's structure, claims, rotation, four algebraic laws, the map-not-fold guard, the DISSOLUTION-HOME verdict, and the `firm` status all stay verbatim. Nothing but the path prefix changes. No abstractor reread needed — the signatures the citations point at are unchanged (re-confirmed identical content at the cited ranges this dispatch).
- **Why `palace/fem/...` (not the dispatch's literal `fem/...`):** codemap-confirmed that `palace/fem/integrator.hpp:58-61` is the `BilinearFormIntegrator::Assemble` pure-virtual (`... CeedOperator *op) const = 0;`) — the exact construct the theme cites as "the pure-virtual dispatch into the libCEED element-local quadrature kernel". The basename competitor `fem/libceed/integrator.hpp` is `AssembleCeedOperator`, a different symbol the theme does not cite. `palace/fem/libceed/operator.cpp:455` is `CeedOperatorFullAssemble`, the COO→CSR materialization the theme names by symbol at every occurrence. **Deviation from the dispatch's literal target, citecheck-driven:** the dispatch named `fem/integrator.hpp:58-61` / `fem/libceed/operator.cpp:455`, but `citecheck` (the citation source-of-truth) rules the bare `fem/...` form a `[MISS]` (the on-disk repo layout is `reference/palace/palace/fem/...`; the `palace/`-relative-to-`reference/` form is what resolves). The `palace/fem/...` form is the minimal prefix that BOTH disambiguates the basename collision AND resolves under citecheck — and it matches the file's own §Evidence section-header convention (lines 195/197). Per the lifter discipline "citecheck/on-disk wins when the stated target disagrees", I emitted the resolving form. Re-confirmed: `citecheck 'palace/fem/integrator.hpp:58-61'` → ok; `citecheck 'palace/fem/libceed/operator.cpp:455'` → ok.
- **§Evidence sub-bullets (lines 196, 198) intentionally NOT touched.** They use the `:455` / `:58-61` short form scoped under full-path section headers (`palace/fem/libceed/operator.cpp` line 195, `palace/fem/integrator.hpp` line 197), so they are already unambiguous in context; repointing them would be redundant and would break the header-then-sub-bullet citation pattern the §Evidence block uses throughout.
- **Build-safety confirmed.** All five repointed citations are inline-code spans (single backticks), not markdown links `[..](..)`; `linkcheck2` does not parse them as links, so the path change cannot create a dangling link. No `book/src/` write performed by this dispatch (DISPATCH-phase discipline) — changes emitted as proposed-changes blocks only.

## Supporting evidence
- `book/src/L4-L3/fe-assemble-fold-dissolution.md` — the theme re-anchored (5 inline-prose occurrences at lines 86, 102, 106 ×2, 126).
- codemap `read_range` palace/fem/integrator.hpp:58-61 → `BilinearFormIntegrator::Assemble` pure-virtual (this dispatch).
- codemap `read_range` palace/fem/libceed/operator.cpp:452-458 → `CeedOperatorFullAssemble` signature at 454-455 (this dispatch).
- `tools/citecheck/citecheck.py 'palace/fem/integrator.hpp:58-61' --anchor 'Assemble'` → ok, anchor line 58 in range, zero-drift.
- `tools/citecheck/citecheck.py 'palace/fem/libceed/operator.cpp:455' --anchor 'CeedOperatorFullAssemble'` → ok, anchor line 455 in range, zero-drift.

## Open questions / caveats
None. The formalized signatures at both targets exactly match what the theme assumed (pure-virtual leaf-kernel contract + COO→CSR materialization); this is a path-prefix disambiguation only, with no signature shift and no contradiction. No abstractor rerun warranted.
