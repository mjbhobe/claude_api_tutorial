# 05 · Configuration & Knowledge Management (Revision Notes)

## Where This Lesson Sits in the Exam

| Domain | Weight | Objectives covered here |
| :-- | :-- | :-- |
| **5 · Configuration and Knowledge Management** | **12%** | Configure Claude Projects with instructions and knowledge sources · Manage uploaded knowledge and connectors (e.g., Google Drive, Gmail) · Create effective system-level instructions · Inform, maintain, and update configurations, knowledge sources, and instructions |

### Exam Objective → Where It Is Covered

| Domain 5 objective (exam guide) | Sections in these notes |
| :-- | :-- |
| **Configure Projects** with instructions and knowledge sources | 1.1 to 1.6 |
| Manage **uploaded knowledge and connectors** (Google Drive, Gmail) | 2.1 to 2.4 |
| Create effective **system-level instructions** | 3.1 to 3.4 |
| **Maintain and update** configurations, knowledge, instructions | 4.1 to 4.5 |

### Core Ideas
- **Using vs operating Claude.** *Using* = typing a good prompt today. *Operating* = building an environment where the right **context, instructions, and procedures are already in place**, so every chat starts from a **configured baseline, not a blank slate**.
- **Configuration is leverage:** set it up **once**, benefit on **every** conversation after.
- **Turns individual skill into team capability.** With a curated Project, **two people asking the same question get the same quality of answer**. Without it, everyone **re-invents context daily** and answers **drift**.
- **Second half of the discipline = maintenance.** Configurations **age**: last quarter's instruction, superseded documents in the knowledge base, an out-of-date Skill all **quietly degrade output**. Build deliberately; **review on a cadence**.

---

## Memory Map

```
CONFIGURATION & KNOWLEDGE MANAGEMENT
│
├── USING (good prompt today) vs OPERATING (configured baseline every chat)
│     configuration = leverage · individual skill → team capability · must be MAINTAINED
│
├── 1. FOUR CONFIGURATION MECHANISMS ("right slot for each need")
│     ├── Standing instructions → BEHAVIOUR (tone, format defaults, verification habits)
│     ├── Knowledge base ........ FACTS & REFERENCE (docs, policies; no re-upload)
│     ├── Skills ................ PROCEDURES; ACCOUNT-level under CUSTOMIZE; reusable in any Project
│     └── Scoped Memory ......... CONTINUITY; what the Project has SETTLED; isolated per Project
│     Test: "always cite sources" = instruction · "brand hex codes" = knowledge ·
│           "format into report template" = Skill
│     Most common mistake: procedure in instructions / behaviour rule in KB
│     Memory vs KB: stable reference fact → KB · evolving record of decisions → Memory
│     PAIRING RULE: needs often span 2 slots (instruction + KB docs; Skill + brand guide)
│     One Project per client; share on Team/Enterprise under permissions
│
├── 2. CONNECTORS & UPLOADED KNOWLEDGE
│     ├── Connector = reach an external system YOU AUTHORIZE (Drive search, find email)
│     ├── Keep access DELIBERATE, not everything by default
│     ├── Boundaries: mail may SEARCH/READ but NOT SEND → confusing failure, not clear error
│     ├── Pitfall 1: add-connector path → PUBLIC DIRECTORY, not org-vetted → check with admin
│     ├── Pitfall 2: boundary hit looks like a BUG → fix misrouted to wrong team (field-observed)
│     └── Uploaded knowledge: CURRENT · RELEVANT · NO DUPLICATES (3 policy versions → wrong cite)
│
├── 3. SYSTEM-LEVEL INSTRUCTIONS THAT STICK
│     ├── Write guardrails ONCE (cite sources; "I don't know" not guessing) → inherited by all chats
│     ├── Anticipate use cases (format, register up front → first draft near final)
│     ├── PRECISION or it SILENTLY fails ("be professional" [bad] → formal register,
│     │     define acronyms, paragraphs < 4 sentences [good])
│     └── TEST: would two different people read it the same way?
│
└── 4. MAINTAINING CONFIGURATIONS (living assets; stale = quiet degradation, no error)
      ├── Review cadence: MONTHLY for active Projects (instructions current? KB free of
      │     superseded docs? right Skills enabled?) · late signal = quality slips for no visible reason
      ├── Skills versioning: Anthropic-built + org-provisioned = AUTO-update ·
      │     custom-uploaded = change ONLY when you RE-UPLOAD · off-format every run = maintenance problem
      ├── Memory lifecycle: review · edit/delete stale · EXPORT backup before major change ·
      │     FULL RESET when outdated context misleads · accuracy > volume
      ├── Configuration is ADDITIVE: missing fact → add to instructions or Memory explicitly
      └── Audit example: renamed metric in instruction + 2 template versions + departed
            stakeholder in Memory → fix = MAINTENANCE, not a new prompt
```

