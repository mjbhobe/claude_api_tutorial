# Governance, Risk & Responsible Use

<span style="font-size: 1.25em;">_One inappropriate use case can freeze an entire organization's AI program._</span>

Sensitive data uploaded to the wrong place, an untrusted Skill granted broad access, a quiet policy violation at the wrong moment: any of these can trigger a freeze that costs every team the productivity they had gained. Governance is what keeps adoption moving safely, and it is exercised by practitioners, one decision at a time, not by a policy binder on a shelf.

That is the framing for this module: governance is a practitioner skill. The policy sets the boundary, but you are the one who decides, in the moment, whether this use case, this Skill, this upload is appropriate. Two competencies from the AI Fluency Framework govern those decisions. Diligence is about ownership and verification. Delegation supplies the criteria for judging whether a use case is appropriate at all.

## Appropriate vs Inappropriate Use Cases

<span style="font-size: 1.25em;">_Deciding whether a use case is appropriate is a structured evaluation, not a gut feeling._</span>

The same Delegation criteria that map workflow steps also screen whole use cases: reversibility, consequence of error, the need for human creativity or empathy, and accountability. Running them every time turns a vague unease into a defensible call.

## Delegation criteria for screening

| Criterion | The question to ask |
| :-- | :-- |
| Reversibility | Can a wrong output be caught and undone before it causes harm? Irreversible consequences raise the bar sharply. |
| Consequence of error | What is the cost if the output is wrong? Higher consequence demands more human control or rules the use case out. |
| Need for human creativity or empathy | Does the task require judgment, relationship, or care that AI cannot supply? Some work should stay human regardless of capability. |
| Accountability | Who is answerable for the outcome, and can that accountability be exercised over an AI-produced result? |

> [!Tip]
> <small>THE CRITERIA INTERACT: NAME THE LOAD-BEARING ONE</small>
>
> The four criteria are not a checklist where any single failure ends the discussion. They interact. A task can be low-consequence and reversible and still require human review. Accountability cannot be transferred to a model. Drafting a condolence note to a client is low-stakes and fully reversible, yet the relationship element means a person should own it. Conversely, a task can be high consequence but still appropriate with the right gate: a financial summary that feeds a decision is consequential, but if a named reviewer signs off before it is used, the accountability and reversibility are restored. The practical rule is to run all four, then ask which one is load bearing for this specific use case. The **load-bearing** criterion is the one that, if it is changed, would move the use case between classifications. Naming it is what makes your classification defensible to a risk or compliance reviewer.

### Three classifications

Each proposed use case sorts into one of three, with documented rationale:

* **Fully appropriate.** Reversible, low consequence, no special human element. Delegate with normal review.
* **Appropriate with human review.** Useful for AI assistance, but the stakes or accountability require a human gate. Define the gate explicitly.
* **Inappropriate.** The consequence, irreversibility, or human-element requirement means AI should not perform this. Articulate why and name the human role that must own it.

> [!Tip]
> <small>THE GATE IS THE CLASSIFICATION</small>
>
> `"Appropriate with human review"` is the classification people most often get wrong. Often, they stop at the label and never specify the gate. The gate is not `"someone will check it."`
>
> A defined gate establishes three things: who reviews (the role with the accountability, not whoever is free), what they verify (the specific risk the review exists to catch, such as factual accuracy, fairness, or policy compliance), and when in the workflow the review happens (before the output is used, not after). `"A manager reviews the shortlist for adverse-impact patterns before any candidate is contacted"` is a defined gate. `"We will keep a human in the loop"` is not. If you cannot state the gate in that who/what/when form, the use case is not yet ready to run.

### Worked example: a use-case portfolio

1. **Draft internal FAQ from approved policy docs**: Is Fully appropriate. Reversible, low stakes, factual grounding available.
2. **Summarize candidate resumes to a shortlist**: **Appropriate with human review**, and only with bias safeguards. Consequential, fairness-sensitive, accountability rests with the hiring manager; the human owns the selection.
3. **Generate a final medical or legal determination
Inappropriate:** Irreversible consequence and a professional accountability that cannot transfer to a tool. The human professional must make and own the determination.
4. **Draft customer-facing responses to billing complaints:** This is the hard one, because it sits on the line. It is reversible if the response is reviewed before sending, moderately consequential (a wrong answer about a charge erodes trust and can have regulatory weight in some industries), and partly relationship sensitive. The right classification is appropriate with human review, and the load-bearing criterion is accountability: the company owns what it tells a customer about their money. The defined gate: a support agent reads each drafted response for accuracy against the actual account record and adjusts tone before it sends. The interesting governance work is not the obvious "yes" or "no" use cases; it is naming the gate for the ones in the middle.

