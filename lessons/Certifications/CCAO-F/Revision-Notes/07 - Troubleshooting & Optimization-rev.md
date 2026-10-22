# 07 · Troubleshooting & Optimization (Revision Notes)

## Where This Lesson Sits in the Exam

| Domain | Weight | Objectives covered here |
| :-- | :-- | :-- |
| **7 · Troubleshooting and Optimization** | **10%** (smallest domain) | Identify, diagnose, and resolve issues with underperforming prompts or poor outputs · Adjust approach based on feedback and results · Optimize workflows for efficiency and effectiveness |

### Exam Objective → Where It Is Covered

| Domain 7 objective (exam guide) | Sections in these notes |
| :-- | :-- |
| **Identify, diagnose, resolve** underperforming prompts or poor outputs | 1.1 to 1.5 |
| **Adjust approach** based on feedback and results | 2.1 to 2.4 |
| **Optimize workflows** for efficiency and effectiveness | 3.1 to 3.6 |

**Core idea:** when output disappoints, most people either **give up** ("Claude can't do this") or **thrash** (change random things until something works). **Diagnostic skill replaces both with a sequence.** Underperformance has **findable root causes**; the sequence usually turns a dead end into a **five-minute fix**.

This lesson pulls together earlier lessons: the **five prompt components** (02), **context management** (01), **feature and model choice** (01, 03), and **configuration maintenance** (05).

---

## Memory Map

```
TROUBLESHOOTING & OPTIMIZATION
│
├── BAD DEFAULTS: GIVE UP or THRASH → replace with a DIAGNOSTIC SEQUENCE
│
├── 1. FAILURE PATTERNS (read the SYMPTOM TIMING)
│     ├── Under-specification ..... wrong from FIRST RESPONSE → add context/constraints/format
│     │                             (most common, cheapest)
│     ├── Context overload ........ DEGRADED OVER TIME in a good session → restart / summary
│     ├── Wrong feature or model .. SPECIFIC, REPEATABLE ERROR TYPE
│     │                             subtly-off numbers → code exec · shallow depth → model tier
│     ├── Stale configuration ..... "IT USED TO WORK" → maintenance (Lesson 05 checklist)
│     └── Expectation mismatch .... task was never a fit → RESHAPE the task (range + assumptions)
│
├── DIAGNOSTIC SEQUENCE (cheapest fix first; don't skip to step 5)
│     1 Prompt vs 5 components → 2 Conversation length → 3 Feature & model →
│     4 Configuration current? → 5 Only then: is the task a fit?
│     Common inversion: "use the most capable model" / "impossible" first = expensive
│     Ends in: cheap specific fix (usually) or reasoned "reshape the task" (sometimes)
│
├── 2. ADJUSTING FROM FEEDBACK
│     ├── Every bad output = diagnostic data about the SETUP
│     ├── Feedback loops in recurring work: same weekly correction = setup missing something
│     ├── REACTION ("too generic") → INSTRUCTION ("add the audience")
│     │     Ask: what must be present to be right, and which LEVER controls it?
│     │     (prompt · context loaded · configuration) · can't name lever = still a reaction
│     └── CAPTURE what worked: phrasing → standing instruction · multi-step fix → Skill
│           Test: will this correction be needed again (by me or anyone)? → configuration
│           Memory = per-user, best-effort · configuration = deliberate, shared, reliable
│           Captured (marketer) vs Lost (analyst + test accounts)
│
└── 3. OPTIMIZING WORKFLOWS (deliberate: instrument → find friction → promote)
      ├── Friction signals: REPETITION → saved context/instruction ·
      │     CORRECTION → config change · VARIANCE → shared Skill/KB
      │     Find it: run one cycle, write down EVERY manual step = backlog
      ├── CONSOLIDATE steps · PROMOTE patterns into Projects and Skills
      ├── RULE → instructions · REFERENCE → knowledge base · PROCEDURE → Skill
      ├── Promote with caution: run a few cycles with old approach available, then commit
      ├── MEASURE: time per cycle · revision rounds · consistency · quality
      │     pick the metric that matches WHY it matters; stop when good enough
      └── Audit: 45 → 25 min, consistent format, one fewer revision round
```

---

## 1. Diagnosing Underperformance

### 1.1 Common Failure Patterns and Root Causes

