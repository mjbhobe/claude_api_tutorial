# 06 · Governance, Risk & Responsible Use (Revision Notes)

## Where This Lesson Sits in the Exam

| Domain | Weight | Objectives covered here |
| :-- | :-- | :-- |
| **6 · Governance, Risk, and Responsible Use** | **15%** (3rd largest) | Identify appropriate and inappropriate use cases · Apply data sensitivity, regulatory, and privacy considerations · Follow organizational AI policies and governance standards · Understand the ethical implications of AI usage |

### Exam Objective → Where It Is Covered

| Domain 6 objective (exam guide) | Sections in these notes |
| :-- | :-- |
| Identify **appropriate and inappropriate use cases** | 1.1 to 1.5 |
| Apply **data sensitivity, regulatory, and privacy** considerations | 2 (Skill/feature risk), 3.1 to 3.6 |
| Follow **organizational AI policies** and governance standards | 4.1 to 4.4 |
| Understand the **ethical implications** of AI usage | 5.1 to 5.5 |

### Core Ideas
- **One inappropriate use case can freeze an entire organization's AI program**: sensitive data uploaded to the wrong place, an untrusted Skill with broad access, a quiet policy violation at the wrong moment. A freeze costs **every team** the productivity it had gained.
- **Governance keeps adoption moving safely.** It is exercised **by practitioners, one decision at a time**, not by a policy binder on a shelf.
- **Governance is a practitioner skill.** Policy sets the boundary; **you decide in the moment** whether this use case, Skill, or upload is appropriate.
- **Two AI Fluency competencies:**
  - **Diligence** = ownership and verification.
  - **Delegation** = the criteria for judging whether a use case is appropriate at all.

---

## Memory Map

```
GOVERNANCE, RISK & RESPONSIBLE USE
│
├── WHY: one bad use case can FREEZE the whole AI program
│     governance = practitioner skill, one decision at a time
│     DILIGENCE (ownership, verification) + DELEGATION (is the use case appropriate?)
│
├── 1. USE-CASE SCREENING (structured, not gut feel)
│     ├── 4 criteria: REVERSIBILITY · CONSEQUENCE OF ERROR ·
│     │     NEED FOR HUMAN CREATIVITY/EMPATHY · ACCOUNTABILITY
│     ├── Criteria INTERACT → name the LOAD-BEARING one
│     │     (the one that, if changed, moves the classification)
│     ├── 3 classes: FULLY APPROPRIATE · APPROPRIATE WITH HUMAN REVIEW · INAPPROPRIATE
│     ├── "With human review" → DEFINE THE GATE: WHO (accountable role) ·
│     │     WHAT (specific risk) · WHEN (before use). Can't state it → not ready
│     └── Portfolio: FAQ = fully · resume shortlist = review + bias safeguards ·
│           final medical/legal determination = inappropriate ·
│           billing-complaint replies = review, load-bearing = ACCOUNTABILITY
│
├── 2. SKILL TRUST & FEATURE RISK (a Skill is software)
│     ├── Check: SOURCE · REACH (inherits session access; audit bundle) · APPROPRIATENESS
│     ├── Internal ≠ vetted (sister-department software)
│     ├── Outcomes: ENABLE · ESCALATE (admin/security) · DECLINE
│     └── Any feature (connector, tool, integration): who provides · what it accesses ·
│           proportional? → LEAST PRIVILEGE, revisit when job changes
│
├── 3. DATA SENSITIVITY & FEATURE CONTROLS
│     ├── CLASSIFY BEFORE UPLOAD; unsure → ask; between tiers → treat as MORE sensitive
│     │     GREEN safe · YELLOW review first · RED keep out unless approved path
│     ├── Redaction: when task doesn't need identifiers ("Customer 1, 2")
│     │     Failures: PARTIAL redaction (account no., rare title, date) ·
│     │     redaction that BREAKS THE TASK → approved path or keep out
│     ├── Controls: code-exec SANDBOX · MEMORY persistence · INCOGNITO
│     │     (out of history + Memory, NOT out of org retention/exports) ·
│     │     ORG MEMORY: Team = none · Enterprise = Owners/Primary Owners
│     ├── Match: Green → none · Yellow (no persistence) → Incognito ·
│     │     Red → approved entry point FIRST
│     └── INCOGNITO DOES NOT MAKE RED DATA SAFE ("allowed here?" comes first)
│
├── 4. POLICY & DILIGENCE AS A HABIT
│     ├── Followed only when watched ≠ governance; risk lives in the policy/practice gap
│     ├── Apply on ROUTINE low-visibility decisions (drift accumulates there)
│     ├── AUDIT usage vs policy → close gaps · STAY CURRENT (policy + features change)
│     └── Mini audit: unreleased spec to non-approved entry point · unvetted Skill ·
│           skipped review gate → all DRIFT, not malice → habit-level fixes
│
└── 5. ETHICS: BIAS · FAIRNESS · TRANSPARENCY (part of routine review)
      ├── Bias from prompt, framing, language patterns; highest risk in people-facing work
      ├── Disclosure: depends on setting/audience/policy; unsure → DISCLOSE
      ├── Ambiguous cases: WHO affected · WHAT could go wrong · FAIR outcome ·
      │     DISCLOSURE needed → document reasoning
      ├── Escalate to governance/ethics function: large population · significant harm ·
      │     outside team's standing → bring REASONING, not a verdict
      └── Performance-review summaries → appropriate with human review + fairness check
```

