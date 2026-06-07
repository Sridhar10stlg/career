# 02 — Three-Year Roadmap

> Phases overlap. Dates anchored to **June 2026**. Each phase has: Goals · Skills · Projects · Books · Certs (only if worth it) · Deliverables · Outcome.

---

## Theme of each year

- **Year 1 (Jun 2026 – Jun 2027): FOUNDATIONS + SPIKE.** Fix fundamentals (DSA, OOP, CS), go deep on Data+AI engineering, start system design. *Become undeniably strong hands-on.*
- **Year 2 (Jun 2027 – Jun 2028): ARCHITECTURE + SCALE.** Solution/system design for real, cloud depth, lead frameworks, begin consulting communication. *Become an architect-in-practice.*
- **Year 3 (Jun 2028 – Jun 2029): POSITIONING + LEVERAGE.** Public portfolio, consulting fluency, MAANG interview machine, job-switch execution. *Become hireable at the top tier.*

---

## PHASE A — Next 3 Months (Jun – Sep 2026)

**Mission:** Stop the bleeding on fundamentals; build the daily habit; ship one strong portfolio project.

### Goals
- Re-establish DSA muscle (patterns, not grinding 500 problems).
- Write code *without* an LLM for fundamentals practice (LLM allowed only for unfamiliar APIs, never for logic).
- Solidify Python OOP and SQL window functions.
- Ship **one** flagship project to GitHub with a real README.

### Skills
- DSA: arrays, strings, hashing, two pointers, sliding window, binary search, recursion, basic trees.
- Python OOP: classes, dunder methods, composition vs inheritance, dataclasses, typing.
- SQL: window functions, CTEs, query plans (EXPLAIN).
- Git/GitHub hygiene, clean READMEs, basic CI.

### Projects
- **P1 — "Lakehouse-in-a-box" data pipeline** (your flagship). Ingest a public dataset → bronze/silver/gold (medallion) on Databricks or DuckDB+Delta locally → dbt-style tests → one BI view. Config-driven (lean on your existing ETL-framework experience). *This is your proof-of-depth artifact.*

### Books (read 1, skim 1)
- *Fluent Python* (Ramalho) — selected chapters on OOP/data model. **(primary)**
- *Grokking Algorithms* (Bhargava) — fast DSA intuition reboot. **(skim/parallel)**

### Certs
- **None yet.** Build first. (Cert hunting now = procrastination.)

### Deliverables
- Flagship repo (P1) live with README + architecture diagram.
- ~120–150 DSA problems' worth of *pattern* coverage (quality > count; see [06](06-maang-prep.md)).
- A `LEARNING-LOG.md` you update weekly (this is your accountability artifact).

### Expected Outcome
> You can solve easy/medium DSA from patterns without panic, write a clean Python class from scratch, and you have one repo you're proud to show. The LLM-dependency habit is visibly weakening.

---

## PHASE B — Next 6 Months (cumulative: Jun – Dec 2026)

**Mission:** Convert fundamentals into fluency; begin system design; ship your AI-engineering spike project.

### Goals
- DSA at solid medium level across core patterns + intro to graphs/DP.
- Start **system design** seriously (HLD basics, back-of-envelope, core building blocks).
- Ship a **production-grade AI project** (your differentiator).
- Deepen Spark performance and one cloud (pick Azure or AWS).

### Skills
- DSA: trees, graphs (BFS/DFS), heaps, intervals, intro DP.
- System design: load balancing, caching, queues, DB choice, sharding, CAP, back-of-envelope.
- AI eng: RAG done *properly* (chunking, hybrid retrieval, reranking, eval), guardrails, cost/latency.
- Spark: partitioning, shuffle, skew, broadcast joins, caching, AQE.

### Projects
- **P2 — Production RAG/agentic system** with **evaluation harness** (this is the project that sets you apart): a domain-specific assistant with retrieval + an eval suite (faithfulness, relevance, latency, cost dashboards) + guardrails. Document trade-offs. Tie to your Agentic AI / Mosaic AI experience.

