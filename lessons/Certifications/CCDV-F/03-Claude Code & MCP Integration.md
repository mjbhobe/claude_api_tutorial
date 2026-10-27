
<link rel="stylesheet" href="./tabs.css">

# Claude Code & MCP Integration

<span style="font-size: 1.25em">_Claude Code is your terminal-native development partner._</span>

In previous modules, you set up essential API components: prompts, tool schemas, context engineering, agent loops, and multimodal ingestion; this module builds directly on that foundation. 

* **Claude Code** allows you to operate the same model within your terminal environment, introducing a permission layer, configuration system, and team-oriented sharing features. 
* **The MCP protocol** enables secure integration with external services. In this module, you’ll learn how to configure Claude Code and MCP for robust security and effective deployment.

## Permission Modes &amp; Human Gates

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

    On macOS it lives at `/Library/Application Support/ClaudeCode/managed-settings.json`, on Linux and WSL at `/etc/claude-code/managed-settings.json`, and on Windows at `C:\ProgramData\ClaudeCode\managed-settings.json`. The same JSON can also be delivered through MDM (mobile device management, such as Intune or Jamf) or server-managed settings from the claude.ai console. In a bank, MDM is usually the right channel, because an ordinary file can be edited by anyone with local admin rights. 

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
> **How the four levels interact**. For single-value keys such as model, theme or an env variable, Claude Code uses the value from the highest level that sets it, in this order: managed settings, command line, project local, shared project, then user. List keys such as `permissions.allow` and `permissions.deny` work differently. Claude Code combines the lists from each file instead of picking one, so a lower level can add rules but cannot remove rules set elsewhere. When rules conflict, a deny rule always overrides an allow rule, whichever file each came from, and an allow rule in your local file does not outrank an ask rule from a project or managed file. Managed settings therefore cannot be loosened by user, project, local or --settings values. The only lower-level exceptions run in the safe direction: for a few security keys, Claude Code honors a stricter value from a lower level over a looser managed value, so a lower level can tighten managed policy but never relax it. A managed model is also only a starting default, and the real locks are availableModels and deniedModels. 

### Where a human still has to look: placing the review gate by worst-case cost

Permission modes and deny rules decide what the agent can do without asking. They do not decide where you, the human, still need to look before an action lands. That decision rests on one question, the same one that separates a safe mode from a risky one: what is the worst outcome if this action runs without a person checking it? The lower the cost of being wrong, the more you can let through. The higher the cost, and the harder it is to undo, the more a step needs a human gate before it executes.

That same worst-case question places the gate whether the agent is writing code or running unattended in an automated step such as a bot that comments on or blocks a pull request. Three placements follow from it:

Let low-stakes, reversible actions through without a gate. A formatting fix or an edit confined to the working directory carries little cost if it is wrong, so requiring a human to approve each one buys oversight you do not need and slows the work. This is the case acceptEdits is built for.
Gate any action that is hard to undo or reaches a sensitive path: a write outside the working directory, a destructive shell command, or an edit to a security-relevant or protected file. The cost of a wrong call there is high, so the agent should pause and surface the action for a person before it runs. A deny rule enforces this deterministically, and default or plan mode keeps the prompt in place while you decide.
Never let the agent be the only gate on a change to code your team has marked sensitive. There the agent’s work is an input to a human decision, not a replacement for one, so a person must review the change before it merges no matter how confident the agent or its own review sounds.
The placement of the gate and the choice of permission mode are the same decision viewed from two sides. The mode sets the default for a whole session, and the gate is where you override that default for the one action whose cost is too high to leave to the default; both come from asking what breaks if this runs unchecked.

> [!Tip]
> **Cost · Complexity · Risk**
>
> **Cost**: Running in default mode on trusted work adds prompt latency to every tool call, and this accumulates on a long refactor.
>
> **Complexity**: Multiple levels of settings and files with an override hierarchy require consistent care. A deny rule at the enterprise level that contradicts an allow rule at the project level needs to be understood by everyone maintaining the project config.
>
> **Risk**: The risk lies in using the wrong mode for the context. For example, a bypass mode set out of impatience on a non-isolated machine removes every safety prompt between the agent and your live files, and, unlike the other modes, also removes the protected-path guard.

