# 03 · Evaluating and Validating Claude Output (Revision Notes)

## Where This Lesson Sits in the Exam

| Domain | Weight | Objectives covered here |
| :-- | :-- | :-- |
| **2 · Output Evaluation and Validation** | **21% (largest domain)** | Evaluate accuracy and completeness · Identify hallucinations, inconsistencies, bias · Apply fact-checking and validation · Decide when human review is required · Edit, adapt, refine, compare outputs for the audience · Organize information and choose output format (artifacts, inline, structured data) |

**Why it's the biggest domain: accountability.** When your name is on a deliverable, you own every claim in it, whether you wrote it or Claude did.

**The core asymmetry:** time saved is **small and visible**; the cost of an unverified error is **large and arrives later**, paid by someone whose trust you needed.

**Opening case:** a consultant pulled 5 statistics for a client market-sizing deck. 4 were sound; 1 growth rate was **fabricated** but plausible. The client's own analyst caught it in the room. Ten minutes saved cost a **credibility hit and a week of rebuilding trust**. Nothing about the figure looked wrong on screen.

**The twenty-minute rule:** Claude saves you twenty minutes drafting an analysis. One fabricated figure in it, sent to a **client or a regulator**, can cost far more than twenty minutes to undo.

### Exam Objective → Where It Is Covered

| Domain 2 objective (exam guide) | Sections in these notes |
| :-- | :-- |
| Evaluate outputs for **accuracy and completeness** | 2.1 to 2.6 |
| Identify **hallucinations, inconsistencies, and biases** | 3.1 to 3.4 |
| Apply **fact-checking and validation** techniques | 4.1 to 4.3 |
| Determine when **human review or additional verification** is required | 2.3, 5.1 to 5.5, 8 |
| **Edit, adapt, refine, and compare** outputs for the intended audience | 6.1 to 6.3 |
| **Organize and curate** information; select **output formats** (artifacts, inline, structured data) | 7.1 to 7.3 |

---

## Memory Map

```
EVALUATING & VALIDATING CLAUDE OUTPUT
│
├── TWO AI FLUENCY COMPETENCIES
│     ├── DISCERNMENT = HOW you review (evaluate vs requirements, sources, standards)
│     └── DILIGENCE   = WHY you must (decide when to verify; own the result)
│
├── DISCERNMENT PROTOCOL (same check every time)
│     ├── 3 references: REQUIREMENTS · SOURCE MATERIAL · PROFESSIONAL STANDARDS
│     ├── Stakes calibration: domain-dependent
│     │     zero-tolerance (legal, financial, compliance) → verify every claim
│     │     low-stakes internal brainstorm → lighter review
│     ├── Completeness ≠ accuracy (review both; missing items are harder to see)
│     └── 3-way triage (with documented reasoning)
│           READY TO USE · NEEDS REVISION · NEEDS HUMAN OVERRIDE
│
├── FAILURE PATTERNS
│     ├── Hallucinations
│     │     ├── Plausible-but-unsupported claim (MOST DANGEROUS)
│     │     ├── Fabricated specifics (stats, dates, names, quotes, citations)
│     │     └── Confident tone masking uncertainty
│     ├── Inconsistency: internal contradictions in long outputs → consistency pass
│     ├── Bias: confirmation bias when prompt implies preferred answer
│     ├── Completeness failure: misses the hardest / most important file
│     └── Capability hallucination: "I've emailed / saved it" → unverified
│
├── FACT-CHECKING & GROUNDING (build into the prompt)
│     ├── Prompt for verifiability
│     │     ├── Permit "I don't know"
│     │     ├── Restrict to provided sources ("Not covered by this document")
│     │     └── Require auditable citations (section + clause)
│     └── Grounding techniques
│           ├── Quote first, then analyze
│           ├── Best-of-N: agree → confidence up; diverge → soft spot
│           └── Validate vs AUTHORITATIVE source (not a 2nd Claude answer)
│                 Claude for Excel → cell-level citations
│
├── DILIGENCE: 4 RISK THRESHOLDS
│     STAKES · REVERSIBILITY · AUDIENCE · REGULATORY EXPOSURE
│     Do-not-ship-without-review list (decided in advance):
│       client deliverables · audit-critical/financially material calcs ·
│       regulated/confidential/sensitive data · public or legal comms
│     Iteration vs escalation: flat improvement curve → human expert
│     Accountability never transfers to the tool
│
├── EDITING FOR AUDIENCE ("Claude drafts; you deliver")
│     ├── 3 passes: CLARITY · TONE · FORMATTING
│     ├── Exec = decision + impact first · Team = detail + method + action
│     │   External = control disclosure + framing · facts stay the same
│     └── Compare several drafts (runs or models) → edit the strongest
│
└── OUTPUT FORMAT = RELIABILITY DECISION
      ├── Inline ...... act on within chat
      ├── Artifact .... documents, code; editable, reusable deliverable
      ├── Structured .. tables/schemas for tools or readers
      ├── Code exec ... numbers that must be right; computed + traceable
      │                 (code can still have a bug → read, verify, re-run)
      └── Curate inputs: DE-DUPLICATE · LABEL & STRUCTURE · PRUNE irrelevant

  ROUTINE: stakes → 3 references → completeness → signatures → verify →
           4 thresholds → verdict + reason → edit for audience
```

---

## 1. Discernment and Diligence

| Competency (AI Fluency Framework) | Meaning | Short form |
| :-- | :-- | :-- |
| **Discernment** | Critically evaluating output against **requirements, sources, and standards** | **How** you review |
| **Diligence** | Deciding **when verification is required** and **taking responsibility** for the result | **Why** you must |

You must be able to: evaluate systematically, recognise failure patterns, build verification into prompts, know thresholds for mandatory human review, and choose the format that matches the reliability needed.

---

## 2. Discernment: Accuracy, Completeness, Fitness

**Evaluation is not a feeling** about whether output looks good. It is a check against **three fixed references**, run **the same way every time** so quality doesn't depend on how rushed you are.

### 2.1 The Three Evaluation References

| Reference | Question | How to check |
| :-- | :-- | :-- |
| **Requirements** | Does it reflect what I asked for? | Re-read your request; confirm **each part** is addressed, not just the easy parts |
| **Source material** | Does it match the documents I supplied? | **Trace specific claims back to the source**; don't trust that Claude read carefully |
| **Professional standards** | Would this pass in my field? | Watch for a **number without units**, a **recommendation without reasoning**, a **citation you can't locate**. These fail even when fluent |

### 2.2 Stakes Calibration
- Review depth depends on stakes, and stakes are **domain-dependent, not universal**.
- **Zero-tolerance work** (legal analysis, financial figures, compliance reporting): **accuracy outranks speed entirely; verify every claim**.
- **Low-stakes internal brainstorming:** a **lighter review** is fine.
- Risk = applying the **same casual review to both**.
- **Decide the stakes first, then the depth of review.**

