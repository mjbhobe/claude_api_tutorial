# Accelerators and IP Contribution

## Document the build well and the next engagement builds from it instead of from scratch.

In the last three modules you built a production agent, wired it into Claude Code with the right permission and context controls, and set up the MCP connections that pass a security review. Each of those was a working build.

This module covers what happens to a build after it works. You either rebuild it from scratch on the next engagement, or you package it once, so the next team just configures it. The second path is what frees your time for new work instead of repeated rebuilding.

By the end of this module, you will be able to:

1. Package a working solution as a reusable accelerator, whether that is a parameterized agent template, a configurable MCP server, or a portable eval suite, so the next engagement configures an asset rather than fully rebuilding it.
2. Contribute a tool, pattern, or fix back through the documented channels and prepare it so a maintainer can accept it, turning a private asset into shared infrastructure.
3. Choose where a Claude workload runs across the first-party API, Amazon Bedrock, Google Vertex AI, and third-party platforms, and version what ships so a model or prompt change does not silently break production.
4. Compare those platforms on latency, compliance, and cost so the choice is one a procurement and security team can sign off on, rather than a default your team reached for.
5. Build an application that coordinates several Claude deployments into one workflow and scope it so the data and identity boundaries are held under a security or compliance review.

This module is for the Developer who has a build that works and now must make it last. You are practical, code-forward, and pattern-oriented, and the earlier modules assumed and built on that. By this point you can write a production agent, configure it in Claude Code, wire up MCP connections that pass a security review, and prove it all with evals. This module does not re-teach any of that. It picks up the moment your code runs correctly and asks the harder question: can someone else reuse it, can a maintainer accept it, can it survive a model update, and can a security or procurement team sign off on where it runs. The work here is less about writing code and more about the decisions that make finished code reusable, deployable, and defensible to people who did not write it.

## Packaging for Reuse

### Packaging a working build so the next engagement starts from an asset

<span style="font-size:1.15em;">_You finished the prior modules with a build that runs: an agent loop, a configured MCP server, an eval that proves that the prompt works. The most time-consuming and expensive thing on a team is the engineering time that gets spent rebuilding the same thing for the next customer._</span>

### What an accelerator does: keep the reusable parts and separate out the rest

An accelerator is a solution packaged so future engagements start from a working foundation rather than from a blank repository. In blueprint terms, this is packaging for reuse: separating engagement-specific code from the reusable core and parameterizing the rest. Take a working build, separate the parts that are customer-specific, and expose them as parameters with documented defaults. The asset then configures rather than gets entirely rewritten. Packaging for reuse while the build is fresh is cheaper than reconstructing the intent months later, when the person who knew why a value was hardcoded has moved on.

**Most reusable work falls into different asset types, and each one packages differently**

Most reusable work falls into one of three categories used throughout this module: a template, a configurable server, or a portable eval. Each type holds a different kind of work and needs to be packaged in its own way. Reaching for the wrong type can make an asset look reusable while still making it difficult to apply.

| **Asset type** | **What it bundles** | **What correct packaging requires** |
| :--- | :--- | :--- |
| Agent Template | The system prompt, the tool schemas, and the loop structure from a working agent. | Pull the domain-specific values into configuration with documented defaults, so a new team sets the values rather than editing the loop. |
| MCP Server Package | The tools the server exposes, with their inputs and the scope the installing team controls. | Document each tool input and let the installing team set the scope, so the server installs into a new environment without code edits. |
| Eval Suite | The graded test set and the judge rubric that prove the asset works. | Ship the dataset and rubric together so a new team can run them in their own context and confirm the asset still works there. The same eval suite also acts as the gate at deployment. When you promote a new model version to production, run it against a pinned baseline score before the version goes live. |

Shipping an agent as a set of loose scripts instead of a template is the most common version of the wrong approach. The scripts run, so they look reusable, but every customer-specific value is buried in a different file, and the next team copies and diverges them instead of configuring one asset.

### Document both the code and the assumptions

Code describes behavior. Documentation covers what a future builder cannot reliably infer from reading the source: the assumptions the asset makes about its environment, the inputs it expects, the failure modes it already handles, and the eval that defines whether it still works. Without this, the next team treats the asset as a black box and rebuilds it.

