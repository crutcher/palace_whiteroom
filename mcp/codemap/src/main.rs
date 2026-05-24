//! Palace whiteroom codemap MCP server.
//!
//! Wraps tree-sitter (cpp grammar) and ripgrep behind 7 MCP tools that the
//! agent loop (Phases 4–5) uses to navigate Palace source. All paths are
//! resolved relative to the `[target].repo` directory in `config.toml`.
//!
//! Architectural invariant (per BOOTSTRAP.md *Hard invariants*):
//! `read_range` is the **only** tool that returns source text. The other
//! tools return structure (paths, locations, AST shapes) only.

use palace_codemap::{config, tools, types};

use std::path::PathBuf;
use std::sync::Arc;

use anyhow::{Context, Result};
use clap::Parser as ClapParser;
use rmcp::{
    ServerHandler, ServiceExt,
    handler::server::{router::tool::ToolRouter, wrapper::Parameters},
    model::{ServerCapabilities, ServerInfo},
    tool, tool_handler, tool_router,
};
use schemars::JsonSchema;
use serde::{Deserialize, Serialize};

#[derive(ClapParser, Debug)]
#[command(name = "palace-codemap")]
#[command(about = "MCP code-map server for the Palace whiteroom agent loop")]
struct Cli {
    /// Path to config.toml. Defaults to ../../config.toml relative to the
    /// crate (i.e., the repo root when run from inside mcp/codemap/).
    #[arg(long, default_value = "../../config.toml")]
    config: PathBuf,

    /// Override the target.repo path from config.toml. Useful for tests.
    #[arg(long)]
    target_repo: Option<PathBuf>,
}

// ────────────────────────── tool parameter structs ──────────────────────────

#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct ListFilesArgs {
    /// Optional glob pattern (e.g., `palace/linalg/*.cpp`). When omitted,
    /// returns all C/C++ source and header files under the target root.
    #[serde(default)]
    pub glob: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct ReadRangeArgs {
    /// Path relative to the target root, e.g., `palace/linalg/iterative.cpp`.
    pub path: String,
    /// 1-indexed inclusive start line.
    pub start_line: u32,
    /// 1-indexed inclusive end line.
    pub end_line: u32,
}

