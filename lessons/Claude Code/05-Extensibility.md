# Extensibility

## MCP servers: ticketing, error logs, internal systems

<span style="font-size: 1.25em;">_MCP connects Claude Code to your client's systems._</span>

By the end of this lesson you can connect Claude Code to a client's ticketing, error monitoring, or internal API and explain the connection model to the client's platform team in terms they'll understand.

### The connection model

<span style="font-size: 1.15em;">_MCP reaches outside the terminal to connect Claude to the client's tools_</apan>

Claude Code ships with tools for reading files, running code, and searching the web. MCP is the standard that lets you add more, specific to the client's environment, specific to the engagement.

MCP (Model Context Protocol) is an open standard for connecting Claude to external systems. When you install an MCP server, you're giving Claude three new categories of capability in that environment. The model stays the same; what it can reach changes.

| | |
| :-- | :-- |
| <span style="font-size: 1.8em;">**01**</span><br><br><span style="font-size: 1.2em;">**Tools**</span><br><br>Actions Claude can take in the external system: creating a ticket, querying a database, triggering a pipeline run. The model decides which tool to call and what to pass it. | <span style="font-size: 1.8em;">**02**</span><br><br><span style="font-size: 1.2em;">**Resources**</span><br><br>Data Claude can read from the external system: open tickets, recent error logs, API schemas. Loaded into context on demand, not constantly. |
| <span style="font-size: 1.8em;">**03**</span><br><br><span style="font-size: 1.2em;">**Prompts**</span><br><br>Reusable context templates the server exposes, such as a standardised preamble that loads the client's API documentation before any coding task. | <span style="font-size: 1.8em;">**04**</span><br><br><span style="font-size: 1.2em;">**Scoping**</span><br><br>MCP servers can be project-level (one repo), user-level (one developer), or org-level (all developers). The right scope depends on whether this is personal setup or a team deployment. |
| | |

### Installation

<span style="font-size: 1.15em;">_One install command—config placement determines scope_</span>

The install pattern is consistent across all MCP servers. Where the config file lands is what changes.

Run `claude mcp add` followed by the server name and any configuration the server requires. For `--scope project`, Claude Code writes the result to `.mcp.json`; the default local scope writes to `~/.claude.json`. Three real examples from the Activation Plan starter kit:

```bash
# Ticketing - pull issue context before writing a fix
claude mcp add linear

# Browser automation and end-to-end testing
claude mcp add --transport stdio playwright -- npx @playwright/mcp@latest

# Verify the server loaded and check what tools it exposed
/mcp
```

After installation, run `/mcp` at the start of any session to see the connected MCP servers and the tools they expose. That list is what Claude can actually reach in the current session.

Config placement: `.mcp.json` in the project root scopes the server to that project only. `~/.claude.json` with `--scope user` makes it available across all of that developer's projects. **Note:** the default scope (local) also writes to `~/.claude.json` but keys it to the current project; the server won't appear elsewhere. Org-level deployment goes through `managed-settings.json` (covered in the next lesson).

### Engagement scenarios

<span style="font-size: 1.15em;">_Three MCP archetypes that come up on nearly every activation_</span>

The Activation Plan pre-kickoff checklist asks: what MCP servers does this client already use? These are the categories to inventory.

| | | |
| :-- | :-- | :-- |
| <span style="font-size: 1.8em;">**01**</span><br><br><span style="font-size: 1.2em;">**Ticketing systems**</span><br><br>Jira, Linear, GitHub Issues. Claude pulls ticket context before writing a fix: no copy-paste, no context loss. The "Ticket to PR" pattern from the Enablement Deck starts here. Without this connection, developers manually copy ticket descriptions into the session. | <span style="font-size: 1.8em;">**02**</span><br><br><span style="font-size: 1.2em;">**Error logs and observability**</span><br><br>OTel, Datadog, Sentry. Claude reads recent error traces directly when debugging. This compresses the loop between "error appeared in production" and "fix is underway." For clients doing modernisation work, this is high signal. | <span style="font-size: 1.8em;">**03**</span><br><br><span style="font-size: 1.2em;">**Internal systems**</span><br><br>Private APIs, internal databases, service catalogues, Confluence, proprietary tooling. These require a custom or client-built MCP server, or the MCP tunnel when the system isn't reachable from the developer's laptop. Both are covered in Lesson 5.3. |
| | | |

### The framing that lands with clients

<span style="font-size: 1.15em;">_MCP is a context amplifier, not a data integration project_</span>

The business case for MCP isn't `"Claude can read Jira."` It's something sharper than that.

When a developer fixes a bug today, they open the ticket, read the description, switch to the editor, open the relevant files, then start typing. MCP collapses the first two steps: when the ticket context is already loaded into Claude's session, the developer starts with Claude already oriented — no context loss.

#### What this means for security and platform teams

For the security and platform teams, the framing depends on how the MCP server authenticates. For OAuth-scoped servers, Claude inherits the user's own permissions — the MCP server surfaces what the user already has access to, nothing more. That distinction usually resolves the "what can Claude see?" question in the security review. But servers using static API keys, service accounts, or `headersHelper` credentials may grant access that differs from the user's own. Always confirm how the MCP server authenticates and what tools it exposes before deploying to a team.

> [!Important]
> <small>FRAMING FOR THE CLIENT CONVERSATION</small>
>
> Properly scoped MCP servers should not grant access beyond what the user or configured credential can reach. It reduces how many context switches developers make to get there. Always review how the MCP server authenticates and what it exposes before deployment.

### Engagement scenario

**The platform team has a constraint**: `You're setting up MCP on Day 3 of the activation. The client's platform team flags a restriction.`

![Engagement Scenario](images/mcp_engagement_scenario.png)

## Approved-server governance and the MCP allowlist

<span style="font-size: 1.25em;">_Developers will ask. You need a defensible answer._</span>

By the end of this lesson you can configure the MCP server allowlist, explain the approval workflow to a client's security team, and handle the most common objection.

### Defense in depth

