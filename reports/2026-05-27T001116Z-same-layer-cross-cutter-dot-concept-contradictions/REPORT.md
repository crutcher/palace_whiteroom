---
agent: same-layer-cross-cutter
invoked_at: 2026-05-27T00:11:16Z
scope: concepts cross-cut — dot-concept-contradictions
status: pending
inputs:
  - book/src/L1/dot.md (cycle-002 firm L1 operator)
  - book/src/concepts/dot.md (older cross-cutting concept page; pre-layered-era)
  - reference/palace/palace/linalg/vector.hpp (Dot/TransposeDot declarations)
  - reference/palace/palace/linalg/vector.cpp (Dot/TransposeDot bodies)
  - grep -rn 'Dotc' reference/palace/ (zero results)
skill_uptake:
  - skill: verify-citation-range
    triggered: true
    decision: artifact_landed
    rationale: Used to verify `vector.cpp:142-178` contains `Get`/`operator=`/`SetBlocks` (not dot), refuting the concept page's bogus citation; results embedded in §"Specific finding" row 3 and §"Supporting evidence".
  - skill: classify-variant-axis
    triggered: true
    decision: explained_non_applicable
    rationale: Report is observation-shape (Contradiction kind), not operator-promotion; variant-axis classification is the rewrite task for cycle-004 `layer-intro-author`, not for this cross-cutter report.
  - skill: verify-refinement-surface
    triggered: true
    decision: explained_non_applicable
    rationale: Report carries no proposed-changes block (cross-cutter role is observation-only); refinement-surface verification does not apply.
integrated_at: 2026-05-27T00:23:54Z
integration_commit: 9aa1c59
integration_notes: Observation-only report; no proposed-changes block to apply. Three contradictions surfaced are recorded for cycle-004 layer-intro-author dispatch (rewrite concepts/dot.md). Four open questions promoted to ledger (concepts-page-authorship-role-scope, concepts-pre-layered-era-sweep, dot-blas-heritage-framing-salvage, dot-backpointer-staleness-after-rewrite). Role-scope question for layer-intro-author vs concept-page-author surfaced to meta-phase.
---

# REPORT: concepts observation — dot-concept-contradictions

## Summary

Comparing the cycle-002 firm L1 operator `book/src/L1/dot.md` against the older cross-cutting prose page `book/src/concepts/dot.md`, the concept page contains three concrete contradictions with the L1 entry and with the Palace source itself: (1) it asserts `ComplexVector::Dot` returns a *real* scalar — the source signature returns `std::complex<double>`; (2) it names a symbol `linalg::Dotc` that does not exist anywhere in the Palace tree (full-tree `grep` returns zero hits) and inverts the conjugation role between `Dot` and `TransposeDot`; (3) its sole cited source range (`vector.cpp:142-178`, claimed to define the projection) does not contain any dot definition — it covers `ComplexVector::Get` / `operator=`. The L1 entry already calls out item (1) inline (`L1/dot.md:17`); items (2) and (3) are not yet flagged anywhere in the artifact and would silently propagate into any downstream chapter that follows the concept page's prose. The L1 entry is authoritative on every point; the concept page is wrong on every contested claim.

## Observation kind

**Contradiction** — `concepts/dot.md` contains semantics that conflict with `L1/dot.md` and, more importantly, with the cited L0 source. This is not a "two operators on the same layer disagree" case; it is "the cross-cutting concept page contradicts both the firm operator entry above it and the source below it." Within the role-spec menu, `Contradiction` is the closest fit (the concept page and the L1 operator are both same-layer-of-discourse for the `dot` family, even though one lives under `concepts/` and the other under `L1/`).

## Specific finding

Three contradictions, side-by-side:

