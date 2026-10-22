# 04 · Workflow Integration & Solution Design (Revision Notes)

## Where This Lesson Sits in the Exam

| Domain | Weight | Objectives covered here |
| :-- | :-- | :-- |
| **4 · Workflow Integration and Solution Design** | **16%** (2nd largest) | Apply Claude to analyze requirements and use cases · Use Claude for research, planning, process optimization · Support solution design, development, iteration · Integrate Claude into existing workflows to augment or redesign them · Communicate Claude's value and limitations to stakeholders |

**Core idea:** "I use Claude" (personal productivity habit) is different from **"our workflow uses Claude"** (a repeatable team process where Claude performs specific steps every time). Value **compounds** only when you make that shift **deliberately**; it goes wrong when teams **automate the wrong steps**.

**Opening case: two teams, same tool, same contract-review process**

| | Team 1 | Team 2 |
| :-- | :-- | :-- |
| Approach | **Mapped the work**; Claude drafted the redline; **a lawyer owned every final decision** | Pointed Claude at **the whole process**; let it **approve low-risk clauses unsupervised** |
| Result | **Review time halved, quality held** | Within a month an approved clause created an **obligation no one caught**; team **pulled the tool entirely** |

The difference was **which steps each team chose to delegate**.

**Anchor competency (AI Fluency Framework): Delegation** = deciding, **for each step**, whether the work is **AI-appropriate, human-retained, or collaborative**. Deliberate delegation turns individual wins into workflow value.

### Exam Objective → Where It Is Covered

| Domain 4 objective (exam guide) | Sections in these notes |
| :-- | :-- |
| Apply Claude to **analyze requirements and use cases** | 1.1 to 1.4 |
| Leverage Claude for **research, planning, and process optimization** | 2.1 to 2.4 |
| Support **solution design, development, and iteration** | 3.1 to 3.3 |
| **Integrate** Claude into existing workflows to **augment or redesign** them | 4.1 to 4.6 |
| **Communicate** Claude's **value and limitations** to stakeholders | 5.1 to 5.6 |

---

## Memory Map

```
WORKFLOW INTEGRATION & SOLUTION DESIGN
│
├── "I use Claude" (habit) → "OUR WORKFLOW uses Claude" (repeatable team process)
│     Anchor competency: DELEGATION (AI-appropriate / human-retained / collaborative)
│
├── 1. ANALYZING REQUIREMENTS
│     ├── Messy inputs → STRUCTURED, TESTABLE requirements (not narrative summary)
│     │     extract · organize · flag ambiguous / missing
│     ├── "We need better reporting" → what report, for whom, how often, what data, what format
│     ├── RFP example: table = label · RFP section · answered? · ambiguity
│     │     run as a PROJECT: KB = past winning proposals · Skills = formatting
│     │     standing instructions = extraction format · Skills are ACCOUNT-level
│     └── PRESSURE-TEST: ask Claude to challenge its own list → hidden requirements
│           extraction + pressure-test > either alone (= Discernment at requirements stage)
│
├── 2. RESEARCH, PLANNING, PROCESS OPTIMIZATION
│     ├── Synthesis (Claude excels) vs Calculation (must be verified)
│     ├── Current info: web search (quick) / Research (deep); verify synthesis
│     ├── Numbers → CODE EXECUTION ("guessed utilization = guess; computed = plan")
│     ├── Capacity plan: code exec on 4 quarters → Claude synthesizes recommendation
│     │     + shows assumptions → defensible line by line
│     └── Synthesis steps = most Claude value · Judgment steps (risk appetite,
│           politics, budget, hiring freeze) = STAY HUMAN
│
├── 3. SOLUTION DESIGN & ITERATION
│     ├── Design collaborator, not vending machine
│     ├── Loop: IDEATE → PROTOTYPE → GATHER FEEDBACK → REFINE (repeat)
│     ├── Run inside a PROJECT → stable context, constraints, prior decisions
│     ├── Dashboard artifact: Build → Filter & totals → Color & print (no code written)
│     └── ESCALATE when others depend on it (uptime, security, integration)
│           → Developer / Architect
│
├── 4. DELEGATION MAPPING (core skill)
│     ├── Each step: AI-appropriate / Human-retained / Collaborative
│     ├── 3 criteria: REVERSIBILITY · STAKES · ACCOUNTABILITY (never delegates)
│     ├── Embed features: Skill = repeatable procedure · Code exec = data steps
│     │     Human steps = explicit REVIEW GATES
│     ├── Over-delegation: drafting quality ≠ licence to delegate the decision
│     └── Mapping errors: HALO delegation · COLLAPSING collaborative into automate
│           · MAPPING THE TOOL not the work
│
└── 5. COMMUNICATING TO STAKEHOLDERS
      ├── Value AND limits; overstating loses trust at first visible miss
      ├── "Claude drafts first-pass redline, lawyer reviews" [good] vs "Claude handles contract review" [bad]
      ├── Calibrate to AI literacy: Legal lead (detail + failure modes) ·
      │     Executive (outcome + oversight) · Risk function (assurance)
      ├── Document human oversight: explicit gates RAISE trust
      └── Red-flag phrases: "fully automated" · "Claude handles X" ·
            "basically as good as a person"  → fix: what tool does + human checkpoint
```