<span style="font-size: 1.15em;">_MCP governance sits inside a layered security model you already brief clients on_</span>

Anthropic's defense-in-depth framework has five layers. MCP allowlisting sits in Layer 02, the platform and runtime layer. It's not a standalone MCP policy; it's part of how Claude Enterprise handles all connector access.

| | |
| :-- | :-- |
| <span style="font-size: 1.8em;">**01**</span><br><br><span style="font-size: 1.2em;">**Identity & environment**</span><br><br>SSO, SCIM provisioning, RBAC, and network access controls. The enterprise perimeter you already brief clients on — who gets access and at what level. Owned by the client's own infrastructure. | <span style="font-size: 1.8em; color: #cc6d50;">**02**</span><br><br><span style="font-size: 1.2em;color: #cc6d50;">**Platform & runtime ← this lesson**</span><br><br>Where a request actually runs: surfaces, sandboxes, egress, and connector consent. MCP allowlisting lives here. Owned jointly — Anthropic controls the platform; your org controls the policy configuration. |
| <span style="font-size: 1.8em;">**03**</span><br><br><span style="font-size: 1.2em;">**Runtime safety**</span><br><br>Anthropic-run classifiers, per-surface system prompts, and usage policy enforcement wrapped around every model call. Catches novel jailbreaks and abuse patterns without requiring a model retrain. | <span style="font-size: 1.8em;">**04**</span><br><br><span style="font-size: 1.2em;">**Model safety**</span><br><br>Safety properties trained directly into the weights — Constitutional AI, RLHF, and trained-in refusal. The layer no system prompt can undo. Owned entirely by Anthropic. |
| <span style="font-size: 1.8em;">**05**</span><br><br><span style="font-size: 1.2em;">**Observability & audit**</span><br><br>Audit logs, Compliance API, OpenTelemetry, and analytics that cut across every other layer. Feeds the client's SIEM, legal hold, and compliance stack. Covered in the Administration module. | |
| | |

This lesson focuses on Layer 02. The specific controls you configure — the MCP server allowlist and egress domain restrictions — sit inside the platform and runtime layer, sandwiched between the identity perimeter the client already owns and the Anthropic-managed safety stack below. That framing matters in the security conversation: you're not asking a client to trust Claude with ungoverned connector access. You're showing them exactly where their policy levers sit within a stack that has four other layers running independently of what any developer can install.

### Two control planes

<span style="font-size: 1.15em;">_User-installed and org-deployed servers are governed differently_</span>

Within Layer 02, there are two distinct mechanisms for getting an MCP server into a developer's environment — and they're governed differently. Understanding this split is essential for the security conversation. Most clients conflate the two, which is why the CISO's question ("can developers install anything?") has a nuanced answer.

| | |
| :-- | :-- |
| <span style="font-size: 0.8em;">**USER-INSTALLED**</span><br><br><span style="font-size: 1.4em;">**Developer-controlled via local .mcp.json**</span><br><br>A developer can add a server to their own `~/.claude.json` or the project's `.mcp.json`. This affects only their own sessions. It's the developer's responsibility. To fully restrict user installs, the admin sets the override policy to deny in `managed-settings.json`. | <span style="font-size: 0.8em;">**ORG-DEPLOYED**</span><br><br><span style="font-size: 1.4em;">**Two mechanisms: allowlist filtering and managed deployment**</span><br><br><span style="font-size: 1.2em;">**Deployment:**</span> `managed-mcp.json` pushes fixed servers to every user automatically — no user action required.<br><br><span style="font-size: 1.2em;">**Filtering:**</span> `allowedMcpServers` in `managed-settings.json` controls which servers developers are allowed to add themselves. Setting `allowManagedMcpServersOnly: true` enforces the filter. These are separate controls — configure both on Day 0. |
| | |

### Day 0 configuration

<span style="font-size: 1.15em;">_The allowlist goes into managed-settings.json before kickoff_</span>

The 30-Day Activation Plan lists MCP allowlist setup as a minimum org-level prerequisite for Day 0, alongside SSO/SCIM and spend reporting. It's not optional. Without an enforced MCP policy, developers may be able to connect to unapproved MCP servers — which creates the security exposure the client is trying to avoid.

Work with the client's platform or security team to define the initial approved server list. The pre-kickoff MCP inventory (what servers the team already uses) feeds directly into this. A practical starting set for most code-focused activations:

```json
// managed-settings.json — MCP allowlist section
// allowedMcpServers entries must be objects, not bare strings
{
    "allowManagedMcpServersOnly": true, // prevents unapproved installs
    "allowedMcpServers": [
        { "serverUrl": "https://api.github.com/*" }, // code context, PR operations
        { "serverUrl": "https://linear.app/mcp/*" }, // ticketing and issue context
        { "serverCommand": ["npx", "-y", "@playwright/mcp@latest"] }, // browser automation / testing
        { "serverUrl": "https://*.client-internal.com/*" } // internal systems
    ]
}
```

The `allowManagedMcpServersOnly: true` flag is the answer to the CISO's question. With it set, developers cannot install servers outside the approved list. Without it, the list is advisory, not enforced.

### Engagement rhythm

<span style="font-size: 1.15em;">_New server requests need a standing review process, not an ad hoc one_</span>

The initial allowlist won't cover everything the team needs by Week 3. Build the review process in Week 1 so requests don't stall the engagement.

| | |
| :-- | :-- |
| 1 | <span style="font-size: 1.4em;">**Pre-kickoff: inventory what already exists**</span><br><br>The consultant and CoE lead catalogue MCP servers the team uses today. These go straight onto the approved list with no new evaluation needed. Unvetted servers get flagged for review. |
| <span style="color: #cc6d50;">2</span> | <span style="font-size: 1.4em;">**Day 0: set the initial allowlist with the security team**</span><br><br>Work with IT or the platform team to load the approved server list into `managed-settings.json`. Confirm egress domains. Set the user install policy. Share the pre-kickoff inventory 48 hours in advance so the team arrives ready to confirm, not to review for the first time. It should take under an hour. |
| 3 | <span style="font-size: 1.4em;">**Weekly: CoE touchpoint includes connector approvals**</span><br><br>The standing weekly CoE meeting covers governance. New connector requests go here. The CoE lead owns the decision; the security team reviews the egress domain for anything non-standard. Turnaround should be same-week, not same-month. |
| | |

