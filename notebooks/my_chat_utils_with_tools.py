# modified helper functions
from anthropic.types import Message


def add_user_message(messages, message):
    user_message = {
        "role": "user",
        "content": message.content if isinstance(message, Message) else message,
    }
    messages.append(user_message)


def add_assistant_message(messages, message):
    assistant_message = {
        "role": "assistant",
        "content": message.content if isinstance(message, Message) else message,
    }
    messages.append(assistant_message)


def chat(
    client,
    model,
    messages,
    system=None,
    temperature=1.0,
    max_tokens=4000,
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


def text_from_message(message):
    return "\n".join([block.text for block in message.content if block.type == "text"])


def add_user_media_message(
    messages,
    media_bytes,
    user_message,
    media_type,  # ["image/png","image/jpeg","application/pdf" etc]
    enable_citation=False,
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
        },
        # add user block
        {"type": "text", "text": user_message},
    ],
    """

    media_block = {
        "source": {
            "type": "base64",
            "media_type": media_type,
            "data": media_bytes,
        },
    }

    type = "image" if media_type.strip().startswith("image") else "document"
    media_block["type"] = type
    user_query_block = {"type": "text", "text": user_message}

    if enable_citation:
        # assert type == "document", ""
        media_block["citations"] = '{"enabled" : True}'

    # print(f"add_user_media_message -> user_message = {[media_block, user_query_block]}")

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