---

## 1. Configuring Claude Projects

A Project has **several configuration slots**. The skill is **putting each piece of a recurring need into the right slot**. Choosing correctly is what makes a Project run smoothly.

### 1.1 The Four Configuration Mechanisms

| Mechanism | Holds | Rule of thumb | Key facts |
| :-- | :-- | :-- | :-- |
| **Standing instructions** | How Claude should **behave** across all chats in the Project: **tone, format defaults, verification habits** | **Behaviour, not facts** | Inherited by every conversation in the Project |
| **Knowledge base** | **Documents, policies, reference files** Claude draws on **without re-uploading** | **Facts and reference, not behaviour** | Keep current, relevant, de-duplicated |
| **Skills** | **Repeatable procedures** followed consistently for a task type | **Procedure, not one-off instructions** | Live at the **account level under Customize**, **not inside any one Project**; **reusable across any Project** |
| **Scoped Memory** | **Continuity** within the Project | **What the Project has already settled** | **Kept separate from other Projects**, so context doesn't bleed between workstreams |

**One-line summary:** Instructions govern **behaviour**, knowledge base holds **facts**, Skills carry **procedures**, scoped Memory keeps **continuity**.

### 1.2 Choosing the Right Mechanism: "Instruction, knowledge, or Skill?"

| Need | Example | Slot |
| :-- | :-- | :-- |
| Rule about **behaviour** | "Always cite sources" | **Standing instruction** |
| **Fact** Claude needs | "Our brand palette is these hex codes" | **Knowledge base** |
| **Multi-step procedure** | "Format findings into our standard report template" | **Skill** (built once at account level under Customize, reused across Projects) |

- **Most common configuration mistake:** putting a **procedure into the instructions**, or a **behaviour rule into the knowledge base**. It makes the Project **harder to maintain**.

### 1.3 Worked Example: Client Account Workspace (one Project per client)

| Slot | Client A content |
| :-- | :-- |
| **Standing instructions** | "Write in a formal register. Always cite the source document for any factual claim. Flag anything you are unsure of rather than guessing." |
| **Knowledge base** | Client's **brand guide**, current **statement of work**, **last three status reports** |
| **Skill (account-level, reused here)** | Firm's **status-report formatter**; lives under **Customize**, available to any Project, so every weekly update has the same structure |
| **Scoped Memory** | Client's **stakeholder names and standing preferences**, which never appear in other clients' Projects |

- On **Team or Enterprise**, the Project can be **shared with the engagement team under permissions**, so everyone works from the **same configured baseline**.
- **Project-scoped Memory guarantees** Client A's context doesn't appear in a Client B conversation. This separation makes **one-Project-per-client safe**.

### 1.4 Scoped Memory as a First-Class Mechanism
- Easy to treat as an afterthought, but in a Project it is **a configuration slot like any other**.
- How the slots divide the work: instructions say **how Claude should behave**; the knowledge base says **what is true**; Skills carry **reusable procedures** (account level); scoped Memory holds **what the Project has already settled**.
- Holds what the Project has **already settled**: **stakeholder names, standing preferences, decisions from earlier conversations** you don't want to restate.
- **"Scoped" is the key word**: sectioned off from your other Projects, so context **never appears in another** client or workstream.
- That **isolation makes Memory safe** for **sensitive or client-specific continuity**; Claude remembers what it needs **without revealing information to the wrong audience**.