## MCP Tunnel - Bridging Local Development

<span style="font-size: 1.25em;">_The client's internal API isn't reachable. The relay is._</span>

By the end of this lesson you know when to use the remote MCP relay pattern, how to set it up, and how to explain it to a client's platform team without it becoming a security escalation.

### The last-mile problem

<span style="font-size: 1.15em;">_Allowlisted but unreachable: when the remote MCP relay bridges the gap_</span>

The MCP allowlist controls what can be approved. The relay controls what's actually reachable. They solve different problems.

The scenario comes up on nearly every enterprise engagement: a developer needs Claude Code to connect to an internal REST API, a database, or a private service. The system is legitimate and already approved for MCP access. But it only accepts connections from inside the corporate network, and Claude Code is running on a developer's laptop that can't directly reach it.

Without this MCP tunnel, the developer copies API responses manually into the Claude Code session. That works for a one-off task. It's unsustainable for a team, and it defeats the purpose of the MCP connection.

> [!Important]
> <small>WHAT THE RELAY ACTUALLY DOES</small>
>
> The remote MCP relay is a relay between Claude Code and an MCP server running inside the client's network. The developer's laptop talks to the relay endpoint; the relay endpoint talks to the internal system. The security boundary stays intact.

The relay pattern is the same concept as a reverse proxy or API gateway: the relay sits between the client and the target system, and only the defined protocol passes through it.

### Architecture decision

<span style="font-size: 1.15em;">_Use the relay pattern only when direct connection isn't possible_</span>

The relay adds latency and an extra point of failure. Don't use it if a direct connection works.

| | |
| :-- | :-- |
| <span style="font-size: 0.8em;">**DIRECT MCP CONNECTION**</span><br><br><span style="font-size: 1.4em;">**Target system is reachable from the developer's environment**</span><br><br>SaaS tools (GitHub, Linear, Slack), VPN-accessible systems, or anything the developer's machine can reach directly. Run `claude mcp add` and the connection works. No tunnel needed. | <span style="font-size: 0.8em;">**REMOTE MCP RELAY**</span><br><br><span style="font-size: 1.4em;">**Target system is behind a network boundary the laptop can't cross**</span><br><br>Internal APIs that only accept requests from specific subnets, air-gapped environments, or systems where the client won't open a firewall rule for developer laptops. The relay bridges the gap without exposing the target internal system directly to every developer laptop. |
| | |

### Configuration

Connecting to internal systems: the relay pattern and the security conversation
The 30-Day Activation Plan introduces this connection pattern in Week 1 as part of Claude Code 101. Treat it as standard setup for any client with internal systems, not an edge case.

The approach: deploy an MCP server inside the corporate network where it can reach the internal system, then expose it via an HTTP or SSE endpoint that developers can reach over VPN. Claude Code connects using the sse or http transport. Configure it in .mcp.json:

```json
// Configure in .mcp.json — connect to an MCP server running inside the corporate network
{
    "mcpServers": {
        "internal-api": {
            "type": "sse",
            "url": "https://mcp.client-internal.com/sse"
        }
    }
}
```
```bash
# Or via the CLI
claude mcp add --transport sse internal-api https://mcp.client-internal.com/sse
```

### What the platform team needs to know

The MCP server carries only MCP protocol traffic — tool call requests and responses. It does not give Claude Code general network access to the internal environment. The MCP server running inside the network controls exactly which tools and resources are exposed. The security boundary is at the MCP server.

Authentication to the MCP endpoint can go through OAuth (for HTTP/SSE servers that support it), static headers (API keys or bearer tokens), or headersHelper for custom authentication such as internal SSO, Kerberos, or short-lived tokens. OAuth is common when the client's identity platform supports it, but not all internal systems require it. Configure authentication in .mcp.json to match how the MCP server expects credentials.

## Skills: packaging reusable task expertise

<span style="font-size: 1.25em;">_The client's standards live in a document nobody reads._</span>

By the end of this lesson you can explain what a Skill is, describe how Claude discovers and loads one, and identify three types of Skill opportunity on an activation engagement.

### Concept

<span style="font-size: 1.15em;">_A Skill is expertise Claude can discover and load only when it's relevant_</span>

Three weeks into an activation, the engineering team wants Claude Code to follow their internal API documentation standard every session. Without a Skill, Claude forgets what happens between sessions. With one, it never has to be told again.

A Skill is a folder of files — instructions, scripts, templates — that gives Claude a specific, reusable capability. The critical property: Claude loads a Skill only when it's relevant to the current task. A Skill that isn't needed for the current session adds no overhead. It simply isn't loaded.

Two categories cover most activation use cases:

| | |
| :-- | :-- |
| <span class="font-size-lg" style="font-size: 1.15em;">**Capability Skills**</span><br><br>Things Claude can't do well without specialised instructions: generating Office files in the client's format, complex PDF layouts, applying proprietary output templates. A PDF generation Skill doesn't load when a developer is writing tests — it activates when Claude is asked to produce a formatted document. | <span class="font-size-lg" style="font-size: 1.15em;">**Knowledge Skills**</span><br><br>Organisation-specific workflows and standards: coding conventions, compliance language, PR description requirements, incident post-mortem format, brand guidelines. If you've ever watched a team ignore a standard because nobody had time to look it up, this is what solves it — the standard lives exactly where Claude can find it, and activates when someone writes a function signature. |
| | |

The pattern that makes Skills valuable
A Skill turns a document nobody reads consistently into something Claude applies automatically. The client's TypeScript standard, their PR template, their security review checklist. These exist. They're just not in Claude's context. A Skill puts them there.

### Structure

<span style="font-size: 1.15em;">_Skill anatomy: a folder, a `SKILL.md`, and optionally bundled files_</span>