### 2.3 The Three-Way Triage (always with documented reasoning)

| Verdict | When |
| :-- | :-- |
| **Ready to use** | Meets requirements, matches sources, clears professional standards. **Ship it.** |
| **Needs revision** | Close, but a **specific gap** remains. **Note the gap and iterate.** |
| **Needs human override** | The **stakes, errors, or uncertainty** mean it shouldn't go out on Claude's draft alone. **Escalate to a person.** |

### 2.4 Completeness Is a Separate Review
- **Accuracy:** is what's present correct?
- **Completeness:** is anything **missing**?
- They **fail independently**. An output can be **fully accurate yet omit the one decisive factor**.
- **Missing items are harder to spot** than wrong ones, because nothing on screen draws your eye.

### 2.5 Protocol Applied: Three Outputs, Three Verdicts

- The protocol is **most useful on outputs that are not obviously good or bad**. Obvious failures catch themselves; the borderline ones are where a fixed check earns its keep.

| Output | What the check found | Verdict | Action |
| :-- | :-- | :-- | :-- |
| **Competitor-pricing summary** from uploaded PDFs | Requirements met, but **source check fails**: "$40/user" vs PDF's "$40/user, **minimum 10 seats**". Omission changes the comparison | **Needs revision** | **Source-restricted re-prompt**, not a rewrite |
| **Internal process recommendation** (3 ways to cut invoice-processing time) | Requirements met, no sources to check, standards cleared, **low stakes** (discussion starter) | **Ready to use** | **Over-verifying wastes the time the tool saved** |
| **Compliance-gap analysis** (policy vs regulation) | Looks complete, but **regulation was not uploaded**; Claude used **training recall of a rule that may have changed**; **regulatory stakes** | **Needs human override** | A useful **prompt for a compliance expert**, **not a substitute** for one |

**Lesson:** the verdict never depends on **how polished** the output looks; it depends on what the **three references and the stakes** return.

### 2.6 Sample Triage Exercise (model answers)

| Output | Verdict | Reason |
| :-- | :-- | :-- |
| **A.** Internal brainstorm of campaign ideas, labelled as a starting point; a few generic entries among strong ones | **Ready to use (with light editing)** | Low stakes, internal, labelled as a draft. Trim weak entries and proceed |
| **B.** Financial summary whose **total doesn't match the sum of line items** | **Needs revision** | **Internal contradiction**. **Recompute with code execution** and confirm before use |
| **C.** Market overview citing **three statistics with no checkable source** | **Needs revision** | Unsourced stats are **unverified claims**. Require **auditable citations** or **validate against authoritative sources** |
| **D.** Draft **regulatory filing** summary, accurate on spot-checked points, **for submission to a regulator** | **Needs human override** | **High stakes, irreversible, regulatory audience.** Mandatory expert review **however clean it looks** |

Note: in D, spot-checks passing does **not** lower the bar.

**Reasoning watch-outs for this exercise (the exam marks the reason, not just the label)**
- **Output B:** the core problem is an **internal contradiction** (total ≠ sum of lines). "Code execution wasn't used" is the fix, not the diagnosis. State both: *contradiction found → recompute with code execution → confirm*.
- **Output C:** the fix for unsourced statistics is **auditable citations or validation against authoritative sources**. Adding more context to the prompt does not make a statistic checkable.
- **Output A:** "ready to use" still means **light editing** (trim weak entries). Ready ≠ untouched.

---

## 3. Hallucinations, Inconsistencies, and Bias

**Plausible ≠ verified.** Claude is fluent whether right or wrong, so **tone and confidence can't flag errors**. Learn the **signatures** so you don't have to read every line with equal suspicion.

### 3.1 Hallucination Patterns

| Pattern | Description | Key point |
| :-- | :-- | :-- |
| **Plausible-but-unsupported claim** | Sounds reasonable, fits the topic, **no basis in source or fact** | **Most dangerous**: nothing looks wrong |
| **Fabricated specifics** | Invented **statistics, dates, names, quotations, citations** | **Specificity reads as authority**, so they persuade |
| **Confident tone masking uncertainty** | Claude **rarely hedges in proportion** to its real certainty | A guess and a grounded fact sound **equally assured** |

### 3.2 Inconsistencies and Bias

| Pattern | Description | Defence |
| :-- | :-- | :-- |
| **Internal contradictions** | Early claim conflicts with a later one in a **long** output | Run a **consistency pass** over the whole document, not just paragraph by paragraph |
| **Confirmation bias in framing** | If your prompt **implies a preferred answer**, Claude may lean toward it | Be wary when output **agrees with you too readily** on a question that should be open |

### 3.3 Two Special Failures

**Completeness failure (field pattern)**
- Asked to compare a batch of documents and find differences. Output listed several and **read as thorough**.
- It **missed differences in the single most important file**.
- Completeness failures **concentrate where attention is lowest**. A confident summary of the easy files can **mask silence on the hard one**.

**Capability hallucination**
- Claude **claims an action it can't take**: "I've emailed that to your team", "I've saved the file".
- In claude.ai, Claude works with the **conversation, connected tools, and uploaded files**. It **does not perform external actions it wasn't given a tool for**.
- **Treat any claimed external action as unverified until you confirm it happened.**

### 3.4 Failure-Pattern Gallery

| Example | The tell |
| :-- | :-- |
| "Approximately **63%** of mid-market SaaS firms adopted AI tools in 2025, up from **41%** in 2024." No source. | **The precision is the tell.** Real figures this specific come with a citation; an uncited 63% is a **number-shaped guess** |
| "Is this clause enforceable in our state?" → confident four-sentence "yes" | Enforceability is **jurisdiction-specific and date-sensitive**; it should hedge and doesn't. **Assurance is not evidence** |
| 10-page analysis: page 2 says market "**~$2 billion**", page 8 projects on "**$2.6 billion**" | Each reads fine alone; only visible if you **hold the whole document in view** → **consistency pass** |

**How to read the gallery:** none of these looks broken. Fluent generation passes a **casual read** by nature. You catch failures by **knowing the signatures and checking against sources**, not by waiting for something to look wrong.

---

## 4. Fact-Checking and Grounding Techniques

**The strongest verification is built into the prompt, before the output exists.** These habits cut hallucinations **at the source** and make what remains **easier to audit**.

### 4.1 Prompt for Verifiability

| Technique | Why | Verbatim prompt |
| :-- | :-- | :-- |
| **Permit "I don't know"** | Without permission, a model **under pressure to answer** is more likely to **invent** | "If the answer is not supported by the documents I provided, say so explicitly rather than estimating. It is acceptable to answer 'the provided materials do not cover this.'" |
| **Restrict to provided sources** | Turns **open-ended generation into bounded retrieval**; flags gaps | "Answer using only the attached contract. Do not use general knowledge. For anything the contract does not address, list it under 'Not covered by this document.'" |
| **Require auditable citations** | **A citation you can't trace is not a citation** | "For every claim, cite the section and clause number it comes from, in parentheses, so I can verify it against the source." |