### Bundle the audit log as part of the package

A regulated customer's reviewer asks what data the asset touches, what identity it acts under, and what log it leaves. An accelerator without these passes a demo and stalls at the first security review. Treat the audit log as part of the package.

### The packaging checklist

Keep this checklist next to the build while you package it. Each column is a decision you make once per asset.

| **Asset type** | **What to parameterize** | **What to document** | **What to bundle for audit** |
| :--- | :--- | :--- | :--- |
| Agent template | Every value that changes per customer: prompts, paths, scopes, credentials by reference, and thresholds. | Environment assumptions, expected inputs, handled failure modes, and the eval that defines working. | The data touched, the identity acted under, and the log of what the asset did. |
| MCP Server | Scopes, credentials by reference, and per-customer paths. | Expected inputs per tool, scope boundaries, and handled failure modes. | The data touched, the identity acted under, and the log of what the asset did. |
| Eval Suite | Thresholds and dataset paths that change per customer or environment. | The rubric logic, what the scores mean, and the baseline the asset is pinned to. | The data touched, the identity acted under, and the log of what the asset did. |

<table style="width: 100%; border-collapse: separate; border-spacing: 12px 0; table-layout: fixed; background-color: transparent;">
  <tr style="background-color: transparent;">
    <td style="background-color: #eaf2ef; border: 1.5px solid #2e8466; border-radius: 8px; padding: 16px; vertical-align: top;">
      <div style="color: #2e8466; font-weight: bold; margin-bottom: 8px; line-height: 1.35;">Handles well</div>
      <div style="color: #262522; line-height: 1.55;">Parameterizing while the build is fresh turns one delivery into an asset the next engagement configures in hours.</div>
    </td>
    <td style="background-color: #f6efe4; border: 1.5px solid #c56a2d; border-radius: 8px; padding: 16px; vertical-align: top;">
      <div style="color: #c56a2d; font-weight: bold; margin-bottom: 8px; line-height: 1.35;">Adds cost or complexity</div>
      <div style="color: #262522; line-height: 1.55;">Separating generalizable from customer-specific parts and documenting assumptions adds real time to the first build.</div>
    </td>
    <td style="background-color: #f8e9e8; border: 1.5px solid #b8443d; border-radius: 8px; padding: 16px; vertical-align: top;">
      <div style="color: #b8443d; font-weight: bold; margin-bottom: 8px; line-height: 1.35;">Use a different approach</div>
      <div style="color: #262522; line-height: 1.55;">For a one-off a customer will never reuse, packaging overhead is not worth it: ship the build and move on.</div>
    </td>
  </tr>
</table>

### Watch Out!

**The template that shipped fast and could not be reused**

> [!Tip]
> Setup
>
> Hardcoding ships faster and you were working under a deadline, so you hardcoded the values that made the demo. The template worked. That is exactly why nobody looked at it again until the next team tried to reuse it.

This is a postmortem, written the way a team writes one after the reuse attempt fails, so you can see the failure form before anyone labels it as a mistake.

**What happened**
A team built an agent template for a customer engagement and shipped it on time. To hit the due date, the customer-specific values went straight into the code: the repository path, the model name, the review thresholds, and a handful of prompt fragments specific to that customer's domain. The template ran, the engagement closed, and the build went into the shared repository labeled as reusable.

Months later a second team picked it up for a similar engagement. They could not configure it, because there was nothing to configure. Every value that needed to change was baked into the loop where the second team could not see it without reading the whole file. There was no document saying which values were customer-specific and which were load-bearing. There was also no bundled eval, so even after they guessed at the edits, nothing confirmed the template still worked in the new context. They had to rewrite it from scratch.

> [!Caution]
> Why it broke
>
> The build was treated as finished the moment it ran rather than at the moment it could be reused. Hardcoding was the reasonable call under a deadline, and it was never revisited. A working template does not announce that it cannot be reused. The cost appeared only when a second team paid for the rebuild that packaging was supposed to prevent, along with the time they lost discovering the template was a dead end.

