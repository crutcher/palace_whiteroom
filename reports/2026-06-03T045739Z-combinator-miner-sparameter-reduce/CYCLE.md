---
agent: combinator-miner
invoked_at: 2026-06-03T045739Z
integrated_at: 2026-06-03T055824Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-075 D1. Applied clean — the coupled registration for D6's sparameter_reduce chapter: L4/index.md dep-map row (Data-algebra sub-group, alpha-within-kind after nrm2) + the reduce-to-matrix cohort note (gram_reduce bilinear-Gram vs sparameter_reduce linear-projection, same shape / different fold) + SUMMARY.md entry (alpha after nrm2). Coupled pair COMPLETE — D6's chapter on disk before this inbound live link. No new OQ slug (report OQs already filed by prior in-cycle integration). citecheck 26 ok / 0 fail. retroactive 0. cargo make book exit 0, linkcheck2 clean."
scope: New L4 reduction verb — sparameter_reduce (driven per-port port-projection reduction)
status: pending
---

# CYCLE: Combinator candidate — sparameter_reduce

## Summary

The driven (frequency-domain) output product — the **scattering matrix S** — is
produced by a per-ω, per-port reduction that is **genuinely distinct from
`gram_reduce`** (cycle-073 / c074 D6 probed this and correctly REFUSED the
symmetric-Gram subsume). I propose `sparameter_reduce` as a **new L4 data-algebra
reduction verb** (combinator-as-entry per the VOCABULARY-SHIFT redirect): the
**per-column port-mode linear-projection reduction** that maps a driven per-ω
solution family `[E_ω]` (one solve per drive-port column) → the scattering matrix
`S`, by (1) **projecting the field onto each receiver port mode** (`sᵢ·E`, the
`GetSParameter` port-mode linear functional), (2) **subtracting the drive-port
self-term** (`S_ii -= 1` on the diagonal — an inhomogeneous `−1`), and (3) applying
the **port-kind impedance/de-embed scaling** (lumped: generalized-S
`√(R_src/R_dst)`; wave: per-endpoint de-embedding `exp(ikₙd)`). It is a per-ω
**linear projection**, NOT a symmetric bilinear Gram: no `symmetric_from_upper` (S's
near-symmetry is reciprocity *physics*, not a construction), an inhomogeneous diagonal
`−1` self-term, a directional (asymmetric) `√(R_src/R_dst)` scaling, complex throughout,
and assembled one drive-column per solve. It rises to L4 as a **feature-surface verb
the backend wants** (directive-1: L4 is the outward backend-lowering target) — the
**driven output-product reduction** completing the driven composition root
(`feature/driven.L4.md:55,98` already forward-reference the slug; verified on disk).

Layer: **L4** (the data-algebra reduce-to-matrix cohort, alongside `gram_reduce`).
Status: **`rough-in`** (warrant-first reasoning in §Proposed combinator / §Status).

## Pattern instances

The reduction is **single-pipeline (driven only)** — S-parameters are a driven-solver
concept. Per the dispatch framing + the `disciplined-cross-pipeline-combinator-mining-gate`
single-witness probe: this is NOT a cross-pipeline mine. The "instances" that warrant
authoring it are (a) the **two port-kind assembly variants of the SAME driven
postprocess** (a variant axis, NOT a 2nd pipeline) and (b) the converging
forward-references that already name the slug. Codemap-verified this dispatch
(`mcp__palace-codemap__read_range` + `search_text`, close-brace discipline):

- **Instance 1 — the per-port reduction assembly loop (driven postprocess):**
  `palace/models/postoperator.cpp:1246` (`void PostOperator<solver_t>::MeasureSParameter()
  const`), body `:1247-1308`. Two structurally-identical port loops — lumped
  (`:1267-1286`) and wave (`:1287-1307`) — each: read the previously-computed projection
  `vi.S`, subtract the drive-port self-term on the diagonal (`if (idx ==
  drive_port_idx) vi.S.real(vi.S.real() - 1.0)`, `:1272-1275` lumped / `:1294-1297`
  wave), then apply the port-kind scaling. The `drive_port_idx` (`:1263`) is the column
  index — one column per solve.
