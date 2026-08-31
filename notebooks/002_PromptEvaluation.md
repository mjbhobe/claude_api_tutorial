# Prompt Evaluation

When working with Claude, writing a good prompt is just the beginning. To build reliable AI applications, you need to understand two critical concepts: prompt engineering and prompt evaluation. Prompt engineering gives you techniques for writing better prompts, while prompt evaluation helps you measure how well those prompts actually work.

<p align="center">
  <img src="images/improving_and_evaluating_prompts.png" alt="Improving &amp; Evaluating Prompts" width="450" height="250">
</p>

## Prompt Engineering vs Prompt Evaluation

Prompt _engineering_ is your toolkit for _crafting effective prompts_. It includes techniques like:

* Multi-shot prompting
* Structuring with XML tags
* Many other best practices

These techniques help Claude understand exactly what you're asking for and how you want it to respond.

Prompt _evaluation_ takes a different approach. Instead of focusing on how to write prompts, it's about _measuring their effectiveness_ through automated testing. You can:

* Test against expected answers
* Compare different versions of the same prompt
* Review outputs for errors

## Three Paths After Writing a Prompt

Once you've drafted a prompt, you typically face three options for what to do next:

<p align="center">
  <img src="images/three_paths_after_prompt.png" alt="Three Paths after writing Prompts" width="450" height="250">
</p>

* **Option 1:** Test the prompt once and decide if it's good enough. This carries a significant risk of breaking in production when users provide unexpected inputs.

* **Option 2:** Test the prompt a few times and tweak it to handle an _edge case_ or two. While better than option 1, users will often provide very unexpected outputs that you haven't considered.

* **Option 3:** Run the prompt through an evaluation pipeline to score it, then iterate on the prompt based on objective metrics. This approach requires more work and cost, but gives you much more confidence in your prompt's reliability.

## Why Most Engineers Fall Into Testing Traps

Options 1 and 2 are common traps that all engineers fall into, myself included. It's natural to write a prompt for a serious application and not test it thoroughly enough. _We tend to underestimate how many edge cases real users will encounter_.

The reality is that when you deploy a prompt to production, users will interact with it in ways you never anticipated. What seemed like a solid prompt during your limited testing can quickly break down when faced with the full variety of real-world inputs.

The _Evaluation-First Approach_
Option 3 represents a more systematic approach to prompt development. By running your prompt through an evaluation pipeline, you get objective metrics about its performance across a broader range of test cases. This data-driven approach lets you:

* Identify weaknesses before they become production issues
* Compare different prompt versions objectively
* Iterate with confidence based on measurable improvements
* Build more reliable AI applications

While this approach requires more upfront investment in time and testing infrastructure, it pays dividends in the reliability and robustness of your final application. The goal is to catch problems during development rather than after your users encounter them.

## A Typical Evaluation Workflow

A typical _prompt evaluation workflow follows **five key steps**_ that help you systematically improve your prompts through objective measurement. While there are many different ways to assemble these workflows and various open source and paid tools available, understanding the core process helps you start small and scale up as needed.

<p align="center">
  <img src="images/prompt_eval_workflow.png" alt="Prompt Eval Workflow" width="450" height="250">
</p>

### Step 1: Draft a Prompt

Start by writing an initial prompt that you want to improve. For this example, we'll use a simple prompt:

```python
prompt = f"""
Please answer the user's question:

{question}
"""
```

<p align="center">
  <img src="images/initial_prompt_draft.png" alt="Initial Prompt Draft" width="450" height="150">
</p>

This basic prompt will serve as our baseline for testing and improvement.

### Step 2: Create an Eval Dataset

Your evaluation dataset contains sample inputs that represent the types of questions or requests your prompt will handle in production. The dataset should include questions that will be interpolated into your prompt template.

<p align="center">
  <img src="images/eval_dataset.png" alt="Create Eval Dataset" width="450" height="250">
</p>

For this example, our dataset includes three questions:

* `"What's 2+2?"`
* `"How do I make oatmeal?"`
* `"How far away is the Moon?"`

In real-world evaluations, you might have tens, hundreds, or even thousands of records. You can assemble these datasets by hand or use Claude to generate them for you.

### Step 3: Feed Through Claude

Take each question from your dataset and merge it with your prompt template to create complete prompts. Then send each one to Claude to get responses.

<p align="center">
  <img src="images/feed_through_claude.png" alt="Feed Through Claude" width="450" height="250">
</p>

For example, the first question becomes:

```
Please answer the user's question:
What's 2+2?
```

Claude might respond with `"2 + 2 = 4"` for the math question, provide oatmeal cooking instructions for the second question, and give the distance to the Moon for the third.

### Step 4: Feed Through a Grader

The grader evaluates the quality of Claude's responses by examining both the original question and Claude's answer. This step provides objective scoring, typically on a scale from 1 to 10, where 10 represents a perfect answer and lower scores indicate room for improvement.

<p align="center">
  <img src="images/feed_through_grader.png" alt="Feed Through Grader" width="450" height="250">
</p>

In our example, the grader might assign:

* Math question: `10` (perfect answer)
* Oatmeal question: `4` (needs improvement)
* Moon question: `9` (very good answer)

The average score across all questions gives you an objective measurement: 

$$\frac{10 + 4 + 9}{3} \approx 7.67$$

Step 5: Change Prompt and Repeat
Now that you have a baseline score, you can modify your prompt and run the entire process again to see if your changes improve performance.

<p align="center">
  <img src="images/change_prompt_and_repeat.png" alt="Change Prompt And Repeat" width="450" height="250">
</p>

For example, you might add more guidance to your prompt:

```python
prompt = f"""
Please answer the user's question:

{question}

Answer the question with ample detail
"""
```

After running this improved prompt through the same evaluation process, you might get a higher average score of `8.7`, indicating that the additional instruction helped Claude provide better responses.

### Prompt Scoring

The key benefit of this workflow is getting objective measurements of prompt performance. You can:

* Compare different prompt versions numerically
* Use the version with the best score
* Continue iterating to find even better approaches

<p align="center">
  <img src="images/prompt_scoring.png" alt="Change Prompt And Repeat" width="450" height="250">
</p>

This systematic approach removes guesswork from prompt engineering and gives you confidence that your changes are actually improvements rather than just different variations.

## Generating Test Datasets

Building a custom prompt evaluation workflow starts with creating a solid prompt and then generating test data to see how well it performs. Let's walk through setting up an evaluation system for a prompt that helps users write AWS-specific code.

### Setting Up the Goal

Our prompt needs to assist users in writing three specific types of output for AWS use cases:

* Python code
* JSON configuration files
* Regular expressions

The key requirement is that when a user requests help with a task, we return clean output in one of these formats without any extra explanations, headers, or footers.

<p align="center">
  <img src="images/generate_dataset_goal.png" alt="Generate Dataset Goal" width="450" height="250">
</p>

Here's our starting prompt (version 1):

```python
prompt = f"""
Please provide a solution to the following task:
{task}
"""
```

### Creating an Evaluation Dataset

An evaluation dataset contains inputs that we'll feed into our prompt. For each combination of prompt and input, we'll run the prompt and analyze the results.

Our dataset will be an array of JSON objects, where each object contains a "task" property describing what we want Claude to accomplish. We can either create this dataset by hand or generate it automatically using Claude.