> [!Caution]
> What to Watch Out for
>
> A template that runs has not been packaged for reuse. These are different finishing states. The warning signs are the absence of three things: no parameters where customer-specific values belong, no documentation describing the assumptions, and no bundled eval proving the asset still works in a different context. Package the asset while the build is fresh. The knowledge of what is customer-specific is most expensive to reconstruct after the people who had it have moved on.

## Contributing Back

### Moving an asset from private reuse into shared infrastructure a maintainer accepts

<span style="font-size:1.15em;">_You have already done most of the work that makes an asset shareable. When you packaged it for your own team to reuse, you pulled out the parameters, wrote down the assumptions, and bundled the eval. The parameters show the asset can be configured rather than rewritten. The documented assumptions tell the maintainer what environment the asset expects. The bundled eval gives them a way to confirm it still works. An asset packaged for internal reuse is already close to what a maintainer needs to accept it._</span>

The contribution channel is designed to receive that packaged asset. It carries the version, the installation steps, and the components as a single unit, so a team that never spoke to you can install it and get the same working setup.

### Match the contribution to the channel built for it

Contributing back means moving an asset from private reuse to shared infrastructure through a documented channel. Each channel is built for a specific kind of contribution. The Claude Cookbook is a GitHub repository of focused reference implementations. It is designed for self-contained single- or multi-pattern implementations demonstrated clearly and working end to end. Open-source MCP servers and tools each live in their own repository with their own contribution conventions. Sending a full multi-component application to the Cookbook is a mismatch. The repository is set up to review one focused pattern rather than an entire application, so a submission that large does not fit what reviewers are looking for and will stall. The first step is matching the contribution to the channel built for it. Putting a full application where a focused example belongs is one of the most common reasons a contribution never gets reviewed.

**What makes verifying a contribution possible**

A maintainer accepts a contribution they can verify. The bar is set by what they need to check, not by how clever the code is. Four things make that verification possible:

1. The code does one thing. A sprawling contribution forces a reviewer to reconstruct your intent before evaluating it.
2. An example shows it running. A reviewer should not have to build a harness to see the behavior.
3. A test proves it works. A test lets a maintainer verify the result without reproducing the reasoning themselves.
4. A short statement names the assumptions. Otherwise, the first failure becomes the maintainer's problem.

### Rights and attribution come before technical review

Licensing and attribution decide whether a contribution can be accepted at all, which is why they come before the technical review. Code carried in from a customer engagement may have constraints on where it can go. Confirming you have the right to contribute it, and attributing anything you built on, is a gate the contribution must pass first. Skipping this is what turns a contribution into a problem the legal team must unwind later.

The example worked here is the customer service agent case. A reusable conversation-handling pattern, built during an engagement, gets stripped of customer specifics and prepared as a general example for the Cookbook. The contribution-back motion is shared across all three roles in this curriculum. Your job as the Developer is technical readiness: the focused code, the example, the test, the assumptions, and the rights check. The engagement context comes from the broader team.

**The contribution-readiness reference**

| **Channel** | **What a maintainer checks** | **Licensing and attribution** | **The example and test bar to clear** |
| :--- | :--- | :--- | :--- |
| Cookbook for a focused example, or the tool or server's own repository for a tool or fix. | That the code does one thing and that they can read it in full. | Confirm that you have the right to contribute code from an engagement, with prior work attributed. | A runnable example plus a test that proves the behavior, not just a description of it. |

<table style="width: 100%; border-collapse: separate; border-spacing: 12px 0; table-layout: fixed; background-color: transparent;">
  <tr style="background-color: transparent;">
    <td style="background-color: #eaf2ef; border: 1.5px solid #2e8466; border-radius: 8px; padding: 16px; vertical-align: top;">
      <div style="color: #2e8466; font-weight: bold; margin-bottom: 8px; line-height: 1.35;">Handles well</div>
      <div style="color: #262522; line-height: 1.55;">A packaged asset needs only the example, test, and rights check to become shared infrastructure others build on.</div>
    </td>
    <td style="background-color: #f6efe4; border: 1.5px solid #c56a2d; border-radius: 8px; padding: 16px; vertical-align: top;">
      <div style="color: #c56a2d; font-weight: bold; margin-bottom: 8px; line-height: 1.35;">Adds cost or complexity</div>
      <div style="color: #262522; line-height: 1.55;">Clearing the maintainer bar and the licensing gate is real work on top of making the code run for you.</div>
    </td>
    <td style="background-color: #f8e9e8; border: 1.5px solid #b8443d; border-radius: 8px; padding: 16px; vertical-align: top;">
      <div style="color: #b8443d; font-weight: bold; margin-bottom: 8px; line-height: 1.35;">Use a different approach</div>
      <div style="color: #262522; line-height: 1.55;">When code carries an engagement licensing constraint you cannot clear, do not contribute it: escalate to the owner instead.</div>
    </td>
  </tr>