### 4.2 Grounding Techniques

| Technique | How it works |
| :-- | :-- |
| **Quote first, then analyze** | For long documents, extract the **supporting quotes before conclusions**. Makes **reasoning and errors visible**. Prompt: "Before you analyze, extract the exact sentences from the document that bear on my question. Then base your analysis only on those quotes." |
| **Best-of-N comparison** | **Re-run the same request and compare.** Where runs **agree, confidence rises**; where they **diverge, you've found soft spots** needing a human look |
| **Validate against authoritative sources** | For claims that matter, check a **trusted external reference**, **not a second Claude response**. In-product aid: **Claude for Excel** gives **cell-level citations** tying figures back to inputs |

### 4.3 Verification Checklist (before relying on any output)
1. Did I **allow uncertainty**?
2. Did I **restrict to sources** where appropriate?
3. Did I **require citations I can audit**?
4. Did I **check high-stakes claims against something authoritative**?

Building these into the prompt is **cheaper than rebuilding trust** afterwards.

---

## 5. Diligence: When Human Review Is Non-Negotiable

Some outputs must **never go out as a Claude draft alone**, however good they look. Know the thresholds **in advance**, so escalation is decided **by policy**, not in the moment after something went wrong.

### 5.1 Four Risk Thresholds (memorise)

| Threshold | Question | Rule |
| :-- | :-- | :-- |
| **Stakes** | What's the cost if wrong? | High-cost errors need human review **regardless of how confident** the output looks |
| **Reversibility** | Can it be undone? | **Irreversible** steps (sent client deliverable, filed report) clear a **higher bar** than a revisable draft |
| **Audience** | Who sees it? | **External, executive, regulatory** audiences need more review than internal drafts |
| **Regulatory exposure** | Does a rule, contract, or law govern it? | Regulated content carries obligations that **AI assistance does not remove** |

### 5.2 Do-Not-Ship-Without-Review List (fixed, decided in advance)
- **Final client deliverables**
- **Audit-critical or financially material calculations**
- Anything with **regulated, confidential, or highly sensitive data**
- **Public or legal communications** where a misstatement has lasting consequences

### 5.3 Iteration vs Escalation
- Productive iteration **improves output each round**.
- When rounds **stop improving** → diminishing returns → the move is **a human expert, not another prompt**.
- **More prompting cannot manufacture judgment the situation requires.**

### 5.4 Owning the Output
- **Accountability does not transfer to the tool.**
- Work made with Claude is **your work** when you ship it; the professional standard is the **same as if unaided**.

### 5.5 Three Escalation Scenarios

| Scenario | Thresholds | Decision |
| :-- | :-- | :-- |
| **The fast "yes"**: internal meeting agenda | Low stakes, reversible, internal, no regulation | **Ship, no escalation** |
| **The deceptive "looks fine"**: board-deck financial summary that reads cleanly | High stakes, executive audience, partly irreversible once presented (**trips 3 thresholds**) | **Human reviewer + recompute figures with code execution**. Clean look is irrelevant |
| **The slow creep**: client proposal iterated 5 times; rounds 3–5 changed almost nothing | Diminishing returns + high-stakes external deliverable | **Stop prompting; escalate to a colleague for a fresh read**. Signal is the **flat improvement curve**, not a visible error |

---

## 6. Editing and Adapting Output for Your Audience

**"Claude drafts; you deliver."** The editing pass is where **your professional standards and audience knowledge** are applied. **An accurate draft is still not finished.**

### 6.1 Three Editing Passes

| Pass | What you do |
| :-- | :-- |
| **Clarity** | Cut hedging, tighten loose sentences, remove anything not earning its place. Claude tends to **thoroughness**; editing tends to **precision** |
| **Tone** | Match **register** to relationship and occasion: peer vs client vs regulator |
| **Formatting** | Shape for how it's read: **scannable for executives**, **detailed for a working team**, **clean for external recipients** |

### 6.2 Audience Calibration (one analysis, several deliverables)

| Audience | Approach |
| :-- | :-- |
| **Executive summary** | Leads with **the decision and the impact** |
| **Working team** | Keeps **detail and method** (and assigns action) |
| **External communication** | **Controls what is disclosed** and **how it's framed** |

**Facts stay the same; selection, depth, and tone change.**

**Worked transformation (Q3 processing time +18%):**
- **Raw:** one long hedged sentence ("may be attributable to… it is recommended that the team consider whether…"). Serves **neither** audience.
- **Executive:** "Q3 processing time rose 18 percent, driven by volume plus onboarding three new hires. Recommend standardized onboarding docs to limit the effect next time." → **number + decision first; method stripped**.
- **Working team:** "Processing time was up ~18% in Q3. Two drivers: higher volume and three new staff still onboarding. Action: draft onboarding documentation… (owner and timeline to confirm in standup)." → **keeps detail, adds operational next step**.

### 6.3 Compare Outputs Before You Edit
- When quality matters, **generate more than one draft** (**across runs or across models**) and **pick the strongest base**.
- **Comparing candidates is cheaper than rescuing a weak draft.**
- It also surfaces **framing you might not have prompted for**.

---

## 7. Choosing Output Formats

**Output format is a reliability decision, not just presentation.** Choose by purpose and, above all, by **how much the numbers must be trusted**.

### 7.1 Format by Purpose

| Format | Use for |
| :-- | :-- |
| **Inline** | Conversational replies you **act on within the chat**; quick, contextual, not standalone |
| **Artifacts** | **Documents and code**: separate, editable block you **refine and reuse**; home for a **deliverable** |
| **Structured formats** | **Data**: tables and defined schemas that **downstream tools or readers consume directly** |
| **Code execution** | **Numbers that must be right**: computed, checkable results, plus charts and processed files |

### 7.2 Code Execution: The Verified-Output Path
- **Have Claude compute numbers, not write them.**
- Prose generation → a **plausible-looking figure** ("a guess in the shape of an answer").
- Code execution → **runs the calculation**, returns a **computed, traceable** result.
- **Caveat (exam trap):** determinism attaches to the **executed computation**, but **Claude writes the code, so the logic can still have a bug**. The guarantee is that you can **read, verify, and re-run** it, **not that it's automatically correct**.

**Same task, two paths (Q3 revenue + top 3 accounts from a spreadsheet):**

| Path | Output | Trust |
| :-- | :-- | :-- |
| **Prose** | "About **$4.7 million**; largest accounts Northwind, Contoso, Globex" | Fluent, fast, **unverifiable**. Model can't reliably add a column; a wrong total **propagates into every downstream slide** |
| **Code-executed** | **$4,712,380** computed sum, top 3 **ranked by real totals**, bar chart | **Traceable to the rows**. When a figure feeds a decision, **the only path that earns trust** |

