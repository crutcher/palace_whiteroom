---
verifies: ../CYCLE.md
critiqued_at: 2026-05-29T024800Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: warning
repaired_at: 2026-05-29T030000Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of "Combinator candidate — inner-product reduce-to-scalar fold family"

## Critique

### Checks run

**citation-validity — warning.** Independently re-read via `palace-codemap read_range`: `vector.cpp:263-274` (both kernels), `vector.cpp:664-685` (real + complex `LocalDot`), `operator.cpp:621-638` (both M-weighted overloads), `vector.hpp:108-120`, `vector.hpp:245-262`, the four smoother class declarations, and ran `search_text TransposeDot` over `palace/**` myself. The **`tdot`/`TransposeDot` zero-call-sites claim is CONFIRMED** — `search_text` returns exactly two hits, `vector.hpp:112` (decl) + `vector.cpp:269` (def), no callers. The three task-named ranges all resolve in-range and support their claims. The smoother class-line citations (`jacobi.hpp:19`, `chebyshev.hpp:23,86`, `distrelaxation.hpp:30`) all land on the exact `class … : public Solver<OperType>` lines. However, **one supporting-evidence claim is factually wrong about the source it cites** (Issue 1): line 78 asserts the `Dot`/`TransposeDot` kernels "differ ONLY in the sign of the imaginary cross-terms," but the read source shows the **real parts also differ** (`Dot` real = `Re·Re + Im·Im`; `TransposeDot` real = `Re·Re − Im·Im`). Because that imprecision is in a "Self-verified via `read_range`" bullet, it is a citation-fidelity miss, not a pointer miss. A second math claim about the weighted member conjugates the wrong operand (Issue 2). Down-grading to warning on these two.

**surface-or-evidence — pass.** This is a proposal report (no surface mutation, explicitly emits no `edit:book/...` block — correctly, per the dispatch-phase write-guard and because the `inner_product` row already stands). It is therefore retroactive/characterization evidence for an existing rough-in, which is allowed. The family-law (split-additivity / concatenation-homomorphism `(length-concat, ++) → (Scalar, +)`) is evidence-grounded: it is a faithful mirror of the firm `linear_combination` concatenation-homomorphism law (`book/src/L2/linear_combination.md:117-124`, "monoid homomorphism from `([(Scalar,Tensor[N])], ++, [])` to `(Tensor[N], +, zeros)`"). The three axes (conjugation / element-type / weight) are each tied to a verified source site (kernels `vector.cpp:263-274`; real-vs-complex fold `vector.cpp:664-685`; weight via `operator.cpp:621-638`).

**rotation-quality — pass.** The level decision (family lives at L2; leaves stay at L1; the unifying object is the L2 fold that lowers via a conjugation/weight-dispatch theme) is justified and mirrors the `linear_combination` precedent (L1 leaves → L2 fold → L2>L1 dispatch theme). This is genuine compaction (a single variadic fold subsuming distinct fixed kernels — `dot`, `tdot`, weighted), not a 1:1 rename. The fold-law is the abstraction evidence. Pass.

**variant-axis-coverage — pass.** The over-unification guard is present, explicit ("Over-unification guard (REQUIRED — stated explicitly)"), and correct on both boundaries: (i) do NOT merge with `linear_combination` (reduce-to-`Tensor[N]`) — the result-type / combining-step / fold-axis distinction is precise and matches the artifact boundary already drawn at `book/src/L2/index.md:25` ("Sibling fold (do NOT merge): `dot`") and `:26`; (ii) do NOT subsume `nrm2` / `matrix-weighted-norm` (`√ ∘ inner_product` consumers, not fold members) — matches the stub's "Consumer (NOT an instance)" note. The four parameter axes (conjugation / element-type / weight-presence / diagonal-degeneration) are enumerated with per-axis citations; no axis is left as a hidden branch. Pass.

