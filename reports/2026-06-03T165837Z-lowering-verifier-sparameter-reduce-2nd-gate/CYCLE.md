---
agent: lowering-verifier
invoked_at: 2026-06-03T16:58:37Z
scope: L4 verb audit — sparameter_reduce 2nd (test-coverage) gate discharge via existing Palace postprocess unit tests
status: integrated
integrated_at: 2026-06-03T210000Z
integration_commit: bdaf851
integration_notes: "Applied cycle-079 (batch-25 position 1). sparameter_reduce ## Status rough-in -> rough-in (test-coverage-bounded) via existing-test citation (test-postoperator.cpp check_port_data dimensionless-S round-trip; batch-24 decision (e)); gate-b recorded already-discharged via firm port_projection (c077); verified_against: block landed; L4/index status cell + sparameters.L1.md composes: frontmatter refreshed. The coupled sparameters column STAYS seed. The sparameters.L1.md PROSE down-link repoint (:39,60,64) DEFERRED to a next-cycle layer-intro-author/lifter follow-up. NO firm-count change."
inputs:
  - book/src/L4/sparameter_reduce.md (the verb under audit; currently rough-in, no prior verified_against block)
  - reference/palace/test/unit/test-postoperator.cpp:145,188-271 (TEST_CASE PostOperator [idempotent]; check_port_data lambda; the c.S dimensional-invariance assertions)
  - reference/palace/test/unit/test-postoperatorcsv.cpp:22-138 (PostOperatorCSV<DRIVEN> fixture)
  - reference/palace/palace/models/postoperator.cpp:1246-1309 (MeasureSParameter — the reduction assembly)
  - reference/palace/palace/models/postoperatorcsv.cpp:162,200-226 (Measurement::Nondimensionalize port-data loop; dim[k].S = data.S // NONE)
  - reference/palace/palace/models/lumpedportoperator.cpp:283-294 + waveportoperator.cpp:780-793 (GetSParameter projection kernels)
  - book/src/L1/port_projection.md (firm L1 projection home, cycle-077 — gate-b)
  - book/src/feature/sparameters.{L4,L1,L0}.md (the seed output-product column; coupled re-check)
---

# CYCLE: Audit sparameter_reduce — 2nd gate (test-coverage) discharge

## Summary

Audited the L4 driven output-product reduction verb `book/src/L4/sparameter_reduce.md`
(currently `rough-in`, no prior `verified_against:` block) against the existing Palace
postprocess unit tests as L0-equivalent semantic documentation, per the batch-24 meta-phase
decision (e) (the 2nd gate is dischargeable in write-scope by CITING the EXISTING postprocess
tests, not authoring a new one). **Verdict: partially-supported → promote to
`rough-in (test-coverage-bounded)`** (not full `firm`). Two findings drive the verdict:

1. **Gate-b (the L1 per-port projection home) is now DISCHARGED out-of-band.** Since this
   theme was authored (cycle-075 D6), cycle-077 landed a **firm** L1 `port_projection.md`
   that explicitly states it satisfies this verb's gate-b. The theme's Status section still
   lists gate-b as open — that is now **stale** and must be refreshed.

2. **Gate-a (the reduction-assembly test) is only OUTPUT-INVARIANT-witnessed, not
   ASSEMBLY-witnessed.** The cited `test-postoperator.cpp` `check_port_data` lambda asserts
   that the reduction OUTPUT field `c.S` is **dimensionless** (`|S|` / `arg(S)` invariant
   under a `Dimensionalize`/`Nondimensionalize` round-trip), for BOTH lumped and wave ports.
   That corroborates the verb's output-semantics (the S-entry is a dimensionless scattering
   ratio — the source-side basis is `postoperatorcsv.cpp:213` `dim[k].S = data.S; // NONE`)
   — but the test uses `RandomMeasurement()` and **never calls `MeasureSParameter`**, so the
   assembly fold (projection + self-term `−1` + impedance/de-embed scaling) is NOT directly
   exercised. This is exactly the `rough-in (test-coverage-bounded)` situation: structure
   firm-on-positive-structure, laws test-gated at the assembly level.