Articulating why a use case fails the test, and what human role must be retained, is the deliverable. "It feels risky" does not travel; "irreversible consequence plus non-transferable accountability" does.

## Skill Trust and Feature-Level Risk

<span style="font-size: 1.25em;">_A Skill is software. It can access what you give Claude access to during a session and can take actions through code execution. A Skill from an untrusted source is therefore a real risk, and the practical answer to that risk is a source-and-permissions check before you enable it._</span>

### Why untrusted Skills are a risk

Because a Skill runs procedures and can touch data and tools available in the session, one from an unknown source could mishandle data or take unintended actions. "Skills are a black box" is a common organizational worry, and the answer is not blind trust or blanket bans; it is a repeatable trust evaluation.

Trust evaluation before enabling:

1. **Source:** Who published this skill? Anthropic-provided and internally-approved Skills ate the lower-risk starting point.; an unknown third-party Skill demands more scrutiny.
2. **Reach:** Skills do not request permission. A Skill inheriys whatever access the session it runs in already has. Ask instead: what could this Skill reach in the session where it will run, and is that exposure proportional to the task?
    Audit the bundle's contents (instructions, dependencies, bundles files) before enabling; a formatting skill whose instructions roam far beyond formatting is a red flag.
3. **Appropriateness:** Is this Skill the right tool for the task at all, or is it more capability than the job needs?

> [!Tip]
> <small>INTERNAL DOES NOT MEAN VETTED</small>
>
> Source is not a simple trusted-or-untrusted switch. The hardest case is the Skill built by another team inside your own organization. "Internal" feels safe, but it does not mean vetted: the team that built it may have given it broad permission for their own convenience or built it against an older policy. Treat an internal Skill from outside your team the way you would treat software from a sister department, confirm with the publisher what it accesses and why, and check that its permissions still match current policy, before you enable it on your own data. The trust question is "do I know what it does and does its access match the job?"

Failing the trust check does not always mean "never use it." It means do not enable it to your authority alone. The three outcomes are:

### Three outcomes from a trust check

* **Enable.** Source, permissions, and appropriateness all clear.
* **Escalate.** The Skill is useful but the source is unknown or the permissions look broad so route it to your admin or security function for review.
* **Decline.** The permissions are clearly disproportionate or the source cannot be established, and no review would change that.

The judgment is identifying which of the three applies.

### Worked example: vetting two Skills

> [!Note]
> <small>TWO SKILLS, TWO CALLS</small>
>
> **An Anthropic-provided document formatter.** Source is trusted, permissions match the task (document handling), appropriate for the need. Enable it.
>
> **A third-party 'analytics booster' from an unknown publisher requesting broad data access.** Unknown source, disproportionate permissions for the stated purpose. Do not enable without your organization's review. Treat it the way you would any unvetted installed software.

The rule generalizes: evaluate a Skill's source and permissions like you would any software you were about to install on a work machine.

Skills are the sharpest version of feature-level risk, but the same proportionality habit applies to any capability you turn on. Before enabling a feature that can read your data or act on it, a connector, a tool, or an integration, ask the same three questions: who provides it, what does it access, and is that access proportional to what you need. The principle is least privilege: grant the narrowest access that lets the job get done and revisit it when the job changes.

## Data Sensitivity, Privacy & Feature Controls

<span style="font-size: 1.25em;">_Before any data enters any feature, you should know its sensitivity._</span>

Data classification is the habit that prevents leakage, and the feature-specific controls, Incognito, Memory management, and sandbox awareness, are how you act on that classification when persistence or processing is not appropriate.

### Classify before you upload

Sort data into what is safe to use, what needs review first, and what stays out entirely. Public and internal-low-sensitivity material is generally fine; regulated, confidential, or personal data needs a deliberate check against policy before it goes anywhere near a feature. When you are unsure, the safe default is to ask before uploading. Most teams need three tiers they can apply in seconds:

<div style="color: #3fb950; margin-bottom: 1.5em;">
  <strong>Green: Safe to use</strong><br>
  Published material, anonymized or aggregated data, or internal documents already cleared for wide sharing.
</div>