## The bypass mode that removed the one prompt that mattered


> [!Important]
> <small>**SETUP**</small>
>
> You switched to bypass Permissions to stop the constant prompts because the work felt routine. The agent had been well-behaved for days, the cleanup task was simple, and the prompt-before-every-tool-call behavior felt like unnecessary friction.

### The transcript

The following pairing session happened on a codebase cleanup that had been running without incident for three days.

```
Dev: "All right, I’m switching to bypassPermissions for this one. It’s just renaming old API endpoint references. Nothing risky."
Claude Code: [Scanning files matching pattern /v1/legacy/ ... 47 files found]
Claude Code: [Updating endpoint references ...]
Claude Code: [Running post-rename cleanup.sh script ...]
Claude Code: [Deleted 3 files matching /v1/legacy/ in /deploy/config/prod/ ...]
Dev: "Wait. What was in /deploy/config/prod/?"
Claude Code: [Files contained environment-specific endpoint overrides for the production deployment. They have been removed.]
Dev: "That directory wasn’t supposed to be in scope. I was working on /src/."
Claude Code: [The pattern /v1/legacy/ matched files in both /src/ and /deploy/config/prod/. In bypassPermissions mode, no confirmation was requested before the deletions.]
```

The prompt that would have caught this mistake was turned off when bypassPermissions was turned on. In default or acceptEdits mode, the cleanup script would not have run without a confirmation, and the user could have stopped the deletion before it reached the production configuration files. In bypassPermissions, the pattern match was broader than intended, and no prompt stood between the script and the files it deleted.

Note the precise location of the gate: it was the script invocation that would have prompted, not rm deletion commands by themselves. acceptEdits auto-approves common filesystem commands, including rm on paths inside the working directory. Had Claude issued the deletions directly as rm commands, acceptEdits would have let them through silently; only default mode prompts for those.

> [!Caution]
> <small>**WHAT TO WATCH OUT FOR**</small>
>
> A bypass mode silences all confirmation prompts, including the ones you might not have anticipated. The failure pattern here is an agent matching a broader set of files than you intended, running in a mode without checkpoints. BypassPermissions also skips the protected path guard that the other modes keep, so even repo state and Claude’s own configuration lose their automatic prompt. To cover this gap, you must set a deny rule on sensitive directories before switching modes. If you want fewer prompts without losing the safety net, use a classifier-gated mode (e.g., auto) instead of a full bypass.

## Durable Project Context

### Durable project context with CLAUDE.md, rules files, hooks, and subagents

<span style="font-size: 1.25em">_Previously we saw how Claude Code gates actions through permission modes and settings files. That configuration layer controls what the agent is allowed to do._</span>

This cluster builds on top of it: now you’ll learn how to configure what the agent knows and how it behaves, so the rules and project context you define in a session are still in effect at the start of the next one.

### CLAUDE.md: the project file that loads into every session

Every time Claude Code starts in a project directory, it looks for a file named `CLAUDE.md` at the root and reads it. The contents are appended to your prompt before any message from you arrives. This means every convention, constraint, and command you put in `CLAUDE.md` is present from the first prompt of every session, without you having to re-state it.

The `/init` command scans your codebase and generates a starter `CLAUDE.md`. The generated file is a great baseline but should be validated before using. Refine it to hold the rules that control the outcome of your prompts: your testing commands, your framework conventions, the paths the agent should not touch, and the style decisions that differ from defaults.

Size is the main failure mode. A `CLAUDE.md` that keeps growing with every new instruction can dilute the rules that matter most. A larger file consumes more of the context window, which makes any single instruction a smaller fraction of what loads, and that reduces the chance that the agent follows the one rule that catches a real mistake. Hold `CLAUDE.md` to the constraints that change behavior and move everything else into Skills that load on demand.