A correction: the dispatch scope cited `test-postoperatorcsv.cpp` as exercising "the
`port-S.csv` measurement-row reduction output". It does NOT — the `PostOperatorCSV<DRIVEN>`
fixture exercises `port-V.csv` (port voltage/current restart + measurement-row plumbing),
NOT `port-S.csv` S-parameter values. The nearest `port-S.csv` content in the test tree is a
synthetic string literal in `test-basesolver.cpp:40` (a restart/symlink test). I record that
citation as `does-not-support` for the S-reduction-output claim.

All L0 anchors the theme asserts were independently re-confirmed this dispatch via
`palace-codemap` `read_range` + `tools/citecheck/citecheck.py --anchor` (and a direct
on-disk Read of the `MeasureSParameter` close-brace). No drift found in the theme's primary
reduction anchors.

## Per-citation audit

- **Citation**: `palace/models/postoperator.cpp:1246-1309` (the reduction assembly).
  - **Theme claim**: the single positive `MeasureSParameter` body off which every
    Algebraic-laws claim is a syntactic read-off (self-term `−1`, generalized-S scale,
    wave de-embed, two structurally-identical port-kind loops).
  - **Found**: `void PostOperator<solver_t>::MeasureSParameter() const` def at `:1246`;
    single-excitation + lumped-XOR-wave guard `:1256-1259`; `drive_port_idx =
    measurement_cache.ex_idx` `:1263`; lumped self-term `vi.S.real(vi.S.real() - 1.0)`
    `:1275` (inside `if (idx == drive_port_idx)` `:1273-1276`); generalized-S scale
    `vi.S *= std::sqrt(src_data.R / data.R)` `:1280`, guarded by `std::abs(data.R) > 0.0`
    `:1278`; wave self-term `:1297` (`:1295-1298`); wave de-embed
    `vi.S *= std::exp(1i * ... kn0 * ... d_offset)` `:1301-1302`. Function close-brace at
    `:1309` (direct on-disk Read confirms `:1307` `}`-wave-loop, `:1308` `}`-if-constexpr,
    `:1309` `}`-function). `citecheck --anchor` `MeasureSParameter` → `[ok]` at `:1246`.
  - **Verdict**: supports.
  - **Notes**: the theme's self-corrected `:1246-1309` range is exact. Every law (linearity
    in the field, no symmetric-mirror, inhomogeneous `−1` diagonal, directional scaling,
    grid-map independence) is a faithful read-off of this body.

- **Citation**: `palace/models/lumpedportoperator.cpp:283-294` (the lumped projection kernel).
  - **Theme claim**: the `(*s)·E` port-mode **linear** functional folded by the reduction
    (`project sᵢ E`).
  - **Found**: `LumpedPortData::GetSParameter` def `:283`; `std::complex<double> dot((*s) *
    E.Real(), 0.0)` `:287`; conditional `dot.imag((*s) * E.Imag())` `:290`;
    `Mpi::GlobalSum` `:292`; close `:294`. A single real covector dotted with the field —
    a linear functional, as claimed.
  - **Verdict**: supports.
  - **Notes**: the theme cites `:285-293` for the body; the actual `dot` construction is
    `:287-291`. Minor — both fall inside the def range. The firm L1 `port_projection`
    entry now owns this kernel's L1 home.

- **Citation**: `palace/models/waveportoperator.cpp:780-793` (the wave projection kernel).
  - **Theme claim**: the `(E×H_inc⋆)·n` projection, complex port mode `port_sr + i·port_si`.
  - **Found**: `WavePortData::GetSParameter` def `:780`; comment `(E x H_inc⋆) ⋅ n = E ⋅ (-n
    x H_inc⋆)` `:782-783`; `MFEM_VERIFY(E.HasImag())` `:784-786`; the 2×2 real recombination
    of `port_sr`/`port_si` against `port_E->Real()`/`Imag()` `:789-790`; `Mpi::GlobalSum`
    `:791`; close `:793`.
  - **Verdict**: supports.

