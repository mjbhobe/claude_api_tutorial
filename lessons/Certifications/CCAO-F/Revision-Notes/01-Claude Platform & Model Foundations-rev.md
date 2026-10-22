# 01 · Claude Platform & Model Foundations (Revision Notes)

## Exam at a Glance

| Item | Detail |
| :-- | :-- |
| Exam / code | Claude Certified Associate – Foundations · CCAO-F |
| Questions | 60 (multiple-choice and multiple-response; each item says how many to pick) |
| Time | 120 minutes (about 2 minutes per question) |
| Pass mark | Scaled score 720 on a 100–1,000 scale |
| Scoring type | Criterion-referenced: measured against a fixed standard, not against other candidates |
| Score report | Pass/fail + scaled score + percent-correct per domain (domain % does not decide pass/fail) |
| Validity | 12 months; free, non-proctored renewal assessment if renewed on time |

**Domain weights (where marks come from)**

| # | Domain | Weight | Main lesson |
| :-- | :-- | :-- | :-- |
| 2 | Output Evaluation and Validation | **21%** | 03 |
| 4 | Workflow Integration and Solution Design | 16% | 04 |
| 6 | Governance, Risk, and Responsible Use | 15% | 06 |
| 1 | Prompting and Task Execution | 14% | 02 |
| 3 | **Product and Model Selection** | **12%** | **01 (this lesson)** |
| 5 | Configuration and Knowledge Management | 12% | 05 |
| 7 | Troubleshooting and Optimization | 10% | 07 |

**Domain 3 objectives this lesson covers**
- Select the right product feature (Projects, research mode, chat, artifacts)
- Tell apart the model types (Haiku, Sonnet, Opus)
- Match the model to task needs (cost, speed, quality)
- Understand and manage context limits and memory (when to **restart, summarize, or persist**)

Expect overlap with Domain 2 (review every output) and Domain 5 (Projects, Memory).

---

## Memory Map

```
CLAUDE PLATFORM & MODEL FOUNDATIONS
│
├── 4 DECISIONS BEFORE ANY PROMPT
│     1 Entry point → 2 Capability features → 3 Model → 4 Context management
│     (decides whether work builds on itself or needs constant re-setup)
│
├── 5 GEN-AI BEHAVIOURS (true for every feature)
│     ├── Responses vary (probabilistic, not deterministic) → build in review
│     ├── Confident tone ≠ accuracy → fabricated stats sound just as sure
│     ├── Context is a budget → long chats get summarized, early detail fades
│     ├── Knowledge has a training cutoff → use connector / web search / Research
│     └── Configured procedures (Skills) still vary → review stays in
│
├── ENTRY POINTS ("WHERE you work")
│     ├── Chat ......... one-off, quick, exploratory, not reused
│     ├── Projects ..... recurring work, stable context
│     │                   = standing instructions + knowledge base + own chat list
│     │                   (chats inside a Project do NOT share context with each other)
│     ├── Artifacts .... deliverable output, separate editable block
│     └── Research ..... deep multi-source synthesis (paid plans)
│                        quick current lookup → web search toggle in Chat
│
├── CAPABILITY LAYER ("WHAT Claude can do")
│     ├── Projects  → carry CONTEXT
│     ├── Skills    → define PROCEDURES (same steps every time)
│     ├── Code Exec → VERIFY COMPUTATION (must be correct, not plausible)
│     └── Memory    → persist CONTINUITY across sessions
│           ├── Settings → Memory: "Search & reference chats" vs "Generate memory from chats"
│           ├── Project-scoped (automatic, separate per Project)
│           ├── Incognito (ghost icon): out of Memory + history; not org retention
│           └── Curate monthly: review, delete, update; accuracy > volume
│
├── MODELS ("HOW WELL, at what speed/cost")
│     ├── Haiku  → fastest, cheapest; structured, high-volume, low cost of error
│     ├── Sonnet → balanced; DEFAULT start for most knowledge work
│     ├── Opus   → nuanced judgment, multi-step reasoning, ambiguity, high stakes
│     └── (Fable → above Opus; long agentic/coding work; lesson flags as NOT exam-relevant)
│     Rule: Sonnet first → up to Opus if quality short → down to Haiku if volume/speed
│
└── CONTEXT MANAGEMENT ("HOW LONG it works well")
      ├── Warning signs: ignores earlier instructions, only answers latest turn, accuracy drops
      ├── RESTART  → new chat; Project instructions + KB carry over, thread does not
      ├── SUMMARIZE→ ask for state summary (decisions, WIP, open questions), paste into new chat
      ├── PERSIST  → save to Memory or Project knowledge base for all future sessions
      └── Usage limits: short rolling window + weekly limits (separate pool for top tier)
            → segment big tasks, save interim work to KB, restart from summary
```

