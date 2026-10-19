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


