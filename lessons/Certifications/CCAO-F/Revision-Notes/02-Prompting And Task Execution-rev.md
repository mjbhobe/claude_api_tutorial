# 02 · Prompting and Task Execution (Revision Notes)

## Where This Lesson Sits in the Exam

| Domain | Weight | Objectives covered here |
| :-- | :-- | :-- |
| **1 · Prompting and Task Execution** | **14%** | Create effective prompts · Apply task decomposition · Iterate prompts to improve output · Adapt strategy by task type (analysis, research, drafting, brainstorming) |

Overlap: diagnosing weak prompts also shows up in **Domain 7 (Troubleshooting & Optimization, 10%)**, and research/citation advice links to **Domain 2 (Output Evaluation, 21%)**.

**Core idea:** the same request phrased two ways gives two levels of quality. The model doesn't get smarter between them; **the prompt does**. Prompting is a **learnable communication discipline**, not a knack.

---

## Memory Map

```
PROMPTING AND TASK EXECUTION
│
├── DESCRIPTION (AI Fluency Framework competency)
│     = telling Claude precisely what you want; making every component explicit
│     Claude can't see inbox / org chart / last meeting unless a Connector gives access
│     (and even then only what you allowed) → anything else = CONTEXT GAP
│     Context gaps = #1 reason prompts underperform for new users
│
├── 5 COMPONENTS (mnemonic C·T·R·O·C, "See-Troc")
│     ├── Role ........ who Claude is → vocabulary, depth, assumptions
│     ├── Context ..... what Claude can't know → MOST OFTEN OMITTED
│     ├── Task ........ ONE primary verb, unambiguous (Summarize/Compare/Draft/Identify)
│     ├── Constraints . length, tone, include/exclude/avoid → usable without heavy edits
│     └── Output fmt .. table / bullets / 3-para memo / email → saves an iteration
│     Quick question = task (+ maybe constraint) · Client deliverable = ALL FIVE
│
├── DECOMPOSITION (big multi-stage tasks)
│     one prompt → shallow work on every stage, hidden reasoning
│     split into discrete, ORDERED steps, run in sequence
│     ├── Vendor eval: Criteria → Score → Trade-offs → Recommend
│     ├── Each step = checkable intermediate result; work becomes AUDITABLE
│     ├── Same chat: steps that build on each other
│     ├── New chat: step is independent OR context degrading (link to Lesson 01)
│     └── Parallel case: shared extraction FIRST → VERIFY → then parallel drafts
│
├── ITERATION (diagnose, don't rewrite)
│     ├── Generic/off-base ........ thin CONTEXT → add background
│     ├── Wrong question answered . ambiguous TASK verb → sharpen
│     ├── Wrong length/tone/shape . missing CONSTRAINT/FORMAT → add it
│     ├── Close, one section off .. iterate THAT section only, keep the draft
│     ├── Change ONE component, resend, compare
│     └── STOP when rounds give marginal change → quick manual edit instead
│
└── STRATEGY BY TASK TYPE (control vs latitude dial)
      ├── Analysis ...... TIGHT: criteria, standards, scope · loose: phrasing
      ├── Research ...... TIGHT: question, sources, citations · loose: synthesis approach
      │                    web search (quick) vs Research (deep, paid); verify citations
      ├── Drafting ...... TIGHT: audience, tone, format · loose: word choice (medium latitude)
      └── Brainstorming . TIGHT: goal + guardrails only · loose: quantity, direction
                           over-specifying kills divergence; volume first, narrow later
```

---

## 1. Description: The Backbone Competency

- **Description** is a competency in the **AI Fluency Framework**: telling Claude **precisely** what you want.
- It is the habit of making each prompt component **explicit** instead of assuming Claude will infer it.
- Claude **cannot see** your inbox, org chart, or last week's meeting **unless you connect a source through a Connector**.
- Even with a connector, Claude sees **only what you allowed it to access**.
- Anything that lives **only in your head** or **outside a connected source** is a **context gap**.
- **Context gaps are the single most common reason** a prompt underperforms for new users.