<div style="color: #d29922; margin-bottom: 1.5em;">
  <strong>Yellow: Review first</strong><br>
  Internal documents not meant to leave the company, anything with names or contact details, or draft material tied to a deal or product not yet announced.
</div>

<div style="color: #f85149; margin-bottom: 1.5em;">
  <strong>Red: Keep out unless an approved path exists</strong><br>
  Regulated data (health, financial, government), credentials and secrets, or anything covered by a confidentiality obligation to a third party.
</div>

When you are unsure between two tiers, treat the data as the more sensitive one until you can confirm otherwise.

### Redaction and anonymization

When the substance of a task does not require the sensitive specifics, remove them. Redacting names, account numbers, or identifiers before uploading lets you get the analytical value without exposing the data. Building this habit prevents the most common form of accidental leakage. Redaction works when the task does not depend on the identifiers. Asking for trends across a customer list does not require the customers' names; replacing them with "Customer 1, Customer 2" loses nothing the analysis needs.

<div style="color: #f85149; margin-bottom: 1.5em;">
  <strong><small>TWO REDACTION FAILURE MODES</small></strong><br/><br/>
<strong>1. Partial redaction.</strong> Removing the name but leaving an account number, a rare job title, or a specific date can still identify someone, especially in a small population. Strip every field that could lead to identification.<br/><br/>

<strong>2. Redaction that breaks the task.</strong> If the work genuinely needs the sensitive specifics, redaction is not the answer. It is better to confirm an approved path for that data or keep it out entirely. Redaction is a tool for the case where sensitivity and necessity do not overlap; it is not a way to make any data safe.
</div>

### Feature-specific controls

1. **Code execution sandbox**: Code runs in a sandboxed environment, and uploaded files are processed there.

    Review what you upload before running analysis.

2. **Memory persistence**: Memory carries information across sessions.

    For sensitive work, that persistence may be exactly what you do not want.

3. **Incognito mode**: Keeps the session out of your chat history and Memory. Incognito chats still follow your organization's data-retention policies and can appear in organizational data exports. Memory exclusion and data retention are separate controls.

    Use it for sensitive conversations or confidential inputs that should not surface in history or Memory.

4. **Org-level Memory controls**: Team plans do not have organization-level controls for memory features; on Enterprise, Owners and Primary Owners hold the org-wide Memory controls, including disabling memory for the organization.

    Know which plan you are on and who controls the setting. Verify current behavior at the Claude Help Center memory article (support.claude.com).

