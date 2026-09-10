# Prompt Engineering

Prompt engineering is about taking a prompt you've written and improving it to get more reliable, higher-quality outputs. This process involves iterative refinement - starting with a basic prompt, evaluating its performance, then systematically applying engineering techniques to improve it.

<p align="center">
  <img src="images/prompt_engineering.png" alt="Prompt Engineering" width="450" height="250">
</p>

## The Iterative Improvement Process

The approach follows a clear cycle that you can repeat until you achieve your desired results:

1. `Set a goal` - Define what you want your prompt to accomplish
2. `Write an initial prompt` - Create a basic first attempt
3. `Evaluate the prompt` - Test it against your criteria
4. `Apply prompt engineering techniques` - Use specific methods to improve performance
5. `Re-evaluate` - Verify that your changes actually improved the results

You repeat the last two steps until you're satisfied with the performance. Each iteration should show measurable improvement in your evaluation scores.

## Setting Up Your Evaluation Pipeline

To demonstrate this process, we'll work with a practical example: `creating a prompt that generates one-day meal plans for athletes`. The prompt needs to take into account an athlete's height, weight, goals, and dietary restrictions, then produce a comprehensive meal plan.

<p align="center">
  <img src="images/pe_evaluation_pipeline.png" alt="Prompt Eveluation Pipeline" width="450" height="250">
</p>

The evaluation setup uses a `PromptEvaluator` class that handles dataset generation and model grading. When creating your evaluator instance, you can control concurrency with the `max_concurrent_tasks` parameter:

```python
evaluator = PromptEvaluator(max_concurrent_tasks=5)
```

Start with a low concurrency value (like 3) to avoid rate limit errors. You can increase it if your API quota allows for faster processing.

### Generating Test Data

The evaluation system can automatically generate test cases based on your prompt requirements. You define what inputs your prompt needs:

```python
dataset = evaluator.generate_dataset(
    task_description="Write a compact, concise 1 day meal plan for a single athlete",
    prompt_inputs_spec={
        "height": "Athlete's height in cm",
        "weight": "Athlete's weight in kg", 
        "goal": "Goal of the athlete",
        "restrictions": "Dietary restrictions of the athlete"
    },
    output_file="dataset.json",
    num_cases=3
)
```

Keep the number of test cases low (2-3) during development to speed up your iteration cycle. You can increase this for final validation.

### Writing Your Initial Prompt

Start with a simple, naive prompt to establish a baseline. Here's an example of a _deliberately basic_ first attempt:

```python
def run_prompt(prompt_inputs):
    prompt = f"""
        What should this person eat?

        - Height: {prompt_inputs["height"]}
        - Weight: {prompt_inputs["weight"]}
        - Goal: {prompt_inputs["goal"]}
        - Dietary restrictions: {prompt_inputs["restrictions"]}
        """
    
    messages = []
    add_user_message(messages, prompt)
    return chat(messages)
```

This basic prompt will likely produce poor results, but it gives you a starting point to measure improvement against.

### Adding Evaluation Criteria

When running your evaluation, you can specify additional criteria that the grading model should consider:

```python
results = evaluator.run_evaluation(
    run_prompt_function=run_prompt,
    dataset_file="dataset.json",
    extra_criteria="""
        The output should include:
        - Daily caloric total
        - Macronutrient breakdown  
        - Meals with exact foods, portions, and timing
        """
)
```

This helps ensure your prompt is evaluated against the specific requirements that matter for your use case.

### Analyzing Results

After running an evaluation, you'll get both a numerical score and a detailed HTML report. The report shows you exactly how each test case performed, including the model's reasoning for each score.

<p align="center">
  <img src="images/prompt_engineering_report.png" alt="Prompt Engineering Report" width="450" height="250">
</p>

Don't be discouraged by low initial scores - a score of 2.3 out of 10 is typical for a first attempt. The goal is to see consistent improvement as you apply engineering techniques.

The detailed evaluation report helps you understand exactly where your prompt is failing and what improvements are needed. Use this feedback to guide your next iteration.

## Being Clear and Direct

The first line of your prompt is the most important part of your entire request. This is where you set the stage for everything that follows, and getting it right can dramatically improve your results.

### Being Clear and Direct

When crafting that crucial first line, you want to focus on two key principles: clarity and directness. This means using simple language that leaves no room for ambiguity about what you want Claude to do.

<p align="center">
  <img src="images/pe_be_clear_and_direct.png" alt="Prompt Engineering - Be Clear &amp; Direct" width="450" height="250">
</p>

### Clear Communication

Being "clear" means:

* Use simple language that anyone can understand
* State exactly what you want without beating around the bush
* Lead with a straightforward statement of Claude's task

