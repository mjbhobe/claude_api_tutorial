# Deployment Architecture

## Deployment Decision Framework

<span style="font-size: 1.25em;">_One decision shapes the entire engagement._</span>

By the end of this lesson you can recommend a deployment path for any client profile and defend it on billing, auth, compliance, and capability grounds.

### Why this decision is hard to reverse

<span style="font-size: 1.15em;">_The path sets the rails before anyone writes a prompt_</span>

Where the client's Claude Code traffic runs determines who bills them, how users authenticate, where usage data lands, and which features exist at all.

* **Procurement** signs against the billing route
* **Security** reviews the auth model
* **Finance** builds chargeback on the cost-tracking surface

Reversing the path after rollout means re-running all three workstreams, which is why on a standard 30-day activation this recommendation lands in pre-kickoff, the two weeks before Day 0, alongside the security questionnaire and org-level setup, not in a mid-engagement change request. Treat it the way you'd treat a platform selection in any modernization engagement: a one-way door unless someone pays to walk back through it.

> <small>**WORKING RULE**</small>
>
> The client's existing cloud commitments and compliance posture pick the path. Your job is to surface them before the client picks by default.

### The Four Paths

<span style="font-size: 1.15em;">_Same Claude Code, four different rails_</span>

The CLI is identical on every path. What changes is everything around it.

| | |
| :-- | :-- |
| <span style="font-size: 1.25em">**01**</span><br><br>**Claude for Enterprise (direct)**<br><br>Anthropic's recommended default. Seat-based contract, **SSO and domain capture**, role-based permissions, managed policy settings, compliance API. The only path that bundles Claude on the web and the only path eligible for **zero data retention**. Auth is Claude.ai SSO; cost tracking lives in the usage dashboard. | <span style="font-size: 1.25em">**02**</span><br><br>**Amazon Bedrock**<br><br>Model traffic stays inside the client's AWS account. PAYG billing through AWS, so spend burns down **existing AWS commitments**. Auth via IAM or Bedrock API keys, audit via CloudTrail, cost tracking in Cost Explorer, content filtering via Bedrock Guardrails. The client owns model enablement per account and region. |
| <span style="font-size: 1.25em">**03**</span><br><br>**Google Vertex AI**<br><br>GCP-native equivalent. Billing through GCP, auth via **GCP credentials** and Application Default Credentials, IAM roles, Cloud Audit Logs. Model access is requested per project through Model Garden and can take 24 to 48 hours to approve, which matters for activation timelines. Supports global, multi-region, and regional endpoints. | <span style="font-size: 1.25em">**04**</span><br><br>**Microsoft Foundry**<br><br>Azure-native path. Billing through Azure, auth via API key or **Microsoft Entra ID**, RBAC policies, Azure Monitor. The client provisions Claude model deployments in the Foundry portal. One nuance to know cold: Foundry requests route to Anthropic-operated infrastructure, unlike Bedrock and Vertex. That changes the data residency conversation, and Lesson 3.5 covers how. |
| | |

### The decision drivers

<span style="font-size: 1.15em;">_Four questions, asked in this order_</span>

Work through these in discovery. The client's answers do the narrowing.

| | |
| :-- | :-- |
| # 1 | **Where do cloud commitments sit?**<br><br>A committed-spend agreement the client needs to burn down, an AWS EDP (Enterprise Discount Program), GCP CUD (Committed Use Discount), or Azure MACC (Microsoft Azure Consumption Commitment), is the single strongest pull toward the matching cloud path. Spend that counts against the commitment is money the client considers already spent. Ask procurement, not just IT. |
| # 2 | **How does procurement want to buy?**<br><br>Seat-based subscription through a new Anthropic contract, or PAYG through a cloud marketplace vendor they already have on paper? Many enterprises can approve marketplace spend in days and a new vendor in months. This decides timelines as much as architecture. |
| # 3 | **What does the compliance posture demand?**<br><br>If the client requires **zero data retention**, that is Enterprise direct only. If they require traffic to stay inside their own cloud tenancy and regions, that points to Bedrock or Vertex. Get the security questionnaire early; Lesson 3.5 gives you the answers it will ask for. |
| # 4 | **Who manages users and budgets?**<br><br>Enterprise direct gives admins seat management, managed policy settings, and a usage dashboard out of the box. On the cloud paths the client builds the equivalent from IAM plus cloud cost tooling, or adds an **LLM gateway** for central auth and budgets. That gateway pattern is Lesson 3.4. |
| | |

