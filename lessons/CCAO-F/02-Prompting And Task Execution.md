# Prompting and Task Execution

<span style="font-size: 1.25em;">_The same request, phrased two ways, produces two different levels of quality._</span>

Ask Claude to `"write something about our Q3 results"` and you get a generic paragraph. Specify the audience, the three results that matter, the format, and the length, and you get a draft you can almost send. The model did not get smarter between those two requests. The prompt did.

This module treats prompting as a communication discipline with learnable structure, not a knack some people have and others do not. The structure has a name in the AI Fluency Framework: Description, the competency of telling Claude precisely what you want. Description is the backbone of this module and the prompting foundation the rest of the course builds on.

## Anatomy of an Effective Prompt

<span style="font-size: 1.25em;">_A strong prompt is built from components, and most weak prompts are missing one or more of them._</span> 

Naming the components turns prompting from guesswork into a checklist you can run before sending any non-trivial request.

### The Component stack

**Five components** carry almost all the weight in a professional prompt.

1. **Role**: _Who you want Claude to be for this task_ -> a financial analyst, an editor, a policy reviewer. Role sets the vocabulary, depth and assumptions that Claude brings.
2. **Context**: _The background that Claude cannot know unless you provide it_: the audience, the situation, prior decisions, the source material. This is the component that is most often omitted!
3. **Task**: _The specific action_ stated as a clear instruction. `"Summarize"`, `"Compare"`, `"Draft"`, `"identify"`: _One primary verb_, stated unambiguously!
4. **Constraints**: The boundaries: length, tone, what to include, what to leave out, what to avoid. Constraints are how you keep the output useable without heavy editing.
5. **Output Format**: _The shape of the result_ - a table, a bulleted list, a 3-para memo, a draft email. Stating the format up-front saves an iteration.

Not every prompt needs all five. A quick question needs a task and maybe a constraint. **A client deliverable needs all five**. The skill is noticing which components a given task requires.

### Description in practice

The Description competency is the habit of making each component explicit instead of assuming Claude will infer it. Unless you connect a source through a Connector, Claude cannot see your inbox, your org chart, or last week's meeting, and even with a connector, Claude sees only what you have allowed it to access. Anything that lives only in your head or outside a connected source is a context gap, and context gaps are the single most common reason a prompt underperforms for new users.

### Diagnosing a weak prompt

Hold a disappointing prompt against the component stack and the gap usually becomes obvious. Missing context produces generic output. An ambiguous task verb produces the wrong action. Absent constraints produce output that is the wrong length or tone. The components are also a diagnostic checklist, which is why Lesson 4 returns to them when output falls short.

## A Worked example

### Weak prompt: everything left implicit

```
"Write a summary of our quarterly operations."
```

Claude produces three plausible paragraphs that could describe almost any company. No audience, no figures, no format, no sense of what matters. The output is not wrong. It is unusable, because the prompt specified almost nothing.

### Strong prompt: components made explicit

```
"You are an operations analyst (role). I am preparing a one-page update for our regional director, who cares about throughput and cost, not process detail (context and audience). Summarize the attached Q3 operations data (task), covering only the three metrics that moved more than 10 percent against target (constraint). Format as a short headline followed by three bullet points, each one sentence (output format)."
```

Same model, same data. The second prompt produces a draft the analyst can refine in two minutes instead of rebuilding from scratch. The difference is entirely in the specification.

> 📌 **The Habit to Build**
>
> BEFORE SENDING ANY PROMPT THAT MATTERS
>
> Run the five components in your head: have I given Claude the `role`, the `context` it cannot infer, an unambiguous `task`, the `constraints`, and the `format` I want back? Thirty seconds of specification routinely saves several rounds of correction.

> 🎗️ **REMEMBER - C R A F T**
>
> * `C`ontext: the background the model needs (e.g., "We are a mid-size Indian NBFC reviewing personal loan complaints")
> * `R`ole: who Claude should act as (e.g., "a senior credit risk analyst")
> * `A`ction: the Task, stated as a specific verb-led instruction ('Classify', 'Summarize' etc.)
> * `F`ormat: how the output should look (table, JSON, bulleted list)
> * `T`ype of limits (constraints): tone, length, what to avoid)

## Task Decomposition for Complex Requests

<span style="font-size: 1.25em;">_Some requests are too large to specify as a single instruction**._</span>

When a task has several distinct stages, packing it into one prompt produces shallow work on every stage. Decomposition is how you break a complex request into a sequence Claude can execute well.

