---
agent: lowering-verifier
invoked_at: 2026-06-03T205952Z
scope: L4 verb law-confidence deepen-audit — sparameter_reduce (A1, output-product-reduce-verb cohort lead)
status: pending
integrated_at: 2026-06-03T212210Z
integration_commit: PLACEHOLDER_SHA
integration_notes: "cycle-083 (batch-26 pos 2/3). Applied clean (D1, COUNT OWNER). sparameter_reduce PROMOTED rough-in (test-coverage-bounded) → firm via the firm-on-positive-structure / syntactic-identity escape (laws syntactic identities / closed-form arithmetic over firm port_projection c077 + positive MeasureSParameter assembly source); L4 firm 15→16 main / 19→20 grand; coupled sparameters.{L4,L1,L0} verb-token refresh + sparameters.L0.md:28 bilinear-form→port_projection citation correction; column STAYS seed (promotion-rule prose held for the batch-26 feature-column-promotion-break-the-seed-deadlock directive). A1 half of output-product-reduce-verb-test-coverage-bounded-promotion-route RESOLVED-BY-AUDIT. retroactive-budget 0; build exit 0."
inputs:
  - book/src/L4/sparameter_reduce.md (the verb under audit; status rough-in (test-coverage-bounded))
  - palace/models/postoperator.cpp:1246-1309 (MeasureSParameter — the positive assembly source)
  - palace/models/lumpedportoperator.cpp:283-294 + palace/models/waveportoperator.cpp:780-793 (the two GetSParameter projection kernels folded)
  - palace/models/postoperator.cpp:1141,1239 (the per-port projection cache writes the assembly reads)
  - book/src/L1/port_projection.md (firm L1, c077 — the folded projection primitive; gate-b)
  - test/unit/test-postoperator.cpp:188-271 (the [idempotent] output-invariance test)
  - book/src/L4/eigenfreq_qfactor_reduce.md (the A2 c082 precedent — the SAME escape route)
  - book/src/L1/matrix-weighted-norm.md (the c080 contrast — the escape RULED OUT)
  - book/src/L4/index.md (the firm/rough-in tally + dep-map status-cell)
  - book/src/feature/sparameters.{L4,L1,L0}.md (the coupled feature column, status seed)
---

# CYCLE: Audit sparameter_reduce

## Summary

Law-confidence deepen-audit on the L4 driven output-product reduction verb
`sparameter_reduce` (currently `rough-in (test-coverage-bounded)`), resolving the A1 half
of OQ `output-product-reduce-verb-test-coverage-bounded-promotion-route`: can the
**firm-on-positive-structure / syntactic-identity escape** — the same route that promoted
its sibling `eigenfreq_qfactor_reduce` (A2) to `firm` in c082 — discharge the assembly-test
gate, rather than waiting on an out-of-write-scope `MeasureSParameter`-entry-point test?

**Verdict: PROMOTE to `firm`** (fully-supported). I read the single positive assembly body
`MeasureSParameter` on-disk (`postoperator.cpp:1246-1309`, def + close-brace
citecheck-confirmed), the two `GetSParameter` projection kernels
(`lumpedportoperator.cpp:283-294`, `waveportoperator.cpp:780-793`), and the projection-cache
writes the assembly reads (`:1141`/`:1239`). **Every one of the verb's 5 algebraic laws + 2
do-not-hold laws is a syntactic identity / closed-form arithmetic read-off** over (a) the
firm folded primitive `port_projection` (firm L1, c077 — gate-b discharged) and (b) the
fully-specified positive `MeasureSParameter` body. **No law smuggles in an unverified
mathematical-property axiom** — there is no inner-product axiom, no norm inequality, no
positivity/SPD claim conditional on a numerically-asserted structure (the exact failure mode
that ruled out the escape for the c080 sibling `matrix-weighted-norm`, whose laws 4/6/7 are
inner-product theorems conditional on SPD `B` only numerically asserted). The self-term
(literal `vi.S.real() - 1.0`), the generalized-S scale (literal `sqrt(R_src/R_dst)`), and the
de-embed (literal `exp(i·kn0·d_offset)`) are bare scalar arithmetic over the firm projection
— structurally identical to A2's `quality_factor = freq_re / |kappa|` bare-arithmetic-over-
firm-halves assembly. The verb's own Status flags the "cached projection crossing" as a prior
toward the ceiling; on-disk inspection shows the cache write is the firm primitive output
**verbatim with no intervening transform** (`vi.S = data.GetSParameter(*E)`), so the crossing
is an evaluation-strategy/data-flow detail, NOT an algebraic axiom — it does not gate the
syntactic-identity laws. The `[idempotent]` test (`RandomMeasurement()`, never calls
`MeasureSParameter`) is output-invariance documentation, not the firming basis — the same
disposition the c082 A2 audit gave its `[idempotent]` test. Promotion edits: flip the chapter
`## Status` to `firm` + emit a fresh `verified_against:` block; bump `L4/index.md` firm tally
`15 + 4 → 16 + 4` + flip the dep-map status-cell; record the verb firmed in the `sparameters`
feature column **without** changing the column status (`seed`) or its promotion-rule prose
(deferred to batch-26 meta per the pending user directive).

## Per-citation audit

- **Citation**: `palace/models/postoperator.cpp:1246-1309` (`MeasureSParameter`)
  - **Theme claim**: the single positive assembly body; every Algebraic-laws claim is a
    syntactic read-off of it; self-term `:1275`/`:1297`, generalized-S scale `:1280` guarded
    `:1278`, wave de-embed `:1301-1302`.
  - **Found**: `void PostOperator<solver_t>::MeasureSParameter() const` def at `:1246`,
    close-brace at `:1309` (citecheck `--anchor 'MeasureSParameter'` OK + on-disk `awk` of
    `:1263-1309`). The body: drive-port index `:1263`; lumped loop `:1267-1286` with self-term
    `if (idx == drive_port_idx) vi.S.real(vi.S.real() - 1.0)` at `:1273-1276` (the literal `-1`
    is `:1275`), generalized-S `if (std::abs(data.R) > 0.0) vi.S *= std::sqrt(src_data.R /
    data.R)` at `:1278-1281` (scale `:1280`, guard `:1278`); wave loop `:1287-1307` with
    self-term `:1295-1298` (literal `:1297`), de-embed `vi.S *= std::exp(1i * kn0 * d_offset)`
    twice (src `:1301`, dst `:1302`). The single-excitation + lumped-XOR-wave preconditions
    `:1256-1259`. **All line pinpoints exact on-disk.**
  - **Verdict**: supports
  - **Notes**: The assembly operates on the CACHED `vi.S` (read from
    `measurement_cache.{lumped,wave}_port_vi.at(idx)`), then applies the literal `-1` and the
    literal `*= scale`. Each operation is bare scalar arithmetic — no axiom, no
    numerically-asserted mathematical structure. This is the decisive read for the escape.

