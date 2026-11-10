# Production Engineering, Evals & Security

<span style="font-size:1.25em;">_You have built agents that work. This module is about proving they keep working under production traffic._</span>

It turns "it works on my machine" into a system you can defend in a review: an eval that defines what "done" means, a test and tracing layer that catches regressions before they ship, failure handling that survives a rate limit at peak, a cost and orchestration budget that holds at scale, and a security boundary that survives a regulated review.

## Evals & Judges

### Defining done before you ship: evals and a calibrated judge

Your success metric is simple: the code works correctly. The agents and tools you built in the prior modules answer correctly when you try them by hand. The gap is that "I tried it a few times and it looked right" is not a signal you can track.

The first thing production hardening needs is a way to turn that intuition into a measurable number that you can track as the prompt, the tools, or the model change. That is what an eval gives you, and the rest of this module leans on it.

Write the design document that states what's done, safe, and affordable
Before you write any production code, write down what you are going to build and how you will know it is right. A design document is that written record. It is a short file, usually a single markdown page, that states the success criteria for the features, the failures the system must survive, the cost and latency the system must stay inside, and the trust boundary the system must defend. It is the planning step that comes before implementation, and it exists so that you define what is correct instead of rationalizing whatever the model produces later.

The reason the document comes first is that every production layer in this module is based on it. The success criteria become the cases against which your eval is graded. The failures you listed become the retriable and terminal cases your error handling must cover. The cost and latency numbers become the budget you instrument against and the floor you refuse to optimize below. The trust boundary becomes the input you treat as data and the action you gate with a hook. Writing those four decisions down once, before you build, is what keeps the layers consistent with each other instead of each one solving a different problem.

A useful design document holds four decisions, each stated concretely enough that someone could check the built system against it:

1. **Success criteria** name what the feature must produce. State the output for representative cases in terms specific enough to grade, because a vague goal like "summarize the thread" cannot be checked while "a two-sentence summary that lists every action item and its owner" can. These criteria are what your eval set is built from, so writing them first is what makes the eval possible.
2. **Failure handling** names the failures the system must survive and what it does for each. List the errors production will throw, mark each one retriable or terminal, and say what the user gets when a failure cannot be recovered. Deciding this on paper is what stops the first real rate-limit response from being the moment you discover you have no error path.
3. **Cost and latency budget** names the ceiling the system must stay under and the reliability floor it cannot trade away. Set hard cost and latency budgets before architecture is determined. Write the per-request budget, the monthly cost ceiling, and the latency target, along with the minimum reliability the design must hold. Setting these numbers before you build is what lets you check the architecture against the budget before a line of code is written.
4. **Trust boundary** names which inputs are untrusted and what the system is allowed to do. Write down which content the agent reads that someone else can write, and the smallest set of actions and access the feature needs to do its job. Naming the boundary on paper is what turns least privilege into a design decision you can enforce with a hook rather than a setting you remember to add later.

If you build an agentic coding tool, this document is also what you hand in before it writes anything. Plan the work first and capture the result as a written artifact, then implement against it. A tool given clear success criteria and explicit constraints makes fewer assumptions and produces code you can check against the document you already agreed on. The rest of this module teaches each of the four decisions in turn, and the cumulative task at the end asks you to harden a system against all four at once.

### An eval is the test set that defines what a feature must do before it ships

An eval works the way a thermometer does. It does not make the patient healthier. It just gives you a number you can trust. Before you have one, "done" is a feeling. After, it is a score on a fixed set of cases.

You collect a set of input cases. For each one you write down the behavior you expect. You run the feature on every case and grade the output against that expected behavior. The collection of cases, expectations, and grades is the eval. "Done" stops being a feeling after a few manual tries and becomes a score. You write the eval before the feature because it forces you to define success before implementation begins. Otherwise, you may find yourself rationalizing whatever output the model produces later.

The pipeline is small and requires the same framework every time: load a dataset of cases, run each case through the feature, grade each result, and average the scores. A minimal version is only a few functions. The first runs the feature on one case, the second grades that output, and the third loops over the dataset and averages.

```python
def run_test_case(test_case):
    """Run one case through the feature, then grade the result."""
    output = run_prompt(test_case)
    score = grade(test_case, output)        # grading covered below
    return {"output": output, "test_case": test_case, "score": score}

def run_eval(dataset):
    """Run every case and report the average score."""
    results = [run_test_case(c) for c in dataset]
    average = sum(r["score"] for r in results) / len(results)
    print(f"Average score: {average}")
    return results
```