**Memory vs knowledge base: decide by type**

| Type of information | Goes in |
| :-- | :-- |
| **Stable reference fact** | **Knowledge base** |
| **Evolving record of Project decisions** | **Memory** |

### 1.5 The Pairing Rule (when a need spans two mechanisms)
- The cleanest configurations **rarely map a need to a single slot**.
- **Most common pattern: a behaviour rule + the facts it acts on.**
  - "Always cite the source document" = **standing instruction**; the documents it cites = **knowledge base**.
  - **Neither works alone:** the instruction has **nothing to cite** without the documents; the documents get used **inconsistently** without the instruction.
- **Skills pair the same way:** a status-report **Skill** carries the procedure; the **brand guide** it formats against sits in **knowledge**.
- When configuring, ask: **which slot does this need belong in, and does it need two slots wired together?**

### 1.6 Quick Slot-Sorting Practice

| Item | Slot |
| :-- | :-- |
| "Say 'I don't know' rather than guessing" | Standing instruction |
| Current statement of work | Knowledge base |
| Firm's weekly status-report procedure | Skill |
| "The client's CFO prefers figures in a one-page appendix" (settled preference) | Scoped Memory |
| "We agreed last week to drop the Q2 comparison" (evolving decision) | Scoped Memory |
| Approved product price list | Knowledge base |

---

## 2. Connectors and Uploaded Knowledge

Connectors extend Claude's reach into the data you already work in, **like Google Drive and Gmail**. They are **powerful and have boundaries**. Manage them as **curated sources** and know **exactly what each can and cannot do**.

### 2.1 Connecting External Sources
- A connector lets Claude reach an **external system you authorize**, e.g. **search your Drive** for a document or **find a relevant email**.
- **You manage what is accessible.** Keep that set **deliberate**, **not connecting everything by default**.

### 2.2 Capability Boundaries
- Each connector has a **defined boundary**; knowing it **prevents wasted time**.
- Example: a **mail connector may let Claude search and read messages, but not send them**.
- Expecting an action a connector can't perform gives a **confusing failure, not a clear error**.
- **Learn each connector's boundaries before you build a workflow on it.**

### 2.3 Two Field-Observed Pitfalls

| Pitfall | What happens | Fix |
| :-- | :-- | :-- |
| **Wrong path to add a connector** | The obvious add-connector path can route to a **public directory** instead of your **organization's vetted connectors** | **Confirm the right path with your admin**, especially on **Team or Enterprise**, so you connect the **approved source, not a look-alike** |
| **Boundary confusion misroutes fixes** | A connector hitting its boundary can **look like a bug** (reported from **field use, not documented product behaviour**); reports go to the **wrong team** and the fix **stalls** | **Know where each connector's capability ends** so the issue isn't mislabelled |

### 2.4 Keeping Uploaded Knowledge Current
- Uploaded knowledge needs the **same care as a connected source**: **current, relevant, free of duplicates**.
- **Three versions of the same policy invite Claude to cite the wrong one.**
- Curate it **like a shared drive**: **remove deprecated versions as you add new ones**.

---

## 3. System-Level Instructions That Stick

Teams keep asking: *can we bake the guardrails in once instead of re-typing them every conversation?* **Persistent (standing) instructions are exactly that mechanism.** Write **verification behaviours, format defaults, and tone once**; **every conversation in the Project inherits them**.

### 3.1 Write the Guardrails Once
- **Highest-value instructions = the ones you'd otherwise re-type constantly.**
- Example verification instruction: "Cite the source document for every factual claim, and say 'I don't know' rather than guessing when the documents do not cover something."
- That discipline then applies to **every conversation without anyone remembering to ask**.

### 3.2 Anticipate the Use Cases
- Good standing instructions embed **format, tone, and guardrail guidance ahead of need**.
- If the Project produces **client deliverables**, specify **preferred format and register up front**, so the **first draft lands closer to final** instead of needing the **same corrections each time**.

