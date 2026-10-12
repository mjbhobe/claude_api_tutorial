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

Three outcomes from a trust check
Enable. Source, permissions, and appropriateness all clear.

Escalate. The Skill is useful but the source is unknown or the permissions look broad so route it to your admin or security function for review.

Decline. The permissions are clearly disproportionate or the source cannot be established, and no review would change that.

The judgment is identifying which of the three applies.

Worked example: vetting two Skills
Two Skills, two calls
An Anthropic-provided document formatter. Source is trusted, permissions match the task (document handling), appropriate for the need. Enable it.

A third-party 'analytics booster' from an unknown publisher requesting broad data access. Unknown source, disproportionate permissions for the stated purpose. Do not enable without your organization's review. Treat it the way you would any unvetted installed software.

The rule generalizes: evaluate a Skill's source and permissions like you would any software you were about to install on a work machine.

Skills are the sharpest version of feature-level risk, but the same proportionality habit applies to any capability you turn on. Before enabling a feature that can read your data or act on it, a connector, a tool, or an integration, ask the same three questions: who provides it, what does it access, and is that access proportional to what you need. The principle is least privilege: grant the narrowest access that lets the job get done and revisit it when the job changes.


