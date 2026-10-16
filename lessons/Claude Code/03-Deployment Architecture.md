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