| # | `concepts/dot.md` claim | Palace source reality | `L1/dot.md` agrees with |
|---|---|---|---|
| 1 | "Palace's `Vector::Dot` and `ComplexVector::Dot` both return a **real** scalar" (`concepts/dot.md:27-29`); canonical signature listed as `dot(x, y) → ℝ` (`concepts/dot.md:44`) | `ComplexVector::Dot(...) const` returns `std::complex<double>` (`palace/linalg/vector.hpp:111`). Body returns a non-trivial imaginary part for cross-vector cases (`palace/linalg/vector.cpp:263-267`). `mfem::Vector::operator*` does return `double`, but `ComplexVector::Dot` does not. | Source. `L1/dot.md:17` and `L1/dot.md:37-43` explicitly call out the concept page's error and show element-type → return-type table. |
| 2 | "The complex-conjugate version is `Dotc`; the un-conjugated bilinear version is `Dot`" (`concepts/dot.md:18`) | (a) **`Dotc` does not exist.** `grep -rn 'Dotc' reference/palace/` returns zero hits. (b) **Conjugation polarity is inverted.** `ComplexVector::Dot` *is* the conjugated/Hermitian form: `vector.hpp:110` header comment names it `yᴴ x`, and `vector.cpp:263-267` computes the conjugated kernel. `ComplexVector::TransposeDot` is the unconjugated bilinear form: `vector.hpp:110` names it `yᵀ x`, body at `vector.cpp:269-274` confirms. | Source. `L1/dot.md:10-11`, `L1/dot.md:40-41`, `L1/dot.md:99-100` correctly map `dot` → `ComplexVector::Dot` (Hermitian) and `tdot` → `ComplexVector::TransposeDot` (unconjugated). |
| 3 | "See [palace/linalg/vector.cpp:142-178](...) for the projection definition." (`concepts/dot.md:37-39`) | Lines 142–178 of `vector.cpp` are the body of `ComplexVector::Get` (device/host pointer dispatch) and the start of `operator=(std::complex<double>)` / `SetBlocks` — not any dot definition. The actual `Dot` body is at `vector.cpp:263-267`. The cited "projection definition" does not exist as a Palace function at all (claim 1 above means there is no projection happening in the C++; projection only enters caller-side via `std::abs` / `std::real`, as documented at `L1/dot.md:43`). | Source. `L1/dot.md:113-125` has a comprehensive evidence list with verified line ranges. |

All three contradictions stem from a single underlying misreading: the concept page (predating the L1 entry, predating direct source verification) appears to have been authored from BLAS-API memory rather than from the Palace headers, mixing up `cdotc`/`cdotu` BLAS naming with Palace's `Dot`/`TransposeDot` and then rationalising the inversion via an invented "real-projected" convention. The L1 entry corrects all three by direct citation.

## Recommendation

**Dispatch `layer-intro-author` in cycle-004 with scope `rewrite concepts/dot.md to align with L1/dot.md`.**

Routing rationale:
- `harvester` is wrong — its scope is "formalize one L_n operator per invocation," and the L1 `dot` operator is already firm; this is not an operator-promotion task, it's a concept-page reconciliation.
- `integrator` is wrong — it applies reports, doesn't author.
- A new `concept-page-author` role would be a meta-phase ask; defer.
- `layer-intro-author` is the closest existing fit: its role is described as authoring "L_n / L_{n+1}>L_n Part overviews + dep-maps" in CLAUDE.md §"The 13 agents," and the `concepts/` library functions as cross-cutting narrative material analogous to a Part overview (per-concept rather than per-layer). The fit is imperfect — see Open questions.

Suggested concrete scope for the dispatch:
1. Rewrite `concepts/dot.md` to: (a) state the correct return-type rule (complex element-type → complex return; real → real); (b) name `ComplexVector::Dot` (Hermitian) and `ComplexVector::TransposeDot` (unconjugated) correctly, and delete every reference to the non-existent `linalg::Dotc`; (c) replace the bogus `vector.cpp:142-178` cite with the verified ranges already collected in `L1/dot.md:113-125`; (d) demote the page from "primary definition" to "narrative pointer at `L1/dot.md`" with the concept-page acting as cross-cutting prose (variant-axis-coverage, slice-usage index) rather than authoritative signature.
2. Update the back-pointer in `L1/dot.md:17` once the concept page is corrected (it currently warns the reader that the concept page is wrong — that warning becomes redundant and should be removed in the same cycle by the integrator or a follow-on `layer-intro-author` pass).
3. Sweep `book/src/concepts/` for any other concept pages that predate the layered era for analogous wrong-signature / hallucinated-symbol risks (out of scope for this report; flag as candidate cycle-005 dispatch).

## Supporting evidence

