---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T000000Z
critic_version: 1
checks:
  citation-validity: warning
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-01T000000Z
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

# META: verification of "Formalize axpy at L2" (cycle-043 D3, L2 axpy floor)

## Critique

### Checks run

**citation-validity — warning.** Mechanical `citecheck.py --scan` returned `10 ok, 0 failing` (bounds + path hygiene clean). I anchor-verified all six load-bearing L0 pinpoints against the resolved tree (`reference/palace/palace/linalg/vector.{cpp,hpp}`) and read each range. All anchors land in-range and the structural claims hold on the meaning-read: `:702-712` is the real-real `AXPY(double, Vector, Vector)` with the `alpha == 1.0` fast-path at `:704` (`y += x` else `y.Add(alpha, x)`) — exactly as described; `:714-718` is the real-α-on-complex forwarding overload (`y.AXPY(alpha, x)`); `:276-311` is `ComplexVector::AXPY` + the `forall_switch` kernels (the `ai != 0` branch at `:307` is `YR[i] += ar·XR[i] − ai·XI[i]`, matching the report's kernel sketch); `vector.hpp:115-118` is the member decl with the `In-place addition (*this) += alpha * x` comment; `vector.hpp:305-307` is the free-fn template decl. **One precision defect:** the citation pointer `palace/linalg/vector.cpp:715-723`, labeled "the complex-α overload `AXPY(std::complex<double>, ComplexVector, ComplexVector)`", does not cleanly bound that construct — the complex-α overload is at lines **720-724** (the report's OWN inline parenthetical correctly says `(:720-724)` at CYCLE.md:400). The cited `715-723` range instead (a) includes lines 715-718, which are the tail of the *real-α-on-complex* forwarding overload already covered by the separate `:714-718` citation, and (b) omits line 724, the closing brace of the complex-α overload. The anchor `complex` matched at line 721 (in-range), so `--scan` passed it as bounds-valid, but the pointer mislabels its construct. This is a citation-precision warning, not a bounds failure — the correct range (`720-724`) appears inline in the same bullet, so the meaning is recoverable.

**surface-or-evidence — pass.** This is a `new:` operator entry (not a refinement of an existing operator/theme): a brand-new `book/src/L2/axpy.md` chapter plus an additive index dep-map row and SUMMARY registration. The check is oriented at refinement-shaped proposals; for a new-floor entry the relevant bar is that the surface (the chapter body) is present with its evidence chain, which it is. Not a pure rotation_claim. Pass.

**rotation-quality — pass.** The report does NOT claim a compacting rotation; it explicitly and correctly frames the L2↔L1 relationship as **identity-in-form** (value-thread-isomorphic, textually identical signature, no multi-operation kernel fusion to unfold beyond the arity-2 single aligned pass). Under the methodology this is the licensed shape for a thin floor under the "Identity-lowerings still require both L levels" invariant — it is not asserted as a 1:1 *rotation* dressed up as a rotation; it is correctly labeled an identity-in-form floor whose justification is layer-coherence, not abstraction gain. The fusion content is deferred to `linear_combination` §"Fusion note" (the arity-2 case), which is the correct home for it. Pass (identity-in-form floor, properly framed).

**variant-axis-coverage — pass.** Two axes are listed (element-type real|complex; scalar-promotion sub-axis), matching the L1 and L3 entries exactly. The orthogonal **output-aliasing** axis (in-place vs out-of-place) is explicitly handled: the entry attributes it to the FOLD (`linear_combination` §Variant axes axis 1), carried by reference, NOT introduced as a leaf-specific axis, and records the rationale + OQ `arity-family-leaf-floors-output-aliasing-axis-is-the-folds`. I verified `linear_combination.md:220` is indeed "Output aliasing (in-place vs out-of-place)" axis 1 — the attribution is correct and the construction-time absorption of both leaf axes is stated. No hidden branches. Pass.

**cross-reference-integrity — pass.** All linked artifact targets exist on disk: `L1/axpy.md`, `L3/axpy.md`, `L2/scal.md`, `L2/linear_combination.md`, `L2/index.md`, `L1-L0/axpby-mutation-rotation.md`, `concepts/axpy.md`, `concepts/scalar-promotion.md`, `L1/axpby.md`, `decisions/axpby-as-primitive.md`. The fold-parent claim is exact: `linear_combination.md:69` is `axpy(α, x, y) = linear_combination [(α, x), (1, y)] -- second coeff fixed to 1`; law 6 ("Specialization identities (derived)") is at `:150`; output-aliasing axis 1 at `:220`. The index `linear_combination` anchor row (`L2/index.md:69`) matches the edit block's first line verbatim, and no `axpy` row pre-exists (no duplication); insertion lands cleanly between `linear_combination` (69) and `scal` (70). SUMMARY currently has `linear_combination`/`scal` with no `axpy` — the edit inserts `axpy` between them, matching the shown context. Firm-body-inside-fence guard: 6 fence markers (3 balanced pairs), even parity, no nested fences; the firm apparatus (`## Status` :315, Signature :105, Algebraic laws :173, Evidence :359) is fully INSIDE the `new:book/src/L2/axpy.md` block — no fence-truncation defect. The one bracketed ref `[`L0/transparent-vs-load-bearing-tricks`]` (CYCLE.md:170) is a reference-style link with no `(url)` definition, so it renders as literal text (no linkcheck2 hazard); the target file does exist on disk, mirroring how `scal.md` writes the same reference as plain prose. Pass.

