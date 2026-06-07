# 08 — Portfolio Strategy

> Your portfolio is your *proof*. In a market flooded with people who claim AI/data skills, **demonstrated artifacts** (repos, writing, talks) are what separate you. Quality over quantity: **4–6 excellent repos beat 30 abandoned ones.**
> Theme everything around your spike: **Production-grade Data + AI engineering on the lakehouse, with evaluation and governance.** A coherent portfolio tells a story; a random one tells nothing.

---

## Guiding principles

1. **Every repo has a great README** (problem, architecture diagram, how-to-run, trade-offs, what you'd do next). Recruiters/engineers read the README, not all the code.
2. **Show *engineering*, not just function:** tests, CI, typing, docs, ADRs. This directly counters the "LLM-dependent, thin fundamentals" risk.
3. **Document decisions** (ADRs, design docs) — this is what makes you read as architect-level.
4. **Pin 4–6 repos** on your GitHub profile; archive/hide the noise.
5. **Each artifact should map to a STAR story and an interview talking point.**

---

## GitHub repositories to build (the core set)

| Repo | What it proves | Maps to | When |
|---|---|---|---|
| **lakehouse-medallion-pipeline** (P1) | End-to-end DE: ingestion → bronze/silver/gold → DQ tests → BI view; config-driven | DE depth | Phase A |
| **production-rag-with-eval** (P2) | RAG done right + an evaluation harness (faithfulness/relevance/cost/latency dashboards) + guardrails | **Your spike** | Phase B |
| **streaming-lakehouse** (P3) | Kafka → Structured Streaming → Delta → serving, with data contracts | DE scale | Phase C |
| **architecture-playbook** (P4) | Your ADR/C4/design-doc templates + worked examples from P1–P3 | Architect signal | Phase C |
| **mcp-data-server** | An MCP server exposing a data source + client; agentic integration | AI/agentic edge | Phase C |
| **go-data-tooling** (G1–G4) | A Go CLI / concurrent worker / small service with tests | Polyglot + systems | Year 1+ |
| **enterprise-agentic-reference-arch** (P6) | Full reference architecture: design doc + working slice + cost model + ROI narrative | Architect + consultant | Year 2 |

> Don't build all at once. One flagship at a time, finished and polished, then the next.

---

## Architecture projects to showcase

These are *documents + diagrams* (often more impressive than code for architect roles):

1. **Reference architecture: "Enterprise Agentic AI on the Lakehouse"** (P6) — the centerpiece. C4 diagrams, ADRs, NFRs, trade-off matrices, cost model, ROI story.
2. **Design-doc collection** — for each major repo, a real design doc (problem, options, decision, trade-offs, risks).
3. **A "Snowflake vs Databricks" decision framework** — a public weighted-decision-matrix write-up (also a consulting artifact; see [05](05-consulting-roadmap.md)).
4. **A data-platform blueprint** — how you'd design a greenfield enterprise data platform (governance, quality, lineage, serving).

---

## AI projects to build (lean into your differentiator)

1. **production-rag-with-eval** (P2) — the eval harness is the differentiator; most people skip it.
2. **A multi-agent workflow with reliability engineering** — retries, guardrails, human-in-the-loop, cost/latency tracking. Show *when multi-agent beats single-agent* (and when it doesn't).
3. **An MCP server/client** for a real data tool — early-mover signal on the protocol.
4. **An "LLM eval framework" mini-library** — reusable evaluation utilities (LLM-as-judge with calibration, regression tests for prompts). Even small, this screams "senior AI engineer."
5. **A cost/latency optimization case study** — take a working AI feature, cut cost 50% via caching/model-routing/smaller models, *measure and document it.*

---

## Blog topics to write (publish on dev.to / Medium / your own site + LinkedIn)

Writing forces clarity, builds authority, and is itself interview prep. **Target: 1 post/month, building to a recognizable voice.**

**Beginner-friendly authority (Year 1):**
- "Medallion architecture: what it actually buys you (and when it doesn't)"
- "Window functions every data engineer should own (with real examples)"
- "Snowflake vs Databricks: a decision framework, not a holy war"
- "Spark performance: the 7 things that fixed 90% of my slow jobs"

**Spike / differentiator (Year 1–2):**
- "Your RAG is a demo until you measure it: building an eval harness"
- "Production agentic AI: reliability engineering for LLM agents"
- "MCP explained for data engineers"
- "When multi-agent systems actually beat a single good prompt"
- "LLM-as-a-judge: how to use it without fooling yourself"

**Architecture / consulting (Year 2–3):**
- "Designing enterprise agentic AI on the lakehouse" (companion to P6)
- "Writing ADRs that your future team will thank you for"
- "How I turned a data pipeline into a business case (ROI for engineers)"
- "From engineer to architect: the questions that changed how I work"

---

## Technical content beyond blogs (Year 2–3)

- **A conference / meetup talk** (start with an internal Psiog talk, then a local meetup). Topic: your reference architecture or your eval framework.
- **Open-source contributions** to a tool you use (dbt, a vector DB, an agent framework, Great Expectations). Even small PRs signal depth + collaboration.
- **A LinkedIn cadence**: short, substantive posts about what you're building/learning (not motivational fluff). Consistency > virality.
- **A "build-in-public" thread** for your flagship project (documents the journey, attracts an audience).

---

## Sequencing (don't overload)

| Period | Build | Write |
|---|---|---|
| Phase A | P1 (flagship DE) | set up blog; 1 post |
| Phase B | P2 (RAG+eval) | 2 posts (incl. the eval one) |
| Phase C | P3, P4, MCP | 2–3 posts; polish GitHub profile |
| Year 2 | P6 reference arch; Go repo | monthly posts; 1 talk |
| Year 3 | OSS contributions; thought-leadership series (P7) | series + talk; LinkedIn authority |

---

## The "profile readiness" checklist (review quarterly)
- [ ] GitHub: 4–6 pinned, polished repos with great READMEs + diagrams.
- [ ] At least 2 repos show tests + CI + ADRs.
- [ ] One reference architecture document published.
- [ ] LinkedIn headline reflects your positioning (see [01](01-assessment-and-gap-analysis.md)).
- [ ] 6+ blog posts published; a recognizable theme.
- [ ] One talk delivered.
- [ ] Every artifact maps to a STAR story you can tell ([06](06-maang-prep.md)).