The score on its own is not inherently good or bad. The first attempt scoring two or three out of ten is normal. What matters is whether the number increases as you change the prompt, the tools, or the model. Change one of these at a time, so that you know which caused the improvement. The eval is the instrument that makes that change measurable instead of a matter of opinion.

### Matching the grading method to the shape of the output

The grader is the part that turns an output into a measurable signal, usually a number between one and ten. There are three ways to produce that signal, and choosing the wrong one is where eval effort gets wasted.

1. **Exact or string match** works when the output has one correct form. A classifier that must return one label, or a function that must return a known value, can be checked character by character. It is the cheapest grader and the most brittle: any acceptable paraphrase of an open-ended answer fails it. It is the wrong tool anytime the output can be phrased more than one way.
2. **Code-graded checks** work when a function can validate the output. Valid JSON, parseable Python, a number inside a range, a response that contains a required field: each of these is a check you can write in code that returns a pass or a fail. The output does not have to match a fixed string, only satisfy a rule. This method catches format and syntax failures a string match would miss, and a human would find tedious to check by hand.
3. **LLM-as-judge** works for open-ended outputs where quality matters but cannot be evaluated through pattern matching. You give a second model the output and a rubric, and it returns a score with reasoning. This is the only method that scales questions like "is this summary faithful?" or "did this answer follow the instructions?" because no code rule captures those. It is also the most expensive and the noisiest, so using it when a code check would suffice adds cost and variance for no gain.

A code grader is often just a parse attempt. If the output parses into the required format, it scores well, while if it throws an error, it scores zero. That is enough to catch a whole class of format failures cheaply.

```python
import json, ast

def validate_json(text):
    try:
        json.loads(text.strip())
        return 10          # parses as JSON
    except json.JSONDecodeError:
        return 0           # malformed, fail the case

def validate_python(text):
    try:
        ast.parse(text.strip())
        return 10
    except SyntaxError:
        return 0
```

Comparing how the same output scores under each method often makes the right choice clear. Imagine a feature that should return the three capital cities of a region as a JSON array. One run returns the array in a different order than your reference string. An exact match scores as zero, because the characters do not line up, even though the answer is correct. A code grader that parses the JSON and checks membership scores it well, because all three cities are present and the structure is valid.

Now imagine the feature should return a one-paragraph rationale for a recommendation. The code grader can confirm it is a non-empty string, which is nearly worthless here, and the exact match is hopeless, because no two good rationales are worded the same. Only a judge can say whether the rationale is faithful and complete. The method follows from the output structure: one correct form takes a match, a structural rule takes a code check, and open-ended quality takes a judge. There is also a cost dimension that the table understates. An exact match and a code check run locally and effectively cost nothing per case, so you can run thousands of them on every change.

A judge is a second model call per case, so a thousand-case eval graded by a judge is a thousand extra API calls every time you run it. That is reasonable for a periodic full evaluation but wasteful as a tight inner loop. Many teams grade format and structure with code on every commit and reserve the judge for a slower, scheduled quality pass. Matching the grader to the task is partially about signal and partially about how often you can afford to run it.

### The grader-selection table you can keep open while you build

Of the three methods listed below, the judge is the only one you must build and tune, so it gets its own treatment here.

| Task type | Grading method | What it catches | Where it is unreliable |
| :-- | :-- | :-- | :-- |
| Single correct label or value | Exact or string match | A wrong answer when there is exactly one correct answer, with zero ambiguity and near-zero cost. | Fails every valid paraphrase or reordering, so it is wrong for anything open-ended. |
| Structured or code output | Code-graded check | Invalid JSON, unparseable code, out-of-range numbers, and missing required fields. | Says nothing about whether the content is good, only that it is well-formed. |
| Open-ended quality | LLM-as-judge | Faithfulness, instruction following, completeness, and tone that no code rule expresses. | Noisy and costly and produces a confident-looking number that means nothing until it is calibrated. |

### Building and calibrating the judge so its scores are defensible

A judge is a second model call guided by a clear rubric. What makes it usable is asking it to provide strengths, weaknesses, and reasoning alongside the score, rather than returning the score alone. Without that, models drift toward a safe middle number, usually around six, regardless of the output's actual quality. Asking the judge for reasoning first is what anchors the score to something specific.