</table>

### Watch Out!

**The pull request a maintainer could not verify**

> [!Tip]
> Setup
>
> You opened the contribution with the exact code that solved your problem. This was the natural choice because it worked in your case and it was accessible. It worked for you, but that is precisely why it was missing everything a stranger needs to trust it.

This is an exchange from an internal channel so you can hear how a maintainer explains the silence on a pull request.

**The exchange**

```
**Developer:** My PR has been open three weeks with no review. The code works, I use it every day. What is the holdup?
**Maintainer:** It probably works for you. The problem is I can’t tell. There is no test I can run, no example that proves the behavior, and nothing saying what it assumes about the environment.
**Developer:** So, you want me to add a test and an example?
**Maintainer:** Yes. A contribution a reviewer cannot verify sits at the back of the queue until someone has time to reconstruct what it does. A focused PR with a test and an example gets reviewed fast because there is nothing left for me to reverse-engineer.
```

> [!Caution]
> Why it broke
>
> The code was correct. The contribution stalled because the maintainer could not verify it without reconstructing the developer's work. That gap is easy to overlook because the author already has the missing context. The example, the test, and the assumptions statement all seem obvious to the person who created the code. To the maintainer, however, they are not, and a reviewer who must reconstruct intent will always do it last.

> [!Caution]
> What to Watch Out for
>
> A pull request stalls on what the reviewer cannot verify. Before opening a contribution, add the example that shows it running, the test that proves the behavior, and the short statement naming what it assumes. Those three features are what move a contribution from the back of the queue to a fast review, because they leave the maintainer nothing to reverse-engineer.

## Requirements and Lifecycle

### From business requirements to functional and infrastructure requirements

The deployment-platform decisions that follow all assume the requirements already exist: the residency rule, the latency target, the identity model. This screen is where those requirements come from: turning a business problem into the functional and infrastructure requirements a deployment decision can be defended against.

### Capturing functional requirements from a business problem

A functional requirement names what the system must do, stated with enough detail to check. A business problem (e.g. "help support agents answer faster") is not yet a requirement; the functional requirements derive from it (e.g. "classify each ticket into one of four queues; draft a reply citing the relevant policy; never auto-send without human approval"). The discipline is to write each as a checkable statement of behavior. A vague goal cannot be designed against or verified, while a specific one becomes a line in an eval and a criterion at review.

### Deriving infrastructure requirements

Infrastructure requirements are the non-functional constraints the deployment must satisfy. Most of them are not stated in the business problem; instead, you derive them by asking the questions the business problem implies. Latency: how fast does a response need to be, measured where the user is? Scale: how many requests, and at what peak? Residency: where must the data be processed, and under which regulation? Identity: who acts, under what credentials, and what must be auditable? Latency, scale, residency, and identity are the infrastructure requirements that most often decide the deployment platform, and they are easiest to capture at the start, before a platform is chosen for other reasons.

### Documenting requirements so a decision can be defended

Requirements are written down because the deployment decision will be reviewed by people who did not gather them. A short requirements record covering the functional behaviors, the infrastructure constraints, and the regulation each constraint comes from lets you defend a platform choice as following from the requirements rather than from familiarity. This record is the input the next screen's deployment decision reads from.

