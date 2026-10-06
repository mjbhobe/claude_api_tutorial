# Prompting and Task Execution
The same request, phrased two ways, produces two different levels of quality.

Ask Claude to "write something about our Q3 results" and you get a generic paragraph. Specify the audience, the three results that matter, the format, and the length, and you get a draft you can almost send. The model did not get smarter between those two requests. The prompt did.

This module treats prompting as a communication discipline with learnable structure, not a knack some people have and others do not. The structure has a name in the AI Fluency Framework: Description, the competency of telling Claude precisely what you want. Description is the backbone of this module and the prompting foundation the rest of the course builds on.

## Anatomy of an Effective Prompt

A strong prompt is built from components, and most weak prompts are missing one or more of them. Naming the components turns prompting from guesswork into a checklist you can run before sending any non-trivial request.

### The component stack

Five components carry almost all the weight in a professional prompt.

1. **Role**: Who you want Claude to be for this task: a financial analyst, an editor, a policy reviewer. Role sets the vocabulary, depth and assumptions that Claude brings.
2. **Context**: The background that Claude cannot know unless you provide it: the audience, the situation, prior decisions, the source material. This is the component that is most often omitted!
3. **Task**: The specific action stated as a clear instruction. `"Summarize"`, `"Compare"`, `"Draft"`, `"identify"`: one primary verb, stated unambiguously!
4. **Constraints**: The boundaries: length, tone, what to include, what to leave out, what to avoid. Constraints are how you keep the output useable without heavy editing.
5. **Output Format**: The shape of the result - a table, a bulleted list, a 3-para memo, a draft email. Stating the format up-front saves an iteration.

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

> **The habit to build**
>
> BEFORE SENDING ANY PROMPT THAT MATTERS
>
> Run the five components in your head: have I given Claude the role, the context it cannot infer, an unambiguous task, the constraints, and the format I want back? Thirty seconds of specification routinely saves several rounds of correction.

> **REMEMBER**
>
> **CRAFT**
> * `C`ontext: the background the model needs (e.g., "We are a mid-size Indian NBFC reviewing personal loan complaints")
> * `R`ole: who Claude should act as (e.g., "a senior credit risk analyst")
> * `A`ction: the Task, stated as a specific verb-led instruction ('Classify', 'Summarize' etc.)
> * `F`ormat: how the output should look (table, JSON, bulleted list)
> * `T`ype of limits (constraints): tone, length, what to avoid)

## Task Decomposition for Complex Requests

**Some requests are too large to specify as a single instruction**.

When a task has several distinct stages, packing it into one prompt produces shallow work on every stage. Decomposition is how you break a complex request into a sequence Claude can execute well.

Decomposition means splitting a multi-part problem into discrete, ordered steps, then running them in sequence rather than asking for everything at once. A vendor evaluation is a good example: it is really four tasks wearing one sentence.

The single-prompt version that underperforms
Single prompt
"Evaluate these three vendors and tell me which to pick."
Claude has to invent criteria, apply them, weigh trade-offs, and recommend, all in one pass. It will do all four shallowly and you will not see the reasoning behind the recommendation.

The decomposed version
1
Derive criteria
2
Score vendors
3
Raise trade-offs
4
Recommend
Step 1 · Derive criteria
From the requirements document, derive the evaluation criteria that matter and weigh them.

Each step produces a checkable intermediate result. If the criteria in Step 1 are wrong, you catch it before scoring, not after the recommendation. Decomposition also makes the work auditable, which matters when someone asks how the recommendation was reached.

One conversation or several
Keep sequential steps that build on each other in one conversation, so each step sees the prior results. Move to a separate conversation when a step is genuinely independent, or when the conversation has grown long enough that early context is degrading. That judgment connects directly to the context-management skills from Module 1.

