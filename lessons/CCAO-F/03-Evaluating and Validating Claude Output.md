<link rel="stylesheet" href="./tabs.css">

# Evaluating and Validating Claude's Output

> <small>A SHORT CAUTIONARY CASE</small>
>
> A consultant asked Claude to pull supporting statistics for a client market-sizing deck. Claude returned five clean figures with confident framing. Four were sound. One, a growth rate, was fabricated, plausible enough that nobody questioned it. The figures went into a deck, the deck went to a client, and the client's own analyst flagged the fabricated figure in the room.
>
> The ten minutes saved on research cost a credibility hit and a week of rebuilding trust. Nothing about the figure looked wrong on the screen. That is the problem this module is intended to solve: the cost of a missed error is not paid when you save the time, it is paid later, by someone whose trust you needed.
> &nbsp;<br/><br/>

<span style="font-size: 1.25em;">_Claude saved you twenty minutes drafting an analysis. One fabricated figure in that analysis, sent to a client or a regulator, can cost far more than twenty minutes to undo._</span>

This is the asymmetry at the center of professional AI use: the time saved is small and visible, and the cost of an unverified error is large and arrives later.

**This is the largest section of the certification exam, and the reason is accountability**. When you put your name on a deliverable, you own every claim in it, whether you wrote the words or Claude did. This module gives you the discipline to stand behind AI-assisted work.

Two competencies from the AI Fluency Framework anchor the module. _Discernment_ is the skill of critically evaluating output against requirements, sources, and standards. _Diligence_ is deciding when verification is required and taking responsibility for the result. Discernment is how you review; Diligence is why you must.

> **NOTE**
>
> You are accountable for everything you ship, created with Claude's help. Learn to evaluate output systematically, recognize the failure patterns, build verification into your prompts, know the thresholds where human review is mandatory, and choose the output format that matches the reliability the task demands.
> <br/><br/>

## Discernment: Evaluating Accuracy, Completeness, and Fitness

_Evaluation is not a feeling about whether output looks good_. It is a **check against three fixed references**: the `requirements` you set, the `source material`, and the `professional standards` of your field. The discernment protocol is running that check the same way every time, so quality does not depend on how rushed you happen to be.

### Three evaluation references

**Requirements.** Does the output reflect what you asked for? Re-read your own request and confirm each part is addressed, not just the easy parts.

**Source material.** Where the output relies on documents you supplied, does it match them? Trace specific claims back to the source rather than trusting that Claude read carefully.

**Professional standards.** Would this pass in your field? A number without units, a recommendation without reasoning, a citation you cannot locate. These fail professional standards even when they read fluently.

### Stakes calibration

How deeply you review depends on the stakes, and the stakes are domain-dependent, not universal. In zero-tolerance work (legal analysis, financial figures, compliance reporting), accuracy outranks speed entirely, and every claim gets verified. In low-stakes internal brainstorming, a lighter review is appropriate. The risk is applying the same casual review to both. Determine the stakes before you decide the depth of review.

### A three-way triage

After review, sort each output into one of three states, with documented reasoning:

| Verdict | When it applies |
| :-- | :-- |
| Ready to use | Meets requirements, matches sources, clears professional standards. Ship it. |
| Needs revision | Close, but a specific gap remains. Note the gap and iterate. |
| Needs human override | The stakes, the errors, or the uncertainty mean this should not go out on Claude's draft alone. Escalate to a person. |

### Completeness is a separate review

Accuracy asks whether what is present is correct. Completeness asks whether anything is missing. They fail independently: an output can be entirely accurate and still omit the one factor that impacts a decision. Review for both. Missing elements are harder to spot than wrong ones, because nothing on the screen draws your eye to them.

### The protocol on three real outputs

The protocol is most effective on outputs that are not obviously good or bad. Here it is applied to three, each a different verdict.

**Output 1: a competitor-pricing summary.** You asked Claude to summarize three competitors' published pricing from PDFs you uploaded. The summary is clean and well-organized. Running the three references: requirements met (it covers all three competitors), but the source review fails: one price is listed as "$40/user" when the uploaded PDF says "$40/user, minimum 10 seats." The omission changes the comparison. Verdict: needs revision. The fix is a source-restricted re-prompt, not a rewrite.