<table style="width: 100%; border-collapse: separate; border-spacing: 12px 0; table-layout: fixed; background-color: transparent;">
  <tr style="background-color: transparent;">
    <td style="background-color: #eaf2ef; border: 1.5px solid #2e8466; border-radius: 8px; padding: 16px; vertical-align: top;">
      <div style="color: #2e8466; font-weight: bold; margin-bottom: 8px; line-height: 1.35;">Handles well</div>
      <div style="color: #262522; line-height: 1.55;">Turning a business problem into checkable functional and infrastructure requirements before any platform is chosen.</div>
    </td>
    <td style="background-color: #f6efe4; border: 1.5px solid #c56a2d; border-radius: 8px; padding: 16px; vertical-align: top;">
      <div style="color: #c56a2d; font-weight: bold; margin-bottom: 8px; line-height: 1.35;">Adds cost or complexity</div>
      <div style="color: #262522; line-height: 1.55;">Eliciting infrastructure constraints up front takes a scoping conversation the team is tempted to skip.</div>
    </td>
    <td style="background-color: #f8e9e8; border: 1.5px solid #b8443d; border-radius: 8px; padding: 16px; vertical-align: top;">
      <div style="color: #b8443d; font-weight: bold; margin-bottom: 8px; line-height: 1.35;">Use a different approach</div>
      <div style="color: #262522; line-height: 1.55;">For a throwaway prototype with no review and no regulated data, lightweight notes are enough.</div>
    </td>
  </tr>
</table>

### Systems lifecycle for Claude applications

The requirements you just captured are the first phase of a longer arc. This screen names that arc as the systems lifecycle, so the deployment, versioning, and boundary work in the rest of this module sits in the right phase rather than arriving as unrelated tasks.

**The lifecycle phases applied to a Claude application**

A Claude application moves through the same lifecycle as any engineered system, with the model work mapped onto it:

1. Requirements: capture functional and infrastructure needs
2. Design: choose the platform, the model, and the trust boundaries
3. Build: write the agent, tools, and prompts
4. Test: evals, unit, integration, and end-to-end checks
5. Deploy: pin the version, gate promotion on the eval
6. Operate: instrument cost, latency, and errors; enforce guardrails
7. Iterate: feed production findings back into requirements

The phases are the same ones the earlier modules taught one at a time. Identifying them as a lifecycle is what shows how they connect.

**Gating between phases**

A gate is a decision to move from one phase to the next, and it is where a regulated engagement keeps control. You do not move from design to build until the platform satisfies the residency requirement; you do not move from deploy toward full production until the new version clears the eval against the pinned baseline. Placing engineering work in the right phase, and refusing to skip a gate, is what keeps a Claude application reviewable.

<table style="width: 100%; border-collapse: separate; border-spacing: 12px 0; table-layout: fixed; background-color: transparent;">
  <tr style="background-color: transparent;">
    <td style="background-color: #eaf2ef; border: 1.5px solid #2e8466; border-radius: 8px; padding: 16px; vertical-align: top;">
      <div style="color: #2e8466; font-weight: bold; margin-bottom: 8px; line-height: 1.35;">Handles well</div>
      <div style="color: #262522; line-height: 1.55;">Placing each piece of engineering work in the lifecycle phase it belongs to, with a defined artifact and gate.</div>
    </td>
    <td style="background-color: #f6efe4; border: 1.5px solid #c56a2d; border-radius: 8px; padding: 16px; vertical-align: top;">
      <div style="color: #c56a2d; font-weight: bold; margin-bottom: 8px; line-height: 1.35;">Adds cost or complexity</div>
      <div style="color: #262522; line-height: 1.55;">Gating between phases adds checkpoints a team under deadline is tempted to skip.</div>
    </td>
    <td style="background-color: #f8e9e8; border: 1.5px solid #b8443d; border-radius: 8px; padding: 16px; vertical-align: top;">
      <div style="color: #b8443d; font-weight: bold; margin-bottom: 8px; line-height: 1.35;">Use a different approach</div>
      <div style="color: #262522; line-height: 1.55;">A one-off experiment may collapse phases, but a regulated deployment cannot.</div>
    </td>
  </tr>
</table>

## Deployment and Versioning

### Choosing where a Claude workload runs and versioning what ships

A packaged asset and a contributed one are both merely code until something runs them. The asset now faces a different question: where it runs and how to lock its version, so an upstream change does not become an untracked change in production. That platform decision is rarely about technical merit alone. In practice, it is usually shaped by where the customer already has cloud infrastructure, identity management, and compliance agreements in place. The first question is usually about which platform the customer already trusts and operates on.

