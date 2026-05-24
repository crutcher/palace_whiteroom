//! Tool implementations. Plain sync functions; the MCP layer in main.rs
//! wraps these as async tool methods.

use anyhow::{anyhow, bail, Context, Result};
use globset::{Glob, GlobMatcher};
use grep_regex::RegexMatcher;
use grep_searcher::{Searcher, Sink, SinkMatch};
use std::path::{Path, PathBuf};
use walkdir::WalkDir;

use crate::parser::{find_name, name_matches, new_cpp_parser, node_text, walk};
use crate::types::{CallSite, Include, SearchHit, SymbolDef, TreeNode};

/// Resolve a target-relative path under `root`, rejecting `..` escapes.
fn resolve_under(root: &Path, rel: &str) -> Result<PathBuf> {
    let candidate = root.join(rel);
    let canonical = candidate.canonicalize()
        .with_context(|| format!("resolving path {rel} under {}", root.display()))?;
    let root_canonical = root.canonicalize()
        .with_context(|| format!("canonicalizing root {}", root.display()))?;
    if !canonical.starts_with(&root_canonical) {
        bail!("path {rel} escapes target root {}", root.display());
    }
    Ok(canonical)
}

pub fn list_files(root: &Path, glob: Option<&str>) -> Result<Vec<String>> {
    let matcher: Option<GlobMatcher> = match glob {
        Some(g) => Some(Glob::new(g).context("compiling glob")?.compile_matcher()),
        None => None,
    };
    let root_canonical = root.canonicalize().context("canonicalizing root")?;
    let mut out = Vec::new();
    for entry in WalkDir::new(&root_canonical).into_iter().filter_map(|e| e.ok()) {
        if !entry.file_type().is_file() {
            continue;
        }
        let rel = match entry.path().strip_prefix(&root_canonical) {
            Ok(r) => r.to_string_lossy().into_owned(),
            Err(_) => continue,
        };
        // Default: C/C++ source and header files. With an explicit glob,
        // honor that instead.
        let is_cpp = matches!(
            entry.path().extension().and_then(|s| s.to_str()),
            Some("cpp" | "hpp" | "h" | "cc" | "cxx" | "hxx" | "C")
        );
        let keep = match &matcher {
            Some(m) => m.is_match(&rel),
            None => is_cpp,
        };
        if keep {
            out.push(rel);
        }
    }
    out.sort();
    Ok(out)
}

pub fn read_range(root: &Path, path: &str, start_line: u32, end_line: u32) -> Result<String> {
    if end_line < start_line {
        bail!("end_line {end_line} < start_line {start_line}");
    }
    let abs = resolve_under(root, path)?;
    let contents = std::fs::read_to_string(&abs)
        .with_context(|| format!("reading {}", abs.display()))?;
    let mut out = String::new();
    for (idx, line) in contents.lines().enumerate() {
        let line_no = (idx + 1) as u32;
        if line_no < start_line {
            continue;
        }
        if line_no > end_line {
            break;
        }
        out.push_str(line);
        out.push('\n');
    }
    Ok(out)
}

pub fn search_text(root: &Path, pattern: &str, glob: Option<&str>) -> Result<Vec<SearchHit>> {
    let root_canonical = root.canonicalize().context("canonicalizing root")?;
    let matcher = RegexMatcher::new(pattern)
        .with_context(|| format!("compiling regex {pattern:?}"))?;
    let glob_matcher: Option<GlobMatcher> = match glob {
        Some(g) => Some(Glob::new(g).context("compiling glob")?.compile_matcher()),
        None => None,
    };
    let mut hits = Vec::new();
    let mut searcher = Searcher::new();
    for entry in WalkDir::new(&root_canonical).into_iter().filter_map(|e| e.ok()) {
        if !entry.file_type().is_file() {
            continue;
        }
        let path = entry.path();
        let rel = match path.strip_prefix(&root_canonical) {
            Ok(p) => p.to_string_lossy().into_owned(),
            Err(_) => continue,
        };
        // With no glob, default to C/C++ extensions (same as list_files default).
        let keep = match &glob_matcher {
            Some(m) => m.is_match(&rel),
            None => matches!(
                path.extension().and_then(|s| s.to_str()),
                Some("cpp" | "hpp" | "h" | "cc" | "cxx" | "hxx" | "C")
            ),
        };
        if !keep {
            continue;
        }
        let mut sink = CollectingSink { rel: &rel, hits: &mut hits };
        // Best-effort: skip files we can't open (e.g., permission, transient).
        let _ = searcher.search_path(&matcher, path, &mut sink);
    }
    Ok(hits)
}

struct CollectingSink<'a> {
    rel: &'a str,
    hits: &'a mut Vec<SearchHit>,
}

impl<'a> Sink for CollectingSink<'a> {
    type Error = std::io::Error;

    fn matched(&mut self, _searcher: &Searcher, mat: &SinkMatch<'_>) -> Result<bool, Self::Error> {
        let line_no = mat.line_number().unwrap_or(0) as u32;
        let bytes = mat.bytes();
        // Strip a trailing newline if present.
        let trimmed_end = bytes.iter().rposition(|&b| b != b'\n' && b != b'\r')
            .map(|i| &bytes[..=i])
            .unwrap_or(bytes);
        let snippet = String::from_utf8_lossy(trimmed_end).into_owned();
        self.hits.push(SearchHit {
            file: self.rel.to_string(),
            line: line_no,
            snippet,
        });
        Ok(true)
    }
}

