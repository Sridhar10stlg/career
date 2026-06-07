# 01 — Current Assessment & Gap Analysis

> Re-run this every quarter. Date each run. Honesty here is the whole game.

---

## Part 1: Current Assessment (June 2026)

### Context that frames everything

You have **~22 months of experience** (GET Aug 2024 → SE Aug 2025 → Systems Designer Apr 2026). That is **fast progression** — three titles in under two years is unusual and is a genuine signal. But understand what it means and doesn't mean:

- It means: Psiog rates you, you ship, you've been trusted with bigger scope quickly.
- It does **not** mean: you have the *depth* that someone with 4–5 years at a strong eng-culture company has. Title inflation is common in services/consulting firms. The market will calibrate you on **demonstrated depth**, not your title.

This gap — *real talent + fast title growth, but thin foundational depth* — is the single most important thing about your current position. Everything below flows from it.

### Strengths

1. **Modern, in-demand stack.** Snowflake + Databricks + PySpark + Python + SQL is exactly the 2026 data-engineering core. You're not learning yesterday's tools.
2. **Real end-to-end delivery.** An MDM-based data exchange pipeline, config-driven ETL frameworks, Python integrations — these are *systems*, not tutorials. Most people your age have only done toy projects.
3. **You're already in the AI wave early.** Agentic AI, Databricks Mosaic AI, dataset-agnostic agents, agentic workflows, MCP-adjacent work. This is the highest-leverage skill area in the market right now and you have a head start.
4. **Breadth across the value chain.** Data engineering → modeling → warehousing → BI evaluation → AI. You can see the whole pipeline, which is rare and is the *seed* of architect/consultant thinking.
5. **Self-awareness.** This document exists because you asked for a brutally honest plan. That meta-skill compounds.

### Weaknesses (your stated ones, sharpened)

1. **DSA — weak, ~2 years cold.** This is your hardest *gateway* blocker for MAANG-tier roles. Not because the job uses DSA daily, but because the interview filter is real and unforgiving.
2. **OOP & coding fundamentals — shaky, LLM-dependent.** This is the most dangerous one. Over-reliance on LLMs is hollowing out the exact muscle (writing correct code from first principles) that architecture and senior interviews test. You can *produce* code but may not deeply *own* it.
3. **Problem solving / logical rigor.** Related to #1 and #2. You can pattern-match but struggle to derive.
4. **Questioning ability / analytical thinking.** This is the consultant's core skill and you've correctly identified it as missing.
5. **Consulting communication — stakeholder, exec storytelling.** Expected at 22 months; this is a Year 2–3 build, not a now-crisis.

### Career risks (the ones that will actually hurt you)

- **R1 — The "LLM-dependency trap."** If you keep outsourcing thinking to LLMs, in 2 years you'll have a senior title and a junior's actual capability. The market is *flooding* with people who can prompt; it is *starving* for people who deeply understand systems. Do not be in the first group.
- **R2 — Services-firm depth ceiling.** Psiog gives you breadth and client variety but may not push the *engineering rigor* (code review culture, testing discipline, scale) that product companies have. You must manufacture that rigor yourself.
- **R3 — Breadth without a spike.** You're broad. Broad-and-shallow is a generalist; broad-and-spiky is an architect. Without one undeniable area of depth, you read as "jack of all trades."
- **R4 — Title-reality mismatch in interviews.** "Systems Designer with 2 years" sets a high expectation bar. If your fundamentals don't back the title, strong interviewers will notice fast.
- **R5 — Roadmap-collector syndrome.** Reading/planning instead of building. (Ironic given this document — so: this is the last plan you write for a while. Now you execute.)

### Missing skills (objective inventory)

| Area | Status | Priority |
|------|--------|----------|
| DSA (patterns, not memorization) | Cold | **Critical (interview gate)** |
| CS fundamentals (OS, networking, concurrency basics) | Thin | High |
| OOP + design patterns (applied) | Shaky | **Critical (depth)** |
| Testing discipline (unit/integration, TDD-ish) | Likely thin | High |
| Distributed systems theory (CAP, consistency, partitioning) | Unknown/thin | High (architect gate) |
| System design (interview + real) | Beginner | **Critical** |
| Cloud depth (one of AWS/Azure/GCP, deep) | Likely broad-shallow | High |
| Streaming (Kafka/Flink/Spark Structured Streaming) | Likely batch-heavy | Medium-High |
| Data governance / lineage / contracts | Partial (MDM helps) | Medium |
| Production AI/LLMOps (eval, guardrails, cost, latency) | Emerging | **High (your spike)** |
| GoLang | Zero | Medium (deliberate, Year 1+) |
| Consulting / exec comms | Thin | Medium (Year 2 ramp) |
| Writing/communicating publicly | Unknown | Medium-High |

### Market positioning (2026)

- **The data-engineering market** has matured: pure ETL is commoditizing; the premium is on **lakehouse architecture, data quality/contracts, and cost/performance at scale**.
- **The AI-engineering market** is white-hot but rapidly professionalizing — moving from "can you build a RAG demo" to "can you ship a reliable, evaluated, cost-controlled, governed AI system in production." **This convergence (Data Eng + AI Eng) is your single best bet.** Very few people are genuinely strong at both, and *every* enterprise AI system is bottlenecked on data engineering.
- **Where you sit:** top ~30% of 2-year engineers on stack/breadth; bottom ~40% on fundamentals/DSA. The roadmap's job is to move you to **top 10% on fundamentals AND keep your stack/AI edge** → that combination is top-1%-architect material.

