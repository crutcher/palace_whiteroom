---
verifies: ../REPORT.md
critiqued_at: 2026-06-01T053000Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: pass
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-01T053500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of "Formalize scal at L2" (cycle-041 D3, L2 floor entry)

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` reports 8/8 in-bounds with clean path hygiene. Anchor-checked all load-bearing L0 pinpoints: `vector.hpp:98-99` (anchor `operator*=` at :99, comment `Scale all entries by s.` at :98) `[ok]`; `vector.hpp:262-270` (`Normalize` at :262,:264) `[ok]`; `vector.cpp:203-227` (`operator*=` at :203) `[ok]`; `vector.cpp:207-211` (anchor `si == 0.0` at :207) `[ok]`; `vector.cpp:212-225` (anchor `forall_switch` at :218) `[ok]`; `book/src/L2/index.md:17` (`scal` in the base-primitive vocabulary) `[ok]`. I read `vector.cpp:203-227` directly via codemap: line 207 is `if (si == 0.0)`, 209-210 the two-real-call branch (`Real() *= sr; Imag() *= sr;`), 211 the closing brace, 212-225 the general complex `forall_switch` kernel computing `XR[i] = sr·XR[i] − si·XI[i]; XI[i] = si·XR[i] + sr·XI[i]` — exactly as the report describes (§Semantics line 169, §Evidence line 382, §Variant-axes line 291). NOTE on a citecheck false-positive: an exploratory `--anchor 'imag'` on `:207-211` reported `[DRIFT -1]` pointing at line 206; this is NOT a defect — `imag()` (the `s.imag()` extraction at line 206) is not what the report cites at :207-211. The report cites the `if (si == 0.0)` *branch* (line 207), and `--anchor 'si == 0.0'` resolves it cleanly within range. The drift is an artifact of probing with the wrong token, not producer citation drift; the original `:207-211` is correct. No `verified_against:` block in this report, so the YAML round-trip sub-check is not applicable.

**surface-or-evidence — pass.** This is a `new:` operator entry (`book/src/L2/scal.md`) plus a dep-map row + SUMMARY registration — new-surface authoring, not a refinement of an existing operator/theme. The surface/rotation_claim-pairing rule is for refinement-shaped proposals; this floor-backfill authors fresh L2 surface backed by inherited-and-re-verified L0 evidence. Applicable shape satisfied.

**rotation-quality — pass (with the correct reading of an identity-floor).** The report does NOT assert a compacting algebraic/structural rotation — it explicitly claims `scal` L2 ↔ L1 is **identity-in-form** (value-thread-isomorphic; signature textually identical), authored as an identity-lowering floor entry per the methodology invariant "Identity-lowerings still require both L levels." An identity-floor is not subject to the "must be strictly more compact" bar (that bar gates *claimed* rotations; an honest identity claim is a different shape). The report does not dress the identity up as a rotation — it states the no-fusion-to-unfold reason (single scalar-vector multiply, leaf primitive) and routes the one fusion note (degenerate arity-1 single-aligned pass) to the `linear_combination` fold's fusion note. Correctly framed; no renaming-masquerading-as-rotation.

**variant-axis-coverage — pass.** Two variant axes declared (element-type real/complex; scalar-promotion real-α-against-complex-x sub-axis), both covered with L0 anchors (separate `operator*=` overloads; the `si == 0.0` value-based promotion branch at `vector.cpp:207-211`). The report explicitly states no other axes (§Variant-axes line 297: "unconditionally pure, element-local, reduction-free, rank-local across all variants") and explicitly contrasts the *absence* of a scalar-value constant-folding branch (unlike `axpy`'s `α == 1.0` path) — distinguishing the complex-scalar-*shape* branch from a scalar-*value* branch. Axis count is asserted to match L1 and L3 exactly (two axes). No hidden branches.

**cross-reference-integrity — pass.** All referenced artifact files exist on disk (`L1/scal.md`, `L1-L0/scal-mutation-rotation.md`, `L3/scal.md`, `L2/linear_combination.md`, `L2/index.md`, `L3/normalize.md`, `concepts/scal.md`, `concepts/scalar-promotion.md`, `decisions/axpby-as-primitive.md`, `L1/axpby.md`, `L2/inner_product.md`); the sole "missing" target is `book/src/L2/scal.md`, which is the `new:` file this report creates (correct). Cross-reference pinpoints verified: `linear_combination.md` line 68 is exactly `scal(α, x) = linear_combination [(α, x)]`; law 6 is "Specialization identities (derived)" carrying that same identity — the report's framing ("derived identity, not a decomposition") matches the source's own `(derived)` label. The fold-cohort boundary exists at `L2/index.md` §22-26 and §75 (load-bearing do-NOT-merge, exactly as cited). The L2/index `edit:` anchor row (the `linear_combination` row) matches line 52 verbatim. The forthcoming `L2-L1/scal-fusion` / `L3-L2/scal` themes are correctly forward-referenced in **plain text** (not live links), per `rough-in-forward-reference-must-be-plain-text-not-live-link`. **Fence-parity build-readiness guard:** 8 fences, even parity; the `new:book/src/L2/scal.md` block (lines 40–406) ENCLOSES the full firm apparatus — Signature (113), Semantics (138), Algebraic laws (172), Status (308), Evidence (348) all sit inside the fence. The flagged inner ```` ```text ```` signature fence opens at 115 and closes at 118, fully nested and balanced inside the `new:` block — NOT the cycle-019 fence-truncation defect. The two `edit:` blocks (index 408–411, SUMMARY 420–424) are balanced.