**Output 2: an internal process recommendation.** You asked for three options to reduce invoice-processing time. The output gives three sensible options with trade-offs. Requirements met, no sources to check against, professional standards cleared, low stakes (internal discussion starter). Verdict: ready to use. Over-verifying this one wastes the time the tool saved.

**Output 3: a compliance-gap analysis.** You asked Claude to compare your data-handling policy against a regulation and flag gaps. It flags four gaps confidently. Requirements appear met, but the regulation was not uploaded, so Claude worked from training-data recall of a rule that may have changed, and the stakes are regulatory. Verdict: needs human override. The output is a useful prompt for a compliance expert, not a substitute for one.

Same protocol, three verdicts. The difference is never how polished the output looks; it is what the three references and the stakes return.

## Hallucinations, Inconsistencies & Bias

<span style="font-size: 1.25em;">_Plausible is not the same as verified. Claude writes fluently whether it is right or wrong, so you cannot rely on tone or confidence to flag an error._</span>

Knowing the specific signatures of failure lets you spot them quickly instead of reading every line with equal suspicion.

###  Hallucination patterns

> [!NOTE]
> **Plausible-but-unsupported claims.** A statement that sounds reasonable and fits the topic, with no basis in the source or in fact. The most dangerous kind, because nothing about it looks wrong.
>
> **Fabricated specifics.** Invented statistics, dates, names, quotations, or citations. Specificity reads as authority, which is exactly why fabricated specifics are persuasive.
>
> **Confident tone masking uncertainty.** Claude rarely hedges in proportion to its actual certainty. A guess and a well-grounded fact arrive in the same assured voice.

### Inconsistencies and bias

> [!NOTE]
> **Internal contradictions.** In a long output, a claim early on can conflict with one later. Long documents are where contradictions hide, because you rarely hold the whole thing in view at once.
>
> **Confirmation bias in framing.** If your prompt implies a preferred answer, Claude may lean toward it. Watch for output that agrees with you a little too readily on a question that should be genuinely open.

> [!TIP]
> <small>A COMPLETENESS FAILURE WORTH REMEMBERING</small>
>
> A common, anonymized field pattern: a professional asks Claude to compare a batch of documents and identify the differences. The output lists several differences and reads as thorough. It missed differences in the single most important file in the batch. Completeness failures concentrate where attention is lowest, and a confident summary of the easy files can mask silence on the hard one.

> [!TIP]
> <small>CAPABILITY HALLUCINATION</small>
>
> Claude can claim to have taken an action it cannot actually take, such as `"I've emailed that to your team"` or `"I've saved the file."` Within `claude.ai`, Claude works with the conversation, connected tools, and uploaded files; it does not perform external actions it was not given a tool for. Treat any claimed external action as unverified until you confirm it happened.

### A failure-pattern gallery

Each pattern below is shown the way it can actually appear, so you recognize the signature rather than the label.

> [!Note]
> <small>FABRICATED SPECIFIC, IN THE WILD</small>
>
> Prompt: "What share of mid-market SaaS firms adopted AI tools in 2025?" Output: "Approximately 63 percent of mid-market SaaS firms adopted at least one AI tool in 2025, up from 41 percent in 2024."<br/>
> The numbers are precise, the trend is plausible, and there is no source. The precision is the tell. Real figures this specific come with a citation; an uncited 63 percent is a number-shaped guess.

> [!Note]
> <small>CONFIDENT TONE MASKING UNCERTAINTY</small>
>
> Prompt: "Is this clause enforceable in our state?" Output: a four-sentence answer stating it is enforceable, in the same assured voice Claude uses for arithmetic.<br/> Legal enforceability is jurisdiction-specific and date-sensitive, exactly the kind of claim that should hedge and does not. Assurance is not evidence.

> [!Note]
> <small>INTERNAL CONTRADICTION ACROSS A LONG OUTPUT</small>
>
> In a ten-page market analysis, page two states the addressable market is "roughly $2 billion" and page eight builds a projection on "the $2.6 billion market." Both read fine in isolation. The contradiction only becomes visible if you hold the whole document in view, which is why long outputs need a consistency pass, not just a paragraph-by-paragraph read.

