# 04 — Architecture Roadmap

> Growth path: **Engineer → Senior Engineer → Systems Designer (you) → Solution Architect → Principal Architect.**
> Architecture is not a title you wait for. It's a way of working you adopt *now*, at your current role, on your current projects.

---

## The mental shift at each level

| Level | Question you optimize for | Scope | Output |
|---|---|---|---|
| Engineer | "Does my code work?" | A task | Working code |
| Senior Engineer | "Is this the right solution, built well?" | A feature/service | Solution + tests + docs |
| **Systems Designer (you)** | "Do these components fit together correctly?" | A system | System design + interfaces |
| Solution Architect | "Does this solve the *business* problem, at acceptable cost/risk?" | A solution across systems | Architecture + trade-offs + roadmap |
| Principal Architect | "Is the *whole org's* technical direction sound?" | Org / platform | Standards, vision, influence |

The promotion is mostly **scope of ambiguity you can absorb** and **stakeholders you can align**. Manufacture both early.

---

## Architecture skills (build in this order)

### Tier 1 — Foundations (Year 1)
- **System building blocks:** load balancers, caches, queues, databases (SQL/NoSQL/columnar/vector), CDNs, API gateways.
- **Distributed systems literacy:** CAP, consistency models, partitioning, replication, idempotency, exactly-once, back-pressure. *(DDIA is the spine.)*
- **Back-of-envelope estimation:** QPS, storage, bandwidth, latency budgets.
- **Non-functional requirements (NFRs):** scalability, availability, latency, durability, security, cost, maintainability. *Architects live in NFRs.*

### Tier 2 — Solution design (Year 1–2)
- **Trade-off reasoning:** every design is a trade. Practice articulating "X over Y because [NFR], at the cost of [Z]."
- **Integration patterns:** sync vs async, event-driven, pub/sub, sagas, idempotent consumers, the outbox pattern.
- **Cloud architecture (one cloud deep):** compute/storage/network/identity, well-architected framework (5 pillars), reference architectures.
- **Cost modeling / FinOps:** the question juniors forget and architects always ask — "what does this cost at 10×?"
- **Security & compliance basics:** identity, least privilege, encryption, data residency, PII.

### Tier 3 — Enterprise & strategy (Year 2–3)
- **Enterprise architecture concepts (lightly):** capability maps, domains, TOGAF vocabulary, target vs current state.
- **Architecture roadmaps:** sequencing migrations, strangler-fig, phased delivery, risk-managed rollout.
- **Build-vs-buy, platform thinking, technology selection** with weighted decision matrices.

---

## Design skills (the daily craft)

- **Decompose:** break a vague problem into bounded components with clear responsibilities.
- **Define interfaces/contracts** before implementations (APIs, schemas, data contracts).
- **Identify the hard part first** (the bottleneck, the riskiest unknown) and design around it.
- **Design for failure:** what breaks, what's the blast radius, how do we degrade gracefully.
- **Sketch fast:** whiteboard/Excalidraw a design in 10 minutes; iterate.

> **Practice protocol:** for every project you touch at Psiog, *before* coding, write a one-page design: problem, constraints/NFRs, options considered, chosen approach, trade-offs, risks. Even when nobody asks. This single habit converts you into an architect faster than any course.

---

## Documentation skills (architects are judged on artifacts)

- **C4 model:** Context → Container → Component → Code. Learn it; use it everywhere. (Tooling: Structurizr, Excalidraw, draw.io, Mermaid.)
- **ADRs (Architecture Decision Records):** short docs capturing *decision + context + consequences*. Keep an `adr/` folder in every repo. (Format: Michael Nygard's template.)
- **Design docs / RFCs:** problem, goals/non-goals, proposed design, alternatives, risks, rollout. (Google/Amazon-style.)
- **Diagrams that communicate:** the right altitude for the audience (execs get Context; engineers get Component).
- **Trade-off matrices:** options × criteria (weighted) — makes your reasoning legible and defensible.

**Deliverable:** a personal `architecture-playbook` repo with your ADR template, C4 examples, design-doc template, and 2–3 worked examples from your projects.

---

## Leadership skills (the part engineers skip and then plateau)

- **Technical influence without authority:** win through clear writing, sound reasoning, and listening — not seniority.
- **RFC-driven decision making:** propose, invite critique, converge. (Run one at Psiog.)
- **Mentoring:** explain your designs to juniors; teaching exposes your own gaps and builds leadership signal.
- **Driving alignment:** translate between business and engineering; get diverse stakeholders to "yes."
- **Owning outcomes, not just code:** track whether the architecture actually delivered the business result.

---

## How to grow *at your current job* (most important section)

You don't need a new title to do architecture. Starting this month:

1. **Write design docs for everything**, even uninvited. Share them. Build a reputation as "the person whose designs are clear."
2. **Volunteer for the ambiguous problem** nobody wants to scope. Ambiguity-absorption is the architect skill.
3. **Propose a reusable framework/standard** (you already build config-driven frameworks — formalize one as an internal standard with docs + ADRs).
4. **Ask the NFR questions in meetings:** "What's the latency budget? Cost at scale? Failure mode? Who's the user?" This *signals* architect-thinking to everyone watching.
5. **Run one cross-team initiative** end-to-end (Year 2). This is your promotion case and your interview story.

---

## Milestones

- **Year 1:** Design docs are habitual; you know C4/ADRs; you can design a data platform on a whiteboard with NFRs and trade-offs.
- **Year 2:** You've led one framework/initiative; produced a full reference architecture (P6); can pass a system-design interview at senior+ level.
- **Year 3:** You operate as a Solution Architect in practice; your `architecture-playbook` + reference architectures are public proof; you're sought out for design reviews.

## Books (architecture)
- *Designing Data-Intensive Applications* — Kleppmann (foundations).
- *Software Architecture: The Hard Parts* — Ford, Richards et al. (trade-offs).
- *Fundamentals of Software Architecture* — Richards & Ford (the discipline).
- *The Software Architect Elevator* — Gregor Hohpe (connecting tech to business — bridges into consulting).
- *System Design Interview Vol 1 & 2* — Alex Xu (interview-shaped, but great building-block reference).
