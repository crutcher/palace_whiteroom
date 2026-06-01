---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T230000Z
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
repaired_at: 2026-06-01T231500Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: not-needed
  edge-label-fidelity: not-needed
  plan-kind-consistency: not-needed
  skill-uptake-survey: not-needed
overall_status: ready
follow_up_agent: null
---

# META: verification of L2/L3 index reconciliation + cohort-narrative + count (cycle-052 D4)

## Critique

### Checks run

**citation-validity — warning.** Ran `citecheck.py --scan` on the report (4 ok, 2 "failing") and `--anchor` on the one load-bearing L0 pinpoint. The two scan "failures" (`normalize.md:111`, `scal.md:223-228`) are **false positives** — they are book-internal file:line pointers (a micro-sweep target line; the scal §Dependencies range being REMOVED), not L0 source citations; the scanner only flags them as ambiguous basenames. No real defect there. The single genuine L0 citation in the edits is `vector.cpp:745-772` (the `axpbypcz` template specialisations, change 7 `[new]`). `--anchor 'AXPBYPCZ'` against `palace/linalg/vector.cpp:745-772` resolves OK (anchor at lines 746–771, in range). **The warning:** that pinpoint is written as the **bare basename** `vector.cpp:745-772`, missing the `palace/linalg/` prefix — citecheck `[MISS]` on the bare form, `[ok]` only with the full path. This is a path-hygiene defect carried verbatim from the on-disk `[old]` row (the on-disk `axpbypcz.md` uses the correct full path `palace/linalg/vector.cpp:745-772`), so D4 propagates rather than introduces it. Low severity (range is real, anchor confirmed), but the index row should use the resolvable full path.

**surface-or-evidence — pass.** Refinement-shaped proposal (modifies existing index dep-map rows + cohort narrative). It modifies surface (index/narrative text) and the rotation evidence is the existing firm combinators (`linear_combination`/`inner_product` at L2/L3, all confirmed `## Status` present on-disk). Not a pure rotation_claim; the surface edits are the substance.

**rotation-quality — pass.** Not a new-rotation proposal; this is an index/count reconciliation recording an already-landed rotation (the combinator-as-entry refactor). The recorded relationships (leaf → specialization/consumer-stub of combinator) are strictly-more-abstract (the combinator subsumes the per-arity / per-conjugation leaves), consistent with the vocabulary-shift redirect. No renaming-only masquerade.

**variant-axis-coverage — pass.** The variant axes each stub retains are explicitly scoped: `dot` keeps the conjugation axis (Hermitian/`tdot`), `nrm2` keeps the `std::abs` guard + element-type (collapsed), the arity members keep element-type/scalar-promotion, and output-aliasing is explicitly attributed to the FOLD (not leaf-specific). No hidden branches.

**cross-reference-integrity — pass.** All 21 `[old]` anchors verified to exist verbatim on-disk (10 in L2/index.md, 5 in L3/index.md, 3 in L3/linear_combination.md, 3 in L2/normalize.md); the change-15 anchor confirmed unique (count=1). All combinators the stubs point up to exist and are firm. No firm-body-inside-fence concern (these are dep-map-row/prose edits, not new firm chapter bodies). Collision discipline clean: D4 touches only index.md ×2, L2/normalize.md, L3/linear_combination.md — none are the leaf-body chapters D1/D2/D3 rewrite (the L{2,3}/{scal,axpy,axpby,axpbypcz,dot,nrm2}.md bodies). normalize.md and linear_combination.md are the composite/combinator chapters, distinct from the reduced leaves.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge-label entries authored; the edges referenced (L3>L2 in-line identity notes, L2>L1 fold-specialization themes) are named consistently with their prose.

**plan-kind-consistency — pass.** Declared kind is index/count reconciliation (layer-intro-author). Content matches: dep-map rows, cohort narrative, count tally, frontmatter-coordination note, micro-sweep. No firm-operator-with-placeholders mis-classification.

**skill-uptake-survey — pass.** The report references the count-ownership convention (`parallel-blind-shared-index-count-divergence`) and the collapsed-leaf-disposition convention. citecheck was self-flagged as not-run by the producer; I ran it (see citation-validity). No blocking skill gap.

### Issues found

1. **[low] Bare-basename L0 citation in change-7 `[new]` row** (`CYCLE.md` §"7. L2/index.md — dep-map row: axpbypcz", `[new]` status cell): the `axpbypcz` template-specialisation citation is written `vector.cpp:745-772` — citecheck `[MISS]` on the bare basename; resolves `[ok]` only as `palace/linalg/vector.cpp:745-772` (anchor `AXPBYPCZ` confirmed at lines 746–771). Carried verbatim from the on-disk `[old]` row (the standalone `axpbypcz.md` already uses the full path), so propagated, not introduced. The resolvable full path should be used.

