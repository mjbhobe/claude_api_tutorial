# Production-Grade Prompting, Agents & Tool-use

<span style="font-size: 1.25em;">_Writing code that uses Claude is different from using Claude to write code._</span>

You have probably used Claude interactively when you’ve typed a prompt, read the response, and adjusted it as needed. This module addresses all subsequent aspects of using Claude beyond this basic level, including tool schemas, context management, and agent loops. This module builds upon your ability to shape Claude’s outputs. **As an engineer, you are responsible for programmatically integrating Claude, ensuring reliable output handling, and successfully deploying a robust production solution**.

Each topic in this module addresses a specific failure mode that is frequently overlooked during development but requires significant time and effort to identify and resolve after development is underway. When you learn to identify and avoid these failure modes, you’ll be positioned to effectively and efficiently integrate Claude into your development processes.

## Prompting Craft

### System prompts, XML, few-shot, and output constraints

<span style="font-size: 1.15em;">_A prompt that works once in interactive use often breaks when it runs in production against untested inputs. The fix for this isn’t just adding more words, it is identifying which structural piece is missing from the prompt and adding that one piece. This section reviews how to read a failed output, then walks through the four techniques that produce the fixes._</span>

### Four techniques that give Claude a reliable output shape

When a first-pass response misses, the instinct is often to add more words to the prompt and run it again. However, that instinct can make the problem harder to isolate and rarely fixes it. Rewording changes how you say something but does not add to the structural piece of the prompt that’s missing. For example, if Claude is crossing the boundary between your instructions and your input data, clearer phrasing will not fix it, and if the output format keeps drifting, `"please format this correctly"` will not fix it either.

The failure mode tells you which of the four techniques is absent. Diagnose how your prompt is failing first, then add the specific technique that addresses that failure. The four techniques themselves are defined in full further down this screen.

| What you observed | What the prompt is missing | Why this technique is the fix |
| :-- | :-- | :-- |
| **The result comes back in the wrong shape:** a sentence where you expected a label, prose where you expected JSON. | An output constraint. The prompt never specified the form, field names, or stopping point of the response. | An output constraint controls the form of the response independent of its content. Without one, Claude returns plausible text that the downstream parser was not built to accept. |
| **The content is off:** scope drifts, tone shifts, or Claude answers a wider question than you asked, and it gets worse deeper into the conversation. | A system prompt, or a more specific one. The behavioral contract was too vague to hold across turns. | The system prompt sets the rules that apply to every response regardless of the user turn. When it is underspecified, there is nothing holding role, scope, and format steady as the conversation runs on. |
| **The task is right, but the structure is invented:** Claude understood what to do and produced output in a shape you never asked for. | Few-shot examples. Claude cannot infer an exact structure from a description alone. | Few-shot examples show the pattern rather than describe it. One correct input-output pair gives Claude the exact shape to match, which a written instruction often fails to pin down. |
| **Output is clean on the inputs you tested but breaks on a variant:** an edge case, an unusual field, an input you did not anticipate. | A constraint covering the variant. The prompt handles the happy path and has no rule for the case the parser breaks on. | The prompt was validated against a narrow set of inputs. Naming the variant in the constraint, or adding an example that covers it, closes the gap the test inputs never exposed. |

### Diagnosing a classification prompt that returns the wrong output shape

**The rule is simple:** name the failure, add the one technique that matches it, and re-run it. If it still fails, diagnose again. When a prompt keeps getting longer with every pass, that’s the sign you’re skipping the diagnosis step and just adding words.

The pattern below is the first row of the table in action: a prompt that produces the right content in a shape the downstream code cannot accept. The classifier understands the task and returns the correct category, but the form of that answer varies from run to run, so the router that consumes it fails. The missing piece is an output constraint, and the fix pulls in two of the other techniques to lock the label set and show the format. The walkthrough moves from the bare prompt that causes the problem to the constrained version that resolves it.

#### Worked example: a classification prompt before and after

A developer needs Claude to classify support tickets into three categories: `billing`, `technical`, and `escalation`. The first prompt is a bare instruction with no constraint on the output:


> **System:** `"You are a support classifier. Classify the ticket."`
>
>**User:** <ticket>I was charged twice for the same month.</ticket>

Claude returns `"Billing"` on some runs, `"billing"` on others, and occasionally a full sentence like `"This looks like a billing issue."` The downstream router expects one of a fixed set of labels and breaks on the inconsistency.

Read this against the table above, this situation matches what is described in the first row: the output comes back in a shape the parser cannot accept, so the missing piece is an output constraint. Adding that constraint pulls in two more techniques, because locking the label set and showing the format are jobs those techniques do better than a written instruction can. Few-shot examples show Claude the exact label and casing to return, and XML tags keep those examples separate from the instruction so Claude does not read them as part of the task:

> **System:** `"You are a support classifier. Classify each ticket into exactly one of: BILLING, TECHNICAL, ESCALATION. Return only the label. No other text."`
>
> <sample_input>My account shows two charges for April.</sample_input>
> <ideal_output>BILLING</ideal_output>
>
> <sample_input>The API keeps returning a 429 error.</sample_input>
> <ideal_output>TECHNICAL</ideal_output>
>
> **User:** `<ticket>I was charged twice for the same month.</ticket>`

Three techniques are doing distinct work here. The system prompt sets the output contract: exactly one label from a fixed set, nothing else. The XML tags mark where each example ends and the next begins, so Claude does not read the examples as part of the instruction. The few-shot pairs show the exact casing and format rather than describing it. Together they produce a result consistent enough to route programmatically.