---

## 1. The Four Up-Front Decisions

Before writing any prompt, decide in this order:

1. **Entry point** (Chat, Project, Artifact, Research)
2. **Capability features** to switch on (Skills, Code Execution, Memory)
3. **Model** (Haiku, Sonnet, Opus)
4. **Context management** across the session

- These choices set the **quality ceiling** for everything that follows.
- They decide whether sessions **build on earlier work** or need **constant re-setup**.
- Learning "one or two things Claude does well" is fine for simple tasks, but not for recurring work, team projects, or deliverables that must survive review.

---

## 2. What to Expect from Generative AI (5 Behaviours)

These apply **no matter which feature** you use.

| # | Behaviour | What it means | What you do |
| :-- | :-- | :-- | :-- |
| 1 | **Responses vary** | Same question twice gives two different answers. Output is based on probability, not deterministic. Neither is "the one correct answer". | Plan for variation; build **review** into any workflow needing consistency. |
| 2 | **Confident tone ≠ accuracy** | Claude is equally fluent when right or wrong. A made-up statistic sounds as sure as a real one. | Never treat confidence as proof. Verify. |
| 3 | **Context is a budget** | Each conversation has a working-memory limit. Near the limit, claude.ai **auto-summarizes earlier messages** (paid plans with Code Execution enabled). Summaries compress detail. | Expect early instructions to **lose force** late in a long session. |
| 4 | **Knowledge has a training cutoff** | Anything after the cutoff is outside reliable knowledge: recent events, current regulations, live market data. | Connect a current source, turn on **web search** in Chat, or use **Research**. |
| 5 | **Configured procedures still vary** | A Skill **reduces** variance but does **not eliminate** it. | Keep review in the workflow, however good the Skill. |

**Exam traps**
- "Claude was confident, so it's correct" is always wrong.
- "A Skill guarantees identical output" is always wrong.
- "Claude knows about last month's regulation change" is unreliable without a current source.

---

## 3. Entry Points: Chat, Projects, Artifacts, Research

One interface, four ways of working. The choice decides **efficiency** and whether **today's context carries into tomorrow**.

### 3.1 Chat
- Default, **unstructured** conversation.
- Saved to history (left sidebar) and **can be continued later**.
- **Memory** and **past-chat search** can bring key context into new chats.
- What Chat lacks vs a Project: **deliberate persistence, standing instructions, curated knowledge base**.
- Use for: one-off questions, quick drafts, exploratory prompting, tasks you won't repeat; work that **starts and ends in that session**.
- **Signal you've outgrown Chat**: you keep opening new chats by **pasting the same background paragraph** you pasted last week.

### 3.2 Projects
- **Persistent workspaces.** Hold three things:
  1. **Standing instructions**: what Claude should know and do in every conversation in the Project.
  2. **Knowledge base**: documents, policies, reference files **uploaded once**, used without re-uploading.
  3. **Conversation history**: its **own** chat list, separate from your global history.
