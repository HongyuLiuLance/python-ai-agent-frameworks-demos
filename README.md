# Cooking Agent

A Python desktop application that downloads a cooking video’s audio, transcribes it with Azure Whisper, and automatically extracts:

- **Ingredients** (with quantities)  
- **Step-by-step instructions**

Built with:
- Azure Whisper REST API  
- Azure OpenAI chat deployments  
- PyQt5 for the GUI  

---

## Table of Contents

1. [Features](#features)  
2. [Project Structure](#project-structure)  
3. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Running](#running)  
4. [Team & Category](#team--category)  
5. [Submission](#submission)  
6. [Demo Video](#demo-video)  
7. [Architecture](#architecture)  
8. [Judging Criteria](#judging-criteria)  
9. [License](#license)  
10. [Contact](#contact)  

---

## Features

1. **Download & Transcribe**  
   Uses `yt-dlp` to fetch audio and Azure Whisper to produce a transcript.  
2. **Ingredient Extraction**  
   Calls Azure OpenAI to parse “Ingredient: Quantity” pairs.  
3. **Step Extraction**  
   Calls Azure OpenAI to parse cooking steps into an ordered list.  
4. **Desktop UI**  
   Enter a YouTube cooking video URL → see ingredients on the left and steps on the right.

---

## Project Structure

.
├── examples
│   └── cooking_agent
│       ├── agent
│       │   └── cooking_agent.py           # Core orchestrator
│       ├── app.py                         # PyQt5 GUI definition
│       ├── main.py                        # Entry script (bridges GUI and agent)
│       └── tools
│           ├── transcribe_tool.py         # Whisper transcription tool
│           ├── extract_ingredients_tool.py  # Ingredient extraction tool
│           └── extract_steps_tool.py      # Step extraction tool
├── infra
│   ├── write_dot_env.sh                   # azd post-provision script (POSIX)
│   └── write_dot_env.ps1                  # azd post-provision script (Windows)
├── .env.example                           # Sample environment variables
├── requirements.txt
├── azure.yaml                             # Azure Developer CLI configuration
└── README.md

---

## Getting Started

### Prerequisites

- **Python 3.10+**  
- **ffmpeg** installed and on your PATH  
- An **Azure OpenAI** resource with:  
  - a **Whisper** deployment  
  - a **chat** model deployment  
- A `.env` file populated from `.env.example` with:
  ```ini
  OPENAI_API_TYPE=azure
  OPENAI_API_BASE=https://<your-resource>.cognitiveservices.azure.com
  OPENAI_API_VERSION=2025-03-01-preview
  OPENAI_API_KEY=<your-key>
  OPENAI_DEPLOYMENT=<your-whisper-deployment>
  AZURE_OPENAI_CHAT_DEPLOYMENT=<your-chat-deployment>

## Installation

git clone https://github.com/<you>/python-ai-agent-frameworks-demos.git
cd python-ai-agent-frameworks-demos
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your Azure details

## Running

PYTHONPATH=. python -m examples.cooking_agent.main

	1.	Paste a YouTube cooking video URL into the GUI.
	2.	Click Submit.
	3.	View the extracted ingredients and steps.

## Team & Category
	•	Team Members: Hongyu Liu (zero0lancelot@gmail.com), Carl Li (lishilin15@gmail.com)
	•	Category: Best Agent in Python

## Submission
	•	Deadline: April 30 2025, 11:59 PM PST
	•	How to submit:
	1.	Fork or clone the AI Agents Hackathon repo.
	2.	Create a new issue using the hackathon’s issue template.
	3.	Fill in all required fields and attach your project link.

## Demo Video

≤ 5 minutes, covering:
	1.	Project demo
	2.	Development experience
	3.	Motivation for this solution
	4.	How the agentic framework enabled your solution

Watch the demo on YouTube

https://youtu.be/_3-4XBTJe5o

## Architecture

graph LR
  UI[PyQt5 UI] --> Agent[CookingAgent]
  Agent --> T1[TranscribeVideoTool]
  T1 --> Whisper[Azure Whisper REST]
  Agent --> T2[ExtractIngredientsTool]
  T2 --> Chat1[Azure OpenAI Chat]
  Agent --> T3[ExtractStepsTool]
  T3 --> Chat2[Azure OpenAI Chat]

## Judging Criteria
	1.	Innovation
	2.	Impact
	3.	Usability
	4.	Solution Quality
	5.	Alignment with “Best Agent in Python”

## License

This project is licensed under the MIT License. See LICENSE for details.

## Contact

For questions or feedback, open an issue or email zero0lancelot@gmail.com or lishilin15@gmail.com