| Pattern | What's happening | Fix |
| :-- | :-- | :-- |
| **Under-specification** | Prompt left out **context, constraints, or format**. **Most common cause and cheapest to fix** | **Add what was missing** |
| **Context overload** | Long conversation near the context limit; **earlier context summarized** to make room; detail compresses, **early instructions lose force** | **Restart or summarize**, **not a better prompt** |
| **Wrong feature or model** | Calculation asked for **in prose instead of code execution**, or **deep analysis from a speed-tier model** | **Use the right tool**, **not more prompting** |
| **Stale configuration** | A standing instruction, knowledge source, or Skill has **drifted out of date**, degrading output **silently** | **Maintenance** |

### 1.2 Read the Symptom Timing (memorise)
The patterns produce **similar-looking bad output**, so the skill is reading **when and how** the problem shows up.

| Symptom timing / pattern | Pattern | Why |
| :-- | :-- | :-- |
| **Wrong from the very first response** | **Under-specification** | The prompt **never carried what it needed** |
| **Started fine, degraded as the conversation grew** | **Context overload** | Early context compressed |
| **Specific, repeatable error types** | **Wrong feature or model** | **Subtly-off numbers** → needs **code execution**; **shallow analysis** on a task needing depth → **wrong model tier** |
| **"It used to work"** (good last month, not now) | **Stale configuration** | Something it depends on **drifted** |

Shorthand: **first-response-wrong · degraded-over-time · specific-error-type · used-to-work**. Each points to a **different fix**.

### 1.3 Isolating the Cause
**Before blaming the tool, locate the failure.** Is it:
- the **prompt** (specification),
- the **context** (window full, or **wrong material loaded**),
- the **feature choice** (wrong **entry point, model**, or **no code execution**), or
- an **expectation mismatch** (the task was **never one Claude could do well**)?

Naming which one **points straight to the fix**.

> **How the lists fit together:** the lesson names **four failure patterns** (under-specification, context overload, wrong feature or model, stale configuration), but this "isolate the cause" list swaps stale configuration for **expectation mismatch**, and the gallery shows **five** cases. Learn all five: the four fixable patterns (diagnostic steps 1 to 4) plus expectation mismatch (step 5).

### 1.4 The Diagnostic Sequence (run in order)

| Step | Check | Relative cost |
| :-- | :-- | :-- |
| 1 | **Re-read the prompt against the five components**: anything under-specified? | **Seconds**; fixes the **most common** failure |
| 2 | **Check conversation length**: context overloaded, needs a **restart or summary**? | A little more effort |
| 3 | **Check feature and model**: a calculation needing **code execution**, or a complex task on a **speed-tier model**? | More |
| 4 | **Check configuration**: are instructions, knowledge, and Skills **current**? | More |
| 5 | **Only then** question whether the task **fits at all** | **Most expensive conclusion**: it **ends the attempt** |

- **Cheapest-fix-first on purpose.**
- **Most people invert this**: they jump to **"switch to the most capable model"** or **"this task is impossible"** first, the expensive moves that **usually weren't needed**.
- **Discipline = resisting the urge to skip to step 5.**
- Run end to end, the sequence takes **a minute or two** and ends in one of two places:
  - a **specific, cheap fix** (most of the time), or
  - a **confident, reasoned "this task needs reshaping"** (occasionally).
- **Both are wins**: each replaces the two bad defaults with **a decision you can explain**.
- **Habit:** reach for the sequence **automatically** the moment output disappoints, **before forming an opinion about whose fault it is**.

### 1.5 Worked Example: Failure Gallery (five failures, five diagnoses)

| Complaint | Diagnosis | Fix |
| :-- | :-- | :-- |
| "The summary keeps **missing key points**." | **Under-specification**: prompt never said which points matter | **Name the criteria for "key"** |
| "It **stopped following my format halfway through**." | **Context overload** in a long session | **Restart from a summary**, or **persist the format to a standing instruction** |
| "The **numbers are subtly wrong**." | **Wrong feature** | **Move the calculation to code execution** |
| "It **worked last month, now it's off**." | **Stale configuration** | Run the **Lesson 05 maintenance checklist** |
| "I asked it to **predict next quarter's exact sales** and the number was wrong." | **Expectation mismatch** (the **step-5** case) | **Reshape the task**: ask for a **range with stated assumptions**, or a **model of the drivers you can adjust** |

