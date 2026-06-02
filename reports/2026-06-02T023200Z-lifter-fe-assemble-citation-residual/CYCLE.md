---
agent: lifter
invoked_at: 2026-06-02T02:32:00Z
scope: L1 fe_assemble citation residual — laplaceoperator.cpp:215-217 → :216-217 (2 occurrences)
status: pending
inputs:
  - book/src/L1/fe_assemble.md
  - reference/palace/palace/models/laplaceoperator.cpp:213-218 (ground-truth re-read on-disk)
integrated_at: 2026-06-02T040000Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-056 D3 (build-relevant). Citation-hygiene fix applied to book/src/L1/fe_assemble.md: essential-BC pinpoint laplaceoperator.cpp:215-217 -> :216-217 at TWO occurrences (line 147 full-path form + line 257 abbreviated form); :215 is a stray closing brace, :216=ParOperator construction, :217=SetEssentialTrueDofs; on-disk re-read confirmed. The legitimate :184-223 GetStiffnessMatrix broader span deliberately NOT touched. No fence/body change. Build: cargo make book exit 0; fe_assemble.html renders with :216-217 (2 occurrences, 0 stray :215-217). Closes the cycle-055 deferred fe_assemble.md:147 citation-residual OQ. NO count delta."
---

# CYCLE: Re-anchor fe_assemble citation residual (laplaceoperator.cpp:215-217 → :216-217)

## Summary
Citation-hygiene fix on `book/src/L1/fe_assemble.md`: the `eliminate_essential_bc` /
`ParOperator::SetEssentialTrueDofs` site was cited as `laplaceoperator.cpp:215-217`, but `:215` is a
stray closing brace `}` (it closes the inner `Mpi::Print` block), NOT part of the essential-BC site.
The BC site is the `ParOperator` construction (`:216`) + `SetEssentialTrueDofs(...)` (`:217`), so the
range should start at `:216`. The cycle-055 hand-off said "1 place" but the cycle-056 planner re-grep
found **2 occurrences** — confirmed on-disk: line 147 (full-path form) + line 257 (abbreviated
`(:215-217` form). Both are the drifted essential-BC citation and both are corrected to `:216-217`.
The third `laplaceoperator.cpp` range citation — line 253's `:184-223` (the whole
`GetStiffnessMatrix`) — is correct and is left untouched (it is the broader-range cite the cycle-055
D7-repairer flagged as legitimate). No body re-authoring; pinpoint correction only.

## On-disk verification (source of truth, not codemap)
`reference/palace/palace/models/laplaceoperator.cpp` lines 213-218:

    213	        Mpi::Print("\n");
    214	      }
    215	    }
    216	    auto K_l = std::make_unique<ParOperator>(std::move(k_vec[l]), h1_fespace_l);
    217	    K_l->SetEssentialTrueDofs(dbc_tdof_lists[l], Operator::DiagonalPolicy::DIAG_ONE);
    218	    K->AddOperator(std::move(K_l));

`:215` = stray closing brace (not the BC site). `:216` = `ParOperator` construction. `:217` =
`SetEssentialTrueDofs`. The `eliminate_essential_bc` post-composition (ParOperator wrap +
SetEssentialTrueDofs) is `:216-217`.

`citecheck --anchor 'SetEssentialTrueDofs'` on the corrected range:

    [ok] palace/models/laplaceoperator.cpp:216-217  (anchor lit: 'SetEssentialTrueDofs')
         anchor at line(s) [217] within range 216-217

(Note: citecheck reports `:215-217` as also "ok" because the anchor `SetEssentialTrueDofs` is *within*
both ranges — citecheck is a containment lint, not a start-bound checker. The start-bound correction
`:215`→`:216` is justified by the on-disk re-read above: `:215` is a brace, not part of the cited
construct. This is exactly the codemap-localization-only / on-disk-is-truth discipline.)

## Proposed changes

```edit:book/src/L1/fe_assemble.md
[old]: - **BC-elimination is NOT part of the fold**: pinning essential (Dirichlet) dofs
  (`eliminate_essential_bc`, L0 `ParOperator::SetEssentialTrueDofs`,
  `palace/models/laplaceoperator.cpp:215-217`) and lifting inhomogeneous Dirichlet data into the RHS
[new]: - **BC-elimination is NOT part of the fold**: pinning essential (Dirichlet) dofs
  (`eliminate_essential_bc`, L0 `ParOperator::SetEssentialTrueDofs`,
  `palace/models/laplaceoperator.cpp:216-217`) and lifting inhomogeneous Dirichlet data into the RHS
```

```edit:book/src/L1/fe_assemble.md
[old]:   the single-term assembly `fe_assemble(h1_space, [diffusion(ε)])` — then per-level `ParOperator`
  wrap with `SetEssentialTrueDofs` (`:215-217`, the separable `eliminate_essential_bc` post-comp).
[new]:   the single-term assembly `fe_assemble(h1_space, [diffusion(ε)])` — then per-level `ParOperator`
  wrap with `SetEssentialTrueDofs` (`:216-217`, the separable `eliminate_essential_bc` post-comp).
```

## Discipline notes
- Pure citation-hygiene lift, no vocabulary re-anchor and no body re-authoring. Both edits change only
  the pinpoint range `215-217` → `216-217`.
- **Bounded prose-correction provenance** (per the lifter L0-evidence-driven-correction boundary): the
  start-bound correction is directly supported by the on-disk re-read of
  `laplaceoperator.cpp:213-218` (this dispatch read it). It is bounded (a drifted-citation pinpoint
  fix, not a decomposition/signature change) and recorded here.
- Line 253's `:184-223` (`GetStiffnessMatrix` whole-range) is verified correct and deliberately NOT
  touched — it cites the broader assembly span, not the BC site. This resolves the cycle-055
  D7-repairer's note that one of the §Evidence refs might legitimately cite the broader range: line 253
  IS that legitimate broader-range cite; line 257's `(:215-217` is a separate, drifted BC-site cite in
  the same bullet that DOES need fixing.
- Codemap `read_range` and on-disk `awk` agreed on the line numbers here (no ±1 brace-boundary drift on
  this block); the emitted citation comes from the on-disk re-read regardless, per the
  codemap-localization-only discipline.

## Supporting evidence
- `reference/palace/palace/models/laplaceoperator.cpp:213-218` — on-disk re-read confirming `:215` is
  a stray brace and `:216-217` is the `ParOperator` + `SetEssentialTrueDofs` essential-BC site.
- `tools/citecheck/citecheck.py palace/models/laplaceoperator.cpp:216-217 --anchor 'SetEssentialTrueDofs'`
  — anchor resolves at `:217` within the corrected range.
- Cycle-055 D4 (deferred residual) + cycle-056 planner re-grep (2 occurrences: `fe_assemble.md:147`,
  `:257`).

## Open questions / caveats
- None. The two drifted occurrences are both corrected; the one broader-range cite (`:184-223`) is
  verified-correct and left as-is. citecheck's containment-only behavior means the `:215`→`:216`
  start-bound tightening is a semantic (on-disk-verified), not mechanical-lint, correction — flagged
  here for the integrator's awareness but the change itself is unambiguous.