---

## 1. Appropriate vs Inappropriate Use Cases

Deciding whether a use case is appropriate is a **structured evaluation, not a gut feeling**. The same **Delegation** criteria that map workflow steps also **screen whole use cases**. Running them every time turns **vague unease into a defensible call**.

### 1.1 Delegation Criteria for Screening (four)

| Criterion | Question to ask |
| :-- | :-- |
| **Reversibility** | Can a wrong output be **caught and undone before it causes harm**? **Irreversible consequences raise the bar sharply.** |
| **Consequence of error** | What is the cost if wrong? Higher consequence → **more human control**, or **rules the use case out** |
| **Need for human creativity or empathy** | Does it need **judgment, relationship, or care** AI cannot supply? Some work **stays human regardless of capability** |
| **Accountability** | Who is answerable, and **can that accountability be exercised over an AI-produced result**? |

### 1.2 The Criteria Interact: Name the Load-Bearing One
- The four criteria are **not a checklist where any single failure ends the discussion**. They **interact**.
- A task can be **low-consequence and reversible and still need human review**. **Accountability cannot be transferred to a model.**
  - Example: a **condolence note to a client** is low-stakes and fully reversible, but the **relationship element** means **a person should own it**.
- A task can be **high-consequence but still appropriate with the right gate**.
  - Example: a **financial summary feeding a decision** is consequential, but if a **named reviewer signs off before it's used**, **accountability and reversibility are restored**.
- **Practical rule:** run **all four**, then ask which one is **load-bearing** for this use case.
- **Load-bearing criterion** = the one that, **if changed, would move the use case between classifications**.
- **Naming it makes your classification defensible** to a risk or compliance reviewer.

### 1.3 Three Classifications (always with documented rationale)

| Classification | When | What to do |
| :-- | :-- | :-- |
| **Fully appropriate** | Reversible, low consequence, no special human element | **Delegate with normal review** |
| **Appropriate with human review** | Useful for AI assistance, but **stakes or accountability need a human gate** | **Define the gate explicitly** |
| **Inappropriate** | Consequence, irreversibility, or human-element requirement means AI should not do it | **Articulate why** and **name the human role that must own it** |

### 1.4 The Gate Is the Classification
- "Appropriate with human review" is the classification **people most often get wrong**: they **stop at the label and never specify the gate**.
- The gate is **not** "someone will check it."
- **A defined gate states three things:**

| Element | Meaning |
| :-- | :-- |
| **Who** reviews | The **role with the accountability**, not whoever is free |
| **What** they verify | The **specific risk** the review exists to catch (factual accuracy, fairness, policy compliance) |
| **When** it happens | **Before the output is used**, not after |

- Defined gate: "A **manager** reviews the shortlist **for adverse-impact patterns** **before any candidate is contacted**."
- Not a gate: "We will keep a human in the loop."
- **If you can't state the gate in who/what/when form, the use case is not ready to run.**

### 1.5 Worked Example: A Use-Case Portfolio

| Use case | Classification | Reasoning |
| :-- | :-- | :-- |
| Draft internal FAQ from **approved policy docs** | **Fully appropriate** | Reversible, low stakes, **factual grounding available** |
| Summarize candidate resumes to a **shortlist** | **Appropriate with human review**, **only with bias safeguards** | Consequential, **fairness-sensitive**; accountability rests with the **hiring manager**, who **owns the selection** |
| Generate a **final medical or legal determination** | **Inappropriate** | **Irreversible consequence** + **professional accountability that can't transfer to a tool**; the human professional makes and owns it |
| Draft **customer-facing responses to billing complaints** (the hard one) | **Appropriate with human review**; **load-bearing criterion = accountability** (the company owns what it tells a customer about their money) | Reversible **if reviewed before sending**; moderately consequential (erodes trust, **can have regulatory weight** in some industries); partly relationship-sensitive |