The minimum viable Skill is a single file. Real engagement Skills usually bundle a few more.

```bash
# Minimum structure
my-skill/
└── SKILL.md      ← required
```

The `SKILL.md` has two parts: YAML frontmatter (the metadata Claude reads first) and the body (the instructions Claude loads if the Skill is relevant).

```yaml
# SKILL.md structure
---
name: API Documentation Standards
description: Apply client's internal REST API documentation format when writing or reviewing any endpoint specification
---

## Overview
[Instructions Claude follows when this skill loads]

## Format Requirements
[Specifics: header format, field definitions, required fields]

## Example
[One worked example of a compliant spec]

Read ./endpoint-template.yaml for the full schema
```

For comprehensive reference material, bundle it in linked files. Claude only reads them when needed, not on every task:

```bash
# Richer structure with bundled resources
api-docs-skill/
├── SKILL.md
├── endpoint-template.yaml   ← loaded on demand
├── example-spec.yaml        ← loaded on demand
└── apply_template.py        ← run if needed
```

### Mechanics

<span style="font-size: 1.15em;">_Progressive disclosure: how Claude decides which Skills to load_</span>

Claude doesn't load everything. It works through three steps before touching a Skill's content.

| | | |
| :-- | :-- | :-- |
| <span class="font-size-lg" style="font-size: 1.25em;">**Step 1: Scan**</span> | Skill name + description only | Decides: relevant to this task? |
| <span class="font-size-lg" style="font-size: 1.25em;">**Step 2: Load**</span> | Full SKILL.md body | Reads instructions and examples |
| <span class="font-size-lg" style="font-size: 1.25em;">**Step 3: Fetch**</span> | Linked bundled files (if needed) | Accesses templates, specs, scripts |
| | | |

This is why the description field is the most important line you'll write. If it doesn't accurately describe when to use the Skill, Claude won't load it when it should, or will load it when it shouldn't.

The practical implication for engagement work: a Skills library of 10–20 specialist Skills doesn't degrade performance on every task. The overhead is proportional to relevance, not to the number of Skills installed.

Contextual loading is the default, but it's not the only path. Users can also invoke a Skill directly by name (e.g. `/skill-name`) or reference it explicitly in their instructions to force it into context regardless of Claude's relevance assessment.

### Engagement application

<span style="font-size: 1.15em;">_Three Skill opportunities in a 30-day activation_</span>

The pre-kickoff discovery checklist asks you to inventory what Skills, MCPs, and plugins the client already has. What you don't find in that inventory, you build. These three patterns cover most of what you'll build.

| | | |
| :-- | :-- | :-- |
| <span class="font-size-lg" style="font-size: 1.15em;">**Pattern 1: Refined through experience**</span><br><br>Repeated tasks with established quality standards: code review format, incident post-mortem, PR description requirements. The client's team already knows what good looks like. Package it. | <span class="font-size-lg" style="font-size: 1.15em;">**Pattern 2: Quality depends on materials**</span><br><br>Tasks where Claude needs reference material to do the work well: API spec format, regulatory compliance language, internal service catalogue, data model conventions. Bundle the reference; Claude reads it when needed. | <span class="font-size-lg" style="font-size: 1.15em;">**Pattern 3: Capability gap**</span><br><br>Something Claude can't do well without specialised instructions: generating documents in a client-specific format, applying a proprietary schema, running a custom validation step. A Capability Skill with bundled scripts and templates closes the gap. |
| | | |

When to build vs when to install: The Activation Plan places the skills inventory at pre-kickoff and the depth work on Week 2. By Week 4, the Skills you've built get packaged into the team plugin. Don't build Skills from scratch if the client or Anthropic's marketplace already has one. Check first.

### Worked example

<span style="font-size: 1.15em;">_One client, three Skill opportunities — spotted in Week 2_</span>

A UK financial services firm, 50-person engineering team. Week 2 of a 30-day activation. Three observations, three patterns, three builds.

| | | |
| :-- | :-- | :-- |
| <span class="font-size-lg" style="font-size: 1.15em;">**Situation 1 — Pattern 1**</span><br><br>Every morning, two senior engineers write post-incident reports in the format the firm's risk committee requires. Junior engineers copy it imperfectly. Claude has been writing the reports but produces inconsistent severity classifications.<br><br>**Pattern 1.** Build a Skill that encodes the severity rubric and the required fields. The inconsistency stops at the source. | <span class="font-size-lg" style="font-size: 1.15em;">**Situation 2 — Pattern 2**</span><br><br>The firm's compliance team has a 90-page API security checklist. Developers validate every new endpoint against it; whoever reviews pastes the relevant sections manually each time.<br><br>**Pattern 2.** Bundle the checklist as a reference file in the Skill. It loads when Claude is asked to review an endpoint. No more manual paste. | <span class="font-size-lg" style="font-size: 1.15em;">**Situation 3 — Pattern 3**</span><br><br>The firm uses ISO 20022 XML for payment messages. When developers ask Claude to write a payment handler, it invents field names that fail the schema.<br><br>**Pattern 3.** Build a Skill that gives Claude the schema, required fields, and a worked example. Claude can't guess this format; it needs the Skill to do the work correctly. |
| | | |

## Authoring Effective Skills

<span style="font-size: 1.25em;">_A developer built a Skill. Claude never loads it._</span>

By the end of this lesson you can author a Skill that Claude correctly invokes, that doesn't over-load context, and that the client's team can maintain after the engagement ends.

### The most important line you'll write

<span style="font-size: 1.15em;">_The description is the trigger. Everything else is secondary_</span>

The scenario is common: a developer builds a well-structured Skill, commits it to the repo, and Claude never loads it. The instructions are fine. The description isn't.

Claude reads the description field in the `SKILL.md` frontmatter to decide whether a Skill is relevant to the current task, before loading any instructions. A vague description means Claude doesn't know when to load it. An over-broad description means Claude loads it on every task and creates context overhead.

