# 09 — Monthly Execution Plan (Next 12 Months)

> **Jun 2026 → May 2027.** This is the file you live in week-to-week.
> Budget: ~28.5 hrs/week (Weekdays 2.5 × 5 = 12.5; Weekends 8 × 2 = 16).
> **Standing weekday split (default):** 1 hr DSA + 1.5 hr current main track. **Weekend:** project build + system design + writing + review.
> Update the checkboxes and your `LEARNING-LOG.md` every Sunday. Miss a day? Don't "make up" 5 hours — just resume. Consistency > intensity.

---

## The fixed weekly skeleton (applies every week unless a month overrides it)

| Slot | Mon | Tue | Wed | Thu | Fri | Sat (8h) | Sun (8h) |
|---|---|---|---|---|---|---|---|
| DSA (1h) | ✅ | ✅ | redo | ✅ | — | — | — |
| Main track (1.5h) | ✅ | ✅ | ✅ | ✅ | ✅ | — | — |
| Project build | — | — | — | — | — | 4h | 3h |
| System design | — | — | — | — | — | 2h | — |
| Writing/blog | — | — | — | — | — | — | 2h |
| Reading (book) | — | — | — | — | — | 1h | 1h |
| Review + log + redo | — | — | — | — | — | 1h | 2h |

> Fri's 2.5 hrs is deliberately light (behavioral story / reading / catch-up / rest). Protect against burnout — this is a 3-year game.

---

## MONTH 1 — Jun 2026 · *Foundations + flagship kickoff*
- **Main track:** Python OOP + fundamentals refresh ([03 §1](03-technical-learning-plan.md)).
- **DSA:** Patterns 1–3 (Arrays/Hashing, Two Pointers, Sliding Window) — ~40 problems, no LLM.
- **Project:** Start **P1 lakehouse-medallion-pipeline** — pick dataset, design medallion layers, write the design doc *first*.
- **Book:** *Fluent Python* (OOP/data-model chapters).
- **Weekly goals:** W1 env + design doc + DSA pattern 1 · W2 bronze/silver layers + pattern 2 · W3 gold + DQ tests + pattern 3 · W4 README + diagram + redo week.
- **Milestone:** P1 skeleton runs end-to-end; `LEARNING-LOG.md` started.
- **Checkpoint (last Sun):** Can I write a Python class from scratch, no LLM? Did I solve pattern-1 problems unaided?

## MONTH 2 — Jul 2026 · *OOP depth + SQL windows*
- **Main track:** Python OOP deep (dunders, composition, ABCs, dataclasses) + start SQL window functions ([03 §2.2](03-technical-learning-plan.md)).
- **DSA:** Patterns 4–5 (Stack, Binary Search) — ~40 problems.
- **Project:** Refactor P1 into clean OOP (config-driven mini-framework); add tests (pytest).
- **Book:** finish *Fluent Python* selections; start *Grokking Algorithms* (skim).
- **Milestone:** P1 has tests + typing; you can solve 10 window-function problems.
- **Checkpoint:** Are my classes well-designed (composition over inheritance)? Tests passing in CI?

## MONTH 3 — Aug 2026 · *Polish flagship + SQL optimization + first writing*
- **Main track:** SQL optimization (query plans, Snowflake micro-partitions) + finish window functions.
- **DSA:** Patterns 6–7 (Linked List, Trees) — ~40 problems; **cumulative ~120**.
- **Project:** Finish + polish **P1**; add GitHub Actions CI; write **Blog post #1** ("Medallion architecture, honestly").
- **Milestone (end of Phase A):** P1 shipped & pinned; blog live; ~120 DSA problems; daily habit locked.
- **QUARTERLY CHECKPOINT:** Re-run [01](01-assessment-and-gap-analysis.md) self-scores. Honest: is LLM-dependency dropping? Did I *finish* P1 or abandon it?

---

## MONTH 4 — Sep 2026 · *AI engineering begins (your spike)*
- **Main track:** AI Eng — LLM fundamentals + RAG done properly ([03 §5.1–5.2](03-technical-learning-plan.md)).
- **DSA:** Pattern 8–9 (Tries, Heaps) — ~30 problems.
- **Project:** Start **P2 production-rag-with-eval** — design doc, ingestion, chunking, retrieval.
- **Book:** start *Designing Data-Intensive Applications* (long-running) + *Designing ML Systems* (Huyen).
- **System design:** begin — framework + building blocks; 1 design (URL shortener).
- **Milestone:** P2 retrieves and answers; you understand chunking/hybrid retrieval trade-offs.

## MONTH 5 — Oct 2026 · *RAG evaluation (the differentiator)*
- **Main track:** RAG evaluation (faithfulness, relevance, RAGAS-style) + guardrails ([03 §5.6](03-technical-learning-plan.md)).
- **DSA:** Pattern 10 (Backtracking) — ~25 problems.
- **Project:** Build P2's **eval harness** + cost/latency dashboards. *This is the artifact that sets you apart.*
- **System design:** 2 designs (rate limiter, news feed); back-of-envelope drills.
- **Milestone:** P2 has a working eval suite with metrics dashboards.