**cross-reference-integrity — warning.** No live `[link]` to a missing file: the report deliberately emits no markdown links into `book/` and references the existing stubs (`book/src/L2/inner_product.md`, `book/src/L2-L1/inner-product-fold-specialization.md`) and the standing row (`L2/index.md:26`) — all of which I confirmed exist. No dep-map mutation (correctly leaves the cycle-018 rough-in row untouched). The warning is a **named-concept slug drift** (Issue 3): the report twice refers to "the constructed-operator-gate concept" (lines 68, 95), but no `concepts/constructed-operator-gate.md` exists — the actual page is `concepts/nested-constructed-operator-gate.md` (siblings `constructed-operators.md`, `constructed-operator-factory.md`). Plain prose, so no `linkcheck2` break, but the corroboration that the smoother cohort is "already partly captured" leans on a mis-named concept.

**edge-label-fidelity — pass (n/a).** Not applicable to a pure proposal report — it carries no `L_{n+1}→L_n` edge label whose prose must be checked. The directional framing it does use (L1 leaves fuse *up* to L2 fold; L2>L1 dispatch theme lowers down) is internally consistent and matches the high→low invariant.

**plan-kind-consistency — pass.** The proposal is well-formed and honestly classified. It does not over-claim novelty: it explicitly declares itself a **mode-validation** result (the row pre-exists from cycle-018) rather than a new-row proposal, and the content shape matches that declaration — characterization + fold-law + over-unification guard + a mode-gap finding, no spurious `edit:` block. Status `pending`. Consistent.

**skill-uptake-survey — warning.** The report's shape implies at least two applicable skills: `classify-variant-axis` (it enumerates four variant axes and states the over-unification guard — exactly that skill's output shape) and `verify-citation-range` (it repeatedly asserts "Self-verified via `read_range`" across ~6 ranges). Neither skill is referenced by name anywhere in the report (grep for skill names returns nothing). The work appears to have been done, but the telemetry is absent. Pure presence check — surfaces telemetry, non-blocking.

### Mode-validation soundness assessment (requested)

The `## Mode validation` reasoning is **sound and well-scoped**, and is safe to feed the next meta-phase's friction-ledger resolution of `combinator-miner-arity-blind-parametric-family-detection`:

- **Claim 1 (mode independently surfaces the cohort as one candidate)** holds. The trigger genuinely fires on dot/tdot/weighted-Dot (same operand shape `(Tensor[N], Tensor[N])`, same combining step `acc + kernel`, differing only along the three axes), and the unifying split-additivity homomorphism is stateable and grounded. The "arity-blind same-shape counting would see only 3 too-thin leaves (tdot = 0 sites)" argument is corroborated by my independent `search_text` confirming tdot has zero callers — so the mode genuinely catches what instance-counting misses.
- **Qualification A (candidate already existed → validated, not first-to-surface)** is honest and correct. The report does not fabricate a novel row; it correctly identifies the mode's distinctive deliverable as the *fold-law + axis taxonomy* (characterizer, not just surfacer). The pre-existing row is real (`L2/index.md:26`, proposed-by combinator-miner:2026-05-28T231046Z).
- **Qualification B (no positive channel for non-fold parametric families)** is the load-bearing finding and it is sound. The smoother cohort is verified real (four `: public Solver<OperType>` classes) and is genuinely parametric (element-type + relaxation-kernel) yet genuinely NOT a fold (operator-action `Tensor[N] → Tensor[N]`, no combining-step / concatenation-homomorphism). The logic — the mode's "if you cannot state a unifying fold/parametric law it is NOT a parametric family" guard *correctly excludes* it, but the spec gives *no positive channel* for "this IS a structured parametric family, just not a fold one" — is coherent and identifies a real spec gap. Correctly filed as non-blocking (no row lost; cohort partly captured) and routed to the meta-phase. The one soft spot: the "already partly captured" backstop cites the mis-slugged concept (Issue 3) — the backstop is real but the citation is imprecise.

### On the conjugation-contradiction self-correction (requested)

