from openai import OpenAI
from typing import List


class ChatGPTConnector:

    def __init__(self) -> None:
        self.client = OpenAI()

    def chat_create_json(
        self, model: str, system_instructions: str, response_format: dict
    ) -> dict:
        """
        Generates a chat completion based on the specified model, system
        instructions, and response format.This function interacts with a
        chat API to create a chat completion using the provided model,
        system instructions, and response format. The completion is returned
        as a JSON-like dictionary.

        Args:
        :param model: The name of the model to use for generating the chat
        completion.
        :param system_instructions: The instructions or context to be
        provided to the system for the completion.
        :param response_format: A dictionary specifying the desired
        response format.

        :return: The content of the generated chat completion, extracted
        from the API's response.

        """

        completion = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": system_instructions}],
            response_format=response_format,
        )

        return completion.choices[0].message.content