| | |
| :-- | :-- |
| **VAGUE: WON'T TRIGGER RELIABLY**<br><br>`description: Apply PR format`<br><br>Claude doesn't know when "PR format" applies. This won't load on PR creation tasks because there's no explicit trigger condition. | **PRECISE: TRIGGERS CORRECTLY**<br><br>`description: Apply the client's internal PR description format when creating or reviewing pull request descriptions. Includes required fields: summary, testing plan, reviewer checklist, and linked ticket.`<br><br>The trigger condition is explicit. Claude knows when to load this, and what it will find when it does. |
| | |

Three rules for a description that works:

| | | |
| :-- | :-- | :-- |
| <span class="font-size-xl" style="font-size: 1.5em;">**01**</span><br><span class="font-size-lg" style="font-size: 1.15em;">**Name the trigger condition**</span><br><br>"When creating or reviewing pull request descriptions" : be explicit, not implied. | <span class="font-size-xl" style="font-size: 1.5em;">**02**</span><br><span class="font-size-lg" style="font-size: 1.15em;">**Name the output or context**</span><br><br>"PR description format": what does the Skill produce or apply? Claude needs to match this against the task. | <span class="font-size-xl" style="font-size: 1.5em;">**03**</span><br><span class="font-size-lg" style="font-size: 1.15em;">**Mention key materials**</span><br><br>"Includes required fields: summary, testing plan, reviewer checklist". Distinctiveness helps Claude choose between multiple similar Skills. |
| | | |

### Authoring principles

<span style="font-size: 1.15em;">_Practices that separate Skills that last from ones that drift_</span>

From the Skills Workshop. These aren't guidelines. They're the difference between a Skill the team maintains and one they quietly stop using.

| | | |
| :-- | :-- | :-- |
| <span class="font-size-lg" style="font-size: 1.15em;">**Keep it focused**</span><br><br>One Skill per workflow. Don't bundle coding standards, PR format, and security review into one file. Focused Skills load precisely; bundled ones load when only one part is needed. | <span class="font-size-lg" style="font-size: 1.15em;">**Start simple**</span><br><br>Core guidance first. Expand based on real usage. The gaps that show up in practice are better guides than the gaps you anticipate. | <span class="font-size-lg" style="font-size: 1.15em;">**Use examples**</span><br><br>One worked example beats three paragraphs of rules. Show Claude what good output looks like. Don't just describe it. |
| <span class="font-size-lg" style="font-size: 1.15em;">**Test incrementally**</span><br><br>Test after each change. Don't build a complex multi-file Skill without verifying the simple version first. A Skill that fails silently is worse than no Skill. | <span class="font-size-lg" style="font-size: 1.15em;">**Version your Skills**</span><br><br>Client standards change. When the client's PR template changes, the Skill needs to change. Treat Skills like code. They belong in version control with the same rigour as production code. | |
| | | |

### Worked example

<span style="font-size: 1.15em;">_Building a TypeScript API documentation Skill from scratch_</span>

A concrete walkthrough of the five-step authoring process for a Knowledge Skill. You'll use this pattern on most GSI engagements.

**Step 1: Identify the trigger** When does this Skill activate? Be specific: "When writing or reviewing TypeScript function signatures, API endpoints, or service interface documentation."

**Step 2: Write the description**

```yaml
description: Apply the client's TypeScript documentation standard when writing or reviewing function signatures, API endpoints, or service interfaces. Includes JSDoc format, required fields, and example patterns.
```

**Step 3: Write the SKILL.md core** State the format. Show one complete example. List required fields. Link to the reference file rather than embedding it.

SKILL.md structure

```yaml
---
name: TypeScript API Documentation Standard
description: Apply the client's TypeScript documentation standard...
---

## Format
All functions and endpoints must use JSDoc with the following
required fields: @param, @returns, @throws, @example.

## Example
[One complete compliant function signature with JSDoc block]

## Required fields
[List of fields and their formats]

Read ./spec-template.yaml for the full endpoint schema.
```

**Step 4: Bundle the reference file**

```bash
api-docs-skill/
├── SKILL.md
└── spec-template.yaml   ← full schema, loaded on demand
```

**Step 5: Test Request** "Document this endpoint" and verify: Did Claude load the Skill? Does the output match the standard? Fix the description if Claude didn't load it. Fix an instruction if Claude loaded it but produced the wrong output.

> [!Important]
> <small>THE SKILL CREATOR SHORTCUT</small>
>
> Prompt Claude: "Build a Skill for [task]. Here are 5 examples." Claude generates the folder structure, `SKILL.md`, and example files. Start here for Knowledge Skills. It's faster than writing from scratch and the description will reflect how Claude actually interprets the task.

## Hooks: pre-task, post-edit, on-failure, on-completion

<span style="font-size: 1.25em;">_"Can we log every bash command Claude runs?"_</span>

By the end of this lesson you can configure a hook for a specific lifecycle event, write the shell command it runs, and explain what hooks are used for in an enterprise deployment.

### Concept

<span style="font-size: 1.15em;">_Hooks are system-level triggers, not Claude instructions_</span>

The client's security team asks: `"Can we automatically log every time Claude runs a bash command?"` The answer is yes: a PostToolUse hook on Bash, one JSON block in the hooks configuration.

Hooks let you register shell commands that run at specific points in Claude Code's lifecycle. They're not Claude instructions. They run regardless of what Claude is doing. A formatting hook fires after every TypeScript file edit. A logging hook fires after every tool call. A blocking hook fires before a protected write and can prevent it entirely.

If you've deployed Jira pre-commit gates or ServiceNow change approval workflows, this is the same enforcement logic: hooks run locally in the developer's session instead of in a shared CI pipeline.

Most hook requirements on a Claude Code activation fall into one of four use cases:

| | | | |
| :-- | :-- | :-- | :-- |
| <span class="font-size-lg" style="font-size: 1.15em;">**Notifications**</span><br><br>Slack message when Claude finishes a task. Sound when Claude is waiting for input. Quality-of-life improvements for developers working across multiple terminals. | <span class="font-size-lg" style="font-size: 1.15em;">**Auto-formatting**</span><br><br>Run Prettier on every .ts edit. Run gofmt on every .go file. The formatting runs whether Claude remembered to apply it or not. | <span class="font-size-lg" style="font-size: 1.15em;">**Logging**</span><br><br>Write a timestamped record of every tool call to a log file or audit system. Useful for compliance, incident review, or debugging unexpected Claude behaviour. | <span class="font-size-lg" style="font-size: 1.15em;">**Enforcement**</span><br><br>Use PreToolUse to check conditions before the action — exit code 2 blocks the tool call entirely. Use PostToolUse to react after: run a linter, log the result, alert on violations. Block writes to protected directories without a ticket reference. |
| | | | |

### Lifecycle events

<span style="font-size: 1.15em;">_Five common events: start here_</span>

Each hook is tied to an event in Claude Code's lifecycle. Choosing the right event is the first configuration decision. These five cover the majority of enterprise use cases — Claude Code supports 20+ total lifecycle events for specialised governance patterns.

| | | |
| :-- | :-- | :-- |
| `PreToolUse` | Before Claude runs any tool | Blocking enforcement: check conditions before the action |
| `PostToolUse` | After a tool run completes | Logging, auto-formatting, side-effect triggers |
| `Notification` | When Claude sends a notification | Alerts: Slack message, desktop sound, webhook ping |
| `Stop` | When the main agent's task completes | Summary logging, cleanup, end-of-session actions |
| `SubagentStop` | When a subagent completes | Subagent result handling, parallel job coordination |
| | | |

**The enforcement distinction:** Use `PreToolUse` when you need to block an action before it happens. Use `PostToolUse` when you need to react after the fact. This distinction matters more than any other configuration decision you'll make with hooks.

**Beyond the five:** Advanced governance patterns use additional events such as `SessionStart` (session initialisation), `PermissionRequest/PermissionDenied` (fine-grained approval workflows), `FileChanged` (sensitive file protection), and     `ConfigChange` (detecting drift). See the full hooks reference in Claude Code documentation for the complete list.

### Configuration

<span style="font-size: 1.15em;">_Hook configuration format: two real examples_</span>

Hooks are configured via the /hooks command or in a hooks.json file in a plugin's hooks directory.

```json
// Example 1: Log every Bash tool call (PostToolUse)
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            // Tool input arrives as JSON on stdin — parse with jq, never use $TOOL_INPUT (it doesn't exist)
            "command": "jq -r '.tool_input.command' | xargs -I {} sh -c 'echo \"[$(date)] Bash: {}\" >> ~/claude-bash-log.txt'"
          }
        ]
      }
    ]
  }
}
```
```json
// Example 2: Auto-format TypeScript after every edit (PostToolUse)
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            // File path arrives as JSON on stdin — parse with jq, never use $EDITED_FILE (it doesn't exist)
            "command": "jq -r '.tool_input.file_path' | { read file; [[ \"$file\" == *.ts ]] && npx prettier --write \"$file\"; }"
          }
        ]
      }
    ]
  }
}
```

The shell command your hook runs determines what Claude does next. That's controlled by exit code.

> [!Important]
> <small>EXIT CODE BEHAVIOUR</small>
>
> **Exit 0:** hook succeeded; Claude Code continues. **Exit 1:** failure, non-blocking — the error surfaces in Claude's context but execution proceeds. **Exit 2:** blocks tool execution. This is the mechanism for enforcement hooks: only a PreToolUse hook exiting with code 2 prevents Claude from proceeding with the tool call.

> [!Note]
> <small>SECURITY CAVEAT FOR THE CLIENT'S PLATFORM TEAM</small>
>
> Hooks run shell commands with the same permissions as the developer's Claude Code session. Hook scripts themselves should be reviewed before deployment. A compromised hook is a lateral movement path. The CoE should own and version all hooks that go into the team plugin.

### Engagement application

<span style="font-size: 1.15em;">_When to build hooks during an activation, and the security caveat_</span>

The Activation Plan introduces hooks in Week 1 (Claude Code 101). This isn't an advanced feature. It's baseline setup. Have an opinion on hooks by Day 3.

**Week 1 / Day 3–5:** Start with two low-risk, high-value hooks. First, a notification hook: a sound or Slack ping when Claude needs input keeps the developer from being blocked. Second, an auto-format hook on the client's primary language: an immediate productivity win and zero additional developer effort.

**Week 4 / packaging phase:** Security logging hooks and custom compliance hooks belong in the team plugin. They're the artifacts that demonstrate Claude Code is running under governance, which the client's security team needs to see before the engagement closes.

## Sub-agents and Parallel Orchestration

<span style="font-size: 1.25em;">_he task is too large for one context. Subagents split the work._</span>

By the end of this lesson you can design a subagent pattern for a multi-step engagement task, explain the context isolation model, and advise a client team on when subagents are the right tool versus parallel Claude instances.

### Architecture decision

<span style="font-size: 1.15em;">_Two orchestration patterns: choose based on need_</span>

The client's security team asks: `"Can Claude Code run a security audit while a developer keeps coding, without one polluting the other's context?"` Yes. That's exactly what subagents are for.

A commonly asked but different question is: `"Can we run two independent features simultaneously?"` That's not subagents — that's parallel Claude instances, and it's a separate pattern.

The two get confused because both involve multiple Claude processes running at the same time. The difference is in how they relate: one pattern has a parent coordinating children and collecting their output; the other has independent instances that never communicate.

### The key distinction

**Subagents return results** to the main agent. Parallel Claude instances **ship work independently**. Getting this wrong is the most common subagent design error on engagement teams.

| | | |
| :-- | :-- | :-- |
| <span class="font-size-lg" style="font-size: 1.25em;">**What it is**</span> | Specialised mini-agents spawned within your session | Independent Claude Code instances in separate terminals |
| <span class="font-size-lg" style="font-size: 1.25em;">**Context**</span> | Isolated sub-context; returns results to main agent | Full independent context per instance |
| <span class="font-size-lg" style="font-size: 1.25em;">**When to use**</span> | Delegate specialised work without polluting main context | Multiple tasks that could each ship as separate PRs; hours of independent work |
| <span class="font-size-lg" style="font-size: 1.25em;">**Coordination**</span> | Automatic: main agent waits for results | Manual: you manage across terminals; TMUX for awareness |
| | | |