The table below shows how we can stack all the four techniques together, where the prompt should be simplified, and where we should diagnose before adding more before too many iterations.

| | |
| :-- | :-- |
| Stack all four techniques | Stacking all four techniques against a clearly defined output contract. Tasks with well-specified formats and edge cases that can be covered by examples.|
| Simplify the prompt | Adding all four techniques to a simple task that only needs one. A "summarize this paragraph" prompt does not need few-shot examples and an output schema.|
| Diagnose before adding more | Prompts that are growing longer with each iteration rather than more precise. If you have re-prompted five times and the output is still wrong, diagnose the failure type before adding more text.|

### When to reach for each technique

Now, let’s understand more about each of these techniques and when each one applies:

<link rel="stylesheet" href="./tabs.css">

<div class="jb-tabs-container">
<input type="radio" class="jb-r1" name="jb-tab-group-1" id="g1-tab1" checked>
<input type="radio" class="jb-r2" name="jb-tab-group-1" id="g1-tab2">
<input type="radio" class="jb-r3" name="jb-tab-group-1" id="g1-tab3">
<input type="radio" class="jb-r4" name="jb-tab-group-1" id="g1-tab4">

<div class="jb-tabs-header">
<label class="jb-tab-label jb-l1" for="g1-tab1">System Prompts</label>
<label class="jb-tab-label jb-l2" for="g1-tab2">XML Tags</label>
<label class="jb-tab-label jb-l3" for="g1-tab3">Few-shot Examples</label>
<label class="jb-tab-label jb-l4" for="g1-tab4">Output Constraints</label>
</div>

<div class="jb-tab-content">

<div class="jb-tab-panel jb-p1" id="g1-content1">
<p><strong>System Prompts</strong><br/><p>System prompts carry the behavioral contract for the whole session. Write them once and treat them as your persistent instruction layer. They define Claude’s role, the output format, and any rules that must not change between conversations.</p>
</div>

<div class="jb-tab-panel jb-p2" id="g1-content2">
<p><strong>XML Tags</strong><br/><p>XML tags are used when the prompt mixes inputs with instructions. A prompt that asks Claude to debug code using provided documentation is a good example; without tags, the code and the documentation look the same to Claude.

Wrap them with descriptive tag names like `<my_code>` and `<docs>` and the boundary becomes unambiguous. You do not need to use official XML tag names; descriptive names that match your content work best.</p>
</div>

<div class="jb-tab-panel jb-p3" id="g1-content3">
<p><strong>Few-shot Examples</strong><br/><p>Few-shot examples are considered useful because they show rather than just tell. Instead of trying to describe the exact format you want, you provide one correct input-output pair and let Claude infer the pattern. To use this, wrap examples using consistent XML structure, for instance < sample_input > and < ideal_output >, so the boundary between example and prompt is clear. You can use some examples from your highest-scoring evaluation outputs rather than writing them from scratch.</p>
</div>

<div class="jb-tab-panel jb-p4" id="g1-content4">
<p><strong>Output Constraints</strong><br/><p>Output constraints are the last line of defense before Claude’s response reaches your parser. You should specify exactly what you need, including field names, types, length limits, whether to include preamble, and what to do when data is absent. Use structured output features in cases when the format must be machine-readable.</p>
</div>

</div>
</div>

### The iteration loop: Diagnosing before re-prompting

When a first-pass response misses the mark, the instinct is to add more words to the prompt and try again. That instinct almost always makes the problem harder to diagnose and rarely fixes it.

Instead, diagnose the problem first, and then re-prompt based on your findings. The failure type tells you which technique is missing:

* **Wrong format:** This is caused due to a missing output constraint. The prompt never specified what shape the result should take.
Wrong content or scope drift: This is caused due to an underspecified system prompt; the behavioral contract was too vague to hold across conversations.
* **Correct task but hallucinated structure:** This happens when few-shot examples are needed. Claude cannot infer the exact structure from a description alone.
* **Good output on simple inputs but breaks on edge cases:** The prompt handles the happy path but has no constraint covering the variant the parser breaks on.

The fix is structural, not a matter of phrasing. For example, if Claude is ignoring a boundary between your instructions and your content, clearer wording will not fix it, and if the output format keeps drifting, saying "please format this correctly" will not fix it either. In each case, identify which of the four techniques is absent and add it.

### Moving output control from the prompt into the API with structured outputs

Everything up to this point shapes the output by writing instructions into the prompt and hoping Claude follows them. That works most of the time, but the prompt is a request, so a model can still return a stray sentence, a wrong field name, or malformed JSON that breaks the parser downstream.

The Claude API has a separate mechanism that removes that gap for production code. It is called structured outputs, and instead of asking for a shape in words, you hand the API a JSON schema, and the model is constrained at generation time to produce output that matches it. This technique is constrained decoding: as Claude generates each token, the API only allows tokens that keep the output valid against your schema, so a response that violates the schema cannot be produced in the first place.

Structured outputs cover two situations that show up in real pipelines. Each one constrains a different part of what the model returns, and you can use them on their own or together in the same request.

* **JSON outputs constrain the final response.** You set the output_config.format parameter with type json_schema and your schema, and Claude returns valid JSON in the response text that matches that schema every time. Reach for this when the model itself is producing the structured payload your code consumes, like extracting fields from a support ticket or formatting an API response, because it removes the parse-and-retry code you would otherwise write around every call.
* **Strict tool use constrains the inputs Claude passes to your tools.** You set strict to true on a tool definition, and the arguments Claude sends to that tool are validated against the input schema before your code runs. Reach for this in agentic loops where a malformed tool argument would crash the function or trigger a wrong action; this helps guarantee the call your code receives already conforms to the contract you defined. 

