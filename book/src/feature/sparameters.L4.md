---
kind: feature-surface
feature: sparameters
level: L4
status: seed
composes:
  - book/src/feature/driven.L4.md (the producing driver column — supplies the per-ω solution family [Eᵢ])
  - book/src/L4/sparameter_reduce.md (firm as of cycle-083 — the port-projection reduction; projects each per-ω field onto the port modes → the scattering matrix S)
l0_ground_truth:
  - palace/models/postoperator.cpp:1246-1307 (PostOperator::MeasureSParameter — the S-matrix post-process)
  - palace/models/lumpedportoperator.cpp:283-294 (LumpedPortData::GetSParameter — lumped port-mode projection)
  - palace/models/waveportoperator.cpp:780-793 (WavePortData::GetSParameter — wave port-mode projection)
---

# sparameters — L4 composition-root

The **scattering matrix `S`** output product, presented at L4 as a single composition of L4 combinators. This chapter is a **composition root** of the *output-product* sub-kind (a **leaf feature column**): its stage-(2) constituent is a *vocabulary op* (the [`sparameter_reduce`](../L4/sparameter_reduce.md) *(firm, c083)* port-projection reduction), and its upstream stage is *another feature column* (the [`driven`](./driven.L4.md) driver, which produces the per-ω solution family the reduction consumes). It introduces no new combinator; it wires the already-decomposed L4 vocabulary into the user-facing product (config → scattering matrix `S`), and links DOWN to each composed piece.

The scattering matrix is the physical product the user runs the **driven** (frequency-domain) solver to obtain: the per-frequency `n_port × n_port` complex scattering matrix `S(ω)` — `Sᵢⱼ(ω)` the response measured at port `i` for an excitation driven at port `j`, swept over the frequency family. The **driven driver column** ([`driven.L4`](./driven.L4.md)) produces the per-ω solution family `[Eᵢ]` (one field per swept frequency); this output-product column reduces that family to `S` via the **port-projection** reduction — projecting each per-ω field onto the configured port modes and assembling the scattering entries.

## The composition

At L4 the scattering-matrix product is the composition (Haskell-style; the strawman `book/src/design/l4_calculus.md` notation):

    -- inputs = config (ports + frequency sweep); output = the scattering matrix (the physical product)
    sparameters :: DrivenConfig -> ScatteringMatrix
    sparameters cfg =
      let es = driven_family cfg            -- (1) the driven driver column: assemble {K,C,M} once,
                                            --     operator-VARYING per-ω solve map → solution family [Eᵢ]
                                            --     ── feature/driven.L4 (the producing driver column)
          s  = sparameter_reduce es (ports cfg) -- (2) per-ω port-mode projection → scattering matrix
                                            --     ── L4/sparameter_reduce
      in  s                                 --     Sᵢⱼ(ω) = ⟨port_mode_i, Eⱼ(ω)⟩  (+ self-reflection − 1, de-embed/normalize)

Two composed stages, the first a down-link to the producing driver column, the second a down-link to the L4 port-projection reduction combinator:

1. **The producing driver column** — [`driven.L4`](./driven.L4.md). The driven driver is the operator-VARYING frequency sweep that assembles the fixed operator basis `{K, C, M}` once, then rebuilds the system operator `A(ω) = K + iωC − ω²M + A2(ω)` inside the per-ω map ([`frequency_sweep`](../L4/frequency_sweep.md), `SetOperators` inside the loop) and runs one [`ksp_solve`](../L4/ksp_solve.md) at each swept frequency, collecting the per-ω solution family `[Eᵢ]`. The S-parameter output product does NOT re-derive that solve; it consumes the driver column's solution family and projects it. This is the output-product / driver split the FEATURE-SURFACE SPINE encodes: one driver column (driven), with the S-parameter reduction one of the output products hanging off its solution family. L0: the per-ω solve loop in `drivensolver.cpp:168-196`.

2. **The port-projection reduction** — [`sparameter_reduce`](../L4/sparameter_reduce.md) (**firm, c083**). The L4 port-projection reduction `sparameter_reduce es ports` projects each per-ω solution field onto the configured port modes (the per-port mode inner product) and assembles the scattering entries, with the driving-port self-reflection (`S_jj ← S_jj − 1`) and the per-port-kind closing (generalized-S impedance normalization for lumped ports; phase de-embedding for wave ports). It is **NOT** [`gram_reduce`](../L4/gram_reduce.md) (the c074 capacitance/inductance symmetric-Gram energy reduction): `gram_reduce` folds a family against ITSELF through an operator `K` to a symmetric real matrix (`Xⱼᵀ K Xᵢ`); `sparameter_reduce` projects a family against a FIXED set of port-mode covectors `[sₖ]` to a generally-complex, non-symmetric scattering matrix (`⟨sᵢ, Eⱼ⟩`) with port-kind-specific post-processing. It is the **port-projection sibling** in the output-product reduction family, not the energy-Gram sibling. L0: `MeasureSParameter` (`postoperator.cpp:1246`, body `:1246-1307`) post-processing the per-port projections cached at `:1141` (lumped) / `:1239` (wave); the projection verb itself is `LumpedPortData::GetSParameter` (`lumpedportoperator.cpp:283-294`, the `(*s)·E` port-mode inner product) and `WavePortData::GetSParameter` (`waveportoperator.cpp:780-793`, the `(E × H_inc⋆)·n` surface integral).