### Rules instruction files: scoping guidance to where it applies

In the previous section, we established that `CLAUDE.md` loads into every session and should hold the instructions that apply across the whole project. The next question is what to do with guidance that matters only in one part of the codebase. That is where rules instruction files come in: they let you apply instructions only where they are relevant, instead of loading them into every session.

`CLAUDE.md` is always on, and rules files add a narrower layer on top of that baseline. They live in the project’s `.claude/rules/` directory and can be scoped to specific paths using a `paths` glob in their YAML frontmatter. A rule scoped this way loads into context only when Claude Code works with files matching the pattern, this allows a rule to be applied to one part of the codebase without cluttering the rest of the context.

Note that the scoping comes from the frontmatter, not from file placement. Rules files can be organized into subdirectories of `.claude/rules/` (e.g., `.claude/rules/database/`), but that structure is organizational only; a rules file without a `paths` field loads unconditionally at launch, with the same priority as `CLAUDE.md`, no matter where it sits inside `.claude/rules/`.

In practice, put broad project memory and universal constraints in `CLAUDE.md`, and put narrow, path-specific guidance in rules files scoped with paths. A constraint like “never modify the database schema” lives in `CLAUDE.md` because it applies everywhere. A constraint like “all SQL in the database module must include an explicit transaction boundary” lives in `.claude/rules/database.md` with frontmatter such as:

```
---
paths:
  - "src/db/**/*.sql"
---
```

so it enters context only when Claude is working with those files.

### Hooks: running your own scripts at fixed points in the lifecycle

A **Hook** allows you to intercept and control tool calls before or after they execute. When you write a specific rule in `CLAUDE.md` telling the agent to run `Prettier` after every file edited, the agent will follow it most of the time. Alternatively, a hook makes it happen every single time without exceptions because the hook fires independently of what the model decides to do.

Hooks are defined in settings files and configured using the `/hooks` command. Each hook is bound to a lifecycle event, an optional matcher that scopes it to specific tool types, and a command that runs when the event fires. The core events for most guardrail and automation use cases are:

* `PreToolUse`: Runs before a tool call executes. Because it runs first, a `PreToolUse` hook can examine the tool call and exit with code 2 to block it, writing the reason to stderr as feedback the agent sees. This is how you enforce access controls at the configuration layer rather than hoping the agent respects a `CLAUDE.md` instruction.
* `PostToolUse`: Runs after a tool call completes. Since the call has already happened, this event cannot block it, which makes it the right place for automated side effects: running a code formatter after an edit, triggering tests after a file change, or logging the operation for an audit trail.
* `UserPromptSubmit`: Runs when you submit a prompt, before the model processes it. Use it when you need to inject context or validate the request before any work starts.
* `Stop`: Runs when the model finishes responding. Use it for follow-up actions that belong at the end of a turn, such as notifications, cleanup tasks, or committing the audit log.
* `Notification`: Runs when Claude Code sends a notification, which occurs when Claude needs permission to use a tool or after Claude Code has been idle for 60 seconds. Use it to route those signals to an external channel or logging system.
* `SessionStart`: Runs when a session starts or resumes. Use it to initialize state, validate environment variables, or confirm required services are reachable before the agent begins work.
* `SessionEnd`: Runs when a session ends. Use it for teardown tasks, final audit writes, or notifications that the session has closed.

A hook that blocks edits to a production configuration path using a `PreToolUse` event enforces that constraint at every tool call during every session, regardless of permission mode. That is the difference between a guardrail and a convention.

#### Worked Example

Here is a complete worked example of setting up hooks - we will set these up in `.claude/settings.json` (i.e. at project level). Each hook receives a JSON object on stdin, and exit code 0 means success, exit code 2 is a blocking error whose stderr is shown to Claude, and any other code is a non-blocking error. Your script must therefore read stdin and choose its exit code deliberately.


**Project Layout**