The reason this belongs in the production code and not just in the prompt is because of reliability under inputs you did not test. A prompt-level instruction to return only JSON holds on the cases you tried and then slips on an edge case you did not, which is the exact failure the earlier classification example walked through. A schema constraint does not slip, because the API enforces it on every token rather than trusting the model to remember the instruction. That moves output correctness from something you verify after the fact to something the API rules out before it happens.

Constraining generation has costs, and a developer choosing this in production needs to weigh them rather than enabling it everywhere by default. Below are some of those costs you must consider:

* **The first request on a new schema is slower.** The API compiles your schema into a grammar before it can constrain output, and that compilation adds latency on the first call. Compiled grammars are cached for 24 hours from last use, so steady traffic on a stable schema pays the cost once, but a workload that changes schemas constantly pays it repeatedly.
* **Your input token count rises.** When structured outputs are on, the API adds a system prompt describing the expected format, and that injected prompt is billed like any other input token. The increase is small per call, but it is worth knowing when you are estimating cost at volume.
* **A guaranteed schema is not a guaranteed success.** Two cases still return output that does not match: a refusal, where the model declines for safety reasons and the response carries stop_reason refusal, and a truncation, where the response hits the max_tokens limit and stops mid-structure with stop_reason max_tokens. Your code still checks stop_reason rather than assuming every response parses.
* **It does not combine with message prefilling.** JSON outputs and prefilling the assistant message are incompatible, so a pattern that starts the response for Claude and a pattern that constrains the whole response to a schema cannot run on the same request. Pick the one that fits the task.

## Extended Thinking

### Turning reasoning on, calibrating effort, and reading it back correctly

<span style="font-size: 1.15em;">_The prompting techniques shape what Claude produces. Extended thinking shapes how much work Claude does before it answers. Turn it on, and the model writes out its step-by-step reasoning first, then gives you the final answer. Your job is to decide when that extra work is worth the cost and to handle the reasoning it sends back._</span>

### What extended thinking does

When you turn on extended thinking, the model "thinks out loud" before it responds. You’ll see this reasoning come back as its own thinking block in the API response, positioned just ahead of the block that holds the actual answer. On the newest models, the thinking block's content is omitted by default; you must request a readable summary through the display setting to see it.

> 📌 **NOTE**<br/><br/>
> **On current models reasoning is adaptive:** you enable it with the thinking parameter where it is not already on by default, and the model decides how much reasoning each request needs. You tune depth with the effort setting rather than a fixed token budget. The older `budget_tokens` control is deprecated and, on the newest model generations, returns a 400 error.

**That reasoning isn’t free**; thinking tokens cost the same as output tokens, so running a simple task at high effort means paying for accuracy you don’t need. The choice here mirrors the one you have already made: match the tool to the task. Don’t reach for extended thinking by default, apply it strategically where needed.

### When to use extended thinking

|Task shape | Extended thinking call | Reason |
| :-- | :-- | :-- |
| Multi-step reasoning where the model has to hold several constraints at once: a math derivation, a multi-hop logic problem, planning a sequence of dependent actions. | Enable it, with the effort level matched to the depth of the problem. | The reasoning pass is where the model works through dependencies it would otherwise skip. |
| Mechanical or lookup tasks: classification, format conversion, extracting a field, short factual answers. | Leave it off. | Extended thinking will not improve the answer, and you will be paying more tokens for something you didn’t need. A bare prompt with an output constraint is the right tool. |
| Agentic loops where the model plans across several tool calls. | Enable it and budget for the planning step rather than per call. | Reasoning before a plan reduces wrong-tool selection downstream. Note the carry-back rule below, which applies in every tool-use loop. |

#### The carry-back rule: thinking blocks must return to the API unchanged

When extended thinking is on and your conversation uses tools, there’s one rule you can’t skip: every thinking block you get back has to go back to the API exactly as it arrived on the next turn. Each block comes with a signature that confirms the reasoning wasn’t tampered with. If you edit it, summarize it, or drop it, the signature stops matching and the API rejects the request.

Redacted thinking blocks work the same way. Their contents are encrypted and not meant to be read by humans, but they still have to be returned untouched.

This is a structural requirement, not a prompting choice you get to make. The most common slip-up is stripping out the thinking block to save context, which ends up breaking your next request. If the real worry is how much context piles up from accumulated reasoning, the fix is the context-engineering work we’ll cover in this module.

> 👉 **Forward pointer**
>
> This lesson enables reasoning and calibrates its effort setting; it does not cover model selection. Choosing which model to run, as distinct from whether to enable reasoning, is taught in the MSO Foundations module that precedes this one.

**Handles well**
Hard reasoning and planning tasks where a wrong answer is expensive and the extra tokens buy accuracy.

**Adds cost or complexity**
The carry-back requirement in tool-use loops, and an effort setting you now must calibrate.

**Use a different approach**
For classification, extraction, and format tasks, a well-constrained prompt is cheaper and just as accurate.

![Test your knowledge](images/extended_thinking_tyk.png)

## Tool Usage &amp; Schema Design

### Tool Schemas Claude Selects Correctly: Definition, Loop, and Calling Patterns

<span style="font-size: 1.15em;">_So far, the work has been about shaping what Claude produces: framing the request, giving examples, picking the technique that fits the output you want. With tool-use, you’re not steering language toward a good answer anymore, you’re handing Claude a set of actions and trusting it to pick the right one; that pick is driven almost entirely by what you wrote in the schema._</span>