The combinator-miner's conjugation-contradiction framing in **Open questions** (line 101) is **NOT a citation error worth flagging as a defect** — it is correct. The report accurately reads Palace as `Dot(comm, x, y) = yᴴ x` (argument conjugated, receiver linear — which I re-derived from `ComplexVector::Dot`'s body: receiver·conj(arg)) and accurately reads `book/src/L1/dot.md:34,43` as a *deliberate L1 re-order* placing the conjugated argument first, explicitly labeling it "an intentional L1 mutation-rotation choice … not an error." That matches what `dot.md:43` says about itself verbatim ("the L1 signature names the conjugated argument first"). So the report correctly characterized this as Palace-vs-L1-entry convention divergence (an intentional rotation), not a Palace-internal contradiction — i.e., it already arrived at the corrected framing the wave-2 harvester confirmed. No penalty.

The *real* conjugation issue is a separate one the report introduces in its own math (Issue 2 below), which is ironic given the report flags conjugation-pinning as a hard must-resolve-before-firm.

### Issues found

1. **[low severity — citation fidelity] Kernel-difference claim is imprecise.** `CYCLE.md:78` ("Conjugation axis"): states the `Dot`/`TransposeDot` kernels "differ ONLY in the sign of the imaginary cross-terms." Source (`vector.cpp:263-274`, self-read) shows the **real parts also differ**: `Dot` real = `Re·Re + Im·Im`, `TransposeDot` real = `Re·Re − Im·Im`. The artifact's own `book/src/L1/dot.md:112-113` records this correctly. Fix: "differ in the sign on the `Im·Im` real-part term and on the imaginary cross-terms" (i.e. `Dot = a·conj(b)` per element vs `TransposeDot = a·b`).

2. **[medium severity — math fidelity, self-undermining] Weighted-member conjugates the wrong operand.** `CYCLE.md:12` ("`xᴴ M y`"), `:32-35` (signature sketch `inner_product_M(x, M, y) = (M·x)ᴴ y`), and the Open-question prose at `:101` ("`(Ax)ᴴ y`") conjugate the M-applied (first) operand. But the actual Palace overload `Dot(comm, x, A, y)` (`operator.cpp:621-628`) computes `Ax = A·x` then `Dot(comm, Ax, y)`, and `Dot` conjugates its **second** argument (`yᴴ x` convention) — so the body is `yᴴ (A x) = yᴴ A x`, NOT `(Ax)ᴴ y`. The standing stub `book/src/L2/inner_product.md:7` gets this right ("Palace documents `Dot(comm, x, A, y) = yᴴ A x`"); the report contradicts the stub it is supposed to be characterizing for the harvester. This is the exact convention the report itself flags as must-pin-before-firm, so getting it backwards in the proposal is self-undermining and should be corrected before the harvester inherits it.

3. **[low severity — named-concept slug drift] `constructed-operator-gate` does not exist.** `CYCLE.md:68` and `:95` reference "the constructed-operator-gate concept" as the existing partial-capture of the smoother cohort. No such concept page exists; the actual slug is `nested-constructed-operator-gate` (`book/src/concepts/nested-constructed-operator-gate.md`; siblings `constructed-operators.md`, `constructed-operator-factory.md`). Plain prose so no build break, but the mode-validation Qualification-B "no row is lost, already partly captured" backstop rests on this reference — fix the slug so the backstop is verifiable.

4. **[low severity — skill telemetry] No skill invocations referenced.** The report performs variant-axis enumeration (cf. `classify-variant-axis`) and repeated citation-range self-verification (cf. `verify-citation-range`) but names no skill. Non-blocking telemetry gap; flag for the skill-uptake survey.

5. **[informational — not a defect] `tdot` evidentiary-weight caveat is well-handled.** The zero-call-sites finding (confirmed independently) is surfaced as an Open question with two readings and a recommendation, and propagated to the variant-axis discussion. No fix needed; noting it as a correctly-handled weak-evidence axis value for the repairer/integrator's awareness (it bears on whether the harvester cites `tdot` as firm or rough-in).

---

## Repair

### Fixes attempted