- For expectation mismatch, **no prompt, restart, feature, or configuration change fixes it**: the task asks for something the tool **can't do** (predict a future number **with precision**).
- **Recognizing a genuine mismatch is as much a skill as fixing a fixable failure**; it stops you burning time tuning a prompt for an output that **was never available**.

---

## 2. Adjusting Approach from Feedback and Results

**Every disappointing output is diagnostic data.** Fixing the same problem by hand each time it recurs lets that data **evaporate**. The skill: **translate critique into a specific adjustment, then capture the fix so it persists**.

### 2.1 Build Feedback Loops into Recurring Work
- Treat each round's output as **a signal about the setup**.
- A recurring report needing **the same manual correction every week** is telling you the **prompt, context, or configuration is missing something**.
- Habit: after each round, ask **what the output revealed about the system that produced it**.

### 2.2 Translate Critique into a Specific Adjustment
- "This isn't quite right" **improves nothing**. Convert it to the **precise change**: **which component, which context, which configuration setting**.
- The adjustment must be **specific enough to act on and to check**.

**Reaction vs instruction**

| Reaction (how it feels) | Instruction (what to change) |
| :-- | :-- |
| "Too generic" | "Add the audience to the context" / "Name the audience and the one action I want them to take" |
| "Wrong tone" | "Add a tone constraint to the standing instruction" |
| "Missed the point" | "State the single question the output must answer up front" |

- **How to make the jump:** ask "**What specifically would have to be present for this to be right, and which part of the setup controls that?**"
- Each translation points to a **specific lever**: **the prompt, the context loaded, or a configuration setting**. That lever is where the fix goes.
- **If you can't name the lever, the critique is still a reaction, and the next attempt will be a guess.**

### 2.3 Capture What Worked
- **Don't leave a working fix in a one-off conversation** where it will be lost. **Promote it**:
  - a **phrasing** that reliably works → **standing instruction**
  - a **multi-step fix** → **Skill**
- Capturing turns **a lucky round into a permanent improvement**.
- **Expensive failure mode: finding the fix, then losing it.** An uncaptured fix is **rediscovered** next week **and by whoever else runs the task**; each rediscovery costs the same, **multiplied by every person and every cycle**.
- Capture **once** (standing instruction in the Project, or Skill) → **repeated cost becomes one-time cost**.
- **Test for promotion:** "**Will this same correction be needed again, by me or someone else?**" If yes → **configuration**.
- **Memory vs configuration:** Claude's **Memory may pick up patterns you repeat**, but it is **per-user and best-effort**. **Configuration is the deliberate, shared, reliable home** for a fix.

### 2.4 Worked Example: Captured vs Lost

| | Captured | Lost |
| :-- | :-- | :-- |
| Who | **Marketer** | **Analyst** |
| Recurring problem | Every campaign-brief draft **omits the target segment** and **buries the call to action** | Monthly report must **exclude internal test accounts** |
| What they did | Added **two standing instructions** to the briefs Project: "Always state the target segment in the first line" and "Place the call to action in its own closing section" | Found the right instruction in month one but **kept it in conversation**, retyping it monthly |
| Outcome | **Next draft arrives correct**; recurring weekly correction removed | Six months later still typing it; a **covering colleague didn't know**, and **a report shipped with test data** |
| Lesson | One round of feedback **captured into configuration** | **The fix existed the whole time; the failure was leaving it uncaptured** |

---

## 3. Optimizing Workflows for Efficiency and Effectiveness

**Optimization is deliberate, not accidental.** You **instrument the workflow, find the friction, promote the fix into configuration**. Done well it **compounds**: each redundancy removed and pattern promoted makes the workflow **faster and more consistent for everyone**.

### 3.1 Find Redundancy and Friction
- Look for steps that **repeat unnecessarily**: **same context pasted** every session, **same correction** every round, **same manual reformatting** at the end. Configuration can remove each.
- Friction is **easy to live with and hard to see**, because you **absorb it one session at a time**.
- **How to find it:** watch **one full cycle** and note **every step you do by hand that you also did last time**. Still can't see it? Run it once with the **explicit job of writing down every manual step**. **That list is your optimization backlog.**

**Three friction signals and fixes (memorise)**

