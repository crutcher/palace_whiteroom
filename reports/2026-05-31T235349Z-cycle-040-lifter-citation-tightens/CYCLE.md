---
agent: lifter
invoked_at: 2026-05-31T235349Z
scope: L1>L0 opportunistic citation-range tightens (×2, disjoint files) — floquet M-block comment :25-26→:25 + chebyshev dead-transpose-kernel :101-110→:102-110
status: integrated
integrated_at: 2026-06-01T010000Z
integration_commit: 26b58f6
integration_notes: "Applied clean (D3/3, cycle-040). 2 pure citation-range tightens on firm L1>L0 themes, disjoint files: floquet-correction-mutation-rotation M-block :25-26->:25 (2 edits, drops stale 'theme body line 229' ref + MINOR over-extension flag); chebyshev-smoother-mutation-rotation dead-transpose-kernel :101-110->:102-110 at 3 occurrences (sibling :147-155 untouched). Status firm preserved on both — no structural/signature/status change. Both re-confirmed via citecheck --anchor against reference/. DISCHARGED 2 OQs (closes c038 D4 + c035 D1). No codemap drift."
inputs:
  - book/src/L1-L0/floquet-correction-mutation-rotation.md
  - book/src/L1-L0/chebyshev-smoother-mutation-rotation.md
  - reference/palace/palace/linalg/floquetcorrection.cpp
  - reference/palace/palace/linalg/chebyshev.cpp
---

# CYCLE: Re-anchor — two opportunistic L1>L0 citation-range tightens

## Summary
Two pure citation-range tightens (fired-trigger LOW-fan-out hygiene), in disjoint L1>L0 theme files; no structural change to either lowering. (1) In `floquet-correction-mutation-rotation.md`, the M-block comment citation `palace/linalg/floquetcorrection.cpp:25-26` over-extends one line into the opening brace `{` (on-disk `:25` is the comment, `:26` is `{`) — tightened to `:25`. (2) In `chebyshev-smoother-mutation-rotation.md`, the first dead-code complex conjugate-`dinv` transpose-kernel citation `palace/linalg/chebyshev.cpp:101-110` overshoots its start by one line (on-disk `:101` is the close brace of the *non*-transpose `if constexpr (!Transpose)` branch; the dead `else`-block body is `:102-110`) — tightened to `:102-110` at all three occurrences in the theme (prose §Sub-pattern C, the `verified_against` yaml note, and §Open questions). Both tightens verified on-disk against `reference/` (codemap and on-disk agree at both boundaries; no `read_range`+1 drift observed here) and confirmed via `citecheck --anchor`. Both OQs can be closed at integration.

## Proposed changes

### Tighten 1 — floquet M-block comment `:25-26` → `:25`

```edit:book/src/L1-L0/floquet-correction-mutation-rotation.md
[old]: - `palace/linalg/floquetcorrection.cpp:26-39` — `M_RT` assembly: comment
  `:25-26`, `BilinearForm a(rt_fespace)` `:28`, `VectorFEMassIntegrator` `:29`,
[new]: - `palace/linalg/floquetcorrection.cpp:26-39` — `M_RT` assembly: comment
  `:25`, `BilinearForm a(rt_fespace)` `:28`, `VectorFEMassIntegrator` `:29`,
```

Also update the `verified_against` note that records the (now-fixed) over-extension so the yaml no longer flags a live defect:

```edit:book/src/L1-L0/floquet-correction-mutation-rotation.md
[old]:     note: ctor body; sig :20-23, M assembly :26-39 (ComplexParOperator wrap :33 / dead-code ParOperator :37), Cross assembly :41-57 (MaterialPropertyCoefficient :42, GetFloquetCross :43, ComplexParOperator :50-51 / dead-code :55), ksp+JacobiSmoother :60-66 (CgSolver :60, JacobiSmoother :65), SetOperators(*M,*M) :67, rhs sizing :69-70 — all finer anchors lit (citecheck OK). MINOR — theme body line 229 cites the M-block comment as :25-26 but it is at :25 only (:26 is the opening brace); non-load-bearing over-extension, range :26-39 itself correct.
[new]:     note: ctor body; sig :20-23, M assembly :26-39 (ComplexParOperator wrap :33 / dead-code ParOperator :37), Cross assembly :41-57 (MaterialPropertyCoefficient :42, GetFloquetCross :43, ComplexParOperator :50-51 / dead-code :55), ksp+JacobiSmoother :60-66 (CgSolver :60, JacobiSmoother :65), SetOperators(*M,*M) :67, rhs sizing :69-70 — all finer anchors lit (citecheck OK). M-block comment anchored at :25 (the comment line; :26 is the opening brace) — tightened from the earlier :25-26 over-extension (cycle-040 D3).
```

### Tighten 2 — chebyshev first dead-transpose-kernel `:101-110` → `:102-110` (all 3 occurrences)

Occurrence A — §Sub-pattern C prose:

```edit:book/src/L1-L0/chebyshev-smoother-mutation-rotation.md
[old]: complex conjugate-`dinv` transpose kernels exist
(`palace/linalg/chebyshev.cpp:101-110, :147-155`) but are dead code under the
[new]: complex conjugate-`dinv` transpose kernels exist
(`palace/linalg/chebyshev.cpp:102-110, :147-155`) but are dead code under the
```

