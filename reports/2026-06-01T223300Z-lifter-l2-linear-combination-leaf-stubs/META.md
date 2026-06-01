---
verifies: ../CYCLE.md
critiqued_at: 2026-06-01T225809Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: pass
  skill-uptake-survey: pass
repaired_at: 2026-06-01T230500Z
repairer_version: 1
repairs:
  citation-validity: not-needed
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

# META: verification of "Re-anchor (reduce-to-stub) the four L2 linear_combination leaf chapters"

## Critique

### Checks run

**citation-validity — pass.** Ran `citecheck.py --scan` over the full CYCLE.md: **43 ok, 0 failing** (bounds + path-hygiene clean). Then `--anchor`-verified the load-bearing unique L0 anchors per stub against on-disk `reference/palace/palace/linalg/vector.{hpp,cpp}`: `scal` (`vector.hpp:98-99` `operator*=` decl with the exact "Scale all entries by s." comment via `--show`; `vector.cpp:207-211` `if (si == 0.0)`; `vector.hpp:262-270` `Normalize`), `axpy` (`vector.hpp:115-118`, `vector.cpp:276-311`, `:714-718`, `:720-724`), `axpby` (`vector.hpp:130-131`, `vector.cpp:732-737`, `:739-743`), `axpbypcz` (`vector.hpp:133-136`, `vector.cpp:745-758`, `:760-765`, `:767-772`) — all `[ok]`, anchors land inside their ranges. The report's own §Discipline note flagged a spurious `[DRIFT]` on `vector.cpp:207-211 --anchor 'imag'`; I confirmed independently that `:207-211` anchored on `si == 0.0` resolves cleanly, so the producer's spurious-drift call is sound. No `verified_against:` YAML block in this report (not a lowering-verifier audit), so the round-trip sub-check is N/A.

**surface-or-evidence — pass.** This is the explicit refinement-shaped case the convention permits: the proposal modifies surface (replaces each of the four L2 chapter bodies with a reduced specialization-stub) under the ratified information-non-lossy reduce-to-stub convention (`collapsed-leaf-disposition-convention-cohort-wide`, batch-15). It is not a pure rotation_claim; the surface change is the deletion of the duplicated firm body and the retention of unique anchors + variant row, with the rotation evidence deferred to the firm combinator. Allowed.

**rotation-quality — pass.** The relevant rotation (the arity-axis fold that makes `linear_combination` strictly more compact than the four fixed-arity leaves) lives in the combinator entry, not in these stubs; this dispatch is the down-stream consequence (collapsing the now-redundant leaves into specialization pointers). The reduction itself is strictly compacting (365/406/437/449-line firm bodies → thin stubs), and the L2 form is genuinely more abstract than the L1 leaves (one variadic fold vs four fixed-arity operators) per the combinator §"Arity specializations". Not a rename, not a 1:1 mapping.

**variant-axis-coverage — pass.** Each stub retains its variant-axis row with both axes covered: **element-type** (real/complex with the real⊑complex scalar-promotion sub-axis, each anchored to its per-type promotion-overload site — `scal` `vector.cpp:207-211`, `axpy` `:714-718`, `axpby` `:739-743`, `axpbypcz` `:767-772`) and **output-aliasing** recorded as the FOLD's axis (deferred to `linear_combination` §Variant axes axis 1, scoped out at L2 as an L2>L1 lowering concern). No hidden branch: the aliasing axis is explicitly attributed to the combinator and scoped out at this layer rather than dropped.