---

## 1. Analyzing Requirements and Use Cases with Claude

Most real work starts from **messy inputs**: a long document, a thread of half-formed emails, a verbal ask. Requirements must be **extracted, structured, and pressure-tested** before you build.

### 1.1 What Claude Does Here
- Turns **raw inputs into testable requirements** others can act on.
- Takes unstructured material and returns **structure**:
  - **pulls** requirements out of a document,
  - **organizes** them,
  - **flags** what is **ambiguous or missing**.
- Rule: upload raw inputs and ask for a **structured analysis, not a narrative summary**.

### 1.2 Translating Business Needs into Task Definitions
- "We need better reporting" is **not actionable**.
- Claude helps convert it into **specific task definitions**:
  - **what** report, **for whom**, **how often**, **from what data**, **in what format**.
- Each becomes a requirement you can **build against and check completion on**.

### 1.3 Worked Example: RFP Response Workflow
- **Inputs:** a **40-page RFP** + a **scattered internal email thread**.
- **Recurring task:** turn them into a **structured list of answerable requirements**.
- **Prompt asks for, per requirement:** a **short label**, the **exact RFP section**, **whether the thread already has an answer**, and any **ambiguity needing clarification**, returned **as a table**.
- **Output:** a requirements table the whole team works from; each row **traced to its RFP section**, marked **answered or open**, ambiguities flagged for a **clarifying question to the client**.

**Why this is a Project, not a one-off Chat**

| Element | Where it lives |
| :-- | :-- |
| Past winning proposals | Project **knowledge base** |
| Extraction format | Project **standing instructions** |
| Formatting steps | **Skills** (live at the **account level** and apply **everywhere**, this Project included) |

- **No technical build required.**

### 1.4 Pressure-Testing the Requirements
- **Extraction is the first pass; pressure-testing makes it trustworthy.**
- Ask Claude to **challenge its own list**: "Which are ambiguous as written? Which could be interpreted two ways by our proposal team? Which imply a requirement the RFP states only indirectly?"
- Surfaces **hidden requirements**: buried in a **subordinate clause** or **implied by an evaluation criterion**. Missing these **costs teams the bid**.
- **Structured list + pressure-test pass is far stronger than either alone.**
- This is the **Discernment** habit (Lesson 03) applied at the **requirements stage**.

---

## 2. Research, Planning & Process Optimization

Planning mixes two things Claude handles differently: **synthesis** (it **excels**) and **calculation** (must be **verified**). The strongest planning workflows **pair Claude's synthesis with code-executed analysis**, so the plan rests on numbers that were **computed, not generated**.