```python
def grade_by_model(task, solution):
    eval_prompt = f"""
    You are an expert reviewer. Evaluate the solution for the task.
    Task: {task}
    Solution: {solution}
    Return JSON with:
      "strengths":  array of 1-3 points
      "weaknesses": array of 1-3 points
      "reasoning":  a one to two sentence explanation, 50 words maximum
      "score":      a number from 1 to 10
    """
    messages = [{"role": "user", "content": eval_prompt}]
    result = chat(messages)        # returns the JSON above
    return json.loads(result)
```

Most people skip calibration, which is what makes the judge untrustworthy until they do it. Start with a set of cases a human has already labeled, run the judge on the same cases, and measure how often the judge agrees with the human. A judge that disagrees with human labels half the time produces a number that looks rigorous but provides no value. Measuring agreement before relying on the scores is what turns the judge from a guess into evidence you can defend. If agreement is low, you fix the rubric: tighten what each score means, add an example of a good and a bad answer, and re-measure.

### Coverage matters more than perfection

A larger evaluation set with slightly noisier automated grading usually reveals more than a small set of hand-graded cases. The point of an eval is to provide enough coverage to catch a regression, not to create the perfect rubric. Twenty cases that include irregular and edge inputs will catch a break that three carefully chosen cases never exercise. When you need more cases, you can have Claude generate additional ones from a small, labeled starting set. You can then spot-check the generated cases so the set stays honest. Coverage is the thing that catches edge cases, and coverage comes from volume.

Put the three pieces together and the workflow is a loop: set a goal, write an initial prompt, run the eval, read where it failed, apply one prompt-engineering change, and run the eval again. You repeat the last two steps until the score holds where you need it. The eval is what tells you a change helped instead of just feeling different.

The strategy that makes the loop work is changing one component at a time. If you rewrite the prompt, add two examples, and switch the model all in one pass, and the score moves, you have learned nothing about which change caused it. Move one lever, re-run, read the per-case results, and keep the change only if the score goes up. This approach is slower for a single iteration, but far faster than the life of the feature, because it teaches you what drives the score. The per-case breakdown matters as much as the average. A steady average can hide a change that fixed three cases and broke three others. The per-case view shows that immediately, while the average conceals it.

A low score is information to act on. When a case fails, the important question is not whether it failed, but why. A formatting failure points at the prompt's output instructions. A factual failure on retrieved content points at the retrieval step. A failure that only appears on long input points at context handling. The eval tells you a case failed, and the per-case output tells you the category, which is what turns the next iteration into a targeted fix rather than a guess.

<table style="width: 100%; border-collapse: separate; border-spacing: 16px; border: none; background: transparent;">
  <tr style="border: none;">
    <!-- Column 1: Green Card -->
    <td style="
      width: 33.33%;
      vertical-align: top;
      background-color: #f0f7f4;
      border: 1.5px solid #2e7d6b;
      border-radius: 12px;
      padding: 20px;
    ">
      <div style="color: #2e7d6b; font-weight: 700; font-size: 1.15em; margin-bottom: 12px;">
        Handles well
      </div>
      <div style="color: #2b2b2b; line-height: 1.5;">
        Turns "looks right" into a tracked score you can defend and move one deliberate change at a time.
      </div>
    </td>
    <!-- Column 2: Orange/Amber Card -->
    <td style="
      width: 33.33%;
      vertical-align: top;
      background-color: #fdf8f2;
      border: 1.5px solid #c97a48;
      border-radius: 12px;
      padding: 20px;
    ">
      <div style="color: #c97a48; font-weight: 700; font-size: 1.15em; margin-bottom: 12px;">
        Adds cost or complexity
      </div>
      <div style="color: #2b2b2b; line-height: 1.5;">
        Authoring cases and calibrating a judge is real up-front work before any feature ships.
      </div>
    </td>
    <!-- Column 3: Red Card -->
    <td style="
      width: 33.33%;
      vertical-align: top;
      background-color: #fdf2f1;
      border: 1.5px solid #b8544c;
      border-radius: 12px;
      padding: 20px;
    ">
      <div style="color: #b8544c; font-weight: 700; font-size: 1.15em; margin-bottom: 12px;">
        Use a different approach
      </div>
      <div style="color: #2b2b2b; line-height: 1.5;">
        For a single fixed-format output, a code check alone is enough. Skip the judge entirely.
      </div>
    </td>
  </tr>
</table>

### Watch Out!