---

## 2. Anatomy of an Effective Prompt

Most weak prompts are **missing one or more components**. Naming them turns prompting from guesswork into a **checklist** to run before any non-trivial request.

### 2.1 The Five Components

| # | Component | What it is | Why it matters | Key note |
| :-- | :-- | :-- | :-- | :-- |
| 1 | **Role** | Who Claude should be (financial analyst, editor, policy reviewer) | Sets **vocabulary, depth, assumptions** | |
| 2 | **Context** | Background Claude can't know unless told: **audience, situation, prior decisions, source material** | Grounds the output | **Most often omitted** |
| 3 | **Task** | The specific action as a clear instruction | Tells Claude what to do | **One primary verb**, unambiguous (Summarize, Compare, Draft, Identify) |
| 4 | **Constraints** | Boundaries: **length, tone, what to include, what to leave out, what to avoid** | Keeps output **usable without heavy editing** | |
| 5 | **Output format** | Shape of the result: table, bullets, 3-para memo, draft email | Stating it **up front saves an iteration** | |

**Mnemonic: C·T·R·O·C ("See-Troc")** = **C**ontext · **T**ask · **R**ole · **O**utput format · **C**onstraints

### 2.2 How Many Components?

- **Not every prompt needs all five.**
- Quick question → **task** and maybe a **constraint**.
- **Client deliverable → all five.**
- The skill is **noticing which components a given task requires**.

### 2.3 Diagnosing a Weak Prompt

Hold a disappointing prompt against the stack; the gap is usually obvious.

| Missing / weak | Result |
| :-- | :-- |
| Context | **Generic** output |
| Ambiguous task verb | **Wrong action** |
| No constraints | **Wrong length or tone** |

The component stack doubles as a **diagnostic checklist** (used again in troubleshooting).

### 2.4 Worked Example

**Weak:** "Write a summary of our quarterly operations."
- Result: three plausible paragraphs that could describe almost any company.
- No audience, no figures, no format, no sense of priority.
- Output is **not wrong; it is unusable**, because the prompt specified almost nothing.

**Strong (components labelled):**
> "You are an operations analyst **(role)**. I am preparing a one-page update for our regional director, who cares about throughput and cost, not process detail **(context and audience)**. Summarize the attached Q3 operations data **(task)**, covering only the three metrics that moved more than 10 percent against target **(constraint)**. Format as a short headline followed by three bullet points, each one sentence **(output format)**."

- Same model, same data. Draft can be refined in **two minutes** instead of rebuilt.
- The difference is **entirely in the specification**.

**Habit to build:** before any prompt that matters, run the five components in your head. **Thirty seconds of specification saves several rounds of correction.**

---

## 3. Task Decomposition for Complex Requests

### 3.1 What and Why
- When a task has **several distinct stages**, one prompt produces **shallow work on every stage**.
- **Decomposition** = splitting a multi-part problem into **discrete, ordered steps**, then **running them in sequence** instead of asking for everything at once.

### 3.2 Vendor Evaluation Example ("four tasks wearing one sentence")

**Single prompt (underperforms):** "Evaluate these three vendors and tell me which to pick."
- Claude must **invent criteria, apply them, weigh trade-offs, recommend** in one pass.
- All four done **shallowly**; you **can't see the reasoning**.

**Decomposed version:**

| Step | Action |
| :-- | :-- |
| 1 · **Derive criteria** | From the requirements document, derive the criteria that matter and **weight** them |
| 2 · **Score vendors** | Score each vendor against those criteria using supplied materials |
| 3 · **Raise trade-offs** | Highlight where vendors **diverge most** |
| 4 · **Recommend** | Recommend, with reasoning **tied back to the weighted criteria** |

**Benefits**
- Each step gives a **checkable intermediate result**.
- Wrong criteria in Step 1 are caught **before scoring**, not after the recommendation.
- Work becomes **auditable** (matters when someone asks how the recommendation was reached).