**edge-label-fidelity — pass.** The report's directional claims are internally consistent: §"Lowers to" narrates L2→L1 (identity-in-form), §"Lifts from" narrates L1→L2 (value-thread-isomorphic), high→low direction preserved throughout. The `lowers_to` / `lifts_from` frontmatter both point at `L1/scal.md` with the matching characterizations. No mismatched edge label.

**plan-kind-consistency — pass.** Declared kind is `firm` (identity-in-form floor; firm-on-positive-structure). Content shape matches: complete Signature + Semantics + nine Algebraic laws + Status + Evidence + Variant-axes, no rough-in placeholders, no `TODO`/`?` gaps. The firm justification is sound and correctly invokes the syntactic-identity-laws-on-positive-source escape (the `apply_linop` situation): the `operator*=` L0 surface is small, fully present, and positively cited, every law is a syntactic identity on that closure, so the absence of a dedicated `scal` unit test does not gate firm. This is the documented escape, applied correctly. The high→low discipline holds — the L2 entry is defined in L2 (fusion-rotation) vocabulary (leaf base primitive + fold-membership), not in terms of L1/L0 primitives; the L2>L1 lowering work is routed to the (forthcoming) D6 theme, not authored into the L2 body.

**skill-uptake-survey — pass.** The report references its citecheck `--anchor` self-verification (§Supporting evidence, "L0 anchors — self-verified ... citecheck `--anchor`") and names `upgrade-plain-text-ref-to-live-link-when-target-on-disk` as the future-pass skill for the forward-referenced themes. Skill-uptake is surfaced; presence check satisfied.

### Issues found

No defects found. All eight checks pass. Notes for downstream (none blocking):

1. **`fold_parent` frontmatter field is new — flag for layer-intro-author / meta-phase consistency (NOT a defect).** The report introduces a `fold_parent:` frontmatter field on `book/src/L2/scal.md` recording the `linear_combination` arity-1 membership in machine-readable form. I confirmed L1 `scal` and L3 `scal` frontmatter carry no such field (frontmatter there is `layer`/`operator`/`firmness`/`lowers_to`/`lifts_from`/`variant_axes` only). The report self-discloses this in §Open-questions/caveats (CYCLE.md:512–518) and flags it as a low-stakes convention choice that can be dropped without affecting the body. This is a frontmatter-convention question for the layer-intro-author / meta-phase to ratify (adopt fold_parent across the fold cohort, or keep membership prose-only) — surfaced here per the task directive, carried as a convention signal, not a repairable defect.