- Chats in one Project **share instructions + knowledge base**, but **do NOT share context with each other**.
- Solves the biggest productivity drain: **re-explaining the same background every session**.
- Example: RFP response for "Acme Inc". Client's documents → **knowledge base**; how to respond → **standing instruction**.

### 3.3 Artifacts
- Use when the result is a **deliverable**, not a conversational reply.
- Appears as a **separate, editable block alongside the chat**, not inside the thread.
- Use for: **draft documents, data tables, formatted reports, code**.
- Use **inline responses** for answers you'll act on **within** the conversation.
- Example: a final trip plan (photos, hotels, flights) as a shareable document.

### 3.4 Research
- **Deep, multi-source synthesis**; available on **paid plans**.
- Runs **multi-step searches** across many sources and **synthesizes** them.
- Compare with **web search**:
  - Web search is a **per-chat toggle** in the chat input, available on **all plans**.
  - On **Team and Enterprise**, an **Owner or Primary Owner** must first enable web search for the workspace in **organization capability settings**; only then can members switch it on.
  - Official docs do not say whether the toggle is on or off by default.
- Rule: **quick current-info lookup → web search in Chat**; **deep investigation / synthesis of current info → Research**.

### 3.5 Selection Logic (memorise)

| Task type | Entry point |
| :-- | :-- |
| One-off question or quick task, no reuse | **Chat** |
| Recurring work, stable context (e.g. RFP responses using client docs) | **Project** |
| Output is a deliverable someone will open and read (e.g. weekly status report) | **Artifact** |
| Deep multi-source investigation or synthesis | **Research** |
| Quick current-information lookup | **Web search in Chat** |

---

## 4. Capability Layer: Skills, Code Execution, Memory

> Entry points decide **where** you work. The capability layer decides **what** Claude can do there.

Three features extend plain text generation: **Skills** (consistent procedures), **Code Execution** (verified computation), **Memory** (continuity across sessions).

### 4.1 The Four-Layer Model

| Layer | Job | Key phrase |
| :-- | :-- | :-- |
| **Projects** | Carry **context** | Background knowledge + standing instructions for the workstream |
| **Skills** | Define **procedures** | Step-by-step "how to do this task", consistently every time |
| **Code Execution** | **Verify computations** | When the result **must be correct, not merely plausible** |
| **Memory** | Persist **continuity** | Relevant facts carry forward without re-entry |

- Use layers **alone or combined**, based on the task.

### 4.2 Memory
- Keeps **work-relevant facts across sessions** so you don't re-enter them.
- Good things to store: **recurring role context, output-format preferences, names of frequent collaborators, standing constraints** across projects.

**Memory settings (Chat): Settings → Memory**

| Toggle | What it does | What it does NOT do |
| :-- | :-- | :-- |
| **Search and reference chats** | Looks through past chats when you refer to earlier work ("the exam prep plan we discussed"); retrieves content from specific old chats **on request** | Does **not** build a profile of you |
| **Generate memory from chats** | The **actual Memory feature**: distils details (role, preferences) from chats and stores them for future chats | n/a |

**Project-scoped Memory**
- Memory is kept **separate per Project**: client A context never appears in client B sessions.
- **No separate setting**; it's on by default and distinct for each Project.
- Practice: **separate Projects for separate workstreams**; Memory follows the same boundaries.

**Incognito mode**
- Ghost icon, top right of the chat window.
- Keeps a session **out of Memory and chat history**.
- Applies to **standalone chats, outside Projects**.
- Use for **sensitive conversations** or exploratory work with **confidential inputs**.
- Does **NOT override your organization's data retention**.

**Memory import from other AI platforms**
- **Experimental** (as of June 2026).
- Documented for **Free, Pro, Max, Team** plans (**not Enterprise**).
- If auto-import isn't available: **add key facts to Memory manually** in memory settings, **not** into a Project knowledge base.

### 4.3 Memory Curation
- Stale memory can be **actively misleading** (accurate last quarter, wrong now).
- Review stored memories **at least once a month** (active users).
- **Delete or update** entries that no longer hold.
- Keep only information that **genuinely recurs** across sessions.
- Treat Memory like a **working file**. **Accuracy matters more than volume.**

