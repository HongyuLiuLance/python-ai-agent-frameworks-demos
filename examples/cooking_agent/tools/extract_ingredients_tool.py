# examples/cooking_agent/tools/extract_ingredients_tool.py

import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI

class ExtractIngredientsTool:
    """
    Uses Azure OpenAI to extract ingredients and quantities from a transcript.
    Returns a list of strings like "Tomato: 2 pcs".
    """

    def __init__(self):
        # Load environment variables from .env
        load_dotenv()

        # Initialize the Azure OpenAI client
        self.client = AzureOpenAI(
            api_key        = os.getenv("OPENAI_API_KEY"),
            azure_endpoint = os.getenv("OPENAI_API_BASE"),
            api_version    = os.getenv("OPENAI_API_VERSION"),
        )
        # Name of the deployment for the chat model
        self.model = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")

    def run(self, transcript: str) -> list[str]:
        # Build the prompt messages
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a cooking assistant. Extract only the ingredients and their "
                    "quantities from the transcript. Do not add any other commentary."
                )
            },
            {
                "role": "user",
                "content": (
                    "Please return only a JSON array of strings, each in the format "
                    "\"Ingredient: Quantity\", for example:\n"
                    "[\"Tomato: 2 pcs\", \"Egg: 3 pcs\", ...]\n"
                    "Do not include explanations, line breaks, or extra text.\n\n"
                    f"{transcript}"
                )
            }
        ]

        # Call the Azure OpenAI chat completion endpoint
        response = self.client.chat.completions.create(
            model       = self.model,
            messages    = messages,
            temperature = 0.0,
        )

        # Get the raw JSON text from the response
        raw = response.choices[0].message.content.strip()

        # Attempt to parse it as JSON
        try:
            data = json.loads(raw)
            if not isinstance(data, list):
                raise ValueError("Returned JSON is not a list")
            return [item.strip() for item in data]
        except Exception:
            # Fallback: split by lines if JSON parsing fails
            return [line.strip() for line in raw.splitlines() if line.strip()]