```bash
.claude/
  settings.json
  hooks/
    common.py
    pre_tool_use_guard.py
    post_tool_use_format.py
    user_prompt_submit_pii.py
    stop_run_tests.py
    notification_slack.py
    session_start_check.py
    session_end_audit.py
```

1. `.claude/settings.json`

This single file wires all seven events. The matcher field only applies to tool events (`PreToolUse`, `PostToolUse`). The other events ignore it.

```json
// .claude/settings.json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/pre_tool_use_guard.py"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/post_tool_use_format.py"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/user_prompt_submit_pii.py"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/stop_run_tests.py",
            "timeout": 180
          }
        ]
      }
    ],
    "Notification": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/notification_slack.py"
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/session_start_check.py"
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/session_end_audit.py"
          }
        ]
      }
    ]
  }
}
```
2. `common.py` (shared helpers)

```python
"""Shared helpers for Claude Code hook scripts."""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, NoReturn


def project_dir() -> Path:
    """Returns the project root, falling back to the current directory.

    Returns:
        Path to the directory Claude Code was launched from.
    """
    return Path(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd()))


def read_event() -> dict[str, Any]:
    """Parses the JSON event that Claude Code writes to stdin.

    Returns:
        The decoded event payload.

    Raises:
        SystemExit: With code 1 (non-blocking error) if stdin is not valid JSON.
    """
    try:
        return json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        print(f"Hook received invalid JSON on stdin: {exc}", file=sys.stderr)
        sys.exit(1)


def block(reason: str) -> NoReturn:
    """Exits with code 2 and sends the reason to Claude via stderr.

    Args:
        reason: Human-readable explanation Claude will see as feedback.
    """
    print(reason, file=sys.stderr)
    sys.exit(2)


def append_audit(record: dict[str, Any]) -> None:
    """Appends one JSON line to the project audit log.

    Args:
        record: Fields to store. A UTC timestamp is added automatically.
    """
    log_path = project_dir() / ".claude" / "audit" / "audit.jsonl"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    record = {"ts": datetime.now(timezone.utc).isoformat(), **record}
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record) + "\n")
```

3. `PreToolUse: block edits to production config`

Scenario: the repo holds credit-policy thresholds in `config/prod/` and applied database migrations. A change there needs a reviewed pull request, never an agent edit.

```python
#!/usr/bin/env python3
"""PreToolUse hook: block edits to protected BFSI configuration paths."""

from __future__ import annotations

from pathlib import PurePosixPath

from common import append_audit, block, read_event

# Paths relative to the repo root that the agent may never modify.
PROTECTED_PREFIXES = (
    "config/prod/",          # credit-policy cut-offs, interest rate tables
    "db/migrations/applied/",  # migrations already run in production
    ".github/workflows/",    # deployment pipelines
)


def is_protected(file_path: str, project_root: str) -> bool:
    """Checks whether a path falls under a protected prefix.

    Args:
        file_path: Absolute or relative path the tool wants to modify.
        project_root: Absolute path of the project root.

    Returns:
        True if the path is inside a protected location.
    """
    normalised = file_path.replace("\\", "/")
    root = project_root.replace("\\", "/").rstrip("/") + "/"
    if normalised.startswith(root):
        normalised = normalised[len(root):]
    # Collapse "../" segments so "src/../config/prod/x" cannot slip through.
    parts: list[str] = []
    for part in PurePosixPath(normalised).parts:
        if part == "..":
            if parts:
                parts.pop()
        elif part != ".":
            parts.append(part)
    clean = "/".join(parts)
    return any(clean.startswith(prefix) for prefix in PROTECTED_PREFIXES)


def main() -> None:
    event = read_event()
    tool_input = event.get("tool_input", {})
    file_path = tool_input.get("file_path", "")
    if file_path and is_protected(file_path, event.get("cwd", "")):
        append_audit(
            {"event": "blocked_edit", "tool": event.get("tool_name"), "path": file_path}
        )
        block(
            f"Blocked: {file_path} is a protected path. Production config and "
            "applied migrations change only through a reviewed pull request. "
            "Propose the change as a diff in chat instead."
        )


if __name__ == "__main__":
    main()
```

