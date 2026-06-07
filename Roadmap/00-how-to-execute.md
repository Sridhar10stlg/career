# 00 — How To Execute (The Handbook)

> The other files tell you **what** to do. This file tells you **how** to actually do it — the mechanics, the tools, the rituals. Read this once fully, then refer back to the relevant section whenever you start a new activity type.
> Golden rule: **the roadmap fails by vagueness, not by ambition.** Every "learn X" below is turned into "open this, do this, for this long, and you're done when this is true."

---

## 0. One-time setup (do this on Day 1, ~1 hour)

Before any learning, set up the rails so you never lose momentum to friction:

1. **Accounts:** Create a [LeetCode](https://leetcode.com) account and bookmark [NeetCode.io](https://neetcode.io) (the roadmap view is free).
2. **A "career" GitHub repo** named `learning-journey` (or similar). Inside it:
   - `LEARNING-LOG.md` — your weekly/monthly log (template in [09](09-monthly-execution-plan.md)).
   - `dsa/` — your solved problems, organized by pattern (yes, commit your solutions).
   - `dsa/REDO.md` — the list of problems you failed and must retry.
   - `system-design/` — your HLD notes.
   - `thinking-log.md` — when you apply a framework from [07](07-thinking-frameworks.md).
3. **A calendar block.** Put your weekday 2.5h and weekend 8h blocks in your actual calendar *as recurring events*. Treat them like meetings you can't skip. This is the #1 thing that makes or breaks the plan.
4. **A timer.** Phone timer or [Pomodoro](https://pomofocus.io). You'll use it for time-boxing problems.

That's it. Don't spend 3 days "setting up the perfect system." 1 hour, then start.

---

## 1. HOW to do DSA (the example you asked about)

**The roadmap says:** *"Patterns 1–3 (Arrays/Hashing, Two Pointers, Sliding Window) — ~40 problems, no LLM."* Here is exactly how.

### Where you do it
**NeetCode.io → "Roadmap"** (or the NeetCode 150 list). It groups problems *by pattern* and has free video explanations. Solve *on LeetCode*, track *on NeetCode*. Don't shop around for the "best" resource — NeetCode is more than enough. Decision made.

### The exact problems for Month 1 (Patterns 1–3)
Do these ~20 core problems, then ~20 more "Easy" tagged ones in the same patterns on LeetCode to drill fluency (= ~40 total).

**Pattern 1 — Arrays & Hashing** (do in this order)
1. Contains Duplicate (E)
2. Valid Anagram (E)
3. Two Sum (E)
4. Group Anagrams (M)
5. Top K Frequent Elements (M)
6. Product of Array Except Self (M)
7. Valid Sudoku (M)
8. Longest Consecutive Sequence (M)

**Pattern 2 — Two Pointers**
9. Valid Palindrome (E)
10. Two Sum II – Input Array Is Sorted (M)
11. 3Sum (M)
12. Container With Most Water (M)

**Pattern 3 — Sliding Window**
13. Best Time to Buy and Sell Stock (E)
14. Longest Substring Without Repeating Characters (M)
15. Longest Repeating Character Replacement (M)
16. Permutation in String (M)
17. Minimum Window Substring (H — attempt, don't stress)
18. Sliding Window Maximum (H — attempt, don't stress)

> Fill the remaining ~20 with LeetCode's "Easy" problems tagged `Array`, `Hash Table`, `Two Pointers`, `Sliding Window` to build speed on the basics.

### The daily ritual (your 1 hr DSA block = ~2 problems)
For **each** problem, follow these 7 steps. Do NOT skip step 4's "no LLM."

1. **Read & restate** (2 min): say the problem back in your own words. Note input/output, constraints, edge cases.
2. **Examples** (1 min): work one example by hand. Try to find a tricky edge case.
3. **Brute force first** (3 min): what's the dumb-but-correct solution? State its time/space complexity out loud. (Interviewers *want* this first.)
4. **Optimize → find the pattern** (5–10 min): "can a hashmap remove this nested loop? can two pointers replace this scan?" *Think.* This is the rep that builds your brain. **LLM stays off.**
5. **Code it yourself** (10–15 min): type it. Talk aloud as you go (literally — it builds the interview muscle). If you blank on syntax (not logic), the docs are fine; an LLM for *logic* is not.
6. **Test** (3 min): run it, then test edge cases (empty, single element, duplicates, negatives).
7. **Log it** (2 min): in `dsa/`, commit your solution with a one-line comment: *pattern, did-I-solve-it-unaided (Y/N), the key insight.*

### The "I'm stuck, no LLM" protocol (critical)
This is the part people get wrong. When you're stuck:
- **0–25 min:** keep struggling. Re-read constraints. Try a smaller example. Try a different pattern. *The struggle IS the learning.* Most growth happens here.
- **At ~25–30 min:** stop. Watch the **NeetCode video** for that problem (not an LLM — a structured explanation that teaches the *pattern*, not just the answer).
- **After understanding:** close everything and **re-code it from memory.** If you can't, you didn't understand it — rewatch.
- **Add it to `dsa/REDO.md`** with today's date. Retry it in ~7 days from a blank file. You haven't "learned" it until you can solve it cold a week later.

> Why no LLM specifically here? An LLM hands you the answer, your brain files it under "solved," and you learn nothing. A video teaches the *reusable pattern*. The whole point of DSA is to rebuild your problem-solving muscle — outsourcing it defeats the purpose entirely. (This is literally career-risk R1 in [01](01-assessment-and-gap-analysis.md).)

### How you know a pattern is "done"
You can take a *new, unseen* problem in that pattern and solve it in <25 min, from a blank file, explaining your reasoning aloud, without help. When that's true for patterns 1–3, you're ready for month 2's patterns. Speed comes later — correctness-from-scratch first.

### A realistic Month-1 DSA week
| Day | Problems | Notes |
|---|---|---|
| Mon | #1, #2 | warm easy ones, nail the ritual |
| Tue | #3, #4 | |
| Wed | redo + #5 | revisit anything shaky |
| Thu | #6, #7 | |
| (weekend) | #8 + 4 LeetCode easies | more volume on the rest day |

Repeat through the pattern list across the month. ~40 problems lands naturally.

---

## 2. HOW to build a project (P1, P2, ...)

The roadmap names projects but a project is where people freeze ("where do I even start?"). Here's the unfreeze:

### The project ritual
1. **Write the design doc FIRST** (1–2 hrs, before any code). One page: *problem, goal, inputs/outputs, the components (boxes & arrows), the tech choices + why, what could go wrong.* This is also your architecture practice (see [04](04-architecture-roadmap.md)). Put it in the repo as `DESIGN.md`.
2. **Slice it into a "walking skeleton"**: the thinnest end-to-end version that *runs*. For P1: read 1 file → write it to a bronze table → done. Ugly is fine. **A running ugly thing beats a beautiful plan.**
3. **Iterate in vertical slices**, not horizontal layers. Add one *complete* capability at a time (e.g., "now add the silver layer with one transform + one test"), commit, repeat.
4. **Commit small and often** with clear messages. Your commit history *is* a portfolio signal.
5. **Write the README last but properly**: problem, architecture diagram, how-to-run, trade-offs, "what I'd do next." (See the README standard in [08](08-portfolio-strategy.md).)

### Where LLMs are OK on projects (different rule than DSA)
On *real projects*, an LLM is a legitimate tool — like a senior pairing with you. But discipline still applies:
- ✅ OK: unfamiliar library syntax, boilerplate, "what are options for X," explaining an error.
- ⚠️ Make yourself **read and understand every line** before committing it. If you can't explain it, don't ship it.
- ❌ Not OK: letting it architect the whole thing while you copy-paste. The *design* must be yours.

### "I don't know where to start" → start here
Pick the smallest dataset, the simplest tool, the first layer. Build the walking skeleton in your first weekend. Momentum solves the blank-page problem; planning more does not.

---

## 3. HOW to read a technical book (so it sticks)

Reading *DDIA* cover-to-cover passively = wasted hours. Instead:

1. **Read with a purpose question** for each chapter: "what problem does this solve?"
2. **Take notes in your own words** (in the repo). If you can't summarize a section in 2 sentences, re-read it.
3. **Connect to your work**: "this replication concept — where does it show up in Snowflake/Databricks?" Concepts stick when anchored to something real you've touched.
4. **Don't finish what isn't serving you.** Skim/skip chapters not relevant yet. Books are references, not novels.
5. **Pace:** ~1–2 hrs/weekend. DDIA will take months — that's expected and fine.

---

## 4. HOW to do system design practice

1. **Pick a system** from the list in [06](06-maang-prep.md) (start: URL shortener).
2. **Set a 45-min timer.** Solo, on paper or [Excalidraw](https://excalidraw.com).
3. **Follow the 7-step framework** in [06](06-maang-prep.md): clarify → estimate → API → high-level → data model → deep-dive → trade-offs.
4. **Then watch/read a reference solution** (ByteByteGo / Alex Xu's book) and compare. Note what you missed.
5. **Write a 1-page summary** into `system-design/` — your own playbook entry. Re-reading your own notes before interviews beats re-reading a book.

You're "good enough" when you can talk through any common system for 45 min, unprompted, covering trade-offs.

---

## 5. HOW to write a blog post (don't overthink it)

1. **Write about what you just built/learned** — P1, the eval harness, a Spark fix. Don't invent topics; document your real work.
2. **Outline with the Pyramid Principle** ([07](07-thinking-frameworks.md)): conclusion first, then 3 supporting points, then detail.
3. **Draft ugly, edit later.** First draft is allowed to be bad.
4. **Publish on dev.to or Medium + cross-post to LinkedIn.** Done > perfect. Nobody's judging post #1.
5. **~3–4 hrs total per post.** It doubles as interview prep (forces you to explain clearly).

---

## 6. The weekly operating rhythm (tie it all together)

- **Each weekday (2.5h):** 1h DSA (ritual above) + 1.5h current main track (read + small build).
- **Each weekend (8h/day):** the project (vertical slices) + 1 system design + 1 reading block + writing + your Sunday review.
- **Every Sunday (~30 min):** update `LEARNING-LOG.md`, update `REDO.md`, plan next week's specific problems/tasks. *Specific* — "Two Sum, 3Sum, P1 silver layer," not "do DSA."
- **Every month-end:** the monthly review template in [09](09-monthly-execution-plan.md).
- **Every quarter:** re-score the gap analysis in [01](01-assessment-and-gap-analysis.md).

---

## 7. The three rules that make all of this work

1. **Specificity beats motivation.** Never sit down to "study." Sit down to "solve Two Sum and Valid Anagram." Decide the exact task the night before. A vague plan = a skipped session.
2. **Showing up beats catching up.** Miss a day? Don't try to do 5 hours tomorrow. Just do today's normal block. The streak matters more than any single session.
3. **Finishing beats starting.** One finished project/problem/post is worth ten started ones. Resist the urge to jump to the next shiny thing before closing the current one.

> When in doubt about *how* to do anything in this roadmap: make it smaller, make it specific, set a timer, and start. You'll figure out the rest by doing — which is the entire point.