- **Citation**: `test/unit/test-postoperator.cpp:145,188-271` (the postprocess test — the
  2nd-gate evidence).
  - **Theme claim** (dispatch-scoped): the `check_port_data` lambda's dimensionalize /
    non-dimensionalize round-trip invariance over the `Measurement` cache S-field `c.S`
    documents the S-entry's reduction-output semantics + impedance/normalization invariants.
  - **Found**: `TEST_CASE("PostOperator", "[idempotent][Serial]")` `:145`. Setup uses
    `RandomMeasurement()` `:147`, then `Dimensionalize` `:149` / `Nondimensionalize` `:150`.
    `check_port_data` lambda def `:189`. Non-dim assertions: `CHECK_THAT(std::abs(c.S),
    WithinRel(std::abs(ndc.S)))` `:195`, `arg` `:196`. Dim assertions:
    `CHECK_THAT(std::abs(c.S), WithinRel(std::abs(dc.S))) // Scattering always non-dim`
    `:228`, `arg ... // Phase unchanged by normalization` `:229-230`. Invoked over BOTH
    `cache.lumped_port_vi[k]` `:266` and `cache.wave_port_vi[k]` `:271`. All anchors
    `citecheck --anchor` → `[ok]`.
  - **Verdict**: partially-supports.
  - **Notes** (the load-bearing nuance): the test witnesses **only the OUTPUT invariant** —
    that `S` is dimensionless (a scattering ratio: `|S|` and `arg(S)` survive the
    dimensionalize round-trip unchanged for both port kinds). It does **NOT** call
    `MeasureSParameter`; the `c.S` values are RANDOM (`RandomMeasurement()`). So it confirms
    law-3's output property (the S-entry is dimensionless) and that the invariant holds
    across the lumped/wave variant axis — but it does **NOT** exercise the assembly fold
    (the projection, the `−1` self-term, the `√(R_src/R_dst)` / `exp(ikₙd)` scaling). The
    assembly-level laws remain test-unconfirmed. This is the gate that keeps the verb at
    `rough-in (test-coverage-bounded)` rather than `firm`.

- **Citation**: `palace/models/postoperatorcsv.cpp:162,200-226` (`Measurement::Nondimensionalize`
  port-data loop — the source-side basis for the test invariant).
  - **Theme claim**: not previously cited; surfaced this audit to ground the dimensionless-S
    test assertion in source.
  - **Found**: `dimensionalize_port_post_data` lambda `:200`; within it `dim[k].S = data.S;
    // NONE` `:213` — the S-field is passed through with NO scale factor (all sibling fields
    P/V/I/I_RLC/energies ARE scaled). The `// NONE` is Palace's own marker that S is
    dimensionless.
  - **Verdict**: supports.
  - **Notes**: this is WHY the test's "Scattering always non-dim" holds — it is a genuine
    reduction-output invariant of `Sᵢⱼ` (a ratio), corroborating the verb's output
    semantics. It is NOT evidence for the assembly fold.

