-- The 420 Code — canon schema (SQLite).
-- The executable "story bible" of G's work: axioms, proofs, predictions, kill switches,
-- and the dependency edges between them. A small queryable graph — a
-- queryable graph the gate re-ingests and audits — but the canon here is a physics
-- derivation, not a novel. Everything is rebuilt from the mirror; this DB is derived.

PRAGMA foreign_keys = ON;

-- The four founding axioms (S, B, R, C) + any paper-local axiom sets (e.g. AP02's A1–A6).
CREATE TABLE IF NOT EXISTS axiom (
    id          TEXT PRIMARY KEY,        -- 'S','B','R','C', or 'AP02:A1'
    symbol      TEXT NOT NULL,           -- 'S'
    name        TEXT NOT NULL,           -- 'Selection'
    statement   TEXT NOT NULL,           -- one-line definition
    family      TEXT NOT NULL DEFAULT 'core'  -- 'core' | paper id for paper-local axiom sets
);

-- The 42 Artist's Proofs (+ companion prose volumes), as the spine of the corpus.
CREATE TABLE IF NOT EXISTS proof (
    id          TEXT PRIMARY KEY,        -- 'AP01' .. 'AP42', or 'PROSE:Predictions'
    kind        TEXT NOT NULL,           -- 'proof' | 'prose'
    title       TEXT NOT NULL,           -- 'The Actualization State'
    part_no     TEXT,                    -- 'I'..'VIII' (proofs only)
    part_title  TEXT,                    -- 'The Premise'
    domain      TEXT,                    -- 'Axioms, foundations, logical proof'
    pdf         TEXT NOT NULL,           -- relative path under mirror/pdf/
    words       INTEGER,                 -- extracted word count
    ks_count    INTEGER DEFAULT 0        -- kill switches whose origin is this proof
);

-- Numeric predictions the gate actually EXECUTES (re-derives from α and checks vs measured).
-- Sourced from engine.verify (G's Appendix B). Stored for query/report; verify.py is the oracle.
CREATE TABLE IF NOT EXISTS prediction (
    key             TEXT PRIMARY KEY,    -- 'proton_electron_mass_ratio'
    part            TEXT NOT NULL,       -- 'I'
    name            TEXT NOT NULL,
    formula         TEXT NOT NULL,
    predicted       REAL NOT NULL,
    measured        REAL NOT NULL,
    unit            TEXT NOT NULL,
    residual        REAL NOT NULL,
    residual_unit   TEXT NOT NULL,       -- 'ppb' | 'ppm' | '%'
    tolerance       REAL NOT NULL,
    measured_source TEXT NOT NULL,
    passed          INTEGER NOT NULL     -- 1/0 at ingest time
);

-- The kill-switch registry: G's published falsification conditions. The heart of "testable".
-- Beyond id+status, each switch carries G's own STRUCTURE: a published TYPE (kind_token —
-- EMPIRICAL / HARD / STRUCTURAL / NON-NEGOTIABLE / DEPENDENT / DEBT / MATHEMATICAL / …), the
-- verbatim fire-condition (the exact trigger as written), and weight flags (moral/non-negotiable,
-- global, "sharpest test"). These are extracted deterministically from the per-proof bodies so the
-- model mirrors his falsification structure, not merely his counts.
CREATE TABLE IF NOT EXISTS kill_switch (
    id          TEXT PRIMARY KEY,        -- 'KS-V.1', 'KS-30.4', 'KS-Q.7' ...
    description TEXT NOT NULL,           -- name + condition (human-readable)
    fire_condition TEXT,                 -- the verbatim trigger sentence(s), as G wrote them
    status      TEXT NOT NULL,           -- 'LIVE' | 'CLOSED' | 'COND_CLOSED' | 'ADDRESSED' | 'OPEN_DEBT'
    status_raw  TEXT,                    -- e.g. 'LIVE — NON-NEGOTIABLE'
    kind_token  TEXT,                    -- G's published TYPE token, verbatim (EMPIRICAL/HARD/…)
    test_kind   TEXT,                    -- canonical bucket: empirical|structural|logical|theoretical
    origin      TEXT,                    -- originating proof, e.g. 'AP01 A' / 'AP15'
    section     TEXT NOT NULL,           -- 'physics' | 'philosophy' | 'oh_models'
    non_negotiable INTEGER DEFAULT 0,    -- a moral / NON-NEGOTIABLE switch (forbids a USE, not just falsifies)
    sharpest    INTEGER DEFAULT 0,       -- G flags it the "sharpest test" of its proof
    global      INTEGER DEFAULT 0        -- a declared GLOBAL kill switch (e.g. KS-V.1)
);

-- Dependency / provenance edges (queryable graph): proof→axiom, prediction→proof, ks→proof.
CREATE TABLE IF NOT EXISTS edge (
    src     TEXT NOT NULL,   -- e.g. 'AP10'
    dst     TEXT NOT NULL,   -- e.g. 'R'
    rel     TEXT NOT NULL,   -- 'uses_axiom' | 'predicts' | 'falsified_by' | 'in_part'
    PRIMARY KEY (src, dst, rel)
);

-- Provenance / corpus-level facts (the registry's own declared counts, versions, deltas).
CREATE TABLE IF NOT EXISTS corpus_fact (
    key     TEXT PRIMARY KEY,
    value   TEXT NOT NULL
);