**edge-label-fidelity — pass.** The entry carries L2↔L1 (Lowers to / Lifts from) and a cited fold-membership edge to `linear_combination`. The prose discusses exactly those edges: §"Lowers to" narrates L2→L1 identity-in-form; §"Lifts from" narrates L1→L2; the fold-specialization identity discusses the `axpy`→`linear_combination` arity-2 relationship. No L3>L2 edge is authored here (correctly deferred — the L3 re-anchor is routed to c044). Labels match prose. Pass.

**plan-kind-consistency — pass.** Declared `firm`; content shape supports it. The firm justification is the firm-on-positive-structure escape (syntactic-identity laws on the small fully-present `AXPY` free-function / `ComplexVector::AXPY` surface; absence of a dedicated `axpy` unit test does not gate firm), consistent with the precedent escapes for `scal` (cycle-041) and `linear_combination` (cycle-018) and the CLAUDE.md `apply_linop`-situation carve-out. No rough-in placeholders, no unresolved TODOs in the body. The six inherited laws match `L1/axpy.md:41-46` verbatim. Pass.

**skill-uptake-survey — pass.** The report's shape (L0-anchored citations) implies `verify-citation-range` / the mechanical `citecheck` realization; the report references its invocation explicitly ("self-verified via `tools/citecheck/citecheck.py --anchor` + `Read`", CYCLE.md:458) and reports `[ok]` results. Telemetry present. Pass.

### Issues found