### How the tool-use loop works

The most common misconception about tool-use is that Claude runs the tools. Instead, Claude reads your tool definitions, decides which one fits the situation, and tells your application what to call it along with the required inputs. Your application executes the tool, gets the result, and sends it back; then Claude uses that result to continue.

This back-and-forth shouldn’t be ignored in production: if your application does not handle the return correctly, Claude never gets the data it asked for, and the loop breaks. The boundary between what Claude owns and what your code owns is where most tool-use bugs live. 

Here is the sequence to ensure proper implementation of tool-use:

1. **Define schema:** You define a schema with a name, a description, and an input schema. Claude reads this to decide whether and when to call the tool.
2. **Send message:** Your code sends a message to Claude including the tool definitions and the user's input.
3. **`tool_use` block:** Claude issues a tool-use block containing the tool name, a unique ID, and the input arguments it wants to pass. The API response comes back with stop_reason: tool_use.
4. **Execute tool:** Your code executes the tool using those arguments. Note that the assistant turn has already ended (Claude is not holding a connection open or waiting on your server). The model is stateless between calls. To continue, your code makes a fresh API request containing the prior messages plus the tool result.
5. **Return result:** You return the result in a tool-result block that references the original tool-use ID.
6. **Claude continues:** Claude continues using the tool result as context for its next response, either another tool-use block or a final end turn.

It’s important to note that the loop is not automatic and you need to complete the fourth step. If the miss is systematic, the fix is in the schema definition step.

### Message block structure in a tool-use conversation

A tool-use conversation is built out of structured blocks, not plain text. Each assistant turn and user turn is a list of blocks, and four block types do the work in a tool-use session. A `text` block carries Claude’s prose response. A `tool_use` block carries a tool call, including the tool name, a unique ID, and the input arguments. A `tool_result` block carries what your code returned after running the tool. A `thinking` block carries Claude’s internal reasoning, and it only appears when extended thinking is enabled.

The API enforces a specific pairing between these blocks. Every `tool_use` block in an assistant turn must be answered by a `tool_result` block with a matching ID in the user turn that immediately follows. If the IDs don’t match, if the result is missing, or if the turns are out of order, the request fails validation. This is not something you can fix by adjusting your prompt; it’s structural, and your code has to produce the sequence correctly on every request.

The table below summarizes each block type, what it contains, and the rule that governs how your code must handle it.

| | | | |
|:-- |:-- |:-- | :-- |
| Block type | Role | Contains | Critical Rule |
`text` block | Assistant/Claude | Claude’s prose output | Claude may return a text block alongside a `tool_use` block in the same turn. When it does, your code must preserve the full content array, including the text block, when appending that turn to conversation history. Dropping the text block corrupts the context Claude relies on for follow-up turns. |
| `tool_use` block | Assistant/Claude | The tool name, a unique ID, and the input arguments Claude wants passed to your function | Every `tool_use` block must be answered by a `tool_result` block in the immediately following user turn. The `tool_result` must carry the same ID. Without that pairing, the API rejects the next request. |
| `tool_result` block | User | Matching `tool_use` ID, the result content, and an optional `is_error` flag set to true when the tool call fails | The `tool_use_id` value must match the original `tool_use` block exactly. Claude uses this ID to connect each result back to the call that produced it, which matters when a single assistant turn issues multiple tool calls and the results arrive in a different order. |
| `thinking` block | Assistant (extended thinking only)/Claude | Claude’s internal reasoning, visible only when extended thinking is enabled | The block must be passed back to the API unchanged in subsequent turns. The signature verifies the reasoning hasn’t been modified, so any edit or summary breaks the signature and the API rejects the message. Redacted thinking blocks follow the same rule: pass them back as received, even though the content is encrypted and not human-readable. |

The critical invariant is that every `tool_use` block from an assistant turn must have a corresponding `tool_result` block in the immediately following user turn. Missing `tool_result` blocks, or `tool_result` blocks that appear in a later turn rather than the immediately following user turn, cause an API validation error.

### Schema anatomy: What Claude reads to make a tool selection decision

A tool schema has three parts, including `name`, `description`, and `input_schema`. The description determines whether Claude selects the tool correctly or not.

1. **Name:** A short identifier that should be specific. For example, `get_account_balance` is more useful to Claude than `get_data`.
2. **Description:** A critical part that Claude reads to decide whether a tool is required or not. You should always write the description in two parts, including when to and when not to use the tool:
    * A description that says "use this to find information" will cause wrong selections because Claude cannot distinguish it from any other tool that retrieves something.
    * A description that says "use this to retrieve the current balance for a specific account ID and do not use this for transaction history" gives Claude an exclusion condition to work with and is appropriately descriptive.
3. **`input_schema`:** Defines the parameters (the inputs your tool function accepts) using JSON Schema.
    * You should mark parameters as required when Claude requires them to call the tool correctly.
    * You can mark parameters as optional when the tool can operate without them. Overlapping parameter types between tools is the most common source of wrong-tool calls.

### Decision table: Schema design choices

The schema is what Claude reads to decide which tool to call, what arguments to pass in, and whether it has enough information to respond. A schema that’s vague, under-described, or missing required fields will produce tool calls that look syntactically correct but pick the wrong tool, pass malformed inputs, or loop unnecessarily. The five decisions below determine whether your implementation behaves predictably under real conditions. The table notes where sequential and parallel tool-calling diverge.