### The trade-off to name out loud

<span style="font-size: 1.15em;">_Cloud-native control, or the full product_</span>

Every path recommendation is a trade. Saying the trade explicitly is what separates a recommendation from a preference.

| | |
| :-- | :-- |
| <sub>**CLOUD PROVIDER PATHS**</sub><br><br><span class="font-size: 1.25em">**The client's perimeter, the client's tooling**</span> | <sub>**CLAUDE FOR ENTERPRISE DIRECT**</sub><br><br><span class="font-size: 1.25em">**The full surface, managed by Anthropic**</span> |
| Traffic and billing inside infrastructure the client already governs. IAM they already audit, cost tooling finance already uses, commitments procurement already signed. The cost: no bundled Claude on the web, no ZDR, and a handful of capability gaps you will flag in Lesson 3.2. Two consequences hit the activation directly:<br><br>• <sup>–</sup> **Own model version pinning:** unpinned aliases resolve to defaults that can lag new releases or break users when a model isn't enabled in their account yet; pin versions in managed settings before rollout<br><br>• <sup>–</sup> **Build the usage dashboard:** cost reporting gets assembled from Cost Explorer, GCP Billing, or Azure Cost Management, or centralized through the gateway pattern in Lesson 3.4 | One subscription covers Claude Code and Claude on the web, with SSO, seat management, managed settings, compliance API, and ZDR eligibility. The cost: a new vendor relationship, seat-based pricing rather than committed-spend burn-down, and model traffic to Anthropic's platform rather than the client's own tenancy. |
| | |

### From decision to Day -14

The recommendation writes your pre-kickoff checklist
On a 30-day activation, pre-kickoff runs from Day -14 to Day 0. Each path puts different blockers on that list, and some have lead times you cannot compress.

| | |
| :-- | :-- |
| <sub>**ENTERPRISE DIRECT**</sub><br><span class="font-size: 1.15em">**Identity is the long pole**</span><br><br>• <sup>–</sup> **Configure** SSO and domain capture with the client's IdP team<br><br>• <sup>–</sup> **Map** seat list and role assignments<br><br>• <sup>–</sup> **Apply** managed policy settings<br><br>• <sup>–</sup> **Submit** ZDR enablement request to the Anthropic account team if required; it is confirmed per organization | <sub>**AMAZON BEDROCK**</sub><br><span class="font-size: 1.15em">**Account plumbing, mostly same-day**</span><br><br>• <sup>–</sup> **Submit** use-case form per AWS account (access is immediate)<br><br>• <sup>–</sup> **Create** IAM policy for model invocation and inference profiles<br><br>• <sup>–</sup> **Enable** Claude models in target regions<br><br>• <sup>–</sup> **Pin model IDs** in shared settings before anyone installs |
| <sub>**GOOGLE VERTEX AI**</sub><br><span class="font-size: 1.15em">**File the access request on Day 1**</span><br><br>• <sup>–</sup> **Enable** Vertex AI API on the project<br><br>• <sup>–</sup> **Request** Claude access in Model Garden (approval can take **24 to 48 hours**)<br><br>• <sup>–</sup> **Confirm** quota in the target region<br><br>• <sup>–</sup> **Pin** model IDs in shared settings<br><br><sub>The approval wait is the reason this can't start the week of kickoff.</sub> | <sub>**MICROSOFT FOUNDRY**</sub><br><span class="font-size: 1.15em">**Provision deployments, fix the versions**</span><br><br>• <sup>–</sup> **Provision** Foundry resource<br><br>• <sup>–</sup> **Create** Claude model deployments with **fixed versions** rather than auto-update<br><br>• <sup>–</sup> **Agree** Entra ID roles or API key handling with the identity team<br><br>• <sup>–</sup> **Pin** deployment names in settings |
| | |

## Feature Parity Gaps and Flags

<span style="font-size: 1.15em;">_Flag the gaps before the contract_</span>

