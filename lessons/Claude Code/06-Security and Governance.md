# Security and Governance

## Managed-settings.json: forced login, allow and deny MCP, hooks restrictions

The policy file users cannot override
By the end of this lesson, you can configure managed-settings.json for a new client deployment and know which controls to set before anyone logs in.

### Your client

**FinCo Financial Services:** FinCo is a 1,800-developer financial services firm modernizing core banking infrastructure. They are AWS-native, running all workloads in us-east-1 and us-west-2. They use Okta for identity management and SSO, and Jamf for macOS device management. Their security team has three non-negotiables before any new tooling can go live: all data processing must stay within approved AWS regions, every developer account must trace back to Okta, and any new AI tooling must clear a written security review. This is the client context for the security questionnaire you will build across Course 6.

### The governance layer

`managed-settings.json` sits above everything. No user or project setting can override it.

| Step | Details |
| :--- | :--- |
| <span style="color: orange;">**1**</span> | **<span style="font-size: 1.15em;">Managed settings</span>**<br>IT-enforced via MDM or server push. Cannot be overridden by any other layer. This is where the organization's non-negotiable policy lives. |
| <span style="color: orange;">**2**</span> | **<span style="font-size: 1.15em;">Command line arguments</span>**<br>Session-level overrides, applied when the CLI is invoked. Useful for automation scripts but temporary. |
| <span style="color: orange;">**3**</span> | **<span style="font-size: 1.15em;">Local project settings</span>**<br>`.claude/settings.local.json`: developer-level, typically not committed to source control. |
| <span style="color: orange;">**4**</span> | **<span style="font-size: 1.15em;">Shared project settings</span>**<br>`.claude/settings.json`: committed to source control, shared across the team. |
| <span style="color: orange;">**5**</span> | **<span style="font-size: 1.15em;">User settings</span>**<br>`~/.claude/settings.json`: personal preferences, the lowest priority layer. |

> [!Note]
> To remember
>
> Every other settings layer serves the individual. managed-settings.json serves the organization. A developer can configure their personal settings.json, but managed-settings.json means they cannot undo what the admin set.

### Delivery mechanisms

Three ways to push it. Which one fits depends on the client's device management setup.

| <span style="color: orange; font-size: 1.8em;">**01**</span><br><br>**Server-managed** | <span style="color: orange; font-size: 1.8em;">**02**</span><br><br>**MDM / OS policies** | <span style="color: orange; font-size: 1.8em;">**03**</span><br><br>**File-based** |
| :--- | :--- | :--- |
| Pushed via the Claude.ai admin console (available on Teams and Enterprise plans), making it the right choice for organizations without existing MDM infrastructure.<br><br>**<span style="font-size: 1.25em;">Fits a client who:</span>**<br>wants central control without standing up device management. The simplest path when there's no Jamf or Intune already in place. Enterprise unlocks the full managed-settings feature set; Teams provides basic admin console access. | macOS managed preferences via Jamf; Windows registry via Intune or Group Policy. Best for organizations with existing device management in place.<br><br>**<span style="font-size: 1.25em;">Fits a client who:</span>**<br>already manages developer endpoints. FinCo runs Jamf for macOS, so this is the natural fit for their rollout, no new infrastructure required. | Manual filesystem install to system directories. Appropriate for pilots, smaller deployments, or staged testing before a full MDM rollout.<br><br>**<span style="font-size: 1.25em;">Fits a client who:</span>** is testing before committing. Good for a pilot cohort, but it doesn't scale, plan the move to MDM or server-managed before a full deployment. |

### Day 0 controls

Lock down authentication and MCP access before anyone touches a keyboard.

| | | |
| :--- | :--- | :--- |
| <span style="color: orange; font-size: 0.8em;">**A U T H**</span><br>**<span style="font-size: 1.15em;">forceLoginMethod</span>**<br>Enforces "claudeai" or "console" authentication. Blocks API key login, which bypasses SSO and audit controls.<br><br>**<span style="font-size: 1.2em;">For FinCo:</span>** set to `"claudeai"` so every login routes through Okta SSO. An API key would sidestep their "every account traces back to Okta" requirement. | <span style="color: orange; font-size: 0.8em;">**A U T H**</span><br>**<span style="font-size: 1.15em;">forceLoginOrgUUID</span>**<br>Login fails unless the account belongs to the specified organization UUID. Prevents access from shadow personal accounts on the company domain.<br><br>**<span style="font-size: 1.2em;">For FinCo:</span>** pins logins to the corporate org, so a developer can't quietly sign in with a personal Claude account that happens to use their work email. | |
| <span style="color: orange; font-size: 0.8em;">**M C P**</span><br>**<span style="font-size: 1.15em;">allowedMcpServers</span>**<br>Allowlist of approved MCP server names. An empty array enforces total lockdown: no MCP connections of any kind.<br><br>**<span style="font-size: 1.2em;">For FinCo:</span>** start narrow. An explicit allowlist (or an empty array during review) means no MCP server runs until the security team has signed off on it. | <span style="color: orange; font-size: 0.8em;">**M C P**</span><br>**<span style="font-size: 1.15em;">allowManagedMcpServersOnly</span>**<br>Only admin-defined MCP servers can be active. User-added servers are blocked regardless of the allowlist state.<br><br>**<span style="font-size: 1.2em;">For FinCo:</span>** this is the category-level control. It closes the whole class of "developer added their own server" risk, not just one server at a time. The answer to this lesson's scenario. | |

