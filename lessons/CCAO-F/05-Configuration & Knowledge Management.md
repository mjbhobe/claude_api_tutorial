# Configuration & Knowledge Management

<span style="font-size: 1.25em;">_There is a line between using Claude and operating Claude._</span>

Using it means typing a good prompt today. Operating it means building an environment where the right context, instructions, and procedures are already in place, so every conversation starts from a configured baseline instead of a blank slate. Configuration is leverage: you set it up once and benefit from it on every conversation that follows.

Configuration is also the move that turns individual skill into team capability. When the Project, instructions, and knowledge are curated, two people asking the same question get the same quality of answer. When they are not, everyone re-invents context daily and the answers drift.

There is a second half to the discipline: maintenance. Configurations age. A standing instruction written for last quarter's process, a knowledge base full of superseded documents, or a Skill that has drifted out of date will quietly degrade output. A well-configured environment is built deliberately and reviewed on a cadence.

## Configuring Claude Projects

<span style="font-size: 1.25em;">_A Project has several configuration slots, and the skill is putting each piece of a recurring need into the right one. Instructions govern behavior, the knowledge base holds facts, Skills carry procedures, and scoped Memory keeps continuity. Choosing the right slot for each need is what makes a Project run smoothly._</span>

### The four configuration mechanisms

1. **Standing Instructions:** How Claude should behave across all conversations in a project: tone, format defaults, verification habits. _Bahaviour, not facts_.
2. **Knowledge base:** The documents, policies and reference files that Claude should draw on _without re-uploading_. _Facts and reference, not behaviour_.
3. **Skills:** Repeatable procedures that Claude should follow consistently for a task type. _Procedure, not one-off instructions_. Skills live at account level under Customize, not inside any one project. A Skill you build is reuseable across any project that needs it.
4. **Scoped Memory:** Continuity within the project, kept separate from your other projects so context does not bleed between workstreams.

### Choosing the right mechanism

The recurring question is: _instruction, knowledge, or Skill?_ A rule about behavior (`"always cite sources"`) is an instruction. A fact Claude needs (`"our brand palette is these hex codes"`) is knowledge. A multi-step procedure (`"format findings into our standard report template"`) is a Skill, built once at the account level under Customize and reused across any Project that needs it, rather than configured inside a single Project.

Putting a procedure into the instructions, or a behavior rule into the knowledge base, is the most common configuration mistake, and it makes the Project harder to maintain.

### Worked example: a client account workspace

> [!Important]
> <small>ONE PROJECT PER CLIENT</small>
>
> A consultant sets up one Project per client. For Client A:
>
> **Standing instructions:** "Write in a formal register. Always cite the source document for any factual claim. Flag anything you are unsure of rather than guessing."
>
> **Knowledge base:** the client's brand guide, the current statement of work, and the last three status reports.
>
> **Skill (account-level, reused here):** the firm's status-report formatter, which lives under Customize at the account level and is available to any Project, so every weekly update comes out in the same structure.
> 
> **Scoped Memory:** the client's stakeholder names and standing preferences, which never appear in Client A's Project.

On Team or Enterprise, the Project can be shared with the engagement team under permissions, so everyone works from the same configured baseline. Project-scoped Memory is what guarantees Client A's context does not appear in a Client B conversation, the separation that makes one-Project-per-client safe.

### Scoped Memory as a first-class mechanism

Memory is easy to treat as an afterthought, but in a Project, it is a configuration slot like any other. Instructions say how Claude should behave and the knowledge base says what is true. Skills carry reusable procedures at the account level, available to any Project that needs them. Scoped Memory holds what the Project has already settled: the stakeholder names, the standing preferences, the decisions from earlier conversations you do not want to restate every time.

The word that matters is "scoped". A Project's Memory is sectioned off from your other Projects, so context built up for one client or workstream never appears in another. That isolation is what makes Memory safe for sensitive or client-specific continuity. Claude remembers what it needs to without the risk of it revealing information to the incorrect audience. Deciding what belongs in Memory versus knowledge comes down to type: a stable reference fact goes in knowledge while an evolving record of Project decisions goes in Memory.

### When a need spans two mechanisms

> [!Tip]
> <small>THE PAIRING RULE</small>
>
> The cleanest configurations rarely map a need to a single slot. The most common pattern is a behavior rule plus the facts it acts on: <small>`"Always cite the source document for factual claims"`</small> is a standing instruction, but the documents it cites live in the knowledge base. Neither works alone: the instruction has nothing to cite without the documents, and the documents get used inconsistently without the instruction. Skills pair the same way: a status-report Skill carries the procedure, while the brand guide it formats against sits in knowledge. So when you configure a Project, ask which slot a need belongs in, and whether it needs two slots wired together.

## Connectors and Uploaded Knowledge

<span style="font-size: 1.25em;">_Connectors extend Claude's reach into the data you already work in, like Google Drive and Gmail. They are powerful, and they have boundaries._</span>

Managing them as curated sources, and knowing exactly what each one can and cannot do, is what keeps them useful instead of frustrating.

### Connecting external sources

A connector lets Claude reach an external system you authorize, such as searching your Drive for a document or finding a relevant email. You manage what is accessible, and you keep that set deliberate rather than connecting everything by default.

