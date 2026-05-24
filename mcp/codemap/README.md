# palace-codemap

MCP code-map server for the Palace whiteroom agent loop. Phase 1 of `BOOTSTRAP.md`.

Wraps tree-sitter (cpp grammar) and a pure-Rust regex search (`grep-searcher`) behind 7 MCP tools the agents use to navigate Palace source. All paths are resolved relative to `[target].repo` in the repo-root `config.toml`.

## Tools

| Tool                  | Purpose                                              | Returns source? |
|-----------------------|------------------------------------------------------|-----------------|
| `list_files`          | Files under the target, optionally glob-filtered     | no              |
| `read_range`          | Read a line range from a file                        | **YES** — the only tool that does |
| `search_text`         | Regex search across the tree                         | snippets only   |
| `list_dependencies`   | `#include` directives parsed from a file             | no              |
| `get_file_subtree`    | AST structure (kind + ranges + children), bounded    | no              |
| `get_symbol_def`      | Symbol definitions by name (suffix-`::`-match)       | no              |
| `get_call_sites`      | Call sites by name (handles `Foo::bar`, `obj.bar`, …) | no              |

The `read_range`-is-the-only-source-returning-tool rule is a load-bearing methodology invariant (CLAUDE.md *Load-bearing invariants*). Other tools deliberately return structure or locations so that Explorers must call `read_range` explicitly — forcing grounding.

## Build

```
cargo build --release
```

Produces `target/release/palace-codemap`. Tests:

```
cargo test --release
```

`tests/smoke.rs` exercises each tool against `reference/palace/` and is the Phase 1 DONE check.

## Run

The server speaks the MCP protocol over stdio. It's not typically run by hand; Claude Code (or the future orchestrator) launches it via `.claude/mcp.json`.

For manual debugging:

```
./target/release/palace-codemap --config ../../config.toml
```

CLI flags:

- `--config <PATH>` — path to `config.toml`. Default: `../../config.toml` relative to the crate (i.e., the repo root when run from inside `mcp/codemap/`).
- `--target-repo <PATH>` — override `target.repo` directly.

Logging is on stderr (stdout is the MCP transport). `RUST_LOG=debug ./palace-codemap ...` to raise verbosity.

## Registration with Claude Code

See `.claude/mcp.json` at the repo root. Build the release binary once before starting Claude Code in this repo — the binary must exist for CC to launch the MCP server.

## Path convention

Tool input and output paths are **relative to the target repo root** (`target.repo` in `config.toml`, typically `reference/palace`). The citation format used in the spec is *also* `palace/<rest>` because Palace's clone happens to have its source under an inner `palace/` directory — but the MCP server does not know or care about citation format. Agents writing claims handle the citation prefix.

Example: the file `palace/linalg/iterative.cpp` (MCP tool input) lives on disk at `reference/palace/palace/linalg/iterative.cpp` and is cited in the spec as `palace/palace/linalg/iterative.cpp:NNN-MMM`.

## Limitations / known v1 simplifications

- **Walks the whole target tree** on each `get_symbol_def` / `get_call_sites` call. Palace is ~300 files; the smoke suite completes in ~0.5s. If this becomes painful, file as `kind: skill-friction` / `kind: tooling-gap` in `problems/` and consider an in-memory index in v2.
- **No clangd integration.** Symbol matching is tree-sitter pattern-based, not semantic. Overloads, ADL, template specialization, and macro-expanded calls may be missed or over-matched. Per BOOTSTRAP Phase 1, clangd is optional for v1.
- **`get_symbol_def` matches the unqualified tail.** Querying `Mult` matches `CgSolver::Mult`, `GmresSolver::Mult`, and so on. Caller refines.
- **Tree-sitter parse failures are silently skipped** in the bulk walks (some files use macros tree-sitter can't model). If a known file consistently fails to parse, file under `problems/`.
