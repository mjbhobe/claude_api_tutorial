# Using Tools with Claude

Tools allow Claude to access information from the outside world, extending its capabilities beyond what it learned during training. By default, Claude only knows information from its training data and can't access current events, real-time data, or external systems. Tool use solves this limitation by creating a structured way for Claude to request and receive fresh information.

## The Problem Without Tools

When users ask Claude for current information, it hits a wall. For example, if someone asks `"What's the weather in San Francisco, California?"` Claude has to respond with something like `"I'm sorry, but I don't have access to up-to-date weather information."`.

This creates a frustrating user experience when people need real-time data that Claude could theoretically help with if it just had access to current information.

## How Tool Use Works

Tool use follows a specific back-and-forth pattern between your application and Claude. Here's the complete flow:

<p align="center">
  <img src="images/how_tool_usage_works.png" alt="How Tools Usage Works" width="450" height="300">
</p>

1. `Initial Request`: You send Claude a question **along with instructions on how to get extra data from external sources** (i.e. list of tools and when & how to call them)
2. `Tool Request`: Claude analyzes the question and decides it needs additional information. So tells your server that it needs extra info - it can determine this from the extra info. we sent it along with our request.
3. `Data Retrieval`: **Your server runs code to fetch the requested information from external APIs or databases** - this is important to understand. Claude _cannot_ run any code to fetch extra info - it can only tell your server that it needs extra info and server calls the function(s).
4. `Server fetches info`: The server calls APIs/function/makes-Db-call (whatever is needed) to fetch the _extra_ information.
5. `Final Response`: Your server the _raw retrieved data_ back to Claude, which then generates a complete response using both the original question and the fresh data.

### Weather Example in Practice

Let's see how this works with the weather question. The process becomes much more specific:

<p align="center">
  <img src="images/tool_usage_example_weather.png" alt="Weather Data Fetch Example" width="450" height="300">
</p>

When a user asks about current weather [for example: `what's the current weather in Mumbai?`], **you include instructions in your prompt about how to retrieve weather data** (maybe your prompt tells Claude to call a `get_weather` function with city name as parameter for example). Claude recognizes it needs current information tells your server to fetch the additional info (for example, tells your server that it should call the `get_weather("Mumbai")` function). Your server then calls the `get_weather(...)` function, which could use weather API to get real-time conditions for a city/ The server will then send the raw data it fetched back to Claude. Finally, Claude combines the fresh weather data with the user's question to provide an accurate, current response.

### Key Benefits

* `Real-time Information`: Access current data that wasn't available during Claude's training
* `External System Integration`: Connect Claude to databases, APIs, and other services
* `Dynamic Responses`: Provide answers based on the latest available information
* `Structured Interaction`: Claude knows exactly what information it needs and how to ask for it

Tool use transforms Claude from a static knowledge base into a dynamic assistant that can work with live data. This opens up possibilities for building applications that need current information, whether that's weather data, stock prices, database queries, or any other real-time information your users might need.

## Practical Example of Tool Usage

We're going to build a practical project that teaches Claude how to set reminders for future dates. This might sound simple at first, but it reveals several interesting challenges that we'll solve using custom tools.

The goal is straightforward: we want to be able to tell Claude `"Set a reminder for my doctor's appointment. It's a week from Thursday"` and have Claude respond with `"OK, I will remind you"`. Making this possible is not as easy as it sounds - we need to address some limitations in how Claude handles time and reminders.

### Why This Is Challenging?

While Claude knows the current date, there are three specific problems we need to solve:

* `Limited time awareness`: Claude might know the current date, but not the exact time.
* `Date calculation issues`: Claude doesn't always handle time-based addition well, especially when looking many days into the future
* `No reminder capability`: Claude doesn't know how to set a reminder - it has no built-in mechanism for this!

Each of these limitations represents a gap between what Claude can do naturally and what we need for our reminder system. Tools are how we bridge these gaps.

### Tools We'll Need to create

<p align="center">
  <img src="images/tools_well_need.png" alt="Tools We'll Need" width="450" height="150">
</p>

We'll create three separate tools to handle each challenge:

