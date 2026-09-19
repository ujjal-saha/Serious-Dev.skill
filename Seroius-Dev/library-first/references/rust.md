# Rust crates

Install with `cargo add <name>`. This updates `Cargo.toml`.
Check first whether the standard library already does the job: `std::fs`, `std::path`, `std::thread`, `std::sync`, `std::collections`, `std::time`, `std::env`.

| Package | Install | Use it for |
|---|---|---|
| serde | cargo add serde --features derive | convert structs to and from JSON, YAML, and other formats |
| serde_json | cargo add serde_json | read and write JSON |
| tokio | cargo add tokio --features full | async runtime, async network and timers |
| reqwest | cargo add reqwest --features json | HTTP client, GET, POST, downloads |
| axum | cargo add axum | web server, REST API |
| clap | cargo add clap --features derive | command-line arguments and options |
| anyhow | cargo add anyhow | simple error handling in applications |
| thiserror | cargo add thiserror | define custom error types |
| rand | cargo add rand | random numbers, shuffle, choose |
| regex | cargo add regex | regular expressions |
| chrono | cargo add chrono | dates, times, time zones |
| tracing | cargo add tracing tracing-subscriber | structured logging |
| rayon | cargo add rayon | run loops in parallel on all CPU cores |
| sqlx | cargo add sqlx | async SQL database queries |
| csv | cargo add csv | read and write CSV files |
| image | cargo add image | open, resize, save images |