If you’ve run engagements with parallel workstreams reporting to a single project lead, you already know this model: the main agent is the PM, subagents are the workstreams, and only the deliverables come back up.

### Structure

<span style="font-size: 1.15em;">_Subagent anatomy: a spec file in the agents directory_</span>

Each subagent is a markdown spec file. Claude reads the description to decide which subagent to spawn for a given task.

Directory structure
```bash
my-project/
├── CLAUDE.md
├── agents/
│   ├── code-reviewer.md      ← each file is a subagent spec
│   ├── security-auditor.md
│   └── researcher.md
└── src/
```

```bash
# security-auditor.md (example spec)
name: security-auditor
description: Scans for SQL injection, XSS, CSRF, and OWASP
             Top 10 vulnerabilities in modified code. Returns
             a structured findings report.
tools: Read, Grep, Bash
```

Two fields drive the subagent pattern. The description is how the main agent decides which subagent to spawn for a given task. Write it the same way you'd write a Skill description: explicit about the trigger condition. The tools list scopes the subagent to exactly what it needs. A security auditor doesn't need Edit or Write access.

### Canonical pattern

<span style="font-size: 1.15em;">_The three-agent security audit: the engagement pattern to propose first_</span>

The most concrete subagent pattern in the source material, and the one most likely to resonate with a client's security team.

> [!NOTE]
> MAIN AGENT<br>
> <span class="font-size-lg" style="font-size: 1.15em;">**Writing the feature**</span><br><br>
> Full context window. Owns the coding task. Spawns the audit subagent when the feature is ready for review.

<p align="center"><span style="color: coral; font-size: 1.2em;">↓</span></p>

> [!TIP]
> AUDIT SUBAGENT<br>
> <span class="font-size-lg" style="font-size: 1.15em;">**Scans for OWASP Top 10**</span><br><br>
> Isolated context. Only sees the code it was given and its own tool results. Returns a structured findings report, not its full reasoning process.

<p align="center"><span style="color: coral; font-size: 1.2em;">↓ findings</span></p>

> [!TIP]
> REMEDIATION SUBAGENT<br>
> <span class="font-size-lg" style="font-size: 1.15em;">**Fixes the vulnerabilities**</span><br><br>
> Receives the findings report. Applies targeted fixes. Returns the remediated code to the main agent.

<p align="center"><span style="color: coral; font-size: 1.2em;">↓</span></p>

> [!NOTE]
> MAIN AGENT<br>
> <span class="font-size-lg" style="font-size: 1.15em;">**Secure feature complete**</span><br><br>
> Main context stayed clean throughout. Receives the final remediated output. The audit detail never entered the main context window.

