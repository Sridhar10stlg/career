# 06 — MAANG / Top-Tier Interview Prep Plan

> Covers DSA · System Design · Coding · Behavioral · Leadership Principles, plus a weekly schedule.
> **Reality:** the interview is a *separate skill* from the job. You can be a great engineer and fail the loop, or a mediocre one and pass it. Treat it as its own discipline. Start *light and early* (now), go *heavy* ~6 months before you apply (≈ Year 2).
> **Non-negotiable rule for your profile:** practice coding **without an LLM**. The LLM crutch is exactly what these interviews are designed to expose.

---

## Component 1: DSA

### Philosophy
Do **not** grind 500 random problems. Learn **patterns** (~15 of them), do ~150–250 carefully, and *redo* the ones you fail. Quality and spaced repetition beat volume.

### The patterns (learn in this order)
1. Arrays & Hashing
2. Two Pointers
3. Sliding Window
4. Stack
5. Binary Search
6. Linked List
7. Trees (traversals, BST)
8. Tries
9. Heaps / Priority Queue
10. Backtracking
11. Graphs (BFS/DFS, topological sort, union-find)
12. Dynamic Programming (1D → 2D)
13. Intervals
14. Greedy
15. Bit manipulation (light)

### Resources (pick one primary)
- **NeetCode 150 / NeetCode Roadmap** (best structured path — *primary*).
- *Grokking the Coding Interview* (pattern-based, great for your relearn).
- LeetCode (use NeetCode list to select; don't doomscroll problems).
- For the *mindset* gap: *A Common-Sense Guide to Data Structures and Algorithms* (Wengrow) — gentle, builds intuition.

### Method (per problem)
1. Read; restate; ask clarifying questions (yes, even alone).
2. Brute force first; state its complexity.
3. Optimize; identify the pattern.
4. Code it **yourself, no LLM**. Talk aloud.
5. Test with edge cases.
6. If you couldn't solve it in ~25–30 min, study the solution, *understand it*, and **re-add it to a redo list** for 1 week later.
7. Log it (problem, pattern, did-I-solve-it, lesson).

### Targets
- **Phase A (mo 1–3):** patterns 1–7, ~120–150 problems, easy + early-medium.
- **Phase B (mo 4–6):** patterns 8–13, solid mediums, ~250 cumulative.
- **Year 2 (heavy phase):** mediums fluent, hards attempted; timed sessions; ~350–400 cumulative with redos.

---

## Component 2: System Design

### Two flavors
- **Data/AI system design** (your home turf — lean in): design a data platform, a feature store, a RAG system, a streaming pipeline.
- **Classic system design:** URL shortener, news feed, rate limiter, chat, etc.

### Framework (use every time)
1. **Clarify** requirements (functional + NFRs) and scope.
2. **Estimate** scale (QPS, storage, bandwidth — back-of-envelope).
3. **API design** (the contract).
4. **High-level design** (boxes & arrows: clients, LB, services, DBs, caches, queues).
5. **Data model** & storage choice (justify).
6. **Deep dive** on the hard part (the bottleneck/the interviewer's interest).
7. **Trade-offs, failure modes, scaling, cost.**

### Resources
- *System Design Interview Vol 1 & 2* — Alex Xu (*primary*).
- *Designing Data-Intensive Applications* — Kleppmann (the depth behind the answers).
- ByteByteGo, "Grokking the System Design Interview."
- Build your own **HLD playbook repo** (your notes per common system).

### Targets
- **Phase B:** framework + 5 classic designs.
- **Year 1 end:** 12–15 designs incl. data/AI-specific; can lead a 45-min design.
- **Year 2:** strong-senior/staff level; mock with peers.

---

## Component 3: Coding Interviews (execution)

- Pick **one language** for interviews (Python — your strongest; clean and fast to write).
- Drill **fluency**: implement common structures from memory (hashmap usage, heap, deque, defaultdict, bisect).
- Practice **talking while coding** (record yourself; it's awkward, do it anyway).
- Time-box: medium in ~25–35 min including explanation.
- **Mock interviews:** Pramp, interviewing.io, or peers — at least 8–10 before applying.

---

## Component 4: Behavioral Interviews

### STAR method
**S**ituation → **T**ask → **A**ction → **R**esult (quantify the result).

### Build a story bank (10–12 stories) covering:
- A project you led / drove.
- A hard technical problem you solved.
- A conflict / disagreement and how you handled it.
- A failure and what you learned.
- A time you influenced without authority.
- A time you dealt with ambiguity.
- A time you went above and beyond / showed ownership.
- A time you mentored/helped someone.
- A time you made a trade-off / tough call under pressure.
- A time you disagreed with a decision but committed.

> You already have strong raw material: the MDM pipeline, config-driven frameworks, agentic AI work, fast promotions. Mine these. Write each as STAR, quantify outcomes, rehearse aloud.

---

## Component 5: Leadership Principles (Amazon-style; generalizes to all)

Amazon's 16 LPs are the most explicit; even non-Amazon behavioral rounds test these traits. Map 2–3 of your STAR stories to each of the big ones:
- **Customer Obsession**, **Ownership**, **Invent and Simplify**, **Dive Deep**, **Bias for Action**, **Deliver Results**, **Earn Trust**, **Are Right, A Lot**, **Learn and Be Curious**, **Insist on Highest Standards**.

For each: have a concrete, quantified story ready. Practice the *follow-up* "dive deep" questions interviewers ask.

---

## Weekly preparation schedule

### Light phase (now → ~Year 1.5; alongside main roadmap, ~5–6 hrs/wk of the 28)
| Day | Focus | Time |
|---|---|---|
| Mon | 2 DSA problems (current pattern) | 1 hr |
| Tue | 2 DSA problems | 1 hr |
| Wed | Redo 1 failed problem + review notes | 0.5 hr |
| Thu | 2 DSA problems | 1 hr |
| Fri | — (main roadmap / rest) | — |
| Sat | 1 system design (study + sketch) | 1.5 hr |
| Sun | Behavioral: write/refine 1 STAR story | 0.5 hr |

### Heavy phase (~6 months before applying, Year 2; ~12–15 hrs/wk)
| Day | Focus | Time |
|---|---|---|
| Mon | 3 DSA (timed) + redo list | 2 hr |
| Tue | 3 DSA (timed) | 2 hr |
| Wed | 1 system design (full, written) | 2 hr |
| Thu | 3 DSA + 1 mock (coding) | 2.5 hr |
| Fri | Behavioral rehearsal + LP mapping | 1 hr |
| Sat | 1 mock interview (peer) + 1 system design | 3 hr |
| Sun | Review week, update redo list & story bank | 1.5 hr |

---

## Timeline to "apply-ready"

- **Now → Year 1:** light phase; foundations form; ~250 problems; 12+ designs; story bank drafted.
- **Year 2 H1:** heavy phase; mocks; timed practice.
- **Year 2 H2 / Year 3:** start applying when you can: pass mediums reliably, lead a system design, deliver 10 STAR stories crisply, and **code without an LLM under pressure.** That's the bar — don't apply before it, don't wait forever after it.

## Anti-patterns (don't)
- Don't memorize solutions — you'll be caught on follow-ups.
- Don't skip the redo list — that's where learning sticks.
- Don't grind DSA at the expense of the *real* skills that make the job (the roadmap balances this deliberately).
- Don't use an LLM during practice. Ever. For interview prep, it is poison to the exact muscle being tested.
