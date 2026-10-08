# Workflow Integration & Solution Design

<span style="font-size: 1.25em;">_There is a difference between "I use Claude" and "our workflow uses Claude."_</span>

The first is a personal productivity habit. The second is a repeatable process, run by a team, where Claude performs specific steps every time. The value compounds only when you make that shift deliberately, and the shift can go awry when teams automate the wrong steps.

> [!Note]
> <small>TWO TEAMS, SAME TOOL, DIFFERENT OUTCOMES</small>
>
> Consider two teams that adopted Claude for the same contract-review process. The first mapped the work and let Claude draft the redline while a lawyer owned every final decision; review time dropped by half and quality held. The second pointed Claude at the whole process and let it approve low-risk clauses unsupervised; within a month an approved clause created an obligation no one caught, and the team pulled the tool entirely.
>
> Same product, same process. The difference was which steps each team chose to delegate.

This module is about making that choice well. The anchoring competency from the AI Fluency Framework is Delegation: deciding, for each step, whether the work is AI-appropriate, human-retained, or collaborative. Delegation done deliberately is what turns individual wins into workflow value.

## Analyzing Requirements and Use Cases with Claude

<span style="font-size: 1.25em;">_Most real work starts from messy inputs: a long document, a thread of half-formed emails, a verbal ask. Before you can build anything, the requirements have to be extracted, structured, and pressure-tested._</span>

Claude is a strong partner for exactly that translation, turning raw inputs into testable requirements others can act on. Claude can take unstructured material and return structure by pulling the requirements out of a document, organizing them, and flagging what is ambiguous or missing. Upload raw inputs and ask Claude for a structured analysis, rather than a narrative summary.

### Translating business needs into task definitions

A business need stated as `"we need better reporting"` is not actionable. Claude can help convert that business need into specific task definitions: what report, for whom, how often, drawn from what data, and in what format. Each becomes a requirement you can build against and check completion on.

### Worked example: an RFP response workflow

> [!Tip]
> <small>THE WORKFLOW</small>
>
> A proposal team responds to client RFPs. The inputs are a 40-page RFP document and a scattered email thread of internal answers. **The recurring task:** turn that into a structured list of answerable requirements.
>
> <small>THE PROMPT</small>
>
> <small>`"From the attached RFP and the email thread, extract every distinct requirement the client is asking us to address. For each, give a short label, the exact RFP section it comes from, whether our thread already has an answer, and any requirement that is ambiguous and needs clarification. Return it as a table."`</small>
>
> **The output:** A requirements table the whole team can work from: each row a requirement, traced to its RFP section, marked answered or open, with ambiguities flagged for a clarifying question to the client.

This is a Project, not a one-off Chat. Past winning proposals live in the knowledge base, the Skills carry the formatting steps, and the standing instructions hold the extraction format. No technical build is required. The standing instructions and knowledge base live in the Project's configuration; the Skills live at the account level and apply everywhere, this Project included. Module 5 covers the configuration in depth.

### Pressure-testing the requirements

Extraction is the first pass; pressure-testing is what makes the output trustworthy. Ask Claude to challenge its own list:

<small>`"Review the requirements you extracted. Which are ambiguous as written? Which could be interpreted two ways by our proposal team? Which imply a requirement the RFP states only indirectly?"`</small>

This surfaces the hidden requirements, the ones buried in a subordinate clause or implied by an evaluation criterion, that cost teams the bid when missed. **The structured list plus a pressure-test pass is a far stronger foundation than either alone**, and it is the Discernment habit from Module 3 applied at the requirements stage.

## Research, Planning & Process Optimization

<span style="font-size: 1.25em;">_Planning work usually mixes two things Claude handles differently: synthesis, where it excels, and calculation, where it must be verified._</span>

The strongest planning workflows pair Claude's synthesis with code-executed analysis, so the plan rests on numbers that were computed, not generated.

### Research and synthesis

Claude can synthesize across sources to develop a plan: gather the considerations, structure the options, and lay out the trade-offs. For current information that post-dates training, web search in chat covers quick lookups and Research supplies the deeper up-to-date inputs. The synthesis is useful, and it is where unverified claims can enter, so the verification discipline from Module 3 applies throughout.

### Code execution for verified analysis

When a plan depends on numbers, have Claude compute them. Upload the dataset and use code execution to run the calculations, produce trend charts, and process the files. A staffing plan built on a guessed utilization rate is a guess; one built on a code-executed analysis of the actual timesheet data is a plan.

