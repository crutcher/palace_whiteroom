---
kind: feature-surface
feature: sparameters
level: L0
status: seed
l0_ground_truth:
  - palace/models/postoperator.cpp:1246-1307 (PostOperator::MeasureSParameter — the S-matrix post-process)
  - palace/models/postoperator.cpp:1141 (the lumped per-port S projection: vi.S = data.GetSParameter(*E), in MeasureLumpedPorts)
  - palace/models/postoperator.cpp:1239 (the wave per-port S projection: vi.S = data.GetSParameter(*E), in MeasureWavePorts)
  - palace/models/lumpedportoperator.cpp:283-294 (LumpedPortData::GetSParameter — lumped port-mode projection)
  - palace/models/waveportoperator.cpp:780-793 (WavePortData::GetSParameter — wave port-mode projection)
lifts_to:
  - book/src/feature/sparameters.L1.md (the L1 pure-function composition root)
---

# sparameters — L0 ground-truth surface

The **scattering matrix `S`** output product at L0: the cited Palace source that realizes the port-projection reduction composition root, with the per-stage source ranges that the L1 / L4 S-parameter feature chapters lift. This is the ground-truth surface — every claim is a `(file:start-end)` citation into the Palace `models/` sources.

The S-parameter reduction is split across two source phases. **Per-port projection** runs inside the per-frequency measurement (`MeasureLumpedPorts` / `MeasureWavePorts`), caching each port's raw projection `vi.S`. **S-matrix post-processing** is `PostOperator<solver_t>::MeasureSParameter()` (`palace/models/postoperator.cpp:1246`, body `:1246-1307`, def closing brace `:1309`), which applies the driving-port self-reflection and the per-port-kind closing. The reduction is the **output-product** tail of the driven driver: the driver's frequency sweep (`drivensolver.cpp:168-196`) collects the per-ω solution family `[Eᵢ]`; the projection + post-process reduce that family to the scattering matrix `S`.

## The composition, in source

The scattering matrix is a port-mode projection of each per-ω field, with the driving-port self-reflection and port-kind closing. The source stages, in order:

1. **Per-port projection (cached).** During the per-frequency measurement, each port's raw scattering entry is computed `vi.S = data.GetSParameter(*E)` — lumped at `postoperator.cpp:1141` (inside `MeasureLumpedPorts`), wave at `:1239` (inside `MeasureWavePorts`). This is the boundary between the producing driven driver column and the output-product reduction: the per-ω field `E` (the driver's solution-family member) is projected onto the port mode.

2. **The port-mode projection verb (lumped).** `LumpedPortData::GetSParameter(GridFunction &E)` (`lumpedportoperator.cpp:283`, body `:283-294`) computes the port S-parameter as the projection of the field onto the port mode: `std::complex<double> dot((*s) * E.Real(), 0.0)` (`:287`), with the imaginary part `dot.imag((*s) * E.Imag())` when `E.HasImag()` (`:290`), reduced by `Mpi::GlobalSum(1, &dot, ...)` (`:292`). `s` is the port-mode covector; the product `(*s) * E` is the port-mode inner product. This is the L0 site the L1 [`bilinear-form`](../L1/bilinear-form.md) projection (and the L4 [`sparameter_reduce`](../L4/sparameter_reduce.md) *(rough-in)* lumped projection) lift.

3. **The port-mode projection verb (wave).** `WavePortData::GetSParameter(GridFunction &E)` (`waveportoperator.cpp:780`, body `:780-793`) computes the wave-port projection as the surface integral `(E × H_inc⋆)·n = E·(−n × H_inc⋆)` (`:782-783`): the field is transferred to the port FE space (`port_nd_transfer->Transfer(...)`, `:787-788`) then projected against the real/imag port covectors `(*port_sr)`/`(*port_si)` into a complex `dot` (`:789-790`), reduced by `Mpi::GlobalSum` (`:791`). This is the L0 site the wave-port projection lifts; it is the wave variant of the same projection shape (a fixed port covector dotted with the driven field).

