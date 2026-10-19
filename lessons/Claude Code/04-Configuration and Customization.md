# Configuration and Customization

## Configuration Hierarchy and Precedence

<span style="font-size: 1.25em;">_One config doesn't fit all. Four scopes solve that._</span>

By the end of this lesson, you will know which scope wins when settings conflict and which one to reach for on a client engagement.

### Why four scopes?

<span style="font-size: 1.15em;">_There are four places Claude reads config, and they don't carry equal weight._</span>

Claude Code reads configuration from four sources. When the same setting appears in more than one place, a fixed priority order decides which value applies.

The four sources are **Managed** (deployed by IT, the highest priority), **Local** (personal project overrides, git-ignored), **Project** (team-shared settings committed to the repo), and **User** (personal defaults that follow you across all projects). Each scope can only be overridden by something above it in the chain. Permissions are the exception: allow and deny lists merge across scopes rather than override, so a developer's local configuration adds to the project's rules rather than replacing them.

> [!Tip]
> <small>WORKING RULE</small>
>
> Scope is an **ownership question** before it is a technical one. Who controls this setting? Who should it affect? Can they override it? Answer those three questions and the right scope picks itself.

### The four scopes

<span style="font-size: 1.15em;">_Each scope has a fixed location and a defined audience._</span>

These two facts are what you need to choose the right one on any client engagement.

| | |
| :-- | :-- |
| <span class="font-size-xl" style="font-size: 1.5em;">**M**</span><br><span class="font-size-lg" style="font-size: 1.15em;">**Managed**</span><br><br>Deployed by IT via MDM, Group Policy, or a system-level config file. Applies to every session on the machine. Cannot be overridden by any user or project setting.[cite: 5]<br><br>*macOS: /Library/Application Support/ClaudeCode/ · Linux: /etc/claude-code/*[cite: 5] | <span class="font-size-xl" style="font-size: 1.5em;">**L**</span><br><span class="font-size-lg" style="font-size: 1.15em;">**Local**</span><br><br>Personal overrides for one specific project. Git-ignored automatically when Claude Code creates the file. Applies only to you, only in this repo.[cite: 5]<br><br>*.claude/settings.local.json*[cite: 5] |
| <span class="font-size-xl" style="font-size: 1.5em;">**P**</span><br><span class="font-size-lg" style="font-size: 1.15em;">**Project**</span><br><br>Shared team settings committed to git. Applies to everyone working on this repo. Use for allowed and denied tools, hooks, and approved MCP servers.[cite: 5]<br><br>*.claude/settings.json*[cite: 5] | <span class="font-size-xl" style="font-size: 1.5em;">**U**</span><br><span class="font-size-lg" style="font-size: 1.15em;">**User**</span><br><br>Personal defaults across all your projects. Lowest priority: applies when no higher scope has set the value. Use for preferred model, editor keybindings, notification preferences.<br><br>*~/.claude/settings.json* |
| | |

### Precedence

<span style="font-size: 1.15em;">_Managed can't be overridden. User is the last resort._</span>

When Claude Code resolves a setting, it walks this chain from top to bottom and takes the first value it finds.

| | |
| :-- | :-- |
| <span class="font-size-lg" style="font-size: 1.25em;">**1**</span> | <span class="font-size-lg" style="font-size: 1.15em;">**Managed: highest authority**</span><br><br>Set by IT or DevOps via a system-level file. Applies to the whole machine. No user or project setting can override it. This is where client compliance requirements belong. |
| <span class="font-size-lg" style="font-size: 1.25em;">**2**</span> | <span class="font-size-lg" style="font-size: 1.15em;">**CLI flags: session-level overrides**</span><br><br>Flags passed when launching Claude Code, such as `--allowedTools` or `--model`. Override all file-based settings for that session only. Not persisted. |
| <span class="font-size-lg" style="font-size: 1.25em;">**3**</span> | <span class="font-size-lg" style="font-size: 1.15em;">**Local: personal project override**</span><br><br>`.claude/settings.local.json` in the repo. Your personal config for this project. Overrides project settings for your session only, without changing the shared file. |
| <span class="font-size-lg" style="font-size: 1.25em;">**4**</span> | <span class="font-size-lg" style="font-size: 1.15em;">**Project: shared team baseline**</span><br><br>`.claude/settings.json` committed to git. Every collaborator on the repo gets these settings. Use for team standards: pre-approved commands, hooks, MCP servers. |
| <span class="font-size-lg" style="font-size: 1.25em;">**5**</span> | <span class="font-size-lg" style="font-size: 1.15em;">**User: personal fallback**</span><br><br>`~/.claude/settings.json`. Applies when nothing above has set the value. The lowest priority in the chain. |
| | |