## Inputs / outputs (the feature surface)

- **Input — config (ports + frequency sweep).** `DrivenConfig`: the **port set** (the lumped-port and/or wave-port boundary definitions → the port-mode covectors `[sₖ]` and the family-index domain `i`/`j`), the **swept frequency family** (the `omega_sample` list → the ω the scattering matrix is indexed over), inherited from the producing driven driver column. All `readonly` construction-stratum inputs. L0 home: `fem_op->GetLumpedPortOp()` / `fem_op->GetWavePortOp()` (`postoperator.cpp:1267`, `:1287`) — the port-operator surfaces driving the projection; the driving-port index `measurement_cache.ex_idx` (`:1263`).
- **Output — the physical product.** `ScatteringMatrix` — the per-ω complex `n_port × n_port` scattering matrix `S(ω)`. This is what the driven simulation is run to compute. L0 home: the per-port `vi.S` entries (`postoperator.cpp:1141` lumped / `:1239` wave projection, post-processed `:1246-1307`).

## Why this is an output-product column (and not gram-shaped)

The S-parameter product is the **port-projection** output-product composition root — the second shape in the output-product cohort, distinct from the c074 energy-Gram shape:

- The upstream family is supplied whole by the [`driven.L4`](./driven.L4.md) driver column — no re-derivation, just consumption of `[Eᵢ]`.
- The reduction is [`sparameter_reduce`](../L4/sparameter_reduce.md) *(firm, c083)*, a **projection against fixed port-mode covectors**, NOT a self-Gram fold. The scattering matrix is complex and generally non-symmetric (the driving-port self-reflection `−1` and the wave-port de-embedding break the symmetry the Gram reductions have); this is the structural reason it is a *sibling* reduction verb, not a `gram_reduce` weight specialization. (Capacitance/inductance are the two `gram_reduce` weight specializations; S-parameters are the first member of the projection-shaped output-product family.)
- The per-port-kind closing (lumped generalized-S normalization vs wave-port phase de-embedding) is the load-bearing port-kind axis of [`sparameter_reduce`](../L4/sparameter_reduce.md) *(firm, c083)*, absorbed into the reduction (it does not surface as a new feature-level combinator).

The whole output product therefore lowers cleanly outward to the L4 backend surface: `sparameters = sparameter_reduce (ports) ∘ driven_family` — a one-reduction tail on the driven driver column. The column is `seed`. NOTE (cycle-083): [`sparameter_reduce`](../L4/sparameter_reduce.md) was **promoted to `firm`** (the lowering-verifier firm-on-positive-structure escape) — so its constituent is now firm, but the column promotion-rule (a feature column may promote past `seed` only once ALL its composed constituents are firm) and the `seed` status are **held pending the batch-26 meta-phase** (a user directive to revise the column-promotion rule is pending; out of scope for the c083 dispatch). The earlier rough-in rationale is superseded by the firm promotion; the column-status reconciliation is the batch-26 item.

## Constituent down-links

| Stage | L4 constituent | Status | L0 site |
|---|---|---|---|
| producing driver column | [`driven.L4`](./driven.L4.md) (driver feature column) | seed | `drivensolver.cpp:37-229` |
| port-projection reduction | [`sparameter_reduce`](../L4/sparameter_reduce.md) | firm (c083) | `postoperator.cpp:1246-1307` |
| lumped port-mode projection | `lumpedportoperator.cpp:283-294` (`GetSParameter`) | (L0 site) | `postoperator.cpp:1141` |
| wave port-mode projection | `waveportoperator.cpp:780-793` (`GetSParameter`) | (L0 site) | `postoperator.cpp:1239` |

## Status

`seed` — an output-product **leaf feature column** authored under the FEATURE-SURFACE SPINE directive (2026-06-02). The composition is sound: stage (1) consumes the [`driven.L4`](./driven.L4.md) driver column's per-ω solution family; stage (2) composes the [`sparameter_reduce`](../L4/sparameter_reduce.md) *(firm, c083)* port-projection reduction (the port-projection sibling of the c074 energy-Gram reductions, NOT a `gram_reduce` weight specialization). The column stays `seed` pending the batch-26 meta-phase: `sparameter_reduce` is now `firm` (c083 lowering-verifier promotion), so its constituent is firm — but a user directive to revise the column-promotion rule (a feature column may promote past `seed` only once ALL its composed constituents are firm) is pending the batch-26 meta-phase, so the column-status reconciliation is held out of scope for c083. This chapter carries the *compositional* claim (S-parameters = the port-projection reduction over the driven driver's per-ω solution family), not the constituents' per-op algebraic claims (those live in `sparameter_reduce` and the L0 projection sites). Evidence: the L0 reduction range `postoperator.cpp:1246-1307` (`MeasureSParameter`) + the port-projection verbs (`lumpedportoperator.cpp:283-294`, `waveportoperator.cpp:780-793`), all self-verified on-disk via palace-codemap this dispatch, plus the constituent down-links.