| | | |
| :-- | :-- | :-- |
| Decision | How to handle it | Why it matters |
| **Subtask dependency** | When one tool’s output feeds the next, the calls have to run in sequence because the second call cannot be built until the first result comes back. When the subtasks are independent of each other, you can structure the tool set so Claude issues multiple `tool_use` blocks in a single turn and your code runs them concurrently. | This is the one decision that changes how you design the schema. Current Claude models default to parallel calls when calls are independent. Where a real dependency exists, model it as separate turns so the first result is available before the next call is built. Use `disable_parallel_tool_use` to force one tool call per turn if needed. |
| **Required fields** | Mark a field as required only when the call doesn’t make sense without it. Place these in the required array of the input schema. | Marking everything required forces Claude to fabricate values for fields it has no basis to fill in. The required array is how you tell Claude which inputs are non-negotiable. |
| **Optional fields** | Use optional fields for parameters with sensible defaults or where absence carries meaning. Leave them out of the required array and give them defaults in the function signature. | Optional fields let Claude omit information it doesn’t have, instead of guessing. If a field is optional but marked required, every call must invent a value, which can cause bad inputs. |
| **Description length** | Write three to four sentences per tool covering what it does, when Claude should reach for it, and what it returns. Include examples of valid inputs where format matters. | If the description is too short, Claude guesses because there isn’t enough signal to distinguish your tool from others. If the description is too long, the trigger conditions get buried under detail Claude doesn’t reference at decision time. |
| **Overlapping parameter types** | When two tools accept the same parameter shape, add disambiguating language to each description that names the domain or trigger the tool is meant for. | Claude routes on name plus description, with parameter types as a secondary signal. When signatures are identical, routing collapses to description alone, and similar-sounding descriptions become indistinguishable. |

**Worked example: A schema that causes wrong-tool selection and the fix**

This is an illustrative example based on common patterns observed in tool-use implementations. Tool names, descriptions, and test results are constructed to demonstrate the selection-disambiguation principle, not drawn from a specific production system.

A developer registers two tools, including `search_knowledge_base` and `get_cached_result`. The tool names are distinct, but Claude’s tool selection weighs descriptions heavily; when descriptions overlap, name alone is not sufficient to disambiguate. Both have descriptions that start with _"use this to find information..."_ Without exclusion conditions, Claude frequently selected the wrong tool on ambiguous inputs during development testing.

The problem is that both descriptions look identical to Claude at the point where the selection decision is made. The fix is adding an additional sentence per description:

* `search_knowledge_base`: "Use this to search the knowledge base when the user asks a question that requires looking up current information. Do not use this if the result of a prior search in this session already covers the question."

* `get_cached_result`: "Use this to retrieve a result that was already fetched during this session. Only use this if `search_knowledge_base` was called earlier in this conversation for the same query."

The exclusion conditions give Claude a decision rule rather than two identical-looking options. These conditions rely on complete conversation history being passed in each request. If prior turns are truncated or dropped, Claude cannot evaluate them and the exclusion logic silently fails.

**Every additional tool you register increases the surface area Claude has to reason over**, so this discipline only pays off when the underlying tools are distinct. The table below shows where exclusion-condition disambiguation helps and where a different approach is warranted.

> **Handles well**
> Routing Claude to the right tool reliably when descriptions are specific and exclusion conditions are stated.
>
> **Poor fit**
> Two tools that do similar things and need ever-longer descriptions to keep apart: at that point, merge them into one tool with a type parameter instead.

### When someone else has already written your tools: MCP as an alternative to manual schema authoring

Everything in the previous sections assumes you are writing the tool schemas yourself: `name`, `description`, `input_schema`, and the function that executes when Claude issues a `tool_use` block. For many integrations, you do not need to do that. The Model Context Protocol (MCP) is a standardized communication layer that moves tool definitions and execution out of your application code and into dedicated servers. When an MCP server exists for the service you want to reach, you can connect directly to the MCP server rather than building the integration yourself.

Take a GitHub integration as a concrete case. GitHub exposes repositories, pull requests, issues, projects, and more. To build a complete integration using the tool schema approach from this module, you would need to write a schema and an execution function for every piece of that functionality and maintain it as GitHub’s API evolves. An MCP server for GitHub has already done that. So, your application connects to the server, receives the full list of available tools, and Claude selects among them using the same description-based routing you have already been working with. The underlying mechanism is identical, but what changes is who wrote it and who owns the tool definitions.

### How MCP fits into the tool-use loop

The loop you built earlier in this module does not change when you introduce MCP. Claude still issues a `tool_use` block, your application still executes the tool and returns a `tool_result`, and the message block pairing rules still apply. The difference is in the setup step. Instead of registering schemas you wrote, your MCP client sends a `ListToolsRequest` to the MCP server, receives the full tool list back, and passes those definitions to Claude. From Claude’s perspective, those tools are indistinguishable from ones you authored manually.

**One practical implication worth noting**: MCP servers add tool definitions to the context window even when the tools are not being used in the current turn. If you connect several servers at once, the tool definitions themselves consume budget before the first message arrives. The schema design discipline from earlier in this module applies here too. Register only the servers you are actively using, and check context cost against your window limit if you are connecting multiple servers in the same session.

If you are using the API MCP Connector, you control loading cost through an `mcp_toolset` object in the tools array. The `mcp_toolset` carries a `default_config` block that applies to every tool on the server, and you can override individual tools through configs keyed by tool name. Two settings matter for context cost:

* The `defer_loading` boolean, set inside `default_config` or a per-tool entry in configs, delays loading a tool definition until the model needs it, which reduces upfront context cost when you connect a server with a large tool list.
* The `enabled` boolean turns individual tools on or off, so you can register a server but expose only the tools you want the model to see. The MCP Connector requires the `mcp-client-2025-11-20` beta header to be set on the request.

Without that header, the `mcp_toolset` configuration will not apply as described here.

The other piece worth knowing at this stage is how the client actually talks to the server. MCP runs over one of two transports, and which one you use depends on where the server lives. **Local servers use `stdio`** and your application spawns the server as a subprocess and communicates over standard input and output. **Remote servers use `Streamable HTTP`** and your application connects over the network via HTTP, using POST for client-to-server messages and an optional GET-based SSE stream for server-initiated messages. An older SSE-only transport exists but is deprecated, and new integrations should use Streamable HTTP. One constraint worth flagging if you are using Anthropic’s MCP connector in the API: only HTTP-exposed servers are supported through the connector, and stdio servers require managing the MCP client connection yourself via the SDK. Once the connection is established and tool definitions are received, your application code treats both transports identically.

> [!Tip]
> <small>**USE MCP WHEN**</small>
>
> A well-maintained MCP server already exists for the service you need (check that it covers the specific operations you require and is actively maintained against the service’s current API. Writing and owning those schemas yourself adds implementation overhead for no additional capability. **Note that the Claude API MCP Connector only supports remote servers**. Local stdio servers require Claude Desktop or Claude Code as the client; they cannot be connected directly through the API.

> [!Tip]
> <small>**WRITE SCHEMAS MANUALLY WHEN**</small>
>
> No MCP server covers your use case, or when you need precise control over tool scope and description quality that a general-purpose server does not provide. Before defaulting to manual schemas for scope control, note that the API MCP Connector supports allowlisting and denylisting specific tools per server via MCPToolset configuration. Manual authoring may still be warranted for description quality, but not always for scope.

> [!Tip]
> <small>**USE BOTH WHEN**</small>
>
> Connect to an MCP server for breadth then apply the description-tuning discipline from earlier in this module to the specific tools you are actively routing to. MCP and manual schema authoring are not mutually exclusive as the server gives you coverage, and your descriptions give you precision where it matters. Apply tool allowlisting via MCPToolset to limit the surface area Claude reasons over before layering in description tuning. Narrowing the tool set and sharpening the descriptions are two separate levers, and you should use both.

### The description that sent Claude to the wrong tool

> [!Tip]
> <small>SETUP</small>
>
> **A schema can look correct and still fail**. Typed parameters and passing happy-path tests tell you the structure is valid, but they do not tell you whether Claude can reliably choose between your tools when an input sits near the boundary of two overlapping descriptions. That is the failure mode that initial testing misses and the one most likely to surface during production.

**A Developer is three hours into a code review when they paste an internal channel conversation into a debug session.**

_This is a composite exchange based on common patterns in developer debugging conversations. The dialogue is constructed to illustrate the diagnostic moment when description overlap gets named, not transcribed from a specific code review._

Let’s look at the exchange below that happens after a Developer has been debugging incorrect tool selections since morning. The Senior Developer asks one question that reframes the whole problem:

> **Developer**: "Why does Claude keep calling search_docs when the answer is already in the context? I've re-run this four times, and it keeps going to the wrong tool."
> 
> **Senior Developer**: "What does the description for search_docs say?"
> 
> **Developer**: "'Use this to find information about the product.'"
> 
> **Senior Developer**: "And what does get_context_summary say?"
> 
> **Developer**: "'Use this to retrieve relevant information from the current session.'"
> 
> **Senior Developer**: "Those descriptions are the same thing from Claude's perspective. Both say, 'find information.' One of them needs to say when not to call it."
> 
> **Developer**: "So, I need to add an exclusion?"
> 
> **Senior Developer**: "Right. Try using search_docs ‘when the user asks a question that requires looking up content not already present in this conversation. Do not call this if the answer is available in the current session context.' Then get_context_summary handles the in-context case. You will want to tighten get_context_summary's description the same way: add 'Only use this if the answer is already present in the current session. Do not use this to look up new information.' Both tools need the boundary, not just one."
> 
> **Developer**: "That's two sentences."
> 
> **Senior Developer**: "Right. One to say when to use it, one to say when not to. That's the whole fix."

> [!Important]
> <small>WHAT TO WATCH OUT FOR</small>
>
> Claude selects a tool by reasoning over all registered descriptions in the context of the full conversation. When two descriptions look similar, that reasoning has no reliable signal to distinguish them so Claude picks based on small surface differences that may not correspond to the distinction you intended.
>
> When the failure is overlapping descriptions, the fix is consistent: add one sentence naming when not to call the tool to give Claude a decision boundary. If the descriptions cannot be cleanly separated even with exclusion conditions, the tools may need to be merged into one with a type parameter instead.

## Streaming Responses

### Streaming responses and handling partial output without corrupting state

<span style="font-size: 1.15em;">_Every request so far has waited for the whole response to arrive before doing anything with it. That's fine, until the response is long, or a user is sitting there staring at a blank screen. Streaming sends the response in pieces, sending them along as the model generates them. That makes things feel faster, but it also gives your code a new job: now you are tasked with assembling the final content yourself based on the series of outputs, and you need to be prepared if the series stops early._</span>

### What streaming changes about the response

In a non-streamed request, the API hands you one complete message with every content block, fully formed. In a streamed request, the API instead sends a series of events that describe the message as it's being built. Your code listens to that series and reassembles the blocks. The message you end up with is identical to what a non-streamed call would have given you, but the difference is that you have to assemble the pieces, and you decide what to do if the events stop before the message is finished.

It helps to know what's not happening: the model isn't holding some live object open for you. Each event is its own small message describing a single change, a block started, some text or input got added to it, a block finished, the whole message finished. Your handler takes each event and applies it to the partial state it's been building up.

### The event sequence, and what your handler does with each

| | | |
| :-- | :-- | :-- |
| Event | What it signals | What your handler does |
| `message_start` | A new message is beginning. Carries the message shell with empty content and initial usage. | Set up an empty content array to collect blocks in. |
| `content_block_start` | A new content block is opening, with its type (text, tool_use, or thinking) and index. | Make a slot at that index for the named block type. A tool_use block opens with its name and id, but no input yet. |
| `content_block_delta` | An incremental piece of one block: a text fragment, a fragment of JSON input for a tool call, or a thinking fragment. | Append the fragment to the block at that index. Tool-call inputs arrive as a partial JSON string spread across several deltas, you can't parse them until the block closes. |
| `content_block_stop` | The block at this index is complete. | Finalize the block. For a tool_use block, this is the first moment the accumulated JSON input is complete enough to parse. |
| `message_delta` | Top-level changes to the message: the stop_reason and final usage counts. | Record the stop_reason. It tells you whether the model finished or stopped for some other reason. |
| `message_stop` | The stream is complete. | The assembled content array is now the finished message. From here, treat it exactly like a non-streamed response. |

### The rule that keeps your state from getting corrupted: don't act on a partial block

The `tool_use` block is the one to watch. Its input shows up as a partial JSON string spread across many `content_block_delta` events, and that string isn't valid JSON until `content_block_stop` closes the block. If your code tries to parse the input or run the tool before the block closes, it either chokes on malformed JSON or runs with half the arguments missing. So, the rule is simple: collect the deltas, and act only after `content_block_stop` for that block.

The same discipline applies when you add a streamed assistant turn to your conversation history. Add it only after `message_stop`, with every block fully assembled. A turn built from a stream that got cut off partway is incomplete, and the `tool_use` pairing rules will reject your next request if a half-built `tool_use` block ends up in the history.

### When the stream stops early

Streams sometimes fail in the middle. A dropped network connection, a timeout, or a client disconnect can end the event series before `message_stop` arrives. The failure that really bites is treating whatever you've collected so far as if it were complete. A partial text block shown to a user is just a cosmetic glitch and a partial tool_use block written into history is a structural problem that corrupts the next turn.

* **Track completion on purpose**. A turn is usable only once message_stop has arrived. Until then, treat what you've accumulated as provisional.
* **On an interrupted stream, throw away the partial assistant turn** instead of saving it to history, then retry the request. Committing a half-built turn is exactly what breaks the following request.
* **Check the `stop_reason` from `message_delta` before you continue a loop**. A `stop_reason` of `tool_use` means your assembled tool calls are ready to run; any other value means you're on a different path, not the tool path.

> **Handles well**
> Long responses and user-facing interfaces where showing output as it generates removes the blank-screen wait.
> 
> **Adds cost or complexity**
> You assemble blocks yourself, you must not act on partial blocks, and you must handle mid-stream interruption explicitly.
> 
> **Use a different approach**
> For short responses or backend jobs where no one is waiting on the output, a non-streamed call is simpler and removes the partial-state risk entirely.
> 

### The stream that left a half-written tool call in the history

> [!Tip]
> <small>SETUP</small>
>
> A streamed response can look fine on screen and still corrupt the next request. The text rendered, the user saw an answer, and the handler appended the turn to history. What the handler did not catch was that the stream dropped mid-block, so the tool_use call it stored was missing half its input. The next request fails validation, and the error points at the next turn and not the stream that caused it.

**Postmortem: partial tool_use block committed to history after a dropped stream**

An agent used streaming so its operators could watch responses generate in real time. The handler accumulated content_block_delta events and appended the assistant turn to history when its read loop ended. In testing on a fast local connection, streams always ran to completion, so the loop always ended at message_stop and the stored turns were always complete.

In production, a network blip ended one stream after the tool_use block had opened and received part of its JSON input, but before content_block_stop. The read loop ended the same way it always had, so the handler appended the turn: an assistant turn containing a tool_use block whose input string was truncated JSON. The operator saw a partial answer and retried. The retry request included that corrupted turn in history, and the API rejected it with a validation error pointing at the malformed tool_use block.

The team spent an afternoon inspecting the schema and the retry logic, because the error surfaced on the retry request. However, the actual cause was upstream: the handler treated 'the read loop ended' as equivalent to 'the message is complete,' and those are not the same.

> [!Important]
> <small>WHAT TO WATCH OUT FOR</small>
>
> A stream ending is not the same as a message completing. Only message_stop means the message is whole. If your handler commits a turn whenever its read loop exits, an interrupted stream writes a half-built block into history, and the failure shows up on the next request rather than the one that caused it. Gate the history append on message_stop, discard the partial turn on interruption, and retry from the last complete turn. When a tool-use error appears on a retry, check whether the prior turn was assembled from a stream before you touch the schema.

Here is how you would typically process streaming response:

```python
"""Stream one assistant turn from the Claude API and rebuild its content blocks.

Example context: a BFSI assistant that can call a loan EMI calculator tool.
"""

import json
import logging
from typing import Any

import anthropic
from anthropic.types import RawContentBlockDelta, RawContentBlockStartEvent

logger = logging.getLogger(__name__)

MODEL = "claude-haiku-4-5"
MAX_TOKENS = 4096

# Tool inputs stream as JSON fragments. We buffer them under this private key
# and replace the buffer with a parsed dict in assemble().
_JSON_BUFFER = "_partial_json"

# Block types whose "input" arrives as input_json_delta fragments.
_TOOL_BLOCK_TYPES = {"tool_use", "server_tool_use"}


class StreamInterruptedError(RuntimeError):
    """Raised when a stream ends before the message_stop event."""


# One client per process. It reads ANTHROPIC_API_KEY from the environment.
client = anthropic.Anthropic()


def init_block(event: RawContentBlockStartEvent) -> dict[str, Any]:
    """Create an empty, mutable block from a content_block_start event.

    Args:
        event: The content_block_start event from the stream.

    Returns:
        A plain dict in the shape the Messages API accepts as assistant content.
    """
    block = event.content_block
    block_type = block.type

    if block_type == "text":
        return {"type": "text", "text": block.text or ""}

    if block_type == "thinking":
        return {
            "type": "thinking",
            "thinking": block.thinking or "",
            "signature": block.signature or "",
        }

    if block_type in _TOOL_BLOCK_TYPES:
        # The start event carries an empty input; the real input streams in later.
        return {
            "type": block_type,
            "id": block.id,
            "name": block.name,
            "input": {},
            _JSON_BUFFER: "",
        }

    # redacted_thinking and server tool results arrive complete in the start
    # event, so we pass them through unchanged.
    return block.model_dump(exclude_none=True)


def apply_delta(block: dict[str, Any], delta: RawContentBlockDelta) -> None:
    """Merge one content_block_delta payload into its block, in place.

    Args:
        block: The block created by init_block for this event index.
        delta: The delta payload from a content_block_delta event.
    """
    delta_type = delta.type

    if delta_type == "text_delta":
        block["text"] += delta.text
    elif delta_type == "thinking_delta":
        block["thinking"] += delta.thinking
    elif delta_type == "signature_delta":
        # Sent once, just before the block closes. It must be sent back to the
        # API unchanged, or a later request that includes this block is rejected.
        block["signature"] = delta.signature
    elif delta_type == "input_json_delta":
        block[_JSON_BUFFER] += delta.partial_json
    elif delta_type == "citations_delta":
        block.setdefault("citations", []).append(
            delta.citation.model_dump(exclude_none=True)
        )
    else:
        # A newer delta type this code does not know about. Log it so the gap is visible.
        logger.warning("Ignoring unknown delta type: %s", delta_type)


def assemble(blocks: dict[int, dict[str, Any]]) -> list[dict[str, Any]]:
    """Turn accumulated blocks into final assistant content.

    Args:
        blocks: Mapping of stream block index to block dict.

    Returns:
        Content blocks ordered by index, with tool inputs parsed into dicts.

    Raises:
        ValueError: If a tool block's accumulated JSON is invalid, for example
            when max_tokens cut the output mid-argument.
    """
    content: list[dict[str, Any]] = []
    for index in sorted(blocks):
        block = dict(blocks[index])  # shallow copy so the input mapping stays untouched
        if _JSON_BUFFER in block:
            raw = block.pop(_JSON_BUFFER)
            try:
                # No arguments streamed means a tool call with an empty input.
                block["input"] = json.loads(raw) if raw else {}
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"Invalid tool input JSON for block {index} "
                    f"({block.get('name')}): {raw!r}"
                ) from exc
        content.append(block)
    return content


def stream_turn(
    messages: list[dict[str, Any]],
    tools: list[dict[str, Any]],
    model: str = MODEL,
) -> None:
    """Stream one assistant turn and append it to messages on success.

    Args:
        messages: Conversation history. Mutated only if the turn completes.
        tools: Tool definitions in the Messages API format.
        model: Model identifier.

    Raises:
        StreamInterruptedError: If the stream ends before message_stop.
    """
    blocks: dict[int, dict[str, Any]] = {}
    stop_seen = False

    with client.messages.stream(
        model=model, max_tokens=MAX_TOKENS, messages=messages, tools=tools
    ) as stream:
        for event in stream:
            if event.type == "content_block_start":
                blocks[event.index] = init_block(event)
            elif event.type == "content_block_delta":
                apply_delta(blocks[event.index], event.delta)
            elif event.type == "message_stop":
                stop_seen = True

    if stop_seen:
        messages.append({"role": "assistant", "content": assemble(blocks)})
    else:
        raise StreamInterruptedError(
            "Stream ended before message_stop; discarding partial turn. "
            "Retry from the last complete turn."
        )


if __name__ == "__main__":
    print(f"anthropic SDK version: {anthropic.__version__}")

    emi_tool = {
        "name": "calculate_emi",
        "description": "Calculate the monthly EMI for a loan.",
        "input_schema": {
            "type": "object",
            "properties": {
                "principal": {"type": "number", "description": "Loan amount in INR."},
                "annual_rate_pct": {"type": "number", "description": "Interest rate, e.g. 9.5."},
                "tenure_months": {"type": "integer", "description": "Loan tenure in months."},
            },
            "required": ["principal", "annual_rate_pct", "tenure_months"],
        },
    }
    history = [
        {
            "role": "user",
            "content": "What is the EMI on a 50 lakh home loan at 8.75% for 20 years?",
        }
    ]
    stream_turn(history, [emi_tool])
    print(json.dumps(history[-1], indent=2))
```