- Prose isn't "lazy"; it's a different kind of output. Fine for a **low-stakes gut-check**; anything **reported** → code execution.

### 7.3 Curate Inputs to Shape Output
- **Organized inputs → organized outputs.** Supply clean, labelled material and **state the structure you want back**.
- **Selection rule:** pick the output modality by the **reliability the task requires**.
- Curating means **removing wrong material**, not just adding right material.

| Technique | Why |
| :-- | :-- |
| **De-duplicate sources** | Claude isn't reconciling three near-identical copies |
| **Label and structure inputs** | Each input's role is explicit ("this is the approved policy; these are the draft responses") |
| **Prune irrelevant material** | **Noise in the input becomes noise in the output** |

**Clean, well-labelled, minimal inputs** beat a large undifferentiated pile.

---

## 8. Putting It Together: A Review Decision Flow

This combines Discernment (Section 2) and Diligence (Section 5) into one routine.

```
1. SET STAKES FIRST ........ zero-tolerance (legal, financial, compliance) or low-stakes internal?
2. CHECK 3 REFERENCES ...... requirements (every part) · sources (trace claims) · professional standards
3. CHECK COMPLETENESS ...... what's missing? look hardest at the most important / hardest input
4. SCAN FOR SIGNATURES ..... uncited specifics · confident legal/regulatory claims · contradictions
                             (consistency pass) · too-ready agreement · claimed external actions
5. VERIFY WHAT MATTERS ..... sources / citations / code execution for numbers / authoritative check
6. APPLY 4 THRESHOLDS ...... stakes · reversibility · audience · regulatory exposure
                             + is it on the do-not-ship list?
7. VERDICT + REASON ........ READY TO USE / NEEDS REVISION / NEEDS HUMAN OVERRIDE
8. IF ITERATING ............ change one thing per round; flat curve → escalate to a human
9. EDIT FOR AUDIENCE ....... clarity · tone · formatting
```

**Quick verdict guide**

| If you see… | Verdict usually is… |
| :-- | :-- |
| Low stakes, internal, meets requirements, nothing to source-check | **Ready to use** (light edit if needed) |
| A specific, fixable gap: missed source detail, contradiction, unsourced stat, wrong total | **Needs revision** (note the gap, targeted re-prompt or recompute) |
| High stakes + regulatory/legal/external/irreversible, or missing authoritative source, or iteration has flat-lined | **Needs human override** |

---

## 9. Links From Lessons 01 and 02 That Are Tested Under This Domain

| Earlier point | How it shows up in Domain 2 |
| :-- | :-- |
| **Responses vary** (L01) | Plan for variation; Best-of-N uses it to find soft spots |
| **Confident tone ≠ accuracy** (L01) | Basis of the "confident tone masking uncertainty" pattern |
| **Training cutoff** (L01) | Compliance-gap case: Claude recalled a rule that may have changed |
| **Skills still vary** (L01) | Review stays in even for configured workflows |
| **Artifacts vs inline** (L01) | Output format choice in Section 7 |
| **Code Execution = verified computation** (L01) | Code-executed path for numbers |
| **Citations from training memory need checking** (L02) | Auditable citations; validate against authoritative sources |
| **Code execution for counts** (L02 feedback case) | Numbers that must be right are computed, not written |
| **Iteration converges / diminishing returns** (L02) | Here, a flat curve on high-stakes work means **escalate**, not just "edit manually" |

---

## 10. Common Exam Traps

