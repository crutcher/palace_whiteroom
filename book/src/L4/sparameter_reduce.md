---
layer: L4
operator: sparameter_reduce
firmness: rough-in
consumes:
  - book/src/L4/frequency_sweep.md (firm — the driven solve-half map producing the per-ω solution family [E_ω] this reduction reduces over; the upstream composition-root stage)
lowers_to:
  - the per-port port-mode linear functional sᵢ·E (lumped (*s)·E / wave (E×H⋆)·n) by identity-in-form on the body; the per-entry self-term/scale is a scalar map. No dedicated L4>L3 theme — the in-line-marker route (the gram_reduce / inner_product / linear_combination pattern); in-line §"Lowers to"
variant_axes:
  - port-kind (lumped | wave — THE load-bearing axis; absorbed into the PortMode + scale closure; whole-model XOR, not per-port — Palace forbids mixing)
  - scaling-presence (generalized-S present/absent via |R| > 0 resistive guard; de-embed present/absent via d_offset ≠ 0 — absorbed into the scale closure; absent = the scale-axis identity)
  - element-type (complex — pinned; S-parameters intrinsically complex, unlike the real energy-Gram)
---

# sparameter_reduce

The L4 **driven per-port port-projection reduction combinator**: reduce a driven per-ω
solution family `[(j, Eⱼ)]` (one solve per drive-port column `j`) into the scattering
matrix `S`, where each entry `Sᵢⱼ = scale(i,j) · (project sᵢ Eⱼ − [i==j])` projects the
driven field onto each receiver port mode (`sᵢ·E`, a **linear** functional), subtracts the
drive-port self-term on the diagonal (the inhomogeneous incident-wave `−1`), and applies
the port-kind impedance/de-embed scaling. It is the **driven output-product reduction** —
the verb that turns the per-ω driven solves the frequency sweep produces into the
scattering matrix the user ran the driven solver to compute.

`sparameter_reduce` is a **pure value-producing reduction** (no `Solve` monad, no carry, no
convergence predicate) — the **reduce-to-matrix** member of the L4 algebra-of-folds family,
the **linear-projection sibling** of the bilinear symmetric-Gram
[`gram_reduce`](./gram_reduce.md) and the reduce-to-scalar
[`inner_product`](./inner_product.md). It rises to L4 as a **feature-surface verb the
backend wants** ([`black-box-vs-accelerated-kernels`](../concepts/black-box-vs-accelerated-kernels.md)
§"The combinators rise regardless"; directive-1: L4 is the outward backend-lowering
target) — the output-product half of the driven composition root
([`driven.L4`](../feature/driven.L4.md)) reaches the L4 surface through it.

It is **genuine NEW spine vocabulary, NOT a `gram_reduce` specialization** — c074 D6
probed and REFUSED the S-parameter-as-3rd-Gram-witness subsume
([`gram_reduce.md`](./gram_reduce.md):178-189; OQ
`gram-reduce-third-witness-probe-eigenmode-driven-postprocess`, CLOSED-NEGATIVE). The two
reductions share the `Matrix[p,p]` result shape but have **different folds**: `gram_reduce`
is a symmetric **bilinear** pair-grid (`xⱼᵀ K xᵢ`, `symmetric_from_upper`, homogeneous
diagonal, real); `sparameter_reduce` is a per-column **linear projection** (`sᵢ·E`, no
mirror, inhomogeneous `−1` diagonal, directional scaling, complex). Same shape, different
fold — exactly the `dot`-vs-`linear_combination` same-operand-shape-different-fold guard
(`concepts/black-box-vs-accelerated-kernels.md` §2). It is the driven output-product
column's OWN reduction verb.

## Context

L4 is **vocabulary** (`L4/index.md:7-13`). `sparameter_reduce` names the per-column
linear-projection reduction the driven driver runs once per swept frequency on its per-ω
solution family. It consumes the family the [`frequency_sweep`](./frequency_sweep.md) map
produces (the driven composition root's solve-half output — one driven solve per swept ω,
each excited at one drive port), and maps it to the scattering matrix `S` for that ω:

- each entry projects the driven field onto a receiver port mode — `project sᵢ E = sᵢ·E`,
  the port-mode **linear functional** (lumped `(*s)·E`; wave `(E×H_inc⋆)·n`);
- the diagonal carries the additive incident-wave subtraction `−1` (the drive-port
  self-term, an **inhomogeneous** affine contribution at `i == j`);
- the port-kind impedance/de-embed scaling multiplies each entry (lumped: generalized-S
  `√(R_src/R_dst)`, guarded by `|R| > 0`; wave: per-endpoint de-embed
  `exp(ikₙᵢdᵢ)·exp(ikₙⱼdⱼ)`).

The combinator is defined **in L4 vocabulary** (high→low discipline): its semantics,
signature, and laws are stated in terms of the per-ω driven family it consumes and the
per-port projection + scalar self-term/scale maps it folds — NOT in terms of the L0 C++
port loops. It is a methodology-level combinator distilled from the `MeasureSParameter`
two-loop body + the two `GetSParameter` projection kernels; Palace's C++ writes the
explicit per-port loop (project-then-postscale, two phases), not the L4 reduction form.

## Signature

    -- the driven per-ω per-port S-parameter reduction: project each per-ω solution onto
    -- each receiver port mode, subtract the drive-port self-term, apply the port-kind
    -- impedance/de-embed scaling. One drive-COLUMN per solved family member.
    sparameter_reduce :: [PortMode]                 -- the receiver port modes [sᵢ] (lumped s; wave port_sr + i·port_si)
                      -> [(Int, Tensor[N])]         -- the driven family: (drive_port_idx j, Eⱼ) per solved column
                      -> Matrix[p, p]               -- the scattering matrix S (p = #ports), per column over the family
    sparameter_reduce ports family =
      matrix_from_columns
        [ [ scale ports i j * (project (ports!!i) e - selfterm i j)  -- entry Sᵢⱼ for receiver i, drive column j
            | i <- [0 .. p-1] ]
          | (j, e) <- family ]
      where
        p              = length ports
        project s e    = port_dot s e                  -- the linear functional sᵢ·E (lumped (*s)·E / wave (E×H⋆)·n)
        selfterm i j   = if i == j then 1 else 0       -- the inhomogeneous diagonal −1 self-term (drive-port subtract)
        scale ports i j = port_scale (ports!!i) (ports!!j)  -- lumped: √(R_src/R_dst) (|R|>0); wave: exp(ikₙᵢdᵢ)·exp(ikₙⱼdⱼ)

Shape contract (bunsen-style; named axes):

- `ports : [PortMode]` — read-only; the per-port mode functionals (lumped `s`; wave
  `port_sr + i·port_si`) + the per-port impedance/de-embed parameters (`R`, `kn0`,
  `d_offset`) absorbed into the `scale` closure. `p = length ports`. **Precondition:** the
  ports are whole-model one kind — all-lumped XOR all-wave (Palace forbids mixing for
  S-parameters, `postoperator.cpp:1256-1259`), so `port-kind` is a model-level axis, not a
  per-entry branch.
- `family : [(Int, Tensor[N])]` — the driven solution family ([`frequency_sweep`](./frequency_sweep.md)'s
  per-ω output): per solved column, the drive-port index `j` + the per-ω complex field `E`.
  Read-only. The whole reduction is applied **once per swept frequency**; the ω index rides
  as the outer family axis (factored out — the driven composition root owns the ω map, so
  `sparameter_reduce` is the per-port reduction at a single ω; see §Lowers to caveat).
  **Precondition:** single-excitation-per-port — the S-matrix is only measured when
  `GetPortExcitations().IsMultipleSimple()` (`postoperator.cpp:1256`), i.e. one drive port
  per excitation column.
- result `Matrix[p, p]` — the (complex) scattering matrix `S` for that ω; `Sᵢⱼ` is the
  receiver-`i`, drive-column-`j` entry.

The shape contract makes structural what is conventional in the C++ two-phase port loop:

1. **Each entry is independent (the column-grid map is a list homomorphism over
   columns × receivers).** No state threads between entries; the reduction collects. The
   C++ projection cache (`vi.S = data.GetSParameter(*E)`, `postoperator.cpp:1141` lumped /
   `:1239` wave) is phase 1; the self-term + scale in `MeasureSParameter` is phase 2.
2. **There is NO `symmetric_from_upper`.** Every entry is computed independently (one
   drive-column per solve, all receiver rows per column). `S`'s near-symmetry `Sᵢⱼ ≈ Sⱼᵢ`
   is reciprocity *physics*, not a construction the reduction imposes.

## Semantics

`sparameter_reduce ports family` evaluates, for each solved drive-column `(j, Eⱼ)` and each
receiver port `i`, the port-mode linear projection `sᵢ·Eⱼ`, subtracts the drive-port
self-term (`−1` when `i == j`), and scales by the port-kind impedance/de-embed factor. It
is a `map`-then-collect over the column × receiver grid with no `Solve` effect — a pure
function `([PortMode], family) -> Matrix[p, p]`.

The combinator's structural payoff: the driven driver's per-port S-parameter assembly —
scattered across the two structurally-identical port loops of `MeasureSParameter`
(lumped + wave) and the cached `GetSParameter` projections — is ONE reduction over the
per-ω family. The two port kinds are **assembly variants of the same driven postprocess**
(a variant axis, NOT a 2nd pipeline): they differ only in the projection kernel (`(*s)·E`
vs `(E×H⋆)·n`) and the scale (`√(R_src/R_dst)` vs `exp(ikₙd)`), both absorbed into the
`PortMode` + `scale` closure.

This is the **reduce-to-matrix** rank, shared with the bilinear
[`gram_reduce`](./gram_reduce.md): both produce a `Matrix[p,p]` over a port/family index.
But the FOLD differs — `sparameter_reduce` is a per-column **linear projection** `sᵢ·E`
(linear in the field `E`), where `gram_reduce` is a per-pair **bilinear** `xⱼᵀ K xᵢ`
(bilinear in the family pair). This is the load-bearing structural difference and the
do-NOT-merge guard (c074 D6 closed-negative).

## Algebraic laws

Every law is a **syntactic identity on the fold structure**, read off the single positive
`MeasureSParameter` body (`postoperator.cpp:1246-1309`) with its two port-kind loops + the
two `GetSParameter` projection kernels.

1. **Linearity in the field (per column)** (load-bearing — the distinction from
   `gram_reduce`). Each raw entry `project sᵢ E = sᵢ·E` is **linear** in `E` (`sᵢ·E` is a
   linear functional; `lumpedportoperator.cpp:285-293`, `waveportoperator.cpp:782-792`) —
   contrast `gram_reduce`'s entries, which are **bilinear** in the family pair `(xᵢ, xⱼ)`.
   S is a per-column linear projection; the Gram is a pair-grid bilinear.
2. **No symmetry-by-construction** (the do-NOT-merge-with-`gram_reduce` structural identity).
   There is no `symmetric_from_upper`. `S`'s near-symmetry `Sᵢⱼ ≈ Sⱼᵢ` is **reciprocity
   physics** (a property of the assembled `S` for reciprocal media), NOT a construction the
   reduction imposes — every entry is computed independently (one column per solve, all
   receiver rows per column). The over-unification guard vs `gram_reduce`: do NOT add a
   symmetric mirror.
3. **Inhomogeneous diagonal (the `−1` self-term).** The diagonal carries an additive `−1`
   (`Sᵢᵢ = scale·(sᵢ·Eᵢ − 1)`) — the incident-wave subtraction
   (`vi.S.real(vi.S.real() - 1.0)` when `idx == drive_port_idx`, lumped `:1273-1276` /
   wave `:1295-1298`). This is an **inhomogeneous** (affine, not linear) contribution at
   the diagonal, with no analog in `gram_reduce` (whose diagonal is the homogeneous
   self-bilinear).
4. **Directional (asymmetric) scaling.** The lumped generalized-S scale
   `√(R_src/R_dst)` (`:1280`) is **directional** — it depends on the ordered
   `(drive, receiver)` pair and is NOT symmetric under swap (`√(R_j/R_i) ≠ √(R_i/R_j)`).
   The wave de-embed `exp(ikₙᵢdᵢ)·exp(ikₙⱼdⱼ)` (`:1301-1302`) IS symmetric in `(i,j)` but
   is a per-endpoint product (distinct from lumped). These are two values of the
   `port-kind` scaling variant axis.
5. **Grid-map independence.** Each entry depends only on
   `(ports!!i, ports!!j, family-column e)`; the column × receiver map carries no state —
   embarrassingly parallel over entries (the two C++ port loops carry no inter-entry
   accumulator).

Laws that explicitly **do not** hold:

- **Not a symmetric-Gram reduction.** No `symmetric_from_upper`, no family-PAIR `xⱼᵀ K xᵢ`
  bilinear — the linear-projection-vs-bilinear-Gram + no-mirror distinction from
  [`gram_reduce`](./gram_reduce.md) (c074 D6 closed-negative; OQ
  `gram-reduce-third-witness-probe-eigenmode-driven-postprocess`).
- **Identity / no-op specialization on the scale axis.** When all ports are non-resistive
  (`|R| = 0`, lumped) the generalized-S scale is **skipped** (`vi.S *= √(R_src/R_dst)`
  guarded by `std::abs(data.R) > 0.0`, `:1278-1281`); when `d_offset = 0` (wave default)
  the de-embed `exp(ik·0) = 1` is the identity (`:1301-1302`). So the un-scaled raw
  projection-minus-self-term is the scale-axis identity element (the `gram_reduce` `w ≡ 1`
  analog on the scaling axis).

## Dependencies

L4 rows this combinator consumes:

- [`frequency_sweep`](./frequency_sweep.md) (firm) — the driven solve-half map producing
  the per-ω solution family `[E_ω]` this reduction reduces over (the driven composition
  root's upstream stage, [`driven.L4`](../feature/driven.L4.md)).

The per-port projection kernel this folds — the port-mode **linear functional** `sᵢ·E`
(lumped `(*s)·E` `lumpedportoperator.cpp:283-294`; wave `(E×H⋆)·n`
`waveportoperator.cpp:780-793`) — does **not yet have a firm L1 home** (see OQ
`sparameter-reduce-l1-port-projection-home`); the reduction folds it directly off the two
`GetSParameter` bodies, which is one of the two reasons the entry is `rough-in` rather than
firm.

Sibling data-algebra reduction combinators (the L4 algebra-of-folds family):

- [`gram_reduce`](./gram_reduce.md) (reduce-to-matrix, **bilinear**) — the same
  `Matrix[p,p]` result shape, DIFFERENT fold: `sparameter_reduce` is the per-column
  **linear-projection** sibling (no mirror, inhomogeneous `−1` diagonal, directional
  scaling, complex). The c074 D6 closed-negative non-subsume — author as its OWN verb,
  cross-link as data-algebra reduce-to-matrix siblings.
- [`inner_product`](./inner_product.md) (reduce-to-scalar) — `sparameter_reduce`'s
  per-entry projection `sᵢ·E` is a single-pair **linear** functional (one covector dotted
  with the field), the linear-form sibling of `inner_product`'s symmetric pairing.
- [`linear_combination`](./linear_combination.md) (reduce-to-tensor) — the tensor-producing
  fold sibling in the algebra-of-folds family.

## Lowers to

`sparameter_reduce` lowers by **identity-in-form on the body** to the per-port port-mode
linear functional `sᵢ·E` it folds (lumped `(*s)·E`; wave `(E×H⋆)·n`) plus a per-entry
scalar self-term/scale map. The reduction is a plain column × receiver `map` of port
projections + scalar adjustments — there is no intervening L3/L2 absorption that reshapes
the fold. No dedicated L4>L3 theme file — the in-line-marker route (the
[`gram_reduce`](./gram_reduce.md) / [`inner_product`](./inner_product.md) /
[`linear_combination`](./linear_combination.md) pattern); the substantive downward content
is the C++ two-phase project-then-postscale assembly (the cached projection
`postoperator.cpp:1141,1239`, then the self-term + scaling in `MeasureSParameter`
`:1246-1309`) + the port projection kernels' own L1>L0 rotations (the `GetSParameter`
bodies). This entry records the rotation direction in-line per high→low discipline; it does
not author a theme.

**Per-ω axis caveat.** The swept-frequency ω axis is factored OUT of `sparameter_reduce`:
the reduction is applied once per ω (matching how `MeasureSParameter` runs once per measured
frequency), and the ω index rides as the outer family axis owned by the driven composition
root / [`frequency_sweep`](./frequency_sweep.md). This keeps `sparameter_reduce` the
per-port reduction at a single ω and lets the sweep own the ω map — the clean separation.

## Status

`rough-in`. **Reasoning (warrant-first):** the combinator's **structure** is
firm-on-positive-structure — the per-column linear-projection skeleton (project `sᵢ·E`,
subtract the drive-port self-term `−1`, apply the port-kind scaling, no symmetric mirror)
is read directly off the single positive `MeasureSParameter` body
(`postoperator.cpp:1246-1309`) with its two structurally-identical port-kind loops, and
every algebraic claim (§Algebraic laws) is a syntactic read-off of that body + the two
`GetSParameter` kernels. So the *structure* would clear the firm-on-positive-structure
escape. BUT two factors gate it to `rough-in`:

1. The **reduction-level assembly** (the self-term + port-kind scaling stitched onto the
   projection in `MeasureSParameter`) is **integration-level / test-unconfirmed** — only
   the projection *kernel* `GetSParameter` is unit-tested
   (`test/unit/test-lumpedportintegration.cpp:367,720`,
   `test/unit/test-romoperator.cpp:603`); the reduction assembly is exercised only through
   the full driven `Solve(mesh)` driver, so the reduction-level laws are test-unconfirmed.
2. The **per-port projection L1 home is not yet firm** — the port-mode linear functional
   `sᵢ·E` does not yet have a firm L1 entry (see OQ `sparameter-reduce-l1-port-projection-home`),
   so the entry would inherit reduced maturity from its folded constituent (the
   `gram_reduce` pattern: rough-in because its `bilinear-form` / `matrix-weighted-norm`
   constituents are rough-in).

I chose plain `rough-in` over `rough-in (test-coverage-bounded)` deliberately (following
D1's warrant): the test-coverage-bounded qualifier names entries whose *structure* is fully
L0-anchored and only the *laws* are test-gated; here BOTH the constituent L1 projection home
is absent AND the reduction assembly is test-gated — closer to plain `rough-in`. (A future
pass that firms the L1 projection home may refine this to
`rough-in (test-coverage-bounded)`.) Promotion route: (a) a firm L1 port-mode-projection
entry the reduction folds, AND (b) a dedicated S-matrix-assembly test OR a
lowering-verifier pass raising the reduction-level law confidence to
`frequency_sweep`-equivalent.

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

## Evidence

All L0 citations self-verified on-disk this dispatch via the codemap
(`mcp__palace-codemap__read_range`) + a numbered `awk` dump of the `MeasureSParameter`
body + `tools/citecheck/citecheck.py --anchor` on the three primary anchors (the dispatch
scope warned that D1's pinpoints drifted; corrected to on-disk line numbers below).

- **The per-port reduction assembly (positive witness — the reduction itself):**
  `palace/models/postoperator.cpp:1246` (`void PostOperator<solver_t>::MeasureSParameter()
  const` def; body `:1247-1308`, closes `:1309`), `:1256-1259` (the single-excitation +
  lumped-XOR-wave precondition guards), `:1263` (`auto drive_port_idx =
  measurement_cache.ex_idx` — the column index), `:1267-1286` (the lumped port loop:
  self-term `:1273-1276`, generalized-S scale `:1278-1281`), `:1287-1307` (the wave port
  loop: self-term `:1295-1298`, de-embed scale `:1299-1302`).
- **The per-port-mode projection kernels (the fold element):**
  `palace/models/lumpedportoperator.cpp:283` (`LumpedPortData::GetSParameter` def, body
  `:285-293` — the `(*s)·E` linear functional, real `:285` + imag `:286-289` parts),
  `palace/models/waveportoperator.cpp:780` (`WavePortData::GetSParameter` def, body
  `:782-792` — the `(E×H_inc⋆)·n` projection, `:782-783` comment, complex port mode
  `port_sr + i·port_si` `:788-789`).
- **The two-phase project-then-postscale cache:** `palace/models/postoperator.cpp:1141`
  (lumped, `vi.S = data.GetSParameter(*E)`) + `:1239` (wave, `vi.S = data.GetSParameter(*E)`)
  — the projection `sᵢ·E` is computed per port during the per-port measure pass, consumed
  by `MeasureSParameter` (`:1246`) which applies the self-term + scaling.
- **Dedicated unit tests for the projection kernel (L0-equivalent; the status gate):**
  `test/unit/test-lumpedportintegration.cpp:367` + `:720`
  (`std::complex<double> s_param = port_1.GetSParameter(...)`),
  `test/unit/test-romoperator.cpp:603` (`auto S = port_data.GetSParameter(E)`). The
  *reduction* assembly (`MeasureSParameter`) has no dedicated unit test — integration-level
  under the full driven `Solve(mesh)`.
- **Feature-chapter forward-references (the converging demand that flagged the mine):**
  `book/src/feature/driven.L4.md:55` (composition-root stage 3 `sparameter_reduce es (ports
  cfg)`), `:97-99` (the not-authored-here forward-ref), `:157` (the down-link table
  forward-ref row).
- **The c074 D6 NON-MATCH probe that scoped S-params OUT of `gram_reduce`:**
  `book/src/L4/gram_reduce.md:178-189` (the closed-negative probe: S-params are "a
  per-column port-mode LINEAR PROJECTION ... NOT symmetric-Gram ... author their OWN
  reduction verb").
- **Firm vocabulary grounding / siblings:** `book/src/L4/gram_reduce.md` (the
  reduce-to-matrix bilinear sibling), `book/src/L4/inner_product.md` +
  `book/src/L4/linear_combination.md` (the reduce-to-scalar / reduce-to-tensor
  algebra-of-folds siblings), `book/src/L4/frequency_sweep.md` (the firm driven solve-half
  map producing the family this reduces),
  `book/src/concepts/black-box-vs-accelerated-kernels.md` §"The combinators rise regardless"
  (the L4-feature-surface-verb warrant + the same-shape-different-fold over-unification
  guard, §2).
- **Provenance:** D1 (combinator-miner, cycle-075) proposed `sparameter_reduce` from the
  driven feature-chapter forward-mine flags (`driven.L4.md:55,98,157`) and correctly
  deferred the full chapter to a harvester; this dispatch (D6) is that harvester
  formalization. WARRANT verdict: genuine L4 entry (the driven output-product reduction
  verb; the linear-projection reduce-to-matrix member of the L4 algebra-of-folds, a
  navigable L4 home — NOT a stranded mine, NOT a `gram_reduce` specialization,
  c074 D6 closed-negative).