### The customer's cloud usually determines the platform

The deployment platform is the environment where the Claude workload runs. The same model can run in several deployment environments, and the customer's existing cloud usually determines which one. The first-party Claude API is Anthropic's own environment and typically receives new features first. Claude Platform on AWS is accessed through the customer's AWS account using Anthropic's own model IDs and lifecycle; inference is Anthropic-operated, outside the AWS boundary. Amazon Bedrock offers two integrations: Claude in Amazon Bedrock uses the Messages API at /anthropic/v1/messages with broad feature parity; confirm any feature-specific requirements against the Bedrock documentation, as a features-not-supported list exists, while Claude on Amazon Bedrock (legacy) uses the InvokeModel/Converse APIs with ARN-versioned identifiers. Google Vertex AI does the same inside Google Cloud. Third-party platforms, such as Microsoft Foundry, embed Claude inside a product the customer already uses. Microsoft Foundry offers Claude in two hosting forms: Hosted on Azure (currently Claude Opus 4.8, Claude Sonnet 5, and Claude Haiku 4.5, with inference running end-to-end on Azure infrastructure, generally available) and Hosted on Anthropic (all other Foundry Claude models, with inference on Anthropic-operated infrastructure). Residency assumptions for regulated customers depend on the hosting form of the specific model. Confirm the hosting form and the current model split with Microsoft at build time.

**Identity and data residency are important for security**

Identity and data location are answered by the platform, not your code. Bedrock uses AWS identity and keeps data inside the customer's AWS boundary; Vertex uses Google Cloud identity and boundary. Both offer regional routing when residency is a constraint. Matching the platform to the customer's existing compliance agreement avoids a data-residency review from scratch.

**Pin the version so an upstream model change is not a silent production change**

Versioning is what keeps a model or prompt change from becoming a silent change in production. Every Claude model ID points to a specific model snapshot. Aliases such as Opus and Sonnet are convenient, but they evolve over time and may resolve to different versions across deployment platforms. A pinned full model ID resolves to a fixed snapshot. Pin the specific model version rather than the alias, so an upstream model update is a deliberate choice rather than a silent production change. Then version the prompt and the asset alongside the code. Finally, keep the prior version available so the regression can be rolled back. An unpinned deployment makes every upstream model update an untracked change to your output.

```
The first line follows a moving alias. The second pins the snapshot.

# Pre-4.6 example: a convenience alias can resolve to a new
# version without you knowing
model = "claude-haiku-4-5"

# Pre-4.6 pinned snapshot: the version is fixed until you change this line
model = "claude-haiku-4-5-20251001"
```

For Claude 4.6 and later, the model ID alone pins to a specific snapshot; for earlier models, the ID plus a date suffix is required. Verify the current convention at platform.claude.com at build time.

**Promote a version through the eval**

Gate promotion on the eval suite. Send a new version to a portion of traffic, compare against the pinned baseline, and promote or roll back on the result. This is where the eval stops being a one-time test and becomes the deployment gate.

**The deployment-platform decision table**

