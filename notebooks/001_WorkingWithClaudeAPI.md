# Working with the Claude API

When building applications with Claude, understanding the complete request lifecycle helps you make better architectural decisions and debug issues more effectively. Let's walk through what happens from the moment a user clicks "send" in your chat interface to when Claude's response appears on screen.

![Chat Example](images/chat_example.png)

## The Five-Step Request Flow

Every interaction with Claude follows a predictable pattern with five distinct phases: request to server, request to Anthropic API, model processing, response to server, and response to client.

![Five Step Request Flow - Step 1](images/five_step_request_flow1.png)

### Why You Need a Server

You should **never make requests to the Anthropic API directly from client-side code**. Here's why:

API requests require a secret API key for authentication Exposing this key in client code creates a serious security vulnerability. Anyone could extract the key and make unauthorized requests. Instead, your web or mobile app sends requests to your own server, which then communicates with the Anthropic API using the securely stored key.

### Making API Requests

When your server contacts the Anthropic API, you can use either an official SDK or make plain HTTP requests. Anthropic provides SDKs for Python, TypeScript, JavaScript, Go, and Ruby.

![Five Step Request Flow - Step 2](images/five_step_request_flow2.png)

Every request must include these essential fields:

* **API Key** - Identifies your request to Anthropic
* **Model** - Name of the model to use (such as, "`claude-haiku-4-5-20251001`"  or "`claude-sonnet-4-5`")
* **Messages** - List containing the user's input text
* **Max Tokens** - Limit for how many tokens Claude can generate

### Inside Claude's Processing

Once Anthropic receives your request, Claude processes it through four main stages: tokenization, embedding, contextualization, and generation.

**Tokenization**

Claude first breaks your input text into smaller chunks called tokens. These can be whole words, parts of words, spaces, or symbols. For simplicity, think of each word as one token.

![Tokenization](images/tokenization.png)

**Embedding**

Each token gets converted into an embedding - a long list of numbers that represents all possible meanings of that word. Think of embeddings as numerical definitions that capture semantic relationships.

Words often have multiple meanings. For example, "quantum" could refer to:

![One Word Many Meanings](images/one_word_many_meanings.png)

* A discrete unit of physical quantity (physics)
* Quantum mechanics or quantum physics concepts
* Something extremely small or subatomic
* Quantum computing applications

** Contextualization**

Claude refines each embedding based on surrounding words to determine the most likely meaning in context. This process adjusts the numerical representations to highlight the appropriate definition.

![Contextualization](images/contextualization.png)

** Generation **

The contextualized embeddings pass through an output layer that calculates probabilities for each possible next word. Claude doesn't always pick the highest probability word - it uses a mix of probability and controlled randomness to create natural, varied responses.

![Generation](images/generation.png)

** When Claude Stops Generating?**

After each token, Claude checks several conditions to decide whether to continue:

![Stops Generation](images/stops_generation.png)

**The API Response**

When generation completes, the API sends back a structured response containing:

* Message - The generated text
* Usage - Count of input and output tokens
* Stop Reason - Why generation ended

![Five Step Request Flow - Step 4](images/five_step_request_flow4.png)


Your server receives this response and forwards the generated text back to your client application, where it appears in the user interface.

![Five Step Request Flow - Step 5](images/five_step_request_flow5.png)

## Key Takeaways

Understanding this flow helps you:

* Design secure architectures that protect your API keys
* Set appropriate token limits for your use case
* Handle different stop reasons in your application logic
* Debug issues by understanding where they might occur in the pipeline