# examples/cooking_agent/tools/extract_steps_tool.py

import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI

class ExtractStepsTool:
    """
    Extracts cooking steps from a transcript using Azure OpenAI.
    Returns a list of step descriptions, e.g. ["Heat pan and add oil", "Stir-fry onions", ...].
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
        # Deployment name for the chat model
        self.model = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT")

    def run(self, transcript: str) -> list[str]:
        # Prepare system and user messages
        system_message = {
            "role": "system",
            "content": (
                "You are a cooking assistant. Extract the sequence of cooking steps "
                "from the following transcript. Return only a JSON array of step descriptions, "
                "without numbering or extra commentary."
            )
        }
        user_message = {"role": "user", "content": transcript}

        # Call the Azure OpenAI chat completion endpoint
        response = self.client.chat.completions.create(
            model       = self.model,
            messages    = [system_message, user_message],
            temperature = 0.0,
        )

        raw_output = response.choices[0].message.content.strip()

        # Attempt to parse the output as JSON
        try:
            steps = json.loads(raw_output)
            if not isinstance(steps, list):
                raise ValueError("Expected a JSON array of steps")
            return [step.strip() for step in steps]
        except Exception:
            # Fallback: split lines if JSON parsing fails
            return [line.strip() for line in raw_output.splitlines() if line.strip()]