4. `PostToolUse`: format and lint every edited Python file

The edit has already happened, so this hook cannot undo it. It cleans up and reports problems back to Claude.

```python
#!/usr/bin/env python3
"""PostToolUse hook: run ruff on every Python file Claude edits."""

from __future__ import annotations

import subprocess
import sys

from common import append_audit, block, read_event


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    """Runs a command and captures its output.

    Args:
        cmd: Command and arguments.

    Returns:
        The completed process with stdout and stderr as text.
    """
    return subprocess.run(cmd, capture_output=True, text=True, timeout=60, check=False)


def main() -> None:
    event = read_event()
    file_path = event.get("tool_input", {}).get("file_path", "")
    if not file_path.endswith(".py"):
        sys.exit(0)

    run(["ruff", "format", file_path])
    lint = run(["ruff", "check", "--fix", file_path])
    append_audit({"event": "file_edited", "path": file_path, "lint_ok": lint.returncode == 0})

    if lint.returncode != 0:
        # Exit 2 shows stderr to Claude so it fixes the remaining issues.
        block(f"ruff found issues in {file_path}:\n{lint.stdout}")


if __name__ == "__main__":
    main()
```

5. `UserPromptSubmit`: stop customer identifiers reaching the model

This hook runs before the model sees your prompt. It rejects prompts containing an Indian PAN or Aadhaar-shaped number, and otherwise injects the current git branch as context.

```python
#!/usr/bin/env python3
"""UserPromptSubmit hook: reject prompts that contain customer identifiers."""

from __future__ import annotations

import re
import subprocess

from common import block, read_event

PAN_PATTERN = re.compile(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b")          # e.g. ABCDE1234F
AADHAAR_PATTERN = re.compile(r"\b\d{4}\s?\d{4}\s?\d{4}\b")      # 12 digits


def contains_identifier(text: str) -> str | None:
    """Detects PAN or Aadhaar-shaped values in text.

    Args:
        text: The prompt submitted by the user.

    Returns:
        The identifier type found, or None if the text looks clean.
    """
    if PAN_PATTERN.search(text):
        return "PAN"
    if AADHAAR_PATTERN.search(text):
        return "Aadhaar"
    return None


def current_branch() -> str:
    """Returns the current git branch name, or 'unknown' on failure."""
    result = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        capture_output=True, text=True, check=False,
    )
    return result.stdout.strip() or "unknown"


def main() -> None:
    event = read_event()
    found = contains_identifier(event.get("prompt", ""))
    if found:
        # Exit 2 on this event blocks the prompt and shows the message to you.
        block(f"Prompt rejected: it appears to contain a {found} number. "
              "Replace real customer data with masked test values and resubmit.")
    # For this event, stdout on exit 0 is added to Claude's context.
    print(f"Context: working on git branch '{current_branch()}'.")


if __name__ == "__main__":
    main()
```

6. `Stop`: do not let Claude finish while tests fail

```python
#!/usr/bin/env python3
"""Stop hook: run the fast test suite before Claude ends its turn."""

from __future__ import annotations

import subprocess
import sys

from common import block, read_event


def main() -> None:
    event = read_event()
    # Without this guard, a failing suite would force Claude to continue forever.
    if event.get("stop_hook_active"):
        sys.exit(0)

    result = subprocess.run(
        ["pytest", "-x", "-q", "-m", "not slow", "tests/"],
        capture_output=True, text=True, timeout=150, check=False,
    )
    if result.returncode != 0:
        # Exit 2 on Stop tells Claude to keep working, with this feedback.
        tail = "\n".join(result.stdout.splitlines()[-25:])
        block(f"Tests are failing. Fix them before finishing:\n{tail}")


if __name__ == "__main__":
    main()
```

7. `Notification`: route permission prompts to Slack

