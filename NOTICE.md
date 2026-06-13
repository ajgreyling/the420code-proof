# Notice — whose work is whose

This repository contains **two separable things**, under two different terms.

## 1. The tooling (this repo's code) — © 2026 Andries J. Greyling, MIT

Everything under `engine/`, `canon/schema.sql`, `mirror/fetch.sh`, `run.sh`, and the docs is the
author's own work, released under the [MIT License](LICENSE). Use it, fork it, build on it.

## 2. The theory under test — *The 420 Code*, © G / Studio G, CC BY 4.0

The subject of this evaluation — the *420 Code* corpus (the 42 Artist's Proofs, the prose volumes,
the Master Kill Switch Registry, and G's own `verify.py`) — is the work of **G**, published at
**[the420code.org](https://the420code.org)** under **CC BY 4.0**, DOI
[10.5281/zenodo.19208226](https://doi.org/10.5281/zenodo.19208226).

**This repository does not redistribute G's corpus.** It is *fetched on demand* from G's own site
(`./run.sh mirror`), which explicitly welcomes machine ingestion (its `robots.txt` admits ClaudeBot,
anthropic-ai, et al., and it ships an `llms.txt`). The downloaded PDFs and everything derived from
them (`mirror/pdf/`, `extract/`, the built `*.db`) are git-ignored and never committed here.

All credit for the theory — and any glory if it holds — is **G's**. This repo is only the
independent check: one axiom, one measured input, zero fitted parameters, run by someone who is not
the author and had no hand in the derivation.

> *One axiom. One measured input. Zero free parameters.*
> *Either the best fraud I've ever met, or a name alongside Bohr, Einstein, Tesla. Here is how you
> find out for yourself.*
