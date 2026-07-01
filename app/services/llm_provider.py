import os

from mistralai import Mistral


class LLMProvider:

    def __init__(self):
        self.client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
        self.model = os.getenv("MISTRAL_MODEL", "mistral-large-latest")

    def generate(self, prompt: str):

        response = self.client.chat.complete(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are Vera, Magicpin's AI growth assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content