### Beyond Day 0

Hooks, permissions, version pinning, and org instructions complete the policy.

| | |
| :--- | :--- |
| <span style="color: orange; font-size: 1.8em;">**01**</span><br><br>**<span style="font-size: 1.15em;">Hooks controls</span>**<br>allowManagedHooksOnly and disableAllHooks control which pre- and post-task scripts are permitted to run.<br><br>**<span style="font-size: 1.2em;">Why it matters:</span>** hooks run arbitrary scripts around tasks. `allowManagedHooksOnly` lets the org ship approved automation while blocking anything a developer wires up on their own. | <span style="color: orange; font-size: 1.8em;">**02**</span><br><br>**<span style="font-size: 1.15em;">Permission controls</span>**<br>allowManagedPermissionRulesOnly and disableAutoMode prevent users from overriding tool approval rules or enabling auto-accept globally.<br><br>**<span style="font-size: 1.2em;">Why it matters:</span>** `disableAutoMode` stops a developer from turning off the approval prompts entirely, keeping a human in the loop on tool calls in a regulated environment. |
| <span style="color: orange; font-size: 1.8em;">**03**</span><br><br>**<span style="font-size: 1.15em;">Version enforcement</span>**<br>requiredMinimumVersion and requiredMaximumVersion pin the CLI version range and exit at startup if the installed version falls outside it.<br><br>**<span style="font-size: 1.2em;">Why it matters:</span>** for clients with tested-version compliance rules, this is enforcement, not documentation. Claude Code refuses to start outside the approved range. | <span style="color: orange; font-size: 1.8em;">**04**</span><br><br>**<span style="font-size: 1.15em;">Org CLAUDE.md</span>**<br>The claudeMd key injects organization-wide instructions into every session as managed memory, applied before any project or user CLAUDE.md file.<br><br>**<span style="font-size: 1.2em;">Why it matters:</span>** because it loads first and can't be overridden, it's the place for non-negotiable instructions, not preferences a developer can quietly ignore. |

### Org instructions: what to write

The managed `CLAUDE.md` sets policy. Four principles for writing it well.

| | |
| :--- | :--- |
| <span style="color: orange; font-size: 1.8em;">**01**</span><br><br>**<span style="font-size: 1.15em;">Policy, not preferences</span>**<br>Security requirements, compliance rules, and IP handling constraints belong here. Coding style and output format preferences belong in project CLAUDE.md.<br><br>**<span style="font-size: 1.2em;">The test:</span>** would violating this create a compliance or legal issue? If yes, it's org instructions. If no, it belongs at the project or user layer where developers can adjust it. | <span style="color: orange; font-size: 1.8em;">**02**</span><br><br>**<span style="font-size: 1.15em;">Use Claude to draft them</span>**<br>Share the client's acceptable use policy or data handling guidelines with Claude and ask it to produce a draft managed CLAUDE.md. Then review and tighten.<br><br>**<span style="font-size: 1.2em;">Why this works:</span>** Claude produces instructions calibrated to the client's own language and policy structure. The consultant's job becomes editing and approving rather than writing from scratch. |
| <span style="color: orange; font-size: 1.8em;">**03**</span><br><br>**<span style="font-size: 1.15em;">Avoid over-restriction</span>**<br>Overly prescriptive org instructions degrade output quality and create developer friction. Constrain what must be constrained; leave Claude room to operate within those bounds.<br><br>**<span style="font-size: 1.2em;">In practice:</span>** a security team that adds 30 lines of stylistic rules alongside 3 compliance requirements buries the signal. Claude will attempt to satisfy all instructions equally, diluting the ones that actually matter. | <span style="color: orange; font-size: 1.8em;">**04**</span><br><br>**<span style="font-size: 1.15em;">Include the why</span>**<br>Add brief context alongside each constraint — "due to regulatory requirements" or "per our IP policy." Developers who understand a limitation are less likely to work around it.<br><br>**<span style="font-size: 1.2em;">Secondary benefit:</span>** rationale lines make org instructions easier to audit and update when policies change. A constraint without context is harder to evaluate when someone asks whether it still applies. |