By the end of this lesson you can name the capability gaps of each deployment path and put them in front of the client without losing the deal.

### Why timing determines the outcome

<span style="font-size: 1.15em;">_Every gap gets discovered. The only question is by whom, and when._</span>

In Lesson 3.1 you recommended a path. The same CLI runs on all of them, but the surface around it differs, and those differences surface mid-activation if you let them.

On a 30-day activation the pattern is predictable:

* **Week one:** a champion asks where a feature went
* **Week two:** the CoE asks why the metrics dashboard is empty
* **Day 30:** the biggest-gaps report either contains items the client has known about since contract time, or items they're hearing for the first time with your name attached.

A one-page gap memo, delivered with the path recommendation before signature, is the cheapest insurance in this course. It's the same discipline as flagging scope exclusions in an SOW: nobody disputes a line they agreed to.

> <small>**WORKING RULE**</small>
>
> A gap flagged at contract time is consulting. The same gap discovered in week three is a defect with your name on it.

### The Gap Map

<span style="font-size: 1.15em;">_Six gaps that belong in your memo_</span>

These are the differences between the cloud paths and Enterprise direct that clients actually hit. Match them to the path you recommended in 3.1.

| | |
| :-- | :-- |
| <sub>**BEDROCK · CAPABILITY**</sub><br><span class="font-size: 1.15em">**WebSearch is unavailable**</span><br><br>The built-in WebSearch tool does not work on Bedrock. Teams that lean on live documentation lookups need an approved MCP alternative, scoped during pre-kickoff, not improvised in week two. | <sub>**ALL CLOUD PATHS · PRODUCT SURFACE**</sub><br><span class="font-size: 1.15em">**No bundled Claude on the web**</span><br><br>Only Teams and Enterprise direct include the web surface. On Bedrock, Vertex, or Foundry, business stakeholders have no chat surface unless the client buys one separately. This surfaces the first time an executive asks for a demo. |
| <sub>**ALL CLOUD PATHS · COMPLIANCE**</sub><br><span class="font-size: 1.15em">**Anthropic ZDR does not apply**</span><br><br>Zero data retention is an Enterprise-direct capability. On the cloud paths, retention follows the provider policies the client already governs. Accurate framing, as you practiced in 3.1: different control, not absent control. | <sub>**ALL CLOUD PATHS · OPERATIONS**</sub><br><span class="font-size: 1.15em">**Model versions are the client's job**</span><br><br>Aliases like **sonnet** resolve to defaults that can lag releases or point at models the account hasn't enabled. Background tasks also default to the primary model rather than a cheaper Haiku-class one. Pin versions in shared settings before rollout. |
| <sub>**ALL CLOUD PATHS · MEASUREMENT**</sub><br><span class="font-size: 1.15em">**Telemetry defaults to off**</span><br><br>Anthropic metrics, error reporting, and **/feedback** submission are disabled by default on third-party paths; feedback writes a local bundle instead. The adoption metrics the CoE reviews weekly need OTel or a gateway, which Lesson 3.4 covers. | <sub>**VERTEX · LEAD TIMES AND DEFAULTS**</sub><br><span class="font-size: 1.15em">**Vertex has its own fine print**</span><br><br>• <sup>–</sup> <span class="font-size: 1.15em">**Allow 24 to 48 hours for Model Garden access approval**</span><br><br>• <sup>–</sup> <span class="font-size: 1.15em">**Enable MCP tool search explicitly:**</span> off by default, so large tool catalogs load upfront if left unconfigured<br><br>• <sup>–</sup> <span class="font-size: 1.15em">**Verify prompt caching by region:**</span> availability varies on both Vertex and Bedrock; if cache counts sit at zero, check the region |
| | |

### The conversation

<span style="font-size: 1.15em;">_A gap memo is one page, not a risk register_</span>

Structure each line the same way:

* **Name the gap:** which capability is absent or reduced on this path
* **Place the moment:** which week, which person, which meeting the client would have hit it
* **Lead with the mitigation:** the plan already in place, stated before the limitation

`"WebSearch is unavailable on Bedrock; your platform docs team would hit this in week one; we'll scope an approved MCP alternative in pre-kickoff"` reads as preparation. A bare feature comparison table reads as a reason to stall the deal. Lead with the mitigation, and the memo becomes evidence you've done this before.

