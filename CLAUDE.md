# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository status

Pre-Phase-0 scaffolding is in place: this `CLAUDE.md`, `BOOTSTRAP.md`, the mdBook under `book/` (methodology overview, L4 calculus draft, meta-review procedure, one hand-drafted CG slice), the `problems/` channel, and the `reference/` clones. The agent-loop infrastructure (`questions.md`, `lessons.md`, `episodic.jsonl`, `config.toml`, `schemas/`, `prompts/`, `mcp/codemap/`, `orchestrator/`) does **not** yet exist — that is what Phases 0–5 of `BOOTSTRAP.md` build.

`BOOTSTRAP.md` is the build specification — the source of truth for what to construct, in what order, and why. Read it before doing anything substantive here.

When you implement a phase, follow the DONE criteria in `BOOTSTRAP.md` literally. Each phase has explicit completion checks; do not skip ahead and do not add scope not described in the document (no UIs, no databases, no embedding stores — those are Phase 9+ concerns).

## What this system is

A multi-agent pipeline that dissects an external target simulator's source code into an **incremental impedance-matching stack** of algorithmic representations (see *Extraction goal* below), where every claim cites `file:line` in the target and every cross-layer rotation carries an explicit equivalence justification. The agents grow a typed knowledge graph stored as plain files committed to git per loop iteration — git is the audit trail.

Roles, each invoked as a **separate API call with an isolated context** and its own system prompt from `prompts/<role>.md`. Per-cycle roles run continuously during the normal loop; the meta-cycle role runs only when the meta-review is triggered (see *Meta-review* below).

Per-cycle:

- **Planner** — picks the next push (forward / back / sideways) per the process model.
- **Explorer** (×N) — produces L0 + L1 for one slice: cites source ranges, records dataflow and any in-place mutation/aliasing observed.
- **Synthesizer** — produces L1 → L2 → L3 → L4 depth-first for a slice; proposes per-edge rotations; flags push-back opportunities.
- **Critic** — adversarial; verifies per-edge rotations against cited source and prior layers; flags labored rotations as push-back candidates.

Meta-cycle:

- **Meta-Critic** — distinct role; runs only when the meta-review trigger fires. Reviews patterns of friction across cycles with its own incremental project history (prior meta-review records). Empowered with **medium-cascade authority**; produces a refinement plan for human approval before enactment; the normal loop is paused throughout. See `book/src/meta-reviews/index.md` for the procedure.

## Layout that will exist after Phase 0

```
BOOTSTRAP.md         # phased build spec for the agent system
CLAUDE.md            # this file — operational guidance for agents
Makefile.toml        # cargo-make tasks: `cargo make book` / `book-serve` / `book-clean`
book/                # the spec, rendered as an mdBook
  book.toml          # mdBook config (matches bunsen's pattern: katex + linkcheck2 + mermaid)
  katex-macros.txt
  src/
    SUMMARY.md       # table of contents
    introduction.md
    methodology/     # methodology overview (currently a stub → CLAUDE.md)
    spec/
      index.md       # slice status table (THE place to read first)
      slices/        # one file per slice; subdirectory for genuinely large slices
    concepts/
      index.md       # shared-primitive library; extracted on demand
    design/
      index.md
      l4_calculus.md # L4 strawman — the formal graph-evaluation calculus
    meta-reviews/
      index.md       # records of friction-integration passes
problems/            # out-of-band concern channel — see problems/README.md
reference/           # local clones of palace, bunsen, burn, tensorflow-java (gitignored)

# Files Phase 0 of BOOTSTRAP.md creates (agent-loop infrastructure):
questions.md         # open/closed question ledger — surfaces unknowns
lessons.md           # cross-run lessons appended by the Critic
episodic.jsonl       # append-only per-cycle log (becomes the research record)
config.toml          # target paths, language, model ids, budgets
schemas/             # exploration_finding.json, critic_verdict.json
prompts/             # planner.md, explorer.md, synthesizer.md, critic.md
mcp/codemap/         # Rust MCP server (Phase 1) — tree-sitter wrapper
orchestrator/        # Python loop (Phase 5) — raw Anthropic SDK
```

The mdBook is the public-facing rendering of the spec; the markdown under `book/src/` *is* the artifact. Build with `cargo make book` (one-time tooling install on first run); live preview with `cargo make book-serve`.