2. **Count-ownership discipline observed correctly (confirming-note, no issue).** The dispatch touches only its own `book/src/L2/scal.md` chapter, its own L2/index dep-map *row* (inserted after the `linear_combination` anchor row), and the SUMMARY registration. It explicitly does NOT touch the L2/index consolidated firm-count tally (§"Vocabulary cohort" / §"Working Notes") — correctly deferring that to D7 per the count-ownership partition (CYCLE.md:413–418, 484–491). The fold-cohort do-NOT-merge boundary is respected: `linear_combination` is cited as fold-parent and the arity-1 membership is recorded as a *derived identity* (law 4 / fold-specialization identity), NOT as a decomposition — the leaf stays standalone and firm, matching the load-bearing boundary at `L2/index.md` §75.

3. **citecheck `imag`-anchor false-positive (documentary, for the record).** As noted under citation-validity: probing `vector.cpp:207-211` with `--anchor 'imag'` yields `[DRIFT -1]` → line 206, but this is the wrong token to probe — the report cites the `si == 0.0` branch (line 207), which `--anchor 'si == 0.0'` resolves in-range. No drift in the report; recorded so the repairer does not chase a phantom off-by-one.

---

## Repair

### Fixes attempted

The critic returned all eight checks `pass` with **no defects found**. There are no flagged warning/fail findings to repair. The three downstream notes are explicitly characterized by the critic as non-defects; each is recorded below as informational-no-defect, with the repair decision and the reason no edit is applied.

- **Finding (note 1)**: `fold_parent` frontmatter field is new on `book/src/L2/scal.md` (L1/L3 `scal` carry no such field).
  - **Decision**: not-needed (informational; no defect).
  - **Rationale**: This is a frontmatter-convention question the critic surfaced for the **layer-intro-author / meta-phase** to ratify (adopt `fold_parent` across the fold cohort, or keep membership prose-only). It is a methodology-level convention choice, not a mechanical defect — out of repair authority ("Methodology-level concerns the critic flagged for meta-phase attention"). The report self-discloses the field in its §Open-questions/caveats and notes it can be dropped without affecting the body, so it is non-blocking. Carried forward as a convention signal for the meta-phase; no edit applied.

- **Finding (note 2)**: Count-ownership discipline observed (confirming-note).
  - **Decision**: not-needed (confirming-note; no defect).
  - **Rationale**: The critic confirmed the dispatch touches only its own chapter, its own L2/index dep-map row, and the SUMMARY registration, correctly deferring the consolidated firm-count tally to D7 per the count-ownership partition. Nothing to repair.

- **Finding (note 3)**: citecheck `imag`-anchor false-positive (`vector.cpp:207-211` → spurious `[DRIFT -1]` at :206 when probed with `--anchor 'imag'`).
  - **Decision**: not-needed (anti-repair flag; the cited range is CORRECT).
  - **Rationale**: The cited `vector.cpp:207-211` pinpoints the `if (si == 0.0)` branch body; `--anchor 'si == 0.0'` resolves it cleanly in-range. The `[DRIFT -1]` is an artifact of probing with the wrong token (`imag()` at :206), not producer citation drift. **No regression applied** — pinning this citation to :206 would be a defect, not a fix. Left exactly as authored.

### Unrepairable findings

None. No finding requires deferral to a follow-up agent.

## Suggested resolution

`ready`. All eight checks pass with zero defects; the three downstream notes are informational and non-blocking. Integrator notes:
- Apply the report as-authored. Do **not** regress the `vector.cpp:207-211` citation toward :206 — that range is correct (the `si == 0.0` branch body).
- The `fold_parent:` frontmatter field is a convention signal carried for the **meta-phase** to ratify (adopt across the fold cohort vs. keep membership prose-only); it is not a defect and does not gate integration.
