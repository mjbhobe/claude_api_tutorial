
<link rel="stylesheet" href="./tabs.css">

# Claude Code & MCP Integration

<span style="font-size: 1.25em">_Claude Code is your terminal-native development partner._</span>

In previous modules, you set up essential API components: prompts, tool schemas, context engineering, agent loops, and multimodal ingestion; this module builds directly on that foundation. 

* **Claude Code** allows you to operate the same model within your terminal environment, introducing a permission layer, configuration system, and team-oriented sharing features. 
* **The MCP protocol** enables secure integration with external services. In this module, you’ll learn how to configure Claude Code and MCP for robust security and effective deployment.

### Claude Code agent loop, permission modes, settings, and where a human gate goes

<span style="font-size: 1.15em">_Module 2 established how the agent loop works at the API level: the model calls tools, gets results back, and continues until the task is done._</span>

**Claude Code runs that same loop in your terminal but adds an additional layer:** a permission system that gates every action the agent wants to take. Before you can configure anything, you need to understand how the loop runs and what the permission modes control.

### How Claude Code works through a task: explore, plan, and code

When you hand Claude Code a task, it does not start writing immediately. It reads files, traces the relevant logic, and builds a picture of the codebase first; this is the exploration phase. Then, once it understands enough to propose a change, it creates a plan. A plan is a structured description of the edits it intends to make. Only after you review and approve the plan does it move into the code phase, where it writes and executes the changes.

This sequence matters for two reasons. First, it produces better output: Claude Code understands the codebase before touching anything, so it makes fewer assumptions and catches more downstream effects. Second, it is where the permission modes plug in: plan mode holds Claude Code in the explore phase, blocking all file edits and shell commands until you release it, making it a useful default for unfamiliar codebases or high-stakes work.

### Permission modes: approvals, gates, and constraints

Permission modes control how often Claude Code stops to ask for confirmation. Each mode makes a different tradeoff between speed and oversight. The right choice depends on how well you know the codebase and how reversible the changes are.

Select each tab for what that mode auto-approves, what it still gates, and its limitations.

<div class="jb-tabs-container">
<input type="radio" class="jb-r1" name="jb-tab-group-1" id="g3-tab1" checked>
<input type="radio" class="jb-r2" name="jb-tab-group-1" id="g3-tab2">
<input type="radio" class="jb-r3" name="jb-tab-group-1" id="g3-tab3">
<input type="radio" class="jb-r4" name="jb-tab-group-1" id="g3-tab4">
<input type="radio" class="jb-r5" name="jb-tab-group-1" id="g3-tab5">
<input type="radio" class="jb-r6" name="jb-tab-group-1" id="g3-tab6">

<div class="jb-tabs-header">
<label class="jb-tab-label jb-l1" for="g3-tab1">default</label>
<label class="jb-tab-label jb-l2" for="g3-tab2">acceptEdits</label>
<label class="jb-tab-label jb-l3" for="g3-tab3">plan</label>
<label class="jb-tab-label jb-l4" for="g3-tab4">auto</label>
<label class="jb-tab-label jb-l5" for="g3-tab5">dontAsk</label>
<label class="jb-tab-label jb-l6" for="g3-tab6">bypassPermissions</label>
</div>

<div class="jb-tab-content">

<div class="jb-tab-panel jb-p1" id="g1-content1">
<p>
<b>What it auto-approves:</b> Reads only. Prompts before nearly every edit or command.

<b>What it still gates:</b> All file edits and shell commands require confirmation.

<b>Limitations:</b> Safe but slow on trusted work. The baseline for any new project or unfamiliar codebase.
</p>
</div>

<div class="jb-tab-panel jb-p2" id="g1-content2">
<p>
What it auto-approves: Reads, file edits, and common filesystem commands (mkdir, touch, rm, rmdir, mv, cp, and sed) inside the working directory. Auto-approval is scoped to paths inside the working directory, and protected paths still prompt.

What it still gates: All other shell commands; writes outside the working directory; writes to protected paths.

Limitations: Trusted local work where shell execution still needs a human eye. Not appropriate if the agent must run scripts.
</p>
</div>

<div class="jb-tab-panel jb-p3" id="g1-content3">
<p>
What it auto-approves: Reads only. Research and proposes; makes no edits.

What it still gates: All file edits and shell commands until you approve a plan.

Limitations: Exploration and planning on sensitive or unfamiliar codebases. Not appropriate for tasks that must write output.
</p>
</div>

<div class="jb-tab-panel jb-p4" id="g1-content4">
<p>
What it auto-approves: Everything, but a separate classifier reviews each action first and blocks anything that escalates beyond your request, targets unrecognized infrastructure, or appears driven by hostile or inappropriate content.

