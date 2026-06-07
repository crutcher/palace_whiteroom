---
verifies: ../CYCLE.md
critiqued_at: 2026-06-06T234500Z
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
repaired_at: 2026-06-06T235500Z
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

# META: verification of CYCLE — L1>L0 theme `build-mesh-construction-rotation`

## Critique

### Checks run

**citation-validity — pass.** `citecheck --scan` reports 34 ok / 2 failing, but BOTH failures are non-citations: `palace/fem/geodata.cpp:421-450` and `main.cpp:287-302` appear only inside the report's own "Supporting evidence" / "Open questions" sections where the report *quotes the prompt's wrong path/overshoot to self-correct them* — they are not emitted artifact citations. Every load-bearing EMITTED citation was verified on disk: `palace/main.cpp:285-302` (level-vector decl `:285`, scope `:286`/`:301`, four-stage chain `:287-291`, wrap loop `:297-300`, `make_unique<Mesh>(std::move(m))` `:299` — all exact); `palace/utils/geodata.hpp:25-50` (`Load` doc+decl `:25-31`, `Partition` `:33-36`, `RefineMesh` contract `:45-50` — exact); `palace/utils/geodata.cpp:421-455` RefineMesh body (`:424-425` MFEM_VERIFY, `:426` uniform_ref_levels, `:429` reserve, `:448` loop, `:452` emplace_back, `:454` UniformRefinement — all exact, and the brace-boundary END-line the planner flagged is correct: the loop's closing `}` is at `:455`, so `:421-455` legitimately encloses the full mutation, no off-by-one); `palace/utils/geodata.cpp:262-290` Partition (`:271-276` distribution branch, `:276` Mpi::Broadcast — exact); `palace/fem/mesh.hpp:76-81` ctor (`:77` adopt, `:79` EnsureNodes, `:80` Update — exact) and `:44-115` wrapper (`:44` class, `:49` mesh handle, `:51-59` attr maps, `:84-96` read surface — exact). The two prompt-errata the planner pre-flagged (path `palace/fem/`→`palace/utils/geodata.cpp`; `main.cpp` range overshoot to blank `:302`) are correctly self-corrected in the emitted citations. No drift in any emitted pinpoint.

**surface-or-evidence — pass.** This is a refinement-shaped proposal (a new firm L1>L0 theme + coupled re-anchor of an existing L1 chapter) AND it modifies surface with positively-anchored evidence: the theme authors the lowering narrative against the cited L0 RHS, and the coupled edit upgrades `build_mesh.md`'s edge. Per the FEATURE-SURFACE adaptation this is NOT a feature-surface chapter — it is a standard per-edge lowering theme, so the un-adapted check applies and is satisfied. Record-definition sub-check: the theme's signature names the `Mesh` record; the report does NOT define it in-chapter but cross-references its existing definition home `../L1/build_mesh.md#record-definition`, which exists on disk (the `## Record definition` heading is present in build_mesh.md). A lowering theme referencing (not introducing) a record whose definition home already exists is correct — no missing definition home. The pending `concepts/mesh.md` migration (D6) is correctly flagged in Open questions, not silently assumed.

**rotation-quality — pass.** The lowering is a genuine vocabulary translation, not a degenerate identity-in-named-terms rename. The L1 form is a referentially-transparent `config → Mesh` value-pipeline (immutable typed value, no handles); the L0 form is an imperative free-function chain threading three successive `unique_ptr` handle types via `std::move` ownership transfer, with `RefineMesh` growing the level-vector in place and the adopting ctor running construction-time side-effects. The three named translation pieces (P1 value-pipeline → handle-ownership threading; P2 return-a-sequence → in-place mutable-reference growth; P3 typed-value construction → ctor-with-finalization-side-effects) each name a real semantic-organization shift, not a 1:1 term map. The vocabulary genuinely shifts (value-threading → C++ memory discipline), satisfying the redirect's translation-not-rename discipline.

**variant-axis-coverage — pass.** The orthogonal axes are handled explicitly: the refinement-depth axis is covered (zero-refinement identity vs k-level monotone stack, P2, tied to c117 laws 3/4); the region-vs-uniform refinement split is named (region in `Load`, uniform in `RefineMesh`, `:423` comment); and the MPI/`Par*` partition/distribute axis is flagged-once-and-skipped per §Scope (single-rank = identity distribution), with the `mesh::Partition` distribution-path branch (`:271-276`) explicitly read single-rank. The `use_mesh_partitioner` partitioner-vs-broadcast policy is correctly scoped out as multi-rank machinery. No hidden branches — the single-machine carve-outs are enumerated as "the only" ones.

**cross-reference-integrity — warning.** All `[link]` targets resolve on disk: `../L1/build_mesh.md` (+ `#record-definition` anchor → present `## Record definition` heading), `L1-L0/fe-space-construction-rotation`, `L1-L0/essential-dofs-construction-rotation`, `L1/fe_space`, `feature/lifecycle.L1`, `L1-L0/index.md`, `construction-rotation-intro.md` all exist; the `Mesh` record reference correctly points at the current in-chapter home rather than a guessed (nonexistent) `concepts/mesh.md` link; `lifecycle.L1.md:44` confirms the cited build_mesh constituent. The coupled re-anchor edge and graded-stack frontmatter are internally consistent. The WARNING is on two coupled-edit fidelity issues that will bite at integration: (1) the **SUMMARY.md edit** lists only `build-mesh` + `essential-dofs`, but the live SUMMARY has FIVE construction-rotation children (essential-dofs `:266`, fe-collection `:267`, fe-operator-assemble `:268`, fe-space `:269`, weak-form-term `:270`) — the alpha-first placement of `build-mesh` (b < e) is correct, but the edit's surrounding-context snippet does not reflect the actual neighbor lines, so a literal apply could mis-anchor; (2) the **index.md edit** is described as replacing "the header row + the immediately-following essential-dofs row", which is accurate (essential-dofs IS the first construction-rotation row at `:63`), and the alpha-first insertion is correct — this one is fine, but is coupled to the same alpha-neighbor assumption. These are edit-application/anchor concerns, not broken references.

**edge-label-fidelity — pass.** The edge type `depends-on (kind: lowers-to)` from `L1/build_mesh` → `L1-L0/build-mesh-construction-rotation` is the correct direction (L1 source lowers-to its L1>L0 theme) and the prose discusses exactly that edge. Graded-stack rank/well-foundedness holds: build_mesh is firm (rank 3), the theme is firm (rank 3 = min(endpoints), with the L0 endpoint rank-terminal ground truth), so `rank(u) ≤ rank(v)` is satisfied for the new `lowers-to` edge (3 ≤ 3) and the upgrade is now legal (previously the chapter correctly withheld the edge because the lower endpoint did not yet exist). The theme's own `depends-on` edges are `lowers-to` (to the firm L1 endpoint, rank 3) + `cites-evidence` (to rank-terminal L0), all rank-consistent. The `reference` edges to sibling themes constrain nothing. No edge-label/prose mismatch.

**plan-kind-consistency — pass.** Declared kind is an L1>L0 lowering theme of an already-firm L1 operator; the content shape matches — LHS L1 form, RHS L0 form, per-piece translation narrative, Applicability/Scope/Justification/Evidence sections, no speculative L_{n+1} operators (correctly "None"). Status `firm` (firm-on-positive-structure) is justified: every translation piece is a syntactic identity on positive source with no convergence/iteration semantics to test-gate, and the no-dedicated-mesh-construction-test caveat is correctly cited as non-gating per the `fe_space`/`fe_collection`/`essential_dofs` precedent. The MFEM-owned-read-as-given kernel boundary is a witnessed library-ownership posture, not a constructive sub-part, so `firm` (not `partly-constructive`) is the right tier.

**skill-uptake-survey — pass.** The report's shape (a lowering theme with heavy L0 citation) implies citation-verification tooling; the report references `tools/citecheck/citecheck.py` + on-disk `read_range` self-verification (Supporting evidence). Pure presence check — telemetry only, non-blocking.

### Issues found

1. **`book/src/SUMMARY.md` edit — incomplete neighbor context (cross-reference-integrity, low/medium severity).** CYCLE.md:377-381. The proposed SUMMARY edit shows the construction-rotation group as `build-mesh` followed only by `essential-dofs`, but the live SUMMARY (`book/src/SUMMARY.md:265-270`) has five children: essential-dofs (`:266`), fe-collection (`:267`), fe-operator-assemble (`:268`), fe-space (`:269`), weak-form-term (`:270`). The alpha-first placement of `build-mesh` (before essential-dofs) is correct, but the edit block omits the three other existing entries, so a literal application risks mis-anchoring or dropping siblings. Integrator should insert the single `build-mesh` line in alpha position ahead of `:266` and leave the other four untouched.

2. **Redundant / ambiguous first build_mesh.md edit block (plan-kind / edit-fidelity, low severity).** CYCLE.md:309-318. The first `edit:book/src/L1/build_mesh.md` block shows only the unchanged `reference:` block + `---` with a parenthetical saying it "add the `lowers-to` depends-on edge" — but the actual lowers-to insertion is fully specified by the SECOND edit block (CYCLE.md:320-334, the complete frontmatter with the new edge). The first block is a no-op-shaped framing fragment that does not itself carry the change and could confuse a literal applier. The substantive edit (block 2) is correct and unambiguous; this is a presentation redundancy in the proposed-changes, not a content error.

3. **Downward-note + schema-comment staleness edits are correct but order-coupled (informational, no severity).** CYCLE.md:339-365 correctly identify and rewrite the now-stale "named, NOT authored this cycle" / "No `lowers-to` edge is asserted yet" claims at `build_mesh.md:11-12`, `:180-186`. Verified the old-text matches the live chapter exactly (`:11-12` comment, `:178-186` Downward block). No defect — recorded so the integrator applies all three build_mesh.md edits (frontmatter edge + schema-comment + Downward prose) together to avoid leaving a half-stale chapter.

### Note on the two citecheck "failures"

For the repairer/integrator: the `citecheck --scan` MISS (`palace/fem/geodata.cpp:421-450`) and AMBIG (`main.cpp:287-302`) are both deliberate quotations of the prompt's errata inside the report's self-correction prose (Supporting evidence / Open questions), NOT emitted artifact citations. The emitted citations use the corrected `palace/utils/geodata.cpp` path and the `:285-302` / `:286-301` / `:287-291` ranges, all on-disk-verified. No citation repair is needed; these scan hits are expected artifacts of the report documenting its own corrections.

## Repair

### Fixes attempted

- **Finding (issue 1):** `book/src/SUMMARY.md` edit — incomplete neighbor context. The proposed `edit:` block showed the construction-rotation group as `build-mesh` + `essential-dofs` only, but the live SUMMARY (`book/src/SUMMARY.md:265-270`) has FIVE children (`essential-dofs`/`fe-collection`/`fe-operator-assemble`/`fe-space`/`weak-form-term`). A literal apply risked mis-anchoring or dropping the three unrepresented siblings.
  - **Decision:** repaired.
  - **Action:** Rewrote the SUMMARY proposed-changes block (CYCLE.md `edit:book/src/SUMMARY.md`) into an unambiguous old-text→`becomes` INSERT anchored on the real neighbors — the `Construction-rotation themes` group header + the first existing child line (`essential-dofs`, live `:265-266`). The `build-mesh` line is inserted alpha-first (b < e) immediately after the group header / before `essential-dofs`; the four other sibling lines are explicitly left untouched. Anchor verified against the live `book/src/SUMMARY.md:265-270`.

- **Finding (issue 2):** Redundant / no-op-shaped first `build_mesh.md` edit block (CYCLE.md:309-318) — a framing fragment showing only the unchanged `reference:` block + `---`, whose actual change is fully specified by the second (complete) frontmatter block.
  - **Decision:** repaired.
  - **Action:** Removed the no-op-shaped first `edit:book/src/L1/build_mesh.md` block; replaced its parenthetical with a one-line note pointing the integrator at the single complete frontmatter `edit:` block (block 2, the `rank: firm` … frontmatter that inserts the `lowers-to` `depends-on` edge). No substantive content changed — the load-bearing edit (block 2) was already correct and is left verbatim.

- **Finding (issue 3):** The three coupled `build_mesh.md` staleness edits (frontmatter `lowers-to` edge insert + schema-comment rewrite + Downward-prose rewrite) must form one coherent diff applied together.
  - **Decision:** not-needed (verify-only).
  - **Action:** Verified all three edits' old-text against the live `book/src/L1/build_mesh.md`: frontmatter `depends-on`/`reference` block (live `:14-22`), schema-comment (live `:10-12`), Downward block (live `:178-186`) — each matches exactly. The three together coherently flip the chapter from "named-not-authored / no `lowers-to` edge yet" to "`lowers-to` edge asserted (c118)". No edit required; recorded so the integrator applies all three together.

### Unrepairable findings

None. The two repairable findings (issues 1, 2) were both proposed-changes-block anchor/presentation fixes within repair authority; issue 3 was verify-only. The critic's `cross-reference-integrity: warning` was driven entirely by the SUMMARY anchor concern (issue 1) plus the index.md alpha-neighbor coupling (which the critic itself found correct) — both now resolved/confirmed at the proposed-changes level. No substantive authoring was required.

## Suggested resolution

`ready`. All eight critic checks are `pass` except `cross-reference-integrity` (`warning`), whose underlying anchor concerns are now mechanically resolved in the CYCLE.md proposed-changes (SUMMARY insert re-anchored against the 5 live siblings; the redundant first edit-block removed). Notes for the integrator:
- Apply the SUMMARY edit as an INSERT-only of the single `build-mesh-construction-rotation` child line, alpha-first ahead of `essential-dofs` at live `:266`; do not disturb the other four construction-rotation siblings.
- Apply all three `build_mesh.md` edits (frontmatter edge insert + schema-comment + Downward prose) together — they form one coherent staleness-clearing diff verified against the live chapter.
- The two `citecheck --scan` hits are documented prompt-errata quotations in the report's own prose, NOT emitted citations (per the critic's note) — no action.
- Open-question follow-ons the report already flagged (the `concepts/mesh.md` D6 `#record-definition` re-anchor; the prompt path/range errata) are informational; promote per the standard Open-questions path.