Occurrence B — `verified_against` yaml citation + note:

```edit:book/src/L1-L0/chebyshev-smoother-mutation-rotation.md
[old]:   - citation: palace/linalg/chebyshev.cpp:101-110,147-155
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: dead-code complex conjugate-dinv transpose kernels (recognition rules); second-kernel range tightened from :150-159 to :147-155 (cycle-035 D1)
[new]:   - citation: palace/linalg/chebyshev.cpp:102-110,147-155
    verdict: supports
    audited_at: 2026-05-28T19:33:25Z
    note: dead-code complex conjugate-dinv transpose kernels (recognition rules); first-kernel start tightened from :101-110 to :102-110 (:101 is the close brace of the non-transpose if-branch; the dead else-block is :102-110) (cycle-040 D3); second-kernel range tightened from :150-159 to :147-155 (cycle-035 D1)
```

Occurrence C — §Open questions bullet:

```edit:book/src/L1-L0/chebyshev-smoother-mutation-rotation.md
[old]: - **Dead-code complex transpose kernels.** `palace/linalg/chebyshev.cpp:101-110,
  :147-155` define conjugate-`dinv` transpose elementwise kernels that are
[new]: - **Dead-code complex transpose kernels.** `palace/linalg/chebyshev.cpp:102-110,
  :147-155` define conjugate-`dinv` transpose elementwise kernels that are
```

## Discipline notes
- **Pure citation-range tighten, no structural change.** Both lowerings keep their L1 LHS, L0 RHS, sub-pattern decomposition, applicability conditions, and `firm` status. Only the cited byte-ranges firm up. No re-architecting, no signature change, no prose-correction beyond the citation ranges themselves (the §Sub-pattern C / §Open-questions prose surrounding the chebyshev range is unchanged in substance).
- **Tighten 1 (floquet):** on-disk `reference/palace/palace/linalg/floquetcorrection.cpp:25` is `// Create the mass and cross product operators for Floquet correction.`; `:26` is the opening brace `{` of the M-assembly scope block. The citation labelled `:25-26` as "comment" but only `:25` is the comment. Tightened to `:25`. The enclosing range `:26-39` (the M-assembly body) is itself correct and untouched. I also folded the `verified_against` note that had recorded this as a live `MINOR` over-extension, so the yaml no longer carries a now-stale defect flag.
- **Tighten 2 (chebyshev):** on-disk `reference/palace/palace/linalg/chebyshev.cpp:93` is `if constexpr (!Transpose)`, lines `:94-101` are the non-transpose branch (close brace `}` at `:101`), `:102` is `else`, and `:102-110` is the dead conjugate-transpose `else`-block body (close brace `}` at `:110`). The citation `:101-110` overshot the start by including `:101` (the close brace of the *preceding* non-transpose branch), which is not part of the dead kernel. Tightened to `:102-110`. The sibling second-kernel range `:147-155` was already correct (cycle-035 D1) and is left untouched; I verified it still lights its `else` anchor at its range-start line `:147`. Re-anchored at all three theme occurrences (prose, yaml, OQ) to keep the citation consistent across the file per the `verify-citation-range` sibling-consistency discipline.
- **Codemap vs on-disk (`codemap-read-range-plus-one-drift-on-brace-boundary` guard in force):** for the floquet boundary I cross-checked codemap `read_range(24-30)` against a direct on-disk `Read` of `floquetcorrection.cpp:23-31`; the two **agreed** (`:25`=comment, `:26`=`{`) — no +1 drift on this boundary. For the chebyshev boundary I read on-disk directly. Every emitted `path:lo-hi` was confirmed by `citecheck --anchor` against the on-disk `reference/` file (the source of truth), not off codemap output.

## Supporting evidence
- `citecheck` (on-disk `reference/` source of truth):
  - `palace/linalg/floquetcorrection.cpp:25` `--anchor 'Create the mass and cross product operators'` → `[ok] anchor at line(s) [25] within range 25-25`.
  - `palace/linalg/chebyshev.cpp:102-110` `--anchor 'else'` → `[ok] anchor at line(s) [102] within range 102-110` (anchor sits exactly at the tightened range-start; the old `:101-110` put the `else` anchor at line 102, i.e. one inside the range, confirming `:101` is a non-anchor over-extension line).
  - `palace/linalg/chebyshev.cpp:147-155` `--anchor 'else'` → `[ok] anchor at line(s) [147] within range 147-155` (sibling second kernel, left untouched, still correct).
- On-disk confirmations: `floquetcorrection.cpp:23-31` (`:25` comment, `:26` `{`); `chebyshev.cpp:84-111` (`:93` `if constexpr (!Transpose)`, `:101` non-transpose close `}`, `:102` `else`, `:102-110` dead transpose body, `:110` close `}`).

## Open questions / caveats
- Both target OQs **can be closed at integration**:
  - `floquet-mutation-rotation-m-block-comment-citation-over-extension` — resolved by Tighten 1 (`:25-26`→`:25`).
  - `chebyshev-smoother-mutation-rotation-applyorder0-true-citation-tighten-sibling` — resolved by Tighten 2 (`:101-110`→`:102-110`); the sibling `:147-155` was already firm from cycle-035 D1.
- No structural caveat surfaced; no abstractor reread needed. Neither tighten touched the lowering decomposition, signatures, or status.