- **Citation**: `book/src/L1/port_projection.md` (firm L1 projection home — gate-b).
  - **Theme claim**: the theme's Status gate (2) asserts "the per-port projection L1 home is
    not yet firm" (OQ `sparameter-reduce-l1-port-projection-home`).
  - **Found**: a **firm** L1 entry `port_projection.md` (`firmness: firm`, Status
    `firm — firm-on-positive-structure`), landed cycle-077. It explicitly states (`:61-64`):
    "That reduction's gate-b — 'the per-port projection has no firm L1 home' — is satisfied
    by this entry," and reiterates at `:219-221`, `:343-345`.
  - **Verdict**: supports (and renders the theme's gate-2 STALE).
  - **Notes**: gate-b is DISCHARGED. The theme's Status section must drop gate (2) and the
    "I chose plain `rough-in`" reasoning that rested on it.

- **Citation**: `test/unit/test-postoperatorcsv.cpp:22-138` (the dispatch-cited CSV fixture).
  - **Theme claim** (dispatch-scoped): exercises the `port-S.csv` measurement-row reduction
    output (the serialized S-parameter reduction table).
  - **Found**: `class PostOperatorCSVManualTest : public PostOperatorCSV<ProblemType::DRIVEN>`
    `:22-25`; the fixture body asserts on `port-V.csv` existence and the
    `row_i` / `ex_idx_i` / `nr_expected_measurement_rows` / `InitializePortVI` /
    `port_V.has_value()` / `port_I.has_value()` restart + measurement-row plumbing
    (`:80,92,96-97,126,...`). No `port-S.csv` reference, no S-field assertion anywhere in the
    file (grep confirms zero `port-S` / `\.S` hits).
  - **Verdict**: does-not-support (for the S-reduction-output claim — out-of-range).
  - **Notes**: the CSV test covers the port-V/I serialization, not S. The only `port-S.csv`
    content in the test tree is a synthetic literal `"f,S11\n1.0,0.5\n"` in
    `test-basesolver.cpp:40,55-56,62,65` (a restart/symlink file-handling test, not an
    S-reduction assertion). Recorded so a future consumer does not re-chase this as
    S-assembly coverage.

## Applicability conditions

- **Condition**: single-excitation-per-port (`GetPortExcitations().IsMultipleSimple()`).
  - **Verifiable**: yes, from the cited reduction body. Confirmed at `postoperator.cpp:1256`
    (the `if (!...IsMultipleSimple() || ...) return;` early-return guard). The theme's
    `:1256` citation is exact.
  - **Found counter-example?**: no.
- **Condition**: whole-model one port kind — all-lumped XOR all-wave (Palace forbids mixing
  for S-parameters).
  - **Verifiable**: yes. Confirmed at `postoperator.cpp:1257-1259`
    (`!((GetLumpedPortOp().Size() > 0) xor (GetWavePortOp().Size() > 0))` → `return`). The
    comment `:1252-1255` states the de-embedding-convention reason. The theme's
    `:1256-1259` range is exact.
  - **Found counter-example?**: no.
- **Condition**: scaling-presence axis — generalized-S guarded by `|R| > 0`; de-embed
  identity when `d_offset = 0`.
  - **Verifiable**: yes, partially via the test (the dimensionless-S invariant holds for both
    port kinds regardless of scale), and fully via source. Confirmed: lumped scale guard
    `std::abs(data.R) > 0.0` `:1278`; wave de-embed `:1301-1302` is the identity when
    `d_offset = 0` (since `exp(ik·0) = 1`). The test does not exercise specific R/d_offset
    values (random cache), so the scale-axis identity element is source-witnessed only.
  - **Found counter-example?**: no.

## Algebraic laws (cited)

The verb's laws are syntactic identities on the fold, read off the single positive
`MeasureSParameter` body. Per-law audit:

- **Law 1 — Linearity in the field (per column).** Holds. `project sᵢ E = sᵢ·E` is the
  lumped `(*s)·E.Real() [+ i·(*s)·E.Imag()]` / wave 2×2 recombination — linear in `E` with
  no conjugation (confirmed against `lumpedportoperator.cpp:287-290`,
  `waveportoperator.cpp:789-790`, and corroborated by the now-firm L1 `port_projection`
  law-1). Load-bearing distinction from `gram_reduce` (bilinear) — verified.
- **Law 2 — No symmetry-by-construction.** Holds. The body has no `symmetric_from_upper`;
  each entry is one drive-column per solve, all receiver rows. `Sᵢⱼ ≈ Sⱼᵢ` is physics, not
  construction. Verified against the two independent port loops (`:1267-1286`, `:1287-1307`).
- **Law 3 — Inhomogeneous diagonal (`−1` self-term).** Holds. `vi.S.real(vi.S.real() - 1.0)`
  at `i == j`: lumped `:1275`, wave `:1297`. **This law's OUTPUT consequence (S is a
  dimensionless ratio) is the one the postprocess test directly witnesses** (`c.S`
  dimensional invariance) — but the self-term subtraction ITSELF is source-witnessed, not
  test-witnessed (the test never runs the assembly).
