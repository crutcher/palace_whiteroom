# Methodology — the graded resolution ladder + feature-root reachability (2026-06-04)

**Status:** user directive, 2026-06-04. Peer artifact to `METHODOLOGY-REDIRECT.md` (2026-06-01) and `MIGRATION.md` (2026-05-26). This document is the *full spec*; `CLAUDE.md` §Methodology invariants carries the operational distillation and the supersession pointers; `book/src/methodology/` carries the reader-facing (non-authoritative) mirror.

**What it does:** gives the artifact **two orthogonal, mechanically-checkable axes** that together define artifact health, and — as a consequence — **finalizes the Phase-1 corpus depopulation** by lowering the floor of the maturity ladder so that *intent* has an in-discipline home and never again has to be parked in a frozen slice.

---

## 0. The two problems this fixes

**0a — The Phase-1 corpus never finished depopulating.** The slice-reduction policy said *lift → reduce → delete*, with the layered/concept artifact becoming authoritative. But the incremental + conciseness discipline resists thin entries: when a layer abstracts a slice's detail away (e.g. `L2/krylov-step` deliberately erases the per-method primitive sequence that `arnoldi_step`'s §L2 still holds), the leftover detail has no clean home. The system's only expressible options were (a) bloat the firm entry with pre-abstraction detail it is trying to erase, (b) drop the detail, or (c) park it in the slice as "unique material." It chose (c) every time, and the `annotated-and-retained` carve-out blessed it. The slices became a **frozen second source of truth, not beholden to combinator-refactoring or fusion** — a brake on the very freedom the vocabulary-shift redirect grants the layers. The root cause: the cheapest materializable tier was `stub`, which still implies a *sketch/claim*, so **intent had no legal, in-discipline, claim-free place to land** — and slices absorbed it.

**0b — "Well-founded" and "justified" were enforced by hand.** "A reduction is as firm as its least-firm folded primitive" (gram_reduce, domain_energy_reduce) and "is this artifact still referenced by anything live?" (the periodic detritus eyeball-pass) were both real invariants the project obeyed manually. They should be mechanical.

---

## 1. Axis 1 — the graded resolution ladder + the well-foundedness invariant

**1a — The ladder is a total order with a rank.** Assign a resolution rank:

```
roadmap_goal = 0   <   stub = 1   <   rough-in = 2   <   firm = 3
```

(`partly-constructive` and `rough-in (test-coverage-bounded)` are **sub-ranks pinned just under firm** — rank 2.5; `firm` cannot rest on them. See §1f.)

**1b — The well-foundedness invariant.** For every **dependency** edge `u → v` (`u` is well-founded on `v`):

> `rank(u) ≤ rank(v)` — equivalently, `rank(u) ≤ min over deps(u) of rank(v)`.
>
> **An entry is at most as resolved as its least-resolved dependency.**