#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct SearchTextArgs {
    /// Regex or literal pattern, as ripgrep understands it.
    pub pattern: String,
    /// Optional glob filter passed to ripgrep's `-g` flag.
    #[serde(default)]
    pub glob: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct ListDependenciesArgs {
    /// Path relative to the target root.
    pub path: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct GetFileSubtreeArgs {
    /// Path relative to the target root.
    pub path: String,
    /// Maximum depth to recurse into the AST (root = depth 0). Unbounded
    /// when omitted.
    #[serde(default)]
    pub max_depth: Option<u32>,
}

#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct GetSymbolDefArgs {
    /// Symbol name to look up. Suffix-after-`::` matching is applied; e.g.,
    /// querying `Mult` matches `CgSolver::Mult`.
    pub name: String,
    /// Optional tree-sitter node-kind filter
    /// (`function_definition`, `class_specifier`, etc.).
    #[serde(default)]
    pub kind: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct GetCallSitesArgs {
    /// Function/method name to find call sites for. Suffix-after-`::` and
    /// `.`/`->` matching is applied to handle qualified calls.
    pub name: String,
}

// ──────────────────────────────── server ────────────────────────────────────

#[derive(Clone)]
pub struct CodemapServer {
    inner: Arc<CodemapServerInner>,
    tool_router: ToolRouter<Self>,
}

pub struct CodemapServerInner {
    target_root: PathBuf,
}

impl CodemapServer {
    pub fn new(target_root: PathBuf) -> Self {
        Self {
            inner: Arc::new(CodemapServerInner { target_root }),
            tool_router: Self::tool_router(),
        }
    }
}

#[tool_router(router = tool_router)]
impl CodemapServer {
    /// List files under the target repo, optionally filtered by a glob. With
    /// no glob, returns all C/C++ source and header files.
    #[tool(description = "List files under the target repo, optionally filtered by a glob. Returns paths relative to the target root.")]
    pub async fn list_files(
        &self,
        Parameters(args): Parameters<ListFilesArgs>,
    ) -> Result<rmcp::Json<types::ListFilesResult>, rmcp::ErrorData> {
        tools::list_files(&self.inner.target_root, args.glob.as_deref())
            .map(|files| rmcp::Json(types::ListFilesResult { files }))
            .map_err(to_mcp_err)
    }

    /// Read a line range from a target file. This is the ONLY tool that
    /// returns source text — other tools return structure or locations.
    #[tool(description = "Read a line range from a target file. THE ONLY TOOL THAT RETURNS SOURCE TEXT.")]
    pub async fn read_range(
        &self,
        Parameters(args): Parameters<ReadRangeArgs>,
    ) -> Result<String, rmcp::ErrorData> {
        tools::read_range(&self.inner.target_root, &args.path, args.start_line, args.end_line)
            .map_err(to_mcp_err)
    }

    /// Search target files for a pattern (ripgrep-equivalent). Returns
    /// {file, line, snippet} hits.
    #[tool(description = "Search target files for a pattern (regex). Returns {file, line, snippet} hits — note the snippet is a single matched line, not arbitrary source.")]
    pub async fn search_text(
        &self,
        Parameters(args): Parameters<SearchTextArgs>,
    ) -> Result<rmcp::Json<types::SearchHits>, rmcp::ErrorData> {
        tools::search_text(&self.inner.target_root, &args.pattern, args.glob.as_deref())
            .map(|hits| rmcp::Json(types::SearchHits { hits }))
            .map_err(to_mcp_err)
    }

    /// List `#include` directives in a target file. Distinguishes
    /// `"quoted"` (project) from `<angled>` (system/library) includes.
    #[tool(description = "List #include directives in a target file. Distinguishes quoted (project) vs angled (system) headers.")]
    pub async fn list_dependencies(
        &self,
        Parameters(args): Parameters<ListDependenciesArgs>,
    ) -> Result<rmcp::Json<types::IncludeList>, rmcp::ErrorData> {
        tools::list_dependencies(&self.inner.target_root, &args.path)
            .map(|includes| rmcp::Json(types::IncludeList { includes }))
            .map_err(to_mcp_err)
    }

    /// Return the AST structure of a target file as a nested tree of
    /// {kind, line/column ranges, children}. NO source text in the output.
    #[tool(description = "Return the AST structure of a target file as nested {kind, ranges, children}. NO source text. Respect max_depth to bound large files.")]
    pub async fn get_file_subtree(
        &self,
        Parameters(args): Parameters<GetFileSubtreeArgs>,
    ) -> Result<rmcp::Json<types::TreeNode>, rmcp::ErrorData> {
        tools::get_file_subtree(&self.inner.target_root, &args.path, args.max_depth)
            .map(rmcp::Json)
            .map_err(to_mcp_err)
    }

    /// Find symbol definitions by name across the target repo.
    /// Walks all C/C++ files; matches functions, classes, structs, unions,
    /// namespaces, enums, typedefs. Suffix-after-`::` matching for qualified
    /// names.
    #[tool(description = "Find symbol definitions (functions, classes, structs, namespaces, enums, typedefs) by name. Suffix-after-:: matching for qualified names. Walks the whole target tree.")]
    pub async fn get_symbol_def(
        &self,
        Parameters(args): Parameters<GetSymbolDefArgs>,
    ) -> Result<rmcp::Json<types::SymbolDefs>, rmcp::ErrorData> {
        tools::get_symbol_def(&self.inner.target_root, &args.name, args.kind.as_deref())
            .map(|symbols| rmcp::Json(types::SymbolDefs { symbols }))
            .map_err(to_mcp_err)
    }

    /// Find call sites for a function/method name across the target repo.
    /// Handles qualified calls (`Foo::bar`, `obj.bar`, `obj->bar`,
    /// `Foo<T>::bar`).
    #[tool(description = "Find call sites for a function/method name across the target repo. Handles qualified, member, and template-instantiated calls. Returns {file, line, callee}.")]
    pub async fn get_call_sites(
        &self,
        Parameters(args): Parameters<GetCallSitesArgs>,
    ) -> Result<rmcp::Json<types::CallSitesResult>, rmcp::ErrorData> {
        tools::get_call_sites(&self.inner.target_root, &args.name)
            .map(|sites| rmcp::Json(types::CallSitesResult { sites }))
            .map_err(to_mcp_err)
    }
}

#[tool_handler(router = self.tool_router)]
impl ServerHandler for CodemapServer {
    fn get_info(&self) -> ServerInfo {
        let mut info = ServerInfo::default();
        info.capabilities = ServerCapabilities::builder().enable_tools().build();
        info.instructions = Some(
            "Palace whiteroom codemap server. Use list_files / get_file_subtree / \
             get_symbol_def / get_call_sites / list_dependencies / search_text to \
             localize before reading. read_range is the only source-returning tool — \
             use it deliberately. All paths are relative to the target repo root.".into()
        );
        info
    }
}

fn to_mcp_err(e: anyhow::Error) -> rmcp::ErrorData {
    rmcp::ErrorData::internal_error(format!("{e:#}"), None)
}

#[tokio::main(flavor = "current_thread")]
async fn main() -> Result<()> {
    tracing_subscriber::fmt()
        .with_writer(std::io::stderr)  // stdout is the MCP transport
        .with_env_filter(
            tracing_subscriber::EnvFilter::try_from_default_env()
                .unwrap_or_else(|_| "info".into()),
        )
        .init();

    let cli = Cli::parse();

    let target_root = if let Some(tr) = cli.target_repo {
        tr
    } else {
        let cfg = config::Config::load(&cli.config)
            .with_context(|| format!("loading {}", cli.config.display()))?;
        // Resolve target.repo relative to the config file's directory.
        let cfg_dir = cli.config.parent().unwrap_or_else(|| std::path::Path::new("."));
        cfg_dir.join(cfg.target.repo).canonicalize()
            .context("canonicalizing target.repo")?
    };

    tracing::info!("palace-codemap starting; target_root = {}", target_root.display());

    let server = CodemapServer::new(target_root);
    let transport = (tokio::io::stdin(), tokio::io::stdout());
    let service = server.serve(transport).await
        .context("starting MCP service")?;
    service.waiting().await.context("MCP service exited")?;
    Ok(())
}
