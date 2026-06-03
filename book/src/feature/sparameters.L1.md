---
kind: feature-surface
feature: sparameters
level: L1
status: firm
composes:
  - book/src/feature/driven.L1.md (the producing driver column — supplies the per-ω solution family [Eᵢ])
  - book/src/L1/port_projection.md (firm — the port-mode projection ⟨s, E⟩, the dual-pairing/linear-functional primitive the reduction folds; the FIRM L1 home as of cycle-077, replacing the earlier bilinear-form approximation)
l0_ground_truth:
  - palace/models/postoperator.cpp:1246-1307 (PostOperator::MeasureSParameter — the S-matrix post-process)
  - palace/models/lumpedportoperator.cpp:283-294 (LumpedPortData::GetSParameter — lumped port-mode projection)
  - palace/models/waveportoperator.cpp:780-793 (WavePortData::GetSParameter — wave port-mode projection)
---

# sparameters — L1 composition-root

The **scattering matrix `S`** output product, presented at L1 as a pure-function composition of L1 operators. This is the **pure-function feature surface** of the output-product sub-kind: the same composition root as the L4 chapter, but expressed in L1 vocabulary (explicit per-port inner-product projections, no L4 combinator naming) — the form a reader navigating L1 sees when asking "what whole product do these L1 projection evaluations add up to?"

At L1 the scattering-matrix product is a pure function `config → scattering matrix`: it consumes the per-ω solution family `[Eᵢ]` produced by the [`driven.L1`](./driven.L1.md) driver column, then for each swept frequency projects the driven field onto each configured port mode and assembles the scattering entries (the **mutation already lifted** — the L0 in-place `Mpi::GlobalSum(&dot)` accumulation and the `vi.S *= ...` post-process writes are lifted to value-returning forms per the L1>L0 mutation rotation).

## The composition

    -- inputs = config (ports + frequency sweep); output = the scattering matrix (the physical product)
    sparameters :: DrivenConfig -> ScatteringMatrix
    sparameters cfg =
      let es      = driven_family cfg                 -- (1) the driven driver column → per-ω solution family [Eᵢ]
          ports   = port_modes cfg                    -- the port-mode covectors [sₖ] (lumped: sₖ; wave: the (−n×H_inc⋆) covector)
          drive   = drive_port_idx cfg
          s i j   = let raw = port_projection (ports!!i) (e_at es j) -- projection ⟨sᵢ, Eⱼ⟩
                    in  port_close i j drive raw       -- self-reflection (i==drive ⇒ −1) + lumped generalized-S / wave de-embed
      in  matrix s                                     -- (2) per-(port,frequency) projection grid → scattering matrix S

1. **The producing driver column** — [`driven.L1`](./driven.L1.md). The driven driver assembles the fixed basis `{K, C, M}` once and maps the per-ω pure solve over the swept frequency family (the operator-VARYING rebuild + per-member [`ksp_solve`](../L1/ksp_solve.md)), collecting the per-ω solution family `[Eᵢ]`. The S-parameter output product consumes that family; it does not re-derive the solve. L0: the per-ω solve loop `drivensolver.cpp:168-196`.

2. **Scattering-matrix reduction** — the per-(port, frequency) grid `Sᵢⱼ = ⟨sᵢ, Eⱼ⟩`, built from L1 port-mode projections over the solution family, with the driving-port self-reflection and the per-port-kind closing:
   - the projection `⟨sₖ, E⟩` — the port-mode linear-functional projection, the firm [`port_projection`](../L1/port_projection.md) `α = ⟨s, E⟩` dual-pairing of the field against the fixed pre-assembled port-mode covector `sₖ` (L0 lumped: `(*s) * E.Real()` + imaginary part, `lumpedportoperator.cpp:287-290`; L0 wave: the `(E × H_inc⋆)·n` surface-integral form `waveportoperator.cpp:789-790`).
   - the **self-reflection** — the driving-port diagonal subtracts the incident wave: `S_{drive,drive} ← S_{drive,drive} − 1` (L0 `postoperator.cpp:1275` lumped / `:1297` wave).
   - the **port-kind closing** — lumped ports apply the generalized-S impedance normalization `S *= sqrt(R_src / R)` when resistive (L0 `:1278-1281`); wave ports apply phase de-embedding `S *= exp(i kₙ d)` for source + measured port (L0 `:1299-1302`).
   The result is the per-ω complex scattering matrix `S`. This stage is a pure fold of port-mode projections over the (port, frequency) grid — no L1 operator is *new* here; the reduction composes the firm [`port_projection`](../L1/port_projection.md) with the port-kind closing. At L4 this exact fold is named the [`sparameter_reduce`](../L4/sparameter_reduce.md) *(firm, c083)* combinator (the port-projection sibling of `gram_reduce`); L1 sees the unfolded projection grid.