## Corporate Proxy Configuration

<span style="font-size: 1.25em;">_Day 1 lives or dies at the proxy_</span>

By the end of this lesson you can configure Claude Code for a proxied, TLS-inspected corporate network and hand the client's network team the exact allowlist they'll ask for.

### Where installs break

<span style="font-size: 1.15em;">_The first support ticket of every enterprise activation is a network ticket_</span>

The activation plan calls it `setup support: confirm blockers prior to kickoff."` In practice it means one thing: find out what sits between the developer's terminal and the model endpoint before forty people install at once.

Two different components can sit in that path, and they solve different problems. A corporate proxy routes outbound traffic through the client's network perimeter for monitoring and policy enforcement; you configure Claude Code to pass through it. An LLM gateway sits in front of the model provider to handle auth, budgets, and usage attribution; that's Lesson 3.4. They stack: plenty of clients run both. This lesson is the perimeter half, and it's pure pre-kickoff work, because the failure mode is forty developers with hanging terminals in the first hour of Week 1.

| | |
| :-- | :-- |
| <sub>**CORPORATE PROXY · THIS LESSON**</sub><br><br><span class="font-size: 1.25em">**Gets traffic out of the building**</span><br><br>The client's existing network perimeter: HTTP/HTTPS proxy, TLS inspection, firewall allowlists. Claude Code respects the standard proxy environment variables. Owned by the network and security teams. | <sub>**LLM GATEWAY · LESSON 3.4**</sub><br><br><span class="font-size: 1.25em">**Controls what happens to model traffic**</span><br><br>Centralized auth, usage tracking, budgets, audit. A service the client deploys deliberately, not perimeter plumbing they already have. Configured through base-URL overrides rather than proxy variables. |
| | |

### The proxy variables

Four environment variables cover most networks
Configuration detail ahead: developers and architects, this is yours. Business-facing consultants can skip to Topic 4, where the allowlist conversation lives.

```bash
# Route Claude Code through the corporate proxy export 
HTTPS_PROXY=https://proxy.client.com:8080 
# HTTP fallback if the proxy has no HTTPS endpoint
export HTTP_PROXY=http://proxy.client.com:8080 
# Keep internal hosts off the proxy (comma- or space-separated) 
export NO_PROXY="localhost,.client.com,169.254.169.254" 
# Proxy requires basic auth? Credentials go in the URL -- # from a secrets manager, never hardcoded in a script 
export HTTPS_PROXY=http://user:pass@proxy.client.com:8080
```

Proxy env vars are OS-level and cannot be set via Claude Code's settings files. To deploy them org-wide, use MDM: **Jamf** or **Kandji** on macOS, **Windows registry policy on Windows**. 

Two boundaries to know before the client asks:

* **Rule out SOCKS proxies:** not supported; if the client runs SOCKS for other engineering tools, it's not a viable path for Claude Code
* **Escalate NTLM or Kerberos auth to the gateway:** Claude Code can't speak either protocol directly; an LLM gateway that handles enterprise auth becomes the answer, which is one more reason 3.4 matters

### TLS inspection and trust

<span style="font-size: 1.15em;">_"Self-signed certificate in chain" means the proxy is working as designed_</span>

TLS-inspecting proxies like Zscaler or Netskope re-sign traffic with the corporate root CA. Claude Code trusts the OS system trust store by default, so on a well-managed fleet this usually just works.

When it doesn't, the corporate root certificate isn't where Node can see it. The fix is to point at it directly, not to disable verification. Any suggestion of turning off TLS checks fails the client's own security review, and it should.

```bash
# Trust the corporate root CA directly 
export NODE_EXTRA_CA_CERTS=/etc/ssl/corp-root-ca.pem 
# Control which trust stores are used (default: system) 
export CLAUDE_CODE_CERT_STORE=system 
# Client-certificate (mTLS) environments 
export CLAUDE_CODE_CLIENT_CERT=/path/to/client-cert.pem 
export CLAUDE_CODE_CLIENT_KEY=/path/to/client-key.pem
```

### The allowlist conversation

<span style="font-size: 1.15em;">_"Which domains does this thing need?" deserves a prepared answer_</span>

