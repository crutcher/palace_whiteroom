//! Tree-sitter helpers — parser construction and traversal.

use anyhow::{Context, Result};
use tree_sitter::{Node, Parser};

/// Build a fresh tree-sitter parser configured for C++.
///
/// Parsers are not cheap to spin up *and* not Send-safe across awaits, so each
/// async tool invocation that needs one constructs its own.
pub fn new_cpp_parser() -> Result<Parser> {
    let mut parser = Parser::new();
    parser
        .set_language(&tree_sitter_cpp::LANGUAGE.into())
        .context("setting tree-sitter cpp language")?;
    Ok(parser)
}

/// Depth-first pre-order traversal of all descendant nodes (including root).
///
/// `visit` is called once per node. Uses `TreeCursor` rather than recursion to
/// avoid stack blow-up on deeply nested templates.
pub fn walk<F: FnMut(Node)>(root: Node, mut visit: F) {
    let mut cursor = root.walk();
    loop {
        visit(cursor.node());
        if cursor.goto_first_child() {
            continue;
        }
        loop {
            if cursor.goto_next_sibling() {
                break;
            }
            if !cursor.goto_parent() {
                return;
            }
        }
    }
}

/// Extract the textual name from a node assumed to be an identifier-like node.
///
/// Falls back to the node's full source span if the node has unexpected
/// structure (e.g., a `qualified_identifier` whose final segment is itself
/// nested). The caller is expected to match by suffix when comparing
/// qualified names.
pub fn node_text<'src>(node: Node, source: &'src str) -> &'src str {
    &source[node.byte_range()]
}

/// For a node whose conceptual "name" is a child, find that child's text.
///
/// Tree-sitter's C++ grammar puts names in various places depending on the
/// outer node kind. This helper centralizes the lookup.
pub fn find_name<'src>(node: Node, source: &'src str) -> Option<&'src str> {
    // Most `*_definition` nodes have an explicit `name` field.
    if let Some(name_node) = node.child_by_field_name("name") {
        return Some(node_text(name_node, source));
    }

    // `function_definition` doesn't have a top-level `name` field — the name
    // lives inside the `declarator` subtree, typically as an `identifier`,
    // `field_identifier`, or `qualified_identifier` at the deepest position.
    if let Some(declarator) = node.child_by_field_name("declarator") {
        return find_declarator_name(declarator, source);
    }

    None
}

/// Walk into a `*_declarator` subtree to find the innermost name node.
fn find_declarator_name<'src>(node: Node, source: &'src str) -> Option<&'src str> {
    // The declarator nesting: function_declarator → ... → identifier
    //                       | pointer_declarator → declarator → ...
    //                       | reference_declarator → declarator → ...
    //                       | ...
    let mut current = node;
    loop {
        match current.kind() {
            "identifier" | "field_identifier" | "qualified_identifier"
            | "operator_name" | "destructor_name" => {
                return Some(node_text(current, source));
            }
            _ => {}
        }
        if let Some(inner) = current.child_by_field_name("declarator") {
            current = inner;
            continue;
        }
        // Try the first named child as a fallback for nodes that don't
        // expose a `declarator` field.
        if let Some(first) = current.named_child(0) {
            current = first;
            continue;
        }
        return None;
    }
}

/// Whether a qualified or simple name `candidate` matches a requested `target`.
///
/// Match rules:
/// - Exact equality: `Foo::Bar` == `Foo::Bar`.
/// - Suffix-after-`::`: `Foo::Bar` matches target `Bar`.
/// - Plain identifier match.
///
/// This is intentionally lenient — call sites and definitions for the same
/// symbol can appear in either qualified or unqualified form depending on the
/// surrounding scope.
pub fn name_matches(candidate: &str, target: &str) -> bool {
    if candidate == target {
        return true;
    }
    if let Some(tail) = candidate.rsplit("::").next() {
        if tail == target {
            return true;
        }
    }
    false
}