## Inputs / outputs (the feature surface)

- **Input — config (ports + frequency sweep).** `DrivenConfig` (port set → port-mode covectors `[sₖ]` + family-index domain; swept frequency family → the ω the matrix is indexed over), inherited from the producing driver column. All read-only.
- **Output — the physical product.** `ScatteringMatrix` — the per-ω complex `n_port × n_port` scattering matrix `S`. L0: the per-port `vi.S` entries (`postoperator.cpp:1141` lumped / `:1239` wave).

## L1 vs L4

The L1 and L4 composition roots express the **same output product**; they differ in vocabulary:
- **L1** (this chapter): the reduction is an explicit per-(port, frequency) grid of port-mode linear-functional projections ([`port_projection`](../L1/port_projection.md)) plus the explicit self-reflection + port-kind closing arithmetic.
- **L4** ([`sparameters.L4`](./sparameters.L4.md)): the whole reduction is the [`sparameter_reduce`](../L4/sparameter_reduce.md) *(firm, c083)* combinator (the projection grid + self-reflection + port-kind closing made *structural*). The L4 form is the one the outward backend consumes; the L1 form is the pure-function decomposition the L4 combinator names.

The L1→L0 direction (how the projection pure functions lower to the in-place `GlobalSum` accumulation + `vi.S *=` post-process writes) is the per-operator L1>L0 mutation-rotation themes of the constituent ops; this composition root records only the L1 composition (high→low discipline).

## Constituent down-links

| Stage | L1 constituent | Status | L0 site |
|---|---|---|---|
| producing driver column (sibling reference, not a blocker) | [`driven.L1`](./driven.L1.md) (driver feature column) | seed | `drivensolver.cpp:37-229` |
| port-mode projection ⟨sₖ, E⟩ | [`port_projection`](../L1/port_projection.md) | firm | `lumpedportoperator.cpp:287-290`, `waveportoperator.cpp:789-790` |
| self-reflection + port-kind closing | (port-kind arithmetic; absorbed by [`sparameter_reduce`](../L4/sparameter_reduce.md) at L4) | rough-in | `postoperator.cpp:1275-1302` |

## Status

`firm` — the L1 pure-function composition root for the scattering-matrix output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02). It consumes the [`driven.L1`](./driven.L1.md) driver column's per-ω solution family, then folds the firm L1 port-mode projection ([`port_projection`](../L1/port_projection.md), firm as of cycle-077) over the (port, frequency) grid with the self-reflection + port-kind closing. The per-mode projection primitive is firm; as of cycle-083 the whole-grid reduction it composes — [`sparameter_reduce`](../L4/sparameter_reduce.md) at L4 — is **also `firm`** (the lowering-verifier firm-on-positive-structure promotion). **The column promotes off `seed` to `firm` under the OWN-COMPOSITION rule (USER DIRECTIVE 2026-06-03):** its sole directly-owned constituent — the reduction's L4 home [`sparameter_reduce`](../L4/sparameter_reduce.md) — is firm (c083). The batch-26 meta-phase the c083 prose deferred to has now fired and enacted the OWN-COMPOSITION rule; the cross-link to the [`driven.L1`](./driven.L1.md) driver column (its own `status: seed`) is a **SIBLING reference, NOT a blocker** — the reciprocal drift-guard, not a constituent-firmness dependency. The chapter carries the compositional claim only; per-op algebraic claims live in the linked chapters. Evidence: the L0 reduction range `postoperator.cpp:1246-1307` + the port-projection verbs (`lumpedportoperator.cpp:283-294`, `waveportoperator.cpp:780-793`), self-verified on-disk this dispatch, plus the constituent down-links.