- **Finding 1 (medium — wrong-operand conjugation).** The report wrote the M-weighted member as `xᴴ M y` / `(M·x)ᴴ y` (`CYCLE.md:12`, `:32-35`, `:101`), conjugating the M-applied first operand, contradicting both Palace's L0 form and the standing L2 stub.
  - **Decision**: repaired.
  - **Action**: Verified the source first via `palace-codemap read_range`: `operator.cpp:621-628` (`Dot(comm, x, A, y)` builds `Ax = A·x` then returns `Dot(comm, Ax, y)`), `vector.cpp:263-267` (`ComplexVector::Dot(y)` = `Real()·y.Real() + Imag()·y.Imag()` → receiver linear, **second arg `y` conjugated**), and `vector.hpp:246` (`// Calculate the parallel inner product yᴴ x`). Corrected all three locations to Palace's actual L0 form `yᴴ A x` (Summary `CYCLE.md:12`; signature-sketch comment block `CYCLE.md:32-35`; Open-question prose `CYCLE.md:101`). Disambiguated where the L2 entry's separate arg-1 `xᴴ` pin (matching the L1 leaves) differs from the L0 characterization, per the standing stub `book/src/L2/inner_product.md:7` ("Palace documents `Dot(comm, x, A, y) = yᴴ A x`"). The report is now consistent with the stub it characterizes. Mechanical math-notation fix.

- **Finding 2 (low — kernel-difference imprecision).** `CYCLE.md:78` claimed `dot` vs `tdot` differ "ONLY in the sign of the imaginary cross-terms."
  - **Decision**: repaired.
  - **Action**: Verified `vector.cpp:263-274` via `read_range` — `Dot` real = `Re·Re + Im·Im`, `TransposeDot` real = `Re·Re − Im·Im` (the real parts differ on the `Im·Im` term, not only the imaginary cross-terms). Rewrote `CYCLE.md:78` to state both the `Im·Im` real-part sign difference and the imaginary-cross-term difference, with the per-element forms `Dot = a·conj(b)` / `TransposeDot = a·b`, and cited `book/src/L1/dot.md:112-113` which records this correctly. Mechanical wording fix.

- **Finding 3 (low — nonexistent slug).** `CYCLE.md:68`, `:95` referenced `constructed-operator-gate`.
  - **Decision**: repaired.
  - **Action**: Confirmed via `ls book/src/concepts/` that only `nested-constructed-operator-gate.md` (+ siblings `constructed-operators.md`, `constructed-operator-factory.md`) exist; no `constructed-operator-gate.md`. Replaced both references with `nested-constructed-operator-gate`. Plain-prose slug fix (no build break either way; makes the Qualification-B partial-capture backstop verifiable).

- **Finding 4 (low — skill telemetry).** No skill invocations named.
  - **Decision**: not-needed.
  - **Rationale**: Pure telemetry surface; recording a skill name post-hoc would be authoring a claim about what the producer did, not a mechanical fix. Left as the critic's non-blocking survey note.

- **Finding 5 (informational — `tdot` evidentiary weight).** Critic noted it is well-handled, no fix requested.
  - **Decision**: not-needed (no defect).

### Unrepairable findings

None. All flagged issues were mechanical (math-notation, wording, slug) and surgically repairable on the proposal report; the skill-telemetry warning is non-blocking and non-substantive. The critic's mode-validation soundness assessment and the conjugation-contradiction self-correction were affirmed as correct (no defect to repair).

## Suggested resolution

`ready`. Notes for the integrator:
- This is a PROPOSAL / mode-validation report — it emits NO `edit:book/...` block (correctly, per the dispatch-phase write-guard; the `inner_product` L2 rough-in row already stands from cycle-018). Nothing to apply to `book/`.
- The actionable persistence is the report's harvester-input characterization (fold-law, four parameter axes, over-unification guard, `tdot`-uncalled finding, conjugation-pinning OQ). The natural home is an OQ-ledger append (integrator-per-report owns `scaffolding/open-questions.md`); the conjugation-pinning item is already tracked by OQ `inner-product-harvester-formalization-and-conjugation-pinning`.
- After repair, the report's L0-characterization of the M-weighted member (`yᴴ A x`) now matches the standing stub `book/src/L2/inner_product.md:7` — the in-flight cycle-019 inner_product harvester can inherit the corrected math directly.
- Mode-gap finding (Qualification B — no positive channel for non-fold "constructed-operator-action" parametric families) is correctly routed to the next meta-phase; non-blocking for this cycle.