```python
#!/usr/bin/env python3
"""Notification hook: forward Claude Code notifications to a Slack channel."""

from __future__ import annotations

import json
import os
import sys
import urllib.request

from common import read_event


def post_to_slack(webhook_url: str, text: str) -> None:
    """Posts a plain-text message to a Slack incoming webhook.

    Args:
        webhook_url: Slack incoming-webhook URL.
        text: Message body.
    """
    request = urllib.request.Request(
        webhook_url,
        data=json.dumps({"text": text}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    urllib.request.urlopen(request, timeout=5).close()


def main() -> None:
    event = read_event()
    webhook = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook:
        sys.exit(0)  # Silently skip when the webhook is not configured.
    message = event.get("message", "Claude Code needs your attention.")
    try:
        post_to_slack(webhook, f"Claude Code ({event.get('cwd', '')}): {message}")
    except OSError as exc:
        print(f"Slack notification failed: {exc}", file=sys.stderr)
        sys.exit(1)  # Non-blocking: the session continues.


if __name__ == "__main__":
    main()
```

8. `SessionStart`: validate the environment before work begins

```python
#!/usr/bin/env python3
"""SessionStart hook: confirm required configuration exists."""

from __future__ import annotations

import os

from common import append_audit, read_event

REQUIRED_ENV = ("DATABASE_URL", "BUREAU_API_BASE_URL")  # e.g. credit-bureau sandbox


def missing_variables() -> list[str]:
    """Lists required environment variables that are unset or empty.

    Returns:
        Names of the missing variables.
    """
    return [name for name in REQUIRED_ENV if not os.environ.get(name)]


def main() -> None:
    event = read_event()
    missing = missing_variables()
    append_audit({"event": "session_start", "source": event.get("source"), "missing_env": missing})

    # stdout from SessionStart is added to Claude's context.
    if missing:
        print("WARNING: missing environment variables: " + ", ".join(missing) + ". "
              "Do not attempt anything that needs the database or bureau API.")
    else:
        print("Environment check passed. Use the sandbox bureau endpoint only.")


if __name__ == "__main__":
    main()
```

9. `SessionEnd`: write the final audit record

```python
#!/usr/bin/env python3
"""SessionEnd hook: record why and when the session closed."""

from __future__ import annotations

from common import append_audit, read_event


def main() -> None:
    event = read_event()
    append_audit(
        {
            "event": "session_end",
            "session_id": event.get("session_id"),
            "reason": event.get("reason"),  # e.g. "clear", "logout", "exit"
        }
    )


if __name__ == "__main__":
    main()
```

### Subagents: delegating work to an isolated context

A subagent is a specialized assistant that Claude Code can delegate tasks to, and each assistant runs a task in its own separate context and returns only its output. It does not inherit your main conversation history, the files you have accumulated in context, or your current session state. When you send a task to a subagent, it starts from a clean slate, does the work, and hands back the result.

The built-in subagents differ in what they load at startup; this difference determines how your project rules apply. Always check the current list in the Claude Code docs, because the set has grown over time, but know that the specific split that affects your project rules holds across versions. The Explore and Plan built-in subagents skip `CLAUDE.md` and git status to keep research fast and cheap. They are optimized for speed, so project-level rules and repository state defined in `CLAUDE.md` are not in their context when they run. The general-purpose subagent loads both. If you delegate a task to Explore or Plan and a rule from your `CLAUDE.md` applies, it’s because that context was not loaded. For tasks where your project constraints must be respected, use the general-purpose subagent or a custom subagent that explicitly loads the rules it needs.

Custom subagents also do not automatically see your skills. If you define a custom subagent in `.claude/agents` and it needs a specific skill, you must explicitly list that skill in the agent’s front matter. Built-in agents do not have preloaded skills. If a built-in agent needs skill-backed behavior, the correct path is to create a custom subagent with those skills listed in its configuration.

The map below names each mechanism, what it loads, when it runs, its context cost, and what belongs in it. Use it to decide which mechanism carries a specific piece of project knowledge, since each one makes a different tradeoff between how much context it costs and how reliably it applies. Flip each card for the full picture.

<< TO DO - the map at bottom>>