- Billing-complaint **gate**: **a support agent** reads each drafted response **for accuracy against the actual account record** and **adjusts tone** **before it sends**.
- The interesting governance work is **naming the gate for the cases in the middle**, not the obvious yes/no ones.
- **The deliverable is articulating why** a use case fails and **what human role must be retained**. "It feels risky" doesn't travel; "**irreversible consequence plus non-transferable accountability**" does.

---

## 2. Skill Trust and Feature-Level Risk

**A Skill is software.** It can access **what you give Claude access to during a session** and can **take actions through code execution**. A Skill from an **untrusted source is a real risk**. The answer is a **source-and-permissions check before enabling it**.

### 2.1 Why Untrusted Skills Are a Risk
- A Skill runs procedures and can touch **data and tools available in the session**; one from an unknown source could **mishandle data or take unintended actions**.
- "Skills are a black box" is a common worry. The answer is **neither blind trust nor blanket bans**, but a **repeatable trust evaluation**.

### 2.2 Trust Evaluation Before Enabling (three checks)

| Check | Question | Key points |
| :-- | :-- | :-- |
| **Source** | Who published it? | **Anthropic-provided and internally approved** Skills = **lower-risk starting point**; **unknown third-party** = **more scrutiny** |
| **Reach** | What could it reach in the session where it will run, and is that **proportional to the task**? | **Skills don't request permission**; a Skill **inherits whatever access the session already has**. **Audit the bundle** (instructions, dependencies, bundled files) before enabling. **A formatting Skill whose instructions roam far beyond formatting is a red flag** |
| **Appropriateness** | Is it the right tool at all, or **more capability than the job needs**? | |

### 2.3 Internal Does Not Mean Vetted
- Source isn't a simple trusted/untrusted switch. **Hardest case: a Skill built by another team in your own organization.**
- "Internal" feels safe but **isn't vetted**: the team may have given it **broad access for their own convenience** or built it **against an older policy**.
- Treat it like **software from a sister department**: **confirm with the publisher what it accesses and why**, and check its access **still matches current policy**, before enabling it on your data.
- **The trust question:** "**Do I know what it does, and does its access match the job?**"

### 2.4 Three Outcomes from a Trust Check
Failing the check doesn't always mean "never use it". It means **don't enable it on your authority alone**.

| Outcome | When |
| :-- | :-- |
| **Enable** | Source, access (permissions), and appropriateness **all clear** |
| **Escalate** | Useful, but **source unknown** or **access looks broad** → route to **admin or security function** |
| **Decline** | Access **clearly disproportionate** or **source can't be established**, and **no review would change that** |

**The judgment = identifying which of the three applies.**

### 2.5 Worked Example: Vetting Two Skills

| Skill | Assessment | Call |
| :-- | :-- | :-- |
| **Anthropic-provided document formatter** | Trusted source; access matches the task (document handling); appropriate | **Enable** |
| **Third-party "analytics booster"**, unknown publisher, wanting **broad data access** | Unknown source; **disproportionate access** for stated purpose | **Don't enable without your organization's review**; treat like **unvetted installed software** |

- **General rule:** evaluate a Skill's source and access **like any software you'd install on a work machine**.

### 2.6 Beyond Skills: Feature-Level Risk and Least Privilege
- Skills are the **sharpest** case, but the same habit applies to **any capability that can read or act on your data**: a **connector, a tool, an integration**.
- Ask the same three questions: **who provides it**, **what does it access**, **is that access proportional**?
- **Principle of least privilege:** grant the **narrowest access** that gets the job done, and **revisit it when the job changes**.

---

## 3. Data Sensitivity, Privacy & Feature Controls

**Before any data enters any feature, know its sensitivity.** **Classification prevents leakage**; feature controls (**Incognito, Memory management, sandbox awareness**) are how you act on it when persistence or processing isn't appropriate.

### 3.1 Classify Before You Upload
- Sort data into **safe to use**, **needs review first**, and **stays out entirely**.
- Public and internal low-sensitivity material is generally fine; **regulated, confidential, or personal data** needs a **deliberate check against policy** first.
- **Unsure? The safe default is to ask before uploading.**

| Tier | Meaning | Examples |
| :-- | :-- | :-- |
| **Green: Safe to use** | Use freely | **Published material**, **anonymized or aggregated data**, internal documents **already cleared for wide sharing** |
| **Yellow: Review first** | Check policy before use | Internal docs **not meant to leave the company**, anything with **names or contact details**, **draft material tied to an unannounced deal or product** |
| **Red: Keep out unless an approved path exists** | Don't upload without a confirmed approved path | **Regulated data (health, financial, government)**, **credentials and secrets**, anything under a **confidentiality obligation to a third party** |

