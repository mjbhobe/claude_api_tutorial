# CLI install and prerequisites across OS and platforms

## Installation and environments

<span style="font-size: 1.25em;">_The install is one command. Getting there is the work._</span>

Before any developer on a client engagement runs Claude Code, you need to confirm the environment. This lesson covers the pre-kickoff checklist you send to IT, the clean install walk-through, and how to diagnose what breaks when something goes wrong.

## Before you begin

**Confirm the environment before install day, not during it!**

Setup failures during a client kickoff are almost always avoidable. The 30-Day Activation Plan is explicit: confirm blockers before kickoff, not at it. This means one short call or checklist exchange with the client's IT team in the week prior.

Three things determine whether install day goes cleanly: whether the target OS is supported, whether the client's network can reach Anthropic's endpoints, and how Claude Code will be authenticated for the developer cohort. All three are answerable in advance, so none require a developer to be present. This is a conversation with IT.

> [!Warning]
> **Engagement principle**
> 
> If install day is the first time you're checking the environment, you're already behind.

## Platform support

<span style="font-size: 1.25em;">_`macOS`, `Linux`, and `Windows` are all natively supported. Windows has two paths._</span>

Most enterprise developer fleets are a mix. Know the Windows options before kickoff so you can advise the client's IT team on which path fits their environment.

### macOS

Claude Code runs natively on macOS. The install is the same whether developers are on Apple Silicon (M1+) or Intel machines. No additional setup beyond the curl install command. If the team uses a corporate proxy or custom certificate authority, point `NODE_EXTRA_CA_CERTS` at the CA certificate file.

### Linux

Claude Code runs natively on Linux. Common distributions (Ubuntu 20.04+, Debian 10+, Alpine 3.19+) are all supported. The install is the standard curl command. Like macOS, proxy and certificate handling works through standard environment variables: `HTTPS_PROXY` (or `HTTP_PROXY`) and `NODE_EXTRA_CA_CERTS`.

### Windows: `Native` Path

Claude Code runs natively on Windows without requiring WSL or any Linux layer. Developers launch it from PowerShell or CMD. Native Windows is the simpler path for most teams, requiring no IT provisioning beyond network access. Git for Windows is optional but recommended; without it, Claude Code uses PowerShell as its shell instead of Git Bash. Confirm with IT before kickoff if this trade-off fits the team's workflow.

### Windows: `WSL` Path

WSL (Windows Subsystem for Linux) is the right choice when the team needs Linux toolchains or wants sandboxing unavailable on native Windows. WSL requires IT enablement on managed machines. If developers choose this path, they install Claude Code inside the WSL environment; it then behaves identically to the Linux install. WSL 2 is recommended for performance and isolation.

## Installation

<span style="font-size: 1.25em;">_One command. What happens after it runs is the part to prepare for._</span>

The install script handles the runtime setup. Authentication is the first decision point after it completes.

The install command varies by OS. On macOS and Linux, use the curl installer. On Windows, use PowerShell (recommended) or CMD.

**macOS and Linux**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows (PowerShell, recommended)**

```powershell
irm https://claude.ai/install.ps1 | iex
```

**Windows (CMD)**

```bash
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

After the install completes, Claude Code opens a terminal prompt asking how the developer wants to authenticate. There are two paths, and the choice shapes your entire cohort setup and whether IT needs to be involved.

Browser-based login

The developer presses Enter at the authentication prompt. A browser window opens to a login page where they sign in with their Anthropic account (Team or Enterprise subscription). The browser returns a session token to the terminal, and Claude Code is ready to use. This is the standard path for interactive developers on a Team or Enterprise plan. No IT involvement required for key management; authentication stays at the individual level.

API key entry

The developer enters an API key directly at the prompt. This is the standard path for headless use, CI pipelines, or automated workflows, covering any scenario where the developer isn't logging in through a browser. API key distribution requires IT coordination: the key must be created in the Anthropic console, distributed securely (environment variable, secrets vault, or secure file), and rotated periodically. For enterprise cohort deployments where multiple developers share a key, confirm this approach with IT before kickoff: it shapes your provisioning workflow.