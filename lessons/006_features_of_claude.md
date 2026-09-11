# Features of Claude

## Extending Thinking
@See [Extended Thinking Example](../notebooks/006_features_of_claude.ipynb#extended-thinking-capability)

Extended thinking is Claude's **advanced reasoning feature that gives the model time to work through complex problems before generating a final response**. Think of it as Claude's "scratch paper" - you can see the reasoning process that leads to the answer, which helps with transparency and often results in better quality responses.

> 📌 **Important Note:** Extended Thinking is **not compatible** with some other features, notable message pre-filling and temperature. 
>
> See the full list of restrictions here: https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#feature-compatibility

### How Extended Thinking Works

When extended thinking is enabled, Claude's response changes from a simple text block to a structured response containing two parts:

<p align="center">
  <img src="images/claude_adv_features_extending_thinking1.png" alt="Claude Advanced Features: Extended Thinking">
</p>

With thinking enabled, you get both the reasoning process and the final answer.

The key benefits include:

* Better reasoning capabilities for complex tasks
* Increased accuracy on difficult problems
* Transparency into Claude's thought process

However, there are important trade-offs:

* Higher costs (you pay for thinking tokens)
* Increased latency (thinking takes time)
* More complex response handling in your code

### When to Use Extended Thinking

**The decision is straightforward: _use your prompt evaluations_**. Run your prompts without thinking first, and if the accuracy isn't meeting your requirements after you've already optimized your prompt, then consider enabling extended thinking. It's a tool for when standard prompting isn't quite getting you there.

### Response Structure and Security

Extended thinking responses include a **special signature** system for security:

<p align="center">
  <img src="images/claude_adv_features_extending_thinking2.png" alt="Claude Advanced Features: Extended Thinking - response">
</p>

The signature is a cryptographic token that ensures you haven't modified the thinking text. This prevents developers from tampering with Claude's reasoning process, which could potentially lead the model in unsafe directions.

### Redacted Thinking

Sometimes you'll receive a redacted thinking block instead of readable reasoning text. This **happens when Claude's thinking process gets flagged by internal safety systems**. The redacted content contains the actual thinking in encrypted form, allowing you to pass the complete message back to Claude in future conversations without losing context.

### Implementation

To enable extended thinking in your code, you need to add two parameters to your chat function:

```python
def chat(
    messages,
    system=None,
    temperature=1.0,
    stop_sequences=[],
    tools=None,
    ## these 2 are additional params for extended thinking!
    thinking=False,
    thinking_budget=1024
):
```

The thinking budget sets the maximum tokens Claude can use for reasoning. The minimum value is 1024 tokens, and your max_tokens parameter must be greater than your thinking budget.

Add the thinking configuration to your API parameters:

```python
if thinking:
    params["thinking"] = {
        "type": "enabled",
        "budget": thinking_budget
    }
```

Then call it with thinking enabled:

```python
chat(messages, thinking=True)
```

### Testing Redacted Responses

For testing purposes, you can force Claude to return a redacted thinking block by sending a special trigger string. This helps ensure your application handles redacted responses gracefully without crashing.

Extended thinking is a powerful feature when you need Claude to tackle complex reasoning tasks, but use it judiciously given the cost and latency implications. Start with standard prompting, optimize thoroughly, then add thinking when you need that extra reasoning capability.

## Image Support
@See [Image Support Example](../notebooks/006_features_of_claude.ipynb#images-support)

Claude's vision capabilities let you include images in your messages and ask Claude to analyze them in countless ways. You can ask Claude to describe what's in an image, compare multiple images, count objects, or perform complex visual analysis tasks.

### Image Handling Basics

There are several important limitations to keep in mind when working with images:

* **Up to 100 images** across all messages in a single request
* Max size of 5MB per image
* When sending one image: max height/width of `8000px`
* When sending multiple images: max height/width of `2000px`
* Images can be included as base64 encoding or a URL to the image
* Each image counts as tokens based on its dimensions: `tokens = (width px × height px) / 750`

To send an image to Claude, you include an image block in your user message alongside text blocks. Here's the structure:

```python
with open("image.png", "rb") as f:
    image_bytes = base64.standard_b64encode(f.read()).decode("utf-8")

add_user_message(messages, [
    # Image Block
    {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": "image/png",
            "data": image_bytes,
        }
    },
    # Text Block
    {
        "type": "text",
        "text": "What do you see in this image?"
    }
])
```

### Message Flow

The conversation works just like text-only interactions. Your server sends a user message containing both image and text blocks to Claude, and Claude responds with a text block containing its analysis.

<p align="center">
  <img src="images/claude_adv_features_msg_flow_with_image.png" alt="Claude Advanced Features: Message Flow with Image">
</p>

### Prompting Techniques

The key to getting good results with images is **applying the same prompting engineering techniques you'd use with text**. Simple prompts often lead to poor results. For example, asking `"How many marbles are in this image?"` might return an incorrect count.

<p align="center">
  <img src="images/claude_adv_features_prompting_images.png" alt="Claude Advanced Features: Basic Prompting with Images">
</p>

You can dramatically improve Claude's accuracy by:

* Providing detailed guidelines and analysis steps
* Using one-shot or multi-shot examples
* Breaking down complex tasks into smaller steps


### Step-by-Step Analysis

Instead of a simple question, provide Claude with a methodology:

```
Analyze this image of marbles and determine the exact count using this methodology:
1. Begin by identifying each unique marble one at a time. Assign each a number as you identify it.
2. Verify your result by counting with a different method. Start from the bottom-left corner and work row by row, from left to right.

What is the exact, verified number of marbles in this image?
```

### One-Shot Examples

You can also improve accuracy by providing examples within your message. Include an image with a known count, state the correct answer, then ask about your target image. This gives Claude a reference point for the type of analysis you want.

<p align="center">
  <img src="images/claude_adv_features_prompting_images_one_shot.png" alt="Claude Advanced Features: One Shot Example">
</p>

### Real-World Example: Fire Risk Assessment

Here's a practical application: automating fire risk assessments for home insurance. Instead of sending inspectors to every property, insurance companies can use satellite imagery and Claude's analysis.

<p align="center">
  <img src="images/claude_adv_images_example.png" alt="Claude Advanced Features: Real World Example">
</p>

The system analyzes satellite images to identify:

* Dense, close-packed trees near the residence
* Difficult access routes for emergency services
* Branches overhanging the residence

Rather than a simple prompt like `"provide a fire risk score,"` a well-structured prompt breaks down the analysis into specific steps:

```
Analyze the attached satellite image of a property with these specific steps:

1. Residence identification: Locate the primary residence on the property by looking for:
   - The largest roofed structure
   - Typical residential features (driveway connection, regular geometry)
   - Distinction from other structures (garages, sheds, pools)

2. Tree overhang analysis: Examine all trees near the primary residence:
   - Identify any trees whose canopy extends directly over any portion of the roof
   - Estimate the percentage of roof covered by overhanging branches (0-25%, 25-50%, 50-75%, 75%+)
   - Note particularly dense areas of overhang

3. Fire risk assessment: For any overhanging trees, evaluate:
   - Potential wildfire vulnerability (ember catch points, continuous fuel paths to structure)
   - Proximity to chimneys, vents, or other roof openings if visible
   - Areas where branches create a "bridge" between wildland vegetation and the structure

4. Defensible space identification: Assess the property's overall vegetative structure:
   - Identify if trees connect to form a continuous canopy over or near the home
   - Note any obvious fuel ladders (vegetation that can carry fire from ground to tree to roof)

5. Fire risk rating: Based on your analysis, assign a Fire Risk Rating from 1-4:
   - Rating 1 (Low Risk): No tree branches overhanging the roof, good defensible space around the home
   - Rating 2 (Moderate Risk): Minimal overhang (<25% of roof), some separation between tree canopies
   - Rating 3 (High Risk): Significant overhang (25-50% of roof), connected tree canopies, multiple vulnerability points
   - Rating 4 (Severe Risk): Extensive overhang (>50% of roof), dense vegetation against structure

For each item above (1-5), write one sentence summarizing your findings, with your final response being the numerical rating.
This detailed prompt guides Claude through a systematic analysis, resulting in much more accurate and useful assessments than a simple request would provide.
```

> 🎗️ **Remember:** the _same prompting techniques that work for text apply to images_. Invest time in crafting detailed, structured prompts rather than relying on simple questions if you want reliable results.

## PDF Support

Claude can read and analyze PDF files directly, making it a powerful tool for document processing. This capability works similarly to image processing, but with a few key differences in how you structure your code.

### Setting Up PDF Processing

To process a PDF file with Claude, you'll use nearly identical code to what you'd use for images. The main differences are in the file type specifications and variable names for clarity.

Here's how to modify your existing image processing code for PDFs:

```python
with open("earth.pdf", "rb") as f:
    file_bytes = base64.standard_b64encode(f.read()).decode("utf-8")

messages = []

add_user_message(
    messages,
    [
        {
            "type": "document",
            "source": {
                "type": "base64",
                "media_type": "application/pdf",
                "data": file_bytes,
            },
        },
        {"type": "text", "text": "Summarize the document in one sentence"},
    ],
)

chat(messages)
```

### Key Changes from Image Processing

When adapting your image processing code for PDFs, you need to update several elements:

* Change the file extension from `.png` to `.pdf`
* Update the variable name from `image_bytes` to `file_bytes` for clarity (this is a variable, so use a clear name!)
* Set the type to `"document"` instead of `"image"`
* Change the media type to `"application/pdf"` instead of `"image/png"`

### What Claude Can Extract from PDFs

Claude's PDF processing capabilities go beyond simple text extraction. It can analyze and understand:

* Text content throughout the document
* Images and charts embedded in the PDF
* Tables and their data relationships
* Document structure and formatting

This makes Claude essentially a one-stop solution for extracting any type of information from PDF documents, whether you need summaries, data analysis, or specific content extraction.

![Earth PDF](images/earth_pdf.png)

The example above shows Claude successfully processing a Wikipedia article about Earth that was saved as a PDF, demonstrating how it can understand and summarize complex document content in a single sentence.