#### The demo that passed and the edge case that did not

> [!Tip]
> You watched the agent answer correctly a dozen times, so you concluded it was done. The problem was that dozen attempts all used inputs that looked like the ones you had in mind when you built it.

**Postmortem: the feature passed every check it had, and still extracted the wrong value**

A team shipped a feature that extracted structured fields from customer messages. Before launch, they ran it through roughly a dozen example messages, read the outputs, agreed they looked right, and moved into deployment. The feature had input validation in place: it confirmed each message was non-empty text, checked that a date field came back populated, and rejected extractions that returned a malformed or impossible date. For two weeks it appeared to work as expected.

Then a customer sent a message that put two dates in one sentence: "I placed my order on March 3 but did not receive it until April 12." The feature extracted April 12 as the order date. Every validation check passed, because both dates are well-formed and the field came back populated. Validation confirms that a value is the right shape. It cannot confirm the value is the right one. Downstream logic acted on the wrong date and a batch of records was updated incorrectly.

The review found no bug in the model or in the prompt. The feature had never been measured against a message containing two dates, because nobody had defined the expected behavior for that case as a graded example. The dozen manual checks all used single-date messages, which is the input the builder pictured. There was no holdout set, so there was no signal that the two-date input existed in the population.

The missing graded set was the root cause. Some behavior change, most likely a prompt change naming which date to extract, corrected the output. The eval did not fix the extraction; it detected the failure, documented the expected behavior as a checkable case, and guarded against the same regression on every future change. The two-date message became case one in that set.

One way to find inputs like this before a customer does: ask the model to enumerate edge cases that could break the current implementation. Two dates in one sentence, no date at all, a relative date like "next Tuesday." Turn the plausible ones into graded cases with a human-checked expected output. This is the same case-generation move the eval-building section covers, applied before launch rather than after.

> [!Caution]
> <small>Why this broke</small>
>
> Success was judged by impression instead of a graded set. The eval is what surfaces failures and guards against regression. The prompt is what changes the output. Write the expected behavior down as graded cases before you ship, and use the model to help you find the edge inputs you did not think to test.

## Testing & Tracing

<span style="font-size: 1.15em">_The eval you just built tells you what good looks like as a number. It does not tell you where a failure happened, nor does it prevent a passing eval from hiding a break somewhere in the workflow._</span>

A graded target needs a test and tracing layer underneath it: tests that isolate each failure type, and traces that show which step produced the bad result.

### Various test levels, each catching a failure the others miss

A test is only useful if you know which failure it identifies. Four levels divide the work, and most silent production breaks live at one particular level:

* A unit test isolates one function, such as a parser or a tool wrapper, and checks it on its own. It tells you that one piece behaves, but nothing about how pieces fit together.
* A functional test checks that one Claude call returns the expected shape for a given input: the right fields, the right type, a parseable response. It validates the call rather than the system around it.
* An integration test exercises the handoff between two components, for example, where a retrieval result is passed into a model call. This is where most silent failures hide, because each side can pass its own tests while the handoff between them is broken.
* An end-to-end test runs the whole flow the way a user would, from input to output. It catches breaks that only appear when everything runs together, at the cost of being the slowest to run and the hardest to localize.

### Tracing: finding the source of failure

Tests tell you that a failure exists, but they do not tell you which step caused it. That is what a trace adds.

A trace records each step of a run: the prompt, the tool calls, the intermediate outputs, and the timing. When a case fails, the trace lets you see which step produced the bad result. Without a trace, a failed eval tells you something is wrong but does not tell you where it failed. This is the difference between a five-minute fix and a day spent tracing the workflow by hand. A trace reads like a timeline of the run, and the failing step is usually obvious once you can see the intermediate output.

```
[trace run_id=8f21c]  case: "Where is my refund?"
  step 1  retrieve(query)        ok    42ms   -> 3 chunks
  step 2  build_prompt(chunks)   ok     1ms   -> prompt 1,240 tok
  step 3  model.call(prompt)     ok   980ms   -> answer "..."
  step 4  parse(answer)          FAIL   2ms   -> KeyError: amount
          final score: 0   (failure localized to step 4, the parser)
```

The trace turns "the case failed" into "step four: the parser raised a KeyError on a field the model did not return." That is also what makes a change reviewable: you can show the step that moved rather than just the score that dropped.

### Routing between the two approaches so you pay for iteration only when you need it