- `book/src/L1/dot.md:1-126` — cycle-002 firm L1 operator entry. Particularly:
  - `L1/dot.md:10-11` — correct mapping of `ComplexVector::Dot` (Hermitian, returns complex) and `ComplexVector::TransposeDot` (unconjugated, returns complex).
  - `L1/dot.md:17` — inline note that `concepts/dot.md` is wrong about the return type.
  - `L1/dot.md:37-43` — element-type → return-type table.
  - `L1/dot.md:113-125` — verified evidence list (correct cited line ranges).
- `book/src/concepts/dot.md:1-60` — concept page with the three contradictions. Particularly:
  - `concepts/dot.md:17-18` — invented `Dotc` symbol; inverted conjugation roles.
  - `concepts/dot.md:25-31` — wrong return-type claim ("both return a **real** scalar").
  - `concepts/dot.md:37-39` — wrong source citation (`vector.cpp:142-178`).
  - `concepts/dot.md:43-45` — canonical signature listed as `dot(x, y) → ℝ`.
- `reference/palace/palace/linalg/vector.hpp:110-113` — declarations for `ComplexVector::Dot` (return type `std::complex<double>`) and `ComplexVector::TransposeDot`; header comment `Vector dot product (yᴴ x) or indefinite dot product (yᵀ x) for complex vectors.`
- `reference/palace/palace/linalg/vector.cpp:263-267` — `ComplexVector::Dot` body computing the Hermitian kernel.
- `reference/palace/palace/linalg/vector.cpp:269-274` — `ComplexVector::TransposeDot` body computing the unconjugated bilinear kernel.
- `reference/palace/palace/linalg/vector.cpp:142-178` — actually `ComplexVector::Get` / `operator=` / start of `SetBlocks`; no dot content (refuting the concept page's citation).
- `grep -rn 'Dotc' reference/palace/` — zero matches (refuting the existence of `linalg::Dotc`).

## Open questions / caveats

1. **Role-scope clarification (meta-phase input).** The role-routing table in CLAUDE.md §"The 13 agents" doesn't explicitly assign `concepts/` page authorship to any of the 13 agents. `layer-intro-author` is described as authoring "L_n / L_{n+1}>L_n Part overviews + dep-maps." `concepts/` is neither a Part overview nor a dep-map; it's a third category (cross-cutting prose, indexed by primitive rather than by layer). The pragmatic recommendation above routes to `layer-intro-author` as the closest existing fit, but **meta-phase should consider** whether to (a) explicitly broaden `layer-intro-author`'s scope to include `concepts/`, (b) add a `concept-page-author` role, or (c) decide that `concepts/` is in the process of being absorbed into per-layer chapters and should not receive net-new authorship (in which case the cycle-004 dispatch could instead *delete or stub* `concepts/dot.md` and redirect readers to `L1/dot.md`). Flagging here for meta-phase, not blocking the cycle-004 dispatch.
2. **Concept-page-wide risk.** Only `concepts/dot.md` was inspected. The same pre-layered-era authorship pattern likely affects other concept pages (e.g. `concepts/axpy.md`, `concepts/orthogonalize.md` if present). A sweep is warranted but out of scope per the one-observation-per-invocation discipline.
3. **Does the BLAS-convention framing have any salvageable value?** `concepts/dot.md`'s "Background" section (`concepts/dot.md:25-39`) ties Palace's dot to BLAS `ddot`/`zdotc` heritage. The framing is partly useful (Palace is BLAS-flavoured); only the *factual claims about Palace's actual return type and symbol names* are wrong. A rewrite should keep the BLAS-heritage framing while correcting the specifics.
4. **Risk of stale back-pointer.** `L1/dot.md:17` currently contains a warning that the concept page is wrong. If the concept page is corrected but the back-pointer warning isn't deleted, future readers will be confused. Whichever agent edits `concepts/dot.md` should either also edit `L1/dot.md:17` (if their write-authority permits) or flag the back-pointer for the integrator. Per CLAUDE.md write-authority partition, `layer-intro-author` writes to `reports/<id>/REPORT.md`, and the integrator applies; so the cycle-004 REPORT should explicitly propose the `L1/dot.md:17` edit as part of the diff for the integrator to apply.