The network team will ask. Handing them the list in the first meeting, with rationale per domain, is the difference between a same-week approval and a three-week change request.

| | |
| :-- | :-- |
| <sub>**MODEL AND API**</sub><br><span class="font-size: 1.15em">**api.anthropic.com**</span><br><br>Claude API requests on the direct path, and the<br><span class="font-size: 1.25em">**WebFetch domain safety check**</span><br>on every path. Block it on a Bedrock deployment and WebFetch fails even though model traffic flows fine, unless settings disable the preflight. | <sub>**AUTHENTICATION**</sub><br><span class="font-size: 1.15em">**claude.ai · platform.claude.com**</span><br><br>Account authentication for claude.ai and Console accounts respectively. On Bedrock, Vertex, and Foundry, auth goes to the cloud provider instead, so these mostly matter on the direct path. |
| <sub>**DISTRIBUTION**</sub><br><span class="font-size: 1.15em">**downloads.claude.ai**</span><br><br>Native installer, auto-updater, and plugin executable downloads. Clients that distribute Claude Code through their own artifact registry can often skip this for end users. | <sub>**CLOUD PATHS**</sub><br><span class="font-size: 1.15em">**Provider endpoints instead**</span><br><br>On Bedrock, Vertex, or Foundry, model and auth traffic go to the provider's endpoints, which are usually already reachable. Optional telemetry to Anthropic defaults off, as flagged in 3.2. Verify the final posture with **/status** inside Claude Code. |
| | |

Once the allowlist is approved, the next question from IT is usually: "How do we make sure every developer uses the right configuration?" That is what managed settings is for.

| | |
| :-- | :-- |
| <sub>**WHAT IT IS**</sub><br><span class="font-size: 1.15em">**The org–level policy layer**</span><br><br>`managed-settings.json` sits at the top of Claude Code's settings hierarchy, above user and project settings. Rules set here cannot be overridden by individual developers. Use it to lock permissions, enforce allowed MCP servers, require SSO login, and pin version floors across the org. | <sub>**HOW IT REACHES DEVELOPER MACHINES**</sub><br><span class="font-size: 1.15em">**Three delivery paths**</span><br><br><span class="font-size: 1.25em">Server-managed</span> via the Anthropic admin console, Enterprise only. <span class="font-size: 1.25em">**MDM/OS-level**</span> via plist on macOS or registry on Windows; deploy through Jamf, Kandji, or similar. <span class="font-size: 1.25em">**File-based**</span>: write `managed-settings.json` to the system directory for the OS. All three require admin rights, which is the point. |
| | |

## LLM Gateway Pattern

<span style="font-size: 1.25em;">_A proxy passes traffic. A gateway understands it._</span>

By the end of this lesson, you can explain when a client needs an LLM gateway over a proxy, configure one for any deployment path, and show how session headers turn gateway logs into per-team chargeback.

### Proxy vs. gateway

<span style="font-size: 1.15em;">_The distinction that matters for enterprise clients_</span>

Enterprise clients with multiple development teams making model calls will eventually ask: who is spending what? A proxy cannot answer that question. A gateway can.

| | |
| :-- | :-- |
| <sub>**P R O X Y**</sub><br><br><span class="font-size: 1.25em">**Forwards traffic**</span><br><br>Routes requests from inside the network to an external endpoint. Applies firewall rules, TLS inspection, and egress controls. Sees packets. Does not understand what is inside them. | <sub>**G A T E W A Y**</sub><br><br><span class="font-size: 1.25em">**Understands model traffic**</span><br><br>Parses the request, applies auth policy, attributes cost to a team, enforces rate limits, logs the interaction, and routes to the right provider. The proxy gets traffic out of the building. The gateway governs what happens to it. |
| | |

### What a gateway provides

<span style="font-size: 1.15em;">_Five capabilities a proxy cannot replicate_</span>

A proxy has no concept of a team, a budget, or a provider. A gateway has all three. These are the five things enterprise clients with more than one team will eventually ask for.