1. **Citation pointer mislabels its construct — `vector.cpp:715-723` should be `720-724`** (CYCLE.md frontmatter line 12; §Variant axes / §Evidence line 399-401; §Supporting evidence line 458). Severity: **low-moderate (warning)**. The range `715-723` is labeled "the complex-α overload `AXPY(std::complex<double>, ...)`" but that overload occupies lines 720-724 (the report's own parenthetical at :400 says `(:720-724)`). The cited range straddles the tail of the preceding real-α forwarding overload (715-718, already covered by `:714-718`) and truncates the complex-α overload's closing brace (omits 724). Bounds-valid (anchor `complex` at 721), so `--scan` passes it, but the pointer does not delimit the construct it names. Repair: change the three occurrences of `:715-723` to `:720-724`.

2. **"Two non-laws inherited unchanged" framing is inaccurate — the body lists three non-laws** (frontmatter input line 7 / Summary line 20 say "two non-laws... inherited"; §Algebraic laws lines 211-225 and §"Operator content" line 449 list three). Severity: **low (warning)**. `L1/axpy.md` lists exactly two non-laws (commutativity, ternary non-associativity; `L1/axpy.md:47-52`). The L2 report adds a THIRD non-law — IEEE-754 floating-point summation non-associativity — which is well-grounded (consistent with the load-bearing-numerical-trick methodology and the `linear_combination` permutation non-law) but is an *addition*, not strictly "inherited unchanged" from L1/axpy. The summary's "two non-laws inherited unchanged" undercounts and mis-frames its own body. Repair: reconcile the count (either "three non-laws (two inherited from L1 + the FP-summation non-law made explicit at L2)" or align the summary to "three").

3. **(Very low / non-blocking) `[`L0/transparent-vs-load-bearing-tricks`]` left as a non-resolving reference-style bracket** (CYCLE.md:170). The target `book/src/L0/transparent-vs-load-bearing-tricks.md` exists on disk; the `upgrade-plain-text-ref-to-live-link-when-target-on-disk` skill would license making it a live link `[...](../L0/transparent-vs-load-bearing-tricks.md)`. Not a build hazard (renders as literal text, no linkcheck2 error) and consistent with how `scal.md` writes it as prose — flagged only as an optional uptake opportunity, not a defect.

**Note (not a defect):** The report's caveat #1 (the firm L3 `axpy` entry goes stale once this floor lands — `L3/axpy.md:6,:97,:114` assert a direct L3→L1 rotation with "no L2 intermediate") is accurate (I confirmed those three sites) and is correctly scoped OUT of this dispatch and routed to the c044 L3-re-anchor sweep per the one-operator-per-invocation discipline. Not a defect here. Likewise count-ownership is correctly observed (only the own dep-map row + body + SUMMARY appended; the L2/index consolidated firm-count tally deferred to D2), and the fold-member discipline (cited as arity-2 member, NOT merged; fixed-1 y-coefficient distinction from axpby; fusion deferred to the fold) is correct throughout.

---

## Repair

### Fixes attempted

1. **Finding**: Citation pointer mislabels its construct — `vector.cpp:715-723` labeled "the complex-α overload" but that overload is at `:720-724` (CYCLE frontmatter line 12, §Evidence line 399-400, §Supporting-evidence line 458). *(critic Issue 1; citation-validity warning)*
   - **Decision**: repaired
   - **Action**: On-disk verified via codemap `read_range` + vanilla `Read` of `reference/palace/palace/linalg/vector.cpp` (no codemap↔disk +1 drift). The complex-α overload `AXPY(std::complex<double>, ComplexVector, ComplexVector)` occupies lines 720-724 (`template <>` at 720, signature 721, body 722-723, closing brace 724); the cited `715-723` straddled the tail of the preceding real-α forwarding overload (715-718, already covered by the separate `:714-718` citation) and truncated the closing brace 724. Changed all THREE occurrences of `:715-723` → `:720-724` (frontmatter input list; §Evidence L0-anchor bullet — also dropped the now-redundant inline `(:720-724)` parenthetical; §Supporting-evidence self-verified list). The `:714-718` real-α forwarding anchor was left untouched (it was already correct).

2. **Finding**: "Two non-laws inherited unchanged" framing undercounts the body, which lists three non-laws (the IEEE-754 FP-summation non-law is an L2 addition, not inherited from L1/axpy which has exactly two). *(critic Issue 2; citation-validity warning)*
   - **Decision**: repaired
   - **Action**: Reconciled the count to match the body, keeping the (valid) IEEE-754 FP-summation non-law. (i) Summary line 20: "six laws + two non-laws + two variant axes inherited unchanged" → "six laws + two inherited non-laws (with the IEEE-754 FP-summation non-law made explicit at L2 — three non-laws total in the body) + two variant axes inherited unchanged". (ii) Frontmatter input line 7: "two non-laws" → "two inherited non-laws". (iii) §Algebraic-laws non-law header "Laws that explicitly do not hold (inherited from L1):" → "(the first two inherited from L1; the IEEE-754 FP-summation non-law made explicit at L2):". (iv) The FP-summation non-law's own closing sentence "Inherited from L1; recorded here, not erased." → "Made explicit at L2 (not among L1/axpy's two non-laws; added here under the load-bearing-numerical-trick methodology), recorded, not erased." The §"Operator content" summary at line 449 already said "three non-laws" and was left as-is (now consistent with the body and the reconciled summary).

3. **Finding** (very-low / optional): `[`L0/transparent-vs-load-bearing-tricks`]` left as a non-resolving reference-style bracket (CYCLE.md:170); target exists on disk. *(critic Issue 3; cross-reference / uptake opportunity)*
   - **Decision**: repaired (trivial)
   - **Action**: Confirmed `book/src/L0/transparent-vs-load-bearing-tricks.md` exists on disk; upgraded the reference-style bracket to a live link `[`transparent-vs-load-bearing-tricks`](../L0/transparent-vs-load-bearing-tricks.md)` per the `upgrade-plain-text-ref-to-live-link-when-target-on-disk` skill. Relative path from `book/src/L2/axpy.md` verified (`../L0/...`).

### Unrepairable findings

None. All three findings were mechanical/surgical (citation-range correction, count reconciliation, plain-text→live-link upgrade) and fully within repair authority — no substantive re-authoring required. The IEEE-754 non-law content itself was kept intact (the critic affirmed it is valid); only the count/framing was reconciled.

## Suggested resolution

`ready`. Notes for the integrator:
- Citation-validity warnings both repaired in-place; the `:720-724` correction is on-disk verified (codemap + Read, no drift). All six L0 anchors now bound their named constructs.
- The non-law count is now internally consistent across frontmatter / Summary / §Algebraic-laws body / §"Operator content" (three non-laws in the body: two inherited from L1 + the L2-explicit IEEE-754 FP-summation non-law).
- The new live link `../L0/transparent-vs-load-bearing-tricks.md` resolves to an on-disk file — no `linkcheck2` hazard introduced; integrator's build gate should pass it.
- The report's own caveats (L3/axpy staleness → c044 re-anchor sweep; output-aliasing-axis-ownership OQ; L2/index consolidated tally → D2) are correctly scoped out and routed; nothing for the integrator to action beyond the standard OQ promotion.