### Capability boundaries

Each connector has a defined boundary and knowing it prevents wasted time. A mail connector may let Claude search and read messages but not send them. Expecting an action a connector cannot perform produces a confusing failure, not a clear error, so learn each connector's boundaries before you build a workflow on it.

### Two field-observed pitfalls

1. **Wrong path to add a connector**: The obvious add-connector path can route to a public directory rather than your organization's vetted connectors. Confirm the right path with your admin, especially on Team or Enterprise, so you connect the approved source and not a look-alike.
2. **Boundary confusion misroutes fixes**: When a connector hits its capability boundary, the failure can look like a bug, a pattern reported from field use rather than documented product behavior. Reports then go to the wrong team and the fix stalls. Knowing where each connector's capability ends keeps the issue from being mislabeled.

### Keeping uploaded knowledge current

Uploaded knowledge needs the same care as a connected source: keep it current, relevant, and free of duplicates. A knowledge base with three versions of the same policy invites Claude to cite the wrong one. Curate it the way you would a shared drive, removing deprecated versions as you add new ones.

## System-Level Instructions That Stick

<span style="font-size: 1.25em;">_Teams keep asking a version of the same question: can we bake the guardrails in once instead of re-typing them every conversation? Persistent instructions are exactly that mechanism._</span>

You write the verification behaviors, format defaults, and tone once, and every conversation in the Project inherits them.

### Write the guardrails once

The highest-value instructions are the ones you would otherwise re-type constantly. Set the verification behaviors as standing instructions, for example:

> <small>`"Cite the source document for every factual claim, and say 'I don't know' rather than guessing when the documents do not cover something."`</small>

Now that discipline applies to every conversation without anyone remembering to ask for it.

### Anticipate the use cases

Good standing instructions embed format, tone, and guardrail guidance ahead of need. If the Project produces client deliverables, the instructions can specify the preferred format and register up front, so the first draft lands closer to a final deliverable rather than needing the same corrections each time.

### Precision, or it silently fails

Vague instructions do not announce that they failed; they just quietly do not work. `"Be professional"` gives Claude almost nothing to act on. `"Use a formal register, define any acronym on first use, and keep paragraphs under four sentences"` is precise enough to change the output.

The test of an instruction is whether two different people would read it the same way.

### Worked example: before and after an instruction

<link rel="stylesheet" href="./tabs.css">

<div class="jb-tabs-container">
<input type="radio" name="jb-tab-group" id="tab1" checked>
<input type="radio" name="jb-tab-group" id="tab2">
<input type="radio" name="jb-tab-group" id="tab3">

<div class="jb-tabs-header">
<label class="jb-tab-label" for="tab1">Before: vague</label>
<label class="jb-tab-label" for="tab2">After : Precise</label>
</div>

<div class="jb-tab-content">

<div class="jb-tab-panel" id="content1">
<p><strong><small>VAGUE INSTRUCTION.</small></strong><br/> <p>"Make the reports good and accurate." Output quality varies conversation to conversation; nothing concrete changed.</p>
</div>

<div class="jb-tab-panel" id="content2">
<p><strong><small>PRECISE INSTRUCTION.</small></strong><br/> <p>"For every figure in a report, state its source. If a figure is not in the provided data, mark it 'unverified' rather than including it. Lead each report with a one-sentence headline." Now the verification behavior is consistent, and the headline appears every time.</p>
</div>

</div>
</div>

## Maintaining Configurations

<span style="font-size: 1.25em;">_Configurations are living assets. Instructions, knowledge, Skills, and Memory all drift toward stale, and stale configuration degrades output quietly, with no error to alert you. Scheduling maintenance is how you catch decay before it reaches a deliverable._</span>

### Review cadence

Set a recurring review for each active Project: do the standing instructions still match the current process, is the knowledge base free of superseded documents, are the right Skills enabled? A monthly pass for active Projects catches most drift. The signal that you waited too long is output quality slipping for no visible reason.

### Skills versioning

Skills update over time. Anthropic-built and organization-provisioned Skills update automatically; your own custom-uploaded Skills change only when you re-upload them. Watch for a misconfigured or out-of-date Skill degrading output. A Skill that silently produces a slightly off format every run is a maintenance problem, not a prompting problem.

### Memory lifecycle

Treat Memory like a working file. Review it periodically, edit or delete entries that have gone stale, and export it as a backup before a major change. When a Project's Memory has accumulated enough outdated context to mislead, a full reset is the right call. The accuracy of what is stored matters more than the volume.

**Configuration is also additive:** when Claude has not automatically captured a fact that matters: a constraint, a preference, a piece of background, add it explicitly to standing instructions or Memory rather than re-supplying it each session.

### Worked example: auditing a degraded setup

> [!Tip]
> <small>A RECURRING REPORT PROJECT STARTS PRODUCING SUBTLY WRONG OUTPUT</small>
>
> The maintenance checklist finds the causes: a standing instruction still references a metric the team renamed last quarter, the knowledge base holds two versions of the template, and a Memory entry records a stakeholder who has left.
>
> The fix is maintenance, not a new prompt: update the instruction, remove the old template, delete the stale Memory entry. Output returns to standard without changing how anyone prompts.