- **Citation**: `palace/models/lumpedportoperator.cpp:283-294` (`LumpedPortData::GetSParameter`)
  - **Theme claim**: the lumped `(*s)·E` linear functional folded by the reduction; its L1
    `port_projection` home is now firm.
  - **Found**: def `:283`, close-brace `:294` (citecheck + on-disk). Body returns the **pure
    projection** `std::complex<double> dot((*s)*E.Real(), 0.0)` (`:287`) with imag part
    `dot.imag((*s)*E.Imag())` (`:290`) when `E.HasImag()`, `Mpi::GlobalSum` `:292`. **NO
    self-term, NO scale** inside the kernel — exactly the firm `port_projection` dual pairing
    `⟨s, E⟩`.
  - **Verdict**: supports
  - **Notes**: This is the structural confirmation that the projection is a firm primitive
    and the self-term/scale live entirely in the assembly — so the assembly arithmetic
    composes a firm primitive, the A2 parallel.

- **Citation**: `palace/models/waveportoperator.cpp:780-793` (`WavePortData::GetSParameter`)
  - **Theme claim**: the wave `(E×H_inc⋆)·n` projection folded by the reduction; complex
    recombination `:789-790`.
  - **Found**: def `:780`, close-brace `:793` (citecheck + on-disk). Body returns the **pure**
    complex `(E×H_inc⋆)·n` projection: `dot(-((*port_sr)*port_E->Real()) -
    ((*port_si)*port_E->Imag()), -((*port_sr)*port_E->Imag()) + ((*port_si)*port_E->Real()))`
    at `:789-790`, `Mpi::GlobalSum` `:791`. **NO self-term, NO scale** — the wave port-kind
    variant of the same dual-pairing fold.
  - **Verdict**: supports
  - **Notes**: confirms the lumped-vs-wave split is a projection-kernel variant axis (the
    fold element), with the self-term/scale uniformly applied by the assembly.

- **Citation**: `palace/models/postoperator.cpp:1141` + `:1239` (the projection cache writes)
  - **Theme claim**: the two-phase project-then-postscale cache; projection computed per port
    in the measure pass, consumed by `MeasureSParameter`.
  - **Found**: `vi.S = data.GetSParameter(*E)` at `:1141` (in `MeasureLumpedPorts`) and
    `:1239` (in `MeasureWavePorts`). The cached value is the firm primitive's output
    **verbatim** — no transformation between the cache write and the `MeasureSParameter` read.
  - **Verdict**: supports
  - **Notes**: This is the on-disk resolution of the verb's own "cached projection crossing"
    ceiling-prior. Because the cache holds the firm primitive output unchanged, the crossing
    introduces NO untested semantic content — it is an eager-vs-cached evaluation-strategy
    detail the L4 reduction form correctly abstracts over. The crossing does not gate the
    syntactic-identity laws.

- **Citation**: `book/src/L1/port_projection.md:1-354` (firm L1, c077)
  - **Theme claim**: gate-b discharged — the per-port projection now has a firm L1 home that
    explicitly satisfies this verb's gate-b (`:61-64`).
  - **Found**: `firmness: firm`; the entry IS the dual-pairing `⟨s, E⟩` primitive; `:61-64`
    state "That reduction's gate-b ... is satisfied by this entry." Lifts both `GetSParameter`
    kernels (`:27-28`).
  - **Verdict**: supports
  - **Notes**: The verb's ONE folded primitive is firm L1 — the structure-side gate is fully
    discharged, exactly the A2 precondition (A2 had both folded halves firm; A1 has its one
    folded projection-kernel firm, with the self-term/scale being literal scalar maps, not
    primitives needing a home).