> [!TIP]
> <small>HOW TO READ THE GALLERY</small>
>
> None of these outputs looks broken. That is the point of the lesson: the failure modes are designed, by the nature of fluent generation, to pass a casual read. You catch them by knowing the signatures and checking against sources, not by waiting for something to look wrong.

## Fact Checking and Grounding Techniques

<span style="font-size: 1.25em;">_The strongest verification is built into the prompt, before the output exists._</span>

A few prompt habits cut hallucinations at the source rather than catching them after the fact, and they make whatever remains far easier to audit.

<link rel="stylesheet" href="./tabs.css">

<div class="jb-tabs-container">
<input type="radio" name="jb-tab-group" id="tab1" checked>
<input type="radio" name="jb-tab-group" id="tab2">
<input type="radio" name="jb-tab-group" id="tab3">

<div class="jb-tabs-header">
<label class="jb-tab-label" for="tab1">Prompt for verifiability</label>
<label class="jb-tab-label" for="tab2">Grounding techniques</label>
<label class="jb-tab-label" for="tab3">Verbatim prompts</label>
</div>

<div class="jb-tab-content">
<div class="jb-tab-panel" id="content1">
<p><strong>Permit "I don't know."</strong> Tell Claude explicitly that admitting uncertainty is acceptable. Without that permission, a model under pressure to answer is more likely to fill the gap with something invented.</p>
<p><strong>Restrict to provided sources.</strong> For document work, instruct Claude to answer only from the materials you supplied and to flag anything those materials do not cover. This converts open-ended generation into bounded retrieval.</p>
<p><strong>Require auditable citations.</strong> Ask for the specific source and location behind each claim, in a form you can check. A citation you cannot trace is not a citation.</p>
</div>

<div class="jb-tab-panel" id="content2">
<p><strong>Quote first, then analyze.</strong> For long documents, ask Claude to extract the supporting quotes before drawing conclusions. Grounding the analysis in pulled quotes makes both the reasoning and the errors visible.</p>
<p><strong>Best-of-N comparison.</strong> Re-run the same request and compare. Where the runs agree, confidence rises; where they diverge, you have found the soft spots that need a human look.</p>
<p><strong>Validate against authoritative sources.</strong> For claims that matter, check against a trusted external reference rather than a second Claude response. In-product aids help here: Claude for Excel can produce cell-level citations that tie figures back to their inputs.</p>
</div>

<div class="jb-tab-panel" id="content3">
<p style="font-size: 1.15rem; font-weight: 600; color: #dfe1e5; margin-bottom: 4px;">The techniques as verbatim prompts</p>
<p style="margin-bottom: 16px;">Each technique is a phrase you can paste. The wording is the skill.</p>

<div class="jb-tab-subhead">Permission to not know</div>
<p>"If the answer is not supported by the documents I provided, say so explicitly rather than estimating. It is acceptable to answer 'the provided materials do not cover this.'"</p>

<div class="jb-tab-subhead">Source restriction</div>
<p>"Answer using only the attached contract. Do not use general knowledge. For anything the contract does not address, list it under 'Not covered by this document.'"</p>

<div class="jb-tab-subhead">Auditable citation</div>
<p>"For every claim, cite the section and clause number it comes from, in parentheses, so I can verify it against the source."</p>

<div class="jb-tab-subhead">Quote-grounding</div>
<p>"Before you analyze, extract the exact sentences from the document that bear on my question. Then base your analysis only on those quotes."</p>
</div>
</div>
</div>

> [!TIP]
> <small>THE VERIFICATION CHECKLIST</small>
>
> Before relying on an output: did I allow uncertainty, restrict to sources where appropriate, require citations I can audit, and check the high-stakes claims against something authoritative? Building these into the prompt is cheaper than rebuilding trust in the output afterward.

## Diligence: When Human Review Is Non-Negotiable

<span style="font-size: 1.25em;">_Some outputs must never go out as a Claude draft alone, no matter how good they look._</span>

Diligence means knowing those thresholds in advance, so the decision to escalate is made by policy, not in the moment after something has already gone wrong.

### Four risk thresholds

