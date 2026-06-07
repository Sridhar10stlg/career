# 03 — Technical Learning Plan

> Deep tracks for Python · SQL · Data Engineering · GoLang · AI Engineering.
> Rule for all tracks: **build something with each concept.** Reading without building = forgetting.

---

## Track 1: Python

Your goal: go from "competent + LLM-assisted" to "I own every line and could write it on a whiteboard."

### 1.1 Fundamentals (refresh, ~2 weeks)
- Data types, mutability, truthiness, comprehensions, generators.
- Functions: args/kwargs, closures, decorators, scoping.
- Error handling, context managers (`with`), iterators.
- **Drill:** re-implement common builtins (`map`, `filter`, a simple `defaultdict`) from scratch, no LLM.

### 1.2 OOP (your weak spot — spend real time)
- Classes, `__init__`, instance vs class vs static methods.
- Dunder methods (`__repr__`, `__eq__`, `__hash__`, `__iter__`, `__enter__/__exit__`).
- Composition vs inheritance (prefer composition), mixins, ABCs.
- `dataclasses`, `@property`, encapsulation patterns.
- **Project:** build a small library *as classes* — e.g., a config-driven ETL mini-framework (you already think this way at work; now own the OOP).

### 1.3 Advanced Python
- Typing: `typing`, generics, `Protocol`, `TypedDict`, mypy/pyright.
- Concurrency: threading vs multiprocessing vs asyncio; the GIL; when each wins.
- Generators/coroutines deeply; `itertools`, `functools`.
- Memory model, references, `__slots__`.

### 1.4 Design Patterns (in Python idiom)
- Creational: factory, builder, singleton (and why singletons are often bad).
- Structural: adapter, decorator, facade.
- Behavioral: strategy, observer, command.
- **Map each to your real work** (e.g., strategy pattern = your config-driven ETL transforms).

### 1.5 Testing (you almost certainly under-do this)
- `pytest`, fixtures, parametrize, mocking, coverage.
- Unit vs integration; testing data pipelines (small fixtures, golden files).
- A taste of TDD: write the test first for one module.

### 1.6 Performance
- Profiling (`cProfile`, `line_profiler`), Big-O awareness in real code.
- Vectorization (numpy/pandas/polars), avoiding Python loops on big data.
- When to drop to PySpark vs single-node (polars/duckdb).

### 1.7 Enterprise Python
- Packaging (`pyproject.toml`, `uv`/`poetry`), virtual envs.
- Structure: src layout, modules, config management (pydantic-settings).
- Logging, observability, CLI (typer/click), API (FastAPI).
- CI (GitHub Actions: lint+test+type-check).

**Python milestones:** (1) a tested, typed, packaged mini-framework; (2) can explain GIL + concurrency choices; (3) you stop reaching for an LLM to write a class.

---

## Track 2: SQL

Your stack lives on SQL. Aim for "I can out-SQL most people in the room."

### 2.1 Beginner→Advanced (refresh fast)
- Joins (all types, anti/semi), aggregation, `GROUP BY`/`HAVING`, set ops.
- Subqueries vs CTEs vs derived tables.

### 2.2 Window Functions (master these — interview + work gold)
- `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`/`LEAD`, `NTILE`.
- Running totals, moving averages, frames (`ROWS BETWEEN`).
- Gaps-and-islands, deduplication, top-N-per-group.

### 2.3 Query Optimization
- Read execution plans (`EXPLAIN` / `EXPLAIN ANALYZE`).
- Indexes (B-tree, when they help/hurt), partition pruning.
- Snowflake: micro-partitions, clustering keys, result cache, warehouse sizing.
- Avoiding spills, predicate pushdown, broadcast vs shuffle joins.

### 2.4 Data Warehouse SQL
- Star/snowflake schemas, fact/dimension queries, SCD handling in SQL.
- Incremental/merge (`MERGE`/upsert), idempotent loads.

### 2.5 Analytics SQL
- Cohort analysis, funnels, retention, sessionization, time-series rollups.
- `QUALIFY` (Snowflake), pivot/unpivot, arrays/structs/semi-structured (`VARIANT`, `LATERAL FLATTEN`).

### 2.6 Interview SQL
- 50–60 hard SQL problems (window-heavy). Use StrataScratch / DataLemur / LeetCode DB.

**SQL milestones:** solve any top-N-per-group, gaps-and-islands, and cohort question cold; read and improve a slow query plan.

---

## Track 3: Data Engineering

You have real experience here — this track is about **depth, scale, and rigor**, not basics.

### 3.1 Batch
- Idempotency, backfills, late-arriving data, partitioning strategy.
- Orchestration: Airflow **or** Dagster — build real DAGs (retries, sensors, SLAs).
- File formats: Parquet, Delta, Iceberg — and *why* (columnar, predicate pushdown, time travel).

### 3.2 Streaming
- Kafka fundamentals (topics, partitions, offsets, consumer groups, delivery semantics).
- Spark Structured Streaming (watermarks, windows, stateful ops, exactly-once-ish).
- Batch vs streaming trade-offs; Lambda vs Kappa.

### 3.3 Data Modeling
- Kimball dimensional modeling (deep): facts, dims, grain, SCD types 1/2/3.
- Data Vault basics (when/why), normalization vs denormalization for analytics.
- One Big Table vs star for modern lakehouses.

### 3.4 Lakehouse
- Medallion (bronze/silver/gold) done rigorously (you do this — formalize it).
- Delta/Iceberg internals: transaction log, ACID, time travel, OPTIMIZE/Z-ORDER/compaction.
- Databricks + Snowflake architecture trade-offs (you know both — articulate when each wins).