- **Instance 2 — the per-port-mode linear projection `sᵢ·E` (lumped variant):**
  `palace/models/lumpedportoperator.cpp:283` (`std::complex<double>
  LumpedPortData::GetSParameter(GridFunction &E) const`), body `:285-294`:
  `std::complex<double> dot((*s) * E.Real(), 0.0); if (E.HasImag()) dot.imag((*s) *
  E.Imag());` — the linear functional `sᵢ·E` (the port-mode linear form `s` dotted with
  the field), real + imag parts. This is the projection kernel folded per receiver port.
- **Instance 3 — the per-port-mode linear projection (wave variant, same shape):**
  `palace/models/waveportoperator.cpp:780` (`std::complex<double>
  WavePortData::GetSParameter(GridFunction &E) const`), body `:782-793`: transfer `E` to
  the port FE space, then `dot(-((*port_sr)*port_E->Real()) - ((*port_si)*port_E->Imag()),
  ...)` — the `(E × H_inc⋆)·n` port-mode projection (`:782-783` comment), the wave-port
  realization of the same `sᵢ·E` linear functional with the complex port-mode `s = port_sr
  + i·port_si`.
- **Instance 4 — the per-ω projection is cached during the measure pass:**
  `palace/models/postoperator.cpp:1141` + `:1239` (`vi.S = data.GetSParameter(*E);`) — the
  projection `sᵢ·E` is computed per port during `MeasureLumpedPorts` / `MeasureWavePorts`,
  then `MeasureSParameter` (`:1246`) applies the self-term + scaling. The two-phase
  structure (project, then post-scale) is the C++ realization of the reduction.
- **Instance 5 — forward-references that already name the slug (converging demand):**
  `book/src/feature/driven.L4.md:55` (the composition-root stage 3 `sparameter_reduce es
  (ports cfg)`), `:97-99` (the `sparameter_reduce is NOT authored in this chapter`
  forward-ref), `:157` (the constituent down-link table row `S-parameter reduction
  (output product) | sparameter_reduce *(...; not authored here)* | forward-ref`).
  `book/src/L4/gram_reduce.md:182-188` (the c074 D6 probe naming the S-param column as a
  NON-MATCH that "author[s] [its] OWN reduction verb").
- **Instance 6 — dedicated unit tests EXIST for the projection kernel (L0-equivalent
  semantic evidence):** `test/unit/test-lumpedportintegration.cpp:367` + `:720`
  (`std::complex<double> s_param = port_1.GetSParameter(port_primary_gf_ht_cn);`),
  `test/unit/test-romoperator.cpp:603` (`auto S = port_data.GetSParameter(E);`). The
  *projection kernel* is unit-tested; the *reduction* (self-term + scaling assembly in
  `MeasureSParameter`) is integration-level. This split gates the status precisely (see
  §Status).

## Proposed combinator

- **Slug**: `sparameter_reduce`
- **Layer**: **L4** — the data-algebra reduce-to-matrix cohort, the sibling of
  `gram_reduce` (the energy-output-product Gram reduction). Rationale for L4 (not an
  adjacent layer): it is a **feature-surface verb the backend wants** (directive-1: L4
  is the outward backend-lowering target; `concepts/black-box-vs-accelerated-kernels.md`
  §"The combinators rise regardless") — the driven output-product reduction completing
  the driven composition root (`feature/driven.L4.md` stage 3). It is a pure
  value-producing reduction (no `Solve` monad / carry / convergence predicate) over the
  collected per-ω family, so it belongs in the same L4 data-algebra cohort as
  `inner_product` / `linear_combination` / `gram_reduce`, NOT at the iteration-structural
  outer-driver layer. NOT L3/L2/L1: the per-port projection kernel (`sᵢ·E`) already has
  L1 homes (the port-mode linear functional — a `bilinear-form`-adjacent linear form);
  the *reduction* (the per-column self-term + port-kind scaling assembly) is the new
  vocabulary, and it is the **feature-surface verb** — its natural home is L4 where the
  driven feature column down-links.