### 3.3 Precision, or It Silently Fails
- **Vague instructions don't announce failure; they just quietly don't work.**
- "Be professional" gives Claude **almost nothing** to act on.
- "Use a formal register, define any acronym on first use, and keep paragraphs under four sentences" is **precise enough to change the output**.
- **Test of an instruction: would two different people read it the same way?**

### 3.4 Before and After

| | Instruction | Result |
| :-- | :-- | :-- |
| **Vague** | "Make the reports good and accurate." | Quality **varies chat to chat**; nothing concrete changed |
| **Precise** | "For every figure in a report, state its source. If a figure is not in the provided data, mark it 'unverified' rather than including it. Lead each report with a one-sentence headline." | Verification behaviour is **consistent**; the headline **appears every time** |

---

## 4. Maintaining Configurations

Configurations are **living assets**. **Instructions, knowledge, Skills, and Memory all drift toward stale**, and stale configuration **degrades output quietly, with no error to alert you**. **Scheduled maintenance** catches decay **before it reaches a deliverable**.

### 4.1 Review Cadence
- Set a **recurring review for each active Project**. Ask:
  1. Do the **standing instructions still match the current process**?
  2. Is the **knowledge base free of superseded documents**?
  3. Are the **right Skills enabled**?
- **A monthly pass for active Projects catches most drift.**
- **Signal you waited too long:** **output quality slipping for no visible reason**.

### 4.2 Skills Versioning

| Skill type | How it updates |
| :-- | :-- |
| **Anthropic-built** Skills | **Update automatically** |
| **Organization-provisioned** Skills | **Update automatically** |
| **Your own custom-uploaded** Skills | **Change only when you re-upload them** |

- Watch for a **misconfigured or out-of-date Skill** degrading output.
- A Skill that **silently produces a slightly off format every run** is a **maintenance problem, not a prompting problem**.

### 4.3 Memory Lifecycle
- Treat Memory **like a working file**.
- **Review periodically**; **edit or delete stale entries**.
- **Export it as a backup before a major change.**
- When Memory has accumulated **enough outdated context to mislead**, a **full reset** is the right call.
- **Accuracy of what's stored matters more than volume.**

### 4.4 Configuration Is Additive
- If Claude **hasn't automatically captured** a fact that matters (a **constraint, a preference, a piece of background**), **add it explicitly** to **standing instructions or Memory** rather than **re-supplying it each session**.

### 4.5 Worked Example: Auditing a Degraded Setup
**Symptom:** a recurring report Project starts producing **subtly wrong output**.

| Cause found by the maintenance checklist | Slot | Fix |
| :-- | :-- | :-- |
| Standing instruction references a **metric renamed last quarter** | Instructions | **Update the instruction** |
| Knowledge base holds **two versions of the template** | Knowledge base | **Remove the old template** |
| Memory entry records a **stakeholder who has left** | Memory | **Delete the stale entry** |

- **The fix is maintenance, not a new prompt.** Output returns to standard **without changing how anyone prompts**.

---

## Links to Other Lessons (Configuration Points Tested Here)

| Earlier point | Lesson | Why it matters for Domain 5 |
| :-- | :-- | :-- |
| A Project holds **standing instructions, knowledge base, own conversation history**; chats in a Project **don't share context with each other** | 01 | Basis of Project configuration |
| Memory settings: **"Search and reference chats"** (retrieves past chats on request, no profile) vs **"Generate memory from chats"** (the actual Memory feature) | 01 | Know which toggle does what |
| **Project Memory needs no separate setting**; it's on by default and distinct per Project | 01 | Supports one-Project-per-client |
| **Incognito** keeps standalone chats out of Memory and history; **doesn't override org data retention** | 01 | Sensitive work outside Projects |
| **Memory import** from other AI platforms: experimental; Free, Pro, Max, Team (not Enterprise); fallback = **add key facts to Memory manually, not to a Project knowledge base** | 01 | Slot choice for imported facts |
| Memory review **at least monthly** for active users | 01 | Same cadence as Project reviews |
| Skills **reduce but don't eliminate** variance; review stays in | 01 | A good Skill doesn't remove review |
| RFP Project: past proposals = knowledge base, extraction format = standing instructions, formatting = **account-level Skills** | 04 | Worked slot example |

