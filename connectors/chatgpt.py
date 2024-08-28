from openai import OpenAI
from typing import List


class ChatGPTConnector:

    def __init__(self) -> None:
        self.client = OpenAI()

    def chat_create_json(
        self, model: str, system_instructions: str, response_format: dict
    ) -> dict:

        completion = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": system_instructions}],
            response_format=response_format,
        )

        return completion.choices[0].message.content