| **Platform** | **Identity and data model** | **When to choose it** | **How versioning is pinned** |
| :--- | :--- | :--- | :--- |
| First-party Claude API | Anthropic identity and terms. | The customer has no binding cloud or residency constraint and wants the newest capabilities. | Pin the full model ID and keep the prior snapshot. |
| Claude Platform on AWS | Anthropic identity and terms, accessed through the customer's AWS account; inference is Anthropic-operated outside the AWS boundary. Model lifecycle follows Anthropic's deprecation schedule. | The customer is on AWS but wants Anthropic model IDs, lifecycle, and feature parity with the first-party API. | Pin using the same model ID format as the Claude API (for example, `claude-opus-4-6`). Lifecycle follows Anthropic's schedule. (Confirm at publish time.) |
| Claude in Amazon Bedrock | Messages API at `/anthropic/v1/messages`, broad feature parity with the first-party API; confirm feature-specific requirements against the Bedrock documentation. Data stays inside the customer's configured AWS boundary. | The customer is on AWS, wants broad feature parity with the first-party API (confirm feature-specific requirements), and holds a compliance posture there. | Pin the full model ID using the `anthropic.` prefix format. Partner retirement dates differ from Anthropic's schedule. Confirm at publish time. |
| Claude on Amazon Bedrock (legacy) | AWS identity and billing, InvokeModel/Converse APIs with ARN-versioned model identifiers. | The customer is on an existing Bedrock integration using InvokeModel or Converse and has not migrated to the Messages API. | Pin via ARN-versioned model identifiers per Bedrock's versioning controls. |
| Google Vertex AI | Google Cloud identity, Identity and Access Management (IAM), and billing, with regional or global endpoints for residency. | The customer is on Google Cloud and holds a compliance posture there. | Pin the full model ID before rollout using Vertex's model ID format. Partner retirement dates differ from Anthropic's schedule. |
| Third-party platform | The wrapping product's identity and billing model. Note: Claude in Microsoft Foundry offers two hosting forms: Hosted on Azure (currently Opus 4.6, Sonnet 5, and Haiku 4.5; inference end-to-end on Azure) and Hosted on Anthropic (all other Foundry Claude models). Confirm residency and compliance terms with Microsoft before selecting this path for a regulated customer. | The customer already runs the platform that embeds Claude. | Pin per the platform's versioning controls. |

<table style="width: 100%; border-collapse: separate; border-spacing: 12px 0; table-layout: fixed; background-color: transparent;">
  <tr style="background-color: transparent;">
    <td style="background-color: #eaf2ef; border: 1.5px solid #2e8466; border-radius: 8px; padding: 16px; vertical-align: top;">
      <div style="color: #2e8466; font-weight: bold; margin-bottom: 8px; line-height: 1.35;">Handles well</div>
      <div style="color: #262522; line-height: 1.55;">Matching the platform to the customer cloud and pinning the version keeps a migration reviewable and a rollback possible.</div>
    </td>
    <td style="background-color: #f6efe4; border: 1.5px solid #c56a2d; border-radius: 8px; padding: 16px; vertical-align: top;">
      <div style="color: #c56a2d; font-weight: bold; margin-bottom: 8px; line-height: 1.35;">Adds cost or complexity</div>
      <div style="color: #262522; line-height: 1.55;">Pinning, retaining prior versions, and gating promotion on the eval add release-process overhead to every deployment.</div>
    </td>
    <td style="background-color: #f8e9e8; border: 1.5px solid #b8443d; border-radius: 8px; padding: 16px; vertical-align: top;">
      <div style="color: #b8443d; font-weight: bold; margin-bottom: 8px; line-height: 1.35;">Use a different approach</div>
      <div style="color: #262522; line-height: 1.55;">For a throwaway prototype that never touches production, a moving alias is fine: pinning is for what ships.</div>
    </td>
  </tr>
</table>

### Watch Out!

**The deployment that broke when the model alias moved**

> [!Tip]
> Setup
>
> You shipped against the alias that pointed at the recommended version, because that was the convenient default and it gave you the latest model for free. It worked. Then the alias advanced, and what was free turned out to have a price.

This is a trace excerpt from a production log, the kind you would scroll back through after an incident. It shows the day the output shape changed and why there was nothing to roll back to.

```
The log

--:  deploy: model="opus"  status=ok
--:  alias advanced -> new opus version (no app change)
--:  parser: KeyError "summary" in response payload
--:  Error: output shape changed; downstream parse failed
--:  rollback attempted -> no pinned prior version retained
--:  incident: hotfix parser; root cause = unpinned deployment
```

> [!Caution]
> Why it broke
>
> The application never changed, but the alias did. No pinned prior version had been retained, so there was nothing to roll back to. The hotfix repaired the parser but left the unpinned deployment in place.

> [!Caution]
> What to Watch Out for
>
> An alias resolves to a moving target; a pinned full model ID is a fixed snapshot. Pin the full model ID so an upstream update is something you adopt on purpose. Keep the prior pinned version available so a regression is a rollback rather than a hotfix. Gate the new version through your eval before you promote it, so the output-shape change shows up in a test run instead of in production.