### 4.4 Scenario: Monthly Regulatory Tracking Report

**Before (months 1–2, in Chat):** each session she uploaded regulatory docs, re-pasted portfolio context, re-typed format instructions, and verified every number. Caught 2 errors in month 1 and 1 in month 2, all before release.

**After (month 3, capability layer):**
- Portfolio context + standing format instructions → **Project**
- Prior reports → **knowledge base**
- Report output format → **Skill**
- Numeric calculations → **Code Execution**
- Verification step → **still ran**

**Result:** time per session **65 → 30 minutes**; **no errors** in months 3–8.

**The four questions she asked (map question to layer)**

| Question | Layer |
| :-- | :-- |
| Which parts are the same every time? | **Standing instructions + Skill** |
| Which reference material recurs across sessions? | **Knowledge base** |
| Which outputs must be computed correctly, not just "sound right"? | **Code Execution** |
| Which context should carry across sessions without re-entry? | **Memory** |

Lesson: automation **cut time**, but **verification was kept**.

---

## 5. Choosing Models: Haiku, Sonnet, Opus

> The capability layer decides **what** Claude does. The model decides **how well**, and at what cost in **speed**.

Goal: avoid **over-engineering routine work** and **under-resourcing high-stakes analysis**.

| Model | Profile | Use for |
| :-- | :-- | :-- |
| **Haiku** | **Fastest, most efficient** (token use). Good with structured tasks. | **Classification, extraction, formatting, straightforward summarization, high-volume routine work** where speed matters and **cost of an imperfect output is low**. Speed advantage **compounds** across hundreds of items. |
| **Sonnet** | **Balanced** tier; strong quality across task types. | **Drafting, synthesis, analysis, research assistance, document review.** **Right starting point for most knowledge work.** |
| **Opus** | **Higher capability** than Sonnet and Haiku; slower. | **Nuanced judgment, complex multi-step reasoning, ambiguous inputs, quality over speed.** Client-facing deliverables, complex document analysis, strategic planning, high-stakes multi-source synthesis. |

**Movement rules**
- Start with **Sonnet**.
- Quality falling short on a complex task → **upgrade to Opus**.
- Speed/volume is the main need and task is structured → **consider Haiku**.

**Decision logic (memorise)**

| Task profile | Model |
| :-- | :-- |
| Routine, structured extraction/classification at volume | **Haiku** |
| Most professional drafting, synthesis, analysis | **Sonnet** |
| Complex judgment, high-stakes output, ambiguous or multi-layered inputs | **Opus** |

**Usage and cost**
- Opus = better on complex tasks, **slower**. Reserve it for work where the **quality ceiling genuinely matters**.
- On **metered / usage-budgeted plans (including API)**, speed vs capability is also a **per-call cost** trade-off: Opus uses **more usage per call** than Haiku or Sonnet. Efficiency = cost + speed.
- On the **standard claude.ai subscription**, treat **efficiency (speed + usage headroom)** as the practical proxy for cost. Selection logic **does not change**.
- Model picker lineup, default model, and automatic model-switching **vary by plan and change over time**. Decision logic applies whatever tiers you have.