| Threshold | What to ask |
| :-- | :-- |
| Stakes | **What is the cost if this is wrong?**<br/> High-cost errors demand human review regardless of how confident the output appears. |
| Reversibility | **Can the action be undone?**<br/> An irreversible step (a sent client deliverable, a filed report) clears a higher bar than a draft you can revise. |
| Audience | **Who sees it?**<br/> External, executive, and regulatory audiences raise the review requirement above internal working drafts. |
| Regulatory exposure | **Does a rule, contract, or law govern this?**<br/> Regulated content carries obligations that AI assistance does not remove. |

### The do-not-ship-without-review list

Decide these in advance and treat them as fixed:

* Final client deliverables
* Audit-critical or financially material calculations
* Anything involving regulated, confidential, or highly sensitive data
* Public or legal communications where a misstatement carries lasting consequence

### Iteration versus escalation

Productive iteration improves the output each round. When rounds stop improving it, you have diminishing returns, and the right move is not another prompt; it is a human expert. Recognizing that line is part of Diligence: more prompting cannot manufacture judgment the situation requires.

> [!Tip]
> <small>OWNING THE OUTPUT</small>
>
> The accountability does not transfer to the tool. Work produced with Claude is your work when you ship it, and the professional standard is the same as if you had produced it unaided. Diligence is the habit of acting as though that is true, because it is.

### Three escalation scenarios

**The fast "yes."** Claude drafts an internal meeting agenda. Low stakes, reversible, internal audience, no regulatory exposure. All four thresholds say ship. No escalation; this is the routine case you can move quickly on.

**The deceptive "looks fine."** Claude produces a board-deck financial summary that reads cleanly. The stakes are high, there's an executive audience, and the result will be partly irreversible once presented, tripping three of the risk thresholds. The clean appearance is irrelevant; this goes to a human reviewer and the figures get recomputed with code execution.

**The slow creep.** You have iterated a client proposal five times. Rounds three through five changed almost nothing. Diminishing returns plus a high-stakes external deliverable: stop prompting, escalate to a colleague for a fresh read. The signal to escalate is the flat improvement curve, not a visible error.

## Editing and Adapting Output for Your Audience

<span style="font-size: 1.25em;">_Claude drafts; you deliver. The gap between a raw draft and a finished deliverable is the editing pass, and that pass is where your professional standards and your knowledge of the audience get applied. A draft that is accurate is still not finished._</span>

### From raw output to deliverable

Three passes turn a draft into something you would put your name on:

**Clarity.** Cut hedging, tighten loose sentences, remove anything that does not earn its place. Claude tends toward thoroughness; editing tends toward precision.

**Tone.** Match the register to the relationship and the occasion. The same content reads differently to a peer, a client, and a regulator.

**Formatting.** Shape the output for how it will be read: scannable for an executive, detailed for a working team, clean for an external recipient.

### Audience calibration

One analysis often needs to become several deliverables. An executive summary leads with the decision and the impact. A working-team version keeps the detail and the method. An external communication controls what is disclosed and how it is framed. The underlying facts hold steady; the selection, depth, and tone change with who is reading.

Comparing outputs before you edit
When quality matters, generate more than one draft (across runs or across models) and choose the strongest base to edit from, rather than committing to the first response. Comparing candidates is cheaper than rescuing a weak draft, and it invites framing you might not have prompted for.

One analysis, two audiences: a transformation
Raw output (excerpt)
"The analysis indicates that processing time increased by approximately 18 percent in Q3, which may be attributable to a combination of higher volume and the onboarding of three new staff members who were still onboarding during the period, and it is recommended that the team consider whether additional process documentation might help mitigate similar effects in future onboarding cycles."

Executive version
"Q3 processing time rose 18 percent, driven by volume plus onboarding three new hires. Recommend standardized onboarding docs to limit the effect next time." Leads with the number and the decision; one sentence.

Working-team version
"Processing time was up ~18% in Q3. Two drivers: higher volume and three new staff still onboarding. Action: draft onboarding documentation so the next cohort ramps faster (owner and timeline to confirm in standup)." Keeps the method and adds the operational next step.

Same facts, same 18 percent. The executive cut strips method and leads with impact; the working cut keeps detail and assigns action. Neither is a raw draft, which would not serve either audience.