You do not have to pick one strategy for everything. A cheap classification step can send single-fact lookups to the fetch-once path and multi-part questions to the search-across-rounds path. This allows you to spend on iteration only when the query needs it. Defaulting everything to iterative search inflates cost and latency on questions a single fetch would have answered, while defaulting everything to a static index gives shallow answers on questions that needed several passes. The router is one small model call that reads the query and picks the path.

```python
def route(query):
    kind = classify(query)        # cheap call: "lookup" or "multi_step"
    if kind == "lookup":
        return fetch_once(query)  # static retrieval, one pass
    return agentic_search(query)  # search across rounds
```

That one classification call costs far less than running iterative search on a query a single retrieval would have answered. The router earns its cost whenever your traffic is mixed: some queries are simple lookups and some need several passes. If every query is the same shape, skip the router and hardcode the path that fits.

### The reference you can keep open while you build
| Level | What it isolates | What it cannot catch |
| :-- | :-- | :-- |
| Unit | One function, such as a parser or tool wrapper, on its own. | Anything about how components fit together. |
| Functional | One Claude call returning the expected shape for an input. | Failures in the system around that single call. |
| Integration | The seam where two components hand off, such as retrieval into the model. | Whole-flow behavior that only emerges end to end. |
| End-to-end | The full flow as a user runs it, input to output. | Where exactly the break is, since it sees only the final result | 
| Retrieval choice | Fetch a fixed set once for single-fact lookups in a stable corpus. | Multi-step questions and changing corpora, which need search across rounds.|

<table style="width: 100%; border-collapse: separate; border-spacing: 16px; border: none; background: transparent;">
  <tr>
    <!-- Card 1: Handles well -->
    <td style="width: 33.33%; vertical-align: top; background-color: #edf7f4; border: 1.5px solid #2d7a6e; border-radius: 12px; padding: 22px 20px; font-family: inherit;">
      <div style="font-size: 19px; font-weight: 700; color: #2e6f66; margin-bottom: 14px; line-height: 1.3;">
        Handles well
      </div>
      <div style="font-size: 17px; line-height: 1.55; color: #1f2328;">
        Localizes a failure to a step and matches each test to the break it can see.
      </div>
    </td>
    <!-- Card 2: Adds cost or complexity -->
    <td style="width: 33.33%; vertical-align: top; background-color: #faf5ee; border: 1.5px solid #be7e57; border-radius: 12px; padding: 22px 20px; font-family: inherit;">
      <div style="font-size: 19px; font-weight: 700; color: #b86237; margin-bottom: 14px; line-height: 1.3;">
        Adds cost or complexity
      </div>
      <div style="font-size: 17px; line-height: 1.55; color: #1f2328;">
        Tracing and four test levels are infrastructure you build and maintain.
      </div>
    </td>
    <!-- Card 3: Use a different approach -->
    <td style="width: 33.33%; vertical-align: top; background-color: #faf0ee; border: 1.5px solid #b55d5d; border-radius: 12px; padding: 22px 20px; font-family: inherit;">
      <div style="font-size: 19px; font-weight: 700; color: #a4433b; margin-bottom: 14px; line-height: 1.3;">
        Use a different<br>approach
      </div>
      <div style="font-size: 17px; line-height: 1.55; color: #1f2328;">
        For a single-fact lookup in a stable corpus, fetch-once retrieval beats iterative search.
      </div>
    </td>
  </tr>
</table>

### Watch Out!

#### The pieces passed and the seam broke

> [!Tip]
> You tested the prompt and the parser in isolation. Both passed, so you trusted the whole flow.

**Trace excerpt: green unit and functional runs, a red end-to-end run at the handoff**

A trace from an eval run shows the parser unit tests passing and the model-call functional test passing. Each returns the expected shape when tested in isolation. The end-to-end run fails. Reading down the trace, the failure occurs at the handoff where the retrieval result is passed into the model call.

```
PASS  test_parser_unit                 parser returns date objects
PASS  test_extract_shape_functional    model call returns {primary_date, issue}
FAIL  test_full_flow_e2e
  [trace] step 1 retrieve(q)        ok   -> 3 chunks (list of dicts)
          step 2 build_prompt(ctx)  ok   -> ctx inserted as raw list
          step 3 model.call(prompt) ok   -> answer ignores the context
          step 4 assert answer...  FAIL -> model answered from memory
  cause: retrieve() returns [{"content": ...}], build_prompt() expected
         a plain string, so the model received malformed context.
```