### 3.5 Governance
- Catalogs (Unity Catalog), access control, data classification, PII handling.
- Lineage, auditability, compliance basics (GDPR-style thinking).

### 3.6 Data Quality
- Tests/expectations (Great Expectations / dbt tests / Soda).
- Data contracts, SLAs/SLOs for data, anomaly detection, freshness checks.

### 3.7 MDM & Metadata
- You have MDM experience — formalize: match/merge, survivorship, golden records, hierarchies.
- Metadata management, data catalog, semantic layer concepts.

**DE milestones:** P1 (medallion), P3 (streaming + contracts) from [02](02-three-year-roadmap.md); can defend Databricks-vs-Snowflake and batch-vs-streaming with trade-offs.

---

## Track 4: GoLang (absolute beginner — deliberate, Year 1+)

> Why Go: it teaches you *systems thinking, concurrency done right, and explicitness* — the antidote to LLM-leaning Python habits. It's also valued for infra/platform/backend roles. Keep it *small and real*; don't let it crowd out fundamentals.

### Learning order
1. **Syntax & types:** variables, structs, slices, maps, functions, pointers (Go forces you to understand pointers — good).
2. **Idioms:** error handling (`error` values, not exceptions), interfaces (implicit), composition.
3. **Concurrency (Go's superpower):** goroutines, channels, `select`, `sync` (WaitGroup, Mutex), context.
4. **Tooling:** modules, testing (`testing` pkg, table-driven tests), `go fmt`, benchmarks.
5. **Std lib:** `net/http`, `encoding/json`, `io`.

### Projects (in order)
- **G1:** CLI tool — e.g., a log parser or a CSV→Parquet-ish transformer (mirrors your data world).
- **G2:** Concurrent worker pool — fetch/process N things with goroutines + channels (this *is* the lesson).
- **G3:** A small REST API service with tests (FastAPI's spiritual cousin).
- **G4 (stretch):** A tiny high-throughput data ingestion service or a Kafka consumer in Go.

### Milestones
- Explain goroutines vs threads and channels vs locks.
- Ship one Go service with table-driven tests.

### Enterprise use cases (why it matters)
- High-throughput data ingestion/edge services, CLIs/internal tooling, Kubernetes/cloud-native infra (most of it is Go), microservices where Python's GIL/latency hurts.

### Resources
- *A Tour of Go* (official) → *Learn Go with Tests* (free, excellent, TDD-based — also fixes your testing gap) → *The Go Programming Language* (Donovan/Kernighan) for depth.

---

## Track 5: AI Engineering (your spike — go deepest here)

> This is your differentiator. The market is moving from "demos" to "reliable, evaluated, governed, cost-controlled production AI." Live on the production side.

### 5.1 LLM Fundamentals
- Tokens, embeddings, context windows, temperature/sampling, prompting patterns.
- How transformers work (intuition, not from scratch), fine-tuning vs prompting vs RAG (when each).
- Structured outputs, function/tool calling, JSON-mode reliability.

### 5.2 RAG (do it *properly* — most people don't)
- Chunking strategies, embedding models, vector stores (and when you *don't* need one).
- Hybrid retrieval (BM25 + vector), reranking, query rewriting, metadata filtering.
- Evaluation: faithfulness, answer relevance, context precision/recall (RAGAS-style).
- Failure modes: hallucination, lost-in-the-middle, stale data.

### 5.3 MCP (Model Context Protocol)
- What it is, why it matters (standardized tool/context interfaces for agents).
- Build an MCP server exposing a data source + an MCP client that uses it.
- Ties directly to your agentic work — make this a public artifact.

### 5.4 Agentic AI
- Agent loops (ReAct, plan-execute), tools, memory, reflection.
- Frameworks: LangGraph / your Mosaic AI / Agentfield experience — and *when to use no framework*.
- Reliability: retries, guardrails, fallbacks, human-in-the-loop, cost/latency control.

### 5.5 Multi-Agent Systems
- Orchestration patterns (supervisor/worker, debate, hierarchical).
- Communication, shared state, when multi-agent actually beats single-agent (often it doesn't — know when).

### 5.6 Evaluation Frameworks (your secret weapon)
- Offline eval (golden datasets, LLM-as-judge + its pitfalls), online eval (A/B, user feedback).
- Metrics for RAG and agents; regression testing for prompts; eval-driven development.
- **This is the skill that separates senior AI engineers from prompt jockeys. Own it.**

### 5.7 Production AI Systems (LLMOps)
- Observability/tracing (LangSmith/Langfuse/OpenTelemetry), prompt versioning.
- Cost optimization (caching, model routing, smaller models where they suffice), latency.
- Security: prompt injection, data exfiltration, PII, guardrails, access control.
- Deployment, monitoring, drift, feedback loops.

**AI milestones:** P2 (RAG + eval harness) and P6 (enterprise agentic ref architecture) from [02](02-three-year-roadmap.md). You can speak about *evaluation and reliability*, not just capabilities — that's the senior signal.

---

## How the tracks sequence (so you don't try to do all five at once)

| Period | Primary track(s) | Secondary |
|---|---|---|
| Months 1–3 | Python (OOP/fundamentals), SQL (windows) | DSA (separate, daily) |
| Months 4–6 | AI Engineering (RAG+eval), Spark depth | Python (testing/advanced) |
| Months 7–12 | Data Eng (streaming, governance), Cloud | GoLang (start), System design |
| Year 2 | Architecture, AI (agents/multi-agent), GoLang depth | Consulting |
| Year 3 | AI frontier, public artifacts | Maintenance of all |

> Never run more than **2 deep tracks + DSA** at once. More than that and you'll finish none.