4. **Driving-port self-reflection.** In `MeasureSParameter` (`:1246`), the driving-port index `drive_port_idx = measurement_cache.ex_idx` (`:1263`); for the driven diagonal `if (idx == drive_port_idx) vi.S.real(vi.S.real() − 1.0)` (lumped `:1273-1276`, wave `:1295-1298`) subtracts the incident wave from the reflected wave (the scattering convention `S = reflected/incident − 1` at the driving port). This is the L0 site the L4 self-reflection step lifts.

5. **Port-kind closing → the physical product.** The per-port-kind normalization closes the entry:
   - **Lumped (generalized-S).** When resistive, `if (std::abs(data.R) > 0.0) vi.S *= std::sqrt(src_data.R / data.R)` (`:1278-1281`) renormalizes to the source-port reference impedance (generalized S-parameters, avoiding divide-by-zero).
   - **Wave (de-embedding).** `vi.S *= std::exp(1i * src_data.kn0 * src_data.d_offset)` and `vi.S *= std::exp(1i * data.kn0 * data.d_offset)` (`:1299-1302`) apply the phase de-embedding `S_demb = S · exp(ikₙᵢdᵢ) · exp(ikₙⱼdⱼ)` for the source and measured ports.
   The guard `if (!IsMultipleSimple() || !(lumped xor wave)) return;` (`:1256-1260`) restricts the S-matrix to single-excitation-per-port, non-mixed-port models. These are the L0 sites the L4 port-kind closing axis of [`sparameter_reduce`](../L4/sparameter_reduce.md) *(rough-in)* lifts.

## Inputs / outputs (the feature surface, in source)

- **Input — config (ports + frequency sweep).** The port operators `fem_op->GetLumpedPortOp()` (`:1267`) / `fem_op->GetWavePortOp()` (`:1287`) — the port-mode covectors `s` / `port_sr`/`port_si` and the port index domain; the driving-port index `measurement_cache.ex_idx` (`:1263`); the swept-frequency family supplied by the producing driven driver column (the per-ω field `E` measured per frequency).
- **Output — the physical product.** The per-port scattering entries `vi.S` (the `measurement_cache.lumped_port_vi` / `wave_port_vi` map values, projected `:1141`/`:1239`, closed `:1246-1307`) — assembled across ports + frequencies into the scattering matrix `S`.

## Lifts to

This L0 surface lifts to the L1 pure-function composition root [`sparameters.L1`](./sparameters.L1.md) (each in-place `GlobalSum` accumulation + `vi.S *=` post-process write → a value-returning projection pure function) and the L4 combinator composition root [`sparameters.L4`](./sparameters.L4.md) (the per-port projection + self-reflection + port-kind closing → the [`sparameter_reduce`](../L4/sparameter_reduce.md) *(rough-in)* port-projection combinator). The per-operator L1>L0 mutation-rotation themes carry the per-write lifts; this feature surface records the output-product *site map* (which source range realizes which reduction stage).

## Status

`seed` — the L0 ground-truth surface for the scattering-matrix output product (the output-product **leaf feature column**), authored under the FEATURE-SURFACE SPINE directive (2026-06-02). Every stage is a cited range into the Palace `models/` sources, confirmed on-disk via palace-codemap `read_range` this dispatch (`postoperator.cpp:1246-1307` `MeasureSParameter` body + def `:1246-1309`; the per-port projection cache `:1141` lumped / `:1239` wave; the self-reflection `:1275`/`:1297`; the lumped generalized-S `:1278-1281`; the wave de-embed `:1299-1302`; the lumped projection verb `lumpedportoperator.cpp:283-294`; the wave projection verb `waveportoperator.cpp:780-793`). The chapter's evidence IS the source range + the per-stage site map to the constituent ops (the adapted surface-or-evidence form for the feature-surface kind).