Each side was correct in isolation. The retrieval function returns a list of chunk dictionaries, and the prompt builder was written expecting a plain string. This causes the context to arrive malformed and the model to answer from its own memory instead of the retrieved policy. The handoff between the two components was never exercised, because no test covered that seam. This is the failure the integration level exists to catch. A unit test cannot identify it, because the unit itself works. A functional test cannot identify it, because the call works on a well-formed input. Only a test that drives the retrieval-to-model handoff with real retrieved data can raise the mismatch before a user does.

> [!Caution]
> <small>Why this broke</small>
>
> The format contract between the retrieval step and the prompt builder was never defined. One returned a list of dictionaries, the other expected a plain string, and nothing enforced the boundary between them.

> [!Tip]
> <small>How to prevent it</small>
> Add an integration test that drives the two components together with real retrieved data. A unit test cannot catch this because each component works in isolation. Only a test that exercises the handoff surfaces the mismatch before a user does.

## Failure Handling &amp; Model Selection

### Surviving production failure: tool errors

<span style="font-size: 1.15em;">_Your tests now tell you a failure exists and the trace tells you where it happens. The next question is what the system does the moment a failure happens in live traffic._</span>

Production introduces failures a prototype never sees. The difference between a resilient system and a fragile one is whether you decided in advance how each kind of failure is handled.

### Every failure starts with one question: is it retriable or terminal?

The test is a single question: would waiting and trying the exact same request again plausibly work? If yes, it is retriable. If not, it is terminal. A rate limit clears with time; a malformed request will fail identically until the request itself is fixed.

Production traffic produces failures development never shows you: rate-limit responses, timeouts, malformed tool results, and transient network errors. The first decision for any failure is whether a later attempt is likely to succeed. If so, the failure is retriable. If not, retrying only wastes time and budget, making it terminal. A rate-limit response or a temporary server overload is retriable, because the same request will probably go through in a moment. A malformed request or an authentication failure is terminal, because retrying the identical bad request changes nothing. Every subsequent handling decision depends on which bucket a failure lands in. On the Anthropic API, the status code tells you the bucket. A 429 means you hit a rate limit and a 529 means the service is temporarily overloaded, both are retriable. A 400 means a bad request and a 401 means an auth failure, both are terminal. Server errors in the 5xx range, including a 500 internal error and a 504 timeout, are also retriable, because they are Anthropic-side faults that typically resolve on retry.

```python
RETRIABLE = {429, 529, 500, 502, 503, 504}   # rate limit, overload, transient
TERMINAL  = {400, 401, 403, 404}             # bad request, auth, missing

def is_retriable(status):
    return status in RETRIABLE   # everything else fails fast
```

The reason this one distinction carries so much weight is that it determines whether waiting helps. A retriable error is one where the cause is transient: the service was momentarily over capacity, a connection dropped, or you briefly exceeded a per-minute limit. Time alone resolves it, so a later attempt is likely to succeed. A terminal error is one where the cause is in the request itself: a malformed body, an expired key, a model name that does not exist. Time changes nothing, because each request will produce an identical error. Retrying a terminal error wastes the retry budget and hides the actual problem behind a wall of identical failures. Each unnecessary retry consumes retry budget and increases the latency that a retriable failure elsewhere in the flow might have needed. Correct classification preserves the retry budget for failures that need it.

A few statuses sit on the line and are worth calling out. A timeout is usually retriable because the work may simply have taken longer than the client was willing to wait. Repeated timeouts on expensive requests is a signal to fix the request itself, not to retry it. A 500 from the service is retriable, because it is a server-side fault that often clears. A 403 is terminal, because it is a permissions problem that a retry cannot fix. When you are unsure, the safe default is to treat an error as terminal and raise it. A failure incorrectly classified as terminal fails loudly and gets fixed. A failure incorrectly classified as retriable hammers a service and hides the real problem behind a wall of retries.

### The SDK already retries some failures, so know what it covers before you write your own

Before you build a retry loop by hand, check what the SDK does for you. The Anthropic client libraries automatically retry transient failures with progressive retry delays, up to a configurable number of attempts. The point of knowing this is to avoid adding your own retries on top of the ones the SDK is already running. Two retry loops wrapped around the same call multiply attempts against a rate limit rather than capping them. Decide where the retry lives: either let the SDK handle transient cases and reserve your own code for application-specific fallbacks, or turn the SDK retries down and own the full path yourself. Running both layers retrying the same failure without either knowing about the other is the pattern to avoid.