---

## Exam Traps

1. **Putting a multi-step procedure in standing instructions.** Procedures belong in a **Skill**. Behaviour rules go in instructions, facts in the knowledge base.
2. **Putting a behaviour rule ("always cite sources") in the knowledge base.** It's a **standing instruction**. This and trap 1 are named as the **most common configuration mistake**.
3. **"Skills are configured inside each Project."** Skills live at the **account level under Customize** and are **reusable across any Project**.
4. **Choosing a single slot when the need spans two.** "Cite the source" needs the **instruction + the documents in the knowledge base**; a report Skill needs the **brand guide in knowledge**. Look for the **pairing** answer.
5. **Stable facts in Memory, or evolving decisions in the knowledge base.** Stable reference fact → **knowledge base**; evolving record of decisions → **Memory**.
6. **"One shared Project for all clients is fine if we tell Claude to keep them apart."** Use **one Project per client**; **project-scoped Memory** is what guarantees separation.
7. **"Connect everything so Claude has maximum access."** Keep connector access **deliberate**; you manage what's accessible.
8. **"The mail connector can send the reply."** Not necessarily: a mail connector may **search and read but not send**. Learn boundaries before building on them.
9. **Treating a connector boundary as a product bug.** It can look like a bug; misreporting sends the fix to the **wrong team**.
10. **Using the obvious add-connector path on Team/Enterprise without checking.** It may lead to a **public directory**; confirm the **org-vetted path with your admin**.
11. **Keeping old policy versions "just in case".** Duplicates invite Claude to cite the wrong one; **remove deprecated versions** as you add new ones.
12. **"Be professional" / "make it good and accurate" as instructions.** Too vague; they **fail silently**. Use precise, testable wording that **two people would read the same way**.
13. **Fixing a degraded Project by writing better prompts.** If the cause is stale instructions, duplicate templates or outdated Memory, the fix is **maintenance**.
14. **"All Skills update themselves."** Only **Anthropic-built and org-provisioned** Skills auto-update; **custom-uploaded Skills change only when re-uploaded**.
15. **Waiting for an error message to signal stale config.** There is **no error**; the signal is **quality slipping for no visible reason**. Review **monthly**.
16. **Deleting Memory before a major change without a backup.** **Export first**; **full reset** only when outdated context would mislead.
17. **Re-pasting a missing constraint each session.** Configuration is **additive**: add it to instructions or Memory once.

---

## Most Likely Questions

**Q1.** [Easy] What is the difference between "using" and "operating" Claude?
- A. Using means paid plans; operating means free plans.
- B. Using means writing a good prompt today; operating means building an environment where context, instructions and procedures are already in place.
- C. Operating means writing code against the API.
- D. There is no difference.

**Answer: B**
**Why:** Operating builds a configured baseline so every conversation starts ready, which is leverage. C describes developer work, which is outside this credential.

---

**Q2.** [Easy] Match the need to the slot: "Always cite sources."
- A. Knowledge base
- B. Standing instruction
- C. Skill
- D. Scoped Memory

**Answer: B**
**Why:** It's a rule about behaviour. Standing instructions govern behaviour, not facts.

---

**Q3.** [Easy] Match the need to the slot: "Our brand palette is these hex codes."
- A. Standing instruction
- B. Knowledge base
- C. Skill
- D. Connector

**Answer: B**
**Why:** It's a fact Claude needs. The knowledge base holds facts and reference, not behaviour.

---

**Q4.** [Medium] Where do Skills live, and what does that mean?
- A. Inside each Project; they must be rebuilt for every Project.
- B. At the account level under Customize; a Skill you build is reusable across any Project that needs it.
- C. In the knowledge base as documents.
- D. In Memory, as remembered procedures.

**Answer: B**
**Why:** Skills are not inside any one Project. Build once at the account level and reuse anywhere.

---

**Q5.** [Medium] What is described as the most common configuration mistake? (Select 2)
- A. Putting a procedure into the standing instructions
- B. Putting a behaviour rule into the knowledge base
- C. Creating one Project per client
- D. Enabling project-scoped Memory

