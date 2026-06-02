---
agent: lifter
invoked_at: 2026-06-02T205715Z
scope: L1 cap citation re-anchor — fe_assemble weak-form-term witness line drift
status: integrated
integrated_at: 2026-06-02T222500Z
integration_commit: 9d3d0676fa3820067e0cac7c3a00eb0b4ced3674
integration_notes: |
  Applied by integrator-per-report (staging row D4, applied_at 2026-06-02T212846Z); finalized by integrator-finalize cycle-069.
  PURE citation re-anchor (lifter pass): L1/fe_assemble.md (4 loci) witness-line-drift cite re-anchor (laplaceoperator.cpp:191-192→:193-196; curlcurloperator.cpp:179-181→:180-181; §Evidence pinpoints). ENACTS the c068 OQ fe-assemble-l1-cap-weak-form-term-witness-line-drift-reanchor — brings the firm L1 cap into agreement with the c068 D2 fe-operator-assemble-mutation-rotation theme; closure note appended to the OQ ledger. fe_assemble stays firm. Bounded 3→4 locus (critic-confirmed). The +2/+1 drift is the recurrence-6 codemap-read-range-plus-one-drift-on-brace-boundary boundary drift, mechanically corrected. Build-relevant: cargo make book exit 0; citecheck 13 ok/0 fail. Zero gate hits; retroactive-budget = 1 (the cycle's sole retroactive-cite draw, under the ≥4 threshold).
inputs:
  - book/src/L1/fe_assemble.md
  - reference/palace/palace/models/laplaceoperator.cpp:184-223 (on-disk verified)
  - reference/palace/palace/models/curlcurloperator.cpp:172-193 (on-disk verified)
  - reference/palace/palace/models/spaceoperator.cpp:270-285 (on-disk verified)
  - reports/2026-06-02T205156Z-cycle-planner-cycle-069/CYCLE.md §D4
---

# CYCLE: Re-anchor fe-assemble-l1-cap-witness

## Summary
Pure citation-hygiene re-anchor on the firm L1 cap `book/src/L1/fe_assemble.md`. The weak-form-term
witness citations for the electrostatic DiffusionIntegrator and magnetostatic CurlCurlIntegrator
cases carried the standard codemap `+1/+2` boundary drift (friction `codemap-read-range-plus-one-drift-on-brace-boundary`,
recurrence-6): `laplaceoperator.cpp:191-192` actually points at the `MaterialPropertyCoefficient
epsilon_func(...)` coefficient line, not at the `AddDomainIntegrator<DiffusionIntegrator>` witness
(which is at `:194`, inside the `BilinearForm k`/`Assemble` block `:193-196`); `curlcurloperator.cpp:179-181`
spans the coefficient line `:179` (`muinv_func`) plus the witness, when the `BilinearForm
k`/`AddDomainIntegrator<CurlCurlIntegrator>` witness pair is `:180-181`. All ranges re-verified by
direct on-disk `Read` of the three Palace source files (NOT trusting `citecheck --anchor` for the
END lines, per the recurrence-6 close-brace blind-spot). No status flip, no structural/law change —
the firm L1 fold's structure, signature, and four laws are unaffected; only the witness line numbers
drifted. NO index-cell touch (this entry is not a status promotion).

The re-anchor also corrects the SAME drift in the §Evidence block's bare-pinpoint cites (`:191`/`:192`/`:194`
→ `:193`/`:194`/`:196`), which the planner's §D4 step-2 grep did not surface (it grepped for the
`:191-192`/`:179-181` full-range form) but which are part of the identical witness-line-drift defect
and are demonstrably wrong against disk — leaving them un-corrected adjacent to the fixed body cites
would be incoherent. This is bounded citation hygiene on the same OQ (the witness lines), not a
structural change.

## On-disk verification (the source of truth — NOT codemap, NOT `--anchor` for END)

**`reference/palace/palace/models/laplaceoperator.cpp`** (`LaplaceOperator::GetStiffnessMatrix`, fn `:184-223`):

    184  std::unique_ptr<Operator> LaplaceOperator::GetStiffnessMatrix()
    ...
    190    constexpr bool skip_zeros = false;
    191    MaterialPropertyCoefficient epsilon_func(mat_op.GetAttributeToMaterial(),
    192                                             mat_op.GetPermittivityReal());
    193    BilinearForm k(GetH1Space());
    194    k.AddDomainIntegrator<DiffusionIntegrator>(epsilon_func);
    195    // k.AssembleQuadratureData();
    196    auto k_vec = k.Assemble(GetH1Spaces(), skip_zeros);
    ...
    216      auto K_l = std::make_unique<ParOperator>(std::move(k_vec[l]), h1_fespace_l);
    217      K_l->SetEssentialTrueDofs(dbc_tdof_lists[l], Operator::DiagonalPolicy::DIAG_ONE);
    ...
    223  }

So `:191-192` is the coefficient ctor (2-line); the DiffusionIntegrator witness is the
`BilinearForm k`/`AddDomainIntegrator<DiffusionIntegrator>`/`Assemble` block `:193-196`. The
fn-range `:184-223` and `SetEssentialTrueDofs` `:216-217` are already correct.