| | | |
| :-- | :-- | :-- |
| <span class="font-size: 1.3em">**01**</span><br><br><span class="font-size: 1.15em">**Centralised authentication**</span><br><br>Provider credentials live in one place the platform team controls. Developers hold short-lived gateway tokens.<br><br><span class="font-size: 1.25em">**Credential rotation happens once**</span>, centrally, not across every developer machine. | <span class="font-size: 1.3em">**02**</span><br><br><span class="font-size: 1.15em">**Per-team cost attribution**</span><br><br>Session headers map each request to a team token.[cite: 9] The gateway answers who spent what without parsing request bodies or estimating from cloud invoices. | <span class="font-size: 1.3em">**03**</span><br><br><span class="font-size: 1.15em">**Budget enforcement**</span><br><br>Rate limits and spend caps applied per team at the request boundary, before the model call is made.[cite: 9] This is an enforcement feature, not a reporting feature.[cite: 9] |
| <span class="font-size: 1.3em">**04**</span><br><br><span class="font-size: 1.15em">**Model routing**</span><br><br>Switch providers or model versions behind a stable endpoint.[cite: 9] A client running Bedrock and Vertex side by side presents both through one base URL.[cite: 9] No developer machine changes required on a provider swap.[cite: 9] | <span class="font-size: 1.3em">**05**</span><br><br><span class="font-size: 1.15em">**Compliance audit logging**</span><br><br>Every model interaction logged in the client's own stack. On cloud paths where OTel telemetry to Anthropic defaults off, as covered in 3.2, <span class="font-size: 1.25em">**the gateway audit log is where observability comes from**</span>. | |
| | | |

### Configuration

<span style="font-size: 1.15em;">_A base URL, a token, and a skip flag_</span>

Developers and architects: this section is for you. The pattern is identical across deployment paths. Only the variable names change.

```bash
# Gateway exposing the Anthropic API format 
export ANTHROPIC_BASE_URL=https://llm-gateway.client.com 
# Bedrock behind the gateway
export ANTHROPIC_AUTH_TOKEN=team-token-from-gateway  
export CLAUDE_CODE_USE_BEDROCK=1 
export ANTHROPIC_BEDROCK_BASE_URL=https://llm-gateway.client.com/bedrock 
# Vertex behind the gateway 
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1 
export CLAUDE_CODE_USE_VERTEX=1 
export ANTHROPIC_VERTEX_BASE_URL=https://llm-gateway.client.com/vertex 
export CLAUDE_CODE_SKIP_VERTEX_AUTH=1
```

The skip-auth flags are the centralised-auth payoff in code: Claude Code stops signing requests itself because the **gateway injects provider credentials server-side**. For rotating per-user tokens, configure **apiKeyHelper** in settings to run a script that fetches from the client's vault. One requirement for the gateway team's acceptance criteria: the gateway must forward **anthropic-beta and anthropic-version headers** intact. A gateway that strips them silently degrades Claude Code features, and that failure looks like a product bug until someone inspects the traffic.

### Session headers

<span style="font-size: 1.15em;">_How Claude Code labels its own traffic_</span>

Every Claude Code request carries attribution headers the gateway can read without parsing the request body. These three headers are the foundation of per-team chargeback.

| | |
| :-- | :-- |
| SESSION LEVEL<br><span class="font-size-lg" style="font-size: 1.15em;">**X-Claude-Code-Session-Id**</span><br><br>A unique ID for the current Claude Code session. The gateway aggregates all requests in a session under this ID. This gives you <span class="font-size-xl" style="font-size: 1.35em;">**session-level cost and duration reporting**</span> without touching request bodies. | SUBAGENT LEVEL<br><span class="font-size-lg" style="font-size: 1.15em;">**X-Claude-Code-Agent-Id**</span><br><br>Present on requests from subagents. When Claude Code fans out into parallel subagents, each carries its own agent ID so the gateway can attribute cost to individual agent threads within the session. |
| PARENT RELATIONSHIP<br><span class="font-size-lg" style="font-size: 1.15em;">**X-Claude-Code-Parent-Agent-Id**</span><br><br>Links a subagent to its parent. Enables <span class="font-size-xl" style="font-size: 1.35em;">**full nested agent attribution:**</span> a session that spawns five subagents still rolls up correctly into a single team's cost report at the CoE review. | WHAT THIS ENABLES<br><span class="font-size-lg" style="font-size: 1.15em;">**Per-team chargeback**</span><br><br>Map gateway tokens to teams and the three headers give you cost per team per week, sessions per developer, and budget alerts before the next invoice. The CoE metrics review and the CFO conversation, served by the same data pipe. |
| | |

