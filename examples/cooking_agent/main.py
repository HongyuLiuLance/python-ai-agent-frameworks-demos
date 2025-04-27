from openai import AzureOpenAI
import download
import extract

OPENAI_API_KEY = 'CLW2Qniw6YNf0bHoe9j0kVGiuNE7jxqmOguOsaFA7yftmfqgMIcSJQQJ99BDACHYHv6XJ3w3AAAAACOGEYlZ'
OPENAI_VERSION = '2025-03-01-preview'
AZURE_ENDPOINT = 'https://sli39-m9z5fe1j-eastus2.cognitiveservices.azure.com/openai/deployments/gpt-4o-transcribe/audio/transcriptions?api-version=2025-03-01-preview'

url = "https://www.youtube.com/shorts/x0zx32CbcKY"
download.download_youtube_video(url)

extract.extract_audio()

client = AzureOpenAI(
    api_key= OPENAI_API_KEY,
    azure_endpoint=AZURE_ENDPOINT,
    api_version=OPENAI_VERSION,
)

extract.transcribe_audio_1(client)