The API also returns rate-limit headers on each response that tell you how much of your limit remains and when it resets. The most useful is retry-after, which a 429 or 529 response includes to tell you how long to wait before trying again. Honoring that value is more precise than guessing with backoff alone, because the service is telling you exactly when capacity returns. The corrected retry code later in this module reads retry-after first and falls back to exponential backoff only when the header is absent. Treat the header as the authoritative wait time when it is present, and treat your own backoff as the fallback when it is not. The specific header names and limit values are version-pinned, so confirm them against the reference layer at build time.

### Tool errors must come back to Claude explicitly rather than dropped

When your code runs a tool and that tool fails, the result should be returned to Claude with is_error explicitly set to true. It should not return as a silent empty result. With the error returned, the model can react: try a different approach, ask for clarification, or stop. A tool that drops its own error and returns nothing produces a confident yet wrong answer downstream. This is because the model treats the empty result as valid data and continues reasoning on top of it. A visible failure is far easier to catch than a confident but incorrect answer built on missing data.

```python
def run_tool(tool_use):
    try:
        result = execute(tool_use)
        return {"type": "tool_result", "tool_use_id": tool_use.id,
                "content": result}
    except Exception as e:
        # surface the error so Claude can react, do NOT return empty
        return {"type": "tool_result", "tool_use_id": tool_use.id,
                "is_error": True, "content": f"Tool failed: {e}"}

def run_tool(tool_use):
  # A refusal is a 200 at the HTTP layer, the retriable classifier will not catch it
  if response.stop_reason == "refusal":
      raise ValueError("Model refused the request. Review input before retrying.")
```

With is_error set, the model knows the tool failed and can react. Without it, the model treats the empty result as valid data and continues on a false premise.

### The error-handling decision table you can keep open while you build

| Error type | Retriable or fail-fast | Backoff strategy | Fallback behavior |
| :-- | :-- | :-- | :-- |
| Rate limit (429) | Retriable | Exponential backoff with jitter, honor retry-after, capped attempts. | After the cap, raise a clean error or route to a cached or simpler result. |
| Overloaded (529) | Retriable | Backoff; a 529 reflects Anthropic-side load, so it is not a rate-limit signal. | Fail over to a fallback path or return a graceful error if it persists. |
| Bad request (400) | Fail fast | No retry. The identical request will fail again. | Fix or reject the input and surface the error to the caller. |
| Tool result error | Depends on the tool | Retry only if the underlying cause is transient. | Return the error flag to Claude so the model can react, never silence it. |
| Refusal (200, stop_reason: "refusal") | Fail fast | No retry. The model made a content decision, not a transient error. | Raise the refusal to the caller. Log it. Do not silently retry or treat it as valid output. |

<table style="width: 100%; border-collapse: separate; border-spacing: 16px; border: none; background: transparent;">
  <tr>
    <!-- Card 1: Handles well -->
    <td style="width: 33.33%; vertical-align: top; background-color: #edf7f4; border: 1.5px solid #2d7a6e; border-radius: 12px; padding: 22px 20px; font-family: inherit;">
      <div style="font-size: 19px; font-weight: 700; color: #2e6f66; margin-bottom: 14px; line-height: 1.3;">
        Handles well
      </div>
      <div style="font-size: 17px; line-height: 1.55; color: #1f2328;">
        Keeps one bad response from cascading into an outage by handling each failure type by name.
      </div>
    </td>
    <!-- Card 2: Adds cost or complexity -->
    <td style="width: 33.33%; vertical-align: top; background-color: #faf5ee; border: 1.5px solid #be7e57; border-radius: 12px; padding: 22px 20px; font-family: inherit;">
      <div style="font-size: 19px; font-weight: 700; color: #b86237; margin-bottom: 14px; line-height: 1.3;">
        Adds cost or complexity
      </div>
      <div style="font-size: 17px; line-height: 1.55; color: #1f2328;">
        Every failure path is code you write, test, and maintain on top of the happy path.
      </div>
    </td>
    <!-- Card 3: Use a different approach -->
    <td style="width: 33.33%; vertical-align: top; background-color: #faf0ee; border: 1.5px solid #b55d5d; border-radius: 12px; padding: 22px 20px; font-family: inherit;">
      <div style="font-size: 19px; font-weight: 700; color: #a4433b; margin-bottom: 14px; line-height: 1.3;">
        Use a different<br>approach
      </div>
      <div style="font-size: 17px; line-height: 1.55; color: #1f2328;">
        Do not retry a terminal error. Retrying a 400 does nothing but waste the retry budget.
      </div>
    </td>
  </tr>
