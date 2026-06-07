# 07 — Thinking Frameworks

> These are the mental tools that turn a coder into an architect/consultant. You named "questioning ability" and "problem solving" as weak — *these frameworks are the fix.* Learn one, then deliberately apply it for two weeks until it's reflex.
> Meta-rule: a framework is useless until you've *used it on a real problem*. Each one below has a drill. Do the drills.

---

## 1. First Principles Thinking

**What:** Strip a problem to its fundamental truths and reason up from there, instead of reasoning by analogy ("we've always done it this way").

**How:**
1. State the problem.
2. List your assumptions.
3. Challenge each: "Is this *actually* true, or just convention?"
4. Rebuild a solution from only the things that are fundamentally true.

**Drill:** Take something you do at work "because that's how it's done" (e.g., "we always batch-load nightly"). Ask: what's the actual constraint? Why nightly? What if we didn't? Rebuild the reasoning. Do this on 3 work conventions.

---

## 2. Systems Thinking

**What:** See the whole system — components, relationships, feedback loops, second-order effects — not isolated parts.

**How:**
- Map the system: parts, flows, dependencies.
- Find feedback loops (reinforcing & balancing).
- Ask: "If I change X, what *else* moves? What's the second-order effect?"
- Look for leverage points (small changes, big impact).

**Drill:** Diagram one of your data pipelines as a system *including the humans and decisions around it* (who consumes it, what decisions depend on it, what breaks downstream if it's late). Identify one leverage point. (*Book: Thinking in Systems, Donella Meadows.*)

---

## 3. Root Cause Analysis (RCA)

**What:** Find the *real* cause of a problem, not the symptom.

**How:** Define the problem precisely → gather evidence → trace causal chain → distinguish symptom vs root cause → verify by asking "if I fix this, does the problem truly go away?"

**Tools:** 5 Whys (below), fishbone/Ishikawa diagram, fault tree.

**Drill:** Next bug/incident at work, write a 1-page RCA: what happened, impact, timeline, root cause, fix, prevention. (This is also a great architect/SRE habit and a behavioral interview story factory.)

---

## 4. MECE (Mutually Exclusive, Collectively Exhaustive)

**What:** Break a problem into buckets that don't overlap (ME) and leave nothing out (CE). The backbone of structured/consulting thinking.

**How:** When listing causes/options/segments, check: do any overlap? Is anything missing? Restructure until clean.

**Drill:** "Why is this pipeline slow?" — produce a MECE breakdown (e.g., ingestion / transformation / storage I/O / compute config / downstream). No overlaps, nothing missed. Then "How could we cut cloud cost?" MECE it.

---

## 5. The 5 Whys

**What:** Ask "why?" ~5 times to drill from symptom to root cause.

**Example:**
- Dashboard is wrong → *why?* Source table stale → *why?* Job failed → *why?* Upstream schema changed → *why?* No schema contract → *why?* We never built data contracts. **Root cause: missing data contracts.** (Now the fix is structural, not a band-aid.)

**Drill:** Apply 5 Whys to one recurring annoyance at work. Notice the fix changes when you reach the real root.

---

## 6. The Pyramid Principle

**What:** Communicate top-down: **answer/conclusion first**, then grouped supporting arguments (MECE), then detail. (Barbara Minto.) The single most valuable communication upgrade for architect/consultant roles.

**How (SCQA for framing):** **S**ituation → **C**omplication → **Q**uestion → **A**nswer. Then structure support as a pyramid: governing thought on top, MECE arguments below, evidence at the bottom.

**Drill:** Rewrite your last technical email/update so the *first sentence is the conclusion/ask*. Group the rest into 2–3 MECE supporting points. Cut everything else. (Also see [05](05-consulting-roadmap.md).)

---

## 7. Hypothesis-Driven Thinking

**What:** Start with a likely answer (hypothesis), then seek evidence to confirm or kill it — instead of analyzing everything exhaustively. How consultants move fast.

**How:**
1. Form a hypothesis ("I think the bottleneck is the shuffle stage").
2. Identify what evidence would prove/disprove it.
3. Get *that* evidence first (cheapest test).
4. Confirm → act. Disconfirm → new hypothesis.

**Drill:** Next performance problem, write your hypothesis *before* investigating. Then test it directly. Track how often your first hypothesis was right (calibration improves analytical judgment).

---

## Bonus frameworks worth knowing

- **Second-Order Thinking:** "And then what?" — consequences of consequences.
- **Inversion:** instead of "how do I succeed?", ask "how would this *fail*?" and avoid that. (Great for architecture risk.)
- **Occam's Razor:** prefer the simplest explanation/solution that fits.
- **Cost-Benefit / Trade-off matrix:** options × weighted criteria — makes decisions legible (architect staple).
- **Eisenhower Matrix:** urgent/important — for protecting your 28 hrs/week from busywork.
- **OODA Loop:** Observe-Orient-Decide-Act — for fast decisions under uncertainty.

---

## How to build the habit (the only part that matters)

1. **One framework per two weeks.** Don't learn all 7 at once — *apply* one at a time.
2. **Keep a `thinking-log.md`**: each time you consciously use a framework, jot the problem + how it helped.
3. **Force application in meetings:** silently MECE the problem; form a hypothesis before opining; answer in Pyramid form.
4. **Review monthly:** which frameworks are becoming reflex? Which need more reps?

> The compounding effect: in 6 months these stop being "techniques you apply" and become *how you think*. That shift — visible in how you ask questions and structure answers — is exactly the "analytical thinking" and "questioning ability" you flagged as weak. It's also the most visible marker of seniority in any room.

## Books
- *Thinking in Systems* — Donella Meadows.
- *The Pyramid Principle* — Barbara Minto.
- *The McKinsey Way* / *The McKinsey Mind* — Ethan Rasiel.
- *Super Thinking* — Weinberg & McCann (a buffet of mental models).
- *Thinking, Fast and Slow* — Kahneman (how your own reasoning misfires).