1. `Get the current date time`: Claude needs to know the current date and time precisely
2. `Add duration to date time`: Claude isn't perfect with date time addition, so we'll give it a reliable tool for this
3. `Set a reminder`: We need a way to actually set a reminder in the system (some API to interface with your calendar and set reminder for that date/time)

We'll implement these tools one at a time, starting with the simplest one. This approach lets us understand how tool calling works before building more complex functionality. By the end, Claude will be able to handle natural language requests like `"remind me in a week"` by combining these tools to calculate the exact time and set the reminder.

### What Are Tool Functions?

A tool function is a plain Python function that gets executed automatically when Claude decides it needs extra information to help a user. For example, if someone asks `"What's the weather in Mumbai?"`, Claude would call (i.e. ask your server to call) your weather tool to get the weather information.

Here's an example of a weather tool function. Notice how it validates inputs and provides clear error messages - these are important best practices.

```python
def get_weather(location):
    if not location or location.strip() == "":
        raise ValueError("Location cannot be empty!")

    url = "https://fakeweatherapi.example.com/current"
    params = {
        "q" : location,
        "appid" : api_key,
        "units" : "metric"
    }

    response = requests.get(url, params=params, timeout=10.0)
    response.raise_for_status()

    return response.json()
```

### Best Practices for Tool Functions

When writing tool functions, follow these guidelines:

* **Use descriptive names**: Both your function name and parameter names should clearly indicate their purpose
* **Validate inputs**: Check that required parameters aren't empty or invalid, and raise errors when they are
* **Provide meaningful error messages**: Claude can see error messages and might retry the function call with corrected parameters

**The validation is particularly important** because Claude learns from errors. If you raise a clear error like `"Location cannot be empty"`, Claude might try calling the function again with a proper location value.

### Building Your First Tool Function

Let's create a function to get the current date and time. This function will accept a date format parameter so Claude can request the time in different formats:

```python
from datetime import datetime

def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    if not date_format:
        raise ValueError("date_format cannot be empty")
    return datetime.now().strftime(date_format)
```

This function uses Python's datetime module to get the current time and format it according to the provided format string. The default format gives us year-month-day hour:minute:second.

You can test it with different formats:

```python
# Default format: "2024-01-15 14:30:25"
get_current_datetime()

# Just hour and minute: "14:30"
get_current_datetime("%H:%M")
```

The validation check ensures Claude can't pass an empty string for the date format. While this specific error is unlikely, it demonstrates the pattern of validating inputs and providing helpful error messages that Claude can learn from.

Creating the function is just the first step. Next, **you'll need to write a JSON schema that describes the function to Claude, then integrate it into your chat system**. This tool function approach gives Claude powerful capabilities while keeping your code organized and maintainable.

## Tool Schemas

After writing your tool function, the next step is **creating a JSON schema that tells Claude what arguments your function expects and how to use it**. This schema acts as documentation that Claude reads to understand when and how to call your tools.

### Understanding JSON Schema

JSON Schema isn't specific to AI or tool calling - it's a widely-used data validation specification that's been around for years. The AI community adopted it because it's a convenient way to describe function parameters and validate data.

Here is an example:

```json
{
    "name" : "get_weather",
    "description" : "Retrieves current weather for a specific location",
    "input_schema" : {
        "type" : "object",
        "properties" : {
            "location" : {
                "type" : "string",
                "description" : "The location for which the weather information is desired (e.g. Mumbai)"
            }
        },
        "required" : [
            "location",
        ]
    }
}
```

The complete tool specification has three main parts:

* `name` - A clear, descriptive name for your tool (like "get_weather")
* `description` - What the tool does, when to use it, and what it returns
* `input_schema` - The actual JSON schema describing the function's arguments

### Writing Effective Descriptions

Your _tool description is crucial_ for helping Claude understand when to use your function. Best practices include:

* Aim for 3-4 sentences explaining what the tool does
* Describe when Claude should use it
* Explain what kind of data it returns
* Provide detailed descriptions for each argument.

### The Easy Way to Generate Schemas

Writing a schema definition like the one above by hand is tedious and error prone. A much easier was is to ask Claude itself to generate them 😊. 

Here's the process:

* Copy your tool function code 
* Go to Claude (`claude.ai`) and ask it to write a JSON schema for tool calling
* Include the Anthropic documentation on tool use as context
* Let Claude generate a properly formatted schema following best practices

