//! Shared types for tool inputs and outputs.

use schemars::JsonSchema;
use serde::{Deserialize, Serialize};

/// A location in a source file: target-relative path plus a line range.
///
/// Lines are 1-indexed and inclusive on both ends, matching the citation
/// format used throughout the spec.
#[allow(dead_code)] // Reserved for future tools; SymbolDef/CallSite carry the same fields with extras.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct Location {
    pub file: String,
    pub start_line: u32,
    pub end_line: u32,
}

/// A symbol-definition hit.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct SymbolDef {
    pub file: String,
    pub start_line: u32,
    pub end_line: u32,
    /// Tree-sitter node kind that contained the match
    /// (`function_definition`, `class_specifier`, etc.).
    pub kind: String,
    /// The matched name as it appears at the definition site.
    pub name: String,
}

/// A call-site hit.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct CallSite {
    pub file: String,
    pub line: u32,
    /// The full text of the function part of the call
    /// (e.g., `obj.foo`, `Foo::bar`, `bar`).
    pub callee: String,
}

/// An `#include` directive.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct Include {
    /// The included path, e.g. `palace/linalg/vector.hpp` or `vector`.
    pub path: String,
    /// `true` for `#include <...>` (system / library header);
    /// `false` for `#include "..."` (project / quoted header).
    pub system: bool,
    pub line: u32,
}

/// A node in the structural-subtree response.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct TreeNode {
    /// Tree-sitter node kind (e.g., `function_definition`, `class_specifier`).
    pub kind: String,
    pub start_line: u32,
    pub end_line: u32,
    pub start_col: u32,
    pub end_col: u32,
    pub children: Vec<TreeNode>,
}

/// A search hit from `search_text`.
#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct SearchHit {
    pub file: String,
    pub line: u32,
    pub snippet: String,
}

// ─────────── per-tool array wrappers ───────────
//
// MCP spec requires every tool's outputSchema to have root type `object`.
// rmcp's `Json<Vec<T>>` would emit `{type: array}`, which fails the check at
// tool-registration time. We wrap each array return in a one-field struct.

#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct ListFilesResult {
    pub files: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct SearchHits {
    pub hits: Vec<SearchHit>,
}

#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct IncludeList {
    pub includes: Vec<Include>,
}

#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct SymbolDefs {
    pub symbols: Vec<SymbolDef>,
}

#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct CallSitesResult {
    pub sites: Vec<CallSite>,
}