- **Signature sketch** (best guess; harvester firms up; L4 strawman notation):

      -- the driven per-ω per-port S-parameter reduction: project the per-ω solution
      -- onto each receiver port mode, subtract the drive-port self-term, apply the
      -- port-kind impedance/de-embed scaling. One drive-COLUMN per solved member.
      sparameter_reduce :: [PortMode]                 -- the receiver port modes [sᵢ] (lumped: s; wave: port_sr+i·port_si)
                        -> [(Int, Tensor[N])]         -- the driven family: (drive_port_idx, E) per solved column
                        -> Matrix[p, p]               -- the scattering matrix S (p = #ports), per column over the family
      sparameter_reduce ports family =
        matrix_from_columns
          [ [ scale ports i j (project (ports!!i) e - selfterm i j)   -- entry Sᵢⱼ for receiver i, drive column j
              | i <- [0 .. p-1] ]
            | (j, e) <- family ]
        where
          p              = length ports
          project s e    = port_dot s e                  -- the linear functional sᵢ·E (lumped (*s)·E / wave (E×H⋆)·n)
          selfterm i j   = if i == j then 1 else 0       -- the inhomogeneous diagonal −1 self-term (drive-port subtract)
          scale ports i j = port_scale (ports!!i) (ports!!j)  -- lumped: √(R_src/R_dst); wave: exp(ikₙᵢdᵢ)·exp(ikₙⱼdⱼ)

  Shape contract (bunsen-style; named axes):
  - `ports : [PortMode]` — read-only; the per-port mode functionals (lumped `s`, wave
    `port_sr + i·port_si`) + the per-port impedance/de-embed parameters (`R`, `kn0`,
    `d_offset`) absorbed into the `scale` closure. `p = length ports`.
  - `family : [(Int, Tensor[N])]` — the driven solution family: per solved column, the
    drive-port index `j` + the per-ω complex field `E`. (Per-ω: the whole reduction is
    applied once per swept frequency; the ω index rides as the outer family axis,
    factored out for clarity.)
  - result `Matrix[p, p]` — the (complex) scattering matrix `S` for that ω.

- **Algebraic intuition**:
  - **Linearity in the field (per column).** Each raw entry `project sᵢ E` is **linear**
    in `E` (`sᵢ·E` is a linear functional) — contrast `gram_reduce`'s entries, which are
    **bilinear** in the family pair `(xᵢ, xⱼ)`. This is the load-bearing structural
    difference: S is a per-column linear projection, the Gram is a pair-grid bilinear.
  - **NO symmetry-by-construction.** There is no `symmetric_from_upper`. S's near-symmetry
    `Sᵢⱼ ≈ Sⱼᵢ` is **reciprocity physics** (a property of the assembled S for reciprocal
    media), NOT a construction the reduction imposes — every entry is computed independently
    (one column per solve, all receiver rows per column). So the over-unification guard vs
    `gram_reduce`: do NOT add a symmetric mirror.
  - **Inhomogeneous diagonal (the `−1` self-term).** The diagonal carries an additive `−1`
    (`S_ii = project sᵢ E_i − 1`) — the incident-wave subtraction. This is an
    **inhomogeneous** term (an affine, not linear, contribution at the diagonal), with no
    analog in `gram_reduce` (whose diagonal is the homogeneous self-bilinear).
  - **Directional (asymmetric) scaling.** The generalized-S scale `√(R_src/R_dst)` is
    **directional** — it depends on the ordered `(drive, receiver)` pair and is NOT
    symmetric under swap (`√(R_j/R_i) ≠ √(R_i/R_j)`). The wave-port de-embed
    `exp(ikₙᵢdᵢ)·exp(ikₙⱼdⱼ)` IS symmetric in `(i,j)` but is a per-endpoint product
    (distinct from lumped). These are two values of the **port-kind scaling variant axis**.
  - **Identity / no-op specialization.** When all ports are non-resistive (`|R| = 0`,
    lumped) the generalized-S scale is skipped (`S *= √(R_src/R_dst)` guarded by
    `std::abs(data.R) > 0.0`, `:1277-1280`); when `d_offset = 0` (wave, the default) the
    de-embed `exp(ik·0) = 1` is the identity. So the un-scaled raw projection-minus-self-term
    is the scale-axis identity element.

- **Variant axes**:
  - **port-kind** (lumped | wave — THE load-bearing axis; absorbed into the `PortMode` +
    `scale` closure). Lumped: `s` linear form, generalized-S `√(R_src/R_dst)` scale (resistive
    guard). Wave: `(E×H⋆)·n` projection, per-endpoint de-embed `exp(ikₙd)` scale. The two
    are **assembly variants of the SAME driven postprocess** — a variant axis, NOT a 2nd
    pipeline (per the disciplined-mining-gate single-witness-probe framing in the dispatch
    scope). Note: Palace forbids *mixing* lumped+wave in one model
    (`postoperator.cpp:1255-1259` — the `xor` guard), so a given reduction is wholly one kind.
  - **scaling-presence** (generalized-S present/absent via the `|R| > 0` resistive guard;
    de-embed present/absent via `d_offset ≠ 0`) — absorbed into the `scale` closure; the
    absent case is the scale-axis identity.
  - **element-type** (complex — pinned; S-parameters are inherently complex, unlike the
    real energy-Gram). A non-collapsing axis here (contrast `gram_reduce`'s real pin).
  - **single-excitation-per-port precondition** — the S-matrix is only measured when
    `GetPortExcitations().IsMultipleSimple()` (`postoperator.cpp:1257`), i.e. one drive port
    per excitation column; absorbed as a precondition, not a variant.

  **Over-unification guard (do NOT subsume into `gram_reduce`).** `gram_reduce` is the
  symmetric **bilinear** reduce-to-matrix (pair-grid `xⱼᵀ K xᵢ`, `symmetric_from_upper`,
  homogeneous diagonal, real). `sparameter_reduce` is the per-column **linear-projection**
  reduce-to-matrix (column-indexed `sᵢ·E`, no mirror, inhomogeneous `−1` diagonal,
  directional scaling, complex). Same result *shape* (`Matrix[p, p]`), **different fold**
  (linear projection vs bilinear Gram) — exactly the `dot`-vs-`linear_combination`
  same-operand-shape-different-fold guard pattern (`concepts/black-box-vs-accelerated-kernels.md`
  §2; precedent `gram_reduce.md:182-189` keeping S-params explicitly out of scope). Author
  it as its OWN verb; cross-link the two as data-algebra reduce-to-matrix siblings.

## Proposed changes

```edit:book/src/L4/index.md
[Add a row to the "### Data-algebra combinators & named verbs" dep-map table,
in alpha-within-kind position: AFTER the `nrm2` row (line 100), as the new last
row of that group (s > n). The row:]

| [`sparameter_reduce`](./sparameter_reduce.md) | `sparameter_reduce :: [PortMode] -> [(Int, Tensor[N])] -> Matrix[p, p]`; `Sᵢⱼ = scale(i,j) · (project sᵢ E_j − [i==j])`, per drive-column over the family (no symmetric mirror). The driven **per-port port-projection reduction combinator**: project each per-ω solution onto each receiver port mode (`sᵢ·E`, a **linear** functional — NOT a bilinear Gram), subtract the drive-port self-term (inhomogeneous diagonal `−1`), apply the port-kind impedance/de-embed scaling (lumped generalized-S `√(R_src/R_dst)`; wave de-embed `exp(ikₙd)`). The **reduce-to-matrix** member of the L4 algebra-of-folds for the driven output product — the linear-projection sibling of the bilinear symmetric-Gram [`gram_reduce`](./gram_reduce.md) (same `Matrix[p,p]` result shape, DIFFERENT fold: linear projection vs bilinear Gram, no mirror, inhomogeneous `−1` diagonal, directional scaling, complex — the do-NOT-merge over-unification guard). Pure value-producing reduction — no `Solve` monad / carry / predicate. | Folds (the per-port projection kernel): the port-mode linear functional `sᵢ·E` (lumped `(*s)·E` `lumpedportoperator.cpp:283`; wave `(E×H⋆)·n` `waveportoperator.cpp:780`). Consumes: [`frequency_sweep`](./frequency_sweep.md) (produces the per-ω driven family `[E_ω]` this reduces). Concepts: `black-box-vs-accelerated-kernels` (§"the combinators rise regardless"). Sibling reduce-to-matrix combinator: [`gram_reduce`](./gram_reduce.md). | L1 the port-mode projection by **identity-in-form on the body** (the reduction is a per-column fold of the port-mode linear functional + a per-entry scalar self-term/scale map; **no dedicated L4>L3 theme** — the in-line-marker route; the substantive downward content is the C++ two-phase project-then-postscale assembly `postoperator.cpp:1141,1239,1246-1309` + the port projection kernels' own L1>L0 rotations). | `rough-in` (harvested cycle-075 D1 LEAD from the driven feature-chapter forward-mine flags `driven.L4.md:55,98,157`; structure firm-on-positive-structure on the single positive driven postprocess `postoperator.cpp:1246-1309` with two port-kind assembly variants, but `rough-in` because the *reduction-level* assembly (self-term + port-kind scaling) is integration-level / test-unconfirmed (only the projection KERNEL `GetSParameter` is unit-tested, `test-lumpedportintegration.cpp:367,720` + `test-romoperator.cpp:603`) AND the per-port projection L1 homes are not yet firm. Single-pipeline BY DESIGN — driven only; the lumped-vs-wave split is a variant axis, NOT a 2nd pipeline. Over-unification guard: NOT a `gram_reduce` specialization — linear projection ≠ bilinear Gram) |
```

```edit:book/src/L4/index.md
[Update the "### Data-algebra combinators & named verbs" cohort prose (around the
group intro / §Vocabulary cohort) to add a one-sentence bullet noting the new
reduce-to-matrix sibling pairing. Suggested addition to the cohort narrative
(harvester/layer-intro-author may place precisely):]

The reduce-to-matrix corner of the L4 data-algebra now carries **two distinct folds**
of the same `Matrix[p,p]` result shape: [`gram_reduce`](./gram_reduce.md) (the symmetric
**bilinear** energy-Gram — capacitance/inductance output products, `w·xⱼᵀKxᵢ`,
`symmetric_from_upper`) and [`sparameter_reduce`](./sparameter_reduce.md) (the per-column
**linear-projection** scattering reduction — the driven S-parameter output product,
`scale·(sᵢ·E − [i==j])`, no mirror). Same shape, different fold (the do-NOT-merge
over-unification guard, `concepts/black-box-vs-accelerated-kernels.md` §2).
```

Note: this report does **not** create `book/src/L4/sparameter_reduce.md` — that is the
harvester's formalization job. Combinator-miner adds only the dep-map row (as a
`rough-in`) + the cohort note. **`SUMMARY.md` insertion needed** (flagged for the
integrator; combinator-miner does not author the chapter so the live-link in
`SUMMARY.md` should be added by the harvester pass that creates the file, OR by the
integrator stub-materialization per CLAUDE.md §"Integration may materialize implied
components as stubs"): add `  - [sparameter_reduce](./L4/sparameter_reduce.md)` to the
"Data-algebra combinators & named verbs" L4 sub-list **after** line 47
(`  - [nrm2](./L4/nrm2.md)`), before line 48 (the "Outer-driver caps" group) —
alpha-within-kind (s > n). The dep-map row above uses an inline-code/plain forward-ref
style for the slug per the forward-reference convention until the file exists; the
`[`sparameter_reduce`](./sparameter_reduce.md)` live link in the proposed row will only
resolve once the harvester creates the file — if the integrator applies this row before
the file exists, downgrade the row's first cell to plain `` `sparameter_reduce` `` to
avoid a `linkcheck2` hard error (friction-ledger
`rough-in-forward-reference-must-be-plain-text-not-live-link`).

## Supporting evidence

All L0 citations self-verified on-disk this dispatch via the palace-codemap
(`mcp__palace-codemap__read_range` + `search_text`, close-brace discipline; the dispatch
scope warned that c074 D6's repairer corrected several pinpoints here, so each was
re-verified):

- **The per-port reduction assembly (positive witness, the reduction itself):**
  `palace/models/postoperator.cpp:1246` (`MeasureSParameter` def), `:1255-1259` (the
  single-excitation + lumped-XOR-wave precondition guards), `:1263` (`drive_port_idx =
  measurement_cache.ex_idx` — the column index), `:1267-1286` (the lumped port loop:
  self-term `:1272-1275`, generalized-S scale `:1277-1280`), `:1287-1307` (the wave port
  loop: self-term `:1294-1297`, de-embed scale `:1300-1302`).
- **The per-port-mode projection kernels (the fold element):**
  `palace/models/lumpedportoperator.cpp:283-294` (`LumpedPortData::GetSParameter` — the
  `(*s)·E` linear functional), `palace/models/waveportoperator.cpp:780-793`
  (`WavePortData::GetSParameter` — the `(E×H⋆)·n` projection).
- **The two-phase project-then-postscale cache:** `palace/models/postoperator.cpp:1141`
  + `:1239` (`vi.S = data.GetSParameter(*E)` — projection computed during the per-port
  measure pass, consumed by `MeasureSParameter`).
- **Dedicated unit tests for the projection kernel (L0-equivalent; the status gate):**
  `test/unit/test-lumpedportintegration.cpp:367` + `:720`, `test/unit/test-romoperator.cpp:603`
  (`GetSParameter` exercised directly). The *reduction* assembly (`MeasureSParameter`) has
  no dedicated unit test — integration-level under the full driven `Solve(mesh)`.
- **Feature-chapter forward-references (the converging demand that flagged the mine):**
  `book/src/feature/driven.L4.md:55` (composition-root stage 3), `:97-99` (the
  not-authored-here forward-ref), `:157` (the down-link table forward-ref row).
- **The c074 D6 NON-MATCH probe that scoped S-params OUT of `gram_reduce`:**
  `book/src/L4/gram_reduce.md:182-189` (the closed-negative probe: S-params are "a
  per-column port-mode LINEAR PROJECTION ... NOT symmetric-Gram ... author their OWN
  reduction verb").
- **Firm vocabulary grounding / siblings:** `book/src/L4/gram_reduce.md` (the
  reduce-to-matrix bilinear sibling), `book/src/L4/inner_product.md` +
  `book/src/L4/linear_combination.md` (the reduce-to-scalar / reduce-to-tensor algebra-of-folds
  siblings), `book/src/L4/frequency_sweep.md` (the firm driven solve-half map that
  produces the family this reduces), `book/src/concepts/black-box-vs-accelerated-kernels.md`
  §"The combinators rise regardless" (the L4-feature-surface-verb warrant + the
  same-shape-different-fold over-unification guard, §2).
- **Skill cited:** `skills/disciplined-cross-pipeline-combinator-mining-gate/SKILL.md` —
  run as the single-witness probe: S-params are **single-pipeline (driven)**; the
  lumped-vs-wave split is a **variant axis** (two assembly variants of the same driven
  postprocess), NOT a 2nd pipeline, so the gate's ≥2-pipeline bar does NOT apply — this is
  a within-pipeline output-product reduction, authored from the single driven witness with
  the port-kind variant axis explicit (step 2: no break-witness to classify as a scope
  boundary; step 3: no unprobed pipeline — S-params do not exist outside driven; step 4:
  combinator-as-entry, the two port kinds re-express through it).

## Status warrant (warrant-first)

`rough-in`. **Reasoning.** The combinator's **structure** is firm-on-positive-structure
— the per-column linear-projection skeleton (project `sᵢ·E`, subtract drive-port self-term
`−1`, apply port-kind scaling, no symmetric mirror) is read directly off the single
positive `MeasureSParameter` body (`postoperator.cpp:1246-1309`) with its two
structurally-identical port-kind loops, and every algebraic claim (§Algebraic intuition)
is a syntactic read-off of that body. So the *structure* would clear the
firm-on-positive-structure escape. BUT two factors gate it to `rough-in`:
1. The **reduction-level assembly** (the self-term + port-kind scaling stitched onto the
   projection in `MeasureSParameter`) is **integration-level** — only the projection
   *kernel* `GetSParameter` is unit-tested (`test-lumpedportintegration.cpp:367,720`,
   `test-romoperator.cpp:603`); the reduction assembly is exercised only through the full
   `Solve(mesh)` driver. So the reduction-level laws are test-unconfirmed.
2. The **per-port projection L1 homes are not yet firm** (the port-mode linear functional
   `sᵢ·E` — a `bilinear-form`-adjacent linear form — does not yet have a firm L1 entry the
   way `inner_product` does), so the entry would inherit reduced maturity from its folded
   constituents (the `gram_reduce` pattern: rough-in because its `matrix-weighted-norm` /
   `bilinear-form` constituents are rough-in).

I chose `rough-in` over `rough-in (test-coverage-bounded)` deliberately: the
test-coverage-bounded qualifier names entries whose *structure* is fully L0-anchored and
only the *laws* are test-gated. Here BOTH the constituent L1 projection homes are absent/
non-firm AND the reduction assembly is test-gated — closer to plain `rough-in` (the
harvester may refine to `rough-in (test-coverage-bounded)` if it firms the L1 projection
home in the same pass). Promotion route: (a) a firm L1 port-mode-projection entry the
reduction folds, AND (b) a dedicated S-matrix-assembly test OR a lowering-verifier pass
raising the reduction-level law confidence.

**Scope: single-pipeline (driven) BY DESIGN** — S-parameters are a driven-solver output
product; there is no cross-pipeline generalization (the disciplined-mining-gate
single-witness probe resolves to "within-pipeline output-product reduction with a
port-kind variant axis", not a deferred cross-pipeline mine). This is the **3rd
output-product reduction verb** alongside `gram_reduce` (capacitance/inductance) — the
eigenmode Q-factor scalar-ratio map and the S-parameter linear projection were both
probed as `gram_reduce` 3rd-witnesses and CORRECTLY refused (different folds); this report
authors the S-parameter one as its own verb per that closed-negative finding.

## Open questions / caveats

- **OQ candidate (append to ledger):** `sparameter-reduce-l1-port-projection-home` —
  the per-port linear functional `sᵢ·E` (lumped `(*s)·E`, wave `(E×H⋆)·n`) is the fold
  element of `sparameter_reduce` but has no firm L1 entry. Is it a specialization of the
  existing `bilinear-form` L1 entry (a linear form is the `y`-fixed / left-fixed
  partial-application of a bilinear form at the port-mode covector), or its own L1
  `port_projection` verb? Resolving this firms the gate-(b) promotion route for
  `sparameter_reduce` AND may unify with `gram_reduce`'s `bilinear-form` constituent. The
  harvester authoring `sparameter_reduce.md` should pin which L1 home it folds.
- **OQ candidate:** `sparameter-reduce-eigenmode-q-factor-third-output-product` — the
  eigenmode Q-factor / energy post-processing (`eigensolver.cpp:424-471` +
  `postoperator.cpp:1174-1217`, per `gram_reduce.md:182-185`) is a per-mode SCALAR-RATIO
  map `Q_mj = ω_m/κ_mj` — a THIRD output-product reduction shape (neither bilinear-Gram
  nor linear-projection-matrix; a per-mode scalar reduction). It is NOT in scope here but
  is the next output-product reduction verb candidate (reduce-to-vector / per-mode-scalar).
  Flag for a future cycle so the output-product spine gets its 3rd reduction verb.
- **Caveat (per-ω axis factoring):** I factored the swept-frequency ω axis OUT of the
  `sparameter_reduce` signature (the reduction is applied once per ω; the ω index rides as
  the outer family axis). The harvester should decide whether `sparameter_reduce` takes a
  single-ω family `[(Int, Tensor[N])]` (the form above, mapped over ω by the driven
  composition root) or the full `[ω -> family]` (ω folded in). The single-ω form keeps the
  combinator the per-port reduction and lets `frequency_sweep` own the ω map — cleaner
  separation, matching how `MeasureSParameter` runs once per measured frequency.
- **Caveat (mixed-port exclusion):** Palace forbids mixing lumped+wave ports in one model
  for S-parameters (`postoperator.cpp:1255-1259`, the `xor` guard — "we need to fix
  consistent conventions / de-embedding"). The `port-kind` variant axis is therefore
  **whole-model**, not per-port — the harvester should record this as a precondition on the
  `[PortMode]` argument (all-lumped XOR all-wave), not a per-entry branch.
- **Caveat (forward-reference link discipline):** `feature/driven.L4.md:157` carries the
  slug as a plain-text `*(...; not authored here)*` forward-ref (correct per the
  convention). When the harvester creates `sparameter_reduce.md`, the
  `upgrade-plain-text-ref-to-live-link-when-target-on-disk` skill should be run to upgrade
  that down-link row + the `:55,:98` references to live links, and the driven feature
  column's `status: seed` may then advance (a feature column promotes past `seed` only once
  ALL composed constituents are firm — `sparameter_reduce` landing `rough-in` does NOT yet
  clear that, but it converts the stage-3 forward-ref into a real linked constituent).