### 2.1 Research and Synthesis
- Claude synthesizes across sources to build a plan: **gather considerations, structure options, lay out trade-offs**.
- Current info after the training cutoff: **web search in chat** for quick lookups; **Research** for deeper up-to-date inputs.
- Synthesis is useful **and is where unverified claims can enter**, so Lesson 03 verification applies **throughout**.

### 2.2 Code Execution for Verified Analysis
- When a plan depends on numbers, **have Claude compute them**.
- Upload the dataset; use code execution to **run calculations, produce trend charts, process files**.
- "A staffing plan built on a **guessed utilization rate is a guess**; one built on a **code-executed analysis of actual timesheet data is a plan**."

### 2.3 Worked Example: Capacity Plan
- Operations lead planning **next quarter's headcount**.
- Workflow:
  1. Upload **last four quarters** of ticket-volume data.
  2. **Code execution** computes **quarterly volume growth** and **average tickets resolved per analyst**.
  3. Claude **synthesizes a staffing recommendation** from the verified figures to hold current resolution time, and **shows the assumptions**.
- **The recommendation is only as trustworthy as the figures under it.** Code-executed figures mean the plan can be **defended line by line**.
- **Identifying which steps of a plan are built on a number** is how you decide where AI insight impacts the answer.

### 2.4 Where AI Insight Changes the Plan

| Step type | Who | Why |
| :-- | :-- | :-- |
| **Synthesis steps** (many considerations to weigh and structure) | **Claude adds the most** | Turning data into a structured, defensible recommendation |
| **Judgment steps** (risk appetite, political reality) | **Stay human** | Need context and authority Claude doesn't have |

- A **quick scan for synthesis-heavy steps** tells you where to apply Claude and where to leave the call to a person.
- Capacity plan: Claude's leverage = four quarters of data → defensible recommendation. **The decision to hire** (against **budget and hiring-freeze realities Claude cannot see**) **stays with the operations lead**.

---

## 3. Solution Design, Development & Iteration

**Claude is a design collaborator, not a vending machine.** Value shows up in an **explicit loop**.

### 3.1 The Iteration Loop

**Ideate → Prototype → Gather feedback → Refine** (repeat until the solution holds)

| Stage | Purpose |
| :-- | :-- |
| Ideate | Produces **options** |
| Prototype | Makes one **concrete** |
| Gather feedback | **Exposes what is wrong** |
| Refine | **Fixes it** |

- Run the loop **inside a Project** so **context, constraints, and prior decisions stay stable**; each iteration **builds on the last instead of restarting**.
- Result: **a solution, not a pile of one-off drafts**.

### 3.2 Worked Example: Internal Process Tool (three iterations, no code written)
A business analytics team needed a small internal tool to **track and visualize** a set of metrics. Instead of commissioning a build, they had Claude produce it as a **web artifact** and **iterated by asking**.

| Cycle | Request |
| :-- | :-- |
| **1 · Build** | "Build a simple dashboard artifact that shows these five metrics from the attached data, with a chart for each." → working artifact |
| **2 · Filter & totals** | "Add a filter by region and a summary row at the top with the totals." → refine by **describing the change, not coding it** |
| **3 · Color & print** | "Month-over-month deltas color-coded, green for improvement; layout should print cleanly." |

Three cycles, **no code written by the team**.

### 3.3 Knowing When to Escalate
- The artifact worked because it served **a small team's internal need**.
- When a solution becomes **a system others depend on**, with **uptime, security, or integration requirements**, it has **outgrown Associate scope** → **Developer or Architect** expertise.
- **Escalation signal = dependency**: the moment people **rely on it as infrastructure**, it's no longer a prompt-and-iterate exercise.

---

## 4. Delegation Mapping: Redesigning Workflows with Claude Inside

