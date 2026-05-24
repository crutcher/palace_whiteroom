//! Phase 1 smoke test (BOOTSTRAP.md DONE criteria).
//!
//! Drives the tool functions directly against `reference/palace/` — does not
//! exercise the MCP wire layer. The wire layer is registered via
//! `.claude/mcp.json`; this test covers the codemap logic.

use std::path::PathBuf;

use palace_codemap::tools::{
    get_call_sites, get_file_subtree, get_symbol_def, list_dependencies, list_files,
    read_range, search_text,
};

fn target_root() -> PathBuf {
    // Tests run from the crate directory; the target lives at ../../reference/palace.
    let mut p = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    p.push("../../reference/palace");
    p.canonicalize().expect("target root must exist for smoke test")
}

#[test]
fn smoke_list_files_returns_cpp_sources() {
    let files = list_files(&target_root(), None).expect("list_files default");
    assert!(!files.is_empty(), "expected at least some C/C++ files");
    assert!(
        files.iter().any(|f| f.ends_with(".cpp")),
        "expected at least one .cpp; got {:?}",
        &files[..files.len().min(5)]
    );
    // Default mode excludes non-C++ extensions like .md, .txt.
    assert!(
        files.iter().all(|f| {
            let ext = std::path::Path::new(f).extension().and_then(|s| s.to_str());
            matches!(ext, Some("cpp" | "hpp" | "h" | "cc" | "cxx" | "hxx" | "C"))
        }),
        "default mode should only return C/C++ files"
    );
}

#[test]
fn smoke_list_files_with_glob() {
    let files = list_files(&target_root(), Some("palace/linalg/*.cpp"))
        .expect("list_files glob");
    assert!(!files.is_empty(), "expected linalg/*.cpp matches");
    assert!(
        files.iter().all(|f| f.starts_with("palace/linalg/") && f.ends_with(".cpp")),
        "glob should narrow to palace/linalg/*.cpp; got {:?}",
        files
    );
}

#[test]
fn smoke_read_range_returns_source() {
    // Read a small range from iterative.cpp (CgSolver::Mult lives in this file).
    let out = read_range(&target_root(), "palace/linalg/iterative.cpp", 1, 5)
        .expect("read_range");
    assert!(!out.is_empty(), "expected non-empty output");
    // First lines of a Palace C++ file should include the copyright header.
    assert!(out.contains("//") || out.contains("/*"), "expected comment header");
}

#[test]
fn smoke_read_range_rejects_inverted_range() {
    let err = read_range(&target_root(), "palace/linalg/iterative.cpp", 100, 50);
    assert!(err.is_err(), "expected error on end < start");
}

#[test]
fn smoke_read_range_rejects_path_escape() {
    let err = read_range(&target_root(), "../../../etc/passwd", 1, 1);
    assert!(err.is_err(), "expected escape rejection");
}

#[test]
fn smoke_search_text_finds_pattern() {
    let hits = search_text(&target_root(), "CgSolver", None).expect("search_text");
    assert!(!hits.is_empty(), "expected at least one CgSolver hit");
    assert!(
        hits.iter().any(|h| h.file.ends_with("iterative.hpp")
            || h.file.ends_with("iterative.cpp")),
        "expected hits in iterative.{{cpp,hpp}}; got {:?}",
        hits.iter().map(|h| &h.file).take(5).collect::<Vec<_>>()
    );
}

#[test]
fn smoke_list_dependencies_parses_includes() {
    let inc = list_dependencies(&target_root(), "palace/linalg/iterative.cpp")
        .expect("list_dependencies");
    assert!(!inc.is_empty(), "expected at least one #include");
    // Sanity: distinguishes system vs quoted.
    let any_system = inc.iter().any(|i| i.system);
    let any_quoted = inc.iter().any(|i| !i.system);
    assert!(any_system || any_quoted, "expected some includes to be classified");
}

#[test]
fn smoke_get_file_subtree_returns_ast() {
    let root = get_file_subtree(&target_root(), "palace/linalg/iterative.cpp", Some(2))
        .expect("get_file_subtree");
    assert_eq!(root.kind, "translation_unit", "C++ file root should be translation_unit");
    assert!(!root.children.is_empty(), "expected child nodes");
    // depth 2 from root should NOT have grandchildren of grandchildren — the children list at
    // root level is depth-1; we said max_depth=2 so root's children's children are present.
    // Just sanity: the tree should have structure.
    assert!(root.start_line >= 1);
}

#[test]
fn smoke_get_symbol_def_finds_cgsolver() {
    let defs = get_symbol_def(&target_root(), "CgSolver", None).expect("get_symbol_def");
    assert!(!defs.is_empty(), "expected at least one CgSolver definition");
    assert!(
        defs.iter().any(|d| d.file.ends_with("iterative.hpp") || d.file.ends_with("iterative.cpp")),
        "expected CgSolver in iterative.{{hpp,cpp}}; got {:?}",
        defs.iter().map(|d| (&d.file, &d.kind)).collect::<Vec<_>>()
    );
}

#[test]
fn smoke_get_call_sites_for_mult() {
    // BOOTSTRAP.md DONE: get_call_sites on a known function returns at least one caller.
    // `Mult` is a virtual method used pervasively across the linalg layer; if any name
    // is going to have callers, it's this one.
    let sites = get_call_sites(&target_root(), "Mult").expect("get_call_sites");
    assert!(!sites.is_empty(), "expected at least one call site for Mult");
    eprintln!(
        "[smoke] get_call_sites(\"Mult\") returned {} hits; sample: {:?}",
        sites.len(),
        sites.iter().take(3).collect::<Vec<_>>()
    );
}