2. **[informational, not a defect] Micro-sweep changes 19/20/21 depend on D1 being applied first.** D4's `normalize.md` micro-sweep retires references to the scal.md §Dependencies "223-228" range on the premise that D1 reduced `L2/scal.md` to a stub (deleting that range). On disk `scal.md` is still 365 lines with the §Dependencies range intact — i.e. **D1 is not yet applied** (wave-1 producers' edits are still staged in their own CYCLE.md, pre-integration). This is consistent with the documented wave ordering (D1/D2/D3 apply before D4 at integration), and D4's `[old]` anchors correctly match the current pre-D1 disk state. Flagging only as an integration-ordering dependency the integrator must honor (apply D1 before D4); not a content defect.

3. **[informational] `fold_parent` no-op claim is correctly scoped but not globally true.** D4 asserts the `fold_parent:`→`specialization_of:` frontmatter rename is a no-op because neither index keys off the field — verified true for both index files. Note that `scaffolding/open-questions.md` and `scaffolding/integrator-signals.md` do mention `fold_parent` in prose, but those are not index consuming-conventions and do not contradict D4's narrowly-scoped claim. No action needed; recorded so a reader does not over-read the no-op claim.

### Verified-correct load-bearing claims

- **Count integrity (the core claim): confirmed exact.** L2/index.md has exactly 21 `firm` rows + 1 partly-constructive (`deflate`) = 22 dep-map rows; L3/index.md has exactly 17 `firm` + 3 `partial-obstruction` rows; the L3 single-authoritative tally bullet on-disk reads "17 firm + 3 partial-obstruction". D4 introduces NO count delta (reduce-to-stub keeps all files on disk, statuses stay `firm`), and change-14 restates the count without changing a number. No off-by-one.
- **dot=specialization / nrm2=consumer labels: correct and consistent** across all 21 blocks + summary; do-NOT-merge boundary preserved for both.
- **refactor-pass-COMPLETE framing: present and coherent** in changes 1, 2, 3, 10, 14 (both indexes) and the micro-sweep tense fixes; the retired rectangular-floor / leaf-vs-fold-fork framing is removed from the fold-family cohort while historical cycle-042/043 standalone-floor narratives are correctly left intact (they have no combinator to defer to).
- **Fence parity: 42 fence markers = 21 balanced edit blocks.**

## Repair

### Fixes attempted

- **Finding**: [low] Bare-basename L0 citation in change-7 `[new]` row — `axpbypcz` template-specialisation pinpoint written as bare `vector.cpp:745-772`; citecheck `[MISS]` on the bare form, `[ok]` only as `palace/linalg/vector.cpp:745-772` (anchor `AXPBYPCZ` confirmed lines 746–771, in range).
  - **Decision**: repaired
  - **Action**: `CYCLE.md` §"7. L2/index.md — dep-map row: axpbypcz", `[new]` status cell — changed the bare `vector.cpp:745-772` to the full resolvable path `palace/linalg/vector.cpp:745-772`. In-scope (citation line range / path-hygiene fix; range + meaning already correct). The `[old]` row is intentionally left bare — it matches the current pre-D1 on-disk state the edit anchors against; only the `[new]` row D4 authors is corrected.

### Informational notes (no fix)

- **Integration-ordering dependency (changes 19/20/21 micro-sweep).** D4's `normalize.md` micro-sweep retires references to the `scal.md` §Dependencies "223-228" range on the premise that D1 reduced `L2/scal.md` to a stub. D4 is wave-2, applied after the wave-1 leaf reductions (D1/D2/D3), so the integration order honors this dependency. D4's `[old]` anchors correctly match the current pre-D1 disk state. Integrator must apply D1 before D4. Not a content defect.
- **`fold_parent`→`specialization_of` no-op claim is correctly scoped.** Verified true for both index files (neither keys off the field). `scaffolding/open-questions.md` / `scaffolding/integrator-signals.md` mention `fold_parent` in prose, but those are not index consuming-conventions and do not contradict D4's narrowly-scoped claim. No action.

### Unrepairable findings

None.

## Suggested resolution

`ready`. The lone warning was a one-token path-hygiene fix (bare basename → full path), now applied; range and anchor were already correct. Integrator note: this is a wave-2 report — apply D1/D2/D3 (the leaf-body reductions) before D4 so the micro-sweep `[old]` anchors and the reduce-to-stub premise hold. No count delta introduced (reduce-to-stub keeps files; statuses stay firm).