| Signal | Looks like | Fix |
| :-- | :-- | :-- |
| **Repetition** | You paste or type the same thing every run | **Saved context or a standing instruction** |
| **Correction** | You fix the same flaw in every output | **A configuration change** so the flaw stops appearing |
| **Variance** | Different people running the same task get **different results** | **A shared Skill or knowledge base** so everyone runs the same setup |

### 3.2 Consolidate and Promote
Two moves do most of the work:
1. **Consolidate** steps that can run **together** instead of as separate prompts.
2. **Promote** repeated patterns into **Projects and Skills**:
   - context you paste every time → **knowledge base or standing instructions**
   - a procedure you run every time → **Skill**

**Promotion turns a personal workaround into a team-wide efficiency.**

### 3.3 The Rule · Reference · Procedure Test (where a fix belongs)

| Fix is a… | Example | Home |
| :-- | :-- | :-- |
| **Rule** that should always apply in a Project | "Always include the target segment" | **Standing instruction** |
| **Reference** every run needs | "Our brand voice guide", "the current product list" | **Project knowledge base** |
| **Procedure** with steps | "Generate the weekly report in this exact format and order" | **Skill** |

- **Wrong home = optimization that doesn't stick:**
  - a **procedure pasted as a one-line instruction loses its steps**;
  - **reference material crammed into an instruction bloats every prompt**.

### 3.4 Promote with Caution
- **Not every change is an improvement.**
- When you move a fix into configuration, **run the workflow a few cycles with the old approach still available** before fully relying on the new setup.
- If the optimized version is **worse or less predictable**, catch it **before it has shipped several times**.
- Compounding works both ways: real **compounding benefit**, but also **compounding cost of a bad change** baked into a workflow everyone uses.
- **Prove the gain on a few runs, then commit.**

### 3.5 Measure the Improvement
- **Optimization you can't measure is hard to justify or sustain.**
- Track concrete gains: **time saved per cycle**, **revision cycles reduced**, **consistency across people**. E.g., **40 → 25 minutes**, or **three revision rounds → one**.
- **Time is the easiest metric but not always the one that matters most.** Other real gains:
  - **Consistency**: same format, same issues caught, **whoever runs it**.
  - **Quality**: **fewer errors reach the final product**.
- **Pick the metric that matches why the workflow matters:**

| Workflow | Optimize for |
| :-- | :-- |
| **Customer-facing report** | **Consistency and accuracy** more than raw speed |
| **Internal draft** | **Time** |

- Choosing the metric **up front** also tells you **when to stop**: optimization has **diminishing returns**; once the metric is **good enough**, further tuning is **its own kind of friction**.

### 3.6 Worked Example: Workflow Efficiency Audit

**Before:** weekly reporting takes **about 45 minutes per analyst**; **outputs vary by who runs it**.

| Friction found | Type | Home | Fix |
| :-- | :-- | :-- | :-- |
| Each analyst **re-pastes the same background** | **Reference** | **Knowledge base** | Move background into a **shared Project knowledge base** |
| Each **reformats output by hand** | **Procedure** | **Skill** | Add a **Skill for the report format** |
| Each **catches different things** | **Rule** | **Standing instruction** | Set a **standing instruction for the verification step** |

**After:** **about 25 minutes per analyst**, **consistent format across the team**, **one fewer revision round**.
- Friction was **found by instrumenting the workflow**; the gain came from **promoting the fixes into configuration**.
- Sorting each friction into **rule, reference, or procedure** turns **a list of annoyances into a concrete set of changes**.

---

## Note on the Lesson's Disclaimer

The lesson includes an educational-content disclaimer: the course is **not legal, financial, or professional advice**; products **change quickly**, so content may be **outdated**; examples are **illustrative and often fictitious**; company mentions **don't imply endorsement or affiliation**; and Anthropic's **terms, policies and documentation take precedence** over course content. This is not an exam objective, but it reinforces "verify current product behaviour".

---

## Links to Other Lessons (Tested Under Domain 7)