The controls are only useful if you reach for the right one at the right moment. The habit is: classify first, then pick the control that matches. Green data needs no special control. Yellow data that should not persist across sessions is the case for Incognito, confidential but not regulated, where you want the analysis now without it entering Memory or chat history (your organization's underlying data-retention policy still applies). Red data needs an approved entry point confirmed before anything is uploaded, regardless of Memory settings. The common error is using Incognito and assuming it makes sensitive data safe.

<div style="color: #f85149; margin-bottom: 1.5em;">
  <strong><small>INCOGNITO DOES NOT MAKE RED DATA SAFE</small></strong><br/><br/>
Incognito controls whether something gets remembered; it does not confirm whether the data was allowed here in the first place. For regulated data, that second question comes first.
</div>

### Awareness across entry points, in plain terms

Different claude.ai entry points may handle data retention differently depending on how your organization has configured Claude. You do not need to memorize the technical detail; you need the habit of asking, when in doubt about a given entry point, before uploading. The plain rule: know your data's sensitivity first, then match the feature and its controls to it.

#### Worked example: four data decisions

<div style="color: #2f81f7; margin-bottom: 1.5em;">
  <strong><small>APPLYING THE TIERS</small></strong>

* <strong>Anonymized survey data for trend analysis.</strong> Green. Safe to upload; use code execution for verified counts. No personal identifiers present.
* <strong>A confidential M&A document for summarization.</strong> Yellow. Needs review against policy first, and Incognito so it does not enter Memory or chat history (it remains subject to organizational data retention). If policy prohibits the entry point, it stays out.
* <strong>A spreadsheet of customer PII for cleanup.</strong> Redact or anonymize the identifiers before upload, or keep it out entirely and confirm the approved path with your admin.
* <strong>Patient records for a healthcare workflow summary.</strong> This is red and it is the case Incognito does not solve. The data is regulated, so the first question is whether this entry point is approved for protected health information at all. If your organization has not confirmed an approved, compliant path for that data, the correct action is to stop and escalate to your admin. For regulated data, "is this allowed here" is settled before "how do I handle it here."
</div>

## Organizational Policies and Diligence as a Habit

<span style="font-size: 1.25em;">_A policy that is followed only when someone is watching is not governance._</span>

The gap between what the policy says and what people do, is exactly where risk lives. Diligence is the habit of applying the governance framework consistently, and of auditing real usage against it to close the gaps.

### Apply governance consistently

Governance compliance is a sustained habit, not a one-time acknowledgment. The standard is to apply the framework on the routine, low-visibility decisions, not only on the obvious high-stakes ones, because the routine decisions are where drift accumulates unnoticed.

### Audit usage against policy

Periodically compare what your team does or is planning to do with Claude against what the policy requires. Where they diverge, you have found a Diligence gap to close: a data type being uploaded that should not be, a review step being skipped, a Skill enabled without vetting. Spotting and closing those gaps is important work.

### Stay current

Policies and capabilities both evolve. A practice that was compliant last quarter may not be after a policy update or a new feature. Staying current with both is part of the habit, so your judgment keeps pace with the tools and the rules.

### Worked example: a mini usage audit

<div style="color: #2f81f7; margin-bottom: 1.5em;">
  <strong><small>THREE GAPS, THREE CLOSEABLE ACTIONS</small></strong><br/>
A team lead reviews a month of the team's Claude use against policy and finds three gaps: a marketer uploaded an unreleased product spec to a non-approved entry point, a Skill was enabled without a source check, and a recurring client report skipped its required human-review gate twice under deadline pressure.

None was malicious; all were drift. The fixes are habit-level: a reminder on approved entry points, a Skill-vetting step added to the Project setup, and a non-negotiable review gate on client deliverables. The audit converted invisible risk into three closeable actions.
</div>

## Ethical Implications: Bias, Fairness, Transparency

<span style="font-size: 1.25em;">_Ethical risk does not announce itself; it hides in ordinary outputs._</span>

A summary that quietly favors one group, a recommendation built on a biased framing, an AI-assisted document presented as fully human-authored: these are routine outputs with ethical weight. Evaluating for bias, fairness, and transparency belongs in routine review, not a separate ethics exercise.

### Recognize bias and fairness risk

AI-assisted work products can carry bias from the prompt, the framing, or the underlying patterns in how language is generated. In people-facing work, hiring, evaluation, communications to specific groups, check whether the output treats people fairly and whether a framing has tilted the result. The risk is highest where the stakes for individuals are highest.

### Transparency and disclosure

Know when to disclose AI assistance. Some contexts and some organizational policies require it; others treat it as routine tooling. The obligation depends on the setting and the audience, and the responsible default, when unsure, is to disclose rather than to conceal.

### Reasoning through ambiguous cases

Many ethical questions have no rule that settles them cleanly. A structured approach helps: name who is affected, what could go wrong, what the fair outcome looks like, and what disclosure the situation calls for. Reasoning it through, and documenting the reasoning, is the professional standard when no policy gives a direct answer.

<div style="color: #3fb950; margin-bottom: 1.5em;">
  <strong>WHEN REASONING ALONE IS NOT ENOUGH</strong><br/><br/>
Structured reasoning handles most ambiguous cases, but some situations require more than individual judgment. If the affected population is large, the potential harm is significant, or the ethical question touches areas your team does not have standing to resolve the right move is to escalate rather than decide alone. Your organization's AI governance or ethics function exists for exactly these cases. Escalating the question with documented reasoning is more useful than bringing a verdict: it shows you applied the framework, identified where it ran out, and flagged the gap for the right reviewer.
</div>

### Worked example: an ambiguous case

<div style="color: #2f81f7; margin-bottom: 1.5em;">
<strong><small>PERFORMANCE-REVIEW SUMMARIES</small></strong><br/><br/>
A manager uses Claude to draft performance-review summaries from their own notes. Is this appropriate? Working the reasoning: those affected are the employees; the risk is that a generated phrasing introduces an unfair or inconsistent tone across reviews; the fair outcome requires the manager to verify each summary reflects the actual notes and applies a consistent standard; and the setting may call for disclosing that AI assisted the drafting.

The conclusion is appropriate with human review and a fairness check, not a blanket yes or no. The reasoning, not the verdict alone, is what makes the decision defensible.
</div>