**`reference/palace/palace/models/curlcurloperator.cpp`** (`GetStiffnessMatrix`):

    177    constexpr bool skip_zeros = false;
    178    MaterialPropertyCoefficient muinv_func(mat_op.GetAttributeToMaterial(),
    179                                           mat_op.GetCurlCurlInvPermeability());
    180    BilinearForm k(GetNDSpace());
    181    k.AddDomainIntegrator<CurlCurlIntegrator>(muinv_func);

So `:179` is the second line of the coefficient ctor; the CurlCurlIntegrator witness pair is
`:180-181`.

**`reference/palace/palace/models/spaceoperator.cpp:278`** (confirmed exact — no change):

    277      {
    278        a.AddDomainIntegrator<VectorFEMassIntegrator>(*f);
    279      }

(Note: `spaceoperator.cpp:278` is NOT currently cited in `fe_assemble.md` — the planner's §D4
"add/confirm if cited" reduces to "confirm not present"; I verified it is absent, so no edit adds it.
Confirming the line per the spec's mandate, but it is not part of this file's re-anchor.)

`citecheck --anchor` confirms all three re-anchored ranges in-range (`AddDomainIntegrator<DiffusionIntegrator>`
at 194 ∈ 193-196; `AddDomainIntegrator<CurlCurlIntegrator>` at 181 ∈ 180-181; `VectorFEMassIntegrator`
at 278 ∈ 278); the END lines (`:196` = `k.Assemble`, `:181` = the CurlCurl add) were confirmed by
direct on-disk `Read`, not by `--anchor`.

## Proposed changes

Four loci in `book/src/L1/fe_assemble.md`: law-3 body cite (`:134`), §Dependencies witness cites
(`:166-167`), and the §Evidence bare-pinpoint cites (`:259-260`). Each edit is verbatim against the
on-disk file.

```edit:book/src/L1/fe_assemble.md
[old]: 3. **Single-term reduction**: `fe_assemble(space, [t]) = A(space, t)`. A one-term assembly is just
   that term's contribution — the witness electrostatic case `fe_assemble(h1_space, [diffusion(ε)])`
   = the permittivity-weighted diffusion operator (`palace/models/laplaceoperator.cpp:191-192`).
[new]: 3. **Single-term reduction**: `fe_assemble(space, [t]) = A(space, t)`. A one-term assembly is just
   that term's contribution — the witness electrostatic case `fe_assemble(h1_space, [diffusion(ε)])`
   = the permittivity-weighted diffusion operator (`palace/models/laplaceoperator.cpp:193-196`).
```

```edit:book/src/L1/fe_assemble.md
[old]:  in-scope solver-K witnesses, ∇/Gradient (electrostatic diffusion, `palace/models/laplaceoperator.cpp:191-192`)
  and ∇×/Curl (magnetostatic curl-curl, `palace/models/curlcurloperator.cpp:179-181`) — with identity/mass and
[new]:  in-scope solver-K witnesses, ∇/Gradient (electrostatic diffusion, `palace/models/laplaceoperator.cpp:193-196`)
  and ∇×/Curl (magnetostatic curl-curl, `palace/models/curlcurloperator.cpp:180-181`) — with identity/mass and
```

```edit:book/src/L1/fe_assemble.md
[old]:- `palace/models/laplaceoperator.cpp:184-223` — `LaplaceOperator::GetStiffnessMatrix`: the
  electrostatic witness. `BilinearForm k(GetH1Space())` (`:191`) +
  `k.AddDomainIntegrator<DiffusionIntegrator>(epsilon_func)` (`:192`) + `k.Assemble(...)` (`:194`) —
  the single-term assembly `fe_assemble(h1_space, [diffusion(ε)])` — then per-level `ParOperator`
  wrap with `SetEssentialTrueDofs` (`:216-217`, the separable `eliminate_essential_bc` post-comp).
[new]:- `palace/models/laplaceoperator.cpp:184-223` — `LaplaceOperator::GetStiffnessMatrix`: the
  electrostatic witness. `BilinearForm k(GetH1Space())` (`:193`) +
  `k.AddDomainIntegrator<DiffusionIntegrator>(epsilon_func)` (`:194`) + `k.Assemble(...)` (`:196`) —
  the single-term assembly `fe_assemble(h1_space, [diffusion(ε)])` — then per-level `ParOperator`
  wrap with `SetEssentialTrueDofs` (`:216-217`, the separable `eliminate_essential_bc` post-comp).
```

The §Algebraic-laws "BC-elimination is NOT part of the fold" cite at `:152`
(`laplaceoperator.cpp:216-217` for `SetEssentialTrueDofs`) is left UNCHANGED — verified correct on
disk (`:216` = the `ParOperator` ctor, `:217` = `SetEssentialTrueDofs`). The fn-range `:184-223` and
`:216-217` carry no drift; only the per-construct witness pinpoints inside the body drifted.