| Earlier point | Lesson | How it shows up here |
| :-- | :-- | :-- |
| **Five prompt components** (Role, Context, Task, Constraints, Output format; C·T·R·O·C) | 02 | Diagnostic step 1 checks the prompt against them |
| **Symptom → cause → fix table**: generic = thin context; wrong question = ambiguous verb; wrong length/tone/shape = missing constraint/format; one section off = iterate that section only | 02 | Under-specification diagnosis in detail |
| **Change one component at a time**; stop when rounds give marginal change | 02 | Targeted adjustment, not thrashing |
| **Context warning signs** and **Restart · Summarize · Persist** (Project instructions and knowledge base carry into a new chat; the thread does not) | 01 | Fix for context overload (step 2) |
| **Model tiers**: Haiku = speed/volume; Sonnet = default; Opus = complex, nuanced, high-stakes | 01 | Fix for "shallow analysis" (step 3) |
| **Code execution** for numbers that must be right (still read and verify the code) | 01, 03 | Fix for "subtly wrong numbers" (step 3) |
| **Maintenance checklist**: instructions current, no superseded docs, right Skills enabled; custom Skills change only on re-upload | 05 | Fix for stale configuration (step 4) |
| **Instruction / knowledge / Skill** slot choice | 05 | Same as the rule · reference · procedure test |
| **Iteration vs escalation**: flat improvement on high-stakes work → human expert | 03 | When troubleshooting stalls on a high-stakes output, escalate |

---

## Exam Traps

1. **Jumping straight to "use the most capable model".** That's step 3 at best, and usually unnecessary. Start with the **prompt** (step 1, cheapest).
2. **Concluding "Claude can't do this" early.** Task fit is **step 5**, the most expensive conclusion. Rule out the cheaper causes first.
3. **Writing a better prompt for context overload.** If a good session degraded over time, the fix is **restart or summarize**, not a better prompt.
4. **Prompting harder for subtly-wrong numbers.** Wrong feature: move the calculation to **code execution**.
5. **Fixing a "used to work" problem with prompt tweaks.** It's **stale configuration**: run maintenance.
6. **Misreading symptom timing.** First response wrong = **under-specification**. Degraded over time = **context overload**. Specific repeatable error = **wrong feature/model**. Used to work = **stale configuration**.
7. **Tuning prompts for an impossible output** (exact future sales). That's **expectation mismatch**: **reshape the task** (range plus assumptions, or a driver model).
8. **Vague critique as feedback** ("not quite right"). Convert the reaction into an **instruction tied to a lever** (prompt, context, configuration).
9. **Leaving a working fix in the chat.** Promote it: phrasing → **standing instruction**; multi-step fix → **Skill**.
10. **Relying on Memory to remember team fixes.** Memory is **per-user and best-effort**; configuration is **deliberate, shared, reliable**.
11. **Putting a procedure in a one-line instruction** (loses its steps) or **reference material in an instruction** (bloats every prompt). Use **rule → instruction, reference → knowledge base, procedure → Skill**.
12. **Committing to an optimization immediately.** Run a few cycles with the old approach still available, then commit.
13. **Measuring only time saved.** For customer-facing work, **consistency and accuracy** may matter more.
14. **Optimizing forever.** Once the chosen metric is **good enough**, stop; more tuning is friction.
15. **Variance across people fixed by "everyone write better prompts".** Fix with a **shared Skill or knowledge base**.
16. **Blaming the tool before locating the failure.** Locate it first: prompt, context, feature choice, or expectation mismatch.

---

## Most Likely Questions

**Q1.** [Easy] What is the most common cause of underperforming output, and the cheapest to fix?
- A. Context overload
- B. Under-specification
- C. Stale configuration
- D. Wrong model tier

**Answer: B**
**Why:** Prompts that leave out context, constraints or format are the most common failure. Adding what's missing costs seconds.

---

**Q2.** [Medium] An output was wrong from the very first response. Which pattern is most likely?
- A. Context overload
- B. Stale configuration
- C. Under-specification
- D. Expectation mismatch

**Answer: C**
**Why:** First-response-wrong means the prompt never carried what it needed. Context overload shows up after a good start. Stale configuration shows up as "it used to work".

---

**Q3.** [Medium] A session followed your format perfectly for an hour, then drifted. What is the best fix?
- A. Rewrite the prompt with more detail.
- B. Restart from a summary, or persist the format to a standing instruction.
- C. Switch to Haiku.
- D. Conclude the task doesn't fit.

**Answer: B**
**Why:** Degraded-over-time points to context overload. Earlier context was summarized and detail compressed. The fix is a restart or summary (or persisting the rule), not a better prompt.

---