</table>

### Watch Out!

> [!Tip]
> <small>The call that never failed in development</small>
>
> In development, you called the endpoint a few dozen times and it returned cleanly every time, so there was no obvious reason to write an error path. That is the trap. Development traffic is low volume, runs on a stable connection, and rarely hits the conditions that cause a call to fail: rate limits, timeouts, transient network drops, or a malformed response underload. None of those show up when you are testing by hand, so the code that handles them never gets written. The first time the call fails is in production, and the failure appears as an unhandled exception rather than a recoverable error.

#### Anecdote: the first rate-limit response took the whole request down

A developer building a customer-facing feature called the API in a loop. Every development run returned successfully because development traffic never came close to a rate limit. The code was written without any error handling, because up until now, nothing had ever failed there.

```python
results = []                      # collect each response

for item in batch:
# shipped version, no error path
    resp = client.messages.create(model=MODEL, max_tokens=MAX_TOKENS, messages=msg(item))
    results.append(resp.content)    # assumes every call returns 200
```

The feature shipped. At the first traffic peak the API returned a rate-limit response, the unhandled error was raised and the whole request failed instead of waiting a moment and trying again. To the user it looked like the feature was simply broken. The developer's first instinct was to add immediate retries in a tight loop. This made it worse: each instant retry counted as another request against the same limit, deepening it. The real fix was the distinction from the teaching screen. The rate-limit response was retriable, so it needed exponential backoff with a capped number of attempts and a retry that honored the retry-after value when the response included one. Development never produced the failure, so the path that would know how to handle one was never written.

> [!Caution]
> <small>Why this broke</small>
>
> A retriable failure met code that had no error path, then met a hammering retry that deepened the limit. Sort the error as retriable, then back off with a cap, before traffic finds the gap for you.

### Model Selection in Production

The previous screens kept a system inside its cost budget once the model was chosen. This screen handles the choice that sets that budget in the first place: which Claude model runs the workload.

Cost management optimizes spend within a model. Model selection determines the baseline that optimization works from.

The model family and its capability tiers
Claude is a family of models that trade cost, latency, and capability against each other: Fable is the most capable for the most demanding reasoning, coding, and agentic work; Opus handles demanding work above the Sonnet envelope; Sonnet is the balanced default for most production workloads; Haiku is built for speed and cost efficiency on tasks that fit its envelope. The same prompt runs on any of them, so model choice is a lever you set per workload and can change without rewriting the application. Confirm the current lineup and model IDs against platform.claude.com at build time.

The latency, cost, and quality trade-off
Upgrading model tier trades quality at the price of higher per-token cost and usually higher latency. Downgrading the model tier buys speed and lower cost at the risk of a quality drop. A higher-tier model can also process a request faster and cheaper if it reaches a conclusion in fewer tokens than a lower-tier model would. The cost of a mistake belongs in that calculation: saving a few dollars a day on a lower-tier model is not a sound trade if the quality drop introduces errors that carry significant downstream cost. There is no globally correct choice, only the right choice for a task at a quality standard. The discipline is to make the trade-off measurable rather than reaching for the most capable model by default. This is the most common and most expensive model-selection mistake in production. The default is to start with Sonnet, move up to Opus only when an eval shows Sonnet missing the quality bar, and move down to Haiku only when an eval shows the quality drop is acceptable for the task.

Routing: a default model plus an override on a task signal
A system does not have to use one model for everything. A common production pattern is a default model with an override: route the bulk of traffic to a balanced default, and send specific request types to a larger or smaller model based on a cheap signal read from the request, such as task type, input length, or a difficulty classification. This is the same routing idea used for retrieval, applied to model choice: you pay for the more capable model only on the requests that need it. Where every request is the same shape, skip the router and pin one model.

When to step up and when to step down
Step up a tier when an eval shows the current model failing on the hardest cases your traffic contains and the cost of a wrong answer is high. Step down a tier when an eval shows a cheaper model holding the quality bar on the bulk of traffic, freeing budget and latency. In both directions the eval is the instrument: a model change is promoted on a measured score against your cases. This is why the eval you built earlier is also the gate for a model decision.