Consequences (the user's statement of the rule):
- `firm (3)` ⇒ every dependency is `firm`.
- `rough-in (2)` ⇒ dependencies ≥ `rough-in`.
- `stub (1)` ⇒ dependencies ≥ `stub`.
- `roadmap_goal (0)` ⇒ dependencies unconstrained — **roadmap_goals stack on roadmap_goals, stubs, rough-ins, and firms.**

This subsumes "a reduction is as firm as its least-firm folded primitive" (the `k=3` case) and the feature-column OWN-COMPOSITION promotion rule (§2c). It is **orthogonal to, and compatible with, "layers are defined high→low"**: *definition* flows down (a layer is written in its own/higher vocabulary); *well-foundedness/maturity* flows up (you cannot be firm until your supports are). Two duals.

**1c — The promotion rule (the invariant, read forward).** An entry is promotable to rank *k* only once **all** its dependencies are ≥ *k*. Promotion propagates **upward** through the dependency DAG; the **frontier is the rank-discontinuity surface** where the resolved region meets the unbuilt region. (The matrix-weighted-norm → gram_reduce/domain_energy_reduce → columns cascade of cycles 088–091 was exactly a wave of rank propagating upward under this constraint.)

**1d — `roadmap_goal` is a real book chapter (rank 0).** It is **not** an off-book roadmap node — it is a materialized chapter, so links to it resolve natively (no shortcode, no linkcheck change) and it is the **authoritative location that accretes the entry's working context in place** as the entry climbs the ladder. A `roadmap_goal` chapter carries:
- `status: roadmap_goal` frontmatter (rank 0);
- the **intent** — the L_n operator / theme / concept it will become;
- **pulled-by** provenance — the ≥1 real inbound *blocking* consumer that justifies it (the proliferation guard, §2b; this is also its reachability requirement, §2);
- the **declared dependencies** it will be well-founded on (which may themselves be roadmap_goals) — the linter reads these;
- the **accreting working context** — the speculative sketch, gathered citations, the gap observation, prior cross-cutter/abstractor notes;
- **no claims** — anything asserted is explicitly flagged speculative; no firm laws, no citations-as-truth.

A `roadmap_goal` chapter is the **in-discipline replacement for the `annotated-and-retained` slice**: the same role (a home for intent + working context), but on the ladder, governed by the invariant, refactorable, so it actually climbs instead of freezing.

**1e — The `stub` vs `roadmap_goal` line.** Both are claim-free chapters, so the distinction is not "file vs no-file." Two things separate them, both falling out of the invariant:
- **What the referent is.** A `stub` stands for a referent that is *real but undissected* — implied by ≥2 converging references or actual Palace structure. A `roadmap_goal` stands for an *intended* entry whose referent may itself be speculative (the abstractor's "speculative L_{n+1} operators that don't need to exist yet").
- **What it may rest on.** `stub` ⇒ deps ≥ stub (grounded in at-least-placeholders). `roadmap_goal` ⇒ deps unconstrained (intent may rest on intent).

The `roadmap_goal → stub` promotion **is** the invariant firing: "all my supports are now at least materialized, and my referent is confirmed real." Adjacent rungs, intentionally similar in content; the load-bearing difference is what is allowed to rest on them, and therefore what downstream claims can transitively rest on them.

**1f — Obstruction is a separate axis; qualifiers are sub-ranks.** `obstruction` / `partial-obstruction` are **not** low-resolution — a *firm* obstruction is a well-founded negative result (exhaustively cited). So the total order is over **constructive resolution**, and `obstruction` is a *kind* that is itself rankable. `partly-constructive` and `rough-in (test-coverage-bounded)` are sub-ranks pinned just under firm (rank 2.5; `firm` cannot rest on them). Keeping these on the correct axis is what keeps the clean total order clean. (The existing first-class-transient-gate semantics of `partly-constructive` / `rough-in (test-coverage-bounded)` are unchanged.)

**1g — Well-foundedness CAPS a composition-root at its least-resolved blocking dep; the firm-on-positive-structure escape is orthogonal (batch-39 meta-phase clarification, 2026-06-07; resolves OQ `krylov-iteration-rough-in-vs-firm-over-partial-obstruction-iteration-views`).** Two distinct gates were briefly conflated. **The well-foundedness invariant (§1b) is the rank CAP:** a composition-root whose blocking `depends-on` constituents include a `partial-obstruction` (rank ≈2.5) node is **capped at ≈2.5 → rough-in** by `rank(u) ≤ min(deps)` — it CANNOT be `firm` while a blocking dep is below firm, period. The **firm-on-positive-structure escape** (CLAUDE.md §Methodology-invariants `rough-in (test-coverage-bounded)`) is a SEPARATE, orthogonal mechanism: it lets an entry whose *laws* are syntactic identities on fully-specified positive source skip the *test-coverage* gate — it escapes a **law-confidence** demotion, NOT the well-foundedness cap. The two precedents make the line concrete: the **GMG column** promoted firm because ALL its blocking `depends-on` constituents are *firm* (well-foundedness satisfied; firm-on-positive-structure then cleared the residual test-coverage question); the **krylov-iteration column** correctly landed *rough-in* because its blocking deps `fold_solve`/`orthogonalize` are `partial-obstruction` (well-foundedness caps it — no escape applies, because the cap is not a test-coverage question). **Rule:** firm-on-positive-structure can promote rough-in→firm ONLY when well-foundedness already permits firm (all blocking deps ≥ firm); over a partial-obstruction blocking dep there is no firm to escape to. (A composition-root may still narrate its positive composition structure as firm-in-prose; its *node rank* is the well-foundedness-capped value.)

---

## 2. Axis 2 — the feature root-set + reachability / liveness

**2a — The feature surfaces are the root set (think: garbage collector).** The FEATURE-SURFACE SPINE columns (the 5 drivers, the lifecycle spine-ROOT, the output products, wave-port/boundary-mode) are the **roots** — the entry points for motivated users and applications, the things people come to the artifact *for*. **Reachability from the roots over `depends-on` edges defines liveness.** A node on no root-to-leaf path is **garbage** — unjustified, however firm. `seed` is the **root-set marker**: it does **not** collapse into the resolution ladder (a root's own composition-maturity is a separate property it carries; its root-role is permanent and categorical — the `seed→firm` flips of cycles 085/091 were maturity events on nodes whose root-role never changed).

**2b — Reachability is justification.** A vocabulary node exists *because* some feature surface transitively depends on it. This **principled-izes** two things previously hand-waved:
- The detritus / orphan hunt **is a mark-sweep from the root set** — "is this read/referenced by anything live?" ≡ "is this reachable from a root?" Orphaned artifacts (frozen slices, kickoff-dead scaffolding, dead `priorities.md` active-heads) are unreachable nodes.
- The `roadmap_goal` **proliferation guard** ("≥1 real inbound pull") *is* the reachability requirement: a roadmap_goal is justified only if its pull-chain terminates at a feature root. No path to a root ⇒ speculation-noise ⇒ GC'd. **Orphaned-intent GC and detritus GC are the same sweep**, over built and intended nodes uniformly.

**2c — The OWN-COMPOSITION rule falls out of the root marker.** A feature column's edges to *vocabulary* are blocking `depends-on` (constrain its maturity); its edges to *sibling roots* are non-blocking `reference` (roots are independently live and must not gate each other's rank). So the OWN-COMPOSITION promotion rule (a column promotes on its own firm constituents; sibling columns are references not blockers) is **derived from "is the target a root?"**, not a special edge type.

**2d — Boundary of the graph.** The root set is the feature surfaces **only**. Methodology / process pages (`book/src/methodology/`, `book/src/design/`, `concepts/` *meta* pages about the construction) sit **outside** the subject DAG — they document the construction, they are not nodes in it. Negative-result / obstruction nodes **are** on live paths (a driver→assemble→solver path that hits "and here Palace forwards opaquely") — which is precisely why the negative-result slices are load-bearing and must migrate to reachable homes rather than be dropped.

**2e — Fan-out is reachability weight.** The existing fan-out impact model (`|concepts| × |downstream-reuse| × 1/cost`) is approximately the count of root-to-leaf paths through a node. High-fan-out vocabulary is vocabulary many roots depend on. The planner's "dispatch highest-fan-out first" is unchanged; it is now understood as "promote the most-reachable frontier nodes first."

**2f — When the GC sweep surfaces an unreachable node: GROUND, don't remove, a genuine future/absorbed dependency (user directive 2026-06-05; thrice-applied cycles 107/108).** A node the reachability GC marks garbage is *not* automatically detritus to delete. Before removing or filing it as detritus, **examine whether it is a genuine future or absorbed dependency of a reachable goal node** — i.e. a node the live spine really does (or will) depend on, whose only defect is a *missing or un-typed `depends-on` edge*, not a missing justification. If so, **GROUND it**: sketch the honestly-typed `depends-on` edge into the reachable goal node (or type the missing `edges:` on the intervening pre-scheme chapter) so liveness propagates down the real chain. The disposition is a strict **priority order**, NOT a free choice:
- **(1) GROUND** — the preferred disposition. The node is a real (current/future/absorbed) dependency of a reachable node; type the **faithful, honestly-classified `depends-on` edge** (citation-grounded, critic-verifiable) into the reachable chain so the node is rescued by genuine liveness. This is what rescued the BC-elimination + divfree clusters (c107: `fe_assemble →absorbed-post-composition→ eliminate_bc`; `eigenmode.L4 →constrains-eigvec→ divfree-projector`) and the L1/L0 lowering homes (c108: typing the missing `edges:` down the BC + divfree lowering chains). **Forbidden as a grounding edge:** a *false* edge that misclassifies the relationship (e.g. forcing `column →depends-on→ internal-op` when the op is an absorbed post-composition, or `eliminate_bc →depends-on→ L1-op` when the real relationship is a *lowering* not a *constituent-use*). Grounding is **faithful-edge-or-finding**, never force-an-edge-to-flip-a-number.
- **(2) ROUTE as a genuine-detritus finding** — only when **no plausible goal-dependency exists** (the node serves no reachable consumer and names no future intent the spine will pull). Then it is real garbage; route it as a detritus finding.
- **(3) DELETE / baseline-exception** — the last resort. Deletion (frozen slices, kickoff-dead scaffolding) or a tracked baseline-exception (a known-firm-but-absorbed node that genuinely cannot yet carry a faithful edge, enumerated with a promotion condition per §5) applies only after (1) is ruled out as unfaithful.

The grounding disposition is the reachability-axis analogue of `roadmap_goal` on the resolution axis: both are in-discipline ways to keep a genuinely-wanted-but-not-yet-wired node legally in the artifact rather than dropping it. The role that owns the typed-edge campaign (`layer-intro-author`) carries this disposition; the reachability-GC reviewer (`cross-layer-cross-cutter`, the meta-phase GC sweep) applies it before filing any node as detritus.

**2g — DELIBERATE-reference-only-reachable structural nodes are the Axis-2 baseline-exception pattern, NOT decay-detritus (batch-39 meta-phase adjudication, 2026-06-07; resolves the c122/c123 REFERENCE-EDGE-LIVENESS scheme question).** Three structural models the project adopted *after* the §3 "reference does not carry liveness" rule was written deliberately produce firm/roadmap_goal nodes that reach a root ONLY via `reference`-class edges: (i) the **combinator-primary** model (the leaf is a specialization-note of its reachable combinator; the typed edge runs leaf→combinator `depends-on`, combinator→leaf is `reference` — RE6/RE7); (ii) the **DIRECTIVE-3 kernel-API/impl** dual-surface (the `kernel-impl` node is linked to its `kernel-api` surface by a `realizes-kernel-api` `reference`-class edge — the impl is *forbidden* to `depends-on` the opaque API, which would mis-type the correspondence as a build-dependency and falsely block); (iii) feature-root→node `reference` under OWN-COMPOSITION (§2c). **The §3 rule is correct and UNCHANGED** — its load-bearing purpose is "a mere mention must not keep DEAD vocabulary alive," and that still holds: these nodes are not dead, they are firm-and-faithful-but-correctly-off-the-`depends-on`-spine, exactly as RE1–RE10's absorbed-below-the-spine nodes are. **The diagnostic is the contrast** (c123-D2): when a node is genuinely *composed*, the consumer carries a `depends-on` edge and the node FLIPS reachable on the real spine (the krylov-iteration column → `krylov-step`/`fold_solve`/`orthogonalize` discharge); a node whose only inbound edge is *deliberately* `reference` (realizes-kernel-api, combinator-primary, root-sibling) stays off the `depends-on` spine BY DESIGN. **Disposition:** such nodes are ratified as a **reachability baseline-exception cohort** (RE11, the deliberate-reference-only-reachable kind — `scaffolding/graded-stack-baseline-exceptions.md`), with the standard promotion condition (a future *faithful `depends-on` consumer* names the node as a constituent, OR the combinator-primary leaf is demoted to an in-chapter `## … specializations` note removing it as a standalone DAG node). This is a *reporting/classification* refinement, NOT a gate-behavior change — `reference` still constrains nothing and carries no liveness; the GC still marks these `[GARBAGE*]`; they are simply *tracked* as baseline-exception rather than read as decay. A `detritus` climb that is fully accounted-for by NEW deliberate-reference-only-reachable firm nodes (each matched to RE11 or a new RE) does **not** trip the "STRONGER climbs without a ratified RE" escalate-guard. (An optional linter reporting tier separating `reference-reachable` from `true-detritus` is an `ask`-class `tools/` change, surfaced to the human — it would make the headline `detritus` number a cleaner health signal but changes no gate.)

---

## 3. The shared substrate — typed dependency edges

Both analyses run over **one** dependency graph whose edges are typed:

- **`depends-on`** — blocking. Well-foundedness (constrains rank, §1b) **and** liveness (carries reachability, §2). This is the bit both linters consume.
- **`reference`** — navigational "see-also". Constrains nothing; does **not** carry liveness (a mere mention must not keep dead vocabulary alive).
- **Optional `kind:`** annotation on a `depends-on` edge (`folds` / `lowers-to` / `uses-record` / `cites-evidence` / …) — **documentation only; the linters ignore it.** Promote a `kind` to a real typed distinction later *only if* an analysis ever needs it.

"Constrains rank" ≡ "carries liveness" ≡ "is a `depends-on` edge." The minimal binary is sufficient because the analyses consume only the blocking bit, and the feature OWN-COMPOSITION subtlety is handled by the orthogonal root marker (§2c), not a finer edge type.

Dep-maps (the per-chapter dependency sections + the `concepts/dependency-map.md`) are where edges are declared; they must mark each edge `depends-on` or `reference` (default `depends-on` is wrong — classify deliberately; an edge to a *root* is `reference`).

---

## 4. The two linters (one typed graph)

- **Rank linter** — graph walk; asserts `rank(u) ≤ min over depends-on deps of rank(v)` for every node. Reports rank violations (e.g. a `firm` entry resting on a `rough-in` dep) and emits the **promotion frontier** (nodes all of whose deps are ≥ their target rank) for free.
- **Reachability GC** — mark from the feature roots over `depends-on` edges; unmarked nodes are garbage. Reports detritus, unjustified vocabulary, and dead intent (roadmap_goals whose pull-chain no longer reaches a root).

Both live under `tools/` (purpose-built evaluation tooling). Artifact health = *every node reachable from a root* **and** *the rank invariant holds*.

---

## 5. Adoption — audit-first, hard-gate-new, bounded-baseline-exceptions

The edge-typing pass is **whole-artifact and mandatory** (it gates the audit), so keep the scheme minimal (§3) to make that unavoidable pass cheap. The typing pass *is* where violations surface (classifying an edge as blocking forces the "this firm thing rests on a rough-in thing" realization), so **edge-typing and the audit are one combined campaign**, not sequential decisions.

Adoption protocol:
1. **Type the edges** artifact-wide (minimal binary; an edge to a root is `reference`).
2. **Run both linters as the audit.** The reachability GC pass is the first detritus-collection pass — a deliverable you want regardless.
3. **Triage violations.** Small/quick rank violations: fix before flipping the switch. Genuinely-large remediations: enumerate as an **explicit, tracked baseline-exception set with promotion conditions** (the same first-class-transient-gate pattern as `partly-constructive`) — **not** open-ended fix-forward.
4. **Adopt the invariant as a HARD gate for all new work immediately** — no new violations admitted — while the bounded baseline burns down. A known-violated invariant is not an invariant; the gate keeps its teeth by admitting no *new* red.

---

## 6. Migration completion criterion (the Phase-1 corpus)

The slice deletions are *done* when, after them:
1. the **reachability GC** shows the `book/src/spec/slices/*` nodes **unreachable** (garbage), and every load-bearing claim is reachable via a **non-slice** path; and
2. the **rank invariant holds** with zero slice nodes in the DAG.

Per the slice audit (2026-06-04), the disposition is: **exactly one genuine gap** — `L4/preconditioning-framework.md` (the `(op, pc_op)` capability-typed binding surface; firm-on-first-authoring, so it goes straight to `firm`, *not* a roadmap_goal). Everything else is *absorb worked-example content into the concept/theme home (citing L0 directly), repoint citations off slice line-anchors, migrate pending-lift OQs, delete.* Genuinely-not-yet-describable intended homes that the migration surfaces (e.g. the un-authored `orthogonalize-mutation-rotation` L1>L0 theme) become **`roadmap_goal` chapters** resting on their firm supports — the disciplined replacement for the retained slice. The `annotated-and-retained` carve-out and the slice-reduction-audit skill are **retired** on completion.

---

## 7. What this supersedes or revises

| Artifact | Disposition |
|---|---|
| `CLAUDE.md` "Integration may materialize implied components as stubs" — "**`stub`** is the thinnest maturity tier" | **Revised.** `roadmap_goal` is now the thinnest tier; `stub` is rank 1. The stub bar (≥2 converging references) and stub mechanics are unchanged; the new `roadmap_goal` tier (§1d/1e) sits below it. |
| `CLAUDE.md` "Phase 1 corpus reduces as material is lifted" + the `annotated-and-retained` carve-out + skill `phase-1-slice-reduction-audit` | **Superseded on migration completion.** The corpus is *finalized and deleted*, not indefinitely reduced; the carve-out (which made permanent retention the standard landing state) and the audit skill are retired (§6). |
| The "as firm as its least-firm folded primitive" rule (lived practice; gram_reduce / domain_energy_reduce) | **Subsumed** as the `k=3` case of the rank invariant (§1b). |
| The feature-column OWN-COMPOSITION promotion rule (`project_feature_column_promotion_rule`) | **Subsumed / re-derived** from the root marker + edge typing (§2c). The rule is unchanged; it is now mechanical. |
| The periodic detritus / orphan eyeball-pass | **Mechanized** as the reachability GC (§2b, §4). The meta-phase's GC sweep covers detritus + orphaned-intent uniformly. |
| `roadmap.md` fan-out impact model | **Re-grounded** (§2e) as reachability weight; unchanged in form. |

---

## 8. Role responsibilities (summary; the full bullets live in `.claude/agents/*`)

- **abstractor** — speculative L_{n+1} operators/themes land as **`roadmap_goal` chapters** (rank 0, claim-free, pulled-by + declared deps), not stranded sketches in reports.
- **harvester** — promotion is **rank-climbing**; `firm` requires all `depends-on` deps `firm` (the invariant); authored dep-maps mark edges `depends-on`/`reference`.
- **layer-intro-author** — authors `roadmap_goal` chapters + the book methodology page; types dep-map edges; carries the feature root marker; the within-column high→low ordering is unchanged.
- **integrator-per-report / integrator-finalize** — materialize-implied → **`stub`** (rank 1) preferred over plain-text-defer; **enforce the rank gate** (block a promotion that would violate `rank(u) ≤ min(deps)`); mark new edges typed.
- **lowering-verifier** — a lowering theme is at most as resolved as its endpoints (the lowering edge is `depends-on` on both); a rank check is part of the audit.
- **critic** — checklist gains a **rank-invariant check** and a **reachability check** (does this entry's claim rest only on ≥-rank deps; is it reachable from a root).
- **cycle-planner** — fan-out = reachability weight; sequences the typing+audit campaign; dispatches the most-reachable frontier nodes first.
- **layer-intro-author / cross-layer-cross-cutter** — apply the §2f **GROUND-don't-remove** disposition (priority: ground via faithful edge → route as detritus → delete/baseline-exception) before any node is filed as garbage; the typed-edge campaign rescues absorbed/future deps by typing the honest `depends-on` edge, never a forced one.
- **meta-phase** — runs/commissions the **GC sweep** (detritus + orphaned-intent uniformly) each batch, applying the §2f grounding priority; maintains the **baseline-exception set**; refreshes the **book methodology** page (it already owns `goal-flow.md`).

---

## 9. Book methodology update (instructions)

The reader-facing mirror under `book/src/methodology/` must gain this framework (executed in the campaign, post-restart; `layer-intro-author` authors, `meta-phase` owns the refresh):
- **New page `book/src/methodology/resolution-ladder.md`** — reader-facing exposition of both axes: the graded ladder + the `rank(u) ≤ min(deps)` invariant with a worked example (the matrix-weighted-norm cascade as rank propagation); the `roadmap_goal` chapter and the `stub` vs `roadmap_goal` line; the feature root-set + reachability/liveness; the typed-edge substrate + the two linters. Non-authoritative mirror of *this* doc (if it contradicts this doc, this doc wins). Wire into `book/src/SUMMARY.md` under `# Methodology` after `goal-flow.md`.
- **`book/src/methodology/goal-flow.md`** — GOAL section gains "two checkable health invariants (well-foundedness + reachability)"; FLOW section gains the typing+audit campaign + the roadmap_goal tier. (This also resolves the open `goal-flow-mwn-firm-flip-cascade-refresh-stale-rough-in-refs` OQ.)
- Mark every `roadmap_goal` chapter unmissably (frontmatter banner + a SUMMARY grouping such as `## Roadmap goals — unbuilt frontier`) so readers never mistake intent for established fact.
