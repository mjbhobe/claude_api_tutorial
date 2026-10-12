def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


def chat(client, model, messages, system=None, temperature=1.0, stop_sequences=[]):
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

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message.content[0].text
