# modified helper functions
from anthropic.types import Message
from rich.console import Console


def add_user_message(messages, message):
    user_message = {
        "role": "user",
        "content": message.content if isinstance(message, Message) else message,
    }
    messages.append(user_message)


def add_assistant_message(messages, message):
    if isinstance(message, list):
        assistant_message = {
            "role": "assistant",
            "content": message,
        }
    elif hasattr(message, "content"):
        content_list = []
        for block in message.content:
            if block.type == "text":
                content_list.append({"type": "text", "text": block.text})
            elif block.type == "tool_use":
                content_list.append(
                    {
                        "type": "tool_use",
                        "id": block.id,
                        "name": block.name,
                        "input": block.input,
                    }
                )
        assistant_message = {
            "role": "assistant",
            "content": content_list,
        }
    else:
        # String messages need to be wrapped in a list with text block
        assistant_message = {
            "role": "assistant",
            "content": [{"type": "text", "text": message}],
        }
    messages.append(assistant_message)


def chat(
    client,
    model,
    messages,
    system=None,
    temperature=1.0,
    max_tokens=4096,
    stop_sequences=[],
    # for adding tools capability
    tools=None,
    # for extended thinking
    thinking=False,
    thinking_budget=1024,
):
    params = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": messages,
        "stop_sequences": stop_sequences,
        # this will work with older (<1.1.0) SDK
        # "temperature": temperature,
        # ------------------------------
        # for 1.1.0+ SDK use the following
        "extra_body": {"temperature": temperature},
    }

    if thinking:
        params["thinking"] = {
            "type": "enabled",
            "budget_tokens": thinking_budget,
        }

    if tools:
        params["tools"] = tools

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message


def chat_stream(
    client,
    model,
    messages,
    system=None,
    temperature=1.0,
    stop_sequences=[],
    # for adding tools capability
    tools=None,
    tool_choice=None,
    betas=[],
    # for extended thinking
    thinking=False,
    thinking_budget=1024,
):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "stop_sequences": stop_sequences,
        # this will work with older (<1.1.0) SDK
        # "temperature": temperature,
        # ------------------------------
        # for 1.1.0+ SDK use the following
        "extra_body": {"temperature": temperature},
    }

    if thinking:
        params["thinking"] = {
            "type": "enabled",
            "budget_tokens": thinking_budget,
        }

    if tool_choice:
        params["tool_choice"] = tool_choice

    if tools:
        params["tools"] = tools

    if system:
        params["system"] = system

    if betas:
        params["betas"] = betas

    return client.beta.messages.stream(**params)


def text_from_message(message):
    return "\n".join([block.text for block in message.content if block.type == "text"])


def run_tools(message, run_tool_function):
    """finds out tools from message block and runs the tools"""
    tool_requests = [block for block in message.content if block.type == "tool_use"]
    tool_result_blocks = []

    for tool_request in tool_requests:
        try:
            tool_output = run_tool_function(tool_request.name, tool_request.input)
            tool_result_block = {
                "type": "tool_result",
                "tool_use_id": tool_request.id,
                "content": json.dumps(tool_output),
                "is_error": False,
            }
        except Exception as e:
            tool_result_block = {
                "type": "tool_result",
                "tool_use_id": tool_request.id,
                "content": f"Error: {e}",
                "is_error": True,
            }

        tool_result_blocks.append(tool_result_block)

    return tool_result_blocks


def run_conversation(
    client,
    model_name,
    messages,
    run_tools_function,
    tool_schemas=[],
    run_in_notebook=True,
):
    console = Console(console=Console(force_jupyter=(not run_in_notebook)))

    while True:
        response = chat(
            client,
            model_name,
            messages,
            tools=tool_schemas,
        )

        add_assistant_message(messages, response)
        # added this print so we can follow along
        console.print(
            f"[blue]Got response from chat:[/blue] {response}\n[yellow]-----[/yellow]"
        )
        text_response = text_from_message(response)
        # added this print so we can follow along
        console.print(f"[green]text_from_message:[/green] {text_response}\n")
        console.print(
            f"[red]Stop reason:[/red] {response.stop_reason}\n[yellow]-----[/yellow]"
        )

        if response.stop_reason != "tool_use":
            break

        tool_results = run_tools(response, run_tools_function)
        add_user_message(messages, tool_results)

    return messages


def stream_conversation(
    client,
    model,
    messages,
    run_tools_function,
    tool_schemas=[],
    tool_choice=None,
    fine_grained=False,
    run_in_notebook=True,
):
    console = Console(force_jupyter=(not run_in_notebook))

    while True:
        with chat_stream(
            client,
            model,
            messages,
            tools=tool_schemas,
            betas=["fine-grained-tool-streaming-2025-05-14"] if fine_grained else [],
            tool_choice=tool_choice,
        ) as stream:
            for chunk in stream:
                if chunk.type == "text":
                    print(chunk.text, end="")

                if chunk.type == "content_block_start":
                    if chunk.content_block.type == "tool_use":
                        console.print(
                            f'\n[red]>>> Tool Call:[/red] "{chunk.content_block.name}"'
                        )

                if chunk.type == "input_json" and chunk.partial_json:
                    print(chunk.partial_json, end="")

                if chunk.type == "content_block_stop":
                    print("\n")

            response = stream.get_final_message()

        add_assistant_message(messages, response)
        # added this print so we can follow along
        console.print(
            f"[blue]Got response from stream:[/blue] {response}\n[yellow]-----[/yellow]"
        )

        if response.stop_reason != "tool_use":
            break

        tool_results = run_tools(response, run_tools_function)
        add_user_message(messages, tool_results)

        if tool_choice:
            break

    return messages


def add_user_media_message(
    messages,
    media_bytes,
    user_message,
    media_type,  # ["image/png","image/jpeg","application/pdf", "text/plain" etc]
    title=None,
    enable_citations=False,
):
    # build the message block - it should look something like this
    """
    [
        # add an media block
        {
            "type": "image" or "document"
            "source": {
                "type": "base64",
                "media_type": media_type,
                "data": media_bytes,
            },
            # these two fields needed if citations requested
            "title": "earth.pdf",  # title of document
            "citations": { "enabled": True }
        },
        # add user block
        {"type": "text", "text": user_message},
    ],
    """

    media_block = {
        "source": {
            "type": "text" if media_type == "text/plain" else "base64",
            "media_type": media_type,
            "data": media_bytes,
        },
    }

    type = "image" if media_type.strip().startswith("image") else "document"
    media_block["type"] = type

    if enable_citations:
        # citations make sense only if type == "document"
        if type != "document":
            raise ValueError(
                "ERROR: for citations, user message type must be 'document'"
            )
        # require title if citations are enabled
        if title is None:
            raise ValueError(
                "ERROR: `title` parameter is required if citations requested!"
            )
        # give your document a readable name
        media_block["title"] = title
        media_block["citations"] = {"enabled": True}

    user_query_block = {"type": "text", "text": user_message}

    add_user_message(
        messages,
        [
            # add an image block first
            media_block,
            # {
            #     "type": "image",
            #     "source": {
            #         "type": "base64",
            #         "media_type": media_type,
            #         "data": media_bytes,
            #     },
            # },
            # and now the user query
            user_query_block,
            # {"type": "text", "text": user_message},
        ],
    )