**The core skill of this module.** Before redesigning a workflow around Claude, **map it step by step** and decide who owns each step: **AI, a human, or both**. Getting it right decides whether the workflow **compounds value or quietly accumulates risk**.

### 4.1 Three Classifications, Three Criteria

**Classify each step as:** **AI-appropriate** · **Human-retained** · **Collaborative**

| Criterion | Question | Rule |
| :-- | :-- | :-- |
| **Reversibility** | Can it be undone if Claude gets it wrong? | Reversible → more delegation; **irreversible → human involvement** |
| **Stakes** | Cost of an error at this step? | High-cost steps stay **human-owned or human-reviewed** |
| **Accountability** | Who is answerable for the outcome? | **Accountability does not delegate, even when the drafting does** |

### 4.2 Building the Redesign
- Embed the right feature at each AI step:
  - **Skill** → **repeatable procedure** steps
  - **Code execution** → **data** steps
- **Consistency from a configured Skill beats "heroic prompting"** that relies on remembering the right wording every time.
- **Human-retained steps become explicit review gates, not afterthoughts.**

### 4.3 Worked Map 1: Contract Review (a common first-win workflow)

| Step | Delegation | Why |
| :-- | :-- | :-- |
| Extract clauses | **AI-appropriate** | Reversible, low stakes, mechanical |
| Flag departures from the company playbook | **AI-appropriate** | Reversible; **a Skill carries the playbook rules** |
| Draft the redline and rationale | **Collaborative** | AI drafts, **human judges each edit** |
| Approve or reject each change | **Human-retained** | High stakes; accountability doesn't delegate |
| Compute financial exposure of a penalty clause | **AI-appropriate (code execution)** | Numeric; **computed, not estimated** |
| Sign and send | **Human-retained** | **Irreversible, external, legally binding** |

### 4.4 Worked Map 2: Onboarding Documents

| Step | Delegation | Why |
| :-- | :-- | :-- |
| Pull new-hire details from the HRIS export | **AI-appropriate (code execution)** | Mechanical, reversible, **must be exact** |
| Draft the offer letter from the approved template | **AI-appropriate** | Reversible draft; **a Skill carries the template** |
| Personalize the welcome note | **Collaborative** | AI drafts; **hiring manager adds the human voice** |
| Confirm compensation figures match the approved req | **Human-retained** | High stakes; accountability doesn't delegate |
| Send the signed offer | **Human-retained** | Irreversible, legally binding |

- The AI does **real work** (including the **redline draft**), not just a summary.
- **The human owns the decisions and the irreversible steps. That split is the redesign.**