- **Law 4 — Directional (asymmetric) scaling.** Holds. Lumped `√(R_src/R_dst)` `:1280` is
  directional (`√(R_j/R_i) ≠ √(R_i/R_j)`); wave de-embed `exp(ikₙᵢdᵢ)·exp(ikₙⱼdⱼ)`
  `:1301-1302` is symmetric per-endpoint product. Source-witnessed; not test-exercised.
- **Law 5 — Grid-map independence.** Holds. The two C++ port loops carry no inter-entry
  accumulator; each `vi.S` depends only on its own port `data`, the `src_data` drive port,
  and the cached projection. Verified.
- **Do-not-hold: not a symmetric-Gram reduction; scale-axis identity element.** Both
  confirmed against source (no `symmetric_from_upper`; `|R|=0` skips the scale; `d_offset=0`
  → de-embed identity).

All laws hold on the operator per its signature. The gate is test-coverage of the
**assembly**, not law-correctness.

## Proposed changes

The audit UNBLOCKS a status refinement (`rough-in` → `rough-in (test-coverage-bounded)`):
gate-b is discharged (firm L1 `port_projection`), and gate-a is downgraded to a pure
test-coverage bound (assembly-level laws not directly exercised; output invariant
witnessed). This is NOT a flip to `firm` — the assembly fold is not test-exercised — so the
proposed-changes body is the refreshed `## Status` + Evidence + the new `verified_against:`
block, all inside the fence below. (Per the fence-parity guard: the closing fence sits after
the last edited section; the nested `verified_against:` block uses a ` ```yaml ` fence; I
confirmed balance.)

```edit:book/src/L4/sparameter_reduce.md
[replace the `## Status` section (lines 238-280, from "## Status" through the end of the "Scope: single-pipeline (driven) BY DESIGN" paragraph ending "...authors it as its own verb per that closed-negative finding.") with:]
## Status

`rough-in (test-coverage-bounded)`. **Reasoning (warrant-first):** the combinator's
**structure** is firm-on-positive-structure — the per-column linear-projection skeleton
(project `sᵢ·E`, subtract the drive-port self-term `−1`, apply the port-kind scaling, no
symmetric mirror) is read directly off the single positive `MeasureSParameter` body
(`postoperator.cpp:1246-1309`) with its two structurally-identical port-kind loops, and
every algebraic claim (§Algebraic laws) is a syntactic read-off of that body + the two
`GetSParameter` kernels. The `test-coverage-bounded` qualifier records the one remaining
gate:

- The **reduction-level assembly** (the self-term + port-kind scaling stitched onto the
  projection in `MeasureSParameter`) is **test-bounded at the assembly level**. The driven
  postprocess test `test/unit/test-postoperator.cpp` (`TEST_CASE("PostOperator",
  "[idempotent]")`, the `check_port_data` lambda `:189`, run over BOTH `lumped_port_vi`
  `:266` and `wave_port_vi` `:271`) asserts the reduction **OUTPUT** field `c.S` is
  **dimensionless** — `|S|` / `arg(S)` invariant under a `Dimensionalize`/`Nondimensionalize`
  round-trip (`:195-196` non-dim, `:228-230` dim "Scattering always non-dim / Phase unchanged
  by normalization"). This **directly witnesses law-3's output consequence** (the S-entry is
  a dimensionless scattering ratio; the source-side basis is `postoperatorcsv.cpp:213`
  `dim[k].S = data.S; // NONE`) across the lumped/wave variant axis. But the test uses
  `RandomMeasurement()` and does **NOT** call `MeasureSParameter`, so the **assembly fold**
  (the projection + the `−1` self-term + the `√(R_src/R_dst)` / `exp(ikₙd)` scaling) is not
  directly exercised; the projection *kernel* `GetSParameter` is unit-tested
  (`test/unit/test-lumpedportintegration.cpp:367,720`, `test/unit/test-romoperator.cpp:603`)
  but the *assembly* is integration-tested only (the full driven `Solve(mesh)`). The
  assembly-level laws are therefore output-witnessed but not assembly-witnessed — the
  `test-coverage-bounded` bound.

The **per-port projection L1 home is now FIRM** — `book/src/L1/port_projection.md` (landed
cycle-077; `firmness: firm`, firm-on-positive-structure) is the dual-pairing `⟨s, E⟩`
projection kernel this reduction folds, and it explicitly satisfies this verb's former
gate-b (`port_projection.md:61-64,219-221,343-345`). The OQ
`sparameter-reduce-l1-port-projection-home` is **resolved** by that entry. The verb no
longer inherits reduced maturity from an absent constituent home — only the assembly-level
test bound remains, which is exactly the `rough-in (test-coverage-bounded)` situation
(structure firm-on-positive-structure; laws test-gated, per the `eigsolve` /
`matrix-weighted-norm` precedent).

Promotion route to `firm`: a dedicated S-matrix-**assembly** test exercising
`MeasureSParameter` at the reduction entry point (the self-term + port-kind scaling applied
to a known projection), OR a lowering-verifier pass raising the assembly-level law confidence
to `frequency_sweep`-equivalent. (Note the firm-on-positive-structure escape would apply if
the assembly laws were purely syntactic identities on fully-specified positive source — they
are read off `MeasureSParameter`, but the self-term + scaling stitching crosses the cached
projection from the per-port measure pass, so the assembly is treated as integration-level
until the assembly test or a confidence-raising audit lands. The current audit raised
confidence on the OUTPUT invariant + discharged gate-b but did not exercise the assembly,
hence `rough-in (test-coverage-bounded)`, not `firm`.)

**Scope: single-pipeline (driven) BY DESIGN** — S-parameters are a driven-solver output
product; there is no cross-pipeline generalization (the
`disciplined-cross-pipeline-combinator-mining-gate` single-witness probe resolves to
"within-pipeline output-product reduction with a port-kind variant axis", NOT a deferred
cross-pipeline mine). The **lumped-vs-wave split is a variant axis** (two assembly variants
of the SAME driven postprocess), NOT a 2nd pipeline. This is the driven member of the L4
output-product reduction cohort alongside `gram_reduce` (electrostatic/magnetostatic
capacitance/inductance) and `eigenfreq_qfactor_reduce` (eigenmode `(f,Q)`); the S-parameter
linear projection was probed as a `gram_reduce` 3rd-witness and CORRECTLY refused (different
fold) — this chapter authors it as its own verb per that closed-negative finding.

verified_against:

```yaml
verified_against:
  - citation: palace/models/postoperator.cpp:1246-1309
    verdict: supports
    audited_at: 2026-06-03T16:58:37Z
    note: MeasureSParameter def+body+close-brace; on-disk close-brace at :1309. Self-term :1275 (lumped) / :1297 (wave); generalized-S scale :1280 guarded |R|>0 at :1278; wave de-embed :1301-1302. Every Algebraic-laws claim is a syntactic read-off of this single positive body.
  - citation: palace/models/lumpedportoperator.cpp:283-294
    verdict: supports
    audited_at: 2026-06-03T16:58:37Z
    note: LumpedPortData::GetSParameter, the lumped (*s)E linear functional folded by the reduction; dot construction :287-291, close :294. Its L1 port_projection home is now firm (cycle-077).
  - citation: palace/models/waveportoperator.cpp:780-793
    verdict: supports
    audited_at: 2026-06-03T16:58:37Z
    note: WavePortData::GetSParameter, the wave (E x H_inc*)n projection folded by the reduction; 2x2 real recombination :789-790, close :793.
  - citation: test/unit/test-postoperator.cpp:188-271
    verdict: partially-supports
    audited_at: 2026-06-03T16:58:37Z
    note: TEST_CASE PostOperator [idempotent] check_port_data lambda (:189), run over BOTH lumped_port_vi (:266) and wave_port_vi (:271). Asserts the reduction-OUTPUT field c.S is dimensionless (|S| :195 non-dim / :228 dim, arg(S) :196/:230 phase-unchanged) under Dimensionalize round-trip. Witnesses law-3 OUTPUT invariant only; uses RandomMeasurement() and does NOT call MeasureSParameter, so the assembly fold is NOT exercised. Gate-a stays test-coverage-bounded.
  - citation: palace/models/postoperatorcsv.cpp:213
    verdict: supports
    audited_at: 2026-06-03T16:58:37Z
    note: dim[k].S = data.S; // NONE in Measurement::Nondimensionalize port-data loop (:200-226) - the source-side basis for the dimensionless-S test invariant; S carries no unit scale factor.
  - citation: book/src/L1/port_projection.md:1-354
    verdict: supports
    audited_at: 2026-06-03T16:58:37Z
    note: firm L1 port_projection entry (cycle-077) discharges gate-b - the per-port projection now HAS a firm L1 home (:61-64, :219-221, :343-345 state it satisfies this verb's gate-b). The former Status gate-2 is resolved.
  - citation: test/unit/test-postoperatorcsv.cpp:22-138
    verdict: does-not-support
    audited_at: 2026-06-03T16:58:37Z
    note: PostOperatorCSV<DRIVEN> fixture exercises port-V.csv (port_V/port_I, row_i, nr_expected_measurement_rows, InitializePortVI restart plumbing), NOT port-S.csv S-reduction output. The S-reduction-table coverage is out-of-range here; nearest port-S.csv content is a synthetic literal in test-basesolver.cpp:40.
```
```

Additionally, the theme's **Status-preamble line at the top of the file** should be checked
by the integrator: the dep-map status token currently reads `rough-in` in the L4 index
(`book/src/L4/index.md:104`), which carries the now-stale rationale "the per-port projection
L1 homes are not yet firm". That is an integrator carry-forward correction (see Open
questions), not an edit I make from the theme file.

## Coupled re-check — `book/src/feature/sparameters.{L4,L1,L0}.md` (status `seed`)

- **Down-links**: already **live links** (`[`sparameter_reduce`](../L4/sparameter_reduce.md)`)
  throughout all three column files — NO plain-text→live-link upgrade needed. The L1 column
  links the port-mode projection to `bilinear-form` (rough-in), NOT to the now-firm
  `port_projection`; that is a **stale down-link target** (see proposed change below).
- **Column promotion `seed` → ?**: **keep `seed`.** The column files state the promotion
  rule explicitly ("a feature column may promote past `seed` only once ALL its composed
  constituents are firm", `sparameters.L4.md:54,67`). After this audit the constituent
  `sparameter_reduce` is `rough-in (test-coverage-bounded)` — refined, but still not `firm`.
  So the column stays `seed` by its own stated rule. Its qualifier text should be refreshed
  from "rough-in ... no dedicated S-parameter-reduction test" to the more precise
  "`rough-in (test-coverage-bounded)` ... reduction-output invariant test-witnessed, assembly
  test-bounded" — a precision refresh, not a promotion.

Proposed (small, evidenced) refreshes the integrator MAY apply (NOT promotions):

```edit:book/src/feature/sparameters.L1.md
[in the `composes:` frontmatter, the line:]
  - book/src/L1/bilinear-form.md (rough-in — the port-mode projection ⟨sₖ, E⟩ = the linear-functional / inner-product against the port covector)
[should become:]
  - book/src/L1/port_projection.md (firm — the port-mode projection ⟨s, E⟩, the dual-pairing/linear-functional primitive the reduction folds; the FIRM L1 home as of cycle-077, replacing the earlier bilinear-form approximation)
```

(The L1 column body at `:39,60,64` also references `bilinear-form` as the port-mode
projection; repointing those prose mentions to `port_projection` is a larger surgical edit —
I flag it as a follow-up below rather than proposing the full prose rewrite here, to stay
within the bounded-correction boundary.)

## Supporting evidence

Files consulted (read or codemap `read_range` / `citecheck --anchor`):

- `reference/palace/palace/models/postoperator.cpp:1246-1309` — `MeasureSParameter`
  (the reduction assembly), full body read on-disk; close-brace confirmed `:1309`.
- `reference/palace/palace/models/postoperatorcsv.cpp:162,200-226` —
  `Measurement::Nondimensionalize` port-data loop; `dim[k].S = data.S; // NONE` `:213`.
- `reference/palace/palace/models/lumpedportoperator.cpp:283-294` +
  `waveportoperator.cpp:780-793` — the two `GetSParameter` projection kernels.
- `reference/palace/test/unit/test-postoperator.cpp:145,147,149-150,189,194-196,226-230,266,271`
  — the postprocess test (`RandomMeasurement` setup; `check_port_data`; the S-field
  dimensional-invariance assertions; both port-kind invocations).
- `reference/palace/test/unit/test-postoperatorcsv.cpp:22-138` — the CSV fixture (port-V/I
  plumbing; no port-S).
- `reference/palace/test/unit/test-basesolver.cpp:40,55-56,62,65` — the only `port-S.csv`
  content in the test tree (synthetic literal, restart/symlink test).
- `reference/palace/test/unit/test-lumpedportintegration.cpp:367,720` +
  `test-romoperator.cpp:603` — the projection-KERNEL unit tests (already cited by the theme).
- `book/src/L1/port_projection.md` — the firm L1 projection home (gate-b discharge).
- `book/src/L4/index.md:104` — the dep-map row carrying the stale rationale.
- `book/src/feature/sparameters.{L4,L1,L0}.md` — the seed output-product column.
- `tools/citecheck/citecheck.py --anchor` — clean `[ok]` on every primary anchor asserted
  (`MeasureSParameter`, `vi.S.real`, `std::sqrt`, `check_port_data`, `std::abs(c.S)`,
  `Scattering always non-dim`, `idempotent`).

## Open questions / caveats

1. **Integrator carry-forward — L4 index dep-map status refresh.** `book/src/L4/index.md:104`
   carries the verb's status as `rough-in` with the rationale "the per-port projection L1
   homes are not yet firm" (now stale — gate-b discharged) and "the reduction-level assembly
   ... is integration-level / test-unconfirmed". After this audit the row should read
   `rough-in (test-coverage-bounded)` with the gate-b clause dropped. One theme per
   invocation, so I do not edit the index from this audit; flagging it as the matching
   carry-forward so the index and the chapter stay consistent.

2. **Follow-up dispatch — L1 column down-link repoint (prose).** `sparameters.L1.md:39,60,64`
   references `bilinear-form` (rough-in) as the port-mode projection; the firm L1 home is now
   `port_projection`. I proposed the frontmatter `composes:` repoint above; the prose
   mentions are a larger surgical edit best done by a follow-up `layer-intro-author` /
   `lifter` pass on the column (within the bounded-correction boundary, but beyond what this
   audit should rewrite wholesale).

3. **Gate-a promotion to `firm` is GATED, not enacted.** The only path to `firm` is a
   dedicated `MeasureSParameter`-assembly test (out of project write-scope — there is no
   such test, and authoring one is out of scope per the dispatch + decision (e)), OR a future
   confidence-raising audit. This audit discharged the 2nd gate to the extent the EXISTING
   tests permit (output invariant + gate-b), which is exactly `rough-in
   (test-coverage-bounded)` — the OQ `sparameter-reduce-status-promotion-double-gated`
   resolves to "single-gated now (assembly-test only); refined to test-coverage-bounded".

4. **Direction-of-definition: clean.** The theme narrates the rewrite forward (L4 →
   per-port projection + scalar maps, "Lowers to" §). No high→low violation observed.

5. **Minor anchor precision (non-blocking).** The theme cites the lumped projection body as
   `:285-293`; the actual `dot` construction is `:287-291`. Both inside the def range; not a
   drift, just a slightly loose body range. The firm L1 `port_projection` uses `:285-293`
   for the same body, so they are consistent with each other — left as-is.