**Decomposition means splitting a multi-part problem into discrete, ordered steps, then running them in sequence** rather than asking for everything at once. A vendor evaluation is a good example: it is really four tasks wearing one sentence.

### The single-prompt version that underperforms

> [!Tip]
> <small>SINGLE PROMPT</small>
>
> "Evaluate these three vendors and tell me which to pick."

Claude has to invent criteria, apply them, weigh trade-offs, and recommend, all in one pass. It will do all four shallowly and you will not see the reasoning behind the recommendation.

### The Decomposed version

![The decomposed version](images/prompt_decomposition.png)

* **Step 1 · Derive criteria**: From the requirements document, derive the evaluation criteria that matter and weigh them.
* **Step 2 · Score vendors**: Score each vendor against those criteria using the supplied materials.
* **Step 3 · Raise trade-offs**: Raise the trade-offs where vendors diverge most.
* **Step 4 · Recommend**: Recommend, with the reasoning tied back to the weighted criteria.

Each step produces a checkable intermediate result. If the criteria in Step 1 are wrong, you catch it before scoring, not after the recommendation. Decomposition also makes the work auditable, which matters when someone asks how the recommendation was reached.

#### One conversation or several

Keep sequential steps that build on each other in one conversation, so each step sees the prior results. Move to a separate conversation when a step is genuinely independent, or when the conversation has grown long enough that early context is degrading. That judgment connects directly to the context-management skills from Module 1.

### Decompose a Parallel Case

Three deliverables, one foundation: sequence the shared extraction first.

> [!Note]
> <small>SCENARIO</small>
>
> A communications manager needs to turn a dense 20-page policy change into an (1) internal announcement, (2) a FAQ for staff, and (3) a short briefing for executives. 
>
> Before reading on, decompose this into an ordered sequence of steps you would run with Claude.

#### Model decomposition

* **Step 1:** Extract the substantive changes from the policy document and what each one means in practice.
* **Step 2:** Confirm the extraction is complete and accurate before building anything on top of it.
* **Step 3:** Draft the staff announcement from the confirmed change list, tuned to a general audience.
* **Step 4:** Draft the FAQ, anticipating the questions staff will likely ask about those changes.
* **Step 5:** Draft the executive briefing, compressed down to decisions and impact.

#### Why this order

Steps 1 and 2 build a verified foundation that the three deliverables all draw on. Drafting any deliverable before the change list is confirmed risks propagating the same misreading into three documents. Sequence the shared, high-stakes extraction first; let the parallel drafts follow.

## Iterating Prompts to Improve Output

A first draft from Claude rarely lands perfectly. _The skill is not rewriting the whole prompt when output disappoints. It is reading the output to diagnose which component fell short, then fixing that one thing._

### Output deficiencies are prompt diagnostics

Each kind of disappointment points back to a specific component:

| Symptom | Likely cause | Fix |
|:--|:--|:--|
| Output is generic or off-base | The context was thin | Add the background Claude could not infer |
| Output answered the wrong question | The task verb was ambiguous | Sharpen the instruction |
| Output is the wrong length, tone, or shape | A constraint or the format was missing | Add it |
| Output is close but misses on one section | &nbsp; | Iterate on that section only; do not discard a draft that is mostly right |

### Targeted revision, not wholesale rewriting

When you rewrite the entire prompt, you lose the parts that worked and you cannot tell which change fixed the problem. _Change the one component the output told you to change, resend, and compare_. The same diagnostic discipline applies to troubleshooting any underperforming workflow, covered in depth in Module 7.

### A live iteration cycle

Watch the diagnose-and-fix loop run on one deliberately weak prompt.

> <small>ROUND 1 PROMPT</small>  
> "Write a follow-up email to the client about the delayed deliverable."
>
> <small>ROUND 1 OUTPUT</small>  
> A generic, slightly defensive three-paragraph email that does not say when the deliverable will arrive or why it slipped. **Diagnosis:** the context is thin (no reason, no new date) and there is no tone constraint.
>
> <small>ROUND 2 PROMPT</small>  
> "Write a follow-up to the client about the two-day delay on the analytics deliverable. The cause was a data-quality issue we have now fixed; new delivery is Thursday. Tone: accountable, not over-apologetic. Keep it under 120 words."
>
> <small>ROUND 2 OUTPUT</small>  
> A tight, accountable note with the cause, the new date, and a confident close. **Diagnosis:** strong; only the subject line is missing.
>
> <small>ROUND 3 PROMPT</small>  
> "Good. Add a subject line that signals resolution, not just delay."
> &nbsp;


