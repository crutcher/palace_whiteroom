---
verifies: ../REPORT.md
critiqued_at: 2026-06-07T210000Z
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
repaired_at: 2026-06-07T211500Z
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

# META: verification of "L4 roadmap_goal sketch — sharding-decompose-reduce"

## Critique

### Checks run

**citation-validity — pass.** Every Palace L0 citation was re-verified on-disk this dispatch with `citecheck --anchor`: `geodata.cpp:262` (`Partition`), `:3230-3242` (`GetMeshPartitioning`), `:3239` (`GeneratePartitioning`), `rap.hpp:24` (`ParOperator`), `rap.cpp:116-126` (`RAP`) — all `ok`, anchors in-range. The firm-law book cross-references were read on-disk and each supports its claim precisely: `inner_product.md:154-157` is the split-additivity/shape-concatenation monoid-homomorphism law verbatim; `linear_combination.md:146-151` is the concatenation-homomorphism law verbatim; `gram_reduce.md:119-120` is the per-pair list-homomorphism; `domain_energy_reduce.md:21-27` is the domain-RESTRICTED reduce model, `:147-152` the map-independence/concatenation-homomorphism fold law, `:172-178` the config-conditional partition-of-unity NON-law the chapter's non-law section follows. The MPI-boundary paths (`rap.{hpp,cpp}`, `geodata.cpp`) are cited as deferred-MECHANISM ONLY, explicitly NOT lifted — DIRECTIVE-1 honored. The `verified_against:` YAML block round-trips under `yaml.safe_load` (no leading-quote scalar collision; every `note:` value opens with prose). The new chapter's own frontmatter YAML also round-trips.

**surface-or-evidence — pass.** A `roadmap_goal` (rank-0) chapter makes no claims, so this check largely no-ops (analogous to the `stub` tier). The chapter nonetheless carries its evidence basis (firm-law citations + the c133 gate-CLEAR provenance), which is appropriate for a claim-free future-direction sketch. Record-definition sub-check: the speculative signatures name shape-group types (`Tensor[(S: ...)]`, `IndexBlock`, `Partition`) but these are the calculus's standing notation, not newly-introduced record types needing a definition home; `subdomain_reduce`/`restrict_to_block` are combinators, not records. No undefined-record gap.

**rotation-quality — pass (not applicable to roadmap_goal kind).** A rank-0 future-direction sketch asserts no rotation; the chapter explicitly frames `subdomain_reduce = reduce ∘ restrict-to-block` as a DERIVED consumer of standing firm homomorphism laws ("no new reduction algebra"), not as a new L_{n+1}→L_n rotation. No rotation claim to grade.

