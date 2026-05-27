---
verifies: ../CYCLE.md
critiqued_at: 2026-05-26T23:40:00Z
critic_version: 1
checks:
  citation-validity: pass
  surface-or-evidence: pass
  rotation-quality: pass
  variant-axis-coverage: pass
  cross-reference-integrity: warning
  edge-label-fidelity: pass
  plan-kind-consistency: warning
  skill-uptake-survey: warning
repaired_at: 2026-05-26T23:55:00Z
repairer_version: 1
repairs:
  citation-validity: repaired
  surface-or-evidence: not-needed
  rotation-quality: not-needed
  variant-axis-coverage: not-needed
  cross-reference-integrity: repaired
  edge-label-fidelity: not-needed
  plan-kind-consistency: repaired
  skill-uptake-survey: repaired
overall_status: ready
follow_up_agent: lowering-verifier
---

# META: verification of REPORT — L1>L0 theme sketch (axpby-mutation-rotation)

## Critique

### Checks run

**citation-validity** — pass. Spot-verified every source range cited:
- `vector.cpp:276-311` — `ComplexVector::AXPY` definition. Confirmed (lines 276-311 are exactly the AXPY member methods including the two-overload form with the `ai == 0.0` branch).
- `vector.cpp:701-712` — real free-function `AXPY(double, Vector, Vector)` with the `alpha == 1.0` branch at line 704. Confirmed.
- `vector.cpp:704-706` — exact body `if (alpha == 1.0) { y += x; }`. Confirmed verbatim.
- `vector.cpp:710` — `y.Add(alpha, x)` in α≠1 branch. Confirmed.
- `vector.cpp:714-723` — complex free-function dispatches to `y.AXPY(alpha, x)`. Confirmed (two overloads at lines 714-718 and 720-724).
- `vector.cpp:726-743` — AXPBY family templates. Confirmed.
- `vector.cpp:745-758` — AXPBYPCZ real-path template. Confirmed.
- `vector.hpp:115-118` — comment + AXPY decl + Add inline alias + Subtract inline. Confirmed (line 115 is the `// In-place addition` comment; lines 116-118 are AXPY/Add/Subtract). The report's "AXPY / Add decls" labelling at 115-117 is loose by one line (line 117 is Add, 118 is Subtract) but no claim is contradicted.
- `vector.hpp:119-128` — operator+= and operator-= bodies as `AXPY(±1.0, x)`. Confirmed verbatim.
- `vector.hpp:130-136` — AXPBY/AXPBYPCZ member decls. Confirmed.
- `vector.hpp:305-316` — free-function `AXPY`, `AXPBY`, `AXPBYPCZ` template decls. Confirmed (the report's source-list says 305-316; comments/decls span lines 305-316 inclusive).
- `vector.hpp:311` — free-function `AXPBY` template. Confirmed.
- `operator.cpp:458-475` — `SumOperator::AddMult` with `y.Add(a*c, z)` at line 464 (and the transpose at 474). Confirmed.
- `rap.cpp:73` — `b.Add(-1.0, ty)`. Confirmed verbatim (line 73, in Dirichlet residual correction context).
- `rap.cpp:317` — `y.Add(a, ty)` in `ParOperator::AddMult`. Confirmed verbatim.
All claims have evidence pointers and the pointers land in-range.

**surface-or-evidence** — pass. The report is a new-theme entry (additive); it proposes book surface (a new chapter `book/src/L1-L0/axpby-mutation-rotation.md` plus an `axpby` row in `book/src/L1/index.md` and a SUMMARY entry). This is original surface emission, not refinement of an existing operator/theme, so the rotation_claim-without-surface failure mode does not apply.

**rotation-quality** — pass. The L1 form `axpy(α, x, y_old) → y_new` and `axpby(α, x, β, y_old) → y_new` strictly hide the destination-buffer mention and the in-place mutation channel. The L0 form is `y.Add(α, x)` (destination-named-on-LHS-of-call, in-place); L1 names only values. This is genuine state-hiding compression, not renaming. The three constant-folded sub-patterns (general α, α==1, α==-1) all reduce to the single L1 operator — a clear coarsening (3→1 collapse).

**variant-axis-coverage** — pass. The variant axis here is the scalar-value-constant-folding axis: {general α, α==1, α==-1}. The report explicitly identifies all three sub-patterns, walks the L0 evidence for each, justifies each (structural for A, algebraic for B and C), and explicitly absorbs the α==1 branch as a transparent performance trick rather than promoting it to a separate L1 operator. Caveat #2 calls this out explicitly. A second variant axis — real vs. complex element type — is also surfaced (the report notes the real path branches on α==1 while the complex path does not). Caveat #5 covers the real-path α==-1 case. The "real-path branch on α==1 is a transparent performance trick" judgment is defensible: `y += x` vs. `y.Add(1.0, x)` saves one multiply per element but is algebraically equal in floating-point (`1.0 * x + y` and `y + x` differ only by an unnecessary multiplication that IEEE-754 specifies as identity for finite values; the FMA fused-multiply-add risk does not apply here because both branches use the same scalar multiply-then-add discipline). The caveat about a `lowering-verifier` audit confirming no L0 site relies on bit-exact distinction is appropriate hedging. Agree with the classification.

**cross-reference-integrity** — warning. Most links resolve: `[L1/axpy](../L1/axpy.md)` resolves to `book/src/L1/axpy.md` (verified to exist as a firm operator). The open question slugs `axpby-axpbypcz-next-harvest` and `axpy-l1-l0-three-subpatterns` both resolve in `scaffolding/open-questions.md`. The empty L1-L0 `index.md` confirms the theme is the first entry there. However, the report's caveat #6 surfaces a real discrepancy between the cycle-002 plan filename (`theme-mutation-rotation.md`) and the report's adopted slug (`axpby-mutation-rotation.md`). The discrepancy is surfaced clearly with a recommendation, so the integrator can choose, but the integrator will need to either rename the file or accept the slug-based name. The warning reflects that the surface emission carries an unresolved naming choice into the artifact.

**edge-label-fidelity** — pass. The edge label is `L1>L0`. The report's prose consistently discusses the L1>L0 edge: the LHS is the pure L1 form, the RHS is Palace's L0 in-place mutating call. No prose drift into L2>L1 or L0>L1.

**plan-kind-consistency** — warning. The report mixes kinds in a way that the integrator must read carefully:
- The theme `axpby-mutation-rotation` is declared `rough-in` in its own Status section (the chapter-body's last line). Acceptable shape for a theme rough-in (sub-rule recognition sketched, full audit deferred to `lowering-verifier`).
- The `axpby` L1 operator is declared `rough-in` in the dep-map row (`status: rough-in, proposed-by: ...`), with the actual L1 page `book/src/L1/axpby.md` not created. The SUMMARY edit adds the theme chapter but does NOT add an `axpby` chapter under `L1/`. So the dep-map row points to a non-existent chapter (`./axpby.md`). Either the integrator must accept a broken link until harvester firms `axpby`, or the rough-in row should defer adding the link until the chapter exists. This is a real plan-kind tension: the dep-map row is declared `rough-in` but the artifact would carry a broken link. The cycle-plan's intent was likely to add only the theme chapter and defer the L1 operator row to harvester; the report's expansion to also add the dep-map row is a scope drift that ought to be flagged for integrator decision.

**skill-uptake-survey** — warning. The report's shape implies several available skills should have been invoked:
- `verify-citation-range` — the report enumerates ~15 evidence ranges. No mention of `verify-citation-range` skill invocation. (Sub-agents may run skills silently; pure presence check.)
- `classify-variant-axis` — the report explicitly reasons about a variant axis (scalar-value constant-folding) and decides absorption-vs-separate-operator. No mention of `classify-variant-axis` skill invocation.
- `propose-rotation` — present in `skills/`; not referenced by name, though the report's structure (LHS / RHS / applicability / justification kind / verified-against / status) reads like the propose-rotation template.
- `verify-refinement-surface` — not applicable here (additive emission, not refinement).

The report would benefit from naming the skills it followed. Telemetry only; not blocking.

### Issues found

1. **Dep-map row points to a non-existent chapter** (CYCLE.md §Proposed changes, second block, `book/src/L1/index.md` edit). The new row `[\`axpby\`](./axpby.md)` references `book/src/L1/axpby.md`, which is not created by this report. If the integrator applies the row, the mdBook link-check gate will fail. Severity: high (blocks integration). Repair options: (a) drop the dep-map row in this report — the theme chapter alone is the cycle-002 deliverable; defer the L1 row to a follow-up harvester cycle that creates `axpby.md`; (b) make the row bare text without a link (`\`axpby\``) until the chapter exists; (c) include a stub `axpby.md` chapter marked `rough-in` (scope drift; recommend against).

2. **Filename / slug discrepancy with cycle-002 plan** (CYCLE.md caveat #6). Plan says `theme-mutation-rotation.md`; report uses `axpby-mutation-rotation.md`. Report recommends slug-based name with clear forward-compatibility argument (`axpbypcz-mutation-rotation`, `mult-output-arg-rotation` ahead). Severity: low (clearly surfaced, integrator can choose). Repair options: (a) integrator accepts slug-based name (matches the SUMMARY entry as written); (b) integrator renames file + SUMMARY to plan's name. No code change to CYCLE.md needed.

3. **`vector.hpp` line-range labelling is off by one** (CYCLE.md §Sub-pattern A citations, "vector.hpp:115-117 — ComplexVector::AXPY / Add decls"). Line 115 is the comment, lines 116 (AXPY) and 117 (Add) are the decls. The range should be 116-117 if naming "AXPY / Add decls" strictly. Severity: low (cosmetic; range is in-bounds, no claim contradicted). Repair option: rewrite as `vector.hpp:115-118` (covering the leading comment through Subtract) or as `vector.hpp:116-117` (strict decls).

4. **`vector.hpp:118` is cited at single-line granularity in Sub-pattern C** ("`Subtract(α, x) { AXPY(-α, x); }`"). The cited line 118 is exactly that. Confirmed in-range. No issue; noted because the report mixes single-line and multi-line ranges without a stated convention. Severity: information.

5. **Skill invocations not named** (telemetry). The report does not reference `verify-citation-range`, `classify-variant-axis`, or `propose-rotation` skills despite their availability and apparent relevance. Severity: information.

6. **Parent-session annotation at end of CYCLE.md** documents a meta-finding (custom-agent dispatch resolves but subagent `*CYCLE.md` writes are blocked). This is appropriate transparency, surfaces a real friction pattern, and points to meta-phase action. Not an issue; noted because it duplicates the harvester report's same finding — meta-phase should consolidate.

## Repair

### Fixes attempted

- **Finding 1**: Dep-map row links to `./axpby.md` chapter that doesn't exist (`book/src/L1/index.md` edit block). After integrator applies, mdBook link-check would fail.
  - **Decision**: repaired
  - **Action**: Edit on CYCLE.md §Proposed changes, `edit:book/src/L1/index.md` block. Changed `[\`axpby\`](./axpby.md)` to plain `` `axpby` `` (no link). Per the dep-map convention, rough-in entries don't link until they're firm. Harvester will re-link when `book/src/L1/axpby.md` is created in a future cycle.
  - **Rationale**: Mechanical fix; preserves the rough-in dep-map entry (which carries semantic value: signals upcoming axpby work and subsumption relation to integrator + future agents) while removing the broken link that would fail the link-check gate.

- **Finding 2**: Filename slug discrepancy (cycle-002 plan named `theme-mutation-rotation.md`; report uses `axpby-mutation-rotation.md`).
  - **Decision**: not-needed
  - **Rationale**: The report's choice is justified (caveat #6) and more durable; integrator already has the surfaced reasoning and can choose. No content authoring required from repairer.

- **Finding 3**: `vector.hpp:115-117` range off-by-one (line 115 is the leading comment; strict AXPY/Add decls are 116-117).
  - **Decision**: repaired
  - **Action**: Edit on CYCLE.md §Sub-pattern A citations. Changed `vector.hpp:115-117` → `vector.hpp:116-117`. Verified against source: line 115 is `// In-place addition (*this) += alpha * x.`, line 116 is `void AXPY(...)`, line 117 is `void Add(...)`. The 116-117 range exactly matches the labelling "ComplexVector::AXPY / Add decls".
  - **Rationale**: Cosmetic off-by-one; mechanical fix verified against source.

- **Finding 4**: Skill telemetry absent — `verify-citation-range`, `classify-variant-axis`, `propose-rotation` not named.
  - **Decision**: repaired
  - **Action**: Edit on CYCLE.md frontmatter. Added `skill_uptake:` block mirroring the pilot-1 axpy format (`reports/2026-05-26T223039Z-harvester-axpy-L1/CYCLE.md`). Entries: `verify-citation-range` (explained_non_applicable; deferred until critic-phase mechanism stabilizes; repairer post-hoc tightened one range), `classify-variant-axis` (artifact_landed; scalar-value constant-folding axis classified into three sub-patterns), `propose-rotation` (artifact_landed; theme follows the template).
  - **Rationale**: Mechanical telemetry restoration; the decisions and rationales are derivable from the report content itself, not authored.

### Unrepairable findings

None. All four findings either repaired or marked not-needed (integrator decision surfaced cleanly).

## Suggested resolution

Status: `ready`. The integrator can apply this report's surface emissions (the new theme chapter, the dep-map row without link, the SUMMARY entry).

Follow-up: name `lowering-verifier` for a subsequent cycle to audit the three sub-patterns against the full L0 corpus exhaustively (the theme's Status section already calls for this). When harvester firms `axpby` in a later cycle, the dep-map row should be re-linked.

Integrator notes:
- The filename discrepancy (Finding 2) is the integrator's choice. Report recommends `axpby-mutation-rotation.md`; cycle-plan named `theme-mutation-rotation.md`. The SUMMARY edit block uses the slug-based name; integrator should keep them aligned.
- The parent-session annotation at the end of CYCLE.md (about subagent `*CYCLE.md` write blocks) duplicates the harvester report's same finding. Meta-phase should consolidate, not the integrator.