What it still gates: Production deploys and migrations, mass deletes, credential exfiltration, and force-push to main are blocked by default.

Limitations: Reduces prompts but does not guarantee safety; this is a research preview, not a substitute for reviewing sensitive operations. Availability depends on plan, model version, and admin settings. Always verify current requirements before build.
</p>
</div>

<div class="jb-tab-panel jb-p5" id="g1-content5">
<p>
What it auto-approves: Only tools you pre-approved in an allow rule, plus read-only commands. Auto-DENIES everything else.

What it still gates: Every tool call not on the allow list is denied. There is no queue for confirmation.

Limitations: Built for locked-down CI and scripts. It restricts well, but it is not a way to reduce friction on local interactive work.
</p>
</div>

<div class="jb-tab-panel jb-p6" id="g1-content6">
<p>
What it auto-approves: All tool calls. No confirmation prompts and no safety checks.

What it still gates: Nothing in normal operation. The standard permission checks are bypassed; only catastrophic delete commands such as rm -rf / and rm -rf ~ still trigger a last-resort prompt.

Limitations: Only inside an isolated container or VM where the environment is disposable. Never on a developer workstation against a live codebase.
</p>
</div>

</div>
</div>

### Where does the configuration live and who it applies to

Settings can be placed at several levels, and each level determines the scope of the rules it contains.

* **User level** (`~/.claude/settings.json`): Applies to every project on the machine. This is the right place for preferences that should follow you everywhere, such as a preferred default mode for exploration work. 

    This file belongs to one developer and follows them into every project on their machine. It holds taste and habit. It carries no team rules and no policy, because nobody else receives it. It is not checked into version control.

    Here is an example:
    ```json
        {
            "$schema": "https://json.schemastore.org/claude-code-settings.json",
            "model": "claude-sonnet-5-5",
            "theme": "dark",
            "permissions": {
                "defaultMode": "plan",
                "allow": [
                    "Bash(git status)",
                    "Bash(git diff *)",
                    "Bash(git log *)"
                ],
                "deny": [
                    "Read(~/Downloads/**)"
                ]
            }
        }
    ```
* **Project level** (`.claude/settings.json`, committed to the repo): Applies to everyone who clones the repository. This is the right place for team-wide conventions, allow rules for the tools your project uses, and deny rules for paths that should not be touched.

    This file lives in the repository and every teammate receives it on clone. It holds the team’s tooling and the project’s own rules. It must not contain anything personal.

    Here is an example:
    ```json
        {
        "$schema": "https://json.schemastore.org/claude-code-settings.json",
        "permissions": {
            "allow": [
                "Bash(python -m pytest *)",
                "Bash(ruff check *)",
                "Bash(ruff format *)",
                "Bash(mypy *)",
                "Bash(bandit -r src *)",
                "Bash(pip-audit *)",
                "Bash(git status)",
                "Bash(git diff *)"
            ],
            "ask": [
                "Bash(git commit *)"
            ],
            "deny": [
                "Read(./data/**)",
                "Read(./tests/fixtures/prod_extract/**)",
                "Edit(./config/prod/**)",
                "Edit(./poetry.lock)"
            ]
        },
        "env": {
            "PYTHONPATH": "src",
            "APP_ENV": "test"
        },
        "hooks": {
            "PostToolUse": [
            {
                "matcher": "Edit|Write",
                "hooks": [
                {
                    "type": "command",
                    "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/python_quality_gate.sh"
                }
                ]
            }
            ]
        }
        }
    ```
* **Local project level** (`.claude/settings.local.json`): Personal overrides for one project, automatically git-ignored. This is the right place for your own preferences that should not be committed to the whole team.

    This is your personal override for one repository. It sits above the shared project file in precedence and stays out of git. That makes it the right place for experiments before you propose a change to the team. 

    Here is an example:

    ```json
    {
        "model": "claude-opus-5-5",
        "spinnerTipsEnabled": false,
        "permissions": {
            "allow": [
            "Bash(python -m pytest tests/payments/*)"
            ]
        },
        "env": {
            "APP_ENV": "local",
            "LOG_LEVEL": "DEBUG"
        }
    }
    ```