**About Fable (know it exists, don't over-study)**
- Introduced June 2026, **above Opus** (Mythos-class), priced **above Opus**.
- For **long-horizon** work over hours and many dependent steps: large-scale coding/refactoring, autonomous agentic workflows, multimodal research. Safeguards on biology, cybersecurity, AI research topics may limit some requests.
- "If Opus already meets your quality bar, stay with Opus."
- The lesson states the certification **pins the three-tier Haiku/Sonnet/Opus frame** and marks the fourth tier as **not exam-relevant**. Answer exam questions using **Haiku/Sonnet/Opus**.

---

## 6. Context Management

> Model and capabilities decide **what** Claude can do. Context management decides **how long** it can do it well.

### 6.1 The Context Window in Practice
- Every conversation has a **finite working-memory budget** that runs down as it grows (messages + uploaded documents).
- Near the limit, claude.ai **auto-summarizes earlier messages** (**only on paid plans with Code Execution enabled**); full history stays available for reference.
- Effect: detailed instructions given in minute 10 may **not be followed at minute 90**. Not because Claude ignores them, but because **detail compresses in the summary**.

### 6.2 Warning Signs a Conversation Needs Intervention
1. Claude **stops following instructions** it followed earlier in the same session.
2. Responses address **only the latest exchange**, ignoring earlier decisions.
3. **Accuracy drops** in ways consistent with missing early context.

### 6.3 Three Responses When Context Degrades (Restart · Summarize · Persist)

| Response | How | When |
| :-- | :-- | :-- |
| **Restart** | Start a **new conversation**. **Project instructions + knowledge base carry forward automatically**; the **conversation thread does not**. | Session has **drifted beyond recovery**, or you're starting a **genuinely new task** in the same workstream. |
| **Summarize** | Before restarting, ask Claude for a **summary of current state: decisions made, work in progress, open questions**. Paste it at the start of the new chat. | You need **thread continuity** without carrying a **degraded context** forward. |
| **Persist** | Save to **Memory** or update the **Project knowledge base**. | Information needed in **all future sessions**. Saving at the right moment beats re-entering repeatedly. |

- A well-kept Project with a **current knowledge base** reduces the impact of any single session's context limit.

### 6.4 Usage Limits
- Work on **more than one time window**:
  - a **short rolling session window**, plus
  - **weekly limits** on paid plans **across models**, with a **separate weekly pool for the highest tier**.
- Exact windows/allowances **vary by plan and change**; check the Help Center.
- Long sessions on **higher-tier models** may hit a limit before work is done.
- **Plan ahead** rather than work around an interruption:
  - **Break large tasks into segments**
  - **Save interim progress to the knowledge base**
  - **Restart from a summary** rather than stretching one session indefinitely

---

## Most Likely Questions

**Q1.** You get two different answers when you ask Claude the same question twice. What is the best explanation?
- A. The first answer was a hallucination.
- B. Claude's outputs are probability-based, so variation is expected.
- C. Your Memory settings changed between the two questions.
- D. The model was switched automatically.

**Answer: B**
**Why:** Responses vary because generation is probabilistic, not deterministic. Neither answer is "the one correct response". A assumes one must be wrong. C and D are possible in theory but are not the general explanation the lesson gives.

---

**Q2.** Which statement about Claude's tone is correct?
- A. A confident answer is more likely to be accurate.
- B. Claude adds hedging words when it is unsure, so hedged answers need checking.
- C. Claude writes with the same fluency whether it is right or wrong.
- D. Fabricated statistics usually read less fluently than verified ones.

**Answer: C**
**Why:** Confident tone is not a signal of accuracy. A fabricated statistic reads with the same assurance as a real one. A and D contradict this. B implies only hedged answers need checking, which is wrong.

---

**Q3.** A marketing lead pastes the same three-paragraph brand background into a new Chat every week before drafting campaign copy. What should they do?
- A. Keep using Chat but switch to Opus.
- B. Move the work into a Project with the background as standing instructions or knowledge.
- C. Use Research mode so Claude can find the brand background online.
- D. Use Incognito mode to avoid cluttering history.

**Answer: B**
**Why:** Re-pasting the same background is the signal a workstream has outgrown Chat. A Project sets context once so every chat starts with it. A changes the model, not the re-setup problem. C is for multi-source investigation. D removes history and Memory, making it worse.

---

**Q4.** Which THREE items does a Claude Project hold? (Select 3)
- A. Standing instructions
- B. Knowledge base
- C. Its own conversation history
- D. A shared context window across all its chats
- E. A dedicated model that can't be changed

**Answer: A, B, C**
**Why:** A Project holds standing instructions, a knowledge base, and its own conversation list. D is a classic trap: chats inside a Project share instructions and knowledge but do NOT share context with each other. E is not described.

---

**Q5.** In a Project, you made key decisions in Chat 1. You open Chat 2 in the same Project. What does Claude have access to in Chat 2?
- A. Everything from Chat 1, because chats in a Project share context.
- B. The Project's standing instructions and knowledge base, but not Chat 1's conversation.
- C. Nothing, since each chat starts blank.
- D. Only Chat 1's conversation, not the knowledge base.

**Answer: B**
**Why:** Project chats share instructions and the knowledge base but not context with each other. To carry Chat 1's decisions, summarize them or persist them to the knowledge base or Memory.

---

**Q6.** You need a formatted weekly status report that your director will open and read. Which entry point fits best?
- A. Chat inline reply
- B. Artifact
- C. Research
- D. Incognito chat

**Answer: B**
**Why:** Artifacts are for deliverables the recipient will open and read. They appear as a separate, editable block. Inline replies (A) are for answers you act on within the chat. C is for investigation. D is a privacy mode, not an output format.

---

**Q7.** An operations analyst needs a quick check of a currency's current exchange rate before a call. Which is the most efficient choice?
- A. Research mode
- B. Web search toggled on in Chat
- C. Upload last year's report to a Project
- D. Ask Claude without any tools, since it knows recent rates

**Answer: B**
**Why:** Quick current-information lookups belong in Chat with web search. Research (A) is for deep multi-source synthesis and is more than needed. C gives stale data. D fails because of the training cutoff.

---

**Q8.** A strategy team needs a synthesized view of competitor moves across dozens of current news sources, filings, and analyst notes. Which entry point should they choose?
- A. Chat without web search
- B. Artifact
- C. Research
- D. Project with last quarter's documents only

**Answer: C**
**Why:** Research runs multi-step searches across many sources and synthesizes current information. A has no current data. B is an output format, not an investigation method. D lacks current information.

---

**Q9.** On a Team plan, a member cannot find the web search toggle in their chats. What is the most likely reason?
- A. Web search only exists in Research mode.
- B. An Owner or Primary Owner has not enabled web search for the workspace.
- C. Web search is available only on Enterprise.
- D. The member must turn on "Generate memory from chats".

**Answer: B**
**Why:** On Team and Enterprise plans, an Owner or Primary Owner must enable web search in organization capability settings before members can switch it on. A is wrong: web search is a per-chat toggle. C is wrong: it's on all plans. D is unrelated.

---

**Q10.** Match the need to the capability. A finance associate needs loan-portfolio totals that must be exactly right, not just plausible. Which capability fits?
- A. Memory
- B. Skills
- C. Code Execution
- D. Standing instructions

**Answer: C**
**Why:** Code Execution verifies computations when the result must be correct, not merely plausible. Memory carries continuity, Skills define procedures, and standing instructions carry context. None of these checks arithmetic.

---

**Q11.** Which pairing of layer and purpose is INCORRECT?
- A. Projects: carry context
- B. Skills: define repeatable procedures
- C. Memory: verify computations
- D. Code Execution: verify computations

**Answer: C**
**Why:** Memory persists continuity across sessions. It does not verify computations; Code Execution does. A, B, D are correct pairings.

---

**Q12.** A team has a well-built Skill that formats their monthly compliance summary. A manager proposes dropping the human review step because "the Skill makes it the same every time". What is the best response?
- A. Agree; Skills produce identical output.
- B. Disagree; Skills reduce variance but don't eliminate it, so review should stay.
- C. Agree, but only if the team uses Opus.
- D. Disagree; Skills only work in Chat, not Projects.

**Answer: B**
**Why:** Configured procedures still produce varied output. Review stays in the workflow however well the Skill is built. A is the trap. C: no model removes variation. D is made up.

---

**Q13.** In Settings → Memory, what does "Search and reference chats" do when ON?
- A. Builds a profile of your role and preferences.
- B. Lets Claude retrieve content from specific past chats when you refer to earlier work.
- C. Shares your chats with your organization's admins.
- D. Keeps chats out of history.

**Answer: B**
**Why:** It retrieves content from old chats on request and does not build a profile. Building a profile (role, preferences) is what "Generate memory from chats" does (A). C and D are not what this setting does; D describes Incognito.

---

**Q14.** A consultant works for two competing banks and worries context from Bank A could appear in Bank B work. What is the best setup?
- A. One Project for both clients with a note to keep them separate.
- B. Separate Projects for each client, since Project memory is scoped per Project.
- C. Turn off all Memory and re-paste context each time.
- D. Use Incognito inside a shared Project.

**Answer: B**
**Why:** Project-scoped Memory keeps contexts separate, and there is no extra setting to turn on. A relies on an instruction instead of a structural boundary. C throws away the productivity gain. D is wrong because Incognito applies to standalone chats outside Projects.

---

**Q15.** Which TWO statements about Incognito mode are true? (Select 2)
- A. It keeps the session out of Memory and chat history.
- B. It overrides your organization's data retention policy.
- C. It applies to standalone chats outside Projects.
- D. It makes sharing regulated personal data acceptable.

**Answer: A, C**
**Why:** Incognito keeps a chat out of Memory and history and applies to standalone chats. It does not override org data retention (B). It doesn't change what data policy allows (D).

---

**Q16.** A user on an Enterprise plan wants to bring facts from another AI assistant's memory into Claude, but automatic import is not available. What is the documented fallback?
- A. Upload the facts to a Project's knowledge base.
- B. Add the key facts to Memory manually through memory settings.
- C. Paste them into every new chat.
- D. Ask the admin to enable Research.

**Answer: B**
**Why:** The documented fallback is adding key facts to Memory manually, not routing them into a Project knowledge base (A). Note that import is documented for Free, Pro, Max, Team, not Enterprise. C is inefficient. D is unrelated.

---

**Q17.** A support team must tag 5,000 incoming customer emails into eight fixed categories each day. A wrong tag is easy to fix later. Which model fits best?
- A. Haiku
- B. Sonnet
- C. Opus
- D. Use the most capable model available for every email

**Answer: A**
**Why:** Haiku suits structured, high-volume classification where speed matters and the cost of an imperfect output is low. Its speed advantage compounds at volume. C and D over-spend on capability and speed. B works but isn't the best fit for routine volume.

---

**Q18.** A project manager is unsure which model to use for drafting a stakeholder update and summarizing meeting notes. What does the lesson recommend?
- A. Start with Haiku and upgrade if needed.
- B. Start with Sonnet; move to Opus only if quality falls short on complex work.
- C. Always use Opus for anything external.
- D. Pick the model with the lowest usage limit.

**Answer: B**
**Why:** Sonnet is the right starting point for most knowledge work (drafting, synthesis, analysis). Upgrade to Opus if quality falls short. A suits structured volume tasks. C wastes capacity on routine work. D makes no sense.

---

**Q19.** Which tasks are typical Opus candidates? (Select 2)
- A. Board-level strategic plan built from several conflicting reports
- B. Reformatting 300 addresses into one standard layout
- C. Analysis of an ambiguous, multi-party contract for a client deliverable
- D. Extracting invoice numbers from a batch of PDFs

**Answer: A, C**
**Why:** Opus fits nuanced judgment, complex multi-step reasoning, ambiguous inputs, and high-stakes client-facing work. B and D are structured, high-volume formatting or extraction: Haiku territory.

---

**Q20.** On a metered or usage-budgeted plan (including API access), what changes about model selection?
- A. Nothing; cost is identical across tiers.
- B. The speed vs capability trade-off also becomes a per-call cost trade-off, since Opus consumes more usage per call.
- C. Only Haiku is allowed.
- D. The decision logic reverses: use Opus for volume work.

**Answer: B**
**Why:** On metered plans, efficiency means cost as well as speed, and Opus uses more per call. The selection logic itself does not change (D is wrong). A and C are false.

---

**Q21.** Ninety minutes into a long session, Claude stops applying a formatting rule you set in the first ten minutes. What is the most likely cause?
- A. Claude is deliberately ignoring the instruction.
- B. Earlier context was summarized as the window filled, so detail was compressed.
- C. The model was downgraded to Haiku.
- D. Memory was turned off.

**Answer: B**
**Why:** As the context window fills, claude.ai summarizes earlier messages (paid plans with Code Execution enabled), and detail compresses. The lesson says plainly this is not Claude ignoring you (A). C and D aren't indicated.

---

**Q22.** A session has drifted badly, but you need the decisions and open questions from it in the next session. What is the best sequence?
- A. Keep going in the same chat and repeat instructions louder.
- B. Ask Claude for a summary of decisions, work in progress, and open questions; start a new chat and paste it in.
- C. Start a new chat with no context.
- D. Switch to Opus in the same chat.

**Answer: B**
**Why:** Summarize then restart keeps thread continuity without dragging a degraded context forward. A keeps the degraded window. C loses continuity. D doesn't fix context degradation.

---

**Q23.** Which actions match "Persist" in context management? (Select 2)
- A. Save a stable fact to Memory
- B. Update the Project knowledge base with the latest policy document
- C. Open a new chat
- D. Ask Claude to summarize the current chat

**Answer: A, B**
**Why:** Persist means saving information needed in all future sessions to Memory or the Project knowledge base. C is Restart. D is Summarize.

---

**Q24.** An analyst running long Opus sessions keeps hitting usage limits mid-task. What is the recommended approach? (Select 3)
- A. Break the large task into segments
- B. Save interim progress to the knowledge base
- C. Restart from a summary rather than extending one session indefinitely
- D. Keep one session running as long as possible to save context

**Answer: A, B, C**
**Why:** For intensive tasks, plan ahead: segment, save interim work, restart from a summary. D is the opposite of the guidance and increases the risk of both limits and context degradation.

---

**Q25.** It's been four months since a user last reviewed their stored Memory. Their role changed last month. What is the main risk, and the fix?
- A. No risk; more memories always help.
- B. Stale entries can actively mislead; review at least monthly and delete or update outdated entries.
- C. Memory auto-expires after 30 days, so nothing is needed.
- D. Move all memories into a Project knowledge base.

**Answer: B**
**Why:** Memory is most useful when curated. Out-of-date entries can mislead, and accuracy matters more than volume. A contradicts this. C is invented. D isn't the recommended fix.

---

## Key Takeaways

1. **Decide before you prompt.** Entry point → capability features → model → context management. These set the quality ceiling.
2. **Five Gen-AI facts never change:** answers vary, confidence ≠ accuracy, context is a budget, knowledge has a cutoff, and even Skills produce varied output. **Review is always part of the workflow.**
3. **Entry points:** Chat = one-off. Project = recurring work with stable context (instructions + knowledge base + own chats; chats don't share context with each other). Artifact = deliverable. Research = deep multi-source synthesis; quick lookups use **web search in Chat**.
4. **Four layers, four jobs:** Projects carry **context**, Skills define **procedures**, Code Execution **verifies computation**, Memory persists **continuity**.
5. **Memory hygiene:** know the two toggles (search past chats vs generate memory), Project memory is automatic and separate per Project, Incognito keeps chats out of Memory and history but doesn't override org retention, and review memory **monthly**.
6. **Models:** Haiku = fast, structured, high volume, low cost of error. **Sonnet = default.** Opus = complex, ambiguous, high stakes. On metered plans, higher tier = higher cost per call.
7. **Context:** watch for drift signs, then **Restart, Summarize, or Persist**. For usage limits, segment work, save interim progress, restart from a summary.