### 3.3 One Conversation or Several?

| Situation | Choice |
| :-- | :-- |
| Sequential steps that **build on each other** | **Same conversation**, so each step sees prior results |
| A step that is **genuinely independent** | **Separate conversation** |
| Conversation so long that **early context is degrading** | **Separate conversation** (context management from Lesson 01) |

### 3.4 Parallel Case: Three Deliverables, One Foundation

**Scenario:** turn a dense **20-page policy change** into (1) an internal announcement, (2) a staff FAQ, (3) a short executive briefing.

| Step | Action |
| :-- | :-- |
| 1 | **Extract** the substantive changes and what each means in practice |
| 2 | **Confirm** the extraction is complete and accurate |
| 3 | Draft the **staff announcement** (general audience) from the confirmed list |
| 4 | Draft the **FAQ**, anticipating staff questions |
| 5 | Draft the **executive briefing**, compressed to **decisions and impact** |

**Why this order**
- Steps 1–2 build a **verified foundation** all three deliverables use.
- Drafting before the change list is confirmed risks **propagating the same misreading into three documents**.
- Rule: **sequence the shared, high-stakes extraction first; let the parallel drafts follow.**

---

## 4. Iterating Prompts to Improve Output

A first draft rarely lands perfectly. The skill is **not rewriting the whole prompt**; it is **reading the output to diagnose which component fell short**, then **fixing that one thing**.

### 4.1 Symptom → Cause → Fix (memorise)

| Symptom | Likely cause | Fix |
| :-- | :-- | :-- |
| Generic or off-base | **Thin context** | Add background Claude couldn't infer |
| Answered the wrong question | **Ambiguous task verb** | Sharpen the instruction |
| Wrong length, tone, or shape | **Missing constraint or format** | Add it |
| Close, but one section misses | (Draft is mostly right) | **Iterate on that section only**; don't discard the draft |

### 4.2 Targeted Revision, Not Wholesale Rewriting
- Rewriting everything **loses the parts that worked**.
- You also **can't tell which change fixed the problem**.
- Method: **change the one component the output told you to change → resend → compare.**
- Same discipline applies to troubleshooting any underperforming workflow (Domain 7).

### 4.3 Live Iteration Cycle (Delayed-Deliverable Email)

| Round | Prompt | Output | Diagnosis |
| :-- | :-- | :-- | :-- |
| 1 | "Write a follow-up email to the client about the delayed deliverable." | Generic, slightly defensive, 3 paragraphs; no new date, no cause | **Thin context** (no reason, no date) + **no tone constraint** |
| 2 | Adds: two-day delay on analytics deliverable; cause = data-quality issue now fixed; new date Thursday; tone accountable, not over-apologetic; under 120 words | Tight, accountable, cause + date + confident close | Strong; only **subject line missing** |
| 3 | "Good. Add a subject line that signals resolution, not just delay." | Marginal improvement | **Signal to stop** |

- Each round changed **exactly** the component the previous output exposed.
- **No round threw away working text.**

### 4.4 Knowing When to Stop
- Iteration has **converged** when extra rounds give **marginal change, not improvement**.
- Then a **quick manual edit** beats more prompting.
- Goal = **a usable result, not a perfect prompt.** Recognising diminishing returns is part of the skill.

---

## 5. Adapting Strategy by Task Type

The component stack applies to **every** prompt; the **emphasis** shifts. One fixed style across all task types **costs quality** on every task it doesn't fit.

### 5.1 The Four Task Types

| Task type | Approach | Latitude |
| :-- | :-- | :-- |
| **Analysis** | **Tight constraints, explicit criteria.** Say what to measure, against what standard, how to handle ambiguity. | **Low** latitude, high specification |
| **Research** | **Clear scope + source discipline.** Define question, boundaries, whether current sources are needed. **Ask for citations** so claims are checkable. Quick currency → **web search in Chat**; deep multi-source → **Research** (paid plans). | Scoped |
| **Drafting** | Specify **audience, tone, format**; leave room for phrasing. You control the shape, Claude fills it. | **Medium** latitude |
| **Brainstorming** | **Loose constraints, high latitude.** Give goal + boundaries, ask for **volume and range** before narrowing. **Over-specifying kills divergence.** | **High** latitude |