Three rounds, each changing exactly the component the previous output exposed. No round threw away working text, and by round three the improvement was marginal, the signal to stop.

### Knowing when to stop

Iteration has converged when each additional round produces marginal change rather than improvement. At that point, further prompting yields less than a quick manual edit. Recognizing diminishing returns is part of the skill: the goal is a usable result, not a perfect prompt.

## Adapting Strategy by Task Type

_The component stack applies to every prompt, but the emphasis shifts with the task_.

Analysis, research, drafting, and brainstorming each reward a different balance of specificity and creative latitude. Using one fixed style across all four costs quality on every task it does not fit.

> **Analysis.** Want tight constraints and explicit criteria. Tell Claude what to measure, against what standard, and how to handle ambiguity. _Low creative latitude; high specification_.
>
> **Research.** Wants clear scope and source discipline. Define the question, the boundaries, and whether current sources are required. Quick currency needs can be met by turning on web search in chat, while deep multi-source investigation points to Research (available on paid plans). Ask for citations so claims are checkable.
>
> **Drafting.** Wants audience, tone, and format specified, with room for Claude to find the phrasing. Medium latitude: you control the shape, Claude fills it.
>
> **Brainstorming.** Wants loose constraints and high latitude. Over-specifying kills the divergence you are after. Give the goal and the boundaries, then ask for volume and range before you narrow.

### Strategy quick reference

| Task type | What to tighten | What to loosen |
| :-- | :-- | :-- |
| Analysis | Criteria, standards, scope | Phrasing |
| Research | Question, sources, citations | Synthesis approach |
| Drafting | Audience, tone, format | Word choice |
| Brainstorming | Goal and guardrails only | Quantity and direction |

### Four mini-demos, one per task type

> **Analysis**. "Compare these two vendor contracts on payment terms, termination rights, and liability caps. For each, state which contract is more favorable to us and why, in a three-row table." Tight criteria, defined output, no room to wander.
>
> **Research**. "Using current sources, summarize how three named competitors positioned their Q2 launches. Cite each source. Flag anything you cannot verify." Scope and citation discipline up front; Research (or web search in chat for lighter needs) supplies the currency.
>
> **Note:** citations are checkable when they come from a grounded source (web search or Research results); citations produced from training memory alone can look equally confident and should be independently verified.
>
> **Drafting**. "Draft a 150-word LinkedIn post announcing our new reporting feature, aimed at operations managers, in a confident but not salesy voice." Audience, length, and tone fixed; phrasing left open.
>
> **Brainstorming**. "Give me 20 angles for a campaign around faster month-end close. Range widely; do not self-edit yet." Goal and one guardrail only; the constraints come later, after the range exists.

The same prompt structure underlies all four, but the dial between control and latitude moves with the task. The underlying move is the same each time: decide where you need control and where you need range, then set constraints accordingly. Matching strategy to task type is what separates a competent prompter from one who gets the same mediocre output on every task.

## Repair underperforming prompt

Below is a prompt, the output it produced, and the author's actual goal. Work in three steps: find the specification gaps, match each fix to the component it repairs, then assemble the repaired prompt. The ideal answer is revealed at the end.

> <small>The weak prompt</small>
>
>"Summarize the customer feedback and tell me what to do."

> <small>The output it produced</small>
>
> A generic five-bullet list of themes ("customers want faster support," "pricing is a concern") with vague advice ("consider improving response times"). Nothing tied to the actual data, no priorities, nothing actionable.

> <small>The author's real goal</small>
>
> A product manager has 200 survey responses and needs the top three issues by frequency, each with a representative quote, ranked so she can decide what to fix this quarter.

### Solution

**Observation**: 👎

The prompt **is missing _every component_** -> Role, Context, Task (specificity), Constraints, and Output Format 

**Here is the final prompt**

```
"You are a product analyst (role). Attached are 200 customer survey responses (context). Identify the three most frequently raised issues (task), ranked by how many responses mention each, and for each issue include one representative verbatim quote and the approximate share of responses it appears in (constraints). Use code execution to count accurately rather than estimating. Format as a ranked list, most frequent first (output format)."
```

**Documented improvements** 👍

* Added role and context so the analysis is grounded in the actual responses
* Replaced the vague task with a specific, ranked, countable instruction
* Added constraints (representative quote, share of responses) that make the output actionable
* Specified code execution so the frequency counts are verified, not guessed
* Specified the output format so the result is decision-ready