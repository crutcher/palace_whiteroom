---
verifies: ../REPORT.md
critiqued_at: 2026-06-03T053000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
overall_status: ready
---

# META: verification of "Formalize sparameter_reduce at L4" (D6, cycle-075)

## Critique

### Checks run

**citation-validity — pass.** `citecheck.py --scan` returns 22 ok / 0 failing (bounds + path
hygiene clean). I then hand-Read the load-bearing corrected anchors with brace-boundary
discipline (the class citecheck-anchor can miss at function boundaries), and every one of
D1's drifted pinpoints that D6 corrected verifies EXACTLY on disk:
- `:1263` = `auto drive_port_idx = measurement_cache.ex_idx;` (D1 had `:1261`; D6 correct).
- `:1309` = the function's closing brace (D1 had `:1308`, which is the inner `}` of the
  `if constexpr`; the function `}` is genuinely on `:1309` — D6's correction is right, and
  this is exactly the brace-boundary off-by-one the dispatch warned about).
- `:1273-1276` = lumped self-term `if (idx == drive_port_idx) { vi.S.real(vi.S.real() - 1.0); }` ✓
- `:1278-1281` = generalized-S scale guarded by `std::abs(data.R) > 0.0`; `:1280` =
  `vi.S *= std::sqrt(src_data.R / data.R);` ✓
- `:1295-1298` = wave self-term ✓; `:1299-1302` = de-embed, `:1301-1302` = the two
  `exp(1i*kn0*d_offset)` multiplies ✓.
- Projection kernels: `lumpedportoperator.cpp:283` def, `(*s)·E` linear functional in body
  `:285-293` ✓; `waveportoperator.cpp:780` def, `(E×H_inc⋆)·n` comment `:782-783`, complex
  `port_sr`/`port_si` mode ✓.
- Two-phase cache: `postoperator.cpp:1141` (lumped `vi.S = data.GetSParameter(*E)`) and
  `:1239` (wave) both confirm.
- Test anchors: `test/unit/test-lumpedportintegration.cpp:367,720` and
  `test-romoperator.cpp:603` all confirm `GetSParameter(...)` call sites (files live at
  `reference/palace/test/unit/`, matching the `test/unit/...` relative-to-`reference/palace/`
  citation form citecheck validated).
- The c074-D6 non-subsume probe `gram_reduce.md:178-189` confirms the closed-negative
  S-parameter-not-symmetric-Gram finding word-for-word.
This report carries no `verified_against:` YAML block, so that sub-check is not applicable.
Minor non-blocking sub-line looseness noted under Issues (sub-anchor real/imag attribution),
but all are inside the cited ranges and do not affect any claim.

**surface-or-evidence — pass.** This is a `create:` of a new L4 chapter (new surface), not a
refinement of existing operator/theme text; the surface-modification arm applies and is
satisfied (a full new chapter body with signature, semantics, laws). Every algebraic claim
is grounded in the single positive `MeasureSParameter` body + the two `GetSParameter`
kernels, all re-verified above. Not a pure rotation-claim-without-surface.

**rotation-quality — pass.** The L4 form is strictly more compact/abstract than the L0
two-phase port-loop assembly: the two structurally-identical C++ port loops
(project-then-postscale, lumped + wave) collapse into ONE `matrix_from_columns` reduction
with the port-kind difference absorbed into a `PortMode` + `scale` closure. This is genuine
state-hiding / loop-to-fold compression (the inter-entry accumulator is shown to be absent;
the per-kind branch is hoisted to a model-level axis), not a 1:1 rename.

**variant-axis-coverage — pass.** Three axes are declared and each disposed: port-kind
(lumped XOR wave — the load-bearing axis, absorbed into the closure, with the
whole-model-not-per-entry precondition cited at `:1256-1259`); scaling-presence
(generalized-S via `|R| > 0` guard `:1278-1281`, de-embed via `d_offset ≠ 0` `:1301-1302`,
absent = scale-axis identity); element-type (complex, pinned). No hidden branch: the
`if (std::abs(data.R) > 0.0)` and the `d_offset` default-0 cases are both surfaced as the
scale-axis identity element (law 5 / the "do not hold" note). Coverage is complete and the
identity-element framing is correct.