### 5.2 Quick Reference (memorise)

| Task type | Tighten | Loosen |
| :-- | :-- | :-- |
| Analysis | Criteria, standards, scope | Phrasing |
| Research | Question, sources, citations | Synthesis approach |
| Drafting | Audience, tone, format | Word choice |
| Brainstorming | Goal and guardrails only | Quantity and direction |

### 5.3 Mini-Demos

- **Analysis:** "Compare these two vendor contracts on payment terms, termination rights, and liability caps. For each, state which is more favorable to us and why, in a three-row table." → tight criteria, defined output.
- **Research:** "Using current sources, summarize how three named competitors positioned their Q2 launches. Cite each source. Flag anything you cannot verify." → scope + citation discipline; Research (or web search) supplies currency.
- **Drafting:** "Draft a 150-word LinkedIn post announcing our new reporting feature, aimed at operations managers, in a confident but not salesy voice." → audience, length, tone fixed; phrasing open.
- **Brainstorming:** "Give me 20 angles for a campaign around faster month-end close. Range widely; do not self-edit yet." → goal + one guardrail; constraints come **after** the range exists.

### 5.4 Citations Warning (exam favourite)
- Citations are **checkable** when they come from a **grounded source** (web search or Research results).
- Citations from **training memory alone** can look **equally confident** and **must be independently verified**.

**Underlying move every time:** decide **where you need control** and **where you need range**, then set constraints accordingly. This separates a competent prompter from one who gets the same mediocre output on every task.

---

## 6. Repairing an Underperforming Prompt (Case Study)

| | |
| :-- | :-- |
| **Weak prompt** | "Summarize the customer feedback and tell me what to do." |
| **Output** | Generic 5-bullet themes ("customers want faster support") + vague advice; not tied to data, no priorities, not actionable |
| **Real goal** | PM has **200 survey responses**; needs **top 3 issues by frequency**, each with a **representative quote**, **ranked**, to decide what to fix this quarter |
| **Diagnosis** | Missing **every** component: role, context, specific task, constraints, format |

**Repaired prompt:**
> "You are a product analyst **(role)**. Attached are 200 customer survey responses **(context)**. Identify the three most frequently raised issues **(task)**, ranked by how many responses mention each, and for each issue include one representative verbatim quote and the approximate share of responses it appears in **(constraints)**. **Use code execution to count accurately rather than estimating.** Format as a ranked list, most frequent first **(output format)**."

**What improved**
- Role + context → analysis **grounded in the actual responses**.
- Vague task → **specific, ranked, countable** instruction.
- Constraints (quote, share of responses) → **actionable** output.
- **Code execution** → frequency counts **verified, not guessed** (links to Lesson 01 capability layer).
- Output format → **decision-ready** result.

---

## Most Likely Questions

**Q1.** Which prompt component is most often omitted by users?
- A. Role
- B. Context
- C. Task
- D. Output format

**Answer: B**
**Why:** Context (audience, situation, prior decisions, source material) is named as the component most often left out. Context gaps are the single most common reason prompts underperform for new users. The others matter but are not singled out this way.

---

**Q2.** What does the "Role" component mainly set?
- A. The length of the response
- B. The vocabulary, depth, and assumptions Claude brings
- C. The file format of the output
- D. Which model Claude uses

**Answer: B**
**Why:** Role (financial analyst, editor, policy reviewer) shapes vocabulary, depth and assumptions. Length is a constraint (A). File shape is output format (C). Role has nothing to do with model choice (D).

---