**variant-axis-coverage — pass.** The chapter explicitly scopes its variant surface: the partition-of-unity / disjoint-and-exhaustive coverage condition is carried as a config-conditional NON-law (mirroring `domain_energy_reduce`'s coverage non-law), and the cross-block-state / interface-coupling axis is explicitly assigned to the deferred mechanism, not asserted. The reduce-vs-solve-vs-assemble generalization is explicitly marked speculative-intent (only the reduction case carries the firm law today). No hidden branches.

**cross-reference-integrity — warning.** All five `reference:` edge targets resolve on-disk (`L4/domain_energy_reduce.md`, `L4/inner_product.md`, `L4/linear_combination.md`, `L4/gram_reduce.md`, `L2/gram.md`), and every in-prose `[link]` resolves. HARD TRIPWIRE (the load-bearing constraint): VERIFIED — the new chapter's frontmatter `edges:` has a single key, `reference:`, with NO `depends-on:` key; all five firm roots sit under `reference:` only. A rank-0→rank-3 `depends-on` would have manufactured a `rank(u) ≤ min(deps)` violation; none is present. The `warning` is for the SUMMARY alpha-position only — see Issue 1 below. (Build-readiness fence guard: the chapter is `roadmap_goal`, not `firm`; the firm-body-inside-fence guard is N/A, but I confirmed the full chapter body — banner, Status, Evidence, `verified_against` YAML — sits INSIDE the `new:` fence with balanced even parity (8 fence markers = 4 pairs), so no fence-truncation defect.)

**edge-label-fidelity — pass.** No L_{n+1}→L_n directional edge label is carried; the chapter is a within-L4 roadmap_goal. The `reference:` edges are navigational (and correctly so — an edge to firm roots from a rank-0 node is `reference`-class, free). N/A directional-edge prose mismatch.

**plan-kind-consistency — pass.** The declared kind (`rank: roadmap_goal`, `status: roadmap_goal`) matches the content shape throughout: the banner declares it claim-free; the Status, Speculative-semantics, and Speculative-algebraic-laws sections are all explicitly framed as intended-target-shape-NOT-asserted; intent + pulled_by provenance + declared deps + accreting working context are all present (the rank-0 chapter requirements per the graded-stack spec). No firmness over-claim. Rank-invariant: trivially satisfied — a rank-0 node may rest on anything, and here it rests on nothing via `depends-on` (only `reference`). Reachability: the chapter records its pulled-by chain (human batch-43 (C) directive + c133 gate-CLEAR) and notes its reference edges reach firm reduce roots reachable from the feature-spine output-product columns; provenance is wired.

**skill-uptake-survey — pass.** The report references `citecheck --anchor` invocation for its L0 citations (the expected skill for citation verification). The roadmap_goal-chapter shape has no other strongly-implied skill. Telemetry only.

### Issues found

1. **SUMMARY alpha-position is off — `sharding-decompose-reduce` is inserted AFTER `sparameter_reduce`, but alphabetically belongs BEFORE it.** Location: `CYCLE.md` Proposed changes, the `edit:book/src/SUMMARY.md` block (CYCLE.md:358-362), and the Open-questions note (CYCLE.md:400-402). The block places the new row between `sparameter_reduce` and `waveguide_mode_reduce`. But `sharding` vs `sparameter` diverge at the second character: `h` (0x68) < `p` (0x70), so `sharding-decompose-reduce` sorts BEFORE `sparameter_reduce`. The correct alpha position within the "Data-algebra combinators & named verbs" group (current group runs `...nrm2`, `sparameter_reduce`, `waveguide_mode_reduce` at SUMMARY.md:81-83) is immediately BEFORE `sparameter_reduce` (i.e. after `nrm2`/`mk_matrix_free_operator`). Severity: low — group choice (data-algebra reduce-family) is correct; only the intra-group ordinal is wrong. This violates the alpha-within-kind-group convention and is a mechanical fix to the `edit:` block's anchor lines.

### Notes (non-issues, recorded for the integrator)

- The chapter adds NO L4 `index.md` dep-map row (correct per the report's own reasoning — the dep-map is the firm/rough-in vocabulary table; a rank-0 roadmap_goal is wired via SUMMARY + frontmatter edges). The report flags this for layer-intro-author confirmation; not a defect.
- The author's-judgment bifurcation escape (split `restrict_to_block` / `subdomain_reduce` into two chapters) was considered and declined with a stated rationale; appropriate for a rank-0 sketch.

## Repair

### Fixes attempted

- **Finding**: SUMMARY alpha-position is off — `sharding-decompose-reduce` inserted AFTER `sparameter_reduce` but `sh` < `sp` so it belongs immediately BEFORE `sparameter_reduce` (intra-group ordinal wrong; group choice correct).
  - **Decision**: repaired
  - **Action**: Rewrote the `edit:book/src/SUMMARY.md` proposed-changes block in CYCLE.md (CYCLE.md §Proposed changes) so the integrator anchors the insertion between `nrm2` and `sparameter_reduce` (the correct alpha slot within the "Data-algebra combinators & named verbs" group). The block now reads anchor `nrm2` → new `sharding-decompose-reduce` → anchor `sparameter_reduce`, matching the live SUMMARY.md:81-82 ordering. Also updated the consistency note in CYCLE.md §Open questions / caveats to describe the corrected position ("between `nrm2` and `sparameter_reduce`, `sharding` < `sparameter`"). Purely mechanical: corrects the insertion ordinal; no content/claim change, the chapter body is untouched.

### Unrepairable findings

None. The single warning was a mechanical alpha-ordinal fix; all eight critic checks otherwise passed and the load-bearing hard tripwire (firm roots under `reference:` only, no `depends-on` from the rank-0 node) was honored.

## Suggested resolution

`ready`. Notes for the integrator:
- The `edit:book/src/SUMMARY.md` block now anchors on `nrm2` (SUMMARY.md:81) and `sparameter_reduce` (SUMMARY.md:82); insert `sharding-decompose-reduce` between them — verified against the current SUMMARY.md ordering this repair.
- Re-confirm `rank_violations=0` via the graded-stack rank linter after applying (the critic verified the frontmatter has `reference:`-only edges with no `depends-on:` key; this is the one constraint both c133 probe arms turned on).
- No L4 `index.md` dep-map row is added (correct — rank-0 roadmap_goal wired via SUMMARY + frontmatter edges); the report flags this for layer-intro-author confirmation, not a defect.