**cross-reference-integrity — pass.** All sibling links resolve on disk: `gram_reduce.md`,
`inner_product.md`, `linear_combination.md`, `frequency_sweep.md`,
`concepts/black-box-vs-accelerated-kernels.md`, `feature/driven.L4.md`, `design/l4_calculus.md`
all present. Build-readiness fence guard: the `create:` block has exactly even fence parity
(opener `:46`, closer `:381`, no nested ` ``` ` fences — the Signature uses 4-space indented
code, the truncation-safe form), and the full firm-shaped body (`## Status` + Signature +
Algebraic-laws + Evidence) sits INSIDE the fence. No fence-truncation defect. The coordination
note correctly flags the D1-row/D6-chapter ordering dependency (live link would be a
`linkcheck2` hard error if the row lands first) — proper integrator guidance, not a defect.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is carried (this is an L4 operator
entry, not a lowering theme); the §"Lowers to" is correctly the in-line-marker route, not a
mislabeled theme. The over-unification guard (sibling-of-`gram_reduce`, NOT a specialization)
is the load-bearing fidelity point here and it is correctly stated and cited: the
`gram_reduce.md:178-189` closed-negative probe is quoted faithfully, and the
same-shape-different-fold distinction (linear projection vs bilinear Gram, inhomogeneous `−1`
diagonal, no `symmetric_from_upper`, directional scaling) is the exact c074-D6 finding.

**plan-kind-consistency — pass.** Declared `rough-in` matches content shape. The warrant is
sound and well-reasoned: structure is firm-on-positive-structure (would clear the escape) but
TWO genuine gates hold it at `rough-in` — (1) the reduction-level assembly is test-unconfirmed
(only the `GetSParameter` KERNEL is unit-tested, confirmed at the three test anchors; the
`MeasureSParameter` reduction has no dedicated test), and (2) the per-port projection has no
firm L1 home (OQ `sparameter-reduce-l1-port-projection-home`). The deliberate choice of plain
`rough-in` over `rough-in (test-coverage-bounded)` is correctly justified (the L1 home is
absent, not just laws test-gated). No firm-claim-with-placeholders mismatch.

**skill-uptake-survey — warning (non-blocking, telemetry only).** D6's shape implies two
relevant skills the report does NOT name by invocation: `verify-citation-range` /
`tools/citecheck` `--anchor` (the report DOES describe running `citecheck --anchor` on the
three primary anchors — partial uptake, good) and, for the coordination note,
`upgrade-plain-text-ref-to-live-link-when-target-on-disk` (the report correctly NAMES this
skill as a follow-up for the integrator/repairer on `driven.L4.md:55,98,157` — good). The
build-readiness fence guard `proposed-changes-fence-encloses-full-body-guard` is not
referenced but is a critic-side skill, so its absence on a producer report is expected. This
is a pure presence-survey surfacing; nothing blocks.

### Issues found

1. **(trivial, citation sub-line looseness) — `book/src/L4/sparameter_reduce.md` §Evidence,
   projection-kernel bullet.** D6 attributes the lumped real part to `:285` and imag to
   `:286-289`; on disk the `dot` real-part init is `:287` and the imag branch is `:288-291`
   (the `:285` line is the explanatory comment). Similarly the wave complex mode `port_sr +
   i·port_si` is used at `:789-790`, cited as `:788-789`. Both are INSIDE the cited enclosing
   ranges (`:285-293` / `:782-792`) and back the same `(*s)·E` / `(E×H⋆)·n` claims, so no
   claim is affected — flagged only for completeness. Severity: trivial.

2. **(observation, not a defect) — house-style parallelism.** `gram_reduce.md` carries a
   dedicated `## Specialization` section; D6 folds the do-NOT-merge / over-unification guard
   into its opening paragraphs + §Semantics + §Algebraic laws (laws 1–4 + the "do not hold"
   note) rather than a same-named section. The guard content is present, prominent, and
   correctly cited, so this is an acceptable structural variation in the reduce-family house
   style, not a fidelity break. Noting it so the repairer/integrator does not mistake the
   missing section header for an omission. Severity: none (informational).

3. **(skill-uptake telemetry, non-blocking) — see skill-uptake-survey check.** No explicit
   in-report invocation marker for `verify-citation-range` (the `citecheck --anchor` use is
   described prose-style, not as a named skill invocation). Surfaces telemetry only.
