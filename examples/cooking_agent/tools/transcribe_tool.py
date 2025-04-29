# examples/cooking_agent/tools/transcribe_tool.py

import os
import re
import subprocess
import requests
from dotenv import load_dotenv

load_dotenv()

# Azure Whisper configuration from environment
API_KEY     = os.getenv("AZURE_OPENAI_API_KEY")
ENDPOINT    = os.getenv("AZURE_OPENAI_ENDPOINT").rstrip("/")
API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
DEPLOYMENT  = os.getenv("AZURE_OPENAI_DEPLOYMENT")


class TranscribeVideoTool:
    """
    Download a video's audio track via yt-dlp, convert to MP3, 
    and transcribe it using Azure Whisper.
    """
    name = "transcribe_video"
    description = "Download and transcribe video audio with Azure Whisper."

    def run(self, video_url: str) -> str:
        # 1. Extract the YouTube video ID
        match = re.search(r"(?:v=|youtu\.be/)([\w\-]+)", video_url)
        if not match:
            raise ValueError("Unable to extract video ID from URL.")
        video_id = match.group(1)

        # 2. Download audio as MP3 using yt-dlp CLI
        audio_file = "example_audio.mp3"
        cmd = [
            "yt-dlp",
            "-f", "bestaudio",
            "--extract-audio",
            "--audio-format", "mp3",
            "--output", audio_file,
            video_url,
        ]
        print(f"[TranscribeVideoTool] Running command: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(result.stdout)
            print(result.stderr)
            raise RuntimeError("yt-dlp failed to download audio.")
        print(f"[TranscribeVideoTool] Audio downloaded and converted: {audio_file}")

        # 3. Send the MP3 to Azure Whisper REST API
        print("[TranscribeVideoTool] Sending audio to Azure Whisper for transcription...")
        transcribe_url = f"{ENDPOINT}/openai/deployments/{DEPLOYMENT}/audio/transcriptions"
        params = {"api-version": API_VERSION}
        headers = {"api-key": API_KEY}
        with open(audio_file, "rb") as f:
            files = {"file": (audio_file, f, "audio/mpeg")}
            response = requests.post(transcribe_url, params=params, headers=headers, files=files)
        response.raise_for_status()

        # 4. Parse and return the transcription text
        data = response.json()
        transcript = data.get("text") or data.get("transcription")
        print("[TranscribeVideoTool] Transcription completed.")
        return transcript