---
verifies: ../CYCLE.md
critiqued_at: 2026-06-07T161500Z
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
repaired_at: 2026-06-07T162400Z
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

# META: verification of "Combinator candidate — inner-product-family-re-style-elimination" (D4)

## Critique

### Checks run

**citation-validity — warning.** `citecheck --scan` on the report: 57 ok / 1 failing of 58 citations. The single failing item is `operator.cpp:598-617` flagged `[AMBIG]` (bare basename matches both `reference/palace/palace/linalg/operator.cpp` and `.../fem/libceed/operator.cpp`). I resolved it: as `palace/linalg/operator.cpp:598-617` it is in-range and OK (`citecheck` confirms `[ok]`). This is a path-hygiene defect (missing the `linalg/` qualifier in the report's §Supporting-evidence line 410), NOT an out-of-range/wrong citation — the referent is the firm `inner_product` evidence anchor and is correct. All other cited line-pinpoints (the combinator §-section anchors `:176/:449` L2, `:146/:333` L3; the L0 anchors `vector.cpp:263-274,664-685`; `:266,679`) are in-range. Warning (not pass) only on the ambiguous-basename hygiene; not load-bearing for the refactor's correctness.

**surface-or-evidence — pass.** This is a destructive consolidation refactor of an EXISTING firm combinator, not a new-operator/new-record proposal. It modifies surface (the combinator §Specializations / §Consumer provenance edits + the de-link sweep) and is framed as a retroactive-consolidation refactor with the RE6 `linear_combination` precedent as evidence. No record is named in a new signature, so the record-definition sub-check no-ops. The leaf-fact audit (conjugation table, `&y==this` self-dot fast path, `std::abs` guard) confirms the substance already lives in the combinators (verified: `L2/inner_product.md:176` §Specializations + `:449` §Consumer exist and carry the folded content), so no leaf fact is stranded on deletion.

**rotation-quality — pass (not the primary axis here).** No new algebraic rotation is asserted; the refactor consolidates already-firm vocabulary and re-points edges (the "reduce four DAG nodes into the combinator" move). Consolidation/state-hiding, not a rename masquerading as a rotation. The do-NOT-merge boundary is correctly preserved (see cross-reference-integrity below): `dot` → §Specializations (codomain specialization), `nrm2` → §Consumer (NOT a member), which is exactly the partition that keeps this from being an over-unification.

**variant-axis-coverage — pass.** The conjugation × element-type × weight-presence axis is named and is folded into the surviving combinator's §Specializations (the `dot`/`tdot` table). The over-unification guard is explicitly held: `nrm2` is the `√∘abs∘inner_product` consumer (split-additivity lost under `√`), kept distinct from the fold members. No hidden branch.

**cross-reference-integrity — pass (CRITICAL CHECK, independently verified complete).** This is the load-bearing check for a 4-chapter deletion. I ran an independent inbound-link sweep across all three surfaces and confirmed the report's inventory is COMPLETE at the file level and correctly disambiguates the deletion targets:
- **Disambiguation (the trap):** `./dot.md` / `./nrm2.md` are same-directory relative links. The kept files `L1/dot.md`, `L1/nrm2.md`, `L4/dot.md`, `L4/nrm2.md`, `concepts/dot.md`, `concepts/nrm2.md` ALL exist and ALL receive `./dot.md`/`./nrm2.md` inbound links that resolve to THEMSELVES, not to a deleted file. The report correctly scopes deletion to ONLY `L2/dot`, `L2/nrm2`, `L3/dot`, `L3/nrm2`, and its re-point rules target the specific resolving paths (`](./dot.md)` only inside L2/L3 dirs; `](../L3/dot.md)`; `](../L2/dot.md)`) — it does NOT touch the L1/concepts/L4 self-links. Verified: `concepts/`, `L1/dot`, `L1/nrm2` are absent from the report's delete/edit set (correct — they survive).
- **Surface (i) body links — complete:** my per-directory resolution (same-dir `./` links in L2/ and L3/ + all explicit `../L2|L3/` paths + SUMMARY `./L2|L3/`) yields exactly the file set the report's inventory enumerates: L2/dot ← {fold-family-stubs-intro, divfree-projector, index, reciprocal, assemble-diagonal}; L2/nrm2 ← {divfree-projector, index, reciprocal, normalize, fold-family-stubs-intro}; L3/dot ← {orthogonalize, chebyshev, blas1-intro, ksp_solve, inner_product, index, orthogonalize-variant-split, L4/dot, L4/index}; L3/nrm2 ← {blas1-intro, normalize, inner_product, orthogonalize, chebyshev, ksp_solve, index, reciprocal, L4/nrm2, L4/index}. No file is missed.
- **The L4/index.md:52 / :55 mixed-link case (verified):** these lines carry BOTH a `./dot.md` (→ kept `L4/dot.md`) AND a `../L3/dot.md` (→ deleted). The report lists :52/:55 as inbound hits and its mechanical rule re-points only the `](../L3/dot.md)` substring, correctly leaving the kept-verb self-link. L4/index.md:112 (×2 `../L3/dot.md`) and :120 (×2 `../L3/nrm2.md`) confirmed.
- **Surface (iii) frontmatter typed edges — complete:** my `grep` for list-item + `target:` forms yields exactly {fold-family-stubs-intro:8,9 (reference STRIKE); blas1-intro:8,11 (reference); orthogonalize:29 (depends-on composes); normalize:7 (depends-on); L4/dot:9 (depends-on); L4/nrm2:8 (depends-on)} plus the deleted files' own self-resolving edges (L2/nrm2:10, L3/nrm2:23,25). Matches the report's table. The 4 re-pointed depends-on (L4/dot:9, L4/nrm2:8, L3/orthogonalize:29, L3/normalize:7) all land on firm `L3/inner_product`.
- **Anchors resolve:** both target headings exist verbatim — `## Specializations (the members, as notes under the combinator)` and `## Consumer (NOT an instance): nrm2 / matrix-weighted-norm` at L2:176/449 and L3:146/333; the report's slugs (`#specializations-the-members-as-notes-under-the-combinator`, `#consumer-not-an-instance-nrm2--matrix-weighted-norm` — double-hyphen from ` / ` correctly anticipated) are mdBook-correct.
- **SUMMARY.md:** all four entries present (`:107,:110,:152,:153`), report strikes all four.
- **L4 verbs / L1 leaves / concepts pages NOT deleted:** confirmed surviving (the black-box-vs-accelerated-kernels §2 kept-dual is intact; only the L2/L3 standalones go).

**edge-label-fidelity — pass.** The four re-pointed depends-on edges are all firm→firm (verified on-disk: `L3/inner_product` `## Status` = firm; `L2/inner_product` = firm; `L4/dot`/`L4/nrm2` = firm; the consumer re-pointers `L3/normalize` firm / `L3/orthogonalize` partial-obstruction both point UP to firm `L3/inner_product`). `unresolved_depends_on_targets` stays 0; rank-invariant (rank(u) ≤ rank(dep)) holds for every re-point. The L4/dot `kind: specializes` edge to `L4/inner_product` is correctly left untouched (only the `L3/dot` blocking-lift edge re-points).

**plan-kind-consistency — pass.** Declared as a combinator-miner consolidation/elimination refactor (replace-and-propagate, RE6 shape), not a new operator (no dep-map row). The content matches: deletions + §-section folds + de-link sweep. No firm-body-inside-fence concern (no new firm chapter is authored; the `edit:` blocks are surgical line replacements on existing firm chapters).

**skill-uptake-survey — pass.** The report references skill `deleted-slug-inbound-live-link-sweep` (the 3-surface sweep) and the RE6 precedent. Appropriate skill uptake for a deletion-and-re-point refactor.

### Issues found

1. **`reports/.../CYCLE.md:410 (§Supporting evidence)` — ambiguous citation basename, severity LOW.** `operator.cpp:598-617` is written as a bare basename and `citecheck --scan` flags it `[AMBIG]` (two `operator.cpp` files in the tree). The intended referent is `palace/linalg/operator.cpp:598-617`, which is in-range and correct. Fix: qualify the path to `linalg/operator.cpp:598-617` (or `palace/linalg/...`). Does not affect the refactor's correctness; flagged for path hygiene.

2. **Anchor-stability latent risk (the report's own §Open-questions caveat) — severity LOW, NOT a current defect.** ~30 inbound links re-point to the two long combinator §-heading anchor slugs. If those headings are ever reworded, the links break. The report correctly flags this as out-of-D4-scope and does not act on it; noted here so the integrator/finalize is aware the build-correctness of this refactor depends on the headings staying verbatim (verified present at L2:176/449, L3:146/333 — currently correct).

3. **NO cross-reference defect found (the critical concern cleared).** The inbound-link inventory is complete across all three surfaces; the deletion-vs-keep disambiguation (`./dot.md` in L1/concepts/L4 resolving to surviving same-dir files) is correctly handled; the do-NOT-merge boundary (dot→§Specializations, nrm2→§Consumer) is preserved; the surviving L4/L1/concepts `dot`/`nrm2` are not deleted. This is recorded as a positive finding because it was the dispatch's highest-risk surface and it passed independent verification.

### Note on overall_status
Not set — one check is `warning` (citation-validity, the AMBIG basename), so `overall_status` is left for the repairer.

---

## Repair

### Fixes attempted

- **Finding 1 — citation-validity (warning, LOW): `CYCLE.md:410` bare basename `operator.cpp:598-617` flags `[AMBIG]`.**
  - **Decision**: repaired.
  - **Action**: qualified the bare basename to the disambiguated path in CYCLE.md §Supporting evidence (line 410): `operator.cpp:598-617` → `linalg/operator.cpp:598-617`. Verified first via palace-codemap: exactly two `operator.cpp` files exist (`palace/fem/libceed/operator.cpp`, `palace/linalg/operator.cpp`); `read_range` on `palace/linalg/operator.cpp:598-617` returns the `Norml2`/`Dot` matrix-weighted-norm template (`B.Mult` → `Dot(comm, Bx, x)` → `std::sqrt`), which is precisely the firm `inner_product` evidence anchor the line cites. The repository citation convention is path-relative-to-`reference/` (the report already writes the sibling `vector.cpp` anchors as bare-but-unambiguous basenames); `linalg/operator.cpp` is sufficient to disambiguate within the `palace/` tree and matches the critic's resolution. Mechanical path-hygiene fix, squarely within repair authority (the original agent dropped the `linalg/` qualifier).

- **Finding 2 — anchor-stability latent risk + positive cross-reference finding (LOW, NOT defects).**
  - **Decision**: not-needed.
  - **Rationale**: Finding 2 is the report's own §Open-questions caveat (the ~30 anchor re-points depend on the two long combinator §-headings staying verbatim) — explicitly out of D4 scope, no edit requested, and the headings are verified present (L2:176/449, L3:146/333). Finding 3 is a positive finding (the critical cross-reference-integrity surface passed independent verification). Nothing to repair; confirmed and left.

### Unrepairable findings

None. The sole `warning` (citation-validity path hygiene) was mechanically repairable; all other checks passed at critique.

## Suggested resolution

`ready`. Note for the integrator: this is a destructive 4-chapter consolidation refactor (`L2/dot`, `L2/nrm2`, `L3/dot`, `L3/nrm2` deleted; folded into the firm `inner_product` combinator). The critic independently verified the inbound-link inventory complete across all three de-link surfaces and confirmed the kept L1/L4/concepts `dot`/`nrm2` self-links survive. The ~60 body-link re-points to the two combinator §-anchors are applied mechanically against the report's §Inbound-link inventory; the two mdBook anchor slugs were verified to resolve verbatim. D5 (WAVE-2, dep D4) reconciles the L2/index firm-count prose against the D4 row strikes — sequence D4 before D5 per the plan.