### 4.5 Recognizing Over-Delegation
- **Over-delegation** = giving AI **more than the risk profile justifies** (e.g., letting Claude **approve clauses** or **send the contract** because it drafted them well).
- **Drafting quality is not a licence to delegate the decision.**
- If the map gives an **irreversible or high-accountability** step to AI → over-delegation (Team 2's mistake).

### 4.6 Common Mapping Errors (memorise all three)

| Error | What happens | Fix |
| :-- | :-- | :-- |
| **Halo delegation** | A step goes to AI **because the previous step went well** | **Judge each step on its own** |
| **Collapsing collaborative into automate** | "AI drafts, human reviews" quietly becomes "AI drafts" because the **review gate is never staffed** | **A collaborative step with no real reviewer is an automated step**; staff the gate |
| **Mapping the tool, not the work** | Team maps around **features they like** (e.g., a Skill they built) | **Map the work first, then adjust the features** |

---

## 5. Communicating Value and Limitations to Stakeholders

Integrating Claude means describing it to people **who didn't build it**: a **manager, a client, a risk function**. **Credibility comes from accurate claims**: communicate **limits as clearly as value**. **Overstating capability loses trust on the first visible miss.**

### 5.1 Describe Capability Accurately
- State what Claude **can reliably do** for this use case and what it **cannot**, **without inflation or false modesty**.
- [good] "Claude drafts the first pass redline, which a lawyer reviews." (accurate, credible)
- [bad] "Claude handles contract review." (overstates; invites the question your first error will answer badly)

### 5.2 Same Workflow, Three Audiences (contract review)

| Audience | Focus | Message |
| :-- | :-- | :-- |
| **Legal lead** | **High literacy**: features + **failure modes** | "Claude extracts clauses, flags playbook departures, drafts the redline. It does **not approve** changes; that gate stays with you. **Known failure mode:** it can **miss obligations implied indirectly**, so flags are **a prompt for your read, not a substitute**." |
| **Practice executive** | **Outcome focused** | "Review time is **down about half** at the **same approval standard**. Every change is still approved by a lawyer before it leaves the building." |
| **Client risk function** | **Assurance focused** | "AI assists drafting; a **qualified human reviews and approves every term**. **No contract is sent without human sign-off.**" |

**Same workflow, same human gate.** What changes is **the detail each audience needs to trust it**.

### 5.3 Calibrate to the Audience
- Match the message to the audience's **AI literacy**.
  - **Technical stakeholder:** feature detail and **failure modes**.
  - **Executive:** **outcome, oversight in place, risk posture**.
- The expectation you set should **match the capability boundary**, so **no one is surprised later**.
- This is the **Description** competency (Lesson 02) **applied outward**: precise specification of what the tool can and can't do, aimed at **stakeholders instead of Claude**.

### 5.4 Document the Human Oversight
- **Name the review gates** that stay in place: "Every output destined for a client passes human review."
- That control **makes the workflow defensible**.
- Stakeholders trust an AI workflow **more, not less**, when human checkpoints are **explicit**.

### 5.5 Good vs Bad Messaging

| Overstated [bad] | Accurate [good] |
| :-- | :-- |
| "Our new AI system reviews contracts automatically." Sets an expectation the workflow doesn't meet and **hides the human gate**. | "Claude drafts the redline and flags playbook departures; our legal lead reviews and approves every change before anything is sent. Review time is down about half, with the same approval standard." **Value and limits in one breath.** |

### 5.6 Phrases That Quietly Overstate

| Phrase | Problem |
| :-- | :-- |
| **"Fully automated"** | Almost never true; **first visible error exposes it** |
| **"Claude handles X"** | **Collapses the human gate** out of the sentence |
| **"It's basically as good as a person at Y"** | Sets a standard the tool will **eventually miss publicly** |

**Fix every time:** **state what the tool does, then identify the human checkpoint.**

---

## Exam Traps

1. **"Claude drafted it well, so let it approve / send it."** Over-delegation. Drafting quality never licenses delegating the decision or an irreversible step.
2. **"The last step went well, so automate the next one too."** Halo delegation. Each step is judged on its own reversibility, stakes and accountability.
3. **"AI drafts, human reviews" with nobody actually reviewing.** That's automation in disguise. A collaborative step needs a staffed review gate.
4. **"We built a great Skill, so design the workflow around it."** Mapping the tool, not the work. Map the work first.
5. **"Accountability moves to whoever (or whatever) drafted it."** Accountability does not delegate, even when drafting does.
6. **Asking for a narrative summary of requirements.** Ask for a **structured analysis** (table, section references, answered/open, ambiguities).
7. **Stopping at extraction.** The stronger answer adds a **pressure-test pass** for ambiguous and implied requirements.
8. **Letting Claude estimate the numbers a plan depends on.** Use **code execution**; a guessed rate is a guess.
9. **Handing the final hire/budget decision to Claude.** Synthesis is Claude's strength; **judgment steps** (risk appetite, politics, budget, hiring freeze) stay human.
10. **Keeping a widely-used artifact in prompt-and-iterate mode.** Once others depend on it (uptime, security, integration), **escalate to Developer/Architect**.
11. **Running design iterations as separate one-off chats.** Use a **Project** so context and prior decisions stay stable.
12. **"Fully automated" / "Claude handles X" / "as good as a person".** All overstate. Pair the capability with the human checkpoint.
13. **Hiding the human gate to sound impressive.** Explicit oversight **increases** stakeholder trust.
14. **One message for all audiences.** Same facts and same gate; detail calibrated to AI literacy (legal lead vs executive vs risk function).
15. **Skills belong to one Project.** Skills live at the **account level** and apply everywhere; standing instructions and knowledge base live in the Project.
16. **Mixing up the two criteria sets.** Delegation mapping (this lesson) uses **Reversibility, Stakes, Accountability**. Human-review thresholds for outputs (Lesson 03) use **Stakes, Reversibility, Audience, Regulatory exposure**. Read the question to see which one it is asking about.
17. **Treating synthesis as automatically safe.** Synthesis is where Claude adds most value **and** where unverified claims can enter; Lesson 03 verification still applies.

---

## Most Likely Questions

**Q1.** [Easy] Which AI Fluency Framework competency anchors workflow integration?
- A. Description
- B. Discernment
- C. Delegation
- D. Diligence

**Answer: C**
**Why:** Delegation means deciding for each step whether work is AI-appropriate, human-retained or collaborative. Description is about prompting (and here, about stakeholder messaging applied outward). Discernment and Diligence are about evaluating output.

---

**Q2.** [Medium] Two teams used Claude for contract review. Team 2 let Claude approve low-risk clauses unsupervised and later missed a harmful obligation. What was the root cause?
- A. They used the wrong model.
- B. They delegated the wrong steps: a decision step went to AI.
- C. They didn't use Artifacts.
- D. They used Projects instead of Chat.

**Answer: B**
**Why:** Same product, same process. The difference was which steps were delegated. Approval is high-stakes and accountability can't be delegated; that is over-delegation.

---

**Q3.** [Easy] A manager says, "We need better reporting." What is the best way to use Claude first?
- A. Ask Claude to build a dashboard immediately.
- B. Have Claude convert the need into specific task definitions: what report, for whom, how often, from what data, in what format.
- C. Ask Claude for a narrative essay on reporting best practice.
- D. Escalate to a Developer.

**Answer: B**
**Why:** A vague business need isn't actionable. Turning it into task definitions creates requirements you can build against and check completion on.

---

**Q4.** [Medium] A bank's proposal team has a 40-page RFP and a messy email thread. Which request gets the most useful output?
- A. "Summarize the RFP in a few paragraphs."
- B. "Extract every distinct requirement; for each give a label, the exact RFP section, whether our thread has an answer, and any ambiguity. Return as a table."
- C. "Write our RFP response."
- D. "Tell me if we should bid."

**Answer: B**
**Why:** Ask for structured analysis, not a narrative summary. The table traces each requirement to its source, shows answered/open status and flags ambiguities for clarification.

---

**Q5.** [Medium] After extracting RFP requirements, what step makes the list trustworthy?
- A. Reformat it as bullets.
- B. Ask Claude to pressure-test its own list for ambiguous, double-meaning and indirectly implied requirements.
- C. Send it straight to the client.
- D. Switch to Haiku.

**Answer: B**
**Why:** Extraction is the first pass; pressure-testing surfaces hidden requirements buried in subordinate clauses or implied by evaluation criteria. The combination is stronger than either alone.

---

**Q6.** [Hard] The RFP workflow runs as a Project. Where does each element live? (Select 3)
- A. Past winning proposals: Project knowledge base
- B. Extraction format: Project standing instructions
- C. Formatting steps: Skills, which live at the account level and apply everywhere
- D. Skills: only inside this one Project

**Answer: A, B, C**
**Why:** Knowledge base and standing instructions are Project configuration. Skills live at the account level and apply everywhere, including this Project, so D is wrong.

---

**Q7.** [Medium] An operations lead wants a headcount plan. Which workflow is best?
- A. Ask Claude to estimate a utilization rate and recommend headcount.
- B. Use code execution on four quarters of ticket data to compute growth and per-analyst throughput, then have Claude synthesize a recommendation and show assumptions.
- C. Use Research to find industry averages and hire accordingly.
- D. Let Claude make the hiring decision.

**Answer: B**
**Why:** Pair Claude's synthesis with code-executed analysis so the plan rests on computed numbers and can be defended line by line. A is a guess. D hands a judgment step to AI.

---

**Q8.** [Medium] In a planning workflow, which steps should stay human? (Select 2)
- A. Weighing the organization's risk appetite
- B. Decisions shaped by budget limits and a hiring freeze Claude can't see
- C. Structuring many considerations into options and trade-offs
- D. Computing quarterly volume growth

**Answer: A, B**
**Why:** Judgment steps (risk appetite, political reality, constraints Claude can't see) stay human. Synthesis (C) is where Claude adds the most. Computation (D) goes to code execution.

---

**Q9.** [Easy] What is the correct order of the design iteration loop?
- A. Prototype → Ideate → Refine → Gather feedback
- B. Ideate → Prototype → Gather feedback → Refine
- C. Gather feedback → Ideate → Prototype → Refine
- D. Refine → Prototype → Ideate → Gather feedback

**Answer: B**
**Why:** Ideation gives options, a prototype makes one concrete, feedback exposes what's wrong, refinement fixes it, and the loop repeats.

---

**Q10.** [Medium] Why run design iterations inside a Project?
- A. Projects make Claude write code faster.
- B. Context, constraints and prior decisions stay stable, so each iteration builds on the last instead of restarting.
- C. Projects remove the need for feedback.
- D. Projects automatically escalate to Developers.

**Answer: B**
**Why:** Stable context turns iterations into a solution rather than a pile of one-off drafts.

---

**Q11.** [Hard] A team's dashboard artifact, built in three prompt cycles, is now used daily by 400 staff, and IT asks for single sign-on and a live database link. What should the associate do?
- A. Keep iterating with prompts to add SSO.
- B. Escalate to Developer or Architect expertise, since people now rely on it as infrastructure with security and integration requirements.
- C. Rebuild it as a new artifact.
- D. Switch to Opus and continue.

**Answer: B**
**Why:** Dependency is the escalation signal. Uptime, security and integration needs put it beyond Associate scope.

---

**Q12.** [Easy] Which three criteria decide whether a workflow step is AI-appropriate, human-retained or collaborative?
- A. Speed, cost, quality
- B. Reversibility, stakes, accountability
- C. Role, context, task
- D. Audience, tone, format

**Answer: B**
**Why:** These are the delegation-mapping criteria. A is model selection. C is prompt components. D is editing.

---

**Q13.** [Medium] In the contract-review map, which steps are human-retained? (Select 2)
- A. Extract clauses
- B. Approve or reject each change
- C. Compute financial exposure of a penalty clause
- D. Sign and send

**Answer: B, D**
**Why:** Approval is high stakes and accountability doesn't delegate. Sign-and-send is irreversible, external and legally binding. Extraction is AI-appropriate; exposure calculation is AI-appropriate via code execution.

---

**Q14.** [Medium] In the onboarding map, "Personalize the welcome note" is classified as:
- A. AI-appropriate
- B. Human-retained
- C. Collaborative
- D. Code execution

**Answer: C**
**Why:** AI drafts and the hiring manager adds the human voice. Pulling HRIS details is AI-appropriate via code execution. Confirming compensation and sending the offer are human-retained.

---

**Q15.** [Medium] Which features should be embedded at AI steps in a redesigned workflow? (Select 2)
- A. A Skill for repeatable procedure steps
- B. Code execution for data steps
- C. Incognito mode for every step
- D. Research mode for clause extraction

**Answer: A, B**
**Why:** Skills give consistent procedures (better than "heroic prompting"), and code execution handles data steps. C and D don't fit.

---

**Q16.** [Hard] Claude extracted clauses and flagged playbook departures perfectly for months, so the team now lets it approve the changes too. Which mapping error(s) apply? (Select 2)
- A. Halo delegation
- B. Over-delegation
- C. Mapping the tool, not the work
- D. Collapsing collaborative into automate

**Answer: A, B**
**Why:** A step was handed over because earlier steps went well (halo), and an approval step with high accountability went to AI (over-delegation). C and D describe different errors.

---

**Q17.** [Hard] A workflow document says "AI drafts the credit memo, analyst reviews", but analysts have stopped reviewing because of workload. What has happened?
- A. Nothing; the design is still collaborative.
- B. The collaborative step has collapsed into automation; a step with no real reviewer is an automated step.
- C. Halo delegation.
- D. The Skill has failed.

**Answer: B**
**Why:** "AI drafts, human reviews" quietly becomes "AI drafts" when the review gate isn't staffed. The paper design no longer matches reality.

---

**Q18.** [Medium] A team built a strong Skill and redesigned their whole workflow around what it can do. What is the error and fix?
- A. Halo delegation; judge each step on its own.
- B. Mapping the tool, not the work; map the work first, then adjust features.
- C. Over-delegation; remove the Skill.
- D. No error; Skills should drive design.

**Answer: B**
**Why:** Mapping around a favoured feature rather than the actual workflow steps is the error. Map the work, then fit features to it.

---

**Q19.** [Medium] Which statement to a client risk function is most appropriate?
- A. "Our AI reviews contracts automatically."
- B. "AI assists drafting; a qualified human reviews and approves every term. No contract is sent without human sign-off."
- C. "Claude handles contract review end to end."
- D. "It's basically as good as a lawyer."

**Answer: B**
**Why:** The risk function is assurance-focused, so it needs the human gate stated clearly. A, C and D all overstate and hide the human checkpoint.

---

**Q20.** [Hard] Which messages fit the right audience? (Select 2)
- A. To a legal lead: "It can miss obligations implied indirectly, so flags are a prompt for your read, not a substitute."
- B. To a practice executive: "Review time is down about half at the same approval standard, and every change is still lawyer-approved."
- C. To a practice executive: a detailed list of every failure mode and feature setting.
- D. To a client risk function: "Fully automated, no human needed."

**Answer: A, B**
**Why:** High-literacy legal leads want features and failure modes. Executives want outcome, oversight and risk posture. C gives an executive the wrong level of detail. D overstates and removes the gate assurance-focused readers need.

---

## Key Takeaways

1. **Shift from "I use Claude" to "our workflow uses Claude" deliberately.** Value compounds only when you choose the right steps to delegate.
2. **Delegation is the anchor competency.** Classify every step as AI-appropriate, human-retained or collaborative, using **reversibility, stakes and accountability**. Accountability never delegates.
3. **Requirements:** turn messy inputs into a **structured, testable** table (not a narrative), then **pressure-test** it for ambiguous and implied requirements. Run recurring work in a **Project** (knowledge base + standing instructions; Skills are account-level).
4. **Planning:** Claude excels at **synthesis**; numbers come from **code execution**. Judgment steps (risk appetite, politics, budget, hiring freeze) stay human.
5. **Design:** use the **Ideate → Prototype → Gather feedback → Refine** loop inside a Project. Escalate to **Developer/Architect** once others depend on the solution (uptime, security, integration).
6. **Redesign:** Skills for procedures, code execution for data, human steps as explicit review gates. Avoid **over-delegation, halo delegation, collapsing collaborative into automate, and mapping the tool instead of the work**.
7. **Stakeholders:** state value **and** limits, calibrate detail to AI literacy, and **name the human checkpoints**. Avoid "fully automated", "Claude handles X" and "as good as a person".