## Discipline notes
- Pure citation re-anchor — no `## Status` flip (`fe_assemble` stays `firm`), no structural change,
  no law change. The witness-line drift does not affect the fold's structure, signature, or the four
  algebraic laws (those quantify over the opaque `A` and term list, not over specific source lines).
  Per the planner §D4 step-4 "STRUCTURE unaffected (only witness line numbers)" + the lifter
  "structural rewrite, not authorship" discipline — this is the cleanest in-scope lifter case.
- NO index-cell touch: this is not a promotion (no `## Status` line flips), so the
  `index-table-status-cell-drifts-when-theme-file-promoted` guard does not apply.
- **Self-verified every re-anchored citation against on-disk source BEFORE emitting** (per the
  recurrence-6 close-brace `--anchor`-blind-spot sub-bullet): directly `Read` the source line ranges
  in all three `.cpp` files. The END lines (`:196`, `:181`) were confirmed by on-disk `Read`, NOT by
  `citecheck --anchor` (which is blind to range-END off-by-one). `citecheck --anchor` was used only
  to confirm the anchor token sits IN-range (it does, for all three).
- **Bounded scope extension (recorded, not silent):** the planner §D4 named 3 pre-drift loci
  (`:134`, `:166`, `:167`). I additionally re-anchored the §Evidence bare-pinpoint cites at `:259-260`
  (`(:191)`/`(:192)`/`(:194)` → `(:193)`/`(:194)`/`(:196)`) — the planner's §D4 step-2 grep used the
  `:191-192`/`:179-181` full-range pattern and so did not catch the bare-pinpoint form, but these
  cite the IDENTICAL witness constructs (`BilinearForm k`, `AddDomainIntegrator<DiffusionIntegrator>`,
  `k.Assemble`) and are demonstrably wrong against disk by the same +2 drift. Correcting them is the
  same OQ (`fe-assemble-l1-cap-weak-form-term-witness-line-drift-reanchor` — the *witness lines*),
  directly supported by the on-disk `Read` this dispatch performed, and bounded (fixing drifted
  pinpoints, not re-architecting the entry). Leaving them stale adjacent to the corrected body cites
  would be incoherent. This is the L0-evidence-driven bounded prose-correction carve-out (cycle-012
  `lifter-scope-content-correction-boundary`).
- This re-anchor closes the firm L1 cap's stale-witness defect that the c068 D2
  `fe-operator-assemble-mutation-rotation` re-anchor identified but could not fix (out of D2's
  append-only L1>L0-theme write-scope). The c068 D2 theme already re-anchored its OWN copies to the
  correct `:193-196`/`:180-181`/`:278` lines; this dispatch brings the firm L1 cap into agreement.

## Supporting evidence
- `book/src/L1/fe_assemble.md` — the firm L1 cap being re-anchored (4 loci: `:134`, `:166-167`,
  `:259-260`).
- `reference/palace/palace/models/laplaceoperator.cpp:184-223` — `GetStiffnessMatrix`; DiffusionIntegrator
  witness `:193-196` (coefficient at `:191-192`, witness block at `:193-196`). On-disk verified.
- `reference/palace/palace/models/curlcurloperator.cpp:172-193` — `GetStiffnessMatrix`; CurlCurlIntegrator
  witness pair `:180-181` (coefficient at `:178-179`). On-disk verified.
- `reference/palace/palace/models/spaceoperator.cpp:270-285` — `VectorFEMassIntegrator` at `:278`
  (confirmed exact; NOT cited in `fe_assemble.md`, so no edit).
- `reports/2026-06-02T205156Z-cycle-planner-cycle-069/CYCLE.md` §D4 — the dispatch scope + drift
  hints (codemap-derived; superseded by this dispatch's on-disk `Read`).
- Friction-ledger `codemap-read-range-plus-one-drift-on-brace-boundary` (recurrence-6) — the drift
  class; OQ `fe-assemble-l1-cap-weak-form-term-witness-line-drift-reanchor` (opened c068).

## Open questions / caveats
- **The codemap-vs-on-disk drift held exactly as predicted:** `laplaceoperator.cpp` witness drifted
  `+2` (`:191-192`→`:193-196`, because the codemap merged the 2-line `MaterialPropertyCoefficient`
  ctor + `BilinearForm` open), `curlcurloperator.cpp` drifted `+1` (`:179-181`→`:180-181`). No NEW
  drift class surfaced; this is the standard recurrence-6 boundary drift, mechanically corrected.
- **§D4 step-2 grep undercount (flag for the planner's deliverable-check discipline, NOT a content
  issue):** the planner's §D4 deliverable check located 3 loci by grepping the `:191-192`/`:179-181`
  full-range form, missing the §Evidence bare-pinpoint cites (`(:191)`/`(:192)`/`(:194)`) which carry
  the identical drift. A future witness-drift re-anchor grep should also match the bare-`(:NNN)`
  pinpoint form, not only the full `:lo-hi` range form, to enumerate all loci up front. Recorded as a
  caveat; I handled it within this dispatch (bounded, evidenced, see §Discipline notes) — no follow-on
  needed.
- **No abstractor reread needed:** the re-anchor is pure line-number hygiene; the firm L1 cap's
  semantics, signature, and laws are unchanged. The integrator should NOT treat this as a status
  change (no `## Status` flip, no index-cell touch).