## MONTH 6 — Nov 2026 · *Spark depth + ship P2 + write*
- **Main track:** Spark performance (partitioning, shuffle, skew, AQE) ([03 §3.x](03-technical-learning-plan.md)).
- **DSA:** Patterns 11 (Graphs: BFS/DFS, topo sort) — ~30 problems; **cumulative ~205**.
- **Project:** Finish + ship **P2**; **Blog post #2** ("Your RAG is a demo until you measure it"). Optional: **Databricks DE Associate** cert.
- **System design:** 1 data-system design (a data pipeline/feature store).
- **Milestone (end of Phase B):** P2 shipped; 2 blogs live; system-design framework solid; ~205 DSA.
- **QUARTERLY CHECKPOINT:** Phase 1 of vision (strong hands-on Data+AI engineer) ≈ achieved? Re-score gaps.

---

## MONTH 7 — Dec 2026 · *Distributed systems + streaming start*
- **Main track:** Distributed systems (CAP, consistency, partitioning, idempotency) via DDIA + Kafka fundamentals.
- **DSA:** Pattern 12 (DP 1D) — ~25 problems.
- **Project:** Start **P3 streaming-lakehouse** (Kafka → Structured Streaming → Delta).
- **System design:** 2 designs (chat system, notification system).
- **Milestone:** Kafka producer/consumer + a streaming job running; can explain delivery semantics.
- *Note: holiday month — adjust hours down if needed; protect the habit, not the volume.*

## MONTH 8 — Jan 2027 · *Streaming depth + cloud start*
- **Main track:** Spark Structured Streaming (watermarks, windows, stateful) + pick a cloud (Azure or AWS) and start its data-engineering path.
- **DSA:** Pattern 12 (DP 2D) — ~25 problems.
- **Project:** P3 — add data contracts + DQ; finish streaming pipeline.
- **System design:** 2 designs (incl. a streaming/analytics system).
- **Milestone:** P3 functional with contracts; cloud fundamentals underway.

## MONTH 9 — Feb 2027 · *Cloud cert push + architecture docs*
- **Main track:** Cloud certification prep (Azure Data Engineer / AWS Data Engineer Associate).
- **DSA:** Pattern 13–14 (Intervals, Greedy) — ~25 problems; **cumulative ~280**.
- **Project:** Finish **P3**; start **P4 architecture-playbook** (C4 + ADRs for P1–P3); **Blog post #3**.
- **System design:** 1 design + start your HLD playbook repo.
- **Milestone:** P3 shipped; learning C4/ADRs; cloud cert exam scheduled.
- **QUARTERLY CHECKPOINT:** Re-score. Am I producing *architecture artifacts*, not just code?

---

## MONTH 10 — Mar 2027 · *Cloud cert + GoLang kickoff*
- **Main track:** Take the cloud cert. Then **start GoLang** ([03 §4](03-technical-learning-plan.md)): Tour of Go + Learn Go with Tests.
- **DSA:** Review/redo weak patterns; light volume (cert focus) — ~15 problems.
- **Project:** Finish **P4**; start **Go G1** (CLI tool).
- **System design:** 2 designs.
- **Milestone:** Cloud cert earned; P4 published; first Go program runs.

## MONTH 11 — Apr 2027 · *Go concurrency + MCP project*
- **Main track:** GoLang concurrency (goroutines/channels) + AI: MCP ([03 §5.3](03-technical-learning-plan.md)).
- **DSA:** Graphs advanced (union-find) + DP review — ~25 problems.
- **Project:** **Go G2** (concurrent worker pool); start **mcp-data-server**.
- **System design:** 1 data/AI design + HLD playbook update.
- **Milestone:** Go concurrency understood (can explain goroutines vs threads); MCP server prototype.
- **Blog post #4** (MCP for data engineers).

## MONTH 12 — May 2027 · *Consolidate + year-1 review*
- **Main track:** Finish MCP project; consolidate AI agentic patterns ([03 §5.4](03-technical-learning-plan.md)).
- **DSA:** Full review; timed mediums; **cumulative ~330**; identify weak spots.
- **Project:** Ship **mcp-data-server**; polish GitHub profile (pin 4–6 repos); **Blog post #5**.
- **System design:** Self-assess — can I lead a 45-min design? Do 1 mock.
- **Milestone (end of Phase C / Year 1):** 4–5 strong repos, cloud cert, Go basics, 5 blogs, system-design competent.
- **ANNUAL CHECKPOINT (critical):**
  - Re-run full [01](01-assessment-and-gap-analysis.md) gap analysis.
  - Am I Senior-DE-level? Could I pass a screening loop?
  - Has LLM-dependency genuinely dropped? (Honest test: solve a fresh medium + write a class, no LLM, timed.)
  - Update [02](02-three-year-roadmap.md) Year-2 plan with what I learned.
  - Decide: am I on track to start MAANG heavy-prep + consulting build in Year 2?

---

## Monthly review template (paste into LEARNING-LOG.md each month-end)

```
## Month __ (Mon YYYY)
- Hours logged: ___ / ~120 target
- DSA: ___ problems (cumulative ___) | weak patterns: ___
- Main track progress: ___
- Project: ___ (% done / shipped?)
- Writing: ___ (post published? Y/N)
- System design: ___ designs
- Book: ___ (% / finished?)
- Win of the month: ___
- Slipped / didn't do: ___
- LLM-dependency check (1–5, lower=better): ___
- Adjust next month: ___
```

## If you fall behind (you will, sometimes)
- **Triage in this order:** keep DSA habit → keep current project moving → keep one book → drop blog/extras temporarily.
- **Never drop:** the daily habit and the *finishing* of projects. A half-finished portfolio is worth ~0.
- **Don't compensate by adding a new track.** Falling behind = do *less*, better. Not more.