**Non-technical leads:** these headers are what enable per-team cost reporting in the Day 30 readout. You do not configure them. Claude Code sends them automatically. The gateway reads them.

### Reference implementation

<span style="font-size: 1.15em;">_LiteLLM as the starting point_</span>

Anthropic's gateway documentation uses LiteLLM as its reference implementation. It is not the only option, but it has the most tested configuration patterns for Claude Code deployments.

LiteLLM proxies support both **Anthropic Messages format** and **OpenAI-compatible format** pass-through. For clients who already run OpenAI-format tooling, this means a single gateway can serve both workflows without a separate integration layer. The base-URL override and skip-auth flags documented in Section 3 work identically whether the path is the Anthropic API, Bedrock, or Vertex. Configuration details and currently tested versions are in the Anthropic LLM gateway documentation at `code.claude.com/docs/en/llm-gateway`.

> [!Note]
> <small>SECURITY NOTICE</small>
>
> LiteLLM PyPI versions 1.82.7 and 1.82.8 were compromised with credential-stealing malware. Do not install those versions. Before any client deployment using LiteLLM, verify the current safe version against the Anthropic LLM gateway documentation. This is a supply chain risk, not a product limitation.

> [!Note]
> <small> POSITIONING PRINCIPLE</small>
>
> Every enterprise client with more than one team will eventually ask who is spending what. Recommend a gateway before they ask, not after the first invoice surprises someone.

## Data residency, compliance posture, ZDR eligibility

<span style="font-size: 1.25em;">_Answer the security questionnaire in the room_</span>

By the end of this lesson you can answer the training, retention, and residency questions a client security review asks, and state exactly what ZDR does and doesn't cover.

### The gate

<span style="font-size: 1.15em;">_The questionnaire is the first item in pre-kickoff for a reason_</span>

Every activation plan starts with the security onboarding questionnaire, because nothing else proceeds until it clears. Three questions decide it.

| | |
| :-- | :-- |
| <span class="font-size-lg" style="font-size: 1.25em;">**1**</span> | <span class="font-size-lg" style="font-size: 1.15em;">**"Does our data train your models?"**</span><br><br>Short answer: no, not under commercial terms. The full answer, including the one opt-in exception you must know about, is Topic 2. |
| <span class="font-size-lg" style="font-size: 1.25em;">**2**</span> | <span class="font-size-lg" style="font-size: 1.15em;">**"What do you retain, and for how long?"**</span><br><br>Short answer: governed by your customer agreement; confirm the current retention window with your account team. ZDR is the no-server-side-persistence option on one specific path. Topics 2 and 3. |
| <span class="font-size-lg" style="font-size: 1.25em;">**3**</span> | <span class="font-size-lg" style="font-size: 1.15em;">**"Where does our data physically go?"**</span><br><br>Short answer: it depends on the path you chose in 3.1, and one path behaves differently than clients assume. Topic 4. |
| | |

You've already practiced the stakes: in the Meridian scenario, one wrong ZDR answer in front of a CISO cost more credibility than any architecture diagram earned back. This lesson gives you the complete answers, so the questionnaire becomes a meeting you run rather than a form you fear.

### Training and retention

<span style="font-size: 1.15em;">_The answers, with the nuances that survive fact-checking_</span>

Half-right answers are worse than no answer, because security teams verify. These are the complete versions.

**Training:** Anthropic does not train generative models on code or prompts sent to Claude Code under commercial terms: Team, Enterprise, API, and the cloud paths alike. The one exception is explicit opt-in, such as the Development Partner Program, which an org admin must actively join, and which isn't even available on Bedrock or Vertex. Say "no, unless you explicitly opt in," not "no, never": the qualified version survives the client's own research. Retention: Server-side retention is governed by the customer agreement; confirm the current retention window with your account team or the Anthropic privacy documentation rather than quoting a number that may not match their plan. And the answer endpoint-security teams actually need: Claude Code also caches session transcripts locally on each developer's machine, in plaintext under the user's home directory, configurable via settings. That's a device-management conversation, not a cloud one.