### Worked example: a capacity plan

> [!Note]
> <small>THE WORKFLOW</small>
>
> An operations lead is planning headcount for next quarter. The workflow: upload the last four quarters of ticket-volume data, use code execution to compute the trend and the per-analyst throughput, then have Claude synthesize a staffing recommendation from the verified figures.
>
> <small>THE PROMPT</small>
>
> <small>`"Using code execution on the attached ticket data, calculate quarterly volume growth and average tickets resolved per analyst. Then, from those figures, recommend the headcount needed to hold our current resolution time next quarter, and show the assumptions."`</small>
>
> The recommendation is only as trustworthy as the figures under it. Because the figures came from code execution rather than prose, the plan can be defended line by line. Identifying which steps of a plan are built on a number is how you decide where AI insight impacts the answer.

### Where AI insight changes the plan

Not every step of a planning workflow benefits equally from Claude. The **synthesis steps**, where many considerations have to be weighed and structured, **are where it adds the most**. The **judgment steps**, where a person weighs risk appetite or political reality, **stay human**. A quick scan of a workflow for its synthesis-heavy steps tells you where to apply Claude and where to leave the call to a person.

For the capacity plan, Claude's leverage is in turning four quarters of data into a defensible recommendation; the decision to hire, against budget and hiring-freeze realities Claude cannot see, remains up to the operations lead.

## Solution Design, Development & Iteration

<span style="font-size: 1.25em;">_Claude is a design collaborator, not a vending machine. The value shows up in an explicit loop: ideate → prototype → gather feedback → refine._</span>

Treating it as a loop, and keeping the design context stable across iterations, is what produces a solution rather than a pile of one-off drafts.

### The iteration loop

Ideate → Prototype → Gather feedback → Refine

Ideation produces options; a prototype makes one concrete; feedback exposes what is wrong; refinement fixes it; and the loop repeats until the solution holds. Running this inside a Project keeps the context, constraints, and prior decisions stable, so each iteration builds on the last instead of restarting.

### Worked example: an internal process tool

> [!Note]
> <small>THREE ITERATIONS, NO CODE WRITTEN</small>
>
> A business analytics team needed a small internal tool to track and visualize a maintained set of metrics. Rather than commission a build, they had Claude produce it as a web artifact and iterated by asking.

<center> Build  → Filter & Totals → Color & Build </center><br/>

**Cycle 1 · Build**

"Build a simple dashboard artifact that shows these five metrics from the attached data, with a chart for each." Claude produces a working artifact.

**Cycle 2 · Filter & totals**

"Add a filter by region and a summary row at the top with the totals." The team refines by describing the change, not by coding it.

**Cycle 3 · Color & print**

"The month-over-month deltas should be color-coded, green for improvement, and the layout should print cleanly." Three cycles, no code written by the team.

### Knowing when to escalate

The artifact worked because it served a small team's internal need. When a solution becomes a system others depend on, with uptime, security, or integration requirements, it has outgrown Associate scope and belongs with Developer or Architect expertise.

That dependency is the escalation signal: the moment people rely on it as infrastructure, the build is no longer a prompt-and-iterate exercise.

## Delegation Mapping: Redesigning Workflows with Claude Inside

<span style="font-size: 1.25em;">_This is the core skill of the module. Before you redesign a workflow around Claude, map it step by step and decide, for each step, who owns it: AI, a human, or both together._</span>

The mapping is judged on three criteria, and getting it right determines whether the workflow compounds value or quietly accumulates risk.

### Three steps, three criteria

For each step in a workflow, classify it as **AI-appropriate**, **human-retained**, or **collaborative**, judged against:

* **Reversibility**: Can the step be undone if Claude gets it wrong? Reversible steps tolerate more delegation; irreversible ones demand human involvement.
* **Stakes**: What is the cost of an error at this step? High-cost steps stay human-owned or human-reviewed.
* **Accountability**: Who is answerable for the steps' outcome? Accountability does not delegate, even when the drafting does.

### Building the redesign

Once mapped, embed the right feature at each AI step: a Skill for repeatable procedure steps, code execution for data steps. Consistency from a configured Skill beats heroic prompting that depends on remembering the right wording every time. The human-retained steps become explicit review gates, not afterthoughts.

Contract review is a common first-win workflow for business teams, so it is worth mapping fully.

### Two worked maps, same criteria

