import os
import httpx
from dotenv import load_dotenv

load_dotenv()

class LLMProvider:

    def __init__(self):
        self.api_key = os.getenv("MISTRAL_API_KEY")
        self.model = os.getenv("MISTRAL_MODEL", "mistral-large-latest")


    def generate(self, prompt: str):

        response = httpx.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": self.model,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are Vera, Magicpin's AI growth assistant.",
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                "temperature": 0.2,
            },
            timeout=20,
        )

        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]