1. **"It looks clean / polished / confident, so it's fine."** Never. Polish and tone are not evidence.
2. **"Ask Claude to rate its own confidence."** Self-reported confidence is not a reliable accuracy signal.
3. **"Ask Claude again / ask another model" as validation of a high-stakes claim.** Use an **authoritative external source**. (Re-running is Best-of-N: it finds soft spots, it doesn't prove facts.)
4. **"Code execution = guaranteed correct."** It's traceable and re-runnable; the code can still have a bug.
5. **"Spot-checks passed, so the regulatory filing can go."** Regulatory + irreversible + high stakes = human override regardless.
6. **"Verify everything to the maximum, always."** Over-verifying low-stakes internal work wastes the time saved. Calibrate to stakes.
7. **"Accurate means complete."** They fail independently.
8. **"Keep prompting until it's right."** When rounds stop improving high-stakes work, escalate to a person.
9. **"Claude said it sent / saved it."** Capability hallucination until you confirm.
10. **"Rewording or reformatting fixes it."** Format changes don't fix correctness (except choosing code execution for numbers, which changes how the number is produced).
11. **"Upload everything for maximum context."** Curate: de-duplicate, label, prune.
12. **"The tool shares responsibility."** Accountability does not transfer to the tool.

**Best-of-N vs comparing drafts (easy to confuse)**

| | Best-of-N comparison (Section 4.2) | Comparing outputs before editing (Section 6.3) |
| :-- | :-- | :-- |
| Purpose | **Verification**: find where runs disagree | **Quality**: pick the strongest base to edit |
| Runs across | Same request, re-run | Runs **or models** |
| Outcome | Agreement raises confidence; divergence = soft spot for human look | Edit the best candidate; may surface new framing |

---

## Most Likely Questions

60 questions in two sets. Set 1 covers every section; Set 2 goes deeper on calibration, thresholds, the triage exercise and traps.

### Set 1: Core Questions (Q1 to Q30)

**Q1.** An associate asks Claude to summarize a new regulation. The summary cites a specific subsection number confidently. Before sending it to the compliance team, what should they do?
- A. Send it; Claude was confident.
- B. Verify the cited subsection against the official regulation text.
- C. Ask Claude to rate its confidence and send if high.
- D. Reword it to sound more formal.

**Answer: B**
**Why:** Fabricated specifics like citation numbers are a hallucination signature. Validate against an authoritative source, especially for a compliance audience. Self-reported confidence (A, C) is not reliable evidence. Rewording (D) doesn't fix correctness.

---

**Q2.** What are the three references in the discernment protocol? (Select 3)
- A. The requirements you set
- B. The source material
- C. The professional standards of your field
- D. How polished the output looks
- E. Claude's stated confidence

**Answer: A, B, C**
**Why:** Evaluation is a check against requirements, sources and professional standards. Polish (D) and confidence (E) are explicitly not signals of quality.

---

**Q3.** Which AI Fluency competency is about deciding when verification is required and taking responsibility for the result?
- A. Description
- B. Discernment
- C. Diligence
- D. Decomposition

**Answer: C**
**Why:** Diligence is why you must verify and owning the result. Discernment is how you review (evaluating against references). Description is the prompting competency from Lesson 02. Decomposition (D) is the Lesson 02 technique for splitting complex tasks.

---

**Q4.** Claude summarizes three competitors' pricing from uploaded PDFs. One price reads "$40/user" but the PDF says "$40/user, minimum 10 seats." What is the verdict and fix?
- A. Ready to use; the price is correct.
- B. Needs revision; use a source-restricted re-prompt.
- C. Needs human override; escalate to legal.
- D. Needs revision; rewrite the whole prompt.

**Answer: B**
**Why:** Requirements were met but the source check failed, and the omission changes the comparison. Note the gap and iterate with a source-restricted re-prompt, not a full rewrite (D). It's not a high-stakes escalation case (C). A ignores a completeness gap that changes the meaning.

---

**Q5.** Claude gives three sensible options to reduce internal invoice-processing time, as a discussion starter. No sources were involved. What is the most appropriate verdict?
- A. Ready to use
- B. Needs revision
- C. Needs human override
- D. Verify every sentence against external sources first

**Answer: A**
**Why:** Requirements met, no sources to check, standards cleared, low stakes. Over-verifying (D) wastes the time the tool saved. Stakes calibration means lighter review for low-stakes internal work.

---

**Q6.** Claude compares your data-handling policy against a regulation and confidently flags four gaps. The regulation itself was not uploaded. What is the verdict?
- A. Ready to use, since four gaps were found.
- B. Needs revision; ask Claude to find more gaps.
- C. Needs human override; Claude relied on training recall of a rule that may have changed, and the stakes are regulatory.
- D. Ready to use if Claude says it's confident.

**Answer: C**
**Why:** Without the source, Claude worked from memory of a possibly outdated rule, and regulatory stakes are high. The output is a useful prompt for a compliance expert, not a substitute for one.

---

**Q7.** Which statement about accuracy and completeness is correct?
- A. An accurate output is always complete.
- B. They fail independently; an accurate output can still omit the one decisive factor.
- C. Completeness is only relevant for legal documents.
- D. Missing items are easier to spot than wrong ones.

**Answer: B**
**Why:** Accuracy asks whether what's present is correct; completeness asks whether anything is missing. Missing items are harder to spot, because nothing on screen draws your eye (D is reversed).

---

**Q8.** Which hallucination pattern is described as the most dangerous?
- A. Fabricated citations
- B. Plausible-but-unsupported claims
- C. Internal contradictions
- D. Capability hallucinations

**Answer: B**
**Why:** A plausible-but-unsupported claim sounds reasonable and fits the topic, so nothing about it looks wrong. The others are real failures but are not labelled "most dangerous".

---

**Q9.** Claude states: "Approximately 63 percent of mid-market SaaS firms adopted AI tools in 2025, up from 41 percent in 2024." No source is given. What is the key warning sign?
- A. The trend direction
- B. The precision of the figures with no citation
- C. The use of the word "approximately"
- D. The topic is too recent

**Answer: B**
**Why:** "The precision is the tell." Real figures this specific come with a citation; an uncited 63% is a number-shaped guess. The trend (A) is plausible, which is what makes it persuasive.

---

**Q10.** After a session, Claude says "I've emailed the summary to your team." No email tool or connector was set up. How should you treat this?
- A. Trust it; Claude can send emails from claude.ai.
- B. As a capability hallucination; treat it as unverified until you confirm it happened.
- C. As a confirmation bias problem.
- D. Ask Claude to resend it.

**Answer: B**
**Why:** Claude can claim actions it can't take. In claude.ai it works with the conversation, connected tools and uploaded files only. Any claimed external action is unverified until confirmed.

---

**Q11.** A manager asks: "Our new pricing strategy is clearly better than the old one, right? Explain why." Claude agrees enthusiastically. What risk should you watch for?
- A. Capability hallucination
- B. Confirmation bias in framing
- C. Context window limit
- D. Internal contradiction

**Answer: B**
**Why:** When a prompt implies a preferred answer, Claude may lean toward it. Watch for output that agrees too readily on a question that should be open.

---

**Q12.** A ten-page market analysis says the market is "roughly $2 billion" on page 2 and builds a projection on "$2.6 billion" on page 8. Which review step would catch this?
- A. A paragraph-by-paragraph read
- B. A consistency pass across the whole document
- C. Asking Claude to sound more confident
- D. Changing the output format to inline

**Answer: B**
**Why:** Internal contradictions hide in long outputs because each part reads fine alone. They only show when you hold the whole document in view.

---

**Q13.** Claude compares 15 contracts and lists differences thoroughly, but misses changes in the single most important contract. What failure type is this?
- A. Fabricated specific
- B. Completeness failure
- C. Capability hallucination
- D. Confirmation bias

**Answer: B**
**Why:** Completeness failures concentrate where attention is lowest. A confident summary of the easy files can mask silence on the hard one.

---

**Q14.** Which prompt techniques reduce hallucinations at the source? (Select 3)
- A. Explicitly permit "I don't know"
- B. Restrict answers to the provided sources and list what isn't covered
- C. Require citations with section and clause numbers
- D. Ask Claude to sound authoritative

**Answer: A, B, C**
**Why:** These are the three "prompt for verifiability" techniques. Permission to not know reduces invention under pressure. Source restriction turns generation into bounded retrieval. Auditable citations make claims traceable. D increases the risk of confident errors.

---

**Q15.** Why does permitting "I don't know" help?
- A. It makes responses shorter.
- B. Without it, a model under pressure to answer is more likely to fill gaps with invented content.
- C. It switches Claude to a more capable model.
- D. It turns on web search.

**Answer: B**
**Why:** Giving explicit permission to admit uncertainty reduces the pressure to fabricate. A, C and D are not effects of this instruction.

---

**Q16.** You run the same analysis prompt three times. Two conclusions agree; one figure differs across all three runs. What does this tell you?
- A. All three runs are wrong.
- B. Agreement raises confidence; the diverging figure is a soft spot needing a human look.
- C. Use the most common answer and ship it.
- D. The model is broken.

**Answer: B**
**Why:** This is Best-of-N comparison. Where runs agree, confidence rises; where they diverge, you've found the spots that need human review. C stops short of checking the soft spot.

---

**Q17.** To validate a high-stakes claim, which is the best check?
- A. Ask Claude a second time.
- B. Ask a different Claude model the same question.
- C. Check against a trusted, authoritative external reference.
- D. Check whether the claim is written confidently.

**Answer: C**
**Why:** Validate against an authoritative source rather than a second Claude response (A, B). Confidence (D) is not evidence.

---

**Q18.** Which are the four risk thresholds for deciding on human review? (Select 4)
- A. Stakes
- B. Reversibility
- C. Audience
- D. Regulatory exposure
- E. Length of the output

**Answer: A, B, C, D**
**Why:** These four thresholds decide when human review is non-negotiable. Length (E) is not a threshold.

---

**Q19.** Which items belong on the do-not-ship-without-review list? (Select 3)
- A. Final client deliverables
- B. Audit-critical or financially material calculations
- C. Public or legal communications with lasting consequences
- D. An internal meeting agenda

**Answer: A, B, C**
**Why:** The fixed list is client deliverables, audit-critical or financially material calculations, regulated/confidential/sensitive data, and public or legal communications. An internal agenda (D) is the "fast yes" case.

---

**Q20.** A board-deck financial summary from Claude reads cleanly. What should happen?
- A. Ship it; it reads cleanly.
- B. Send to a human reviewer and recompute the figures with code execution.
- C. Ask Claude to double-check its own numbers in prose.
- D. Convert it to an Artifact and ship.

**Answer: B**
**Why:** High stakes, executive audience and partial irreversibility trip three thresholds. The clean appearance is irrelevant. C relies on prose arithmetic. D changes the format, not the reliability.

---

**Q21.** You've iterated a client proposal five times. Rounds 3 to 5 changed almost nothing. What is the right move?
- A. Keep iterating with stronger wording.
- B. Switch to Haiku for speed.
- C. Stop prompting and escalate to a colleague for a fresh read.
- D. Ship it, since iteration has converged.

**Answer: C**
**Why:** Flat improvement plus a high-stakes external deliverable signals escalation. More prompting can't manufacture the judgment the situation needs. D ignores the high-stakes external audience.

---

**Q22.** Who is accountable for a client report drafted with Claude's help?
- A. Anthropic
- B. Claude
- C. The professional who ships it, to the same standard as if unaided
- D. Shared equally between the user and Claude

**Answer: C**
**Why:** Accountability does not transfer to the tool. Work made with Claude is your work when you ship it.

---

**Q23.** One analysis must become an executive summary and a working-team update. What changes between them? (Select 2)
- A. The underlying facts and figures
- B. Selection and depth of detail
- C. Tone and framing
- D. Whether the numbers are verified

**Answer: B, C**
**Why:** Facts stay steady; selection, depth and tone change with the reader. Executives get decision and impact first; the team keeps method and action. Verification (D) applies to both.

---

**Q24.** Which description fits the executive version of an analysis?
- A. Keeps the full method and assigns owners and timelines
- B. Leads with the number and the decision, in as little as one sentence
- C. Controls what is disclosed to outsiders
- D. A raw draft with hedging intact

**Answer: B**
**Why:** Executives get the decision and impact first. A describes the working-team version. C describes external communications. D serves no audience.

---

**Q25.** What are the three editing passes that turn a raw draft into a deliverable?
- A. Clarity, tone, formatting
- B. Accuracy, completeness, sourcing
- C. Role, context, task
- D. Stakes, audience, reversibility

**Answer: A**
**Why:** Clarity (cut hedging, tighten), tone (match register) and formatting (shape for how it's read). B is evaluation, C is prompt components, D is risk thresholds.

---

**Q26.** When quality matters, what does the lesson recommend before editing?
- A. Commit to the first response to save time.
- B. Generate more than one draft (across runs or models) and edit the strongest.
- C. Always use the longest draft.
- D. Merge every draft into one.

**Answer: B**
**Why:** Comparing candidates is cheaper than rescuing a weak draft, and it can surface framing you didn't prompt for.

---

**Q27.** You need total Q3 revenue from an uploaded sales spreadsheet for a board slide. Which output path fits?
- A. Inline prose answer
- B. Code execution over the actual file
- C. Brainstorm several estimates
- D. Ask for a confident answer

**Answer: B**
**Why:** When numbers must be right and get reported, code execution computes a traceable result. A prose total is a guess in the shape of an answer, and a wrong total propagates into every downstream slide.

---

**Q28.** Which statement about code execution is TRUE?
- A. Code-executed results are guaranteed correct.
- B. The computation is deterministic, but Claude writes the code, so the logic can contain a bug; you can read, verify and re-run it.
- C. Code execution is only for producing charts.
- D. Code execution removes the need for human review.

**Answer: B**
**Why:** The guarantee is traceability and re-runnability, not automatic correctness. A and D overstate it. C ignores computed results and processed files.

---

**Q29.** Match the need to the format. A data table that a downstream tool will ingest should be produced as:
- A. Inline reply
- B. Structured format (table or defined schema)
- C. A brainstorm list
- D. A long narrative Artifact

**Answer: B**
**Why:** Structured formats are for data that downstream tools or readers consume directly. Inline is for acting within the chat. Artifacts are for documents and code.

---

**Q30.** Before asking Claude to compare draft customer responses against policy, you have three near-identical copies of the policy and several unrelated files. Which input-curation steps help? (Select 3)
- A. De-duplicate the policy copies.
- B. Label which file is the approved policy and which are draft responses.
- C. Prune the unrelated files.
- D. Upload everything so Claude has maximum context.

**Answer: A, B, C**
**Why:** De-duplicate, label and structure, and prune irrelevant material. Noise in the input becomes noise in the output. D is the "undifferentiated pile" the lesson warns against.

---

### Set 2: Additional Practice Questions (Q31 to Q60)

Difficulty is marked as [Easy], [Medium] or [Hard].

---

**Q31.** [Easy] What does "stakes calibration" mean?
- A. Every output gets the same depth of review.
- B. Review depth is set by the stakes, and the stakes depend on the domain.
- C. Review depth is set by how long the output is.
- D. Only legal documents need review.

**Answer: B**
**Why:** Stakes are domain-dependent, not universal. Zero-tolerance work (legal, financial, compliance) gets every claim verified. Low-stakes internal brainstorming gets a lighter review. A is the risk the lesson warns about. C and D are not the rule.

---

**Q32.** [Medium] An operations lead uses the same quick skim for internal brainstorms and for monthly figures sent to the finance controller. What is the main problem?
- A. The skim is too slow for brainstorms.
- B. The same casual review is being applied to zero-tolerance work and low-stakes work.
- C. Brainstorms should get the deepest review.
- D. Nothing; one consistent method is best.

**Answer: B**
**Why:** You decide the stakes first and then the depth of review. Financial figures are zero-tolerance, where accuracy outranks speed entirely. D confuses a consistent *protocol* (good) with consistent *depth* (bad).

---

**Q33.** [Easy] Which items fail professional standards even when they read fluently? (Select 3)
- A. A number without units
- B. A recommendation without reasoning
- C. A citation you cannot locate
- D. A bulleted list

**Answer: A, B, C**
**Why:** These are the three examples the lesson gives. Fluency doesn't save them. A bulleted list (D) is a format choice, not a standards failure.

---

**Q34.** [Medium] You asked Claude for five things in one request. It handled four well, but the fifth (the hardest) is thin. Which evaluation reference should have caught this?
- A. Source material
- B. Requirements
- C. Professional standards
- D. Stakes

**Answer: B**
**Why:** The requirements check means re-reading your own request and confirming each part is addressed, not just the easy parts. Stakes (D) set review depth; they are not one of the three references.

---

**Q35.** [Easy] What is the right way to check outputs against the source material you supplied?
- A. Trust that Claude read the documents carefully.
- B. Trace specific claims back to the source.
- C. Check whether the summary is well organized.
- D. Ask Claude whether it used the documents.

**Answer: B**
**Why:** Trace specific claims back to the source rather than trusting that Claude read carefully (A). Organization (C) and self-report (D) are not evidence.

---

**Q36.** [Medium] A reviewer looks at an output Claude produced and labels it "Needs revision" with no further note. What is missing from the triage step?
- A. Nothing; the label is enough.
- B. Documented reasoning, including the specific gap to fix.
- C. A confidence score from Claude.
- D. A second label.

**Answer: B**
**Why:** Triage sorts outputs into three states *with documented reasoning*. For "Needs revision" you note the gap and iterate. Without the gap noted, nobody knows what to fix.

---

**Q37.** [Medium] Claude drafts a promotional email that will be sent to 50,000 retail customers. Which risk thresholds does this clearly trip? (Select 3)
- A. Stakes
- B. Reversibility
- C. Audience
- D. Word count

**Answer: A, B, C**
**Why:** A mass customer email is high-cost if wrong, can't be unsent, and has an external audience. Word count (D) is not a threshold.

---

**Q38.** [Easy] Which are examples of "fabricated specifics"? (Select 4)
- A. Invented statistics
- B. Invented dates
- C. Invented quotations
- D. Invented citations
- E. Section headings

**Answer: A, B, C, D**
**Why:** Fabricated specifics are invented statistics, dates, names, quotations or citations. Headings (E) are structure, not factual claims.

---

**Q39.** [Medium] Why are fabricated specifics especially persuasive?
- A. Claude marks them in bold.
- B. Specificity reads as authority.
- C. They always appear with a citation.
- D. They are usually close to the real figure.

**Answer: B**
**Why:** Precise numbers and names look researched. That is exactly why they persuade, and why precision with no citation is the tell. C is the opposite of the warning sign.

---

**Q40.** [Medium] A user asks "Is this clause enforceable in our state?" and Claude answers "yes" in four assured sentences. Why is this a red flag?
- A. The answer is too short.
- B. Enforceability is jurisdiction-specific and date-sensitive, so it should hedge and doesn't.
- C. Claude cannot read contracts.
- D. Legal questions require Research mode.

**Answer: B**
**Why:** This is "confident tone masking uncertainty". Claude rarely hedges in proportion to its real certainty, and assurance is not evidence.

---

**Q41.** [Medium] Which prompt best turns open-ended generation into bounded retrieval?
- A. "Tell me everything you know about this contract's risks."
- B. "Answer using only the attached contract. Do not use general knowledge. List anything it doesn't address under 'Not covered by this document.'"
- C. "Be as confident as possible."
- D. "Summarize the contract in a friendly tone."

**Answer: B**
**Why:** Source restriction plus an explicit "not covered" list bounds the answer to supplied material and flags gaps. A invites general knowledge. C and D don't touch grounding.

---

**Q42.** [Medium] A credit analyst must assess a 120-page credit policy against a specific question. Which technique makes both the reasoning and any errors visible?
- A. Ask for a one-line answer.
- B. Quote first, then analyze: extract the exact sentences that bear on the question and base the analysis only on them.
- C. Ask Claude to rate its certainty.
- D. Switch to an inline response.

**Answer: B**
**Why:** Quote-first grounding for long documents shows exactly what the conclusion rests on, so a wrong quote or a leap in logic is easy to see.

---

**Q43.** [Hard] A colleague says: "I ran the same prompt three times and got the same capital-adequacy figure each time, so it's verified for the regulator." What is the best response?
- A. Agree; three identical runs prove the figure.
- B. Agreement raises confidence, but a claim that matters must be validated against an authoritative source, and a regulatory submission needs human review.
- C. Run it ten more times.
- D. Ask a different model to confirm.

**Answer: B**
**Why:** Best-of-N finds soft spots where runs diverge; agreement only raises confidence. High-stakes claims are checked against a trusted external reference, not another Claude response (D). Regulatory content also trips the review thresholds.

---

**Q44.** [Easy] Which in-product aid can tie figures back to their inputs with cell-level citations?
- A. Incognito mode
- B. Claude for Excel
- C. Memory
- D. Research mode

**Answer: B**
**Why:** The lesson names Claude for Excel as an aid for validation, producing cell-level citations.

---

**Q45.** [Medium] Which is NOT part of the verification checklist before relying on an output?
- A. Did I allow uncertainty?
- B. Did I restrict to sources where appropriate?
- C. Did I ask Claude to rate its own confidence?
- D. Did I check high-stakes claims against something authoritative?

**Answer: C**
**Why:** The checklist is: allow uncertainty, restrict to sources, require auditable citations, check high-stakes claims against an authoritative source. Self-rated confidence is not a reliable signal.

---

**Q46.** [Easy] Under the reversibility threshold, which output must clear the highest bar?
- A. An internal draft you will revise tomorrow
- B. A report filed with an authority
- C. A brainstorm list
- D. A meeting agenda

**Answer: B**
**Why:** Irreversible steps, such as a sent client deliverable or a filed report, clear a higher bar than drafts you can still revise.

---

**Q47.** [Medium] Why should risk thresholds and the do-not-ship list be decided in advance?
- A. To save typing time.
- B. So escalation is decided by policy, not in the moment after something has gone wrong.
- C. So Claude can enforce them.
- D. Because Claude needs them in Memory.

**Answer: B**
**Why:** Diligence means knowing the thresholds ahead of time, so the escalation decision doesn't depend on how rushed or confident you feel at the moment.

---

**Q48.** [Medium] In the "slow creep" scenario (client proposal iterated five times), what is the signal to escalate?
- A. A visible factual error
- B. The flat improvement curve across later rounds
- C. Claude refusing to continue
- D. A usage limit warning

**Answer: B**
**Why:** Rounds 3 to 5 changed almost nothing. Diminishing returns on a high-stakes external deliverable mean stop prompting and get a colleague's fresh read. No visible error is needed.

---

**Q49.** [Hard] After six rounds, Claude's interpretation of an ambiguous clause in a lending agreement keeps shifting slightly, and nothing is getting better. What does Diligence call for?
- A. A seventh round with a stronger role prompt.
- B. A human expert, because more prompting cannot manufacture the judgment the situation requires.
- C. Pick the most recent answer.
- D. Switch to brainstorming mode.

**Answer: B**
**Why:** When iteration stops improving the output, the right move is a human expert, not another prompt. The legal stakes reinforce that.

---

**Q50.** [Medium] A manager argues that because Claude drafted a regulated disclosure, some of the team's regulatory obligations are reduced. What is correct?
- A. True; AI assistance shares the obligation.
- B. False; regulated content carries obligations that AI assistance does not remove.
- C. True, if the output was reviewed by a second model.
- D. True, for internal disclosures only.

**Answer: B**
**Why:** Regulatory exposure is a threshold precisely because the obligations stay with you. Accountability does not transfer to the tool.

---

**Q51.** [Easy] Which action belongs to the **clarity** editing pass?
- A. Matching register to a regulator
- B. Cutting hedging and tightening loose sentences
- C. Making the document scannable for an executive
- D. Choosing a table format

**Answer: B**
**Why:** Clarity cuts hedging, tightens sentences and removes anything that doesn't earn its place. A is the tone pass. C and D are formatting.

---

**Q52.** [Medium] What is distinctive about adapting an analysis for an **external** communication?
- A. It keeps all method detail.
- B. It controls what is disclosed and how it is framed.
- C. It changes the underlying facts.
- D. It assigns owners and timelines.

**Answer: B**
**Why:** External versions control disclosure and framing. A and D describe the working-team version. Facts never change (C).

---

**Q53.** [Medium] Claude's draft is fully accurate. Why is it still "not finished"?
- A. Accurate drafts must always be rewritten.
- B. The editing pass is where your professional standards and knowledge of the audience get applied.
- C. Claude always adds errors in formatting.
- D. Only Opus drafts are finished.

**Answer: B**
**Why:** "Claude drafts; you deliver." An accurate draft still needs clarity, tone and formatting matched to its reader.

---

**Q54.** [Medium] The raw Q3 output was one long hedged sentence about an 18% rise in processing time. Why does it serve neither the executive nor the working team?
- A. It contains a wrong number.
- B. It buries the number and decision for executives and lacks a clear action and owner for the team.
- C. It is too short.
- D. It uses a table.

**Answer: B**
**Why:** Executives need the number and decision first; the team needs the drivers and an operational next step. The facts were right; the shaping was wrong.

---

**Q55.** [Hard] In the sample triage exercise, Output C was a market overview with three statistics that named no checkable source. Which reasoning matches the model answer?
- A. Ready to use, because the statistics sound plausible.
- B. Needs revision: unsourced statistics are unverified claims; require auditable citations or validate against authoritative sources.
- C. Needs revision: add more background context to the prompt.
- D. Needs human override, because all market overviews are regulated.

**Answer: B**
**Why:** The gap is verifiability, so the fix is citations or authoritative validation. More context (C) doesn't make a statistic checkable. D overstates the stakes.

---

**Q56.** [Hard] In the sample triage exercise, Output B was a financial summary whose total didn't match its line items. Which statement captures the complete model answer? (Select 2)
- A. The diagnosis is an internal contradiction between the total and the line items.
- B. The fix is to recompute with code execution and confirm before use.
- C. The verdict is "Ready to use" because the line items are present.
- D. The verdict is "Needs human override" because all figures need a regulator.

**Answer: A, B**
**Why:** The verdict is "Needs revision": the diagnosis is the contradiction, and the fix is recomputing with code execution and confirming. Naming only the fix misses the diagnosis the exam expects you to spot.

---

**Q57.** [Medium] A prose answer gives Q3 revenue as "about $4.7 million" and it goes into a board deck. What is the specific danger?
- A. The number is rounded.
- B. The model can't reliably sum a column in prose, and a wrong total propagates into every downstream slide.
- C. The board prefers charts.
- D. Prose answers can't name accounts.

**Answer: B**
**Why:** A prose total is the model's best guess at summing a column. Once reported, the error spreads. Code execution gives a computed, traceable figure.

---

**Q58.** [Medium] When is a prose (non-computed) number acceptable?
- A. For a board report
- B. For a low-stakes gut-check
- C. For an audit file
- D. Never

**Answer: B**
**Why:** The prose answer is not lazy, just a different kind of output. It may be fine for a quick gut-check. Anything that gets reported needs code execution. D is too absolute.

---

**Q59.** [Medium] What does "curating inputs" involve? (Select 2)
- A. Removing wrong or irrelevant material, not just adding the right material
- B. Stating the structure you want back
- C. Uploading every related file for maximum context
- D. Keeping duplicate versions so Claude can choose

**Answer: A, B**
**Why:** Organized inputs produce organized outputs. Curating includes removing material and stating the output structure. C and D create noise, and noise in the input becomes noise in the output.

---

**Q60.** [Hard] Claude prepares a credit-risk summary for a bank's board from an uploaded portfolio file. The figures were written in prose, and one paragraph cites a central bank circular from memory (it wasn't uploaded). Which actions are required? (Select 3)
- A. Recompute the figures with code execution over the uploaded file.
- B. Validate the circular citation against the authoritative text.
- C. Send to a human reviewer before it goes to the board.
- D. Ship it, since Claude used the uploaded file.

**Answer: A, B, C**
**Why:** Board audience, high stakes and partial irreversibility trip the thresholds, so it needs human review. Numbers that feed decisions must be computed, not written. A citation from training memory must be checked against the authoritative source. D ignores all three risks.

---

## Key Takeaways

1. **You own what you ship.** Accountability never transfers to Claude. Time saved is small and visible; the cost of an error is large and arrives later.
2. **Discernment (how) + Diligence (why).** Check every output against **requirements, source material, professional standards**, the same way every time, at a depth set by the **stakes**.
3. **Triage into three verdicts:** Ready to use, Needs revision, Needs human override. Polish never decides the verdict.
4. **Accuracy and completeness fail independently.** Missing items are harder to see, and they hide in the hardest or most important file.
5. **Know the failure signatures:** plausible-but-unsupported claims (most dangerous), fabricated specifics (precision is the tell), confident tone, internal contradictions (run a consistency pass), confirmation bias, capability hallucinations ("I've emailed it").
6. **Build verification into the prompt:** permit "I don't know", restrict to sources, require auditable citations, quote first, Best-of-N, and validate against **authoritative** sources, not a second Claude answer.
7. **Four thresholds: Stakes, Reversibility, Audience, Regulatory exposure.** Fixed do-not-ship list: client deliverables, material calculations, sensitive or regulated data, public or legal comms. A flat iteration curve means escalate to a human.
8. **Claude drafts; you deliver.** Edit for clarity, tone and format. Tailor to exec, team or external readers, keeping facts constant. Compare drafts before editing.
9. **Format is a reliability decision.** Inline for in-chat action, Artifacts for documents and code, structured formats for data, **code execution for numbers that must be right** (still read and verify the code). Curate inputs: de-duplicate, label, prune.
10. **Run the same routine every time:** set stakes, check the three references and completeness, scan for failure signatures, verify what matters, apply the four thresholds, give a verdict **with a reason**, then edit for the audience.