**Q3.** A team member asks, "Can Claude just check what we agreed in last Tuesday's meeting?" No connector is set up and the notes were never shared. What is the issue?
- A. Claude needs a higher-tier model to recall meetings.
- B. This is a context gap; Claude can only see what you provide or allow through a connector.
- C. Claude can infer the agreement from general knowledge.
- D. Turning on Research will find the meeting notes.

**Answer: B**
**Why:** Claude can't see your inbox, org chart or meetings unless you provide the content or connect a source, and even then only what you allowed. A and C are wrong because no model can see private, unshared information. D searches public sources, not your private meetings.

---

**Q4.** Which statement best describes how many prompt components a request needs?
- A. Every prompt must contain all five components.
- B. Only client deliverables need a task verb.
- C. A quick question may need only a task and perhaps a constraint, while a client deliverable needs all five.
- D. Role is the only required component.

**Answer: C**
**Why:** The skill is noticing which components a task requires. A is the trap; not every prompt needs all five. B and D are false.

---

**Q5.** Claude answers a different question from the one you intended. Which component most likely failed?
- A. Context was thin
- B. The task verb was ambiguous
- C. Output format was missing
- D. Role was missing

**Answer: B**
**Why:** "Answered the wrong question" points to an ambiguous task verb; the fix is to sharpen the instruction. Thin context (A) gives generic output. Missing format or constraints (C) gives the wrong shape, length or tone.

---

**Q6.** A draft from Claude is generic and could describe any company. What is the best first fix?
- A. Switch to a more capable model.
- B. Add the background Claude could not infer: audience, figures, situation.
- C. Rewrite the whole prompt from scratch.
- D. Ask Claude to try again with the same prompt.

**Answer: B**
**Why:** Generic or off-base output points to thin context. Add the missing background. A doesn't fix missing information. C loses what worked and hides which change helped. D just produces another variation of the same gap.

---

**Q7.** A one-page memo is right except the risk section, which is too shallow. What should you do?
- A. Discard the draft and write a fully new prompt.
- B. Iterate on the risk section only and keep the rest of the draft.
- C. Switch to brainstorming mode.
- D. Start a new conversation with the original prompt.

**Answer: B**
**Why:** When output is close but misses on one section, iterate on that section only. Don't discard a draft that is mostly right. A and D throw away working text. C is the wrong strategy for the task.

---

**Q8.** Why is targeted revision preferred over rewriting the entire prompt? (Select 2)
- A. Rewriting loses the parts that already worked.
- B. Rewriting makes it impossible to tell which change fixed the problem.
- C. Claude penalizes long prompts.
- D. Rewriting always produces lower-quality output.

**Answer: A, B**
**Why:** These are the two reasons given. Change one component, resend, compare. C is invented. D is too absolute; the problem is diagnostic, not guaranteed lower quality.

---

**Q9.** After three rounds of iteration, each new round makes only tiny changes. What should you do?
- A. Keep iterating until the prompt is perfect.
- B. Recognise convergence and make a quick manual edit instead.
- C. Switch models and start over.
- D. Add all five components again.

**Answer: B**
**Why:** Iteration has converged when rounds give marginal change. A quick manual edit beats more prompting. The goal is a usable result, not a perfect prompt.

---

**Q10.** A manager prompts: "Evaluate these three vendors and tell me which to pick." What is the main weakness?
- A. The prompt is too short to process.
- B. Claude must invent criteria, apply them, weigh trade-offs and recommend in one pass, so all four are shallow and the reasoning is hidden.
- C. Vendor evaluation needs Research mode.
- D. Claude can't compare more than two vendors.

**Answer: B**
**Why:** This is "four tasks wearing one sentence". Decomposition fixes it. A, C, D are not reasons given in the lesson.

---

**Q11.** Put the decomposed vendor-evaluation steps in the correct order.
- A. Score vendors → Derive criteria → Recommend → Raise trade-offs
- B. Derive criteria → Score vendors → Raise trade-offs → Recommend
- C. Raise trade-offs → Derive criteria → Score vendors → Recommend
- D. Recommend → Derive criteria → Score vendors → Raise trade-offs