**Q4.** [Easy] Financial totals in Claude's prose output are subtly off every time. What is the fix?
- A. Ask Claude to be more careful.
- B. Move the calculation to code execution.
- C. Restart the session.
- D. Add a tone constraint.

**Answer: B**
**Why:** Subtly-off numbers are a specific, repeatable error type pointing to the wrong feature. Calculations belong in code execution, not prose.

---

**Q5.** [Medium] A deep strategic analysis comes back shallow on every attempt, even with a well-specified prompt in a fresh chat. What should you check next in the sequence?
- A. Whether the task is impossible
- B. The feature and model: a complex task may be running on a speed-tier model
- C. Memory settings
- D. Incognito mode

**Answer: B**
**Why:** With the prompt and context ruled out, step 3 checks feature and model. Shallow analysis on a task needing depth points to the wrong model tier. A is step 5, the last resort.

---

**Q6.** [Medium] A monthly report Project produced good output last month but is now off, with no change to how anyone prompts. What is the diagnosis?
- A. Under-specification
- B. Stale configuration; run the maintenance checklist
- C. Context overload
- D. Expectation mismatch

**Answer: B**
**Why:** "It used to work" signals stale configuration. Something it depends on (instruction, knowledge, Skill) has drifted.

---

**Q7.** [Easy] Put the diagnostic sequence in order.
- A. Task fit → Model → Prompt → Context → Configuration
- B. Prompt → Conversation length → Feature & model → Configuration → Task fit
- C. Configuration → Prompt → Task fit → Model → Context
- D. Model → Prompt → Context → Task fit → Configuration

**Answer: B**
**Why:** The sequence runs cheapest fix first: re-read the prompt (seconds), check context length, check feature/model, check configuration, and only then question task fit.

---

**Q8.** [Medium] Why is "question whether the task is a fit at all" placed last?
- A. It's the least important step.
- B. It's the most expensive conclusion: it ends the attempt, so cheaper causes must be ruled out first.
- C. Claude can't assess task fit.
- D. It requires admin approval.

**Answer: B**
**Why:** Concluding the task doesn't fit ends the attempt. Most people invert the sequence; discipline means resisting the urge to skip to step 5.

---

**Q9.** [Hard] A sales lead asks Claude to predict next quarter's exact revenue. The number turns out wrong, and prompt tweaks don't help. What is the correct response?
- A. Switch to the most capable model and retry.
- B. Add more historical data and demand an exact figure.
- C. Recognize an expectation mismatch and reshape the task: ask for a range with stated assumptions, or a model of the drivers.
- D. Restart the conversation.

**Answer: C**
**Why:** No prompt, restart, feature or configuration change fixes a request for something the tool can't do (predict a future number precisely). Reshape it into a task that fits.

---

**Q10.** [Hard] Which reflect the "isolating the cause" step? (Select 3)
- A. Check whether the prompt is under-specified
- B. Check whether the context window is full or the wrong material is loaded
- C. Check whether the wrong entry point, model, or no code execution was used
- D. Blame the tool first, then investigate

**Answer: A, B, C**
**Why:** Before blaming the tool, locate the failure: prompt, context, feature choice, or expectation mismatch. D is exactly what the lesson warns against.

---

**Q11.** [Medium] A manager's feedback on a draft is "It's too generic." Which converts this reaction into an instruction?
- A. "Make it better."
- B. "Name the audience and the one action I want them to take."
- C. "Try again."
- D. "Use a more capable model."

**Answer: B**
**Why:** An instruction names what to change and points to a lever (here, context). If you can't name the lever, the critique is still a reaction and the next attempt is a guess.

---

**Q12.** [Medium] Which question best helps turn a critique into a specific adjustment?
- A. "Whose fault is this?"
- B. "What specifically would have to be present for this to be right, and which part of the setup controls that?"
- C. "Which model is the newest?"
- D. "How long is the output?"

**Answer: B**
**Why:** This finds the missing element and the lever (prompt, context loaded, or configuration setting) where the fix goes.

---

**Q13.** [Medium] An analyst found the right instruction to exclude internal test accounts in month one but retyped it every month. A colleague covering for them didn't know, and a report shipped with test data. What was the real failure?
- A. Claude ignored the instruction.
- B. The fix was never captured into configuration (a standing instruction), so it was lost.
- C. The model was too small.
- D. Memory was off.