- **Unsure between two tiers? Treat it as the more sensitive one** until confirmed otherwise.

### 3.2 Redaction and Anonymization
- When the task **doesn't need the sensitive specifics, remove them**.
- Redacting **names, account numbers, identifiers** before upload gives the **analytical value without exposing the data**.
- This habit prevents the **most common form of accidental leakage**.
- Works **when the task doesn't depend on the identifiers**: trends across a customer list don't need names; "Customer 1, Customer 2" loses nothing.

**Two redaction failure modes**

| Failure | What goes wrong | Fix |
| :-- | :-- | :-- |
| **Partial redaction** | Removing the name but leaving an **account number, rare job title, or specific date** can still identify someone, **especially in a small population** | **Strip every field that could lead to identification** |
| **Redaction that breaks the task** | The work **genuinely needs** the sensitive specifics | Redaction isn't the answer: **confirm an approved path** or **keep it out**. Redaction is for when **sensitivity and necessity don't overlap**; it **doesn't make any data safe** |

### 3.3 Feature-Specific Controls

| Control | What it does | Practitioner note |
| :-- | :-- | :-- |
| **Code execution sandbox** | Code runs in a **sandboxed environment**; **uploaded files are processed there** | **Review what you upload** before running analysis |
| **Memory persistence** | Carries information **across sessions** | For sensitive work, that persistence may be **exactly what you don't want** |
| **Incognito mode** | Keeps the session **out of chat history and Memory** | **Still follows org data-retention policies** and **can appear in organizational data exports**. **Memory exclusion and data retention are separate controls.** Use for sensitive conversations or confidential inputs that shouldn't surface in history or Memory |
| **Org-level Memory controls** | **Team plans: no org-level controls** for memory. **Enterprise: Owners and Primary Owners** hold org-wide Memory controls, **including disabling memory for the organization** | Know **your plan** and **who controls the setting**; verify current behaviour in the Claude Help Center memory article (support.claude.com) |

### 3.4 Classify First, Then Pick the Matching Control

| Tier | Control |
| :-- | :-- |
| **Green** | **No special control** |
| **Yellow** that shouldn't persist (confidential, not regulated) | **Incognito**: analysis now, not in Memory or chat history (**org retention still applies**) |
| **Red** | **Approved entry point confirmed before anything is uploaded**, **regardless of Memory settings** |

- **Common error: using Incognito and assuming it makes sensitive data safe.**
- **Incognito does not make Red data safe.** It controls **whether something is remembered**, not **whether the data was allowed here in the first place**. For regulated data, **"is it allowed here?" comes first**.

### 3.5 Awareness Across Entry Points
- Different claude.ai entry points **may handle data retention differently** depending on **how your organization configured Claude**.
- You don't need the technical detail; you need the **habit of asking before uploading** when unsure about an entry point.
- **Plain rule: know your data's sensitivity first, then match the feature and its controls to it.**

### 3.6 Worked Example: Four Data Decisions