**Contract review**

| Workflow step | Delegation | Why |
| :-- | :-- | :-- |
| Extract clauses from the contract | AI-appropriate | Reversible, low stakes, mechanical |
| Flag departures from the company playbook | AI-appropriate | Reversible; a Skill carries the playbook rules |
| Draft the redline and rationale | Collaborative | AI drafts, human judges each edit |
| Approve or reject each change | Human-retained | High stakes, accountability does not delegate |
| Compute financial exposure of a penalty clause | AI-appropriate (code execution) | Numeric; must be computed, not estimated
| Sign and send | Human-retained | Irreversible, external, legally binding |

**Onboarding documents**

| Workflow step | Delegation | Why |
| :-- | :-- | :-- |
| Pull new-hire details from the HRIS export | AI-appropriate (code execution) | Mechanical, reversible, must be exact |
| Draft the offer letter from the approved template | AI-appropriate | Reversible draft; a Skill carries the template |
| Personalize the welcome note | Collaborative | AI drafts, hiring manager adds the human voice |
| Confirm compensation figures match the approved req | Human-retained | High stakes, accountability does not delegate |
| Send the signed offer | Human-retained | Irreversible, legally binding |


Note that the AI does real work here, including the redline draft, not just a summary. The human owns the decisions and the irreversible steps. That split is the redesign.

### Recognizing over-delegation

It is an incorrect approach to give AI more than the risk profile justifies: letting Claude approve clauses, or send the contract, because it drafted them well. Drafting quality is not a license to delegate the decision. When the map gives an irreversible or high-accountability step to AI, that is over-delegation, and it is exactly where the second team in the introduction went wrong.

### Common mapping errors

* **Halo delegation.** A step gets handed to AI because the previous step went well. Each step is judged on its own.
* **Collapsing collaborative into automate.** `"AI drafts, human reviews"` quietly becomes `"AI drafts"` when the review gate is never actually staffed. A collaborative step with no real reviewer is an automated step.
* **Mapping the tool, as opposed to the work.** Teams sometimes map around the features they like (a Skill they built) rather than the actual workflow steps. Map the work first, then adjust the features.

## Communicating Value and Limitations to Stakeholders

Integrating Claude into a team workflow means describing it to people who did not build it: a manager, a client, a risk function.

Credibility comes from accurate claims, which means communicating the limits as clearly as the value. Overstating capability is how teams lose stakeholder trust on the first visible miss.

Describe capability accurately
State what Claude can reliably do for the use case and what it cannot, without inflation or false modesty. "Claude drafts the first pass redline, which a lawyer reviews" is accurate and credible. "Claude handles contract review" overstates and invites the question your first error will answer badly.

The same workflow, different audiences
Consider the contract-review workflow, interpreted from varied perspectives:

Legal lead
Practice executive
Client risk function
High literacy. "Claude extracts clauses, flags playbook departures, and drafts the redline. It does not approve changes, that gate stays with you. Known failure mode: it can miss obligations implied indirectly, so the playbook-departure flags are a prompt for your read, not a substitute."

This is the same workflow and the same human gate. What changes is the detail each audience needs to trust it at.

Calibrate to the audience
Match the message to the audience's AI literacy. A technical stakeholder wants the feature detail and the failure modes; an executive wants the outcome, the oversight in place, and the risk posture. The expectation you set should match the capability boundary, so no one is surprised later. This is the Description competency from Module 2 applied outward: the same precise specification of what the tool can and cannot do, now directed at stakeholders rather than at Claude.

Document the human oversight
Name the review gates that stay in place. "Every output destined for a client passes human review" is the control that makes the workflow defensible. Stakeholders trust an AI workflow more, not less, when the human checkpoints are explicit.

Good and bad messaging, side by side
Overstated	Accurate
"Our new AI system reviews contracts automatically." Sets an expectation the workflow does not meet and hides the human gate.	"Claude drafts the redline and flags playbook departures; our legal lead reviews and approves every change before anything is sent. The team's review time is down about half, with the same approval standard." Value and limits in one breath.
Phrases that quietly overstate
"Fully automated" is almost never true, and the first visible error exposes it. "Claude handles X" collapses the human gate out of the sentence. "It's basically as good as a person at Y" sets a standard that the tool will eventually miss publicly. Each replaces a defensible, bounded claim with an inflated one. The fix is the same every time: state what the tool does, then identify the human checkpoint.