### Books
- *Designing Data-Intensive Applications* (Kleppmann) — **the** book. Start it; you'll be on it for months. **(primary, long-running)**
- *Designing Machine-Learning Systems* (Huyen) — for the AI/production mindset.

### Certs
- **Databricks Certified Data Engineer Associate** — *worth it* (validates your daily stack, helps externally). Optional but cheap leverage.

### Deliverables
- P2 repo with eval dashboards + a blog post explaining it (your first public writing).
- System-design notes repo (your own HLD playbook).
- 250+ DSA problems of pattern coverage cumulatively.

### Expected Outcome
> You can design a basic distributed system on a whiteboard, you've shipped a *measured* AI system (not a demo), and you've published once. You now read as "strong hands-on Data+AI engineer." **Phase 1 of your vision is essentially achieved.**

---

## PHASE C — Next 12 Months (cumulative: Jun 2026 – Jun 2027)

**Mission:** Architect-in-training. Distributed systems depth, real cloud architecture, GoLang kickoff, first architecture artifacts. Begin interview readiness.

### Goals
- DSA: comfortable with most mediums, some hards; can pass a screening round.
- System design: can design data platforms + AI systems end-to-end with trade-offs.
- Cloud: one cloud deep + certified.
- Start GoLang (deliberate, small).
- Produce architecture documents (ADRs, C4 diagrams) for your projects.

### Skills
- Distributed systems: consistency models, consensus (intuition), partitioning, replication, idempotency, exactly-once.
- Streaming: Kafka + Spark Structured Streaming (a real streaming project).
- Architecture: C4 model, ADRs, NFRs, trade-off matrices.
- GoLang: syntax → concurrency (goroutines/channels) → a small CLI/service.

### Projects
- **P3 — Streaming + lakehouse pipeline** (Kafka → Structured Streaming → Delta → serving). Add data-quality contracts.
- **P4 — Architecture portfolio doc**: take P1/P2/P3 and write proper architecture docs (C4 + ADRs + trade-offs). This is what architects actually produce.
- **P5 (Go, small):** a Go CLI tool or a tiny high-throughput API — proof you can pick up a systems language.

### Books
- Finish *DDIA*.
- *The Pragmatic Programmer* (Hunt/Thomas) — craft & professionalism.
- *Fundamentals of Data Engineering* (Reis/Housley) — fills any DE conceptual gaps.

### Certs
- **One cloud cert** — Azure (DP-203 successor / Azure Data Engineer) **or** AWS (Data Engineer Associate). Pick the cloud your clients/market use most.

### Deliverables
- 3–4 strong repos + architecture docs.
- 2–3 blog posts published.
- Cloud cert.
- A polished LinkedIn + GitHub presence.

### Expected Outcome
> You're a strong Senior-DE-level engineer with an AI spike and emerging architecture skills. You could pass a Senior DE / AI Engineer loop at many strong companies. **Phase 2 (architecture) has begun in earnest.**

---

## PHASE D — Year 2 (Jun 2027 – Jun 2028)

**Mission:** Become an architect in practice and start the consulting build. Get interview-ready for top tier.

### Goals
- Lead an architecture/framework effort at Psiog (or drive one if not handed to you).
- System design at strong-senior/staff interview level.
- Begin consulting skills: discovery, stakeholder comms, ROI, exec storytelling.
- Deepen GoLang to "can build a real service."
- Run a full MAANG interview-prep cycle (DSA + design + behavioral).

### Skills
- Solution architecture: multi-system designs, integration patterns, security/compliance basics, cost modeling.
- Enterprise architecture intro: domains, capability maps, TOGAF concepts (lightly).
- Consulting: requirement gathering, discovery workshops, business cases, ROI models (see [05](05-consulting-roadmap.md)).
- Communication: written design docs, presentations, executive summaries (Pyramid Principle — see [07](07-thinking-frameworks.md)).