| Data | Tier | Decision |
| :-- | :-- | :-- |
| **Anonymized survey data** for trend analysis | **Green** | Safe to upload; **use code execution for verified counts**; no identifiers |
| **Confidential M&A document** for summarization | **Yellow** | **Review against policy first** + **Incognito** (not in Memory/history; **still subject to org retention**). If policy prohibits the entry point, **it stays out** |
| **Spreadsheet of customer PII** for cleanup | (contains personal identifiers) | **Redact or anonymize identifiers before upload**, **or keep it out** and **confirm the approved path with your admin** |
| **Patient records** for a healthcare workflow summary | **Red** (the case Incognito doesn't solve) | First question: **is this entry point approved for protected health information at all?** If no approved, compliant path is confirmed → **stop and escalate to your admin** |

- For regulated data, **"is this allowed here" is settled before "how do I handle it here."**

---

## 4. Organizational Policies and Diligence as a Habit

**A policy followed only when someone is watching is not governance.** The **gap between what the policy says and what people do is where risk lives**. Diligence = applying the framework **consistently** and **auditing real usage** to close gaps.

### 4.1 Apply Governance Consistently
- Compliance is a **sustained habit, not a one-time acknowledgment**.
- Apply the framework on **routine, low-visibility decisions**, not only the obvious high-stakes ones, because **routine decisions are where drift accumulates unnoticed**.

### 4.2 Audit Usage Against Policy
- **Periodically compare** what your team does (or plans to do) with Claude against what policy requires.
- Divergence = a **Diligence gap** to close, e.g.:
  - a **data type uploaded that shouldn't be**,
  - a **review step skipped**,
  - a **Skill enabled without vetting**.

### 4.3 Stay Current
- **Policies and capabilities both evolve.** A practice compliant **last quarter** may not be after a **policy update or new feature**.
- Staying current keeps your **judgment in step with the tools and the rules**.

### 4.4 Worked Example: A Mini Usage Audit
A team lead reviews **a month** of Claude use and finds three gaps:

| Gap found | Habit-level fix |
| :-- | :-- |
| Marketer uploaded an **unreleased product spec** to a **non-approved entry point** | **Reminder on approved entry points** |
| A **Skill was enabled without a source check** | **Skill-vetting step added to Project setup** |
| A recurring **client report skipped its required human-review gate twice** under deadline pressure | **Non-negotiable review gate on client deliverables** |

- **None was malicious; all were drift.**
- The audit **converted invisible risk into three closeable actions**.

---

## 5. Ethical Implications: Bias, Fairness, Transparency

**Ethical risk doesn't announce itself; it hides in ordinary outputs**: a summary that **quietly favours one group**, a recommendation built on a **biased framing**, an AI-assisted document **presented as fully human-authored**. Evaluate bias, fairness and transparency **in routine review, not as a separate ethics exercise**.

### 5.1 Recognize Bias and Fairness Risk
- Bias can come from **the prompt, the framing, or underlying patterns in how language is generated**.
- In **people-facing work** (**hiring, evaluation, communications to specific groups**) check whether the output **treats people fairly** and whether a **framing has tilted the result**.
- **Risk is highest where stakes for individuals are highest.**

### 5.2 Transparency and Disclosure
- Know **when to disclose AI assistance**. Some **contexts and organizational policies require it**; others treat it as routine tooling.
- The obligation **depends on the setting and the audience**.
- **Responsible default when unsure: disclose rather than conceal.**

### 5.3 Reasoning Through Ambiguous Cases (four questions)
1. **Who is affected?**
2. **What could go wrong?**
3. **What does the fair outcome look like?**
4. **What disclosure does the situation call for?**

- **Reason it through and document the reasoning**: the professional standard when **no policy gives a direct answer**.

### 5.4 When Reasoning Alone Is Not Enough (escalate)
Escalate to your organization's **AI governance or ethics function** rather than deciding alone if:
- the **affected population is large**,
- the **potential harm is significant**, or
- the question touches areas your **team doesn't have standing to resolve**.

- **Escalate with documented reasoning, not a verdict.** It shows you **applied the framework**, **identified where it ran out**, and **flagged the gap** for the right reviewer.

### 5.5 Worked Example: Performance-Review Summaries
A manager uses Claude to draft performance-review summaries **from their own notes**.

| Question | Answer |
| :-- | :-- |
| Who is affected? | **The employees** |
| What could go wrong? | Generated phrasing introduces an **unfair or inconsistent tone across reviews** |
| Fair outcome? | Manager **verifies each summary reflects the actual notes** and **applies a consistent standard** |
| Disclosure? | The setting **may call for disclosing** that AI assisted the drafting |

- **Conclusion: appropriate with human review and a fairness check**, not a blanket yes or no.
- **The reasoning, not the verdict alone, makes the decision defensible.**

---

## Links to Other Lessons (Governance Points Tested Here)

| Earlier point | Lesson | Why it matters for Domain 6 |
| :-- | :-- | :-- |
| **Incognito** applies to **standalone chats, outside Projects**, and doesn't override org data retention | 01 | Incognito can't be used as a control inside a Project |
| **Project-scoped Memory** keeps client contexts apart | 01, 05 | Prevents revealing one client's information to another |
| On **Team/Enterprise**, an **Owner or Primary Owner** must enable **web search** for the workspace | 01 | Admin-controlled capabilities |
| **Do-not-ship-without-review** list includes **regulated, confidential, or highly sensitive data** and **public or legal communications** | 03 | Overlaps with Red-tier data and "appropriate with human review" |
| **Confirmation bias**: prompts that imply a preferred answer tilt the output | 03 | A source of bias in framing |
| **Delegation mapping** (reversibility, stakes, accountability); over-delegation; staffed review gates | 04 | Same thinking, applied here to whole use cases |
| Add connectors through the **org-vetted path** (the obvious path may lead to a public directory); keep connector access **deliberate** | 05 | Feature-level risk and least privilege |

---

## Exam Traps

1. **"Incognito makes sensitive or regulated data safe."** No. Incognito only keeps a chat out of history and Memory. It doesn't confirm the data was **allowed** there, and chats still follow **org retention** and can appear in **org data exports**.
2. **"Tell Claude not to retain it" as a privacy control.** An instruction to the model doesn't satisfy a policy control. Redact/anonymize, or use an approved path.
3. **"Skip the task entirely" when anonymization would work.** Unnecessary. If the task doesn't need identifiers, **redact** and proceed.
4. **Partial redaction.** Removing names but leaving account numbers, rare job titles or specific dates can still identify people, especially in small groups.
5. **Redacting data the task actually needs.** Then redaction breaks the task; use an approved path or keep the data out.
6. **Unsure between Yellow and Red → pick the lighter tier.** Wrong. Treat it as the **more sensitive** tier until confirmed.
7. **"Appropriate with human review" with no defined gate.** "We'll keep a human in the loop" is not a gate. State **who (accountable role), what (specific risk), when (before use)**.
8. **Treating the four screening criteria as a pass/fail checklist.** They interact; name the **load-bearing** criterion.
9. **"Low stakes + reversible = fully appropriate, always."** Not if a human element applies (e.g., condolence note) or accountability can't transfer.
10. **"High consequence = always inappropriate."** A defined human gate (named reviewer signs off before use) can make it appropriate with review.
11. **"Internal Skill = safe."** Internal doesn't mean vetted. Confirm with the publisher what it accesses and that it matches **current** policy.
12. **"Skills ask for permissions, so I'll see what they access."** Skills **don't request permission**; they **inherit whatever access the session has**. Audit the bundle.
13. **Choosing only "enable" or "ban".** There's a third outcome: **escalate** to admin/security when useful but the source is unknown or access looks broad.
14. **Granting broad access "just in case".** Apply **least privilege** and revisit when the job changes.
15. **"Team plan admins can switch off Memory for everyone."** Team plans have **no** org-level Memory controls; on **Enterprise**, **Owners/Primary Owners** can disable Memory org-wide.
16. **Asking "how do I handle it?" before "is it allowed here?" for regulated data.** Permission comes first; if no approved path, stop and **escalate to your admin**.
17. **Bringing a verdict to the ethics function.** Bring **documented reasoning** that shows where the framework ran out.
18. **Unsure about disclosure → stay quiet.** Default is to **disclose**.
19. **Mixing criteria sets across lessons.** Use-case screening here has **four**: reversibility, **consequence of error**, **need for human creativity or empathy**, accountability. Workflow step mapping (Lesson 04) has **three**: reversibility, stakes, accountability. Output review thresholds (Lesson 03) have **four**: stakes, reversibility, audience, regulatory exposure.
20. **Governance only on big decisions.** Drift accumulates in **routine, low-visibility** decisions; audit usage regularly.

---

## Most Likely Questions

**Q1.** [Easy] A project manager wants to upload a spreadsheet with customer names and account numbers so Claude can analyze trends. Policy restricts sharing regulated personal data. What is the most appropriate action?
- A. Upload as-is, since the analysis is internal.
- B. Remove or anonymize the personal identifiers before uploading, consistent with policy.
- C. Upload but tell Claude not to retain the file.
- D. Skip the analysis entirely.

**Answer: B**
**Why:** Trend analysis doesn't need identifiers, so redaction keeps the value without exposing data. A violates policy. C relies on an instruction to the model, which doesn't satisfy the policy control. D is unnecessary when anonymization enables the task.

---

**Q2.** [Easy] Which are the four delegation criteria for screening a use case? (Select 4)
- A. Reversibility
- B. Consequence of error
- C. Need for human creativity or empathy
- D. Accountability
- E. Output length

**Answer: A, B, C, D**
**Why:** These four screen whole use cases. Length (E) is irrelevant.

---

**Q3.** [Medium] What is the "load-bearing" criterion in a use-case classification?
- A. The criterion that scores highest
- B. The criterion that, if changed, would move the use case between classifications
- C. Always accountability
- D. The first criterion you check

**Answer: B**
**Why:** Run all four criteria, then name the one that actually decides the classification. That makes the call defensible to risk or compliance reviewers. Accountability is load-bearing in the billing example, but not always (C).

---

**Q4.** [Medium] Drafting a condolence note to a client is low-stakes and fully reversible. How should it be classified?
- A. Fully appropriate; delegate entirely.
- B. Inappropriate; AI must never touch it.
- C. A person should own it because of the relationship element, even though stakes are low and it's reversible.
- D. Escalate to the ethics function.

**Answer: C**
**Why:** The criteria interact. The need for human empathy and relationship is load-bearing here, so a person should own it. A ignores the human element. B and D overreact.

---

**Q5.** [Medium] Which statement is a properly defined human-review gate?
- A. "We will keep a human in the loop."
- B. "Someone will check it."
- C. "A manager reviews the shortlist for adverse-impact patterns before any candidate is contacted."
- D. "The team will look at outputs when they have time."

**Answer: C**
**Why:** A defined gate names who (the accountable role), what (the specific risk: adverse impact) and when (before use). The others give none of these.

---

**Q6.** [Medium] Which use case is inappropriate for AI to perform?
- A. Drafting an internal FAQ from approved policy documents
- B. Summarizing resumes into a shortlist with bias safeguards and manager review
- C. Generating a final medical or legal determination
- D. Drafting billing-complaint responses that an agent reviews before sending

**Answer: C**
**Why:** Final medical or legal determinations have irreversible consequences and professional accountability that can't transfer to a tool. A is fully appropriate. B and D are appropriate with human review.

---

**Q7.** [Hard] A bank wants Claude to draft replies to customer billing complaints. Which classification, load-bearing criterion and gate are correct?
- A. Fully appropriate; reversibility; no gate needed
- B. Appropriate with human review; accountability; a support agent checks each reply against the actual account record and adjusts tone before sending
- C. Inappropriate; empathy; humans must write every reply
- D. Appropriate with human review; output length; a manager spot-checks weekly

**Answer: B**
**Why:** The company owns what it tells customers about their money, so accountability is load-bearing. The gate must be who/what/when, before sending. D's gate is after the fact and uses an irrelevant criterion.

---

**Q8.** [Medium] What are the three checks before enabling a Skill?
- A. Speed, cost, quality
- B. Source, reach, appropriateness
- C. Role, context, task
- D. Stakes, audience, reversibility

**Answer: B**
**Why:** Who published it, what it could reach in the session and whether that's proportional (audit the bundle), and whether it's the right tool for the job.

---

**Q9.** [Hard] Which statements about Skill access are correct? (Select 2)
- A. Skills request specific permissions before running.
- B. A Skill inherits whatever access the session it runs in already has.
- C. You should audit the bundle's instructions, dependencies and files before enabling.
- D. Skills can't take actions, only read text.

**Answer: B, C**
**Why:** Skills don't request permission; they inherit session access, so ask what they could reach and audit the bundle. D is false: Skills can act through code execution.

---

**Q10.** [Medium] A Skill built by another department in your company would be useful, but you don't know what it accesses. What should you do?
- A. Enable it; internal Skills are vetted.
- B. Confirm with the publisher what it accesses and why, and that its access matches current policy, before enabling it on your data.
- C. Decline it permanently.
- D. Enable it in Incognito.

**Answer: B**
**Why:** Internal doesn't mean vetted. It may have broad access for the builders' convenience or be built against an older policy. Treat it like sister-department software.

---

**Q11.** [Medium] A useful third-party Skill has an unknown publisher and looks like it would reach far more data than its stated purpose needs. What is the best outcome of your trust check?
- A. Enable it.
- B. Escalate (or don't enable) pending your organization's review.
- C. Enable it but avoid sensitive files.
- D. Rewrite its instructions yourself.

**Answer: B**
**Why:** An unknown source plus disproportionate access means you don't enable it on your own authority. Escalate to admin or security, or decline if no review would change the picture.

---

**Q12.** [Easy] What does the principle of least privilege mean for connectors, tools and integrations?
- A. Give the broadest access so nothing breaks.
- B. Grant the narrowest access that gets the job done, and revisit it when the job changes.
- C. Only admins may use connectors.
- D. Disable all features.

**Answer: B**
**Why:** Ask who provides it, what it accesses and whether that access is proportional, then grant the minimum.

---

**Q13.** [Medium] Classify: a draft press release for a product that hasn't been announced yet.
- A. Green
- B. Yellow
- C. Red
- D. No classification needed

**Answer: B**
**Why:** Draft material tied to an unannounced deal or product is Yellow: review first. Red is regulated data, credentials and secrets, or third-party confidentiality obligations.

---

**Q14.** [Medium] An analyst can't decide whether a dataset is Yellow or Red. What should they do?
- A. Treat it as Yellow to keep working.
- B. Treat it as Red until they can confirm otherwise.
- C. Upload it in Incognito.
- D. Split the file in half.

**Answer: B**
**Why:** When unsure between two tiers, treat data as the more sensitive one. The safe default is to ask before uploading.

---

**Q15.** [Hard] An employee removes customer names from a file but leaves account numbers, rare job titles and exact dates, then uploads it. What is the problem?
- A. None; names were removed.
- B. Partial redaction: the remaining fields can still identify people, especially in a small population.
- C. The redaction broke the task.
- D. The file should have been put in Memory.

**Answer: B**
**Why:** Strip every field that could lead to identification, not just names.

---

**Q16.** [Hard] A team wants to summarize patient records for a healthcare workflow and plans to use Incognito "to be safe". What is the correct action?
- A. Proceed in Incognito; the data won't be remembered.
- B. First confirm whether this entry point is approved for protected health information; if no approved, compliant path exists, stop and escalate to the admin.
- C. Redact patient names and proceed.
- D. Turn off Memory and proceed.

**Answer: B**
**Why:** This is Red, regulated data. Incognito controls whether data is remembered, not whether it was allowed there. "Is it allowed here" comes before "how do I handle it".

---

**Q17.** [Medium] Which statements about Incognito are true? (Select 2)
- A. It keeps the chat out of history and Memory.
- B. It exempts the chat from organizational data-retention policies.
- C. Incognito chats can appear in organizational data exports.
- D. It makes regulated data safe to upload.

**Answer: A, C**
**Why:** Memory exclusion and data retention are separate controls. Incognito still follows org retention, can appear in exports, and doesn't make Red data safe.

---

**Q18.** [Medium] Who can disable Memory for an entire organization?
- A. Any member on a Team plan
- B. Team plan admins
- C. Owners and Primary Owners on Enterprise
- D. Nobody; Memory can't be disabled

**Answer: C**
**Why:** Team plans have no org-level Memory controls. On Enterprise, Owners and Primary Owners hold org-wide Memory controls, including disabling it.

---

**Q19.** [Hard] A monthly usage audit finds: an unreleased spec uploaded to a non-approved entry point, a Skill enabled without a source check, and a client report that skipped its review gate twice under deadline pressure. Which responses fit? (Select 3)
- A. A reminder on approved entry points
- B. A Skill-vetting step added to Project setup
- C. A non-negotiable review gate on client deliverables
- D. Disciplinary action, since the gaps were malicious

**Answer: A, B, C**
**Why:** None of the gaps was malicious; all were drift. The fixes are habit-level, and the audit turned invisible risk into closeable actions.

---

**Q20.** [Hard] A manager uses Claude to draft performance-review summaries from their own notes and isn't sure about the ethics. Which approach matches the lesson? (Select 2)
- A. Reason through who is affected, what could go wrong, the fair outcome and the disclosure needed, and document it.
- B. Classify it as appropriate with human review plus a fairness check: verify each summary matches the notes and applies a consistent standard.
- C. Ban AI for HR work entirely.
- D. Let Claude finalize the summaries to ensure consistency.

**Answer: A, B**
**Why:** Structured, documented reasoning gives the defensible conclusion: appropriate with human review and a fairness check. Disclosure may be required, and when unsure the default is to disclose. C is a blanket no; D removes the human gate.

---

## Key Takeaways

1. **Governance is a practitioner skill.** One bad use case can freeze the whole AI program. Diligence gives ownership; Delegation gives the criteria.
2. **Screen use cases with four criteria:** reversibility, consequence of error, need for human creativity or empathy, accountability. They interact, so **name the load-bearing one**.
3. **Three classifications:** fully appropriate, appropriate with human review, inappropriate. **"With review" needs a defined gate: who, what, when (before use).** "It feels risky" doesn't travel; documented reasons do.
4. **A Skill is software.** Check **source, reach (it inherits session access; audit the bundle), appropriateness**, then **enable, escalate or decline**. Internal doesn't mean vetted. Apply **least privilege** to every connector, tool and integration.
5. **Classify data before upload:** Green (safe), Yellow (review first), Red (keep out unless approved path). When unsure, go **more sensitive** and ask.
6. **Redact when the task doesn't need identifiers**, and redact completely. If the task needs them, use an approved path or keep the data out.
7. **Controls:** sandbox (review uploads), Memory (persistence), Incognito (out of history and Memory, **not** out of retention or exports), org Memory controls (Enterprise Owners/Primary Owners only). **Incognito does not make Red data safe.**
8. **Policy as habit:** apply it on routine decisions, audit usage against it, stay current. Gaps are usually drift, fixed with habits.
9. **Ethics in routine review:** watch for bias in people-facing work, disclose when unsure, reason through ambiguous cases (who, what could go wrong, fair outcome, disclosure), and escalate large or high-harm questions **with your reasoning**.
