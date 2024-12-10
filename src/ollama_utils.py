from ollama import Client


def ollama_quick_chat(system_message, user_input, llm="llama3:8b-instruct-fp16"):
    """
    Sends a chat request to the Ollama client with the specified user input and system message.

    Parameters:
    system_message (str, optional): The system message to provide context or instructions. Defaults to an empty string.
    user_input (str): The input message from the user.
    llm (str, optional): The model to use for the chat. Defaults to 'llama3:8b-instruct-fp16'.

    Returns:
    dict: The response from the Ollama client.
    """

    # Instantiate Ollama client
    client = Client(host="http://127.0.0.1:11434")

    response = client.chat(
        model=llm,
        messages=[
            {
                "role": "system",
                "content": f"{system_message}",
            },
            {
                "role": "user",
                "content": f"{user_input}",
            },
        ],
    )

    return response  # Return response from client