The prompt should be something like: `"Write a valid JSON schema spec for the purposes of tool calling for this function. Follow the best practices listed in the attached documentation."`

Once Claude generated the scheme for us, we can copy it into our code file (where we define the tool functions), like this:

```python
from datetime import datetime

def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    # tool function
    ...


get_current_datetime_schema = {
    "name": "get_current_datetime",
    "description": "Returns the current date and time formatted according to the specified format",
    "input_schema": {
        "type": "object",
        "properties": {
            "date_format": {
                "type": "string",
                "description": "A string specifying the format of the returned datetime. Uses Python's strftime format codes.",
                "default": "%Y-%m-%d %H:%M:%S"
            }
        },
        "required": []
    }
}
```

#### Adding Type Safety

For better type checking, import and use the `ToolParam` type from the Anthropic library:

```python
from anthropic.types import ToolParam

get_current_datetime_schema = ToolParam({
    "name": "get_current_datetime",
    "description": "Returns the current date and time formatted according to the specified format",
    # ... rest of schema
})
```

While not strictly necessary for functionality, this prevents type errors when you use the schema with Claude's API and makes your code more robust.

## Handling Message Blocks

**When working with Claude's tool functionality**, you'll encounter a new type of response structure that's different from the simple text responses you've seen before. Instead of just getting back a single text block, **Claude now returns multi-block messages that contain both text and tool usage information**.

### Making Tool-Enabled API Calls

To enable Claude to use tools, you need to include a `tools` parameter in your API call. Here's how to structure the request:

```python
messages = []

messages.append({
    "role": "user",
    "content": "What is the exact time, formatted as HH:MM:SS?"
})

response = client.messages.create(
    model=MODEL,
    max_tokens=MAX_TOKENS,
    messages=messages,
    # NOTE: we pass the schema, not function name!
    tools=[get_current_datetime_schema],
)
```

The `tools` parameter takes a list of **JSON schemas** that describe the available functions Claude can call. Running the above code should produce output like this.

<p align="center">
  <img src="images/message_block_example.png" alt="Message Block example" width="450">
</p>

This is a structure we have not seen before. Notice that the `content` is a list, but `content[0]` is **not** a text block. Instead you see a `ToolUseBlock`

### Understanding Multi-Block Messages

When Claude decides to use a tool, it returns an assistant message with multiple blocks in the content list. This is a significant change from the simple text-only responses you've worked with before.

<p align="center">
  <img src="images/multi_block_messages.png" alt="Multi-block Messages" width="450" height="150">
</p>

A multi-block message typically contains:

* `Text Block` - Human-readable text explaining what Claude is doing (like "I can help you find out the current time. Let me find that information for you") (📌 optional**)
* `ToolUseBlock` - Instructions for your code about which tool to call and what parameters to use 

The ToolUse block includes:

* An `id` for tracking the tool call
* The `name` of the function to call (like `"get_current_datetime"`)
* Input parameters (`input`) formatted as a dictionary (`input={"date_format":"%H:%M:%S"}`)
* The `type` designation `"tool_use"`

### Managing Conversation History with Multi-Block Messages

Remember that Claude doesn't store conversation history - you need to manage it manually. When working with tool responses, you must preserve the entire content structure, including all blocks.

Here's how to properly append a multi-block assistant message to your conversation history:

```python
messages.append({
    "role": "assistant",
    # NOT response.content[0].text!
    "content": response.content
})
```

This preserves both the text block and the tool use block, which is crucial for maintaining the conversation context when you make subsequent API calls.

### The Complete Tool Usage Flow

The tool usage process follows this pattern:

1. Send user message with tool schema to Claude
2. Receive assistant message with text block **and** tool use block
3. Extract tool information and execute the actual function
4. Send tool result back to Claude along with complete conversation history
5. Receive final response from Claude

Each step requires careful handling of the message structure to ensure Claude has the full context it needs to provide accurate responses.

### Updating Helper Functions

We'll need to update our helper functions  `add_user_message()` and `add_assistant_message()` to handle multi-block content. They now need to accommodate the more complex content structures that include tool use blocks.

This multi-block message handling is essential for building robust applications that can seamlessly integrate Claude's tool capabilities while maintaining proper conversation flow.

## Sending Tool Results

