//! Minimal loader for the agent-loop `config.toml`. Only fields the codemap
//! server needs are parsed; unknown fields are tolerated.

use anyhow::{Context, Result};
use serde::Deserialize;
use std::path::Path;

#[derive(Debug, Deserialize)]
pub struct Config {
    pub target: TargetConfig,
}

#[derive(Debug, Deserialize)]
pub struct TargetConfig {
    /// Filesystem path to the target repo clone, relative to the directory
    /// containing `config.toml` (or absolute).
    pub repo: String,
    /// Target source language. For now only `"cpp"` is supported by this
    /// server; other languages would require a different grammar.
    #[allow(dead_code)] // Reserved for future grammar dispatch; presently we hard-code cpp.
    pub language: String,
}

impl Config {
    pub fn load(path: &Path) -> Result<Self> {
        let contents = std::fs::read_to_string(path)
            .with_context(|| format!("reading config at {}", path.display()))?;
        let cfg: Config = toml::from_str(&contents)
            .with_context(|| format!("parsing config at {}", path.display()))?;
        Ok(cfg)
    }
}