**Engagement application:** Propose this to clients who need to demonstrate security governance on AI-generated code. The pipeline produces an auditable trail (each subagent's task and output can be logged) without slowing down the main development flow.

### Context isolation

<span style="font-size: 1.15em;">_What the subagent sees, and what happens when it fails_</span>

Context isolation is the main benefit of subagents. It's also the constraint you need to design around.

**What the subagent sees:** its own system prompt (from the spec file), the task it was given by the main agent, and its own tool results. It does not see the main agent's full conversation history. This is the mechanism that keeps the main context clean. The audit subagent can do extensive analysis without the findings flooding the developer's working context.

**What it doesn't see:** prior messages, MCP connections established in the main session (unless explicitly passed), or the main agent's current file state beyond what's included in the task description. Design subagent tasks to be self-contained.

**Network and credentials:** Subagents operate within the same Claude Code session and use separate context windows. This is not the same as process-level or network-level isolation. Before delegating sensitive tasks, verify that the client's network policy, proxy rules, and credentials apply as expected to subagent operations — don't assume isolation that hasn't been explicitly confirmed.

> [!Important]
> <small>FAILURE HANDLING: DESIGN FOR IT UPFRONT</small>
>
> When a subagent fails, the main agent receives an error result instead of a success result. The main agent is responsible for handling it: retry, skip, or escalate. **Don't build pipelines where failure of one subagent silently corrupts the next.** The remediation subagent receiving a failed audit output is the most common failure mode. Make the audit result explicit and validate it before passing it downstream.
>
> In the security audit pattern: if the audit subagent fails to parse a minified file, the main agent receives an error result. Not a null response. Not a silent skip. It looks like: <small>`{ status: 'error', message: 'Parse failed: minified file at /dist/app.min.js' }`</small>. The main agent then decides: retry with a different approach, flag the file for manual review, or proceed with the other audit results. None of that happens automatically. It has to be written into the main agent’s instructions.

## Plugin Marketplaces and Dependency Versioning

<span style="font-size: 1.25em;">_Day 30. What survives after you leave?_</span>

By the end of this lesson, you can evaluate which activation artifacts belong in the team plugin, make the Day 28 bundling call with a defensible rationale, and hand off a versioned plugin the client's CoE can maintain after the engagement ends.

### Concept

<span style="font-size: 1.15em;">_A plugin is everything you've built, bundled into one installable unit_</span>

You've built Skills, configured hooks, set up MCP servers, and defined subagent specs. A plugin is the mechanism that keeps all of it together and distributable after the engagement ends.

A plugin is a folder with a `plugin.json` manifest and the full set of Claude Code extensions it provides. The developer installs it with one command and gets everything the plugin contains (Skills, hooks, MCP configs, slash commands, subagent specs) without installing each component separately. After install, verify that each component loads and functions as expected — MCP auth issues, hook permission errors, and plugin conflicts can prevent individual components from activating.

```bash
# Plugin directory structure
my-plugin/
├── .claude-plugin/
│   └── plugin.json          ← required: plugin manifest
├── commands/                ← custom slash commands
│   └── code-review.md
├── agents/                  ← subagent specs
│   └── security-auditor.md
├── skills/                  ← Skills
│   └── coding-standards/
│       └── SKILL.md
├── hooks/                   ← hook configuration
│   └── hooks.json
└── .mcp.json                ← MCP server definitions
```
```json
// plugin.json — plugin manifest
{
  "name": "finserv-activation",
  "version": "1.0.0",
  "description": "Claude Code activation plugin for FinServ Corp engineering team"
}
```

#### Install commands

```bash
# Install a specific plugin
/plugin install @org/plugin-name

# Browse available plugins
/plugin browse

# Update an installed plugin
/plugin update @org/plugin-name
```

### Worked example

<span style="font-size: 1.15em;">_The Day 30 packaging exercise: what to bundle and what to leave out_</span>

You're wrapping a four-week activation with a 12-person engineering team at a financial services client. The Activation Plan calls for a Week 4 packaging decision: which skills, MCP configs, hooks, subagents, and slash commands built during the activation should bundle into the team plugin?

Not everything belongs in the plugin. A component that worked for one developer's workflow isn't ready for 12. Apply this fitness test for each component before bundling:

> [!Important]
> <small>THE COE CONVERSATION TO HAVE BEFORE DAY 27</small>
>
> The plugin needs somewhere to live after the engagement ends. That means an enterprise marketplace or a shared registry the CoE owns. **Don't wait until Day 30 to have this conversation.** If the marketplace doesn't exist, setting it up takes time. Raise it at the Week 3 CoE touchpoint.

### Distribution model

<span style="font-size: 1.15em;">_Team plugin vs enterprise marketplace: two distribution scopes_</span>

The separation matters for governance. Different owners, different release cadences, different audiences.

| | |
| :-- | :-- |
| TEAM PLUGIN<br><span class="font-size-lg" style="font-size: 1.15em;">**Team-specific, team-owned**</span><br><br>Skills and hooks specific to this team's workflow. Installed from a shared registry the CoE manages. Developers on this team install it; no one else needs it. The team can iterate on it without a CoE release cycle. | ENTERPRISE MARKETPLACE<br><span class="font-size-lg" style="font-size: 1.15em;">**Org-wide, CoE-governed**</span><br><br>Approved MCP configurations, security hooks, and compliance Skills that apply to all developers. CoE verifies and publishes. Stricter release cycle: changes go through the approval workflow before pushing to the whole org. |
| | |

The architecture mirrors how good organisations manage shared infrastructure: a governance layer (CoE plugin) and a team layer (team plugin), each with its own release cadence and owner. One mega-plugin couples the two; a change to any component requires a full CoE release.

When the enterprise marketplace has an approved plugin, the CoE can connect it to RBAC and SCIM group assignment in the Admin Console. The workflow is three steps: create and approve the plugin, publish it to the marketplace, assign it to the relevant SCIM groups. From that point, any developer provisioned into those groups receives the approved configuration automatically — no manual install, no shadow tooling, no gap between access and setup.

> [!Important]
> <small>THE DAY 1 GOVERNANCE PITCH</small>
>
> When a client's CISO asks how they maintain control as Claude Code scales across teams, this is the answer: **your security team approves the plugin, your IT team assigns it to the right SCIM groups, and every new developer inherits the approved configuration on their first day**. Access to the tool and access to the governed configuration arrive together. That's the model — not policy documents and a hope that developers comply.

### Dependency versioning

<span style="font-size: 1.15em;">_Plugin versioning: what to tell the CoE about keeping things stable_</span>

The plugin delivers a known-good configuration. Versioning is what keeps it known-good after the engagement ends.

The `plugin.json` manifest supports versioning. Three practices to establish with the CoE at Day 30:

1. **Pin MCP server versions.** MCP servers update independently, so an upstream change to a tool's input schema can break a workflow the team relies on. Pin versions in the manifest and let the CoE test and promote new versions deliberately.

2. **Version the plugin itself.** When the CoE releases a new version, developers run /plugin update, and the version number tells support exactly which configuration a team is running.

3. **Document the Day 30 package.** Record what's in the plugin, which version of each MCP server is bundled, and who owns it. This is the handoff document. The CoE takes it from you; without it, the plugin is a black box that nobody knows how to maintain.

Two statements to check your read on these boundaries before the scenario.

## Walkthrough

<span style="font-size: 1.15em;">_Build your activation plugin_</span>

Everything built in Lessons 5.1–5.7 goes into one installable plugin. This is the artifact you hand off to the client's CoE on Day 30.

| | |
| :-- | :-- |
| <span class="font-size-lg" style="font-size: 1.25em;">**1**</span> | <span class="font-size-lg" style="font-size: 1.15em;">**Create the plugin directory**</span><br><br>Make a `<client-name>-activation/` directory. Inside it: `.claude-plugin/plugin.json` (the manifest), `skills/`, `hooks/`, `agents/`, and `.mcp.json`. |
| <span class="font-size-lg" style="font-size: 1.25em;">**2**</span> | <span class="font-size-lg" style="font-size: 1.15em;">**Copy your components in**</span><br><br>Copy the `SKILL.md` from Lesson 5.5 into `skills/<skill-name>/`. Copy the `hooks.json` from Lesson 5.6 into `hooks/`. Copy the subagent spec from Lesson 5.7 into `agents/`. Add the `.mcp.json` from Lesson 5.1. |
| <span class="font-size-lg" style="font-size: 1.25em;">**3**</span> | <span class="font-size-lg" style="font-size: 1.15em;">**Write the plugin.json manifest**</span><br><br>Define the plugin name, version, and description. These are the three required fields. Pin the MCP server versions you bundled so the CoE controls when updates are promoted. |
| <span class="font-size-lg" style="font-size: 1.25em;">**4**</span> | <span class="font-size-lg" style="font-size: 1.15em;">**Install and verify**</span><br><br>Run `/plugin install ./<client-name>-activation/`. Verify the Skill loads, the hook fires, and the MCP server connects. |
| | |