pub fn list_dependencies(root: &Path, path: &str) -> Result<Vec<Include>> {
    let abs = resolve_under(root, path)?;
    let source = std::fs::read_to_string(&abs)
        .with_context(|| format!("reading {}", abs.display()))?;
    let mut parser = new_cpp_parser()?;
    let tree = parser.parse(&source, None)
        .ok_or_else(|| anyhow!("parse failed for {}", abs.display()))?;
    let mut includes = Vec::new();
    walk(tree.root_node(), |node| {
        if node.kind() != "preproc_include" {
            return;
        }
        let Some(path_node) = node.child_by_field_name("path") else { return };
        let raw = node_text(path_node, &source);
        let (system, trimmed) = if raw.starts_with('<') && raw.ends_with('>') {
            (true, &raw[1..raw.len()-1])
        } else if raw.starts_with('"') && raw.ends_with('"') {
            (false, &raw[1..raw.len()-1])
        } else {
            (false, raw)
        };
        let line = node.start_position().row as u32 + 1;
        includes.push(Include {
            path: trimmed.to_string(),
            system,
            line,
        });
    });
    Ok(includes)
}

pub fn get_file_subtree(root: &Path, path: &str, max_depth: Option<u32>) -> Result<TreeNode> {
    let abs = resolve_under(root, path)?;
    let source = std::fs::read_to_string(&abs)
        .with_context(|| format!("reading {}", abs.display()))?;
    let mut parser = new_cpp_parser()?;
    let tree = parser.parse(&source, None)
        .ok_or_else(|| anyhow!("parse failed for {}", abs.display()))?;
    let max = max_depth.unwrap_or(u32::MAX);
    Ok(build_tree_node(tree.root_node(), 0, max))
}

fn build_tree_node(node: tree_sitter::Node, depth: u32, max_depth: u32) -> TreeNode {
    let start = node.start_position();
    let end = node.end_position();
    let mut children = Vec::new();
    if depth < max_depth {
        let mut cursor = node.walk();
        for child in node.named_children(&mut cursor) {
            children.push(build_tree_node(child, depth + 1, max_depth));
        }
    }
    TreeNode {
        kind: node.kind().to_string(),
        start_line: start.row as u32 + 1,
        end_line: end.row as u32 + 1,
        start_col: start.column as u32,
        end_col: end.column as u32,
        children,
    }
}

pub fn get_symbol_def(root: &Path, name: &str, kind_filter: Option<&str>) -> Result<Vec<SymbolDef>> {
    let mut hits = Vec::new();
    for rel in list_files(root, None)? {
        let abs = root.join(&rel);
        let source = match std::fs::read_to_string(&abs) {
            Ok(s) => s,
            Err(_) => continue,
        };
        let mut parser = new_cpp_parser()?;
        let Some(tree) = parser.parse(&source, None) else { continue };
        walk(tree.root_node(), |node| {
            let k = node.kind();
            let is_def = matches!(k,
                "function_definition" | "class_specifier" | "struct_specifier"
                | "union_specifier" | "namespace_definition" | "enum_specifier"
                | "type_definition"
            );
            if !is_def {
                return;
            }
            if let Some(filter) = kind_filter {
                if k != filter {
                    return;
                }
            }
            if let Some(found_name) = find_name(node, &source) {
                if name_matches(found_name, name) {
                    hits.push(SymbolDef {
                        file: rel.clone(),
                        start_line: node.start_position().row as u32 + 1,
                        end_line: node.end_position().row as u32 + 1,
                        kind: k.to_string(),
                        name: found_name.to_string(),
                    });
                }
            }
        });
    }
    Ok(hits)
}

pub fn get_call_sites(root: &Path, name: &str) -> Result<Vec<CallSite>> {
    let mut hits = Vec::new();
    for rel in list_files(root, None)? {
        let abs = root.join(&rel);
        let source = match std::fs::read_to_string(&abs) {
            Ok(s) => s,
            Err(_) => continue,
        };
        let mut parser = new_cpp_parser()?;
        let Some(tree) = parser.parse(&source, None) else { continue };
        walk(tree.root_node(), |node| {
            if node.kind() != "call_expression" {
                return;
            }
            let Some(callee_node) = node.child_by_field_name("function") else { return };
            let callee_text = node_text(callee_node, &source);
            // Strip template arguments before comparison: `Foo<int>` → `Foo`.
            let bare = callee_text.split('<').next().unwrap_or(callee_text);
            // For `obj.foo`, `obj->foo`, `Foo::bar` — take the trailing identifier.
            let last_id = bare
                .rsplit("::").next().unwrap_or(bare)
                .rsplit("->").next().unwrap_or(bare)
                .rsplit('.').next().unwrap_or(bare)
                .trim();
            if last_id == name || name_matches(bare, name) {
                hits.push(CallSite {
                    file: rel.clone(),
                    line: node.start_position().row as u32 + 1,
                    callee: callee_text.to_string(),
                });
            }
        });
    }
    Ok(hits)
}