**Answer: B**
**Why:** Criteria (weighted, from the requirements doc) come first, then scoring against them, then trade-offs where vendors diverge, then a recommendation tied back to the weighted criteria. Scoring before criteria (A) has no standard to score against.

---

**Q12.** Which are benefits of task decomposition? (Select 3)
- A. Each step produces a checkable intermediate result.
- B. Errors in early steps are caught before later steps build on them.
- C. The work becomes auditable.
- D. It removes the need for human review.

**Answer: A, B, C**
**Why:** All three are stated benefits. D is false; decomposition makes review easier, it doesn't remove it.

---

**Q13.** You are on step 3 of a 4-step analysis where each step uses the previous step's results. Where should step 4 run?
- A. In a new conversation, to keep things tidy.
- B. In the same conversation, so it sees the prior results, unless early context is degrading.
- C. In Incognito mode.
- D. In a separate Project.

**Answer: B**
**Why:** Keep sequential, dependent steps in one conversation. Move to a new conversation only when a step is genuinely independent or context is degrading. A breaks the dependency. C and D are irrelevant.

---

**Q14.** A communications manager must turn a 20-page policy change into a staff announcement, an FAQ, and an executive briefing. What should happen FIRST?
- A. Draft the executive briefing, since it's the highest priority.
- B. Draft all three deliverables at once to save time.
- C. Extract the substantive changes and confirm the extraction is complete and accurate.
- D. Draft the FAQ, since staff questions drive everything.

**Answer: C**
**Why:** Sequence the shared, high-stakes extraction first and verify it. Drafting before the change list is confirmed risks spreading the same misreading into three documents.

---

**Q15.** Which task type calls for loose constraints and high latitude?
- A. Analysis
- B. Research
- C. Drafting
- D. Brainstorming

**Answer: D**
**Why:** Brainstorming wants volume and range; over-specifying kills divergence. Analysis wants tight criteria (low latitude). Research wants scope and source discipline. Drafting is medium latitude.

---

**Q16.** For a drafting task, what should you tighten and what should you leave open?
- A. Tighten word choice; leave audience open.
- B. Tighten audience, tone and format; leave word choice open.
- C. Tighten quantity; leave goal open.
- D. Tighten nothing; drafting needs full latitude.

**Answer: B**
**Why:** Drafting is medium latitude: you control the shape (audience, tone, format) and Claude finds the phrasing. A reverses it. C fits nothing. D describes brainstorming taken too far.

---

**Q17.** A compliance analyst asks Claude to compare two contracts on payment terms, termination rights and liability caps, stating which is more favourable for each, in a three-row table. Which strategy is this, and why does it work?
- A. Brainstorming; it asks for many options.
- B. Analysis; tight criteria and a defined output leave no room to wander.
- C. Drafting; it fixes tone.
- D. Research; it needs current sources.

**Answer: B**
**Why:** Analysis wants explicit criteria, standards and scope, with low creative latitude. The prompt names the criteria and the table format.

---

**Q18.** Claude gives you three citations for a claim during a normal chat, with web search and Research both off. What should you do?
- A. Trust them; citations prove the claim.
- B. Verify them independently, since citations from training memory can look equally confident.
- C. Ask Claude to rate how confident it is in the citations.
- D. Reformat them into a reference list.

**Answer: B**
**Why:** Citations are checkable when they come from a grounded source (web search or Research results). From training memory alone they can look just as confident and must be independently verified. C relies on self-reported confidence. D doesn't address accuracy.

---

**Q19.** Which TWO elements belong in a good research prompt? (Select 2)
- A. A clear question and boundaries, including whether current sources are needed
- B. A request for citations and a flag for anything unverifiable
- C. "Range widely; do not self-edit yet"
- D. A fixed word choice for every sentence

**Answer: A, B**
**Why:** Research wants clear scope and source discipline, with citations so claims are checkable. C is a brainstorming instruction. D over-controls phrasing and isn't relevant to research.

---