**Answer: B**
**Why:** The fix existed the whole time; the failure was leaving it in conversation. A standing instruction would have applied for anyone running the task.

---

**Q14.** [Hard] Why is configuration preferred over Memory as the home for a recurring team fix? (Select 2)
- A. Memory is per-user and best-effort.
- B. Configuration is deliberate, shared and reliable.
- C. Memory can't store text.
- D. Configuration updates itself automatically.

**Answer: A, B**
**Why:** Memory may pick up patterns you repeat, but only for you and not reliably. Configuration (standing instructions, Skills) applies to everyone who runs the task. D is false; configuration must be maintained.

---

**Q15.** [Medium] Match each friction signal to its fix. "Different analysts running the same task get different results."
- A. Saved context or a standing instruction
- B. A configuration change so the flaw stops appearing
- C. A shared Skill or knowledge base so everyone runs the same setup
- D. Switch everyone to Opus

**Answer: C**
**Why:** That's variance. A fits repetition. B fits correction (the same flaw every output).

---

**Q16.** [Medium] Using the rule · reference · procedure test, where does "our current product list" belong?
- A. Standing instruction
- B. Project knowledge base
- C. Skill
- D. Memory

**Answer: B**
**Why:** It's a reference every run needs. Rules go to standing instructions; procedures with steps go to Skills.

---

**Q17.** [Hard] A team pasted its eight-step weekly report procedure into one line of the standing instructions, and outputs keep skipping steps. What went wrong?
- A. The model tier is too low.
- B. The fix landed in the wrong home: a procedure pasted as a one-line instruction loses its steps; it belongs in a Skill.
- C. The knowledge base is too large.
- D. Context overload.

**Answer: B**
**Why:** Wrong home is why some optimizations don't stick. Procedures go to Skills.

---

**Q18.** [Medium] You've just moved a fix into a shared Project's configuration. What is the recommended next step?
- A. Remove the old approach immediately.
- B. Run the workflow a few cycles with the old approach still available, then commit once the gain is proven.
- C. Tell the team the workflow is now fully automated.
- D. Stop measuring.

**Answer: B**
**Why:** Not every change is an improvement, and a bad change baked into a shared workflow compounds. Prove the gain on a few runs, then commit.

---

**Q19.** [Hard] A team is optimizing a customer-facing monthly statement summary. Which metric should lead?
- A. Raw speed only
- B. Consistency and accuracy
- C. Number of prompts used
- D. Length of output

**Answer: B**
**Why:** Pick the metric that matches why the workflow matters. Customer-facing reports optimize consistency and accuracy more than speed; internal drafts optimize time.

---

**Q20.** [Hard] A weekly reporting workflow takes 45 minutes per analyst and varies by person. Analysts re-paste the same background, reformat by hand, and catch different things. Which mapping of fixes is correct? (Select 3)
- A. Background → shared Project knowledge base
- B. Report format → Skill
- C. Verification step → standing instruction
- D. Background → Skill

**Answer: A, B, C**
**Why:** Reference → knowledge base, procedure → Skill, rule → standing instruction. The result was about 25 minutes, a consistent format, and one fewer revision round. D puts reference material in the wrong home.

---

## Key Takeaways

1. **Don't give up or thrash; diagnose.** Underperformance has findable causes, and the sequence usually yields a quick fix.
2. **Read the symptom timing:** first-response-wrong = **under-specification**; degraded-over-time = **context overload**; specific repeatable error = **wrong feature or model**; used-to-work = **stale configuration**. A task that was never a fit = **expectation mismatch**: reshape it.
3. **Run the sequence cheapest-first:** prompt → conversation length → feature & model → configuration → task fit. Don't jump to "bigger model" or "impossible".
4. **Turn reactions into instructions** by naming the lever (prompt, context, configuration).
5. **Capture fixes:** phrasing → standing instruction, multi-step fix → Skill. Memory is per-user and best-effort; configuration is shared and reliable. Uncaptured fixes get rediscovered at full cost by everyone.
6. **Optimize deliberately:** look for repetition, correction and variance; consolidate and promote. Use **rule → instruction, reference → knowledge base, procedure → Skill**.
7. **Promote with caution and measure:** trial a few cycles, then commit. Track time, revision rounds, consistency or quality, depending on why the workflow matters, and stop when the metric is good enough.