The target repo lives outside this workspace at the `[target].repo` path in `config.toml`. Treat it as read-only.

## Extraction goal — what the spec is *for*

This work is part of a broader methodology being developed in the user's **bunsen** project: lifting traditional C/Fortran tensor-field simulators — which evolve fields by array iteration with in-place mutation — into a **citation-grounded, incrementally-layered series of representations**, where each layer re-expresses the layer below in a representation that has rotated one specific impedance, and the rotation is explicitly stated and verified.

Palace is a substantial test case for this methodology. **No port is produced as part of this work.** The output is a layered specification; a separate downstream effort will use it to incrementally build burn components.

- **Source environment:** Palace, C++/HPC, makes aggressive use of in-place mutation of vectors and matrices, reused scratch/workspace buffers, and aliasing-aware BLAS-style kernels. These exist because the source environment makes them cheap; they are *implementation*, not semantics.
- **Spec notation:** the spec is written in **language-agnostic, Haskell/Scheme-flavored abstract notation** — immutable tensors, collection structures over them, and monads over the above (Haskell sense). It does **not** commit to burn, to Rust, to eager-vs-traced execution, or to any specific concrete representation. The goal is **abstract ownership / update-operation extraction in language-agnostic form**, suitable as input to a future "what burn needs to realize this" requirements-spec — which is itself a separate artifact, not a layer in this stack. Targeting burn (or any architecture) prematurely would introduce constraints on the math we don't want.
- **Out of scope for this effort:** `burn::module::Module` / `forward()` machinery (wrong shape for stateful iterative simulators); `burn-ir` (internal kernel-fusion IR, not a public API, the user is familiar with its limits); any concrete Rust API design. Those belong to the downstream burn-realization work, not here.

### Output structure: an incremental impedance-matching stack

The output is not a single port. It is an **incremental stack of representations**, each of which:

- Is a complete description of the algorithm at its own level of abstraction.
- Has an explicit *reference layer* immediately below it.
- States the **semantic rotation** by which the reference layer's semantics are re-expressed in the new representation, and justifies that the rotation preserves what matters.

Design notion: **Incremental Impedance Matching.** No single jump from C++/HPC to a formally-specified graph-evaluation calculus could be both faithful and reviewable. The tower lets each layer match *one* impedance — mutation → purity, fusion → algebraic decomposition, iteration → global tensor op, operator algebra → formal graph-evaluation calculus — so each rotation can be implemented and validated as a stepping stone.

**Lower layers** (already identifiable from the C++ side):

- **L0** — cited Palace/MFEM source ranges (`file:line`). Ground truth.
- **L1** — *mutation rotation*. Source operations re-expressed as pure functions: explicit input set, output set; in-place mutation and aliasing patterns either erased (workspace/scratch buffers) or made explicit (semantically-meaningful aliasing). Structurally close to the source loop.
- **L2** — *fusion rotation*. L1 unfolded back into composition of base algebraic primitives, with HPC/SIMD tricks (cache-blocked loops, kernel fusion across multiple algebraic ops, packed sparse formats, batched specialized BLAS) erased. The canonical algebraic decomposition. See `### Optimization tricks vs. base algebra` below.
- **L3** — *iteration rotation*. Where it exists, L2 re-expressed as a global tensor-field / convolution-over-space operation — whole-tensor ops, no element loop. Where no such global form exists (Gauss-Seidel-flavored smoothers, certain triangular solves, sequentially-reordered preconditioners), record the **obstruction** that prevents the lift, and stop. Negative L3 results — algorithms that genuinely don't lift, with reasons — are first-class output.

**L4** — the top of the stack: a **small, formally-defined graph-evaluation calculus**, in the Haskell/Scheme tradition. Algorithms are described in this calculus's syntax, with semantics governed by formal evaluation rules — not informal pseudo-code.

L4 is **vocabulary, not architecture.** It is not pseudo-Rust, not a burn API sketch, not a runtime design. It does not commit to eager-vs-traced, to specific containers, or to any particular monad implementation. **Code-like syntax is allowed and expected**, but the goal is not "we can run this." The goal is to capture, in language-agnostic form:

1. **What operations happen** — the primitives / verbs, with their signatures and shape contracts.
2. **Who owns the state** — with explicit, first-class distinction between:
   - **Simulator state** (the iterate, residual, convergence flags — what evolves through the algorithm).
   - **Operator internal parameters** (matrix entries, preconditioner factorizations, mesh+basis tables, time-step constants — what operators *hold* as closure-like data and apply to sim state, but which does not itself evolve during a solve).
   - **Ephemeral intermediates** (per-step values that exist only inside a single update and don't survive across iterations).
3. **How state evolution is coordinated** — sequencing, iteration, convergence tests, branching, effects (logging, monitoring) — expressed as monadic structure (Haskell sense), not informal control flow.

L4 is built from:

- A **grammar** for terms: variables, abstractions, applications, let-bindings, tensor literals, primitive ops, monadic bind/return for stateful iteration. Roughly an ANF / let-binding form in the lambda-calculus tradition (Pierce *TAPL* / Harper *PFPL*), with JAX's jaxpr as a working reference for what such a form looks like as a small calculus.
- **Evaluation rules** (small-step reductions): β, let-substitution, δ-rules for primitive tensor ops, monad laws (left identity / right identity / associativity), sharing rules where applicable. The semantics describe state evolution, not CPU execution.
- **Type and shape rules**: typed judgments `Γ ⊢ e : τ` with τ carrying symbolic tensor shapes (bunsen `DimExpr`-style algebra at the type level). Linear / affine annotations where single-use ownership matters — they are the formal mechanism for distinguishing operator-params-as-closure from sim-state-being-threaded.
- **Algebraic equational laws**: commutativity, associativity, distributivity of ops where they hold; the simplification rules that make Palace's L3 forms formally equal to L4 monadic programs.
- **Worked examples**: Palace algorithms (and bunsen's Conway/LBM as sanity checks) expressed in L4 syntax, with their L3↔L4 correspondence argued via the reduction rules.

**Syntactic style.** The notation borrows **TypeScript-style record literal / destructuring / spread-update syntax** (`{ x, r, ...rest } = state`, `{ ...state, x: x_new, rr: rr_new }`) for state-update ergonomics — TS has notably better record syntax than Haskell or Scheme for this purpose. Monadic structure (`do`-blocks, `>>=`) is Haskell-flavored, for coordination of state evolution and effects. **Deliberately avoided:** Haskell's lens / optic machinery and any equivalent Scheme record-accessor library — they obscure the algorithm more than they help. Type annotations are Haskell-style (`f :: A -> B -> M C`). The notation does not need to compile; it needs to read clearly and admit formal-semantics treatment.

The **L3→L4 rotation** is therefore a *formal correspondence argument*: given an L3 pure-tensor-algebraic decomposition, exhibit an L4 program and a chain of equational steps justifying their equivalence. The Critic verifies this chain. Where the chain breaks (the L3 form has no L4 correspondent under the calculus), record the obstruction as a push-back candidate against either L3 or the L4 calculus design itself.

After L4 exists, **a separate downstream artifact** specs what burn would need to *realize* the L4 calculus — backend operations, evaluation strategy, shape solver, monad-realization choice, expression-graph or eager dispatch, etc. That artifact is **not** a layer in the stack; it consumes L4 as input, and its design is explicitly out of scope for the layered spec work.

**Equivalence is per-edge.** For every adjacent pair `(Li, Li+1)` and every algorithm, the spec carries an explicit rotation claim and its justification — algebraic argument, structural/symmetry argument, formal reduction chain (for L3→L4), or empirical match against a reference run. The Critic verifies these per-edge; it does not try to verify L4 against L0 directly, because the whole point of the tower is that no single rotation is that long.

**Where bunsen sits.** The `kits::sims` examples (Conway, LBM) implement L3 pure tensor-algebra concretely against burn — pure tensor-in / tensor-out functions wrapped in thin mutable state structs. The mutable wrappers *gesture toward* L4 but don't realize it: no formal calculus, no first-class distinction between sim state and operator params, no explicit effect tracking. The bunsen contracts macros and docstring shape annotations show how L3 is *written* in practice in real Rust+burn code. Bunsen is what L3-in-burn looks like today; the (separate, downstream) burn-realization artifact will eventually specify what additional burn machinery is needed to realize L4 against this foundation.

### Process: push-forward, push-back; the stack is a research artifact

**The stack is not the deliverable.** It is a research artifact whose construction yields the understanding that *is* the deliverable. Layers exist to expose friction. The valuable signal lives in the friction:

- **"How hard is it to build the next layer *for this part*?"** — measures whether the current layer's representation is adequate for the next rotation. High friction means the current layer is missing something.
- **"What could have existed in the previous layer to make this simpler?"** — the push-back signal. When friction shows up at layer N+1, the answer becomes a structural change to layer N.

The process is **not** waterfall through the stack. Do not write all of L1, then all of L2, then all of L3. That discards the signal. Instead:

1. **Push-forward, one slice at a time.** Take a slice of Palace (one algorithm, one routine, one piece of state). Build L1 for that slice *only to the point that L2 concepts can begin to be described*. Then build L2 only to the point that L3 can begin. Same for L4. **A layer's job ends as soon as the next layer can speak.** Completing a layer breadth-first across all algorithms before moving up is wrong; the cross-algorithm pressure that drives unification doesn't show up until you've reached for the next layer.
2. **Push-back when friction surfaces.** While working at layer N+1, if a different framing of layer N would make N+1 dramatically easier, unify multiple algorithms at N+1, or eliminate an awkward corner — restructure layer N. The change ripples down to L0 (new questions / re-explorations) and back up to N+1 as a now-easier rotation.
3. **Move sideways.** When one slice is pushed high enough that progress is blocked on infrastructure rather than its own substance, switch to a different slice. Use the sideways move to surface unification opportunities ("L2 for X and L2 for Y look similar — could they share a primitive?").

Implications for the agent loop, encoded in `BOOTSTRAP.md`:

- **The Planner picks the next push**, not the next open question from a ledger — forward at some slice, back from a friction point, or sideways for unification.
- **"Done" is friction-resolved**, not citation-complete: the lower layers are unified enough that adding a new algorithm at L1 propagates upward easily, and L4 has at least one worked sample showing the rotation chain end-to-end. Count-based criteria (citations present, N slices to L4) are necessary scaffolding, not sufficient closure.
- **The episodic log is a research record**, not just telemetry. Every push (forward, back, sideways) records the friction observed and the structural change made. The log is part of the artifact.
- **The question ledger surfaces unknowns**, not to-dos. The to-do is whatever push the current friction suggests.

### Role contracts

Roles operate within the push-forward / push-back process above. Per slice the loop is depth-first through the stack; per layer the loop is friction-driven, not enumerative. L4 is designed as a system (separate work) rather than synthesized per-algorithm; L1–L3 are produced per-slice by the agent loop.

- **Explorers** produce L0 + L1: cite the source range and record the explicit input set (tensors read), output set (tensors produced), and any in-place mutation/aliasing pattern observed. A claim like "`Foo::Apply(x, y)` computes `y = A·x`" is too loose — is `y` overwritten? accumulated into? aliased with `x`? Record what the source actually does.
- **Synthesizer** produces just-enough L1 to enable L2 for the current slice, just-enough L2 to enable L3, and so on (depth-first per slice, not breadth-first per layer). It proposes the L1→L2 rotation (fusion-unfolded algebraic decomposition) and L2→L3 (field-transition) **when those become reachable for the slice in hand** — explicitly leaving "no global lift found, obstruction = X" as a valid L3 outcome. It also **flags push-back opportunities**: when the L1 form forces a labored L2 rotation, or L2 forces an awkward L3, propose a structural change to the lower layer rather than absorbing the awkwardness silently.
- **Critic** checks each per-edge rotation the Synthesizer has proposed: does the source support L1; does L1 algebraically equal L2 after unfolding the noted optimization tricks; does L2 equal L3 as a field-transition. Insufficient justification is `missing_case` or `unclear`; an outright rotation mismatch is `control_flow_mismatch` or `contradicts_existing_spec`. **The Critic also surfaces friction-as-a-signal:** a rotation that's technically correct but obviously forced — special cases, exception branches, special-pleading conditions — is a push-back candidate; flag it as `unclear` with an explicit "would lower-layer change X eliminate this friction?" suggestion.

The schemas and prompts encoding this discipline live in `BOOTSTRAP.md` Phases 3–4: `schemas/rotation_claim.json` with `justification_kind ∈ {algebraic, structural, reduction_chain, empirical_match, obstruction}`, the Explorer prompt's mutation-pattern enum, the Synthesizer's transparent-vs-load-bearing distinction, and the Critic's per-edge rotation checks.

Patterns to expect, and how they should appear in the spec:

| Palace (C++/HPC, mutating)                | L1 form (mutation-lifted, pure-functional)           |
|-------------------------------------------|------------------------------------------------------|
| `x.Add(alpha, y)` → `x += α·y`            | `x_{k+1} = x_k + α·y`                                |
| `A.Mult(x, y)` → writes into `y`          | `y = A·x`  (no mention of destination buffer)        |
| CG/GMRES loop mutating iterate in place   | functional unfold: `state_{k+1} = step(state_k)`     |
| Reused workspace `tmp` across iterations  | omitted; the COW backend handles allocation          |
| MPI ghost-cell exchange / cross-rank op   | **out of scope** — see Scope below                   |

### Optimization tricks vs. base algebra

A significant fraction of Palace's C++ exists because it was tuned for the cost model of CPU + cache hierarchy + SIMD lanes. **That cost model is not burn's**, and most of the resulting code shape is counter to the goals of a pure GPU tensor implementation. Cache-blocked loops, SIMD intrinsics, manual unrolling, kernel fusion across multiple algebraic operations, packed sparse formats (CSR / ELLPACK / block-sparse), specialized small-element kernels, and batched BLAS calls are **optimization tricks**, not algebra. They obscure what the code is actually computing.

The L2 form is the **canonical algebraic decomposition**: the operation written as composition of base tensor / operator / quadrature primitives, **with optimization tricks unfolded back into the base algebras** (this is the L1→L2 rotation). For example, a fused FE-operator loop that interleaves gradient evaluation at quadrature points, material contraction, quadrature weighting, and test-function assembly is L2-described as the composition `G^T · W · M · G` (read right-to-left, applied to a DoF vector), with at most a brief note that the source fuses these steps for cache locality. Cache blocking, SIMD packing, and memory-layout choices are not mentioned at all — they are below the level of abstraction the spec captures.

The Critic must distinguish two categories of trick and treat them very differently:

- **Transparent performance tricks** — fusion, tiling, packing, batching, memory layout, recomputation-vs.-lookup-table — are algebraically equivalent to their unfolded form. The L1 form is the unfolded form; the trick gets a one-line note in the spec, not a claim.
- **Load-bearing numerical tricks** — non-associative reduction orderings, fast-math flags, mixed-precision intermediates, deterministic-vs.-atomic accumulation choices, sign/scaling conventions inside factorizations — are **part of the algorithm**, not just its execution. They must be preserved as explicit algebraic claims, with the property they buy (determinism, condition-number behavior, IEEE compliance) called out.

When in doubt about which category a given trick belongs to, the Critic should flag it as `unclear` and let the human triage. Mis-classifying a load-bearing trick as transparent silently changes the algorithm; the converse (over-flagging transparent tricks) is merely annoying.

## Scope

**Target deployment is a single machine.** The speedup story is **CPU → GPU** via burn's device backends (CUDA / ROCm / WGPU / Metal — burn handles dispatch). MPI / multi-rank distribution is **out of scope**: it requires targeted R&D on the host environment that is not part of this effort.

Concrete implications for Explorers:

- Any code path conditioned on `MPI_*`, multi-rank communicators, ghost-cell exchange, `HYPRE_Par*`, or cross-rank reductions is **out of scope** — flag it once in an Explorer note (so the Synthesizer doesn't keep re-questioning the same files) and skip it. Do not raise it as an open question.
- In MFEM, the `Par*` family of types (`ParGridFunction`, `ParBilinearForm`, `ParMesh`, `HypreParVector`, …) are the parallel analogues of `GridFunction`, `BilinearForm`, `Mesh`, `Vector`, etc. **Read parallel types as their single-rank equivalents semantically** — the spec records the local algorithm; parallel wrapping is implementation.
- Distributed mesh partitioning, parallel I/O, and rank-aware assembly are out of scope. Single-rank assembly and the solver pipeline that consumes assembled operators are in scope.
- The pure-functional / COW lifting (above) still fully applies — burn's GPU backends are why we need it.

**Solvers in scope: all five.** Electrostatic, magnetostatic, eigenmode, driven (frequency-domain), transient (time-domain). They share substantial infrastructure (FE spaces, operator assembly, linear/eigenvalue solvers) — Phase 2's `questions.md` seed includes a top-level question per solver in addition to the generic shared-infrastructure questions, so the Planner can interleave the two rather than getting stuck in one solver's silo.

**Mesh / FE-space construction is in scope** (resolved 2026-05-23). The spec dissects MFEM-equivalent FE assembly — quadrature, basis tables, geometric-factor computation, sparse-assembly patterns — alongside the five solver pipelines. Drawing the boundary at the assembled-operator interface would have been narrower but the user took the more ambitious option deliberately: full-pipeline spec.

Practical consequence: Phase 2's `questions.md` seed includes mesh/FE-space top-level questions in addition to the per-solver questions. When choosing a Phase 6 smoke-test slice, prefer assembled-operator algorithms first (GMRES, per `BOOTSTRAP.md`) — mesh/FE assembly is a substantial separate surface that benefits from being tackled after the solver pipeline has been validated.

## Target system

The target being dissected is **AWS Labs Palace** — <https://github.com/awslabs/palace>. "PArallel, LArge-scale Computational Electromagnetics": an open-source parallel finite element code for full-wave 3D EM simulation.

- **Language:** C++ (~85% of the tree). Set `[target].language = "cpp"` in `config.toml`. Tree-sitter has a C++ grammar — no Phase 1 escalation expected on that front.
- **Build:** CMake ≥ 3.24.
- **Major deps:** MFEM (finite element discretization), libCEED (exascale discretization kernels), MPI, BLAS/LAPACK; optional CUDA / ROCm for GPU.

Implications for the dissection agents:

- Many symbols resolve into **upstream libraries** (MFEM, libCEED). Explorers should cite Palace source — not vendored or upstream code — and raise the upstream surface as `contract` claims rather than chasing definitions into MFEM. If a question genuinely requires upstream behavior, log it as an open question and surface it to the human.
- Heavy use of **C++ templates and library-provided abstractions** means `get_symbol_def` / `get_call_sites` will sometimes return many sites; prefer `search_text` with tighter patterns when that happens, and narrow before calling `read_range`.
- For MPI-related code paths, see Scope above — single-rank semantics are the spec; parallel wrapping is implementation.

## Reference repos (local clones)

`reference/` (gitignored) holds shallow clones of the three relevant upstream repos. Read them locally; don't re-fetch from GitHub.

- `reference/palace/` — the C++ source being dissected.
- `reference/bunsen/` — the user's burn-overlay library. **`reference/bunsen/crates/bunsen/src/kits/sims/` is the methodology reference for this project** (see below).
- `reference/burn/` — the target tensor library. Before claiming an L2 form maps cleanly to "burn primitives," verify the relevant op actually exists in burn.

## Bunsen methodology conventions

The methodology being applied to Palace was developed in the bunsen project. Its `kits::sims` module is the canonical realization, in working Rust+burn code:

- `conway/{life2d,life3d}.rs` — Conway's Game of Life. The textbook iteration-to-tensor-field lift: per-cell scan with neighbor-counting becomes `unfold` + `sum_dims` + elementwise rule. The floor of the methodology's range — minimal but complete.
- `lbm/d2q9/` — Lattice-Boltzmann fluid simulation (D2Q9), decomposed into separate modules for `streaming`, `collision`, `reflection`, `relaxation`, `space`, `thermal`, and the `simulation` orchestrator. Mid-range example with multi-operator composition, boundary handling, and conservation-checking tests.

Conventions visible in those examples that should propagate into Palace's spec:

- **Pure tensor-in / tensor-out functions are the algebra.** `pub fn outflow_clipping_stream<B>(dist: Tensor<B,4>) -> Tensor<B,4>` is the canonical L1 form. State-bearing structs (`ConwayLife2DState`) are *thin* wrappers whose `step()` is `self.state = pure_step(self.state.clone())`. The mutation lives in the wrapper; the algebra is pure.
- **Decompose into named algebraic pieces.** LBM does *not* fuse streaming + collision + boundary handling into one `step()`. They are separate functions in separate files. Palace's spec should decompose each solver the same way — each piece independently citeable and independently testable.
- **Symbolic shape contracts at boundaries.** bunsen's `contracts::unpack_shape_contract!` / `assert_shape_contract_periodically!` macros declare input/output shapes symbolically — e.g., `[H, W, VY=3, VX=3]` with named axes and pinned values where present. Every L1 operation in the spec should declare its shape contract in this form.
- **Docstrings declare I/O sets explicitly.** `# Arguments` / `# Returns` blocks with shape annotations, e.g. `dist: [H, W, VY=3, VX=3]` → `[H-2, W-2, VY=3, VX=3]`. This is exactly the L1 record the methodology requires. The spec's prose should mirror this format.
- **L1↔L2 equivalence is tested concretely.** Conway's `test_logic` runs `next_interior_2d` against a known state and asserts exact equality to a hand-computed result. LBM's `test_debug_flow_loss` checks energy conservation through streaming + collision. When the cost is reasonable, the spec's equivalence claims should be backed by tests of this kind, not by algebra alone.
- **Performance notes are inline `// Timing:` comments, not abstractions.** Backend-dispatch tricks (`cat([cat([t,]),])` outperforms `cat([t,]).reshape(...)` by ~10% — actual comment in `streaming.rs`) are noted in-place. These are exactly the **transparent performance tricks** the methodology distinguishes from algebra: they affect *expression* of an algebraically-equivalent op, not the algebra itself, and stay below the spec's level of abstraction.
- **Config/init pattern for hyperparameters.** `ConwayLife2DConfig { shape: [usize; 2] }` + `impl Config { fn init(self, device) -> ConwayLife2DState }`. Palace's solver hyperparameters (frequency, time step, tolerance, max iters, preconditioner choice, …) should be expressible as bunsen-style `Config` structs in any eventual port.

Conway is the floor; LBM is roughly mid-range. **Palace's solvers will sit above LBM in complexity** — Krylov iterations, preconditioners, eigenvalue solvers on FE-assembled operators — but the *decomposition discipline* is the same.

## Load-bearing invariants

Violating any of these defeats the architecture — do not "improve" them away:

- **Citations are mandatory.** Every claim in the spec must carry `(file, start_line, end_line)`. No citation, no claim. The Explorer prompt enforces this; the Critic verifies it.
- **`read_range` is the only source-returning MCP tool.** All other tools (`list_files`, `get_file_subtree`, `get_symbol_def`, `get_call_sites`, `list_dependencies`, `search_text`) return structure or locations, never source text. This forces Explorers to localize before reading.
- **Roles do not share context.** Each role gets its own API call, its own system prompt, no conversation history from other roles. The Critic in particular must not see the Explorer's chain-of-thought — reasoning is persuasive in the wrong direction.
- **Synthesizer outputs diffs, not rewrites.** Spec growth must be monotonic and visible in `git log`.
- **Commit every cycle, pass or fail.** Episodic log + git history together are the audit trail.
- **Lessons append on every disagreement.** Cheap, disproportionately effective.
- **If a step is ambiguous, stop and ask the human.** Do not improvise around the spec.

## Models (per `config.toml`)

- Planner: `claude-haiku-4-5-20251001` (cheap routing)
- Explorer / Synthesizer / Critic: `claude-opus-4-7` (quality matters; Critic most of all)

## Problems channel — out-of-band concerns

`problems/` is the channel for agents to raise concerns that exceed their own role's authority. **Bar: "the right answer requires authority I don't have."** Files are named `${YYYY-MM-DDTHHMMSS}Z.md` (UTC, colons stripped). Full protocol — when to file, when not, file format, lifecycle — lives in `problems/README.md`. Read that file before filing or reviewing.

Three categories qualify:
- **Out-of-role conflicts** (e.g. Critic notices a Synthesizer-prompt-level pattern).
- **In-line framing concerns** (the methodology as described doesn't fit the slice in hand, in a way that exceeds the agent's responsibility).
- **Tooling / infrastructure gaps** the agent can't work around in-role.

Things that **do not** belong here: target-code unknowns (→ `questions.md`), agent mistakes recognized in retrospect (→ `lessons.md`), normal layer push-back (→ Synthesizer, expected process), per-claim rotation failures (→ Critic verdict). Conservative temperature — if it fits any of those channels, use them.

Problems are reviewed out-of-cycle by the human, not by the agent loop. Resolved problems are annotated in place; never deleted (they're part of the research record).

## Meta-review — out-of-cycle friction integration

Full procedure: `book/src/meta-reviews/index.md`.

**Trigger**: every 10 completed agent cycles, or human invocation. The normal loop **pauses** until the meta-review is fully enacted — analysis → plan → human approval → enactment — and only then resumes.

**Driver**: a distinct **Meta-Critic** role (not the per-cycle Critic) with its own system prompt, isolated context, and incremental project history built from prior meta-review records. The Meta-Critic carries **medium-cascade authority**:

- **Low** (typos, single-file clarifications, prompt-wording polish): applied directly.
- **Medium** (prompt revisions, methodology adjustments within the framework, slice-convention restructuring, new `concepts/` entries): **bundled into a refinement plan, requires human approval before enactment.**
- **High** (layer-count or layer-semantics changes, L4 calculus revisions, core process-model changes, new agent roles): **surfaced as escalation, not acted on** — design-level conversation with the human follows.

Each pass produces two artifacts in `book/src/meta-reviews/`:

- `<YYYY-MM-DD>.md` — the meta-review **record** (immutable once committed; the next Meta-Critic reads these as project history).
- `<YYYY-MM-DD>-plan.md` — the **refinement plan** (proposed-and-finalized; the as-proposed and as-enacted are both readable historically).

Recurring patterns across meta-review records are first-class signal — a problem resolved once that recurs is evidence the resolution didn't stick, and may escalate from Medium to High on the third hit.

## Pinned conventions (confirmed)

- **Layer count: 4 above L0.** L1 mutation, L2 fusion-unfolded algebra, L3 field-transition, L4 formal graph-evaluation calculus. Not collapsed.
- **Output format: mdBook from day one.** Plain Markdown with KaTeX math under `book/src/`. Layout mirrors bunsen's book.
- **Slice granularity: one slice per algorithm.** Small / medium slices are a single Markdown file with consistent `## L0` / `## L1` / `## L2` / `## L3` / `## L4` section headings. **Genuinely large slices** (e.g., GMRES with Hessenberg, Givens rotations, restart logic; or block-multigrid) are organized as a **subdirectory `book/src/spec/slices/<slice>/` from the start**, with per-layer files or per-aspect files (best judgment by the Synthesizer). Splitting after-the-fact is more disruptive than planning multi-file from the start; reach for the subdirectory shape when the single-file form would exceed ~400 lines or the layer sections would each be book-chapter-sized.
- **Citation format: plain text** `relative/path/file.ext:start-end` (relative to `reference/`), e.g., `palace/linalg/cg.cpp:42-67`. Editors with line-aware navigation resolve these against local clones. No markdown links — the grep/IDE workflow is the navigation.
- **Meta-cycle: every 10 completed agent cycles or manual.** Procedure in `book/src/meta-reviews/index.md`.
- **`concepts/` library** (under `book/src/concepts/`) is extracted on demand: when a slice reaches for a primitive or abstract concept that "feels canonical," add it. Cross-link from slices. This is both DRY and the unification artifact of the methodology.
- **Every piece of produced spec content** (slice file, concept file, design artifact, meta-review record) may optionally include two agent-facing sections:
  - **`## Context`** — at the top of the file, after the title: a short orientation paragraph for agents reading this section cold. What this is, why it exists, what you need to know to read the rest. Not the spec content itself.
  - **`## Working Notes`** — at the bottom of the file: issues, todos, ongoing needs, breadcrumbs for the next agent or human to pick up where the prior author left off. Loose-form. The place to leave "I noticed X but didn't address it" without forcing it into the question ledger or `problems/`.

## Escalation triggers (stop and ask)

Surface these to the human immediately rather than working around them — they signal architectural problems, not content problems:

- Tree-sitter has no grammar for the target language.
- No clear entry point after exploring Q1.
- Critic rejects three consecutive Synthesizer outputs on the same question (prompt bug, not content).
- An Explorer's input exceeds `explorer_max_input_tokens` on one region (scope too coarse — Planner needs to subdivide).
- Question ledger grows monotonically over 20 cycles with zero closures (generating questions faster than answering).
- Two Explorers produce contradictory claims about the same source range across consecutive cycles (source itself may be ambiguous — needs human triage).

## Inputs the human must supply before Phase 0

`TARGET_REPO` (absolute path), `WORKSPACE` (empty dir), primary target language, Anthropic API access, and optionally target build/run instructions (enables Phase 7 execution grounding). If any are missing or ambiguous when you start a phase, **stop and ask** — do not guess.