* **Enterprise level** (`managed-settings.json`, set by administrators): **Cannot be overridden by users or project files**. The right place for organization-wide security controls such as denying edits to environment files or blocking specific shell commands across all projects.

    On macOS it lives at `/Library/Application Support/ClaudeCode/managed-settings.json`, on Linux and WSL at `/etc/claude-code/managed-settings.json`, and on Windows at `C`:\ProgramData\ClaudeCode\managed-settings.json`. The same JSON can also be delivered through MDM (mobile device management, such as Intune or Jamf) or server-managed settings from the claude.ai console. In a bank, MDM is usually the right channel, because an ordinary file can be edited by anyone with local admin rights. 

    Here is an example:
    ```json
    {
        "$schema": "https://json.schemastore.org/claude-code-settings.json",
        "forceLoginMethod": "claudeai",
        "forceLoginOrgUUID": "00000000-0000-0000-0000-000000000000",
        "requiredMinimumVersion": "2.1.257",
        "cleanupPeriodDays": 7,
        "allowManagedMcpServersOnly": true,
        "permissions": {
            "disableBypassPermissionsMode": "disable",
            "deny": [
            "Read(./.env)",
            "Read(./.env.*)",
            "Read(**/secrets/**)",
            "Read(**/*.pem)",
            "Read(**/*.pfx)",
            "Read(~/.ssh/**)",
            "Read(~/.aws/**)",
            "Edit(./.github/workflows/**)",
            "Bash(curl *)",
            "Bash(wget *)",
            "Bash(pip install *)",
            "Bash(pip3 install *)",
            "Bash(git push --force*)",
            "Bash(git push -f *)"
            ],
            "ask": [
            "Bash(git push *)"
            ]
        },
        "sandbox": {
            "enabled": true,
            "failIfUnavailable": true
        },
        "env": {
            "PIP_INDEX_URL": "https://artifactory.examplebank.internal/api/pypi/pypi-approved/simple"
        },
        "hooks": {
            "PreToolUse": [
                {
                    "matcher": "*",
                    "hooks": [
                        {
                            "type": "command",
                            "command": "/opt/examplebank/bin/claude-audit-log"
                        }
                    ]
                }
            ]
        }
    }
    ```

Allow and deny rules layer on top of the selected mode. **A deny rule always wins over an allow rule**, regardless of the mode in effect. The most durable governance control is an enterprise-level deny rule: it cannot be removed by any individual developer and applies even when a bypass mode is set.

> [!Caution]
> **How the four levels interact**. For single-value keys such as model, theme or an env variable, Claude Code uses the value from the highest level that sets it, in this order: managed settings, command line, project local, shared project, then user. List keys such as permissions.allow and permissions.deny work differently. Claude Code combines the lists from each file instead of picking one, so a lower level can add rules but cannot remove rules set elsewhere. When rules conflict, a deny rule always overrides an allow rule, whichever file each came from, and an allow rule in your local file does not outrank an ask rule from a project or managed file. Managed settings therefore cannot be loosened by user, project, local or --settings values. The only lower-level exceptions run in the safe direction: for a few security keys, Claude Code honors a stricter value from a lower level over a looser managed value, so a lower level can tighten managed policy but never relax it. A managed model is also only a starting default, and the real locks are availableModels and deniedModels. 

### Where a human still has to look: placing the review gate by worst-case cost

Permission modes and deny rules decide what the agent can do without asking. They do not decide where you, the human, still need to look before an action lands. That decision rests on one question, the same one that separates a safe mode from a risky one: what is the worst outcome if this action runs without a person checking it? The lower the cost of being wrong, the more you can let through. The higher the cost, and the harder it is to undo, the more a step needs a human gate before it executes.

That same worst-case question places the gate whether the agent is writing code or running unattended in an automated step such as a bot that comments on or blocks a pull request. Three placements follow from it:

Let low-stakes, reversible actions through without a gate. A formatting fix or an edit confined to the working directory carries little cost if it is wrong, so requiring a human to approve each one buys oversight you do not need and slows the work. This is the case acceptEdits is built for.
Gate any action that is hard to undo or reaches a sensitive path: a write outside the working directory, a destructive shell command, or an edit to a security-relevant or protected file. The cost of a wrong call there is high, so the agent should pause and surface the action for a person before it runs. A deny rule enforces this deterministically, and default or plan mode keeps the prompt in place while you decide.
Never let the agent be the only gate on a change to code your team has marked sensitive. There the agent’s work is an input to a human decision, not a replacement for one, so a person must review the change before it merges no matter how confident the agent or its own review sounds.
The placement of the gate and the choice of permission mode are the same decision viewed from two sides. The mode sets the default for a whole session, and the gate is where you override that default for the one action whose cost is too high to leave to the default; both come from asking what breaks if this runs unchecked.

Cost · Complexity · Risk
Cost: Running in default mode on trusted work adds prompt latency to every tool call, and this accumulates on a long refactor.

Complexity: Multiple levels of settings and files with an override hierarchy require consistent care. A deny rule at the enterprise level that contradicts an allow rule at the project level needs to be understood by everyone maintaining the project config.

Risk: The risk lies in using the wrong mode for the context. For example, a bypass mode set out of impatience on a non-isolated machine removes every safety prompt between the agent and your live files, and, unlike the other modes, also removes the protected-path guard.