**Answer: A, B**
**Why:** Mixing up slots makes the Project harder to maintain. C and D are recommended practices.

---

**Q6.** [Medium] Which belongs in scoped Memory rather than the knowledge base?
- A. The client's signed statement of work
- B. The company's brand guide
- C. A decision made last week to drop a section from future reports
- D. The approved price list

**Answer: C**
**Why:** Stable reference facts go in knowledge. An evolving record of Project decisions goes in Memory.

---

**Q7.** [Hard] A team adds "Always cite the source document for factual claims" as a standing instruction, but never uploads the documents. What is wrong?
- A. Nothing; the instruction is enough.
- B. The pairing rule is broken: the instruction has nothing to cite without the documents in the knowledge base.
- C. The instruction should be a Skill.
- D. Citing should be stored in Memory.

**Answer: B**
**Why:** Many needs span two slots. A behaviour rule needs the facts it acts on, and documents without the rule are used inconsistently.

---

**Q8.** [Medium] A consultant works for two competing banks. What setup prevents Bank A context from appearing in Bank B work?
- A. One shared Project with a standing instruction to keep them separate
- B. One Project per client, relying on project-scoped Memory
- C. Turning Memory off entirely
- D. Putting both clients' documents in one knowledge base

**Answer: B**
**Why:** Project-scoped Memory guarantees separation, which makes one-Project-per-client safe. A relies on an instruction instead of structural isolation.

---

**Q9.** [Medium] On a Team plan, how can an engagement team all work from the same configured baseline?
- A. Each member copies the instructions into their own chats.
- B. Share the Project with the team under permissions.
- C. Put the instructions in each person's Memory.
- D. Email the knowledge base files to everyone.

**Answer: B**
**Why:** On Team or Enterprise, a Project can be shared with the team under permissions, so everyone uses the same instructions, knowledge and configuration.

---

**Q10.** [Medium] An analyst expects Claude to send replies through the Gmail connector, but nothing happens and the failure is confusing. What is the most likely explanation?
- A. The model is too small.
- B. The connector may allow search and read but not send; this is a capability boundary.
- C. Gmail is not supported.
- D. Memory is full.

**Answer: B**
**Why:** Each connector has a defined boundary, and hitting it produces a confusing failure rather than a clear error. Learn the boundaries before building workflows on them.

---

**Q11.** [Hard] On an Enterprise plan, a user clicks the obvious add-connector option and connects a tool with a familiar name. What risk does the lesson highlight?
- A. Connectors slow Claude down.
- B. The path may route to a public directory rather than the organization's vetted connectors, so the user may connect a look-alike.
- C. Enterprise plans can't use connectors.
- D. The connector will delete files.

**Answer: B**
**Why:** Confirm the right path with your admin, especially on Team or Enterprise, so you connect the approved source.

---

**Q12.** [Medium] A connector keeps "failing", and the team files bug reports with IT, which go nowhere. What does the lesson suggest is happening?
- A. A genuine product defect
- B. Boundary confusion: the connector hit its capability limit, which looks like a bug, so the fix was misrouted
- C. A Memory conflict
- D. Usage limits

**Answer: B**
**Why:** This is a field-observed pattern. Knowing where each connector's capability ends stops the issue being mislabelled and sent to the wrong team.

---

**Q13.** [Easy] A knowledge base holds three versions of the same credit policy. What is the risk?
- A. Claude will refuse to answer.
- B. Claude may cite the wrong version.
- C. The Project will be deleted.
- D. None; more versions give more context.

**Answer: B**
**Why:** Keep uploaded knowledge current, relevant and free of duplicates. Remove deprecated versions as you add new ones.

---

**Q14.** [Medium] Which standing instruction is precise enough to change output reliably?
- A. "Be professional."
- B. "Make the reports good and accurate."
- C. "Use a formal register, define any acronym on first use, and keep paragraphs under four sentences."
- D. "Do your best."

**Answer: C**
**Why:** Vague instructions fail silently. The test is whether two different people would read it the same way, and only C passes.

---