- **Citation**: `test/unit/test-postoperator.cpp:188-271` (`[idempotent]` round-trip)
  - **Theme claim**: witnesses the reduction-OUTPUT invariant (S dimensionless) but does NOT
    call `MeasureSParameter`, so the assembly fold is not exercised.
  - **Found**: `check_port_data` lambda `:189`; `|S|`/`arg(S)` invariant `:195-196` (non-dim)
    and `:227-230` (dim, comments "Scattering always non-dim" `:228` / "Phase unchanged by
    normalization" `:230`); run over `lumped_port_vi` `:266` + `wave_port_vi` `:271`. The
    fixture uses `RandomMeasurement()` (`:147`); `grep` confirms NO `MeasureSParameter` /
    `Measure*` assembly call anywhere in the file.
  - **Verdict**: partially-supports
  - **Notes**: output-witness only (the S-entry is a dimensionless scattering ratio); NOT the
    firming basis. Identical disposition to the c082 A2 audit's `[idempotent]` test. Per
    CLAUDE.md "Tests as semantic supplement" this remains supporting documentation alongside
    the syntactic-identity escape, not the gate.

- **Citation**: `palace/models/postoperatorcsv.cpp:213`
  - **Theme claim**: `dim[k].S = data.S; // NONE` — source-side basis for the dimensionless-S
    output invariant.
  - **Found**: `dim[k].S = data.S;  // NONE` at `:213` (citecheck `--anchor 'NONE'` OK).
  - **Verdict**: supports
  - **Notes**: confirms S carries no unit scale factor; supporting the output-witness.

## Applicability conditions

- **Condition**: single-excitation-per-port — S measured only when
  `GetPortExcitations().IsMultipleSimple()` (`postoperator.cpp:1256`).
  - **Verifiable**: yes — read on-disk at `:1256-1259` (the guard `if (!IsMultipleSimple() ||
    !(lumped xor wave)) return;`). The signature precondition matches.
  - **Found counter-example?**: no.

- **Condition**: whole-model one port-kind — all-lumped XOR all-wave (Palace forbids mixing,
  `postoperator.cpp:1256-1259`).
  - **Verifiable**: yes — the `xor` guard at `:1257-1258` and the two separate
    non-combined loops. The port-kind is a model-level variant axis, not a per-entry branch.
  - **Found counter-example?**: no.

- **Condition**: the lumped-vs-wave split is a variant axis (two assembly variants of the
  SAME driven postprocess), NOT a 2nd pipeline.
  - **Verifiable**: yes — the two loops differ ONLY in the projection kernel (`(*s)·E` vs
    `(E×H⋆)·n`) and the scale (`√(R_src/R_dst)` vs `exp(ikₙd)`); both apply the same self-term
    `−1` and the same independent-entry collect. Confirmed on-disk `:1267-1307`.
  - **Found counter-example?**: no.

## Algebraic laws

The discriminating test (the c082 A2 / c080 matrix-weighted-norm test): **does any law smuggle
in an unverified mathematical-property axiom (a theorem conditional on a numerically-asserted
structure)?** For each law:

- **Law 1 — Linearity in the field (per column).** `project sᵢ E = sᵢ·E` is linear in `E`.
  **Holds**: this is the firm `port_projection` dual-pairing `⟨s, E⟩ = Σ sᵢ Eᵢ`, literally a
  sum-of-products in `E` (`lumpedportoperator.cpp:287-290`). Linearity is the firm primitive's
  established property, inherited — a structural read-off, NOT a numerically-asserted axiom.
  PASSES the escape.
- **Law 2 — No symmetry-by-construction.** A NEGATIVE structural claim (no
  `symmetric_from_upper`). **Holds**: read off the body — each entry computed independently
  (one drive-column per solve, all receiver rows), no mirror construction. The `Sᵢⱼ ≈ Sⱼᵢ`
  near-symmetry is reciprocity physics, NOT a construction the verb imposes. Structural
  read-off. PASSES.
- **Law 3 — Inhomogeneous diagonal (`−1` self-term).** **Holds**: literal `vi.S.real(vi.S.real()
  - 1.0)` at `:1275` (lumped) / `:1297` (wave), gated `if (idx == drive_port_idx)`. The L4 law
  claims only the FOLD STRUCTURE (an affine `−1` at the diagonal), NOT the physical correctness
  of the scattering value — exactly the discipline A2 used (it claimed `Q = ω/κ` as the fold,
  not Q's physical correctness). Literal arithmetic read-off. PASSES.
- **Law 4 — Directional (asymmetric) scaling.** **Holds**: lumped `√(R_src/R_dst)` literal
  `:1280`; the directionality `√(R_j/R_i) ≠ √(R_i/R_j)` is an arithmetic property of
  `sqrt`-of-ratio (trivially true, not a numerically-asserted structure). Wave
  `exp(ikₙᵢdᵢ)·exp(ikₙⱼdⱼ)` `:1301-1302` symmetric-product form, syntactic. PASSES — no
  inner-product/positivity axiom.
- **Law 5 — Grid-map independence.** **Holds**: each entry depends only on `(ports!!i,
  ports!!j, e)`; the two C++ loops carry no inter-entry accumulator (`:1267-1307`). Structural
  read-off of the list-map spine. PASSES.
- **do-not-hold 1 — Not a symmetric-Gram reduction.** A negative structural read-off (no
  `symmetric_from_upper`, no family-PAIR bilinear). PASSES (c074 D6 closed-negative).
- **do-not-hold 2 — Scale-axis identity element.** **Holds**: read off the `|R| > 0` guard
  `:1278` (skip scale when non-resistive) and `d_offset = 0 ⇒ exp(0) = 1` wave default
  `:1301-1302`. Literal read-off. PASSES.

**No law requires a theorem conditional on a numerically-asserted structure.** Contrast the
c080 `matrix-weighted-norm` laws 4/6/7 (triangle / Cauchy–Schwarz / parallelogram) — those are
inner-product axioms holding only if `B` is genuinely SPD, a structure the L0 source merely
`MFEM_ASSERT(dot > 0.0)`-asserts. `sparameter_reduce` has no such axiom-needing law. **The
firm-on-positive-structure / syntactic-identity escape applies — promote to `firm`.**

## Proposed changes

Three coupled edits: (1) flip the `sparameter_reduce` chapter `## Status` to `firm` + replace
its `verified_against:` block; (2) bump the `L4/index.md` firm tally + flip the dep-map
status-cell; (3) record the verb firmed in the `sparameters` feature column **without**
touching the column status or promotion-rule prose.

### Edit 1 — `book/src/L4/sparameter_reduce.md`: flip Status to firm + fresh verified_against

Also flip the frontmatter `firmness:` line and the `## Status` heading line. The replacement
`## Status` body + `verified_against:` block (the firm body lands inside this fence; the
nested ` ```yaml ` is the channel-mandated fenced form for the verified_against block):

````edit:book/src/L4/sparameter_reduce.md
[replace frontmatter line]
firmness: rough-in
[with]
firmness: firm

[replace the entire `## Status` section — from the `## Status` heading through the closing ``` of the verified_against block — with]
## Status

`firm`. **Reasoning (firm-on-positive-structure / syntactic-identity escape):** the
combinator's **structure** is read directly off the single positive `MeasureSParameter` body
(`postoperator.cpp:1246-1309`, def + close-brace) with its two structurally-identical
port-kind loops, and **every** law (§Algebraic laws) is a **syntactic identity** / closed-form
arithmetic read-off — NO law smuggles in an unverified mathematical-property axiom:

- law 1 (linearity in the field) inherits the firm L1 [`port_projection`](../L1/port_projection.md)
  (c077) dual-pairing's established linearity `⟨s, E⟩ = Σ sᵢ Eᵢ` — a firm-primitive property,
  not a numerically-asserted axiom;
- law 2 (no symmetry-by-construction) + do-not-hold 1 (not a symmetric-Gram) are NEGATIVE
  structural read-offs of the independent-entry assembly (no `symmetric_from_upper`, no
  family-PAIR bilinear; `:1267-1307`);
- law 3 (inhomogeneous `−1` diagonal) is the literal `vi.S.real(vi.S.real() - 1.0)`
  (`:1275` lumped / `:1297` wave) — the L4 law claims the FOLD STRUCTURE (an affine `−1` at the
  diagonal), not the physical correctness of the scattering value;
- law 4 (directional scaling) reads the literal `√(R_src/R_dst)` (`:1280`, guarded `:1278`) and
  the wave de-embed `exp(ikₙd)` (`:1301-1302`) — arithmetic properties of `sqrt`-of-ratio and
  the symmetric exponential product, no inner-product/positivity axiom;
- law 5 (grid-map independence) + do-not-hold 2 (scale-axis identity) are read off the
  no-inter-entry-accumulator loops and the `|R| > 0` / `d_offset = 0` guards.

The reduction-level **assembly** — the self-term + port-kind scaling stitched onto the cached
projection in `MeasureSParameter` — is **bare scalar arithmetic over a firm primitive**: the
cache write `vi.S = data.GetSParameter(*E)` (`:1141` lumped / `:1239` wave) holds the firm
[`port_projection`](../L1/port_projection.md) output **verbatim with no intervening transform**,
and `MeasureSParameter` reads that cached value and applies the literal `-1.0` and `*= scale`.
The "cached projection crossing" is therefore an **evaluation-strategy / data-flow** detail the
L4 reduction form correctly abstracts over (eager-vs-cached), NOT an algebraic axiom — it does
not gate the syntactic-identity laws. This is the same escape that landed the SIBLING
[`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) firm (c082 — bare scalar arithmetic
`quality_factor = freq_re / |κ|` over two firm halves), and the same escape that landed
[`eigenvalue-untransform`](../L1/eigenvalue-untransform.md) (c080),
[`assemble_frequency_operator`](./assemble_frequency_operator.md), and
[`frequency_sweep`](./frequency_sweep.md) firm. The contrast is the c080 SIBLING
[`matrix-weighted-norm`](../L1/matrix-weighted-norm.md) audit, which RULED OUT the escape
precisely because its norm-axiom laws (triangle / Cauchy–Schwarz / parallelogram) are theorems
conditional on an inner-product structure (SPD/Hermitian `B`) the L0 source only *numerically
asserts* — **no such theorem-needing-proof exists in this verb's assembly** (the self-term `−1`,
the `√(R_src/R_dst)` scale, the `exp(ikₙd)` de-embed are all literal scalar maps).

**Both structure-side gates were already discharged before this promotion:** gate-b — the
per-port projection L1 home — is FIRM via [`port_projection`](../L1/port_projection.md) (c077;
`:61-64` state it satisfies this verb's gate-b); the self-term/scale are literal scalar maps,
not primitives needing a home. The earlier `rough-in (test-coverage-bounded)` qualifier was held
only on the absence of a dedicated S-matrix-**assembly** test. The driven postprocess test
`test/unit/test-postoperator.cpp` (`TEST_CASE("PostOperator", "[idempotent]")`, `check_port_data`
`:189` over lumped `:266` + wave `:271`) witnesses the reduction-**OUTPUT** invariant (`c.S`
dimensionless: `|S|`/`arg(S)` invariant under a `Dimensionalize` round-trip `:195-196`/`:227-230`,
source basis `postoperatorcsv.cpp:213` `// NONE`) but uses `RandomMeasurement()` (`:147`) and
**never calls `MeasureSParameter`**, so it does not exercise the assembly fold — it is
output-invariance documentation, NOT the firming basis. The cycle-083 lowering-verifier
law-confidence pass IS the promotion route the OQ
`output-product-reduce-verb-test-coverage-bounded-promotion-route` named: the audit finds the
assembly-level laws are syntactic identities over the firm projection + positive source,
carrying no residual untested semantic claim, so the firm-on-positive-structure escape
discharges the assembly-test gate (the SAME route as the c082 A2 promotion). The projection
*kernel* `GetSParameter` is additionally unit-tested
(`test/unit/test-lumpedportintegration.cpp:367,720`, `test/unit/test-romoperator.cpp:603`).

**Scope: single-pipeline (driven) BY DESIGN** — S-parameters are a driven-solver output
product; there is no cross-pipeline generalization (the
`disciplined-cross-pipeline-combinator-mining-gate` single-witness probe resolves to
"within-pipeline output-product reduction with a port-kind variant axis", NOT a deferred
cross-pipeline mine). The **lumped-vs-wave split is a variant axis** (two assembly variants of
the SAME driven postprocess), NOT a 2nd pipeline. This is the driven member of the L4
output-product reduction cohort alongside `gram_reduce` (electrostatic/magnetostatic
capacitance/inductance) and the firm `eigenfreq_qfactor_reduce` (eigenmode `(f,Q)`); the
S-parameter linear projection was probed as a `gram_reduce` 3rd-witness and CORRECTLY refused
(different fold) — this chapter authors it as its own verb per that closed-negative finding.

verified_against:

```yaml
verified_against:
  - citation: palace/models/postoperator.cpp:1246-1309
    verdict: supports
    audited_at: 2026-06-03T205952Z
    note: MeasureSParameter def+body+close-brace re-verified on-disk via citecheck --anchor (def :1246, close-brace :1309). The assembly fold reads the CACHED projection vi.S then applies bare scalar arithmetic - self-term vi.S.real(vi.S.real()-1.0) at :1275 (lumped) / :1297 (wave); generalized-S scale vi.S *= sqrt(src_data.R/data.R) at :1280 guarded |R|>0 at :1278; wave de-embed vi.S *= exp(1i*kn0*d_offset) at :1301-1302. Every Algebraic-laws claim is a syntactic read-off; the cache-crossing is an evaluation-strategy detail, not an axiom.
  - citation: palace/models/lumpedportoperator.cpp:283-294
    verdict: supports
    audited_at: 2026-06-03T205952Z
    note: LumpedPortData::GetSParameter (def :283, close-brace :294) returns the PURE projection dot((*s)*E.Real(), (*s)*E.Imag()) at :287-290 - NO self-term, NO scale. This is exactly the firm L1 port_projection dual pairing; the assembly's arithmetic composes this firm primitive.
  - citation: palace/models/waveportoperator.cpp:780-793
    verdict: supports
    audited_at: 2026-06-03T205952Z
    note: WavePortData::GetSParameter (def :780, close-brace :793) returns the PURE (E x H_inc*)n projection, complex recombination :789-790 - NO self-term, NO scale. Folded by the reduction as the wave port-kind projection variant.
  - citation: palace/models/postoperator.cpp:1141
    verdict: supports
    audited_at: 2026-06-03T205952Z
    note: vi.S = data.GetSParameter(*E) - the lumped per-port projection cache write in MeasureLumpedPorts. The cached value is the firm primitive output verbatim, with NO intervening transform before MeasureSParameter reads it; this is why the cache-crossing carries no untested semantic content (the c082 A2 bare-arithmetic-over-firm-halves parallel).
  - citation: palace/models/postoperator.cpp:1239
    verdict: supports
    audited_at: 2026-06-03T205952Z
    note: vi.S = data.GetSParameter(*E) - the wave per-port projection cache write in MeasureWavePorts. Same as lumped - the cached value is the firm primitive output verbatim.
  - citation: book/src/L1/port_projection.md:1-354
    verdict: supports
    audited_at: 2026-06-03T205952Z
    note: firm L1 port_projection (cycle-077, firmness firm) is the dual-pairing projection the reduction folds; :61-64 explicitly state it satisfies this verb's gate-b. The verb's ONE folded primitive is firm L1 - the structure-side gate is fully discharged, exactly the A2 precondition.
  - citation: test/unit/test-postoperator.cpp:188-271
    verdict: partially-supports
    audited_at: 2026-06-03T205952Z
    note: TEST_CASE PostOperator [idempotent] check_port_data lambda (:189), run over lumped_port_vi (:266) + wave_port_vi (:271). Asserts the reduction-OUTPUT field c.S is dimensionless (|S| :195/:227, arg(S) :196/:229, comments Scattering always non-dim / Phase unchanged) under Dimensionalize round-trip. Uses RandomMeasurement() (:147) and does NOT call MeasureSParameter - so the assembly fold is NOT exercised. Output-witness only; NOT the firming basis (the syntactic-identity escape is), the same disposition as the A2 [idempotent] test.
  - citation: palace/models/postoperatorcsv.cpp:213
    verdict: supports
    audited_at: 2026-06-03T205952Z
    note: dim[k].S = data.S; // NONE in the Nondimensionalize port-data loop - the source-side basis for the dimensionless-S output invariant; S carries no unit scale factor. Supporting evidence for the output-witness, not the firming basis.
```
````

(The chapter `## Evidence` section, the `## Dependencies` "rough-in rather than firm" sentence
about the absent L1 home, and the §Lowers to prose are unaffected EXCEPT the §Dependencies
clause "which is one of the two reasons the entry is `rough-in` rather than firm" — see Edit 1b.)

### Edit 1b — `book/src/L4/sparameter_reduce.md` §Dependencies: drop the stale rough-in clause

The §Dependencies prose still says the projection kernel "does **not yet have a firm L1 home**
... which is one of the two reasons the entry is `rough-in` rather than firm." `port_projection`
is firm (c077) and the entry is now firm. Correct the clause:

```edit:book/src/L4/sparameter_reduce.md
[replace]
The per-port projection kernel this folds — the port-mode **linear functional** `sᵢ·E`
(lumped `(*s)·E` `lumpedportoperator.cpp:283-294`; wave `(E×H⋆)·n`
`waveportoperator.cpp:780-793`) — does **not yet have a firm L1 home** (see OQ
`sparameter-reduce-l1-port-projection-home`); the reduction folds it directly off the two
`GetSParameter` bodies, which is one of the two reasons the entry is `rough-in` rather than
firm.
[with]
The per-port projection kernel this folds — the port-mode **linear functional** `sᵢ·E`
(lumped `(*s)·E` `lumpedportoperator.cpp:283-294`; wave `(E×H⋆)·n`
`waveportoperator.cpp:780-793`) — has a **firm L1 home**:
[`port_projection`](../L1/port_projection.md) (c077; OQ
`sparameter-reduce-l1-port-projection-home` resolved). The reduction folds that firm
primitive, and the cycle-083 lowering-verifier law-confidence pass found the assembly fold to
be bare scalar arithmetic over it (the firm-on-positive-structure escape), promoting the entry
to firm.
```

### Edit 2 — `book/src/L4/index.md`: firm tally + dep-map status-cell

`sparameter_reduce` joins the firm cohort. Bump the firm count `15 + 4 → 16 + 4`. (The §57
rough-in count line `1 + 1 test-coverage-bounded` does NOT change — `sparameter_reduce` was not
a bullet in that section; it lives only in the dep-map table. See Open questions for the tally
audit note.)

```edit:book/src/L4/index.md
[replace]
**Firm at L4 (15 + 4 outer-driver)** —
[with]
**Firm at L4 (16 + 4 outer-driver)** — cycle-083 promoted the driven output-product reduction [`sparameter_reduce`](./sparameter_reduce.md) to `firm` (the lowering-verifier law-confidence pass on the **firm-on-positive-structure / syntactic-identity escape** — every law a read-off over the firm L1 [`port_projection`](../L1/port_projection.md) (c077, gate-b) + the single positive `MeasureSParameter` body; the self-term `−1` + `√(R_src/R_dst)` scale + `exp(ikₙd)` de-embed are bare scalar arithmetic over the firm projection, no inner-product-axiom content — the A2 [`eigenfreq_qfactor_reduce`](./eigenfreq_qfactor_reduce.md) c082 parallel, the matrix-weighted-norm contrast). Before it,
```

Flip the dep-map status-cell (line 107) — replace the trailing status parenthetical:

```edit:book/src/L4/index.md
[replace]
| `rough-in (test-coverage-bounded)` (harvested cycle-075 D1 LEAD from the driven feature-chapter forward-mine flags `driven.L4.md:55,98,157`; structure firm-on-positive-structure on the single positive driven postprocess `postoperator.cpp:1246-1309` with two port-kind assembly variants; 2nd gate discharged cycle-079 D-sparameter-reduce — gate-b (the per-port projection L1 home) is now FIRM via `L1/port_projection.md` (cycle-077), and the existing driven postprocess test `test-postoperator.cpp` witnesses the reduction-OUTPUT invariant (S dimensionless, both port kinds) per batch-24 decision (e); only the *assembly* fold remains test-bounded (the test uses `RandomMeasurement()` and never calls `MeasureSParameter`; the projection KERNEL `GetSParameter` is unit-tested, `test-lumpedportintegration.cpp:367,720` + `test-romoperator.cpp:603`) — hence `test-coverage-bounded`, not `firm`. Single-pipeline BY DESIGN — driven only; the lumped-vs-wave split is a variant axis, NOT a 2nd pipeline. Over-unification guard: NOT a `gram_reduce` specialization — linear projection ≠ bilinear Gram) |
[with]
| `firm` (harvested cycle-075 D1 LEAD from the driven feature-chapter forward-mine flags `driven.L4.md:55,98,157`; structure firm-on-positive-structure on the single positive driven postprocess `postoperator.cpp:1246-1309` with two port-kind assembly variants; promoted firm cycle-083 D1 on the **firm-on-positive-structure / syntactic-identity escape** — gate-b (the per-port projection L1 home) is FIRM via `L1/port_projection.md` (cycle-077), and every law is a syntactic read-off over that firm projection + the single positive body: the self-term `−1` (`:1275`/`:1297`), the `√(R_src/R_dst)` scale (`:1280` guarded `:1278`), the `exp(ikₙd)` de-embed (`:1301-1302`) are bare scalar arithmetic over the firm projection (the cache write `:1141`/`:1239` holds the firm primitive output verbatim), carrying no inner-product-axiom content — the A2 `eigenfreq_qfactor_reduce` c082 parallel, the matrix-weighted-norm contrast. The driven postprocess test `test-postoperator.cpp` `[idempotent]` (`RandomMeasurement()`, never calls `MeasureSParameter`) is reduction-OUTPUT-invariance documentation (S dimensionless, both port kinds), NOT the firming basis; the projection KERNEL `GetSParameter` is unit-tested, `test-lumpedportintegration.cpp:367,720` + `test-romoperator.cpp:603`. Single-pipeline BY DESIGN — driven only; the lumped-vs-wave split is a variant axis, NOT a 2nd pipeline. Over-unification guard: NOT a `gram_reduce` specialization — linear projection ≠ bilinear Gram) |
```

Also update the reduce-to-matrix prose note (line 79) status-token for `sparameter_reduce`:

```edit:book/src/L4/index.md
[replace]
and [`sparameter_reduce`](./sparameter_reduce.md) (the per-column **linear-projection** scattering reduction — the driven S-parameter output product, `scale·(sᵢ·E − [i==j])`, no mirror). Same shape, different fold (the do-NOT-merge over-unification guard, `concepts/black-box-vs-accelerated-kernels.md` §2).
[with]
and [`sparameter_reduce`](./sparameter_reduce.md) *(firm, c083)* (the per-column **linear-projection** scattering reduction — the driven S-parameter output product, `scale·(sᵢ·E − [i==j])`, no mirror). Same shape, different fold (the do-NOT-merge over-unification guard, `concepts/black-box-vs-accelerated-kernels.md` §2).
```

### Edit 3 — `book/src/feature/sparameters.{L4,L1,L0}.md`: record the verb firmed; KEEP `seed` + promotion-rule prose

The column stays `seed` and the promotion-rule prose ("a feature column may promote past `seed`
only once ALL its composed constituents are firm") is **unchanged** per the pending batch-26
user directive. Only the **factual `(rough-in)` verb-status tokens** are corrected to `(firm)`,
and a one-line note flags the now-apparent tension for the batch-26 meta-phase. The `seed`
status-frontmatter and the `## Status` rationale's promotion RULE are left verbatim.

`sparameters.L4.md` — frontmatter `composes:` line + the `(rough-in)` tokens:

```edit:book/src/feature/sparameters.L4.md
[replace]
  - book/src/L4/sparameter_reduce.md (rough-in; chapter authored cycle-075 D6 — the port-projection reduction; projects each per-ω field onto the port modes → the scattering matrix S)
[with]
  - book/src/L4/sparameter_reduce.md (firm as of cycle-083 — the port-projection reduction; projects each per-ω field onto the port modes → the scattering matrix S)
```

```edit:book/src/feature/sparameters.L4.md
[replace]
The column is `seed` (not promoted past it) because [`sparameter_reduce`](../L4/sparameter_reduce.md) is itself `rough-in` — its per-port projection primitives and the port-kind closing are rough-in and there is no dedicated S-parameter-reduction test; a feature column may promote past `seed` only once ALL its composed constituents are firm.
[with]
The column is `seed`. NOTE (cycle-083): [`sparameter_reduce`](../L4/sparameter_reduce.md) was **promoted to `firm`** (the lowering-verifier firm-on-positive-structure escape) — so its constituent is now firm, but the column promotion-rule (a feature column may promote past `seed` only once ALL its composed constituents are firm) and the `seed` status are **held pending the batch-26 meta-phase** (a user directive to revise the column-promotion rule is pending; out of scope for the c083 dispatch). The earlier rough-in rationale is superseded by the firm promotion; the column-status reconciliation is the batch-26 item.
```

```edit:book/src/feature/sparameters.L4.md
[replace]
`seed` — an output-product **leaf feature column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02). The composition is sound: stage (1) consumes the [`driven.L4`](./driven.L4.md) driver column's per-ω solution family; stage (2) composes the [`sparameter_reduce`](../L4/sparameter_reduce.md) *(rough-in)* port-projection reduction (the port-projection sibling of the c074 energy-Gram reductions, NOT a `gram_reduce` weight specialization). The column stays `seed` (does not promote) because [`sparameter_reduce`](../L4/sparameter_reduce.md) is `rough-in` — its per-port projection primitives + port-kind closing are rough-in and no dedicated S-parameter-reduction test exists; a feature column may promote past `seed` only once ALL its composed constituents are firm.
[with]
`seed` — an output-product **leaf feature column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02). The composition is sound: stage (1) consumes the [`driven.L4`](./driven.L4.md) driver column's per-ω solution family; stage (2) composes the [`sparameter_reduce`](../L4/sparameter_reduce.md) *(firm, c083)* port-projection reduction (the port-projection sibling of the c074 energy-Gram reductions, NOT a `gram_reduce` weight specialization). The column stays `seed` pending the batch-26 meta-phase: `sparameter_reduce` is now `firm` (c083 lowering-verifier promotion), so its constituent is firm — but a user directive to revise the column-promotion rule (a feature column may promote past `seed` only once ALL its composed constituents are firm) is pending the batch-26 meta-phase, so the column-status reconciliation is held out of scope for c083.
```

The remaining `*(rough-in)*` tokens at L4 lines 39, 51, 52 are body-prose verb-status mentions;
correct them to `*(firm)*` for factual accuracy (status token only — no rule/prose change):

```edit:book/src/feature/sparameters.L4.md
[replace]
2. **The port-projection reduction** — [`sparameter_reduce`](../L4/sparameter_reduce.md) (**rough-in**). The L4 port-projection reduction
[with]
2. **The port-projection reduction** — [`sparameter_reduce`](../L4/sparameter_reduce.md) (**firm, c083**). The L4 port-projection reduction
```

```edit:book/src/feature/sparameters.L4.md
[replace]
- The reduction is [`sparameter_reduce`](../L4/sparameter_reduce.md) *(rough-in)*, a **projection against fixed port-mode covectors**, NOT a self-Gram fold.
[with]
- The reduction is [`sparameter_reduce`](../L4/sparameter_reduce.md) *(firm, c083)*, a **projection against fixed port-mode covectors**, NOT a self-Gram fold.
```

```edit:book/src/feature/sparameters.L4.md
[replace]
- The per-port-kind closing (lumped generalized-S normalization vs wave-port phase de-embedding) is the load-bearing port-kind axis of [`sparameter_reduce`](../L4/sparameter_reduce.md), absorbed into the reduction
[with]
- The per-port-kind closing (lumped generalized-S normalization vs wave-port phase de-embedding) is the load-bearing port-kind axis of [`sparameter_reduce`](../L4/sparameter_reduce.md) *(firm, c083)*, absorbed into the reduction
```

The L4 line-54 sentence "The column is `seed` ... because [`sparameter_reduce`] is itself
`rough-in`" is the §Composition-narrative duplicate of the line-39-area prose already corrected
above (Edit 3 first L4 replacement targets the line-54 sentence verbatim) — confirm the
integrator applies the matching block once.

`sparameters.L1.md` — the `*(rough-in)*` verb-status tokens at lines 39, 50 (the
`port_projection` constituent is already firm and unchanged; only the L4-verb token shifts):

```edit:book/src/feature/sparameters.L1.md
[replace]
At L4 this exact fold is named the [`sparameter_reduce`](../L4/sparameter_reduce.md) *(rough-in)* combinator (the port-projection sibling of `gram_reduce`); L1 sees the unfolded projection grid.
[with]
At L4 this exact fold is named the [`sparameter_reduce`](../L4/sparameter_reduce.md) *(firm, c083)* combinator (the port-projection sibling of `gram_reduce`); L1 sees the unfolded projection grid.
```

```edit:book/src/feature/sparameters.L1.md
[replace]
- **L4** ([`sparameters.L4`](./sparameters.L4.md)): the whole reduction is the [`sparameter_reduce`](../L4/sparameter_reduce.md) *(rough-in)* combinator (the projection grid + self-reflection + port-kind closing made *structural*).
[with]
- **L4** ([`sparameters.L4`](./sparameters.L4.md)): the whole reduction is the [`sparameter_reduce`](../L4/sparameter_reduce.md) *(firm, c083)* combinator (the projection grid + self-reflection + port-kind closing made *structural*).
```

The L1 `## Status` `seed`-rationale (line 64) names the WHOLE-grid reduction as "still
`rough-in`" — correct the factual token while KEEPING the promotion rule + `seed`:

```edit:book/src/feature/sparameters.L1.md
[replace]
The per-mode projection primitive is therefore firm; the column nonetheless stays `seed` because the whole-grid reduction it composes — [`sparameter_reduce`](../L4/sparameter_reduce.md) at L4, the projection grid + self-reflection + port-kind closing made structural — is still `rough-in`, and a feature column promotes past `seed` only once ALL its composed constituents are firm.
[with]
The per-mode projection primitive is firm; as of cycle-083 the whole-grid reduction it composes — [`sparameter_reduce`](../L4/sparameter_reduce.md) at L4 — is **also `firm`** (the lowering-verifier firm-on-positive-structure promotion). The column nonetheless stays `seed` pending the batch-26 meta-phase: the promotion rule (a feature column promotes past `seed` only once ALL its composed constituents are firm) and the column status are held for the pending column-promotion-rule user directive (out of scope for c083).
```

The L1 dep-map row line 60 ("self-reflection + port-kind closing | ... | rough-in |") is the
per-stage status of an UNNAMED arithmetic stage (the port-kind closing), not the
`sparameter_reduce` verb itself; it is absorbed-by-`sparameter_reduce` and the closing
arithmetic has no separate L1 home — leave it `rough-in` (it is not the verb's status, and
re-classifying the unnamed closing stage is out of this dispatch's scope).

`sparameters.L0.md` — the two `*(rough-in)*` L4-verb tokens at lines 28, 37, 46:

```edit:book/src/feature/sparameters.L0.md
[replace]
This is the L0 site the L1 [`bilinear-form`](../L1/bilinear-form.md) projection (and the L4 [`sparameter_reduce`](../L4/sparameter_reduce.md) *(rough-in)* lumped projection) lift.
[with]
This is the L0 site the L1 [`port_projection`](../L1/port_projection.md) (firm, c077) projection (and the L4 [`sparameter_reduce`](../L4/sparameter_reduce.md) *(firm, c083)* lumped projection) lift.
```

```edit:book/src/feature/sparameters.L0.md
[replace]
These are the L0 sites the L4 port-kind closing axis of [`sparameter_reduce`](../L4/sparameter_reduce.md) *(rough-in)* lifts.
[with]
These are the L0 sites the L4 port-kind closing axis of [`sparameter_reduce`](../L4/sparameter_reduce.md) *(firm, c083)* lifts.
```

```edit:book/src/feature/sparameters.L0.md
[replace]
and the L4 combinator composition root [`sparameters.L4`](./sparameters.L4.md) (the per-port projection + self-reflection + port-kind closing → the [`sparameter_reduce`](../L4/sparameter_reduce.md) *(rough-in)* port-projection combinator).
[with]
and the L4 combinator composition root [`sparameters.L4`](./sparameters.L4.md) (the per-port projection + self-reflection + port-kind closing → the [`sparameter_reduce`](../L4/sparameter_reduce.md) *(firm, c083)* port-projection combinator).
```

(NOTE: the L0 line-28 prose also said the lumped projection lifts "the L1 `bilinear-form`
projection" — that is a STALE pre-c077 reference; `port_projection` (firm, c077) is the correct
firm L1 home, per `sparameters.L1.md:8`. The Edit-3 L0 replacement above corrects it to
`port_projection`. This is a bounded, evidenced carry-forward citation correction within the
lifter-scope content-correction boundary.)

## Supporting evidence

- `palace/models/postoperator.cpp:1246-1309` — `MeasureSParameter` body (def + close-brace
  citecheck-confirmed; full on-disk `awk` of `:1263-1309`). The assembly fold over the cached
  projection.
- `palace/models/postoperator.cpp:1141`, `:1239` — the lumped / wave projection-cache writes
  `vi.S = data.GetSParameter(*E)` the assembly reads (firm primitive output verbatim).
- `palace/models/lumpedportoperator.cpp:283-294`, `palace/models/waveportoperator.cpp:780-793`
  — the two `GetSParameter` projection kernels (pure projection, no self-term/scale).
- `palace/models/postoperatorcsv.cpp:213` — `// NONE` (source basis for the dimensionless-S
  output invariant; citecheck `--anchor` confirmed).
- `book/src/L1/port_projection.md` — firm L1 (c077); `:61-64` discharge gate-b.
- `test/unit/test-postoperator.cpp:147,188-271` — `[idempotent]` output-invariance test
  (`RandomMeasurement()`; no `MeasureSParameter` call — confirmed by `grep`).
- `test/unit/test-lumpedportintegration.cpp:367,720`, `test/unit/test-romoperator.cpp:603` —
  the projection-kernel unit tests (cited unchanged; not re-verified this dispatch — inherited
  from the prior audit, in-range per the existing block).
- `book/src/L4/eigenfreq_qfactor_reduce.md` — the A2 c082 precedent (the SAME escape route;
  bare-arithmetic-over-firm-halves assembly).
- `book/src/L1/matrix-weighted-norm.md:108-118` — the c080 contrast (the escape RULED OUT;
  laws 4/6/7 inner-product axioms conditional on numerically-asserted SPD `B`).
- `book/src/L4/index.md:32,57,79,107` — the firm/rough-in tally + the dep-map status-cell +
  the reduce-to-matrix prose note.

## Open questions / caveats

- **OQ `output-product-reduce-verb-test-coverage-bounded-promotion-route` — A1 half RESOLVED.**
  The firm-on-positive-structure escape DOES promote `sparameter_reduce` to firm (matching the
  A2 c082 resolution). The OQ's broader cohort question (whether the escape generalizes as the
  STANDING promotion route for output-product reduce-verbs) now has BOTH A1 + A2 resolved
  affirmatively; the remaining cohort member `domain_energy_reduce` is gated DIFFERENTLY — its
  folded `matrix-weighted-norm` numerator-energy primitive is itself `rough-in
  (test-coverage-bounded)` (a reduction is as firm as its least-firm folded primitive), so the
  escape does NOT yet apply to it (the structure-side gate is not discharged — unlike A1/A2
  whose folded primitives are all firm). Recommend the OQ be narrowed to note: "the escape
  applies to an output-product reduce-verb iff ALL its folded L1 primitives are firm AND the
  assembly is bare arithmetic with no axiom-needing law; A1+A2 met this, `domain_energy_reduce`
  does not (yet)."
- **Tally audit note (for the integrator / cross-layer-cross-cutter).** The `L4/index.md` §57
  rough-in count `(1 + 1 test-coverage-bounded)` did NOT previously include `sparameter_reduce`
  — the verb was tracked only in the dep-map table (line 107) and the reduce-to-matrix prose
  note (line 79), never as a §57 bullet. So this promotion does NOT decrement the §57 count
  (it stays `1 + 1 test-coverage-bounded` = `domain_energy_reduce` rough-in + `solve_family`
  test-coverage-bounded). The firm count §32 increments `15 → 16`. This is a pre-existing
  asymmetry in how the index tracks the test-coverage-bounded verbs (the §57 line tracks 2 of
  the 3 test-coverage-bounded/rough-in verbs as bullets); flag for the cross-layer-cross-cutter
  coverage pass whether the §57 line should explicitly enumerate all rough-in/test-bounded
  verbs or remain a curated subset.
- **Column-promotion-rule tension (held for batch-26 meta-phase, per dispatch).** With
  `sparameter_reduce` now firm AND `port_projection` firm (c077), the `sparameters` feature
  column's only non-firm constituent is the unnamed "self-reflection + port-kind closing"
  arithmetic stage (which has no separate L1 home and is absorbed by the firm
  `sparameter_reduce`). Under the CURRENT column-promotion rule ("ALL constituents firm"), the
  column would now arguably be eligible to promote past `seed` — but the dispatch explicitly
  defers the column-promotion-rule revision to the pending batch-26 user directive. I have left
  the column `seed` + the rule prose verbatim and only corrected the factual verb-status tokens
  + flagged the tension. The batch-26 meta-phase should reconcile: does the firm
  `sparameter_reduce` (absorbing the closing arithmetic) discharge the column's last
  non-firm constituent, and does the revised rule then promote the column?
- **No direction-of-definition violation.** The chapter narrates forward (L4 → L1/L0): the
  combinator is defined in L4 vocabulary, lowering by identity-in-form to the per-port
  projection it folds. High→low discipline honored.
- **Inherited test citations not re-verified.** The projection-kernel unit-test citations
  (`test-lumpedportintegration.cpp:367,720`, `test-romoperator.cpp:603`) are carried forward
  from the prior audit unchanged; I did not re-`read_range` them this dispatch (they are not
  the firming basis — the syntactic-identity escape is — and they were in-range in the existing
  block). If the integrator wants them re-anchored, that is a bounded carry-forward check, but
  it does not affect the promotion verdict.