**Q20.** A PM's prompt "Summarize the customer feedback and tell me what to do" produced vague themes. The goal is the top three issues from 200 responses, by frequency, each with a quote. Which addition most directly makes the frequency counts trustworthy?
- A. Asking for a confident tone
- B. Instructing Claude to use code execution to count rather than estimate
- C. Adding a role of "senior executive"
- D. Asking for 20 themes instead of 3

**Answer: B**
**Why:** Code execution makes counts verified, not guessed. A doesn't affect accuracy. C changes the perspective but not the counting. D goes against the goal.

---

**Q21.** In the repaired customer-feedback prompt, which elements are constraints? (Select 2)
- A. "You are a product analyst"
- B. "Include one representative verbatim quote for each issue"
- C. "Include the approximate share of responses each issue appears in"
- D. "Format as a ranked list, most frequent first"

**Answer: B, C**
**Why:** The quote and share requirements are constraints that make the output actionable. A is the role. D is the output format.

---

**Q22.** In the delayed-deliverable email example, Round 1 produced a generic, slightly defensive email. What did Round 2 add?
- A. A new role only
- B. Context (cause, new date) and constraints (tone, under 120 words)
- C. A request for 20 alternative emails
- D. A switch to Opus

**Answer: B**
**Why:** Round 1 was diagnosed as thin context with no tone constraint. Round 2 added the cause (fixed data-quality issue), new date (Thursday), tone (accountable, not over-apologetic) and length (under 120 words). Each round changed exactly what the previous output exposed.

---

**Q23.** A colleague uses the same tightly specified style for every request, including brainstorming campaign ideas, and gets narrow, repetitive ideas. What is the best advice?
- A. Add even more constraints to the brainstorm.
- B. Loosen constraints for brainstorming: give the goal and guardrails, ask for volume and range, then narrow.
- C. Switch to Haiku for brainstorming.
- D. Use decomposition to split each idea into four steps.

**Answer: B**
**Why:** One fixed style costs quality on every task it doesn't fit. Over-specifying kills divergence. A makes it worse. C and D don't address the latitude problem.

---

**Q24.** In the strong Q3 operations prompt, "covering only the three metrics that moved more than 10 percent against target" is which component?
- A. Role
- B. Context
- C. Constraint
- D. Output format

**Answer: C**
**Why:** It sets a boundary on what to include. The role is "operations analyst". The context is the regional director who cares about throughput and cost. The format is a headline plus three one-sentence bullets.

---

**Q25.** What is the main lesson of the weak vs strong "quarterly operations summary" example?
- A. The stronger prompt used a more capable model.
- B. The weak output was factually wrong.
- C. With the same model and data, the difference in quality came entirely from the specification.
- D. Longer prompts are always better.

**Answer: C**
**Why:** "The model did not get smarter. The prompt did." The weak output was not wrong, just unusable (B is false). A is false; it was the same model. D overgeneralises; the point is the right components, not length.

---

## Key Takeaways

1. **The prompt sets the quality, not the model.** Description (AI Fluency Framework) means making every component explicit.
2. **Five components, C·T·R·O·C:** Context, Task (one clear verb), Role, Output format, Constraints. Context is the most often omitted. Client deliverables need all five; quick questions need fewer.
3. **Claude only knows what you give it** or allow through a connector. Context gaps are the top cause of weak output.
4. **Decompose big tasks** into ordered steps with checkable results (criteria → score → trade-offs → recommend). Keep dependent steps in one chat; split when independent or context degrades. For parallel deliverables, **extract and verify the shared foundation first**.
5. **Iterate by diagnosis:** generic = thin context, wrong question = vague verb, wrong shape/tone/length = missing constraint or format, one section off = fix that section only. Change one thing at a time. **Stop when changes become marginal.**
6. **Match strategy to task type:** Analysis tight, Research scoped with citations, Drafting medium, Brainstorming loose. Verify citations that don't come from web search or Research.
7. **Use code execution for counts** so numbers are verified, not estimated.