**Q15.** [Medium] A reporting Project's standing instructions say: "For every figure, state its source. If a figure is not in the provided data, mark it 'unverified' rather than including it. Lead each report with a one-sentence headline." What does this achieve?
- A. It guarantees every figure is correct.
- B. It makes the verification behaviour and headline consistent in every conversation.
- C. It replaces the need for a knowledge base.
- D. It turns on code execution.

**Answer: B**
**Why:** Precise guardrails written once are inherited by every chat. They improve consistency but don't guarantee correctness (A), and they still need the data in the Project (C).

---

**Q16.** [Medium] How often should active Projects be reviewed, and what is the sign you waited too long?
- A. Yearly; an error message appears.
- B. Monthly; output quality slips for no visible reason.
- C. Never; configurations don't age.
- D. Daily; Claude asks for a review.

**Answer: B**
**Why:** A monthly pass catches most drift. Stale configuration degrades quietly, with no error to alert you.

---

**Q17.** [Hard] Which Skills update automatically? (Select 2)
- A. Anthropic-built Skills
- B. Organization-provisioned Skills
- C. Your own custom-uploaded Skills
- D. Skills stored in the knowledge base

**Answer: A, B**
**Why:** Custom-uploaded Skills change only when you re-upload them. Skills aren't stored in the knowledge base (D).

---

**Q18.** [Hard] A weekly report Skill produces a slightly wrong format every run. Prompt tweaks don't help. What is the correct diagnosis?
- A. A prompting problem; write longer prompts.
- B. A maintenance problem: a misconfigured or out-of-date Skill.
- C. A model problem; switch to Opus.
- D. A connector problem.

**Answer: B**
**Why:** A Skill that silently produces an off format every run is a maintenance problem, not a prompting problem. Fix or re-upload the Skill.

---

**Q19.** [Hard] A recurring report Project produces subtly wrong output. The audit finds a renamed metric still referenced in the instructions, two template versions in the knowledge base, and a Memory entry for a stakeholder who left. What is the fix? (Select 3)
- A. Update the standing instruction to the new metric name
- B. Remove the old template from the knowledge base
- C. Delete the stale Memory entry
- D. Ask users to write more detailed prompts

**Answer: A, B, C**
**Why:** The fix is maintenance, not a new prompt. Output returns to standard without changing how anyone prompts.

---

**Q20.** [Hard] Before restructuring a long-running Project, a manager notices its Memory is full of outdated context that keeps misleading Claude. What is the best sequence?
- A. Delete everything immediately.
- B. Export Memory as a backup, then do a full reset and add back what's still accurate.
- C. Ignore it; more memory is better.
- D. Move all Memory into the knowledge base.

**Answer: B**
**Why:** Export as a backup before a major change; a full reset is right when outdated context misleads. Accuracy matters more than volume. A skips the backup. D mixes up the slots.

---

## Key Takeaways

1. **Operate, don't just use.** Configuration gives every conversation a ready baseline, turns individual skill into team capability, and needs **regular maintenance**.
2. **Four slots:** Instructions = **behaviour**. Knowledge base = **facts**. Skills = **procedures** (account level under Customize, reusable). Scoped Memory = **continuity** (settled decisions and preferences, isolated per Project).
3. **Ask "instruction, knowledge, or Skill?"** Misplacing procedures or behaviour rules is the most common mistake. Stable facts go in the knowledge base; evolving decisions go in Memory. Many needs **pair two slots**.
4. **One Project per client**, shared under permissions on Team/Enterprise. Project-scoped Memory keeps clients apart.
5. **Connectors:** authorize deliberately, learn each one's boundaries (mail may read but not send), add through the **org-vetted** path, and don't mistake a boundary for a bug.
6. **Uploaded knowledge:** current, relevant, no duplicates. Remove old versions as you add new ones.
7. **Standing instructions:** write guardrails once, anticipate use cases, and be **precise**. Vague instructions fail silently. The test: would two people read it the same way?
8. **Maintain monthly.** Only Anthropic-built and org-provisioned Skills auto-update; custom ones need re-uploading. Curate Memory (export before big changes, reset when misleading). Add missing facts explicitly. When output degrades, **fix the configuration, not the prompt**.