**Positioning statement to grow into (your future LinkedIn headline):**
> *"Data & AI Engineer specializing in production-grade agentic systems on the lakehouse — turning enterprise data into reliable, governed, business-impacting AI."*

---

## Part 2: Gap Analysis vs Target Roles

Scoring: each role rated on the dimensions that matter for it. **You (Jun 2026)** is your honest current level (1–5). **Bar** is what the role demands. **Gap** = work to close.

### 2.1 Senior Data Engineer (your nearest realistic target, ~12–24 mo)

| Dimension | You | Bar | Gap |
|---|---|---|---|
| SQL (advanced, optimization) | 3 | 4 | Window fns, query plans, tuning |
| Python (production, testing) | 3 | 4 | OOP rigor, tests, packaging |
| Spark/distributed processing | 3 | 4 | Tuning, partitioning, skew, memory |
| Lakehouse (Databricks/Snowflake) | 4 | 4 | ✅ near bar — *keep* |
| Data modeling (dim, vault) | 3 | 4 | Kimball depth, slowly-changing dims |
| Orchestration (Airflow/Dagster) | 2–3 | 4 | Build real DAGs, idempotency, retries |
| Streaming | 2 | 3–4 | Kafka + Structured Streaming |
| Data quality / contracts | 3 | 4 | Great Expectations / dbt tests, SLAs |
| CS fundamentals | 2 | 3 | Concurrency, memory, complexity |

**Verdict:** You're ~70% to Senior DE. **6–12 months of focused depth** closes it. This is your fastest, most certain win — anchor here first.

### 2.2 Staff Data Engineer

| Dimension | You | Bar | Gap |
|---|---|---|---|
| Everything in Senior, deeper | 3 | 5 | Scale, edge cases, war stories |
| System design (data platforms) | 2 | 5 | **Large gap** |
| Cross-team technical leadership | 2 | 4 | Influence, mentoring, RFCs |
| Driving standards/frameworks | 3 | 4 | You've built frameworks — lean in |
| Ambiguity → architecture | 2 | 5 | Big gap |
| Cost/reliability ownership | 2 | 4 | SLOs, FinOps for data |

**Verdict:** ~18–36 months *after* hitting Senior. Staff is about org-level impact and judgment, which needs time + scope you can partly manufacture (frameworks, RFCs) but partly must earn.

### 2.3 Solution Architect

| Dimension | You | Bar | Gap |
|---|---|---|---|
| Breadth across stack | 4 | 4 | ✅ strength |
| Deep in ≥1 domain | 3 | 4 | Pick AI-on-lakehouse spike |
| System/solution design | 2 | 5 | **Large gap** |
| Cloud architecture (1 deep) | 3 | 4 | Certify + build (Azure or AWS) |
| Cost/trade-off reasoning | 2 | 5 | Big gap |
| Requirements → architecture | 2 | 5 | Discovery, NFRs |
| Stakeholder communication | 2 | 5 | **Large gap** |
| Documentation (ADRs, diagrams) | 2 | 4 | Learn C4, ADRs |

**Verdict:** ~24–36 months. Your breadth is a real head start; the gaps are *design rigor* and *communication*. The roadmap builds both deliberately.

### 2.4 Technical Consultant

| Dimension | You | Bar | Gap |
|---|---|---|---|
| Business/domain fluency | 2 | 5 | **Large gap** |
| Stakeholder management | 2 | 5 | Large gap |
| Discovery / requirements | 2 | 5 | Large gap |
| ROI / business case | 1 | 5 | **Largest gap** |
| Exec storytelling | 1 | 5 | Largest gap |
| Technical credibility | 3 | 4 | You have the base |
| Structured thinking (MECE etc.) | 2 | 5 | See [07](07-thinking-frameworks.md) |

**Verdict:** ~30–42 months. This is the *latest-maturing* track and that's correct — consulting credibility rests on a foundation of having actually built and architected things first. Don't rush it.

### 2.5 MAANG / Top-Tier Engineer

| Dimension | You | Bar | Gap |
|---|---|---|---|
| DSA (interview) | 1–2 | 4 | **Critical gate** |
| System design (interview) | 2 | 4 | Critical |
| Coding fluency (no LLM) | 2 | 4 | **Critical** |
| Behavioral / leadership stories | 2 | 4 | STAR bank needed |
| Domain depth (Data/AI) | 3–4 | 4 | ✅ near bar |
| CS fundamentals | 2 | 4 | High |

**Verdict:** The domain depth is closer than you think; the **interview machinery (DSA + system design + coding-without-LLM)** is the wall. ~18–30 months of consistent prep makes you competitive. See [06](06-maang-prep.md).

### Cross-role summary: your 5 biggest gaps, ranked

1. **DSA + coding-without-LLM fluency** (gates MAANG + builds real depth) → start *now*.
2. **System / solution design** (gates Architect + Staff + MAANG) → start month 3.
3. **Production AI engineering depth** (your spike, your differentiator) → start *now*, continuous.
4. **Distributed-systems & CS fundamentals** (underpins everything senior) → months 1–12.
5. **Consulting communication / business fluency** (gates Consultant) → Year 2 ramp.

> **The unlock:** Gaps #1 and #2 feel like a slog and you'll be tempted to skip them for the fun AI work (#3). Don't. The people who pair AI-engineering flash with rock-solid fundamentals are vanishingly rare and command the top offers. That pairing is your entire thesis.