Instead of writing something vague like _"I need to know about those things people put on their roofs that use sun - those solar panel things, I think they're called,"_ be direct and write: _"Write three paragraphs about how solar panels work."_

### Direct Instructions

Being "direct" focuses on how you structure your request:

* Use instructions, not questions
* Start with direct action verbs like "Write," "Create," or "Generate"

Rather than asking _"I was reading about renewable energy and geothermal energy sounds neat. What countries use it?"_ try: _"Identify three countries that use geothermal energy. Include generation stats for each."_

### Putting It Into Practice

Let's see this technique in action. Starting with a weak prompt that simply asked `"What should this person eat?"` we can apply our clear and direct approach.

The improved version becomes: `"Generate a one-day meal plan for an athlete that meets their dietary restrictions."`

This revision immediately tells Claude:

* What action to take (generate)
* What to create (a meal plan)
* Key constraints (one day, for an athlete, meeting dietary restrictions)

### Results Matter

This simple change can have a significant impact on performance. In our example, the evaluation score jumped from `2.32` to `3.92` - a substantial improvement from just restructuring that opening line.

The key takeaway is that Claude responds best when you treat it like a capable assistant who needs clear direction rather than someone who has to guess what you want. Start strong with a direct action verb, be specific about the task, and you'll see better results right away.## 

## Being Specific

When working with Claude, one of the most effective ways to improve your results is to be specific about what you want. Instead of leaving everything up to the model's interpretation, you can provide clear guidelines or steps that direct Claude toward the kind of output you're looking for.

Think about it this way: if you ask Claude to "write a short story about a character who discovers a hidden talent," Claude could go in countless directions. The story might be 200 words or 2,000 words. It might have one character or five. It could focus on any type of talent discovery scenario.

<p align="center">
  <img src="images/pe_being_specific.png" alt="Prompt Engineering - Being Specific" width="450" height="250">
</p>

By adding specific guidelines, you give Claude a clearer target to aim for. This dramatically improves both the consistency and quality of the output.

### Two Types of Guidelines

There are two main approaches to being specific in your prompts, and you'll often see them used together in professional applications.

<p align="center">
  <img src="images/pe_guideline_types.png" alt="Prompt Engineering - Types of Guidelines" width="450" height="250">
</p>

#### Output Quality Guidelines

The first type focuses on listing qualities that your output should have. These guidelines help you control:

* Length of the response
* Structure and format
* Specific attributes or elements to include
* Tone or style requirements

For example, you might specify that a story should be under 1,000 words, include a clear action that reveals the character's talent, and feature at least one supporting character.

#### Process Steps

The second type provides specific steps for Claude to follow. This approach is particularly useful when you want Claude to think through a problem systematically or consider multiple perspectives before arriving at a final answer.

Instead of jumping straight to writing, you might ask Claude to:

1. Brainstorm three talents that would create dramatic tension
2. Pick the most interesting talent
3. Outline a pivotal scene that reveals the talent
4. Brainstorm supporting character types that could increase the impact

### Real-World Impact

The difference that specificity makes is dramatic. In testing a meal planning prompt, adding guidelines improved the evaluation score from 3.92 to 7.86 - more than doubling the quality of the output simply by telling Claude exactly what elements to include.

```
Guidelines:
1. Include accurate daily calorie amount
2. Show protein, fat, and carb amounts  
3. Specify when to eat each meal
4. Use only foods that fit restrictions
5. List all portion sizes in grams
6. Keep budget-friendly if mentioned
```

### When to Use Each Approach

Here's a practical guide for when to use each type of specificity:

#### Always Use Output Guidelines

You should include quality guidelines in almost every prompt you write. They're your safety net for getting consistent, useful results.

#### Use Process Steps For Complex Problems

Add step-by-step instructions when you're dealing with:

* Troubleshooting complex problems
* Decision-making scenarios
* Critical thinking tasks
* Any situation where you want Claude to consider multiple angles

<p align="center">
  <img src="images/pe_when_to_use_steps.png" alt="Prompt Engineering - When to use steps" width="450" height="250">
</p>

For instance, if you're asking Claude to analyze why a sales team's performance dropped, you'd want to guide it through examining market metrics, industry changes, individual performance, organizational changes, and customer feedback - rather than letting it focus on just one potential cause.

### Combining Both Approaches

In professional prompting, you'll often see both techniques used together. You might have guidelines that control the format and content of your output, plus steps that ensure Claude thinks through the problem thoroughly before responding.

This combination gives you both consistency in your results and confidence that Claude has considered all the important factors in reaching its conclusion.

## Structure with XML Tags