### Encryption at rest

<span style="font-size: 1.15em;">_Where inference data lives, by path_</span>

| | |
| :-- | :-- |
| ANTHROPIC DIRECT<br><span class="font-size-lg" style="font-size: 1.15em;">**AES-256, ZDR available**</span><br><br>Infrastructure-level disk encryption, with zero data retention as the no-server-side-persistence option for eligible Enterprise orgs. Topic 3 covers eligibility. | AMAZON BEDROCK<br><span class="font-size-lg" style="font-size: 1.15em;">**Client's AWS account, KMS optional**</span><br><br>AES-256 with AWS-managed keys, customer-managed keys available through KMS. Retention and key policy are governed by controls the client already audits. |
| GOOGLE VERTEX AI<br><span class="font-size-lg" style="font-size: 1.15em;">**Client's GCP project, CMEK optional**</span><br><br>Google-managed encryption keys by default, customer-managed (CMEK) available. Same logic as Bedrock: the client's cloud governance applies. | MICROSOFT FOUNDRY<br><span class="font-size-lg" style="font-size: 1.15em;">**The one that surprises people**</span><br><br>Foundry is an Azure-native deployment — Azure billing, Microsoft Entra ID authentication, and Azure RBAC policies apply. Confirm the data routing path with Anthropic before advising clients with cloud-specific data residency requirements. The "data never leaves our tenancy" question belongs in the path conversation, not the post-mortem. |
| | |

### ZDR, precisely

<span style="font-size: 1.15em;">_Zero data retention is a scope, not a slogan_</span>

ZDR applies to Claude Code on Claude for Enterprise, enabled per organization by the Anthropic account team after eligibility review. It is not in the standard Enterprise plan by default, and it is not available on the cloud paths.

| | |
| :-- | :-- |
| WHAT IT COVERS<br><span class="font-size-lg" style="font-size: 1.15em;">**Claude Code inference, full stop**</span><br><br>Prompts and model responses from Claude Code sessions are processed in real time and not stored after the response returns, regardless of model, except where law or abuse-handling requires it. Admin capabilities like cost controls, analytics, and audit logs keep working. | WHAT IT DOESN'T, AND WHAT IT DISABLES<br><span class="font-size-lg" style="font-size: 1.15em;">**The trade the client must choose**</span><br><br>Not covered: claude.ai chat, Cowork, admin metadata like seat assignments, and anything third-party MCP servers process. Disabled outright because they require server-side storage: <span class="font-size-xl" style="font-size: 1.3em;">**Claude Code on the web, remote sessions from the desktop app, and /feedback.**</span> And flagged sessions can still be retained up to 2 years under the usage policy. A client who wants ZDR and Claude Code on the web is choosing between them. |
| | |

Also worth saying in the room: analytics under ZDR shows usage metrics but not contribution metrics, so the Day 30 scorecard should be designed around what will actually be measurable. Each new org under the same account needs its own enablement, which is a detail that bites multi-org enterprises at rollout.

### Residency and certifications

<span style="font-size: 1.15em;">_Residency follows the path. Certifications follow the Trust Center_</span>

If the client has a hard residency requirement, the cloud paths are where region control lives: Bedrock offers region selection across AWS regions, Vertex offers global, multi-region, and regional endpoints.

On the direct path, service availability follows Anthropic's supported countries; specific region-level processing guarantees are an account-team conversation, and the honest move is to say so rather than improvise one. For the certification half of the questionnaire, the artifact set is self-serve at `trust.anthropic.com`: SOC 2 Type 2, ISO 27001:2022, ISO/IEC 27017 and 27018 for cloud security and privacy, ISO/IEC 42001 for AI management systems, CSA STAR Level 2, HIPAA with BAA available, GDPR, NIST 800-171 attestation, FedRAMP High through Claude for Government, and annual third-party penetration test summaries. Knowing that list from memory is optional; knowing it's all downloadable the same day the CISO asks is not.

> [!Note]
> <small>WORKING RULE</small>
>
> Answer from the facts you can cite, name the one thing you'll verify, and never improvise a guarantee. Security teams forgive `"I'll confirm the region commitment."` They don't forgive a wrong yes.