**cross-reference-integrity — warning.** All link-up targets resolve on disk: `linear_combination.md`, the four `L1/{scal,axpy,axpby,axpbypcz}.md` leaves, the three `L1-L0/*-mutation-rotation.md` themes, `concepts/scalar-promotion.md`, and the combinator-referenced `L2-L1/linear-combination-fold-specialization.md` all exist. The arity mappings written into each stub match the combinator's §"Arity specializations" block (`linear_combination.md:80-84`) verbatim. The unique-anchor non-loss check passes: each retained anchor is genuinely absent from the combinator's shared Evidence set (combinator carries `vector.hpp:305-316` free-function decls + `:203-227` parent range + the `nleps/romoperator/timeoperator/iterative` live sites; stubs carry the member decls `:98-99`/`:115-118`/`:130-131`/`:133-136` + per-type overload defs — disjoint). Zero-dangling is sound by construction (reduce-to-stub keeps all four files; the report's inbound-link enumeration is correct and no `delete:` fence is emitted). **The warning is the edit-block deletion under-specification** — see Issue 1. The fence-enclosure guard passes: 8 balanced top-level fences (4 `edit:` open + 4 close), zero indented/nested fences, each `## Status` + Signature + Variant-axes + Evidence sits INSIDE its fence — no firm-body-outside-fence defect.

**edge-label-fidelity — pass.** No L_{n+1}→L_n edge label is asserted by this dispatch (it is a within-L2 leaf-to-combinator re-anchor, not a lowering-theme authoring). The `lowers_to:` frontmatter pointers (L2→L1 identity) and the prose discussing them are consistent (each stub's `lowers_to` points at its same-named L1 leaf and the prose narrates that exact edge). N/A-leaning, marked pass.

**plan-kind-consistency — pass.** Declared shape is a reduce-to-stub refactor producing `## Status: firm` specialization-stubs; the content matches (firm specialization pointers, no rough-in placeholders, claim-deferral to the firm combinator). `firm` is the correct status per the convention (the stub is a firm specialization pointer, not a stub-tier claim-free placeholder). Consistent.

**skill-uptake-survey — pass.** The report references the relevant skills: `verify-citation-range` / `tools/citecheck` (anchor self-verification of all 16 retained anchors), `deleted-slug-inbound-live-link-sweep` (used as a verification gate, correctly noting no file is deleted), and `convert-nested-fences-to-indented-code-in-proposed-changes-block` (the 4-space-indent fence discipline). Telemetry present and appropriate to the shape.

### Issues found

**Issue 1 — edit-block `[old]` anchor captures only the head matter, not the body it intends to delete (CYCLE.md §Proposed changes, all four `edit:` blocks; severity: MEDIUM, mechanical).**
Each `[old]`/`[new]` pair anchors `[old]` on only the **frontmatter + `# <op>` heading** (e.g. scal `[old]` ends at `# scal`, report line 63), while the Summary states the block "replaces the **entire** current chapter body" and the `[new]` payload is a complete standalone chapter (frontmatter through §Evidence). If `integrator-per-report` applies this as a **literal-string `[old]`→`[new]` swap**, only the head matter is replaced and the old duplicated firm body (e.g. `scal.md:17-365`) survives below the new stub — producing a frontmatter-swapped-but-double-bodied chapter, NOT a stub. The reduction is only correct if the integrator treats each block as a **full-file replace** (where `[new]` is the entire new file content). The `[new]` blocks ARE self-contained complete chapters, so full-file-replace is well-defined and is clearly the intent; the defect is that the mechanical block does not encode the deletion of the trailing body, leaving the application mode dependent on integrator interpretation. Candidate repair: extend each `[old]` to span the full current chapter body (frontmatter through end-of-file), or add an explicit `full-file-replace` annotation / META-SIGNAL instructing the integrator to overwrite the whole file with `[new]` rather than anchor-swap. (Confirmed the `[old]` head matter matches current `scal.md:1-16` verbatim, so an anchor swap would succeed mechanically — which is exactly why a silent partial-replace is the risk, not a hard failure.)

**Issue 2 — stale bare-code-span pinpoints into the deleted scal body (LOW; out of this dispatch's four-file scope; already self-flagged).**
`book/src/L2/normalize.md:11,:111,:141,:164` carry bare code-span references `book/src/L2/scal.md:223-228` pointing at the former scal §Dependencies "Sibling subsumption" note that the reduction deletes. The report correctly classifies these as stale-but-not-build-breaking (bare code-spans, not `](...)` links; linkcheck2 does not check prose code-spans) and correctly scopes them out (normalize.md is D4's narrative-reconcile territory, not D1's four-file scope). Not a defect in this report — recorded so the integrator/D4 can pick up the bounded re-anchor. No action required of this dispatch.

**Issue 3 — `fold_parent:` → `specialization_of:` frontmatter-key rename is a cross-dispatch coordination point (LOW; already self-flagged).**
The four stubs replace the `fold_parent:` frontmatter key with `specialization_of:`. The report flags (Open questions) that if D4's `index.md` dep-map narrative keys off the old `fold_parent` field name, that is a coordination point. This is correctly surfaced, not resolved (index.md is D4's count-owner scope and was correctly left untouched — confirmed via `git status`: no working-tree mutation of `L2/index.md` or the four stub files in the dispatch phase). Flagged for integration-ordering awareness; not a defect in this report.

---

## Repair

### Fixes attempted

- **Finding (Issue 1, cross-reference-integrity, MEDIUM):** the 4 `edit:` blocks for `L2/{scal,axpy,axpby,axpbypcz}.md` anchored `[old]` on ONLY the frontmatter + `# <op>` heading while the INTENT was full-chapter-body replacement; a literal anchor-swap would leave the old duplicated firm body (e.g. `scal.md:17-365`) surviving below the new stub → a double-bodied/corrupted chapter.
  - **Decision:** repaired.
  - **Action:** Converted all four `edit:` blocks to the **full-file-overwrite encoding** (CYCLE.md §Proposed changes, lines 49 / 135 / 218 / 304). Removed the `[old]: …` head-matter span, the `# <op>` line, and the `[new]:` marker from each block so the block body now begins directly at `---` frontmatter and is the **complete new file content** (frontmatter through §Evidence). Per `.claude/agents/integrator-per-report.md` step 3, an `edit:<path>` block carrying full-file content (no anchor markers) is applied via `Edit` full-replace when the target exists — which removes the old body in full. Also updated the §Proposed-changes preamble and the §Discipline fence-enclosure bullet to state the full-file-overwrite encoding (so the prose matches the blocks).
  - **Verification:** (a) zero `[old]:`/`[new]:` markers remain; each block's first content line is `---`. (b) Fence parity holds: exactly 8 top-level triple-backtick fences (4 `edit:` open + 4 close), zero nested fences — the `[new]` bodies were already 4-space-indented code (no nested ```` ``` ````), so the full-file conversion introduced no fence mis-toggle and required no `convert-nested-fences…` rewrite. (c) Each block closes after its §Evidence content (verified close-fence positions at lines 133/216/302/396, bodies intact). (d) `citecheck.py --scan` re-run: **43 ok, 0 failing** — unchanged from the critic's run (the head-only marker removal touches no citation). (e) On-disk frontmatter of all four files matches the removed `[old]` head verbatim, confirming the full-file body is the intended successor, not a partial.

- **Finding (Issue 2, stale `normalize.md` bare code-spans → `scal.md:223-228`, LOW):** out of D1's four-file scope; `normalize.md` is D4's narrative-reconcile territory; bare code-spans are not `](…)` links so linkcheck2 does not flag them (not build-breaking).
  - **Decision:** not-needed (out of scope; correctly deferred to D4's micro-sweep by the producer).

- **Finding (Issue 3, `fold_parent:` → `specialization_of:` frontmatter-key rename, LOW):** cross-dispatch coordination point if D4's `index.md` dep-map keys off the old field name.
  - **Decision:** not-needed (out of scope; correctly surfaced for D4 coordination by the producer; index.md left untouched in the dispatch phase).

### Unrepairable findings

None. The single MEDIUM finding was a mechanical encoding defect (anchor-swap vs full-file-replace) and was repaired surgically; the two LOW findings are correctly out of D1's scope and require no repair here.

## Suggested resolution

`ready`. Notes for the integrator:
- The four `L2/{scal,axpy,axpby,axpbypcz}.md` blocks are now **full-file-overwrites** — apply each via `Edit` full-replace (target files exist on disk); do NOT anchor-swap. Each block body is the complete successor chapter.
- Integration ordering: this report renames the `fold_parent:` frontmatter key to `specialization_of:` in the four files. D4 (the `L2/index.md` count-owner) reconciles the consolidated dep-map narrative; if D4's index narrative keys off the old `fold_parent` name, sequence accordingly.
- The stale `normalize.md:11/:111/:141/:164` bare code-spans pointing at the deleted `scal.md:223-228` body are a bounded D4 micro-sweep follow-up (non-build-breaking).