### Projects
- **P6 — A full reference architecture** for "Enterprise Agentic AI on the Lakehouse" — design doc + working slice + cost model + ROI narrative. This single artifact spans engineer + architect + consultant. **Your magnum opus.**
- Contribute to / lead a real internal framework or reusable asset at Psiog.

### Books
- *Software Architecture: The Hard Parts* (Ford et al.).
- *The Pyramid Principle* (Minto) — consulting communication.
- *Storytelling with Data* (Knaflic).

### Certs (only if strategic)
- Optional: a 2nd cloud at associate level *only if* it serves a real target. Otherwise skip.

### Deliverables
- P6 reference architecture (public-safe version on GitHub/blog).
- A talk or internal presentation delivered (exec-style).
- STAR behavioral story bank (10–12 stories).
- Mock interviews logged (DSA + system design).

### Expected Outcome
> You operate as a Solution-Architect-in-practice, you've communicated to stakeholders, and you're interview-ready. You can credibly apply to Senior/Staff DE, AI Engineer, or Solutions Architect roles at top-tier companies. **Phases 2 & 3 are live.**

---

## PHASE E — Year 3 (Jun 2028 – Jun 2029)

**Mission:** Convert capability into outcome — top-tier offer and/or consulting positioning. Establish public authority.

### Goals
- Run an active, deliberate job search at top-tier companies (or strategically reposition at/above current).
- Establish public credibility (blog series, talks, maybe open-source contributions).
- Consulting fluency: lead discovery, build business cases, advise on technology decisions.
- Sustain technical edge (AI moves fast — keep shipping).

### Skills
- Negotiation, interview execution, personal branding.
- Advanced consulting: technology advisory, roadmap creation, transformation framing.
- Whatever the 2028 AI frontier is (assume: stronger autonomous agents, deeper eval/governance, on-device/efficient models — keep adapting).

### Projects
- **P7 — Thought-leadership series**: a multi-part blog or a small book-let / talk on "Production Agentic AI on the Lakehouse" — establishes you as a voice, not just a builder.
- Open-source: meaningful contributions to a data/AI tool you use (signals depth + collaboration).

### Books
- *Staff Engineer* (Larson) — for the IC-leadership path.
- *The Trusted Advisor* (Maister) — for the consulting path.
- Re-read *DDIA* selectively (you'll get 3× more the second time).

### Certs
- Generally none new — by now your *portfolio and interviews* carry you. Cert only if a specific employer demands it.

### Deliverables
- Offers / role transition (the outcome).
- Public portfolio (repos + writing + talk) that makes the interview almost a formality.
- A repeatable interview & negotiation playbook (write it down).

### Expected Outcome
> You are positioned as a top-tier Data & AI Engineer / Solution Architect with consulting range. **All four phases of your vision are realized or in clear reach.** Whether you take a MAANG-tier offer, become a high-end consultant, or accelerate at a great product company, you now *choose* — instead of hoping.

---

## One-page tracker (copy into LEARNING-LOG.md)

```
PHASE A (Jun–Sep 2026)  [ ] DSA patterns  [ ] OOP  [ ] SQL windows  [ ] P1 shipped  [ ] log habit
PHASE B (–Dec 2026)     [ ] DSA mediums   [ ] sys design basics  [ ] P2 (AI+eval)  [ ] 1st blog  [ ] DDIA started
PHASE C (–Jun 2027)     [ ] distributed sys  [ ] streaming P3  [ ] cloud cert  [ ] Go P5  [ ] arch docs P4
YEAR 2  (–Jun 2028)     [ ] P6 ref arch  [ ] consulting basics  [ ] STAR bank  [ ] mocks  [ ] talk delivered
YEAR 3  (–Jun 2029)     [ ] job search  [ ] thought leadership P7  [ ] offer/transition
```
