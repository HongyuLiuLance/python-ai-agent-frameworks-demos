Cooking Agent

An end-to-end Cooking Agent that:
	1.	Downloads and transcribes cooking tutorial videos (YouTube or local audio).
	2.	Extracts ingredients and their quantities.
	3.	Extracts step-by-step cooking instructions.

All powered by Azure Whisper for transcription and Azure OpenAI for information extraction.

⸻

Features
	•	Video Transcription: Uses yt-dlp to download audio and Azure Whisper REST API for transcription.
	•	Ingredient Extraction: Prompts an Azure OpenAI chat model to return a structured JSON list of ingredients.
	•	Step Extraction: Prompts the same model to return a JSON list of cooking steps.

⸻

Prerequisites
	•	Python 3.10+ installed
	•	ffmpeg available on PATH
	•	An Azure Cognitive Services resource with OpenAI deployed:
	•	Whisper-enabled deployment (e.g., gpt-4o-transcribe)
	•	Chat model deployment (e.g., gpt-4.1-chat)
	•	A .env file with the following variables:

AZURE_OPENAI_API_KEY=<your-key>
AZURE_OPENAI_ENDPOINT=https://<your-resource>.cognitiveservices.azure.com
AZURE_OPENAI_API_VERSION=2025-03-01-preview
AZURE_OPENAI_DEPLOYMENT=<your-whisper-deployment>
AZURE_OPENAI_CHAT_DEPLOYMENT=<your-chat-deployment>



⸻

Installation
	1.	Clone the repository

git clone https://github.com/<your-user>/python-ai-agent-frameworks-demos.git
cd python-ai-agent-frameworks-demos


	2.	Create a virtual environment and install dependencies

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt yt-dlp ffmpeg-python python-dotenv requests pytube


	3.	Create and edit .env at project root with your Azure credentials (see Prerequisites).

⸻

Usage

Run the main script to process a video or local audio file:

source .env
PYTHONPATH=. python3 -m examples.cooking_agent.main

You’ll be prompted to enter a YouTube URL or local audio path. The agent will then:
	1.	Transcribe the audio.
	2.	Print the raw transcript.
	3.	Extract and list ingredients.
	4.	Extract and list cooking steps.

Example output:

🔄 Transcribing audio...
📝 Transcript:
 "Hello everyone, today we'll make tomato scrambled eggs..."

🔄 Extracting ingredients...
🍅 Extracted Ingredients:
  - Tomato: 2 pcs
  - Egg: 3 pcs
  - Salt: 1 g

👩‍🍳 Extracted Cooking Steps:
  1. Dice tomatoes into evenly sized chunks.
  2. Beat eggs with salt and white vinegar.
  3. Heat oil in pan and cook eggs until set.
  4. Stir-fry tomatoes, add tomato paste and water, simmer.
  5. Season, thicken sauce, return eggs and mix.



⸻

Project Structure

examples/
└── cooking_agent/
    ├── main.py                # Entry point
    └── tools/
        ├── transcribe_tool.py # Download & transcribe
        ├── extract_ingredients_tool.py
        └── extract_steps_tool.py

requirements.txt
.env.example                 # Template for environment variables
README.md                    # This file



⸻

Contributing

Feel free to open issues or submit pull requests. Ensure you:
	•	Keep dependencies up to date in requirements.txt.
	•	Follow PEP8 and maintain consistent docstrings/comments.

⸻

© 2025 Cooking Agent Project