# Prompt Engineering

**See notebook**: [Prompt Engineering](../notebooks/002_PromptEngineering.ipynb)

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
def run_prompt(prompt_inputs, prompt):
    rendered_prompt = evaluator.render(prompt, prompt_inputs)

    messages = []
    add_user_message(messages, rendered_prompt)
    return chat(client, model, messages)
```

```python
    naive_prompt = f"""
        What should this person eat?

        - Height: {prompt_inputs["height"]}
        - Weight: {prompt_inputs["weight"]}
        - Goal: {prompt_inputs["goal"]}
        - Dietary restrictions: {prompt_inputs["restrictions"]}
        """
```

This basic prompt will likely produce poor results, but it gives you a starting point to measure improvement against.

### Adding Evaluation Criteria

When running your evaluation, you can specify additional criteria that the grading model should consider:

```python
results = evaluator.run_evaluation(
    run_prompt_function=run_prompt,
    dataset_file="dataset.json",
    prompt=naive_prompt,
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

For the `evaluator.run_evaluation(...)` call, I could see results like this for example:

```
Graded 1/3 test cases
Graded 2/3 test cases
Graded 3/3 test cases
Average score: 2.6666666666666665
```

Don't be discouraged by low initial scores - a score of `2.6` out of 10 is typical for a first attempt. The goal is to see consistent improvement as you apply engineering techniques.

The detailed evaluation report helps you understand exactly where your prompt is failing and what improvements are needed. Use this feedback to guide your next iteration.

## Prompt Improvement Techniques

In this section we'll review techniques of improving a naive prompt. We'll see techniques such as:

* Being Clear and Direct
* Being Specific
* Structure with XML tags
* Providing Examples

### 1. Being Clear and Direct

The first line of your prompt is the most important part of your entire request. This is where you set the stage for everything that follows, and getting it right can dramatically improve your results.

When crafting that crucial first line, you want to focus on two key principles: clarity and directness. This means using simple language that leaves no room for ambiguity about what you want Claude to do.

#### Clear Communication

Being "clear" means:

* Use simple language that anyone can understand
* State exactly what you want without beating around the bush
* Lead with a straightforward statement of Claude's task

Instead of writing something vague like _"I need to know about those things people put on their roofs that use sun - those solar panel things, I think they're called,"_ 

Be direct and write: _"Write three paragraphs about how solar panels work."_

#### Direct Instructions

Being "direct" focuses on how you structure your request:

* Use instructions, not questions
* Start with direct action verbs like "Write," "Create," or "Generate"

Rather than asking _"I was reading about renewable energy and geothermal energy sounds neat. What countries use it?"_ 

Try: _"Identify three countries that use geothermal energy. Include generation stats for each."_

#### Putting It Into Practice

Let's see this technique in action. Starting with a weak prompt that simply asked `"What should this person eat?"` we can apply our clear and direct approach.

The improved version becomes: `"Generate a one-day meal plan for an athlete that meets their dietary restrictions."`

This revision immediately tells Claude:

* What action to take (generate)
* What to create (a meal plan)
* Key constraints (one day, for an athlete, meeting dietary restrictions)

```python
clear_and_direct_prompt = """
  Generate a one-day meal plan for an athlete that 
  meets their dietary restrictions.

  - Height: {height}
  - Weight: {weight}
  - Goal: {goal}
  - Dietary restrictions: {restrictions}
"""

results = evaluator.run_evaluation(
    run_prompt_function=run_prompt,
    dataset_file="dataset.json",
    prompt=clear_and_direct_prompt,
    extra_criteria="""
        The output should include:
        - Daily caloric total
        - Macronutrient breakdown  
        - Meals with exact foods, portions, and timing
        """
)
```

Running the above code, improves the results - for example, I saw something like this:

```
Graded 1/3 test cases
Graded 2/3 test cases
Graded 3/3 test cases
Average score: 5.666666666666667
```

#### Results Matter

This simple change can have a significant impact on performance. In our example, the evaluation score jumped from `2.67` to `5.67` - a substantial improvement from just restructuring that opening line.

The key takeaway is that **Claude responds best when you treat it like a capable assistant who needs clear direction rather than someone who has to guess what you want**. Start strong with a direct action verb, be specific about the task, and you'll see better results right away.## 

### 2. Being Specific

When working with Claude, one of the most effective ways to improve your results is to be specific about what you want. Instead of leaving everything up to the model's interpretation, you can provide clear guidelines or steps that direct Claude toward the kind of output you're looking for.

Think about it this way: if you ask Claude to "write a short story about a character who discovers a hidden talent," Claude could go in countless directions. The story might be 200 words or 2,000 words. It might have one character or five. It could focus on any type of talent discovery scenario.

<p align="center">
  <img src="images/pe_being_specific.png" alt="Prompt Engineering - Being Specific" width="450" height="250">
</p>

By adding specific guidelines, you give Claude a clearer target to aim for. This dramatically improves both the consistency and quality of the output.

#### Two Types of Guidelines

There are two main approaches to being specific in your prompts, and you'll often see them used together in professional applications.

<p align="center">
  <img src="images/pe_guideline_types.png" alt="Prompt Engineering - Types of Guidelines" width="450" height="250">
</p>

**Output Quality Guidelines**

The first type focuses on **listing qualities that your output should have**. These guidelines help you control:

* Length of the response
* Structure and format
* Specific attributes or elements to include
* Tone or style requirements

For example, you might specify that a story should be under 1,000 words, include a clear action that reveals the character's talent, and feature at least one supporting character.

**Process Steps**

The second type **provides specific steps for Claude to follow**. This approach is particularly useful when you want Claude to think through a problem systematically or consider multiple perspectives before arriving at a final answer.

Instead of jumping straight to writing, you might ask Claude to:

1. Brainstorm three talents that would create dramatic tension
2. Pick the most interesting talent
3. Outline a pivotal scene that reveals the talent
4. Brainstorm supporting character types that could increase the impact

#### Real-World Impact

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

#### When to Use Each Approach

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

#### Combining Both Approaches

In professional prompting, you'll often see both techniques used together. You might have guidelines that control the format and content of your output, plus steps that ensure Claude thinks through the problem thoroughly before responding.

This combination gives you both consistency in your results and confidence that Claude has considered all the important factors in reaching its conclusion.

```python
clear_direct_and_specific_prompt = """
Generate a one-day meal plan for an athlete that 
meets their dietary restrictions.

- Height: {height}
- Weight: {weight}
- Goal: {goal}
- Dietary restrictions: {restrictions}

Guidelines:
1. Include accurate daily calorie amount
2. Show protein, fat, and carb amounts
3. Specify when to eat each meal
4. Use only foods that fit restrictions
5. List all portion sizes in grams
6. Keep budget-friendly if mentioned
"""

results = evaluator.run_evaluation(
    run_prompt_function=run_prompt,
    dataset_file="dataset.json",
    prompt=clear_direct_and_specific_prompt,
    extra_criteria="""
        The output should include:
        - Daily caloric total
        - Macronutrient breakdown  
        - Meals with exact foods, portions, and timing
        """
)
```

Running the above code I saw something like this - a slightly better score:

```
Graded 1/3 test cases
Graded 2/3 test cases
Graded 3/3 test cases
Average score: 6.333333333333333
```

### 3. Structure with XML Tags

When you're building prompts that include a lot of content, Claude can sometimes struggle to understand which pieces of text belong together or what different sections are supposed to represent. XML tags provide a simple way to add structure and clarity to your prompts, especially when you're interpolating large amounts of data.

#### Why Structure Matters

Consider a prompt where you need to analyze 20 pages of sales records. Without clear boundaries, Claude might have trouble distinguishing between your instructions and the actual data you want analyzed.

```
Write a 1 page decision report to troubleshoot why a Sales team's numbers have dropped 30% last quarter.

Here are the last 20 pages of our sales records:
{sales_records}

Follow these steps:
1. Compare current vs previous market metrics
2. Identify relevant industry changes
3. Analyze individual team member performance
4. Consider recent organizational changes
5. Review customer feedback
```

The example above shows how unclear boundaries can make it difficult for Claude to parse your intent. By wrapping the sales records in XML tags like `<sales_records>` and `</sales_records>`, you create clear delimiters that help Claude understand the structure of your prompt.

```
Write a 1 page decision report to troubleshoot why a Sales team's numbers have dropped 30% last quarter.

Here are the last 20 pages of our sales records:
<sales_records>
{sales_records}
</sales_records>

Follow these steps:
1. Compare current vs previous market metrics
2. Identify relevant industry changes
3. Analyze individual team member performance
4. Consider recent organizational changes
5. Review customer feedback
```

#### Practical Example: Code and Documentation

Here's a more dramatic example of why XML tags matter. If you ask Claude to debug code using provided documentation, mixing everything together creates confusion:

<table cellspacing="0" cellpadding="0">
<tr style="vertical-align: top;">
  <th>Not Great</th>
  <th>Better!</th>
</tr>
<tr style="vertical-align: top;">
  <td>
    Debug my code below using the provided documentation:

    from datavortex import Pipeline, DataSource

    def process_data(input_file, output_file):
      pipeline = Pipeline()
      source = Datasource.from_csv(input_file)

    \# creating a data source from data vortex
    csv_source = DataSource.from_csv("data.csv")
  </td>
  <td>
    Debug my code below using the provided documentation:
  
    <my_code>
    from datavortex import Pipeline, DataSource

    def process_data(input_file, output_file):
      pipeline = Pipeline()
      source = Datasource.from_csv(input_file)
    </my_code>

    <docs>
    \# creating a data source from data vortex
    csv_source = DataSource.from_csv("data.csv")
    </docs>
  <td>
  </td>
</tr>
</table>

The **"Not Great"** version makes it nearly impossible to tell what's code versus documentation. The **"Better!"** version uses `<my_code>` and `<docs>` tags to create clear boundaries.

#### Custom Tag Names

**You don't need to use official XML tags**. Create descriptive names that make sense for your content:

* `<sales_records>` is better than `<data>`
* `<athlete_information>` clearly identifies user details
* `<my_code>` and `<docs>` separate different types of content

The more specific and descriptive your tag names, the better Claude can understand the purpose of each section.

#### When to Use XML Tags

XML tags are most useful when:

* Including large amounts of context or data
* Mixing different types of content (code, documentation, data)
* You want to be extra clear about content boundaries
* Working with complex prompts that interpolate multiple variables

Even for shorter content, XML tags can help serve as delimiters that make your prompt structure more obvious to Claude.

#### Real-World Application

In practice, you might structure a prompt like this:

```
<athlete_information>
- Height: 6'2"
- Weight: 180 lbs
- Goal: Build muscle
- Dietary restrictions: Vegetarian
</athlete_information>

Generate a meal plan based on the athlete information above.
```

This makes it crystal clear that the `height`, `weight`, `goal`, and `dietary restrictions` are all related athlete data that should be considered together when generating the meal plan.

While you might not see dramatic improvements with simple prompts, XML tags become increasingly valuable as your prompts grow more complex and include larger amounts of varied content.


```python
clear_direct_specific_with_xml = """
  Generate a one-day meal plan for an athlete that 
  meets their dietary restrictions.

  <athlete_information> 
  - Height: {height} 
  - Weight: {weight} 
  - Goal: {goal} 
  - Dietary restrictions: {restrictions} 
  </athlete_information>

  Guidelines:
  1. Include accurate daily calorie amount
  2. Show protein, fat, and carb amounts
  3. Specify when to eat each meal
  4. Use only foods that fit restrictions
  5. List all portion sizes in grams
  6. Keep budget-friendly if mentioned
"""

results = evaluator.run_evaluation(
    run_prompt_function=run_prompt,
    dataset_file="dataset.json",
    prompt=clear_direct_specific_with_xml,
    extra_criteria="""
        The output should include:
        - Daily caloric total
        - Macronutrient breakdown  
        - Meals with exact foods, portions, and timing
        """
)
```

Running the above code I saw something like this. As expected, I didn't see any dramatic improvement for this simple prompt:

```
Graded 1/3 test cases
Graded 2/3 test cases
Graded 3/3 test cases
Average score: 6.333333333333333
```

### 4. Providing Examples

**Providing examples in your prompts is one of the most effective prompt engineering techniques you'll use**. This approach, known as "one-shot" or "multi-shot" prompting, involves giving Claude sample input/output pairs to guide its responses.

#### How Examples Work

Let's look at a sentiment analysis example. Say you want Claude to categorize whether a tweet is positive or negative:

```
Categorize the sentiment of the below tweet:

<input_tweet>
Yeah, sure that was the best movie I hae seen since 'Plan 9 from outer space'
</input_tweet>

If the tweet has has positive sentiment, respond with 'Positive'. If it is negative, respond with 'Negative'.
```

The challenge here is sarcasm. A tweet like `"Yeah, sure, that was the best movie I've seen since 'Plan 9 from Outer Space'"` appears positive on the surface, but it's actually sarcastic and negative (Plan 9 is famously one of the worst movies ever made).

#### Adding Examples to Handle Corner Cases

To solve this, you can add examples that show Claude how to handle tricky cases:

```
Categorize the sentiment of the below tweet:

<input_tweet>
Yeah, sure that was the best movie I hae seen since 'Plan 9 from outer space'
</input_tweet>

If the tweet has has positive sentiment, respond with 'Positive'. If it is negative, respond with 'Negative'.

Here is a example input with ideal response:
<sample_input>
Great game tonight.
</sample_input>
<ideal_output>
Positive
</ideal_output>

Be especially careful with tweets that contain sarcasm.
For example:
<sample_input>
Oh yeah, I really need a flight delay tonight! Excellent!
</sample_input>
<ideal_output>
Negative
</ideal_output>
```

The improved prompt includes:

* A clear positive example: `"Great game tonight!"` → `"Positive"`
* A sarcastic example: `"Oh yeah, I really needed a flight delay tonight! Excellent!"` → `"Negative"`

Context explaining why sarcasm should be treated carefully
Notice how the examples are wrapped in XML tags like `<sample_input>` and `<ideal_output>`. This structure makes it crystal clear to Claude what each part represents.

#### When to Use Examples

Examples are particularly useful for:

* Capturing corner cases or edge scenarios
* Defining complex output formats (like specific JSON structures)
* Showing the exact style or tone you want
* Demonstrating how to handle ambiguous inputs

#### One-Shot vs Multi-Shot

* `One-Shot`: Provide a single example to establish the pattern
* `Multi-Shot`: Provide multiple examples to cover different scenarios

Use `multi-shot` when you need to handle various edge cases or want to show different types of valid responses.

#### Finding Good Examples from Evaluations

When running prompt evaluations, look for your highest-scoring outputs to use as examples:

![Finding Good Examples](images/finding_good_examples.png)

Find responses that scored 10 (or your highest available score) and use those input/output pairs as examples in your prompt. This helps Claude understand what "perfect" output looks like for your specific use case.

#### Adding Context to Examples

Don't just provide the input/output pair - explain why the output is good:

```
<ideal_output>
[Your example output here]
</ideal_output>

This example is well-structured, provides detailed information on food choices and quantities, and aligns with the athlete's goals and restrictions.
```

This additional context helps Claude understand the reasoning behind good responses, not just the format.

#### Best Practices

* Always use XML tags to structure your examples clearly
* Be explicit about what you're showing: "Here is an example input with an ideal response"
* Include examples that address your most common failure cases
* Explain why your example outputs are considered ideal
* Keep examples relevant to your specific task

Examples are especially powerful because they show rather than tell. Instead of trying to describe exactly what you want in words, you demonstrate it directly. This makes your prompts much more reliable and helps Claude understand subtle requirements that might be hard to express in instructions alone.

Here is a prompt that includes all the best practices listed above:

```python

clear_direct_specific_with_xml_and_examples = """
Generate a one-day meal plan for an athlete that meets their dietary restrictions.

<athlete_information> 
- Height: {height} 
- Weight: {weight} 
- Goal: {goal} 
- Dietary restrictions: {restrictions} 
</athlete_information>

Guidelines:
1. Include accurate daily calorie amount
2. Show protein, fat, and carb amounts
3. Specify when to eat each meal
4. Use only foods that fit restrictions
5. List all portion sizes in grams
6. Keep budget-friendly if mentioned

Here is an example with a sample input and an ideal output:
<sample_input>
height: 170
weight: 70
goal: Maintain fitness and improve cholesterol levels
restrictions: High cholesterol
</sample_input>
<ideal_output>
Here is a one-day meal plan for an athlete aiming to maintain fitness and improve cholesterol levels:

*   **Calorie Target:** Approximately 2500 calories
*   **Macronutrient Breakdown:** Protein (140g), Fat (70g), Carbs (340g)

**Meal Plan:**

*   **Breakfast (7:00 AM):** Oatmeal (80g dry weight) with berries (100g) and walnuts (15g). Skim milk (240g).
    *   Protein: 15g, Fat: 15g, Carbs: 60g
*   **Mid-Morning Snack (10:00 AM):** Apple (150g) with almond butter (30g).
    *   Protein: 7g, Fat: 18g, Carbs: 25g
*   **Lunch (1:00 PM):** Grilled chicken breast (120g) salad with mixed greens (150g), cucumber (50g), tomato (50g), and a light vinaigrette dressing (30g). Whole wheat bread (60g).
    *   Protein: 40g, Fat: 15g, Carbs: 70g
*   **Afternoon Snack (4:00 PM):** Greek yogurt (170g, non-fat) with a banana (120g).
    *   Protein: 20g, Fat: 0g, Carbs: 40g
*   **Dinner (7:00 PM):** Baked salmon (140g) with steamed broccoli (200g) and quinoa (75g dry weight).
    *   Protein: 40g, Fat: 20g, Carbs: 80g
*   **Evening Snack (9:00 PM):** Small handful of almonds (20g).
    *   Protein: 8g, Fat: 12g, Carbs: 15g

This meal plan prioritizes lean protein sources, whole grains, fruits, and vegetables, while limiting saturated and trans fats to support healthy cholesterol levels.
</ideal_output>
This example meal plan is well-structured, provides detailed information on food choices and quantities, and aligns with the athlete's goals and restrictions.
"""

results = evaluator.run_evaluation(
    run_prompt_function=run_prompt,
    dataset_file="dataset.json",
    prompt=clear_direct_specific_with_xml_and_examples,
    extra_criteria="""
    The output should include:
    - Daily caloric total
    - Macronutrient breakdown
    - Meals with exact foods, portions, and timing
    """,
)

```